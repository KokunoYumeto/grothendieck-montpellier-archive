# F54 Parts 2–3: identity traces, marked traces, and the actual nonstandard action

Author: /root/gct_statements, GPT-6 Astra Pro. Inherited effort is not exposed. Date: 2026-11-21 UTC.

This report gives complete new deductions from the previously checked actual rank-three algebra and tensor-lattice models F19/F21. It does not claim a source theorem about nonstandard RH or canonical bases. Part 1 of F54 is the separate genuine algebraic trace-classification report by /root/grothendieck_dictionary. The model and comparison axioms below are explicit, so the positive examples and obstructions have different, stated scopes.

## 1. The fixed actual algebra and module

Write

\[
\delta=v+v^{-1},\quad D=\delta^2,\quad
z_1=\frac{D-1}{D},\quad z_2=\frac{4(D-1)}{D^2},\quad
\Delta=z_1-z_2=\frac{(D-1)(D-4)}{D^2}.
\tag{T1}
\]

Over the finite localization

\[
S_0=\mathbb Q[v,v^{-1},\delta^{-1},(D-1)^{-1},(D-2)^{-1}],
\]

the established actual algebra and actual right tensor module are

\[
A=S_0\times S_0\times M_2(C),\qquad
C=S_0[x]/(x(x-\Delta)),
\tag{T2}
\]

\[
M=\epsilon_+^{20}\oplus\epsilon_-^4
       \oplus N(\delta)^{16}\oplus N(D-2)^4.
\tag{T3}
\]

The rank of M is 64. In the source's row-action convention,

\[
P_1|_{N(a)}=\begin{pmatrix}D&0\\a&0\end{pmatrix},\qquad
P_2|_{N(a)}=\begin{pmatrix}0&a\\0&D\end{pmatrix}.
\tag{T4}
\]

On the scalar sectors the named P_i act by D and 0, respectively. The regular F21 basis changes and the Morita branch identifications preserve these named operators. They use only the indicated finite localizations, including 2, which is invertible over Q. The central coordinate x has values 0 on N(delta) and Delta on N(D−2).

For real v>1, D>4, and therefore

\[
0<\Delta=(1-D^{-1})(1-4D^{-1})<1.
\tag{T5}
\]

At v=1, Delta has order exactly two, since

\[
D-4=(v-1)^2(v+1)^2/v^2
\]

and (D−1)/D² is a unit there.

## 2. A genuine trace-only model retaining the whole relative order

### 2.1 Exact formula

Fix the base parameter b=2. Put

\[
k=\frac{2500}{189},
\]

\[
a=3-v,
\]

\[
c=-v^3+2v^2+4v-8+k\Delta,\qquad d=c+k\Delta,
\]

\[
z=6v^3-6v^2-14v+30-6k\Delta.
\tag{T6}
\]

These are rational functions over Q. Direct collection of terms gives

\[
a+z+2c+2d=1+v+2v^2+2v^3=:S_H(v),
\tag{T7}
\]

\[
20a+4z+16c+4d=20+4v+16v^2+4v^3=:S_K(v).
\tag{T8}
\]

Also

\[
\Delta(2)=189/625,\quad k\Delta(2)=4,
\]

\[
(a,z,c,d)|_{v=2}=(1,2,4,8),\qquad
(a,z,c,d)|_{v=1}=(2,16,-3,-3).
\tag{T9}
\]

Thus there are three distinct nonzero sectors at the collision, while the two center branches collide to order two.

### 2.2 A single finite coefficient base supports every evaluation

Let S be obtained from S_0 by inverting a,z,c,d and

\[
a-z,\quad a-c,\quad a-d,\quad z-c,\quad z-d.
\tag{T10}
\]

This is a finite localization. Crucially, d−c=k Delta is not inverted.

Every inverted function is nonzero at v=1 by (T9). They are also nonzero at every v=2^n, n>=1. For n=1 this follows from (T9). At v=4 exact calculation gives

\[
(a,z,c,d)=
\left(-1,\frac{17007502}{83521},
-\frac{1192004}{83521},-\frac{379504}{83521}\right),
\]

so c<d<a<0<z.

For v>=8, (T5) gives

\[
d-a<-v^3+2v^2+5v-11+2k.
\]

The right side is negative at v=8: its value is −62095/189. Its derivative is −3v²+4v+5, negative for v>=8. Thus c<d<a<0 there.

For v>=4,

\[
z>6v^3-6v^2-14v+30-6k.
\]

