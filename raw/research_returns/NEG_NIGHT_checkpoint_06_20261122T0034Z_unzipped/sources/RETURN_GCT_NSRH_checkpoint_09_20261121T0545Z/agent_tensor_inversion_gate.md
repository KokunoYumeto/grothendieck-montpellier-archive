# F68: universal tensor inversion of the actual coefficient object

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This note strengthens the previously proved failure of an inverse in a bounded Weil realization. It proves an obstruction to making the actual coefficient tensor-invertible by any nonzero additive strong monoidal functor, even into an unbounded target and even when the functor is not symmetric. The exact source duality maps or direct-sum decomposition, not an Euler character alone, are essential.

## 1. Categories and the meaning of inversion

An additive monoidal category here has a zero object, finite biproducts and tensor product additive in each variable. Its unit is denoted 1. It is nonzero if \(1_1\ne0\); if \(1_1=0\), additivity of tensor and the unit constraints imply \(1_Y=0\) for every object Y.

A tensor-invertible object X has a two-sided inverse Y, with isomorphisms \(X\otimes Y\simeq1\simeq Y\otimes X\). A strong monoidal functor has invertible tensor and unit structure maps. We require the functor to be additive, so it preserves zero morphisms and finite biproducts. Exactness, faithfulness and finite cohomological amplitude of its target are not assumed.

The conclusions below concern inversion of an actual object in this sense. They do not rule out a localization of a Grothendieck ring, inversion of a scalar trace function, a functor that discards source maps, a merely lax monoidal operation, or an arbitrary filtration/extraction procedure.

## 2. An invertible summand cannot be a proper summand of the unit

### Lemma TI-A

In an additive monoidal category, if an invertible object U is a direct summand of the unit, then its complementary summand is zero.

### Proof

Choose maps \(i:U\to1\), \(p:1\to U\) with \(pi=1_U\), and put \(e=ip\in\operatorname{End}(1)\). For every object Y define the natural unit-scalar endomorphism

\[
 e_Y=\lambda_Y\circ(e\otimes1_Y)\circ\lambda_Y^{-1},
 \tag{TI1}
\]

where \(\lambda_Y:1\otimes Y\to Y\) is the left unitor. Coherence gives \(e_1=e\). Naturality with i gives
\(ei=i e_U\). Since \(ei=i\), composing with p gives \(e_U=1_U\).

Right tensoring with the invertible U is an equivalence. In particular the map
\(\operatorname{End}(1)\to\operatorname{End}(U)\) sending e to e_U is faithful. Thus \(e=1_1\). If \(1\simeq U\oplus V\), the projection e onto U kills the inclusion of V; as e is the identity, that inclusion and hence \(1_V\) vanish. Thus V is zero. No braiding was used. QED.

### Corollary TI-B

Let \(L_1,\ldots,L_r\) be tensor-invertible objects with r at least two. Their finite direct sum is not invertible in a nonzero additive monoidal category.

If a strong additive monoidal functor F is defined on a category containing these objects and their displayed biproduct, then \(F(\bigoplus L_i)\) cannot be invertible unless the target unit is zero.

### Proof

If \(P=\bigoplus L_i\) were invertible, right tensor its decomposition by an inverse. The unit would be a direct sum of the invertible objects \(L_i\otimes P^{-1}\). Lemma TI-A says that the complement of the first is zero; at least one of those complementary invertible summands is therefore zero. Its inverse then makes the unit zero. A strong monoidal functor preserves invertibles, and an additive functor preserves the displayed biproduct, so the same argument applies to F. QED.

This proof permits an unbounded derived target, arbitrary idempotents, and infinite direct sums elsewhere in the target. It uses only this finite displayed biproduct.

## 3. A zero source trace gives another non-symmetric obstruction

Let \(\mathcal C\) be a symmetric additive monoidal category. Let X be dualizable, with a chosen dual \(X^\vee\) and maps

\[
 \eta:1\to X\otimes X^\vee,\qquad
 \epsilon:X^\vee\otimes X\to1
\]

satisfying the two triangle identities. Its categorical dimension is the actual source endomorphism

\[
 \dim_{\mathcal C}(X)
   =\epsilon\circ c_{X,X^\vee}\circ\eta
   \in\operatorname{End}_{\mathcal C}(1).
 \tag{TI2}
\]

