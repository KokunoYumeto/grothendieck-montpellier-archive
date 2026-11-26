# All rows of the outer-six table. No weight expansion, so no large dictionaries:
# <s_mu[h_n], s_lam> = sum_rho chi^mu(rho)/z_rho * [product over parts r of p_r[h_n]] paired with s_lam
import sys,csv
from collections import defaultdict
from fractions import Fraction as Fr
exec(open('kron.py').read().split('def kron(')[0])
def expansion(rho,n):
    tot={():Fr(1)}
    for r in rho:
        new=defaultdict(Fr)
        for t,c in tot.items():
            for sig in partitions(n):
                new[tuple(sorted(t+tuple(r*x for x in sig),reverse=True))]+=c/zee(sig)
        tot=new
    return tot
m=6; power={}; plethysm={}
rows=list(csv.DictReader(open(sys.argv[1]),delimiter='\t'))
seen=set(); bad=[]; per=defaultdict(int)
for r in rows:
    n=int(r['n'])
    mu=tuple(int(x) for x in r['outer'].split(','))
    lam=tuple(int(x) for x in (r['output'] or '').split(',') if x and int(x)>0)
    if (mu,n) not in plethysm:
        tot=defaultdict(Fr)
        for rho in partitions(m):
            c=mn(mu,rho)
            if not c: continue
            if (rho,n) not in power: power[rho,n]=expansion(rho,n)
            for t,v in power[rho,n].items(): tot[t]+=Fr(c,zee(rho))*v
        plethysm[mu,n]=tot
    v=sum(c*mn(lam,t) for t,c in plethysm[mu,n].items())
    per[n]+=1; seen.add((n,mu,lam))
    if v!=int(r['power_sum_MN']) or v!=int(r['weight_alternant']): bad.append((r,v))
want={(n,mu,lam) for n in range(4) for mu in partitions(6) for lam in partitions(6*n)}
print('rows',len(rows),'per n',dict(per),'mismatches',len(bad),bad[:5])
print('distinct',len(seen),'expected',len(want),'missing',len(want-seen),'extra',len(seen-want))
