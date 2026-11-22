#!/usr/bin/env python3
"""Exact integer certificates for cote 68: interval axioms and noncommutative asymmetry.
No third-party modules, no random search. All tested finite families are enumerated.
"""
from itertools import permutations, product
from collections import Counter
from pathlib import Path
import json,time
START=time.perf_counter()

def conv(f,g,mul):
    n=len(f); out=[0]*n
    for i,a in enumerate(f):
        for j,b in enumerate(g): out[mul(i,j)]+=a*b
    return out

def indicator(a,n): return [int(i in a) for i in range(n)]
def majorized(f,g):
    sf=sg=0
    for a,b in zip(sorted(f,reverse=True),sorted(g,reverse=True)):
        sf+=a; sg+=b
        if sf>sg: return False
    return True

def cone_coefficients(v,chain):
    """Exact decomposition into indicators of a strictly increasing chain ending in G."""
    prev=set(); shell_values=[]
    for a in chain:
        shell=set(a)-prev
        values={v[x] for x in shell}
        if len(values)!=1: return None
        shell_values.append(next(iter(values)))
        prev=set(a)
    coeff=[shell_values[i]-(shell_values[i+1] if i+1<len(chain) else 0) for i in range(len(chain))]
    if any(a<0 for a in coeff): return None
    reconstructed=[sum(c*int(x in a) for c,a in zip(coeff,chain)) for x in range(len(v))]
    assert reconstructed==v
    return coeff

G=set(range(4))
families={}
for k in range(8):
    a=k//2
    if k%2==0:
        families[k]=[{a%4},{(a-1)%4,a%4,(a+1)%4},G]
    else:
        families[k]=[{a%4,(a+1)%4},G]
counts=Counter(); decompositions=[]; alignments=[]
for k,chain in families.items():
    assert all(a<=b or b<=a for a in chain for b in chain)
    counts['chain_fibres']+=1
    for a in chain:
        assert a=={(k-x)%4 for x in a}
        counts['symmetry_atoms']+=1
for k,l in product(range(8),repeat=2):
    for a,b in product(families[k],families[l]):
        v=conv(indicator(a,4),indicator(b,4),lambda x,y:(x+y)%4)
        coeff=cone_coefficients(v,families[(k+l)%8])
        assert coeff is not None,(k,l,a,b,v)
        counts['convolution_atom_pairs']+=1
        decompositions.append({'k':k,'l':l,'A':sorted(a),'B':sorted(b),'convolution':v,'coefficients':coeff})
    witnesses=[]
    for s in range(4):
        union=families[k]+[{(x+s)%4 for x in b} for b in families[l]]
        if all(a<=b or b<=a for a in union for b in union): witnesses.append(s)
    assert witnesses,(k,l)
    alignments.append({'k':k,'l':l,'s':witnesses[0]})
    counts['alignment_pairs']+=1
for u,k in product([0,2],range(8)):
    assert families[(2*u+k)%8]==[{(u+x)%4 for x in a} for a in families[k]]
    counts['torsion_equivariance_pairs']+=1
assert {len(a) for chain in families.values() for a in chain}=={1,2,3,4}
f=indicator({0,1},4); h=indicator({0,2},4); c4_f=f[:]
f2=conv(f,f,lambda a,b:(a+b)%4); f3=conv(f2,f,lambda a,b:(a+b)%4)
h2=conv(h,h,lambda a,b:(a+b)%4); h3=conv(h2,h,lambda a,b:(a+b)%4)
assert max(f3)==3 and max(h3)==4
assert sorted(f)==sorted(h)
assert not majorized(h2,f2)

perms=list(permutations(range(3))); index={p:i for i,p in enumerate(perms)}
def pmul(i,j):
    p,q=perms[i],perms[j]
    return index[tuple(p[q[x]] for x in range(3))]
e=index[(0,1,2)]; a=index[(1,0,2)]; b=index[(0,2,1)]
f=[0]*6; f[e]=1; f[a]=2
g=[0]*6; g[b]=1; g[pmul(a,b)]=2
fg=conv(f,g,pmul); gf=conv(g,f,pmul)
assert max(fg)==5 and max(gf)==4
profiles=[]
for i,j in permutations(range(6),2):
    v=[0]*6; v[i]=2;v[j]=1;profiles.append(v)
packed_checks=0
for fp,gp in product(profiles,repeat=2):
    assert majorized(conv(fp,gp,pmul),fg)
    packed_checks+=1
assert not majorized(fg,gf)
result={
 'C4':{'group':'Z/4Z','index_group':'Z/8Z','rho':'k mod 4','i':'u -> 2u mod 8 for u in {0,2}',
       'families':{k:[sorted(a) for a in chain] for k,chain in families.items()},
       'counts':dict(counts),'f':c4_f,'h':h,'f2':f2,'h2':h2,'f3':f3,'h3':h3,
       'K_failure':{'lhs':max(h3),'rhs':max(f3)},'all_cardinalities':[1,2,3,4]},
 'S3':{'enumeration':[list(p) for p in perms],'multiplication':'p composed with q',
       'e':e,'a':a,'b':b,'f':f,'g':g,'fg':fg,'gf':gf,
       'maxima':[max(fg),max(gf)],'packed_checks':packed_checks},
 'runtime_seconds':time.perf_counter()-START,
}
out=Path(__file__).with_name('part_c_finite_checks_output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
Path(__file__).with_name('part_c_C4_certificate.json').write_text(json.dumps({'decompositions':decompositions,'alignments':alignments},indent=2)+'\n')
print(json.dumps(result,indent=2))
print('PASS: every asserted finite check passed.')
