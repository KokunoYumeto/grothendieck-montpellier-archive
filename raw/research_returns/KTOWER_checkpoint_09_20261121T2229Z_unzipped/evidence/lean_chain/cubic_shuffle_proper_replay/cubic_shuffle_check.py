"""Exact cochain/sign and unitriangular-binomial checks for CS.1--10."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import sympy as s

A,B,C,a,b,c = s.symbols('A B C a b c')
half = s.Rational(1,2)
F = A*b-B*a
U,V,W = A+a,B+b,C+c+half*F
Phi = -A*c-half*A*a*b-half*A*A*b
Theta = A*c-C*a-half*A*a*b-half*A*B*a
d_uw = A*C+a*c-U*W
d_uuv = A*A*B+a*a*b-U*U*V
d_ua = -d_uw-half*d_uuv
Omega = -3*half*(A*c-C*a)-s.Rational(1,4)*(A-a)*F
Rdiff = 3*half*d_uw+half*d_uuv
checks = {}
def check(name,expression):
    if isinstance(expression,s.MatrixBase):
        good=all(s.expand(x)==0 for x in expression)
    else:
        good=s.expand(expression)==0
    assert good,name
    checks[name]=True
check('canonical u-u primitive',-half*(A*A+a*a-U*U)-A*a)
check('u-v primitive',-C-half*A*B-c-half*a*b+W+half*U*V-A*b)
check('v-u primitive',C-half*A*B+c-half*a*b-W+half*U*V-B*a)
check('endpoint consecutive identity',Theta+2*Phi+d_ua)
check('BCH consecutive identity',Omega-3*Phi+Rdiff)
check('relative global cocycle transport',-Omega+3*Phi-Rdiff)
E=lambda i,j:s.eye(4)[:,i]*s.eye(4)[j,:]
g=s.eye(4)+A*E(0,1)+A*E(1,2)+B*E(2,3)+half*A*A*E(0,2)+(C+half*A*B)*E(1,3)
h=s.eye(4)+a*E(0,1)+a*E(1,2)+b*E(2,3)+half*a*a*E(0,2)+(c+half*a*b)*E(1,3)
gh=s.eye(4)+U*E(0,1)+U*E(1,2)+V*E(2,3)+half*U*U*E(0,2)+(W+half*U*V)*E(1,3)
def without_center(M):
    R=M.copy();R[0,3]=0;return R
check('defining system matrix law modulo center',without_center(g*h-gh))
q=s.eye(4)-half*E(0,1)
conjugated=q*g*(s.eye(4)+half*E(0,1))
target=g-half*A*E(0,2)
check('binomial block conjugation modulo center',without_center(conjugated-target))
sharifi=A*(c+half*a*b)+(half*A*A-half*A)*b
check('Sharifi sign and primitive difference',sharifi+Phi+half*A*b)
x=s.symbols('x')
fg=B+(C+half*A*B)*x
fh=b+(c+half*a*b)*x
fgh=V+(W+half*U*V)*x
df=s.expand(fg+(1+A*x+half*A*(A-1)*x*x)*fh-fgh)
check('augmentation cocycle modulo I squared',df.coeff(x,0)+x*df.coeff(x,1))
check('second Bockstein exact cochain',df.coeff(x,2)-sharifi)
root=Path(__file__).resolve().parent
text=(root/'cubic_shuffle_comparison.tex').read_text()
stack=[]
for i,line in enumerate(text.splitlines(),1):
    if r'\[' in line: stack.append(i)
    if r'\]' in line:
        assert stack,('unmatched display close',i)
        stack.pop()
assert not stack,stack
report={'status':'PASS all exact shuffle, relative-sign and binomial-matrix identities',
        'checked_utc':datetime.now(timezone.utc).isoformat(),
        'checks':checks,'check_count':len(checks),'display_balance':True,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_sha256':sha256(text.encode()).hexdigest(),
        'scope':'Symbolic identities and exact Bockstein cochain; published properness identification is imported separately; no arithmetic nonvanishing.'}
(root/'cubic_shuffle_check.json').write_text(json.dumps(report,indent=2)+'\n')
print(report['status'],len(checks));print(report['proof_sha256'])
