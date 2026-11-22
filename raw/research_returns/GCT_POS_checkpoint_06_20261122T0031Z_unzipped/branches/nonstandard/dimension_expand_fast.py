"""Broader exact dimension search; numerical residue prefilter, every survivor checked over Z[D]."""
import sys,pathlib,json,time,itertools,numpy as np
base=pathlib.Path(__file__).resolve().parent/'dependencies';sys.path.insert(0,str(base))
import consult_a157422a_dimension_ring_search as S
import dimension_ring_minimal_pairs as M
out=pathlib.Path(__file__).resolve().parent
quad=lambda A,B,C:S.trim([2*A-2*B+C,B-4*A,A])
Ws=[[c-2*a,a] for a in range(1,10,2) for c in range(2,21,2) if 2*a+c<=20]
Us=[[c-2*a,a] for a in range(1,16,2) for c in range(2,33,2) if 2*a+c<=40]
deltas=[quad(a,b,c) for a in range(1,8,2) for b in range(1,10,2) for c in range(0,13,2) if 2*a+2*b+c<=24]
L1=[quad(a,b,c) for a in range(0,14,2) for b in range(1,20,2) for c in range(2,25,2) if 2*a+2*b+c<=60]
L2=[quad(a,b,c) for a in range(1,14,2) for b in range(0,20,2) for c in range(2,25,2) if 2*a+2*b+c<=60]
print('counts',len(Ws),len(Us),len(deltas),len(L1),len(L2),flush=True)
vals={p:np.array([S.ev(d,p) for d in deltas],dtype=np.int64) for p in (4,7,11)}
start=time.time();found=[];seen=set();cut=20328
for wi,W in enumerate(Ws):
 w4=S.ev(W,4);ww=S.mul(W,W)
 for U1 in Us:
  u14=S.ev(U1,4)
  for U2 in Us:
   u24=S.ev(U2,4);den4=w4*w4-u14*u24
   if den4<=0:continue
   g14=4*w4*(w4*vals[4][:,None]+u14*vals[4][None,:])
   g24=4*w4*(w4*vals[4][None,:]+u24*vals[4][:,None])
   mask=(g14%den4==0)&(g24%den4==0)
   g1q=g14//den4;g2q=g24//den4
   lower=g1q*g2q//w4+20*(g1q+g2q)+200*w4+20*(u14+u24+32)+82*(vals[4][:,None]+vals[4][None,:])
   mask &= lower<=cut
   if not mask.any():continue
   den=S.sub(ww,S.mul(U1,U2))
   for p in (7,11):
    wp=S.ev(W,p);u1p=S.ev(U1,p);u2p=S.ev(U2,p);dp=S.ev(den,p)
    if dp<=0:mask[:]=False;break
    n1=p*wp*(wp*vals[p][:,None]+u1p*vals[p][None,:]);n2=p*wp*(wp*vals[p][None,:]+u2p*vals[p][:,None])
    mask &= (n1%dp==0)&(n2%dp==0)
   for di,dj in zip(*np.where(mask)):
    d1=deltas[di];d2=deltas[dj]
    n1=S.mul(S.mul(S.D,W),S.add(S.mul(W,d1),S.mul(U1,d2)))
    n2=S.mul(S.mul(S.D,W),S.add(S.mul(W,d2),S.mul(U2,d1)))
    g1=S.divexact(n1,den);g2=S.divexact(n2,den)
    if g1 is None or g2 is None:continue
    if not (S.ge_abs(g1,S.g1) and S.ge_abs(g2,S.g2)):continue
    sc=S.divexact(S.mul(g1,g2),W)
    if sc is None or not S.ge_abs(sc,S.s0):continue
    par=(W,U1,U2,d1,d2,g1,g2,sc)
    found.append(par)
 print('W',wi+1,'solutions',len(found),'seconds',round(time.time()-start,2),flush=True)
(out/'dimension_fast_preliminary.json').write_text(json.dumps(found))
best=[];nfull=0
for ii,(W,U1,U2,d1,d2,g1,g2,sc) in enumerate(found):
 # modular obstruction at D mod 2 catches most candidates exactly through ge_abs below.
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
 if ii%100==0:print('full phase',ii,'of',len(found),'full',nfull,'seconds',round(time.time()-start,2),flush=True)
res={'counts':[len(Ws),len(Us),len(deltas),len(L1),len(L2)],'preliminary_solutions':len(found),'full_solutions':nfull,'best':best,'seconds':time.time()-start,'mass_lower_bound':cut}
(out/'dimension_fast_certificate.json').write_text(json.dumps(res,indent=2))
print('FINAL',res,flush=True)
