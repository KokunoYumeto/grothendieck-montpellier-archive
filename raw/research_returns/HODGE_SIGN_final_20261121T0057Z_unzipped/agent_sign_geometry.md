> Working-history note: preliminary geometric gaps below are superseded by SG-08–SG-11 in HODGE_SIGN.tex and agent_sign_strengthening.md. Use the final paper for accepted conclusions.

# Geometry and sign report — agent sign_geometry

Date: 2026-11-21 (UTC). Agent: /root/sign_geometry. Model: GPT-6 Astra Pro (inherited); effort: not exposed to this agent. This note is independent mathematical work, not a Lean verification. The supplied Alpöge RH/Dirichlet-GRH theorems are accepted as inputs; no authenticity investigation is made. Source inspection covers the supplied note p.3 footnote 3, cote 16 scans 14–18, 34–40, 49–50, SA06 intake §§1–4, and Fable explained suggestion 4. Only these source excerpts, not the missing full SA06 proofs, were used in this agent's argument. The parent agent is separately inspecting a downloaded mirror of selected imported Lean source modules; this note makes no claim to have checked those imports.

## Main conclusion

The definite *multiplicity sign* supplied by concentration of compactly supported cohomology in one degree is the sign in an alternating trace/determinant. It is not the Hodge-index sign of the intersection form. Local Picard–Lefschetz self-intersection signs are a third, related geometric datum; they too do not assert that all evanescent cohomology has a definite intersection form. Thus the suggested identification is false as a general identification of structures, although signs can numerically agree on a one-dimensional Tate primitive summand after normalization. This does not refute the note's sign-only method. Subsequent SG-08–SG-10, in agent_sign_strengthening.md, close the generic weak-Lefschetz/Gysin gate and give a complete sign-only reconstruction of finite-field absolute values.

Cote 16 scans 34,36,38,40 give restriction, Gysin, Lefschetz operators, the evanescent summand, and its projector. They do not supply a positive-definiteness theorem. Scan 49 explicitly distinguishes algebraicity of inverses from the further index relation I(X×X) needed for semisimplicity and splittings. Scan 50 announces a deduction of Weil from C and A, but the definitions of those two labels at their earlier occurrence are not among the supplied excerpts: do not silently identify these letters with the modern standardized labels B/I. Scans 35,37,39 are unrelated printed pages in the supplied transcription. Their presence is not by itself a transcription error.

## SG-01 — Cohomological parity and Hodge-index signature are different

**Statement.** The parity sign ε=(-1)^j attached to a nonzero cohomology group H^j, and the determinant exponent (-1)^{j+1}, do not determine the raw intersection sign of a primitive algebraic class in H^j, nor give positive definiteness on evanescent cohomology.

**Proof, with explicit geometric examples.** Let Q^{2r} be the smooth split quadric of dimension 2r, embedded as a smooth hyperplane section in a split Q^{2r+1}; work in characteristic different from 2 if desired to avoid any convention about orthogonal forms. Let a,b be the two classes of maximal linear r-planes, and h the hyperplane class. Their difference ζ=a−b is primitive. The explicit computation in SG-02 gives

    hζ=0,     deg(ζ²)=2(−1)^r,
    E^{2r}=Q_l(−r),     Frob_q|E^{2r}=q^r.

Here E^{2r}=ker(i_*:H^{2r}(Q^{2r})→H^{2r+2}(Q^{2r+1})(1)) is precisely the evanescent summand of the indicated hyperplane inclusion. Its point-trace contribution is +q^{rn} over F_{q^n}, and its determinant occurs to exponent −1 in the zeta function. Both signs are independent of r. Its raw intersection square is negative for r odd and positive for r even. Q², Q⁴, Q⁶ therefore exhibit all relevant distinctions: trace sign +,+,+; determinant exponent −,−,−; raw primitive square −2,+2,−2. No fixed identification of parity with the raw intersection sign survives this comparison.

One might instead normalize the primitive form as (x,y)↦(−1)^r deg(xy); it is positive on each of these Tate lines. This equality of a normalized numerical sign with +1 is not an identification of the constructions: positivity is a bilinear inequality on rational algebraic cycles, while parity is a sign on a virtual cohomology class and requires no pairing.

