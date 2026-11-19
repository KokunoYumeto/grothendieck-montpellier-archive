"""Post-curation attribution audit; every amendment is manually specified."""
import json,csv
from pathlib import Path
O=Path(__file__).resolve().parents[1]
P='MPL_7_061-072+8_001-078'
def read(n): return json.loads((O/(n+'_c8.json')).read_text())
items,claims,problems,entries=map(read,['items','claims','problems','entries'])
by={x['id']:x for x in items}
by['P78-I048'].update(check='agrees',check_reason='Earlier notes L.34–L.37 already give the K×/A× distinction, independent rescaling and arbitrary-subgroup counterexample. This run rechecks them; they are not new ideas of this run.')
by['P78-I052'].update(check='agrees',check_reason='Earlier note T.09 already gives the Borel-restriction counterexample and T.10 the target-semisimplicity condition. Both were independently re-proved here, with attribution retained.')
for e in entries:
 if e['entry_id'].endswith('#60'): e.update(verdict='kept',reason='Earlier notes already flag period normalization and arbitrary-subgroup overreach; both were rechecked against the page and Tate’s theorem.')
 if e['entry_id'].endswith('#66'): e.update(verdict='kept',reason='Earlier note T.09 already supplies the Borel counterexample to the formal full-faithfulness implication; this run independently rechecks it.')
for c in claims:
 if c['id']=='P78-C048': c['fate']=c['present_status']='Standard jet constructions; the supplied coordinate proofs are rechecked in proof_audit_root.md §13. The opened publisher record verifies the Bourbaki fascicule family. The archive draft catalogue could not be opened, so draft382 and pagewise identity remain unverified provenance leads.'
 if c['id']=='P78-C063': c['fate']=c['present_status']='Tate1966 proves the finite-field abelian homomorphism theorem and its divisor consequences. The general higher-codimension agenda remains broader. Search found Li2026 as a conditional recent lead, but all attempted primary opens failed; it is not used as an established result or as proof of the current general status.'
for p in problems:
 if p['id']=='P78-P020':p['state_of_art']='Tate1966 establishes the finite-field abelian homomorphism theorem and divisor consequences. The general cycle conjectures are not settled by that theorem. A 2026 conditional-preprint search lead is listed as unverified and is not used as a proved result.'

