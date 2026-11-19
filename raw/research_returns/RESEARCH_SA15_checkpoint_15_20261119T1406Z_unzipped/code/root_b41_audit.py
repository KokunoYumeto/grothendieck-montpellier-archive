"""Root proof audit and preserved universal 3-isogeny/quotient certificate."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_c3_isogeny_exclusion.py'
author=program.with_suffix('.output.json');dest=w/'outputs/root_verify_c3_isogeny_exclusion.json'
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
    (w/'outputs/root_verify_c3_isogeny_exclusion.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD41-isogeny','independent re-proof','PASS: entire proof/code read. Root independently derived the rational Y-coordinate from completed-square differential normalization. Universal target equation, pole divisor2(O+T−T), nonzero discriminant, degree3, origin-preserving group law and exact kernel checked. Invariant and specialized j formulas verified. The rational-three-point source is the already read Fisher4.1p8; quotient is proved explicitly here.'),
('prop:B-RD41','independent re-proof','PASS: full proof independently checked. Common twist removes C6; unique invariant rational3 line is carried by any27 isomorphism. The exact finite-group-scheme preimage T={P:9P in C} lies inE[27], and T/C=E1[9]. Rational Dieudonne/isogeny preserves special characters. Both quotient j-valuations are>=6, contradicting every quotient residual alternative through B37,B38,B39. Thus the complete C3/C6 level27 branch is excluded, leaving only C4 with individual3/6,j6/6,joint18 and B40 antisymplectic orientation.'),
('prop:B-RD41','computation or formal certificate',f"PASS: author-preserving full root rerun in{out['elapsed_seconds']}s. Universal isogeny substitution/differential, exact c4/Delta/j,1002valuation cases, unique invariant line, and actual729→243→81 finite module quotient checked. Remaining C4 existence is not decided.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: elimination by the rational three-isogeny\n\nThe source point/order-three convention is Fisher4.1p8, already read in the original. The quotient curve and map are not imported from an unseen formula: the rational map, normalized differential, pole degree, kernel and invariant polynomials are fully proved in B41 and checked by a universal exact certificate. Root independently derived the Y-coordinate using completion of the square and dX/dx. The level27-to-level9 construction is an actual Galois-equivariant finite-module quotient, not an informal level decrement. Complete root rerun {out['elapsed_seconds']}s, with the author output preserved. This excludes C3/C6 at27 and leaves only antisymplectic C4, not a complete least-index decision.\n''')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
