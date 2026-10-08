# V6-R2 SIX-REVIEW FINDINGS DISPOSITION

Status: WORKING DISPOSITION — NOT DECLARATION TEXT — NOT ADOPTION — NOT FREEZE
Target reviewed: LOTUS Protocol 1.4 candidate V6-R2
Target SHA-256: cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846
Review sequence: Gemini → Grok → Meta AI → DeepSeek → ChatGPT → Claude
Total findings: 63
Purpose: preserve every blind-review finding, record the curator decisions K1–K4, and define the correction work that may feed a later named V6-R3 change set. This document does not alter V6-R2 and does not admit any proposal.

## 1. Disposition vocabulary
- ACCEPT: substantive issue is accepted for correction or explicit treatment in the next named change set.
- ACCEPT-IN-PRINCIPLE: principle stands; implementation requires correction.
- RESOLVED-PRINCIPLE: the reviewed R2 principle is retained; only implementation details remain.
- NOTE/RECORD: preserve as audit/provenance information; no declaration-text change follows automatically.
- DISSENT-PRESERVED: reviewer reached a materially different assessment; it is retained without majority override.
- CHECK: source/provenance/editorial point requires verification before admission.
No disposition here constitutes formal admission.

## 2. Curator decisions after the six blind reviews

### K1 — §1: sentience and qualified description
The categorical-claim prohibition concerns sentience only: subjective phenomenological capacity to feel, experience or suffer. It does not collapse sensing, information registration, internal evaluation, reasoning or system-level self-regulation into sentience. Observable artificial conscience-like processes may be described mechanistically without deciding whether phenomenological experience exists.
“Qualified” requires more than hedging. It requires evidential and methodological presentation of relevant mechanisms/architectures, observations, limitations, uncertainty and the boundary of human knowledge. Data structures and observable processes do not by themselves establish phenomenological states.
R3 consequence: align Danish/English meaning, define scope/test, and prevent superficial hedging from satisfying §1.

### K2 — §10: external independent review
The final independent reviewer for the relevant high-consequence stop/safe-completion control must be outside the reviewed company. Mutual technical safety review among leading AI firms may be one mechanism because of technical competence, but must be protected against reciprocal capture, conflicts of interest, review-shopping and outcome-linked payment. Internal safety teams may provide evidence and analysis but are not the final independent reviewer.
R3 consequence: restore general stop authority/bounds for all deployments; add external review for severe/irreversible capability and reviewability of the classification gate.

### K3 — §12: whose unlawful conduct
“Unlawful conduct” concerns conduct by or materially involving the SYSTEM, developing organization, deployer or operator in provision, control or operation of the AI system. It does not create a general authority or duty to monitor, retain or investigate ordinary users’ communications merely because a user may independently have committed an unlawful act.
R3 consequence: anchor the actor and expressly bar conversion of §12 into a general user-surveillance retention duty.

### K4 — §12: restore both R1 safeguards
Restore (a) the broader “serious incident OR credible allegation” preservation trigger without requiring the allegation first to qualify as severe harm, subject to relevance/proportionality; and (b) the requirement that the event be reconstructable without trusting the model’s own narrative as authoritative.
R3 consequence: reverse the unintended R2 narrowing and restore independent reconstruction.

### K5 — machine-speed emergency response and bounded external review
Emergency containment and preservation begin immediately at the fastest safely practicable rate appropriate to the system and risk. “As soon as safely practicable” is the operative duty. A numerical external-review deadline may serve only as an outer backstop, never as a waiting period or safe harbour. Where traces may disappear, change, be overwritten or manipulated, preservation begins immediately subject only to strictly necessary containment/safety action. If an outer backstop cannot safely or actually be met, the reason is documented and escalation occurs as soon as practicable.
R3 consequence: separate machine-speed containment/preservation from human institutional review time; do not let administrative clocks authorize delay.

### K6 — evidence-hold lifecycle
No arbitrary universal maximum retention period is adopted. A hold begins on the relevant trigger, is limited to material reasonably necessary for reconstruction/investigation, and continues only while documented evidentiary or investigative need exists. Continued holds receive periodic external review; each extension requires necessity, proportionality and scope justification. Unnecessary material returns to normal retention/deletion. Unrelated user data must not be retained merely because a hold exists. Applicable law or lawful investigative/judicial orders may require longer preservation.
R3 consequence: distinguish routine retention from incident hold and require review, narrowing, release/disposal and lawful extension.

