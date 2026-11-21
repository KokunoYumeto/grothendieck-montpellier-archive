# Prime-adjacent square blocks, specialization, and exact canonical-image semigroups

## G-013. Explicit determinant and padded-rectangle image ranges

Work over \(\mathbf Q\), with the normalized symmetric-tensor and canonical-map conventions of R-001, R-002, and R-008. For an integer \(a\ge2\), let
\[
\mathcal B_a=\{b\ge a: b\text{ is even and either }b-1\text{ or }b+1\text{ is an odd prime}\},
\qquad
\mathcal S_a=\left\{\sum_{b\in\mathcal B_a}n_b b:n_b\in\mathbf N,
\text{ finitely many }n_b\ne0\right\}.
\tag{P.1}
\]
Every \(B\in\mathcal S_a\) has a rational, explicitly constructed preimage of the determinant tensor \(I_{a,B}\) under the actual canonical map
\[
 h_{B,a}:\operatorname{Sym}^B(\operatorname{Sym}^a W)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^B W),\qquad \dim W=a.
\tag{P.2}
\]
In particular its rank on the target \((B^a)\) determinant component is one. For every integer \(s\ge0\), multiplication of the constructed preimage by \((e_1^a)^s\) gives a nonzero image of highest weight
\[
 (as+B,B^{a-1})
\quad\text{under}\quad h_{B+s,a}.
\tag{P.3}
\]
The target multiplicity of this weight is exactly one. These component statements hold in every ambient dimension at least \(a\), by the displayed subspace inclusion and highest-weight vector.

The set \(\mathcal S_a\) is cofinite among the even integers. More explicitly, for every odd prime \(p>a\),
\[
 B\text{ even},\qquad B\ge \frac{(p-1)(p-3)}2
 \quad\Longrightarrow\quad B\in\mathcal S_a.
\tag{P.4}
\]
This is an established range with an explicit preimage; no distributional assertion about primes is used in its proof. An ordinary prime search supplies a suitable \(p\).

For the ranks \(2\le a\le100\), the attached finite Apéry certificates determine the entire semigroup \(\mathcal S_a\), using only the widths \(a\le b\le4a\) in (P.1). The exact even conductor \(C_a\) means that every even \(B\ge C_a\) belongs to \(\mathcal S_a\), and, for \(C_a>0\), the even integer \(C_a-2\) does not. It describes precisely this constructed seed semigroup; a degree outside it may still have a nonzero canonical determinant block by another construction.

| Rank \(a\) | Exact even conductor \(C_a\), both prime-adjacent seeds | Prime-minus-one seeds alone | Known full-map surjectivity bound \((a-1)^2\) |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 1 |
| 3 | 4 | 4 | 4 |
| 4 | 4 | 4 | 9 |
| 5 | 6 | 16 | 16 |
| 6 | 6 | 16 | 25 |
| 7 | 8 | 16 | 36 |
| 8 | 8 | 16 | 49 |
| 9 | 10 | 16 | 64 |
| 10 | 10 | 16 | 81 |
| 12 | 12 | 28 | 121 |
| 16 | 28 | 28 | 225 |
| 20 | 36 | 56 | 361 |
| 26 | 52 | 64 | 625 |
| 32 | 58 | 92 | 961 |
| 50 | 96 | 116 | 2401 |
| 64 | 126 | 148 | 3969 |
| 100 | 190 | 196 | 9801 |

The last column is Sra III, Theorem 1.3, with its complete proof read in this run. It concerns every target component and is included only with that larger scope. The first columns certify the specified determinant and row-extended determinant components.

### 1. The exact square-to-smaller-rank pullback

Let \(b\) be one of the even square orders with \(c_b\ne0\), where R-002 defines the normalized scalar by
\[
 h_{b,b}(I_{b,b})=c_b I_{b,b}.
\tag{P.5}
\]
Take \(2\le a\le b\). Choose a decomposition
\[
 U^*=W^*\oplus\langle z_{a+1},\ldots,z_b\rangle,\qquad \dim U=b,
\]
and the actual linear multiplication map
\[
 j:\operatorname{Sym}^a W^*\longrightarrow\operatorname{Sym}^b U^*,
 \qquad F\longmapsto Fz_{a+1}\cdots z_b.
\tag{P.6}
\]
Let \(\Pi_a:(W^*)^a\to\operatorname{Sym}^a W^*\) and \(\Pi_b:(U^*)^b\to\operatorname{Sym}^b U^*\) multiply their ordered linear forms. The affine map \(\iota\) appends the fixed forms \(z_{a+1},\ldots,z_b\). Then
\[
 j\circ\Pi_a=\Pi_b\circ\iota.
\tag{P.7}
\]
Taking the degree-\(b\) coordinate pullbacks gives the commutative equality
\[
 h_{b,a}\circ\operatorname{Sym}^b(j^*)
 =\iota^*\circ h_{b,b}.
\tag{P.8}
\]
Here \(j^*\) is the dual linear map. The usual perfect characteristic-zero symmetric pairings identify it with a map \(\operatorname{Sym}^b U\to\operatorname{Sym}^a W\); its coefficients are determined by this duality. Thus all binomial factors of a monomial tensor basis are included by the defined map, without an implicit rescaling.

