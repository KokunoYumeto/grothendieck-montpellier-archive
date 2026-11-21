"""Extract and exhaustively verify the finite kernel tails used in R032."""
from pathlib import Path
from itertools import product
import csv

HERE=Path(__file__).resolve().parent


def main():
    with (HERE/'OUTER5_CANONICAL_LOW_DEGREE_CHECK.tsv').open() as f:
        records=list(csv.DictReader(f,delimiter='\t'))
    bases={t:[] for t in range(1,6)}
    for row in records:
        t=int(row['n']);mu=tuple(map(int,row['output'].split(',')))
        k=int(row['actual_cokernel_multiplicity'])
        if mu[1]<=t and k:
            bases[t].append((mu,k))
    bases[5]=[((12,5,4,3,1),1),((11,5,4,4,1),1)]
    assert [len(bases[t]) for t in range(1,6)]==[0,3,4,19,2]
    out=[];tail_data=[]
    for t in range(1,6):
        tails=sorted(set(mu[1:] for mu,k in bases[t]))
        minimal=[v for v in tails if not any(u!=v and all(x<=y for x,y in zip(u,v)) for u in tails)]
        wanted=[(t-j,)+(2,)*(j+1)+(0,)*(2-j) for j in range(t-1)] if t<=4 else [(5,4,3,1)]
        assert minimal==sorted(wanted),(t,minimal,wanted)
        for mu,k in bases[t]:
            out.append(dict(t=t,partition=','.join(map(str,mu)),kernel_multiplicity=k,
                            minimal_tail=int(mu[1:] in minimal)))
        for tail in product(range(t+1),repeat=4):
            if tuple(sorted(tail,reverse=True))!=tail:continue
            excluded=any(all(x<=y for x,y in zip(v,tail)) for v in minimal)
            if t<=4:
                p=tail[0];q=1+sum(v>=2 for v in tail)
                safe=p+q<=t+2
            else:
                safe=tail[0]<=4 or tail[1]<=3 or tail[2]<=2 or tail[3]==0
            assert safe==(not excluded),(t,tail,safe,excluded)
            tail_data.append(dict(t=t,tail=','.join(map(str,tail)),
                                  safe=int(safe),status='PASS'))
    for name,rows in [('FINITE_BASE_KERNELS.tsv',out),('FINITE_BASE_TAIL_CHECK.tsv',tail_data)]:
        with (HERE/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
    lines=['| t | Base kernel partition | Multiplicity |','|---:|---|---:|']
    lines += [f'| {r["t"]} | ({r["partition"]}) | {r["kernel_multiplicity"]} |' for r in out]
    (HERE/'FINITE_BASE_KERNELS.md').write_text('\n'.join(lines)+'\n')
    print('PASS all28 base-kernel summands and',len(tail_data),'sorted tails')


if __name__=='__main__':main()
