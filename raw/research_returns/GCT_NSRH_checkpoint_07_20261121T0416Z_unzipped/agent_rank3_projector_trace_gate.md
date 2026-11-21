# F26 proposal: the actual normalized projector trace is not a finite Weil trace family

Author/checker: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 Europe/Berlin. This is an explicit deduction from the actual r=3 tensor action, with a general elementary rational-function lemma. It is not asserted as a requirement imposed by the GCT sources: it tests a precisely stated possible grading-to-Frobenius comparison and proves that this particular comparison fails.

## 1. Actual nonstandard projector invariant

Use the consistent GCT IV normalization from §3.1 and equation (93):

\[
\delta=v+v^{-1},\quad D=\delta^2,\quad
P_i=c_i\otimes c_i+(c_i-\delta)\otimes(c_i-\delta).
\]

The quadratic relation is `P_i²=DP_i`, so

\[
e_i=P_i/D
\]

is an actual idempotent over the localization used in the rank-three reports. This is an algebraic idempotent, not yet an idempotent sheaf functor.

Let `M=(V⊗W)^{⊗3}` for `dim V=dim W=2`, the actual 64-dimensional tensor module. The explicit regular changes of basis in `agent_rank3_tensor_geometry.md` prove

\[
M=\epsilon_+^{20}\oplus\epsilon_-^4\oplus N(\delta)^{16}\oplus N(D-2)^4.
\tag{P1}
\]

For the source's row module `N(a)`, equation (110) gives

\[
P_1=\begin{pmatrix}D&0\\a&0\end{pmatrix},\qquad
P_2=\begin{pmatrix}0&a\\0&D\end{pmatrix}.
\]

Consequently `Tr_N(a)(e_1e_2)=a²/D²`. On `epsilon_+` the trace is one and on `epsilon_-` it is zero. Applying (P1),

\[
\begin{aligned}
\operatorname{Tr}_{M}(e_1e_2)
&=20+16\frac1D+4\frac{(D-2)^2}{D^2}\\
&=24+\frac{16}{D^2}.
\end{aligned}
\tag{P2}
\]

This is a basis-independent ordinary matrix trace of a word in the two actual normalized projectors. It does not depend on an artificial external basis or a guessed canonical-basis expansion. At `v=1`, it equals 25; at positive real `v→∞`, it tends to 24. For the unnormalized generators,

\[
\operatorname{Tr}_{M}(P_1P_2)=24D^2+16,
\tag{P3}
\]

a Laurent polynomial. The difference between (P2) and (P3) is essential.

## 2. Explicit non-power-sum theorem

Fix a real `q>1` (a prime power is the arithmetic case). The two substitutions `v=q^(n/2)` and `v=q^(−n/2)` give the same value of `D` and hence the same sequence

\[
h_n=24+\frac{16}{(q^n+2+q^{-n})^2}
=24+16\frac{q^{-2n}}{(1+q^{-n})^4}.
\tag{P4}
\]

**Claim P-A.** The sequence `(h_n)` is not a finite exponential-polynomial sequence, even eventually. In particular it cannot be written

\[
h_n=\sum_{j=1}^s p_j(n)\alpha_j^n
\tag{P5}
\]

for all sufficiently large integers `n`, with finite `s`, arbitrary complex polynomials `p_j`, and arbitrary nonzero complex `alpha_j`. Constant complex coefficients, signed Euler multiplicities, and real coefficients are special cases of the excluded form.

**Full proof.** Put `rho=q^(−1)∈(0,1)`. The binomial expansion, absolutely convergent for every positive `n`, gives

\[
h_n=24+16\sum_{j\ge0}(-1)^j\binom{j+3}{3}\rho^{(j+2)n}.
\tag{P6}
\]

For `|T|<1`, absolute convergence permits interchange of the two sums: the absolute sum is bounded by

\[
\sum_{j\ge0}\binom{j+3}{3}
\frac{\rho^{j+2}|T|}{1-\rho^{j+2}|T|}<\infty.
\]

Thus the ordinary generating series has the representation

