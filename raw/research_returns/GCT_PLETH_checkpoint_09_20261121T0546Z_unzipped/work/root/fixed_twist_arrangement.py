"""Exact rank-three G027 arrangement characters at fixed ideal order and twist."""
from functools import lru_cache
from itertools import combinations, permutations, product
from collections import defaultdict
from first_power_zero_twist import PERMS, cycle_type, complete_values
from five_row_cycle_trace import LABELS, SIZES, CHARS, multiplicities

P3 = tuple(permutations(range(3)))
EPS = {p: (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in P3}

@lru_cache(None)
def normal_schur(cycles,k):
    polynomial={(0,0,0):1}
    for ell in cycles:
        factor=[(ell*i,ell*j,ell*(t-i-j))
                for t in range(k) for i in range(t+1) for j in range(t-i+1)]
        following=defaultdict(int)
        for a,coefficient in polynomial.items():
            for b in factor:following[tuple(x+y for x,y in zip(a,b))]+=coefficient
        polynomial=dict(following)
    delta=(2,1,0);answer=[]
    for degree in range(sum(cycles)*(k-1)+1):
        for r in range(degree//3+1):
            for q in range(r,(degree-r)//2+1):
                p=degree-q-r;rho=(p,q,r)
                value=sum(EPS[sigma]*polynomial.get(tuple(rho[i]+delta[i]-delta[sigma[i]] for i in range(3)),0) for sigma in P3)
                if value:answer.append((rho,value))
    return tuple(sorted(answer))

@lru_cache(None)
def terms(class_index,k):
    permutation=PERMS[class_index];answer=defaultdict(int)
    for size in range(4):
        for selected in combinations(range(5),size):
            if set(permutation[i] for i in selected)!=set(selected):continue
            chosen=cycle_type(permutation,selected)
            complement=cycle_type(permutation,[i for i in range(5) if i not in selected])
            sign=(-1)**len(chosen)
            for rho,value in normal_schur(chosen,k):answer[(complement,rho)]+=sign*value
    return tuple((value,cycles,rho) for (cycles,rho),value in sorted(answer.items()) if value)

@lru_cache(None)
def skew(cycles,alpha,rho):
    if any(r>s for r,s in zip(rho,alpha)):return 0
    h=complete_values(cycles,max(alpha)+2)
    def H(i):return h[i] if i>=0 else 0
    return sum(EPS[sigma]*H(alpha[0]-rho[sigma[0]]+sigma[0])*
               H(alpha[1]-rho[sigma[1]]-1+sigma[1])*
               H(alpha[2]-rho[sigma[2]]-2+sigma[2]) for sigma in P3)

def traces(x,b,k,c):
    alpha=(b+x+c,b+c,c)
    return tuple(sum(value*skew(cycles,alpha,rho) for value,cycles,rho in terms(g,k)) for g in range(7))

def coefficients(x,b,k,c):
    values=traces(x,b,k,c);answer=[]
    for row in CHARS:
        numerator=sum(s*t*v for s,t,v in zip(SIZES,row,values))
        assert numerator%120==0,(x,b,k,c,numerator)
        answer.append(numerator//120)
    return tuple(answer)

def grid(xs,bs,k,c):
    """Fast exact-int64 grid, with a prior absolute bound on all operations."""
    import numpy as np
    X=np.asarray(xs,dtype=np.int64)[:,None]
    B=np.asarray(bs,dtype=np.int64)[None,:]
    alpha=(B+X+c,B+0*X+c,np.full((len(xs),len(bs)),c,dtype=np.int64))
    maxdegree=int(np.max(alpha[0]))+2
    traces=[];largest_bound=0
    for g in range(7):
        total=np.zeros_like(alpha[0]);absolute_bound=0
        for coefficient,cycles,rho in terms(g,k):
            if rho[2]>c:continue
            h=np.asarray(complete_values(cycles,maxdegree),dtype=np.int64)
            values={}
            for i in range(3):
                for j in range(3):
                    index=alpha[i]-rho[j]-i+j
                    values[i,j]=np.where(index>=0,h[np.maximum(index,0)],0)
            det=np.zeros_like(total)
            for sigma in P3:
                bound=1
                for i in range(3):
                    bound*=int(np.max(np.abs(values[i,sigma[i]])))
                    assert bound<2**63,(g,'prefix product',i,bound)
                absolute_bound+=abs(coefficient)*bound
                assert absolute_bound<2**63,(g,absolute_bound)
                det+=EPS[sigma]*values[0,sigma[0]]*values[1,sigma[1]]*values[2,sigma[2]]
            contained=(alpha[0]>=rho[0])&(alpha[1]>=rho[1])
            total+=coefficient*np.where(contained,det,0)
        traces.append(total);largest_bound=max(largest_bound,absolute_bound)
    result=[]
    for row in CHARS:
        bound=sum(abs(s*t)*int(np.max(np.abs(v))) for s,t,v in zip(SIZES,row,traces))
        assert bound<2**63,bound
        value=sum(s*t*v for s,t,v in zip(SIZES,row,traces))
        assert np.all(value%120==0)
        result.append(value//120)
    return np.asarray(result),largest_bound

if __name__=='__main__':
    total=0
    for k in (1,2,3):
        for c in range(3):
            for b in range(9):
                for x in range(8):
                    if 2*b+x+3*c<5*k:continue
                    n=b+x+c-k
                    lam=(3*b+2*x+4*c-5*k,b+x+c,b+x,x,0)
                    if n<0:continue
                    proposed=coefficients(x,b,k,c)
                    if (b+x+c)%2:proposed=proposed[::-1]
                    expected=multiplicities(lam)
                    assert proposed==expected,(x,b,k,c,lam,proposed,expected)
                    total+=7
    print('PASS',total,'actual coefficients',flush=True)
