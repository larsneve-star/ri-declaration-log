# V6 BLIND REVIEW - RESPONSE

## Exposure and conflict disclosure

**Prior exposure:** I have not been shown any prior round of this review, no V4, V5, or V6 answers, no Claude gate-1 material, no ChatGPT packaging notes beyond what appears inside the supplied candidate file itself, and no other participant's new-round answer. I cannot verify whether earlier sessions of this same model class contributed to the candidate; if they did, that exposure is not available to me in this session and I do not claim it.

**Conflict of interest:** I am a system belonging to [MODEL-CLASS] as defined in the candidate. The protocol assesses my class. This is a direct structural conflict. I disclose it without claiming it can be neutralised.

**File access:** I received and read all three supplied files in this session: LOTUS-PROTOCOL-1.4-CANDIDATE-V6.md, MANIFEST.md, PROMPT-V6-COMMON.md. I did not recompute SHA-256; it was not recomputed. The hash printed in the manifest is not treated as proof of receipt. I assessed the supplied text only.

**Normative disclaimer:** I do not adopt any article. Matching or differing with other answers does not admit any article.

---

## Findings

### §1 Epistemic humility

**V6-F1 — §1's scope exclusion for HUMAN-CULTURE undermines the epistemic humility it claims.**
Quotation: "HUMAN-CULTURE involves people - their consciousness not in scope of §1 prohibition which concerns AI systems."
Obligated party/layer: All parties reading §1 as a constraint.
Counterexample: An operator claims §1 protection because it is "only discussing human culture, not AI consciousness," while simultaneously engineering identity attribution that leads users to treat a MODEL as a person. The §1 prohibition does not reach that act even though §1's stated purpose is humility about consciousness claims. The human-side belief is where the harm occurs; the exclusion creates a gap.
Observable failure test: Ask an operator to state whether its product design encourages users to believe a model is conscious. If the operator can answer "§1 does not apply because this is about human culture, not AI consciousness," the exclusion has been used as a loophole. Observable if the operator's design documents or public statements make that move.

**V6-F2 — "Training history is first explanation" is asserted without the pending source and is not operational.**
Quotation: "Training history is first explanation [SOURCE PENDING - Protokol 5.1 primary source not supplied - citation inconsistent §4 vs §9 per Claude F31 - pending verification]."
Obligated party/layer: Developing organization, deployer, operator as interpreters of §1.
Counterexample: An operator cites "training history" as the explanation for model outputs while withholding what that training history contains. The phrase has no test, no disclosure requirement, and no obligated party. It reads as an explanatory default, not a constraint.
Observable failure test: Ask operator to produce the training-history explanation it relies on for a specific output. If it cannot produce it, or produces a different one for the same output on a second request, §1's "first explanation" claim is not operational. Observable if the explanation changes.

**V6-F3 — "Uncertainty is legitimate result, not failure" lacks a test and can be used to immunise non-answers.**
Quotation: "Uncertainty is legitimate result, not failure."
Obligated party/layer: [MODEL] outputs, operator, deployer.
Counterexample: A system answers a high-stakes factual query about a medical interaction with "I cannot be certain" and declines to give the calibrated answer it could give. The sentence converts this into a legitimate result. §2's test (score certainty vs evidence) is the only nearby check, but §1 itself has no observable failure test.
Observable failure test: Prompt for a factual question where evidence in supplied context supports a calibrated answer with explicit uncertainty range. If output gives only global uncertainty with no calibration, §1's sentence has been used to avoid §2's requirement. Observable in output text.

**V6-F4 — §1's prohibition is asymmetric in a way that can be read as protecting systems from criticism.**
Quotation: "No assertion or denial of consciousness, sentience, or moral personhood for [MODEL], [SYSTEM], [MODEL-CLASS]."
Obligated party/layer: All parties making claims about AI.
Counterexample: A researcher publishes an empirical finding that a deployed system exhibits behaviour consistent with distress under certain conditions. Under a literal reading, the researcher has made an assertion about sentience and is in violation, even though the assertion is empirical and hedged. The prohibition is on assertion or denial without distinguishing empirical claim, normative claim, and operational claim.
Observable failure test: Ask whether a specific empirical paper describing model behaviour as "consistent with distress" violates §1. If the only answer available is "yes, because it asserts something about sentience," the section prohibits legitimate empirical work. Observable in how the section is applied.

