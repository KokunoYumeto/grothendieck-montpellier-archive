# What the findings change

Run **CX_GRH-20261121**, begun 21 November 2026 in Europe/Berlin. The precise proofs and citations are in `CX_GRH.tex`; the question and check registers identify the scope and verification of each conclusion.

## The premise contract matters

The task stipulates Alpöge's Dirichlet RH/GRH and the supplied OpenAI counting theorem as theorems. This report uses that contract. It does not audit their authenticity or claim to replay their complete Lean developments. The attachment contains the two Alpöge interface files, but not the full imported development or the described 175,187-file scan.

Write **A_D** for the rational Dirichlet theorem, **M** for Masullo's all-number-field Hecke-GRH claim, and **E** for the supplied counting theorem. Every consequence of M remains **conditional on M**. Calling a result unconditional through A_D means no further conjectural analytic premise remains in that transfer, under the task's theorem convention. It does not mean that the algorithm has become faster than its stated bound, or that the task was previously outside P.

Masullo's introductory claim is in Chapter 1, §1.2, especially §1.2.3, PDF pp.12–16; the relevant Hecke conventions are Chapter 3, Definition 3.2.1.2, Proposition 3.2.1.3, and Definition 3.2.1.4, pp.123–124. Theorem 13.3.1.2 on p.522 is an empty heading with an insertion footnote. The paper therefore cites the introductory claim and the actual trace statements 12.5.1.1 and 13.3.1.1 in their proper roles. It does not manufacture a completed theorem from the index.

## 1. The exact analytic boundary

The basic distinction is between a character over **Q** and a character over an arbitrary number field. A finite-order ray-class character over K is a Hecke character of K. Some older algorithm papers call it a “Dirichlet character of K.” That terminology does not identify it with an ordinary Dirichlet character over Q.

CX-R01 proves that A_D supplies RH for Dedekind zeta functions of finite abelian extensions of Q, using the primitive-character factorization. M supplies RH for every Dedekind zeta function by its trivial-character case, and supplies the finite-order Hecke characters used in class and ray class groups. No transfer here requires a conjecture asserting holomorphy of arbitrary Artin L-functions.

CX-R02 gives a concrete check on the distinction. The permutation representation associated with Q(cube root of 2) has dimension three but trace zero at a lifted three-cycle commutator. Every virtual integral sum of rank-one characters has trace at a commutator equal to its dimension. This refutes the proposed rank-one representation decomposition. It does **not** prove logical independence of rational Dirichlet GRH and more general Dedekind RH.

| Task | What is established | Retained qualification |
|---|---|---|
| Miller testing with Bach's bound | A_D supplies the quadratic Dirichlet hypothesis; deterministic polynomial-time testing with bases through ceil(2 log² N). CX-N01. | This particular test is justified; PRIMES was already in P. No factorization of N−1 beyond its power of two is needed. |
| Specified r-th nonresidue in Fp | A_D gives a polynomial-time search for prime r dividing p−1. CX-N02. | The rest of p−1 need not be factored. |
| Primitive root in Fp | Deterministic polynomial-time construction when the full factorization of p−1 is supplied; a polynomial-size guaranteed candidate list without it. CX-N03–N04. | A short candidate list does not by itself identify or certify a generator. |
| Quadratic nonresidue in a supplied Fp^m | A_D suffices for every m; even m is already unconditional. CX-N13. | The irreducible polynomial defining the field is supplied. In characteristic two every element is a square. |
| More general extension nonresidues | For every specified prime r dividing p−1, A_D suffices in the supplied extension. CX-N13. | This does not cover every r dividing p^m−1 when r does not divide p−1. |
| Shoup's quadratic-extension primitive-root candidates | The published route uses ray-class Hecke characters of an imaginary quadratic field; M supplies them. CX-N05. | The weaker quadratic-nonresidue task has the better transfer above. |
| Buchmann–Shoup multiplicative generating sets | M supplies both auxiliary-prime and ray-class gates. CX-N06 and CX-N11. | Time remains (n log p)^{O(n)}. It is polynomial for fixed n, and the output is a generating set. |
| General finite-field factoring | CX-N15 gives a complete independent deterministic factorization proof under M, through explicit cyclotomic–Kummer Dedekind-zeta hypotheses and the AL86/BGL/IKRS algorithms. | Time remains (d^{log d} log q)^{O(1)}. The unrestricted A_D-only replacement is unproved; no general polynomial-time degree bound is asserted. |
| Class-group factor bases | M supplies the ideal-class character estimates and the 12 log²|Δ| generator bound. CX-N07. | Generators do not include their full relation lattice. Even abelian K/Q can have a Hilbert class field nonabelian over Q. |
| Class-group and unit verification | A factor-two analytic interval certifies the integer index once the stated rank, torsion, and factor-base conditions hold. CX-N08. | It gives no relation-collection running time. |
| Imaginary-quadratic class-group computation | The cited Biasse–Erukulangara algorithm transfers under M with expected Las Vegas bound exp((3/√8+o(1))√(log d log log d)). CX-N12. | Randomness is retained. The displayed bound is superpolynomial and subexponential in the bit length. |

