# Proof checks and counterexamples for cotes 156-1 and 156-2

Date: 19 November 2026. Actor: GPT-6 Astra Pro, root consolidation run; runtime reasoning-effort setting not exposed. Source line numbers refer to `pro/MPL_156-1+156-2_transcription.tex`, counted from 1. These are checks made in this run. Examples attributed below to the earlier notes are not claimed as new. A proof here is a mathematical argument, not a machine-checked certificate. The separate Python output checks only the finite assertions it explicitly lists.

## R-SA21-support: support injectivity and internal endpoint uniqueness

Assume F1 and the two separation/side-containment clauses of F2, with two distinct endpoints for each segment. Nonempty interiors are unnecessary for this argument. Suppose I and J have the same support X, and let the endpoints of I be a,b. If c is an endpoint of J but not of I, apply F2 to I at c. J is a subsegment of I incident to c, so X is contained in one of I_ac,I_bc. The other endpoint of I then belongs to both pieces, whose intersection is {c}, a contradiction. Thus the endpoint pairs agree; F1 at a gives I=J.

For the stronger *local* assertion that two segments J,K contained in a fixed I and with the same endpoints u,v are equal, an endpoint of I among u,v permits immediate use of F1. Otherwise apply F2 in I at u. Both J and K must lie on the same side, since otherwise v belongs to the intersection {u}. On that side u is an endpoint, and F1 again gives equality. The existence criterion for the pair {u,v} follows at the same time: v must be in one of the two initial/final subsegments based at u, and F1 in that subsegment is sufficient. This proves the exact corollaries at I scans6–7 without assuming a total order.

## R-SA21-infinite: divisibility is essential

With the original nonempty-interior clause, subdivide a segment at an interior point, retain a subsegment incident to a fixed endpoint, and repeat. F2 ensures that the other endpoint of the previous segment is excluded from the retained smaller segment. The nested supports therefore decrease strictly. This gives arbitrarily many distinct lieux and segments. The argument does not apply once the author admits empty interiors: a nonempty simple graph has no regular lieux. Correspondingly S=∅ iff L_r=∅ is valid only in the divisible version; the implication from left to right needs no divisibility.

## R-SA21-branches: the actual transitivity requirement

Define I~_x J by a common nontrivial initial subsegment. Reflexivity and symmetry are immediate. For transitivity, common initial subsegments of I,J and of J,K must themselves possess a common nontrivial initial subsegment inside J. This is the strengthened F3′ condition, extended from internal witnesses to arbitrary nontrivial initial pieces by subdividing first in the divisible case. The two applications of F1 identify that smaller segment in all three ambient segments. The F3 dichotomy alone is not the missing transitivity proof. In a reduced network the witness is a nontrivial segment, not an interior point (interiors are empty).

## R-SA21-orders: exactly what the order model verifies

Let P be a dense partial order such that, whenever x<y,z, some u satisfies x<u≤y,z, and dually. Take the nondegenerate closed order intervals as segments. F1 is restriction to [a,z] or [z,b]. F2 is interval separation and the fact that an interval incident to z has its other endpoint on one side. Two intervals issuing upwards from x share an initial interval by local downward directedness of the strict upper cone; downward intervals are dual; oppositely directed intervals meet just at x. These facts verify F3 and F3′. If two intervals meet just at a regular joint z, they cannot both issue in the same direction: the local filtering condition would give another common point. Their other endpoints therefore lie on opposite sides, and [a,b] is the unique F4 composite. Its support can strictly exceed the union. At an internally occurring point both directions exist, and the two direction classes are exactly its branches, giving F5.

This proves the interval-model direction, including every hypothesis used for the three order counterexamples below. It does not by itself prove the converse for an arbitrary network or a global orientation theorem. Hua2026, Theorem76.1, supplies an exact checked prose proof of the *single ambient segment* converse with F1,F2,F3′,F4; its Lean claim is reported, not rerun here. F3 and F5 are not needed for that forward direction. The manuscript itself leaves that characterization without a complete proof.

## R-SA21-restriction: the dense diamond

