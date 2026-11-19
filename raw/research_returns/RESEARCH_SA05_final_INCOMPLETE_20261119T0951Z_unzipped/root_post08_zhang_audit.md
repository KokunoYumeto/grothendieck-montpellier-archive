# A bounded audit of Zhang's invariant-cycle comparison

**Scope.** This note concerns the archived arXiv version 2009.07089v3, submitted 29 April 2022 and internally dated 2 May 2022. Its page numbering has 50 pages. It does not automatically attribute a wording issue to a later or differently typeset version. The source is Shou-Wu Zhang, *Standard conjectures and height pairings*, subsequently published in *Pure and Applied Mathematics Quarterly*, 18(5), 2221–2278 (2022), DOI 10.4310/PAMQ.2022.v18.n5.a7. Publication metadata was checked against Princeton's author record and the publisher's article page; the publisher records online publication on 12 January 2023.

Root read the definitions in §1.1, pp. 8–9; the complete local proof of Theorem 1.3.1, pp. 14–16; and Proposition A.1.1 with its complete proof, pp. 37–38. The actual PDF page 9 was also rendered and visually inspected. The retained source is `sources/root_post08/Zhang2022v3.pdf`, whose SHA256 is `397b44c28e6166f89f538d8415f45a3967dc090c6127669b16a98fd6e0fa0a89`. Fetch details are in `code/fetch_root_zhang_source_output.json`. Raw third-party sources are not redistributed inside the checkpoint ZIP.

## 1. The checked invariant-cycle equivalence

Use the source's strictly local convention: the complete discrete valuation ring has separably closed residue field, and the scheme descends to a trait with finite residue field in the case used here. Let `X` be proper, flat and regular over this ring, with relative dimension `n`, smooth generic fibre, and an ample class. Write `Y=X_s`. Supported localization gives

\[
\cdots\longrightarrow H^{i-1}(X_\eta)
\longrightarrow H^i_Y(X)\xrightarrow{\mu_i}H^i(Y)
\longrightarrow H^i(X_\eta)\longrightarrow\cdots.
\]

Zhang defines

\[
H^i_\phi(Y)=\operatorname{im}\mu_i,
\qquad H^i_\psi(Y)=\operatorname{coker}\mu_i.
\]

Thus `H_psi` is the image in the cohomology of the generic fibre over the strictly local field. It is not defined as the image in geometric cohomology or in its inertia invariants. These are different objects until the relevant comparison is proved.

Properness and supported duality give weights at most `i` on `H^i(Y)` and at least `i` on `H^i_Y(X)`. Exactness and disjoint weight ranges consequently identify

\[
H^i_\psi(Y)=W_iH^i(X_\eta).
\]

On the other hand, Hochschild–Serre gives

\[
0\longrightarrow H^{i-1}(X_{\bar\eta})_I(-1)
\longrightarrow H^i(X_\eta)
\longrightarrow H^i(X_{\bar\eta})^I\longrightarrow0.
\]

There is no general right to discard the left term before controlling its weights. Generic hard Lefschetz preserves the weight filtration on geometric inertia invariants, but that fact alone therefore does not prove hard Lefschetz for `H_psi`.

Theorem 1.3.1 proves the equivalence, simultaneously in all degrees of this fixed degeneration, of:

1. Hard Lefschetz for `H_psi`.
2. Bijectivity of `H_psi -> H(X_bar_eta)^I`.
3. Surjectivity of specialization from `H(Y)` to geometric inertia invariants.
4. The bound `weights H^i(X_bar_eta)^I <= i` in every degree.

For the implication from (1), split the even and odd Hochschild–Serre sequences as Lefschetz modules. Their two ends have centres differing by one half in the source's degree convention. Proposition A.1.1 proves the required unique splitting: primitive lifts are obtained by subtracting the unique element of the lower submodule that kills the relevant Lefschetz power. The same proposition makes the two off-diagonal maps between the localization splitting and the Hochschild–Serre splitting vanish in the indicated direction. This yields (2). The implications (2) to (3) to (4) are immediate from the maps and properness.

