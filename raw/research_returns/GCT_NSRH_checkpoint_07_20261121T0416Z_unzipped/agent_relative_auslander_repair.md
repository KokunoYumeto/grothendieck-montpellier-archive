# F44: a smooth relative corner, the actual tensor lattice, and a Frobenius limitation

Author: /root/grothendieck_dictionary, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**Status:** complete elementary author proof. Independent full review is requested before integration. This construction uses a smaller generator than the proposed full Cohen–Macaulay Auslander order and does not rely on a nodal-order theorem for a tacnode.

## 1. Setup and branch labels

Let \(R\) be a commutative domain and let \(0\ne\Delta\in R\). Set
\[
C=R[x]/(x(x-\Delta)),\qquad
L_1=C/(x),\qquad L_2=C/(x-\Delta).
\tag{R1}
\]
Both branch modules are free of rank one over \(R\). In the actual F19/F21 family we keep the previously defined \(\Delta=z_1-z_2\) and choose
\[
x=z_1-z.
\]
Consequently \(L_1\) is exactly the multiplicity-16 branch \(z=z_1\), while \(L_2\) is the multiplicity-4 branch \(z=z_2\). This sign convention prevents an unintended exchange of the two multiplicities.

Define
\[
\Gamma=\operatorname{End}_C(C\oplus L_1).
\tag{R2}
\]
Let \(e_1,e_2\) denote the two summand idempotents. Let \(a:L_1\to C\) send \(1\mapsto x-\Delta\), let \(b:C\to L_1\) be evaluation at zero, and let \(c=ab\). Multiplication is composition, right factor first. Then
\[
a=e_1ae_2,\quad b=e_2be_1,\quad ba=-\Delta e_2,\quad
c=ab,\quad c^2=-\Delta c.
\tag{R3}
\]
The element \(c\) acts on \(C\) by multiplication by \(x-\Delta\).

These formulas give the actual endomorphism algebra, not just an abstract candidate. Indeed \(\operatorname{End}_C(C)=C\), \(\operatorname{End}_C(L_1)=R\), \(\operatorname{Hom}_C(C,L_1)=R b\), and
\[
\operatorname{Hom}_C(L_1,C)=\operatorname{ann}_C(x)=R(x-\Delta)=R a.
\]
The annihilator identity follows by writing an element as \(u+vx\): its product with \(x\) is \((u+v\Delta)x\), so it is annihilated exactly when \(u=-v\Delta\). Therefore \(\Gamma\) is free of rank five with basis \(e_1,e_2,a,b,c\). The relation \(ba=-\Delta e_2\) reduces every longer alternating path to that basis and its multiplication table. In particular
\[
e_1\Gamma e_1=R[c]/(c(c+\Delta))\simeq C,\qquad x=c+\Delta e_1.
\tag{R4}
\]
At \(\Delta=0\) this is precisely the five-dimensional algebra in F40, up to the stated corner-coordinate sign. When \(\Delta\) is invertible, \(C=R\times R\) and
\[
\Gamma\simeq M_2(R)\times R.
\]

## 2. Explicit smoothness over R

All tensor products in this section are over \(R\). Use the same relative bimodules as in F40:
\[
Q_0=(\Gamma e_1\otimes e_1\Gamma)
       \oplus(\Gamma e_2\otimes e_2\Gamma),
\]
\[
Q_1=(\Gamma e_1\otimes e_2\Gamma)_a
       \oplus(\Gamma e_2\otimes e_1\Gamma)_b,\qquad
Q_2=\Gamma e_2\otimes e_2\Gamma.
\]
They are finite projective over \(\Gamma\otimes_R\Gamma^{\mathrm{op}}\), and are free over \(R\) of ranks \(13,12,4\), respectively. Define multiplication \(\mu:Q_0\to\Gamma\) and
\[
d_1(u\otimes v)_a=ua\otimes v-u\otimes av,\qquad
d_1(u\otimes v)_b=ub\otimes v-u\otimes bv,
\]
\[
d_2(u\otimes v)=(ub\otimes v)_a+(u\otimes av)_b.
\tag{R5}
\]
The subscripts label the two summands. These are bimodule maps and \(\mu d_1=0\). The deformed relation causes no error:
\[
d_1d_2(u\otimes v)=uba\otimes v-u\otimes bav
 =-\Delta u\otimes v+u\otimes\Delta v=0.
\]

