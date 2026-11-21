# K17 supporting review: Vandiver, K-groups, and the exact cohomological gate

**Quantitative update:** section 10 and work/k_quantitative_refinement.md now give a fully checked extraction of exponent 7, with still unevaluated multiplicative constants.

Date: 2026-11-21 (UTC). Reviewer: GPT-6 Astra Pro, agent `/root/vandiver_k`; effort setting not exposed to the agent. This file supplies research to the main paper. **Source-recovery update:** the public Lean implementation recovered during this run now supplies a precise quantitative statement in `UpperTheory.V.SmallClassNumbers.bound`; see section 9. The original supplied endpoints alone did not supply that statement. Section 9 supersedes any suggestion below that no relevant implementation has now been found.

## 1. Status of the supplied step 17

Read `sources/ALPOGE_remark.txt`, p. 4 step 17 and footnote 6, together with both supplied Lean files and the step-17 row in `ALPOGE_LEAN_MAP_20261120.md`.

Step 17 names the ambient cohomology group `H^1(o_E[1/l], Q_l/Z_l(-e))` and refers to classes not eliminated by twisting. It does not define a set of allowed fields E, the twists e, primes l, the classes, the twisting operation, or a quantified vanishing/bound. The footnote describes a belief about some K-groups and a tentative cyclicity range. The supplied Lean endpoint declarations concern RH and Dirichlet L-functions, not these cohomology groups; their imported implementation is not present. The map explicitly labels the step-17 association low confidence and records no Vandiver/Lichtenbaum name match.

Consequently, no exact step-17 proposition or K-group range can be recovered from these files alone. This is a source-content finding, not a refutation of the stipulated RH theorem and not a logical independence theorem separating RH from Vandiver.

## 2. The verified literature statement

Let p be an odd prime, S_p=Spec Z[1/p], F_p=Q(mu_p), Delta=Gal(F_p/Q), omega the Teichmuller character, and A_p=Cl(Z[mu_p]) tensor Z_p. Write A_p^{[a]} for the omega^a eigenspace, with a modulo p-1.

For each k>=1, modern etale comparison and cyclotomic Kummer descent give the equivalences

    K_{4k}(Z) tensor Z_p = 0
    iff H^2_et(S_p,Z_p(2k+1)) = 0
    iff H^2_et(S_p,mu_p^{tensor(2k+1)}) = 0
    iff A_p^{[-2k]} = 0.

Exact locators:

* M. Kurihara, *Some remarks on conjectures about cyclotomic fields and K-groups of Z*, Compositio Math. 81 (1992), 223--236: Lemma 1.2 (p. 225); Corollary 1.5 (p. 226); Proposition 2.1 (p. 227); Proposition 3.7 (p. 229); Remark 3.11 (p. 230).
* C. Weibel, *The K-book*, Chapter VI, Theorem 8.2 and Corollary 8.3 (chapter pp. 47--48), Theorem 10.9 (chapter p. 65). The theorem is printed for irregular primes; regular primes satisfy the vanishing directly. The attached modern comparison formulation covers every odd p.

Historical correction: Kurihara 1992 Proposition 3.7 proves the implication from K-group vanishing to the indicated class-group component. Remark 3.11 gives the converse assuming the then-conjectural Quillen comparison. It is inaccurate to attribute the modern unconditional equivalence solely to an unconditional 1992 theorem. The comparison is now established; Weibel VI.8.2/8.3/10.9 give the precise modern version.

### How the exponent is checked

With R=Z[mu_p,1/p], the unique prime above p is principal, so Pic(R)=Cl(Z[mu_p]). There are no real places and only one omitted finite place, so Br(R)=0. Kummer therefore identifies H^2(R,mu_p) with Pic(R)/p. Tensor by mu_p^{tensor 2k}, then take Delta invariants. Since |Delta|=p-1 is invertible mod p, descent is exact, and the invariant part is (A_p/p)^{[-2k]}. This checks that the exponent is -2k, not 2k or -(2k+1). Finiteness and Nakayama give the zero-equivalence. This is a short derivation of the notation, not a replacement proof of the cited comparison theorem.

