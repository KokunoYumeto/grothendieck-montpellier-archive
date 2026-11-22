"""Record the complete root audit of the actual common-incidence proof."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP30_common_Cartier_incidence_candidate.tex'
expected='a66b95b4de7a405fe4f0aa143a57ad5f6186254d530b846995de573206a5b8f7'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
out=w/'outputs/root_common_Cartier_incidence_audit.json'
snapshot=w/'notes/root_common_Cartier_incidence_audited_candidate.tex'
assert not out.exists() and not snapshot.exists();shutil.copy2(p,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:DE-common-incidence-multiplication','prop:DE-common-Cartier-incidence',
 'cor:DE-odd-principal-cube-kernel-birational','rem:DE-common-Cartier-incidence-scope']
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire four-label stable candidate read and independently rederived; complete current root differential/birational criterion reread. Exact TCM, symmetrizer and degree-one proof inputs were fully audited immediately beforehand. No new numerical or original-source reading claimed.',
 'proof_checks':[
  'Fixing the first input in TCM5 gives output-rowk/input-columnj entry c_(k-j)v_(2k-j)=c_(k-j)v_(-(k+j)). This literal triality identity identifies the multiplication determinant with the same nonzero Moore determinant, with only a permutation of its variables.',
  'For nontrivial oddP choose its halfQ andu withphi_M(u)=Q. Translation by-u sends M andMP toMQ^-1 andMQ. The target M^(2)Q^(2) is exact becauseF^* of it isM²P; translation by-F(u) trivializes its Q twist. Thus the balanced nonzero determinant pulls back to a nonzero polynomial on the fixed section spaceH0(M).',
  'On an odd cover multiplication bys0 permutes all nontrivial character blocks by their unique halves. Each is invertible on a nonempty open in the same9-dimensional affine space. The full symmetric trivial tensor supplies a fixed linear isomorphismJ from that section space to the dual Frobenius-twisted target, and its left kernel isJ(s0) on rank8.',
  'ExtendingJ(s0) by zero gives the actual left kernel once all other multiplication blocks are invertible. Every dual cross determinant composed withJ is again a nonzero polynomial in the same variables. Intersecting the finite multiplication, dual, rank8, smooth and actual degree-one relative-Hasse opens is legitimate on one integral affine space.',
  'The etale inverse image of the smooth base divisor is smooth. Its ample line bundle hasH1(L^-1)=0 by Serre duality and ample vanishing, so its global functions arek and it is connected. In the actual relative coherent bundle all nontrivial character summands are entire summands, permuted bijectively; the remaining trivial relative block is exactly the known degree-one relative Frobenius. This proves actual sharpness of this particular pullback family.',
  'At this common pair M_s andB_lambda both have rankh-1. The re-read differential formula gives rankdκ=h-1. Separability and dominance follow, and the unique radical ofB_lambda on its generic rank open gives the rational inverse. This closes the prior common-incidence gap, with the outgoing degree-d² quotient retaining the fixed source surface.'
 ],
 'scope_guard':'No claim that a corank-one Hasse wall meets the differential open, that its local inertia is full, or that local radicals generate the global monodromy. No new exact-group degree is inferred.',
 'numerical_program_executed':False}
out.write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/root_check_events.tsv').open('a',newline='')as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','independent re-proof',
  'PASS: full typed common-incidence proof rederived, including literal other Moore contraction, shared section opens, actual character-cycle Frobenius and birational inverse. No new numerical run. Details: outputs/root_common_Cartier_incidence_audit.json. Local Hasse-wall and global group gates remain.'])
with(w/'notes/checkpoint31_changes.md').open('a')as f:
 f.write('\n## Actual common incidence and birational kernel map\n\nThe four-label common-incidence proof has passed the full root audit at '+now+'. It uses the literal other contraction of the Moore tensor to make each nontrivial multiplication block invertible. The level-three symmetrizer identifies the trivial left kernel linearly with the same section variable. All multiplication and dual determinant opens therefore meet at one actual section/left-kernel pair, with bijective relative coherent Frobenius on the smooth connected etale pullback curve. The left-kernel map for every fixed odd principal-cube degree is consequently separably dominant and birational. The proof does not yet put a corank-one Hasse divisor in that open or establish its full local inertia and global generation.\n')
print(json.dumps({'status':'PASS','actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))
