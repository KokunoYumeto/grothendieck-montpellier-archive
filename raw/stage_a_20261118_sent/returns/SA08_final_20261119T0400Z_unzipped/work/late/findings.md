# Findings from scans235–327

## Coverage and the main result

This contribution reads both complete supplied transcriptions,
MPL_136_235-281 and MPL_136_282-327, against all163 indexed note entries
(75 and88 respectively). The resulting records contain122 items,90 claims,
30 problem entries and73 mathematical reading alarms. No second-pass files or
manuscript scans were supplied. Every proposed correction is therefore a
mathematical alarm, not an emendation of the diplomatic source.

The central outcome is a sharper separation of three achievements. The
weighted integral cohomology comparison has exact published developments.
The positive tail and finite derived recovery assertions can be proved over
arbitrary coefficient rings. The stronger programme—an infinite quotient
carrying multiplication and enough coherent operations to recover homotopy
types—still needs a precise category and a precise comparison map. The
manuscript itself marks several of these transitions as incomplete.

The later pages also contain a second, coherent exposition on universal
constructions: an authored cover at301 followed by seventeen numbered pages
302–318. Its ordinary categorical results are largely recognizable through
Yoneda, presheaf cocompletion and Dold–Kan. The open parts concern the selected
operation category, arbitrary-topos extension and nonlinear structures. The
geometry at326–327 is a separate curve/projective-connection investigation,
not an example inferred from the repeated SGA7 donor material.

The tables preserve three different voices: the manuscript; ideas and
comparisons of the earlier Pro runs; and reconstructions or counterexamples
checked in this consolidation. Historical classes A–F are not truth values.
In particular, class C can mean that a local assertion is proved here while an
exact published fate has not been identified. It does not assert novelty or
current mathematical openness.

## 1. Source layers and chronology

The reuse of paper matters. Printed seminar notices in1975 give evidence about
the support, not an exact date for the handwritten argument. A scheduled
defence date is not the date of printing or writing. The annotation1975–1976
beside302 and the uncertain title word at301 do not fix a delivery date.
Cartan's original article supplies a different kind of evidence: §7 explicitly
refers to Grothendieck's lecture of12December1975. The article appeared in
December1976. Its note added in proof already knew Miller's preprint, whose
publication followed in1978. These dates should not be collapsed into the
catalogue's broad date cue. [SA08-402, SA08-511; late_Cartan1976]

The alternating ExposéIX pages are a separate donor stratum. Twenty-three
late-package leaf matches are recorded in links.tsv, from the original SGA7I
publication. The original PDF page is the published page plus5. The reused
text covers semistable reduction, abelian parts of Néron models, monodromy
pairings, formal algebraization, analytic comparison and Picard
representability. It was published in1972, before the live PD compilation.

For exact authored donor-to-publication matches the dossier uses class A, with
that chronology stated in every record. Imported GAGA and Tate inputs retain
their prior-background status. Unresolved stronger questions remain separate.
This convention does not claim that a1972 theorem was a later development of
the1975–1976 de Rham work. A full-text audit added Proposition7.5 on262 as
C288/item523, because it was present in the transcription but not isolated by
the notes. [late_SGA7IX, publishedp412]

The analysis exercises on292 and294 are also reused support. Their Dirichlet
test and geometric sums do not constitute another chapter of the universal
constructions exposition. The source inventory, local author pagination and
reported missing cover at319 are recorded as different kinds of evidence.

## 2. Weighted comparison, completion and the degenerate object

Scans235–239 preserve a filtered assertion with explicit restrictions. The
associated-graded coefficient map from the one-generator PD algebra must be
an isomorphism. The comparison is stated in a degree range, and the stronger
unfiltered formula at the start of237 is deleted. The notes correctly resist
restoring it as the conclusion. The modern reconstruction must additionally
state what completion means, whether the differential is continuous, and what
justifies passing between a completed filtered complex and its associated
graded. [C201–204; D10–46,85–115,146–152]

Cartan1976 is the closest exact published source. Theorem3p267 has a
flat-cycle hypothesis; §6p268 modifies an extension axiom and retains
multiplicativity conditions. Section7pp269–271 gives the weighted integral
model and the degree/weight comparison. It also explicitly recovers the
ordinary cup product from the family of binomial product factors by their
gcd1 property. The earlier note's Bézout illustration is correct, but the
deduction is already printed there. [C284; late_Cartan1976]

