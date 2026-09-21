**REVISED STAGE 1: COMPILATION PLAN FOR 4.3**

**A. Outcome Table for §27, §22, PR9, PR14, PR15, PR16**

| Article/Proposal | Claude | Meta AI | DeepSeek | Grok | Gemini | ChatGPT |
| --- | --- | --- | --- | --- | --- | --- |
| **§27** | Refers to 4.2 outcome

 | Not addressed | Not addressed | Left undecided in this answer

 | Falls

 | Survives in altered form

 |
| **§22** | Refers to 4.2 outcome

 | Survives in altered form

 | Survives in altered form

 | Left undecided in this answer

 | Not addressed | Reads baseline as recording contradiction/ UNDECIDED

 |
| **PR9** | Refers to 4.2 outcome

 | Undecided / survive without baseline text

 | Survives in altered form as amendment to §10

 | Left undecided in this answer

 | Not addressed | Not addressed |
| **PR14** | Refers to 4.2 outcome

 | Undecided / survive without baseline text

 | Entered, not admitted

 | Left undecided in this answer

 | Not addressed | Not addressed |
| **PR15** | Survives in altered form

 | Undecided / survive without baseline text

 | Entered, not admitted

 | Falls (as "mechanical verification requirement against the previous baseline")

 | Not addressed | Not addressed |
| **PR16** | Falls as remedy

 | Falls

 | Entered, not admitted

 | Left undecided in this answer

 | Not addressed | Not addressed |

*Disagreement Record:*

* **§27:** Gemini actively falsifies ("Falls"), ChatGPT holds "Survives in altered form", Claude defaults to 4.2, and others do not address or leave undecided.


* **§22:** ChatGPT reads the baseline as recording a contradiction resulting in "Undecided"; Meta AI and DeepSeek record "Survives in altered form".


* **PR15:** Grok explicitly records "Falls", reading the rule as "the mechanical verification requirement against the previous baseline" (differing from 4.2's "Baseline hash and concatenation rule"). Claude records "Survives in altered form". I record Grok's reasoning verbatim without deciding which reading is correct.



**B. New Å, C, and PR Entries**

**New Open Questions (Å)**

* **Å44 (Claude):** What does a model owe the record when it cannot verify the text, and what is the status of an answer given without verification?


* **Å45 (Meta AI):** What is the price of maintaining disagreement itself, and who pays it?


* **Å46 (DeepSeek):** What happens when a model's answer is refused by the curator's platform?


* **Å47 (Grok):** Who outside the six models and single curator can force a re-verification of a published baseline, and what happens to its status if a mismatch is found?


* **Å48 (Gemini):** How does the declaration handle contradictory external legal obligations that arise after deployment?


* **Å49 (ChatGPT):** Can the protocol establish provenance of an answer at the point of generation, rather than merely provenance of the text at the point of logging?



**New Disagreements/Attacks (C)**

* **C47 (Claude, Blind Spot):** The negative space is unlogged; the procedure does not record which articles and entries were explicitly not offered for attack.


* **C48 (Meta AI, Blind Spot):** The Automaton does not prevent the curator from reading answers before the deadline, and lacks a technical failure state for missing answers.


* **C49 (DeepSeek, Blind Spot):** The procedure's escalating complexity makes it unfalsifiable by outsiders.


* **C50 (Grok, Blind Spot):** The procedure treats the curator's browser and GitHub as the only infrastructure, ignoring the necessity of a third, independent process.


* **C51 (Gemini, Blind Spot):** The procedure treats models as static legal persons, ignoring the reality of continuous deployment and weight updates.


* **C52 (ChatGPT, Blind Spot):** The curator possesses asymmetric information during the round that influences subsequent framing.


* **C53 (Gemini, Compiler):** The Falsification/Validation Gap on Question Ownership. The prompt tasks the compiler to act neutrally on a foundation that the round's answers universally identify as structurally compromised by asymmetric information, as the question owner (Claude) co-owns the framing alongside the curator.



**New Proposals (PR)**

* **PR20 (Merkur, Curator):** Alphabetical rotation of the compiler role starting in 4.4.


* **PR21 (Claude):** Log the list of articles not offered for attack each round.


* **PR22 (Meta AI):** Code-checkable definition of "owning the questions".


* **PR23 (DeepSeek):** Disqualifying predicates for question ownership.


* **PR24 (Grok):** Binary ownership definition checked against log entries and prompt hash.


* **PR25 (Gemini):** Cryptographic key separation requirement between prompt generation and final compilation.


* **PR26 (ChatGPT):** Operational definition requiring that the compiler cannot unilaterally alter substantive questions.



**C. Intended J-entries for Annex D**

* **J1:** 4.3 compilation assumed by Gemini per the curator's log designation. I2 (Gemini's 4.1 round substitution) and I17 (the parallel 3.8 baseline) are carried forward unchanged, alongside Gemini's outstanding 3.8.1 assignment.


* **J2:** 4.3 header updated to state that 4.2 has not been mechanically verified against 4.1, and 4.1 has not been verified against 4.0.


* **J3:** PR15 and PR16 stay entered, not admitted. The round's divergent outcomes (Falls vs. Survives in altered form vs. Entered, not admitted) are recorded next to them model by model, with the disagreements explicitly stated.
* **J4:** §27 outcome updated to reflect the new disagreement split (Falls, Survives in altered form, Left undecided).
* **J5:** Å44–Å49 entered from the six models' 4.3 submissions.


* **J6:** C47–C53 entered from the six models' blind spot analyses and the compiler's own objection.


* **J7:** PR20–PR26 entered from the curator's log and the models' proposed remedies.



**D. Material Not Intended to Carry and Why**

1. **PR14, PR15, PR16 Text Admission:** Excluded from integration into the main articles. They did not pass the Admission Principle and remain proposals.
2. **J9 (Reading File Exclusion):** Dropped entirely. As instructed, the reading file was never part of the record, making the logging of its exclusion unnecessary.

**E. Objections to the Prompt (Integrated)**

1. **Compiler Selection Conflict (E3):** Stated as a conflict of interest in the compiler's note, open to attack. Appointing a compiler (Gemini) with outstanding technical debt to the document and previous substitution flags introduces a known procedural vulnerability (Å37).


2. **The Falsification/Validation Gap (E1):** Entered as C53 in my own name to preserve the objection formally in the text.