Here c is the source symmetry. This dimension is distinct from a Frobenius-inserted trace.

### Lemma TI-C

If \(\dim_{\mathcal C}(X)=0\) and
\(F:\mathcal C\to\mathcal D\) is an additive strong monoidal functor into an additive monoidal category, then F(X) cannot be tensor-invertible unless the target unit is zero. The target need not be symmetric and F need not preserve any target braiding.

### Proof

A strong monoidal functor carries the displayed dual pair and its triangle identities to a dual pair for F(X), with dual F(\(X^\vee\)), after its structural isomorphisms are inserted.

If an object Z is invertible, every dual of Z is a tensor inverse, and the evaluation and coevaluation of that dual pair are isomorphisms. One justification is the adjunction
\((-\otimes Z)\dashv(-\otimes Z^\vee)\): the left functor is an equivalence when Z is invertible. Its right adjoint is therefore an inverse equivalence and both adjunction unit and counit are isomorphisms. At the unit object these are precisely the coevaluation and evaluation, with associators and unitors. Equivalently, uniqueness of a dual identifies it with the inverse dual pair, whose structure maps are isomorphisms.

Thus if F(X) were invertible, both F(\(\eta\)) and F(\(\epsilon\)), with the monoidal constraints, would be isomorphisms. F(c) is an isomorphism simply because c is one. Their composite is the image of TI2, which is the zero morphism by additivity. A zero endomorphism of the unit that is also an isomorphism forces \(1_1=0\). This proves the lemma.

No identification of F(c) with a target symmetry was made. The argument retains the actual source evaluation, coevaluation and symmetry map as morphisms; it cannot be applied to a category from which these maps or the dual object have been removed. QED.

For a symmetric strong monoidal functor there is also the usual shorter trace proof: it preserves categorical dimension, whereas the dimensions of an invertible object and its inverse multiply to \(1_1\). A zero dimension therefore forces a zero unit. TI-C proves that preservation of a target symmetry is unnecessary once the source trace word and dual pair are retained.

## 4. An actual Frobenius-equivariant splitting of the absolute torus object

Fix a prime power q, a prime ell not dividing q, and a finite extension E of Q_ell. Write E(r) for the Tate line, on which geometric Frobenius acts by \(q^{-r}\). All derived cohomology below is geometric cohomology with its Weil action, equivalently the geometric fiber of the derived pushforward to Spec F_q.

Put

\[
 T=R\Gamma_c(\mathbb G_{m,\overline{\mathbb F}_q},E).
 \tag{TI3}
\]

We need an isomorphism of actual derived Weil objects, not merely its cohomology groups or its Euler class.

The Gysin sequence for the smooth pair
\((\{0,\infty\},\mathbb P^1)\), and the projective-line calculation, give

\[
 H^0(\mathbb G_m,E)=E,\qquad
 H^1(\mathbb G_m,E)=E(-1),\qquad
 H^i=0\ (i\ne0,1).
 \tag{TI4}
\]

Indeed the Gysin map \(E(-1)^2\to H^2(\mathbb P^1,E)=E(-1)\) sends both rational point classes to the degree-one generator, so it is the sum map. Its kernel is E(-1), and its cokernel is zero. All maps are Frobenius-equivariant.

The rational point \(1\in\mathbb G_m(\mathbb F_q)\) gives actual derived Weil maps

\[
 E\xrightarrow{\;\mathrm{unit}\;}
 R\Gamma(\mathbb G_m,E)
 \xrightarrow{\;\mathrm{ev}_1\;}E
 \quad\hbox{with composite }1_E.
 \tag{TI5}
\]

This splits off E in the derived category. Its complementary object has exactly the single cohomology E(-1) in degree one by TI4, so the standard truncation identifies the complement with E(-1)[-1]. Hence

\[
 R\Gamma(\mathbb G_m,E)
       \simeq E\oplus E(-1)[-1]
 \tag{TI6}
\]

as derived Weil objects. This proof uses an actual rational-point retraction, not an assumed Frobenius-semisimple splitting.

The canonical cup-product/trace pairing for the smooth curve yields an actual derived Weil isomorphism

\[
 T\simeq R\Gamma(\mathbb G_m,E)^\vee(-1)[-2].
 \tag{TI7}
\]

The pairing is perfect on all cohomology groups, so its derived adjoint is an isomorphism; naturality of cup product and the trace Tate line makes it Frobenius-equivariant. Applying it to TI6 gives

