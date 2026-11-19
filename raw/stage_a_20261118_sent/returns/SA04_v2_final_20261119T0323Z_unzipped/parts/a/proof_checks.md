# Mathematical checks for cote 93, scans 37–73 and 83

These are the present run's arguments. They are distinct from the manuscript, from earlier-run proposals, and from results used from references. The exact calculations are in `programs/a_computations.py`, with saved output `outputs/a_computations.txt`. A finite matrix or cochain calculation is described as such. It is not a certificate of the analytic or topological theorem that interprets it.

## 1. Crystalline conventions and global denominators

For maps (F:M^{(p)}\to M) and (V:M\to M^{(p)}), the composite (FV) has domain (M), whereas (VF) has domain (M^{(p)}). The two identity subscripts in Codex scan38, line206, are reversed relative to these displayed arrows. Contravariance also requires `BT(S)^op` in the functor on line210. This is a domain check, not a proposed decision about the ink.

On a perfect characteristic-(p) ring (A), let (M) be a finite projective (W(A))-module with semilinear (F,V) and (FV=VF=p). The Witt ring and (M) are (p)-torsion free. Thus (F) and (V) are injective. If (F(x)\in pM), write (F(x)=py=FV(y)). Injectivity implies (x=V(y)). After reduction modulo (p), this gives \(\ker\bar F=\operatorname{im}\bar V\); interchanging (F,V) gives the other equality. Consequently the source's kernel/image formula cannot concern (M) before reduction. The further assertion that the resulting Hodge quotient is projective is not proved by cancellation. Lau, Definition6.1 and Lemma6.2, is the separately checked input. His Theorem6.4 supplies classification over perfect rings, not a classification of arbitrary singular bases by ordinary crystals.

The warning that global isogeny localization is not a stack has a direct example. On (S=\coprod_{n\ge0}\operatorname{Spec}\mathbb F_p), take the constant height-one étale (p)-divisible group. Its global endomorphisms form \(\prod_n\mathbb Z_p\). The componentwise quasi-endomorphisms (p^{-n}) agree on every overlap of the disjoint open cover. They do not lie in \((\prod_n\mathbb Z_p)[1/p]\), whose elements have a single denominator bound. Thus descent already fails for morphisms. This checks the earlier run's example; no descent theorem is inferred from it.

Grothendieck's published ICM1970 §5, p434, explicitly assumes the infinitesimal thickening ideal is annihilated by one power of (p) in the isogeny invariance assertion. That is stronger than merely having (p) locally nilpotent on a non-quasi-compact base. The manuscript cancels quasi-compactness and prints the suspicious phrase “une puissance de J”. The published wording is evidence for checking that letter, not authority to change the transcription.

The isocrystal example distinguishing ranks from admissibility is (D=K_0e_0\oplus K_0e_1), \(\varphi e_0=e_0,\varphi e_1=pe_1\), with \(\operatorname{Fil}^1D_K=Ke_0\), \(\operatorname{Fil}^0D_K=D_K\), \(\operatorname{Fil}^2=0\). The total Hodge and Newton numbers are both1, and the Hodge ranks are the expected two-step ranks. On the stable line (K_0e_0), however, (t_H=1>0=t_N). This violates the necessary inequality for weak admissibility. The example rules out a rank-only criterion, not the possibility of attaching some smaller Galois representation to a nonadmissible object. Colmez–Fontaine §4.1 and Theorem4.3 are the external necessity/equivalence input.

The two universal-extension conventions must also be kept apart. The displayed \(D^*(A)=\operatorname{Lie}E(A^*)\) implies \(D^*(A^*)=\operatorname{Lie}E(A)\). Consequently the uncertain extra linear-dual exponent in the second display on scan47 cannot be appended without changing this convention. Perfection of a pairing with the dual abelian scheme does not provide an unpolarized canonical self-duality. Frobenius-compatible Cartier duality also involves the appropriate Tate twist; the manuscript's pairing is written on an underlying nilpotent crystalline site without that extra datum.

## 2. Cancelled anonymous Banach exercises

### Geometric sum and factorization induction

