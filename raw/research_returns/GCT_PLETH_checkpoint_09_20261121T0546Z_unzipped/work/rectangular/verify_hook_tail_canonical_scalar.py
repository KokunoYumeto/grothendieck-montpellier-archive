"""R050: literal normalized monomial pairing of Vandermonde/affine minors."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations,combinations
from math import factorial,prod,comb
import csv
from verify_second_row_two_rank_law import product_form
HERE=Path(__file__).resolve().parent

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def determinant(a):
    return sum(sign(p)*prod(a[i][p[i]] for i in range(len(a))) for p in permutations(range(len(a))))
def falling(a,d):return prod(range(a-d+1,a+1))

def sample(m,n,tag):
    xs=[i+1 if tag==0 else (i+1)*(i+2) for i in range(n)]
    us=[2+i%3 if tag==0 else (-1)**i*(i+2) for i in range(n)]
    ws=[tuple(x**j for j in range(1,m)) for x in xs]
    ell=[(u,)+tuple(u*x for x in w) for u,w in zip(us,ws)]
    form=product_form(ell)
    fn=factorial(n)
    pairing={}
    for p in range(m):
        for q in range(m):
            beta=[p]+[0]*(m-2)
            if q:beta[q-1]+=1
            d=sum(beta)
            pairing[p,q]=form.get((n-d,)+tuple(beta),0)*factorial(n-d)*prod(factorial(x) for x in beta)
    # Expand BOTH determinant permutations and pair each original row monomial.
    perms=[(p,sign(p)) for p in permutations(range(m))]
    numerator=0
    for p,sp in perms:
        for q,sq in perms:
            numerator+=sp*sq*prod(pairing[p[i],q[i]] for i in range(m))
    population=0
    for I in combinations(range(n),m):
        vandermonde=prod(xs[j]-xs[i] for i,j in combinations(I,2))
        affine=determinant([(1,)+ws[i] for i in I])
        population+=vandermonde*affine
    assert population
    return F(numerator,fn**m),prod(us),population

def main():
    rows=[]
    for m in range(2,7):
        ns=(m,m+1,m+2) if m<=5 else (6,)
        for n in ns:
            for tag in ((0,1) if m<=5 else (1,)):
                base,u,population=sample(m,n,tag)
                for a in (m,m+1,m+3):
                    literal=comb(a,m)*u**(a-m)*base
                    scalar=F((-1)**comb(m,2)*falling(a,m)*prod(factorial(j) for j in range(1,m)),
                             n*prod(falling(n,d) for d in range(2,m+1)))
                    target=u**a*population
                    assert literal==scalar*target,(m,a,n,tag,literal,scalar,target)
                    rows.append(dict(m=m,a=a,n=n,sample=tag,literal_pairing=str(literal),
                      target_highest_polynomial=target,canonical_scalar=str(scalar),status='PASS'))
        print('checked literal hook-tail scalar m',m,'cases',len(rows),flush=True)
    with (HERE/'HOOK_TAIL_CANONICAL_SCALAR_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS literal hook-tail scalar',len(rows),flush=True)

if __name__=='__main__':main()
