"""Record the full root proof/source/code audit of primitive type (1,3)."""
from pathlib import Path
import csv, datetime, hashlib, json, shutil, subprocess, sys, time
w = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
candidate = w / 'agents/obstructions_crystals/post_CP35_primitive_type_1_3_candidate.tex'
source = w / 'agents/obstructions_crystals/code/verify_primitive_type_1_3.py'
author = source.with_suffix('.output.json')
expected = '6c928494de0ea71b09838a8fb140823a21fdcf6e0526911047d10f023b48376d'
assert sha(candidate) == expected
assert sha(source) == '656d2dd179b064bdcc05361a2e6f936ddf4284e118f2a6b2be521c06af1b2c5b'
assert sha(author) == 'afad81f4708c2d7d9b6d62f98628d3d398fcc619f38f9b7ca0f0db4703b5d9d1'
before = {str(p.relative_to(w)): sha(p) for p in [candidate, source, author]}
folder = w / 'code/audit_snapshots/primitive_type_1_3_root_independent'
assert not folder.exists()
folder.mkdir(parents=True)
copy = folder / source.name
shutil.copy2(source, copy)
snapshot = w / 'notes/root_primitive_type_1_3_audited_candidate.tex'
out = w / 'outputs/root_primitive_type_1_3_audit.json'
assert not snapshot.exists() and not out.exists()
shutil.copy2(candidate, snapshot)
started = time.perf_counter()
run = subprocess.run([sys.executable, str(copy)], cwd=w, capture_output=True, text=True)
wall = time.perf_counter() - started
(w / 'outputs/root_primitive_type_1_3_independent.stdout.json').write_text(run.stdout)
(w / 'outputs/root_primitive_type_1_3_independent.stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
independent = copy.with_suffix('.output.json')
a = json.loads(author.read_text())
b = json.loads(independent.read_text())
mathpart = lambda x: {k:v for k,v in x.items() if k not in ('actual_utc', 'runtime_seconds')}
assert a['status'] == b['status'] == 'PASS' and mathpart(a) == mathpart(b)
assert before == {str(p.relative_to(w)): sha(p) for p in [candidate, source, author]}
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
labels = ['lem:DE-odd-line-Frobenius-stable', 'lem:DE-three-section-divisor-degree',
 'lem:DE-primitive-one-three-Cartier', 'lem:DE-primitive-one-three-smooth-member',
 'lem:DE-primitive-one-three-Euler', 'thm:DE-primitive-one-three-full-image',
 'rem:DE-primitive-one-three-scope']
r = {
 'status': 'FULL-INDEPENDENT-PROOF-SOURCE-CODE-PASS', 'actual_utc': now,
 'reviewer': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate': str(candidate.relative_to(w)), 'candidate_sha256': expected, 'labels': labels,
 'read_scope': 'Entire seven-label written proof read, with complete final theta-divisor dichotomy and certificate paragraph separately checked against retained prior/diff. Entire exact checker read. Full OW12/OW13 hypersurface model and dense-open transfer reread. The stability and explicit Lang-slice arguments were independently derived by root before this candidate was written, then checked against every final hypothesis.',
 'proof_checks': [
  'The relative Frobenius diagonal filtration in characteristic2 and dimension2 has graded L, L tensor Omega1, L tensor wedge2Omega1. Triviality of Omega1 refines it to four O quotients after twisting by L inverse. Thus the pullback is semistable for every polarization, which implies semistability of F_*L.',
  'For a saturated equal-slope subsheaf Q of rank1,2 or3, flat Frobenius preserves torsion-freeness of the quotient. Intersecting S=F^*Q tensor L^-1 with the O filtration gives rank-one ideal sheaves I_Z(-D). Their nonpositive degrees sum to0, so every D vanishes, detS is trivial and chiS<=0. The same argument for T^* inside U^* gives chiT^*<=0; reflexive hull and surface Riemann-Roch give chiT<=0. Additivity with chiU=0 forces chiS=0. Riemann-Roch then gives4chiQ=qchiL, incompatible with odd chiL and1<=q<=3. No curve stability theorem is applied to the surface.',
  'Every effective divisor on an abelian surface is nef by translation. Positive square gives ampleness, then D^2=2h0D and Hodge index gives D.H>=6. In square0, all components have square0 and pairwise intersection0; adjunction and absence of rational curves identify smooth elliptic translates in one subgroup direction. D descends from an elliptic quotient, with degree h0D>=3. Global generation forces H.E>=2, again giving D.H>=6.',
  'Finite-flat duality gives a perfect L^(2)-valued Cartier product pairing on F_*L. Nonordinary top Cartier trace vanishes, so its diagonal vanishes locally and it is alternating. The odd theta group acts equivariantly. On the three-dimensional clock/shift basis, both wedge2W and W^(2) are irreducible of central weight2; clock weights and shift determine the displayed one-scalar tensor.',
  'If beta vanished, the saturated evaluation image Q would have isotropic rank at most2. In rank1 it has at least3 sections; in rank2 its nonzero equivariant wedge-evaluation is injective, giving at least3 determinant sections. The actual numerical identity c1(F_*L)=2c1(L^(2)) gives slope3, so stability implies detQ.H<3q<=6, contradicting the divisor bound. Hence beta is the nonzero isomorphism claimed.',
  'Odd maximal-isotropic descent uses an actual splitting of the cyclic order3 theta extension and an etale degree3 quotient. The descended ample line has Euler characteristic1. The final proof of the principal-theta alternative is complete: square2 rules out multiple support; irreducible singular theta would normalize to genus1 and have smooth elliptic image, a contradiction. With several components, ampleness and total intersection2 force exactly two multiplicity-one components, each with square0 and mutual intersection1. They are smooth elliptic translates meeting transversely.',
  'Etale pullback supplies a reduced smooth or nodal member. Global generation supplies a second section nonzero at every node. In xy+z*u=0 with u a unit, relative singular equations put x,y in(z), and the equation then forces z times a unit to vanish; no singular component dominates the parameter trait. Properness excludes a generic singularity elsewhere. Ample-line vanishing gives connectedness of every divisor; adjunction gives genus4. No separability-dependent Bertini shortcut is used.',
  'The universal divisor sequence over every nonzero coefficient identifies the actual coherent quotient with Omega1_P2. Duality gives the restriction M_s^t from (s^[2])perp to s_perp. Multiplication in the actual Euler frames gives the displayed2x2 matrix and determinant c^2(1+t^3+u^3), a reduced smooth Fermat cubic. Its wall factorization and second semilinear iterate give stable rank1 on tu!=0.',
  'Constant scaling by c^-1 removes c from the Lang equation. On t=0 the nonzero solutions satisfy a^3=(1+u^3)^-1, irreducible because of the three simple poles. On u=1 the rational nonzero vector is(0,t^-1), while the other two satisfy w^2+w=t^-3+1; its odd-order pole prevents an Artin-Schreier coboundary. These actual restrictions supply elements of orders3 and2 in the same global S3 subgroup, hence full GL2(F2).',
  'The smooth-member open meets the Euler bijective open. Connected finite etale covers of the normal integral base remain connected on a nonempty open, so the actual smooth-family image is unchanged; neither test line nor the wall must consist of smooth members. Exactness of stable Frobenius fixed spaces in the actual cohomology sequence gives generic p-rank f(A)+2. No higher-rank odd-cover theorem outside its hypotheses is imported.',
  'The unchanged exact checker verifies38 universal characteristic-two identities, including frames, determinant, wall iterate, scalar normalization, both Lang slices and clock weights. It supplies algebraic identities only; the full geometric and field proofs are independent written arguments.'
 ],
 'external_source_scope': {
  'Sun': 'Original full Definition3.1, Lemmas3.2,3.3,3.5, Definition3.4 and Theorem3.6 with proofs, printed pp5-9 of arXiv math/0608043v2, were actually opened/read before this audit; retained root record notes/CP35_primitive_source_scope/record.json. Only the canonical filtration is imported.',
  'theta': 'Original AV Proposition8.19 and Corollary8.20 with complete proofs were read in the prior root wedge audit; the explicit clock/shift and cyclic splitting arguments are checked again here. No new external-source opening claimed in this recording script.'
 },
 'requested_repair': 'Complete principal-theta dichotomy with multiplicity and extra-component exclusions, retained under agents/obstructions_crystals/notes/primitive_type_1_3_theta_dichotomy.',
 'program_sha256': sha(source), 'author_output_sha256': sha(author), 'author_bytes_unchanged': True,
 'independent_program': str(copy.relative_to(w)), 'independent_output': str(independent.relative_to(w)),
 'independent_output_sha256': sha(independent), 'independent_runtime_seconds': b['runtime_seconds'],
 'author_runtime_seconds': a['runtime_seconds'], 'subprocess_wall_seconds': wall,
 'all_mathematical_output_identical': True, 'check_count': b['check_count'], 'executed_failures': [],
 'scope_guard': 'Fixed nonordinary surface, ample globally generated type(1,3) line. No assertion that all type(1,3) lines are globally generated, no arbitrary primitive odd-degree full image and no resolution of fixed-principal degree17 or general A.4.'
}
out.write_text(json.dumps(r, indent=2) + '\n')
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
 wr = csv.writer(f, delimiter='\t')
 for label in labels:
  wr.writerow([label, now, r['reviewer'], 'independent re-proof / computation or formal certificate', 'PASS: full seven-label proof/source audit and unchanged38-identity isolated rerun. See outputs/root_primitive_type_1_3_audit.json.'])
print(json.dumps({k:r[k] for k in ['status', 'actual_utc', 'candidate_sha256', 'independent_runtime_seconds', 'check_count', 'all_mathematical_output_identical']}, indent=2))
