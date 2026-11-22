from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
candidate=own/'B_p5_third_point_ramification_candidate.tex'
program=own/'code/verify_p5_third_point_ramification.py'
output=program.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
result=json.loads(output.read_text())
assert result['status']=='PASS'
record={'status':'CANDIDATE_AWAITING_COMPLETE_ROOT_AND_COMPANION_AUDITS',
        'actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(candidate),'candidate_sha256':sha(candidate),
        'labels':re.findall(r'\\label\{([^}]+)\}',candidate.read_text()),
        'program':str(program),'program_sha256':sha(program),
        'output':str(output),'output_sha256':sha(output),
        'author_run_utc':result['actual_utc'],'author_runtime_seconds':result['runtime_seconds'],
        'counts':result['counts'],'executed_failures':[],
        'proof_scope':'Actual p3 point stabilizers, two Galois degree25 towers, fixed-coordinate forcing, actual intersections and elementary composita, exact subgroup/quotient ramification, and nonintegral determinant coset average.',
        'source_scope':'Internal B60 fixed-coefficient proof previously reread in B89 audit; B76 inverse Newton proof, B87 coefficient/point-field proof, and entire B88 proof reread. Colmez full original quotient/Herbrand source remains the previously audited input; no new external opening claimed.',
        'limitation':'Only tame reducible residual p5/e20 branch. No unrestricted least-index closure; B89 base example remains valid.'}
out=own/'outputs/B90_candidate_record.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
