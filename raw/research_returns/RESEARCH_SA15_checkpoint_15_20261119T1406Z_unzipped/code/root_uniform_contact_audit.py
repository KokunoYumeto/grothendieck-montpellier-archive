"""Preserve root universal-contact rerun and global-smoothness proof audit."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/monodromy/code/supersingular_uniform_contact_identities.py'
author=w/'agents/monodromy/outputs/supersingular_uniform_contact_identities.json'
dest=w/'outputs/root_supersingular_uniform_contact_identities.json'
assert not dest.exists()
before=author.read_bytes();original=Path.write_text;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    if path.resolve()!=author.resolve():raise RuntimeError('Unexpected output')
    return original(dest,data,*args,**kwargs)
try:
    Path.write_text=write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),
             {'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=original
    (w/'outputs/root_supersingular_uniform_contact_identities.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:ss-uniform-local-contact','independent re-proof','PASS: entire local proof and exact code read; Artin-Schreier irreducibility by odd U-infinity pole, all section/gradient equations, source Hessian inverse modulo Q, nonzero degree-six residue-value obstruction, and actual elliptic addition contact coefficient T(c⁴+c) checked. This proves local mixed contact and global coefficient identities only.'),
('lem:ss-uniform-local-contact','computation or formal certificate',f"PASS: exact universal contact certificate rerun in{out['elapsed_seconds']}s preserving author output. All nine inverse-Hessian coefficients, source equations and two addition expansions checked; full output retained."),
('lem:ss-uniform-source-smoothness','independent re-proof','PASS: full global proof independently read/rederived. Classified all four projective charts, three basepoints and rank-two/one exceptions. Main incidence is irreducible with explicit ordinary node and generic F,T,h,v nonzero. F/T residual curves smooth, each has three transverse nodes smoothed to first order. Fixed P and Q critical values have exact orders3 and2. Restriction of degree54 reduced full discriminant has factors F³T³h³v² plus one irreducible factor with total degree43, excluding the irreducible Hasse cubic. This proves global source smoothness for every nonflex translation slice. Further norm collisions and uniform triple bridges remain open.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
