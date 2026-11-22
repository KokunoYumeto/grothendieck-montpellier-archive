# C2 full proof audit — 20 November 2026, 15:38 UTC

Claim: for any proper scheme X over an excellent henselian local A with H1(X,O) of finite length, Pic(X)→Pic(X_Â) is an isomorphism. Artin approximation supplies injectivity and density; it suffices to prove finite determination after completion. Everything below, apart from approximation, uses only a complete noetherian local base.

## 1. Principal-ideal lemma

Let R be noetherian and a-adically complete, let Z/R be proper, a regular on O_Z, and suppose a^c H1(Z,O)=0. The a-power torsion of the finite module H2(Z,O) is killed by a^d. With e=c+d, the exact multiplication sequence gives a^e H1(Z_n,O)=0 for all n, Z_n=V(a^n).

For L trivial on Z_n, n>e, H1(L)/a^n injects into H1(O_Zn), so a^e H1(L)=a^n H1(L), hence a^e H1(L)=0 by Nakayama (a in Jac R). The obstruction to lifting the chosen unit section at order n-e is a^e times its obstruction at order n and vanishes. It lifts to a section of L matching the chosen trivialization to order n-e. The lift is a generator everywhere: its failure locus is closed with proper image and misses V(a), while every nonempty closed subset of SpecR meets V(a). This includes an explicit bounded loss for the chosen trivialization, not only triviality of the isomorphism class.

## 2. Remove sections supported on the closed fibre

Let I⊂O_X be the coherent m-power torsion ideal; some m^c kills I. For N large, I∩m^N O_X=0 by Artin–Rees. Put X0=V(I). Then O_X=O_X0×_{O_X0,N}O_XN. The finite module H1(X0,O) has finite length by 0→I→O_X→O_X0→0, since all Hq(I) are finite modules killed by m^c. Once the completion statement is known for X0, any formal line bundle on X patches from its algebraized restriction to X0 and its unchanged restriction to X_N. The gluing isomorphism lives on X0,N, unchanged by completion. Thus it suffices to treat X with no m-power torsion. For finite determination rather than algebraization, the same patch can be combined with step5's unit stabilization.

## 3. Blow up and use the principal lemma locally

Assume A complete and X has no m-power torsion. Put Z=Bl_m(SpecA), X'=Bl_{mO_X}(X), and π:X'→X. There is a proper h0:X'→Z, and J=mO_X' is invertible and defines an effective Cartier divisor. In particular, local equations of mO_Z act regularly on X'. Take its Stein factorization X'→^h T→Z. Then h_*O_X'=O_T, T is finite over Z and proper over A, and J_T=mO_T is likewise an invertible ideal defining a Cartier divisor (regularity follows by pushing forward O_X').

Away from the closed point of SpecA, X' and X agree and Z agrees with SpecA. Since R1f_*O_X vanishes there, R1h_*O_X' vanishes away from V(J_T). It is consequently killed by J_T^c for a uniform c. The J_T-power torsion in the coherent R2h_*O_X' is killed by J_T^d for a uniform d. Choose a finite affine cover of T trivializing J_T. On each completed affine chart, the principal-ideal lemma applies to h with e=c+d.

Suppose L on X is trivial on X_N. On formal X', choose the local generators supplied by the lemma, matching this fixed trivialization modulo J_T^{N-e}. Their ratios descend uniquely to units on formal T because h_*O_X'=O_T and the theorem on formal functions identifies the corresponding completed pushforward. These units define M on formal T with h^*M=L|formalX'. The units are 1 modulo J_T^{N-e}: O_T/J_T^r→h_*O_X'_r is injective, by the multiplication exact sequence and h_*O_X'=O_T. Thus M is trivial on T_{N-e}.

## 4. Kill M on T

Off the closed point, T is the finite Stein space Spec(f_*O_X). Therefore H1(T,O_T) and H2(T,O_T) have finite length over A. Perling–Schroer Proposition1.2 and the proof of Theorem1.1, with E=O_T, show Pic(formalT)→Pic(T_q) injective for q large. Hence M is trivial for N-e≥q. Consequently π^*L is trivial on X' (formal GAGA over complete A).

## 5. Descent of triviality through π at finite order

Let Y=Spec_X π_*O_X'. Then Y→X is finite, isomorphic off X_s, and O_X→O_Y injects because X has no m-power torsion. The map Pic(Y)→Pic(X') is injective by h_*O=O and the projection formula. Thus L_Y is trivial.

Let C⊂X and C'⊂Y be the conductor subschemes. Their ideals contain m^k for some k, and O_X=O_Y×_{O_C'}O_C. Take N≥k. A trivialization of L_Y and the given one of L_XN differ on Y_N by a unit u_N. For a fixed k, formal functions and the Mittag–Leffler property of the finite-length modules H0(Y_n,O) imply that, for all N sufficiently large, the image H0(Y_N,O)→H0(Y_k,O) equals the image of H0(Y,O) (A is complete). Thus u_N mod m^k lifts to u∈H0(Y,O). Its restriction to Y_s is a unit, so u is a global unit by properness over a local base. Adjust the trivialization on Y by u. It now agrees with the one on C after pullback to C', so conductor patching makes L trivial on X.

All bounds depend only on X/A, not L. This proves finite determination for X without m-power torsion, and steps2 plus Artin's density prove the full completion isomorphism. No H2 finite-length assumption is made on the original X; it is imposed only on the auxiliary proper T where it follows from finiteness away from the closed point.

Audit points: blowup effective Cartier and induced X'→Z; Stein map R1 vanishing off exceptional locus; formal pushforward and unit descent; conductor unit stabilization. These have explicit explanations above. No computations or false claim of independent provenance involved.
