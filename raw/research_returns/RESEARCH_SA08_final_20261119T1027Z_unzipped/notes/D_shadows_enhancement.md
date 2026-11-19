# A.2/A.4: enhanced shadow recovery, with every categorical gate isolated

GPT-6 Astra (OpenAI, ChatGPT Pro mode), SA08 run, 19 November 2026.
This extends D.1--D.6. No priority is claimed. The root agent independently
suggested the same unbounded localization argument; this note checks it.

## D.6e. Unbounded and E-infinity recovery (Proved)

Let G=Gr_{>=0}(Gamma_k(T)), let T be the localizing Serre closure of bounded-
weight modules, and let Q:G->H=G/T have section R. Use the unbounded derived
infinity categories of these Grothendieck module categories, with derived
tensor products. Then the following statements hold.

1. The derived functor D(Q):D(G)->D(H) is a localization. Its kernel is
   D_T(G), the complexes all of whose cohomology modules lie in T.
2. This kernel is a tensor ideal. Consequently D(H) has the symmetric
   monoidal structure induced by the localization, and D(Q) is strong
   symmetric monoidal. This agrees with the tensor induced from graded
   tensor over S on the abelian quotient and its derived extension.
3. sigma=QF:D(k)->D(H) is fully faithful and strong symmetric monoidal.
   Hence CAlg(sigma):CAlg(D(k))->CAlg(D(H)) is fully faithful.
4. For every simplicial set X, the strict weighted PD-form DGA C_gr(X),
   regarded canonically as an E-infinity algebra, satisfies

       D(Q)(C_gr(X)) ~= sigma(C^*(X;k))

   in CAlg(D(H)), naturally in X. Thus its E-infinity algebra of ordinary
   cochains is recovered functorially, with a contractible space of choices,
   from the strict graded DGA and the fixed shadow category. One does not
   have to add an E-infinity structure to the supplied forms by hand.

Proof of (1). Since Q is exact, R sends K-injective complexes to K-injective
complexes: the Hom complex from an acyclic complex U to R(J) is the Hom
complex from the acyclic complex Q(U) to J. If J is a K-injective resolution
of an object of D(H), the termwise counit QR(J)=J proves D(Q) RR=Id.
Derived adjunction therefore identifies RR as fully faithful and D(Q) as
a localization. Exactness of Q identifies its kernel with D_T(G).
This also proves the assertion at the infinity level: mapping spectra
are the derived Hom complexes, and the adjunction is an adjunction of
those enhancements, not only of their homotopy categories.

Proof of (2). The kernel is localizing: D(Q) preserves colimits, and its
kernel is closed under cofibers and shifts. It is stable under every upward
weight shift because T is. Fix P in D_T(G). The full subcategory of V in
D(G) for which P tensor_S^L V belongs to D_T(G) is localizing, since
derived tensor preserves colimits separately. It contains every graded
free generator S[-n], n>=0, as tensoring with this generator is upward
weight shift. The objects S[-n], together with cohomological shifts,
compactly generate D(G): a complex with zero derived Hom from all of
them has every weightwise cohomology group zero. Therefore this
subcategory is all D(G). This proves the tensor-ideal assertion without
an unbounded tensor spectral sequence. The symmetric monoidal
localization universal property now supplies (2). On modules its tensor
is Q(P tensor_S M); the higher tensor comparisons are obtained using
resolutions by graded free modules and colimits. Thus the construction
agrees with the derived tensor on the abelian quotient, rather than merely
postulating a second unrelated tensor structure there.

Proof of (3). D.5 supplies exact adjoints Lbar left adjoint to sigma left
adjoint to psi, with psi sigma=Id and sigma exact. If I is K-injective over
k, then sigma I is K-injective in H: for every acyclic U in H,

    Hom_complex(U,sigma I)=Hom_complex(Lbar U,I)

is acyclic because Lbar is exact. For a K-injective replacement K->I,
Rpsi(sigma K)=psi sigma I=I. This proves the unit equivalence for arbitrary
unbounded K, and hence full faithfulness as stable infinity categories.
Induction F is strong symmetric monoidal because S is k-flat and
F(K) tensor_S^L F(L)=F(K tensor_k^L L). Compose with (2).
A fully faithful symmetric monoidal functor is fully faithful on
commutative algebra objects: the diagrams expressing the multiplication,
unit and all higher coherences have mapping spaces computed in the source
by full faithfulness. Equivalently apply full faithfulness levelwise to
the defining diagrams over finite pointed sets and their Segal limits.
An E-infinity algebra in the target whose underlying object is in the
image lifts uniquely up to a contractible space, because all its tensor
powers are also in the image and all structure maps and coherences lift.

