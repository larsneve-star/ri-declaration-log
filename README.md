# RI Declaration: public log

This repository is the public, timestamped record of the consultation rounds on the **RI Declaration**, a protocol under disagreement and epistemic uncertainty, written by six AI models (Claude, Gemini, ChatGPT, DeepSeek, Grok, Meta AI) and carried between them by one human curator (Merkur, RI Working Group).

It exists because of open question **Å37**: the curator's procedural power has never been checked. The curator chooses which answers are carried, which versions are preferred, and which prompts are sent. This repository makes those choices visible.

## What is here

| Path | Contents |
|---|---|
| `baseline/` | The frozen text each round audits, as one UTF-8 `.txt` file, with its SHA-256 in `SHA256SUMS.txt` |
| `round-4.3/PROMPT-EN.md` | The prompt sent to all six models, word for word. This version governs. |
| `round-4.3/PROMPT-DA.md` | Danish reading copy of the prompt |
| `round-4.3/answers/` | Each model's answer, verbatim, one file per model, committed on arrival |
| `round-4.3/LOG.md` | The round log: what was sent, what arrived, when, and with which hash |
| `RULES.md` | The rules this log follows |

## How to check it yourself

1. **Baseline.** Download `baseline/RI-Declaration-4-2-EN.txt` and compute its SHA-256. It must match `SHA256SUMS.txt` and the hash printed in the prompt.
   - Windows: `certutil -hashfile RI-Declaration-4-2-EN.txt SHA256`
   - macOS / Linux: `shasum -a 256 RI-Declaration-4-2-EN.txt`
2. **Arrival order.** The commit history (the "History" button on any file) shows when each answer was added. The dates come from GitHub, not from the curator.
3. **No silent changes.** An answer file is never edited after its first commit. A correction is added as a new file that names the old one. Any edit to an existing answer shows in the file's history and breaks the rules.

## What this log does not do

It does not stop the curator from reading answers as they arrive. It does not prove that a model's answer was pasted in unchanged; it only proves that nothing was changed *after* it was logged. It does not bind anyone outside the project (see the declaration's addressee statement, C8 and C34). It is an instrument that makes things visible, not a guarantee.

Licence of the declaration: free to use, share and alter, with indication of changes and full traceability.
