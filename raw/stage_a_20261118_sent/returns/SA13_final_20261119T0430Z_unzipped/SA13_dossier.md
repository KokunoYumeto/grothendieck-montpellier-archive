# SA13 — Séminaire de Géométrie Algébrique

## Consolidated dossier, part 2: cotes 33, 34, 36 and 39

**Assessment date: 19 November 2026.** This dossier consolidates the supplied
Pro notes and diplomatic transcriptions, together with every supplied Codex
supplement. Its unit of coverage is the 379 entries of `NOTES_INDEX.tsv`.
Every entry has an individually authored verdict based on its note and its
transcribed passage. The scripts assemble those reviews, apply explicitly
reasoned semantic merges, and check their integrity; they do not infer verdicts
from headings or keywords.

The principal result is a differentiated map of the work. Much of the trace,
duality, monodromy and biextension programme has an identifiable published
afterlife. Some formulations are stronger than their published counterparts;
several are false literally; others cannot be identified precisely enough to
assign a theorem. The formal-function axioms in cote 39 and several local
depth, coherence and motivic proposals require especially careful separation
between an established ingredient and the entire assertion. The dossier keeps
these distinctions in the claim and problem records instead of assigning one
status to a subject area.

### Sources and limits

The supplied archive contains no `second_pass` records and no manuscript
images. The Pro and Codex transcriptions are therefore the textual witnesses
used here. **No transcription has been changed.** A mathematical contradiction
can justify a reading alarm, but it cannot decide whether a mark is present,
deleted, inserted or misread on the original sheet. “False as stated” refers to
the expressly stated literal formulation, with the counterexample and its
hypotheses documented; it is not an attribution of that error to unseen ink.

The complete source read comprises four Pro packages and fourteen Codex files.
There are 384 supplied scan-marker occurrences: 178 in the Pro texts and 206
in the Codex texts. These are occurrences, not a claim to possess 384 distinct
original sheets. Catalogue page totals, gaps in scan numbering, interleaving
of fronts and backs, and overlap between witnesses are retained. Locators in
the JSON tables use the source filename, cote, scan, and **one-based global
line numbers in that file**. This convention makes the references reproducible
without renumbering a transcription.

The brief quotations in the records distinguish working manuscript, reused
printed text and earlier-run commentary. Printed GIT, Haar measure,
commutative algebra, functional analysis and operator-theory material is not
assigned to Grothendieck merely because it was kept in his papers. A class A
publication match occasionally concerns a later EGA or SGA formulation of a
result on such a leaf; the authorship qualification remains explicit.

## 1. The whole topic and this part's boundary

The following is the complete orientation supplied by `TOPIC.md`. “Other
part” records the topic's structure; it does not imply a review of manuscripts
not attached to this run. Catalogue descriptions and counts are source
metadata, not reconstructed dates of individual sheets.

| Cote | Catalogue subject | Catalogue pages | Coverage here |
|---|---|---:|---|
| 27 | SGA 3, complements XII–XVII, annotated typescript and notes | 36 | Other part |
| 28 | Algebraic groups, SGA 3 | 10 | Other part |
| 29 | Fundamental group, SGA 4/7; letters dated 1959, 1967, 1969 | 216 | Other part |
| 31 | SGA 4, residual drafting material | 101 | Other part |
| 32 | Corrections and additions, including SGA 4 | 47 | Other part |
| 33 | “SGA 1965”, manuscript draft | 180 | Pro scans 098–181 in two packages, with supplied gaps |
| 34 | SGA 7 notes | 209 | Pro scans 002–017 and Codex K34-01 through K34-12 |
| 35 | SGA 7 plan | 5 | Other part |
| 36 | “SGA 7 (ma part)” | 84 | Two Pro packages and Codex A36-01/A36-02 |
| 37 | Re-editions of SGA/EGA; letters 1967–1971 and undated material | 99 | Other part |
| 39 | Elementary functions and structures; formal schemes and preparation | 19 | Supplied Pro transcription, 16 scan markers |
| 40 | Calculations on affine principal bundles | 27 | Other part |
| 41 | Construction of étale morphisms, chapter V | 13 | Other part |
| 42 | Networks of local rings | 6 | Other part |

The 379 indexed entries divide as 70, 113, 93 and 103 among the four Pro
packages. Codex notes supply leads and additional mathematical objects, but
no additional Pro verdict rows. Empty manuscript locators on a context-only
item are deliberate: an earlier-run register or bibliography is not a sentence
in the manuscript.

## 2. Cote 33: derived operations, trace and duality

### 2.1 Constructing the operations and their compatibilities

The order of the working text begins with duality and derived inverse image,
then projection and Künneth maps, their compatibilities, constructibility and
cohomological dimension. It proceeds to curve traces, finite-Tor models,
additivity, local pairings and the passage toward an adic theory. The natural
objects are complexes of sheaves, the operations on them, and the actual
maps between their derived images. An abstract categorical resemblance does
not replace those constructions.

