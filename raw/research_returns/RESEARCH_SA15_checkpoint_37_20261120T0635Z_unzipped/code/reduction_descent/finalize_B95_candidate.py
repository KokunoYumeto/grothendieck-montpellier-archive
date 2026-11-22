from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib,re
own=Path(__file__).resolve().parents[1]
p=own/'B_remaining_tracefree_rows_candidate.tex';s=p.read_text()
prior=own/'notes/B_remaining_tracefree_rows.before_certificate.tex';assert not prior.exists();prior.write_text(s)
old='''The finite supplement will be recorded with its exact program,
output and runtime before independent audits. Its profiles are
necessary arithmetic possibilities only. The proof above supplies
the critical coefficient bound, actual field identification and
symbolic strict inequalities independently of enumeration.'''
new=r'''The retained standalone exact program
\path{code/reduction_descent/verify_remaining_tracefree_rows.py}
checks all 654 necessary conductor profiles against independent
rational Herbrand integration, the eight closed strict-gap formulas,
all four relative-field threshold maxima, 1,736 critical-bound
inequalities and 26 exact binomial coefficients. Its author run
passed at 04:39:29.825537 UTC on 20 November 2026 in
0.062296249001519755 seconds. The earlier isolated exploratory
probe and its complete output are also retained; it passed in
0.056594914000015706 seconds. No executed B95 computation failed.
The complete source, output, stdout, pre-certificate proof and exact
diff remain retained. These profiles are necessary arithmetic
possibilities only. The proof above supplies the critical coefficient
bound, actual field identification and symbolic strict inequalities
independently of enumeration.'''
assert old in s;n=s.replace(old,new);p.write_text(n)
(own/'notes/B95_certificate.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),n.splitlines(True),fromfile=prior.name,tofile=p.name)))
h=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
code=own/'code/verify_remaining_tracefree_rows.py';out=code.with_suffix('.output.json');j=json.loads(out.read_text());assert j['status']=='PASS'
now=datetime.now(timezone.utc).isoformat();labels=re.findall(r'\\label\{([^}]+)\}',n);assert len(labels)==4
r={'status':'CANDIDATE_READY_FOR_FULL_AUDITS','actual_utc':now,'candidate':str(p),'candidate_sha256':h(p),'labels':labels,'code':str(code),'code_sha256':h(code),'author_output':str(out),'author_output_sha256':h(out),'author_actual_utc':j['actual_utc'],'author_runtime_seconds':j['runtime_seconds'],'profiles':j['profiles'],'critical_bound_checks':j['critical_bound_checks'],'binomial_checks':j['binomial_checks'],'minimum_a_gap':j['minimum_a_gap'],'minimum_d_gap':j['minimum_d_gap'],'pre_certificate':str(prior),'exploratory_program':'code/probe_remaining_tracefree_rows.py','executed_failures':[],'scope':'Proposed elimination of the four remaining tracefree-first-layer rows, hence all residual-wild layer(3,4). Residual-wild full Iwahori(4,4) and irreducible-residual sectors remain; no realization or unrestricted least-index conclusion.'}
(own/'outputs/B95_candidate_record.json').write_text(json.dumps(r,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:f.write('\t'.join([now,'B95_CANDIDATE','CANDIDATE_READY','Complete four-label actual-field proof and exact finite supplement; awaiting full root and companion audits.','B_remaining_tracefree_rows_candidate.tex;outputs/B95_candidate_record.json','All programs and outputs retained; no promotion or current-gate update'])+'\n')
print(json.dumps(r,indent=2))
