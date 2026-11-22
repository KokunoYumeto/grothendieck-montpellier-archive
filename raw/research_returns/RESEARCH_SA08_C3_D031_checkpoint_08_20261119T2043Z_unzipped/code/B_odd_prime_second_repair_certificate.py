#!/usr/bin/env python3
"""Exact odd-prime continuation of the complete A-P01 low lattices."""
from collections import defaultdict
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import time
import sympy as sp
from A_cosimplicial_deep_tail_certificate import Resolution, kernel, smith, vp


def add(out,key,value):
    if value:
        out[key]+=value
        if not out[key]: del out[key]


class Tail:
    def __init__(self,p):
        self.p=p; self.res=Resolution(p); self.gens={}; self.by_degree=defaultdict(list)
        for kind,top in [('u',2*p-1),('v',2*p-2)]:
            for level in range(top):
                for name,wt in self.res.gens[level]:
                    label=f'{kind}:{level}:{name}'
                    self.gens[label]=(top-level,wt,kind,level,name)
                    self.by_degree[top-level].append(label)

    def differential(self,label):
        degree,wt,kind,level,name=self.gens[label]; result=[]
        if kind=='v': result.append((f'u:{level}:{name}',0,F(self.p)))
        if level:
            for target_name,value in self.res.data[level][name].items():
                target=f'{kind}:{level-1}:{target_name}'
                result.append((target,wt-self.gens[target][1],value if kind=='v' else -value))
        return result

    def zero_basis(self,weight):
        source,_,matrix=self.res.w_d1(weight)
        if not source:return []
        basis=kernel(matrix,len(source),self.p)
        rank=len(basis[0]) if basis else 0
        return [{f'{kind}:{level}:{name}':(weight-wt,basis[i][j])
                 for i,(kind,level,name,wt) in enumerate(source) if basis[i][j]}
                for j in range(rank)]

    def odd_pair(self,first,second,k=0):
        col=defaultdict(F)
        for target,l,a in self.differential(first):add(col,('positive',second,target,k+l),a*comb(k+l,k))
        for target,l,a in self.differential(second):add(col,('positive',first,target,k+l),-a*comb(k+l,k))
        return dict(col)

    def zero_even(self,zero,even):
        col=defaultdict(F)
        for one,(k,a) in zero.items():
            add(col,('positive',one,even,k),a)
            for target,l,b in self.differential(even):
                add(col,('zero_embedding',one,target,k+l),a*b*comb(k+l,k))
        return dict(col)

    def d2(self,weight):
        cols=[]; ones=self.by_degree[1]
        for i,first in enumerate(ones):
            for second in ones[i+1:]:
                k=weight-self.gens[first][1]-self.gens[second][1]
                if k>=0:cols.append(self.odd_pair(first,second,k))
        for even in self.by_degree[2]:
            m=weight-self.gens[even][1]
            if m<0:continue
            assert m<=self.p*self.p
            cols.extend(self.zero_even(zero,even) for zero in self.zero_basis(m))
        rows=sorted(set().union(*(set(col) for col in cols))) if cols else []
        return rows,[[col.get(row,F(0)) for col in cols] for row in rows],len(cols)


