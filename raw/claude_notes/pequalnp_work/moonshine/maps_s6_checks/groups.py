from sympy.combinatorics import Permutation, PermutationGroup
def P(cycles, n): return Permutation([list(c) for c in cycles], size=n)
# S6-029 index-10 cover: s=(01)(24)(35)(69)(78), r=(023)(1)(467)(589)
s = P([(0,1),(2,4),(3,5),(6,9),(7,8)], 10); r = P([(0,2,3),(4,6,7),(5,8,9)], 10)
G = PermutationGroup([s, r]); sr = s*r
print("index-10: |G| =", G.order(), " transitive:", G.is_transitive(), " primitive:", G.is_primitive(),
      " is A10:", G.order() == 1814400, " is S10:", G.order() == 3628800, " cycle type sr:", sr.cycle_structure, " rs:", (r*s).cycle_structure)
# index-4: s=(01)(23), r=(023)(1)
s4 = P([(0,1),(2,3)], 4); r4 = P([(0,2,3)], 4)
G4 = PermutationGroup([s4, r4]); print("index-4: |G| =", G4.order(), " cycle sr:", (s4*r4).cycle_structure, (r4*s4).cycle_structure)
# S6-031 OS47 degree 9: S=(12)(34)(57)(6)(89), R=(123)(456)(789) (1-based)
S9 = P([(0,1),(2,3),(4,6),(7,8)], 9); R9 = P([(0,1,2),(3,4,5),(6,7,8)], 9)
G9 = PermutationGroup([S9, R9])
print("OS47 degree 9: |G| =", G9.order(), " primitive:", G9.is_primitive(), " SR:", (S9*R9).cycle_structure, " RS:", (R9*S9).cycle_structure)
# PSL2(F7) order 168, PSL2(F8)=? acting on 9 points: PGammaL(2,8) on P^1(F8) has order 1512, PSL2(8) order 504
print("9! =", 362880, " |A9| =", 181440)
