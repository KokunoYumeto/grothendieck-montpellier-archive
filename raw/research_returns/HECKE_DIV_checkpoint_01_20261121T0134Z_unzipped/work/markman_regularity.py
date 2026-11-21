"""Exact Gotzmann computations for Markman's d=12 genus-three seed.
No inference about Fourier–Mukai transform regularity is made here.
"""
import sympy as s
from pathlib import Path
import json
t=s.Symbol('t')
def binpoly(x,k):return s.prod(x-j for j in range(k))/s.factorial(k)
def gotzmann(P):
    R=s.expand(P);offset=0;blocks=[]
    for d in range(s.degree(P,t),-1,-1):
        num=s.expand(R).coeff(t,d)*s.factorial(d)
        assert num.is_Integer and num>=0,(d,num)
        num=int(num)
        block=s.expand(binpoly(t+d-offset+1,d+1)-binpoly(t+d-offset-num+1,d+1))
        blocks.append({'degree':d,'count':num,'start_index_zero_based':offset})
        R=s.expand(R-block);offset+=num
    assert R==0
    return offset,blocks
Pc=9*t-2
Pz=117*t-26
Pf=27*t**3+27*t**2-108*t-12
cnum,cblocks=gotzmann(Pc)
assert cnum==34
znum,zblocks=gotzmann(Pz)
assert znum==6760
m=znum+1
fnum,fblocks=gotzmann(Pf.subs(t,t+m))
xnum,xblocks=gotzmann(27*t**3)
result={'P_Z':str(Pz),'Gotzmann_Z':znum,'Z_blocks':zblocks,'F_globally_generated_twist_L':m,'P_F':str(Pf),'P_F_shifted':str(s.expand(Pf.subs(t,t+m))),'Gotzmann_F_shifted':fnum,'F_shifted_blocks':fblocks,'safe_regular_bound_i_push_F':fnum+m,'P_X':'27*t**3','Gotzmann_X':xnum,'X_blocks':xblocks,'ambient_P_dimension':26,'degree_X_for_3Theta':162,'number_generators_safe':str(64*s.binomial(6760+26,26)),'scope':'Input ideal and secant sheaf only; no transform regularity or degree D asserted.'}
result.update({'P_C':str(Pc),'Gotzmann_C':cnum,'C_blocks':cblocks,'disjoint_union_regularity_bound':13*cnum,'improved_F_regularity_bound':13*cnum+3,'improved_evaluation_generators':int(Pf.subs(t,13*cnum+3)),'evaluation_kernel_regularity_bound':13*cnum+7,'union_only_F_regularity_bound':znum+3})
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
