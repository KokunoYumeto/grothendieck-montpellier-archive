from pathlib import Path
import hashlib,runpy,contextlib,io,json,re
from datetime import datetime,timezone
base=Path(__file__).resolve().parents[1]
author=base.parent/'monodromy/outputs/degree_three_theta_graph_checks.json'
before=hashlib.sha256(author.read_bytes()).hexdigest()
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
 runpy.run_path(str(base/'code/independent_degree_three_theta_graph_checks.py'),run_name='__main__')
(base/'outputs/independent_degree_three_theta_graph_checks.stdout.txt').write_text(buf.getvalue())
after=hashlib.sha256(author.read_bytes()).hexdigest()
assert before==after
out=json.loads((base/'outputs/degree_three_theta_graph_checks.json').read_text())
p=base.parent/'monodromy/nonordinary_ppav_degree_three_node_gluing_candidate.tex'
labels=re.findall(r'\\label\{([^}]+)\}',p.read_text())
record={'actual_utc':datetime.now(timezone.utc).isoformat(),'result':'FULL INDEPENDENT PROOF/SOURCE/CODE AUDIT PASS','candidate':str(p),'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'labels':labels,'author_output_sha256_before':before,'author_output_sha256_after':after,'isolated_output':out,'proof_scope':'All six assertions rederived: cyclic theta descent and type(1,3) eigenmap global generation including both fixed-part cases and nine-versus-six basepoints; chord/eigenprojection exceptional dimensions; characteristic-two difference cover and its fierce quadratic inertia; distinct shifted branch supports; full independent S18 factors; joint product and actual equivariant splitting; extension as section of a finite etale torsor over the full normal source Lang scheme; local torsor trivializations giving the pure selected-pair rank-one inertia; q12+q13 vertex-star and eight/ten coordinates forcing every type heart; conditional GL80 assembly.','source_scope':'Fresh full original AV9.11 and proof131–133,9.14/proof133,9.18/proof134–135 read from retained original. Existing principal theta dichotomy, three-distinct-values lemma, all-theta double-image proof, previous odd natural-block H1 argument, conditional graph proof, and just-audited no-three-torsion-triple proof reread. No new page image claimed.','limitation':'The GL80 theorem still assumes an indecomposable polarized three-neighbour; existence is a separate root assertion. No arbitrary odd-kernel theorem inferred.'}
(base/'degree_three_node_gluing_independent_audit.json').write_text(json.dumps(record,indent=2)+'\n')
with (base/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([record['actual_utc'],label,'INDEPENDENT_FULL_PASS',record['result'],record['candidate'],'degree_three_node_gluing_independent_audit.json'])+'\n')
print(json.dumps({'actual_utc':record['actual_utc'],'result':record['result'],'runtime':out['runtime_seconds'],'author_preserved':before==after,'labels':labels}))
