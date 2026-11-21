# What primitive divisors and Hooley do—and do not—force

Date: 2026-11-21. Checker: GPT-6 Astra Pro, effort not exposed, `/root/row_audit`.

## Result

The recovered B.3 sufficient test cannot be forced universally: A23 gives an ordinary genus-two curve over F4 for which its inequality fails for every prime and every constant extension. The curve nevertheless has the A13 geometric theta witness. This is a proved obstruction to that particular numerical route.

For the separate Lang subgroup route A12, the primary primitive-divisor and greatest-prime-factor theorems checked here do not supply the required joint conclusion. The shortfall has two independent parts: exponential subgroup size as a function of extension degree, and synchronization of that subgroup's prime support with the order of the unrelated integer 2. Hooley supplies candidate primes; it does not supply either synchronization with a fixed Jacobian sequence or a sufficiently short rationality extension. No nonexistence of theta points is inferred.

## 1. The exact Lang threshold

Fix a genus-two curve in characteristic two and write

\[
Q=q^m,\quad G_m=J(\mathbf F_Q),\quad J_m=|G_m|,\quad
a=[G_m:H],\quad s=\sqrt Q.
\]

A12's nonzero-point sufficient test is

\[
Q+1-2(a+1)\sqrt Q>a.
\]

Solving for the index and subgroup size gives the equivalent inequalities

\[
a<\frac{(s-1)^2}{2s+1},\qquad
|H|>R_Q:=J_m\frac{2s+1}{(s-1)^2}.
\tag{1}
\]

The Weil inequalities `(s-1)^4 <= J_m <= (s+1)^4` show that `R_Q ~ 2 Q^(3/2)`, and explicitly

\[
R_Q\ge(s-1)^2(2s+1)=2Q^{3/2}-3Q+1.
\tag{2}
\]

For an ordinary curve the origin is outside theta, so the weaker positivity test is sufficient. It gives instead

\[
a<\frac{(s-1)^2}{2s},\qquad
|H|>J_m\frac{2s}{(s-1)^2}\ge2s(s-1)^2.
\tag{3}
\]

The asymptotic scale is the same. These conditions are sufficient tests; a theta point can exist when they fail.

For `H=G_m[ell^b]`, let `c_1,...,c_4 >= 0` be the elementary-divisor exponents of the rational ell-primary subgroup (padding with zero exponents). Then

\[
|H|=\ell^{\sum_i\min(b,c_i)}\le\ell^{4b}.
\tag{4}
\]

Thus even the most favorable full-rank case of (1) requires a conductor `ell^b > R_Q^(1/4) ~ 2^(1/4) Q^(3/8)`. If `v_ell(J_m)=1`, then `|G_m[ell]|=ell`, and the requirement is instead `ell>R_Q ~ 2Q^(3/2)`. A large exponent in the group order is not automatically the size of a specified truncated torsion subgroup; formula (4) is the relevant distinction. For the entire Sylow subgroup, its order is exactly `ell^(v_ell(J_m))`, but the signed-doubling condition must then hold at its actual exponent.

## 2. A primary primitive-divisor theorem applies, but gives the wrong quantity

**Exact primary locator.** L. P. Postnikova and A. Schinzel, *Primitive divisors of the expression a^n-b^n in algebraic number fields*, Math. USSR-Sbornik **4** (1968), no. 2, 153–159, **Theorem 1, p. 153**. The theorem states effective eventual existence of a primitive **prime ideal** divisor for coprime algebraic integers a,b with a/b not a root of unity. The original statement and definition were opened in the publisher-hosted English PDF. DOI: <https://doi.org/10.1070/SM1968v004n02ABEH002783>. Stable article page: <https://www.mathnet.ru/eng/sm3975>. PDF route: <https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=3975&what=fullteng>.

Apply this with a Frobenius eigenvalue `alpha` and `b=1` in `K=Q(alpha)`. The hypotheses hold: alpha is an algebraic integer, coprimality with 1 is automatic, and every complex conjugate has absolute value `sqrt(q)>1`. Here `[K:Q]<=4`. For every sufficiently large m, a primitive prime ideal `p` divides `alpha^m-1`. If its rational prime is ell and its residue degree is f, then

\[
\operatorname{ord}_{\mathcal O_K/\mathfrak p}(\alpha)=m,
\qquad m\mid\ell^f-1,
\qquad \ell\ge(m+1)^{1/f}\ge(m+1)^{1/4}.
\tag{5}
\]

The same rational ell divides the integer Jacobian count: the characteristic polynomial and `T^m-1` have a common root modulo ell, so their resultant is divisible by ell. Equivalently, the norm of `1-alpha^m` is a factor of `J_m`, counted with its polynomial multiplicity.