\[
H(T)=\sum_{n\ge1}h_nT^n
=\frac{24T}{1-T}
+16\sum_{j\ge0}(-1)^j\binom{j+3}{3}
\frac{\rho^{j+2}T}{1-\rho^{j+2}T}.
\tag{P7}
\]

The infinite series on the right converges **normally on every compact subset of the complex plane avoiding the points `T=rho^(−j−2)`**. Indeed, if `|T|≤L`, then for all sufficiently large `j` one has `rho^(j+2)L≤1/2`; the absolute value of that tail term is bounded by

\[
2\binom{j+3}{3}\rho^{j+2}L,
\]

whose sum converges. Only finitely many earlier terms remain, and they are holomorphic on a compact set avoiding their poles. The same argument on a small closed disk around one excluded point, with that single term removed, shows that the rest of the series is holomorphic there.

At `T_j=rho^(−j−2)=q^(j+2)`, the `j`th summand has a nonzero simple-pole coefficient; all other summands and `24T/(1−T)` are holomorphic in a sufficiently small neighborhood. The points are distinct and exceed one, so the constant term's pole cannot cancel any of them. Therefore (P7) is a meromorphic continuation with genuine poles at

\[
T=q^2,q^3,q^4,\ldots.
\]

It is not a rational function.

For completeness, every sequence `p(n)alpha^n` has rational ordinary generating series: start from `sum_(n≥0)(alpha T)^n=(1−alpha T)^(−1)` and apply the operator `T d/dT` enough times to generate powers of `n`. A finite sum remains rational. Changing finitely many initial values changes the generating function by a polynomial, so eventual equality in (P5) would still make `H(T)` rational. This contradicts the infinitely many genuine poles. ∎

There is no positivity assumption in this proof. Arbitrary grouping and cancellation among finitely many complex roots, arbitrary signs, and polynomial factors in `n` do not evade it.

## 3. General rational-function criterion

The explicit proof admits a clean general version.

**Claim P-B.** Let `b>1` be real and let `f(x)∈C(x)`. Then the sequence `f(b^n)`, for all sufficiently large positive integers `n`, is a finite exponential-polynomial sequence if and only if `f` is a Laurent polynomial. A rational function has no poles on `b^n` for all sufficiently large `n`, so the eventual sequence is always defined.

**Proof of sufficiency.** If `f(x)=sum_(j=L)^J a_j x^j`, then `f(b^n)=sum a_j(b^j)^n`, already a finite power sum.

**Proof of necessity.** Expand at infinity:

\[
f(x)=\sum_{j=-\infty}^{J}a_jx^j
\]

for `|x|` sufficiently large. There are only finitely many positive powers. Choose an integer `N` so large that this expansion converges absolutely at `x=b^N`, and slightly inside that circle as well. More concretely, the negative coefficients obey a bound `|a_(−m)|≤C A^m` for some `A`, and we may take `b^N>A`.

For `T` near zero, absolute convergence then gives

\[
G_N(T)=\sum_{n\ge N}f(b^n)T^{n-N}
=\sum_{j=-\infty}^{J}\frac{a_j b^{jN}}{1-b^jT}.
\tag{P8}
\]

The terms with `j≥0` are finite in number. For the negative tail and any fixed compact set `|T|≤L`, the denominator is bounded below by one half for all sufficiently negative `j`; the numerator is bounded by a summable geometric sequence because `b^N>A`. Therefore (P8) converges normally away from its displayed poles, with the same omitted-single-term argument as in §2.

Every nonzero `a_j` contributes a genuine pole at `T=b^(−j)`: no other index has that pole. If the Laurent expansion has infinitely many nonzero coefficients, there are infinitely many poles and `G_N` cannot be rational. But an eventually finite exponential-polynomial sequence has rational `G_N`, by the preceding differential-operator argument. Hence only finitely many coefficients are nonzero. The resulting Laurent polynomial agrees with `f` near infinity, and thus as a rational function everywhere. ∎

Replacing `f(x)` by `f(x^(−1))` gives the equivalent statement for `f(b^(−n))`. A change of sign convention for the grading variable therefore does not remove the obstruction. In (P2), the rational function is invariant under that inversion anyway.

