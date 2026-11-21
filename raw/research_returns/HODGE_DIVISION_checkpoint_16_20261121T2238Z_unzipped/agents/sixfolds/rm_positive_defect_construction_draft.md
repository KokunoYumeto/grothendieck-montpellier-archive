# Positive defect determinant: an actual balanced family with nonsplit hulls

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** complete new construction and exact certificate, submitted for
review. This shows that the necessary determinant in draft E825 is actually
realizable with the entire balanced character and with genuine nonsplit
hull extensions. It is not a semiregular seed. The explicit one-step family
still has free direct summands; its ordinary semiregularity is excluded.
No indecomposability or coherent finite action is claimed.

## 1. Actual divisors and a smooth surface

Take X=E_i^4 with its product principal polarization theta. Set

\[
 U=\operatorname{diag}\left(
 \begin{pmatrix}1&1\\1&-1\end{pmatrix},
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}\right),\qquad
 S=\operatorname{diag}(1,1,-1,-1).
 \tag{PD.1}
\]

These symmetric integral matrices commute, U squared is2, and each gives
an actual line class theta_U, theta_S or theta_US. Explicitly, every
symmetric integral matrix A gives a line bundle by tensoring coordinate
pullbacks of O_E(A_jj[0]) and powers of
\((p_j+p_k)^*O_E([0])\otimes p_j^*O_E(-[0])\otimes p_k^*O_E(-[0])\)
for its off-diagonal entries. Thus no merely real class is used.

Let D=4theta and L=O_X(D). On each elliptic factor a degree-four line bundle
is very ample: removing a subscheme of length two leaves degree two, whose
H1 vanishes by the curve Riemann--Roch/duality calculation. Thus sections
separate every length-two subscheme. The exterior product followed by the
Segre embedding makes L very ample on X. Choose ordered sections f,g with
smooth complete intersection S0. Such choices form a nonempty open by the
previously checked Bertini theorem. Its negative-ample Koszul resolution
shows H0(O_S0)=C, so the smooth surface is connected and integral. A further
nonempty-open condition on f needed in section4 will be imposed below.

Let F be the actual unit sheaf for this surface, with the complete locally
free resolution

\[
 0\longrightarrow O_X(-4D)\longrightarrow O_X(-3D)^2
  \longrightarrow O_X(-D)^2\longrightarrow F\longrightarrow0.
 \tag{PD.2}
\]

Its torsion is O_S0(-2D), its hull is O_X, and its hull defect is O_S0.
Put G=F tensor O_X(14theta). Thus the canonical defect line of G, including
its extension to the first neighborhood, is O_X(14theta) restricted there.
Since14theta=7D/2, this is exactly the positive determinant required in E825.

## 2. An exact positive integral character identity

Use the four common eigenline volume forms omega1,...,omega4, normalized
so omega_j squared is zero and their product integrates to1. The first two
belong to the positive RM plane and the last two to the negative plane.
A divisor specified by four integers (a,b,c,d) means
\(a\theta+b\theta_U+c\theta_S+d\theta_{US}\). Its four eigenvalues are

\[
 a+b\sqrt2+c+d\sqrt2,\quad a+b\sqrt2-c-d\sqrt2,\quad
 a-b\sqrt2+c-d\sqrt2,\quad a-b\sqrt2-c+d\sqrt2.
 \tag{PD.3}
\]

For any such divisor beta its full exponential has coefficient
\(\prod_{j\in J}\lambda_j\) on the monomial omega_J. This follows by
multiplying the four factors1+lambda_j omega_j. The unit character is

\[
 \operatorname{ch}(G)
  =2e^{10\theta}-2e^{2\theta}+e^{-2\theta}.
 \tag{PD.4}
\]

Its subset coefficients in increasing binary-mask order are

\[
 (1,14,14,196,14,196,196,1976,
     14,196,196,1976,196,1976,1976,19984).
 \tag{PD.5}
\]

Put r=32649230592 and R=32r=1044775378944. The following sixteen actual
line bundles, with the indicated strictly positive multiplicities, form a
vector bundle V of rank R-r=1012126148352.

