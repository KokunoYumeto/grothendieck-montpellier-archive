#!/usr/bin/env python3
"""Independent all-q and finite odd-C2 audit.

No author arithmetic, selected rows, or result records are imported.
The finite Fourier routines are this reviewer's previously audited code.
The new polynomial parser uses exact Fraction coefficients in Q[q,t].
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import ast,hashlib,json,time,itertools
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square
from audit_a7_core import polynomial,cyclo
from flint import fmpz_poly

B=Path(__file__).resolve().parent
SRC=B.parents[1]/'imprimitive/odd_c2'

def clean(p):return {k:v for k,v in p.items() if v}
def add(a,b,sign=1):
 p=a.copy()
 for k,v in b.items():p[k]=p.get(k,F(0))+sign*v
 return clean(p)
def mul(a,b):
 p={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():p[i+k,j+l]=p.get((i+k,j+l),F(0))+u*v
 return clean(p)
def val(a):
 if isinstance(a,ast.Constant):
  assert type(a.value)==int;return clean({(0,0):F(a.value)})
 if isinstance(a,ast.Name):
  assert a.id in ['q','t'];return {(int(a.id=='q'),int(a.id=='t')):F(1)}
 if isinstance(a,ast.UnaryOp):
  assert isinstance(a.op,(ast.USub,ast.UAdd));return {k:(-v if isinstance(a.op,ast.USub) else v) for k,v in val(a.operand).items()}
 assert isinstance(a,ast.BinOp)
 p=val(a.left)
 if isinstance(a.op,ast.Pow):
  assert isinstance(a.right,ast.Constant) and type(a.right.value)==int and a.right.value>=0
  z={(0,0):F(1)}
  for _ in range(a.right.value):z=mul(z,p)
  return z
 r=val(a.right)
 if isinstance(a.op,ast.Add):return add(p,r)
 if isinstance(a.op,ast.Sub):return add(p,r,-1)
 if isinstance(a.op,ast.Mult):return mul(p,r)
 assert isinstance(a.op,ast.Div) and set(r)=={(0,0)}
 return {k:v/r[0,0] for k,v in p.items()}
def parse(s):return val(ast.parse(s,mode='eval').body)
def scale(p,c):return clean({k:v*c for k,v in p.items()})
def shift(p,q0):
 z={}
 for (i,j),a in p.items():
  for k in range(i+1):z[k,j]=z.get((k,j),F(0))+a*comb(i,k)*q0**(i-k)
 return clean(z)
def positive(p):assert all(j==0 and a>=0 for (i,j),a in p.items())
def swap(p):return {k:v*(-1)**k[1] for k,v in p.items()}

def main():
 start=time.perf_counter();raw=(SRC/'unipotent_data.json').read_bytes();data=json.loads(raw)
 assert data['basis_order']==['1','a1','a2','b','c','d1','d2']
 # Independent transcription of the six printed basis rows (the sign of
 # sqrt(sq) only exchanges each paired label).
 a=['(q*q+1)/2','(1+q*t)/2','(1-q*t)/2','(q+1)/2','(1-q)/2','(1+t)/2','(1-t)/2']
 b=['q*(q-1)**2/2','q*(1-q)/2','q*(1-q)/2','0','q','0','0']
 c=['q*(q*q+1)/2','q*(q+1)/2','q*(q+1)/2','0','q','0','0']
 d=['(q-1)**2*(q*q+1)/2','(1-q)/2+q*(q-1)*(1+t)/2','(1-q)/2+q*(q-1)*(1-t)/2','(1-q)/2','(1-3*q)/2','(1-t)/2','(1+t)/2']
 aa=list(map(parse,a));dd=list(map(parse,d))
 bases=[[parse('1')]*7,aa,list(map(swap,aa)),list(map(parse,b)),list(map(parse,c)),dd,list(map(swap,dd))]
 assert bases==[[parse(x) for x in r] for r in data['basis_rows']]
 rs={}
 for name,cs in data['indexed_restriction_vectors'].items():
  assert len(cs)==7 and all(type(x)==int for x in cs)
  rs[name]=[]
  for j in range(7):
   z={}
   for i,k in enumerate(cs):z=add(z,scale(bases[i][j],k))
   rs[name].append(z)
 # Direct published Table2 rows, not the four inconsistent indexed
 # restriction formulas. These were read separately in the source.
 z=['(q+1)**2*(q*q+1)/2','(q+1)/2+q*(q+1)*(1-t)/2','(q+1)/2+q*(q+1)*(1+t)/2','(1+3*q)/2','(1+q)/2','(1-t)/2','(1+t)/2']
 zz=['(q**4-1)/2','(q-1)/2+q*(q+1)*(t-1)/2','(q-1)/2-q*(q+1)*(t+1)/2','(q-1)/2','-(q+1)/2','(t-1)/2','-(t+1)/2']
 rs['xi41']=list(map(parse,z));rs['xi42']=list(map(swap,rs['xi41']))
 rs['xi41prime']=list(map(parse,zz));rs['xi42prime']=list(map(swap,rs['xi41prime']))
 assert rs=={n:[parse(x) for x in r] for n,r in data['expanded_rows'].items()}
 assert len(rs)==44
 out={'status':'PASS','method':'new exact Fraction polynomial audit; reviewer-owned rational-trace Fourier, no author arithmetic',
      'unipotent_input_sha256':hashlib.sha256(raw).hexdigest(),'generic_types':0,'generic_entries':0,'small_tables':[],'small_rows':0,'small_spectra':0,'fusions':0}
 small={'theta3','theta4','theta7','theta8'}
 for name,row in rs.items():
  if name=='1':continue
  deg=row[0];positive(shift(add(deg,parse('(q*q-1)/2'),-1),7))
  if name not in small:positive(shift(add(deg,parse('q*(q-1)**2/2'),-1),7))
  for v in row[1:]:
   sp=shift(v,7);assert all(j<=1 for i,j in sp)
   bound={}
   for (i,j),a in sp.items():
    if j==0:bound[i,0]=bound.get((i,0),F(0))+abs(a)
    else:
     bound[i,0]=bound.get((i,0),F(0))+3*abs(a)
     bound[i+1,0]=bound.get((i+1,0),F(0))+abs(a)/2
   positive(add(scale(shift(deg,7),F(1,2)),bound,-1));out['generic_entries']+=1
  out['generic_types']+=1
 positive(shift(parse('(q-1)**2-4*q'),7))
 assert (out['generic_types'],out['generic_entries'])==(43,258)
 # Exact polynomial arithmetic for every universal inequality in the
 # written proof. Endpoints are checked only after these all-q identities.
 positive(shift(parse('q*q-4*q-1'),7))
 positive(shift(parse('q**3-5*q*q-49*q+5'),11))
 assert F(2,3)*(1-F(1,7**3))>=F(1,2)
 assert F(1,2)*F(2,3)*(1-F(1,9))==F(8,27)>F(1,4)
 assert F(6*7,7-3)==F(21,2)<24
 assert 7*6**2//2==126>84 and 9*8**2//2==288>54
 assert 24**2>84 and 40**2>54
 assert all(rs[n][1].get((1,1),F(0))!=0 for n in small)

 raw=(SRC/'character_inputs.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()=='6824ca705e8619733ced3c7aceab6e145b7b45735fa56a9990ed7607eb6f7a73'
 data=json.loads(raw);ts={t['name']:t for t in data['tables']}
 assert set(ts)=={'2.S4(5)','2.S4(5).2','S4(7)','S4(7).2','S4(9)','S4(9).2_1','S4(9).2_2','S4(9).2_3'}
 chars={n:[[encode(z) for z in r] for r in t['characters']] for n,t in ts.items()}
 minima={};degrees={}
 for name,t in ts.items():
  assert ('origin: ATLAS of finite groups' in t['information']) if 'S4(5)' in name else ('Dixon' in t['information'])
  cs=chars[name];assert len(cs)==len(t['orders'])==len(t['sizes'])
  assert all(len(c)==len(cs) for c in cs)
  assert sum(c[0]**2 for c in cs)==sum(t['sizes'])==t['order']
  if 'fusion' in t:
   u=ts[t['core']];fu=t['fusion'];assert t['order']==2*u['order']
   assert [i for i,j in enumerate(fu) if j==1]==[0]
   assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fu))
   assert all(sum(s for s,k in zip(u['sizes'],fu) if k==j)==t['sizes'][j-1] for j in set(fu))
   pp={x['prime']:x['map'] for x in t['power_maps']}
   for p in u['power_maps']:assert all(fu[k-1]==pp[p['prime']][j-1] for j,k in zip(fu,p['map']))
   out['fusions']+=1
  rec={'table':name,'rows':0,'spectra':0,'minimum_ratio':'1'};minrat=F(1)
  for i,c in enumerate(cs):
   a=c[0]
   if a<=1:continue
   if 'fusion' in t:
    norm=sum(s*rational_mean_abs_square(c[j-1]) for s,j in zip(u['sizes'],fu))/u['order']
    assert norm.denominator==1
    if norm!=1:continue
    assert tuple(c[j-1] for j in fu) in {tuple(r) for r in chars[t['core']]}
   else:degrees[name]=min(a,degrees.get(name,a))
   rec['rows']+=1;out['small_rows']+=1
   for j,z in enumerate(c):
    if abs_square(z)[1]==(a*a,):continue
    ms=spectrum(t,c,j);nu=a-max(ms);assert 4*nu>=a
    minrat=min(minrat,F(nu,a));rec['spectra']+=1;out['small_spectra']+=1
  rec['minimum_ratio']=str(minrat);out['small_tables'].append(rec)
  minima[t['core']]=min(minima.get(t['core'],F(1)),minrat)
 assert (out['small_rows'],out['small_spectra'],out['fusions'])==(485,37502,5)
 assert degrees=={'2.S4(5)':12,'S4(7)':25,'S4(9)':41}
 assert minima=={'2.S4(5)':F(4,13),'S4(7)':F(9,25),'S4(9)':F(16,41)}
 # Reconstruct a separate global-column transcription match directly from
 # the original full finite rows, not the author's cross-check results.
 # Doubling clears every rational polynomial coefficient; quadratic Gauss
 # sums supply the square root for q5 and q7, while q9 uses t=3.
 out['unipotent_finite_comparison']=[]
 for field,prime,name in [(5,5,'2.S4(5)'),(7,7,'S4(7)'),(9,3,'S4(9)')]:
  t=ts[name];n=prime if field!=9 else 1
  root=fmpz_poly([3]) if field==9 else sum((polynomial([prime,[int(i==a*a%prime) for i in range(prime)]],prime) for a in range(prime)),fmpz_poly())
  assert (root*root)%cyclo(n)==fmpz_poly([field if field%4==1 else -field])
  def evaluate(p):
   aa=sum(v*field**i for (i,j),v in p.items() if j==0)
   bb=sum(v*field**i for (i,j),v in p.items() if j==1)
   assert (2*aa).denominator==(2*bb).denominator==1
   return tuple(int(x) for x in ((fmpz_poly([int(2*aa)])+int(2*bb)*root)%cyclo(n)).coeffs())
  source={tuple(evaluate(v) for v in row) for row in rs.values()}
  def ppow(o):
   while o>1 and o%prime==0:o//=prime
   return o==1
  cols=[j for j,o in enumerate(t['orders']) if ppow(o)]
  assert len(cols)==7 and cols[0]==0
  actual=[tuple(tuple(int(x) for x in (2*polynomial(z,n)%cyclo(n)).coeffs()) for z in [row[j] for j in cols]) for row in t['characters']]
  matches=[]
  for perm in itertools.permutations(range(1,7)):
   order=(0,)+perm
   if all(tuple(row[j] for j in order) in source for row in actual):matches.append([j+1 for j in order])
  assert matches
  out['unipotent_finite_comparison'].append({'q':field,'table':name,'rows':len(actual),'columns':[j+1 for j in cols],'matching_permutations':matches})
 assert sum(r['rows'] for r in out['unipotent_finite_comparison'])==186
 out['minimum_by_core']={n:str(x) for n,x in minima.items()};out['degree_minima']=degrees
 out['finite_input_sha256']=hashlib.sha256(raw).hexdigest()
 out['proof_sha256']=hashlib.sha256((SRC/'odd_c2_all_fields_section.tex').read_bytes()).hexdigest()
 out['finite_proof_sha256']=hashlib.sha256((SRC/'finite_odd_c2_section.tex').read_bytes()).hexdigest()
 out['seconds']=round(time.perf_counter()-start,6)
 (B/'audit_odd_c2.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))

if __name__=='__main__':main()