**Independent algebraic proof of necessity.** The fresh reviewer `/root/rectangular_and_theta` supplied a second proof, which I checked. An eventual exponential-polynomial sequence satisfies a nonzero constant-coefficient recurrence

\[
\sum_{j=0}^s c_j f(b^{n+j})=0
\]

for all large `n`, with `c_0≠0` after trimming any initial zero coefficients (or by using a recurrence with nonzero characteristic roots). Hence the rational function `sum_j c_j f(b^j x)` has infinitely many zeros `x=b^n` and is identically zero. If `f` has a nonzero finite pole, choose one of maximal absolute value. That pole appears in the `j=0` term. No `j≥1` term can have a pole there, since its pole set is obtained by dividing the poles of `f` by `b^j`, strictly reducing their moduli. It therefore cannot cancel, contradiction. Thus `f` has poles only at zero and infinity, which is precisely the Laurent-polynomial condition. This independently proves P-B without analytic continuation; the explicit normally convergent expansion in §2 remains available as the requested certificate for (P4).

This criterion is purely an exact trace-family criterion. It does not assert that every Laurent polynomial has an effective pure realization, that its coefficients are positive, or that a choice of individual realizations is compatible with multiplication.

## 4. Why a finite derived Weil complex still has a rational trace series

Let `V^bullet` be a bounded complex with finite-dimensional cohomology over a coefficient field embedded in `C`, equipped with an invertible Frobenius `F`. Let `T` be a fixed endomorphism. If `T` is a Weil endomorphism, it commutes with `F`, but that additional assumption is not needed for the following conclusion:

\[
u_n=\sum_i(-1)^i\operatorname{Tr}(T F^n\mid H^i(V^\bullet))
\]

has rational generating series. For each finite-dimensional term,

\[
\sum_{n\ge0}\operatorname{Tr}(TF^n)Z^n
=\operatorname{Tr}\bigl(T(I-ZF)^{-1}\bigr),
\]

a rational function. Sum over the finitely many degrees. Equivalently the Cayley–Hamilton recurrence or Jordan normal form makes `u_n` an exponential polynomial. If `T` commutes with `F`, traces of the nilpotent Jordan contributions vanish and the sequence is a finite ordinary power sum; the more generous rational-series argument already suffices.

Thus allowing mixed cohomological parity, nonsemisimple Frobenius, arbitrary signed/complex coefficients, or even polynomial-in-`n` terms cannot realize (P4). This genuinely tests the finite-spectrum input used in the signed even-power criterion F24, rather than merely its positivity hypothesis.

## 5. The exact comparison axiom ruled out

It is essential to separate two quantities:

1. The ordinary matrix trace in a formal algebra representation, followed by the substitution `v=q^(n/2)`.
2. The trace of a **fixed** geometric/derived correspondence against the `n`th power of a **fixed** Frobenius operator.

They are not equal by definition. The following is a possible proposed bridge, and the result proves that it is too strong for the actual normalized projectors:

> There exists a finite-cohomology Weil realization `V^bullet` and fixed Weil endomorphisms `E_1,E_2`, intended to realize the two actual normalized nonstandard projectors, such that for every word `w` and every extension degree `n`,
>
> `sum_i (−1)^i Tr(w(E_1,E_2)F^n | H^i(V^bullet)) = Tr_M(w(e_1(v),e_2(v)))|_(v=q^(n/2))`.

**Claim P-C.** This bridge is impossible. The single word `w=e_1e_2` already gives the nonrational sequence (P4), while every left side has rational generating series by §4. The same is true for the inverse-variable convention `v=q^(−n/2)`. In fact no assumptions about `E_i²=E_i` are needed for the contradiction, so requiring actual idempotents cannot repair it.

The conclusion does **not** say that the GCT sources impose this bridge, that the algebra has no geometric model, or that the actual projectors cannot act on any Weil object. The coherent model and actual tensor-module action in the preceding reports already give genuine algebraic idempotent endomorphisms in a coherent category. At one fixed numerical specialization `v=q^(1/2)`, the matrices themselves may also be placed on a finite-dimensional constant Weil vector space with scalar Frobenius. That realizes the specialized algebra action, but then `Tr(E_1E_2F^n)` is a fixed finite spectral sequence; it is not the result of replacing `v` by `q^(n/2)` anew at every extension degree. The grading-to-Frobenius comparison remains different.

