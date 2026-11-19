# Cote 64, scans 2–77: mathematical checks

Run SA16-2026-11-19-cote64-early; 19 November 2026. These are this run's proofs and computations, not a replacement transcription. Manuscript locators in the accompanying JSON use one-based physical transcript lines. No scan was available. Literature keys refer to references.bib; the source ledger records precisely what was opened.

## 1. Four-sets and the symmetric group

For a four-set I, the identity and the three double transpositions form a normal Klein group V. Every nonidentity element is fixed-point-free, so the action is regular and makes I an affine torsor under the two-dimensional vector space V over F₂. An origin is additional data. A permutation commuting with every translation is itself a translation: its value at one point determines it everywhere. Thus C(V)=V while N(V)=S₄. This checks both visible corrections in items 211–212.

Conjugation on J=V∖{0} gives 1→V→S_I→S_J→1. The sign characters on I and J agree: a transposition interchanges two elements of J. Their orientation torsors consequently have two natural identifications, differing by the nonidentity element of C₂. Naturality does not select one.

There are eight 3-cycles, two per Sylow 3-subgroup, hence four such subgroups. Conjugation on them is faithful: the kernel is normal and lies in a subgroup of order 6, while none of the normal Klein elements acts trivially. This identifies S₄ with their permutation group. An automorphism of S₄ acts on this four-set; composing with an inner automorphism makes that action trivial, and faithfulness of the representation then makes the automorphism itself trivial. The groupoid equivalence follows, with invertible arrows exactly as required by the manuscript margin. The uncertain numeral “trois” on scan 6 is false under its literal reading, without deciding the ink.

The cycle-type counts are 1,3,8,6,6 for identity, double transpositions, 3-cycles, transpositions, and 4-cycles. Squaring the six 4-cycles maps them two-to-one onto V∖{0}. A double transposition has centralizer of order 2²·2!=8: one may interchange its two cycles and exchange their endpoints independently. This is D₈, not C₄. Its two square roots generate the distinguished C₄ within it. These are claims 214,216,305,306.

The exhaustive finite_groups.py program stores every subgroup and its actual elements: 30 subgroups, 11 conjugacy classes, and 66 Hasse covers. Burnside1897 §173, Theorem VIII, is an exact historical source for the inner-automorphism fact. Our finite certificate completes the requested inclusion diagram without claiming that the book prints our diagram.

## 2. Squares and reflection groups

Write D₈=⟨r,s | r⁴=s²=1, srs=r⁻¹⟩ and a=r². Its center and derived subgroup are ⟨a⟩, its abelianization C₂², and its three index-two subgroups the rotation C₄ and two Klein groups. The square descriptions on scans 8–10 reconstruct a four-set with antipodism from its two diagonals and their two-element fibers, or from dual incidence data. Disjoint union of diagonal fibers and products of the relevant two-element torsors give inverse constructions. In the product description opposite vertices are (x,y) and (ax,ay). These operations commute with isomorphisms and hence are canonical once the stated data, rather than extra representatives, are retained.

The action signs on vertices, diagonals and codiagonals multiply to 1; checking r and s proves this for D₈. The ordered product of chosen representatives additionally depends on multiplication convention. The script exhibits rcd=r² and dcr=1 with function composition; this illustrates order sensitivity, not a contradiction to the author's declared convention.

The four noncentral involutions of D₈ form a square, with opposite pair x,ax. They generate the group, so the action of Aut(D₈) on this square is faithful. An automorphism chooses the image of r among r,r⁻¹ and that of s among four reflections, giving eight automorphisms. The reflection-square functor therefore induces an automorphism-group isomorphism and an equivalence of the connected groupoids. In contrast Q↦Aut(Q) induces conjugation with kernel ⟨a⟩. The manuscript's scan-16 question is answered by scan 17's different reflection construction.

The written commutator-only relations on scan 17 cannot be a complete finite presentation. Sending every reflection generator to 1 in Z and a to 0 satisfies them and gives an infinite quotient. A repair adds a²=x²=y²=1, centrality of a, opposite symbols x′=ax,y′=ay, and [x,y]=a for adjacent reflections. Moving a left and commuting x,y at the cost of a reduces every word to a^εx^ηy^θ. The standard square realizes all eight forms, proving the repaired presentation C-SA16-322. These are added relations, not words silently supplied to the transcription.

