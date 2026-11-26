# Connection map, region NUMBER_THEORY (ALPOGE, ZETA_GRH, HODGE, the number theory of SWEEP3_A/B, and outside work)

Written 24-25 Nov 2026 by Claude Opus 5.5 at effort max, launched by the main session 329fb1e6 (Claude Opus 5.5 at effort
max), following `MAP_BRIEF.md`. The runs mapped here are GPT-6 Astra (ChatGPT Pro mode) unless named otherwise; their
checkers are named as the cluster files give them. Rows: `MAP_NUMBER_THEORY.tsv` (one per link). Checks made for this map:
`MAP_NUMBER_THEORY_CHECK_EVENTS.tsv`. Running notes: `agent_notes/20261124T2142Z_Connection_map_number_theory_NOTES.md`.

**Inputs read.** The cluster files ALPOGE, ZETA_GRH, HODGE, SWEEP3_A, SWEEP3_B; LITERATURE_20261124 (with the Hexagon
appendix); TOPICALITY_NT_HODGE (whose outside searches I did not repeat); OLDER_RUNS (head); the earlier map
`field_experts/structural_maps_20261123/GRH_RUNGS.md`. In the runs, at the statements a link depends on: BEYOND_DIRICHLET
(STATEMENTS.tsv; `research/cubic_joint_content_fragment.tex` l.119-301; `research/structural_comparisons.tex`, Thm
`th:category`); CX_GRH.tex l.280-660 (CX-K01, K02, K05, K06); HODGE_FINISH Paper A `main.tex` l.440-500, 808-860, 3260-3345;
THETA3.tex l.14285-14765 (C32); NIGHT_AFTER_ALPOGE `papers/ihara/main.tex` l.1-330 and `papers/k-groups/main.tex` l.1-140;
KTOWER.tex l.4158-4200; RESEARCH_SA05 `sections/b1_diagonal_gate.tex`; GRH_ALGORITHMS_FINISH QUESTIONS.tsv.

**Outside sources opened at the statement** (all unrefereed unless said): Cureton-Thorner, Hexagon 2610.00200v2, Thm 1.1
and Cor 1.2 (pdf l.150-240); B. Hu, 2610.00216v2, Cor 9.6 (pdf l.3870-3960); B. Liu, 2611.00421v2 (abstract) and
2611.00741v1 (pdf l.1-330); Jaswal, 2611.00339v3, Thm 1.1, Cor 1.2, Thm 1.3 (pdf l.80-200); Milne, 2611.00244v1, Thm 3.1,
3.5 (pdf l.295-480); Koiran, J. Complexity 12 (1996), Thms 1, 8, 9 and Cor 1; Rojas, arXiv math/0301111; Rojas-Zhu, arXiv
1803.04104; Ait El Manssour-Balaji-Nosan-Shirmohammadi-Worrell, arXiv 2408.13027v3, Thm 1 and §3.4; Pak-Robichaux, arXiv
2504.03004, Thm 1.1, 3.4, Cor 1.4; OpenAI's preprints of 1 Oct (Landau-Siegel), 4 Oct (primitive roots, Thm 1.1-1.2) and
5 Oct (QRH 11/12); D. Zhang, arXiv 2611.30749v1; Pila-Shankar-Tsimerman (with Esnault-Groechenig), arXiv 2109.08788
(abstract); Kahn, arXiv math/0205158 (abstract; Ann. ENS 36 (2003) 977-1002); Hexagon abstracts of 2610.00228, 2610.00294,
2610.00699, 2610.00716, 2611.00071, 2611.00080, 2611.00082, 2611.00086, 2611.00334, 2611.00788, 2611.00808, 2611.00829
(with bibliography), 2611.00885, 2611.00911, 2611.00976, 2611.00995, 2611.00998 (with bibliography). The whole Hexagon
catalogue (1,530 works, 1 Sep-24 Nov, the dump in the session scratchpad `older_runs/hex_all.json`) was grepped for every
new statement below.

**Notation.**
- **A**: Alpöge's theorem (20 Nov 2026, Lean-checked by several kernels): RH for ζ and every Dirichlet L-function.
- **M**: GRH for Hecke L-functions as claimed by Masullo's draft. No credence; results resting on M stay conditional.
- **QRH(θ)**: a zero-free half-plane Re s > θ for every Dedekind zeta function (with its pole at 1), θ < 1 fixed. Three
  outside sources give it: **CT** = Cureton-Thorner, θ = 31/32 (proof formalized in Lean with AxiomProver); **Hu**, θ = 7/8
  for every unitary Weil L-function, infinite-order Hecke characters included, with an effective Chebotarev theorem (Cor.
  9.6); **Liu**, θ_G ∈ (0.8733326374459049352, 0.8733326374459051924) for every continuous unitary Hecke, Artin and Weil
  L-function (2611.00741, 20 Nov; it improves his B* = 0.8733458561067185768 of 2611.00421v2, which the QuasiRiemannTracker
  site lists as its best verified bound on 24 Nov).
- **PF26**: OpenAI, deterministic polynomial factorization over F_p (4 Oct 2026).

---

## 1. The new knowledge, ranked by usefulness

### NK-1. Koiran's theorem without GRH: Hilbert's Nullstellensatz is in AM, and so are its descendants

**Statement.** Assume QRH(θ) for some fixed θ < 1 (supplied by CT, Hu or Liu). Then:
1. HN (does a system of integer polynomials have a complex solution?) lies in AM ∩ RP^NP ⊆ Π₂^P (Koiran 1996, Thm 2,
   there under GRH).
