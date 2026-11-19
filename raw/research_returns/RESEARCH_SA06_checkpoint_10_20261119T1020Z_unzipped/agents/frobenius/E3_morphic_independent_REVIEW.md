# Independent audit: the full morphic Abel–Jacobi obstruction

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort, /root/frobenius.

This is an independent source and proof review of the proposed cycles-agent counterexample. The complete typed E.3t and E.3u in research/agents/cycles/morphic_counterexample.tex have now been independently read and pass. This includes the exact Lawson criterion, the degree-fourteen sixfold construction, the integral singular-class vanishing, the fixed elliptic family, and the geometric-generic point witness. The smooth-dominant spread formulation correctly allows auxiliary transcendental coefficients.

## 1. Exact primary sources

**[OPENED]** Walker, M. E. (2007). The morphic Abel–Jacobi map. *Compositio Mathematica, 143*, 909–944. https://doi.org/10.1112/S0010437X07002278

Full published PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4A44146CE680F4F3C857048FDEDD9F48/S0010437X07002278a.pdf/the-morphic-abel-jacobi-map.pdf

Exact locators independently read: Example5.5 p.928; Theorem5.7(1)–(4) p.930 and proof p.931; Corollary5.9 and its preceding factorization p.932; Theorem6.1 and Theorem6.2 pp.933–934, including the full cap-product proof; Corollary6.3 p.934; Definition3.1 pp.915–916 and Proposition3.3 p.916.

**[OPENED]** Friedlander, E. M. (2000). Relative Chow correspondences and the Griffiths group. *Annales de l'Institut Fourier, 50*(4), 1073–1098. https://doi.org/10.5802/aif.1785

Published primary PDF: https://www.numdam.org/item/10.5802/aif.1785.pdf

Author primary PDF, also opened: https://dornsife.usc.edu/ericmfriedlander/wp-content/uploads/sites/233/2023/06/17.pdf

The needed published result is **Theorem3.4, p.1082**, with Definition3.1 and Theorem3.2 pp.1081–1082 and proof pp.1095–1097. Walker's citation to this paper as “4.5” does not match the published numbering: Proposition4.5 pp.1089–1090 concerns relative characteristic classes. The author copy likewise numbers the result Theorem3.4 (p.8; proof pp.18–20). We must cite the verified locator rather than reproduce the mismatch.

The effective Nagel sources and their exact numerical hypotheses were independently opened in the earlier Nori_independent_REVIEW.md. They are reused here only for the same universal relative-cohomology conclusion.

## 2. The full morphic map kills the generated relation

Example5.5 identifies the zero-cycle morphic Abel–Jacobi map on every smooth projective parameter with its Albanese map. Theorem5.7(4) gives naturality for arbitrary Chow correspondences of nonnegative dimension shift. A generator defining \(N^i(X)\) starts with an Albanese-zero zero-cycle on a smooth projective parameter and has target dimension \(\dim X-i\ge0\). Its full morphic image is therefore zero.

The theorem's printed notation reuses its index inconsistently in the displayed diagram, but both its statement and proof give the required correspondence shift. The specific zero-cycle-to-positive-dimensional-cycle application has no negative shift.

## 3. A single fixed cycle gives a nonzero elliptic family

Let \(Y\) be smooth projective of dimension \(2r+1\), and let \(\gamma\) be an \(r\)-cycle with zero rational singular class and
\[
s\gamma\ne0\quad\text{in }L_{r-1}H_{2r}(Y)_{\mathbb Q}.
\]
For an elliptic curve \(E\), put \(X=Y\times E\). The map
\[
\lambda_\gamma:H_1(E,\mathbb Q)\longrightarrow
L_rH_{2r+1}(X,\mathbb Q),\qquad v\longmapsto\gamma\times v
\]
is injective. Indeed, for nonzero \(v\) choose \(w\) with nonzero intersection pairing. Capping with the pullback of \(w\) and pushing to \(Y\), exactly as in Walker's proof of Theorem6.2, gives
\[
\langle v,w\rangle\,s\gamma\ne0.
\]
The map is a morphism of inductive mixed Hodge structures; its source is pure of weight minus one. Strictness therefore gives an injection of its one-dimensional complex Hodge quotient into the target Hodge quotient.

By Definition3.1 the integral Lawson group is countable. Modulo its image, the induced homomorphism
\[
E(\mathbb C)\longrightarrow J_r^{\mathrm{mor}}(X)
\]
has countable kernel and countable preimage of the torsion subgroup: upstairs a nonzero complex linear injection can meet each integral period, or each rational multiple of such a period, at at most one point. Consequently uncountably many points give nontorsion images. This argument does not require the full morphic Jacobian to be a finite-dimensional complex torus.