For three C₂-torsors L_j, the product ∏L_j has eight elements and is a C₂^J-torsor. Quotienting by the four-element sum-zero kernel gives the contracted product ∧L_j with two elements and C₂-action. This proves C-SA16-328 and identifies the mistaken acting-group label. The exact published construction is SGA1 XI §4, after Proposition 4.3; Definition 4.1 only defines torsors. All the explicit finite constructions descend to finite étale sheaves using SGA1 VIII Theorem 2.1 and IX Proposition 4.1. Matching orders alone would not prove this: the equivariant maps above are what descend.

## 3. Cube correspondences

The program cube_and_pgl.py realizes 24 cube rotations as signed permutation matrices of determinant 1. Their faithful action on four body diagonals identifies the group with S₄. It enumerates the ten nontrivial transitive feature sets in its output and records each stabilizer as actual permutations of the body diagonals; the one-point set supplies the remaining subgroup class. This is our completion of the requested correspondence table.

A face diagonal has a stabilizer of order 2 generated by a double transposition, and hence contained in the normal Klein group. The negative word in the current scan-25 reading reverses the answer; the image must decide whether this is author or transcription error. The two six-element actions on scan 23 have stabilizers C₄ and a nonnormal V₄, so are inequivalent despite equal size. Their action characters are checked on every element in finite_groups.py. Burnside1897 §§202–203 supplies the historical polyhedral-group setting, not this exact ten-row output.

## 4. Rank-two Z/4 modules

Let R=Z/4, M₀=M/2M, and J=M₀∖{0}. Multiplication by 2 identifies M₀ with 2M. Each of the three nonzero vectors has four lifts, giving 64 triples. Their sum lies in 2M; varying one lift moves the sum transitively over four values. Thus the zero-sum triples form a 16-element torsor P_M. Its translation group is ker(Σ:M₀^J→M₀), canonically End(M₀): evaluate a linear map on the three vectors; conversely values on two basis vectors, with the zero-sum condition, determine it. The full-product subscript in the current transcription has dimension 6 rather than 4.

Let A be zero and the three order-two matrices in GL₂(F₂). Let W be the subalgebra spanned by id and an order-three matrix q, with q²+q+id=0, so W≅F₄. Both planes are stable under conjugation, A∩W=0, and End(M₀)=A⊕W. The trace pairing makes them orthogonal, and sl(M₀)=A⊕F₂id. Within W the scalar line is self-orthogonal; within all End(M₀) its perpendicular has dimension 3. The S₃-invariants of W are exactly F₂id, on which trace is zero, so 0→F₂→W→F₂→0 does not split equivariantly. All sixteen matrices, their traces, products and conjugates are tested. BrauJones2016, proof of Lemma 3.1 after equation (26), supplies an independently opened occurrence of these two invariant planes.

The congruence kernel is u↦1+2ũ; multiplication corresponds to addition and det(1+2ũ)=1+2tr(u). The integral matrices (0,−1;1,−1) and (0,1;1,0) generate an S₃ complement in GL₂(R). Their reductions are generators of GL₂(F₂). No complement lies in SL₂(R). A lift of a transvection is conjugate modulo 4 to
g=(1+2a,1+2b;2c,1+2d).
The equation g²=1 gives c=0 and a+d=1 modulo 2, while det(g)=1 requires a+d−c=0. Thus every order-two element of SL₂(R) reduces to the identity, contradicting what a section would do to a transposition. A proper *supplement* need not be a complement; the opened current DetinkoFlanneryHulpke2018 Theorem 2.5 uses the former word.

The quotients I=P_M/W and Q=P_M/A each have four elements, and Q inherits a square structure from the scalar involution in W. The natural action into S_I×Aut(Q) is faithful and its image satisfies the codiagonal-character equality. Its target fiber product S₄×_{C₂}D₈ has order 24·8/2=96=|GL₂(R)|, so the injection is an isomorphism. Both groupoids have a standard local object; the induced automorphism isomorphism proves the equivalence and the explicit construction descends. The code checks all 96 actions, their kernels, and the character equality.

