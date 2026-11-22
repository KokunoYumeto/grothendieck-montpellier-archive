"""Refresh current CP26 mathematical gates from promoted proofs only."""
from pathlib import Path
import json,re,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current25.py')],cwd=w,check=True)
def proved(rel):
    p=w/rel
    return p.exists() and '\\status{Candidate' not in p.read_text()
b69=proved('agents/reduction_descent/B_one_slope_quotient.tex')
b70=proved('agents/reduction_descent/B_next_tame_boundary.tex')
b71=proved('agents/reduction_descent/B_marked_quotient_sector.tex')
bad5=proved('agents/monodromy/nonordinary_rank_one_bad_five_kernel.tex')
seven=proved('agents/monodromy/nonordinary_uniform_seven_theta_geometry.tex')
rows=json.loads((w/'notes/item_status.json').read_text())
for row in rows:
    if row['item']=='A.4' and seven:
        row['status']=('OPEN generally; every fixed f0 principal surface at d=3^i5^j7^k and sums of two '
                       'such degrees; every fixed f1 principal surface at powers of3 and two-term sums')
        row['where']+=('; lem:uniform-seven-interpolation-candidate; '
                       'lem:uniform-seven-triple-obstruction-candidate; '
                       'lem:uniform-seven-parameter-certificate-candidate; '
                       'thm:uniform-seven-nodal-self-isogeny-candidate; '
                       'cor:f0-three-five-seven-degree-groups-candidate')
        old=('Every fixed f0 genus-two Jacobian has the separately proved nodal5-self-isogeny on the SAME '
             'surface. Combining it with the known3-power family gives, for all i,j>=0 and d=3^i5^j, '
             'geometric and arithmetic group GL_(9d²-1). For d=a+b with botha,b of that form, the '
             'group is F2^(9d²-4) semidirect GL_(9d²-4), in rank9d²-3. The smallest remaining f0 '
             'odd degree is7 and the smallest remaining even degree is22.')
        assert old in row['gate']
        row['gate']=row['gate'].replace(old,
            'Every fixed f0 genus-two Jacobian has proved nodal5- and7-self-isogenies on the SAME '
            'surface. Combining them with the known3-power family gives, for all i,j,k>=0 and '
            'd=3^i5^j7^k, geometric and arithmetic group GL_(9d²-1). For d=a+b with botha,b '
            'of that form, the group is F2^(9d²-4) semidirect GL_(9d²-4), in rank9d²-3. '
            'The exact bounded family census includes every even degree2 through90. The first '
            'remaining f0 odd degree is11 and the first remaining even degree is92.')
        old=('The retained degree7 quaternion interpolation is not a nodality proof and contributes no '
             'new unconditional degree without its missing triple-fibre exclusion.')
        assert old in row['gate']
        row['gate']=row['gate'].replace(old,
            'The universal norm7 quaternion interpolation now has its complete triple-fibre exclusion. '
            'It treats infinity, Z=0, conjugate points and both A(L) branches before the exact '
            'resultant calculation. The degree97 bad-r radical and its cubic-remainder gcd '
            'z³+z²+1 let one choose a good presentation of every fixed modulus. The resulting '
            'theta image has exactly48 nodes. This is a universal proof with exact identities, '
            'not an extrapolation from the retained finite-parameter explorations.')
    if row['item']=='A.4' and bad5:
        row['where']+='; prop:root-f1-bad-five-kernel; rem:root-f1-bad-five-kernel-scope'
        row['gate']+=(' The stronger claim that every five-kernel has nodal theta image is false '
                      'even at two-rank1: on y²+xy=x5+x3+x, the exact function with divisor '
                      '5P-5Q gives six maximal isotropic kernels identifying Q,P,iota(P). '
                      'This explicit counterexample does not settle the required existence '
                      'of a good incoming neighbour and closes no remaining degree.')
    if row['item']=='B.4' and b69:
        row['where']+=('; lem:B-RD69-rules; lem:B-RD69-quotients; prop:B-RD69-one-slope; '
                       'prop:B-RD69-two-slope; thm:B-RD69')
        row['status']=('OPEN generally; exact height-two initial tame sector and e=p²-1; '
                       'minimal cyclotomic index has value1')
        old=('The next unresolved five-adic height2 index is e20, which is divisible by5; '
             'the next unresolved five-prime index is e24. No value there, general ramification '
             'formula, or higher-height least-index classification is asserted.')
        assert old in row['gate']
        row['gate']=row['gate'].replace(old,'')
        row['gate']+=(
            ' The new actual one-slope rank-p quotient has unequal slopes with parameterB=e. '
            'Together with the common-point-field rules, this excludes mixed one-/two-slope '
            'actualp³ comparisons at everyp-prime ramification index. Equal one-slope '
            'characters are recovered either by B67 or by the actual scalar tame eigenvalue. '
            'The determinant-free two-slope argument gives the full filtered-monodromy '
            'p³ upper bound whenever(p-1)|e,p does not dividee,e<p². With the actual '
            'p² lower example this provesnu_min(p,p²-1,2)=2, including(5,24,2). '
            'The critical parameterB=e is expressly handled as a one-slope high quotient; '
            'it is never treated by an unequal-slope formula.')
        if b70:
            row['where']+=('; lem:B-RD70-high; lem:B-RD70-exchange; prop:B-RD70-tame; '
                           'prop:B-RD70-formal; thm:B-RD70')
            row['status']=('OPEN generally; exact height-two initial tame sector and '
                           'e=p²-1,(p+2)(p-1); minimal cyclotomic index has value1')
            row['gate']+=(
                ' A further complete proof givesnu_min(p,(p+2)(p-1),2)=2 for everyp>=5, '
                'including(5,28,2). The only new small-parameter congruence pair{1,p} '
                'exchanges the Frobenius-conjugate special eigenvalues. Tame exchanged '
                'high lines would force(p-1)|(B1+B2), which excludes the exceptional '
                'B1=B2=p² case. The common point-field inequality uses e<p³. '
                'The next unresolved five-prime ramification index is32; its compatible '
                'arithmetic pair{2,p+1} is not asserted to arise from any actual groups.')
        else:
            row['gate']+=' The next unresolved five-prime ramification index is28.'
        row['gate']+=(' The next unresolved five-adic index is still20, divisible by5. '
                      'Other exact ramification sectors and the higher-height least-index '
                      'classification remain open.')
        if b71:
            row['where']+=('; lem:B-RD71-first-level; lem:B-RD71-marked-low; '
                           'prop:B-RD71-separated-high; prop:B-RD71-common-high; '
                           'prop:B-RD71-tame; thm:B-RD71')
            row['status']=('OPEN generally; exact height-two index2 for e=t(p-1), '
                           '2<=t<=2p+1,p notdividingt; minimal cyclotomic index has value1')
            old=('The next unresolved five-prime ramification index is32; its compatible '
                 'arithmetic pair{2,p+1} is not asserted to arise from any actual groups.')
            assert old in row['gate']
            row['gate']=row['gate'].replace(old,
                'The later marked-quotient theorem also excludes the pair{2,p+1} by an '
                'actual second-quotient comparison, as explained below.')
            row['gate']+=(
                ' The full height-two exact sector is nownu_min(p,t(p-1),2)=2 for '
                '2<=t<=2p+1,p notdividingt,p>=5. The actual small high quotient carries '
                'a preserved stable low line, making its first-level module rational over '
                'the tame good field. A common degree-p² point-field inequality forces '
                'its high lines to correspond even when the residual action is scalar. '
                'A second actual quotient retains onlyp-torsion; the new first-level '
                'prime-parameter break lemma is exactly sufficient there. This adds '
                'the five-prime indices32,36,44. The first remaining five-prime index is48, '
                'at the general boundarye=2(p²-1), where the compatible small pair '
                '{1,2p-1} is retained as unexcluded arithmetic only. The five-divisible '
                'index20, further ramification sectors and higher heights remain open.')
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
marker='\n## Checkpoint 26 work: actual one-slope quotients and the next tame boundary\n'
if marker in body:body=body.split(marker)[0]
body+=marker+'\n'+(w/'notes/checkpoint26_changes.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body)
print('Refreshed CP26 proved gates:',{'uniform_seven':seven,'bad_five_counterexample':bad5,'one_slope_boundary':b69,'next_tame_boundary':b70,'marked_quotient_sector':b71})
