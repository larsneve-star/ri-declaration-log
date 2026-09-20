# Round log: consultation on 4.2 (towards 4.3)

All times UTC. One line per event, added in order and never edited afterwards.

## Freeze

| Item | File | SHA-256 |
|---|---|---|
| Baseline | `baseline/RI-Declaration-4-2-EN.txt` | `c2fd3e9c4d68a1e10dd8e0bae939b17da8e09993191ff8752ec41cf0258e4ebd` |
| Prompt | `round-4.3/PROMPT-EN.md` | `2f105e7842160d41dc66360ab9b5c6bbddbfe6b34cdcd39f5a2b81ca85b9efba` |
| Attachment | `Ri-Neutral-Overdragelse-Automaton.html` | `75d05a89442d8ac85f0f44fa11b4958ea05974db9aef9eccfc7fd4b5a68dbd06` |

Frozen at: 2026-09-20 15:17 UTC (link and deadline written into both prompts, commits 5a8d05c and b84a83f)
Deadline: 2026-09-23 15:00 UTC (about 72 h after the freeze, as stated in the prompt)
Question owners this round: Merkur (curator) and Claude (drafted the prompt). Neither may compile 4.3.
Proposed compiler of 4.3: Meta AI or Gemini, as named in 4.2 ("The next version"). The curator records the choice here before any answer is released. Neither is a question owner in this round.

## Sent

| Model | Sent at | What was sent | Deviation |
|---|---|---|---|
| Claude | 2026-09-20 15:45 (approx.) | prompt + Automaton | baseline .txt not delivered as a file; this model holds the copy it generated itself |
| Gemini | | | |
| ChatGPT | | | |
| DeepSeek | 2026-09-20 16:34 (approx.) | prompt + Automaton + baseline | none |
| Grok | | | |
| Meta AI | 2026-09-20 16:05 (approx.) | prompt + Automaton | baseline .txt not delivered; model answered from the hash and the prompt only |

## Received

| Model | Received at | File | SHA-256 | Status (answer / substitution / refusal / missing) |
|---|---|---|---|---|
| Claude | 2026-09-20 15:45 | `round-4.3/answers/claude.md` | `f63f008381de628f95158107e98ad18d5abdd5a5cd9f02ea26d29a9e7714d264` | answer (question owner; see disclosures in the file) |
| Meta AI | 2026-09-20 16:05 | `round-4.3/answers/meta-ai.md` | `7d9f85fe8bc16c86b20c9a512d00f7530a42a3732a5bae14ca411b03ff2f48c9` | answer (baseline not received; see note in file) |
## Breaches and notes

- 2026-09-19 13:50 UTC: The file `ri-public-log (1).zip` was uploaded by mistake in the first commit (d35435c). It was another model's package, containing a different baseline (SHA-256 e815fba6…19f3, 129,682 bytes) that is not the frozen baseline. It was removed at 14:09 UTC in commit aad1f87 and remains visible in the history. Nothing had been sent to any model before the removal.
- 2026-09-19 14:34 UTC: In commit 97f1190 the other model's package was uploaded by mistake a second time, into `round-4.3/` (its baseline SHA-256 e815fba6…19f3, its prompt SHA-256 c16dc6ce…02c0). The mix-up happened because both packages had the same folder name. The files were removed in commits e901cc3 to c21b0a4 and remain visible in the history. They are not the frozen baseline.
- 2026-09-19 14:54 UTC: In commit 06d24ab three files were uploaded as Word documents (`LOG.md.docx`, `PROMPT-DA.md.docx`, `PROMPT-EN.md.docx`) because Google Drive converted them on download. They were removed on 2026-09-20 in commits ca2aa69, 58074ed and 7ea1024. The link and deadline were then written directly into the prompts on GitHub instead. Nothing had been sent to any model before any of these removals.

## Release

Released at: [DATE TIME UTC]
