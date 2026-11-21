# Compact U(3) coverage of the everywhere-unramified GL(3) branch

**Finding K17-U3-COVERAGE.** Date: 2026-11-21 UTC. Author/checker: `/root/vandiver_k`, GPT-6 Astra Pro; effort not exposed. Status: complete deduction; independently audited by `/root/archive_kummer`, with the source-scope clarifications below incorporated. This note proves a representation-theoretic coverage statement. It does not certify the separate neighbor computation, the class number, a Hecke normalization, or a K-group vanishing.

## 1. Exact statement and supplied source interface

Put \(E=\mathbf Q(\sqrt{-3})\), \(O_E=\mathbf Z[\zeta_3]\), and

\[
G=U(E^3,h),\qquad h(x,y)=\sum_{i=1}^3\overline{x_i}y_i,
\qquad K=\prod_q\operatorname{Stab}_{G(\mathbf Q_q)}(O_E\otimes\mathbf Z_q)^3.
\]

Let \(\Pi\) be a conjugate-self-dual cuspidal automorphic representation of \(\mathrm{GL}_3(\mathbf A_E)\), in unitary normalization, such that:

1. every finite local component is unramified;
2. its archimedean Langlands parameter is
   \(\operatorname{diag}((z/\bar z)^6,1,(z/\bar z)^{-6})\).

Then a discrete automorphic representation \(\pi\) of \(G(\mathbf A_\mathbf Q)\) exists with stable base change \(\Pi\), with \(\pi_f^K\ne0\), and with \(\pi_\infty\) the irreducible compact representation of highest weight \((5,0,-5)\). Its occurrence has multiplicity one. In particular every such \(\Pi\) contributes its Hecke system to the algebraic modular-form space of this compact group, this full lattice level, and this coefficient representation (or its dual, which is isomorphic here).

The parent has independently checked that its `Adm3` branch for \(e=6,N=2\) has precisely these inputs: `KillsMu 2` forces all level characters to be trivial, the source Weil–Deligne conditions include zero monodromy and unramified inertia at every finite place, and the previously checked coefficient shift gives the archimedean parameter above. The present theorem is stated directly in terms of \(\Pi\), so those source-interface checks are not silently reproved here.

## 2. Proved global packet theorem, including its scope

Use Kaletha–Mínguez–Shin–White, *Endoscopic classification of representations: inner forms of unitary groups*, arXiv:1409.3731v3, local file `kmsw_inner_forms.pdf`.

The exact sufficient theorem is **Theorem 5.0.5, printed p.206**, together with its immediately preceding paragraph, not the unrestricted starred Theorem 1.7.1. The preceding paragraph explicitly verifies its two hypotheses for a generic global parameter and a pure inner twist. The theorem then gives the complete discrete multiplicity formula for that parameter. Its printed proof was read in full in this run. The foundational trace-formula arguments cited by that proof are used as published background, not independently reproved.

The group \(G\) is a pure inner form: **§0.3.3, printed p.18**, last paragraph, identifies precisely the pure inner forms as the unitary groups of Hermitian spaces over the field \(E\), as opposed to unitary groups over a nontrivial division algebra. Our defining algebra is \(M_3(E)\). At every finite place \(G\) is quasi-split; for odd dimension there is only one local unitary group up to isomorphism. This is also explicit in the local discussion on printed pp.17–18 and §1.6 p.79. At the real place it is compact.

For completeness the correct sign and the absence of a global parity obstruction are as follows.

