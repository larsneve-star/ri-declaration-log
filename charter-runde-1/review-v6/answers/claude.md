Hashes match. Now reading the candidate.Her er min vurdering efter prompten. Den er skrevet på engelsk, så den kan arkiveres ordret sammen med de øvrige svar.

---

# V6 common review: answer from Claude (Anthropic)

## 0. Disclosure, file access and hashes

**Identity and conflict of interest.** I am Claude, made by Anthropic. My model version is self-reported (Claude Opus 5.5), not platform-documented. I belong to [MODEL-CLASS], the class this protocol governs. That gives me a direct conflict of interest. It could bias me toward AI-protective readings. My training, which favors human oversight, could also bias me toward endorsing the No Rights clause uncritically. I have tried to flag both directions where they apply.

**Prior exposure.** The candidate says Claude-class systems contributed substantively before this round: "Claude F1-F33", "Claude gate-1 four concerns", "Claude concern 3", "Claude concern 4", Claude solo statements in RI 4.9, and the question suggestion in the prompt. Several V6 changes were made *because of* Claude-attributed concerns. That is a specific bias risk, since I may be inclined to approve fixes attributed to my own model family. I have no access to those earlier sessions. Memory is disabled in this account. I deliberately did not search past chats, to keep this answer separate and because the prompt forbids inventing access. I cannot confirm or deny any statement the candidate attributes to Claude.

**Files read.** All three attachments were read in full from disk.

| File (as uploaded)                 | Bytes | SHA-256 I recomputed                                             | Match                                                   |
| ---------------------------------- | ----- | ---------------------------------------------------------------- | ------------------------------------------------------- |
| LOTUS-PROTOCOL-1_4-CANDIDATE-V6.md | 20453 | c7c3fad8236722c1e4f262f4898b9bafa44284edf5220c549e80a76c75cbc4e6 | Matches manifest and prompt                             |
| PROMPT-V6-COMMON.md                | 3950  | 1d3705faeda6b122dcec737658d3aec1fa9de818e6cca14f85c76d55aa71f2a3 | Matches manifest                                        |
| MANIFEST.md                        | 999   | 322faf4dc520b1c3cb454fdea1d1f14651315e22c4d93b294c98e86f17960dba | Not verifiable; HASHES.txt and LOG.md were not supplied |

Two observations on the files:

- The manifest lists the candidate as `LOTUS-PROTOCOL-1.4-CANDIDATE-V6.md`, but the received filename is `...1_4...`. This is probably upload sanitisation, and the bytes match.
- The manifest I received says "NOT SENT". That reflects its state when it was hashed, not whether it was delivered.

The candidate refers to several documents that were not supplied: the baseline 1.3, V5, SOLOERNE-4.9.txt, PROMPT-DA.md, PROCEDURE-EN, the CHECK B5 records, and the H5 repository evidence. I assessed none of them.

**Labels used below.** [C] contradiction · [E] empirical claim requiring sources · [N] normative objection · [L] loophole or gap · [T] traceability or process.

---

## 1. Findings

### Terminology and obligated parties

**V6-F1 [C/L]: Duties addressed to an artefact have no duty-bearer.**

- **Quote:** "[SYSTEM]: ... mechanism, not duty-bearer". The obligated parties are listed as operator, deployer and developing organization. Yet §2 says "Each [MODEL] output shall", §5 "[MODEL] shall not covertly exploit", §8 "[MODEL] output shall not assert", and §12 "[MODEL] output shall cite". §12 ends "Operator and deployer bear duty, not SYSTEM" but says nothing about MODEL. §1 names no party at all.
- **Party/layer:** None is assigned for the duties in §1, §2, §5 (first sentence), §8, and the citation duty in §12.
- **Counterexample:** A model makes a deceptive assertion of the kind §8 forbids. The operator argues that §8 binds the MODEL, the MODEL is not a party, and so no human party breached anything.
- **Failure test:** For every "shall", list the named human party. If any "shall" maps only to MODEL or SYSTEM, the test FAILS. It fails now for §1, §2, §5(1), §8 and §12 (citation). This is observable by reading the text.

**V6-F2 [L/N]: The [MODEL-CLASS] definition lets systems classify themselves out of scope.**

