# B.8: every mathematical claim on scans 374--376, checked against Breen

GPT-6 Astra (OpenAI, ChatGPT Pro mode), SA08 run, 19 November 2026.
No priority is claimed. The primary source is Lawrence Breen, *Extensions
du groupe additif*, Publications mathematiques de l'IHES 48 (1978), 39--125.
The complete Numdam PDF was opened and downloaded, its text was extracted,
and printed pages 40, 47, 48 and 86 were visually inspected. Page locators
below are printed journal pages, not PDF-page indices.

The manuscript transcription used is
`input/RESEARCH_SA08_transcriptions/transcriptions/K136-03_transcription.tex`,
lines 718--945. This is a single transcription witness, with the marked
reading doubts preserved. The attached reading is
`input/RESEARCH_SA08_study/study/readings/136_282-376.md`, lines 382--395.
No original manuscript scan image was attached for these leaves; assertions
below distinguish errors in the transcribed formula from uncertain ink.

## D.13. The hypotheses and categories (Known, exact scope checked)

Breen's notation is a topos T with a ring object O of characteristic p>0,
R=Gamma(T,O), and additive underlying F_p-module sheaf G_a. His hypotheses
A1 and A2 (pp.45--46) say respectively:

* functions O^d->O are exactly polynomials R[x_1,...,x_d];
* H^q(O^d,O)=0 for q>0 and every finite d, including d=0.

Breen Theorem 1.3 applies under precisely these hypotheses. They hold on
the big fppf, big etale and big Zariski sites over any affine F_p-algebra
R, and on subsites containing all affine spaces over the base; see
Examples 1.4--1.6, pp.47--48. He expressly excludes replacing this by the
small etale or small Zariski site without a further argument: A1 need
not hold there. The presheaf topos on affine R-algebras is also covered.
For nonaffine bases the relative version Theorem 1.7, p.49, computes the
sheaf Ext; global Ext is subject to the local-to-global spectral sequence.

Throughout D.15--D.20, Ext_Fp means Ext in the abelian category of sheaves
of F_p-vector spaces. Ext_Z means Ext in all abelian sheaves. These are
different categories, even when both arguments are killed by p.
The ring H=End(G_a) is the skew polynomial ring R[F], with

    F a = a^p F.

This is Breen Lemma 1.2, p.46. It is not generally the commutative
polynomial ring when R differs from F_p.

## D.14. Coefficient extension and the first operations formula (Refuted / corrected)

The first line on scan374,

    H^*(X;R)=H^*(X;F_p) tensor_Fp R,

is not valid for arbitrary infinite X and arbitrary R. For the discrete
space X=N and R=F_p[t], its left side in degree0 is product_N R, whereas
the canonical right side consists of sequences with a uniform finite
bound on polynomial degree. The sequence (t^n)_n is missing. This is an
infinite counterexample and is proved directly; a finite computation
cannot certify this failure. The formula is valid, for example, when
R is finite dimensional over F_p, or when X has finitely many
nondegenerate simplices in each relevant degree.

Even where this tensor formula is valid, the manuscript's pair
P_R^i=P^i tensor1 for i>0, P_R^0=1 tensor F does not give Breen's
coefficient-natural operations. All single P^i and Q^i, including i=0,
are Frobenius-semilinear in the coefficients. In a tensor presentation
of ordinary cohomology the actual formula for a single operation is

    P_R^i=P^i tensor F,       Q_R^i=Q^i tensor F,

and likewise Sq_R^i=Sq^i tensor F in characteristic2. A word of length
ell has coefficient Frobenius F^ell. This follows either directly from
the p-fold construction, Breen (4.1)--(4.3), pp.83--84, or from the
coefficient relation (4.13), p.89.

A finite algebraic counterexample to the printed formula is p=2,
R=F_2[t]/(t^2), X=CP^2, with u in H^2(X;F_2). The top-square axiom gives

    Sq^2(tu)=(tu)^2=0,

whereas the claimed coefficient-linear extension gives t u^2 !=0.
The finite cohomology algebra R[u]/(u^3) is exhaustively represented
in the supplied exact program, which checks these two values.
This refutes the conjunction of the manuscript formulas with the
ordinary Steenrod axioms; one may of course define a separate
R-linear additive extension of P^i, but it is not the claimed system
with P_R^0=F and Cartan's formula.

