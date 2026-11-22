"""Retain the complete root B88 proof audit and unchanged exact supplement run."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_p5_full_image_ramification_candidate.tex'
source=w/'agents/reduction_descent/code/verify_p5_full_image_ramification.py'
author=source.with_suffix('.output.json');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='59e1f80c1b6a5b1b269859c2b5bd7ab488771a008409d4c9760931cdf9293fab'
assert sha(candidate)==expected
assert sha(source)=='fffeeb27fff0fa51250c8e7d2b825d52a21759d77cc5a2a2fffe997fee0b42c4'
before=sha(author);assert before=='3ee1ccf40ced207e98027351d56c3542d621203562d8c4b90ba5d9500d786886'
dest=w/'code/audit_snapshots/B88_root_independent_certificate.py'
snapshot=w/'notes/root_B88_audited_candidate.tex';out=w/'outputs/root_B88_audit.json'
assert not dest.exists()and not snapshot.exists()and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter();run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B88_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B88_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items()if k not in('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['prop:B-RD88-point-fields','cor:B-RD88-cyclotomic','rem:B-RD88-scope']
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire three-label stable candidate and exact checker read; every actual point-field, coefficient, character-sum and tame-scaling step independently rederived; unchanged isolated rerun.',
 'proof_checks':[
  'In the full first layer the two evaluations have distinct diagonal quotient fields A11 andA22. Their common use of the B87 coordinate rows does not identify these diagonal fields. Each point field has degree25 and tame-stable axes, hence exactly two distinct breaks with the stated residue constraints.',
  'ForE1 an off-diagonal last line is excluded by6<24. Diagonal last gives larger quotient72 andsmaller t in6,30,54. At30 the forced first prime exponent135 is divisible by5. At54 the other coordinate would requireJ=71 before its leading exponent95. Only lower breaks6,336 remain.',
  'ForE2 a diagonal last line would give t18,u48. Row4 first forcesJ117 by cancellation at135<375, then its unique displacement at the last line is165 rather than1125. With off-diagonal last, quotient66 forces t24or48. At48 the other coordinate forcesJ77 and last displacement215 rather than2375. Only24,234 remain. All comparisons lie below12000.',
  'The four independent coordinate cyclic characters have breaks6,24,66,72. In their actual two-dimensional quotients, a sum of characters of unequal breaks remains nonzero on the last line and has the larger break by the exact coset average. Iteration proves the full character filtration without combining unrelated fields.',
  'Upper-numbering quotient compatibility identifies successive ranks4,3,2,1. Integrating indices1,5,25,125 gives lower breaks6,96,1146,1896. The numbers of projective characters by their last nonzero coordinate are1,5,25,125, summing to156. The independent different/conductor total is43728.',
  'The actual determinant modulo25 is1+5(A11+A22), so its nontrivial cyclotomic quotient has break72. Since mu5 is already inK, K(mu25)/K has degree5. Its compositum with the tame degree24 field is the direct product extension. A tame uniformizerz withz^24=x converts g(z)/z to g(x)/x; the exponent24 is a unit, so the normalized break overL is24times the one overK, giving3.'
 ],
 'source_scope':'Reuses the fresh original Colmez2.12 and3.7 full proofs and the following complete Herbrand proof read by root in its B86 source pass, recorded in outputs/root_B86_audit.json. No additional fresh Serre reading is claimed. The full B87 proof was independently audited just before this check.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'author_output_sha256':before,'author_output_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'author_runtime_seconds':original['runtime_seconds'],
 'independent_runtime_seconds':independent['runtime_seconds'],
 'independent_subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'counts':independent['counts'],'executed_failures':[],
 'scope_guard':'Necessary ramification profile only. It neither realizes nor excludes the full5^8 torsion comparison and does not prove cyclotomic break3 impossible over an allowed base.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/root_check_events.tsv').open('a',newline='')as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
  'independent re-proof / computation or formal certificate',
  'PASS: complete actual-field and coefficient proof rederived; unchanged isolated checker rerun, all mathematical outputs identical. Exact necessary full-image ramification profile only; no realization or impossibility claimed. Details: outputs/root_B88_audit.json.'])
with(w/'notes/checkpoint31_changes.md').open('a')as f:
 f.write('\n## Necessary profile of the surviving full first layer\n\nThe B88 complete root proof/code audit passed at '+now+'. The actual two point fields have lower breaks(6,336) and(24,234). The full second-division field has upper breaks6,24,66,72 and lower breaks6,96,1146,1896. Its actual cyclotomic quotient forces break3 overK. This constrains the surviving full-image branch without excluding or realizing it. The unchanged isolated checker passed in '+str(independent['runtime_seconds'])+' seconds; all mathematical output equals the retained author output.\n')
print(json.dumps({k:record[k]for k in('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))
