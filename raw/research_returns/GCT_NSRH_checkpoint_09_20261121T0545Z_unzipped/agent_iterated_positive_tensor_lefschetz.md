# F66 supplement — the positive whole tensor does not carry a single Lefschetz center

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This is separate from the F66 positive four-state report with the reviewed path-order coherence correction, SHA256 caae7ec42e5cd3b57a58d157fe0b3380cfe19d6d7df96e786b669ba5d07f78a1. It uses the same actual named action, not the negative simple projector. Its conclusion concerns an additional degree-two, single-center Lefschetz comparison. The pure point-complex construction in that report remains valid.

## 1. The actual unmarked two-word trace

Retain
\[
 \delta=v+v^{-1},\qquad D=\delta^2,\qquad
 d=D^2,\qquad A=D^2-8D+8.
\]
The four-dimensional actual iterated tensor has generic decomposition into the two scalar modules, with generator values d and zero, and the two-dimensional module N(A). Therefore its named two-word trace is
\[
 T(v)=\operatorname{Tr}(R_1R_2)
     =\operatorname{Tr}(S_1S_2)=d^2+A^2.
 \tag{HL1}
\]
Direct expansion gives
\[
 T(v)=2v^8+40v^4+64v^2+108
            +64v^{-2}+40v^{-4}+2v^{-8}.
 \tag{HL2}
\]
In particular the coefficients at v^{\pm6} vanish. All displayed coefficients are positive, and T(1)=320, matching d(1)^2+A(1)^2=16^2+8^2.

This is an unmarked trace on the entire four-state tensor. No effectiveness of the projector onto N(A) is assumed.

## 2. The precise single-center Lefschetz obstruction

Let V be a finite Z-graded vector space over a field of characteristic zero. A degree-two Lefschetz operator with center c means an operator L:V^j -> V^{j+2} and isomorphisms
\[
 L^i:V^{c-i}\xrightarrow{\sim}V^{c+i}
 \qquad(i\ge0),
 \tag{HL3}
\]
where c is an integer. We use dimensions, so any harmless one-dimensional Tate factor in the target is irrelevant for this definition.

### Proposition HL-A

No finite graded vector space with dimension polynomial T(v) admits (HL3), for any center. More generally, no Laurent monomial shift v^s T(v), s an integer, admits a degree-two Lefschetz operator about any single center.

### Proof

For T, the least and greatest nonzero degrees are -8 and 8. The symmetry of dimensions forced by (HL3) reflects the support about c, so its extrema give c=0. But V^{-8} has dimension two and V^{-6}=0. The first step of L^8:V^{-8} -> V^8 is zero. This contradicts its required invertibility.

For v^s T(v), the extrema instead force c=s. The same contradiction uses the zero space in degree s-6 between the nonzero spaces in degrees s-8 and s+8. QED.

### Corollary HL-B

T(v) is not the character of a genuine finite-dimensional algebraic SL_2 representation. Consequently there is no simultaneous realization of the actual named matrices R_1,R_2 by matrix kernels whose entries are genuine finite-dimensional SL_2 representations and whose characters, compositions and ordinary closed-word traces agree with the actual Laurent matrices and traces.

### Proof

In characteristic zero, a finite SL_2 representation has weight symmetry and a degree-two raising operator with the Lefschetz isomorphisms (HL3), centered at zero. In this particular case one can avoid this general formulation: the largest weight in T is eight, of multiplicity two. Each highest-weight-eight constituent contains a weight-six line, whereas T has no weight-six term. Constituents with larger highest weight cannot occur because their top terms would be visible. Thus the purported representation cannot exist.

For kernels, direct sums, tensor products and finite sums of diagonal entries all stay within genuine SL_2 representations. Their two-word closed trace would therefore be such a representation with character T, contradicting the first assertion. This deduction is independent of a state basis and needs no source simple projector. QED.

The hypothesis here is stronger than an effective graded kernel. The positive coefficient spaces X,Y in the F66 core are graded spaces; they are not asserted to be SL_2 representations. A Laurent monomial grading shift, or a nonzero positive constant multiple when it has integral coefficients, cannot remove the obstruction, by the same support-gap proof as HL-A. Arbitrary Laurent polynomial multiplication is not covered. A sum of separately centered Lefschetz pieces is not a single-center structure and is not excluded.

## 3. Exact arithmetic and projective-perverse scope

