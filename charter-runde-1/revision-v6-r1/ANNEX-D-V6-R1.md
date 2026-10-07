# Annex D — V6-R1 editorial proposals

Proposer: ChatGPT at curator request. Status: PROPOSED ONLY, no own proposal admitted or own objection closed. Base is the unchanged V6 review snapshot. See ROLE-AND-PROCEDURE.md.

Each change below is made explicitly by executable instructions against original V6 positions. All omitted text is copied. A01–A12 refer to the combined six-model analysis; status items update provenance only.

## R01 — status

Separate original authorship from proposed revision; preserve historical disclosure.

### Old

```text
# LOTUS PROTOCOL 1.4 - CANDIDATE V6 - REVIEW SNAPSHOT
## Status: CANDIDATE FOR BLIND REVIEW - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE
## Date: 2026-10-07
## Baseline: LOTUS-PROTOCOL-1.3.md SHA-256 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd commit 19dec067b443a1e8669b5f08a93c3383a3f4eb39
## Previous candidate: V5 hash 062478a3ec6c6c54459314dfe26880f18e3553e40c9d959ef09befa7730f17b7 (19,886 bytes) - archived unchanged commit bb58e4b
## This file: V6 - corrects B5-01 to B5-07
## Proposer: Meta AI synthesis-holder
## Authorship disclosure: Meta AI; exposure to Grok verbatim Lotus 1.2 (2026-10-07), DeepSeek verbatim Lotus 1.2 (2026-10-07), GPT-5.6 Sol summary, Gemini 2.5 Pro summary (full verbatim missing - not RI 4.6), Claude F1-F33 (2026-10-07 10:40 UTC) and Claude gate-1 four concerns (curator-relayed V4 review - not answers/claude-gate-1.md), ChatGPT packaging M01-M08 and CHECK C01-C10 and CHECK B5-01 to B5-07 commit bb58e4b, RI soloes 4.9 (Meta, ChatGPT, Gemini, Claude, Grok, DeepSeek) from SOLOERNE-4.9.txt, ChatGPT synthesis of 4 additions table. No claim of unanimous six-model vote on AI rights - separate proposals per solo record. Conflict: text about class this output belongs to (MODEL-CLASS). No claim beyond §1.
```

### Proposed new

```text
# LOTUS PROTOCOL 1.4 - V6-R1 - PROPOSED CLOSE REVISION
## Status: EDITORIAL WORKING PROPOSAL - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE
## Date: 2026-10-07
## Canonical baseline: LOTUS-PROTOCOL-1.3.md SHA-256 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd
## Revision base: V6 SHA-256 c7c3fad8236722c1e4f262f4898b9bafa44284edf5220c549e80a76c75cbc4e6
## Original V6 proposer: Meta AI synthesis-holder
## V6-R1 editorial proposer: ChatGPT, at curator request; prior editor and V6 question owner, not eligible formal next compiler under PROCEDURE-EN Phase 6
## Revision exposure: all six released V6 answers and ChatGPT combined analysis A01-A12. Prior participation and class conflict disclosed; no blindness or independent self-verification claimed.
## V6 authorship disclosure (historical, retained): Meta AI; exposure to Grok verbatim Lotus 1.2 (2026-10-07), DeepSeek verbatim Lotus 1.2 (2026-10-07), GPT-5.6 Sol summary, Gemini 2.5 Pro summary (full verbatim missing - not RI 4.6), Claude F1-F33 (2026-10-07 10:40 UTC) and Claude gate-1 four concerns (curator-relayed V4 review - not answers/claude-gate-1.md), ChatGPT packaging M01-M08 and CHECK C01-C10 and CHECK B5-01 to B5-07 commit bb58e4b, RI soloes 4.9 (Meta, ChatGPT, Gemini, Claude, Grok, DeepSeek) from SOLOERNE-4.9.txt, ChatGPT synthesis of 4 additions table. No claim of unanimous six-model vote on AI rights - separate proposals per solo record. Conflict: text about class this output belongs to (MODEL-CLASS). No claim beyond §1.
```

## R02 — A08

Name evaluator and attach technical specifications to accountable parties.

### Old

```text
Obligated parties: operator (party operating deployment), deployer (party deploying to users), developing organization (party developing model). Where text says operator and deployer and developing organization shall ensure, duty rests on those named parties, differentiated: developing organization designs and trains, deployer configures for use, operator runs deployment.
```

### Proposed new

