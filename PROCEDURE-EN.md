# How a round is run

This describes the procedure used from round 4.3 onward. It is not a standard and binds no one. It is the working method of this project, written down so that it can be checked and attacked. Every step leaves a trace in the public log.

## Phase 0 — Freeze

1. Create a folder for the round: `round-X.Y/`, with an `answers/` folder inside it.
2. Place the version to be audited in `baseline/` as one UTF-8 .txt file, delivered in one piece.
3. Record its SHA-256 in the round's `LOG.md` under Freeze.
4. Confirm that the main branch is protected against force pushes and deletion.

Nothing is sent before this commit exists.

## Phase 1 — Prompt

1. Write the prompt as a file in the round folder. State in it: the baseline file name and hash, the deadline, the link to the public log, the tasks, and the answer format.
2. Name the question owners in the prompt itself: whoever drafted it, whoever approved it, whoever chose which articles are put up for attack.
3. Commit the prompt, then compute its SHA-256 and record it in `LOG.md` under Freeze.
4. The prompt is not edited after the first model has received it. If it must be changed, the change is a new version with a new hash, and every recipient is told, and the deviation is logged per model.

## Phase 2 — Send

1. Send the same three artefacts to all six models: the baseline as a file, the prompt, and any attachment named in the prompt.
2. Deliver the baseline as a file, not as a name in the prompt. In round 4.3 two of six models answered without it, and both said so; one of them reasoned about articles it had not seen.
3. For each model, record in the Sent table: the time in UTC, what was actually sent, and any deviation, in the model's own row.

## Phase 3 — Receive

1. Commit each answer verbatim as soon as it arrives, as `answers/<model>.md`. Target: within one hour of arrival.
2. Record in the Received table: the model, the time in UTC, the file path, the file's SHA-256, and the status: answer, substitution, refusal, or missing.
3. An answer is never edited after its first commit. Curator metadata belongs in the log, not inside the answer.
4. A non-answer is logged as what it is. Silence is not agreement.
5. Every mistake made while handling the round is written under Breaches and notes, with the time and what happened. Corrections are additions, never deletions.

## Phase 4 — Release

1. Release when all six have answered or the deadline has passed, whichever comes first.
2. Write the release time in `LOG.md`.
3. Only after that may any answer be shown to another model or to anyone outside the round.

## Phase 5 — Verification

1. The mechanical check in Annex H is performed by a party who did not compile the version under check. It may be a human.
2. The result is recorded in the log with the verifier's name, the date, the hashes checked, and the count of lines present, altered and missing.
3. A version that has not been verified is not used as a frozen baseline.

## Phase 6 — Compiler

1. The compiler of the next version may not be: a question owner of the round, the curator, the compiler of the previous version, or the editor of the previous version.
2. The choice and its reason are recorded in the log before compilation begins.

## Phase 7 — Compile

1. The compiler works from the committed files, not from memory.
2. It may not admit its own proposals as article text, and may not close its own objections.
3. Every change to the frame is logged in Annex D in the compiler's own name.
4. Where a passage cannot be reproduced exactly, it is marked, not paraphrased.

## Phase 8 — Next freeze

The compiled version becomes the baseline of the next round, with its own hash, and the cycle begins again at Phase 0.

## Standing rules

- All times in UTC.
- Everything that is sent or received is hashed.
- Nothing is removed from the record; the record is corrected by addition.
- What the procedure cannot do is stated wherever it is offered: the curator still carries the texts and reads every answer as it arrives, the log proves what was committed and not what was produced, and the repository owner can disable its own protections.
