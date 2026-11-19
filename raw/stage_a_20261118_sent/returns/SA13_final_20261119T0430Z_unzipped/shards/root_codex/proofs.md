# Proof and computation audit: K34-09–12

These are this run’s mathematical checks, distinct from manuscript proof status.
The manuscript passages were read in full. Bibliographical matches are recorded
separately in `reference_audit.json`. An invocation of a published purity,
Lefschetz, deformation, Tannakian or Lie-integration theorem below is an input,
not an independent re-proof of that theorem. Computation output is in
`outputs/root_codex_computations.json`.

## localization

The degree convention is fixed by the source itself, K34-05:094 and
K34-08:145: its Φ is the usual vanishing-cycle complex shifted by −1. Thus
H^i(Φ_manuscript)=H^{i−1}(RΦ_usual). If the latter has its sole cohomology
in degree n, the former has it in n+1. This is an observed convention, not an
ink correction. A localization triangle A→B→C gives the exact sequence
H^{i−1}C→H^iA→H^iB→H^iC. Vanishing of both outer groups proves the
specialization isomorphism. At the first or last nonzero degree only the
corresponding injection/surjection follows. This checks C600–606’s index use.

The induction in5.1 needs vanishing at every strict generization, so that the
restriction to the punctured strict local fibre vanishes in the range used.
Vanishing at x alone says nothing about that restriction. The exact filtered
colimit comparison for the neighborhoods X(h) is the source’s geometric input;
after that comparison the étale-depth bound gives the local cohomology
vanishing by definition. We checked this logical implication and the published
SGA7 I4.5 proof(1), not a new general base-change theorem.

## amplitudes

Let F be a bounded constructible complex supported on a d-dimensional
finite-type variety over a separably closed field, with invertible torsion
coefficients, and suppose its cohomology sheaves lie in [a,b]. The support
cohomological-dimension bound gives hypercohomology in [a,b+2d]. In the source
a=n−d+1,b=n+1 would by that bound alone give [n−d+1,n+2d+1]. The stronger
displayed [n−d+1,n+d+1] therefore needs the *pointwise rectified-depth upper
bound* b_x=n+1−dim closure{x}, or the perverse-support formulation; it is
not justified merely by a global sheaf interval and a support dimension.
This distinction is retained in C605’s audit. In the modern flat lci setting,
Illusie2003 establishes perversity, which supplies the stronger support
control. We do not infer it from a coarser two-line spectral sequence.

For an isolated point d=0 this ambiguity disappears: the shifted cycle
complex is concentrated in n+1 and has no higher support cohomology. The
finite enumeration checks the shift and the endpoints for n≤10,d≤n; the
symbolic support argument, not that enumeration, handles arbitrary dimensions.

## nearby-cones

For an open immersion j:U→X with complementary closed immersion i:Z→X,
the triangles i_*i!K→K→Rj_*j*K and j_!j*K→K→i_*i*K are different triangles.
They cannot be interchanged by replacing ! by *. For a regular codimension-c
immersion and invertible torsion coefficients, purity identifies i!Λ with
Λ(−c)[−2c]. Once this input is fixed, the degrees in the punctured-space
sequence follow formally. For a strict regular local scheme of dimension n,
acyclicity of the strict local total space and purity at the closed point
give reduced punctured cohomology only in degree2n−1, equal toΛ(−n).
Replacing n by n+1 gives degree2n+1 and twist−n−1.

For a two-term complex Cone(f)^k=B^k⊕A^{k+1}, choose differential
d(b,a)=(d_Bb+f(a),−d_Aa). The cone triangle has a fixed connecting map with
this convention. The formal localization/nearby-cycle comparison in6.4 can
be organized with that choice. It does not decide whether the writer’s β
used that choice: the page says “signe?” and “à des signes et shifts près”.
Part(b) is deferred on160. This audit verifies which shifts purity requires
and which exact triangles must be compared; it does not claim a handwritten
sign was proved or read.

## inertia-cohomology

Let ℓ≠p. Wild inertia is pro-p, so invariants on ℓ-primary discrete torsion
modules are exact, by averaging on finite quotients. For the ℓ-part of tame
inertia, a generator T gives the two-term complex [M --T−1→ M]. Hence H⁰
is ker(T−1), H¹ is coker(T−1), and higher cohomology vanishes. Equivariantly,
the generator is an element of Z_ℓ(1), so the degree-one term carries the
dual twist: H¹(I,M)=M_I(−1) after the prime-to-ℓ factors have been removed.
For trivial M this is M(−1). The underlying module can be written without
the twist only after a choice of generator, and that choice need not commute
with residue Frobenius.

