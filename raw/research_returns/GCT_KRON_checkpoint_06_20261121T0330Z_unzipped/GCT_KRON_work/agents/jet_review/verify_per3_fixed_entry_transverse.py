"""Independent exact verification of the per3 projected Jacobian witness."""
from pathlib import Path
from itertools import permutations
from datetime import datetime,timezone
import json,hashlib
import sympy as sp
p=Path(__file__).with_name('per3_fixed_entry_transverse_certificate.json');data=json.loads(p.read_text());b=data;A=b['pencil_coefficients'];r=7

def mul(P,Q):
 out={}
 for a,c in P.items():
  for bb,d in Q.items():
   e=tuple(x+y for x,y in zip(a,bb));out[e]=out.get(e,0)+c*d
 return {e:c for e,c in out.items() if c}
def per_polynomial(matrix):
 total={};zero=(0,)*r
 for perm in permutations(range(3)):
  term={zero:1}
  for i,j in enumerate(perm):
   linear={tuple(int(a==k) for a in range(r)):c for k,c in enumerate(matrix[i][j]) if c}
   term=mul(term,linear)
  for e,c in term.items():total[e]=total.get(e,0)+c
 return {e:c for e,c in total.items() if c}

base=per_polynomial(A);target=[tuple(e) for e in b['target_monomials']];J=b['Jacobian']
for i in range(3):
 for j in range(3):
  for k in range(r):
   varied=[[list(v) for v in row] for row in A];varied[i][j][k]+=1
   out=per_polynomial(varied);col=(3*i+j)*r+k
   for row,e in enumerate(target):assert out.get(e,0)-base.get(e,0)==J[row][col]
print('All63 derivative columns match full permanent polynomial differences exactly.',flush=True)
cols=b['pivot_source_columns'];M=sp.Matrix([[row[j] for j in cols] for row in J]);det=int(M.det(method='domain-ge'))
assert det and det%data['prime']==b['selected_minor_mod_prime']
result={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','status':'PASS','independent_method':'Full permanent expanded as six products of three linear forms; changing each single source coefficient byone gives exactly its derivative because the permanent is linear in each entry. All63 columns compared exactly with cofactor construction. Selected49x49 determinant computed overintegers via Sympy DomainMatrix Gaussian elimination.','integer_determinant':str(det),'modulus':data['prime'],'residue':det%data['prime'],'omitted_source_columns':[j for j in range(63) if j not in cols],'all_derivative_columns_checked':63,'input_certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
out=Path(__file__).with_name('per3_fixed_entry_transverse_independent_certificate.json');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
