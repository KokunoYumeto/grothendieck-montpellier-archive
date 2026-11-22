"""Refresh only proved CP19 gates and retain all actual historical reviews."""
from pathlib import Path
import subprocess,sys,json,re
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current18.py')],check=True,cwd=w)
def proved(relative):
    p=w/relative
    return p.exists() and '\\status{Candidate' not in p.read_text()
strip=proved('agents/monodromy/mixed_three_by_b_strip_groups.tex')
cm=proved('agents/reduction_descent/B_tame_CM_gate.tex')
cycle=proved('agents/reduction_descent/B_tame_residual_cycle.tex')
pencil=proved('agents/obstructions_crystals/A3_mixed_positive_index_pencil.tex')
d3=proved('agents/monodromy/mixed_degree_three_norm_groups.tex')
near=proved('agents/reduction_descent/B_tame_CM_neighborhood.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.3' and pencil:
        row['where']+='; lem:DE-A3-positive-pencil-contraction-candidate; cor:DE-A3-positive-first-rank-candidate'
        row['gate']+=' The positive-index determinant problem now has an exact curve-pencil model: on D, A=R0² is a degree-b basepoint-free pencil, the contraction cokernel is H1(D,A), and sharpness is equivalent to invertibility of cup product by the actual alpha2 torsor class beta on H0(D,A). At the etale double pullback, the full first Cartier rank is 2b-2-nullity(alpha cup), while the restricted first and stable ranks stay 2b-4. The cross Ext bundle is acyclic. This identifies the remaining variation map but does not prove its determinant nonzero or exclude either rank-one matrix ruling. The retained finite probe has total weight image dimension2, not3.'
    if row['item']=='A.4' and strip:
        row['where']+='; thm:mixed-three-by-b-full-groups-candidate; lem:mixed-strip-grid-candidate'
        row['gate']+=' Every mixed product of factor degrees(3,b), b>=3, now has exact full geometric=arithmetic images: GL_(3b-1)(F2) for oddb, and F2^(3b-2) semidirect GL_(3b-2)(F2) for evenb, the full stabilizer of the ordinary-factor trace covector. The proof handles the residual two-group quotient, the fixed-system translation cover, and regular trace/body kernels at the K3,b grid. Its special rank3b-3 is not identified with the generic rank3b-1. This strip result does not settle balanced(3d,3d) degreesd>=3.'
    if row['item']=='B.4' and cm:
        row['where']+='; thm:B-RD52; lem:B-RD52-CM; lem:B-RD52-LT'
        row['gate']+=' Within the potentially CM, potentially supersingular height-two formal subclass at e=p-1,p>=5, the least manuscript index is exactly1: p² torsion recovers the finite special character and an explicit CM twist pair shows failure atp. A nonsquare finite determinant forces unramified quadratic CM and an actual maximal-order lattice. The full first wild Lubin-Tate layer forces a p² intertwiner to centralize the quadratic residue field. Therefore every remaining unrestricted p² ambiguity must involve at least one non-CM formal model. The unrestricted index remains in{1,2}.'
    if row['item']=='B.4' and cycle:
        row['where']+='; lem:B-RD53-leading; prop:B-RD53-cycle; cor:B-RD53-quadratic'
        row['gate']+=' In the branch with irreducible residual inertia over Fp, every unequal-type comparison has joint tame degree p²-1 and its normalized special types are adjacent vertices of an explicit cycle of length(p+1)/2. Nonmaximal tame degrees require reducible residual inertia. For p congruent3 mod4, p>=7, opposite quadratic-twist types are excluded in this irreducible branch; for p congruent1 mod4 only one exchanged adjacent pair survives. At p5 the cycle is a triangle and yields no new pair exclusion. These necessary conditions do not construct a BT congruence or decide the unrestricted least index.'
    if row['item']=='A.4' and d3:
        row['where']+='; thm:mixed-every-fixed-modulus-degree-three-candidate; lem:mixed-d3-common-partial-normalizations-candidate'
        row['gate']+=' The next balanced fixed-modulus case d=3 is now also closed: every ordinary/supersingular elliptic pair has geometric=arithmetic GL80(F2). A cyclic three-isogeny norm of a sharp(3,9) source supplies an actual GL26 block, S54 node image and every translation into the53-dimensional graph heart. The729 partial normalizations of one full-rank target rule out any remaining graph subspace; no rank-drop specialization is used. The balanced fixed-modulus gate now starts at d=4, and higher odd degrees remain separate.'
    if row['item']=='B.4' and near:
        row['where']+='; lem:B-RD54-continuity; prop:B-RD54-neighborhood'
        row['gate']+=' The non-CM gate is further bounded in every normalized Honda framing: at least one parameter in a different-character p² pair satisfies0<v_L(x)<=4e_L. If both are deeper than4e, equivariant Hensel matching identifies their truncations with canonical CM shadows overK, and B52 excludes the pair. The continuity lemma holds at p^n whenv(x)>2n e_L. This leaves the explicit shallow parameter interval unresolved.'
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux));idmap={r['id']:r['label'] for r in root}
def location(t):
    return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in t.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table+='\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 19 work: mixed strips and the CM formal subclass\n'
if marker in body:body=body.split(marker)[0]
notes=w/'notes/checkpoint19_changes.md'
if notes.exists():body+=marker+'\n'+notes.read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Current CP19 proved gates refreshed:',{'mixed_strips':strip,'CM_subclass_exact_index':cm,'residual_cycle':cycle,'curve_pencil':pencil,'mixed_degree3':d3,'near_CM_exclusion':near})
