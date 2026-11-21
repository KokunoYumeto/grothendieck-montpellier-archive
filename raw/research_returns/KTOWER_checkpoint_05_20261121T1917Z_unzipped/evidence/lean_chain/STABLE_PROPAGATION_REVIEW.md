# Independent whole-proof review of stable residual propagation

Date: 2026-11-21 UTC. Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.

## Verdict

**PASS for KT-STABLE-PROPAGATION and KT-STABLE-LARGE-PRIME**, with the exact ambient-automorphic scope stated in the proof. I read the entire `main_gate/stable_residual_propagation.tex`, including the later explicit estimates SP.2a–SP.2b, and the entire seed certificate program. The finite-group growth, simultaneous Hecke propagation, integral eigenflag argument, stable-dimension subtraction, residual Galois conclusion, and carried rational vanishing implications are valid. The separately reviewed rank-three spectral exhaustion theorem is the required background for identifying the complement of the endoscopic space as stable.

The conclusion is stronger than a coincidence at one Hecke prime: for every sufficiently large even e congruent to the seed modulo ell−1, at least one actual stable automorphic eigensystem has the Eisenstein residual system simultaneously at all good split primes and hence globally over E. It does **not** establish an actual point of the deformation ring, the archive predicate Adm3U_s, a rational Selmer class, or nonzero K-theory. The stated example instead has zero rational K-primary part throughout its weight progression.

## 1. The finite-group asymptotic

The weight (a,0,−a) has dimension (a+1)^3 and trivial scalar action, so the reduction of an algebraic integral lattice acts through PGL3(F_ell). Any ell-regular projective element has an ell-regular lift to GL3(F_ell), since a power of that lift is scalar of order dividing ell−1. Evaluation of the formal weight character at compatible lifted roots of unity gives its Brauer character independently of the choice of lattice.

The displayed Weyl numerator has exponent columns a+2,1,−a and denominator columns2,1,0. For three distinct eigenvalues its numerator is bounded by six. For exactly two equal eigenvalues, canceling one Vandermonde factor differentiates one row and introduces at most a linear factor in a. Three equal eigenvalues give precisely the identity in PGL3, where the character is (a+1)^3. Thus the O(a+1) estimate is valid at every nonidentity regular class; it does not inadvertently include unipotent classes.

The proof does not assume semisimplicity of the finite group algebra. The traces of its simple modules are independent as k-valued functions: a relation extends linearly to the algebra, and a lifted diagonal matrix unit in one factor of the semisimple quotient isolates its coefficient. A group element and its ell-regular part have the same modular trace, because the commuting ell-part is unipotent on each regular eigenspace. Hence there is a nonzero maximal minor on regular classes. Compatible cyclotomic lifts give a Brauer-character minor whose determinant has nonzero reduction and is therefore nonzero in characteristic zero.

The regular module has Brauer character N at the identity and zero at all other regular elements, where N=|G|. Subtracting (a+1)^3/N times that character cancels the entire cubic contribution. Applying the inverse fixed minor proves the claimed asymptotic for every simple composition multiplicity. Each leading coefficient is positive because every simple is a quotient of the regular module. This is a Jordan–Hölder multiplicity statement; replacing it by an argument about direct summands would not have been justified.

## 2. The explicit estimate

The effective version is also valid. Central invariance permits division of all eigenvalues by one of them. Their ratios have orders dividing N, so distinct ratios are separated by at least4/N on the complex unit circle. The ordinary Vandermonde denominator has three such factors. The repeated-root denominator has two, while the differentiated numerator is bounded by6(a+2). Both cases satisfy the stated bound N^3(a+2).

A simple module has dimension at most N. For an invertible minor of size r<=N, its entries and all cyclotomic conjugates therefore have absolute value at most N; the determinant and cofactors are bounded by H=N^(2N). All roots involved have order dividing the prime-to-ell part of N, so the cyclotomic field degree is at most N. The nonzero integral norm bounds the chosen determinant below by H^(−(N−1)), and hence every inverse entry above by H^N=N^(2N^2). The row sum gives the error N^(2N^2+4)(a+2) exactly as in SP.2a.

Writing C=N^(2N^2+4), the condition a>=N^(N^2+3) gives a^2/N>=NC and a+2<=2a. The lower bound is consequently at least a(N−2)C>a/3. This is an explicit sufficient threshold, with no assertion that it is close to the smallest one.

## 3. One fixed Hecke action, at every relevant prime

At split ell, the lattice model is integral for GL3(Z_ell). The finite image of Gamma has order dividing1296, so averaging is legitimate for ell>3. This exact idempotent both commutes with reduction and makes W↦uW an exact functor on finite G-modules.

The Hecke representatives are chosen in the fixed rational unitary group and preserve the lattice away from their own split prime q. For q≠ell their reductions are elements of G. They give fixed corner elements u(sum g_j)u, independent of a. Including both minuscule directions and all such q in the algebra H is essential. Although the generating set is infinite, H is a subalgebra of the finite-dimensional algebra u k[G]u. The proof selects a single character of this algebra, rather than selecting a potentially different eigenvector at each q.

The exact-functor argument is sound even without using the optional auxiliary-level argument for commutativity of the full corner action. The seed character occurs in uV_(a0), hence in uS for at least one simple G-composition factor S. Exactness and additivity then give its multiplicity in every uV_a at least [V_a:S]. The asymptotic, or the uniform effective lower bound, therefore applies to that same simultaneous character. On the actual modular-form spaces the operators are the usual commuting spherical Hecke operators.

## 4. Integral lifting and the stable summand

