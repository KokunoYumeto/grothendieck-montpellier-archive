# SF-E826. Coupled two-slope extensions: actual indecomposable objects and a middle-Ext obstruction

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** new full proof and actual exact certificates, submitted for
independent review. This excludes an entire precisely specified extension
architecture, including an actual indecomposable balanced example. It does
not exclude all positive-determinant forms from E825. A connected Ext graph
is not used as a substitute for constructing an extension or checking its
endomorphisms. No formality or vanishing of uncomputed Yoneda products is
assumed.

## 1. An actual triangle lemma, with its invariant form

Let X be a smooth projective fourfold and let

\[
 0\longrightarrow A\xrightarrow{i}E\xrightarrow{p}B\longrightarrow0,
 \qquad e:B\longrightarrow A[1],
 \tag{E826.1}
\]

be an actual coherent extension. Suppose
\(\operatorname{Ext}^1(A,B)=\operatorname{Ext}^3(B,A)=0\). Then

\[
 \operatorname{ext}^2(E,E)\ge
 \operatorname{ext}^2(A,A)+\operatorname{ext}^2(B,B).
 \tag{E826.2}
\]

If a finite group has a coherent action preserving this exact sequence,
the same inequality holds for invariant Ext groups. On an abelian
fourfold, the ordinary Ext1 vanishing follows from the displayed Ext3
vanishing by Serre duality. The following proof uses actual long exact
sequences, not a degeneration claim for a spectral sequence.

Apply Hom(A,-) to the triangle. The Ext1(A,B) vanishing gives both a
surjection Ext1(A,A) to Ext1(A,E) and an injection
\(i_*:\operatorname{Ext}^2(A,A)\to\operatorname{Ext}^2(A,E)\).
Apply Hom(B,-). The Ext3(B,A) vanishing gives a surjection
\(\operatorname{Ext}^2(B,E)\to\operatorname{Ext}^2(B,B)\).
Finally apply Hom(-,E), obtaining the exact segment

\[
 \operatorname{Ext}^1(A,E)\xrightarrow{\partial_1}
 \operatorname{Ext}^2(B,E)\longrightarrow
 \operatorname{Ext}^2(E,E)\longrightarrow
 \operatorname{Ext}^2(A,E)\xrightarrow{\partial_2}
 \operatorname{Ext}^3(B,E).
 \tag{E826.3}
\]

Every class in Ext1(A,E) is i[1]a for some a in Ext1(A,A).
Its boundary is i[2]a[1]e, so it is in the image of Ext2(B,A). It
therefore maps to zero in Ext2(B,B). Hence the quotient
\(Q=\operatorname{Ext}^2(B,E)/\operatorname{im}\partial_1\), which
injects into Ext2(E,E), still surjects onto Ext2(B,B).
For a in Ext2(A,A), the other boundary of i[2]a is i[3]a[1]e.
Its middle composite a[1]e is in Ext3(B,A), hence zero. Thus the
quotient of Ext2(E,E) by Q contains the injected copy of Ext2(A,A).
This proves(E826.2). All maps are functorial for the given coherent action;
finite invariants are exact in characteristic zero. The identical argument
therefore proves the invariant inequality. No equivariant splitting of
(E826.1) is used.

## 2. The full extension architecture excluded by the lemma

Work on the balanced RM abelian fourfold, with ample theta, D=4theta,
a smooth ordered complete-intersection surface S, and the actual unit
sheaf F of E823--E825. Put \(\mathscr U=F\otimes O_X(14\theta)\).
Consider any extension(E826.1) with

\[
 A=\mathscr U^{\oplus r}\oplus\bigoplus_{a=1}^{u}L_{\alpha_a}^{\oplus n_a},
 \qquad
 B=\bigoplus_{b=1}^{v}L_{\beta_b}^{\oplus m_b},
 \tag{E826.4}
\]

where r and all multiplicities are positive. Assume:

- all alpha_a have theta-slope14theta4, are pairwise distinct as Chern
  classes, and differ from14theta;
- all beta_b have theta-slope minus14theta4 and are pairwise distinct as
  Chern classes;
- Ext3(B,A)=0;
- the entire normalized character is \(e^{B_{\mathrm{fld}}}\operatorname{ch}(E)=R v_q\)
  for q nonzero and \(B_{\mathrm{fld}}\) rational algebraic, and u+v is at least4.

Then E has **no weakly semiregular lift for any specified effective coherent
finite translation/tensor action** of the kind in supplied S21. This is a
statement about every extension in this architecture, not just a selected
matrix or an indecomposable example.

