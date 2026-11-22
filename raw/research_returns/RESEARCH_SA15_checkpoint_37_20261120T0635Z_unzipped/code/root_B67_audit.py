"""Complete arbitrary-index B67 proof audit and author-preserving exact rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess, sys

w = Path(__file__).resolve().parents[1]
candidate = w / 'agents/reduction_descent/B_tame_irreducible_arbitrary_index_candidate.tex'
source = w / 'agents/reduction_descent/code/verify_irreducible_arbitrary_index.py'
author = source.with_suffix('.output.json')
before = author.read_bytes()
dest = w / 'outputs/root_B67_audit.json'
snap = w / 'code/audit_snapshots/B67_root_independent_certificate.py'
assert not dest.exists() and not snap.exists()
snap.write_bytes(source.read_bytes())
run = subprocess.run([sys.executable, str(snap)], capture_output=True, text=True)
(w / 'outputs/root_B67_independent_certificate.stdout.txt').write_text(run.stdout)
(w / 'outputs/root_B67_independent_certificate.stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
data = json.loads(snap.with_suffix('.output.json').read_text())
old = json.loads(before)
omit = {'actual_utc', 'runtime_seconds'}
assert {k: v for k, v in data.items() if k not in omit} == {k: v for k, v in old.items() if k not in omit}
assert author.read_bytes() == before
(w / 'outputs/root_B67_independent_certificate.json').write_text(json.dumps(data, indent=2) + '\n')
checks = {
    'lem:B-RD67-normalization': (
        'Fresh full B49 tame-inertia proof read, with its already audited actual-lattice descent dependency '
        'retained. The common tame degree N=p^2-1 field gives both formal models and residual division '
        'fields without a faithfulness assumption. An irreducible residual module has no nontrivial '
        'normal p-action. Its inertia-stable valuation filtration is one-step, giving first-level '
        'valuation e and primitive second-level valuation e/q in L. The inverse Newton segment has '
        'all intermediate terms strictly above it. The common p^2 division extension has elementary '
        'abelian W in M2(Fp), and integrality with p-prime e forces r>=2. Recomputed A=e*p^(r-2), '
        'eF=N*q*A and eta^A=zeta^e. The finite tame complement splits by the explicit correction of '
        'a lift; averaging gives an exact eigen-uniformizer. Tate full faithfulness applies to the '
        'actual semilinear descent map and its inverse. The integral Honda conjugator has residue m '
        'and is a unit. Primitive leading classes are a scalar Fq-plane because the irreducible tame '
        'multiplier is nonscalar; the normalized multiplication-by-p map is z->z^q=z. Therefore '
        'different special character pairs force a Frobenius-semilinear residual intertwiner, with '
        'the same orientation on the first-level submodule.'
    ),
    'lem:B-RD67-small-wild': (
        'The coefficient ring is chosen in O_K, so every coefficient representative is fixed by W. '
        'Since eF>qA, discarded mixed-characteristic terms have valuation above the entire calculation. '
        'A degree j of exact p-valuation s changes first at j+p^s*b with coefficient '
        '(j/p^s)*d_g^(p^s). For r2, all primitive changes occur at A+b=qA and identify the full '
        'Cartan coefficient plane as scalar multiples of the common d-map, contradicting the '
        'required Frobenius orientation. For r3, A=pe and b0=Ne. A low break forces the first '
        'ordinary term j=A+(p-1)b with coefficient linear in z; a high break forces j=qA-b. '
        'The full anti-plane single-break case is excluded below b0 by the degree-(p-1) cardinality '
        'bound and above b0 by Frobenius versus scalar proportionality. In the two anti-break case, '
        'the first low ordinary term is uniquely earlier at the later break and would be Cartan '
        'rather than anti-Cartan; if the first break is high, all later changes miss qA. For '
        'Cartan2 plus anti1, the explicit comparison includes Cartan c=b0 and excludes every case '
        'except b<b0 and c=p*b0-(p-1)b>b0. This forces all nonzero Cartan elements to share one '
        'break and gives the same full-plane Frobenius contradiction. Every tame-stable '
        'three-dimensional matrix subspace has been exhausted.'
    ),
    'lem:B-RD67-final-plane': (
        'For full W, the primitive point stabilizer has dimension2, hence its actual point field is '
        'a Galois q-extension with coordinate valuation e prime to p and displacement valuation qe. '
        'Its single lower and upper break is therefore Ne. The cyclotomic degree-p quotient has '
        'coordinate valuation eN/(p-1), prime to p, and the same break. Upper-numbering quotient '
        'compatibility makes W^(Ne) surject under every point evaluation and under trace, while '
        'all later groups vanish. At its last lower break c the leading ramification map is '
        'injective and has scalar tame weight eta^c. Averaging a vector with nonzero trace gives '
        'a nonzero tame-fixed vector, forcing eta^c=1 and then the whole last group to be tame '
        'fixed. The tame centralizer is the Cartan plane; evaluation surjectivity forces equality. '
        'The preceding proper-filtration interval makes the Herbrand value Ne strictly smaller '
        'than c. No lower/upper interchange is made before these quotient calculations.'
    ),
    'lem:B-RD67-full-wild': (
        'Recomputed the three first-change slopes q,p,1 for A=qe. At the final Cartan break c, '
        'the q-divisible terms are too late and no nonzero polynomial of degree at most p can '
        'cancel on its q-element leading plane; hence the displayed minimum is exactly qA. '
        'For one anti-Cartan break, its arbitrary root polynomial is X^q+s_D X^p+t_D X, '
        'with t_D nonzero. The middle term cannot be dropped. A high anti-break contradicts '
        'the later Cartan minimum. A low one forces K0=A+N*b and J>=A+(q-p)*b, with '
        'the ordinary coefficient a fixed nonzero multiple of z. At c that term is uniquely '
        'first. For two anti-breaks b1<b2<c, the minimum at b2 is below qA; involving the '
        'slope-q term would make it uniquely too small at b1. Thus p/ordinary cancellation '
        'occurs at b2 and q/p cancellation at b1, yielding both exact degree identities. '
        'Fixed elements of those breaks make both coefficient functions fixed multiples of z '
        'for every nonzero primitive class. The final Cartan displacement is again proportional '
        'to the common d_g over a full q-plane, incompatible with the different-character '
        'Frobenius intertwiner.'
    ),
    'thm:B-RD67': (
        'The completed maximal unramified extension preserves e, the actual finite torsion '
        'comparison and the relevant inertia action. The three wild dimensions2,3,4 exhaust '
        'all possibilities. Their exclusion proves equality of the actual finite special '
        'characters for irreducible residual inertia and any p-prime e, p>=5. This is not '
        'a change of lattice, CM assumption, or rescaling of a minimal-index result.'
    ),
    'rem:B-RD67-scope': (
        'The entire finite supplement was read and independently rerun from a preserved copy. '
        'All mathematical outputs agree with the author and its output is unchanged. The '
        '150 indices,221 arbitrary additive planes and conditional arithmetic patterns '
        'supplement the universal proof; they do not construct BT groups or prove existence '
        'by sampling. Reducible residual inertia, p-divisible e and higher heights remain '
        'outside this theorem.'
    ),
}
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for label, detail in checks.items():
        writer.writerow([label, now, 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'targeted proof check', 'PASS. ' + detail])
record = {
    'status': 'FULL ARBITRARY-INDEX PROOF, PRIMARY-SOURCE AND EXACT-CERTIFICATE PASS',
    'actual_utc': now,
    'candidate': str(candidate.relative_to(w)),
    'candidate_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest(),
    'independent_runtime_seconds': data['runtime_seconds'],
    'counts': data['counts'],
    'author_output_sha256': hashlib.sha256(before).hexdigest(),
    'author_output_unchanged': True,
    'all_mathematical_output_equals_author_output': True,
    'checks': checks,
    'fresh_primary_reads': [
        {'source': 'Stacks Project, Theorem10.160.8 (032A)',
         'url': 'https://stacks.math.columbia.edu/tag/032A', 'ref': 'turn268057077view0',
         'scope': 'Full coefficient-ring theorem and proof, including the mixed-characteristic construction.'},
        {'source': 'Tate1967, p-divisible groups',
         'url': 'https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf',
         'ref': 'turn138414309view0',
         'scope': 'Original printed181-182, Theorem4, its Corollaries1-2, complete proof and complete Proposition12 proof. Indexed original text read; no page-image claim.'},
        {'source': 'Serre1961, Sur les corps locaux a corps de restes algebriquement clos',
         'path': 'agents/reduction_descent/sources/serre1961_algebraically_closed.txt',
         'scope': 'Original printed127-128, Herbrand functions and Section3.1 Proposition3. The original refers out for its proof.'},
        {'source': 'Colmez, Corps locaux',
         'path': 'agents/reduction_descent/sources/colmez_corps_locaux.txt',
         'scope': 'Author notes printed14-16, complete norm-polynomial proof Proposition3.7, Lemma3.8, Corollary3.9, full Theorem3.10 and Proposition3.13 proofs.'},
    ],
}
dest.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