This counterexample is from the earlier run and is independently checked here. Form

P=(Q∩[0,1)) ⊕ ((Q∩(1,2))_0 ⊔ (Q∩(1,2))_1) ⊕ (Q∩(2,3]).

Each summand is ordered as written; the two middle chains are incomparable to one another; ordinal sums put every point of an earlier level below every point of a later level. All comparable-pair intervals are segments. There are a minimum 0 and maximum 3. Density holds within a chain; across levels an intermediate point can be chosen closer to the endpoint inside its chain. The same choice, sufficiently close to x in x's chain, proves both local filtering conditions. The order-model check above proves strengthened F1–F5. Strong F6 holds by taking [x,3] for the positive branch and [0,x] for the negative branch; weak F6 follows as well, including the endpoint cases. Every point except 0 and3 is regular.

Choose z=(3/2,0), and restrict to P′=[0,z]∪[z,3]. The entire second middle chain is omitted. The intervals [0,z] and [z,3] remain, meet precisely at z, and z is still regular, witnessed by an interval around it in its own middle chain. Any ambient segment with endpoints 0,3 is the unique interval [0,3]=P, which is not retained. Thus restricted F4 fails. All hypotheses of the author's claimed inheritance theorem hold in the ambient structure. The finite code checks the displayed support obstruction only; it does **not** claim that a finite sampling of this dense order satisfies its axioms.

Closing a subset under all F4 composites required by its retained segments is a necessary repair. Order-convex subsets give a useful sufficient setting in this interval model. A blanket corrected inheritance theorem for arbitrary networks is not asserted here.

## R-SA21-fork: local filtering does not give global filtering

The author's withdrawn local-to-global argument is refuted by his fork pattern; the earlier run supplies the explicit instance P=Q⊕(Q_0⊔Q_1). It is dense and locally filtered in both directions by choosing a point sufficiently close to x in the same chain. Every point has smaller and larger points. Its comparability graph is connected, since any two upper-arm points have a common predecessor in the lower Q. Nevertheless a point in one upper arm and a point in the other have no common upper bound. The interval-model proof verifies strengthened F1–F5, and every lieu is regular. Positive intervals based in the lower Q and reaching different upper arms share a branch but have no common extension, so F6 fails. This is a genuine role for F6, not a proof of global filtering from the earlier axioms.

## R-SA21-weakF6: interior extension versus support extension

This is the earlier run's example, rechecked. Let P=(Q∩[0,1))⊔{u,v}, with u,v incomparable and above all rationals, and with all comparable-pair intervals. The same local arguments verify density, both local filtering conditions and F1–F5. The two maxima are singular. At any rational x, the intervals [x,u] and [x,v] have exactly the same interiors, namely the rationals strictly above x. Thus either of these intervals gives the weak interior extension for this pair. More generally any two positive intervals can be extended internally by one of these, and downward intervals have a common extension towards0. At u or v there is only the downward branch, also internally extendible. Hence weak F6 holds everywhere. No interval can contain both u and v, so strong F6 fails.

This does not refute the special equal-endpoint lemma at I scan26. Its written proof needs a common segment containing the shared singular endpoint; interior inclusion alone does not supply that segment. The proposed reduction of weak to strong F6 for regular other endpoints uses the separate endpoint-prolongation corollary. We have checked the logical dependence; we do not treat that corollary as independently proved here.

## R-SA21-orientation: a diagnostic, not a solution

The earlier run's transport reformulation makes the outstanding obstruction precise. Each endpoint or branch pair is a two-element set; the prescribed bijections form a graph of transports. If this graph is connected, its quotient has two classes precisely when every closed walk has trivial permutation holonomy. A closed walk inducing the nonidentity permutation merges the labels into one class. A choice of a root label proves this elementary assertion by path transport. This does not prove that the manuscript's network axioms force trivial holonomy. The global orientation theorem and the unfinished equal-endpoint intersection argument remain separate open steps on the pages.

## R-SA21-quotient-embedding