For (4) to (1), Poincaré duality and the bound in complementary degree imply that inertia coinvariants of `H^{i-1}` have weights at least `i-1`. After the twist `(-1)`, the left term in the displayed Hochschild–Serre sequence has weights at least `i+1`. Therefore its weights are disjoint from the at-most-`i` weights on the right. It follows that

\[
H^i_\psi(Y)=W_iH^i(X_\eta)
\simeq H^i(X_{\bar\eta})^I.
\]

Generic hard Lefschetz now gives the required Lefschetz isomorphisms on `H_psi`. This proof does not use the erroneous perfect-pairing wording discussed below.

The last display in the source's proof on p. 16 prints `W_i H^i(X_s)` at this step. The preceding localization calculation and the displayed argument show that the subscript must be `eta`. For a reducible semistable elliptic fibre, the special fibre's `H^2` can have dimension two while `H_psi^2` has dimension one, so this is not a harmless equality of the two underlying groups; it is a local typographical repair in an otherwise valid implication.

These fixed-degeneration equivalences do not assert weight–monodromy for that degeneration. The new exterior-power criterion in Part C adds tests on finitely many powers and quantifies over traits before obtaining the universal equivalence. No novelty claim is made for the determinant mechanism, which also occurs in Taylor–Yoshida's Lemma 1.4.

## 2. An explicit counterexample to the literal pairing claim on p. 9

Page 9 states that the supported perfect pairing induces perfect pairings on both `H_phi` and `H_psi`, including

\[
H^i_\psi(Y)\otimes H^{2n-i}_\psi(Y)(n)
\longrightarrow\mathbf Q_\ell.
\]

That unconditional assertion for `H_psi` fails even for a split multiplicative elliptic curve. The following example supplies its field, equation, regular model and cohomological verification without relying merely on a Kodaira-type label.

Take `R=Z_5`, `K=Q_5`, and `ell=3`. Let

\[
\mathcal W:\quad y^2z=x(x-z)(x-5z)\subset\mathbf P^2_R.
\]

Its generic fibre `E` is a smooth elliptic curve: the cubic roots `0,1,5` are distinct in `K`, and the point at infinity is smooth. Its discriminant is `6400`, with 5-adic valuation two, and `c_4=336` is a unit. The only singular point of the special fibre is the affine origin. The point at infinity and the rest of the special fibre are smooth over `R`.

Blow up the closed point with ideal `(5,x,y)` and take the strict transform `X` of `W`. In the `x` chart set `y=xv` and `5=xw`. The strict-transform equations are

\[
xw=5,\qquad v^2-x+6-w=0.
\]

Eliminating `w` gives `x(v^2-x+6)=5`. On the exceptional locus `x=0`, the only points where the morphism to `R` is not smooth have `v^2+1=0` in `F_5`, namely `v=2,3`. At either point `2v` is a unit. The second equation therefore eliminates `v` étale locally, leaving the regular strictly semistable equation `xw=5`. At all other points in this chart at least one factor is a unit, so the morphism is smooth.

In the `5` chart set `x=5a`, `y=5b`. Its equation is

\[
b^2-5a^3+6a^2-a=0.
\]

The special fibre is `b^2+a^2-a=0`. Its two derivatives vanish only at `b=0`, `a=1/2`, which does not satisfy the equation because its value is `-1/4`. This proves smoothness over the algebraic closure, not merely at the rational points. These charts cover the exceptional locus: its projective tangent conic is

\[
Y^2+X^2-PX=0\subset\mathbf P^2_{\mathbf F_5},
\]

and a point with `P=X=0` cannot lie on that conic. Its homogeneous derivatives also show it is smooth. It has the rational point `[P:X:Y]=[1:0:0]`, so it is a projective line. Away from the exceptional locus the blowup is an isomorphism over the already smooth locus. This proves regularity of `X` and strict semistability of its morphism to `R`. The blowup is projective and proper; it is flat because its integral affine coordinate rings are torsion free over the discrete valuation ring.

