# Proof and computation audit: cotes 46 and 53

Reviewer: GPT-6 Astra Pro / inherited effort / agent46. Date: 19 November 2026.

This file separates checks of the author's calculations, current reconstructions,
and explicit counterexamples. It does not repair the diplomatic transcription.
The executable certificates are `scripts/checks.py`; its actual output is
`outputs/computations.json` and `outputs/computations.txt`. A finite example is
never used as proof of a universal statement. Reference keys resolve in
`references.bib`; the search/open provenance is in `literature_search.tsv`.

## 1. Rigidified torsors

Claims CL-SA18-46001–46002. With the convention in the transcription,
compatibility is `u a = b f(u)`. Right multiplication by `f(u)⁻¹` gives
`b=u a f(u)⁻¹`. There is no permissible commutation of `a` with `u`.
For `f=id`, take `u=(12)` and `a=(23)` in S₃, and put `b=uau⁻¹=(13)`.
The hypothesis holds; `b⁻¹a≠1=f(u)u⁻¹`. The certificate prints the actual
permutations and products. Thus the displayed simplification is literally false.

The corrected coordinate equation also verifies the proposed classification:
the standard object has automorphisms `N=Eq(f,id)`. If the Lang map is an
epimorphism of sheaves, each local parameter can be changed to the standard
one. The sheaf of isomorphisms from the standard object is an N-torsor;
contracted product supplies the inverse construction. The site and local
surjectivity are part of this reconstruction. This is a targeted check of the
written torsor argument, not an independent proof witness for another folder.

## 2. The Lang map, quotient, and finiteness boundary

Claims46003–46005. For `L(x)=f(x)x⁻¹`, with `df=0`, translations identify the
tangent map with minus an invertible translation. Smoothness of G/S then gives
étaleness. Over an algebraically closed field, the twisted action
`t·a=f(t)a t⁻¹` has étale orbit maps, so each orbit is open. A connected fibre
cannot partition into two nonempty unions of open orbits; hence the orbit of1
is the whole fibre. This proves surjectivity fibrewise and therefore globally.

If `L(x)=L(y)`, then `f(y⁻¹x)=y⁻¹x`; conversely `L(yn)=L(y)` for `n∈N`.
Thus the right N-quotient maps monomorphically and étale into G; it is an open
subscheme by Stacks025F. Fixed points are étale. Finiteness in the finite-field
finite-type case follows from the finite set of rational points and the
zero-dimensional finite-type fixed scheme. An infinite constant group over F_q
is smooth and étale, its Frobenius is the identity, and its fixed group is
infinite. This does **not** refute the connected finite-type Lang theorem.

## 3. Frobenius-fixed modules and local systems

Claims46006–46007. For a rank-n vector bundle with invertible Frobenius
structure, the scheme of frames respecting that structure is locally the
solution space of the GL_n Lang equation. GL_n is smooth connected, and its
Frobenius fixed subgroup is GL_n(F_p), finite étale. Consequently this frame
scheme is an étale locally trivial GL_n(F_p)-torsor, yielding the F_p local
system; tensoring the latter with O gives the inverse.

For a finitely presented module M over R, base change of Fitting ideals gives
`Fitt_i(M)=Fitt_i(M)^[p]`. Localize at a prime. Every proper finitely generated
ideal I in the local ring satisfies `I^[p]⊂mI`; if `I=I^[p]`, Nakayama gives
`I=0`. Every localized Fitting ideal is therefore0 or R. The finite-presentation
criterion in Stacks07Z6, Lemma15.8.8, gives local freeness. The use of finite
generation of the Fitting ideals is explicit.

For failure with a finitely generated module, let R be the valuation subring
of `F_p(t^(1/p^∞))` with nonnegative t-adic valuation. Equivalently take the
union of the local rings `F_p[t^(1/p^n)]_(t^(1/p^n))`. R is perfect. Its maximal
ideal m consists of positive-valuation elements and is not finitely generated:
a finite list has a smallest positive valuation, while a suitable further
p-th root has smaller positive valuation. M=R/m is cyclic and nonzero. Because
Frobenius is an automorphism preserving m, `F* M≅M`. M is not locally free:
over the local domain R a nonzero free module is torsion-free, whereas m
annihilates M. It is not finitely presented. The finite valuation sequence in
the output illustrates, but does not replace, this all-n argument.

## 4. Frobenius formularium and ideal powers

Claims46008–46016,46018. In affine coordinates the relative Frobenius ring map
is `B⊗_(A,F_A)A→B`, `b⊗a↦b^p a`. Tensoring the base gives compatibility with
base change; composition gives the iterate formulas. The absolute Frobenius
is identity on prime ideals because `b^p∈q iff b∈q`. The relative map is integral,
radicial and surjective. These are scheme morphism assertions, distinct from
an underlying-scheme isomorphism induced by a perfect base-field automorphism.

