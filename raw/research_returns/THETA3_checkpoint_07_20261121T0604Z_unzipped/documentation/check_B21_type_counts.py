"""Independent exact complete-type/autocorrelation calculation for B21."""
import json

def autocorrelation(signs):
    hol = [(1 + s) // 2 for s in signs]
    return [sum(hol[t] * hol[(k + t) % 6] for t in range(6)) for k in range(6)]

rows = []
for a, b in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
    d = [1, a, b, -1, -a, -b]
    flipped = d.copy()
    flipped[0] *= -1
    flipped[3] *= -1
    ad, af = autocorrelation(d), autocorrelation(flipped)
    rows.append({'type': d, 'A': ad, 'A_flip': af,
                 'M': [2*x+y for x,y in zip(ad, af)]})
assert all(rows[0]['type'][i]+rows[1]['type'][i] ==
           rows[2]['type'][i]+rows[3]['type'][i] for i in range(6))
difference = [rows[0]['M'][i]+rows[1]['M'][i]-rows[2]['M'][i]-rows[3]['M'][i]
              for i in range(6)]
assert difference == [0, 6, -6, 0, -6, 6]
print(json.dumps({'rows': rows, 'difference': difference, 'status': 'PASS'}, indent=2))
