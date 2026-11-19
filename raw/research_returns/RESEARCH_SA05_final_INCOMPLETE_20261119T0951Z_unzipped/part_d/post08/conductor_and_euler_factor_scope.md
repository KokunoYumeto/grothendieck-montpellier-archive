# Conductor and bad-Euler-factor routes to C.6

19 November 2026. Part D. These are source-scope checks and two proved
method diagnostics. They neither settle general C.6 nor establish an
equivalence between it and a stronger compatibility conjecture.

## 1. What a degreewise conductor theorem would supply

For a finite-dimensional quasi-unipotent representation V of the local
Galois group at residue characteristic p, with coefficients Q_l and l != p,
the representation-theoretic Artin conductor is

    a(V) = dim V - dim V^I + Sw(V).

Both summands are nonnegative. Thus a(V)=0 exactly when inertia is
trivial. A common Artin conductor for the realizations of the requested
pure motive would answer the unramifiedness question. It is necessary to
distinguish this conductor from an arithmetic model's Euler-characteristic
conductor.

A supplied homogeneous algebraic idempotent can remove alternating
cohomological degrees from a correspondence-compatible trace formula.
This possibility is retained throughout the present check. It does not,
by itself, change which numerical trace that formula computes.

## 2. Exact primary sources inspected

**Ochiai (1999).** The author version of *l-independence of the trace of
monodromy* has been opened and archived. The introduction, pp.1–2,
states the individual-trace conjecture and the alternating-trace result.
Corollary2.5 and its full proof, p.9, isolate individual degrees for
smooth proper surfaces and smooth complete intersections. Corollaries2.6–2.7,
pp.9–10, concern Swan conductors. They do not compute the tame term
dim V−dim V^I. The concluding averaging argument for Theorem2.4,
pp.8–9, was also read, but the complete preceding alteration proof was
not independently checked in this audit.

Primary URL: https://www.math.titech.ac.jp/top/~ochiai/lind.pdf.
Published metadata: *Mathematische Annalen*, 315(2), 321–340,
DOI10.1007/s002080050370. The DOI is confirmed in another opened
primary paper's bibliography; the publisher page itself was inaccessible.

**Dokchitser and Dokchitser (2025).** The accepted chapter has been opened
and archived. Theorem1.1 and its displayed proof, pp.1–2 and4, reconstruct
a semisimple Weil representation from appropriate Frobenius traces;
some finite-group ingredients are explicitly referred to an earlier
paper. Corollary1.3 and its full proof, pp.3 and5, give uniqueness.
Corollaries1.4–1.5, p.3, pass to Weil–Deligne representations only with
the stated weight–monodromy compatibility. They do not prove independence
of the required bad Euler factors. The pure/abelian application therefore
does not remove C.6's general monodromy issue.

Primary accepted text:
https://discovery.ucl.ac.uk/id/eprint/10205744/1/weil2-ems.pdf.
Publisher DOI10.4171/ECR/20/4; *Arithmetic of L-Functions*, pp.101–111.
UCL and EMS primary metadata were independently opened. Author-page
locators above are deliberately not relabelled as published-page locators.

**Kisin (2026).** The current Hexagon version1 of *Serre's conjecture on
the Artin character for a regular local ring*, dated28October2026, has
been opened and archived. Theorem1.1, pp.1–2, concerns the rational
character defined by isolated fixed-point lengths for a finite group
acting on a regular local ring. The introduction and the full graph-trace
Lemma5.2 with its proof, pp.13–15, were read. The formula is expressed
using two finite virtual representations obtained from periodized derived
inertia invariants of vanishing cycles. It is not an assertion about the
Artin conductor of each arbitrary pure generic-fibre summand. The full
18-page proof and its external categorical dependencies were not audited.

Primary URL: https://hexagonmath.org/pdf/2610.00597v1.
The submission page confirms the author, version and date.

**Beraldo and Pippi (2025).** The current arXiv version1 of
*Categorification of the localized intersection product and Bloch
conductor formula* has been obtained directly even though the web
renderer rejected its PDF endpoint. The introductory formulas1.1.5–1.1.7,
p.2, Theorem8.4.3 and its complete local proof, p.73, Lemma8.4.4 and its
local proof, pp.73–74, and the complete twisted construction8.5.1–8.5.6,
pp.74–75, were read. The twisted formula permits coherent kernels; it
uses traces over the derived inertia-cochain algebra. No full audit of
the preceding73pages or all external inputs is claimed.

Primary URL: https://arxiv.org/pdf/2511.10527v1.

**Beraldo and Pippi (2024).** The earlier *Proof of the Deligne–Milnor
conjecture*, arXiv version1, was obtained and archived. The introduction,
the definitions of the ordinary and categorical conductors in1.4–1.6,
pp.5–9, and the complete local proof of TheoremA in6.2, pp.52–53,
were read. The vanishing-cycle invariant is an Euler/Swan total dimension,
with derived-invariant module traces in its categorical expression.
This audit does not claim independent verification of the whole
foundational comparison or of the isolated-singularity theorem.

Primary URL: https://arxiv.org/pdf/2410.02327v1.

The two arXiv version histories were opened on19November2026 and still
list only version1. Retrieval timestamps, exact hashes, extracted text
paths and failures are recorded by
`code/fetch_conductor_scope.py` in `output/conductor_source_fetch.json`.
Raw PDFs remain outside the packaged research tree.

## 3. A homogeneous summand still has a monodromy-blind F-trace

Here is a direct algebraic check of the specific scalar trace in the
categorical formula. It addresses the projector issue rather than merely
observing that the original cohomology is alternating.