A finite-rank integral lattice has only finitely many independent endomorphisms. The characteristic-zero commuting spectral algebra and its eigencharacters split after one finite coefficient extension. Intersection with a common eigenline is saturated, so the quotient lattice is free. Repeating constructs the claimed invariant flag, and reduction remains exact at every step. The residue-character multiplicity equals the number of characteristic-zero eigenlines reducing to it, counted with their eigenspace dimensions.

The characteristic-zero compact spectral decomposition gives simultaneous diagonalizability. One may count the complete endoscopic summand first; it has only floor(a/3) dimensions for the even e=a+1 under consideration. Once the seed residue character occurs more often than that, some remaining line is stable. The finite-group argument supplies a cubic multiplicity, so this subtraction is valid. It does not assume that a single residual occurrence lifts to a chosen characteristic-zero packet.

## 5. Normalization, global residual traces, and attachment scope

The raw minuscule operator is q times the normalized standard trace; the opposite operator is q times the dual trace. Because q≠ell, division by q is permitted. The raw target q^(1−e0)+q+q^(1+e0) remains the same whenever e≡e0 modulo ell−1. This accounts for the exact progression in the theorem.

The two directions cover the two primes of E above a split rational prime. Such degree-one prime ideals have Frobenius classes dense in every finite quotient of G_E: in a normal closure over Q, Chebotarev applied to an element fixing E produces a rational prime splitting in E, and a place above it gives the desired element. Consequently simultaneous congruence at all those Hecke operators gives equality of the residual trace functions everywhere. Both residual systems factor through a finite common quotient. Independence of simple modular trace functions gives equality of composition multiplicities modulo ell; dimension3<ell makes those integer multiplicities equal, proving the displayed semisimplification.

I checked the exact published attachment statement in Shin, *Galois representations arising from some compact Shimura varieties*, Annals173 (2011), Theorem1.2, printed pp.1647–1648, including the following paragraph on a compatible system over a number field. It applies to the regular algebraic conjugate-self-dual cuspidal rank-three constituents supplied by the stable spectrum, with no even-rank slight-regularity condition. It gives a continuous semisimple system, local compatibility away from ell, and a finite coefficient field. The same normalization as in the reviewed compact coverage identifies its Frobenius traces. The statement does not itself prove characteristic-zero irreducibility, and none is required by this propagation theorem. In particular this attachment is not an automatic verification of the additional archive admissibility predicates.

Primary source: <https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p09-p.pdf>. Theorem1.2 is imported background; its trace-formula proof has not been reconstructed in this review.

## 6. The large-prime seed and rational vanishing

The entire `large_prime_seed_certificate.py` was read, then a byte-identical copy was freshly executed in this review directory. Trial division through91442 proves ell=8361790201 prime, and the exact Fraction Bernoulli recurrence gives

`B_(37,chi_-3)/37 = -1701990248643001964415638362402/3`.

The numerator is divisible by ell; the denominator is not. The prime is1 modulo3 and exceeds2^31. The inert-q=2 residue is6536635074, excluding CM for the produced level-three form. All output fields agree with the author's report; outputs are `large_prime_seed_replay.json`, `.log`, and `large_prime_seed_reconciliation.json`.

The previously checked Fretwell–Roberts sufficient theorem applies at weight37, level3 and the full primitive quadratic character. The already reviewed endoscopic injection gives the seed line in M17. At a split prime its standard parameter is1 plus the normalized two-dimensional parameter, whose determinant is one; its dual has the same trace. Thus both raw targets are exactly the targets needed in SP.9.

I read the whole carried K17-BERNOULLI-8361790201 statement and proof, input K17.tex lines5037–5128. Its complete two large enumerations give B_(ell−19)=1827838999 modulo ell. Those enumerations were not rerun here. K17-REFLECTOR therefore kills A^[−18], and the previously read all-positive-k comparison (K2) applies to every e=18+(ell−1)t. Only the class-group character index is periodic; no periodicity of K-group orders or isomorphisms is assumed.

## 7. Consequence and limits

For the entire compact stable spectrum over Q(sqrt(−3)), an all-weight determinant-unit assertion at every split test prime is false at this fixed prime above2^31. The counterexamples occur in every sufficiently large member of the displayed progression, while the corresponding rational K-primary parts vanish. Removing the endoscopic factor cannot remove them.

The theorem leaves open a proof based on the stricter actual source family, another auxiliary field, or the reflected rational class-group criterion. It does not supply a nonzero Selmer class, a Vandiver counterexample, or an Ihara conclusion. Actual check events, finite arithmetic replays, and imported background are distinguished in `CHECK_EVENTS.tsv`; no Lean kernel run is claimed.

Reviewed proof snapshot SHA256: `e85e67d73e92694f5febe956c0d16cbb6e868eface2add684239de7ecf87a443`.

## Added small-summand corollary

I read the complete added KT-PROPAGATION-SMALL-SUMMANDS statement and proof. It passes: a Hecke-invariant complement exists for the simultaneous semisimple characteristic-zero action; removing a subspace of dimension d removes at most d occurrences of the fixed residue character. Any o(a^3) family is dominated by the established positive cubic lower bound. This applies to endoscopy plus the proposed constructed symmetric-square subspace without asserting that the latter exhausts every possible symmetric-square origin. For a subspace stated only over C, the same dimension count inside the algebraically defined common eigenspaces produces an algebraic vector outside it; one need not impose an integral structure on an arbitrary transcendental choice of subspace. The explicit Shin paragraph has also been reread and accurately states the theorem scope.

Updated reviewed proof SHA256: `23676ef9ca0fcfb7dd0060f9854086be0f824410edc9e6c88f4eea8f3ace6805`.
