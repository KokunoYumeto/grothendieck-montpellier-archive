"""T067: literal original plethysm comparison in the new lower-a range.

The actual side imports only the existing power-sum/MN implementation.
The expected side calls the supplied positive evaluator; no normal-module
or complementary-hook decomposition is used to compute actual coefficients.
"""
from pathlib import Path
import importlib.util,csv
from verify_rectangular import partitions
from verify_outer4_chambers import actual
HERE=Path(__file__).resolve().parent
source=HERE.parent/'theta'/'unstable_hook'/'all_fixed_order_hook_positive.py'
spec=importlib.util.spec_from_file_location('theta_all_fixed_hook',source)
proposed=importlib.util.module_from_spec(spec);spec.loader.exec_module(proposed)

def main():
    rows=[]
    cases=[(3,4,m,None) for m in (8,9,10)]
    cases +=[(4,6,m,None) for m in (6,7,8)]
    cases +=[(4,5,m,None) for m in (10,11)]
    cases +=[(4,5,13,(3,))]
    for k,a,m,legs in cases:
        for r in (range(m-1) if legs is None else legs):
            if (m-2)*a<m*k+r:continue
            for t in (0,1):
                n=a+t-k
                lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
                assert n>=1 and sum(lam)==m*n and sorted(lam,reverse=True)==list(lam)
                for mu in partitions(m):
                    got=actual(mu,n,lam)
                    expected=proposed.coefficient(m,k,a,r,t,mu)
                    assert got==expected,(m,k,a,r,t,mu,lam,got,expected)
                    rows.append(dict(m=m,k=k,a=a,r=r,t=t,n=n,
                      outer=','.join(map(str,mu)),output=','.join(map(str,lam)),
                      original_cycle_index_MN=got,proposed_positive_evaluator=expected,status='PASS'))
        print('checked lower hook endpoint',m,k,a,'cases',len(rows),flush=True)
    with (HERE/'ALL_FIXED_ORDER_HOOK_ENDPOINT_MN_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    print('PASS T067 lower endpoints',len(rows),flush=True)

if __name__=='__main__':main()