Let I be an inertia group and let V be a finite-dimensional unipotent
Q_l-representation. Write its action as exp(t_l N), where N is nilpotent.
Put

    F = RΓ(I,Q_l),       M(V) = RΓ(I,V).

The group-cochain cup action makes M(V) an F-module. The filtration
ker N ⊂ ker N² ⊂ ... ⊂ V is I-stable, and inertia is trivial on its
successive quotients. Applying RΓ(I,−) to each short exact sequence
gives an exact triangle of F-modules. For a quotient of dimension d
with trivial inertia, its derived invariants are F tensor Q_l^d.
It follows inductively that M(V) is perfect over F and

    [M(V)] = (dim V)[F]       in K0(Perf F).

The scalar trace of the identity on a perfect module is additive in
exact triangles. This can also be checked on a finite free resolution:
it is the alternating sum of the diagonal matrix traces. Consequently

    Tr_F(id,M(V)) = dim V.

More generally, let e:V→V be an idempotent commuting with I. Then
V=eV⊕(1−e)V as representations, so the trace of the induced idempotent
on M(V) is the trace of the identity on M(eV). Therefore

    Tr_F(e,M(V)) = dim(eV).

If V is placed in cohomological degree j, this becomes
(−1)^j dim(eV). The same calculation survives extension of scalars to
the two-periodic algebra Q_l[β,β^−1] used in the inspected sources:
trace commutes with that scalar extension. Nothing in this calculation
assumes e is a projector onto all cohomology of a variety; it already
applies to a supplied homogeneous summand.

An explicit model is the exterior differential graded algebra
F=Q_l[ε]/(ε²), |ε|=1, and the finite semifree module F tensor V with
d(v)=εNv. A homogeneous N-kernel filtration proves semifreeness.
Reduction along F→Q_l leaves V with zero differential. Thus this
augmentation trace records dim V, whereas the degree-zero cohomology
of the original two-term model is ker N. These are different operations.
This explicit model illustrates the filtration proof; no use of an
unproved global formality theorem is needed for that proof.

Take V=Q_l² and e=id. Compare N=0 with

    N(e2)=e1,     N(e1)=0.

The scalar F-trace is2 in both cases. Both representations are tame
and have Swan conductor0. Their inertia-invariant dimensions are2
and1, so their representation-theoretic Artin conductors are0 and1.
This is a formal local-representation example, not a pair of pure
geometric motives and not a counterexample to C.6.

The example can retain the entire ordinary Weil character. Take K=Q2,
l=3 and geometric Frobenius φ=diag(1,2) in the basis(e1,e2), with either
of those two operators N. Then φNφ^−1=N/2 in both cases, and the
underlying unramified Weil representations have the same characteristic
polynomial (T−1)(T−2). For the alternating matrix

    J = [[0,1],[-1,0]],

one has φ^t J φ=2J and N^t J+JN=0. Thus both have the same compatible
pairing multiplier and determinant weight2. The nonzero-N member has
one string with weights2,0 and centre1; the zero-N member has separate
centres0 and2. Only the former is weight–monodromy pure of weight1.
This reinforces why the formal pair is not a counterexample among
realizations of a fixed pure weight-one motive.

The conclusion is restricted to this additive scalar trace. The full
F-module retains the nilpotent differential, and may carry more
information. We have not shown that every construction using the
categorical object is monodromy-blind. What fails is the proposed direct
identification of this particular trace, even after a homogeneous
idempotent, with dim V−dim V^I.

## 4. The arithmetic model's conductor is not the generic conductor

Let R be a complete DVR with finite residue field and take the good
model P²_R. Blow it up at a rational closed point of its special fibre.
The generic fibre remains P²_K. Every generic cohomology representation
is unramified, so its representation-theoretic Artin conductor is zero.

The new special fibre has components Bl_point(P²_k) and P²_k, meeting
in P¹_k. Their geometric Euler characteristics are4,3 and2. Hence

    χ(new special fibre) = 4+3−2 = 5,
    χ(generic fibre) = 3.

The generic Swan term is still zero. Thus the scalar
χ(X_s)−χ(X_generic)−Sw(X_generic) is2 for the blown-up model and0
for the original good model, although the generic representations are
identical. The local blowup charts and two-component geometry are
proved in `../post07/bgv_semistable_blowup_diagnostic.md`.

The computation is compatible with the generalized Bloch formula: its
geometric intersection number is model-dependent as well. It simply
prevents replacing that formula's scalar by the generic representation's
Artin conductor. A correspondence-compatible refinement would still
need an additional argument identifying its invariant-cycle contribution
with the ordinary inertia-invariant dimension.

## 5. Remaining step

No opened result here proves a common value of
dim T_l(M)^I, or of a(T_l(M)), for an arbitrary pure algebraic-homological
or motivated summand at a mixed-characteristic place. Ordinary Weil
traces and their homogeneous-projector refinements leave the nilpotent
operator invisible. The new twisted formulas do not automatically fill
this gap. A different degreewise invariant-cycle comparison or a
pure-local realization of the earlier square-zero analytic encoding
would still be required. Neither has been established in this note.

## Independent checks

Part C read sections3–4 and the surrounding scope statements in full,
and independently passed the filtration, perfectness, scalar trace,
idempotent, periodization and model-blowup arguments. It did not
independently open the five primary sources. Root subsequently read the
entire note and passed the same proof, without claiming a new primary
PDF audit. Root also supplied and independently checked the explicit
Frobenius/pairing enhancement of the two-dimensional formal example;
Part D checked its matrices and weight centres when incorporating it.
