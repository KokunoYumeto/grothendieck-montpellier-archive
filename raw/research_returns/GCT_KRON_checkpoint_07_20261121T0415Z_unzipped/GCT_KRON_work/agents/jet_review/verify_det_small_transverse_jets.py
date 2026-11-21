"""Independent symbolic and integer verification of the n4/n5 witnesses."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as sp
p=Path(__file__).with_name('det_small_transverse_jet_certificate.json');data=json.loads(p.read_text());z=sp.symbols('x1:8');out=[]
for rec in data['records']:
 n=rec['n'];A=sp.Matrix([[sum(c*z[k] for k,c in enumerate(entry)) for entry in row] for row in rec['pencil_coefficients']]);target=[tuple(a) for a in rec['target_monomials']];J=rec['Jacobian']
 for i in range(n):
  for j in range(n):
   cof=sp.Poly(sp.expand((-1)**(i+j)*A.minor_submatrix(i,j).det(method='berkowitz')),*z)
   coefs={e:int(c) for e,c in cof.terms()}
   for k in range(7):
    col=(n*i+j)*7+k
    for row,e in enumerate(target):
     reduced=list(e);reduced[k]-=1
     value=coefs.get(tuple(reduced),0) if reduced[k]>=0 else 0
     assert J[row][col]==value
 print(f'n={n}: all symbolic cofactor columns match.',flush=True)
 cols=rec['pivot_columns'];M=sp.Matrix([[row[c] for c in cols] for row in J]);det=int(M.det(method='domain-ge'))
 assert det and det%data['prime']==rec['selected_minor_mod_prime']
 out.append({'n':n,'rank':len(target),'integer_determinant':str(det),'modulus':data['prime'],'residue':det%data['prime'],'all_columns_checked':n*n*7})
 print(json.dumps(out[-1]),flush=True)
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'PASS','method':'Each full symbolic minor independently calculated by Sympy Berkowitz determinant, expanded as an exact multivariate polynomial, and allsourcecolumns compared; selected squareminors evaluatedoverintegers byDomainMatrix elimination.','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'records':out}
q=p.with_name('det_small_transverse_independent_certificate.json');q.write_text(json.dumps(result,indent=2)+'\n');print(str(q),flush=True)
