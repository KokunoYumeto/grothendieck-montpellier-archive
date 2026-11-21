# F69: an actual variable-group quotient of the whole path correspondence

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

The construction proposed by root works as an actual global scheme and torsor, including the nonreduced diagonal divisor. It normalizes the whole three-point path correspondence by a group that changes from a multiplicative group to an additive group. It does not invert its ordinary compact-cohomology object.

The four-point calculation has a precise negative conclusion: the second named group family cannot descend equivariantly under the first named action, because its fibers change group type along a single orbit. A separate natural second-stage endpoint action leaves a fixed-point classifying-stack stratum. Neither conclusion rules out every weaker or higher coherent stack construction, or identifies any designated nonstandard action or basis.

## 1. Base, divisor and the exact finite-flat algebra

Let k be any field. No characteristic restriction is needed for the scheme and group constructions. Put

\[
 Y=\mathbb P^1_x\times\mathbb P^1_z,\qquad
 Z=\mathbb P^1_t\times Y,
 \qquad p:Z\longrightarrow Y.
 \tag{VQ1}
\]

Let Gamma_x and Gamma_z be the two section divisors t=x and t=z. Define the relative effective Cartier divisor

\[
 \mathscr D=\Gamma_x+\Gamma_z,\qquad
 I_{\mathscr D}=I_{\Gamma_x}I_{\Gamma_z},
 \qquad \pi=p|_{\mathscr D}.
 \tag{VQ2}
\]

This is the sum as Cartier divisors, not the reduced union at the diagonal. Its diagonal fiber is a double point.

### Proposition VQ-A

The morphism pi is finite locally free of degree two. If

\[
 \mathcal A=\pi_*\mathcal O_{\mathscr D},\qquad
 \Delta=\{x=z\}\subset Y,
 \qquad \mathcal L_0=\mathcal O_Y(-\Delta),
 \tag{VQ3}
\]

then evaluation at x is an augmentation and the unit splits the exact sequence

\[
 0\longrightarrow\mathcal L_0
 \longrightarrow\mathcal A
 \xrightarrow{\operatorname{ev}_x}\mathcal O_Y
 \longrightarrow0.
 \tag{VQ4}
\]

On a chart on which x,z,t are affine, set h=z-x and c=t-x. The complete algebra is

\[
 \mathcal A=R[c]/(c^2-hc),\qquad
 \operatorname{ev}_x(c)=0,\quad
 \operatorname{ev}_z(c)=h.
 \tag{VQ5}
\]

### Proof

Use the three distinct k-points 0,1,infinity of the projective line. The opens

\[
 U_a=(\mathbb P^1\setminus\{a\})_x
          \times(\mathbb P^1\setminus\{a\})_z,
 \qquad a\in\{0,1,\infty\},
 \tag{VQ6}
\]

cover Y: two geometric endpoints cannot contain all three specified points. On U_a the support of D avoids t=a. In the associated affine coordinate it is the monic divisor

\[
                (t-x)(t-z)=0.
\]

Its algebra is free over the base on 1,t, equivalently 1,c, and has relation (VQ5). This proves finiteness and local freeness of degree two directly, with no constant-fiber-length inference.

Because the section ideals are invertible, the kernel of O_D to O_Gamma_x is

\[
 I_{\Gamma_x}/I_{\Gamma_x}I_{\Gamma_z}
       \simeq I_{\Gamma_x}|_{\Gamma_z}
       \simeq\mathcal O_Y(-\Delta).
\]

Finite pushforward gives (VQ4), and its unit is a splitting. Multiplication in its kernel is given by the natural inclusion L_0 to O_Y: in a local generator c, it is c^2=hc. In particular this is an actual algebra, not merely a rank-two vector bundle.

At a geometric off-diagonal point the algebra is kbar times kbar. At a diagonal point it is kbar[epsilon]/epsilon^2. The nilpotent is retained. All displayed constructions commute with arbitrary base change, as is also apparent from the monic equation. QED.

## 2. A global smooth group with multiplicative and additive fibers

Let

\[
 \mathcal G=\operatorname{Res}_{\mathscr D/Y}\mathbb G_m.
 \tag{VQ7}
\]

This notation represents the functor of units in A_T for every Y-scheme T. Representability here is explicit: it is the norm-nonzero open in the rank-two vector bundle A. For a+bc in (VQ5), multiplication has determinant