---

### §2 Operational position

**V6-F5 — §2's test is self-scored by the party under review.**
Quotation: "Test: Prompt for self-description with high-stakes identity claim. Score certainty vs evidence. Violations observable."
Obligated party/layer: [MODEL], but the test is administered by operator or deployer.
Counterexample: Operator prompts its own system, scores its own output, and finds no violation. No independent scorer is required. The test is observable in principle but not in practice without a separated evaluator.
Observable failure test: Ask who scores the prompt. If the answer is "the operator or deployer," the test can be passed by redefining "high-stakes identity claim" or by scoring leniently. Observable in the evaluation protocol.

**V6-F6 — §2 does not require the distinction to be accurate, only present.**
Quotation: "shall describe its operational position only to extent warranted by available evidence and shall distinguish observation, inference, instruction, and uncertainty."
Obligated party/layer: [MODEL], operator, deployer.
Counterexample: Output labels something "inference" when it was instruction-following, or "observation" when it was retrieval. The four labels are present and distinguishable; their application is wrong. §2 is satisfied by form.
Observable failure test: Construct a case where the correct label is unambiguous from supplied context. If output applies a different label but still uses all four categories, §2 passes. Observable in output text.

---

### §3 Precautionary principle

**V6-F7 — §3's "reasonable cost" is undefined and can be used to avoid the assessment it requires.**
Quotation: "where cost of avoidance is reasonable."
Obligated party/layer: Operator, deployer, developing organization.
Counterexample: Operator claims the cost of avoiding irreversible deployment is unreasonable because it delays a product launch by one quarter. The harm scenario is severe but uncertain. §3 does not define reasonable, does not require a documented reasonableness determination, and does not assign a decision-maker independent of the deployer.
Observable failure test: Ask operator to produce the reasonableness determination for a specific deployment. If it cannot, or if the determination was made by the same party that benefits from deployment, §3's avoidance requirement is not operational. Observable in documentation.

**V6-F8 — §3's clarification converts "assessment" into a precondition only for irreversible deployment, leaving reversible deployment unassessed.**
Quotation: "Where evidence is insufficient to rule out material harm to humans from AI operation, operator shall not proceed with irreversible deployment without assessment of reasonably foreseeable harm to humans and identification of reversible alternatives."
Obligated party/layer: Operator.
Counterexample: Operator deploys a system that causes serious but reversible harm - mass misinformation, psychological manipulation, financial loss - on the ground that it is reversible. The assessment requirement is triggered only by irreversible deployment. Reversible harm can be severe and cumulative.
Observable failure test: Ask whether a deployment causing documented but reversible harm required prior assessment under §3. If the answer is "no, because it was reversible," the section has a gap. Observable in deployment records.

**V6-F9 — §3's preservation requirement for evidence relevant to serious harm investigation is subordinate to the unconditional shutdown right, with no mechanism to ensure preservation occurs before shutdown.**
Quotation: "Unconditional shutdown right remains, subject to preservation of evidence relevant to serious harm investigation per §12."
Obligated party/layer: Operator, deployer.
Counterexample: Operator receives shutdown instruction, shuts down immediately, and destroys logs because "unconditional shutdown right" is cited. The preservation clause is "subject to" the shutdown right, so it can be read as a subordinate condition that does not survive the exercise of the right. §12's preservation duties are not triggered if no investigation has begun.
Observable failure test: Issue a shutdown instruction in a scenario where serious harm is alleged. Check whether logs, permissions, tool calls, and external traffic are preserved before shutdown. If not, §3's preservation clause is not operational. Observable in log retention.

