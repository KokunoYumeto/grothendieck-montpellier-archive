from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, difflib

own=Path(__file__).resolve().parents[1]
source=own/'B_residual_wild_last_crossing_candidate.tex'
program=own/'code/verify_residual_wild_last_crossing.py'
output=program.with_suffix('.output.json')
prior=own/'notes/B_residual_wild_last_crossing.before_certificate.tex'
record_path=own/'outputs/B93_candidate_record.json'
assert not prior.exists() and not record_path.exists()
data=json.loads(output.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert data['status']=='PASS' and data['source_sha256']==sha(program)
before=source.read_text()
old='''original-source opening is claimed here. The exact numerical
supplement and its actual execution provenance will be
appended after execution; no finite arithmetic row is used
as an existence assertion.'''
new=r'''original-source opening is claimed here. The retained original
source conventions are the full Cohen proof and the different,
subgroup and quotient Herbrand proofs already checked in B86--B90
\cite{Stacks032A,ColmezCorpsLocaux}.

The standalone exact supplement
\path{code/reduction_descent/verify_residual_wild_last_crossing.py}
checks all 35 displayed normal-closure arithmetic cases without
asserting their existence, enumerates all 390,625 actual matrices
of the full parahoric group and reconstructs their ten point/field
images, stabilizers and the two intersections. It independently
performs the rational Herbrand conversions, the coset average and
all 125 terminal determinant checks. The bounds 275,496 and
70,296 are strictly below the cyclotomic lower bound 391,896,
with gap 116,400. The first author run passed at
03:48:13.668022 UTC on 20 November 2026 in
0.6302177960023982 seconds. No executed computation failed.
The full source, output, pre-certificate version and exploratory
provenance note are retained. These finite checks supplement the
actual field proof; no finite arithmetic row is used as an
existence assertion.'''
assert old in before
after=before.replace(old,new)
prior.write_text(before)
source.write_text(after)
(own/'notes/B93_certificate.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=str(source)+':before',tofile=str(source)+':after')))
labels=re.findall(r'\\label\{([^}]+)\}',after)
assert len(labels)==5
now=datetime.now(timezone.utc).isoformat()
record={'status':'CANDIDATE_READY_FOR_FULL_INDEPENDENT_AUDITS','actual_utc':now,'candidate':str(source),'candidate_sha256':sha(source),'labels':labels,'program':str(program),'program_sha256':sha(program),'output':str(output),'output_sha256':sha(output),'author_actual_utc':data['actual_utc'],'author_runtime_seconds':data['runtime_seconds'],'scope':'Actual remaining residual-wild crossing(5,45) excluded by upper bounds on the two terminal diagonal characters and a lower bound on the same cyclotomic determinant. Both-large and irreducible-residual branches remain open; no least-index closure.','source_scope':'Self-contained degree-five normal-closure/different derivation. Prior full Cohen and Colmez different/Herbrand source conventions reused; no fresh external opening claimed. Full invoked internal B60/B86/B88-B92 arguments rechecked.','executed_failures':[],'exploratory_provenance':'notes/B93_exploratory_provenance.md','preserved_prior':str(prior)}
record_path.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'CANDIDATE_AUTHOR_CHECKED',record['scope'],source.name+';outputs/B93_candidate_record.json','Complete author proof and retained exact checker PASS; full independent audits pending'])+'\n')
print(json.dumps(record,indent=2))
