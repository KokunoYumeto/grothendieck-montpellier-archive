from pathlib import Path
import sys,json,time
sys.path.insert(0,str(Path('sources/OURS_counting_scripts').resolve()))
import consult_a157422a_dimension_ring_search as S
import dimension_ring_minimal_pairs as M

start=time.monotonic()
LIMIT=7952
lin=[[c-2*a,a] for a in range(1,20,2) for c in range(2,42,2) if 2*a+c<=68]
deltas=[d for d in ([b,a,1] for a in range(-3,12,2) for b in range(-6-2*a,22-2*a,2)) if S.ge_abs(d,S.dtrue) and S.ev(d,4)<=12]
L1=[l for l in ([c-6*a-2*b,b,a] for a in range(0,12,2) for b in range(1-4*a,30-4*a,2) for c in range(2,32,2)) if S.ge_abs(l,S.l1true)]
L2=[l for l in ([c-6*a-2*b,b,a] for a in range(1,12,2) for b in range(-4*a,30-4*a,2) for c in range(2,32,2)) if S.ge_abs(l,S.l2true)]
print('candidates',len(lin),len(deltas),len(L1),len(L2),flush=True)
# Lower bounds use total sum d and |c| over the 113 nonunit constants.
abs_total=4424
cap=abs_total+2*LIMIT
best=[]
base=0
for W in lin:
    w=S.ev(W,4)
    WW=S.mul(W,W)
    for U1 in lin:
        u1=S.ev(U1,4)
        for U2 in lin:
            u2=S.ev(U2,4)
            den=w*w-u1*u2
            if den<=0:continue
            for d1 in deltas:
                dd1=S.ev(d1,4)
                for d2 in deltas:
                    dd2=S.ev(d2,4)
                    g1n=4*w*(w*dd1+u1*dd2);g2n=4*w*(w*dd2+u2*dd1)
                    if g1n%den or g2n%den:continue
                    g1=g1n//den;g2=g2n//den
                    if g1<48 or g2<48 or (g1*g2)%w:continue
                    ss=g1*g2//w
                    if ss<576:continue
                    lower=ss+20*(g1+g2)+200*w+20*(u1+u2+32)+(dd1+dd2)*82
                    if lower>cap:continue
                    Den=S.sub(WW,S.mul(U1,U2))
                    G1=S.divexact(S.mul(S.mul(S.D,W),S.add(S.mul(W,d1),S.mul(U1,d2))),Den)
                    G2=S.divexact(S.mul(S.mul(S.D,W),S.add(S.mul(W,d2),S.mul(U2,d1))),Den)
                    if G1 is None or G2 is None or not S.ge_abs(G1,S.g1) or not S.ge_abs(G2,S.g2):continue
                    Sc=S.divexact(S.mul(G1,G2),W)
                    if Sc is None or not S.ge_abs(Sc,S.s0):continue
                    base+=1
                    ok=[]
                    for la_list,dd,gg,uu,kk,ddd in [(L1,d1,G2,U1,S.K1,dd1),(L2,d2,G1,U2,S.K2,dd2)]:
                        oo=[]
                        for la in la_list:
                            lv=S.ev(la,4)
                            if lv<4:continue
                            part=S.divexact(S.mul(S.mul(W,dd),S.sub(S.DD,la)),gg)
                            if part is None:continue
                            vv=S.add(S.mul(S.D,uu),part)
                            if not S.ge_abs(vv,kk):continue
                            cost=20*S.ev(vv,4)+ddd*(26+14*lv)
                            oo.append((cost,la,vv))
                        ok.append(sorted(oo,key=lambda x:x[0]))
                    if not all(ok):continue
                    # score depends only on evaluating each positive polynomial at q=1.
                    const=ss+20*(g1+g2)+200*w+20*(u1+u2)
                    for cost1,la1,v1 in ok[0]:
                        for cost2,la2,v2 in ok[1]:
                            score=(const+cost1+cost2-abs_total)//2
                            if score>LIMIT:continue
                            par={'S':Sc,'G':{1:G1,2:G2},'W':W,'delta':{1:d1,2:d2},'Lam':{1:la1,2:la2}}
                            try: sc=M.score(par)
                            except AssertionError: continue
                            if sc is None or sc[0]>LIMIT:continue
                            out={'score':sc,'W':W,'U1':U1,'U2':U2,'delta1':d1,'delta2':d2,'Lambda1':la1,'Lambda2':la2,'G1':G1,'G2':G2,'S':Sc,'V1':v1,'V2':v2}
                            best.append(out)
                            if sc[0]<LIMIT:
                                LIMIT=sc[0];cap=abs_total+2*LIMIT
                                print('IMPROVEMENT',json.dumps(out),flush=True)
                                Path('work/gct/dimension_search_best.json').write_text(json.dumps(out,indent=2))
    if time.monotonic()-start>3600:break
print('base',base,'limit',LIMIT,'seconds',time.monotonic()-start,flush=True)
Path('work/gct/dimension_search_results.json').write_text(json.dumps({'seconds':time.monotonic()-start,'base':base,'best':best,'limit':LIMIT},indent=2))
