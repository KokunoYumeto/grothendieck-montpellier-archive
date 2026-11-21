#!/usr/bin/env python3
"""Independent Gaussian local arithmetic, without sibling code imports.

The sibling group enumeration is rerun separately in g31_rerun. Here moving
determinants come from sums of principal minors, ranks from the last nonzero
elementary symmetric coefficient, and all small determinants use Leibniz sums.
This deliberately avoids the sibling's Gaussian elimination/induced action.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

class C:
    def __init__(self,a=0,b=0):
        if isinstance(a,C):self.a,self.b=a.a,a.b
        else:self.a,self.b=Q(a),Q(b)
    def __add__(x,y):
        y=C(y);return C(x.a+y.a,x.b+y.b)
    __radd__=__add__
    def __neg__(x):return C(-x.a,-x.b)
    def __sub__(x,y):return x+-C(y)
    def __rsub__(x,y):return C(y)+-x
    def __mul__(x,y):
        y=C(y);return C(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
    __rmul__=__mul__
    def bar(x):return C(x.a,-x.b)
    def __bool__(x):return bool(x.a or x.b)
    def __eq__(x,y):
        y=C(y);return x.a==y.a and x.b==y.b
    def pair(x):return [str(x.a),str(x.b)]

def eye(n):return [[C(i==j) for j in range(n)]for i in range(n)]
def mul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),C()) for j in range(len(b[0]))]for i in range(len(a))]
def star(a):return [[a[j][i].bar() for j in range(len(a))]for i in range(len(a[0]))]
def sub(a,b):return [[x-y for x,y in zip(r,s)]for r,s in zip(a,b)]
def determinant(a):
    n=len(a);answer=C()
    for p in permutations(range(n)):
        term=C(-1 if sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))%2 else 1)
        for i in range(n):term=term*a[i][p[i]]
        answer=answer+term
    return answer
def minor(a,ii,jj):return [[a[i][j] for j in jj]for i in ii]
def elementary(a,k):return sum((determinant(minor(a,jj,jj))for jj in combinations(range(len(a)),k)),C())
def decode(e):return [[C(Q(e[2*(4*i+j)],2),Q(e[2*(4*i+j)+1],2)) for j in range(4)]for i in range(4)]
def from_pairs(a):return [[C(*z)for z in row]for row in a]
def norm_bad(q):
    out=[]
    for number in [q.numerator,q.denominator]:
        p=2
        while p*p<=number:
            parity=0
            while number%p==0:number//=p;parity^=1
            if p%4==3 and parity:out.append(p)
            p+=1
        if number>1 and number%4==3:out.append(number)
    return sorted(p for p in set(out)if out.count(p)%2)

def check_group(number):
    raw=json.loads((ROOT/'g31_rerun'/f'G{number}_classes.json').read_text())
    comparison=json.loads((ROOT/'g31_rerun'/f'G{number}_local_discriminants.json').read_text())
    bad=[]
    for item,expected in zip(raw['classes'],comparison['classes']):
        g=decode(item['representative']);assert mul(star(g),g)==eye(4)
        a=sub(eye(4),g)
        coeff=[elementary(a,k)for k in range(5)]
        rank=max(k for k,z in enumerate(coeff)if z)
        b=coeff[rank]
        if rank:
            for jj in combinations(range(4),rank):
                u=minor(a,range(4),jj);gram=determinant(mul(star(u),u))
                if gram:break
            else:raise AssertionError('no independent columns')
        else:gram=C(1)
        assert not gram.b and gram.a>0 and (not b.a or not b.b)
        q=gram.a/(abs(b.a)if b.a else abs(b.b))
        odd=norm_bad(q)
        assert rank==expected['moving_rank']
        assert b.pair()==expected['det_one_minus_moving']
        assert gram.pair()==expected['moving_gram_determinant']
        assert str(q)==expected['positive_local_q']
        assert odd==expected['inert_prime_odd_valuations']
        if odd:bad.append({'index':item['index'],'rank':rank,'order':item['order'],'q':str(q),'b':b.pair(),'size':item['size']})
    assert sum(c['size']for c in raw['classes'])==raw['group_order']
    return {'group':number,'classes_checked':len(raw['classes']),'nonnorm':bad}

def check_tuple():
    data=json.loads((ROOT/'g31_rerun/nonsplit_tuple.json').read_text())
    tt=[from_pairs(g)for g in data['sixfold_tuple']]
    p=eye(4)
    for g in tt:p=mul(p,g)
    assert p==eye(4)
    i=C(0,1)
    u=[[C(1),-i,C(-1),i],[i,C(1),i,C(1)],[C(-1),-i,C(1),i],[-i,C(1),-i,C(1)]]
    u=[[z*C(Q(1,2))for z in r]for r in u]
    c=[[C(),1-i,-1-i,C()],[-1+i,C(),C(),1+i],[1-i,C(),C(),1+i],[C(),-1+i,-1-i,C()]]
    c=[[z*C(Q(1,2))for z in r]for r in c]
    assert tt[-2]==u and tt[-1]==c
    assert determinant(sub(eye(4),c))==3
    cp=[elementary(c,k)for k in range(5)]
    assert cp==[C(1),C(0),C(1),C(0),C(1)]
    p=eye(4)
    for k in range(1,7):
        p=mul(p,c)
        assert (p==eye(4))==(k==6)
    dets=[]
    for key in ['sixfold_parabolic_certificate','tail_parabolic_certificate']:
        gram=from_pairs(data[key]['cup_gram'])
        assert star(gram)==[[-z for z in row]for row in gram]
        det=determinant(gram)
        assert det.pair()==data[key]['cup_determinant']
        dets.append(det.pair())
    assert dets==[['3/8','0'],['3/2','0']]
    assert 1+Q(46080,2)*(-2+10*Q(1,2)+Q(5,6))==88321
    return {'printed_u_c_match':True,'characteristic_polynomial_c':'x^4+x^2+1','exact_order_c':6,'cup_determinants':dets,'genus':88321}

if __name__=='__main__':
    result={'groups':[check_group(29),check_group(31)],'tuple':check_tuple(),'all_pass':True}
    (ROOT/'audit_g31_independent.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