For an ideal I the image ideal is `I^[p]=(a^p:a∈I)`. It need not be `I^p`:
`xy∈(x,y)²` and `xy∉(x²,y²)`. For q=p^ν the lengths of
`k[x,y]/(x^q,y^q)` and `k[x,y]/(x,y)^q` are q² and q(q+1)/2; monomial bases are
enumerated in the output. Thus a Frobenius neighbourhood and the ordinary
order-q neighbourhood are different already in dimension2.

Frobenius pullback is ordinary tensor base change, hence right exact and
compatible with tensor products and the constructions specified by universal
properties. For nonflatness let R=F_p[ε]/ε². The inclusion `(ε)→R` becomes zero
after Frobenius pullback, although its source becomes
`R/(F(ε))=R`. Hence left exactness cannot be assumed. For transition functions
`g_ij`, pullback sends them to `g_ij^p`, precisely the transition functions of
`L^⊗p`. Projective coordinates of degree p yield pullback O(1)=O(p).
Over F₄ a scalar a with a²≠a shows why the coordinate p-power map is semilinear;
its second iterate is the identity on the base field.

The locally finitely presented unramified/étale criteria are checked against
SGA5XV §1 Proposition2, not inferred solely from these examples. The deleted
scan17 proposition is kept separate from the live augmentation-ideal statement.

## 5. A homeomorphism onto a closed subset is affine

Claim46017. Let f:X→Y be such a morphism. For y in its image choose an affine
neighbourhood V of y and an affine neighbourhood U of its unique preimage,
mapping into V. Since f is a homeomorphism onto a closed subset, some principal
open D(h)⊂V contains y and has `D(h)∩f(X)⊂f(U)`. Its inverse image is the
principal open `D(f#h)` in U, hence affine. Points outside the image have
neighbourhoods with empty inverse image. Affineness is local on the target,
so f is affine. This is exactly the argument checked in Stacks04DE; no universal
homeomorphism, properness or finite-presentation hypothesis was inserted.

## 6. Units, Pic[p], and logarithmic differentials

Claims46019–46022. For a proper reduced scheme over a perfect field, its finite
global function algebra is reduced, hence a finite product of finite field
extensions; those extensions are perfect. Thus global units are p-divisible.
The exact sequence with kernel pth powers gives the Pic[p] identification
asserted in the source. This does not make the p-torsion group scheme reduced.

For a p-torsion line bundle choose local trivializations and a trivialization
of its pth power. Local units differ by pth powers, so their logarithmic
differentials glue. On a smooth scheme, Cartier's logarithmic criterion
identifies the fixed forms with locally logarithmic ones and gives the stated
image, with the Frobenius twist retained. The source's proposed injection
`K*/O*→Ω¹_K/Ω¹_O` is false: in a DVR of characteristic p, t^p is a nonunit,
has nonzero valuation, and `dlog(t^p)=0`. Dividing by pth powers is necessary.
Normality alone is not a license to replace the local ring by a regular ring.
Oda's finite-group-scheme/de Rham comparison is not recovered by listing the
rational points of Pic[p].

## 7. Restricted p-power and height-one duality

Claims46023–46025. For D=d/dt on k[t], D^p=0: each pth derivative contains a
product of p consecutive integers. The Euler derivation E=tD has
`E^p(t^n)=n^p t^n=n t^n`, so `E^p=E`. This disproves O-linearity of
`D↦D^p`; there is no ordinary O-linear transpose. The certificate verifies
monomials through degree2p for four primes, while the preceding factorial and
Fermat calculation proves every degree.

The finite-flat height-one correspondence is the p-Lie statement of
SGA3VIIA Theorem7.4 and Remark7.5. The bracket vanishes exactly in the
commutative restricted-Lie situation; the dual cotangent operations must be
defined in that category. A general quasi-coherent module is not silently made
finite locally free. The uncertain last word on46:22 remains a reading alarm.

## 8. Verschiebung and symmetric tensors

Claims46026–46028. In the p-fold symmetric construction, a mixed monomial with
multiplicities `m_i<p`, `Σm_i=p`, has orbit size `p!/∏m_i!`, divisible by p.
Only pure pth tensor powers survive the relevant diagonal symmetrization in
characteristic p. This divisibility, including all multiplicity patterns in
three variables for p=2,3,5,7, is recomputed. The general argument uses that the
numerator has one factor p and the denominator none.

The resulting field-base map is the Verschiebung after the stated twist.
On G_a, V=0 and [p]=0; on G_m, V is the identity on the appropriate twist and
F is pth power; on α_p both F and V are zero. Finite locally free Cartier
duality interchanges F and V. SGA3VIIA §4.3 verifies the flat-base extension
and FV=VF=[p]. The earlier projection also named Ver has a different domain
and is not this operation. The newly supplied C46-01 opening is part of the
same construction as the already transcribed scan27.

## 9. Uniform structures on a reused sheet