Here is the equivariance argument in full. T=tors(E) is canonical. Since B
is locally free, the sequence splits locally, so T=tors(A) and

\[
 A/T=(I_S\otimes O_X(14\theta))^{\oplus r}
       \oplus\bigoplus_a L_{\alpha_a}^{\oplus n_a}.
 \tag{E826.5}
\]

Every factor is torsionfree of rank one and slope14theta4; it is slope
semistable. Their direct sum is semistable. B is semistable of slope
minus14theta4. Thus A/T is the positive part of the two-step HN filtration
of E/T. One can characterize it without invoking any splitting theorem:
it is the sum of the images in E/T of all semistable torsionfree sheaves
of positive slope. Every such image lies in A/T, because a nonzero map to
the semistable negative-slope B is impossible; its image would be both a
quotient of positive slope and a subsheaf of negative slope. Conversely
A/T itself is such a sheaf. This characterization is intrinsic.

Translations and tensoring by a degree-zero line bundle preserve torsion,
semistability and these slopes. Consequently any coherent finite action
on E preserves A, the inverse image of this intrinsic A/T, and induces an
actual coherent action on B. No additional linearization is chosen.

Each displayed line-class block in A and B is also an actual equivariant
summand of its respective quotient. Distinct line bundles of the same
slope with distinct Chern classes have no Hom in either direction: a
nonzero section of their difference would give an effective nonzero divisor
of theta-degree zero. The blocks involving U are orthogonal as well.
Indeed U dual is O_X(-14theta), so Hom(U,L_alpha)=H0(L_alpha-14theta)=0.
For the reverse Hom use the torsion sequence for F: its hull term has no
section for the same reason, and the torsion term on S has class
\(-2D-(\alpha-14\theta)\), whose theta-degree on S is negative.
It has no nonzero section either. End(U)=C, since
End(F)=O_X plus O_S(-D)^2 and the latter has no global section.
These vanishing statements show that the displayed projections are the
central block projections. An action cannot mix their different Chern
classes, and cannot turn U, which has nonzero torsion, into a line bundle.
It therefore preserves all those projections and summands. This is an
argument on the actual sheaves, not on a decomposition appearing only
after an isogeny.

For each positive-rank line-class block its Chern character is n exp(alpha).
The degree-two Hochschild cap map has rank6: conjugate by exp(alpha), and
its image becomes H2(O_X), which has dimension6. The published BF
trace/evaluation identity shows that its invariant self-Ext2 dimension is
at least6, whether or not that block itself is semiregular. Evaluation
lands in invariants because these translations/tensor functors act
trivially on Hochschild cohomology. Thus

\[
 \operatorname{ext}^2_\Gamma(A,A)+\operatorname{ext}^2_\Gamma(B,B)
       \ge6(u+v).
 \tag{E826.6}
\]

The triangle lemma applies after invariants and yields the same lower bound
for E. On the other hand, weak semiregularity and the invariant CY4
adjunction in supplied S21, specifically(S21.8), force
\(\operatorname{ext}^2_\Gamma(E,E)=\operatorname{rank}c^2_{Rv_q}=18\).
For clarity, the rank18 calculation is the elementary E801 product
calculation: in the volume-form exterior model the balanced character is
omega_+ wedge omega_-, with two nondegenerate two-forms on complementary
four-spaces. Pure exterior-square pieces contribute1 each, and the mixed
piece contributes16 because wedge with each omega is an isomorphism from
vectors to three-vectors. The total is18. A rational B field changes this rank by an invertible
exterior shear, as in the full S21 proof: contraction by a vector becomes
contraction plus wedge by its contraction with B. Thus the normalized
character has the same rank, without pulling back E or its action.
Since6(u+v) is greater than18,
there is a contradiction. This proves the entire architecture assertion.

## 3. Exact character data for an actual coupled example

We now construct a member with no nontrivial direct-sum decomposition,
while retaining the preceding obstruction. Use the actual Gaussian
fourfold and integral divisor basis(theta,theta_U,theta_S,theta_US) of the
positive-defect construction. Explicitly X=E_i^4, theta is product
principal, U is block diagonal with two copies of the matrix[[1,1],[1,-1]],
and S is diag(1,1,-1,-1). Every symmetric integral matrix gives an actual
line bundle by coordinate divisor pullbacks and the pairwise Poincare
bundles (addition pullback minus the two coordinate divisors). These U,S,US
are symmetric integral. D=4theta is very ample since degree4 separates
length-two subschemes on each elliptic factor; the product embeddings and
Segre embedding give the claim. The previously proved Bertini/Koszul
argument gives a smooth integral ordered complete intersection.
For a tuple(a,b,c,d), average its exponential
over the four distinct tuples