The right side is positive at v=4, with value 11506/63, and its derivative 18v²−12v−14 is positive for v>=4. Hence z>0 throughout this range. These inequalities prove all the required separations at every 2^n. The base S_0 factors are nonzero at v=1 and every real v>1. Therefore the stated finite S admits the collision specialization and all arithmetic parameter evaluations used below.

### 2.3 Exact End/Hom realization

Keep C=S[x]/(x(x−Delta)) and let J=C as a free rank-two S-module. Give J the invertible operator

\[
F_J=c+kx.
\tag{T11}
\]

In the column basis (1,x),

\[
F_J=\begin{pmatrix}c&0\\k&d\end{pmatrix}.
\]

Its determinant cd is a unit. Since k is a unit,

\[
x=(F_J-c)/k,
\]

so, over S and after every coefficient base change,

\[
\operatorname{End}_{F_J}(J)=C.
\tag{T12}
\]

At the collision c=d=−3, and the nonzero lower-left entry k retains a genuine Jordan block.

Let S_r denote a scalar line with operator r, and put

\[
H=S_a\oplus S_z\oplus J^2,\qquad \operatorname{rank}_S H=6.
\tag{T13}
\]

The differences between the scalar sectors and the J sector are units: the determinants are (a−c)(a−d) and (z−c)(z−d), and a−z is a unit. Thus all cross-sector intertwiners vanish. Inside J², commuting with F is equivalent to being C-linear. Consequently, after every coefficient base change,

\[
\operatorname{End}_{F}(H)
  =S\times S\times M_2(C)=A_S.
\tag{T14}
\]

This is the actual whole relative order, not just the same generic or special algebra type.

Let

\[
L_0=C/(x),\qquad L_\Delta=C/(x-\Delta)
\]

with operators c,d, and define

\[
K=S_a^{20}\oplus S_z^4\oplus L_0^{16}\oplus L_\Delta^4,
\qquad \operatorname{rank}_S K=44.
\tag{T15}
\]

Again cross sectors vanish. Because J is the cyclic regular module,

\[
\operatorname{Hom}_F(J^2,L_i)=\operatorname{Hom}_C(C^2,L_i)
   =\operatorname{Row}(L_i).
\]

Precomposition gives the right matrix action. Hence

\[
\operatorname{Hom}_F(H,K)
 =\epsilon_+^{20}\oplus\epsilon_-^4
  \oplus\operatorname{Row}(L_0)^{16}
  \oplus\operatorname{Row}(L_\Delta)^4=M_S
\tag{T16}
\]

with exactly the F21 rank-64 tensor lattice and named P_i. This is not merely a dimension calculation. The regular branch comparison from F21 identifies the complete right action; the original tensor basis is recovered by its invertible matrix over S.

Postcomposition on K retains the complete actual ordinary left commutant as well. Over the domain S, cross-branch maps vanish because k Delta is a nonzero divisor, and

\[
\operatorname{End}_F(K)
  =M_{20}(S)\times M_4(S)\times M_{16}(S)\times M_4(S)
  \cong\operatorname{End}_{A_S}(M_S).
\tag{T17}
\]

The isomorphism is the explicit identification of multiplicity matrix units under (T16). At collision the two branch target sectors merge; both sides acquire all maps between their 16 and 4 multiplicities, and their dimension becomes

\[
20^2+4^2+20^2=816.
\]

Thus the model retains both actual actions with their specialization behavior. The conjugation operator on the invariant Hom is the identity by definition; this fact is independent of the scalar identity-trace comparisons next.

### 2.4 Both identity traces retune, but the spectra do not

At v=2, the H-spectrum is 1,2,4,8 with multiplicities 1,1,2,2, and the K-spectrum has multiplicities 20,4,16,4. Therefore (T7)–(T9) prove, for every n>=1,

\[
\operatorname{Tr}F_H(2^n)=\operatorname{Tr}(F_H(2)^n),
\]

\[
\operatorname{Tr}F_K(2^n)=\operatorname{Tr}(F_K(2)^n).
\tag{T18}
\]

These are genuine traces, with positive multiplicities, and the entire actual relative algebra/action model has been retained.

Full spectral retuning already fails at n=2: a(4)=−1, whereas every eigenvalue of F_H(2)^2 is positive. The base eigenvalues have integral weights 0,1,2,3 under v=sqrt(Q), with Q=4. It does not follow that the family at v=2^n has the corresponding weights, or even a mixture of integral weights at every parameter. For example a(8)=−5 has modulus 5, which is not 8^w for any integer w. Thus this model violates neither F51 nor the common-radius obstruction in F54 Part1.

It does prove that, in the unrestricted multiple-weight setting, even two genuine identity-trace systems and the whole actual order/action do not imply full spectral retuning or the F52 contact contradiction.

