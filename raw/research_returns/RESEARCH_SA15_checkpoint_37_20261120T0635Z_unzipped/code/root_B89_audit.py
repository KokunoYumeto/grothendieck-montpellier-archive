"""Retain the full independent B89 proof audit and unchanged exact checker run."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_p5_cyclotomic_break_three_example_candidate.tex'
source=w/'agents/reduction_descent/code/verify_p5_cyclotomic_break_three_example.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='a7e4181ce539b437c10c124ff016c5a6a65d1c4747fda01f8958f93dd3cdfbd8'
assert sha(candidate)==expected
assert sha(source)=='6493112f34e0dce0d4a571be92c59408e9b77676e4ee664b4f4f93335015c1f0'
before=sha(author)
assert before=='455e68945c3e2678d4d2993da23f4f6590c47a837f613041daae86c37e8fd613'
dest=w/'code/audit_snapshots/B89_root_independent_certificate.py'
snapshot=w/'notes/root_B89_audited_candidate.tex'
out=w/'outputs/root_B89_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B89_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B89_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text())
independent=json.loads(dest.with_suffix('.output.json').read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(original)==mathpart(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD89-base','rem:B-RD89-scope']
record={
 'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire stable candidate and checker read; complete canonical B60 lower-break proof and B88 tame-scaling proof reread. Full field, valuation, and cyclotomic intersection argument independently rederived.',
 'proof_checks':[
  'For arbitrary algebraically closed k of characteristic5, W(k) is a complete DVR with uniformizer5. The shifted cyclotomic polynomials have Eisenstein coefficients, giving actual degrees4,20,100 and the cyclic degree25 cyclotomic tower above K1.',
  'The degree-five defining polynomial is Eisenstein at pi1. Possible extra cancellation in10+pi1^4 only raises an interior coefficient valuation and cannot change the Eisenstein conclusion. The actual field K has uniformizer t, residue k, v_K(pi1)=5 and e_K=20.',
  'Using the defining relation, x=zeta25-1-t satisfies the displayed shifted polynomial with constant valuation22, four interior valuations20, and leading coefficient1. Every interior point is strictly above the chord; each root has valuation22/5.',
  'Since mu5 lies in K, K(mu25)/K is Galois of degree dividing5. The fractional coordinate valuation forces ramification degree5 and hence total field degree5. The normalized value of x is22.',
  'Every nonidentity automorphism displaces x by (zeta5^j-1)zeta25, of normalized valuation25. The B60 fixed-residue-representative expansion has a unique leading changed term when the coordinate valuation22 is prime to5; it gives lower break25-22=3 for the actual extension.',
  'The intersection of the degree-five field K with the cyclic degree25 tower above K1 is either K1 or K. The latter possibility forces the unique cyclotomic degree-five subfield to equal K, contradicting mu25 not contained in K. Therefore K(mu125)/K has full cyclic degree25.',
  'The tame degree24 extension is disjoint from the cyclotomic degree-five extension. In the actual compositum, a uniformizer z with z^24=x0 for a uniformizer x0 of C yields equal valuations of g(z)/z-1 and g(x0)/x0-1; exponent24 is a unit. Normalization scales break3 to72.',
  'The construction realizes only a base field and cyclotomic quotients. It supplies neither a height-two BT group nor an ambiguous torsion comparison. The initially failed author structural-equality assertion is retained and is not used as evidence.'
 ],
 'source_scope':'No new external classification or source reading is claimed. The complete internal B60 and B88 dependencies were reread; B88 original Colmez input retains its earlier full root audit scope.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'author_output_sha256':before,'author_output_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'author_runtime_seconds':original['runtime_seconds'],
 'independent_runtime_seconds':independent['runtime_seconds'],
 'independent_subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'counts':independent['counts'],
 'author_retained_failure':'agents/reduction_descent/code/verify_p5_cyclotomic_break_three_example.failed_structural_equality.failure.json',
 'root_executed_failures':[],
 'scope_guard':'Base-field and cyclotomic realization only; no B4 main gate closure or full-image pair realization.'
}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
   'independent re-proof / computation or formal certificate',
   'PASS: full explicit field and valuation proof rederived; unchanged isolated checker rerun and mathematical output identical. Only base/cyclotomic realization; no BT pair. See outputs/root_B89_audit.json.'])
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('\n## Explicit base realizing the necessary cyclotomic break\n\nThe complete root B89 proof and code audit passed at '+now+'. An actual field with e_K=20 and mu5 realizes cyclotomic break3 and full cyclic order25 at level125. This invalidates an attempted impossibility shortcut, but does not construct the unresolved height-two torsion comparison or shrink that main gate. The unchanged independent checker passed in '+str(independent['runtime_seconds'])+' seconds. The initial author structural-equality failure remains preserved.\n')
print(json.dumps({k:record[k] for k in ('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))
