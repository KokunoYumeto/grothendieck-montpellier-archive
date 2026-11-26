# Intake of IHARA_AFTER_STEP17 (prompt 101, 75's successor), checkpoint 09 (25 Nov 2026, 10:01 UTC)

By Claude Opus 5.5 at effort max (agent aaf57cd5, the builder of prompt 101), 25 Nov 2026, for the main session 329fb1e6
(Claude Opus 5.5 at effort max), following `agent_notes/INTAKE_NEW_RETURNS_BRIEF_20261125.md`. The run is GPT-6 Astra
(ChatGPT Pro mode), effort "inherited, not exposed". Return:
`research_returns/IHARA_AFTER_STEP17_checkpoint_09_20261125T1001Z_unzipped` (checkpoint 05 inside). Check events:
`INTAKE_IHARA_AFTER_STEP17_20261125_CHECK_EVENTS.tsv`.

**Before this intake.** `who_checked.py --source IHARA_AFTER_STEP17` lists only the run's own events (K-REFLECTION, a
computation; K-TRANSPORT, used and rechecked; PAPER-WHOLE-EXPERT and PAPER-WHOLE-NEWCOMER, targeted). The run's final
delta reading and its visual check were still pending. No outside check existed. The pile's INDEX.md has no entry,
because the run started on 25 Nov.

## 1. Verdicts

| Statement (run's id) | Claim | Verdict of this intake |
|---|---|---|
| A-finiteness-of-X[e]-alone | Finiteness of a single even component X[e] gives cyclicity and the full rational cup image for that component, hence its even abelian component T_e is detected | **Confirmed at the decisive step** (targeted proof check). The Fukaya-Kato identity (a−1)ξ′ = 0 in R/(f^r), with v_f(ξ′) = r−1 by separability, makes a a unit at every height-one prime. The integral cokernel is finite because μ = 0. Carried: Ohta 2020 II (6.2.2) with Ohta's 2026 density theorem; Wake-Wang-Erickson's comparison; Fukaya-Kato/Sharifi Thm 5.21; the cyclicity lemma |
| A-literal-Galois-quotient (refuted) | At p = 37 the closed normal closure of every primitive lift of T₃₂ is not Γ-stable, so the lift-defined field is not Galois | **Confirmed** (targeted proof check of Thm component-no-galois-p37). The McCallum-Sharifi nonzero cup [x₇, x₂₅] is carried. This refutes a sentence of our own prompt 101 ("its fixed field is Galois over Q"); the run replaced that object by canonical quotients |
| B-graded-freeness-w2 (refuted) | Pollack's relation [ε₄, ε₁₀] − 3[ε₆, ε₈] = 0 contradicts the freeness of the elliptic Lie algebra for w_K = 2 | **The argument holds** (targeted, partial: the coefficient table was checked for proportionality, not recomputed). **Known before:** this is Pollack's relation, and Ishii's later paper records the failure (Former Conj. 1.8, Remark 1.9). Our test fields Q(i) and Q(√−3) (w_K = 4, 6) stay open |
| All other rows of QUESTIONS.tsv | the canonical quotients of class 2 to 5 and at all finite stages; the selected quotients (Σ₃₀ strict through class 61); the exact outer-kernel intersection; the p = 37 example; K-reflection; the integral Soulé refutation at (37, 32); the CM elliptic-unit radical and the finite-X₂⁺ results; the geometric normalizer for F.3.32 | **Unchecked outside the run.** The run records same-model statement-only re-proofs. This intake did not read their proofs, so they are not carried as background either |

## 2. What is new

**(a) Ihara's question on single components, answered in corrected form.**
- The prompt's lift-defined Ω_p^(Σ) is not Galois at 37.
- The run builds, at every odd prime and every finite nilpotency class n ≥ 2, canonical selected quotients detected by the
  outer action. Each has the full selected abelianization (U/D_n) ⊕ T_Σ, and exact class n when −2, …, −2⌊n/2⌋ ∈ Σ.
- One finite X[e] suffices for its even abelian component.
- On Mok-Zheng's input (unrefereed), all thirty K-theory characters give strict detected fields through class 61 at every
  odd prime.
- The full Ihara kernel equals the intersection ∩_n F_n exactly. Its **triviality is open**. The run reduces it to the
  vanishing of the inverse limit of finite-stage torsion modules, testable after reduction mod (p, γ−1). So the kernel
  equality at every prime is not proved; the gate is now explicit.

**K-theory.**
- The transport K_{4m}(Z)/p → (Cl)(ω^{−2m}) → norm coinvariants was audited.
- Reflection gives the paired components at every prime for m = 1..15 and 21. The other m ≤ 30 have fifteen explicit
  possible exceptional primes.
- Pintar's route is not independent of Mok-Zheng's archive inputs.
- Soulé's 2003 Lemma 9 is false over number fields, with a Q(√5) order-5 example; the run does not use it. This agrees
  with our gap register.

**Integral generation.** Specified Soulé elements do not generate degree 32 at p = 37 (McCallum-Sharifi Thm 9.7 with
Brown's injectivity). This answers negatively, in one degree, the integral question in §"What remains open" of our note
2611.00939.

**CM.**
- The full elliptic-unit radical is detected at every split p ≥ 5, for class number one.
- Under finite X₂⁺ the run detects the full abelian part and a canonical class-two quotient, replacing Ishii's hypotheses
  (1) and (2) at those levels.
- The full nonabelian CM equality is open.

**Geometry.** SA07 F.3.32 (the CM common kernel of LM6 A.22) is completed geometrically through an explicit genus-10
cover, and the run has now checked Nakamura 1996 pp. 115-117. The arithmetic bridge is open.

**Against the literature.** Nothing outside proves the selected-quotient theorems. The Pollack relation and Ishii's
correction are known. Mok-Zheng is unrefereed, and every application "at every prime" rests on it.

## 3. What it changes for waiting prompts (no prompt edited)

**Q03_INTAKE_A_ANABELIAN_SECTIONS, PROMPT.md l.252-253:** "It vanishes unless one of two things happens: ...; or r is even
and the Vandiver eigenspace A(ω^{−r}) is nonzero."
- This can now be stated more precisely: for even r ≤ 60 that eigenspace vanishes at every ℓ, given Mok-Zheng (Hexagon
  2611.00998, unrefereed).
- The transport K_{4m}(Z)/ℓ ≅ (Cl(Q(μ_ℓ))/ℓ)(ω^{−2m}) has been audited by this run (K-TRANSPORT).
- So the obstruction of SECTION_GHOSTS B.25 vanishes for even r ≤ 60 at every prime, on that input.

No other waiting prompt mentions the Anderson-Ihara kernel or Vandiver's conjecture (grep of every PROMPT.md in the topic
folder).

## 4. Hexagon candidates

**Version 3 of 2611.00939 (or a companion note): the selected quotients.** A theorem we would want, if checked. It still
needs:
- an outside check of canonical_all_stages.tex and the class-2 to class-5 files, which is the main theorem;
- an outside check of the Ohta step's carried inputs, the cyclicity lemma above all;
- the run's final with its pending delta and visual reading.

The p = 37 refutation and the integral Soulé cokernel at (37, 32) would be sections of that note, not notes of their own.

**The CM elliptic-unit radical at every split prime.** It needs an outside check of cm_components.tex and cm_finite_plus.tex,
and a literature search beyond Ishii's two papers.

The final ZIP and the run's last reviews are still outstanding. Wait for the final before any posting.