The whole evanescent part need not admit any definite intersection form. Embed X=P² by O(3), and let Y⊂X be a smooth plane cubic, now a hyperplane section. Since H¹(P²)=H³(P²)=0, the evanescent space is E¹=H¹(Y), of dimension two. Graded commutativity gives x∪y=−y∪x, so its nondegenerate cup-product form is alternating and every x has square zero. It cannot be a positive- or negative-definite real symmetric form. Nevertheless its cohomological trace sign is uniformly −1. The example already disproves a statement that Bertini gives a definite intersection form on the whole E. It does not contradict the Hodge standard conjecture, which concerns the rational space of primitive algebraic classes in even degree, with its specified sign normalization. ∎

**Exact source support.** Deligne, *La conjecture de Weil I* (1974), equation (1.5.4), p.276, for determinant parity; §4.1, p.287, table of local vanishing-cycle squares (2,0,−2,0 as dimension varies modulo 4); §5.9, p.293, for the alternating/symmetric intersection form on E/(E∩E⊥). These local signs are genuine intersection signs, but §5.9 asserts nondegeneracy after quotienting, not positive definiteness. Archive: cote16 scans034,036,038,040.

## SG-02 — Split-quadric calculation, including the arithmetic Tate factor

**Statement.** On the split smooth Q^{2r}, the primitive middle cohomology and rational Chow motive are Q_l(−r) and Q(−r). With ζ=a−b as above,

    deg(ζ²)=2(−1)^r.

For every finite field F_q and extension degree n,

    #Q^{2r}(F_{q^n}) = Σ_{j=0}^{2r}q^{jn}+q^{rn},
    Z(Q^{2r}/F_q,T) = [(1−q^rT) ∏_{j=0}^{2r}(1−q^jT)]^(−1).

In particular Q⁶ has primitive eigenvalue q³ and primitive L-factor (1−q³T)^(−1). Over Z, for the split smooth model Σ_{i=0}^3 x_i y_i=0 in P⁷_Z, the primitive Tate L-function is ζ(s−3). Under the stipulated Alpöge RH, its nontrivial zeros have Re(s)=7/2. That global shifted critical line and the local weight-six assertion |q³|=q³ are different claims.

**Proof.** Use coordinates Σ_{i=0}^r x_i y_i=0. The open set x_0≠0 is A^{2r}; its complement is the projective cone on Q^{2r−2}, with vertex one point. Away from that vertex it is an A¹-bundle over Q^{2r−2}. Repeatedly applying this decomposition, with Q⁰ equal to two points, gives an affine paving whose dimensions are 0,1,…,2r and one extra r. The decomposition exists over the split base; each affine cell over F_{q^n} has q^{jn} points. This proves the point count and, on exponentiating Σ_n #Q(F_{q^n})T^n/n, the zeta formula. The same cell filtration and the localization long exact sequence give only even cohomology, with one Q_l(−j) in degree 2j and an extra Q_l(−r) in middle degree. There is no extension of distinct weights within a fixed degree: the middle classes are explicitly the two rational r-planes and are Frobenius eigenvectors q^r.

The normal exact sequence of an r-plane P^r⊂Q^{2r} is

    0→N_{P^r/Q}→O(1)^{r+1}→O(2)→0.

Thus its self-intersection is the coefficient of t^r in (1+t)^{r+1}/(1+2t), namely (1+(−1)^r)/2. A special linear P^{r+1} section of the quadric is the union of an r-plane from each ruling, so h^r=a+b. Because deg(h^r a)=deg(h^r b)=1, we obtain

    a²=b²=(1+(−1)^r)/2,    ab=(1−(−1)^r)/2,
    ζ²=a²+b²−2ab=2(−1)^r.

The cell computation gives a one-dimensional H^{2r+2}; since deg(h^{r−1}ha)=deg(h^{r−1}hb)=1, we have h(a−b)=0 in cohomology. In the Chow ring the same equality follows from the single-cell generator in codimension r+1. The primitive projector is

    p_prim = (ζ×ζ)/(deg ζ²)

