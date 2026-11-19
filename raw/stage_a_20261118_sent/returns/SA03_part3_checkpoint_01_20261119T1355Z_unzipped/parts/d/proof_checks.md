# Cote 93: exact scope of checks

These are the present run’s arguments. They do not alter the diplomatic text.
Polynomial and finite-field checks have their code and literal outputs alongside
this file. An opened theorem statement is not counted as an independent proof.

## D-P01. Genus-one cohomology (CL-SA03-601–603)

Use the source’s fibre classification (carried as background): an integral
arithmetic-genus-one fibre with the smooth marked point is Gorenstein, and its
dualizing line is trivial. On such a fibre, Serre duality identifies H¹(O(ne))
with the dual of H⁰(O(−ne)); the latter vanishes for n>0 because a nonzero
section of a line bundle of negative degree on an integral proper curve is
impossible. Riemann–Roch then gives h⁰(O(ne))=n. Relative cohomology and base
change give the stated locally free bundles and vanishing; that general
theorem is used, not reproved. The smooth section is Cartier, so these twists
are actual line bundles. For n=0 the geometrically integral proper fibres
have H⁰ equal to the residue field, the hypothesis of Stacks0E1J. This proves
the reduction to the checked foundational results, not the entire relative
duality or cubic-classification theorem. Stacks0E6N fixes the modern degree
−1 of p!O. Both independent transcriptions and the 1968 printing retain the
positive superscript, so the ink is not decided.

## D-P02. Integral Weierstrass calculations (CL-SA03-604–620)

The exact program expands the equation after the full coordinate substitution,
checks all five new coefficients, and checks every displayed b,c,d and Δ
identity over the integer polynomial ring. It therefore remains valid after
arbitrary base change, apart from explicitly inverted units. It also reduces
the exceptional charts modulo2 and3. A zero symbolic residual is a certificate
for the particular polynomial identity; it does not prove a moduli
representability or graded-generation theorem. The missing derivative in
the fourth coefficient and the incorrect middle entry in the composition
law have nonzero literal residuals. Their corrected formulas are specified
with a fixed composition order. The genus-one chart with6 invertible includes
singular curves; only its discriminant open represents smooth curves.

## D-P03. Hasse polynomial and valuations (CL-SA03-620,625)

Let p=2n+1. In xⁿ(x−1)ⁿ(x−λ)ⁿ the x^(2n) term comes from paired exponents
i and n−i. The signs have product(−1)ⁿ and the coefficient is
(−1)ⁿ binom(n,i)² λ^i, after reindexing. Summing proves the displayed
polynomial for all odd primes; the explicit checks for primes3–31 merely
confirm the implementation. The source’s differential convention must still
be kept when calling that coefficient a Hasse scalar.

In equal characteristic3, c₄=b₂², hence j=b₂⁶/Δ; in characteristic2,
c₄=a₁⁴, hence j=a₁¹²/Δ. For a DVR with Δ a unit and finite v(j), the two
divisibilities follow. The two equal-characteristic families have Δ a unit
and attain6 and12. The mixed-characteristic examples also have unit
discriminants, but valuations3 and15; they disprove an extension of the
claim, not the explicitly characteristic3/2 margin. All fractions and
valuations appear in the output. At j=1728 the correct vanishing expression
is j−1728=c₆²/Δ. A unit j cannot itself have positive order there.

## D-P04. Geometric automorphisms and sheafification (CL-SA03-614–626)

For y²+y=x³ overF4 the program exhausts all24 triples satisfying the
automorphism equations, verifies closure and associativity, and records
element orders. Its order8 kernel has one involution and six elements of
order4, giving Q8; the order3 scalar subgroup splits the quotient. For
y²=x³−x overF9, u⁴=1 and r³=r give12 transformations, and composition is
checked. These are checks of the geometric groups. The central elliptic
involution extends naturally to every deformation: on a marked deformation,
applying it provides an isomorphism to the object with the sign-changed
marking, so its action on deformation isomorphism classes is trivial. This
does not prove that the remaining action is faithful or calculate a wild
invariant ring. Over a disjoint union of two generic bases, each sign can be
chosen independently, giving four global automorphisms. That verifies the
source’s sheafification warning exactly.

## D-P05. Orientation signs and uniqueness (CL-SA03-636)