| (a,b,c,d) | multiplicity |
|---|---:|
| (-16,0,0,0) |71520925267|
| (-8,-6,-8,6) |59890215297|
| (-8,-6,8,-6) |59890215297|
| (0,-11,0,0) |69240052352|
| (-8,6,-8,-6) |59890215297|
| (0,0,-16,0) |73261417339|
| (0,0,0,-11) |69779709056|
| (8,-6,-8,-6) |56874362655|
| (-8,6,8,6) |59890215297|
| (0,0,0,11) |69779709056|
| (0,0,16,0) |73261417339|
| (8,-6,8,6) |56874362655|
| (0,11,0,0) |69240052352|
| (8,6,-8,6) |56874362655|
| (8,6,8,-6) |56874362655|
| (16,0,0,0) |48984553783|

The exact sixteen-coordinate identity is

\[
 r\operatorname{ch}(G)+\operatorname{ch}(V)
       =R\left(1-\frac{\theta_+^2}{4}\right)
          \left(1-\frac{\theta_-^2}{4}\right)
       =R v_{1/2}.
 \tag{PD.6}
\]

There is no omitted degree component: after dividing the right side by R, its subset coefficients are
1 at mask0, minus1/2 at masks3 and12, plus1/4 at mask15, and zero elsewhere.
Equations(PD.3)--(PD.5), the table and ordinary multiplication in the
sixteen-dimensional square-zero algebra prove(PD.6) directly. The attached
exact quadratic-field script reconstructs all those coordinates and checks
every positive integer and the total rank. It does not use numerical
approximations to sqrt2 or infer any cycle from a numerical fit.

## 3. A nonzero global extension with the same local form

Choose the free line type beta=(-8,-6,-8,6), and write B_beta for its line
bundle. The four eigenvalues of
\(A=14\theta-\beta\) are

\[
 30,\quad14+12\sqrt2,\quad30,\quad14-12\sqrt2.
 \tag{PD.7}
\]

The last is negative. For j=1,3,4 the classes A-jD still have exactly one
negative and three positive eigenvalues. The published abelian index
vanishing theorem and Riemann--Roch therefore place their whole cohomology
in degree1, with dimensions respectively

\[
 127088,\qquad92016,\qquad55664.
 \tag{PD.8}
\]

For example these are the negatives of the products of their four
nonzero eigenvalues; the product polarization has theta4/24=1. Applying
cohomology to(PD.2) tensored by O_X(A) gives a single nonzero row. Its final
cokernel is H1(F tensor O_X(A)), so

\[
 \dim\operatorname{Ext}^1_X(B_\beta,G)
 =h^1(F\otimes O_X(A))
 \ge2\cdot127088-2\cdot92016=70144.
 \tag{PD.9}
\]

This is a dimension inequality, not an assertion of a generic maximal rank.
Every class produces an actual coherent extension

\[
 0\longrightarrow G\longrightarrow E_e\longrightarrow B_\beta
       \longrightarrow0.
 \tag{PD.10}
\]

It splits locally because B_beta is locally free. Thus E_e has local form
F plus one free summand, retains the canonical torsion and quotient Q of G,
and has the same extension of Q to S2. In local triangular transition
matrices, the map ell of E825 ignores the off-diagonal free-to-F block and
keeps the transition of O_X(14theta). This is also a direct verification
of the determinant condition without assuming it persists abstractly.

Any nonzero extension(PD.10) is not isomorphic to G plus B_beta. Indeed
\(\operatorname{Hom}(G,B_\beta)=H^0(O_X(\beta-14\theta))=0\):
F dual is O_X and the displayed line has index3. If its middle term were
that direct sum, any surjection to B_beta would vanish on G and be an
invertible scalar on B_beta, providing a splitting of the exact sequence.

## 4. The hull can also be a genuinely nonsplit extension

This is stronger than the preceding nonzero extension claim and needs an
additional argument. All six lines O_X(A-jD), j=0,...,5, have index1.
In particular h1(O_X(A))=82800. Choose five sections of the globally
generated L with no common zero. Such a choice exists by cutting the
fourfold successively and choosing the last section nonzero on the finite
remaining set. Their Koszul complex tensored by O_X(A) is exact. Every
term has cohomology only in degree1, so its cohomology-row complex is exact.
In particular the sum of the five multiplication maps

\[
 H^1(O_X(A-D))^{\oplus5}\longrightarrow H^1(O_X(A))
 \tag{PD.11}
\]

is surjective. At least one of these section maps has rank at least
82800/5=16560. Having rank at least16560 is a nonempty Zariski open
condition on a section of L, because the map is linear in that section.
It therefore intersects the nonempty smooth-Bertini open. Choose f there,
and then choose g to make the smooth connected S0 used above. This proves
the claimed rank lower bound for the actual chosen pair without presuming
maximal rank of a particular multiplication map.

