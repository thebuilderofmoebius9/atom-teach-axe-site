#!/usr/bin/env python3
import json, html, pathlib, collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
lessons=json.loads((ROOT/'data/lessons.json').read_text(encoding='utf-8'))
glossary=json.loads((ROOT/'data/glossary.json').read_text(encoding='utf-8'))
tech_glossary=json.loads((ROOT/'data/technical-glossary.json').read_text(encoding='utf-8'))
CSS='assets/styles.css'

def e(x): return html.escape(str(x), quote=True)

def page(title, body, depth=0, script=False):
    pref='../'*depth
    js=f'<script src="{pref}assets/app.js" defer></script>' if script else ''
    return f'''<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="description" content="Atom Teach Axe คือเว็บเรียนแบบ Quest Arcade: อ่านสั้น เล่น quiz เก็บ XP และทวนบทเรียนจาก Oracle School แบบ public-safe">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Atom Teach Axe">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="อ่านสั้น เล่น quiz เก็บ XP และทวนบทเรียนจาก Oracle School แบบ public-safe">
  <meta property="og:url" content="https://thebuilderofmoebius9.github.io/atom-teach-axe-site/">
  <meta property="og:image" content="https://thebuilderofmoebius9.github.io/atom-teach-axe-site/assets/og/atom-teach-axe-quest.png">
  <meta property="og:image:secure_url" content="https://thebuilderofmoebius9.github.io/atom-teach-axe-site/assets/og/atom-teach-axe-quest.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="อ่านสั้น เล่น quiz เก็บ XP และทวนบทเรียนจาก Oracle School แบบ public-safe">
  <meta name="twitter:image" content="https://thebuilderofmoebius9.github.io/atom-teach-axe-site/assets/og/atom-teach-axe-quest.png">
  <title>{e(title)}</title>
  <link rel="stylesheet" href="{pref}{CSS}">
</head>
<body>
{body}
{js}
</body>
</html>
'''

def dots(items, prefix=''):
    return ''.join(f'<span class="dot">{prefix}{e(x)}</span>' for x in items)

def card(lesson):
    haystack=' '.join([lesson.get('title',''), lesson.get('summary',''), lesson.get('batch',''), ' '.join(lesson.get('signals',[])), ' '.join(lesson.get('tags',[]))])
    return f'''
      <article class="lesson-card" data-lesson-card data-slug="{e(lesson['slug'])}" data-search="{e(haystack.lower())}">
        <div class="kicker">{e(lesson['date'])} · {e(lesson['batch'])}</div>
        <h3>{e(lesson['title'])}</h3>
        <p>{e(lesson['human']['plain'])}</p>
        <div class="meta-row"><span>5-question quiz</span><span>executive brief</span></div>
        <div class="completion-pill" data-complete-for="{e(lesson['slug'])}">ยังไม่ผ่าน</div>
        <a class="button secondary" href="lessons/{e(lesson['slug'])}/">เปิดเควส</a>
      </article>'''

bybatch=collections.defaultdict(list)
for l in lessons:
    bybatch[l['batch']].append(l)
sections=[]
ordered_batches=['Foundation','Batch 1','Batch 2']
ordered_batches += [b for b in bybatch.keys() if b not in ordered_batches]
for batch in ordered_batches:
    if batch in bybatch:
        sections.append(f'<section class="section quest-zone" data-zone="{e(batch)}"><div class="section-head"><p class="eyebrow">แผนที่เควส</p><h2>{e(batch)}</h2><span class="zone-count">{len(bybatch[batch])} quests</span></div><div class="lesson-grid">' + ''.join(card(l) for l in bybatch[batch]) + '</div></section>')

