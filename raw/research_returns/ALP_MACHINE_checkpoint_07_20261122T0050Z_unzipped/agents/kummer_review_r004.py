"""Independent AM-R004 review checks. Central inputs are never rewritten."""
from pathlib import Path
from fractions import Fraction as F
import contextlib, io, json, hashlib, datetime
import sympy as s
import mpmath as mp

root=Path('/workspace/scratch/66d4177eb491')
script=root/'work/scripts/jacobian_theta_certificate.py'
report=root/'work/research/jacobian_period_theta.md'
saved=root/'work/evidence/theta_certificate.json'
source=script.read_text()
# Execute every proof assertion, while suppressing only directory/output writes.
source=source.replace("dest.parent.mkdir(parents=True,exist_ok=True)", "pass")
source=source.replace("dest.write_text(json.dumps(output,indent=2))", "pass")
ns={'__file__':str(script),'__name__':'__independent_review__'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source,str(script),'exec'),ns)
old=json.loads(saved.read_text())
for k,v in ns['output'].items():
    if k!='date_utc':
        assert old[k]==v,(k,old[k],v)
# Explicitly certify the sine-monotonicity and denominator side conditions.
assert 0 < 3*ns['pi'][1]/7 < ns['pi'][0]/2
assert F(314159,100000)*F(6,25)>F(3,4)
assert 0<ns['u']<1 and 0<ns['tail_ratio']<1

t=s.symbols('t')
phi=sum(t**k for k in range(7))
red=lambda e:s.rem(s.Poly(s.expand(e),t),s.Poly(phi,t)).as_expr()
A=s.Matrix([[t**(2*i*j) for j in range(3)] for i in range(1,4)])
B=s.Matrix([[sum(t**(i*(2*k+1)) for k in range(j,3)) for j in range(3)] for i in range(1,4)])
tau=s.Matrix([
[-t**5-1,-t**5-t**4-t**2-2,t**5+t**3+t],
[-t**5-t**4-t**2-2,t**5-t**4+2*t**3+t,t**5+t**3+t**2+1],
[t**5+t**3+t,t**5+t**3+t**2+1,t**2]])
assert (A*tau-B).applyfunc(red)==s.zeros(3)
assert tau==tau.T
# The gamma intersection matrix from the displayed symplectic basis.
J=s.zeros(6)
for i in range(3):
    J[i,3+i]=1;J[3+i,i]=-1
gamma=s.zeros(6)
for j in range(3):
    gamma[j,2*j]=1
    gamma[3+j,2*j+1]=1
    if j+1<3:gamma[3+j+1,2*j+1]=-1
E=gamma.T*J*gamma
expected=s.Matrix(6,6,lambda j,k:1 if k==j+1 else -1 if j==k+1 else 0)
assert E==expected
assert abs(gamma.det())==1
assert abs(s.discriminant(phi,t))==7**5

mp.mp.dps=70
zeta=mp.e**(2j*mp.pi/7)
An=mp.matrix([[zeta**(2*i*j) for j in range(3)] for i in range(1,4)])
Bn=mp.matrix([[sum(zeta**(i*(2*k+1)) for k in range(j,3)) for j in range(3)] for i in range(1,4)])
taun=An**-1*Bn
Y=mp.matrix([[mp.im(taun[i,j]) for j in range(3)] for i in range(3)])
cs=[mp.mpc(0,-2)/7*mp.beta(mp.mpf(i)/7,mp.mpf('0.5'))*(zeta**i-1) for i in range(1,4)]
P=mp.diag(cs)*An
G=P*Y*P.H
known=[2*mp.pi/7*mp.gamma(mp.mpf(i)/7)*mp.gamma(mp.mpf('0.5')-mp.mpf(i)/7)/
       (mp.gamma(1-mp.mpf(i)/7)*mp.gamma(mp.mpf('0.5')+mp.mpf(i)/7)) for i in range(1,4)]
# Diagnostic agreement only: the proof is the exact bilinear identity.
err=max(abs(G[i,j]-(known[i] if i==j else 0)) for i in range(3) for j in range(3))
assert err<mp.mpf('1e-12')
vol=mp.mpf(7)**mp.mpf('2.5')/8*mp.fprod(abs(c)**2 for c in cs)
assert abs(mp.det(G)-vol)<mp.mpf('1e-12')
out={
'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'who':'GPT-6 Astra Pro; ALP_MACHINE /root/kummer_extension; inherited effort not separately exposed',
'checked_report_sha256':hashlib.sha256(report.read_bytes()).hexdigest(),
'checked_script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
'central_outputs_rewritten':False,
'exact_assertions':[
'all original certificate assertions executed',
'all retained certificate fields match saved evidence, excluding timestamp',
'sine arguments lie below pi/2, so endpoint monotonicity applies',
'pi_lower*(6/25)>3/4 and both geometric-series ratios are in (0,1)',
'A*tau=B modulo cyclotomic polynomial, exact',
'tau symmetric, exact',
'gamma basis unimodular and intersection matrix matches trace form, exact',
'cyclotomic polynomial discriminant absolute value 7^5, exact'],
'numerical_diagnostics_only':{
'Hodge_Gram_max_error':str(err),
'Hodge_diagonal':[str(x) for x in known],
'volume_determinant_error':str(abs(mp.det(G)-vol))},
'proof_review_scope':[
'complete report and script whole-read',
'Tadokoro Proposition3.2 checked from local primary PDF text',
'path beta integral, symplectic change, trace signs and period normalization independently recomputed',
'Chern gauge and anti-holomorphic connection term independently recomputed',
'shifted Gaussian bound, Cauchy minimization and level M cancellation independently recomputed',
'probability-Haar L2 orthogonality/unfolding independently recomputed'],
'result':'PASS in stated complex geometric and archimedean scope; no finite-integral or MainX conclusion'
}
dest=root/'work/agents/kummer_review_AM_R004.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':out['result'],'exact_checks':len(out['exact_assertions']),'diagnostic_Gram_error':str(err),'output':str(dest)},indent=2))