def main():
    start=time.perf_counter(); results=[]
    for p in [3,5,7]:
        tail=Tail(p); c=factorial(p-1); a0=p*(p-1)+1; h=2*a0-1; first=h-(p-1)
        weights=[]
        for wt in range(1,h+1):
            rows,matrix,ncols=tail.d2(wt)
            diagonal,_,rank=smith(matrix,ncols,p)
            valuations=[vp(diagonal[i][i],p) for i in range(rank)]
            nonunits=[v for v in valuations if v]
            assert (rank,nonunits)==((5,[1]) if wt==h else ((1,[]) if wt>=first else (0,[])))
            weights.append({'weight':wt,'domain_rank':ncols,'differential_rank':rank,'nonunit_valuations':nonunits})
        def label(kind,level,index):return f'{kind}:{level}:{tail.res.gens[level][index][0]}'
        g=label('u',2*p-2,0); ell=label('u',2*p-2,1)
        x=label('v',2*p-3,0); y=label('v',2*p-3,1)
        r=label('u',2*p-3,0); sigma=label('u',2*p-3,1)
        a=label('v',2*p-4,0); b=label('v',2*p-4,1)
        e=label('u',2*p-4,0); f=label('u',2*p-4,1)
        z=label('v',2*p-5,0); w=label('v',2*p-5,1)
        zeros={'C':{g:(0,F(p)),x:(1,F(1)),y:(0,F(-p*c))},
               'H':{g:(p-1,F(-c)),ell:(0,F(p*c))},
               'K':{ell:(0,F(p)),x:(p,F(1)),y:(p-1,F(-c))},
               'J':{g:(p,F(-1)),ell:(1,F(1))}}
        cols=[tail.zero_even(zeros['C'],r),tail.odd_pair(g,x),tail.zero_even(zeros['H'],a),
              tail.zero_even(zeros['K'],a),tail.zero_even(zeros['C'],b),tail.odd_pair(x,y)]
        rows=sorted(set().union(*(set(col) for col in cols)))
        matrix=[[col.get(row,F(0)) for col in cols] for row in rows]
        zeta=defaultdict(F)
        for zn,positive,scale in [('K',e,1),('C',f,-1),('H',w,-1),('J',z,1)]:
            for one,(k,val) in zeros[zn].items():add(zeta,('zero_embedding',one,positive,k),scale*val)
        for one,two,scale in [(ell,a,1),(y,r,1),(x,sigma,-1),(g,b,-1)]:add(zeta,('positive',one,two,0),F(scale))
        primitive=[F(-1,c),F(-1,c),F(1,c),F(0),F(0),F(0)]
        image={row:sum(v*t for v,t in zip(vals,primitive)) for row,vals in zip(rows,matrix)}
        assert all(image.get(row,0)==p*zeta.get(row,0) for row in set(image)|set(zeta))
        detector=matrix[rows.index(('positive',g,b,0))]
        assert detector==[0,p*c,0,0,p,0]
        assert all(sum(v*t for v,t in zip(vals,[1,1,-1,c,-c,c]))==0 for vals in matrix)
        keys=[('positive',g,a,p-1),('positive',x,r,1),('positive',x,a,p),('positive',x,b,1),('positive',g,b,0)]
        five=sp.Matrix([matrix[rows.index(key)][:5] for key in keys]); det5=F(five.det())
        four=sp.Matrix([[matrix[rows.index(key)][j] for j in [0,2,3,4]] for key in keys[:4]]);det4=F(four.det())
        assert det5==-p*c*c and det4==c
        # The period identity reduces exactly to tH=pcJ; verify it in dW0.
        th=defaultdict(F)
        for one,(k,val) in zeros['H'].items():add(th,(one,k+1),val*(k+1))
        pcj={(one,k):p*c*val for one,(k,val) in zeros['J'].items()}
        assert dict(th)==pcj
        def ze(out,zero_name,positive,k=0,scale=F(1)):
            for one,(l,val) in zeros[zero_name].items():
                add(out,('zero_embedding',one,positive,k+l),scale*val*comb(k+l,k))
        left=defaultdict(F);right=defaultdict(F)
        ze(left,'H',a,k=1,scale=F(1,c));ze(left,'C',r,k=1,scale=F(-1,c))
        add(left,('odd_pair',g,x,1),F(-1,c))
        add(right,('odd_pair',g,x,1),F(-1,c));add(right,('odd_pair',g,y,0),F(p))
        ze(right,'C',r,k=1,scale=F(-1,c));ze(right,'C',sigma,scale=F(p))
        ze(right,'J',a,scale=F(p));add(right,('odd_pair',g,y,0),F(-p));ze(right,'C',sigma,scale=F(-p))
        assert dict(left)==dict(right)
        assert (2*(p*3)+h+1)%p==2%p
        results.append({'prime':p,'coefficient_cutoff':p*p,'first_form2_weight':first,'first_H3_weight':h,
                        'weight_cases':weights,'natural_degree2_basis':['Cr','gx','aH','aK','Cb','xy'],
                        'degree3_embedding_rows':rows,'differential_matrix':matrix,'detector':detector,
                        'minor4':four.tolist(),'minor5':five.tolist(),'determinants':[det4,det5],
                        'named_identities':{'dB_equals_p_zeta':True,'tH_equals_pcJ':True,'period_identity':True}})
    result={'passed':True,'primes':[3,5,7],'results':results,'runtime_seconds':time.perf_counter()-start}
    dest=Path(__file__).resolve().parents[1]/'logs/B_odd_prime_second_repair_certificate.json'
    dest.write_text(json.dumps(result,default=str,indent=2)+'\n')
    print(json.dumps({'passed':True,'primes':result['primes'],'weight_cases':[len(r['weight_cases']) for r in results],
                      'determinants':[r['determinants'] for r in results],'runtime_seconds':result['runtime_seconds']},default=str))


if __name__=='__main__':main()
