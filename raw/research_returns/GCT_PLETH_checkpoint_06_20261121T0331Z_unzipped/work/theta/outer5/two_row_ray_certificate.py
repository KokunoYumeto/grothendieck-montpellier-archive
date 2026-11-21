#!/usr/bin/env python3
"""T044: independent exact Newton certificate for all two-row Q shapes.

The section module is H0(I^k(2k) S_(b+x,b) Q), x,b,k >= 0.
This certificate uses three separable Euler-character products, not the
ordinary-polynomial domination used in root G021. It retains compact exact
bounds, zero sets and hashes, rather than a 120-million-entry lookup table.
"""
from pathlib import Path
from math import comb
from itertools import product
import hashlib
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES=(1,10,15,20,20,30,24)
CHARACTERS=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),(5,1,1,-1,1,-1,0),
            (6,0,-2,0,0,0,1),(5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
            (1,-1,1,1,-1,-1,1))
WEIGHTS=tuple(tuple(s*c for s,c in zip(SIZES,row)) for row in CHARACTERS)


def h(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n*n+4*n+4-(n%2))//4
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    if g==6:return (1,-1,0,0,0)[n%5]
    raise ValueError(g)


def schur_terms(g,x,b):
    a=b+x
    H=lambda n:h(g,n)
    return (H(a)*H(b)-H(a+1)*H(b-1),
            H(a-1)*H(b)-H(a+1)*H(b-2),
            H(a-1)*H(b-1)-H(a)*H(b-2))


def scalar_terms(g,k):
    jet=CLASSES[g].count(1)*h(g,k-1)
    return (h(g,2*k)-jet,h(g,2*k-1)-jet,h(g,2*k-2)-jet)


def trace(g,x,b,k):
    A,B,C=schur_terms(g,x,b)
    X,Y,Z=scalar_terms(g,k)
    return A*X-B*Y+C*Z


def multiplicity(label,x,b,k):
    row=WEIGHTS[LABELS.index(tuple(label))]
    num=sum(w*trace(g,x,b,k) for g,w in enumerate(row))
    assert num%120==0
    return num//120


def pair_line_correction(g,x,b):
    """Ind_(S2 x S3)^S5(sign2 x det(h3)^b Sym^x h3)."""
    if g==0:return 10*(x+1)
    if g==1:return 3*(-1)**b*int(x%2==0)-(x+1)
    if g==2:return -2*(-1)**b*int(x%2==0)
    if g==3:return (1,-1,0)[x%3]
    if g==4:return -(1,-1,0)[x%3]
    return 0


def fixed_constant(label,residues,orders):
    rx,rb,rk=residues;i,j,l=orders
    return sum((-1)**(i+j+l-u-v-w)*comb(i,u)*comb(j,v)*comb(l,w)
               *multiplicity(label,rx+60*u,rb+60*v,rk+60*w)
               for u in range(i+1) for v in range(j+1) for w in range(l+1))