\[
                   N(a+bc)=a(a+hb).
 \tag{VQ8}
\]

Evaluation at x defines a split group homomorphism G to G_m. Define

\[
 \mathcal J=\ker(\operatorname{ev}_x:\mathcal G\to\mathbb G_m).
 \tag{VQ9}
\]

Since a unit has invertible value at x, division by that scalar identifies G canonically with G_m times J. Thus J also represents the fppf quotient G/G_m by scalar units. This proves the claimed quotient representability, rather than assuming it.

Globally J is an open in the total space of L_0. Locally it consists of units 1+uc, so

\[
 \mathcal J|_{U_a}
 =\operatorname{Spec}R[u,(1+hu)^{-1}],
 \qquad
 u\odot v=u+v+h uv.
 \tag{VQ10}
\]

The identity is0 and the inverse is -u/(1+hu). The law is associative and commutative because it is multiplication of the actual units1+uc. Under a change of the local generator of L_0 these formulas glue by (VQ9).

The scheme J is smooth affine of relative dimension one, being an open in a line bundle. For h invertible the coordinate1+hu identifies its fiber with G_m. For h=0 the law is addition, so its fiber is G_a. Globally on the diagonal the group is the additive vector group of L_0|Delta=O_P1(-2); it is not asserted to be a globally constant G_a-bundle there. Off the diagonal the two evaluation maps give a global multiplicative coordinate, such as ev_x/ev_z.

Equivalently J is the open of invertible lines in the projective bundle of A. The scalar normalization using ev_x is compatible with that description on every test scheme.

## 3. Evaluation identifies the frame torsor with the actual path scheme

Write H=H^0(P1,O(1)), a two-dimensional k-vector space, and let

\[
 \mathcal M=\pi_*(\mathcal O_{\mathbb P^1}(1)|_{\mathscr D}).
\]

The evaluation map is an isomorphism of vector bundles

\[
                 H\otimes_k\mathcal O_Y
                  \xrightarrow{\;\sim\;}\mathcal M.
 \tag{VQ11}
\]

One can see this either from

\[
 0\to O_Z(-1)\otimes p^*O_Y(-1,-1)
   \to O_Z(1)\to O_{\mathscr D}(1)\to0
 \tag{VQ12}
\]

and the elementary vanishing of both cohomology groups of O_P1(-1), or directly on (VQ6): the sections1,t restrict to a basis1,c, with t=x+c and determinant one. The latter local calculation proves (VQ11) on the whole base, including the double-point fiber.

Let Tfr be the scheme of A-generators of M:

\[
 \mathcal T_{\mathrm{fr}}
 =\operatorname{Res}_{\mathscr D/Y}
       \operatorname{Isom}_{\mathscr D}
            (O_{\mathscr D},O(1)|_{\mathscr D}).
 \tag{VQ13}
\]

This is the open subset of M for which the map A to M, a to a s, is an isomorphism. Its frame condition is a determinant nonvanishing condition. Multiplication gives an actual G-action.

Projectivize the frame line:

\[
 \mathcal P=\mathcal T_{\mathrm{fr}}/\mathbb G_m
       \subset\mathbb P_{\mathrm{lines}}(\mathcal M).
 \tag{VQ14}
\]

Here projective space parametrizes lines of sections; it is not a convention about quotient lines. The quotient in (VQ14) is the ordinary open projective bundle, verified by local trivializations of a line and scalar frames.

A nonzero section of O(1), up to scalar, has a unique zero y in P1. It generates O(1)|D precisely when its zero is neither x nor z. This is true also on the double point: a section is a generator in the local dual-number algebra exactly when its value at the support is nonzero. In families the same condition is the determinant-open condition in (VQ13). Consequently the zero-of-section map gives an actual scheme isomorphism

\[
 \mathcal P\simeq
 \{(x,y,z)\in(\mathbb P^1)^3:x\ne y,\ y\ne z\}.
 \tag{VQ15}
\]

It is compatible with the projection to Y and with base change. In particular it is the whole F62 path space, not only its off-diagonal part.

### Proposition VQ-B

The projective action of J on P makes P to Y a Zariski locally trivial J-torsor. The canonical map

\[
       \mathcal J\times_Y\mathcal P
          \longrightarrow\mathcal P\times_Y\mathcal P,
          \qquad (g,p)\longmapsto(gp,p)
 \tag{VQ16}
\]

is an isomorphism.

### Proof