Let A be closed in X and A⊂X′⊂X. A closed saturated subset D of X′ is X′∩F for its ambient closure F=cl_X D. If D meets A it contains A, and so does F. If D misses A, F∩A=∅ because A⊂X′ and F∩X′=D. Thus F is saturated in either case. Its image in X/A is closed, and the trace on X′/A is the image of D. This proves that the induced bijection from X′/A onto its image is a topological embedding. No normality or closedness of X′ is needed. The apparent source phrase placing this image in X instead of X/A is a reading alarm, not a silently changed quotation.

## R-SA21-cones: radial bases and finite polyhedral pairs

For the cone on a compact base B, every neighborhood of the apex contains a uniform small subcone. In B×[0,1] its inverse image is open along B×{0}; finitely many product neighborhoods cover that compact slice, and the minimum of their radial bounds works. The closed and open radial subcones are therefore cofinal. Locality of the regular-immersion definition follows by choosing one of them inside the given ambient neighborhood.

For a finite simplicial pair (K,L), barycentrically subdivide so that L is a full subcomplex. Let f be the piecewise linear function with vertex values0 on L and1 elsewhere. Then f^{-1}(0)=|L|. Fix 0<ε<1. The closed neighborhood N={f≤ε} has boundary B={f=ε}. In each simplex, a point of level t∈(0,ε] decomposes uniquely into its normalized L-coordinates and its normalized complementary coordinates. Rescaling t to ε identifies N\|L| with B×(0,ε], compatibly on faces. After collapsing |L|, the level0 is one point. The induced map cone(B)→N/|L| is a continuous bijection from a compact space to a Hausdorff space, hence a homeomorphism; N\B is open. This proves the finite-polyhedral assertion directly. If L is a union of components, the isolated apex uses the manuscript's explicit convention cone(∅)={apex}. It does not prove an undefined universal assertion about every category called “tame.”

## R-SA21-ficelle-connectivity

Let U=X\(A∪B), with the disjoint closed nonopen ends stipulated by the definition. If each connected component C of U has closure meeting both A and B, its image after collapsing B, together with the collapsed point b, is connected: adjoining a closure point to a connected set preserves connectedness. The union of all these connected subsets through b is (X\A)/B. The other quotient is dual. If U has finitely many components, each is clopen in U. If the closure of C missed B, C would define a nonempty clopen subset away from b in (X\A)/B, contradicting connectedness. Thus the converse uses the finite-component hypothesis precisely there.

Contracting a closed C inside the interior preserves the two connectedness conditions by continuous quotient maps. Neighborhoods of A and B may be taken off C, preserving the conic conditions. Separately collapsing A and B gives the same local tests and the same punctured quotient spaces, so the reduced criterion is equivalent. For point ends a,b, the connected sets X\{a}, X\{b} cover X and intersect: if they did not, X={a,b}, whose closed singletons are also open, excluded by the definition. Hence a reduced ficelle is connected.

## R-SA21-disconnected: a ficelle with disconnected underlying space

Take X=[0,1]×{−1,+1}, A={0}×{−1,+1}, B={1}×{−1,+1}. The two ends are nonempty, disjoint, closed and not open. Collapsing either end gives near its image a two-arm cone, a cone on a two-point compact space. Removing A and collapsing B joins two half-open intervals at b, hence is connected; the dual condition is identical. All four axioms hold, although X has two components. This refutes the necessity part of II scan11's compact-triangulable NB under the literal, unrestricted end convention. The example is attributed to the earlier run.

## R-SA21-interval: the missing connected-end hypothesis

On X=[0,1], set A={0,1}, B={1/2}. Both are disjoint closed nonopen regularly immersed subsets: collapsing A gives a circle with a conical marked point, and B already has a two-arm neighborhood. (X\B)/A consists of two half-intervals joined at their remaining endpoint and is an open interval. (X\A)/B=(0,1), since B is a singleton. Thus this is a ficelle omitted by the displayed classification by initial and final closed intervals.

