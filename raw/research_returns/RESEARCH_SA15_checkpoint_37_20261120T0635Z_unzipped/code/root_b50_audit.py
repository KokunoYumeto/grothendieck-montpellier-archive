"""Retain the full root B50 audit and an author-preserving exact certificate run."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w = Path(__file__).resolve().parents[1]
program = w / 'agents/reduction_descent/code/verify_tame_norm_square_boundary.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_verify_tame_norm_square_boundary.json'
summary_path = w / 'outputs/root_b50_audit.json'
assert not dest.exists() and not summary_path.exists()
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
    (w / 'outputs/root_verify_tame_norm_square_boundary.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
assert out['status'] == 'PASS'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:B-RD50-boundary', 'independent re-proof',
     'PASS: complete statement and proof read and independently rederived, including the full earlier B34 logarithm/kernel argument. The invariant-differential identity forces coefficients of monomials with an exponent prime to p to be divisible by p. Product height-two special fibre forces every term below total degree p² to vanish modulo the uniformizer, in any integral coordinates. Thus [p](pi h) has coefficient valuations at least q=min(a+1,p+1,p²)>=a/(p-1) for a<=p²-1. Integration gives v(c_alpha)>=-a floor(log_p degree), and the geometric-series inequality proves every logarithm coefficient has valuation at least q at equality as well. Augmentation makes each coefficient a finite sum, so no analytic convergence at equality is assumed. Root freshly read original Bondarko Propositions9-12 and Lemma3 in full, pp674-676, and Proposition16 with its full proof p681. His ideal exponent is exactly ceiling(a/(p-1)), including equality. Integral Omega action preserves coefficient-valuation ideals; bounded projections, fz=p(z-z(0))Delta^-1 and pR contained in J give the one-F bound. The saturated image uses absence of finite flat kernel and applies to the actual target G. Theorem2(8), equation6 identifies the saturation quotient with the special kernel and f with relative Frobenius.'),
    ('prop:B-RD50-square', 'independent re-proof',
     'PASS: common finite determinant square root gives a simultaneous scalar BT twist, preserving the p² comparison and inequality of inertia traces. Cyclotomic determinant makes the faithful finite height-two special actions norm one, hence their common tame order divides p+1 and a=(p-1)m<=p²-1. Distinct norm-one two-dimensional traces have disjoint Teichmuller eigenvalue orbits, so their minimal polynomials have coprime reductions and an integral polynomial in the common inertia generator projects onto one entire factor. Actual alternating perfect Tate-lattice pairings extend with their inverses to the good BT models, as in the previously audited B33 argument; a unit adjustment matches the p² graph multiplier. Equal-rank flat closures make the graph self-orthogonal on the special fibre. The projector splits it into two formal subgroups; uniqueness of the one-dimensional subgroup of each p-power rank and self-orthogonality force each factor to be p-torsion, or ker(F²). The quotient special fibre is a product of height-two Frobenius twists. The map (q,pr_M) has zero finite flat kernel but special kernel 0 x N0[p]. The one-F target estimate contradicts its nonzero rank-p Frobenius image. No thickness condition is transported from the source to its quotient. If the original joint degree is p+1, norm characters are already trivial and this exclusion applies directly.'),
    ('cor:B-RD50-remaining', 'independent re-proof',
     'PASS: on procyclic tame inertia a mu_(p-1) character has a mu_(p-1) square root exactly when its generator value is square. A nonsquare determinant can be normalized to any primitive determinant by a simultaneous finite scalar twist, because their quotient is square. Write a height-two eigenvalue zeta^c in mu_(p²-1). Primitive norm gives gcd(c,p-1)=1; c is odd and gcd(c,p²-1) is an odd divisor of p+1. The lcm of two faithful orders has the same form (p²-1)/d with d an odd divisor of p+1. Consequently p5 leaves8,24 and p7 leaves48. This is a necessary character-class restriction only; no remaining pair is constructed and the least-index interval remains{1,2}.'),
    ('B50-EXACT-CERTIFICATE', 'computation or formal certificate',
     f"PASS: the complete author program was read and rerun with its author output preserved byte-for-byte, in {out['elapsed_seconds']} seconds. It checks {out['logarithm_cases']} logarithm inequalities, {out['crt_spectral_pairs']} finite-field CRT spectral pairs, and {out['primitive_norm_exponents']} primitive-norm exponents. The universal proof is the coefficient estimate and cyclic-group argument; these finite checks do not prove existence or nonexistence of a remaining formal-group pair.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_18.md').open('a') as f:
    f.write(f'''# Root source and search log after checkpoint 17\n\n## {now}: B50 closed logarithm boundary and square finite determinants\n\nRoot read the complete candidate B_tame_norm_square_boundary.tex and reread the entire earlier B_height_two_logarithm_gate.tex, including the coefficientwise logarithm, bounded-projection and saturation proofs. Root freshly opened the original Bondarko PDF at https://www.mathnet.ru/links/143cd4ef0c053a08f030f68ecac286cd/im691_eng.pdf, actually read Propositions9-12 with their written proofs and Lemma3, printed pp674-676, and the whole statement and proof of Proposition16, p681. The web views were turn498664735view0/view1 and turn985317369view0/view1. No new visual page inspection is claimed. The exact ideal in Proposition9 is m^(-floor(a/(1-p))), so equality gives the same ceiling exponent; the argument is coefficientwise in a formal augmentation variable. The previously audited Theorem2(8), equation6 supplies the covariant Frobenius identification, and the previously audited Tate1967 Theorem4/Corollaries1-2 supplies the actual integral duality maps used by B33.\n\nThe full program verify_tame_norm_square_boundary.py was read and independently rerun; its output is retained in outputs/root_verify_tame_norm_square_boundary.json and its stdout in the adjacent text file. Author output is unchanged. Runtime {out['elapsed_seconds']} seconds. The companion complete proof/source/code audit is agents/obstructions_crystals/B50_independent_audit.json. All three statements pass. The proposed m=2(p-1) refinement is separate and is not included in this verdict. No priority claim and no existence claim for a remaining pair is made.\n''')
summary = {
    'status': 'PASS', 'actual_utc': now,
    'elapsed_seconds': out['elapsed_seconds'],
    'complete_mathematical_assertions': 3, 'events': len(events),
    'source_scope': 'Original Bondarko full Propositions9-12/Lemma3 pp674-676; full Proposition16 p681; previous audited Theorem2(8) and Tate integral duality.',
    'gate': 'Every remaining p² ambiguity has nonsquare common finite determinant; after primitive-norm normalization, m=(p²-1)/d for d an odd divisor of p+1. No remaining-pair existence claim.'
}
summary_path.write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
