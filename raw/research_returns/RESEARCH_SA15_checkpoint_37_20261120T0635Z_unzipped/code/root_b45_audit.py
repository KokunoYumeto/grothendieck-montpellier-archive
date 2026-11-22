"""Full dyadic logarithm audit and author-preserving exact certificate rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_p2_height_two_log_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_p2_height_two_log_gate.json'
assert not dest.exists()
before=author.read_bytes();old_write=Path.write_text;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    assert path.resolve()==author.resolve()
    return old_write(dest,data,*args,**kwargs)
try:
    Path.write_text=write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=old_write
    (w/'outputs/root_verify_p2_height_two_log_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD45','independent re-proof','PASS: entire lemma and full prior B33/B34 graph and logarithm proofs read and independently rederived. The order-three projector is integral on two-primary groups, graph closure stays self-orthogonal, and unique one-variable closed subgroups force ker(F^r) in both factors. Target degree-at-least-four special two-series gives q_next=min(a+q,1+2q,4q); logarithm differential coefficients give v(c_alpha)>=-a floor(log2|alpha|), so q>a suffices. Root freshly opened/read the published Bondarko original: p663 explicitly allows p2, Theorem2(8)/eq6 p668, Propositions6/8 pp673-674, Propositions9-12/Lemma3 pp674-676, and complete Proposition16 p681. The integral Omega action preserves valuation ideals, J=2R, bounded projection and saturation identify the finite special kernel. Applying this to P -> (P/H_n) x M kills ker(F^n) by F^u only if u>=n. No finite-level full-faithfulness or closed-immersion assumption has been substituted.'),
('thm:B-RD45','independent re-proof','PASS: the B44 mixed-case exclusion and exact-elliptic reduction leave joint inertia m=3*2^r, 0<=r<=6. At absolute e1 this is a=v_L(2). Root separately checked the exceptional a3 sequence1,3,6 and crossing2; for r>=1 crossing is r+1. Thus levels16,32,64,128 leave respectively joint degrees24/48/96/192,48/96/192,96/192,192; level256 leaves none. B43 gives lower manuscript index3 and n8 gives upper index7. This proves3<=nu_min(2,1,2)<=7, with no existence claim for any remaining row.'),
('B45-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: entire code read and rerun without changing author output in {out['elapsed_seconds']}s. Cubic projector, seven ramification sequences, five necessary-condition rows,192000 logarithm-degree cases and24576 coefficient-valuation cases pass. The universal Cartier and graph proof was separately checked, not inferred from the finite arithmetic tests.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_16.md').open('a') as f:
    f.write(f'''\n## {now}: full B45 dyadic graph and logarithm audit\n\nRoot read and independently rederived the complete B45 proof, the complete preceding B33/B34 graph and Cartier-module proofs, and the exact B45 program. The author-preserving rerun passed in {out['elapsed_seconds']}s, with192000 logarithm-degree and24576 coefficient-valuation checks. The published Bondarko original was actually reopened via its cached original reference after a direct hashed-URL request redirected to a homepage. The successful original URL is https://www.mathnet.ru/links/143cd4ef0c053a08f030f68ecac286cd/im691_eng.pdf; exact passages read were p663, Theorem2(8)/eq6 p668, Propositions6/8 pp673-674, Propositions9-12/Lemma3 pp674-676, and all of Proposition16 p681. The special role of p2 was checked explicitly: the paper imposes no p>2 restriction, and its coefficient ideal is J=2R. The original statement's field wording was requested to specify a complete discretely valued mixed-characteristic(0,2) field. Both substantive assertions pass. The bound3<=nu_min(2,1,2)<=7 narrows the open gate but does not settle16-torsion sufficiency. No finite decision procedure for curve pairs has been executed.\n''')
summary={'status':'PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],'events':len(events),'new_bound':'3<=nu_min(2,1,2)<=7'}
(w/'outputs/root_b45_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
