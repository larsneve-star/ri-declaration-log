# V6-R3 — EXACT-ANCHOR PRECOMPILATION AUDIT

Status: EDITORIAL MECHANICAL PRECHECK ONLY — NO COMPILATION / ADMISSION / FREEZE

Base file: `LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R2.md` at branch `forslag-lotus-v6-r2`, blob SHA `518b76c2f1ed30a99df701b27fb58471fea0d1f8`.

Proposal: `V6-R3-CHANGE-SET-PROPOSED.md`, blob SHA `88540149e7576deb4f1c47c9a7d5fa6e87890b79`.

## R3 item anchor check

- R3-01: FOUND — `Scope of §1: No categorical assertion or denial of AI consciousness`
- R3-02: FOUND — `No categorical assertion or denial of AI consciousness, sentience or moral personhood.`
- R3-03: FOUND — `This does not waive preservation of a model artefact when it is relevant evidence under §12`
- R3-04: FOUND — `Containment without system cooperation:`
- R3-05: FOUND — `If an emergency makes a particular preservation step unsafe`
- R3-06: FOUND — `## §10 Self-preservation and shutdown`
- R3-07: FOUND — `Investigatable traces and model evidence:`
- R3-08: FOUND — `A credible suspicion of possible unlawful conduct shall trigger preservation`
- R3-09: FOUND — `Preserve the relevant model version, weights and configuration`
- R3-10: FOUND — `Secure relevant artefacts against alteration and destruction`
- R3-11: FOUND — `Define proportionate retention before use`
- R3-12: FOUND — `Test: Can relevant model evidence or traces be lost`
- R3-13: FOUND — `Known information means information actually available`
- R3-14: NOT FOUND AS LITERAL — `At inference time`

## Overlap and editorial blockers

- R3-03 contains two replacements in different sections (§3 and No Rights), so must be split into separately auditable operations.
- R3-04 is a whole-paragraph replacement of §10 containment; preserve existing test criteria and enforcement details explicitly rather than assuming the shorter draft is equivalent.
- R3-05 is embedded in the §10 obligation paragraph; use exact sentence replacement, not a paragraph-level overwrite.
- R3-06 is an insertion in §10 and may overlap with R3-04. Specify a unique insertion boundary.
- R3-07/R3-08/R3-09/R3-10/R3-11/R3-12 target the same §12 paragraph. Compile as sequential, non-overlapping sentence operations and test all anchors against the original R2 before applying.
- R3-13 is a distinct insertion after the `Known information` paragraph.
- R3-14 is a provenance audit instruction, not a normative replacement. Its historical `At inference time` wording is not an anchor in the current R2 file; review R1/R2 Annex history separately.
- R3 title/status/authorship need separate explicit old/new operations. Never leave a compiled R3 headed V6-R2 or falsely describe its review status.
- K5 does not establish a numerical deadline; do not silently insert one.
- Preserve R2 untouched, and retain all six original reviews and Gemini dissent.

## Gate

This audit is a proposer self-check only. It does not certify correctness of normative wording or constitute noncompiler verification. Next: exact byte-level Annex and deterministic build, then independent check and compiler designation/admission procedure.
