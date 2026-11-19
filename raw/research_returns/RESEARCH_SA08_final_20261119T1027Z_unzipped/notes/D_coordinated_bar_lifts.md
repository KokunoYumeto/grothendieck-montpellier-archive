# C28: coordinated absolute finite bar lifts

2026-11-19, GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras.

The full theorem and proof are in `sections/D_coordinated_bar_lifts.tex`.
The coefficient ring is arbitrary. The original form degree q is odd
and positive; P has projective normalized terms. Each target row
A_j^(w,q) is acyclic. Through a finite arity M, assume vertical exactness
of A_j^(mw,*) through m(q+1), for every 2<=m<=M. No higher horizontal
acyclicity is needed.

The key construction is explicit. For the finite product of the target
rows, choose free covers F_n of the normalized cycles and primitives
of their basis vectors. The sum of identity disks D_(n+1)(F_n) maps
surjectively to the target complex and is contractible. Its kernel is
acyclic. The parameter map lifts degree by degree: lift a graded map,
then lift its cycle-valued differential defect to the acyclic kernel
using projectivity of N_n(P). This gives one contractible free
simplicial parameter L and a map P->L for all targets.

The arity-m PD indecomposable terms Q_m^i(L) are reduced functors of L,
so they preserve its simplicial contraction. C24 gives degreewise
freeness; normalized projectivity plus contractibility makes them
projective objects in sMod, rather than merely termwise projective
normalized complexes. Therefore the ordinary cochain extension
obstruction is computed by the bounded Hom complex. Finite vertical
exactness reduces it to Hom(Q_m(L),constant k), which is identically
zero because each Q_m^i(L) is horizontally acyclic. Induction gives
compatible finite partial PD maps and they pull back to P.

This construction need not retain arbitrary earlier higher-arity
primitives. C27 does retain them for K(Z,2) under its distinct bounds.
Neither result gives a preassigned boundary-relative extension or
one weight satisfying all eventual bounds. The first unsolved
global use is still the source-side boundary map needed by C24's
relative pushout: the source row contains the horizontal class
which one is trying to kill and is not acyclic there.
