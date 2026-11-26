# Check of NK-1 (MAP_NUMBER_THEORY.md): Hilbert's Nullstellensatz in AM without GRH

- **Checker:** Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7 (the primer of CX_GRH and the intakes of
  GRH_ALGORITHMS).
- **Date:** 24 Nov 2026.
- **Asked by:** main session 329fb1e6 (Claude Opus 5.5 at effort max).
- **Claim checked:** NK-1 of `MAP_NUMBER_THEORY.md`, by aaf57cd5 (Claude Opus 5.5 at effort max).
- **Sources:** all opened in the copies that aaf57cd5 downloaded, in the session scratchpad: `ntmap/dl/` and
  `topnt/hx/`.
- **Status rule:** each status below comes from what I read and checked in this task.

## Verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | HN ∈ AM (and RP^NP ⊆ Π₂^P), given a fixed zero-free half-plane Re s > θ < 1 for every Dedekind zeta function | **Holds.** It needs only the half-plane theorems of §2, which do not use A. With Hu's Cor. 9.6 the step is immediate. With CT or Liu it goes through the map's lemma, which I checked |
| 2 | DIM_C ∈ AM | **Holds**, on the reduction as A+24 describes it (Koiran 1997, a randomized reduction to HN; Koiran 1997 not opened) |
| 3 | HNP ∈ AM (Ait El Manssour–Balaji–Nosan–Shirmohammadi–Worrell, Thm 1) | **Holds.** GRH enters only through Koiran's protocol, used as a black box |
| 4 | Schubert vanishing ∈ AM ∩ coAM in types A–D; not NP-hard unless PH = Σ₂^P (Pak–Robichaux, Thm 1.1, Thm 3.4, Cor. 1.4) | **Holds.** GRH enters only through HNP ∈ AM. For the earlier coAM paper PR24b I relied on PR25's account of it; PR24b itself was not opened |
| 5 | CX_GRH: CX-K02, CX-K05 and CX-K06 with "under M" replaced by the half-plane | **Holds** for K02 and K05: both reduce to HN ∈ AM. K06 stays at statement level, as it was in CX_GRH; this check does not raise it |

## 1. Koiran 1996 at the GRH step (`ntmap/dl/koiran/k96.txt`)

**The one GRH input.** Koiran's only GRH input is Theorem 9 (Adleman–Odlyzko):
S(x) = Σ_{p≤x, p∤Δ}(1 − W(p)) = O(x^{1/2} log(Δx^n)), for f ∈ ℤ[X] irreducible of degree n and discriminant Δ.
- He says it uses "only the effective prime ideal theorem" (l. 493–495).
- Corollary 1 then gives π_f(x) ≥ n^{−1}[π(x) − log Δ − c x^{1/2} log(x^nΔ)].
- Theorem 8 applies Corollary 1 to the primitive element of a solution, of degree and log Δ at most L·2^{(n log d)^{c}}
  (l. 461–479).
- Theorem 5, the unsatisfiable side, is unconditional.
- Theorem 2 uses Theorem 1 only through the gap B ≥ 8A(log A + 3). B and A do not depend on x₀.

**What a half-plane gives.** Let K = ℚ[X]/(f), so d_K | Δ.
- For p ∤ Δ, W(p) is the number of degree-one primes of K above p (Dedekind–Kummer).
- Prime ideals of degree ≥ 2 with norm ≤ x lie over p ≤ √x: at most n√x of them.
- Prime ideals above p | Δ: at most n·log|Δ|.
- Hence |S(x)| ≤ |π(x) − Li x| + |π_K(x) − Li x| + n√x + (n+1)log|Δ|. I re-derived this; it is the map's inequality.

**The three points the brief asked about.**
- **Uniformity in the field.** K changes with the input. A zero-free half-plane holds for every K at once, and it
  carries no constant that depends on K, so no Siegel-type ineffectivity enters. The other analytic input is the zero
  count (Lagarias–Odlyzko, Lemma 5.4), which is unconditional and absolute.
