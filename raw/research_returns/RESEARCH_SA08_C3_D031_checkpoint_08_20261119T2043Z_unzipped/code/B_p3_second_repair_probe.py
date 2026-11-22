#!/usr/bin/env python3
"""Exact arity-two H3 torsion probe for the p=3 deep tail.

Only total unshifted weights <=13 are certified here. Every W0
factor then has unshifted weight <=9, where A-P01 specifies the
complete coefficient resolution. The target embeds saturatedly
in a free lattice by d:W0 -> W1, so nonunit factors of d2 are
exact H3 torsion factors, independently of the unused d3 rows.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import time
import sympy as sp

from A_cosimplicial_deep_tail_certificate import Resolution, kernel, smith, vp


def add(out, key, value):
    if value:
        out[key] += value
        if not out[key]:
            del out[key]


class Tail:
    def __init__(self):
        self.res = Resolution(3)
        self.gens = {}
        self.by_degree = defaultdict(list)
        for kind, top in [('u', 5), ('v', 4)]:
            for level in range(top):
                degree = top-level
                for name, wt in self.res.gens[level]:
                    label = f'{kind}:{level}:{name}'
                    self.gens[label] = (degree, wt, kind, level, name)
                    self.by_degree[degree].append(label)

    def differential(self, label):
        degree, wt, kind, level, name = self.gens[label]
        result = []
        if kind == 'v':
            target = f'u:{level}:{name}'
            result.append((target, 0, F(3)))
        if level:
            for target_name, value in self.res.data[level][name].items():
                target = f'{kind}:{level-1}:{target_name}'
                tw = self.gens[target][1]
                result.append((target, wt-tw, value if kind == 'v' else -value))
        return result

    def zero_basis(self, weight):
        source, _, matrix = self.res.w_d1(weight)
        if not source:
            return []
        basis = kernel(matrix, len(source), 3)
        rank = len(basis[0]) if basis else 0
        answer = []
        for j in range(rank):
            answer.append({f'{kind}:{level}:{name}': (weight-wt, basis[i][j])
                           for i, (kind, level, name, wt) in enumerate(source)
                           if basis[i][j]})
        return answer

    def d2(self, weight):
        inputs, columns = [], []
        ones = self.by_degree[1]
        for i, first in enumerate(ones):
            for second in ones[i+1:]:
                k = weight-self.gens[first][1]-self.gens[second][1]
                if k < 0:
                    continue
                inputs.append({'type':'odd_pair', 'first':first, 'second':second, 'coefficient_weight':k})
                column = defaultdict(F)
                for target,l,a in self.differential(first):
                    add(column, ('positive', second, target, k+l), a*comb(k+l,k))
                for target,l,a in self.differential(second):
                    add(column, ('positive', first, target, k+l), -a*comb(k+l,k))
                columns.append(dict(column))
        for even in self.by_degree[2]:
            m = weight-self.gens[even][1]
            if m < 0:
                continue
            assert m <= 9, (weight, even, m)
            for zero in self.zero_basis(m):
                inputs.append({'type':'zero_even','zero_weight':m,'zero_derivative':zero,'even':even})
                column = defaultdict(F)
                for one,(k,a) in zero.items():
                    add(column, ('positive',one,even,k), a)
                    for target,l,b in self.differential(even):
                        add(column, ('zero_embedding',one,target,k+l), a*b*comb(k+l,k))
                columns.append(dict(column))
        rows = sorted(set().union(*(set(c) for c in columns))) if columns else []
        matrix = [[c.get(row,F(0)) for c in columns] for row in rows]
        return inputs,rows,matrix


def main():
    start=time.perf_counter()
    tail=Tail()
    results=[]
    for w in range(1,14):
        inputs,rows,matrix=tail.d2(w)
        diagonal,change,rank=smith(matrix,len(inputs),3)
        torsion=[]
        for j in range(rank):
            exponent=vp(diagonal[j][j],3)
            if exponent:
                primitive=[change[i][j] for i in range(len(inputs))]
                image=[sum(a*b for a,b in zip(row,primitive)) for row in matrix]
                assert all(vp(a,3)>=exponent for a in image if a)
                torsion.append({'exponent':exponent,'primitive':primitive,
                                'cycle_in_saturated_embedding':[a/(3**exponent) for a in image]})
        results.append({'unshifted_weight':w,'degree2_rank':len(inputs),
                        'ambient_degree3_rank':len(rows),'d2_rank':rank,
                        'torsion_exponents':[x['exponent'] for x in torsion],
                        'inputs':inputs,'rows':rows,'matrix':matrix,'torsion_witnesses':torsion})
        assert (rank,[x['exponent'] for x in torsion]) == ((5,[1]) if w==13 else ((1,[]) if w in (11,12) else (0,[])))
    # Natural source basis: Cr, gx, aH, aK, Cb, xy.
    inputs,rows,matrix=tail.d2(13)
    natural=[[row[2],row[0],-2*row[3],-2*row[4],row[5],row[1]] for row in matrix]
    g='u:4:q4_0'; ell='u:4:q4_1'; x='v:3:q3_0'; y='v:3:q3_1'
    r='u:3:q3_0'; sigma='u:3:q3_1'; a='v:2:q2_0'; b='v:2:q2_1'
    e='u:2:q2_0'; f='u:2:q2_1'; z='v:1:r0'; z1='v:1:r1'
    zero={
        'C':{g:(0,F(3)),x:(1,F(1)),y:(0,F(-6))},
        'H':{g:(2,F(-2)),ell:(0,F(6))},
        'K':{ell:(0,F(3)),x:(3,F(1)),y:(2,F(-2))},
        'J':{g:(3,F(-1)),ell:(1,F(1))}}
    def ze(out,zero_name,positive,k=0,scale=F(1)):
        for one,(l,c) in zero[zero_name].items():
            add(out,('zero_embedding',one,positive,k+l),scale*c*comb(k+l,k))
    zeta=defaultdict(F)
    for zn,positive,scale in [('K',e,1),('C',f,-1),('H',z1,-1),('J',z,1)]:
        ze(zeta,zn,positive,scale=F(scale))
    for one,two,scale in [(ell,a,1),(y,r,1),(x,sigma,-1),(g,b,-1)]:
        add(zeta,('positive',one,two,0),F(scale))
    b_vector=[F(-1,2),F(-1,2),F(1,2),F(0),F(0),F(0)]
    d_b={row:sum(v*c for v,c in zip(values,b_vector)) for row,values in zip(rows,natural)}
    assert all(d_b.get(row,0)==3*zeta.get(row,0) for row in set(d_b)|set(zeta))
    # The gb coefficient kills every degree-two boundary modulo3.
    detector=rows.index(('positive',g,b,0))
    assert all(vp(v,3)>=1 for v in natural[detector] if v)
    assert zeta[('positive',g,b,0)]==-1
    assert all(sum(v*c for v,c in zip(row,[1,1,-1,2,-2,2]))==0 for row in natural)
    five_keys=[('positive',g,a,2),('positive',x,r,1),('positive',x,a,3),
               ('positive',x,b,1),('positive',g,b,0)]
    five=sp.Matrix([natural[rows.index(k)][:5] for k in five_keys])
    det5=F(five.det())
    assert vp(det5,3)==1
    four=sp.Matrix([[natural[rows.index(k)][j] for j in [0,2,3,4]] for k in five_keys[:4]])
    det4=F(four.det())
    assert vp(det4,3)==0
    # Check tB=d(Cg/2)+3(aJ-gy-Csigma) in the saturated degree2 embedding.
    left=defaultdict(F)
    ze(left,'H',a,k=1,scale=F(1,2)); ze(left,'C',r,k=1,scale=F(-1,2))
    add(left,('odd_pair',g,x,1),F(-1,2))
    right=defaultdict(F)
    add(right,('odd_pair',g,x,1),F(-1,2))
    add(right,('odd_pair',g,y,0),F(3))
    ze(right,'C',r,k=1,scale=F(-1,2)); ze(right,'C',sigma,scale=F(3))
    ze(right,'J',a,scale=F(3))
    add(right,('odd_pair',g,y,0),F(-3)); ze(right,'C',sigma,scale=F(-3))
    assert dict(left)==dict(right)
    result={'prime':3,'scope':'complete W-arity2 H3 torsion in unshifted weights1..13; actual complete coefficient lattice through9; named dB=3zeta and period identities',
            'results':results,'named_degree2_basis':['Cr','gx','aH','aK','Cb','xy'],
            'named_degree2_matrix':natural,'degree3_embedding_rows':rows,
            'nonboundary_detector_row':natural[detector],
            'rank5_minor':five.tolist(),'rank5_determinant':det5,
            'rank4_minor':four.tolist(),'rank4_determinant':det4,
            'exact_identities':{'dB_equals_3zeta':True,'T_B_equals_d_Cg_half_plus_3_Q':True,
                                'd_xi_equals_zero':True},
            'runtime_seconds':time.perf_counter()-start}
    dest=Path(__file__).resolve().parents[1]/'logs/B_p3_second_repair_probe.json'
    dest.write_text(json.dumps(result,default=str,indent=2)+'\n')
    print(json.dumps({'results':[{'weight':r['unshifted_weight'],'domain_rank':r['degree2_rank'],
                                  'd2_rank':r['d2_rank'],'torsion':r['torsion_exponents']} for r in results],
                      'runtime_seconds':result['runtime_seconds']}))


if __name__=='__main__':
    main()
