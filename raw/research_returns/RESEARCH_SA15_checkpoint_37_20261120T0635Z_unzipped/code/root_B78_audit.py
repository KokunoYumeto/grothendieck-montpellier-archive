"""Full wild CM proof/source audit and corrected isolated finite certificate."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/reduction_descent/B_wild_CM_layer_candidate.tex'
source=w/'agents/reduction_descent/code/verify_wild_CM_layer.py'
author=source.with_suffix('.output.json')
out=w/'outputs/root_B78_audit.json'
assert not out.exists()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)=='9f40d83044089c669d36982ab2760e06d59c8baecf6a4115c78ce5905e9e7fa7'
assert sha(source)=='ff92c68d99fdf53703d5a665b524ebc420e27a4abb4ee5947b2cf946ed07a499'
before=sha(author)
assert before=='c2f5aeb9ee273566d5df260c1b631d1e9885c9999ae8704ba3b61df09cf31fe6'
snapshot=w/'code/audit_snapshots/B78_root_independent_certificate.py'
assert not snapshot.exists();shutil.copy2(source,snapshot)
with (w/'outputs/root_B78_independent_certificate.stdout.txt').open('w') as stdout, (w/'outputs/root_B78_independent_certificate.stderr.txt').open('w') as stderr:
    run=subprocess.run([sys.executable,str(snapshot)],cwd=w,stdout=stdout,stderr=stderr)
assert run.returncode==0
a=json.loads(author.read_text());b=json.loads(snapshot.with_suffix('.output.json').read_text())
omit={'runtime_seconds','actual_utc'}
assert {k:v for k,v in a.items() if k not in omit}=={k:v for k,v in b.items() if k not in omit}
assert before==sha(author) and sha(source)==sha(snapshot)
data={'status':'FULL PROOF, PRIMARY SOURCE AND CORRECTED EXACT CERTIFICATE PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'candidate_sha256':sha(candidate),
 'checks':{
  'lem:B-RD78-model':'Complete B52 CM and integral LT-model proofs freshly reread. Reduction injectivity, finite-extension endomorphism descent, the two ramified-normalizer cases, the unramified unit-normalizer centralization, the nonsquare stable-lattice generator and the averaged deformation parameter do not use prime-to-p absolute index. The unique oriented good CM model and finite tame quotient character therefore extend at arbitrary e. The endomorphism notion remains finite-extension endomorphisms, not abstract algebraic-closure generic endomorphisms.',
  'lem:B-RD78-layer':'Fresh original Lubin-Tate Lemma1 and Theorems1/2 full proofs read on printed pp381-384, together with full Stacks032A proof. The original finite-residue scope is explicitly extended by the written Eisenstein polynomial and free rank-one torsion argument over W(k), not by unproved reciprocity over infinite residue fields. The coefficient ring gives finite degreee, so the division-image index has p-part at mostp^v. The abelian quotient is killed byp^v; the binomial successive-lift argument gives all1+p^(v+1) units modulo p^n and hence the terminal layer for n>=v+2.',
  'prop:B-RD78-CM':'Compatible tangent orientations identify both good factors with the same LT character. An actual mod-p^n intertwiner centralizes all1+p^(n-1)b on the common good field. Its reduction commutes with F_(p2), hence is nonzero field multiplication. The full G_K identity then cancels this scalar and theta, yielding equality of the finite tame twists by injective Teichmuller reduction. Completed maximal unramified passage preserves e and the required inertia comparison.',
  'thm:B-RD78':'At first wilde=p(p-1), square determinants are covered by B77 and nonsquare CM determinants by the n3 layer argument. The lower pair uses the actual full LTp2 division field and its fixed subgroup mu_(p+1) times scalarFp, giving e=p(p-1) and mu_p by the norm determinant. The exact mod-p2 wild image is scalar, so field conjugation intertwines theta*omega with theta*omega^(3p-2). The finite special exponent orbits are disjoint for everyp>=5, with common primitive norm. This is an actual field and actual generic BT twists, not just compatible formal character data. The exact restricted index is2; any full remaining p5/e20 actual125 failure has a non-CM member.',
  'rem:B-RD78-scope':'Complete initial and corrected finite code read. Root found that the explicitly labelled terminal additive coordinate was p^(n-1), the zero class, although the stronger p^v test was correct. The executed initial source/output are preserved, and the corrected direct test uses nonzero p^(n-2). The corrected literal isolated rerun passes every field comparison with author bytes unchanged. No non-CM recovery follows.'},
 'independent_runtime_seconds':b['runtime_seconds'],'counts':b['counts'],
 'program_sha256':sha(source),'author_output_sha256':before,
 'author_output_unchanged':True,'all_mathematical_fields_equal_author':True,
 'fresh_primary_reads':[
  'Lubin and Tate1965, original Annals81(2),380-387: complete Lemma1 proof printed381-382, full Theorem1 proof382-383, full Theorem2 proof383-384. Original finite residue field scope explicitly retained. https://math.bu.edu/people/jsweinst/AWS/Files/LubinTateFormalCMinLocalFields.pdf',
  'Stacks Project Theorem10.160.8 Tag032A: complete coefficient-ring existence and power-series presentation proof. https://stacks.math.columbia.edu/tag/032A'],
 'reused_source_scope':'Previously audited Hopkins-Gross deformation and reduction-injectivity passages and Tate full faithfulness reused through freshly reread complete B52 proofs; no fresh original read of those two sources claimed.',
 'scope_limit':'Exact first-wild index2 only within the potentially CM potentially supersingular subclass. Full first-wild index remains in{2,3}; higher heights and non-CM actual comparisons remain open.'}
out.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
