"""R042 literal cubic extension and finite coefficients."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
from math import factorial
import csv,random
from verify_rectangular import sign
from verify_outer4_chambers import actual
from verify_second_row_two_rank_law import product_form
from verify_four_even_tail_block import literal,generators

HERE=Path(__file__).resolve().parent

def contractions(m,vectors,extension):
    n=3;pair={}
    for beta,value in product_form(vectors).items():
        norm=F(value,factorial(n))
        for e in beta:norm*=factorial(e)
        pair[beta]=norm
    def moment(e):
        if sum(e)==4:
            return F(extension*(1+sum((j+2)**v for j,v in enumerate(e))))
        assert sum(e)<=3
        return pair.get((3-sum(e),)+tuple(e),0)
    p=[moment((j,)+(0,)*(m-1)) for j in range(3)]
    sums=[F(0)]*4
    perms=tuple((p,sign(p)) for p in permutations(range(m+1)))
    for sigma,s1 in perms:
        for tau,s2 in perms:
            block=[]
            for i in range(m+1):
                e=[0]*m
                if sigma[i]:e[sigma[i]-1]+=1
                if tau[i]:e[tau[i]-1]+=1
                row=[]
                for q in range(3):
                    z=e[:];z[0]+=q;row.append(moment(z))
                block.append(row)
            base=F(1)
            for row in block:base*=row[0]
            first=F(0);second=F(0)
            for i in range(m+1):
                prod=F(1)
                for j in range(m+1):
                    if i!=j:prod*=block[j][0]
                first+=block[i][1]*prod
                second+=block[i][2]*prod
            square=second
            for i,j in combinations(range(m+1),2):
                prod=2*block[i][1]*block[j][1]
                for q in range(m+1):
                    if q not in (i,j):prod*=block[q][0]
                square+=prod
            for q,value in enumerate((base,first,second,square)):
                sums[q]+=s1*s2*value
    return p,sums

def beta(a,m):
    return (F(a-1,a*a),F(a*a-3*a+m+2,a**3),
            F(-(m-1)*(2*a-m-2),2*a**3))

def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        w.writeheader();w.writerows(rows)

def main():
    rng=random.Random(42042);rows=[]
    for m in (2,3,4):
        for tag in (0,1):
            lower=[tuple(rng.randrange(-3,5) for j in range(m)) for i in range(3)]
            vectors=[(i+2,)+tuple((i+2)*v for v in row) for i,row in enumerate(lower)]
            P1=generators(vectors)[0];u=2*3*4
            values=[]
            for extension in (0,7):
                p,sums=contractions(m,vectors,extension)
                out={}
                for a in range(max(4,m+1),9):
                    b=beta(a,m);ps=literal(a,m,p,sums)
                    out[a]=(b[0]*ps[1]-b[1]*ps[0],b[0]*ps[2]-b[2]*ps[0])
                values.append(out)
            assert values[0]==values[1],(m,tag,values)
            for a,pair in values[0].items():
                if m==2:
                    scalars=(F((a-3)*(a-2)*(a-1)*(a*a-3*a+8),216*a**3),
                             F(-(a-3)*(a-2)*(a-1)*(5*a-8),216*a**3))
                else:scalars=(F(0),F(0))
                for j in (0,1):
                    expected=scalars[j]*u**a*P1
                    assert pair[j]==expected,(a,m,tag,j,pair[j],expected)
                    rows.append(dict(a=a,m=m,sample=tag,generator=j+2,
                        literal_pairing=str(pair[j]),expected=str(expected),
                        independent_fourth_extensions_agree=True,status='PASS'))
        print('completed cubic extension m',m,'cases',len(rows),flush=True)
    write('FOUR_EVEN_TAIL_CUBIC_SCALAR_CHECK.tsv',rows)
    rows=[]
    for a in range(4,10):
        for m in range(2,a):
            lam=(3*a-2*m-2,4)+(2,)*(m-1)
            if lam[0]<4:continue
            target=actual((a,),3,lam);source=actual((3,),a,lam)
            assert target==min(2,max(0,a-m-1)),(a,m,target)
            assert source==int(m==2),(a,m,source)
            rows.append(dict(a=a,m=m,output=','.join(map(str,lam)),
                target_actual_MN=target,source_actual_MN=source,status='PASS'))
        print('completed cubic family MN a',a,'cases',len(rows),flush=True)
    write('FOUR_EVEN_TAIL_CUBIC_MN_CHECK.tsv',rows)
    print('PASS cubic actual coefficients',len(rows),flush=True)

if __name__=='__main__':main()

