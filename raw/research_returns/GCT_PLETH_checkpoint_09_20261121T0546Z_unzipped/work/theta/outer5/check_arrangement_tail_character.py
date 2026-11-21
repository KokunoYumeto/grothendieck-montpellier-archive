"""Independent T049 tail-product comparison against cycle-index/MN."""
from pathlib import Path
import sys
import csv
import json
import hashlib
from itertools import product

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import partitions
from verify_outer4_chambers import actual
from arrangement_tail_character import (CLASSES,LABELS,CHAR,SIZES,multiplicities,
    balanced_traces,table_polynomial,table_polytope,trace_alpha)


def literal_table(cycles,k,beta):
    """Recursively enumerate the actual DP.11 integer arrays."""
    if min(beta)<0:return 0
    if not cycles:return int(beta==(0,0,0))
    c=cycles[0];ans=0
    for row in product(*(range(b//c+1) for b in beta)):
        if sum(row)<k:continue
        rest=tuple(beta[a]-c*row[a] for a in range(3))
        ans+=literal_table(cycles[1:],k,rest)
    return ans


def main():
    literal=0
    for cyc in [(1,),(2,),(1,1),(2,1)]:
        for k in range(3):
            poly=table_polynomial(cyc,k,3)
            for beta in product(range(4),repeat=3):
                expected=literal_table(cyc,k,beta)
                assert int(poly[beta])==expected,(cyc,k,beta,poly[beta],expected)
                matrices=table_polytope(cyc,k,beta)
                assert len(matrices['variables'])==3*len(cyc)
                literal+=1
    rows=[];class_checks=0;partition_cases=0;positive_k=0
    for n in range(5):
        cap=5*n//2+2
        for part in partitions(5*n):
            if len(part)>5:continue
            lam=part+(0,)*(5-len(part))
            vals=multiplicities(n,lam,cap)
            actual_values=tuple(actual(mu,n,lam) for mu in LABELS)
            assert vals==actual_values,(n,lam,vals,actual_values)
            traces=balanced_traces(n,lam,cap)
            expected_traces=tuple(sum(CHAR[i][j]*actual_values[i] for i in range(7))
                                  for j in range(7))
            assert traces==expected_traces,(n,lam,traces,expected_traces)
            class_checks+=7;partition_cases+=1;positive_k+=lam[1]>n
            for mu,v in zip(LABELS,vals):
                rows.append({'n':n,'outer':','.join(map(str,mu)),
                    'output':','.join(map(str,lam)),'tail_table_count':v,
                    'cycle_index_MN':v,'status':'PASS'})
        print('completed n',n,'coefficient cases',len(rows),flush=True)
    low_degree=0
    for k in range(1,4):
        for N in range(5*k):
            for alpha in partitions(N):
                if len(alpha)>3:continue
                padded=alpha+(0,)*(3-len(alpha))
                for cyc in CLASSES:
                    assert trace_alpha(cyc,k,padded,5*k+1)==0
                    low_degree+=1
    receipt={'statement':'T-049','status':'PASS','partition_cases':partition_cases,
             'coefficient_cases':len(rows),'class_trace_checks':class_checks,
             'positive_k_cases':positive_k,'literal_table_cases':literal,
             'below_mk_zero_traces':low_degree,
             'method':'48 Weyl/exterior shifts of literal tail table counts; comparison with independent cycle-index/Murnaghan-Nakayama',
             'sha256':hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest()}
    with (HERE/'ARRANGEMENT_TAIL_CHECK.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    (HERE/'ARRANGEMENT_TAIL_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
