# F61: coherent pure complexes for the actual rank-three graded kernels

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

This is a constructive continuation of F56, not a new proof of a source positivity conjecture. The formal positive kernels and their explicit quadratic and degree-five isomorphisms already exist in F56. The addition here is a grading-to-arithmetic functor which preserves those actual maps, their specified tensor comparisons, and their positive Euler traces while making each kernel entry pure of a prescribed single complex weight. There are two parameter conventions, with different domains. Their limitations are part of the statement.

## 1. Exact input and purity convention

Fix a prime power q, a prime ell not dividing q, and a finite extension E of Q_ell, enlarged when necessary to contain the stated arithmetic lines and Gaussian coefficients. All multiplicity spaces have trivial Frobenius. Let V be finite Z-graded E-vector spaces, and give V ordinary tensor symmetry, without Koszul signs on the formal grading. Write E<e> for a line in formal degree e. For a finite state set I, use

\[
(K\star L)_{ab}=\bigoplus_{h\in I}K_{ah}\otimes L_{hb}.
\tag{R1}
\]

The monoidal unit has E in degree zero on its diagonal. These kernels act on row vectors, so T_L composed with T_K is T_(K star L). The associator preserves the state path and the ordered homogeneous tensor factors.

The actual F43/F56 rank-three right action has 64 states: 20 scalar-plus states, 4 scalar-minus states, 16 copies of the two-state module N(delta), and 4 copies of N(D-2), where

\[
\delta=v+v^{-1},\qquad D=\delta^2.
\]

Put

\[
A_1=E<-1>\oplus E<1>,\qquad
A_2=E<-2>\oplus E<2>,\qquad
\mathcal D=A_1^{\otimes2}.
\tag{R2}
\]

On N(A), with A equal to A_1 or A_2, the kernels are

\[
K_1=\begin{pmatrix}\mathcal D&0\\ A&0\end{pmatrix},
\qquad
K_2=\begin{pmatrix}0&A\\0&\mathcal D\end{pmatrix}.
\tag{R3}
\]

Both kernels are D on each plus state and zero on each minus state. Their entrywise graded characters are the actual named P_1 and P_2 matrices in the proved regular F43 tensor basis. This statement retains that basis's finite-localization scope; it makes no new assertion about VIII's original global tensor lattice. Keeping one copy of each scalar and two-state block gives the faithful six-state version.

We use geometric Frobenius. For a point complex C, BBD §5.1.8, pp. 126–127, says that C is pure of weight w exactly when H^i(C) is punctually pure of weight w+i. Its integer-weight convention is §5.1.5, pp. 125–126. On the point every constructible cohomology sheaf is lisse, so the smooth/lisse qualification in §5.1.8 applies. In particular shifting a pure sheaf of weight a by [-i] gives a complex pure of weight a-i.

All complexes constructed below are explicit bounded split complexes with zero differentials. Their tensor products and maps can first be read as complexes of finite Weil spaces and then as objects and morphisms of the derived constructible Weil category. We use the specified split image and do not assert that it contains every morphism of the ambient derived category.

## 2. Full-Tate convention: every graded kernel has a coherent pure lift

For the convention v=q^n at extension degree n, define

\[
\Phi_{\mathrm T}(U)
 =\bigoplus_{e\in\mathbb Z}U_e\otimes E(-e)[-2e].
\tag{R4}
\]

The vector space U_e is a multiplicity space with trivial Frobenius. Geometric Frobenius on E(-e) is q^e. Every nonzero summand lies in degree 2e, has cohomology weight 2e, and is therefore pure of complex weight zero. The finite sum is pure of weight zero. Its Euler trace is

\[
\operatorname{Tr}_{\mathrm{Euler}}(F^n;\Phi_{\mathrm T}(U))
 =\sum_e\dim(U_e)q^{en}
 =\operatorname{ch}(U)(q^n).
\tag{R5}
\]

There is no Euler minus sign, since every degree 2e is even. Negative formal degrees cause no difficulty: both positive and negative cohomological degrees are allowed in a bounded complex.

Choose the usual tensor identifications E(-e) tensor E(-f)=E(-(e+f)). On a homogeneous tensor u tensor u', define the tensorator

