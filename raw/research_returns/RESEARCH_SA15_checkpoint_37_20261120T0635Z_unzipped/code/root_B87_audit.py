"""Retain complete B87 root proof/code audit and an unchanged isolated run."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_p5_tame_full_first_layer_candidate.tex'
source=w/'agents/reduction_descent/code/verify_p5_tame_full_first_layer.py'
author=source.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='ec7c365f216d6f8d5d44f86dab22bee217f6a7eac6ca96cba03a36b999361bf5'
assert sha(candidate)==expected
assert sha(source)=='18440404e3b7986fcdff83dd6e3b527f1bdaca949571338e97f0f4199e82479e'
before=sha(author)
assert before=='d5e9383836cb488b7ad210247bf36ea637a386e42baae2bd11b2090d4613ed15'
dest=w/'code/audit_snapshots/B87_root_independent_certificate.py'
snapshot=w/'notes/root_B87_audited_candidate.tex';out=w/'outputs/root_B87_audit.json'
assert not dest.exists() and not snapshot.exists() and not out.exists()
shutil.copy2(source,dest);shutil.copy2(candidate,snapshot)
start=time.perf_counter()
run=subprocess.run([sys.executable,str(dest)],cwd=w,capture_output=True,text=True)
wall=time.perf_counter()-start
(w/'outputs/root_B87_independent_stdout.json').write_text(run.stdout)
(w/'outputs/root_B87_independent_stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
original=json.loads(author.read_text());independent=json.loads(dest.with_suffix('.output.json').read_text())
mathematical=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert mathematical(original)==mathematical(independent)
assert sha(author)==before and sha(dest)==sha(source)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:B-RD87-coefficient','lem:B-RD87-fields','prop:B-RD87-three','cor:B-RD87-full','rem:B-RD87-scope']
record={'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire five-label candidate and exact checker read; all fixed-coefficient and field arguments independently rederived; complete current B84 and B85 canonical proofs reread; unchanged isolated exact supplement rerun.',
 'proof_checks':[
  'Fixed residue representatives can be chosen in O_L because the two complete fields have the same residue field. For a nonzero coefficient at exponentj, the first binomial term not divisible byp has indexp^v_p(j). Belowv_E(p), all p-divisible coefficients disappear. Asv_p(A)=1, every higher exponent divisible byp first changes later thanA+pb; the earliest prime-to-p exponentJ first changes atJ+b.',
  'When H differs from the last lineT, a nonzero element inH has breakt and displacementD1, while one inT has breaku and displacementD0<D1. The minimum m(u) is at mostD0 and m(t)<D0. Hence cancellation at the smaller break is compulsory, forcingJ=A+(p-1)t. Atu the J+u term is uniquely first, soD0=A+(p-1)t+u. All terms are below the strict mixed-characteristic cutoff; the proof does not extrapolate the finite binomial supplement.',
  'The exact quotient formula averages b+1 over a coset. A quotient not killingT has one coset element of breaku andp-1 of breakt, giving(u+(p-1)t)/p. The quotient killingT has breakt. This is the complete norm-polynomial proof in Colmez3.7, freshly read in the root B86 audit and reused here; no new Serre source reading is claimed.',
  'B84 fixes the normalized p5 parameters25,75 and residual exponents(0,6) or(12,18) in the common e1,e2 order. Tame conjugation onW1 therefore has weights18 onE12,6 onE21 and0 on diagonals. B83/B85 giveW1=span(E12,E21,diag(a,b)) withab nonzero ifdimW1=3.',
  'The actual second-level division field has additive groupW1. Evaluation on e1 and e2 has kernelsE12 andE21, hence both point fields are Galois of degree25. Their intersection is the degree5 quotient by the span of both off-diagonal axes, so the diagonal fieldD is genuinely the same field for both comparisons.',
  'Every relevant kernel is tame-stable. For a degree5 quotientF/L, if the tame uniformizer multiplier onL iszeta, then the one onF haseta^5=zeta andeta=zeta^5. The leading coefficient of tau g tau^-1 is multiplied byeta^b. Thus5b equals the quotient weight modulo24, yielding0,6,18 respectively. The diagonal quotient is nontrivial and totally wildly ramified, so its break is a positive multiple24.',
  'Distinct tame weights force each proper ramification line to be an eigenaxis. A single lower break would give identical cyclic quotient breaks, contradicting their distinct residues. Therefore there are two breaks and their last axis is detected by which displayed cyclic quotient has the larger break.',
  'The current B84/B85 inverse polygons give actual coordinate rows(95,125,2375),(15,375,1125),(5,125,2375),(45,375,1125); both intermediate vertices lie strictly above each inverse chord. Their first values have5-adic order1, and all displacements are belowv_E(5)=12000. Formal addition changes the translating coordinate by a unit.',
  'IfE1 has off-diagonal last line, the first row forceso1=6>d>=24, impossible. Otherwise its second row forcesd=72. InE2 the diagonal last line forcesd=24, whereas the off-diagonal last line forceso2=66>d=72. These exhaust all lines and exclude dimension3.',
  'B85 then forcesdimW1=4; actual fifth powers embedW1 intoW2, so both areM2(F5). The subgroup has the same order5^8 as its containing principal congruence kernel and equals it. Its determinant modulo25 has nonzero trace, hence the actual cyclotomic character onL is nontrivial andmu25 is not inK. No existence or exclusion of this full image is claimed.'
 ],
 'source_scope':'Root reuses its fresh full Colmez Proposition3.7 proof reading from outputs/root_B86_audit.json (original pp14-15); entire B84 and B85 canonical texts reread now. New uniform cancellation and tame leading-coefficient arguments are self-contained. No fresh Serre read is claimed.',
 'program':str(source.relative_to(w)),'program_sha256':sha(source),
 'author_output_sha256':before,'author_output_unchanged':True,
 'independent_program':str(dest.relative_to(w)),
 'independent_output':str(dest.with_suffix('.output.json').relative_to(w)),
 'independent_output_sha256':sha(dest.with_suffix('.output.json')),
 'author_runtime_seconds':original['runtime_seconds'],
 'independent_runtime_seconds':independent['runtime_seconds'],
 'independent_subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'counts':independent['counts'],'executed_failures':[],
 'scope_guard':'Only p5/e20 residual-tame actual125 comparison. Other residual sectors and the unrestricted least index in{2,3} remain open.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/root_check_events.tsv').open('a',newline='')as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
  'independent re-proof / computation or formal certificate',
  'PASS: complete actual-field and uniform coefficient proof rederived; entire checker read and rerun unchanged in isolation, all mathematical output identical. Details: outputs/root_B87_audit.json. Only the p5 residual-tame sector; full5^8 image not realized or excluded.'])
with(w/'notes/ROOT_SEARCH_LOG_31.md').open('a')as f:
 f.write('\n## B87 actual point-field quotient audit\n\n'+now+': full root proof and exact checker audit passed against candidate SHA256 '+expected+'. The full current B84/B85 proofs were reread; the earlier fresh full Colmez3.7 root reading is reused with its exact scope. The isolated unchanged certificate passed in '+str(independent['runtime_seconds'])+' seconds, with every mathematical output identical and author bytes preserved. The surviving full5^8 image is only a necessary condition, not an existence claim.\n')
print(json.dumps({k:record[k]for k in('status','actual_utc','candidate_sha256','independent_runtime_seconds','all_mathematical_output_identical','counts')},indent=2))
