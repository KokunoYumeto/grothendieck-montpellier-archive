"""Retain the complete root proof/source audit and author-preserving exact rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_tame_height_two_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_tame_height_two_gate.json'
summary_path=w/'outputs/root_b49_audit.json'
assert not dest.exists() and not summary_path.exists()
before=author.read_bytes(); old_write=Path.write_text; capture=io.StringIO()
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
    (w/'outputs/root_verify_tame_height_two_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text()); assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD49-point','independent re-proof','PASS: entire statement and proof independently rederived. In the normalized p-typical coordinate the terms of degrees 2 through p-1 vanish, c_p=(1-p^(p-1))u, the intermediate coefficients lie in (p,u), and c_(p²) is a unit. Every rational positive valuation is integral. If x has exact order p², its image has valuation Z<=a/(p-1)<=p²-1, so the linear and p² terms at x have valuation >Z. This forces 1<=b=v(u)<a and Z=b+pA. At its p-torsion image every term except linear and degree p is strictly higher, forcing a=b+(p-1)Z=p(b+(p-1)A), contrary to p not dividing a. The u=0, b>=a and p=2 edges were checked. Root freshly opened the original Hopkins-Gross cached PDF and read Prop5.7 with its coefficient congruence, equations12.3-12.5, and the complete written proof and arbitrary residue-extension scope of Prop12.10.'),
('lem:B-RD49-inertia','independent re-proof','PASS: the height-two Honda endomorphism division algebra has degree2, maximal-order residue F_(p²), and pro-p reduction kernel. For p>=5 an element of order p would generate a field of degree p-1>2, impossible. Every finite subgroup is therefore prime to p and injects into the cyclic residue units. The kernel of special inertia is removed by the previously proved crystalline descent plus actual-lattice quotient construction, which root reread in full in B17. Over the completed strictly henselian base, faithful good extensions are tame cyclic; their compositum degree is an lcm and still divides p²-1. No norm-one or elliptic-realization assumption is used.'),
('prop:B-RD49-mixed','independent re-proof','PASS: completed maximal unramified base change preserves e and any torsion isomorphism. A height-one filtered subgroup gives a primitive cyclic subgroup C of M[p²] with character chi^b epsilon. If b0, an inverse finite twist gives a rational p²-point. If b1, quotient by C gives a cyclic image with character epsilon0/epsilon by the determinant; its inverse twist gives the same point. Finite subgroup closures are flat over the good DVR, and quotients and finite scalar twists preserve potential good dimension1/slope1/2. The faithful tame good extension has absolute index (p-1)m, m dividing p²-1, prime to p. The rational point extends through the finite flat torsion scheme and reduces to the unique point of the connected special torsion, contradicting the preceding valuation lemma.'),
('thm:B-RD49','independent re-proof','PASS: at e=p-1 the cyclotomic image modulo p² on inertia has order p, while finite determinant characters have order dividing p-1. Their product equality forces equal dimensions d in {0,1,2}, since the dimension difference is strictly smaller than p, and equal finite determinants. Dimensions0/2 reduce to Brauer characters of generic mod-p representations; d1 reduces to height-one filtered groups or a whole potentially supersingular group. The mixed comparison has just been excluded. Two whole formal groups have a common tame good extension of degree m dividing p²-1. Freshly opened Bondarko E(1), Proposition18 and its complete E proof show that e_L<(p-1)p² allows p³ comparison to extend to an actual p-torsion model isomorphism, compatible with generic maps and hence descent. This determines the special prime-to-p character. If m<=p, the same theorem with u1 works from p². B18 supplies the strict lower bound nu>=1. Thus 1<=nu_min(p,p-1,2)<=2, and every remaining p² ambiguity has two formal groups, equal finite determinants and m>p.'),
('B49-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: full author program read and independently rerun without changing its output, in {out['elapsed_seconds']}s. The exact recursion reconstructs all coefficients through p² for p2,3,5,7,11 and verifies f([p]T)=pf(T); {out['valuation_cases']} integer cancellation configurations, {out['joint_degree_cases']} tame degree pairs and {out['determinant_cases']} determinant cases pass. These are finite auxiliary checks, not a proof of arbitrary formal-model existence or an evaluation of the remaining least index.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events: writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_17.md').open('a') as f:
    f.write(f'''\n## {now}: tame height-two minimal-ramification audit\n\nRoot independently rederived all four B49 candidate assertions and fully read its exact program. The author-preserving rerun passed in {out['elapsed_seconds']} seconds. The direct original URL https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf timed out, while its cached original was successfully opened. Root actually read Prop5.7 and the displayed coefficient congruence, equations12.3-12.5, and the complete written proof of Prop12.10, including its allowance of any residue-field extension of Fp. No visual PDF inspection is claimed. Root also freshly opened https://www.mathnet.ru/links/143cd4ef0c053a08f030f68ecac286cd/im691_eng.pdf and read TheoremE(1), Proposition18 and its entire short proof of TheoremE. The prescribed-generic-map compatibility in E is essential for descent equivariance. B17 crystalline/actual-lattice descent, B18 lower-bound construction, and B5 height-one characters were reread in full at the steps used.\n\nThe proved gate, once companion audit/promotion passes, is 1<=nu_min(p,p-1,2)<=2 for p>=5. Any remaining p² ambiguity must compare two whole potentially supersingular groups, with equal finite determinant characters and joint tame faithful degree m dividing p²-1 but m>p. The mixed formal/height-one-filtered case is excluded by the uniform rational-second-level-point valuation lemma. No existence or sharp least-index assertion for those pairs is made.\n''')
summary={'status':'PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],
         'complete_mathematical_assertions':4,'events':len(events),
         'gate':'1<=nu_min(p,p-1,2)<=2 for p>=5; only two whole formal groups with equal finite determinants and joint tame m>p remain at p².'}
summary_path.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
