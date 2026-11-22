"""N017: exact globalization of the minimal two-dimensional rank-four block.

Two explicit label-order repairs are tested in the actual unsaturated
Q[D] order.  The product order succeeds on all four bitableaux; a
row-first total refinement fails at its fourth stage.  These are variants
of VIII's printed prescription, which N012/N014 show needs amendment.

The finite procedure is the all-degree cutoff of N016, implemented with
triangular polynomial arithmetic.  Full-domain uniqueness includes the
odd delta*Q[D] summand, not merely the beta-even polynomial order.
"""
from pathlib import Path
import gzip,json,time
from flint import fmpq,fmpq_poly
from bar_fixed_first_stages import parse,vector,sp,sv,decide,length
from bar_fixed_gt_stages import Rational,exact,linear_combine,bounded_coefficients,odd_dimension

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def solve_stage(H,ambient,den,lower_scalings,keys,order='factor_product'):
    """H is triangular, with the current coordinate first.

    lower_scalings[i-1] is the exponent attached to coordinate i.
    Coefficients of a vector in the actual module are polynomials in
    its H rows.  The primitive current-line coefficient u is the lcm
    of the reduced denominators of the rational cancellation vector.
    Reducing the first row coefficient modulo u gives a finite exact
    complement.  Necessary bounds on subsequent row coefficients are
    obtained inductively from triangularity, and then all degree-cap
    equations are imposed; no saturation or sample degree is used.
    """
    k=len(H);assert len(lower_scalings)==k-1
    rational=[Rational(ONE)]
    for i in range(1,k):
        a=Rational()
        for j in range(i):a=a.add(rational[j].times(H[j].get(i,ZERO)))
        rational.append(a.times(-ONE).divide(H[i][i]))
    u=ONE
    for r in rational:u=exact(u*r.q,u.gcd(r.q))
    coefficients=[r.p*exact(u,r.q) for r in rational]
    assert coefficients[0]==u
    g=ZERO
    for c in coefficients:g=g.gcd(c)
    assert g.degree()==0
    assert all(not sum((coefficients[j]*H[j].get(i,ZERO) for j in range(i+1)),ZERO)
               for i in range(1,k))
    t=linear_combine(coefficients,ambient);tn=u*H[0][0]
    scale=den[0].leading_coefficient()/tn.leading_coefficient()
    t={j:p*scale for j,p in t.items()};tn*=scale
    coefficients=[p*scale for p in coefficients]
    caps=[None]+[-a-1+den[i+1].degree() for i,a in enumerate(lower_scalings)]
    complement=bounded_coefficients(H,ambient,caps,current_bound=u.degree()-1)
    ys,yn=complement['vectors'],complement['top_numerators']
    B=max([0]+[p.degree()-t[z].degree() for y in ys for z,p in y.items() if z in t])
    space=ys+[{z:p*D**i for z,p in t.items()} for i in range(B+1)]
    top=yn+[tn*D**i for i in range(B+1)]
    row_combinations=complement['coefficients']+[[p*D**i for p in coefficients] for i in range(B+1)]
    answer=decide(space,top,den[0],keys,ambient_order=order)
    answer.update({'primitive_kernel_first_coefficient':sp(u),
                   'kernel_row_coefficients':[sp(p) for p in coefficients],
                   'finite_complement_coefficient_bounds':complement['coefficient_bounds'],
                   'finite_complement_parameter_count':complement['variables'],
                   'finite_complement_row_coefficients':[[sp(p) for p in c] for c in complement['coefficients']],
                   'finite_quotient_dimension':len(ys),'cutoff_B':B,
                   'finite_space_dimension':len(space),'basis_vectors':[sv(v) for v in space],
                   'top_numerators':[sp(p) for p in top],'top_denominator':sp(den[0])})
    def row_coefficients(point):
        return [sp(sum((fmpq(c)*a[i] for c,a in zip(point['coefficient_vector'],row_combinations)),ZERO))
                for i in range(k)]
    answer['lexicographic_candidate']['actual_row_coefficients']=row_coefficients(answer['lexicographic_candidate'])
    if answer['partial_order_failure_witness'] is not None:
        answer['partial_order_failure_witness']['actual_row_coefficients']=row_coefficients(answer['partial_order_failure_witness'])
    if answer['global_minimum_exists']:
        odd=odd_dimension(H,ambient,den,list(reversed(lower_scalings)),answer['lexicographic_profile'])
        full=answer['lexicographic_minimizing_dimension']+odd
        answer.update({'odd_minimizing_dimension':odd,'full_bar_fixed_minimizing_dimension':full,
                       'unique_in_full_bar_fixed_domain':full==1})
    return answer


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    all_ambient=[vector(r['ambient_coordinates']) for r in data['rows']]
    all_GT=[vector(r['gt_numerators']) for r in data['rows']]
    all_den=[parse(p) for p in data['coordinate_denominators']]
    keys=[(tuple(a),tuple(b)) for a,b in data['ambient_coordinates']]
    # Actual last four Hermite rows form B_S intersect the Sprime22 block.
    assert all(data['coordinate_labels'][i]['module']=='Sprime22' for i in range(110,114))
    assert all(not set(all_GT[i])-set(range(110,114)) for i in range(110,114))
    product_sets=[[113],[112,113],[111,113],[110,111,112,113]]
    total_sets=[[113],[112,113],[111,112,113],[110,111,112,113]]
    results={}
    for variant,sets in [('product_paths',product_sets),('row_first_total',total_sets)]:
        scalings={};stages=[]
        for allowed in sets:
            reindex={j:i for i,j in enumerate(allowed)}
            assert all(not set(all_GT[j])-set(allowed) for j in allowed)
            H=[{reindex[j]:p for j,p in all_GT[i].items()} for i in allowed]
            amb=[all_ambient[i] for i in allowed];den=[all_den[i] for i in allowed]
            answer=solve_stage(H,amb,den,[scalings[i] for i in allowed[1:]],keys)
            # The broader length-stratum interpretation gives exactly the
            # same least candidate, or the same failure, in these stages.
            broad=solve_stage(H,amb,den,[scalings[i] for i in allowed[1:]],keys,'length_strata')
            assert broad['global_minimum_exists']==answer['global_minimum_exists']
            assert broad['lexicographic_candidate']==answer['lexicographic_candidate']
            if answer['global_minimum_exists']:
                assert broad['unique_in_full_bar_fixed_domain']==answer['unique_in_full_bar_fixed_domain']
            else:
                least=vector(answer['lexicographic_candidate']['ambient_coordinates'])
                witness=vector(answer['partial_order_failure_witness']['ambient_coordinates'])
                z=272
                # Record the simple diagonal witness used in the proof,
                # even when a different valid witness is encountered first.
                assert witness.get(z,ZERO).degree()<least.get(z,ZERO).degree()
                lengths=[tuple(sorted((length(a),length(b)),reverse=True)) for a,b in keys]
                predecessors=[x for x in range(len(keys))
                              if lengths[x][0]>=lengths[z][0] and lengths[x][1]>=lengths[z][1]
                              and lengths[x]!=lengths[z]]
                assert all(witness.get(x,ZERO).degree()<=least.get(x,ZERO).degree() for x in predecessors)
                answer['additional_diagonal_failure']={'coordinate':z,
                        'permutations_one_based':[[a+1 for a in w] for w in keys[z]],
                        'least_polynomial_degree':least[z].degree(),
                        'witness_polynomial_degree':witness[z].degree(),
                        'all_length_stratum_predecessors_checked':len(predecessors)}
            answer.update({'actual_row_indices':allowed,
                           'label':data['coordinate_labels'][allowed[0]],
                           'also_verified_for_length_stratum_order':True})
            stages.append(answer)
            print(json.dumps({'variant':variant,'stage':len(stages),
                              'global_minimum':answer['global_minimum_exists'],
                              'unique':answer.get('unique_in_full_bar_fixed_domain'),
                              'exponent':answer['lexicographic_candidate']['scaling'],
                              'quotient_dimension':answer['finite_quotient_dimension'],
                              'cutoff':answer['cutoff_B'],
                              'row_coefficients':answer['lexicographic_candidate']['actual_row_coefficients']}),flush=True)
            if not answer['global_minimum_exists']:break
            assert answer['unique_in_full_bar_fixed_domain']
            scalings[allowed[0]]=answer['lexicographic_candidate']['scaling']
        results[variant]=stages
    assert [r['lexicographic_candidate']['scaling'] for r in results['product_paths']]==[-8,-8,-7,-6]
    assert all(r['global_minimum_exists'] for r in results['product_paths'])
    assert not results['row_first_total'][-1]['global_minimum_exists']
    record={'status':'PASS','scope':'Two explicit repaired bar-fixed/order variants; not the literal printed E(4).',
            'actual_order_source':'polynomial_order_gt_hermite.json.gz',
            'GT_normalization_source':'rational_gt_rank4_verified.json',
            'ambient_order':'Product of genuine reverse-length factor orders; equal-length distinct permutations incomparable.',
            'variants':results,'seconds':time.time()-started}
    (HERE/'bar_fixed_block_rank4_verified.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'PASS','seconds':time.time()-started}),flush=True)


if __name__=='__main__':main()
