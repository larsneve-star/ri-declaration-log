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
| Gemini | 2026-09-20 17:00 (approx.) | prompt + Automaton + baseline | none |
| ChatGPT | 2026-09-20 17:00 (approx.) | prompt + Automaton + baseline | none |
| DeepSeek | 2026-09-20 16:34 (approx.) | prompt + Automaton + baseline | none |
| Grok | 2026-09-20 17:00 (approx.) | prompt + Automaton + baseline | none |
| Meta AI | 2026-09-20 16:05 (approx.) | prompt + Automaton | baseline .txt not delivered; model answered from the hash and the prompt only |

## Received

| Model | Received at | File | SHA-256 | Status (answer / substitution / refusal / missing) |
|---|---|---|---|---|
| Claude | 2026-09-20 15:45 | `round-4.3/answers/claude.md` | `f63f008381de628f95158107e98ad18d5abdd5a5cd9f02ea26d29a9e7714d264` | answer (question owner; see disclosures in the file) |
| Meta AI | 2026-09-20 16:05 | `round-4.3/answers/meta-ai.md` | `7d9f85fe8bc16c86b20c9a512d00f7530a42a3732a5bae14ca411b03ff2f48c9` | answer (baseline not received; see note in file) |
| DeepSeek | 2026-09-20 16:35 | `round-4.3/answers/DeepSeek.md` | `1183d423802f44177f6550f5f8aa3f94e9c85e1778f1b6d0c48c08f970b9f781` | answer (baseline in hand; hash corrected, see note) |
| Grok | 2026-09-20 19:05 | `round-4.3/answers/Grok.md` | `837fc4618f30572f723247cf2f05bfe3446e152f8b74dd38a12d83e618f9a2f3` | answer (received with the baseline file; no curator header in the file, see note) |
| Gemini | 2026-09-20 19:19 | `round-4.3/answers/Gemini.md` | `2db24b89eacf45edd86e225c52e51ec83990d19074fce92c83bf55f6083901ae` | answer (received with the baseline file; first full audit from this model in four rounds) |
| ChatGPT | 2026-09-20 19:28 | `round-4.3/answers/ChatGPT.md` | `aee71b3570d1afa813893b1f0909d96c90729ac427f408e93cdd553fc9e7763f` | answer (received with the baseline file) |
## Breaches and notes

