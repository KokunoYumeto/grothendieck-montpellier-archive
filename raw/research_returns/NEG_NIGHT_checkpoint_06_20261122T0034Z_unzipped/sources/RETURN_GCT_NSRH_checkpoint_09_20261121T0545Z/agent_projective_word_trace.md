# F45: a projective coefficient motive and Lefschetz structure for every rank-three word trace

Author/checker: `/root/rectangular_and_theta`. Date: 2026-11-21 UTC. The parent supplied the symmetric-square and invariant-projector route; all normalizations, identities, purity statements and scope restrictions below are proved and checked here. This is a realization of the actual scalar word-trace polynomial, not a new canonical basis or an action of the nonstandard algebra on these motive objects.

## 1. Exact input and statement

Let \(w\) be a nonempty word in the actual rank-three right generators \(P_1,P_2\), of length \(L\). Write \(2s\) for its cyclic number of transitions. Then \(0\le2s\le L\). Set

\[
\delta=v+v^{-1},\qquad D=\delta^2,
\]
\[
T_w(v)=\operatorname{Tr}_{M}(P_w)
=20D^L+16D^{L-s}+4D^{L-2s}(D-2)^{2s},
\tag{W1}
\]

as proved for the actual rank-64 action in F43. For the empty word the trace is 64 and may be realized by 64 copies of the unit object; all constructions below concern the nonempty case.

**Claim F45.** The Laurent polynomial (W1) is the character of an actual finite-dimensional \(SL_2\)-representation with only even weights. Its coefficients are symmetric and unimodal in the variable \(v^2\).

For every finite field \(k=\mathbf F_q\) and prime \(\ell\ne\operatorname{char}k\), an explicit algebraic rational projector on a product of projective lines gives a word-dependent rational Chow-motive realization. Its centered \(\ell\)-adic realization is a bounded Weil complex \(\mathcal K_w\) satisfying

\[
\sum_r(-1)^r\operatorname{Tr}(F^n\mid H^r(\mathcal K_w))
=T_w(q^{n/2})\qquad(n\ge1).
\tag{W2}
\]

Only even cohomological degrees occur, and

\[
H^{2r}(\mathcal K_w)\simeq\mathbf Q_\ell(-r)^{\oplus c_r},
\quad T_w(v)=\sum_{r=-L}^{L}c_rv^{2r}.
\tag{W3}
\]

Thus each cohomological degree is pure of its degree weight, and \(\mathcal K_w\) is **pure of weight zero in BBD's convention for complexes**. Its total ungraded Weil space is mixed, with distinct weights; purity of this complex is not a claim that every total eigenvalue has modulus one. There is an explicit invariant ample class giving hard Lefschetz on the projector image and hence on the centered direct sum.

## 2. An actual SL2 character: the symmetric-square repair

Let \(V\) be the standard two-dimensional characteristic-zero representation of \(SL_2\), with character \(\delta\). Put \(W=V^{\otimes2s}\), so \(\chi_W=\delta^{2s}=D^s\). For any representation with eigenvalues \(z_i\), elementary symmetric-square linear algebra gives

\[
2\chi_{\operatorname{Sym}^2W}
=\left(\sum_i z_i\right)^2+\sum_i z_i^2
=\chi_W(v)^2+\chi_W(v^2).
\]

Indeed the right side is twice \(\sum_{i\le j}z_iz_j\). In this case

\[
\chi_W(v^2)=(v^2+v^{-2})^{2s}=(D-2)^{2s},
\]
\[
\chi_{\operatorname{Sym}^2W}
=\tfrac12\bigl(D^{2s}+(D-2)^{2s}\bigr).
\tag{W4}
\]

Since \(L-2s\ge0\), all tensor exponents in

\[
\mathcal R_w=
(V^{\otimes2L})^{\oplus16}
\oplus(V^{\otimes2(L-s)})^{\oplus16}
\oplus\left(V^{\otimes(2L-4s)}\otimes
                 \operatorname{Sym}^2(V^{\otimes2s})\right)^{\oplus8}
\tag{W5}
\]

are nonnegative. Taking characters and using (W4) gives

\[
\chi_{\mathcal R_w}
=16D^L+16D^{L-s}
 +8D^{L-2s}\cdot\tfrac12\bigl(D^{2s}+(D-2)^{2s}\bigr)
=T_w.
\]

Every tensor power in (W5) has even total highest-weight parity. Hence all its irreducible \(SL_2\)-constituents have even highest weights. Their characters are the strings
\(v^{-2a}+v^{-2a+2}+\cdots+v^{2a}\), \(a\ge0\). A nonnegative sum of these centered nested strings has symmetric coefficients nondecreasing toward the center. This proves symmetry and unimodality in \(v^2\). No assertion of unimodality after inserting zeros at odd powers of \(v\) is made.

