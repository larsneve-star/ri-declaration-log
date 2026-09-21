#!/usr/bin/env python3
"""
The log robot for the RI Declaration public log.

It writes the routine lines of a round's LOG.md, so that the curator does not
have to type times, hashes or file names, and so that those lines come from a
machine instead of from a participant. It only ever ADDS lines, under the
heading "## Machine log" at the end of the round's LOG.md. It never edits or
removes a line, and it never touches an answer.

Commands (run by the GitHub workflows in .github/workflows/robot-*.yml):

  freeze   ROUND BASELINE PROMPT [ATTACHMENTS] [DEADLINE]
           Hashes the files, writes the freeze entry and the deadline, and
           creates round-ROUND/STATE.json. DEADLINE is "YYYY-MM-DD HH:MM" in UTC,
           or a number of hours from now (default 72).
  sent     MODEL WHAT [DEVIATION]
           Logs that the curator sent the round to MODEL, with the time.
  register BEFORE AFTER
           Called after every push. Logs every file added, and warns about
           every file deleted, renamed or edited that should stay frozen.
           When a compiled part is added, it compares the compiled text with
           the round's baseline at once and logs the counts.
  tick     Called every hour. Releases an open round when all six have
           answered or the deadline has passed, and logs any missing answers.

Written by Claude at the curator's request. Claude is one of the six
answerers in round 4.3, so the code is kept short and public. Standard
library only.
"""
import fnmatch
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

MODELS = {  # file name stem (lower case) -> model name
    'claude': 'Claude', 'gemini': 'Gemini', 'chatgpt': 'ChatGPT',
    'deepseek': 'DeepSeek', 'grok': 'Grok', 'meta-ai': 'Meta AI', 'meta': 'Meta AI',
}
SIX = ['Claude', 'Gemini', 'ChatGPT', 'DeepSeek', 'Grok', 'Meta AI']
FROZEN = ['baseline/*.txt', 'baseline/*.docx', 'round-*/answers/*.md',
          'round-*/PROMPT-*.md', 'round-*/COMPILE-*.md', 'round-*/READING-*.md',
          'round-*/compile-*/*', 'round-*/checks/*', 'PROCEDURE-*.md']
NOT_FROZEN = ['round-*/answers/_TEMPLATE.md']
SKIP = ['round-*/LOG.md', 'round-*/STATE.json']
HEADING = '## Machine log'
HERE = os.path.dirname(os.path.abspath(__file__))


# ---------- helpers ----------

def now():
    return datetime.now(timezone.utc)


def fmt(t):
    return t.strftime('%Y-%m-%d %H:%M UTC')


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True,
                          check=True).stdout.strip()


def match(p, pats):
    return any(fnmatch.fnmatch(p, x) for x in pats)


def rounds():
    return sorted(glob.glob('round-*/'), key=lambda d: [int(x) for x in
                  re.findall(r'\d+', d)])


def state(rdir):
    p = os.path.join(rdir, 'STATE.json')
    return json.load(open(p)) if os.path.exists(p) else None


def save_state(rdir, st):
    json.dump(st, open(os.path.join(rdir, 'STATE.json'), 'w'), indent=2)


def current_round():
    """The newest open round, or else the newest round."""
    rs = rounds()
    for r in reversed(rs):
        st = state(r)
        if st and st.get('status') == 'open':
            return r
    return rs[-1] if rs else None


def round_of(path):
    m = re.match(r'(round-[^/]+)/', path)
    return m.group(1) + '/' if m else current_round()


def append(rdir, lines):
    """Add lines under '## Machine log' at the end of the round's LOG.md."""
    p = os.path.join(rdir, 'LOG.md')
    text = open(p, encoding='utf-8').read() if os.path.exists(p) else \
        f'# Round log: {rdir.strip("/")}\n\nAll times UTC.\n'
    if HEADING not in text:
        text = text.rstrip('\n') + f'\n\n{HEADING}\n\n' \
            'Lines below are written by the log robot (tools/robot.py), not by a person. ' \
            'It only adds lines.\n\n'
    text = text.rstrip('\n') + ('\n\n' if text.rstrip().endswith('It only adds lines.') else '\n') + '\n'.join(f'- {l}' for l in lines) + '\n'
    open(p, 'w', encoding='utf-8').write(text)