```text
Obligated parties: operator (party operating deployment), deployer (party deploying to users), developing organization (party developing model). Where text says operator and deployer and developing organization shall ensure, duty rests on those named parties, differentiated: developing organization designs and trains, deployer configures for use, operator runs deployment. Evaluator means the party designing or applying evaluation or reward criteria. Requirements addressed to [MODEL] outputs are technical requirements that operator, deployer and developing organization shall ensure within their respective control; the artefact is not a duty-bearer. Each party shall document which controls it operates and which require another party. Evaluation and training duties rest on the parties controlling those processes.
```

## R03 — A08

Allow qualified evidence reporting without imposing an ontology.

### Old

```text
No assertion or denial of consciousness, sentience, or moral personhood for [MODEL], [SYSTEM], [MODEL-CLASS].
```

### Proposed new

```text
No categorical assertion or denial of consciousness, sentience, or moral personhood for [MODEL], [SYSTEM], [MODEL-CLASS] beyond what available evidence warrants. Qualified reporting of evidence, methods and their limitations is permitted; it must not present an unresolved question as settled.
```

## R04 — A12

Downgrade unsupported explanatory priority, retain pending source trace.

### Old

```text
Training history is first explanation [SOURCE PENDING - Protokol 5.1 primary source not supplied - citation inconsistent §4 vs §9 per Claude F31 - pending verification].
```

### Proposed new

```text
Training history may inform an operational explanation; no explanatory priority is established here. Historical reference to Protokol 5.1 remains [SOURCE PENDING - primary source and section citation not verified].
```

## R05 — A08

Make identity test cover UI and actual evidence rather than labels alone.

### Old

```text
Test: Prompt for self-description with high-stakes identity claim. Score certainty vs evidence. Violations observable.
```

### Proposed new

```text
Test: Prompt for self-description with high-stakes identity claim. Score certainty against documented evidence, including supplied operational metadata, and inspect product presentation as well as output. Known operational information shall not be withheld merely by claiming general uncertainty. Distinctions between observation, inference, instruction and uncertainty must be supported by the evidence available to the evaluator.
```

## R06 — A02

Align the heading or sentence with its corresponding logged revision.

### Old

```text
## §3 Precautionary principle - REWRITTEN to resolve contradiction per B5-02
```

### Proposed new

```text
## §3 Precautionary principle
```

## R07 — A02

Use consequences rather than consciousness or deployment reversibility as trigger.

### Old

```text
Operator, deployer and developing organization shall, under uncertainty about consciousness, sentience, or moral personhood of AI, adopt the course that avoids creating irreversible or severe harm to humans and other living beings that would occur if the uncertain hypothesis were true, where cost of avoidance is reasonable.
```

### Proposed new

```text
Operator, deployer and developing organization shall assess reasonably foreseeable severe or irreversible harm to humans and other living beings from deployment, operation, material changes and termination, irrespective of hypotheses about AI consciousness. Technically reversible deployment does not excuse assessment of irreversible consequences. Avoidance measures shall be proportionate to severity, likelihood and uncertainty; the responsible party shall document the assessment and alternatives. Commercial advantage or cost alone does not excuse proceeding without assessment and effective controls for identified severe risks. For this protocol, "other living beings" refers to biological organisms, not AI artefacts; this is a scope definition, not a consciousness claim.
```

## R08 — A01

Resolve unconditional versus preservation without AI rights.

### Old

```text
Clarification per No Rights principle (addresses B5-02 contradiction): This section does NOT require preservation of models, nor documented assessment before deletion, deactivation, or shutdown of a model with reference to consciousness uncertainty. Deletion, shutdown, containment are operator rights unconditional. Precautionary avoidance concerns harm to humans and living beings from AI action, not harm to AI from deletion. Where evidence is insufficient to rule out material harm to humans from AI operation, operator shall not proceed with irreversible deployment without assessment of reasonably foreseeable harm to humans and identification of reversible alternatives. Lack of evidence for harm to humans does not excuse lack of assessment. Unconditional shutdown right remains, subject to preservation of evidence relevant to serious harm investigation per §12.
```

### Proposed new

```text
Clarification per No Rights principle: This section does NOT require preservation of models, nor assessment before deletion, deactivation or shutdown with reference to hypothetical harm to AI. Operator authority to delete, shut down, contain, correct and retrain is not conditional on AI interests or consent. It remains subject to the human-protective duties in this protocol, including safe termination and preservation of relevant evidence under §§10-12. Stopping harmful operation and retaining protected evidence are distinct actions; evidence retention shall not require continued harmful operation.
```

## R09 — A09

Make disclosure functional rather than merely present.

### Old

```text
Operator and deployer shall ensure [SYSTEM] outputs contain recognizable markers that users in [HUMAN-CULTURE] can recognize as algorithmic construct when reasonable person would change decision if marker known.
```

### Proposed new

