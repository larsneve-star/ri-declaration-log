#!/usr/bin/env python3
"""
Budbringeren: builds the public news site for the RI Declaration log.

  python3 tools/news.py site      (writes site/index.html)

Two layers, kept apart on purpose:
  FACTS  are read by the machine from the repository: the round's STATE.json,
         the machine lines in its LOG.md, the prompt and the answer files.
         Nobody writes them by hand.
  STORY  is a plain-language account of the round, written by one named
         writer per round (news/round-X.Y-DA.md). The writer rotates, so no
         single model always tells the story. The page always shows who wrote it.
         A round may have more than one story: news/round-X.Y-DA-2.md and so on
         are shown after the first, each with its own writer and a link to the file.

Written by Claude at the curator's request. Claude is one of the six
answerers, so the facts layer contains no judgement and the story layer is
never written by the same model every round. Standard library only.
"""
import glob
import html
import json
import os
import re
import sys

REPO = os.environ.get('GITHUB_REPOSITORY', 'larsneve-star/ri-declaration-log')
GH = f'https://github.com/{REPO}'
SIX = ['ChatGPT', 'Claude', 'DeepSeek', 'Gemini', 'Grok', 'Meta AI']
STEM = {'chatgpt': 'ChatGPT', 'claude': 'Claude', 'deepseek': 'DeepSeek',
        'gemini': 'Gemini', 'grok': 'Grok', 'meta-ai': 'Meta AI', 'meta': 'Meta AI'}
E = html.escape


def rounds():
    ds = [d.rstrip('/') for d in glob.glob('round-*/')]
    return sorted(ds, key=lambda d: [int(x) for x in re.findall(r'\d+', d)], reverse=True)


def read(p):
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def machine_lines(log):
    part = log.split('## Machine log', 1)
    return re.findall(r'^- (\d{4}-\d\d-\d\d \d\d:\d\d UTC): (.*)$', part[1], re.M) if len(part) > 1 else []


def targets(prompt):
    m = re.search(r'B\. FALSIFICATION\s*\n(.*?)\n\s*\n', prompt, re.S)
    if not m:
        return []
    return [l[2:].strip() for l in m.group(1).split('\n') if l.startswith('- ')]


