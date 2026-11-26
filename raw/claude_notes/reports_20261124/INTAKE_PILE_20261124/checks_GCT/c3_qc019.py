# GCT_OBS QC-019 comparison step: q(s*lam0) >= C(s+155,155) vs K_9(s*lam0) <= C(3b+151,151), lam0=(216,9,9,9), b=9s.
from math import comb
def gap(s): return comb(s+155,155) - comb(27*s+151,151)
s0=67*28**38
print("s0 digits:",len(str(s0)), " gap(s0)>0:",gap(s0)>0)
# threshold: smallest s with gap>0 (monotone eventually); bisection on s
lo,hi=1,s0
assert gap(hi)>0
while hi-lo>1:
    mid=(lo+hi)//2
    if gap(mid)>0: hi=mid
    else: lo=mid
print("smallest s with C(s+155,155) > C(27s+151,151):",hi, "~10^%d"%(len(str(hi))-1), " ratio s0/threshold ~", s0//hi)
# also check K-side: lam0 = (9d-3b,b,b,b) at d=27, b=9: 9*27-27=216
print("lam0 check:",9*27-3*9==216)
