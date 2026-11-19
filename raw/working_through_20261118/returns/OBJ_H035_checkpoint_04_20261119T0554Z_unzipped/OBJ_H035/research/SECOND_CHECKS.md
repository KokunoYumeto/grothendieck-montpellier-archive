# Second mathematical checks

These are second checks in the requested single stream, by GPT-6 Astra Pro
(effort setting not exposed), after the proof drafts. They are not a second
reader's endorsement, a formal proof certificate, or a claim that the supplied
notes were correct. Each paragraph states what was recalculated from the
hypotheses. Dates and event types are also recorded in CHECK_EVENTS.tsv.

## H035.1–H035.6 — checked 2026-11-19, 04:05–04:17 UTC

**H035.1.** Independently compute an augmented map to A⊕M as e+d:
the multiplication identity is precisely the derivation identity, and the
restriction to I kills I². Conversely C=A⊕I supplies the unique derivation.
Products of r elements of I generate I^r, so the symmetric-algebra map is
surjective. The fibre-product obstruction is real: (1,1) and (1,−1) are
distinct modulo a common sign, although both coordinates agree modulo signs.
This checks the explicit affine realization and the warning about unrestricted
functors; it does not turn an unspecified title-sheet programme into a theorem.

**H035.2.** Reconstruct scalar multiplication and addition from their module
maps. The interchange diagrams involve finite products; their images give an
A-module, and the diagonal/codiagonal formula proves additivity on morphisms.
Localization is the explicit filtered system of multiplication maps. General
flat base change uses Lazard, not an unsupported assertion that every flat
algebra is a union of finite free subalgebras: only its underlying module is
a filtered colimit of finite free modules. The module comparison is canonical.

**H035.3.** Rechecked the descent datum by evaluating the two scalar extensions
on the same B⊗B-modules. Yoneda gives the cocycle. Effective module descent is
the opened Stacks Proposition 35.3.9 (023N); applying left exact F to the
faithfully flat equalizer recovers F on every A-module. A finite generating
set after base change uses finitely many elements before base change; faithful
flatness kills the quotient. Applying this to the kernel of a finite free
presentation proves finite-presentation descent. Corrected “exactness of Hom”
to “left exactness”; full exactness is not being assumed.

**H035.4.** Recomputed the compatible-presentation argument without assuming
that kernels commute with reduction. The finite generators of P₁ lift, and
the kernel transitions are surjective after correction by f^n A^(r). If K is
the limiting kernel, its image is the kernel at each level. This gives
P_n=Ahat^r/(K+f^n Ahat^r)=P/f^nP. It does NOT give K_n=K/f^nK.
The two components Ahat and A_f cover all primes, so their product is faithfully
flat. Finite modules over Ahat, including nonalgebraizable ones, are the actual
test modules in the argument. No localization/completion commutation is used.

**H035.5.** The induction is on ideals, using their ascending chain condition,
not on dimension. A nonnilpotent f has (f^n)≠0 for every n, so all quotients
needed by Lemma 2 are strictly larger ideals. A unit causes no difficulty.
For the zero quotient, even F=0 cannot provide a nonnilpotent element; this is
an actual boundary defect in the literal clause, not a proof of a false
nonzero-ring statement.

**H035.6.** On an artinian local ring, independently test the proposed P on
the injective cogenerator E: P=D(F(E)), so Hom(P,E)=F(E). End(E)=A makes the
identification compatible with every matrix between finite sums of E.
Two-step injective copresentations and left exactness extend it to all finite
modules. Thus no exactness of F beyond left exactness is used. The only
finite-value test objects required before completion are the finite E_n;
one does not assume finite values on arbitrary finite completed modules.

## H035.7–H035.15 — checked 2026-11-19, 04:13–04:17 UTC

**H035.7.** A finite-length A_p-module is killed by a power of pA_p and is
already complete. This is precisely the local finite-value input to H035.6.
The representing module at a generization is its scalar extension, by
Yoneda; this compatibility is needed, and is available, in the support proof.