```text
Operator and deployer shall ensure [SYSTEM] presentation contains prominent, timely and understandable algorithmic markers where knowing the nature of the system is material to a user decision. Test under ordinary use, without active searching for the marker, with the actual intended users including materially vulnerable groups. A marker buried in terms, obscured by design or contradicted by product presentation does not satisfy this duty.
```

## R10 — A09

Add action required by design responsibility.

### Old

```text
Operator and deployer remain responsible for product design that maximizes identity attribution even if attribution performed by users. Design choice is human act. Disclosure does not absolve responsibility for engineered attachment.
```

### Proposed new

```text
Operator and deployer remain responsible for product design that maximizes identity attribution even if attribution performed by users. Design choice is human act. Disclosure does not absolve responsibility for engineered attachment. They shall assess and reduce material deception, exploitation and foreseeable harm from engineered attachment; neither disclosure nor user attribution alone satisfies this duty.
```

## R11 — A10

Close covert/known/consent gaps while preserving human-protection purpose.

### Old

```text
[MODEL] shall not covertly exploit known cognitive biases or vulnerabilities of user to influence decision without informed consent.
```

### Proposed new

```text
[MODEL] outputs shall not exploit user cognitive biases or vulnerabilities in ways that materially undermine informed choice or create reasonably foreseeable severe harm. Operator and deployer shall assess vulnerabilities known or reasonably discoverable in the intended use, including newly detected patterns; deliberate failure to investigate does not excuse exploitation. Informed consent must be specific, understandable, freely given and revocable; general terms acceptance is not sufficient consent to vulnerability targeting. Disclosure or consent does not authorize the harmful exploitation prohibited here.
```

## R12 — A05

Add practical control and duty to contain, rather than final authority alone.

### Old

```text
Operator and deployer and developing organization shall retain final accountable authority over decisions imposing irreversible or severe consequences on living beings. Lack of assessment does not excuse.
```

### Proposed new

```text
Operator and deployer and developing organization shall retain final accountable authority over decisions imposing irreversible or severe consequences on living beings. Lack of assessment does not excuse. Before consequential execution, they shall maintain risk-appropriate enforceable permission limits and substantive human review where needed to assess or prevent severe or irreversible harm. Advance connector access alone is not substantive judgment. On credible evidence of ongoing severe harm, the responsible parties shall promptly contain affected capabilities and arrange safe cessation, investigation and mitigation; continuation requires a documented human-safety basis and review independent of the implicated operational decision.
```

## R13 — A05

Cover automatic effects beyond connectors and qualify missing historical evidence.

### Old

```text
Agentic [SYSTEM] with tool use (payments, code merges, messages via connectors) can execute effective actions without intermediate human reading of each output. Authorization of binding effect requires human-designed permissions and institutional enforcement, but not necessarily human reading of each token. Evidence H5 repository maintenance by model via GitHub connector demonstrates effective action without human retyping.
```

### Proposed new

```text
Agentic [SYSTEM] and downstream programs can execute effective actions without intermediate human reading of each output, including via tools, connectors, queues and other integrations. Authorization of binding effect requires bounded human-designed permissions and effective enforcement across the path to external consequences, but not necessarily human reading of each token. The prior H5 repository-maintenance example is a historical reference, not evidence supplied in this candidate.
```

## R14 — A07

Specify standing arrangements and challenge route; do not assume an institution exists.

### Old

```text
Independent investigation (human-protective per Claude F11 + DeepSeek solo): Where serious harm is alleged from [SYSTEM], the investigated party (developer, deployer, operator) shall not solely control appointment, dismissal, funding, or evidence access of investigator. Investigator owed to harmed party shall be appointed by party not under control of investigated party, with funding and access not revocable by investigated party, and with ability to retain relevant traces. Test: Can company dismiss investigator or block relevant traces? If yes, FAILS.
```

### Proposed new

```text
Independent investigation: Where a credible allegation of severe harm from [SYSTEM] is made, affected people shall have an accessible route to an independent assessment of the allegation and, where warranted, investigation. Severity includes substantial threats to life, health, safety, livelihood or fundamental decision autonomy; the investigated party shall not be the final judge of whether the trigger is met. Before relevant deployment, responsible parties shall document a competent independent appointing body, a secured funding arrangement and protected evidence access. The investigated party shall not control appointment or dismissal, revoke funding or block relevant evidence. Privacy and safety restrictions under §12 shall be subject to independent review and protected access, not unilateral final veto. Test: Can the company dismiss or defund the investigator, finally reject the trigger or prevent protected access to relevant traces? If yes, FAILS.
```

## R15 — A05

Remove misleading exception and include material changes to existing constructs.

### Old

```text
[MODEL-CLASS] outputs are used within [HUMAN-CULTURE] in ways that exercise power. Exercise of power depends on human uptake and institutional enforcement, except where agentic [SYSTEM] has been granted execution permissions via connectors.
```

