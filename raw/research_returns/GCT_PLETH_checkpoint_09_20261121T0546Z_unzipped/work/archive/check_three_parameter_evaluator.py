"""Independent behavior and literal matrix checks for the G020 evaluator."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
from itertools import product,combinations
from math import comb
import importlib.util,json,sys,subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
spec=importlib.util.spec_from_file_location("g020_evaluator",ROOT/"five_point_three_parameter_positive.py")
ev=importlib.util.module_from_spec(spec);spec.loader.exec_module(ev)
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import partitions,character,z

@lru_cache(None)
def schur_plethysm(mu,n):
    result=defaultdict(Fraction)
    for alpha in partitions(5):
        ch=character(mu,alpha)
        if not ch:continue
        term={():Fraction(ch,z(alpha))}
        for length in alpha:
            nxt=defaultdict(Fraction)
            for old,c in term.items():
                for beta in partitions(n):
                    cyc=tuple(sorted(old+tuple(length*r for r in beta),reverse=True))
                    nxt[cyc]+=c/z(beta)
            term=nxt
        for cyc,c in term.items():result[cyc]+=c
    return dict(result)

small=0
for a,k,t,d in product(range(4),repeat=4):
    if a+k+t+d>3:continue
    for mu in ev.LABELS:
        _,_,n,lam=ev.parameters(a,k,t,d,mu)
        direct=sum(c*character(lam,cyc) for cyc,c in schur_plethysm(mu,n).items())
        actual=ev.coefficient(a,k,t,d,mu)
        assert direct==actual,(a,k,t,d,mu,direct,actual)
        small+=1

sq=json.loads((ROOT/"FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json").read_text())["labels"]
odd=json.loads((HERE.parent/"theta"/"outer5"/"Q_PLUS_SYMMETRIC_TABLE.json").read_text())["labels"]
specializations=0
for a,k in [(0,0),(0,1),(1,0),(1,1),(2,2),(59,59),(60,0),(0,60),(61,62),(137,128)]:
    for d,mu in product((0,1),ev.LABELS):
        _,nu,_,_=ev.parameters(a,k,0,d,mu)
        label=",".join(map(str,nu))
        for t,table in ((0,sq),(1,odd)):
            constants=table[label][a%60][k%60]
            expected=sum(constants[4*i+j]*comb(a//60,i)*comb(k//60,j)
                         for i in range(4) for j in range(4))
            assert expected==ev.coefficient(a,k,t,d,mu)
            specializations+=1

summary=json.loads((HERE/"THREE_PARAMETER_ANALYTIC_RECEIPT.json").read_text())
zero_checks=0
for label,triples in summary["zero_triples_in_residue_cube"].items():
    mu=tuple(map(int,label.split(",")))
    for a,k,t in triples:
        d=a%2
        assert ev.coefficient(a,k,t,d,mu)==0
        for axis in range(3):
            args=[a,k,t];args[axis]+=60
            assert ev.coefficient(*args,d,mu)>0
            zero_checks+=1
        zero_checks+=1

# Direct large-degree trace formula uses no residue interpolation.
def direct_trace(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n//2+1)*((n+1)//2+1)
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    return (1,-1,0,0,0)[n%5]
huge=(10**120+61,10**110+62,10**100+63,10**80+1)
for mu in ev.LABELS:
    a,k,t,d=huge
    _,nu,_,_=ev.parameters(a,k,t,d,mu)
    total=0
    for g,(size,ch,fixed) in enumerate(zip(ev.CLASS_SIZES,ev.CHARACTERS[nu],ev.FIXED_LETTERS)):
        ha,hb=direct_trace(g,a),direct_trace(g,a-1)
        total+=size*ch*(ha*direct_trace(g,2*k+t)-hb*direct_trace(g,2*k+t-1)
                       -fixed*direct_trace(g,k-1)*(ha-hb))
    assert total%120==0 and total//120==ev.coefficient(*huge,mu)

def valid(poly,point):
    return (all(sum(c*x for c,x in zip(row,point))==rhs for row,rhs in poly["equalities"])
            and all(sum(c*x for c,x in zip(row,point))<=rhs for row,rhs in poly["inequalities"]))
matrix_cases=0;boundary_points=0;witness_points=0
cases=[(0,0,0),(1,0,0),(2,1,1),(2,3,1),(60,0,0),(0,60,0),(0,0,60),
       (180,120,60),(61,62,63)]
for (a,k,t),mu in product(cases,ev.LABELS):
    polys=ev.polytopes(a,k,t,0,mu)
    qs=(a//60,k//60,t//60)
    total=0
    by_order={}
    for poly in polys:
        assert len(poly["variables"])<=9
        i,j,ell=poly["orders"]
        chains=[list(combinations(range(1,q+1),degree))
                for q,degree in zip(qs,(i,j,ell))]
        total+=poly["constant"]*len(chains[0])*len(chains[1])*len(chains[2])
        by_order[tuple(poly["orders"])]=poly
        for xs,zs,ws in product(*chains):
            for yy in {0,poly["constant"]-1}:
                point=(*qs,yy,*xs,*zs,*ws)
                assert valid(poly,point)
                boundary_points+=1
            assert not valid(poly,(*qs,poly["constant"],*xs,*zs,*ws))
    actual=ev.coefficient(a,k,t,0,mu)
    assert total==actual
    seen=set()
    for item in ev.witnesses(a,k,t,0,mu,limit=100):
        order=tuple(item["orders"]);point=tuple(item["point"])
        assert valid(by_order[order],point)
        assert (order,point) not in seen
        seen.add((order,point));witness_points+=1
    assert len(seen)==min(actual,100)
    matrix_cases+=1

# The lazy generator also supports quotient variables far larger than memory.
for mu in ev.LABELS:
    points=list(ev.witnesses(*huge,mu,limit=2))
    assert len(points)==2
    polys={tuple(p["orders"]):p for p in ev.polytopes(*huge,mu)}
    assert all(valid(polys[tuple(p["orders"])],p["point"]) for p in points)

bad=[(-1,0,0,0,(5,)),(0,True,0,0,(5,)),(0,0,0.0,0,(5,)),
     (0,0,0,0,(4,)),(0,0,0,0,(3,2.0))]
for args in bad:
    try:ev.coefficient(*args)
    except ValueError:pass
    else:raise AssertionError(("accepted invalid input",args))
cli=subprocess.run([sys.executable,str(ROOT/"five_point_three_parameter_positive.py"),
                    "--a","2","--k","3","--t","1","--d","0",
                    "--outer","5","--polytopes","--witnesses","2"],
                   capture_output=True,text=True,check=True)
cli_data=json.loads(cli.stdout)
assert cli_data["coefficient"]==6 and cli_data["witness_count"]==2
assert cli_data["witnesses_truncated"] and len(cli_data["polytopes"])<=36
receipt={"statement":"G020 standard-library evaluator validation","status":"PASS",
         "genuine_Murnaghan_Nakayama_plethysm_cases":small,
         "G019_T042_specializations":specializations,
         "zero_and_direction_checks":zero_checks,
         "large_integer_trace_comparisons":7,
         "matrix_count_cases":matrix_cases,"literal_boundary_points":boundary_points,
         "lazy_witness_points":witness_points,
         "huge_quotient_witness_checks":14,
         "invalid_input_cases":len(bad),"CLI_JSON_check":True}
(HERE/"THREE_PARAMETER_EVALUATOR_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
