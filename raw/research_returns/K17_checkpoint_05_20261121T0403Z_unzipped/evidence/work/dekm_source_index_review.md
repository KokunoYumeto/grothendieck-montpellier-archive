# DEKM endpoint review and repaired K12 criteria

Date: 2026-11-21 UTC. Agent: /root/tripod_integral.
Model: GPT-6 Astra Pro; reasoning effort not exposed.
Status: complete source and degree check; no independent proof found for the
rank-eight degree-five endpoint. The strengthened criterion and the local
double-building repair are deductions with explicit hypotheses.

## Checkpoint locator summary

In the current author PDF, §1.1 p.3 and §1.2.1 p.4 define the
projective cells; Proposition1.5 p.5 gives their Steinberg shift;
Definition2.1 p.6 defines cone rank. Table3 p.14 counts cone ranks,
whereas Proposition4.3/Table4 p.15 uses the projective cell notation
with those same numerical column labels. Theorem4.5 p.16 announces
the one-degree-larger endpoints, and Table5 p.17 imports them.
The forced conversion is d=r−1 and q=r−N. Thus the documented direct
ranges are q≤4,2,1 for N=8,9,10. The needed rank-eight group has
q=5, d=12, r=13. MPP CorollaryE p.7 independently supplies H2(GL10)
integrally. The existing rank-nine double-building degree10 hypothesis
supplies H3(GL9) conditionally, as proved below. No independent
replacement for H5(GL8) was located; retain it explicitly.

## 1. Forced degree conversion

Write N for lattice rank, r for the dimension of the linear span of the
rank-one forms, d for projective Voronoi degree, and q for Steinberg
homological degree. The definitions and the comparison give

    d = r−1,       q = d−N+1 = r−N,       r = q+N.

The first equality follows by intersecting the positive cone with trace=1.
The second is DEKM Proposition 1.5. Orienting the linear cone span instead
of its trace-one section changes neither the stabilizer's orientation sign
nor this degree shift, because the radial line has a fixed positive orientation.

The current author version's Table 3 is indexed by cone rank. Table 4 copies
those counts into columns described as projective cell dimensions. Its
rank-eight first entry counts the thirteen configurations with eight
independent minimal pairs, whose projective dimension is seven, not eight.
The exact first-record check already performed by vandiver confirms that
the file n8_rnk12 has a record of quadratic rank twelve and projective
dimension eleven. I read that check's complete script and result; I did
not rerun the complete source enumeration.

| Group | Projective degree d | Required cone rank r | Posted endpoint | Consequence |
|---|---:|---:|---:|---|
| H4(GL8;St8) | 11 | 12 | n8_rnk12 | Within documented enumeration |
| H5(GL8;St8) | 12 | 13 | n8_rnk12 | One cone rank beyond it |
| H2(GL9;St9) | 10 | 11 | n9_rnk11 | Within documented enumeration |
| H3(GL9;St9) | 11 | 12 | n9_rnk11 | One cone rank beyond it |
| H1(GL10;St10) | 10 | 11 | n10_rnk11 | Within documented enumeration |
| H2(GL10;St10) | 11 | 12 | n10_rnk11 | One cone rank beyond it |

Taking the reported enumeration and orientation calculations as inputs,
their corrected direct ranges are q≤4 at N=8, q≤2 at N=9, and q≤1
at N=10, after the usual small-prime localization. This statement does
not claim that all 50,645 rank-eight records were independently recomputed.

## 2. Announced theorem versus checked source mechanism

DEKM Theorem 4.5, author p.16, explicitly announces projective homology
vanishing through degree12 at rank8 and through degree11 at ranks9,10.
Corollary5.1 and Table5 use that announced range. Thus the paper really
does assert all three endpoint groups in the table above vanish.
The source-index conflict identifies a gap between the displayed
enumeration/orientation argument and those endpoints. It does not prove
the announced endpoint vanishings false.

Freshly checked primary locations:

- Current author PDF, linked as the more recent version on Martinet's
  publication page:
  https://jamartin.perso.math.cnrs.fr/Publications/DEKM.pdf .
  Definitions §§1.1–1.2.1, Proposition1.5, Definition2.1,
  §§3.2–3.4, Tables3–4, Propositions4.3–4.4, Theorem4.5,
  Corollary5.1 and Table5 were read.
  Retrieval refs: turn248314379view0; turn226928436search5.
  Local PDF/text: work/k12_source_data/dekm_author_current.pdf/.txt.
- Earlier author PDF:
  https://jamartin.perso.math.cnrs.fr/Publications/DEKM_arXiv.pdf .
  It retains the same endpoint announcement and labels;
  retrieval ref turn226928436search4.
- arXiv https://arxiv.org/abs/1910.11598 currently exposes only v1,
  submitted25October2019; retrieval ref turn279805313view1.
- The publisher's article is DOI10.1017/S1474748025101394,
  J.Inst.Math.Jussieu25(2026),565–590, online24November2025.
  Its public metadata shows no linked correction found in this search;
  full-page retrieval redirects to the abstract.
  Retrieval refs turn279805313view0 and turn437663408view2.
- Author publication pages were checked for a listed correction:
  https://jamartin.perso.math.cnrs.fr/Publications/
  and https://mathieudutsik.github.io/Publications/index.html .
  Retrieval refs turn437663408view1 and turn437663408view3.
