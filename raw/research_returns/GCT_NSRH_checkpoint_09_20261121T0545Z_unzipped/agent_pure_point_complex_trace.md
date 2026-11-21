# Pure point-complex traces: a precise supplement to F57

Date: 2026-11-21 UTC. Author/checker: /root/gct_statements, GPT-6 Astra Pro; inherited reasoning effort is not separately exposed. This is a new elementary deduction from the point case of BBD's weight convention, not a new theorem attributed to BBD. The original BBD source and all displayed arguments were read in full. No formal proof assistant was used.

## 1. Statement and exact convention

Let q be a prime power, let ell not divide q, and choose an algebraic number lambda=sqrt(q)>0 under a specified complex embedding. Work over a finite ell-adic coefficient extension E containing a chosen ell-adic realization of lambda. The chosen square root, and not just the equation lambda^2=q, fixes the positive-real trace convention. Let

\[
 f(v)=\sum_{e\in\mathbb Z}c_e v^e\in\mathbb Z[v,v^{-1}],
 \qquad u_n=f(q^{n/2})=\sum_e c_e\lambda^{en}.
\]

For any integer w, the following are equivalent.

1. There is a bounded Weil complex K on Spec F_q, pure of the single weight w, whose Frobenius Euler traces are u_n for every sufficiently large positive n.
2. For every e, the integer (-1)^(e-w)c_e is nonnegative; equivalently

\[
                    (-1)^w f(-v)\in\mathbb N[v,v^{-1}].                 \tag{P1}
\]

If (P1) holds, the realizing complex can be chosen to give the equality for every positive n. If f is nonzero and the definition permits a real weight w, existence in fact forces w to be an integer, since a visible weight e must equal w+i for an integer cohomological degree i. We use BBD's original integral-weight convention throughout.

The inverse variable convention v=q^(-n/2) gives the same parity test, since -e-w and e-w have the same parity. The sufficiency is an arithmetic coefficient realization. It does not assert that an odd-weight line is a geometric half-Tate motive.

A useful consequence is that a nonzero f divisible by v-v^(-1) cannot satisfy (P1). Indeed f(-1)=0, whereas a nonzero polynomial (-1)^w f(-v) with nonnegative coefficients has strictly positive value at v=1. Equivalently, for the pure realization (P5), (-1)^w f(-1) is the total cohomology dimension. This applies to the nonzero signed/factored source coefficients with a positive exponent of that factor, provided the stated Laurent variable is the one assigned weight one. It calls for a mixed or normalized comparison of the raw coefficient, not a rejection of positivity of its stripped factor.

## 2. Proof of necessity, including hidden cancellation

BBD, Faisceaux pervers, §5.1.5, pp. 125–126, defines punctual purity with all complex conjugates and integer weights. In §5.1.8, pp. 126–127, the final smooth/lisse clause says that K is pure of weight w if and only if each H^i(K) is punctually pure of weight w+i. On Spec F_q every constructible sheaf is lisse, so that clause applies directly. We have reread the definition and its immediately surrounding context in the original source.

Let the eigenvalues of geometric Frobenius on H^i(K) be alpha, with algebraic multiplicity m_(i,alpha). Frobenius is invertible. Jordan blocks do not affect the power trace, and therefore

\[
 \sum_i(-1)^i\operatorname{Tr}(F^n;H^iK)
 =\sum_{i,\alpha}(-1)^i m_{i,\alpha}\alpha^n.                          \tag{P2}
\]

The sum is finite. Subtract the finite exponential expression for u_n and group equal nonzero roots. Distinct nonzero complex roots have linearly independent sequences alpha^n, even when equality is assumed only for all sufficiently large n: the equations at N,N+1,...,N+s-1 form an invertible Vandermonde matrix multiplied by the nonzero diagonal alpha^N. Consequently the grouped coefficient of lambda^e in (P2) equals c_e.

Purity gives |alpha|=q^((w+i)/2) for each embedding. In particular alpha=lambda^e can occur only when

\[
                              i=e-w.                                \tag{P3}
\]

Thus all contributions to the same root have the same cohomological parity. Their grouped coefficient is

\[
                      c_e=(-1)^{e-w}m_{e-w,\lambda^e},               \tag{P4}
\]

where the multiplicity is a nonnegative integer. This proves (P1).

The same argument excludes a hidden-cancellation escape. Any other root alpha has a fixed absolute value and hence can occur in at most one degree of a complex pure of one weight. Its contributions therefore cannot cancel between opposite parities. Equality with u_n forces such a root to be absent. This does not require arithmetic Frobenius semisimplicity.

## 3. Proof of sufficiency and arithmetic scope

Assume (P1) and put m_e=(-1)^(e-w)c_e. Let L_e be the one-dimensional E-Weil representation on which geometric Frobenius is lambda^e. All algebraic conjugates of lambda^e have absolute value q^(e/2), so L_e is pure of weight e. Define

