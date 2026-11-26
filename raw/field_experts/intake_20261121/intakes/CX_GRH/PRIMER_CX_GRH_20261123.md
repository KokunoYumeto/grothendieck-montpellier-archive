# Primer: CX_GRH (prompt 28), "GRH and ETH in complexity: Koiran, GCT V"

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7). It is a recall of the run and of our
intake; nothing new.

**The run and its final.** GPT-6 Astra (ChatGPT Pro mode), final of 21 Nov 00:05 UTC. The paper is
`research_returns\CX_GRH_final_20261121T0005Z_unzipped\CX_GRH.tex` (3,867 lines); line numbers below refer to it.

**Our intake.** `intakes/CX_GRH/INTAKE_CX_GRH_20261121.md`, 21 Nov, by Claude Opus 5.5 at effort high (agent
af2a18f62da23b48e). Of 39 findings, 21 were confirmed with every step checked, four of them as transfers of cited
theorems; 18 were read at statement level; there were no gaps or refutations.

**Inputs.**
- A: Alpöge's theorem, RH for every Dirichlet L-function. It gives RH for ζ_K with K/Q abelian.
- M: GRH for the Hecke L-functions concerned. This was Masullo's claim; his draft is not a proof, so M is an open
  hypothesis.
- E: the outside input refuting ETH, OpenAI's preprint.

## 1. Which Riemann hypothesis each algorithm needs
**CX-R01** (l. 163-192), A and M: A gives RH for every abelian Dedekind ζ_K, through ζ_K = ∏_χ L(s, χ) (Washington,
Theorem 4.3; the imprimitive factors have extra zeros only on Re s = 0). M gives RH for ζ_K and every finite-order Hecke
L-function of every K.

**CX-R02** (l. 194-219), no input: the permutation representation of Q(2^{1/3}) is not a virtual sum of rank-one
characters.
- Mechanism: every rank-one character is 1 on the commutator c of lifts of (12) and (23); the trace of c is 0, not 3.
- Use: A alone does not reach ζ of a non-normal cubic field.

**CX-K04** (l. 515-534), no input: x³ − 2 has no root in any abelian extension of Q. A non-normal cubic field cannot
lie in an abelian extension. So "bounded abelian witnesses" cannot cover all of Koiran's systems.

## 2. Koiran's Nullstellensatz in AM, and GCT V
**CX-K01** (l. 339-431): Koiran's analytic input localizes to RH for ζ_E, with E the field of his bounded solution. No
Galois closure is needed.
- Lemma: Lagarias-Odlyzko 1977, Theorem 1.1, applied to the trivially Galois extension E/E. That is the prime-ideal
  theorem under RH(ζ_E).
- Proof: degree ≥ 2 primes cost ≤ d√x, and each rational p carries ≤ d primes. With log D_E and d ≤ 2^{q(N)}, and
  x = 2^{P(N)}, the main term Li(x)/d beats every error and Koiran's Theorem 5 bound for inconsistent systems. The
  primes found keep polynomial bit length.
- Use: Hilbert's Nullstellensatz (HN) ∈ AM needs one solution-field zeta function, which A gives when E is abelian.

**CX-K02** (l. 433-478), under M: HN for circuit systems and for nonzero homogeneous points is in AM ⊆ Π₂P, by gate
variables and the normalization Σ u_i x_i = 1.

**CX-K03** (l. 480-508), under A: the promise problem with explicitly bounded abelian witnesses is in AM (K01 + R01).

**CX-K05** (l. 540-638), under M: a homogeneous system of parameters (h.s.o.p.) of linear forms for an equation-given
standard-graded cone is constructible in FP^{Σ₂P}; unconditionally it is in PSPACE.
- Mechanism: Good(I, L) is the complement of K02's AM predicate, so it lies in co-AM ⊆ Σ₂P. Then a prefix search, with
  the graded Krull bound dim R/(L) ≥ d − s > 0 for s < d.
- Use: it sharpens GCT V, Theorem 3.4, from "PH" to a level.

**At statement level:**
- CX-K06: GCT V Theorems 4.10 and 5.12 transfer under M; Theorems 4.1 and 5.5 keep their access hypothesis.
- CX-K07: small separating systems already have unconditional PSPACE constructions (Forbes-Shpilka, Theorem 7.1;
  Guo-Saxena-Sinhababu 2019, Theorems 1.5-1.6). This is a credit correction.

## 3. Number-theoretic algorithms
**From A alone:**
- **CX-N01** (l. 793-829): Miller's test with Bach's cutoff is deterministic polynomial; quadratic characters suffice
  (Schoof 2008, Theorem 2.2; Bach 1990, Theorem 2).
- **CX-N02** (l. 831-854): for a specified r | p−1, an r-th nonresidue in F_p in poly(log p).
- **CX-N03** (l. 856-879): a primitive root of F_p given the factorization of p−1, as a product of primary components.
- **CX-N04** (l. 881-901): Shoup's least primitive root O((log p)⁶) gives a candidate list.

