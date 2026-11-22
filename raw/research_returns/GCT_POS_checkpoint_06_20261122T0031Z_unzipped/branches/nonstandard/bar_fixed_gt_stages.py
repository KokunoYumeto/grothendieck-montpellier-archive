"""Exact finite globalization stages in the explicitly recorded order variant.

The actual GT-Hermite order basis makes the primitive current-line kernel
and a finite complement accessible by triangular polynomial arithmetic.
The source prescription is not silently amended: this is the bar-fixed,
rationally normalized, explicitly totally ordered variant described in
the branch proofs.  Default: first four stages; --stages can request more.
"""
from pathlib import Path
import argparse,json,gzip,time
from flint import fmpq,fmpq_poly
from bar_fixed_first_stages import parse,vector,sp,sv,combine,Equations,decide

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def exact(p,q):
    a,r=divmod(p,q);assert not r
    return a


class Rational:
    def __init__(self,p=ZERO,q=ONE):
        if not p:self.p,self.q=ZERO,ONE;return
        g=p.gcd(q);p,q=exact(p,g),exact(q,g)
        c=q.leading_coefficient();self.p,self.q=p/c,q/c
    def add(self,other):
        g=self.q.gcd(other.q)
        a,b=exact(other.q,g),exact(self.q,g)
        return Rational(self.p*a+other.p*b,self.q*a)
    def times(self,p):return Rational(self.p*p,self.q)
    def divide(self,q):return Rational(self.p,self.q*q)


def linear_combine(polys,rows):
    out={}
    for p,row in zip(polys,rows):out=combine(ONE,out,p,row)
    return out


def bounded_coefficients(H,ambient,caps,current_bound=None):
    """All coefficient vectors in a finite box satisfying GT degree caps.

    H is upper triangular in the chosen descending GT coordinate order.
    With current_bound supplied, coordinate0 is unconstrained by caps
    and its polynomial row coefficient is bounded by that value instead.
    Otherwise every GT coordinate is capped.  Exact cancellation equations
    are imposed after deriving necessary coefficient bounds recursively.
    """
    k=len(H);bounds=[]
    for i in range(k):
        if i==0 and current_bound is not None:
            bounds.append(current_bound);continue
        upper=max([caps[i]]+[bounds[j]+H[j].get(i,ZERO).degree()
                  for j in range(i) if bounds[j]>=0 and H[j].get(i,ZERO)])
        bounds.append(max(-1,upper-H[i][i].degree()))
    variables=[(i,e) for i,b in enumerate(bounds) for e in range(b+1)]
    E=Equations(len(variables))
    for i in range(k):
        if i==0 and current_bound is not None:continue
        high=max([caps[i]]+[bounds[j]+H[j].get(i,ZERO).degree()
                 for j in range(i+1) if bounds[j]>=0 and H[j].get(i,ZERO)])
        for power in range(max(0,caps[i]+1),high+1):
            E.add([H[j].get(i,ZERO)[power-e] if power>=e else fmpq(0)
                   for j,e in variables])
    coefficients=[];vectors=[];current=[]
    for c in E.kernel():
        polys=[]
        for i,b in enumerate(bounds):
            a=[fmpq(0) for _ in range(b+1)]
            for x,(j,e) in zip(c,variables):
                if i==j:a[e]=x
            polys.append(fmpq_poly(a))
        for i in range(k):
            if i==0 and current_bound is not None:continue
            a=sum((polys[j]*H[j].get(i,ZERO) for j in range(i+1)),ZERO)
            assert a.degree()<=caps[i]
        coefficients.append(polys)
        vectors.append(linear_combine(polys,ambient))
        current.append(polys[0]*H[0][0])
    return {'coefficient_bounds':bounds,'variables':len(variables),
            'coefficients':coefficients,'vectors':vectors,'top_numerators':current}


def odd_dimension(H,ambient,denominators,scalings,profile):
    # A pure odd element of a least-profile box cannot have a nonzero
    # current coefficient, by N013.  Thus it lies in the lower flag.
    k=len(H)-1
    if not k:return 0
    lowerH=[{j-1:p for j,p in row.items() if j>=1} for row in H[1:]]
    caps=[-scalings[-1-i]-1+denominators[i+1].degree() for i in range(k)]
    result=bounded_coefficients(lowerH,ambient[1:],caps)
    vectors=result['vectors'];E=Equations(len(vectors))
    for z,cap in enumerate(profile):
        # delta*w at most delta^epsilon*D^cap forces deg_D w_z<=cap-1.
        bound=cap-1
        high=max((v.get(z,ZERO).degree() for v in vectors),default=-1)
        for power in range(max(0,bound+1),high+1):
            E.add([v.get(z,ZERO)[power] for v in vectors])
    return len(E.kernel())