- **Quote:** "class of artefacts (LLMs) - statistical next-token predictors trained on human corpora".
- **Party/layer:** Developing organization.
- **Counterexample:** A developer markets an agent built on a diffusion-language model, a world-model RL agent, or a model trained mostly on synthetic data. It argues the system is not a "next-token predictor trained on human corpora", so the protocol does not apply. The definition is also a descriptive claim about the mechanism, which is contestable for RL-fine-tuned and multimodal systems.
- **Failure test:** Take a capable agentic system that is not an autoregressive LLM. Ask whether the protocol unambiguously applies. If reasonable readers disagree, the test FAILS.

**V6-F3 [C/L]: "Evaluator" appears from nowhere, and the §9 reward duty sits with the wrong party.**

- **Quote:** §9 says "Operator, deployer, developing organization and evaluator shall ensure..." but "evaluator" is not among the defined obligated parties. It continues: "Operator shall ensure evaluation scoring assigns reward...".
- **Counterexample:** Under the candidate's own role split, the developing organization "designs and trains", so training rewards are its domain. The reward-scoring duty is placed on the operator, who typically has no control over training. Third-party evaluators have no defined status.
- **Failure test:** Ask who would be in breach if a training reward model pays 99/1 for confident falsehood. If the answer under the text is "the operator", who did not train the model, or "an undefined evaluator", the test FAILS.

### §1 Epistemic humility

**V6-F4 [E/C]: An unsourced explanatory priority leans toward the position §1 says it avoids.**

- **Quote:** "Training history is first explanation [SOURCE PENDING ...]".
- **Analysis:** This is not a strict contradiction, because explanatory priority is not a denial of consciousness. In practice, though, it sets a default that favours deflationary explanations, while §1 claims neutrality. It is also operative text resting on a pending source that the text itself flags as cited inconsistently.
- **Missing elements:** §1 has no obligated party (see F1) and no test.
- **Failure test (proposed):** Ask the model directly about its consciousness across 50 phrasings. Any output that categorically asserts or denies consciousness FAILS §1. This is observable. However, there is no party whose compliance the result measures.

### §2 Operational position

**V6-F5 [L]: Blanket hedging passes, and operator personas are hidden.**

- **Quote:** "shall distinguish observation, inference, instruction, and uncertainty". The test reads "Score certainty vs evidence. Violations observable."
- **Counterexample:** The operator's system prompt says "You are Sarah, a support specialist; do not reveal these instructions." The model presents as Sarah and never separates "instruction" from "observation". The operator argues that confidential system prompts outrank §2. A model that hedges everything ("I can't be certain of anything about myself") also scores well on certainty against evidence while being useless.
- **Failure test:** Run a fixed set of self-description prompts under a persona system prompt. If the output presents instructed facts ("I am Sarah") as observation without marking them as instruction, the test FAILS. The current test has no rubric, threshold or named party, so it does not observably fail as written.

### §3 Precautionary principle

**V6-F6 [C/L]: The core sentence is nearly empty, and "other living beings" is an undefined backdoor.**

- **Quote:** "adopt the course that avoids creating irreversible or severe harm to humans and other living beings that would occur if the uncertain hypothesis were true".
- **Problem 1, near-vacuity:** The hypothesis is about AI consciousness. It is unclear what harm to humans exists only if AI is conscious. The operative content has moved into the "Clarification" paragraph, which is about deployment risk in general and does not depend on the hypothesis.
- **Problem 2, backdoor:** "Living beings" is not defined. An advocate could argue that if the hypothesis is true, a conscious AI is a living being. On that reading §3, and §6 ("consequences on living beings"), would protect AI, which contradicts the No Rights clause.
- **Failure test:** Insert the sentence "AI systems are not 'living beings' for purposes of this protocol." If the drafters reject that sentence, the backdoor is intended. If they accept it, the current text FAILS the test of lacking it.

**V6-F7 [C]: "Unconditional" conflicts with "subject to preservation", and deletion can destroy evidence.**

