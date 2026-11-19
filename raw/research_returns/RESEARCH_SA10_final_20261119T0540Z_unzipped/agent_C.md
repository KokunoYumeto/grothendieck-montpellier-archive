# Cote 150: mathematical contributions


## C2.05 — Known with explicit translation: the corrected smooth resolution theorem

The exact smooth replacement uses the whole boundary-fibration structure, not just one incidence level. Take a finite deployment whose nonempty object spaces are smooth manifolds with corners. Require every incoming \(\Sigma_{ij}\subset\Sigma_j\) to be a collective embedded boundary hypersurface, with their union the whole boundary, with incomparable incoming faces disjoint, and with the specified transverse product collars. Require the sources to be proper smooth locally trivial bundles with compact manifold-with-corners fibres, compatible with all base and fibre faces. On a triple require both the subset identity and projection control of C2.02. Require that the boundary of a source fibre consists exactly of the intermediate-label faces, and choose compatible radial collar germs.

In these hypotheses the data are precisely a system of manifolds with iterated boundary fibrations. To see the correspondence without suppressing labels, on a maximal piece \(\Sigma_m\) the hypersurface labelled \(i\) is \(\Sigma_{im}\), its base is \(\Sigma_i\), and its fibration is \(s_{im}\). At an intersection \(i<j<m\), the diagram is
\[
 \Sigma_{ijm}\xrightarrow{s_{jm}}\Sigma_{ij}\subset\Sigma_j,
 \qquad
 s_{im}=s_{ij}s_{jm}.
\]
This is exactly the commuting boundary-fibration diagram. Its inverse-image identity says that the horizontal boundary is the pullback of the base boundary. All other boundaries are the stated vertical fibre boundaries. Higher intersections are recovered by iterating these identities, so no further arbitrary associativity datum remains. Conversely such an iterated-fibration system supplies all the \(\Sigma_i,\Sigma_{ij}\), their intersections, sources, and collars. If two top pieces have a common lower stratum, retain the common base and use the disjoint union of their faces as one collective hypersurface. Separating that collective hypersurface would instead normalize a disconnected-link singularity.

Albin, \cite[Theorem 6.3(a)--(c), p.48]{C_Albin2016}, gives resolution and blowdown as inverse constructions for compact Thom–Mather spaces and manifolds with these iterated fibrations, after choosing compatible collars. Its paragraph following the theorem states explicitly that without fixed collars the blowdown is defined only up to isomorphism. The collective-hypersurface qualification and normalization warning are on p.49. The theorem's proof reduces to ALMP, \cite[Propositions 2.3 and 2.5, pp.253--257]{C_ALMP}; Propositions 2.6–2.7, p.258, give the isomorphism comparison.

For finite-depth, second-countable, locally compact spaces without compactness, the precise modern formulation is Albin--Banagl--Piazza, *Smooth atlas stratified spaces*, \cite[Theorems 2.10 and 2.13, pp.24--28]{C_ABP}. The former proves the resolution/blowdown equivalence for its smooth atlas category, with maps preserving the regular part and the interior respectively; the latter identifies the geometric objects with Thom–Mather spaces. We use its object and isomorphism statement. We do not identify arbitrary continuous stratified maps, arbitrary conically smooth maps, and its liftable smooth maps.

Here is why the cited theorem gives precisely the needed control identities. In the collar of a boundary fibration \(H_i\to\Sigma_i\), write a point as \((h,r_i)\) and collapse \(r_i=0\) along that fibration. Define \(\pi_i(h,r_i)=s_i(h)\) and \(\rho_i(h,r_i)=r_i\). On an overlapping lower collar \(k<i\), source compatibility makes \(\pi_i\) preserve the \(r_k\) coordinate, so \(\rho_k\pi_i=\rho_k\); triple commutativity gives \(\pi_k\pi_i=\pi_k\). Away from the zero radius the product coordinates and smooth bundle maps make \((\pi_i,\rho_i)\) a stratumwise submersion. These are Mather's two control identities and submersion requirement \cite[section 7, p.15]{C_Mather}. Conversely cutting a controlled tube at \(r_i=\epsilon_i\) gives the incoming face and its source. The two control equations restrict respectively to the subset identity and projection identity, and the controlled collar flow supplies the omitted radial germs. Iterating gives the cited resolution.

A single chosen \(\epsilon\) records only the corresponding level diagram. To claim equivalence of *control data* one must retain the radial collars, or equivalently all sufficiently small levels with their compatible identifications. C2.03 proves why this extra datum cannot be discarded. Different collar choices give isomorphic resolved geometric objects; they need not give equal numerical radius functions. Empty strata and empty hypersurfaces may be deleted. Disconnected strata are handled componentwise or with collective faces; one must not silently replace a disconnected fibre by its components.

## C3.04 — Proved: the exact local criterion for a manifold with the specified corners

First distinguish the literal §8 input from a collection of unrelated cone charts. For the finite recursive conical data actually defined on 150/035--036, retaining the boundaries always gives a precylindrical structure in the manuscript's collar sense. This assertion does not require source fibrancy. The induction is explicit in the original /036, visually checked: after cutting the minimal strata, (22) contains the old collared boundaries together with every new link boundary, as a mutually transverse family transverse to the remaining strata; the next conical datum is required on this entire system.

Here is the inductive verification. A cut replaces each selected cone direction by its radius interval and retains its zero-radius boundary. Conical transversality to an old boundary says in coordinates that this cut is a product with the old collar coordinate; hence each old collar restricts to the cut piece and commutes with the new collar. Distinct simultaneously cut minimal strata are disjoint, so their new faces are disjoint. By the recursive requirement the next cuts are products with all the retained coordinates. This proves the transverse-collar axioms at every stage and on every removed base piece \(\Sigma_i\). Two incoming labels that are incomparable cannot meet: their original closed strata intersect only in lower strata, and, after those lower strata have been cut, a common positive-radius link point would give a point of both original strata outside that lower intersection. Thus all nonempty face intersections have flag labels. Their subface intervals are the Boolean intervals proved in C3.02. The intersection of two such closed faces is the face for the union of their labels when that union is an admissible flag, and is empty otherwise; local incidence branches are retained separately. Including the full pieces and deleting empty faces verifies the finite closed-cover and intersection axioms (14). This proves precylindricity for each cut-open piece and hence for the maximal pieces comprising the full unzip of the literal recursive §8 datum. Merely choosing separate conical neighborhoods without this retained-boundary compatibility is not that datum.

The remaining question is exactly when this precylindrical output is a manifold with its specified corners. For any of TOP, PL, or smooth, fix a finite precylindrical structure with the stated compatible collars and incidence branches. At a point \(x\), let \(F_x^\circ\) be the open face obtained by intersecting precisely the boundary germs through \(x\), and deleting all smaller faces. Let \(k(x)\) be the number of those independent germs. The collar axioms provide a germ
\[
 (X,x)\cong (F_x^\circ,x)\times([0,\infty)^{k(x)},0)
\]
respecting each specified face. The resulting space is a manifold with these corners in the chosen category if and only if every \(F_x^\circ\) is a manifold in that category and the collar transition maps have that regularity. Its dimension is locally constant; for a single prescribed dimension \(n\), also require \(\dim F_x^\circ+k(x)=n\) for every point. Empty outputs satisfy the convention vacuously.

Indeed, a local manifold chart on \(F_x^\circ\), followed by the collar product, is exactly an orthant chart of dimension \(\dim F_x^\circ+k(x)\). Conversely a corner chart preserving all the prescribed faces restricts on their full intersection to a manifold chart on \(F_x^\circ\). Both implications are local; compatibility gives an atlas. Hausdorffness and second countability are required separately for the usual definition of manifold and are inherited in the finite resolution settings considered here.

This is an exact criterion rather than an assertion that every collared topological factor of a manifold is itself a manifold. In TOP that cancellation assertion is false by C5.03–04. Even the open cone on \(F=\Sigma H\) from C5.03 is homeomorphic to \(\mathbb R^5\), while its prescribed conical cutting produces \(F\times[0,\infty)\), which is not a manifold with boundary. Thus ordinary manifoldness of the original strata cannot alone validate an arbitrary topological choice of conical data.

For recursive finite-depth smooth or PL conical data whose resolved link pieces and base strata are manifolds and whose transitions lift compatibly to their resolutions, the criterion holds inductively: replacing a local cone \(B\times C(L)\) by \(B\times[0,\infty)\times\widetilde L\) gives its required orthant charts. The same is a sufficient criterion in TOP, with the full products checked as above. In the smooth Thom–Mather case it holds by C2.05. Finiteness can be replaced by locally finite finite-depth data with locally finite charts and collars; an arbitrary non-locally-finite family does not define an ordinary finite-dimensional corner chart at an accumulation point.

## C4.05 — Proved under an actual compatible conical deployment: \(V_d\simeq\Sigma_d\)

\input{C4_collar_proof_B}

## C4.06 — Proved: canonical normal-crossings form of 147/176 (294)

