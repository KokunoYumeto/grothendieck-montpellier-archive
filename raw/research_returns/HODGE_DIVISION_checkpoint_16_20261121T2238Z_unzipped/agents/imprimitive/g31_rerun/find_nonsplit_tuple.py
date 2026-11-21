#!/usr/bin/env python3
"""Exact G31 nonsplit product-one tuple; no dominance claim.
Finds a six-reflection word containing all five published generators with
regular order-six inverse, then inserts two doubled-reflection pairs.
"""
from fractions import Fraction as Q
from pathlib import Path
import random,json
import gaussian_exact as M
from check_local_discriminants import spectrum,inert_parities
HERE=Path(__file__).resolve().parent

def decode(a):return [[M.F(Q(a[2*(4*j+k)],2),Q(a[2*(4*j+k)+1],2)) for k in range(4)] for j in range(4)]
def key(a):return tuple(tuple(row)for row in a)
def order(a):
    p=M.eye(4)
    for j in range(1,193):
        p=M.mul(p,a)
        if p==M.eye(4):return j
    raise AssertionError('order not found')

def quotient(tt):
    m=4;blocks=[];us=[];selectors=[];dims=[];actions=[];p=M.eye(m)
    product_q=M.ONE
    for g in tt:
        a=M.sub(M.eye(m),g);cols=M.rref(a)[1]
        U=M.tr([M.tr(a)[j]for j in cols]);rows=M.rref(M.tr(U))[1];left=M.inv([U[j]for j in rows])
        T=M.mul(left,[M.mul(g,U)[j]for j in rows]);assert M.mul(U,T)==M.mul(g,U)
        gram=M.mul(M.star(U),U);b=M.det(M.sub(M.eye(len(cols)),T))
        product_q*=M.det(gram)/b
        blocks.append(M.mul(p,U));us.append(U);selectors.append((rows,left));dims.append(len(cols));actions.append(T)
        p=M.mul(p,g)
    assert p==M.eye(m)
    D=sum(dims);R=[sum((block[j]for block in blocks),[])for j in range(m)];cob=[]
    for g,(rows,left)in zip(tt,selectors):cob.extend(M.mul(left,[M.sub(M.eye(m),g)[j]for j in rows]))
    assert M.rank(R)==M.rank(cob)==m and M.iszero(M.mul(R,cob))
    offsets=[0]
    for d in dims:offsets.append(offsets[-1]+d)
    S=M.zero(D,D)
    for j,U in enumerate(blocks):
        for i in range(j,len(tt)):
            block=M.mul(M.star(U),blocks[i])
            if i==j:block=M.mul(M.star(M.inv(M.sub(M.eye(dims[i]),actions[i]))),block)
            for a in range(dims[j]):
                for b in range(dims[i]):S[offsets[j]+a][offsets[i]+b]=block[a][b]
    assert M.add(S,M.star(S))==M.mul(M.star(R),R)
    assert M.mul(M.star(cob),S)==R
    ex=[row[:]for row in cob];pcols=[]
    for v in M.tr(M.nullspace(R)):
        candidate=[row+[x]for row,x in zip(ex,v)]
        if M.rank(candidate)>M.rank(ex):ex=candidate;pcols.append(v)
    P=M.tr(pcols);gram=M.mul(M.star(P),M.mul(S,P))
    assert M.add(gram,M.star(gram))==M.zero(D-2*m,D-2*m)
    determinant=M.det(gram);assert not determinant.b and determinant.a>0
    assert not product_q.b and product_q.a>0
    assert inert_parities(determinant.a)==inert_parities(product_q.a)==[3]
    return {'moving_dimensions':dims,'relation_rank':m,'coboundary_rank':m,
            'parabolic_dimension':D-2*m,'basis':M.serialize(P),
            'cup_gram':M.serialize(gram),'cup_determinant':determinant.pair(),
            'local_determinant_product':product_q.pair(),'signed_discriminant_inert_parities':[3]}

def main():
    raw=json.loads((HERE/'G31_classes.json').read_text());ss=[decode(a)for a in raw['generators']]
    roots={key(ss[-1])};todo=[ss[-1]]
    while todo:
        g=todo.pop()
        for s in ss:
            a=M.mul(s,M.mul(g,s))
            if key(a)not in roots:roots.add(key(a));todo.append(a)
    refs=[[list(r)for r in a]for a in sorted(roots,key=lambda a:tuple((x.a,x.b)for row in a for x in row))]
    assert len(refs)==60
    rng=random.Random(20261121)
    for trial in range(1000):
        permutation=list(range(5));rng.shuffle(permutation)
        tail=[ss[j]for j in permutation]+[rng.choice(refs)]
        p=M.eye(4)
        for s in tail:p=M.mul(p,s)
        g=M.star(p)
        if order(g)!=6 or M.rank(M.sub(M.eye(4),g))!=4:continue
        b=M.det(M.sub(M.eye(4),g))
        if b!=3:continue
        eig=spectrum(g,6);age=sum((Q(k*n,6)for k,n in enumerate(eig)),Q())
        if age!=2:continue
        break
    else:raise AssertionError('fixed-seed search exhausted')
    tt=[ss[0],ss[0],ss[1],ss[1]]+tail+[g]
    q6=quotient(tt);q2=quotient(tail+[g])
    assert q6['parabolic_dimension']==6 and q2['parabolic_dimension']==2
    result={'group':'G31','group_order':46080,'seed':20261121,'trial':trial,
            'published_generator_order_in_tail':[j+1 for j in permutation],
            'all_five_generators_occur_in_tail':True,
            'tail_six_reflections':[M.serialize(s)for s in tail],
            'regular_inverse':M.serialize(g),'regular_order':6,'regular_eigenvalue_multiplicities':eig,
            'regular_det_one_minus':b.pair(),
            'sixfold_tuple':[M.serialize(s)for s in tt],
            'sixfold_branch_orders':[2]*10+[6],'sixfold_cover_genus':88321,
            'sixfold_signature':[3,3],'sixfold_source_dimension':8,
            'sixfold_period_rank':'not computed; at most8',
            'sixfold_parabolic_certificate':q6,
            'tail_signature':[1,1],'tail_source_dimension':4,
            'tail_parabolic_certificate':q2}
    (HERE/'nonsplit_tuple.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS nonsplit tuple trial',trial,'regular det(I-g)',b,'sixfold/tail determinants',q6['cup_determinant'],q2['cup_determinant'])

if __name__=='__main__':main()