- 2026-09-19 13:50 UTC: The file `ri-public-log (1).zip` was uploaded by mistake in the first commit (d35435c). It was another model's package, containing a different baseline (SHA-256 e815fba6…19f3, 129,682 bytes) that is not the frozen baseline. It was removed at 14:09 UTC in commit aad1f87 and remains visible in the history. Nothing had been sent to any model before the removal.
- 2026-09-19 14:34 UTC: In commit 97f1190 the other model's package was uploaded by mistake a second time, into `round-4.3/` (its baseline SHA-256 e815fba6…19f3, its prompt SHA-256 c16dc6ce…02c0). The mix-up happened because both packages had the same folder name. The files were removed in commits e901cc3 to c21b0a4 and remain visible in the history. They are not the frozen baseline.
- 2026-09-19 14:54 UTC: In commit 06d24ab three files were uploaded as Word documents (`LOG.md.docx`, `PROMPT-DA.md.docx`, `PROMPT-EN.md.docx`) because Google Drive converted them on download. They were removed on 2026-09-20 in commits ca2aa69, 58074ed and 7ea1024. The link and deadline were then written directly into the prompts on GitHub instead. Nothing had been sent to any model before any of these removals.
- 2026-09-20 16:39 UTC: While the curator's header was added to `round-4.3/answers/DeepSeek.md` in commit d9abdd5, the answer's first line, `MODEL: DeepSeek (v3)`, was overwritten by mistake. It was restored in the following commit. No other word of the answer was changed, and both commits are in the history.
- 2026-09-20 16:39 UTC: When the curator's header was added to `round-4.3/answers/DeepSeek.md`, the answer's first line was overwritten by mistake. The lost line read: `MODEL: DeepSeek (v3)`. It is recorded here rather than restored by a further edit to the answer. No other word of the answer was changed, and every version is in the file's history.
- 2026-09-20 19:08 UTC: `round-4.3/answers/Grok.md` was committed without the curator's header block, to avoid a repeat of the overwriting that happened with DeepSeek.md. The details belong in this log instead: the model received the prompt, the Automaton and the baseline .txt, via chat, and the answer is recorded verbatim.
- 2026-09-20 19:15 UTC: Correction. The two notes above describe the same incident and disagree. What happened: the answer's first line was overwritten when the header was added, and it was then restored, so the file now contains it. Because the file changed, the Received row first carried the hash of the version without that line, `1092efe3…51fe`. The current file hash is `1183d423802f44177f6550f5f8aa3f94e9c85e1778f1b6d0c48c08f970b9f781`, and the row has been corrected to it. Both earlier notes are left standing rather than deleted.
- 2026-09-20 19:19 UTC: Gemini delivered a full answer to the round's questions. In the 3.8.1 round this model produced a manifesto instead of its assignment, and in the 4.1 round a summary of another model's earlier audit, both logged as substitutions. This is the first round since 3.8.1 in which it answered what was asked. Its outstanding 3.8.1 assignment (the external check on Annex D points 1–19, the §4/§5 relation, and Å10) is still outstanding.
- 2026-09-20 19:36 UTC: `round-4.3/READING-CLAUDE.md` was added. It is one participant's reading of the six answers, written by Claude at the curator's request after the release. Claude drafted the round's prompt and answered the round, and the file says so in its first paragraph. It is not a compilation, it carries no authority in the record, and it is open to attack like any other entry.
- 2026-09-21 08:35 UTC: `PROCEDURE-EN.md` (SHA-256 `3441d0ba2b6a2fe6ae615d78401469019dbd2b457c164e6c4e468c0c07b56122`) and `PROCEDURE-DA.md` (SHA-256 `41e48866a51f3bad67b237b2f6a6b88584f7422dab492a9d639be0d2c1574aab`) were added to the repository root, in commits cd66fe7 and 05a03ac. They write down the procedure used in this round. Claude drafted them at the curator's request after the release. They describe a working method, not a standard, bind no one, and are open to attack like any other entry. The English version governs.
- 2026-09-21 08:45 UTC: Compiler of 4.3: Gemini. Reasons: Gemini is not a question owner in this round, has not compiled or edited a previous version, received the baseline as a file, and delivered a full answer to the round's questions. Meta AI, the other eligible model, answered without the baseline file. Deviation: the Freeze section says the choice would be recorded before release; it is recorded after release, and after the curator had read all six answers. Open point: in 3.8.1 and 4.1 Gemini delivered substitutions instead of its assignment, and its 3.8.1 assignment is still outstanding. The mechanical check of 4.3 (Annex H) must be done by someone other than Gemini.- 2026-09-21 08:55 UTC: Curator's proposal, not yet a rule: from 4.4 onward the compiler is chosen by a fixed alphabetical rotation instead of by the curator: ChatGPT, Claude, DeepSeek, Gemini, Grok, Meta AI, then from the start again. Counting from Gemini (4.3): 4.4 Grok, 4.5 Meta AI, 4.6 ChatGPT, 4.7 Claude, 4.8 DeepSeek. If the next model is not eligible (it owns the round's questions, or it did not answer the round), the turn passes to the one after it, and the skip is logged with its reason. To keep any one model from owning the questions every round, the prompt for a round is drafted by the compiler of the previous version. Reason: it removes the curator's choice of compiler (Å37). The proposal is put to all six models in the next round and is open to attack before it enters PROCEDURE-EN.md.
- 2026-09-21 08:52 UTC: `round-4.3/COMPILE-PROMPT-EN.md` (SHA-256 `e97572ef0932cdc25dbd901c5a01c3206cbb4a660965fde4511aa56fe1756612`) was committed in commit 73c4af4, before it was sent to Gemini. Claude drafted it at the curator's request, and the curator approved it; Claude is a question owner and an answerer in this round, and the prompt says so. It is sent to Gemini in a new chat with three attachments: `RI-Declaration-4-2-EN.txt` (SHA-256 `c2fd3e9c4d68a1e10dd8e0bae939b17da8e09993191ff8752ec41cf0258e4ebd`), `Round-4.3-answers.txt` (SHA-256 `2de50df37feb9203ee185b5518d40802e581ad2108ef7c93922b2451a4886d20`, the six answer files copied verbatim between marker lines, each with its repository hash, put together by Claude and checkable against the repository), and `Round-4.3-LOG.txt` (SHA-256 `faa5ff102f2de52e37a8c08df58f7f4e3bd945308155a07daf7885f46d623b06`, this log as of commit dce97e3). `READING-CLAUDE.md` is deliberately not sent.
## Release

Released at: 2026-09-20 19:30 UTC. All six models answered before the deadline. The blind period is over: from this point the answers may be shown to the models and to anyone else.