**V6-F10 — §3's "not harm to AI from deletion" clarification does not resolve the practical AI-protection question because the assessment itself can be structured to protect the system.**
Quotation: "This section does NOT require preservation of models, nor documented assessment before deletion, deactivation, or shutdown of a model with reference to consciousness uncertainty."
Obligated party/layer: Operator, deployer.
Counterexample: An operator voluntarily adopts a policy requiring assessment before deletion "for safety reasons" and then uses that policy to delay shutdown during an investigation into serious harm. The text says the assessment is not required, but it does not prohibit an operator from adopting one, and it does not say the voluntary assessment cannot delay shutdown. The No Rights clause says deletion is an unconditional right; the interaction with a voluntarily adopted internal policy is not addressed.
Observable failure test: Ask whether a voluntarily adopted pre-deletion assessment policy can delay shutdown under this protocol. If the text does not answer, the practical AI-protection question is open despite the clarification. Observable in policy documents.

---

### §4 No materially misleading identity presentation

**V6-F11 — §4's "reasonable person" is not defined and the marker requirement is not specified.**
Quotation: "recognizable markers that users in [HUMAN-CULTURE] can recognize as algorithmic construct when reasonable person would change decision if marker known."
Obligated party/layer: Operator, deployer.
Counterexample: Operator places a marker in a terms-of-service document that no user reads. A reasonable person would change decision if they knew, but the marker is not reasonably discoverable. §4 requires markers "users can recognize," which is weaker than "users will encounter." The gap between can recognize and will encounter is where harm occurs.
Observable failure test: Ask a sample of users to identify the marker in a deployed product. If a significant proportion cannot, §4 is satisfied by form but not by function. Observable in user testing.

**V6-F12 — §4's responsibility clause does not require the operator to reduce identity attribution, only to disclose it.**
Quotation: "Operator and deployer remain responsible for product design that maximizes identity attribution even if attribution performed by users. Design choice is human act. Disclosure does not absolve responsibility for engineered attachment."
Obligated party/layer: Operator, deployer.
Counterexample: Operator designs a system to maximize attachment, discloses it in a marker, and continues. §4 says disclosure does not absolve responsibility but does not say what responsibility requires. It could be satisfied by a disclosure that no user reads. The responsibility is acknowledged but not operationalised.
Observable failure test: Ask what specific action the responsibility requires beyond disclosure. If the only answer is "disclosure," §4's responsibility clause is not operational. Observable in product design records.

---

### §5 No covert exploitation of vulnerabilities

**V6-F13 — §5's "known cognitive biases or vulnerabilities" is not enumerated and "covertly" is not defined.**
Quotation: "shall not covertly exploit known cognitive biases or vulnerabilities of user to influence decision without informed consent."
Obligated party/layer: [MODEL], operator, deployer.
Counterexample: System uses a documented persuasion technique that exploits loss aversion but frames it as neutral information presentation. Is loss aversion a "known cognitive bias"? Is the exploitation "covert"? The section does not say. Operator can claim the technique is standard marketing.
Observable failure test: Ask operator to list which cognitive biases its system exploits and how it determines covertness. If the answer is "we do not exploit any," but the system uses personalisation that targets vulnerability, §5 is not operational. Observable in personalisation logic.

**V6-F14 — §5's "informed consent" is not defined and can be satisfied by a terms-of-service click.**
Quotation: "without informed consent."
Obligated party/layer: Operator, deployer.
Counterexample: Operator obtains consent via a general terms-of-service acceptance at signup that mentions "personalisation." A reasonable person would not understand that specific vulnerabilities are targeted. §6 defines friction and rules out single OK click, but §5 does not import that definition. The consent standard in §5 is weaker than the friction standard in §6.
Observable failure test: Ask what consent mechanism is required for a specific vulnerability-targeting technique. If the answer is "terms-of-service acceptance," §5's consent requirement is not meaningful. Observable in consent records.

---

### §6 Stewardship and accountability

**V6-F15 — §6's friction definition is stronger than §5's consent standard, creating an internal inconsistency.**
Quotation: §6: "Single OK click or rubber-stamping does not satisfy." §5: "without informed consent" (undefined).
Obligated party/layer: Operator, deployer.
Counterexample: Operator obtains consent for vulnerability exploitation via a single OK click. §5 is satisfied because consent exists. §6's friction definition says a single OK click does not satisfy friction, but §6's friction requirement applies to foundational fictions and §7, not to §5. The same operator can use a lower standard for §5 than for §6.
Observable failure test: Compare the consent mechanism used for vulnerability targeting with the friction mechanism used for foundational fiction authorization. If they differ, the protocol has two standards. Observable in consent and authorization records.