Theorem5.7(4) identifies this map on points with
\[
e\longmapsto\Phi_r^{\mathrm{mor}}\bigl(\gamma\times([e]-[0])\bigr).
\]
The normalized correspondence is \(\gamma\times(\Delta_E-E\times\{0\})\), with factors ordered as parameter \(E\), then \(Y\), then target \(E\). Its total rational Betti class is zero, so its cylinder action vanishes. Yet its map to \(P^i(X)\) has nontorsion values, since the full morphic map kills \(N\).

The finite-dimensional Walker family map also vanishes: it is a homomorphism of abelian varieties whose rational \(H_1\)-map is the zero cylinder. Thus no multiplication to kill a finite Walker image is necessary for this explicit family.

## 4. Effective degree-fourteen choice

Use \(r=2\), \(Y\subset Q^6\) the degree-fourteen geometric generic hypersurface, and
\[
\gamma=(\Pi_+-\Pi_-)|_Y.
\]
The ambient primitive class is nonzero; its square has degree minus two. Its restriction has zero rational singular class by the already checked weak-Lefschetz calculation.

Friedlander's Theorem3.4 proof uses connectivity only for the characteristic-class degree
\[
u=2n-2r+2j
\]
and the final degree \(2n-2r\), and again in degree \(u\) after passing to the resolved relation space. With \(n=5,r=2,j=1\), these degrees are eight and six. Relative vanishing through degree nine is sufficient for all the required isomorphisms. The Nagel bound supplies vanishing through degree ten.

Numerically, Nagel's connectivity parameter is five, \(\mu=5\), the bundle-rank-minus-one is zero, and \(m_{Q^6}=1\). His conditions reduce to \(14\ge6\) and \(14\ge12\). The omitted parameter-bound hypothesis is also satisfied with equality.

A failure of \(s\gamma\ne0\) admits the finite algebraic witness supplied by Friedlander's Theorem3.2: a homologically trivial one-cycle on a possibly singular projective threefold and a Chow correspondence. Spread this witness over a smooth dominant parameter base above the hypersurface parameter space, retaining the homological vanishing after stratifying and shrinking. Resolve the witness and the relation space and shrink so their structural maps are smooth. Friedlander's proof then applies with the explicit Nagel connectivity and forces the ambient primitive class to vanish, a contradiction.

One must not automatically describe a witness initially given after an embedding into \(\mathbb C\) as defined over a finite extension of the geometric-generic field: its coefficients can have additional transcendence. The smooth-dominant-base formulation avoids this error; Nagel permits every smooth base. A subsequent multisection is another possible way to reduce to an étale base. The relation is finite algebraic data and its zero homology class is locally constant on a topologically trivial stratum, which is the reason the spreading step is legitimate.

## 5. Scope of the conclusion

For this construction \(X\) has dimension six, the fibres are two-cycles, and the codimension is four. The contradiction is to the universal complex family converse, integrally and rationally. The result does not assert a codimension-two counterexample or settle all lower-dimensional cases. It depends on the published Lawson-homology results with the explicit connectivity substitution, not on a conjectural identification of the full morphic object with the finite-dimensional Walker Jacobian.

## Final typed audit

The typed proof has the correct dimensions: Y has dimension five, X has dimension six, gamma has dimension two, and Z has codimension four on E times X. The homological cylinder H1(E) to H5(X) and its Poincare-dual map H1(E,Q(1)) to H7(X,Q(4)) agree with these conventions. Integral weak Lefschetz makes H4(Y,Z) isomorphic to H4(Q,Z)=Z, so equal degrees give integral, not merely rational, vanishing of gamma.

The generic-point argument for e is valid: a finite expression in N, including its Chow rational-equivalence witnesses and the relative Albanese-zero conditions, spreads on a smooth dominant base over an open of E. The image contains a nonempty complex open. The entire open would then have morphic image killed by one fixed nonzero integer, contrary to the countable torsion-preimage statement. Additional transcendental coefficients do not invalidate the argument because the base is permitted to have positive relative dimension.

For the Lawson witness, proper topological stratification (equivalently constructibility and base change for the relative homology complex) makes the zero class persist after shrinking. The model is chosen from the field generated by all finite witness coefficients, so its defining complex point is generic over the original coefficient field and is retained on these dense opens. The two resolved bases are smooth over the hypersurface parameter after generic smoothness. Thus the all-embedding formulation does not assume that an unspecified analytic exceptional locus is defined over the original countable field.

No finite-dimensionality of the full morphic target is used. The conclusion refutes the universal complex converse integrally and rationally in the stated codimension-four example.
