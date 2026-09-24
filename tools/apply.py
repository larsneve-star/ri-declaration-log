#!/usr/bin/env python3
"""
apply.py — builds a new version of the declaration from the previous one plus a
list of the compiler's insertions. The compiler never retypes the text.

  python3 tools/apply.py INSTRUCTIONS.txt          (check only, writes nothing)
  python3 tools/apply.py INSTRUCTIONS.txt --write  (writes the output file)

Why: three compilations in a row lost text because a model cannot write 190,000
characters into a chat window and tried to shorten instead. Here the baseline is
copied by the machine, byte for byte, and the compiler supplies only what is
added or changed. Losing a passage becomes impossible; every change is named.

FORMAT of the instruction file (plain text, UTF-8):

    BASELINE: baseline/RI-Declaration-4-3-EN.txt
    BASELINE-SHA256: ba24a372...          (must match, or nothing is done)
    OUTPUT: baseline/RI-Declaration-4-4-EN.txt

    --- K1 INSERT-AFTER
    ANCHOR: <one line copied exactly from the baseline, occurring exactly once>
    TEXT:
    <one or more lines to insert>
    END

    --- K2 INSERT-BEFORE
    ANCHOR: <line>
    TEXT:
    <lines>
    END

    --- K3 REPLACE
    ANCHOR: <the line to replace>
    TEXT:
    <the new line or lines>
    END

    --- K4 REPLACE-BLOCK
    FROM: <first line of the block>
    TO: <last line of the block>
    TEXT:
    <the new lines>
    END

    --- K5 APPEND-END
    TEXT:
    <lines added at the end of the file>
    END

Rules the program enforces, before anything is written:
  * the baseline's SHA-256 must match the one declared;
  * every ANCHOR, FROM and TO line must occur exactly once in the baseline,
    otherwise the program stops and names the entry;
  * no line of the baseline is ever deleted except inside a REPLACE or
    REPLACE-BLOCK, and the program prints exactly what those removed;
  * entries are applied to the ORIGINAL line positions, so their order in the
    file does not matter.
It prints a report: every K entry, the line it acts on, and how many lines were
added or removed, plus the SHA-256 of the result.

Written by Claude at the curator's request. Standard library only.
"""
import hashlib
import re
import sys


def die(msg):
    print('STOPPED. Nothing was written.\n' + msg)
    sys.exit(1)


def parse(path):
    text = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    head, entries, cur = {}, [], None
    mode = 'head'
    for raw in text.split('\n'):
        line = raw.rstrip('\n')
        if mode == 'head':
            m = re.match(r'(BASELINE|BASELINE-SHA256|OUTPUT):\s*(.+)$', line.strip())
            if m:
                head[m.group(1)] = m.group(2).strip()
                continue
        m = re.match(r'---\s*(\S+)\s+(INSERT-AFTER|INSERT-BEFORE|REPLACE-BLOCK|REPLACE|APPEND-END)\s*$', line.strip())
        if m:
            if cur:
                entries.append(cur)
            cur = {'id': m.group(1), 'op': m.group(2), 'text': [], 'reading': None}
            mode = 'entry'
            continue
        if cur is None:
            continue
        if cur['reading'] == 'text':
            if line.strip() == 'END':
                cur['reading'] = None
            else:
                cur['text'].append(line)
            continue
        m = re.match(r'(ANCHOR|FROM|TO):\s?(.*)$', line)
        if m:
            cur[m.group(1)] = m.group(2).rstrip()
            continue
        if line.strip() == 'TEXT:':
            cur['reading'] = 'text'
            continue
    if cur:
        entries.append(cur)
    for k in ('BASELINE', 'BASELINE-SHA256', 'OUTPUT'):
        if k not in head:
            die(f'The instruction file has no "{k}:" line.')
    if not entries:
        die('The instruction file contains no entries (no line starting with "--- ").')
    return head, entries


