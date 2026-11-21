#!/usr/bin/env python3
"""Check the oracle-free T037 evaluator against independently computed receipts."""
from pathlib import Path
import csv
from outer4_positive import (
    polytopes, coin23, prefix23, coin246, interval46, normalize, TRIV,
)

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
SOURCE = WORK / "rectangular" / "OUTER4_ALL_FORMULA_INDEPENDENT_CHECK.tsv"


def partition(text):
    return tuple(int(x) for x in text.split(",") if x)


def main():
    for N in range(-5, 121):
        brute = [(x,y) for x in range(max(0,N//2+1))
                 for y in range(max(0,N//3+1)) if 2*x+3*y <= N]
        assert prefix23(N) == len(brute), ("prefix",N)
        assert coin23(N) == sum(2*x+3*y == N for x,y in brute), ("coin",N)
        xyz = [(x,y,z) for x in range(max(0,N//2+1))
               for y in range(max(0,N//4+1))
               for z in range(max(0,N//6+1)) if 2*x+4*y+6*z == N]
        assert coin246(N) == len(xyz), ("246",N)
    for low in range(-5,26):
        for high in range(-5,41):
            brute = sum(low <= 4*x+6*y <= high
                        for x in range(max(0,high//4+1))
                        for y in range(max(0,high//6+1)))
            assert interval46(low,high) == brute, ("interval46",low,high)

    rows = []
    point_total = 0
    polytope_total = 0
    with SOURCE.open() as f:
        original = list(csv.DictReader(f, delimiter="\t"))
    for row in original:
        n = int(row["n"])
        mu, lam = partition(row["outer"]), partition(row["output"])
        data, pp = polytopes(mu,n,lam)
        actual = int(row["cycle_index_MN"])
        value = sum(p.count() for p in pp)
        assert value == actual, (mu,n,lam,value,actual)
        assert len({p.tag for p in pp}) == len(pp)
        witnesses = 0
        for p in pp:
            desc = p.description()
            pts = list(p.points())
            assert len(pts) == len(set(pts)) == p.count(), (mu,n,lam,p)
            for x in pts:
                assert all(v>=0 for v in x)
                for a,rhs in zip(desc["equality_matrix"],desc["equality_rhs"]):
                    assert sum(v*w for v,w in zip(a,x)) == rhs
                for a,rhs in zip(desc["inequality_matrix"],desc["inequality_rhs"]):
                    assert sum(v*w for v,w in zip(a,x)) <= rhs
            witnesses += len(pts)
        assert witnesses == actual
        point_total += witnesses
        polytope_total += len(pp)
        rows.append(dict(n=n,outer=row["outer"],output=row["output"],
                         polytope_count=len(pp),direct_positive=value,
                         cycle_index_MN=actual,enumerated_witnesses=witnesses,
                         status="PASS"))
    invalid = [
        (TRIV,-1,()),
        ((3,),1,(4,)),
        (TRIV,1,(2,0,2)),
        (TRIV,1,(3,)),
        (TRIV,1,(5,-1)),
    ]
    for args in invalid:
        try:
            normalize(*args)
        except ValueError:
            pass
        else:
            raise AssertionError(("accepted invalid input",args))
    assert polytopes(TRIV,2,(2,2,2,1,1))[1] == []
    dest = HERE / "OUTER4_DIRECT_POLYTOPE_CHECK.tsv"
    with dest.open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter="\t")
        writer.writeheader();writer.writerows(rows)
    summary = (
        f"PASS {len(rows)} independent coefficient comparisons.\n"
        f"PASS {polytope_total} exact tagged polytope matrices.\n"
        f"PASS {point_total} enumerated tagged lattice witnesses.\n"
        "PASS arithmetic coin/prefix counts and invalid-input/long-partition cases.\n"
    )
    (HERE/"OUTER4_DIRECT_POLYTOPE_CHECK.txt").write_text(summary)
    print(summary,end="")


if __name__ == "__main__":
    main()