All commutators and generated subgroups are computed. The derived groups of GL and SL have orders 24 and 12; the latter is A₄ and intersects {±1} trivially. The abelianizations are C₂² and C₄, and both centers are {±1}. The five subgroup squares at scan 32 are checked as explicit intersections, retaining their trivialization choices.

There are twelve primitive vectors and six sign classes. The projective action has kernel {±1} and image 48. The eight faces are selections of a vertex above each of the three reduction directions; each has two zero-sum lifts exchanged by −1. The three nontrivial characters are mod-2 sign, determinant and their product. The earlier-run matrix U=(1,0;1,1) has determinant 1, odd reduction sign and projective cycle lengths 4,1,1. This is a verified finite example, without a verified cusp interpretation.

The symmetric reference module M_J=ker(Σ:R^J→R) has vectors r_j=3e_j−Σe_k, namely (2,3,3) and its permutations. They have zero sum, reduce to the three nonzero mod-2 vectors, and any two have odd determinant in two independent coordinates, hence form a basis. Its underlying additive extension cannot split: all elements killed by 2 already lie in 2M. That is compatible with the automorphism-group splitting.

The earlier-run scalar-quotient formula can also be checked locally without its missing external project endpoint. For a trace-zero matrix A=(a,b;c,a), put f_A(v)=det(v,Av) on J=V minus {0}. In the ordered coordinates (1,0),(0,1),(1,1), its values are (c,b,b+c). Modulo constant functions this is the class of the point mass at (b,c), with the zero vector mapped to zero. The scalar parameter a disappears. The function construction is linear in A, and determinant is invariant under GL₂(F₂), proving equivariance and scalar kernel. Both quotient spaces have dimension two, so the map is an isomorphism. The program scalar_quotient.py checks all 64 additivity pairs, 48 equivariance pairs and eight coordinate comparisons. This establishes C-SA16-307 locally; it does not verify the cited LM/R17 source.

Twisting an octahedron by its orientation torsor through antipodism squares its orientation character, giving a canonical orientation of the new object. It does not orient the original object. Likewise, (E,α) and (E,−α) are isomorphic marked elliptic curves through [−1], although α and −α are distinct elements of the frame torsor.

## 5. Central lifting obstruction

Take adjacent involutions a,b of D₈ with central commutator z, and section q(x,y)=b^y a^x of D₈→C₂². Then
q(x,y)q(u,v)=z^(xv)q(x+u,y+v).
The factor set is c(g)d(h), so for two quotient torsors c,d the obstruction is c∪d in H²(S,C₂). Lift transition functions by q(c_ij,d_ij); their failure of the cocycle equation is c_ij d_jk. Changing lifts by a 1-cochain changes this by a coboundary. On a general site this is the obstruction gerbe formulation; one may refine the cover, and a single chosen Čech cover is not asserted to compute arbitrary H². When the obstruction vanishes, lifts form a groupoid acted on transitively by C₂-torsors, with a fixed lift's automorphisms H⁰(S,C₂).

The manuscript reduces its mod-4 projective lifting question to this square lifting question. This resolves the finite obstruction problem. The formula is an earlier-run reconstruction independently re-proved here. MerkurjevScavia2024 §1.1, equations (1.3)–(1.4), Example 1.4, gives the matching profinite-group criterion; its field formulation alone is not our entire relative dictionary. The script checks all sixteen factor-set products.

The universal central extension does not split: T=(0,−1;1,0) satisfies T²=−1, while its projective image has order 2 and both lifts T,−T have order 4. A group section would preserve the order-two relation. Individual torsor liftability and universal group splitting are therefore distinct assertions.

## 6. Octahedra and characteristic 5

Assume 2 invertible and a fiberwise faithful Klein subgroup of a relative projective line. Étale locally, a nontrivial involution has two disjoint fixed sections, which can be put at 0,∞; it is then z↦−z. A different commuting involution interchanges them and has form z↦a/z, with a a unit. Adjoin a square root of a and rescale, and adjoin i²=−1. These are étale extensions. The three fixed pairs become {0,∞}, {1,−1}, {i,−i}. This proves the local normal form, including characteristic 3, without using a prime-to-24 classification.

