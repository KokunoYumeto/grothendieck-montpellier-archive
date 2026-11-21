#!/usr/bin/env python3
"""Independent exact audit of T037's fixed tables and scalar counts.

No coefficient oracle or implementation from the author is imported.  The
identities checked here are rational functions and finite arithmetic bounds.
"""
from pathlib import Path
import json
import sympy as s

q = s.symbols("q")
labels = ("4", "1111", "22", "31", "211")
chars = {
    "4": (1, 1, 1, 1, 1),
    "1111": (1, -1, 1, 1, -1),
    "22": (2, 0, 2, -1, 0),
    "31": (3, 1, -1, 0, -1),
    "211": (3, -1, -1, 0, 1),
}
sizes = (1, 6, 3, 8, 6)
trace = (
    (1 + q) / (1 - q) ** 2,
    1 / (1 + q),
    1 / (1 + q),
    (1 + q) / (1 + q + q**2),
    (1 + q) / (1 + q**2),
)
E = {
    "4": (0, 9), "1111": (3, 6), "22": (2, 4, 5, 7),
    "31": (2, 3, 4, 5, 6, 7), "211": (1, 3, 4, 5, 6, 8),
}
F = {"4": (0,), "1111": (3,), "22": (1, 2)}
G = {"4": (0,), "1111": (3,), "22": (1, 2),
     "31": (0, 1, 2), "211": (1, 2, 3)}
den = (1-q**4)*(1-q**6)
for label in labels:
    average = sum(a*b*c for a, b, c in zip(sizes, chars[label], trace))/24
    assert s.cancel(average - sum(q**e for e in E[label])/den) == 0

# All tensor entries are computed from the class table, not copied.
tensor = {}
for rho in F:
    for tau in labels:
        for nu in labels:
            numerator = sum(z*a*b*c for z, a, b, c in
                            zip(sizes, chars[rho], chars[tau], chars[nu]))
            assert numerator % 24 == 0
            multiplicity = numerator // 24
            assert multiplicity in (0, 1)
            tensor[rho, tau, nu] = multiplicity

tag_counts = {}
for nu in labels:
    d = sum(tensor[rho,tau,nu]*len(F[rho])*len(G[tau])
            for rho in F for tau in labels)
    w = sum(tensor[rho,tau,nu]*len(F[rho])*len(E[tau])
            for rho in F for tau in labels)
    tag_counts[nu] = dict(D=d, W=w, L=w, full_even=2*d+2*w)
assert tag_counts == {
    "4": {"D": 6, "W": 12, "L": 12, "full_even": 36},
    "1111": {"D": 6, "W": 12, "L": 12, "full_even": 36},
    "22": {"D": 12, "W": 24, "L": 24, "full_even": 72},
    "31": {"D": 18, "W": 36, "L": 36, "full_even": 108},
    "211": {"D": 18, "W": 36, "L": 36, "full_even": 108},
}

# The three S3 series, from the exact three-class trace average.
s3chars = ((1, 1, 1), (1, -1, 1), (2, 0, -1))
s3trace = (1/(1-q)**2, 1/(1-q**2), 1/(1+q+q**2))
s3tags = ((0,), (3,), (1, 2))
for character, tags in zip(s3chars, s3tags):
    average = sum(a*b*c for a,b,c in zip((1,3,2), character, s3trace))/6
    assert s.cancel(average - sum(q**f for f in tags)/((1-q**2)*(1-q**3))) == 0

def C(N):
    return 0 if N < 0 else 1 + N//6 - (N % 6 == 1)

def P(N):
    if N < 0:
        return 0
    answer = 0
    for e in (0,1):
        T = (N-3*e)//6
        answer += (T+1)*((N-3*e)//2+1) - 3*T*(T+1)//2
    return answer

for N in range(-12, 121):
    pairs = [(x,y) for x in range(max(0,N//2+1))
             for y in range(max(0,N//3+1))]
    assert C(N) == sum(2*x+3*y == N for x,y in pairs)
    assert P(N) == sum(2*x+3*y <= N for x,y in pairs)

# Direct enumeration of all interval endpoint parities used by A31.
for b in range(31):
    for e in range(10):
        count = sum(1 <= 4*x+6*y+e <= b+1
                    for x in range((b+1)//4+1)
                    for y in range((b+1)//6+1))
        assert count == P((b+1-e)//2)-P((-e)//2)

# The independent odd-c sign example from balanced Schur traces.
# h11*h5-h12*h4 at row degree4: one 2-cycle and two fixed letters.
fixed = lambda degree: sum(2*x+y+z == degree for x in range(5)
                          for y in range(5) for z in range(5))
assert fixed(11)-fixed(12) == 1

receipt = {
    "status": "PASS", "harmonic_rational_identities": 5,
    "S3_rational_identities": 3, "tensor_entries_checked": 75,
    "scalar_N_range": [-12,120], "harmonic_intervals_checked": 310,
    "odd_degree_transposition_trace": 1, "tag_counts": tag_counts,
    "scope": "Exact fixed-table and arithmetic identities; not a plethysm coefficient sweep.",
}
output = Path(__file__).with_name("OUTER4_FIXED_TABLE_RECEIPT.json")
output.write_text(json.dumps(receipt, indent=2)+"\n")
print(json.dumps(receipt, indent=2))