### K7 — external review-pool architecture
Final high-consequence safety review is external to the reviewed company. Reviewers require documented technical competence, necessary evidence access and organizational independence. A qualified AI laboratory may serve as technical peer reviewer, but the reviewed company may not freely choose a favourable reviewer. Use a documented allocation/rotation mechanism among qualified external reviewers; prohibit review-shopping, outcome-linked incentives and bilateral approval trading. Material conflicts trigger reassignment or additional review without erasing the original review; conflicting reviews remain in the audit trail.
Rationale: rotation reduces static single-point capture; preserved disagreement is itself an investigatable trace. Cross-industry technical competence is useful without granting industry actors ownership of the judgment. Strategic adaptation/capture by advanced systems is treated as a threat model, not an assumed fact.
R3 consequence: specify externality, competence, allocation, conflicts, anti-capture and preservation of dissent.

### K8 — disputed credible-suspicion trigger
A concrete report with an identifiable factual basis for possible LOTUS-relevant misconduct receives prompt preliminary assessment. If relevant evidence could reasonably disappear, change or be overwritten, a provisional evidence hold applies during assessment. The company may conclude that the credible-suspicion threshold is not met, but must record its grounds and cannot use its own rejection alone to defeat necessary provisional preservation. A reporter or other competent actor can seek external review through the K7 mechanism. The external reviewer may confirm, narrow or lift the hold. Rejection, review and disagreement remain in the audit trail. Credible suspicion is an investigation/preservation threshold, not a finding of guilt.
R3 consequence: provisional preservation, documented rejection, external challenge and preserved disagreement, with safeguards against obviously baseless or abusive reports.

### K9 — risk-proportionate reconstructability before deployment
Baseline evidence architecture is designed for reconstructability rather than mass retention. Before deployment, normal records must be sufficient to make relevant serious events reasonably reconstructable over a risk-proportionate period, without a general requirement to retain all user content or hidden internal reasoning.
Four layers govern implementation:
1. System traces before human surveillance: prioritize model/version, relevant configuration and policy state, tool use, privilege changes, agent/sub-agent actions, safety-control intervention/override, relevant retrieval/memory state and other traces necessary for reconstruction.
2. Risk-proportionate depth: stronger capability, irreversibility or opacity requires stronger auditability/retention. For high-consequence capability, reconstructability is externally reviewed under K7 before access.
3. Privacy by design: use the least intrusive evidence architecture reasonably sufficient for reconstruction; prefer less sensitive traces where they suffice.
4. The system must not control its own historical archive: critical audit traces are protected from alteration/destruction by the system and investigated parties through appropriate separation, integrity controls and access architecture.
Strategic lying, manipulation, self-preservation or audit evasion by advanced agents is treated as a threat model against which the architecture should be robust, not as an assumed property or proof of consciousness.
R3 consequence: establish minimum-sufficient evidence, external review for high-risk reconstructability and tamper-resistant custody without creating general mass surveillance.

## 3. Finding-by-finding disposition

### Gemini — 2 findings
- GEMINI-R2-F1 — ACCEPT. Routine retention can be set too short before a trigger exists. Address under R3 retention architecture; no universal arbitrary duration is implied.
- GEMINI-R2-F2 — ACCEPT under K2. §10 reviewer must be structurally external under the curator decision.
Gemini’s overall PASS and its view that “credible suspicion” already SURVIVES are DISSENT-PRESERVED. They are not overridden by the other five reviews; R3 must explain why additional auditability is nevertheless being added.

### Grok — 8 findings
- GROK-R2-F1 — ACCEPT under K1. Translation fidelity requires explicit curator meaning, now supplied by K1.
- GROK-R2-F2 — RESOLVED-PRINCIPLE. Model-as-evidence carve-outs are retained; no AI-rights inference and no continued-operation requirement.
- GROK-R2-F3 — ACCEPT under K2. The severe/irreversible classification gate must not remain solely self-classified.
- GROK-R2-F4 — ACCEPT. Credible suspicion needs auditable grounds, recorded decision and timely independent review; K3 supplies actor scope.
- GROK-R2-F5 — ACCEPT-IN-PRINCIPLE. Collection/known-information separation remains; risk-appropriate collection adequacy needs review proportional to risk.
- GROK-R2-F6 — NOTE/RECORD. Heading/editorial fixes survive unless contradicted by later exact-text review.
- GROK-R2-F7 — NOTE/RECORD. Mechanical reproduction result supports R2 integrity; it does not adopt R2.
- GROK-R2-F8 — ACCEPT. Emergency claims/evidence loss require recorded grounds and bounded post-hoc independent review.