The first substantive self-correction concerns inverse image without
flatness. Preservation of injectives by a right adjoint requires exactness
of its left adjoint; the elementary argument cannot simply survive removal
of flatness. The corrected modern construction uses suitable derived
resolutions. The manuscript identifies the defect on scan 106; the dossier
does not turn a correction into a continuing open question. The map of
canonical operations is compared with SGA 4 XVII and modern derived-sheaf
formulations, while the handwritten requests to check particular diagrams
remain separately identifiable obligations. [C-SA13-005,008,012–013;
MP-SA13-01,03; `SGA4XVII` §§5.2.9,5.4.3; `Stacks06YV`.]

Several coefficient and finiteness distinctions change the truth value of
the formulas. Ordinary Künneth with characteristic-p torsion fails in the
nonproper setting; the Artin–Schreier class defined by the product of two
coordinates supplies the checked obstruction. A proper-factor version is
different. Similarly the ordinary direct-image projection formula for an
open immersion cannot be substituted for the exceptional version: the
boundary of the punctured affine line detects the failure. Finite Tor
dimension alone is not perfectness; pseudocoherence or an appropriate
finite-generation hypothesis is also needed. Stalkwise finite bounds need
not give a uniform global amplitude. Each of these is expressed with its own
hypotheses in the claims and proof notes, rather than as a general rejection
of the formalism. [C-SA13-010–011,015–018,022–023,031 and the linked p1 proof audit;
`SGA4XVII`; `Stacks0FPP`.]

### 2.2 Trace is a construction with coherence data

The curve programme and the local pairing recur across the package boundary.
The sequence 33:144 → 146 → 148 is one continuing construction, not three
independent discoveries. Its local Hom factors, support conditions,
evaluation morphism, shifts and comparison with the global trace have been
merged at the object level while distinct claims remain distinct. The
precise published comparison is SGA 5 III §4; a request to verify one arrow
or compatibility has not been discharged merely by citing “Verdier
duality.” [SA13-32–35,37; C-SA13-036–038,100–105,124–125;
MP-SA13-09; `SGA5III`.]

The trace-additivity discussion needs an equally exact distinction. Strict
cone-compatible chain endomorphisms admit the expected supertrace proof.
Arbitrary endomorphisms of an abstract distinguished triangle do not supply
all the coherence that proof uses, and the audit gives a counterexample to
the unrestricted inference. An unbounded representative of a perfect
object presents another issue: its intrinsic categorical trace is defined,
whereas an infinite alternating sum of termwise traces may be meaningless.
In particular an unbounded contractible representative has intrinsic trace
zero. A deletion of “bounded” is therefore not, by itself, evidence of a
false categorical statement. [C-SA13-024–026,039; MP-SA13-07;
`shards/p1/proofs.md`.]

The finite-level congruences in the adic discussion have been recomputed.
They do not establish a complete adic derived category or all limit
compatibilities. SGA 5 V–VI supplies specific finiteness and passage-to-limit
results, whose scope must be stated separately from the elementary matrix
calculation. The remaining worthwhile task is a precise companion to the
chosen inverse system, not a claim that adic trace theory is still wholly
unconstructed. [C-SA13-024,030,034–035; MP-SA13-06,08.]

The publication history also matters. The SGA 5 seminar was delivered in
1965–1966, but publication was in 1977. Illusie's checked 2026 historical
account distinguishes drafting in 1966, Ferrand's 1968 work, the 1974
correspondence and the spring-1975 compatibility proof. The dossier records
those dates without using them to date an undated archival leaf. Curve
trace comparisons use the actual printed exposés and pagination: VIII,
pp. 351–371; XII, pp. 407–441; XIV = XV, pp. 442–480. [C-SA13-019–021;
`IllusieChronology2026`; the SGA 5 bibliography and p1 reference audit.]

### 2.3 Internal Ext, support bounds and reused mathematical leaves

The later cote 33 pages examine duality and constructibility through Ext
spectral sequences and support estimates. The internal-sheaf/global-group
distinction is decisive. A global Ext bound by twice geometric dimension
fails already over a finite field with suitable torsion coefficients; an
internal statement has different content. A proposed codimension estimate
for ordinary support fails by purity for a closed point in a curve.
Biduality on all bounded complexes is also too broad: an infinite-dimensional
vector space already defeats unrestricted double duality. Constructible
finite objects require a separate statement. These examples explain why
the sheaf mark, the dimension convention and the spectral-sequence indices
are high-priority reading alarms. [C-SA13-107,109–119,162–163;
MP-SA13-36–41; `ILO2014` XVII §6.2.]

The constructible-approximation question is not refuted by showing that
stalkwise injectivity differs from sheaf injectivity. The audit supplies
that distinction and leaves the actual approximation assertion at its
searched, precisely qualified status. Likewise a rank-one Picard assertion
for every smooth surface in P³ of degree at least four cannot be
saved by a genericity theorem: a line on a Fermat quartic contradicts the
literal unrestricted claim. [C-SA13-113–114,141; MP-SA13-38.]

