from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN=ROOT/'agents/reduction_descent'
source=ROOT/'agents/obstructions_crystals/post_CP32_Lang_polar_irreducibility_candidate.tex'
expected='4226990b44304d3d26f45f20faad1f14046806fbb502318106f105860ac20058'
digest=hashlib.sha256(source.read_bytes()).hexdigest()
assert digest==expected
labels=re.findall(r'\\label\{([^}]+)\}',source.read_text())
assert len(labels)==4
record={
    'status':'PASS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'candidate':str(source),
    'candidate_sha256':digest,
    'labels':labels,
    'full_independent_proof_scope':[
        'Read the complete candidate and checked every Frobenius target: A(y) squares coefficientwise to B(y^[2]), and the actual Lang equation is B(y^[2])s=y. The section-cone scaling produces the specified Euler-bundle element.',
        'Re-derived nonzero and squarefree reduced q from parity and the primitive gradient sigma^[2]. Re-derived commutation and square-zero for each derivation with squared coefficients, including extension to rational functions and independent section variables.',
        'For every irreducible factor, checked divisibility of its derivative, the degree-one logarithmic derivative, the square-zero identity, and its restriction to an additive F2-valued global Lang covector. This is an actual local-system covector, not merely a tangent identity.',
        'If the covector vanishes, the unit Lang frame spans ann(s). The constant matrix therefore preserves every generic line and is scalar; the unconstrained alternating polynomial identity then forces the scalar to be zero.',
        'Re-derived the fraction-field radical equation for the factor gradient, the UFD denominator argument from gcd(sigma)=1, the negative homogeneous degree contradiction, and the perfect-field square obstruction. This includes the linear reduced polar case.',
        'Rechecked the actual common wall point produces a nonzero maximal-rank point of q=0, without assuming the discarded common Pfaffian factor is nonzero elsewhere. The radical s0 is used only for nonemptiness, not as the affine Lang section solution.',
        'The maximal-rank Lang incidence is an affine-line torsor over the nonempty irreducible open of the reduced polar cone. The full Jacobian in y is -I, giving etale quasi-finite projection and dominance of this main component. Cone scaling preserves irreducibility on projectivization.',
        'The claim leaves exceptional components supported in lower dual-rank strata unresolved. It establishes no full-cover connectedness or new full-monodromy degree.'
    ],
    'dependency_read_scope':[
        'Freshly read the entire canonical sections/A_nonordinary_ppav_covectors.tex, including the exact any-nilpotent-length covector realization and the complete all-degree geometric invariant-covector proof.',
        'Freshly read the entire canonical agents/obstructions_crystals/A4_common_Cartier_incidence.tex, including the actual common Frobenius-bijective section and outgoing-isogeny scope.',
        'Freshly reread the full outgoing odd principal-cube corollary and proof in agents/monodromy/ppav_twisted_Cartier_Moore.tex.',
        'Freshly reread the full common-wall proposition and proof in agents/monodromy/ppav_all_odd_full_root_inertia.tex; its full source and same-coordinate proof had also been audited earlier this session.'
    ],
    'computation_scope':'No numerical program was needed or executed for this symbolic proof. This script records the completed mathematical audit only.',
    'primary_source_scope':'No new original external source was opened or claimed; the new derivation proof is self-contained and the stated canonical dependencies were read as recorded.',
    'defects':[]
}
out=OWN/'outputs/independent_Lang_polar_irreducibility_audit.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([record['actual_utc'],label,'INDEPENDENT_PASS','Full symbolic factor-to-covector and polar irreducibility proof; unique main Lang component only','outputs/independent_Lang_polar_irreducibility_audit.json','Entire four-assertion proof and exact canonical dependencies read/rederived; no numerical run or fresh external source claimed'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':record['actual_utc'],'candidate_sha256':digest,'labels':labels,'record':str(out)}))