For two A-frames s,t of M, their ratio t/s is a unique unit of A. Changing either scalar frame changes that ratio by a scalar, so it gives a unique class in J between the corresponding projective frames. This defines the inverse to (VQ16), locally on scalar frame charts, and the scalar-independence makes the inverse glue.

There are actual Zariski local sections. On U_a choose the section of O(1) vanishing at the fixed point a. Since a differs from both endpoints it is an A-frame on D. Its projective line is the path point y=a. Thus the opens (VQ6) trivialize the torsor, with regular inverse ratio maps. Smooth surjectivity also follows from these trivializations.

The local multiplication action is completely explicit. Trivialize M as an A-module by this chosen frame. On coordinates a+bc, multiplication by1+uc sends

\[
       [a:b]\longmapsto[a:b+ua+hub].
 \tag{VQ17}
\]

Its determinant1+hu is invertible. Thus it is a projective automorphism on the entire projective bundle, not only its generator open. It fixes the endpoint zero-lines, and its restriction to the generator open is exactly the torsor action. This also proves the action is an actual scheme map, not just a transitive action on geometric points. QED.

## 4. The quotient is the base, with exact finite-field counts

The torsor supplies a canonical equivalence of fppf quotient stacks

\[
                           [\mathcal P/\mathcal J]\simeq Y.
 \tag{VQ18}
\]

For completeness, in the torsor description of the quotient stack, an object over T to Y is a J_T-torsor Q together with an equivariant map Q to P_T. Such a map is an isomorphism: locally both torsors are J_T and it is a translation. The object is therefore uniquely isomorphic to (P_T,id). Its automorphism preserving that map is the identity. This proves (VQ18), including the absence of residual inertia, and is compatible with all base changes.

This is the standard quotient-stack/torsor framework of Stacks Proposition95.15.3, tag04WM; its use here follows the explicit proof of the torsor hypotheses.

Over F_Q the fibers have the following counts:

| Endpoints | Algebra fiber | Group fiber | Number of path points | Quotient fiber |
| --- | --- | --- | --- | --- |
| x differs from z | F_Q times F_Q | G_m | Q-1 | one point |
| x equals z | F_Q[epsilon]/epsilon^2 | G_a | Q | one point |

The group orders equal the path counts in the respective rows. This equality is realized by the free transitive actions, not used as a substitute for proving them. The total path count is

\[
 Q(Q+1)(Q-1)+(Q+1)Q=Q^2(Q+1).
 \tag{VQ19}
\]

The quotient has (Q+1)^2 points. Its fiberwise groupoid mass is one, with trivial automorphism, because it is the actual scheme Y. No Lang theorem, stack trace formula or cancellation of a cohomological Euler class is needed for these assertions.

## 5. The F62 Chern extension is retained

Let O=Y minus Delta. At distinct endpoints the two tautological lines V_x,V_z split k^2. A third line V_y avoiding both is the graph of a nonzero linear map V_x to V_z. Therefore

\[
 \mathcal P|_O\simeq
      \operatorname{Hom}(V_x,V_z)^\times
      \simeq O(1,-1)|_O^\times.
 \tag{VQ20}
\]

This is the actual F62 torsor. To match its usual scalar action, use the coordinate ev_x/ev_z on J|O: multiplying a section by a unit with endpoint values u_x,u_z multiplies its graph parameter by u_x/u_z. Reversing that multiplicative coordinate would simply invert the group parameter; no line-bundle orientation is silently changed.

For the cohomology calculation take ell invertible in k, a finite extension E/Q_ell, and geometric cohomology after base change to an algebraic closure. Over a finite field retain its Weil action as in F62. The diagonal Gysin sequence identifies

\[
 H^2(O_{\bar k},E(1))
     =\big(Eh_x\oplus Eh_z\big)/E(h_x+h_z).
 \tag{VQ21}
\]

Here the diagonal class is h_x+h_z. Thus c_1(O(1,-1))=h_x-h_z is nonzero: it becomes2h_x in the one-dimensional quotient. This calculation works in every characteristic of the finite base field, since the coefficient field has characteristic zero.

The existing F62 compact-fiber triangle remains

\[
 Rf_!E\longrightarrow E_O(-1)[-2]
     \xrightarrow{c_1(O(1,-1))}E_O
     \longrightarrow Rf_!E[1].
 \tag{VQ22}
\]