Here is an exactness proof over \(R\), with no reduction or flatness inference left implicit. The left ideal bases are
\(\Gamma e_1=\langle e_1,b,c\rangle\) and
\(\Gamma e_2=\langle e_2,a\rangle\);
the right ideal bases are
\(e_1\Gamma=\langle e_1,a,c\rangle\) and
\(e_2\Gamma=\langle e_2,b\rangle\).
The image of \(d_1\) contains
\[
\begin{gathered}
a\otimes e_2-e_1\otimes a,\quad
a\otimes b-e_1\otimes c,\quad
b\otimes e_1-e_2\otimes b,\quad
c\otimes e_1-a\otimes b,\\
b\otimes a+\Delta e_2\otimes e_2,\quad
b\otimes c+\Delta e_2\otimes b,\quad
c\otimes a+\Delta a\otimes e_2,\quad
c\otimes c+\Delta a\otimes b.
\end{gathered}
\tag{R6}
\]
They have an eight-by-eight minor equal to a unit in the indicated tensor basis. One choice of pivot coordinates is
\[
a\otimes e_2,\ e_1\otimes c,\ e_2\otimes b,\ c\otimes e_1,\
b\otimes a,\ b\otimes c,\ c\otimes a,\ c\otimes c.
\]
The pivot matrix is triangular in two blocks, with diagonal entries \(1,-1,-1,1,1,1,1,1\); its extra \(\Delta\)-entries do not change its determinant. Thus their span \(V\) is a free direct summand of \(Q_0\), with free quotient of rank five. Multiplication annihilates \(V\) and is surjective onto the free rank-five module \(\Gamma\). The induced surjection \(Q_0/V\to\Gamma\) between free modules of the same rank is an isomorphism. Hence \(V=\ker\mu=\operatorname{im}d_1\).

The \(a\)-component of \(d_2\) uses \(u\mapsto ub\), which sends the basis \(e_2,a\) of \(\Gamma e_2\) to the two independent basis elements \(b,c\) of \(\Gamma e_1\). Projection onto these coordinates is a left inverse. Thus \(d_2\) is a split injection as an \(R\)-module map, with free quotient of rank eight. The induced map \(Q_1/\operatorname{im}d_2\to V\) is a surjection between free rank-eight modules and therefore an isomorphism. This proves the full relative diagonal resolution
\[
0\longrightarrow Q_2\xrightarrow{d_2}Q_1
 \xrightarrow{d_1}Q_0\xrightarrow{\mu}\Gamma\longrightarrow0.
\tag{R7}
\]
\(\Gamma\) is consequently smooth over \(R\), and it is proper over \(R\) because it is finite free. The construction and this resolution in fact work over any commutative base; the domain assumption is used later for Hom and Ext.

If \(R\) is a regular discrete valuation ring, this also gives the concrete absolute bound
\[
\operatorname{gldim}\Gamma\le3.
\tag{R8}
\]
To see it directly, tensor (R7), as a left-\(\Gamma\) resolution of the projective module \(\Gamma\), with any right module \(N\). The resolution is split exact as left modules, so tensoring remains exact. Each resulting term is a finite sum of \(Ne_i\otimes_R e_j\Gamma\). Every \(R\)-module has projective dimension at most one over a DVR, so these terms have projective dimension at most one over \(\Gamma\). A resolution of length two by such terms bounds the projective dimension of \(N\) by three. No assertion that the bound is always sharp is needed.

## 3. The relative actual algebra and a perfect rank-96 lift

Set
\[
\Lambda=R\times R\times M_2(\Gamma),\qquad
f=(1,1,I_2\otimes e_1),\qquad \mathcal P=f\Lambda.
\]
This is a smooth proper \(R\)-algebra of rank 22, and
\[
\operatorname{End}_\Lambda(\mathcal P)
 =f\Lambda f=R\times R\times M_2(C)=A.
\tag{R9}
\]
Thus it is the actual F19 algebra through its specified isomorphism. In the named matrix-generator formulas one must use
\[
z=z_1-x=z_2-c.
\]
This retains the actual generators and not merely an abstract algebra type.

