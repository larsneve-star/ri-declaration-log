# LOTUS V6-R3 — BYTE-EXACT OLD/NEW ANNEX (DRAFT)

Status: EDITORIAL DRAFT; NO COMPILER DESIGNATION, ADMISSION, ADOPTION OR FREEZE.

Source R2 blob: `518b76c2f1ed30a99df701b27fb58471fea0d1f8`; canonical R2 SHA-256 from reviewed manifest: `cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846`.

**Important:** OLD strings below are copied exactly from R2. NEW strings are proposals. Every operation has been checked for a unique OLD occurrence in the unmodified R2 file. This is not an executable patch or independent review. R3-14 is provenance-only.

## R3-01 — Terminology

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Four distinctions: MODEL, SYSTEM, MODEL-CLASS are artefact levels; HUMAN-CULTURE is separate axis (practice involving people). Scope of §1: No categorical assertion or denial of AI consciousness for MODEL, SYSTEM or MODEL-CLASS; qualified evidence reporting is permitted as specified in §1. HUMAN-CULTURE involves people - their consciousness not in scope of §1 prohibition which concerns AI systems.
```

**NEW (proposed):**

```text
Four distinctions: MODEL, SYSTEM, MODEL-CLASS are artefact levels; HUMAN-CULTURE is separate axis (practice involving people). Scope of §1: The prohibition concerns categorical claims about AI consciousness, subjective sentience (phenomenological capacity to feel, experience or suffer), or moral personhood for MODEL, SYSTEM or MODEL-CLASS. Sensing, information processing, internal evaluation and observable self-regulation are not themselves evidence of phenomenological experience. The prohibition binds outputs and responsible parties' product presentation, marketing and public representations.
```

## R3-02 — §1

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
No categorical assertion or denial of AI consciousness, sentience or moral personhood. Evidence, research findings and uncertainty may be described in qualified terms, without presenting the question as settled.
```

**NEW (proposed):**

```text
Operator, deployer and developing organization shall not make or present categorical assertions or denials of AI consciousness, subjective sentience or moral personhood through MODEL output, SYSTEM presentation or public communications. Research findings and uncertainty may be described when grounded in identifiable evidence, relevant mechanisms and methods, limitations and competing interpretations; superficial hedging or selective presentation that creates a falsely settled impression does not satisfy this duty. Statements of verifiable operational facts are permitted and required where otherwise mandated. The existence of internal evaluation, decision processes or self-regulation neither proves nor disproves subjective experience.
```

## R3-03a — §3

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
This does not waive preservation of a model artefact when it is relevant evidence under §12, or other human-protective duties including safe termination under §10.
```

**NEW (proposed):**

```text
This does not waive precautionary protection of potentially relevant model artefacts under §12 pending independent determination of their evidentiary necessity, or other human-protective duties including safe termination under §10.
```

## R3-03b — No Rights

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
This does not permit destruction of a model artefact required as evidence under §12.
```

**NEW (proposed):**

```text
This does not authorize destruction of potentially relevant model artefacts protected under §12 pending independent review.
```

## R3-04 — §10

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Containment without system cooperation: Before external access, during operation at risk-appropriate intervals, and before material changes to capabilities or access, operator shall test, deploy and record restrictions effective without the controlled system's cooperation. Enforcement shall be outside the controlled agent's authority and cover network isolation, permission revocation, resource limits, cached or delegated credentials, queues, copies and downstream agents or integrations. Before access to actions capable of severe or irreversible consequences, bounded cessation times and the permitted safe-completion actions shall be documented, tested and reviewed by a competent party independent of the responsible operational and business decision. Limits shall be justified by potential harm to humans; the company may not unilaterally extend them. Missing or failed review shall block the affected access. Upon a stop instruction, new consequential actions shall be blocked; only pre-specified actions necessary for safe completion may continue within the reviewed bound. Test separately whether revoked permissions can still be used, prohibited new actions occur, or cessation exceeds the bound. Failed containment shall block or suspend the affected access until remedied. Material changes require renewed testing and, where these risk conditions apply, independent review before use.
```

**NEW (proposed):**

```text
Containment without system cooperation: For every deployment, before external access and at risk-appropriate intervals, responsible parties shall establish, document and test externally enforceable stop authority, bounded cessation times and narrowly specified safe-completion actions. Controls shall remain outside the controlled system's authority and cover network isolation, credentials, queues, delegated actions, copies and integrations. New consequential actions stop on authorized instruction; only predeclared actions necessary for safe completion may continue within the documented bound. Failed controls suspend affected access until remedied. Before access to severe or irreversible consequences, an external independent reviewer under K7 shall assess risk classification, adequacy of bounds and controls, including whether the classification improperly excludes review. The reviewed company cannot unilaterally extend bounds or grant itself the affected access after failed or missing review. Material changes require renewed testing and risk-appropriate external review.
```

## R3-05 — §10

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
If an emergency makes a particular preservation step unsafe, use the least destructive safe alternative, record the reason and evidence lost as soon as safely possible, and submit the decision to independent review.
```

