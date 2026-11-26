from fractions import Fraction
def mobius(n):
    m, p, res = n, 2, 1
    while p*p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0: return 0
            res = -res
        p += 1
    if m > 1: res = -res
    return res
tr = {'1':2,'t':0,'r':-1}
def power(g,d):
    if g=='1': return '1'
    if g=='t': return 't' if d%2 else '1'
    if g=='r': return '1' if d%3==0 else 'r'
def L(n,g):
    s = 0
    for d in range(1,n+1):
        if n % d == 0:
            s += mobius(d)*tr[power(g,d)]**(n//d)
    return Fraction(s,n)
a = {1: Fraction(0)}
for n in range(2,40):
    a[n] = (2*L(n,'1')-L(n+1,'1')-2*L(n,'r')-3*L(n+1,'t')-2*L(n+1,'r'))/6
def b(n):
    s = 0
    for i in range(2,n):
        j = n-i
        if 2<=i<j: s += a[i]*a[j]
    if n%2==0:
        x = a[n//2]; s += x*(x-1)/2
    return s
W = {1:0,2:0,3:1,4:0,5:1,6:0,7:2,8:1,9:4,10:2,11:9,12:7}
print("n  a_n  b_n  d_n  W_n(LM2)")
for n in range(2,25):
    an = a[n]; bn = b(n); dn = max(0, an-bn)
    print(n, an, bn, dn, W.get(n,''))