The reused Roos leaves concern more than one topos. Zariski and étale
versions, local-isomorphism criteria and retraction arguments are related
but not interchangeable. SGA 4 VII acknowledges Roos; its §4.1 is not
automatically the strongest draft criterion. The regular-local algebra
leaves also require their physical continuation: the lemma begins at
33:173, continues at 137, and finishes at 135. Reassembled in that order,
it concerns two regular local domains of the same dimension, with common
residue field and m·R̄=m̄. Their common completion yields ideal
contraction, descent of principality and the fraction-field intersection.
It does not assume that a bar denotes completion. The blow-up calculation
has likewise been checked in general dimension through its polynomial
chart. [C-SA13-064,072,130–135,164; MP-SA13-46–47;
`shards/p2/cross_package_merge_audit.md`.]

Other reused leaves belong to topological vector spaces and singular
operators. The exact EVT revision, the “Tribu 63” context, operator
Theorems 4.5.2/4.5.4 and reference [18a] are not securely identified from
the supplied evidence. The dossier preserves their mathematical content
and candidate sources, with unverified bibliographic status where
appropriate. It does not silently import definitions of caps, symbols or
multipliers from a convenient later source. [C-SA13-150–155,159–161,231–241;
MP-SA13-48–50,52–53,178.]

## 3. Cote 34: monodromy, nearby cycles and the depth programme

### 3.1 Inertia and reductions to curves

The opening Pro and Codex material develops monodromy, the action of inertia,
the reduction to H¹ of curves, and the distinction between finite,
unipotent and semisimple behavior. Later notes pursue coinvariants,
fundamental groups and constant parts. These are separate mathematical
statements even when they share a representation-theoretic vocabulary.

The generic-curve reduction uses a parameter function field and a suitable
dominating valuation, followed by finite extensions when needed. It cannot
be described as a finite extension of the original field alone. The
condition ensuring the required open inertia image remains explicit.
Similarly, replacing a general cover by an extension of constants is a
real strengthening: the checked CM quadratic twist over Q(t) becomes
trivial after adjoining a square root of t, while no constant-field
extension removes that dependence. The solvable radical also need not
be isogenous to the abelianization; a semidirect product with a vector
group supplies the obstruction. [C-SA13-180–181,198,203–208,227;
MP-SA13-161,170–173.]

The p-adic good-reduction parenthesis is another substantive warning.
The ordinary good-reduction example with Serre–Tate parameter 1+5 gives
a nontrivial p-adic extension and refutes an unrestricted semisimplicity
converse. A Barsotti–Tate criterion in SGA 7 IX §5.13 is a different
statement. The audit keeps the prime, the base field and the representation
condition visible. A trace described as a natural integer can also fail
by sign: the explicit inertia involution has trace −2. [C-SA13-186,213–215;
MP-SA13-175; the p2 computation and proof records.]

The handwritten coinvariant exposé has a recognizable argument involving
curves, finite Jacobians, twists and almost-all-prime consequences. Its
exact publication history is not settled by matching a draft exposé
number to printed SGA 7 II. The constant-part propositions numbered 4.4
in an earlier reference remain a specific collation gap where the exact
primary proposition was not obtained. This is a gap in identification,
not a declaration that the modern theory of constant parts is open.
[C-SA13-199–204,217–226; MP-SA13-169,176.]

### 3.2 Nearby cycles: conventions before conclusions

K34-05 through K34-08 builds nearby and vanishing cycles, inertia
cohomology, spectral sequences, hyperplane arguments and rectified
depth. The later §5 and §6 in K34-09 return to promises made there.
The crucial convention is explicit on 34:094 and 145:

\[
\Phi_{\mathrm{man}}=R\Phi_{\mathrm{usual}}[-1].
\]

Thus usual isolated-lci concentration in degree n appears in manuscript
degree n+1. Many apparent off-by-one errors disappear after this
translation; other inconsistent indices remain genuine reading alarms.
The dossier does not globally alter every occurrence of Φ to a modern
convention. [C-SA13-800–882,600–613; `P4_SGA7XIII`;
`shards/p4/proof_audit.md` §§10–19.]

Local nearby-cycle triangles do not require properness. The global
identification with generic-fibre cohomology used in specialization does.
For example, remove a single closed special-fibre point from a projective
line over a trait. The resulting morphism is smooth, so its local vanishing
cycles vanish, but the special fibre is an affine line and the geometric
generic fibre is a projective line; their H² differs. The corrected
global statements retain properness. Constructibility is compared with
the exact general finite-type theorem in SGA 4½, Finitude §3.2, printed
p. 244, rather than being restricted unnecessarily to the earlier
characteristic-zero résumé. [C-SA13-802,804,809,812,815;
`P4_DeligneFinitude1977`; `P4_SGA7XIII` §§2.3.1,2.4.2.]

The normal-crossing monodromy exponent also needs precise indexing:
the checked modern logarithmic bound uses min(q+1, log rank), not the
off-by-one reading inherited from the old formula. In divisor transition
maps the multiplier is ramification index, not field degree; those
numbers can differ over an imperfect residue field even in the relevant
strict local setting. These calculations have complete hypotheses and
captured code outputs. [p4 Codex claim/proof records;
`P4_IllusieLog2002`, Corollary 8.4.4.]

### 3.3 Geometric depth and its exact limits

