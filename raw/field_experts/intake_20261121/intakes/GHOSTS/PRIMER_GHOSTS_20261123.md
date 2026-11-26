# Primer: the mathematics of GHOSTS, final (23 Nov 2026)

This primer is by agent ae4ae3dc (Claude Opus 5.5 at effort max), for the main session to read after a compaction. It
restates; it does not develop. Its source is the intake `intakes/GHOSTS/INTAKE_GHOSTS_20261121.md`, by the HODGE_SIGN
intake agent (Claude Opus 5.5 at effort high), together with the return's `QUESTIONS.tsv`.

**The run.** GHOSTS is prompt 39, "Hodge ghost classes at supersingular and ordinary primes", GPT-6 Astra (ChatGPT Pro
mode). It ran on 21 Nov from about 00:5x to 02:56 UTC.
- Final return: `grothendieck_archive_transcription_20261110/research_returns/GHOSTS_final_20261121T0256Z_unzipped/`.
- The paper is `GHOSTS.tex` (69 pp.) with 17 section files.
- This is the Hodge line, not the GT̂ tower line. The GT̂ tower run with "ghosts" in its name is SECTION_GHOSTS, whose
  route-2 gate (E.176-E.181) feeds the H17 note.

**Check labels**, from the intake:
- `[TPC]`: targeted proof check;
- `[COMP]`: computation rerun;
- `[PL]`: plausibility;
- `[stmt]`: statement level.

**Alpöge's theorem** (RH and GRH for Dirichlet L-functions, a theorem) enters only R30, for constants.

## 1. Sketch 2.5: bounded specialization and the ghost dichotomy (sections/bounded.tex)

**B01 `[TPC]`.** The cycles of bounded degree D and their classes form a finite union of projective schemes.
- The construction: FGA 221, Lemma 2.4 and Theorem 3.2 (Hilbert schemes); SGA 4½ *Cycle* 2.3.7-2.3.8 (relative cycle
  class).
- The condition "class = Δ" is open and closed, because Δ is a section of a lisse sheaf.

**B02, with B02a `[TPC]`.** For fixed N and D the following are equivalent:
1. integral numerator cycles exist in characteristic 0;
2. they exist at infinitely many places;
3. they exist at every place.
- Proof: the image of the projective locus is closed, a proper closed subset of the curve U is finite, then comparison.
- Integral numerators are necessary: t = h^r/2 on P^g is rationally algebraic but fails with N = 1.
- Precedent: Brünjes–Serpé, arXiv 0901.4853, Thm 3.4.

**B03, the ghost dichotomy `[TPC]`.**
- For an algebraic class, the local complexity c(v) is eventually constant (F_C is closed in U, and F_{C₀−1} is finite).
- For a non-algebraic class, c(v) → ∞ along every infinite set of places.

**B04 `[TPC]`.** Exactness at one prime outside an exceptional integer b_D (generic flatness, EGA IV₂ 6.9.1).
**B05 `[TPC]`.** Descent from C to Q̄.
**B06 `[TPC]`.** Bounded numerator degree bounds the multipliers: each component of H_D carries at most one N.

**Good for.** It makes the project's term exact. A non-algebraic Hodge class would be a ghost in the strict sense: it
passes at every prime, and its complexity escapes along every infinite set of primes. There is no third behaviour.

## 2. Task 4: the least complexity of the T5 Weil class on E⁴ (sections/local_weil.tex)

**P06 `[TPC]`.** The projector e_W = (9+S)(2−R−R²)/54.
- On Λ^aV_σ ⊗ Λ^{4−a}V_σ̄, S acts by 9(−1)^a and R by ω^{2−a}.

**P07 `[TPC, method]`.** 3w = PU − PV − QU − 2QV, a six-surface certificate.

**P08-P09 `[TPC]`.** c_θ(t_*) = 16 over C.
- The coordinate z(Γ_a) = ā², and z(t_*) = 2(1−ω), so |z| = 2√3.
- Cauchy–Schwarz on (2,0)-forms gives |z(V)| ≤ √(ab).
- deg V = 2(a+b+c), with c ≥ 2√(ab) by the surface Hodge index theorem.
- So degree ≤ 14 forces |z| ≤ √2.
- The minimum is attained by four graphs of degree 8, with N = 1. Also t_*² = 24.

**P13 `[TPC]`** (p > 3 rederived; p = 2, 3 read). The minimum is exactly 16 at every geometric good reduction, ordinary
and supersingular.
- The algebraic coordinate z replaces the period: z(Γ_h) = conj(det h_K).
- Degree budgets, plus the bound |det h_K|² ≤ deg h, decide it.

**P14 `[TPC]`.** At p = 5, h = [[2, j], [−j, 2]] with j² = −5 has z = 4 and degree 40. So the complex bound fails in
characteristic p, and P13 needs the low-degree classification.

**P12 `[TPC]`.** c(θ^k t_*) = 16k², and 8√3·M ≤ c(Mt_*) ≤ 16M.

**V01-V07 `[stmt]`.**
- The primitive half-class t₀ = t_*/2 also has minimum 16.
- V07: the integral Weil lattice is Zt₀ ⊕ ZRt₀, with Gram matrix [[6,−3],[−3,6]] and determinant 27.

**W01-W04 `[stmt]` + `[COMP]`.** The complex minimum of w = e_W[Γ₁] is 24. The W04 program reruns with PASS.

