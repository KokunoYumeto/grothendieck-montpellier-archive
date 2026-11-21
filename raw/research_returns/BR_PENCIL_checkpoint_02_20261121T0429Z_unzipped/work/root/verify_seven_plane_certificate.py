#!/usr/bin/env python3
"""Independent exact verifier for the signed seven-plane obstructions.

Uses NumPy only for integer arrays and modular arithmetic; no floating point,
rank oracle, symbolic nullspace, or import from the certificate generator.
Every product is reduced modulo a prime <2^20, hence fits in int64.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import argparse,json,math,time
import numpy as np

PAIRS=list(combinations(range(4),2))
RECTS=[(I,J) for I in PAIRS for J in PAIRS]


def var_weight(v):
    r,c=divmod(v,4)
    return tuple(int(x==r) for x in range(4))+tuple(int(x==c) for x in range(4))


def quad_weight(q):
    I,J=RECTS[q]
    return tuple(int(x in I) for x in range(4))+tuple(int(x in J) for x in range(4))


def reconstruct(S,sign):
    assert sign in (-1,1)
    variables=sorted({4*r+c for q in S for r in RECTS[q][0] for c in RECTS[q][1]})
    ix={v:i for i,v in enumerate(variables)}
    T=np.zeros((len(S),len(variables),len(variables)),dtype=np.int64)
    for h,q in enumerate(S):
        (r,s),(c,d)=RECTS[q]
        a,b,x,y=[ix[z] for z in [4*r+c,4*r+d,4*s+c,4*s+d]]
        for i,j,value in [(a,y,1),(y,a,1),(b,x,sign),(x,b,sign)]:
            T[h,i,j]=value
    classes=defaultdict(list)
    for h,q in enumerate(S):
        for i,v in enumerate(variables):
            w=tuple(x-y for x,y in zip(var_weight(v),quad_weight(q)))
            classes[w].append((h,i))
    image={tuple(-x for x in var_weight(v)):i for i,v in enumerate(variables)}
    blocks=[{'weight':list(w),'coordinates':[list(c) for c in coords],
             'quotient_dimension':len(coords)-(w in image)}
            for w,coords in classes.items() if len(coords)-(w in image)>0]
    return variables,T,blocks,image


def extended_basis(T,blocks,image,chosen):
    omitted={image.get(tuple(blocks[i]['weight'])) for i in chosen}
    basis=[T[:,:,c].copy() for c in range(T.shape[2]) if c not in omitted]
    for i in chosen:
        for q,v in blocks[i]['coordinates']:
            m=np.zeros(T.shape[:2],dtype=np.int64);m[q,v]=1;basis.append(m)
    return basis


def wedge_submatrix(basis,orientation,rows,cols):
    """Rebuild only the requested entries, from the exterior-map definition."""
    arrays=np.array(basis,dtype=np.int64)
    if orientation=='A':arrays=arrays.transpose((0,2,1))
    ell,other,factor=arrays.shape
    wedges=list(combinations(range(factor),2))
    assert all(0<=r<other*len(wedges) for r in rows)
    assert all(0<=c<ell*factor for c in cols)
    selected=np.array(cols,dtype=np.int64)
    s=selected//factor
    v=selected%factor
    out=np.zeros((len(rows),len(cols)),dtype=np.int64)
    for h,row in enumerate(rows):
        q,pair=divmod(row,len(wedges))
        i,j=wedges[pair]
        out[h,:]=(v==j)*arrays[s,q,i]-(v==i)*arrays[s,q,j]
    return out


def rank_mod(matrix,p):
    a=np.array(matrix,dtype=np.int64,copy=True)%p
    nr,nc=a.shape;r=0
    for c in range(nc):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        rr=r+int(nz[0])
        if rr!=r:a[[r,rr]]=a[[rr,r]]
        a[r,c:]=a[r,c:]*pow(int(a[r,c]),-1,p)%p
        inds=np.flatnonzero(a[r+1:,c])+r+1
        if len(inds):a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[r,c:])%p
        r+=1
        if r==nr:break
    return r


def det_mod(matrix,p):
    a=np.array(matrix,dtype=np.int64,copy=True)%p
    assert a.shape[0]==a.shape[1]
    n=a.shape[0];value=1
    for k in range(n):
        nz=np.flatnonzero(a[k:,k])
        if not len(nz):return 0
        r=k+int(nz[0])
        if r!=k:a[[k,r]]=a[[r,k]];value=-value
        pivot=int(a[k,k]);value=value*pivot%p
        a[k,k:]=a[k,k:]*pow(pivot,-1,p)%p
        inds=np.flatnonzero(a[k+1:,k])+k+1
        if len(inds):a[inds,k:]=(a[inds,k:]-a[inds,k,None]*a[k,k:])%p
    return value%p


def check_minor(basis,c,p):
    order=c['minor_order']
    assert len(c['rows'])==len(c['cols'])==order
    assert len(set(c['rows']))==len(set(c['cols']))==order
    M=wedge_submatrix(basis,c['orientation'],c['rows'],c['cols'])
    value=det_mod(M,p)
    assert value==c['determinant_mod_p']!=0


def check_line(T,block,image,line,p):
    coordinates=block['coordinates']
    params=coordinates[:-1] if tuple(block['weight']) in image else coordinates
    assert params==line['parameter_coordinates']
    dim=len(params)
    assert dim==block['quotient_dimension']==line['quotient_dimension']
    assert line['weight']==block['weight']
    U=[T[:,:,c].copy() for c in range(T.shape[2])]
    for q,v in line.get('extra_base_coordinates',[]):
        extra=np.zeros(T.shape[:2],dtype=np.int64);extra[q,v]=1;U.append(extra)
    X=[]
    for q,v in params:
        m=np.zeros(T.shape[:2],dtype=np.int64);m[q,v]=1;X.append(m)
    orientation=line['orientation']
    factor=T.shape[0] if orientation=='A' else T.shape[1]
    assert len(line['conditions'])==factor
    conditions=[]
    for j,c in enumerate(line['conditions']):
        assert c['factor_index']==j
        rows=c['output_rows']
        ann=np.array(c['annihilator'],dtype=np.int64).reshape((len(c['annihilator']),len(rows)))
        assert np.max(np.abs(ann),initial=0)<=1000
        assert len(rows)<1000
        # These unreduced integer products have absolute values <10^6.
        M0=wedge_submatrix(U,orientation,rows,list(range(len(U)*factor)))
        assert not np.any(ann@M0)
        Z=wedge_submatrix(X,orientation,rows,[s*factor+j for s in range(dim)])
        conditions.append(ann@Z)
    zero_count=line['forbidden_zero_subset_size']
    assert zero_count==factor-line['minimum_increment']+1
    checked=0
    for zeros in combinations(range(factor),zero_count):
        equations=np.concatenate([conditions[j] for j in zeros],axis=0)
        assert rank_mod(equations,p)==dim
        checked+=1
    return checked


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('per7_m12_certificate.json'))
    args=parser.parse_args()
    path=args.certificate
    proof=json.loads(path.read_text())
    p=proof['prime']
    assert p<2**20 and all(p%d for d in range(2,math.isqrt(p)+1))
    start=time.time();summaries=[]
    for case in proof['cases']:
        S=case['subset'];variables,T,blocks,image=reconstruct(S,case['sign'])
        assert variables==case['variables'] and blocks==case['blocks']
        assert len(S)==7 and case['r_excluded']==13
        q=13-len(variables)
        assert q==case['quotient_dimension']
        U=[T[:,:,c].copy() for c in range(len(variables))]
        check_minor(U,case['base_rank_certificate'],p)
        completed=set()
        for record in case['saturation_certificates']:
            chosen=tuple(record['chosen'])
            assert chosen not in completed
            basis=extended_basis(T,blocks,image,chosen)
            c=record['certificate']
            factor=T.shape[0] if c['orientation']=='A' else T.shape[1]
            assert c['minor_order']==len(basis)*factor-12
            check_minor(basis,c,p)
            completed.add(chosen)
        line_checks=0
        for index,line in case['line_certificates'].items():
            line_checks+=check_line(T,blocks[int(index)],image,line,p)
        if q==1:
            allchoices={(i,) for i in range(len(blocks))}
            for chosen in allchoices-completed:
                i=chosen[0];line=case['line_certificates'][str(i)]
                orientation=line['orientation']
                assert case['base_rank_certificate']['orientation']==orientation
                lower=case['base_rank_certificate']['minor_order']+line['minimum_increment']
                factor=len(S) if orientation=='A' else len(variables)
                assert lower>(factor-1)*13
                completed.add(chosen)
        else:
            assert q==2
            allchoices={(i,) for i,b in enumerate(blocks) if b['quotient_dimension']>=2}
            allchoices.update(combinations(range(len(blocks)),2))
            aw=[tuple(-x for x in quad_weight(z)) for z in S]
            supplied={tuple(x['pair']):x for x in case['pair_increment_checks']}
            conditioned={tuple(x['pair']):x for x in case.get('conditioned_pair_checks',[])}
            for chosen in allchoices-completed:
                assert len(chosen)==2
                if chosen in conditioned:
                    record=conditioned[chosen]
                    fixed,variable=record['fixed_index'],record['variable_index']
                    assert set(chosen)=={fixed,variable}
                    assert blocks[fixed]['quotient_dimension']==1
                    assert blocks[fixed]['weight']!=blocks[variable]['weight']
                    coordinates=blocks[fixed]['coordinates']
                    params=coordinates[:-1] if tuple(blocks[fixed]['weight']) in image else coordinates
                    assert len(params)==1 and params[0]==record['fixed_coordinate']
                    base=U.copy()
                    extra=np.zeros(T.shape[:2],dtype=np.int64)
                    extra[tuple(record['fixed_coordinate'])]=1;base.append(extra)
                    check_minor(base,record['base_rank_certificate'],p)
                    line=record['line_certificate']
                    assert line.get('extra_base_coordinates')==[record['fixed_coordinate']]
                    line_checks+=check_line(T,blocks[variable],image,line,p)
                    orientation=line['orientation']
                    assert record['base_rank_certificate']['orientation']==orientation
                    factor=len(S) if orientation=='A' else len(variables)
                    assert record['base_rank_certificate']['minor_order']+line['minimum_increment']>(factor-1)*13
                    completed.add(chosen)
                    continue
                assert chosen in supplied
                i,j=chosen
                left,right=case['line_certificates'][str(i)],case['line_certificates'][str(j)]
                assert left['orientation']==right['orientation']=='A'
                wi,wj=blocks[i]['weight'],blocks[j]['weight']
                weights_i={tuple(x+y for x,y in zip(wi,a)) for a in aw}
                weights_j={tuple(x+y for x,y in zip(wj,a)) for a in aw}
                overlap=len(weights_i&weights_j)
                lower=left['minimum_increment']+right['minimum_increment']-overlap
                assert overlap==supplied[chosen]['overlapping_A_weights']
                assert lower==supplied[chosen]['lower_A_increment']
                assert case['base_rank_certificate']['minor_order']+lower>6*13
                completed.add(chosen)
        assert completed==allchoices
        result={'case':case['name'],'subset':S,'torus_choices_excluded':len(completed),
                'saturation_minors_verified':len(case['saturation_certificates']),
                'linear_zero_patterns_verified':line_checks,
                'border_rank_lower_bound':14,'field_scope':'characteristic zero','status':'PASS'}
        summaries.append(result)
        print(json.dumps(result),flush=True)
    output={'results':summaries,'seconds':time.time()-start,
            'method':'exact modular minors plus exact integer annihilator identities; no floating point'}
    out=path.with_name(path.stem.replace('_certificate','_verification')+'.json')
    out.write_text(json.dumps(output,indent=2)+'\n')
    print('PASS',out,'seconds',time.time()-start)


if __name__=='__main__':main()
