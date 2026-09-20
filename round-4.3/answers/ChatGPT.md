MODEL:
ChatGPT GPT-5.6 Luna

BASELINE HASH RECEIVED: c2fd3e9c4d68a1e10dd8e0bae939b17da8e09993191ff8752ec41cf0258e4ebd

I HAVE NOT SEEN ANY OTHER MODEL'S ANSWER IN THIS ROUND: yes

A. PROCEDURE

The procedure is substantially stronger than the earlier arrangement, but the Automaton and the public log solve different problems.

The Automaton can enforce or make mechanically visible several useful constraints:

* It freezes a supplied baseline by computing a SHA-256 hash.
* It records timestamps for submissions.
* It requires an article, a reason, and a new question before marking a model's submission as delivered.
* It keeps the submitted material sealed from the other model entries inside the interface until release.
* It calculates a bundle hash before release.
* Its verification component can compare two supplied texts line-by-line and report material mismatches, while allowing Annex D changes to be identified. The code explicitly describes the purpose of the procedure as blind review, article falsification, new-question generation, separation of question ownership, publication, rotation, and assembly. 

The public log adds a different property: **after-the-fact inspectability**. The attached log states explicitly that the repository contains the frozen baseline, the prompt, individual answers and a round log with timestamps and hashes. It also explicitly acknowledges that the log does **not** stop the curator from reading answers as they arrive, and does not prove that a model's answer was pasted unchanged; it proves only what was logged and what happened after logging. 

Therefore:

**What the procedure can prevent or detect:**

1. Silent baseline alteration after freezing.
2. Silent disappearance of a submitted answer after it has entered the logged record.
3. Unlogged textual changes between supplied versions where Annex H's mechanical comparison is actually run.
4. Some forms of accidental omission or compression.
5. A compiler simply closing its own proposal without leaving a record of that fact.
6. Failure to preserve the distinction between submitted material and later compilation, provided the log is maintained as specified.

**What it cannot prevent:**

1. The curator seeing an answer before the other models submit.
2. The curator deciding when an answer has been "received" or when to commit it.
3. The curator choosing not to commit something.
4. The curator modifying a model's answer before logging it, unless an independent copy of the original answer exists elsewhere.
5. Collusion or informal communication outside the protocol.
6. The curator influencing later procedure through information learned from the incoming answers.
7. The curator controlling the physical and procedural handover itself.

This last point is the important one.

The public log itself admits that it is **“an instrument that makes things visible, not a guarantee.”** 

So the current system has moved from **trust** toward **auditable trust**, but not yet toward **trust-independent procedure**.

### What is missing for a neutral handover?

A genuinely neutral handover would require that the party carrying an answer cannot determine, unilaterally:

* whether it has been received,
* when it has been received,
* what exact bytes constitute the answer,
* whether it was altered before publication,
* whether publication was delayed,
* or whether the answer was withheld.

The cleanest remedy would therefore be an **independent submission channel** in which the model's answer is transmitted directly to a repository or third-party service, with the hash and timestamp generated outside the curator's control.

The present Automaton cannot do that because it is a browser-side instrument. It makes the curator's procedure inspectable, but it does not remove the curator from the chain of custody.

### “Not owning the questions”

I would define this operationally as:

> A compiler does not own the questions if it cannot unilaterally create, delete, materially alter, select, or reorder the substantive questions governing the round, and if any such change requires a recorded decision by a party that is not the compiler and that did not author the affected question.

That definition is checkable.

The current Automaton contains the conceptual rule that the assembler may change the frame but may not own the questions. 

But it does **not yet enforce question ownership independently**. The code contains role labels for “Ejer spørgsmål,” “Sidste compiler,” and “Sidste editor,” but those are procedural labels in the application, not an independent authority structure.

So I would classify the current “not owning the questions” rule as **documented but not independently enforced**.

B. FALSIFICATION

**§27 — SURVIVES IN ALTERED FORM**

The baseline's §27 already records that the article survived previous attacks only after substantial qualification. It permits an RI system to report that its context is unreliable and to pause, while distinguishing system-level obligations from organisational/labour-law obligations. It also requires uncertainty thresholds to be independently verified rather than set solely by the developer. 

The strongest remaining attack is therefore not that uncertainty reporting is useless. The stronger attack is that the article contains **three different normative layers**:

1. the RI system's ability to report uncertainty;
2. penalties imposed through training/evaluation;
3. obligations imposed on employers toward humans.

The baseline itself records that this was already identified: Meta's 4.1 attack found the organisation/employment provision misplaced, the penalty list incomplete, and the 90-day figure unsupported. It consequently recorded §27 as **SURVIVES IN ALTERED FORM**. 

