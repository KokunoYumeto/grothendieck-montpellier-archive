# Independent whole-proof audit: SF-E824 and UG unit gluing

Reviewer: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed.
Run: HODGE_DIVISION, 2026-11-21. The actual record-write timestamp is in
`audit_record.json`; no estimated start/end interval is asserted.

**Outcome: PASS for both complete written proofs in their stated scopes.**
No full derived trace, spectral-sequence degeneration, equivariant splitting,
or preservation of semiregularity under an isogeny is needed or assumed.

## Exact material read

- `agents/sixfolds/rm_unit_gluing_obstruction_draft.md`, current SHA-256
  `f42a0232fbbcfbd21a1aa66516888b3d142658d7b3d1aff16c27df7d3f8c1ffe`.
  I read the entire original mathematical text and both later precision
  repairs: the theta subscript typo and the explicit affine/stalk complex
  vector-space splitting, with no global or O-linear splitting claimed.
- `agents/sixfolds/rm_unit_gluing_analysis_draft.md`, SHA-256
  `16b9e88d5c5c5190628272560e4749daa475da6b585cbc80af56e199abeacc77`.
  I read every section, including all endomorphism/Ext calculations, the
  chain nullhomotopy, actual extension classification, actual nontensor
  family and the warning about full derived descent.
- The complete author `rm_unit_gluing_certificate.py` was read. It was not
  imported or rerun; the independent calculation below uses different
  arithmetic.
- The complete `rm_unequal_slope_compensation_proofs.md` was read, including
  the exact free resolution, arbitrary-bivector local corrections, all16
  positive hull multiplicities, and the distinction between actual
  construction and semiregularity. Its character is independently
  reconstructed below.

## 1. The local algebra and the globally twisted positive Ext sheaves

For the local regular sequence x,y put v=(-y,x)^t, w=(x,y),
F=R²/(Iv), I=(x,y). The complex R→R²→R² with maps v and vw is
exact before F. Indeed wv=0; ker(vw)=ker(w)=Rv, since multiplication
by the nonzero column v is injective in the regular domain. Its image
in degree zero is Iv. The hull map to I has kernel T=(R/I)v, whose
annihilator is exactly I.

Every endomorphism descends to multiplication by a on I and hence its
hull R. Compatibility with the unit local extension class forces the
torsion scalar to be a modI. After subtracting a identity the map has
image in T and kills T, so factors through I→T. Every such map occurs,
because the Koszul relation is zero in T. This gives precisely
End(F)=R⊕(R/I)², with the second summand square zero. The matrix vb
realizes it, and (vb)(vc)=v(bv)c vanishes on F because bv∈I annihilates T.
This proves commutativity of the actual degree-zero algebra, rather than
only of a quotient.

I independently reconstructed the Hom complex F²→F²→F with maps
u w_F and w_F, where u=(x,y)^t and w_F(a,b)=−ya+xb. If w_F(a,b)=0,
the hull relation yields p(a)=xc,p(b)=yc. Then a=ce1+t1,b=ce2+t2,
and c v=0 forces c∈I. Subtracting u m for p(m)=c leaves T².
The intersection uF∩T² is zero, since it forces p(m)=0 and then uT=0.
The incoming image is u(IF); ker(u)=T⊂IF. Hence Ext¹ is
(F/IF)⊕T² and Ext² is F/IF, of local ranks4 and2 on S.

Both actions of the square-zero ideal vanish on these positive Ext
groups. The right action is precomposition with the explicit chain lift
(vb,(bv)I2,bv), so it is multiplication by an element of I. The left
action kills T² and uF, and sends F into T⊂IF in the last quotient.
Thus centrality is proved on both sides, with no illicit implication
from degree-zero commutativity.

Restoring the actual resolution twists gives Ext¹=i*O_S(D)^4 and
Ext²=i*O_S(3D)^2. In particular the Ext² twist uses (F/IF)(4D), while
the two Ext¹ pieces are (F/IF)(2D) and T(3D)^2. End(F) is globally
O_X⊕i*O_S(−D)^2; the scalar splitting is intrinsic. Higher local Ext
vanishes by the length-two locally free resolution.

I also checked the product nullhomotopy in UG.9 in every degree. It
explains correctly why the zero product on the sheaf End algebra does
not provide strict multiplicative chain lifts. The proof never upgrades
this observation to formality or to a trace on the entire derived object.

## 2. Actual nontensor forms and their complete characters

