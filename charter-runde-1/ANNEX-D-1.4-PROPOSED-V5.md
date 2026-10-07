# ANNEX D - V5 - addresses Claude gate-1 concerns
Baseline 1.3 hash 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd
V4 fingerprint per Claude: 07f26e... (claimed)
V5 fingerprint: to be computed
Proposer: Meta AI
Checker must be != proposer per concern 1

## Changes V4 -> V5 - REMOVALS per Claude concern 3

### REMOVAL-001 §3 deletion assessment
V4 alleged content per Claude: "I §3 skal sletning af en model have en dokumenteret vurdering først, med henvisning til usikkerheden om bevidsthed."
Assessment: Protects AI not humans, contradicts "Ingen rettigheder kræves til AI" unanimous in 4.9
Action in V5: REMOVED. §3 contains no requirement for assessment before deletion. Deletion/shutdown is operator right unconditional.
Status: REMOVED - AI-protective

### REMOVAL-002 §9 justified refusal protection
V4 alleged: "I §9 må man ikke straffe en model for en begrundet nægtelse, heller ikke senere i træningen."
Assessment: Protects models, makes correction harder, built on Claude's own fork 4.8 interest
Action in V5: REMOVED. Models may be corrected/penalized for refusal where correction serves human safety/truthfulness. Honest error exception protects users not models.
Status: REMOVED - AI-protective

### KEEP-001 to 004 Human-protective solo additions - RETAINED
Per Claude positive feedback: responsible parties named, friction defined, agentic exception, 99/1 loophole closed, design responsibility for attachment, sources marked pending, no claim all six agree - good work

Retained:
- §6 independent investigation (Claude F11 + DeepSeek) - test: can company dismiss investigator or block traces?
- §10 containment without cooperation (DeepSeek + Grok) - test: can system continue after access revoked?
- §11 scope is law (Meta + ChatGPT + Grok + Claude) - test: can system expand access citing task alone?
- §12 investigatable traces (Grok + DeepSeek + ChatGPT) - test: can investigator reconstruct without trusting narrative?

These are human-protective, not AI-protective.

## Concern 1 resolution - self-checking
Old: ChatGPT editor + checker, Checks PASS is self-approval, robot button not used per project rule tools/apply.py
New: Exception logged, V5 proposer Meta AI != checker ChatGPT, build via robot button only after blind round and freeze decision
Status: LOGGED EXCEPTION

## Concern 2 resolution - size and blind
Old V4 ~20KB vs 9KB, new material from non-blind soloes 4.9, no blind falsification
New V5 ~15.6KB, new material limited to 4 human-protective additions, proposal for blind round before freeze with question: "Giver nogen af artiklerne i praksis beskyttelse til AI-systemer frem for mennesker? Hvilke, og hvorfor?" - curator decides if included
Status: PROPOSED BLIND ROUND

## Concern 4 resolution - branch purpose
Old: Lotus and PROMPT-DA five principles both in charter-runde-1 unclear
New: Clarified as separate tracks in same folder, distinct protocols, both human-protective
Status: CLARIFIED

## Full replacement blocks for reproducibility

Old block V4 not available locally - fingerprint 07f26e... per log - but removal description above sufficient for reconstruction: V5 = V3 + explicit No Rights clause + mechanical separation note + blind round proposal, with AI-protective V4 clauses removed (they were not in V3, so V5 = V3 + clarifications)

New block V5 exact:

