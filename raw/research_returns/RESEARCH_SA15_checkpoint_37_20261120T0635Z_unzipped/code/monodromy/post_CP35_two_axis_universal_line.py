"""Exact universal two-axis product cross determinant on one fixed line.

The displayed finite line witness is extended to two arbitrary finite
nonzero points (a,b),(c,d) on y^2+y=x^3.  All coefficient reductions use
the two monic curve equations.  No general nodality/monodromy assertion.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,traceback,signal
import sympy as sp
from sympy.polys.matrices import DomainMatrix

start=time.perf_counter()
output=Path(__file__).with_suffix('.output.json')
record={'status':'RUNNING','actual_utc':datetime.now(timezone.utc).isoformat()}
def save():
 record['runtime_seconds']=time.perf_counter()-start
 output.write_text(json.dumps(record,indent=2)+'\n')
def alarm(signum,frame):raise TimeoutError('Retained 60-second universal-line bound')
signal.signal(signal.SIGALRM,alarm);signal.alarm(60);save()
try:
 a,b,c,d,t=sp.symbols('a b c d t')
 def matrices(x,y):
  return [sp.Matrix([[1,x,0],[x,0,y],[0,y+1,x]]),
          sp.Matrix([[0,0,1],[0,1,0],[1,0,0]]),
          sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])]
 A=matrices(a,b);B=matrices(c,d)
 T=sp.Matrix([[0,0,t],[1,1+t,1+t],[1+t,1,1+t]])
 matrix=sum((T[i,j]*sp.kronecker_product(A[i],B[j]) for i in range(3) for j in range(3)),sp.zeros(9))
 domain=sp.GF(2).poly_ring(a,b,c,d,t)
 det=DomainMatrix.from_Matrix(matrix).convert_to(domain).det()
 expr=domain.to_sympy(det)
 record['unreduced_term_count']=len(sp.Poly(expr,a,b,c,d,t,modulus=2).terms());save()
 G=sp.groebner([b*b+b+a**3,d*d+d+c**3],b,d,a,c,t,modulus=2)
 reduced=G.reduce(expr)[1]
 record['reduced_polynomial']=str(reduced)
 record['reduced_terms']=[[list(m),int(v)%2] for m,v in sp.Poly(reduced,a,b,c,d,t,modulus=2).terms()]
 record['reduced_term_count']=len(record['reduced_terms'])
 derivative=sp.Poly(sp.diff(reduced,t),a,b,c,d,t,modulus=2).as_expr()
 record['derivative']=str(derivative)
 record['f_plus_t_derivative']=str(sp.Poly(reduced+t*derivative,a,b,c,d,t,modulus=2).as_expr())
 record['t_coefficients']={str(m[0]):str(coef) for m,coef in sp.Poly(reduced,t).terms()}
 assert sp.Poly(reduced.subs({a:0,b:0,c:0,d:0})-(t**9+t+1),t,modulus=2).is_zero
 record['status']='PASS-UNIVERSAL-LINE-COEFFICIENTS'
except Exception as exc:
 record['status']='FAILED_OR_TIMEOUT';record['error']=str(exc);record['traceback']=traceback.format_exc()
finally:
 signal.alarm(0);save()
 print(json.dumps({k:v for k,v in record.items() if k!='reduced_terms'},indent=2))
