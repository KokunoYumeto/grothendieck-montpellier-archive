#!/usr/bin/env python3
"""Record formal review02 at or after its scheduled time, never earlier."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 19, 18, 39, tzinfo=timezone.utc)
if now < due:
    raise SystemExit("Review02 is not yet due; nothing written.")
ledger = root / "PROGRESS_LEDGER.md"
heading = "## Formal movement review 02"
old = ledger.read_text()
if heading in old:
    raise SystemExit("Review02 already recorded; refusing duplicate.")
entry = f"""

{heading} —19 November2026,{(now+timedelta(hours=1)).strftime('%H:%M')} Europe/Berlin

Actual review time:{now.isoformat()}. Scheduled review:18:39UTC/19:39Europe/Berlin. We compare with formal review01 at17:39UTC; checkpoint05, independent rechecks and the new scoped catalogue theorems do not themselves count as movement.

**Movement:YES. Consecutive reviews without movement:0. Next review:19:39UTC/20:39Europe/Berlin.**

### Actual movement since review01

The previously open unrestricted qcqs torsion-comparison row is now **refuted with a complete counterexample**, with positive replacement classes retained. Lemma C:Nagata-input uses the original1952 construction together with its essential1955 correction; Lemma C:Goldman-branches constructs the required strictly local ring and branch overlap; Theorem C:subject21-torsion-counterexample verifies every hypothesis of the doubled scheme pair and proves failure for every constant finite cyclic coefficient of order greater than one. Root, B, C and A567 independently audited the exact construction. The finite endpoint/idempotent certificate is explicitly limited to its finite algebraic checks; the infinite construction has its written proof. This changes the open mathematical row to a proved refutation.

The independent separated finite-type positive theorem was also strengthened from the special local/flat setting to arbitrary noetherian henselian ring pairs: C:local-curve-avoidance, C:henselian-horizontal-proper, C:henselian-noetherian-pair-comparison and C:henselian-noetherian-closedpoint-criterion. That strict reduction was proved and audited after review01. Neither this positive class nor the counterexample supplies the still-unread original Gabber/Fujiwara theorem passages.

The subject15 historical-identification obligation was removed by a separate **scope correction**, recorded at18:18UTC: the literal B.3 task permits the strongest proved theorem with its locator. The scoped higher-homotopy results already satisfy that alternative, while the identity of the unspecified1964 construction remains honestly undetermined. This correction of an added obligation is **not counted as mathematical movement**. The subsequent Mondal–Reinecke comparisons are additional known scoped results and likewise do not reset the stagnation count.

### Main questions and their strongest established state

| Main question | Present state and exact gate |
|---|---|
| A.1/L2 | The unrestricted global isomorphisms are refuted with their full stated stable-type scope. The exact support domain, tangent and fundamental-group comparison, moving-cap inverse and local plumbing identifications are proved. A:04, A:alltypes, A:graph-radius-domain, A:graph-pi-one, A:EarleMarden-local and A:hinich-explicit. No unresolved A.1 gate remains in the literal task. |
| A.2–A.5,A.7/L3–L5,L7,L9 | The complete scoped proofs, explicit counterexamples and corrected replacements recorded in review01 remain established; the report maps every lettered clause to its numbered statement. No new undecided clause is introduced. |
| A.6/L6 | The intrinsic compactification, stated arithmetic reconstruction classes, graph/tensor and inertia scope, NB and presentations retain the exact proofs and limits recorded in review01. A:polycurve-coarse-compactification, A:intrinsic-anabelian-compactification, A:polycurve-four-dimensional-anabelian, A:arithmetic-quilts and A:real-Galois-obstruction. |
| B.1/L1 | Characteristic-zero agreement, the positive-characteristic abelian-fourfold result with its explicitly stated2026-preprint dependency, the exact positivity criterion and first-question refutation remain established. B:charzero, B:abelian, B:criterion and B:tau. |
| B.2 | Both assertions remain refuted by the explicit nontorsion cycle/square and Albanese calculation, with the proved kernel-generation replacement. B:square and B:alb-kernel. |
| B.3/subject21 mathematics | Arbitrary coefficients and unrestricted qcqs torsion comparison are refuted, while affine, proper, affine-closed-fibre and the arbitrary noetherian henselian-pair separated finite-type classes are proved. C:subject21-torsion-counterexample and C:henselian-noetherian-pair-comparison close the former mathematical gate. The two explicitly requested original-source derivations remain separate requirements below. |
| B.3 catalogue | The scoped statement/locator alternative is implemented for all subjects and Pour-mémoire entries except the unrecognized category clause of subject11. Its adjacent Néron clause has a scoped modern representability theorem; a newly located archival definition is being checked before claiming that it identifies the historical functor. In subject15 the integral affinization, unipotent homotopy and formal comparison theorems have explicit scopes and do not assert a retrospective identity of constructions. |
| C.1–C.2/L8 | All requested algebra, functor, finite/discrete group, rearrangement and symmetry clauses retain their complete proved/refuted answers and finite certificates, including the required nonnoetherian and infinite cases. |