## 3. An explicit regular marked insertion

Put e=P_1/D and f=P_2/D, and define

\[
Z=e+f-ef-fe,\qquad
X=\frac{Z(z_1-Z)}{z_2}.
\tag{T19}
\]

Both expressions are regular at the collision and over S_0: D and z_2 are units. This X is not an unspecified abstract observable. It is a fixed rational expression in the actual named generators.

For any idempotents e,f, one has

\[
Ze=eZ=e-efe,\qquad Zf=fZ=f-fef,
\]

so Z, and hence X, is central in the generated algebra. On both scalar sectors Z=0. On N(a), multiplication of (T4) gives

\[
Z=(1-a^2/D^2)I.
\]

It follows that

\[
X|_{\epsilon_\pm}=0,\qquad
X|_{N(\delta)}=0,\qquad
X|_{N(D-2)}=\Delta I.
\tag{T20}
\]

Under (T2), X is zero on the scalar factors and the central coordinate x on the matrix factor. Equivalently, with

\[
B=D(P_1+P_2)-(P_1P_2+P_2P_1),
\]

\[
X=\frac{B((D-1)D-B)}{4(D-1)D^2}.
\tag{T21}
\]

On the actual rank-64 module, X has generic Delta-eigenspace of rank 8, and X(1)=0 as an operator. The latter is an exact consequence of the regular F21 splitting, not only the vanishing of its eigenvalues. On the cyclic auxiliary H in (T13), X at collision is a nonzero nilpotent in the J sector.

The arithmetic requirement tested below is the marked trace identity

\[
\operatorname{Tr}(X_{b^n}F_{b^n})
   =\operatorname{Tr}(X_bF_b^n)
\quad\hbox{for every sufficiently large }n.
\tag{T22}
\]

The left insertion is the actual parameter-dependent X at b^n; the right insertion is the fixed operator X_b. Identity-trace equality alone does not imply (T22). In particular, its rational coefficients in (T19) cannot silently be retuned inside a fixed-operator correspondence.

### 3.1 Scalar lemmas, with full proofs

Let g be an algebraic function over C(v), evaluated at v=b^n through places of the same function-field relation, where b>1. All functions are regular at the evaluations used, and polynomial coefficient poles exclude only finitely many parameters.

**Single exponential lemma.** If

\[
g(b^n)=C\alpha^n
\]

eventually, with C and alpha nonzero, then there are L>0 and m in Z such that

\[
g(v)^L=C^L v^m.
\tag{T23}
\]

To prove this, let P(v,Y) be its irreducible polynomial over C(v), cleared to a nonzero polynomial. Expanding P(b^n,C alpha^n)=0 gives a finite power sum whose roots are b^i alpha^j. Vandermonde uniqueness forces a collision between two distinct monomials. Their Y-exponents differ, since b>1, so alpha^L=b^m for some L>0,m in Z.

Restrict to n=Lr and set v=t^L. Then

\[
P(t^L,Ct^m)=0
\]

at infinitely many t=b^r, hence as a rational identity. The irreducible P has the root Ct^m in a finite extension, and consequently divides Y^L−C^L v^m over C(v). This proves (T23). In particular g is a unit at every place above v=1.

**Common-radius lemma.** Suppose

\[
g(b^n)=\sum_{j=1}^r \alpha_j^n
\tag{T24}
\]

eventually, with multiplicities included, all alpha_j nonzero and of a single modulus R. Then, for some L>0 and m in Z,

\[
g(v)^L=r^L v^m.
\tag{T25}
\]

Here is a direct proof of the needed scalar consequence of F54 Part1. Write alpha_j=R zeta_j with |zeta_j|=1, let s=log_b R, and put w_n=sum zeta_j^n, so w_0=r. Expand

\[
P(b^n,R^n w_n)=
\sum_{i,j}p_{ij}b^{(i+js)n}w_n^j.
\]

For each value h=i+js, the corresponding coefficient is a finite power sum on the unit circle. Distinct h give distinct absolute values of the resulting roots, so finite power-sum uniqueness makes every such coefficient sequence zero for every n, including n=0. Thus

\[
\sum_{i+js=h}p_{ij}r^j=0
\]

for each h. If s were irrational, each group would contain a single monomial, contradicting P nonzero and r>0. Write s=m/L. The grouped identities then say

\[
P(v,r v^{m/L})=0.
\]

Irreducibility gives (T25), as in the preceding proof. No integral-weight assumption or continuous evaluation sheet is required. In particular g cannot vanish above v=1.

**Several integral weights.** Suppose (T24) holds and