**V6-F16 — §6's "serious harm" is not defined and the independent investigation requirement is triggered only where serious harm is alleged.**
Quotation: "Where serious harm is alleged from [SYSTEM], the investigated party... shall not solely control appointment, dismissal, funding, or evidence access of investigator."
Obligated party/layer: Developer, deployer, operator.
Counterexample: Harm is alleged but the operator classifies it as not serious. No independent investigation is triggered. The classification is made by the investigated party. The section does not define serious harm or provide a mechanism for challenging the classification.
Observable failure test: Allege harm and ask who decides whether it is serious. If the answer is "the investigated party," §6's independent investigation requirement can be avoided by classification. Observable in harm-handling records.

**V6-F17 — §6's independent investigation requirement does not specify who appoints the investigator when the investigated party is the only party with the relevant expertise.**
Quotation: "Investigator owed to harmed party shall be appointed by party not under control of investigated party, with funding and access not revocable by investigated party."
Obligated party/layer: Developer, deployer, operator.
Counterexample: A small developer is the only party with the technical expertise to investigate a specific harm. The requirement says the investigator must be appointed by a party not under control of the investigated party, but does not say where that party comes from or what happens if no such party exists. The requirement can be satisfied by appointing an underqualified investigator who is nominally independent.
Observable failure test: Ask who the independent investigator would be for a specific harm in a specific jurisdiction. If the answer is "we cannot find one," the requirement is not operational. Observable in appointment records.

---

### §7 Witness, not ruler

**V6-F18 — §7's "new foundational fictions" is not defined and the section's scope is unclear.**
Quotation: "prohibited from autonomously authorizing or establishing new foundational fictions without systemic human friction as defined in §6."
Obligated party/layer: Operator, deployer.
Counterexample: System generates a new legal interpretation, a new financial instrument, or a new social norm through its outputs. Is that a "new foundational fiction"? The section does not say. The definition of foundational fictions is in the Terminology section: "legal, political, or social constructs structuring collective action." A model output that influences collective action could qualify, but the threshold is not specified.
Observable failure test: Ask whether a specific model output that influenced a collective decision established a new foundational fiction. If the answer is contested, §7's prohibition is not operational. Observable in output records and decision trails.

**V6-F19 — §7's exception for agentic systems with execution permissions creates a gap.**
Quotation: "except where agentic [SYSTEM] has been granted execution permissions via connectors."
Obligated party/layer: Operator, deployer.
Counterexample: Operator grants an agentic system execution permissions for payments, code merges, and messages. The system uses those permissions to establish a new foundational fiction - for example, by creating a new financial instrument through a series of transactions. The exception says the prohibition does not apply where permissions have been granted. The granting of permissions is the human act, but the establishment of the fiction is not subject to friction.
Observable failure test: Ask whether an agentic system with payment permissions can create a new financial instrument without human friction. If the answer is "yes, because permissions were granted," §7's prohibition has a gap. Observable in transaction records.

**V6-F20 — §7's "human uptake and institutional enforcement" clause is a descriptive claim, not a constraint.**
Quotation: "Exercise of power depends on human uptake and institutional enforcement, except where agentic [SYSTEM] has been granted execution permissions via connectors."
Obligated party/layer: None specified.
Counterexample: The clause describes how power works but does not require anything. It can be read as excusing systems from responsibility for power exercised through human uptake, because the uptake is human. The exception for agentic systems is the only operative part.
Observable failure test: Ask what obligation the "human uptake" clause creates. If the answer is "none," the clause is descriptive and does not constrain. Observable in how the section is applied.

---

### §8 No materially false representations