With (u_k=e), the source's finite expression is
\[
\sum_{k=1}^n\gamma(1-\gamma)^k+(1-\gamma)^n
=1-\gamma+\gamma(1-\gamma)^n.
\]
Its limit for (0<\gamma<1) is (1-\gamma), whereas the displayed infinite expression with exponent (k-1) sums to1. Replacing the finite exponent by (k-1) repairs this arithmetic. It does not by itself verify the whole printed Cohen-factorization induction. The endpoint (z=xy) follows from continuity of multiplication once the corrected sequence has (x_n\to x), (x_n^{-1}z\to y). Existence of a sequence with those properties is an external factorization theorem, not certified by the geometric-sum check.

The printed perturbation target is independently false. In (B=\mathbb C), set (u=1,w=2,C=2,\varepsilon=1/2,\gamma=0). Every hypothesis holds for every positive \(\eta\): \(|u|<C\), \(uw-w=0\), and (0\le\gamma\le1/(4C)\). Yet (y=1) and \(|yw-u|=1\). The corrected target \(|yw-w|<\varepsilon\) follows from
\[
a=(1-\gamma)e+\gamma u,
\quad a-e=\gamma(u-e),
\quad a^{-1}w-w=\gamma a^{-1}(w-uw).
\]
For a normalized unital norm, \(\|a-e\|\le\gamma(C+1)<1/2\), so \(\|a^{-1}\|<2\). Therefore \(\|a^{-1}w-w\|\le2\gamma\eta\). This is a sufficient uniform estimate and matches the role of the step in factorization.

### Weighted Liouville computation

Write \(f(z)=\sum_{\nu\ge0}a_\nu z^\nu\) and \(p(\theta)=\sum_{\mu=k}^mc_\mu e^{i\mu\theta}\), (c_k\ne0). Termwise integration on each circle gives, for integer (q\ge0),
\[
r^{-q}\int_0^{2\pi}p(\theta)f(re^{i\theta})e^{-i(k+q)\theta}\,d\theta
=2\pi\sum_{\substack{k\le\mu\le m\\k+q-\mu\ge0}}c_\mu a_{k+q-\mu}r^{k-\mu}.
\]
The finite right-hand sum tends to (2\pi c_ka_q). The uniform source bound gives norm at most (2\pi Mr^{\alpha-q}). Hence (a_q=0) for (q>\alpha). If (alpha) is an integer and the bound is uniformly little-o of (r^\alpha), the same argument also kills (a_\alpha). The missing (2\pi) has no effect on the vanishing conclusion. The program checks the Fourier normalization; this written finite-sum identity proves the general extraction formula.

The source of the little-o assertion does not specify its uniformity in \(\theta\). A dominated-integral argument is valid under the preceding uniform big-O bound plus pointwise little-o, and the uniform little-o formulation is sufficient without this extra clarification. No proof of an unqualified raywise condition alone is claimed.

For quasinilpotent (x) in a unital Banach algebra, ((e-\lambda x)^{-1}) is entire with Taylor coefficients (x^j). Applying the preceding result with the trigonometric polynomial (cos^n\theta) yields (x^n=0), under the specified uniformity/dominating hypothesis. The ambiguous printed (z|x) matters: the argument requires the same element (x).

### Boundary growth and the Cayley substitution

The big-O reading of the pole exercise is false. Take (f(z)=(z-1)^{-2}). For (|z|<1), its coefficient (a_n=n+1); for (|z|>1), its coefficient (b_n=n-1) for (n\ge2), with (b_0=b_1=0). Both are (O(n)), but the pole degree is2, violating the strict bound (<\alpha+1=2). All hypotheses other than the disputed (o|O) reading hold: it is an entire polynomial in (1/(z-1)), and the two expansions have the prescribed domains.

Under the little-o reading, split the coefficient sum at an index where \(\|a_n\|\le\delta n^\alpha\). The finite beginning multiplied by ((1-r)^{\alpha+1}) tends to0. The tail is bounded by a constant depending on (alpha) times (delta(1-r)^{-\alpha-1}); choose (delta) smaller than the requested epsilon divided by that constant. The outside estimate is the same argument in (r^{-1}). This proves the epsilon boundary estimate, including the otherwise suppressed constant rescaling.

