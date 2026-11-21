"""Complete fixed residue and direct character checks of T056."""
from pathlib import Path
from itertools import product,islice
import json,hashlib,sys
from one_twist_strip import value,traces,coefficient,tags,constraints,witnesses,LABELS

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[2]/'root'))
import fixed_twist_arrangement as arrangement
import five_row_cycle_trace as actual


def main():
    records=[];digest=hashlib.sha256()
    for mu in LABELS:
        vals=[];zeros=[]
        for X,K in product(range(60),repeat=2):
            v=value(mu,(X,0,K))
            assert v>=0
            vals.append(v)
            if not v:zeros.append((X,K))
        digest.update((repr((mu,vals))+'\n').encode())
        records.append({'label':mu,'minimum':min(vals),'maximum':max(vals),'zeros':zeros,
                        'origin_value':vals[0]})
    restriction=0;balanced=0;continuation=0;matrix_witnesses=0
    for k,x in product((5,6,7),(0,1,3)):
        b=3*k-4
        assert traces((x,0,k-5))==arrangement.traces(x,b,k,1)
        restriction+=7
    for k,x,d in product((5,6),(0,1,2),(0,1)):
        b=3*k-4
        lam=(d+3*b+2*x+4-5*k,d+b+x+1,d+b+x,d+x,d)
        expected=actual.multiplicities(lam)
        proposed=tuple(coefficient(x,k,d,mu) for mu in LABELS)
        assert expected==proposed,(lam,expected,proposed)
        balanced+=7
    for X,K,d,mu in product((0,1,60,121),(0,1,60,121),(0,1),LABELS):
        k=K+5;b=3*k-4
        label=LABELS[6-LABELS.index(mu)] if (d+b+X+1)%2 else mu
        assert coefficient(X,k,d,mu)==value(label,(X,0,K))
        continuation+=1
    for X,K,mu in product((0,60),(0,60),LABELS):
        for tag in tags(X,K+5,0,mu):
            poly=constraints(tag)
            assert len(poly['variables'])<=9
            for point in islice(witnesses(tag),2):
                assert all(lo<=z<=hi for lo,z,hi in zip(poly['lower_bounds'],point,poly['upper_bounds']))
                assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(poly['A_eq'],poly['b_eq']))
                assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(poly['A_ge'],poly['b_ge']))
                matrix_witnesses+=1
    out={'statement':'T-056','result':'PASS','residue_constants':7*60**2,
         'labels':records,'residue_sha256':digest.hexdigest(),
         'restriction_class_traces':restriction,'actual_balanced_coefficients':balanced,
         'continuation_parity_cases':continuation,'literal_matrix_witnesses':matrix_witnesses,
         'method':'unbounded rational/integer arithmetic for residues; full rank3 arrangement and balanced-cycle comparisons'}
    (HERE/'ONE_TWIST_STRIP_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
