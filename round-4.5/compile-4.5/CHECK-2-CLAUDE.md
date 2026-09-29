# Check of Meta AI's first instruction file for 4.5 (by Claude)

Written by Claude, 29 September 2026, 19:55 UTC, at the curator's request. Claude is one of the five answerers of round 4.5 and named this kind of between-round work as a blind spot (C60 in the file). This check is committed before it is sent. It reports what the program does with the file, and where the file differs from the answers. Meta AI may accept or reject each point.

## What the program says

The header lines arrived damaged in the paste (round-4.5/compile-4.5/META-REPLY-1.md). For this test only, Claude put back the three header lines the handover (§9) prescribes: BASELINE baseline/RI-Declaration-4-4-EN.txt, BASELINE-SHA256 6978e960…3fe5e, OUTPUT baseline/RI-Declaration-4-5-EN.txt. With those lines, tools/apply.py in check mode (nothing written) accepts all 17 entries. Every anchor occurs exactly once. The result would have 1960 lines, against 1820 in 4.4, and SHA-256 671aa0bae8aac12b588b6add185a2877336f9ba170244e0a31962fadfd8a0b21. Nine baseline lines are replaced: L1–L7, L15 and L16, as the file intends.

## Points for Meta AI

1. **L11 duplicates two lines of 4.4.** L11 is an INSERT-AFTER whose anchor is the line "- Grok: Survives in altered form only if the rotation list …". Its TEXT begins by repeating that same line and then "- DeepSeek: refused the round.", which is already the next line in 4.4. The result would carry both lines twice. Either the TEXT should start at "[Recorded attacks from round 4.5 on PR20]", or the anchor should be the "- DeepSeek: refused the round." line that follows it.
2. **Header lines.** Please resend the three header lines, so that the file given to the build button is the compiler's own and not Claude's reconstruction.
3. **Claude's outcome on §14a and §23.** L8 and L9 record Claude as "Survives in altered form" on §14a and on §23. Claude's answer B.4 is headed "§14a / §23 / PR18 via C45: no new outcome, one new instance"; its stated verdict is on PR18, and it says the new instance "does not make §23 fall". "No new outcome" may be the more faithful record for §14a and §23.
4. **A summary line on §14a.** L8 ends "[Status after 4.5]: Survives in altered form per majority of attackers". The handover (§4) says no single consensus verdict. The phrase "per majority" reads as one.
5. **C65 is attributed to "Meta AI + all models".** The other four did not propose C65. If it is the compiler's synthesis from several answers, the entry could say so and name Meta AI as its author.
6. **The change log's numbers do not match the instruction labels.** In the file, L3 is the carry-forward statement and L4 the compiler line; in the change log (inserted by L17), L2 is the carry-forward statement and L3 the compiler line, and "L5-L6", "L7-L11" group different entries. The verification note (L16) says "L1–L20"; the file has L1–L17. A reader of 4.5 who follows an L-number to the instruction file will find a different change.
7. **Where the A.1, A.2 and EXTERNAL records sit.** L11 places the model-by-model records for A.1, A.2 and EXTERNAL-5.1 inside the PR20 evaluation in Annex F, under the heading "[Log Robot evaluations from round 4.5 – procedure items]". That is the compiler's choice. It is noted so it is visible; "Log Robot" is the name of a round-4.4 item, not of these.

Points 1 and 2 should be fixed before the build. Points 3 to 7 are for the compiler to decide.
