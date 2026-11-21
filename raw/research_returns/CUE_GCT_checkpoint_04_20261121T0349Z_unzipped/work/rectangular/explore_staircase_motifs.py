"""Exploration: second-order row and column relations in a b-row staircase.
No uniform rank conclusion is inferred from these finite computations.
"""
from pathlib import Path
import json, random
from check_simultaneous_chords import field_for, product_coefficients, rank_columns


def factors(m,k,p,roots,a,typ,pr,qr):
    if typ=='U':
        ai=[pr]+[i for i in range(m) if i not in {(a+j)%m for j in range(k+1)}]
        bi=[a,qr]+list(range(a+2,a+k))
    elif typ=='V':
        ai=[pr,a+1]+[i for i in range(m) if i not in {(a+j)%m for j in range(k+2)}]
        bi=[qr]+list(range(a+2,a+k+1))
    elif typ=='C':
        ai=[pr,a]+[i for i in range(m) if i not in {j%m for j in range(a-k,a+2)}]
        bi=[qr]+list(range(a-k,a-1))
    elif typ=='D':
        ai=[pr]+[i for i in range(m) if i not in {j%m for j in range(a-k+1,a+2)}]
        bi=[a,qr]+list(range(a-k+1,a-1))
    aa=product_coefficients([i%m for i in ai],roots,p)
    bb=product_coefficients([i%m for i in bi],roots,p)
    assert len(aa)==m-k+1 and len(bb)==k+1
    return aa,bb


def character_cols(m,b,k,t,p,q,proots,qroots):
    roots=[pow(q,i,p) for i in range(m)]
    pairs=[(r,t-r) for r in range(m-k+1) if 0<=t-r<=k]
    aa=product_coefficients(range(k,m),roots,p)
    bb=product_coefficients(range(k-1),roots,p)
    base=[[aa[r]*(bb[s] if s<len(bb) else 0)%p for r,s in pairs],
          [aa[r]*(bb[s-1] if 1<=s<=len(bb) else 0)%p for r,s in pairs]]
    def f(a,typ,pr,qr):
        a1,b1=factors(m,k,p,roots,a,typ,pr,qr)
        return [a1[r]*b1[s]%p for r,s in pairs]
    def sub(x,y):return [(u-v)%p for u,v in zip(x,y)]
    zero=[0]*len(pairs)
    row=[];column=[]
    for i in range(1,b):
        left=f(i-1,'V',proots[i-1],qroots[i-1]) if i>1 else zero
        right=f(i,'U',proots[i],qroots[i]) if i<b-1 else zero
        row.append(sub(left,right))
    for i in range(b-1):
        left=f(i,'D',proots[i-1],qroots[i]) if i>0 else zero
        right=f(i+1,'C',proots[i],qroots[i+1]) if i<b-2 else zero
        column.append(sub(left,right))
    return base,row,column


def main():
    data=[]
    for b in [4,5,6]:
        m=6*b;p,q=field_for(m);k=t=m//2
        rng=random.Random(104+b)
        best=0
        for case in range(100):
            pp={i:rng.randrange(m) for i in range(b-1)}
            qq={i:rng.randrange(m) for i in range(1,b-1)}
            base,row,col=character_cols(m,b,k,t,p,q,pp,qq)
            rr=rank_columns(base+row+col,p)-rank_columns(base,p)
            if rr>best:
                best=rr
                d={'b':b,'m':m,'p':p,'q':q,'case':case,'normal_rank':rr,
                   'p_roots':pp,'q_roots':qq,
                   'row_rank':rank_columns(base+row,p)-rank_columns(base,p),
                   'column_rank':rank_columns(base+col,p)-rank_columns(base,p)}
                data.append(d);print(json.dumps(d),flush=True)
            if rr==2*b-2:break
    Path(__file__).with_name('staircase_motif_exploration.json').write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':main()
