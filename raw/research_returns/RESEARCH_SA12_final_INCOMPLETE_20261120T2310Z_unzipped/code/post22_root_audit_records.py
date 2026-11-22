"""Record completed actual-file/source audits and stage the next review; no ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
actor = dict(actor='root', model='GPT-6 Astra Pro (OpenAI)',
             effort='inherited; no separate setting asserted', run='SA12 run1',
             type='targeted proof check', recorded_utc=now)

def audit(name, path, sha, checks, primary, reused, scope):
    assert hashlib.sha256((root/path).read_bytes()).hexdigest() == sha
    record = dict(actor, path=path, sha256=sha, outcome='PASS', verdict='PASS',
                  actual_file_read='Complete statement and proof read from the actual current file.',
                  checks=checks, fresh_primary_reads=primary,
                  previously_checked_dependencies_reused=reused, scope=scope)
    p = root/name
    assert not p.exists()
    p.write_text(json.dumps(record, indent=2)+'\n')
    return name

g = audit('parts/D/post22_research/audit_SNC_general_geometry_root.json',
 'parts/D/post22_research/D_SNC_general_Brauer_geometry.tex',
 'af55454e3650c589f90ad8b2573088e2f5c113037790ab9757b35dde234edfe1',
 [
  'The support triangle retains the signed incidence kernel over Z/n; a spanning tree gives the free b1 graph-cycle factor without requiring a split Brauer extension sequence.',
  'Proper base change, n-divisible formal Picard kernel, multidegrees and coker(N mod n) give the full coefficient H2 order; the Kummer summand is retained.',
  'Vanishing of Br(Y)[n] and purity make the geometric period the lcm of residue orders. Componentwise root orders kill codimension-one ramification; the Azumaya reflexive-hull argument supplies an actual algebraic extension.',
  'The strict-local double residue identifies the node symbol and scalar commutator. For orders b,c and commutator order h dividing both, X^h,Y^h give bc/h^2 central factors and each block is M_h(k). Scalar powers are retained.',
  'The spectral torsor is etale over the adjacent-root curve, with coarse ramification h and residual root order c/h. The rank formula r=m_i*s_i and tame Riemann-Hurwitz formula follow with the stated number m_i/h of points.',
  'The scalar-weight-one Picard gerbe on the spectral root curve has trivial prime-to-p geometric Brauer class. Its formal neutralizing line lifts using coherent H2=0, with fixed coefficients not counted as parameters.',
  'All-ring node gluing uses split matrix-algebra Morita, projective multiplicity modules and actual frame atlases. Hom kills the scalar centre, hence has abelian quotient characters even when the bundles have noncommuting node actions.',
  'Each Hom character occupies exactly (a*a_i)*(a*a_j) monomials in the stated rectangle; summing character dimensions gives the claimed rr-prime budget.',
  'An actual algebraic Azumaya twisted bundle tensor all root-character lines generates all relevant inertia irreducibles. It is used for existence/algebraization only, without a uniform-rank or coordinate-cost assertion.'
 ],
 [dict(work='Lieblich, Period and index in the Brauer group of an arithmetic surface, arXiv:math/0702240v4',
       url='https://arxiv.org/pdf/math/0702240',
       scope='Freshly read complete Proposition3.2.1 statement/proof, printed10–11; complete Lemma4.3.1 and Proposition4.3.2 proofs, printed13–14; complete Proposition4.3.7 proof, printed14–15. The latter section has equal-prime and finite-field hypotheses; the composite mixed-order calculation is internal to the candidate.',
       retrieval_refs=['turn870067296view0','turn870067296view1','turn371940974view0'])],
 ['Full actual tree geometry source freshly reread for the shared support/Picard calculation.',
  'Prior checked absolute-purity compatibility, Stacks15.6.4–15.6.9, tame invariants, nilpotent etale invariance, and local Picard lifting reused; no fresh full-source claim for these.'],
 'Two geometry/residual-category statements only. No arbitrary-SNC count, hereditary uniformity, or full finite generation follows from this audit alone.')

shutil.copy2('/tmp/sa12_Steinberg608_root.png', root/'qa/Steinberg1960_p608_root.png')
c = audit('parts/D/post22_research/audit_classical_automorphism_crowns_root.json',
 'parts/B/post22_research/D_classical_automorphism_crowns_B.tex',
 '6a3107e7bb2bfd26e04ab62b8218619b9e07d52154b2508f4ae3663c6dcde21e',
 [
  'Steinberg3.2–3.6 supplies a normal inner-diagonal-field subgroup; the final quotient has order at most6, with split D4 triality and the characteristic2 B2/C2 exception retained.',
  'Checked all natural diagonal matrices against the simple-root values. The typeD last-root value is a_(l-1)*a_l/c; typeC is a_l^2/c, so no unavailable square root is required.',
  'The projective adjoint-torus realization is equivariant for diagram action; self-conjugate twisted characters normalize the twisted matrix model over F_(q^2). Entrywise field action is typed over that actual field, without an artificial Galois section.',
  'Projective centralization of unipotent root elements is actual centralization since their only eigenvalue is1. The natural-module commutant is scalar in the stated classical ranges, and field-part uniqueness makes the PΓL realization faithful.',
  'Checked the table against the source: Q=q for split families, Q=q^2 for unitary and minus-orthogonal families; twisted triality is explicitly excluded and low-rank repetitions are routed to stated families.',
  'Reused the previously proved exact group-order estimates: d^2*log(Q)<=16*log|S| includes the doubled coefficient-field exponent for minus orthogonal groups.',
  'B0=B intersect A0 is normal of index<=6. Applying the proved normal-subgroup crown corollary with kappa16 gives 16*(6*A_R+1)+5=96*A_R+21. Only the outer quotient is required radially tame.',
  'The finite-exception remark uses the conjugation permutation action of Aut(S) on S, which is faithful and has no nonidentity scalar permutation matrix; it makes no additional classification assertion.'
 ],
 [dict(work='Steinberg (1960), Automorphisms of finite linear groups, Canadian Journal of Mathematics12,606–615',
       local_source='parts/B/sources/Steinberg1960/published.txt',
       url='https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16023F257E0F21D57873B1450E9F15E4/S0008414X00010245a.pdf/automorphisms-of-finite-linear-groups.pdf',
       scope='Freshly read all written Sections2–7, including complete statements3.2–3.6 and their written proofs. Initial long output omitted a short passage of printed611; the entire page was reread separately before this audit. Root actually viewed the rendered published608 image to check exact inequalities, normal sequence, graph indices and field orders.',
       image='qa/Steinberg1960_p608_root.png', retrieval_refs=['turn396287226view0'])],
 ['Previously checked classical natural models/order formulas and the current normal-subgroup crown theorem are reused. This is not a fresh complete reading of Taylor or of all Chevalley/Bruhat sources cited inside Steinberg.'],
 'Recognition within the same post-review14 unbounded-field crown enlargement; no additional independent movement and no wild-outer-quotient conclusion.')

p = root/'code/output/review15_main_assessment.json'
a = json.loads(p.read_text())
mname = 'parts/C/post21_research/integration_manifest_C_normal_subgroup_crowns.json'
m = json.loads((root/mname).read_text())
assert hashlib.sha256((root/m['path']).read_bytes()).hexdigest() == m['sha256']
if not any(v['path']==m['path'] for v in a['verified_files']):
    a['verified_files'].append(dict(path=m['path'],sha256=m['sha256'],audit_manifest=mname))
a['assessment_staged_utc'] = now
a['remaining_strongest_gates'][3] = ('General monolithic nonabelian crowns outside the proved radially tame one-smooth-exceptional-curve faithful-linear and faithful-projective families. The projective family allows unrestricted diagonal and field-image actions; it suffices that a bounded-index normal subgroup containing the simple socle embeds in PΓL with the stated order comparison. No ambient action of the entire outer group is required. Wild radial permutation quotients, other realizations and other geometries remain unresolved.')
a['auxiliary_not_movement'][-1] = ('The coherent-gerbe, single-sector and skew-unit statements, and the completed bounded-index normal-subgroup refinement, belong to the same unbounded-field crown enlargement. Their assembly and later named-family recognition are not separate movements.')
p.write_text(json.dumps(a,indent=2)+'\n')

s = (root/'code/formal_review14.py').read_text()
s = s.replace('review14','review15').replace('Review14','Review15')
s = s.replace('review13','review14').replace('Review13','Review14')
s = s.replace("datetime(2026,11,20,16,10", "datetime(2026,11,20,17,10")
s = s.replace("'review_number':14", "'review_number':15").replace("'review':14", "'review':15")
s = s.replace('checkpoint21','checkpoint22').replace('Checkpoint21','Checkpoint22')
s = s.replace("'latest_successful_checkpoint':21", "'latest_successful_checkpoint':22")
s = s.replace('16:10UTC','17:10UTC').replace('16:40UTC','17:25UTC')
s = s.replace("'2026-11-20T17:10:00+00:00'", "'2026-11-20T18:10:00+00:00'")
s = s.replace("'2026-11-20T16:40:00+00:00'", "'2026-11-20T17:25:00+00:00'")
assert not (root/'code/formal_review15.py').exists()
(root/'code/formal_review15.py').write_text(s)
s = (root/'code/scheduled_review11.py').read_text().replace('review11','review15').replace('13:10UTC','17:10UTC').replace('2026,11,20,13,10','2026,11,20,17,10')
(root/'code/scheduled_review15.py').write_text(s)

with (root/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Post-checkpoint22 actual-file audits and next review preparation\n\nINCOMPLETE. '+now+'. Root completed exact-hash audits of the arbitrary-SNC geometry packet and the classical-family crown recognition packet, with the fresh primary scopes recorded in their audit files. They remain candidates until every required audit and promotion is complete. The previously fully checked C normal-subgroup crown corollary is assembled (one statement/four events) and included within the same crown reduction staged for review15. Review15 is only prepared, not performed; it is due17:10UTC. No archive was created.\n')
print(json.dumps(dict(utc=now,audits=[g,c],review_prepared=15,review_completed=False,archive_created=False),indent=2))