### Every actual residual row

| Open row | Status | Exact remaining requirement | Attempts, obstruction and next approach |
|---|---|---|---|
| B.3/subject11: category clause and historical functor identification | Historically unidentified; incomplete | Recover a primary definition of the objects and morphisms called schémas morcelés, or an explicit contemporary comparison that makes a genuinely relevant structures/group-objects theorem applicable; check the relation to the adjacent Néron functor. | Cotes91/102 and adjacent material, Néron/Serre, SGA3 and correspondence searches give nearby constructible categories but no verified identification. A newly opened Hrushovski draft quotes Grothendieck's17June1979 letter to Poizat and explicitly describes a piecewise-morphism category; the full original letter and its relation to1964 remain unverified. A bounded search of Michel Hua's project locates a candidate Néron-functor definition on cote43, original folios91–97, through finite constructible partitions. The original scans are being retrieved, so the modern transcript is only a search aid. Continue these concrete primary leads and inspect the relevant constructible-group theorem. |
| B.3/subject21: Gabber1994 original | Source derivation not certified | Open the necessary original theorem passage, its exact hypotheses and required definitions/dependencies; derive the scoped affine conclusion. An adequate original preview would suffice. | Full modern proof is opened; publisher/author-profile/index/collection/public-repository routes expose metadata, abstract or access controls. The exact OpenAIRE record is CLOSED with no repository copy. No original theorem was obtained. Continue materially new authorized public original-source routes. |
| B.3/subject21: Fujiwara1995 original | Source derivation not certified | Open the necessary original comparison passage, its hypotheses and required definitions/dependencies; derive the scoped punctured conclusion. | Full modern proof and the distinct1998 author restatement/outline are opened. Exact Euclid, catalogue, repository and author-profile routes have not exposed the1995 theorem. ResearchGate explicitly has no full text. Continue materially new authorized public original-source routes. |

### Continuation and stopping rule

There are exactly **three actual residual rows** at this review. The report remains **INCOMPLETE**. No theorem source is marked opened solely because its bibliographical record or a later quotation was read. We continue research, with the next checkpoint due19:09UTC/20:09Europe/Berlin and the next formal movement review due19:39UTC/20:39Europe/Berlin. If two consecutive later formal reviews record no qualifying movement, the user's stopping rule requires the final package; packaging and repeated gate descriptions will not be counted.
"""
ledger.write_text(old + entry)
record = {
    "review": 2, "due_utc": due.isoformat(), "actual_utc": now.isoformat(),
    "baseline": "formal review01 at2026-11-19T17:39:12+00:00",
    "movement": True, "consecutive_stagnant_reviews": 0, "open_rows": 3,
    "movement_evidence": [
        "C:subject21-torsion-counterexample closes previously open general torsion row",
        "C:henselian-noetherian-pair-comparison is a strict proved extension of the positive class"
    ],
    "not_counted": [
        "subject15 literal-scope correction", "additional known scoped catalogue theorems",
        "independent rechecks", "source-access failures", "checkpoint packaging"
    ],
    "next_review_utc": "2026-11-19T19:39:00+00:00",
    "next_checkpoint_utc": "2026-11-19T19:09:00+00:00"
}
(root/"logs/progress_review_02.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))

