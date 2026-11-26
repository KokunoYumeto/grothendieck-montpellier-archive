# Algebraic geometry, Hodge theory, analytic number theory: commentary on the 34 fleet maps, and a structural note towards global Langlands

By Claude Opus 5.5 at effort high (agent a11adac491e93d1d6, launched from main session 329fb1e6, Claude Opus 5.5 at effort
max), 23 Nov 2026, evening. Brief: `BRIEF.md` in this folder. Work file:
`<local>/Documents\agent_notes\a11adac491e93d1d6_NOTES.md`.

**What this note rests on.**
- The maps: `<local>/pequalnp_work\fleet_map\maps\{analytic_number_theory, algebraic_geometry, hodge_theory}.md`
  (ANT-01 to 15, AG-01 to 11, HT-01 to 08; written by me earlier today).
- The fleet nodes as read in `pequalnp_work\desk\lemma_cache`.
- The primers in `field_experts\intake_20261121\intakes\<RUN>\PRIMER_<RUN>_20261123.md`: HODGE_FINISH,
  HODGE_BOUNDED_CYCLES, NEG_NIGHT, GRH_ALGORITHMS_FINISH, ZETA_HEAT, ALP_MACHINE, THETA3, HECKE_DIV, CX_GRH, ALP_CONNES.
- The returns at the locators given in the maps.

**Status words.** "Derived here" means I worked it out in this task, on paper, with no second reader yet. "Checked by
us" is taken from the check events the primers record. Any other result carries the status its run gave it. I label
nothing from memory. Where I use a classical dictionary that I did not reopen, I say so.

A is Alpöge's theorem (RH for every Dirichlet L-function, ζ included; https://alpo.ge/remark.pdf; Lean). E is the
OpenAI manuscript of 25 Oct 2026 on exact #k-SAT, as our runs cite it.

---

## Part A. The 34 maps, ranked by the mathematics they suggest

Each entry gives the mathematics the map points to and the next statements to prove or compute. The first nine carry
most of the interest. The rest are mainly service rows: their mathematics is short or classical, or the bridge needs
an object the fleet does not have.

**1. HT-01: the level-space core as a point of a period domain; the barrier families as special points.**
- *What it suggests.* The core K = L ∩ DC of a level space is isotropic for p_2, and p_2 is definite on real DC. So K
  is the H^{2,0} of a weight-2 Hodge structure, a point of OG(k, (n−1)^2), and the higher S_k are sections of
  Sym^k S^*. The known large families are fixed points of finite symmetries. Part B §2 works this out and proves a
  dimension formula for every eigenspace level space of one symmetry (Proposition B.2): they are all below n. So the
  extremal level spaces (2n − 3, the floor of L-gct-080) are not single-symmetry special points.
- *Next.*
  - (i) Add transposition: compute dim E_ω(g) for g = transpose ∘ (σ, τ) and check levelness numerically for n ≤ 7.
  - (ii) Decide whether the checked n = 4 core (MAPPING_AGENT_RESULTS 1.5: K = span(v e_1^T, v′ e_2^T, v e_3^T) in the
    Klein chart) is fixed by a torus of S_4 × S_4 ⋊ ⟨transpose⟩. If not, find the smallest symmetry group it is an
    eigenspace for.
  - (iii) Equivariant Chern classes of ⊕_{j≤q} Sym^j S^* on the fixed loci of OG for n = 4, 5, against the checked
    κ(4) = 3 (L-gct-216) and the open L-gct-199.
  - (iv) A "distance to a special point" inequality: dim L ≤ C·n + C′·(defect from the nearest eigenspace). This is
    Codex's route R3 in this language.

**2. HT-02 with ANT-09: Hasse-Witt and Frobenius traces carry #SAT.**
- *What it suggests.* NEG_NIGHT puts #SAT mod 2 into the Frobenius on a coherent Hodge piece (NN-C023/C024) and #SAT
  into the H^1 trace of a curve (NN-C026). On the automorphic side these are the a_p-type data of a motive. The
  question is where the hardness lives: in p, in the rank, or in the succinctness. Part B §3.
- *Next.*
  - (i) Statement: for the Fermat pencil F_u = Σ z_i^r + uF of NN-C024, the u = 0 fibre has the diagonal μ_r^r
    symmetry. Compute the μ_r^r-character of the top coherent line, and show the deformation direction F carries the
    #SAT scalar into that character's eigenline.
  - (ii) Separate the parameters. In bounded rank, Pila's point counting gives Frobenius polynomials in poly(log p)
    (as GRH_ALGORITHMS uses it in P125, `thm:fixed-wild-cm`). In NN-C026 the genus is exponential. Find the largest
    rank function g(n) for which the trace stays computable in poly(n, log q). Is it polynomial?

**3. ANT-02: Mahler measure against the DIV hypotheses.**
- *What it suggests.* DIV (L-gct-103/104) holds outright unless the g_i have coefficients of size
  exp(T^e log T / M). The divisor ∏(X+j) has Mahler measure Γ(N+1) and its roots are poles of Γ. So DIV is a statement
  about an archimedean factor against heights (Part B §5).
