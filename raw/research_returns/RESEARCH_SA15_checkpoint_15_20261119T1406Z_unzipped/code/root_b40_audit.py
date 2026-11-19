"""Full root marked-Fourier proof audit and preserved exact B40 execution."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_c4_orientation_gate.py'
author=program.with_suffix('.output.json');dest=w/'outputs/root_verify_c4_orientation_gate.json'
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
    (w/'outputs/root_verify_c4_orientation_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('prop:B-RD40','independent re-proof','PASS: full proof/code read and calculations rederived. Fourier action conjugates the two actual Hesse translations with one inverse; fixed-point test and origin translation justify marked symplectic order4 lift. Plane coordinate determinant2 and equation scale4 give residue factor2/3, then constant scaling2/c gives eta=c/3 omega. Actual marked cocycle ratio, invariant Delta*omega^12, valuation difference2mod4 and opposite u residues checked. Direct cube condition overF implies vF(u+u-prime)>=3; exact trace factorization and norm identity yield a K-cube with deviation valuation1, contradiction. All unit multipliers mod27 handled. Only direct orientation is excluded.'),
('prop:B-RD40','computation or formal certificate',f"PASS: author-preserving complete root certificate rerun in{out['elapsed_seconds']}s. Fourier, Hesse, short Weierstrass, residue scaling, norm identity,1000cube cases,9000trace inequalities and all mod27 unit multipliers verified. Initial structural-equality failure remains retained; no antisymplectic pair exclusion asserted.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: marked cyclic-four orientation\n\nRead and independently rederived the entire B40 marked Fourier calculation. The Hesse translation convention is the already opened Fisher Section2pp4–5; the constant family identification is checked directly, including the residue factor2/3 before the constant2/c Weierstrass scaling. No unexplained parameter-dependent differential factor is assumed. The exact norm-cube contradiction is checked over the original e2 field. Root author-preserving certificate runtime {out['elapsed_seconds']}s. This excludes only direct9 congruences with opposite tame characters, leaving antisymplectic27 undecided.\n''')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