The manuscript anchor for that comparison is only the phrase about
compatibility with multiplication on273 (D1571). The weighted-product/gcd
deduction belongs to earlier-run note74. The binomial recurrence on275 is
instead the module-rigidity calculation; it must not be cited as a displayed
weighted-product formula.

Garvín et al.1998 was initially inaccessible through the web fetch, then
successfully downloaded as the original eight-page article and read in full.
Theorems4.1–4.2 give the arbitrary-simplicial-set result in the strict range
\(p<q\). Proposition3.2 and Remark3.3 establish \(q\)-extendability and the
failure of the next extension condition. The looser words “up to degree q” in
the next statement are not used to enlarge the explicit theorem. This
source does not, by itself, establish the manuscript's inclusive boundary
or its arbitrary completed coefficient formulation. [C204;
late_Garvin1998, pp174–176]

One final audit corrected a substantive overinterpretation in this run. On239
the degenerate object is written \(\Gamma_k^p(\Psi_*)\), followed by an uncertain
\(\Pi_*|K_*(k,p)\) name. It cannot simply be called an ordinary
Eilenberg–Mac Lane object. For the standard simplex quotient, the normalized
quadratic divided power is
\[
0\longrightarrow k\xrightarrow{-2}k\longrightarrow0
\]
in degrees2 and1. Thus it has \(\ker(2)\) and \(k/2k\), and is acyclic over
\(\mathbb Q\). Both the ordinary-\(K(k,2)\) reading and the all-weight
nonflasqueness assertion need a notation/hypothesis alarm. Weight1 is still
nontrivial, so this does not restore full unfiltered acyclicity. The exact
faces and matrix calculation are saved separately. BMT2016 Proposition3.5
and Corollary3.6p270 give the corresponding derived nonlinear framework.
[C205; proofs.md §15; late_quadratic_normalization.json]

## 3. The \(p\)-adic test is now explicit

The question on239 is answered by the valuation function
\[
a_p(n)=v_p(p^n/n!)=
\frac{(p-2)n+s_p(n)}{p-1},
\qquad
b_p(i)=\min_{n\geq i}a_p(n).
\]
The ideal generated by the tail is \(p^{b_p(i)}\mathbb Z_p\).
For odd \(p\), any minimizer lies below the explicit finite bound
\[
\left\lfloor
\frac{(p-1)a_p(i)-1}{p-2}
\right\rfloor.
\]
The filtration is cofinal with the ordinary \(p\)-adic one. At2 all positive
ideals are \(2\mathbb Z_2\), so the separated completion is \(\mathbb F_2\).
For odd primes,
\(b_p(p-1)=b_p(p)=p-1\); hence a positive associated-graded piece vanishes.
Cofinality therefore does not supply the graded-free hypothesis used on235.
[C206–207; proofs.md §1; late_Stacks07GK]

The line asserting weak monotonicity exactly when no carry occurs needs
correction on the ink. The exact difference is
\[
a_p(i+1)-a_p(i)=1-v_p(i+1).
\]
Weak monotonicity allows valuation1; strict monotonicity requires valuation0.
The test \(p=3,i=2\) gives equality and detects the distinction. This is a
new reading alarm in the consolidation, with no diplomatic change. [C208]

## 4. Finite adjoints are sound; the derived inference needs a real extra fact

For finite cutoffs in nonnegatively graded modules, the four adjoints
\(q\dashv i\dashv\tau\dashv\rho\) have explicit formulas. High truncation is
exact, the right section is graded Hom from a tail, and its counit is an
isomorphism. The quotient left adjoint is generally only right exact:
\(tk[t]\hookrightarrow k[t]\) becomes \(tk[t]\to0\) at cutoff1.
These are ordinary restriction/Kan-extension facts. [C212–214; proofs.md §3;
late_Kelly1982]

For \(S=\Gamma_k(T)\), the positive-degree binomial recurrence is rigid over
arbitrary \(k\)-modules. Prime-local cofinal rows with degree
\(\ell^r-1\) make the necessary binomial coefficients units. This proves
the nonnegative unit, not a unit in every integer degree. The same
cofinal method completes the explicit left coefficient adjoint
\[
L(P)=
\left(\bigoplus_{n\geq0}P_n\right)/
\left([T^{(m)}x]_{n+m}
-\binom{n+m}{n}[x]_n\right).
\]
After localization at a prime, \(L\) is a filtered colimit of exact degree
evaluations with specified normalized transition maps; it is therefore exact.
Consequently the coefficient embedding \(i\) preserves injectives, and the
finite derived unit and induced-target Ext vanishing follow.
The parent and early agents independently checked this proof.
[C215,C222,C286; proofs.md §§4–5]