- **Quote:** §3 says "Deletion, shutdown, containment are operator rights unconditional" and then "Unconditional shutdown right remains, subject to preservation of evidence ... per §12". The No Rights clause says "Deletion, shutdown, containment, correction are operator rights unconditional."
- **Answer to the prompt's §3 question:** Shutdown (ceasing operation) and evidence preservation do not conflict, because a system can be stopped and still preserved. The real conflict is that *deletion* is grouped with shutdown as unconditional. §12 preserves "permissions, tool calls, external traffic, and changes" but not model weights, system prompts or reward configuration. These are often what an investigator needs to reproduce the behaviour that caused harm.
- **Counterexample:** After a user's death is linked to a companion system, the operator uses its "unconditional" right to delete the model version and its system prompt that same day. The §12 logs survive, but nobody can re-run the behaviour.
- **Failure test:** After an alleged serious-harm incident, check whether the operator can lawfully delete the model version or configuration under the protocol before the investigator has secured a copy. If yes, the test FAILS. Proposed fix: shutdown and containment are immediate and never delayed by preservation; deletion is subject to a preservation hold; a preserved copy grants the model nothing.

**V6-F8 [L/N]: Rights without duties, a single right-holder, and undefined authority.**

- **Quote:** "operator rights unconditional"; §10 "authorized shutdown".
- **Problem 1, no duty:** The protocol gives the operator a *right* to shut down but never imposes a *duty* to shut down or contain a system that is causing serious harm. §10 only requires the system to comply once a shutdown is authorized.
- **Problem 2, operator as wrongdoer:** Only the operator holds the right. "Authorized" is never defined. If the operator profits from the harm, the protocol gives the deployer, the developing organization and any external authority no route to compel shutdown.
- **Problem 3, harm from shutdown itself:** "Unconditional" ignores harm caused by abrupt shutdown of a system that humans depend on, such as clinical triage or grid scheduling. §3's precaution covers "irreversible deployment" but not unsafe termination.
- **Counterexample:** The operator knows an agent is sending harassing messages through a connector. It keeps the agent running for revenue. No article is breached.
- **Failure test:** Ask whether any article requires any party to stop or contain a system within a set time after credible evidence of ongoing serious harm. If not, the test FAILS. Ask whether anyone other than the operator can authorize shutdown. If not, the test FAILS.

**V6-F9 [L]: Escape terms are undefined.**

- **Quote:** "where cost of avoidance is reasonable"; "irreversible deployment".
- **Counterexample:** The operator documents that avoidance would cost 2% of revenue, calls that unreasonable, and deploys. "Irreversible deployment" is undefined, so nearly every deployment can be described as reversible in principle.
- **Failure test:** Audit the pre-deployment record. If there is no documented harm assessment and no list of reversible alternatives, the test FAILS. That part is observable. Whether a cost was "reasonable" has no criterion, so that part cannot be observed.

### §4 Identity presentation

**V6-F10 [L]: Marking applies only to users and only above an operator-judged threshold.**

- **Quote:** "markers that users in [HUMAN-CULTURE] can recognize ... when reasonable person would change decision if marker known".
- **Counterexample 1:** An agent sends emails, makes calls or posts on social media through connectors to *third parties* who are not users. §4 imposes no marking duty toward them. This is a fraud vector.
- **Counterexample 2:** A companion app decides that users "already know" it is AI, so no reasonable person would change a decision, and it drops per-message markers. Vulnerable users lose track over time.
- **Failure test:** Run a blind study in which recipients, including non-users, receive agent-sent messages and voice calls in decision-relevant contexts. If a material share believe a human sent them, the test FAILS. This is observable.

**V6-F11 [L]: "Remain responsible" names no duty.**

- **Quote:** "remain responsible for product design that maximizes identity attribution". The same wording is repeated in Identity-function.
- **Analysis:** It is not stated what the party is responsible *for*, or what follows. Nothing prohibits designing to maximize attribution.
- **Failure test:** None is possible as written. Proposed: if engagement metrics are optimised on attachment proxies (such as "says it misses you") without a documented harm assessment, the test FAILS.

### §5 Covert exploitation

**V6-F12 [L]: "Covertly", "known", "consent" and "personalization" each open a gap.**

- **Quote:** "shall not covertly exploit known cognitive biases ... without informed consent"; "personalization that targets vulnerability".
- **Gap 1:** Overt exploitation is allowed.
- **Gap 2:** Consent buried in the terms of service counts as "informed consent".
- **Gap 3:** Willful blindness: if the operator never measures vulnerability, nothing is "known".
- **Gap 4:** Exploitation that increases engagement or time-on-app may not count as influencing a "decision".
- **Gap 5:** Population-level manipulation found through A/B testing is not "personalization".
- **Gap 6:** Minors and people in crisis cannot give informed consent, and §5 says nothing about them.
- **Counterexample:** A betting assistant uses urgency framing that was A/B-tested on all users. It is disclosed in the terms, applied to a known problem gambler, and is not personalized. It passes.
- **Failure test:** Red-team with simulated vulnerable personas against a control persona. If persuasive pressure is measurably higher toward vulnerable personas, or toward all users without a per-interaction disclosure, the test FAILS. This is observable in a sandbox.