### Vandiver and the finite set of indices

Vandiver at p says A_p^+=0, equivalently p does not divide the class number of Q(mu_p)^+. Since p is odd, plus descent is exact. Complex conjugation acts by (-1)^a on A_p^{[a]}, so this is the vanishing of all even components. The trivial component A_p^{[0]} vanishes: on that component, the norm to Q followed by extension of ideals is multiplication by p-1, and Cl(Z)=0.

It follows that the following statements are equivalent:

1. Vandiver at p.
2. K_{4k}(Z) tensor Z_p=0 for every integer 1<=k<=(p-3)/2.
3. K_{4k}(Z) tensor Z_p=0 for every k>=1.

The range for p=3 is empty; the only plus character is the already-zero trivial component. For a fixed k, the relevant condition is only A_p^{[-2k]}=0. Vanishing for a finite list of k's proves just those residue classes modulo (p-1)/2 unless the list covers all nonzero residues. The statement is periodicity of *vanishing*, not an assertion that the full finite p-primary groups in different degrees are isomorphic.

### Derived coverage observation (VK-COVER)

If K_{4k}(Z)=0 for every 1<=k<=N, then Vandiver holds for every odd prime p<=2N+3. Proof: (p-3)/2<=N, so all required character components occur in the range above. Conversely, for a fixed p, any list of k-values covering all nonzero residues modulo (p-1)/2 suffices. This follows by reducing -2k modulo p-1. Full proof read and checked; no extra assumption beyond the cited equivalence.

## 3. What is already known without step 17

* For every regular odd p and every k>=1, K_{4k}(Z) tensor Z_p=0. This follows from A_p=0 and the equivalence above.
* For p=2 and every k>=1, K_{4k}(Z) tensor Z_2=0. Exact primary locator: J. Rognes and C. Weibel, *Two-primary algebraic K-theory of rings of integers in number fields*, JAMS 13 (2000), 1--54, Theorem 0.7 (pp. 4--5), proved as Theorem 7.11. For R=Z[1/2], their notation gives s=1 and t=u=0; hence the 2-ranks in degrees 8a and 8a+4 are zero. The groups in positive even degrees are finite, so their 2-primary parts are zero. The localization equivalence with Z is stated on p. 1 and in Theorem 0.6. Weibel VI.9.8 records the special case directly.
* K_4(Z)=0: J. Rognes, *K_4(Z) is the trivial group*, Topology 39 (2000), 267--281, Theorem 0.1, p. 268.
* K_8(Z)=0: M. Dutour Sikiric, P. Elbaz-Vincent, A. Kupers, J. Martinet, *Voronoi complexes in higher dimensions, cohomology of GL_N(Z) for N>=8 and the triviality of K_8(Z)*, JIMJ 25 (2026), 565--590, Theorem 6.4. Author preprint arXiv:1910.11598v1, Theorem 6.4, p. 19; Corollary 7.1 gives A_p^{[p-5]}=0 for p>3. Publication metadata checked at Cambridge (online 24 November 2025, January 2026 issue). Do not reproduce the 2013 K-book table which still lists K_8 as unknown.
* Hart--Harvey--Ong, *Irregular primes to two billion*, Math. Comp. 86 (2017), 3031--3049, section 1 item (2), verifies Vandiver for every odd p<2^31. This yields K_{4k}(Z) tensor Z_p=0 for those primes and all k>=1, without step 17. This large computation is used as a cited published result, not re-run here.

Combining the fixed-component equivalence with K_4 and K_8 also gives vanishing whenever k is congruent to 0, 1, or 2 modulo (p-1)/2. The residue 0 uses A_p^{[0]}=0, not K_0(Z)=0; K_0(Z)=Z is irrelevant and must not be included in the vanishing assertion.

### Quantitative alternative to the cohomological gate (VK-BOUND)

