"""Exact finite supplement to B93; no formal-group realization is inferred."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import time

started=time.perf_counter()

def encode(value):
    if isinstance(value,Q):
        return int(value) if value.denominator==1 else f'{value.numerator}/{value.denominator}'
    if isinstance(value,dict): return {k:encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [encode(v) for v in value]
    return value

def upper_from_lower(lower, initial_order, drop_factors):
    assert len(lower)==len(drop_factors)
    previous=Q(0); result=[]; value=Q(0); order=initial_order
    for stop,factor in zip(lower,drop_factors):
        value+=(Q(stop)-previous)*Q(order,initial_order)
        result.append(value); previous=Q(stop); order//=factor
    assert order==1
    return result

def psi(upper, factors, value):
    value=Q(value); previous=Q(0); result=Q(0); index=1
    for stop,factor in zip(upper,factors):
        stop=Q(stop)
        if value<=stop: return result+(value-previous)*index
        result+=(stop-previous)*index
        previous=stop; index*=factor
    return result+(value-previous)*index

# Normal-closure arithmetic, without asserting existence of any row.
cyclotomic_rows=[]
for m in (1,2,4):
    for bt in range(1,5*m+1):
        d=4+Q(4*bt,m)
        assert d.denominator==1 and d<=24
        ut=Q(bt,m)
        via_t=m*ut+5*m*(8-ut)
        target=44-d
        assert via_t==m*target and target>=20
        cyclotomic_rows.append({'m':m,'lower_break':bt,'different':d,'normal_closure_upper':ut,'last_upper_over_K':target})
assert upper_from_lower([4,24],25,[5,5])==[4,8]

# Derive the unique outer-coset maximum from the exact quotient average.
def coset_average(M):
    return Q(100*min(24,M)+20*min(384,M)+4*min(44634,M)+M,125)
assert coset_average(234)==66
assert coset_average(233)<66<coset_average(235)
f2_counts=Counter({24:100,384:20,44634:4})
for _ in range(4): f2_counts.update({24:100,234:25})
assert f2_counts==Counter({24:500,234:100,384:20,44634:4})
f2_lower=sorted(f2_counts)
f2_upper=upper_from_lower(f2_lower,625,[5]*4)
assert f2_upper==[24,66,72,426]
e_upper=[6]+f2_upper
e_lower=[psi(e_upper,[5]*5,u) for u in e_upper]
assert e_lower==[6,96,1146,1896,223146]

# Enumerate the actual full parahoric matrices and their actual point images.
images={name:set() for name in ['F2','FQ','E','R','S','high25','high125','high125_R','low25','low125']}
stabilizers=Counter()
e_elements=set(); e_over_s=set(); e_over_low=set(); terminal=set()
matrix_rows=0
for a in range(25):
    for d in range(25):
        for b in range(125):
            for c in range(5):
                matrix_rows+=1
                a0=a%5; d0=d%5; u=b%5; b25=b%25
                e_tuple=(a0,d0,b25,c)
                images['F2'].add((a0,d0,b25))
                images['FQ'].add((a0,d0,u,c))
                images['E'].add(e_tuple)
                images['R'].add(u)
                images['S'].add((u,a0))
                images['high25'].add((1+5*a0)%25)
                images['high125'].add(((1+5*a)%125,25*c))
                images['high125_R'].add(((1+5*a)%125,25*c,u))
                images['low25'].add((b25,(1+5*d0)%25))
                images['low125'].add((b,(1+5*d)%125))
                e_elements.add(e_tuple)
                if u==a0==0: e_over_s.add(e_tuple)
                if b25==d0==0: e_over_low.add(e_tuple)
                in_u=(a0==d0==b25==c==0)
                high_stab=(a==c==0)
                high_r_stab=(high_stab and u==0)
                low_stab=(b==d==0)
                low25_stab=(b25==d0==0)
                if in_u:
                    terminal.add((a//5,b//25,d//5))
                    stabilizers['U']+=1
                for name,condition in [('high125',high_stab),('high125_R',high_r_stab),('low125',low_stab),('low25',low25_stab),('U_intersect_high_R',in_u and high_r_stab),('U_intersect_low125',in_u and low_stab)]:
                    if condition: stabilizers[name]+=1
assert matrix_rows==5**8
expected_images={'F2':625,'FQ':625,'E':3125,'R':5,'S':25,'high25':5,'high125':125,'high125_R':625,'low25':125,'low125':3125}
assert {k:len(v) for k,v in images.items()}==expected_images
assert len(terminal)==125 and len(e_over_s)==125 and len(e_over_low)==25
assert stabilizers['U_intersect_high_R']==25
assert stabilizers['U_intersect_low125']==5
high_composite_degree=Q(matrix_rows,stabilizers['U_intersect_high_R'])
low_composite_degree=Q(matrix_rows,stabilizers['U_intersect_low125'])
assert Q(3125*625,high_composite_degree)==125  # T_h intersection E = SC.
assert Q(3125*3125,low_composite_degree)==125  # E_low^+ intersection E = E_low.

# Filtration in the actual E quotient, determined by its four actual
# coordinate characters and its central upper-entry character.
def e_break(t):
    a0,d0,b25,c=t
    if c: return 6
    if d0: return 96
    if b25%5: return 1146
    if a0: return 1896
    if b25: return 223146
    return None

e_counts=Counter(e_break(t) for t in e_elements if e_break(t) is not None)
assert e_counts==Counter({6:2500,96:500,1146:100,1896:20,223146:4})
s_counts=Counter(e_break(t) for t in e_over_s if e_break(t) is not None)
low_counts=Counter(e_break(t) for t in e_over_low if e_break(t) is not None)
assert s_counts==Counter({6:100,96:20,223146:4})
assert low_counts==Counter({6:20,1896:4})
e_s_upper=upper_from_lower(sorted(s_counts),125,[5]*3)
e_low_upper=upper_from_lower(sorted(low_counts),25,[5]*2)
assert e_s_upper==[6,24,8946] and e_low_upper==[6,384]

# Actual coordinate normalizations and unconditional break bounds.
high_inverse_values=[Q(19,25),Q(3,25)]
assert [v*625 for v in high_inverse_values]==[475,75]
high_last_lower_bound=625*75-75
assert high_last_lower_bound==46800
high_character_upper=6+Q(high_last_lower_bound-6,5)
assert high_character_upper==Q(46824,5)
low_coordinate=Q(1,625)*3125
low_character_upper=3125-low_coordinate
assert low_coordinate==5 and low_character_upper==3120
terminal_a_bound=psi(e_s_upper,[5]*3,high_character_upper)
terminal_d_bound=psi(e_low_upper,[5]*2,low_character_upper)
cyclotomic_lower=psi(e_upper,[5]*5,480)
assert terminal_a_bound==275496
assert terminal_d_bound==70296
assert cyclotomic_lower==391896
assert max(terminal_a_bound,terminal_d_bound)<cyclotomic_lower

# The determinant is the same actual terminal trace character.
determinant_rows=0
for a1,b2,d1 in terminal:
    determinant=((1+25*a1)*(1+25*d1))%125
    assert determinant==(1+25*(a1+d1))%125
    determinant_rows+=1

out={
    'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
    'runtime_seconds':time.perf_counter()-started,
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'normal_closure_arithmetic_rows':cyclotomic_rows,
    'matrix_rows':matrix_rows,'point_image_sizes':expected_images,
    'stabilizer_sizes':dict(stabilizers),
    'F2_lower_counts':dict(sorted(f2_counts.items())),
    'F2_upper':f2_upper,'E_lower_counts':dict(sorted(e_counts.items())),
    'E_upper':e_upper,'E_over_S_lower_counts':dict(sorted(s_counts.items())),
    'E_over_S_upper':e_s_upper,
    'E_over_low25_lower_counts':dict(sorted(low_counts.items())),
    'E_over_low25_upper':e_low_upper,
    'high_point_character_upper_bound':high_character_upper,
    'low_point_character_upper_bound':low_character_upper,
    'terminal_a_bound':terminal_a_bound,'terminal_d_bound':terminal_d_bound,
    'cyclotomic_terminal_lower_bound':cyclotomic_lower,
    'strict_gap':cyclotomic_lower-max(terminal_a_bound,terminal_d_bound),
    'terminal_determinant_rows':determinant_rows,
    'scope':'Exact supplement to the actual field/stabilizer/Herbrand proofs. No existence from a numerical row; only the crossing(5,45) is addressed. The normal-closure, different bound, character persistence, and coordinate inequality are proved in the text rather than inferred from the finite run.'
}
dest=Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(encode(out),indent=2)+'\n')
print(json.dumps(encode(out),indent=2))