This verifies an existing manuscript assertion and an earlier-run repair. It
does not validate the abstract argument on263. An exact fully faithful
embedding landing in the underived section image need not be acyclic for that
section functor. The saved triangular-category counterexample over
\(k[\epsilon]/\epsilon^2\) retains the extra exact extraction right adjoint and
still has nonzero higher derived sections. The actual repair is exact \(L\),
not an appeal to underived full faithfulness. [C221; proofs.md §6;
late_Stacks015M, late_Stacks015Z]

## 5. Infinite quotients and negative degrees must be separated

The manuscript moves among several negligible classes. Uniformly
bounded-above modules form a Serre subcategory but are not closed under
arbitrary coproducts. Elementwise eventual annihilation by high PD tails is
not even extension-closed over \(\Gamma_{\mathbb F_p}(T)\). If \(I\) is the
positive ideal, the sequence
\[
0\longrightarrow I/I^2\longrightarrow S/I^2
\longrightarrow\mathbb F_p\longrightarrow0
\]
has negligible ends, while the middle is not negligible because the
indecomposable classes \(T^{(p^r)}\) survive arbitrarily high.
[C216–218; proofs.md §7]

A legitimate replacement is the localizing Serre closure of bounded modules
in the nonnegative category. Exact \(L\) kills this class, and the injective
coefficient objects are local. This gives a derived recovery statement for
that explicitly changed quotient. It does not identify it with the
manuscript's elementwise class or prove the proposed colimit formula for the
section functor. The missing definition and finiteness hypotheses remain in
the problem index. [C287; MP66–67; late_Stacks02MN]

The negative-degree recurrence on299 has a different answer. Its universal
coefficient group is \(\mathbb Q\), so the resulting value on a module \(M\)
is \(\operatorname{Hom}_{\mathbb Z}(\mathbb Q,M)\), not
\(M\otimes\mathbb Q\). Evaluation at1 need not embed this group into \(M\):
the quotient map \(\mathbb Q\to\mathbb Q/\mathbb Z\) is nonzero and kills1.
This variance distinction is central to avoiding an incorrect all-graded
full-faithfulness claim. [C239,C286; proofs.md §8]

## 6. Universal constructions and nonlinear operations

The exposition302–318 has several firm ordinary categorical steps. A small
presheaf category is the free cocompletion of its representables; the
category-of-elements formula gives the extension. The Ab-enriched version
gives the additive construction. Dold–Kan works in the stated additive
idempotent-complete setting, and the definition includes degeneracies: the
historical word demi-simplicial is not evidence for replacing the indexing
category by injective maps only. [C240–247; KellyTh4.51; Stacks019G;
Ekedahl§1]

The internal Hom formula describes degree-zero cycles, namely chain maps;
its degree-zero homology would instead describe chain-homotopy classes.
Commuting bicomplex differentials require a totalization sign. Native
levelwise tensor and ordinary chain tensor are not strictly identified by
normalization: the degree-one rank of the levelwise tensor of
\(\operatorname{DK}(\mathbb Z[1])\) differs from that of
\(\mathbb Z[1]\otimes\mathbb Z[1]\). Transported structures and comparison maps
are separate constructions. [C244,C246,C251; Richter2009§7;
Schwede–Shipley2003]

The author explicitly says that raw representable invariants need not be
homotopy invariants and that bare additive chains do not recover
multiplication. Both warnings receive claim rows, C289 and C290. They have
elementary checks: a representable functor based on
\(\operatorname{DK}(\mathbb Z[1])\) separates the point from the interval,
and \(\mathbb{CP}^2\) and \(S^2\vee S^4\) have the same free chain-homotopy
type but different cup squares. This is exactly the distinction that later
E-infinity, numerical, binomial and affine models require one to respect.

The selected-shape operation construction has a precise analogue in
KellyTh5.35, but the manuscript's variance and projector reservations are
substantive. The arbitrary-topos expectation does not yet specify the
appropriate class of functors. A newly checked2026 comparison, Touzé's
preprint on the universal property of strict polynomial functors, proves
uniqueness and restricted existence for exact strong tensor functors over a
field and specified tensor abelian targets. It is useful current context,
not a proof for the manuscript's arbitrary-ring or lax-convolution setting.
[C248–250,C259; late_Touze2026, introductionpp1–5]

