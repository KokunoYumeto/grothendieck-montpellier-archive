"""Record the complete B81 proof check and an unchanged isolated exact rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_first_wild_Cartan_exclusion_candidate.tex'
source=w/'agents/reduction_descent/code/verify_first_wild_Cartan_exclusion.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='8b7c13a40f6c40f2f55a54d3d17a5c214e01c4456cbf0a0c81eeb27462da332b'
assert sha(candidate)==expected
assert sha(source)=='5675075829b7d8c7ee9e290cbea07fd20877a2872dfd0b702b5e84aade18c48c'
before=sha(author)
dest=w/'code/audit_snapshots/B81_root_independent_certificate.py'
snapshot=w/'notes/root_B81_audited_candidate.tex';out=w/'outputs/root_B81_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B81_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B81_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
def math(x):return {k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert math(original)==math(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
 'labels':['lem:B-RD81-levels','prop:B-RD81-Cartan','cor:B-RD81','rem:B-RD81-scope'],
 'proof_scope':'Every paragraph of the complete final candidate and entire exact checker read; both coefficient levels and the vanishing boundary rederived independently.',
 'proof_checks':[
  'B80 supplies the actual group W=(Z/p^2)^2, U=pW and both full original Cartan layers. Invertibility of nonzero Cartan matrices gives exact displacement valuations D1=qA and D2=q^2A for every primitive point.',
  'For every nonidentity h in U, surjectivity of the actual pth-power map gives h=g^p with g of order p^2. Additivity of the first uniformizer coefficient gives b(h)>b(g)>=a. Hence the minimum break is realized outside U.',
  'Fixed primitive lifts and fixed coefficient representatives permit one simultaneous expansion. Leading p and p^2 series give d_i^q lambda_i(g)z and d_i^(q^2) lambda_i(h)z; arbitrary-index Frobenius orientation gives lambda2=lambda1^p on both Cartan layers.',
  'For a<a0 cancellation yields the first prime degree j=A+(p-1)a and a nonzero z-linear coefficient. For a>a0 the Cartan displacement gives j=D1-a with the same z-linearity. The two displayed positive gaps prove uniqueness of the first terminal change at either break.',
  'Thus all terminal elements would have one common break D2-j and lambda_i(h)=kappa_i d_h on the whole field. Scalar proportionality and nontrivial Frobenius cannot both hold.',
  'At a=a0, j0 is prime to p, and no lower prime term is permitted. The exact D1 coefficient equation itself forces f_i,j0(z)=c_i z, including the possibility c_i=0; no unsupported nonvanishing for individual z is assumed.',
  'If one c_i is nonzero, the terminal break is D2-j0, strictly above the terminal critical break. The same actual terminal action forces the same nonzero prime degree in the other model. The full terminal-plane scalar/Frobenius contradiction applies again.',
  'If both c_i vanish, any higher-break nonterminal element would move all fixed points strictly later than D1. All nonterminal elements therefore have break a0; the leading quotient W/U is a full two-plane, and lambda_i(g)=(A/p)d_i^(1-q)d_g^p again makes the full first-layer maps scalar-proportional, contradicting Frobenius.',
  'Only actual wild order p^4 with irreducible residual inertia is excluded. Together with B79, remaining orders are p^5 through p^8, while reducible residual comparisons and the unrestricted index in{2,3} stay open. No CM extension, existence or full recovery is inferred.'
 ],
 'dependencies_read_scope':'Complete B79 was freshly read during the immediately preceding B80 audit, and complete B80 including every coefficient and Cartan proof was read in this root pass before B81. Their hypotheses and conclusions were explicitly reapplied at the actual common field.',
 'primary_source_scope':'No new original-source reading. The earlier fully recorded coefficient-ring source scope is retained; no finite-level quadratic action is promoted to a CM theorem.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'isolated_program':str(dest.relative_to(w)),'author_output_sha256_before_and_after':before,
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'independent_runtime_seconds':independent['runtime_seconds'],'wall_seconds':wall,
 'author_runtime_seconds':original['runtime_seconds'],'all_mathematical_fields_equal':True,
 'counts':independent['counts'],'executed_failures':[]}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for label in record['labels']:
  writer.writerow([label,now,record['reviewer'],'targeted proof check / unchanged independent exact-program rerun',
    'PASS: complete proof and checker read; low, high and boundary coefficient cases rederived. Literal isolated rerun agrees in all mathematical fields and preserves author output. See outputs/root_B81_audit.json.'])
 for label in ['lem:B-RD79-layers','prop:B-RD79-minimal','lem:B-RD80-first','thm:B-RD80']:
  writer.writerow([label,now,record['reviewer'],'used and rechecked in this run',
    'Complete actual-field layer and coefficient arguments read in the same root pass and explicitly reapplied for B81 without a CM inference. See outputs/root_B81_audit.json.'])
print(json.dumps(record,indent=2))