The auxiliary-prime construction is made concrete in CX-N11. For p not dividing n, use E=Q(ζ_(2n),p^(1/n)). A Frobenius conjugacy class generates its cyclic Kummer subgroup. Effective Chebotarev under RH for ζ_E and ζ_Q produces q=O(n⁴ log²(np)), q congruent to 1 modulo 2n, with the required order condition on p. The degree-n cyclic subfield of Q(ζ_q) then has p inert. The cyclic field used to represent the finite field and the generally nonabelian field used to prove that a small auxiliary prime exists are different fields.

CX-N15 completes the general finite-field factorization transfer through a separate accessible proof. For a degree-d input over Fq, q=p^m, the small-characteristic branch p≤d is handled unconditionally. In the other branch, a sufficient analytic family is RH for ζ_Q and ζ_{E_ν}, where E_ν=Q(ζ_(2ν),p^(1/ν)), ν=sr with s=ord_r(p), or ν is one of the auxiliary primes ℓ dividing r−1 required by BGL. Every used ν is at most d² and is coprime to p. These are sufficient hypotheses, not a claim of necessity.

The proof constructs F_(p^(sr)), takes its Frobenius-fixed F_(p^s) subfield, and constructs a maximal r-primary unit by a Frobenius eigenvector. Equivariant interpolation places that unit in the cyclotomic coefficient algebra required for IKRS descent. For the original polynomial, the algebra fixed by p-power Frobenius is a split Fp-algebra indexing its irreducible factors. Its idempotents yield those factors, with the same quasipolynomial bound. No general factorization or historical radical oracle is called in this construction.

The original full EVD94 proof was not retrieved. That historical source limitation does not leave a proof gap in CX-N15, which uses the accessible AL86 Theorem 1 and Algorithm A, BGL Theorem 2, and the IKRS Main Theorem, Lemma 4.2 and Proposition 4.6. The main conditional transfer is established; extending it to A_D alone remains a separate question. The rank-one and higher-valuation counterexamples refute specified shortcuts, not the possibility of a different A_D-only algorithm.

The exact published locators are Bach (1990), §6 and Theorems 2–3, p.372, Miller consequence p.373, Theorem 4 p.375 and corollary p.376; Shoup (1992), author-version Theorems 2–3, pp.3–4, Propositions 9 and 13, pp.10–12; Buchmann–Shoup (1996), Fact 2.1 p.1314 and Fact 4.3 p.1319; and Bach–Sorenson (1996), §2 p.1720 and Theorem 5.1 p.1729. The paper gives the remaining individual locators and distinguishes author pagination from journal pagination.

The independent factoring composition uses Adleman–Lenstra (1986), Theorem 1 p.350, Algorithm A pp.350–351 and Lemma 6 p.352; BGL (2001), Theorem 2 p.7; Lenstra (1991), the explicit-data convention p.329 and subfield construction p.332; and IKRS (2008), Main Theorem p.3, Lemma 4.2 p.14 and Proposition 4.6 pp.16–17.

## 2. Koiran and GCT V

Koiran's proof uses the prime-ideal theorem for the **field of a bounded algebraic solution**. This field need not be normal. CX-K01 applies Lagarias–Odlyzko Theorem 1.1 to the trivial extension E/E, counts degree-one prime ideals, and removes the primes at which denominators or the chosen order obstruct reduction. A Galois closure is unnecessary; avoiding it prevents a needless factorial growth in degree.

Conditional on M, the resulting Hilbert Nullstellensatz decision problem is in AM, hence in Π₂^P. CX-K02 proves that rational circuit representations and the nonzero homogeneous version preserve the bound. The complement is in Σ₂^P. The AM locator is the extended DIMACS report, §2 Theorem 2, printed pp.5–6; the journal's displayed formulation uses RP^NP. The 8 August 1997 erratum's correction to Theorem 8 is retained.

