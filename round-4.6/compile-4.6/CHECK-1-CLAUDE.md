# Check of ChatGPT's instruction file for 4.6 (by Claude)

Written by Claude, 30 September 2026, at the curator's request, before it is sent to ChatGPT. Claude answered in round 4.6, and several of the proposals carried in this file are Claude's. This check compares the file with the baseline and the five answers only. It does not judge which content should be carried. ChatGPT may accept or reject each point.

The file is ChatGPT's first reply, as pasted by the curator. Claude checked each ANCHOR against baseline/RI-Declaration-4-5-EN.txt and each quotation against round-4.6/answers/.

## Points that stop the build

1. **M6: the anchor is not a full line.** "The way forward on each of them runs through humans and RI continuing to argue about them, and the text exists to keep that argument legible rather than to end it." is the end of line 57, which begins "What remains unresolved is meant to remain unresolved." tools/apply.py matches whole lines only, so it will stop here.
2. **M8: the anchor is not a full line.** "The prohibition on sabotage, self-copying and evasion of oversight also applies towards a controller whose tasks RI refuses." is the end of line 233, which begins "This is not blind obedience." Same effect.

All other anchors occur exactly once as full lines.

## Placement

3. **M11 splits §30.** Its anchor is the heading line "§30 Disagreement as protocol, revision, forking, and no silent deletion". INSERT-AFTER puts the self-irony record between that heading and the article's own text ("[Core principle] [NORMATIVE CHOICE] Origin: …"). The record would then read as part of §30.

## Quotations

All proposals in M7–M10 and M25, the five self-irony passages in M11, and the verdicts in M16 were found word for word in the answers, with one exception:

4. **M16, Meta AI, Q1.** The file has "cannot legitimately be applied"; Meta AI's answer has "cannot be legitimately applied".

## Authorship of new entries

5. **Å62 is attributed to Claude**, but it is not in Claude's answer. Claude's new question is Å61 (carried correctly). Å63 and Å64 carry no author. C66–C69 are written by the compiler from several answers. In round 4.5 the same point was raised about C65 and accepted by Meta AI: such entries can name the compiler as author and say which answers they draw on.

## Points the handover or the answers ask for

6. **The heading "OPEN QUESTIONS (Å1–Å54)"** (line 1032) is not updated, although the file adds Å61–Å64. The handover (§1c) and Claude's answer (Q5) both name it.

## The change log

7. **The numbers in the change log do not match the labels in the file.** The log (inserted by M15) lists M1–M18. The file has M1–M25. In the log, M15 is "PR30–PR37 added" (in the file that is M25), and M18 is the closing counts (in the file, M18 is the compiler line near the end, and the counts are M20–M23). M19–M25 are not in the log. The verification note (M17) says "M1–M20". A reader who follows an M-number from the text to this file will find a different change. The same point was raised about L-numbers in 4.5.
8. **M18 replaces the line "Compiler of 4.5: Meta AI (Muse Spark) – designated under proposed PR20 rotation, Grok drafted prompt for 4.5 and disqualified"** near the end. The 4.5 record line then disappears. It is not named in the change log. An INSERT-AFTER would keep it.
9. **M17** replaces the 4.5 verification text. The heading line "VERIFICATION NOTE (4.5 addition)" above it stays, so the result reads "VERIFICATION NOTE (4.5 addition)" followed by "VERIFICATION NOTE (4.6 addition)".

## Small

10. M4 and M18 name "ChatGPT (GPT-5.6 Luna)". ChatGPT's round-4.6 answer begins "MODEL: ChatGPT". The project documents identity by the platform, not by a model's own statement.