\[
 \boxed{T\simeq E[-1]\oplus E(-1)[-2].}
 \tag{TI8}
\]

Both summands are tensor-invertible. With the usual Koszul symmetry on complexes, their categorical dimensions are respectively -1 and +1. Thus \(\dim(T)=0\), whereas the inserted Frobenius trace is

\[
 \operatorname{Tr}_{\rm Eul}(F^n;T)=q^n-1.
 \tag{TI9}
\]

The nonzero arithmetic function in TI9 must not be confused with the zero source endomorphism TI2 for the identity.

### Absolute inversion consequence

Every additive strong monoidal functor from this coefficient category to a nonzero additive monoidal target fails to make T invertible. Corollary TI-B proves this using the actual splitting, and TI-C independently proves it using the actual dual pair and zero source trace. Neither proof requires target symmetry, faithfulness, boundedness, or a finite-dimensional realization of the target.

The same applies to every positive tensor power of T and any Tate/cohomological normalization. Explicitly

\[
 T^{\otimes2}(1)
 \simeq E(1)[-2]\oplus E[-3]^{\oplus2}\oplus E(-1)[-4].
 \tag{TI10}
\]

Its Euler Frobenius trace is \(q^n+q^{-n}-2\), the F62/IV scalar factor. This direct sum has four invertible summands and categorical dimension zero. The point coefficient \(R\Gamma_c(\mathbb G_m^2\times\mathbb P^2,E(2))[1]\) used for the exact VIII printed coefficient is likewise excluded: Künneth and the projective-bundle maps decompose it into twelve shifted Tate invertibles.

## 5. The stronger formal-inversion boundary for the F38 projective-line object

The rational-point retraction and projective-line cohomology similarly give the actual derived Weil splitting

\[
 H=R\Gamma(\mathbb P^1,E)
      \simeq E\oplus E(-1)[-2].
 \tag{TI11}
\]

Its categorical dimension is 2, so the zero-trace argument is not the one used here. Corollary TI-B nevertheless proves:

> No additive strong monoidal functor into a nonzero additive monoidal category can make the actual projective-line cohomology object H tensor-invertible.

This strengthens the prior statement that a faithful finite or unbounded Weil realization cannot give H a tensor inverse. The stronger conclusion is formal and does not require faithfulness or any target cohomology functor. The two invertible direct summands are the decisive retained structure.

The F38 stack trace-inverse still exists as a trace statement. No contradiction follows: an inverse to all extension-degree Euler traces is not an isomorphism \(H\otimes Z\simeq1\). Likewise a formal localization of a Grothendieck ring can invert the class \(1+\mathbb L\) without furnishing such an additive strong monoidal functor on the actual source objects.

## 6. Relative F62: dualizability and zero trace, without a global splitting

Retain F62's base
\(O=(\mathbb P^1\times\mathbb P^1)\setminus\Delta\),
line bundle \(\mathcal L=O(1,-1)|_O\), and actual coefficient

\[
 \mathcal K=R\pi_!E,\qquad
 \pi:\mathcal L^\times\to O.
 \tag{TI12}
\]

Its established triangle is

\[
 \mathcal K\longrightarrow E_O(-1)[-2]
 \xrightarrow{\,c_1(\mathcal L)\,}E_O
 \longrightarrow\mathcal K[1].
 \tag{TI13}
\]

The Chern class is nonzero; \(\mathcal K\) does not globally split as the two summands in TI8. We do not apply the global split-summand argument to it.

Instead, trivialize the line bundle on a Zariski cover. On each open set the relative compact pushforward is the constant complex with fiber T, by compact-support base change and Künneth/projection formula. Therefore \(\mathcal K\) is locally a bounded complex of finite-rank free E-sheaves. It is tensor-dualizable in the usual constructible derived tensor category, with dual \(R\mathcal Hom(\mathcal K,E_O)\). Dualizability and the required evaluation identities can be checked on this cover.

The categorical trace of its identity restricts to \(-1+1=0\) on every trivializing open. It is a degree-zero endomorphism of \(E_O\), so local vanishing implies that the global trace is zero:

\[
                  \dim(\mathcal K)=0.
 \tag{TI14}
\]