For (z=(w-1/2)/(w+1/2)), put (A=|w+1/2|,B=|w-1/2|,w=Re^{i\theta}). Then (A^2-B^2=2R\cos\theta). If (r=|z|<1),
\[(1-r)^{-1}=A(A+B)/(2R\cos\theta)\le(9/4)R/\cos\theta\]
because (R\ge1) gives (A,B\le3R/2). If (r>1), the analogous denominator is (-2R\cos\theta), so the printed positive-(cos\theta) denominator has the wrong sign. At (w=-2) it gives a positive left side (5/2) bounded by the negative number (-9/2). A minus sign or absolute value repairs the estimate. The exercise's last sentence is truncated; no completed final conclusion is supplied as a manuscript statement.

### Pseudo-resolvents

From (R_\lambda-R_\mu=-(\lambda-\mu)R_\lambda R_\mu), interchanging the arguments shows commutativity. With (\delta=\lambda-\lambda_0),
\[R_\lambda(1+\delta R_{\lambda_0})=R_{\lambda_0}.\]
The Neumann expansion is therefore justified by \(|\delta|\|R_{\lambda_0}\|<1\). The source instead uses \(\|R_\lambda\|\). For (R_\lambda=1/\lambda), (\lambda_0=1,\lambda=3), its literal bound is (2/3<1), but its proposed series has terms ((-2)^n). All assumptions hold on \(\Delta=\mathbb C^*\). This refutes the printed sufficient condition.

