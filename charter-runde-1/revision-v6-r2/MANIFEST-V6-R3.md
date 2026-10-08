# V6-R3 REVIEW PACKAGE — VERIFIED DIGEST MANIFEST (EDITORIAL)

Repository: `larsneve-star/ri-declaration-log`  
Branch: `forslag-lotus-v6-r2`  
Pinned package HEAD before manifest update: `8804caea4c25259cf6745f236c933e574e533958`  
Status: hashes computed from GitHub-returned UTF-8 file contents; SHA-256 implementation passed known-answer tests for `abc` and empty input. Reviewers must independently calculate on downloaded bytes. Git blob hashes are SHA-1 and distinct from SHA-256.

| File | Bytes | SHA-256 | Git blob SHA-1 |
|---|---:|---|---|
| LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R2.md | 29033 | `cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846` | `518b76c2f1ed30a99df701b27fb58471fea0d1f8` |
| LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R3.md | 35736 | `7e30c4d8a8999e8c95563a4b635abb0c9d0d3181d84e006482a44d62834c2bbe` | `26fc0599e0508351961af37a3861411bbecc053b` |
| ANNEX-D-V6-R3-BUILD.md | 15918 | `42ce4e19a49281c252e77602d6e9e079e11a11551ff98e1c44fcf5bf95b7828f` | `1480c4e473aa2d3601f79da575c13ab0363224ba` |
| apply-v6-r3.py | 2341 | `5417c29da55039daeaec2aa637fc8985be6f39a8854f105eea06c73e4ad3a267` | `a95cc11427bc2c5b9c0bf6b4c3a86bfcf637f03d` |
| INSTRUCTIONS-V6-R3.txt | 1599 | `d4769418478cbd430d3a979a532aff84a8a097642473d8b564743257aa3507aa` | `2a106d7226b8fd967077939dc5460b90b2312c6c` |
| V6-R2-SIX-REVIEW-FINDINGS-DISPOSITION.md | 23652 | `ba3d048091edb78ccdb95bc0b416c89bedfcda13bdca2c9747c9baba1eb125dc` | `55b0efd6495d895534d2a24ed87ceea64f53a24a` |
| V6-R3-CLAUDE-GEMINI-INDEPENDENT-REVIEW-PROMPT.md | 3004 | `d9d2dcbac50f0727eb0389d1d92ae61527e5125347051643fab929b65383faae` | `4dc70adf36fdd7ac87332e6c3fb3d3278b27dd1c` |
| V6-R3-REVIEW-PROMPT-CURATOR-APPROVAL.md | 2014 | `9d415754dd866be9a4f4bdf588b00760721a43f2f1dbfd8ffd01e82ebf497326` | `f5bf1728eb051a5b6e852427125e3eab40b952d6` |

R2 historical reviewed SHA-256 was recorded as `cdfa88fd8918c59da6e7adcdaf046fcb6181804dcd65fb321b27b571fe9d0846`. Compare against the freshly computed R2 digest above; any mismatch must be resolved before claiming equivalence to the reviewed bytes.

**Outstanding provenance:** K1–K9 exact UTC decision times and the complete Claude V6-R1 S1–S10 original review-to-disposition trace remain unverified. R3 header date 2026-10-07 is not the creation date 2026-10-08. These are openly declared review issues, not silently corrected.

**Mechanical rebuild:** `python3 apply-v6-r3.py --r2 LOTUS-PROTOCOL-1.4-CANDIDATE-V6-R2.md --annex ANNEX-D-V6-R3-BUILD.md --output REBUILT-V6-R3.md --expected-sha256 7e30c4d8a8999e8c95563a4b635abb0c9d0d3181d84e006482a44d62834c2bbe`. Compare bytes to the supplied R3 candidate. This command is a reproducibility recipe, not a record of an executed independent Python test.