**H035.8.** Rechecked the delicate spreading step. Extend the coherent support
on U to a finite submodule inside M, and spread generators for N(p). In a
punctured neighbourhood of p they agree stalkwise by generization compatibility.
If the closure of a difference component met p, its generic point would be a
generization of p lying in U, contradicting this equality. Removing those
finitely many closures gives the required extension near p. The image of α
in the quotient then vanishes after shrinking, by localization of F. The
generic representation on A/p and Nakayama fill the remaining closed stratum.
For the pro-object, a map of full-support pairs is onto, while two parallel
maps agree because α belongs to their equalizer. Products and equalizers
produce a cofiltered essentially small system. The local identity of Q_p
factors at one stage; the corresponding epimorphism Q_p→(P_i)_p is also a
split monomorphism, hence an isomorphism. The missing nonzero f is essential.

**H035.9.** A finite module over a domain is free on a nonempty principal
open after clearing a fraction-field basis. Repeating on the finitely many
irreducible components of the residual closed subset gives noetherian
induction, and a finite locally closed stratification. No normality is used.

**H035.10.** Recomputed L_(p)=p^(-1) Z_(p), while L_f has arbitrarily new
prime denominators. Thus every local rank and every residue rank is one, but
no nonzero principal localization is finite. The element 1 belongs to the
image of F(pZ) for every prime p and to no F(0); their intersection is zero.
This separately checks failure of minimal support. For the repair, n minimal
generators and generic rank n over a domain give B_p^n≅P_p: its kernel is
torsion and a submodule of a torsion-free module. The extra finite F(B) then
provides a finite locally free representing dual on an open. Theorem 12
really contains that extra hypothesis.

**H035.11.** The nilradical is nilpotent locally, so only finitely many graded
pieces occur on each noetherian affine. Generic freeness applies to each.
This statement is about graded freeness, not openness of the CM locus.

**H035.12.** Independently check the regular-element implication on the last
nonzero graded piece of A. That piece is free and faithful over A/J, so an
annihilator modulo J would contradict regularity on A. On each coefficient
graded piece regularity implies xR∩J^rR=xJ^rR. The quotient filtration is
therefore the reduction of the original filtration and induction applies.
Only nilpotence of the image ideal in the quotient is needed; it need not
equal the quotient's nilradical. The Koszul resolution supplies every positive
Tor, as required later.

**H035.13.** Recomputed with the two exact sequences involving image B and
cokernel H. Tor₁(M,B)=0 injects Z⊗M into K⁰⊗M and Tor₁(M,H)=0 injects
B⊗M into K¹⊗M. The kernel is exactly Z⊗M. The lemma supplies these two
modules simultaneously on a common dense open.

**H035.14.** The field example gives dimensions 1 and 2, so the written
coefficient cannot compute the stated Hom. Applying Hom(−,Q) to the finite
presentation independently gives L_i^∨⊗Q. The correction concerns the formula,
not a change of the earlier source module P.

**H035.15.** Recomputed the periodic resolution with d₁=x,d₂=y over
k[x,y]/(xy). Tensoring with A/(y) makes d₁ injective, so Tor₁ is zero.
Z¹=A gives the other zero Tor. Meanwhile (x)⊗A/(x)=k whereas the kernel
of y on k[y] is zero. This is a full counterexample under the standard cycles
meaning of Z¹. The repaired B¹ condition follows from the two exact sequences;
the alternative Tor₂(H¹) condition follows from their long Tor sequence.

## H035.16–H035.21 — checked 2026-11-19, 04:15–04:18 UTC

**H035.16.** Re-derived the length argument: all powers of a fixed parameter
system give length n₁⋯n_d C. For one variable, multiplication maps between
successive quotients must be injective by the length difference. Krull
intersection then gives regularity, successively, on W. After completion it
is enough to use the chosen original parameter system, not an unproved claim
about every new formal parameter system. MCM duality gives L/qL=A/q; the
surjection A→L is an isomorphism because Tor₁(L,A/q)=0 and Nakayama kill its
kernel. This proves the canonical-module reconstruction. It does not identify
the literal heading with Kähler differentials; the k/k test rules that out.

**H035.17–18.** The dual Koszul resolution has one nonzero cohomology in
degree r, namely ω/(x)ω. Shifting ω[d] gives the quotient's normalized
dualizing complex in degree −(d−r), verifying the sign and the dimension.
At dimension zero Matlis duality gives E(k), whose simple essential socle
proves indecomposability and whose cogenerator property detects maps.

