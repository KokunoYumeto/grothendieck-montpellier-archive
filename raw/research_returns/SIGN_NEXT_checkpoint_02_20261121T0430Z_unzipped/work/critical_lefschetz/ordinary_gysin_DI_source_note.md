# Ordinary upper Gysin with D(W) and I(W): exact cited refinement

This is a source/application note, not a new finding and not a re-proof of a known theorem.
Reviewer: GPT-6 Astra Pro; effort not exposed. Date: 21 November2026.

Use the notation of SN-C03 and SN-C04. Let X be smooth projective of dimensionn, Y a smooth hyperplane section, T=X x X of dimension2n with the Segre polarization, and W a smooth hyperplane section of T with its induced polarization L_W. Work with rational algebraic cycle classes in a Weil cohomology satisfying the relevant weak and strong Lefschetz theorems. In particular dim W=2n-1.

The ordinary upper critical Gysin condition is

    G^0(T,W): j_* Alg^n(W) = Alg^(n+1)(T).

The weighted condition in the corrected critical criterion is

    G_L^0(T,W): L_T j_* Alg^(n-1)(W) = Alg^(n+1)(T).

SN-C03 proves the exact equivalence

    G_L^0(T,W)  <=>  G^0(T,W) and A_0(W),

where A_0(W) is algebraic surjectivity of L_W:Alg^(n-1)(W) -> Alg^n(W), an isomorphism by strong Lefschetz.

Kleiman1968, Corollary3.9, printed p380, states that under the index conjecture I(W,L_W) and strong Lefschetz, A(W,L_W) and D(W) are equivalent. Thus adding D(W) and I(W,L_W) to ordinary upper Gysin supplies all of A(W), in particular the missing A_0(W), and hence supplies the weighted condition. Together with critical restriction R^0(T,W) and historical C_G(Y), this gives C_G(X) by the already cited Kleiman2.13(ii') and SN-C03.

There is a sharper one-way locator: Kleiman1968, Proposition3.6, printed pp379--380, already states that D(W) and strong Lefschetz imply A(W,L_W) for any polarization. The I hypothesis is not needed for this direction. Therefore the sufficient replacement may be written with D(W) alone, in addition to R^0(T,W), ordinary G^0(T,W), and C_G(Y). Under I, Corollary3.9 additionally gives the converse equivalence A(W)<=>D(W). These are applications of the exact published statements, not new proofs.

Here D(W) means equality of numerical and the chosen cohomological equivalence for algebraic cycles on the actual hyperplane W of X x X. It is not D(Y), and W is not Y x Y. The D hypothesis forces nondegeneracy of complementary algebraic intersection pairings; the I hypothesis asserts positivity on primitive algebraic classes. Purity of Frobenius eigenvalues and coefficient trace identities do not assert either of these cycle-theoretic statements. The trace/rigid-tensor countermodel SN-14 specifically shows that purity and the listed trace operations cannot formally produce a nondegenerate positive adjoint trace form. The formal model is not a geometric counterexample to D or I, and no claim is made that a conjectured geometric implication has been refuted.

The special class mu in Kleiman's proof is already produced from an algebraic middle correspondence T_X. Ordinary upper-Gysin lifting of that class does not by itself invert L_W on its high algebraic lift. The exact SN-C03 equivalence identifies that remaining inverse as A_0(W). Adding D(W) is a precise independent cycle hypothesis that supplies it; adding only trace-purity is not a substitute for that hypothesis.

Primary source checked in full for these applications: Kleiman, *Algebraic cycles and the Weil conjectures*, Propositions3.6 and3.8 and Corollary3.9, printed pp379--380, local `Kleiman1968.txt` and corresponding PDF.