The identity operation is the empty word, and differs from P^0=F (or
Sq^0=F) on G_a. They agree on F_p-valued points. Breen Lemma 4.1, p.84,
and the paragraph introducing empty words on p.85 state this distinction.

## D.15. Cohomology of K(O,n), including the missing odd-primary generators

**Known/corrected statement.** Under A1,A2 and n>=1, Breen Theorem4.3,
p.86, for odd p, gives a free graded-commutative R-algebra on
P^J iota_n, where J is admissible and satisfies

    e(J)<n,  or  e(J)=n with leading epsilon_1=1.

The extended algebra includes P^i of degree2i(p-1) and Q^i of
degree2i(p-1)+1, for every i>=0. Its admissible words retain P^0; one
does not impose P^0=1. The notation beta P^i used in the formal words
means Q^i, not an actual identification with the composite beta P^i.
Indeed beta=Q^0 and beta P^i=Q^i P^0; Breen Remark4.2(b), pp.85--86.
For p=2, Theorem4.4, p.86, gives the polynomial algebra on admissible
Sq^I iota_n with e(I)<n, allowing zero indices and retaining Sq^0.
The index n must be used consistently; the manuscript switches m,n.

**Refutation of the literal odd-primary theorem.** The scan374 theorem
lists only the even-degree P^i and the strict inequality e(I)<n. At
p=3,n=1 it cannot produce a degree2 generator: the fundamental class
has degree1, all positive P's increase degree by multiples of4, and
an odd generator squares to zero. Yet the normalized polynomial
bar cochain

    c_p(x,y)=((x+y)^p-x^p-y^p)/p mod p

is a nonzero class of H^2(BG_a,G_a). The numerator is divisible by p
in Z[x,y]. The cocycle equation

    c_p(y,z)-c_p(x+y,z)+c_p(x,y+z)-c_p(x,y)=0

holds integrally by cancellation. It cannot be a polynomial coboundary:
the bar differential preserves total polynomial degree, and a
one-variable homogeneous polynomial of degree p is a multiple of x^p,
whose additive coboundary is zero in characteristic p. But c_p is
nonzero (its coefficient of x y^{p-1} is1). By A1,A2 the polynomial bar
complex computes the indicated sheaf hypercohomology; see Breen
Lemma2.11. Thus this is a full counterexample over F_3, where
c_3=x^2y+xy^2. The program verifies the polynomial cocycle identity
for p=2,3,5,7 as an identity of polynomial coefficient dictionaries,
not merely by testing F_p-valued points. The general proof covers
all primes. This is the Witt/Bockstein class already indicated in
another part of the same scan; Breen Remark4.2(b) confirms it.

The claim that the proof proceeds from n=1 by the bar/Leray spectral
sequence and the usual transgression argument is correct. Breen's
proof of Theorems4.3--4.4, pp.86--87, explicitly cites Lazard's
*Lois de groupes formels et analyseurs*, Theorem12.1, for n=1,
and carries out this reduction. We rely on Breen's opened proof,
not on an unopened statement attributed to Lazard.

## D.16. Right-derived Sym, duality, and classification of operations

**Known with corrected signs and weights.** Breen Lemma2.11,
formula(2.15), p.61, identifies algebras

    H^*(K(O,n),O) = R^* Sym(R,-n).

The right-hand side is the cohomology of the cosimplicial symmetric
algebra on the dual of the usual finite-free simplicial model. Over
F_p it is the weightwise linear dual of the corresponding derived
Gamma complex. With general R it is the corresponding R-base change.
The manuscript's F_p[m] notation needs this variance/sign convention;
it is not an ordinary additive derived functor applied to a module
in degree zero. The dual is restricted by polynomial weight.
Taking the full linear dual of the direct sum of all weights instead
produces a product and is a different object.