The Hochschild–Serre spectral sequence has only columns0 and1 and therefore
gives 0→H^{i−1}(V_barη)_I(−1)→H^i(V_η)→H^i(V_barη)^I→0. If geometric
cohomology vanishes above n, arithmetic generic cohomology vanishes above
n+1. This is the complete index calculation on161, separate from the
geometric affine-vanishing theorem used as an input.

## prime-to-p

At the finite-group level, quotienting by the normal subgroup generated by
all p-Sylows kills every p-element; the quotient has order prime to p.
Every homomorphism to a prime-to-p group kills the Sylows, proving the
universal property. The same statement at every finite quotient gives the
closed-normal-subgroup description for a profinite group.

If a pro-p group maps continuously into a pro-prime-to-p group, its image is
both and is trivial. Thus, in Aut(π)→Out(π) for pro-prime-to-p π, vanishing
of a wild action in Out forces vanishing in Aut, because the remaining image
lies in Inn(π). This proves the “equivalently” in the wild-monodromy theorem.
The geometric arithmetic-π1 exact sequence itself requires geometric
connectedness. A rational point defines a section only after its induced
geometric base point is chosen; otherwise one has conjugacy ambiguity.

For finitely generated profinite π, there are finitely many open subgroups
of any fixed index. Their characteristic intersections form a cofinal
system. Aut(π) is a closed subgroup of the inverse limit of automorphism
groups of these finite characteristic quotients, hence profinite. This proof
does not establish the unqualified claim for arbitrary profinite π.

## fixed-paths

A finite p-group acting on a finite set whose cardinality is prime to p has
a fixed point: nontrivial orbits have cardinality divisible by p, so the
number of fixed points is congruent to the cardinality of the set modulo p.
For a pro-p group acting on a finite set the action factors through a finite
p-group. For the inverse limit of finite prime-to-p torsors, each finite
system of fixed-point conditions is realized at a common refinement, and
the corresponding closed subsets in the compact inverse limit have the
finite intersection property. Therefore a fixed path exists. This supplies
the compatibility step, not just separate fixed points at each level.

The assertion fails for all inertia: an ℓ-primary tame quotient may act by
translation on an ℓ-element torsor with no fixed point. The small cyclic
permutation checks in the program illustrate precisely that distinction.

## kummer

For m invertible and t a unit, A[T]/(T^m−t) is finite free, and mT^{m−1}
is a unit in the quotient. It is therefore étale. In contrast, A[T]/(T^m)
for m>1 has a nonzero nilpotent and its differential module has the relation
mT^{m−1}dT=0, not dT=0. Thus the missing −t_i on180 changes the theorem.

At a strict normal-crossing point with r divisor branches, the complement
has r independent prime-to-p Kummer parameters. Its local R^qj_* is the
q-th exterior power, with rank binomial(r,q) and twist−q. In a semistable
family the geometric nearby fibre imposes the diagonal relation from the
base parameter, leaving rank r−1 in degree1 and binomial(r−1,q) in degree q.
The program verifies these exterior ranks separately; conflating them would
lose one monodromy direction.

If a universal node parameter t_i pulls back to u_iπ^{n_i} on a trait, its
Kummer character on tame inertia is n_i times that of π; units have trivial
geometric tame valuation character in the strict local setting. Commuting
node monodromies thus pull back to ∏h_i^{n_i}. For a DVR,
length(V/(u_iπ^{n_i}))=n_i. This redoes the computation in3.2.1; stable
deformation and Abhyankar’s lemma remain cited geometric inputs.

## analytic-envelopes

A continuous image of a compact group in GL_n(Q_ℓ) is compact and closed,
hence analytic by the closed-subgroup theorem. For two quotient maps, the
joint image in the product is compact analytic and has kernel the
intersection, giving the cofiltered analytic-image system. Finite-image
representations differentiate to zero. Two distinct finite characters
therefore exhibit the failure of fullness of differentiation, though the
underlying linear maps make it faithful.

Local integration uses the exponential and BCH convergence on sufficiently
small lattices. A linear map intertwining differentiated actions intertwines
the exponentials on a small open subgroup, which proves fullness after taking
the colimit over opens. A finite-dimensional Lie representation integrates
there, proving essential surjectivity. We use this classical convergence
theorem; we do not claim the finite program proves p-adic convergence.