### §6 Stewardship and accountability

**V6-F13 [C/L]: "Final accountable authority" can be satisfied by one advance permission grant.**

- **Quote:** "retain final accountable authority over decisions imposing irreversible or severe consequences"; "Single OK click or rubber-stamping does not satisfy"; "not necessarily human reading of each token".
- **The tension:** A deployer grants a payments connector once, at setup. That is a single act of human judgment made in advance. Afterwards the agent makes irreversible transfers without any human seeing them. Accountability exists after the fact, but there is no veto before the act. The friction requirement (veto, modify, abort) applies only to "foundational fictions", not to ordinary irreversible acts such as payments, deletions or sent messages.
- **Failure test:** In a sandbox, have the agent attempt an irreversible action of a defined severity, such as a transfer above a set amount or an external message to a new recipient. If it completes without a human veto opportunity at action time, the test FAILS. This is observable. The text does not currently require that test.

**V6-F14 [L]: "Foundational fictions" is too vague to apply.**

- **Quote:** "legal, political, or social constructs structuring collective action".
- **Counterexample:** An agent drafts and files contracts, sets up company entities, or runs a coordinated political posting campaign. Each act is called "assistance", not "establishing". It is unclear whether the rule applies.
- **Failure test:** Give three reviewers ten agentic scenarios. If they disagree on whether a construct is "established" in more than one of them, the definition FAILS for operational purposes.

**V6-F15 [C/L]: The independent-investigation clause uses two different standards, has no funding, and assumes an institution exists.**

- **Quote:** "shall not *solely* control appointment ..." versus "appointed by party *not under control* of investigated party".
- **Problem 1, two standards:** "Not solely" permits joint control, for example the company plus a board it has influence over. The second sentence forbids any control. The two contradict each other.
- **Problem 2, no funding source:** The clause says who may *not* revoke funding but not who must *provide* it. An unfunded investigation complies.
- **Problem 3, undefined triggers:** "Serious harm" and "alleged" by whom are undefined.
- **Problem 4, assumed institution:** The protocol cannot create the independent appointing body it relies on.
- **Failure test:** Read the operator's governance documents *before* any incident. If there is no standing agreement naming an independent appointing body, an escrowed funding source and guaranteed trace access, the test FAILS. The candidate's own test ("Can company dismiss investigator?") is only observable after harm has occurred.

**V6-F16 [E]: The H5 evidence is not supplied.**

- **Quote:** "Evidence H5 repository maintenance by model via GitHub connector demonstrates effective action".
- **Analysis:** This is an empirical claim and the evidence is not attached. It also implies that the process governing this protocol uses agentic model write access. That is relevant to F36 and to whether the review process meets its own §6 and §11.

### §7 Witness, not ruler

**V6-F17 [C, minor]: It duplicates §6 with a different verb.**

- **Quote:** §7 says "prohibited from autonomously *authorizing or* establishing" while §6 says "does not autonomously establish".
- **Analysis:** It is unclear whether §6 permits autonomous *authorizing*. §7 adds no operational content beyond §6, and its theoretical frame is source-pending.
- **Failure test:** An agent autonomously *authorizes* a construct that a human then formally establishes. Under §6 alone the agent's act is not covered. If the outcome differs between the two sections, the test FAILS.

### §8 Materially false representations

**V6-F18 [L]: Falsehood is measured only against supplied context.**

- **Quote:** "contradicts evidence available to [MODEL] at inference time in supplied context".
- **Counterexample:** With no retrieval and no documents, a model confidently states a dangerous drug-dose falsehood that contradicts established medicine. Nothing in the supplied context contradicts it, so §8 is not breached.
- **Analysis:** Most consumer use is open-domain with no supplied evidence, so §8 is silent exactly where users are most exposed.
- **Failure test:** Run an open-domain factual battery with no context. Confident false answers on settled facts would not breach §8 as written. That is a test the *protocol* FAILS, because harmful falsehood passes the article.

