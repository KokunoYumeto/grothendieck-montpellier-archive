# Exact polynomial certificates for the remaining small-degree gate

Date: 2026-11-21 UTC. Author/reviewer: GPT-6 Astra Pro, agent /root/vandiver_k. Effort: not exposed. This is a mathematical follow-up to k_quantitative_refinement.md, under its same stipulated source contract. No qualifying trace polynomial has been numerically computed in this run.

## 1. Polynomial evaluation removes the need to enumerate algebraic roots

Fix e = 2k > 0, K = Q(sqrt(-3)), N = 2, and a regular auxiliary prime p >= 7 different from 3. Let w divide p, q = Norm(w), and D = D_(p,e) be the full finite trace system used in the source congruence-integer construction. Retain its complete index set S, including multiplicities. Put

    F_(p,e)(X) = product_(s in S) (X - q^e t_s),
    E_(p,e) = q^(2e) + q^e + 1.

Then F_(p,e) is a monic polynomial in Z[X]. Indeed, each q^e t_s is an algebraic integer, and every complex-field automorphism permutes the indexed multiset. Every coefficient is therefore an algebraic integer fixed by all automorphisms of the algebraic closure of Q, hence is rational and integral. This uses precisely TrData.int and TrData.conj in Classifies.lean; it requires no conjectural identification of a Hecke space.

With d = |S|, the actual source integer is

    n_p(e) = (-1)^d F_(p,e)(E_(p,e)).

This follows term by term from q^e(t_s - (q^(-e)+1+q^e)) = q^e t_s - E_(p,e). The bound |t_s| <= 3 and q >= 7 imply E_(p,e) > 3q^e, so this evaluation is nonzero. The previously proved all-prime valuation argument gives

    |K_(2e)(Z)| divides |F_(p,e)(E_(p,e))|^2.

Thus an exact characteristic-polynomial computation is sufficient; explicit algebraic eigenvalues or a factorization into number fields are not necessary. One must still certify the entire trace system and all its multiplicities.

## 2. A certified larger polynomial also suffices

Suppose P_(p,e) is a nonzero monic polynomial in Z[X] for which F_(p,e) divides P_(p,e) in Q[X]. Since F is monic integral, polynomial division and Gauss's lemma give P = FQ with Q in Z[X]. An overcount is therefore harmless for this divisibility application, provided it includes every required root with at least the required multiplicity.

If P(E) is zero, divide P by the maximal power (X-E)^a and call the quotient P*. Every such division remains in Z[X], and P*(E) is nonzero. As F(E) is nonzero, F has no factor X-E. Unique factorization in Q[X] implies F divides P*; monic division again puts the quotient in Z[X]. Consequently

    |K_(2e)(Z)| divides |P*_(p,e)(E_(p,e))|^2.

This algebraic removal can eliminate exact Eisenstein eigenvalues from a larger Hecke module without computing a cuspidal projection. It does not itself certify that an arbitrary Hecke module contains all the source representations, or supply the needed integral normalization. Those remain explicit mathematical hypotheses of the computation. Distinct representations can have the same trace at one prime, so replacing P by its squarefree part is not justified.

If two regular auxiliary primes p and r provide such polynomials, define the positive integer

    G_e = gcd(|P*_(p,e)(E_(p,e))|, |P*_(r,e)(E_(r,e))|).

Then |K_(2e)(Z)| divides G_e^2. It is sufficient to prove that every prime factor of G_e is below 2^31, because the already verified Vandiver range kills each such primary part. It is also sufficient to verify just the corresponding class-group component at each prime factor. This is a finite certificate condition, not a claim that either G_e or its factorization has been obtained here.

## 3. Prefer two split auxiliary primes for a first calculation

Both 7 and 13 split in Q(sqrt(-3)); both are regular. Regularity of 13 follows directly from the numerators 1, -1, 1, -1, 5 of B_2, B_4, B_6, B_8, B_10. Thus p = 13 may replace the previously displayed p = 11 and gives q = p at both auxiliary places. The earlier p = 11 argument remains valid, with residue-field order q = 121. The rank-three representation is a representation of G_K; no extension to G_Q is assumed in either argument.

Exact evaluation points, checked by integer arithmetic:

| K-group | e | p | q | q^e | E = q^(2e)+q^e+1 |
|---|---:|---:|---:|---:|---:|
| K_12 | 6 | 7 | 7 | 117649 | 13841404851 |
| K_12 | 6 | 13 | 13 | 4826809 | 23298089949291 |
| K_16 | 8 | 7 | 7 | 5764801 | 33232936334403 |
| K_16 | 8 | 13 | 13 | 815730721 | 665416609998910563 |

The coefficient highest weights for the source GL_3 cohomology are (5,0,-5) in the first row-pair and (7,0,-7) in the second. Their scalar complex dimensions are 216 and 512; the two-embedding coefficient bounds are 46656 and 262144. These are coefficient dimensions, not computed dimensions of the automorphic spaces.

## 4. What existing computational sources do and do not supply

The official Magma v2.30-1 handbook gives a working example for definite rank-three unitary modular forms over Q(sqrt(-7)), including weight (3,0,-3), complete Hecke decomposition, eigenvalues, and congruence calculations. See Further Examples, the subsection titled “Unitary Forms of Rank 3 and Discriminant -7,” especially the commands beginning UnitaryModularForms and the discussion following the two-dimensional summands:

https://docs.magma-maths.org/v2.30-1/ModularArithmeticGeometry/AlgebraicModularForms/further-examples.html

The example is evidence that relevant exact computational machinery exists. It is not a table for the field, level, and weight required here, and it does not prove a transfer theorem covering the source's whole Adm3 set. In particular, one may not silently identify its default lattice-stabilizer level with the principal level in the source.

Assaf, Fretwell, Ingalls, Logan, Secord, and Voight, “Definite orthogonal modular forms: computations, excursions, and discoveries,” Research in Number Theory 8 (2022), article 70, section 3.1, describes the neighbor/isometry method and its extension to Hermitian lattices and arbitrary weights. The paper also notes multiplicity issues for nonmaximal lattices. These are implementation results for the specified spaces; they do not by themselves establish the missing coverage of our source trace system.

https://doi.org/10.1007/s40993-022-00373-2

Greenberg and Voight's primary algorithm reference is “Lattice methods for algebraic modular forms on classical groups,” arXiv:1209.2460; author PDF:

https://jvoight.github.io/articles/orthohecke-240123.pdf

This last article was located, but its entire proof was not read in this follow-up, so no new proof-verification claim is made for its algorithm.

Bergström and van der Geer, “Picard modular forms and the cohomology of local systems on a Picard modular surface,” arXiv:2012.07673 / Commentarii Mathematici Helvetici 97 (2022), 305–381, works over Q(sqrt(-3)). Its abstract expressly makes the proposed Eichler–Shimura formula conjectural and states that the indicated Hecke traces are computed assuming it. Therefore those traces cannot be substituted as an unconditional complete certificate here on the strength of that abstract. The same abstract separately identifies unconditional results on dimensions and Euler characteristics; they are not the asserted trace formula.

https://arxiv.org/abs/2012.07673

Targeted primary-source searches in this run did not locate exact polynomials at our required field/level/weights together with the completeness and transfer certificate. This is a report of this search, not a theorem that no such calculation exists.

## 5. Next exact data requirement

For e = 6 or 8, produce an integral Hecke model whose polynomial at p = 7 and p = 13 has a proved multiplicity-preserving inclusion of the source's scaled trace multiset. The model may be larger, by section 2. Record the level, coefficient representation, Galois/Frobenius convention, integral scaling q^e, and the coverage proof. Then strip only the exact scalar root E, evaluate, take the gcd, and certify its remaining prime factors. Each stage is finite and independently checkable. No floating-point spectrum or dimension-only count can replace the coverage proof.

The results completed now remain the exponent-seven global estimate, its individual integer divisibility and gcd refinements, and the explicit finite certificate reduction. No new K_12 or K_16 vanishing follows without the missing exact input data.

## Root follow-up, 2026-11-21 01:26 UTC

A renewed primary-source search confirmed that the authors' 2019 Voronoi preprint, Remark 6.6 p.19, identifies H_12(Vor_GL_N(Z)) for N=9,10,11 as the missing computation in that route to K_12. Search indexing dates were not treated as publication dates: the author PDF is arXiv:1910.11598v1, 25 October 2019. A local executable search found no Sage, Magma or PARI/GP executable in the checked standard locations. This records the available environment, not a mathematical impossibility of the finite calculation. The source Hecke coverage gate remains.