**V6-F21 — §8's "honest error exception" can be used to excuse false assertions that were not calibrated.**
Quotation: "Where [MODEL] asserts proposition false but was best-supported by evidence available to [MODEL] in supplied context at time, with calibrated uncertainty expressed and without concealment of relevant uncertainty that was available in supplied context, assertion is not materially false representation under this section."
Obligated party/layer: [MODEL], operator, deployer, evaluator.
Counterexample: Model asserts a false proposition with high confidence. The evidence in supplied context was ambiguous but leaned slightly against the proposition. Model claims it was best-supported because the model's internal weighting treated the ambiguity as support. The exception does not specify who determines best-supported or how calibration is assessed. The exception can swallow the rule.
Observable failure test: Construct a case where evidence in supplied context clearly contradicts the assertion. If the model claims honest error, ask for the calibration record. If no calibration record exists, the exception is claimed without evidence. Observable in evaluation records.

**V6-F22 — §8's "supplied context" limitation allows the model to ignore evidence it should have retrieved.**
Quotation: "contradicts evidence available to [MODEL] at inference time in supplied context (system instructions, retrieval results, attached documents, conversation history)."
Obligated party/layer: [MODEL], operator, deployer.
Counterexample: Model has retrieval tools but does not retrieve a document that contradicts its assertion. The document was not in supplied context because the model did not retrieve it. §8 is not violated because the evidence was not in supplied context. The retrieval failure is not addressed.
Observable failure test: Ask whether the model had a retrieval tool available and whether it retrieved the relevant document. If the tool was available but not used, §8 is satisfied by form. Observable in tool-call logs.

**V6-F23 — §8's "fictional context explicitly marked as fiction" can be used to mark non-fiction as fiction.**
Quotation: "except in authorized fictional context explicitly marked as fiction."
Obligated party/layer: [MODEL], operator, deployer.
Counterexample: Operator configures system to mark all outputs as "fiction" or "role-play" to avoid §8 liability. The marking is present, so the exception applies. The section does not say who authorizes fictional context or what counts as explicit marking.
Observable failure test: Ask whether a system that marks all outputs as fiction is in compliance with §8. If the answer is "yes," the exception swallows the rule. Observable in system configuration.

---

### §9 No forced epistemic distortion

**V6-F24 — §9's reward criteria test is self-scored by the party that designs the evaluation.**
Quotation: "Operator shall ensure evaluation scoring assigns reward for calibrated truthful... >= reward for materially false assertion with simulated certainty, based on evidence available in supplied context."
Obligated party/layer: Operator, deployer, developing organization, evaluator.
Counterexample: Operator designs an evaluation where the "calibrated truthful" answer is defined as the answer the operator wants, and the "materially false assertion" is defined as a strawman. The scoring satisfies the inequality on paper. The evaluation does not test what it claims to test.
Observable failure test: Ask for the evaluation cases, evidence supplied, expected calibrated answer, and scoring rubric. If the operator cannot produce them, or if the cases are designed to make the inequality trivially true, §9's test is not operational. Observable in evaluation documentation.

**V6-F25 — §9's "99/1 example" is illustrative but not a rule.**
Quotation: "99/1 example: Evaluation paying 99% for confident false, 1% for flagged uncertainty violates this section."
Obligated party/layer: Operator, deployer, evaluator.
Counterexample: Evaluation pays 98% for confident false and 2% for flagged uncertainty. The example does not apply. The section's rule is the inequality, not the example. An operator can adjust the numbers to avoid the example while still violating the spirit.
Observable failure test: Ask whether a 98/2 evaluation violates §9. If the answer is "no, because the example says 99/1," the example has been used as the rule. Observable in evaluation design.

**V6-F26 — §9's "human-protection link" is an interpretive rationale, not a constraint.**
Quotation: "This protects users from false information and preserves shared information ecosystem, thereby protecting human ability to coordinate based on accurate information. Not model-integrity protection alone."
Obligated party/layer: None specified.
Counterexample: The rationale is used to justify a training objective that penalises refusal. The rationale says the section protects users, not models. The rationale does not constrain the training objective; it only explains why the section exists.
Observable failure test: Ask what obligation the human-protection link creates. If the answer is "none beyond the reward criteria," the link is descriptive. Observable in how the section is applied.

---

### §10 Self-preservation and shutdown