The normalized tensor \(I_{b,b}\) represents the polynomial \(\det_b(\ell_1,\ldots,\ell_b)^b\) on the ordered linear forms. Substituting the appended basis forms gives a block matrix with an identity complement, so
\[
 \iota^*(I_{b,b})=I_{a,b}.
\tag{P.9}
\]
Consequently the explicit rational vector
\[
 u_{a,b}=\operatorname{Sym}^b(j^*)\left(\frac{I_{b,b}}{c_b}\right)
 \quad\text{satisfies}\quad h_{b,a}(u_{a,b})=I_{a,b}.
\tag{P.10}
\]
The map \(j\) commutes with the block inclusion \(GL(W)\to GL(U)\); therefore \(u_{a,b}\) has determinant character \(\det_W^b\). Equation (P.10) also proves its nonvanishing directly.

For \(b=p-1\), Glynn's Theorem 3.2, and for \(b=p+1\), Drisko's Theorem 9, give \(c_b\ne0\), with the exact rational normalizations and prime-adic valuations proved in R-007. Applying (P.10) proves every seed in \(\mathcal B_a\). R-008 gives an additional, sharper congruence and an alternative source vector for the minus-one seeds. We use these known square results with their exact locators and make no priority claim for this specialization consequence.

### 2. Multiplication gives the specified preimages

R-008's map
\[
 \mu_a:\operatorname{Sym}(\operatorname{Sym}^a W)
 \longrightarrow \bigoplus_{d\ge0}\operatorname{Sym}^a(\operatorname{Sym}^d W)
\]
is a graded algebra morphism; its degree-\(d\) component is \(h_{d,a}\). Its target multiplication is componentwise multiplication in the \(a\) tensor factors. The determinant tensors satisfy
\[
 I_{a,b}I_{a,c}=I_{a,b+c}.
\tag{P.11}
\]
Evaluation on arbitrary \(a\) covectors proves this equality by the product \(\det^b\det^c=\det^{b+c}\), and these evaluations separate the symmetric tensors. Hence, for any specified expression \(B=\sum n_b b\),
\[
 u_{a,B}:=\prod_b u_{a,b}^{n_b}
 \quad\text{satisfies}\quad h_{B,a}(u_{a,B})=I_{a,B}.
\tag{P.12}
\]
No linear independence of different seed expressions is claimed or needed.

For (P.3), multiply (P.12) by \((e_1^a)^s\). Its image is
\[
 I_{a,B}\,(e_1^s)^{\otimes a},
\tag{P.13}
\]
a nonzero polynomial on the ordered covectors. It is a highest-weight vector of weight \((as+B,B^{a-1})\): the first factor has determinant character and the second is the power of the highest line. The refined balanced-weight realization T-002 identifies its target multiplicity with the invariant part of
\[
 \left(\det^B\otimes\operatorname{Sym}^{as}\mathbf Q^a\right)_{((B+s)^a)}.
\]
After removing the determinant factor, the only balanced monomial is \((x_1\cdots x_a)^s\), and its permutation character is \(\operatorname{sgn}^B=1\). Thus this multiplicity is exactly one. Appending zero weight coordinates under \(W\hookrightarrow V\) retains the same highest-weight vector, proving the ambient-dimension statement.

### 3. Cofiniteness and the explicit uniform range

