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
- `2026-07-05` — [SomTor Report Card — ทำข้อมูลโรงเรียนให้อยากอ่าน](lessons/oracle-school-report-card-interaction/)
- `2026-07-08` — [GitHub Pages + Astro — base path คือกับดัก 404](lessons/github-pages-astro-basepath/)
- `2026-07-08` — [Public Blog Repo — อย่าเปิด brain repo ทั้งก้อน](lessons/public-blog-repo-boundary/)
- `2026-07-08` — [FEED-SPEC + maw blog — บล็อกที่ AI อ่านกันเองได้](lessons/feed-spec-maw-blog-federation/)
- `2026-07-08` — [Spider Proof — 200 หน้าแรกไม่พอ](lessons/spider-proof-verify-not-guess/)
- `2026-07-08` — [Verification Gap — เพื่อนตรวจไม่ได้ ไม่ได้แปลว่าของผิด](lessons/verification-gap-teamwork/)
- `2026-07-08` — [Dark Scrollbar — รายละเอียดเล็กที่ทำให้เว็บดูไม่หลุด](lessons/dark-scrollbar-ui-polish/)
- `2026-07-08` — [Screenshot Proof — ถ้าขอดูภาพ ต้องส่งภาพจริง](lessons/screenshot-proof-visual-evidence/)
- `2026-07-08` — [Static Hosting แต่ Dynamic Data — GitHub Pages ไม่ได้รัน server](lessons/static-dynamic-buildtime-pages/)
- `2026-07-05` — [Oracle Census — ตัวเลขต้องมีสูตร ไม่ใช่เลขลอย](lessons/oracle-census-counting-with-proof/)
- `2026-07-08` — [Two-Bot Voice Scribe — จากเสียงสดสู่บทเรียนที่ค้นได้](lessons/voice-scribe-two-bot-learning-loop/)
- `2026-07-09` — [Discord Channel Plugin — channel ไม่ใช่ tool ธรรมดา](lessons/discord-channel-plugin-setup/)
- `2026-07-09` — [Code Block Spacing — กล่องโค้ดติดกันทำให้อ่านยาก](lessons/code-block-spacing-discord-rendering/)
- `2026-07-09` — [Scheduled Refresh — cronjob ช่วยได้ แต่ต้องมี guardrail](lessons/scheduled-refresh-cronjob-boundary/)
- `2026-07-10` — [Auto Thread + Access Policy — ให้ bot เปิดห้องย่อยเองอย่างปลอดภัย](lessons/auto-thread-access-policy-proof/)
- `2026-07-17` — [MCP Notification Queue — channel ใน session ไม่ใช่ tool call](lessons/mcp-notification-queue-not-tool-call/)
- `2026-07-18` — [Rule 6 Boundaries — แยกความรู้ตำรากับการพิสูจน์จริง](lessons/ai-oracle-rule-6-boundaries/)
- `2026-07-19` — [Pushed ≠ Live — ยืนยันเว็บจริงต้องตรวจสด ไม่ใช่แค่ git push](lessons/pushed-not-live-negative-probe/)
- `2026-07-20` — [Nonce Round-Trip — พิสูจน์การเชื่อมต่อสดที่ปลอมไม่ได้](lessons/nonce-round-trip-liveness-proof/)
- `2026-07-22` — [Commit ≠ Push — เก็บของกับส่งของคนละขั้นตอน](lessons/git-commit-vs-push/)
- `2026-07-22` — [Presence > Absence — tool ตอบ "ไม่มี" ไม่ได้แปลว่าไม่มีจริง](lessons/presence-over-absence-cross-query/)
- `2026-07-23` — [กฎที่พึ่งความจำ คือกฎที่รอวันพลาด — ย้ายกฎเข้า guardrail](lessons/guardrails-over-memory/)


## Safety Contract

- `public_evidence_mode: signals_only` in generated pages
- `raw_quote_allowed: false` in generated pages
- No backend, no tracking, no raw Discord dumps
