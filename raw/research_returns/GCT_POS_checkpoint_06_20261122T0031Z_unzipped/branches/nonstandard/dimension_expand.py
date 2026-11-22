"""Extend the supplied dimension-ring search to negative D intercepts and higher top coefficients."""
import sys,pathlib,json,time,itertools
base=pathlib.Path(__file__).resolve().parent/'dependencies'
sys.path.insert(0,str(base))
import consult_a157422a_dimension_ring_search as S
import dimension_ring_minimal_pairs as M
out=pathlib.Path(__file__).resolve().parent
# From symmetric q coefficients A at +-2, B at +-1 and C at zero.
def quad(A,B,C):return S.trim([2*A-2*B+C,B-4*A,A])
lin=[[c-2*a,a] for a in (1,3,5) for c in (2,4,6) if 2*a+c<=16]
deltas=[quad(a,b,c) for a in (1,3,5) for b in (1,3,5) for c in (0,2,4,6) if 2*a+2*b+c<=20]
L1=[quad(a,b,c) for a in (0,2,4,6) for b in (1,3,5,7,9) for c in (2,4,6,8,10,12) if 2*a+2*b+c<=32]
L2=[quad(a,b,c) for a in (1,3,5,7) for b in (0,2,4,6,8) for c in (2,4,6,8,10,12) if 2*a+2*b+c<=32]
print('counts',len(lin),len(deltas),len(L1),len(L2),flush=True)
start=time.time();found=[]
for wi,W in enumerate(lin):
 ww=S.mul(W,W)
 for U1 in lin:
  for U2 in lin:
   den=S.sub(ww,S.mul(U1,U2));d4=S.ev(den,4);d7=S.ev(den,7);d11=S.ev(den,11)
   if min(d4,d7,d11)<=0:continue
   for d1 in deltas:
    for d2 in deltas:
     n1=S.mul(S.mul(S.D,W),S.add(S.mul(W,d1),S.mul(U1,d2)))
     n2=S.mul(S.mul(S.D,W),S.add(S.mul(W,d2),S.mul(U2,d1)))
     if any(S.ev(n,d)%S.ev(den,d) for n in (n1,n2) for d in (4,7,11)):continue
     g1=S.divexact(n1,den);g2=S.divexact(n2,den)
     if g1 is None or g2 is None:continue
     if not (S.ge_abs(g1,S.g1) and S.ge_abs(g2,S.g2)):continue
     sc=S.divexact(S.mul(g1,g2),W)
     if sc is None or not S.ge_abs(sc,S.s0):continue
     found.append((W,U1,U2,d1,d2,g1,g2,sc))
 print('W',wi+1,'solutions',len(found),'seconds',time.time()-start,flush=True)
best=[];nfull=0
for W,U1,U2,d1,d2,g1,g2,sc in found:
 ok1=[];ok2=[]
 for la in L1:
  t=S.divexact(S.mul(S.mul(W,d1),S.sub(S.DD,la)),g2)
  if t is not None and S.ge_abs(S.add(S.mul(S.D,U1),t),S.K1):ok1.append(la)
 for la in L2:
  t=S.divexact(S.mul(S.mul(W,d2),S.sub(S.DD,la)),g1)
  if t is not None and S.ge_abs(S.add(S.mul(S.D,U2),t),S.K2):ok2.append(la)
 for la1 in ok1:
  for la2 in ok2:
   par={'S':sc,'G':{1:g1,2:g2},'W':W,'delta':{1:d1,2:d2},'Lam':{1:la1,2:la2}}
   try:score=M.score(par)
   except AssertionError:continue
   if score is None:continue
   nfull+=1
   if not best or score[0]<best[0]['score'][0]:
    best=[{'score':score,'parameters':par,'U1':U1,'U2':U2}];print('NEW BEST',best[-1],flush=True)
   elif score[0]==best[0]['score'][0]:best.append({'score':score,'parameters':par,'U1':U1,'U2':U2})
res={'counts':[len(lin),len(deltas),len(L1),len(L2)],'preliminary_solutions':len(found),'full_solutions':nfull,'best':best,'seconds':time.time()-start}
(out/'dimension_expand_certificate.json').write_text(json.dumps(res,indent=2))
print('FINAL',res,flush=True)