with the usual correspondence convention; it acts as the identity on ζ and kills the hyperplane line. The cycle ζ supplies a map from the Tate motive Q(−r), and the transposed cycle divided by deg ζ² supplies its inverse on that summand. This is an explicit rational Chow-motive isomorphism.

For the hyperplane inclusion Q^{2r}⊂Q^{2r+1}, the target of Gysin in middle degree is one-dimensional and h^r maps nontrivially. Since i_*ζ=0 (or use its pairing with the single ambient middle class), the Gysin kernel is the just-computed primitive line. Thus it is exactly the evanescent E in SG-01.

The Z-model is smooth at every prime: all homogeneous partial derivatives are its x_i,y_i coordinates, which cannot vanish simultaneously in projective space. Each finite-field fibre is split. Multiplying the local primitive Euler factors gives ∏_p(1−p^{3−s})^(−1)=ζ(s−3) in the domain of absolute convergence, and thence by meromorphic continuation. Substitution u=s−3 into the assumed RH gives Re(s)=3+1/2. ∎

This proves the requested absolute values for the ambient quadric directly; SG-08–SG-10 also give them through the now-proved general sign-only criterion. Its elementary intersection computation is also exactly the primitive Hodge inequality in this case: (−1)^rζ²=2>0.

## SG-03 — What the positive-involution route actually needs

**Statement (linear algebra form of the Weil-form argument).** Let A be a finite-dimensional real algebra with identity, † an involutive anti-automorphism, and τ:A→R a cyclic linear functional with τ(a†)=τ(a). Assume B(a,b)=τ(ab†) is positive definite. If F∈A satisfies F†F=c·1 with c>0, every eigenvalue of F in any faithful finite-dimensional representation has modulus √c.

**Short proof in this exact form.** The equation makes F invertible, so FF†=c as well. Cyclicity gives

    B(Fa,Fb)=τ(Fab†F†)=τ(F†Fab†)=c B(a,b).

Thus left multiplication by c^(−1/2)F is an isometry of a positive-definite real vector space. Its complex eigenvalues have modulus one. The minimum polynomial of left multiplication by F is the minimum polynomial of F as an element of A, since p(L_F)=L_{p(F)} and evaluation on 1 detects zero. Any faithful representation has this same minimum polynomial, hence the same set of eigenvalues. ∎

This is a short form of the classical positive-Rosati proof, not a claim of a new theorem. Milne, *Abelian Varieties*, version 1.10 (AV110.pdf), Theorem13.2 and Lemmas14.2–14.3, gives the geometric instances and the field-valued argument. In the full Grothendieck correspondence route, the positive involution must be constructed from algebraic Lefschetz operators and the index relations. Cote16:49 explicitly marks that extra input. Merely knowing an alternating trace sign supplies neither † nor B nor its positivity.

**Sharp formal warning.** Without positive definiteness, even a Frobenius similitude does not force the desired modulus. On R² take J=[[0,1],[1,0]] and F=diag(c^(1/2)a,c^(1/2)a^(−1)), a>1. Then F^t J F=cJ but its two eigenvalues have unequal absolute values. Conversely F=c^(1/2)I is pure in modulus for the indefinite form J. This is a formal countermodel to an implication between linear algebra data; it is not a claimed geometric counterexample to the Hodge standard conjecture.

## SG-04 — The hexagonal CM elliptic curve: what is unconditional

**Statement.** If E/C is the elliptic curve C/Z[ω], every rational algebraic cohomology class on E^n is a Lefschetz class, i.e. a polynomial in divisor classes. The same conclusion holds for the geometric algebraic l-adic cohomology classes on powers of each good finite-field reduction of E. Therefore the Hodge standard conjecture for these algebraic classes is already an unconditional theorem, by Milne (2002), Remark3.7 (and Remark3.8). This statement is about cohomology classes; it does not assert that every Chow class, or every cycle modulo algebraic equivalence, is a polynomial in divisors.