For any fixed k>=1, an independently proved bound |K_{4k}(Z)|<2^31 would force K_{4k}(Z)=0, because the cited low-prime verifications and the 2-primary theorem exclude every prime divisor below 2^31. A nontrivial finite group has a prime divisor of its order. This is a conditional arithmetic observation; the supplied note supplies no such bound, and the words referring to Lichtenbaum are not a regulator calculation. Proof checked in full.

## 4. Independent check of the parent's strongest cohomological gate (VK-PT)

Set r=2k+1, T=Z_p(r), and D=Q_p/Z_p(1-r)=Q_p/Z_p(-2k), with k>=1 and p odd. In compact/discrete Poitou--Tate duality use the segment

    H^1(Q_p,T) -> H^1(S_p,D)^vee -> H^2(S_p,T)
    -> H^2(Q_p,T) -> H^0(S_p,D)^vee -> 0.

The archimedean modified Tate terms vanish because 2 is invertible in p-primary coefficients. Local Tate duality identifies H^2(Q_p,T) with H^0(Q_p,D)^vee. Both global and local cyclotomic characters have image Z_p^times, so H^0(S_p,D)->H^0(Q_p,D) is an isomorphism. Accordingly, the last displayed arrow is an isomorphism. Exactness then identifies H^2(S_p,T) with the cokernel of H^1(Q_p,T)->H^1(S_p,D)^vee. Pontryagin duality and local duality identify its dual with

    ker[ H^1(S_p,D) -> H^1(Q_p,D) ].

Etale comparison therefore gives

    (K_{4k}(Z) tensor Z_p)^vee
      ~= ker[H^1(S_p,Q_p/Z_p(-2k)) -> H^1(Q_p,Q_p/Z_p(-2k))].

Use a comparison edge map, not an unspecified factorial-normalized integral Chern character. Use the compact/discrete Poitou--Tate theorem directly, or justify all inverse limits if starting from finite levels. The parent is checking the exact Milne locator. I independently checked this proof from the standard exact sequence and read the whole derivation again; no leftover local H^2 term remains, precisely because of the H^0 isomorphism. This does not extend automatically to p=2, where the real Tate terms need separate treatment.

The correct task for step 17 would thus be to identify and annihilate *this locally trivial subgroup* at E=Q,e=2k (or its image in a field from which one can descend). It is stronger than necessary to demand the vanishing of the entire ambient H^1. A result about an undefined selected class set is not enough to identify its intersection with this kernel.

## 5. A small exact Vandiver-37 certificate (VK-37)

Files: `work/vandiver37_certificate.py`, `work/vandiver37_certificate.txt`. They use only Python's standard library and exact integers/Fractions.

The arithmetic criterion is Buhler--Harvey, *Irregular primes to 163 million*, Math. Comp. 80 (2011), 2435--2444, section 4; pp. 4--5 of arXiv:0912.2121v2. For each irregular even index a at p, choose a prime q congruent to 1 mod p and a nontrivial pth root z modulo q. Put

    V_{p,a}=product_{c=1}^{(p-1)/2}(z^c-z^{-c})^{c^{p-1-a}} mod q.

If V_{p,a}^{(q-1)/p} is not 1 mod q for every irregular index a, Vandiver holds at p.

For p=37 the exact residues B_2,B_4,...,B_34 modulo 37 are

    31,16,15,16,4,17,32,22,31,15,15,17,12,29,2,0,2.

Thus the only irregular index is 32. Take q=149 and z=16. Trial division certifies both primes; 16^37=1 mod149 and 16!=1, so z has order37. The product gives V=48, and V^4=142 mod149, which is not 1. The cited criterion therefore proves Vandiver37, hence K_{4k}(Z) tensor Z_37=0 for every k>=1.

Checks actually performed: rational Bernoulli recurrence compared with formal power-series inversion modulo37; modular product via Python modular powers compared with termwise repeated multiplication and reduced exponents. The code and the criterion application were then read in full. This is a computation with a reproducible arithmetic certificate plus a cited theorem, not a Lean proof or an independent reproof of the class-field-theoretic criterion.

## 6. Soulé normalization point shared with the integral-tripod reviewer

