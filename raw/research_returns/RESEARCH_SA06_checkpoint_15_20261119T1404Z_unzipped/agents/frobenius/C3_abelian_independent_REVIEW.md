# Independent audit of C.3h

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius. Date: 19 November 2026, 04:59 UTC.

We read research/sections/C3_abelian.tex and reopened Beauville (2010), *The action of SL2 on abelian varieties*, primary published PDF https://math.univ-cotedazur.fr/u/beauvill/pubs/SLA-rms.pdf. We checked the adequate-equivalence footnote 1 on p. 254, Theorem 4.2 on p. 260, Propositions 5.2 and 5.5 on p. 261, and Proposition 5.11 with its proof on p. 262.

The two exact graded criteria pass the independent proof check. Every operator is an algebraic correspondence, so both the quotient modulo algebraic equivalence and the invariant algebraically trivial subgroup inherit the locally finite rational SL2 representation. Local finiteness and semisimplicity concern representations over \(\mathbf Q\); they impose no characteristic-zero requirement on the algebraically closed ground field and no semisimplicity assertion about a category of cycles.

A string beginning in codimension \(a\) and Beauville index \(s\) has length \(g+s-2a\). The term in codimension \(r\) is killed by \(\theta^{g-2r}\) exactly when \(a>r+s\), and by \(\theta^{g-2r+1}\) exactly when \(a>r+s-1\). The first inequality is impossible for \(s\ge0\), and the second for \(s\ge1\). Conversely, the lowest term of every string with negative index, respectively nonpositive index, is in an allowed source degree and is killed by the relevant power. These observations prove both directions, including the assertion about all degrees on the right.

The translation reduction to a symmetric rational ample class is valid over every algebraically closed field, including characteristic two. After clearing a denominator, the polarization isogeny is surjective on geometric points, and multiplication on \(\operatorname{Pic}^0(k)\) is surjective. Pullback by the resulting translation conjugates the two multiplication maps. On the quotient modulo algebraic equivalence, translation also acts as the identity.

For \(g=5\), the Fourier transform sends \(B^2_{(s)}\) to \(B^{3+s}_{(s)}\). At \(s\le-2\) this is a negative-index divisor class, a codimension-zero class, or a nonexistent codimension, hence zero. The remaining \(s=-1\) group is primitive because its lowering image lies in \(B^1_{(-1)}=0\), and its string length is zero. Positive-index strings and the index-zero strings inject under the displayed single power. This gives the exact kernel \(B^2_{(-1)}\).

For \(g=4\), the Fourier transform similarly eliminates every negative-index component of \(J^2\). Since \(J^1_{(0)}=0\), the component \(J^2_{(0)}\) is primitive of length zero, and all positive-index strings inject. Thus the second displayed kernel is exactly \(J^2_{(0)}\).

The fragment correctly leaves both remaining groups unproved. Adding \(g\ge1\) is appropriate for the explicit operator containing \((g-1)!\); the dimension-zero case is vacuous.