def main(point_shift=0,degree_shift=0,statement='T-044',prefix='TWO_ROW_RAY',
         with_pair_correction=False,b_shift=0,correction_kind=None):
    correction_kind=correction_kind or ('two' if with_pair_correction else None)
    def correction_trace(g,x,b):
        if correction_kind=='two':return pair_line_correction(g,x,b)
        if correction_kind=='three_positive_b':
            if g==0:return 60*(x+1)
            if g==1:return 6*(-1)**b*int(x%2==0)
        return 0
    # Independently verify all seven closed h formulas against the cycle
    # generating functions, through every index this calculation will use.
    for g,cyc in enumerate(CLASSES):
        raw=[1]+[0]*600
        for ell in cyc:
            for n in range(ell,len(raw)):raw[n]+=raw[n-ell]
        assert all(h(g,n)==raw[n]-(raw[n-1] if n else 0) for n in range(601))

    x,b,k=sp.symbols('x b k');actual_b=b+b_shift;a=actual_b+x;kp=k+point_shift;c=2*k+degree_shift
    H=lambda n:(n+1)*(n+2)*(n+3)/6
    S0=H(a)*H(actual_b)-H(a+1)*H(actual_b-1)
    S1=H(a-1)*H(actual_b)-H(a+1)*H(actual_b-2)
    S2=H(a-1)*H(actual_b-1)-H(a)*H(actual_b-2)
    identity=S0*(H(c)-5*H(kp-1))-S1*(H(c-1)-5*H(kp-1))+S2*(H(c-2)-5*H(kp-1))
    P=(x+1)*(actual_b+x+2)*(actual_b+1)*((c+1)*(actual_b+c+2)*(actual_b+x+c+3)-5*kp*(kp+1)*(kp+2))
    identity+=correction_trace(0,x,actual_b);P+=12*correction_trace(0,x,actual_b)
    assert sp.expand(12*identity-P)==0
    terms=[(tuple(e),int(v)) for e,v in sp.Poly(P,x,b,k).terms()]
    assert all(v>0 for e,v in terms)
    assert max(map(sum,(e for e,v in terms)))==6
    assert tuple(max(e[j] for e,v in terms) for j in range(3))==(3,4,3)

    # Exact polynomial identities, rather than finite sampling, prove the
    # nonidentity degree bounds on every phase. All h arguments are >=-2,
    # where these polynomial extensions equal the required zero convention.
    phase_bounds=[]
    for g,modulus,bound in ((1,2,3),(2,2,3),(3,3,1)):
        for phase in product(range(modulus),repeat=3):
            substitution=dict(zip((x,b,k),phase))
            def HP(n):
                n=sp.sympify(n);r=int(n.subs(substitution))%modulus
                if g==1:return (n*n+4*n+4-r)/4
                if g==2:return sp.Integer(0) if r else (n+2)/2
                return (n+3-r)/3
            A=HP(a)*HP(actual_b)-HP(a+1)*HP(actual_b-1)
            B=HP(a-1)*HP(actual_b)-HP(a+1)*HP(actual_b-2)
            C=HP(a-1)*HP(actual_b-1)-HP(a)*HP(actual_b-2)
            J=CLASSES[g].count(1)*HP(kp-1)
            correction=0
            if correction_kind=='two':
                if g==1:correction=3*(-1)**(phase[1]+b_shift)*int(phase[0]%2==0)-(x+1)
                elif g==2:correction=-2*(-1)**(phase[1]+b_shift)*int(phase[0]%2==0)
                else:correction=(1,-1,0)[phase[0]%3]
            elif correction_kind=='three_positive_b' and g==1:
                correction=6*(-1)**(phase[1]+b_shift)*int(phase[0]%2==0)
            expression=sp.Poly(sp.expand(A*(HP(c)-J)-B*(HP(c-1)-J)+C*(HP(c-2)-J)+correction),x,b,k)
            degree=expression.total_degree()
            assert degree<=bound,(g,phase,degree)
            phase_bounds.append(dict(class_index=g,phase=phase,total_degree=int(degree)))

    def configured_scalar_terms(g,K):
        jet=CLASSES[g].count(1)*h(g,K+point_shift-1)
        return tuple(h(g,2*K+degree_shift-j)-jet for j in range(3))

    # Monomial differences make the identity calculation cancellation-free.
    DM={}
    for power in range(5):
        for order in range(5):
            DM[power,order]=np.array([
                sum((-1)**(order-u)*comb(order,u)*(r+60*u)**power for u in range(order+1))
                for r in range(60)],dtype=np.int64)
            assert np.all(DM[power,order]>=0)

    # Nonidentity Schur terms and their exact mixed differences.
    DXB=np.zeros((7,3,4,5,60,60),dtype=np.int64)
    DCORR=np.zeros((7,4,5,60,60),dtype=np.int64)
    DK=np.zeros((7,3,4,60),dtype=np.int64)
    for g in range(1,7):
        vals=np.array([[schur_terms(g,xx,bb+b_shift) for bb in range(300)] for xx in range(240)],dtype=np.int64)
        for i in range(4):
            for j in range(5):
                v=np.zeros((60,60,3),dtype=np.int64)
                for u in range(i+1):
                    for w in range(j+1):
                        v+=((-1)**(i+j-u-w)*comb(i,u)*comb(j,w))*vals[60*u:60*(u+1),60*w:60*(w+1),:]
                DXB[g,:,i,j]=v.transpose(2,0,1)
                if correction_kind:
                    DCORR[g,i,j]=[
                        [sum((-1)**(i+j-u-w)*comb(i,u)*comb(j,w)
                              *correction_trace(g,rx+60*u,rb+60*w+b_shift)
                              for u in range(i+1) for w in range(j+1))
                         for rb in range(60)] for rx in range(60)]
        for ell in range(3):
            for order in range(4):
                DK[g,ell,order]=[
                    sum((-1)**(order-u)*comb(order,u)*configured_scalar_terms(g,r+60*u)[ell] for u in range(order+1))
                    for r in range(60)]

    minima={','.join(map(str,v)):{} for v in LABELS}
    maxima={key:{} for key in minima}
    hashes={key:hashlib.sha256() for key in minima}
    zeros={key:[] for key in minima}
    bounds={};bad=[];zero_orders=[];total=0
    indices=[(i,j,l) for i in range(4) for j in range(5) for l in range(4)]
    for i,j,l in indices:
        # Python integers prove every individual monomial and their sum fit
        # signed64 before any NumPy operation is executed.
        id_bound=sum(v*int(DM[e[0],i].max())*int(DM[e[1],j].max())*int(DM[e[2],l].max()) for e,v in terms)
        assert id_bound<2**63
        identity_values=np.zeros((60,60,60),dtype=np.int64)
        for e,v in terms:
            identity_values+=v*DM[e[0],i][:,None,None]*DM[e[1],j][None,:,None]*DM[e[2],l][None,None,:]
        assert np.all(identity_values%12==0)
        identity_values//=12
        classarrays=[identity_values]
        classbounds=[id_bound//12]
        for g in range(1,7):
            this_bound=sum(int(np.abs(DXB[g,ell,i,j]).max())*int(np.abs(DK[g,ell,l]).max()) for ell in range(3))
            if l==0:this_bound+=int(np.abs(DCORR[g,i,j]).max())
            assert this_bound<2**63
            value=DXB[g,0,i,j,:,:,None]*DK[g,0,l][None,None,:]
            value-=DXB[g,1,i,j,:,:,None]*DK[g,1,l][None,None,:]
            value+=DXB[g,2,i,j,:,:,None]*DK[g,2,l][None,None,:]
            if l==0:value+=DCORR[g,i,j,:,:,None]
            if i+j+l>3:assert not np.any(value),(g,i,j,l,'degree')
            classarrays.append(value);classbounds.append(this_bound)
        worst=max(sum(abs(w)*bb for w,bb in zip(row,classbounds)) for row in WEIGHTS)
        assert worst<2**63,(i,j,l,worst)
        slot=f'{i},{j},{l}';bounds[slot]=worst
        allzero=True
        for mu,row in zip(LABELS,WEIGHTS):
            key=','.join(map(str,mu))
            value=sum(w*v for w,v in zip(row,classarrays))
            assert np.all(value%120==0),(mu,i,j,l,'integrality')
            value//=120
            low=int(value.min());high=int(value.max())
            minima[key][slot]=low;maxima[key][slot]=high
            hashes[key].update(value.astype('<i8',copy=False).tobytes(order='C'))
            total+=value.size
            if low<0:
                locations=np.argwhere(value<0)
                bad.append(dict(label=mu,orders=(i,j,l),count=len(locations),examples=[(list(map(int,p)),int(value[tuple(p)])) for p in locations[:8]]))
            if high:allzero=False
            if (i,j,l)==(0,0,0):zeros[key]=[list(map(int,p)) for p in np.argwhere(value==0)]
        if allzero:zero_orders.append([i,j,l])
        if j==0 and l==0:print('x order',i,'entries',total,'negative blocks',len(bad),flush=True)
    summary=dict(statement=statement,point_order=f'K+{point_shift}',line_twist=f'2*K+{degree_shift}',
                 correction_kind=correction_kind,b_shift=b_shift,
                 period=60,separate_degrees=[3,4,3],verified_entries=total,
                 negative_blocks=bad,minima=minima,maxima=maxima,
                 identically_zero_orders=zero_orders,zero_residue_triples=zeros,
                 table_sha256={key:val.hexdigest() for key,val in hashes.items()},
                 identity_numerator_terms=[dict(exponent=e,coefficient=v) for e,v in terms],
                 signed64_intermediate_bounds=bounds,
                 exact_nonidentity_phase_polynomial_degrees=phase_bounds,
                 hash_order='i=0..3,j=0..4,l=0..3; residue x,b,k C order; little-endian signed64')
    (HERE/(prefix+'_SUMMARY.json')).write_text(json.dumps(summary,indent=2)+'\n')
    message=f'PASS: {total} exact mixed Newton constants; {len(zero_orders)} identically zero orders; {len(bad)} negative blocks.\n'
    message+=f'Maximum value: {max(v for row in maxima.values() for v in row.values())}.\n'
    message+=f'Maximum signed64 numerator bound: {max(bounds.values())}.\n'
    for key,row in zeros.items():message+=f'{key}: {len(row)} zero residue triples.\n'
    (HERE/(prefix+'_CHECK.txt')).write_text(message)
    print(message,flush=True)
    assert not bad


if __name__=='__main__':main()
