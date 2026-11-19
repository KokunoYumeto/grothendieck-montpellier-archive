# A cusp conjugator outside the proper-homology completion

19 November 2026. Exact group counterexample to the proposed implication

\[
 f^{-1}yf\in\mathcal H_c
 \quad\Longrightarrow\quad
 f\in\mathcal H_c C_G(y).
 \tag{CC.0}
\]

The groups and actual cover maps are exactly those of E.2.30. This constructs a specified element of the free profinite group. It does not construct an automorphism with all peripheral conditions or an element of the arithmetic Galois image. It is therefore a tested limitation of this particular intermediate implication, not a conclusion about the full E.2 gate.

## CC1. The actual local fixed spaces and transition map

Let F=<x,y>, G=Fhat, and retain

\[
 1\longrightarrow\widehat A_N^c\longrightarrow P_N^c
  \longrightarrow Q_N\longrightarrow1,
 \qquad A_N^c=H_1(C_N,\mathbb Z),
 \qquad\Gamma_N^c=F/L_N.
\]

Write y_N for the actual image of y in P_N^c. Its conjugation action on the abelian kernel is the deck action of its image in Q_N. Define

\[
 Z_N^y=(\widehat A_N^c)^{y_N},\qquad
 T_N^y=\Gamma_N^c Z_N^y\subset P_N^c.
 \tag{CC.1}
\]

The product is a subset; no subgroup claim is used. For gamma in Gamma_N^c and z in Z_N^y,

\[
 (\gamma z)y_N(\gamma z)^{-1}=\gamma y_N\gamma^{-1}
       \in\Gamma_N^c. \tag{CC.2}
\]

Let M⊂N be open normal subgroups. The actual compactified morphism

\[
 \pi:C_M\longrightarrow C_N
\]

is a finite holomorphic map of degree e=[N:M]. It may be branched at the filled cusps. Its pushforward on integral H1 is the same map as the restriction of P_M^c→P_N^c to the abelian kernels: both maps are induced by the original map of pointed covers and the filling homomorphisms.

Define the integral umkehr by oriented Poincare duality:

\[
 \pi^!=\operatorname{PD}_{C_M}^{-1}\pi^*
                     \operatorname{PD}_{C_N}:
 H_1(C_N,\mathbb Z)\longrightarrow H_1(C_M,\mathbb Z).
 \tag{CC.3}
\]

One has pi_*pi^!=e id. For completeness, for integral classes a,b, pairing pi_*pi^!a with b on C_N gives the cup-product pairing of pi^*PD(a) and pi^*PD(b) on C_M, which is e times the pairing on C_N because pi has oriented degree e. The integral intersection pairing is unimodular; equality of all such pairings gives the identity integrally. This argument remains valid for a branched map of compact oriented surfaces.

The actual deck transformations satisfy pi y_M=y_N pi, so naturality of pullback, pushforward and oriented Poincare duality gives

\[
 \pi^! (A_N^c)^{y_N}\subset (A_M^c)^{y_M},
 \qquad
 \pi_*\pi^!=e\,\mathrm{id}. \tag{CC.4}
\]

The invariant lattice is the kernel of the integer matrix y_N−1. Smith normal form shows that completion preserves this exact kernel:

\[
 Z_N^y=(A_N^c)^{y_N}\otimes\widehat{\mathbb Z}.
 \tag{CC.5}
\]

Indeed, after integral changes of basis the matrix is diagonal; every nonzero diagonal entry acts injectively on Zhat. Completing (CC.4) now gives the actual image inclusion

\[
 \pi_*(Z_M^y)\supset e Z_N^y. \tag{CC.6}
\]

## CC2. Surjectivity of the compatible sets

The transition T_M^y→T_N^y is surjective. Given gamma z in T_N^y, choose an integral invariant a_0 in (A_N^c)^y representing z modulo e Z_N^y; it exists by (CC.5). Then

\[
 z'=\pi^!((z-a_0)/e)\in Z_M^y,
 \qquad\pi_*z'=z-a_0.
\]

Choose gamma' in Gamma_M^c mapping to gamma a_0; the discrete quotient transition is onto by E.2.30. The product gamma' z' belongs to T_M^y and maps exactly to gamma z. Thus neither surjectivity of the centralizer transition by itself nor compactness of a nonclosed set is needed.

## CC3. The explicit A5 starting cover and its quotient genus

Take the exact monodromy of E.2.29, namely x=(123) and y=(12345) on five letters, with the same permutation-composition convention as its frozen certificate. Their product has order5, they generate A5, and the actual regular cover has degree60. The three inertia orders are3,5,5. Riemann--Hurwitz gives

\[
 2g(C)-2=60(-2+(1-1/3)+(1-1/5)+(1-1/5))=16,
\]

so g(C)=9. Put N_0=ker(G→A5).

Let H=<y>, of order5. Each branch fibre of inertia order5 consists of the twelve cosets A5/I, with I a subgroup of order5. Exactly two of them are fixed by H: the cosets with gIg^{-1}=H are counted by |N_{A5}(H)|/|I|=10/5=2. All subgroups of order5 are conjugate. The order3 fibre has no H-fixed point. A nonidentity element of H generates H, so each of the four nonidentity elements fixes exactly four points in C, two above each order5 branch point. Therefore

\[
 16=5(2g(C/H)-2)+4(5-1),
 \qquad g(C/H)=1. \tag{CC.7}
\]

The actual quotient map and averaging give