Claim46029. If Δ⊂W and `W∘W⁻¹⊂V`, then
`W⁻¹=Δ∘W⁻¹⊂W∘W⁻¹⊂V`; inversion supplies the corresponding symmetry
requirement. The filter axioms and closure under composition give the usual
entourage formulation. The program exhausts all relations on a three-element
set for the displayed implication. The proof is the inclusion argument, not
the finite enumeration. The reused sheet supplies no reliable authorship or
date. BourbakiUniform is a comparator, not an attribution of this sheet.

## 10. Étale Frobenius and the gluing fragments

Claims46030–46036. For U étale over X in characteristic p, relative Frobenius
is an isomorphism. This yields the canonical comparison of inverse-image
functors on the small étale site, hence the identity on cohomology after the
correct coefficient identification. It does not say every written coefficient
automorphism is literally the identity: over Spec F_p, the finite étale object
Spec F_(p²), hence its representable étale sheaf, carries a nontrivial
p-Frobenius even though the base Frobenius is the identity. It also does not say geometric
Frobenius acts trivially on geometric cohomology.

The topology cannot be changed without a new argument. For K=F_p(t), the
fppf Kummer sequence gives H¹(K,μ_p)=K*/K*^p. The class of t is nonzero,
by its valuation. Pullback by absolute Frobenius, using the usual μ_p
base-change identification, sends [a] to [a^p]=0. In contrast the étale sheaf
of μ_p-points is trivial on this reduced field site. This is a concrete
boundary between the two sites; it is not a counterexample to the precise
étale coefficient-comparison theorem or a resolution of the abstract
unidentified converse.

In the gluing fragment a sheaf embedding in a product followed by agreement on
an overlap is an equalizer, hence a kernel in the abelian case, not a cokernel.
The full square and its adjoints are not legible enough to prove the proposed
general converse or derived comparison. Those claims remain F or C with the
missing hypotheses stated; no recollement theorem is substituted for them.

## 11. Brauer–Severi geometry, Picard, and linear systems

Claims46037–46038,46043–46049,46051,46057–46060. Étale locally a
Brauer–Severi scheme is projective space. Transition matrices are only defined
up to scalar; choosing lifts produces a central Čech2-cocycle `c_ijk`.
Tensor representations multiply cocycles, and the degree-n symmetric
representation sends the scalar c to c^n. Thus its Brauer obstruction is n
times the original class. This calculation is redone symbolically.

A section, or a suitable degree-one invertible sheaf, supplies the splitting
mechanism used in BrauerII1966 §0. The map determined by a quotient
`f*E→L` has pullback O(1)=L; it is not linear merely because it is a
monomorphism. The quadratic Veronese `P¹→P²`, `[x:y]↦[x²:xy:y²]`, is a closed
immersion and satisfies `Z₁²=Z₀Z₂`, but pulls O(1) back to O(2). It is an exact
counterexample to the missing degree-one implication.

For a vector bundle E, the canonical pairing between symmetric powers can
degenerate in small characteristic: in degree2 on a rank-two free module the
permutation pairing has diagonal `(2,1,2)`, of rank1 modulo2. The appropriate
dual object is a divided-power construction unless extra factorial invertibility
or a different convention is imposed. The manuscript's tilde must be read on
the ink. The later scans58–60 genuinely develop the degree-n question marked
earlier; the earlier margin should not remain labelled unanswered.

The projection formula `f*(f*L⊗F)=L⊗f*F` for an invertible L follows by
trivializing L and gluing. Using it to descend an invertible sheaf additionally
needs the asserted evaluation isomorphism and base-change/local-freeness
hypotheses. The cohomological hypotheses in the Picard margin are not deleted
by this formal identity. The generic Brauer injection retains the regular or
other precise hypotheses of BrauerII1966; no singular-base theorem is inferred.

## 12. Coxeter and graph calculations on reused pages

Claims46039–46042. For a finite real reflection group normalize the simple
roots to have length1. Their Gram matrix has diagonal1 and entries
`−cos(π/m_ij)≤−1/2` on edges, with0 off edges. If a cycle has r vertices,
the vector with coefficient1 on those vertices has quadratic value at most
`r−r=0`; chords can only decrease it. This contradicts positive definiteness,
so the diagram is a forest. Distinct connected components give orthogonal
invariant summands. Conversely an orthogonal invariant decomposition assigns
each reflection root to one summand, forcing the same block decomposition of
the graph. Transitivity on chambers identifies the wall reflections by
conjugation and makes the diagram independent of chamber choice.

Cyclically rotating a product `s₁...s_n` of involutions
conjugates it by s₁. Interchanging adjacent commuting factors leaves it
unchanged. For a tree, remove an end vertex and apply induction to the
remaining tree; cyclic moves and commuting moves allow the end vertex to be
placed in the required order. This checks the conjugacy argument for the
forest setting of the source, not a theorem that all Coxeter elements of every
arbitrary graph are conjugate.