\[
 (a,b,c,d),\quad(a,-b,c,-d),\quad(a,b,-c,-d),\quad(a,-b,-c,d).
 \tag{E826.7}
\]

All eight orbits in the following table have four distinct elements. The
last column is the multiplicity of **each** line bundle in that orbit.
The table is exact rational data; floating linear programming was used
only to discover its support, and supplies no premise of this proof.

| Orbit representative | Total weight per unit copy | Multiplicity per line |
|---|---:|---:|
|(-14, 4, 12, -8)|9851034439/7111578272|118212413268|
|(-14, 8, 8, -4)|803399867/888947284|77126387232|
|(-14, 12, 16, -12)|361040431311/28446313088|1083121293933|
|(-14, 16, 16, -32)|21876066325/28446313088|65628198975|
|(14, 8, 12, 4)|154311465847/10667367408|1234491726776|
|(14, 8, 24, -16)|37616523853/85338939264|37616523853|
|(14, 12, 32, 12)|2658612777/28446313088|7975838331|
|(-14, 16, 24, 16)|1/4|21334734816|

Put r=341355757056 and R=32r=10923384225792. The twelve lines with a=14
belong to A, together with U to multiplicity r. The twenty lines with
a=-14 belong to B. The free positive lines have total rank15r and the
negative lines total rank16r. Thus both A and B have rank16r.

Here is a compact full-character verification. For an orbit representative
write \(V_0=2b^2+c^2+2d^2\). Its orbit-averaged exponential has seven independent
subset coefficients

\[
 \begin{split}
 &(1,a,\ a^2+2b^2-c^2-2d^2,\ a^2-2b^2+c^2-2d^2,\\
 &\quad a^2-2b^2-c^2+2d^2,\ a^3-aV_0+4bcd,\\
 &\quad a^4-2a^2V_0+16abcd+4b^4+c^4+4d^4
                      -4b^2c^2-8b^2d^2-4c^2d^2).
 \end{split}
 \tag{E826.8}
\]

The three degree-two positions are the pairs12,13,14; the other three
pairs are their orbit partners. All degree-one coefficients agree, as do
all degree-three coefficients. The character of U is \(2e^{10\theta}-2e^{2\theta}+e^{-2\theta}\),
as follows directly from the actual unit resolution. Weighted by
the table, the free part has the exact seven coefficients

\[
 (31,-14,-212,-196,-196,-1976,-19976).
 \tag{E826.9}
\]

Consequently the sum of A and B is R v_(1/2) in **all sixteen** subset
coordinates. The exact certificate independently expands those sixteen
coordinates over Q(sqrt2), so no omitted component or orbit convention is
hidden by the seven-coordinate notation. Every coherent extension of B by
A has that complete character, local form F^r plus a free rank(R-r), and
canonical defect Qtilde=O_X(14theta)^r on S2. In a triangular transition
matrix the off-diagonal free-to-A extension maps disappear under E825's
ring map ell, so its determinant satisfies the positive requirement exactly.

## 4. Actual Ext1 spaces and absence of the opposite Ext3 direction

For a line pair with difference(a,b,c,d), its two Gaussian 2-by-2 blocks
have parameters(a+c,b+d) and(a-c,b-d). Their determinants are
\((a+c)^2-2(b+d)^2\) and \((a-c)^2-2(b-d)^2\). In this table every
cross difference alpha-beta is nondegenerate. Its index is the sum of
the numbers of negative eigenvalues in those two blocks; each contributes
one for negative determinant, zero for positive determinant and positive
trace, or two for positive determinant and negative trace. The full index
counts over the240 line pairs are36 of index0,144 of index1, and60 of
index2. None has index3. The published index theorem therefore gives

\[
 \operatorname{Ext}^3(L_{\beta_b},L_{\alpha_a})=0
       \quad\hbox{for every such pair.}
 \tag{E826.10}
\]

For the unit target U, Ext3(L_beta,U)=H3(F tensor O(14theta-beta)).
In its length-two resolution only H3 of the first term and H4 of the
middle term could contribute to total degree3. The first term is the line
with class10theta-beta; for every one of the twenty beta's it is
nondegenerate of index0,1 or2, so its H3 vanishes. The middle line has
class2theta-beta, of positive theta-slope16theta4, so its H4 vanishes by
Serre duality and the negative degree of its dual. This proves

\[
 \operatorname{Ext}^3(B,A)=0
 \tag{E826.11}
\]

for every smooth regular choice of the two surface sections. It is not a
numerical rank guess for a differential of the resolution.