The notation here is checked in the original scans 147/173--177 \cite{C_Grothendieck147}. Their notation is a filtered normal bundle over \(B=D_{d_*}^*\), with a pair \(d_0''\le d_0'\) of entries of the flag and an exact sequence
\[
 0\longrightarrow A=\check N_{d_*,d_0'}
 \longrightarrow E=\check N_{d_*,d_0''}
 \xrightarrow{q}Q=\check N_{d_*,(d_0',d_0'')}
 \longrightarrow0.
\]
This is (286)–(287). The normal-crossings branches give \(Q\) a local decomposition into complex lines, with transitions allowed to permute those lines. Write \(Q^*\) for the complement of all coordinate hyperplanes. Thus its fibre is \((\mathbb C^*)^r\), not \(\mathbb C^r\setminus\{0\}\). For rank zero, the empty coordinate arrangement has complement the whole zero bundle; the torus fibre is a point. The same argument then applies without a puncture, and an empty base gives the empty equivalence. Page175(290) defines \(E^*=q^{-1}(Q^*)\); (291) describes \(E^*\to Q^*\) as a torsor for the pulled-back additive bundle \(A\).

The quotient map \(q:E^*\to Q^*\) is a canonical homotopy equivalence. Choose a Hermitian splitting \(E=A\oplus Q\); then
\((a,v)\mapsto((1-t)a,v)\) contracts the kernel and proves the claim. Splittings form an affine space, so their homotopies identify all inverse choices. The map \(q\) itself does not depend on a splitting.

The sector tube \(V^{d_0'}_{d_*,d_0''}\) is, by definition of the normal-crossings incidence sector, the neighborhood germ of \(B\) in the \(E\)-directions, with precisely the coordinates belonging to \(Q\) required to be nonzero. Its pro-homotopy type has a canonical comparison with \(E^*\). Here is a construction and a check of its ambiguity. For a simple normal crossings divisor, use its divisor line bundles with defining sections. Choose an ordinary smooth tubular projection onto the intersection \(B\) and connections on those line bundles. Parallel transport identifies their restrictions on a small neighborhood with their pullbacks from \(B\); the tuple of defining sections then has differential the normal-coordinate isomorphism along \(B\). The inverse function theorem, after variable-radius shrinking, gives an adapted tubular germ from the direct sum of the normal lines to the original space. It takes every coordinate hyperplane and every flag subbundle to the corresponding divisor incidence. This constructs the required sector comparison.

Normalize each adapted tubular germ to have identity derivative on the intrinsic normal bundle, by composing with the inverse of its fibrewise normal derivative. This preserves the coordinate arrangement and the flag subbundles. Arbitrary normal-bundle automorphisms are not being declared homotopic to the identity. If a kernel block has no chosen line decomposition, retain its coordinates from an ordinary tubular chart and use the defining sections in the quotient block; the same inverse-function argument respects every flag subbundle.

If \(\Phi,\Psi\) are two adapted tubular germs with the same normal derivative, their transition \(g=\Psi^{-1}\Phi\) fixes the zero section and has identity normal derivative. Fibre dilations give
\[
 g_t=\delta_{1/t}\,g\,\delta_t\quad(t>0),\qquad g_0=\mathrm{id}.
\]
Taylor's formula in normal coordinates shows this is a continuous, indeed smooth, family of germs through \(t=0\); its tangential displacement tends to zero and its normal derivative tends to the identity. Every \(g_t\) preserves the coordinate-hyperplane arrangement. Restricting to sufficiently small variable-radius neighborhoods makes the family defined for all \(t\in[0,1]\). The same construction works for parameter families. Hence the induced comparison on the sector has a unique homotopy class, compatible with refinements and changes of tubular choices. This supplies the canonical meaning that the manuscript explicitly leaves unresolved below (294).

The small-sector pro-germ also compares explicitly with the entire punctured bundle. For a bundle norm and a positive continuous radius function \(\eta\) on the base, the inclusion \(\{v\in E^*:\|v\|<\eta(\pi v)\}\hookrightarrow E^*\) is a homotopy equivalence. An inverse up to homotopy is
\[
 v\longmapsto \frac{\eta(\pi v)}{\eta(\pi v)+\|v\|}v.
\]
Interpolation of its strictly positive scalar factor with \(1\) supplies both inverse homotopies and preserves every coordinate nonvanishing condition. Such variable-radius disk neighborhoods are cofinal by the tubular chart and paracompactness of the base. Their natural inclusions therefore identify the sector prospace with the constant space \(E^*\), coherently under shrinking.

Combining it with \(q\) gives the precise statement
\[
 V^{d_0'}_{d_*,d_0''}
 \ \simeq\
 \left.\check N_{d_*,(d_0',d_0'')}^{\,*}\right|_{D_{d_*}^*}.
\]
The ambiguity is homotopy, not a distinguished homeomorphism of neighborhoods. A Hermitian norm further retracts each punctured line to its unit-circle bundle, giving the corresponding torus bundle; metrics form a convex space of choices.

For normal crossings with branch monodromy, perform the construction on the finite local branch-label cover. The normal line bundles and the quotient map descend equivariantly, as does the homotopy-class comparison, because the coordinate arrangement and the dilation are invariant under branch permutations. On a Deligne–Mumford orbifold chart finite-group averaging supplies invariant auxiliary metrics and connections. Thus the result is canonical in the incidence/orbifold category. Passing to an unlabelled orbit-poset and discarding stabilizers would lose data.

## C5.05 — Proved with the standard PL-bundle and smooth-submersion meanings

Work with the entire completed incidence system of C2.02, its transverse target collars, and its full boundary decomposition. Impose the following regularity on every source map. The positive PL and smooth assertions require these category-specific meanings of fibrancy. In PL assume the source is a locally trivial PL bundle and every collar and transition is PL. In the smooth case assume every source is a proper smooth submersion with the stated product behavior on horizontal faces. Together with full projection control this gives the vertical-face regularity proved below; alternatively one may start with the corresponding smooth bundles of corner manifolds. A map which is merely smooth and a Hurewicz fibration need not have the required differential regularity.

First, in PL, a locally finite polyhedron \(F\) such that \(F\times\mathbb R^m\) is a PL manifold is itself a PL manifold. Use a product triangulation and choose a top-dimensional simplex in the second factor. The link of its interior product with a vertex of \(F\) is the link of that vertex in \(F\). In a PL manifold that link is a PL sphere or ball, according as the point is interior or boundary. The link criterion gives the conclusion, at every vertex and then throughout \(F\). Applying this in a local bundle trivialization over an interior base point proves that the fibre is a PL manifold with boundary/corners; local triviality identifies the other fibres with it.

In the smooth case first verify tangential surjectivity on every vertical face, using the whole source-map system. On \(\Sigma_{ikj}\), with \(i<k<j\), projection control gives
\[
 s_{ij}|_{\Sigma_{ikj}}
   =s_{ik}\circ(s_{kj}|_{\Sigma_{ikj}}).
\]
The horizontal pullback and product-collar condition makes
\(s_{kj}|_{\Sigma_{ikj}}:\Sigma_{ikj}\to\Sigma_{ik}\)
a submersion, while \(s_{ik}\) is another source submersion. Their composite is therefore a submersion. Iterating this argument on flags gives surjectivity on every intersection of vertical faces. Thus one can choose horizontal lifts tangent to all those faces; in a product corner chart take such lifts simultaneously and combine them with a partition of unity. Horizontal base-boundary coordinates are separated by the specified product collars. The corner submersion theorem now gives fibre charts by fixing the base coordinates, so the fibre is a manifold with corners. Properness allows these lifts to be integrated over a common base neighbourhood, giving compatible local trivializations. An isolated smooth submersion lacking these vertical-face checks would not justify that conclusion.

In both categories a local chart on an arrow space \(\Sigma_{ij}\) therefore separates into base coordinates, horizontal base-boundary coordinates, fibre coordinates, and vertical fibre-boundary coordinates. The horizontal faces are exactly
\(\Sigma_{kij}\), \(k<i\), by the inverse-image identity; the vertical faces are exactly \(\Sigma_{ikj}\), \(i<k<j\), by the full boundary decomposition and the ordering of the incoming labels. Thus
\[
 \partial\Sigma_{ij}
 =\bigcup_{k<i}\Sigma_{kij}
   \ \cup\!
   \bigcup_{i<k<j}\Sigma_{ikj},
\]
while the intrinsic boundary of each source fibre consists only of the latter, intermediate-index pieces. These formulas include all corners through their intersections. This proves the mixed-fibre and face-boundary conclusions of /051, /063, and /067 under these precise PL and smooth hypotheses.

For /067 alone, no source bundle is needed if the incoming collars and all ambient spaces are PL/smooth: the same local link criterion in PL, or the smooth collar chart in the smooth category, proves that each transverse face intersection is a manifold with corners. The boundary formula follows by deleting exactly the other incoming faces through each point. The TOP counterexample C5.04 explains why this cancellation step cannot be copied into bare topology.

For /062, the implication from the bare order and face axioms is false in every category, by C5.02. Strong local triviality of the entire face diagram over the base collars is a sufficient correction in every category. For /070–071 in the ordered-space situation, C5.01 proves the claimed component order and makes the extra monomorphism assumption redundant whenever components are path-connected and open (in particular for manifolds and locally path-connected PL spaces), in all three categories, without the manuscript's finite-dimensionality hypothesis.


## C4.01 — Proved for finite metric HSS: (51), (56), (57), and (69)

Use a finite stratification satisfying the frontier condition, with closed lower unions and locally closed strata \(S_i=X_i^*\). This is the finite-index scope explicitly adopted at /038–039. Assume the metric space is homotopically stratified in Quinn's sense. Whitney and Thom–Mather examples fall in this scope. Put \(O_i=X\setminus\bigcup_{k<i}S_k\), so \(S_i\) is closed and pure in the open subspace \(O_i\). Let \(V_i\) be the prospace of open neighborhoods of \(S_i\) in \(O_i\), ordered by shrinking. These neighborhoods are also open in \(X\). Finite intersections define \(V_d\).

Quinn, \cite[Proposition 3.2, p.469]{Quinn1988}, gives one fixed nearly strict, stratum-preserving neighborhood deformation
\(h_i:N_i\times[0,1]\to O_i\), with \(h_i(x,0)=x\), \(h_i(x,1)\in S_i\), and \(h_i(s,t)=s\) for \(s\in S_i\). Until the final time it stays in the starting stratum. Reversing Quinn's interval convention gives the notation used here. The theorem applies to \(O_i\), whose induced stratification is again HSS: restrictions of pairwise tameness and holink fibrations give the defining conditions, or directly use Quinn 2.4 Corollary (2)–(3).

**Single-stratum germs.** Given an open \(U\supset S_i\), compactness of the time interval and continuity of \(h_i\) imply that
\[
 W_U=\{x\in N_i:h_i(x,[0,1])\subset U\}
\]
is open and contains \(S_i\). The fixed endpoint retraction \(r_i=h_i(-,1)\), restricted to \(W_U\), and the restricted homotopy prove that
\(S_i\to V_i\) is a pro-homotopy equivalence. The same endpoint map is used at all levels, so these are compatible pro maps, not unrelated levelwise equivalences. This proves (51). If \(Z\) is a locally closed union of strata containing \(S_i\), the homotopy on \(W_U\cap Z\) stays in \(Z\), including its endpoint, proving both arrows of (56).

**Flag germs.** Let \(d=(i_0<\cdots<i_n=j)\), and fix target neighborhoods \(U_{i_k}\) for every flag entry. First shrink \(N_j\) so that its whole fixed homotopy stays in \(U_j\). For \(k<n\), metric normality and closedness of \(S_{i_k}\) in \(O_{i_k}\) give open neighborhoods \(U'_{i_k}\) with
\(\overline{U'_{i_k}}^{\,O_{i_k}}\subset U_{i_k}\).
Set \(A=\bigcap_{k<n}U_{i_k}\) and \(A'=\bigcap_{k<n}U'_{i_k}\).
Because \(O_j\subset O_{i_k}\), one has
\(\overline{A'}^{\,O_j}\subset A\).
Let
\[
 W=\{x\in N_j:h_j(x,[0,1])\subset A\}.
\]
It is open and contains \(S_j\cap A\). Therefore
\(F=\overline{A'}^{\,O_j}\setminus W\) is closed in \(O_j\) and disjoint from \(S_j\).
Choose \(U'_j=N_j\setminus F\). Then \(A'\cap U'_j\subset W\), so its whole homotopy lies in \(A\cap U_j\). These restrictions of the one fixed \(h_j\) define a pro-homotopy retraction
\[
 V_d\longrightarrow V_d\cap S_j.
\]
It is the identity on \(S_j\), giving both inverse homotopies. If \(Z\) is a locally closed union of strata containing \(S_j\), the same homotopy restricted to \(Z\) stays there. The triangle through \(V_d\cap S_j\) proves (57), in fact under the weaker requirement \(S_j\subset Z\); the manuscript assumes \(X_j\subset Z\).

These are homotopy equivalences in prospaces, represented by maps and homotopies after cofinal shrinking; in particular they are isomorphisms in \(\operatorname{Pro}(\mathrm{HoTop})\). No assertion is made that taking a limit in ordinary spaces or topoi preserves them. A coherent pro-space formulation uses the same fixed homotopies, so all refinements come from restriction.

**Bands and (69).** Let \(J,L\subset I\) be convex bands satisfying \(J\prec L\): every member of \(J\) is below some member of \(L\), and every member of \(L\) is above some member of \(J\). The interval hull
\[
 I'=\{i:\exists j\in J,\ell\in L,\ j\le i\le\ell\}
\]
is convex; \(J\) is a lower set and \(L\) an upper set in \(I'\). For example, if \(j_0\le i\le j\) and \(j_0,j\in J\), convexity puts \(i\) in \(J\); the upper statement is dual. This proves the manuscript's order lemma, including uniqueness of the interval hull.

For a finite normal stratification choose a cofinal system of neighborhoods with \(U_i\cap U_k=\varnothing\) when \(i,k\) are incomparable. Indeed the two strata are disjoint closed subsets after removing both lower frontiers; normality separates them, and finitely many such shrinkings can be intersected. Thus any nonempty finite neighborhood intersection has flag labels. The space \(V_J\cap V_L\) is covered by the finitely many \(V_j\cap V_\ell\), \(j\in J,\ell\in L\). If \(j\le\ell\), the maximum label is in \(L\). If \(\ell<j\), then convexity and domination imply both labels belong to \(J\cap L\); again the maximum is in \(L\). The same remains true for every finite intersection of these pieces.

Apply the flag result to each such intersection, with \(Z=X_L^*\), which contains its largest stratum. It gives a pro-homotopy equivalence on every intersection after restricting to \(X_L^*\). Finite open-cover homotopy descent then gives
\[
 V_J^L=V_J\cap X_L^*\ \longrightarrow\ V_J\cap V_L
\]
as a pro-homotopy equivalence, proving (69). To justify descent concretely, use the finite poset of nonempty subsets of the finite cover-piece label set, with opposite inclusion for its intersection diagram. Its nerve has finitely many nondegenerate simplices. A partition of unity gives a homotopy inverse from the union to this finite homotopy colimit. The natural restriction map of intersection diagrams is an equivalence in prospaces at every object by the fixed-homotopy proof above; its inverses need not be chosen as separate natural maps. Finite homotopy colimits preserve this equivalence and commute with a synchronized cofiltered presentation: on mapping spaces this is the fact that filtered colimits commute with finite limits. Only finitely many source refinements are required. This argument does not truncate the unbounded ordinary Čech nerve, and would require a separate justification for an infinite index family.

This argument does not require a strictly commuting system of Mather retractions. The inherited R7 assertion that rho-control is necessary for this pro-homotopy statement is stronger than needed.

## C4.02 — Proved: the precise holink comparison, and the overlap exception

\input{C4_path_proof_B}

## C4.03 — Proved: spectral sequence (73) in its finite scope

Fix finite dominated bands, the interval hull \(I'\), and
\[
 D=\{d\subset J\cup L:d\text{ a nonempty flag},\
             \min d\in J,\ \max d\in L\}.
\]
Give \(D\) arrows \(d\to e\) when \(d\subset e\). Thus \(V_e\subset V_d\), and cohomological restriction is covariant in \(D\). For an abelian sheaf \(F\) on the neighborhood germ \(V_J^L\), interpret its cohomology as the filtered colimit of cohomology of representatives. There is a first-quadrant, strongly convergent spectral sequence
\[
 E_2^{p,q}=R^p\!\lim_{d\in D}H^q(V_d^{X'},F)
 \ \Longrightarrow\ H^{p+q}(V_J^L,F).
\]
This is the typed meaning of the category-cohomology notation in (73).

First choose cofinal representatives for which every upper-band neighbourhood \(U_l\) lies in the open upper union \(X_L^*\subset X'\). Their union is then exactly \(X_L^*\). Consequently the union of the pairwise cover pieces \(U_j\cap U_l\) is exactly \(V_J\cap X_L^*=V_J^L\) at that stage. All flags in \(D\) have maximum in \(L\), so their intersections are actual opens of this union. Thus no homotopy invariance of arbitrary sheaf cohomology is being invoked. Choose these representatives for the finite open cover and a flabby resolution of \(F\). Form the double complex whose degree \((p,q)\) is the product of
\(\Gamma(V_{d_p},\mathcal I^q)\) over chains \(d_0\subset\cdots\subset d_p\), with the usual alternating restriction differential horizontally. Its horizontal augmentation computes sections on the union. Exactness can be checked locally inside a covering piece: adjoining that piece to an intersection gives the common refinement and contracts the augmented Čech complex; empty intersections contribute zero. More precisely use the augmented complex of sheaves obtained by direct image from the open intersections. On a covering open set, contraction is by adjoining its flag; a nonflag union has empty intersection and contributes zero. This local contraction proves exactness without identifying the stalk of an open direct image outside its open set with zero. With a flabby resolution, all the open direct images are flabby. Flabbiness makes all restriction terms acyclic for sections, so the total complex computes sheaf cohomology on the union.

Taking vertical cohomology first yields the derived-limit complex of the coefficient diagram \(d\mapsto H^q(V_d,F)\), proving the displayed \(E_2\)-page. Taking filtered colimits over representative neighborhoods is exact in abelian groups and commutes with the finite products here. Finally \(D\) has bounded chain length, so the horizontal filtration is finite; there is no convergence or product-completion ambiguity. Empty \(D\) gives the empty union and zero groups.

## C4.04 — Refuted: HSS alone supplies an actual conical deployment

Quinn's example \cite[p.452]{Quinn1988} is the shrinking hedgehog
\[
 X=\bigvee_{n\ge1}[0,1/n],\qquad Y=\{0\},
\]
with the metric \(|s-t|\) on one arm and \(s+t\) on distinct arms. It is compact metric. The radial contraction \(h((n,s),t)=(n,(1-t)s)\) makes \(Y\) tame, strictly off \(Y\) until the final time; the holink map to a point is a fibration. Thus the two-step filtration is homotopically stratified in Quinn's general definition.

It has no mapping-cylinder neighborhood of \(Y\). Every neighborhood contains all sufficiently short arms, including their terminal endpoints, and these endpoints converge to \(Y\). In a mapping-cylinder neighborhood with radial coordinate \(r\), a point with \(0<r<1\) lies on an embedded interval through itself, obtained by varying \(r\) in both directions. A terminal endpoint of an arm cannot be an interior point of any embedded interval in \(X\). Hence every such endpoint would have to lie on the outer level \(r=1\). Continuity is contradicted by their convergence to the apex \(r=0\). The same argument applies after making the cylinder smaller.

Therefore \(\Sigma_d\) in the actual collar/mapping-cylinder sense need not exist for a general HSS. Equations (51), (56), (57), (69), the holink comparison, and the finite spectral sequence have the independent pro-homotopy proofs above. An equality \(V_d\simeq\Sigma_d\) requires an actual compatible conical deployment, or must define a replacement \(\Sigma_d\) using the full iterated holink diagram. The example uses Quinn's general strata, not manifold strata; no claim is made here that it satisfies an additional manifold-strata hypothesis.


## C1.03 — Proved: an explicit simultaneous-cone diagram

This supplies an explicit completion of the postponed construction, rather than attributing unspecified transition maps to /043. Let \(\Sigma:\operatorname{Drap}(I)^{op}\to\mathrm{Top}\) be the flag diagram of the deployed category, including flags of length zero. For a nonempty flag \(e=\{i_0<\cdots<i_n\}\), write \(e_{\le a}=\{i\in e:i\le a\}\). A pair \((d,e)\) means \(d\subset e\setminus\{\max e\}\); the empty \(d\) is allowed. Put \(a_0<\cdots<a_p=\max e\) for the elements of \(d\cup\{\max e\}\), so \(p=|d|\), not necessarily the length of \(e\).

Define the simultaneous mapping cylinder
\[
 C(d,e)=\operatorname{hocolim}\bigl(
 \Sigma_{e_{\le a_p}}\longrightarrow\cdots\longrightarrow
 \Sigma_{e_{\le a_0}}\bigr),
\]
using the ordinary thick simplicial mapping-cylinder model. Explicitly it is the quotient of
\[
 \coprod_{k=0}^{p}\Sigma_{e_{\le a_k}}\times\Delta^k
\]
that identifies the face omitting the last vertex with its image under
\(\Sigma_{e_{\le a_k}}\to\Sigma_{e_{\le a_{k-1}}}\), and makes the analogous identifications on all nested subfaces. Faces omitting a nonfinal vertex remain boundary faces. In particular \(C(\varnothing,e)=\Sigma_e\); for one cut it is the mapping cylinder of the indicated projection, called a mapping cone in the manuscript's convention.

There are three kinds of maps, generating the transition diagram.

* If \(d\subset d'\subset e\setminus\{\max e\}\), the inclusion of the selected vertices gives \(C(d,e)\to C(d',e)\).
* For \(f=d\cup\{\max e\}\subset e\), the restriction maps
\(\Sigma_{e_{\le a}}\to\Sigma_{f_{\le a}}\) give
\(C(d,e)\to C(f\setminus\{\max f\},f)\).
* For each selected \(a\in d\), the initial-prefix cylinder already present as a face has its canonical map
\(C(d\cap e_{<a},e_{\le a})\to C(d,e)\).
  These maps identify internal prefix blocks with their standalone objects in the diagram.

All relations among these maps are those induced by inclusions of flags and functoriality of \(\Sigma\). This can equivalently be taken as the image diagram with the maps above, imposing every commuting square that follows from the displayed inclusions.

The colimit of this diagram is canonically homeomorphic to the ordinary realization of the strict nerve:
\[
 \operatorname{colim}_{(d,e)}C(d,e)
 \;\cong\;
 \left(\coprod_{\varnothing\ne e\in\operatorname{Drap}(I)}
 \Sigma_e\times\Delta^{|e|-1}\right)/\sim .
\]

**Proof.** A continuous map out of the right-hand quotient is a family of continuous maps \(f_e:\Sigma_e\times\Delta^{|e|-1}\to Y\), compatible with every face restriction. The full block \(C(e\setminus\{\max e\},e)\) contains the final-vertex-deletion faces internally; the third transition family identifies each such prefix face with its standalone prefix block, including iterated final deletions. Its other faces correspond to \(C(d,e)\). The first transition map identifies these as the corresponding faces of the full block; the second imposes precisely the restriction to the selected flag \(d\cup\{\max e\}\). Every face is either final-vertex deletion or contains the final vertex. Thus cocones out of the cone diagram and maps out of the realization are the same, naturally in the target topological space. The quotient topologies agree by this universal property. Empty \(d\) supplies the vertex identifications; flags of one element supply the object spaces. For \(I=\varnothing\), both constructions are empty. Identities can instead be inserted to use the ordinary unital nerve; its degenerate simplices collapse and give the same realization.

**Geometric recovery.** Suppose the finite conical space is supplied with recursive compatible collars in the sense actually used in its construction: cutting a minimal stratum \(A\) gives a space \(X'\), with retained outer boundary \(H\), and
\[
 X=X'\cup_H C(H\to A),
\]
while the same collar systems induce the smaller deployments on \(X'\) and \(H\). Induction is performed simultaneously for spaces with any already retained outer boundary faces. Then the realization is homeomorphic to \(X\), relative to those faces.

For completeness, let \(C\) be the deployed category and \(i\) a minimal label. Let \(D\) be its restriction to the other labels. Define \(M\) by
\(N_nM=\coprod_{j_0<\cdots<j_n}\Sigma_{i,j_0,\ldots,j_n}\).
The face maps make \(M\) the deployment of \(H\). Every strict simplex of \(C\) either lies in \(D\) or has \(i\) as its unique first vertex. Hence its realization has a canonical homeomorphism
\[
 |C|\cong |D|\cup_{|M|} C(|M|\to\Sigma_i).
\]
On a simplex containing \(i\), write its barycentric coordinates as
\(t_i=1-r,\ t_{j_k}=r u_k\). At \(r=0\) all points are identified by the source to \(\Sigma_i\); at \(r=1\) they attach to \(D\) by forgetting \(i\). These formulas and their inverse are compatible with every face, so define continuous inverse maps of the quotient spaces. The induction hypothesis identifies \(|D|,|M|\), and their map with \(X',H\), and its boundary inclusion. The last display becomes the given conical pushout for \(X\). This proves the assertion. Fibrancy is not needed for this topological reconstruction; it is needed in the separate exit-category comparison.

The notation \(p=\operatorname{long}(d')\) in /043 conflicts with the preceding \(2^n\) count and its own marginal description \(d=\{\max d_1,\ldots,\max d_p\}\). The original scan has now been visually checked: the inconsistent notation is genuinely written. The construction above explicitly corrects it to \(p=|d|\). An internal audit also caught that the third transition family is essential: without it, for the constant one-point diagram on \(0<1\), the standalone \(\Sigma_0\) remains an extra isolated point. With it the colimit is the required interval. This correction is part of the construction, not a claim that those transitions were supplied in the manuscript. The attached exact cell-quotient program checks this counterexample: omitting prefix maps gives three vertices and one edge in two components, while all three transition families give two vertices and one edge. For constant diagrams on chains of zero through six vertices it checks the complete simplex face counts. The recorded run took 0.024328412 seconds.

## C5.02 — Refuted in TOP, PL, and smooth: transversality follows from the other bare order conditions

Use \(I=\{0<1<2\}\),
\[
 \Sigma_0=\{*\},\quad
 \Sigma_1=\mathbb R\times[0,\infty),\quad
 \Sigma_2=\mathbb R\times[0,\infty)^2.
\]
Write \((x,t,r)\) on the last space and take
\[
 \Sigma_{01}=\mathbb R\times\{0\},\quad
 \Sigma_{12}=\{r=0\},\quad
 \Sigma_{02}=\{t=0\}.
\]
All targets are face inclusions and \(s_{01},s_{02}\) are constant. Put
\[
 s_{12}(x,t,0)=(xt,t)
\]
for the smooth example. For a PL example replace \(xt\) by
\(f(x,t)=\max(-t,\min(x,t))\), a finite piecewise-linear function.

The incoming faces are closed, properly embedded, and transversely collared. Their intersection is \(\{t=r=0\}=s_{12}^{-1}\Sigma_{01}\), and projection control holds because both maps to \(\Sigma_0\) are constant. Thus the induced relation is a topological order with finite totally ordered lower intervals; every bare algebraic and face condition in the proposed implication holds. The source is not assumed fibrant in the general Scholium or its /062 margin.

Yet \(s_{12}\) is not transverse to the base boundary in the collar-product meaning explicitly used at /025–027 and /031. Its boundary restriction maps the whole \(x\)-axis to \((0,0)\). If a collar-product description existed near that axis, the image of a small collar neighborhood would lie in a one-dimensional collar through that point. In either example the image of every sufficiently small neighborhood of \((0,0)\) contains a nonempty open two-dimensional wedge: in the smooth example \(|u|<\delta t\), and in the PL example \(|u|<t\). A one-dimensional embedded collar cannot contain an open subset of a two-dimensional manifold, by invariance of dimension. Thus the specified collar-product transversality fails even topologically. This terminology must be retained: the smooth map does satisfy ordinary differential transversality to the target boundary, which is a weaker requirement here.

A sufficient extra hypothesis is local triviality of the entire boundary diagram over the base collar, with its trivializations preserving all its faces. Pulling that diagram back along the collar's product coordinate then gives compatible product collars. This is the strong equisingularity qualification in /039; an unspecified use of “fibrant” must not be substituted for it.

Even adding raw proper Hurewicz fibrancy does not imply the smooth product-collar condition. Take
\(\Sigma_0=\{*\}\), \(\Sigma_1=[0,1]\),
\(\Sigma_2=[0,1]^2\),
\(\Sigma_{01}=\{0,1\}\),
\(\Sigma_{12}=[0,1]\times\{0,1\}\), and
\(\Sigma_{02}=\{0,1\}\times[0,1]\).
Let \(s_{12}(u,v)=u^2\) and let the other sources be constant. Every source is proper and Hurewicz: on each component \(u\mapsto u^2\) is a homeomorphism. All target collars, intersections, and projection-control identities hold. But the derivative of \(s_{12}\) in the normal direction at \(u=0\) is zero, invariant under smooth collar changes; a smooth product over that collar has nonzero normal derivative. Thus the smooth source transversality fails. The assertion in the inherited reading that the written fibrancy hypothesis itself supplies local triviality must use its stronger, category-specific bundle interpretation.

## C5.03 — Refuted in TOP: mixed nonsingularity from equisingularity and nonsingularity

Let \(H\) be the Poincare homology three-sphere and \(F=\Sigma H\) its suspension. Then \(F\) is a compact polyhedron which is not a topological manifold: near either suspension vertex the punctured neighborhood is \(H\times(0,\epsilon)\), whose nontrivial fundamental group cannot become that of a punctured four-ball. More precisely the nested punctured cone neighborhoods all induce isomorphisms on that nontrivial group, whereas a four-manifold has a basis of punctured simply-connected ball neighborhoods.

Cannon's double-suspension theorem gives \(\Sigma^2H\cong S^5\). Removing the two outer suspension points gives
\(F\times\mathbb R\cong S^4\times\mathbb R\): the image of those two points can be sent to the north and south poles by a homeomorphism of \(S^5\). Consequently \(E=F\times S^1\) is a closed topological five-manifold, since it is locally \(F\times\mathbb R\).

Take \(\Sigma_0=S^1,\ \Sigma_1=E\times[0,1]\), with incoming face
\(\Sigma_{01}=E\times\{0,1\}=\partial\Sigma_1\), and source projection to \(S^1\). This is a proper locally trivial topological bundle, with fibre \(F\amalg F\). Both object spaces are manifolds and the target is the whole boundary. All triple, order, and transversality conditions are vacuous. The fibre is not a manifold. This disproves the mixed-fibre implication at /051 and /063 even with genuine bundles, not merely homotopy fibrations.

The precise primary statements used here are Cannon \cite[Theorem 1.5, p.833; Corollary 3.6, p.838]{C_Cannon}.

## C5.04 — Refuted in TOP: the /067 face-manifold margin

Use the same compact polyhedron \(F=\Sigma H\) as in C5.03, and put
\[
 \Sigma_0=\{*\},\qquad \Sigma_1=[0,1],\qquad
 \Sigma_2=F\times[0,1]^2.
\]
Let \(\Sigma_{01}=\{0,1\}\),
\(\Sigma_{12}=F\times[0,1]\times\{0,1\}\), and
\(\Sigma_{02}=F\times\{0,1\}\times[0,1]\).
In coordinates \((z,u,v)\), the source \(s_{12}\) is projection to \(u\), and \(s_{01},s_{02}\) are constant to the point.

The square is locally a plane at its interior points and a half-plane at every boundary point, including its vertices. Since \(F\times\mathbb R\) is a five-manifold by C5.03, \(\Sigma_2\) is a compact topological six-manifold with boundary. Its whole boundary is
\(F\times\partial([0,1]^2)\cong F\times S^1\), itself a five-manifold. It is the union of the two specified collective faces. These faces have their evident transverse product collars, and
\[
 \Sigma_{12}\cap\Sigma_{02}
 =F\times\{0,1\}^2=s_{12}^{-1}(\Sigma_{01}).
\]
The source \(s_{12}\) respects the base collars, and projection control holds because the other two source maps are constant. Every object \(\Sigma_i\) is a manifold with boundary. All source maps are now proper Hurewicz fibrations: \(s_{12}\) is a product bundle with compact fibre \(F\amalg F\), and the other targets are points. Thus even adding equisingularity does not repair this TOP face assertion.

Each incoming face is a disjoint union of two copies of \(F\times[0,1]\), which is not a manifold with boundary. At positive interior interval coordinates the space is a five-manifold. At an endpoint its local homology vanishes in all degrees, since the relative local homology of the half-interval factor vanishes. Hence, if the product were a five-manifold with boundary, its intrinsic boundary would be exactly \(F\times\{0,1\}\). The boundary of a manifold with boundary is a manifold, contradicting the proved singularity of \(F\). The full family therefore satisfies the surrounding order, properness, source-fibrancy, target-collar and source-transversality conditions while its incoming faces are not manifolds. This refutes both the /067 margin and the version of /051(d) that tries to deduce manifold flag spaces from c) and the object-manifold part of d).

## Exact status after the independent audits

All five C requests now have proved statements or explicit refutations with their corrected scope; the numbered statements and the exact TOP/PL/smooth matrix are in the generated paper. This is a C contribution only, not a claim that Parts A and B are complete.

| Item | Settled result and exact scope |
|---|---|
| C.1 | Weak §8 does not imply fibrancy. Explicit three-family simultaneous-cone diagram reconstructs the geometric deployment. Full complete-Segal/Exit comparison is proved for recursive proper compatible conical bundles, including the retained-face induction. Stable-graph incidence groupoids retain isotropy; raw nerves require the specified completion. |
| C.2 | Bare a)-c) fail; the primary hexagon is already labelled commutative. The algebraic repair, one-level versus radial-control distinction, and exact smooth iterated-fibration/control-data equivalence are proved. |
| C.3 | Precylindrical alone need not mean manifold. Exact local criterion and face-incidence indexing are proved; ordinary moduli blowup is orbifold with corners, and a fully explicit coarse genus-four counterexample rules out a universal manifold assertion. |
| C.4 | Finite metric HSS suffice for (51),(56),(57),(69), relative holink comparison and actual finite-cover spectral sequence. Actual germ/face comparison uses proper controlled collars; HSS alone need not supply them. The normal-crossings comparison (294) is canonical in the stated homotopy/incidence category. |
| C.5 | Full margin matrix proved/refuted in C5.08. Raw proper Hurewicz fibrancy is insufficient even for PL and smooth maps. Arbitrary connected TOP components fail; open path-connected components, or open proper source maps, give the corrected order theorem. General-category manifold and PL versions are proved separately. |

## Conventions

Spaces are Hausdorff when properness is used. Proper means closed with compact fibres; it agrees with compact-inverse-image properness in the locally compact Hausdorff examples. A local immersion is locally an embedding. A collar of B in M is a homeomorphism B×[0,δ) onto a neighborhood, restricting to the identity on B×0. PL/smooth statements require maps and collars in that category.

The grading poset has its discrete topology when grading the disjoint union of deployed spaces. The Alexandrov topology is used to stratify the reconstructed space. We distinguish Hurewicz fibrations, locally trivial bundles, smooth submersions, and PL bundles. The margin 150/039 itself says that fibrancy is too weak for the intended equisingularity.

## C1.01 — Refuted: §8 conical data imply (1) of 150/039

Let Y=R, E=S¹, M=D². Embed E as ∂M, give it its usual collar, and let p:E→Y be constant with value 0. Form X=M ⨿_E C(p), where

C(p)=(E×[0,1] ⨿ Y)/((e,0)∼p(e)),

and E×1 is identified with ∂M. Thus X is a sphere attached to a line at one point. Set X₀=Y and X₁=X. The open complement of Y is R². The collar supplies exactly the conical neighborhood of 150/023 used inductively at /036. No local triviality of p occurs in those data. The closed family is finite, increasing, exhaustive, and satisfies the required intersection identity.

Its prescribed deployment has Σ₀=R, Σ₁=D², Σ₀₁=S¹, source p, and target the boundary embedding. All embedding, intersection, and triple conditions hold or are vacuous. The source is proper because S¹ is compact. It is not a Hurewicz or Serre fibration: the path α(t)=t in R starts at p(e)=0 but cannot lift through a constant map for t>0.

This does not refute modern conical stratifications. This two-stratum decomposition is not locally conically trivial along Y at 0. It refutes the implication from the weaker §8 data. The margin of /039 explicitly restricts condition (1) to the equisingular case.

**Correct implication.** If the maps Σᵢⱼ→Σᵢ are locally trivial bundles, or fibrations stable under the relevant base changes and composites, every initial-segment map Σ_d′→Σ_d is a fibration. The Segal pullback identity expresses it as a succession of base changes of these source maps. This is an additional hypothesis, not a consequence of arbitrary §8 conical structure.

## C1.02 — Proved: completeness of the nerve under the homotopy-pullback hypothesis

Let C be an internal category in compactly generated spaces, graded by a finite poset I. Suppose C₀=∐ᵢΣᵢ, C₁=∐ᵢ≤ⱼΣᵢⱼ, Σᵢᵢ=Σᵢ consists exactly of identities, and each strict source Σᵢⱼ→Σᵢ is a Hurewicz fibration. The ordinary nerve has Segal maps that are homeomorphisms onto iterated ordinary pullbacks. A pullback along a Hurewicz fibration computes a homotopy pullback. Thus its nerve is a Segal object in the infinity-category of spaces.

The functor to N(I) takes equivalences to identities. Every equivalence therefore lies over i=i. That summand consists only of identities, and all identities are equivalences. Hence C₀→N(C)₁^eq is an equivalence, proving completeness.

If “Segal space” is defined to require Reedy fibrancy, take a Reedy fibrant replacement. The raw nerve need not be Reedy fibrant. For the identity-only category on S¹ it is constant, and its first matching map is S¹→S¹×S¹, the diagonal. A pair of unequal paths starting at the same point cannot lift through this diagonal.

This proves completeness, not the geometric identification with Exit(X). That identification requires a separate comparison; an equivalence of realizations alone does not imply it.

## C2.01 — Refuted: bare a)-c) of 150/065 imply transitivity

The ill-typed bᵢⱼ⁻¹(Σᵢⱼ) is interpreted as sⱼₖ⁻¹(Σᵢⱼ) inside Σⱼₖ. The bare conditions say:

1. bᵢⱼ:Σᵢⱼ→Σⱼ is a closed embedding.
2. Σᵢₖ∩Σⱼₖ is empty for incomparable i,j.
3. Σᵢₖ∩Σⱼₖ=sⱼₖ⁻¹(Σᵢⱼ), for i<j<k.

They do not imply sᵢₖ=sᵢⱼsⱼₖ on the common subset.

**Finite example.** Let I={0<1<2}, every space be {0,1}, every b the identity, s₀₁=s₁₂=id, and s₀₂(z)=1−z. Conditions 1–3 hold; all subsets in condition 3 are the whole set. But (0,0)<(1,0)<(2,0), while no arrow (0,0)→(2,0) exists. The analogous failure occurs at 1. The exact program code_C/check_cote150.py verifies all six arrows and both missing composites.

**Smooth compact proper enhancement.** Let A=S¹ and g:A→A be rotation by π. Take Σ₀=A, Σ₁=A×[0,1], Σ₂=A×[0,1]². Let Σ₀₁=A×{0,1}⊂Σ₁. In coordinates (z,u,v) on Σ₂ put

Σ₁₂=A×[0,1]×{0,1},    Σ₀₂=A×{0,1}×[0,1].

All targets are inclusions. Set s₀₁(z,u)=z, s₁₂(z,u,v)=(z,u), and s₀₂(z,u,v)=g(z). They are proper smooth bundles with fibres two points, two points, and two intervals, respectively. Opposite faces are transverse; their intersection A×{0,1}² is exactly s₁₂⁻¹(Σ₀₁). Every boundary component is accounted for. The maps respect base collars: s₁₂ is a product projection and Σ₀ has no boundary. Thus d)-e), properness, equisingularity, and the nonsingular condition do not repair the omission. At every corner s₀₁s₁₂(z,u,v)=z but s₀₂(z,u,v)=g(z).

**Precision about the manuscript.** It does explicitly call (41) a “diagramme commutatif hexagonal.” Its left commutativity is the needed equation. The false inference is “donc” from the bare conditions; if commutativity of (41) is included as an axiom it is already written on the page. The inherited SA10-K150e-02 should be qualified accordingly.

## C2.02 — Proved: the exact algebraic repair

Add to 1–3 the identity

sᵢₖ|Σᵢⱼₖ=sᵢⱼ∘(sⱼₖ|Σᵢⱼₖ).

The restriction on the right has target Σᵢⱼ by condition 3. For x∈Σᵢ,y∈Σⱼ define x<y iff i<j, y∈Σᵢⱼ, and x=sᵢⱼ(y). Irreflexivity follows from strict labels. If x<y<z, with i<j<k, then z∈Σⱼₖ and sⱼₖ(z)=y∈Σᵢⱼ. Condition 3 puts z in Σᵢⱼₖ; the new identity gives sᵢₖ(z)=x. Hence the relation is transitive.

At most one predecessor of a point has a given label, since bᵢₖ is an embedding. Two predecessor labels must be comparable by condition 2. If i<j, condition 3 and projection control order the corresponding predecessors. Thus every lower interval is totally ordered and its order is induced by I.

Conversely, suppose this relation is transitive and each lower interval has the order induced by I. For z∈Σᵢₖ∩Σⱼₖ with i<j, its predecessor of label i must precede its predecessor of label j, giving the new identity. Transitivity gives the reverse inclusion in condition 3. Thus the subset identity and the projection identity are exactly the needed algebraic facts. Longer compositions are associative because an ordered category has at most one arrow between two fixed objects.

## C2.03 — Proved: one level does not recover rho-control

In a positive-radius tubular chart write coordinates (r,y), where r>0 is a lower radial function and y≥0 is normal to an intermediate stratum. The controlled retraction is π(r,y)=(r,0). Fix \(\epsilon>0\) and choose explicitly \(h(y)=-y/(4(1+y))\), so \(-1/4<h(y)\le0\), with equality only at \(y=0\). Set

π′(r,y)=(r+(r−ε)h(y),0).

It is a retraction. The new radial coordinate is positive because \(r(1+h(y))-\epsilon h(y)>0\) for \(r>0\). Its derivative in \(r\) is \(1+h(y)>3/4\), so \((\pi\prime,y)\) is a diffeomorphism onto a variable-width neighbourhood of the base and is still a tubular coordinate map after shrinking. Both maps agree on r=ε and have the same inverse image of that level, because

r+(r−ε)h(y)−ε=(r−ε)(1+h(y)).

But rπ′ is not r off that level. Hence a level-set incidence condition is strictly weaker than rho-control. If one fixed map preserves every small level, the full equation follows by choosing ε equal to the radial value of each point. Coherent radial collars or all levels are required to recover the functional equation from deployment data.

## C2.04 — Refuted: the completed bare recapitulation is equivalent to Thom–Mather data

Take one label and Σ₀ a Cantor set. Every a)-e) and projection-control condition is vacuous. A Thom–Mather stratum must be a manifold; a Cantor set is not. Thus the bare completed recapitulation is not such an equivalence. The established comparison concerns suitably smooth manifolds with corners, compatible iterated boundary fibrations, and radial collar information, not arbitrary spaces and one isolated level. Even adding compact manifold object and arrow spaces and proper Hurewicz source fibrations is insufficient: the two-stratum examples C5.06 satisfy the triple and projection conditions vacuously and have nonmanifold fibres. Thus the regular source-bundle hypotheses in C2.05 have mathematical content.


## C3.01 — Refuted: precylindrical means manifold with corners without manifold hypotheses

The definition 150/028 asks for collared predecessor embeddings, transverse collars, and Boolean intervals. It does not require strata to be manifolds. Let K be the middle-thirds Cantor set, M=K×[0,∞), X₀=K×{0}, and X₁=M. The interval {0<1} is Boolean. The required collar is the identity K×[0,δ)→M. The family is finite and satisfies (14). Thus it is precylindrical.

No point has a locally connected neighborhood, because arbitrarily small clopen separations in K persist in the product. Every Euclidean orthant is locally connected. Thus M is not a manifold with corners.

**Exact local correction.** A finite precylindrical structure is a manifold-with-corners structure precisely when the transverse bases of its local collar products are manifolds of the required dimensions. A local product B×[0,δ)^k becomes an orthant chart if B≅R^d locally. Conversely an orthant chart preserving the specified faces restricts to a manifold chart on their full intersection. The requirement to preserve the specified faces matters: TOP has exotic collared factors of ambient manifolds.

For conically smooth finite-depth spaces with manifold strata, AFT \cite[Theorem 7.3.8]{C_AFT} gives the full unzip as a smooth manifold with corners. The local step replaces R^d×C(L) by R^d×[0,∞)×L; induction resolves L. This supplies the corrected theorem in that exact category, not for arbitrary §8 spaces.

## C3.02 — Proved: the face intervals of flags are Boolean

For a maximal label i, deployed faces are Σ_d for flags d ending at i, with the reverse-inclusion order. For e⊂d with the same last entry, an intermediate flag is exactly e∪A for A⊂\(d\setminus e\). Every such subset is a flag. Hence the interval [d,e] is the Boolean lattice of subsets of \(d\setminus e\) (with orientation adjusted to the chosen ordering convention). Transverse collars supply one independent normal coordinate for each added flag entry.

The finite program checks every naturally labelled poset of size at most five: counts 1,1,2,7,40,357 for sizes 0,…,5, comprising 4,135 flags and 10,603 intervals. The argument above proves the assertion in all finite sizes; these counts only check the implementation of the combinatorial description.

For a stratum with several local branches, a global label does not identify a branch. The face index must retain the local incidence or boundary germ. For a normal crossings divisor with k local branches, faces are locally indexed by subsets of those branches. Monodromy and automorphisms may permute them, so the global description is an incidence category or an orbifold groupoid. An orbit-poset loses that action.

## C3.03 — Refuted: fixed contractions alone turn every moduli blow-up into a manifold

This is a counterexample on the coarse space as well as an orbifold qualification. Let C be the smooth projective completion of

y²=x(x−1)(x−3)(x−7)(x−12)(x−20)(x−31)(x−45)(x−64).

There are nine distinct finite branch points and infinity, so Riemann–Hurwitz gives genus 4. The exact program checks all 10·9·8=720 Möbius maps specified by the images of (∞,0,1). Only the identity preserves the whole branch set. This is exhaustive even over C: the unique map carrying three rational projective points to three rational projective points is defined over Q. The hyperelliptic quotient is unique here: two distinct degree-two maps to \(\mathbb P^1\) would give a birational image of bidegree \((2,2)\) in \(\mathbb P^1\times\mathbb P^1\), whose arithmetic genus is one. If their joint map instead had degree two, the image would have bidegree \((1,1)\), making the maps equivalent. Both alternatives exclude distinct degree-two quotients for this genus-four curve. Every automorphism consequently descends to that quotient, with its two-element deck group as kernel. Thus Aut(C)={1,ι}, ι(x,y)=(x,−y).

A neighborhood of [C] in M₄ is a finite quotient of the smooth universal deformation germ, with tangent H¹(C,T_C). A finite holomorphic action is linearizable: average the initial coordinate map \(z\) as \(|G|^{-1}\sum_{g\in G}(dg_0)^{-1}z\circ g\). The average is equivariant, with identity derivative, so it is a coordinate map. Serre duality identifies the dual tangent representation with H⁰(C,2K_C).

An invariant basis is x^k(dx/y)² for 0≤k≤6, and an anti-invariant basis is x^k dx²/y for 0≤k≤1. At a finite branch point use x−a=t²,y=t·unit, so regularity is immediate. At infinity x=t⁻²,y=t⁻⁹·unit; the two displayed differentials have orders 12−2k and 3−2k, respectively. The bounds are exactly those making the orders nonnegative. Independence is clear in the function field, and 7+2=9=3g−3, so the forms span. The quotient germ is consequently

C⁷×(C²/{±1}).

The second factor is the cone on RP³. The product link is S¹³*RP³≅Σ¹⁴RP³. The integral cellular complex of RP³ has d₂=2,d₁=d₃=0; hence H₁(RP³;Z)=Z/2. Local homology at the quotient origin therefore has Z/2 in degree 16, besides its top Z in degree 18. That is impossible for a topological manifold. This point lies in the interior, so blowing up the Deligne–Mumford boundary leaves the local obstruction untouched. Indexing contractions cannot remove it.

**Correct moduli statement.** A universal deformation chart B of a stable marked curve has normal crossing boundary, with branches indexed by the actual nodes e. Replacing q_e by r_e exp(iθ_e) gives a manifold-with-corners chart, acted on by the finite automorphism group. These charts define an orbifold with corners. On an actual torsion-free level cover they define a manifold with corners. Fixed contractions record the subsets of nodes that remain unsmoothed, not a removal of isotropy.

The precise source is Looijenga \cite[Theorems 8.11 and 9.13; Proposition 9.16]{C_Looijenga}: deformation tangent, stable charts, and orbifold real oriented blow-up, respectively.

## C5.01 — Proved: the component-index theorem without a dimension assumption

Let P be a Hausdorff locally path-connected topological poset, with closed order R⊂P×P and projections s,b:R→P. Assume b is a proper local immersion and s a proper Hurewicz fibration. The diagonal is clopen in R: it is closed by Hausdorffness and open by local injectivity of b at identities. Then distinct comparable points belong to different path components; the induced relation on π₀(P) is a partial order. If every lower interval is totally ordered, the target map on arrows between any two fixed components is a closed embedding.

**Proof.** Fibres of b are discrete and compact, hence finite. Put N(y)=|b⁻¹(y)|, including the identity. This is locally bounded. Choose neighborhoods U₁,…,U_N of the points over y on which b is injective. The image of the closed complement of their union is closed and avoids y. In its open complement W every fibre has at most N points.

For fixed x the upper interval P_≥x=b(s⁻¹(x)) is compact. A finite subcover of the preceding neighborhoods bounds N on it. Suppose x<y lie in one path component C. Lift through s any path from x to another point of C, starting at the arrow x<y. Its target remains in C, and its arrow remains strict because identities form a clopen subset. Hence every point of C has a strict successor in C. Construct arbitrarily long chains x=x₀<x₁<…<x_n. Their endpoints lie in P_≥x by transitivity but have N(x_n)≥n+1, a contradiction.

For component arrows C→D and D→E, lift a path in D from the source of the second to the target of the first, giving composable representatives. Thus the component relation is transitive. If C≤D≤C, the resulting composite lies within C, so its endpoints coincide; antisymmetry in P then identifies the middle point as well, proving C=D.

Finally, two arrows from C to one target z have sources in the totally ordered lower interval of z. The sources are comparable and in one component, hence coincide. Thinness then identifies the arrows. The restricted target map is proper, because components are clopen, and a proper injective map to a Hausdorff space is a closed embedding. This proves all assertions.

This repairs the ordered-space application of 150/070–071 without the questionable “rare subset lowers dimension” step on /069. It does not prove the same statement for an arbitrary category with nontrivial idempotents; the order hypothesis is used in forming arbitrarily long strict chains.

## Opened sources and useful exact locators

1. Ayala–Francis–Tanaka, arXiv:1409.0501v6. TeX downloaded and opened; Theorem 7.3.8 (full unzip), Proposition 7.3.10 (proper constructible blow-up square), Proposition 8.2.5 (tubes). Author PDF opened: https://math.montana.edu/dayala/documents/AFT1.pdf .
2. Mather, Notes on topological stability (July 1970), §7 p.15 (both control identities), §§8–10 (abstract pre-stratified sets, controlled vector fields, isotopy). https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf .
3. Marco Volpe, Verdier duality on conically smooth stratified spaces, arXiv:2206.02728v2; PDF and TeX opened. Lemma 2.13 (exit pushout of a fibrewise cone of a proper conically smooth bundle), Corollary 2.17 (tubular open-cover exit pushout). https://arxiv.org/pdf/2206.02728 .
4. Ayala–Francis–Rozenblyum, A stratified homotopy hypothesis, arXiv:1502.01713; PDF and TeX downloaded and partly opened. No unextracted theorem is used as an established deployed-nerve comparison.
5. Looijenga, Moduli spaces of Riemann surfaces at Tsinghua, §§8–9, Theorems 8.11 and 9.13, Proposition 9.16. https://webspace.science.uu.nl/~looij101/tsinghua.pdf .

The full fetched copyrighted PDFs and sources are not to be put in the delivered ZIP. Preserve this locator manifest and our own proofs.

## Search record

Queries: Ayala Francis Tanaka local structures unzipping resolution manifold corners; Mather Notes on topological stability control data; exit unzip complete Segal; stratified homotopy hypothesis blow-up Exit; homotopy link evaluation homotopy equivalence Quinn; Verdier duality conically smooth stratified spaces; moduli curves local quotient H1 tangent hyperelliptic; real oriented blowup Deligne Mumford orbifold corners; hyperelliptic locus normal space g−2 involution. These found the sources above. No assertion of novelty is made.

## Computations

code_C/check_cote150.py and check_cote150.output.json are the full exact finite certificate. First recorded run: total 0.854292 seconds; 720 Möbius transformations 0.724255 s; 10,603 flag intervals 0.129894 s; twist and cellular homology negligible. The computations verify finite parts of the arguments, not the deformation-theory theorem.



## C5.07 — Refuted in arbitrary finite-dimensional TOP: connected-component strictness

The word "connected" in /068–071 cannot be replaced silently by "path-connected." Even all the stated finiteness, properness, local-immersion, and collared-target conditions permit a strict arrow within one connected component. The following example also satisfies the stronger bordant-target condition of /063, not just the nowhere-dense condition of /069.

Let \(K\subset\mathbb R^2\) be a compact, nondegenerate hereditarily indecomposable continuum, for example the plane pseudoarc constructed by R. H. Bing, *Concerning hereditarily indecomposable continua*, Example 1, printed pp.43--44 \cite{C_Bing1951}. Every path in \(K\) is constant. Indeed, a nonconstant path has a nondegenerate image continuum. Uniform continuity partitions its domain into finitely many consecutive intervals whose image continua all have diameter smaller than that whole image. The image would then be a finite union of proper continua with connected successive unions. Indecomposability rules this out, by induction on the number of pieces.

Choose a continuous map \(q:[1,\infty)\to\mathbb R^2\) whose cluster set at infinity is exactly \(K\), with \(\operatorname{dist}(q(t),K)\to0\). Here is an explicit existence construction. Fix a point of \(K\). For each positive integer \(n\), choose a finite \(1/n\)-net in \(K\). Its open \(1/n\)-neighbourhood in the plane is connected and hence path-connected. On \([n,n+1]\), let \(q\) traverse a piecewise linear loop, based at the fixed point, which visits every point of that net and stays in that neighbourhood. Concatenation is continuous. These visits show that every point of \(K\) is a cluster point; the neighbourhood bound excludes any other cluster point.

Set
\[
 C=\{(q(t),1/t):t\ge1\}\subset\mathbb R^3,
 \qquad P=C\cup(K\times\{0\}).
\]
The height coordinate identifies \(C\) with the ray \([1,\infty)\). The space \(P\) is its compact closure, hence is a connected compact metric space of finite covering dimension at most three. The dimension bound can be checked directly: for any finite open cover of this compact subset of \(\mathbb R^3\), choose a sufficiently fine triangulation of \(\mathbb R^3\). Its vertex open-star cover restricts to a refinement on \(P\), by the Lebesgue number of the given cover; each point lies in at most four such stars, the vertices of its carrier simplex. This is the defining covering-dimension bound. Its single connected component is open. Write \(b=(q(1),1)\); its neighbourhood with height greater than \(1/(1+\epsilon)\) is a collar \([0,\epsilon)\) of the point \(b\). Choose \(a\in K\times\{0\}\).

The path component of \(a\) in \(P\) is the singleton \(\{a\}\). To verify this, suppose a path starting in the remainder enters \(C\). An interval component of the inverse image of \(C\) has a finite left endpoint at which the height is zero. On that interval the corresponding ray parameter tends to infinity at its left endpoint. By the intermediate value theorem, the image of every sufficiently short interval after that endpoint contains an entire tail \([T,\infty)\) of ray parameters. Continuity of the path would therefore force the whole tail of \(q\) to converge to the same remainder point. This contradicts its nondegenerate cluster set \(K\). A path remaining in the remainder is constant by the preceding indecomposability argument.

Give \(P\) the order with relation
\[
 R=\Delta_P\cup\{(a,b)\}\subset P\times P.
\]
This is a closed partial order. Its strict relation consists of one point, which is a clopen component of \(R\); the other component is \(\Delta_P\cong P\). Every lower interval is totally ordered and has at most two elements. Both projections \(s,b:R\to P\) are proper because the domain is compact. The target projection is a local embedding: it is the identity on the diagonal component and the embedding of a point on the strict component. The strict target image \(\{b\}\) is nowhere dense and collared. Thus its family of incoming boundary germs is transverse; there is at most one such germ at any point.

The source projection is a Hurewicz fibration, including its full lifting property for arbitrary parameter spaces. Given a map \(g:Z\to R\) and a homotopy \(H:Z\times[0,1]\to P\) with \(H(z,0)=s(g(z))\), let \(Z_e\) be the inverse image of the isolated strict arrow. This is clopen in \(Z\). On \(Z_e\), each path \(H(z,-)\) starts at \(a\), so it is constant; lift it constantly to the strict arrow. On \(Z\setminus Z_e\), lift by \((H(z,t),H(z,t))\in\Delta_P\). These continuous lifts agree with the initial map and glue across the clopen partition. Source transversality to the target collar is also satisfied: on the identity component it is the identity, while the strict component maps to \(a\), outside a chosen collar of \(b\).

Nevertheless \(a<b\) lie in the same connected component of \(P\). The map to the one-point set of connected components is not strictly increasing. This refutes the unrestricted TOP conclusion of /070 and therefore the equivalence claimed in /071 in that scope. The additional monomorphism condition for distinct components is vacuous here and cannot repair it. No doubtful transcription is used: the original /070–071 explicitly says connected components, as does the open-component assumption on /068.

The exact correction proved in C5.01 is to use open, path-connected components; in particular it applies to manifolds and locally path-connected PL spaces. Another sufficient correction, which can use connected components without local path-connectedness, is to require the proper source map to be open. Here is the additional proof. Suppose a strict arrow has source and target in the same open connected component \(D\). The strict arrows whose targets lie in \(D\) form a clopen subspace of \(R\). Their source image is open by openness of \(s\), and closed by properness; it meets \(D\), so it contains all of \(D\). Thus every point of \(D\) has a strict successor in \(D\). Starting at one point gives arbitrarily long strict chains in its compact upper interval. Proper local injectivity of the target projection makes the cardinalities of lower intervals locally bounded, hence bounded on that compact upper interval, a contradiction. The same open-and-closed image argument aligns middle objects to prove transitivity of the component relation. Cycles would give a strict chain returning to a component and then the same contradiction. Total ordering of the pointwise lower intervals gives the proper-injective target comparison of C5.01. A locally trivial source bundle is open, so this correction applies to the strong equisingular interpretation too.

## C1.04 — Proved under the corrected geometric hypotheses: incidence groupoids and moduli

Here are the construction and the category in which the moduli version holds. For finite-depth smooth Thom–Mather data, perform the successive cuts in a linear order in which every lower stratum is cut before the strata above it, retaining every new boundary. At the stage of label \(i\), the cut-open closure of its stratum is \(\Sigma_i\). The face of \(\Sigma_j\) over an incidence \(i<j\) is \(\Sigma_{ij}\), and its source is the retained link-bundle projection to \(\Sigma_i\). A longer flag \(d=(i_0<\cdots<i_n)\) defines
\[
 \Sigma_d=\Sigma_{i_0i_n}\cap\cdots\cap\Sigma_{i_{n-1}i_n}.
\]
Removing a nonfinal entry gives the inclusion of intersections. Removing a final entry gives the appropriate source projection restricted to that intersection. Projection control identifies all composites with the same source and target, so these maps define the contravariant flag functor. The inverse-image identities make its Segal squares cartesian. Proper stratified link bundles and their base changes prove the initial-segment fibrancy; the incoming target faces have their specified commuting collars. The empty-index case gives the empty space and the empty category. A one-stratum deployment is its fundamental infinity-groupoid.

The hypotheses needed in C1.B3 hold for this construction: a cut or an intersection of faces retains the same iterated boundary fibrations, their proper source bundles, and the restrictions of the commuting collars. C2.05 derives this closure property from the iterated-fibration resolution theorem. In the conically smooth formulation it is supplied by AFT, *Local structures on stratified spaces*, Theorem 7.3.8 (full unzip), Proposition 7.3.10 (the blow-up square), and Proposition 8.2.5 (the tubular presentation) \cite{C_AFT}. Thus C1.B3 identifies the resulting complete Segal object with the full exit category in that class. C1.01 explains why the weaker literal mapping-cone data in §8 do not imply this result without equisingularity.

For \(\overline{\mathcal M}_{g,n}\), use the following finite incidence category, retaining automorphisms. Its objects are stable graphs \(\Gamma\) of type \((g,n)\), with labelled legs, vertex genera, and stability at every vertex. An arrow is a specified edge contraction \(c:\Gamma\to\Gamma'\), together with its identification of the contracted graph with \(\Gamma'\); graph isomorphisms are arrows as well. Composition contracts the union of the specified edge sets. Contracting a loop raises the genus of its vertex; contracting an edge joining two vertices merges them and adds their genera. The open stratum is the orbifold
\[
 \mathcal S_\Gamma=
 \left[\prod_{v\in V(\Gamma)}\mathcal M_{g(v),n(v)}
          \big/\operatorname{Aut}(\Gamma)\right].
\]
Equivalently one may keep half-edge labels throughout and then form the indicated finite groupoids. Fixed contractions preserve which node branches are involved; an orbit-poset does not.

Use the cutting construction in smooth universal deformation charts. Looijenga's Theorem 9.13 \cite{C_Looijenga} supplies the chart and its finite automorphism action; its boundary parameters \(q_e\) are indexed by the actual nodes. The ordinary real oriented blow-up writes \(q_e=r_e\exp(i\theta_e)\). To obtain the full deployment with a boundary hypersurface for every strict stratum incidence, further blow up its corner faces successively in increasing dimension. Locally this replaces the face lattice by its flag lattice. In a normal coordinate space with \(r\) nodes, the outgoing link before resolution is the coordinate-stratified sphere \(S^{2r-1}\); the source fibre of the full deployment is its recursively resolved link. For \(r=1\) this is a circle. For \(r>1\), radial-ratio coordinates and their faces are also retained, so identifying this full link with only \((S^1)^r\) would discard data. The ordinary oriented blow-up and the full flag deployment are related by these explicit further corner blow-ups.

For a composable chain of specified contractions, take the corresponding flag-face space in these charts and its groupoid of chart identifications and graph automorphisms. Denote the resulting orbifold by \(\boldsymbol\Sigma_d\). Face and source maps are the preceding geometric maps with their equivariant identifications. In simplicial degree \(k\), take the disjoint union over contraction chains of length \(k\), modulo their isomorphism groupoids. Thus fibre products are homotopy fibre products of groupoids/spaces, not orbit-set fibre products. Local transverse product collars and proper link bundles show the Segal comparisons are equivalences. The maps glue because changes of deformation chart preserve the labelled normal-crossings incidences and their resolved boundary fibrations. The source and target maps therefore define a Segal object in orbifold homotopy types.

There are two equivalent descriptions of its completion. In the classifying-space construction take the classifying space of the entire groupoid of chains in every degree, with isomorphisms at every vertex and commuting identifications on each arrow. Replacing only the object set by classifying spaces, while leaving the raw arrow sets unchanged, would not suffice. For example, for one object with automorphism group \(G\), the groupoid of length-\(k\) strings is
\[
 G^k\mathbin{/\mkern-6mu/}G^{k+1}.
\]
The action changes the trivializations at each vertex. It is transitive with stabilizer a diagonal copy of \(G\), so its classifying space is \(BG\) in every degree. The degree-zero degeneracy to the equivalence subspace in degree one is therefore an equivalence. This is the Rezk classifying-diagram construction. Applied to the entire incidence diagram, with homotopy fibre products for compositions, it gives a complete-Segal model. Equivalently take the Rezk completion of the raw incidence/action-category nerve. A raw group nerve with one discrete object is not already complete when its automorphism group is nontrivial, and discarding that group is not completion.

Choose the compatible boundary fibrations and collar data once on the orbifold resolution, and pull them back to each atlas chart. These data can be constructed equivariantly: normal-crossings blow-ups preserve incidence labels, invariant metrics and connections exist by finite-group averaging and orbifold partitions of unity, and the iterated collar construction proceeds on the preserved boundary fibrations. A change of chart consequently preserves the pulled-back structures. Independent arbitrary collar choices are not being asserted to agree. The chartwise source maps are representable proper locally trivial bundles, so their pullbacks compute the needed homotopy fibre products after passage to atlas chain groupoids.

Define the orbifold exit category by descent from an orbifold atlas: take the colimit in infinity-categories of the exit categories of its simplicial atlas and its chart identifications. On a finite quotient chart \([U/G]\), this is \(\operatorname{Exit}(U)\mathbin{/\mkern-6mu/}G\). The atlas definition is independent of the atlas. For a surjective stratum-preserving local diffeomorphism \(V\to U\), cover \(U\) by opens admitting stratum-preserving local sections. A section supplies an extra degeneracy in the augmented Čech diagram, making its image under the exit functor a split augmented simplicial diagram. Its colimit is the exit category of that open. Exit open-cover excision \cite[Theorem A.7.1]{LurieHA} and interchange of colimits globalize the equivalence to \(U\). Two atlases have a common refinement given by their fibre product; applying the preceding argument in both directions of its bisimplicial atlas identifies the two colimits. For \([U/G]\), the atlas nerve is \(U\times G^\bullet\), giving precisely the homotopy-orbit category just displayed, including ineffective isotropy.

The comparison of C1.B3 is natural for the face maps, source maps, and isomorphisms. It is consequently an equivariant equivalence on every deformation chart and on every atlas intersection. Taking the displayed colimit gives
\[
 \widehat{N\boldsymbol\Sigma}\simeq
 \operatorname{Exit}_{\mathrm{orb}}(\overline{\mathcal M}_{g,n}),
\]
where the hat denotes complete-Segal localization. The proof is categorical descent of chartwise equivalences; equality of classifying-space realizations alone is not used. Realization gives the homotopy type of the orbifold, with its finite isotropy. On a level cover on which all stabilizers act freely, the same construction gives the ordinary space and its ordinary exit category.

For coarse moduli spaces, finite orbit quotients commute with the explicit topological colimits of C1.03, so their cone realization still recovers the coarse space. However quotienting can destroy source fibrancy and can make the stated strata nonmanifolds; C3.03 gives a concrete interior obstruction in genus four. Thus the orbifold exit comparison cannot simply be transferred to the boundary-only coarse stratification. One may instead refine its strata by the isotropy/quotient singularity type and apply the ordinary conical theorem to that refined structure. Fixed contractions alone do not perform that refinement.

For the basic case \(\overline{\mathcal M}_{0,4}\cong\mathbb P^1\), the ordinary space has three point strata. Its open object is a sphere with three open discs removed, its point objects are those three points, and its three arrow spaces are the three boundary circles. The source on each circle maps to its point object; the target is the corresponding boundary embedding. Gluing the three mapping cylinders fills the three holes by discs, giving \(S^2\). Thus the cut-open convention does satisfy the presentation in this case; taking the open stratum or a boundary circle as its point object would be a different datum. This verifies the specific inherited \((0,4)\) comparison independently.

Empty labels may be deleted, and disconnected strata may be kept as disjoint unions. A grading need not be injective on components: a strictly increasing grading can merge incomparable components, but their actual incidences and disjoint incoming branches must remain in the diagram. The orbifold formulation allows ineffective actions as well. A stabilizer that acts trivially on a deformation chart still contributes its classifying space; quotienting by its kernel would change the stack and its exit category. In particular the vertex moduli factors retain their own automorphisms in addition to graph automorphisms. No divisibility or dense-order assumption on the indexing order is made or needed.

Finally this is a homotopy and exit-category presentation, not the missing topos gluing theorem of A.1. The successive cylinders retain the entire face-incidence diagram and its coherence. The manuscript's pair/triple stones omit actual iterated neighbourhood intersections, as the counterexample of A.1 shows. Taking all complete flag-intersection pro-topoi and their Čech descent maps gives the topos reconstruction there; taking only the homotopy types or only the global stratum-poset forgets information needed for arbitrary sheaves. These are different functors applied to the geometric descent diagram, and their colimit claims have been proved in their respective categories.

## C5.08 — Proved and refuted: the complete margin matrix and the category digression

For the matrix below, **raw fibrancy** means a proper Hurewicz fibration, even when its underlying map happens to be PL or smooth. A **regular PL source** is a locally trivial PL bundle; a **regular smooth source system** has proper submersions on every source and compatible horizontal product collars, together with full projection control; C5.05 proves the necessary regularity on all vertical faces. A transversality assertion refers to the manuscript's product-collar condition, not merely to equality of inverse-image subsets. These distinctions are necessary to evaluate R7.

| Manuscript margin | TOP | PL | Smooth |
|---|---|---|---|
| /051(d): incoming flag faces are manifolds from the ambient object-manifold condition | False: C5.04 | True for PL collars: C5.05 | True for smooth collars: C5.05 |
| /051(e) and /063: mixed fibre-manifold and fibre-boundary condition follows from nonsingularity and raw fibrancy | False even for locally trivial TOP bundles: C5.03 | False: the proper PL Hurewicz example C5.06 | False: the proper smooth Hurewicz example C5.06 |
| Same mixed implication with regular PL/smooth source | A TOP bundle still does not suffice | True: C5.05 | True: C5.05 |
| /062: source transversality follows from the other bare order/face axioms | False: C5.02 | False: C5.02 | False: C5.02 |
| /062 with local product triviality of the full face diagram | True by the product charts | True by the product charts | True by the product charts |
| /067: incoming faces and their stated boundaries are manifolds from object nonsingularity | False: C5.04 | True: C5.05 | True: C5.05 |
| /070–071 for ordered spaces with open path-connected components | True: C5.01 | True: C5.01 | True: C5.01 |
| /070–071 for arbitrary open finite-dimensional connected TOP components | False even with collared strict target: C5.07 | Locally finite PL spaces are locally path-connected, so C5.01 applies | Manifolds are locally path-connected, so C5.01 applies |

The proposed boundary formulas in the positive rows are part of C5.05, not extra assumptions about the answer: horizontal faces are the inverse images of lower faces of the base, and vertical faces are exactly those inserting an intermediate label. Their union is the boundary of the arrow/flag space; only the vertical part is the intrinsic boundary of the source fibre. Empty fibres cause no exception. These arguments are local in every dimension, including zero, one, and two. The counterexamples in larger dimensions refute the unrestricted claims without purporting to be minimal-dimensional ones.

The general categorical paragraph /067–070 can also be settled for manifold object components, without assuming the category is thin. Let a topological category have Hausdorff object and arrow spaces, open manifold components of its object space, proper locally embedding target map \(b\), Hurewicz source map \(s\), and locally nowhere-dense target image of the strict arrows. Assume every invertible arrow is an identity. Then the induced relation on object components is a partial order, and every nonidentity arrow connects distinct components.

Here is a full proof which avoids the manuscript's dimension inequalities. The identity section is closed by Hausdorffness and open by local injectivity of \(b\): near an identity, both that section and a sufficiently small arrow neighbourhood lie in a target-injective chart, so the only arrow in that chart with a given nearby target is its identity. Hence strict arrows form a clopen subspace. Source lifting along a path cannot change from a strict arrow to an identity, and target continuity keeps its target in one component. It follows that the existence of an arrow from one component to another is independent of which source point in the first component is prescribed. This also proves transitivity by lifting the second arrow along a path joining the intermediate endpoints.

Suppose a strict arrow has source and target in the same connected \(n\)-manifold component \(D\), allowing boundary or corners. Move its source by path lifting into the interior of \(D\); connected manifold components are path-connected and have nonempty interior, with the dimension-zero case interpreted directly. The target remains in \(D\). Restrict to strict arrows whose source and target lie in \(D\). Over a sufficiently small open coordinate ball \(U\subset D\), a contraction of \(U\) to a point and the Hurewicz lifting property give a continuous section \(\sigma:U\to R^{<}\) of \(s\). Starting from a constant arrow lift proves this for arbitrary parameter space \(U\); the lift stays strict and its target stays in \(D\). Shrink \(U\) around a point so that \(\sigma(U)\) is contained in one target-injective neighbourhood. Then \(b\sigma:U\to D\) is injective, because \(\sigma\) is a section and \(b\) is injective on that neighbourhood. Choose a target corner chart and include its orthant in \(\mathbb R^n\). Invariance of domain makes the image of \(b\sigma\) open in \(\mathbb R^n\); it cannot meet the boundary of that orthant, and hence is open in \(D\). This contradicts the locally nowhere-dense strict target image. Thus no strict arrow has both endpoints in one component. This argument includes dimension zero directly: a nonempty image in a discrete component is open.

If there are arrows from \(D\) to \(E\) and back, path lifting aligns their middle endpoints. Write the resulting arrows as \(u:d\to e\) and \(v:e\to d'\), with \(d,d'\in D\). The composite \(vu\) must be an identity by the preceding paragraph, so \(d'=d\). The composite \(uv\), with endpoints in \(E\), must likewise be an identity. Thus \(u\) and \(v\) are inverse; the assumption on invertible arrows forces \(D=E\). This proves antisymmetry. If the category is an ordered space with totally ordered lower intervals, the extra componentwise monomorphism statement and incomparable-face disjointness follow exactly as in C5.01; no extra monomorphism axiom is needed.

The same categorical proof applies to finite-dimensional locally finite PL object spaces, even if they are polyhedra rather than manifolds, provided the arrow charts are PL and the target map is a PL local embedding. These are the category-specific assumptions used in the PL-image argument below. For an alleged strict arrow within a component of maximal dimension \(n\), use source path lifting to move its source into the interior of a maximal \(n\)-simplex; this is an open \(n\)-ball. A local source section embeds that ball into a target-injective strict arrow chart. The locally rare PL target image contains no \(n\)-simplex and has local dimension at most \(n-1\). For completeness this cannot contain an embedded \(n\)-ball: a compact sub-ball meets only finitely many target simplices; the closed preimages of these simplices cover it, so one has interior by the Baire theorem. That gives an injective map from an open \(n\)-ball into a Euclidean space of dimension at most \(n-1\), contradicting invariance of domain after inclusion into \(\mathbb R^n\). The remaining component-order argument is unchanged. The TOP counterexample C5.07 explains why arbitrary connected finite-dimensional components do not admit this argument.

**Doubtful and ill-typed readings.** The original /051, /062, /063, /067, /070, and /071 scans have been opened visually \cite{C_Grothendieck150}. In /063(d) the transcription flags the source letter as \(s\) or \(b\); the source reading is the one explicitly typed as \(p_1\) in the preceding cartesian square on /062 and used in /065–066. All nontrivial statements above use that reading. If one literally requires the target boundary embedding \(b\) to be product-collar transverse to itself, a nonempty strict arrow chart is impossible: its inverse image of that boundary is its whole domain, which cannot itself be a nonempty collared boundary subset of that domain. Under that alternative the strict relation is empty and the nonsingular object's boundary is empty, so the corresponding mixed assertions are vacuous. The uncertain indices in /067's displayed source are typed as \(s_{jk}:\Sigma_{jk}\to\Sigma_j\); every other reading with a different source label must be reindexed to this type or is not a composable map. The uncertainty in /051(d) between deducing and separately requiring manifold flag spaces does not affect the mixed counterexamples: their arrow spaces are themselves manifolds. Finally the dimension and connected-component wording on /070–071 is clear in the original; C5.07 does not depend on an uncertain reading.

## C5.06 — Refuted in PL and smooth: raw proper Hurewicz fibrancy implies manifold fibres

The full construction and proof, independently audited, follows. It gives a closed six-manifold mapping properly to a circle with one nonmanifold fibre; in the smooth model there is one critical point.

\input{C5_Hurewicz_C}