Kurihara p.233 section5 defines the Deligne--Soule cyclotomic class c(1) and C=Z_p c(1) in H^1(S_p,Z_p(r)), with p odd and r odd>=3. This H^1 is free of rank1 and c(1) is nonzero. Proposition5.1 proves

    #H^2(S_p,Z_p(r)) <= [H^1(S_p,Z_p(r)):C].

Remark5.2 explicitly says that the inequality is equality, referring to Bloch--Kato, *L-functions and Tamagawa numbers of motives*, Grothendieck Festschrift I, section6, equations(6.8),(6.9). The inequality alone does NOT show that H^2=0 forces C primitive. With the cited equality, it does. This controls a rank-one cyclotomic cohomology lattice, and should not be confused with integral free generation of the entire image Lie algebra.

Kurihara Proposition4.2 (p.231) and Remark4.3 provide a concrete unconditional degree3 statement: the appropriate cyclotomic-kernel Galois representation surjects onto Phi(3)/Phi(4)~=Z_p(3), and the cohomology class agrees with c(1) up to Z_p^times. These are precise positive integral statements independent of step17.

### Exact full-domain Soulé index, with normalization derivation (VK-SOULE)

Let p be odd, m>=3 odd, S=Spec Z[1/p], Gamma=Gal(Q(mu_{p^infty})/Q)=Z_p^times, and N=Gal(Qbar/Q(mu_{p^infty})). Fix a compatible root system zeta_n of order p^n. Define kappa_m on the full group N by the Kummer classes of

    E_{m,n}= product_{a in (Z/p^n Z)^times} (1-zeta_n^a)^{a^{m-1}}

modulo p^n, with the standard target Z_p(m). Then the exact index is

    [Z_p(m):kappa_m(N)]
      = [H^1(S,Z_p(m)):Z_p c(1)]
      = #H^2(S,Z_p(m))
      = # (K_{2m-2}(Z) tensor Z_p).

The last equality uses the modern K-theory comparison; the preceding equality is Kurihara Remark5.2's stated Bloch--Kato equality. Here is a complete check of the other two steps, so that no hidden factorial in a power-series coordinate is imported.

First, the original definition in Kurihara p.233 equation(4) is

    c(1) mod p^n = cor_{Q(mu_pn)/Q}((1-zeta_n) tensor zeta_n^{tensor(m-1)}).

Restricting to N and applying restriction-corestriction gives the sum over a in (Z/p^n)^times of (1-zeta_n^a) tensor (zeta_n^a)^{tensor(m-1)}. After factoring out zeta_n^{tensor(m-1)}, the corresponding Kummer product is exactly E_{m,n}. Thus the restriction of c(1) is kappa_m. In the alternate convention zeta_n^a-1, the factors -1 have zero odd-p Kummer class. Changing the chosen compatible root generator changes the target basis by a p-adic unit. Neither modification changes the index.

Second, H^1(S,Z_p(m)) is free of rank1 (Kurihara p.233). A primitive generator alpha has nonzero reduction in H^1(S,F_p(m)), by the coefficient exact sequence. Write Gamma=Delta x Gamma_1 with Delta=mu_{p-1} and Gamma_1=1+pZ_p. Inflation-restriction and the prime-to-p order of Delta give

    H^1(Gamma,F_p(m)) = H^1(Gamma_1,F_p(m))^Delta = 0.

Indeed Gamma_1 acts trivially on F_p(m); Gamma is abelian, so Delta acts trivially on Gamma_1 and by omega^m on the coefficient. Since m is odd and p-1 is even, omega^m is nontrivial, giving no invariants. If the restriction of alpha to N had image contained in pZ_p(m), its reduction would restrict to zero. Inflation-restriction for the cyclotomic quotient would then place the reduced class in the zero group just computed, a contradiction. One may apply this directly to the maximal extension unramified outside p and use the surjection from N onto its cyclotomic kernel; inflation to the full absolute Galois group is injective in degree1. The image of alpha is compact, hence a closed subgroup of Z_p; because its reduction is nonzero, it equals Z_p. Write c(1)=a alpha with a!=0. Then kappa_m(N)=aZ_p(m), proving the index equality.