Preserving this unordered partition defines the structured normalizer. The transformations iz,1/z,(z+1)/(z−1) act transitively on its six points. A structured automorphism fixing ∞ fixes its opposite 0, hence is az; it must have a∈{1,−1,i,−i}. There are therefore exactly 6·4=24. This is a scheme argument: a projectivity is uniquely determined by three disjoint sections, giving an injection into the finite permutation scheme; all 24 allowed permutations are realized by explicit projectivities over the étale base, and the same argument holds after every base change. No additional infinitesimal sections remain. Thus the structured group scheme is finite étale of rank 24 over Z[1/2], though its rational sections depend on the form.

For the bare divisor, a stabilizer fixing ∞ is az+b and permutes the five finite points, whose sum is 0. Their transformed sum is 5b. If 5 is invertible, b=0 and the same conclusion follows. In characteristic 5 take i=2: the six points are P¹(F₅). Every projectivity preserving them is determined by three of those points and is in PGL₂(F₅), of order 120. The map 2z+1 fixes ∞,−1 but changes opposition. The orbit of a regular opposition has 120/24=5 elements. All fifteen pair partitions are enumerated: five regular ones have stabilizer 24, ten others stabilizer 12.

Consequently the universal bare stabilizer over Z[1/2] is nonflat and not étale: its geometric degree jumps. The structured result survives. The manuscript rejects intermediate arithmetic but does not retract the false bare-divisor conclusion. Hua2026 §42 proves the field exception and explicitly leaves the relative correspondence unproved; no formal source was compiled here.

A regular structured octahedron determines its three fixed-pair involutions, hence its Klein group. Its direct symmetries extend uniquely to projectivities: uniqueness follows from three points and existence from the 24 formulas. Thus the three-way correspondence is valid with opposition retained. A quarter-turn has tangent multiplier i or −i; reversing combinatorial orientation swaps them, giving the canonical orientation torsor μ₄*.

For the four-cover formulation, take the reference conic x²+y²+z²=0 and the six coordinate-plane intersections paired within each plane. Signed permutation matrices of determinant 1 give a constant S₄ of order 24, preserving the conic and its opposition, and exhausting its structured symmetries. Twisting by the S₄-torsor of labelings of a four-cover, and reversing via the automorphism torsor, gives the equivalence. These forms descend effectively as projectivized quadratic modules. The orientation identification is the canonical one; an independently chosen additional identification would change the groupoid. Over R the reference conic is anisotropic, whereas split P¹ is not. On split P¹ the normalizer has eight real sections, so one must not identify every form with a constant S₄ subgroup of PGL₂(R).

## 7. Cubic conics and genus-one twists

For a rank-three finite étale algebra A over a base with 2 invertible, Tr(y²) is nondegenerate because its polarized trace pairing is. After an étale split A=O³, the conic Σy_j²=0 has gradient (2y_j), with no common projective zero. This works also in characteristic 3; Tr(1)=0 does not make the trace pairing degenerate. The coordinate-square map [y_j]↦[y_j²] lands in Σx_j=0 and is a degree-four quotient by sign changes modulo common sign. Its three branch labels are the coordinate planes. The construction commutes with permutations and descends.

For the standard Klein action, q=z²+z⁻² is invariant of degree 4 and generates the invariant function field. The normalization g₂=−(z²−1)²/(4z²)=(2−q)/4 is independently verified. This is a local algebraic equality; the proposed cote 142/146 project endpoints remain unavailable.

Twisting V_J-torsors adds cocycles; since V_J has exponent 2, twisting twice by a fixed torsor is the identity. Hence I=K∧F_t and K=I∧F_t without I constant. The specific identification with V_J matters: geometric connectedness does not select one of the six possible GL₂(F₂) markings.

For I={0,1,∞,t}, the canonical double transpositions extend as
σ₀=(z−t)/(z−1), σ₁=t/z, σ∞=t(z−1)/(z−t).
Their determinants are units when t,t−1 are units, they are involutions, and σ₀σ₁=σ∞. Three point values give uniqueness, so the extensions descend without a labeling. This concerns the Klein subgroup, not every S₄ permutation.

