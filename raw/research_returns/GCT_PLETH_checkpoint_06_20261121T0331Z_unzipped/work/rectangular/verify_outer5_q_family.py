"""Independent cycle-index/MN check of the G017 fixed-tag formula."""
from pathlib import Path
import csv
import hashlib
import json
from verify_rectangular import partitions
from verify_outer4_chambers import actual, transpose

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "root" / "FIVE_POINT_Q_TAGS.json"


def main():
    data = SOURCE.read_bytes()
    catalog = json.loads(data)
    assert catalog["parameter_degrees"] == [2,4,6,10]
    tags = {tuple(t["label"]): t["coefficients"] for t in catalog["tags"]}
    coins = [1]+[0]*5
    for weight in [2,4,6,10]:
        for j in range(weight,6):
            coins[j] += coins[j-weight]
    rows = []
    for n in range(1,7):
        for k in range(n):
            d = n-k-1
            lam = (d+3*k+2,d+2*k+1,d+1,d+1,d)
            assert sum(lam) == 5*n
            for mu in partitions(5):
                nu = transpose(mu) if (d+1)%2 else mu
                expected = sum(c*coins[k-j] for j,c in enumerate(tags[nu]) if j<=k)
                value = actual(mu,n,lam)
                assert value == expected, (n,k,d,mu,lam,value,expected)
                threshold = {(4,1):0,(5,):1,(3,2):1,(3,1,1):1,
                             (2,2,1):1,(2,1,1,1):2,(1,1,1,1,1):3}[nu]
                assert (value>0) == (k>=threshold)
                rows.append(dict(n=n,k=k,d=d,outer=",".join(map(str,mu)),
                    output=",".join(map(str,lam)),cycle_index_MN=value,
                    fixed_tag_count=expected,status="PASS"))
        print("completed n =",n,"cases =",len(rows),flush=True)
    with (HERE/"OUTER5_Q_FAMILY_INDEPENDENT_CHECK.tsv").open("w",newline="") as out:
        writer=csv.DictWriter(out,fieldnames=list(rows[0]),delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print("PASS",len(rows),"Q-family cases; source SHA256",hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