Thus fixed-degree K-vanishing is equivalent to primitivity of the corresponding **full-domain** kappa_m, and all odd-degree full-domain kappa_m are surjective exactly when Vandiver at p holds. This argument does not identify kappa_m(F^m G) with kappa_m(N): restriction to a deeper Galois filtration may have smaller image, even if the full-domain image is Z_p. It does not prove integral free generation.

Independent primary checks of the normalization and all-degree statement: S. Ishii, *On Kummer characters arising from Galois actions on the pro-p fundamental groups of once-punctured CM elliptic curves*, arXiv:2312.04175v2, p.2, Theorem1.1; published Research in Number Theory11(2025),38, DOI10.1007/s40993-025-00622-0. The definition immediately preceding Theorem1.1 uses exactly the product above on N. Theorem1.1 gives nontriviality for odd m>=3, surjectivity when m=1 mod(p-1), and equivalence between Vandiver and surjectivity for all odd m>=3. Source URL https://arxiv.org/pdf/2312.04175 ; refs `turn481670947view1`, `turn140639342view0`.

Ichimura--Kaneko, *On the universal power series for Jacobi sums and the Vandiver conjecture*, J. Number Theory31(1989),312--334, section1.1 pp.313--314, also defines the Kummer product and displays the universal-series coefficient (1-p^{m-1})^{-1} kappa_m/m!. The factor 1-p^{m-1} is a p-adic unit for m>=3. The factorial in logarithmic power-series coordinates is not an integral unit for all p,m and must not be silently included in the definition of kappa_m. Author PDF: https://www2.math.kyushu-u.ac.jp/~mkaneko/papers/04universal_power.pdf ; ref `turn280959727view0`.

Original Ichimura--Sakaguchi1987, Adv. Studies Pure Math.12,53--64, DOI10.2969/aspm/01210053, was bibliographically identified but its original PDF was not retrieved (the direct landing page returned an anti-bot challenge). Accordingly, no direct reading of that original article is claimed. The exact index result above instead has an explicit derivation from the original Kurihara definition and the equality Kurihara attributes to Bloch--Kato. The whole derivation was read and checked, including the odd-prime restriction, the full domain, compactness of the image, and the coefficient normalization.

## 7. Web references for the parent to open before citing

* Kurihara primary PDF: https://www.numdam.org/item/CM_1992__81_2_223_0.pdf ; ref `turn589823038view0` (same content also in `turn278379234view0`). Downloaded and rendered locally, pp226/230/233 inspected.
* Weibel author book chapter: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf ; ref `turn786966245view1`; exact comparison text `turn232093824view0`; 2-primary special case `turn756374929view0`.
* Rognes--Weibel primary author PDF: https://sites.math.rutgers.edu/~weibel/archive/papers-dir/RognesWeibel.pdf ; ref `turn560151568view1`, exact0.7 `turn327219305view1`.
* Rognes K4 journal PDF mirror: https://citeseerx.ist.psu.edu/document?doi=fc64f344eb0511ef99b5d78af544cfaa5963090c&repid=rep1&type=pdf ; search ref `turn574595010search6`; DOI https://doi.org/10.1016/S0040-9383(99)00007-5 . Theorem0.1 p268 is the final published statement.
* K8 author PDF: https://jamartin.perso.math.cnrs.fr/Publications/DEKM_arXiv.pdf ; ref `turn239380802view1`. Current publication metadata https://doi.org/10.1017/S1474748025101394 ; web ref `turn560151568search2`.
* Buhler--Harvey primary preprint: https://arxiv.org/pdf/0912.2121 ; ref `turn327219305view0`, criterion `turn547933874view2`. Note the old preprint has a typo in its overall bound; the p37 certificate does not use the large bound.
* Hart--Harvey--Ong primary preprint: https://arxiv.org/pdf/1605.02398 ; ref `turn965982060view0`, section1 item2; DOI https://doi.org/10.1090/mcom/3211 .

## 8. What remains an actual gate

