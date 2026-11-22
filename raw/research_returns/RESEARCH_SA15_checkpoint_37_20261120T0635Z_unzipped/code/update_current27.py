"""Refresh CP27 gates using only canonical independently audited proofs."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current26.py')],cwd=w,check=True)
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
b72=proved('agents/reduction_descent/B_first_level_mixed_boundary.tex')
b73=proved('agents/reduction_descent/B_rational_high_line.tex')
unipotent=proved('agents/obstructions_crystals/A3_mixed_positive_index_unipotent.tex')
boundary=proved('agents/obstructions_crystals/A3_mixed_positive_index_boundary_kernel.tex')
nine=proved('agents/monodromy/nonordinary_nine_theta_norm_transfer.tex')
neighbors=proved('agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex')
uniform=proved('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex')
b74=proved('agents/reduction_descent/B_iterated_high_quotient.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']=='A.4' and nine:
  row['status']=('OPEN generally; every fixed f0 principal surface in all even degrees '
                 'and odd degrees divisible by3, plus the proved3/5/7 family; '
                 'fixed f1 powers of3 and their two-term sums')
  row['where']+=('; lem:nine-theta-clean-cubic-contacts-candidate; '
                 'lem:nine-theta-node-product-candidate; '
                 'lem:nine-theta-weighted-graph-candidate; '
                 'prop:nine-theta-full-gluing-candidate; '
                 'thm:nine-theta-arbitrary-odd-norm-candidate; '
                 'cor:f0-all-even-nine-theta-transfer-candidate')
  old=('The exact bounded family census includes every even degree2 through90. The first '
       'remaining f0 odd degree is11 and the first remaining even degree is92.')
  assert old in row['gate']
  row['gate']=row['gate'].replace(old,
      'The earlier exact bounded family census included every even degree2 through90. '
      'The later nine-theta transfer now closes every remaining f0 even degree; '
      'the first remaining f0 odd degree is still11.')
  row['gate']+=(' The complete nine-theta transfer works through ANY odd polarized '
       'isogeny with indecomposable nonordinary source, without principal-theta '
       'nodality. Three movable cubic components give clean isolated contacts; '
       'their162-node type permutations and exact eighteen-label graph lifts '
       'force every translation heart. The normal Lang torsor splitting extends '
       'across the explicitly retained boundary rank drop. The resulting target '
       'group isGL_(81n²-1) in degree3n. Quaternion endomorphisms and the complete '
       'four-squares descent give every odd multiplier on the SAME fixed f0 '
       'Jacobian. Thus every odd degree divisible by3 is proved, and even '
       'addition with degrees1 and5 proves every even degree, with group '
       'F2^(9d²-4) semidirectGL_(9d²-4) in relative rank9d²-3. These geometric '
       'and arithmetic groups are exact. Remaining odd fixed-f0 degrees and '
       'the fixed-f1 degree5 gate remain open; no all-degree conclusion is made.')
 if row['item']=='A.4' and neighbors:
  row['status']=('OPEN generally; every fixed nonordinary principal surface in '
                 'odd degrees divisible by3; all f0 even degrees; f1 even degrees '
                 '0 or4mod6 and2; additional proved f0 odd3/5/7 family')
  row['where']+=('; lem:nonordinary-mixed-principal-complement-candidate; '
                 'thm:nonordinary-arbitrary-odd-neighbor-candidate; '
                 'cor:nonordinary-all-odd-multiples-three-candidate')
  row['gate']+=(' A full scheme-theoretic connected-complement proof now gives '
       'an indecomposable incoming source of every odd multiplier for EVERY '
       'fixed nonordinary principal surface. In f1, the unique ordinary and '
       'supersingular elliptic subvarieties have the same principal degree d; '
       'a product prime-ell quotient forces d=ell and the unique possible '
       'kernelEo[ell]=Es[ell]. Another isotropic subgroup is available. In f0, '
       'Cartier rank excludes every product odd quotient. Iteration and '
       'polarized duality give the required incoming direction. Consequently '
       'all fixed-f1 odd degrees divisible by3 and even degrees0or4mod6 are '
       'now proved, as is the separate degree2 base. The exact f1 even group '
       'isHom(F2²,F2^(9d²-4)) semidirectGL_(9d²-4), with pointwise arithmetic '
       'covector descent. Fixed-f1degree5 and degree8, and the remaining '
       'even2mod6 class, remain open.')
 if row['item']=='A.4' and uniform:
  row['status']=('OPEN generally; every fixed f0 principal surface in all even '
                 'degrees and odd degrees divisible by3,5or7; every fixed f1 '
                 'surface in odd degrees divisible by3 and even degrees0or4mod6, plus2')
  row['where']+=('; lem:cubic-component-clean-node-product-candidate; '
                 'prop:cubic-component-weighted-graph-gluing-candidate; '
                 'thm:cubic-component-arbitrary-odd-norm-transfer-candidate; '
                 'cor:f0-odd-multiples-three-five-seven-candidate')
  row['gate']+=(' The complete uniform e-component transfer now works for every '
       'odd source degree e>=3 with known full image, through any odd polarized '
       'isogeny of multiplier n with indecomposable nonordinary source. Its '
       'e movable cubic components give18e² nodes per type and a vertex star '
       'with36(e-1) ones and18e²-36(e-1) zeros. Exact pure graph lifts and '
       'the finite-Lang extension argument give the full targetGL_(9e²n²-1). '
       'Applying the uniform source degrees3,5,7 and the incoming-neighbour '
       'theorem proves every fixed-f0 odd degree divisible by at least one '
       'of3,5,7. The least remaining fixed-f0 odd degree is11. The source '
       'degree1 case and fixed-f1degree5/even8 are not proved.')
 if row['item']=='B.4' and b72:
  row['status']=('OPEN generally; exact height-two index2 for e=t(p-1), '
                 '2<=t<=2p+2, p not dividing t; minimal cyclotomic index has value1')
  row['where']+=('; lem:B-RD72-first-mixed; prop:B-RD72-mixed-quotients; '
                 'prop:B-RD72-common-high; prop:B-RD72-formal; thm:B-RD72')
  old=('The first remaining five-prime index is48, '
       'at the general boundarye=2(p²-1), where the compatible small pair '
       '{1,2p-1} is retained as unexcluded arithmetic only.')
  assert old in row['gate']
  row['gate']=row['gate'].replace(old,
      'The later B72 boundary theorem excludes the pair{1,2p-1} by the '
      'strict first-level mixed-break comparison after two actual quotients.')
  row['gate']+=(' B72 proves nu_min(p,2(p²-1),2)=2 for every p>=5. '
       'The first actual quotient preserves the marked low line; its nonscalar '
       'tame eigenvalues identify the high lines. The second actual quotient '
       'retains precisely p-torsion. Its parameters p³ and3p²-2p-2 violate '
       'the necessary strict prime-versus-divisible ordering. This extends '
       'the exact sector to2<=t<=2p+2, p not dividing t, adding p5/e48. '
       'The next remaining five-prime index is52. The five-divisible index20 '
       'and the general higher-height classification remain open.')
 if row['item']=='B.4' and b73:
  row['status']=('OPEN generally; exact height-two index2 iff p<e<p³ for '
                 'p>=5, p not dividing e, mu_p in K; minimal index has value1')
  row['where']+=('; lem:B-RD73-high-branch; prop:B-RD73-high-recovery; '
                 'lem:B-RD73-common-high; prop:B-RD73-formal; thm:B-RD73')
  row['gate']=row['gate'].replace('The next remaining five-prime index is52.',
       'The later rational-high-line theorem settles every remaining '
       'five-prime index below125, including52.')
  row['gate']+=(' The exact full height-two index-two classification is now '
       'nu_min(p,e,2)=2 iff p<e<p³, for p>=5, p not dividing e and mu_p in K. '
       'Equivalently e=t(p-1), 2<=t<=p²+p+1, p not dividing t. Actual '
       'L-rational first-level torsion allows its high line to be recovered '
       'from the next torsion level at arbitrary e, using a degree-p or '
       'degree-p² point-field break. Two actual high quotients then leave '
       'exactly p-torsion; tame/wild opposition and the interval1..p-1 '
       'exhaust the remaining comparisons belowp³. The known actual lower '
       'examples give index1 at e=p-1 and index>=3 for permitted e>p³. '
       'For p5 all prime-to5 multiples of4 from8 through124 have index2; '
       'at e128 the least index is at least3. Its exact value, the '
       'five-divisible index20, arbitrary higher indices and higher '
       'heights remain open at this stage.')
 if row['item']=='B.4' and b74:
  row['status']=('OPEN generally; exact height-two index2 iff p<e<p³ and '
                 'exact index3 on p³<e<p⁴, with proved larger-index bounds '
                 'for p>=5, p not dividing e, mu_p in K')
  row['where']+=('; lem:B-RD74-actual-levels; prop:B-RD74-formal; '
                 'thm:B-RD74-upper; cor:B-RD74-third-index')
  row['gate']=row['gate'].replace(
       'at e128 the least index is at least3. Its exact value, the '
       'five-divisible index20, arbitrary higher indices and higher '
       'heights remain open at this stage.',
       'at e128 the least index is exactly3 by the later B74 induction. '
       'The five-divisible index20 and higher heights remain open.')
  row['gate']+=(' The full actual-quotient induction proves nu_min<=n-1 '
       'whenever e<p^n and n>=3 under the same prime-to-p height-two '
       'hypotheses. The jth quotient retains actual p^(n-j)-torsion, '
       'so high-line alignment uses a real available second level and the '
       'last comparison only p-torsion. With p^k<e<p^(k+1), e>p, '
       'floor((k+3)/2)<=nu_min<=max(2,k). In particular nu_min=3 '
       'throughout p³<e<p⁴. For p5 this settles all prime-to5 multiples '
       'of4 from128 through624. At the next permitted e628 only3<=nu<=4 '
       'is proved here. This interval is not claimed to classify every '
       'instance of index3, and no p-divisible or higher-height case is inferred.')
 if row['item']=='A.3' and unipotent and boundary:
  row['where']+=('; lem:DE-A3-primitive-unipotent; '
                 'lem:DE-A3-unipotent-Frobenius; '
                 'lem:DE-A3-residual-boundary-kernel')
  row['gate']+=(' The actual quotient bundle in the primitive mixed case is '
       'now explicitly a nonsplit extension ofO byO with Frobenius-killed '
       'class; positive actual local index gives the split extension. '
       'Its symmetric square has cohomology(2,4,2), or(3,6,3) in the split '
       'case. The exact residual-boundary kernel retains the additional '
       'twisted-pencil contribution H0(D,AG), which is nonzero. These are '
       'proved auxiliary reductions only; they do not establish '
       'dim imPsi_s>=2 or close the primitive mixed rank gate.')
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
marker='\n## Checkpoint 27 work: actual quotient recovery and monodromy geometry\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint27_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP27 proved gates:',{'mixed_boundary':b72,'rational_high_line':b73,'unipotent_bundle':unipotent,'boundary_kernel':boundary,'nine_theta_transfer':nine,'arbitrary_odd_neighbors':neighbors,'uniform_cubic_transfer':uniform,'iterated_high_quotients':b74})