**Proof of the precise no-exotic-classes reduction.** For the complex curve, End^0(E)=Q(ω)=K. Under the product polarization, End^0(E^n)=M_n(K) and Rosati is conjugate transpose. The self-adjoint subspace has rational dimension n+2·binom(n,2)=n². By the Néron–Severi/Rosati identification (Milne AV110, Proposition13.1), NS(E^n)_Q has dimension n². The divisor cycle map is injective on NS_Q, and H^{1,1}(E^n) has complex dimension n²; hence divisor classes span H^{1,1} after extension to C. Write H¹(E^n,C)=U⊕W, where U is type(1,0), W type(0,1), each of dimension n. The subspace H^{r,r}=Λ^rU⊗Λ^rW is spanned by products (u_1∧w_1)…(u_r∧w_r), so it is generated by H^{1,1}. Consequently the rational divisor-generated algebra in degree2r has complexification H^{r,r}; every rational algebraic class lies in this rational algebra. This argument proves the exact E^n assertion rather than presuming it for all CM abelian varieties.

For an ordinary elliptic curve over a finite field, the two Frobenius eigenvalues α,β on H¹ satisfy αβ=q and α/β is not a root of unity (the ordinary p-adic slopes are different). On E^n, any geometric algebraic class is invariant under some power of Frobenius after its Tate twist. After extending coefficient fields, in degree2r such an invariant is a linear combination of monomials with exactly r α-vectors and r β-vectors. These are products of the paired degree-two classes. The same Rosati calculation gives NS rank n², equal to the dimension of the paired degree-two subspace, so its injective cycle map fills that subspace. Thus all geometric algebraic classes are in the Q_l-span of divisor products. The invariance after a Frobenius power follows because an algebraic cycle is defined over a finite extension, including any of its finitely many constituent subvarieties.

For a supersingular elliptic reduction, End^0(E) is a quaternion algebra with canonical conjugation as Rosati. Self-adjoint matrices in M_n(End^0(E)) have dimension n+4·binom(n,2)=n(2n−1)=binom(2n,2). The injective divisor class map therefore spans the whole H². The even exterior algebra on H¹ is generated by H², so every even cohomology class is in the Q_l-span of divisor products. These standard descriptions of the ordinary/supersingular elliptic endomorphism algebras are used as background; they are not derived from Alpöge's note.

To obtain rational rather than merely Q_l coefficients in both finite-field cases, use the perfect restriction of Poincare duality to the paired invariant subspaces (ordinary case) or all even cohomology (supersingular case). Choose divisor products b_i and complementary divisor products d_j that are Q_l-bases of these dual subspaces. Their intersection matrix M=(deg(b_i d_j)) is rational and invertible. If z is an algebraic cycle and cl(z)=Σ c_i cl(b_i), its pairings with the d_j give a rational vector. Thus the invertible rational system M^t c=(deg(z d_j)) forces every c_i to be rational. This proves the asserted rational divisor-generation and also its independence from scalar extensions.

Milne's Remark3.7 states positive definiteness of (x,y)↦(−1)^r deg(L^{n−2r}xy) on primitive Lefschetz classes over an arbitrary algebraically closed field. The preceding argument makes its class space all algebraic cohomology classes for E^n and its finite-field reductions, proving the final claim. ∎

**Limits.** Do not replace “CM elliptic curve E” by “arbitrary CM abelian variety,” or by an unspecified higher-genus curve with CM Jacobian: exotic classes require separate analysis. Milne (2002), Theorem3.3 asserts the standard conjecture for all abelian varieties conditional on Hodge for all complex CM abelian varieties. No specific Masullo theorem is supplied here, and no new consequence conditional on it is claimed by this note. The unconditional sign-only absolute-value theorem does not itself prove this index positivity.

## SG-05 — Arbitrary abelian varieties: the classical purity proof survives

For every A/F_q, Rosati positivity on End^0(A) and π†π=q imply that eigenvalues on H¹ have modulus √q. The exterior-algebra isomorphism H^i(A)=Λ^iH¹(A) then gives modulus q^{i/2}. Exact locators: Milne AV110, Theorem13.2, Lemma14.2, Lemma14.3, Theorem14.1, and Theorem11.1(b). This is the known Weil proof, used as background, not re-proved here.

