"""Full B93 independent proof/source audit and literal isolated certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_residual_wild_last_crossing_candidate.tex'
program = author / 'code/verify_residual_wild_last_crossing.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '50a83a2885ff0a8fb79dfce8abdca45e142b4d1fb2224993830e8086f57bea04',
    program: '56c7cab1f24540ff693aa8c526efbdff25a6768683806e4fd283293277217753',
    author_output: '860e792a4c8f05621df62a16de3b892d61964032cf1ff719b01dc773bcfbebb3',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 5
isolated = own / 'outputs/B93_independent_run'
isolated.mkdir(exist_ok=False)
copied = isolated / program.name
copied.write_bytes(program.read_bytes())
assert sha(copied) == expected[program]
run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                     capture_output=True, text=True)
(isolated/'stdout.txt').write_text(run.stdout)
(isolated/'stderr.txt').write_text(run.stderr)
preserved = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
             for p, h in expected.items()}
(isolated/'author_hashes.json').write_text(json.dumps(preserved, indent=2)+'\n')
assert all(v['before'] == v['after'] for v in preserved.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author_output.read_text())
mathematical = lambda d: {k:v for k,v in d.items() if k not in ('actual_utc','runtime_seconds')}
assert result['status'] == 'PASS'
assert mathematical(result) == mathematical(original)
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)), 'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': 'Entire final five-label candidate and entire standalone checker read. Full canonical B86, B87, B88, B90, B91 and B92 proofs reread, and the complete B60 fixed-representative lower-break proof plus its Newton setup read. All newly used field/stabilizer/conductor steps independently rederived below; no finite enumeration substitutes for them.',
    'checks': [
        'Cohen structure embeds a complete unramified coefficient DVR with the same perfect residue field. K/K0(mu5) is totally ramified of degree5. For a uniformizer its Eisenstein derivative has leading valuation24, while all other nonzero terms occupy the other four residues modulo5, so the different exponent is at most24.',
        'The normal closure is a transitive subgroup of S5 with nontrivial normal wild group C5 and faithful tame complement C_m, m dividing4. Its unique positive break gives 5m-1+4b=(m-1)+m*d, and upper b/m=(d-4)/4<=5. This does not invoke solvability of an arbitrary quintic: the local inertia structure forces the normal C5.',
        'The cyclotomic degree25 extension over K0(mu5) has lower4,24 and upper4,8. Its intersection with the normal closure is trivial: for m>1 the faithful semidirect product has no C5 quotient, while m=1 would force the excluded K=K0(mu25). Since8 exceeds the other last upper break, the terminal cyclotomic group survives and subgroup conversion gives m(44-d). Tame descent gives conductor44-d>=20 over K and >=480 over L.',
        'In the actual full parahoric group, reduction mod25 has degree625 and its subgroup over R is additive upper triangular with coordinates a0,d0,b1. B92 gives the actual low point field over R lower24,9234 and hence character conductors24,1866. The independent a0 field has conductor96 over R, giving F2/R lower24,384,44634.',
        'The exact quotient norm average in each nontrivial residual coset is strictly increasing in its maximum M and uniquely forces M=234. The maximum/minimum rule is valid also at equal subgroup breaks by maximality. Thus F2/L has counts500,100,20,4 at lower24,234,384,44634 and upper24,66,72,426.',
        'The terminal lower-entry character c is independent of the entire original mod25 image and has conductor6. Thus E=F2*C is the actual direct compositum, with upper6,24,66,72,426 and lower6,96,1146,1896,223146. Restricting its actual subgroup to u=a0=0 gives E/S lower6,96,223146; restricting to u=b1=d0=0 gives E/E_low lower6,1896. Their upper conversions match the displayed values.',
        'The two actual mod25 kernels intersect in U=1+25 upper-triangular matrices, of dimension3. All field identifications use this original125 representation and the actual high-quotient lattice, not unrelated abstract extensions.',
        'A tame eigenprojector selects the first-model high inverse of e1 inside its stable size5 inverse coset. Its actual25 valuations are19 and3; the following inverse polygons are single segments and give19/25 and3/25. The first-column stabilizer a=c=0 yields degree125, and adjoining R yields degree625. Over S=RA the quotient is genuinely elementary abelian25 with additive coordinates a1,c, because u=a0=0 kills all cross terms.',
        'The high translation line c=0 in that degree25 extension has displacement46875 in the second coordinate of valuation75, so its lower break is <=46800. The quotient c has conductor6. Considering whether the last ramification line equals this high line bounds a1 by46824/5 in all one- and two-break cases. Restriction to E uses an upper bound and does not assume disjointness; the actual intersection is SC. Herbrand gives275496.',
        'For the second column the level125 stabilizer b=d=0 is normal inside the actual level25 point stabilizer b=0 mod25,d=0 mod5. The quotient is elementary abelian25 with coordinates b2,d1 and total point-field degree3125. Its first-model coordinate has value5, and every d1-nonzero translation has displacement3125. The unconditional lower-break inequality and exact quotient average bound d1 by3120; restriction through E/E_low gives70296. The actual intersection of the low125 point field with E is precisely the low25 point field.',
        'The actual mod25 determinant is a0+d0, of conductor72 since its summands have distinct conductors72 and24. Therefore mu25 is not in K. The last cyclotomic conductor is >=480, strictly beyond E/L last426, so its restricted terminal character has exact Herbrand conductor >=391896. On U the same determinant is1+25(a1+d1), whose conductor is at most275496. The strict gap116400 excludes the last crossing.',
        'The consequence is confined to the original residual-wild crossing(5,45). The both-large layer shapes(3,4)/(4,4), irreducible residual sector and unrestricted least-index interval remain untouched. No625-torsion comparison or local-class-field theorem is silently imported.'
    ],
    'primary_sources': [
        {'title': 'Stacks Project, Theorem10.160.8, Tag032A',
         'url': 'https://stacks.math.columbia.edu/tag/032A',
         'web_ref': 'turn868607854view0',
         'actual_read_scope': 'Freshly opened and read the full theorem and complete coefficient-ring existence proof, including the mixed-characteristic inverse-limit construction.'},
        {'title': 'Pierre Colmez, Corps locaux, notes du cours de M2',
         'url': 'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf',
         'web_ref': 'turn868607854view1',
         'retained_text': 'agents/reduction_descent/sources/colmez_corps_locaux.txt',
         'retained_text_sha256': sha(author/'sources/colmez_corps_locaux.txt'),
         'actual_read_scope': 'Original PDF freshly opened and introductory complete-discrete-field scope read. From retained original text, complete Proposition2.12 p11, Proposition3.7, Lemma3.8, Corollary3.9, Theorem3.10 and Proposition3.13 pp14-16, Propositions3.17/3.18 and Corollary3.19 pp17-18, and Lemma3.20 through the conductor definition/Lemma3.25 pp18-20 read. Both different identities and full subgroup/quotient proofs were checked. No finite-residue hypothesis or image-view claim.'}
    ],
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied),
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'exact_certificate_summary': {
        'normal_closure_rows':len(result['normal_closure_arithmetic_rows']),
        'matrix_rows':result['matrix_rows'],
        'terminal_determinant_rows':result['terminal_determinant_rows'],
        'terminal_a_bound':result['terminal_a_bound'],
        'terminal_d_bound':result['terminal_d_bound'],
        'cyclotomic_terminal_lower_bound':result['cyclotomic_terminal_lower_bound'],
        'strict_gap':result['strict_gap']
    },
    'scope':'Complete five-assertion proof/source/code audit. Only the last original residual-wild crossing is excluded; no full first-wild recovery or existence claim.'
}
audit = own/'B93_independent_audit.json'
with audit.open('x') as f:
    json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'independent_full_proof_source_code_audit',str(source.relative_to(root)),
            'Entire actual field/conductor proof and invoked dependencies; complete original passages; literal unchanged isolated certificate',
            'PASS',str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':'FULL PASS','actual_utc':now,'record':str(audit.relative_to(root)),
                  'candidate_sha256':expected[source],'independent_runtime_seconds':result['runtime_seconds'],
                  'mathematical_output_identical':True,'author_unchanged':True,'labels':labels}))
