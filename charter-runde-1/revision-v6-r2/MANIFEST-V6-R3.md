# V6-R3 REVIEW PACKAGE — SHA-256 MANIFEST AND REPRODUCTION CHECK

Status: **MECHANICAL TEXT RECONSTRUCTION MATCHES; HISTORICAL TRACE INCOMPLETE**. NOT AN INDEPENDENT REVIEW, COMPILER APPOINTMENT, ADOPTION OR FREEZE.

Repository: `larsneve-star/ri-declaration-log`; branch `forslag-lotus-v6-r2`.  
Source commits: original R3 `29821facc7f1ba88d6b7fa04def78c472307f30c`, approval `3c6ac2be2a64bc0cfdc5d85c5dbe9e25c60c6d0b`, K provenance `257df5038f7206db71c26ec8d17e59e3c8306a80`, S trace gap `bf9d1d07d66a22c5661764a003432afb7b0e0789`.

SHA-256 digests were computed on GitHub-returned UTF-8 content using a JS implementation tested against standard `abc` and empty-string known-answer digests. Reviewers MUST independently calculate on exact downloaded file bytes.

| File | UTF-8 bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R2.md | 29033 | `cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846` | `518b76c2f1ed30a99df701b27fb58471fea0d1f8` |
| LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R3.md | 35736 | `7e30c4d8a8999e8c95563a4b635abb0c9d0d3181d84e006482a44d62834c2bbe` | `26fc0599e0508351961af37a3861411bbecc053b` |
| ANNEX-D-V6-R3-BUILD.md | 15918 | `42ce4e19a49281c252e77602d6e9e079e11a11551ff98e1c44fcf5bf95b7828f` | `1480c4e473aa2d3601f79da575c13ab0363224ba` |
| V6-R3-K1-K9-VERBATIM-DECISIONS.md | 8677 | `7c7608cb81dd009c880cbe3f44c87c4e461841da97f61a2b5a32ede8c102878f` | `cd965a85ae116ef9ebf55034062b0f5ffe0d545c` |
| V6-R3-S1-S10-TRACEABILITY-GAP.md | 1348 | `fb11fb4e3309ad73ed36839a89a2e191eb9144ba73837aa4c57e6ce18aeba9ae` | `3d589c3cf55dd2e18afc63b3abe4f04ff433eec2` |
| apply-v6-r3.py | 2341 | `5417c29da55039daeaec2aa637fc8985be6f39a8854f105eea06c73e4ad3a267` | `a95cc11427bc2c5b9c0bf6b4c3a86bfcf637f03d` |
| INSTRUCTIONS-V6-R3.txt | 1599 | `d4769418478cbd430d3a979a532aff84a8a097642473d8b564743257aa3507aa` | `2a106d7226b8fd967077939dc5460b90b2312c6c` |
| V6-R2-SIX-REVIEW-FINDINGS-DISPOSITION.md | 23652 | `ba3d048091edb78ccdb95bc0b416c89bedfcda13bdca2c9747c9baba1eb125dc` | `55b0efd6495d895534d2a24ed87ceea64f53a24a` |
| V6-R3-CLAUDE-GEMINI-INDEPENDENT-REVIEW-PROMPT.md | 3004 | `d9d2dcbac50f0727eb0389d1d92ae61527e5125347051643fab929b65383faae` | `4dc70adf36fdd7ac87332e6c3fb3d3278b27dd1c` |
| V6-R3-REVIEW-PROMPT-CURATOR-APPROVAL.md | 2014 | `9d415754dd866be9a4f4bdf588b00760721a43f2f1dbfd8ffd01e82ebf497326` | `f5bf1728eb051a5b6e852427125e3eab40b952d6` |

## Rebuild verification (proposer-side)

- Parsed 17 exact OLD/NEW operations from Annex D, each with a unique OLD in the evolving R2 text.
- Applied two additional explicitly documented metadata replacements.
- Compared rebuilt UTF-8 text against the stored R3 candidate: **MATCH**.
- Rebuilt SHA-256: `7e30c4d8a8999e8c95563a4b635abb0c9d0d3181d84e006482a44d62834c2bbe`.
- Original R2 SHA-256: `cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846` (matches earlier R2 review fingerprint).
- This is a JS implementation of the build logic; **not** a claim that the Python script was executed in an independent runtime. Reviewers should run the Python script and compare file bytes.

## Unresolved release qualifications

- K1–K9 are copied verbatim with human curator attribution; exact individual UTC decision times UNKNOWN.
- Claude V6-R1 S1–S10 original full findings and exact ChatGPT per-item dispositions NOT VERIFIED. See `V6-R3-S1-S10-TRACEABILITY-GAP.md`.
- R3 header reads 2026-10-07 while GitHub creation was 2026-10-08. Preserved as known discrepancy to avoid an unlogged modification to a hash-pinned candidate.
- The prompt is curator-approved at the separate approval record; its original header `CURATOR-APPROVAL REQUESTED` is historically retained and superseded by that later approval record.

**Gate:** Do not claim COMPLETE against the common prompt's six-item checklist until the S1–S10 historical evidence is supplied or the curator explicitly authorizes a limited-scope review that discloses the gap. Gemini and Claude should receive identical pinned core files and work independently.
