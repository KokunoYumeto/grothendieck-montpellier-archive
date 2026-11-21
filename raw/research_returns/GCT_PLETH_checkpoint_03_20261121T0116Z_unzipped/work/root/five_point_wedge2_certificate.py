"""Exact G-018 character and positive Newton certificate."""
from pathlib import Path
from fractions import Fraction
from math import comb
import csv
import json
import sys
import sympy as s

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rectangular'))
from verify_rectangular import character, partitions, z

labels = list(partitions(5))
classes = ((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
t, u = s.symbols('t u')
maximum = 359
characters = {}
rational = {}
degrees = {}

for cyc in classes:
    m1 = cyc.count(1)
    e = m1-1
    sign = (-1)**(5-len(cyc))
    denom = s.cancel(s.prod(1-u**c for c in cyc)/(1-u))
    h = 1/denom
    even = s.cancel((h+h.subs(u,-u))/2)
    odd = s.cancel((h-h.subs(u,-u))/(2*u))
    def to_t(expr):
        numerator, denominator = s.fraction(s.cancel(expr))
        def convert(poly):
            terms = s.Poly(poly,u).terms()
            assert all(exponent[0] % 2 == 0 for exponent,value in terms)
            return sum(value*t**(exponent[0]//2) for exponent,value in terms)
        return s.cancel(convert(numerator)/convert(denominator))
    a0, a1 = to_t(even), to_t(odd)
    jets = m1*t/denom.subs(u,t)
    c1 = a1-jets
    c2 = (a0-1)/t-jets
    series = s.cancel(sign*(e*c1-c2))
    numerator = s.cancel(series*(1-t**60)**4)
    assert s.denom(numerator) == 1
    numerator = s.Poly(numerator,t)
    assert numerator.degree() <= 239
    rational[str(cyc)] = str(s.factor(series))
    degrees[str(cyc)] = numerator.degree()

    trace = [1]+[0]*(2*maximum+2)
    for length in cyc:
        for degree in range(length,len(trace)):
            trace[degree] += trace[degree-length]
    trace = [trace[0]]+[trace[i]-trace[i-1] for i in range(1,len(trace))]
    values=[]
    for k in range(maximum+1):
        jet=m1*trace[k-1] if k else 0
        values.append(sign*(e*(trace[2*k+1]-jet)-(trace[2*k+2]-jet)))
    characters[cyc]=values
    for k,value in enumerate(values):
        assert value == sum(int(numerator.nth(j))*comb((k-j)//60+3,3)
                            for j in range(k%60,min(k,numerator.degree())+1,60))

tables={}
rows=[]
initial={}
for mu in labels:
    values=[]
    for k in range(maximum+1):
        value=sum(Fraction(character(mu,cyc)*characters[cyc][k],z(cyc)) for cyc in classes)
        assert value.denominator==1 and value>=0,(mu,k,value)
        values.append(int(value))
    table=[]
    for residue in range(60):
        difference=[values[residue+60*q] for q in range(4)]
        newton=[]
        while difference:
            newton.append(difference[0])
            difference=[b-a for a,b in zip(difference,difference[1:])]
        assert all(c>=0 for c in newton),(mu,residue,newton)
        assert newton[3]>0
        for q in range(6):
            assert values[residue+60*q]==sum(c*comb(q,j) for j,c in enumerate(newton) if j<=q)
        rows.append({'label':','.join(map(str,mu)),'residue':residue,
                     **{f'delta{j}':c for j,c in enumerate(newton)},'outcome':'PASS'})
        table.append(newton)
    tables[','.join(map(str,mu))]=table
    initial[','.join(map(str,mu))]=values[:20]
    print(mu,'initial',values[:12], 'minima',[min(row[j] for row in table) for j in range(4)])

(HERE/'FIVE_POINT_WEDGE2_NEWTON_TABLE.json').write_text(json.dumps({
    'statement':'G-018','period':60,'polynomial_degree':3,'labels':tables,
    'class_rational_series':rational,'common_numerator_degrees':degrees,
    'initial_coefficients':initial},indent=2)+'\n')
with (HERE/'FIVE_POINT_WEDGE2_CHECK.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
    writer.writeheader();writer.writerows(rows)
receipt=('PASS: all7 character series have denominator dividing(1-t^60)^4 and numerator degree<=239.\n'
         'PASS: 2520 class coefficients match exact rational functions.\n'
         'PASS: 2520 irreducible coefficients are nonnegative integers.\n'
         'PASS: all1680 Newton coefficients are nonnegative; all420 cubic coefficients are positive.\n'
         'PASS: every residue polynomial agrees at six successive integer arguments.\n')
(HERE/'FIVE_POINT_WEDGE2_CHECK.txt').write_text(receipt)
print(receipt)
