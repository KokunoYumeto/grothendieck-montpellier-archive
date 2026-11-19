# Adversarial audit of D006E / A018

2026-11-19, GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras.
Parent explicitly requested a new full audit because a strict commutative
PD DGA might appear unable to retain ordinary Steenrod operations. This
audit reread the complete current proofs, rather than using earlier audit
summaries. No mathematical correction to the theorem was found.

## 1. The relevant monoidal category and its unit

The input is a strict commutative algebra in weight-graded S-modules,
S=Gamma_k(T), with derived tensor over S. Its monoidal unit is S.
The output shadow category has unit QS. The comparison is not a
quasi-isomorphism between the unweighted strict k-CDGA and ordinary
k-cochains. Forgetting weights does not factor through Q, since Q
kills every bounded-weight module and the unweighted functor does not.

A concrete check prevents a mistaken termwise extraction argument.
For P=S[-i], the unit P->F L(P) sends its generator to e_i. Hence
the colax map

    L(S[-i-j]) -> L(S[-i]) tensor L(S[-j])

is multiplication by binomial(i+j,i). At i=j=1 it is multiplication
by2 and is zero over F2. L is exact and left adjoint to the strong
monoidal embedding F; it is not strong monoidal. Thus applying L to
the underlying strict DGA term by term does not yield a strict k-CDGA
that computes the recovered power operations.

For the circle, H1(C_gr)=I1 and H1(C_gr)_0=0. In the shadow category
QI1=QS because S/I1 is bounded. The ordinary degree-one class is
represented using this coefficient-tail localization equivalence,
not by a weight-zero S-linear cocycle of the original complex.
Derived symmetric powers of such coefficient-tail representatives,
rather than products of individual homogeneous cocycles, control the
corresponding power operations. The formal E-infinity comparison in
the theorem determines them; no explicit Steenrod calculation is
being substituted for that proof.

## 2. Unbounded symmetric monoidal localization

I rechecked each step of the kernel argument. Q is exact and its
section R is right adjoint. Applying R to a K-injective complex
preserves K-injectivity because Hom(U,RJ)=Hom(QU,J) and Q takes
acyclic complexes to acyclic complexes. The termwise identity QR=id
therefore gives the derived counit; D(Q) is a genuine localization
with kernel exactly the complexes whose cohomology belongs to T.

T is stable under upward weight shifts: the inverse image under an
exact colimit-preserving shift is a localizing Serre class containing
every bounded-weight module. For fixed P in the derived kernel,
the V with P tensor_S^L V again in that kernel form a localizing
subcategory. It contains every compact projective generator S[-n]
and every cochain shift, since their tensor action is upward weight
shift. These generators detect all weightwise cohomology. Hence the
kernel is a derived tensor ideal, including in the unbounded category.
The opened HA2.2.1.9 criterion therefore applies without a hidden
bounded spectral-sequence assumption.

## 3. Fully faithful symmetric monoidal coefficient embedding

The exact adjunction Lbar left-adjoint sigma right-adjoint psi is used
in its actual directions. Exactness of Lbar makes sigma preserve
K-injectives; psi sigma=id termwise then proves the derived unit on
all unbounded complexes. Induction F(-)=(-) tensor_k S is derived
strong symmetric monoidal because S is k-flat. Q is strong monoidal
by the preceding localization, so sigma=QF is as well.

Full faithfulness on commutative algebra objects is legitimate:
tensor powers of every object in the image remain in the image,
and the equivalences of all mapping spaces lift the operations and
their coherent relations. This is an infinity-categorical statement,
not just a fully faithful functor of triangulated categories.

## 4. The comparison is an actual coherent algebra map

Strict DGAs and strict evaluation maps at simplices form a strict
cone. Restricting along a fixed cofibrant E-infinity operad and
localizing at underlying quasi-isomorphisms gives a homotopy-coherent
cone in CAlg(D(G)); strict composition relations supply all its
coherences. The universal property of the homotopy limit gives the
comparison map of E-infinity algebras. A model structure on strict
commutative DGAs is not assumed.

The natural PD Poincare maps S->A_n are quasi-isomorphisms of strict
DGAs, so the entire simplex diagram is equivalent to the constant
E-infinity algebra S. Its indexing nerve is homotopy equivalent to X.
The exact left adjoint L of F proves that derived F is also a right
adjoint on unbounded categories, hence preserves all homotopy limits.
Since algebra-object limits are computed on underlying objects, this
identifies the homotopy limit with F C*(X;k) as an E-infinity algebra.

The passage from ordinary sections to that homotopy limit is the
usual derived-sections comparison, not merely an unspecified map
with the right cohomology: restriction from Delta to the category of
elements Delta/X has an exact left adjoint given by the direct sums
over simplex fibers. It therefore preserves injectives and computes
the same derived sections. This checks the compatibility of the
algebra cone with the weightwise dimension-shifting comparison.

## 5. Why localization makes this map an equivalence

At weight w the ordinary-to-derived sections comparison is an
isomorphism through cohomological degree w. The form complex has no
terms above w. Thus in every fixed cohomological degree the cone has
bounded weight support. The cone belongs to D_T, so the actual
E-infinity comparison becomes an equivalence after Q. The fully
faithful sigma then recovers ordinary cochains with their full
coherent commutative structure.

All these arguments are weightwise and preserve products indexed by
arbitrary simplicial sets. They use C_gr=direct_sum_w Hom(X,A_w),
not the literal Hom(X,direct_sum_w A_w) when X is infinite.

## 6. Scope of the Mandell step

The recovered object is the ordinary integral E-infinity cochain
algebra, so the cited Mandell theorem applies to nilpotent finite-type
spaces as stated. It determines objects, not all maps. A binary product
in D(Z) alone would not suffice; the coherent cone and symmetric
monoidal localization are the essential extra steps audited above.

The explanatory paragraph added to D_enhancement.tex records the
weighted-unit distinction, the colax factor2, and the circle example.
No claim that L is monoidal has been introduced.
