"""G037: tableau/coin encodings and an independent recurrence at huge degree."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from collections import Counter
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'root'))
import stable_hook_positive as target

def partitions(n,ceiling=None):
    if not n:yield ();return
    for first in range(min(n,ceiling or n),0,-1):
        for rest in partitions(n-first,first):yield (first,)+rest

@lru_cache(None)
def tableaux(shape):
    """Place the largest label in each removable corner; return cell sequence."""
    if not shape:return ((),)
    out=[]
    for i,row in enumerate(shape):
        if i+1<len(shape) and shape[i+1]==row:continue
        smaller=list(shape);smaller[i]-=1
        while smaller and smaller[-1]==0:smaller.pop()
        out.extend(t+((i+1,row),) for t in tableaux(tuple(smaller)))
    return tuple(out)

@lru_cache(None)
def coin_count(weights,degree):
    if degree<0:return 0
    if not weights:return int(degree==0)
    w=weights[0]
    return sum(coin_count(weights[1:],degree-w*j) for j in range(degree//w+1))

def coin_witness(weights,degree):
    if degree<0:return None
    if not weights:return () if degree==0 else None
    w=weights[0]
    for j in range(degree//w+1):
        rest=coin_witness(weights[1:],degree-w*j)
        if rest is not None:return (j,)+rest

def numerator(shape,r):
    cells=[(i+1,j+1) for i,v in enumerate(shape) for j in range(v)]
    retained=[c for c in cells if c not in ((1,1),(2,1))]
    result=Counter()
    for T in tableaux(shape):
        maj=sum(len(T)-j for j in range(1,len(T)) if T[j][0]>T[j-1][0])
        for chosen in combinations(retained,r):
            result[maj+sum(j-i+1 for i,j in chosen)]+=1
    return result

counts=Counter()
for m in range(3,7):
  for shape in partitions(m):
    for r in range(m-1):
      N=numerator(shape,r) if shape!=(m,) else None
      if N is not None:
        assert min(N)>=0
        got=target.nontrivial_numerator(shape,r)
        assert N==Counter({i:v for i,v in enumerate(got) if v})
        L=min(N)
      else:L=(r+2)*(r+3)//2-1
      for D in sorted(set(range(r+1,r+6))|{max(r+1,L-1),max(r+1,L),max(r+1,L+1),max(r+1,L+2)}):
        a=D-r;P=target.module_polytope(m,a,r,shape)
        assert P['variable_count']<=(m*m+3*m-4 if shape!=(m,) else 3*m-3)
        total=0;witness=None
        if shape!=(m,):
          total=sum(v*coin_count(tuple(range(2,m+1)),D-d) for d,v in N.items())
          cells=[(i+1,j+1) for i,v in enumerate(shape) for j in range(v)]
          retained=[c for c in cells if c not in ((1,1),(2,1))]
          for T in tableaux(shape):
            desc=[int(T[j][0]>T[j-1][0]) for j in range(1,m)]
            comaj=sum((m-j)*v for j,v in enumerate(desc,1))
            for chosen in combinations(retained,r):
              coin=coin_witness(tuple(range(2,m+1)),D-comaj-sum(j-i+1 for i,j in chosen))
              if coin is None:continue
              witness={f'X{c[0]}_{c[1]}_{j}':int(T[j-1]==c) for c in cells for j in range(1,m+1)}
              witness.update({f'd{j}':v for j,v in enumerate(desc,1)})
              witness.update({f'Y{c[0]}_{c[1]}':int(c in chosen) for c in retained})
              witness.update({f'c{j}':v for j,v in zip(range(2,m+1),coin)})
              break
            if witness is not None:break
        else:
          for i in range(2,m+1):
            for chosen in combinations(range(i+1,m+1),r):
              rem=D-i-sum(chosen)
              total+=coin_count(tuple(range(i,m+1)),rem)
              coin=coin_witness(tuple(range(i,m+1)),rem)
              if witness is not None or coin is None:continue
              beta={j:0 for j in range(2,m+1)};beta[i]=1
              for j in chosen:beta[j]+=1
              for j,v in zip(range(i,m+1),coin):beta[j]+=v
              witness={f'z{j}':int(j==i) for j in beta}
              witness.update({f'y{j}':int(j in chosen) for j in beta})
              witness.update({f'b{j}':v for j,v in beta.items()})
        assert total==target.module_coefficient(m,a,r,shape),(m,a,r,shape,total)
        assert bool(total)==target.module_support(m,a,r,shape)
        counts['coefficient_counts']+=1;counts['support_cases']+=1;counts['matrices']+=1
        if witness is not None:
          assert target.valid_witness(P,witness)
          counts['literal_witnesses']+=1

# Independent binary exponentiation modulo the recurrence polynomial.
def recurrence_coin(weights,N):
    if N<0:return 0
    Q=[1]
    for w in weights:
        old=Q[:];Q += [0]*w
        for j,v in enumerate(old):Q[j+w]-=v
    d=len(Q)-1
    initial=[coin_count(weights,j) for j in range(d)]
    def product_mod(A,B):
        C=[0]*(2*d-1)
        for i,v in enumerate(A):
            for j,w in enumerate(B):C[i+j]+=v*w
        for e in range(2*d-2,d-1,-1):
            for j in range(1,d+1):C[e-j]-=C[e]*Q[j]
        return C[:d]
    result=[1]+[0]*(d-1);power=[0,1]+[0]*(d-2)
    while N:
        if N&1:result=product_mod(result,power)
        power=product_mod(power,power);N//=2
    return sum(v*w for v,w in zip(result,initial))

for m,r,shape in [(3,0,(3,)),(3,1,(1,1,1)),(4,1,(2,2)),(5,2,(3,2)),(6,4,(1,1,1,1,1,1)),(6,2,(6,))]:
  for D in (10**12+17,10**30+21):
    if shape==(m,):
      value=sum(recurrence_coin(tuple(range(i,m+1)),D-i-sum(S)) for i in range(2,m+1)
                for S in combinations(range(i+1,m+1),r))
    else:value=sum(v*recurrence_coin(tuple(range(2,m+1)),D-d) for d,v in numerator(shape,r).items())
    assert value==target.module_coefficient(m,D-r,r,shape)
    counts['huge_degree_recurrence_checks']+=1
out={'statement':'G037 independent positive-combinatorics and literal matrix audit','status':'PASS',
     'method':'removable-corner tableau recursion; direct cell subsets and coin enumeration; independent recurrence-polynomial binary powering at huge degree',
     'm_range':[3,6],**dict(counts),'original_cycle_or_MN_sweep':'not repeated'}
(HERE/'STABLE_HOOK_INDEPENDENT_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