The case \(s=0\) is included: \(W=V^{\otimes0}\) is the unit representation, its symmetric square is again the unit, and (W5) has 40 copies of \(V^{\otimes2L}\), giving \(T_w=40D^L\).

## 3. The actual projective schemes and algebraic projector

For \(d\ge0\), put

\[
X_d=(\mathbf P^1_k)^{2d},\qquad
K_d=R\Gamma(X_{d,\bar k},\mathbf Q_\ell)(d)[2d].
\tag{W6}
\]

For \(d=0\), this is the rational point and unit complex. Every scheme \(X_d\) is smooth projective of dimension \(2d\). Its product line bundle \(\mathcal O(1,\ldots,1)\) is ample and defined over \(k\).

On \(X_L\), partition \(4s\) of its factors into two ordered blocks, each containing \(2s\) factors, and let \(\sigma\) exchange the blocks coordinate by coordinate. Leave the other \(2L-4s\) factors fixed. Thus \(\sigma\) is an actual \(k\)-defined involution, a product of \(2s\) transpositions. For \(s=0\), take the identity. Its graph defines an algebraic correspondence, and

\[
\pi_s=\tfrac12(\Delta_{X_L}+\Gamma_\sigma)
\quad\in CH^{2L}(X_L\times X_L)_\mathbf Q
\tag{W7}
\]

is an actual idempotent: the graph composition satisfies \(\Gamma_\sigma^2=\Delta_{X_L}\). The graph/transposed-graph convention is immaterial for this involution. In the pseudo-abelian category of rational Chow motives its image exists by the defining idempotent completion. On cohomology it is exactly the invariant projector \((1+\sigma^*)/2\).

This averaging uses rational coefficients. It does not require the characteristic of \(k\) to be different from two, since the coefficient field has characteristic zero and the involution and its graph are defined without forming a quotient variety. In particular no smoothness claim for a geometric quotient is used.

Define the centered Weil complex

\[
\mathcal K_w=K_L^{\oplus16}\oplus K_{L-s}^{\oplus16}
                    \oplus(\pi_s K_L)^{\oplus8}.
\tag{W8}
\]

Each summand comes from the displayed smooth projective scheme and an algebraic rational projector, followed by its specified twist and even cohomological shift. Equivalently, before the centering shifts, the rational Chow-motive expression is

\[
h(X_L)(L)^{\oplus16}\oplus h(X_{L-s})(L-s)^{\oplus16}
\oplus\operatorname{im}\bigl(\pi_s:h(X_L)(L)\to h(X_L)(L)\bigr)^{\oplus8},
\tag{W9}
\]

where the twist convention is the one whose realization is the usual \(\mathbf Q_\ell(d)\). The centered realization (W8) shifts the first and third components by \(2L\), and the second by \(2(L-s)\). These shifts are part of the complex construction; they are not an unmentioned common shift of (W9).

## 4. Exact trace, all finite extensions, and integral multiplicities

The projective-space computation gives
\(H^*(\mathbf P^1)=\mathbf Q_\ell\oplus\mathbf Q_\ell(-1)[-2]\).
The product cohomology has basis \(x_I=\prod_{i\in I}x_i\), with \(x_i^2=0\), degree \(2|I|\), and geometric Frobenius \(F^n\) eigenvalue \(Q^{|I|}\), where \(Q=q^n\). Its untwisted algebraic divisor classes are over \(k\), with the usual Tate factor accounting for the eigenvalue. These statements follow from the projective-bundle formula, and are also direct from the product cell decomposition.

There are no odd groups. The even shift in (W6) changes no Euler sign. Thus

\[
\operatorname{Tr}(F^n\mid K_d)
=Q^{-d}(1+Q)^{2d}
=D_n^d,
\quad D_n=Q+2+Q^{-1}.
\tag{W10}
\]

Here and below trace of a complex means its finite alternating trace. The displayed even-degree vanishing makes it equal to the sum of its cohomological traces.

The action of \(\sigma\) permutes the basis \(x_I\) without Koszul signs, because all factor classes have even degree. Its twisted Frobenius trace counts the \(\sigma\)-stable subsets: each fixed factor contributes \(1+Q\), and each transposed pair contributes \(1+Q^2\), since it must be included as a pair or excluded. Hence

\[
\operatorname{Tr}(\sigma F^n\mid K_L)
=Q^{-L}(1+Q)^{2L-4s}(1+Q^2)^{2s}
=D_n^{L-2s}(D_n-2)^{2s}.
\tag{W11}
\]

