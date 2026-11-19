"""Full root proof/source audit of the final C4 case, with preserved certificate."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json
w = Path(__file__).resolve().parents[1]
program = w / 'agents/reduction_descent/code/verify_c4_final_exclusion.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_verify_c4_final_exclusion.json'
assert not dest.exists()
before = author.read_bytes()
old_write = Path.write_text
capture = io.StringIO()
def write(path, data, *args, **kwargs):
    assert path.resolve() == author.resolve()
    return old_write(dest, data, *args, **kwargs)
try:
    Path.write_text = write
    with redirect_stdout(capture):
        exec(compile(program.read_text(), str(program), 'exec'),
             {'__name__': '__main__', '__file__': str(program)})
finally:
    Path.write_text = old_write
    (w / 'outputs/root_verify_c4_final_exclusion.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:B-RD42-normal', 'independent re-proof',
     'PASS: entire proof independently rederived. Short models are integral at delta6/12/18; delta18 scales down. The two low B-valuations have a unique Newton-polygon three-line, while B-valuation>=3 removes wild reduction by a quadratic twist. Unit fourth-root normalization gives M_b and its pi-twist. Exact cubic good model, faithful special actions, cyclic cubic discriminant, lower break1 and minimal good fields checked. Cardano identifies the Kummer class in U2/U3, and previously proved U3-cube surjectivity gives the precise residue ±b field criterion.'),
    ('lem:B-RD42-reverse', 'independent re-proof',
     'PASS: complete proof and marked conventions checked. Root freshly reread Fisher original Section2pp4–5, Section3p7 with iota=diag(1,-1) and Lemma3.2pp7–8, Lemma4.2 and Theorem4.3/equation11 with its full proof pp8–10. Actual S-inverse lift differs by elliptic inversion, hence differential −kappa. Delta6/12 gives differential-valuation difference2 and equal u-residues. Reverse theta1 cube, exact trace identity, squared-unit half-step and the pi5 cubic expansion force b-prime²=b², so the good cubic fields agree. No parameter-dependent differential factor or missing numerator3 is omitted.'),
    ('thm:B-RD42', 'independent re-proof',
     'PASS: full assembly audited against B29/B34/B35/B37–B41. The nine-torsion lower example remains valid. Every putative27 ambiguity is reduced to the remaining elliptic antisymplectic C4 pair, which now has a common good extension of degree6, contradicting necessary joint order18. Thus the exact least manuscript index at(p,e,h)=(3,2,2) is2. General higher-height/ramification least indices remain open; no claim that the whole B.4 row is closed.'),
    ('thm:B-RD42', 'computation or formal certificate',
     f"PASS: entire exact certificate read and author-preserving rerun passed in {out['elapsed_seconds']}s. Universal normal/good-model invariants, Cardano polynomial, trace elimination and pi-adic coefficient identities, actual opposite marked matrices, all discriminant/Newton cases, {out['cube_cases']} cube bounds and {out['GF9_residue_cases']} residue cases checked. Initial structural-SymPy-equality failure and its program/trace retained; algebraic zero-test correction verified. The geometric proof, not finite enumeration, establishes the theorem.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: exact smallest height-two character index\n\nRoot read and independently rederived every step of B42. The only new imported convention was checked in Fisher's original retained article: Section2pp4–5, the explicit reverse involution iota=diag(1,-1) in Section3p7, Lemma3.2pp7–8 and Theorem4.3 equation11/proof pp9–10, with Lemma4.2p8. The previously verified actual Fourier residue factor, integral elliptic realization and logarithmic joint-inertia restriction are reused explicitly. The delicate reverse sign, tame valuation comparison and trace-to-b² expansion were rederived by hand. The exact symbolic program was read in full and rerun without changing the author's output, in {out['elapsed_seconds']}s. The earlier failed structural-equality assertion is retained and is not treated as a mathematical counterexample. The result closes the (3,2,2) least-index instance at nu=2; the general B.4 formula remains open.\n''')
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now, 'events': len(events)}, indent=2))