def find(lines, needle, eid, label):
    hits = [i for i, l in enumerate(lines) if l.rstrip() == needle.rstrip()]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        near = [i for i, l in enumerate(lines) if needle.strip()[:40] and needle.strip()[:40] in l]
        hint = f'\n  Closest lines in the baseline: ' + '; '.join(
            f'line {i + 1}: {lines[i][:70]}' for i in near[:3]) if near else ''
        die(f'{eid}: the {label} line is not in the baseline, character for character:\n'
            f'  {needle[:120]}{hint}')
    die(f'{eid}: the {label} line occurs {len(hits)} times in the baseline '
        f'(lines {", ".join(str(h + 1) for h in hits)}). Choose a line that occurs once.\n  {needle[:120]}')


def main():
    if not sys.argv[1:]:
        sys.exit(__doc__)
    head, entries = parse(sys.argv[1])
    write = '--write' in sys.argv[2:]
    try:
        raw = open(head['BASELINE'], 'rb').read()
    except OSError as e:
        die(f'Cannot read the baseline: {e}')
    got = hashlib.sha256(raw).hexdigest()
    if got != head['BASELINE-SHA256'].lower():
        die(f'The baseline is not the declared one.\n  declared: {head["BASELINE-SHA256"]}\n  actual:   {got}')
    lines = raw.decode('utf-8').replace('\r\n', '\n').split('\n')

    plan, appended = [], []
    for e in entries:
        op, eid = e['op'], e['id']
        if op == 'APPEND-END':
            appended.append((eid, e['text']))
            plan.append((len(lines), 0, eid, op, e['text']))
            continue
        if op == 'REPLACE-BLOCK':
            if 'FROM' not in e or 'TO' not in e:
                die(f'{eid}: REPLACE-BLOCK needs both a FROM: and a TO: line.')
            a = find(lines, e['FROM'], eid, 'FROM')
            b = find(lines, e['TO'], eid, 'TO')
            if b < a:
                die(f'{eid}: the TO line (line {b + 1}) comes before the FROM line (line {a + 1}).')
            plan.append((a, b - a + 1, eid, op, e['text']))
            continue
        if 'ANCHOR' not in e:
            die(f'{eid}: {op} needs an ANCHOR: line.')
        i = find(lines, e['ANCHOR'], eid, 'ANCHOR')
        if op == 'INSERT-AFTER':
            plan.append((i + 1, 0, eid, op, e['text']))
        elif op == 'INSERT-BEFORE':
            plan.append((i, 0, eid, op, e['text']))
        else:  # REPLACE
            plan.append((i, 1, eid, op, e['text']))

    plan.sort(key=lambda p: p[0])
    for (a1, n1, id1, *_), (a2, n2, id2, *_) in zip(plan, plan[1:]):
        if n1 and a1 + n1 > a2:
            die(f'{id1} and {id2} act on the same lines. Each line may be changed by one entry only.')

    out, prev, report = [], 0, []
    for start, n, eid, op, text in plan:
        out += lines[prev:start]
        removed = lines[start:start + n]
        out += text
        prev = start + n
        report.append((eid, op, start + 1, len(text), removed))
    out += lines[prev:]
    result = '\n'.join(out)
    if not result.endswith('\n'):
        result += '\n'

    print(f'# Building {head["OUTPUT"]}\n')
    print(f'Baseline: {head["BASELINE"]} (SHA-256 verified: {got})')
    print(f'Baseline lines: {len(lines)}   Result lines: {len(out)}\n')
    print('| Entry | What | At line | Lines added | Lines removed |')
    print('|---|---|---|---|---|')
    for eid, op, at, added, removed in report:
        print(f'| {eid} | {op} | {at} | {added} | {len(removed)} |')
    rem = [(eid, r) for eid, op, at, added, removed in report for r in removed]
    print(f'\nLines of the baseline removed or replaced: {len(rem)}')
    for eid, r in rem:
        print(f'  {eid}: {r[:150]}')
    print(f'\nSHA-256 of the result: {hashlib.sha256(result.encode()).hexdigest()}')
    if write:
        open(head['OUTPUT'], 'w', encoding='utf-8').write(result)
        print(f'\nWritten: {head["OUTPUT"]}')
    else:
        print('\nCheck only. Run again with --write to create the file.')


if __name__ == '__main__':
    main()
