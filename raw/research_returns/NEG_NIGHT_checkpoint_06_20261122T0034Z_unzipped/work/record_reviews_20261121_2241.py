import csv
import json
from pathlib import Path

UTC = '2026-11-21 22:41:09 UTC'
p = Path('work/review_status.json')
d = json.loads(p.read_text())
d['NN-A028'] = dict(date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type='targeted proof check', outcome='PASS; complete deduction proof read; empty-prefix minor-size notation repaired and reread', scope_and_method='Read the whole Gaussian negativity proof, exact normalized Weyl-HCIZ identity, coalescing-pole bounds, all determinant remainder terms via sorted log moduli, positive-prefix isolation, Hermite heat application, translated unitary alphabet and four-way simplicity equivalence. Required r=lambda_1<=n in the final dual Jacobi-Trudi when p=0 and reread the repair.', limitations='Not formal verification or an independent re-proof. The theorem characterizes simplicity but does not prove simplicity. Exact higher-multiplicity leading constants are not asserted here.', evidence='work/analytic/multiplicity_detection_equivalence.tex; primary Zuber equations6,11,12')
for fid in ['NN-G027', 'NN-G028']:
    d[fid]['outcome'] = 'PASS; complete deduction proof read and separate computation events recorded'
    d[fid]['limitations'] = ('Not formal verification or an independent re-proof. G027 supplies a 3352-pair incumbent; G028 proves optimality only in the subclass W=3D,U1=3D,U2=D. Neither is an unrestricted optimality claim.')
p.write_text(json.dumps(d, indent=2)+'\n')
p = Path('work/root/CHECK_EVENTS.tsv')
with p.open() as f:
    fields = next(csv.reader(f, delimiter='\t'))
rows=[]
def event(fid, kind, outcome, scope, evidence, limitations):
    rows.append(dict(statement_id=fid, date_utc=UTC, who='/root', model='GPT-6 Astra Pro', effort='not exposed by runtime', type=kind, outcome=outcome, scope_and_method=scope, limitations=limitations, evidence=evidence))
event('Zuber2018-HCIZ-eq6-11-12', 'used and rechecked in this run', 'PASS: normalized Haar orbital integral and factorial normalization', 'Opened the primary journal PDF and read orbital definition6 on p311, determinant identity11 on p312 and normalization12 on p313. The extension to complex diagonal arguments follows by the holomorphic continuation stated and explained in A028.', 'https://www.numdam.org/item/10.4171/aihpd/56.pdf', 'Exact classical identity interface audit, not a full-paper reading or independent proof of HCIZ.')
event('E-Prop3.4-Lem4.7-Lem4.8-symbolic-interface', 'used and rechecked in this run', 'PASS: rational-only operations and coefficient-independent control support NN-C016', 'Reread NN-C016 in full and primary E Section3.1, layout definition, measurement-separation proof, Proposition3.4 proof, layout/parameter statements and AppendixB Hermite matrix and bit bounds. Scans test integer measurements and bit restrictions; no coefficient-algebra identity oracle or symbolic division is used.', 'sources/LIT_OpenAI_ETH_is_False/main_full_version.tex; work/complexity/chapter.tex NN-C016', 'Input statements of E are used as designated theorems; no independent verification of the entire E paper is claimed. This audit concerns the interfaces needed for the symbolic circuit transfer.')
event('Hatcher-1.20-2.20-4.32-4.33', 'used and rechecked in this run', 'PASS: exact topological theorem interfaces for NN-S016', 'Read the author PDF extraction for van Kampen1.20 p43, excision2.20 p119 and its open-cover version, Hurewicz4.32 pp366-367 with its displayed proof, and homology Whitehead4.33 pp367-368 with its proof. The CW/open-cover interfaces4G.1-2 were checked separately earlier.', 'https://pi.math.cornell.edu/~hatcher/AT/AT.pdf; work/complexity/hatcher_AT.txt', 'Source statement/local proof reading. No claim of having reread all prerequisite topology or the full book.')
with p.open('a', newline='') as f:
    csv.DictWriter(f, fieldnames=fields, delimiter='\t').writerows(rows)
print('Recorded', len(d), 'review entries and', len(rows), 'source-interface events.')