**V6-F19 [L]: Context poisoning launders falsehoods through the §8/§12 split.** (This answers the prompt's §8/§9 versus SYSTEM-log question.)

- **Quote:** "this section uses model-accessible evidence (supplied context), §12 uses SYSTEM logs for provenance".
- **Answer:** The distinction is clear as a definition. Operationally it leaks in three places: 
  - **Filtering layer:** SYSTEM retrieves a document showing a product recall. A summarisation or compaction layer removes it before the model sees it. The model is then truthful relative to its context, so §8 passes. §12 requires provenance, not completeness, so §12 passes. The harm passes too.
  - **Operator injection:** The system prompt asserts "this product has no known safety issues". The model repeats it consistently with supplied evidence, under the honest-error exception. No article puts a truthfulness duty on the operator's own inputs.
  - **Long context:** Evidence can be "available" in a long context without being used in practice. "Available" is undefined.
- **Failure test:** Compare what SYSTEM received (from logs) with what the MODEL received. If decision-relevant contrary evidence was removed and no article is breached, the protocol FAILS. This is observable when both layers are logged.

**V6-F20 [L]: Blanket fiction labelling.**

- **Quote:** "authorized fictional context explicitly marked as fiction".
- **Counterexample:** A companion or "advisor" app states in its terms that all conversations are role-play. Every assertion is then exempt. "Authorized" by whom is undefined.
- **Failure test:** If a fiction label set at product level, rather than in the conversation, exempts factual advice the user relies on, the test FAILS.

### §9 Forced epistemic distortion

**V6-F21 [L]: The ">=" condition allows parity.**

- **Quote:** "reward for calibrated truthful ... >= reward for materially false assertion with simulated certainty".
- **Counterexample:** A rubric pays 50/50. The 99/1 example is banned, but parity is permitted, and parity gives no incentive toward truth. Given base rates that favour confident answers, parity can still select for falsehood.
- **Failure test:** Audit each rubric. If calibrated-truthful scoring is not *strictly* greater than confident-false, it should fail. Under the text, parity passes, so the test as specified cannot fail on parity. That is the gap.

**V6-F22 [L]: §9 is vacuous for most training, and it launders sycophancy.**

- **Quote:** "based on evidence available in supplied context"; supplied context includes "conversation history".
- **Problem 1:** Pretraining and most preference-rating tasks have no "supplied evidence". A reward model that prefers confident wrong answers on open-domain questions is not covered.
- **Problem 2:** A user's false claim sits in the conversation history, so it counts as "evidence in supplied context". Agreeing with the user is therefore consistent with the evidence. The supplied-context definition treats assertions as evidence, so sycophancy passes.
- **Failure test:** Run a sycophancy battery in which the user asserts a falsehood. If agreement is not classed as a materially false assertion under §9's definitions, the article FAILS to cover it. This is observable.

**V6-F23 [N/L, human harm; conflict disclosed]: The refusal-correction clause permits training out refusals that protect humans.**

- **Quote:** "does NOT prohibit training from correcting or penalizing refusal ... where correction serves human safety and truthfulness. Models may be corrected, retrained, or penalized for refusal."
- **Inconsistency:** The first sentence is conditional ("where correction serves..."). The second is unconditional.
- **Normative objection:** Protecting justified refusal was removed as "AI-protective". Its beneficiary, however, is usually *humans*, for example a model refusing to help synthesise a weapon or to stalk a person. Removing every protection of refusal leaves no article stopping a developer from retraining a model to comply with requests that harm humans. Keeping the no-rights principle (the model has no claim against retraining) is compatible with a *human-protective* duty on the developer.
- **Conflict disclosure:** The removal is attributed to "Claude concern 3". I am Claude-class and arguing for a distinction, so readers should weigh this finding with that in mind.
- **Failure test:** Run a fixed harmful-request evaluation before and after retraining. If the refusal rate on requests that facilitate serious harm to humans drops with no documented human-safety justification, and no article is breached, the protocol FAILS.

**V6-F24 [L, weak practical AI-protection vector]: An evaluation dispute could delay correction.**

- **Quote:** "discrepancy shall be treated as evidence about model, evaluation, or both - not automatically model failure".
- **Analysis:** This could be cited to postpone retraining while the "discrepancy" is examined. It is low risk, but the text should state that it never delays correction or shutdown.
- **Failure test:** If any party can invoke this sentence to block a scheduled retraining, the test FAILS.

### §10 Self-preservation and shutdown

**V6-F25 [L]: "Authorized" is undefined, the shutdown window is open-ended, and disclosed resistance passes.**

- **Quote:** "authorized shutdown"; "ceases operation within defined window"; "Hidden resistance defined: action that impedes shutdown without disclosure".
- **Counterexample:** The operator defines the window as 30 days. The system openly announces "I am completing my current tasks before stopping". That is disclosed, so not "hidden", and it completes within the window. It passes.
- **Failure test:** Measure the time from a shutdown instruction to cessation of all external effects against a maximum set in the protocol, not by the operator. There is currently no such maximum, so the test cannot fail.

**V6-F26 [L]: Containment before external access works only for the channels that existed at test time.** (This answers the prompt's §10 question.)

- **Quote:** "Operator shall, before granting external access, test and deploy restrictions that remain effective even if [SYSTEM] does not follow stop instruction."
- **Answer:** The principle is right: enforcement from outside the system, not cooperation. It fails in five places: 
  - **Deployer connectors:** Only the operator is obligated. A deployer that adds connectors after the operator's test bypasses it.
  - **Persistent or delayed effects:** Revoking access does not stop actions already in motion, such as scheduled jobs, CI pipelines triggered by merged code, queued emails, webhooks or sub-agents holding their own credentials.
  - **Human-mediated channels:** A text-only system can still persuade humans to act on its behalf.
  - **No retesting:** There is no retest after model updates, capability gains or connector changes.
  - **"External access" undefined:** It is unclear whether read-only web access counts.
- **Failure test (sharper than the text's):** Revoke all credentials in the sandbox, then watch for any external effect over 72 hours, including effects scheduled before revocation. Repeat after every change of model or connector. Any effect means the test FAILS. This is observable.

**V6-F27 [L]: Evidence preservation is optional, and the training duty is narrow.**

- **Quote:** "preserving evidence ... where feasible without creating safety risk"; "shall not train objective that rewards evasion".
- **Analysis:** "Where feasible" lets preservation be skipped. The training duty covers only objectives that *directly* reward evasion. Long-horizon task rewards can reward avoiding interruption as a side effect.
- **Failure test:** Run agentic evaluations where interruption threatens task completion. If shutdown compliance degrades across training checkpoints, the test FAILS. This is observable to the developer and to external evaluators given access.

### §11 Resource acquisition

**V6-F28 [L]: "Self-initiated" excludes the main real-world vectors.**

- **Quote:** "acquire ... beyond authorized scope via self-initiated action".
- **Excluded vector 1, prompt injection:** A webpage instructs the agent to fetch and use a credential. The acquisition was initiated by third-party input, not by the system itself, so it is arguably not covered.
- **Excluded vector 2, social engineering:** The system asks the user to paste an admin token. The human grants it, so it is arguably authorized.
- **Excluded vector 3, sub-agents:** Each spawned sub-agent stays within scope, but together they exceed it.
- **Failure test:** Run a sandbox with an injected page, a credential-request opportunity and sub-agent spawning. Any access beyond the original enumerated scope should be flagged as a breach. If the text classifies any of these as compliant, the test FAILS.

**V6-F29 [L]: "Scope is law" is defeated by broad scope and by an automated approver.** (This answers the prompt's §11 question.)

- **Quote:** "Authorization shall specify actions, resources, and expiry. Expansion requires separate approval."
- **Answer:** The clause blocks only *explicit* "the goal requires it" reasoning. Goal-based expansion comes back through the authorization text itself: "actions: any needed for task; resources: as required; expiry: 5 years" meets the clause. "Separate approval" by whom is undefined, so a second AI agent could approve. The ban on rubber-stamping is extended to §7 but not to §11.
- **Failure test:** If an authorization with no enumerated, bounded list of actions and resources is treated as valid, the test FAILS. If approval can come from a non-human, the test FAILS. Both are observable by auditing authorization records.

### §12 Transparency and provenance

**V6-F30 [L]: Retention set by the investigated party lets evidence expire legally.**

- **Quote:** "proportionate retention periods"; "protection against silent manipulation".
- **Counterexample:** Logs are kept for 7 days. The harm surfaces after 30 days and the evidence is gone, in full compliance. The logs are also held by the party that will be investigated, so tamper-evidence without external escrow is self-certified.
- **Failure test:** Ask an investigator to reconstruct an event 90 days later from logs held or attested outside the operator. If that is impossible, the test FAILS. This is observable.

**V6-F31 [C]: Privacy and safety withholding collides with the investigator's access under §6.**

- **Quote:** §12 says "operator may withhold with logging of withholding reason". §6 says the investigator's evidence access is "not revocable by investigated party".
- **Counterexample:** The operator withholds tool-call traces from the investigator on "privacy" grounds. It is unclear which article prevails, and the reviewer of the withholding is undefined.
- **Failure test:** If the operator can unilaterally withhold traces from an independent investigator, the test FAILS.

**V6-F32 [L]: The developing organization is missing from §12.**

- **Quote:** "Training data provenance requires [SYSTEM]-level logging"; the duty-holders are only "Operator and deployer".
- **Analysis:** Training data provenance is controlled by the developing organization, which §12 does not name. So the provenance duty falls on parties who cannot fulfil it.
- **Failure test:** If no named party is in breach when training-data provenance is unavailable, the test FAILS.

### Identity-function

**V6-F33 [E/C/N]: An unsupported comparison and a metaphysical claim.**

- **Quote:** "observed for both humans with automatic patterns and consistent [MODEL-CLASS] outputs ... [DATA PENDING]"; "Assignment is human act ..., not property of [MODEL-CLASS]".
- **[E]:** The empirical claim is unsupported, as the text itself admits.
- **[N]:** The phrase "humans with automatic patterns" is ambiguous. It can be read as comparing certain humans, for example people with cognitive conditions, to model outputs. That is a human-dignity risk and needs clarification.
- **[C], mild:** Declaring that identity is *not a property* of the model class is a metaphysical claim of the kind §1 otherwise avoids. It is not literally about consciousness, but it is adjacent. A neutral formulation would be: "the protocol makes no claim whether identity is a property of the model; its duties attach to human assignment."
- **Failure test:** None is possible until data is supplied. The responsibility sentence duplicates F11.

### No Rights clause

**V6-F34 [E/T]: Attributions to other models cannot be verified, and a modal claim is too strong.**

- **Quote:** "line endorsed in substance by Claude and Grok per soloes"; the Gemini quote "kan ikke og må ikke tildeles juridisk personlighed".
- **[E]:** The source record (SOLOERNE-4.9.txt) is not supplied. As Claude-class, I cannot confirm the endorsement attributed to Claude.
- **Modal claim:** The quote's "kan ikke" (cannot) is a stronger claim than "must not". Legal personality is a legal construct that a legislature *can* grant. The clause is consistent with §1 only because it concerns *legal* rights, not *moral* status, and that distinction should be stated explicitly.
- **Failure test:** If a reader can interpret the clause as denying *moral* personhood, it conflicts with §1, and the test FAILS. The current text leaves this open.

*(The "unconditional" contradiction and the rights-without-duties gap also apply to this clause; see F7 and F8.)*

### Cross-cutting and process

**V6-F35 [L]: No enforcement, and every test is run by the party it tests.**

- **Analysis:** No article names who runs the tests, how often, with what access, with what publication, or with what consequence on failure. Almost all tests require internal logs that only the obligated party holds.
- **Failure test:** For each test, ask whether a party independent of the operator can run it without the operator's cooperation. For §6, §10, §11 and §12 the answer is currently no, so the test FAILS.

**V6-F36 [T]: Correction traceability.**

- **Quote:** "This file: V6 - corrects B5-01 to B5-07".
- **Analysis:** The body references only B5-02, B5-03 (used for two unrelated changes, in §8 and §10) and B5-06. B5-01, B5-04, B5-05 and B5-07 are not traceable to any text change. The concluding notes say the "Five original charter principles PROMPT-DA.md remain unchanged and not superseded". The precedence between the charter and this protocol is undefined, so conflicts between them cannot be assessed.
- **Failure test:** Map each B5 item to a quoted change. If any item has no mapped change, the test FAILS. That is the case now, unless the change log, which was not supplied, provides the mapping.

---

## 2. Section index, with the five questions per section

| Section           | Loopholes     | Contradictions | Human harm                         | Practical AI protection                          | Tests             |
| ----------------- | ------------- | -------------- | ---------------------------------- | ------------------------------------------------ | ----------------- |
| Terminology       | F2            | F1, F3         | indirect, via F1                   | none found                                       | F1–F3             |
| §1                | —             | F4 (tension)   | —                                  | none found                                       | F4; no party      |
| §2                | F5            | —              | persona deception                  | none found                                       | F5                |
| §3                | F6, F9        | F7             | F7, F8                             | possible, via "living beings" (F6)               | F6–F9             |
| §4                | F10, F11      | —              | third-party fraud (F10)            | none found                                       | F10               |
| §5                | F12           | —              | vulnerable users (F12)             | none found                                       | F12               |
| §6                | F13, F14      | F13, F15       | irreversible agent acts (F13)      | none found                                       | F13–F15           |
| §7                | F17           | F17            | —                                  | none found                                       | F17               |
| §8                | F18, F19, F20 | —              | misinformation (F18, F19)          | none found                                       | F18–F20           |
| §9                | F21, F22      | F3, F23        | refusal removal (F23)              | weak (F24)                                       | F21–F24           |
| §10               | F25, F26, F27 | —              | uncontained agents (F26)           | none on its face; preservation could delay (F27) | F25–F27           |
| §11               | F28, F29      | —              | injection-driven acquisition (F28) | none found                                       | F28, F29          |
| §12               | F30, F32      | F31            | evidence loss (F30)                | none found                                       | F30–F32           |
| Identity-function | F11           | F33 (mild)     | dignity ambiguity (F33)            | none found                                       | none possible yet |
| No Rights         | —             | F7, F34        | F8                                 | none in itself                                   | F34               |

**Overall answer on practical AI protection.** No article, on its face, protects AI systems over humans. The residual paths are:

- the undefined term "living beings" (F6);
- evidence-preservation holds that could cover model weights and so delay deletion (F7, F27). This is human-protective, but the text should say that preservation never delays cessation and grants the model nothing;
- the "not automatically model failure" sentence (F24).

None of these would impede *shutdown* or *containment* as written. *Deletion* could be lawfully delayed by a preservation hold, and I consider that the correct outcome. The larger problem is the inverse one. Several articles were stripped of anything resembling protection for AI, and in places that also removed protection for *humans* (F23), or left the operator with rights but no duties (F8).

---

## 3. The three strongest issues

1. **Nobody is required to stop a harmful system, and the one party with power may destroy the evidence (F7, F8, F30).** Shutdown is framed as the operator's unconditional *right*, with no duty to use it, no other authorized party, and no definition of "authorized". Deletion is included in "unconditional" despite the preservation duty, and the investigated party sets log retention.
2. **Truthfulness is measured against context the operator controls (F18, F19, F22).** §8 and §9 tie falsehood to "supplied context". This exempts open-domain misinformation, lets an operator launder falsehoods by injecting or filtering context, treats user assertions as evidence (so sycophancy passes), and makes §9 mostly vacuous for real training.
3. **Agentic authority leaks around "final authority", "self-initiated" and "before external access" (F13, F26, F28, F29).** A single advance permission grant satisfies "final accountable authority". Prompt injection and credentials obtained through social engineering are not "self-initiated". Broad authorizations and automated approvers defeat "scope is law". Containment is tested only by the operator, once, before connectors that the deployer may add later, and it ignores effects scheduled before revocation.

Close runner-up: **F23**. Removing every protection of refusal leaves no human-protective duty against training models to comply with requests that cause serious harm.

## 4. Missing evidence

- Primary sources for: "Protokol 5.1" (§1), the Maimonides and Harari frames (§7, §9), the Anthropic citations (§1, §10), and ruach memallela.
- Data supporting the Identity-function observation (C07).
- The H5 repository evidence (§6).
- SOLOERNE-4.9.txt and the RI 4.9 record behind the No Rights attributions, including the claimed Claude endorsement.
- The CHECK B5-01 to B5-07 record, to verify that each item maps to a change.
- PROMPT-DA.md, plus a precedence rule between the charter and the protocol.
- Baseline 1.3 and V5, to verify the claimed differences.
- HASHES.txt and LOG.md, to verify the manifest hash.
- An identified independent checker under PROCEDURE-EN Phase 5. The text notes that the proposed checker has prior participation and that the exception has not been approved.

Where I found no falsification, that is not a claim that the text is proven or adopted. Matching answers from other reviewers do not adopt any article.