In a locally flat codimension-one chart, the two half-spaces have opposite
outward normals. The outward-normal-first convention therefore induces
opposite boundary orientations. The side sheaf is overY, not the ambientX.
For two sections of the orientation étalé space, their equality locus is
open; separation makes it closed. On connectedX it is all ofX if nonempty.
This is uniqueness of an existing orientation, not existence or a proof of
the entire equivalence between the handwritten and printed axioms.

## D-P06. Conditional strong convergence (CL-SA03-638)

Assume sup||t||=M<∞, tθ=θ, θy is in the norm-closed convex hull ofTy,
and for any finite list t_i all sufficiently late t satisfy tt_i=t.
Choose convex coefficients with ||θy−Σα_i t_i y||<ε/(M+1). Then
θy−ty=t(θy−Σα_i t_i y), whose norm is at mostMε/(M+1)<ε.
These assumptions prove exactly the visible estimate. Weak compactness
alone does not supply the missing absorption lemma. If θ is an idempotent
two-sided zero in the operator closure, imθ is the fixed space and the
displayed direct-sum argument is valid. Existence ofθ and the vector-measure
application remain dependent on pages not supplied.

## D-P07. Schwarzian and the earlier run’s p-curvature shortcut

For S(f)=f'''/f'−(3/2)(f''/f')², direct differentiation gives
S(exp∘f)=S(f)−(f')²/2, hence the source’s G=−2S has coefficient1.
The code also checks Möbius postcomposition invariance and the ratio-of-ODE-
solutions formula S(y1/y2)=2q for y''+qy=0 with nonzero Wronskian.
These are differential identities, not a proof that the ambiguousπ-action
or a proposed arithmetic family has the required geometric origin.

The earlier note’s broad p-curvature implication is tested independently:
overF_p[t], p odd, let D=d/dt and A=[[0,1],[1/4,0]]. The connection D−A
is integrable on the line. D^[p]=0 and constantA commutes withD, so its
p-curvature is−A^p=−A, an invertible matrix. Thus the associated rank2
equation need not have nilpotent p-curvature. This is not attributed to
the manuscript. Cartier descent requires zero p-curvature; nilpotence
alone is a different condition. Katz1972Proposition2.3.2 andTheorem3.2,
visually inspected on printedpp22 and40, impose properness, locally free
Hodge cohomology with base change, and E1 degeneration before identifying
the graded geometric p-curvature map with the twisted Kodaira–Spencer map.

## D-P08. What FV=p proves (CL-SA03-660)

Let F:Q→P,V:P→Q withFV=p onP,VF=p onQ andp injective on both modules.
F is injective: Fx=0 impliespx=VFx=0. If Fx=py=FVy, injectivity gives
x=Vy. Modulo p this proves ker(Fbar)=im(Vbar); interchangeF,V for the other
equality. It does not prove local freeness. In R=Z_p[x,y]/(xy−p), the
maps F=x,V=y satisfy the hypotheses; R is a domain andp is a nonzerodivisor.
Modulo p, annihilator(x)=(y) and annihilator(y)=(x), so the complex is
exact. At the node, the nonzero cyclic image(y) has nonzero annihilator(x)
and cannot be free of rank1; Nakayama excludes other positive ranks.
This is a linear-algebra counterexample, not an absolute-crystal example.

## D-P09. Filtrations, Frobenius and dimensions

Overk[ε]/ε², ordinary Frobenius killsε. The direct-summand lines generated
by(1,0) and(1,ε) are distinct but have identical Frobenius pullback. This
does not refute the programme’s crystallineφ, whose exact site matters.
Across a square-zero idealI, with a fixed locally free ambient liftH and
a fixed locally split subbundleF moduloI, locally every lift is a graph.
Differences of graph maps lie in Hom(F,H/F)⊗I. For ranksg and2g the rank
isg². The affine global torsor follows by the usual patching of this
quasicoherent Hom sheaf, conditional on existence of a lift. None of this
proves the effectivity or automorphism assertions of the full deformation
theorem. μ_(p∞) over an algebraically closed characteristic-p field has no
nonidentity geometricp-power torsion points but is a nonzero group scheme;
this warns against the naive geometric-point Tate realization only.

## Evidence boundaries

The supplied sources are the only manuscript witnesses. Full third-party
PDFs used for inspection remain outside the deliverable. The literal
computer outputs and brief reference/search metadata are included.
Publication witnesses, theorem statements, proof arguments, independent
re-proofs and executable algebra certificates receive different event types.