Write \(P_1=e_1\Gamma\), \(P_2=e_2\Gamma\). Left multiplication by \(a\) gives the exact sequence
\[
0\longrightarrow P_2\xrightarrow{a}P_1
 \longrightarrow S\longrightarrow0.
\tag{R10}
\]
It is injective because it sends \(e_2,b\) to the independent vectors \(a,c\). The quotient \(S\) is free of rank one over \(R\), with \(e_1\) acting as one and \(a,b,c,e_2\) as zero. Its projective dimension over \(\Gamma\) is at most one. The corners are
\[
P_2e_1=Rb\simeq L_1,\qquad Se_1=S\simeq L_2.
\tag{R11}
\]
Indeed \(b x=b(c+\Delta e_1)=-\Delta b+\Delta b=0\), while \(x\) acts on \(S\) as \(\Delta\).

For a right \(\Gamma\)-module \(N\), let \(\operatorname{Row}(N)=(N,N)\) be its standard right \(M_2(\Gamma)\)-Morita module. Define
\[
\widetilde M=
\epsilon_+^{20}\oplus\epsilon_-^4
\oplus\operatorname{Row}(P_2)^{16}
\oplus\operatorname{Row}(S)^4.
\tag{R12}
\]
It is free of rank \(24+16\cdot4+4\cdot2=96\) over \(R\), and is perfect over \(\Lambda\), with projective dimension at most one. Its corner is the actual rank-64 lattice:
\[
\widetilde M f=
\epsilon_+^{20}\oplus\epsilon_-^4
\oplus N_1^{16}\oplus N_2^4=M,
\]
\[
\operatorname{Hom}_\Lambda(\mathcal P,\widetilde M)\simeq M
\quad\text{as right }A\text{-modules}.
\tag{R13}
\]
Evaluation at \(f\) proves the Hom identity; precomposition by (R9) is exactly the original right action. This comparison holds over the actual localization in F19/F21, through the collision, not just at its generic or closed fiber.

The specialized lift here has rank 96 and is perfect rather than entirely projective. It is not the rank-104 projective lift chosen in F40. Both recover the same specialized corner module; their different ambient ranks cause no contradiction.

## 4. A coherent extension retains the collision order

The two relative lifts do not preserve all branch Ext groups, but one oriented Ext is exact and useful. Applying \(\operatorname{Hom}_\Gamma(-,P_2)\) to (R10) gives
\[
R b\xrightarrow{-\Delta}R e_2,
\]
because precomposing the map represented by \(b\) with \(a\) gives \(ba=-\Delta e_2\). Since \(\Delta\ne0\) in the domain \(R\),
\[
\operatorname{Hom}_\Gamma(S,P_2)=0,\qquad
\operatorname{Ext}^1_\Gamma(S,P_2)=R/(\Delta).
\tag{R14}
\]
In the opposite direction \(P_2\) is projective and
\(\operatorname{Hom}_\Gamma(P_2,S)=Se_2=0\), so all Hom and positive Ext vanish. Self-Ext of \(P_2\) vanishes by projectivity; the same resolution shows \(\operatorname{End}_\Gamma(S)=R\) and no positive self-Ext. It follows by the matrix Morita equivalence and the separate scalar factors that
\[
\operatorname{Ext}^1_\Lambda(\widetilde M,\widetilde M)
 \simeq (R/(\Delta))^{64}.
\tag{R15}
\]
Only the \(4\cdot16\) oriented cross pairs contribute.

For \(\Delta=u t^m\) in a DVR, this group has length \(64m\). It therefore retains the order \(m\) in an actual coherent derived Hom inside the smooth relative category. In the actual order-two family its length is 128. The original F25 group is \((R/(\Delta))^{128}\), of length 256 when \(m=2\), because both orientations contribute there. We do not identify these two Ext groups or claim a fully faithful embedding of the nonperfect branch modules preserving their derived Hom.