The geometric-depth invariant is defined from a regular local
presentation and the **minimum number of generators of the defining
ideal**. Arithmetic rank and ordinary depth are different invariants.
The localization inequality and the flat-local comparison on 34:151–153
therefore require their own hypothesis audit. The searched sources
establish important finite-type and lci cases, but do not by themselves
settle every all-noetherian formulation retained on those pages.
[C-SA13-603–604; MP-SA13-190–191; `RC_SGA2` XIV §5.3.]

For a flat lci family of relative dimension n over the specified trait,
with singular support in the special fibre of dimension at most d, the
proper global manuscript range is [n−d+1,n+d+1]; the sheaf range has
upper endpoint n+1. The sharp global upper bound uses a pointwise
support estimate from perversity. Combining a crude sheaf range with
the bound 2d alone would not prove it. The characteristic-zero SGA 7 I
antecedent and Illusie's general prime-to-residue-characteristic trait
theorems are distinguished. The isolated case gives the familiar
restriction of nontrivial monodromy to the middle degree under its
properness assumptions. [C-SA13-605–606; `RC_SGA7I` §§4.5–4.8;
`RC_Illusie2003`, Theorem 2.6 and Corollaries 2.7,2.10.]

The literal unrestricted root-tower question on 34:139 has a negative
answer. Gabber's example, expounded by Orgogozo, gives a regular
strictly henselian local ring of dimension two with a principal open U
and nonzero H³(U,Z/ℓ). The prime-to-characteristic root tower has
deck group of ℓ-cohomological dimension one. If that tower had
cohomological dimension at most one, the two-column Cartan–Leray
spectral sequence would force H³(U,Z/ℓ)=0. This deduction is explicitly
the review's application of the published example. It does not refute
a suitably restricted quasi-excellent version. [C-SA13-868;
`P4_OrgogozoDimension2014`, XVIII_B §2.4.3, pp. 465–466.]

The vanishing used in the four/five-space diagram must hold on the
whole punctured special fibre, or at every relevant strict generization;
vanishing at one point is insufficient. The later wording on 149 and
157 supplies that uniform premise. The construction also retains
H¹(I,Λ)=Λ(−1), rather than canonically trivializing the Tate twist.
The promised compatibility of cones remains a separate, bounded
follow-up task. [C-SA13-600,609–613; MP-SA13-194,242.]

### 3.4 Prime-to-p fundamental groups and stable marked curves

The subsequent pages distinguish an actual action from an outer action,
potential tameness from triviality, and finite generation from finite
presentation. SGA 7 I §§5.2–5.4 provides close published matches, with
the lecture explicitly dated 19 November 1968 and the volume published
in 1972. Orgogozo's later base-extension invariance is Corollary 4.5,
and finite presentation is Theorem 4.11. The broader excellent-base
nonabelian-depth proposal is retained separately. [C-SA13-607–608,614–626;
`RC_SGA7I`; `RC_Orgogozo2003`; `RC_MRaynaud1974`.]

The stable-curve deformation argument first reduces to a complete base
and uses a Cohen-ring map. Its formal deformation input belongs to
Schlessinger/Rim; its use in Grothendieck's SGA 7 I is not independent
authorship of that theorem. The node covers are T_i^m=t_i, with m
invertible, not T_i^m=0. Pullback of their Kummer classes gives the
valuation multiplicities in the product of commuting node monodromies.
The proposed fixed square of an ample bundle in the hyperplane step
is not proved by a sufficiently-large-power Bertini theorem.
[C-SA13-622,624–626; MP-SA13-195–196.]

## 4. Cote 34 appendices: envelopes, models, weights and GIT

### 4.1 Three group objects that must remain distinct

The appendix on analytic and algebraic envelopes studies a profinite
group through its finite-dimensional representations, then introduces
arithmetic model systems. With the forgetful fibre functor retained,
Tannakian reconstruction recovers the profinite component quotient.
The warning on scan 185 and the recovery formula on 186 cannot both
be repeated without explaining which information was forgotten.
[C-SA13-627–642; `RC_DeligneMilne1982`, Theorem 2.11.]

A rational component quotient does not imply that all its components
contain rational points. The normalizer of the norm-one torus for
Q₃(√3)/Q₃ has constant component quotient C₂, while a point in its
other component would require norm −1; reduction modulo 3 excludes
that norm. The proof checks the local-field and group hypotheses.
Likewise the arithmetic analytic pro-Lie algebra need not be infinitely
dimensional: for Spec(F̄_p), finite-field models give dimension one.
The corresponding algebraic envelope can have quotients of arbitrarily
large dimension through independent exponential characters. These
are different constructions. [C-SA13-635,647–648; MP-SA13-198–199;
`shards/root_codex/proofs.md`; `shards/p3/root_lie_audit.md`.]