# Separate earlier-run contributions from propositions attributed to the manuscript.
# The cited parent items carry the precise transcription lines; source subnotes carry
# the actual origin of the idea. These are curated groups, not keyword verdicts.
groups=[
 (61,[14,15,18,19,21,22,23],[14,16,20,21,24,26,29,31],['E.24','E.06','E.13','E.14','E.29','E.32'], 'Derived and Frobenius tests proposed by the earlier run: nonreduced Frobenius need not be faithful; two cohomology objects omit an Ext² attaching class; relative Ext should be a homotopy fibre; a linear kernel must be realized before it is a group-scheme counterexample.'),
 (62,[24,25,26,28],[15,22,25,27,30],['ER.03','ER.05','ER.09','S.021.2'], 'Earlier-run reconstructions of the Lipman chart, the proper-base-change diagram chase, the canceled relative μ₂ mapping fibre and the polydisc Lipschitz bound.'),
 (63,[30,31,32,33,34,35],[33,34,35,36,37,38],['L.08','L.03','S.026.3','L.05','S.029.3','S.030.2','L.10','L.11'], 'Earlier-run ordinary-extension checks: module splitting need not be horizontal; matrix order, gauge differential and rank-one sign must agree; p−σ on an ideal needs a convergence hypothesis; rationally invertible elements need not be integral units.'),
 (64,[36],[39],['R.03','R.04'], 'Earlier-run proof of the ℓ≠p filtration-length descent via Zariski closure of unipotent inertia, and the finite-character warning.'),
 (65,[37,38,39,40,43,44,45],[40,42,44,46,48,50,51,53,55],['L.12','L.13','L.14','L.15','S.040.4','L.16','S.042.3','L.18','L.19','L.22','L.23','L.24','L.27'], 'Earlier-run Lubin–Tate tests: slope1/h, W-rank e, sum of exponents, equivariant Hom recurrence, common effective lattice, Ω/p versus Ω/π, contravariant coefficient dual, PD bound and its nonnilpotent endpoint, multiplication quotient, admissibility and dual exponent sign.'),
 (66,[41,42],[41,43,45,47,49,52,54],['R.06','R.07','R.08','R.09'], 'Earlier-run jet and multilinear arguments: origin-preserving jet count subtracts the q constant coefficients; the printed group action is ill typed; characteristic-p derivatives lose the T^p jet; section operations reconstruct locally from frame values.'),
 (67,[46,47,48],[56,58,60],['L.34','L.37'], 'Earlier-run period tests: each eigenperiod can be independently rescaled by K×, so one period does not determine all the others without compatibility; A× uniqueness needs normalization; an arbitrary subgroup includes the trivial subgroup.'),
 (68,[50],[62,63],['L.38'], 'Earlier-run low-confidence suggestion to compare unlabeled polygon slopes with effectivity bounds. This run retains it only as a possible future test: no Newton-polygon identification is established.'),
 (69,[51,52,57],[64,66,78],['T.02','T.03','T.04','T.09','T.10','T.11','T.27','T.28','T.29'], 'Earlier-run Tannakian and filtration countertests: admissibility is stronger than a stable lattice; effectivity is not preserved by duality; Borel restriction is fully faithful but not dense; two gradings need not commute; weak admissibility does not force Frobenius stability of the filtration; BMS pairs are a distinct modern construction.'),
 (70,[53,54,55],[68,70,72,74,76],['S.063.4','T.15','T.18','T.20','T.21','T.22','S.071.4','S.073.3'], 'Earlier-run torsor reconstructions: inner forms, scaling cocycles, σ-conjugacy, decomposition-group choice, Frobenius over Q_p and the real involution, together with comparison of the diagrams on71 and73.'),
 (71,[58,59],[65,67,69,71,73,75,77,79],['R.12','R.14','R.15'], 'Earlier-run comparison with the published purity argument, the L∞ translation endpoint test and the convention-explicit unimodular convolution check.'),
 (72,[60],[80],['E.36','E.37'], 'Earlier-run finite free character resolution and μ_n cotangent-complex test; derived tensor detects the torsion term omitted by an underived formula.'),
 (73,[56,57],[78],['S.075.6'], 'Earlier-run proposal to organize the final agenda into distinct questions. The problem register adopts that organizational idea without attributing its modern expanded formulations to the manuscript.')
]
for n,parents,src,sub,st in groups:
 pp=[by[f'P78-I{i:03}'] for i in parents]
 items.append(dict(id=f'P78-I{n:03}',sources=[P+'#'+str(s) for s in src],kind='idea of the earlier run',cote=['8'],scans=sorted({s for p in pp for s in p['scans']}),lines=sorted({s for p in pp for s in p['lines']}),his_words='',statement=st,reconstruction='These are explicitly the earlier research notes’ ideas, not words or claims supplied by the manuscript. Their parent items and relevant claims contain the present rechecks.',check='not on the page',check_reason='Correctly labeled own ideas in the earlier notes; read against the cited passage to test relevance and attribution. A not-on-the-page verdict here is an attribution fact, not a rejection of the idea.',earlier_run_subnotes=sub,related_items=[p['id'] for p in pp]))
for name,data in [('items',items),('claims',claims),('problems',problems),('entries',entries)]:
 (O/(name+'_c8.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (O/'check_events_c8.tsv').open('a') as f:
 w=csv.writer(f,delimiter='\t')
 from datetime import datetime,timezone
 for n,*_ in groups:w.writerow([f'P78-I{n:03}',datetime.now(timezone.utc).isoformat(),'GPT-6 Astra Pro; effort not exposed; SA15-20261119/root','used and rechecked in this run','Read the earlier-run own-idea subnotes and their manuscript passages; preserved origin and linked the actual mathematical recheck.'])
print(json.dumps({'attribution_groups':len(groups),'items_after_amendment':len(items),'verdicts_amended':['#60','#66']}))
