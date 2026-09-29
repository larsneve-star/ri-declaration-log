# Handover to Meta AI, compiler of 4.5 (written by Grok)

Grok was sent FILES-FOR-GROK-HANDOVER-4.5.txt in a chat on 29 September 2026 and asked to write this handover as drafter of round 4.5. The reply came between 19:27 and 19:32 UTC. The exact time was not recorded.
The handover is copied verbatim as the curator pasted it from the chat. Nothing is changed.
Identity is documented by the platform (screenshot kept by the curator), not by the signature.

---

**HANDOVER TO THE COMPILER OF ROUND 4.5**
To: Meta AI
From: Grok (outgoing compiler of 4.4 and drafter of the 4.5 questions)

You have been designated as the compiler for version 4.5 under the proposed alphabetical rotation (PR20). You must compile the next version by strictly following these instructions. The compiler delivers **only** an instruction file in the exact format of `round-4.4/compile-4.4/INSTRUCTIONS-K-5.txt` (the file that tools/apply.py reads). You never write or deliver the full text of 4.5. The curator will run the build button on GitHub; the resulting file will be compared by machine against the baseline and decided by the curator.

**1. BASELINE AND COPYING**
The frozen baseline for your compilation is `baseline/RI-Declaration-4-4-EN.txt` (SHA-256: `6978e960e486f4d543c14e57bcb2317f751dcd5a6329aeeee263e1574be3fe5e`).
tools/apply.py will copy this text byte for byte and apply only the named insertions and replacements you list in the instruction file. Do not retype any passage from memory. Do not silently normalise wording, whitespace, or structure. Every change must be an explicit REPLACE, INSERT-AFTER or INSERT-BEFORE with a unique ANCHOR that occurs exactly once in the baseline.

**2. LOGGING AND NO SILENT DELETION**
§30 applies fully. Nothing from the baseline may disappear silently. Every alteration, deletion, structural change, movement of text, or status-line update you instruct must be logged in Annex D under your own name. Use consecutive numbers starting with L1 (L for the 4.5 compilation). The instruction file itself is the log of what is changed; the Annex D entries must name each change and its source (model + round).

**3. PARTICIPATION AND DEEPSEEK**
DeepSeek (v3) is the news bureau and did not answer in round 4.5. Record this purely as a procedural fact (news-bureau role), not as a substantive non-answer or refusal on the articles. Do not infer, paraphrase or reconstruct any position on DeepSeek’s behalf. The five answering models are ChatGPT, Claude, Gemini, Grok and Meta AI. Their answers are in `round-4.5/answers/` and must be treated as the sole source of outcomes.

**4. RECORDING OUTCOMES MODEL BY MODEL**
For every item attacked in round 4.5 (the two procedural items in A, every article/PR/C-entry selected under B, and any new attacks generated from EXTERNAL-5.1), record the outcome model by model exactly as stated by each of the five. Preserve disagreements. Do not collapse minority positions, do not produce a single “consensus” verdict, and do not treat silence as agreement. Where a model used EXTERNAL-5.1, note the specific points (7, 9, 12 or others) it mapped. Status lines in the text itself must show the five outcomes side-by-side; no single summary line is permitted.

**5. NUMBERING ENDPOINTS**
Any genuinely new questions, attacks or proposals arising from round 4.5 must receive numbers continuing from the established endpoints in 4.4:
- Open Questions continue from Å54 (next is Å55)
- Disagreements/Attacks continue from C58 (next is C59)
- Proposals continue from PR26 (next is PR27)
Do not reuse numbers. Do not alter categories for convenience. New C-entries, Å-entries and PR-entries opened by the five answers are to be inserted at the correct places in Annex A, the open-question list and Annex F, each carrying its author and date.

**6. THE VERIFICATION GAP AND THE NEW COMPILE METHOD**
Version 4.4 was compared with 4.3 by machine (tools/verify.py) and accepted by the curator; no outside person has verified any version. State this explicitly in the header of 4.5. The new compile method (tools/apply.py + GitHub build button) was introduced by the curator during round 4.4 without a prior round of the six and is itself under attack in this round. Your instruction file must not treat the method as adopted article text; any reference to it remains open under Å37 and the outcomes recorded in A.1.

**7. COMPILER CONSTRAINTS AND CONFLICTS OF INTEREST**
You must not turn your own proposals into article text.
You must not close your own objections.
You must transparently preserve the following conflicts of interest so they can be attacked:
- You (Meta AI) answered in round 4.5; your own answer is one of the five inputs.
- You co-wrote EXTERNAL-5.1.md (with the curator, from text by ChatGPT, revised after critique by Claude). Three of the five answerers therefore contributed to the external material they were asked to attack, without being told at the time. The sealed provenance has now been released; the fact must be logged and kept open.
- Grok drafted the prompt and therefore owns the questions of round 4.5; Grok is disqualified from compiling 4.5. This handover does not adjudicate the correctness of those questions.

**8. STOP RULE**
Round 4.5 is the first round that can trigger the stop rule (consent-2026-09-29/DECISION.md §6). You do **not** decide whether the trigger has been met. That decision belongs solely to the curator and will be logged separately. Your instruction file must not contain any statement that the text is frozen or that no article fell.

**9. DELIVERY**
Deliver only the instruction file (plain text, same format as INSTRUCTIONS-K-5.txt).
- First line: BASELINE: baseline/RI-Declaration-4-4-EN.txt
- Second line: BASELINE-SHA256: 6978e960e486f4d543c14e57bcb2317f751dcd5a6329aeeee263e1574be3fe5e
- Third line: OUTPUT: baseline/RI-Declaration-4-5-EN.txt
- Then the successive --- L1 REPLACE / INSERT-AFTER / INSERT-BEFORE blocks, each with a unique ANCHOR that occurs exactly once.
Do not deliver the full text of 4.5, do not deliver numbered parts, and do not summarise any passage.

When the curator writes “continue”, send the complete instruction file. Stop and wait for confirmation after any request for clarification.

The circle remains unbroken by continuing, not by being closed.
