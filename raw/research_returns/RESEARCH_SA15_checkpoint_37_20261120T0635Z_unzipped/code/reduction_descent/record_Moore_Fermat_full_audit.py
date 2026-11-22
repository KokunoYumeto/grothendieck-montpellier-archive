from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
other=own.parent/'obstructions_crystals'
source=other/'post_CP31_Moore_Fermat_nondivisibility_candidate.tex'
expected='35451b9383a4772ab7114cb9f47b444670bac239eedcd772def059475e0071f6'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source)==expected
s=source.read_text()
assert r'c_{Ag+q}' in s and r'Aa+2q' in s and r'Ab+q' in s
code=json.loads((own/'outputs/independent_Moore_Fermat_code_audit.json').read_text())
assert sha(other/'code/verify_Moore_Fermat_nondivisibility.py')==code['author_hashes']['program']
assert sha(other/'code/verify_Moore_Fermat_nondivisibility.output.json')==code['author_hashes']['output']
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==5
now=datetime.now(timezone.utc).isoformat()
checks=[
 'Monic x0 division commutes with every parameter specialization. The literal determinant and complete remainder were reconstructed independently; all coefficient/support witnesses are polynomial identities and nonzero monomial exclusions, not sampling of field points.',
 'Affine covariance is exact: c_(Ag+q), x_(Ag) are obtained by row Aa+2q and column Ab+q. Their sum removes3q and difference leavesq. Character scaling is a row/column scaling and fixes cubes and parallel-line products. The final q notation repair was read and verified.',
 'The three-block affine-line restriction gives product of the three displayed Hesse cubics. Reduction modulo the restricted Fermat polynomial forces at least one line cube sum to vanish, since this polynomial cannot divide a coordinate monomial. Four-direction choices are exactly concurrent9 or triple-plus-one72.',
 'The six-element stabilizer fixes the triple point and fourth affine line, permuting the other three directions. Its point orbits are exactly the triple point, three double points, three single points, and two uncovered points listed in the proof.',
 'The five cube identities in the nonconcurrent normal form follow from the four selected line sums and the total cube sum. The nonzero f/d ratio is a cube root, and a linear character sets f=d without changing the equations.',
 'For full support, all factors of K=d^2*a*b*u*v*w*t are units. Cubing each of the three product equations retains the rs(r+s) cross term and gives (D+A)U=K, (D+W)B=K, (D+V)T=K. The exact identity between their left sides contradicts K nonzero. The corrected ideal certificate agrees.',
 'For eight support: an uncovered zero forces two zeros; a triple-point zero gives opposite-cube equalities. A single zero a=0 gives the explicit cubic contradiction B^2+(1+B)^2=1. A double zero u=0 gives A=1, D=W=V and all four opposite cube pairs about index2. Covariance covers every zero location.',
 'The two/four/six-support factors are actual remainder coefficients, independently checked. The complete previously audited matching/reflection proof and phase-extension construction were reread. Eight-support phase substitutions retain independent variables and every bad phase has a nonzero monomial witness. Thus necessity is universal.',
 'Membership in V_(h,ell) makes the actual Moore matrix alternating of odd size after the stated row operation, proving the reverse implication and equivalence with the81 spaces. No scheme-theoretic radical, geometric coordinate identification, or full monodromy conclusion is imported.'
]
record={'status':'FULL_INDEPENDENT_PROOF_AND_CODE_PASS','actual_utc':now,
 'source':str(source),'source_sha256':expected,'labels':labels,'checks':checks,
 'proof_scope':'Entire final five-label proof read and independently rederived. Complete earlier Moore support/matching/classification proof reread. Final covariance notation-only delta verified.',
 'code_scope':code['code_read_scope'],'independent_runtime_seconds':code['independent_runtime_seconds'],
 'code_audit_record':'outputs/independent_Moore_Fermat_code_audit.json',
 'author_hashes':code['author_hashes'],'author_hashes_unchanged':True,
 'all_mathematical_output_identical':True,'counts':code['counts'],
 'remainder_sha256':code['remainder_sha256'],
 'retained_author_failure':'Initial omitted-cross-term ideal assertion preserved by author; no conclusion inferred from that failure.',
 'source_scope':'No new external-source opening or numerical geometric sampling claimed.',
 'limitation':'Universal algebraic statement only; same-coordinate geometric application requires its own proof.'}
(own/'outputs/independent_Moore_Fermat_full_audit.json').write_text(json.dumps(record,indent=2)+'\n')
with(own/'CHECK_EVENTS.tsv').open('a')as f:
 for label in labels:f.write('\t'.join((now,label,'INDEPENDENT_FULL_PASS','Complete Fermat nondivisibility proof and literal universal checker; actual geometry not inferred',str(source),'outputs/independent_Moore_Fermat_full_audit.json'))+'\n')
print(json.dumps(record,indent=2))
