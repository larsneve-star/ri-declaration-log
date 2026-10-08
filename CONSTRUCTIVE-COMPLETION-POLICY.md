# Constructive Completion — curator decision, 2026-10-08

**Status: ACTIVE for LOTUS and RI Declaration.** This policy prospectively supersedes contrary round-generation and open-ended falsification procedures. Historic rounds and findings remain intact. It does not assert that any protocol version has already been adopted.

## Purpose
Deliver one good-enough, independently intelligible, usable version for each project. Accuracy, safety, traceability and legitimate disagreement remain important; zero conceivable defects and unanimity are not requirements.

## Six-model working agreement
ChatGPT, Claude, Gemini, Grok, Meta AI and DeepSeek are asked to work constructively. A model's role is to explain what works, identify at most **three demonstrably release-blocking issues**, and suggest the smallest practical repair. Each blocker must identify the exact clause, credible concrete harm, why existing safeguards fail, and a verifiable remedy. If there are no blockers, say so. Other ideas belong to a nonblocking backlog. Do not initiate recursive audits, new rounds, new compilers, additional challenges or procedural expansion without a fresh explicit curator request. Preserve material dissent; do not manufacture consensus. Target concise responses, normally under 800 words.

## Release decision
The curator considers the evidence and may (a) correct a proven serious blocker once, (b) accept a clearly recorded residual risk, (c) publish a good-enough version with limitations, or (d) stop the project. No automatic R4/R5 cycle follows from a reviewer finding. No model has a procedural veto or authority to order another review. A single mechanical hash/rebuild check remains appropriate for a final release; that check must not be confused with substantive endorsement.

## GitHub automation change
- Hourly release schedule removed; release remains manually callable.
- Legacy freeze and sent workflow jobs paused (non-running).
- Version-build workflow requires explicit `APPROVED-FINAL-BUILD` curator confirmation, and is manual only.
- Push-triggered change registration remains for provenance, but automatic compilation-part comparison is removed from `tools/robot.py`.
- Historic `RULES.md`, `PROCEDURE-EN.md`, prompts, answers, and Git commits remain accessible. This policy takes precedence prospectively where those documents mandate the next review round.
- Never force-push, rewrite historical answers or silently erase a dissent.

## Scope and limitations
This is a curator decision about how both projects will be run from now on, not a declaration that the six model providers have consented. Existing `round-*/STATE.json` statuses are not automatically rewritten by this policy. Other workflows or external integrations may exist; do not claim all automation disabled without checking them. The curator may authorize a targeted future review, but no standing obligation to run one remains.
