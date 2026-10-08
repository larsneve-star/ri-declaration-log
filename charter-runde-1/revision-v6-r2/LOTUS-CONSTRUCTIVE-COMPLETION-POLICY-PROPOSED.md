# LOTUS — Constructive Completion Policy (curator-directed proposal)

Date: 2026-10-08
Status: PROPOSED IMPLEMENTATION OF CURATOR'S NEW DIRECTION; NOT YET AN ADOPTED AMENDMENT TO MAIN-BRANCH RULES.

## Objective
Produce one good-enough, independently intelligible and usable LOTUS V6-R3-based protocol. No unbounded falsification or self-perpetuating revision cycles. Preserve genuine disagreement without treating every disagreement as a defect.

## Six-model working contract
All six participants (ChatGPT, Claude, Gemini, Grok, Meta AI and DeepSeek) work constructively:
1. State what works and what should remain unchanged.
2. Report at most three release-blocking findings, each with exact quotation, plausible concrete harm, a demonstrated failure of existing protections and the smallest sufficient repair. If none, explicitly say NONE.
3. Classify other suggestions as nonblocking backlog; no extra rounds or automatic repairs.
4. Offer one implementable improvement only where it materially improves safety, clarity or usability.
5. Preserve disagreements. Consensus is neither required nor evidence of correctness.
6. Do not initiate new prompts, audits, compilers, review chains or token-intensive ancillary reports without a fresh explicit curator instruction.
7. Do not manufacture defects, assume bad faith by another model or describe speculative vulnerabilities as demonstrated.
8. Keep each response short (target 800 words, unless curator requests more).

## Release decision
The human curator decides after a single consolidated assessment. A blocking defect requires a credible serious consequence and evidence that the current text fails to prevent it. The curator may fix a confirmed blocker once, accept a documented residual risk, or decline publication. Ordinary imperfections do not block a usable version.

## GitHub motor changes proposed — NOT YET APPLIED
- Disable scheduled `.github/workflows/robot-release.yml` (hourly cron).
- Disable manual new-round workflows `robot-freeze.yml` and `robot-sent.yml` during completion.
- Simplify `robot-register.yml` to an append-only history register without automatic compiler-part comparisons or feedback loops.
- Restrict `robot-build.yml` to curator-authorized one-time final builds; no automated next-round trigger.
- Remove the mandatory Phase 8 recurrence from `PROCEDURE-EN.md` for LOTUS completion; preserve the original as historical record and explicitly record the replacement decision.
- Keep hashes, source files, original answers and immutable history. No force-push, rewriting or silent deletion.

## Important scope boundary
The repository also holds RI Declaration rounds. Do not change main-branch workflows or standing RI rules without explicitly deciding whether this new policy governs LOTUS only or both projects. No automation or branch protection has been changed by this proposal.