**H035.19–20.** Matched Lyu Lemma 6.1(ii) to the finite module spread from
each generic point, and Corollary 4.7 to quotients of a regular ring.
Gor-2 implies CMU, so the cited EGA openness statement supplies the CM open.
The opens can be chosen in disjoint components, then their sheaves extended
coherently. The extension uses the quasi-coherent direct image on an affine
noetherian neighbourhood and finite generators on its quasi-compact open;
Zorn glues compatible extensions in the locally noetherian case. Excellence
gives J-2, hence a regular and therefore Gorenstein open in every integral
quotient. This proves the margin's excellent clause, without claiming a
global dualizing complex on every excellent scheme.

**H035.21.** Rechecked all steps of the counterexample rather than treating
the displayed infinite-variable algebra as noetherian. A nonzero polynomial
belongs to only finitely many block primes. Finite prime avoidance and a
generic scalar combination show that the stated localizations have exactly
those maximal ideals. Finitely many local generators, together with one
nonzero ideal element, then generate any ideal globally. Each local ring is
the one-dimensional semigroup domain K[t³,t⁴,t⁵]_(t³,t⁴,t⁵). Modulo t³ the
basis is 1,t⁴,t⁵ and the socle has dimension two; scripts/check_examples.out
checks that finite computation as well. Every dense open meets such a point.
A finite generic canonical module would have rank one and be free on a
smaller dense open, where this socle computation contradicts the required
injective hull. Gor-2 is the correct uniform all-integral-quotients condition:
necessity follows by generic freeness of a rank-one canonical module.

## H035.22–H035.31 — checked 2026-11-19, 04:35–04:44 UTC

**H035.22.** Constant one satisfies the written implication because its
antecedent never holds, and satisfies multiplication and subadditivity.
It fails the diagonal axiom for a distance. After adding f(0)=0,
multiplicativity forces f(1)=f(−1)=1 and the reciprocal identity.
The displayed inversion estimate proves continuity at every nonzero point.
This independently checks the definition's actual defect; the inserted
typescript is still not attributed to Grothendieck without evidence.

**H035.23.** Recomputed the estimate on the n+1 binomial terms, including
the zero case for their maximum. The factor (n+1)^(1/n) tends to one.
A uniform bound on all integers implies the bound one by applying it to
arbitrary powers of each fixed integer. The logarithm construction gives
a real valuation, with infinity assigned only to zero.

**H035.24.** At n=p the alleged root of unity is exactly zero, so the
supporting sentence is false even though the corollary is true. On the
nonzero prime-field elements, finite multiplicative order gives value one;
the remaining value is zero. H035.23 then applies with all its hypotheses.

**H035.25.** A zero exponent identifies a nontrivial value with the trivial
one on the multiplicative group and prevents symmetry. Re-derived the
positive-power topology theorem using powers a^n and rational cuts of
logarithms. The trivial topology case is separate: a nontrivial absolute
value has a sequence of nonzero powers converging to zero and is not
discrete. This matches the exact Bourbaki proposition checked separately.

**H035.26.** In the nonarchimedean case two small-valued distinct primes
contradict Bezout, since all integer coefficients have value at most one.
In the other case, the base-b expansion gives the upper logarithmic bound
with a constant independent of the power n. If any integer a≥2 had value
at most one, the reverse base-a expansion would bound an exponential by a
linear function. Thus the reverse logarithmic bound is legitimate. The
triangle inequality forces the exponent at most one, and concavity in the
elementary form t^s≥t on [0,1] proves the converse. No omitted trivial case
or unfinished sentence is used as a source for this completed proof.

**H035.27–28.** Independently applied finite artinian Matlis duality to
identify the Hom test with the map modulo each parameter ideal. Nakayama
first gives surjectivity, even if not assumed. The kernel belongs to every
parameter-power multiple of the source, hence vanishes by Krull intersection.
For the cancelled corollary, tensoring the isomorphism on Omega and using
both stated base-change maps gives exactly this test. The single-parameter-
ideal DVR example checks why the universal quantifier cannot be dropped.

**H035.29.** Recomputed the zero-transition system over a field: its colimit
Hom functor is zero, but none of its nontrivial transition maps is invertible.
For the repaired strict system, finite generation selects a stage equal to
F(Omega). In the parameter square, the right vertical map is injective by
strictness; the upper horizontal is surjective and the left vertical is an
isomorphism, which forces right-vertical surjectivity. This argument does
not assume base change for the individual Hom stages. H035.27 then makes
each later transition an isomorphism at every prime, hence globally.