The projector commutes with Frobenius, and the trace on its image is its projector trace. Consequently

\[
\operatorname{Tr}(F^n\mid\pi_sK_L)
=\tfrac12\left[D_n^L+D_n^{L-2s}(D_n-2)^{2s}\right].
\tag{W12}
\]

Combine 16, 16 and 8 copies as in (W8): the first coefficient becomes \(16+8/2=20\), the alternating-block coefficient is \(8/2=4\), and the middle coefficient is 16. This is exactly (W1) at \(v=Q^{1/2}\), proving (W2) simultaneously for all extensions.

The denominator two is the genuine projector denominator, not a division of an unexplained count. In each degree the invariant subspace has an actual basis consisting of sums over \(\sigma\)-orbits of the subset basis. Its dimension is an integer. Frobenius is already a scalar on the whole degree, so that invariant subspace is a direct sum of the same Tate line, with no issue of arithmetic semisimplicity or hidden Jordan blocks.

## 5. Centered purity and the exact Lefschetz conclusion

For (W6), \(H^{2r}(K_d)=H^{2(r+d)}(X_d)(d)\). Thus it is

\[
\mathbf Q_\ell(-r)^{\oplus\binom{2d}{r+d}}
\quad(-d\le r\le d),
\tag{W13}
\]

and all odd groups vanish. Its weight is \(2r\), equal to its cohomological degree. The projector \(\pi_s\) preserves that property, since it acts degree by degree on these scalar Tate groups. Direct sums in (W8) then prove (W3).

At a point, BBD 5.1.8 says precisely that a complex is pure of weight zero when its degree-\(i\) cohomology is pure of weight \(i\). This applies here. The underlying ungraded Weil space has, for example, nonzero weight \(-2L\) and \(2L\) pieces when \(L\ge1\), so it is not a single-weight-zero representation. Centering is essential: without the shifts in (W6), the two differently twisted dimensions in (W8) can have different weights in the same absolute cohomological degree.

Let \(\eta_d=\sum_{i=1}^{2d}c_1(\mathcal O_i(1))\). This is the first Chern class of the ample line bundle \(\mathcal O(1,\ldots,1)\). It is \(\sigma\)-invariant on \(X_L\), so cup product commutes with \(\pi_s\). Hard Lefschetz on the smooth projective \(X_d\), applied to the constant intersection complex, gives

\[
\eta_d^{2r}:H^{-2r}(K_d)
          \xrightarrow{\sim}H^{2r}(K_d)(2r),\qquad r\ge0.
\tag{W14}
\]

The inverse of this isomorphism also commutes with \(\sigma\), so (W14) restricts to an isomorphism on the invariant summand. On the direct sum (W8), use the block diagonal operator with \(\eta_L\), \(\eta_{L-s}\), and the restriction of \(\eta_L\), respectively. These have the same centered degree convention, so (W14) holds for \(\mathcal K_w\) itself.

For \(r<0\), cup product \(H^{2r}\to H^{2r+2}(1)\) is injective: if it kills a vector then the further power giving the hard-Lefschetz isomorphism from degree \(2r\) to degree \(-2r\) also kills it. Thus \(c_r\le c_{r+1}\) below the center, while (W14) gives \(c_{-r}=c_r\). This supplies a geometric proof of the symmetry and unimodality already established by the actual \(SL_2\) character in §2.

The special case can also be checked entirely within the product cohomology ring: on each two-dimensional \(H^*(\mathbf P^1)\), multiplication by \(x\), the contraction sending \(x\) to 1, and the degree operator form the standard \(\mathfrak{sl}_2\) representation. Their diagonal tensor operators commute with factor permutations. The invariant subspace is therefore an actual \(\mathfrak{sl}_2\) subrepresentation; its raising operator is cup product by \(\eta_L\). This is the elementary instance of the cited hard-Lefschetz theorem, not a new general proof of that theorem.

## 6. Sharp scope of the repair

The construction realizes the actual all-extension scalar polynomial of each word by a finite, word-dependent projective coefficient motive with an actual projector and Lefschetz operator. It is more specific than assigning unrelated Tate lines to already computed coefficients. It nevertheless supplies no operators on these objects corresponding to both nonstandard generators, no specified compatibility with concatenation of different words, and no comparison with VIII's designated canonical basis or multiplication constants.

The dependence on the word is through \((L,s)\), just as the scalar trace depends only on those parameters. The total dimension of its realized trace object is

\[
T_w(1)=20\cdot4^L+20\cdot4^{L-s}.
\tag{W15}
\]

