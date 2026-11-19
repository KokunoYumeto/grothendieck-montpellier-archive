"""Exact polynomial checks for the explicit refinement of the BMS example.

Run with Python and SymPy. This checks smoothness over algebraic closure,
not just absence of singular rational points: a unit Groebner ideal on
each standard chart certifies the empty geometric singular locus.
"""
import itertools, json, pathlib, time
import sympy as s
start=time.monotonic()
v=s.symbols('x1 x2 x3 y1 y2 y3'); x=v[:3]; y=v[3:]
Q=[x[i]**2+x[(i+1)%3]*x[(i+2)%3]-y[i]**2-x[i]*y[i] for i in range(3)]
action={y[i]:-x[i]-y[i] for i in range(3)}
invariance=[s.expand(q.xreplace(action)-q) for q in Q]
assert invariance==[0,0,0]
J=s.Matrix([[s.diff(q,z) for z in v] for q in Q])
minors=[s.expand(J[:,cols].det()) for cols in itertools.combinations(range(6),3)]
charts=[]
for a in range(6):
    variables=tuple(z for j,z in enumerate(v) if j!=a)
    polynomials=[s.Poly(q.subs(v[a],1),*variables,modulus=2).as_expr() for q in Q+minors]
    local_start=time.monotonic()
    gb=s.groebner(polynomials,*variables,modulus=2,order='grevlex')
    unit=(len(gb.polys)==1 and gb.polys[0].as_expr()==1)
    assert unit
    charts.append({'chart':str(v[a])+'=1','groebner_basis':[str(q.as_expr()) for q in gb.polys],
                   'seconds':round(time.monotonic()-local_start,6)})
# E: y^2+xy=x^3+1, with a1=1,a2=a3=a4=0,a6=1.
b2,b4,b6,b8=1,0,4,1
disc=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert disc==-433 and disc%2==1
# The odd Hensel root u of u^3+u^2+64=0 gives P=(u/4,-u/8).
u=1; hensel=[]
for bits in range(1,33):
    modulus=2**bits
    if (u**3+u**2+64)%modulus:
        u+=modulus//2
    assert (u**3+u**2+64)%modulus==0
    assert (3*u*u+2*u)%2==1
    hensel.append({'bits':bits,'u_mod_2n':u})
out={'scope':'Exact universal involution identity; geometric special-fibre smoothness in all six charts; elliptic discriminant and Hensel root.',
     'quadrics':[str(q) for q in Q], 'invariance':[str(q) for q in invariance],
     'smoothness_charts':charts,'elliptic_discriminant':disc,
     'hensel_root_last':hensel[-1], 'total_seconds':round(time.monotonic()-start,6),
     'limitation':'Does not choose a final surface hypersurface; its existence and selection algorithm are proved in the paper.'}
path=pathlib.Path(__file__).resolve().parents[1]/'outputs'/'k3_lift_check.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
