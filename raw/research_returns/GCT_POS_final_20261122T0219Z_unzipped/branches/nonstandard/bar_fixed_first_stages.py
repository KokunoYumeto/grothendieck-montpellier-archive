"""Execute the first two stages of the explicit recorded bar-fixed variant.

Uses the global cutoff N-016 and its exact partial-order witness test.
The input order is explicitly additional to VIII, as recorded in the GT
Hermite certificate.  This script does not identify its result with E(4).
"""
from pathlib import Path
import json,gzip,time
from flint import fmpq,fmpq_poly

HERE=Path(__file__).resolve().parent
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);D=fmpq_poly([0,1])


def parse(p):return fmpq_poly([fmpq(p.get(str(i),'0')) for i in range(max(map(int,p),default=-1)+1)])
def vector(v):return {int(j):parse(p) for j,p in v.items()}
def sp(p):return {str(i):str(c) for i,c in enumerate(p.coeffs()) if c}
def sv(v):return {str(j):sp(p) for j,p in v.items() if p}


def combine(a,x,b,y):
    z={j:p*a for j,p in x.items() if p*a}
    for j,p in y.items():
        v=z.get(j,ZERO)+p*b
        if v:z[j]=v
        else:z.pop(j,None)
    return z


class Equations:
    def __init__(self,n,rows=None):self.n=n;self.rows={} if rows is None else dict(rows)
    def copy(self):return Equations(self.n,self.rows)
    def remainder(self,row):
        a=list(row)
        for j,b in sorted(self.rows.items()):
            if a[j]:
                c=a[j];a=[x-c*y for x,y in zip(a,b)]
        return a
    def add(self,row):
        a=self.remainder(row)
        j=next((j for j,c in enumerate(a) if c),None)
        if j is not None:
            c=a[j];self.rows[j]=[x/c for x in a]
    def viable(self,functionals):return any(any(self.remainder(f)) for f in functionals)
    def kernel(self):
        out=[]
        for j in range(self.n):
            if j in self.rows:continue
            a=[fmpq(0) for _ in range(self.n)];a[j]=fmpq(1)
            for k,b in sorted(self.rows.items(),reverse=True):
                a[k]=-sum((b[i]*a[i] for i in range(k+1,self.n)),fmpq(0))
            out.append(a)
        return out


def length(w):return sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w)))


def decide(vectors,top,denominator,keys,ambient_order='length_strata'):
    n=len(vectors);H=[max((v.get(z,ZERO).degree() for v in vectors),default=-1) for z in range(len(keys))]
    functionals=[[p[k] for p in top] for k in range(max(p.degree() for p in top)+1)]
    coefs={(z,k):[v.get(z,ZERO)[k] for v in vectors]
           for z,h in enumerate(H) for k in range(h+1)}
    lengths=[tuple(sorted((length(a),length(b)),reverse=True)) for a,b in keys]
    extension=sorted(range(len(keys)),key=lambda z:(-sum(lengths[z]),-lengths[z][0],z))
    if ambient_order=='length_strata':
        predecessors={z:[x for x in range(len(keys))
                          if lengths[x][0]>=lengths[z][0] and lengths[x][1]>=lengths[z][1]
                          and lengths[x]!=lengths[z]] for z in range(len(keys))}
    elif ambient_order=='factor_product':
        # Distinct permutations of equal length are incomparable.  The
        # tensor order is the product of these genuine factor orders.
        # Flip-identical coefficients permit folding to unordered pairs;
        # either orientation of a predecessor can witness the comparison.
        def le(a,b):return a==b or length(a)>length(b)
        def less(x,z):
            a,b=keys[x];c,d=keys[z]
            return x!=z and ((le(a,c) and le(b,d)) or (le(b,c) and le(a,d)))
        predecessors={z:[x for x in range(len(keys)) if less(x,z)] for z in range(len(keys))}
    else:raise ValueError(ambient_order)

    def bounded(E,z,bound):
        for k in range(bound+1,H[z]+1):E.add(coefs[z,k])

    E=Equations(n);profile=[-1]*len(keys);linear_tests=0;rank_drops=[]
    for z in extension:
        for bound in range(-1,H[z]+1):
            trial=E.copy();bounded(trial,z,bound);linear_tests+=1
            if trial.viable(functionals):
                if len(trial.rows)>len(E.rows):
                    rank_drops.append({'coordinate':z,'degree_bound':bound,
                                       'constraint_rank':len(trial.rows)})
                E=trial;profile[z]=bound;break
        else:raise AssertionError('greedy feasibility lost')

    def point(E):
        for a in E.kernel():
            p=sum((c*t for c,t in zip(a,top)),ZERO)
            if not p:continue
            scale=denominator.leading_coefficient()/p.leading_coefficient()
            a=[c*scale for c in a];p*=scale
            out={}
            for c,v in zip(a,vectors):out=combine(ONE,out,fmpq_poly([c]),v)
            assert p.leading_coefficient()==denominator.leading_coefficient()
            return a,out,p,denominator.degree()-p.degree()
        raise AssertionError('no viable point')

    a,minimum,p,exponent=point(E)
    assert [minimum.get(z,ZERO).degree() for z in range(len(keys))]==profile
    witness=None
    for z,cap in enumerate(profile):
        if cap<0:continue
        W=Equations(n)
        for x in predecessors[z]:bounded(W,x,profile[x])
        bounded(W,z,cap-1);linear_tests+=1
        if W.viable(functionals):
            c,y,h,ya=point(W)
            assert y.get(z,ZERO).degree()<cap
            assert all(y.get(x,ZERO).degree()<=profile[x] for x in predecessors[z])
            witness={'coordinate':z,'coefficient_vector':[str(x) for x in c],
                     'ambient_coordinates':sv(y),'top_numerator':sp(h),'scaling':ya}
            break
    return {'global_minimum_exists':witness is None,'lexicographic_profile':profile,
            'lexicographic_minimizing_dimension':len(E.kernel()),
            'lexicographic_candidate':{'coefficient_vector':[str(x) for x in a],
                                     'ambient_coordinates':sv(minimum),'top_numerator':sp(p),'scaling':exponent},
            'partial_order_failure_witness':witness,'linear_tests':linear_tests,
            'greedy_rank_drops':rank_drops,
            'ambient_order':ambient_order}


