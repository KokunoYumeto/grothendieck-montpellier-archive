"""Completed full proof audit with an isolated dual-number certificate rerun."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/obstructions_crystals/code/post_CP19_GF4_cup_derivative_check.py'
dependency_names=['post_CP19_GF4_canonical_variation_probe.py','post_CP19_canonical_cup_variation_probe.py','post_CP16_etale_double_variation_probe.py','A3_mixed_product_probe.py']
dependencies=[source.with_name(s) for s in dependency_names]
author=source.with_suffix('.output.json')
author_files=[author,source.with_name('post_CP19_GF4_canonical_variation_probe.output.json')]
before={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in author_files}
program=source.read_text();needle="Path(__file__).with_suffix('.output.json').write_text"
assert program.count(needle)==1
target=w/'outputs/root_positive_cup_derivative_dual_numbers.json'
assert not target.exists()
executed=program.replace(needle,'Path('+repr(str(target))+').write_text')
snapshot=w/'code/audit_snapshots/post_CP19_GF4_cup_derivative_check_at_root_audit.py'
assert not snapshot.exists();snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_positive_cup_derivative_dual_numbers_stdout.txt').write_text(stream.getvalue())
assert before=={str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in author_files}
run=json.loads(target.read_text());assert run['status']=='PASS' and run['cases']==216
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:DE-A3-positive-cup-derivative-candidate': 'Complete corrected proof actually read and independently rederived, with explicit semilinear domains, coherent transpose and trace-splitting independence. In root coordinates U and ordinary coordinates W=U^(2), sharpness gives W=imM plus imR, PM=0 and PR=1. The deck identity for the actual trace splitting gives K(u,v)=H(u,v)+H(v,u)+B(u,v). Replacing q by q+pullLambda changes H(u,u_i) only by a vector in imM, so A=P H(u)r is independent of the splitting. Corrected trace lifts satisfy H(u,u_i)+M w_i=R A_i. Differentiation in root coordinates gives dR=0, (dP)R=0, (dP)M=P dM and hence dA_i=P B(v,w_i)+P H(v,u_i)+P H(u,v_i). Toral orthogonality and PM=0 identify this with the actual Cartier-dual root-removed variation. Its columns are dual cokernel lifts and rows dual kernel coordinates; the coherent K-to-Q matrix is the transpose of the entrywise square in actual section direction v^[2]. Thus all variations have trace zero exactly when d trA=0, equivalently trA is square in the rational parameter function field over the perfect ground field. Neither this square condition nor determinant nonvanishing is proved.',
'rem:DE-A3-positive-cup-derivative-scope-candidate': 'Entire current finite certificate and all four imported source programs actually read; their exact import cutoffs were inspected. Author-preserving dual-number rerun independently verifies all216 coordinate directions on twelve retained GF4 sharp product sources by direct bilinear Cartier evaluation and unit-pivot elimination over GF4[epsilon]/epsilon^2. The inverse formula a^-1+epsilon b a^-2 and Frobenius-root convention were checked. The numerical projection splitting need not preserve toral weights because the proved matrix A is splitting independent. This finite evidence proves neither uniform trace symmetry nor determinant nonvanishing on arbitrary mixed surfaces.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={
 'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
 'root_rerun_seconds':run['elapsed_seconds'],'directions_checked':run['cases'],
 'author_output_sha256_unchanged':before,
 'candidate_sha256':hashlib.sha256((w/'agents/obstructions_crystals/post_CP19_positive_index_cup_derivative_candidate.tex').read_bytes()).hexdigest(),
 'program_dependency_sha256':{str(p.relative_to(w)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [source]+dependencies},
 'source_scope':'Complete current derivative proof, previous toral lattice/double-corank and trace-radical proofs freshly read. Existing actual source checks underlying those proved dependencies reused; no new primary-source read is asserted by this audit.',
 'remaining_gate':'Prove the square condition for trA and exclude the common kernel/image matrix alternatives, or directly prove determinant nonvanishing. The derivative identity alone is an equivalent reduction and is not separate strict review movement.'
}
dest=w/'outputs/root_positive_cup_derivative_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
