# A.2: verified shadow reconstruction

Author: GPT-6 Astra (OpenAI, ChatGPT Pro mode), research run SA08, 19 November 2026.
This note records independently checked arguments. No priority is claimed.

## Provenance and a correction to the prompt

The prompt's R4 says that the general graded Ext corollary is unproved. That is
inconsistent with the attached `MPL_136_235-281_notes.md`, N32--N33, lines 304--328:
those notes supply the exact left adjoint used below. N71, lines 646--654, also
supplies the corrected localizing quotient and the derived recovery mechanism.
The attached reading `136_282-376.md`, lines 40--50, explicitly records both
results. We have independently re-proved the claims, including the exactness
step and the derived unit. This is a correction of a status report, not a claim
of a new theorem.

## D.1. Exact coefficient extraction (Proved)

Let k be any commutative ring, S=Gamma_k(T)=direct-sum_{n>=0} k e_n, with
e_a e_b=binom(a+b,a)e_{a+b}. Let G=Gr_{>=0}(S) be the abelian category of
nonnegative graded left S-modules, with degree-zero S-linear morphisms. Put
F(M)=M tensor_k S, where M is a k-module in weight zero. There are adjunctions

    L : G <--> Mod(k) : F,       F : Mod(k) <--> G : kappa,

where kappa(P)=P_0 and

    L(P) = (direct-sum_{n>=0} P_n) /
      < [e_a x]_{n+a} - binom(n+a,n)[x]_n : x in P_n, a,n>=0 >.

The three functors L,F,kappa are exact, and L F = kappa F = identity.

Proof. A map from the displayed quotient to M is exactly a family f_n:P_n->M
such that f_{n+a}(e_a x)=binom(n+a,n)f_n(x). This is exactly a graded S-map
P->F(M), proving L adjoint to F. The other adjunction is ordinary induction and
weight-zero evaluation. Exactness of F and kappa is immediate, since every
S_n is the free rank-one k-module.

We prove exactness of L rather than assuming it. Localize at an arbitrary
rational prime p. Write r_j=p^j-1. All binom(r_j,n), 0<=n<=r_j, are units in
Z_(p): modulo p, (1+z)^(p^j-1)=(1+z^(p^j))/(1+z), whose coefficients through
degree r_j are (-1)^n. Define a directed system P_{r_j} with transition

    x |-> e_{r_l-r_j}x / binom(r_l,r_j)       (l>=j).

The identity

    binom(r_l,r_j) binom(r_j,n)
      = binom(r_l,n) binom(r_l-n,r_j-n)

makes the transition maps compose correctly. The map from P_n to its colimit
is represented, for any r_j>=n, by e_{r_j-n}x/binom(r_j,n). The same identity
shows independence of j and all defining relations of L(P). Conversely the
maps P_{r_j}->L(P), x-> [x]_{r_j}, are compatible, since the relations identify
e_{r_l-r_j}x with binom(r_l,r_j)x. These two maps are inverse. Consequently

    L(P) tensor_Z Z_(p) = colim_j (P tensor_Z Z_(p))_{r_j}.

The expression on the right is exact in P. Localization commutes with the
presentation of L. A sequence of abelian groups is exact iff its localization
at every rational prime is exact; hence L is exact for every k. Finally,
the relation at n=0 identifies [m e_n] with [m e_0], so L F(M)=M.

## D.2. All finite tails, all higher Ext (Proved)

For N>=0, let G_N be the category of graded S-modules supported in weights
>=N, tau_N:G->G_N the exact weight truncation, and j_N:G_N->G its exact
inclusion. Then j_N is left adjoint to tau_N; hence tau_N preserves injectives.
Let rho_N be the right adjoint to tau_N. It exists explicitly, with

    (rho_N P)_i = Hom_{G_N}(tau_N(S[-i]),P),       i>=0.

Here S[-i]_n=S_{n-i}, so S[-i] is generated in weight i. For every k-module M,
every N>=0 and every i>=0, the canonical map

    M -> Hom_G(tau_N(S[-i]),F(M))

