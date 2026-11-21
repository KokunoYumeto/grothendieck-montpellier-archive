"""Independent exact behavior and literal matrix checks for G-021."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from functools import lru_cache
from itertools import product, combinations, permutations
from math import comb
import importlib.util, json, sys, subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent / "root"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ev = load("g021_evaluator", ROOT / "five_point_two_row_positive.py")
old = load("g020_evaluator", ROOT / "five_point_three_parameter_positive.py")
sys.path.insert(0, str(HERE.parent / "rectangular"))
from verify_rectangular import partitions, character, z

bound = json.loads((ROOT / "TWO_ROW_QUOTIENT_POLYNOMIAL_BOUND.json").read_text())
assert ev.ACTIVE_ORDERS == tuple(sorted(map(tuple, bound["downset"])))


@lru_cache(None)
def schur_plethysm(mu, n):
    result = defaultdict(Fraction)
    for alpha in partitions(5):
        ch = character(mu, alpha)
        if not ch:
            continue
        term = {(): Fraction(ch, z(alpha))}
        for length in alpha:
            nxt = defaultdict(Fraction)
            for previous, coefficient in term.items():
                for beta in partitions(n):
                    cycle = tuple(sorted(previous + tuple(length*r for r in beta),
                                         reverse=True))
                    nxt[cycle] += coefficient / z(beta)
            term = nxt
        for cycle, coefficient in term.items():
            result[cycle] += coefficient
    return dict(result)


small = 0
for x, b, k, t, d in product(range(4), repeat=5):
    if x+b+k+t+d > 3:
        continue
    for mu in ev.LABELS:
        _, _, n, lam = ev.parameters(x, b, k, t, d, mu)
        direct = sum(coefficient * character(lam, cycle)
                     for cycle, coefficient in schur_plethysm(mu, n).items())
        actual = ev.coefficient(x, b, k, t, d, mu)
        assert direct == actual, (x, b, k, t, d, mu, direct, actual)
        small += 1
print("genuine plethysm", small, flush=True)

specializations = 0
for (x, k, t), d, mu in product(
        [(0,0,0),(1,1,0),(2,2,1),(59,59,59),(60,0,0),
         (0,60,0),(0,0,60),(61,62,63),(137,128,191)],
        (0,1), ev.LABELS):
    assert ev.coefficient(x, 0, k, t, d, mu) == old.coefficient(x,k,t,d,mu)
    specializations += 1

hook = json.loads((HERE.parent / "theta" / "outer5" /
                   "HOOK_ALL_POWERS_TABLE.json").read_text())["labels"]
hook_specializations = 0
for (x,k), d, mu in product(
        [(0,0),(0,1),(1,0),(1,1),(2,2),(59,59),(60,0),
         (0,60),(61,62),(137,128)], (0,1), ev.LABELS):
    _, nu, _, _ = ev.parameters(x,1,k,0,d,mu)
    constants = hook[",".join(map(str,nu))][x % 60][k % 60]
    expected = sum(constants[4*i+j]*comb(x//60,i)*comb(k//60,j)
                   for i in range(4) for j in range(4))
    assert expected == ev.coefficient(x,1,k,0,d,mu)
    hook_specializations += 1
print("specializations", specializations, hook_specializations, flush=True)

support = json.loads((ROOT / "TWO_ROW_QUOTIENT_SUPPORT.json").read_text())
zero_checks = 0
for name, mu in zip(("5","41","32","311","221","2111","11111"), ev.LABELS):
    for x,b,k,t in support["labels"][name]["zeros"]:
        d = (x+b) % 2
        assert ev.coefficient(x,b,k,t,d,mu) == 0
        zero_checks += 1
        for axis in range(4):
            args = [x,b,k,t]
            args[axis] += 60
            assert ev.coefficient(*args,d,mu) > 0
            zero_checks += 1
print("support boundary checks", zero_checks, flush=True)


def h(g,n):
    if n < 0:
        return 0
    if g == 0:
        return comb(n+3,3)
    if g == 1:
        return (n//2+1)*((n+1)//2+1)
    if g == 2:
        return n//2+1 if n % 2 == 0 else 0
    if g == 3:
        return n//3+1
    if g == 4:
        return (1,-1,1,0,0,0)[n % 6]
    if g == 5:
        return int(n % 4 == 0)
    return (1,-1,0,0,0)[n % 5]


def determinant(matrix):
    result = 0
    for perm in permutations(range(3)):
        value = (-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for i in range(3):
            value *= matrix[i][perm[i]]
        result += value
    return result


def ambient_minus_jets(g,x,b,k,t):
    a,c = x+b,2*k+t
    matrix = [[h(g,a+c+j) for j in range(3)],
              [h(g,a-1+j) for j in range(3)],
              [h(g,x-2+j) for j in range(3)]]
    ambient = (1,-1,1,1,-1,-1,1)[g]**a * determinant(matrix)
    hw = lambda n: h(g,n)-h(g,n-1)
    jet_fiber = hw(a)*hw(b)-hw(a+1)*hw(b-1)
    return ambient - ev.FIXED_LETTERS[g]*h(g,k-1)*jet_fiber


huge = (10**120+61,10**110+62,10**100+63,10**90+64,10**80+1)
for mu in ev.LABELS:
    _,nu,_,_ = ev.parameters(*huge,mu)
    numerator = sum(size*ch*ambient_minus_jets(g,*huge[:4])
                    for g,(size,ch) in enumerate(zip(ev.CLASS_SIZES,ev.CHARACTERS[nu])))
    assert numerator % 120 == 0
    assert numerator//120 == ev.coefficient(*huge,mu)
print("large integer ambient-Schur comparisons", 7, flush=True)


def valid(poly,point):
    return (all(sum(c*x for c,x in zip(row,point)) == rhs
                for row,rhs in poly["equalities"])
            and all(sum(c*x for c,x in zip(row,point)) <= rhs
                    for row,rhs in poly["inequalities"]))


matrix_cases = boundary_points = witness_points = 0
cases = [(0,0,0,0),(1,0,0,0),(1,2,1,0),(60,0,0,0),
         (0,60,0,0),(0,0,60,0),(0,0,0,60),(120,120,120,120),(61,62,63,64)]
for args,mu in product(cases,ev.LABELS):
    polys = ev.polytopes(*args,0,mu)
    qs = tuple(v//60 for v in args)
    total = 0
    by_order = {}
    for poly in polys:
        assert len(poly["variables"]) <= 11
        orders = tuple(poly["orders"])
        chains = [list(combinations(range(q),degree)) for q,degree in zip(qs,orders)]
        count = poly["constant"]
        for chain_list in chains:
            count *= len(chain_list)
        assert count == poly["lattice_count"]
        total += count
        by_order[orders] = poly
        for chain_tuple in product(*chains):
            flat = sum(chain_tuple,())
            for yy in {0,poly["constant"]-1}:
                assert valid(poly,(*qs,yy,*flat))
                boundary_points += 1
            assert not valid(poly,(*qs,poly["constant"],*flat))
    actual = ev.coefficient(*args,0,mu)
    assert total == actual
    seen = set()
    for item in ev.witnesses(*args,0,mu,limit=100):
        order,point = tuple(item["orders"]),tuple(item["point"])
        assert valid(by_order[order],point)
        assert (order,point) not in seen
        seen.add((order,point))
        witness_points += 1
    assert len(seen) == min(actual,100)
    matrix_cases += 1

for mu in ev.LABELS:
    points = list(ev.witnesses(*huge,mu,limit=2))
    assert len(points) == 2
    polys = {tuple(p["orders"]):p for p in ev.polytopes(*huge,mu)}
    assert all(valid(polys[tuple(point["orders"])],point["point"]) for point in points)

bad = [(-1,0,0,0,0,(5,)),(0,True,0,0,0,(5,)),(0,0,0.0,0,0,(5,)),
       (0,0,0,0,0,(4,)),(0,0,0,0,0,(3,2.0))]
for args in bad:
    try:
        ev.coefficient(*args)
    except ValueError:
        pass
    else:
        raise AssertionError(("accepted invalid input",args))
cli = subprocess.run([sys.executable,str(ROOT/"five_point_two_row_positive.py"),
                      "--x","1","--b","2","--k","1","--t","0","--d","0",
                      "--outer","5","--polytopes","--witnesses","2"],
                     capture_output=True,text=True,check=True)
cli_data = json.loads(cli.stdout)
assert cli_data["coefficient"] == 2 and cli_data["witness_count"] == 2
assert not cli_data["witnesses_truncated"] and len(cli_data["polytopes"]) <= 122
receipt = {
    "statement":"G021 standard-library evaluator validation","status":"PASS",
    "active_downset_match":122,"genuine_Murnaghan_Nakayama_plethysm_cases":small,
    "G020_specializations":specializations,"T043_specializations":hook_specializations,
    "zero_and_direction_checks":zero_checks,"large_integer_ambient_Schur_comparisons":7,
    "matrix_count_cases":matrix_cases,"literal_boundary_points":boundary_points,
    "lazy_witness_points":witness_points,"huge_quotient_witness_checks":14,
    "invalid_input_cases":len(bad),"CLI_JSON_check":True,
}
(HERE/"TWO_ROW_EVALUATOR_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