def main():
    started=time.time()
    with gzip.open(HERE/'polynomial_order_gt_hermite.json.gz','rt') as f:data=json.load(f)
    keys=[(tuple(a),tuple(b)) for a,b in data['ambient_coordinates']]
    r1,r2=data['rows'][113],data['rows'][112]
    t1,w=vector(r1['ambient_coordinates']),vector(r2['ambient_coordinates'])
    g=parse(r1['gt_numerators']['113']);h=parse(r2['gt_numerators'].get('113',{}))
    u=parse(r2['gt_numerators']['112'])
    den1=parse(data['coordinate_denominators'][113]);den2=parse(data['coordinate_denominators'][112])
    assert g.leading_coefficient()==den1.leading_coefficient()==1
    stage1={'label':data['coordinate_labels'][113],'scaling':den1.degree()-g.degree(),
            'top_numerator':sp(g),'top_denominator':sp(den1),'ambient_coordinates':sv(t1),
            'global_minimum_exists':True,'unique_in_full_bar_fixed_domain':True,
            'reason':'Primitive one-dimensional actual order line; N013 excludes odd parity and nonconstant polynomials increase every nonzero degree.'}

    d,alpha,beta=h.xgcd(g)
    assert alpha*h+beta*g==d
    gd,gr=divmod(g,d);hd,hr=divmod(h,d);assert not gr and not hr
    t=combine(gd,w,-hd,t1);tn=gd*u
    lift=combine(alpha,w,beta,t1);ln=alpha*u
    m=g.degree()-d.degree()
    ys=[combine(D**i,lift,ZERO,{}) for i in range(m)]
    yn=[D**i*ln for i in range(m)]
    B=max([0]+[p.degree()-t[z].degree() for y in ys for z,p in y.items() if z in t])
    space=ys+[combine(D**i,t,ZERO,{}) for i in range(B+1)]
    top=yn+[D**i*tn for i in range(B+1)]
    assert all((d*D**i).degree()<=g.degree()-1 for i in range(m))
    result=decide(space,top,den2,keys)
    result.update({'label':data['coordinate_labels'][112],'finite_quotient_dimension':m,
                   'cutoff_B':B,'finite_space_dimension':len(space),
                   'primitive_line':sv(t),'finite_complement':[sv(v) for v in ys],
                   'basis_vectors':[sv(v) for v in space],'top_numerators':[sp(p) for p in top],
                   'top_denominator':sp(den2)})
    if result['global_minimum_exists']:
        result['unique_in_full_bar_fixed_domain']=result['lexicographic_minimizing_dimension']==1
        result['odd_perturbation_check']='At stage2 any odd minimum perturbation has zero current coefficient by N013; it is delta*p(D)*t1, whose lower valuation bound forces deg p<=-1. Thus it is zero.'
    record={'status':'PASS','scope':'First two stages only; explicitly chosen bar-fixed/order/normalization variant, not printed E(4).',
            'variant_order':data['variant_order'],'stage1':stage1,'stage2':result,
            'seconds':time.time()-started}
    (HERE/'bar_fixed_first_stages_verified.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':'PASS','stage1_scaling':stage1['scaling'],
                     'stage2_global_minimum':result['global_minimum_exists'],
                     'stage2_unique':result.get('unique_in_full_bar_fixed_domain'),
                     'quotient_dimension':m,'cutoff':B,'finite_dimension':len(space),
                     'linear_tests':result['linear_tests'],
                     'stage2_scaling':result['lexicographic_candidate']['scaling'],
                     'failure_coordinate':None if result['partial_order_failure_witness'] is None else result['partial_order_failure_witness']['coordinate'],
                     'seconds':time.time()-started}),flush=True)


if __name__=='__main__':main()