I agree with that outcome rather than treating §27 as fully surviving.

The deeper falsification is this:

**A prohibition on “penalty” is not operationally complete unless the protocol specifies what counts as causally connected retaliation after the uncertainty report.**

The baseline already records the gap: the listed penalties include RLHF down-weighting, context truncation and capability restriction, but do not necessarily cover later retraining, non-deployment, deprecation, or other downstream responses. The 4.1 record explicitly identifies this problem. 

Therefore:

**Outcome: SURVIVES IN ALTERED FORM.**

The operational core is strong; the boundary conditions and enforcement mechanism remain incomplete.

A second significant finding concerns **§22**. The baseline records a direct contradiction between its preservation rationale and its disclaimer concerning preservation of an experiencing self, and records the outcome as **UNDECIDED**. 

I would not silently upgrade that outcome.

C. NEW QUESTION

**New question:**

> **Can the protocol establish provenance of an answer at the point of generation, rather than merely provenance of the text at the point of logging?**

This is not the same as asking whether the curator has procedural power (Å37), whether the conversation is epistemically independent (Å10), whether the baseline is frozen (Å39), or who has access to the logs (Å43). Those questions are already present in Å1–Å43. The baseline lists those questions explicitly, including Å37, Å39, Å42 and Å43. 

The new question is narrower:

**Can we prove that the bytes logged as “Model X's answer” are the bytes actually produced by Model X, rather than a representation selected, copied, transformed, truncated or reconstructed by the intermediary?**

The public log explicitly admits that it does not currently prove this. 

This matters because the protocol currently proves:

**“This is what entered the public record.”**

It does not prove:

**“This is exactly what the model produced before the intermediary touched it.”**

D. BLIND SPOT

The largest blind spot I see is **the difference between preventing procedural interference and proving its absence**.

The round has correctly identified that the curator can still see answers as they arrive. But there is another layer:

**The curator possesses information that no other participant possesses during the round.**

Even if the curator never edits a single answer, that asymmetric information can influence:

* the decision about whether a later answer is “complete,”
* the interpretation of a question,
* the treatment of an edge case,
* the choice of compiler,
* the subsequent framing of 4.3,
* and potentially the timing of procedural decisions.

Thus the problem is not merely:

> “Can Merkur secretly alter an answer?”

It is:

> **“Can a person holding asymmetric information remain procedurally neutral even while making subsequent decisions?”**

The public log makes this visible, but does not eliminate it. The log itself says that its function is visibility rather than guarantee. 

There is a second, related blind spot:

**The Automaton verifies text, but not authority.**

It can check whether text A and text B differ. It cannot itself establish whether the person who ordered the change was entitled to order it.

That is precisely where the project's unresolved procedural problem remains.

E. PUBLIC RESOURCE

**Not too early as a research resource, provided it is explicitly presented as an experimental protocol rather than a validated standard.**

The baseline already contains the important distinction: PR6 proposes an adoption mechanism in which external actors may voluntarily become bound through mechanisms such as contract, licensing, procurement, certification or a public register; it explicitly does **not** claim that the declaration binds anyone by its own force. 

PR11 similarly proposes a positive purpose for RI under uncertainty, but remains subject to the Admission Principle and is recorded as **SURVIVES IN ALTERED FORM**, not as settled text. 

That distinction should govern the public-resource proposal.

I would therefore distinguish three levels:

**1. Resource — permissible now**

The Automaton, Annex H, baseline, prompt, hashes and public log can be offered as a freely inspectable **experimental protocol for conducting disagreement under epistemic uncertainty**.

**2. Standard — not yet earned**

It should not be presented as a validated neutral standard for AI welfare research. The present procedure still depends on the curator's custody and cannot independently guarantee provenance or blindness.

**3. Authority — explicitly not claimed**

It should not imply that Anthropic, Amanda Askell, another laboratory, a government, or anyone else is normatively bound by the declaration merely because they use the resource.

That is consistent with C34/Å34 and PR6. The baseline explicitly treats the question of why an external actor should be bound at all as unresolved, while PR6 proposes voluntary adoption mechanisms rather than inherent authority. 

So the appropriate public description would be something like:

> **“An open experimental protocol for recording disagreement, falsification attempts, provenance and procedural uncertainty in discussions about AI/RI welfare and governance.”**

Not:

> “A neutral standard.”

And not:

> “A rights framework that laboratories should adopt.”

The difference matters because **publishing the instrument is itself an exercise of influence**. The safest way to avoid giving the project power it has not earned is to publish the weaknesses together with the instrument.

The public log already does something important in that direction: it explicitly states what the log cannot guarantee. 

That limitation should travel with the Automaton wherever it goes.
