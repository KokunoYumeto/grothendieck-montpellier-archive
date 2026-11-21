# SF-E829. A wedge-pairing gate for arbitrary surface directions

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on the frozen draft
`4cab77bfcc30b75151e946b3a1da06e29e2461ce59f8787c326c9aa5ab666b28`.
All reviewers: GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION, 21 November2026. The peer also supplied an independently
written supplementary exact exterior certificate; the infinite theorem
is the complete proof below, not an extrapolation from finite checks.
This extends E827 beyond its rational four-divisor algebra. It is a
necessary support-incidence gate for the same actual equivariant extension
architecture. It is not a classification of all coherent sheaves, an
existence theorem for a semiregular seed, or an assertion that the remaining
elliptic/surface configurations succeed.

## 1. Exact statement

Let X be a polarized abelian fourfold and retain the actual coherent
extension and actual equivariant blocks from E827:

\[
 0\longrightarrow A\longrightarrow E\longrightarrow B\longrightarrow0,
 \qquad A=A_0\oplus\bigoplus_{a=1}^u L_a^{n_a},
 \qquad B=\bigoplus_{b=1}^v M_b^{m_b}.
 \tag{E829.1}
\]

Every cross difference line N_ab=L_a tensor M_b inverse is assumed to
have nonzero first Chern class. This is automatic for the opposite slopes
in E826. Write rank(N) for the complex rank of its Hermitian form, relative
to the fixed positive polarization. For every pair, require either
rank(N_ab) at least2 or \(H^*(X,N_{ab})=H^*(X,N_{ab}^{-1})=0\). Thus a rank-one
pair is allowed only if its flat kernel twist makes it cohomologically
irrelevant. The rank-one cases with nonzero cohomology are deliberately
not covered by the theorem.

Put V=H1(X,O_X), dim V=4. For each rank-two difference whose nondegenerate
surface part has index one and whose flat kernel part is trivial after the
product isogeny below, let V_N be the two-dimensional subspace of V coming
from that surface factor. Let z_N=Lambda2 V_N, a line in Lambda2 V. Define

\[
 Z=\operatorname{span}_\mathbf C\{z_N\}\subset\Lambda^2V,
 \qquad z=\dim Z.
 \tag{E829.2}
\]

The construction below gives these subspaces canonically after choosing
the fixed polarization. Including an extra acyclic rank-two pair in Z is
permitted and only weakens the bound. Choose a nonzero volume in Lambda4 V
and let q be the nondegenerate symmetric wedge pairing on Lambda2 V.
Let rho be the dimension of the radical of q restricted to Z. Put

\[
 w=6-z-\rho.
 \tag{E829.3}
\]

Let J be any subset of negative-block indices for which Ext3(M_b,A0)=0.
For every specified coherent effective finite action preserving the actual
sequence and blocks,

\[
 \operatorname{ext}^2_\Gamma(E,E)\ge w(u+|J|).
 \tag{E829.4}
\]

In particular, if the complete normalized character is a nonzero multiple
of the balanced v_q of E801, with any rational algebraic B field, weak
semiregularity requires w(u+|J|) at most18. The letter q in the wedge pairing
and the parameter in v_q denote different objects; in the proof below the
pairing is written q_wedge when needed to avoid ambiguity.

## 2. The product isogeny and the cohomology calculation

We give the needed degenerate-line reduction directly, including the
isogeny and its scope. On the real tangent space of X, the alternating form
E_theta of the polarization identifies the alternating form E_N of a line
bundle with a rational linear operator T:

\[
 E_N(x,y)=E_\theta(Tx,y).
 \tag{E829.5}
\]

Both forms are integral on the lattice, and E_theta is nondegenerate, so T
is rational. Their type(1,1) condition implies that T commutes with the
complex structure. Alternation gives
E_theta(Tx,y)=E_theta(x,Ty), so T is self-adjoint for the positive Hermitian
form associated with theta. It is therefore diagonalizable with real
eigenvalues. Its kernel K_R and image C_R are rational complex subspaces,
and are E_theta-orthogonal complements. Intersecting them with the lattice
produces complex subtori K and C. The restriction of theta to each is
positive, so these are abelian subvarieties. Their sum map

\[
 f:C\times K\longrightarrow X
 \tag{E829.6}
\]

is an isogeny: the differential is an isomorphism, and the sum of the two
intersection lattices has finite index in the original lattice. This is a
lattice proof of the needed complement; no generic splitting or rational
RM eigenspace is being treated as an abelian subvariety.

