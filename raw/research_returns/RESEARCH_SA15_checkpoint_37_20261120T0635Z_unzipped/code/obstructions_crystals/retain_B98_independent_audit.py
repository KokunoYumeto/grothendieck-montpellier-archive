"""Complete B98 actual-field/different audit with unchanged isolated rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_first_wild_cyclotomic_different_candidate.tex'
program = author / 'code/verify_first_wild_cyclotomic_different.py'
author_output = program.with_suffix('.output.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
expected = {
    source: '0b8f978f9cfa246cfc0f6b1f2fb99212912cd4b4cfd1df86b0f04d7a8a868dc1',
    program: '154100c1a72927764be6657cee78140b1ae7def7abd4938e1db5d1c8b0856c2e',
    author_output: '27f2a52e50e9359d0cabcc1d947bcb5e6d85cd87936a1d7f1886fff0f36d361c',
}
for path, digest in expected.items():
    assert sha(path) == digest, str(path)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 4
isolated = own / 'outputs/B98_independent_run'
isolated.mkdir(exist_ok=False)
copied = isolated / program.name
copied.write_bytes(program.read_bytes())
assert sha(copied) == expected[program]
run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                     capture_output=True, text=True)
(isolated / 'stdout.txt').write_text(run.stdout)
(isolated / 'stderr.txt').write_text(run.stderr)
preserved = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
             for p, h in expected.items()}
(isolated / 'author_hashes.json').write_text(json.dumps(preserved, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in preserved.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author_output.read_text())
mathematical = lambda d: {k: v for k, v in d.items()
                        if k not in ('actual_utc', 'runtime_seconds')}
assert result['status'] == 'PASS'
assert mathematical(result) == mathematical(original)
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'proof_read_scope': (
        'Entire final four-label B98 candidate and complete standalone checker read. '
        'Entire final six-label B97 point-field proof and its checker read as a dependency, '
        'without claiming a separate B97 numerical rerun. Complete B86 Cohen/cyclotomic proof, '
        'complete B76 determinant/dimension/mixed reduction, full B63 all-index existence theorem '
        'and exact-index corollary, and entire canonical B90 actual point/compositum/tame-exclusion '
        'proof freshly read. The full B96 selected-point proof was independently rederived '
        'and its literal checker rerun in this same session at05:14:15.230135. '
        'The earlier B79/B81/B82--B85 and B87/B88 dependencies retain their previously recorded audits.'),
    'checks': [
        'The final standing field hypotheses are complete mixed-characteristic DVR, algebraically closed residue, e=p(p-1), and mu_p contained. The B98 corollary explicitly supplies mu5 after unramified completion, rather than silently assuming it for every original B.4 base.',
        'For a Cohen ring Lambda in O_K with perfect residue, the powers1,pi,...,pi^(e-1) span O_K modulo p as a vector space over the same residue field. Iterated p-adic lifting supplies their Lambda-span, and valuations distinct modulo e give independence. Thus K/K0 is finite of degree e even for the infinite residue field. No locally compact or finite-residue assumption is used.',
        'Cyclotomic shifted polynomials are Eisenstein over Lambda. Hence K1=K0(mu_p) has degreep-1 and K/K1 degreep. The cyclic degree-p^2 extension C0=K0(mu_p^3) overK1 has a unique degree-p subfield. Since mu_p^2 is not inK, its intersection withK is exactlyK1, giving the actual degrees[C:K]=p^2 and[C:C0]=p. C/K is cyclic even though K/K1 need not be Galois.',
        'For the monogenic degree-p extension K/K1, a uniformizer polynomial derivative has leading term valuation e_K+p-1=p^2-1. Every other nonzero derivative term i*a_i*pi^(i-1) has residue i-1 modulo p, while the leading term has residue-1. Thus their valuations are pairwise distinct and the minimum cannot cancel; d(K/K1)<=p^2-1. The analogous Eisenstein derivative in C/C0 has every term valuation at leastp-1. Uniformizer monogenicity follows from the same total-ramification expansion, not from a finite-residue theorem.',
        'For C0/K1 the nonterminal cyclotomic exponents have uniformizer displacementp and the pth-power subgroup displacementp^2. The exact sum(p^2-p)*p+(p-1)*p^2 gives2p^2(p-1). Different transitivity in the two actual towers gives d(C/K)+p^2*d(K/K1)=d(C/C0)+p*d(C0/K1), with factors determined by actual ramification indices. Consequently d(C/K)>=p^2(p-1)^2+p-1.',
        'A totally ramified cyclic group of orderp^2 has two positive lower breaks, since the first leading ramification quotient has exponentp and a nontrivial pth power has larger break. If the upper breaks are delta1<delta2, its lower breaks are delta1 and p*delta2-(p-1)*delta1. Summing the lower groups gives d=(p-1)(delta1+p*delta2+p+1), proving delta1+p*delta2>=p(p^2-p-1). The rational endpoint delta2>=p^2-p-2+1/p retains all possibilities and requires no Hasse--Arf theorem.',
        'The full B97 degree proof uses actual Galois point translations. A hypothetical degree-p second-point field forces a degree-p^3 third-point field by valuation denominators; its full terminal translation plane contradicts scalar versus Frobenius leading maps. Thus every second point has degreeq and each next point degreeq over it. When r1=2 the primitive stabilizer is actually central and normal, giving a single-point Galois field of degreep^4. The two-level first-ordinary-coefficient argument then rules out r1=2 without assuming an abelian or Cartan image.',
        'The B97 one/two-break argument proves c1=N(p-1) and c2=(q^2-1)(p-1) for each actual point tower, with all coordinate changes below its mixed-characteristic cutoff. Two actual second-point fields generate F2, so their character conductors bound its last upper break exactly byc1. For a third-point stabilizer S_i and second-point stabilizer H_i, terminal evaluation is onto, so U*S_i=H_i. Therefore F2 intersection T_i=E_i and[F2T_i:F2]=q.',
        'In H_i/(U intersection S_i), first-layer matrices kill the chosen residual column; both their commutator and pth power also kill that column. Hence the actual compositum F2T_i/E_i is elementary abelian. The upper quotient/subgroup formulas bound the terminal quotient conductor by psi_(F2/E_i)(c2)<=p^(r1-2)c2. The two point-column maps have zero joint kernel, so their dual spaces span every terminal character, including determinant. This is a complete character-space bound, not a bound on just one selected cyclic direction.',
        'B97 excludes traceless first layers by the exact Cohen-field cyclotomic calculation of B86. It leaves r1 in{3,4} with nonzero trace and full terminal-character boundp^(r1-2)c2. The two-dimensional traceless Lie algebra in a hypothetical traceful(3,3) case has a characteristic nilpotent line, contradicting the irreducible tame normalizer; the final layer shapes are therefore exactly the stated ones.',
        'On the actual good field L the finite determinant is killed, so determinant is cyclotomic. Nonzero first-layer trace means mu_p^2 is not contained inL orK. Tame base change of degreeN scales the positive lower breaks byN by the actual uniformizer root argument, and hence scales the upper breaks byN. The actual first cyclotomic layer is a quotient of F2/L, forcing delta1<=p-1.',
        'The bound d2=N*delta2 gives d2>c1 and q*(d2-c1)-c2>=N*(p^4-3p^3+1)>0 for everyp>=5. This was independently expanded directly, with positivity p^4-3p^3+1=p^3(p-3)+1.',
        'The actual cyclic degree-p^2 field LC/L intersects the elementary F2/L in exactly their common first cyclotomic field, since an elementary quotient cannot contain the whole cyclic degree-p^2 extension. Hence F2C/F2 is a genuine nonzero terminal cyclic quotient insideF3/F2. Above c1 the compositum upper group lies in the subgroup overF2 and maps nontrivially to the last cyclic line until d2. Subgroup conversion therefore gives its exact conductor psi_(F2/L)(d2), including the common first layer.',
        'Since F2/L has degreep^r1 and no upper break afterc1, psi(d2)=psi(c1)+p^r1(d2-c1)>p^r1(d2-c1)>p^(r1-2)c2. This contradicts the complete actual terminal-character bound. No unrelated extension, unknown first cyclotomic conductor, finite-residue class field theory or upper-break integrality is substituted.',
        'For the full p5,e20 consequence, completed maximal unramified base change preserves e and the inertia comparison. Writing5=u*pi^20 and taking a fourth root ofu puts the unique tame degree-four Cohen-field extension K0(5^(1/4))=K0(mu5) insideK. Thus B76 dimension/determinant detection and mixed exclusion apply atn3, since3=v5(20)+2 and20<=25. The residual irreducible, residual-wild reducible and tame reducible cases are exhausted by B98, the fully audited B96 and the canonical B90 chain respectively.',
        'The B63 all-index arc theorem explicitly permits p-divisiblee. Atp5,n2,e20>5 it constructs an actual25-torsion comparison with different finite special characters, giving the strict lower bound. Since manuscript indexnu=n-1, recovery at125 and failure at25 give exactlynu_min(5,20,2)=2. This full least-index equality is asserted only at that triple; the all-prime theorem is only the irreducible-residual branch.',
        'The complete standalone program has nine symbolic rational identities, a stated finite derivative-profile supplement, all cyclotomic exponent counts at its nine primes, rational-break tests with denominators1,p,p^2, and actual terminal determinant/dual-column checks. The two dual-column maps span full M2* and sl2* for every enumerated ordered basis. These finite checks do not infer actual fields or formal-group realizations. The isolated rerun preserves every author byte and matches every mathematical JSON field.',
    ],
    'primary_source_scope': {
        'fresh_retained_original_reads': [
            'Colmez Corps locaux: opening definition and expansion lemma1.5; full Proposition3.7 proof, Lemma3.8, Corollary3.9, Theorem3.10, Definition3.11, Proposition3.13 and their full proofs, printed pp14-16.',
            'Colmez Corps locaux: Lemma3.15 trace-dual preliminaries, full Proposition3.17 transitivity proof, complete Proposition3.18 monogenic derivative proof including its continuation, and Corollary3.19 ramification-different proof, printed pp16-18.',
        ],
        'retained_original': str((author / 'sources/colmez_corps_locaux.txt').relative_to(root)),
        'retained_original_sha256': sha(author / 'sources/colmez_corps_locaux.txt'),
        'Cohen_scope': 'The complete actual B86 Cohen-field proof was reread. The original Stacks032A full coefficient-ring proof remains in the prior B86 audit/source chain; no fresh Stacks opening is claimed here.',
        'new_external_openings_for_B98': [],
        'precise_limits': 'No fresh Hopkins--Gross opening or B63 numerical rerun is claimed. Its complete all-index existence argument was reread, while its underlying exact universal arc and finite-extension-lifting proofs retain their earlier complete audits. No PDF/image inspection is claimed in this proof audit.',
    },
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'program_sha256': sha(copied),
    'independent_output_sha256': sha(copied.with_suffix('.output.json')),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'exact_counts': result['counts'],
    'scope': 'Complete four-assertion proof/source/code PASS. All-prime first-wild irreducible-residual recovery, and exact full height-two least indexnu_min(5,20,2)=2 using the separately audited exhaustive reductions. No corresponding exact full first-wild index at another prime is asserted.',
}
audit = own / 'B98_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_code_audit',
                           str(source.relative_to(root)),
                           'Actual cyclotomic different towers, entire terminal character bound and exhaustive p5 reductions; unchanged isolated checker',
                           'PASS', str(audit.relative_to(root))]) + '\n')
print(json.dumps({'status': 'FULL PASS', 'actual_utc': now,
                  'record': str(audit.relative_to(root)),
                  'candidate_sha256': expected[source], 'labels': labels,
                  'independent_runtime_seconds': result['runtime_seconds'],
                  'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
                  'counts': result['counts']}))
