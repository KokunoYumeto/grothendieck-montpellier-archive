#!/usr/bin/env python3
"""Write the first formal movement review only once its scheduled time arrives."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,17,39,tzinfo=timezone.utc)
if now<due:raise SystemExit('Review is not yet due; nothing written.')
ledger=root/'PROGRESS_LEDGER.md'
heading='## Formal movement review 01'
if heading in ledger.read_text():raise SystemExit('Review 01 already recorded; refusing duplicate.')
entry=f'''

{heading} —19 November2026,{(now+timedelta(hours=1)).strftime('%H:%M')} Europe/Berlin

Actual review time:{now.isoformat()}. Scheduled first review:17:39UTC/18:39Europe/Berlin. We compare with the initial15:49Europe/Berlin ledger, including every intervening proved change. This is the first formal review, not a retrospective count of checkpoint updates.

**Movement:YES. Consecutive reviews without movement:0. Next review:18:39UTC/19:39Europe/Berlin.** Multiple initially open rows are now proved or refuted with complete proofs. The general torsion comparison has also been reduced to strictly narrower supported-cohomology and cyclic-torsor gates. Packaging, extra examples that leave a gate unchanged, and unsuccessful source searches do not contribute to this decision.

### Main questions and their strongest established state

| Main question | Present state and exact theorem/reduction |
|---|---|
| A.1/L2 | Literal unrestricted global isomorphisms refuted in every stable positive-complexity type. The exact Jenkins–Strebel support domain, invertible tangent map, retained-normalization fibre fundamental group, and moving-cap inverse are proved; the local plumbing comparison is derived from opened primary sources. A:04, A:alltypes, A:graph-radius-domain, A:graph-pi-one, A:EarleMarden-local, A:hinich-explicit. No unresolved main-question gate remains at this stated scope. |
| A.2–A.5 and A.7/L3–L5,L7,L9 | Every requested clause has a complete scoped proof or explicit refutation and repair, including zero-weight cap limits, collar counterexamples, slit fold conditions, characteristic5, and real elliptic edge cases. Exact clause-to-statement mapping is in the report. |
| A.6/L6 | Canonical normal compactification exists intrinsically and functorially for every characteristic-zero hyperbolic polycurve. Stated arithmetic reconstruction hypotheses are retained; Hoshi supplies arbitrary polycurves through dimension4. The graph/tensor, inertia, NB and presentation assertions have proved or refuted scoped answers. A:polycurve-coarse-compactification, A:intrinsic-anabelian-compactification, A:polycurve-four-dimensional-anabelian, A:arithmetic-quilts, A:real-Galois-obstruction. |
| B.1/L1 | Characteristic-zero fourfold numerical/homological agreement proved; positive-characteristic abelian fourfold conclusion derived with explicit2026-preprint dependency. The exact necessary-and-sufficient class for the same positivity argument and finite-image classes are stated. First question of24 refuted. B:charzero, B:abelian, B:criterion, B:tau. |
| B.2 | Completely specified nontorsion Albanese-kernel cycle and square refute both assertions; kernel-generation replacement proved. B:square, B:alb-kernel. |
| B.3 other than the open rows below | All28 subjects and9Pour-mémoire entries have exact scoped source locators. Finite-flat degree-one groups are identified by Nori; an explicit smooth genus-two example refutes arbitrary algebraically closed base extension. B:nori-finite-flat, B:nori-base-change-counterexample. The finite-polyhedral local-Hurewicz claim is refuted with an exact conical repair. |
| B.3/subject21 | Unrestricted coefficients refuted twice, including constant integers. UniversalH0 gives all torsor injectivity and full finite-étale faithfulness. For qcqs pairs, full torsion comparison is equivalent to supported-cohomology vanishing in degreesq≥2; degree2 is equivalent to extending cyclic prime-power torsors on all finite finitely-presented covers. Affine closed subschemes in quasi-separated pairs and separated finite-type henselian-DVR models are proved positive classes. The independently audited note B:henselian-local-flat-proper additionally proves properness and comparison for all flat separated finite-type models over positive-dimensional henselian noetherian local bases. This is a strict reduction of the initially unrestricted gate, not a complete settlement. |
| C.1–C.2/L8 | All literal tasks proved or refuted with exact repairs, finite certificates, nonnoetherian/infinite edge cases and actionwise module-functor criteria. No further open task introduced beyond the prompt. |

### Every current open row

| Open row | Status | Exact remaining gate | Tried; failure; next approach |
|---|---|---|---|
| B.3/subject11: morcelés | Historically unidentified; incomplete | Open a primary defining passage for the intended category, sufficient to state a theorem with the manuscript's actual quantifiers. | Cote91 and102 scans, Néron/Serre and surrounding notes checked. A tempting reading on91/130 is application ensembliste, not the sought term. Nearby finite-partition constructibility does not determine a category. Continue contemporaneous defining-source search. |
| B.3/subjects15–16: higher infinitesimal homotopy | Degree-one finite-flat part identified; higher general-topos part incomplete | Identify Grothendieck's intended higher construction and compare it with an actually proved source theorem. |1959 correspondence/SGA1 determine degree-one torsors. Nori plus Pauly settle a precise degree-one construction/base-extension question. Toën's schematization is not silently substituted for the unidentified higher functor. Next: exact Pursuing Stacks historical passages and their definition dependencies. |
| B.3/subject21: general nonproper torsion | Open in the remaining generality | For every qcqs universalH0 closed pair and torsion étale sheafG on its complement, proveH^q(X,j!G)=0 forq≥2, or construct a completely verified counterexample. The degree2 test is cyclic prime-power torsor extension on all finite finitely-presented covers. | Affine, proper, affine-closed, henselian-DVR, flat separated finite-type henselian noetherian local-base, and stated proper-closed-fibre classes are proved. Henselized affine-cover descent fails termwise: a fully explicit self-intersection has a clopen component missing the closed fibre; certificate in B_henselized_affine_descent.md. A doubled-local conditional counterexample reduces construction to a strictly henselian local ring with connected localization and a disconnected Jacobson-closed overlap; no actual such ring is supplied. Next: attack this ring gate or establish extension beyond the proved positive classes. |
| B.3/subject21: Gabber1994 original source | Original derivation not certified | Open the actual original comparison theorem and the definitions/dependencies needed to derive the stated affine result; a sufficient public original preview would count. | Publisher abstract/cover, repository searches, restricted archive and authentication redirects do not expose the required theorem. Full modern proofs are opened and cited separately. Continue authorized public original-source search; no invented full-volume access requirement. |
| B.3/subject21: Fujiwara1995 original source | Original derivation not certified | Open the actual original comparison theorem and the definitions/dependencies needed for the stated derivation. | Euclid is an Incapsula shell; exact archive issue restricted; public bibliographic records do not show proof text. Fujiwara1998 gives a genuine short outline but does not certify the original1995 derivation. Continue authorized public original-source search. |

### Review discipline

The manuscript, report and canonical register preserve all unresolved hypotheses. The Jacobson-overlap construction is conditional, not a counterexample. The original-source access limitations are separate from mathematical proof by modern sources. The flat-local-base theorem B:henselian-local-flat-proper was independently audited before this review; its complete proof is preserved in notes while main-TeX integration follows the compilation freeze. Other note-level candidates are not counted as established without an actual independent audit. The report remains INCOMPLETE.
'''
ledger.write_text(ledger.read_text()+entry)
record={'review':1,'due_utc':due.isoformat(),'actual_utc':now.isoformat(),'baseline':'initial15:49Europe/Berlin ledger','movement':True,'consecutive_stagnant_reviews':0,'open_rows':5,'next_review_utc':'2026-11-19T18:39:00+00:00','next_checkpoint_utc':'2026-11-19T18:24:00+00:00'}
(root/'logs/progress_review_01.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