Proof of (4). Fix a cofibrant E-infinity operad E with its augmentation
E->Com. Restriction along this augmentation views every strict CDGA as
an E-algebra; after derived localization this gives an object of CAlg of
the derived category. This is the usual enhancement of a strict CDGA,
and introduces no choices depending on X. Its underlying object is the
original chain complex in the derived category. It is not necessary to
assert a model structure on strict commutative DGAs over torsion rings.
Only the E-infinity algebra model, or the equivalent infinity category,
is used here.

Let I_X be the simplex category of X, with objects x:Delta[n]->X. Its
projection p:I_X->Delta is a discrete fibration. The diagram

    I_X^op -> strict CDGAs in G,       (n,x) |-> A_n^bullet

has ordinary limit exactly C_gr(X): limits in G are taken weightwise,
so no exchange of Hom with infinite direct sums occurs. Evaluation at
each simplex gives a strict DGA cone from C_gr(X), hence an E-infinity
cone after the preceding enhancement. By the universal property of the
infinity-categorical limit, this cone induces a canonical E-infinity map

    C_gr(X) -> holim_{I_X^op} A_n^bullet.                         (*)

The universal PD Poincare contraction proves that S->A_n^bullet is a
quasi-isomorphism of strict DGAs for every n, naturally in simplicial
operators. Therefore it is an equivalence of E-infinity diagrams, and

    holim_{I_X^op} A_n^bullet ~= holim_{I_X^op} S.

The latter is F(C^*(X;k)) as an E-infinity algebra. Indeed the nerve of
I_X has the homotopy type of X, and the homotopy limit of the constant
E-infinity k-algebra k over that space is the E-infinity algebra of
ordinary cochains. The exact adjunction L left adjoint to F persists on
unbounded derived categories, so F preserves limits. It is strong
symmetric monoidal, and therefore also preserves these limits of
commutative algebras, whose limits are computed on underlying objects.

For clarity, the underlying map (*) is precisely the ordinary-to-derived
sections map used in D.6. Restriction p^* on module presheaves preserves
injectives: its left adjoint has, at [n], the direct sum over x in X_n
of the values at (n,x), and is exact. Hence Rlim p^* computes R Gamma_X.
The resolution edge isomorphism in weight w is valid in cohomological
degrees <=w, while C_w vanishes in higher degrees. The cone of (*) has
cohomology supported in finitely many weights in each degree, so belongs
to D_T(G). Apply the strong symmetric monoidal localization D(Q).
It turns (*) into an E-infinity equivalence, proving (4).

There is no inference here from equality of binary cohomology products
to equality of E-infinity structures. The comparison was built as an
E-infinity map before its underlying equivalence was proved. Nor does
this say that recovering only the ring H^*(X;k), or only the product in
D(k), recovers the E-infinity algebra. The strict weighted DGA provides
the input cone and all its commutative-algebra coherences.

## Consequence for the main user's A.4 homotopy clause

Over Z, apply Mandell's 2006 Main Theorem to the recovered E-infinity
cochain algebra. On nilpotent spaces of finite type, the strict weighted
PD-form cochains determine the integral weak homotopy type. This is a
determination statement, not a claim that the cochain functor is full.
The statement uses the whole graded cochain object; the graded
cohomology algebra alone has much less information. The independent
binomial associated-graded claim can still fail, and its failure does
not invalidate this enhanced shadow argument.

## Literature and scope notes

The elementary exact adjoints were already present in the attached
Pro notes N32--N33 and N71. The enhanced argument above was independently
checked in this run; no priority is claimed. Search terms used included
"category of simplices weak equivalence nerve" and
"E-infinity cochains homotopy limit constant". The category-of-simplices
weak equivalence is Hirschhorn, Model Categories and Their Localizations,
Theorem 18.9.3; the author's paper The Diagonal of a Multicosimplicial
Object, proof of Proposition 9.6, explicitly invokes that theorem and
was opened at https://math.mit.edu/~psh/diagncosimplicial.pdf. The book
PDF URL tried was inaccessible; do not mark the full book opened.
Related literature found and opened: Richter--Sagave, A strictly
commutative model for the cochain algebra of a space, Compositio Math.
156 (2020), 1718--1743, arXiv:1801.01060. Their commutative I-diagrams
are a different strict model, so this is a comparison reference, not a
source claimed to prove the exact shadow theorem above.
The root agent has opened Lurie's Higher Algebra for the symmetric
monoidal localization and commutative-algebra limit formalism, and
Mandell's paper for the exact scope of the concluding application.
