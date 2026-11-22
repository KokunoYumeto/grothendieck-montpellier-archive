"""Independent full-proof record and author-preserving cross-Cartier rerun."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,shutil,subprocess,sys,time

work=Path(__file__).resolve().parents[3]
agent=work/'agents/monodromy'
other=work/'agents/obstructions_crystals'
source=other/'post_CP29_ss_product_dual_Cartier_candidate.tex'
program=other/'code/verify_ss_product_cross_Cartier.py'
author=program.with_suffix('.output.json')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before={str(p.relative_to(work)):sha(p) for p in (source,program,author)}
assert sha(source)=='6bfbdec7f65a16c39f6094e86485364ad685c80d87ce23ad14cec266e495ba18'
folder=agent/'outputs/independent_ss_product_cross_Cartier'
folder.mkdir(parents=True,exist_ok=True)
copy=folder/program.name
shutil.copy2(program,copy)
t=time.perf_counter()
run=subprocess.run([sys.executable,str(copy)],capture_output=True,text=True)
(folder/'stdout.txt').write_text(run.stdout)
(folder/'stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
result=json.loads(copy.with_suffix('.output.json').read_text())
old=json.loads(author.read_text())
for key in ('status','checks','check_count','twisted_determinant','one_trivial_schur','untwisted_8_minor','scope'):
    assert result[key]==old[key],key
assert {str(p.relative_to(work)):sha(p) for p in (source,program,author)}==before
now=datetime.now(timezone.utc).isoformat()
assertions=[
 {'label':'lem:DE-SS-cross-elliptic','verdict':'PASS','details':'The two degree-three divisor spaces and their rational bases are correct. Multiplication by x+a gives the exact product trivialization. Relative Cartier fixes base coefficients, and all nine p-basis decompositions, the target twist, determinant and reversal coefficient were independently rederived.'},
 {'label':'lem:DE-SS-cross-product','verdict':'PASS','details':'Kunneth gives the tensor blocks. The one-trivial-coordinate matrix is not assumed symmetric; its actual Schur complement is the displayed determinant-one matrix. The untwisted tensor separates into three exchanged pairs and the rank-two diagonal block.'},
 {'label':'thm:DE-SS-odd-pullback-dual-rank','verdict':'PASS','details':'The connected odd-etale eigensheaves are distinct degree-zero lines, and Frobenius relabeling preserves the trivial character. A functional on the trivial target pairs precisely inverse characters; the finitely many determinant opens meet. Alternation and odd dimension supply the matching upper bound.'},
 {'label':'cor:DE-SS-odd-rectangle-dual-rank','verdict':'PASS','details':'The fully reread explicit quaternion norm lemma gives odd-degree etale self-isogenies. Inverse-pair cancellation of their kernel sums proves exact pullback line classes and the stated rectangle dimension.'},
 {'label':'rem:DE-SS-cross-scope','verdict':'PASS','details':'The theorem proves only maximal dual alternating rank on the specified odd-etale product pullbacks; it asserts neither indecomposable-ppav cross nonvanishing nor new full monodromy.'}
]
record={'status':'PASS_FULL_PROOF_AND_CODE_AUDIT','actual_utc':now,'source':str(source.relative_to(work)),'source_sha256':sha(source),'assertions':assertions,'author_output_sha256':sha(author),'author_bytes_preserved':True,'independent_output':str(copy.with_suffix('.output.json').relative_to(work)),'exact_runtime_seconds':result['runtime_seconds'],'isolated_wall_seconds':time.perf_counter()-t,'scope':'Complete final file and exact program read, all five assertions independently rederived; full original internal quaternion-norm proof reread. No fresh external-source access is claimed. Exact polynomial identities are distinguished from geometric basis and character arguments.'}
out=agent/'outputs/independent_ss_product_dual_Cartier_audit.json'
out.write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as handle:
    writer=csv.writer(handle,delimiter='\t')
    for assertion in assertions:
        writer.writerow([assertion['label'],now,'/root/monodromy','FULL-PROOF-CODE-AUDIT-PASS',assertion['details']])
print(json.dumps({'status':record['status'],'actual_utc':now,'source_sha256':sha(source),'record':str(out.relative_to(work)),'runtime_seconds':result['runtime_seconds']},indent=2))