Thus all abelian varieties, and their powers, have the required finite-field absolute values without assuming the full Hodge standard conjecture in every codimension. That conclusion cannot be advertised as a consequence of identifying the step-5 parity sign with an index form. It uses a known positive involution in degree one and exterior powers. For divisor-generated classes on any abelian variety, Milne Remark3.7 gives index positivity; beyond that class subalgebra, neither parity nor purity proves the full index statement from the supplied data.

## SG-06 — SA06 C.1a–C.1q: finite-field weights and the kernel of the cycle map

**Statement.** A smooth projective complex variety X admits a smooth projective spread f:𝓧→S after shrinking an integral finite-type Z-scheme S over which it is defined. For every closed finite-field point s∈S and each i, the eigenvalues of geometric Frobenius on H^i(𝓧_sbar,Q_l), l≠char κ(s), have absolute value #κ(s)^{i/2}. This is Deligne Weil I Theorem1.6, applied fibre by fibre. It is a known theorem; SG-08–SG-10 now also give an independently checked reconstruction by the sign-only method, with the generic Gysin hypotheses proved.

A cycle z with zero cohomology class has zero intersection number with every complementary algebraic cycle, by compatibility of cycle classes with products and trace. Thus the intersection form modulo algebraic equivalence has all such Griffiths classes in its radical wherever they enter its domain. Every cohomological Frobenius trace, characteristic polynomial, and associated local L-factor is unchanged on replacing a cycle by another with the same cohomology class. This elementary factorization proves that the spectral information by itself does not recover the algebraic-equivalence quotient or kill its kernel. It is not an assertion that finite-field Griffiths groups provide a known counterexample to their conjectured rational vanishing.

The spread exists by descending finitely many equations and the projective embedding to a finitely generated integral subring of C, then shrinking to the open smooth locus. There is no canonical single finite-field Frobenius on the original complex variety. A very general complex example can require a transcendental field of definition; a chosen arithmetic spread still has finite-field closed fibres. Purity of all of those fibres is a meaningful statement, whereas writing a canonical number-field L-function for the original complex example without further descent data is not.

The following table lists *every* C.1 row named in the intake. Its descriptions are limited by the attached table: the original full proofs behind C.1f–q were not supplied, and the intake itself says it read only their statements. The table makes no unverified upgrade of those prior-run conclusions.

