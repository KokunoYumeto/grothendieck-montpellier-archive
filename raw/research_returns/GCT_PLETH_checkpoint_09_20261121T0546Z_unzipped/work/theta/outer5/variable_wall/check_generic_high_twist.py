"""T059 actual coefficients, finite support seeds and bounded constraints."""
from pathlib import Path
from itertools import product,islice
import json,sys,hashlib
from generic_high_twist_positive import (
    LABELS,coefficient,traces,fixed_value,tags,constraints,witnesses,
)

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'root'))
import fixed_twist_arrangement as arrangement
import five_row_cycle_trace as actual


def physical(Z):
    X,B,K,U=Z
    return X,K+B+1,K+U+1,K+2*U+1


def shape(Z,d=0):
    X,B,K,U=Z
    return (d+2*K+3*B+2*X+3*U+2,d+2*K+B+X+2*U+2,d+K+B+X+1,d+X,d)


def actual_effective(Z):
    values=actual.multiplicities(shape(Z));x,b,k,c=physical(Z)
    return values[::-1] if (b+x+c)%2 else values


def main():
    boundary=[];cube=[];zeros=[];comparisons=0;direct=[];continuation=[];witness_count=0
    for axis in range(4):
        for bits in product((0,1),repeat=4):
            Z=tuple(3+v if i==axis else v for i,v in enumerate(bits))
            values=tuple(fixed_value(mu,Z) for mu in LABELS)
            assert min(values)>0 and values==actual_effective(Z),(Z,values)
            boundary.append({'axis':axis,'coordinates':Z,'effective_multiplicities':values})
            comparisons+=7
    for Z in product(range(3),repeat=4):
        values=tuple(fixed_value(mu,Z) for mu in LABELS)
        assert min(values)>=0 and values==actual_effective(Z),(Z,values)
        cube.append((Z,values));comparisons+=7
        zeros += [{'coordinates':Z,'effective_label':mu} for mu,v in zip(LABELS,values) if not v]
    for Z in product((0,1),repeat=4):
        x,b,k,c=physical(Z)
        expected=arrangement.traces(x,b,k,c)
        assert traces(Z)==expected,(Z,traces(Z),expected)
        direct.append((Z,expected))
    for Z in ((0,0,0,0),(1,2,3,4),(59,59,59,59),(60,0,0,0),
              (0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60),
              (61,62,63,64),(120,180,240,60)):
        x,b,k,c=physical(Z)
        for d,mu in product((0,1),LABELS):
            label=LABELS[6-LABELS.index(mu)] if (d+b+x+c)%2 else mu
            value=coefficient(x,b,k,c,d,mu)
            assert value==fixed_value(label,Z)
            continuation.append((Z,d,mu,value))
    for Z in ((60,0,0,0),(0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60)):
        x,b,k,c=physical(Z)
        for mu in LABELS:
            for tag in tags(x,b,k,c,0,mu):
                poly=constraints(tag);assert len(poly['variables'])<=11
                for point in islice(witnesses(tag),2):
                    assert all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],point,poly['upper_bounds']))
                    assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
                    assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge']))
                    witness_count+=1
    receipt={'statement':'T-059','result':'PASS','boundary_vectors':boundary,
             'cube_vectors':cube,'zeros':zeros,'zero_count':len(zeros),
             'actual_balanced_coefficients':comparisons,'full_rank3_restriction_traces':7*len(direct),
             'continuation_and_parity':len(continuation),'literal_matrix_witnesses':witness_count,
             'support_sha256':hashlib.sha256(repr([boundary,cube]).encode()).hexdigest(),
             'method':'actual balanced-cycle comparison of all64 boundary parity seeds and all81 small cube vectors; no60^4 cube enumeration'}
    (HERE/'GENERIC_HIGH_TWIST_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({key:value for key,value in receipt.items() if key not in ('boundary_vectors','cube_vectors')},indent=2))


if __name__=='__main__':main()
