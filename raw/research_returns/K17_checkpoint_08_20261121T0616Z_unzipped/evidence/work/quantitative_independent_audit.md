# Independent audit: the seventh-power K-group estimate

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, agent `/root/archive_kummer`. Effort setting: not exposed. This is a source-content and ordinary mathematical proof review, not a Lean execution or a fresh verification of the imported automorphy theorems.

## Verdict

**Pass under the source contract used by the main paper.** The whole argument in `work/k_quantitative_refinement.md` was read, including the final individual trace-integer divisibility and gcd consequences. Its use of standard highest-weight theory sharpens the actual source construction, rather than merely asserting a smaller bound for an unspecified coefficient representation. No mathematical correction is requested. The remaining constant consists of fixed arithmetic cohomology bounds; it has not been numerically evaluated.

The resulting conclusion is that some positive natural number C satisfies

    log |K_(4k)(Z)| <= C (2k)^7       for every k >= 1.

The displayed choice C = 20 D is valid for the D defined below. For each e = 2k, the constructed nonzero integer n_7(e) satisfies

    |K_(4k)(Z)| divides |n_7(e)|^2.

The analogous n_11 gives divisibility by the square of their gcd. This does not prove all these K-groups vanish, does not compute the integers, and does not supply a numerical C. It is not a claim that the general proposition `HeightAndVanishing/Counts.lean:CorG` has been compiled or proved by this review.

## 1. Files read in full

All of the following source files in `work/quantitative_sources/` were read completely, including their proofs rather than only declaration signatures:

- `Scalar.lean`, `ExistsScalar.lean`, `ExistsTens.lean`, `WeylC.lean`;
- `CohBoundFree.lean`, `KlevThree.lean`, `CrystallineKlevThree.lean`;
- `CountK.lean`, `CountP.lean`, `CountQ.lean`, `CountSys.lean`;
- `CountQuadraticOfHyp.lean`, `RootSum.lean`;
- `FrobeniusTraceCountBoundOfCmEigensystemCount.lean`, `FrobeniusTraceCountBoundOfRatEigensystemCount.lean`;
- `Classifies.lean`, `FrobeniusTraceNormNonzeroLogBound.lean`, `CongruenceNumberRankThree.lean`.

The last file contains statement organization; it is not itself treated as a proof of every named proposition. `work/k_quantitative_refinement.md` and `work/vandiver_k.md` were also read in full. The SmallClassNumbers theorem and local coefficient definitions had already been independently reviewed; see `work/step17_independent_audit.md`.

## 2. The exact coefficient dimensions apply

The source sets, with indices starting at zero,

    nu_j = j + 1 + H - m_(n-1-j),       N_det = n + H.

For rank three the inputs are m = (e-1,-1,-e-1), H = e+1. Therefore nu = (2e+3,e+4,5), N_det = e+4, and the determinant-adjusted highest weight is (e-1,0,1-e). For rank two the inputs are m = (e,-e), H = e, giving nu = (2e+1,2), N_det = e+2, and adjusted weight (e-1,-e). All nonnegativity and dominance requirements hold when e >= 1.

The essential implementation point is the call to `Scalar.scalar`. It replaces the initial polynomial representation by the span S of the matrix orbit of a nonzero highest-weight vector v of weight nu. In a semisimple finite-dimensional rational representation of GL_n(C), write the nu-isotypic part as L_nu tensor M. Every nonzero irreducible projection of a vector killed by the upper nilpotent algebra and of weight nu has highest weight nu. Hence v is a highest-weight basis vector in L_nu tensored with a single vector of M, and its GL_n orbit spans one copy of L_nu. The span of the full matrix orbit equals this span: applying any linear functional annihilating the invertible-matrix orbit gives a polynomial in matrix entries vanishing on the Zariski-dense invertible locus, hence vanishing on all matrices. Thus the source scalar representation has dimension exactly the Weyl dimension of L_nu.

The rank-three Weyl factors are e, e, and (2e)/2, giving e^3. The rank-two factor is 2e. Determinant twisting preserves dimensions. `ExistsTens.exists_tens` constructs an irreducible coefficient with dimension at most the scalar dimension to the number of complex embeddings. Over every imaginary quadratic field used here, this proves the bounds e^6 and 4e^2. Its infinitesimal character is retained by the existing construction. No assertion that the quantum determinant uniquely identifies every irreducible is needed.

