"""Record the complete root audit of arbitrary-quotient faithful-linear crowns."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
root=Path(__file__).resolve().parents[1]
path='parts/D/post25_research/D_arbitrary_quotient_linear_crowns.tex'
data=(root/path).read_bytes(); sha=hashlib.sha256(data).hexdigest()
assert sha=='661dcb3da0e0d7062e0f35a93926fe745a508edf6b9b820d3995e94e2332f33c'
delta=json.loads((root/'parts/D/post25_research/arbitrary_linear_crowns_typography_delta.json').read_text())
assert data.decode().replace(delta['new'],delta['old'],1)==(root/delta['snapshot']).read_text()
out=root/'parts/D/post25_research/audit_arbitrary_quotient_linear_crowns_root.json'
assert not out.exists()
record=dict(actor='root',model='GPT-6 Astra Pro',effort='setting not independently exposed',run='SA12 run1',
 recorded_utc=datetime.now(timezone.utc).isoformat(),type='targeted proof check',verdict='PASS',path=path,sha256=sha,
 labels=['D:arbitrary-quotient-faithful-linear-crowns'],
 actual_file_scope='Complete initial actual c7c13ca0 theorem, every proof line and scope remark read in full; sole final661dcb3d display-command change read, with exact reversal verified.',
 certificate_scope='Mathematical proof audit; no numerical certificate.',
 checks=[
 'The stabilizer H has index t; its fixed outer coordinate character determines H0 of total index at with a<=b0, independently of a lift. The new ordinary hereditary theorem applies to this arbitrary connected punctured cover.',
 'The exact nonsplit transport formula and its inverse modulo N/S conjugacy are the previously fully checked wreath comparison. No splitting or tame extension is inserted.',
 'Surjectivity to L_k forces its coordinate lifts to be pairwise nonconjugate by N; equal classes would put a pair in a proper conjugate diagonal. This gives the needed upper bound by stabilizer lift classes.',
 'Each ambient GL conjugacy orbit contains at most |GL| actual S-conjugacy restriction classes, regardless of normalizers. S-conjugation to an actual representative preserves B-valuedness and the outer character.',
 'At most a-1 additional fixed coset representatives determine an extension of a normalized restriction. Their prescribed outer images each allow only |S| choices, yielding |S|^(a-1), not an uncontrolled power of |B|.',
 'The size comparison r^2 log(q)<=kappa log|S| and t>=1 give the stated uniform c_R and k<=|S^t|^c_R. The quotient generator number is not used for multiplicity.',
 'The complete primary LMT written proof was freshly reread. For s>=d(L)=max(2,d(P)), its equations give psi_L(s)>=|N|^(s-1)/(2t|OutS|); the outer bound and |S|>=60 give denominator<=|N|. Choosing s=max(2,d(P),c_R+2) is exact.',
 'Pure permutation L=S^t semidirect P has unique minimal normal N and trivial socle centralizer. A nonabelian minimal normal subgroup is not Frattini; a maximal subgroup avoiding it has trivial core. Thus this specialization meets the monolithic primitive hypotheses.',
 'The centre-free SL_(p^u) example has gcd(p^u,p^f-1)=1, the stated known excluded small parameters, and the previously checked quadratic natural-order comparison. It supplies an unbounded-rank faithful-linear family.',
 'The theorem genuinely removes the one-curve/radially-tame restrictions for this precise linear crown class. It retains the faithful embedding, bounded residual outer index and d(P); no arbitrary projective, unrestricted field-semilinear or full-generation inference is made.'
 ],
 fresh_primary_reads=[dict(path='sources/LMT2020/pp10-13.txt',underlying_primary='sources/LMT2020/paper.pdf',
 locator='Entire retained published pp10-13 excerpt, in particular Proposition2.6 full statement and written proof, equations(2.1)-(2.2), and p13 outer-automorphism bound.',
 scope='All written proof in the excerpt reread. Referenced classification/probability/generation inputs are explicitly Known; no fresh recursive reading of their original sources is claimed.')],
 rechecked_actual_dependencies=['Complete parts/C/post21_research/D_normal_subgroup_projective_crowns.tex, including S-normalized extension count.','Complete parts/B/post21_research/D_bounded_field_automorphism_crowns_B.tex, including the actual orbit-splitting argument.','Root complete arbitrary-cover ordinary growth audit in this same interval.'],
 movement_scope='Concrete enlargement of the controlled nonabelian crown family. Group with its new ordinary hereditary count and prerequisites as one reduction in the scheduled formal review; no requested-row status change.'
)
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(root)),'sha256':sha,'verdict':'PASS'},indent=2))
