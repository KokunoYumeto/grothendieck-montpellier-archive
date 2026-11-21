"""Direct actual-character, seed, and literal-polytope checks for T058."""
from pathlib import Path
from itertools import product,islice,combinations
import json,sys,hashlib
from generic_twist_upper_positive import (
    LABELS,coefficient,traces,fixed_value,tags,constraints,witnesses,
)

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'root'))
import fixed_twist_arrangement as arrangement
import five_row_cycle_trace as actual


def physical(Z):
    X,B,K,C=Z
    return X,C+3*K+10+B,C+K+4,C


def shape(x,b,k,c,d=0):
    return (d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d)


def main():
    direct=[];balanced=[];continuation=[];seed=[];witness_count=0
    for X,B,K,C in product((0,2),(0,1),(0,1),(0,1,2,3)):
        Z=(X,B,K,C);x,b,k,c=physical(Z)
        expected=arrangement.traces(x,b,k,c)
        assert traces(Z)==expected,(Z,traces(Z),expected)
        direct.append((Z,expected))
    for X,B,K,C,d in product((0,1),(0,1),(0,1),(0,1,2),(0,1)):
        Z=(X,B,K,C);x,b,k,c=physical(Z);lam=shape(x,b,k,c,d)
        expected=actual.multiplicities(lam)
        proposed=tuple(coefficient(x,b,k,c,d,mu) for mu in LABELS)
        assert proposed==expected,(Z,d,expected,proposed)
        balanced.append((lam,expected))
    for Z in ((0,0,0,0),(1,2,3,4),(59,59,59,59),(60,0,0,0),
              (0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60),
              (61,62,63,64),(120,180,240,60)):
        x,b,k,c=physical(Z)
        for d,mu in product((0,1),LABELS):
            label=LABELS[6-LABELS.index(mu)] if (d+b+x+c)%2 else mu
            v=coefficient(x,b,k,c,d,mu)
            assert v==fixed_value(label,Z),(Z,d,mu,v)
            continuation.append((Z,d,mu,v))
    for X,B,K in ((0,0,0),(0,0,1),(0,1,0),(1,0,0)):
        Z=(X,B,K,2);x,b,k,c=physical(Z);lam=shape(x,b,k,c)
        values=tuple(fixed_value(mu,Z) for mu in LABELS)
        actual_values=actual.multiplicities(lam)
        if (b+x+c)%2:actual_values=actual_values[::-1]
        assert values==actual_values and min(values)>0
        seed.append({'coordinates':Z,'output':lam,'effective_multiplicities':values})
    for Z in ((60,0,0,0),(0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60)):
        x,b,k,c=physical(Z)
        for mu in LABELS:
            for tag in tags(x,b,k,c,0,mu):
                poly=constraints(tag)
                assert len(poly['variables'])<=11
                for point in islice(witnesses(tag),2):
                    assert all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],point,poly['upper_bounds']))
                    assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
                    assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge']))
                    witness_count+=1
    square_seed=0
    for triple in combinations(range(1,6),3):
        pair=tuple(i for i in range(1,6) if i not in triple)
        h=(triple[1]-triple[0])*(triple[2]-triple[0])*(triple[2]-triple[1])*(pair[1]-pair[0])
        square_seed+=12*h*h
    assert square_seed>0
    out={'statement':'T-058','result':'PASS','full_rank3_restriction_traces':7*len(direct),
         'actual_balanced_coefficients':7*len(balanced),'continuation_and_parity':len(continuation),
         'literal_matrix_witnesses':witness_count,'C2_seeds':seed,
         'invariant_square_seed_at_Vandermonde':square_seed,
         'comparison_sha256':hashlib.sha256(repr([direct,balanced,continuation]).encode()).hexdigest(),
         'scope':'actual-module comparisons and four finite seed vectors; no full60^4 residue cube was enumerated'}
    (HERE/'GENERIC_TWIST_UPPER_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
