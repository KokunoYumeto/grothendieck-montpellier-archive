import itertools, cmath
G=list(itertools.permutations(range(5)))
def comp(a,b): return tuple(a[b[i]] for i in range(5))
def sign(p):
    s=1
    for i in range(5):
        for j in range(i+1,5):
            if p[i]>p[j]: s=-s
    return s
def fix(p): return sum(1 for i in range(5) if p[i]==i)
def chiV(g): return fix(g)-1
def sq(g): return comp(g,g)
chars={
 '1':lambda g:1,'eta':sign,'V':chiV,'Veta':lambda g:chiV(g)*sign(g),
 'W':lambda g:(chiV(g)**2+chiV(sq(g)))/2-1-chiV(g),
 'X':lambda g:(chiV(g)**2-chiV(sq(g)))/2}
chars['Weta']=lambda g:chars['W'](g)*sign(g)
order=['1','eta','V','Veta','W','Weta','X']
# check orthonormality
for a in order:
  for b in order:
    ip=sum(chars[a](g)*chars[b](g) for g in G)/120
    assert abs(ip-(a==b))<1e-9,(a,b,ip)
# subgroups
J=[g for g in G if g[4]==4]
# F20: affine maps t->ut+v on F5 as permutations of 0..4
F20=[]; tau={}
for u in range(1,5):
  for v in range(5):
    p=tuple((u*t+v)%5 for t in range(5)); F20.append(p)
    # primitive quartic char: 2 is generator mod 5; tau(2)=i
    k={1:0,2:1,4:2,3:3}[u]; tau[p]=1j**k
T=[g for g in G if set([g[0],g[1]])=={0,1}]
def alpha(g): return -1 if g[0]==1 else 1  # sign on S2 factor {0,1}
def ind_decomp(H,lam):
  return {R: sum((lam(h).conjugate() if isinstance(lam(h),complex) else lam(h))*chars[R](h) for h in H)/len(H) for R in order}
def show(name,H,lam):
  d=ind_decomp(H,lam); print(name, {k:round(abs(v),6) if abs(v)>1e-9 else 0 for k,v in d.items() if abs(v)>1e-9})
show('Ind_J 1',J,lambda g:1)
show('Ind_J eta',J,sign)
show('Ind_F20 1',F20,lambda g:1)
show('Ind_F20 eta',F20,sign)
show('Ind_F20 tau',F20,lambda g:tau[g])
show('Ind_T alpha',T,alpha)
show('Ind_T alpha*eta',T,lambda g:alpha(g)*sign(g))
# sign restricted to F20 equals tau^2?
print('sign|F20==tau^2', all(abs(sign(g)-tau[g]**2)<1e-9 for g in F20))
