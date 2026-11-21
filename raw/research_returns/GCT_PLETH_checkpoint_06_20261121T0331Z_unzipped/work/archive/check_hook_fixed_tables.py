from pathlib import Path
import sympy as s
import json
HERE=Path(__file__).resolve().parent
t=s.symbols("t")
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes=[1,10,15,20,20,30,24]
chars=[[1,1,1,1,1,1,1],[4,2,0,1,-1,0,-1],[5,1,1,-1,1,-1,0],
       [6,0,-2,0,0,0,1],[5,-1,1,-1,-1,1,0],[4,-2,0,1,1,0,-1],
       [1,-1,1,1,-1,-1,1]]
aa=[[4,6,13],[2,3,3,4,4,4,5,5,5,6,6,7],
    [2,3,3,4,4,4,5,5,5,6,6,6,7,7,8],
    [1,2,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,9],
    [2,3,4,4,5,5,5,6,6,6,7,7,8,8,9],
    [3,4,4,5,5,6,6,7,7,8,9,10],[6,7,8]]
bb=[[5,6,7],[],[],[],[],[],[]]
den4=s.prod(1-t**w for w in (2,3,4,5))
den3=s.prod(1-t**w for w in (2,3,5))
traces=[]
for cyc in classes:
    e=cyc.count(1)-1
    H=(1-t)/s.prod(1-t**l for l in cyc)
    traces.append(s.cancel((e-1/t)*H+1/t))
for row in range(7):
    mult=sum(s.Rational(size*chars[row][j],120)*traces[j] for j,size in enumerate(sizes))
    positive=sum(t**r for r in aa[row])/den4+sum(t**r for r in bb[row])/den3
    assert s.cancel(mult-positive)==0
kk=[[0,0,1,0,0,0,0],[0,1,1,1,1,0,0],[1,1,1,1,1,1,0],
    [0,1,1,2,1,1,0],[0,1,1,1,1,1,1],[0,0,1,1,1,1,0],
    [0,0,0,0,1,0,0]]
tags=[sum(kk[r][j]*(len(aa[r])+len(bb[r])) for r in range(7)) for j in range(7)]
assert tags==[15,60,78,90,75,60,15]
assert s.expand(t**4+t**5+2*t**6+t**7-t**9-t**10-t**11+t**13
                -(t**4+t**6+t**13+(1-t**4)*(t**5+t**6+t**7)))==0
receipt={"statement":"Independent T041 fixed rational identities","status":"PASS",
         "rational_identities":7,"cancellation_identity":"5H.15","tag_counts":tags,
         "method":"Exact characters from the actual polarization splitting, compared to the printed positive shifts in every degree.",
         "scope":"Complete geometric proof reviewed separately; no variable coefficient sweep claimed."}
(HERE/"HOOK_FIXED_TABLE_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
