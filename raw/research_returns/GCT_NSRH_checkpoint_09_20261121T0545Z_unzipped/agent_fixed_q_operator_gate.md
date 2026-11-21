# F42: fixed operators, extension-dependent grading, and a finite-spectrum obstruction

Author: `/root/gct_statements`, GPT-6 Astra Pro; inherited effort not exposed. Date: 21 November 2026 UTC. Status: complete elementary proof; independent review requested. This is a precise comparison result for the actual generator and tensor module already established in F19/F21, not a historical priority claim about finite-spectrum sequences or representation categories.

## 1. The actual trace family

Use the consistent Hecke convention from GCT IV section 3.1: c_i squared equals delta c_i, delta = v+v^{-1}, and the other rank-one element is c_i-delta. The source's section 11 printed assignments interchange the exponents; we do not silently use those inconsistent assignments. Equation (93), label `e sP definition`, gives the intended symbolic nonstandard generator

\[
 P_i=c_i\otimes c_i+(c_i-\delta)\otimes(c_i-\delta),
 \qquad D=\delta^2=v^2+2+v^{-2}.
\tag{O1}
\]

The two rank-one terms are orthogonal and each squares to D times itself, so

\[
 P_i^2=DP_i.
\tag{O2}
\]

On the actual rank-three tensor module of dimension 64 from F21, P_1 has eigenvalue D with multiplicity 40 and eigenvalue zero with multiplicity 24. Indeed the scalar positive block has multiplicity 20, the scalar zero block multiplicity 4, and the two two-dimensional blocks occur 16 and 4 times. On each two-dimensional block P_1 has rank one and trace D. Consequently, for every integer k at least one,

\[
 \operatorname{Tr}_{M}(P_1^k)=40D^k.
\tag{O3}
\]

Fix a real q greater than one. Under either of the all-extension substitutions v=q^{n/2} and v=q^{-n/2}, put

\[
 D_n=q^n+2+q^{-n}.
\]

Then (O3) becomes the exact sequence

\[
 u_{k,n}=40D_n^k
 =40\sum_{j=0}^{2k}\binom{2k}{j}q^{(k-j)n}.
\tag{O4}
\]

Every coefficient is nonzero. The 2k+1 roots are distinct.

## 2. No one finite Frobenius space can realize all these words

**Theorem O-A.** There is no finite-dimensional complex vector space V, fixed invertible operator F on V, and collection of endomorphisms T_k on V, for an unbounded set of positive integers k, such that

\[
 \operatorname{Tr}(T_kF^n)=40D_n^k
\tag{O5}
\]

for every sufficiently large integer n. The lower threshold may depend on k. No commutation between T_k and F is assumed. In particular this excludes a dictionary using T_k=P^k for one fixed generator P. It also excludes a bounded finite-dimensional graded or derived realization with Euler supertraces and one common finite Frobenius spectrum.

**Proof.** The generating function of the left-hand side, starting at n=0, is

\[
 \operatorname{Tr}\bigl(T_k(1-TF)^{-1}\bigr).
\tag{O6}
\]

It is rational, and all of its poles belong to the fixed set of inverses of the eigenvalues of F. Jordan blocks can increase pole orders but do not add pole locations. Removing finitely many initial terms changes a generating function by a polynomial and does not affect its finite poles.

The generating function of (O4) is

\[
 40\sum_{j=0}^{2k}\binom{2k}{j}
       \frac{1}{1-q^{k-j}T}.
\tag{O7}
\]

Each of its 2k+1 poles is genuine: at a particular inverse root only its corresponding summand has a pole, with nonzero residue. Therefore the number of distinct eigenvalues of F must be at least 2k+1. A fixed finite-dimensional V cannot satisfy this for unbounded k. For a finite graded object, apply the same argument to the union of its even and odd Frobenius spectra. For a bounded complex, take its finite-dimensional cohomology and its Euler trace. This proves all versions. QED.

An even shorter argument without the finite-dimensional lower bound uses exponential growth. For fixed k, the left side of (O5) is bounded by C_k n^h R^n, where R is the maximum absolute value of an eigenvalue of F and h is a fixed Jordan bound. The right side has growth radius q^k. Thus R is at least q^k for unbounded k, which is impossible. The pole proof also yields the following stronger normalization statement.

**Corollary O-B.** The conclusion remains true if the desired right side for each k is multiplied by a nonzero scalar a_k and one nonzero exponential factor beta_k^n, with beta_k allowed to depend on k. In particular, word-dependent signs, nonzero scalar renormalizations, and single Tate shifts do not produce a common finite Frobenius space.

**Proof.** Its 2k+1 distinct roots are beta_k q^{k-j}, still with nonzero coefficients. A common finite Frobenius spectrum must contain all of them for each k, and hence have at least 2k+1 elements. QED.

