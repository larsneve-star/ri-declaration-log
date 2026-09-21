#!/usr/bin/env python3
"""
Annex H check for the RI Declaration: compare an earlier version with a later one.

Usage:
    python3 verify.py EARLIER.txt LATER.txt [LATER_PART_2.txt ...]  > report.md

If the later version is delivered in parts, list the parts in order after the
first one. They are joined exactly as Annex H says: in order, UTF-8, LF line
endings, nothing added at the joins.

What it does, following Annex H section III:
  For every non-empty line of the earlier version:
    1. is it present in the later version?
    2. if present, is it identical, character for character?
    3. if not, the report lists the old line and the most similar new line,
       so a human can look in Annex D for the entry that names the change.
  It also prints the SHA-256 of every input and the counts listed in
  Annex H section IV.

Two levels are reported:
  STRICT      - character for character, exactly as Annex H asks.
  FORMAT-ONLY - ignores list bullets, heading marks (#), bold marks (**),
                backslashes and link brackets that appear when text is copied
                out of a chat window. A line that passes here but not in STRICT
                differs only in formatting.

This script was written by Claude, one of the six answerers in round 4.3, at
the curator's request. It is short on purpose, so that the verifier can read
all of it. The verifier can also check the result with any ordinary diff tool.
Standard library only.
"""
import difflib
import hashlib
import re
import sys


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fmt(line: str) -> str:
    s = line.strip()
    s = re.sub(r'^(#+\s*|[-*+]\s+)', '', s)
    s = s.replace('**', '').replace('\\', '')
    s = re.sub(r'\[(https?://[^\]]+)\]\(\1\)', r'\1', s)
    return re.sub(r'\s+', ' ', s).strip()


def lines(text: str):
    out = []
    for l in text.split('\n'):
        t = l.strip()
        if not t or re.fullmatch(r'[=\-_*]{3,}', t):
            continue
        if re.fullmatch(r'PART \d+ OF \d+.*', t):
            continue
        out.append(t)
    return out


def counts(text: str) -> dict:
    ls = [l.strip() for l in text.split('\n')]
    c = lambda pat: sum(1 for l in ls if re.search(pat, fmt(l)))
    return {
        'Articles (§ headings)': c(r'^§\d+[ab]? [A-Z]'),
        'Falsification attempts': c(r'^\[Falsification attempt\]'),
        'Outcomes': c(r'^\[Outcome\]'),
        'Origin lines': c(r'Origin:'),
        'C-entry headings (C1, C2 ...)': len({m.group(1) for l in ls
                                              for m in [re.match(r'^C(\d+) ', fmt(l))] if m}),
        'Å-numbers': len({m.group(1) for l in ls
                          for m in [re.match(r'^Å(\d+) ', fmt(l))] if m}),
        'PR-numbers': len({m.group(1) for l in ls
                           for m in [re.match(r'^PR(\d+)\. ', fmt(l))] if m}),
        'Annex headings': len({m.group(1) for l in ls
                               for m in [re.match(r'^ANNEX ([A-Z]) ', fmt(l))] if m}),
    }


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    old_b = open(sys.argv[1], 'rb').read()
    part_b = [open(p, 'rb').read() for p in sys.argv[2:]]
    new_b = b''.join(part_b)
    old = old_b.decode('utf-8').replace('\r\n', '\n')
    new = new_b.decode('utf-8').replace('\r\n', '\n')

    print('# Annex H check\n')
    print('## Inputs (SHA-256)\n')
    print(f'- Earlier: `{sys.argv[1]}` `{sha(old_b)}`')
    for p, b in zip(sys.argv[2:], part_b):
        print(f'- Later: `{p}` `{sha(b)}`')
    if len(part_b) > 1:
        print(f'- Later, parts joined in the order above: `{sha(new_b)}`')

    ol, nl = lines(old), lines(new)
    strict = set(nl)
    fmt_set = {fmt(l) for l in nl}
    fmt_list = list(fmt_set)
    present, fmt_only, altered, missing = [], [], [], []
    for l in ol:
        if l in strict:
            present.append(l)
        elif fmt(l) in fmt_set:
            fmt_only.append(l)
        else:
            m = difflib.get_close_matches(fmt(l), fmt_list, n=1, cutoff=0.6)
            (altered if m else missing).append((l, m[0] if m else None))

    print('\n## Result\n')
    print(f'Non-empty lines in the earlier version: {len(ol)}\n')
    print('| | Lines |\n|---|---|')
    print(f'| Present, identical character for character (STRICT) | {len(present)} |')
    print(f'| Present, differs only in formatting (FORMAT-ONLY) | {len(fmt_only)} |')
    print(f'| Altered (a similar line exists) | {len(altered)} |')
    print(f'| Missing (no similar line) | {len(missing)} |')

    print('\n## Counts (Annex H section IV)\n')
    co, cn = counts(old), counts(new)
    print('| | Earlier | Later |\n|---|---|---|')
    for k in co:
        print(f'| {k} | {co[k]} | {cn[k]} |')
    print('\nThe counts are found by pattern and are a help, not proof. '
          'Compare them with the counts the versions state about themselves.')

    print('\n## Altered lines\n')
    print('For each: is the change named in Annex D? Write the entry number, or "not logged".\n')
    for i, (o, n) in enumerate(altered, 1):
        print(f'### A{i}\n\nOLD: {o}\n\nNEW: {n}\n\nAnnex D entry: ______\n')

    print('\n## Missing lines\n')
    print('For each: is the removal named in Annex D? Write the entry number, or "not logged".\n')
    for i, (o, _) in enumerate(missing, 1):
        print(f'### M{i}\n\nOLD: {o}\n\nAnnex D entry: ______\n')


if __name__ == '__main__':
    main()
