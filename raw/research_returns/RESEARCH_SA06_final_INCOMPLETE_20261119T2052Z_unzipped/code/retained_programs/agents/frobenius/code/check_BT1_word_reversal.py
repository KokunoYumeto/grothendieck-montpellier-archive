from itertools import product
rot=lambda w:[w[i:]+w[:i] for i in range(len(w))]
for n in range(2,7):
 ws=[w for x in product('fv',repeat=n) for w in [''.join(x)] if len(set(rot(w)))==n and min(rot(w))==w]
 pairs=[(w,min(rot(w[::-1]))) for w in ws if w!=min(rot(w[::-1]))]
 print(n,len(ws),pairs)
