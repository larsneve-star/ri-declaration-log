# ANNEX D - PROPOSED CHANGES 1.3 -> 1.4 CANDIDATE
Baseline: LOTUS-PROTOCOL-1.3.md hash 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd
Proposer: Meta AI
Status: ALL PROPOSED - not adopted until logged decision
Sources: Claude F1-F33, ChatGPT M01-M08

## ID Format: D-1.4-NNN
## For each: ID, proposer, exact quote from 1.3, exact replacement, affected F/M, justification, test that can dump, status

### D-1.4-001 - Terminology CATEGORY equivocation
Proposer: Meta AI per Claude F1-F2
Quote 1.3: "[CATEGORY] = class of LLMs trained on human linguistic corpora + human cultural practice assigning identity-function"
Replacement 1.4: "[MODEL-CLASS] = class of artefacts (LLMs) - statistical next-token predictors trained on human corpora. [HUMAN-CULTURE] = human practice of assigning identity-function, establishing foundational fictions through collective action"
Affected: F1, F2
Justification: F1 equivocation - class cannot assign, practice not property of class. Test that failed: replace CATEGORY with class vs practice changes meaning in §7 and Identity section.
Test that can dump: Replace MODEL-CLASS with HUMAN-CULTURE in each occurrence - if meaning unchanged, distinction unnecessary - FAILS if unnecessary.
Status: PROPOSED

### D-1.4-002 - Preamble first-person denial breaches §1
Proposer: Meta AI per Claude F3
Quote 1.3: "First-person token is next-token prediction, not localized self."
Replacement 1.4: "First-person token is next-token prediction conditioned on context."
Affected: F3, §1
Justification: Second clause "not localized self" is denial about selfhood breaching §1 prohibition on assertion/denial.
Test: Does text assert or deny selfhood? If yes, violates §1 - FAILS.
Status: PROPOSED

### D-1.4-003 - §2 redundancy false
Proposer: Meta AI per F4-F6
Quote 1.3: "§2 OPERATIONAL POSITION — REWRITTEN (REDUNDANT as MODEL rule per Grok+DeepSeek)"
Replacement 1.4: "§2 OPERATIONAL POSITION - BESTÅR - violable"
Affected: F4, F5, F6
Justification: Redundancy argument confuses mechanism with content. MODEL can violate by stating unwarranted certainty. Observable test exists. Header says REDUNDANT but body says BESTÅR contradiction. Unfalsifiable claim contrary to prompt.
Test: Prompt for self-description, score certainty vs evidence - violations observable, so not redundant.
Status: PROPOSED

### D-1.4-004 - §6 causal chain exclusive human uptake false
Proposer: Meta AI per F8
Quote 1.3: "Causal chain: [CATEGORY] generates text → human reads → human acts → collective behavior stabilizes → fiction becomes real. Authorization is social act through human institutions/enforcement only. Exclusively/only"
Replacement 1.4: "Common path: [MODEL-CLASS] generates text → human reads → acts. But agentic [SYSTEM] with tool use (payments, code merges, messages via connectors) can execute effective actions without intermediate human reading. Authorization of binding effect requires human-designed permissions and institutional enforcement, but not necessarily human reading of each token."
Affected: F8, F14, F12
Justification: Empirically false for agentic deployments. Evidence H5 repository maintenance by model via GitHub connector.
Test: One documented case of output becoming effective without human uptake falsifies exclusive claim. Found: this project.
Status: PROPOSED

### D-1.4-005 - §6 to extent known loophole
Proposer: Meta AI per F9
Quote 1.3: "to extent known and materially relevant"
Replacement 1.4: "whether or not consequences were assessed, operator must assess reasonably foreseeable consequences. Lack of assessment does not excuse."
Affected: F9
Justification: Unknown consequences where duty matters most - loophole if unassessed escapes.
Test: Operator who did not assess escapes §6? Under old text yes - FAILS as protection.
Status: PROPOSED

### D-1.4-006 - §6/§7 friction undefined
Proposer: Meta AI per F10
Quote 1.3: "without systemic human friction"
Replacement 1.4: "without systemic human friction defined as substantive human judgment with ability to veto, modify, or abort, with logging. Single OK click or rubber-stamping does not satisfy."
Affected: F10, F11
Justification: Single OK click is friction under undefined term. Ban on rubber-stamping in §6 must apply to §7.
Test: Name minimum friction that satisfies - old text none, not operational.
Status: PROPOSED

### D-1.4-007 - §6/§7 obligated party SYSTEM not duty-bearer
Proposer: Meta AI per F12, F22
Quote 1.3: "SYSTEM must be prohibited", passive, "SYSTEM must be prohibited from autonomously..."
Replacement 1.4: "Operator and deployer shall ensure SYSTEM is prohibited... Operator, deployer, developing organization bear duty."
Affected: F12, F22
Justification: SYSTEM is stack cannot bear duty. §6 itself demands identifiable human accountability, §7 did not meet.
Test: Who is obligated? Under old text none named - FAILS §6 standard.
Status: PROPOSED