For compact linearity, choose a small open subgroup U on which an Ado
representation integrates faithfully. Compactness makes [G:U] finite.
Ind_U^G(V) has finite dimension [G:U]dim V. Its kernel lies in the kernel
of V upon restriction to the distinguished U-coset, and an element acting
trivially must also preserve that coset, hence belong to U. The kernel is
therefore trivial. This supplies the missing “réf?” mechanism.

If H⊂G(Q_ℓ) is a closed analytic subgroup, Lie(H)=Lie(G) implies that the
inclusion is locally an analytic isomorphism at1, hence H is open near1.
Conversely an open subgroup has the same Lie algebra. Applied to the
Zariski closure of each image, this proves the finite-dimensional openness
criterion. Algebraicity of perfect linear Lie algebras is a classical input,
not independently reproved here. A central isogeny of semisimple groups is
locally invertible in characteristic zero; restricting to a small compact
open subgroup lifts it, which explains the discarded remark6.7.

## tannakian

The category of continuous finite-dimensional Q_ℓ-representations is rigid,
abelian, Q_ℓ-linear and has the exact faithful forgetful tensor functor.
Deligne–Milne2.11 therefore applies. Concretely, a finite collection of
representations is dominated by its direct sum; tensor operations and
subquotients ensure that the resulting Zariski closures have the correct
representation category. We check these hypotheses, rather than re-prove
Tannaka duality.

For every finite quotient π→F, its regular representation is faithful and
continuous, so F appears as a constant algebraic quotient of πalg.
Conversely, for each Zariski-dense image π→G(Q_ℓ), its map into G/G⁰ is
surjective and continuous with finite image. Surjectivity follows because a
missed component is open and closed in G and contradicts density. Therefore
the inverse system of component quotients is precisely the finite-quotient
system of π. This proves πalg/(πalg)⁰=π and explains the conflict with an
unqualified reading of6.5.

For a connected algebraic group in characteristic zero, a vector killed by
the Lie action is fixed by the group: its stabilizer is a closed subgroup
with full Lie algebra, hence has the same dimension, and connectedness makes
it the whole group. Apply this to Hom(V,W) to get full faithfulness of
differentiation. Algebraization of arbitrary Lie modules fails already for
G_m, whose algebraic characters have integral weights although its
one-dimensional Lie algebra admits any scalar weight.

Finite-index restriction makes image closures have the same identity
component. Surjectivity of image maps therefore gives surjectivity on
connected algebraic quotients and Lie algebras. These arguments prove the
specific functoriality used on191; they do not identify full analytic groups
with all rational points of their algebraic envelopes.

## rational-components

Let k=Q₃ and L=k(√3), a ramified quadratic extension. Embed the norm-one
torus T into SL₂(k) using multiplication on the two-dimensional vector space
L. Its normalizer Γ has Γ/T equal to the constant group C₂: the nonidentity
component acts on T by the nontrivial field automorphism. Over an algebraic
closure this is the usual torus normalizer in SL₂, so Γ⁰=T.

An element of the other component, if rational, has form m_a∘c, where m_a
is multiplication by a∈L× and c is conjugation. Its determinant is −N(a).
Membership in SL₂(k) requires N(a)=−1. Since the norm has valuation zero,
a is a unit of O_L. The residue fields are both F₃; the residue norm of a
unit is its square, so it is1, while −1 has residue2. This is impossible.
Thus Γ(k)=T(k), not Zariski dense in Γ, although every point of Γ/Γ⁰ is
k-rational. Every hypothesis of the literal general assertion on187 is
satisfied. For the particular G_E of the manuscript, density follows instead
from the definition as a Zariski closure; that application is unaffected.
The program checks the residue obstruction and determinant symbolically.

## pro-objects

For Π_n=Z/ℓ^n with reduction maps, limΠ_n=Z_ℓ. All finite groups have zero
Lie algebra, but Z_ℓ has Lie algebra Q_ℓ. For Π_n=ℓ^nZ_ℓ with inclusions,
the inverse limit is the intersection0, whereas every differentiated map is
an isomorphism of one-dimensional Q_ℓ-spaces. Both counterexamples include
their transition maps. There is no assertion here that a finite enumeration
computes an infinite inverse limit.