## 7. Convolution powers: a positive flat theorem and two exact limits

Yoneda translates the proposed natural operations into maps
\(A\to\Gamma^n A\). Addition, multiplication and iteration are separate
compatibility diagrams. Set-valued natural transformations need not be
additive in the element on which the operation acts, and the universal pair
for addition consists of the two inclusions into \(A\oplus A\).
[C252–254]

For a flat counital cocommutative coalgebra \(A\), the construction works.
SGA4XVII5.5.2.4–5 gives
\(\Gamma^n A\simeq(A^{\otimes n})^{\Sigma_n}\) and flatness of the relevant
divided powers. The iterated coproduct lifts canonically to
\(\delta_n:A\to\Gamma^n A\), and the convolution operation is
\[
\gamma_n(f)=e_n\Gamma^n(f)\delta_n,
\]
where \(e_n:\Gamma^n J\to J\) is the PD evaluation. The proof checks all
PD identities without assuming the ideal \(J\) flat. The original SGA4
pages374–375 were rendered and inspected; they supply the ingredients, not a
verbatim statement of the assembled Hom theorem. [C285; proofs.md §11;
late_SGA4XVII, late_Lundkvist2008]

Nonflat existence can fail outright. The explicit coalgebra
\(\mathbb Z\oplus(\mathbb Z/2)e\) and PD ideal generated by
\(t\) of order2 and \(u\) of order4, with \(t^2=2u\), give a convolution
square that cannot equal twice any additive map. The ring, coalgebra and PD
axioms were checked symbolically and by finite exact enumeration.
[C255]

The uniqueness example has a narrower scope. Over \(\mathbb F_2\), the
canonical family and the family with all powers of index at least2 set to
zero satisfy the positive-index composition and fixed-object binomial
relations. The latter fails the zero-index augmentation equation and full
additive naturality across coefficient modules. The source's quantifier
range is not settled, so this is not an unconditional refutation of its
uniqueness question. [C257]

## 8. Curve geometry and donor-text cautions

On326–327 the real group must be distinguished from its other component:
\(\mathrm{SL}_2(\mathbb R)\) maps onto
\(\mathrm{PSL}_2(\mathbb R)\), not all real
\(\mathrm{PGL}_2\). The missing factor \(i\) in the rotation formula is
detected by a direct substitution. The source itself replaces the full group
by the pointed-disc stabilizer, and changes an analytic description to a
topological one. A topological splitting does not determine a holomorphic
extension class. [C260–262]

For a compact curve and a nonzero-degree holomorphic line bundle, the literal
split projective bundle in the final box cannot carry a holomorphic
projective connection. Such a connection induces one on its trace-zero
endomorphism bundle and hence, by inclusion and projection, on a
nonzero-degree line summand. A holomorphic line connection on a compact
curve has degree zero. The modern nonsplit jet bundle is a comparison, not a
replacement reading. Properness, Omega, the plus sign and the intended
category must be decided on the ink. [C264; BHR2021pp6–8; Dumas2009]

The SGA7 donor matches also expose original printed tensions. The
\(V\subset V^\perp\) line and its proof endpoint disagree in the original
publication, and a corollary's implication label is opposed to its argument.
An extension diagram's P/Q placement also needs care. These should not be
described as errors introduced only by AI transcription. Broad
algebraization and direct ample-descent questions were searched against
Artin, Raynaud and the source's own forward references; the exact stronger
fate was not always identifiable. No novelty inference is made.

## Records for subsequent work

Items, entries and claims retain exact transcription-file line locators.
The55 checked links are separate from14 consolidated project leads and157
literal context-provenance rows. The latter preserve the earlier notes'
reported run names and locators, but unavailable external endpoints are not
certified as mathematical bridges. The twenty-family search log maps every
claim to actual queries, opened sources, failures and hypothesis comparisons.
All substantive web outputs are saved. CHECK_EVENTS.tsv distinguishes source
fidelity, theorem use, independent proof, targeted review and finite
computation.

The next tasks are ranked in directions.md. The strongest unresolved
mathematical target is the precise multiplicative infinite recovery, followed
by the completed comparison hypothesis envelope and the full universal-power
axiom system. The exact coefficient adjoint, finite Ext consequence, negative
coefficient formula and flat convolution construction are already checked
lemmas to carry into those tasks.
