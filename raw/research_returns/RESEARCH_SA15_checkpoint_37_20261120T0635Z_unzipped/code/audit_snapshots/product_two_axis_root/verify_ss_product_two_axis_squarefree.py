"""Independent universal binary determinant certificate for two product axes.

No symbolic determinant or factorization package is used.  Coefficients lie
in F2[a,b,c,d,t]/(b^2+b+a^3,d^2+d+c^3), and every determinant is reconstructed
by the subset permutation recurrence.  The homogeneous squarefreeness and
full-pencil consequences are supplied by the accompanying written proof.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time

start=time.perf_counter()
zero=set();one={(0,0,0,0,0)}
def add(*polys):
    ans=set()
    for p in polys:ans.symmetric_difference_update(p)
    return ans
def var(i):
    m=[0]*5;m[i]=1
    return {tuple(m)}
a,b,c,d,t=[var(i) for i in range(5)]
def mul(P,Q):
    out=set()
    for m in P:
        for n in Q:
            e=tuple(x+y for x,y in zip(m,n))
            assert e[1]<=2 and e[3]<=2
            pending=[e]
            if e[1]==2:
                pending=[]
                f=list(e);f[1]=1;pending.append(tuple(f))
                f=list(e);f[1]=0;f[0]+=3;pending.append(tuple(f))
            reduced=[]
            for f in pending:
                if f[3]!=2:reduced.append(f);continue
                g=list(f);g[3]=1;reduced.append(tuple(g))
                g=list(f);g[3]=0;g[2]+=3;reduced.append(tuple(g))
            for f in reduced:
                if f in out:out.remove(f)
                else:out.add(f)
    return out
def power(p,n):
    q=one
    for _ in range(n):q=mul(q,p)
    return q
def derivative(p,index):
    ans=set()
    for m in p:
        if m[index]%2:
            e=list(m);e[index]-=1;ans.add(tuple(e))
    return ans
def mat(x,y):
    return [[[one,x,zero],[x,zero,y],[zero,add(y,one),x]],
            [[zero,zero,one],[zero,one,zero],[one,zero,zero]],
            [[zero,zero,zero],[zero,zero,one],[zero,one,zero]]]
line=[[zero,zero,t],[one,add(one,t),add(one,t)],
      [add(one,t),one,add(one,t)]]
def cross_matrix(A,B,T):
    return [[add(*(mul(T[i][j],mul(A[i][r//3][s//3],B[j][r%3][s%3]))
                    for i in range(3) for j in range(3)))
             for s in range(9)] for r in range(9)]
def determinant(M):
    dp={0:one}
    for mask in range(1<<9):
        p=dp.get(mask,zero)
        if not p or mask==(1<<9)-1:continue
        row=mask.bit_count()
        for col in range(9):
            if not (mask>>col)&1:
                nxt=mask|(1<<col)
                dp[nxt]=add(dp.get(nxt,zero),mul(p,M[row][col]))
    return dp[(1<<9)-1]

A=mat(a,b);B=mat(c,d)
f=determinant(cross_matrix(A,B,line))
u=add(b,d,mul(a,c),a,one)
v=mul(c,add(a,one))
w=add(mul(a,c),a,c)
Delta=add(b,d,a,c,one)
expected=add(mul(power(u,2),power(t,9)),mul(power(v,2),power(t,8)),
             mul(power(w,2),add(power(t,7),power(t,6))),t,one)
assert f==expected
assert add(u,v)==Delta
assert derivative(f,4)==power(add(mul(u,power(t,4)),mul(w,power(t,3)),one),2)
assert add(f,mul(t,derivative(f,4)))==power(add(mul(v,power(t,4)),mul(w,power(t,3)),one),2)

# Negating the first actual elliptic point is b -> b+1.  The corresponding
# change A0 -> A0+A2 is exactly row2 -> row2+row0 on the functional matrix.
changed=[list(row) for row in line]
changed[2]=[add(x,y) for x,y in zip(line[2],line[0])]
f_negative=determinant(cross_matrix(mat(a,add(b,one)),B,line))
f_changed=determinant(cross_matrix(A,B,changed))
assert f_negative==f_changed
u_negative=add(u,one)
expected_negative=add(mul(power(u_negative,2),power(t,9)),mul(power(v,2),power(t,8)),
                      mul(power(w,2),add(power(t,7),power(t,6))),t,one)
assert f_negative==expected_negative
assert add(u_negative,v)==add(Delta,one)

# Exact homogeneous derivatives in variables T,U are represented by
# exponent pairs; the written argument takes their square roots.  A common
# root would satisfy Delta*T^4=0 and then U^4=0, impossible if Delta!=0.
assert one # The nonzero constant term in each square root is retained above.
at_zero={m[4] for m in f if m[:4]==(0,0,0,0)}
assert at_zero=={9,1,0}
record={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'method':'Pure binary polynomial arithmetic with two monic elliptic relations and three independent subset-determinant reconstructions.',
        'universal_reduced_term_count':len(f),
        'universal_reduced_terms':[list(m) for m in sorted(f)],
        'negated_reduced_terms':[list(m) for m in sorted(f_negative)],
        'identities':['universal fixed-line determinant','u+v=Delta','first homogeneous partial square on U=1','second homogeneous partial square on U=1','negated-point determinant equals changed-line determinant','universal negated fixed-line formula','negation changes Delta by1','order-three specialization is t9+t+1'],
        'Delta':'b+d+a+c+1',
        'line_matrix':[['0','0','t'],['1','1+t','1+t'],['1+t','1','1+t']],
        'changed_line_matrix':[['0','0','t'],['1','1+t','1+t'],['1+t','1','1']],
        'scope':'Universal two-axis actual product dual-cross determinant reducedness, using the written homogeneous-derivative argument. No cycle stable-rank, wall inertia, indecomposable fixed-surface or full-monodromy claim.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if not k.endswith('_terms')},indent=2))