**H035.30 — central implication independently rechecked.** Starting from
the six hypotheses, first pass to every quotient using exactness of
noetherian completion; do not pass the completion assertions to arbitrary
localizations. The local criterion and finite-length tests give finite
representing modules at all primes. Constructible rank plus the additional
finite F(B), supplied by (iv), gives generic representation on integral
quotients by H035.10. The full-support construction then gives a strict
finite prorepresentation. Choose Omega canonical on a dense open, not
merely a nonempty one: this makes its intersection with the nonempty open
from (vi) nonempty even when the base is reducible. F(Omega) remains finite
after localization, and H035.29 makes the localized pro-object stationary.
Noetherian induction via H035.5 closes the proof over the original A.
For necessity, Hom commutes with limits, finite presentation gives filtered
colimits and finite values, and the generic CM open plus H035.13 gives (vi).
The literal insertion “non nul” was checked on the scan. This pass found no
remaining dependency on the false statements H035.10, H035.15, H035.21 or
the non-strict version of H035.29. Their proved repairs suffice without
strengthening the hypotheses of Theorem 12.

**H035.31.** On an integral quotient use Omega=B in (vi), then intersect
with a regular open. A regular local ring has a parameter system generating
its maximal ideal, so the comparison gives F(B) tensor k(p)=F(k(p)).
Generic freeness of the finite module F(B) makes this rank constant on a
nonempty open. Noetherian induction gives (v). The ring condition is Gor-2,
so the canonical-module step still applies. This checks both claims.

## H035.32–H035.38 — checked 2026-11-19, 04:38–04:44 UTC

**H035.32–33.** Matched proper finite presentation, proper support and
base flatness to Hall Theorem C, final author version p.4; matched left
exactness to Example 3.10 p.18. For finite F, its Hom functor commutes with
filtered colimits on the quasi-compact quasi-separated X, which gives finite
presentation of P. For arbitrary F only a representing module is asserted.
Recomputed arbitrary affine base change using the affine projection X_T→X:
the pushed coefficient is exactly G tensor_A M even for a nonflat B.
Yoneda gives P_B and the cocycle, hence gluing. In the colimit construction
the maps P_i→P_j go in the same direction as F_i→F_j. No flat base-change
assumption or reversal of that direction remains.

**H035.34.** Re-derived the formal comparison before taking limits.
Artin–Rees makes reduction exact in the pro-category on finite modules;
locally it compares the Ext complexes with their coefficient quotients.
The proper cohomology comparison is the actual pro-isomorphism of Stacks
30.20.4(1),(3), not only the eventual inverse-limit equality. The exact
reduction functor can therefore be applied to the finite part of the
local-to-global Ext spectral sequence, and its E_2 comparison propagates
to the abutment. This verifies formal modules that do not descend to A.
For the generic arbitrary-tensor and regular-quotient claims, the proof was
expanded to list the finitely many page kernels, images and filtration terms.
Generic flatness, respectively all-positive-Tor vanishing, keeps each page
exact after the coefficient change. This avoids an assumed global locally
free resolution and an unexplained interchange with a spectral sequence.
The example Ext^1(A/(t),−)=−/t confirms failure of left exactness.

**H035.35–36.** A local resolution needs one term beyond the desired
cohomology degree; the written truncation retains it and also includes its
artificial final cohomology in the generic-freeness list. For the Tor
criterion, re-indexed the resolution/complex double complex: a bounded
cochain direction gives finitely many terms on each total diagonal. The
two vanishing assumptions collapse the two spectral sequences and the
augmentation identifies the surviving edge map with the canonical map.
This is stronger than the false two-Tor assertion on scan 10.

**H035.37.** Rechecked that the graded coefficient pieces are finite over
finite-type algebras, so relative generic freeness gives flatness over the
reduced base; they need not be finite base modules. The last nonzero free
graded piece of A is faithful and detects regularity modulo the nilpotent
ideal. Strictness of the coefficient filtration survives quotienting.
The proof needs both graded objects; the ambiguous ink is not resolved by
this need. R/F is a definite notation mismatch, while the first graded
coefficient remains uncertain.

**H035.38.** Recomputed the P^1 extension via its connecting map t:
H^0(E)=0, H^1(E)=A/(t), and H^0(E_0)=k. The sheaf is locally free and the
map proper, so all hypotheses of the literal all-S claim are met. For the
repair, first localize at p; the parameter Koszul complex is finite free
over A_p. Its tensor with E is a resolution by the generic Tor vanishing.
Applying derived global sections and the all-positive-Tor vanishing of
the finite cohomology modules gives exactly the required edge isomorphism.

