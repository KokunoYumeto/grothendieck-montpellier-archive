#!/usr/bin/env python3
"""Independent exact supplement to the complete HOS13--15 peer audit.

The author's checker was read, but no implementation or output is imported.
Our form enumeration is an incremental base-three coefficient traversal.
Our carrier spectra are full matrix ranks over F19, whose nine distinct
ninth roots preserve the characteristic-zero monomial multiplicities.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
from flint import nmod_mat
import time,hashlib,json

START=time.perf_counter();HERE=Path(__file__).resolve().parent
PROOF=HERE.parent.parent/'g34_eightfolds/bireflection/higher_odd_symplectic_three_cutoff_section.tex'
EXPECTED='42ccec86bd4fa25e91c9156204e215e901f3b8ea6a175c9012ba2948dae72bba'
assert hashlib.sha256(PROOF.read_bytes()).hexdigest()==EXPECTED
out={'status':'PASS','proof_sha256':EXPECTED,'implementation':'Independent; no author arithmetic imported'}

# Exact independent form traversal, including every symmetric matrix in
# dimensions2,3,4. The current value vector is updated when a ternary
# coefficient advances; reduction mod3 handles all carry digits.
form_results=[]
for n in (2,3,4):
    vectors=list(product(range(3),repeat=n))[1:]
    basis=[[((1 if i==j else 2)*v[i]*v[j])%3 for v in vectors]
           for i in range(n) for j in range(i,n)]
    digits=[0]*len(basis);values=[0]*len(vectors);total=0
    maximum_zero=maximum_nonzero=F(0)
    for serial in range(1,3**len(basis)):
        k=0
        while True:
            values=[(x+y)%3 for x,y in zip(values,basis[k])]
            digits[k]=(digits[k]+1)%3
            if digits[k]:break
            k+=1
        C=Counter(values)
        maximum_zero=max(maximum_zero,F(C[0],len(vectors)))
        maximum_nonzero=max(maximum_nonzero,F(max(C[1],C[2]),len(vectors)))
        assert 9*C[0]<=5*len(vectors)
        assert max(C[1],C[2])<=2*3**(n-1)
        assert 9*max(C[1],C[2])<=7*len(vectors)
        total+=1
    form_results.append({'dimension':n,'forms':total,
      'max_zero_fraction':str(maximum_zero),'max_nonzero_fraction':str(maximum_nonzero)})
out['complete_form_enumeration']=form_results
assert sum(r['forms'] for r in form_results)==59802

# Work with all quadratic phase operators on functions F3^2, then multiply
# on the left by every Heisenberg displacement, including its central half
# phase. Full9x9 matrices are used, not an orbit/cycle spectral formula.
# F19 contains primitive ninth root4 and primitive third root7.
mod=19;zeta=4;omega=pow(zeta,3,mod)
assert omega==7 and pow(zeta,9,mod)==1 and pow(zeta,3,mod)!=1
roots=[pow(zeta,j,mod) for j in range(9)]
assert len(set(roots))==9
phase_of={pow(omega,j,mod):j for j in range(3)}
vec=list(product(range(3),repeat=2));index={v:i for i,v in enumerate(vec)}
I=nmod_mat([[int(i==j) for j in range(9)] for i in range(9)],mod)
def matrix_operator(aa,bb,dd,x,y):
    rows=[[0]*9 for _ in range(9)]
    for u in vec:
        target=((u[0]+x[0])%3,(u[1]+x[1])%3)
        # A=D*L_x,y; changing multiplication order merely changes the
        # arbitrary linear phase. This differs from the author's convention.
        phase=(2*(aa*target[0]**2+2*bb*target[0]*target[1]+dd*target[1]**2)
               +y[0]*u[0]+y[1]*u[1]+2*(x[0]*y[0]+x[1]*y[1]))%3
        rows[index[target]][index[u]]=pow(omega,phase,mod)
    return nmod_mat(rows,mod)
def exact_trace_norm(A):
    cnt=[0,0,0]
    for i in range(9):
        x=int(A[i,i])
        if x:cnt[phase_of[x]]+=1
    return sum(x*x for x in cnt)-sum(cnt[i]*cnt[j] for i in range(3) for j in range(i+1,3))
ops=rank2=powerchecks=0;support_hist=Counter();degree_hist=Counter()
for aa,bb,dd in product(range(3),repeat=3):
    rank=2 if (aa*dd-bb*bb)%3 else int(bool(aa or bb or dd))
    for x in vec:
        for y in vec:
            A=matrix_operator(aa,bb,dd,x,y);A2=A*A;A3=A2*A
            c=int(A3[0,0]);assert c and A3==I*c
            assert A3*A3*A3==I
            multiplicities=[9-(A-I*r).rank() for r in roots]
            assert sum(multiplicities)==9
            support=9-max(multiplicities)
            if rank==2:
                assert support>=4
                rank2+=1;support_hist[support]+=1
            for B in (A,A2):
                assert exact_trace_norm(B)<=3**(4-rank)
                powerchecks+=1
            degree_hist[1 if A==I else 3 if A3==I else 9]+=1
            ops+=1
assert ops==2187 and powerchecks==4374
out['full_matrix_carriers']={'operators':ops,'trace_power_checks':powerchecks,
 'rank_two_carriers':rank2,'rank_two_support_histogram':dict(sorted(support_hist.items())),
 'matrix_order_histogram':dict(sorted(degree_hist.items())),
 'coefficient_field':'F19 with zeta9=4; A^9=I and all9 roots remain distinct'}

# Independent finite-field verification of the Siegel-conjugation word in
# three coordinate planes, every ordered pair and both root parameters.
n=3;dim=6
def mat(rows):return nmod_mat(rows,3)
eye=mat([[int(i==j) for j in range(dim)] for i in range(dim)])
J=mat([[int(j==i+n)-int(i==j+n) for j in range(dim)] for i in range(dim)])
def trans(j,c):
    A=eye*1
    for k in range(dim):A[j,k]=int(A[j,k])+c*int(J[j,k])
    return A
words=0
for i in range(n):
 for j in range(n):
    if i==j:continue
    W=trans(j,1)*trans(n+j,1)*trans(j,1)
    for c in (1,2):
        U=eye*1;U[i,n+j]=c;U[j,n+i]=c
        L=W*U*W.inv()
        assert L.transpose()*J*L==J
        assert all(int(L[r,n+s])==int(L[n+r,s])==0 for r in range(n) for s in range(n))
        assert L!=eye
        words+=1
out['siegel_generation_words']=words

# Universal constants, compared as rational numbers rather than decimal
# approximations or enormous degrees. The inequalities themselves are
# independently proved in the peer report.
sigma=F(1,10**29);published=F(1,6507*2**21*10**18);N0=10**30
assert published>7*sigma
assert F(N0-1,2*10**29)>1
assert F(1,2)*F(2,3)*(1-F(1,3))==F(2,9)
assert F(1,4)*(1-F(1,9))==F(2,9)
assert F(1,2)*F(4,5)*(1-F(1,3))==F(4,15)>F(2,9)
assert 12*F(2,9)-2==F(2,3) and 6/(12*F(2,9)-2)==9
out['constants']={'support':'2/9','natural_rank_cutoff':str(N0),'degree_ceiling':9,
 'published_sigma':str(published),'retained_sigma':str(sigma)}
out['seconds']=round(time.perf_counter()-START,9)
(HERE/'independent_checked.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
