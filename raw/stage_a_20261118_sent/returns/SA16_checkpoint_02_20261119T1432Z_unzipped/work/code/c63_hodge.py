#!/usr/bin/env python3
"""Cote63 periods, Hodge splitting, real structure and exact zero-locus bounds."""
from pathlib import Path
import sympy as s,mpmath as mp,json,math
mp.mp.dps=70;out={}
def sigma(n):return sum(d for d in range(1,n+1) if n%d==0)
def e2(tau,N=160):
 q=mp.exp(2j*mp.pi*tau)
 return 1-24*sum(sigma(n)*q**n for n in range(1,N+1))
def e2star(tau):return e2(tau)-3/(mp.pi*mp.im(tau))
def delta(tau,N=160):
 q=mp.exp(2j*mp.pi*tau)
 return q*mp.fprod((1-q**n)**24 for n in range(1,N+1))
def fmt(v):return mp.nstr(v,45)
tau=mp.mpc('0.3','1.1');A=mp.pi**2/3*e2(tau)
etas=[-A,-tau*A+2j*mp.pi]
alpha=-(etas[1]-mp.conj(tau)*etas[0])/(tau-mp.conj(tau))
out['period_normalization']={'tau':fmt(tau),'eta1':fmt(etas[0]),'eta2':fmt(etas[1]),'alpha_periods':fmt(alpha),'alpha_E2star':fmt(mp.pi**2/3*e2star(tau)),'residual':fmt(alpha-mp.pi**2/3*e2star(tau))}
out['quasiperiod_sums']=[]
for N in [10,30,100]:
 row={'N':N,'shape':'|m|,|n|<=N'}
 for i,w in enumerate([mp.mpf(1),tau]):
  exc=(1,0) if i==0 else(0,1)
  val=-3/w+w*w*sum(1/((m+n*tau)**2*(m+n*tau-w)) for m in range(-N,N+1) for n in range(-N,N+1) if(m,n) not in[(0,0),exc])
  # |m+n*tau|>=0.7 max(|m|,|n|), and for the tail |a-w|>=|a|/2.
  bound=16*abs(w)**2/(mp.mpf('0.7')**3*N)
  row[f'eta{i+1}']=fmt(val);row[f'error{i+1}']=fmt(abs(val-etas[i]));row[f'rigorous_tail_bound{i+1}']=fmt(bound)
  assert abs(val-etas[i])<bound
 out['quasiperiod_sums'].append(row)
m,n,T,Q=s.symbols('m n tau abs_tau_squared')
den=(m+n*T)**2*(m-1+n*T)*(m+(n-1)*T)
correct=((m-1)*T**2+n*T**3-(n-1)*Q-m*Q/T)/den
line480=((m-1)*T**2+n*T**3-(n-1)*Q+m*Q/T)/den
line490=(n*T**4+(m-1)*T**3+(n-1)*Q*T+m*Q)/(T*den)
out['scan71_symbolic_residuals']={'line480_minus_correct':s.factor(line480-correct),'line490_minus_correct':s.factor(line490-correct),'missing_factor3_constant_residual':2*(1-Q)/T}
R=s.Rational(1,200);P=(1+4*R+R**2)/(1-R)**4
exp_lower=sum(s.Rational(27,5)**k/s.factorial(k) for k in range(21))
out['zero_locus_certificates']={'r_bound':'exp(-pi sqrt3)<1/200, because pi>3.14,sqrt3>1.73 imply pi sqrt3>5.4 and the finite Taylor lower bound for exp(5.4)>200','exp_5_4_partial_sum_gt200':bool(exp_lower>200),'sum_n3_rn_over_r_at_bound':P,'P_lt_21_over20':bool(P<s.Rational(21,20)),'imaginary_tail_over_first_lt':P-1,'derivative_bound_upper':48*10*s.Rational(3,800)*s.Rational(21,20),'derivative_bound_lt3':bool(48*10*s.Rational(3,800)*s.Rational(21,20)<3),'argument':'On F, imaginary part has sign -sin(2pi x); on x=0 and x=1/2 the real value increases strictly with y. Modularity supplies the zeros i and rho, so these are the only orbits.'}
out['sample_E2star']={name:fmt(e2star(v)) for name,v in [('i',1j),('rho',mp.mpc(-.5,mp.sqrt(3)/2)),('3i',3j),('generic',tau)]}
real_a=-mp.pi*3/3*e2star(3j)
out['actual_elliptic_bound_counterexample']={'tau':'3i','rho':3,'alpha_real_structure':fmt(real_a),'abs_alpha_squared':fmt(abs(real_a)**2),'greater_than1':bool(abs(real_a)**2>1),'tail_bound':'|E2(3i)-1|<=24*r*(1+r)/(1-r)^3, r=exp(-6pi); much smaller than1e-5.'}
ar,ab,rho=s.symbols('alpha alphabar rho',real=False)
beta=-2*s.I*rho;c=(ar*ab-1)/beta
M=s.Matrix([[ar,c],[beta,ab]])
Mbar=s.Matrix([[ab,-c],[-beta,ar]])
residual=s.simplify(M*Mbar-s.eye(2))
assert residual==s.zeros(2)
assert s.factor(M.det())==1
out['real_structure_matrix_residual']=residual
out['determinant']=s.factor(M.det())
out['sigma_identity']=s.factor(4*rho*c/(2*s.I))
out['canonical_phase']={'formula':'phase(E2*(tau)^6/Delta(tau))','generic_value':fmt((e2star(tau)**6/delta(tau))/abs(e2star(tau)**6/delta(tau))),'scope':'Defined away from j=0,1728. Real analytic, independent of SL2Z representative and 12th-root choice. No holomorphy asserted.'}
txt=json.dumps(out,ensure_ascii=False,indent=2,default=str)+'\n'
(Path(__file__).resolve().parents[1]/'outputs/c63_hodge.json').write_text(txt);print(txt)