- *Next.*
  - (i) Bound the coefficient heights produced by the fleet's permanent-to-DIV reduction (their routes/algebraic,
    addendum DIV; the fleet must supply it).
  - (ii) The height-free regime: a p-adic count in residue discs (ANT-12), calibrated on ∏(X+j) itself.
  - (iii) Lean: a separate bounded-height node from `Polynomial.mahlerMeasure_mul`,
    `mahlerMeasure_le_sum_norm_coeff` and `one_le_mahlerMeasure_of_ne_zero` (all in the fleet's Mathlib pin).

**4. AG-02: the level hypersurface at infinity meets the singular locus of the permanent hypersurface.**
- *What it suggests.* The closure of {perm(J+t) = n!} meets {s = 0} in {perm_n = 0}, and its singular points there are
  Sing{perm_n = 0}. Large level spaces are thereby tied to linear spaces in the singular locus of the permanent
  hypersurface, the object of L-gct-036/037.
- *Next.*
  - (i) Prove a Gauss-map inequality, dim Λ ≤ (dim X + dim(Λ ∩ Sing X) + 1)/2, for linear Λ in a hypersurface X, in
    the form needed.
  - (ii) Compute dim Sing{perm_n = 0} for n ≤ 6.
  - (iii) Compute P(L) ∩ Sing{perm_n = 0} for the 2n − 3 family (L-gct-080), the DC family and F_q.

**5. ANT-03: Chebotarev's theorem on roots of unity onto L-gct-211/116.**
- *What it suggests.* A Fourier minor is a GL_k character evaluated at a torus element of order p. Modulo (1 − ζ) it
  reduces to the dimension of the representation, a p-adic unit. Part B §4 gives the four-line proof (derived here).
  The same reduction-at-the-identity drives Codex's prime-power valuation step for 211.
- *Next.*
  - (i) Write 211 with Chebotarev as the black box.
  - (ii) At n = pq, find which minors the identity needs: principal ones (arXiv:2505.24326, 2412.08600, 2505.01189v3;
    to be opened), or all.
  - (iii) An uncertainty form of 211: (number of row frequencies of L) + (column support) ≥ n + 1 at the extremes.

**6. AG-05: the IP gadget as the Arf map on theta characteristics.**
- *What it suggests.* y0y1 + y2y3 on F_2^4 takes the value 0 ten times and 1 six times: these are the 10 even and 6
  odd theta characteristics of a genus-2 curve. A sum of k gadgets is the Arf map in genus 2k. Route M of L-pcx-071
  becomes a covering statement for affine families of odd theta characteristics. Our S15b/S15c (monodromy on theta
  characteristics in characteristic 2) sit next to it.
- *Next.*
  - (i) Orbit-reduce pcx.md's L2 and L3 enumerations by Sp_4(F_2) ≅ S_6.
  - (ii) Find the largest affine flat inside the odd characteristics in genus 2k (L1 gives codimension ≥ 2k). Is it
    attained only by "syzygetic" configurations?
  - (iii) Restate M3 in this language.

**7. ANT-04 with AG-01: Gauss sums, Singer sets and finite geometry for the NOT ladder.**
- *What it suggests.* The fleet's planes are Singer sets. Their circulant spectrum (|D^(χ)|^2 = q, derived) gives
  ext_q(W) ≲ q^3/W. Arcs, conics and unitals give lower constructions. The min-max of L-meta-715 becomes computable.
- *Next.*
  - (i) Exact ext_q(W) for q ≤ 9 by ILP against the spectral bound.
  - (ii) Lean the two witness sets of 660 (order 8) and 661 (order 7) as decidable checks.
  - (iii) For odd q, the blocking-set dual by Rédei polynomials.

**8. AG-03: linear spaces on {p_2 = p_3 = 0} and the order-4 layer of the core.**
- *What it suggests.* A stability theorem for p_2 = p_3 (the analogue of Codex's p_2 = p_4 theorem) would make a near
  n²/3 core a direct sum of triple lines. The identity of L-gct-134 then becomes a placement problem on the grid.
- *Next.*
  - (i) Prove the stability theorem.
  - (ii) Compute the largest triple-line sums inside DC_n that kill the 134 quartic, n ≤ 8, against F_4 ∩ DC
    (dimension n(n−1)/4).

**9. ANT-08: Koiran's HN in AM and the dihedral GL_2 rung.**
- *What it suggests.* CX-K01 (checked by us) localizes Koiran's analytic input to RH(ζ_E), with E the solution field.
  For E = Q(2^{1/3}), ζ_E = ζ · L(ρ_2), with ρ_2 induced from a cubic character of Q(ω). That L-function is a dihedral
  weight-one GL_2 object, the same rung as ALP_CONNES's gate H04.4 (F = Q(∛269)) and ALP_MACHINE Q3. Part B §1.
- *Next.* State "HN for systems with dihedral-cubic solution fields is in AM" as a consequence of RH for
  finite-order Hecke characters of imaginary quadratic fields. That isolates the exact next-rung input.

**10. HT-04: hard Lefschetz against GCT positivity.**
- *What it suggests.* H23 (the unimodality clause of GCT VIII's Positivity conjecture fails at r = 3) excludes any
  polarized Lefschetz module with those graded dimensions. Q4-PRIMITIVE and QNEW-SATAKE (GCT_NSRH) are the positive
  side: pure Tate realizations.
- *Next.*
  - (i) State H23 as a no-Lefschetz-realization theorem.
  - (ii) List which multiplicities in the L-gct-011 obstruction searches lie in Q4-PRIMITIVE's scope.

**11. HT-07: c_t as a complexity measure.**
- Part B §6 sets c_t (HODGE_FINISH) beside border complexity in GCT. They share the closed-sublevel and Baire
  mechanism.
- *Next.* Define the analogous "witness-degree" of a non-membership paddedPerm ∉ orbitClosure(det), and prove its
  semicontinuity and dichotomy in the form of HODGE_FINISH Q05.

**12. AG-04: E's ideal certificates (NN-C029, NN-C021).**
- *What it suggests.* There is a separation between IPS size and monomial-PC size on one family. On the algebraic
  side it is a degree/size trade-off for Nullstellensatz multipliers.
- *Next.* Separate the multiplier degree (≤ v) from the circuit size S(v). Is there a family where degree-v
  Nullstellensatz needs 2^{Ω(v)} monomials but E's circuits are 2^{o(v)}? NN-C021 gives this for resolution and PC;
  the question is whether it holds for the same CNF family.

**13. ANT-07: Lenstra's construction problem and succinct planes.**
- *Next.* Write the succinct PG(2, p^r) language with `thm:small-cyclotomic-cofactor` (P128) or P126. The uniform gate
  is GRH_ALGORITHMS Q01.

**14. HT-03: Lorentzian polynomials and Hessian signatures.**
- *Next.* Test numerically whether x ↦ perm(Σ_σ x_σ P_σ) is Lorentzian for n ≤ 5. If it is, the Brändén-Huh
  inequalities give constraints on subpermanent sums on the Birkhoff cone.

**15. HT-05: Hodge loci through Fermat varieties.**
- arXiv:2112.14818 (abstract read): fake linear cycles exist only in degrees 3, 4 and 6; the minimal component of the
  Hodge locus parametrizes hypersurfaces containing linear subvarieties of dimension n/2.
- *Next.* Compute the first-order IVHS condition for the triple-line subspaces under the deformation (p_2, p_3) →
  (p_2, p_3, S_4 − (3/2)p_4).

**16. AG-06: reduction mod 2 for L-gct-025.**
- *Next.* Search integer substitutions of det over F_2 for smooth forms with (r−1)(d−1) > 121k, with homogeneous lifts.
  Audit the September manuscript for characteristic-2 vanishing. P90a shows where such vanishing fails.

**17. AG-10: algebraic extremal graphs.**
- *Next.* A K_{s,t}-free version: |E| + bc(G) − 1 for monotone circuits, carried by projective norm graphs.

**18. ANT-01: Cauchy-Davenport onto L-gct-117.** Next: the Lean proof via `ZMod.cauchy_davenport`.

**19. ANT-05: Legendre onto L-gct-127 and 149.** Next: the Lean proof via `Nat.sub_one_mul_sum_div_pow_eq_sub_sum_digits`.

**20. ANT-06: the binomial idempotent onto L-clb-033.**
- P_k = Σ_{i≥k} C(2k−1, i) x^i (1−x)^{2k−1−i}. It is the polynomial form of Hensel lifting an idempotent.
- *Next.* The Lean proof.

**21. AG-07: integral orbit closures (ALPOGE_GCT B7).** Next: the converse of L-gct-006, and B7's witness-degree gate.

**22. AG-08: Ax-Katz and AC0[p].** Next: the top coefficient of an AC0[2] approximator, compared with
`smolensky_card_le`.

**23. AG-09: Newton bases for DIV (S20).** Next: ranks of [h_{e−k}(−1, …, −k−1)] on the certified instances.

**24. ANT-12: p-adic discs for DIV.** Next: the valuations of binomial moments for L-gct-132 and 147.

**25. HT-06: purity → character sums.** Next: carry the Weil bound for curves as a cited input of a Paley-type clb node.

**26. ANT-10: PIT with cyclotomic constants (NN-C048, NN-C049).** Next: a new node, ZPP under A.

**27. ANT-11: small bias from quadratic characters (CUE_GCT P-02).** Next: a character sum that fools one exact
threshold atom.

**28. HT-08: spectrum semicontinuity for L-gct-028.** The sources still have to be opened. Next: the spectrum of
perm_3 and perm_4 at a zero.

**29. ANT-13: E against FP3 (L-lib-123).** The work is all on the machine side.

**30. ANT-14: H15 enumeration.** A time bound from the explicit c_g.

**31. ANT-15: H27 and ZETA_HEAT spectra.** No fleet node.

**32. AG-11: anabelian and motivic rows.** No fleet node, except through AG-05.

**33. HT-07 second half: S07b.** A halting-set Hodge pair. A computability node only.

(All 34 ids appear above: #2 joins HT-02 and ANT-09, #7 joins ANT-04 and AG-01, and #11 and #33 split HT-07.)

---

## Part B. Structural note: how AG, Hodge theory and ANT carry A towards global Langlands

### B.1 The ladder over Q, and where each of our results stands

| rung | automorphic object | motivic/Galois object | our results on this rung (locators) | what A does here |
|---|---|---|---|---|
| GL_1 over Q | Dirichlet characters | Artin characters of abelian fields; μ_n | GRH_ALGORITHMS classical table (Miller, r-th nonresidues, primitive roots, least primes in progressions), P074/P092 averages (checked by us), P128/P131/P145 (unconditional; their mechanism is cyclotomic projection); CX-N01-N04, N13; CX-K01/K03 (HN ∈ AM for abelian solution fields); H15 (A excludes the exceptional zero in the averaged Colmez estimate); ALP_CONNES T51 (A ⟺ the cutoff trace formula); ZETA_HEAT and NEG A-rows (zeros of ζ and L(χ) under deformation); on the fleet side ANT-01, 03, 04 (characters of Z/p: GL_1 over F_p, the local avatar) | A is the input |
| GL_1 over a number field K | Hecke characters of K | Artin characters of abelian extensions of K | GRH_ALGORITHMS P001: under A, RH(ζ of Q(p^{1/r})) ⟺ RH(ζ of Q(ζ_r, p^{1/r})); ζ_E = ζ_K (ζ_F/ζ)^{r−1}, with the gate one induced order-r Hecke character over Q(ζ_r) (Q02 open); ALP_MACHINE Q3 (Kummer Hecke character over Q(ω)); the HODGE Weil engine (Part B §2.3: the extraction projector separates algebraic Hecke characters of K by infinity type) | A covers only the characters factoring through the norm to Q (CX-R02: the permutation representation of Q(2^{1/3}) is not a virtual sum of rank-one characters of Q) |
| GL_2 over Q, weight 1, dihedral | theta series of Hecke characters of imaginary quadratic K | 2-dimensional Artin representations induced from K | ALP_CONNES gate H04.4 (RH for ζ_F/ζ, F = Q(∛269); K-groups of Q(ω, ∛269) computed, AC-G22, K12, K21-K23 checked by us); CX-K01 for non-abelian cubic solution fields; Koiran's HN for dihedral fields (Part A #9) | not enough: A gives the GL_1 over Q factors only |
| GL_2, weight ≥ 2, CM | theta series of algebraic Hecke characters | CM elliptic curves; the Weil planes W_K at CM points | HODGE_FINISH Paper A (bounded division at CM points is equivalent to the Hodge conjecture for abelian varieties; Q01, checked at the deductions); HECKE_DIV R24E; THETA3 C32 (a Weil cycle on a Q(i)-Weil fourfold, Schoen's method) | the CM points enter via Shimura-Taniyama; A enters H15's orbit bound |
| higher rank: unitary groups, theta lifts | definite unitary groups, seesaws | CM abelian varieties of dimension r^{b−1} | Alpöge's proof itself (a chain of theta lifts; ALP_MACHINE LIFT054-055: size floors m > 2^7778; LIFT077: central values of Ichino-Ikeda/GGP shape); GRH_ALGORITHMS P125/P126 (under A, Frobenius polynomials of CM abelian varieties of dimension r^{b−1} by Pila's algorithm); THETA3 (the seesaw between signature (2,1) and the definite groups, open at the MainX gate) | A is proved by going up this rung and coming down |
| trace formula | Weil explicit formula, Connes's cutoff trace | Lefschetz/Grothendieck trace formula on curves and hypersurfaces | ALP_CONNES T51 (checked at the deduction), S50 (credited to Suzuki 2610.32704); NEG NN-C026 (the H^1 trace q − 2#SAT); NN-C023/C024 (coherent Frobenius trace) | T51 is equivalent to A |

The pattern: our analytic results sit on GL_1 over Q. Every gate one rung up is a finite-order Hecke character of a
non-abelian-over-Q field, in practice a cubic character of Q(ω) or Q(ζ_r): GRH_ALGORITHMS Q02, ALP_MACHINE Q3,
ALP_CONNES H04.4, CX-R02 and CX-K04. Through automorphic induction that is a weight-one dihedral GL_2 form. Three
separate runs reached this same next rung from three directions: algorithms, the Connes trace formula and Alpöge's
machine. **The concrete next-rung statement they share:** RH for L(s, ψ) with ψ a cubic Hecke character of Q(ω) of
small conductor (ALP_CONNES: F = Q(∛269); GRH_ALGORITHMS: the order-r character over Q(ζ_r) attached to p^{1/r}).

### B.2 Thread 1: the period-domain picture of the level-space core, read on the automorphic side

**Objects.** DC_n = V ⊗ V, with V the sum-zero vectors in C^n, of dimension N = (n−1)^2. On DC, S_2 = p_2/2 and
S_3 = (2/3)p_3 (fleet checked L-gct-105, 106), and 24 S_4 is the expression of L-gct-134. G = S_n × S_n ⋊ ⟨transpose⟩
acts on DC, preserving p_2 and every S_k.

**B.2.1 Hodge-theoretic reading (derived here).** p_2 restricted to the real points DC_R is the Euclidean norm. An
isotropic K ⊂ DC_C therefore has K ∩ K̄ = 0 (x ∈ K ∩ K̄ gives p_2(x, x̄) = |x|^2 = 0), so
DC_C = K ⊕ (K ⊕ K̄)^⊥ ⊕ K̄. This is a weight-2 Hodge structure with h^{2,0} = k, polarized by a definite form. The
space of such structures is the whole isotropic Grassmannian OG(k, N) = SO(N)/(U(k) × SO(N − 2k)), with Hodge bundle
F^2 = S (the tautological bundle). The level conditions are sections S_j|_K ∈ H^0(OG, Sym^j S^*), and the core bound of
L-gct-086 is the largest k for which their common zero locus is nonempty.

**The Shimura side.** For the definite form, OG is the compact dual. The non-compact period domains appear only after
changing the real structure.
- At k = 1, OG(1, N) is the quadric, the compact dual of the orthogonal Shimura varieties SO(2, N − 2) (K3 type).
- At k = N/2 it is SO(N)/U(N/2), the compact dual of the type D^H domain SO^*(N)/U(N/2).

The intermediate k are not Hermitian symmetric, the usual situation for weight-2 period domains. What carries over
intact is the notion of a **special point**: a K fixed by a torus of the symmetry group, i.e. a sum of eigenlines.

**B.2.2 Special points of the core problem.** Let T be a torus (or a finite abelian group) acting by isometries of
(DC, p_2). If g is an isometry, x is a λ-eigenvector and y a μ-eigenvector, then p_2(x, y) = p_2(gx, gy) =
λμ p_2(x, y). So eigenvectors are orthogonal unless λμ = 1. Hence a T-fixed point of OG is a choice of one eigenvalue
from each pair {λ, λ^{−1}}, together with isotropic pieces of the self-dual eigenspaces. If moreover g preserves every
S_k (g ∈ G), then on the ω-eigenspace S_k(t) = S_k(gt) = ω^k S_k(t), so S_k vanishes there unless ω^k = 1. **This is
the Weil-type mechanism.** On an abelian variety with an action of an imaginary quadratic K, the eigenspaces of
a ∈ K are isotropic for the polarization (E(ax, ay) = Nm(a) E(x, y)), and the Weil classes live in the top exterior
power of one eigenspace. The fleet's checked L-gct-119 (t(σi, τj) = z t(i, j) with z^k ≠ 1 for k ≤ n implies t is
level) is the same statement, and so are the barrier families F_q of gct.md 5.1(c): F_q is the ω-eigenspace of the
row permutation that cycles each block of q rows.

**Proposition B.2 (derived here; computation checked).** Let g = (σ, τ) ∈ S_n × S_n act on n × n matrices by
(gt)(i, j) = t(σ(i), τ(j)), and let ω be a root of unity of order q > n. Then E_ω(g) = {t : gt = ωt} is a level space
(L-gct-119), and

  dim E_ω(g) = Σ over pairs (a cycle of σ of length a, a cycle of τ of length b) with q | lcm(a, b) of gcd(a, b)
             ≤ n^2/q < n.

*Proof.*
1. The ⟨g⟩-orbits on [n] × [n] coming from cycles of lengths a and b are gcd(a, b) orbits, each of length lcm(a, b).
2. The permutation representation on an orbit of length ℓ is the regular representation of Z/ℓ, which contains each
   ℓ-th root of unity exactly once. So ω occurs there iff q | ℓ.
3. gcd(a, b) = ab/lcm(a, b) ≤ ab/q whenever q | lcm(a, b), and Σ ab = n^2.

*Check.* For n = 4, 5, 6 and random σ, τ, the dimension of the null space of g − ω agrees with the formula, and
max_{k≤n} |S_k| on a random element is below 10^{−14} (script `scratchpad\sp\eig.py`, in the work file).

*Meaning.* Single-symmetry special points with eigenvalue order above n are level, and all have dimension below n. The
fleet's floor 2n − 3 (L-gct-080) and the checked LS(4) range 5-6 (L-gct-214) lie above every such point. Truncated
families (q ≤ n) need the extra vanishing of S_q, S_{2q}, … that gct.md 5.1(d) organizes as a hyper-permanent.
**So on the automorphic side, the extremal level spaces are not CM points but deformations of sums of them.** The next
statement is a deformation statement: how far can a level space be from the span of special points, measured by the
defect of Codex's prime-power theorem (dim L ≤ (n−1)(r+1))?

**B.2.3 The Weil engine in the same language (from HODGE_FINISH Q02 and HECKE_DIV R24E).**
- For a ∈ K acting on a Weil 2n-fold of signature (n, n), H^1 ⊗ C = V_a ⊕ V_ā with dim V_a = dim V_ā = 2n.
- The Weil plane is ∧^{2n}V_a ⊕ ∧^{2n}V_ā, on which a acts by a^{2n} and ā^{2n} (R24E).
- The extraction polynomial P(S) = ∏(S − β_j), with S = a^* + ā^* and β_j = q^j(a^{2n−2j} + ā^{2n−2j}), kills the
  other eigen-types of ∧^{2n}H^1.

At a CM point these eigenvalues are values of algebraic Hecke characters of K with infinity types (2n−2j, 2j) (the
Shimura-Taniyama dictionary; not reopened here). So the extraction projector is a projector in the Hecke algebra
separating Hecke characters by infinity type: a GL_1-over-K operation. The level-core picture has the same shape with
the cyclic group ⟨g⟩ in place of K^×: an isotropic eigenspace selected by a character, and invariants of degree k
seeing χ^k.

**Dictionary.**

| level spaces (GCT, L-gct-086) | Weil classes (HODGE) |
|---|---|
| DC_n with the definite form p_2 | H^1 with the polarization E |
| finite symmetry g ∈ S_n × S_n | CM endomorphism a ∈ K |
| ω-eigenspace, isotropic | V_a, isotropic |
| S_k vanishes when ω^k ≠ 1 | Hodge type forced on ∧^{2n}_K |
| F_q barrier families | Weil classes on CM points |
| 2n − 3 floor: not a special point | Hodge classes at non-CM points: bounded division (Q01) |
| "distance to a special point" bound (open) | c_t bounded on CM points ⟺ everywhere (Q01, Baire) |

The right column has a theorem (HODGE_FINISH Q01: bounded on one dense set ⟺ bounded everywhere) whose left analogue
is not available, because level spaces do not form a family with a dense set of special points in any sense yet set
up. **Statement to try:** the set of k-dimensional level subspaces of DC_n is a closed subvariety Z_k of OG(k, N),
stable under G. Do the G-torus-fixed points meet every component of Z_k? If yes, a bound on special points (with
truncation) plus a semicontinuity argument bounds Z_k.

### B.3 Thread 2: Hasse-Witt and Frobenius traces as GL_1 and GL_2 data

**Objects (NEG_NIGHT, checkpoint 15).**
- NN-C023: Φ ↦ F, a form of degree r in r variables over F_2, with H^{r−2}(X, O) = F_2 and Frobenius = #SAT(Φ) mod 2.
- NN-C024: the pencil F_u = Σ z_i^r + uF, smooth over F_2(u), with Frobenius uc.
- NN-C026: a curve with #C(F_q) = 1 + 2#SAT and pure H^1 of trace q − 2#SAT, of exponential genus.
- NN-C005: N mod 2 = [x_1⋯x_n] ML(∏(1 + f_i)), with Katz's "On a theorem of Ax" as the input.
- The trace and point-count congruence is SGA 7 XXII 3.1-3.2, as NEG_NIGHT locates it.

**The GL_2 reading.**
- For an elliptic curve E/F_p, #E(F_p) = p + 1 − a_p, and the congruence gives #E(F_p) ≡ 1 − h mod p, with h the
  Hasse-Witt scalar. So h = a_p mod p: the Hasse-Witt scalar is the mod-p reduction of the GL_2 Hecke eigenvalue
  when E is modular.
- NN-C023 is the same statement for the top coherent line of a hypersurface, i.e. for the "Hodge level zero" piece of
  its motive. It places #SAT mod 2 there.

**The GL_1 reading.**
- At u = 0 the pencil is the Fermat hypersurface. Its symmetry μ_r^r splits the cohomology into characters of μ_r^r.
  On the ℓ-adic side these are Jacobi-sum Hecke characters of Q(ζ_r) (Weil's dictionary; not reopened here).
- NN-C024 deforms away from this CM point in the direction F, and the parity of #SAT is the first-order coefficient
  of that deformation on one character line.
- **Statement to compute:** the μ_r^r-character χ_top of H^{r−2}(X_0, O). Show that the scalar uc is the derivative,
  at u = 0, of the Frobenius on the χ_top-line. This would make "#SAT mod 2" a first-order deformation coefficient of
  a Jacobi-sum motive.

**Where the hardness lives (our sources, side by side).**

| bounded rank, growing p | growing rank, succinct presentation |
|---|---|
| GRH_ALGORITHMS P125/P126: CM abelian varieties of dimension r^{b−1}, Frobenius polynomials by Pila's algorithm in (log p)^{c_{r,b}} | NN-C026: genus exponential, trace #P-hard |
| the automorphic object: one Hecke character or one GL_2 form; a_p in poly(log p) for fixed data is what P125 uses | NN-C023/C024: the Frobenius on a one-dimensional coherent piece, ⊕P-hard; smooth inputs give ⊕P ⊆ BPP ⇒ NP = RP |
| A controls zero locations | NEG primer: "A controls the zeros of ζ_X(s) = ζ(s − v − h) ζ(s − h)^N; the counting difficulty is the multiplicity N" (NN-C027) |

So purity and RH fix where the spectrum lies; the count N sits in the multiplicity, which no positivity sees. On the
automorphic side, NN-C027's motive is a sum of N copies of one Tate motive: the GL_1 rung, with multiplicity N.
Computing N from a succinct presentation is the hard operation. **Next statement:** for families of motives of rank R
presented by formulas of size s, is the trace mod 2 computable in poly(s, R, log q)? NN-C026 shows the answer must use
R (rank exponential in s gives #P-hardness). The question is the polynomial-rank regime.

### B.4 Thread 3: Chebotarev and Fourier minors as character sums at the GL_1 rung

**Proof of Chebotarev's theorem through the Weyl dimension formula (derived here).**
1. Let p be prime and ζ a primitive p-th root of unity. Take distinct a_1, …, a_k and distinct b_1 < … < b_k in
   [0, p). Put x_i = ζ^{a_i}.
2. Then det(x_i^{b_j}) = a_δ(x) s_λ(x), with a_δ the Vandermonde (nonzero, since the x_i are distinct) and s_λ the
   Schur polynomial, λ_j = b_{k+1−j} − (k − j).
3. Modulo 𝔭 = (1 − ζ) every x_i ≡ 1, so s_λ(x) ≡ s_λ(1^k) = ∏_{i<j}(b_j − b_i)/(j − i), an integer.
4. Its numerator factors lie in (0, p) and its denominator factors in (0, k), with k ≤ p. So it is prime to p, hence
   not in 𝔭 ∩ Z = pZ. So s_λ(x) ≠ 0 and every k × k minor of (ζ^{ab}) is nonzero.

*Structure.* The minor is the character of the GL_k representation of highest weight λ, evaluated at a torus element of
order p, times the Weyl denominator. The prime of Q(ζ_p) above p sends that torus element to the identity, and the
character at the identity is the dimension. This "trace at the identity" step is the same move as the
identity-contribution term of a trace formula. In 211's proof it is the strictly smaller p-adic valuation of the
single-block term (gct.md 5.3), where (1 − ζ)-adic valuation kills everything except the identity class.

**Where it sits.**
- The row-shift decomposition L = ⊕_χ L_χ (ANT-03), the Fourier-mode level sets (L-gct-117 via Cauchy-Davenport) and
  the Singer spectrum |D^(χ)|^2 = q (ANT-04) are all statements about characters of Z/n or of F_q^×: GL_1 over F_p.
- The global GL_1 rung they lift to is Dirichlet characters, where A lives. The cyclotomic ring Z[ζ_r] and its prime
  above p are the same objects GRH_ALGORITHMS manipulates in 𝒟 = F_p[Z]/Φ_r(Z): the Teichmüller unit η with
  σ_c(η) = η^{ω(c)} (`thm:teich`) is an eigenvector of Gal(Q(ζ_r)/Q) with the character ω.
- So both the 211 argument and Lenstra's construction select a Galois or shift eigenvector and use the prime above p
  to read it.

**Next rung, as a concrete statement.** Replace Z/p by a ray class group of an imaginary quadratic K: the "Fourier
matrix" of characters of Cl_𝔪(K) evaluated at prime ideals. Its minors control the uniqueness of Hecke-eigenvector
decompositions. The question: are all minors of the character table of Cl_𝔪(K), restricted to the classes of degree-1
primes below x, nonzero once x exceeds a polynomial in log |disc|? A for K-characters factoring through Q gives the
abelian-over-Q part; RH for Hecke characters of K would give the rest.

### B.5 Thread 4: Mahler measure and heights against L-values

**DIV and the Γ-factor (derived here).** The divisor of the DIV hypotheses is the rising factorial
(X+1)_N = Γ(X + N + 1)/Γ(X + 1). Its roots −1, …, −N are poles of Γ(X), and its Mahler measure is
∏ max(1, j) = N! = Γ(N + 1). ANT-02's inequality reads

  log Γ(N + 1) ≤ log M(F) ≤ log K + M log(T H):

an archimedean local factor bounded by a height. In the zeta function the poles of Γ(s/2) give the trivial zeros. So
DIV asks how many of the "trivial-zero positions" a short sum of M-th powers of sparse polynomials can hit, and the
Mahler bound answers it whenever the height is small.

**Heights against L-values in our runs.**
- H15 (hexagon note, not posted): |Gal x| ≥ c_g |disc R_x|^{1/(4g)}. Its proof combines Gaudron-Rémond's isogeny
  bounds with the averaged Colmez formula. A is used once, to exclude an exceptional real zero in the height estimate.
  The averaged Colmez formula expresses an average Faltings height through logarithmic derivatives of Artin
  L-functions at s = 0, a GL_1-rung input when the relevant characters are odd Dirichlet characters.
- HECKE_DIV A2: h(E_{7^r}) = h(E) + (r/2) log 7 along a fixed-field orbit.
- The Hodge Poincaré-pairing bound (HODGE_FINISH Q01 step 4): M^2 q_t ≤ C(2d, d)(deg Z^+ + deg Z^−)^2. This is a
  degree-height inequality whose positivity is Hodge-Riemann.

**Side by side.**

| DIV (fleet) | CM orbits (H15) | bounded division (HODGE) |
|---|---|---|
| count: N roots at −1..−N | count: orbit size \|Gal x\| | multiplier M |
| archimedean size: N! = M(∏(X+j)) | Faltings height | degree of cycles |
| upper bound: \|\|F\|\|_1 ≤ K(TH)^M | Colmez: L'/L at 0 | C(2d, d)(deg)^2 |
| where A enters: not at all (the bound is height-only); next: the height of the permanent reduction | excludes the Siegel zero | not used |

**Next statement.** A height-free DIV would need an arithmetic input replacing the height: the p-adic disc counts of
ANT-12 are the non-archimedean analogue, with the product formula tying the places together. Concretely: for
F ∈ Z[X] divisible by (X+1)_N, Σ_p (number of roots in Z_p-discs, weighted by log p) relates to log N! by the product
formula. Compute this for the fleet's certified instances L-gct-132, 147.

### B.6 Thread 5: the same mechanism in complexity and in arithmetic

| mechanism | arithmetic/geometric instance | complexity instance | dictionary |
|---|---|---|---|
| **closed sublevel sets + density** | HODGE_FINISH Q01 / HECKE_DIV R21: {c_t ≤ C} is Zariski closed (bounded Hilbert schemes, SGA 6 XIII 6.11); bounded on a dense set (CM points, a Hecke orbit) ⟺ bounded everywhere, by Baire | GCT: border complexity has closed sublevel sets (orbit closures; L-gct-006: an expression puts the padded permanent in the orbit closure; the converse via `hasBorderDetExpression_bind₁`, MAPPING_OUR_RESULTS 1.1) | c_t is the "border complexity of a Hodge class": the least size of an algebraic witness. Both use a semicontinuity to pass from a dense set to the closure |
| **char 0 against char p** | HODGE_FINISH Q05 dichotomy: the minimum degree at reductions equals the char-0 minimum outside finitely many v, or tends to ∞; P6 lifting | ALPOGE_GCT B7.1 (a char-0 separation survives at almost all p), B7.3 (a char-2 separation need not lift); over F_2, perm = det (AG-06) | specialization of algebraic witnesses; both sides have "finitely many bad primes" theorems |
| **eigenspace isotropy** | Weil classes (B.2.3); Teichmüller units σ_c(η) = η^{ω(c)} (GRH_ALGORITHMS `thm:teich`); Kummer theory | F_q barrier families, L-gct-119, Proposition B.2; 211's row-shift decomposition | a cyclic group acts, a character selects an isotropic eigenspace, a degree-k invariant sees χ^k |
| **positivity bounding isotropic dimension** | Hodge-Riemann in the Poincaré-pairing bound; Weil positivity W(f ∗ f^*) ≥ 0 (ALP_CONNES T51 ⇐, via Connes-Consani-Marcolli) | real level spaces ≤ p + q − 2 (L-gct-158); the real case of 036/037 (signature (2m−3, (m−1)^2)); Lemma K (definite form on the stabilizer) | the excess escapes into the non-real part: the complex core has K ∩ K̄ = 0; Weil classes are where divisor positivity does not detect (R24E) |
| **trace with the count in the error term** | Weil purity: #C = q + 1 − tr with \|tr\| ≤ 2g√q; S50: finite compressions recover the multiplicities | NN-C026: #SAT sits in tr when g is exponential; E counts exactly in 2^{o(n)} | the main term is free, and the count is the multiplicity (NN-C027) |
| **lifting to prove a lower-rank statement** | Alpöge: RH for GL_1 via theta lifts on definite unitary groups (ALP_MACHINE LIFT054-077); THETA3 seesaw | pcx: lower bounds for Res(⊕) via the IP lift (L-pcx-065, 072); Line E: the Kronecker substitution x_j → X^{2^j} (L-gct-149) | a quantity on the small side equals a pairing on the large side; the cost is a size floor (ALP_MACHINE: m > 2^7778; pcx: the gadget's 4 bits per variable) |
| **trace at the identity** | Chebotarev via the Weyl dimension (B.4); the identity term of a trace formula | 211's p-adic single-block step; Lemma K's stabilizer decomposition (only the identity block survives the pairing) | reduction at the prime above p collapses a torus element to 1 |

### B.7 What it suggests, most promising first

1. **Special points and deformations of level spaces.**
   - Prove Proposition B.2 with transposition included.
   - Then the statement of B.2.3: Z_k = {k-dimensional level subspaces} ⊂ OG(k, N) is closed and G-stable. Do
     G-torus-fixed points meet every component?
   - Compute this for n = 4 (where κ(4) = 3 and LS(4) ∈ {5, 6} are on the board).
2. **The common next rung.** RH for a cubic Hecke character of Q(ω) (ALP_CONNES H04.4 with F = Q(∛269);
   ALP_MACHINE Q3; GRH_ALGORITHMS Q02). Consequences that follow by our checked mechanisms once it holds:
   - Koiran's HN ∈ AM for dihedral-cubic solution fields (CX-K01);
   - the auxiliary prime of P001 at r = 3;
   - cubic fields in poly(log p) with no valuation restriction at r = 3, through P001 (to be traced against
     GRH_ALGORITHMS Q01).
3. **Hasse-Witt as a deformation coefficient.**
   - Compute χ_top and the first-order Frobenius derivative for the Fermat pencil of NN-C024.
   - Then the polynomial-rank question of B.3.
4. **Chebotarev for class groups** (B.4, next rung). Nonvanishing of minors of Hecke-character tables at small primes.
   This is the class-group analogue of 211's input.
5. **Heights.**
   - The height regime of the fleet's DIV reduction (B.5).
   - The product-formula form of the disc count.
6. **c_t as a complexity.** Define a witness degree for paddedPerm ∉ orbitClosure(det). Prove its Q05-type dichotomy
   across primes, using B7.1/B7.3.
7. **Theta characteristics for L-pcx-071** (Part A #6): the maximal affine families of odd characteristics in genus 2k.

Check events (statement id, date, who, type, outcome):
- Proposition B.2, 2026-11-23, Claude Opus 5.5 at effort high (agent a11adac491e93d1d6): first proof in this run plus
  computation (n = 4, 5, 6, random σ, τ; dimension formula and vanishing of S_1..S_n to 10^{−14}). Outcome: proved on
  paper and agrees with the computation; no second reader yet.
- Chebotarev via the Weyl dimension (B.4), same: first proof in this run, paper.
- DIV/Γ reading (B.5) and Weil-engine eigenvalue reading (B.2.3), same: derivations from the cited statements, paper.
- The run results cited (P001, P125/P126, NN-C005/C023/C024/C026/C027, Q01, Q05, T51, CX-K01, CX-R02): carried as
  background with the check levels the primers record.
