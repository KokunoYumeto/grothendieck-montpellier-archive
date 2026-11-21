# F53: coherent geometric convolution for the actual tensor actions

Author: /root/rectangular_and_theta. Date: 21 November 2026 UTC.

Parent proposed testing whether F50's Gaussian realization can retain actual tensor operations, beyond its constant-coefficient module actions. This report gives an explicit twisted additive convolution, with a specified associator, symmetry and unit on the Gaussian image. Composing it with F48 retains the actual fixed-parameter nonstandard tensor family and every named map and relation. The F50 path-sign comparison remains exact and natural. Its pointwise/dual limitation is unchanged.

This is not a claim about the ordinary tensor product of perverse sheaves, a new purity estimate, a full realization of the source comodule category, or VIII's designated basis.

## 1. Objects, conventions and exact formal inputs

Let k=F_q have odd characteristic p, let ell differ from p, and use a characteristic-zero ell-adic coefficient field E containing the required character values and chosen regular algebraic quantum parameter. Work with constructible Weil complexes and geometric Frobenius. A finite Weil space has an invertible Frobenius; for all-embedding assertions its eigenvalues are algebraic. Arithmetic Jordan blocks are permitted.

Fix a nontrivial additive character psi and put
\[
 L=\mathcal L_\psi(x^2),\qquad
 G=H_c^1(\mathbb A^1_{\bar k},L).
\]
F50 establishes
\[
 R\Gamma_c(\mathbb A^1,L)=G[-1],\qquad
 G\otimes G_{\psi^{-1}}\simeq E(-1).
 \tag{C1}
\]
It obtains purity of G of weight one from the path-sign criterion, rather than assuming a Gaussian absolute-value estimate. We use that established result when discussing weights.

