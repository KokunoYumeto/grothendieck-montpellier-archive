"""Replay the cone certificate via direct standard-T multiplication (not direct dual action)."""
import pathlib,sys,json,time,itertools
base=pathlib.Path(__file__).resolve().parent/'dependencies';sys.path.insert(0,str(base))
import e4lib as L
out=pathlib.Path(__file__).resolve().parent
cert=json.loads((out/'mixed_cone_certificate.json').read_text())
basis=[];rows=[];P=1000003;V=2;piv=[];t=time.time();D={-2:1,0:2,2:1}
def add_rank(X):
 x={k:sum(c*pow(V,e,P) for e,c in p.items())%P for k,p in X.items()};x={k:a for k,a in x.items() if a}
 for col,r in piv:
  if col not in x:continue
  m=x[col]
  for k,a in r.items():
   z=(x.get(k,0)-m*a)%P
   if z:x[k]=z
   elif k in x:del x[k]
 if not x:return False
 col=min(x);iv=pow(x[col],-1,P);x={k:a*iv%P for k,a in x.items()};piv.append((col,x));return True
for rec in cert['records']:
 X=L.word_elt(tuple(rec['word']))
 for c in rec['corrections']:
  p={0:c['multiple']}
  for _ in range(c['D_power']):p=L.pmul(p,D)
  X=L.tadd(X,L.tscale(basis[c['donor_index']],p))
 co=L.dualcoords(X)
 assert all(c>=0 for p in co.values() for c in p.values()),rec['index']
 assert add_rank(X),rec['index']
 basis.append(X)
 rows.append({'index':rec['index'],'coordinates':len(co),'positive_monomials':sum(len(p) for p in co.values()),'min_coefficient':min(c for p in co.values() for c in p.values()),'max_coefficient':max(c for p in co.values() for c in p.values())})
 if len(rows)%20==0:print('verified',len(rows),'seconds',time.time()-t,flush=True)
assert len(rows)==114
(out/'positive_basis_verified.json').write_text(json.dumps({'verified_elements':114,'all_coefficients_nonnegative':True,'independent_mod_prime':P,'v_specialization':V,'rows':rows,'seconds':time.time()-t},indent=2))
print('PASS114 direct T-basis construction, KL conversion and modular independence',time.time()-t)