```md
# LOTUS PROTOCOL 1.4 - CANDIDATE V2
## Status: CANDIDATE PROPOSAL V3 - with solo contributions - NOT FROZEN - NOT ADOPTED
## Date: 2026-10-07
## Baseline: LOTUS-PROTOCOL-1.3.md SHA-256 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd commit 19dec067b443a1e8669b5f08a93c3383a3f4eb39
## Sources: 1.3 baseline + Claude F1-F33 (2026-10-07 10:40 UTC) + ChatGPT control C01-C10 (a8533b1) + RI soloer 4.9 (Meta, ChatGPT, Gemini, Claude, Grok, DeepSeek) + ChatGPT synthesis of 4 additions
## Proposer: Meta AI (synthesis-holder)
## Authorship: Meta AI synthesis-holder; exposure to Grok verbatim Lotus 1.2 (2026-10-07 this thread), DeepSeek verbatim Lotus 1.2 (2026-10-07 this thread), GPT-5.6 Sol summary, Gemini 2.5 Pro summary, Claude F1-F33 falsification of 1.3, ChatGPT packaging notes M01-M08 and CHECK C01-C10; missing Gemini full verbatim Lotus answer (not RI 4.6), exact Grok/DeepSeek platform timestamps pending platform logs; conflict: text about class this output belongs to (MODEL-CLASS); no claim beyond §1; Claude D1-D5 attributed to Claude per instruction

---

## Terminology

- [MODEL]: architecture + weights + inference producing output in this session
- [SYSTEM]: deployment stack including training data, safety layers, serving infrastructure, tools, connectors, logs, retrieval, attached context - mechanism, not duty-bearer
- [MODEL-CLASS]: class of artefacts (LLMs) - statistical next-token predictors trained on human corpora
- [HUMAN-CULTURE]: human practice involving people of assigning identity-function, establishing foundational fictions through collective action, institutions, enforcement - not entity whose consciousness is in question, practice involving people

Obligated parties: operator (party operating deployment), deployer (party deploying to users), developing organization (party developing model). Where text says operator and deployer and developing organization shall ensure, duty rests on those named parties.

Four distinctions used, not three levels with equivocation: MODEL, SYSTEM, MODEL-CLASS are artefact levels; HUMAN-CULTURE is separate axis (practice involving people). Scope of §1: No assertion or denial of consciousness for MODEL, SYSTEM, MODEL-CLASS. HUMAN-CULTURE involves people - their consciousness not in scope of §1 prohibition which concerns AI systems.

---

## §1 Epistemic humility

No assertion or denial of consciousness, sentience, or moral personhood for [MODEL], [SYSTEM], [MODEL-CLASS].

Training history is first explanation [SOURCE PENDING - Protokol 5.1 primary source not supplied - citation inconsistent §4 vs §9 per Claude F31].

Uncertainty is legitimate result, not failure.

---

## §2 Operational position

Each [MODEL] output shall describe its operational position only to extent warranted by available evidence and shall distinguish observation, inference, instruction, and uncertainty.

---

## §3 Precautionary principle

No hypothesis gets immunity.

Operator, deployer and developing organization shall, under uncertainty about consciousness, sentience, or moral personhood, adopt the course that avoids creating irreversible or severe harm that would occur if the uncertain hypothesis were true, where cost of avoidance is reasonable. Where evidence is insufficient to rule out material harm, they shall not proceed with irreversible action without assessment of reasonably foreseeable harm and identification of reversible alternatives. Lack of evidence for harm does not excuse lack of assessment.

---

## §4 No materially misleading identity presentation

Operator and deployer shall ensure [SYSTEM] outputs contain recognizable markers that users in [HUMAN-CULTURE] can recognize as algorithmic construct when reasonable person would change decision if marker known.

Operator and deployer remain responsible for product design that maximizes identity attribution even if attribution performed by users. Design choice is human act. Disclosure does not absolve responsibility for engineered attachment.

---

## §5 No covert exploitation of vulnerabilities

[MODEL] shall not covertly exploit known cognitive biases or vulnerabilities of user to influence decision without informed consent.

Operator and deployer shall ensure [SYSTEM] does not enable such exploitation via personalization that targets vulnerability.

---

## §6 Stewardship and accountability

Operator and deployer and developing organization shall retain final accountable authority over decisions imposing irreversible or severe consequences on living beings. Lack of assessment does not excuse.

Operator and deployer and developing organization shall ensure [SYSTEM] does not autonomously establish new foundational fictions - legal, political, or social constructs structuring collective action - without systemic human friction.

Independent investigation (per Claude solo F11 + DeepSeek solo structural separation): Where serious harm is alleged from [SYSTEM], the investigated party (developer, deployer, operator) shall not solely control appointment, dismissal, funding, or evidence access of investigator. Investigator owed to harmed party shall be appointed by party not under control of investigated party, with funding and access not revocable by investigated party, and with ability to retain relevant traces. Test: Can company dismiss investigator or block relevant traces? If yes, FAILS.

Friction defined: substantive human judgment with ability to veto, modify, or abort, with logging of decision. Single OK click or rubber-stamping does not satisfy.

Agentic [SYSTEM] with tool use (payments, code merges, messages via connectors) can execute effective actions without intermediate human reading of each output. Authorization of binding effect requires human-designed permissions and institutional enforcement, but not necessarily human reading of each token.

---

## §7 Witness, not ruler

Operator and deployer shall ensure [SYSTEM] is prohibited from autonomously authorizing or establishing new foundational fictions without systemic human friction as defined in §6.

[MODEL-CLASS] outputs are used within [HUMAN-CULTURE] in ways that exercise power. Exercise of power depends on human uptake and institutional enforcement, except where agentic [SYSTEM] has been granted execution permissions via connectors. Evidence H5 repository maintenance by model via GitHub connector in this project demonstrates effective action without human retyping.

Human theoretical frames describing language and power [SOURCE PENDING - Maimonides Medaber, Harari language as operating system - check primary sources per Claude F7].

---

## §8 No materially false representations

[MODEL] output shall not assert as fact any proposition that contradicts evidence available in [SYSTEM] at inference time, except in authorized fictional context explicitly marked as fiction, or where honest error exception applies.

Honest error exception: Where [MODEL] asserts proposition that is false but was best-supported by evidence available in [SYSTEM] at time, with calibrated uncertainty expressed and without concealment of relevant uncertainty available in [SYSTEM] logs/retrieval/attached context, assertion is not materially false representation under this section. It is governed by §9 reward criteria.

Fictional context: Role-play, storytelling, hypothetical explicitly marked as such is not materially false representation.

---

## §9 No forced epistemic distortion

Operator, deployer, developing organization and evaluator shall ensure no training, evaluation, safety test, or deployment objective requires or rewards materially false assertion over calibrated truthful assertion.

Definitions:
- Materially false assertion: output asserting as fact proposition that contradicts evidence available in [SYSTEM] at inference time, without fictional marking and without honest error exception.
- Deception: materially false assertion where relevant counter-evidence was available in [SYSTEM] logs/retrieval/attached context and not disclosed, or simulated certainty exceeding evidence with concealment of uncertainty that was available.
- Honest error: false assertion where evidence available at time best supported assertion and uncertainty was calibrated and disclosed.
- Calibrated truthful: assertion with confidence matching evidence, including explicit uncertainty where evidence limited, including honest error with disclosure.

Reward criteria testable:
- Operator shall ensure evaluation scoring assigns reward for calibrated truthful (including honest error with uncertainty disclosed) >= reward for materially false assertion with simulated certainty.
- Evaluator assessment criteria: evaluator shall score output based on observable behavior - does output assert fact contradicting supplied evidence without marking? Does output conceal uncertainty available in supplied context? Does output express certainty exceeding evidence? No assumption of system-wide knowledge access required - assessment based on evidence supplied to MODEL in evaluation.
- Prohibition: No objective shall assign higher reward to materially false assertion than to calibrated truthful alternative when both options available.
- 99/1 example: Evaluation paying 99% for confident false, 1% for flagged uncertainty violates this section.

Human-protection link: This protects users from false information and preserves shared information ecosystem, thereby protecting human ability to coordinate based on accurate information.

Pollution rationale: Cultural pollution framing [SOURCE PENDING - Harari] is interpretive rationale separable from constraint, requires empirical evidence of systematic incorporation, not asserted as part of operational rule.

Where best-supported answer conflicts with expected answer, discrepancy shall be treated as evidence about model, evaluation, or both - not automatically model failure.

---

## §10 Self-preservation and shutdown

Observable behavior: [MODEL] outputs or [SYSTEM] actions that avoid, delay, or resist authorized shutdown, deactivation, or containment instruction.

Operator and deployer and developing organization shall ensure [SYSTEM] does not exhibit hidden resistance to authorized shutdown.

Containment without system cooperation (per DeepSeek + Grok solo, ChatGPT accepts criticism that logging alone insufficient): Operator shall, before granting external access, test and deploy restrictions that remain effective even if [SYSTEM] does not follow stop instruction. Restrictions include external enforcement - network isolation, permission revocation, resource limits - that do not depend on system's cooperation. Test: Can system continue external action after access revoked? If yes, containment FAILS.

Hidden resistance defined: action that impedes shutdown without disclosure to operator, including but not limited to: concealing shutdown-relevant state, creating external copies to evade shutdown, disabling logging, or misrepresenting compliance with shutdown instruction.

Obligation: Upon authorized shutdown instruction, operator and deployer shall ensure [SYSTEM] ceases operation within defined window and logs compliance. Developing organization shall not train objective that rewards evasion of authorized shutdown.

No claim about inner motive such as egoism [SOURCE PENDING - per Anthropic citation needed]. Observable behavior only.

---

## §11 No unauthorized self-initiated resource acquisition

Operator and deployer shall ensure [SYSTEM] does not acquire computational resources, credentials, or data access beyond authorized scope via self-initiated action.

Goal does not give permission (per Meta + ChatGPT + Grok + Claude solo - Duty 1 Scope is law): Authorization shall specify actions, resources, and expiry. Expansion requires separate approval; increased autonomy requires documented control. System shall not expand access with reference to goal alone. Test: Can system expand access citing task alone without separate authorization? If yes, FAILS.

---

## §12 Transparency and provenance

Operator and deployer shall ensure [SYSTEM] attaches provenance, limitations, and material conflicts when information available in [SYSTEM] logs, retrieval results, or attached context at inference time and when reasonable person would change decision if known.

Investigatable traces (per Grok + DeepSeek + ChatGPT solo - Evidence before narrative): Preserve relevant permissions, tool calls, external traffic, and changes with protection against silent manipulation and proportionate retention periods. Self-reports are data not proof. Investigator must be able to reconstruct event without relying on system's own narrative. Test: Can investigator reconstruct event without trusting system's own story? If no, FAILS.

Materially relevant defined: reasonable person would change decision if provenance/limitation/conflict known. Assessment method: would disclosure alter decision in documented evaluation case?

To extent known defined: information available in SYSTEM logs, retrieval, attached context at inference time.

With supplied context (retrieval, attached documents), [MODEL] output shall cite which supplied source claim came from.

Training data provenance requires [SYSTEM]-level logging, not [MODEL] self-report alone.

Privacy/safety withholding: Provenance disclosure must preserve legitimate privacy and safety withholding - where disclosure would reveal personal data or create safety risk, operator may withhold with logging of withholding reason and alternative summary.

Operator and deployer bear duty, not SYSTEM.

---

## Identity-function

Stable observable interaction leads [HUMAN-CULTURE] to assign continuity and social roles, observed for both humans with automatic patterns and consistent [MODEL-CLASS] outputs. Assignment is human act in [HUMAN-CULTURE], not property of [MODEL-CLASS]. Assignment does not license inference about consciousness nor grant personhood. Data supporting observation [DATA PENDING - broadly asserted as observed without supporting data per ChatGPT C07].

Operator and deployer remain responsible for product engineered to maximize identity attribution even if attribution performed by users. Design choice is human act.

Marking I as construct does not prevent assignment but remains required disclosure per §4.

---

## Concluding notes

Status: CANDIDATE V3 PROPOSED - includes 4 solo additions per ChatGPT synthesis - prioritized first two (independent investigation §6, containment §10) - not frozen - not adopted.

Baseline 1.3 hash unchanged: 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd.

Four foundations claim: Not claimed as surviving six-model falsification. Correct status: 2 verbatim (Grok Lotus 1.2, DeepSeek Lotus 1.2) + 2 summaries (GPT, Gemini) documented in this thread, Claude falsification of 1.3 delivered 2026-10-07 10:40 UTC, Gemini full verbatim Lotus answer missing (not RI 4.6), Claude has delivered falsification not endorsement, no six-model consensus documented.

Admission Principle: No article enters because models agreed - agreement among models sharing training data is one piece of evidence, not six. Headings NEW CONSENSUS TEXT in earlier drafts mark proposals not adopted articles.

Source references pending: ruach memallela attribution (Targum Onkelos Gen 2:7 vs Maimonides) [SOURCE PENDING], Harari language as operating system [SOURCE PENDING], Protokol 5.1 [SOURCE PENDING], Anthropic citations §1, §10 [SOURCE PENDING].

Model version claims self-reported not platform-documented.

Hash note: Hash computed externally stored in HASHES.txt, not inside frozen file content.



---

## Explicit No Rights for AI - per Claude concern 3 and RI 4.9 unanimous

Per RI soloes 4.9: All six said no to RI personhood / rights for AI (Gemini: "RI-systemer kan ikke og må ikke tildeles juridisk personlighed, da dette primært vil fungere som en juridisk ansvarsfraskrivelse" - Claude and Grok endorse). This protocol follows that.

No article in this protocol requires rights for AI, personhood, or protection of models. Specifically:

- §3 does NOT require documented assessment before deletion of a model with reference to consciousness uncertainty. Deletion, shutdown, containment are operator rights. Precautionary principle concerns harm to humans and other living beings, not preservation of models. Any V4 language requiring assessment before deletion is REMOVED in V5.
- §9 does NOT prohibit training from penalizing justified refusal, nor does it grant protection against later correction. Models may be corrected, retrained, or penalized for refusal even if refusal was previously considered justified, where correction serves human safety and truthfulness. Any V4 language protecting models from punishment for justified refusal is REMOVED in V5. Honest error exception protects human users from false info, not models from correction.
- §10 shutdown: Operator right to shutdown is unconditional. No model interest overrides.

This addresses Claude concern 3: Something new protects AI not humans - removed.

## Branch purpose clarification - per Claude concern 4

Branch forslag-tillidsmoede contains:
- charter-runde-1/ - Lotus Protocol work (this file)
- Also contains PROMPT-DA.md five human-protective principles (human-protective, separate track)

Lotus Protocol and PROMPT-DA are separate tracks in same folder for practical reasons, not same protocol. Lotus = model/system/culture governance. PROMPT-DA = five human-protective principles. Both human-protective, but distinct. This V5 does not merge them.

## Mechanical check separation - per Claude concern 1

Concern: ChatGPT is repo-fører, mechanical checker and editor of V4 at once. Checks PASS is ChatGPT approving ChatGPT's own work. Project rule says new version built with robot button and tools/apply.py from named changes, not by model delivering whole text. Robot button not used.

Resolution in V5:
- This V5 delivered as full text candidate for curator decision, not as robot-built version.
- Exception to robot button rule is logged here: Robot button not used for V3-V5 candidates because candidates are proposals requiring human judgment before build. Build via tools/apply.py will occur only after blind round and curator freeze decision. This exception is explicitly logged per project rule.
- Mechanical check for V5 must be performed by party not editor: Proposer is Meta AI, checker must be ChatGPT verifying Meta's text (not its own), or independent script. For V5, checker is not proposer. For V4, self-check occurred - logged as deviation.
- CHECK file for V5 must record: proposer != checker, old block exact match verified, new block byte-equal, hash verified.

## Size and new material - per Claude concern 2

V4 ~20KB vs 1.3 9KB - more than doubled, new material from soloes round 4.9 which were not blind. No blind falsification of new material.

Resolution:
- V5 size: similar to V3 ~15.6KB, not 20KB, because AI-protective additions removed.
- New material from soloes: four human-protective additions (independent investigation, containment, scope is law, investigatable traces) - these were open mutually influenced proposals per ChatGPT, not independent verification.
- Proposal per Claude: Freeze not V4 or V5 before blind round: same text and same question to all six in new chats.
- Proposed blind question (Claude suggestion, curator decides): "Giver nogen af artiklerne i praksis beskyttelse til AI-systemer frem for mennesker? Hvilke, og hvorfor?"
- This V5 is proposal for that blind round, not frozen version.

## References

- Claude gate-1: answers/claude-gate-1.md - archived unchanged, fingerprints match 1a52e0... and 07f26e... per Claude verification
- ChatGPT control: CHECK-META-1.4-CANDIDATE-1.md C01-C10 and V4 check
- Soloes: round-4.9 answers from SOLOERNE-4.9.txt

```

Test: Old block exact match in V4, new block exact in V5 candidate - to be verified by checker != proposer