The model-group Tate endomorphism question has a qualified affirmative
modern formulation. Tate's finite-field theorem, Zarhin's positive-
characteristic work, Mori's characteristic-two contribution recorded
by Moret-Bailly, and Faltings's characteristic-zero theorem supply the
field cases. Gajda–Petersen Theorem 2.3 gives the finitely generated
field statement and Lemma 3.4 the normal-base extension. Finite-
presentation descent then proves the stated arithmetic-model version.
It would be wrong to substitute ordinary geometric π₁ for that
pro-system. Lie-algebra centralizers additionally require a sufficiently
fine model to remove the finite component obstruction of the chosen
representation. Moret-Bailly XII §§2.4–2.5 calls Mori's contribution
unpublished; no invented first-circulation date is assigned to it.
[C-SA13-650–653; MP-SA13-200–201; `RC_Tate1966`;
`RC_MoretBailly1985`, pp. 244–245; `RC_GajdaPetersen2022`.]

### 4.2 Weight arguments and independence of ℓ

The final handwritten appendix contains three related spectral sequences.
For a proper normal-crossing Čech construction, weights give E₂
degeneration. For an open divisor complement, and for the stated
support version, a potentially nonzero d₂ survives and weights give
E₃ degeneration. The punctured projective line supplies an explicit
nonzero d₂. At the boundary q=0, the needed weight inequality must
also be checked; comparing only interior rows is insufficient.
[C-SA13-654,658–661; `RC_WeilII1980` §§3.3.4–3.3.6;
`shards/p2/weights_audit.md`.]

Arithmetic Rj_* at a crossing has one Kummer generator per divisor;
geometric nearby cycles impose the diagonal relation. In the trait
calculation with geometric special-fibre terms, the abutment is
cohomology over K^nr, not K and not K̄. The inertia exact sequence
has coinvariant term V_I(−1). The split Tate elliptic curve refutes
the assertion that both invariants and coinvariants of H¹ have weight
one: their weights are zero and two. This is compatible with the
correct monodromy-weight formulation. [C-SA13-661–663;
`Illusie1994`; `RC_Illusie2021`.]

Degeneration does not by itself give independence of the ranks of the
algebraic differentials. Van Dobben de Bruyn's Theorem 1 precisely
relates independence of cycle-class kernels, ranks of algebraic
correspondences and compact-support Betti numbers over F̄_p. It is
an equivalence of conjectural assertions, not their unconditional
proof. The current Wan–Zhang author text still records the general
singular/nonproper Betti-independence question as open. The October
2026 Ito–Zou preprint is recorded within its hyper-Kähler and numerical
hypotheses; it is not a resolution of general weight–monodromy.
[C-SA13-655,662; MP-SA13-202; `RC_vanDobben2020`, Theorem 1,
p. 3; `RC_WanZhang2025` §1.1; `RC_ItoZou2026`.]

### 4.3 The interleaved printed GIT faces

The English GIT pages interleaved with the weights appendix are reused
source material. The sign convention is μ=−min of the surviving
weights; strict numerical stability excludes the trivial one-parameter
subgroup. Their argument order differs from scan order. The 1982
Mumford–Fogarty comparator identifies Definition 2.2, Theorem 2.1,
Propositions 2.2–2.3 and the relevant valuation steps. The first
embedding reduction cites Theorem 1.19; the orbit-closure reduction
still cites Theorem 1.14. The two references must not be globally
replaced together. [C-SA13-664–670; MP-SA13-205;
`RC_MumfordGIT`; `shards/p4/git_collation.md`.]

The public reproduction has an OCR gap after printed p. 53. The
coordinate continuation and the body of Proposition 2.4 were therefore
not completely collated against that reproduction; Appendix 2A
confirms the proposition's identity but not the supposed p. 55
pagination. The supplied coordinate argument was independently
checked. Appendix 2A, p. 156, modifies the Iwahori lifting in positive
characteristic after a ramified extension. The comparator establishes
source concordance, not the date or authorship of the retained sheet.

## 5. Cote 36: Néron models, biextensions and the Griffiths argument

### 5.1 Pairings, torsors and invariant cycles

The early pages revise Néron-model arguments, pairings and torsors.
Draft proposition numbering on 36:003–008 is not silently equated
with published SGA 7 IX numbering. An early proposed deformation
counterexample remains explicitly a proposal unless its realization
has been proved. The comparison with 1-motives and biextensions is
made at the level of the actual finite or derived objects, not merely
their isomorphism classes. [p3 core claim and problem records;
`SGA7IX`; `SGA7VII`; `SGA7VIII`.]

The biextension construction continues across 36:052–059. Ext classes,
rigidified torsors and the Néron–Severi extension are consolidated
across that boundary. The quadratic identity has the required plus
sign. A doubled lift of the Néron–Severi class is conditional on its
separate compatibility, not supplied by simply multiplying a formal
extension class by two. SGA 7 VII §§2.9.4,2.9.6,3.6.5 and VIII
§§1.1–1.4 are exact comparison loci. The finite-level gluing problem
retains categorical data that a classification of isomorphism classes
alone would omit. [SA13-324,327,329; MP-SA13-134;
`P4_SGA7VII`, pp. 174,176,205; `P4_SGA7VIII`.]