\[
\alpha_j=b^{w_j}\zeta_j,\qquad w_j\in\mathbb Z,\quad |\zeta_j|=1.
\]

Then

\[
g(v)=\sum_{j=1}^r v^{w_j},
\qquad g(1)=r.
\tag{T26}
\]

For completeness, expand P(b^n,sum b^{w_j n}zeta_j^n). After expanding every power, group terms by the integer exponent of b^n. Each remaining coefficient is a finite power sum of unit-modulus roots. Finite power-sum uniqueness makes each group vanish identically in n. At n=0, these grouped identities are exactly the Laurent coefficients of

\[
P\left(v,\sum_jv^{w_j}\right)=0.
\]

An irreducible polynomial over C(v) with that rational root is linear, proving (T26). Negative integral weights cause no problem because this argument takes place over C(v). This is the F51 mixed-integral trace argument, supplied here in the form needed for the marked insertion.

These lemmas use genuine positive multiplicities. No assertion is made for arbitrary virtual cancellation. For example, different finite-cover phases at another point over v=1 can cancel in an unrestricted multiple-fractional-weight sum.

### 3.2 One marked trace excludes a full relative centralizer, without weights

Suppose a finite free regular algebraic family H,F at a place above v=1 has full relative centralizer identified with the actual order A. Suppose its named central insertion X is the actual one in (T20), and suppose the same functions have regular evaluations at b>1 and all sufficiently large b^n.

Because F is central in its full centralizer, its component on the matrix-center factor is c_0+c_1 x. Let d=c_0+c_1 Delta be its value on the x=Delta branch. Generic full-centralizer semisimplicity implies that the two-by-two factor is the full endomorphism algebra of a two-dimensional eigenspace. Explicitly, F is a scalar tuple in the split semisimple algebra, so it is diagonalizable; different primitive central blocks have distinct eigenvalues, or the full centralizer would contain cross-block maps. Thus

\[
g(v):=\operatorname{Tr}_H(X(v)F(v))
      =2\Delta(v)d(v).
\tag{T27}
\]

At the base,

\[
\operatorname{Tr}_H(X_bF_b^n)=2\Delta(b)d(b)^n.
\]

The coefficient and eigenvalue are nonzero: Delta(b)>0 and F_b is invertible. If (T22) holds, the single exponential lemma makes g a unit at every point above v=1. But the right side of (T27) is regular and divisible by Delta, so it vanishes there. Contradiction.

This result needs no spectral-retuning assumption, purity, or weight restriction. It does require full relative-centralizer recovery and the specified marked trace comparison. The generic two-dimensional block and the regularity at the collision are part of its proof, not hidden scalar identities.

For the explicit model in Section 2, (T27) is 2 Delta d. The marked trace comparison would require

\[
2\Delta(v)d(v)=2\Delta(2)v^3
\]

at v=2^n. It already fails at v=4; the exact residual is

\[
-\frac{197896315512672}{4359848400625}\ne0.
\]

Thus the positive trace-only model supplies a concrete boundary test for this stronger axiom.

### 3.3 One marked trace on the actual tensor module: no full-centralizer hypothesis

Let M be the actual rank-64 tensor lattice over a finite algebraic coefficient extension regular at a place above v=1. Let F be an invertible regular algebraic family commuting with the actual A-action. Assume regular evaluations at b and all sufficiently large b^n.

At b>1, X_b/Delta(b) is the projection onto the actual N(D−2) sector, of dimension r=8. Since F_b commutes with X_b, this sector is invariant and its restriction is invertible. Denote its eight eigenvalues, with their genuine algebraic multiplicities, by alpha_1,...,alpha_8.

If (T22) holds, the algebraic scalar function

\[
g(v)=\Delta(b)^{-1}\operatorname{Tr}_M(X(v)F(v))
\]

satisfies (T24) with r=8. On the other hand X(1)=0, and regularity gives g(1)=0. Therefore (T22) is impossible in either of the following two independently sufficient cases:

1. The eight branch eigenvalues have one common absolute value. This includes a pure Weil realization on that sector, with no assumed integrality of the weight. Equation (T25) forbids a zero above v=1.
2. The eight branch eigenvalues have several integral weights, meaning |alpha_j|=b^{w_j} with w_j in Z. Equation (T26) gives g(1)=8, again a contradiction.

The first case does not require a rational or integral weight as an input; algebraicity of the proposed trace system forces the needed rational exponent in the proof. The second case allows different integral weights. The argument uses one complex embedding; an all-conjugate pure realization satisfies that hypothesis automatically.