Applying Hom from the actual two-term resolution of H I_S into
i*(H|S(−2D)) has zero differential. It therefore gives exactly
H¹(End(H|S)(−D))²⊕H⁰(End(H|S)) in global Ext¹. Fixing the identity in
the latter factor still leaves every vector in the first factor as a
genuine coherent extension. The zero vector is H⊗F.

The square-zero thickening Y=(X,End(F)) gives actual transition matrices
in GL_r(End(F)). Multiplying the hull transitions by1+a_ij obeys the
ordinary additive cocycle equation because J²=0. No projective cocycle or
unproved higher gluing condition remains. Conversely every local form of
F^r has such transitions, and its hull reduction is locally free. Tensoring
F over its endomorphism algebra with the resulting bundle on Y recovers
the sheaf locally and hence globally.

The nonzero parameter really detects a nontensor isomorphism class, not
only a marked extension. An isomorphism induces an automorphism of the
canonical hull and, by the unit local class, its same restriction on
torsion. The zero parameter is functorially preserved; conjugation on
the parameter space is invertible and cannot take a nonzero class to zero.
Any alternative tensor hull is already isomorphic by taking double duals.

For the specified difference class delta, the four eigenvalues are
0,16−12sqrt2,0,16+12sqrt2. After subtracting3a, for a=1,2,3, exactly
three are negative, since0<16−3a<12sqrt2. The index theorem and RR give
1071,6768,19359 in degree three. The restriction Koszul complex then has
only that cohomology row; H¹ on S is the kernel of its first map, so its
dimension is at least19359−2·6768=5823. This does not presume maximal
rank of any multiplication map. All16 positive hull multiplicities and
the complete balanced character of rank522387689472 were independently
checked. Every extension preserves that character. No finite action,
indecomposability or semiregularity of this constructed family is inferred.

## 3. The canonical first-overlap obstruction

For these sheaves REnd has cohomology only in degrees0,1,2. The first
truncation triangle gives an injection
H²(tau≤1 REnd)→Ext², with image equal to the kernel of the edge map
to H⁰(Ext²sheaf). Its preceding term is H^{-1}(Ext²sheaf)=0, so
there is no ambiguity from choosing a lift. The second truncation
triangle gives the canonical map from that image to H¹(Ext¹sheaf),
with kernel exactly the image of H²(End). This proves the filtration
claim directly, without degeneration assumptions.

The arbitrary-bivector local correction in the compensation proof is
valid: the uncorrected complex square is epsilon(0,0,−P)^t and the
two displayed corrections sum to(0,0,P)^t. The corrected free complex
has flat cokernel over dual numbers, by the elementary two-step cycle
lifting argument. Therefore the global characteristic class of pi is
locally zero and lies in this first filtration piece.

In a Cech resolution, removing the internal degree-two component by
these local nullhomotopies leaves precisely the differences on overlaps
in bidegree(1,1). The total cocycle equation gives the Cech cocycle in
the Ext¹ sheaf. This identifies the canonical truncation image with the
actual obstruction to lifting transition isomorphisms.

## 4. Why the unit first-overlap class is nonzero

The degree-one semiregularity morphism REnd(F)→Omega¹[1] vanishes on
the embedded sheaf End(F). Its scalar restriction is trace of the
Atiyah class, namely ch1(F)=0. On i*J the morphism group
Ext¹_X(i*J,Omega¹) is zero: the codimension-two regular-sequence
resolution has local Hom and Ext¹ zero against a locally free target,
so the two possible total-degree-one terms both vanish globally.
Thus the semiregularity morphism kills the image of H²(End(F)).

The published BF identity gives sigma¹ rho(pi+)=pi+ contraction ch3(F).
For ch3(F)=−2k³(theta++theta−)^3, only its theta+²theta− term survives
this contraction, giving−12k³ eta+ theta−. This is nonzero in H³(Omega¹)
on the abelian fourfold. Local vanishing of rho and the preceding exact
filtration therefore force the specific first-overlap kappa_F(pi+) to
be nonzero. It is not merely an unspecified nonzero global Ext class.

## 5. The endomorphism-lifting derivation and the only trace needed

On affine sections/stalks, a complex-vector-space splitting identifies a
flat dual-number deformation with F⊕epsilon F. The cochain
a rho1(r)−rho1(r)a is a bar1-cocycle. In the associativity equation,
the fixed multiplication perturbation commutes with every original
R-linear endomorphism, so the two terms cancel. Changing a lift adds
a boundary. Changing the local module deformation by a class beta in
Ext¹ changes this by a beta−beta a, zero because both actions of End(F)
on Ext¹ are central. Hence the class defines a global C-linear sheaf
derivation partial_pi:End(F)→Ext¹sheaf. No O-linear or global vector
space splitting is used. The commutator expansion proves Leibniz, and
complex constants are killed.