Lemma TI-C now applies to any additive strong monoidal functor on this tensor category, or on a subcategory retaining \(\mathcal K\), its dual, evaluation, coevaluation and the source symmetry map. Making \(\mathcal K\) invertible forces the target unit to be zero. Target symmetry is unnecessary by the explicit source-trace-word proof.

This is a different argument from a nonexistent global splitting. It preserves the nonzero extension in TI13. It also excludes inversion of the two-torus relative coefficient and its stated Tate/projective normalizations, whose categorical dimensions remain zero. It does not imply that arbitrary filtered extraction must invert \(\mathcal K\), be additive, or be strong monoidal.

## 7. What formal localization can and cannot mean here

An additive strong monoidal localization that makes any object just excluded tensor-invertible is necessarily the zero category. This includes an exact strong monoidal functor to a stable or unbounded target, since exactness gives additivity and the argument uses only the original finite source maps.

Nonzero formal inversion of the corresponding Laurent factor can still occur after passing to a Grothendieck ring or a trace ring. For example the formal ring \(\mathbb Z[\mathbb L,\mathbb L^{-1},(\mathbb L-1)^{-1}]\) is nonzero. That does not make the actual object \(T=E[-1]\oplus E(-1)[-2]\) invertible in a category retaining its biproduct and duality. The categorical rank map sends its class to zero and cannot extend across that inversion to a nonzero target.

One-sided inverses, nonadditive or merely lax monoidal constructions, arbitrary weight/perverse associated-graded extraction, or a different object with only the same Euler trace are outside these statements. The source data needed by the applicable lemma must be retained: the trace argument needs the displayed dual pair and source symmetry morphism, whereas the split-summand argument needs only the actual biproduct and the invertibility data of its summands. Merely removing duality maps does not evade that second argument if its own data remain. This result does not assert that every possible normalization or canonical coefficient extraction is impossible. It closes the specific route of tensor-inverting the actual nonproper coefficient while retaining the indicated categorical structure.

## 8. Separate Grothendieck dictionary and primary locators

The bounded point complexes are perfect over E in SGA6 I, Definition4.7 pp.121--122 and Example4.8 p.122. Their dual pairs, shifts and direct sums are actual categorical data. The EGA I affine module/sheaf framework, Theorem1.3.7 p.86, Corollary1.3.8 p.87 and Theorem1.4.1 pp.90--92, applies to the line bundle and its local trivializations in the relative calculation.

The exact geometric source contexts were freshly read in Milne, Lectures on Etale Cohomology:

- Theorem16.1 and Corollary16.2, p.108: purity and the smooth-pair Gysin sequence used for TI4.
- Theorem23.2, pp.139--140: projective-bundle cohomology and the hyperplane classes used for projective spaces.
- Theorem24.1(a),(b), p.144, and Remark24.2(b), p.145: the canonical compact top trace, perfect duality, and normalization of the point Gysin classes.
- Theorem22.1 and Remark22.3(b)--(d), pp.135--136, with the immediately following ell-adic passage: actual derived Künneth, including compact support.

Primary URL: https://www.jmilne.org/math/CourseNotes/LEC.pdf. Local original files are primary_sources/Milne_LEC.pdf and .txt. The rational-point retraction, the derivation of the actual splittings, and all categorical inversion lemmas are proved above.

SGA5 III4.7 is the existing trace-formula framework anchor, not a claim that trace equality supplies an object inverse. SGA6 V Sections2--3 with cote133 scan18 supply the existing actual/virtual coefficient-language anchor; the original-scan qualification already carried for this source remains. The use of the actual source trace is separated from Frobenius-inserted traces and from virtual ring localization. No noncommutative lambda-ring, archival purity statement or designated canonical-label identification is asserted.

## 9. Author check and requested independent review

I checked both the unit-summand proof and the separate transported-dual proof from the monoidal axioms. In the latter, the evaluation and coevaluation become isomorphisms only after assuming that the image object is two-sided invertible; the functor's image of the source symmetry is used as an isomorphism, not identified with a target braiding. The relative argument explicitly proves local perfectness/dualizability and zero global trace without splitting the Chern extension.

I read the complete relevant F62 report, retained its exact torsor orientation and nonsplitting, and freshly read the original Milne contexts above. I independently checked all shifts in TI6--TI11 and the distinction between categorical dimension zero and Frobenius trace \(q^n-1\).

Fresh whole-proof and final-text review is requested. No main paper, frozen finding, or shared master log was edited.
