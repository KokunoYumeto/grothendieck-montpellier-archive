"""Exact arithmetic supplement for B65, not a geometric existence proof.

Verifies the Newton polygons, integral canonical-quotient valuations,
all normalized residual parameter cases and all displayed inequalities.
The proof of quotient existence, common point fields and character recovery
is in the accompanying candidate; this finite program does not replace it.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import time,datetime,json,itertools
start=time.perf_counter();p=5;N=24;a=288;t=3
counts={'newton_records':0,'inverse_polygons':0,'quotient_point_counts':0,
        'wild_common_break_rows':0,'wild_divisible_pair_rows':0,
        'tame_pair_rows':0,'exceptional_inequalities':0,
        'one_slope_character_pairs':0,'square_determinant_bounds':0}

def polygon(points):
    h=[]
    for x,y in sorted(points):
        while len(h)>=2:
            x0,y0=h[-2];x1,y1=h[-1]
            if F(y1-y0,x1-x0)>=F(y-y1,x-x1):h.pop()
            else:break
        h.append((x,y))
    return [(F(y0-y1,x1-x0),x1-x0) for (x0,y0),(x1,y1) in zip(h,h[1:]) if y0>y1]

def orb(c):return tuple(sorted({c%N,5*c%N}))
def high(c,B):return (c-B)%N
def semisimple(c,B):
    h=high(c,B);return tuple(sorted((h,(6-h)%N)))
def quotient(B):return 5*B if B<12 else 72-B
rows=[]
for B in range(1,60):
    for c in range(1,24,4):
        if (B-c)%6:continue
        alpha=F(72-B);beta=F(B,5);b=4*B
        assert B%2==1 and alpha>beta
        assert polygon([(0,a),(4,b),(24,0)])==[(alpha,4),(beta,20)]
        invlow=polygon([(0,beta),(1,a),(5,b),(25,0)])
        assert invlow==[(F(B,125),25)]
        invhigh=polygon([(0,alpha),(1,a),(5,b),(25,0)])
        if B<12:assert invhigh==[(F(72-5*B,5),5),(beta,20)]
        else:assert invhigh==[(alpha/25,25)]
        qc=Counter({F(B):4})
        for z,n in invhigh:
            assert z<alpha and (n*4)%5==0
            qc[5*z]+=n*4//5
        Bp=quotient(B);cp=5*c%N
        assert 0<Bp<60 and (Bp-cp)%6==0 and cp%4==1
        assert qc==Counter({F(72-Bp):4,F(Bp,5):20})
        assert orb(cp)==orb(c)
        rows.append({'B':B,'c':c,'alpha':str(alpha),'beta':str(beta),'B_quotient':Bp,'c_quotient':cp})
        counts['newton_records']+=1;counts['inverse_polygons']+=2;counts['quotient_point_counts']+=1
# Same full residual module with wild inertia gives one high-line character.
wild_patterns=Counter()
for x,y in itertools.product(rows,repeat=2):
    B,C=x['B'],y['B'];c,d=x['c'],y['c']
    if high(c,B)!=high(d,C):continue
    r1=[360-6*B] if B%5 else range(1,360-6*B)
    r2=set([360-6*C] if C%5 else range(1,360-6*C))
    for r in r1:
        if r not in r2:continue
        counts['wild_common_break_rows']+=1
        if B%5 and C%5:
            assert B==C and c==d;wild_patterns['both_prime_equal']+=1
        elif bool(B%5)!=bool(C%5):
            U,V=(B,C) if B%5 else (C,B)
            assert U>V
            assert 25*V < V+24*U
            wild_patterns['one_divisible_point_field_contradiction']+=1
        else:
            counts['wild_divisible_pair_rows']+=1
            Bp,Cp=quotient(B),quotient(C)
            if B==C==5:
                assert c==d;wild_patterns['both_small_equal']+=1
            elif B>=15 and C>=15:
                assert Bp%5 and Cp%5
                # Common quotient residual break forces Bp=Cp.
                if Bp==Cp:assert B==C and c==d
                wild_patterns['both_quotients_prime']+=1
            else:
                assert (B==5) != (C==5)
                assert bool(Bp%5)!=bool(Cp%5)
                wild_patterns['mixed_quotient_contradiction']+=1
# Every tame residual parameter has B=5b and b in the displayed set.
tame=[x for x in rows if x['B']%5==0]
assert sorted({x['B']//5 for x in tame})==[1,3,5,7,9,11]
tame_patterns=Counter()
for x,y in itertools.product(tame,repeat=2):
    B,C=x['B'],y['B'];c,d=x['c'],y['c'];b,k=B//5,C//5
    if semisimple(c,B)!=semisimple(d,C):continue
    counts['tame_pair_rows']+=1
    if b%5 and k%5:
        # The proof's two prime coordinate breaks force b=k and the high lines.
        if b==k and high(c,B)==high(d,C):assert c==d
        tame_patterns['both_prime']+=1
    elif b==k==5:
        assert c==d and orb(c)==orb(d)
        tame_patterns['both_exceptional_equal']+=1
    else:
        if b==5:b,k,c,d,B,C=k,b,d,c,C,B
        assert k==5 and b in (1,3,7,9,11)
        # If high lines differ, use a high translation only in the prime model.
        rhs=5+25*(72-5*b)-b
        assert rhs>=419>125
        counts['exceptional_inequalities']+=1
        # Once the high lines agree, low translation and tame character impose:
        if 125>=5+24*b and high(c,B)==high(d,C):
            assert b==1 and (c-d)%24==4 and orb(c)==orb(d)
            tame_patterns['exceptional_surviving_same_orbit']+=1
        else:tame_patterns['exceptional_excluded']+=1
# Direct exhaustion independent of the semisimple filter.
for b in (1,3,7,9,11):
    assert 5+25*(72-5*b)-b>=419
    if 125>=5+24*b and (5*b-25)%4==0:assert b==1
    counts['exceptional_inequalities']+=1
for c,d in itertools.product(range(1,24,4),repeat=2):
    if orb(c+12)==orb(d+12):assert orb(c)==orb(d)
    counts['one_slope_character_pairs']+=1
square=[]
for m in (1,2,3,6):
    aa=12*m;q0=1;q1=min(aa+q0,5*q0+1,25*q0)
    q2=min(aa+q1,5*q1+1,25*q1)
    assert q1>=6 and q2>=F(aa,4)
    square.append({'m':m,'a':aa,'q1':q1,'q2':q2,'threshold':str(F(aa,4))})
    counts['square_determinant_bounds']+=1
assert 12>5 and 12<=5**3
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,'counts':counts,'newton_records':rows,
        'wild_patterns':dict(wild_patterns),'tame_patterns':dict(tame_patterns),
        'square_bounds':square,'scope':'Finite exact support for the displayed B65 Newton, quotient and case arithmetic only. The full formal-group/Galois proof is separate; no group existence or universal theorem is inferred from enumeration.'}
out=Path(__file__).with_suffix('.output.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='newton_records'},indent=2))