| Row | Supplied type/example | Conclusion for the present question |
|---|---|---|
| C.1a | Very general quintic threefold V; infinite rational Griffiths summand G in A²_alg | Smooth finite-field fibres have weight-i H^i. The G summand is invisible to cohomological traces. The genuinely varying H³ is not the Tate line Q(−3). No global H³-GRH follows from Dirichlet GRH. |
| C.1b | Failure of the letter's A,A′,A″ modulo algebraic equivalence on the quintic example | Fibre purity does not repair a cycle-class-kernel obstruction in the algebraic-equivalence formulation. |
| C.1c | L^{n−2}:NS_Q→A^{n−1}_alg and V×P^{n−3} | Product-fibre weights follow from Künneth: H^i(V_s×P^m)=⊕_j H^{i−2j}(V_s)(−j). Its Griffiths cokernel is still invisible. |
| C.1d | Endpoints, dimensions≤2, and surface Hodge index | For finite-field curves the known Hodge-index/Rosati proof gives weight1; all smooth projective fibres also satisfy Weil I. This does not identify parity with a form. |
| C.1e | V×P¹, letter-B vacuous in the stated degree, nonzero numerically trivial G | Product purity holds but does not imply algebraic=numerical. Keep the prior row's vacuity qualification; it is not a direct counterexample to the primitive Hodge standard conjecture. |
| C.1f | Universal ranges of letter-A over C | Finite-field purity is uniform in degree and does not enlarge the valid ranges of an assertion modulo algebraic equivalence. |
| C.1g | Universal quintic over Q(t_1,…,t_113), homologically trivial cycle | Use a model over a finite-type Z-base and then its smooth finite-field fibres. There is no single arithmetic Frobenius attached to the generic transcendental base. The cycle is invisible to traces. |
| C.1h | Geometric generic hyperplane, Gysin image modulo algebraic equivalence | Purity applies to smooth closed fibres; the Gysin-image assertion is separate cycle-theoretic information. |
| C.1i | Universal A′/A″ range and explicit split-quadric examples | Split quadrics have the explicit Tate eigenvalues of SG-02. Their weights do not validate an incorrectly quantified Gysin or restriction statement. |
| C.1j | Complex middle letter-B versus Griffiths-kernel injectivity | Coherent Hodge positivity on cohomology and a kernel condition in the algebraic-equivalence group are distinct; purity tests only the former realization. |
| C.1k | Universal cycle-class injectivity, finite rank/generation and equivalence relations | Frobenius purity does not supply injectivity of the cycle class map or finiteness of its kernel. |
| C.1l | Radical correspondences from Griffiths classes | A correspondence of zero cohomology class acts as zero on cohomology; all its spectral data vanish, without proving it zero modulo algebraic equivalence. |
| C.1m | Semisimplicity modulo algebraic equivalence in universal dimension ranges | Finite-field weight purity alone neither proves Frobenius semisimplicity in general nor semisimplicity of this cycle-equivalence correspondence algebra. Cote16:49 explicitly calls for I(X×X). |
| C.1n | Endpoint image criterion versus standard D and a kernel condition | Weight purity does not supply standard D or the extra cycle-kernel vanishing. |
| C.1o | Projective-space stabilization and the middle-positivity radical | Künneth shifts all weights correctly; projective stabilization does not make a zero cycle class visible to Frobenius. |
| C.1p | Abelian projective stabilizations and Beauville/Griffiths pieces | The abelian-factor weights are classical by SG-05; P^m gives Tate shifts. These do not determine the Beauville grading on a Griffiths kernel. |
| C.1q | Blow-up exceptional normal-bundle polynomial and radical | Every smooth projective finite-field blow-up fibre is pure. A blow-up decomposition of its cohomology involves Tate-shifted cohomology of the center, while any cycle-kernel/radical assertion needs its own Chow-level argument. The truncated intake row is insufficient to reconstruct more. |

No row becomes a theorem about number-field L-functions of a general quintic from the stipulated RH/Dirichlet-GRH. In particular, H³(V) is not shown to be an abelian Artin–Tate motive. The separate ambient quadric factor ζ(s−3) is the case for which the stipulated RH does transfer by a direct change of variable.

## SG-07 — The ambient primitive Tate line does not survive into the SA06 E.3u restriction

Let j:Y→Q⁶ be a smooth hypersurface of positive degree d (d=14 in the supplied E.3u example). Then j^*ζ=0 in H⁶(Y,Q_l), where ζ is the primitive middle class of SG-02. Indeed j_*j^*ζ=d hζ=0 by the projection formula. Weak Lefschetz identifies H⁴(Q⁶)→H⁴(Y), hence by Poincaré duality j_*:H⁶(Y)→H⁸(Q⁶)(1) is an isomorphism. Therefore j^*ζ=0. This is precisely why the difference of the two plane traces can define a homologically trivial cycle on Y. Its possible morphic/Lawson nontriviality is additional structure not carried by the ambient Q(−3) cohomological summand. In particular, the purity of that one-dimensional Tate summand cannot by itself give the weights of the variable H⁵(Y), or information about the Griffiths/Lawson kernel of Y×E. ∎

This observation uses only the geometric portion of the supplied E.3u description. It does not independently verify the stated degree-14 Nagel bound or Walker's nonvanishing theorem.

## Proposed transcription notes (original images not supplied)

1. Cote16 scan034, first kernel diagram: with the written arrow L_Y^{n−i}:H^i(Y)→…, the target degree must be 2n−i, not 2(n−1)±i. The Gysin arrow must consequently have source subscript 2n−i and raises degree to 2n−i+2 as at the top. Certainty: high conditional on the correctly read exponents; compare original scan before changing the record.
2. Cote16 scan036, double sum immediately after “s'identifie donc à L_X”: L_X^jP^j(X) should be L_X^jP^i(X), matching (α), because i is the primitive degree and j the Lefschetz exponent. Certainty: high, formula context.
3. Cote16 scan038, first two double sums: same P^j→P^i correction. Certainty: high, formula context.
4. Cote16 scan038, expression (id_Y−Σp_X^j)φ^*Λ_X: the projectors must be p_Y^j for this composition to be typed as written. Certainty: high, domain/codomain.

