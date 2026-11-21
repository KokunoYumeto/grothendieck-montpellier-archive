# Ordinary plethysm and Kronecker multiplicities as pure Satake Weil spaces

**Run and status.** Prepared by GPT-6 Astra Pro, effort not exposed, for `GCT_NSRH_20261121_grothendieck_dictionary`; 21 November 2026, Europe/Berlin (20 November UTC). This note states a classical construction using geometric Satake and BBD. It does not claim a new proof of those external theorems, a nonstandard quantum realization, or the positivity conjectures of GCT VIII. All weights below use unnormalized intersection complexes; no square root of a Tate twist is introduced.

## 1. Sources and conventions

Fix a finite field `F_q`, an algebraic closure `Fbar_q`, and a prime `ell` distinct from its characteristic. Coefficients are `Qbar_ell`. Frobenius means geometric Frobenius. A Tate twist `Qbar_ell(-1)` has eigenvalue `q` and weight2. The shift convention for complexes is BBD’s: if `L` is a pure lisse sheaf of weight `a`, then `L[t]` is pure of weight `a+t`.

For split `G=GL_r`, write `Gr_G` for its affine Grassmannian and `Gr_alpha` for the Schubert orbit indexed by a dominant coweight `alpha`. For a partition of length at most `r`, use the convention under which `IC_alpha` corresponds to the irreducible polynomial representation `S_alpha(V)` of the dual `GL_r`. Put

\[
D_\alpha=\dim\operatorname{Gr}_\alpha
=\langle2\rho,\alpha\rangle
=\sum_{i=1}^r(r+1-2i)\alpha_i.
\]

The support `X_alpha=closure(Gr_alpha)` is reduced and projective. Define

\[
\operatorname{IC}_\alpha
=(j_\alpha)_{!*}\overline{\mathbf Q}_\ell[D_\alpha]
\]

with the natural Weil structure inherited from the constant sheaf. It is perverse and pure of weight `D_alpha`, not weight zero.

### Primary locators checked

