#!/usr/bin/env python3
"""
Runs every check and prints one report (Markdown) to standard output.
Full reports are also written to the folder given as the first argument.

  python3 tools/run_all.py reports

Used by .github/workflows/record-check.yml, so that the checks run on
GitHub's machines after every change, and the result is public on the
repository's Actions page. Nobody in the project presses the button.
Written by Claude at the curator's request. Standard library only.
"""
import os
import re
import subprocess
import sys

out = sys.argv[1] if len(sys.argv) > 1 else 'reports'
os.makedirs(out, exist_ok=True)
here = os.path.dirname(os.path.abspath(__file__))


def run(args):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    return r.stdout + (f'\n\n```\n{r.stderr}\n```\n' if r.returncode else '')


print('# RI Declaration: automatic record check\n')
print('This page is produced by a machine (GitHub Actions) after every change to the '
      'repository. It compares versions line by line (Annex H) and reads the history '
      'for deletions, edits and log changes. It judges nothing: every "altered", '
      '"missing" or "NO" is something a human verifier must look at.\n')

print('## Version comparisons\n')
for line in open(os.path.join(here, 'check-pairs.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    label, old, new = [p.strip() for p in line.split('|')]
    files = [old, *new.split()]
    missing = [f for f in files if not os.path.exists(f)]
    print(f'### {label}\n')
    if missing:
        print('Not run. File(s) not found: ' + ', '.join(f'`{m}`' for m in missing) + '\n')
        continue
    rep = run([os.path.join(here, 'verify.py'), *files])
    name = re.sub(r'[^0-9A-Za-z.]+', '_', label)
    open(os.path.join(out, f'compare_{name}.md'), 'w', encoding='utf-8').write(rep)
    head, _, rest = rep.partition('## Altered lines')
    print(head.replace('# Annex H check\n', '').replace('\n## ', '\n#### '))
    print('<details><summary>Altered and missing lines</summary>\n')
    body = '## Altered lines' + rest
    body = re.sub(r'(?m)^### ', '##### ', body)
    print(re.sub(r'(?m)^## ', '#### ', body))
    print('\n</details>\n')

print('## Record guard\n')
rep = run([os.path.join(here, 'guard.py')])
open(os.path.join(out, 'guard.md'), 'w', encoding='utf-8').write(rep)
print(rep.replace('# Record guard\n', '').replace('\n## ', '\n### '))