A finite tree with at least two vertices has two leaves: choose a path of
maximal length; either endpoint with another adjacent edge would extend it
or create a cycle. The enumeration checks all labelled forests through five
vertices. In S_n, conjugating `(i,i+1)` by `(1...n)` produces adjacent
transpositions cyclically, and adjacent transpositions generate S_n by moving
the value at1 to1 and inducting. The program computes the resulting groups
for n=2,...,7 and obtains n! in every case. Humphreys1990 §3.16 is the later
comparator; the sheet's reuse does not identify its author.

## 13. Divisible modules over a PID

Claim46050. If M is injective, apply Hom(-,M) to the inclusion `(a)→R`:
the map sending a to m extends to R, giving `m=an`. Conversely, if M is
divisible, any map `(a)→M` extends by choosing n with `an` equal to the image
of a and sending1 to n. Every ideal is principal, so Baer's criterion
(StacksInjective, Lemma19.2.6) gives injectivity. Hence Hom(-,M) is exact in
the required contravariant sense. No computational experiment is needed.

## 14. p-adic cosets and Haar measure

Claims46052–46053. For n≥0, Z_p decomposes into p^n cosets of p^nZ_p.
Translation invariance and normalization μ(Z_p)=1 force μ(p^nZ_p)=p^(-n).
For arbitrary integer n the scaling relation gives the same formula.
Replacing p^n by p^(-n) in the subgroup being partitioned reverses inclusion;
this is the recorded reading alarm. Locally constant functions approximate
continuous functions uniformly on compact p-adic sets by uniform continuity
and a sufficiently fine finite clopen coset cover. The finite sums in the
manuscript are therefore Riemann sums for the normalized integral. The code
checks counts and measures, not the analytic uniform-continuity theorem.

## 15. Pro-groups

Claims46054–46056. A map from a finitely presented target through an affine
filtered inverse limit is determined at a finite stage; equality of two such
maps also descends after enlarging the stage. Applying this simultaneously
to multiplication, unit and inverse verifies the fully faithful finite-data
construction where the manuscript's lim-colim hypotheses apply.
Essential surjectivity of κ is a different assertion. The categories C,C′
and the essentially-affine condition cannot be recovered reliably enough to
turn its explicitly doubtful label into a theorem. Serre1960 perfects
commutative algebraic groups; Perrin1976 treats other exact approximation
categories. Their difference is mathematically substantive.

## 16. Relative effective Cartier divisors

Claim46061. Locally write the candidate ideal I⊂B. A generator of the fibre
ideal lifts to h∈I. Finite presentation and Nakayama give `I=(h)` after
shrinking, using flatness of B/I over the base to identify the fibre ideal.
The fibre nonzerodivisor and the local flatness criterion imply h is a
nonzerodivisor in B in the stated noetherian/finite-presentation setting.
The exact sequence `0→B --h→ B→B/h→0` remains exact after arbitrary base
change because B/h is base-flat. This is the exact qualified conclusion of
Stacks062Y/Stacks056P, Lemma31.19.9(2), not just its weaker part(1).

## 17. Matrix bundles and topological Brauer groups

Claims46062–46066. The natural map `A⊗A^op→End(A)`, `(a⊗b)(x)=axb`, is an
isomorphism for a matrix algebra, hence for an Azumaya algebra after local
trivialization. The program checks the full16-dimensional matrix map for M₂.
This gives the inverse class, and tensor product gives the group law.

The literal equivalence requiring the **same** stabilizer C on both sides,
`A⊗C≅B⊗C`, preserves degree. Over a point M₂ and M₃ have the same trivial
Brauer class, but no positive-dimensional C makes their dimensions equal.
The published relation in BrauerI1966 §1.2 uses independently chosen endomorphism
algebras. This is a mathematical correction, not a silent transcription edit.

The finite-CW realization theorem, the compact-space extension, and the
infinite-CW counterexample concern matrix-bundle Brauer groups and the
appropriate continuous-function coefficient sheaf. HornbostelSchroer2015
Theorem3.1 gives `Br(K(Z/n,2))=0`; its cohomological torsion class persists.
AntieauWilliams2014 gives period2 and index8 in dimension6, disproving a fixed
rank2 realization even in the finite-CW case. Those two obstructions answer
different manuscript questions.

## 18. Projective representations and multipliers

Claims46067–46068. If a d-dimensional projective representation has multiplier
c, taking determinants shows `c^d` is a coboundary. Thus any realizable class
has finite order dividing d. For π=Z² take the multiplier with commutator2.
Its representing matrices would satisfy `UV=2VU`. Their nonzero determinants
would imply `2^d=1`, impossible for d>0.

For a torsion counterexample let
`π=⊕_(i≥1)(C₂ e_i⊕C₂ f_i)`. With coordinates (a_i,b_i) of finite support,
set `c(x,y)=(-1)^(Σ b_i a′_i)`. Bilinearity proves the2-cocycle identity;
its values are ±1. On the first m pairs, the corresponding twisted group
algebra has generators E_i,F_i with squares1, anticommutation within a pair
and commutation across pairs. For one pair the Pauli matrices identify it
with M₂(C); tensoring gives M_(2^m)(C), dimension4^m. Every nonzero finite
module over it has dimension divisible by2^m. A finite-dimensional projective
representation of π would obey this for every m, impossible. The code verifies
the matrix relations for m≤4; tensor-product classification proves all m.

