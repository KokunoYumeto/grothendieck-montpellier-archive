"""Refresh CP25 proved gates only; historical archives and reviews are immutable."""
from pathlib import Path
import json, re, subprocess, sys
w = Path(__file__).resolve().parents[1]
subprocess.run([sys.executable, str(w / 'code/update_current24.py')], check=True, cwd=w)
def proved(rel):
    p = w / rel
    return p.exists() and '\\status{Candidate' not in p.read_text()
rows = json.loads((w / 'notes/item_status.json').read_text())
for row in rows:
    if row['item'] == 'A.3' and proved('agents/obstructions_crystals/A3_mixed_positive_index_residual_boundary.tex'):
        row['where'] += '; lem:DE-A3-residual-pencil-boundary; cor:DE-A3-residual-pencil-restriction'
        row['gate'] += (' The residual-pencil map is now identified exactly: for E=Q-dual, G=g-dual and '
                        'R=omega_D tensor A^-1, the symmetric-square resolution '
                        '0->(LP)^-1->E tensor G->Sym²G->i_*(R²)->0 gives the actual cup-wedge map '
                        'as its two-step boundary after multiplication Sym²H0(R)->H0(R²). '
                        'For integral D the multiplication image W_s has dimension3. The remaining '
                        'gate is its boundary followed by restriction to the actual Delta_s. '
                        'No nonvanishing or variation-image lower bound follows from this identification; '
                        'the twist by P and the boundary kernel remain essential.')
    if row['item'] == 'A.4' and proved('agents/monodromy/nonordinary_good_theta_norm_transfer.tex'):
        row['status'] = ('OPEN generally; every fixed f0 principal surface at d=3^i5^j and sums of two '
                         'such degrees; every fixed f1 principal surface at powers of3 and two-term sums')
        row['where'] += ('; lem:good-theta-uniform-node-product-candidate; prop:good-theta-uniform-gluing-candidate; '
                         'thm:good-theta-odd-norm-step-candidate; cor:f0-three-five-degree-groups-candidate')
        row['gate'] = (
            'The projective-space cases, every fixed balanced elliptic product, and the proved eventual '
            'ordinary-principal-surface range retain their complete group descriptions. On a fixed '
            'nonordinary principal surface in characteristic2, write L=3Theta and f for its two-rank. '
            'The exact odd-degree covector theorem, rank formula and generic-stratum full-image theorem '
            'are proved. Whenever an etale polarized odd isogeny B->A of multipliern has an integral '
            'nodal individual theta image, full GL_(m²-1) for |mTheta_B|, m=3e odd, transfers to full '
            'GL_(n²m²-1) for |mnTheta_A|. This arbitrary-odd good-theta transfer is now complete: '
            'the finite four-value exceptional set gives2-transitivity; isolated theta-boundary collisions '
            'give supported transpositions and the full node permutation product; actual natural blocks, '
            'normal Lang extension, all kernel shifts and transvection generation give the full group. '
            'No full stable-fibre identification across a rank drop is assumed. '
            'Every fixed f0 genus-two Jacobian has the separately proved nodal5-self-isogeny on the SAME '
            'surface. Combining it with the known3-power family gives, for all i,j>=0 and d=3^i5^j, '
            'geometric and arithmetic group GL_(9d²-1). For d=a+b with botha,b of that form, the '
            'group is F2^(9d²-4) semidirect GL_(9d²-4), in rank9d²-3. The smallest remaining f0 '
            'odd degree is7 and the smallest remaining even degree is22. '
            'For each fixed f1 principal surface the proved odd degrees are3^i, and the proved even '
            'degrees are3^i+3^j. The even group is Hom(F2²,F2^(9d²-4)) semidirect GL_(9d²-4), '
            'in rank9d²-2. The smallest remaining f1 degrees are5 and8. A suitable incoming '
            'nodal5-neighbour for every such fixed surface remains unproved. '
            'Every fixed supersingular or mixed elliptic product has the corresponding exact odd/even '
            'groups in every balanced degree, and the prior mixed-strip results remain proved. In '
            'each even group the common covector kernel is irreducible and contained in every nonzero '
            'invariant subspace. Geometrically generic nonordinary ppav strata are classified in every '
            'degree, and any finite prescribed degree set has a common nonempty open and finite-field '
            'examples. The explicit F16 five-kernel census and its20 nodal self-isogeny kernels remain '
            'separately verified. Arbitrary fixed nonproduct degrees outside the families above and '
            'the structural classification for generalX stay open. '
            'The retained degree7 quaternion interpolation is not a nodality proof and contributes no '
            'new unconditional degree without its missing triple-fibre exclusion.'
        )
        if proved('agents/monodromy/nonordinary_odd_theta_nodality_reduction.tex'):
            row['where'] += '; lem:root-nonordinary-odd-theta-nodality'
            row['gate'] += (' For f<=1 and any odd kernel, a tangency forces a three-point fibre through '
                            'a Weierstrass representative of geometric2-torsion. Thus excluding '
                            'three-point fibres suffices for nodality; existence of the incoming '
                            'isogeny is still required.')
    if row['item'] == 'B.4' and proved('agents/reduction_descent/B_initial_tame_sector.tex'):
        row['status'] = ('OPEN generally; exact height-two index2 at every e=t(p-1),2<=t<=p-1,p>=5; '
                         'minimal cyclotomic index has value1')
        row['where'] += ('; lem:B-RD66-rules; lem:B-RD66-quotients; prop:B-RD66-nonsquare; thm:B-RD66; '
                         'lem:B-RD67-normalization; lem:B-RD67-small-wild; lem:B-RD67-final-plane; '
                         'lem:B-RD67-full-wild; thm:B-RD67; lem:B-RD68-rules; lem:B-RD68-quotients; '
                         'prop:B-RD68-nonsquare; lem:B-RD68-square; thm:B-RD68')
        row['gate'] = (
            'Height1 has least manuscript index0. Atp3,e2,height2 the exact least index is2: '
            '27-torsion determines the prime-to-three special inertia character and the actual9-torsion '
            'counterexample is sharp. Atp2,e1,height2 the exact least index is3:16-torsion suffices '
            'and actual8-torsion ambiguity is sharp; within the potentially supersingular elliptic '
            'subclass8 already suffices. All residual branches and marked congruence models remain proved. '
            'For everyp>=5 withmu_p inK, perfect residue field andheight2, the exact least index at '
            'e=p-1 is1, including non-CM and reducible/irreducible residual cases. '
            'For everye=t(p-1) with2<=t<=p-1, the exact least index is now2. Actualp³-torsion '
            'always determines the requested character in the FULL filtered monodromy setting, '
            'whereas actualp²-torsion does not uniformly determine it. This includes(5,8),(5,12), '
            '(5,16), and the independently proved middle indexe=(p²-1)/2 for allp>=5. '
            'The new irreducible-residual theorem already recovers whole-formal special characters '
            'from actualp²-torsion at ANYp-prime ramification index. Its proof explicitly treats '
            'all wild image dimensions2,3,4 using actual common point fields, both ramification '
            'numberings, integral Honda coordinates and arbitrary additive root polynomials with '
            'their middle terms. Reducible residual comparisons in the initial sector use '
            'the actual high/low cyclic quotient transformations B->pB or s-B, andB->B/p. '
            'They preserve the special Frobenius orbit and convert a line-preservingp³ comparison '
            'to an actualp² quotient comparison. Square determinants use the closed logarithm '
            'and integral Cartier saturation bound on the ACTUAL quotient target, never an '
            'unjustified transfer of source coefficient thickness. '
            'The exact cyclic threshold givesnu_min(p,e,h)>=n forp>=5,h>=2,n>=2 and every '
            'multiplee ofp-1 with e>p^(2n-3), without an upper window. Ifp does not dividee, '
            'that strict inequality is also necessary for an actualp^n comparison between a '
            'whole potentially supersingular height2 group and a height2 system filtered by '
            'two potentially good height1 groups. The lower examples retain their complete '
            'Eisenstein tame-equivariant arc and Kummer/averaging extension construction. '
            'The next unresolved five-adic height2 index is e20, which is divisible by5; '
            'the next unresolved five-prime index is e24. No value there, general ramification '
            'formula, or higher-height least-index classification is asserted.'
        )
(w / 'notes/item_status.json').write_text(json.dumps(rows, indent=2) + '\n')
root = json.loads((w / 'notes/root_results.json').read_text())
aux = (w / 'RESEARCH_SA15_paper.aux').read_text()
nums = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux))
idmap = {row['id']: row['label'] for row in root}
def location(value):
    return '; '.join(x + (f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '')
                     for x in value.split('; '))
table = '| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'
table += '\n'.join('| ' + ' | '.join([r['item'], r['status'], location(r['where']), r['gate']]) + ' |'
                   for r in rows) + '\n'
(w / 'notes/current_outcome_table.md').write_text(table)
p = w / 'RESEARCH_SA15_report.md'
old = p.read_text()
body = old[old.index('# RESEARCH_SA15 research report'):]
marker = '\n## Checkpoint 25 work: odd norm transfer and the initial tame sector\n'
if marker in body:
    body = body.split(marker)[0]
body += marker + '\n' + (w / 'notes/checkpoint25_changes.md').read_text()
p.write_text('INCOMPLETE\n\n' + table + '\n' + body)
print('Refreshed CP25 gates from separately promoted canonical proofs.')
