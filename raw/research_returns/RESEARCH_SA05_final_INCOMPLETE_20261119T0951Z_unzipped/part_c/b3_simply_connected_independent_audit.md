# Independent audit of the simply connected surface reduction

Recorded 19 November 2026, 07:14 UTC, by /root/part_c. This is an independent audit for Part B; its final theorem is owned by /root/part_b.

## Mathematical check

Let $P$ be smooth, projective and geometrically connected over a finite field $k$ of characteristic $p$, with a map $f:P\to\mathbb P^1_k$, an extending zero section, generic fibre an abelian variety, and $H^1(P,\mathcal O_P)=0$. Choose a nonempty open $U$ on which $f$ is an abelian scheme. We work first over $\bar k$.

The exact homotopy sequence gives

$$
\pi_1(A_{\bar\eta})\longrightarrow\pi_1(P_U)
\longrightarrow\pi_1(U)\longrightarrow1.
$$

The zero section splits the second map. The map $\pi_1(P_U)\to\pi_1(P)$ is surjective because $P$ is normal and $P_U$ is dense. The image of the section subgroup dies in $\pi_1(P)$ because the section extends across $\mathbb P^1_{\bar k}$, whose étale fundamental group is trivial. Hence $\pi_1(A_{\bar\eta})\to\pi_1(P)$ is surjective. No injectivity assertion at the left end of the homotopy sequence is needed. The source is abelian, so $\pi_1(P)$ is abelian.

The vanishing of $H^1(\mathcal O_P)$ makes the tangent space at the identity of the Picard scheme zero. Its connected identity component is therefore trivial. Thus the group of geometric line bundles is the finitely generated Néron–Severi group. For every $n$ prime to $p$, Kummer gives

$$
\operatorname{Hom}(\pi_1(P),\mathbb Z/n\mathbb Z)
\simeq\operatorname{Pic}(P)[n]
$$

after choosing a primitive root of unity. The union of these character groups is finite, being the prime-to-$p$ torsion in the Néron–Severi group. Artin–Schreier gives $H^1_{\mathrm{et}}(P,\mathbb Z/p\mathbb Z)=0$. An abelian profinite group with these properties is finite of order prime to $p$: its pro-$p$ factor is zero, and its entire prime-to-$p$ character group is finite. Denote this geometric fundamental group by $N$.

The zero section supplies a $k$-rational point of $P$, so the arithmetic fundamental group is $N\rtimes G_k$. The image of $G_k$ is an open subgroup of index $|N|$. Its connected finite étale cover $P'\to P$ is defined over $k$ and has trivial geometric fundamental group. This subgroup need not be normal in the arithmetic fundamental group; normality is unnecessary. The whole zero section lifts because its arithmetic fundamental-group image is this subgroup. The geometric generic fibre of $P'\to\mathbb P^1$ is connected, since the geometric generic-fibre group surjects onto $N$.

The generic map $A'\to A$ is thus a connected finite étale cover with a chosen point over the origin. It has a unique abelian-variety structure making the map an isogeny. Over an algebraic closure this is the Serre–Lang argument in SGA1 XI §2; uniqueness descends the structure. In the present prime-to-$p$ case one can also dominate the pointed cover by multiplication by a prime-to-$p$ integer and descend its kernel quotient. Its degree is $|N|$, hence prime to $p$.

An isogeny of prime-to-$p$ degree has a quasi-inverse whose two compositions are multiplication by an integer prime to $p$. Extending both maps to the Néron models and differentiating shows that their Lie and invariant-differential maps are inverse after division by that integer. The corresponding Hodge bundles are isomorphic. This last step was independently checked by Part B and root against Yuan's notation.