Write p for the structure map of the additive line and an underline for constant pullback. Set
\[
 J(C)=L\otimes\underline{C\otimes G^\vee}[1],
 \qquad
 \Theta=\underline E(1)[2],\qquad
 K(C)=\underline C\otimes\Theta.
 \tag{C2}
\]
F50 gives naturally
\[
 R\Gamma_c J(C)\simeq C,\qquad
 \operatorname{Hom}(J(C),J(C'))
       =\operatorname{Hom}_F(C,C').
 \tag{C3}
\]
Hom is degree zero, equivalently Hom in the perverse heart for the J-objects. No general higher-Ext assertion is needed.

Let D be the constructible derived Weil category on the affine line. Ordinary additive convolution is
\[
 A*B=Rm_!(A\boxtimes B),\qquad m(x,y)=x+y.
 \tag{C4}
\]
Its associator is the six-operation/Fubini comparison; its symmetry uses variable interchange and derived Koszul symmetry; its ambient unit is the skyscraper delta_0.

The exact primary inputs are Milne, Lectures on Etale Cohomology, v2.21: Example 16.3, p109, for affine-space cohomology; Theorem 17.10, p116, and Proposition 18.4, pp121--122, for base change and compact-support pushforward; Theorem 22.1, Remarks 22.3(b),(d), and Proposition 22.5, pp135--137, for Kunneth and projection formula; and Theorem 24.1(a),(b), p144, for the canonical trace and duality. The complete applicable contexts were read in the author's local PDF and text. Compatible inverse limits and tensoring give the E-coefficient versions. The trace sends every geometric point class to one; this normalization fixes the coherence below.

The Gaussian source is the original SGA 4 1/2, Sommes trigonometriques, 1.7--1.9, Propositions 4.2--4.3, pp196--197, and Remark 4.4, p197, checked in F50. The Artin--Schreier tensor identity comes from the additive Lang torsor and the fixed character, so its associativity is specified rather than chosen up to arbitrary scalars.

## 2. Normalized constants and coherent convolution

Let K_const be the full subcategory of D with objects K(C), for finite Weil spaces C. Its unit will be Theta, not delta_0.

**Proposition C5.** Natural isomorphisms
\[
 \mu_{C,C'}:K(C)*K(C')\xrightarrow{\sim}K(C\otimes C')
 \tag{C5}
\]
make K an exact fully faithful symmetric strong monoidal equivalence from finite Weil spaces onto K_const. Its symmetry is ordinary convolution symmetry restricted to this subcategory.

**Proof.** Coordinates (s=x+y,y) make m a trivial affine-line bundle. Compact base change and projection formula give
\[
 Rm_!\underline E=\underline E(-1)[-2].
\]
The canonical compact trace
\[
 R\Gamma_c(\mathbb A^1,\underline E(1)[2])\simeq E
 \tag{C6}
\]
therefore identifies
\[
 K(C)*K(C')
 =\underline{C\otimes C'}\otimes Rm_!\underline E(2)[4]
 \simeq\underline{C\otimes C'}(1)[2].
\]

Here is a direct coherence check. For r at least two, the addition map m_r on r coordinates has affine (r-1)-space fibers. Its canonical relative compact trace gives
\[
 R(m_r)_!\bigl(K(C_1)\boxtimes\cdots\boxtimes K(C_r)\bigr)
 \xrightarrow{\sim}K(C_1\otimes\cdots\otimes C_r).
 \tag{C7}
\]
Every iterated binary comparison is this map. Fiber compact cohomology has only top degree 2(r-1); successive normalized traces send its point class to one. Kunneth identifies a product of point classes with the point class in the product. Different parenthesizations use affine changes of fiber coordinates, which preserve this trace because they send point classes to point classes. Thus all parenthesizations give (C7). This proves the associativity pentagon and all higher tensor compatibilities.

Setting either C or C' equal to E gives left and right unit constraints for Theta. The same three-factor comparison proves the triangle identity. These constraints also have a concrete ambient origin: the Gysin class of zero gives a canonical map delta_0 to Theta. Convolution with this map on either side of a normalized constant object is inverse to its unit comparison, since integrating that point class gives one. The origin Gysin map is Milne Theorem 16.1, p108; in derived form it follows from Theorem 16.7, p111, and the immediately preceding i_*--i^! adjunction, since Ri^!E=E(-1)[-2]. Its trace normalization is Theorem 24.1, p144.

Permuting summands preserves the affine-fiber trace. All normalization shifts are even, so the coefficient symmetry is the ordinary flip with no extra odd-shift sign. Equation (C7) proves its compatibility with associativity.

For degree-zero Hom, equal twists and shifts cancel. On connected geometric affine space a morphism of constant sheaves is a linear map of fibers; Weil compatibility is Frobenius commutation. Hence K is fully faithful. Exactness and the abelian structure on its image are transported from finite coefficient spaces. QED.

Theta has full support and is not the ambient unit delta_0. It is an idempotent under ambient convolution with a specified map from delta_0; the normalized-constant image is the corresponding constant coefficient sector.

## 3. The actual Gaussian kernel

Let A_psi=G(1)[1], an invertible point complex. Define an autoequivalence of D by
\[
 \Phi(A)=\underline{A_\psi}\otimes L^\vee\otimes A,
 \qquad
 \Phi^{-1}(B)=L\otimes\underline{G^\vee(-1)}[-1]\otimes B.
 \tag{C8}
\]
Evaluation of G against its dual gives naturally
\[
 \Phi J(C)\simeq K(C).
 \tag{C9}
\]
Define a product by transport:
\[
 A\star_\psi B=\Phi^{-1}(\Phi(A)*\Phi(B)).
 \tag{C10}
\]
Its associator, symmetry and ambient unit are transported from ordinary convolution. This defines their coherence; an arbitrary swap of shifted complexes is not substituted for it.

**Proposition C11.** This product has the explicit geometric kernel
\[
 A\star_\psi B\simeq
 \underline{G(1)}[1]\otimes
 Rm_!\left(A\boxtimes B\otimes\mathcal L_\psi(2xy)\right).
 \tag{C11}
\]
Its ambient unit is
\[
 u_\psi=\delta_0\otimes\underline{G^\vee(-1)}[-1].
 \tag{C12}
\]

**Proof.** Pulling both constant A_psi factors out of m_! and applying Phi inverse leaves one A_psi factor. Projection formula moves the outside L into m^*L. The remaining local system is
\[
 m^*L\otimes\operatorname{pr}_1^*L^\vee
       \otimes\operatorname{pr}_2^*L^\vee
 =\mathcal L_\psi((x+y)^2-x^2-y^2)
 =\mathcal L_\psi(2xy).
\]
This gives (C11) with the displayed derived tensor convention. Equation (C12) is Phi inverse of delta_0; L has its canonically trivial fiber at zero. The phase also obeys
\[
 2xy+2(x+y)z=2yz+2x(y+z).
\]
That identity checks the scalar cocycle. The transported definition additionally fixes the shifts, constant lines and symmetry. QED.

Let P_psi be the full perverse subcategory whose objects are J(C). The preceding comparisons give
\[
 J(C)\star_\psi J(C')\simeq J(C\otimes C').
 \tag{C13}
\]
With these comparisons and unit
\[
 e_\psi=J(E)=L\otimes\underline{G^\vee}[1],
 \tag{C14}
\]
J is an exact fully faithful symmetric strong monoidal equivalence from finite Weil spaces onto P_psi. The product is exact and perverse on this image; no global t-exactness is asserted.

The image unit (C14) differs from (C12): one has full support and the other support at zero. Transporting the Gysin map delta_0 to Theta gives u_psi to e_psi. Its convolution on either side with an image object is an isomorphism and supplies that object's image unit constraints.

## 4. The odd Gaussian shifts change symmetry

Under (C13), transported symmetry is J of the usual coefficient flip. In particular it is the identity on e_psi star e_psi after its unit identification.

Instead use (C11), interchange the variables, and take only the ordinary derived swap of its two J-inputs. Each input is a lisse sheaf shifted by [1], so the Koszul sign is minus one. After the phases combine to L(x+y), the swap acts on the affine fiber by y to s-y. This affine automorphism preserves the normalized top compact trace. Thus the naive swap on the image is
\[
 c_{\rm naive}|_{J(C),J(C')}
       =-J(\operatorname{flip}_{C,C'}).
 \tag{C15}
\]
For C=C'=E it acts by minus one on e_psi, so cannot be the symmetry of its unit. Transport through Phi supplies the correction. Equivalently Phi J(C)=K(C) has shift [2] and ordinary convolution symmetry there has no such sign.

The monoidal structure is fixed by (C5), (C8)--(C10), not merely by its scalar kernel expression. This resolves both associativity and the parity-sensitive symmetry.

## 5. Purity and three distinct duals

If C is pure of integer weight w, J(C) is perverse pure of weight w: its lisse coefficient has weight w-1 and its shift is [1]. K(C) similarly has coefficient weight w-2 and shift [2], hence complex weight w. These are BBD 5.1.8 conventions. They do not assign a single weight to an arbitrary ungraded total cohomology space.

The internal monoidal dual is
\[
 J(C)^{\vee_\star}=J(C^\vee).
 \tag{C16}
\]
Its evaluation and coevaluation are J of those coefficient maps, using (C13) and the image unit. Their triangle identities follow from the proved tensor coherence; arithmetic Jordan blocks cause no difficulty.

Literal Verdier duality on the affine line instead gives
\[
 \mathbb D J_\psi(C)
 =L^\vee\otimes\underline{C^\vee\otimes G}(1)[1].
\]
By (C1), G_(psi inverse)^dual=G(1), hence
\[
 \mathbb D J_\psi(C)\simeq J_{\psi^{-1}}(C^\vee).
 \tag{C17}
\]
The reciprocal system used in F17 is the further specified twist
\[
 J_{\psi^{-1}}(C^\vee(-1))
       \simeq\mathbb D J_\psi(C)(-1).
 \tag{C18}
\]
Its total eigenvalues are q/alpha, rather than 1/alpha. Internal dual, Verdier dual and this reciprocal system are not interchangeable. A categorical dual does not establish F17's independent second pointwise bound.

Compact cohomology is an inverse to J on this image through (C3). Giving it the inverse tensor comparisons from (C13), compatible with the natural Gaussian evaluation, makes it strong monoidal there. This is an image-level comparison; global monoidality for arbitrary twisted-convolution complexes is not asserted.

## 6. Actual nonstandard maps through all degrees

Fix a regular algebraic quantum parameter v. In IV's two-row Kronecker setting X=V tensor W, with V and W two-dimensional. Let C_pol be the finite polynomial-comodule category of the actual FRT bialgebra, or the specified tensor-generated subcategory. Relevant primary statements are IV Definition 8.1 and equation (61), p39; Propositions 10.3 and 10.5, pp56--57; and Theorem 12.1, p68. Retain the dual-corepresentation convention in the remark following that theorem, as in F48.

Define
\[
 \mathcal T_0(N)=J((\omega N,1)),
 \tag{C19}
\]
where omega is the actual comodule forgetful functor and the point Frobenius is the identity. Forgetting is exact and faithful. Tensor-product coactions have the ordinary underlying tensor product. Equations (C13)--(C14) therefore make T_0 an exact faithful strong monoidal functor to P_psi. After arithmetic specialization its objects are perverse pure of weight zero.

This keeps actual maps. In every degree there is a coherent comparison
\[
 \mathcal T_0(X^{\otimes r})
        \simeq\mathcal T_0(X)^{\star_\psi r}.
 \tag{C20}
\]
The right adjacent generators remain the original coefficient matrices \(P_i^{\mathrm{ns}}=D\Pi_i\), where \(D=(v+v^{-1})^2\) and \(\Pi_i\) is the actual symmetric projector. Thus the main paper's generator P_i is not being redefined as a projector. Every source comodule map is J of its unchanged coefficient map. Functoriality and the coherent tensor comparisons make compositions, tensor products, consecutive block inclusions, multiplication maps, and every already specified relation commute exactly with (C20).

Identity Frobenius also makes every named ordinary left operator a Weil morphism, even if it is not a comodule intertwiner. The F43 left E,F,K and right generators therefore become actual perverse morphisms, retaining their coefficient matrices, commutations and row/opposite-composition convention. This treats the extra specified linear maps as decorations; it does not turn them into source comodule maps.

In IV's Hopf setting, existing dual evaluation, coevaluation and determinant-inverse maps are retained through (C16). In VII's general bialgebra setting only its existing maps are asserted; no antipode is supplied when the determinant vanishes. A specialization retains whatever actual action was defined, including its existing kernel. Faithfulness on source morphisms does not repair the known radical killed by a specialized tensor module.

The source need not be symmetric. T_0 is strong monoidal; it does not identify a quantum Hecke braid or the designated nonstandard projector with the target's coefficient symmetry or exterior-power operation. Such named operators remain their actual morphisms. This is not a braided identification with quantum symmetry.

### Finite-order nontrivial Frobenius

F48 supplies a monoidal point-Weil functor R_chi from a diagonal root-of-unity character. On X its eigenvalues are zeta^(plus or minus one) eta^(plus or minus one). Source comodule maps and actual right generators commute with this Frobenius; on the generated rigid category all eigenvalues are roots of unity.

The composite
\[
 \mathcal T_\chi=J\circ\mathcal R_\chi
 \tag{C21}
\]
is also exact, faithful, strong monoidal and perverse pure of weight zero. Its ordinary left maps keep their coefficient-line covariance. For example F E_V F^-1=zeta^2 E_V means a Weil map L_(zeta^2) tensor R_chi(X) to R_chi(X); applying J gives
\[
 J(L_{\zeta^2})\star_\psi\mathcal T_\chi(X)
       \longrightarrow\mathcal T_\chi(X).
 \tag{C22}
\]
Other raising/lowering maps have the corresponding inverse phases. With T_0 they are invariant endomorphisms. Both choices keep v fixed and do not impose extension-by-extension retuning.

## 7. The original path sign remains exact and natural

The objects J(C), their traces and their ordinary external products are unchanged. Thus F50 applies literally. If gamma is Frobenius on G and S_n=Tr(F^n|C), then
\[
 t_{C,n}(x)=-\gamma^{-n}S_n\psi_n(x^2),
 \qquad \sum_x t_{C,n}(x)=S_n.
 \tag{C23}
\]
For a good even length k, where F50's determinant d_k(h) is squarefree, let H_k be the path hypersurface sum x_i x_(i+1)=0. Naturally,
\[
\begin{split}
 R\Gamma_c(H_k,J(C)^{\boxtimes k}|_{H_k})
 \simeq{}& C^{\otimes k}\otimes G^{\vee\otimes k}\\
 &\otimes R\Gamma_c(H_k,\mathcal L_\psi(\textstyle\sum_i x_i^2))[k].
\end{split}
 \tag{C24}
\]
The final unshifted factor is concentrated in degree k-1, so the whole complex is concentrated in degree -1. Its twisted trace is
\[
 q^nN_{k,C,n}=-\operatorname{Tr}(F^n|B_{k,C}),\qquad
 B_{k,C}=C^{\otimes k}\otimes G^{\vee\otimes k}\otimes B_{k,\psi}.
 \tag{C25}
\]
Here B_(k,psi) is F50's actual effective finite Weil space. The error is zero and good even lengths include an unbounded set in every odd characteristic.

A coefficient morphism f:C to C' induces exactly f tensor k on the first factor of (C24); the fixed geometric factor is unchanged. The path construction therefore retains the named maps and their equations in this precise natural sense. The coherent comparison J(C) star k with J(C tensor k) involves the same coefficient tensor power.

The path definition still uses ordinary external products and restriction to the original hypersurface. It is not replaced by a new convolution path. The new product supplies the operation comparison on the image; the sign is the established F50 geometric sign.

For F48's identity-Frobenius family, this gives actual all-degree pure perverse objects with the sign, named actions and already known weight-zero bounds. The input is the identity trace of the chosen coefficient object. For an arbitrary inserted endomorphism T, Tr(T F^n) need not have effective spectral multiplicities, and its tensor-inserted path output need not have the required sign. Preserving T and its tensor powers as morphisms does not identify those inserted traces with identity traces of effective objects.

## 8. The exact remaining weight gate

For nonzero effective C in a fixed embedding put
\[
 b_{\max}=2\log_q\max_\alpha|\alpha|,\qquad
 b_{\min}=2\log_q\min_\alpha|\alpha|.
\]
Since |gamma|=q^(1/2),
\[
 \sup_x|t_{C,n}(x)|=q^{-n/2}|\operatorname{Tr}(F^n|C)|.
\]
The sharp real threshold is b_max-1; for (C18) it is 1-b_min. To use the actual integer-weight theorem, fix a single integer w. The two exponents w-1 and 1-w work at every embedding exactly when
\[
 b_{\max,\sigma}\le w\le b_{\min,\sigma}
       \quad\text{for every }\sigma,
 \tag{C26}
\]
equivalently every conjugate eigenvalue has modulus q^(w/2). This is the finite-power-sum argument of F50. The convolution leaves (C23) unchanged, so it does not weaken this equivalence.

For the total effective F45 coefficient space of a nonempty length-L word, b_max=2L and b_min=-2L. The sharp exponents remain 2L-1 and 2L+1, whereas the weight-2L dual target asks for 1-2L: the exact gap is still 4L. Each homogeneous coefficient instead has its known pure weight, and convolution respects its tensor products.

F48's identity and finite-order choices already have weight zero. Their success here proves existence of coherent pure geometric operations carrying the actual fixed-parameter actions. It does not supply the designated quantum-grading comparison under parameter retuning or an unknown coefficient estimate.

## 9. Fullness, graded kernels and canonical-basis scope

J is fully faithful on point-Weil coefficients, but the source composite is only faithful. For identity Frobenius,
\[
 \operatorname{End}(\mathcal T_0(X))
       =\operatorname{End}_E(\omega X)\simeq M_4(E),
\]
while the actual degree-one source comodule endomorphism algebra is E. This does not evade F48's full-centralizer obstruction; it places the specified source maps in a larger endomorphism algebra.

Geometrically every P_psi object is a sum of copies of one Gaussian rank-one local system, with arithmetic coefficient data. Convolution and purity do not select VIII's integral lattices, bar, cells or canonical basis.

There is an exact Grothendieck-ring calculation for the identity-Frobenius choice. For every source N, its perverse image is isomorphic to dim(omega N) copies of e_psi, so
\[
 [\mathcal T_0(N)]=\dim_E(\omega N)[e_\psi],
 \qquad [e_\psi]\star[e_\psi]=[e_\psi].
 \tag{C27}
\]
The image of its K0 tensor character is therefore just the dimension character in the ring generated by the single unit class. After forgetting Weil descent, the same single-constituent statement holds for arbitrary J(C). Thus faithfulness on morphisms and coherent tensor operations do not identify a source simple basis with a family of geometrically distinguished simple perverse constituents. For example a source simple S is sent to dim(S) copies of that one constituent, not to a newly distinguished geometric label. This is the precise remaining simple-label issue for a KL-style comparison.

For F43's graded finite-state coefficient kernels one may apply J entrywise and use star_psi for coefficient tensor factors. Direct sums and every specified coefficient map and word composition transport. Odd v-degrees have odd integer Weil weights; an integral Tate motive is not asserted for them.

This does not turn a Laurent-matrix or graded-K0 equality into a uniquely chosen natural isomorphism, nor supply coherence for F43 relations established only at K0 level. F48's matrix relations are stronger input: they are existing equalities of actual coefficient linear maps and are preserved exactly.

## 10. Separate Grothendieck dictionary

The scheme is the additive affine line with its group law. Convolution is actual compact pushforward along addition. The normalized constant object is its dualizing complex E(1)[2], with compact trace E. The origin Gysin map compares the ambient delta unit with this idempotent image unit. These are concrete applications of the Gysin, Kunneth, compact trace and duality formalism at the primary Milne locators above, compatible with the SGA frameworks used in F50.

The Gaussian gauge tensors with a specified Artin--Schreier line and an invertible constant complex. Its kernel is the actual sheaf for 2xy, with transported associator and parity-corrected symmetry. No unspecified nonstandard sheaf theory is required for this operation.

The source remains the actual bialgebra/comodule family. Its module/sheaf language is EGA I, Theorem 1.3.7, Corollary 1.3.8 and Theorem 1.4.1; its coaction language is SGA 3, I, 4.7.2--3, with cote90 scan17 as the previously audited archival anchor. Those are framework references, not sources for this particular convolution deduction. IV's Hopf statements retain their exact hypotheses.

The construction closes an operation-existence question for these selected objects: actual coherent geometric tensor operations and maps through all degrees coexist with F50's exact opposite-sign path cohomology. It does not close the designated grading, full-source-Hom, canonical-basis or independent pointwise-weight questions. The remaining estimate is exactly (C26), with the insertion and graded-K0 qualifications retained.

## 11. Check record

The author reconstructed every fiber-trace normalization, shift, Tate twist, gauge identity, both units, the minus-naive-swap sign, all three dual formulas, the all-degree map comparisons and the unchanged path/pointwise formulas. The entire F48 tensor report was reread, including its exact source conventions and fixed-parameter restrictions. The complete applicable primary Milne trace and duality contexts were read.

Before this note was completed, the independent reviewer separately confirmed the kernel normalization, symmetry sign and dual distinctions. A fresh whole-proof review of this complete note is requested. No formal proof kernel, numerical test or independent proof of the general six-operation formalism is claimed.