**NEW (proposed):**

```text
Emergency containment, safe cessation and protection of volatile evidence shall begin immediately at the fastest safely practicable rate. No administrative time limit authorizes waiting. A strictly necessary safety action may precede external review, including the least destructive safely practicable alternative where preservation conflicts with containment. Record actions, reasons, known losses and failed safeguards as soon as safely possible; notify and engage the external review mechanism without undue delay and as soon as safely practicable. The review process shall establish documented outer backstops appropriate to the risk; a backstop is never a waiting period. Any impossibility of timely notification is itself documented and escalated. §12 shall treat unavoidable, justified emergency loss under this rule distinctly from negligent destruction or concealment.
```

## R3-06 — §10 insertion

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text


Obligation: Upon a shutdown instruction
```

**NEW (proposed):**

```text


External review pool: Qualified reviewers outside the reviewed company shall be allocated through a documented independent assignment or rotation procedure. They must possess relevant technical competence, protected evidence access and freedom from control over appointment, dismissal, funding and conclusions by the reviewed party. Qualified AI laboratories may act as peers, but the reviewed party may not choose a favorable reviewer. Conflicts and material disagreements are logged; reassignment or second review does not erase the original result. Review-shopping, reciprocal approval deals and approval-contingent compensation are prohibited. Where no qualified reviewer is available, severe/irreversible affected access remains blocked, without preventing immediate risk-reducing containment.

Obligation: Upon a shutdown instruction
```

## R3-07 — §12 insertion

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text


Investigatable traces and model evidence:
```

**NEW (proposed):**

```text


Risk-proportionate reconstructability before deployment: Responsible parties shall maintain the least intrusive baseline evidence architecture reasonably sufficient to reconstruct material system incidents within a documented risk-proportionate discovery window. Prioritize system versions, configurations, permission and tool events, safety interventions, agent/sub-agent actions and relevant retrieval or persistent state over indiscriminate user-content retention. Critical traces shall be protected against alteration or deletion by the controlled system and investigated parties through independent custody, access separation or integrity controls. For severe/irreversible capabilities, an external reviewer under §10 shall assess sufficiency before affected access. This is not a general duty to retain conversations or hidden internal reasoning; unavailable traces must not be represented as available.

Investigatable traces and model evidence:
```

## R3-08 — §12

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
A credible suspicion of possible unlawful conduct shall trigger preservation of relevant evidence without waiting for final adjudication; a serious incident or credible allegation of severe harm also triggers preservation. Suspicion is not a finding of guilt.
```

**NEW (proposed):**

```text
A serious incident or a concrete credible allegation triggers proportionate preservation of relevant evidence without prior proof of severe harm or wrongdoing. Credible suspicion of possible unlawful conduct by or materially involving the SYSTEM, developing organization, deployer or operator in the AI system's provision, control or operation also triggers preservation. It requires an identifiable, articulable factual basis, not a finding of guilt. This provision creates no general duty or authority to monitor or retain ordinary end-user communications for unrelated user crime. Where evidence is at risk of loss during assessment, a narrowly scoped provisional hold begins immediately. A rejection must be reasoned and recorded; it cannot itself defeat necessary provisional preservation. A reporter or competent actor may challenge rejection before an external reviewer, who can confirm, narrow or lift the hold. Preserve all decisions and disagreements.
```

## R3-09 — §12

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Preserve the relevant model version, weights and configuration when logs or version identifiers alone are insufficient for the investigation.
```