The preceding representability discussion is correct when placed in
the homotopy category of simplicial sheaves: H^q(K(F,n),G) classifies
natural operations from H^n(-,F) to H^q(-,G). Additivity, stability
and compatibility with products impose additional conditions; they
are not automatic for an arbitrary class. Breen section2,
particularly its discussion leading to Lemma2.11 and the stable
operations in section4, uses this precise interpretation. The
colimit over quasi-isomorphic resolutions is a model for derived
maps, not maps from an arbitrarily fixed nonfibrant object.

The marginal ordinary-space claim about K(R,n) is valid in the
usual finite-dimensional F_p-vector-space case by ordinary
Eilenberg--Mac Lane cohomology: choose a basis of the finite additive
vector space, apply the classical computation and Kunneth, and
extend coefficients. It is not a general formula for arbitrary
infinite R: cochains contain infinite multilinear forms absent
from the free algebra on ordinary finite sums of products of
linear forms. For example take odd p and R=F_p[t]. In the underlying
additive vector space with basis 1,t,t^2,... choose the alternating
form pairing t^{2j},t^{2j+1} to1 for every j and otherwise zero.
It has infinite rank and defines a degree2 group-cohomology class
with values in F_p subset R. Projecting coefficients by t|->0,
any finite sum of products of degree1 R-valued classes gives a
finite-rank alternating form, and Bockstein degree2 classes have
zero alternating commutator. Hence the displayed class is not
in the asserted generated subalgebra. This is an infinite
counterexample, for which the rank argument is the certificate.

## D.17. Finite-field detection: the precise statement needed by scan374

The end of scan374 invokes evaluation on F_{p^h} and an injection
on a bounded-polynomial part. Evaluation is injective on polynomials
of degree<p^h in each variable: successive division by x_i^{p^h}-x_i
or interpolation proves that elementary assertion. Injection of
cochain groups alone does not prove injection of cohomology, and
that per-variable bound is not even preserved by arbitrary linear
changes of coordinates in a general K(O,n) simplex. Therefore the
notation H^*(-)_h must be defined; it cannot silently mean the
cohomology of a coordinate-dependent non-subcomplex.

A sufficient, invariant and fully proved version is this: over
F_p, the part of total polynomial weight <p^h injects after
restriction to K(F_{p^h},n) and extension of coefficients to F_{p^h}.
More generally each finite set of polynomial cohomology classes is
detected for sufficiently large h. Here is a proof from D.15.
For each classical admissible generator I choose its extended lift of
least polynomial weight, say p^{ell(I)}. The extended admissible
generators above it form the Frobenius string indexed by r>=0,
of weight p^{ell(I)+r}; this is the admissible-word description of
Breen Remark4.2(a), p.85, together with Remark4.5(b), p.87.
The integer ell(I) counts the p-fold operations in that extended
lift; in particular Q^i counts once, so this convention does not
incorrectly count a formal beta P^i as two independent operations.
Choose an F_p-basis a_1,...,a_h of F_{p^h}, with dual fundamental
classes z_1,...,z_h. Restriction of this generator is

    sum_j a_j^{p^{ell(I)+r}} I_class(z_j).

This follows by Frobenius semilinearity from D.14 and Breen
(4.8)--(4.10), pp.87--88. For ell(I)+r<h the relevant columns of the
Moore matrix (a_j^{p^s})_{0<=s<h,1<=j<=h} are linearly independent
over F_{p^h}. To check that fact without a citation, a dependence
would give a nonzero additive polynomial of degree<=p^{h-1}
vanishing on all p^h elements, contradicting its degree bound.
For each fixed classical generator I, the corresponding generators
therefore inject linearly into the classical generators for the z_j.
The free graded-commutative algebra on these independent vectors
injects into the free algebra on the full classical basis (extend
an independent set to a basis). This proves the asserted weight
bound and finite-set detection. It supplies the exact detection
claim used by the manuscript argument without asserting that an
undefined per-variable filtration is canonical.

## D.18. The Ext formula: the valuation is off by one (Refuted / corrected)

Breen Theorem1.3, p.47, states

    Ext_Fp^{2j+1}(G_a,G_a)=0,                  j>=0,
    Ext_Fp^{2j}(G_a,G_a)=H/(F^{v_p(j)+1}),     j>0,

