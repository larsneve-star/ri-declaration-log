#!/usr/bin/env python3
"""
Record guard for the RI Declaration public log.

Reads the git history of this repository and reports, without changing anything:
  1. every file that was ever deleted or renamed,
  2. every later edit to a file that should stay frozen once committed
     (answers, baselines, prompts, compiled parts, compile prompts and replies,
     readings, procedures),
  3. every change to a round's LOG.md that removed or rewrote a line
     (the log is meant to grow by addition only),
  4. every file in the repository that no LOG.md mentions, neither by name
     nor by SHA-256.
For 1 to 3 it says whether the commit is mentioned in any LOG.md (by its
7-character commit id). Something that is not mentioned is not necessarily
wrong; it is something a human should look at.

Usage (from the repository root, with full history):
    python3 tools/guard.py > guard-report.md

Written by Claude at the curator's request. Claude is one of the six
answerers in round 4.3. Standard library only, so that it can be read in full.
"""
import fnmatch
import glob
import hashlib
import os
import subprocess
from datetime import datetime, timezone

FROZEN = [
    'baseline/*.txt', 'baseline/*.docx',
    'round-*/answers/*.md',
    'round-*/PROMPT-*.md',
    'round-*/COMPILE-*.md',
    'round-*/READING-*.md',
    'round-*/compile-*/*',
    'PROCEDURE-*.md',
]
NOT_FROZEN = ['round-*/answers/_TEMPLATE.md']
IGNORE_UNLOGGED = ['tools/*', '.github/*', 'README.md', 'RULES.md',
                   'round-*/LOG.md', 'round-*/answers/_TEMPLATE.md', 'LICENSE*']


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True,
                          check=True).stdout


def utc(iso):
    return datetime.fromisoformat(iso).astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')


def match(path, pats):
    return any(fnmatch.fnmatch(path, p) for p in pats)


def log_text():
    return '\n'.join(open(p, encoding='utf-8', errors='replace').read()
                     for p in sorted(glob.glob('round-*/LOG.md')))


def commits():
    out = git('log', '--reverse', '--format=%H%x09%cI%x09%s')
    return [l.split('\t', 2) for l in out.strip().split('\n') if l]


def changes(sha):
    out = git('show', '--format=', '--name-status', '-M', sha)
    rows = []
    for l in out.strip().split('\n'):
        if l:
            parts = l.split('\t')
            rows.append((parts[0][0], parts[1:]))
    return rows


def main():
    logt = log_text()
    seen = set()
    deleted, edited, logchanges = [], [], []

    for sha, iso, subj in commits():
        short = sha[:7]
        mentioned = 'yes' if short in logt else 'NO'
        for status, paths in changes(sha):
            if status == 'D':
                deleted.append((utc(iso), short, 'deleted', paths[0], mentioned))
            elif status == 'R':
                deleted.append((utc(iso), short, 'renamed', f'{paths[0]} → {paths[1]}', mentioned))
                seen.add(paths[1])
            elif status == 'M':
                p = paths[0]
                if match(p, FROZEN) and not match(p, NOT_FROZEN) and p in seen:
                    edited.append((utc(iso), short, p, mentioned))
                if fnmatch.fnmatch(p, 'round-*/LOG.md'):
                    diff = git('show', '--format=', '-U0', sha, '--', p)
                    added = {l[1:].strip() for l in diff.split('\n')
                             if l.startswith('+') and not l.startswith('+++')}
                    # A line that is removed and added back unchanged (for example
                    # when a newline is added at the end of the file) is not a change.
                    removed = [l[1:] for l in diff.split('\n')
                               if l.startswith('-') and not l.startswith('---')
                               and l[1:].strip() and l[1:].strip() not in added]
                    if removed:
                        logchanges.append((utc(iso), short, p, removed))
            for p in paths:
                seen.add(p)

    print('# Record guard\n')
    print(f'Generated {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} '
          f'at commit {git("rev-parse", "--short=7", "HEAD").strip()}.\n')
    print('"In log" means the 7-character commit id appears in a LOG.md. '
          '"NO" is not proof of wrongdoing; it marks something a human should look at.\n')

    print(f'## 1. Files deleted or renamed ({len(deleted)})\n')
    print('| Time | Commit | What | Path | In log |\n|---|---|---|---|---|')
    for r in deleted:
        print('| ' + ' | '.join(f'`{r[1]}`' if i == 1 else str(x) for i, x in enumerate(r)) + ' |')

    print(f'\n## 2. Frozen files edited after their first commit ({len(edited)})\n')
    print('Prompts may be edited before the freeze; everything else should not change.\n')
    print('| Time | Commit | Path | In log |\n|---|---|---|---|')
    for r in edited:
        print(f'| {r[0]} | `{r[1]}` | {r[2]} | {r[3]} |')

    print(f'\n## 3. LOG.md changes that removed or rewrote a line ({len(logchanges)})\n')
    print('The log should only grow. Filling in a table row counts here too, '
          'because the empty row is rewritten.\n')
    for t, short, p, removed in logchanges:
        print(f'<details><summary>{t} · <code>{short}</code> · {p} · '
              f'{len(removed)} line(s)</summary>\n')
        for l in removed:
            print(f'    {l[:300]}')
        print('\n</details>\n')

    files = [f for f in git('ls-files').strip().split('\n') if f]
    unlogged = []
    for f in files:
        if match(f, IGNORE_UNLOGGED):
            continue
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest()
        if h not in logt and os.path.basename(f) not in logt and f not in logt:
            unlogged.append(f)
    print(f'\n## 4. Files not mentioned in any LOG.md ({len(unlogged)})\n')
    print('Neither the file name nor its SHA-256 appears in a round log.\n')
    for f in unlogged:
        print(f'- {f}')


if __name__ == '__main__':
    main()