\[
                   K=\bigoplus_e L_e[-(e-w)]^{\oplus m_e}.           \tag{P5}
\]

Its only contribution at the root lambda^e is in degree e-w. Its degree-i cohomology is therefore pure of weight w+i, so BBD §5.1.8 makes K pure of weight w. Its Euler trace is exactly u_n for all n.

These lines may also be taken as continuous unramified ell-adic representations: lambda^e is an ell-adic unit because ell does not divide q, and its cyclic subgroup has compact closure in E^times. The map from the infinite cyclic Weil group therefore extends to the procyclic Galois group, with the chosen geometric-Frobenius convention. This continuity observation is not needed for the finite Weil proof.

For even e=2k one can take the ordinary Tate line L_(2k)=Q_ell(-k), after coefficient extension. For odd e, the construction merely selects an arithmetic Weil line over E. It supplies no variety whose cohomology produces a geometric half-Tate object, nor any prescribed relation maps for an original nonstandard algebra action.

## 4. Application to the actual F57 word

Write the already proved actual word trace in its Laurent form:

\[
\begin{aligned}
 p((v+v^{-1})^2)={}&-(v^{18}+v^{-18})+2(v^{16}+v^{-16})
 +4(v^{14}+v^{-14})\\
 &+36(v^{12}+v^{-12})+67(v^{10}+v^{-10})+176(v^8+v^{-8})\\
 &+297(v^6+v^{-6})+476(v^4+v^{-4})+657(v^2+v^{-2})+668.
\end{aligned}                                                       \tag{P6}
\]

All nonzero exponents are even. Condition (P1) consequently requires every coefficient to have the same sign (-1)^w. The outer coefficients -1 and the coefficient 668 at v^0 contradict this for either parity of w.

**Therefore the F57 scalar sequence is not the Frobenius Euler trace of any bounded pure point complex of any single weight, regardless of its amplitude.** An overall cohomological shift, or a common Tate twist, cannot change that conclusion: shifts change the common parity and weight together, while Tate twists translate all exponents by an even integer. The previously displayed mixed Tate complex E_+ direct-sum E_-[-1] remains a valid realization. Its validity does not make it pure of a single weight.

This conclusion uses the existing exact F57 product certificate only to obtain (P6). It does not change the actual module scope: the negative P-word belongs to the additional full-algebra five-dimensional N# summand. It still does not exclude a P-only effective kernel construction on the two-row quotient, nor does it refute the sources' signed/factored positivity.

## 5. Application to the actual degeneration coefficient and its geometric repair

The Figure 21 coefficient in F58 is

\[
                   c_0(v)=(v-v^{-1})^2=v^2+v^{-2}-2.                 \tag{P7}
\]

Again all exponents are even and the signs are mixed. Hence c_0(q^(n/2)) cannot be the Euler trace of a bounded point complex pure of any single weight.

There is nevertheless ordinary geometric coefficient data giving this exact scalar sequence. The localization triangle for G_m inside A^1 gives

\[
 H_c^1((G_m)_{\overline{F}_q},Q_\ell)=Q_\ell,
 \qquad H_c^2((G_m)_{\overline{F}_q},Q_\ell)=Q_\ell(-1),             \tag{P8}
\]

with all other compactly supported cohomology zero. Indeed H_c^0(A^1)=H_c^1(A^1)=0, H_c^2(A^1)=Q_ell(-1), and the closed point has only H^0=Q_ell; the localization long exact sequence yields (P8). Kunneth and a Tate twist then give, for

\[
                 K_0=R\Gamma_c((G_m)^2_{\overline{F}_q},Q_\ell(1)),
\]

\[
 H^2K_0=Q_\ell(1),\qquad H^3K_0=Q_\ell^{\oplus2},
 \qquad H^4K_0=Q_\ell(-1),                                        \tag{P9}
\]

and no other cohomology. Its Euler trace is q^(-n)-2+q^n, precisely (P7) under the chosen variable rule. The same equality is q^(-n)(q^n-1)^2 by the point-count formula.

The coefficient sheaf Q_ell(1) is pure on the torus; its shift Q_ell(1)[2] is a pure perverse sheaf of weight zero on this smooth two-dimensional variety. The compact pushforward to the point is mixed, as (P9) shows. Consequently the pure-point-complex obstruction is **not** a no-geometry theorem, and is not a prohibition on pure coefficients on a nonproper source. This is exactly where the distinction between purity of a coefficient object before pushforward and purity of its point trace matters.

The compact-support long exact sequence is covered by Milne, Lectures on Etale Cohomology, Proposition 18.4(b), pp. 121–122; the compact-support Kunneth statement is Theorem 22.1 and Remark 22.3(b), pp. 135–136 (with the ell-adic passage immediately following). The duality/Tate normalization of affine compact cohomology uses Theorem 24.1(a),(b), p. 144. These exact primary contexts were reread locally for this supplement. Primary text: https://www.jmilne.org/math/CourseNotes/LEC.pdf.