For a nondegenerate line pair of index1 its Ext1 dimension is the absolute
product of the two determinants above. For the four beta's in the last
orbit of the input table, the three line terms of the resolution computing
Ext1(L_beta,U) all have index1, and their dimensions are
4718592,3174400,2467584. Hence

\[
 \dim\operatorname{Ext}^1(L_\beta,U)
        \ge2(4718592-3174400)=3088384.
 \tag{E826.12}
\]

This is again a direct cokernel lower bound, requiring no maximal-rank
assertion. These exact dimensions provide all the arrows used below.

## 5. A uniform explicit matrix construction forcing scalar pairs

Let a single directed edge have source dimension m and target dimension n.
If it provides at least ceil(max(m/n,n/m))+2 independent Ext1 classes, one
can choose coefficient matrices on those classes such that the only pairs
(T,S) satisfying T E_j=E_j S for every chosen matrix are
(T,S)=(lambda I_n,lambda I_m).

Here is the full construction. If n is at least m, choose ceil(n/m)
injections F_j:C^m to C^n whose images span C^n, taking consecutive blocks
of m coordinates and the last block ending at n. Include F1 J_m and
F1 J_m transpose as two further arrow matrices, where J_m is the nilpotent
single Jordan shift. The relations for F1 and F1 J_m imply that S commutes
with J_m; the corresponding transpose relation makes it commute with
J_m transpose. These two shifts generate the full matrix algebra: their
products give the end-coordinate rank-one projections and then every
matrix unit. Therefore S is scalar. The spanning injections force T to
be the same scalar.

If m is greater than n, use ceil(m/n) coordinate projections P_j:C^m to
C^n with intersection of kernels zero, and add J_n P1 and J_n transpose P1.
Their equations make T commute with both shifts, hence scalar; the joint
injectivity of the projections forces S to be the same scalar. This proves
the claim for all positive m,n, including the one-dimensional cases.

In a bipartite tree apply this construction separately on each edge, using
linearly independent classes in its actual Ext1 space and zero coefficients
on all unused classes. The scalar constraints on adjacent vertices agree.
Connectedness of the tree therefore forces all vertex endomorphisms to be
one common scalar. This is a construction with explicit ordinary matrices,
not a generic-representation or quiver-root theorem.

## 6. The exact tree and the resulting indecomposable sheaf

Index A0=U, and list the twelve positive line tuples lexicographically as
A1,...,A12. List the twenty negative line tuples lexicographically as
B0,...,B19. These indices are uniquely determined by the orbit table and
(E826.7). The following tree gives, for every edge, the required number
of matrix arrows and the proved available Ext1 dimension or lower bound.

| A index | B index | Matrices required | Available Ext1 |
|---:|---:|---:|---:|
|0|0|18|3088384|
|0|3|18|3088384|
|0|16|18|3088384|
|0|19|18|3088384|
|2|0|5|7462656|
|4|0|60|852992|
|5|0|60|5727232|
|8|0|60|5669888|
|9|0|60|9626624|
|10|0|4|33165056|
|11|0|5|1990400|
|12|0|5|7462656|
|1|3|5|7462656|
|7|3|4|33165056|
|6|16|4|33165056|
|3|19|4|33165056|
|2|1|11|517888|
|2|5|138|790272|
|2|7|12|517888|
|2|9|17|164864|
|2|11|17|336896|
|2|13|12|308992|
|2|15|138|790272|
|2|18|11|8070912|
|4|2|21|435200|
|4|14|4|156672|
|4|17|21|2384896|
|5|4|4|91136|
|5|8|13|302848|
|5|12|19|73728|
|9|6|19|73728|
|9|10|13|302848|

This is a tree on all33 vertices, and every displayed capacity is sufficient.
Its multiplicity ratios are the exact ratios from the input table; the
largest number of matrices needed is138. The attached exact certificate
checks the whole tree, all inequalities and every individual Ext calculation.

The summands A0,...,A12 are pairwise Hom-orthogonal with scalar individual
endomorphism rings, as proved in section2. The same is true of B0,...,B19.
Also Hom(A,B)=0, by their slope comparison (for U use its hull to a
locally free target). Choose the extension class e in Ext1(B,A) by the
matrix construction of section5 on the tree. Since B is locally free,
Ext1(B,A)=H1(B dual tensor A); an actual Cech cocycle glues the local
modules A plus B by upper triangular transition matrices. Their strictly
upper block has square zero, so the usual additive cocycle equation is the
whole gluing condition. There is no additional Maurer--Cartan equation or
assumed dg formality. This gives an actual coherent E in(E826.1), with the
full character and local type already proved in section3. It is ordinary
gluable because it is a coherent sheaf.

