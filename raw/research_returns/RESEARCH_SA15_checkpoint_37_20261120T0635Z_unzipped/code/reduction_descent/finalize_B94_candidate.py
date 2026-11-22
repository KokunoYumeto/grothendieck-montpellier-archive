from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib,shutil,re
root=Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
own=root/'agents/reduction_descent'
p=own/'B_both_large_tracefree_rows_candidate.tex'
old=p.read_text()
prior=own/'notes/B_both_large_tracefree_rows.before_certificate.tex'
assert not prior.exists(); prior.write_text(old)
s=old.replace(',qquad',',\\qquad').replace('>0,qquad','>0,\\qquad')
s=s.replace('Choose actual primitive points $P_h,P_\\ell$ of order25 with\n$5P_h=e_1$, $5P_\\ell=e_2$, and lifts $P_h^+,P_\\ell^+$ of order125.',
'''Take $P_h^+,P_\\ell^+$ to be the two basis vectors of the actual
$125$-module in the chosen integral tame eigenbasis. Put
$P_h=5P_h^+$, $P_\\ell=5P_\\ell^+$, so that
$5P_h=e_1$ and $5P_\\ell=e_2$ at the first level.''')
s=s.replace('The full proofs of the invoked B60 fixed-coefficient bound, B69\nactual quotient and Newton calculation, B86 Cohen/cyclotomic\nargument, B91 actual layer reduction, B92 numerical common-high\nargument, and B93 actual-field conductor method were reread.',
'''The invoked B60 fixed-coefficient proof, B49 complete coefficient
argument, B69 complete actual quotient/Newton proof, B86 complete
Cohen/cyclotomic proof, B91 layer reduction, B92 numerical
common-high proof, and B93 actual-field conductor argument were
reread in their retained canonical forms.''')
s=s.replace('note remain retained. A final dated certificate paragraph will be\nadded before independent audits.',
'''note remain retained. The checker enumerates all 390,625 matrices,
12 actual point/division-field image maps, 125 terminal determinants,
31,250 relative-quotient products, 25 powers of the actual cyclic
lower-root subgroup, and 625 tracefree conjugations. It independently
reconstructs the four mixed coefficient rows and all 18 conductor
profiles. The corrected author run passed at 04:25:12.551765 UTC
on 20 November 2026 in 1.2287049839942483 seconds. The initial run
failed only in its final redundant character census, whose loop
started the second odd parameter at an even integer; every preceding
matrix and conductor check had passed. Its exact source, failure
output and stdout are preserved, and the loop correction is retained.
No initial failed output was overwritten without a preserved copy.''')
assert ',qquad' not in s and '>0,qquad' not in s
p.write_text(s)
(own/'notes/B94_certificate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(prior),tofile=str(p))))
def h(x):return hashlib.sha256(x.read_bytes()).hexdigest()
code=own/'code/verify_both_large_tracefree_rows.py';out=code.with_suffix('.output.json')
j=json.loads(out.read_text());assert j['status']=='PASS'
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==7
rec={'status':'CANDIDATE_READY_FOR_FULL_AUDITS','actual_utc':now,'candidate':str(p),'candidate_sha256':h(p),'labels':labels,'code':str(code),'code_sha256':h(code),'author_output':str(out),'author_output_sha256':h(out),'author_actual_utc':j['actual_utc'],'author_runtime_seconds':j['runtime_seconds'],'counts':j['counts'],'prior_source':str(prior),'prior_source_sha256':h(prior),'diff':'notes/B94_certificate.diff','initial_failure':'notes/B94_initial_pair_enumeration_failure','scope':'Six necessary both-large parameter pairs excluded only in layer shape(3,4), pending full independent proof/code audits. Four(3,4) pairs, all(4,4), irreducible residual and unrestricted least index remain open. No realization inferred.'}
(own/'outputs/B94_candidate_record.json').write_text(json.dumps(rec,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 f.write('\t'.join([now,'B94_CANDIDATE','CANDIDATE_READY','Complete seven-label actual-field proof and finite supplement retained; awaiting two full audits.','B_both_large_tracefree_rows_candidate.tex;outputs/B94_candidate_record.json','Exact author run and initial failed final-census loop preserved; no promotion or main-gate update'])+'\n')
print(json.dumps(rec,indent=2))
