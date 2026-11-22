"""Track post-CP21 promoted gates, retaining earlier snapshots as historical records."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current21.py')],check=True,cwd=w)
def proved(rel):
    p=w/rel;return p.exists() and '\\status{Candidate' not in p.read_text()
degree1=proved('agents/monodromy/p_rank_one_ppav_degree_one_groups.tex')
b59=proved('agents/reduction_descent/B_tame_full_wild_quadratic.tex')
monad=proved('agents/obstructions_crystals/A3_mixed_positive_index_monad.tex')
b61=proved('agents/reduction_descent/B_tame_reducible_recovery.tex')
oddblock=proved('agents/monodromy/nonordinary_ppav_odd_natural_blocks.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.3' and monad:
        row['where']+='; lem:DE-A3-positive-monad-note; lem:DE-A3-positive-monad-variation-note; rem:DE-A3-positive-monad-gate-note'
        row['gate']+=' The audited symplectic monad identifies the exact tangent map as Psi_s:Delta_s->Hom(H1(Q-dual),H1(Q)), dot(w)->H1(dot(w)J_Q), where Delta_s is the actual determinant-variation image. The sufficient missing condition is dim(im(Psi_s))>=2. This equivalent description gives no new lower bound and is not separately counted as movement.'
    if row['item']=='A.4' and degree1:
        row['where']+='; thm:nonordinary-ppav-polar-stable-conditional-candidate; thm:p-rank-zero-ppav-degree-one-full-candidate; thm:every-nonordinary-ppav-degree-one-full-candidate'
        marker='On every nonordinary principal surface in characteristic two, degree-one geometric monodromy now contains'
        if marker in row['gate']:row['gate']=row['gate'].split(marker)[0]
        row['gate']=row['gate'].replace('Fixed nongeneric nonordinary nonproduct ppav surfaces and the structural classification for arbitrary X remain open. ', '')
        row['gate']+='For every fixed nonordinary principally polarized abelian surface over every perfect field of characteristic two, the smooth maximal-rank locus in |3Theta| has relative unit rank8 and both geometric and arithmetic images GL8(F2). This includes every nonproduct surface of p-rank0 or1, with no generic-modulus hypothesis. The actual Cartier cubic is the Coble cubic of the Frobenius-twisted surface. The polar-Lang criterion excludes every extra rank-six component once its polar tensor is stable. Exact normal forms for all p-rank0 and1 genus-two curves, together with polynomial 81-by-81 minors equal to1 and b^4 (b!=0), establish that stability uniformly. Connected nonzero Lang cover plus the full root subgroup gives all elementary matrices. The remaining fixed nonordinary nonproduct principal-surface gate is degree>=2. The general structural classification for arbitrary X remains open; no higher-degree transfer by positive-defect padding or specialization is asserted.'
        row['status']='OPEN generally; every fixed nonordinary principal surface is classified in degree one, and fixed elliptic products in every balanced degree'
        if oddblock:
            row['where']+='; lem:nonordinary-ppav-odd-sharp-norm-candidate; thm:nonordinary-ppav-odd-natural-block-candidate'
            row['gate']+=' In every odd degree d, a pure polarized isogeny norm of a degree-one curve has exactly9(d squared minus1) nodes and attains the target maximal rank. Its node action has order prime to31, so Goursat and the proved natural-module H1 vanishing supply an actual eight-dimensional GL8 block fixing a complement in the geometric image. This is a uniform subgroup theorem; the full higher-degree representation still needs irreducibility and gluing arguments.'
    if row['item']=='B.4' and b59:
        row['where']+='; lem:B-RD58-final-Cartan; thm:B-RD58; thm:B-RD59'
        marker='In the branch with irreducible residual inertia over Fp,'
        if marker in row['gate']:row['gate']=row['gate'].split(marker)[0]
        row['gate']+='The entire irreducible-residual branch is now excluded from every unequal-character p² comparison at p>=5,e=p-1,height2. B55/B57 exclude wild image orders p² and p³. For the full p⁴ image, point fields and the cyclotomic determinant quotient have the same single upper break; upper quotient compatibility forces the final lower group to be the full Cartan plane. B58 treats irreducible anti-Cartan action, and B59 treats both one-break and two-break anti-Cartan patterns at projective order2, retaining the general additive X^p coefficient. The last Cartan coefficient is scalar-linear in both models, contrary to their required Frobenius-semilinear orientation. Thus any remaining unequal-character p² pair must have reducible residual inertia over Fp. It must still involve at least one non-CM model and, in a normalized Honda framing, at least one parameter with0<v_L(x)<=4e_L. The unrestricted least index remains in{1,2}, including atp5; no remaining pair is constructed.'
    if row['item']=='B.4' and b61:
        row['where']+='; lem:B-RD60-break; lem:B-RD60-Newton; prop:B-RD60-residual-break; lem:B-RD61-point-field; prop:B-RD61-wild; prop:B-RD61-tame; thm:B-RD61'
        marker='For every p>=5 at e=p-1 and height2,'
        assert marker in row['gate']
        row['gate']=row['gate'].split(marker)[0]
        row['gate']+='For every p>=5, height2 and minimal cyclotomic ramification e=p-1 with mu_p contained in K, the exact least manuscript index is now1: actual p-squared torsion determines the special prime-to-p inertia character, and the earlier actual p-torsion counterexample proves sharpness. This includes all non-CM deformations and both irreducible and reducible residual inertia. The nonsquare-determinant reducible branch has a canonical high line and exact Newton valuations alpha=p squared-1-B, beta=B/p. In the mixed-divisibility wild case the first break forces B_nondivisible>B_divisible; the actual common elementary-abelian p-squared point field gives the opposite inequality. The tame case forces equal low slopes and equal high lines. The general least-index formula at other ramification indices or heights remains open. No remaining ambiguity is asserted in the now closed minimal-ramification height-two case.'
        row['status']='OPEN generally; exact height-two least indices at every minimal cyclotomic ramification prime, including all p>=5'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text());aux=(w/'RESEARCH_SA15_paper.aux').read_text();nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):];marker='\n## Checkpoint 22 work: every fixed nonordinary degree-one surface\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint22_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Post-CP21 promoted gates refreshed:',{'every_nonordinary_degree1':degree1,'all_irreducible_residual_comparisons':b59,'equivalent_positive_index_monad':monad,'all_p_minimal_height_two_exact':b61,'all_odd_nonordinary_GL8_blocks':oddblock})
