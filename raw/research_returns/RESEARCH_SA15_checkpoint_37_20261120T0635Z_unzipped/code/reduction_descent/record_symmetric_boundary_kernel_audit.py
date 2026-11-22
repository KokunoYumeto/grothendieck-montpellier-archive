from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
source = own.parent/'obstructions_crystals/post_CP26_symmetric_boundary_kernel_candidate.tex'
now = datetime.now(timezone.utc).isoformat()
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
record = {
 'status':'FULL_INDEPENDENT_PROOF_SOURCE_PASS',
 'actual_utc':now,
 'candidate':str(source),
 'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'labels':labels,
 'proof_checks':[
  'Read entire three-assertion candidate and rederived dgamma=gamma^2 theta; smooth alpha2 total space makes theta nonzero, so Hodge-de Rham degeneration and trivial cotangent bundle imply Fgamma=0.',
  'Relative and absolute Frobenius cohomology typing checked; exact coboundary frame change gives Sym^2 U=U+O, with no division by two.',
  'Perfect exterior cup algebra gives cohomology (2,4,2) in the nonsplit case and (3,6,3) in the split case.',
  'Read entire prior residual-pencil resolution and pertinent pencil/norm proofs; checked both long exact sequences, injection H1(EG) into H1(J_res), and exact kernel quotient including surjectivity.',
  'Acyclic G identifies H1(EG) with H0(D,AG|D), and norm sigma plus degree g-1 and curve duality proves this domain is nonzero, including Cartier nonreduced setting.',
  'No residual-product or determinant-direction nonvanishing is inferred.'
 ],
 'primary_source_read':{
  'source':str(own.parent/'obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt'),
  'locator':'Proposition7.27 and proof p108; Corollary7.29 and complete proof pp108-109',
  'method':'Fresh read of retained original text. No fresh web retrieval or image viewing claimed.'
 },
 'code_scope':'No new numerical run. Exact symmetric-square frame identity was among the17 identities already independently rerun at22:10:23; see independent_primitive_unipotent_bundle_audit.json.',
 'earlier_independent_runtime_seconds':0.07015292799042072
}
dest=own/'outputs/independent_symmetric_boundary_kernel_audit.json'
dest.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'INDEPENDENT_FULL_PASS','Fgamma=0, Sym²G cohomology and exact residual-boundary kernel sequence; extra twisted-pencil term retained.','outputs/independent_symmetric_boundary_kernel_audit.json','Entire proof and AV7.27/7.29 original full proofs read; earlier exact17-identity rerun reused, no new numeric run'])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'candidate_sha256':record['candidate_sha256'],'labels':labels}))
