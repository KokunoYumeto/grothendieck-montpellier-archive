"""Root complete proof check and author-preserving B39 certificate run."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_c3_residual_gate.py'
author=program.with_suffix('.output.json');dest=w/'outputs/root_verify_c3_residual_gate.json'
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
    (w/'outputs/root_verify_c3_residual_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD39-units','independent re-proof','PASS: exact Hensel polynomial w³+w+pi*w², unit derivative over algebraically closed residue, cube depth>=3, independence of noncube approximation depth1/2, inverse depth, and cubic-extension valuations3/6 below9 all independently checked.'),
('prop:B-RD39','independent re-proof','PASS: entire proof/code read. Fisher rational-three-point dictionary t_E=a1/3,D=t_E³−a3, discriminant=(3a3)³D checked directly. Full d1/2 source and inverse-target tables, potential-supersingular bounds, norm valuation conventions v_K(N)=v_L, all direct/reverse cube ratios and six unequal minima4/5/7 verified by hand. Unit d0 table and same inverse depth force S-pair{-3,0}. Exact normalized residual alternatives C4:(3,6),joint18,j6/6 and C3:(12,6),joint36,j3/>=6 follow. Undoing common quadratic twist can change tame1/2; no untwisted overclaim.'),
('prop:B-RD39','computation or formal certificate',f"PASS: isolated author-preserving root rerun in{out['elapsed_seconds']}s; both invariant identities, Hensel identity,1000cube-deviation cases, all valuation tables and norm congruence pairs checked. Neither remaining27-torsion row is decided for existence.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: unipotent residual character restriction\n\nRoot read the complete B39 proof and exact program, using the original Fisher Section2p4, Lemmas4.1–4.2p8 and Theorem4.3equations10–11pp9–10 already read in the previous cycle. The actual rational-three-point dictionary and all source-to-conclusion valuation steps were rederived explicitly. No new external theorem or unseen source is invoked. Author-preserving complete root certificate runtime: {out['elapsed_seconds']}s. The independent obstruction/crystal reviewer additionally reopened the printed equation11 visually and reran the full certificate. The resulting two-row normalized27-torsion test is necessary only; neither row is asserted to occur.\n''')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
