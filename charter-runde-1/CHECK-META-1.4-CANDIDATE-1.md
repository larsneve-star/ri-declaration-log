# ChatGPT mechanical check of Meta Lotus 1.4 candidate package

Date: 2026-10-07 UTC
Status: sources archived; mechanical change-plan verification FAILS. No freeze or adoption.
Role: repository maintainer/mechanical checker, with prior Lotus participation disclosed. Editorial observations are not independent substantive certification.

Sources:
- LOTUS-PROTOCOL-1.4-CANDIDATE.md — SHA-256 7880521b28752e4fd6d60982856fc4d9cb204831b35c45813b0daea0c5a970d3
- ANNEX-D-1.4-PROPOSED.md — SHA-256 7dc4c1f66dbd548d153bf7814eaa7551a421ab4d9c497e7df19fe8db3f8ebc24
- DISPOSITIONS-F1-F33.md — SHA-256 9d901fba7b4dc78abc79e9aef37ab07b516d5a2f2799efbe70c77f3031b69e01
- Baseline 1.3 unchanged — SHA-256 1a52e04e26263f1c9933ce61b42567732aa4eb48460f62255a46484328a064fd

C01 — Coverage passes at heading level: §1 through §12 occur once each, and F1 through F33 each have a separate disposition heading. This does not establish complete normative content or correct findings.

C02 — Exact old/new fields fail. For each Annex D item, read the whole Quote 1.3 and Replacement 1.4 line, remove one enclosing pair of straight quotes if present, and search it as a literal substring in baseline/candidate respectively. Results:

| ID suffix | Old field exact in 1.3 | New field exact in candidate |
| --- | --- | --- |
| 001 | No | No |
| 002 | Yes | Yes |
| 003 | No | No |
| 004 | No | No |
| 005 | Yes | No |
| 006 | Yes | No |
| 007 | No | No |
| 008 | No | No |
| 009 | No | No |
| 010 | No | No |
| 011 | No | No |
| 012 | No | No |
| 013 | No | No |

This is a literal-field check, not a rejection of the proposal's merits. Several fields are descriptions, composite quotations or ellipses, so they are not usable as exact replacements. Request exact fenced old/new blocks with unique target anchors, or a machine-readable patch plan. Multi-location edits must be separated or explicitly specified. Applying all proposed edits must reconstruct the complete candidate exactly; all deletions and additions, including concluding metadata, must be accounted for.

C03 — Carry-forward is not literal. Annex D calls §3 unchanged, but its wording differs (the Protokol 5.1 reference is removed). It calls §8 core unchanged, but candidate adds an absolute prohibition absent from the original one-line article. §5 and §11 receive full new sentences, not verbatim carry-forward. Record those exact additions and deletions.

C04 — Normative gaps. §3 says a principle is normative and hypotheses get no immunity, but never states what precaution requires. §10 describes a behavior and marks a source pending, but does not constrain hidden shutdown resistance or identify the responsible party's shutdown duties. Those are material gaps, not just missing tests.

C05 — Honesty and deception. §8's unconditional ban on materially false representation still lacks §9's allowance for honest evidence-limited error and authorized fictional context. §9 attributes "known or should-have-been-known" to SYSTEM although SYSTEM is expressly a mechanism, not a duty-bearer. Define observable output behavior and operator/evaluator assessment criteria without assuming system-wide knowledge access. The 99/1 example is useful, but matched evaluation cases and scoring criteria remain unspecified.

C06 — Responsibility and materiality. Operator/deployer naming is improved. Developing organization is named in general and §9, but not assigned clear differentiated duties throughout. The reasonable-person materiality criterion requires an actual assessment method. Distinguish constraints on product design from what an individual output can comply with. Provenance disclosure must preserve legitimate privacy/safety withholding.

C07 — Separation and consistency. Candidate still contains editorial FIX/per-F comments in articles, and §6 repeats §7's foundational-fiction prohibition while dispositions claim distinct scopes. HUMAN-CULTURE is a practice involving people, not an entity whose consciousness is in question; §1's list needs appropriate scope. Identity attribution remains broadly asserted as observed without supporting data. Several tests or source checks remain pending, despite disposition language saying "fixed".

C08 — Disposition summary fails arithmetic/coverage. The summary's accepted ranges contain 29 IDs, not the stated 28, and omit F27. F31 is both in the accepted ranges and in the pending list; F17 has a mixed accepted/pending disposition. Use one primary status per F ID with optional source-check substatus and produce counts from the actual 33 entries. Annex D 013 says Claude pending while candidate says answer delivered; distinguish historical snapshot status from current status.

C09 — Authorship disclosure received from curator: author Meta AI synthesis-holder; exposure to Grok/DeepSeek Lotus 1.2 verbatim, GPT/Gemini summaries, Claude F1-F33, ChatGPT packaging/M01-M08 and repository log; missing Gemini original and exact Grok/DeepSeek platform timestamps; conflict: text about MODEL-CLASS. These are supplied disclosures, not independently verified platform identity. No blind-round status or six-model consensus is certified.

C10 — Next deliverable: a separate corrected candidate and corrected Annex/dispositions (retain all originals), with complete normative articles, exact reproducible transformation from 1.3, complete F1-F33 statuses and unresolved sources clearly pending. Formal compiler eligibility/exception and substantive verifier still need explicit resolution before freeze. Hash integrity checks alone cannot certify the content.
