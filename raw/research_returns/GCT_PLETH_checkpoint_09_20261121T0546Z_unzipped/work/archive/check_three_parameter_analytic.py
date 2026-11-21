"""Independent exhaustive G020 check using seven closed trace polynomials.

No cycle recurrence is used. Forward differences are applied to explicit
polynomial coefficients via universal integer difference matrices.
"""
from pathlib import Path
from math import comb
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
TARGET=HERE.parent/"root"/"FIVE_POINT_THREE_PARAMETER_SUMMARY.json"
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes=[1,10,15,20,20,30,24]
labels=["5","4,1","3,2","3,1,1","2,2,1","2,1,1,1","1,1,1,1,1"]
chars=[[1,1,1,1,1,1,1],[4,2,0,1,-1,0,-1],[5,1,1,-1,1,-1,0],
       [6,0,-2,0,0,0,1],[5,-1,1,-1,-1,1,0],[4,-2,0,1,1,0,-1],
       [1,-1,1,1,-1,-1,1]]
weights=[[size*c for size,c in zip(sizes,row)] for row in chars]

z=s.symbols("z")
closed_series=[
    1/(1-z)**4,
    (1+2*z+z*z)/(1-z*z)**3,
    1/(1-z*z)**2,
    (1+z+z*z)/(1-z**3)**2,
    (1-z+z*z)/(1-z**6),
    1/(1-z**4),
    (1-z)/(1-z**5)]
for cyc,series in zip(classes,closed_series):
    assert s.cancel(series-(1-z)/s.prod(1-z**l for l in cyc))==0
    for shifted in (series,z*series):
        n,d=s.fraction(s.cancel(shifted*(1-z**60)**4))
        assert d==1 and s.Poly(n,z).degree()<=239

