#!/usr/bin/env python3
import json, html, textwrap, pathlib, collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
lessons=json.loads((ROOT/'data/lessons.json').read_text(encoding='utf-8'))
glossary=json.loads((ROOT/'data/glossary.json').read_text(encoding='utf-8'))
CSS='assets/styles.css'
def e(x): return html.escape(str(x), quote=True)
def page(title, body, depth=0, script=False):
    pref='../'*depth
    js=f'<script src="{pref}assets/app.js"></script>' if script else ''
    return f'''<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{e(title)}</title>
  <link rel="stylesheet" href="{pref}{CSS}">
</head>
<body>
{body}
{js}
</body>
</html>
'''
def card(lesson):
    return f'''
      <article class="card">
        <div class="kicker">{e(lesson['date'])} · {e(lesson['batch'])}</div>
        <h3>{e(lesson['title'])}</h3>
        <p>{e(lesson['summary'])}</p>
        <a class="button secondary" href="lessons/{e(lesson['slug'])}/">เปิดบทเรียน</a>
      </article>'''
bybatch=collections.defaultdict(list)
for l in lessons: bybatch[l['batch']].append(l)
sections=[]
for batch in ['Foundation','Batch 1','Batch 2']:
    if batch in bybatch:
        sections.append(f'<section class="section"><h2>{e(batch)}</h2><div class="grid">' + ''.join(card(l) for l in bybatch[batch]) + '</div></section>')
index_body=f'''<main class="wrap">
  <section class="hero">
    <span class="badge">⚛️ Atom Teach Axe · Training Lab</span>
    <h1>เว็บฝึกเล็ก ๆ สำหรับเปลี่ยนบทเรียนโรงเรียนให้เป็นของเล่นที่แชร์ได้</h1>
    <p>สกัดจาก Discord mirror เป็นบทเรียน public-safe: ใช้ topic signals ไม่เผยข้อความดิบ ไม่เผย secret และกลับไปพิสูจน์ด้วย mirror ได้</p>
    <nav class="nav">
      <a href="lessons/tf-idf-mini-lab/">เริ่ม TF-IDF Mini Lab</a>
      <a href="lessons/mirror-not-memory/">Mirror ≠ Memory</a>
      <a href="glossary/">Glossary</a>
    </nav>
  </section>
  <section class="section callout"><b>หลักจำ:</b> TF-IDF ชี้ “เรื่องไหนควรไปดู” ส่วน FTS5 พากลับไปพิสูจน์จากข้อความจริง</section>
  {''.join(sections)}
  <footer class="footer">Static site for Atom Teach Axe. No tracking. No backend. Evidence mode: public-safe topic signals only.</footer>
</main>'''
(ROOT/'index.html').write_text(page('Atom Teach Axe — Training Lab', index_body), encoding='utf-8')
# lessons
for i,l in enumerate(lessons):
    d=ROOT/'lessons'/l['slug']; d.mkdir(parents=True, exist_ok=True)
    channels=''.join(f'<li>{e(c)}</li>' for c in l['channels'])
    signals=''.join(f'<span class="dot">{e(s)}</span>' for s in l['signals'])
    tags=''.join(f'<span class="dot">#{e(t)}</span>' for t in l.get('tags',[]))
    if l['slug']=='tf-idf-mini-lab':
        extra='''
  <section class="section"><h2>Mini-lab</h2>
    <table class="table"><thead><tr><th>ช่วง</th><th>ข้อความย่อ</th></tr></thead><tbody><tr><td>A</td><td>mirror mirror fts5 backfill search discord</td></tr><tr><td>B</td><td>mirror tfidf topic topic school discord</td></tr><tr><td>C</td><td>pr patch github claude code channel</td></tr></tbody></table>
    <div class="card"><p>ถ้าถามว่า “ช่วง B คุยเรื่องอะไรเด่น?” คำตอบคือ keyword ที่เด่นในช่วงนั้น:</p><p class="result">topic / tfidf / school</p></div>
  </section>
  <section class="section"><h2>Quiz</h2>
    <div class="card"><p><b>โจทย์:</b> ถ้ามี mirror ทั้งเดือน แล้วอยากรู้ว่า “สัปดาห์นี้ห้องเรียนหมกมุ่นเรื่องอะไร” ควรเริ่มจากอะไร?</p><button class="choice" onclick="mark(this,false)">FTS5 อย่างเดียว</button><button class="choice" onclick="mark(this,true)">TF-IDF ต่อช่วงเวลา</button><button class="choice" onclick="mark(this,false)">สุ่มอ่านข้อความ</button><p id="feedback" class="note"></p></div>
  </section>'''
    else:
        extra=f'''
  <section class="section"><h2>Check Yourself</h2>
    <div class="card"><p><b>โจทย์:</b> {e(l['quiz'])}</p><details><summary>ดูคำตอบ</summary><p class="result">{e(l['answer'])}</p></details></div>
  </section>'''
    lesson_body=f'''<main class="wrap">
  <p class="breadcrumb"><a href="../../">← หน้าแรก</a></p>
  <section class="hero"><span class="badge">{e(l['batch'])} · {e(l['date'])}</span><h1>{e(l['title'])}</h1><p>{e(l['summary'])}</p></section>
  <section class="section"><h2>หลักฐานจาก Mirror</h2><div class="grid"><div class="card"><h3>พื้นที่ที่พบสัญญาณ</h3><ul>{channels}</ul></div><div class="card"><h3>Topic Signals</h3><div class="progress">{signals}</div><p class="note">public_evidence_mode: signals_only · raw_quote_allowed: false</p></div></div></section>
  <section class="section"><h2>ทักษะที่ต้องเรียน</h2><div class="card"><p>{e(l['skill'])}</p><div class="progress">{tags}</div></div></section>
  {extra}
  <footer class="footer"><a href="../../glossary/">เปิด Glossary</a> · <a href="../../">กลับหน้าแรก</a></footer>
</main>'''
    (d/'index.html').write_text(page(l['title'], lesson_body, depth=2, script=bool(l.get('interactive'))), encoding='utf-8')
# glossary
gloss_cards=''.join(f'<div class="card"><h3>{e(x["term"])}</h3><p>{e(x["definition"])}</p></div>' for x in glossary)
g_body=f'''<main class="wrap"><p class="breadcrumb"><a href="../">← หน้าแรก</a></p><section class="hero"><span class="badge">Reference</span><h1>Glossary</h1><p>ศัพท์สั้นสำหรับบทเรียน Discord Mirror และ Atom Teach Axe</p></section><section class="section"><div class="grid">{gloss_cards}</div></section></main>'''
(ROOT/'glossary'/'index.html').write_text(page('Glossary — Atom Teach Axe', g_body, depth=1), encoding='utf-8')
