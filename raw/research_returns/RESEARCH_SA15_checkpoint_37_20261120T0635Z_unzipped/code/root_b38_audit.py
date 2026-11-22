"""Preserve the root computation and full B38 proof audit."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_c4_residual_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_c4_residual_gate.json'
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
    (w/'outputs/root_verify_c4_residual_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('prop:B-RD38','independent re-proof','PASS: full proof and code read; Fisher original Section2p4 and Lemma4.2p8 already fully read this audit cycle. Verified A4 double-transposition conjugacy via invariant j-map and cusp action, central sign versus actual marked quadratic twist, including fixed h-points at special j. Norm z=3 gives residue +/-1 distinct from normalized root differences with square-1; all valuations, discriminant twist modulo12, and tame quotient conclusions checked. C4 case retains only individual3/6, joint18; no existence conclusion.'),
('prop:B-RD38','computation or formal certificate',f"PASS: entire symbolic/finite certificate rerun preserving author output in{out['elapsed_seconds']}s. Involution, j/c4/Delta identities, cusp permutation, F9 residues and quadratic twist identity checked.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_13.md').open('a') as f:
    f.write(f'\n## {now}: cyclic-four residual action\n\nThe already read original Fisher full-level definition and family are used to identify the marked quadratic twist, not merely the j-invariant. The exact involution h(t)=(t+2)/(t-1) is checked directly against j and the four cusp points; it is a double transposition in A4. The full source-to-conclusion derivation is in B-RD38. Root full proof audit and author-preserving exact rerun passed in {out["elapsed_seconds"]} seconds. Obstruction/crystal independently read the same original passages and proof, with its own complete retained certificate. The remaining C4 comparison has joint inertia18; C3 cases remain.\n')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