The official published primary source is T. Richarz, *A new approach to the geometric Satake equivalence*, Documenta Mathematica19 (2014),209–246, [publisher PDF](https://ems.press/content/serial-article-files/26224?nt=1). Its numbering differs from arXiv1207.5314v2.

| Input | Exact published locator |
|---|---|
| Convolution is perverse and equivariant | Richarz Theorem3.1(i), p214 |
| Symmetric tensor structure over the ground field | Richarz Theorem3.1(ii), p214; proof pp226–227 |
| Modification of commutativity by the parity of a component; compatibility with Galois action | Richarz proof of Theorem3.1, pp226–227 |
| Geometric semisimplicity and the simple IC objects | Richarz Proposition4.1, p227 |
| Identification of the Tannakian group with the dual group | Richarz Theorem5.1, p230, and proof |
| Finite projective twisted Schubert product and its proper convolution morphism | Richarz pp231–232, preceding Corollary5.3 |
| Semismallness | Richarz Corollary5.3, p232 |
| Twisted external IC is the IC of the twisted product | Richarz Lemma5.4, proof, p232 |
| Geometric tensor-product multiplicity basis from maximal-dimensional fiber components | Richarz Lemma5.4, p232 |
| Galois descent of the tensor category | Richarz Theorem6.1, p235 |

The weight arguments use the original A. Beilinson, J. Bernstein and P. Deligne, *Faisceaux pervers*, Astérisque100 (1982), [Numdam original](https://www.numdam.org/item/AST_1982__100__1_0/):

| Input | Exact locator |
|---|---|
| Fully faithful passage to geometric perverse sheaves with Frobenius; image stable under subquotients | BBD5.1.2, p123 |
| Weight convention; purity criterion for complexes of lisse sheaves | BBD5.1.8, pp126–127 |
| Stability of the two weight bounds under the six operations used here | BBD5.1.14(i),(i*), p128 |
| Perverse subquotients preserve both weight bounds | BBD5.3.1, p134 |
| Intermediate extension preserves purity | BBD5.3.2, p135, **second proof**, which explicitly removes the affine-immersion restriction of the first displayed statement |
| Geometric semisimplicity of pure perverse sheaves | BBD5.3.8, p138 |
| Proper direct image preserves purity | BBD Remark5.4.9, p143 |

The relevant statements and their surrounding proof arguments were read in the original or publisher PDFs. The general BBD and Satake theorems are invoked here, not independently reproved. Web retrieval IDs are `turn106538141view0` and `turn790512219view0`–`turn790512219view2` for Richarz. Local research copies are `primary_sources/Richarz_Satake_2014.pdf/.txt` and `primary_sources/BBD.pdf/.txt`.

## 2. A canonical multiplicity-weight lemma

**Lemma SP1.** Let `P` be a Weil perverse sheaf pure of weight `w`, whose underlying geometric perverse sheaf is a finite semisimple direct sum of simple objects `IC_alpha`. Assume each support, smooth open stratum and the chosen natural Weil structure on `IC_alpha` are defined over `F_q`. Set

\[
M_\alpha=\operatorname{Hom}_{\mathrm{Perv}(X_{\overline{\mathbf F}_q})}
(\operatorname{IC}_\alpha,P).
\]

Equip `M_alpha` with the conjugation action of Frobenius through the two given Weil structures. Then `M_alpha` is a finite-dimensional Weil space pure of weight `w-D_alpha`.

**Proof.** Geometric semisimplicity and absolute simplicity of the `IC_alpha` give the canonical evaluation isomorphism

\[
\bigoplus_\alpha\operatorname{IC}_\alpha\otimes M_\alpha
\xrightarrow{\sim}P.
\]

Explicitly, if `F_A:Frob^*A -> A` denotes a Weil structure, the action on a morphism is

\[
f\longmapsto F_P\circ\operatorname{Frob}^*f\circ F_{\operatorname{IC}_\alpha}^{-1}.
\]

The displayed evaluation is Frobenius-equivariant by this definition. Since the individual supports and the `IC_alpha` are defined over `F_q`, Frobenius preserves each isotypic summand. Thus the evaluation is a Weil isomorphism, rather than an arbitrarily chosen geometric splitting. BBD5.1.2 supplies the corresponding descent statement in the category of sheaves on the finite-field scheme. In particular the isotypic summand is an actual perverse subobject and quotient of `P`; BBD5.3.1 makes it pure of weight `w`.

Regard that summand as an object on its own closed support and restrict to the smooth open orbit `Gr_alpha`. There it is the constant lisse Weil space `M_alpha[D_alpha]`: the natural `IC_alpha` restricts to `Qbar_ell[D_alpha]` with Frobenius1. Open restriction preserves both weight bounds because its ordinary and extraordinary pullbacks agree, `j^*=j^!` (BBD5.1.14). BBD5.1.8 then says precisely that `M_alpha` has weight `w-D_alpha`. This also follows after choosing the rational point `t^alpha` on the split Schubert orbit. This proves the lemma. No arithmetic semisimplicity, diagonalization of Frobenius, or half Tate twist has been assumed. ∎

**Support detail.** A pure summand supported on a closed subscheme is pure when regarded as an object of that closed subscheme: closed pushforward is fully faithful, is exact for the perverse structure, and preserves and detects the two weight bounds. One can equally restrict first to the complement of its boundary inside the original ambient scheme. This avoids treating a locally closed immersion as if it were an open immersion of the whole affine Grassmannian.

## 3. Plethysm

**Proposition SP2.** Let `mu` be a partition of length at most `r`, let `nu` be a partition of `d>=1`, and let `lambda` be a partition of length at most `r`. There is an actual finite-dimensional Weil space `M_lambda;mu,nu` with

\[
\dim M_{\lambda;\mu,\nu}
=\dim\operatorname{Hom}_{\mathrm{GL}_r}
\bigl(S_\lambda(V),S_\nu(S_\mu(V))\bigr),
\]

pure of weight

\[
w_{\lambda;\mu,\nu}=dD_\mu-D_\lambda.
\]

If the multiplicity is zero, the zero space is understood. For nonzero multiplicities, `|lambda|=d|mu|`, and hence

\[
w_{\lambda;\mu,\nu}
=2\bigl(n(\lambda)-d\,n(\mu)\bigr),
\qquad n(\alpha)=\sum_i(i-1)\alpha_i.
\]

**Proof.** Form the `d`-fold twisted Schubert product `X_mu twisted-times ... twisted-times X_mu` and the restricted convolution map `m` to `X_{d mu}`. These are finite-type projective varieties, and `m` is proper. The twisted external product of `d` copies of `IC_mu` is the intersection complex of this twisted product, whose dimension is `dD_mu` (Richarz Lemma5.4, proof). The arithmetic normalization matters: on the dense smooth twisted orbit, descent of the natural constant sheaves gives the natural constant Weil sheaf shifted by `dD_mu`. Thus this is the same IC Weil structure, not merely an unspecified geometric IC isomorphism. BBD5.3.2 gives purity of weight `dD_mu`.

Consequently

\[
K=\operatorname{IC}_\mu^{\star d}
=Rm_*\bigl(\operatorname{IC}_\mu\widetilde\boxtimes\cdots
\widetilde\boxtimes\operatorname{IC}_\mu\bigr)
\]

is pure of weight `dD_mu` by BBD Remark5.4.9. It is perverse by Richarz Theorem3.1(i). These facts apply on the finite projective supports, so no unqualified theorem about cohomology of an infinite-dimensional ind-scheme is being used.

Use the **modified symmetric** Satake commutativity constraint, for which the total cohomology fiber functor is symmetric monoidal into ordinary vector spaces. Its construction is over `F_q`; hence the resulting `S_d` action on `K` commutes with Frobenius.

Choose a primitive idempotent `e_nu` in the `nu` block of the split semisimple rational algebra `Q[S_d]`. It acts on the Specht module `[nu]` with rank1 and annihilates all other Specht types. The image

\[
P_\nu=\operatorname{im}(e_\nu:K\longrightarrow K)
\]

exists in the abelian perverse category and is an actual direct summand. Its Weil structure is inherited because the projector commutes with Frobenius. By BBD5.3.1, `P_nu` is pure of weight `dD_mu`.

Under geometric Satake, `K` corresponds to `S_mu(V)^{tensor d}` and `e_nu K` to `S_nu(S_mu(V))`. To see the projector factor explicitly, for any characteristic-zero vector space `U`,

\[
U^{\otimes d}\cong\bigoplus_{\tau\vdash d}[\tau]\otimes S_\tau(U).
\]

A primitive `e_nu` has one-dimensional image on `[nu]`, so its image is one copy of `S_nu(U)`. In contrast the central idempotent of the whole `nu` block gives `[nu] tensor S_nu(U)` and therefore multiplies every desired multiplicity by `dim[nu]`.

The underlying geometric object `P_nu` is semisimple, either by the Satake category’s semisimplicity or by BBD5.3.8. Define

\[
M_{\lambda;\mu,\nu}=\operatorname{Hom}_{\mathrm{geom}}
(\operatorname{IC}_\lambda,P_\nu)
\]

with the conjugation Frobenius action. Satake gives the stated dimension, and SP1 gives weight `dD_mu-D_lambda`. The formula using `n(alpha)` follows from `D_alpha=(r-1)|alpha|-2n(alpha)` and the equality of polynomial degrees. ∎

This construction uses a chosen primitive idempotent. Different choices give isomorphic multiplicity spaces but no preferred positive basis follows from that fact. The rational projector can involve negative coefficients; purity of its image depends on its being a Frobenius-stable summand, not on coefficient signs.

## 4. Kronecker coefficients

**Proposition SP3.** Let `lambda,mu,nu` be partitions of `d>=1`, with `length(lambda)<=m` and `length(mu)<=n`. There is an actual finite-dimensional Weil space `N_lambda,mu;nu` whose dimension is the ordinary Kronecker coefficient `g(lambda,mu,nu)`, pure of weight

\[
d(m+n-2)-D_\lambda^{(m)}-D_\mu^{(n)}
=2\bigl(n(\lambda)+n(\mu)\bigr).
\]

**Proof.** Use the affine Grassmannian of the split product group `GL_m x GL_n`, and put

\[
A=\operatorname{IC}_{(1)}^{(m)}\boxtimes
\operatorname{IC}_{(1)}^{(n)}.
\]

It is the naturally normalized IC on the product Schubert support, is pure of weight `m+n-2`, and corresponds under geometric Satake to `V tensor W`. Apply the construction of SP2 to `A^{star d}` and a primitive rational idempotent `e_nu`. Its image `P_nu` is a pure perverse Weil sheaf of weight `d(m+n-2)` whose geometric Satake representation is `S_nu(V tensor W)`.

The simple object `IC_lambda external IC_mu` has weight `D_lambda^(m)+D_mu^(n)` and corresponds to `S_lambda(V) tensor S_mu(W)`. Thus

\[
N_{\lambda,\mu;\nu}=
\operatorname{Hom}_{\mathrm{geom}}
(\operatorname{IC}_\lambda\boxtimes\operatorname{IC}_\mu,P_\nu)
\]

has dimension `g(lambda,mu,nu)` by the characteristic-zero Schur–Weyl decomposition of `S_nu(V tensor W)`. SP1, applied to the product group, gives the claimed weight. Expanding the two dimension formulas and using `|lambda|=|mu|=d` gives the final equality. All purity and descent assertions use the same proper finite-type convolution argument as SP2. ∎

The weight in this formula does not depend on `nu`, although the dimension generally does. A pure realization of this kind is therefore not by itself the grading sought by a nonstandard canonical-basis conjecture.

## 5. A signed component line in the smallest nontrivial example

**Proposition SP4.** For `G=GL_2`, let `mu=(1)` and let `K=IC_mu star IC_mu`. The determinant multiplicity space

\[
M=\operatorname{Hom}_{\mathrm{geom}}(\operatorname{IC}_{(1,1)},K)
\]

is `Qbar_ell(-1)`, and the transposition in the modified symmetric Satake `S_2` action acts on it by `-1`. Consequently no basis of this one-dimensional space is permuted by that action.

**Proof.** The Schubert variety `X_(1)` is the minuscule `P^1`, of dimension1. The two-step convolution variety is an iterated `P^1` bundle, hence smooth of dimension2; its IC is the constant Weil sheaf shifted by2. At the determinant lattice `tO^2`, the convolution fiber consists of the intermediate lattices

\[
tO^2\subset L\subset O^2,
\qquad \dim(L/tO^2)=1.
\]

These are exactly the lines in the two-dimensional space `O^2/tO^2`, so the fiber is `P^1` over `F_q`.

The determinant summand is supported at a point. The intermediate extension of the other, positive-dimensional simple constituent has no degree-zero stalk contribution at that point, by the no-boundary-quotient property of intermediate extension. Proper base change therefore identifies the determinant multiplicity with

\[
H^0((Rm_*\overline{\mathbf Q}_\ell[2])_{tO^2})
=H^2(\mathbf P^1,\overline{\mathbf Q}_\ell)
=\overline{\mathbf Q}_\ell(-1).
\]

The last cohomology calculation is the projective-line formula; one checked primary-author source is J. S. Milne, *Lectures on Étale Cohomology*, v2.21 (2013), Example16.3, p109. Its Frobenius eigenvalue is `q`, consistent with SP1: `2D_(1)-D_(1,1)=2`.

The modified symmetric Satake equivalence identifies the transposition with the ordinary tensor flip on `V tensor V`. The determinant summand is `wedge^2 V`, on which that flip is `-1`. Since the multiplicity has dimension1, the only permutation of a one-element basis is the identity. In characteristic zero `-1` is distinct from `1`; no such permuted basis exists. ∎

This is compatible with Richarz’s geometric component basis for convolution multiplicities. The determinant fiber has one top-dimensional component, and the Satake transposition negates its class. The issue is compatibility of the action with a positive or permuted basis. It does not contradict the existence of the component basis, nonnegativity of ordinary dimensions, or purity of the Young-projector image. In this example the symmetric projector kills the line and the alternating projector retains it.

## 6. Precisely what has and has not been supplied

The constructions give actual ordinary finite-field geometric objects, proper convolution maps, Frobenius-stable rational projectors, and pure multiplicity Weil spaces with the required classical dimensions. They are stronger than simply declaring an abstract vector space with Frobenius equal to a scalar. Their proof, however, already invokes geometric Satake and Weil-II/BBD purity. It does not establish those inputs by Alpöge’s sign-only mechanism.

The following additional claims do not follow from SP1–SP4:

- a basis-preserving comparison with a nonstandard quantum-group canonical basis or its deformation parameter;
- a positive cycle or component interpretation of the image of every Schur projector;
- a Frobenius-equivariant permutation action on a component basis;
- a lattice-polytope formula with the algorithmic bounds required in PH1;
- a complexity-theoretic obstruction or lower bound.

A geometric interpretation of an ordinary multiplicity and a positive combinatorial rule for the nonstandard algebra are different requirements. SP4 isolates an explicit action obstruction to one direct permutation-basis route, while leaving other constructions open.

## 7. Separate nilpotent-invariance source check

For ordinary étale cohomology, the directly verified formal statement is the [Stacks Project, Proposition59.45.4, tag03SI](https://stacks.math.columbia.edu/tag/03SI). A universal homeomorphism, including a closed immersion defined by a nilpotent sheaf of ideals, induces equivalent small étale topoi and identical cohomology for corresponding abelian sheaves. The underlying category equivalence is [Theorem59.45.2, tag04DZ](https://stacks.math.columbia.edu/tag/04DZ), which cites EGAIV18.1.2. This applies degreewise to torsion coefficient systems and hence to the usual l-adic constructions. If the immersion is defined over `F_q`, the comparison respects the natural Frobenius action.

An original scan of SGA4 ExposéVIII is indexed at `https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/originaux/SGA4-VIIIo.pdf`; its search-index text identifies Theorem1.1, printedp367, on topological invariance. Until the actual scan is retrieved and read, the exact SGA corollary/example locators should not be claimed as checked. The verified Stacks proposition suffices for the assertion used here. Web source refs: `turn392773452view1` and `turn392773452view2`.

## 8. Motivic refinement: these particular multiplicity spaces are Tate

**Corollary SP5 (using motivic Satake).** The constructions of SP2 and SP3 lift to rational intersection motives in the compact motivic Satake category over `F_q`. Their coefficient motives on the `lambda` (respectively `(lambda,mu)`) stratum are direct sums of a single integral Tate twist. With the notation of SP2, put

\[
h_{\lambda;\mu,\nu}=\frac{dD_\mu-D_\lambda}{2}
=n(\lambda)-d\,n(\mu).
\]

Then the coefficient motive is

\[
\mathbf1(-h_{\lambda;\mu,\nu})^{\oplus a_{\lambda;\mu,\nu}},
\qquad
 a_{\lambda;\mu,\nu}
 =\dim\operatorname{Hom}_{\mathrm{GL}_r}
 (S_\lambda V,S_\nu(S_\mu V)).
\]

For SP3 the corresponding object is

\[
\mathbf1\bigl(-n(\lambda)-n(\mu)\bigr)
 ^{\oplus g(\lambda,\mu,\nu)}.
\]

In particular, the natural Frobenius on the Weil multiplicity spaces of SP2 and SP3 is scalar `q^h`, with `h` given above. It has no nontrivial arithmetic Jordan block. This conclusion concerns these objects with their fixed natural normalization; arbitrary pure Weil objects do not have this property.

**Proof.** Work in the rational motivic Satake category `Sat_G^c` of Richarz–Scholbach. Their Theorem4.1 makes the untwisted intersection motive `IC_alpha` pure of weight `D_alpha`. Proposition4.8 preserves weights under convolution. Proposition5.9 supplies symmetric constraints compatible with corrected symmetric geometric Satake under l-adic realization. Therefore the same primitive rational Young idempotent acts motivically on the convolution power, and its image is an actual summand of weight `w=dD_mu` (or `w=d(m+n-2)` for the product group).

Definition6.2, Corollary6.4 and Lemma6.5 supply the essential extra input: `Sat_G^c` is a semisimple abelian category, generated by the `IC_alpha(n)`, and is stable under convolution. Thus the motivic projector image has a finite decomposition into `IC_lambda(n)`. By their Theorem4.1 and the Tate convention, this simple object has weight `D_lambda-2n`. Since the image is pure of weight `w`, only

\[
n=\frac{D_\lambda-w}{2}=-h
\]

can occur for this `lambda`. The multiplicity of that summand is the ordinary classical coefficient by compatibility of the symmetric realization and geometric Satake. On the open `lambda` stratum, removal of the perverse shift `D_lambda` therefore leaves exactly the coefficient motive `1(-h)` with that multiplicity. Lemma6.3 identifies the corresponding endomorphism and Hom spaces with those of the coefficient motives on the base; it also makes the isotypic description precise.

For product `GL_m x GL_n`, use `D_lambda+D_mu` in the identical argument. The integer formulas for `h` follow from the partition degree equalities already proved in SP2–SP3. Finally the l-adic realization of `1(-h)` is `Q_l(-h)` with geometric Frobenius exactly `q^h`. Its direct sums have scalar Frobenius. ∎

**Terminology and scope.** The “coefficient motive” is an object of the mixed Tate category over the base, recovered by restriction of the isotypic summand and removal of its IC shift. It is not the ordinary rational vector space `Hom_mot(IC_lambda,P)`; that untwisted Hom can vanish when `h` is nonzero. The relevant multiplicity vector space is `Hom_mot(IC_lambda(-h),P)`, while the Weil multiplicity from SP1 is its tensor product with `Q_l(-h)`. The motivic refinement strengthens ordinary purity to Tateness but supplies neither a preferred basis of the projector image nor a positive combinatorial rule for its rank. For example, the signed actions in SP4 and the three-step example below remain present.

### Primary motivic source audit

T. Richarz and J. Scholbach, *The motivic Satake equivalence*, Mathematische Annalen380 (2021),1595–1653, DOI `10.1007/s00208-021-02176-9`. The publisher’s full text and a primary article copy in the German National Library were read:

- [Publisher](https://link.springer.com/article/10.1007/s00208-021-02176-9)
- [Article PDF](https://d-nb.info/1234764768/34)

Exact checked locators are Theorem4.1 (§4.1); Proposition4.8 (§4.2); Proposition5.9 (§5.2); Definition6.2, Lemma6.3, Corollary6.4, Lemma6.5, Corollary6.6 and Theorem6.8 (§6.1). In the 59-page early-publication PDF, Theorem4.1 is on PDFpage28, Proposition4.8 on page30, Definition6.2 through Corollary6.4 on page42, and Lemma6.5 on page43 (all one-based). Lemma6.5’s proof explicitly uses purity to show its indecomposable coefficient motive is `1_S(n)`; this is the exact step needed above. Theorem6.8 identifies the motivic Tannakian group with Deligne’s modified dual group, so retaining integer twists rather than suppressing the weight coordinate is essential.

Web refs: `turn492559917view1`–`turn492559917view4`, `turn624759337view0`–`turn624759337view4`, and `turn646093206search46` for Proposition5.9’s compatibility statement. The general motivic theorems are source-checked inputs, not new theorems proved in this note.

A related 20 December 2023 [author corrigendum to the foundational shtuka-motive paper](https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/richarz/corrigendum.pdf) was also read. It corrects general equivariant Tate-detection and descent assertions but explicitly retains that paper’s affine-flag results in §§4–6; its additional cohomological-dimension hypothesis holds over finite fields (Remark1.9). The label `[RS21]` in that corrigendum denotes the Witt-vector paper, not this motivic-Satake paper, and no contrary bibliographic claim is made here. This check found no change to the split finite-field input used in SP5.

## 9. Three minuscule GL2 steps: geometry checked for the signed-permutation obstruction

For `mu=(1)`, `d=3`, `lambda=(2,1)`, the twisted convolution variety is an iterated `P^1` bundle of dimension3. Its fiber over the lattice of relative type `(2,1)` is the variety of full flags stable under a nilpotent operator `N` of Jordan type `(2,1)` on a three-dimensional space. Write `I=im N`, a line, and `K=ker N`, a plane containing `I`.

A full stable flag `L subset P` has `L subset K` and `I subset P`. If `P` is not `K`, then `N(P)=I`, which forces `L=I`. Hence the fiber is the union

\[
\{L=I,\;P\supset I\}\ \cup\ \{P=K,\;L\subset K\},
\]

two rational projective lines meeting at the flag `(I,K)`. Both components are defined over `F_q`. Its top cohomology is therefore `Q_l(-1)^2`. Since `D_(2,1)=1`, the relevant stalk degree of the convolution complex is `-1`, equal by proper base change to `H^2` of this fiber. The other geometric constituent is `IC_(3)`; its intermediate-extension condition excludes a degree `-dim Gr_(2,1)=-1` contribution along this boundary stratum. Thus the multiplicity is exactly this pure Tate two-dimensional space, of weight `3-1=2`.

Schur–Weyl duality identifies its corrected symmetric `S_3` action with the faithful standard two-dimensional representation. A signed-permutation basis would give an injection of `S_3` into the group of two-by-two signed permutation matrices, which has order8; this is impossible because3 does not divide8. Thus even allowing signs does not turn this action into a permutation of component lines. This geometric degree and fiber check was sent to the agent developing the projector-orbit criterion; that agent owns the fuller representation-theoretic argument and its final finding identifier.
