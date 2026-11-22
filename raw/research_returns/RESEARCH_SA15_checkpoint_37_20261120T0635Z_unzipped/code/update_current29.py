"""Refresh CP29 gates from canonical audited proofs; keep auxiliary routes conditional."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current28.py')],cwd=w,check=True)
def proved(rel):
 p=w/rel
 return p.exists() and '\\status{Candidate' not in p.read_text() and '\\textup{[Candidate' not in p.read_text()
b79=proved('agents/reduction_descent/B_first_wild_irreducible_image.tex')
b80=proved('agents/reduction_descent/B_first_wild_fourth_layer.tex')
b81=proved('agents/reduction_descent/B_first_wild_Cartan_exclusion.tex')
thirteen=proved('agents/monodromy/nonordinary_uniform_thirteen_theta_geometry.tex')
routes=proved('sections/A_route_limitations_29.tex')
interpolation=proved('agents/obstructions_crystals/A4_product_Frobenius_interpolation.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
 if row['item']=='A.4':
  if thirteen:
   row['status']=('OPEN generally; every fixed f0 principal surface in all even degrees and odd degrees '
                  'divisible by3,5,7,11or13 plus degree1; fixed f1 odd multiples3 and even residues0,4mod6 plus2')
   row['where']+='; lem:uniform-thirteen-generic-fibres-candidate; lem:uniform-thirteen-generic-parameters-candidate; lem:uniform-thirteen-exceptional-map-candidate; thm:uniform-thirteen-nodal-self-isogeny-candidate; cor:f0-odd-multiples-thirteen-candidate'
   for old in ['The first remaining fixedf0 odd degree is13.','the least remaining fixed-f0 odd degree is13.']:
    row['gate']=row['gate'].replace(old,'The later uniform norm-thirteen theorem closes13; the first remaining fixed-f0 odd degree is17.')
   row['gate']+=(' The complete uniform norm-thirteen proof supplies an etale polarized self-isogeny '
                 'of multiplier13 on EVERY indecomposable f0 principal surface, whose theta image '
                 'has168 ordinary nodes. For mu^5!=1 the map3+2g is controlled by a separable '
                 'cubic fibre algebra and exact degree224/198 resultants. At mu^5=1 an explicitly '
                 'different three-unit map has everywhere full interpolation rank, an explicit '
                 'affine polynomial-combination certificate with coefficient gcd exactly l2^44, '
                 'and eight separated pole fibres. All remaining affine, infinity and repeated '
                 'residual-divisor cases are covered. The good-theta and cubic-component transfers '
                 'give GL_(9d²-1)(F2), geometrically and arithmetically, for every odd d divisible '
                 'by13. Together with the earlier results, fixed f0 is proved in degree1, '
                 'all even degrees, and all odd degrees divisible by3,5,7,11or13. '
                 'The least remaining fixed-f0 odd degree is17. Fixed-f1 odd5/even8 '
                 'and arbitraryX remain open.')
  if routes:
   row['where']+='; lem:root-full-radical-generation; prop:root-dual-kernel-differential; cor:root-dual-kernel-birational; ex:root-kernel-compression-countermodel'
   row['gate']+=(' The added full-radical generation and dual alternating-kernel lemmas are conditional tools only. '
                 'For higher-degree Cartier families the actual maximal differential rank and global generation '
                 'hypotheses remain unproved; an abstract compression countermodel prevents inferring them '
                 'from generic section rank alone. They do not change the exact-group cases already established.')
  if interpolation:
   row['where']+='; lem:DE-A4-product-Frobenius-interpolation; rem:DE-A4-product-Frobenius-interpolation-scope'
   row['gate']+=(' The critical two-point Frobenius interpolation shortcut is refuted on actual elliptic '
                 'products with line degree(3,3): the evaluation rank is7 when both coordinates differ '
                 'and6 when one agrees, so two evaluation functionals cannot produce rank8. '
                 'The rank for an arbitrary functional and larger point configurations remains unresolved.')
 if row['item']!='B.4':continue
 if b79:
  row['where']+='; lem:B-RD79-layers; prop:B-RD79-minimal; cor:B-RD79'
  row['status']+='; first-wild irreducible residual actualp³ image must have order at leastp⁴ for different characters'
  row['gate']+=(' B79 excludes the minimal wild orderp³ for an actual different-character p³-torsion '
                'comparison with irreducible residual inertia at e=p(p-1),p>=5. The exact common '
                'division-field valuations, pth-power inclusion W1 subset W2 and the entire terminal '
                'Cartan leading plane force incompatible scalar and Frobenius orientations. '
                'Thus the residual-irreducible branch requires wild orderp^r,4<=r<=8; '
                'atp5/e20 its actual125-torsion wild image has order at least625. '
                'This imposes no CM hypothesis and makes no existence assertion. Reducible residual '
                'comparisons and the unrestricted least index in{2,3} remain open.')
 if b80:
  row['where']+='; lem:B-RD80-first; prop:B-RD80-three-terminal; lem:B-RD80-plane; lem:B-RD80-orientation; thm:B-RD80'
  row['status']+='; wild orderp⁴ branch has full finite Cartan image'
  row['gate']+=(' B80 further narrows the orderp⁴ branch: the(1,3) layer shape is excluded for '
                'different characters, while the(2,2) shape has both layers equal to the original '
                'residual nonsplit Cartan. The actual wild group is(Z/p²)^2, the full third-level '
                'inertia image is abelian, and the module is free of rank one over the unramified '
                'quadratic algebra O_E/p³ with wild image exactly(1+p O_E)/(1+p³ O_E). '
                'The proof uses an actual lifted primitive vector for the split-Cartan stabilizer '
                'and fixed coefficients at both displacement levels. This is a finite-level '
                'quadratic action only: neither full-BT potential CM nor exclusion or existence '
                'of that branch follows. The actual finite Cartan branch, ordersp⁵ throughp⁸ '
                'and reducible residual inertia remain to be decided.')
 if b81:
  row['where']+='; lem:B-RD81-levels; prop:B-RD81-Cartan; cor:B-RD81'
  row['status']=row['status'].replace('at leastp⁴ for different characters','at leastp⁵ for different characters')
  row['status']=row['status'].replace('wild orderp⁴ branch has full finite Cartan image','actual wild ordersp³ andp⁴ excluded')
  row['gate']+=(' B81 subsequently EXCLUDES the actual finite Cartan branch left by B80. '
                'Surjectivity of the actual pth-power map gives every nonidentity terminal '
                'element break strictly above the minimum. Fixed coefficients at the two '
                'displacement levels exclude both sides of the critical break. At equality, '
                'the boundary coefficient is forced to be c_i z; its nonzero case gives the '
                'terminal Cartan contradiction and its zero case gives the first-layer '
                'Cartan contradiction. Thus any actual different-character p³ pair with '
                'irreducible residual inertia at e=p(p-1) requires wild orderp^r,5<=r<=8. '
                'Atp5/e20 the actual125-torsion wild image has order at least3125. '
                'This is an actual coefficient exclusion with no CM inference. The '
                'ordersp⁵ throughp⁸, reducible residual comparisons and the unrestricted '
                'least index in{2,3} remain open.')
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
marker='\n## Checkpoint 29 work: actual wild images and conditional monodromy routes\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint29_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP29 proved gates:',{'minimal_third_wild_image':b79,'fourth_wild_Cartan':b80,
 'fourth_wild_Cartan_excluded':b81,'uniform_thirteen':thirteen,
 'conditional_dual_kernel_routes':routes,'product_interpolation_obstruction':interpolation})
