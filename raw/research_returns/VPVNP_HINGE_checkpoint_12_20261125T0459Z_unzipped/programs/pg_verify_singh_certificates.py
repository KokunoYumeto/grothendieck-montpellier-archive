"""Independent semantic and exact-arithmetic audit of Singh's rank certificates.

Unlike the author's checker, this validates every L=5 row against a precise
subspace/rank inequality and every explicit L=7 row.  For orbit rows it also
enumerates all 7! relabelings, checking the stated orbit cardinality and uniform
averaging on every subspace type.  It does not invoke Lean.

--import-source converts primary-source text into self-contained mathematical
proof data; the source Python checker is never imported or executed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import argparse
import hashlib
import json
import re

WORK = Path(__file__).resolve().parents[1]
DATA = WORK / "inputs/pg_singh_rank_certificates.json"
OUT = WORK / "outputs/pg_singh_certificate_verification.json"


def word(text):
    return sorted(set(re.findall(r"[AC]\d+", text)))


def dimension(fn, letters):
    return fn+"("+"+".join(sorted(letters))+")"


def vector(terms):
    d = Counter()
    for key, coefficient in terms:
        if key not in ("f()", "g()"):
            d[key] += coefficient
    return {k: v for k, v in d.items() if v}


def parse_expression(text):
    terms = []
    pattern = r"([+-]\d+)\*((?:[fg]\([^)]*\))|(?:m\[\d+,\d+\])|r\b|k\b|v\d+)"
    found = list(re.finditer(pattern, text))
    remainder = re.sub(pattern, "", text).strip()
    assert not remainder, (text, remainder)
    for match in found:
        value, name = int(match[1]), match[2]
        if name[0] in "fg":
            name = dimension(name[0], word(name))
        terms.append((name, value))
    return vector(terms)


def import_source(folder):
    out = {"source": "Arth Singh, Lower bounds for Naslund's crossing problem (2026)",
           "source_sha256": {}, "five": [], "seven": []}
    for filename in ("L5_fifteen_elevenths.txt", "L7_orbit_rows.txt",
                     "L7_sixtyseven_fortyninths.txt"):
        out["source_sha256"][filename] = hashlib.sha256((folder/filename).read_bytes()).hexdigest()
    pattern = re.compile(r"(\S+) x \[ (.*) <= (-?\d+) \]")
    for line in (folder/"L5_fifteen_elevenths.txt").read_text().splitlines():
        match = pattern.fullmatch(line.strip())
        if match:
            out["five"].append({"weight": match[1],
                                "row": parse_expression(match[2]), "rhs": int(match[3])})
    original = []
    for line in (folder/"L7_orbit_rows.txt").read_text().splitlines():
        match = pattern.fullmatch(line.strip())
        if match:
            original.append({"weight": match[1],
                             "row": parse_expression(match[2]), "rhs": int(match[3])})
    explanations = (folder/"L7_sixtyseven_fortyninths.txt").read_text().splitlines()
    assert len(original) == len(explanations) == 77
    for row, line in zip(original, explanations):
        assert Q(line.split()[0]) == Q(row["weight"])
        if line.split()[1] == "orbit":
            match = re.fullmatch(r"\S+\s+orbit\s+(\d+)\s+(submod|mono)\s+(.+)\s+<= 0", line)
            assert match, line
            orbit_size, kind, expression = int(match[1]), match[2], match[3]
            compare = ">=" if kind == "submod" else "<="
            left, right = expression.split(compare)
            fn = re.search(r"([fg])\(", expression)[1]
            left_sets = [word(x) for x in re.findall(r"[fg]\(([^)]*)\)", left)]
            right_sets = [word(x) for x in re.findall(r"[fg]\(([^)]*)\)", right)]
            row.update(kind=kind, family=fn, left_sets=left_sets,
                       right_sets=right_sets, orbit_size=orbit_size)
        else:
            row["kind"] = "explicit"
        out["seven"].append(row)
    assert len(out["five"]) == 189
    DATA.write_text(json.dumps(out, indent=2)+"\n")
    return out


def classify_five(row, rhs):
    # Every template below is justified explicitly in the manuscript audit.
    assert all(int(token[1:]) < 5 for key in row for token in word(key))
    if rhs == -1:
        for fn in ("f", "g"):
            for i in range(5):
                if row == {dimension(fn, [f"A{i}", f"C{i}"]): -1}:
                    return "diagonal spanning"
        raise AssertionError((row, rhs))
    assert rhs == 0
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            m = f"m[{i},{j}]"
            candidates = [
                ("column intersection", [(m, 1), (dimension("f", [f"A{i}",f"C{j}"]),1),
                  (dimension("f", [f"A{i}"]),-1),(dimension("f",[f"C{j}"]),-1)]),
                ("transposed intersection", [(m,1),(dimension("g",[f"A{j}",f"C{i}"]),1),
                  (dimension("g",[f"A{j}"]),-1),(dimension("g",[f"C{i}"]),-1)]),
                ("Sylvester r", [(m,-1),("r",-1),(dimension("f",[f"A{i}"]),1),
                  (dimension("g",[f"A{j}"]),1)]),
                ("Sylvester s", [(m,-1),("k",-1),(dimension("f",[f"C{j}"]),1),
                  (dimension("g",[f"C{i}"]),1)])]
            for kind, terms in candidates:
                if row == vector(terms):
                    return kind
    families = {key[0] for key in row}
    assert len(families) == 1 and families <= {"f","g"}, row
    fn = next(iter(families))
    sets = {key: frozenset(word(key)) for key in row}
    positives = [sets[k] for k, v in row.items() for _ in range(max(v,0))]
    negatives = [sets[k] for k, v in row.items() for _ in range(max(-v,0))]
    if len(positives) == len(negatives) == 1:
        assert positives[0] < negatives[0], row
        return "monotonicity"
    assert len(negatives) == 2
    s, t = negatives
    expected = vector([(dimension(fn, s|t),1),(dimension(fn,s&t),1),
                       (dimension(fn,s),-1),(dimension(fn,t),-1)])
    assert row == expected, row
    return "submodularity"


def orbit_type(letters):
    a = {int(s[1:]) for s in letters if s[0] == "A"}
    c = {int(s[1:]) for s in letters if s[0] == "C"}
    return len(a-c), len(c-a), len(a&c)


TYPES = [(a,c,b) for a in range(8) for c in range(8-a) for b in range(8-a-c)]


def orbit_key(fn, letters):
    return f"{fn}{orbit_type(letters)}"


def decode_original(row):
    result = {}
    for key, value in row.items():
        i = int(key[1:])
        if i < 240:
            fn, j = ("f", i) if i < 120 else ("g", i-120)
            if TYPES[j] == (0,0,0):
                continue
            key = f"{fn}{TYPES[j]}"
        else:
            key = {240:"m",241:"r",242:"k"}[i]
        result[key] = result.get(key,0)+value
    return {k:v for k,v in result.items() if v}


def verify_orbit(record):
    fn, kind = record["family"], record["kind"]
    left = [frozenset(s) for s in record["left_sets"]]
    right = [frozenset(s) for s in record["right_sets"]]
    if kind == "submod":
        assert len(left) == len(right) == 2
        assert set(right) == {left[0]|left[1],left[0]&left[1]}
        base = vector([(dimension(fn,s),-1) for s in left]+
                      [(dimension(fn,s),1) for s in right])
    else:
        assert len(left) == len(right) == 1 and left[0] < right[0]
        base = vector([(dimension(fn,left[0]),1),(dimension(fn,right[0]),-1)])
    orbit = set()
    accumulated = Counter()
    for perm in permutations(range(7)):
        mapped = vector([(dimension(fn,[x[0]+str(perm[int(x[1:])]) for x in word(key)]),val)
                         for key,val in base.items()])
        signature = tuple(sorted(mapped.items()))
        orbit.add(signature)
        accumulated.update(mapped)
    assert len(orbit) == record["orbit_size"], (len(orbit),record["orbit_size"])
    by_type = defaultdict(list)
    summed = Counter()
    for key,val in accumulated.items():
        typ = orbit_key(fn,word(key))
        by_type[typ].append(val)
        summed[typ] += val
    # The value assigned to each set in a given type must be the same.
    assert all(len(set(values)) == 1 for values in by_type.values())
    averaged = {key:Q(value,5040) for key,value in summed.items() if value}
    assert averaged == decode_original(record["row"])
    assert record["rhs"] == 0
    return averaged


def verify_explicit(record):
    fA, fC, fAC, fD = [f"f{t}" for t in ((1,0,0),(0,1,0),(1,1,0),(0,0,1))]
    gA, gC, gAC, gD = [f"g{t}" for t in ((1,0,0),(0,1,0),(1,1,0),(0,0,1))]
    valid = [({fD:-1},-1),({gD:-1},-1),
             ({"m":1,fAC:1,fA:-1,fC:-1},0),
             ({"m":1,gAC:1,gA:-1,gC:-1},0),
             ({fA:1,gA:1,"m":-1,"r":-1},0),
             ({fC:1,gC:1,"m":-1,"k":-1},0)]
    row = decode_original(record["row"])
    assert (row,record["rhs"]) in valid
    return row


def sum_certificate(records, rows, expected):
    total = defaultdict(Q)
    for record, row in zip(records, rows):
        w = Q(record["weight"])
        assert w > 0
        for key,value in row.items():
            total[key] += w*value
        total["N"] -= w*record["rhs"]
    assert total["r"] == total["k"] == -1
    assert total["N"] == expected
    slack = {k:v for k,v in total.items() if k not in ("N","r","k") and v}
    assert all(v >= 0 for v in slack.values()), slack
    return {"N_coefficient": str(total["N"]), "width_coefficients": [-1,-1],
            "nonzero_slack_coefficients": {k:str(v) for k,v in sorted(slack.items())},
            "correct_sum": f"{expected} N + nonnegative slack <= r+s"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--import-source", type=Path)
    args = parser.parse_args()
    data = import_source(args.import_source) if args.import_source else json.loads(DATA.read_text())
    kinds = Counter(classify_five(row["row"],row["rhs"]) for row in data["five"])
    five = sum_certificate(data["five"],[r["row"] for r in data["five"]],Q(15,11))
    five.update(rows=189,validated_row_kinds=dict(kinds))
    seven_rows = [verify_explicit(r) if r["kind"] == "explicit" else verify_orbit(r)
                  for r in data["seven"]]
    seven = sum_certificate(data["seven"],seven_rows,Q(67,49))
    seven.update(rows=77,explicit_slice_rows=6,orbit_rows=71,
                 relabelings_per_orbit=5040,orbit_cardinalities_checked=True)
    out = {"source_sha256":data["source_sha256"],"five":five,"seven":seven,
           "status":"PASS: all inequality semantics and exact weighted sums verified",
           "lean_status":"Not run; no Lean kernel claim",
           "paper_prose_note":"Both certificates cancel every auxiliary variable exactly. The left-versus-right coefficient wording in Appendix A therefore has no effect on these bounds."}
    OUT.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__ == "__main__":
    main()
