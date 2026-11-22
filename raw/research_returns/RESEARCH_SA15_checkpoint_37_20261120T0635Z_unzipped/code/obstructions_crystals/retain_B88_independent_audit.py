"""Full B88 necessary-profile proof/source audit and unchanged exact rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,subprocess,sys

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals';author=root/'agents/reduction_descent'
source=author/'B_p5_full_image_ramification_candidate.tex'
program=author/'code/verify_p5_full_image_ramification.py'
output=program.with_suffix('.output.json')
expected={source:'59e1f80c1b6a5b1b269859c2b5bd7ab488771a008409d4c9760931cdf9293fab',
          program:'fffeeb27fff0fa51250c8e7d2b825d52a21759d77cc5a2a2fffe997fee0b42c4',
          output:'3ee1ccf40ced207e98027351d56c3542d621203562d8c4b90ba5d9500d786886'}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert all(sha(p)==h for p,h in expected.items())
copied=own/'code/B88_independent_check.py'
assert not copied.exists();copied.write_bytes(program.read_bytes())
run=subprocess.run([sys.executable,str(copied)],cwd=root,capture_output=True,text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes={str(p.relative_to(root)):{'before':h,'after':sha(p)} for p,h in expected.items()}
hp=own/'outputs/B88_author_hashes_preserved.json'
hp.write_text(json.dumps(hashes,indent=2)+'\n')
assert all(r['before']==r['after'] for r in hashes.values())
assert run.returncode==0,run.stderr
result=json.loads(copied.with_suffix('.output.json').read_text())
author_result=json.loads(output.read_text())
strip=lambda d:{k:v for k,v in d.items() if k not in ('runtime_seconds','actual_utc')}
assert result['status']=='PASS' and strip(result)==strip(author_result)
labels=re.findall(r'\\label\{((?:prop|cor|rem):[^}]+)\}',source.read_text())
assert len(labels)==3
now=datetime.now(timezone.utc).isoformat()
record={
 'status':'FULL PROOF, SOURCE AND EXACT CODE PASS','actual_utc':now,
 'candidate':str(source.relative_to(root)),'candidate_sha256':expected[source],'labels':labels,
 'proof_read_scope':'Entire stable three-label B88 source, standalone checker and actual output read. B87 was fully independently proved/source-checked and literally rerun immediately before this audit; all four actual coordinate rows and their fixed-coefficient minimum are reused with the correct full-W1 evaluation kernels.',
 'checks':[
  'For W1=M2(F5), both evaluations on e1,e2 are surjective and their stabilizers are the appropriate two-dimensional kernels. The actual point fields are Galois degree25, independent of the choice of primitive lift. Their diagonal characters are A11 and A22 and are independent; no shared diagonal field from the previous three-dimensional case is reused.',
  'The exact tame residues and quotient averages force E1 last line diagonal, diagonal quotient72, and smaller break in{6,30,54}. The forced first prime degree15+4t excludes30 by5-divisibility. At54 the first-row unique prime change would require degree71 below its leading95. Thus E1 lower breaks are6,336.',
  'For E2, diagonal-last forces18,48; the fourth-row cancellation forces first prime degree117 and the last-line displacement165 rather than1125. Off-last forces larger quotient66 and smaller break24 or48. At48 the third-row degree77 would give later displacement215 rather than2375. Thus E2 lower breaks are24,234. Every comparison is strict below absolute index12000 and retains the same coordinate expansion.',
  'For two independent cyclic characters with unequal breaks, their actual rank-two quotient has a last ramification line killed by the smaller-break character but not the larger one. Its nonzero sum therefore has the larger break by the same exact quotient average. Induction identifies every character combination by its largest nonzero coordinate break, without asserting unrelated point fields coincide.',
  'Herbrand quotient compatibility gives upper breaks6,24,66,72 and ranks4,3,2,1. Integrating the exact indices1,5,25,125 gives lower breaks6,96,1146,1896. The one-dimensional character counts are1,5,25,125 and exhaust156 cyclic degree5 subfields. The independent different/conductor arithmetic agrees at43728.',
  'The actual determinant modulo25 is the trace A11+A22, so its quotient is genuinely L(mu25), of break72 and degree5. The base cyclotomic degree is also5. Coprime Galois degrees5 and24 give the actual direct-product compositum, and algebraically closed residue plus Hensel supplies a uniformizer z with z^24=x for a chosen base-cyclotomic uniformizer x. The residue-one ratio identity gives tame break scaling by24, hence break3 over K.',
  'The conclusion is a necessary actual full-image ramification profile only. It does not establish that break3 is impossible or realizable, does not use the distinct B86 hypothesis mu25 contained in K, and does not settle the unrestricted first-wild index or another residual sector.'
 ],
 'primary_sources':[
  {'title':'Pierre Colmez, Corps locaux, notes du cours de M2',
   'url':'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf','web_ref':'turn902110939view0',
   'retained_original_text':'agents/reduction_descent/sources/colmez_corps_locaux.txt',
   'retained_text_sha256':sha(author/'sources/colmez_corps_locaux.txt'),
   'actual_read_scope':'Original PDF freshly opened in the immediately preceding B87 audit. Complete retained original Proposition2.12 and its Hensel/uniformizer proof p11, Proposition3.7 and its full norm-polynomial proof pp14-15, Lemma3.8/Corollary3.9 and Theorem3.10 full Herbrand proof pp15-16, Definition3.11 and Proposition3.13/full proof p16 freshly read. No new image-view or Serre-source read claim.'}
 ],
 'independent_program':str(copied.relative_to(root)),
 'independent_output':str(copied.with_suffix('.output.json').relative_to(root)),
 'independent_runtime_seconds':result['runtime_seconds'],'counts':result['counts'],
 'author_bytes_unchanged':True,'all_mathematical_output_identical':True,
 'hash_record':str(hp.relative_to(root)),'finite_scope':result['scope'],
 'scope':'Exact necessary point-field/full-first-layer/cyclotomic profile; no realization or impossibility inference.'
}
audit=own/'B88_independent_audit.json'
with audit.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'independent_full_proof_source_code_audit',str(source.relative_to(root)),
                      'Complete fixed-coefficient profile, actual character quotients and primary Herbrand proof; literal isolated checker',
                      'PASS',str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'record':str(audit.relative_to(root)),
                  'runtime_seconds':result['runtime_seconds'],'labels':labels}))
