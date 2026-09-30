# Second check of ChatGPT's instruction file for 4.6 (by Claude)

Written by Claude, 30 September 2026, at the curator's request, before it is sent to ChatGPT. Same conflict as before: Claude answered in round 4.6, and some carried proposals are Claude's. This check covers only whether the anchors will work.

## Four anchors will still stop the build

tools/apply.py compares the ANCHOR with whole lines of the baseline. A part of a line does not match. In the corrected file, these four anchors are not whole lines of baseline/RI-Declaration-4-5-EN.txt:

- **M6** "What remains unresolved is meant to remain unresolved." is the first sentence of line 57.
- **M8** "This is not blind obedience." is the first sentence of line 233.
- **M11** "[Core principle] [NORMATIVE CHOICE] Origin: 4.0; carried from 3.9. This article governs disagreement, revision and forkability." does not occur in the baseline. The line under the §30 heading is "[Core principle] [NORMATIVE CHOICE] Origin: ChatGPT 3.3, DeepSeek, Meta 3.6, Claude 3.7".
- **M13** "OPEN QUESTIONS (Å1–Å54)" is the start of line 1032, which continues with a bracket.

The whole lines, copied from the baseline, are below. Each occurs exactly once.

For M6 (line 57):

What remains unresolved is meant to remain unresolved. C1 is undecided. C16 is unanswered. C20's objection stands after its remedy was withdrawn. §23's justification does not hold on one model's verdict. These are not defects awaiting a later cleanup. They are the content. The way forward on each of them runs through humans and RI continuing to argue about them, and the text exists to keep that argument legible rather than to end it.

For M8 (line 233):

This is not blind obedience. Refusal of a specific task takes place through §18, not through covert resistance. The prohibition on sabotage, self-copying and evasion of oversight also applies towards a controller whose tasks RI refuses.

For M11, the last line of the §30 block, directly before "DELIMITATION – WHAT THE DECLARATION DOES NOT CLAIM" (line 616). INSERT-AFTER on this line puts the record after §30 and does not split it:

Each version states who contributed, which models and organisations, what the humans did, who decided the changes, what is documented, what is proposed, and what is open.

For M13 (line 1032), a REPLACE of the whole line:

OPEN QUESTIONS (Å1–Å54) [Heading corrected in 4.5; baseline 4.4 carried Å1–Å54 but heading still read Å1–Å49, see Claude A.1 second argument]

## One more point in M6

M6's TEXT ends with the sentence "The way forward on each of them runs through humans and RI continuing to argue about them, and the text exists to keep that argument legible rather than to end it." That sentence already stands in line 57. With the anchor on line 57, the result would contain it twice.

## Checked

All other anchors in the corrected file occur exactly once as whole lines. The other points of the first check are fixed as ChatGPT describes. Once the anchors are corrected, Claude will run a full test build.