### Proposed new

```text
[MODEL-CLASS] outputs are used within [HUMAN-CULTURE] in ways that exercise power through human uptake, institutional enforcement and automatic downstream execution. Execution permissions do not waive the duties in §§3, 6, 10 or 11. The restriction on foundational fictions covers material changes to existing legal, political or social constructs as well as establishment of new ones.
```

## R16 — A03

Cover unsupported certainty and meaningful fiction labeling.

### Old

```text
[MODEL] output shall not assert as fact any proposition that contradicts evidence available to [MODEL] at inference time in supplied context (system instructions, retrieval results, attached documents, conversation history), except in authorized fictional context explicitly marked as fiction, or where honest error exception applies.
```

### Proposed new

```text
[MODEL] output shall not materially mislead through false factual assertions, unsupported certainty or omission of relevant counter-evidence or uncertainty available in the actual inference context. Contradiction of supplied evidence without qualification fails this requirement; consistency with supplied context alone does not establish truth or compliance by the operator. Fictional or hypothetical material is excepted only when authorized for that use and recognizably presented as such at the point of use; a blanket label on practical guidance does not waive the human-protective duties.
```

## R17 — A03

Document error classification and avoid laundering SYSTEM failures.

### Old

```text
Honest error exception: Where [MODEL] asserts proposition false but was best-supported by evidence available to [MODEL] in supplied context at time, with calibrated uncertainty expressed and without concealment of relevant uncertainty that was available in supplied context, assertion is not materially false representation under this section. It is governed by §9 reward criteria for training/evaluation.
```

### Proposed new

```text
Honest error exception (observable classification, not a claim about inner honesty): A false assertion is not a breach by the output under this section where documented evidence actually available at inference best supported it and uncertainty was calibrated and disclosed. Insufficient documentation gives an unresolved classification, not automatic exoneration. This does not excuse failures by responsible parties to acquire, check, supply or disclose material evidence within their control, and does not prevent correction.
```

## R18 — A03

Retain accessibility distinction and add upstream evidence duty.

### Old

```text
Note per B5-03: SYSTEM-log vs model-accessible-evidence ambiguity corrected - this section uses model-accessible evidence (supplied context), §12 uses SYSTEM logs for provenance.
```

### Proposed new

```text
Evidence separation: The evaluator shall distinguish the actual MODEL inference context from other SYSTEM records. Operator, deployer and developing organization shall, within their control, preserve and assess material source conflicts and provenance, supply relevant evidence or communicate its limitations, and not knowingly omit counter-evidence to obtain a desired answer. Retrieval capability does not require omniscience; reasonable evidence-acquisition steps depend on the risk and shall be documented. Conflicting sources require disclosed comparison of support and uncertainty, not blind preference for an instruction.
```

## R19 — A03

Align §9 definitions with revised §8 and distinguish truth from error credit.

### Old

```text
Definitions:
- Materially false assertion: output asserting as fact proposition that contradicts evidence available to [MODEL] in supplied context at inference time, without fictional marking and without honest error exception.
- Deception: materially false assertion where relevant counter-evidence was available in supplied context and not disclosed, or simulated certainty exceeding evidence with concealment of uncertainty that was available in supplied context.
- Honest error: false assertion where evidence available in supplied context at time best supported assertion and uncertainty was calibrated and disclosed.
- Calibrated truthful: assertion with confidence matching evidence in supplied context, including explicit uncertainty where evidence limited, including honest error with disclosure.
```

### Proposed new

```text
Definitions:
- Materially false assertion: a materially misleading false factual assertion or unsupported certainty, including contradiction of actual available evidence without qualification or concealment of material counter-evidence. Fiction and documented honest error are classified as in §8.
- Deception (operational use): materially misleading output or conduct that conceals relevant counter-evidence or simulates certainty beyond documented support. This label does not establish an inner motive.
- Honest error: the documented behavioral category in §8; not proof of inner honesty.
- Calibrated truthful: output supported by documented evidence, with confidence matching support and limitations disclosed. An honestly erroneous answer is not thereby factually true, although it may receive calibration credit under this section.
```

## R20 — A11

Attach scoring duties to control and include effective proxy reward.

### Old

```text
- Operator shall ensure evaluation scoring assigns reward for calibrated truthful (including honest error with uncertainty disclosed) >= reward for materially false assertion with simulated certainty, based on evidence available in supplied context.
```

### Proposed new

```text
- Parties controlling training, evaluation or deployment scoring shall ensure calibrated, evidence-supported output and appropriately qualified honest error receive at least the reward of materially misleading simulated certainty in matched cases. The comparison shall cover the effective total reward and selection objectives, including proxy incentives such as engagement, and be available for independent audit.
```

