"""Independent direct plethysm checks for the G018 and G019 Newton tables."""
from pathlib import Path
from math import comb
import csv,hashlib,json
from verify_rectangular import partitions
from verify_outer4_chambers import actual,transpose

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"


def write(name,rows):
    with (HERE/name).open("w",newline="") as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter="\t")
        writer.writeheader();writer.writerows(rows)


def main():
    raw=(ROOT/"FIVE_POINT_WEDGE2_NEWTON_TABLE.json").read_bytes()
    table=json.loads(raw)
    assert table["period"]==60 and table["polynomial_degree"]==3
    rows=[]
    for n in range(1,7):
        for k in range(n):
            d=n-k-1
            lam=(d+3*k+3,d+2*k+1,d+1,d,d)
            for mu in partitions(5):
                nu=transpose(mu) if (d+1)%2 else mu
                q,r=divmod(k,60)
                expected=sum(c*comb(q,j) for j,c in enumerate(table["labels"][",".join(map(str,nu))][r]) if j<=q)
                value=actual(mu,n,lam)
                assert value==expected,("G018",n,k,d,mu,lam,value,expected)
                rows.append(dict(n=n,k=k,d=d,outer=",".join(map(str,mu)),
                    output=",".join(map(str,lam)),cycle_index_MN=value,
                    positive_Newton=expected,status="PASS"))
        print("G018 completed n",n,"cases",len(rows),flush=True)
    write("OUTER5_WEDGE2_INDEPENDENT_CHECK.tsv",rows)
    print("G018 PASS",len(rows),"SHA256",hashlib.sha256(raw).hexdigest(),flush=True)

    raw=(ROOT/"FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json").read_bytes()
    table=json.loads(raw)
    assert table["period"]==60 and table["degrees"]==[3,3]
    rows=[]
    for n in range(6):
        for a in range(n+1):
            for k in range(n-a+1):
                d=n-a-k
                lam=(d+2*a+3*k,d+a+2*k,d+a,d+a,d)
                for mu in partitions(5):
                    nu=transpose(mu) if (d+a)%2 else mu
                    qa,ra=divmod(a,60);qk,rk=divmod(k,60)
                    coefficients=table["labels"][",".join(map(str,nu))][ra][rk]
                    expected=sum(coefficients[4*i+j]*comb(qa,i)*comb(qk,j)
                        for i in range(4) for j in range(4) if i<=qa and j<=qk)
                    value=actual(mu,n,lam)
                    assert value==expected,("G019",n,a,k,d,mu,lam,value,expected)
                    rows.append(dict(n=n,a=a,k=k,d=d,outer=",".join(map(str,mu)),
                        output=",".join(map(str,lam)),cycle_index_MN=value,
                        positive_Newton=expected,status="PASS"))
        print("G019 completed n",n,"cases",len(rows),flush=True)
    write("OUTER5_SYMMETRIC_QUOTIENT_INDEPENDENT_CHECK.tsv",rows)
    print("G019 PASS",len(rows),"SHA256",hashlib.sha256(raw).hexdigest())


if __name__=="__main__":main()