This is a valid unconditional supply of divisors. It gives order information about **alpha in a residue field**, not about **2 modulo ell**. A primitive prime ideal for one eigenvalue also need not be a primitive rational divisor of the full Jacobian sequence: a conjugate eigenvalue can contribute the same rational prime at an earlier index. The polynomial-size bound (5), even raised to the fourth power, cannot force the exponential-size threshold (2).

The theorem does not forbid much larger prime factors; the point is that its stated conclusion does not guarantee them. One must not turn a lower bound that is too weak into an upper bound or a nonexistence result.

## 3. The checked large-prime-factor theorems leave the same gap

**A direct dominant-term theorem.** C. L. Stewart, *On the greatest square-free factor of terms of a linear recurrence sequence*, in *Diophantine Equations* (N. Saradha, ed.), Narosa, 2008, 257–264, **Theorem 1, author PDF p. 2, equations (9)–(10)**. Its hypothesis is an integer `u(m)` with `0<|u(m)-f(m)alpha^m|<|alpha|^(delta*m)`, where `0<delta<1`. Its lower bounds are

\[
P(u(m))>c_1\frac{\log m\log\log m}{\log\log\log m},
\quad
\operatorname{rad}(u(m))>
m^{c_2\log\log m/\log\log\log m},
\tag{6}
\]

with effective constants. Primary PDF: <https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/greatest_square_free_factor_0.pdf>.

For genus two, `J_m=q^(2m)+O(q^(3m/2))`, directly by expanding the four Frobenius factors. Thus the theorem applies with `alpha=q^2`, `f=1`, for example `delta=7/8`, whenever the error is nonzero and m is sufficiently large. That error is nonzero for all sufficiently large m here: (5) supplies an odd prime divisor, since a residue field above 2 of degree at most 4 has multiplicative group order at most 15, and hence cannot contain alpha of order m>15. An odd prime divisor prevents `J_m=q^(2m)` in characteristic two.

Both explicit quantities on the right of (6) are `exp(o(m))`, while (2) is of order `q^(3m/2)`. Moreover a radical bound concerns the product of all prime factors, not a subgroup supported at an eligible prime or at the permitted pair of primes. The elementary consequence (5) is stronger than the first bound in (6) in this particular application; (6) is included as a directly applicable primary large-factor/radical theorem, not as a claim of an optimal bound.

**A stronger special-sequence theorem still has a subexponential scale.** C. L. Stewart, *On divisors of Lucas and Lehmer numbers*, Acta Math. **211** (2013), 291–314, **Theorem 1.1, p. 294, equation (1.7)**. For its stated algebraic pair with `(alpha+beta)^2` and `alpha*beta` nonzero integers and alpha/beta not a root of unity, it proves

\[
P(\Phi_m(\alpha,\beta))>
m\exp\!\left(\frac{\log m}{104\log\log m}\right)
\tag{7}
\]

eventually effectively. DOI: <https://doi.org/10.1007/s11511-013-0105-y>. Author PDF: <https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/s11511-013-0105-y.pdf>.

A general genus-two norm sequence is not automatically a Lucas or Lehmer sequence, and the pair `(alpha,1)` from a quartic Frobenius polynomial need not satisfy this theorem's integral-pair hypotheses. Even in a special case where it applies, the guaranteed quantity in (7) is `exp(o(m))`; it supplies neither the needed exponential mass nor the order condition on 2. No blanket application to every genus-two Jacobian is made here.

These are precise checked implications, not a claim to have exhaustively classified every published prime-factor theorem.

## 4. Why adding Hooley does not fill the missing implication

The Hooley/Lenstra input already checked in the audit and A17 supplies a positive-density set of eligible rational primes, under GRH for the number-field Dedekind zeta functions of `K_n=Q(zeta_n,2^(1/n))`, n squarefree (and the fixed congruence condition of A17). The stipulated Masullo premise M covers that family. The stipulated Dirichlet-only premise does not supply this nonabelian Kummer family in general.

For a fixed m, `J_m` has finitely many prime divisors. A positive-density theorem for primes does not imply that any of them is one of those divisors. Allowing m to vary does not by itself repair the size gap: every odd prime ell already divides some `J_m`, because Frobenius acts invertibly on the finite group `J[ell]` and some power acts as the identity. The extra content needed is an appropriately **short** rationality extension together with enough eligible torsion.

For example, if `|G_m[ell]|=ell^kappa`, with `1<=kappa<=4`, then (1) entails asymptotically

\[
m<\frac{2\kappa}{3}\log_q\ell+O(1).
\tag{8}
\]

Neither the primitive-ideal period `m | ell^f-1` nor Hooley's density provides (8). They also do not ensure that the large prime factors singled out by a divisor theorem lie in Hooley's set. If higher prime powers are used, one must additionally check the signed-doubling condition at that power; its prime-level version alone does not automatically lift through a Wieferich obstruction.

## 5. What conductors 3r can change