as (H,H^op)-bimodules, the denominator being the two-sided ideal
generated by the displayed power. End(G_a)=H in degree zero.
The +1 is visibly present in the primary PDF, checked on printed
p.47 and again in the final deduction on p.116, equations(7.22)--(7.23).
The manuscript transcription on scan376 has d=v_p(i), which omits
this +1. At i=1 its prediction is H/(1)=0, whereas the correct
Ext^2 is H/(F)=R. This is the smallest counterexample, valid already
R=F_p. It follows from the opened theorem rather than a finite
search or extrapolation.

The odd-degree vanishing includes Ext_Fp^1=0. The attached reading,
lines394--395, wrongly argues that the Witt extension makes this
only a statement modulo F-torsion. The middle sheaf W_2 is not
annihilated by p, so its extension is in Ext_Z^1, not Ext_Fp^1.
For example W_2(F_p)=Z/p^2: multiplication by p is nonzero. Thus
there is no conflict between the Witt class of D.15 and
Ext_Fp^1=0. The category distinction fully resolves the apparent
contradiction.

This theorem computes graded bimodules, not the full Yoneda algebra.
Breen explicitly leaves the proposed Yoneda multiplication as
Conjecture7.12, p.116; the abelian-sheaf algebra is Conjecture7.14,
pp.117--118. Nothing in scans374--376 may be promoted to either
conjectural algebra computation on the authority of Theorem1.3.

## D.19. F-torsion and the perfect-site corollary (Known, categories checked)

For F_p-sheaf Ext, D.18 immediately proves the scan375 assertion:
every positive Ext group is F-torsion; in degree2j the uniform
annihilator is F^{v_p(j)+1}, and odd groups vanish. This strengthens
the displayed restriction i>1 to i>0 in that category.

The perfect-site corollary itself is true with its site specified.
Breen's introduction, p.41, states that on the perfect site over a
perfect field, with the etale or Zariski topology,

    Ext_Z^i(G_a^perf,G_a^perf)=0,             i>1.

It concerns abelian sheaves and is not a reason to identify Ext_Z
with Ext_Fp. Frobenius becomes invertible on the perfect site,
which is the mechanism behind vanishing, but carrying Ext through
perfection needs the cited theorem, not a bare formal localization
of an arbitrary abelian category.

The attribution 'Milne(?)' is refined by an opened primary printed
witness: J.S. Milne, *Duality in the flat cohomology of a surface*,
Ann. ENS (4)9 (1976), 171--201, Lemma2.2, printed p.181, labels the
result '(L. Breen)'. Over a perfect affine base S it states
Ext_Fp^i(O_S,O_S)=0 for all i>0 in the perfect etale setting.
Milne cites Breen's preprint and personal communication and applies
the result. Thus the theorem is attributed to Breen, with Milne as
an early application and printed witness. Breen's later chapter
*Extensions du groupe additif sur le site parfait*, in *Surfaces Algebriques*, LNM868 (1981), pp.238--262, was located; its publisher
metadata and two-page preview were opened, but the full chapter
was not available and is not marked opened or used as the sole
support for a theorem.

## D.20. The universal-coefficient spectral sequence and the two lemmas

For a bounded-below simplicial F_p-module sheaf chain object C(X)
and an injective resolution G->I^bullet, filter the double Hom
complex Hom(C(X),I^bullet). Its two filtrations give the usual
universal-coefficient spectral sequence

    E_2^{a,b}=Ext_Fp^a(H_b(C(X)),G) => H^{a+b}(X,G).

In each total degree of the first quadrant only finitely many
bidegrees occur, giving convergence in the use on these pages.
The manuscript's H_b(X) must mean the homology of its free
F_p-linearization. Reduced versus unreduced degree0 must be handled
consistently. Breen's construction of the fundamental spectral
sequence in section3 and the derived Hom setup in section2 supply
the corresponding formalism.