**CX-N13** (l. 1386-1480), under A: for a specified r | p−1, an r-th nonresidue in any supplied F_{p^m} in poly(m log p).
For r = 2 and m even it is unconditional (BIMS17, Corollary 1.3; also GRH_NIGHT CX-ALG-018).
- Proof for r ∤ m: the constant a works, since ζ^m ≠ 1.
- Proof for r | m, r odd: there is a nonzero u with u^Q = ζu, since ζ lies in the image of v ↦ v^{Q−1}. Then
  S = 1 + Q + … + Q^{r−1} ≡ r mod r², so u^{(p^m−1)/r} = ζ.

**CX-N14** (l. 1483-1789): in a split algebra F_p^d with an automorphism τ of order h and a prime r | h, a zero divisor
is found in poly(d, log p) in three cases.
- (i) p ≤ d.
- (ii) r | p−1, under A: τ(z^r) = z^r, a τ-invariant r-th root y exists (Gao, Lemma 2.6), and ∏(z − ζ^j y) = 0 with no
  factor zero.
- (iii) v_r(p^s − 1) = 1, unconditionally, via IKRS Proposition 4.6 and Lemma 4.2.
- Counterexample to dropping (iii), checked by hand: p = 17, r = 3, with ord₃ 17 = 2 and v₃(288) = 2.

**Under M:**
- **CX-N11** (l. 944-1041): RH for ζ_Q and for ζ_E, E = Q(ζ_{2n}, p^{1/n}), gives a prime q = O(n⁴ log²(np)) with
  q ≡ 1 mod 2n and gcd((q−1)/ord_q p, n) = 1.
  - Mechanism: Eisenstein at the primes above p. The class of σ (σ(α) = ζ_n α) is conjugation-stable
    (τστ⁻¹ = σ^u), and Frobenius σ^u gives p^{(q−1)/n} = ζ_n^u of order n. The discriminant is O(n² log(np)), and
    Bach-Sorenson, Theorem 5.1, finishes.
- **CX-N15** (l. 1792-2077): complete deterministic factorization over F_q in (d^{log d} log q)^{O(1)}. The analytic
  input is exactly RH for ζ_Q and ζ_{Q(ζ_{2ν}, p^{1/ν})}, with ν = sr or a prime ℓ | r−1, ν ≤ d².
  - New steps (checked): an r-th nonresidue c = u^r in F_Q; η₀ = c^{w₀} of order r^e; p ≡ ω(p mod r) mod r^e; the
    interpolation P(ζ^a) = η₀^{ω(a)} has P^{(p)} = P, so P ∈ F_p[T]; ρ_b(η) = η^{ω(b)}; noncyclicity of ⟨x, η⟩; the
    Berlekamp subalgebra; a node count of 2d − 1.
  - Cited algorithms, taken as cited: Adleman-Lenstra 1986, Algorithm A; Bach-von zur Gathen-Lenstra, Theorem 2; IKRS.
- Transfers, also under M: N05 (ray-class part of Shoup's F_{p²} set), N09 (Evdokimov), N10 (BGL). At statement level:
  N06-N08, N12.

## 4. ETH
- **CX-E01**, input E: E refutes ETH, #ETH, fixed-width SETH and #SETH, their randomized forms, Gap-ETH and NSETH. It
  refutes neither OVC, 3SUM, APSP nor FPT ≠ W[1]. The bound is h_k(n) = C_k n log log n/√log n = o(n), and for SETH one
  ε = 1/2 serves every k.
- **CX-E04**: some language in E^NP has circuit size > c n √log n infinitely often (OpenAI, Corollary 1.4, transferred).
- At statement level: E02, E03, E05, E06 (nothing here settles VP vs VNP).
- **The geometric dictionary**, K08, E07, E08 and G01-G05, is at statement level. CX-G06, confirmed: finite-monodromy
  sheaves are pointwise of weight 0, which gives no zero location.

## 5. Open rows and where the results went
- The run's unproved extensions CX-U01 to U06 are kept as gates.
- The successor material went into GRH_NIGHT (CX-ALG-016 to 028) and then into GRH_ALGORITHMS (prompt 67): N01-N04,
  N13, N14 (ii) and N15 are rows of its classification table and of its Teichmüller and nonresidue theorems.
- Seed `reports_20261122/paper_seeds/SEED_MAS_ARTIN.md`, Paper 2.
- Koiran and GCT V: prompt 36 (CUE/GCT) was given K05-K07 and E06.
- Our consult of 21 Nov (`reports_20261120/split_zero/consults/CONSULT_af2a18f6_GRH_BACKWARD.md`) used K01-K03. Its
  Q1′ GCT-3 entry was later corrected: VBP ≠ VNP, not VP ≠ VNP.
