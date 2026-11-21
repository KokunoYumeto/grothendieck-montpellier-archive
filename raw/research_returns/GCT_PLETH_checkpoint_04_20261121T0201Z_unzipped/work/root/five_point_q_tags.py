from pathlib import Path
from collections import Counter
from math import gcd
import sys,csv,json
import sympy as s
sys.path.insert(0,str(Path('work/rectangular').resolve()))
from verify_rectangular import partitions,character,z
T=s.symbols('t');labels=list(partitions(5));degrees=(2,4,6,10)
def chiU(cyc):
 c=Counter(cyc);return c[1]*(c[1]-1)//2+c[2]-c[1]
def cpower(cyc,k):
 return tuple(sorted((n//gcd(n,k) for n in cyc for _ in range(gcd(n,k))),reverse=True))
def determinant(cyc):
 es=[s.Integer(1)]
 for i in range(1,6):es.append(s.simplify(sum((-1)**(j-1)*es[i-j]*chiU(cpower(cyc,j)) for j in range(1,i+1))/i))
 return sum((-1)**i*es[i]*T**i for i in range(6))
cs={}
for cyc in labels:
 h=s.cancel((cyc.count(1)-1+T-chiU(cyc)*T**2)*s.prod(1-T**d for d in degrees)/determinant(cyc))
 assert s.denom(h)==1 and s.degree(h,T)<=19
 cs[cyc]=s.Poly(h,T)
rows=[];data=[]
for mu in labels:
 h=s.Poly(s.expand(sum(s.Rational(character(mu,cyc),z(cyc))*cs[cyc].as_expr() for cyc in labels)),T)
 vals=[h.nth(i) for i in range(20)]
 assert all(v>=0 and v.q==1 for v in vals)
 print(mu,vals,'tags',sum(vals))
 rows.append({'outer':','.join(map(str,mu)),**{f'degree_{i}':int(v) for i,v in enumerate(vals)}})
 data.append({'label':mu,'coefficients':[int(v) for v in vals]})
assert sum(character(mu,(1,)*5)*sum(row['coefficients']) for mu,row in zip(labels,data))==4320
with open('work/root/FIVE_POINT_Q_TAGS.tsv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
Path('work/root/FIVE_POINT_Q_TAGS.json').write_text(json.dumps({'parameter_degrees':degrees,'maximum_tag_degree':19,'dimension_of_quotient':4320,'tags':data,'class_denominators':{str(c):str(s.factor(determinant(c))) for c in labels},'class_numerators':{str(c):str(cs[c].as_expr()) for c in labels},'all_exact_character_polynomials_nonnegative':'PASS'},indent=2))