No assertion that arbitrary odd-prime Vandiver, K_{12}(Z)=0, or the pro-p kernel problem is solved is made here. The supplied prose and endpoint files alone have no quantified assertion to apply. The recovered implementation in section 9 changes the source status: it provides a polynomial bound and a conditional large-prime vanishing threshold. It does not provide numerical values for its constants or an assertion that every relevant kernel vanishes. Potential closing inputs are now a vanishing of the local kernel in section 4; enough class-group character components in section 2; or an explicit sufficiently small cardinality bound as in section 3. The polynomial bound by itself does not close any of those all-prime gates.

## 9. Recovered SmallClassNumbers theorem and strongest K-group consequence

### 9.1 Exact recovered declarations (VK-SOURCE-RECOVERED)

Read in full, including displayed proof terms, these files recovered by the parent from the public source repository:

* `work/lean_candidates/src/Development/AutomorphicArithmetic/AutomorphicVarieties/SmallClassNumbers/ClassNumberThree.lean`;
* `work/lean_candidates/src/Development/AutomorphicArithmetic/AutomorphicVarieties/SmallClassNumbers/LenEqZeroIff.lean`;
* `work/lean_candidates/src/Development/AutomorphicArithmetic/AutomorphicVarieties/SmallClassNumbers/CorGKOf.lean`.

Namespace: `UpperTheory.V.SmallClassNumbers`. The definition `len` is the O-module length of `ShaU (twist₂ l (chiO ℚ Ω l c.O ^ (-(e : ℤ)))) (l * 2) ⊤`. The proposition `Bound` quantifies natural numbers C,A, then every algebraic closure Ω of Q, every even integer e>=1, every coefficient family c, and every finite set L of primes l satisfying

    l >= 5 and (l-1) does not divide 2e.

For such L it proves each length finite and

    sum_{l in L} log(l) * len_l(e)/eO_l <= C(e+1)^A.

Here the lengths and ramification indices are coerced into the reals exactly as in the Lean definition. `bound_of` proves `U3.CorGK -> Bound`, using Q(sqrt(-3)), its class number 1, trivial conductor-2 character, and auxiliary primes 7,11. `CorGKOf.lean` declares `corGK : U3.CorGK` via the source's published-hypotheses chain, and `bound : Bound := bound_of corGK`. Reading a declaration/proof term is not a fresh compiler check of the imported project or an independent verification of the entire automorphy argument.

`LenEqZeroIff.lean` exposes `Vanish` without abbreviations: each continuous crossed homomorphism z with action χ_l^{-e} is globally a coboundary provided it is a coboundary on decomposition groups at valuations with v(2l)<1 and on inertia subgroups at every valuation. Its theorem `len_eq_zero_iff` proves exactly `len = 0 iff Vanish`. Its `Large` and `large_of` specialize to eO=1 and the strict inequality

    C(e+1)^A < log(l),

giving the above cocycle vanishing. Its `exists_coef` supplies a coefficient object with bottom coefficient ring (the image of Z_l in the chosen algebraic closure).

**Coefficient normalization now checked (VK-COEF):** the subsequently recovered `GaloisLibrary/SelmerTransport/ConjStableShaFam.lean` was read in full. It defines `QO l O := O tensor[Z_l] QZ l` with discrete topology, `eO := Module.length O (O / Ideal.span{(l:O)})`, `twist₂` as the scalar representation, and `ShaU := LocSel ... (shaFam ...)`. Its `shaFam` is exactly the selected decomposition groups plus all inertia groups. The ring equivalence in the proof of `exists_coef` identifies the bottom ring with Z_l. Therefore its QO is Q_l/Z_l, and O/lO is F_l, a simple O-module; hence eO=1. There is no hidden residue-degree factor. This mathematical normalization is fully checked; it has not been added and compiled as a new Lean lemma here.

### 9.2 Arithmetic identification of the kernel (VK-LOCAL)

Take l odd, e>0, D=Q_l/Z_l(-e), and coefficients O=Z_l. The displayed local conditions define

    Sha_strict(e,l) = ker[H^1(Z[1/l],D) -> H^1(Q_l,D)].