\[
 H_1(C,\mathbb Q)^H\simeq H_1(C/H,\mathbb Q),
 \qquad\operatorname{rank}(A_{N_0}^c)^y=2.
\]

Here the finite-dimensional invariant assertion is also independently verified by the following explicit integral vector, so no unstated integral descent assertion for the branched quotient is required.

Use the frozen 61-dimensional affine cycle basis, saturated boundary module B, and matrices Y and E from E.2.29. The integer operator Q=60I−E kills B and satisfies Q^2=60Q. The matrix

\[
 R=(I+Y+Y^2+Y^3+Y^4)Q
\]

has rank2. Its first nonzero column, with zero-based index1, is the vector w recorded in work/A5_y_fixed_proper_vector.json. Its first coordinate is9, and direct exact calculations give

\[
 Yw=w,\qquad Ew=0,
 \qquad qB=0,\qquad qw=540,
 \quad q=Q_{0,*}. \tag{CC.8}
\]

Thus its proper class v=[w] in A_{N_0}^c is a nonzero integral y-invariant class. The functional q descends to the actual proper lattice and detects v by540. Let a in Zhat have a_2=0 and a_p=1 for every odd prime. Put

\[
 z_0=a v\in Z_{N_0}^y. \tag{CC.9}
\]

This vector is not integral: if it were, its integral detector would be the integer540a. The 2-adic coordinate of that integer would be0, forcing the integer itself to be0, whereas its 3-adic coordinate is the nonzero element540. In particular z_0 is not in Gamma_{N_0}^c, since Gamma_{N_0}^c intersects Ahat_{N_0}^c exactly in A_{N_0}^c.

## CC4. A specified compatible element

The following recursion fixes the compatible element without an unspecified choice of inverse-limit branch. Order the alphabet x,x^{-1},y,y^{-1} as written, and order reduced words by length and then lexicographically. Let N_n be N_0 intersected with all kernels of homomorphisms G→S_j for j≤n. Put N_0 at the start of this descending sequence; repeated equal levels cause no problem. This is a specified cofinal normal chain.

Start with the word g_0=1 and the vector z_0 of (CC.9). Suppose g_n in F and z_n in Z_{N_n}^y have been defined. Let e_n=[N_n:N_{n+1}]. Choose the first reduced word u_n in this ordering such that u_n belongs to K_{N_n}, its proper class a_n is y-invariant, and

\[
 z_n-a_n\in e_n Z_{N_n}^y.
\]

Such a word exists because (A_{N_n}^c)^y surjects onto its quotient modulo e_n, and K_{N_n} surjects onto the proper lattice. Define

\[
 g_{n+1}=g_nu_n,\qquad
 z_{n+1}=\pi_n^!((z_n-a_n)/e_n),\qquad
 t_n=(g_n\bmod L_{N_n})z_n\in T_{N_n}^y.
 \tag{CC.10}
\]

The transition takes t_{n+1} exactly to t_n: the image of u_n is a_n in the abelian kernel, and the image of z_{n+1} is z_n−a_n. Formula (E.2.30g) therefore gives a unique f_0 in G having these coordinates. This specification uses the original covers and their oriented umkehr maps; it makes no assertion about algorithmic recovery of arbitrary profinite data.

Its initial coordinate is z_0, so f_0 is not in H_c. By (CC.2), every coordinate of f_0 y f_0^{-1} is an element of Gamma_N^c. Cofinality and the definition of H_c give

\[
 f_0\notin\mathcal H_c,
 \qquad f_0 y f_0^{-1}\in\mathcal H_c. \tag{CC.11}
\]

Set f=f_0^{-1}. Then f^{-1}yf belongs to H_c, while f does not.

## CC5. The exact centralizer and the refuted implication

Bux--Ershov--Rapinchuk, original Groups Geom. Dyn.5(2011), Corollary2.3 and proof, printedp332, prove for a specified generator of a free profinite group

\[
 C_G(y)=\overline{\langle y\rangle}=y^{\widehat{\mathbb Z}}.
 \tag{CC.12}
\]

The proof was reopened in the complete original journal PDF on19November2026: https://ems.press/content/serial-article-files/29591, web reference turn204474384view0, PDFpage6. It derives the equality from the explicit finite relation-module Proposition2.2(i), pp330--331, so applies to this exact generator and actual free profinite completion.

By E.2.30 the full group y^Zhat is contained in H_c. Hence H_c C_G(y)=H_c, and the specified f above satisfies

\[
 f^{-1}yf\in\mathcal H_c,
 \qquad f\notin\mathcal H_c C_G(y). \tag{CC.13}
\]

This refutes (CC.0). The proof uses actual proper homology and its integral transfer, not a replacement lattice or independent local choices. It says nothing yet about whether the assignments x↦x and y↦f^{-1}yf define an automorphism, preserve the third peripheral class, or occur simultaneously in the arithmetic Galois image. Those are the next exact maps to test.

## Checks and files

Triangle independently passed the entire transition argument, including integral Poincare-duality transfer for branched covers, kernel completion by Smith form, and surjectivity of the sets T_M^y→T_N^y. It extracted the exact vector and detector in (CC.8) from the frozen A5 matrix data.

The finite certificate work/code_generation/check_cusp_conjugator_seed.py verifies the monodromy group, normalizer counts and all quotient-genus identities, and reconstructs w and q from the frozen JSON. The infinite compatible element and its properties are proved above; no finite program is claimed to enumerate that element.