## 19. Restriction of scalars and inseparable norms

Claims46069–46073. The adjunction
`Hom_k(T,Res_(k′/k)G′)=Hom_k′(T×k k′,G′)` gives H⁰ immediately.
The smooth H¹ comparison uses torsors and étale-local sections; it cannot be
repeated unchanged for an infinitesimal group invisible to those sections.
The same distinction applies to the commutative higher-cohomology formulation.

For a purely inseparable extension of degree p, the determinant norm of x is
x^p. More generally the norm in a finite purely inseparable extension of
degree p^r is x^(p^r), including exponent-one extensions of larger degree.
The program computes the determinant of multiplication by
`a₀+a₁s+a₂s²`, `s³=A`, and reduces it modulo3 to
`a₀³+A a₁³+A²a₂³`. The kernel may be reduced over an imperfect base while
becoming nonreduced geometrically. Calling `k₀[[t]]` a field is a separate
reading alarm: the expected Laurent field is `k₀((t))`, and the scan must decide.

## 20. Hilbert90, averaging, and twisting

Claims46074–46075,46079–46080. A cocycle f defines the action
`γ⋆m=f_γ γ(m)`; expanding `(γδ)⋆m` gives the cocycle equation
`f_(γδ)=f_γ γ(f_δ)`. A change by u gives the usual conjugated cocycle and
the corresponding natural isomorphism. The averaging expression
`Σ f_γ γ(a)` satisfies the required intertwining equations by reindexing.
Over an infinite field, nonvanishing of the determinant polynomial permits
an invertible choice after the descent/spanning argument. Over a finite field,
the finite-dimensional algebra's unit group is a nonempty open in affine
space, hence geometrically connected and smooth; Lang supplies the missing
surjectivity. Finite-dimensionality is used here and later, regardless of a
deleted qualifier in a different theorem.

Naturality matters in the converse. For Γ=G=C₅ with trivial original action,
the homomorphisms sending a generator to1 and2 are distinct noncohomologous
cocycles, since G is abelian. Every G-set is a disjoint union of one-point and
free5-point orbits. The two induced actions are separately isomorphic on each
orbit (multiplication by2 conjugates the two5-cycles), hence on every G-set.
There is no natural isomorphism compatible with all G-set maps. The code
prints the free-orbit conjugator. This refutes only the non-natural reading.

## 21. Cyclic cohomology and the corrected twisted norm

Claims46076–46078. A cocycle of C_n is determined by a with
`N_T(a)=aT(a)...T^(n−1)(a)=1`; the formula for the value on the generator's
i-th power proves necessity and sufficiency. Changing the cocycle uses the
stated conjugation convention. Continuous cocycles into a discrete module
factor through finite data; finite cyclic quotients are indexed by divisibility,
not an unqualified linear order of integers.

Put `T_a=Int(a)∘T`. Direct expansion, preserving factor order, gives
`N_T(t a)=N_(T_a)(t) N_T(a)`. The program reduces both free-group words for
n=1,...,8. Generally the conjugating partial products cancel successively,
which proves the identity for all n by induction. If a lifts a quotient
cocycle, `N_T(a)` lies in G′ but need not be1. Thus t must lie in G′ and solve
`N_(T_a)(t)=N_T(a)⁻¹`. The right side and twisted kernel cannot be discarded.
The final unfinished quotient criterion remains a problem, not a proved corollary.

## 22. Semilocal descent, invariant rings, and Sylow detection

Claims46081–46086. For a direct counterexample to the theorem after finiteness
is deleted, take the semilocal noetherian ring O=C, Γ=C₂ acting faithfully by
complex conjugation, and A=C[t,t⁻¹] with `γ(t)=t⁻¹`. The action is semilinear,
the inertia kernel on the residue field C is trivial, and t is a cocycle since
`tγ(t)=1`. Every unit is `c t^m`, so every coboundary has exponent `−2m`.
The odd-exponent cocycle t is nontrivial. The target H¹ of trivial inertia is
a singleton. Every remaining hypothesis in the displayed broad theorem holds;
A is precisely not finite as an O-module.

The finite-module completion argument can instead be checked as a kernel of
a finite system of linear intertwining equations. Flat completion preserves
that kernel; an invertible solution modulo the radical lifts under the retained
finite/noetherian assumptions. This does not prove finiteness over invariants.

Here is a direct failure of invariant residue lifting. In characteristic p,
let `O=F_p(t)[ε]/ε²` and define
`σ(a+bε)=a+(b+D(a))ε`, `D=d/dt`. It is multiplicative by the Leibniz rule;
`σ^j=1+jεD`, hence σ has exact order p. Its action on O/(ε) is trivial.
An invariant lift of a exists iff D(a)=0, so the image of O^Γ in the residue
field is F_p(t^p), strictly smaller than F_p(t). O is local Artinian noetherian.