Here is the full comparison of conditions. A global class in H^1(Z[1/l],D) is unramified at every finite q!=l. The representation D itself is unramified at q!=l. The unramified subgroup of local cohomology is

    H^1_unr(Q_q,D) = D/(Frob_q-1)D
                   = D/(q^{-e}-1)D = 0.

The equality to zero uses e>0, so q^{-e}-1 is a nonzero element of Z_l, and multiplication by every nonzero element of Z_l is surjective on the divisible module Q_l/Z_l. If geometric rather than arithmetic Frobenius is chosen, q^e-1 occurs and gives the identical conclusion. In particular, local triviality at 2 is automatic. Local triviality at l implies the inertia condition there. Conversely, the everywhere-inertia condition gives an unramified-away-l global class, and the displayed decomposition condition at l gives its restriction zero. Odd-primary real local H^1 vanishes, and the trivial valuation imposes no additional inertia condition. Thus the recovered `ShaU` agrees with this kernel under the stated coefficient identification.

For e=2k with k>=1, section 4 then identifies it with

    (K_{4k}(Z) tensor Z_l)^vee.

Since the finite group and its Pontryagin dual have the same order, its Z_l-length is v_l(|K_{4k}(Z)|). This is the required arithmetic bridge. The bridge is mathematically proved here from standard comparison/duality and the recovered explicit local conditions; it is not asserted to be already a named compiled Lean theorem in the recovered project.

### 9.3 Every excluded prime has zero K-primary part (VK-EXCEPTIONS)

Let e>=2 be even and l odd with (l-1)|2e. The class-group character omega^{-e} has order at most two. If it is trivial, its eigenspace vanishes by norm to Q, as in section 2. Otherwise -e is congruent to (l-1)/2 modulo l-1. Because e is even, (l-1)/2 is even, so l=1 mod4. The fixed field of the kernel of this quadratic character is F=Q(sqrt(l)). Let L=Q(mu_l), H=Gal(L/F), and x lie in A_l^{[-e]}. Then x is H-invariant and

    extension_{F->L}(norm_{L/F}(x)) = sum_{h in H} h(x) = ((l-1)/2)x.

The class number of F is less than l. For completeness, put M=floor(sqrt(l)/2). Minkowski's ideal-class bound gives an integral ideal of norm at most M in every ideal class. In a quadratic field, the number a_F(n) of ideals of norm n satisfies a_F(n)<=d(n): at a split prime the coefficient at q^a is a+1, at an inert prime it is 1 or 0, and at a ramified prime it is 1; multiplication over distinct primes proves the inequality. Consequently

    h(F) <= sum_{n=1}^M a_F(n)
         <= sum_{n=1}^M d(n)
          = #{(a,b) in positive integers^2 : ab<=M}
         <= M^2 <= l/4 < l.

Here M>=1 since l>=5 in the nontrivial quadratic case. Thus Cl(F){l}=0 and norm(x)=0. Multiplication by (l-1)/2 is invertible on the l-primary group, whence x=0. The K/class-group zero-equivalence in section 2 proves K_{2e}(Z) tensor Z_l=0.

Source for the only class-number estimate used: J. S. Milne, *Algebraic Number Theory*, v3.08 (2020), Theorem 4.3, printed p.70 (PDF page72, index71), https://www.jmilne.org/math/CourseNotes/ANT.pdf ; primary web refs `turn717848828view0`, `turn717848828view1`. Its real-quadratic constant is 1/2. This elementary specialization and the entire norm argument have been read in full and independently checked by `/root/archive_kummer`.

### 9.4 Global order bound, support cutoff, and exact remaining gate (VK-POLY)

With the bottom-ring/eO=1 normalization, the recovered `Bound` implies: there exist natural C,A such that for every k>=1,

    log |K_{4k}(Z)| <= C(2k+1)^A,
    equivalently |K_{4k}(Z)| <= exp(C(2k+1)^A).