If the ends are additionally connected, each is a closed interval. If A contained neither endpoint of X, then X\A would have two components and the connected, disjoint B could lie in only one; collapsing B would not join them. Therefore A meets an endpoint, and so does B. They must meet opposite endpoints, giving A=[0,α], B=[β,1] with α<β, up to exchange. Conversely such pairs satisfy all axioms. This is the precise repaired classification, not the unrestricted claim.

## R-SA21-tripod: endpoint enlargement is not monotone

Let X be a three-arm tree and choose two leaves a,b as point ends. Removing either leaf leaves a connected tree, and leaf neighborhoods are cones, so this is a reduced ficelle. Enlarge {a} to the whole closed arm from a to the central vertex. This enlarged A′ is connected, contractible, disjoint from b, closed, nonopen and regularly immersed (its quotient has a two-arm conical neighborhood). But X\A′ has the two other arms as separate components, and collapsing the singleton b does not join them. The enlargement fails the ficelle condition. This validates the author's own retraction and the earlier run's more precise example.

## R-SA21-polyhedra: reduced existence and uniqueness

For a connected finite polyhedron with at least two points, take a finite triangulation and a spanning tree in its connected one-skeleton. Choose two distinct leaves a,b of the tree. Removing a leaf vertex leaves the remaining tree connected. Every point of every punctured simplex can be connected within that punctured simplex to a remaining vertex; therefore deleting either chosen vertex from the full polyhedron leaves it connected. Each vertex has a sufficiently small compact conical neighborhood given by its link. Neither is isolated. This proves reduced-ficelle existence.

For uniqueness of the unordered endpoint pair, an arc has exactly its two endpoints as noncut points. If a finite polyhedron has a maximal simplex of dimension≥2, every point in its interior is conical and noncut: the punctured simplex is connected and continues to connect its whole boundary and every attached part. There are infinitely many such points. In dimension1, any edge on a cycle has infinitely many noncut interior points. A finite tree's noncut points are exactly its leaves, and a nontrivial finite tree has exactly two leaves iff it is an arc. These alternatives prove the uniqueness characterization for *unordered reduced endpoint pairs on the given space*. They do not prove uniqueness up to an unspecified equivalence for arbitrary disconnected ends.

## R-SA21-cone-cover: the omitted cover condition

The literal lemma in II scan7 assumes closed Z′,Z″⊂Z meeting only at c but does not say that they cover Z or a neighborhood. The earlier run's counterexample Z=Q, c=0, Z′={0,1}, Z″={0,−1} uses the author's apex-only empty cone convention. The point is isolated in each piece and thus conical, but Q has no compact neighborhood at0. An alternative not using empty links is

Z=([-1,1]×{0})∪({0}×(Q∩[-1,1]))⊂R²,
Z′=[0,1]×{0}, Z″=[−1,0]×{0}, c=(0,0).

The two closed pieces are cones on singletons, while every neighborhood of c in Z contains a closed rational interval on the vertical axis, preventing local compactness. No compact-base conical neighborhood exists in Z.

If instead the two closed pieces cover a neighborhood of c, gluing their compact cone neighborhoods at their apex gives the cone on the disjoint union of their compact bases. Conversely, a small punctured cone in a neighborhood covered this way splits into two clopen pieces. Each is constant on radial fibers; it is therefore B′×(0,t] for a clopen compact B′⊂B, with its apex restored. This proves the intended repaired equivalence. The missing cover is not asserted to be missing ink rather than an implicit contextual hypothesis.

## R-SA21-cutting: what is checked and what remains an obligation

After the two ends have been collapsed, the side decomposition of a lieu is precisely the two connected components of the complement containing a and b. This proves uniqueness of the sides. With connected ends the uncontracted sides are connected as well. The corrected contradiction in II scan6 must be to connectedness of X\{a}, not X\{c}, the latter already being split by the cut.

For closed pieces glued along homeomorphic closed end subspaces, the quotient construction is the topological pushout. Three successive pieces have the same quotient of their disjoint union regardless of parenthesization. This checks the reassociation step in the exchange lemma and the count n+1 pieces and n specified homeomorphisms for n internal cuts. The manuscript does not specify all morphisms for a categorical equivalence. Using endpoint-preserving homeomorphisms commuting with the gluing data is a reconstruction, and all cut regularity conditions must be retained; they are not consequences of arbitrary set-theoretic pushouts.