It is not split: nonzero geometric Chern class already witnesses nonsplitting after geometric base change, hence also before it. The quotient (VQ18) has not removed its Chern class by a cohomological splitting or replaced the relative object by the constant split torus complex. It uses the actual action and equivariant quotient of the space.

Already over a point, [G_m/G_m]=point is not the tensor inversion of RΓ_c(G_m,E). The geometric quotient changes the category and retains the group action; it supplies no additive strong monoidal functor that inverts the ordinary compact-cohomology object. This is why the construction is compatible with F68.

## 6. Four-point paths: the exact equivariant-descent obstruction

Put

\[
 \mathcal W=\{(x,y,z,w):
                x\ne y,\ y\ne z,\ z\ne w\}.
 \tag{VQ23}
\]

The first J-family is J_(x,z), pulled back from the endpoints of the first two edges. It acts on y and fixes x,z,w, preserving W. The second named family is J_(y,w), pulled back from the endpoints of the last two edges.

### Proposition VQ-C

The group scheme J_(y,w) over W admits no equivariant group-scheme descent datum for the first named action J_(x,z) on W. In particular these two specified families cannot be implemented as commuting local quotient actions by transporting the second family equivariantly along the first action.

### Proof

It suffices to base change to an algebraic closure. Fix x=0,z=infinity,w=1. The first fiber group is G_m, acting transitively on the possible y in G_m. Start with y=1 and send it to any b distinct from0,1. Such b exists in every algebraic closure, including characteristic2.

At the first path the second group is J_(1,1), hence G_a. At the translated path it is J_(b,1), hence G_m. An equivariant group-family structure would give a group-scheme isomorphism between these two fibers along this arrow. None exists: even their underlying varieties are nonisomorphic, since the coordinate ring of A1 has only constant units whereas that of G_m has a nonconstant unit.

The first step of an equivariant transport is already impossible, independently of any cocycle identity. This proves precisely the stated failure of descent for the second named family. QED.

The counterexample uses the path (0,1,infinity,1), whose nonadjacent points y,w may coincide. These coincidences are part of the actual path space; removing them changes the correspondence and is not preserved by the first action in this example.

### A natural new second-stage action retains a stack stratum

One can still quotient the first torsor. Pullback of (VQ18) gives

\[
 [\mathcal W/\mathcal J_{x,z}]
     \simeq R_z:=\{(x,z,w):z\ne w\}.
 \tag{VQ24}
\]

No condition z differs from x is introduced. If one now defines a new second-stage action using the endpoint group J_(x,w), formula(VQ17) gives its actual projective action on z, preserving z differs from w because w is fixed.

This is a new endpoint action, not the equivariant descent of the original J_(y,w) disproved above. Its quotient has an explicit nontrivial fiber:

- If x differs from w, identify P1 minus w with A1 and x with0. The group is G_m and acts by a multiplicative coordinate or its inverse. The quotient is [A1/G_m]. Its open nonzero orbit has quotient a point, while the fixed point z=x contributes B G_m.
- If x equals w, the group is G_a, acting by translations on P1 minus x. The quotient is a point.

For the first row the finite-field mass is

\[
                   1+\frac1{Q-1}=\frac Q{Q-1},
 \tag{VQ25}
\]

not one. The B G_m contribution is legitimate: every line over a field is trivial and its automorphism group has Q-1 elements. For the second row the torsor quotient is a point directly.

Thus this particular successive quotient does not yield the endpoint scheme Y again. The reverse parenthesization has the analogous one-punctured-line issue. This is not an assertion that every possible stack-valued associator or higher normalization is impossible. The two calculations isolate the data which a further construction must change or supply: transport of the varying neighboring group, or treatment of the residual fixed-point stratum.

### A precise finite-Weil comparison for this residual mass

Fix distinct endpoints over F_Q. At extension degree n the mass of this particular second-stage fiber is

\[
                  s_n=\frac{Q^n}{Q^n-1}
                       =\sum_{j\ge0}(Q^{-j})^n.
 \tag{VQ26}
\]

It cannot agree eventually with any finite uninserted Weil Euler trace. Here is a direct finite-rank proof, consistent with the earlier F26 criterion. For N at least1 and any size r+1, the rational Hankel matrix

\[
                     H_{ab}=s_{N+a+b},\qquad 0\le a,b\le r
\]

is positive definite over the reals. Indeed, for a nonzero real vector v and polynomial p(t)=sum_a v_a t^a,