The underlying complete reducibility, highest-weight classification, and Weyl formula are standard representation-theoretic inputs cited in the candidate. The application to the particular cyclic module and all displayed arithmetic were independently checked here.

## 3. Fixed levels do not introduce a power of e

The source `CohBoundFree` estimates total cohomology by a constant times the coefficient dimension, with a separate power of the level M. For any one fixed field, rank, and level, absorb that level factor into a positive constant. The `cardK` and `cardP` proofs actually use this linear dimension estimate before coarsening the coefficient and level into a single polynomial bound. Thus retaining the sharper dimensions in those proofs is legitimate.

For K = Q(sqrt(-3)) and N = 2, the rank-three cohomology level is 3N = 6. In the rational rank-two branch M = N |disc K| = 6 and the cohomology level is 3M = 18. None depends on e, p, or ell. Choose positive natural constants B_0 and B_i for these fixed total cohomology bounds.

`CountSys` indexes entire eigenvalue systems and bounds them by pairwise nonisomorphic representations. The trace conversion maps preserve the cardinality of this index set. Consequently the argument has not incorrectly replaced multiplicities by the number of distinct traces at a single prime.

## 4. The six-field count and its factor are correct

For rank n = 2 the source quadratic argument chooses n^2 + 2 = 6 fields with pairwise coprime discriminants. At a given prime p at most one is excluded, so five are available. The quadratic self-twist estimate is n^2 = 4, and ensures an irreducible restriction among those five. The fields of discriminants -3,-7,-11,-19,-23,-31 are a legitimate fixed choice.

For a selected field, the Frobenius residue degree is either one or two. `RootSum` allows at most 2^n possible root multisets and a Boolean factor recording the two possible lifts. Its full multiplicity factor is 2^(n+1) = 8. Therefore the rank-two count is bounded by

    8 sum_(i selected) (4 B_i e^2)
      <= 32 (sum_(i=1)^6 B_i) e^2.

No extra factor of five is necessary: the selected five fields inject into the fixed set of six and the summands are nonnegative. The source's coarser comparison with a common sum of constants can be replaced by this direct bound. Adding the rank-three branch gives

    #D_(p,e) <= B_0 e^6 + 32 (sum_i B_i) e^2 <= D e^6,
    D = B_0 + 32 sum_i B_i.

This constant is positive and independent of e and p.

## 5. The norm estimate adds just one power

For the trivial character orbit, the source trace product is

    n_p(e) = product_s q^e [t_s - (q^(-e)+1+q^e)],
    q = Norm(w) = p^f,       f in {1,2}.

The source proves it is a nonzero rational integer. Integrality is obtained after multiplication by q^e; Galois-stability of the full index system gives rationality; nonvanishing follows from |t_s| <= 3 and q^(-e)+1+q^e > 3. Its proved archimedean estimate is

    log |n_p(e)| <= #D_(p,e) [2e log q + 1].

As q <= p^2, e >= 1 and p >= 7, the bracket is at most 5e log p. Thus

    log |n_p(e)| <= 5D e^7 log p.

The OneChar/orbit valuation argument is unchanged by the sharper counting bound. For ell != p in the theorem's range, it gives the strict Selmer length at most 2 v_ell(n_p(e)). There is no use of an infinite sum: all integers and K-groups involved are finite, and the final prime sum is their finite prime support.

## 6. The all-prime K step and individual divisibility

For e = 2k, k >= 1 and ell odd, compact/discrete Poitou--Tate identifies the strict Selmer kernel with the dual of H^2(Z[1/ell],Z_ell(e+1)). The local and global invariant groups of Q_ell/Z_ell(-e) are equal because both cyclotomic images are Z_ell^times, so the final local H^2 term cancels. Etale K-theory comparison then gives the dual of K_(2e)(Z){ell}. The extra local condition at 2 in the recovered source is automatic: its unramified subgroup is D/(2^(-e)-1)D = 0 by divisibility. These arguments were independently checked in the step17 audit and rechecked against the full Vandiver notes here.

