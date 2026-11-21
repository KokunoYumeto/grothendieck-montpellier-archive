"""Independent complete G018 rational extension and 1680-constant audit."""
from pathlib import Path
from math import comb
import json
import sympy as s
from verify_rectangular import partitions,character,z

HERE=Path(__file__).resolve().parent
table=json.loads((HERE.parent/"root"/"FIVE_POINT_WEDGE2_NEWTON_TABLE.json").read_text())
x,t=s.symbols("x t")
classes=partitions(5)
traces={}
out=[]
for cyc in classes:
    raw=[1]+[0]*480
    for length in cyc:
        for j in range(length,481):raw[j]+=raw[j-length]
    standard=[raw[j]-(raw[j-1] if j else 0) for j in range(481)]
    m=cyc.count(1);sg=(-1)**(5-len(cyc))
    traces[cyc]=[sg*((m-1)*standard[2*k+1]-standard[2*k+2]
                     -m*(m-2)*(standard[k-1] if k else 0)) for k in range(240)]
    gen=(1-x)/s.prod(1-x**j for j in cyc)
    ev=s.cancel((gen+gen.subs(x,-x))/2)
    od=s.cancel((gen-gen.subs(x,-x))/(2*x))
    def even_convert(rat):
        a,b=s.fraction(rat)
        ans=[]
        for p in (a,b):
            pol=s.Poly(p,x)
            assert all(monom[0]%2==0 for monom,c in pol.terms())
            ans.append(sum(c*t**(monom[0]//2) for monom,c in pol.terms()))
        return ans[0]/ans[1]
    ev=even_convert(ev);od=even_convert(od)
    series=s.cancel(sg*((m-1)*od-(ev-1)/t
                     -m*(m-2)*t*gen.subs(x,t)))
    given=s.sympify(table["class_rational_series"][str(cyc)])
    assert s.cancel(series-given)==0
    pol=s.Poly(s.cancel((1-t**60)**4*series),t)
    assert pol.degree()<=239
    out.append(f"PASS exact rational class {cyc}; common numerator degree {pol.degree()}")
for mu in partitions(5):
    values=[]
    for k in range(240):
        v=sum((120//z(cyc))*character(mu,cyc)*traces[cyc][k] for cyc in classes)
        assert v%120==0 and v>=0
        values.append(v//120)
    coefficients=[]
    for r in range(60):
        row=[sum((-1)**(j-h)*comb(j,h)*values[r+60*h] for h in range(j+1))
             for j in range(4)]
        assert min(row)>=0
        coefficients.append(row)
    assert coefficients==table["labels"][",".join(map(str,mu))]
    out.append(f"PASS all240 Newton entries for {mu}")
out.append("PASS all7 rational extension identities and all1680 positive Newton constants")
(HERE/"WEDGE2_NEWTON_INDEPENDENT_CHECK.txt").write_text("\n".join(out)+"\n")
print("\n".join(out))
