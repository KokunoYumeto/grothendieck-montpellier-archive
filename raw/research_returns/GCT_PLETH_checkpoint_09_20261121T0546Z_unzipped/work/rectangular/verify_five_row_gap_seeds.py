"""Independent literal MN checks for the finite gap-two seed table."""
from pathlib import Path
import argparse,csv,hashlib,json,time
from verify_outer4_chambers import actual

HERE=Path(__file__).resolve().parent
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--max-inner',type=int,default=7)
    args=parser.parse_args()
    raw=(HERE.parent/'root'/'FIVE_ROW_GAP2_SEEDS.json').read_bytes()
    data=json.loads(raw);assert not data['failures']
    selected=sorted(((i,row) for i,row in enumerate(data['seeds']) if row['inner']<=args.max_inner),key=lambda pair:(pair[1]['inner'],pair[0]))
    rows=[];timings=[]
    for n in sorted({row['inner'] for _,row in selected}):
        start=time.perf_counter();count=0
        for index,row in selected:
            if row['inner']!=n:continue
            lam=tuple(row['partition']);assert sum(lam)==5*n
            for j,mu in enumerate(LABELS):
                value=actual(mu,n,lam);expected=row['multiplicities'][j]
                assert value==expected,(index,n,mu,lam,value,expected)
                rows.append(dict(seed=index,n=n,outer=','.join(map(str,mu)),
                    output=','.join(map(str,lam)),cycle_index_MN=value,
                    proposed_seed=expected,status='PASS'))
                count+=1
        elapsed=time.perf_counter()-start
        timings.append(dict(n=n,cases=count,seconds=elapsed))
        print('PASS n',n,'cases',count,'seconds',round(elapsed,3),flush=True)
    with (HERE/'FIVE_ROW_GAP2_SEEDS_MN_CHECK.tsv').open('w',newline='') as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    receipt=dict(input_SHA256=hashlib.sha256(raw).hexdigest(),max_inner=args.max_inner,
                 seeds=len(selected),cases=len(rows),timings=timings,status='PASS')
    (HERE/'FIVE_ROW_GAP2_SEEDS_MN_TIMING.txt').write_text(json.dumps(receipt,indent=2)+'\n')
    print('PASS',len(selected),'seeds;',len(rows),'coefficients; SHA256',receipt['input_SHA256'])


if __name__=='__main__':main()
