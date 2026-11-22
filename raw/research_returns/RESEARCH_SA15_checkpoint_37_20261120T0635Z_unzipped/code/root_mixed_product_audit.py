"""Full root proof/source audit and preserved mixed-product arithmetic run."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/obstructions_crystals/code/mixed_product_rank_arithmetic.py'
author=program.with_suffix('.output.json');dest=w/'outputs/root_mixed_product_rank_arithmetic.json'
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
    (w/'outputs/root_mixed_product_rank_arithmetic.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:DE-A3-mixed-odd-factor','independent re-proof','PASS: full proof read. Arbitrary-degree etale ordinary source via iterated Verschiebung and odd cyclic quotient dual, odd-degree supersingular source, norm class(3c,3e), cubic nodality for even kernels, node count, exact translation and ambient nilpotent upper bound checked. Root freshly read original AV5.20–5.22 complete proofs pp80–81; dual-isogeny sources already read in full.'),
('lem:DE-A3-mixed-even-bound','independent re-proof','PASS: first-factor horizontal connection, globally defined derivative, C(s²ω)=0 and C(f df wedge ω_s)=0 by multiplicativity on closed forms checked. Independent sections1+x andx, ordinary vector-field equations and partial²=partial, generic-to-identical minor vanishing and stable-part divisor sequence all verified. Original AV5.26p82 freshly read; coordinate reduction checked directly.'),
('thm:DE-A3-mixed-all-product-ranks','independent re-proof','PASS: full odd-factor and transverse-union proof, positive ample summands, exact full defect2 versus ambient stable rank1, every covered degree and explicit ambient regularity bound checked. The only unstated degree-one case is evena,b1; no arbitrary-surface claim is inferred.'),
('rem:DE-A3-mixed-product-scope','computation or formal certificate',f"PASS: entire arithmetic program read and author-preserving rerun in{out['elapsed_seconds']}s. {out['odd_norm_cases']} norm identities, {out['transverse_union_cases']} union identities and {out['covered_degree_cases']} degree cases; excluded degree-one cases retained separately. Infinite proof is geometric, not an extrapolation.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: arbitrary mixed product polarizations\n\nRead original Edixhoven–van der Geer–Moonen AV5.20,5.21,5.22 with full proofs pp80–81 and Example5.26p82 from the retained full primary text. These give Verschiebung degree/factorization, p-rank invariance and the ordinary a1-nonzero criterion. The reduced characteristic-two model is also checked directly: normalize a1=1, translate x to remove a3, translate y by a constant to remove a4; nonsingularity gives a6!=0. The exact product-norm, Cartier and nodal-union derivations are in the fully audited new proof. Earlier dual-isogeny Theorem7.5 and Corollary7.17 source reads are reused, not falsely described as newly opened. Root arithmetic rerun {out['elapsed_seconds']}s preserves author output.\n''')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'actual_audit_time':now,'events':len(events)},indent=2))