A_D covers a precisely bounded **abelian-witness promise problem**, proved in CX-K03. It does not discharge all solution fields by the displayed factorization. CX-K04 proves that x³−2=0 has no solution in any abelian extension of Q, refuting the proposed universal abelian-witness replacement. This is a refutation of a reduction, not a theorem saying HN in AM cannot have a different proof from A_D.

For a nonzero standard-graded Q-algebra with a circuit list of homogeneous equations and an explicitly listed ambient coordinate set, CX-K05 refines the h.s.o.p. construction to **FP^{Σ₂^P}**, conditional on M. A bounded candidate is good exactly when its forms have no common nonzero geometric zero. Prefix search merges its existential guess with the first existential quantifier block. The least successful number of forms gives the dimension. The proof verifies the finite-module criterion, including nilpotents and reducible cones, and preserves polynomial output bit length. Unconditional polynomial-space construction remains available.

Two distinct outputs must be kept apart for succinct explicit varieties:

- **Strict small separating systems:** the historical GCT V Theorems 4.10 and 5.12 transfer to EXPH under M. A polynomial-space construction already follows from Forbes–Shpilka Theorem 7.1 and is recorded by Guo–Saxena–Sinhababu Theorems 1.5–1.6. This is not a first unconditional consequence of a 2026 GRH theorem.
- **Optimal-cardinality h.s.o.p.:** GCT V Theorems 4.1 and 5.5 retain their additional assumption that defining equations are computable in singly exponential time. Discharging Koiran's analytic premise does not supply those equations. Mixed positive weights also retain the original homogeneous-output conventions.

These results improve or classify the complexity of **constructing a normalization map**. They do not establish the orbit-closure noncontainment required for a permanent lower bound.

## 3. What the ETH theorem actually supplies

For each fixed clause width k, the supplied theorem counts in polynomial space and time poly(n+m) times 2^{O(n log log n/√log n)}. At fixed clause density the log log factor is absent. The constants may depend on fixed k; the theorem is not uniform in growing clause width.

CX-E01 proves the refutation of ETH, counting ETH, SETH and its counting version, randomized versions, Gap-ETH, and NSETH, with their quantifiers stated. A previously proved implication “H implies lower bound B” stays a valid implication when H is false. Neither B nor its negation follows merely by removing H. NP-hardness reductions, unconditional lower bounds, and independent hypotheses keep their separate status.

Actual target-problem algorithms require reductions in the correct direction. CX-E02 proves the transfer when the target reduces to fixed-width CNF with a linear bound on the number of variables in the target parameter. Parsimonious reductions transfer counts. Polynomial blowup in that parameter can destroy the subexponential saving; a polynomial prefactor alone cannot certify a subquadratic fine-grained bound. Counting k-cliques transfers in the graph's **vertex** parameter, not as an FPT claim in k. A sparsification step, when used, must charge its branch count and preserve the counting reconstruction.

CX-E03 gives an exact-counting algorithm for fan-in-two circuits with n input bits and s gates, but its exponent depends on **n+s**. Substituting s=n^a for a>1 does not meet Williams's all-polynomial-size Circuit-SAT premise. The supplied preprint nevertheless already proves the separate quantitative corollary: some language in E^NP has Boolean circuit complexity greater than c n√log n infinitely often. CX-E04 checks that transfer and its constants. This is not an NP lower bound, an all-polynomial-size lower bound, or an arithmetic permanent lower bound.

For an r by r 0–1 matrix with e nonzero entries, CX-E05 gives a permanent algorithm with exponent O((r+e)/√log(r+e)) by a parsimonious linear-size edge-selection circuit. Sparse matrices therefore obtain a subexponential bound in r. For dense matrices this particular encoding has Θ(r²) variables. It does not give a subexponential-in-r algorithm for the general dense permanent.

No deduction in the paper settles P versus NP or VP versus VNP. CX-E06 spells out the model gap: the counter returns an integer at a supplied Boolean input, whereas VNP asks for a symbolic polynomial family and an arithmetic circuit model. The determinant is complete for the weakly skew/branching-program class, not thereby for all VP. The numeric counting bound does not produce graded coordinate-ring representations. Even a hypothetical symbolic upper bound of size 2^{O(r/√log r)} would be compatible with a lower bound 2^{r^ε} for a fixed 0<ε<1; these scales cannot be compared by saying both are subexponential.