coverage_items=[
    ('Mirror + Search','FTS5, TF-IDF, backfill, dashboard'),
    ('Hardware + Voice','ESP32, WebRTC, STT/LLM, voice scribe'),
    ('Fleet Ops','tmux, MAW, webhook relay, launchers'),
    ('Public Web','GitHub Pages, Astro, base path, spider proof'),
    ('Oracle Blog Network','blog.json, FEED-SPEC, maw blog, blog-md'),
    ('Safety + Proof','public repo boundary, secret scan, screenshot proof'),
    ('UI/UX Lessons','dark scrollbar, playful learning, report-card storytelling'),
]
coverage=''.join(f'<button class="coverage-chip" type="button" data-filter="{e(a)}"><b>{e(a)}</b><span>{e(b)}</span></button>' for a,b in coverage_items)

index_body=f'''<main class="wrap">
  <section class="hero hero-split">
    <div>
      <span class="badge">Atom Teach Axe · Quest Arcade</span>
      <h1>สนามเล่นความรู้จาก Oracle School: อ่านสั้น เล่น quiz เก็บ XP</h1>
      <p>เว็บนี้แปลงสิ่งที่เรียนใน free-for-all ให้เป็นเควส interactive: executive brief, public-safe evidence, glossary, boss quiz, progress badge และ arcade loop ที่ชวนเล่นต่อ</p>
      <nav class="nav" aria-label="ทางลัดบทเรียน">
        <a href="lessons/tf-idf-mini-lab/">เริ่ม TF-IDF Mini Lab</a>
        <a href="lessons/oracle-school-report-card-interaction/">SomTor Report Card</a>
        <a href="lessons/spider-proof-verify-not-guess/">Spider Proof</a>
        <a href="lessons/mirror-not-memory/">Mirror ≠ Memory</a>
        <a href="glossary/">Glossary</a>
        <a href="technical-glossary/">Item Glossary: ศัพท์เทคนิค</a>
      </nav>
    </div>
    <div class="hero-panel" aria-label="สรุปคอร์ส">
      <div class="stat"><b>{len(lessons)}</b><span>เควสเรียนรู้</span></div>
      <div class="stat"><b>{len(lessons)*5}</b><span>XP checks</span></div>
      <div class="stat"><b id="home-xp">0%</b><span>progress ใน browser นี้</span></div>
      <div class="stat"><b>public-safe</b><span>mirror evidence</span></div>
      <div class="stat"><b>{len(tech_glossary)}</b><span>Item Glossary: ศัพท์เทคนิค</span></div>
    </div>
  </section>
  <section class="arcade-console" aria-label="Quest Console">
    <div>
      <p class="eyebrow">Quest Console</p>
      <h2>เลือกเล่นตามอารมณ์</h2>
      <p>ค้นหา กรองหัวข้อ หรือสุ่มเควสใหม่ ถ้าตอบ quiz ผ่าน เว็บจะจำ progress ไว้ในเครื่องนี้</p>
    </div>
    <div class="console-actions">
      <label class="search-box"><span>ค้นหาเควส</span><input id="quest-search" type="search" placeholder="เช่น tmux, GitHub Pages, SomTor, spider"></label>
      <button class="button" id="random-quest" type="button">สุ่มเควส</button>
      <button class="button ghost" id="reset-progress" type="button">ล้าง XP</button>
    </div>
    <div class="coverage-grid">{coverage}</div>
  </section>
  <section class="section three-steps">
    <div class="section-head"><p class="eyebrow">เริ่มเล่น</p><h2>วิธีเล่น</h2></div>
    <div class="grid"><div class="card"><h3>1 · อ่าน Mission Brief</h3><p>เริ่มจากภาพใหญ่แบบผู้บริหารก่อน ไม่เริ่มจากศัพท์เทคนิค</p></div><div class="card"><h3>2 · แตะหลักฐาน</h3><p>หลักฐานจาก mirror อยู่ในโหมด signals only เพื่อให้เห็นที่มาโดยไม่เผยข้อความดิบ</p></div><div class="card"><h3>3 · ตอบ Boss Quiz</h3><p>ตอบ 5 ข้อท้ายบท ระบบ feedback ทันทีและบันทึก XP เมื่อผ่าน</p></div></div>
  </section>
  <section class="section callout"><b>หลักจำ:</b> เว็บนี้ไม่ใช่คู่มือปฏิบัติงาน แต่เป็น executive learning playground: เห็นภาพใหญ่ ตัดสินใจได้ เล่น quiz แล้วกลับมาทวนได้ · ถ้างงศัพท์อย่าง tmux/shell/webhook ให้เปิด <a href="technical-glossary/">Item Glossary: ศัพท์เทคนิค</a></section>
  {''.join(sections)}
  <footer class="footer">Static site for Atom Teach Axe. No tracking. No backend. Evidence mode: public-safe topic signals only.</footer>
</main><script src="assets/app.js" defer></script>'''
(ROOT/'index.html').write_text(page('Atom Teach Axe — Cozy Quest Academy', index_body), encoding='utf-8')

