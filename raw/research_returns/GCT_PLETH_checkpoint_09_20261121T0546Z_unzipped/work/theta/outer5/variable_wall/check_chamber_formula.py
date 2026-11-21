"""Direct exact restriction/actual-balanced comparisons for T054."""
from pathlib import Path
from itertools import product,islice
import json,sys,hashlib

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'root'))
import zero_twist_arrangement as arrangement
import five_row_cycle_trace as actual
from positive_wall_chamber import (LABELS,CHAR,SIZES,traces,fixed_value,tags,coefficient,constraints,witnesses)


def satisfies(poly,w):
    return (all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],w,poly['upper_bounds']))
            and all(sum(a*z for a,z in zip(row,w))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
            and all(sum(a*z for a,z in zip(row,w))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge'])))


def main():
    restriction=[];balanced=[];continuation=[];witness_checks=0
    for k,X,B in product((3,4,5,6,8,10,12),(0,1,3),(0,1,4)):
        x=X;b=3*k-2+B;parameters=(X,B,k-3)
        if 2*b+x<5*k:continue
        expected=arrangement.traces(x,b,k)
        assert traces(parameters)==expected,(x,b,k,traces(parameters),expected)
        restriction.append((x,b,k,expected))
    for k,X,B,d in product((3,4,5),(0,1,2,3),(0,1),(0,1)):
        x=X;b=3*k-2+B
        if 2*b+x<5*k:continue
        lam=(d+3*b+2*x-5*k,d+b+x,d+b+x,d+x,d)
        values=actual.multiplicities(lam)
        expected=tuple(fixed_value(mu,(X,B,k-3)) for mu in LABELS)
        if (d+b+x)%2:expected=expected[::-1]
        assert values==expected,(lam,values,expected)
        balanced.append((lam,values))
    assert traces((0,0,0))==(0,)*7
    for parameters in ((1,0,0),(0,1,0),(0,0,1),(1,2,3),(59,59,59),(60,0,0),(0,60,0),(0,0,60),
                       (61,62,63),(120,60,0),(0,120,60),(63,121,180),(180,120,240)):
        X,B,K=parameters;k=K+3;x=X;b=3*k-2+B
        for d,mu in product((0,1),LABELS):
            proposed=coefficient(x,b,k,d,mu)
            target=fixed_value(mu,parameters) if (d+b+x)%2==0 else fixed_value(LABELS[6-LABELS.index(mu)],parameters)
            assert proposed==target,(parameters,d,mu,proposed,target)
            continuation.append((parameters,d,mu,proposed))
    for parameters in ((1,0,0),(0,1,0),(0,0,1),(60,0,0),(0,60,0),(0,0,60),(60,60,60)):
        X,B,K=parameters;k=K+3;x=X;b=3*k-2+B
        for mu in LABELS:
            for tag in tags(x,b,k,0,mu):
                poly=constraints(tag)
                assert len(poly['variables'])<=9
                for point in islice(witnesses(tag),2):
                    assert satisfies(poly,point)
                    witness_checks+=1
    receipt={'statement':'T-054','status':'PASS','independent_restriction_class_traces':7*len(restriction),
             'actual_balanced_coefficients':7*len(balanced),'continuation_and_parity_checks':len(continuation),
             'literal_matrix_witnesses':witness_checks,
             'method':'exact G027 rank-two selected-subset engine; independent balanced cycle/Pieri characters; literal Newton continuations and integer matrices',
             'sha256':hashlib.sha256(json.dumps([restriction,balanced,continuation],sort_keys=True).encode()).hexdigest()}
    (HERE/'VARIABLE_WALL_COMPARISON_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
