# I7: complete-ring residual columns are actually exact, and strict above the first arrow

Full proof is in I_complete_columns.tex.

For a complete regular local A and p≠m, Ext_A^j(E_p,A)=0 for every j. Indeed A=Hom_A(E_m,E_m), so tensor–Hom adjunction with an arbitrary projective resolution gives Ext_A^j(E_p,A)=Hom_A(Tor_j(E_p,E_m),E_m). Choose u∈m\p. The source is A_u-local and (E_m)_u=0, so all these Tor groups vanish. Therefore Hom_A(E_p,K_A) is exact as an abstract complex, strengthening I6's closed-image statement in the complete case.

For degree j>ht(p)+1, the map onto cycles is open in the finite topology. Given finite inputs inside N=Ae, take v∉p annihilating the finite module Ext_A^(j−1)(A/Ann(e),A), and enlarge inputs to N'=A(e/v). A cycle f vanishing on N' has a global preimage g by exactness. Its restriction g|N' is a cycle, and restriction to N multiplies that class by v, hence kills it. An injective extension of a local boundary corrects g to vanish on N. Thus the image of Ann(N) contains the open subgroup Ann(N')∩cycles.

The first-arrow topology is deliberately excluded from this strictness assertion. The proof also does not settle simultaneous families of intermediate primes or construct the full continuous universal map in every dimension.