A variant disproves noetherianity of invariants for finite actions on
noetherian rings without invoking a publication. Let
`k=F_p(t₀,t₁,...)`, with algebraically independent variables, and let the
derivation satisfy `D(t_i)=t_(i+1)`. Then `ker D=k^p`. To verify this, write a
rational function using finitely many variables and expand over k^p in the
p-basis monomials. If n is the largest variable with nonzero derivative
coefficient, the term `t_(n+1) ∂f/∂t_n` cannot cancel with the remaining terms:
over `k^p(t₀,...,t_n)`, the element t_(n+1) has degree p and is not in that
field. Thus `∂f/∂t_n=0`; descend inductively. Conversely every pth power is
killed. On `O=k[ε]/ε²` use the same σ. Then
`O^Γ=k^p⊕kε`, with square-zero ideal kε. This ideal is infinite-dimensional
over k^p, since the p-basis is infinite, so O^Γ is not noetherian, although
O has length2 over k. GiokasSingh2024 gives a published regular-local
counterexample in dimension2 and traces earlier examples. The finite derivative
checks do not purport to prove this infinite p-basis argument.

For a nilpotent filtration the correct quotient is m^n/m^(n+1).
The groups `1+I` for I²=0 identify with the additive module I.
Restriction/corestriction then satisfies `cor res=[Γ:P]`; if the index is
invertible on the module, restriction is injective. This establishes the
additive step. Passing from a neutral-fibre statement to full nonabelian
injectivity uses twisting, so the necessary lifting/finite-module hypotheses
must survive those twists. The source does not verify that for its unrestricted
algebra version.

## 23. The quotient counterexample attempt

Claim46087. For the natural PGL_(N+1) action on P^N,
`dim Stab(x)=((N+1)²−1)−N=N²+N>0` for N≥1. Its free locus is empty.
Moreover P¹ has an ample bundle O(1) but is not affine, so ampleness alone
cannot yield affineness of a quotient. These are separate counterchecks of
the literal construction. They do not identify an uncertain subgroup symbol
or prove that every nearby intended quotient statement is false.

## 24. Components and images of group schemes

Claims46088–46095,46111. The diagonal of a group scheme is the inverse image
of its unit under `(g,h)↦g⁻¹h`; this checks the separation criterion. Over a
field the identity is a closed rational point, giving the known separatedness
result. The map `(g,h)↦(gh,h)` is an isomorphism, so multiplication is a
projection after an isomorphism; field-base projections are universally open.

The arbitrary group-scheme component theorem is checked in Stacks047J
Lemmas39.7.9–11; it is stronger than the locally finite-type SGA3VI_A statement.
One must not deduce it just from a finite-type proof. The literal revised
criterion that a specialization-stable subset is G⁰-invariant is false:
`W={0}⊂G_a` is closed and hence specialization-stable, but translation by1
moves it. Also `U×V` for punctured affine opens is not closed in A².
An intended product image UV is a different expression, so that example is
not used to refute UV. Translation transports fibrewise flatness, but a
universal-generizing conclusion and a closed-image theorem still need their
base-change and approximation hypotheses. The source's own yes-margin is
recorded with that precise proof obligation.

## 25. Geometric properties and missing qualifiers

Claims46096–46101,46106–46110. Geometric regularity/reducedness/irreducibility/
connectedness/integrality are compared with the appropriate field-extension
and product criteria in the corresponding Stacks sections; they are not
interchangeable. Over a perfect field reduced finite-type schemes have a
dense smooth open. The nonreduced scheme Spec k[ε]/ε² has no smooth point:
its local dimension is0 and tangent dimension1. Thus the abbreviated sentence
needs reducedness.

Over `k=F_p(a)` the equation `x^p−ay^p` is irreducible: viewing it over
k(y), a root would require a pth root of a. Its quotient is therefore a
domain. The equation is additive under the group law, defining a reduced
finite-type subgroup of G_a². Over k(b), b^p=a, it becomes `(x−by)^p`, with a
nonzero nilpotent. This verifies every hypothesis of the imperfect-field
counterexample.

The real cone `x²+y²=0` is integral over R but has two components over C,
meeting at its rational origin. A rational point is insufficient for geometric
irreducibility; the unique-geometric-component condition matters. The further
literal omission of ambient irreducibility is refuted by `X=A¹⊔A¹` and a
rational point Z in one component. For connectedness product tests, even
`X=Spec k` fails the condition with every Y: take Y the disjoint union of two
points. The required tests are nonempty connected Y. The reversed arrow in
the separable-extension list is checked with `Spec C→Spec R`.

In a purely inseparable degree-p extension k′/k, the difference
`a^(1/p)⊗1−1⊗a^(1/p)` is nonzero in `k′⊗k k′` but its pth power is zero.
This is the reduced-product obstruction. In contrast the separable test
`C⊗R C≅C×C` gives disconnected geometric factors. All displayed polynomial
factorizations are recomputed exactly.