**Good for.** The prompt asked for "least complexity as a function of v". The answer is that it is constant (16) on
E⁴. It depends on normalization and polarization, not on the prime (P12, V04).
- P02: p ≡ 1 mod 3 is ordinary and p ≡ 2 mod 3 supersingular, on the E⁴ isogeny class.
- P03 refutes extending that to the whole family.

## 3. Task 5: uniform bounded division (sections/family_checked.tex)

**R10 `[TPC]`.** Bounded detection gives an integral Weil basis.
- u = [18Z + 2S^*Z] − [9R^*Z + 9R^{2*}Z + (SR)^*Z + (SR²)^*Z].
- Comass gives d ≤ 729·D₀², and the Gram matrix is d·[[1, −½], [−½, 1]].

**R11 `[TPC]`.** The extraction cost is C₄ = 531441·δ·D₀⁴·(1 + 4⌈√T⌉), by Cramer with Δ = 3d²/4.

**R12 `[TPC]`, given Schoen's dominance** (Compositio 65 (1988) §3, pp. 26-30; Addendum, Compositio 114 (1998) p. 330).
An explicit detecting degree D₀ = 132,269,760 on the principal Eisenstein Q(ω) Weil fourfold component.
- The Prym B of a cyclic triple cover C → X, genus 7 over genus 3, has type (1,1,3,3) and L⁴ = 216.
- deg W₄(C) = 68040 and deg T₀ = 17496. Bézout (Fulton Ex. 8.4.6) gives 68040·17496/9.
- Descent to a principal polarization; the lattice is U ⊕ U.

**R20-R24 `[stmt]`.** Every fixed polarization and determinant, through a principal sixfold, with
D₆ = 57,854,793,024,000.

**R30 `[PL]`.** Under Dirichlet GRH mod 3 (Alpöge) with Lee's constants, some prime p ≡ a mod 3 with p ∤ b satisfies
p ≤ max(e¹⁴, 4 log b + 4). Unconditional PNT-in-progressions constants give the same shape. GRH is inessential.

**R31 `[TPC]`.** The unconditional product-of-primes certificate.

**R40-R45 `[stmt]`.** A terminating algorithm for the whole good-prime function of a known class.

**Good for.** Bounded division on the principal Q(ω) Weil fourfold component, with an explicit integer, from published
inputs. This removes HECKE_DIV M10's dependence on Markman's preprint for that component.

## 4. Tasks 2-3: Remark 8.5 and T9 (sections/source_audit.tex, framework_map.tex)

- **C01 `[stmt]`, conditional on 032.** Remark 8.5 is a deduction with CM transport. The auxiliary CM variety may have
  dimension n·dim A.
- **C02 `[stmt]`.** Refutes sketch 2.6's reading "a CM point of the same special subvariety". The source (p. 33)
  disclaims it.
- **C03-C06 `[stmt]`.** Degree and denominator charges. Transport data are not canonical in p (C06: growth is an
  artefact of the chosen transport).
- **C07 `[stmt]`, conditional on 032.** At ordinary primes, algebraic classes lift to the canonical Serre–Tate lift.
- **C18 `[TPC]`.** T9 made exact: the transport cost on E⁴ is constant, (1,16,16) for t_* and (2,16,16) for t₀, at every
  prime.
- **C15 `[TPC]`.** Milne's report (hexagon 2611.00244, §3.6) omits the sign (−1)^r of the primitive form: a primitive
  divisor on E×E has negative square, (F₁ − F₂)² = −2. To be reported to Milne.
- **C16 `[stmt]`.** van Hoften–Sempliner Th. 4.0.2 gives no numerical bounds.

## 5. Open rows and gates

`QUESTIONS.tsv` has 21 rows, all proved or refuted (Q1-Q7 with their sub-rows). Nothing is left open in the run.

The intake's gates:
- the p = 2, 3 cases of P13 checked independently;
- a literature search for B03's exact eventual constancy;
- C01 and C07 stay conditional on 032.

## 6. Where the results went

- **Hexagon board row H12.** "Bounded division for Weil classes (HD-U) for every imaginary quadratic K and every n,
  with explicit constants; the ghost-class dichotomy". Stage M, moving. Its gates: a literature search and the finished
  text.
- **Hodge bridge sketch** (`reports_20261120/hodge_bridge/HODGE_BRIDGE_SKETCH_20261121.md`). The intake lists edits at
  2.5 (integral numerators; B03), 2.6 (C02), T5 (R10-R12, R20-R24), T9 (C18), "Where GRH enters" (R30) and Route 5
  (C07).
- **HECKE_DIV.** M10's principal component is now unconditional through R12. P6 is the same principle as B06.
- **The next attack** (intake §5): a Hodge class not yet known to be algebraic, on a simple non-CM abelian variety of
  dimension ≥ 6 with exceptional classes. Bound c(v) at ordinary primes through C07-type canonical lifts.
- **Grothendieck's texts.**
  - Cote 14, scans 044-047 (letter to Serre, 27.8.65): C^i is taken modulo algebraic equivalence; GHOSTS works modulo
    homological equivalence.
  - Cote 16, scans 048-049: R11 is the integral, effective form of the Cayley–Hamilton inverse.
- **Outside correction:** the sign (C15) in Milne's report.
