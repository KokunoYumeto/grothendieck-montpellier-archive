import sys
sys.setrecursionlimit(10000)
from benzel_check import region, count_tilings


def CL(a, b):
    s = (a + b) % 3
    if s == 0:
        return (3*a*a - 6*a*b + 3*b*b - a - b) // 2
    if s == 1:
        return (-a*a + 4*a*b - b*b - a - b + 2) // 2
    return (3*a*a - 6*a*b + 3*b*b + a + b - 2) // 2


for n in range(5, 8):
    t, counts, _ = count_tilings(region(n, 2*n - 4))
    print(f"(n,2n-4)=({n},{2*n-4}) T103={t} patterns={len(counts)}")

M = int(sys.argv[1]) if len(sys.argv) > 1 else 9
bad = []
checked = 0
for a in range(2, M + 1):
    for b in range(a, M + 1):
        if b > 2 * a - 2:
            continue
        cl = CL(a, b)
        reg = region(a, b)
        e103, _, _ = count_tilings(reg, 'RHVD', limit=1)
        refl = frozenset((-q - r, r) for (q, r) in reg)  # not used
        checked += 1
        if (e103 > 0) != (cl >= 0):
            bad.append((a, b, cl, e103))
        if a + b in (0,) :
            pass
print('pairs checked (type 103 sign rule, 2<=a<=b<=%d, b<=2a-2):' % M, checked, 'mismatches:', bad)
