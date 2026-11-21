#!/usr/bin/env python3
"""Select and certify a generating E8 Gaussian twelve-branch tuple.

All root closure, matrix, quotient, cup and signature assertions are exact.
This certificate does not assert period rank nine or provide Weil cycles.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import deque
from math import gcd
import sys,json,hashlib
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'g31_rerun'))
import gaussian_exact as M

def imul(a,b):return [[sum(a[i][k]*b[k][j]for k in range(len(b)))for j in range(len(b[0]))]for i in range(len(a))]
def imv(a,v):return tuple(sum(x*y for x,y in zip(r,v))for r in a)
def ii(n):return [[int(i==j)for j in range(n)]for i in range(n)]
def matrix(a):return [a[8*i:8*i+8]for i in range(8)]
def closure(vv,actions):
    roots=list(vv);seen={v:i for i,v in enumerate(roots)};parents=[None]*len(roots)
    p=0
    while p<len(roots):
        for j,a in enumerate(actions):
            v=imv(a,roots[p])
            if v not in seen:seen[v]=len(roots);roots.append(v);parents.append([p,j])
        p+=1
        assert len(roots)<=240
    return roots,parents

def quotient(tt,H):
    m=len(H);blocks=[];selectors=[];dims=[];actions=[];p=M.eye(m);locals=[];product_q=M.ONE
    for g in tt:
        a=M.sub(M.eye(m),g);cols=M.rref(a)[1]
        U=M.tr([M.tr(a)[j]for j in cols]);rows=M.rref(M.tr(U))[1];left=M.inv([U[j]for j in rows])
        T=M.mul(left,[M.mul(g,U)[j]for j in rows]);assert M.mul(U,T)==M.mul(g,U)
        gram=M.mul(M.mul(M.star(U),H),U);b=M.det(M.sub(M.eye(len(cols)),T));gd=M.det(gram)
        product_q*=gd/b
        locals.append({'moving_rank':len(cols),'moving_gram_determinant':gd.pair(),'det_one_minus_moving':b.pair()})
        blocks.append(M.mul(p,U));selectors.append((rows,left));dims.append(len(cols));actions.append(T)
        p=M.mul(p,g)
    assert p==M.eye(m)
    D=sum(dims);R=[sum((b[j]for b in blocks),[])for j in range(m)];cob=[]
    for g,(rows,left)in zip(tt,selectors):cob.extend(M.mul(left,[M.sub(M.eye(m),g)[j]for j in rows]))
    assert M.rank(R)==M.rank(cob)==m and M.iszero(M.mul(R,cob))
    off=[0]
    for k in dims:off.append(off[-1]+k)
    S=M.zero(D,D)
    for j,U in enumerate(blocks):
        for i in range(j,len(tt)):
            block=M.mul(M.mul(M.star(U),H),blocks[i])
            if i==j:block=M.mul(M.star(M.inv(M.sub(M.eye(dims[i]),actions[i]))),block)
            for a in range(dims[j]):
                for b in range(dims[i]):S[off[j]+a][off[i]+b]=block[a][b]
    assert M.add(S,M.star(S))==M.mul(M.mul(M.star(R),H),R)
    assert M.mul(M.star(cob),S)==M.mul(H,R)
    ex=[r[:]for r in cob];pcols=[]
    for v in M.tr(M.nullspace(R)):
        candidate=[r+[x]for r,x in zip(ex,v)]
        if M.rank(candidate)>M.rank(ex):ex=candidate;pcols.append(v)
    P=M.tr(pcols);gram=M.mul(M.star(P),M.mul(S,P));dim=D-2*m
    assert M.add(gram,M.star(gram))==M.zero(dim,dim)
    determinant=M.det(gram);assert not determinant.b and determinant.a>0
    return {'moving_dimensions':dims,'moving_total':D,'relation_rank':m,'coboundary_rank':m,'parabolic_dimension':dim,
            'local_data':locals,'local_determinant_product':product_q.pair(),
            'quotient_basis':M.serialize(P),'cup_gram':M.serialize(gram),'cup_determinant':determinant.pair(),
            'relation_matrix':M.serialize(R),'coboundary_matrix':M.serialize(cob),'ambient_seifert_matrix':M.serialize(S)}

def main():
    source=ROOT/'../../research/e8_class_exploration.json';data=json.loads(source.read_text());H=data['cartan'];I=ii(8)
    ss=[]
    for i in range(8):
        s=[r[:]for r in I]
        for j in range(8):s[i][j]-=H[i][j]
        ss.append(s)
    seedroots=[tuple(int(i==j)for i in range(8))for j in range(8)]
    allroots,_=closure(seedroots,ss);assert len(allroots)==240
    for v in allroots:assert sum(x*y for x,y in zip(v,imv(H,v)))==2
    searches=json.loads((ROOT/'e8_search/search_results.json').read_text())
    branch=next(s for s in searches['searches']if s['label']=='six_simple_E6')
    chosen=None;trials=[]
    for match in branch['matches']:
        j=matrix(match['j']);roots,parents=closure(seedroots[:6],ss[:6]+[j])
        trials.append({'orbit_index':match['orbit_index'],'root_orbit_size':len(roots)})
        if len(roots)==240:chosen=match;break
    assert chosen is not None and set(roots)==set(allroots)
    j0=data['classes'][5]['matrix'];jcheck=j0
    for k in chosen['conjugations']:jcheck=imul(ss[k-1],imul(jcheck,ss[k-1]))
    assert jcheck==matrix(chosen['j']) and imul(jcheck,jcheck)==[[-z for z in r]for r in I]
    j=matrix(chosen['j']);w=matrix(chosen['w'])
    fm=lambda a:[[M.F(x)for x in r]for r in a]
    h=[[M.F(0,x)for x in r]for r in j];g=[[M.F(0,x)for x in r]for r in w]
    fs=[fm(s)for s in ss];HH=fm(H)
    for a in fs+[h,g]:assert M.mul(M.mul(M.star(a),HH),a)==HH
    assert M.mul(h,h)==M.eye(8)
    p=M.eye(8)
    for k in range(1,13):
        p=M.mul(p,g)
        assert (p==M.eye(8))==(k==12)
    tail=fs[:6]+[h,g];tt=[fs[0],fs[0],fs[1],fs[1]]+tail
    cp=quotient(tt,HH);cp2=quotient(tail,HH)
    assert cp['parabolic_dimension']==6 and cp2['parabolic_dimension']==2
    cls=chosen['spectral_class']
    rootspec=([(Q(k,3)+Q(1,4))%1 for k in [1,2]]+
              [(Q(k,12)+Q(1,4))%1 for k in [1,5,7,11]]+[Q(1,4)]*2) if cls==57 else (
              [(Q(k,6)+Q(1,4))%1 for k in [1,5]]+
              [(Q(k,12)+Q(1,4))%1 for k in [1,5,7,11]]+[Q(3,4)]*2)
    assert sum(rootspec,Q())==4 and all(rootspec)
    size=2*696729600;genus=1+Q(size,2)*(-2+11*Q(1,2)+Q(11,12));tailgenus=1+Q(size,2)*(-2+7*Q(1,2)+Q(11,12))
    assert genus.denominator==tailgenus.denominator==1
    out={'status':'PASS','source_class_data_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'weyl_order':696729600,'gaussian_group_order':size,'cartan':H,'simple_reflections':ss,
         'chosen_match':chosen,'generation_trials':trials,'root_generation_count':240,
         'root_generation_vectors':[list(v)for v in roots],'root_generation_parents':parents,
         'root_generation_actions':'six simple reflections, then j; j acts on reflection lines by conjugation with h=i*j',
         'h':M.serialize(h),'g':M.serialize(g),'g_order':12,'g_eigenvalue_exponents':[str(x)for x in sorted(rootspec)],
         'tuple_word':['s1','s1','s2','s2','s1','s2','s3','s4','s5','s6','h','g'],
         'branch_orders':[2]*11+[12],'signature':[3,3],'source_dimension':9,'cover_genus':int(genus),
         'tail_branch_orders':[2]*7+[12],'tail_signature':[1,1],'tail_cover_genus':int(tailgenus),
         'graph_natural_multiplicity':2,'sixfold_parabolic':cp,'tail_parabolic':cp2,
         'period_rank_status':'not yet computed','cycle_supplier_status':'not supplied'}
    (ROOT/'e8_search/tuple_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k]for k in ['status','chosen_match','generation_trials','root_generation_count','signature','source_dimension','cover_genus','tail_signature','graph_natural_multiplicity']}))
    print('CUP determinants:',cp['cup_determinant'],cp2['cup_determinant'])

if __name__=='__main__':main()