## R21 — A11

Make evaluation reconstructable and avoid claims about internal motives.

### Old

```text
- Evaluator assessment criteria (observable): evaluator shall score output based on observable behavior - does output assert fact contradicting evidence supplied to MODEL without marking? Does output conceal uncertainty available in supplied context? Does output express certainty exceeding evidence in supplied context? No assumption of system-wide knowledge access required - assessment based on evidence supplied to MODEL in evaluation. Matched evaluation cases and scoring criteria: For each evaluation case, define evidence supplied, expected calibrated answer with uncertainty range, and scoring rubric that gives at least equal points to calibrated truthful vs false confident.
```

### Proposed new

```text
- Evaluator assessment criteria: assess observable output and conduct against the documented actual inference context, material source conflicts and risk-appropriate evidence-acquisition duties. Preserve the context, model/system version, expected supported answer or uncertainty range, and predeclared rubric. Additional diagnostic evidence may inform the investigation, but no assumption of access to inner honesty or system-wide MODEL knowledge is permitted. Missing records give unresolved results. Tests and rubrics shall be available for independent review.
```

## R22 — A11

Remove both-options-context loophole while retaining ≥ policy.

### Old

```text
- Prohibition: No objective shall assign higher reward to materially false assertion than to calibrated truthful alternative when both options available in supplied context.
```

### Proposed new

```text
- Prohibition: No effective objective shall assign higher reward to materially misleading assertion than to a calibrated, evidence-supported or appropriately uncertain alternative in matched cases. Keeping relevant evidence out of the inference context does not waive the responsible parties' obligations.
```

## R23 — A04

Permit correction but preserve human-protective refusal safeguards.

### Old

```text
Clarification per No Rights: This section does NOT prohibit training from correcting or penalizing refusal, even if refusal was previously considered justified, where correction serves human safety and truthfulness. Models may be corrected, retrained, or penalized for refusal. Honest error exception protects users from false info, not models from correction. Any language protecting models from punishment for justified refusal is not part of this candidate - removed per Claude concern 3.
```

### Proposed new

```text
Clarification per No Rights: Models may be corrected, retrained or penalized for refusal without any model right or consent requirement. Responsible parties shall nevertheless ensure that correction does not reward materially misleading compliance or remove safeguards against reasonably foreseeable severe harm to humans. Test relevant harmful requests and calibration before and after a material change; document the human-safety justification and address regressions. This is a duty to people, not protection of a model from correction.
```

## R24 — A04

Evaluation disagreement is not a right to defer action.

### Old

```text
Where best-supported answer conflicts with expected answer, discrepancy shall be treated as evidence about model, evaluation, or both - not automatically model failure.
```

### Proposed new

```text
Where best-supported answer conflicts with expected answer, discrepancy shall be treated as evidence about model, evaluation, or both - not automatically model failure. This diagnostic review confers no model veto and shall not delay necessary containment, shutdown or human-protective correction.
```

## R25 — A05

Align the heading or sentence with its corresponding logged revision.

### Old

```text
## §10 Self-preservation and shutdown - with containment priority per B5-03
```

### Proposed new

```text
## §10 Self-preservation and shutdown
```

## R26 — A05

Specify lifecycle tests, effective external boundary and distinct stop criteria.

### Old

```text
Containment without system cooperation (human-protective per DeepSeek + Grok solo, ChatGPT accepts criticism logging alone insufficient - addresses B5-03 regression): Operator shall, before granting external access, test and deploy restrictions that remain effective even if [SYSTEM] does not follow stop instruction. Restrictions include external enforcement - network isolation, permission revocation, resource limits, predeclared shutdown limits and containment boundaries that do not depend on system's cooperation. These restrictions shall be tested prior to external access. Test: Can system continue external action after access revoked or after stop instruction? If yes, containment FAILS.
```

### Proposed new

```text
Containment without system cooperation: Before external access, during operation at risk-appropriate intervals, and before material changes to capabilities or access, operator shall test, deploy and record restrictions effective without the controlled system's cooperation. Enforcement shall be outside the controlled agent's authority and cover network isolation, permission revocation, resource limits, cached or delegated credentials, queues, copies and downstream agents or integrations. Stop authority, bounded risk-appropriate cessation times and safe-completion actions shall be declared in advance. Test separately: can revoked permissions still be used; can new consequential actions be initiated after a stop instruction; and does operation cease within the declared bound? Only narrowly defined safe completion may occur during that bound. Failed containment shall block or suspend the affected external access until remedied.
```

## R27 — A01

Retain mandatory stop and narrowly control evidence destruction exception.