## 6. Exact comparison assumptions

### 6.1. Pure matrix kernels with state potentials

There is a useful categorical consequence stronger than an assumption that every coefficient lies in one cohomological degree. Fix finitely many states a, integral state potentials t_a, and finitely many named generators i with integral weights w_i. Suppose the entry (a,b) of generator i is a bounded pure point complex K_(i,a,b) of weight

\[
                              w_i+t_b-t_a.                           \tag{P10}
\]

Use direct sums over intermediate states and the usual derived tensor product to compose these matrix kernels. Tensor products of pure point complexes of weights u and v are pure of weight u+v: the Kunneth decomposition in degree n is the direct sum of H^j tensor H^(n-j), each of weight u+j+v+n-j=u+v+n. A finite direct sum of objects of the same weight is pure of that weight.

For a word i_1,...,i_L, each path from a to b therefore has weight

\[
        \sum_{j=1}^L w_{i_j}+t_b-t_a,                               \tag{P11}
\]

because the potentials telescope. All paths contributing to the same entry have that weight. The closed-word trace object, the direct sum of the diagonal entries, is consequently pure of the single weight sum_j w_(i_j). Euler traces multiply under tensor product and add under direct sum, so a comparison identifying this word-trace object with the F57 scalar sequence contradicts (P1).

Thus no finite matrix-kernel realization of the specified N# word can simultaneously satisfy (P10) and the stated scalar Frobenius-trace comparison. This is an extra pure-word comparison hypothesis, not an axiom asserted in IV/VIII. Homogeneous summands of a mixed kernel may individually be pure without the entire entry satisfying (P10); that weaker condition is not excluded.

Likewise a proposed pushforward along a proper morphism of schemes of finite type over F_q, from a pure complex to the point, cannot realize the F57 sequence. BBD §§5.1.13–5.1.14, p. 128, gives preservation of the upper weight bound by f_! and of the lower weight bound by f_*; for a proper morphism they agree, so purity is preserved. The torus in §5 is nonproper, and its mixed compact pushforward is compatible with these statements.

### 6.2. Limits of the scalar comparison

The criterion concerns equality with the scalar Euler trace of Frobenius itself. A trace of an independently inserted endomorphism can have signed coefficients even on a pure vector space; no contradiction is asserted for that different comparison. Likewise a scalar mixed Tate or torus model does not automatically realize the designated GCT basis, the named word maps, multiplication, or specialization filtration.

The result narrows one prospective arithmetic bridge: if a canonical or nonstandard coefficient is identified with the Euler trace of a point complex claimed to be pure of a single weight, its Laurent coefficients must satisfy (P1). The signed/factored source conventions must be translated before applying this test; they are not an assertion of (P1).

## 7. Separate Grothendieck dictionary

The finite graded coefficient character f belongs to the representation Grothendieck group of a split torus. Its effective cone is N[v,v^-1], whereas a bounded complex gives an Euler class with signs. SGA 3, I, 4.7.2–3 and cote 90, scan 17 supply the action framework; SGA 6, V, §§2–3 and cote 133, scan 18 supply representation and lambda/sigma language. No lambda-ring structure is asserted for the noncommutative word algebra. The bounded coefficient complexes fit SGA 6, I, Definition 4.7, pp. 121–122, and Example 4.8, p. 122. Their Weil actions and the grading-to-weight rule are extra specified data. BBD §5.1.8, pp. 126–127, then imposes the cohomological weight shift that yields (P1). The torus example is an ordinary mixed compact pushforward, not an archival positivity theorem or a construction of the designated nonstandard category.

## 8. Check record and primary source

- Full proof read: all implications P1–P9 above reconstructed by the author; finite Vandermonde argument, shift signs, inverse variable convention and Tate normalization checked directly.
- Primary source read: the local original BBD PDF/text, §5.1.5, pp. 125–126, and the whole §5.1.8, pp. 126–127, including its smooth/lisse qualification; also §§5.1.11–5.1.14, pp. 127–128, for continuous point representations and the proper-pushforward deduction. Primary publication: https://www.numdam.org/item/AST_1982__100__1_0/.
- Additional exact operation locators read: Milne, Proposition 18.4(b), pp. 121–122; Theorem 22.1 and Remark 22.3(b), pp. 135–136; Theorem 24.1(a),(b), p. 144. These supply the compact-support sequence, Kunneth, and duality framework used in P8–P9.
- Existing exact certificate reused only for P6: verify_rank4_negative_trace.py, whose source matrices, product, word reversal and Laurent expansion were independently checked by the theta agent before this supplement.
- This record is not a claim of a new independent proof of BBD, the trace formula, Kunneth, or the original IV module-identification theorem.