Fix a finite field F_Q, a prime ell not dividing Q and a finite ell-adic coefficient field E. Suppose a bounded point complex K is pure of an integral weight w and has Euler traces
\[
 \operatorname{Tr}_{\mathrm{Eul}}(F^n;K)=T(Q^{n/2})
 \tag{HL4}
\]
at every sufficiently large extension degree n. Then BBD5.1.8, pp126--127, and finite power-sum uniqueness force
\[
 \dim H^{e-w}(K)=[v^e]T(v)
 \qquad(e\in\{-8,-4,-2,0,2,4,8\}),
 \tag{HL5}
\]
with no other cohomology, and w is even.

Here is the full argument. Distinct nonzero power roots are linearly independent at sufficiently large consecutive integers by the Vandermonde determinant. The visible roots in HL4 are Q^{e/2}, whose point weights are e. Purity of K puts such a root only in degree e-w. A fixed root cannot cancel between different degrees, because its point weight fixes that degree. Hidden roots cannot cancel for the same reason. The visible Euler coefficients are positive; since every e is even, their degrees are even exactly when w is even. Their ordinary multiplicities are then the displayed coefficients. Jordan blocks do not change this argument.

### Proposition HL-C

There is no projective structure morphism f:X -> Spec F_Q, with X a scheme of finite type, and pure perverse sheaf P of an integral weight, for which K=Rf_*P has the Euler traces (HL4).

### Proof

Proper direct image preserves purity, using f_!=f_* and dual stability as in BBD5.1.13--14, p128. Thus K is pure of the weight w of P and satisfies HL5.

The relative hard-Lefschetz theorem, BBD Theorem5.4.10, p144, supplies a degree-two ample-class operator and isomorphisms
\[
 L^i:H^{-i}(K)\xrightarrow{\sim}H^i(K)(i)
 \qquad(i\ge0).
 \tag{HL6}
\]
The least and greatest cohomological degrees from HL5 are -8-w and 8-w. Their symmetry about zero forces w=0. Hence H^{-8}(K) has dimension two and H^{-6}(K)=0. The first step of the required map L^8 is zero, contradicting HL6. QED.

This proposition requires a pure **perverse** source and one ample-class Lefschetz structure. It does not exclude arbitrary pure complexes on a proper variety: the core's pure point complex already supplies a counterexample to such an overstatement, with the identity map of a point. Nor does it exclude separately shifted direct sums of projective constructions with different Lefschetz centers. The contradiction also requires the uninserted Euler-trace comparison (HL4); traces of an additional arbitrary endomorphism are not positive multiplicities and do not satisfy HL5 automatically.

The source iteration is still at strand rank r=3 and tensor-factor iteration k=4. This is not an all-r theorem, a refutation of signed/factored source positivity, or a claim that every source canonical coefficient has a projective-perverse realization. The new deduction narrows the extra geometric comparison needed for this actual whole-tensor action.

## 4. Separate Grothendieck dictionary

SGA3 I4.7.2--3 and cote90 scan17 supply representation/action language. The ordinary torus grading used by the positive four-state kernels is weaker than an action of SL_2 with its raising operator. SGA6 V Sections2--3 and cote133 scan18 distinguish effective representation classes from their virtual Grothendieck classes; no lambda-ring structure on the noncommutative word algebra is asserted.

The pure bounded point complex from the core lies in the perfect-complex framework of SGA6 I Definition4.7, pp121--122, and Example4.8, p122. BBD5.1.5 and5.1.8, pp125--127, fix its degree/weight convention. The new projective-perverse exclusion uses the actual extra theorem BBD5.4.10, p144, after the exact proper-to-point purity statement BBD5.1.13--14, p128. None of these framework references identifies the auxiliary state basis with a source canonical basis, and the single-center premise is not extracted from an unpublished positivity statement.

## 5. Verification record

The exact script verify_iterated_tensor_lefschetz.py independently expands HL1 and checks every coefficient in HL2, its two missing adjacent weights, its support symmetry and T(1)=320. The degree-two contradiction, kernel semiring implication and pure-projective-perverse proof were read and reconstructed by hand. They are not formal proof-assistant checks.

The original BBD text of5.4.10 was freshly read in full, including the projective morphism, relatively ample class, pure-perverse assumption and target Tate twist. The earlier complete F45 geometric-word argument was also read to keep the single-center premise consistent. Fresh independent whole-proof review is requested before integration.