def model_of(path):
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    return MODELS.get(stem)


def commit_time(path, rev):
    iso = git('log', '-1', '--format=%cI', rev, '--', path)
    return fmt(datetime.fromisoformat(iso).astimezone(timezone.utc)) if iso else fmt(now())


# ---------- commands ----------

def freeze(rnd, baseline, prompt, attachments='', deadline=''):
    rdir = f'round-{rnd}/'
    if state(rdir):
        sys.exit(f'{rdir}STATE.json already exists; round {rnd} is already frozen.')
    files = [baseline, prompt] + [a.strip() for a in attachments.split(',') if a.strip()]
    for f in files:
        if not os.path.exists(f):
            sys.exit(f'File not found: {f}')
    t = now()
    if re.fullmatch(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', deadline.strip()):
        dl = datetime.strptime(deadline.strip(), '%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
    else:
        dl = t + timedelta(hours=float(deadline or 72))
    os.makedirs(rdir, exist_ok=True)
    hashes = {f: sha(f) for f in files}
    nxt = ''
    rot = os.path.join(HERE, 'rotation.txt')
    if os.path.exists(rot):
        for l in open(rot, encoding='utf-8'):
            parts = l.split('#')[0].split(None, 1)
            if len(parts) == 2 and parts[0] == rnd:
                nxt = parts[1].strip()
    save_state(rdir, {'round': rnd, 'status': 'open', 'frozen_at': fmt(t),
                      'deadline': fmt(dl), 'baseline': baseline, 'prompt': prompt,
                      'hashes': hashes})
    lines = [f'{fmt(t)}: FREEZE of round {rnd}. Deadline: {fmt(dl)}.']
    lines += [f'{fmt(t)}: Frozen file `{f}` SHA-256 `{h}`.' for f, h in hashes.items()]
    if nxt:
        lines.append(f'{fmt(t)}: Under the rotation list in `tools/rotation.txt`, the compiler '
                     f'of {rnd} is {nxt}. The rotation is proposal PR20 until it is adopted; '
                     'a skip must be logged with its reason.')
    append(rdir, lines)


def sent(model, what, deviation=''):
    rdir = current_round()
    t = fmt(now())
    line = f'{t}: SENT to {model}: {what}.'
    if deviation.strip():
        line += f' Deviation: {deviation.strip()}'
    st = state(rdir)
    if st and st.get('status') != 'open':
        line += ' NOTE: the round is not open.'
    append(rdir, [line])


def register(before, after):
    if not before or set(before) == {'0'}:
        rng = [f'{after}~1..{after}']
    else:
        rng = [f'{before}..{after}']
    out = git('log', '--reverse', '--format=%H', *rng)
    per_round = {}
    compiled = set()
    for c in [x for x in out.split('\n') if x]:
        short = c[:7]
        for row in git('show', '--format=', '--name-status', '-M', c).split('\n'):
            if not row:
                continue
            parts = row.split('\t')
            status, paths = parts[0][0], parts[1:]
            p = paths[-1]
            if match(p, SKIP) or p.startswith('.github/'):
                continue
            rdir = round_of(p)
            t = commit_time(p, c)
            L = per_round.setdefault(rdir, [])
            if status == 'A' and os.path.exists(p):
                what = 'Answer' if '/answers/' in p and not p.endswith('_TEMPLATE.md') else 'File'
                m = model_of(p) if what == 'Answer' else None
                extra = f' from {m}' if m else ''
                L.append(f'{t}: {what}{extra} added: `{p}` SHA-256 `{sha(p)}` (commit {short}).')
                if re.search(r'/compile-[^/]+/PART-', p):
                    compiled.add(rdir)
            elif status == 'R':
                L.append(f'{t}: WARNING: renamed `{paths[0]}` → `{paths[1]}` (commit {short}). '
                         'A person should say why in the notes.')
            elif status == 'D':
                L.append(f'{t}: WARNING: deleted `{p}` (commit {short}). It stays in the history. '
                         'A person should say why in the notes.')
            elif status == 'M' and match(p, FROZEN) and not match(p, NOT_FROZEN):
                L.append(f'{t}: WARNING: frozen file edited: `{p}`, new SHA-256 `{sha(p)}` '
                         f'(commit {short}). A person should say why in the notes.')
    for rdir in compiled:
        per_round.setdefault(rdir, []).extend(compile_check(rdir, after[:7]))
    for rdir, lines in per_round.items():
        if lines:
            append(rdir, lines)


def latest_parts(rdir):
    """Newest revision of each numbered part: PART-02-r2.md beats PART-02.md."""
    best = {}
    for p in glob.glob(os.path.join(rdir, 'compile-*', 'PART-*.md')):
        m = re.match(r'PART-(\d+)(?:-r(\d+))?\.md$', os.path.basename(p))
        if m:
            n, r = int(m.group(1)), int(m.group(2) or 1)
            if n not in best or r > best[n][0]:
                best[n] = (r, p)
    return [best[n][1] for n in sorted(best)]


def baseline_of(rdir):
    st = state(rdir)
    if st and st.get('baseline'):
        return st['baseline']
    m = re.match(r'round-(\d+)\.(\d+)', rdir)
    if m:
        cand = f'baseline/RI-Declaration-{m.group(1)}-{int(m.group(2)) - 1}-EN.txt'
        if os.path.exists(cand):
            return cand
    return None


def compile_check(rdir, short):
    base, parts = baseline_of(rdir), latest_parts(rdir)
    if not base or not parts:
        return []
    os.makedirs(os.path.join(rdir, 'checks'), exist_ok=True)
    rep = subprocess.run([sys.executable, os.path.join(HERE, 'verify.py'), base, *parts],
                         capture_output=True, text=True).stdout
    out = os.path.join(rdir, 'checks', f'compile-check-{short}.md')
    open(out, 'w', encoding='utf-8').write(rep)
    nums = dict(re.findall(r'\| (Present, identical[^|]*|Present, differs[^|]*|Altered[^|]*|'
                           r'Missing[^|]*) \| (\d+) \|', rep))
    summary = ', '.join(f'{k.split(" (")[0].strip()}: {v}' for k, v in nums.items())
    return [f'{fmt(now())}: COMPILE CHECK of the newest parts '
            f'({", ".join("`" + os.path.basename(p) + "`" for p in parts)}) against `{base}`. '
            f'{summary}. Full report: `{out}`. Every altered or missing line must be named in '
            'Annex D; a person checks that.']


def tick():
    for rdir in rounds():
        st = state(rdir)
        if not st or st.get('status') != 'open':
            continue
        answers = {}
        for p in glob.glob(os.path.join(rdir, 'answers', '*.md')):
            m = model_of(p)
            if m:
                answers[m] = p
        dl = datetime.strptime(st['deadline'], '%Y-%m-%d %H:%M UTC').replace(tzinfo=timezone.utc)
        if len(answers) < len(SIX) and now() < dl:
            continue
        t = fmt(now())
        why = 'all six have answered' if len(answers) == len(SIX) else 'the deadline has passed'
        lines = [f'{t}: RELEASE of round {st["round"]}, because {why}. The blind period is over.']
        for m in SIX:
            if m in answers:
                lines.append(f'{t}: Released answer from {m}: `{answers[m]}` '
                             f'SHA-256 `{sha(answers[m])}`.')
            else:
                lines.append(f'{t}: MISSING: no answer from {m} by the deadline. '
                             'Silence is not agreement.')
        st['status'] = 'released'
        st['released_at'] = t
        save_state(rdir, st)
        append(rdir, lines)


if __name__ == '__main__':
    cmd, *args = sys.argv[1:] or ['']
    {'freeze': freeze, 'sent': sent, 'register': register, 'tick': tick}.get(
        cmd, lambda *a: sys.exit(__doc__))(*args)
