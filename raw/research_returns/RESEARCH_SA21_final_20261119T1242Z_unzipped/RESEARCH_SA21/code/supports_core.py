"""Exact finite polarity computations for RESEARCH_SA21.

GPT-6 Astra (OpenAI), 19 November 2026. No floating point arithmetic.
Vertices and sets are represented by bit masks. N(A) is the common
open neighbourhood of A, and support(A) = N(N(A)).
"""
from itertools import combinations


def bits(a):
    while a:
        b = a & -a
        yield b.bit_length() - 1
        a ^= b


class Orthoset:
    def __init__(self, names, edges):
        self.names = list(names)
        self.n = len(names)
        self.full = (1 << self.n) - 1
        self.adj = [0] * self.n
        for a, b in edges:
            assert a != b
            self.adj[a] |= 1 << b
            self.adj[b] |= 1 << a
        self._polar = {0: self.full}
        self._closed = None

    def polar(self, a):
        if a not in self._polar:
            b = a & -a
            self._polar[a] = self.adj[b.bit_length()-1] & self.polar(a ^ b)
        return self._polar[a]

    def close(self, a):
        return self.polar(self.polar(a))

    def closed(self):
        if self._closed is None:
            c = {self.full}
            for n in self.adj:
                c |= {a & n for a in c}
            self._closed = sorted(c, key=lambda a: (a.bit_count(), a))
            assert all(self.close(a) == a for a in c)
        return self._closed

    def join(self, a, b):
        return self.close(a | b)

    def om_witness(self):
        """A<B with B meet A-perp=0; equivalent to failure of OML."""
        c = self.closed()
        for b in c:
            for a in c:
                if a != b and a & ~b == 0 and b & self.polar(a) == 0:
                    return a, b
        return None

    def om_equation_witness(self):
        for b in self.closed():
            for a in self.closed():
                if a & ~b == 0 and self.join(a, b & self.polar(a)) != b:
                    return a, b
        return None

    def boolean_witness(self):
        for a in self.closed():
            for b in self.closed():
                if a & b == 0 and a & ~self.polar(b):
                    return a, b
        return None

    def maximal_cliques(self, domain=None):
        domain = self.full if domain is None else domain
        def bron(r, p, x):
            if not (p | x):
                yield r
                return
            u = max(bits(p | x), key=lambda i: (p & self.adj[i]).bit_count())
            for v in list(bits(p & ~self.adj[u])):
                yield from bron(r | (1 << v), p & self.adj[v], x & self.adj[v])
                p &= ~(1 << v)
                x |= 1 << v
        yield from bron(0, domain, 0)

    def sumner_witness(self, domain=None):
        """Sumner 1974 p492: a maximal clique E covered by N(u) union N(v), u not~v."""
        domain = self.full if domain is None else domain
        pairs = [(u,v) for u,v in combinations(bits(domain), 2)
                 if not (self.adj[u] >> v & 1)]
        for e in self.maximal_cliques(domain):
            for u,v in pairs:
                if e & ~(self.adj[u] | self.adj[v]) == 0:
                    return e,u,v
        return None

    def dacey_witness(self):
        for a in self.closed():
            for d in self.maximal_cliques(a):
                if self.close(d) != a:
                    return a,d,self.close(d)
        return None

    def decode(self, a):
        return [self.names[i] for i in bits(a)]

    def describe(self):
        return dict(vertices=self.names, edges=[(self.names[i],self.names[j])
                    for i in range(self.n) for j in range(i+1,self.n)
                    if self.adj[i] >> j & 1],
                    closed=[self.decode(a) for a in self.closed()])


def natural_posets(n):
    """All transitive strict subrelations of the fixed natural order.

    Every isomorphism type has a representative here; labelled orders with
    other linear extensions are not counted as separate structures.
    """
    pairs = list(combinations(range(n), 2))
    for mask in range(1 << len(pairs)):
        up = [0] * n
        for k,(a,b) in enumerate(pairs):
            if mask >> k & 1:
                up[a] |= 1 << b
        if any(up[b] & ~up[a] for a in range(n) for b in bits(up[a])):
            continue
        yield {(a,b) for a in range(n) for b in bits(up[a])}


def comparability(n, lt):
    return Orthoset(list(range(n)), lt)


def magasin(n, lt):
    names = [('P', a) for a in range(n)] + [('I',a,b) for a,b in sorted(lt)]
    def le(a,b): return a == b or (a,b) in lt
    def delta(x): return (x[1],) if x[0] == 'P' else x[1:]
    def posless(x,y):
        return x != y and all(le(a,b) for a in delta(x) for b in delta(y))
    edges = [(i,j) for i,j in combinations(range(len(names)),2)
             if posless(names[i],names[j]) or posless(names[j],names[i])]
    return Orthoset(names,edges)


def incidence(x,y):
    return x == y or (x[0]=='P' and y[0]=='I' and x[1] in y[1:])


def immediate(lt,x,y):
    if x == y: return True
    if y[0] != 'I': return False
    if x[0] == 'P': return (y[1],x[1]) in lt and (x[1],y[2]) in lt
    return (x[1] == y[1] or (y[1],x[1]) in lt) and (x[2] == y[2] or (x[2],y[2]) in lt)


def figures(g):
    """All incidence-closed cliques in an interval magasin, including empty."""
    seen = {0}
    for e in g.maximal_cliques():
        a = e
        while True:
            if all(not incidence(x,g.names[j]) or a >> i & 1
                   for j in bits(a) for i,x in enumerate(g.names)):
                seen.add(a)
            if not a: break
            a = (a-1) & e
    return sorted(seen)


def supp1_witness(g, fs):
    for f in fs:
        a = f
        while True:
            if g.close(f) & g.polar(a) != g.close(f ^ a):
                return f,a,g.close(f)&g.polar(a),g.close(f^a)
            if not a: break
            a = (a-1) & f
    return None