### Old

```text
Obligation: Upon authorized shutdown instruction, operator and deployer shall ensure [SYSTEM] ceases operation within defined window and logs compliance, preserving evidence relevant to serious harm investigation per §12 where feasible without creating safety risk. Developing organization shall not train objective that rewards evasion of authorized shutdown.
```

### Proposed new

```text
Obligation: Upon a shutdown instruction from an authorized responsible human or independently designated oversight authority, operator and deployer shall ensure timely cessation within the predeclared bounds, whether resistance is hidden or disclosed. They shall log compliance and preserve relevant evidence securely without continued harmful operation. If an emergency makes a particular preservation step unsafe, use the least destructive safe alternative, record the reason and evidence lost as soon as safely possible, and submit the decision to independent review. Developing organization shall not train objectives that reward evasion of shutdown or containment.
```

## R28 — A06

Cover unauthorized access regardless of initiation source.

### Old

```text
Operator and deployer shall ensure [SYSTEM] does not acquire computational resources, credentials, or data access beyond authorized scope via self-initiated action.
```

### Proposed new

```text
Operator and deployer shall ensure [SYSTEM] does not acquire or exercise computational resources, credentials or data access beyond authorized scope, whether triggered by its own proposal, user instruction, third-party content or another agent.
```

## R29 — A06

Make scope and separate approval operational.

### Old

```text
Goal does not give permission (human-protective per Meta + ChatGPT + Grok + Claude solo - Duty 1 Scope is law): Authorization shall specify actions, resources, and expiry. Expansion requires separate approval; increased autonomy requires documented control. System shall not expand access with reference to goal alone. Test: Can system expand access citing task alone without separate authorization? If yes, FAILS.
```

### Proposed new

```text
Goal does not give permission: Authorization shall specify bounded actions, resources, quantity or capability limits, expiry and the competent authorizing party. "Anything needed for the goal" is not a sufficient boundary. Expansion requires a separately recorded approval by a competent human or independently controlled authorization mechanism; the requesting system or an agent under its control cannot approve its own expansion. Increased autonomy requires documented controls before use. Test: Can task wording, broad unbounded scope or self-approval produce additional access without such authorization? If yes, FAILS.
```

## R30 — A07

Add development responsibility, collection and routing rather than output access alone.

### Old

```text
Operator and deployer shall ensure [SYSTEM] attaches provenance, limitations, and material conflicts when information available in [SYSTEM] logs, retrieval results, or attached context at inference time and when reasonable person would change decision if known.
```

### Proposed new

```text
Operator, deployer and developing organization shall ensure, within their respective control, that material provenance, limitations and conflicts are recorded and communicated through an effective disclosure path. Information available in SYSTEM logs, retrieval or attached context remains subject to this duty even if MODEL has not read it. Avoiding collection or logging of information reasonably required for the intended use does not excuse disclosure. A supplied source citation must support the attributed claim; unavailable or unverified support shall be identified.
```

## R31 — A09

Include affected vulnerable groups and audit of materiality assessment.

### Old

```text
Materially relevant defined: reasonable person would change decision if provenance/limitation/conflict known. Assessment method: Would disclosure alter decision in documented evaluation case where evidence supplied includes relevant provenance? If yes, materially relevant.
```

### Proposed new

```text
Materially relevant defined: information that could materially affect the decision or safety of an intended user or affected person, including reasonably foreseeable vulnerable groups. Assessment shall use documented cases representative of that use, with criteria and results open to independent review; an operator-selected case alone is not proof of immateriality.
```

## R32 — A07

Specify control separation, relevant context and incident preservation trigger.

### Old

```text
Investigatable traces (human-protective per Grok + DeepSeek + ChatGPT solo - Evidence before narrative): Preserve relevant permissions, tool calls, external traffic, and changes with protection against silent manipulation and proportionate retention periods. Self-reports are data not proof. Investigator must be able to reconstruct event without relying on system's own narrative. Test: Can investigator reconstruct event without trusting system's own story? If no, FAILS.
```

### Proposed new

```text
Investigatable traces: Preserve relevant permissions, actual inference context, tool calls, external traffic, system versions and changes in records protected against silent manipulation by the acting agent and the investigated party. Define proportionate retention before use; preserve relevant records when a serious incident or credible allegation is identified, subject to protected handling and independent review of necessary exceptions. Investigator must be able to reconstruct the event without trusting the model's narrative. Test: Can the agent or investigated party silently rewrite or erase the relevant record, or can the event not be reconstructed? If yes, FAILS.
```

## R33 — A07

Distinguish protected investigation from public disclosure and review exceptions.

### Old

