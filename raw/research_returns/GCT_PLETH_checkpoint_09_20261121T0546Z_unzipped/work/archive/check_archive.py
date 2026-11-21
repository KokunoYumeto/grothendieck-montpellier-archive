"""Small exact certificates for archive audit; no numerical approximation."""
from itertools import combinations
from pathlib import Path
import json

def matmul(A, B, p):
    return [[sum(a*b for a,b in zip(row,col)) % p for col in zip(*B)] for row in A]

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def subtract(A,B,p):
    return [[(a-b)%p for a,b in zip(ar,br)] for ar,br in zip(A,B)]

def kronecker(A,B,p):
    return [[A[i][j]*B[k][l]%p for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]

def rank(A,p):
    A=[row[:] for row in A]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[x*inv%p for x in A[r]]
        for i in range(len(A)):
            if i != r:
                factor=A[i][c]
                A[i]=[(x-factor*y)%p for x,y in zip(A[i],A[r])]
        r+=1
    return r

def jordan_ranks(g,p):
    N=subtract(g,identity(len(g)),p)
    powers=N
    out=[]
    for _ in range(p):
        out.append(rank(powers,p))
        powers=matmul(powers,N,p)
    return out

def determinant(A,p):
    if not A: return 1
    return sum((-1)**j*A[0][j]*determinant([r[:j]+r[j+1:] for r in A[1:]],p)
               for j in range(len(A))) %p

def exterior(g,k,p):
    subsets=list(combinations(range(len(g)),k))
    return [[determinant([[g[i][j] for j in J] for i in I],p) for J in subsets] for I in subsets]

J2=[[1,1],[0,1]]
J3=[[0,0,1],[1,0,0],[0,1,0]]
out={}
for name,g in [('J2xJ2',kronecker(J2,J2,3)),('J3xJ2',kronecker(J3,J2,3)),
               ('J3xJ3',kronecker(J3,J3,3)),('wedge2J3',exterior(J3,2,3))]:
    out[name]=jordan_ranks(g,3)
assert out['J2xJ2']==[2,1,0]   # J3 + J1
assert out['J3xJ2']==[4,2,0]   # 2 J3
assert out['J3xJ3']==[6,3,0]   # 3 J3
assert out['wedge2J3']==[2,1,0] # J3
assert exterior(J2,2,3)==[[1]]
assert exterior(J3,3,3)==[[1]]
assert matmul(list(map(list,zip(*J3))),J3,3)==identity(3)

# Burnside ring of C2: elements a*1+b*E, E free of cardinality 2.
def Bmul(u,v):
    a,b=u; c,d=v
    return (a*c,a*d+b*c+2*b*d)
E=(0,1); one=(1,0)
out['Burnside_E_squared']=Bmul(E,E)
out['Burnside_2_lambda2_plus_E']=(2,1)
out['Burnside_C2_fixed_points']={'E_squared':0,'2_lambda2_plus_E':2}
assert out['Burnside_E_squared']!=(2,1)

# Exact multiplication in Green(C3): basis 1, y=J2, x=J3.
def Gmul(u,v):
    a,b,c=u;d,e,f=v
    return (a*d+b*e,a*e+b*d,a*f+c*d+b*e+2*b*f+2*c*e+3*c*f)
def scale(n,u):return tuple(n*x for x in u)
def add(u,v):return tuple(x+y for x,y in zip(u,v))
x=(0,0,1); y=(0,1,0); one=(1,0,0)
psi3x=(3,0,0); psi3y=(0,-2,2)
z=scale(2,y)
out['psi3_of_xz']=(12,0,0)
out['psi3x_times_psi3z']=Gmul(psi3x,scale(2,psi3y))
out['multiplicativity_defect']=add(out['psi3x_times_psi3z'],scale(-1,out['psi3_of_xz']))
assert out['multiplicativity_defect']==(-12,-12,12)

path=Path(__file__).with_name('COMPUTATION_RESULTS.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