## 26. Étale dictionaries and the component-space boundary

Claims46102–46105,46112. Finite étale k-schemes correspond contravariantly to
finite étale k-algebras and covariantly to finite continuous Galois sets.
For a non-Galois cubic extension, geometric points are its three embeddings,
a transitive coset set, not a quotient group by a normal subgroup. Affine
inverse limits of finite étale schemes give the profinite version.

A qcqs scheme has spectral underlying space, whose component space is
profinite by Stacks0906. The component algebra construction and continuity
must use that topology and the corresponding base-change argument. The
initially proposed tag0BQA was opened and found to concern topological
invariance of fundamental groups; it is **not** used as evidence for this
component quotient. The exact quasi-compact-only statement is kept separate
from the qcqs theorem. General pro-étale morphisms and arbitrary totally
disconnected spaces are not substituted for affine profinite objects.

## 27. Characters and finite Cartier duality

Claims46113–46116. For a finite locally free commutative Hopf algebra A, dual
bases identify `(A⊗A)^∨≅A^∨⊗A^∨`, so multiplication and comultiplication
transpose, as do unit, counit and antipode. Double duality gives back A.
The dual of μ_n is the constant Z/n group; the dual of a finite constant
abelian group is its diagonalizable group. For α_p, dual basis multiplication
is `e_i e_j=binom(i+j,i)e_(i+j)` below degree p and zero above it. Since
i! is invertible for i<p, rescaling identifies this with k[t]/t^p.
The code checks the binomial coefficient rescaling for four primes.

The broad Hom(G,G_m) sentence contains incompatible negation and G_m example
readings. The clear finite-flat theorem does not decide that sentence's ink.

## 28. Monoids, GL_n, and the cancellative side remark

Claims46117–46120. The two-element monoid `{1,0}` with0 absorbing is associative
and unital, but0 has no inverse. If embedded into any group, its idempotent0
would equal the group unit, contradicting injectivity. Its coordinate bialgebra
is `k[t]/(t²−t)`, `Δt=t⊗t`, `ε(t)=1`. An antipode would imply `tS(t)=1`,
which becomes0=1 on evaluating at the absorbing point. This is the explicit
letter's counterexample. The reply's M_n correction and scan31 coefficient
proof are actual within-source repairs.

Over a field, finite-type algebraic monoids embed in matrix monoids by finite
coefficient spaces. For cancellative algebraic monoids the unit/idempotent
theory yields a group under the exact field hypotheses of Brion2014.
The side remark over an arbitrary base ring and with only left-translation
monomorphisms is not declared proved by that field theorem. No counterexample
has been supplied for that exact generality; its searched state remains C.

## 29. The full distribution functor and Hopf identities

Claims46121–46125,46135. Here `Dist(Spec A)(R)=Hom_k(A,R)` is the full module
functor represented by Spec Sym A. It is not just distributions supported at
the identity. A map of affine schemes reverses coordinate algebras and hence
gives the stated covariant map of distribution functors. The box tensor is
defined by its bilinear universal property; it must not be replaced by a
tensor product of unrestricted algebraic duals.

Points correspond to unital multiplicative linear functionals. The equation
`Δx=x⊠x` alone includes zero; the counit condition excludes it. Multiplication
of the monoid gives convolution; inversion gives the two antipode identities.
For a finite constant C₃, the dual function algebra has group-algebra basis
`e_i e_j=e_(i+j)`. For a diagonalizable infinite group the full dual is a
product of coefficient modules, requiring the stated topology/functor setting.
Lie derivations are primitive and their commutator and pth composition give
the corresponding operations. Matrix inversion is recomputed as
adjugate/determinant, verifying both antipode equations.

## 30. Actions, coactions, submodules, and intersections

Claims46124–46131. Writing `ρ(m)=Σm_i⊗a_i`, an R-point g acts by
`m↦Σm_i g(a_i)`. Composing g and h and expanding twice gives
`(ρ⊗id)ρ=(id⊗Δ)ρ`; the identity element gives `(id⊗ε)ρ=id`.
This checks the question-mark calculation in the supplied continuation.
Finite-projective dual bases transpose a coaction to an A^∨-module action.
For a split filtered union use the continuous dual: a continuous functional
depends on a finite coefficient stage. The ordinary unrestricted algebraic
double dual is not substituted.

A quotient map q:M→Q is surjective, so any induced coaction is unique and
exists exactly when `(q⊗id)ρ` kills ker q. Right exactness supplies the quotient
tensor map; coassociativity and counit descend by the surjections. For a
submodule i:N→M, uniqueness instead requires `i⊗A` injective, and transferring
coassociativity uses `i⊗A⊗A` injective. Flatness of A, or suitable purity,
is a sufficient condition. Tensoring `2Z→Z` with Z/2 illustrates why an
arbitrary inclusion cannot be cancelled after tensoring.