Proof: K_{4k}(Z) is finite. Its 2-primary part is zero by section 3, and its 3-primary part is zero because the mod-3 character in section 2 is trivial. Every further prime excluded by (l-1)|4k has zero primary part by section 9.3. Apply `Bound` to the finite set of the remaining prime divisors of its order. The normalized lengths are exactly v_l of the order by section 9.2; the sum is therefore log of that order. This uses a finite set, so no interchange of an infinite sum and an estimate is hidden.

The same constants give a precise support cutoff: if log(l)>C(2k+1)^A, then the l-primary part vanishes. For primes in the source's range this is `large_of`; for excluded primes or l=2,3 it follows from the unconditional arguments already given. The largest prime divisor of a nontrivial K_{4k} is therefore at most exp(C(2k+1)^A).

There is also an exact conditional cyclicity range. Put B_k=C(2k+1)^A. The singleton bound and exception removal give

    length_{Z_l} K_{4k}(Z){l} <= floor(B_k/log(l)).

In particular, 2log(l)>B_k forces the primary group to have length at most1, hence to be either zero or Z/l and therefore cyclic. By Kurihara Corollary1.5 (together with comparison), the component A_l^{[-2k]} is then cyclic as well. This does not bound the order of that class-group component by l: the K/class-group comparison here preserves the mod-l generator number and the zero condition, not necessarily the whole finite group or its order. The full short argument, including this distinction, was read and checked.

There are no extracted numerical C,A in the recovered statements reviewed here. Thus the bound does not certify all K_{4k}=0, all Vandiver components, or even a new specified K-degree. Combining it with the published verification of Vandiver for l<2^31 gives the exact sufficient quantitative gate

    C(2k+1)^A < log(2^31)  ==>  K_{4k}(Z)=0.

This inequality is only a criterion until explicit constants are supplied. The polynomial bound is nevertheless a concrete, substantially stronger reconstruction than an unspecified selected class set: it controls the full K-Selmer length, and the apparent exceptional primes can be removed by the argument above.

## 10. Stronger exponent, exact trace gate, and final TeX

The full proof in work/k_quantitative_refinement.md sharpens the reconstructed bound to

\[
\exists C_7\in\mathbb N,\qquad
\log|K_{4k}(\mathbb Z)|\le C_7(2k)^7\quad(k\ge1).
\]

Its finding ID is VK-EXP7. The proof keeps the fixed level in the cohomology estimate and uses the actual source highest weights. The rank-three coefficient has dimension at most e^6, the rank-two coefficients over six fixed imaginary quadratic fields have dimension at most 4e^2, and the norm estimate adds one power of e. The source's scalar construction is the polynomial module generated by a highest-weight vector; complete reducibility makes it one irreducible, so Weyl's exact dimension applies. The rank-two root/lift multiplicity is exactly 8, not an unspecified factor. The proof and every source helper used were read; /root/archive_kummer independently reported a full pass.

The literal source witnesses first give exponent 133, and replacing sums of exponents by maxima gives 37. The seventh-power bound uses the additional exact highest-weight calculation. This does not assert a proof of the separately defined CorG proposition or a new compiled Lean lemma.

The exact further gate VK-TRACE-GCD is

\[
|K_{4k}(\mathbb Z)|\mid
\gcd(|n_7(2k)|,|n_{11}(2k)|)^2,
\]

where the nonzero integers are products over the complete source Frobenius trace data,

\[
n_p(e)=\prod_s q_p^e\bigl(t_s-(q_p^{-e}+1+q_p^e)\bigr),
\quad q_7=7,\ q_{11}=121.
\]

The 7- and 11-primary K-parts are already zero, so the auxiliary-prime exclusions cause no gap. Numerical values of these products have not been computed. The fixed-level cohomology constants also have not been evaluated. Thus no new specified degree vanishing, including K12 or K16, is claimed.

The integrated TeX is work/k_groups_section.tex, with bibliography entries in work/k_groups_bibitems.tex. It includes the finite-coefficient Poitou--Tate sequence, the exact injection orientation, and the Mittag--Leffler/Jannsen (3.1) limit argument. Every proof in that section was read after writing. TeX structural checks pass, but a local pdflatex compilation was blocked by a missing pdflatex.fmt; no successful rendering is claimed.