The invariant-cycle programme connects vertical divisors, Picard
groups, torsion and orthogonal pairings. A kernel contained in the
torsion subgroup need not equal all of it. If its order is e, its
ℓ-primary part has order ℓ^{v_ℓ(e)}, not ℓ. The arithmetic inclusion
in IX §2.6(a) is weaker than the full orthogonal-complement equality
in the different henselian-trait setting of IX §2.4, where the toric part is the intersection of the fixed part with the orthogonal complement of the dual fixed part. P^τ and P⁰
are also not interchangeable in arbitrary dimension.
[C-SA13-415–439; MP-SA13-99,133; `P4_SGA7IX`;
`P4_Raynaud1970`.] The original IX formula 12.1.5 itself omits the
principal-fibre relation: the independently checked divisor group is
Z^I/Z(d_i), as used in C-SA13-415. The projective line over a trait
already detects that omission; the source audit records it explicitly.

The finite pairing can detect torsion invisible in a Tate module.
A finite extension carrying one point does not necessarily carry
a compatible division tower. That distinction is explicit in the
36:079–080 continuation and is merged with the earlier finite/Tate
warning while the two claims retain their own hypotheses. The weighted
curve pairing later in the package uses a symmetrized matrix D·u,
not u alone; comparisons with Bosch–Lorenzini are confined to the
specific component-group setting. [SA13-322; C-SA13-439;
`P4_BoschLorenzini2002` §§4.6–4.7.]

### 5.2 Primitive classes and high-degree sections

A36-01 and A36-02 develop the Griffiths argument through primitive
classes, Leray filtration, algebraic correspondences and high-degree
sections. SGA 7 XX explicitly credits Grothendieck's proof. The
canonical Leray class arises from the first filtration quotient;
its construction does not require degeneration of the entire spectral
sequence. Functoriality under correspondences supplies the necessary
compatibility. [C-SA13-325–327; `SGA7XX` §1.]

The algebraicity of an inverse Lefschetz operator is a separate
hypothesis. Hard Lefschetz supplies an inverse linear map, not a
cycle inducing it. The published theorem retains its pencil,
Lefschetz and algebraic-correspondence assumptions. A quotient of a
subgroup mapping onto primitive algebraic cohomology is not itself
a canonical injection in the opposite direction. The dossier
records the vector-space consequence separately from the geometric
map actually constructed. [p3 A36 claim records; `SGA7XVIII`
§§5.8.4–5.8.7; `SGA7XX` §§3.3–3.4,4.1,5.1.]

The strong trace assertion and its inserted subspace version are
not equivalent. On the trivial representation F_p^{p−1}, invariant
subspaces realize every trace residue through their dimensions, but
the only whole-space trace is p−1. Chebotarev on a fixed
representation does not convert a chosen subspace trace into a
whole-space trace. Katz's published generic nonnilpotence and
Koblitz's later stable-rank growth address related but weaker or
different statements; neither is labelled a proof of the every-
residue whole-space assertion. [C-SA13-343 and linked claims;
`SGA7XXI` §1.4, pp. 374–376; `Koblitz1975`, I §5,
Theorem 2, p. 141.]

### 5.3 An exact specialization counterexample and its repair

The arbitrary-point quantifier of A36 Lemma 7.8 is false as
transcribed. Take

\[
S=\operatorname{Spec}\mathbf F_3[x,x^{-1},y],\qquad F(v)=xv^3,
\]

with t the generic point of the integral curve
y²=x(x−2)² and s=(2,0). The ambient scheme is smooth and normal,
and the semilinear map is invertible on every geometric fibre.
Writing x=u² and y=u(u²−2) identifies the curve's function field
with F₃(u). The generic fixed vectors are 0 and ±1/u, so the
generic fixed representation is trivial. At s the nonzero fixed
vectors satisfy v²=2; Frobenius over F₃ acts by −1, giving image
C₂. Restricting the trivial generic representation to any open
subgroup cannot produce that special action.

The reduction to a normal generic-point situation fails because
the closure of t is nodal and nonnormal, despite normality of S.
Normalizing that curve changes the special residue field and kills
exactly the action at issue. A separate proof establishes the
generic-point repair using the finite part of the étale fixed
locus, a splitting torsor, normality and descent. The repair is
labelled the review's reconstruction; it does not change the ink.
[C-SA13-355,363; `Stacks0BTN`; `Stacks04GK`; `Stacks02LP`;
`shards/p3/code/specialization_counterexample.py` and its output.]

The finite-field nonconiveau deduction also needs fixed ambient
zeta factors. Stable rank growing beyond the bounded contribution
of those factors gives a useful contradiction under the stated
smooth finite-field hypotheses; nonnilpotence alone need not.
The norm-form construction and arbitrary-point-count interpolation
are independently checked, with explicit separation between the
general existence argument and the manuscript's sharper unverified
degree thresholds. No smoothness is claimed for that elementary
interpolation construction. [p3 review §§8–9; `SGA7XXI`;
`SGA7XXII`; `Koblitz1975`.]

## 6. Cote 39 and the other reused sources

Cote 39 studies subrings A_n of formal power series through closure
under substitution, an inverse-function condition H, Hasse divided
derivatives D, flows, Pfaff systems and preparation. These axioms
are the subject, not merely a primitive formulation of a later
named formalism.