An involution of an E₀-torsor inducing −1 on E₀ is locally x↦a−x. Its fixed locus I=[2]⁻¹(a) is an E₀[2]-torsor. Choosing a fixed point converts the involution to −1, and changes of fixed point are translations by E₀[2]; hence E=I∧E₀. The inverse construction is immediate. The quotient by E₀[2] is identified with E₀ by 2x−a. Under x′=x−b,a′=a−2b this expression is unchanged, proving canonicity.

The “almost cartesian” comparison is cartesian off the branch. Over a geometric field its completed local raw fiber product is v²=u², whose normalization is the two branches v=u and v=−u. The raw product is nodal, not smooth. Over a nonnormal base, absolute normalization need not commute with base change: the accurate relative assertion uses the canonical smooth two-branch model, and the geometric normalization assertion is retained with that qualification. This limitation is explicit in the refined problem index.

## 8. Doubling and multiplicities

The canonical Klein action has a degree-four quotient, whose three branch labels identify its target with the source's three-point line. This gives the intrinsic normalized doubling map, and after choosing an elliptic double cover it descends multiplication by 2. Four equal point values alone do not characterize a rational function: quotient invariance, degree and branch labels do.

Put A=z²−2z+t, B=z²−2tz+t and F_t=tA²/B². The program verifies all three Klein invariances. The resultant is 4t(t−1)², and
tA²−B²=(t−1)(z²−t)².
Thus the degree is 4 and all three ramified fibers have the required multiplicities. Each of 0,1,∞,t maps to t. Before squaring, A/B is +1 at 0,∞ and −1 at 1,t. The final formula and c_t=t are correct despite the intermediate sign slip. The fixed quadratic of σ∞ is z²−2tz+t, with roots t±√(t(t−1)); the written alternative radical using t(1−t) gives residual −2t(t−1). This raises an ink alarm without deciding it.

Let q:E→E/±, t=q(0), and F_m q=q[m] for m=2^n. Then deg F_m=m², and since [m] is étale,
e(F_m,q(P)) e(q,P)=e(q,0)=2
for P∈E[m]. Multiplicity is 1 at the four images of E[2] and 2 at the remaining sign pairs. Thus F_m*[t]=q_*[E[m]] as divisors, with degree m² but support m²/2+2. The scheme image of the reduced finite étale E[m] is reduced over a geometric field, so for m≥4 it is not the full fiber. The exact t=2,m=4 factorization in symbolic_checks.json has degree 16 and ten support points. Milnor2004 supplies the complex quotient framework; the polynomial and algebraic ramification arguments here check the stated characteristic and base hypotheses independently.

## 9. Tangential Kummer data

In a tame local model x=u yⁿ, n,u units, multiplication by y on 1,y,…,y^(n−1) has determinant (−1)^(n−1)x/u. Thus determinant norm and leading-jet tangent identifications differ by (−1)^(n−1). The code evaluates n=2,…,8; the companion-matrix expansion proves the general formula. Dualizing and inverting as appropriate gives the tangent map T′^n→T with the same sign. The convention is tracked, not supplied silently.

Local deck transformations y↦ζy have faithful tangent character with image μ_n. For a G-cover with a marked ramification section, its stabilizer therefore gives an actual embedding μ_n→G. It depends on the cover class, contrary to the independently listed target data on scan 73.

For a counterexample take S=Spec C, X=A¹_x, t=0, G=C₂² and X′=A¹_y×{0,1}, mapping by x=y², with (a,b).(y,e)=((−1)^a y,e+b). It is finite locally free of degree 4, smooth over S of relative dimension 1, a G-torsor over G_m, and tame of index 2 at the marked point (0,0). These hypotheses are exactly those on scan 71; there is no connectedness requirement. Actual inertia is A=C₂×{0}. Its class ξ is the quadratic character in the first factor and trivial in the second.

Use that ξ and n=2, but choose i:μ₂→G with image B={0}×C₂. Take T=C and a nonzero square identification with T_X,0, for instance the norm convention coefficient −1. Every independently written target condition holds. It is not in the essential image: ξ fixes actual inertia A, central in G, so no change of point over 0 gives B. Allowing a group isomorphism changes both A and B together, preserving their inequality. The code checks all six group automorphisms and the two preserving ξ. This is a counterexample to essential surjectivity, not merely a complaint about vague morphisms.