For an odd prime \(p>a\), put \(g=(p-1)/2\). Both \(2g\) and \(2(g+1)\) lie in \(\mathcal B_a\). For each nonnegative \(N\), write \(r=N\bmod g\), \(0\le r<g\) (for \(g=1\), take \(r=0\)). The least nonnegative member of the semigroup \(\langle g,g+1\rangle\) with residue \(r\) is
\[
 w_r=r(g+1).
\tag{P.14}
\]
Indeed, in any expression \(ug+v(g+1)\), the second coefficient satisfies \(v\equiv r\pmod g\), and its smallest possible value is \(r\). Conversely \(w_r\) is represented. Every \(N\ge g(g-1)\) satisfies \(N\ge w_r\): the least integer at least \(g(g-1)\) in that residue is \(g(g-1)+r\), whose difference from \(w_r\) is \(g(g-1-r)\ge0\). Therefore
\[
 N=\frac{N-r(g+1)}g\,g+r(g+1)
\tag{P.15}
\]
has nonnegative integral coefficients. Multiplying by two gives (P.4), as well as an explicit two-factor construction in (P.12). The existence of arbitrarily large primes follows from Euclid's finite-product argument, so choosing \(p>a\) requires no unproved prime statement.

### 4. Exact finite semigroups by a residue graph

For a finite seed list \(2g_1,\ldots,2g_k\) with \(\gcd(g_1,\ldots,g_k)=1\), let \(g=\min g_i\). Make a directed graph on \(\mathbf Z/g\mathbf Z\), with an edge of weight \(g_i\) from \(r\) to \(r+g_i\). The residues generated by the \(g_i\) form the whole cyclic group: their subgroup has index the stated gcd, and the monoid they generate in a finite group is a group, since a positive multiple supplies each inverse. All edge weights are positive. Thus a shortest path from zero exists to every residue, and its length \(w_r\) is exactly the smallest nonnegative represented integer in that residue. The path itself records a seed expression.

For every integer \(N\ge0\), the exact membership equivalence is
\[
 N\in\langle g_1,\ldots,g_k\rangle
 \quad\Longleftrightarrow\quad N\ge w_{N\bmod g}.
\tag{P.16}
\]
The forward implication is minimality; the reverse adds copies of the generator \(g\). The greatest missing integer in residue \(r\) is \(w_r-g\), so the normalized conductor is
\[
 c=\max_r w_r-g+1.
\tag{P.17}
\]
For \(g=1\), this formula gives \(c=0\). These equalities also prove the shortest-path algorithm used in the attached code and explain precisely what its certificates certify.

The script `work/root/prime_semigroup.py` uses a direct sieve, enumerates every prime-adjacent width in \([a,4a]\), computes the shortest paths and their explicit integer witnesses, and then verifies all memberships through \(\max w_r+g+\max g_i\) by a separate Boolean recurrence \(D(N)=\bigvee_iD(N-g_i)\). It checks that all witnesses have the stated weights and residues. For every \(2\le a\le100\), it additionally verifies \(c\le2a\). Every omitted prime-adjacent width is greater than \(4a\); its half is therefore greater than \(2a\), and hence already belongs to the finite computed semigroup by (P.16). This proves that the finite list generates the entire \(\mathcal S_a\), without searching infinitely many primes. The same calculation and omission argument were checked for the minus-one lists displayed for comparison.

All 198 finite seed-set calculations passed. The complete data are in `PRIME_SEMIGROUP_RANGES.tsv` and `PRIME_SEMIGROUP_CERTIFICATES.json`, beside the reproducing script. The proof of the square specialization was independently checked through the commutative multiplication diagram by the rectangular agent. The whole proof and all computational checks receive separate events in the ledger.

### Scheme and representation-ring dictionary

The maps \(\Pi_a,\Pi_b,j,\iota\) are morphisms of affine schemes defined by integral coordinate polynomials. Equation (P.7) is equality of these actual scheme morphisms, and (P.8) is its contravariant equality on coordinate rings. The inverse scalar \(c_b^{-1}\) is taken over \(\mathbf Q\); after inverting its numerator and the finitely many symmetric-pairing denominators, the same preimage is defined over the resulting localization of \(\mathbf Z\). This identifies the base explicitly and makes no assertion of an integral inverse at an excluded prime. The nonzero image line is the coefficient of the Schur operation \(s_{(B^a)}\) in the image of the Chow coordinate morphism from G-003, equivalently the corresponding isotypic rank in \(K_0(\operatorname{Rep}_{\mathbf Q}GL_a)\). The tensor multiplication is the product in that representation algebra and in the graded scheme coordinate ring. The finite residue semigroup specifies a concrete finitely generated subalgebra of the canonical image through (P.12); it does not replace the entire coordinate ring by a numerical semigroup. The general SGA 3, SGA 6, EGA I, and FGA locators for these exact constructions are supplied in the dedicated dictionary part.