Likewise, the theorem does not rule out an alternative arithmetic dictionary that extracts Laurent numerators before normalization, retains rational factors outside the finite trace, uses a different auxiliary geometry, or associates more structure than this word-trace rule. Any such dictionary must be stated and checked explicitly; the literal rule above cannot simply be assumed.

## 6. Mixed-parity K0 lifts do not solve the functorial problem

The unnormalized trace (P3) is a Laurent polynomial in `Q=v²`:

\[
24(Q+2+Q^{-1})^2+16.
\]

Its monomials can individually be realized by Tate lines, and arbitrary signed Laurent polynomials by bounded direct sums of Tate lines in even and odd degrees. More generally the actual unnormalized action matrices are Laurent polynomial matrices on the original tensor lattice, so one can formally lift their individual entries to signed graded classes.

This supplies classes and individual trace polynomials. It does not give a functor whose composition realizes multiplication, compatible chain maps for the generators, the quadratic relation as a coherent isomorphism of functors, or splitting data for the normalized idempotents. Those are actual categorical structure and cannot be recovered from K0 identities alone.

There is already an elementary decategorified denominator issue in the natural finite mixed-Tate ring: with `L` the Tate class, `D=L+2+L^(−1)` is not a unit of `Z[L,L^(−1)]` (nor of `Q[L,L^(−1)]`). Thus no bounded finite virtual sum of Tate lines has class `D^(−1)`. In the ambient Hecke basis, the actual normalized generator expands as

\[
\frac{P_i}{D}
=1-\delta^{-1}(c_i\otimes1+1\otimes c_i)
+2\delta^{-2}c_i\otimes c_i.
\]

A bounded object in a category whose Grothendieck group is the ordinary Laurent Hecke lattice cannot have this class without localization or an enlarged completion. The basis-independent trace obstruction in §5 is stronger than this particular basis calculation: it remains after changing the module basis.

Localized Grothendieck rings, stacks with unbounded cohomology, completed Hecke categories, or explicit inverses of Tate Euler factors may accommodate rational functions of `L`; none is claimed nonexistent. A realization of these particular substituted non-Laurent trace functions cannot remain in the finite-spectrum setting unless the desired trace comparison is changed or an additional finite extraction is proved. This does not say that every object in a localized category has infinite cohomology. For example the formal expansion (P6) is precisely an infinite collection of distinct candidate Tate eigenvalues, with unbounded degrees and signed multiplicities. One must establish convergence and a new trace formalism before using such a completion, and the finite-spectral lemma F02/F24 cannot be applied to it unchanged.

The concrete remaining choice is therefore sharper than “find some geometry”: decide which normalized or unnormalized nonstandard expression is to be represented, define an arithmetic comparison that avoids the proved nonrational word-trace obstruction, and then prove its finite-spectrum and categorical composition properties.

## 7. Checks and source scope

- The actual module decomposition used in (P1) was proved by exact regular matrices in `agent_rank3_tensor_geometry.md` and has an executable SymPy certificate. It is not inferred only from source dimensions.
- The scalar trace (P2) was computed directly from source equation (110), then expanded using those actual multiplicities. The cancellation of `1/D` terms leaves `24+16/D²` exactly.
- The normal-convergence and genuine-pole argument in §2 was checked in full, including uniqueness of each pole and invariance under deleting initial terms.
- The general rational-function criterion in §3 was checked in full. Its necessity is not an asymptotic approximation: infinitely many nonzero Laurent coefficients give infinitely many exact meromorphic poles.
- The finite-derived-Weil trace statement follows from the exact matrix resolvent identity and permits more general endomorphisms than the intended Weil correspondences.
- No primary literature beyond the already supplied GCT IV action/presentation is needed for these elementary deductions. They are new calculations in this research record, not claimed GCT theorems or historical first discoveries.
- A fresh independent review and final generated-statement match remain to be recorded separately.