* By **Proposition 1.3.1, p.67**, a conjugate-self-dual cuspidal \(\Pi\) belongs to exactly one simple generic formal parameter for a choice of sign \(\kappa\). By **Proposition 1.3.3, pp.70–71**, this formal parameter localizes at infinity with that same sign. The local parity criterion is in **§1.2.3, pp.59–60**, **Lemma 1.2.5, p.61**. Each of the three distinct archimedean characters in the displayed parameter is conjugate-orthogonal: its exponent difference is even. Distinct characters cannot pair with one another in the required invariant pairing, since each is already its own conjugate dual. Thus the archimedean parameter has positive parity only, forcing \(\kappa=1\) for dimension three. We may and do use the standard untwisted embedding \(\eta_1\).
* The global parameter is simple generic because \(\Pi\) is cuspidal and its Arthur \(\mathrm{SL}_2\) factor is trivial. Its reduced component group is trivial, by **§1.3.4–1.3.5, pp.69–70**, in particular the definition of \(\Psi_{\rm sim}\) in (1.3.7). Consequently the multiplicity condition in **§1.7, pp.88–89** places no restriction on the independently chosen local packet members. The product formula for the center there removes the apparent character of the unreduced group. Theorem 5.0.5 then gives multiplicity one for their restricted tensor product.

At infinity the parameter is discrete and relevant to the compact inner form. Compact highest weight \((5,0,-5)\) has Harish–Chandra parameter \((6,0,-6)\), obtained by adding \(\rho=(1,0,-1)\). Thus it is exactly the desired local packet member. This is the usual archimedean local Langlands description; Bellaïche–Chenevier, arXiv:math/0602340, Appendix A.11, Remark A.11.8, records the explicit distinct-character criterion and relevance for every real inner form. No conjectural global Langlands group from that appendix is used.

Before choosing local packet members, apply Shin, *Galois representations arising from some compact Shimura varieties*, Annals of Mathematics 173 (2011), **Theorem 1.2 and Corollary 1.3, pp.1647–1648**. The displayed infinity type is regular algebraic/cohomological, the representation is cuspidal and conjugate-self-dual, and the rank is odd. Thus every finite local component of \(\Pi\) is tempered; the extra slight-regularity hypothesis is only for even rank. Corollary 7.9 and its complete printed proof are on **p.1728**. Consequently each finite local parameter here is bounded, exactly the scope of KMSW Proposition 1.5.2(5). It remains only to choose a packet member fixed by the specified full lattice stabilizer at every finite place. The next sections do so.

## 3. Trivial central character of the GL(3) representation

The central character \(\omega_\Pi\) is unramified at all finite places, and its archimedean character is the product of the three displayed characters, hence is trivial. Therefore it factors through the ideal class group of \(E\). The Eisenstein integer ring is Euclidean, so this class group is trivial. Hence

\[
\omega_\Pi=1.
\]

This is useful at the ramified place: if \(s\) is the unramified Frobenius parameter of \(\Pi_{E_3}\), conjugate self-duality makes its eigenvalue multiset invariant under inversion. Since it has odd cardinality three and determinant one, it is necessarily

\[
\{a,1,a^{-1}\}.
\]

This remains true with repetitions, including \(\{-1,1,-1\}\). There is no unsupported assumption that \(a\) is distinct from \(1\) or \(-1\).

## 4. The ordinary finite places

At a split finite place, \(G(\mathbf Q_q)\simeq\mathrm{GL}_3(\mathbf Q_q)\); the lattice stabilizer is the usual maximal compact, and the target local representation itself supplies the fixed vector.

At an inert unramified finite place the standard selfdual lattice stabilizer is hyperspecial. The unramified GL(3) parameter has an unramified unitary-group extension, and its packet contains the hyperspecial spherical member. The precise packet assertion is **KMSW Proposition 1.5.2(5), p.79**, together with the usual unramified Satake correspondence. To check unramifiedness directly, inertia of \(\mathbf Q_q\) equals inertia of \(E_q\); the GL(3) restriction is trivial on this inertia. In the unramified extension of the parameter the inertia action is therefore the canonical trivial dual-group part. Uniqueness of the unitary-group extension up to conjugacy follows from **Lemma 1.2.5**. Thus this local packet is the localization of the same global parameter.

These arguments include the prime two, which is inert in \(E\). They do not use any assertion that two is a tame residue characteristic for a ramified unitary group.

## 5. The ramified prime three: an explicit principal-series proof

Use Adler–Lansky, *Depth-zero base change for ramified U(2,1)*, arXiv:0807.1528, local file `adler_lansky_ramified.pdf`. The global characteristic assumptions in **§4.1, p.10**, are characteristic zero and odd residual characteristic. The restrictions \(q>3\), \(q\ne7\) in their main Theorem 1.4 are used for separate supercuspidal finite-group calculations. They are not hypotheses of the principal-series statements used here.