def polynomial(g,n):
    """Power coefficients of h_g(n+60q), valid also at n=-1."""
    assert n>=-1
    if g==0:
        return [(n+1)*(n+2)*(n+3)//6,10*(3*n*n+12*n+11),1800*n+3600,36000]
    if g==1:
        return [(n//2+1)*((n+1)//2+1),30*(n+2),900,0]
    if g==2:
        return [n//2+1,30,0,0] if n%2==0 else [0,0,0,0]
    if g==3:
        return [n//3+1,20,0,0]
    if g==4:
        return [[1,-1,1,0,0,0][n%6],0,0,0]
    if g==5:
        return [int(n%4==0),0,0,0]
    return [[1,-1,0,0,0][n%5],0,0,0]

# Exact difference operators on q^b and (2q+r)^b, b=0,1,2,3.
DD=[[sum((-1)**(i-u)*comb(i,u)*u**b for u in range(i+1))
     for b in range(4)] for i in range(4)]
MM=[[[sum((-1)**(j+l-u-v)*comb(j,u)*comb(l,v)*(2*u+v)**b
           for u in range(j+1) for v in range(l+1))
      for b in range(4)] for l in range(4)] for j in range(4)]
assert all(MM[j][l]==[0]*4 for j in range(4) for l in range(4) if j+l>3)
def apply(op,poly):return sum(a*b for a,b in zip(op,poly))
da=[[[apply(DD[i],polynomial(g,r)) for r in range(60)] for i in range(4)] for g in range(7)]
db=[[[apply(DD[i],polynomial(g,r-1)) for r in range(60)] for i in range(4)] for g in range(7)]
DA=np.array(da,dtype=np.int64);DB=np.array(db,dtype=np.int64)
base=2*np.arange(60)[:,None]+np.arange(60)[None,:]
minima={label:{} for label in labels};maxima={label:{} for label in labels}
hashes={label:hashlib.sha256() for label in labels}
zeros={};zero_positions=[];entry_count=0;largest_bound=0;bounds={}
target=json.loads(TARGET.read_text())
assert target["verified_entries"]==96768000
for i in range(4):
    for j in range(4):
        for l in range(4):
            hp=[[apply(MM[j][l],polynomial(g,n)) for n in range(178)] for g in range(7)]
            hm=[[apply(MM[j][l],polynomial(g,n-1)) for n in range(178)] for g in range(7)]
            # Python integers bound each product, subtraction, weighted product
            # and running sum before any vectorized arithmetic is performed.
            class_bounds=[]
            for g,cyc in enumerate(classes):
                b=max(map(abs,da[g][i]))*max(map(abs,hp[g]))
                b+=max(map(abs,db[g][i]))*max(map(abs,hm[g]))
                if l==0:
                    b+=cyc.count(1)*max(abs(a-bb) for a,bb in zip(da[g][i],db[g][i]))*max(map(abs,db[g][j]))
                class_bounds.append(b)
            bound=max(sum(abs(w)*b for w,b in zip(row,class_bounds)) for row in weights)
            assert max(class_bounds+[bound])<2**63
            largest_bound=max(largest_bound,bound)
            slot=f"{i},{j},{l}";bounds[slot]=bound
            HP=np.array(hp,dtype=np.int64);HM=np.array(hm,dtype=np.int64)
            class_arrays=[]
            for g,cyc in enumerate(classes):
                arr=DA[g,i,:,None,None]*HP[g,base][None,:,:]-DB[g,i,:,None,None]*HM[g,base][None,:,:]
                if l==0:
                    arr-=cyc.count(1)*(DA[g,i]-DB[g,i])[:,None,None]*DB[g,j][None,:,None]
                class_arrays.append(arr)
            identically_zero=True
            for label,ww in zip(labels,weights):
                numerator=np.zeros((60,60,60),dtype=np.int64)
                for w,arr in zip(ww,class_arrays):
                    numerator+=w*arr
                assert np.all(numerator%120==0),(label,slot)
                value=numerator//120
                low,high=int(value.min()),int(value.max())
                assert low>=0,(label,slot,low)
                minima[label][slot]=low;maxima[label][slot]=high
                assert low==target["minima"][label][slot]
                assert high==target["maxima"][label][slot]
                hashes[label].update(value.astype("<i8",copy=False).tobytes(order="C"))
                if (i,j,l)==(0,0,0):
                    zeros[label]=[list(map(int,pos)) for pos in np.argwhere(value==0)]
                    assert zeros[label]==target["zero_triples_in_residue_cube"][label]
                entry_count+=value.size
                identically_zero &= high==0
            if identically_zero:zero_positions.append([i,j,l])
    print("Finished analytic difference order",i,flush=True)
assert entry_count==96768000
expected_zero=[[i,j,l] for i in range(4) for j in range(4) for l in range(4)
               if j+l>3 or (i==3 and j+l==3)]
assert zero_positions==expected_zero==target["identically_zero_difference_positions"]
digests={label:h.hexdigest() for label,h in hashes.items()}
assert digests==target["table_sha256"]
assert sum(map(len,zeros.values()))==115
for label in labels:
    assert all(v>0 for slot,v in minima[label].items()
               if slot!="0,0,0" and list(map(int,slot.split(","))) not in expected_zero)
receipt={
 "statement":"Independent G020 closed-polynomial exhaustive certificate",
 "status":"PASS","method":"Seven rationally verified closed trace formulas; universal difference matrices on polynomial coefficients; no cycle recurrence.",
 "verified_entries":entry_count,"rational_series_checks":7,
 "shifted_common_denominator_checks":14,
 "largest_proved_int64_intermediate_bound":largest_bound,
 "intermediate_bounds_by_order":bounds,
 "identically_zero_difference_positions":zero_positions,
 "strictly_positive_nonconstant_positions":35,
 "zero_triples_in_residue_cube":zeros,
 "minima":minima,"maxima":maxima,"table_sha256":digests,
 "compared_summary_sha256":hashlib.sha256(TARGET.read_bytes()).hexdigest()}
(HERE/"THREE_PARAMETER_ANALYTIC_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","verified_entries":entry_count,
                  "largest_intermediate_bound":largest_bound,
                  "zero_positions":len(zero_positions),
                  "zero_triples":sum(map(len,zeros.values())),
                  "all_seven_hashes_match":True},indent=2))