For the A17 primes `r=5 (mod 8)` with 2 primitive modulo r, the signed-doubling condition holds at 3, r and 3r. Therefore every nonzero theta point in `G_m[3r]` has an order allowed by A18. On rank-one bases A10 excludes order 3, but the ordinary case does not need that exclusion.

Since r differs from 3, finite abelian-group primary decomposition gives exactly

\[
|G_m[3r]|=|G_m[3]|\,|G_m[r]|,\qquad |G_m[3]|\le3^4=81.
\tag{9}
\]

Thus the test requires `|G_m[r]|>R_Q/|G_m[3]|`, and even the largest possible 3-torsion gain only lowers the requirement to `R_Q/81 ~ (2/81)Q^(3/2)`. If r occurs to multiplicity one in `J_m`, this becomes `r>R_Q/81`. Without that assumption, `|G_m[r]|<=r^4` gives only the most favorable necessary condition `r>(R_Q/81)^(1/4)`. This may materially help a particular finite example; it cannot change exponential growth into the subexponential guarantees (5)–(7). In the logarithmic form (8), its maximum gain is the fixed additive quantity `(2/3)log_q(81)` in m, not a new asymptotic regime.

The existing bounded computation is documented at `work/gt_certificates/positive_rank_theta/COMPOSITE_LANG_SEARCH_SCOPE.md`. It found no certified improvement over the prime-only test in its explicitly listed ranges, with bounded factorization effort. The inline code was not retained. No additional computation was run here, and that reported search is not treated as exhaustive or as a nonexistence theorem.

### A sharper rank restriction for the same prime-level tests

The complete auxiliary proof is in `work/row_audit/LANG_PAIRING_RANK_BOUND.tex`. Let `kappa=dim_F_r G_m[r]`. If `kappa>=3`, the rational subspace is not totally isotropic in the four-dimensional symplectic r-torsion space. The principal-polarization Weil pairing therefore has a nontrivial r-th-root-of-unity value on two rational points. Equivariance forces `Q=1 (mod r)`, so

\[
Q\ge2^{\operatorname{ord}_r(2)}.
\]

If 2 is primitive modulo r, this makes either Lang sufficient test impossible for `H=G_m[r]` when `r>=11`, or for `H=G_m[3r]` when `r>=17`, in the case `kappa>=3`. The four-dimensional torsion upper bound is then smaller than even `Q^(3/2)`, which is below the required subgroup threshold. For the weaker signed-doubling condition the corresponding proved cutoffs are 29 and 41. The finite anchor inequalities were checked by `verify_lang_pairing_cutoffs.py`; the proof covers all primes in the indicated ranges by a monotone two-step comparison.

Consequently any successful test in these ranges has `kappa<=2`. The best possible prime bound is sharpened to `r>sqrt(R_Q) ~ sqrt(2) Q^(3/4)`, or `r>sqrt(R_Q)/9 ~ (sqrt(2)/9)Q^(3/4)` for 3r; use the ordinary threshold in place of `R_Q` when appropriate. In particular, making all r-torsion rational cannot force this test for the indicated large eligible primes. This still does not rule out theta points, and the proof is not asserted for arbitrary truncated higher prime powers.

The precise pairing source inspected was Milne, *Abelian Varieties*, 2022 author version, Section 16, p. 29 (nondegenerate Galois-equivariant pairing) and Lemma 16.2(e), p. 30 (alternating polarized pairing): <https://www.jmilne.org/math/xnotes/AVs.pdf>.

## 6. The remaining exact gate

One sufficient arithmetic statement would be: for every positive-p-rank genus-two curve over a finite field of characteristic two, there are m and an odd conductor n with `H=J(F_(q^m))[n]` satisfying (1) (or (3) in the ordinary case), and every nontrivial possible point order in H satisfies the relevant signed-doubling/primitive-orbit condition. Prime powers and the A17 conductors 3r are concrete options. None of the primary theorems checked above proves that statement.

An alternative geometric statement can bypass the size test entirely: there is some odd cyclic subgroup whose theta multiples meet every primitive doubling orbit, equivalently the geometric primitive factor has 2-rank zero in the A18 setting. A single nonzero exact-order theta point with the full signed-doubling unit group suffices. A23 itself shows why retaining this geometric alternative matters: its curve has the A13 witness although every B.3 large-prime numerical test fails.

## Retrieval and review scope

The 1968 theorem statement/definition and publisher metadata, the full statement of Stewart's 2008 Theorem 1, and Stewart's 2013 Theorem 1.1 with its immediately preceding definitions were read in primary-hosted documents. Their full analytic proofs were not independently re-proved here. The 1974 Schinzel article was located bibliographically at J. reine angew. Math. 268/269 (1974), 27–33, DOI 10.1515/crll.1974.268-269.27, but its EuDML request returned 403 and the DigiZeitschriften resolver was inaccessible. No claim uses its uninspected strengthened theorem. The successful 1968 PDF route supersedes earlier failed direct Mathnet download links.