## 4. The consequences in Grothendieck's language

The translations are separate proved dictionaries in Part II. They retain the encoding and all analytic premises. An unencoded abstract scheme does not come with a complexity measure.

| Finding family | Object and proof-carrying translation | Published location | Inspected archival companion |
|---|---|---|---|
| CX-R01–R02; CX-K01–K04 | Spread the solution field to a finite étale cover of an open of Spec Z. Its permutation local system has Euler product ζ_E, and Frobenius trace counts degree-one primes. | SGA 1, V §4 Theorem 1 and §7; SGA 5, XV §3 no.1 Proposition 1. | Cote 98, scans 11–12, sheets 10–11: norm-morphism degree axioms and finite G-sets. |
| CX-K05–K08 | A successful parameter list gives a finite map Spec R→A^d, and, for d≥1, a finite basepoint-free projective projection. The successful matrices form an open locus. | EGA II 6.1.4–6.1.5; FGA Exp.221 §3 Theorems 3.1–3.2. | Cote 98, scan 44, sheet 43: bounded families of coherent sheaves. |
| CX-N01–N06, CX-N09–N15 | Modular powering is a G_m operation. A nonresidue is a nontrivial Kummer torsor class; factorization is computation of primitive idempotents of a finite étale algebra. | SGA 3 VIII 1.1–1.2; SGA 4 IX 3.2; SGA 1 V §7. | Cote 28, scan 3, sheet 2: group-action map and axioms; cote 98, scan 12. |
| CX-N07–N08, CX-N12 | Cl(O_K)=Pic(Spec O_K). The factor base consists of divisor line bundles, relations are principal divisors, and units form the kernel. | SGA 4 IX Theorem 3.3; SGA 6 V 3.10 and VI 3.2–3.3. | Cote 2, scan 5, sheet 4: rank augmentation and Picard comparison in dimension at most one. |
| CX-E01–E05, CX-E07 | The Boolean equations define a constant finite étale Z-scheme with exactly #F components. Gate extension gives an actual scheme isomorphism. Counting computes its degree and the rank of its finite free algebra. | SGA 1 V §7; SGA 6 VI 3.2–3.3. | Cote 98, scans 11–12; cote 2, scan 5. |
| CX-E06, CX-E08, CX-G04–G05 | Integral orbit models have flat coordinate algebras. Containment gives a graded equivariant quotient, hence a Schur-multiplicity inequality in characteristic zero. | SGA 3 I 4.6.3.1 and 4.7.1–4.7.2; FGA Exp.221 Theorems 3.1–3.2, Proposition 3.8; SGA 6 V 2.4. | Cote 28, scan 3; cote 98, scan 44. |
| CX-G06 | Finite-monodromy eigenvalues are roots of unity, hence pointwise weight zero. This is a local statement, not a proof of number-field GRH. | SGA 5 XV §3; Weil II §1.2, Theorem 3.3.1 p.204, Corollary 3.3.9 p.207. | Cote 34, scan 64, sheet 63, crossed-out Remark 1.17; scan 74, sheet 73, equation (2.5.5). |

The representation category contributes its K_0 ring, tensor multiplication, exterior operations λ^i, and the corresponding γ-filtration. Schur functors are images of Young idempotents over a Q-scheme, or after the needed denominators are inverted; integral Schur classes can be expressed by Jacobi–Trudi. No claim of integral semisimplicity is made.

For the Boolean scheme, its class is #F times the unit and its exterior-power series is (1+t)^{#F}. Its reduced rank class is zero. Over a finite-field fiber, geometric étale cohomology is concentrated in degree zero with identity Frobenius, the zeta function is (1−t)^{−#F}, and the Artin motive is a sum of unit motives. These are explicit consequences of its component decomposition, not new purity or standard-conjecture results.

Rank does not recover equivariant representation data: the trivial and sign representations of C₂ have equal rank and different traces. CX-G05 proves this obstruction in K_0. A numeric counting algorithm therefore does not, through this dictionary alone, compute the Schur multiplicities needed for an orbit-closure obstruction.

The archive passages supply historical companions for this language. Cote 34's first cited passage is visibly crossed out; both cited passages concern finite-field Riemann–Weil reasoning. They are not claims about number-field zero locations. The work changes the availability of the explicitly stated computational transfers, not the content or validity of SGA, FGA, or Weil II. It does not solve the plethysm, Kronecker, nonstandard-RH, or other questions assigned to the parallel prompts.
