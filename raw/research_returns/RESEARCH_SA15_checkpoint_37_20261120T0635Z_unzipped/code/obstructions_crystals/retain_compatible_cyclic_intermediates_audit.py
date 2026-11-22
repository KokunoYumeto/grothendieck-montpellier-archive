"""Complete independent five-assertion compatible-intermediate proof audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
src=root/'agents/monodromy/post_CP33_compatible_cyclic_intermediates_candidate.tex'
expected='a40f648e4c968f2b3a2cd105b4866d7ba992361b46de9b62a514ff77535103ae'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)==expected
labels=re.findall(r'\\label\{((?:lem|prop|thm|cor|rem):[^}]+)\}',src.read_text())
assert len(labels)==5
now=datetime.now(timezone.utc).isoformat()
record={
 'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,
 'auditor':'/root/obstructions_crystals','candidate':str(src.relative_to(root)),
 'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire five-assertion candidate read. Entire final general-a source proof, entire canonical narrow deck-slice proof and full group structure freshly read; actual common-incidence proof and full arbitrary-odd-cover wall/inertia proof freshly reread with their hypotheses. All maps and restrictions rederived independently.',
 'checks':[
  'For D=(Z/ell)^2 and ell odd, group-algebra convolution gives e_J^2=e_J and e_D*e_H=e_D. Counting the unique line of every nonidentity element and the even number ell+1 through the identity gives sum_H e_H=1+e_D. A vector killed by all line averages equals e_D*v and is also killed by e_D, so it is zero. This needs no character splitting or invariance hypothesis on a candidate subspace.',
  'The exact factorizations A->A/H->B have degrees ell and exact pullback line bundles, with chi(M_H)=9ell. All surfaces stay nonordinary under the odd isogenies. The full-radical group theorem applies because the arbitrary-odd-cover inertia theorem supplies an actual full radical; its algebraic classification does not require an unproved principal-polarization hypothesis on A or an extra covector theorem.',
  'The common central open S_D is genuinely nonempty: the complete incidence theorem gives smooth sharp degree-one sections for which all nontrivial D-character multiplication blocks are invertible. Etale pullbacks are smooth and ample connectedness makes them connected. The relative trivial part is the base relative Frobenius, and all other finite half-character cycles are bijective, so the total relative rank is9ell^2-1.',
  'For every H, inner characters are exactly the D characters trivial on H. Outer characters form their cosets, and the same original block invertibility implies every intermediate smooth/sharp and outer-cycle condition. Thus S_D lies in the explicitly defined connected normal integral open T_H, rather than being assumed to intersect an arbitrary previously chosen dense open.',
  'On T_H the H deck action is on the actual pulled-back universal curve and commutes with Frobenius. Odd etale pullback and trace identify its invariant Lang part with the intermediate relative local system, including the constant ambient-cohomology quotient. At S_D these operators are literally the restrictions of one D action on one universal pullback family.',
  'The map e_H composed with the restricted inclusion of the global canonical K is a morphism of finite etale local systems on connected T_H. Its zero locus is open and closed, so vanishing on a nonempty open implies vanishing everywhere. No deck invariance of K is needed to define this composition, and no specialization across a rank drop occurs.',
  'The explicit full intermediate GL assumption allows application of the general-a source bound with inner a=ell and outer n=ell. It gives e_H*K=0 on a nonempty source open, hence on T_H and then on the same S_D for every line. All projectors now act on the same fibre of the same K, and their group-algebra identity forces K=0. Constant rank transports this to U and the full-radical theorem gives the full target GL.',
  'For the principal target corollary the outgoing maximal-isotropic quotient is exact, so T_H=eta_H*Theta_B is ample with square2ell. Its type has d1*d2=ell and d1 dividing d2, hence(1,ell). Its cube pulls back to the exact3ellTheta_A line. The needed full images of these particular ell+1 nonprincipal cubic systems remain explicit hypotheses.',
  'The scope correctly leaves the new cyclic-source full-image problem open. One cyclic deck group alone only gives the nontrivial-part inclusion, and neither its character multiplicities nor this compatible-intermediate criterion supplies an unconditional new prime degree.'
 ],
 'dependencies':[
  'agents/obstructions_crystals/A4_general_odd_source_Cartier.tex',
  'agents/obstructions_crystals/A4_Lang_deck_slice_bound.tex',
  'agents/obstructions_crystals/A4_common_Cartier_incidence.tex',
  'agents/monodromy/ppav_all_odd_full_root_inertia.tex',
  'sections/A_full_radical_image_structure.tex'
 ],
 'finite_computation':'None needed or executed; direct group-algebra and finite-local-system proof.',
 'fresh_external_source_opening':False,
 'scope':'Conditional compatible-intermediate criterion. No new unconditional full-image degree, no arbitrary dense-open intersection with a special slice, and no rank-drop full-fibre comparison.'
}
out=own/'compatible_cyclic_intermediates_independent_audit.json'
with out.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'independent_full_proof_audit',str(src.relative_to(root)),
                    'Full proof and invoked dependency hypotheses; actual common local-system fibre and line-projector identity',
                    'PASS',str(out.relative_to(root))])+'\n')
assert sha(src)==expected
print(json.dumps({'status':record['status'],'actual_utc':now,'candidate_sha256':expected,
                  'record':str(out.relative_to(root)),'labels':labels}))
