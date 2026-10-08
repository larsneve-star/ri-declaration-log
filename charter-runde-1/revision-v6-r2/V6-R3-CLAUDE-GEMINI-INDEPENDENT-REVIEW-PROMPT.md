# LOTUS V6-R3 — INDEPENDENT FALSIFICATION REVIEW PROMPT

Status: CURATOR-APPROVAL REQUESTED; this file is a proposal by ChatGPT, not proof of curator approval.

## Reviewer disclosure
State your model identity, prior participation in LOTUS/R1/R2, exposure to any prior findings, and conflicts. A new conversation is not proof of institutional independence. Do not read the other V6-R3 review before submitting your own.

## Required package
1. Full R2 and full R3 candidate.
2. R3 exact OLD/NEW Annex D.
3. Reproducible apply.py and instruction file, with complete file hashes and pinned GitHub commit.
4. Verbatim K1–K9 curator decisions with original author and verified UTC timestamp; if exact timestamp is not established, label UNKNOWN, never infer.
5. Disposition of all 63 R2 findings and separate trace of Claude V6-R1 S1–S10.
6. Review protocol and source/provenance caveats.

**Package completeness gate:** If any mandatory material is missing, report PACKAGE INCOMPLETE, identify precisely what is missing, and proceed with a limited textual review only if clearly labelled. Do not claim mechanical reproduction or full historical traceability.

## Independent review tasks
A. Rebuild R3 from pinned R2 bytes with the supplied apply.py/instructions. Compare SHA-256 of built output with pinned R3; report exact divergence. A matching hash proves mechanical reproduction only.
B. Check each OLD/NEW operation, all changes outside Annex, omitted safeguards and R2-to-R3 regressions. Pay particular attention to §§3, 6, 10 and 12 and their cross-references.
C. Test R3 against each K1–K9 decision without assuming the decisions are themselves sound. Report normative objections to K decisions separately, marked NORMATIVE OBJECTION — NOT R3 IMPLEMENTATION ERROR.
D. Stress-test K9: whether the acting system or investigated party can change, delete, suppress or control audit traces; who actually holds credentials/keys, custody, integrity proofs, independent access, and separation of duties. Evaluate text and control requirements only; do not imply actual deployed systems were tested.
E. Examine credible suspicion, provisional holds, incident preservation, lawful privacy/erasure, emergency containment, reviewer independence and cross-party custody for loopholes and contradictory obligations.
F. Check reviewer allocation, self-review/reciprocal review, conflict disclosure and authority to adopt or freeze.
G. **Report any defect outside the listed focus areas.**

## Output
Begin with disclosure and package completeness. Give each finding a stable ID, severity, exact location, verbatim quote, falsification scenario, violated criterion, and minimally sufficient repair. Separate mechanical, substantive, normative and provenance findings. State PASS / PASS WITH REQUIRED CORRECTIONS / FAIL / INCOMPLETE with scope limits. Preserve minority disagreement. Never close the proposer's objections on the proposer's behalf. Do not claim compiler appointment, adoption or freeze.