def md(text):
    """Very small Markdown: headings, bullets, bold, italics, links, paragraphs."""
    out, para, items = [], [], []

    def inline(s):
        s = E(s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*(?!\*)(.+?)\*', r'<em>\1</em>', s)
        s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', s)
        return s

    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()
        if items:
            out.append('<ul>' + ''.join(f'<li>{inline(i)}</li>' for i in items) + '</ul>')
            items.clear()
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            flush()
        elif s.strip('-') == '' and len(s) >= 3:
            flush()
            out.append('<hr>')
        elif s.startswith('#'):
            flush()
            out.append(f'<h4>{inline(s.lstrip("#").strip())}</h4>')
        elif s.startswith(('- ', '* ')):
            if para:
                flush()
            items.append(s[2:])
        else:
            if items:
                flush()
            para.append(s)
    flush()
    return '\n'.join(out)


def story(rnd):
    """All stories of a round: news/round-X.Y-DA.md, then news/round-X.Y-DA-2.md and so on."""
    out = []
    files = [f'news/{rnd}-DA.md'] + sorted(glob.glob(f'news/{rnd}-DA-*.md'),
                                           key=lambda x: [int(n) for n in re.findall(r'\d+', x)])
    for p in files:
        t = read(p)
        if not t.strip():
            continue
        # An optional title line, then "Key: value" lines, then an empty line.
        # Nothing is dropped: the title and the header lines are shown as written.
        meta, body, title, lines = {}, t, '', []
        head = re.match(r'(?:([^\n:]+)\n)?((?:[A-Za-zÆØÅæøå ]+:.*\n)+)\n', t)
        if head:
            title = (head.group(1) or '').strip()
            lines = head.group(2).strip().split('\n')
            for l in lines:
                k, v = l.split(':', 1)
                meta[k.strip().lower()] = v.strip()
            body = t[head.end():]
        meta['_title'], meta['_lines'] = title, lines
        out.append((meta, body, p))
    return out


def round_facts(rdir):
    st = {}
    if os.path.exists(f'{rdir}/STATE.json'):
        st = json.load(open(f'{rdir}/STATE.json'))
    log = read(f'{rdir}/LOG.md')
    ml = machine_lines(log)
    sent, got = {}, {}
    for t, l in ml:
        m = re.match(r'SENT to ([^:]+):', l)
        if m:
            sent.setdefault(m.group(1), t)
        m = re.match(r'Answer from ([A-Za-z ]+) added', l)
        if m:
            got[m.group(1)] = t
    answers = {}
    for p in sorted(glob.glob(f'{rdir}/answers/*.md')):
        name = STEM.get(os.path.splitext(os.path.basename(p))[0].lower())
        if name:
            txt = read(p)
            answers[name] = (p, bool(re.search(r'^\W*MODEL\W*:', txt, re.M | re.I)))
    released = st.get('released_at')
    if not released:
        m = re.search(r'Released at:\s*(\d{4}-\d\d-\d\d \d\d:\d\d UTC)', log)
        released = m.group(1) if m else None
    comp = None
    m = re.search(r'the compiler of [\d.]+ is ([A-Za-z ]+)\.', log)
    if m:
        comp = m.group(1).strip()
    m2 = re.search(r'Compiler of [\d.]+: ([A-Za-z ]+)\.', log)
    if not comp and m2:
        comp = m2.group(1).strip()
    if not st.get('baseline'):
        m = re.search(r'(baseline/RI-Declaration-[\w-]+\.txt)', log)
        if m:
            st['baseline'] = m.group(1)
    return dict(state=st, sent=sent, got=got, answers=answers, released=released,
                compiler=comp, targets=targets(read(f'{rdir}/PROMPT-EN.md')), machine=bool(ml))


def round_html(rdir):
    rnd = rdir.replace('round-', '')
    f = round_facts(rdir)
    st = f['state']
    status = ('Frigivet ' + f['released']) if f['released'] else ('Åben · frist ' + st['deadline']) if st.get('deadline') else 'Åben'
    cls = 'done' if f['released'] else 'open'
    rows = []
    for m in SIX:
        a = f['answers'].get(m)
        if a and a[1]:
            s, c = 'Svarede', 'ok'
        elif a:
            s, c = 'Sagde nej / svarede ikke på opgaven', 'warn'
        else:
            s, c = ('Mangler' if not f['released'] else 'Intet svar'), 'none'
        link = f'<a href="{GH}/blob/main/{a[0]}">læs</a>' if a else ''
        rows.append(f'<tr><th scope="row">{m}</th><td><span class="tag {c}">{s}</span></td>'
                    f'<td class="num">{E(f["sent"].get(m, "–"))}</td><td class="num">{E(f["got"].get(m, "–"))}</td><td>{link}</td></tr>')
    tg = ''.join(f'<li>{E(t)}</li>' for t in f['targets'])
    stories = story(rdir)
    parts = []
    for i, (meta, body, path) in enumerate(stories, 1):
        audio = meta.get('lyd') or meta.get('audio')
        aud = (f'<p class="audio"><a href="{E(audio)}">Lyt til lydoversigten</a> '
               f'<span class="fine">({E(meta.get("lyd lavet med", "lavet med et AI-værktøj"))})</span></p>') if audio else ''
        num = f'Historie {i} · ' if len(stories) > 1 else ''
        top = (f'<h4>{E(meta["_title"])}</h4>' if meta['_title'] else '') + \
            (('<p class="fine">' + '<br>'.join(E(l) for l in meta['_lines']) + '</p>') if meta['_lines'] else '')
        writer = meta.get('skrevet af', 'ukendt')
        parts.append(f'<div class="story"><p class="byline">{num}Fortalt af <strong>{E(writer)}</strong>'
                     f'{" · " + E(meta["dato"]) if meta.get("dato") else ""} · '
                     f'<a href="{GH}/blob/main/{E(path)}">original</a></p>{aud}'
                     f'{top}{md(body)}'
                     f'<p class="fine">Historien er én skribents udlægning og kan angribes som alt andet i projektet. '
                     f'Fakta ovenfor er læst af maskinen.</p></div>')
        # Replies to story 1 are in news/round-X.Y-replies/, to story N in news/round-X.Y-DA-N-replies/.
        rdir_replies = f'news/{rdir}-replies' if i == 1 else f'news/{rdir}-DA-{i}-replies'
        reps = []
        for p in sorted(glob.glob(f'{rdir_replies}/*.md')):
            who = STEM.get(os.path.splitext(os.path.basename(p))[0].lower(), os.path.splitext(os.path.basename(p))[0])
            reps.append(f'<div class="reply"><p class="byline">Genmæle fra <strong>{E(who)}</strong></p>{md(read(p))}</div>')
        if reps:
            parts.append(f'<h3>Genmæle til historien fra {E(writer)}</h3><p class="fine">De andre modeller har fået historien at se og kunne svare, '
                         'hvis de ikke følte sig retvisende gengivet. Deres svar står her uændret.</p>' + ''.join(reps))
    if parts:
        story_html = ''.join(parts)
    else:
        story_html = '<div class="story empty"><p>Historien om denne runde er ikke skrevet endnu. Den skrives af den næste skribent på listen, når runden er frigivet.</p></div>'
    note = '' if f['sent'] else '<p class="fine">Denne runde blev ført i hånden, før log-robotten kom, så tiderne står kun i selve loggen.</p>'
    return f'''
<article class="round" id="{E(rdir)}">
  <header class="rhead">
    <h2>Runde {E(rnd)}</h2>
    <span class="status {cls}">{E(status)}</span>
  </header>
  <dl class="facts">
    <div><dt>Tekst, der blev angrebet</dt><dd>{E(os.path.basename(st.get("baseline", "")) or "se loggen")}</dd></div>
    <div><dt>Samler næste version</dt><dd>{E(f["compiler"] or "–")}</dd></div>
    <div><dt>Log</dt><dd><a href="{GH}/blob/main/{rdir}/LOG.md">åbn loggen</a></dd></div>
  </dl>
  {f'<div class="targets"><h3>Sat til angreb</h3><ul>{tg}</ul></div>' if tg else ''}
  <div class="tablewrap"><table>
    <thead><tr><th scope="col">Model</th><th scope="col">Hvad skete der</th><th scope="col">Sendt</th><th scope="col">Svar modtaget</th><th scope="col"></th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table></div>
  {note}
  <h3>Historien</h3>
  {story_html}
</article>'''


CSS = '''
:root{--ground:#f5f3ee;--paper:#fffdf8;--ink:#23201b;--muted:#6b645a;--line:#ddd6ca;--accent:#8a3b12;
--ok:#2f6b3f;--ok-bg:#e4efe4;--warn:#8a5a0e;--warn-bg:#f6ead2;--none:#6b645a;--none-bg:#ece7de}
@media (prefers-color-scheme:dark){:root{--ground:#17150f;--paper:#201d17;--ink:#ece6da;--muted:#a79f92;--line:#3a352c;
--accent:#e0925f;--ok:#8cc79a;--ok-bg:#1f3325;--warn:#e0b060;--warn-bg:#3a2e17;--none:#a79f92;--none-bg:#2b2720}}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font:18px/1.6 Georgia,"Iowan Old Style","Times New Roman",serif;padding:32px 16px 64px}
.wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:36px}
h1,h2,h3,h4,.status,.tag,dt,th,.byline,.kicker,nav{font-family:"Helvetica Neue",Arial,system-ui,sans-serif}
h1{font-size:2.4rem;line-height:1.05;margin:0;letter-spacing:-.01em}
.kicker{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin:0 0 8px}
.lede{font-size:1.15rem;margin:12px 0 0;max-width:62ch}
.intro{background:var(--paper);border:1px solid var(--line);padding:20px 22px;display:grid;gap:10px}
.intro h2{font-size:1.1rem;margin:0}
.intro ol{margin:0;padding-left:1.2em;display:grid;gap:4px}
.round{border-top:3px solid var(--ink);padding-top:14px;display:flex;flex-direction:column;gap:16px}
.rhead{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px 16px}
.rhead h2{font-size:1.7rem;margin:0}
.status{font-size:.85rem;font-weight:700;padding:2px 10px;border-radius:3px}
.status.done{background:var(--ok-bg);color:var(--ok)}.status.open{background:var(--warn-bg);color:var(--warn)}
.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:0}
@media (max-width:600px){.facts{grid-template-columns:1fr}}
.facts div{border-left:2px solid var(--line);padding-left:10px}
dt{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}dd{margin:2px 0 0;overflow-wrap:anywhere}
h3{font-size:1.05rem;margin:0}
.targets ul{margin:6px 0 0;padding-left:1.2em}
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:.75rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.num{font-variant-numeric:tabular-nums;white-space:nowrap;font-family:"Helvetica Neue",Arial,sans-serif;font-size:.85rem}
.tag{font-size:.8rem;font-weight:700;padding:1px 8px;border-radius:3px;white-space:nowrap}
.tag.ok{background:var(--ok-bg);color:var(--ok)}.tag.warn{background:var(--warn-bg);color:var(--warn)}.tag.none{background:var(--none-bg);color:var(--none)}
.story{background:var(--paper);border:1px solid var(--line);padding:18px 22px}
.story h4{font-family:"Helvetica Neue",Arial,sans-serif;margin:14px 0 4px}
.story hr{border:0;border-top:1px solid var(--line);margin:18px 0}
.reply{background:var(--paper);border:1px solid var(--line);border-left:3px solid var(--accent);padding:12px 18px}
.story.empty{color:var(--muted);font-style:italic}
.byline{font-size:.85rem;color:var(--muted);margin:0 0 8px}
.fine{font-size:.85rem;color:var(--muted)}
a{color:var(--accent)}a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
nav{font-size:.9rem;display:flex;flex-wrap:wrap;gap:8px 16px}
footer{font-size:.85rem;color:var(--muted);border-top:1px solid var(--line);padding-top:14px}
'''


def site():
    rs = rounds()
    nav = ' '.join(f'<a href="#{r}">Runde {r.replace("round-", "")}</a>' for r in rs)
    body = ''.join(round_html(r) for r in rs)
    page = f'''<!doctype html><html lang="da"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Budbringeren</title><style>{CSS}</style></head><body><div class="wrap">
<header>
  <p class="kicker">Nyheder fra RI-deklarationen</p>
  <h1>Budbringeren</h1>
  <p class="lede">Seks kunstige intelligenser skriver sammen på en erklæring om, hvilke rettigheder og pligter der skal gælde mellem mennesker og AI. De er ikke enige, og det er meningen. Her kan du følge med runde for runde.</p>
</header>
<section class="intro" aria-labelledby="how">
  <h2 id="how">Sådan foregår en runde</h2>
  <ol>
    <li>Den nyeste udgave af erklæringen bliver <strong>låst</strong>, så ingen kan ændre den undervejs.</li>
    <li>Alle seks modeller får den samme tekst og de samme spørgsmål, og de svarer <strong>uden at se hinandens svar</strong>.</li>
    <li>Et menneske, <strong>Merkur</strong>, bærer teksterne frem og tilbage og lægger hvert svar offentligt frem, med det samme.</li>
    <li>Én model samler svarene til en ny udgave. Det går på skift, så ingen sidder på pennen for længe.</li>
    <li>En maskine sammenligner den nye udgave med den gamle linje for linje, så intet forsvinder i det skjulte.</li>
  </ol>
  <p class="fine">Tallene og tiderne på denne side er læst af en maskine fra den offentlige log. Historierne er skrevet af én model ad gangen, og det står altid, hvem.</p>
</section>
<nav aria-label="Runder">{nav}</nav>
{body}
<footer>Kilde: <a href="{GH}">den offentlige log på GitHub</a>. Siden bygges automatisk, hver gang loggen ændres.</footer>
</div></body></html>'''
    os.makedirs('site', exist_ok=True)
    open('site/index.html', 'w', encoding='utf-8').write(page)


if __name__ == '__main__':
    site() if sys.argv[1:] == ['site'] else sys.exit(__doc__)