H by itself does not reflect units back to A₀. The explicit family
A₀=Z and A_n=Z+(t_1,…,t_n)Q[[t_1,…,t_n]] supplies the checked
obstruction. Adding D changes the argument and permits coefficient
extraction; a polynomial-family counterexample to a stronger
faithful-flatness hope fails H and therefore does not refute H+D.
Likewise a formal flow or Baker–Campbell–Hausdorff series existing
in the ambient power-series ring does not prove that it belongs
to the chosen A-system. [C-SA13-443–470 and linked problem records;
`shards/p4/proof_audit.md`.]

The preparation argument can be formulated in a complete linear
topology with the appropriate unit-series factor. The exact
comparison with Strickland's preparation statements is given in
the records. A scalar factor and a unit power series are not
synonymous, and substitution of 1 into an arbitrary formal
variable is not an allowed continuous operation. The quotient
condition for a smooth formal equivalence relation is also
stronger than formal integrability of its ambient distribution.
No general classification of these A-systems is claimed from a
few established examples. [C-SA13-456,470–471,487–489;
`P4_StricklandFPFP` §§33.1–33.2; p4 formal-structure problems.]

The reused Haar-measure leaves are identified with Bourbaki,
Integration VIII §5, Propositions 1–7, first published in 1963.
Compact generation is essential in the indicated subgroup
argument. In the avoidance construction, Δ_U∩Δ_V=Δ_(U∪V), whereas
the inclusion ⋃_j Δ_Uj⊂Δ_(⋂_j Uj) supplies the needed proof step;
these two operations must not be interchanged.
The Lie and Čech leaves are audited independently: characteristic
zero is required for the exponential argument, as the explicit
derivation on F_p[x] demonstrates; exact sheafification supplies
the injective-preservation statement, while the surviving Čech
construction is left exact. Exact unidentified printed editions
remain unidentified. [C-SA13-410–411,474 and p3 Lie/Čech claims;
`P4_BourbakiIntegration78`; p3 review §7.]

## 7. What consolidation changed

Three recurrent errors in the earlier notes have been corrected.
First, a theorem-level phrase often suppressed a hypothesis that
the pages or proof needed: constructibility, properness, normality
of a closure, completeness, coefficient invertibility, a uniform
bound or a finite-component condition. Second, a later theorem
on the same subject was sometimes treated as the exact afterlife
of a stronger draft statement. Third, an earlier project's
vocabulary occasionally supplied an interpretation absent from
these pages. The records retain worthwhile observations from
those notes while separating their origin from the manuscript.

Semantic merging was performed only after comparing the actual
passages. The accepted aliases include the local-pairing
continuation, the common-completion lemma, the Ext/torsor/NS
continuation, finite-versus-Tate warnings, the Kummer construction,
and a repeated monodromy-exponent promise followed by its proof.
The global alias table records every decision and its audit.
Merged records retain source snapshots, separate occurrence
checks, separate page statuses and additional computation audits.
A broad thematic connection is a link, not an alias.

The most useful unresolved work falls into three categories:
exact companions to established constructions, sharply bounded
extensions whose full quantifiers were not matched, and historical
or textual identification. The ranked directions distinguish
those from genuinely general conjectural programmes such as
independence of ℓ or algebraicity of Lefschetz inverses. A problem
being “open on the pages” never means that it is open in 2026.
Likewise a bounded unsuccessful search does not establish novelty.
No claim is assigned class D merely because its first title search
failed.

The separate project table preserves the earlier notes' references
to La Longue Marche, Les Dérivateurs, S6, S19, LM7, LM4, LM7_PUSH,
WG, WG2 and the other named runs, with their source note IDs and
run names. The current-note endpoints were checked. The
underlying external research reports were not supplied; their
results are therefore attributed leads, not independently
verified mathematics. The main archive/published-work comparisons
were checked at both available endpoints. No unsupported status
from an earlier context register is promoted to a current result.

## 8. Evidence, verification and use of the files

Every claim has a recorded searched fate and a dated present
assessment. Searches were grouped by exact mathematical family,
not mechanically repeated for every reformulation. The search
logs record queries, databases or source collections, opened
comparators, and the resulting limits. They include SGA/EGA,
Numdam, arXiv, author bibliographies and primary papers, with
zbMATH and MathOverflow used for discovery and backward tracing
where relevant. An unlocated source is not replaced by a
remembered citation.

The bibliography's `note = {verified}` means that the cited URL
or DOI was actually opened. It does **not** mean that every page
of the work was read, that the proof was independently reproduced,
or that a metadata record establishes a mathematical theorem.
Additional access notes state whether the evidence was a full
text, a specific theorem, an introduction, a preview or metadata.
Unopened candidates retain `note = {unverified}`. Duplicate
bibliography keys were reconciled explicitly; the original access
audits remain in the review folders.

`CHECK_EVENTS.tsv` uses “GPT-6 Astra Pro; configured effort not
exposed” rather than inventing an effort setting. It distinguishes
source/summary comparison, reference access, proof checking,
independent reconstruction, use of a checked result, and executable
calculation. A source-reading event is explicitly not a proof.
The symbolic arguments in the review and proof files establish
universal claims; finite computations check exact examples,
indices, signs and identities at their stated scope. A finite
test grid is never presented as a proof of a deep theorem.