## H035.39–H035.46 — checked 2026-11-19, 04:39–04:44 UTC

**H035.39.** This item remains OPEN. The dense-open upgrade was checked
again: the kernel of B→B_f is killed by a power of f, and the quotient has
support exactly one irreducible component. Its nonempty good open meets
D(f), where the original functor and module agree after localization.
Thus the generic condition survives composition on reducible bases.
Separately checked the countable local-completion lemma in
COMPOSITION_ATTEMPTS.md: finite evaluation images are closed by linear
compactness, their countable union covers the complete metric limit, and
Baire gives a finite open submodule. Artinian stable images plus Chevalley
then give the pro-adic comparison. Countability is used exactly once and
cannot be silently removed. The Dedekind case follows because each finite
completed module is an algebraizable summand and the quotient ideal is
artinian. Neither check settles principal completion in dimension two.

**H035.40.** Ext and Tor of finite modules use finite portions of finite
free resolutions, so the same Artin–Rees and generic-Tor arguments apply.
The proper cohomology examples reduce to H035.34. Direct image along
A^1_k→Spec(k) sends its coherent structure sheaf to the infinite module
k[t], excluding the unqualified nonproper statement. The page's broader
two-scheme notion is prospective and undefined; this is a scope limit on
the programme, not evidence that its contextual proper examples fail.

**H035.41.** On the affine scheme representing linear maps, the unit
equation and the multiplication equation are maps into the structure
sheaf. H035.33 represents each by a map from a quasi-coherent base module.
Their image ideals cut out exactly the algebra maps after every base
change. Checking images rather than pulled-back injections makes the
argument valid also for nonflat base changes. No extra associativity
equation is needed between algebras already known to be associative.

**H035.42.** A finite affine cover selects finitely many algebra generators
from one finitely presented approximation of B as a module. A closed
subscheme of the resulting finite-presentation cone is of finite type.
For finite presentation, the relation ideal is finitely generated over
Sym(Q); choose a finitely presented module R mapping to those ideal
generators. P_R is finite, so its image gives finitely many equations.
This proves finite presentation without a noetherian-base assumption.
The infinite-variable polynomial example checks the distinction between
a closed immersion of finite type and one of finite presentation.

**H035.43–45.** Re-derived the universal-section reduction to Y_T=X_T.
The inclusion of its ideal corresponds to P_I→O_S; its image ideal is
the closed condition. Vanishing after tensor is the relevant statement,
so no false flatness assumption is used. Recomputed the cone for A/(t):
Sym_A(A/(t))=A[x]/(tx), with fibres of different dimensions. Thus coherent
F does not justify “vector bundle,” and the sheaf formula needs f_*.
The exact Murre source is exposition 294, Theorem 3, printed p.255,
with its adic condition (in particular proper X), flatness, finite type
and locally noetherian base. The modern proof here handles proper flat
finite presentation over an arbitrary base. SGA3 VIII 6.4 uses the
different essentially-free hypothesis and is not substituted for Murre.

**H035.46.** The universal property of Sym and relative Spec identifies
sections of the cone with Hom into O. Applying H035.33 and Yoneda gives
the claimed cone on S. The filtered colimit of representing modules
becomes the inverse limit of cones. The identity-map example with an
infinite-dimensional source excludes any additional finiteness conclusion.


## H035.39 — second derivation of the stronger countable-base theorem

Rechecked in reverse dependency order, from the desired composite comparison.
If W=G(M) is finite over the completion C, the outer completion axiom applies
to W. What remains is a pro-isomorphism, not just an equality of inverse
limits: an arbitrary additive F need not preserve an equality of limits.
For the natural W/I^nW→G(M/I^nM), each kernel and cokernel is finite over
C and killed by I^n. At a prime q over I, C_q completed is A_p completed:
the identity modulo p^r follows from exact completion and I^r⊂p^r.
Flat base change for G is valid over C without any finite-output assumption.
The two nested limits of G(M_B/(I^n+m^r)M_B) commute; fixing r makes the
n-system eventually constant. Thus the comparison has zero completed-local
error limits. Matlis duality, exact filtered colimits and exact duality give
exact limits of finite B-modules. This does not assume finite length or ML.