Write \(F=\mathbf Q_3\), \(L=E_3\). In their coordinates the Borel Levi is

\[
M=\{\operatorname{diag}(\alpha,\beta,\bar\alpha^{-1}):
\alpha\in L^\times,\ \beta\in L^1\}.
\]

The standard selfdual lattice stabilizer is their vertex-\(y\) stabilizer. **§4.1, p.11**, identifies the ambient linear stabilizer with \(\mathrm{GL}_3(O_L)\). **§4.2.1, pp.11–12**, identifies the full unitary stabilizer's reductive quotient as
\(O_3(k)=SO_3(k)\times\{\pm1\}\). In particular one must not silently replace the full stabilizer by its connected parahoric. The argument below provides a vector fixed by the full stabilizer.

Choose an unramified character \(\chi:L^\times\to\mathbf C^\times\) whose Frobenius value is \(a\), with the local reciprocity convention chosen consistently with normalized induction. In the notation (4.4.1), set \(\lambda_1=\chi\), \(\lambda_2=1\). Thus

\[
\lambda(\operatorname{diag}(\alpha,\beta,\bar\alpha^{-1}))=\chi(\alpha).
\]

Its stable lift to the diagonal torus of \(\mathrm{GL}_3(L)\) has characters \((\chi,1,\chi^{-c})=(\chi,1,\chi^{-1})\), since \(\chi\) is unramified and \(L/F\) is ramified. This is the normalized principal series with parameter \(\{a,1,a^{-1}\}\).

By the finite temperedness just established, its three unramified Satake characters are unitary. Their ratios cannot be \(|\cdot|_L^{\pm1}\), so the lifted GL(3) principal series is irreducible and equals \(\Pi_L\). This also follows from genericity of local components of a cuspidal GL(3) representation.

The unitary induction \(I=\operatorname{Ind}_B^G\lambda\) is covered by the explicit reducibility list **§4.4, pp.14–15**:

* case (4.4PS–1), \(\chi=|\cdot|_L^{\pm1}\), is impossible because it would make the lifted GL(3) induction reducible;
* case (4.4PS–2), \(\chi|_{F^\times}=\omega_{L/F}|\cdot|_F^{\pm1}\), is impossible because the left side is unramified and \(\omega_{L/F}\) is ramified;
* the remaining possible reducibility is case (4.4PS–3), the nontrivial unramified quadratic \(\chi\), and the two constituents form a single L-packet.

The exact stable base-change assertions are **Proposition 6.1(1),(4), p.21**, and **Proposition 7.1(i),(iv), p.28**. Thus either \(I\) is irreducible and has stable base change \(\Pi_{E_3}\), or its two irreducible constituents form the packet whose stable base change is \(\Pi_{E_3}\). There is an additional source-scope check: their §4.5 assumes Hypothesis 1.5 globally. The particular principal-series assertions used here do not require that depth-preservation hypothesis. The printed proof of ramified Proposition 7.1 refers to the earlier unramified paper (published Proposition 4.1); in **arXiv:math/0601695, Proposition 5.1 and its complete proof, pp.19–20**, cases (i), (iii), and (iv) follow directly from Rogawski, Proposition 4.10.2 and the paragraph before Theorem 13.2.1, without a depth-preservation assumption or residue-size exclusion. We use only cases (i) and (iv).

Finally the full standard lattice stabilizer \(K_3\) is special maximal. Iwasawa decomposition \(G(F)=B(F)K_3\) and triviality of \(\lambda\) and of the modulus on \(B\cap K_3\) give

\[
\dim I^{K_3}=1.
\]

Taking invariants under a compact open subgroup in characteristic zero is exact, by averaging. Some irreducible constituent therefore has a nonzero \(K_3\)-fixed vector. By the preceding packet calculation that constituent belongs to the required local packet. This proves the full-stabilizer assertion, including its disconnected reduction, without any unverified passage from connected-parahoric invariants to full-stabilizer invariants.

