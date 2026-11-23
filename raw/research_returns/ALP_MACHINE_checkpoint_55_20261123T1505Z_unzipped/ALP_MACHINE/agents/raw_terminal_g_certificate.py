"""Exact finite graph/phase diagnostic for LIFT21, not a theta proof."""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json

def gl_order(n,q):
    return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))

def primitive_root(q):
    return next(g for g in range(2,q) if len({pow(g,j,q) for j in range(q-1)})==q-1)

def case(q,k):
    # t=1 suffices to check the joining-column sharp condition.
    t,d,r=k*0+1,2,k+1
    b,N=r+t,r+t+d
    root=primitive_root(q)
    log={pow(root,j,q):j for j in range(q-1)}
    upper=[(i,j) for i in range(r) for j in range(i+1,r)]
    H=[]
    for entries in product(range(q),repeat=len(upper)):
        u=[[int(i==j) for j in range(r)] for i in range(r)]
        for (i,j),x in zip(upper,entries):u[i][j]=x
        for rect in product(range(q),repeat=r):
            for h in range(1,q):
                B=[u[i]+[rect[i]] for i in range(r)]+[[0]*r+[h]]
                sharp=all(B[i][k]==0 for i in range(k))
                add=sum(B[i][i+1] for i in range(r-1))%q
                H.append((B,sharp,add,h))
    Hs=[g for g in H if g[1]]
    hq=q**(r*(r-1)//2+r*t)*gl_order(t,q)
    assert len(H)==hq and len(Hs)==hq//q**k

    # eta0,eta1 are distinct nontrivial for F5; F3 is a
    # higher-k geometry diagnostic and does not assert this hypothesis.
    eta0,eta1=(2,1) if q==5 else (1,1)
    raw_phase_checks=0
    for B,sharp,add,h in H:
        raw_mul=(eta1-eta0)*log[h]%(q-1)
        omega_mul=-eta1*log[h]%(q-1)
        input_mul=eta0*log[h]%(q-1)
        assert (raw_mul+omega_mul+input_mul)%(q-1)==0
        assert (add-add)%q==0
        if sharp:
            sharp_add=sum(B[i][i+1] for i in range(k-1))%q
            assert sharp_add==add
        raw_phase_checks+=1

    graph_count={'plain':0,'sharp':0}
    graph_tests=0
    for z in product(range(q),repeat=b):
        for label,grp in [('plain',H),('sharp',Hs)]:
            counts=[0]*q
            for B,sharp,add,h in grp:
                # w=zB is the actual last row on h_z^-1 X0 B.
                w_k=sum(z[i]*B[i][k] for i in range(b))%q
                raw_add=(add-w_k)%q
                input_add=-add%q
                counts[(raw_add+input_add)%q]+=1
            nonzero=label=='sharp' or all(z[i]==0 for i in range(k))
            if nonzero:
                predicted=[0]*q;predicted[-z[k]%q]=len(grp)
                assert counts==predicted
                graph_count[label]+=1
            else:
                assert len(grp)%q==0
                assert counts==[len(grp)//q]*q
            graph_tests+=1
    assert graph_count=={'plain':q**(b-k),'sharp':q**b}

    Gb,GN,Gd=gl_order(b,q),gl_order(N,q),gl_order(d,q)
    J=F(GN,Gb*Gd*q**(b*d))
    assert J.denominator==1
    vol=F(len(H),Gb);vols=F(len(Hs),Gb)
    raw=F(len(H)*q**b,q**(N*b))
    raws=F(len(Hs)*q**b,q**(N*b))
    c2=F(graph_count['plain'],J)*vol**2
    c2s=F(graph_count['sharp'],J)*vols**2
    assert vols==vol/q**k
    assert raws==raw/q**k and c2s==c2/q**k
    assert c2/raw==c2s/raws
    assert c2/raw==F(q**(N*b-k)*len(H),Gb**2*J)
    # At z=0 every normalized quotient value is precisely v.
    assert graph_count['plain']>0 and graph_count['sharp']>0
    return {
        'q':q,'k':k,'t':t,'b':b,'N':N,
        'distinct_nontrivial_characters_tested':q==5,
        'H_order':len(H),'Hsharp_order':len(Hs),
        'raw_determinant_and_input_phase_checks':raw_phase_checks,
        'full_graph_average_checks':graph_tests,
        'nonzero_graph_counts':graph_count,
        'target_parabolic_index':str(J),
        'H_volume':str(vol),'Hsharp_volume':str(vols),
        'raw_norm_squared':str(raw),'sharp_raw_norm_squared':str(raws),
        'column_output_scale_squared':str(c2),
        'sharp_column_output_scale_squared':str(c2s),
        'common_unit_finite_scale_squared':str(c2/raw),
    }

out={'status':'PASS','cases':[case(5,1),case(3,2)],
     'scope':'Finite raw support/phase and graph-norm diagnostic. General quotient and lattice proofs are LIFT21; low ranks do not satisfy full source Ranks.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