A necessary repair requires i to be the tangent-inertia embedding of ξ, with explicit morphisms compatible with power maps when n changes. The full arbitrary-G equivalence for a minimally repaired target is not asserted here; its precise formulation and descent data remain a task (C-SA16-391).

For the quadratic case there is no competing inertia embedding. A four-branch double cover is étale locally Legendre, and all forms with fixed branch data differ by a μ₂-torsor. Its tangent line at the distinguished branch point with squared norm identification changes by the same torsor. This is checked locally in y²=u x(x−1)(x−t); rescaling the square root of u rescales the tangent root inversely, with the fixed norm sign above. Both automorphism groups are μ₂ and the coordinate-change construction descends, giving the special quadratic groupoid equivalence. AntieauMeier2020 Definition 4.4 and Proposition 4.5 check the labeled case; Lemma 4.7 retains a twisted S₃ action rather than an ordinary action on the atlas.

More explicitly, for fixed cubic étale J and t off its trisection, use the functor from the stack of the corresponding elliptic double covers to the stack of square roots of T_Σ,t, sending a cover to its tangent at the marked ramification section and the norm square map. Étale locally, order J and choose a Legendre model. Root objects and cover objects are then both twists of that reference by μ₂, and deck transformation −1 acts by −1 on the tangent. Hence the induced map of isomorphism sheaves is an isomorphism, not merely a bijection on geometric isomorphism classes. Every root is locally attained by twisting the reference cover. Full faithfulness and local essential surjectivity, with effective descent for the covers, give the equivalence over the original base. This argument proves the pure geometric equivalence; it makes no additional choice of the symmetric μ₄ normalization used later.

An invertible line with a specified n-th power has μ_n automorphisms. Isomorphisms between two such roots, when present, form a μ_n-torsor (Stacks03PK, equation 59.28.4.1). “Unique isomorphism” must therefore refer to the full rigidified comparison, not to a bare root line.

## 10. Orientation and pinning

For the lines convention of P(W), with universal L=O(−1), first-order deformations of L are Hom(L,W/L). If W has rank 2, this is L⁻²⊗det W, proving T_P(W)=O(2)⊗det W. For the trace-zero permutation bundle of the three-cover J, the exact sequence 0→W→O^J→O→0 has determinant det W=det O^J, the orientation sign line. The sum map is surjective even in characteristic 3: no division by 3 occurs. The quotient convention dualizes det W, harmless for the canonically self-dual sign line. This is the independent proof of the tangent formula.

The projective convention was checked directly in EGA II, Proposition 4.1.6 and Proposition 4.2.3 (printed pp. 72–74), with base-change compatibility in §4.2.8–10. These passages give the tautological invertible quotient and its universal property. They are the historical projective-bundle endpoint, not a claim that EGA states this particular orientation formula.

Squaring a line twisted by a μ₄-torsor twists its square by the induced μ₂-torsor. An identification of the orientation of J with μ₄* therefore gives the normalization on scan 76. This character-power identity does not assert an untwisted S₃-action on ordinary Legendre structures; ConradLevel Remark 2.8 explicitly excludes that.

The Q₀ promise is fulfilled at scan 78, physical lines 6–31, read directly in the continuation. Its rotations are μ₄; chosen side endpoints indexed by i∈μ₄* satisfy s′_i=i s_i, and its diagonal torsor is μ₄*. The model x⁴=−4, vertices ±1±i and s_i=1−i, is an optional prior-run/Hua realization, not a manuscript formula. It verifies consistency but is kept apart from the page.

With the orientation identification fixed, two compatible pinnings differ by λ with λ²=1. Thus they form a finite étale μ₂-torsor, with two geometric choices; for varying J the orientation datum must be retained. ConradLevel Proposition 3.2 constructs a canonical Legendre structure from suitable level-4 points and negates its differential when the selected 4-torsion point is negated. This settles existence of a canonical route from level 4, while the manuscript's later symmetric normalization comparison requires its additional data.