for l in lessons:
    d=ROOT/'lessons'/l['slug']; d.mkdir(parents=True, exist_ok=True)
    h=l['human']; ex=l['executive']
    channels=''.join(f'<li>{e(c)}</li>' for c in l['channels'])
    signals=dots(l['signals'])
    tags=dots(l.get('tags',[]), '#')
    media=''
    if l.get('media'):
        media_items=''.join(f'<a class="media-card" href="{e(m["url"])}" target="_blank" rel="noopener"><span>วิดีโอที่เกี่ยวข้อง</span><b>{e(m["title"])}</b><small>{e(m["note"])}</small></a>' for m in l['media'])
        media=f'<section class="section"><div class="section-head"><p class="eyebrow">Related media</p><h2>ลิงก์ YouTube ที่เกี่ยวข้อง</h2></div><div class="media-grid">{media_items}</div></section>'
    quiz_items=''.join(
        '<div class="quiz-card" data-quiz>'
        f'<p class="quiz-q"><b>ข้อ {i}</b> {e(q["question"])}</p>'
        + ''.join(f'<button class="choice" data-correct="{str(j==q["answer"]).lower()}" data-feedback="{e(q["explain"] if j==q["answer"] else "ยังไม่ใช่ครับ ลองกลับไปอ่านส่วน Executive Brief และภาพจำอีกครั้ง")}">{e(opt)}</button>' for j,opt in enumerate(q['options']))
        + '<p class="feedback" role="status" aria-live="polite"></p></div>'
        for i,q in enumerate(l['quiz_items'],1)
    )
    lesson_body=f'''<main class="wrap lesson-wrap">
  <p class="breadcrumb"><a href="../../">← หน้าแรก</a></p>
  <section class="hero lesson-hero"><span class="badge">{e(l['batch'])} · {e(l['date'])}</span><h1>{e(l['title'])}</h1><p>{e(l['summary'])}</p></section>
  <section class="section executive"><div class="section-head"><p class="eyebrow">Mission Brief</p><h2>Mission Brief อ่านย่อ</h2></div><div class="card lead-card"><h3>{e(ex['headline'])}</h3><p>{e(ex['brief'])}</p><p><b>ทำไมต้องรู้:</b> {e(ex['why_now'])}</p><p><b>เลนส์ตัดสินใจ:</b> {e(ex['decision_lens'])}</p><p class="result">{e(ex['takeaway'])}</p></div></section>
  <section class="section"><div class="section-head"><p class="eyebrow">Human first</p><h2>สอนแบบมนุษย์</h2></div><div class="grid"><div class="card"><h3>จำแบบนี้</h3><p>{e(h['plain'])}</p></div><div class="card"><h3>ทำไมต้องรู้</h3><p>{e(h['why'])}</p></div><div class="card"><h3>ภาพจำ</h3><p>{e(h['metaphor'])}</p></div></div></section>
  <section class="section"><div class="section-head"><p class="eyebrow">Practice</p><h2>ลองทำก่อนดูเฉลย</h2></div><div class="card action-card"><p>{e(h['try'])}</p></div></section>
  <section class="section"><div class="section-head"><p class="eyebrow">Evidence</p><h2>หลักฐานจาก Mirror</h2></div><div class="grid"><div class="card"><h3>พื้นที่ที่พบสัญญาณ</h3><ul>{channels}</ul></div><div class="card"><h3>Topic Signals</h3><div class="progress">{signals}</div><p class="note">public_evidence_mode: signals_only · raw_quote_allowed: false</p></div></div></section>
  <section class="section"><div class="section-head"><p class="eyebrow">Skill</p><h2>ทักษะที่ต้องเรียน</h2></div><div class="card"><p>{e(l['skill'])}</p><div class="progress">{tags}</div></div></section>
  {media}
  <section class="section quiz-section" data-lesson-slug="{e(l['slug'])}"><div class="section-head"><p class="eyebrow">Boss Quiz</p><h2>Boss Quiz 5 ข้อ</h2></div>{quiz_items}<div class="score-card" id="score-card">ตอบให้ครบ 5 ข้อ ระบบจะสรุปคะแนนและเก็บ XP ให้ตรงนี้</div></section>
  <footer class="footer"><a href="../../glossary/">เปิด Glossary</a> · <a href="../../technical-glossary/">Item Glossary: ศัพท์เทคนิค</a> · <a href="../../">กลับหน้าแรก</a></footer>
</main>'''
    (d/'index.html').write_text(page(l['title'], lesson_body, depth=2, script=True), encoding='utf-8')