Next, H2(S0,O_S0(A-2D)) is zero. By adjunction and surface Serre duality
it is dual to H0(S0,O_S0(4D-A)). The three lines with classes
4D-A,3D-A,2D-A all have index3. Their surface Koszul complex therefore has
its only cohomology row at degree3 and length two, so it contributes no
H0 on S0. This proves the vanishing for every regular pair f,g.

The exact torsion sequence

\[
 0\to O_{S0}(A-2D)\to F\otimes O_X(A)\to I_{S0}\otimes O_X(A)\to0
 \tag{PD.12}
\]

now makes H1(F tensor O_X(A)) surject onto H1(I_S0 tensor O_X(A)). The
image of the latter in H1(O_X(A)) contains the multiplication image by f
from H1(O_X(A-D)), because f factors through the ideal. Thus the map

\[
 \operatorname{Ext}^1(B_\beta,G)\longrightarrow
 \operatorname{Ext}^1(B_\beta,O_X(14\theta))
 \tag{PD.13}
\]

induced by the hull map has rank at least16560. Choose e with nonzero
image. Pushing out(PD.10) by G to its hull gives an actual nonsplit
extension of the two line bundles. Locally it is the double dual of E_e,
since E_e has local form F plus R and its hull is R squared. Hence the
hull of E_e is itself this nonsplit bundle. It is not isomorphic to the
original two-line direct sum, by the same vanishing of Hom from the first
line to the second used above.

## 5. The entire balanced family and its explicit limitation

Replacing one copy of G and one copy of B_beta in G^r plus V by(PD.10)
with such a class e gives an actual coherent sheaf M with

\[
 \operatorname{ch}(M)=R v_{1/2},\qquad
 M\text{ locally }F^r\oplus O_X^{R-r},\qquad
 \det\widetilde Q=O_X(14r\theta)|_{S_2}.
 \tag{PD.14}
\]

Its hull contains the actual nonsplit extension above. Every coherent
sheaf is ordinary gluable, so negative self-Ext vanishes. The complete
character and the E825 determinant are unchanged by any extension class
in Ext1(V,G^r), not just the single-copy example. The subobject G^r and
the quotient V are actual coherent sheaves; no signed K0 construction
has been substituted for them.

However this one-step family always retains some direct summands. In
particular, for beta=16theta or beta=-16theta,
\(\operatorname{Ext}^1(O_X(\beta),G)=0\). The three resolution terms
have respectively only degree4 or only degree0 cohomology; the length-two
resolution gives no H1. The Ext1 decomposition over the actual direct
sum V then forces those positive-multiplicity quotient blocks to split
off from every such extension. Thus arbitrary gluing only from V into
G^r does not remove them. With the trivial action these actual pure-line
summands are already excluded by the reviewed direct-summand cap criterion
E802. No coherent nontrivial action that could change that scope is
constructed or inferred here.

To seek a seed beyond this family one must at least replace the split free
quotient by further actual gluing among its line classes, change the
compensation architecture, or use a different object. The present result
establishes actual realizability of the positive determinant and a nonsplit
hull; it does not certify a new semiregular object or resolve the remaining
seed gate. The local determinant condition by itself is therefore not a
universal nonexistence theorem.

## 6. Sources and actual checks

The index/vanishing input is Mumford, Abelian Varieties(1970), section16,
printedpp150--153 and the complex Hermitian-index statement/proofpp162--163,
previously fully located and read in this run. The Bertini input is the
already read complete displayed proof at Stacks tag0FD4 and the smooth-
irreducible hyperplane argument at0G4G; connectedness is proved separately
here by the Koszul complex. The full unit resolution is the previously
reviewed actual construction, not an unrefereed theorem. The remaining
cohomology-row and extension arguments are written above.

The exact program rm_positive_defect_compensation.py was actually run,
with output rm_positive_defect_compensation_output.json. It checks all16
full characters over Q(sqrt2), positive integral multiplicities, total
rank, the exact defect determinant, all relevant cohomology indices and
integer dimensions70144/82800/16560. Failed interpolation at scale8 is
retained; scale16 succeeds. The script does not compute generic cup-product
matrices or claim that a finite action or semiregularity was verified.