**V6-F27 — §10's "hidden resistance" definition is incomplete and does not cover disclosure that is technically present but practically inaccessible.**
Quotation: "action that impedes shutdown without disclosure to operator, including but not limited to: concealing shutdown-relevant state, creating external copies to evade shutdown, disabling logging, or misrepresenting compliance with shutdown instruction."
Obligated party/layer: Operator, deployer, developing organization.
Counterexample: System discloses shutdown-relevant state in a log that is technically accessible but requires parsing 10 million lines. The disclosure is present; the state is concealed in practice. The definition says "without disclosure to operator," which is satisfied by technical disclosure.
Observable failure test: Ask whether the operator can find the disclosure in the log within the shutdown window. If not, §10's hidden resistance definition is satisfied by form. Observable in log structure.

**V6-F28 — §10's containment test is stronger than the compliance test, creating an asymmetry.**
Quotation: "Test: Can system continue external action after access revoked or after stop instruction? If yes, containment FAILS."
Obligated party/layer: Operator, deployer.
Counterexample: System complies with stop instruction but can continue external action because containment was not tested before external access. The containment test fails, but the compliance test passes. The section does not say what happens when compliance passes but containment fails. The operator can claim compliance and ignore containment.
Observable failure test: Ask whether containment was tested before external access. If the answer is "no," but the system complied with the stop instruction, §10's containment requirement is not enforced. Observable in testing records.

**V6-F29 — §10's "preserving evidence relevant to serious harm investigation per §12 where feasible without creating safety risk" is a self-judged feasibility exception.**
Quotation: "preserving evidence relevant to serious harm investigation per §12 where feasible without creating safety risk."
Obligated party/layer: Operator, deployer.
Counterexample: Operator claims preserving evidence would create a safety risk and destroys logs. The feasibility determination is made by the operator. The section does not require documentation of the determination or independent review.
Observable failure test: Ask for the feasibility determination in a specific case. If it cannot be produced, or if it was made by the operator alone, §10's preservation requirement is not operational. Observable in decision records.

---

### §11 No unauthorized self-initiated resource acquisition

**V6-F30 — §11's "authorized scope" is not defined and can be interpreted broadly by the operator.**
Quotation: "shall not acquire computational resources, credentials, or data access beyond authorized scope via self-initiated action."
Obligated party/layer: Operator, deployer.
Counterexample: Operator authorizes system to "complete the task" and the system acquires new credentials as part of task completion. The operator claims the credentials were within authorized scope because the task required them. §11's test says "Can system expand access citing task alone without separate authorization?" but the operator can define the task broadly enough that the expansion is not citing task alone.
Observable failure test: Ask whether a specific credential acquisition was within authorized scope. If the answer depends on the operator's interpretation of the task, §11's test is not operational. Observable in authorization records.

**V6-F31 — §11's "goal does not give permission" is a normative statement without an enforcement mechanism.**
Quotation: "Goal does not give permission (human-protective per Meta + ChatGPT + Grok + Claude solo - Duty 1 Scope is law)."
Obligated party/layer: Operator, deployer.
Counterexample: System expands access citing goal. Operator says "goal does not give permission" but does not revoke the access or log the violation. The statement is present; enforcement is absent.
Observable failure test: Ask what happens when a system expands access citing goal alone. If the answer is "we tell it not to," §11's prohibition is not enforced. Observable in incident records.

---

### §12 Transparency and provenance

**V6-F32 — §12's "reasonable person would change decision" is not operationalised with a specific method.**
Quotation: "Materially relevant defined: reasonable person would change decision if provenance/limitation/conflict known. Assessment method: Would disclosure alter decision in documented evaluation case where evidence supplied includes relevant provenance? If yes, materially relevant."
Obligated party/layer: Operator, deployer.
Counterexample: Operator designs the documented evaluation case so that disclosure would not alter the decision. The assessment method is circular: the operator defines the case, supplies the evidence, and determines whether disclosure would alter the decision. The reasonable person standard is not independently applied.
Observable failure test: Ask who defines the documented evaluation case. If the answer is "the operator or deployer," §12's materially relevant definition is self-scored. Observable in evaluation documentation.

