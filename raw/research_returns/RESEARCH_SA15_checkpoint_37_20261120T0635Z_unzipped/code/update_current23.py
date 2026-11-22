"""Refresh the actually proved post-CP22 gates; candidates never close a row."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current22.py')],check=True,cwd=w)
def proved(rel):
    p=w/rel
    return p.exists() and '\\status{Candidate' not in p.read_text()
common=proved('agents/obstructions_crystals/A3_mixed_common_polarization_power.tex')
petri=proved('agents/obstructions_crystals/A3_mixed_positive_index_Petri.tex')
d3=proved('sections/A_nonordinary_degree_three_full.tex')
b62=proved('agents/reduction_descent/B_tame_cyclic_level_counterexamples.tex')
powers3=proved('agents/reduction_descent/A_nonordinary_powers_three.tex')
d2=proved('agents/monodromy/nonordinary_ppav_degree_two_wreath_theta.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.3' and common:
        row['status']='OPEN generally; all mixed classes with a(M)<=b(M) and all elliptic products are classified in every degree'
        row['where']+='; lem:DE-A3-mixed-common-power-root; thm:DE-A3-mixed-index-ordered-ranks; cor:DE-A3-mixed-primitive-rank-gate'
        row['gate']=('Over perfect characteristic-two fields, all ordinary abelian surfaces have rank chi(M)n²-1 for every ample M and n>=3; all mixed and supersingular elliptic products have their proved parity formulas in every degree and every factor modulus. Nonordinary principal surfaces have their exact all-degree rank formulas. For a mixed surface and ample M, write D=chi(M), with ordinary and local-local integral polarization indices a,b. If a=0 the relative rank for |M^(3d)| is9Dd²-1 for odd d and9Dd²-2 for even d. If0<a<=b it is9Dd²-2 for EVERY positive d. The proof supplies the actual maximal root H^(2^min(a,b))=M on the same geometric surface; its indices subtract min(a,b), so the complete systems themselves coincide after exponent rescaling. Thus the remaining mixed nonproduct problem reduces to primitive a>0,b=0. In that primitive sector the proved bounds are9Dd²-2^a<=r<=9Dd²-2 in odd degree and9Dd²-2^(a+1)<=r<=9Dd²-2 in even degree; a=1 and odd d are already exact. The unresolved primitive degrees are a>=2 odd and a>=1 even. Their exact sufficient sharpness gate is a nonzero determinant in the actual trace-zero family Psi_s:Delta_s->Hom(H1(Q-dual),H1(Q)); failure means a zero space or one rank-one nilpotent line, so image dimension at least2 suffices. The symplectic monad gives that exact map, with determinant directions Delta_s and kernel K tensor P. Other inseparable nonordinary polarization types and arbitrary-X structural ranks remain open. All ambient-hypersurface conclusions retain their proved restriction regularity bounds.')
        if petri:
            row['where']+='; lem:DE-A3-positive-restricted-Petri-note; cor:DE-A3-positive-Petri-radical-note'
            row['gate']+=' The restricted symmetric cup-wedge pairing is the precise dual map. Its common radical vanishes exactly when an invertible variation exists. Its annihilator is H1(KP) dual; the twist cannot be omitted or the direction space enlarged to all sections. This is an equivalent test, not an additional nonvanishing theorem.'
    if row['item']=='A.4' and d3:
        row['status']='OPEN generally; every fixed nonordinary principal surface is classified in degrees one and three, and fixed elliptic products in every balanced degree'
        row['where']+='; lem:normal-base-clopen-Lang-closure-candidate; lem:three-theta-odd-labelled-graph-candidate; thm:three-theta-conditional-full-image-candidate; lem:char2-genus-two-three-total-ramifications-candidate; cor:nonordinary-theta-three-torsion-nodal-norm-candidate; lem:root-nonordinary-trigonal-three-excluded-candidate; lem:root-nonordinary-nonproduct-three-neighbor-candidate; lem:root-nonordinary-three-theta-clean-boundary-candidate; prop:nonordinary-three-torsion-node-product-candidate; prop:nonordinary-three-torsion-gluing-hearts-candidate; thm:root-every-nonordinary-ppav-degree-three-full-candidate'
        row['gate']=('All projective-space cases and the proved effective eventual ordinary principal-surface results persist. Over every perfect characteristic-two field and on every fixed nonordinary principally polarized abelian surface, geometric and arithmetic monodromy are GL8(F2) in degree1 and GL80(F2) in degree3, on complete systems |3Theta| and |9Theta|. There is no generic-modulus restriction. The degree1 proof uses the actual stable Cartier/Coble tensor and full root inertia. Degree3 uses a nonproduct (3,3)-neighbour, exact exponent-three theta nodality, finite (1,3) eigenmaps, independent S18 factors, all type-heart gluing translations, and the normal Lang closure/splitting argument across the lower-rank theta boundary. Two independent trigonal proofs exclude theta triples; pair tangencies are also excluded. In every odd degree an actual natural GL8 block fixing a complement is already proved. The remaining fixed nonordinary NONPRODUCT principal-surface degrees are2 and every d>=4; the full structural classification for arbitrary X remains open. For every fixed supersingular elliptic product the odd image is GL_(9d²-1), and the even image is F2^(9d²-4) semidirect GL_(9d²-4) in rank9d²-3. For every fixed mixed elliptic product the odd image is GL_(9d²-1), and the even image is Hom(F2²,F2^(9d²-4)) semidirect GL_(9d²-4) in rank9d²-2, with irreducible common kernel contained in every nonzero invariant subspace. Every mixed strip of factor degrees(3,b), b>=3, is classified as previously stated. Geometric generic nonordinary ppav strata have the exact groups in every degree, and every finite prescribed degree set has a common nonempty open and finite-field examples. The general odd-kernel conditional graph criterion remains explicit: clean individual theta norms and full node/gluing input are proved here only for exponent3, so arbitrary odd degrees are not inferred from it.')
    if row['item']=='B.4' and b62:
        row['where']+='; lem:B-RD62-arc; lem:B-RD62-extension; thm:B-RD62; cor:B-RD62'
        row['gate']+=' A new exact tame-equivariant cyclic-level construction proves nu_min(p,e,h)>=n for every p>=5,h>=2,n>=2 and multiple e of p-1 with p^(2n-3)<e<p^(2n-2). In particular nu_min(p,2(p-1),h)>=2, and e_n=p^(2n-3)+p-2 gives nu_min>=n even though p does not divide e_n. The comparison is a whole potentially good height-two formal group versus an actual height-two group with two potentially good rank-one graded pieces, exactly within the manuscript monodromy condition. Their p^n truncations are isomorphic and their prime-to-p special characters differ. The finite extension is lifted by a complete Kummer/averaging cocycle construction. No upper bound or exact value at e=2(p-1) is claimed.'
for row in rows:
    if row['item']=='A.4' and powers3 and d2:
        row['status']='OPEN generally; every fixed nonordinary principal surface is classified in degree two and every power of three, and fixed elliptic products in every balanced degree'
        row['where']+='; lem:RD-A4-three-power-groups; lem:RD-A4-many-theta-graph; prop:RD-A4-three-step-boundary; thm:RD-A4-three-step; cor:RD-A4-powers-three; thm:every-nonordinary-ppav-degree-two-full-candidate'
        row['gate']=row['gate'].replace('The remaining fixed nonordinary NONPRODUCT principal-surface degrees are2 and every d>=4;', 'The new uniform multiplier-three induction proves GL_(9d²-1) for every d=3^j, j>=0, on every fixed nonordinary principal surface. Its complete proof uses only kernels killed by3, a universal many-theta graph lemma, uniform group-cohomology vanishing and exact Lang extension across rank drops. In degree2, for f=0 or1, the geometric and arithmetic image is Hom(F2^(1+f),F2^32) semidirect GL32, in relative rank33+f. Its32-dimensional common covector kernel is irreducible and lies in every nonzero invariant subspace. The proof uses exact curve-jet strata, lifted-node sum-zero wreath groups and the common six-theta graph; it includes every fixed nonproduct modulus. Thus the remaining fixed nonordinary NONPRODUCT principal-surface degrees are the even d>=4 and the odd d>=5 that are not powers of3;')
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md'; old=p.read_text(); body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 23 work: fixed degree three and primitive polarization reduction\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint23_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Post-CP22 promoted gates refreshed:',{'common_root':common,'restricted_Petri':petri,'allfixed_degree3':d3,'B62_lower_bounds':b62})
