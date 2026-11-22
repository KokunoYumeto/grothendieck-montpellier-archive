"""Stage the comparison with review16; this does not perform a formal review."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
root=Path(__file__).resolve().parents[1]
prior=json.loads((root/'code/output/formal_review16.json').read_text())
manifests=[
 'parts/C/post24_research/integration_manifest_C_matrix_model_alternating.json',
 'parts/C/post24_research/integration_manifest_C_original_boundary_alternating.json',
 'parts/C/post24_research/integration_manifest_C_intrinsic_matrix_models.json',
 'parts/C/post24_research/integration_manifest_C_primitive_defining_characteristic_orbits.json',
]
verified=[]
for path in manifests:
 m=json.loads((root/path).read_text())
 assert m['status']=='Proved'
 assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest()==m['sha256']
 assert set(m['audit_scope'])=={'root','B','C','D'}
 for rec in m['audit_scope'].values():
  audit=json.loads((root/rec['record']).read_text())
  assert 'PASS' in str(audit.get('verdict',audit.get('status',audit.get('outcome','')))).upper(),rec['record']
 verified.append({'path':m['path'],'sha256':m['sha256'],'audit_manifest':path})
gates=list(prior['remaining_strongest_gates'])
gates[0]='Unrestricted alternating simple-quotient multiplicities outside the enlarged whole-source criterion: local orbit models with log(model count)+r^2 log(q)=O(N log(N+1)), intrinsic F_p dimension D with D^4=O(N log(N+1)), and fixed finitely generated local quotients are uncharged; only the residual whole-orbit squared energy is controlled. Primitive defining-characteristic socles and one fixed finite collection qualify, but unbounded alternating socles, unrestricted cross-characteristic socles, and arbitrary imprimitive extensions remain uncovered. The original-boundary normal proper surface scope is included; arbitrary nonnormal divisorial descent is not asserted.'
gates[1]='Hereditary projective constants linear in arbitrary finite-cover degree remain unproved. All-complete cover geometry, canonical generation, ordinary determinant lists, finite-cycle Hom budgets, qualified family realization and exact Hom windows are now auxiliary inputs; an actual all-object parameter atlas with the required quantitative complexity and compatible unit arrows is still missing. Ordinary determinant control is not twisted-projective determinant control.'
a={
 'assessment_actor':'root','assessment_staged_utc':datetime.now(timezone.utc).isoformat(),
 'formal_review_completed':False,'movement':True,
 'requested_status_changes':[],'requested_open':prior['requested_open'],
 'strict_main_gate_reductions':[
  'One strict enlargement of the restricted-alternating main gate after review16: whole local orbits with controlled matrix-model cost or intrinsic small F_p dimension are now uncharged, in addition to orbits through fixed finitely generated local quotients. This includes the checked affine-point, projective-flag and primitive defining-characteristic recognitions. The normal original-divisorial-boundary proper-surface transfer, disconnected, dimensional and finite-normalization consequences belong to this same enlargement. Only uncontrolled whole-orbit squared energy must satisfy O(n log(n+1)).'
 ],
 'verified_files':verified,'all_required_proof_audits_completed':True,
 'remaining_strongest_gates':gates,
 'auxiliary_not_movement':[
  'The four alternating model, intrinsic-dimension, original-boundary and primitive-recognition files establish one enlarged criterion. Their six numbered units and geometric consequences are not separate main-gate movements.',
  'Fixed henselian algebraization and all-complete geometric budgets, the hereditary Cartier bridge, ordinary determinant enumeration, finite-cycle derived Hom and generation-cycle budgets, qualified weak-cycle relative realization, and exact two-level Hom windows are auxiliary inputs. They do not prove an effective object-family atlas, arbitrary independent relation lifting, a hereditary projective count, or full profinite generation.',
  'Post25 uniformly comparable strong cycles and the intrinsic unit-Isom theorem, if promoted by the review time, remain auxiliary. They concern numerical compatibility or already actual canonical families and do not independently shrink a main residual gate.',
  'Previously counted projective growth, restricted crowns, and all earlier geometric cases are historical inputs. Searches, source precision, actual audits, builds, visual inspection, archive creation and saving are not research movement.'
 ],
 'report_summary':'The restricted-alternating main gate is strictly smaller: controlled whole-orbit matrix models and intrinsic small-dimension images are uncharged, with the stated original-boundary and primitive recognitions. This is one enlargement. All new complete-cover geometry and finite-data/conditional-family results remain auxiliary; the effective hereditary atlas is still missing.'
}
out=root/'code/output/review17_main_assessment.json'
assert not out.exists()
out.write_text(json.dumps(a,indent=2)+'\n')
print(json.dumps({'assessment':str(out.relative_to(root)),'strict_gate_reductions':1,'status_changes':0,'formal_review_completed':False}))