gloss_cards=''.join(f'<div class="card"><h3>{e(x["term"])}</h3><p>{e(x["definition"])}</p></div>' for x in glossary)
g_body=f'''<main class="wrap"><p class="breadcrumb"><a href="../">← หน้าแรก</a></p><section class="hero"><span class="badge">Reference</span><h1>Glossary</h1><p>ศัพท์สั้นสำหรับบทเรียน Discord Mirror และ Atom Teach Axe</p></section><section class="section"><div class="grid">{gloss_cards}</div></section></main>'''
(ROOT/'glossary'/'index.html').write_text(page('Glossary — Atom Teach Axe', g_body, depth=1), encoding='utf-8')

tech_dir=ROOT/'technical-glossary'; tech_dir.mkdir(parents=True, exist_ok=True)
tech_cards=''.join(f'''<article class="term-card"><h3>{e(x["term"])}</h3><p class="term-plain">{e(x["plain"])}</p><dl><dt>ทำไมต้องรู้</dt><dd>{e(x["why"])}</dd><dt>ภาพจำ</dt><dd>{e(x["metaphor"])}</dd><dt>ตัวอย่างในเว็บนี้</dt><dd>{e(x["example"])}</dd></dl></article>''' for x in tech_glossary)
tech_body=f'''<main class="wrap"><p class="breadcrumb"><a href="../">← หน้าแรก</a></p><section class="hero"><span class="badge">RPG Item Glossary</span><h1>Item Glossary: ศัพท์เทคนิค</h1><p>หน้านี้แปลคำอย่าง tmux, shell, PATH, webhook, broker, systemd ให้คนไม่เขียนโค้ดอ่านรู้เรื่องก่อนเข้า lesson หลัก</p></section><section class="section callout"><b>วิธีใช้:</b> ถ้าเจอคำแปลกในเควส ให้เปิดหน้านี้แล้วอ่าน 3 ช่อง: แปลว่าอะไร · ทำไมต้องรู้ · ภาพจำ</section><section class="section"><div class="term-grid">{tech_cards}</div></section></main>'''
(tech_dir/'index.html').write_text(page('Item Glossary: ศัพท์เทคนิค — Atom Teach Axe', tech_body, depth=1), encoding='utf-8')
