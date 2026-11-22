"""Refresh post-CP23 proved gates only; preserve every historical checkpoint."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current23.py')],check=True,cwd=w)
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text()
rows=json.loads((w/'notes/item_status.json').read_text())
for r in rows:
 if r['item']=='A.3' and proved('agents/obstructions_crystals/A3_mixed_positive_index_smooth_pencil.tex'):
  r['where']+='; lem:DE-A3-positive-pushforward-jets; prop:DE-A3-positive-smooth-separable-pencil'
  r['gate']+=' In a sufficiently positive actual descent range, first jets of the rank-two pushforward are surjective, a general determinant curve is smooth integral, and its induced pencil is separable with ordinary curve Petri rank three or four. This does not identify the restricted surface cup-wedge map and does not close its common-radical gate. A positive index alone does not supply the required line-bundle descent.'
 if r['item']=='A.4' and proved('agents/monodromy/nonordinary_ppav_even_addition.tex'):
  r['status']='OPEN generally; every fixed nonordinary principal surface is classified at d=3^j and d=3^i+3^j; fixed elliptic products in every balanced degree'
  r['where']+='; thm:nonordinary-even-addition-candidate; cor:nonordinary-even-three-power-sums-candidate'
  old='Thus the remaining fixed nonordinary NONPRODUCT principal-surface degrees are the even d>=4 and the odd d>=5 that are not powers of3;'
  new='Whenever odd a,b have full images on the same fixed nonordinary principal surface, their sum d=a+b has geometric and arithmetic image Hom(F2^(1+f),F2^(9d²-4)) semidirect GL_(9d²-4), in relative rank9d²-3+f. Its covector kernel is irreducible and contained in every nonzero invariant subspace. In particular every d=3^i+3^j is now classified, including4,6,10,12 and18. The uniform proof uses actual lifted-node wreath groups, the many-theta graph, exact Lang extension, natural-module H1 vanishing and independent component blocks. Thus the remaining fixed nonordinary NONPRODUCT degrees are odd d>=5 not powers of3 and even d not sums of two powers of3 (the smallest is8);'
  assert old in r['gate'];r['gate']=r['gate'].replace(old,new)
  if proved('agents/monodromy/nonordinary_five_theta_self_isogenies.tex'):
   r['where']+='; prop:five-theta-twenty-self-isogenies-candidate'
   r['gate']+=' On the single fixed Jacobian of y²+y=x^5 overF16, all156 maximal isotropic5-planes are explicitly classified:20 give24-node theta images, and these20 are exactly the distinct kernels of the polarized self-isogenies2+g for the20 order-four automorphisms displayed in the proof. Geometric triples and tangencies are completely exhausted. This bounded geometric input does not supply degree-five full monodromy or a suitable neighbour for every surface.'
  if proved('agents/monodromy/nonordinary_uniform_five_theta_geometry.tex'):
   r['where']+='; lem:uniform-f0-order-four-presentation-candidate; thm:uniform-f0-five-self-isogeny-nodal-candidate; lem:nonproduct-three-theta-four-values-candidate'
   r['gate']+=' A separate uniform proof now supplies a nodal polarized5-SELF-isogeny on EVERY fixed f0 genus-two Jacobian: an explicit cyclic-order4 presentation, the endomorphism2+g and its residual degree2 divisor calculation exclude all triples and tangencies. The image lies in actual |5Theta| and has24 nodes. For every indecomposable principal surface, any fixed nonzero translated pairs P,P+h,Q,Q+k have only finitely many four-value failures for3Theta; the proof uses products of theta sections and the finite determinant-minus3 addition map. Thus these geometric prerequisites are closed, while isolated degree5 node inertia and full gluing remain open. No f1 five-self-neighbour theorem or degree5 full image is claimed.'
 if r['item']=='B.4' and proved('agents/reduction_descent/B_cyclic_torsion_threshold.tex'):
  r['where']+='; lem:B-RD63-point; prop:B-RD63-mixed; thm:B-RD63-arc; cor:B-RD63'
  old='A new exact tame-equivariant cyclic-level construction proves nu_min(p,e,h)>=n for every p>=5,h>=2,n>=2 and multiple e of p-1 with p^(2n-3)<e<p^(2n-2).'
  new='The exact mixed cyclic threshold now proves nu_min(p,e,h)>=n for every p>=5,h>=2,n>=2 and multiple e of p-1 with e>p^(2n-3), without an upper window. For p not dividinge, e>p^(2n-3) is also necessary for a p^n comparison between a whole potentially supersingular height-two group and a height-two system filtered by two potentially good height-one groups. The necessity uses actual rational torsion-chain Newton polygons; the construction uses an Eisenstein tame-equivariant arc and the fully lifted finite extension.'
  assert old in r['gate'];r['gate']=r['gate'].replace(old,new)
  r['gate']=r['gate'].replace('No upper bound or exact value at e=2(p-1) is claimed.','')
  if proved('agents/reduction_descent/B_tame_quotient_weight_gate.tex'):
   r['status']='OPEN generally; exact height-two indices at e=p-1 and e=2(p-1) for every p>=5, and at p=5,e=12'
   r['where']+='; lem:B-RD64-weighted-kernel; prop:B-RD64-formal; thm:B-RD64'
   r['gate']+=' For every p>=5, e=2(p-1), height2 and mu_p inK, the exact least manuscript index is2: actual p³-torsion determines the prime-to-p special inertia character, and an actual p² counterexample is sharp. The proof imposes the tame congruence on the ACTUAL quotient formal group: degree-p coefficients have valuation at leastp-1, giving q0=1 and q_(j+1)=min(a+q_j,pq_j+p-1). At this index q2=2p²-1 exceeds a/(p-1)=2(p²-1). The closed coefficientwise logarithm and integral Cartier saturation argument rule out distinct whole-formal characters; the mixed case is already excluded by the exact threshold.'
  if proved('agents/reduction_descent/B_p5_e12_high_quotient.tex'):
   r['where']+='; lem:B-RD65-Newton; lem:B-RD65-quotient; prop:B-RD65-nonsquare; lem:B-RD65-square; thm:B-RD65'
   r['gate']+=' Also nu_min(5,12,2)=2. In the nonsquare case, the actual good index288 gives high and low slopes72-B,B/5. The canonical high quotient sendsB to5B forB<12 and72-B forB>12, keeps the special Frobenius orbit, and converts a high-line-preserving125 comparison into an actual25 comparison. Common point-field breaks exhaust all wild and tame branches, including exceptionalB25. Square determinants are excluded by the actual-target two-Frobenius bound over tame degree dividing6. The next unresolved five-adic height-two index is e16; no equality there or general formula is asserted.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text());aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 24 work: even addition, five-isogeny geometry and exact torsion thresholds\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint24_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP24 gates from separately promoted canonical proofs.')
