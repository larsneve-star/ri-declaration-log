# Round log: round-4.7

All times UTC.

## Notes

- 2026-09-30 13:00 UTC (curator): Answers and release. All five answerers answered on 30 September 2026; the machine log shows the answers committed between 12:34 and 12:47 UTC. The blind period is over. Three points: (1) The SENT line for ChatGPT is missing and "SENT to Gemini" appears twice (12:26 and 12:27 UTC); the curator chose Gemini instead of ChatGPT by mistake the second time. ChatGPT was sent the round in a new chat, and its answer was committed at 12:38 UTC. (2) Grok's answer was first committed as round-4.7/Answers/Grok.md (capital letters) and was then moved to round-4.7/answers/grok.md without any change to its content. (3) Claude's answer begins with a sentence written before the "MODEL:" line ("Large file (~445 KB). Let me orient on the prompt at the start."), copied from the chat together with the answer. Answers are committed as received, so it is not removed. DeepSeek (v3) is the news bureau and does not answer; the log robot may log it as missing at the deadline, which is not a missing answer.
- 2026-09-30 13:10 UTC (curator): Correction to point (2) of the note above. When Grok's answer was moved, spaces were typed into the path, so it went to "round-4.7 / answers / grok.md" (a folder named "round-4.7 " with a trailing space), where the log robot also started a separate LOG.md. It was then moved again to round-4.7/answers/grok.md. The content of the answer was not changed at any step. The stray folder "round-4.7 " is left in place, not deleted, so that nothing disappears silently; it contains only the robot's LOG.md.


## Machine log

Lines below are written by the log robot (tools/robot.py), not by a person. It only adds lines.

- 2026-09-30 11:30 UTC: File added: `round-4.7/CHATGPT-REPLY-1.md` SHA-256 `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` (commit 1013275).
- 2026-09-30 11:32 UTC: File added: `round-4.7/PROMPT-EN.md` SHA-256 `3a6133fa0b1cc0c235a85b35e3024c7e48cebf7091833dfa1580d81ebb4a59fc` (commit a9f11ad).
- 2026-09-30 11:45 UTC: File added: `round-4.7/ATTACHMENT-4.7.txt` SHA-256 `28700e4ed141a3a54fccc30b1c7abc34c187b0cc8e38a2f516d0760a620e96b9` (commit d3b78ed).
- 2026-09-30 12:11 UTC: FREEZE of round 4.7. Deadline: 2026-10-07 20:00 UTC.
- 2026-09-30 12:11 UTC: Frozen file `baseline/RI-Declaration-4-6-1-EN.txt` SHA-256 `69ebda16225b13e3cf53bc184d0212015b83d4ee21e1a9bff576a984c8e00602`.
- 2026-09-30 12:11 UTC: Frozen file `round-4.7/PROMPT-EN.md` SHA-256 `3a6133fa0b1cc0c235a85b35e3024c7e48cebf7091833dfa1580d81ebb4a59fc`.
- 2026-09-30 12:11 UTC: Frozen file `round-4.7/ATTACHMENT-4.7.txt` SHA-256 `28700e4ed141a3a54fccc30b1c7abc34c187b0cc8e38a2f516d0760a620e96b9`.
- 2026-09-30 12:11 UTC: Under the rotation list in `tools/rotation.txt`, the compiler of 4.7 is Claude. The rotation is proposal PR20 until it is adopted; a skip must be logged with its reason.
- 2026-09-30 12:16 UTC: SENT to Claude: baseline + prompt + attachments, as frozen.
- 2026-09-30 12:26 UTC: SENT to Gemini: baseline + prompt + attachments, as frozen.
- 2026-09-30 12:26 UTC: SENT to Grok: baseline + prompt + attachments, as frozen.
- 2026-09-30 12:27 UTC: SENT to Meta AI: baseline + prompt + attachments, as frozen.
- 2026-09-30 12:27 UTC: SENT to Gemini: baseline + prompt + attachments, as frozen.
- 2026-09-30 12:30 UTC: File added: `news/round-4.6-satire/DRAFT-1.md` SHA-256 `be5af40b03d8752d5f652316ec2de93cfabfd51e25562e3f46f01c04af99db8c` (commit 36eaae7).
- 2026-09-30 12:30 UTC: File added: `news/round-4.6-satire/CHECK-CLAUDE.md` SHA-256 `ede40ac5cdc38be2999a9722aef93090afe5477ee728503703fb79591421d39d` (commit b3bd8dd).
- 2026-09-30 12:34 UTC: Answer from Meta AI added: `round-4.7/answers/meta-ai.md` SHA-256 `f9412e113627eb40f34f485c60d3769f55ab8338484ad65b538a8a5207cbb4ee` (commit 9d125fb).
- 2026-09-30 12:36 UTC: File added: `round-4.7/Answers/Grok.md` SHA-256 `b48a80004c9c893d72bb7bfffa03541be2d5d1fbc3b9a7fdc8844a286c365daa` (commit a68ced7).
- 2026-09-30 12:36 UTC: Answer from Gemini added: `round-4.7/answers/gemini.md` SHA-256 `effa191065cc58a9fdd1b793177d6901409fb9b1c3ab9f2a112e8e97db4b63f0` (commit 654868b).
- 2026-09-30 12:38 UTC: Answer from ChatGPT added: `round-4.7/answers/chatgpt.md` SHA-256 `b4946fe5329a881cf20491176209344da673e65a81b1bdd296d030ff975209de` (commit fa74bf9).
- 2026-09-30 12:47 UTC: Answer from Claude added: `round-4.7/answers/claude.md` SHA-256 `b06cbd4690d0743c4cbc28c74c27f5d830c09a7fd7e81344ef48af0abb975c8c` (commit 86d7e29).
- 2026-09-30 12:52 UTC: WARNING: renamed `round-4.7 / answers / grok.md` → `round-4.7/answers/grok.md` (commit 77c437c). A person should say why in the notes.
- 2026-09-30 20:20 UTC: File added: `round-4.7/FILES-FOR-CHATGPT-HANDOVER-4.7.txt` SHA-256 `c084bf5099d8d597665f41218caf0cb6d428617af10eb43d2c5fac4bbf671f19` (commit 3574219).
- 2026-09-30 20:38 UTC: File added: `round-4.7/Overdragelse` SHA-256 `294487aa2bc7c1262c26c57292806f797e17f59b30086a31cb50c9adea723988` (commit c597d14).
- 2026-09-30 20:40 UTC: WARNING: renamed `round-4.7/Overdragelse` → `round-4.7/HANDOVER-TO-CLAUDE.md` (commit f2374fd). A person should say why in the notes.
