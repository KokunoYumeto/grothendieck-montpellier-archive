# All-dimensional endpoint lifting: proof and source scope

Owner: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, run /root/real_weil,
RESEARCH_SA06; the inherited effort setting is not separately exposed.
Date: 19 November 2026.

## Current mathematical scope

The complete draft is C3_all_dimension_endpoint_draft.tex, equations
AE.1–AE.14. It assumes an actual regular projective modification of an
algebraizable excellent henselian coefficient-field local scheme, an
effective exceptional Cartier divisor with full support, and ample
conormal. Its dimension is arbitrary, at least two. The reduced support
may be singular and need not have normal crossings.

It proves endpoint lifting for actual perfect gamma-top classes on the
exceptional divisor times a fixed smooth proper curve. It then identifies
ordinary top Chow relations with the intrinsic exceptional perfect-family
relation group. It does not lift a prescribed entire family, prove
vanishing of the negative-K obstruction on the whole product, supply
arbitrary-dimensional resolution in positive characteristic, or compute
the remaining intrinsic exceptional relation group.

This file does not promote or register the draft. Root's complete review
and the scope decision are pending at the time of this initial record.

## New exact primary input

**Bruns, W., & Vetter, U. (1988). _Determinantal rings_ (Lecture Notes in
Mathematics, Vol. 1327). Springer. https://doi.org/10.1007/BFb0080378**

The complete 244-page author-hosted, publisher-authorized PDF was opened:
<https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf>.
Read the natural dual-Koszul construction in Section 2.C, printed
pp.16–18; Theorem2.16, printed p.18; its reduction to split exactness;
and Propositions2.17–2.18 with the proof through printed p.20.
Theorem2.1 and its complete proof, printed pp.10–11, were also
opened and read to make the opposite determinantal height bound
explicit in the expected-grade verification (turn973937492view0).
The exact hypothesis is a noetherian ring and a maximal-minor ideal of
grade n-m+1. The output is an actual finite free resolution and a
perfect quotient, not merely an equality in coherent G-theory.
The acyclicity criterion16.16 is a cited antecedent within that proof;
its deeper foundation is not represented as newly independently proved.

Owner retrievals include turn449900537view0–3. The DOI and volume/year
were separately verified against the publisher's metadata at
turn876009558search0. The original Eagon–Northcott1962 article
DOI10.1098/rspa.1962.0170 was not obtained: publisher access failed.
No claim of an original-paper inspection is made.

Retained local source:
research/sources/bruns_vetter1988_determinantal_rings.pdf,
1,265,993bytes, SHA256
cd2934d1799e64067ebce0e230dd5b08579db3a390ad7b293bf011541831cd33.
Acquisition script and timed manifest:
code/acquire_determinantal_source.py,
output/determinantal_source_manifest.json; completed17:18:58.904283UTC,
8.00579173299775seconds.
Bibliography: C3_all_dimension_endpoint_references.bib,
key D_BrunsVetter1988Determinantal.

The manuscript explicitly uses dual symmetric powers in the natural
complex. It does not identify divided and ordinary symmetric powers in
small characteristic. The determinant/gamma identity is proved directly
by the partial alternating binomial identity after the injective
flag-bundle splitting principle. No associated-graded injectivity is
inferred from that splitting.

## Exact previously audited inputs reused

C3_endpoint_family_SOURCE_AUDIT.md retains the fresh WeibelII
gamma-dimension theorem in its singular quasiprojective scope, the
rational Chern-character source, and all seven exact Stacks
Serre/Picard-thickening/GAGA/Popescu/completion/finite-descent/henselian
specified-point sources. Their proofs were read in the immediately
preceding endpoint investigation. This draft reuses those inputs rather
than claiming a new opening of each one.

FF.4 is the dimension-free actual point restriction isomorphism proved
from KST, levelwise Geisser–Hesselholt nilpotent invariance, and
Drinfeld's henselian-local K-minus-one vanishing. Both the original
FF proof and the later EP proof are reused with their precise scope.
The latter proof's finite-model Chern-character justification remains
necessary in the all-dimensional statement.

## Independent full reviews actually read by the owner

* Cycles completed the full AE.1–14 proof/source check at17:17:21UTC:
  ../cycles/C3_all_dimension_endpoint_independent_REVIEW.md,
  with matching canonical events. The full Bruns–Vetter construction
  and proof were freshly opened. No program was rerun.
* Frobenius finished the complete mathematical reading at17:17:08UTC
  and the primary-source reading by17:18:30UTC:
  ../frobenius/C3_all_dimension_endpoint_independent_REVIEW.md.
  The exact construction and Theorem2.16 proof were freshly opened.
  No computation or build was rerun.

Both reviews were read in full by the owner. The reported minor literal
comma in AE.3 was replaced by explicit multiplication, and the optional
componentwise rank clarification was added. Neither changes the proof.
These are independent agents in the same research run; no different
underlying model or independent historical discovery is claimed.

## Finite certificate and formatting scope

code/check_all_dimension_endpoint.py checks the exact elementary-
symmetric coefficient vectors of the Eagon–Northcott/gamma identity
for ranks1–18 and every permissible gamma degree, deeper-rank avoidance
and flag dimension for d1–32, exact rational top-Adams projectors through
d32, and bounded Cartier-series counts. It produced1,323passes,
0failures in0.018226574997243006seconds, completed17:17:14.299866UTC.
Full vectors and each exact case are retained in
output/all_dimension_endpoint_certificate.json.
It does not certify stratified Bertini, grade, formal existence,
approximation, or the complete geometric theorem.

code/compile_all_dimension_endpoint.py ran four standalone TeX/BibTeX
passes, all exit0 and no overfull/undefined diagnostics, in
2.5809856729974854seconds, completed17:17:16.864873UTC.
Every command's output is retained under timestamped names and
output/compile_all_dimension_endpoint.json. This formatting check
precedes the harmless AE.3 multiplication-spacing repair.
No mathematical conclusion is inferred from compilation.

## Final promotion, 2026-11-19T17:26:43.079342+00:00

Root completed the full mathematical and fresh exact Bruns–Vetter source audit, read both peer receipts, and inspected the full program plus aggregate certificate scope without rerunning it. Statement C.3bn is finalized at C3_all_dimension_endpoint.tex. The entire audited draft is retained in output/C3_all_dimension_endpoint_audited_draft.tex; the old draft is a comment-only pointer. No hypothesis was removed at promotion. The bundle includes it immediately after root’s C.3bm. The earlier pending-status paragraph is historical and superseded by this approval.

Final promoted-version standalone completed 2026-11-19T17:26:56.278579+00:00; four passes all exit0, no diagnostics, runtime 3.1026047529958305seconds. The previous draft build JSON is retained separately.
