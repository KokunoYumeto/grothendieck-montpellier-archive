"""B88 exact exhaustive point-field profile and character-filtration certificate."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from collections import Counter
import json,time

started=time.perf_counter();counts=Counter();p=5;N=24
records=[]
# E1: the off-last case forces a larger quotient break6<d1>=24.
assert 6<N
records.append({'field':'E1','last':'off','excluded':'larger off break6 is below every positive diagonal break'})
counts['excluded_initial_last_line_cases']+=1
E1_survivors=[]
for t in range(6,72,24):
    u=5*72-4*t
    forced_J=15+4*t
    if forced_J%5==0:
        reason='Required first prime exponent is divisible by5'
        assert t==30 and forced_J==135
    elif 95+5*t>125:
        first_J=125-t
        assert first_J<95 and t==54
        reason='Required first exponent71 precedes leading exponent95'
    else:
        reason='Not excluded by these necessary conditions'
        E1_survivors.append((t,u))
    records.append({'field':'E1','last':'diagonal','t':t,'u':u,'forced_prime_degree':forced_J,'reason':reason})
    counts['E1_finite_tame_residue_cases']+=1
assert E1_survivors==[(6,336)]

# E2: diagonal-last would have lower breaks18,48.
t,u=18,48
assert 45+5*t==135<375
forced_J=45+4*t
predicted=min(45+5*u,forced_J+u)
assert forced_J==117 and predicted==165<1125 and 117+48<45+5*48
records.append({'field':'E2','last':'diagonal','t':t,'u':u,
                'forced_prime_degree':forced_J,'predicted_last_displacement':predicted,
                'required_last_displacement':1125,'excluded':True})
counts['excluded_initial_last_line_cases']+=1
E2_survivors=[]
for t in range(24,66,24):
    u=5*66-4*t
    if 5+5*t>125:
        first_J=125-t
        assert first_J>5 and first_J%5
        predicted=min(5+5*u,first_J+u)
        assert predicted==215<2375 and first_J+u<5+5*u
        reason='Unique later prime change has degree215 rather than2375'
    else:
        E2_survivors.append((t,u))
        reason='Not excluded by these necessary conditions'
    records.append({'field':'E2','last':'off','t':t,'u':u,'reason':reason})
    counts['E2_finite_tame_residue_cases']+=1
assert E2_survivors==[(24,234)]

upper=(6,24,66,72)
lower=[upper[0]]
for j in range(1,4):lower.append(lower[-1]+p**j*(upper[j]-upper[j-1]))
assert lower==[6,96,1146,1896]
counts['exact_upper_to_lower_intervals']=4
projective={}
for vector in product(range(p),repeat=4):
    if not any(vector):continue
    first=next(a for a in vector if a)
    inverse=pow(first,-1,p)
    normalized=tuple(a*inverse%p for a in vector)
    jump=max(j for j,a in zip(upper,vector) if a)
    projective[normalized]=jump
    counts['literal_nonzero_coordinate_characters']+=1
hist=Counter(projective.values())
assert hist=={6:1,24:5,66:25,72:125}
assert len(projective)==156
counts['cyclic_degree_five_subfields']=len(projective)
trace=(0,1,0,1) # order A21,A22,A12,A11
assert projective[trace]==72 and 72//N==3 and 72%N==0
counts['actual_trace_and_tame_scaling_rows']=1

# Independent arithmetic consistency: lower-filtration different equals the
# sum of the conductors of every nonzero character.
different=(p**4-1)*(lower[0]+1)
for j in range(1,4):different+=(p**(4-j)-1)*(lower[j]-lower[j-1])
conductor_sum=sum((p-1)*number*(jump+1) for jump,number in hist.items())
assert different==conductor_sum==43728
counts['different_conductor_consistency_checks']=1
for t,u in E1_survivors+E2_survivors:
    assert (u+4*t)%5==0 and t>0 and u>t
    counts['actual_point_field_quotient_averages']+=1

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-started,'counts':dict(counts),
     'point_field_cases':records,'point_field_lower_breaks':{'E1':E1_survivors[0],'E2':E2_survivors[0]},
     'upper_coordinate_order':['A21','A22','A12','A11'],'upper_breaks':upper,'lower_breaks':lower,
     'cyclic_subfield_break_counts':dict(sorted(hist.items())),
     'different_consistency':different,'cyclotomic_break_over_L':72,'cyclotomic_break_over_K':3,
     'scope':'All candidates here arise from proved finite tame-residue lists; no unbounded break search. '
             'All625 coordinate characters are checked except zero, modulo their nonzero scalars. '
             'This certifies a necessary actual full-image profile, not its realization or impossibility; '
             'in particular the cyclotomic break3 over the allowed K is not excluded.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