This is an action-compatible obstruction, rather than a requirement that the actual algebra be the entire point-Weil endomorphism algebra. It retains the original tensor module and merely asks F to commute with its actual action. The same proof works if X(1) is nilpotent and commutes with F(1): then X(1)F(1) is nilpotent, hence has trace zero.

For unrestricted multiple spectral radii without integral weights, neither conclusion is asserted here. A scalar boundary is g=1+t on v=t²: its positive-sheet values over b^n are 1+(sqrt(b))^n, but it vanishes at t=−1 over v=1. This supplies no actual-action or full-order model. The positive identity-trace model in Section 2 does not supply (T22), and its existence does not remove this marked-trace gate.

## 4. Two fixed generator words exclude a composition-preserving comparison

There is an even smaller algebraic-coherence obstruction when the comparison is required to preserve two actual inserted words.

Let M_n be the actual tensor module at v=b^n, b>1, and let P_n be its named P_1. Let F_n be any invertible operators; no algebraic dependence on n is required. At the base require F_1 to commute with P_1. Suppose

\[
\operatorname{Tr}(P_n^jF_n)
   =\operatorname{Tr}(P_1^jF_1^n),
\qquad j=1,2,
\tag{T28}
\]

for every sufficiently large n. The operators inserted on the right are fixed actual base operators, and composition is preserved: the second is genuinely P_1 squared.

The actual relation is

\[
P_n^2=D(b^n)P_n,\qquad P_1^2=D(b)P_1.
\]

Consequently (T28) yields

\[
\bigl(D(b^n)-D(b)\bigr)
       \operatorname{Tr}(P_1F_1^n)=0.
\tag{T29}
\]

The function D(v)=(v+v^{-1})² is strictly increasing for v>1. Thus the first factor is nonzero for n>1, and the second must vanish eventually.

But P_1/D(b) is an idempotent of rank 40 on the actual tensor module: the contributions in (T3) are 20+16+4. Its image is invariant under F_1, and the invertible restriction has genuine eigenvalues lambda_i. Hence

\[
\operatorname{Tr}(P_1F_1^n)
  =D(b)\sum_i\lambda_i^n.
\]

A finite power sum on nonzero distinct roots, grouped with their positive integer multiplicities, cannot vanish for every sufficiently large n, by Vandermonde uniqueness. This contradicts (T29).

The proof requires neither purity, weights, algebraicity, a full centralizer, nor a collision specialization. It even does not use commutation of F_n with P_n away from the base. It is a finite two-word strengthening of the common-space obstruction F42 under the added, explicit action/composition requirement.

This does not exclude a graded coefficient-object dictionary in which the formal scalar D(v) is a varying object, and the quadratic relation is a tensor relation with that coefficient object. Such a dictionary is not the fixed scalar relation D(b) on the right side of (T28). Nor does the theorem exclude the separate word-dependent geometric objects of F45, or the K_0 coefficient kernels of F43. Those alternatives change exactly the comparison requirement used in the proof.

## 5. What has and has not been checked

The file verify_trace_frontier.py is a reproducible exact SymPy certificate for the rational trace identities, the collision/base values, the fixed values used in the all-n inequalities, the source row matrices, the central marked insertion, and the first marked-trace failure. Its output is saved separately. The inequalities for all 2^n and every impossibility theorem are proved above, not inferred from finitely many numeric tests.

The End/Hom and action assertions use the already explicitly proved F19/F21 local algebra and regular tensor-basis identities; their cyclic-source and multiplicity proofs have been supplied again in Section 2. The current work has not identified the designated arithmetic/grading/basis comparison or proved general canonical positivity. The fixed-parameter action and path constructions of F50/F53 remain valid. The present results reduce a broad comparison question to several concrete trace axioms and prove which ones are impossible in the actual small-rank model.

## 6. Separate dictionary paragraph for integration

The positive construction is a finite family of modules over the actual coherent center algebra, with a chosen linear automorphism and an exact invariant-Hom action comparison. The collision retains the algebra's nilpotent center even when identity power traces omit that information. The affine module/sheaf correspondence is the previously audited EGA I, Theorem 1.3.7 p86, Corollary 1.3.8 p87, and Theorem 1.4.1 pp90–92 framework; the specified action uses SGA 3 I, 4.7.2–3 and cote90 scan17.

The marked insertion is an actual regular central algebra element, so it belongs to the action dictionary rather than being recovered from an unmarked scalar trace. Its arithmetic trace identity is an additional comparison axiom. The two-word result further distinguishes composition-preserving operator traces on one fixed coefficient representation from changing coefficient objects with formal grading. No archival theorem is being substituted for these elementary proofs, and no Frobenius eigenvalue or purity convention is inferred merely from a coherent module.

