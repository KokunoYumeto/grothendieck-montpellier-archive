from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN=ROOT/'agents/reduction_descent'
source=ROOT/'agents/obstructions_crystals/post_CP32_Lang_main_orbit_candidate.tex'
digest=hashlib.sha256(source.read_bytes()).hexdigest()
assert digest=='d3637b2c6536b126b86c70ec2ee13eb59547ba15e8d7e0005a9386ca38268d80'
labels=re.findall(r'\\label\{([^}]+)\}',source.read_text())
assert len(labels)==2
record={
    'status':'PASS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'candidate':str(source),
    'candidate_sha256':digest,
    'labels':labels,
    'full_proof_scope':[
        'Read the entire two-label candidate. Re-derived the regular Lang hyperplane from the rank-r-1 special stable part and etale henselian uniqueness. After any finite valuation extension, an integral fixed vector still specializes to an existing etale residue point and is its unique lift, so no additional vector becomes integral.',
        'For a pole vector, scale by the inverse of a coordinate of least valuation. The exact equation M_s^t z^[2]=a z reduces to a nonzero vector in the actual kernel k lambda_0. A maximal minor of B(z^[2]) is then a unit, proving maximal generic dual rank without transporting a stable fibre through the rank drop.',
        'The pointwise fixed space K of the normal closure lies in the regular hyperplane H fixed by the actual wall radical. Hence every vector outside H lies in the one large orbit V minus K.',
        'The unique irreducible maximal-dual-rank component meets that large orbit through the pole vectors. The generic finite-etale component/orbit equivalence therefore identifies it with that entire orbit, of degree 2^r-2^dimK.',
        'The remaining components may lie over lower dual-rank strata; no parity, K=0, entire-cover irreducibility or new full-image degree follows.'
    ],
    'dependency_read_scope':[
        'The full reduced-polar candidate and its complete geometric dependencies were independently audited earlier this turn; exact record outputs/independent_Lang_polar_irreducibility_audit.json.',
        'Freshly read the entire root notes/A_full_radical_image_structure_candidate.tex, including full pointwise stabilizer generation, exact inverse-image group form, unique maximal submodule and large orbit, and geometric application.',
        'Freshly read the complete independent group proof agents/monodromy/post_CP32_full_radical_normal_closure_candidate.tex.',
        'Freshly reread the entire canonical agents/monodromy/Cartier_kernel_wall_inertia.tex, including stable-loss and actual full-radical local hypotheses. The all-odd wall theorem was fully audited earlier this turn.'
    ],
    'computation_scope':'No numerical program is required or executed. This script records the completed direct proof audit only.',
    'primary_source_scope':'No new original external source opening is claimed.',
    'defects':[]
}
out=OWN/'outputs/independent_Lang_main_orbit_audit.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([record['actual_utc'],label,'INDEPENDENT_PASS','Full pole-vector specialization and exact large-orbit identification; no parity or exceptional-component exclusion','outputs/independent_Lang_main_orbit_audit.json','Entire proof and complete group/local-wall dependencies read and rederived; no numerical run or fresh original-source reading'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':record['actual_utc'],'candidate_sha256':digest,'labels':labels,'record':str(out)}))
