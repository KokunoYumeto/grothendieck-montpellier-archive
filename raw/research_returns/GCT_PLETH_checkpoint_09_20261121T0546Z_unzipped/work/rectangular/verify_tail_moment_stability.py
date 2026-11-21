"""R046 exact stable evaluation and split-moment normalization checks."""
from pathlib import Path
from functools import lru_cache
from collections import defaultdict,Counter
from fractions import Fraction as F
from math import factorial
import csv,random
from verify_rectangular import partitions,character,z
from verify_outer4_chambers import power_sum
from derive_double_four_moment_matrix import set_partitions
from verify_second_row_two_rank_law import product_form
HERE=Path(__file__).resolve().parent

@lru_cache(None)
def stable_power(D):
    ans=defaultdict(F)
    for rho in partitions(D):
        if 1 in rho:continue
        term={():F(1)}
        for d,m in Counter(rho).items():
            factor=power_sum((m,),d);out=defaultdict(F)
            for x,c in term.items():
                for y,e in factor.items():out[tuple(sorted(x+y,reverse=True))]+=c*e
            term=out
        for x,c in term.items():ans[x]+=c
    return dict(ans)
@lru_cache(None)
def schur_trace(nu,cyc):
    value=F(0)
    for rho in partitions(sum(nu)):
        chi=character(nu,rho)
        if not chi:continue
        trace=1
        for k in rho:trace*=sum(j for j in cyc if k%j==0)-1
        value+=F(chi*trace,z(rho))
    assert value.denominator==1
    return int(value)
def fixed(nu,n):
    value=sum((F(schur_trace(nu,cyc),z(cyc)) for cyc in partitions(n)),F())
    assert value.denominator==1 and value>=0
    return int(value)
def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        w.writeheader();w.writerows(rows)

def main():
    rows=[]
    for D in range(1,11):
        formal=stable_power(D)
        for nu in partitions(D):
            c=sum((v*character(nu,rho) for rho,v in formal.items()),F())
            assert c.denominator==1 and c>=0
            N=(D+nu[0])//2
            for n in (N,N+1):
                value=fixed(nu,n)
                assert value==c,(nu,n,value,c)
                rows.append(dict(D=D,tail=','.join(map(str,nu)),width=nu[0],row_count=n,
                       bound=N,finite_Schur_average=value,formal_moment_multiplicity=int(c),status='PASS'))
        print('stable evaluation checked degree',D,'rows',len(rows),flush=True)
    write('TAIL_MOMENT_STABILITY_CHECK.tsv',rows)
    print('PASS stable evaluation',len(rows),flush=True)
    rng=random.Random(46046);rows=[]
    for d in range(2,9):
        for n in (d,d+1):
            for tag in range(2):
                w=[(rng.randrange(-3,5),rng.randrange(-3,5)) for _ in range(n-1)]
                w.append((-sum(r[0] for r in w),-sum(r[1] for r in w)))
                form=product_form([(1,)+r for r in w])
                powers={(p,q):sum(x**p*y**q for x,y in w)
                        for e in range(1,d+1) for p in range(e+1) for q in (e-p,)}
                for p in range(d+1):
                    q=d-p;labels=(0,)*p+(1,)*q;mobius=0
                    for pi in set_partitions(d):
                        term=1
                        for block in pi:
                            r=sum(labels[i]==0 for i in block);s=len(block)-r
                            term*=(-1)**(len(block)-1)*factorial(len(block)-1)*powers[r,s]
                        mobius+=term
                    expected=F(mobius*factorial(n-d),factorial(n))
                    actual=F(form.get((n-d,p,q),0)*factorial(n-d)*factorial(p)*factorial(q),factorial(n))
                    assert expected==actual,(d,n,tag,p,actual,expected)
                    rows.append(dict(degree=d,n=n,sample=tag,p=p,q=q,
                       product_pairing=str(actual),Mobius_pairing=str(expected),status='PASS'))
    write('GENERAL_SPLIT_MOMENT_CHECK.tsv',rows)
    print('PASS normalized split-moment entries',len(rows),flush=True)
if __name__=='__main__':main()