For X=K(G_a,n), H_n=G_a, and in the stable range n<=j<2n the
higher homology is a direct sum of copies of G_a, indexed by the
appropriate classical stable homology groups. One obtains this
by stabilization and the additivity of Eilenberg--Mac Lane spectra
on F_p-vector modules; sheafification is exact. The words 'n grand'
on scan375 must mean this stable range for every j under consideration.
The unqualified equality H_j=direct-sum G_a for every j is false.
Already n=1,j=2, evaluation on the finite additive groups F_p and
F_p^2 gives dimensions1 and3 for H_2(-;F_p), whereas a fixed direct
sum of copies of G_a would give dimensions1 and2 after its rank is
fixed by evaluation on F_p. The normalized bar computation for
p=2,3 is included in the finite program; the general dimension
calculation also follows from the elementary Kunneth formula for
a product of two cyclic groups.

In the intended stable range, Lemma1 (the displayed edge obstruction
vanishes 'mod F') is correct after killing F-torsion: all its
positive-Ext targets vanish by D.18. This proves the needed
conclusion, rather than trying to reconstruct the manuscript's
abbreviated induction as a self-contained proof. Over F_p the
phrase may literally be implemented by exact localization at F
in the commutative ring F_p[F]. Over a general imperfect base,
one should instead use the annihilation theorem and the specified
perfect-site result; no Ore localization is assumed without proof.

Lemma2's rule that a single operation P^d maps to the classical
P^d tensor F is correct; a word of length ell maps with F^ell,
with Q^i included at odd primes. This is exactly D.14 and the
finite-field restriction formulas of Breen4.5(b). Checking P^0
alone does not prove it for all positive operations; the p-fold
construction or coefficient relation supplies that missing step.

## D.21. The final bar/Koszul calculation (Known, with a genuine odd-primary warning)

The extended operation algebra maps to the ordinary Steenrod algebra
by imposing P^0=1 (Sq^0=1) and sending the formal Q^i to the usual
beta P^i. Its coproduct is Cartan's coproduct. The bar/cobar diagram
on scan376 is the source of Breen's fundamental spectral sequence.
The exact weightwise Tor terms are displayed in Breen(5.1)--(5.4),
pp.94--95, and calculated by a Koszul resolution in Proposition5.1,
p.95. Tensor products and duals here are weightwise graded ones;
infinite direct sums must not be silently replaced by full duals.

If the final doubtful transcription is read only as an E_2
computation 'par Koszul', that claim is correct with these
conventions. If read as identifying E_2 with the abutment for every
prime, it is false. In characteristic2 all total degrees at E_2
are even, so it collapses, Breen(5.6)--(5.7) and Proposition5.3,
pp.96--97. Breen immediately states on p.97 that in odd
characteristic nonzero differentials prevent this identification;
the subsequent calculation, culminating in Proposition7.9,
p.115, and Proposition7.10, p.116, supplies the corrected abutment.
Thus the ambiguous glyph is not silently resolved to either a
true or false assertion. Both mathematically meaningful readings
are settled. These formulas still do not compute the Yoneda
multiplication, as D.18 explains.

## Corrections to the inherited study and readings

* Prompt R4's status is corrected separately by D.1--D.5: the attached
  Pro notes N32--N33,N71 already had the general exact-adjoint mechanism.
* Reading `136_282-376.md`, lines383--385: the odd-prime generator
  list lacks Q^i and the boundary-excess case; replace by D.15.
* Same reading, line390 and prompt B.8: the exponent v_p(i) must be
  v_p(i)+1; D.18, BreenTheorem1.3.
* Same reading, lines394--395: Ext_Fp^1 actually vanishes; the Witt
  extension is only an abelian-sheaf extension. Replace by D.18.
* Same reading, lines416--418 and leadL8: the extended algebra and
  ordinary Steenrod algebra are distinct, but this does not show
  that the specified automorphisms realize every extended operation.
  The automorphism agent's proof determines their actual action.
  In particular the unit operation is common to both algebras and
  must not be confused with P^0=F.
* Transcription lines724--730: the tensor-coefficient formula needs
  a finiteness hypothesis, and positive operations are also
  Frobenius-semilinear; D.14.
* Transcription lines897--902: +1 is missing in the valuation
  exponent. This is a mathematical correction to the transcription
  as supplied; with no original scan we do not decide whether the
  omission belongs to the manuscript or to the transcription.