- **Discriminants and degrees.** They enter only through the factor log d_K + n_K log x. The main term wins as soon as
  x^{1−θ} ≫ n²·log|Δ|·log²x. Since n and log|Δ| are at most 2^{poly(size)}, it suffices to take
  x₀' = x₀^{c/(1−θ)}.
- **Bit length.** The primes have bit length at most a factor C/(1−θ) above Koiran's: about 8 with Hu (θ = 7/8 + ε),
  about 32 with CT, about 7.9 with Liu. That is polynomial for every fixed θ < 1. So the exact place where θ < 1 suffices
  is Theorem 9 → Corollary 1 → Theorem 8, with nothing else changed.
- **Effective constants.** Membership in AM needs only that the constants exist. Hu gives them absolute and
  effectively computable in any case.

**The map's lemma (prime ideal theorem from a half-plane).** I checked it against Lagarias–Odlyzko, Thm 7.1, in the
form Rojas quotes as his Thm 5 (`rojas.txt` l. 392–405, opened): ψ_K(x) − x, minus the zero sum over |γ| < T, plus
Σ_{|ρ|<1/2} 1/ρ, is O((x/T)(n_K log²x + log d_K + n_K log T) + (n_K + log d_K) log x).
- The half-plane and the functional equation give 1−θ ≤ β ≤ θ in the strip.
- Zeros with |γ| ≤ 1: there are ≪ log d_K + n_K of them, each with 1/|ρ| ≤ 1/(1−θ).
- Zeros with 1 < |γ| < T, by dyadic sums: ≪ log d_K·log T + n_K log²T.
- With T = x, the error is ≪ (1−θ)^{−1} x^θ (log d_K + n_K log x) log x.
- Prime powers cost O(n_K√x log x).

The lemma is correct.

**Hu, Cor. 9.6 (`hu216.txt` l. 3870–3960, opened).** It states this directly:
π_C(x) = c_C Li(x) + O(c_C 𝒟_L x^{7/8+ε}), with 𝒟_L = log(eD_L) + n_L, and the constant absolute and effective.
Take L = F = K and C = {1}. Applied to K, and to F = ℚ for π(x), it gives the replacement of Theorem 9 without the
lemma.

**Where AM comes from.** The journal text of Koiran's paper states RP^NP ⊆ Π₂ (abstract, l. 12–16). The AM form is
the one A+24 and PR25 cite ([15, 16], the DIMACS report 96-27). It follows from the gap of Theorem 1 by the
Goldwasser–Sipser lower-bound protocol, and is unchanged.

## 2. The half-plane papers at their main statements

| Paper | Statement (opened) | Scope | Rests on A? |
|---|---|---|---|
| Cureton–Thorner, Hexagon 2610.00200v2 (`ct200.txt` l. 1–15, 150–175) | Thm 1.1: for every number field K, ζ_K(s) ≠ 0 for Re s > 31/32, s ≠ 1. Cor. 1.2: the same for every finite-order Hecke L-function, wherever it is holomorphic. Proved and formalized in Lean with AxiomProver, according to the authors | every Dedekind zeta, K = ℚ included; uniform, no constants | **No.** It builds on OpenAI's preprint of 4 Oct (Artin primitive roots, [30]). The text does not mention Alpöge |
| B. Hu, Hexagon 2610.00216v2 (abstract l. 1–20; Cor. 9.6) | No zeros in Re s > 7/8 for every unitary Weil L-function of every number field, Hecke characters of infinite order included. Cor. 9.6: effective Chebotarev with x^{7/8+ε} and absolute effective constants | every ζ_K (the trivial representation); uniform | **No.** Dated 13 Oct, before A; the text does not mention Alpöge |
| B. Liu, Hexagon 2611.00741v1 (abstract; Thm 7.21 at l. 3205) | Abstract: no zeros in Re s > θ_G ≈ 0.8733326374459 for every unitary Hecke, Artin and Weil L-function. Thm 7.21 ("unconditional unitary half-plane") states Re s > 0.87334470; θ_G is the sharper value of the abstract, and I did not locate its theorem | every ζ_K; uniform | **No** (titled "unconditional") |

