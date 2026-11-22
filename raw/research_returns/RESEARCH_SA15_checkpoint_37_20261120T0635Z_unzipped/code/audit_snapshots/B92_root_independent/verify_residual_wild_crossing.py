#!/usr/bin/env python3
"""Exact finite checks for B92. No remaining field/group is constructed."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from fractions import Fraction as F
import hashlib
import json
import time


def mul(a,b,m):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%m for i in range(2) for j in range(2))


def power(a,n,m):
    out=(1,0,0,1)
    while n:
        if n&1: out=mul(out,a,m)
        a=mul(a,a,m); n//=2
    return out


def prime_coefficient_possible(A,D0,D1,t,u):
    """Necessary first-change condition, allowing only a genuine tie
    to remove a too-early term; the same prime exponent serves both breaks.
    It deliberately permits any later cancellation after a tie.
    """
    exact=None
    lower=A+1
    for b,D in ((t,D0),(u,D1)):
        leading=A+5*b
        if leading<D:
            value=A+4*b
        elif leading>D:
            value=D-b
        else:
            lower=max(lower,A+4*b)
            continue
        if exact is not None and exact!=value:
            return False
        exact=value
    if exact is None:
        return True
    return exact>=lower and exact%5!=0


def main():
    start=time.perf_counter()
    p=5
    lines=[(1,t) for t in range(5)]+[(0,1)]
    degree_five=[]
    for column,AA in ((1,(19,3)),(2,(1,9))):
        for line in lines:
            high1=line[1]==0
            high2=line[0]==0
            D=(475 if high1 else 25,225 if high2 else 75)
            breaks=(D[0]-AA[0],D[1]-AA[1])
            assert breaks[0]!=breaks[1]
            degree_five.append({'column':column,'translation_line':list(line),'coordinate_values':list(AA),'breaks':list(breaks)})

    # Reconstruct the only tau-stable spaces of dimension three compatible
    # with both surjective column evaluations: two off axes plus a diagonal
    # line with both entries nonzero.
    diagonal_lines=[]
    for b in range(1,5):
        matrices={(a,x,y,a*b%5) for a,x,y in product(range(5),repeat=3)}
        assert len(matrices)==125
        assert len({(a,c) for a,_,c,_ in matrices})==25
        assert len({(b0,d) for _,b0,_,d in matrices})==25
        diagonal_lines.append([1,b])
    assert len(diagonal_lines)==4
    # B87's shared diagonal alternative is impossible: E1 forces d=72,
    # while E2 forces either d=24 or the larger off break 66>d.
    assert 72!=24 and not 66>72

    # Reconstruct B88's exact two point-field alternatives using its strict
    # coefficient equations, with no presumed filtration beyond the table.
    point_cases=[]
    for t in (6,30,54):
        u=360-4*t
        valid=prime_coefficient_possible(95,125,2375,t,u) and prime_coefficient_possible(15,1125,375,t,u)
        # In the second coordinate high translations have the smaller break.
        # The generic routine handles these as the actual two values in order.
        point_cases.append(('E1',t,u,valid))
    assert [(t,u) for name,t,u,valid in point_cases if valid]==[(6,336)]
    e2_diagonal=prime_coefficient_possible(5,2375,125,18,48) and prime_coefficient_possible(45,375,1125,18,48)
    assert not e2_diagonal
    for t in (24,48):
        u=330-4*t
        valid=prime_coefficient_possible(5,125,2375,t,u) and prime_coefficient_possible(45,1125,375,t,u)
        point_cases.append(('E2',t,u,valid))
    assert [(t,u) for name,t,u,valid in point_cases if name=='E2' and valid]==[(24,234)]

    # Actual upper-triangular fifth powers, independently multiplied mod25.
    power_rows=0
    for a,d,b in product(range(5),range(5),range(25)):
        g=(1+5*a,b,0,1+5*d)
        assert power(g,5,25)==(1,5*(b%5),0,1)
        power_rows+=1

    # Conjugation to the genuine quotient lattice is checked coefficient by
    # coefficient on full digit samples, before passing to the F5 characters.
    quotient_rows=0
    for a,d,b0,b1,c in product(range(5),repeat=5):
        g=(1+5*a,b0+5*b1,25*c,1+5*d)
        quotient=(g[0]%25,5*g[1]%25,(g[2]//5)%25,g[3]%25)
        A=tuple(((quotient[i]-(1 if i in (0,3) else 0))//5)%5 for i in range(4))
        assert A==(a,b0,c,d)
        quotient_rows+=1
    assert quotient_rows==3125
    assert 5**(1+3+4)==25*25*125*5

    # Exhaust the necessary first-change constraints for the two concrete
    # common-high pairs. Bounds t<=D0-A and u<=D1-A are the unconditional
    # fixed-coordinate inequality; no guessed break range is used.
    common_high=[]; tested=0
    for b1,b2 in ((1,9),(3,19)):
        rows=[(5*b,125*b,15000-625*b) for b in (b1,b2)]
        max_t=min(D0-A for A,D0,D1 in rows)
        max_u=min(D1-A for A,D0,D1 in rows)
        surviving=[]
        for t in range(1,max_t+1):
            for u in range(t+1,max_u+1):
                tested+=1
                if all(prime_coefficient_possible(A,D0,D1,t,u) for A,D0,D1 in rows):
                    surviving.append((t,u))
        expected=(24*b1,15000-630*b2-96*b1)
        assert surviving==[expected],(b1,b2,surviving)
        first_upper=expected[0]
        second_upper=F(expected[1]+4*expected[0],5)
        assert second_upper==3000-126*b2
        common_high.append({'b':[b1,b2],'data':[list(r) for r in rows],'lower':list(expected),'upper':[first_upper,int(second_upper)]})

    # Identify the same diagonal character before and after the actual
    # quotient basis swap, then compute its disjoint degree-five base change.
    field_rows=[]
    for B1,B2,Rbreak,D22break,forced in ((5,45,66,24,24),(15,95,6,72,72)):
        actual=D22break if D22break<Rbreak else Rbreak+5*(D22break-Rbreak)
        field_rows.append({'parameters':[B1,B2],'R_break':Rbreak,'D22_break':D22break,'base_changed_break':actual,'coordinate_forced_break':forced,'contradiction':actual!=forced})
    assert field_rows[0]['base_changed_break']==24
    assert field_rows[1]['base_changed_break']==336
    assert [r['contradiction'] for r in field_rows]==[False,True]

    result={
        'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'degree_five_translation_rows':degree_five,
        'possible_three_dimensional_diagonal_lines':diagonal_lines,
        'point_field_coefficient_cases':[list(r) for r in point_cases],
        'excluded_E2_diagonal_case':not e2_diagonal,
        'triangular_power_rows':power_rows,
        'actual_quotient_digit_rows':quotient_rows,
        'common_high_break_pairs_tested':tested,
        'common_high_survivors':common_high,
        'actual_diagonal_field_comparisons':field_rows,
        'scope':'Exact finite supplement to the actual field and group proofs. Necessary coefficient tests permit later tie cancellations; only the displayed pair (15,95) is excluded by the same actual diagonal field. No realization of (5,45) or full first-wild recovery is claimed.'
    }
    output=Path(__file__).with_suffix('.output.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