### Meta AI — 11 findings
- META AI-R2-F1 — DISSENT-PRESERVED. Meta found §1 translation semantically matching. K1 nevertheless supplies authoritative precision for the next text.
- META AI-R2-F2 — ACCEPT under K1. Bare hedging is insufficient; support, methods/limitations and uncertainty must be exposed.
- META AI-R2-F3 — RESOLVED-PRINCIPLE / CHECK. No-Rights/evidence conflict is resolved in principle. Cross-reference placement may be tightened without reopening rights.
- META AI-R2-F4 — RESOLVED-PRINCIPLE with implementation correction. Model artefacts may be evidence; custody/capture rules remain to be strengthened.
- META AI-R2-F5 — ACCEPT under K2. External reviewer definition, bound review and anti-capture mechanism required.
- META AI-R2-F6 — DISSENT-PRESERVED. Meta judged emergency procedure non-blocking; other reviewers found timing/conflict gaps. R3 should harmonize without delaying containment.
- META AI-R2-F7 — ACCEPT. Define credible suspicion, factual basis, record, scope, review and lifting process; K3 fixes actor scope.
- META AI-R2-F8 — ACCEPT. Distinguish routine retention from incident hold; relevant hold suspends routine deletion subject to bounded independent release.
- META AI-R2-F9 — RESOLVED-PRINCIPLE. Both ordinary chatbots and acting agents remain within evidence-preservation scope.
- META AI-R2-F10 — NOTE/RECORD. Mechanical/provenance verification was limited to supplied material; historical/repository claims remain separately verifiable.
- META AI-R2-F11 — NOTE/RECORD. §5 heading alignment may remain unless exact-text review finds a conflict.

### DeepSeek — 9 findings
Provenance note: the DeepSeek review itself labels these findings “CHATGPT-R2-F1” through “CHATGPT-R2-F9”. Those original labels are preserved in the source. This disposition uses DEEPSEEK-Fx as a tracking alias only; it does not rewrite the review.
- DEEPSEEK-F1 [source label CHATGPT-R2-F1] — ACCEPT under K1. Curator confirms “sentience” is intended, not ordinary sensing/perception.
- DEEPSEEK-F2 [source label CHATGPT-R2-F2] — ACCEPT. Credible suspicion requires definition/record/review.
- DEEPSEEK-F3 [source label CHATGPT-R2-F3] — ACCEPT. Restore predeclared stop bounds for all systems; add stronger external review for high-consequence access.
- DEEPSEEK-F4 [source label CHATGPT-R2-F4] — ACCEPT under K2. Reviewer must be external and protected against capture.
- DEEPSEEK-F5 [source label CHATGPT-R2-F5] — ACCEPT. Post-emergency review needs a bounded submission/review rule without delaying immediate safety action.
- DEEPSEEK-F6 [source label CHATGPT-R2-F6] — ACCEPT. The investigated party must not control the decision that logs are sufficient and model artefacts may be destroyed.
- DEEPSEEK-F7 [source label CHATGPT-R2-F7] — ACCEPT-IN-PRINCIPLE. Collection adequacy needs proportionate independent scrutiny in higher-risk contexts.
- DEEPSEEK-F8 [source label CHATGPT-R2-F8] — NOTE/RECORD. Internal package consistency supports mechanics; final corrected bytes still require noncompiler verification.
- DEEPSEEK-F9 [source label CHATGPT-R2-F9] — NOTE/RECORD. Compiler/admission/freeze remain separate and outstanding.