For primes excluded by (ell-1) | 2e, the relevant cyclotomic class-group character has order one or two. The trivial component vanishes by norm to Q. The nontrivial case has ell = 1 mod 4 and descends to Q(sqrt(ell)); Minkowski's bound and a quadratic ideal count give h(Q(sqrt(ell))) < ell. Extension after norm multiplies the invariant class by (ell-1)/2, a unit on ell-primary groups, hence that component vanishes. The detailed inequality h <= floor(sqrt(ell)/2)^2 <= ell/4 < ell and its hypotheses were checked. The 2-primary theorem and trivial mod-3 component remove ell = 2,3.

Taking p = 7 leaves only the 7-primary part uncovered by the trace inequality. That part vanishes independently because 7 is regular. Consequently every prime valuation of |K_(4k)(Z)| is at most twice its valuation in n_7(2k), proving the stated divisibility. It follows that

    log |K_(4k)(Z)| <= 10D log(7) (2k)^7 < 20D (2k)^7.

The same argument with the regular prime 11 gives the second individual divisibility and therefore the gcd divisibility. The facts that 7 splits and 11 is inert in Q(sqrt(-3)) give q_7 = 7 and q_11 = 121; they are consistent with the general q <= p^2 bound.

## 7. Limits of the result

The explicit exponent seven is established relative to the stipulated source arithmetic inputs. The constants B_i and the trace systems are not computed here. Thus no new vanishing of K_12(Z) or K_16(Z), no all-prime Vandiver statement, and no numerical range follows solely from this estimate. The candidate clearly maintains these distinctions. The finite-group illustration in its final section is explicitly a logical illustration, not an arithmetic counterexample.

The candidate's current-literature search claims were read for consistency but were not independently repeated as part of this quantitative proof audit. The exact printed primary theorem locators for standard K-theory, duality, and the low-prime computation are supplied by the main source review; this audit does not pretend to reprove them.

## 8. Polynomial-certificate follow-up

The entire `work/k_numeric_followup.md` was subsequently read, and its elementary mathematics in sections 1--3 was independently checked. Its trace polynomial F(X) is monic integral by the integral, Galois-stable indexed trace system, and n_p(e) = (-1)^degree(F) F(E), where E = q^(2e)+q^e+1. Nonvanishing follows from E > 3q^e and the trace absolute-value bound. These facts give the stated square divisibility.

If a nonzero monic integral polynomial P is divisible by F in Q[X], monic division gives an integral quotient. Since F(E) is nonzero, F and X-E are coprime in Q[X]. Removing the maximal power of X-E from P preserves divisibility by F, gives an integral polynomial P* and ensures P*(E) is nonzero. Evaluation gives F(E) dividing P*(E) in Z. Thus the larger-polynomial and gcd variants are correct. The warning that one cannot instead take a squarefree part is necessary and present: source indices, including multiplicities, must be covered.

The substitution of the regular split prime 13 for 11 is valid. An independent exact rational Bernoulli recurrence gives numerators 1,-1,1,-1,5 for B_2,...,B_10, proving regularity of 13 by the usual criterion. Direct modular enumeration gives roots 2,5 of X^2+3 modulo 7 and roots 6,7 modulo 13, so both primes split in Q(sqrt(-3)). Exact integer exponentiation reproduces every evaluation point in the follow-up:

| e | p=q | q^e | E |
|---|---|---|---|
| 6 | 7 | 117649 | 13841404851 |
| 6 | 13 | 4826809 | 23298089949291 |
| 8 | 7 | 5764801 | 33232936334403 |
| 8 | 13 | 815730721 | 665416609998910563 |

The scalar dimensions e^3 are 216 and 512, and coefficient bounds e^6 are 46656 and 262144. These computations were run in Python using exact integers and `fractions.Fraction`, without numerical eigenvalues. The follow-up correctly treats multiplicity-preserving coverage of the complete trace system and the integral normalization as prerequisites of any actual Hecke computation. No qualifying polynomial or gcd was computed. Its literature-search discussion was read but not independently repeated here.
