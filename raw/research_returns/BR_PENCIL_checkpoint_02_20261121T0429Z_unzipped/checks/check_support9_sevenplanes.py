#!/usr/bin/env python3
"""Self-contained exact characteristic-zero certificate for the three P-15 tensors.

Dependencies: Python standard library, NumPy and SymPy.  No input data or other
project code is imported.  Every tensor, quotient map and finite arrangement
is reconstructed from the seven rectangles printed below.  All ranks and
kernel equations use exact rational arithmetic; no finite-field or numerical
rank decisions are used.  The script exits unsuccessfully on any survivor.
"""
from collections import defaultdict,Counter
from datetime import datetime,timezone
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations,product
from math import gcd,lcm
from pathlib import Path
import json,time
import numpy as np
from sympy import Matrix

RECTANGLES=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),
            ((0,2),(0,1)),((0,2),(0,2)),((0,2),(1,2)),
            ((1,2),(0,1))]
A_DIM=7
B_DIM=9
R_TEST=13
SIGN=-1
LIMITS={'A':16,'B':24}
COUNTS=Counter()


def primitive(values):
    values=list(values)
    denominator=1
    for v in values:denominator=lcm(denominator,int(v.q) if hasattr(v,'q') else Fraction(v).denominator)
    integers=[int(v*denominator) for v in values]
    divisor=0
    for v in integers:divisor=gcd(divisor,v)
    if not divisor:return ()
    integers=[v//abs(divisor) for v in integers]
    if next(v for v in integers if v)<0:integers=[-v for v in integers]
    return tuple(integers)


def integer_rows(M):
    return tuple(row for row in (primitive(M.row(i)) for i in range(M.rows)) if row)


@lru_cache(None)
def row_span(rows,d):
    if not rows:return ()
    R,pivots=Matrix(rows).rref()
    return tuple(primitive(R.row(i)) for i in range(len(pivots)))


def rank_q(M):
    """Small exact rank computation over Q, independently of SymPy rank."""
    rows=[[Fraction(int(x)) if isinstance(x,(int,np.integer)) else Fraction(str(x)) for x in row] for row in M]
    if not rows:return 0
    r=0
    for c in range(len(rows[0])):
        pivot=next((i for i in range(r,len(rows)) if rows[i][c]),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        v=rows[r][c];rows[r]=[x/v for x in rows[r]]
        for i in range(r+1,len(rows)):
            if rows[i][c]:
                v=rows[i][c];rows[i]=[x-v*y for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==len(rows):break
    return r


def arrangements(conditions,d):
    """All exact simultaneous zero patterns of linear maps on P^(d-1)."""
    spaces={()}
    for C in conditions:
        new=set()
        for E in spaces:
            F=row_span(E+C,d)
            if len(F)<d:new.add(F)
        spaces.update(new)
    states=[]
    for E in sorted(spaces):
        zeros=frozenset(j for j,C in enumerate(conditions) if len(row_span(E+C,d))==len(E))
        null=Matrix(E).nullspace() if E else [Matrix.eye(d)[:,i] for i in range(d)]
        basis=tuple(primitive(v) for v in null)
        assert len(basis)==d-len(E)
        K=Matrix.hstack(*(Matrix(v) for v in basis))
        EQ=Matrix(E) if E else Matrix.zeros(0,d)
        assert EQ*K==Matrix.zeros(EQ.rows,K.cols) and rank_q(K.tolist())==K.cols
        states.append({'equations':E,'zero_columns':zeros,'basis':basis,'dimension':len(basis)})
    return states


def var_weight(v):
    i,j=divmod(v,3)
    return tuple(int(k==i) for k in range(3))+tuple(int(k==j) for k in range(3))


def quad_weight(rect):
    I,J=rect
    return tuple(int(k in I) for k in range(3))+tuple(int(k in J) for k in range(3))


def add_weight(a,b):return tuple(x+y for x,y in zip(a,b))


def wedge_matrix(basis,orientation):
    matrices=basis if orientation=='B' else [M.T for M in basis]
    n1,n2=matrices[0].shape
    pairs=list(combinations(range(n2),2))
    out=np.zeros((n1*len(pairs),len(basis)*n2),dtype=np.int64)
    for p,(i,j) in enumerate(pairs):
        for q in range(n1):
            for s,L in enumerate(matrices):
                out[q*len(pairs)+p,s*n2+j]=L[q,i]
                out[q*len(pairs)+p,s*n2+i]=-L[q,j]
    return out


def construct():
    T=np.zeros((7,9,9),dtype=np.int64)
    for q,((r,s),(c,d)) in enumerate(RECTANGLES):
        a,b,x,y=3*r+c,3*r+d,3*s+c,3*s+d
        for i,j,v in [(a,y,1),(y,a,1),(b,x,SIGN),(x,b,SIGN)]:T[q,i,j]=v
    U=[T[:,:,c] for c in range(9)]
    assert rank_q(np.stack(U,axis=-1).reshape(63,9).tolist())==9
    classes=defaultdict(list)
    for q,rect in enumerate(RECTANGLES):
        for v in range(9):
            w=tuple(x-y for x,y in zip(var_weight(v),quad_weight(rect)))
            classes[w].append((q,v))
    image={tuple(-x for x in var_weight(v)):v for v in range(9)}
    blocks=[(w,coords,len(coords)-int(w in image)) for w,coords in classes.items() if len(coords)-int(w in image)]
    assert len(blocks) in [33,34] and sum(d for w,c,d in blocks)==54 and max(d for w,c,d in blocks)==3
    basis=list(U);weights=[tuple(-x for x in var_weight(v)) for v in range(9)];owners=[-1]*9;starts={}
    for i,(w,coords,d) in enumerate(blocks):
        starts[i]=len(basis)
        if w in image:
            assert U[image[w]][coords[-1]]!=0
            params=coords[:-1]
        else:params=coords
        assert len(params)==d
        for q,v in params:
            M=np.zeros((7,9),dtype=np.int64);M[q,v]=1
            basis.append(M);weights.append(w);owners.append(i)
    assert len(basis)==63
    allmaps={};saturation={};summary={}
    for orientation,fw in [('A',[tuple(-x for x in quad_weight(q)) for q in RECTANGLES]),('B',[var_weight(v) for v in range(9)])]:
        nf=len(fw);M=wedge_matrix(basis,orientation);groups=defaultdict(list)
        for j,w in enumerate(weights):
            for k,u in enumerate(fw):groups[add_weight(w,u)].append(j*nf+k)
        ranktables=[];quotients={};base_rank=0;rowsets=[]
        for w,cols in groups.items():
            rows=list(map(int,np.flatnonzero(np.any(M[:,cols],axis=1))))
            rowsets.append(set(rows))
            local=M[np.ix_(rows,cols)]
            localowners=[owners[c//nf] for c in cols]
            optional=sorted(set(localowners)-{-1});index={a:i for i,a in enumerate(optional)}
            baselinecols=[c for c in cols if c//nf<9]
            B=Matrix(M[np.ix_(rows,baselinecols)].tolist()) if baselinecols else Matrix.zeros(len(rows),0)
            br=rank_q(B.tolist());assert br==len(B.rref()[1]);base_rank+=br
            null=B.T.nullspace();H=Matrix([primitive(v) for v in null]) if null else Matrix.zeros(0,len(rows))
            assert H*B==Matrix.zeros(H.rows,B.cols)
            assert rank_q(H.tolist())==H.rows
            assert H.rows==len(rows)-br
            quotients[w]=(rows,H)
            lookup={}
            for k in range(min(4,len(optional))+1):
                for chosen in combinations(range(len(optional)),k):
                    mask=sum(1<<i for i in chosen)
                    cs=[j for j,o in enumerate(localowners) if o<0 or mask>>index[o]&1]
                    lookup[mask]=len(cs)-rank_q(local[:,cs].tolist())
            ranktables.append((tuple(optional),lookup))
        assert set.union(*rowsets)==set(range(M.shape[0]))
        assert sum(map(len,rowsets))==M.shape[0]
        expected=62 if orientation=='A' else 80
        assert base_rank==expected
        line_maps={}
        for i,(w,coords,d) in enumerate(blocks):
            maps=[]
            for j,u in enumerate(fw):
                target=add_weight(w,u);rows,H=quotients[target]
                C=Matrix(M[np.ix_(rows,[(starts[i]+k)*nf+j for k in range(d)])].tolist()) if rows else Matrix.zeros(0,d)
                Q=H*C
                maps.append((target,Q))
            line_maps[i]=maps
        allmaps[orientation]=line_maps;saturation[orientation]=ranktables
        summary[orientation]={'full_matrix_shape':list(M.shape),'baseline_shape':[M.shape[0],9*nf],'baseline_rank':base_rank,'weight_blocks':len(groups),'saturation_patterns':sum(len(q) for _,q in ranktables)}
    return T,blocks,allmaps,saturation,summary


def saturated_nullity(tables,mask):
    return sum(table[sum(((mask>>j)&1)<<i for i,j in enumerate(optional))] for optional,table in tables)


def component_states(blocks,maps):
    weights={o:sorted({w for cols in maps[o].values() for w,Q in cols}) for o in ['A','B']}
    ids={o:{w:i for i,w in enumerate(weights[o])} for o in ['A','B']}
    components={}
    for i,(w,coords,d) in enumerate(blocks):
        raw=maps['A'][i]+maps['B'][i]
        for multiplicity in range(1,min(2,d)+1):
            if multiplicity==d:
                E=Matrix.eye(d)
                states=[{'dimension':0,'fixed_basis':E,'ranks':[rank_q(Q.tolist()) for _,Q in raw]}]
                conditions=[]
            else:
                conditions=[];base_drop=[]
                for target,Q in raw:
                    r=rank_q(Q.tolist())
                    if multiplicity==1:
                        conditions.append(integer_rows(Q));base_drop.append((int(r>0),int(r>0)))
                    else:
                        assert multiplicity==2 and d==3
                        if r==0:C=();bd=(0,0)
                        elif r==3:C=tuple(tuple(int(i==j) for j in range(3)) for i in range(3));bd=(2,0)
                        elif r==2:C=tuple(primitive(v) for v in Q.nullspace());bd=(2,1)
                        else:
                            row=next(Q.row(k) for k in range(Q.rows) if any(Q.row(k)))
                            C=tuple(primitive(v) for v in Matrix(row).nullspace());bd=(1,1)
                        conditions.append(C);base_drop.append(bd)
                states=arrangements(conditions,d)
                for st in states:
                    st['ranks']=[b-drop*int(j in st['zero_columns']) for j,(b,drop) in enumerate(base_drop)]
                    if st['dimension']==1:
                        v=st['basis'][0]
                        E=Matrix(v) if multiplicity==1 else Matrix.hstack(*(Matrix(primitive(u)) for u in Matrix([v]).nullspace()))
                        st['fixed_basis']=E
            for st in states:
                for o,offset,n in [('A',0,7),('B',7,9)]:
                    st[o+'_active']=frozenset(raw[offset+j][0] for j in range(n) if st['ranks'][offset+j])
                    for level in [1,2]:st[o+'_mask'+str(level)]=sum(1<<ids[o][raw[offset+j][0]] for j in range(n) if st['ranks'][offset+j]>=level)
            components[i,multiplicity]={'dimension':d,'multiplicity':multiplicity,'states':states,'conditions':conditions}
    return components


def fixed_data(maps,components,choices):
    spaces={};increments={}
    for o in ['A','B']:
        byweight=defaultdict(list)
        for i,m,s in choices:
            E=components[i,m]['states'][s]['fixed_basis']
            for w,Q in maps[o][i]:
                V=Q*E
                byweight[w].extend(list(V.columnspace()))
        increments[o]=0;spaces[o]={}
        for w,cols in byweight.items():
            F=Matrix.hstack(*cols) if cols else Matrix.zeros(0,0)
            if cols:
                r=rank_q(F.tolist());increments[o]+=r
                null=F.T.nullspace();H=Matrix([primitive(v) for v in null]) if null else Matrix.zeros(0,F.rows)
                assert H*F==Matrix.zeros(H.rows,F.cols) and rank_q(H.tolist())==H.rows and H.rows==F.rows-r
                spaces[o][w]=H
        # Missing weights have the identity quotient.
    return spaces,increments


def quotient_line_states(maps,components,choice,spaces):
    i,m,s=choice;assert m==1
    old=components[i,m]['states'][s]
    K=Matrix.hstack(*(Matrix(v) for v in old['basis']));d=K.cols
    conditions=[];oldmaps=[];newmaps=[]
    for o in ['A','B']:
        for w,Q in maps[o][i]:
            P=Q*K;oldmaps.append(P)
            if w in spaces[o]:P=spaces[o][w]*P
            conditions.append(integer_rows(P));newmaps.append((o,w,P))
    states=[]
    for st in arrangements(conditions,d):
        KP=Matrix.hstack(*(Matrix(v) for v in st['basis']))
        if any(j not in old['zero_columns'] and oldmaps[j]*KP==Matrix.zeros(oldmaps[j].rows,KP.cols) for j in range(16)):continue
        active={'A':set(),'B':set()}
        for j,(o,w,Q) in enumerate(newmaps):
            if j not in st['zero_columns']:active[o].add(w)
        states.append({'active':active,'dimension':KP.cols})
    return states


def check_four_lines(maps,components,indices):
    # Cheap valid lower bound: sum individual minima minus the maximum
    # possible loss due to repeated output weights.
    for o in ['A','B']:
        allweights=[w for i in indices for w,Q in maps[o][i]]
        overlap=len(allweights)-len(set(allweights))
        lower=sum(min(len(s[o+'_active']) for s in components[i,1]['states']) for i in indices)-overlap
        if lower>LIMITS[o]:COUNTS['four_supports_minimum_overlap_excluded']+=1;return
    COUNTS['four_supports_after_minimum_overlap']+=1
    any_joint=False
    for state_indices in product(*(range(len(components[i,1]['states'])) for i in indices)):
        choices=tuple((i,1,s) for i,s in zip(indices,state_indices))
        states=[components[i,1]['states'][s] for i,s in zip(indices,state_indices)]
        if any(len(set.union(*(set(st[o+'_active']) for st in states)))>LIMITS[o] for o in ['A','B']):continue
        any_joint=True;COUNTS['four_joint_states']+=1
        fixed=tuple(c for c,st in zip(choices,states) if 'fixed_basis' in st)
        free=tuple(c for c,st in zip(choices,states) if 'fixed_basis' not in st)
        spaces,inc=fixed_data(maps,components,fixed)
        if any(inc[o]>LIMITS[o] for o in ['A','B']):COUNTS['four_states_fixed_rank_excluded']+=1;continue
        assert len(free) in [1,2],('Fixed admissible extension or too many free lines',choices,len(free),inc)
        remaining={o:LIMITS[o]-inc[o] for o in ['A','B']}
        refined=[quotient_line_states(maps,components,c,spaces) for c in free]
        if len(free)==1:
            COUNTS['four_one_free_states']+=1
            for st in refined[0]:
                assert any(len(st['active'][o])>remaining[o] for o in ['A','B']),('One-line survivor',choices,remaining)
            COUNTS['four_one_free_excluded']+=1
        else:
            COUNTS['four_two_free_states']+=1
            for a,b in product(*refined):
                COUNTS['four_two_free_pairs']+=1
                assert any(len(a['active'][o]|b['active'][o])>remaining[o] for o in ['A','B']),('Two-line survivor',choices,remaining)
            COUNTS['four_two_free_excluded']+=1
    if not any_joint:COUNTS['four_supports_joint_union_excluded']+=1


def check_three_weights(maps,components,indices):
    for doubled in indices:
        if (doubled,2) not in components:continue
        keys=[(i,2 if i==doubled else 1) for i in indices]
        for state_indices in product(*(range(len(components[k]['states'])) for k in keys)):
            COUNTS['three_weight_arrangement_states']+=1
            masks=[0,0,0,0]
            for key,s in zip(keys,state_indices):
                st=components[key]['states'][s]
                for j,name in enumerate(['A_mask1','A_mask2','B_mask1','B_mask2']):masks[j]|=st[name]
            bounds={'A':masks[0].bit_count()+masks[1].bit_count(),'B':masks[2].bit_count()+masks[3].bit_count()}
            assert any(bounds[o]>LIMITS[o] for o in ['A','B']),('Three-weight survivor',indices,doubled,state_indices,bounds)
            COUNTS['three_weight_arrangement_excluded']+=1


def check_case(label,rectangles,sign,expected):
    global RECTANGLES,SIGN
    RECTANGLES=rectangles;SIGN=sign;COUNTS.clear()
    start=time.time();T,blocks,maps,tables,summary=construct()
    components=component_states(blocks,maps)
    saturated=[]
    for size in range(1,5):
        for indices in combinations(range(len(blocks)),size):
            if sum(blocks[i][2] for i in indices)<4:continue
            COUNTS['supports_tested']+=1
            mask=sum(1<<i for i in indices)
            nullities={o:saturated_nullity(tables[o],mask) for o in ['A','B']}
            if min(nullities.values())<13:COUNTS['supports_saturation_excluded']+=1;continue
            COUNTS['supports_after_saturation']+=1;COUNTS['saturated_support_size_'+str(size)]+=1
            saturated.append(indices)
    for key in ['supports_tested','supports_after_saturation','saturated_support_size_3','saturated_support_size_4']:
        assert COUNTS[key]==expected[key],(label,key,COUNTS[key],expected[key])
    for number,indices in enumerate(saturated):
        if len(indices)==3:check_three_weights(maps,components,indices)
        else:assert len(indices)==4;check_four_lines(maps,components,indices)
    for key,value in expected.items():assert COUNTS[key]==value,(key,COUNTS[key],value)
    source=Path(__file__).read_bytes()
    report={'status':'PASS','statement':'P-15: the specified seven-plane tensor has border rank at least14 in characteristic zero','case':label,'sign':sign,
            'rectangles':RECTANGLES,'dimensions':[7,9,9],'tested_border_rank':13,
            'quotient_weight_count':len(blocks),'quotient_capacities':[d for w,c,d in blocks],
            'matrix_summary':summary,'counts':dict(COUNTS),'exact_arithmetic':'rational; no numerical or finite-field rank decisions',
            'script_sha256':sha256(source).hexdigest(),'utc':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),'seconds':time.time()-start}
    Path(__file__).with_name('support9_'+label+'_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return report

def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--case',choices=['all','det','perA','perB'],default='all')
    args=parser.parse_args()
    rectangles_A=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),((0,2),(0,1)),((0,2),(0,2)),((0,2),(1,2)),((1,2),(0,1))]
    rectangles_B=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),((0,2),(0,1)),((0,2),(0,2)),((1,2),(0,1)),((1,2),(1,2))]
    keys=['supports_tested','supports_after_saturation','saturated_support_size_3','saturated_support_size_4',
          'four_supports_minimum_overlap_excluded','four_supports_after_minimum_overlap',
          'four_supports_joint_union_excluded','four_joint_states','four_states_fixed_rank_excluded',
          'four_one_free_states','four_one_free_excluded','four_two_free_states','four_two_free_pairs',
          'four_two_free_excluded','three_weight_arrangement_states','three_weight_arrangement_excluded']
    values={
        'det':[46119,13255,236,13019,12307,712,176,7225,6619,592,592,14,32,14,42274,42274],
        'perA':[46119,13762,244,13518,12798,720,180,7697,7057,626,626,14,22,14,45489,45489],
        'perB':[51985,11983,200,11783,11519,264,36,2182,1972,210,210,0,0,0,31796,31796]}
    for label in ['det','perA','perB']:
        if args.case not in ['all',label]:continue
        check_case(label,rectangles_B if label=='perB' else rectangles_A,-1 if label=='det' else 1,dict(zip(keys,values[label])))

if __name__=='__main__':main()
