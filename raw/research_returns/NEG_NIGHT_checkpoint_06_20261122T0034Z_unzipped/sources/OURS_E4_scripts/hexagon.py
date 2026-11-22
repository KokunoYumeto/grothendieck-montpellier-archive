# Symmetries of the structure constants of VIII's E^opp(3) (b2 = -(q+1)^2/q): trace form, dual basis, orbits of the six P-F-E3-01 triples
import os,sys,json,itertools
os.environ['HN']='3'; here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
exec(open(os.path.join(here,'e3_reproduce.py')).read().split('w0=max')[0])
B=basis(-1); names=list(B); E={k:L.comb(B[k]) for k in names}
e=L.e
def tau(X): return tosym(X.get((e,e),{}))          # tau(T_a (x) T_b) = [a=b=e], the tensor square of the standard Hecke trace
G=sp.Matrix([[sp.factor(tau(L.rmul_comb(E[x],B[y]))) for y in names] for x in names])
print('Gram matrix of tau on E^opp(3) (nonzero pattern):')
for i,x in enumerate(names): print(' %-7s'%x, ''.join('X' if G[i,j]!=0 else '.' for j in range(len(names))))
sym=all(sp.simplify(G[i,j]-G[j,i])==0 for i in range(10) for j in range(10))
print('tau symmetric on these:',sym)
cell=['g2_1','g2_12','g2_21','g2_2']; idx=[names.index(c) for c in cell]
print('Gram on the chi^2 cell (rows/cols g2_1,g2_12,g2_21,g2_2):'); print(sp.Matrix([[G[i,j] for j in idx] for i in idx]))