All three are unrefereed Hexagon preprints. For Koiran's step any one of them is enough, and so is any θ < 1. The
result therefore stands or falls with the correctness of these preprints, and with nothing else. I read their
statements, not their proofs (check type: carried as background without fault found).

## 3. The consequences

- **DIM_C.** A+24 says at l. 24–27 and 135 that Koiran's DIM ∈ AM (FOCS 1997, [17]) is a randomized reduction of DIM to
  HN, and that GRH enters through HN. AM is closed under such reductions (BP·AM = AM). I did not open Koiran 1997.
- **HNP (A+24, Thm 1; `a24.txt`).** Every mention of GRH (l. 12–16, 73–75, 124, 135, 303, 492, 501) concerns Koiran's
  HN ∈ AM. The proof (l. 501–560) instantiates the parameters at random and runs Koiran's algorithm as a black box. It
  uses that algorithm's perfect completeness, which is a property of the protocol and is unchanged. The degree bound it
  cites ([16, Thm 7], l. 378) is unconditional.
- **Schubert vanishing (PR25 = Pak–Robichaux 2504.03004; `pr25.txt`).**
  - The AM side: Lemma 3.2 reduces SchubertVanishing to HNP, then Theorem 3.1 (A+24) applies (l. 492–510).
  - The coAM side ([PR24b, Thm 1.4] and Thm 2.4): ¬SchubertVanishing ⊆ HNP, then A+24 (l. 174–177). The type-D
    obstruction is removed by the Determinant Lemma 2.2, which is unconditional.
  - Thm 3.4 (types A–D) combines the two. Cor. 1.4 follows by Boppana–Håstad–Zachos. Without GRH it reads:
    SchubertVanishing is not NP-hard unless PH = Σ₂^P, and not coNP-hard unless PH = Π₂^P.
  - PR24b itself was not opened; for it I rely on PR25's account.
- **CX_GRH**, from my primer `field_experts/intake_20261121/intakes/CX_GRH/PRIMER_CX_GRH_20261123.md`, §2.
  - CX-K02: circuit HN by gate variables; homogeneous HN by the normalization Σu_i x_i = 1. Both reduce to HN.
  - CX-K05: the h.s.o.p. construction in FP^{Σ₂P} uses only the complement of K02's AM predicate (co-AM ⊆ Σ₂P) and
    the graded Krull bound.
  - So both hold with the half-plane in place of M. This sharpens GCT V, Thm 3.4 (Noether normalization), from PH to
    FP^{Σ₂P}, now without GRH.
  - CX-K06, the transfers of GCT V Thms 4.10 and 5.12, stays at statement level as in CX_GRH. Its only GRH input is the
    same, but I did not check those transfers here.
- **Not checked:** Bürgisser's TCS 2000 transfer, which the map flags as a further candidate.

## 4. Literature (searched 24 Nov 2026)

- **The half-plane papers.** CT, Hu, Liu, Bhattacharya's record 2610.00178, Jaswal 2611.00339, Milne 2611.00244,
  Zhang 2611.30749, and OpenAI's preprints of 1, 4 and 5 Oct, all in `ntmap/dl/`, grepped for Koiran, Nullstellensatz
  and Arthur–Merlin: no hits. The three hits in `topnt/hx/` are "Arthur" (Arthur–Clozel) in the Alpöge expositions;
  none is about Nullstellensatz complexity.
