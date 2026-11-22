"""Complete necessary mass relaxation for NN-G035.

All finite loop bounds are proved in the chapter. The script does not claim
that surviving mass data admit coefficientwise positive associative tables.
"""
from math import gcd,lcm
from pathlib import Path
import json

CAP=9912
def delta_values(g,h,w):
    out=[]
    for d in range(4,g//4+1,2):
        a=w*(g-4*d)
        if a%h==0 and a//h>=4 and (a//h)%2==0:
            out.append((d,a//h))
    return out

def least_aux(g,h,w,lower,divisor):
    modulus=lcm(divisor,2*h//gcd(w,2*h))
    a=lower+(4*g-lower)%modulus
    numerator=w*(4*g-a)
    assert numerator%h==0
    v=numerator//h
    assert v%2==0 and a%divisor==0
    if v<16:return None
    step_v=w*modulus//h
    assert step_v%2==0
    step_T=14*modulus-20*step_v
    assert step_T>0
    return a,v,modulus,step_v,step_T

coarse=0;all_bases=[]
for w in range(8,19,2):
    for g1 in range(48,269,4):
        for g2 in range(48,317-g1,4):
            if g1*g2%w:continue
            s=g1*g2//w
            if s<576 or s%4:continue
            low=s+20*(g1+g2)+200*w+800+208+336
            if low>CAP:continue
            coarse+=1
            aux1=least_aux(g1,g2,w,8,2)
            aux2=least_aux(g2,g1,w,16,4)
            if aux1 is None or aux2 is None:continue
            a1,v1,m1,dv1,dt1=aux1
            a2,v2,m2,dv2,dt2=aux2
            for d1,u1 in delta_values(g1,g2,w):
                for d2,u2 in delta_values(g2,g1,w):
                    if w in (8,10):
                        if u1==4 and (g2%(4*w) or (g2//(4*w))%2!=1):continue
                        if u2==4 and g1%(8*w):continue
                    T=s+20*(g1+g2)+200*w+20*(u1+u2+v1+v2)+26*(d1+d2)+14*(a1+a2)
                    if T>CAP:continue
                    all_bases.append(dict(w=w,g1=g1,g2=g2,s=s,d1=d1,d2=d2,
                        u1=u1,u2=u2,a1_min=a1,a2_min=a2,v1_max=v1,v2_max=v2,
                        modulus1=m1,modulus2=m2,v_step1=dv1,v_step2=dv2,
                        mass_step1=dt1,mass_step2=dt2,T_min=T,score_min=(T-4424)//2))
all_bases.sort(key=lambda r:(r['T_min'],r['w'],r['g1'],r['g2'],r['d1'],r['d2']))
assert coarse==1445 and len(all_bases)==55
excluded=[r for r in all_bases if r['s']==576]
bases=[r for r in all_bases if r['s']!=576]
assert len(excluded)==12 and len(bases)==43

count=0;incumbent_found=False
for r in bases:
    increments=[]
    k1max=min((r['v1_max']-16)//r['v_step1'],(CAP-r['T_min'])//r['mass_step1'])
    for k1 in range(k1max+1):
        left=CAP-r['T_min']-r['mass_step1']*k1
        k2max=min((r['v2_max']-16)//r['v_step2'],left//r['mass_step2'])
        for k2 in range(k2max+1):
            increments.append([k1,k2])
            a1=r['a1_min']+r['modulus1']*k1
            a2=r['a2_min']+r['modulus2']*k2
            if (r['w'],r['g1'],r['g2'],r['d1'],r['d2'],a1,a2)==(8,64,96,4,8,16,192):
                incumbent_found=True
    r['allowed_auxiliary_increment_pairs']=increments
    count+=len(increments)
first=sorted({(r['g1'],r['d1'],r['u1']) for r in bases})
expected=[(64,4,4),(72,4,6),(72,6,4),(76,4,6),
          (80,4,8),(80,8,4),(80,8,6),(80,12,4),
          (84,6,6),(84,10,6),(84,14,4),(88,8,8),
          (96,4,10),(96,4,12),(96,6,6),(96,12,4),(96,14,6),
          (100,4,10),(100,6,10),(100,10,6),(128,12,8)]
assert first==expected and incumbent_found
assert min(r['score_min'] for r in bases)==1700
assert min(r['s'] for r in bases)==588
assert sorted({r['w'] for r in bases})==[8,10,12]
out={'cap_nonunit_mass':CAP,'coarse_tuples':coarse,'base_rows_before_bottom_exclusion':55,
     'excluded_minimal_bottom_rows':excluded,'remaining_base_rows':43,
     'full_scalar_increment_choices':count,'first_cell_mass_triples':first,
     'necessary_closed_table_score_lower_bound':1700,'least_remaining_bottom_mass':588,
     'bases':bases,'scope':'Complete necessary scalar relaxation for closed tables only. Surviving data are not asserted realizable; arbitrary Laurent support remains a separate gate.'}
Path('work/gct/closed_mass_gate_2744_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['bases','excluded_minimal_bottom_rows']},indent=2))