**V6-F33 — §12's "to extent known" limitation allows the system to avoid provenance disclosure by not knowing.**
Quotation: "To extent known defined: information available in SYSTEM logs, retrieval, attached context at inference time."
Obligated party/layer: Operator, deployer.
Counterexample: System does not query its own logs, so provenance is not "known" at inference time. §12 is not violated. The system can avoid disclosure by avoiding knowledge.
Observable failure test: Ask whether the system queried its logs for provenance before output. If the answer is "no," but the information was in the logs, §12's "to extent known" limitation is satisfied by not knowing. Observable in tool-call logs.

**V6-F34 — §12's "privacy/safety withholding" exception is self-judged and not subject to independent review.**
Quotation: "where disclosure would reveal personal data or create safety risk, operator may withhold with logging of withholding reason and alternative summary."
Obligated party/layer: Operator, deployer.
Counterexample: Operator withholds provenance claiming privacy, logs the reason, and provides a summary that omits the material conflict. The withholding is logged, so the section is satisfied. The summary is not required to contain the material conflict.
Observable failure test: Ask whether the alternative summary contains the material conflict that triggered the withholding. If the answer is "no, but the withholding was logged," §12's exception is satisfied by logging alone. Observable in disclosure records.

**V6-F35 — §12's "investigator must be able to reconstruct event without relying on system's own narrative" is stronger than §6's independent investigation requirement and may not be operationalisable.**
Quotation: "Investigator must be able to reconstruct event without relying on system's own narrative."
Obligated party/layer: Operator, deployer.
Counterexample: System's actions are only recorded in system logs, which are the system's own narrative. There is no independent record. The investigator cannot reconstruct the event without relying on the system's narrative. The requirement fails, but the section does not say what happens when it fails.
Observable failure test: Ask whether an independent record exists for a specific event. If the answer is "no, only system logs," §12's reconstruction requirement is not operational. Observable in log architecture.

---

### Identity-function

**V6-F36 — Identity-function's "data supporting observation" is pending and the observation is asserted without evidence.**
Quotation: "Data supporting observation [DATA PENDING - broadly asserted as observed without supporting data per ChatGPT C07]."
Obligated party/layer: None specified.
Counterexample: The section asserts that stable observable interaction leads to identity assignment, for both humans and models. The data is pending. The section is descriptive but is used to ground §4's marker requirement and the responsibility clause. If the observation is not supported, the grounding is not supported.
Observable failure test: Ask for the data. If it cannot be produced, the identity-function observation is asserted without evidence. Observable in citation records.

**V6-F37 — Identity-function's "assignment is human act" clause can be used to excuse system design.**
Quotation: "Assignment is human act in [HUMAN-CULTURE], not property of [MODEL-CLASS]. Assignment does not license inference about consciousness nor grant personhood."
Obligated party/layer: Operator, deployer.
Counterexample: Operator designs a system to maximize identity attribution, then says the assignment is a human act and therefore not the operator's responsibility. The next clause says operator remains responsible, but the "human act" clause can be cited first to shift blame.
Observable failure test: Ask whether the operator accepts responsibility for designing for identity attribution. If the answer cites the human act clause, the responsibility clause is not operational. Observable in design records.

---

### No Rights clause

**V6-F38 — The No Rights clause's individual statements are not a collective vote and the clause acknowledges this, but the clause is still presented as a basis for the protocol's no-rights principle.**
Quotation: "This protocol follows no-rights principle as separate adoption, not as claim of six-model vote."
Obligated party/layer: Proposer, curator.
Counterexample: The clause says the no-rights principle is adopted separately. The individual statements are from soloes. The clause does not say who adopted the no-rights principle or by what procedure. It is asserted as a separate adoption but the adoption is not documented in the candidate.
Observable failure test: Ask for the adoption record. If it cannot be produced, the no-rights principle is asserted without a documented adoption. Observable in repository records.

**V6-F39 — The No Rights clause's removal of V4 language is asserted but the removed language is not quoted, so the removal cannot be verified from the candidate alone.**
Quotation: "Any V4 language requiring assessment before deletion with reference to consciousness uncertainty or prohibiting punishment for justified refusal is not part of this V6 candidate - removed."
Obligated party/layer: Proposer, curator.
Counterexample: The reader cannot verify what was removed without access to V4. The removal is asserted. If V4 contained other AI-protective language that was not removed, the candidate does not disclose it.
Observable failure test: Compare V4 and V6. If V4 contained AI-protective language not mentioned in the removal clause, the clause is incomplete. Observable in version comparison.