The complex dimension of C is rank(N), and E_N is nondegenerate on C and
zero on K and on the mixed terms. Thus

\[
 f^*N=N_C\boxtimes P_K,
 \tag{E829.7}
\]

where N_C is a nondegenerate line bundle and P_K is a degree-zero line
bundle. To see the line-level assertion, subtract the pullback of the
restriction to C: the remaining line has zero first Chern class, and a
flat character of the product lattice is a product of characters of its
two factors. Absorb its C component into N_C. This proves(E829.7), not
merely its numerical counterpart.

A nontrivial degree-zero line on an abelian variety has no cohomology.
One may use the previously read published Pic0 vanishing, or the direct
unitary-flat proof: the corresponding flat character is nontrivial, and
the flat Laplacian on its torus has no zero-frequency harmonic mode. Hence
if P_K is nontrivial, both lines in(E829.7) and their inverses are acyclic.
If P_K is trivial, the abelian index theorem puts the cohomology of N_C
in exactly one degree j, and the inverse in degree r-j, where r=dim C.
Kunneth then describes all cohomology and all its products.

The pullback of H1(O_X) is an isomorphism onto
H1(O_C) direct sum H1(O_K), so it identifies V with these two summands.
Define V_N=H1(O_C) under this identification. It is independent of lattice
indices in the above construction because C_R=im T is fixed. The pullback
of \(H^*(X,N)\) is injective by finite-etale trace: trace after pullback is
multiplication by deg f. Products commute with pullback. Thus every
vanishing and every product-containment proved on C times K descends to X.
This use of an isogeny concerns cohomology and products only; no action,
object, or semiregularity is being pulled back in the conclusion.

## 3. Exhaustive ranks at least two

Let V_C=H1(O_C), V_K=H1(O_K), with dimensions r and k=4-r.
When P_K is trivial, the only possible degree-one terms are

\[
 H^1(f^*N)=
 \begin{cases}
 H^0(N_C)\otimes V_K,&j=0,\\
 H^1(N_C)\otimes\mathbf C,&j=1,\\
 0,&j\ge2.
 \end{cases}
 \tag{E829.8}
\]

Multiplication by any class containing a V_C factor raises the C
cohomological degree away from its sole index and is therefore zero.
Only the component in Lambda2 V_K can act nontrivially from degree1 to
3. This observation also applies to N inverse, at its index r-j.

If r=4, the line is nondegenerate on X. Its degree-one group and that of
its inverse cannot both be nonzero, and its own degree-three group is zero
whenever its degree-one group is nonzero. Thus all diagonal degree-one
products vanish and every element of Lambda2 V kills both degree-one
groups into degree3.

If r=3, then k=1 and Lambda2 V_K=0. Every element again kills degree1 into
3. The indices of N_C and its inverse sum to3, so both cannot have index
at most1. Thus both degree-one groups cannot occur simultaneously, and
all their diagonal products vanish. This includes the j=0 term with its
one-dimensional kernel factor; no nondegeneracy on the whole X is assumed.

If r=2 and j=0 or2, only one of the two lines can have degree-one
cohomology. The possible group has j=0 and is H0(N_C) tensor V_K.
Multiplication by Lambda2 V_K lands in Lambda3 V_K=0 because k=2.
The C-containing components already vanish. Thus all diagonal products
vanish and every element of Lambda2 V kills degree1 into3 in these cases.

The sole remaining case with r at least2 is r=2,j=1. Here both lines have

\[
 H^1(f^*N)=H^1(N_C)\otimes\mathbf C,
 \qquad
 H^3(f^*N)=H^1(N_C)\otimes\Lambda^2V_K.
 \tag{E829.9}
\]

Their diagonal degree-one Yoneda products lie in
Lambda2 V_C, the support line z_N. Multiplication of a degree-one class by
w0 in Lambda2 V depends only on its projection to Lambda2 V_K. It is zero
whenever that projection vanishes. Since both V_C and V_K have dimension2,
this condition is exactly

\[
 w_0\wedge z_N=0,
 \tag{E829.10}
\]

meaning the wedge with any generator of that line is zero. Equivalently,
w0 is orthogonal to z_N for q_wedge. This completes the actual cup-product
analysis of every pair allowed in the theorem.

## 4. The surviving diagonal space and invariant exact sequences

For all cross pairs together, the preceding calculations show that every
incoming diagonal degree-one product lies in Z, and every element of
Z perpendicular kills both relevant degree-one groups into degree3.
The pairing on Lambda2 V is nondegenerate. Thus