def main(stages):
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    all_ambient=[vector(r['ambient_coordinates']) for r in data['rows']]
    all_GT=[vector(r['gt_numerators']) for r in data['rows']]
    all_den=[parse(p) for p in data['coordinate_denominators']]
    keys=[(tuple(a),tuple(b)) for a,b in data['ambient_coordinates']]
    scalings=[];records=[]
    for k in range(1,stages+1):
        begin=114-k
        H=[{j-begin:p for j,p in row.items() if j>=begin} for row in all_GT[begin:]]
        ambient=all_ambient[begin:];den=all_den[begin:]
        rational=[Rational(ONE)]
        for i in range(1,k):
            a=Rational()
            for j in range(i):a=a.add(rational[j].times(H[j].get(i,ZERO)))
            rational.append(a.times(-ONE).divide(H[i][i]))
        kernel_coefficient=ONE
        for r in rational:
            kernel_coefficient=exact(kernel_coefficient*r.q,kernel_coefficient.gcd(r.q))
        coefficients=[r.p*exact(kernel_coefficient,r.q) for r in rational]
        assert coefficients[0]==kernel_coefficient
        assert all(not sum((coefficients[j]*H[j].get(i,ZERO) for j in range(i+1)),ZERO)
                   for i in range(1,k))
        t=linear_combine(coefficients,ambient);tn=coefficients[0]*H[0][0]
        scale=den[0].leading_coefficient()/tn.leading_coefficient()
        t={j:p*scale for j,p in t.items()};tn*=scale
        caps=[None]+[-scalings[-i]-1+den[i].degree() for i in range(1,k)]
        complement=bounded_coefficients(H,ambient,caps,current_bound=kernel_coefficient.degree()-1)
        ys,yn=complement['vectors'],complement['top_numerators']
        B=max([0]+[p.degree()-t[z].degree() for y in ys for z,p in y.items() if z in t])
        space=ys+[{z:p*D**i for z,p in t.items()} for i in range(B+1)]
        top=yn+[tn*D**i for i in range(B+1)]
        answer=decide(space,top,den[0],keys)
        answer.update({'stage':k,'label':data['coordinate_labels'][begin],
                       'primitive_kernel_coefficient':sp(kernel_coefficient),
                       'kernel_row_coefficients':[sp(p) for p in coefficients],
                       'finite_complement_coefficient_bounds':complement['coefficient_bounds'],
                       'finite_complement_parameter_count':complement['variables'],
                       'finite_complement_row_coefficients':[[sp(p) for p in c] for c in complement['coefficients']],
                       'finite_quotient_dimension':len(ys),'cutoff_B':B,
                       'finite_space_dimension':len(space),'basis_vectors':[sv(v) for v in space],
                       'top_numerators':[sp(p) for p in top],'top_denominator':sp(den[0])})
        if answer['global_minimum_exists']:
            odd=odd_dimension(H,ambient,den,scalings,answer['lexicographic_profile'])
            full_dimension=answer['lexicographic_minimizing_dimension']+odd
            answer['odd_minimizing_dimension']=odd
            answer['full_bar_fixed_minimizing_dimension']=full_dimension
            answer['unique_in_full_bar_fixed_domain']=full_dimension==1
        records.append(answer)
        record={'status':'PASS','scope':'Exact global stages of explicitly chosen bar-fixed/order/normalization variant; not printed E(4).',
                'variant_order':data['variant_order'],'stages':records,'seconds':time.time()-started}
        (HERE/'bar_fixed_gt_stages_verified.json').write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({'stage':k,'global_minimum':answer['global_minimum_exists'],
                          'unique':answer.get('unique_in_full_bar_fixed_domain'),
                          'finite_quotient':len(ys),'cutoff':B,'finite_dimension':len(space),
                          'full_minimizing_dimension':answer.get('full_bar_fixed_minimizing_dimension'),
                          'scaling':answer['lexicographic_candidate']['scaling'],
                          'failure_coordinate':None if answer['partial_order_failure_witness'] is None else answer['partial_order_failure_witness']['coordinate'],
                          'seconds':time.time()-started}),flush=True)
        if not answer['global_minimum_exists'] or not answer['unique_in_full_bar_fixed_domain']:break
        scalings.append(answer['lexicographic_candidate']['scaling'])


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--stages',type=int,default=4)
    args=parser.parse_args();assert 1<=args.stages<=114
    main(args.stages)