The strict transform of the original nodal cubic is its normalization, again a projective line. Explicitly, over `F_5` the parametrization on the affine part is

\[
x=v^2+1,\qquad y=v(v^2+1).
\]

It meets the exceptional projective line at the two distinct rational points `v=2,3`. The preceding charts prove that both components have multiplicity one and meet transversely. The geometric special fibre `Y` is therefore two projective lines with two transverse intersection points. Base change to the completion of the maximal unramified extension of `Q_5` places this same model in Zhang's strictly local convention.

The normalization exact sequence for this nodal curve gives

\[
0\longrightarrow\mathbf Q_3\longrightarrow\mathbf Q_3^2
\xrightarrow{(a,b)\mapsto(a-b,a-b)}\mathbf Q_3^2
\longrightarrow H^1(Y,\mathbf Q_3)\longrightarrow0,
\]

because both normalized components have zero first cohomology. Consequently `H^1(Y,Q_3)` is one dimensional. The vertices and the two edges are rational over `F_5`, so Frobenius acts as the identity on this graph cohomology. It has weight zero. Also `H^3(Y,Q_3)=0`, as can be seen from the same normalization sequence and the cohomology of projective lines.

Supported duality for the regular proper relative curve now gives

\[
H^1_Y(X,\mathbf Q_3)
\simeq H^3(Y,\mathbf Q_3)^\vee(-2)=0.
\]

Thus the source's definition yields

\[
H^1_\psi(Y)=H^1(Y,\mathbf Q_3)\simeq\mathbf Q_3\ne0.
\]

The asserted pairing on this group is induced by cup product in degree one. Graded commutativity makes it alternating. An alternating bilinear form on a one-dimensional vector space over `Q_3` is identically zero. Equivalently, its weight-zero source cannot map nontrivially by a Frobenius-equivariant cup product to the weight-two degree-two cohomology. Hence the pairing is not perfect.

The supplied `code/check_zhang_pairing_example.py` and its JSON output check the discriminant, both chart substitutions, normalization identity, rational exceptional points and incidence-matrix rank by exact arithmetic. The geometric smoothness and supported-cohomology arguments are the proofs above, not inferences from enumerating rational points.

## 3. The valid duality and the consequence for this project

The perfect pairing that always follows from the supported pairing and adjointness of the maps `mu` is

\[
H^i_\psi(Y)\otimes
\ker\!\left(H^{2n+2-i}_Y(X)\xrightarrow{\mu_{2n+2-i}}
H^{2n+2-i}(Y)\right)
\longrightarrow\mathbf Q_\ell(-n-1).
\]

Indeed, the annihilator of `im(mu_i)` in its perfect dual space is exactly `ker(mu_(2n+2-i))`. Passing to the quotient in the first factor gives this perfect pairing by finite-dimensional linear algebra. Localization identifies the second factor with the appropriate quotient of generic-fibre cohomology. This is the duality used in the checked proof of Theorem 1.3.1; it does not identify that second factor with `H_psi^(2n-i)`.

The literal p. 9 perfection claim and the local subscript typo are therefore kept separate from the valid invariant-cycle comparison. Neither changes any of the eight open universal rows. In particular, the example is not a counterexample to geometric weight–monodromy, to local invariant cycles for curves, or to Part C's exterior-power theorem.

## References and exact read limits

Zhang, S.-W. (2022). Standard conjectures and height pairings. *Pure and Applied Mathematics Quarterly, 18*(5), 2221–2278. https://doi.org/10.4310/PAMQ.2022.v18.n5.a7. Primary version actually read: https://arxiv.org/pdf/2009.07089v3, §1.1 definitions pp. 8–9; Theorem 1.3.1 complete local proof pp. 14–16; Proposition A.1.1 complete proof pp. 37–38. No claim of a full-paper audit or of checking the publisher's typeset mathematical text is made.

The normalization exact sequence, the cohomology of projective lines and supported duality are the same standard exact sequences used in Part C's already audited semistable and local invariant-cycle arguments. The explicit equations above independently verify the geometric hypotheses needed to apply them.
