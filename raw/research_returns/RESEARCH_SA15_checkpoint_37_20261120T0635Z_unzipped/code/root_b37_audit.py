"""Preserved root execution and full-proof/source audit of corrected B37."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_scalar_residual_patterns.py'
author=program.with_suffix('.output.json')
destination=w/'outputs/root_verify_scalar_residual_patterns.json'
assert not destination.exists(), 'Preserve first root execution'
before=author.read_bytes()
write_text=Path.write_text
capture=io.StringIO()
def redirected_write(path,data,*args,**kwargs):
    if path.resolve()!=author.resolve():
        raise RuntimeError('Unexpected certificate output path')
    return write_text(destination,data,*args,**kwargs)
try:
    Path.write_text=redirected_write
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),
             {'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=write_text
    (w/'outputs/root_verify_scalar_residual_patterns.stdout.txt').write_text(capture.getvalue())
assert before==author.read_bytes()
out=json.loads(destination.read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
 ('lem:B-RD37-patterns','independent re-proof','PASS: full five-pattern valuation proof, potential supersingularity criterion and raw discriminant valuations -3,6,15,18,21 checked; correct tame columns2/4 follow from proved B36.'),
 ('lem:B-RD37-units','independent re-proof','PASS: residue of any cube root of a unit congruent1 is1 in characteristic3; expansion3w+3w^2+w^3 has each valuation at least3 at absolute ramification2.'),
 ('prop:B-RD37','independent re-proof','PASS: full corrected proof read; original Fisher introduction, Section2p4, Lemma4.2p8, Theorem4.3pp9-10 and complete theorem proof read; actual printed page9 viewed and numerator3 in equation11 confirmed. Direct opposite tame columns excluded; reverse B/A ratio and D/E root rotation and unit expansion checked algebraically. Simultaneous twist preserves9-congruence and multiplies both special trace functions equally. Residual normalizer C6 and tame cyclic images checked. Only non-scalar C3/C4 cases remain.'),
 ('prop:B-RD37','computation or formal certificate',f"PASS: author-preserving root rerun; {out['opposite_column_comparisons']} opposite-column comparisons; {out['subgroup_count']} SL2(F3) subgroups; reverse shift2; exact invariant and unit identities; runtime{out['elapsed_seconds']}s. Withdrawn missing-factor candidate remains retained."),
 ('rem:B-RD37-known-example','targeted proof check','PASS: q=2^5*3^6 has same nontrivial cube class as2 squared; if2 were a cube then-2 would be a cube, contradicting the cube-unit valuation bound sincev(-3)=2. The mixed Tate/elliptic prior example has non-scalar C3 residual image and is outside the two-potentially-supersingular assertion.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,outcome in events:
        writer.writerow([sid,now,who,kind,outcome])
log=w/'notes/ROOT_SEARCH_LOG_13.md'
with log.open('a') as f:
    f.write(f'''\n## {now}: corrected level-nine scalar residual comparison\n\nOriginal Fisher (2015), *On families of 9-congruent elliptic curves*, actual downloaded arXiv original: read introduction and Section1 pp1-2, full-level family definition Section2p4, Lemmas4.1-4.2p8, Theorem4.3 with equations(10)-(11)p9 and complete proofp10. Actual page9 PNG was visually inspected; equation(11) has numerator3. For Delta=1 the necessary reverse cube is ((t-theta^-1)(t_E-theta))/3. This differs from the withdrawn unpromoted candidate, whose missing-factor error remains documented. Root independently checked all valuation and unit arguments and the twist/normalizer conclusions. Exact author-preserving rerun took {out['elapsed_seconds']} seconds. This proves only the scalar exclusion; the C3/C4 residual level27 gate and least index remain unresolved.\n''')
print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],
                  'audit_events':len(events),'actual_audit_time':now},indent=2))