To detect pro-zero, fix a target index before choosing a prime. The descending
supports of the images stabilize; at a generic point of a nonempty stable
support the images have finite length and hence stabilize nontrivially. Flat
completion and exact inverse limits then give a nonzero local limit, a
contradiction. The order of these choices is essential: vanishing at each
prime alone would not give a uniform index without the support argument.

It remains to check that countability supplies W finite without presupposing
the comparison just proved. Use only the given I-completion equality for G.
Any finite C-submodule L of W has closed image after every completed maximal
localization: the maximal-completion axiom identifies the target limit, and
exactness of inverse limits lifts every compatible family in its finite
coordinate images to L_B. The map from W is continuous because its rth
coordinate kills I^rM. Faithfully flat descent at all maximal ideals proves
L closed globally; it does not require W/L finite. All maximal ideals of C
contain I. Finite presentation makes each evaluation image from N finite
over C. Countability is used precisely to enumerate the finite presentation
matrices of N, not to claim the completion or M is countable. Finitarity gives
the union of the finite sums of these images. Baire gives an open one, and
its quotient is finite because it is a quotient of a submodule of one V_n.

Boundary checks: I=0 gives a constant system; I=A gives the zero completion.
The nonartinian example K_n=(x^n,y^n) does not contradict this argument because
it lacks the completed-local comparison at the generic point (x). The earlier
weighted-torsion candidate explicitly fails that same axiom. The countable
proof makes no claim for an uncountable union of closed finite submodules.
No circular use of finite completed output, generic base change or a presumed
Mittag–Leffler property remains in this derivation. The broad arbitrary-base
assertion stays open; the sufficient finite-output gate is strictly smaller.


## H035.39 — separate check of reductions (E) and (F)

For (E), start with the possible defect W/L. Each U_n is finite because
it is a submodule of the finite V_n. Countably many actual lifts suffice
to make L→U_n surjective for all n. After completed localization B, flatness
preserves those images, while the original local completion axiom identifies
W_B with lim V_n,B. Its assumed finiteness makes the descending projection
kernels a Chevalley system. Thus L_B maps onto W_B/m_BW_B; Nakayama yields
L_B=W_B. Vanishing at every maximal localization proves W/L=0 for this
possibly nonfinite quotient. The global finiteness conclusion then uses a
countable cover by closed finite C-submodules and Baire. This is stronger
than the invalid assertion that stalkwise finite modules are globally finite;
the countable lifts and the actual completion comparison are essential.

For (F), work first with the finite-length output tower, not with an assumed
finite W. Exact inverse limits over D commute with the finite generator map
for m^r, so W/m^rW=lim V_n/m^rV_n. Interchanging r and n gives intrinsic
m-adic completeness. This remains correct for an infinite k-vector space:
its intrinsic m-adic topology is discrete, which need not be its pro-topology.
Finite W/mW and completeness prove finite W by successive coefficient
lifting. Thus passing to the k-valued H loses no obstruction to finite output.

The remaining axioms for H were checked independently: at p≠m it is zero;
its rank has one-point support; its generic comparison is either zero on
a nonempty open or the empty-parameter identity in dimension zero. For a
principal completion C, tensoring H(N) to D changes nothing because H(N)
is killed by m, and D/mD=k. The local-completion double-limit argument
therefore supplies the principal axiom without an unproved localization
of the original principal axiom. No boundedness of the k-dimensions along
the tower is assumed. The remaining question is exactly that boundedness
for finite completed inputs, and it is explicitly still open.
# Additional boundary checks, 19 November 2026, 05:54 UTC

The finite-generator side case was rederived from Yoneda: an element that
generates a finitary functor lifts to its value on a finitely presented
module P. Every use of the original generator factors through this lifted
one, so Hom(P,−) still surjects. On a finite module over a noetherian
extension, Hom(P,−) is the kernel of a map between finite modules; its
quotient is finite. This matches Hall2014, Lemma 6.6, p.24. It does not
assert that every archival functor is finitely generated.

For the residue-field inner case, start instead with arbitrary vector
spaces as filtered unions of finite-dimensional subspaces. Additivity and
finitarity identify the outer functor with tensor by its finite-dimensional
value on k. A finite basis identifies that tensor with a finite direct sum,
which commutes with every inverse limit. No finite dimension of the inner
completed output is used. Both are additional proved cases and checks on
the interpretation of the sufficient gate; neither changes the general gate.