We verify indecomposability of this actual object. Every endomorphism of E
preserves A, since its composite from A into B is zero. Its restrictions
(a,b) must satisfy ae=eb. By pairwise Hom orthogonality these are precisely
the vertex matrices, and the tree construction forces all of them to be
the same scalar. Conversely the scalar identity lifts. The kernel of the
restriction map is Hom(B,A), realized by i f p; this is a square-zero ideal
because p i=0. To see that the compatibility condition is sufficient for
a lift, represent e by a Cech cocycle: ae-eb being a coboundary gives local
upper-right entries which complete a,b to an actual global endomorphism.
Therefore

\[
 \operatorname{End}(E)/\operatorname{Hom}(B,A)=\mathbf C,
 \qquad\operatorname{Hom}(B,A)^2=0.
 \tag{E826.13}
\]

An idempotent in this algebra maps to0 or1 in C. If it maps to0 it lies
in the square-zero ideal and is zero; if it maps to1, its complement does
so and is zero. Hence there is no nontrivial idempotent. The coherent
category is idempotent complete, so E is indecomposable. No simplicity is
claimed: Hom(B,A) may be large.

## 7. The invariant middle-Ext obstruction still excludes the whole family

All the hypotheses in section2 hold for every extension with these A,B,
including the indecomposable one. There are u+v=12+20=32 canonical
line-class blocks. For any specified coherent effective finite action
on its middle sheaf, the torsion/HN argument provides the required actual
actions on A and B and their line-class blocks. Equation(E826.11), Serre
duality and the exact invariant triangle lemma therefore imply

\[
 \operatorname{ext}^2_\Gamma(E,E)\ge192.
 \tag{E826.14}
\]

The full balanced character has cap rank18. Thus no member is weakly
Gamma-semi-regular. This failure persists after all the specified
free-to-free couplings, even though the selected member is indecomposable
and satisfies the positive defect determinant from E825. The proof of this
failure examines actual invariant Ext and the full Hochschild cap rank;
it does not infer failure merely from the split starting character.

The general scope is the whole two-slope architecture in section2 with
Ext3(B,A)=0 and at least four distinct line-class blocks. To evade this
particular obstruction, one needs a nonzero opposite cross Ext3 direction,
a different intrinsic filtration, or a construction outside that
architecture. No claim is made that those alternatives succeed or that
all unstable sheaves have the stated form.

## 8. Source and check boundary

The ordinary abelian index theorem is the previously read original
Mumford, Abelian Varieties(1970), section16 printedpp150--153 and162--163.
The unit sheaf resolution and End description are the fully proved UG/US
inputs. Actual section existence uses the previously checked very-ampleness
and Bertini argument for D=4theta. The general triangle lemma, matrix
construction, Cech extension and endomorphism proof are supplied in full
above.

For the categorical rank consequence, this proof uses the full invariant
CY4 adjunction from supplied DEG_L S21, including the paragraphs preceding
(S21.8), not merely ordinary forgetting compatibility. The entire displayed
S21 proof through(S21.8) was freshly reread for this derivation; its original
source statuses are retained. Published BF2008 Theorem5.1.3,
Proposition5.2.2, Corollary5.2.3 and Proposition6.2.1/Theorem6.4.2 with
Proposition6.4.4, authorpp24--27 and29--33, give evaluation/trace composition
as previously fully read. No supplied preprint premise has been renamed as
a new published theorem. The full balanced rank18 calculation from E801
was freshly reread and its short proof is repeated in section2.

Exact input is rm_two_slope_exact_input.json. The complete certificate
rm_two_slope_coupling_certificate.py verifies the full sixteen-coordinate
character, positive integral multiplicities, all cross Ext3 vanishings,
all148 sufficient edge capacities, and the33-vertex spanning tree. It
imports no floating optimization result as a theorem: exact rational input
is checked from scratch. The exploratory linear-programming script is
retained only as provenance. An initial certificate output serialization
failure was repaired by converting an exact symbolic integer to a Python
integer; the failure is retained in rm_two_slope_coupling_attempts.json.
No generic multiplication rank, invariant action or semiregularity is
claimed to have been computationally verified. The latter is excluded by
the written invariant argument above.

The separate exact matrix checker rm_rectangular_brick_certificate.py actually passed all36 pairs1<=n,m<=6 over the prime1009. Each relation matrix has rank n²+m²−1 modulo that prime; the scalar solution supplies the opposite characteristic-zero bound, so those finite cases are exact. The all-size result is the complete injection/projection and Jordan proof in section5, not an extrapolation from these cases.