sends m to multiplication by m e_i and is an isomorphism. Moreover

    Ext^q_G(tau_N(S[-i]),F(M))=0,                 q>0.

These Ext groups are also the Ext groups in all integer-graded S-modules:
tau_N(S[-i]) has a projective resolution by sums of S[-d], d>=0, which are
projective in both categories. The assertion does not extend to arbitrary
negative i, and it does not refer to ungraded Ext.

Proof of Hom. By D.1 this Hom is Hom_k(L tau_N(S[-i]),M). The natural map
tau_N(S[-i])->S[-i] induces an isomorphism on L, because its cokernel has
bounded weights and L kills bounded-weight modules: locally at p its
colimit description is eventually zero. Also L(S[-i])=k. Indeed the map to k
is induced by e_{n-i}->binom(n,i), and after localization at p its value at
r_j is a unit for all sufficiently large j. Thus the Hom isomorphism is
exactly multiplication by e_i.

Proof of Ext. Since L is exact and left adjoint to F, F preserves injectives.
If M->I^bullet is a k-injective resolution, F(M)->F(I^bullet) is an injective
resolution in G. Apply Hom_G(tau_N(S[-i]),-) and the preceding Hom
isomorphism: the resulting cochain complex is I^bullet. Its positive
cohomology is zero. This proves the corollary of cote 136, scans 27 and 265,
for all the stated rings, modules and indices.

## D.3. Finite-tail derived unit (Proved)

Let sigma_N=tau_N F and psi_N=kappa rho_N. The functors satisfy
sigma_N left adjoint to psi_N; sigma_N is exact and fully faithful. On
bounded-below derived categories, the adjunction unit

    K -> R psi_N(sigma_N K)

is an isomorphism for every K in D^+(k). In particular sigma_N:D^+(k)->D^+(G_N)
is fully faithful.

Proof. F and tau_N preserve injectives, hence sigma_N preserves injectives.
For a bounded-below injective resolution K->I^bullet, sigma_N I^bullet is a
bounded-below injective resolution of sigma_N K. The underived unit, D.2 at
i=0, identifies psi_N sigma_N I^bullet with I^bullet. This proves the derived
unit, and the derived adjunction gives full faithfulness. No illegitimate
composition of derived functors is used.

## D.4. The literal negligible classes must be distinguished (Refuted / corrected)

The class E of modules each of whose homogeneous elements generates a module
with bounded weights need not be extension closed. Let k=F_p and
S=Gamma_k(T), I=S_{>0}. Using the elementary p-digit presentation
S=k[x_0,x_1,...]/(x_j^p), deg x_j=p^j, the quotient I/I^2 is the direct sum of
one copy of k in each weight p^j and is annihilated by I. Thus I/I^2 and
S/I=k are in E. In the exact sequence

    0 -> I/I^2 -> S/I^2 -> k -> 0,

the class of 1 in S/I^2 generates the whole module, which has nonzero
components in the unbounded weights p^j. Hence S/I^2 is not in E.

The bounded-weight class B is Serre, but is not closed under arbitrary direct
sums: the sum of k[-j], j>=0, is not bounded. Thus B and E do not provide the
same quotient, and neither should be silently assigned all the properties
of a localizing Serre subcategory. This is an infinite algebraic
counterexample, proved directly, not a finite computational certificate.

## D.5. A precise infinite-shadow category and its derived unit (Proved)

Let T be the smallest localizing Serre subcategory of G containing B, let
Q:G->G/T be the Gabriel quotient, and let R be its fully faithful right
adjoint (section functor). These constructions are in the category of
modules over the small graded ring category, hence G is Grothendieck.
The exact functor L kills T: its kernel is localizing Serre, since L is
exact and preserves all colimits, and it contains B. Thus L factors through
an exact functor Lbar:G/T->Mod(k).

For sigma=QF and psi=kappa R there are adjunctions

    Lbar left adjoint to sigma left adjoint to psi,

with sigma exact. Moreover RQF(M)=F(M), R^q R(QF(M))=0 for q>0, and

    Id_{D^+(k)} -> R psi sigma

