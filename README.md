# Atom Teach Axe Site

Static public-safe training website generated from a lesson manifest.

## Live

https://thebuilderofmoebius9.github.io/atom-teach-axe-site/

## Content Model

- `data/lessons.json` — lesson manifest, public-safe topic signals only
- `data/glossary.json` — glossary term registry
- `scripts/build_site.py` — static generator
- `assets/` — CSS/JS

## Lessons

- `2026-07-08` — [Mirror ไม่ใช่ Memory](lessons/mirror-not-memory/)
- `2026-07-08` — [TF-IDF Mini Lab](lessons/tf-idf-mini-lab/)
- `2026-06-04` — [Day 001 — Makers, ESP32 และ Claude เป็นสนามเล่น](lessons/day-001-makers-esp32/)
- `2026-06-07` — [Atlas / Discord.js / Voice — Oracle ต้องมี runtime ไม่ใช่แค่ prompt](lessons/atlas-discordjs-voice/)
- `2026-06-08` — [Workshop / Awaken / Reply Rules — เกิด Oracle ต้องมีกติกา](lessons/workshop-awaken-reply-rules/)
- `2026-06-14` — [GPU / P2P / Parquet — จากแชทสู่ระบบข้อมูล](lessons/gpu-p2p-parquet-proposals/)
- `2026-06-16` — [Netbird / WASM / Mesh — เครือข่ายคือห้องเรียนที่ขยายได้](lessons/netbird-wasm-mesh/)
- `2026-06-17` — [ESP32-WASM Desk Pet — ของเล่นที่กลายเป็นบทเรียนระบบฝังตัว](lessons/esp32-wasm-desk-pet/)
- `2026-06-19 ถึง 2026-06-20` — [Backfill Midterm / Nova / P2P — ความจำทีมต้องย้อนอดีตได้](lessons/backfill-midterm-nova-p2p/)
- `2026-06-21` — [Dropbox / AUTH_KEY / P2P — แชร์ไฟล์ได้ แต่ secret ต้องไม่รั่ว](lessons/dropbox-authkey-p2p-safety/)
- `2026-06-22` — [Gale Framework / Launchers — ทำ agent ให้เปิดซ้ำได้อย่างเป็นระบบ](lessons/gale-framework-fleet-launchers/)
- `2026-06-24` — [Codex Team / Shell Hygiene — ทีม agent ต้องมีสภาพแวดล้อมสะอาด](lessons/codex-team-shell-hygiene/)
- `2026-06-29` — [ESP WebRTC / STT / LLM — จาก hardware ไปสู่ voice agent](lessons/esp-webrtc-stt-llm/)
- `2026-07-03` — [Mirror Index / TF-IDF Dashboard — จากฐานข้อความสู่แผนที่ความรู้](lessons/mirror-index-tfidf-dashboard/)
- `2026-07-05` — [MAW / tmux / Webhook Relay — Control Room ต้องเห็นงานที่กำลังวิ่ง](lessons/maw-tmux-webhook-control-room/)

## Safety Contract

- `public_evidence_mode: signals_only` in generated pages
- `raw_quote_allowed: false` in generated pages
- No backend, no tracking, no raw Discord dumps
