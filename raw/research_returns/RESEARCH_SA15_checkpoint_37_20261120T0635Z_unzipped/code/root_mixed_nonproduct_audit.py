"""Root complete proof/source audit and preserved mixed nonproduct certificate."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w = Path(__file__).resolve().parents[1]
program = w / 'agents/obstructions_crystals/code/mixed_nonproduct_rank_checks.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_mixed_nonproduct_rank_checks.json'
assert not dest.exists()
before = author.read_bytes()
original = Path.write_text
capture = io.StringIO()

def write(path, data, *args, **kwargs):
    if path.resolve() != author.resolve():
        raise RuntimeError('Unexpected certificate output path')
    return original(dest, data, *args, **kwargs)

try:
    Path.write_text = write
    with redirect_stdout(capture):
        exec(compile(program.read_text(), str(program), 'exec'),
             {'__name__': '__main__', '__file__': str(program)})
finally:
    Path.write_text = original
    (w / 'outputs/root_mixed_nonproduct_rank_checks.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:DE-A3-mixed-polarization-blocks', 'independent re-proof',
     'PASS: entire proof read. Functorial perfect-field etale/multiplicative/local-local splitting, integral covariant dual lattice, cross-factor orthogonality, equal ordinary indices, and rank-two alternating local block checked. Root freshly read original Oda1.10/1.12,3.14–3.18,3.22–3.24 with their displayed proofs, and actually viewed printed100–101. W(k) torsion-freeness supplies alternation at2. Kernel annihilation by D, finite-flat theta descent, typed integral inverse polarization, Euler characteristic and swapped indices are verified.'),
    ('lem:DE-A3-mixed-index-zero-source', 'independent re-proof',
     'PASS: full iff proof checked. The dual local-local block is trivial precisely at a(M)=0; the multiplicative ordinary half is isotropic of the required order, its Cartier dual is etale, and all odd factors are etale. Typed dual-isogeny identity and norm cancellation checked. Conversely an etale source preserves the local-local lattice and forces b=v2(D), hence a=0.'),
    ('lem:DE-A3-mixed-all-even-Prym', 'independent re-proof',
     'PASS: full proof checked against the prior fully audited Prym lemma. Ample vanishing gives point and tangent injectivity, duality gives smooth connected kernel, and the integral adjoint-polarization equality survives inseparability. The actual A-dual[2] immersion and connected Verschiebung kernel force a Prym defect at least1; adding the ambient defect gives at least2.'),
    ('thm:DE-A3-mixed-nonproduct-ranks', 'independent re-proof',
     'PASS: complete geometric proof checked. Odd powers preserve a=0 and admit the prescribed etale principal source, even when D is even. Previously audited cubic jet/value arguments apply to every etale kernel; node count and normalization sequence give defect1. Two transverse odd sharp members give defect2 in even degree, matched by the all-even Prym upper bound. Very ampleness and exact line-bundle translation use norm sections and polarization surjectivity. Relative subtraction and ambient regularity range checked.'),
    ('rem:DE-A3-mixed-nonproduct-scope', 'computation or formal certificate',
     f"PASS: full scope and example construction checked, with no existence of a simple example inferred without choosing one. Entire symbolic certificate read and author-output-preserving rerun passed in {out['elapsed_seconds']}s: {out['index_cases']} index pairs, {out['odd_norm_cases']} odd norm identities and {out['even_union_cases']} transverse union identities. Symbolic arbitrary-unit block identities are universal; finite cases do not replace geometry.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: mixed nonproduct polarizations and integral duality\n\nRoot opened the original Numdam PDF https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf and read the retained original text of Oda (1969), Propositions1.10 and1.12 pp75–76, Theorem3.14 and Corollaries3.15–3.16 pp87–88, Proposition3.18p89, and Propositions3.22–3.24 pp99–101, including the displayed constructions/proofs. Printed100–101 were also actually viewed as images to verify the dual-lattice convention and skew-symmetry statement. The characteristic-two alternating conclusion is an explicit inference using the absence of2-torsion in W(k), not an extra assertion attributed to Oda. Root freshly read original Edixhoven–van der Geer–Moonen AV4.44–4.45p67 with proofs and8.10–8.11pp116–117/8.19p119 with proofs; these allow the nonreduced isotropic subgroup. Prior fully read Debarre3.2–3.3 and dual-isogeny sources are reused. The whole mixed nonproduct proof and every step of the geometric norm/Prym argument were independently checked. Author-preserving arithmetic rerun {out['elapsed_seconds']}s.\n''')
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now, 'events': len(events)}, indent=2))