Flat tensoring preserves finite intersections by the kernel description of
`N∩P→N⊕P→M`. It does not generally preserve arbitrary intersections:
`∩_n n!Z=0`, whereas each `(n!Z)⊗Q` has image Q in Q. This is an exact
module-theoretic boundary, **not a coalgebra counterexample**. For a coalgebra
whose underlying module is a direct sum of finite projectives, coefficient
functionals detect membership in `N⊗A`; a submodule is stable iff stable
under A^∨. Arbitrary intersections then are stable. The revised flat-only
coalgebra claim is left for the precise theorem/counterexample search.

## 31. Finite coefficient spaces and affine approximation

Claims46132–46134. For a finite set of comodule elements, write their coactions
using a finite coefficient block of the locally projective/direct-sum
coalgebra. Applying dual coordinate functionals and coassociativity shows
that the span of the finitely many resulting coefficients is stable. Over a
field this is the fundamental finite-subcomodule theorem. Apply left and right
coactions to obtain a finite bicomodule coefficient space in the coalgebra;
the tensor-intersection criterion gives a finite-dimensional subcoalgebra.
Every element lies in one, so the coalgebra is their filtered union.

For a finite-type affine monoid, choose algebra generators in such a finite
stable coefficient space. Matrix coefficients generate the coordinate algebra,
so the associated map to M_n is a closed immersion. For a group include
the antipode constraints and obtain GL_n. An arbitrary affine Hopf algebra is
the filtered union of its finitely generated Hopf subalgebras, by closing the
finite coefficient construction under the antipode; dually the affine group
is an inverse limit of finite-type groups. The field hypothesis is retained.
Perrin's nonaffine approximation is a separate stronger theorem.

## 32. V(M), W(M), and endomorphism functors

Claims46136–46138. The symmetric-algebra adjunction gives
`Hom_alg(Sym M,B)=Hom_R(M,B)` for every M, hence
`V(M)=Spec Sym M`. If M is finite projective, dual bases give
`M⊗B≅Hom_R(M^∨,B)`, so W(M) is the vector scheme V(M^∨).
ModuleSchemes2009 Theorem1.1 proves the converse for module schemes. The
following reconstruction in this run proves the stronger assertion with
arbitrary scheme representability, without assuming affineness.

Suppose an R-scheme X represents B↦M⊗_R B on commutative R-algebras.
The zero element gives a section e:Spec R→X. Put Q=e*Ω_(X/R).
For every R-module L form the square-zero R-algebra R⊕L, with multiplication
(r,l)(s,m)=(rs,rm+sl). Consider maps Spec(R⊕L)→X whose restriction along
Spec R→Spec(R⊕L) is e. There is a canonical base lift, the composite of the
projection Spec(R⊕L)→Spec R with e. The difference between any lift and this
base lift is an R-derivation along e. The universal property of differentials
therefore identifies this set of lifts with Hom_R(Q,L).

This description works for every scheme X: the nilpotent thickening has
exactly the topological space of Spec R. On the inverse images of affine
neighbourhoods in X, two ring maps with the same reduction differ by a
derivation into the square-zero ideal. Conversely, adding such a derivation
to the base lift gives a ring map, because products of ideal elements vanish.
The construction is unique on overlaps and glues. This is precisely the
general scheme assertion of Stacks04BU, Lemmas37.9.1–2 and37.9.5, applied
with source Spec R⊂Spec(R⊕L) and target X=X (the zero thickening).

The representing functor identifies the same lift set with the fibre over
0 of M⊗(R⊕L)→M⊗R, namely M⊗L. These identifications are natural for all
R-module maps L→L'. They are R-linear: direct-sum projections identify the
value at L⊕L with two copies of the value at L; naturality for the fold map
gives addition, and naturality for multiplication by r∈R gives scalar
multiplication. Thus there is a natural isomorphism of module-valued functors

    M⊗_R(−) ≅ Hom_R(Q,−).

Tensoring preserves filtered colimits. Hence Hom_R(Q,−) does, and Q is
finitely presented by Stacks0G8P, Lemma10.11.4. Tensoring also takes
surjections to surjections, so Hom_R(Q,−) does; Q is projective by the
lifting definition of projectivity. Evaluating at L=R gives M≅Q∨.
Therefore M is finite projective. Conversely the dual-basis construction
above represents W(M) by the affine scheme Spec Sym(M∨). Affineness follows
after the finite-projectivity conclusion, by uniqueness of representing
schemes; it is not an input to the proof.

This is an independent reconstruction in this run. The 2009 paper directly
states only the module-scheme version; the square-zero argument establishes
the stronger exact manuscript scope using the two opened general lemmas.
Functorial linear biduality here is not the assertion `M=M**` for every
ordinary module.

For finite projective M, `End(M)=M^∨⊗M`. Local trivializations identify its
endomorphism scheme with matrices; the invertible locus is `det≠0`, compatible
with change of basis, giving Aut(M). The symbolic2×2 inverse in the executable
checks verifies the local formula. The universal symmetric-algebra and dual
basis arguments, not the2×2 example, establish the general statement.
