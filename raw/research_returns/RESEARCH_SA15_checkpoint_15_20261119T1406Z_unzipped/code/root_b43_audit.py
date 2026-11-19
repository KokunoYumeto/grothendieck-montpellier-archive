"""Root full dyadic level-eight counterexample audit and preserved exact run."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json
w = Path(__file__).resolve().parents[1]
program = w / 'agents/reduction_descent/code/verify_p2_character_level3.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_verify_p2_character_level3.json'
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
    (w / 'outputs/root_verify_p2_character_level3.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('prop:B-RD43', 'independent re-proof',
     'PASS: complete proof/code and dependencies read. Root rederived the N8 scaling and exact Miller doubling divisor, then checked the normalized boundary ratio and actual finite-etale extension killed by8 via the B29 quotient–Tate lemma. All field, integral discriminant, positive Tate-parameter, potential supersingular and finite-inertia hypotheses are verified. Raw valuation8e forces an order3 image whenever3 does not divide e; the rational isogeny preserves trace−1, while the Tate graded trace is2. The statement explicitly concerns order in the finite special-inertia quotient, not a finite-order absolute-inertia lift. This proves the lower bound3 only;16-torsion sufficiency is unclaimed.'),
    ('prop:B-RD43', 'used and rechecked in this run',
     'PASS: root freshly opened the original Antieau–Auel author PDF and read AppendixA.1 LemmasA.1–A.2 with full proofp22, the N8 family and Figure8pp26–27. The normalized constant cancels in delta(3P)/delta(2P), and the independent explicit Miller computation supplies the class−4lambda/3. The previous full Tate finite-order source and Serre–Tate/B22 special-reduction proof reads are reused explicitly, not claimed as new retrievals.'),
    ('prop:B-RD43', 'computation or formal certificate',
     f"PASS: entire exact program read and author-output-preserving rerun passed in {out['elapsed_seconds']}s. The eight points, all64 additions, nonsingular invariant polynomials/valuations, tangent normalization, affine Miller identity/evaluations and Figure8 eighth-power comparison all checked over Q(lambda),lambda²=−3. Full output retained separately.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
    f.write(f'''\n## {now}: dyadic eight-torsion character ambiguity\n\nRoot opened https://math.dartmouth.edu/~auel/papers/docs/AA_g1c.pdf and read the original July21,2021 author version, AppendixA.1 LemmasA.1–A.2 with proofp22 and the N8 family/Figure8pp26–27. The exact curve and Miller function are independently verified here; no numerical specialization is accepted merely from the table. The quotient–Tate finite-group extension was rechecked in full against B29. Root independently derived the repeated-doubling divisor8[P]−8[O], the class ratio and the raw-discriminant persistence argument. Author-preserving exact rerun {out['elapsed_seconds']}s. The resulting bound nu_min(2,1,h)>=3, and the same for3 not dividing e, strictly removes8-torsion sufficiency from the remaining small dyadic gate. No sufficiency at16 is claimed.\n''')
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now, 'events': len(events)}, indent=2))