The theorem does not assert that the separate fixed-word sequence is impossible: (O4) is a finite positive sum for each k. It proves that clearing the denominators in F26 does not repair a dictionary that insists on one fixed finite Weil space carrying all words while retuning v at every extension. The impossibility holds even after weakening the dictionary to unrelated T_k on that common space; tensor relations cannot repair it. The argument uses one fixed tensor module at tower rank three, so growth of the tower rank is not responsible.

## 3. A valid fixed-q action and tensor-family comparison

The obstruction does not apply when the quantum parameter is fixed once. Let q be a prime power, let ell differ from its characteristic, and choose a coefficient field E containing v_0=q^{1/2}. Set delta_0=v_0+v_0^{-1} and D_0=delta_0^2, which is nonzero.

Here is a concrete minimal **action comparison axiom**, rather than equality of scalar traces. Let M_{r,q}=(V_q tensor W_q)^{tensor r} be the actual ordinary tensor module with the nonstandard generators obtained from the two Hecke actions at v_0. Let A_{r,q} be the actual image algebra generated by these specified operators. Require objects H_r in finite-dimensional E-Weil representations, fiber isomorphisms

\[
 \omega(H_r)\simeq M_{r,q},
\]

and right A_{r,q}-actions by Weil endomorphisms, satisfying both:

1. The fiber isomorphisms intertwine every named P_i, not only its trace or its isomorphism class as an abstract algebra element.
2. The identifications H_r tensor H_s = H_{r+s} and the corresponding fiber maps intertwine the actual local operators on disjoint consecutive tensor blocks. These identifications obey the ordinary tensor associativity constraints.

Restriction from F_q to F_{q^n} raises the Frobenius on H_r to its nth power while keeping these operators and v_0 fixed. This last convention is part of the axiom. There is no assertion that the formal quantum variable is the extension-dependent Frobenius eigenvalue.

**Proposition O-C.** This action comparison axiom has an exact construction for the whole actual tensor family.

**Proof.** Give the vector spaces V_q and W_q the identity Frobenius and give every tensor power the resulting identity Frobenius. Every specified Hecke and nonstandard generator matrix is then a Weil endomorphism. Use the actual local Hecke action of GCT IV section 6.1, label `e T inverse_i act on V`, and form (O1) on the two factors. Since the matrices are unchanged, every relation between the actual operators is unchanged. Their locality proves the compatibility on disjoint tensor blocks, and the usual vector-space tensor associativity gives the coherence. This constructs H_r and all required fiber isomorphisms. QED.

We deliberately use the actual image algebras. For fixed dimensions two and arbitrary r, this is the two-row nonstandard quotient, not a claim that the full abstract nonstandard Hecke algebra acts faithfully at every rank. Nor is a braided functor to the ordinary symmetric Weil category asserted: the quantum Hecke operators are extra specified morphisms, not the target category's symmetry maps.

In this construction the normalized operators e_i=P_i/D_0 are actual idempotents. Division by D_0 is ordinary scalar division in E. Finite-dimensional Weil representations are idempotent complete, so their images are actual Weil subobjects. No tensor object with trace D_n is inverted. Thus this normalization avoids F38 for exactly the stated reason. It preserves the fixed-q action and its tensor relations, including the named generators, while abandoning the literal all-extension retuning dictionary excluded by Theorem O-A.

The trace dictionary is now

\[
 \operatorname{Tr}\bigl(w(P_i(v_0))F_r^n\bigr),
\tag{O8}
\]

with a fixed F_r, and is constant in n for the displayed construction. It is not the arithmetic substitution of v=q^{n/2} into the formal word trace. For example the normalized mixed-word trace from F26 is the constant 24+16/D_0^2. This is a valid trace of a fixed endomorphism; it is not automatically an Euler trace of an object with that same constant multiplicity. In particular a trace of the product e_1e_2 must not be identified with the dimension of an idempotent image: e_1e_2 need not be idempotent.

## 4. A valid coefficient-object dictionary for the quadratic subsystem

There is also a genuine all-extension object model for the individual coefficients in (O4), with the object permitted to grow with the word. In finite-dimensional E-Weil representations on a point, put

\[
 \mathcal D=E(-1)\oplus E^{\oplus2}\oplus E(1).
\tag{O9}
\]

The Tate convention is geometric Frobenius q on E(-1). Thus the trace of F^n on mathcal D is D_n. Define

\[
 \mathcal C_k=E^{\oplus40}\otimes\mathcal D^{\otimes k}.
\tag{O10}
\]

