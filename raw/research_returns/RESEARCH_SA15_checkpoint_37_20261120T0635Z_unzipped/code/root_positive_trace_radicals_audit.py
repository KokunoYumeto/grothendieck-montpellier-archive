"""Root proof audit of trace radicals and an author-preserving finite probe rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/obstructions_crystals/code/post_CP17_variation_weight_probe_v2.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_post_CP17_variation_weight_probe_v2.json'
summary=w/'outputs/root_positive_trace_radicals_audit.json'
assert not dest.exists() and not summary.exists()
before=author.read_bytes();old_write=Path.write_text;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    assert path.resolve()==author.resolve()
    return old_write(dest,data,*args,**kwargs)
try:
    Path.write_text=write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),
             {'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=old_write
    (w/'outputs/root_post_CP17_variation_weight_probe_v2.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='COMPLETED_FINITE_PROBE'
assert out['source_variation']==out['toral_source_variation']==[0,0]
assert [x['rank'] for x in out['weight_spaces']]==[1,2]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:DE-A3-positive-trace-radical','independent re-proof',
 'PASS: complete proof and its earlier double-corank diagram independently rederived. Bijective induced Cartier on W/R and full kernelR give W=R plus imageCartier. The toral idempotent makes trace surjective separately on each weight, so weight-i lifts q_i of s_i exist. Their Cartier images lie in pullW; adding pullw_i reduces them to pullR. Nonzero independent traces then make their classes a basis of the two-dimensional kernel on tildeW/pullR, dual to the restricted coherent Frobenius cokernel. The variation coefficient is the stated trace/Cartier Serre pairing. In directionq_i the correction term beta(s_i,w_j)=beta(s,(w_j)_i) lies in imageCartier and is annihilated by the Frobenius kernel. Off-diagonal products have toral weight1 and zero Cartier; diagonal squares have zero Cartier because A is mixed. Both trace directions s0,s1 therefore vanish. This uses W/R and does not reinstate the previously refuted factorization through the Cartier cokernel. Frobenius twists preserve the zero identities over the stated perfect base.'),
('lem:DE-A3-positive-matrix-ruling','independent re-proof',
 'PASS: entire elementary proof rederived. Normalize one nonzero rank1 matrix to diag(1,0). The determinant polynomial along A+tB forces b22=0, and detB=0 forces b12*b21=0. A vector space cannot be the union of two proper linear subspaces; hence either all second columns vanish or all second rows vanish. These are precisely a common kernel line or a common image line, including the zero matrix-space case. The lemma supplies an exact alternative, and neither geometric exclusion is claimed.'),
('POSITIVE-TRACE-RADICAL-FINITE-PROBE','computation or formal certificate',
 f"PASS as a finite probe only: root read the entire v2 program, its trace-projection and etale-double probe dependencies, and the imported original mixed Cartier functions. The author-preserving rerun took{out['elapsed_seconds']} seconds. At source68667 overF2, both toral spaces have dimension9, their variation-image dimensions are1 and2, and the source and toral-source directions have zero variation. This confirms the recorded sample and does not prove uniform nonvanishing, image dimensions, or either matrix-ruling exclusion.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
record={'status':'PASS','actual_utc':now,'complete_mathematical_assertions':2,
        'events':len(events),'finite_probe_runtime_seconds':out['elapsed_seconds'],
        'source_section':out['source_section'],'remaining_gate':'Exclude both common matrix rulings; no uniform determinant nonvanishing proved.'}
summary.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