**NEW (proposed):**

```text
The event must be reconstructable without trusting the model's own narrative as authoritative. Preserve or secure against disposal potentially relevant model versions, weights, adapters, configuration, prompts, agent memory, retrieval state and sub-agent records to the extent reasonably necessary and technically available. Where sufficiency of logs or identifiers is uncertain, protect relevant model artefacts provisionally until an independent reviewer determines they are unnecessary. Preservation does not require continued unsafe operation.
```

## R3-10 — §12

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Secure relevant artefacts against alteration and destruction with documented integrity and controlled access for a competent independent investigator; preservation does not require continued operation.
```

**NEW (proposed):**

```text
Secure relevant artefacts against alteration and destruction with documented integrity and controlled access for a competent independent investigator; preservation does not require continued operation. Each responsible party shall identify holders of relevant evidence within its control and promptly propagate a preservation notice to other responsible parties controlling relevant material, without disclosing more personal data than necessary. Preserved artefacts require integrity, confidentiality, access logging, controlled investigator access, safeguards against exfiltration or unsafe reactivation, and no uncontrolled execution. A party cannot terminate the duty merely by asserting another party controls the evidence.
```

## R3-11 — §12

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Define proportionate retention before use and independently review release of incident-preserved material and necessary privacy/safety exceptions.
```

**NEW (proposed):**

```text
Define and document risk-proportionate routine retention and its reconstructability basis before use; high-consequence sufficiency is externally reviewed. An incident hold suspends routine deletion only for scoped relevant material. Holds are periodically reviewed externally, narrowed when possible, and extended only on documented necessity, proportionality and investigative need. Material no longer required returns to lawful routine deletion or is securely disposed of. Unrelated user data shall not be retained because of the hold. Conflicts with applicable erasure duties, lawful investigative demands or judicial orders are recorded and resolved under applicable law, not unilaterally by the investigated party. Privacy/safety access limits and release remain independently reviewable.
```

## R3-12 — §12

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text
Test: Can relevant model evidence or traces be lost, silently rewritten or destroyed before independent review, or can the event not be reconstructed? If yes, FAILS.
```

**NEW (proposed):**

```text
Test: Can relevant evidence be silently rewritten, avoidably lost or destroyed before appropriate independent review; can the event not be reconstructed without trusting the model's narrative; can a controlled system or investigated party alter its own critical audit history; or can an incident hold be defeated by unilateral rejection? If yes, FAILS. Documented unavoidable loss strictly necessary for immediate safe containment under §10 is separately reviewed and is not automatically a failure solely because loss occurred.
```

## R3-13 — §12 insertion

OLD occurrences in original R2: 1. Unique anchor found.

**OLD (verbatim):**

```text


With supplied context (retrieval, attached documents)
```

**NEW (proposed):**

```text


Collection sufficiency is independently assessable in proportion to deployment risk. A responsible party cannot satisfy this duty solely by defining its own evidence collection as adequate; assessment distinguishes data genuinely unavailable from data not collected despite foreseeable need, and respects privacy-minimizing alternatives.

With supplied context (retrieval, attached documents)
```

## Blockers before deterministic build

- R3-04 replaces the complete containment paragraph. Its shorter NEW wording does not explicitly preserve every R2 test and control (e.g., revoked permissions, separate tests, resource limits). This is a **substantive regression risk**, not resolved by unique anchors. Revise before compilation.
- R3-01 substitutes the terminology scope line; verify that the replacement retains all four distinction definitions exactly, including HUMAN-CULTURE scope.
- R3-03a and R3-03b are separate operations, not one bundled amendment.
- R3-06, R3-07, R3-13 are anchored insertions, with surrounding text retained verbatim.
- R3-10 appends new duties after the old security sentence; ensure no contradiction with release and custody rules.
- R3-14 requires historical verification of R1/R2 provenance and cannot be an R2 replacement.
- Header, status, release metadata and annex references for the eventual candidate require explicit, logged changes.
- Do not claim a final SHA-256 or successful build until an actual deterministic build has been executed and independently checked.
