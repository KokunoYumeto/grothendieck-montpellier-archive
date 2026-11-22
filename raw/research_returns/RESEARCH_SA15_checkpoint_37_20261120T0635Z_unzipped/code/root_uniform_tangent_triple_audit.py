"""Preserved exact reruns and complete root audits of the uniform triple bridge."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w = Path(__file__).resolve().parents[1]
jobs = [
    ('agents/obstructions_crystals/code/uniform_triple_local_type_checks.py',
     'agents/obstructions_crystals/code/uniform_triple_local_type_checks.output.json',
     'root_uniform_triple_local_type_checks'),
    ('agents/monodromy/code/verify_ss_tangent_incidence_rank.py',
     'agents/monodromy/outputs/verify_ss_tangent_incidence_rank.json',
     'root_verify_ss_tangent_incidence_rank'),
]
results = []
for program_rel, author_rel, name in jobs:
    program, author = w / program_rel, w / author_rel
    dest = w / 'outputs' / (name + '.json')
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
        (w / 'outputs' / (name + '.stdout.txt')).write_text(capture.getvalue())
    assert author.read_bytes() == before
    result = json.loads(dest.read_text())
    assert result['status'] == 'PASS'
    results.append({'program': program_rel, 'output': str(dest.relative_to(w)),
                    'elapsed_seconds': result['elapsed_seconds']})

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
 ('lem:DE-A4-uniform-triple-local-type', 'independent re-proof',
  'PASS: complete proof and exact program read. Root rederived the finite multiplication-by-three exclusions, the five independent rows, independent first gradients in r,s, nonzero contact-order-two coefficients, and transverse third derivative. Both local-type and globally smooth sharp-source conditions are nonempty opens in the same irreducible rank-five P3 bundle; the vertical slice lies in that bundle. This includes the cyclic order-three case.'),
 ('rem:DE-A4-uniform-triple-local-scope', 'computation or formal certificate',
  f"PASS: complete universal matrix certificate read and author-preserving rerun passed in {results[0]['elapsed_seconds']}s. Rank-five minor, both tangent conditions, gradient Jacobian, both contact coefficients, third derivative and cubic tangent quadratic verified; no all-kernel claim is inferred merely from these identities."),
 ('lem:ss-third-value-projection-candidate', 'independent re-proof',
  'PASS: entire projected-value proof read. Root rederived the base fibres (including eta=-2g and the cyclic eta=-g flex), absence of K-differences for the additional old base point, horizontal finite pair-rank locus using degree-two rho poles, all exceptional vertical cases, and generic three-value independence. The only possible three-edge pole cancellation is a complete order-three cycle; equal residues force three coefficients1, contradicted by the nonconstant sum of second-factor x coordinates.'),
 ('lem:ss-third-value-linear-tests-candidate', 'independent re-proof',
  'PASS: normalized value and derivative rows rederived. Independence modulo F,h proves h nonzero. A hypothetical derivative relation forces the rho fibre identity i+eta=-g; its remaining coefficients would make an affine line through three distinct second-factor points tangent at one of them. The extra v test at2g follows from equal X, eta=-i and ell(-i)=ell(i)+1.'),
 ('lem:ss-third-value-other-collisions-candidate', 'independent re-proof',
  'PASS: generic coefficient P1 gives a unique integral moving three-dimensional component. All rank-drop components are too small except specified constant pairs; cyclic curve strata lie over F=0. Exact nonzero Jacobians at P,-eta,Q give main-component etale points. The eta=2g nonflex and order-three noncyclic cases have constant total length3 and hence odd moving degree15. Generic rank-three and finite rank-one strata bound nonconstant triple incidence by dimension2. All constant-pair and rank-zero-triple cases checked.'),
 ('prop:ss-uniform-tangent-triple-candidate', 'independent re-proof',
  'PASS: full proof rederived, including all required openness transfers. A transverse third makes the marked triple reduced; a length2/3 tangent cluster with prescribed length>=2 cannot acquire a second tangency of length>=2. In the cyclic case outside-subgroup incidences avoid every prescribed base pair/triple, while the fully audited collinear witness supplies internal-collision avoidance in the same irreducible main rank-five incidence. Product automorphisms transport any nonzero three-torsion generator. Intersecting nonempty opens gives a globally smooth sharp source, exactly one transverse-third tangent triple and all other nodes, for every finite odd graph kernel.'),
 ('prop:ss-uniform-tangent-triple-candidate', 'computation or formal certificate',
  f"PASS: complete actual witness program read and author-preserving rerun passed in {results[1]['elapsed_seconds']}s. Both existing globally audited witnesses have rank-five contact-plus-third-value rows; third-branch determinants41 and49 are nonzero over GF64. This certifies membership in the main bundle, not global all-kernel existence by sampling."),
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, outcome in events:
        writer.writerow([sid, now, who, kind, outcome])
with (w / 'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
    f.write(f'''\n## {now}: uniform tangent triples, complete root audit\n\nThe full normalized-row local-type lemma and all four assertions of the uniform third-value/collision argument were read and independently rederived. The root audit checked every exceptional value fibre, the degree-two pencil pole cancellation, the order-three cycle, both etale-witness cases and both odd-degree15 cases, all dimension counts, and the finite-flat deformation argument at the marked points. The cyclic order-three case uses the previously completely checked global collinear witness, transported by product automorphisms, within the same rank-five incidence. This is a geometric all-kernel proof, not extrapolation from finite examples. The author-preserving certificate reruns passed in {results[0]['elapsed_seconds']}s and {results[1]['elapsed_seconds']}s. All earlier source/global-witness inputs are cited at their existing proved labels; no new external theorem is invoked without the previous exact checks. The prospective all-odd-degree full-group consequence remains a separate audit-pending theorem.\n''')
print(json.dumps({'status': 'PASS', 'actual_audit_time': now,
                  'events': len(events), 'reruns': results}, indent=2))