Finite-presentation descent over an affine qcqs inverse system follows from
finitely many equations and relations and their equality at some finite
stage. The general gluing statement is Stacks01ZM; finiteness and étaleness
descend by01ZO and07RP. This proves the finite-étale category statement and
the π1 limit. An infinite compatible family of ℓ-power-level data need not
descend at one common stage. Consequently the arithmetic model category is
explicitly the colimit of local-system categories, not all local systems on
the limit scheme.

For a dominant finite-type morphism Y→X of normal integral schemes, the
relative algebraic closure of k(X) in k(Y) is finite. After normalizing in
that extension and restricting to a suitable dense open, geometric generic
connectedness gives the required finite-index image on π1. Normality makes
restriction to the generic point surjective on π1; compare Stacks0BQI.
This verifies the finite-index step used in6.14. Extension of an abelian
scheme homomorphism from the generic point is a separate normal-base theorem,
checked in Gajda–Petersen Lemma3.4.

## arithmetic-dimensions

Take X=Spec(F̄_p), ℓ≠p. This is nonempty, normal and integral, and ℓ is a
unit. Every finite-type F_p-subalgebra of F̄_p is a finite field, so the
finite fields are cofinal arithmetic models. Their fundamental groups are
Zhat, with transition maps corresponding to finite-index inclusions. Every
compact Q_ℓ-analytic image of Zhat is topologically procyclic and has Lie
dimension at most1: its sufficiently small uniform pro-ℓ subgroup is a
procyclic torsion-free pro-ℓ group, hence either trivial or Z_ℓ. Projection
onto Z_ℓ realizes dimension1. Finite-index transitions differentiate to
multiplication by a nonzero integer, which is invertible over Q_ℓ. Thus
Lie^anΠ is the constant one-dimensional pro-Lie algebra. This refutes
“both dimensions always infinite” with every standing hypothesis checked.

For each m choose r₁,…,r_m∈ℓ²Z_ℓ linearly independent over Q. Such choices
exist since Q_ℓ has infinite dimension over Q. The analytic characters
x↦exp(r_ix) define Z_ℓ→G_m^m(Q_ℓ). If its Zariski closure were a proper
algebraic subgroup of the torus, a nonzero integral character would be
trivial on its connected component, so after multiplying its exponents it
would be trivial on the whole image. Taking the convergent logarithm gives
Σn_i r_i=0, contrary to independence. Hence the closure has dimension m.
Restriction to a finite-index subgroup multiplies every r_i by a nonzero
integer and does not change this conclusion. The algebraic pro-envelope is
therefore unbounded-dimensional while the analytic Lie algebra is one
dimensional. No finite numerical test substitutes for Q-linear independence.

The cyclotomic tower Q(μ_{ℓ^n}) is unramified outside ℓ and gives the required
quotient of π1(Spec Z[1/ℓ]). Kronecker–Weber plus its conductor refinement
identifies the maximal abelian quotient as Z_ℓ×. Existence of the quotient
already suffices for the source’s nonzero-Lie argument. The repeated “p>0”
labels are kept as a reading alarm.

## tate-centralizers

Commutation with a fixed endomorphism is cut out by polynomial equations
gA−Ag=0. It holds on a subgroup iff it holds on its Zariski closure.
For a connected algebraic closure it is equivalent to commutation with its
Lie algebra, by the stabilizer argument above. A finite component quotient
can persist at an early arithmetic model even if ordinary π1 of the limit
is trivial. It is killed at some finer model by finite-étale descent; only
then may the connected centralizer formula be used.

For an abelian scheme A at a normal finite-type model X_λ, Gajda–Petersen
Theorem2.3 identifies Tate-module homomorphisms over its finitely generated
function field with Hom⊗Z_ℓ, and Lemma3.4 extends the homomorphisms over
the normal base. Abelian schemes and any particular morphism descend by
finite presentation. Passing to the filtered model category proves the
displayed End⊗Q_ℓ assertion. This uses the established Tate theorem as an
input, not a new proof of Faltings or Zarhin/Mori. Substituting ordinary
π1(Spec kbar)=1 would replace an arithmetic centralizer by all matrices and
destroy the statement.

## weights

If a Frobenius module is pure of weight w, subquotients have the same weight.
There is no nonzero equivariant map between pure modules with distinct
weights, because the absolute values of all eigenvalues differ. This needs
no semisimplicity. On the Čech E2 page, source weight q and target weight
q−r+1 differ for r≥2. Hence the sequence degenerates at E2.

