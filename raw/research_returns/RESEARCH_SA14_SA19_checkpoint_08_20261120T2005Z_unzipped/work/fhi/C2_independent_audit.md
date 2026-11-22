# Independent audit of BCE's C2 proof

Auditor: /root/fhi. Date: 20 November 2026.
Files reviewed: work/bce/C2_audit.md and the full C2.G argument in work/bce/section.tex (the author has since split section_C.tex).
Outcome: no mathematical gap found in the full completion-isomorphism argument under the stated excellent henselian noetherian hypotheses.

## Principal finite determinacy

For a noetherian a-adically complete R, a proper R-scheme W on which a acts regularly, and a^c H1(W,O)=0, let a^d kill the a-power torsion of the finite module H2(W,O). The multiplication exact sequence bounds H1(W_n,O) by an extension of H1(W,O)/a^n and H2(W,O)[a^n], so a^(c+d) annihilates it uniformly.

If L|W_n is trivial, the injection H1(W,L)/a^n → H1(W_n,L_n) gives a^e H1(W,L)=a^n H1(W,L), for e=c+d and n>e. Apply Nakayama to the finite module a^e H1(W,L), using a∈Jac(R), to obtain a^e H1(W,L)=0. In the connecting-map diagram for orders n and n−e, the vertical map on the kernel copy of L is multiplication by a^e. The obstruction to lifting the prescribed generator at order n−e is therefore zero. A lifted section generates everywhere: its non-generating locus has proper closed image avoiding V(a), whereas every nonempty closed subset of Spec(R) meets V(a).

This proves the claimed uniform loss of e in the prescribed trivialization, not merely triviality of L.

## Torsion removal

The coherent m-power-torsion ideal I is killed by one power m^c. Artin–Rees gives I∩m^N O_X=0 for N large. The displayed fibre product of O_X/I and O_X/m^N is therefore exact. The long cohomology sequence proves H1(X/I,O) has finite length because H2(I) is finite and killed by m^c. Milnor patching of invertible modules applies since one map to the intersection ring is surjective.

The absence of m-power torsion survives flat completion: for each n, the kernel of M→M^r given by finitely many generators of m^n remains zero after flat base change. If the quotient is empty, as in the Artinian-base boundary case, the patching statement still gives the result directly.

## Blowup and Stein factor

On the blowup, mO_X' is an invertible ideal defining an effective Cartier divisor. This is true chartwise because the Rees chart embeds in the localization by its chart generator; the generator is regular there. The universal property gives X'→Bl_m(Spec A).

For X'→h T→g Z, the invertible ideal mO_Z remains a regular ideal on T: tensor by that invertible sheaf and push forward the injection on O_X'. The equality h_*O_X'=O_T gives the required injection.

Off the closed point, Z is the original punctured base, X' is X, and g is finite. Precisely, g_*R1h_*O=R1f_*O=0 there. Finite pushforward is faithful, so R1h_*O vanishes there. Its coherence gives a uniform power of J=mO_T annihilating it. The J-power torsion of coherent R2h_*O is also killed by a uniform power. Flat completion of each affine chart preserves these bounds and regularity of the local generator. Hence the principal lemma applies with one uniform e.

## Formal descent to T and its finite cohomology

Formal functions in degree zero identifies h_*O on the formal completions with O_formalT, so ratios of local generators descend uniquely, as do their inverses. The injection O_T/J^r→h_*O_X'_r follows from the regular multiplication sequence and h_*O_X'=O_T. Therefore the descended cocycle is 1 modulo J^(N−e).

The scheme T is proper over A and finite over the punctured base. Consequently all its positive coherent cohomology groups are finite A-modules supported at the closed point, hence have finite length. In particular the use of H2 finite length is confined to T and does not add an assumption on X.

I independently opened Perling–Schroer, arXiv:1407.5443v2, Proposition 1.2 and the proof of Theorem 1.1, pp.4–5. Their argument gives the claimed finite determination for the structure sheaf. The printed general-vector-bundle theorem's E versus End(E) mismatch is irrelevant for E=O_T. One may first algebraize the formal line bundle on T by formal GAGA and then apply the theorem for E=O_T. Source: https://arxiv.org/pdf/1407.5443 .

## Conductor descent

For the finite Stein space Y=Spec_X pi_*O_X', the map O_X→O_Y is injective: its coherent kernel is supported on the closed fibre, hence consists of m-power torsion. The projection formula makes Pic(Y)→Pic(X') injective.

The conductor ideal contains m^k for some k, because O_Y/O_X is finite and supported on the closed fibre. It is also an ideal of O_Y, so both conductor schemes occur inside the corresponding kth thickenings. Their fibre-product ring recovers O_X.

I independently opened Stacks Lemma 30.20.4(3), tag 02OB. It states exactly that the image of H0(Y_N,O) in H0(Y_k,O) equals the image of global H0(Y,O) for N≥k+c, with uniform c. It does not require completeness for this assertion. Thus the comparison unit at order N lifts after restriction to order k. Its global lift is a unit because it is a unit on the closed fibre and the nonunit locus has proper closed image. Adjusting the Y trivialization yields agreement over the conductor and hence descends a trivialization to X.
Source: https://stacks.math.columbia.edu/tag/02OB .

## Approximation and uniformity

Line bundles and their isomorphisms descend under filtered limits of base rings by finite presentation. Excellence makes A→Â regular; Popescu supplies smooth A-algebras, and henselian approximation gives the required A-points congruent to a chosen formal point to any fixed order. This yields injectivity and density without assuming X/A flat.

The constants for the completed finite-determinacy statement depend only on the fixed blowups, Stein factors, coherent modules, and conductor. They do not depend on L. Density followed by finite determinacy therefore yields surjectivity; approximation supplies injectivity. The finite-length H1 hypothesis alone is preserved throughout the preliminary torsion removal.

Suggested exposition improvements communicated to the author: spell out g_*R1h=R1f over the punctured base, and optionally algebraize the formal M on T before applying the E=O_T finite-determinacy theorem.
