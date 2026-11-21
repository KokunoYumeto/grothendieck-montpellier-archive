"""Exact SLP evaluation for a marked sixfold raw-to-base group isomorphism."""
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup


class MarkedRawLift:
    def __init__(self, stored, raw_generators):
        args, state = stored
        self.G = PermutationGroup(args)
        self.G.__dict__.update(state)
        self.identity = np.arange(len(raw_generators[0]))
        self.memo = {}
        for p, q in zip(self.G.generators, raw_generators):
            assert np.array_equal(q[::6] // 6, np.array(p.array_form))
            self.memo[p] = q
            self.memo[p**-1] = np.argsort(q)

    def product(self, factors):
        out = self.identity.copy()
        for p in factors:
            out = out[self.strong(p)]
        return out

    def strong(self, p):
        if p.is_identity:
            return self.identity
        if p in self.memo:
            return self.memo[p]
        if p in self.G._strong_gens_slp:
            out = self.product(self.G._strong_gens_slp[p])
        elif p**-1 in self.G._strong_gens_slp:
            out = np.argsort(self.strong(p**-1))
        else:
            out = self.product(self.G.generator_product(p, original=False))
        assert np.array_equal(out[::6] // 6, np.array(p.array_form))
        self.memo[p] = out
        self.memo[p**-1] = np.argsort(out)
        return out

    def lift(self, value):
        p = Permutation(value.tolist())
        assert self.G.contains(p)
        return self.strong(p)