2. DIM_C (is the complex variety of dimension ≥ d?) lies in AM (Koiran's 1997 randomized reduction to HN).
3. HNP, the parametric Nullstellensatz over C(y), lies in AM (Ait El Manssour et al. 2408.13027, Thm 1: its GRH enters only
   through Koiran's protocol, §3.4).
4. Schubert vanishing lies in AM ∩ coAM in types A, B, C, D (Pak-Robichaux 2504.03004, Thm 1.1 and 3.4, with their earlier
   coAM result; both use GRH only through HNP ∈ AM). Their Cor. 1.4 becomes: Schubert vanishing is not NP-hard unless PH
   collapses to Σ₂^P, with no GRH.
5. In our CX_GRH run, CX-K02 (circuit and homogeneous HN in AM), CX-K05 (an h.s.o.p. of rational linear forms for an
   equation-given graded algebra in FP^{Σ₂P}, which is GCT V Thm 3.4) and CX-K06 (the EXPH transfers of GCT V Thms 4.10 and
   5.12, and 5.5/4.1 with their equation-access hypothesis) hold with "under H_M" replaced by QRH(θ). The run's own proofs
   use M only to obtain H_D (RH for every ζ_E) and H_D only inside Koiran's theorem (CX_GRH.tex l.433-460, 540-660).

**Proof.** The only analytic input in Koiran's proof is his Theorem 9 (Adleman-Odlyzko, under GRH): for f ∈ Z[X]
irreducible of degree n with discriminant Δ, and W(p) the number of roots of f mod p,
S(x) = Σ_{p≤x, p∤Δ} (1 − W(p)) = O(x^{1/2} log(x^n Δ)). Replace it by:

*Lemma (prime ideal theorem from a half-plane).* If ζ_K ≠ 0 on Re s > θ, then for x ≥ 3,
|π_K(x) − Li x| ≤ C (1−θ)^{−1} x^θ (log d_K + n_K log x) log x, with C absolute and effective.
*Proof.* Lagarias-Odlyzko 1977, Thm 7.1 (with L = K and C = {1}; Rojas's Thm 5 quotes it) gives, for 2 ≤ T ≤ x,
ψ_K(x) − x = −Σ_{|γ|<T} x^ρ/ρ + Σ_{|ρ|<1/2} 1/ρ + O((x/T)(n_K log² x + log d_K + n_K log T) + (n_K + log d_K) log x).
By the half-plane and the functional equation every zero in the strip has 1−θ ≤ β ≤ θ, so |ρ| ≥ 1−θ. Lagarias-Odlyzko's
Lemma 5.4 (the unconditional zero count, ≪ log d_K + n_K log(|t|+2) zeros with |γ − t| ≤ 1) then gives
Σ_{|γ|<T} |x^ρ/ρ| ≪ x^θ((log d_K + n_K)/(1−θ) + (log d_K + n_K log T) log T) and |Σ_{|ρ|<1/2} 1/ρ| ≪ (log d_K + n_K)/(1−θ).
Take T = x and pass from ψ_K to π_K by partial summation; prime powers cost O(n_K √x log x). ∎
Hu's Cor. 9.6 states exactly this with θ = 7/8: π_C(x) = c_C Li(x) + O(c_C 𝒟_L x^{7/8+ε}), 𝒟_L = log(eD_L) + n_L, the
constant absolute and effective.

*Koiran's Theorem 9 without GRH.* For p ∤ Δ, W(p) is the number of degree-one primes of K = Q[X]/(f) above p. Hence
|S(x)| ≤ |π(x) − Li x| + |π_K(x) − Li x| + n√x + (n+1) log|Δ| ≤ C(1−θ)^{−1} x^θ (log|Δ| + n log x) log x + 2n√x.
Koiran's Cor. 1 then reads π_f(x) ≥ n^{−1}[π(x) − log|Δ| − |S(x)|]. In his Thm 8, n and log|Δ| are at most
2^{poly(input)}, so the main term dominates once x^{1−θ} ≫ n² log|Δ| log² x. His Thm 1 therefore holds with x₀ replaced
by x₀^{c/(1−θ)}, whose bit length is still polynomial, and his protocol (Thm 2, and its AM form) runs unchanged. The
unsatisfiable side (his Thm 5) was unconditional. Items 2-5 are the cited reductions, each of which I read at the point
where GRH enters. ∎

CX_GRH itself said that Lagarias-Odlyzko's unconditional Thm 1.3 (range x ≥ exp(10 n (log|D_E|)²)) does not keep the
primes of polynomial size, which is true; a fixed half-plane does.

**Status.** Proved here as a deduction; no second reader yet (check events E01-E05). The input is unrefereed: CT is Lean-
formalized (AxiomProver), Hu and Liu are not formalized. TOPICALITY_NT_HODGE flagged the CT + Koiran route for CX-K01/K03 as
"UNSETTLED until the deduction is checked"; this settles the deduction and adds items 2-5.
**Novelty.** The Hexagon catalogue has no item on Koiran, Nullstellensatz complexity, Schubert vanishing or Noether
normalization; Bhattacharya's record of QRH consequences (2610.00178) works only with Dirichlet and Q(√−3) inputs and has no
Koiran section; Hu lists effective Chebotarev but not Koiran; a web search found nothing.
**Why it matters.** Koiran's theorem has been conditional since 1996, and GCT V's "Noether normalization in PH" and the
Schubert results inherit the condition. These are statements complexity theorists and the GCT fleet use. A further
candidate with what looks like the same mechanism, not checked here: Bürgisser, "Cook's versus Valiant's hypothesis" (TCS
235, 2000), whose characteristic-zero transfer (BoolPart(VP) in non-uniform NC³; a false Valiant hypothesis collapses PH to
NC/poly) assumes GRH to reduce complex constants modulo small primes; open it at the GRH step before claiming it.
**Grothendieck's frameworks.** X = Spec Z[x]/(f_i) → Spec Z: a complex point exists iff the generic fibre is nonempty iff
(Chevalley, EGA IV₁ 1.8.4) the image contains a dense open of Spec Z; the protocol samples closed points of X of degree one
over F_p, and their density is governed by ζ of the residue field of a closed point of X_Q (closed points of schemes of
finite type over Z have finite residue fields, EGA IV₃ §10.4 on Jacobson schemes; Serre's "Zeta and L-functions", 1965).
Only a zero-free half-plane of that one ζ_E is needed (CX-K01's localization).

### NK-2. The Galois-orbit criterion of HODGE_FINISH Paper A, without André-Oort and with effective bounds

**Statement.** In the setting of Paper A §"An optional Galois-orbit criterion" (S a geometrically connected fine unitary
Shimura base over F, G^ad Q-simple of type A; D_D = {s : δ_W(s) ≤ D}), drop the hypothesis "André-Oort for every power of
S". Let H(D) bound the Baily-Borel degree of every geometric component of the closure of D_D (there are at most H(D) of
them, so each is defined over a field of degree ≤ [F:Q]·H(D)). Then:
- (a) if D_D ≠ S, every relative-Weyl special point x ∈ D_D satisfies d_{L_x} ≤ c(1/32, H(D), [F:Q]·H(D)) and
  α_x ≤ c(1/32, H(D), [F:Q]·H(D)), where L_x is the splitting field of the Mumford-Tate torus of x and c is Jaswal's
  effectively computable constant (2611.00339v3, Thm 1.1(ii) with Cor. 1.2, which uses CT for QRH(1/32; L_x));
- (b) (effective forcing) one relative-Weyl special point x with δ_W(x) ≤ D and d_{L_x} > c(1/32, H(D), [F:Q]·H(D))
  forces D_D = S, i.e. a detector of degree ≤ D on every fibre;
- (c) (effective dichotomy) either the Weil classes of the family are algebraic on every fibre, or for every D every
  relative-Weyl special point with d_{L_x} > c(1/32, H(D), [F:Q]·H(D)) has δ_W(x) > D. This is an effective form of
  HECKE_DIV R23 and of Paper A's own dichotomy (Q05).

**Proof.** Paper A's proof of Prop. galois-witness (main.tex l.3297-3299, via Chai-Oort Lemma 6.3) shows that a
relative-Weyl special point lies on no proper positive-dimensional special subvariety of S. If D_D is proper and Z is a
geometric component of its closure containing x, any special V with x ∈ V ⊆ Z is {x} or S, and S ⊄ Z; so {x} is maximal
special in Z. Jaswal's Thm 1.1(ii) bounds d_{L_V} and α_V for every special V maximal in a geometrically irreducible
closed Z of degree ≤ D' defined over a field of degree d, under QRH(δ; L_V); CT gives δ = 1/32 for every L (Jaswal's
Cor. 1.2). This is (a); (b) is its contrapositive, and (c) combines (a) with Paper A's Q01 (D_D = S for some D iff the Weil
classes are algebraic everywhere). ∎

**What remains.** H(D) is effective in principle (D_D is the image of a union of connected components of an explicit
Chow/Hilbert parameter space, FGA 221 and Kollár I.3; degrees of images are bounded by degrees of sources), but no number
has been computed, and Jaswal's c is exponential in a power of its degree argument (his Remark 8.2). The detector itself is
still the gate. **For prompt 70d this changes the brief:** its item (b), "Scanlon's B_S(H), ineffective", is now effective,
and H15's orbit bound is not needed for this criterion, since the discriminant replaces the orbit size. Jaswal's paper is
AI-produced and declares no human understanding; the statement is conditional on it and on CT.
**Status.** Proved here as a deduction (event E07). Pila-Shankar-Tsimerman (arXiv 2109.08788, André-Oort "in full
generality") already makes Paper A's hypothesis a theorem, as the HODGE cluster suspected (I opened the abstract);
Jaswal makes it effective.
**Grothendieck.** Hilbert and Chow schemes as bounded families (FGA 221), specialization of cycle classes (SGA 4 XVI 2.2,
SGA 4½ Cycle), Shimura varieties as moduli of motives with additional structure.

### NK-3. Class groups and auxiliary primes in polylogarithmic size from a half-plane (GRH_ALGORITHMS Q02, Q03 rows)

**Statement.** Assume QRH(θ) for the Hecke L-functions of finite-order characters (CT's Cor. 1.2, Hu, Liu).
1. (Bach-type generation) For every number field K ≠ Q, Cl(K) is generated by the classes of prime ideals of norm at most
   C(θ)·(log d_K + n_K)^{1/(1−θ)} ≪ (log d_K)^{1/(1−θ)}: exponent 8 with Hu, 7.8947 with Liu's θ_G, 32 with CT (under GRH,
   Bach: 12 log² d_K). More generally, for every proper subgroup H of Cl(K) a prime ideal outside H exists below that bound.
2. (Q02's auxiliary prime) For prime r and prime p ∤ r there is a prime ℓ ≡ 1 (mod r) with p^{(ℓ−1)/r} ≢ 1 (mod ℓ) and
   ℓ ≪ (r² log(rp))^8 (Hu's Cor. 9.6 for L = Q(ζ_r, p^{1/r}), class C = the nontrivial translations of AGL₁(F_r);
   log D_L ≪ r² log(rp)); with Adleman-Lenstra this constructs F_{p^r} deterministically in time poly(r, log p).

**Proof of 1.** Fix a nonnegative W ∈ C_c^∞((1,2)), W ≠ 0, a_W = Ŵ(1) > 0. For a class-group character χ the smoothed
explicit formula (Hu's (9.13), conductor 1) gives Σ_𝔞 Λ(𝔞)χ(𝔞)W(N𝔞/x) = δ_χ a_W x − Σ_ρ x^ρ Ŵ(ρ) + O_W(log d_K + n_K), and
the zero sum is O_W(x^θ(log d_K + n_K)) because |Ŵ(ρ)| ≪ (1+|ρ|)^{−2}. If every prime ideal of norm ≤ 2x lies in H, take
χ ≠ 1 trivial on H; every 𝔞 in the support is a power of such a prime, so the χ-sum equals the trivial sum. Subtracting,
a_W x ≤ C_W x^θ (log d_K + n_K), false for x > (C_W(log d_K + n_K)/a_W)^{1/(1−θ)}. ∎ Item 2 is Hu's corollary as stated.

**Status.** Events E06 (item 1) and E14 (item 2). Item 2's outcome was already noted by the run (QUESTIONS.tsv Q02: "the separate CT 2026 v2 preprint theorem
... supplies a different conditional route"), and F_{p^r} is in any case known through PF26 (TOPICALITY). Q02 as posed (A
as the only new input) stays open. Item 1 is a two-line corollary of Hu's formula that I found stated nowhere (Hexagon grep
"class group ... generat", web); it moves "Bach's class-group bound" and, by the same character sums, "CM split-prime
selection" in GRH_ALGORITHMS Q03's table from "beyond A" to "given QRH, with exponent 1/(1−θ)". Isogeny-graph expansion
(Jao-Miller-Venkatesan) should follow the same way with edge norms up to (log q)^{1/(1−θ)+ε}; I have not written that out.

### NK-4. THETA3-C32 sharpened: an explicit integral Weil class of self-intersection 128

**Statement.** In THETA3-C32 (H: y² = z∏(z² − a_j²), A = J(H), Q(i)-action ρ(z,y) = (−z, iy)), let u: Sym⁴H → Pic⁴H ≅ A
be the Abel-Jacobi map, r: Sym⁴H → W₀ the quotient map, and B_j ⊂ Sym⁴H the cycle obtained from the plane Q_j ⊂ W₃ through
a resolution of Sym⁴H ×_{W₀} W₃, exactly as THETA3 obtains C_H on H⁴ in (C32q). Then C'_A = u_*(B₀ − B₂) is an integral
algebraic cycle with class w₀ ∈ W_{Q(i)}(A), ∫_A w₀² = 128, and cl(C_A) = 24·cl(C'_A) for THETA3's cycle (73728 = 24²·128).

**Proof.** H⁴ → W₀ has degree |G| = 1536 and factors as r∘π with π: H⁴ → Sym⁴H of degree 24, so r has degree 64. The
argument of (C32r) applied to Sym⁴H in place of H⁴ gives cl(B₀ − B₂) = r*c₀, and (C32p), ∫_{W₀} c₀² = 2, gives
∫_{Sym⁴H} (r*c₀)² = 64·2 = 128. THETA3 shows that a* identifies W_{Q(i)}(A) with q*U₀; since a = u∘π, q = r∘π and π* is
injective on rational cohomology, u*W_{Q(i)}(A) = r*U₀, so r*c₀ = u*w₀ for some w₀ ∈ W_{Q(i)}(A). The map u is birational
(g = 4; THETA3 uses this), so u_*u* = 1, ∫_A w₀² = ∫_{Sym⁴H}(u*w₀)² = 128 and cl(C'_A) = u_*u*w₀ = w₀. A general D in the
support of B_j has its four points over distinct values of t = z², so it contains no hyperelliptic pair and h⁰(D) = 1; u is
injective near the general point and C'_A is a genuine image cycle. Finally cl(C_A) = a_*q*c₀ = u_*π_*π*r*c₀ = 24·w₀. ∎
**Status.** Proved here from THETA3's own (C32p)-(C32s); event E08. **Use.** For the C25 fourfold (End = Z[i]) the
algebraic class is 24 times smaller than recorded, which is what the open THETA3 item "C32 quantitative" and the HD-WQ/HD-U
constants need. Comparing with Paper A's degree-48 detector on principal Gaussian fourfolds (van Geemen's construction)
still needs deg_θ u_*(B_j), computable from u*θ = 7x − δ/2 on Sym⁴H; not done here.

### NK-5. The BEYOND_DIRICHLET register undersells A, and the content exponent with Liu's θ_G

**Statement.**
- Rows stated "under Dirichlet GRH" (BD-R39, R40, R46) and the clauses "under classical zeta RH" (BD-R42's R^{−7/4},
  BD-R43's and BD-R53's 2Y^{2/7}, BD-R52's −7/4, BD-R56's third row) hold unconditionally: they use RH only for ζ or for
  Dirichlet L-functions, which is A. The fragment says "The last row additionally assumes classical zeta RH", with ρ the
  zero-free exponent of the Riemann ζ ("Its trivial character over Q gives the zeta assertion").
- With A and Liu's B*, the content exponent is γ = (B* − 1/2)/(2B* − 1/4) = 0.249447399928862… < 1/4 (not 0.28499…, which is
  the value without A). With Liu's θ_G it becomes 0.249442974129865…, and the no-A value (2θ−1)/(3θ) becomes
  0.284986973224567…; the primitive norm product then exceeds Y^{0.50111405…}/4. OpenAI's 7/8 gives exactly γ = 1/4.
- BD Q02 (Artin's conjecture in Calegari's family): the possible common real zero α of B and C lies in (1/2, θ_G].

**Status.** Computation (E09); the register reading is mine (E10). The change is numerically small; the point is that A
already places the cubic gate's content support strictly below Y^{1/4}.

### NK-6. Alpöge's theorem is the Riemann hypothesis of Borger's F₁-geometry; the relative version is the cubic rung

**Statement.** Let X be a smooth proper Borger Λ-scheme over Z[1/N] (commuting Frobenius lifts; for torsion-free rings this
is a λ-ring structure in Grothendieck's sense, SGA 6 V, by Wilkerson's theorem). Then
ζ_X(s) = ∏_j ∏_χ L^{(N)}(s − j, χ)^{m_{j,χ}}, with χ finite-order Dirichlet characters and L^{(N)} omitting the Euler factors
at p | N, and every non-real zero of ζ_X lies on a line Re s = j + 1/2 (by A) or Re s = j (removed Euler factors),
0 ≤ j ≤ dim X.
**Proof.** BD-R83 (`structural_comparisons.tex`, Thm th:category; Borger Thm 0.1 and Cor. 6.2 with purity): odd
cohomology vanishes and H^{2j}(X_Q̄, Q_ℓ)(j) has finite abelian image, hence is a sum of Dirichlet characters
(Kronecker-Weber). The Euler factor at p ∤ N is ∏_j det(1 − Frob p^{−s} | H^{2j})^{−1}. ∎ It extends ZETA_NEXT NX-L06
(over Z, proper flat) and fixes the exact scope of ALPOGE_BRIDGES CC-F01.
**The relative version, as the object that cancels the obstruction.** BD-R83 shows that the cubic ρ of Q(∛269) is not in
Borger's category, which is why A stops there. BD's own Prop. th:frobenius shows that E = Q(ω, ∛269) does carry commuting
relative Frobenius lifts over O_K[1/(3·269)], K = Q(ω). For relative Λ-schemes over O_K[1/N] the same argument gives
Hecke characters of K in place of Dirichlet characters, so "RH for relative F₁-geometry over O_K" is exactly GRH for the
finite-order Hecke characters of K, the GL₁/K rung of GRH_RUNGS §2 and the common gate of BD Q01, ALP_CONNES Q7, ALP_MACHINE Q3
and GRH_ALGORITHMS Q02. **Status.** Immediate from BD-R83 and A (E11); BD-R83 itself is UNSETTLED against Borger §6 per
TOPICALITY. Useful as a framing for the conference, not as a theorem anyone needs.

### NK-7. Rational and numerical equivalence agree for varieties of abelian type over finite fields

**Statement.** For every smooth projective X of abelian type over a finite field (abelian varieties, products of curves),
CH^m(X)_Q → N^m(X)_Q is an isomorphism; in particular the cycle map CH^m(X)_Q ⊗ Q_ℓ → H^{2m}(X̄, Q_ℓ(m)) is injective.
**Proof.** Kahn (Ann. ENS 36 (2003); arXiv math/0205158 abstract) proves this for X of abelian type whenever the Tate
conjecture holds for X. Milne's report (2611.00244, Thm 3.1) gives the full Tate conjecture for all abelian varieties over
finite fields, from Milne 1999 with OpenAI's CM Hodge proof (human proof: van Hoften-Sempliner, 2610.00259) and the
rationality conjecture (Madapusi, 2610.00226). ∎ Kahn also deduces the Gersten conjecture for DVRs whose residue field is
the function field of such an X.
**Effect on our items.** RESEARCH_SA05 Prop. B-diagonal-Chow-gate reduces Beilinson injectivity, under universal Tate, to
codimension two on threefolds; NK-7 settles that case for threefolds of abelian type, so the open part is the non-abelian
threefolds. If Sun's claimed Tate conjecture over finite fields (arXiv 2611.28178, unverified) holds, SA05's universal
hypothesis holds too and B.1 becomes unconditional as a reduction. **Status.** A combination of two cited theorems (E12);
I opened Kahn only at the abstract. Milne's report does not mention Kahn.

### NK-8. Outside conditional results that A makes unconditional (small)

- Vynohradov, 2611.00885: every interval (x, x + 2 log² x], x ≥ 4, contains an even sum of two primes (RH for ζ only).
- Henriksson, 2611.00808: explicit counts of balanced semiprimes in intervals of length 384√x (log x)² (RH via
  Chirre-Hagen's mean square).
- Yilin Liu, 2611.00788: the Li-Liu spectral hypothesis R fails (GRH used only at one modulus, a Dirichlet input).
- The de Bruijn-Newman constant is Λ = 0 (A with Rodgers-Tao), superseding 2611.00460, 2611.00349 and 2610.00714.
- MOONSHINE.023: Ogg's cutoff 4300 is unconditional (already in the ALPOGE file).
The three papers are primarily AI-generated and declare no human understanding; A removes their hypothesis, not the need
to check them. None changes an item of ours.

---

## 2. Outside results that change our items

| Outside result | Our items | How |
|---|---|---|
| CT 2610.00200 (31/32, Lean); Hu 2610.00216 (7/8, all unitary Weil L, effective Chebotarev); Liu 2611.00741 (θ_G) | CX_GRH CX-K01-K06; GCT V Thms 3.4, 4.10, 5.12 | NK-1: Koiran's theorem and the GCT V transfers no longer need GRH or M |
| same | GRH_ALGORITHMS Q02, Q03 table, Q09 | NK-3: Q02's outcome and Bach-type bounds with exponent 1/(1−θ); Q02 "from A alone" and Q09 stay open |
| Liu 2611.00741, Hu, 2610.00716 (7/8 for angular Hecke L over Q(√−3), Lean-checked closure) | MOONSHINE Q1 (ψ₃₆, ψ₂₇, ψ³, Sym³ of η(6τ)⁴) | the best unconditional statement is now zero-freeness for Re s > θ_G in the unitary normalization; RH open |
| Hu ("CM motives after the weight shift") | ZETA_TWO CM01, board H05, ZETA_NEXT NG07 | the quasi-RH part is unconditional; RH stays on M |
| Hu, Liu (Brauer induction, Artin L-functions) | GRH_NIGHT MT-ART01, MT-S506 | odd 2-dim Artin L-functions: entire (Khare-Wintenberger) and zero-free for Re s > θ_G without M; S₅ Artin factors holomorphic on Re s > θ_G |
| Liu 2611.00741 | BD-R50-R56, BD Q02 | NK-5: γ and the window (1/2, θ_G] |
| A itself | BD-R39/R40/R46 and the zeta-RH clauses | NK-5: unconditional |
| Jaswal 2611.00339v3 + CT; Pila-Shankar-Tsimerman 2109.08788 | Paper A Q27, HECKE_DIV R23, prompt 70d | NK-2 |
| Milne 2611.00244 | Paper A Q01(iv); C44_POS (ambient E⁶); SA05 B.1 | Tate holds at every good reduction of a CM point, so Q01(iv) is exactly a uniform-degree version of a known Tate theorem; the ambient E⁶ of C44_POS is covered, the axes are not; NK-7 |
| Kahn 2003 + Milne | SA05 B.1, B-diagonal-Chow-gate | NK-7 |
| Mok-Zheng 2611.00998; Pintar 2611.00829 | NIGHT_AFTER_ALPOGE C.K12/K80, H18; KTOWER | overtaken (TOPICALITY), but Pintar's "Grothendieck-Montpellier joint representation theorem" is our KTOWER K17-S17-JOINT (KTOWER.tex l.4181; cited at checkpoint 11, edb183a9, l.4158-4272), and Mok-Zheng build on Pintar: the outside range rests on our theorem |
| D. Zhang, arXiv 2611.30749 | HODGE_SIGN SG-08-SG-11, Hexagon 2611.00789 (H01) | the first outside human exposition; treats A¹ only, cites "The Hexagon note, Lemma 3" as its Lemma 2.6, calls our account "not well-polished", reports no error |
| OpenAI 4 Oct (Artin infinitude); 2610.00228 (positive lower density, via CT); 2610.00294 (Lang-Trotter for (y² = x³ − 2x, (2,2))); 2610.00699 (cyclic reduction) | GRH_RUNGS §2 and AN_GRH (Hooley); GRH_ALGORITHMS Q03 "Hooley's Artin density" | the infinitude and positive lower density are proved; the exact Hooley density is still open (a half-plane does not control the middle range of Hooley's sum) |
| OpenAI 1 Oct, Liu 2611.00080, Frei-Kai, Guo, Green (Siegel zeros) | ZETA_NEXT NX01/NX02, NC01-NC04, A.ORBIT (H15) | A is not needed there (TOPICALITY); H15 should present A as one input among several |
| PF26 | CX-N01-N04, N13, N15; the 67c outcome | known before (TOPICALITY) |
| Severn 2610.00387v2 Thm A | HODGE_DIVISION D-G34 | known before; Paper A's Q28 should say "conditional on Severn's Thm A, re-derived in D-G34" (TOPICALITY) |
| Broe-Jiang 2611.30237 | HODGE line at fourfolds | Tate for all abelian fourfolds over finitely generated fields, through Markman; context for Paper A at n = 2, no item changes |
| Sihan Chen 2611.00911 (Bost's slope conjecture) | H15 constants | possibly smaller constants in isogeny estimates of Gaudron-Rémond type; I did not verify that their constants use the tensor-slope inequality |
| Calegari 2611.00976 | none directly | a hyperbolic-geometry asymptotic for sums of Hurwitz class numbers along n² − 1; a CM-point object, no mechanism into our runs found |

---

## 3. The links, by theme (rows L01-L47 of the TSV, with L10b, L15b and L30b)

### 3.1 Zero-free half-planes beyond Dirichlet, and what they unlock
- **L01-L05 (NK-1).** QRH(θ) → Koiran Thm 9 → HN ∈ AM → DIM_C, HNP, Schubert vanishing, CX-K02/K05/K06. Mechanism: the
  error x^{1/2} becomes x^θ, which costs only a factor 1/(1−θ) in the bit length of the sampled primes.
- **L06-L08 (NK-3).** Hu Cor. 9.6 → GRH_ALGORITHMS Q02's auxiliary prime; smoothed explicit formula → Bach-type
  generators; same character sums → CM split-prime selection.
- **L09 (NK-5).** Liu θ_G → BD's γ and Q02 window.
- **L10.** Liu/Hu/2610.00716 → MOONSHINE Q1 status (quasi-RH for ψ₃₆, ψ₂₇, ψ³ and the symmetric cube; RH open).
- **L10b.** Liu's centered cube-free reference (his Thm 4.1: the saving is governed by zeros of L(s, ω³), with ceiling 5/6
  by his Prop. 4.2) is structurally the same two-variable Euler-product device as BD's content decomposition (local factor
  1 − t_p p^{−s} + η(p)p^{−v}); a kinship, not a transfer.
- **L11.** The outside quasi-RH method (OpenAI's 7/8, Hu, CT, Liu, and OpenAI's Artin paper) is the Patterson cubic theta
  over Q(√−3) with sextic Kummer twists, exactly the route our GRH_RUNGS §4 named for the cubic rung and did not carry out.
  The outside work reached θ ≈ 0.8733 uniformly over all fields; our four runs ask for 1/2 for one character.
- **L12.** Hu/Liu → GRH_NIGHT MT-ART01 and MT-S506: Artin L-functions are holomorphic and zero-free for Re s > θ_G by
  Brauer induction; with A, MT-S506's poles of S₅ Artin factors are on Re s = 1/2.

### 3.2 CM points, special points and the Hodge conjecture for Weil classes
- **L13-L15 (NK-2).** Jaswal + CT → Paper A Prop. galois-witness, effective, without André-Oort; → HECKE_DIV R23 made
  effective; → prompt 70d's gate list. **L15b:** Pila-Shankar-Tsimerman → the qualitative removal of the hypothesis.
- **L16.** H15 (A.ORBIT, |Gal·x| ≥ c_g D_x^{1/(4g)}) and Jaswal's Prop. 3.3 orbit exponent μ = 1/(16·t·s·n_T(n_T − 1)):
  H15's exponent is far better (TOPICALITY); Jaswal's bound is the one with effective constants over all Shimura data.
- **L17.** DEG_L B19-B21 (core-index obstruction, degrees ≥ c√J) and HECKE_DIV R23 / NK-2(c): both say that bounded
  division along CM sequences cannot come from a fixed source; NK-2(c) gives the quantitative form on the special-point side.
- **L18 (NK-4).** THETA3-C32 → C'_A with ∫ = 128 → HD-WQ/HD-U constants; Paper A Q03's degree 48 (van Geemen) is the
  comparison still to compute.
- **L19.** Milne's report → Paper A Q01(iv): at every good place of a CM point, sp(t_x) is a Tate class on an abelian
  variety over a finite field, hence algebraic; Q01 says the Hodge conjecture for abelian varieties is equivalent to a
  uniform degree bound in that now-known Tate theorem. Paper A states that it does not use the Tate conjecture (l.270); the
  abstract could say what (iv) adds to Milne's theorem.
- **L20.** Milne's report → C44_POS: Tate and the Hodge standard conjecture for the ambient E⁶ are covered; A13/A28/A30 on
  the non-abelian axes B remain new (TOPICALITY). The two positivity mechanisms differ: C44's Gram form is Tr(aā) on a
  product of CM fields, positive by Weil's RH directly in characteristic p, while Milne transports characteristic-zero Hodge
  positivity through the polarized Tannakian category of CM motives (his §3.10).

### 3.3 K-groups, Iwasawa theory and the Galois action on π₁
- **L21.** KTOWER K17-S17-JOINT → Pintar 2611.00829 (cited by name and line range) → Mok-Zheng 2611.00998 → K_{4m}(Z) = 0
  for m ≤ 30, all resting on the Lean archive's strict Selmer bound (OneCharU_s, Step 17), as our C.K12/K80 does.
- **L22.** K_{4m}(Z)_p = 0 ⟺ the even eigenspace A_p^{(ω^{−2m})} of Cl(Q(μ_p)) vanishes (our k-groups paper, eq.
  (classzero)), and then X_p^{+,(ω^{−2m})} = 0 by Nakayama. C.IHARA (hexagon 2611.00939) needs X_p^+ finite, and its Lemma
  4.1 works even component by component (T_e cyclic, cup generation per component). So Mok-Zheng give the Greenberg
  hypothesis in the components ω^{−2m}, m ≤ 30, at every prime. Whether a component-local form of the kernel equality
  exists is a gate I state but do not settle (conference topic T5).
- **L23.** BD Paper I (K_{2e}(O_E)_(3) for E = Q(ω, ∛269)) and Milne's report (the Lichtenbaum-Milne special-value
  conjecture is a theorem for abelian varieties over F_q, Milne 2015 Thm 11): the same Weil-étale/Selmer formalism; BD's
  every-degree computation is a test case for the number-field side, which is not proved for this non-abelian field.
- **L24.** RESEARCH_SA05 prop:B-integral-errors and SA06 E.4b/E.4g (the Z/2 in 15:173) and Flach-Morin §5.8.3 (known
  before, TOPICALITY): the Weil-étale side of L23.

### 3.4 Λ-rings, F₁ and the line where A stops
- **L25 (NK-6).** BD-R83 + A → RH for smooth proper Λ-schemes over Z[1/N]; extends NX-L06, fixes CC-F01.
- **L26.** BD th:frobenius (relative Frobenius lifts over O_{Q(ω)}) → the relative version is the cubic rung (GRH_RUNGS
  §2's "single missing factor" L_K(s, χ_{p,r})).
- **L27.** ZETA_TWO ZT08 (the Euler factor is a λ-ring invariant, SGA 6 V §2) and RESEARCH_SA20's Int(R) results
  (integer-valued polynomials are binomial rings, i.e. λ-rings with trivial Adams operations): the same Grothendieck λ-ring
  line; SA20 B.022 (Int(F₂[[t²,t³]]) projective) concerns the binomial ring Int(R), not Borger's arithmetic Λ, so no
  transfer.

### 3.5 Positivity and traces (internal links)
- **L28.** ALP_CONNES AC-T51 (Connes's trace formula ⟺ A), TRACE_DET DET-16/DET-18 (Fredholm determinants with positive
  operators ⟺ RH/GRH), ALPOGE_BRIDGES BR-TR-01 (B ≥ 0): with A, all are theorems; GRH_NIGHT MT-M23 shows the positive
  Hilbert realization fails for ζ_L of non-abelian L by induction multiplicities, so the positivity must be posed per
  irreducible ρ (GRH_RUNGS §3).
- **L29.** ZETA_HEAT's simplicity test (hexagon 2611.00996) measures D_{N,k} → 2Σ(m_γ−1)γ^{−2k}; applied to ζ_L for
  non-abelian L it is positive (MT-M23); for abelian K under A it tests simplicity and the absence of coincidences between
  different L(s,χ), a statement our runs have not posed.
- **L30.** HODGE_SIGN SG-08 (sign-only Deligne bound), C44_POS (positivity from Weil's RH alone), SIGN_NEXT SN-14 (sign-only
  identities cannot give scan 049's positivity). **L30b:** Zhang's exposition isolates our Lemma 3, the chain form
  x₁x₂ + … + x_{n−1}x_n, as the step that gives the square-root saving, and finds no error.

### 3.6 The cubic rung
- **L31.** BD Q01, ALP_CONNES Q7, ALP_MACHINE Q3, MOONSHINE Q1 (positive infinity type), GRH_ALGORITHMS Q02: one object,
  Hecke L-functions over Q(ω) (or over Q(ζ_r)); BD-R56's gate is the sharpest proved reduction; the outside method reaches
  θ_G for all of them at once.
- **L32.** ALP_MACHINE AM-S1-S4, BD-R06, MOONSHINE CM.001: the order-3 phase must commute; BD's Lemma commuting-phase
  (structural_comparisons.tex) is the general form.

### 3.7 Corrections and credits
- **L33.** ALPOGE_BRIDGES BR-15 (Thakur Prop. 2.9), GRH_NIGHT CX-ALG-016 (BIMS Thm 3.1), 67c P163 (Guo, Lemma B.1),
  RESEARCH_SA07 G.2.2 (Bhowmik-Pathak Thm 1.11): corrections still owed (TOPICALITY: no source revised).
- **L34.** Pintar's citation of KTOWER (L21) is a credit to record in the H18 withdrawal note.
- **L35-L39.** The A-unconditional items of NK-8: Vynohradov, Henriksson, Yilin Liu, the de Bruijn-Newman constant, the
  Ogg cutoff.

### 3.8 Outside results with no new mechanism of ours (context rows)
- **L40.** The October Landau-Siegel exclusions replace A wherever A only removes a Stark exceptional zero (NX01/NX02,
  NC01-NC04, H15).
- **L41 (NK-7).** Kahn 2003 + Milne's report → SA05's Chow gate in abelian type. **L42.** Sun's claimed Tate conjecture
  over finite fields would supply SA05's universal hypothesis.
- **L43.** Artin's primitive-root conjecture: infinitude (OpenAI, 4 Oct) and positive lower density (2610.00228, via CT);
  Lang-Trotter for one pair (2610.00294); cyclic reduction (2610.00699). The exact Hooley density stays open.
- **L44.** Bost's slope conjecture (Sihan Chen) might lower H15's constants; unverified. **L45.** Broe-Jiang (Tate for
  abelian fourfolds over finitely generated fields): context for Paper A at n = 2. **L46.** Severn's Theorem A: D-G34 known
  before. **L47.** PF26: the CX_GRH algorithms and the 67c outcome known before.

---

## 4. Conference topics and paper candidates across clusters

1. **T1. "Koiran's Nullstellensatz theorem, and what rests on it, without GRH"** (CX_GRH × GCT × outside quasi-RH). NK-1
   with its consequences (HN, DIM_C, HNP, Schubert vanishing, GCT V Noether normalization in PH). A Hexagon note after one
   independent check of the Lemma and of Koiran's Thm 1 with the new x₀. The most useful item of this map.
2. **T2. "Effective special points and Weil classes"** (HODGE_FINISH Paper A × Jaswal × HECKE_DIV R23 × H15). Fold NK-2
   into Paper A v2 and into prompt 70d: drop André-Oort, replace B_S by Jaswal's discriminant bound, state the effective
   dichotomy; the gate is H(D) and the detector.
3. **T3. "What quasi-RH buys in algorithmic number theory"** (GRH_ALGORITHMS 67/67c × CX_GRH × BD-R22). NK-3 with the
   exponent 1/(1−θ) throughout; it would sit as a section of a 67c v2 or of the H29 note, beside PF26.
4. **T4. "The cubic rung across four runs and the outside cubic-theta method"** (BD, ALP_CONNES, ALP_MACHINE, MOONSHINE,
   GRH_ALGORITHMS). Agenda: why the outside method stops at θ_G (Liu's Prop. 4.2 ceiling from 1/ζ(3s)), and whether BD's
   balanced convolution is the place where an order-3 analogue of Alpöge's sign step must act. One try at "the object that
   cancels the obstruction": Liu's ceiling comes from the pole of 1/ζ(3s) in the residue of the cube-free series; a
   reweighting whose Dirichlet series carries ζ(3s) in the numerator would cancel it; whether the theta comparison survives
   such a weight is the question to put to the next prompt.
5. **T5. "K-groups of Z after Step 17, and the Galois action on π₁(P¹ − 3 points)"** (KTOWER, NIGHT_AFTER_ALPOGE Part C,
   C.IHARA × Pintar × Mok-Zheng × LONGUE_MARCHE). Record the credit chain (L21); ask whether C.IHARA's Lemma 4.1 and pole
   separation give a component-local kernel statement from the Greenberg hypothesis in single even components (L22).
6. **T6. "The Hodge conjecture for abelian varieties as uniformity in the Tate theorem"** (Paper A × Milne's report ×
   C44_POS × SA05). Reframe Paper A's abstract (L19); NK-7 for SA05.
7. **T7. "F₁ and where A stops"** (BD-R83, ZETA_NEXT NX-L06, ALPOGE_BRIDGES CC-F01, BD th:frobenius). A short note only after
   BD-R83 is compared with Borger §6.
8. **T8. THETA3's C32 at index 24** (NK-4): fold into a C32 note with deg_θ u_*(B_j) computed.

---

## 5. Checks made, and what I did not read

Check events are in `MAP_NUMBER_THEORY_CHECK_EVENTS.tsv` (E01-E14). In short: NK-1's lemma and its insertion into Koiran
(author deductions, with readings of Koiran Thm 9/Cor 1, A+24 §3.4, Pak-Robichaux §3 and CX-K02/K05 at the points where GRH
enters); NK-2 (deduction, with Paper A l.3285-3299 and Jaswal Thm 1.1 read); NK-3 item 1 (deduction); NK-4 (re-derivation of
THETA3's (C32p)-(C32s) numbers and the factor 24); NK-5 (computation of γ for B*, θ_G, 7/8, 31/32; register reading); NK-6
(deduction); NK-7 (combination of two cited theorems); Zhang's exposition read against SG-08-SG-11 (no discrepancy found).
None of the new statements has an independent second reader yet.

Not read: the full proofs of CT, Hu, Liu and Jaswal (used as stated, all unrefereed; CT formalized); Kahn 2003 beyond its
abstract; Borger 2009 §6; Lagarias-Odlyzko 1977 itself (its Thm 7.1 and Lemma 5.4 as quoted by Rojas and by Hu, whose
Cor. 9.6 carries out the same derivation); the outside papers of NK-8 beyond their abstracts; KTOWER beyond l.4158-4200.
Nothing was refused.