The cutting order is inclusion of families of allowable lieux. It must not be replaced by inclusion of the underlying regions. The source explicitly warns that equal regions need not determine equal cuts. The full directedness/density assertion for arbitrary non-Hausdorff ficelles is recorded at its actual proof level rather than promoted from the interval example.

### R-SA21-side-contraction: a further literal failure

This counterexample was found in the consolidation and independently reviewed by the VIII–IX reader. In II scan7, lines1333–1338, the condition that D avoid all three marked sets is deleted and replaced by containment in one side. That side contains its end A (lines1255–1270). On a tripod with leaf ends a,b, choose C to be a point strictly inside the b-arm, and let D be the whole closed a-arm, including the central vertex o. D is closed, connected, contractible, regularly immersed, and wholly contained in the A-side of C. Contract D. The quotient is an interval made of the two remaining arms, but the image a′ of A is now an interior point. Its complement has two components, and B is a singleton whose contraction cannot join them. Thus (X/D,{q(A),q(B)}) is not a ficelle. All remaining endpoint and regularity hypotheses hold in this finite graph. This also meets the parenthetical suggestion that D be connected.

The earlier interior-contraction lemma, where D is disjoint from both ends, is unaffected. Keeping D disjoint from A∪B, or explicitly rechecking the quotient's end conditions, is necessary to avoid this example. Because the U/X overwrite at the side definition is unresolved, the refutation is stated for the literal side-containing-the-end reading, not as a decision about the ink. The finite graph quotient is included in `root_checks.json`.

There is a separate regularity obstruction if no tame restriction is imposed: take X=[0,1], A={0}, B={1}, C={3/4}, and D the Cantor set scaled into[0,1/2]. The image of A is not conical. Every neighborhood of it contains a whole sufficiently small complementary gap with its endpoints identified, hence a circle; collapsing the complement of that gap gives a retraction of the entire quotient, and of such a neighborhood, onto that circle. A cone is contractible, so no cone neighborhood can exist. In this example the punctured connectivity condition already fails as well. This additional example is not needed for the finite counterexample.

## R-SA21-incompatible: two exact obstructions to literal refinement

In a square with the opposite vertical edges as ends, the middle vertical arc and a slightly tilted top-to-bottom straight arc are each collared separating lieux. They cross, so cannot both be retained as distinct compatible cuts in one ordered cutting chain.

Even ordinary disjointness does not suffice. On a circle with two distinct point ends a,b, parameterize each a-to-b arc by (0,1). Let C have coordinates (1/3,2/3) and D coordinates (2/3,1/3). Each two-point subset is closed, regularly immersed and separates the ends; the cut pieces are arcs with possibly disconnected end subsets and satisfy the ficelle conditions. C and D are disjoint, but D has a point on each side of C, so it is not a lieu of either cut piece. Thus the manuscript's compatibility is strictly stronger than set disjointness. The code checks the arc-order assertion exactly using rational numbers.

## R-SA21-rives: Boolean algebra, conic calculation and local/global distinction

Clop(Z) has addition symmetric difference, multiplication intersection and unit Z. Restriction maps preserve these operations, hence so does the filtered neighborhood colimit. For a compact-base cone, punctured uniform subcones are B×(0,t); a clopen subset is constant along every connected radial fiber. Restricting to one level identifies its algebra with Clop(B). This redoes the author's conic rive calculation.

The unit vanishes in the filtered colimit iff it vanishes at some sufficiently small neighborhood, i.e. V\A=∅ for a neighborhood V of A. This is equivalent to A being open. Thus a nonzero rive ring has distinct complementary elements ρ and1+ρ; an unordered pair has two orientations. The supplied transcription already says “A n'est pas ouvert”; the alternative reading discussed by Hua2026 is not substituted into it.

