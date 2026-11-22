"""Record the scheduled fifth formal research review, never before it is due."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,20,6,58,tzinfo=timezone.utc)
assert now>=due, 'The formal review is not yet due'
assert not (root/'logs/formal_review05.json').exists(), 'Review already recorded'
aux=(root/'RESEARCH_SA17_paper.aux').read_text()
numbers=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
def ref(key):return key+' ('+numbers[key]+')'
with (root/'RESEARCH_SA17_results.csv').open(newline='') as f:rows=list(csv.DictReader(f))
open_ids=[r['id'] for r in rows if r['status'].startswith('Open')]
assert set(open_ids)=={'C:allrings_gate','C:BO_general_gate'},open_ids
text=f'''

## Formal progress review05 — {now.isoformat()}

This fifth formal review was scheduled for20:06:58UTC and compares the proved state with review04 at19:07:20UTC. **Substantive movement: YES. Consecutive reviews without movement:0.** We continue. The next formal review is21:06:58UTC; checkpoint12 is separately due20:36:58UTC. A new whole-family answer counts only after its full proof and independent actual-file audit. Packaging, bounded failed searches, the mixed shallow torsion bound and cancellation of one particular node class are not counted.

| Row open at review04 | Status at review05 | Strict movement established |
|---|---|---|
| C.1 | OPEN, with the entire regular-coherent and valuation families now classified | {ref('C:regular-coherent-criterion')} proves the necessary-and-sufficient characteristic-zero/unit-K0 criterion for every regular coherent ring, with no Noetherian or dimension bound. {ref('C:valuation-domain-criterion')} includes all valuation domains of arbitrary rank and value group. {ref('C:coherent-regular-modular-locus')} requires regular coherence only at positive-residue-characteristic points. These previously unincluded drafts are now fully audited, incorporated and compiled. |
| C.3 | OPEN, with new coherent henselian, global-field and henselian-global coefficient families completely determined | {ref('C:effective-coherent-henselization-WG')} replaces Noetherianity by exact finite matrix-kernel access; its explicit higher-rank valuation examples cannot be flat local unions of Noetherian local rings. The effective C1-residue and full square-class product results are included. {ref('C:global-function-coefficient-WG')} and {ref('C:global-function-henselization-WG')} give full ordinary algorithms over every supplied finite global function-field tower, finite coefficient algebras and the stated local henselizations. {ref('C:henselian-global-field-arithmetic')} and {ref('C:henselian-global-coefficient-WG')} further cover every supplied finite extension of henselized global-place fraction fields, including inseparable towers, their finite algebras and the stated effective coherent local henselizations. Actual division factors and every residual hermitian isometry are decided. {ref('C:henselian-global-new-families')} proves that explicit members are non-C1, nonglobal and of positive characteristic, so this is an additional whole-family removal. |

### Every remaining open row and its strongest proved reduction

| Open row | Strongest proved reduction and exact remaining gate | Active next approaches and failures |
|---|---|---|
| C:allrings_gate / C.1 for every commutative ring | The intrinsic all-ring necessary-and-sufficient condition remains missing. The all-ring obstruction sequence is an exact reduction, not a classification. The rational, positive-characteristic, regular-coherent, valuation and coherent regular-modular-locus cases are settled, together with the earlier square-zero and node families. Still open are the remaining mixed modular singularities, mixed shallow ramified deformations, higher nilpotence and arbitrary rings outside these completed classes. The smallest active reduced example remains xy=pi cubed with2=v*pi squared. | {ref('C:MF-Swan-transfer')} constructs an additive MF-to-Swan map, and {ref('C:ramified-A2-MF-cancellation')} cancels its specified standard rank-four node class; neither proves full node polynomiality. The mixed shallow classes are killed by three but no nonzero class or general vanishing is proved. The positive noncoherent example was already covered by filtered colimits. First-pi and pi-cubed detectors failed in their recorded scopes. The tame cover restricts to MCM modules instead of projectives; ordinary MCM comparison loses classes. A complete-intersection pencil route is being examined, with no exact-category equivalence or positivity theorem claimed. |
| C:BO_general_gate / C.3 for the remaining bases and arithmetic | All previously completed field, finite-algebra, complete-local, profinite, arithmetic-henselian, coherent-local and bounded-product families remain. The new global and henselian-global families have literal decidable indecomposable and Gram-pair coordinates, actual forms/isometries and all specified ring/exterior operations. The remaining task is coefficient bases outside these families and arithmetic not supplied by the stated exact access. Arbitrary-field division/isometry quotients do not count as answers, and existing undecidability results retain their precise access hypotheses. | Effective separably closed fields of finite imperfection degree and henselian fields with infinite residue are under investigation using exact p-component algorithms and Greenberg approximation. Those drafts are not counted at this review. Nonhenselian function-ring lattices require actual integral isomorphism and hermitian arithmetic; local data alone do not settle the genus obstruction. |

A.1 including L1, A.2/L2, A.4, B.3, C.4 and R remain completed in their recorded scopes. Exactly two catalog rows are Open. The283-page/261-statement working build and its visual verification are production records and are not counted as mathematical movement. No authorized stopping condition is met.
'''
with (root/'PROGRESS_LEDGER.md').open('a') as f:f.write(text)
record={'actual_time':now.isoformat(),'scheduled_time':due.isoformat(),'movement':True,'no_movement_streak':0,'open_rows':['C.1','C.3'],'next_review':'2026-11-19T21:06:58+00:00','next_checkpoint':'2026-11-19T20:36:58+00:00','counted_mathematical_families':['all regular-coherent rings and arbitrary valuation domains','coherent rings regular coherent on the positive-characteristic locus','effective C1-residue and coherent-local henselizations','higher-rank valuation families outside flat local Noetherian unions','full square-class coordinates for the stated products','global function fields and finite coefficient algebras and stated local henselizations','henselized global-place fraction fields and all finite towers and stated coefficient algebras and local henselizations'],'excluded_from_count':['packaging and visual QA','noncoherent example already covered by filtered colimits','mixed shallow three-torsion bound without vanishing','specified MF class cancellation without full node result','failed bounded detectors','unincluded infinite-residue and separably closed drafts']}
(root/'logs/formal_review05.json').write_text(json.dumps(record,indent=2)+'\n')
with (root/'notes/ROOT_STATUS.md').open('a') as f:f.write(f'''\n\n## Formal review05 — {now.isoformat()}

C.1/C.3 remain the only Open rows. MovementYES; no-movement streak0. Counted: regular-coherent/valuation C1 classification and coherent modular-locus sufficiency; further C1/coherent henselian and global/henselian-global WG families. Particular MF cancellation, three-torsion bounds, failed probes and production work were excluded. Full ledger is in PROGRESS_LEDGER.md. Current verified build283pages/261statements/75inputs, build200126, QA logs/pdf_qa_checkpoint_12.json; source freeze not imposed. Nextreview21:06:58UTC; nextcheckpoint12at20:36:58UTC. No authorized stop condition met. Continue all research.
''')
print(json.dumps(record,indent=2))