Do not label the unrelated printed versos 35/37/39 as misread mathematical text without seeing scans. Do not broadly “correct” the unusual P^i or Λ normalization elsewhere: the excerpt uses extended endpoint projectors and a normalized lowering operator whose conventions require earlier pages.

## Primary bibliography and verified web handles

- Deligne, *La conjecture de Weil I*, Publ. Math. IHÉS43 (1974), 273–307: (1.5.4), Theorem1.6, §§4.1,5.9. URL https://www.numdam.org/article/PMIHES_1974__43__273_0.pdf. Opened refs turn992409605view1 and turn951341857view0; precise purity location turn992409605view4. Root must open this URL before using those refs in its own final answer.
- Milne, *Polarizations and Grothendieck's Standard Conjectures*, Ann. Math.155 (2002), 599–610, published-version preprint https://jmilne.org/math/articles/2002aP.pdf: Proposition3.2, Theorem3.3, Remarks3.7–3.8. Opened turn992409605view0; retrieved exact relevant remarks turn992409605view3. Note the earlier submitted version 2002aS has different numbering; use 2002aP consistently.
- Milne, *Lefschetz classes on abelian varieties*, Duke Math. J.96 (1999), 639–675, Theorem3.2, §5; official summary and errata https://www.jmilne.org/math/articles/1999a.html, opened turn645223280view0. The erratum on §5.9 explicitly warns that Λ is not globally inverse to L.
- Milne, *Abelian Varieties*, version1.10, https://www.jmilne.org/math/CourseNotes/AV110.pdf: Theorem11.1(b), Proposition13.1, Theorem13.2, Theorem14.1, Lemmas14.2–14.3. Verified refs turn827761366view2, turn909555575view2, turn213088875view0.
- Grothendieck, *Standard conjectures on algebraic cycles*, Bombay1968 proceedings (1969), pp.193–199. Sections3 (Lefschetz) and4 (Hodge type) identified by Milne; the accessible scan URL https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf was opened but has no extractable text in the web tool. Do not pretend its full proof was checked from that opening.

## Checks performed on the whole note

Initial full proof check: SG-01 through SG-04, the elementary kernel factorization in SG-06, and SG-07 have been read from beginning to end by this agent after drafting. The affine-paving recurrence, normal-bundle coefficient, distinction between raw and normalized signs, Rosati matrix dimensions, ordinary paired monomial condition, and restriction/Gysin degree shifts were rechecked. Background theorems are separately identified; no claimed Lean/computer certificate. Finite-field statement SG-04 uses the standard classification of elliptic endomorphism algebras and ordinary slopes as background (not a fresh source-checked proof of those classifications). Every SG claim has corresponding events in agent_sign_events.tsv. A subsequent whole-proof read caught and corrected (a) the Gysin Tate twist in SG-07 and (b) the need for a rational-intersection-matrix descent argument in the finite-field part of SG-04; both corrections are included above. The parent subsequently read the complete SG-01–SG-07 LaTeX fragment and independently checked these proofs; its reported PASS and minor r≥1 scope correction are reflected in section_geometry.tex. The original classification statements were subsequently verified at exact source locators in Sutherland, Lecture13, while their full proofs remain cited background.


Final integration note (2026-11-21 UTC): section_geometry.tex is the final version of SG-01–SG-07. It specifies r≥1 in SG-02 and 0≤r≤n/2 for the primitive Milne form, gives the direct affine-vanishing proof of SG-07, and notes that the same SG-04 argument covers every complex CM elliptic power and every finite-field elliptic power. The final main proof including SG-11 compact-support upper bounds was independently checked in full. Later source inspections by this agent are recorded separately in agent_sign_arithmetic_check.md and do not expand the original source-inspection claim of this note.
