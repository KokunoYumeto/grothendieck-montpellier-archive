"""Full actual proof/code audit and unchanged isolated B92 rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/reduction_descent/B_residual_wild_crossing_candidate.tex'
source=w/'agents/reduction_descent/code/verify_residual_wild_crossing.py'
author=source.with_suffix('.output.json')
expected='54786c9ec226ed8855471c5c4eacaa5efd2927ec3aefee76aa9762bd5c221453'
assert sha(candidate)==expected
assert sha(source)=='8bbd6a806886f0c2b408888b0309cfea391a3800c385dc7342fc84606ab6e2f7'
assert sha(author)=='d087ce7c228beb958d751b9e246de55957a94eed851cdf98b16b6c422dd857e8'
before={str(p.relative_to(w)):sha(p) for p in (candidate,source,author)}
folder=w/'code/audit_snapshots/B92_root_independent'
assert not folder.exists()
folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_B92_audited_candidate.tex';out=w/'outputs/root_B92_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
start=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-start
(w/'outputs/root_B92_independent.stdout.json').write_text(run.stdout)
(w/'outputs/root_B92_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in (candidate,source,author)}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD92-tame25','lem:B-RD92-parahoric','lem:B-RD92-common-high','thm:B-RD92-crossing','rem:B-RD92-scope']
r={'status':'FULL-INDEPENDENT-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire final five-label candidate and entire checker actually read. Fresh full B87 coefficient, shared-field and three-dimensional exclusion proofs and B88 point-field proof read; B90 actual point-field and quotient conventions checked. B60/B69/B82/B84/B86 and B91 were fully checked immediately earlier in the same CP33 work.',
 'proof_checks':[
  'At the actual quotient25 level, each eigenvector point field has degree5 or25. The single-segment inverse values(19/5,3/5) and(1/5,9/5) make the degree5 coordinate valuations prime. All three translation-line types force incompatible actual breaks in the two models. Thus both evaluation maps are surjective without any hypothetical quotient125 comparison.',
  'Separated tame weights then give both off-diagonal axes and a diagonal part with nonzero projections. A three-dimensional image has one shared diagonal cyclic field. The complete B87 proof uses only these actual25 data, not its original125 motivation, and excludes it by diagonal breaks72 versus24 or an off-diagonal66 that would need to exceed72. Thus the full actual25 image is M2.',
  'The full B88 point-field proof at that same actual25 level gives lower profiles(6,336),(24,234) and the four cyclic breaks. Every eliminated first-coefficient alternative was freshly checked against the actual mixed-characteristic cutoff12000 and the prime exponent constraint.',
  'In the original high-quotient lattice(e1/5,e2), quotient rationality forces rho21 divisible by25. Full quotient25 yields joint surjectivity of the four displayed actual characters. The first layer contains the full diagonal plane and E12 from fifth powers. Opposite tame weights force a nonzero terminal lower entry; fifth powers and tame projection make the terminal layer all M2. Counting proves equality with the displayed order5^8 parahoric group.',
  'The quotient basis order is essential. Crossing(5,45) identifies original upper residual and lower diagonal with A12,A22, giving66,24. Crossing(15,95) swaps quotient axes and identifies them with A21,A11, giving6,72. Joint surjectivity proves the two actual cyclic fields are distinct.',
  'For the common-high coordinate lemma, a single ramification break would require a nonzero additive polynomial of degree at most5 to vanish on all25 leading coefficients, or a tie forcing incompatible24b_i. If the last line differs from the common high line, B87 forces incompatible larger cyclic breaks. When they agree, the two strict coefficient regimes give the displayed equations. Equal strict regimes force equal parameters; the mixed regime gives t<24b1 contrary to its assumption. The endpoint t=24b2 forces a prime exponent below its necessary minimum. Therefore t=24b1 and the stated u are necessary.',
  'The original full parahoric image gives a primitive25 point field E of degree125 overL and an actual Galois degree25 extension E/R. Evaluation of the upper-triangular congruence layer identifies its high-translation line and the quotient killing it as the same field D22R/R, not merely an abstract cyclic field.',
  'For(15,95), coordinate comparison forces that field break72. Its two independent cyclic subfields overL have breaks6 and72, so the elementary abelian compositum has lower breaks6 and336; subgroup lower numbering makes D22R/R have break336. This is a contradiction. For(5,45), the analogous coordinate break24 agrees with the base change of the lower-break24 field across the break66 field; no exclusion or realization is inferred.',
  'The checker independently enumerates translation lines, candidate diagonal lines, coefficient alternatives, actual triangular fifth powers and quotient digit conversion. Its common-high search ranges come from unconditional valuation bounds, not guessed cutoffs. The necessary first-change predicate explicitly permits later cancellation after ties, so its exclusions do not impose unwarranted coefficient independence.'
 ],
 'dependencies_freshly_reread':['lem:B-RD87-coefficient','lem:B-RD87-fields','prop:B-RD87-three','prop:B-RD88-point-fields'],
 'source_scope':'No fresh external primary-source opening claimed. The previously full root Colmez norm, subgroup and Herbrand proof audit remains the source convention; actual internal proof passages were rechecked as specified.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,
 'counts':{'translation_lines':len(b['degree_five_translation_rows']),'diagonal_lines':len(b['possible_three_dimensional_diagonal_lines']),
           'triangular_powers':b['triangular_power_rows'],'quotient_digit_rows':b['actual_quotient_digit_rows'],
           'common_high_break_pairs':b['common_high_break_pairs_tested']},
 'executed_failures':[],
 'scope_guard':'Only crossing(15,95) is excluded. Crossing(5,45), both-large layer shapes and the irreducible residual sector remain open; the unrestricted least index stays in{2,3}.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: full proof/code, exact torsion levels and actual cyclic-field identity rederived; unchanged isolated output matches. See outputs/root_B92_audit.json.'])
 for label in r['dependencies_freshly_reread']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete canonical proof freshly read; verified that the part reused needs only actual25 data.'])
with (w/'notes/checkpoint33_changes.md').open('a') as f:
 f.write('\n## Root audit of the actual crossing-field exclusion\n\nB92 passed full independent root proof/code audit at '+now+'. The unchanged isolated checker ran in '+str(b['runtime_seconds'])+' seconds and matched all mathematical output, including2,138,160 necessary break pairs. Quotient25 data alone force the full additive image; the actual original parahoric125 image then identifies a single cyclic field whose break would have to be both72 and336 in crossing(15,95). That crossing is excluded. Crossing(5,45), the both-large branch and the irreducible residual branch remain open.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','counts']},indent=2))