## 5. The relative exceptional pair and the nonadmissible corner

The pair \(\langle S,P_2\rangle\) is a full relative exceptional pair. Its two self-Hom complexes are \(R\), the reverse Hom complex \(R\operatorname{Hom}_\Gamma(P_2,S)\) vanishes, and (R10) recovers \(P_1\). The single-object functors from \(\operatorname{Perf}(R)\) have adjoints defined by finite derived Hom and its \(R\)-dual; those complexes are perfect over \(R\) because the algebra is proper over \(R\). Thus
\[
\operatorname{Perf}(\Gamma)=
\langle\operatorname{Perf}(R),\operatorname{Perf}(R)\rangle.
\tag{R16}
\]
In particular every finite-field fiber has the same two-unit motive calculation as F40; the corresponding \(\Lambda\)-fiber has four unit motives and the previously cited normalized TP spectrum. This is a fiberwise application of the same known semiorthogonal-additivity and enriched-TP statements, not a claim that the fraction field of an arbitrary trait is finite.

The corner functor \(\operatorname{Perf}(C)\to\operatorname{Perf}(\Gamma)\), given by tensoring with \(e_1\Gamma\), is fully faithful by the same derived adjunction as F40. For a nonunit \(\Delta\), it is not right-admissible. The corner of \(P_2\) is \(L_1\), and the exact periodic resolution alternating \(x\) and \(x-\Delta\) gives
\[
\operatorname{Tor}_{2j+1}^{C}(L_1,L_1)=R/(\Delta)
\quad(j\ge0).
\]
Thus \(L_1\) is not perfect. Any right adjoint on perfect categories would have to recover this object when applied to \(P_2\), by testing against \(C[n]\) and its endomorphisms, which is impossible. After inverting \(\Delta\), the idempotent is full because \(ba=-\Delta e_2\); the corner becomes a Morita equivalence. These are different assertions before and after collision.

## 6. A genuine noncommutative Frobenius lift

Now assume \(R\) has characteristic \(p>3\). Let \(F_R(r)=r^p\). Define a ring endomorphism \(\varphi:\Gamma\to\Gamma\), semilinear over \(F_R\), by
\[
\varphi(e_i)=e_i,\qquad
\varphi(a)=a,\qquad
\varphi(b)=\Delta^{p-1}b.
\tag{R17}
\]
The defining relation is preserved:
\[
\varphi(b)\varphi(a)
=\Delta^{p-1}ba=-\Delta^p e_2
=\varphi(-\Delta e_2).
\]
Thus this is an actual noncommutative ring map. It is not the map sending every matrix or algebra element to its \(p\)-th power; for example it fixes the nonzero square-zero arrow \(a\).

On the commutative corner,
\[
\varphi(c)=\Delta^{p-1}c=c^p,\qquad
\varphi(x)=\Delta^{p-1}(c+\Delta e_1)=x^p.
\tag{R18}
\]
Here \(c^2=-\Delta c\), \(p\) is odd, and \(x^2=\Delta x\). Hence the induced corner map is exactly the ordinary scheme Frobenius, including on the actual coordinate \(z=z_2-c\). Extend \(\varphi\) to the scalar and matrix factors of \(\Lambda\) in the evident entrywise fashion; it fixes \(f\).

For right modules, use derived extension of scalars
\[
\mathbf L\varphi^*N=N\otimes_{\Gamma,\varphi}^{\mathbf L}\Gamma.
\]
Each \(P_i=e_i\Gamma\) has an isomorphism
\(\mathbf L\varphi^*P_i\simeq P_i\), since \(\varphi(e_i)=e_i\). In the resolution (R10), the map \(a\) is unchanged. Therefore
\[
\mathbf L\varphi^*S\simeq S
\]
as well, with no extra derived cohomology. The actual objects \(\mathcal P,\widetilde M\) consequently have unit pullback structures over their larger algebras. This is a concrete categorical statement, not yet a unit structure after forgetting to \(R\).

## 7. Why that unit structure is not a unit base linearization