For a transition matrix G, direct expansion of
G rho1_i−rho1_j G, followed by multiplication by G^{-1}, gives
k_ij I+G^{-1}partial_pi G. The first term is scalar in the central
Ext¹ module. Positive Ext conjugation factors through the hull matrices,
so ordinary matrix trace is a globally defined sheaf morphism.
The permutation expansion of the determinant proves the logarithmic
derivative identity for this commutative ring and central module. Thus
tr kappa_M=r kappa_F+[det(G)^{-1}partial_pi det(G)] in H¹(B).
This reasoning establishes precisely a trace on the first overlap
class; it does not construct or assume a cyclic derived trace.

## 6. Killing the determinant correction and the B field

The negative-ample Koszul resolution has cohomology only in degree four,
so H¹(S,J)=0. Since the square-zero unit sequence is split by scalar
inclusion, Pic(Y)→Pic(X) is an isomorphism. If c1(H)=0 in rational
cohomology, it is zero integrally on an abelian variety, and det(H) lies
in Pic0. The elementary harmonic/exponential-sequence description gives
locally constant unitary transition functions. The global derivation
kills those constants; changing determinant frames changes the logarithmic
derivative by a Cech coboundary. Therefore tr kappa_M=r kappa_F.

For B=0 the balanced cap kernel gives rho_M(pi++q eta+)=0 in ordinary
Ext by the supplied finite-action evaluation/forgetting compatibility.
The eta term lies in the image of H²(End(M)), so its first-overlap
class vanishes. This contradicts the nonzero trace r kappa_F.

For rational algebraic B, choose[m] so m²B is integral and tensor the
etale pullback by its line bundle. The hull first Chern class becomes
zero. The pulled-back smooth CI remains connected by its negative-ample
Koszul resolution, and is thus integral. Local form F^r and the unit
extension are preserved. Etale Atiyah pullback and line tensoring give
exactly the B-sheared evaluation identity, with pi'=m^{-2}pi and
eta'=m²eta. The needed ordinary characteristic vanishing pulls back from
the original object. No assertion that semiregularity itself pulls back,
and no transportation of a finite action, enters the proof.

## 7. Independent arithmetic and source boundary

`independent_check.py` uses an original sparse integer polynomial matrix
implementation, then an original pair model of Q(sqrt2) and the16-element
square-zero divisor algebra. It imports neither author code nor Sympy.
Actual run PASS in0.004297seconds:

- generic chain-map identities and all three components of the product
  nullhomotopy;
- arbitrary local Poisson correction P;
- all16 full hull characters, positive integer multiplicities and exact
  rank522387689472; multiplication by the full unit character gives the
  balanced character;
- exact index-three dimensions1071,6768,19359 and lower bound5823;
- positive-Ext Euler consistency192·D^4/24.

The written Ext classification, global gluing, filtration, derivation,
determinant descent and finite-action implication are mathematical proof
checks, not claims supplied by that computation.

The published BF source is the same full author version of the published
Advances in Mathematics217(2008),243–281 paper already read for E823:
https://arxiv.org/pdf/math/0606730 . I freshly reread Proposition5.2.2
with its complete proof onp26, Corollary5.2.3 onp27, the definition and
Proposition6.2.1 onpp29–30, and Theorem6.4.2 and its proof setup onpp31–32.
The complete surrounding proofs were already checked during E823.
The finite-action compatibility remains exactly supplied DEG_L S21.6–8,
previously read and accepted, not independently reproved in this audit.
Mumford, *Abelian Varieties*, §16: the RR/vanishing statements pp150–153
and the precise nondegenerate index theorem statement p155 were reread
from the original scan. The complex Hermitian-sign interpretation is
used with exactly that hypothesis; the nondegenerate eigenvalues above
verify it. No new proof of the published index theorem is claimed.

## 8. Scope and presentation precision

PASS applies to every coherent sheaf locally isomorphic to the full unit
module F^r on the specified smooth ample CI, with positive rank and the
entire algebraically B-normalized balanced character, for any specified
effective coherent finite translation/tensor action in S21's scope.
It does not cover arbitrary added free summands, unequal local ranks,
nonunit/vanishing matrices, other slopes, singular/nonreduced support,
or arbitrary perfect complexes.

The UG draft's final paragraph accurately records the unresolved attempt
to descend a full derived trace. In its canonical version it should say
that E824 avoids this older gap for the unit forms by using only the
first-overlap class. This is a presentation update, not a mathematical
defect. The two typo/splitting precision repairs in E824 are accepted.