It varies with the word. This is consistent with F42's obstruction to retaining the all-extension retuning on one fixed finite common Weil space. No contradiction is obtained by comparing a variable trace object with a fixed-space obstruction.

The unimodality result also does not extend to all entries of the positive F43 action. Already the coefficient \(D-2=v^2+v^{-2}\) in \(N(D-2)\) has coefficient sequence \((1,0,1)\) in \(v^2\), which is not unimodal. Thus the actual whole-word trace has the Lefschetz repair proved here, while an entry-by-entry Lefschetz comparison in this chosen basis would require different information.

### A basis-independent obstruction to preserving the actual summand

There is a stronger trace obstruction, independent of the adapted basis. On the actual rank-two summand \(N(D-2)\), the matrices give

\[
\operatorname{Tr}_{N(D-2)}(P_1P_2)=(D-2)^2=v^4+2+v^{-4}.
\tag{W16}
\]

This is not the character of a finite-dimensional characteristic-zero \(SL_2\)-representation. In fact an irreducible constituent contributing weight 4 has highest weight at least 4 and also contributes weight 2. A representation with positive weight-4 multiplicity and zero weight-2 multiplicity cannot occur. Equivalently its coefficient sequence in \(v^2\) is \((1,0,2,0,1)\), which fails the centered weight-string condition.

For the full actual module, let \(e_2\) be the actual commutant projector onto its multiplicity-four \(N(D-2)\) sector. This projector belongs to the regular commutant from F43; it is not asserted to belong to the nonsplit regular right algebra. Then

\[
\operatorname{Tr}_M(e_2P_1P_2)=4(v^4+2+v^{-4}),
\tag{W17}
\]

which is still not an \(SL_2\)-character by the same weight-4/weight-2 test.

Suppose a matrix-kernel model assigned actual finite-dimensional \(SL_2\)-representations to every entry of kernels for \(P_1,P_2,e_2\), used ordinary direct sum and tensor product for composition, and its character matrices reproduced those actual operators in some basis. The diagonal sum of the composite kernel would be an actual \(SL_2\)-representation. Its character would be the matrix trace of the product, namely (W17), a contradiction. Trace is unchanged by a simultaneous change of basis, so this obstruction is basis independent. On the rank-two summand itself, (W16) already excludes such a model for both generators without an extra projector.

This precisely excludes simultaneous preservation of the specified summand in this positive \(SL_2\)-kernel framework. It does not exclude the word-dependent motive (W8), a model omitting that projector, virtual/signed kernels, or a more general category with different operations. The full-word Lefschetz repair therefore cannot be upgraded to the asserted summand-preserving model solely from its trace identities.

## 7. Primary inputs, check record, and Grothendieck dictionary

The classical projective-space and projective-bundle inputs were freshly inspected in Milne, *Lectures on Étale Cohomology*, version 2.21 (2013), Example 16.3 p.109 and Theorem 23.2 pp.139–140, primary https://www.jmilne.org/math/CourseNotes/LEC.pdf ; retrieval refs `turn294259598view0`–`turn294259598view2`. The formulas above additionally compute the action of the particular permutation directly on its algebraic cycle basis.

BBD, *Faisceaux pervers*, 5.1.8 pp.126–127, supplies the exact complex-weight convention; Theorem 5.4.10 p.144 supplies hard Lefschetz with a projective morphism, ample class and pure perverse input. Both full local contexts were inspected in `primary_sources/BBD.txt`, with the original PDF available alongside it. The applications here have a smooth projective product, its constant pure intersection complex, and the explicitly defined ample line bundle. The general primary theorems are cited inputs; their entire source proofs are not claimed to be independently reverified.

The graph correspondence in (W7) is an actual rational algebraic idempotent. The relevant motive exists by the stated rational Chow category's idempotent completion, not by an unproved standard conjecture. All cohomology of these projective products is split Tate, and the projector image is explicit on the subset basis.

In Grothendieck's language, the data consist of smooth projective schemes, algebraic correspondences, a rational projector, Tate twists, a centered realization and an invariant polarization. The invariant ample class supplies the hard-Lefschetz maps; purity alone was not used as a substitute for them. The quantum parameter remains a formal character variable until the exact substitution in (W2) is made. The construction identifies a scalar trace polynomial with a geometric coefficient object, without identifying the original nonstandard algebra action or its designated integral and canonical structures with these correspondences.

All equations (W1)–(W17), including boundary \(s=0\), every twist and shift, the factor-of-two normalization, the purity/ungraded-weight distinction, and the summand-preservation obstruction have been checked by the author. A fresh full review is requested before integration. Suggested event: `F45-PROJECTIVE-WORD-TRACE-AUTHOR-PROOF`.