Here is an explicit check that our lattice is their selfdual model, without invoking an unrecorded integral classification. Hensel's lemma gives \(a\in\mathbf Z_3^\times\) with \(a^2=-2\). Thus \(v=(1,1,a)\) is a primitive isotropic vector for the standard form. Choose \(w\) in the lattice with \(h(v,w)=1\); replacing it by \(w-\tfrac12h(w,w)v\) makes it isotropic. This gives an integral unimodular hyperbolic plane and an orthogonal unit line of norm \(d\). If \(B\in\mathrm{GL}_3(O_L)\) is the resulting basis matrix, determinants give \(-d=N_{L/F}(\det B)\). Scaling the last basis vector by \((\det B)^{-1}\) therefore makes its norm \(-1\). After ordering the basis as (isotropic vector, unit line, isotropic vector), the Gram matrix is exactly Adler–Lansky's \(\Phi=\left(\begin{smallmatrix}0&0&1\\0&-1&0\\1&0&0\end{smallmatrix}\right)\). Consequently the full standard lattice stabilizer is conjugate to their vertex-\(y\) stabilizer.

As an independent check on the lattice terminology, Pappas–Rapoport, arXiv:math/0702286, **§1.b.3(a), p.11**, identifies the selfdual lattice model \(I=\{0\}\) as a special maximal parahoric for the *similitude* group. Zhu, arXiv:1107.5762v3, **§6 pp.21–23** and **(7.1), p.24**, identifies both odd ramified special lattice vertices as very special and provides the ramified Satake correspondence. These latter statements are corroborating inputs; the proof above specifically handles the unitary full stabilizer and its central component by principal series.

## 6. Global assembly and consequence for the finite computation

Choose the compact member at infinity and the just-constructed spherical members at every finite place. Each belongs to the localization of the simple generic parameter for \(\Pi\), by local base-change uniqueness. All but finitely many are the prescribed unramified members, so their restricted tensor product belongs to the global packet. The reduced global component group is trivial. The proved generic, pure-inner-form case of KMSW Theorem 5.0.5 therefore places this tensor product in the discrete spectrum with multiplicity one.

Since \(G(\mathbf R)\) is compact and \(G\) is anisotropic modulo its center, its discrete automorphic forms of this fixed infinity type and level are precisely the corresponding algebraic modular forms. Thus the Hecke system of every \(\Pi\) in §1 occurs in the computed coefficient space at full lattice level, provided the separate calculation really exhausts that space.

No conclusion about its dimension, the neighbor eigenvalues, the congruence integer, or \(K_{12}(\mathbf Z)\) is part of this coverage lemma. Those are distinct exact-computation and source-translation checks owned by the parent.

## 7. Actual reading and check scope

Fresh complete readings used here: KMSW §0.3.3 final pure-inner paragraph; §1.2.3 parity definitions and Lemma1.2.5 statement/printed proof; Proposition1.3.1 and1.3.3 statements/printed proofs and intervening parameter definitions; §1.7 packet/multiplicity definitions; all of printed Theorem5.0.5 and its proof. Adler–Lansky §4.1, §4.2.1, principal-series part of §4.4, §6.1, §7.1 including the printed proof by reference. Zhu all of §6, start of §7 through (7.1). Pappas–Rapoport §1.b.3(a); Bellaïche–Chenevier Remark A.11.8, printed p.236. Additional complete reads for the audit clarification: Shin Theorem 1.2/Corollary 1.3 and Corollary 7.9 with its printed proof; Adler–Lansky unramified Proposition 5.1 with its entire printed proof. The theorem above was then reconstructed as a separate deduction and read in full after writing. The cited foundational global/local classification proofs are accepted source theorems; no claim to have reread all 220 KMSW pages or rerun a trace formula is made.

Primary URLs:

* https://arxiv.org/pdf/1409.3731
* https://arxiv.org/pdf/0807.1528
* https://arxiv.org/pdf/1107.5762
* https://arxiv.org/pdf/math/0702286
* https://arxiv.org/pdf/math/0602340


* https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p09-p.pdf
* https://arxiv.org/pdf/math/0601695
