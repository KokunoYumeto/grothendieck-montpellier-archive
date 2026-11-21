from pathlib import Path
from collections import defaultdict

def plus(a,b):
 c=defaultdict(int,a)
 for e,v in b.items():c[e]+=v
 return {e:v for e,v in c.items() if v}
def times(a,b):
 c=defaultdict(int)
 for e,u in a.items():
  for f,v in b.items():c[e+f]+=u*v
 return {e:v for e,v in c.items() if v}
def scalar(a,c):return {e:c*v for e,v in a.items() if c*v}
def shift(a,k):return {e+k:v for e,v in a.items()}
def symmetric(vec,step=1):
 out={0:vec[0]}
 for j,v in enumerate(vec[1:],1):out[step*j]=out[-step*j]=v
 return {e:v for e,v in out.items() if v}

A={16:5,12:8,10:-4,8:18,6:-4,4:8,0:5}
D=shift(times(A,times({8:1,0:1},{8:1,0:1})),24)
T=symmetric([22,-2,6,2,3,2],2)
N=symmetric([138,-14,70,20,31,26,6,9,3,3,1],2)
assert plus(times(T,T),scalar(shift(D,-40),-1))==scalar(N,4)
F=symmetric([16,16,16,16,17,18,18,18,16,14,12,10,8,6,4,2,1])
# The coefficients of q^11*fhat_p, transcribed directly from VII p28.
raw_fp={0:10,1:8,4:2,-1:12,-6:18,2:6,3:4,5:1,-2:14,-4:18,-12:16,-8:16,-27:1,-11:16,-10:16,-7:17,-24:6,-5:18,-26:2,-3:16,-9:16,-22:10,-20:14,-25:4,-23:8,-21:12,-18:18,-19:16,-16:18,-17:18,-15:17,-14:16,-13:16}
assert F==shift(raw_fp,11)
a=[708,708,694,680,673,666,642,618,565,512,464,416,365,314,262,210,170,130,106,82,62,42,30,18,11,4,2]
b=[2212002,2205476,2186350,2155076,2112378,2058980,1995675,1923256,1842975,1756084,1663849,1567536,1468102,1366504,1263855,1161268,1059834,960644,864459,772040,684050,601152,523831,452572,387494,328716,276117,229576,188839,153652,123592,98236,77108,59732,45640,34364,25488,18596,13346,9396,6493,4384,2894,1848,1142,672,377,196,95,40,15,4,1]
assert times(F,T)==symmetric(a)
assert times(times(F,F),N)==symmetric(b)
for name,vec in [('T1',a),('N1',b)]:
 assert all(x>=y for x,y in zip(vec,vec[1:]+[0]))
 mult=[x-y for x,y in zip(vec,vec[1:]+[0])]
 assert sum(mult[j]*(2*j+1) for j in range(len(mult)))==vec[0]+2*sum(vec[1:])
 print(name,'degree',len(vec)-1,'at1',vec[0]+2*sum(vec[1:]),'nonnegative Lefschetz multiplicities',mult)
print('All exact Laurent identities and monotonicity checks PASS.')