\[
\Phi_{\mathrm T}(U)\otimes\Phi_{\mathrm T}(U')
 \longrightarrow\Phi_{\mathrm T}(U\otimes U')
\tag{R6}
\]

by that identification, retaining u and u' in their displayed order. Shifts add because -2e-2f=-2(e+f). Every associativity route is the same map on the same ordered pure tensor. The unit E<0> maps to E in degree zero. The derived tensor symmetry on the images contributes the sign (-1)^(2e times 2f)=1, so the source's ordinary flip is preserved. This proves an additive symmetric strong monoidal functor on all of V, including every formal grading shift.

Apply it entrywise to Mat_I(V). Distributing tensor over the finite intermediate-state sum gives natural isomorphisms

\[
\Phi_{\mathrm T}(K)\star\Phi_{\mathrm T}(L)
 \simeq\Phi_{\mathrm T}(K\star L).
\tag{R7}
\]

On a path summand this is exactly (R6). Consequently its associator, unit and tensor-context compatibilities agree with the flattened ordered-path maps of F56. Every actual graded kernel morphism becomes a chain map. Isomorphisms and all equalities among the specified maps are preserved.

Every entry of every image kernel is pure of weight zero. Tensor products and finite sums of pure point complexes of weight zero remain pure of weight zero, either directly from (R4) or from the cohomological Kunneth decomposition. The closed-word trace object, the direct sum of the diagonal entries, is pure of weight zero and has the actual positive Laurent word trace evaluated at v=q^n.

Thus the whole F56 word category P_64, with all grading shifts, has this coherent arithmetic lift. The same holds for the faithful six-state category. This is a construction of coefficient complexes and their actual natural maps, rather than a match of the dimensions of two relation sides.

## 3. Half-step convention: the exact parity condition and state potentials

For the convention v=q^(n/2), choose the algebraic number lambda=sqrt(q)>0 in a specified complex embedding and an ell-adic realization in a finite coefficient field E. Let L_e be the one-dimensional Weil space with geometric Frobenius lambda^e. Choose the tensor identifications using the fixed basis of the tensor powers of L_1 and its dual. Then

\[
L_e\otimes L_f\simeq L_{e+f}.
\]

All complex conjugates of lambda^e have absolute value q^(e/2), so L_e is pure of weight e. Because ell does not divide q, these eigenvalues are ell-adic units. The one-dimensional Weil representations extend to continuous point Galois representations: a unit in the ring of integers of a finite ell-adic field lies in a profinite group, and the map from the integers defined by its powers extends to their profinite completion. This uses the point representation convention of BBD §5.1.11, pp. 127–128. The odd e lines are arithmetic coefficient lines; no geometric half-Tate motive is asserted.

Choose integers t_a for the states. Let Mat_t(V) be the full additive subcategory of kernels with

\[
(K_{ab})_e=0\quad\hbox{unless}\quad e\equiv t_b-t_a\pmod2.
\tag{R8}
\]

It contains the unit and is closed under convolution: the two parity conditions through an intermediate h add to e+f congruent to t_b-t_a. It is closed under even global grading shifts. An odd global grading shift generally leaves this subcategory.

Define entrywise

\[
(\Phi_t K)_{ab}
 =\bigoplus_e(K_{ab})_e\otimes
       L_e[-e+t_b-t_a].
\tag{R9}
\]

The summand is in cohomological degree i=e-t_b+t_a. This degree is even by (R8), and its cohomology weight is e. Its pure complex weight is consequently

\[
e-i=t_b-t_a.
\tag{R10}
\]

Every summand of an entry has the same complex weight, so the entry is pure of weight t_b-t_a. Its Euler trace has no minus sign:

\[
\operatorname{Tr}_{\mathrm{Euler}}
 (F^n;(\Phi_t K)_{ab})
 =\operatorname{ch}(K_{ab})(q^{n/2}).
\tag{R11}
\]

This parity condition is exact for an effective Laurent entry with the specified weight. Indeed the pure-point criterion of the F57 supplement says that a coefficient c_e>0 at lambda^e can occur in a pure weight t_b-t_a complex with this Euler trace only in degree e-t_b+t_a, whose parity must be even. The construction gives the converse. This necessity concerns the stated pure-entry comparison and does not assert that every arithmetic categorification must choose these entry weights.

For convolution, the two shifts add as

\[
(-e+t_h-t_a)+(-f+t_b-t_h)
=-(e+f)+t_b-t_a.
\tag{R12}
\]

Use the fixed tensor identification of L_e and L_f on every homogeneous path summand. Formula (R12) gives a tensorator

\[
\Phi_t(K)\star\Phi_t(L)\simeq\Phi_t(K\star L).
\tag{R13}
\]

It preserves every ordered state path and coefficient tensor. Associativity and the unit follow by the same direct pure-tensor check as for (R7). All cohomological factors in these images are even; reordering them in any specified coefficient comparison therefore introduces no Koszul signs. This is a strong monoidal functor on Mat_t(V), with its inherited kernel action.

The potentials telescope along every word. Thus a word entry (a,b) is pure of weight t_b-t_a, and every closed-word trace object is pure of weight zero. This conclusion is stronger than assigning unrelated scalar pure objects to individual words: the multiplication and relation maps are carried by the one functor (R9).

## 4. The actual 64-state parity assignment and defining maps

Set t=0 on every scalar-plus and scalar-minus state. On each N(delta) copy set t=(0,1); on each N(D-2) copy set t=(0,0). The diagonal D entries in (R3) have only degrees -2,0,2. The off-diagonal A_1 entries have odd degrees, and the off-diagonal A_2 entries have even degrees. Thus both actual kernels K_1,K_2 satisfy (R8), as does the unit.

For example on an N(delta) block,

\[
(\Phi_tK_1)_{21}=L_{-1}\oplus L_1[-2],
\qquad
(\Phi_tK_2)_{12}=L_{-1}[2]\oplus L_1.
\tag{R14}
\]

Their complex weights are -1 and +1, respectively. Their cohomological degrees are even, their Euler coefficients positive, and the two potential differences cancel on a closed path. The faithful six-state version uses the same potentials.

Let P_64^even be the additive word category generated by the unit and these kernels using convolution, finite sums and even global grading shifts. It is contained in Mat_t(V), so (R9) gives the claimed half-step lift. The restriction is deliberate: applying an odd global shift to a kernel changes its parity support and does not preserve (R8). The full-Tate lift of Section 2 does not have that restriction.

Here are the actual relation maps being transported. The source input is IV Theorem 11.16, equations (111)–(112), printed p. 65:

\[
P_i^2=DP_i,\qquad
P_1(P_2P_1-\delta^2)(P_2P_1-(D-2)^2)
=P_2(P_1P_2-\delta^2)(P_1P_2-(D-2)^2).
\tag{R15}
\]

The quadratic kernel isomorphism K_i star K_i to K_i tensor D preserves the initial edge and the final reset loop. In an m-fold power it retains the initial edge and the chronological list of m-1 D factors. If one moves all extracted D factors to the left, different reductions give the coefficient permutations already proved in F56; the two triple reductions differ by the transposition of the two loop factors. All these coefficient factors have even formal degrees, and their images have even cohomological degrees. The same permutations, not their negatives, therefore give the arithmetic comparisons. They satisfy the symmetric-group identities and the previously specified ordered comparison diagrams.

For the degree-five relation put U=A_1^2, V=A_2^2, S=U direct-sum V and T=U tensor V. Let V_1=K_121 and W_1=K_12121, with mirrored V_2,W_2. The positive rearrangement is the actual isomorphism

\[
W_1\oplus V_2S\oplus K_1T
 \simeq W_2\oplus V_1S\oplus K_2T.
\tag{R16}
\]

The F56 map is as follows. On an A_1 block the left list is
(K_1UU,K_2UU,K_2UV,K_1UV), and the right list is
(K_2UU,K_1UU,K_1UV,K_2UV). Send positions 1,2,3,4 to 2,1,4,3, with the identity on coefficient tensors. On an A_2 block the left list is
(K_1VV,K_2VU,K_2VV,K_1UV), and the right list is
(K_2VV,K_1VU,K_1VV,K_2UV). Send positions 1,2,3,4 to 3,4,1,2; use the coefficient flip U tensor V to V tensor U on the second and fourth maps. On plus states use termwise identities, and on minus states the zero isomorphism. Alternating-word identifications retain the chronological edge factors.

These are genuine graded linear isomorphisms with the explicit inverse obtained by reversing the maps. All U and V degrees are even. Hence the scalar coefficient objects U,V,S,T are central objects in the half-step parity category, and every intermediate kernel object and map in (R16) lies there. The odd object A_1 by itself is not an allowed central coefficient in that category; none is required for (R16). The off-diagonal occurrences of A_1 in (R3) are allowed by their state potentials.

Both (R7) and (R13) send the displayed maps to actual chain isomorphisms. The repeated maps on multiplicity copies commute with their matrix-unit maps because the copies have identical potentials and identical coefficient maps. Composition, tensor-context maps, the specified associator and symmetry comparisons, and disjoint-context interchange are preserved by functoriality.

This proves a coherent realization of the actual quadratic and degree-five relation maps. It does not assert a source-prescribed higher categorical presentation: IV gives an algebra presentation, not extra higher 2-relations among all possible rewrite paths. The concrete category has its stated ordinary coherence, with no gratuitous assertion that every unspecified loop of relation isomorphisms is the identity.

## 5. Exact transport of the formal bar

The F56 bar supplement uses the entrywise graded dual

\[
(\mathsf B K)_{ab,e}=(K_{ab,-e})^\vee
\tag{B1}
\]

without transposing the states. Its tensorator pairs ordered pure tensors by the product of their scalar pairings. This is a contravariant strong monoidal involution preserving the order of kernel multiplication, rather than a transpose-dual action adjoint.

For the full-Tate lift, ordinary point duality gives

\[
\Phi_{\mathrm T}(\mathsf B K)_{ab}
 \simeq\bigl(\Phi_{\mathrm T}(K)_{ab}\bigr)^\vee,
\tag{B2}
\]

because the dual of E(-e)[-2e] is E(e)[2e]. On every homogeneous tensor this identification is the product pairing used in the bar supplement. Thus it commutes with the tensorator and with the canonical double-dual evaluation map.

For the half-step lift write d_ab=t_b-t_a. A term of (R9) is U_e tensor L_e[-e+d_ab]. Its ordinary point dual is U_e^vee tensor L_-e[e-d_ab], while applying (R9) to its graded dual gives U_e^vee tensor L_-e[e+d_ab]. Therefore the exact formula is

\[
\Phi_t(\mathsf B K)_{ab}
 \simeq\bigl(\Phi_t(K)_{ab}\bigr)^\vee[2d_{ab}].
\tag{B3}
\]

In particular plain entrywise point duality is not the half-step bar when a nonzero potential difference is present.

Define on the even split kernel image

\[
(\mathsf B_t C)_{ab}=C_{ab}^\vee[2d_{ab}].
\tag{B4}
\]

This is contravariant strong monoidal. Indeed, finite duality commutes with the intermediate-state sum, and d_ah+d_hb=d_ab. The tensorator on the h summand is the order-preserving product pairing

\[
C_{ah}^\vee[2d_{ah}]\otimes C'_{hb}{}^\vee[2d_{hb}]
 \longrightarrow (C_{ah}\otimes C'_{hb})^\vee[2d_{ab}].
\]

All displayed shifts and all source cohomological degrees are even, so the pairing has no Koszul correction. The triple coherence diagram evaluates to the same product of three scalar pairings in the same path summand; the unit has d_aa=0 and its ordinary evaluation pairing. Naturality follows by precomposing the two factors with their respective linear maps.

The double-dual calculation is

\[
\mathsf B_t^2(C)_{ab}
 =(C_{ab}^\vee[2d_{ab}])^\vee[2d_{ab}]
 \simeq C_{ab}^{\vee\vee}.
\tag{B5}
\]

The canonical evaluation C to C^veevee is therefore its involution. On a pure tensor the monoidal double-dual comparison is the usual product evaluation, and evaluating the involution twice gives the original functional. This verifies both monoidal and involutive coherence, not only an objectwise isomorphism.

If C_ab is pure of weight d_ab, its point dual is pure of weight -d_ab; the shift [2d_ab] restores weight d_ab. Thus the corrected bar preserves the entry weights. It also remains in the even split image. Graded shifts reverse under this bar; in the half-step word category these are the allowed even shifts.

Consequently the specified self-dual forms and inverse-map identities of the F56 bar supplement transport through both lifts. In particular the unshifted named kernels are self-dual under the respective bar. The explicit relation maps are isometries for those forms, so under the self-dual identifications their bars are their inverse maps. In shifted or otherwise non-self-dual contexts the context itself is replaced by its bar; no self-duality of every shifted object is claimed. On Euler characters this is the actual substitution v to v^-1. It is neither a positive Hermitian polarization nor a transpose-dual adjunction, and it does not change the completion or adjoint exclusions in F56.

## 6. Gaussian geometric transport to pure derived complexes

In odd characteristic retain F53's Gaussian data on the affine line:

\[
L=\mathcal L_\psi(x^2),\qquad
G=H_c^1(\mathbb A^1_{\bar k},L),\qquad
J(C)=L\otimes\underline{C\otimes G^\vee}[1].
\tag{R17}
\]

The line G is pure of weight one. F53 supplies the product

\[
A\star_\psi B
=\underline{G(1)}[1]\otimes
 Rm_!(A\boxtimes B\otimes\mathcal L_\psi(2xy)),
\qquad m(x,y)=x+y,
\tag{R18}
\]

with its specified transported associator and symmetry, and the image unit J(E). Its symmetry is not the naive swap of two shifted Gaussian kernels.

Extend (R17) to the explicit split point complexes by the same derived formula, so

\[
\widetilde J\left(\bigoplus_i C_i[-i]\right)
 =\bigoplus_i J(C_i)[-i].
\tag{R19}
\]

This construction preserves the actual maps. To check the tensor comparison, expand the two finite split sums. On the (i,j) summand use F53's comparison J(C_i) star_psi J(C'_j) to J(C_i tensor C'_j), with total shift [-i-j]. The original comparison is natural; therefore these maps commute with the direct-sum maps and give

\[
\widetilde J(C)\star_\psi\widetilde J(C')
 \simeq\widetilde J(C\otimes C').
\tag{R20}
\]

The associativity and unit diagrams restrict on every homogeneous summand to the F53 diagram with its common total shift. The symmetry is its derived transported symmetry, including the coefficient Koszul sign. On the two constructions above the point cohomological degrees i,j are even, so that extra sign is one. This retains all the coefficient permutations in Section 4. In particular the existing Gaussian sign correction is not discarded by treating the kernel swap as the commutor.

If C_i is pointwise pure of weight w+i, then J(C_i) is perverse pure of weight w+i: its lisse coefficient in (R17) has weight w+i-1 and the shift is [1]. Hence J(C_i)[-i] is a pure derived complex of weight w. Finite sums of the same weight are pure. Thus (R19) preserves the stated purity of the split complexes, by BBD §5.1.8.

Apply (R19) entrywise, use direct sums over intermediate states and star_psi instead of point tensor product, and use the image unit on each diagonal. Equations (R7), (R13) and (R20) now give actual geometric derived-kernel relation maps, pure of weight zero in the full-Tate case and of weight t_b-t_a in the half-step case. The closed-word trace object is pure of weight zero. On this specified split image, RΓ_c is inverse to J by the Gaussian evaluation of F53 and commutes with the finite sums and shifts; therefore it recovers the point complexes and their Euler traces.

These shifted image objects need not be perverse in degree zero. F53's perverse statement applies to an unshifted Weil coefficient space; (R19) is a derived extension, not a claim that a multidegree coefficient complex remains in that perverse heart. The construction uses the same normalized affine-fiber trace and compact Kunneth as F53, rather than a new monoidality claim for arbitrary constructible complexes.

The formal bar of Section 5 transports to this specified Gaussian image by the same equivalence and its compact-cohomology inverse. It is not being identified with literal Verdier duality on the line: F53 explicitly distinguishes the internal coefficient dual, the Gaussian/Verdier dual and the separately specified reciprocal weight system.

## 7. Exact scope and remaining comparison

Pure complex weight zero is not the assertion that the entire ungraded cohomology has one Frobenius radius. For example

\[
\Phi_{\mathrm T}(\mathcal D)
=E(-2)[-4]\oplus E^{\oplus2}\oplus E(2)[4],
\tag{R21}
\]

while in the half-step convention a diagonal D entry is

\[
L_2[-2]\oplus E^{\oplus2}\oplus L_{-2}[2]
=E(-1)[-2]\oplus E^{\oplus2}\oplus E(1)[2].
\tag{R22}
\]

The total cohomology in (R21) has radii q^2,1,q^-2, and in (R22) it has radii q,1,q^-1. Each degree i has weight i, which is precisely why the complexes are pure of weight zero. The cohomological range of word objects grows with word length. No fixed finite Weil space carries all word traces by this construction.

The F50 pointwise bound and its separate dual bound are not improved by these degree assignments. In particular categorical duality does not supply that independent reciprocal estimate. No Hard Lefschetz operator, polarization, or canonical labels have been constructed. No identity with VIII's balanced lattices or designated canonical bases follows.

The full-Tate lift transports all the F56 word category and its existing completion limitations. The half-step construction transports the explicitly stated even-shift subcategory; no equality with the full Laurent shift category is asserted. The constructions do not change the F56 fact that Karoubi closure enlarges the chosen object cone and changes its simple labels. Nor do they turn the original word category into one closed under all transpose-dual adjoints.

The actual full-algebra rank-four N# block of F57 remains an obstruction to extending this particular pure-word-trace framework through all modules and ranks. In the half-step convention its displayed trace fails the pure-point criterion. In the full-Tate convention every root v^e=q^(en) has even weight 2e; purity of one complex weight would force all its visible Euler coefficients to have one parity sign. The same mixed-sign Laurent trace fails that condition as well. This does not exclude the source's signed/factored positivity or a mixed geometric model.

The positive result is therefore exact but limited: at rank three, the actual effective coefficient-kernel operations, their specified relation maps, and their positive traces admit coherent pure arithmetic and derived Gaussian realizations. It supplies one coefficient-object alternative to the fixed-operator trace obstructions. It does not establish the designated arithmetic/grading/basis comparison required for general GCT canonical positivity or an NSRH theorem.

## 8. Separate Grothendieck dictionary

The source formal grading is a split-torus character grading. SGA 3, I, 4.7.2–3 and cote 90, scan 17 supply the ordinary action framework; SGA 6, V, §§2–3 and cote 133, scan 18 supply representation and lambda/sigma language for the symmetric coefficient category. No lambda-ring structure is asserted on the noncommutative split Grothendieck algebra of matrix-kernel words.

The functors (R4) and (R9) prescribe an additional grading-to-cohomological-degree and grading-to-Frobenius comparison. They are not consequences of that archival representation dictionary. Their finite bounded coefficient complexes lie in the perfect-complex framework of SGA 6, I, Definition 4.7, pp. 121–122, and Example 4.8, p. 122. BBD §5.1.8, pp. 126–127, then proves the exact complex-weight statements. The Gaussian transport uses F53's existing compact-support geometry: Milne, Proposition 18.4, pp. 121–122; Theorem 22.1, Remarks 22.3(b),(d), and Proposition 22.5, pp. 135–137; and Theorem 24.1(a),(b), p. 144. It is a pure derived coefficient construction on the indicated image, not a new archival canonical-basis or positivity theorem.

## 9. Verification record

- Author mathematical check: the formulas (R4)–(R14), all purity shifts, tensorators, parity supports, and full-Tate/half-step distinction were reconstructed directly. The F56 ordered-path and degree-five maps were reread in full before applying the functors.
- Exact input read: the complete F53 definition, normalized-constant and Gaussian transport, symmetry correction, weights, and image-unit proof were reread from the current finding_F53.tex. The derived extension is proved here on the explicit split image.
- Bar refinement: the entire F56 formal-bar supplement was reread. The full-Tate dual formula, the half-step correction [2(t_b-t_a)], the tensorator, naturality, double-dual coherence and entry-weight calculation were reconstructed independently of an objectwise duality assertion. This is a newly added explicit proof in Section 5.
- Source framework: the original BBD and Milne contexts were read in the immediately preceding pure-point audit; their exact locators are retained above. No new source theorem beyond those or IV's already independently verified presentation is claimed.
- No formal proof assistant was used. No numerical computation substitutes for the functorial/coherence proof. A fresh independent review and final-fragment match are requested separately.