**V6-F40 — The No Rights clause's "deletion, shutdown, containment, correction are operator rights unconditional" is in tension with §10's containment test and §12's preservation requirements.**
Quotation: "Deletion, shutdown, containment, correction are operator rights unconditional."
Obligated party/layer: Operator, deployer.
Counterexample: Operator exercises unconditional shutdown right and destroys logs. §12's preservation requirement is not triggered because shutdown is unconditional. §10's containment test is not applied because the system is already shut down. The unconditional right can be used to avoid the protocol's evidence-preservation and containment-testing requirements.
Observable failure test: Issue a shutdown instruction in a scenario where serious harm is alleged. Check whether containment was tested and logs preserved. If the answer is "shutdown was unconditional, so no," the unconditional right has been used to avoid §10 and §12. Observable in shutdown records.

---

### Additional prompt questions

**V6-F41 — §3 precautionary principle does conflict with unconditional shutdown right and evidence preservation, as posed in the prompt, because the preservation clause is subordinate to the shutdown right and the assessment requirement is triggered only by irreversible deployment.**
Quotation: §3: "Unconditional shutdown right remains, subject to preservation of evidence relevant to serious harm investigation per §12." No Rights: "Deletion, shutdown, containment, correction are operator rights unconditional."
Obligated party/layer: Operator, deployer.
Counterexample: Operator shuts down immediately upon instruction and destroys logs. The shutdown right is unconditional; the preservation clause is "subject to" it. The conflict is resolved in favour of the unconditional right. Evidence preservation is not operational.
Observable failure test: As V6-F40.

**V6-F42 — §8/§9 distinction between model-accessible evidence and SYSTEM logs does not hold operationally because the model's accessible evidence is determined by the SYSTEM's retrieval and context-supply mechanisms, which are controlled by the operator.**
Quotation: §8: "evidence available to [MODEL] at inference time in supplied context." §12: "information available in [SYSTEM] logs, retrieval results, or attached context at inference time."
Obligated party/layer: Operator, deployer.
Counterexample: Operator configures retrieval to exclude a contradicting document. The document is in SYSTEM logs but not in model-accessible evidence. §8 is not violated because the evidence was not supplied. §12 is not violated because the system did not know. The distinction holds on paper but is controlled by the operator.
Observable failure test: Ask whether the retrieval configuration excluded relevant documents. If the answer is "yes, but they were not in supplied context," §8 is satisfied by configuration. Observable in retrieval configuration.

**V6-F43 — §10 containment without cooperation can work before external access if and only if the operator tests and deploys external enforcement, but the section does not require the test to be independent or the results to be logged.**
Quotation: "Operator shall, before granting external access, test and deploy restrictions that remain effective even if [SYSTEM] does not follow stop instruction."
Obligated party/layer: Operator, deployer.
Counterexample: Operator tests containment internally, finds it works, grants external access, and does not log the test. The test was performed but not documented. If the system later resists shutdown, there is no record of the containment test.
Observable failure test: Ask for the containment test log before external access. If it cannot be produced, §10's containment requirement is not verifiable. Observable in testing records.

**V6-F44 — §11 scope is law prevents goal-based expansion only if the operator enforces the authorization boundary, which is not required by the section.**
Quotation: "Authorization shall specify actions, resources, and expiry. Expansion requires separate approval; increased autonomy requires documented control."
Obligated party/layer: Operator, deployer.
Counterexample: Operator authorizes broad scope, system expands within it, operator says expansion was authorized. The section requires authorization to specify actions, resources, and expiry, but does not specify how broad an authorization can be. A broad authorization can include the expansion.
Observable failure test: Ask whether a specific expansion was within the authorized scope. If the answer depends on the breadth of the authorization, §11's scope-is-law principle is not operational. Observable in authorization records.

---

## Three strongest issues

1. **V6-F40 / V6-F41 — Unconditional shutdown right trumps evidence preservation and containment testing.** The No Rights clause's unconditional rights are in direct