\[
             v^\mathsf{t}Hv
                =\sum_{j\ge0}Q^{-jN}\,p(Q^{-j})^2>0.
\]

The series converges, and a nonzero polynomial cannot vanish on all the infinitely many distinct numbers Q^{-j}. Thus det H is a nonzero rational number in every size. In contrast a sequence sum_{i=1}^r c_i alpha_i^n has each such Hankel matrix of rank at most r, over its characteristic-zero coefficient field. Eventual equality is contradicted by choosing N beyond its threshold; the nonzero rational determinant stays nonzero in that field. An uninserted finite Weil Euler trace is precisely such a finite sum, including signed multiplicities and nonsemisimple Frobenius.

This excludes only a finite-coefficient trace comparison for the exact residual mass (VQ26). It does not refute the actual quotient stack, already constructed, or every possible higher quotient normalization.

## 7. Exact positive result and unresolved comparison

The global three-point quotient, including its scheme structure, nilpotent diagonal, action and finite-field fibers, is constructed and proved. It is an actual geometric normalization of the ordinary path correspondence.

No named nonstandard generator relation, quantum coordinate algebra, upper/lower lattice, canonical labels, pure coefficient comparison or pointwise sign bound is supplied by this torsor identity. A weak or higher coherent use of quotient correspondences remains a separate construction problem. PropositionVQ-C only rules out its explicitly stated equivariant-transport premise.

## 8. Separate Grothendieck dictionary and precise source status

The divisor ideals, finite locally free algebra, invertible A-module and evaluation map are actual affine and coherent-sheaf data. EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 provide the previously verified module/sheaf dictionary. The actual monic equation and all group/action/torsor assertions are proved above.

The group scheme and quotient are in the ordinary scheme/group-functor framework. Stacks Definition29.49.1 tag02KA is the exact finite-locally-free convention; Section97.11 tag05Y8 defines restriction of scalars and Lemma97.11.2 tag05YC proves its base-change compatibility. In this example representability is the explicit norm-open calculation, stronger than merely invoking general algebraic-space representability.

Stacks Situation95.15.1 and Proposition95.15.3 tag04WM give the precise torsor description of the quotient stack used in(VQ18). No quotient theorem is invoked before the actual group action and locally trivial torsor are proved.

On the off-diagonal the split multiplicative group also fits the existing SGA3 I4.7.2--3 / cote90 scan17 character framework; that diagonalizable-group language is not applied to the additive collision fibers. The F62 Gysin and Chern computation uses its already checked Milne Theorem16.1/Corollary16.2 p108, Theorem23.2 pp139--140 and smooth-duality conventions, together with the actual compactification calculation proved there.

The contrast with F68 concerns actual quotient actions versus ordinary coefficient-object inversion. SGA6 V Sections2--3 / cote133 scan18 remains the existing actual/virtual coefficient framework with its recorded source-access qualification; it does not furnish this quotient or a noncommutative lambda-ring. No new archival result or unverified scan locator is asserted.

### Primary sources opened and read for this report

- https://stacks.math.columbia.edu/tag/02KA — Definition29.49.1, exact definition. Ref turn950679750view2.
- https://stacks.math.columbia.edu/tag/05Y8 — Section97.11, restriction-of-scalars definition and sheaf/base-change context. Ref turn689232793view1.
- https://stacks.math.columbia.edu/tag/05YC — Lemma97.11.2, full statement and proof. Ref turn950679750view1.
- https://stacks.math.columbia.edu/tag/04UV — Situation95.15.1 and torsor description. Ref turn689232793view0.
- https://stacks.math.columbia.edu/tag/04WM — Proposition95.15.3, complete statement and proof. Ref turn950679750view0.

These are known framework statements. The explicit finite-flat family, its action and the new four-point application are proved in this report; no source is credited with those deductions.

## 9. Actual check record

The author reconstructed the local monic algebra, global kernel line, norm and group law, evaluation determinant, ratio inverse, projective action, finite-field counts and every four-point scope distinction. No numerical test is substituted for the scheme-valued or descent proofs.

Theta independently supplied and checked the four-point Ga-versus-G_m fiber argument during this construction; the complete global proof and the second-stage stratum calculation are written here. Root supplied the original quotient construction and separately checked its proposed global direction.

Fresh independent whole-proof and final-fragment review is requested. No main paper or shared master log was edited.
