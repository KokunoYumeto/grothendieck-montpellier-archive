from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
other=own.parent/'monodromy'
source=other/'ppav_all_odd_full_root_inertia_candidate.tex'
expected='0bb79d06ae2ec1a09d9ad1ac3b9cbad85d34621d91357129a4a9c5c11a4de8cf'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source)==expected
s=source.read_text()
labels=[x for x in re.findall(r'\\label\{([^}]+)\}',s) if not x.startswith('subsec:')]
assert len(labels)==5
now=datetime.now(timezone.utc).isoformat()
record={'status':'FULL_INDEPENDENT_PROOF_PASS','actual_utc':now,
 'source':str(source),'source_sha256':expected,'labels':labels,
 'checks':[
 'The exact symmetric theta splitting gives the standard finite Heisenberg matrices in the same e_i basis. R:e_i^(2)->e_i^* is literally the identity in those bases, as rechecked from the complete symmetrizer proof. Thus the central matrix is symmetric alternating, has both kernel vectors s, and its relative wall is exactly sum s_i^3, not an unspecified linear transform.',
 'TCM5 gives the cross block c_(i-j)/2*x_(i+j)/2 with one common scalar. Reindexing i=2u,j=2v leaves the variable x_(u+v), and setting x=s produces the exact Moore determinant in the fixed central coordinates.',
 'For multiplication by the original s, choosing phi_M(u)=Q with Q^2=P and the input basis e_j(z+2u) and output e_k^(2)(z+F(u)) gives the actual line bundles stated. Substitution w=z+u,a=-u into TCM5 retains the first input e_i(z) literally. Its matrix is c_(k-j)(-u)*s_(2k-j), with the sole variable permutation s_v->s_-v. This preserves Fermat exactly. The fixed2-torsion correction changes only the coefficient parameter.',
 'Both coefficient parameters correspond to nontrivial odd twists, so the already proved cross-Cartier theorem makes their determinant polynomials nonzero. The separately fully audited universal Fermat theorem therefore proves nonvanishing on the same integral central cubic for both multiplication and dual blocks.',
 'The nonzero central Pfaffian q is not proportional to Fermat by the earlier complete four-direction argument, reread here. Finitely many nonempty determinant opens and q!=0 intersect on the smooth integral Fermat cubic. The multiplication and inverse-character dual decompositions then give ranks N-1 simultaneously, with the same trivial-block left kernel s. No smoothness of the selected divisor is assumed.',
 'The universal hypersurface sequence, H1(L^-1)=0, and Serre duality produce the actual relative Euler bundle Omega^1 on the entire coefficient space, including singular members. Coherent Frobenius is regular and equals M_s^t from ann(s^[2]) to ann(s) on charts. No stable-fiber identification across a rank drop is used.',
 'The complete previously proved moving-kernel wall proposition was reread: the dual-maximal-rank condition makes kappa etale, the wall is smooth with simple determinant, and maximal kernel variation gives stable loss one. The entire strict-henselian Artin-Schreier lemma was reread, including imperfect separably closed residue fields and all independent t^-2 classes. It gives the full hyperplane radical of order2^(N-2).',
 'Restriction of a finite etale generic representation from a normal integral invertibility open to its dense smooth-member open preserves its image because connected finite etale covers remain integral after restriction. Thus the computed divisorial inertia lies in the smooth-family image even if the wall parametrizes nonsmooth curves.',
 'The fixed-surface odd-degree corollary uses the exact outgoing maximal-isotropic quotient with symmetric principal descent, not mere equality of numerical polarizations. The pullback line bundle is exactly O(3dTheta), n=d^2, giving the stated rank and radical order. The remaining global connectivity/irreducibility problem is explicitly not resolved.'
 ],
 'dependency_read_scope':[
 'Entire ppav_theta_cartier_symmetrizer.tex, including exact finite-Heisenberg Frobenius identification.',
 'Entire relevant TCM1--TCM5 proof and odd outgoing-isogeny corollary in ppav_twisted_Cartier_Moore.tex.',
 'Complete maximal-kernel-variation and common-wall inertia proofs in Cartier_kernel_wall_inertia.tex.',
 'Complete moving-kernel-full-root-inertia proof in mixed_degree_one_uniform_full_groups.tex.',
 'Complete degree-one q-nonvanishing/relative determinant proposition and existing Q-not-proportional proof reread.',
 'Full Fermat nondivisibility proof and unchanged exact checker independently audited separately this turn.'
 ],
 'Fermat_audit':'outputs/independent_Moore_Fermat_full_audit.json',
 'source_scope':'No new external-source opening claimed. Audited canonical geometric inputs are used with the explicit complete internal rereads above.',
 'new_numerical_program':None,
 'scope':'Nonempty actual maximal-rank Hasse wall and full local hyperplane inertia for all fixed odd systems; no new full global-image degree or connectivity assertion.'}
(own/'outputs/independent_odd_wall_full_audit.json').write_text(json.dumps(record,indent=2)+'\n')
with(own/'CHECK_EVENTS.tsv').open('a')as f:
 for label in labels:f.write('\t'.join((now,label,'INDEPENDENT_FULL_PROOF_PASS','Same Fermat coordinates, nonempty common wall and full local radical; global generation open',str(source),'outputs/independent_odd_wall_full_audit.json'))+'\n')
print(json.dumps(record,indent=2))