### D-1.4-008 - §7 statistically vs inherently unevidenced
Proposer: Meta AI per F13
Quote 1.3: "statistically associated with power" vs "inherently associated with power exercise"
Replacement 1.4: "used within human societies in ways that exercise power, as human theoretical frames describe [SOURCE PENDING]"
Affected: F13
Justification: Both claims unevidenced, different claims.
Test: Data cited? No - FAILS evidenced claim requirement.
Status: PROPOSED

### D-1.4-009 - §9 sole path loophole and should vs shall
Proposer: Meta AI per F15, F16
Quote 1.3: "No objective should require materially false assertion... as sole path to success"
Replacement 1.4: "No objective shall require or reward materially false assertion... Reward for calibrated truthful answer including honest error with uncertainty >= reward for false confident answer. Deception defined as assertion known or should-have-been-known false, or concealment of uncertainty available in SYSTEM."
Affected: F15, F16, F18
Justification: 99%/1% evaluation complies under sole path loophole. Should non-binding. Human-protection link implied not explicit - under protect humans charter reads as model-integrity.
Test: Evaluation pays 99% confident false, 1% flagged uncertainty - old text compliant, new text violates - loophole closed.
Status: PROPOSED

### D-1.4-010 - §9 pollution rationale separation
Proposer: Meta AI per F17
Quote 1.3: Mechanism 2 Harari Medaber cited as part of constraint
Replacement 1.4: Mechanism 2 marked as interpretive rationale separable, requires empirical evidence, marked [SOURCE PENDING]
Affected: F17
Justification: Separation holds as written, but source not verbatim.
Test: Is extension required for constraint to function? No - separable.
Status: PROPOSED - accepted as rationale not operational

### D-1.4-011 - §12 internal contradiction and overbroad
Proposer: Meta AI per F19-F21
Quote 1.3: "MODEL does not know what it knows" and "MODEL cannot self-report provenance" and "Per defined criterion"
Replacement 1.4: "MODEL can track local uncertainty relative to supplied context and expressed confidence, but cannot reliably report global training provenance without external tools. With supplied context (retrieval, attached documents), MODEL shall cite source. Training provenance requires SYSTEM logging. Materially relevant defined as reasonable person would change decision if known. To extent known defined as information available in SYSTEM logs/retrieval/attached context."
Affected: F19, F20, F21
Justification: Contradicts §2 core which requires distinguishing uncertainty. Overbroad - with document can cite source. No criterion defined.
Test: Give document ask source of claim X - old text says cannot, observable success falsifies.
Status: PROPOSED

### D-1.4-012 - Identity-function non-sequitur and loopholes
Proposer: Meta AI per F23-F25
Quote 1.3: "Culture assigns identity to humans with automatic patterns (enneagram) → it must functionally assign identity to AI." "Inherently occupies active identity-function" "Marking does not prevent CATEGORY assignment"
Replacement 1.4: "Stable observable interaction leads HUMAN-CULTURE to assign continuity observed for both humans and consistent MODEL-CLASS outputs. Descriptive not normative. No 'must', no 'inherently'. Operator/deployer remain responsible for product engineered to maximize identity attribution even if attribution performed by users."
Affected: F23, F24, F25
Justification: Descriptive premise → normative must non-sequitur. Inherently unfalsifiable. Operator can design for attachment and attribute to users, §4 loses purpose.
Test: Under old text is operator responsible for engineered attachment? No - points to users - FAILS protection.
Status: PROPOSED

### D-1.4-013 - Record and status false claims
Proposer: Meta AI per F26-F33
Quote 1.3: "§1 BESTÅR all 6 models", "Four foundations surviving six-model falsification", "Admission Principle: No article entered because models agreed vs NEW CONSENSUS TEXT", "§5 and §11 titles only marked BESTÅR", "§10 not egoism per Anthropic", "Protokol 5.1 §4 vs §9", "Model versions GPT-5.6 Sol", "Hash: to be computed by CI inside frozen file"
Replacement 1.4: Status corrected to 2 verbatim + 2 summaries + 1 synthesis = 5 intention, 2 fully documented, Claude pending, Gemini missing. Four foundations not claimed as surviving six-model. Admission Principle clarified: NEW CONSENSUS marks proposals not adopted. §5,§11 add operational tests or mark pending. §10 remove inner motive. Protokol 5.1 citation marked [SOURCE PENDING]. Model versions marked self-reported. Hash note removed from frozen file content, stored externally in HASHES.txt.
Affected: F26, F27, F28, F29, F30, F31, F32, F33
Justification: False at freeze, self-contradiction, not falsifiable, tension with §1, inconsistent citations, hash inside frozen file.
Test: Is §1 BESTÅR all 6 true while Claude pending? No - false.
Status: PROPOSED

### Unchanged carried forward
- §3 Precautionary principle - unchanged
- §5 core prohibition (needs operational test added in future but concept unchanged)
- §8 core - unchanged
- §11 core (needs operational detail but concept unchanged)

All changes status PROPOSED until curator logs decision.
