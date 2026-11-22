"""Independent exact polynomial checks for DGJ J6 cubic pencil; no claim of checking Chow theory."""
import sympy as s,time,json,pathlib
start=time.perf_counter()
x=s.symbols('x0:6');t=s.symbols('t');F=sum(x[i]**3 for i in [0,1,2,4,5])+x[3]**2*x[4]
grad=[s.diff(F,v) for v in x]
charts=[]
for j in range(6):
 vs=[v for i,v in enumerate(x) if i!=j]
 G=s.groebner([f.subs(x[j],1) for f in [F]+grad],*vs,modulus=5)
 charts.append(G.contains(s.Integer(1)))
assert all(charts)
y=x[:5];D=s.expand(F.subs(x[5],t*x[4]));gd=[s.diff(D,v) for v in y]
generic=[]
for j in range(5):
 vs=[v for i,v in enumerate(y) if i!=j]
 G=s.groebner([f.subs(y[j],1) for f in [D]+gd],*vs,domain=s.GF(5).frac_field(t))
 generic.append(G.contains(s.Integer(1)))
assert all(generic)
Ds=sum(x[i]**3 for i in [0,1,2])+x[3]**2*x[4]
G0=s.groebner([Ds]+[s.diff(Ds,v) for v in y],*y,modulus=5)
Dinf=F.subs(x[4],0);yi=[x[i] for i in [0,1,2,3,5]]
Ginf=s.groebner([Dinf]+[s.diff(Dinf,v) for v in yi],*yi,modulus=5)
E=sum(x[i]**3 for i in [0,1,2]);Echecks=[]
for j in range(3):
 vs=[x[i] for i in range(3) if i!=j]
 G=s.groebner([f.subs(x[j],1) for f in [E]+[s.diff(E,x[i]) for i in range(3)]],*vs,modulus=5)
 Echecks.append(G.contains(s.Integer(1)))
assert all(Echecks)
out={"scope":"Exact Jacobian and equation checks in characteristic5; ruled-surface intersection and trace claims proved separately.","X_equation":str(F),"X_gradient_mod5":[str(s.Poly(g,*x,modulus=5).as_expr()) for g in grad],"X_all_six_projective_charts_jacobian_unit":charts,"generic_D_equation":str(D),"generic_D_all_five_charts_jacobian_unit":generic,"D_c0_homogeneous_jacobian_basis":[str(p.as_expr()) for p in G0.polys],"D_infinity_homogeneous_jacobian_basis":[str(p.as_expr()) for p in Ginf.polys],"elliptic_axis_base_three_charts_smooth":Echecks,"elapsed_seconds":time.perf_counter()-start}
p=pathlib.Path(__file__).with_suffix('.output.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