Root checked that Yuan's Theorem 4.5 rebuilds a regular projective model $P''$ of the same generic abelian variety, without a forced additional Frobenius base change. Thus $P'$ and $P''$ are smooth proper varieties with the same function field. Their geometric fundamental groups agree by smooth-proper birational invariance, so $\pi_1(P''_{\bar k})=1$. Yuan's construction also restores $H^1(P'',\mathcal O)=0$ using the ample Hodge bundle. Smooth ample cuts from ambient dimension at least three preserve the geometric fundamental group; cutting down to a surface preserves simple connectedness. The separate coherent-cohomology and adjunction arguments must still be retained to preserve $H^1(\mathcal O)=0$ and the prescribed positivity of the canonical bundle.

## Exact primary sources opened and read

- **SGA1**, corrected SMF edition, arXiv:math/0206203v2, https://arxiv.org/pdf/math/0206203. Exposé X, Theorem 1.3 and its proof, pp. 202–203, and Corollary 1.4, p. 203, give the homotopy sequence. Corollaries 1.7–1.8, pp. 204–205, give the proper product formula and geometric extension invariance. We read the relevant complete arguments.
- **SGA1**, Exposé X, Corollary 3.3 and its complete proof, pp. 213–214, and Corollary 3.4, p. 214, give purity and birational invariance for regular proper varieties. The proof extends covers from the codimension-two complement by normalization and purity. All the displayed steps were read.
- **SGA1**, Exposé XI, §2, pp. 221–222, including the complete argument preceding Theorem 2.1, proves that a pointed connected étale cover of an abelian variety is an isogeny and that its geometric fundamental group is abelian. The proof uses the product formula and primitive torsor classes; its uniqueness statement permits descent.
- **SGA1**, Exposé XI, Proposition 6.1, Proposition 6.4 and Corollary 6.6, pp. 233–235, give the exact Kummer calculation. Proposition 6.7, Proposition 6.8 and Corollary 6.10, pp. 236–237, give the Artin–Schreier calculation. Complete relevant arguments were read.
- **SGA2**, corrected edition, arXiv:math/0511279, https://arxiv.org/pdf/math/0511279. Exposé XII, Corollary 3.5, corrected p. 120 (original p. 152), states the ample-divisor fundamental-group isomorphism in the regular ambient case of dimension at least three. We read its complete statement and proof, and the preceding Corollary 3.4 argument on pp. 119–120. We did not claim to re-prove the entire formal-algebraization theorem on which that argument rests.
- **Stacks Project**, Lemma 58.10.7, Tag 0BQI, https://stacks.math.columbia.edu/tag/0BQI. The complete proof was opened and read: for a geometrically unibranch irreducible scheme, every nonempty open induces a surjection on fundamental groups.

The local archives are part_c/sources/sga1_2004.pdf and sga2_2005.pdf, with extracted text and the SHA256 manifest b3_pi1_source_manifest.json. Page numbers above are the corrected-edition printed numbers, except where the original page is explicitly stated.

## Audit outcome and scope

No mathematical obstruction was found in the proposed refinement. The conclusion depends on the actual Yuan same-function-field reconstruction and prime-to-$p$ Hodge-bundle preservation, separately audited by root and Part B. It does not follow from $H^1(\mathcal O)=0$ alone for an arbitrary variety: the abelian-fibration argument is what makes the full fundamental group abelian before Kummer and Artin–Schreier are used.

### Full written-owner proof checked, 07:18 UTC

We read every line of part_b/b3_simply_connected_pending.md and passed its complete proof. In particular, the generic fibre of the integral finite cover is integral; the chosen rational point makes its finite field of global functions the original function field, and proper smooth base change for degree-zero cohomology gives geometric connectedness. The note correctly does not infer coherent $H^1$ vanishing for the finite étale cover itself; it uses the prime-to-$p$ isogeny and Yuan's same-generic-fibre reconstruction to restore it. Multiplying a two-dimensional model by $\mathbb P^1$ preserves its geometric fundamental group, coherent $H^1$, and the generic Picard-zero factor before the final surface cut. A proposed bibliographic correction from Theorem 1.3 to Proposition 1.3 was mistaken: Part B pointed to the exact primary header, and we rechecked it. The correct label is SGA1 X Theorem 1.3; B’s original citation was right. This correction does not affect the proof.