Its trace is exactly 40D_n^k for every n, and the canonical tensor identification C_{k+1}=D tensor C_k realizes multiplication by the coefficient D. Its dimension is 40*4^k and its distinct Frobenius roots are precisely the 2k+1 roots in (O4). It is mixed, with weights from minus 2k to 2k. No purity statement is inferred from coefficientwise positivity.

Even the one-generator quadratic relation has an explicit functor model. On the product category of 64 finite Weil-representation categories, let E_40 be projection onto 40 specified components, and let mathcal P be the endofunctor D tensor E_40. Then

\[
 \mathcal P\circ\mathcal P\simeq\mathcal D\otimes\mathcal P
\tag{O11}
\]

by the canonical tensor associativity and E_40 squared equals E_40. The same identifications are coherent for further powers. In the split eigenbasis of one generator, this models the rank-40/rank-24 action and the formal quadratic relation. It does not simultaneously identify the second nonstandard generator, its interactions, or the original tensor lattice. Those require a joint model; this proposition does not infer them from the one-generator relation.

This is a coefficient-object repair, not a fixed-space operator repair of (O5). The changing tensor powers C_k necessarily supply changing Frobenius spectra. A separate finite-state joint construction can be tested for all generators, but its action and coherence must be stated and verified, rather than deduced from the agreement of a few scalar traces.

## 5. Why even the exact fixed-q action is not the main sign bridge

The action comparison axiom of section 3 is necessary to make an action claim precise, but it is insufficient for the main F24 sign criterion. This can be demonstrated on an actual model, not merely asserted as missing geometry.

Take a constant rank-N sheaf on affine d-space, with identity Frobenius, and let any of the preceding fixed-q algebras act on its fibers. Its tensor and local-generator relations remain exact. Its pointwise trace is t_n(x)=N, so the pointwise hypothesis of F24 holds with a=0 and B=N. But its compact total trace is

\[
 M_n=Nq^{dn}.
\tag{O12}
\]

For d greater than zero its visible root q^d exceeds the claimed upper-bound radius q^{d/2}. Therefore the opposite-sign path-output comparison with the required sublinear boundary budget cannot hold for this sheaf on an unbounded even set. This follows directly from the already proved F24 theorem; all its input hypotheses hold, so its conclusion rules out that additional output comparison. Thus an exact action-compatible pure point model does not provide the path-sign comparison.

A meaningful stronger comparison must specify the actual geometric complex on the path hypersurface, the actual tensor/idempotent construction with which it is compared, and a morphism or triangle in Weil complexes that realizes the required odd shift and controls its cone. In particular the trace of a fixed non-idempotent word operator cannot substitute for an object Euler trace with real integer multiplicities. The positive output in F24 requires an actual one-parity contribution, or another verified source of positive visible spectral coefficients, after the stated comparison. The report does not claim such a triangle for the GCT objects.

## 6. Exact implications and remaining comparison choices

The three notions are therefore separated by explicit results:

- Fixed-q operator action: the actual generator and tensor relations admit the construction in Proposition O-C, with scalar normalization and pure identity Frobenius.
- All-extension coefficient objects for fixed words: (O9)--(O11) provide a genuine positive model for the quadratic subsystem, with changing objects and mixed weights.
- A common finite Weil space realizing all arithmetic-substituted word traces: Theorem O-A rules this out for the actual rank-three generator, even after clearing denominators and allowing Jordan blocks or a monomial normalization of each word.

None of these statements identifies the VIII designated bar-invariant integral bases or proves their positivity, and none upgrades fixed-q numerical positivity to coefficientwise positivity in a formal Laurent variable. For example x^2-x+1 is positive for every real x but has a negative coefficient. A q-independent graded and based comparison is an additional mathematical condition, not a consequence of the fixed-q model.

No assertion is made against infinite completed spectra, word-dependent finite coefficient objects, non-atomic traces, or other tensor products. The common-space theorem is exactly about finite total Frobenius dimension. It is independent of the smooth special-fiber repair F40, whose category-level TP spectrum is not asserted to encode these arithmetic-substituted word traces.

## 7. Source and verification record

Primary supplied source read in context: `sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`, section 6.1 (`ss commuting action on Vtsrr`, `e T inverse_i act on V`) and section 11.1 (`d nonstandard Hecke algebra`, equation (93), `e sP definition`). The section-3.1/section-11 normalization discrepancy is retained explicitly, as established in the earlier exact-source audit. The rank-three multiplicities and matrices are the completely proved F19/F21 results and their saved exact symbolic certificates. No additional external theorem is required for Theorem O-A, Corollary O-B, or the displayed point-Weil constructions.

Author verification: complete algebraic derivation, full finite-pole proof including eventual equality, explicit tensor construction, and exact check of the countermodel's F24 hypotheses. No numerical experiment or formal proof assistant was used. Independent full review remains requested.