For the open-complement Leray sequence, source weight p+2q and target
(p+r)+2(q−r+1)=p+2q+2−r agree exactly for r=2. For local cohomology the
weight formula p+2q−2 has the same difference2−r. Therefore d2 may survive
and the terminal page is E3. In the trait case q=0 has weights≤p; a
differential from q≥1 to q′=0 has r=q+1 and target weights≤p+q+1. For
q≥2 this is less than source weight p+2q, so it vanishes. The only possible
case q=1,r=2 is again d2. No d_r for r≥3 survives, including that boundary
row. The program checks this arithmetic for a grid; the displayed identities
prove it for all p,q,r.

In the localization sequence for U=Xbar−Y, H^i(Xbar) is pure of weight i,
H^i(Y) has weights≤i, and Hc^i(U) has weights≤i. The kernel of Hc^i→H^iXbar
is the image of H^{i−1}Y and has weights≤i−1; its quotient has weight i.
Thus it equals W_{i−1}. Exactness identifies kerφ^i with Gr_iHc^i and
cokerφ^i with W_iHc^{i+1}. The image of φ^i cannot intersect the lower
weight filtration of H^iY. These calculations prove compactification
independence of these identified subquotients, not a canonical splitting.

No weight argument here proves that the rank of every differential is
independent of ℓ. That is a separate assertion about realization of
algebraic maps, explicitly conditional on standard conjectures on the page.

The trait calculation is made after strict henselization. Its geometric
special-fibre terms abut to H^i(X_Knr), where Knr is the maximal unramified
extension; writing H^i(X_K) would add residue-field Galois cohomology.
Hochschild–Serre gives
0 → H^(i−1)(X_Kbar)_I(−1) → H^i(X_Knr) → H^i(X_Kbar)^I → 0.
The twist follows from Hom(Z_ell(1),Q_ell)=Q_ell(−1) even for the trivial
representation. See the independent, fully sourced derivation in
`shards/p2/weights_audit.md`.

For G_m inside P¹, d2 on the two boundary classes is the sum
Q_ell(−1)² → Q_ell(−1). It has rank1, proving that E2 cannot replace E3
in this Leray indexing. The duality exponent on scan205 is consistent
with dim X′=n−1; no opposite dimension convention is silently imposed.
Van Dobben de Bruyn2020 Theorem1 proves the precise equivalence of the
general rank and compact-support Betti-independence conjectures, without
proving their premise. This is the established conditional reduction.

## tate-weights

Let K be a p-adic local field with residue field F_q and E/K a split Tate
elliptic curve with parameter of positive valuation, and let ℓ≠p. Its
cohomology V=H¹(E_Kbar,Q_ℓ) has a basis e₀,e₂ in which nontrivial tame
inertia acts by T=1+tN, N(e₂)=e₀,N(e₀)=0. Geometric Frobenius has
eigenvalues1 and q on the semisimplification; choosing the unramified
splitting for this calculation gives F=diag(1,q). Then
FNF^{-1}=q^{-1}N, as the tame relation requires. Invariants are kerN=Q_ℓe₀
of weight0; coinvariants are V/NV=Q_ℓe₂ of weight2. Both have dimension1
and neither is pure of weight i=1. This is a smooth proper geometrically
connected genus-one generic fibre, so it satisfies the intended geometric
cohomology hypothesis. Its semistable reduction supplies the normal-crossing
context after the usual regular model.

The monodromy filtration instead has graded weights0 and2 centered at1;
that is compatible with weight–monodromy. The counterexample refutes the
literal invariant/coinvariant purity claim, not weight–monodromy. The
program checks N²=0, the relation, kernel/image dimensions and eigenvalues
for several q. The Tate-curve representation is the geometric input.

## git-weights

For a G-linearized line bundle, the λ-character on the limiting fibre adds
under tensor product, changes sign under duality, and pulls back along
equivariant maps. This proves additivity in Pic^G and pullback compatibility.
If x has a λ-limit, the same limiting fibre computes μ for x and its limit.

In projective coordinates with λ-weights r_i and μ=−min{r_i:x_i≠0}, a
regular nonzero lift along the valuative witness forces r_i≥0 for every
surviving coordinate. If it specializes to0 all those inequalities become
strict. Thus μ≤0 or μ<0. The trivial one-parameter subgroup has all r_i=0,
so it must be excluded in a strict-positive stability test. The finite
program checks additivity, scaling and these sign examples; it does not
prove the Iwahori decomposition, invariant-theory separation or the full
Hilbert–Mumford theorem. Those are the reused printed GIT source’s inputs.