Under the preceding isomorphism for \(P_2\), the semilinear map on its \(R\)-basis \(e_2,b\) is
\[
e_2\longmapsto e_2,\qquad
b\longmapsto\Delta^{p-1}b.
\]
Its \(R\)-linearization has matrix
\[
\operatorname{diag}(1,\Delta^{p-1}).
\tag{R19}
\]
It is not invertible at a nonunit \(\Delta\). The \(R\)-linearization on \(S\) is the identity in its rank-one basis. Therefore the chosen structure on the free rank-96 module in (R12) has determinant
\[
\Delta^{32(p-1)}
\tag{R20}
\]
up to a unit: the 16 row copies contain 32 copies of the basis vector \(b\). The recovered rank-64 corner module has the same determinant defect; its multiplicity-16 row branch contributes 32 such vectors. Any other isomorphism for this same pullback differs by an automorphism of the target, hence multiplies the underlying determinant by a unit. It cannot remove the defect.

There is also a complete tradeoff for all such lifts fixing the two vertex idempotents. Any ring endomorphism semilinear over \(F_R\), fixing \(e_1,e_2\), must send
\[
a\longmapsto u a,\qquad b\longmapsto v b
\]
for some \(u,v\in R\), because the two arrow spaces each have rank one. The relation and the nonzerodivisor \(\Delta\) force
\[
uv=\Delta^{p-1}.
\tag{R21}
\]
Conversely this relation defines such a lift and gives the ordinary corner Frobenius.

For this lift the derived pullback of (R10) has differential \(u a\). Since \(u\ne0\), it is injective and its cokernel, as an \(R\)-module, is
\[
R\oplus(R/uR)^2.
\]
It can be isomorphic to the free rank-one module \(S\) only when \(u\) is a unit. Conversely a unit \(u\) makes the resolution isomorphic to (R10), so that condition is sufficient. Meanwhile \(P_2\) always has a unit algebra-pullback isomorphism, but its underlying \(R\)-linearization is \(\operatorname{diag}(1,v)\), up to a unit change of basis. It is a unit over \(R\) exactly when \(v\) is a unit.

At a nonunit \(\Delta\), equation (R21) excludes both requirements simultaneously. For the full module (R12), a nonunit \(u\) produces actual torsion in the pullback of its \(S\)-summands, so even its unit algebra-pullback property fails. A unit \(u\) forces nonunit \(v\), and the base determinant remains nonunit. This proves a scoped obstruction for this fixed-vertex family of lifts; it is not a nonexistence statement about every resolution or every possible realization.

The chosen ring Frobenius lift, its categorical pullback structures, ordinary scheme Frobenius on the center, and the cyclotomic Frobenius on TP are distinct constructions. No equality with cyclotomic Frobenius is asserted. A Weil or unit-vector-bundle realization would require additional comparison data, and (R19)–(R21) show why the algebra-level unit condition alone does not supply it.

## 8. Exact advance and remaining scope

This construction resolves the relative smoothness question for the actual rank-three family without appealing to a tacnode classification. The actual algebra is retained as a corner, its actual tensor lattice is retained as a Hom module between perfect objects, and a coherent extension inside the smooth category retains the collision order. The relative diagonal proof is uniform in that order. A full Cohen–Macaulay generator is not needed for these conclusions.

It does not preserve both orientations of the original coherent Ext, nor does the corner become admissible through collision. The explicit Frobenius lift supplies a unit structure over the larger algebra but fails the independent underlying-base unit condition. Finally no positive nonstandard basis, path-sign comparison, or all-extension quantum-parameter trace rule follows from the fiberwise four-unit TP spectrum.

The Grothendieck dictionary is the affine coherent-module and perfect-diagonal framework, extended by the explicitly stated modern dg and TP constructions already sourced in F40. The unpublished manuscript anchors remain framework anchors only. No relative Auslander order, Frobenius lift, or nonstandard comparison is attributed to those leaves.

All elementary claims (R1)–(R21), including every differential, exactness argument, action comparison, Ext computation, and Frobenius limitation, are proved above. The only motivic source application is the already inspected finite-field exceptional-decomposition implication in F40, with the same Tabuada locators. Independent full review is still required before main-paper insertion.
