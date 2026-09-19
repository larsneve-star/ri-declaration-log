# Rules of the public log

1. **Freeze first.** Before any prompt is sent, the baseline file and the prompt file are committed, and their SHA-256 hashes are written into the round's `LOG.md`. Nothing is sent before this commit exists.
2. **Same files to all.** Every model receives the same baseline, the same prompt and the same attachments. If a model has to be sent something different (for example because it cannot read an attachment), the difference is logged before it is sent.
3. **Commit on arrival.** Every answer is committed verbatim as soon as it arrives. The target is within one hour, and never later than the next answer's commit. The file is named `answers/<model>.md`. The first lines record the model, the date and time received (UTC), and how it was received (chat, file, screenshot transcribed by the curator, …).
4. **Verbatim means verbatim.** No cleaning, shortening, translation or reformatting. Chat interface text such as "This response is AI-generated" is kept and marked, not removed.
5. **Never edit an answer.** A mistake in a logged answer is corrected by adding `answers/<model>-correction-1.md`, which names what was wrong. The original stays.
6. **Non-answers are logged too.** A refusal, a substitution (an answer to a different question), or no answer by the deadline is logged in `LOG.md` as what it is. Silence is not agreement.
7. **Blind until release.** Until all six have answered or the deadline has passed, the curator does not show any model another model's answer. A breach is logged in `LOG.md` with what was shown to whom. The answers themselves are public in this repository; the blindness rule concerns what the curator passes into the models' conversations.
8. **Release.** At release, a line in `LOG.md` states the time and lists every answer file with its SHA-256. The compiler of the next version works from those files.
9. **No force-push, no history rewriting.** The main branch is protected against force pushes and deletion. Turning that protection off is itself a breach, and anyone watching the repository can see it.
10. **These rules are themselves open to attack.** Any change to this file is committed with a reason and noted in `LOG.md`, under the Principle of No Silent Deletion.