For two separated points in R² the two punctured disks are individually connected. Their common-neighborhood germ ring is F₂×F₂. Its nontrivial birive selects one point's punctured neighborhood versus the other's, but neither individual point locally separates R². The author is using a germ along the entire closed set, not a stalkwise separation condition.

A Cantor link has clopen cylinder partitions of size2^n for all n, so its clopen algebra is infinite despite compactness. Links S¹ and S² both have clopen algebra F₂ but different first homology. These examples show exactly which information the Boolean rive invariant forgets; they do not refute a reconstruction retaining other data.

## R-SA21-sheaves: the comparison and its hypotheses

For any sheaf F, equality of the germs of two neighborhood sections at every point of A implies equality on the union of neighborhoods on which they agree. This proves injectivity of colim_{V⊃A}Γ(V,F)→Γ(A,F|A), without paracompactness. For surjectivity with A closed in paracompact Hausdorff X, Schapira2023 Proposition10.1.2(iii) is the exact opened source for sheaves of k-modules, which suffices for the Boolean sheaf here; it explicitly points back to Godement1958. This run checks that statement and its convention for paracompactness, not an independent full proof of the shrinking argument.

A precise *reconstruction* of the implicit spectrum is the relative Stone space of the Boolean sheaf R=(i_*F₂)|A: points (a,p) with p prime in R_a, with basic sets D(s) over open subsets of A. Gillam2011's prime-system localization gives a compatible ringed-space formulation. Under this convention Clop(Spec_A R) identifies with Γ(A,R): locally use the stalk's Stone representation, cover the compact fiber by finitely many basic neighborhoods, and shrink the base until their Boolean coverage identity holds. The finite coverage provides one local section for a given clopen; these sections agree at stalks and glue. This is an explicit conventional reconstruction, not proof that the manuscript selected this convention rather than another.

In X=S¹×[−1,1], A=S¹×{0}, the sheaf has constant fiber F₂². Its relative spectrum is two copies of the circle. The étalé space of its *elements* has four copies. Its global section ring is F₂², whose ordinary spectrum has only two points. The distinctions are essential to the map to A required by the subsequent pushouts.

## R-SA21-Stone: finite algebra counts and their limit

Given n Boolean generators, each point of a representing Stone space has one of at most2^n truth vectors. The nonempty truth-vector classes are the atoms; every element is a union of these atoms. There are at most2^(2^n) elements. Every finite set of elements therefore lies in a finite Boolean subalgebra. Compatible prime ideals in all finite subalgebras give a prime ideal in their union, and conversely by restriction. Their basic clopens agree, proving the inverse-limit description of the global Stone spectrum. This is classical Boolean duality, not a new geometry-of-forms realization theorem. The code enumerates the small free cases and the F₂² spectrum.

## R-SA21-finite-topology: the limitation of a raw inverse limit

Stacks09XV proves that a directed inverse limit of finite sober spaces is spectral; finite T₀ spaces are sober. Every map between finite spaces is quasi-compact, so the bonding-map hypothesis is automatic here. If the limit is Hausdorff, each member of its compact open basis is closed. It is therefore zero-dimensional, and cannot be a connected nontrivial compact Hausdorff interval or circle. McCord's weak equivalence, Barmak–Minian's simple-homotopy comparison and Clader's homotopy equivalence/quotient statements have different conclusions and do not contradict this argument. None identifies its indexing system with the author's literal compatible cutting chains.

Selected horizontal cuts in S¹×[0,1] and S²×[0,1] give the same finite ordered index sets; their labeled pieces have different homology. This checks loss of labels for those selected systems. It does not assert that the complete posets of all possible lieux are isomorphic.

## Unproved here, deliberately not filled in

The exact general F4 endpoint-prolongation corollaries, F5⇔F5′, coherent global orientation, the weak-F6 singular-end argument, the unfinished equal-endpoint intersection assertion, arbitrary property-P stability, the full spectrum-cut topology and regularity transfer, and the final two-node symmetry are retained at their documented proof levels. Literature and version checks are completed for these questions; an unsuccessful bounded search is not a proof that they are globally open. They are inputs to separately ranked tasks, not gaps disguised by a broad modern comparison theorem.