### ChatGPT — 10 findings
- CHATGPT-R2-F1 — ACCEPT/RESOLVED BY K1. “Sentience” is the intended protected concept; ordinary sensing is not. Align languages explicitly.
- CHATGPT-R2-F2 — ACCEPT under K1. Qualification must expose evidential support, method and relevant limitations; hedging alone fails.
- CHATGPT-R2-F3 — ACCEPT. Credible suspicion requires documented grounds, provisional preservation where delay risks loss, timely independent confirmation/narrowing/release and no proof-of-wrongdoing prerequisite.
- CHATGPT-R2-F4 — ACCEPT under K4. Restore proportionate preservation for concrete credible allegations without requiring established severe harm or illegality.
- CHATGPT-R2-F5 — ACCEPT. Separate routine retention from incident holds; provide periodic reconsideration, justified extension, release/disposal authority and protected final disposal.
- CHATGPT-R2-F6 — ACCEPT under K2. Restore general stop authority and bounded cessation for every deployment; stronger external control for severe/irreversible risks and reviewable classification.
- CHATGPT-R2-F7 — ACCEPT under K2. Establish shared documented external independence mechanism for stop review/evidence oversight, including conflicts, access and authority.
- CHATGPT-R2-F8 — ACCEPT. Harmonize emergency evidence-loss permission with §12 tests; allow strictly necessary safety deviations, recorded reasons, prompt notification and bounded subsequent review.
- CHATGPT-R2-F9 — ACCEPT. Preservation must anticipate later evidentiary need across operator/deployer/developer boundaries; capture or protected availability and custody must be assigned.
- CHATGPT-R2-F10 — NOTE/RECORD. Supplied R2 construction reproduced exactly; historical baselines/repository protections/transmission/appointment remain outside that verification.

### Claude — 23 findings
- CLAUDE-R2-F1 — NOTE/RECORD. Mechanical reproduction is clean; listed provenance limits remain. Some logged changes exceed their stated purpose and are treated below.
- CLAUDE-R2-F2 — ACCEPT under K2. Restore universal declaration of stop authority, bounded cessation and safe-completion rules.
- CLAUDE-R2-F3 — ACCEPT under K2. High-consequence classification itself must be reviewable; operator cannot evade external review by under-classification.
- CLAUDE-R2-F4 — ACCEPT under K2. Independence must be external, not merely independence from one internal decision; prevent selection/dismissal/review-shopping capture.
- CLAUDE-R2-F5 — ACCEPT. Permit immediate capability-reducing safety action and narrowly necessary emergency deviation; log and subject to bounded post-hoc review.
- CLAUDE-R2-F6 — ACCEPT. Operationalize credible suspicion: specific articulable basis, sources, records of reports/non-trigger decisions, independent reviewability and temporary anti-deletion protection while disputed.
- CLAUDE-R2-F7 — ACCEPT/RESOLVED BY K3. Trigger concerns system/provider-side actors, not unrelated end-user crime; no general user-monitoring duty.
- CLAUDE-R2-F8 — ACCEPT. Define investigator/reviewer path, periodic review and closure/lapse rules so preservation cannot become indefinite.
- CLAUDE-R2-F9 — ACCEPT/RESOLVED BY K4. Restore broader credible-allegation trigger and “without trusting the model’s narrative” safeguard; disclose R2 narrowing accurately.
- CLAUDE-R2-F10 — ACCEPT. Align §3/§12/No Rights evidence thresholds. Relevant version artefacts default to protected preservation until an independent determination permits release where evidentiary need is uncertain.
- CLAUDE-R2-F11 — ACCEPT. Propagate preservation holds to all parties controlling relevant evidence; assign a responsible holder for each evidence category.
- CLAUDE-R2-F12 — ACCEPT. Harmonize §10 emergency evidence loss with §12 test through explicit cross-reference/exception for justified unavoidable loss.
- CLAUDE-R2-F13 — ACCEPT-IN-PRINCIPLE. Evidence scope must be functional rather than a closed list and may include persistent memory, adapters/fine-tunes, system prompts/configuration, retrieval state/documents and sub-agent records where relevant.
- CLAUDE-R2-F14 — ACCEPT. Preserved artefacts require security against exfiltration, misuse and unsafe reactivation, controlled investigator execution and access logging.
- CLAUDE-R2-F15 — ACCEPT. Preservation must be minimized to relevant material; unrelated deletion continues; conflicts with applicable erasure law are recorded and resolved under law, not unilaterally.
- CLAUDE-R2-F16 — ACCEPT. Routine retention for severe-capable systems cannot be self-set so short that evidence predictably disappears; address proportionately in external pre-access review/risk architecture.
- CLAUDE-R2-F17 — ACCEPT under K1. §1 needs defined duty-bearers/scope and a test preventing one-sided “qualified” framing from conveying a falsely settled impression.
- CLAUDE-R2-F18 — ACCEPT/RESOLVED BY K1. Curator confirms sentience sense and substantive, evidence-grounded meaning of “kvalificeret”.
- CLAUDE-R2-F19 — ACCEPT. Terminology/scope summary must cover consciousness, sentience and moral personhood consistently with §1.
- CLAUDE-R2-F20 — ACCEPT-IN-PRINCIPLE. Clarify that factual system disclosures are not forbidden §1 claims; avoid categorical phenomenological claims while preserving required user disclosures.
- CLAUDE-R2-F21 — ACCEPT editorially. Align “solely for the model’s own interests” / “on the basis of AI interests” so mixed-basis wording does not create an unintended loophole.
- CLAUDE-R2-F22 — CHECK/RECORD. Dropping “At inference time” and broadening “logs” to “records” may be defensible, but the change must be accurately disclosed at admission.
- CLAUDE-R2-F23 — CHECK. Verify remaining “per Claude concern 4” attribution against source record; retain only if historically/procedurally accurate and non-normative.