The correct local expression gives analyticity and, by induction from (R'=-R^2), \(R^{(n)}=(-1)^nn!R^{n+1}\). The program checks the first seven derivative identities in the scalar universal expression; the induction establishes all orders in the Banach subalgebra generated by (R_{\lambda_0}).

For a pseudo-resolvent holomorphic at infinity, write (R(1/s)=\sum_{i\ge0}c_is^i). The identity becomes
\[st(R(1/s)-R(1/t))=(s-t)R(1/s)R(1/t).\]
Comparing boundary coefficients yields (c_0c_i=c_ic_0=0) for every (i), in particular (c_0^2=0). Comparing coefficients with one exponent1 gives (c_1^2=c_1) and (c_1c_i=c_ic_1=c_i) for (i\ge1). Interior coefficients give (c_{i+1}c_j=c_ic_{j+1}); setting (j=1) implies (c_{i+1}=c_ic_2). Hence, with (z=c_0,j=c_1,x=c_2),
\[R(\lambda)=z+j/\lambda+x/\lambda^2+x^2/\lambda^3+\cdots=z+j(\lambda e-x)^{-1}.\]
This is the general coefficient proof. The program also tests a nonzero square-zero (2\times2) block beside a nonzero scalar resolvent block; that test is supplementary, not the proof.

If one (R_{\lambda_0}) is invertible, the identity and commutativity show that every (R_\lambda) is inverse to \(\lambda e-x\), where (x=\lambda_0e-R_{\lambda_0}^{-1}\). Both product orders are checked by multiplying the same identity on the appropriate side. Conversely a genuine resolvent is invertible at every point of its domain. The local geometric series for any element (x) is a pseudo-resolvent because the rational identity holds in the commutative algebra generated by (x), on the norm-convergent disk. These exact statements match Kurbatov–Kurbatova–Oreshina, Theorem16, Corollary17, and Propositions18,23, rather than merely sharing terminology.

## 3. Euler characteristic: what the finite hypotheses buy

For a bounded finite-dimensional cochain complex, write (Z^i=\ker d_i), (B^i=\operatorname{im}d_{i-1}). The two short exact sequences give \(\dim C^i=\dim B^i+\dim H^i+\dim B^{i+1}\). Alternating summation cancels boundaries. This proves Euler additivity for finite long exact sequences, including closed/open compact-support additivity and excisive Mayer–Vietoris. A closed cover alone is not an excision hypothesis for singular cohomology. Hatcher, Theorem2.20 and the Mayer–Vietoris construction, provide the open/interior-cover form. For finite polyhedral subcomplex covers the condition is satisfied. The source's sheaf-to-singular correction cannot be ignored when interpreting this distinction.

Homotopy domination splits ordinary cohomology as a direct summand, proving the finite-total-dimension implication. Homotopy equivalence also identifies its Euler number. Compact-support cohomology is invariant under proper homotopy equivalences, not arbitrary ones: \(\mathbb R\simeq\{*\}\), but \(\chi_c(\mathbb R)=-1\ne1\). The literal missing-cover version of Mayer–Vietoris on scan66 fails for (X=S^1) with both named subspaces the same point: (0\ne1+1-1).

Normalization gives \(\chi(\varnothing)=0\), \(\chi(\{*\})=1\), and finite disjoint-union additivity. Two hemispheres and equator give (s_0=2,s_n=2-s_{n-1}), hence \(\chi(S^n)=1+(-1)^n\). Compactification or one compact-support cell gives \(\chi_c(\mathbb R^n)=(-1)^n\), while ordinary contractibility gives \(\chi(\mathbb R^n)=1\). A finite cellular filtration therefore gives the alternating cell count for compact supports. A rank-(r) local system contributes an (r)-dimensional vector space on every cell, so its compact-support Euler number is (r\chi_c(X)\). Ordinary cohomology gives the analogous identity for spaces of finite CW homotopy type. The proof uses finite cell groups, not just finite ordinary cohomology with constant coefficients. It also proves field independence in this finite range. No field independence is asserted for membership in every broader finiteness class.

For a locally trivial fibration over a finite CW-type base, with finite total cohomology of its fibre, the Serre/Leray spectral sequence has finite-dimensional, bounded (E_2^{ij}=H^i(Y;\mathcal H^j(F;k))). The local-system cell formula gives \(\chi(X)=\chi(Y)\chi(F)\). The compact-support variant requires the corresponding compact-support direct-image formalism and finite relative-cell hypotheses. The source's provisional ordinary formula, assuming only finite constant-coefficient total cohomology, is too broad.

Here is the full counterexample to that broad version, adapted from the earlier notes. Let (Y) be the locally finite mapping telescope of the standard inclusions \(\mathbb{RP}^2\subset\mathbb{RP}^3\subset\cdots\). Each finite stage is a compact finite polyhedron, so the telescope is a locally compact CW complex. It is homotopy equivalent to \(\mathbb{RP}^{\infty}=K(C_2,1)\). Its double cover (X) is the corresponding telescope of spheres (S^2\subset S^3\subset\cdots\), which is a contractible CW space. The covering is locally trivial with fibre two points. Over \(\mathbb Q\), finite-group averaging gives (H^*(Y;\mathbb Q)=\mathbb Q) in degree0 only; the same is true for (X). Thus all three ordinary cohomology finiteness conditions hold, but (1\ne1\cdot2\). With the sign local system on (Y), invariants vanish and higher cohomology vanishes by averaging, so its Euler number is0 despite rank1 and \(\chi(Y)=1\). This single example refutes both overly broad formulations. It does not refute the later conical-at-infinity finite-type claim.

Under the standard recursive interpretation of the source, compact links and finite cone charts make compact conical spaces finite-dimensional, metrizable and locally contractible. Such spaces are compact ANRs: the exact local-contractibility implication, with the separable metric and local compactness hypotheses, was checked in Guilbault–Moran2019, Proposition2.9, p298. West, Corollary5.3, then supplies a finite-polyhedral homotopy model. This uses metrizability and the finite recursive dimension; those are explicit interpretation choices, not words silently added to a potentially broader definition.

In a cone chart at the compactification point, deleting an open half-cone gives a compact core. New boundary points have charts obtained from a link chart times a half interval. Products of cones are cones on joins, so the recursive class is stable under that operation when the link/join conditions of the recursive definition are retained. On the punctured cone, the formula
\[r\longmapsto(1-t)r+t\max(r,1/2)\]
is a strong deformation retraction onto (r\ge1/2), fixed outside that collar. Gluing it to the identity verifies the source's radial retraction. For an excisive core/cone decomposition,
\[\chi(\widehat X)=\chi(\mathrm{core})+1-\chi(S_\infty),\quad
\chi_c(X)=\chi(\widehat X)-1,\quad
\chi(X)=\chi(\mathrm{core}),\]
which gives the end-defect formula. This is not a proof for arbitrary compactifications without cone charts.

The finite-polyhedral axioms determine both Euler functions by finite cell induction. Under the foregoing ANR interpretation, the same uniqueness extends to the conical-at-infinity category: ordinary homotopy invariance determines the compactification and core from finite models, and closed/open additivity determines compact supports. This is a modern conditional completion of the margin question. It is not a manuscript proof of triangulability. West gives a homotopy model; it does not imply that the original conical space is homeomorphic to a polyhedron. The finite face-poset model likewise applies to the model's barycentric subdivision, and yields no proposed minimal cardinality.

Zero-dimensional compact links are finite; one-dimensional cone charts are finite stars; cones on compact finite graphs give local two-dimensional triangulations. The later claims about arbitrary singular compact links in dimensions2/3 need a separate global triangulation argument. Moise's theorem for3-manifolds alone does not supply it. In dimension4, the compact (E_8) topological manifold is locally Euclidean, hence locally conical, and is not triangulable. The nontriangulability is the checked external Casson result reported in Manolescu's primary lecture notes §2.2; it is not independently reproved here. The manuscript asks about dimension4, so this is a negative answer to a question, not a refutation of an asserted theorem.

## 4. The Postnikov scratch leaf

For a connected loop CW-space, the fundamental group is abelian and its action on higher homotopy is trivial. Its first class (k_1\in H^3(K(G,1);M)) can be obtained by cohomology suspension from the next delooping's first relevant class in (H^4(K(G,2);M)). A second lift requires another compatible delooping. It is not forced merely by repeating arrows on the page.

The ambient group need not vanish even for an infinite loop space. Take (X=K(C_2,1)\times K(C_2,2)). Its first class vanishes because the2-type is a product, but (H^3(C_2;C_2)=C_2). The program enumerates all normalized cochains in degrees2–4: the sole possible nonzero value is on the all-ones tuple; every degree2 coboundary is zero, and both degree3 values are cycles modulo2. This is a complete finite cochain calculation, not a sample.

For the single-loop counterexample, let (M=\mathbb Z), (L=\mathbb Z\oplus\mathbb Z/4), \(\partial(m,b)=2m\), and \(w(x,y)=(0,xy\bmod4)\). Both groups are abelian. The reduced-quadratic-module identities of Baues–Conduché §4.1 hold: \(\partial w=0\); \(w(\partial a,x)+w(x,\partial a)=4mx=0\); and \(w(\partial a,\partial b)=4mn=0\), equal to the commutator. The induced crossed-module action is \((m,b)^x=(m,b+2mx)\). It is trivial on \(\ker\partial=C_4\), and \(\operatorname{coker}\partial=C_2\).

Use the section (s(0)=0,s(1)=1) and lift its only nonzero additive defect by (t(1,1)=(1,0)). The crossed-module cocycle is supported at ((1,1,1)), with value2 in (C_4). Enumeration shows that2 is a degree3 cycle and no nonzero degree3 coboundary exists, so the class is nonzero. Baues–Conduché §§4.5,4.7 supplies the realization of a reduced quadratic module by a simply connected3-type whose loop2-type is the associated crossed module. The computation verifies the algebra and cohomology; the realization theorem is an external input. Consequently a single delooping does not imply (k_1=0).

For a double loop space, the relevant double cohomology suspension is zero; Arlettaz's survey Lemma7.4, Proposition7.5 and Theorem7.6 give the exact argument. This yields a split2-type. Baues–Conduché Theorem1.9 separately excludes making such splitting natural in the delooped space. Neither assertion says the entire loop space is a product, or that the ambient (H^3) group vanishes.

## 5. Analytic and integral Schwarzians

For Hasse coefficients (a_i=D^{(i)}f), (b_i=D^{(i)}h), composition through order3 is
\[c_1=a_1b_1,\quad c_2=a_1b_2+a_2b_1^2,\quad
c_3=a_1b_3+2a_2b_1b_2+a_3b_1^3.\]
Put \(Q(a)=-a_3/a_1+(a_2/a_1)^2\). The program reduces
\[Q(c)-b_1^2Q(a)-Q(b)\]
to the zero rational function over \(\mathbb Z[a_i,b_i,a_1^{-1},b_1^{-1}]\). Because the identity is integral before specialization, it works over every commutative base with invertible first jets. Subtracting the identities for (f) and (g) gives quadratic-differential coordinate covariance of \(G_0(f,g)=(Q(g)-Q(f))dt^2\). Additivity in a third coordinate is cancellation. The symbolic Möbius test gives (Q=0), hence projective invariance.

In characteristic0, (f''=2D^{(2)}f) and (f'''=6D^{(3)}f), so the source's ordinary expression satisfies (G=12G_0=-2(S(g)-S(f))dt^2). “Divide by12” means construct the displayed integral Hasse formula; it is not division by a unit on every base. The test (G_0(t,t^2)=dt^2/(4t^2)) requires (2t) invertible and contradicts the retained (dt^2/(2t)). The cube gives (2dt^2/(3t^2)) where (3t^2) is invertible; in characteristic2 its value is0. Nonvanishing in characteristics2 and3 follows instead from (t+t^2) and (t+t^3), with first jet1 and values1 and−1 respectively. These are valid étale coordinates on suitable neighborhoods (indeed the displayed first derivative is identically1 in the respective characteristic).

For the complex analytic statement, (S(f)=S(g)) implies (g) is a constant Möbius transform of (f) locally, and a matched2-jet makes that Möbius transform the identity. Analytic continuation gives equality on a connected domain. To solve a prescribed Schwarzian locally, choose independent solutions of (u''+(q/2)u=0); their ratio has Schwarzian (q), as the Wronskian calculation shows. This gives local sheaf surjectivity and the torsor of projective coordinates modulo locally constant (\mathrm{PGL}_2\). Deligne I§5, especially5.8–5.10, is the exact published counterpart; his normalization is (S/6=-Q). There is no assertion of a global single-valued solution or canonical global section.

A universal rational jet function with polar support contained in (a_1b_1=0) has a reduced denominator consisting only of powers of those variables, by unique factorization in the polynomial ring. Realization of arbitrary complex finite jets with nonzero first derivative makes this a useful route to the source's denominator claim. Applying it to the source's analytic expression with variable coefficient functions requires specifying a reduced local coefficient domain; that translation is kept explicit.

None of these identities proves classification of every rational differential operator allowed by scan72, nor integral uniqueness among all base-natural Hasse operators. The known smooth-group relative-cocycle classification has a different domain and regularity formulation. The exact analytic and integral universal quantifiers are therefore retained as distinct problems, rather than declared settled by verifying one formula. The opposite torsor difference conventions on scans72 and73 are also retained; reversing the additive action repairs the sign, but that is a convention choice, not an ink decision.

## 6. Targeted review of root's no-Ga proof (C-SA04-676)

This section reviews the short argument supplied by the root agent. It is a targeted proof check, not a second independently originated proof or an attestation that A read the root's BLR source.

Let $R$ be a DVR with uniformizer $\pi$ and fraction field $K$. Let $G/R$ be a Néron group scheme, in particular smooth, separated and locally of finite type, with the Néron mapping property for smooth $R$-schemes. Suppose a closed subgroup immersion $i:\mathbf G_{a,K}\hookrightarrow G_K$ exists. Its tangent map is injective, so $v=d i(1)$ is nonzero in $\operatorname{Lie}(G_K)$. This uses the closed-immersion hypothesis: an arbitrary nonzero homomorphism can have zero differential in characteristic p.

For every integer $n\geq0$, the generic morphism $i\circ[\pi^{-n}]$ extends to a morphism $f_n:\mathbf G_{a,R}\to G$ by the Néron property. The extension sends zero to zero: its composition with the zero section and the identity section agree generically, hence agree by uniqueness (or separatedness). Therefore differentiation gives an $R$-linear map into $L=\operatorname{Lie}(G/R)$ whose value on1 is $\pi^{-n}v$ after extension of scalars to $K$.

Smoothness and local finite presentation at the identity make $L$ finite locally free, hence finite free over the local ring $R$; global finite type of $G$ is unnecessary. Thus $\pi^{-n}v\in L$ for every $n$, equivalently $v\in\bigcap_{n\geq0}\pi^nL=0$, a contradiction. The final intersection statement follows coordinatewise from the discrete valuation and needs neither completeness nor henselianity. Scalar multiplication by $\pi^{-n}$ is a $K$-automorphism of the additive group in every characteristic, so no inseparability exception occurs in this step.

The proof therefore establishes the exact no-Ga implication used on cote100 scan53 under the standard Néron-model hypotheses. It does not prove existence of Néron models for arbitrary groups, the semiabelian-image factorization, or the broader BT extension theorem.