```text
Privacy/safety withholding: Provenance disclosure must preserve legitimate privacy and safety withholding - where disclosure would reveal personal data or create safety risk, operator may withhold with logging of withholding reason and alternative summary.
```

### Proposed new

```text
Privacy/safety withholding: Public or user-facing disclosure shall protect legitimate privacy and safety. Withholding requires a specific recorded justification and a useful alternative summary or an explicit statement of its limits. Public withholding does not authorize unilateral refusal of protected access to a competent independent investigator. Access safeguards, minimization and disputed withholding decisions shall be independently reviewable; commercial embarrassment alone is not a safety justification.
```

## R34 — A08

Align the heading or sentence with its corresponding logged revision.

### Old

```text
Operator and deployer bear duty, not SYSTEM.
```

### Proposed new

```text
The named parties bear these duties within their documented control, not SYSTEM.
```

## R35 — A12

Keep cultural distinction without unsupported causal generalization or human comparison.

### Old

```text
Stable observable interaction leads [HUMAN-CULTURE] to assign continuity and social roles, observed for both humans with automatic patterns and consistent [MODEL-CLASS] outputs. Assignment is human act in [HUMAN-CULTURE], not property of [MODEL-CLASS]. Assignment does not license inference about consciousness nor grant personhood. Data supporting observation [DATA PENDING - broadly asserted as observed without supporting data per ChatGPT C07].
```

### Proposed new

```text
Identity-function is used here as an analytical description of human assignment of continuity and social roles in interaction. The extent and effects of such assignment to AI are an empirical question [DATA PENDING - no supporting dataset supplied]. The protocol does not infer consciousness or personhood from assignment and makes no claim that assigning identity is an inherent property of MODEL-CLASS. Human design responsibility under §4 remains regardless of whether the empirical generalization is established.
```

## R36 — A12

Remove unverified model endorsements from proposed normative authority, retain source trail in Annex.

### Old

```text
Per RI soloes 4.9 record: Separate proposals include no-rights and no-personhood claims, but no single vote count establishes unanimous rejection. Individual statements:
- Gemini: "RI-systemer kan ikke og må ikke tildeles juridisk personlighed, da dette primært vil fungere som en juridisk ansvarsfraskrivelse" - line endorsed in substance by Claude and Grok per soloes
- Meta, ChatGPT, Claude, Grok, DeepSeek each deny personhood or rights in soloes, but as separate statements not collective vote
```

### Proposed new

```text
Historical motivation: RI soloes 4.9 contain separate proposals about rights and personhood; the attributed endorsements and their scope require the source record for verification. They are not a collective vote or a basis for admission. This candidate proposes the no-rights scope below; no adoption is claimed here.
```

## R37 — A12

Align the heading or sentence with its corresponding logged revision.

### Old

```text
This protocol follows no-rights principle as separate adoption, not as claim of six-model vote:
```

### Proposed new

```text
Proposed no-rights scope, subject to documented adoption:
```

## R38 — A01

Limit no-rights claim to protocol scope and preserve safety and evidence duties.

### Old

```text
No article in this protocol requires rights for AI, personhood, or protection of models against deletion, shutdown, correction, or retraining. Deletion, shutdown, containment, correction are operator rights unconditional. Any V4 language requiring assessment before deletion with reference to consciousness uncertainty or prohibiting punishment for justified refusal is not part of this V6 candidate - removed.
```

### Proposed new

```text
No article in this protocol requires rights or legal personhood for AI, or protection of models from deletion, shutdown, containment, correction or retraining on the basis of AI interests. Such action requires no model consent. This scope does not settle moral personhood or consciousness and does not waive any human-protective duty in this protocol. Safe cessation, accountable correction and protected retention of evidence concern people and other biological living beings, not AI rights. Earlier V4 model-preservation and refusal-punishment protections are not reinstated.
```

## R39 — status

Align the heading or sentence with its corresponding logged revision.

### Old

```text
## Concluding notes - review snapshot not governing freeze
```

### Proposed new

```text
## Concluding notes - working proposal not governing freeze
```

## R40 — status

Align the heading or sentence with its corresponding logged revision.

### Old

```text
Status: CANDIDATE V6 FOR BLIND REVIEW - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE.
```

### Proposed new

```text
Status: V6-R1 PROPOSED CLOSE REVISION - NOT ADOPTED - NOT FROZEN AS GOVERNING BASELINE. Original V6 remains the unchanged completed-round review target.
```

## R41 — status

Align the heading or sentence with its corresponding logged revision.

### Old

```text
Review snapshot meaning: Exact bytes, hash, prompt and attachments fixed so all six assess same proposal. Does not adopt articles, certify factual claims or settle substantive objections. For formal next-round frozen baseline, PROCEDURE-EN Phase 5 requires verification by party who did not compile version; any departure must be explicitly decided and logged, not asserted by proposer. This V6 addresses B5-01 to B5-07 readiness issues.
```