The main files are intended to be used together:

| File | Purpose |
|---|---|
| `SA13_entries.tsv` | Exactly one verdict per indexed Pro entry |
| `SA13_items.json` | Consolidated objects, source provenance, quotations, reconstruction and text checks |
| `SA13_claims.json` | Precise claims, page status, computations, searched fate, classes and references |
| `SA13_problems.json` | Every consolidated question or deferred step, its strongest supported formulation and current scope |
| `SA13_readings.tsv` | Scan-dependent alarms; no emendations |
| `SA13_links.tsv` | Archive, publication and attributed project connections |
| `SA13_project_links.tsv` | The project leads separately, without importing their conclusions |
| `SA13_aliases.tsv` | Semantic merge decisions and stable-ID redirection |
| `SA13_directions.md` | Ranked follow-on tasks with item/claim/problem origins |
| `SA13_references.bib` | References with actual access status |
| `CHECK_EVENTS.tsv`, `progress.log` | Verification scope and UTC work history |
| `shards/` | Detailed authored reviews, proofs, searches, local tables and original occurrence records |
| `code/`, `outputs/` | Assembly, integrity checks, computations and captured outputs |

An alias remains a valid historical locator into its original
review folder; use the global alias table for the canonical
record. Relative paths in p2/p3/p4 computation descriptions are
resolved against the `computation_base` supplied in the global
claim. Root computation dictionaries already use archive-relative
paths. The archive manifest hashes every included file. Original
attachments and external source PDFs/OCR are omitted; their
filenames, source hashes, retrieval evidence and exact locators
remain documented.

Structural validation checks coverage, unique IDs, source ownership,
required fields, scan/line boundaries, bibliography keys, search
links, computation files and event coverage. Those checks establish
the integrity of the register, not the truth of every mathematical
assertion. The latter rests on the individually recorded arguments
and source comparisons, including their explicit limitations.

## 9. Final counts and completion

Counts are for canonical global records after source-based consolidation. The
original occurrence records and aliases remain available. Bibliography counts are
keys, not distinct publications. The verdict is the
treatment of a note entry; it is not a count of false or retracted manuscript
claims. The page-status column and the literature class answer different questions.

| Register | Count |
|---|---:|
| Indexed Pro entries | 379 |
| Canonical items | 390 |
| Items with indexed Pro sources | 311 |
| Supplementary-only items | 79 |
| Canonical claims | 551 |
| Problems | 168 |
| Reading alarms | 337 |
| Ranked directions | 45 |
| All links | 318 |
| Separately retained project leads | 197 |
| Semantic aliases | 26 |
| Bibliography keys | 176 |
| Bibliography records marked verified (at recorded scope) | 166 |
| Bibliography records marked unverified | 10 |
| Check events | 1504 |

### Entry verdicts

| Verdict | Count |
|---|---:|
| kept | 304 |
| merged | 68 |
| corrected | 7 |
| withdrawn | 0 |
| rests on a misreading | 0 |

### Item kinds

| Kind | Count |
|---|---:|
| conjecture | 20 |
| unproved claim | 111 |
| unpursued implication | 39 |
| idea of the earlier run | 34 |
| reading question | 42 |
| self-flagged step | 77 |
| withdrawn in the same text | 20 |
| title, date or page count | 14 |
| other | 33 |

### Claims by literature class

| Class | Meaning | Count |
|---|---|---:|
| A | Identified in his own later published work, subject to explicit source-authorship qualifications | 126 |
| B | Developed by others into established results, including a proved negative resolution where specified | 120 |
| C | Partly developed; exact remaining scope or identification gap stated | 85 |
| D | Not developed after a documented search | 0 |
| E | Known beforehand or standard at the time | 170 |
| F | Not identifiable precisely from the pages | 50 |

Class D is zero: no bounded negative search has been promoted into a claim
that an idea was never developed. Class C includes explicitly distinguished
historical-identification gaps and stronger residual formulations; it is not
a count of newly discovered open conjectures.

### Claims by status on the pages

| Status | Count |
|---|---:|
| proved there | 65 |
| proof sketched | 196 |
| stated without proof | 150 |
| corrected by himself later | 16 |
| false as stated | 33 |
| open on the pages | 91 |

A merged claim can have a promise at an earlier occurrence and a proof sketch
later. Its `occurrence_statuses` retain that distinction; the table above counts
the canonical record once. The literature fate separately reports what is
known as of 19 November 2026.

All six requested stages are completed at the scope of the supplied sources:
379 individually reviewed verdicts; searched fates and computation/proof records;
a consolidated problem index; evidenced scan alarms without emendation; checked
available archive/publication endpoints with external project leads explicitly
qualified; and fully sourced ranked follow-on tasks. The final validation outputs
record the coverage and integrity checks. Remaining mathematical, bibliographical
and ink uncertainties are the stated findings of the review, not silently filled
gaps.