- The official repository tree archived in
  work/k12_source_data/voronoi_repository_tree.json stops at the
  ranks shown above. GitHub issues retrieval was blocked
  (turn437663408view0), so no conclusion about unseen issues is made.

Searches for an erratum, corrigendum, index correction, higher-rank
Steinberg endpoint calculation and later independent vanishing theorem
found no replacement proof of H5(GL8;St8)=0 over Z[1/13!].
This is a report of the search, not a proof that no such result exists.
An additional round of exact-group, correction and later-cohomology
searches at 03:00 UTC gave the same outcome (refs turn648672647search0--8,
turn967167647search1,3,35). The MPP author PDF again concerned only
the new degree-one and degree-two unconditional results.

## 3. Independent resolution of the rank-ten degree-two endpoint

Miller–Patzt–Putman, arXiv2509.01559, Corollary E, printed p.7,
states H2(GL_n(Z);St_n⊗F)=0 for n≥8 over every commutative ring F.
Its weaker localized range is n≥6 when2and3are invertible.
Thus H2(GL10;St10) vanishes integrally, independently of the DEKM
indexing issue. The same theorem supplies the rank-eleven term in
the K12 argument. Remark1.18's localized earlier result was also
reread. Corollary E proves only degrees1and2, so it does not repair
H3(GL9) or H5(GL8) unconditionally.

Primary: https://arxiv.org/abs/2509.01559 .
Fresh retrieval: turn345524656academia9; current arXiv history rechecked
as v1 only, 1 September 2025 (turn591975731view0); the current author
PDF https://academicweb.nd.edu/~andyp/papers/ReductiveSteinberg.pdf
retains the same 74-page text (turn591975731view1). Local primary
work/steinberg_integral_mpp_2025.pdf/.txt.
The field-group theorem of Ash–Putman–Sam, arXiv1704.08344, does
not apply to GL_n(Z); it cannot supply these integer-group endpoints.

## 4. Repair of the double-building argument without new building hypotheses

The earlier DB proof used rank9 homology through degree3 from Table5.
That endpoint is outside the corrected documented range. However the
existing hypothesis H~10(T²(Z9);R)=0 proves it directly.

MPP Theorem23.3 identifies H_i(S_*) with H~_(i+N−1)(T²(ZN)).
Theorem D' makes S_* exact at S_−1,S0,S1. At N=9 the stated
H~10 hypothesis adds exactness at S2. Use S3→S2→S1→S0→St9→0
and append ker(S3→S2) in degree4. This is an exact R-free resolution.
Its hyperhomology first page in columns0through3 is the ordered
decomposition formula from the existing DB proof.

In total degree3 every factor rank is at most8. The verified low-rank
data through q3 have only (rank,q)=(1,0),(3,3),(4,3) nonzero, each R.
All-rank-one factors require q0,p3 and therefore have total rank5.
A single degree-three factor requires q3,p0 and has total rank at
most4+1=5. Neither can have rank9, so the diagonal is zero and
H3(GL9;St9⊗R)=0 under that existing DB hypothesis.

Now the rank9 degree4 argument uses only ranks≤8 through q4,
within the corrected range. The rank10 degree3 argument uses the
rank9 degree3 vanishing just derived. Thus all three original
building hypotheses still suffice for the two rank9/rank10 target
groups, without invoking the unsupported unconditional rank9 endpoint.
They imply K12=0 once H5(GL8;St8⊗R)=0 is also assumed.

## 5. Strengthened K12 gate

A source-independent use of the questioned endpoint is avoided by retaining
the following three explicit hypotheses over R=Z[1/13!]:

    H5(GL8;St8⊗R)=0,
    H4(GL9;St9⊗R)=0,
    H3(GL10;St10⊗R)=0.

All are projective Voronoi degree12 (cone rank13).
They imply K12(Z)=0 by the already checked rank spectral-sequence
and Hurewicz proof. The only correction is that the rank-eight term
on total degree13 is now an explicit hypothesis instead of an
unverified endpoint input.

For the remaining low-rank diagonal I freshly checked the original
Elbaz-Vincent–Gangl–Soulé primary paper, *Perfect forms, K-theory and
the cohomology of modular groups*, Adv.Math.245(2013),587–624:
https://www.ihes.fr/~soule/documents/YAIMA4438.pdf .
Theorem4.3, printed p.597, gives H12(VorGL7)=Z modulo S7 and
H12(VorGL5)=H12(VorGL6)=0 after small-prime localization.
Ranks≤4 have no projective degree12 cells. Theorem8.1, p.604,
also gives the rank3/rank4 degree3 Steinberg classes used in DB.
Retrieval refs turn201580776view0, turn412034402view0 and
turn412034402view1. This checks the precise cited source claims;
the underlying large computations were not rerun.

Clean strengthened statements and proofs are in
work/k12_index_safe_section.tex, ID K17-K12-THREE-RANKS. The earlier
K17-K12-TWO-RANKS may be retained explicitly as an implication using
DEKM's announced H5(GL8) input, rather than representing that endpoint
as independently verified. The repaired original DB proof is in
work/k12_double_building_section.tex; its K12 consequence now includes
the rank-eight hypothesis. The earlier audit records are preserved as
historical events and receive a follow-up scope note.
