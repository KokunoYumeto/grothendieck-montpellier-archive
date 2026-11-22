"""Refresh CP28 gates from canonical audited proofs only."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current27.py')],cwd=w,check=True)
def proved(rel):
    p=w/rel
    return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
b75=proved('agents/reduction_descent/B_terminal_frobenius_pair.tex')
b76=proved('agents/reduction_descent/B_wild_cyclic_point.tex')
b77=proved('agents/reduction_descent/B_first_wild_finite_patterns.tex')
b78=proved('agents/reduction_descent/B_wild_CM_layer.tex')
eleven=proved('agents/monodromy/nonordinary_uniform_eleven_theta_geometry.tex')
twisted=proved('agents/obstructions_crystals/A3_mixed_positive_index_twisted_pencil.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.4' and eleven:
        row['status']=('OPEN generally; every fixed f0 principal surface in all even degrees '
                       'and odd degrees divisible by3,5,7or11; fixed f1 odd multiples3 '
                       'and even residues0,4mod6 plus2')
        row['where']+=('; lem:uniform-eleven-interpolation-candidate; '
                       'lem:uniform-eleven-quintic-fibres-candidate; '
                       'lem:uniform-eleven-good-parameters-candidate; '
                       'thm:uniform-eleven-nodal-self-isogeny-candidate; '
                       'cor:f0-odd-multiples-eleven-candidate')
        row['gate']=row['gate'].replace(
            'the first remaining f0 odd degree is still11.',
            'the then-remaining f0 odd degree11 is now closed by the later norm-eleven theorem.')
        row['gate']=row['gate'].replace(
            'The least remaining fixed-f0 odd degree is11.',
            'The later norm-eleven theorem closes degree11; the least remaining fixed-f0 odd degree is13.')
        row['gate']+=(
          ' The complete universal norm-eleven proof now supplies an etale polarized '
          'self-isogeny3+g+h of multiplier11 on EVERY indecomposable f0 surface, '
          'whose principal theta image has exactly120 nodes. Arbitrary-section '
          'interpolation excludes finite theta-kernel points, and a universally '
          'separable five-dimensional quotient algebra treats every finite '
          'fibre, includingZ0,A0,L0 and doubled residual divisors. Three exact '
          'resultants of degrees121104,3944,3540 and an explicit degree3354 '
          'parameter Bezout certificate guarantee a good presentation for every '
          'modulus, includingmu0. Both complete proof audits and full root '
          'resultant recomputation passed. Good-theta transfer and incoming '
          'sources followed by cubic-component transfer prove every odd '
          'degree divisible by11. Thus for complete systems|3dTheta| every '
          'fixedf0 surface is proved in all even degrees, degree1, and all '
          'odd degrees divisible by3,5,7or11. Odd image isGL_(9d²-1); '
          'even image is the previously proved full one-covector stabilizer. '
          'The first remaining fixedf0 odd degree is13. Fixedf1odd5/even8 '
          'and generalX remain open. The auxiliary single-class, triple-gluing '
          'and rational/residual route limitations do not themselves shrink this gate.')
    if row['item']=='A.3' and twisted:
        row['where']+='; lem:DE-A3-twisted-pencil-lift; rem:DE-A3-twisted-pencil-lift-scope'
        row['gate']+=(
          ' The intrinsic actual quotient also supplies a nonzero section '
          'sigma_G ofRP annihilated by gamma cup. Gorenstein curve duality '
          'and chi(AP)=0 giveh0(AG)=m+nullity(gamma cup onAP)>=m+1>=2, '
          'where m=h0(AP)=h0(RP); ifm1 the dimension is exactly2. '
          'This holds for nonreduced CartierD and requires no identification '
          'with an earlier norm section. The image of this compulsory domain '
          'and its actual direction restriction remain unresolved, so no '
          'generic-rank or main-gate advance is claimed.')
    if row['item']!='B.4': continue
    if b75:
        row['status']=('OPEN generally; exact height-two index2 iff p<e<p³ and exact index3 '
                       'on p³<e<p³(p+1), for p>=5,p not dividing e,mu_p in K; first wild comparisons narrowed')
        row['where']+='; lem:B-RD75-terminal; prop:B-RD75-formal; thm:B-RD75'
        row['gate']=(
          'Height1 has least manuscript index0. Atp3,e2,height2 the exact least index is2: '
          'actual27-torsion suffices and actual9-torsion ambiguity is sharp. Atp2,e1,height2 '
          'the exact least index is3:actual16-torsion suffices and actual8-torsion ambiguity '
          'is sharp; within the potentially supersingular elliptic subclass8 already suffices. '
          'Forp>=5,perfect residue,mu_p inK,height2,p not dividinge, the full filtered '
          'classification gives index1 ate=p-1 and index2 if and only ifp<e<p³. '
          'The independently proved arbitrary-index irreducible-residual and high-line '
          'recovery propositions remain available under their exact stated hypotheses. '
          'The actual lower construction givesnu_min(p,e,h)>=n forp>=5,h>=2,n>=2 '
          'and every permitted e>p^(2n-3), without an upper window. '
          'B74 givesnu_min<=n-1 whene<p^n,n>=3,p not dividinge; hence '
          'floor((k+3)/2)<=nu_min<=max(2,k) forp^k<e<p^(k+1),e>p. '
          'B75 strengthens the terminal whole-formal comparison to e<p^(n-1)(p+1),n>=3. '
          'The only unequal final parameters in1..p are1,p, and their special '
          'eigencharacters are Frobenius conjugate, so they define the same unordered '
          'character. This gives the FULL filtered boundnu_min<=n-1 for n>=4 '
          'and e<p^(n-1)(p+1); the n3 formal statement is not promoted to a full '
          'index2 bound. Combining the actual lower examples gives exactindex3 '
          'throughoutp³<e<p³(p+1). Forp5 all prime-to5 multiples of4 from128 '
          'through748 now have value3; at the next permitted e752 only3<=nu<=4 '
          'is proved. The abstract next terminal pair{2,p+1} has distinct orbits '
          'but is not a geometric counterexample. No exhaustive classification '
          'of index3 or higher-height formula is asserted.')
    if b76:
        row['where']+='; lem:B-RD76-point; prop:B-RD76-mixed; lem:B-RD76-determinant; cor:B-RD76'
        row['gate']+=(
          ' At arbitrary absolute ramification, B76 proves that a rational point of '
          'orderp^n,n>=2,on a good height2 formal group forces '
          'a>(p²-1)p^(2n-3-v_p(a)), with a the normalized valuation ofp. '
          'An actual mixed whole-formal versus two-height1 comparison therefore '
          'requires e>p^(2n-3-v_p(e)). In the full B4 setting, dimensions are '
          'detected whenn>=v_p(e)+2; if alsoe<=p^(2n-3-v_p(e)), only two '
          'whole potentially supersingular groups can remain. This closes the '
          'mixed branch atp5,e20,actual125-torsion. It alone gives no whole-formal '
          'recovery or exact least index there.')
    if b77:
        row['where']+='; lem:B-RD77-kernel; prop:B-RD77-square; cor:B-RD77'
        row['status']+=(
          '; at first wilde=p(p-1),least index is in{2,3}, with only nonsquare '
          'whole-formal actualp³ comparisons remaining')
        row['gate']+=(
          ' B77 proves2<=nu_min(p,p(p-1),2)<=3 for everyp>=5 in the full '
          'perfect-residue,mu_p setting. At actualp³, a common square finite '
          'determinant is excluded by an actual-target unweighted Cartier '
          'recurrence after the joint norm-one good degree m dividingp+1. '
          'The common nonsquare norm can be normalized to a primitive one. '
          'Atp5,e20, the only remaining distinct type pairs, up to simultaneous '
          'quadratic twist and interchange, are AB orAC, whereA={1,5}, '
          'B={9,21},C={13,17} are exponent pairs modulo24. Their joint faithful '
          'tame degree is24. Existence or impossibility of actual125-torsion '
          'congruence for those pairs is still open. General wild indices, '
          'the remaining larger tame exact intervals, and higher heights remain open.')
    if b78:
        row['where']+='; lem:B-RD78-model; lem:B-RD78-layer; prop:B-RD78-CM; thm:B-RD78'
        row['gate']+=(
          ' B78 further proves recovery for two nonsquare potentially CM '
          'whole-formal groups from actualp^n whenevern>=v_p(e)+2. The '
          'integral unramified quadratic model and an index bound on the '
          'actual LT division image preserve its full terminal wild layer. '
          'At first wilde=p(p-1), the restricted potentially-CM least index '
          'is exactly2: actualp³ recovers the character and an explicit '
          'fixed field in the LTp² division extension gives two actualCM '
          'twists with isomorphicp²-torsion and different special characters. '
          'Thus either remaining fullp5/e20 actual125 patternAB/AC must '
          'contain at least one non-CM model. The unrestricted index '
          'remains in{2,3}; it is not replaced by the restrictedCM answer.')
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',(w/'RESEARCH_SA15_paper.aux').read_text()))
idmap={r['id']:r['label'] for r in root}
def location(value):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in value.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text()
body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 28 work: norm eleven and wild ramification\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint28_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP28 proved gates:',{'terminal_Frobenius_pair':b75,'wild_cyclic_point':b76,'first_wild_finite_patterns':b77,'wild_CM':b78,'uniform_eleven':eleven,'twisted_pencil_domain':twisted})