is an isomorphism. Thus sigma:D^+(k)->D^+(G/T) is fully faithful.

Proof of saturation. By the exact adjunction D.1, for V in T,
Ext^q_G(V,F(M))=Ext^q_k(L(V),M)=0 for every q>=0. The q=0,1 cases say
precisely that F(M) is T-local, i.e. F(M)=RQF(M). To avoid relying on a
criterion without a proof, the counit/unit map F(M)->RQF(M) has torsion
kernel and cokernel. Its kernel is zero by Hom(T,F(M))=0. The extension by
its torsion cokernel splits by Ext^1(T,F(M))=0, and RQF(M), being a section
object, has no torsion subobject; hence the cokernel is zero.

The adjunction Lbar to sigma follows by the quotient universal property, or
by Hom_{G/T}(QP,QF(M))=Hom_G(P,F(M))=Hom_k(L(P),M), using saturation.
Exactness of Lbar implies that sigma preserves injectives. If M->I^bullet
is an injective resolution, sigma I^bullet is injective in G/T and
R sigma I^bullet=F(I^bullet). Since F is exact this proves the higher
vanishing for R. Applying kappa proves the derived unit. The same argument
works for bounded-below complexes. This settles the mathematically repaired
form of the question mark on scan 273; it does not identify the manuscript's
ambiguous negligible category with this quotient.

## D.6. The multiplicative derived reconstruction (Proved)

For every simplicial set X and commutative ring k, let

    C_gr(X)=direct-sum_w Hom_sSet(X,A_w^bullet)

be the genuine weight-graded PD-form complex. There is a natural comparison
in the derived category of graded S-modules,

    c_X:C_gr(X) -> F R Gamma(X;k).

After applying Q it is an isomorphism. It respects multiplication in the
derived category. In particular, for k=Z the pair consisting of R Gamma(X;Z)
and its product in D(Z) is recovered functorially from Q C_gr(X), hence from
the weighted forms with their products, by R psi. The ordinary cohomology
ring is recovered as well. This assertion concerns the product as a morphism
in D(Z); it does not assert recovery of an E_infinity enhancement.

Here are the construction and its multiplicative verification, without
assuming that agreement on cohomology determines derived products.
Let B=sG be the abelian category of simplicial nonnegative graded S-modules.
Write F_s:sMod(k)->B for induction in every simplicial degree. Its exact
left adjoint is L applied in each simplicial degree, so F_s preserves
injectives. For a fixed simplicial set X, let

    Gamma_X:B->G,       (Gamma_X V)_w=Hom_sSet(X,V_w).

This is right adjoint to the exact functor P|->S[X] tensor_S P, where S[X]
is the free simplicial S-module on X, concentrated in weight zero as free
generators. Each S[X]_n is free, so this tensor functor is exact. Hence the
ordinary comparison from Gamma_X to R Gamma_X is defined on bounded-below
complexes. Moreover Gamma_X F_s=F Gamma_X on the nose. Taking a bounded-below
injective resolution in sMod(k), and using preservation of injectives by
F_s, gives a natural isomorphism

    R Gamma_X(F_s k) = F R Gamma_X(k).

The universal PD Poincare contraction of A-001 supplies a quasi-isomorphism
of differential graded algebras in B,

    F_s k -> A^bullet.

The map c_X is the ordinary-to-derived comparison
Gamma_X(A)->R Gamma_X(A), followed by the inverse of R Gamma_X(F_s k)->
R Gamma_X(A). Its cohomology in weight w is exactly the resolution edge
comparison of A-001/A-003. Thus it is an isomorphism in degrees q<=w;
C_w has no terms in degrees q>w. The cohomology of Cone(c_X) in any fixed
degree is consequently supported in only finitely many weights (contained
in 0<=w<q, with the evident harmless shift under the cone convention).
Those modules belong to B, hence to T. Since Q is exact, Qc_X is a
quasi-isomorphism. This handles infinite X because every construction here
is performed weight by weight, rather than interchanging a Hom with an
infinite direct sum.