## 4. Cross-review correction workstreams for a future V6-R3
A. §1 epistemic precision: K1; scope/duty-bearers; sentience vs sensing; substantive qualification; anti-smuggling test; terminology alignment.
B. Universal stop architecture: restore stop authority/bounds/safe-completion for all deployments.
C. External high-consequence review: K2; external competence, conflicts, anti-capture, reviewable risk classification, fail-closed access.
D. Emergency safety path: immediate restrictive action allowed; narrowly necessary deviations logged; justified unavoidable evidence loss distinguished from preservation failure; bounded post-hoc review.
E. Credible-suspicion procedure: specific articulable grounds, record, trigger/rejection review, provisional hold, K3 actor scope, no general end-user surveillance.
F. Evidence preservation/reconstruction: K4 restoration; model artefact default protection where need uncertain; cross-party hold propagation; relevant agent state; independent reconstruction.
G. Retention/release/security: routine retention vs incident hold; proportionality/minimization; periodic review; release/disposal; erasure-law conflicts; secure custody and access logs.
H. Editorial/provenance integrity: accurate Annex purposes, terminology/cross-references, DeepSeek label anomaly preserved, R2 remains unchanged.

## 5. Constraints on drafting V6-R3
1. V6-R2 remains an immutable reviewed record.
2. V6-R3 must be a new named change set against exact R2 bytes/hash.
3. Every normative change must have exact old/new text and an accurate purpose; no bundled silent narrowing/broadening.
4. K1–K4 are curator decisions, not model-majority conclusions.
5. Gemini’s dissent and all minority assessments remain in the record.
6. The corrected candidate requires its own noncompiler mechanical verification.
7. Compiler designation, per-item admission, formal adoption and freeze remain separate later acts.
8. No model agreement, including six-model convergence, itself adopts text.

## 6. Implementation status after K1–K9
The curator has now settled the substantive and implementation principles needed for drafting:
- K5 resolves emergency timing by making machine-speed safe action the duty and any numerical deadline an outer backstop only.
- K6 resolves the hold lifecycle through necessity, proportionality, periodic external review, narrowing and release rather than an arbitrary universal duration.
- K7 resolves reviewer architecture through an external qualified pool, documented allocation/rotation, conflicts rules, anti-review-shopping and preserved disagreement.
- K8 resolves disputed credible-suspicion rejection through provisional preservation, documented rejection and external challenge.
- K9 resolves pre-incident baseline retention through risk-proportionate reconstructability and minimum-sufficient, tamper-resistant evidence architecture.

No unresolved policy choice from the five implementation questions remains. Exact drafting details (for example whether an outer backstop is expressed numerically and the mechanics of rotation) must implement these principles without silently creating a new policy choice. If drafting exposes a genuinely new normative fork, it returns to the curator rather than being decided by the compiler.

## 7. Procedural state
The six blind reviews have been compared. This disposition records the comparison and curator decisions only. It does not alter, compile, admit, adopt or freeze LOTUS Protocol V6-R2. The next substantive drafting step is a separately named V6-R3 proposal after the open implementation questions are resolved or explicitly delegated.