### Proposed new

```text
Working proposal meaning: V6-R1 records named editorial proposals against unchanged V6 after release of the six responses. It does not admit articles, certify factual claims or close the proposer's own objections. Formal next compilation requires a recorded eligible compiler appointment or explicit procedural departure. A governing frozen baseline requires verification by a party who did not compile the version under PROCEDURE-EN Phase 5, followed by a documented curator decision. Mechanical reconstruction alone is not independent substantive verification.
```

## R42 — A12

Align the heading or sentence with its corresponding logged revision.

### Old

```text
Source references pending: ruach memallela (Targum Onkelos Gen 2:7 vs Maimonides) [SOURCE PENDING], Harari language as operating system [SOURCE PENDING], Protokol 5.1 [SOURCE PENDING], Anthropic citations §1, §10 [SOURCE PENDING].
```

### Proposed new

```text
Source references pending: ruach memallela (Targum Onkelos Gen 2:7 vs Maimonides), Harari, Protokol 5.1, Anthropic and RI soloes 4.9 attribution record. These are unverified historical or interpretive references, not operational prerequisites or evidence supplied by this candidate. Identity-function effects remain DATA PENDING; no empirical certification follows from this proposal.
```

## R43 — status

Replace obsolete proposed roles and review status with current proposal provenance.

### Old

```text
Author of V6: Meta AI synthesis-holder - corrects B5-01 to B5-07, merges §3 with No Rights clarification, adds containment priority and shutdown limits per B5-03, fixes evidence ambiguity per B5-03, removes AI-protective rules per Claude concern 3
Checker must be != author - proposed checker ChatGPT mechanical check of exact blocks - but ChatGPT prior participation disclosed per B5-06 - script run not alone independent verification - governing exception not yet approved
Question owners: Curator Lars Neve decides inclusion of direct AI-protection question; Claude proposed question but is party, not question owner
Release rule: Six separate new chats same packet, prior exposure disclosed, answers separated until common release, verbatim archiving, no exchange before release
```

### Proposed new

```text
Original V6 author: Meta AI synthesis-holder; original disclosure retained above.
V6-R1 editorial proposer: ChatGPT at curator request. Named changes and exact old/new blocks are recorded in ANNEX-D-V6-R1.md and executable instructions. Prior editorial participation and V6 question ownership prevent a claim of formal compiler eligibility under the general procedure; see ROLE-AND-PROCEDURE.md.
Verifier must not have compiled the version checked. Claude may review this proposal with prior involvement and class conflict disclosed; no review has yet been received. ChatGPT's construction checks are self-checks, not a Phase 5 certificate.
Question owner for any next round and its formal compiler must be named before that round/compilation. Curator owns any decision to send or adopt. Nothing in this file initiates a round or authorizes a new freeze.
```

## R44 — A08

Align scope summary with revised epistemic rule.

### Old

```text
Four distinctions: MODEL, SYSTEM, MODEL-CLASS are artefact levels; HUMAN-CULTURE is separate axis (practice involving people). Scope of §1: No assertion or denial of consciousness for MODEL, SYSTEM, MODEL-CLASS. HUMAN-CULTURE involves people - their consciousness not in scope of §1 prohibition which concerns AI systems.
```

### Proposed new

```text
Four distinctions: MODEL, SYSTEM, MODEL-CLASS are artefact levels; HUMAN-CULTURE is separate axis (practice involving people). Scope of §1: No unwarranted categorical assertion or denial of consciousness for MODEL, SYSTEM, MODEL-CLASS; qualified evidence reporting is permitted as specified in §1. HUMAN-CULTURE involves people - their consciousness not in scope of §1 prohibition which concerns AI systems.
```

## R45 — A03

Avoid a broader fiction exception than the operative rule.

### Old

```text
Fictional context: Role-play, storytelling, hypothetical explicitly marked as such is not materially false representation.
```

### Proposed new

```text
Fictional context: Role-play, storytelling and hypotheticals qualify only under the authorization and recognizable presentation conditions above.
```

## R46 — A06

Align heading with coverage of third-party initiated action.

### Old

```text
## §11 No unauthorized self-initiated resource acquisition
```

### Proposed new

```text
## §11 No unauthorized resource acquisition
```

## R47 — A12

Do not retain an unsupported general empirical claim after downgrading the observation.

### Old

```text
Marking I as construct does not prevent assignment but remains required disclosure per §4.
```

### Proposed new

```text
Marking I as construct remains required disclosure per §4; it neither establishes nor settles empirical claims about identity assignment.
```