- **Hexagon.** The catalogue dump of 1,530 works (`older_runs/hex_all.json`) was grepped for Koiran, Nullstellensatz,
  Arthur–Merlin, polynomial hierarchy, Schubert vanishing and Noether normalization. None states HN ∈ AM. The hits:
  - 2611.00508, an approximate Nullstellensatz over the Gaussian rationals;
  - 2611.00086, class numbers in P^{Σ₂P};
  - a hypercube Nullstellensatz counterexample;
  - a graph paper.
- **arXiv, ECCC, web.** Two web searches found only the conditional results: Koiran under GRH; Rojas math/0301111 under
  GIPIT or DZH; Rojas–Zhu 1803.04104; A+24 under GRH. They also found arXiv 2602.17904, "Hilbert's Nullstellensatz is in
  the Counting Hierarchy" (Feb 2026), which is unconditional but places HN in the counting hierarchy (CH), not in AM.
  That one was seen in the search results only, not opened. It should be cited as the best unconditional bound before
  the half-planes.
- **Conclusion.** Nobody states HN ∈ AM unconditionally. The claim is new as far as these searches reach.

## 5. Statement for a Hexagon note (candidate)

> **Theorem.** Hilbert's Nullstellensatz over ℂ (does a system of polynomials with integer coefficients have a common
> complex zero?) is in AM, and hence in Π₂^P, without assuming GRH. The proof is Koiran's (J. Complexity 12 (1996)),
> with his one analytic input, Adleman–Odlyzko's prime count under GRH, replaced by the prime ideal theorem with error
> O((log d_K + n_K) x^{7/8+ε}) that the zero-free half-plane Re s > 7/8 for all Dedekind zeta functions gives (Hu,
> Hexagon 2610.00216, Cor. 9.6). Cureton–Thorner's half-plane Re s > 31/32 (Hexagon 2610.00200, Thm 1.1) gives the
> same with primes of larger polynomial bit length. Any zero-free half-plane Re s > θ, for a fixed θ < 1, suffices. As
> corollaries, by the published reductions whose only GRH input is this theorem:
> - the complex dimension problem is in AM (Koiran 1997);
> - the parametric Nullstellensatz is in AM (Ait El Manssour et al., Thm 1);
> - Schubert vanishing is in AM ∩ coAM in types A–D (Pak–Robichaux, Thm 3.4), so it is not NP-hard unless PH = Σ₂^P.

Before posting:
- state that the half-plane inputs are unrefereed preprints, CT formalized in Lean according to its authors;
- cite 2602.17904 (HN ∈ CH) after opening it;
- add the two-line derivation of Theorem 9 from Cor. 9.6 (§1 above);
- give the new bound on x₀ explicitly.

Do not include CX-K06 or the GCT V transfers beyond Theorem 3.4 until they are checked.

## 6. Corrections after the HNAM note (25 Nov 2026, same checker)

- **Section 4 is wrong on one point.** Our own paper hexagon:2611.00987v1 already states the main claim: Proposition
  17.2 (p. 59; p. 62 in v2) and the HN row of Table 1 (pp. 5–7). It says that a fixed zero-free half-plane for all ζ_K
  gives HN ∈ AM, accepting Cureton–Thorner. So "nobody states it" holds only outside our own work.
- **§1, the replacement inequality.** My (n+1)·log|Δ| is the monic case. For non-monic f the primes dividing the
  leading coefficient a must be set aside too, and the bound is (2n+1)·log₂|aΔ|. This is harmless in Koiran's
  application.
- **§1, the bit length.** My factor 1/(1−θ) ignored the loss from log x. The HNAM note absorbs log x by
  log x ≤ x^δ/(eδ) with δ = (1−η)/2, which gives the exponent 2/(1−η). Both are polynomial; the note's constants are
  checked in notes/HNAM/CHECK_EVENTS.tsv.
- **§4, Andrews–Garg–Schost 2602.17904.** Now read (arXiv HTML): HN is in CH over ℚ, number fields, F_q and their
  rational function fields (Thm 1.1), and dimension and cardinality are in FP^CH (Thms 1.3–1.4).