For multiplication, use the diagonal of the free simplicial coalgebra
S[X], sending [x] to [x] tensor[x]. Derived adjunction gives the natural
pairing

    R Gamma_X(U) tensor_S^L R Gamma_X(V)
          -> R Gamma_X(U tensor_S^L V).

Explicitly, its adjoint is evaluation after the diagonal:
S[X] tensor (R Gamma_X(U) tensor^L R Gamma_X(V)) maps, by the diagonal,
to (S[X] tensor R Gamma_X(U)) tensor^L
(S[X] tensor R Gamma_X(V)), and then to U tensor^L V by the two derived
evaluation maps. All these maps are typed in D(B); the source tensor with
S[X] is already derived because S[X] is objectwise free. Coassociativity,
counit and cocommutativity of the diagonal give the associativity, unit
and symmetry compatibilities. The ordinary evaluation maps define the
ordinary-to-derived comparison by the same adjunction. The two possible
composites for its multiplicativity have, under that adjunction, the same
evaluation-after-diagonal map. They are therefore equal in the derived
category. This proves that the comparison is multiplicative, not just that
its induced map on cohomology is multiplicative.

Each A^q is degreewise graded S-free, by choosing the simplex basis
(T,X_1,...,X_n). The first-quadrant tensor complex A tensor_S A resolves
S: its two successive homology spectral sequences have only S in degree
zero. Therefore the ordinary DGA multiplication represents precisely the
derived multiplication transported from S. Applying the preceding pairing
shows that c_X carries the actual form product to the ordinary derived cup
product on F R Gamma_X(k).

To make the shadow tensor product precise, T is stable under upward shifts:
the inverse image of T under such a shift is localizing Serre and contains
all bounded-weight modules, hence contains T. For P in T and any graded
module M, take a graded free resolution of M by sums of S[-d], d>=0.
Tensoring with P has all terms in T, so all Tor_n^S(P,M) belong to T.
Thus tensor descends to G/T and its derived localization. Induction F is
strong symmetric monoidal, with

    F(K) tensor_S^L F(L) = F(K tensor_k^L L).

The quotient sends flat modules to flat objects, since its tensor product
is induced by tensor in G and exact sequences in the quotient can be
represented by exact sequences upstairs. Hence this strong monoidality
also holds for sigma on the derived images in question. For k=Z, bounded-
below derived tensor products remain bounded below (Z has global
dimension one). D.5 now gives full faithfulness on the source, and c_X
identifies Q C_gr(X) with sigma R Gamma(X;Z). Applying the inverse on the
essential image, R psi, recovers both the object and its unique product.
For arbitrary k the same statement is valid in the unbounded derived
categories, using K-injective resolutions: the exact left adjoint Lbar
implies that sigma preserves K-injectives, and psi sigma=Id then proves
the unbounded derived unit by the same calculation. Equivalently one may
stay bounded below wherever the indicated derived tensors stay in that
category.

The literal complex Hom(X,direct-sum_w A_w) is a different object for
infinite X, as A-004 proves. The theorem explicitly applies to the graded
complex named in A.2; it cannot identify that graded object with the literal
one without an additional hypothesis. The existence of c_X and its
multiplicativity close the conditional comparison gate in the earlier
version of this note.

## Alternative independent check of D.2

For a p-local coefficient module M, the quotient of F(M) in weights <=r,
r=p^j-1, is naturally the right adjoint of weight-r evaluation applied to M:
its degree-n component is identified with Hom_k(S_{r-n},M) by multiplication
by binom(r,n). Every such binomial is a p-unit. These quotients are
Ext-acyclic against tau_N(S[-i]), because its weight-r component is k.
Their Hom groups are M, with identity transition maps under the
multiplication-by-e_i parameterization. The two-product resolution of the
inverse limit proves the same Ext vanishing. For arbitrary k, every
injective k-module is a retract of a product of the p-local injectives
Hom_Z(k,Q_p/Z_p): the product of Q_p/Z_p is an injective cogenerator of
abelian groups. Graded products commute with F. This gives a second proof
independent of the left-adjoint calculation.
