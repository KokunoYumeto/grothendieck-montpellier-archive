"""Full root dyadic mixed-case audit, with a preserved exact certificate rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_p2_height_two_mixed_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_p2_height_two_mixed_gate.json';assert not dest.exists()
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
 (w/'outputs/root_verify_p2_height_two_mixed_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
 ('lem:B-RD44-conjugacy','independent re-proof','PASS: complete classification and integral-conjugacy proof read and rederived. The residue-unit quotient has order1/3; its normal2-subgroup has exponent<=4, unique involution and hence1,C2,C4,Q8. The order12 exclusion and C3 action give the complete seven-group list. Root checked all explicit a+i, z+zeta+1 and Hilbert90 conjugators, their valuation-one normalizers, and the labelled order24 embedding. Reduced norms are1. Original Hewett1995 Theorem1.4/Cor1.5 printedp520 actually viewed as a literature parallel; no unproved conjugacy assertion imported.'),
 ('prop:B-RD44-realization','independent re-proof','PASS: full dyadic realization proof and complete earlier B35 labelled Serre-Tate/algebraization proof reread. Integral special conjugacy preserves the entire Tate lattice. The previously opened Tate1967/Katz1.2.1/EGAIII1 existence and formal-faithfulness inputs impose no odd-prime restriction;2 is nilpotent on each O_L/pi^n. Canonical O(3zero) gives compatible ample algebraization, finite-free Hopf completeness gives exact torsion isomorphisms, and only generic polarized Galois descent is asserted.'),
 ('lem:B-RD44-point','independent re-proof','PASS: entire proof read; original Tate1975 Section4 Theorems4.1-4.2 pp41-44 and their complete formal-expansion proof read, original p46 table actually viewed. For a1 in2R, the leading2T term has strictly smallest valuation for everyv(T)>=1, giving no formal2-primary torsion. Goodss reduction has no geometric2-primary points; additive connected reduction has exponent2 and component2-primary exponent<=4. The relevant table rows precede the explicit char-not2or3 boundary, so rational2-primary torsion has exponent<=8 at e1.'),
 ('prop:B-RD44','independent re-proof','PASS: all reductions and characters rederived. Eisenstein Phi16(1+T) gives full cyclotomic mod16 image at e1, so finite sign factors cannot hide a dimension difference1or2. Height-one filtered characters are prime-to2 trace2. A transported cyclic16 summand is made rational by a quadratic twist, or after the elliptic quotient when its cyclotomic exponent is1, contradicting the no16-point lemma. Thus both groups are exact supersingular elliptic BT groups; unequal characters require exactly one inertia order divisible3, with joint order among3,6,12,24,48,96,192. No remaining16 sufficiency claim.'),
 ('B44-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: entire code read; author-preserving rerun {out['elapsed_seconds']}s.24 actual special automorphisms,576 products in both presentations, group isomorphism, quaternion normalizers,120 rational conjugacy tests,18000 valuation tests and nine determinant-dimension cases passed. The universal conjugacy and valuation statements are proved symbolically in the text, not inferred from the finite samples.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
 f.write(f'''\n## {now}: post-freeze B44 dyadic mixed-case audit\n\nRoot read and independently rederived all four B44 assertions and the entire exact program, then reran it without changing author output in {out['elapsed_seconds']}s. The original Hewett1995 scan p520, Theorem1.4/Cor1.5, was actually viewed. The www.wstein.org full-PDF request was oversized; the already indexed original non-www source opened successfully as https://wstein.org/Tables/antwerp/tate/tate.pdf, and Section4 Theorems4.1-4.2 with proofpp41-44 were read. The original p46 component/connected-group table was actually viewed and its characteristic boundary checked. B35's complete labelled realization argument and the exact prior primary-source inputs were reread. Root and OC full audits now pass; B44 remains outside the frozen CP15 paper pending post-save promotion. No assertion of16-torsion sufficiency is made.\n''')
print(json.dumps({'status':'PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],
                  'events':len(events),'paper_status':'Outside frozen CP15; promotion after save'},indent=2))