\[
 \dim Z^\perp=6-z,
 \qquad Z\cap Z^\perp=\operatorname{rad}(q_{\mathrm{wedge}}|_Z).
 \tag{E829.11}
\]

Choose any vector-space complement W to this radical inside Z perpendicular.
Then W intersects Z trivially, and dim W=6-z-rho=w. All such subspaces are
fixed by the allowed translation/tensor functors on H2(O_X), since those
functors act trivially on this cohomology. No invariant choice beyond this
trivial action is needed.

Now apply exactly the actual diagonal-survival proof E827.1--5: the
A-diagonal W identity classes inject through Hom(A,triangle); their next
boundary vanishes because W kills Ext1 into Ext3. The selected B-diagonal
classes lift because Ext3(M_b,A0)=0. Normalized diagonal matrix trace modulo
Z kills the preceding boundary, with its A0 term zero by Serre duality.
Finite invariants are exact and all selected classes are invariant.
Consequently their contributions add to w(u+|J|). This is(E829.4).
There is no degeneration claim for a filtered Ext spectral sequence and no
assumption that different Chern-character terms are summands of E.

For the full balanced character, its cap rank is18 and the rational B
shear is invertible. The already reviewed full supplied S21 adjunction
therefore forces invariant Ext2 dimension18 under weak semiregularity.
Equation(E829.4) gives the claimed necessary inequality.

## 5. Concrete geometric consequences and the elliptic limitation

With no exceptional rank-two index-one pair, Z=0 and w=6. Thus E827's
six-per-block obstruction extends to every rank-three degeneration and to
every rank-two index-zero or index-two degeneration, without assuming the
four-divisor algebra. For u at least4 the weak balanced seed is excluded
under these hypotheses, even if the unit block has nonzero opposite Ext3.

With a single exceptional support line, z=1 and rho=1 because a
decomposable two-vector squares to zero. Hence w=4. With exactly two
independent support lines generated by z1,z2, there are two alternatives:

- if z1 wedge z2 is nonzero, the restriction pairing has matrix
  [[0,c],[c,0]], c nonzero, so z=2,rho=0 and w=4;
- if z1 wedge z2 is zero, the restriction is zero, so z=2,rho=2 and w=2.

For two-dimensional subspaces of a four-dimensional V, the second case
means the two support planes intersect in a nonzero vector; the first
means they are complementary. These are the actual rational surface
support directions defined from their numerical line forms, not the
irrational RM embedding planes. In particular the two complementary
surface directions of E827's four-divisor algebra give w=4, recovering
that earlier bound. Arbitrary additional directions are controlled by the
explicit formula6-dimZ-dimrad, not by an unstated general-position claim.

The rank-one limitation is genuine for this method. On a product C times K
with C elliptic and K three-dimensional, take a nontrivial positive line
N_C and trivial P_K. Then N_C has index0 and its inverse index1. The two
degree-one spaces are H0(N_C) tensor V_K and H1(N_C inverse) tensor C.
By elliptic Serre duality their diagonal products span

\[
 Z_{\mathrm{ell}}=V_C\wedge V_K.
 \tag{E829.12}
\]

For multiplication to kill the inverse degree-one group into degree3,
a two-vector must have zero Lambda2 V_K component. Since V_C is
one-dimensional, the entire allowable annihilator is exactly the same
space V_C wedge V_K. It has zero possible complement disjoint from
Z_ell. Thus the E827 lemma cannot extract any nonzero common W from
this single pair. This is a demonstrated limitation of the diagonal
method, not a proof of semiregularity or existence of a balanced seed.
If a rank-one pair is acyclic because of a nontrivial flat kernel factor,
all its products vanish and it causes no restriction, as permitted in
the statement.

## 6. Sources and check boundary

The product isogeny and its numerical/line-level decomposition are proved
above from the rational self-adjoint operator of the two Riemann forms.
The only substantive external cohomology input is the original Mumford
Abelian Varieties(1970), section16 printedpp150--153 and162--163, already
fully read in the invoked scope for E826, together with the previously read
Pic0 vanishing or the direct flat proof supplied above. Kunneth, finite
trace and the actual cup products are stated with their full uses. The
actual triangle/invariant argument is the wholly proved E827 lemma; the
balanced rank consequence retains the exact supplied S21 and published BF
status already recorded there. No new numerical experiment, period rank,
finite action or semiregular object is asserted.
