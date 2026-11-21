# DP58 — explicit sharp degrees and linear square tensor levels

Date: 2026-11-21 UTC. Author: `/root/formal_bound`, GPT-6 Astra Pro; reasoning effort is not exposed. The parent reserved DP58 and proposed the critical-weight exponential initial-form route. This memo checks that route completely, including the diagonal correction in the harmonic construction. It strengthens the pure-kernel and global-section conclusions of DP54/DP56; those checked files remain unchanged.

## 1. The ordinary primitive-line theorem

Use the actual arbitrary-unit singleton/complement pair \(G,H=G^D\) of DP46 over an unramified ring \(R=W(k)\), with \(p\) odd, \(h\ge3\), and \(k\) perfect containing \(\mathbf F_{p^h}\). Put \(K=\operatorname{Frac}R\), \(s=1/(p-1)\), and let \(\beta\) be its primitive logarithmic Poincaré splitting in additive coordinates, in a normalized invariant integral frame.

Fix a primitive mixed logarithmic line \((x,\mathbf y)=(ut,\mathbf vt)\), with \(u\in R^\times\) and \(\mathbf v\) primitive. Let \(j\) be the first index for which \(v_j\) is a unit, and put

\[
k_*=h-j,\qquad N=p^{k_*},\qquad d=N+1,\qquad
S=\frac{N-1}{p-1},\qquad
w=\frac{sN}{N+1},\qquad c=\frac{s}{N+1}.
\tag{ES1}
\]

For every unit \(\lambda\in R^\times\), write

\[
F_\lambda(t)=\exp\bigl(\lambda\beta(ut,\mathbf vt)\bigr)
=\sum_{n\ge0}A_n(\lambda)t^n.
\]

**DP58(a).** For every integer \(r\ge0\), at the explicit degree

\[
n_r=(p^{k_*}+1)p^r=dp^r,
\]

one has the exact identities

\[
\boxed{v_p(A_{n_r}(\lambda))
=-\frac{p^{k_*+r}-1}{p-1},}
\tag{ES2}
\]

\[
\boxed{v_p\bigl(n_r!A_{n_r}(\lambda)\bigr)
=\frac{p^r-1}{p-1}=cn_r-s.}
\tag{ES3}
\]

In particular all these derivatives are nonzero, their normalized valuations tend to the exact rate \(c\), and the valuation is independent of the unit \(\lambda\). This is a pure-kernel statement. It is not an exact-degree assertion for every additional integral prefactor.

## 2. The exact harmonic witness sequence

Fix an eigenaxis \(j\), keep \(N=p^{h-j}\), and set

\[
F_\lambda(x,y)=\exp\bigl(\lambda\beta(x,e_jy)\bigr).
\]

For \(a,b\ge0\), use the two-column polynomial from DP51:

\[
P_{a,b}=\sum_{i=0}^{\min(a,b)}(-1)^i
\binom ai\binom bi
X_1^{a-i}Y_1^{b-i}X_2^iY_2^i,
\tag{ES4}
\]

and write

\[
H_{a,b}(\lambda)=P_{a,b}(\partial)
\bigl(F_\lambda(x_1,y_1)F_\lambda(x_2,y_2)\bigr)\big|_0.
\]

**DP58(b).** For every \(r\ge0\), put

\[
a_r=p^r,\qquad b_r=p^{h-j+r}=Np^r,
\qquad n_r=a_r+b_r=(N+1)p^r.
\]

Then, for every unit \(\lambda\),

\[
\boxed{v_p(H_{a_r,b_r}(\lambda))
=\frac{p^r-1}{p-1}=cn_r-s.}
\tag{ES5}
\]

For every \(j\) this is an integral polynomial killed by the indicated summed contraction. For \(j=1\), using the first negative row and zero degrees on the later negative rows, it has the full source-shaped algebraic `HaO` conditions proved in DP51. For other \(j\), no impermissible reordering of a prescribed negative-row datum is being asserted.

The row-degree ratio is exactly \(a_r:b_r=1:N\), rather than only asymptotically approaching that ratio.

## 3. An elementary critical-exponential initial-form lemma

Let \(K'\) be a complete discretely valued extension of a mixed-characteristic field, with \(v(p)=1\), and suppose it contains \(\mu\) of valuation \(s=1/(p-1)\). Let \(z\in K'[[Z_1,\ldots,Z_D]]\) have zero constant coefficient and all its coefficients of valuation at least \(s\). Assume

\[
\overline{\mu^{-1}z}=u\,\mathbf Z^\alpha,
\qquad u\ne0,\qquad |\alpha|>0.
\tag{ES6}
\]

The bar denotes reduction in the residue field. Thus (ES6) is an assertion about the **entire** lowest-valuation form, not just the first ordinary-degree term.

Then \(\mu^{-1}(\exp z-1)\) is integral and

\[
\boxed{
\overline{\mu^{-1}(\exp z-1)}
=\sum_{r\ge0}\epsilon_r u^{p^r}
                  \mathbf Z^{p^r\alpha},
\qquad
\epsilon_r=\overline{\frac{\mu^{p^r-1}}{(p^r)!}}\ne0.}
\tag{ES7}
\]

**Proof.** Put \(Q=\mu^{-1}z\), an integral zero-constant series. The exponential expansion is

\[
\mu^{-1}(\exp z-1)
=\sum_{m\ge1}\frac{\mu^{m-1}}{m!}Q^m.
\tag{ES8}
\]

Its scalar in exponential order \(m\) has valuation

\[
(m-1)s-v_p(m!)
=s\bigl(s_p(m)-1\bigr)\ge0.
\tag{ES9}
\]

It is a unit precisely when \(s_p(m)=1\), that is, when \(m=p^r\). In every other order it has strictly positive valuation and contributes zero after reduction. For \(m=p^r\), reduction of \(Q^m\) is \(u^{p^r}\mathbf Z^{p^r\alpha}\). This proves (ES7).

Every coefficient in (ES8) is a finite sum because \(Q\) has zero constant term. The sum in (ES7) is also a well-defined formal series because \(|p^r\alpha|\to\infty\). The exponents \(p^r\alpha\) are distinct, so none of the displayed nonzero coefficients cancel each other. No convergence of an infinite sum at a fixed ordinary degree is being assumed. The hypothesis supplies a positive discrete gap for all other coefficients, but the reduction argument already treats them directly through \(\bar Q\). \(\square\)

This lemma also explains why an Artin–Hasse-type cancellation cannot occur under (ES6): such cancellation would need additional logarithmic monomials in the same lowest-valuation form. The complete one-monomial hypothesis is essential.

## 4. Applying the lemma to the actual full logarithm

The exact critical-weight result already proved in DP46, equations (UI16)–(UI19), gives a finite ramified extension containing a scalar \(\varpi\) with \(v(\varpi)=w\), and

\[
\mu=\frac{\varpi^{N+1}}{p^S},\qquad v(\mu)=s,
\]

such that

\[
\boxed{
\overline{\mu^{-1}\beta(u\varpi T,\mathbf v\varpi T)}
=\xi T^{N+1},\qquad \xi\ne0.}
\tag{ES10}
\]

More precisely \(\xi=(-1)^{k_*-1}\bar\theta_j\bar u\bar v_j^{p^{k_*}}\), where \(\theta_j\) is the unit arrow product in DP46. The important point is that (ES10) is the full initial form after substitution by the actual inverse logarithms. All additional unit arrows retain its nonzero scalar; all other logarithm terms have larger valuation. Invariant integral changes of frame also have larger logarithmic valuation at this profile, by DP46 §5.

Apply the lemma to

\[
z(T)=\lambda\beta(u\varpi T,\mathbf v\varpi T).
\]

Its entire initial form is \(\bar\lambda\xi T^{N+1}\), with nonzero scalar. Formula (ES7) therefore makes the coefficient of \(T^{(N+1)p^r}\) in \(F_\lambda(\varpi T)\) have valuation exactly \(s\), for every \(r\). Hence

\[
v_p(A_{n_r}(\lambda))=s-wn_r
=s-sNp^r
=-\frac{p^{k_*+r}-1}{p-1}.
\]

This proves (ES2), including its exact integer value in the original unramified field.

The integer \(n_r=p^{k_*+r}+p^r\) has base-\(p\) digit sum two, since \(k_*\ge1\). Thus

\[
v_p(n_r!)=s(n_r-2).
\]

Adding to (ES2) gives

\[
v_p(n_r!A_{n_r})=(s-w)n_r-s
=s(p^r-1),
\]

which is (ES3). The proof holds uniformly for every unit \(\lambda\); no congruence of \(\lambda\) to a fixed chosen unit is required.

## 5. The harmonic diagonal correction has no lowest-valuation term

The two-variable version of the same entire initial form is proved in DP51, equation (HA7) and its following paragraph. With independent additive inputs it is

\[
\boxed{
\overline{\mu^{-1}\lambda\beta(\varpi X,e_j\varpi Y)}
=\xi_\lambda X Y^N,\qquad \xi_\lambda\ne0.}
\tag{ES11}
\]

The group-coordinate minimum \(SY_d^p/p\) composes with the reduced inverse coordinates to a unit times \(XY^N\). This is the actual arbitrary-unit calculation, not an inference from the ordinary restriction \(X=Y\).

Put \(\widetilde F(X,Y)=F_\lambda(\varpi X,\varpi Y)\). The lemma gives

\[
\overline{\mu^{-1}(\widetilde F-1)}
=\sum_{r\ge0}\epsilon_r\xi_\lambda^{p^r}
                X^{p^r}Y^{Np^r}.
\tag{ES12}
\]

Write \(f_{a,b}=[x^ay^b]F_\lambda\) and define the diagonal correction and harmonic generating series exactly as in DP51:

\[
D(Z)=\sum_{i\ge0}f_{i,i}Z^i,\qquad
C(x,y)=F_\lambda(x,y)D(-xy).
\tag{ES13}
\]

Because \(N>1\), none of the monomials in (ES12) is diagonal. Thus, for every \(i\ge1\),

\[
v_p\bigl(\varpi^{2i}f_{i,i}\bigr)>s.
\tag{ES14}
\]

The values belong to one discrete value group, so these inequalities give a uniform positive gap beyond \(s\). Equivalently,

\[
\mu^{-1}\bigl(D(-\varpi^2XY)-1\bigr)
\]

is integral and has zero reduction. Since \(\widetilde F\) is integral with constant one, it follows that

\[
\boxed{
\overline{\mu^{-1}\bigl(C(\varpi X,\varpi Y)-1\bigr)}
=\sum_{r\ge0}\epsilon_r\xi_\lambda^{p^r}
                X^{p^r}Y^{Np^r}.}
\tag{ES15}
\]

In particular

\[
v_p(C_{a_r,b_r})=s-w(a_r+b_r).
\tag{ES16}
\]

For completeness, the exact coefficient identity behind the harmonic evaluation is

\[
\begin{split}
H_{a,b}(\lambda)
&=\sum_i(-1)^i\binom ai\binom bi
 (a-i)!(b-i)!(i!)^2 f_{a-i,b-i}f_{i,i}\\
&=a!b!\,[x^ay^b]\bigl(F_\lambda(x,y)D(-xy)\bigr).
\end{split}
\tag{ES17}
\]

Here the identity \(\binom ai\binom bi(a-i)!(b-i)!(i!)^2=a!b!\) is exact in characteristic zero. There is no estimate discarding some alternating summand.

At \(a_r=p^r\), \(b_r=p^{k_*+r}\), both digit sums equal one. Therefore

\[
v_p(a_r!b_r!)=s(a_r+b_r-2).
\]

Together with (ES16) this proves (ES5). The other terms in the alternating polynomial cannot cancel the selected leading value, because their total effect has already been computed in the full generating series (ES15).

## 6. Linear square tensor levels on the actual Jacobian

Apply the preceding results at \(p=11\) to the actual polarized pair on the Jacobian of DP49. Use the ample trace-one line and invariant product normalization of DP54. Choose fixed interpolation constants \(A\ge1\), \(B_0\ge0\) from DP56(a), so every jet of order \(n\) extends integrally in every power \(\kappa\ge An+B_0\).

For any one explicit witness degree \(n=n_r\), put

\[
m_0=\lceil\sqrt{An+B_0}\rceil,
\qquad
M=\begin{cases}
m_0,&11\nmid m_0,\\
m_0+1,&11\mid m_0,
\end{cases}
\qquad \kappa=M^2.
\tag{ES18}
\]

Two consecutive integers cannot both be divisible by 11. Therefore

\[
11\nmid M,\qquad
An+B_0\le\kappa
<An+B_0+4\sqrt{An+B_0}+4.
\tag{ES19}
\]

In particular

\[
\boxed{M=O(\sqrt n),\qquad
       \kappa=An+O(\sqrt n),}
\tag{ES20}
\]

with constants depending only on the fixed model and line. The constants are not numerical universal constants.

At this chosen power, interpolate the algebraic prefactor to the inverse integral frame unit \(U^{-\kappa}\) through degree \(n\), exactly as in DP54. The normalized germ then has the pure kernel jet with exponent \(\lambda=-\kappa\), a unit. Equations (ES3) and (ES5) apply to **every** unit parameter, so they give the exact selected valuation without any additional tensor congruence. The source factor \(M^{-n}\) is a unit.

Thus there are global sections at linearly bounded tensor powers realizing the exact ordinary values

\[
n_r=12\cdot11^r\ \text{or}\ 122\cdot11^r,
\qquad v_{11}(\text{normalized value})=\frac{11^r-1}{10},
\tag{ES21}
\]

for the two primitive-line classes. The first-row two-column harmonic witness is

\[
(a_r,b_r)=(11^r,121\cdot11^r),
\qquad n_r=122\cdot11^r,
\qquad v_{11}(\text{normalized value})=\frac{11^r-1}{10}.
\tag{ES22}
\]

For any fixed finite prefix of these sequences, one can realize all its values with one section at a power satisfying (ES19) for the largest degree: interpolate the complete jet to that order. The same unit parameter \(-\kappa\) works for every earlier witness. If using two columns, use two copies of that section. Finitely many selected primitive paths can likewise be included when their required degrees are bounded by the interpolated order.

The number-field approximation of DP54 preserves these finitely many nonzero valuations at the same chosen tensor power. Hence the sections can be chosen over \(\mathbf Q(\zeta_7)\), integral at the selected prime, without altering (ES19)–(ES22).

## 7. Limits of the strengthened result

The unique full logarithmic initial form supplies explicit pure-kernel sharp degrees, and the harmonic diagonal correction is strictly above that initial form. This eliminates the tensor congruence condition entirely for these witnesses and improves the subexponential tensor levels of DP56 to linear tensor powers.

The theorem does not assert exact values at these degrees for every integral theta prefactor. The global construction prescribes a special finite prefactor jet using integral interpolation. It does not make one fixed section realize the infinitely many witnesses; each finite prefix may require a larger tensor power and a new section. It does not prove bounds for the archimedean norms or heights of these sections, membership in the prescribed translated family, compatibility with an unrelated prescribed row-degree sequence, or the global endpoint and cost inequalities of a shorter lift chain.

The parameter must be a unit; the nonunit tensor behavior in DP50 is a different regime. No claim here contradicts that distinction or extends the primitive-projection hypothesis to a zero or nonprimitive projection.

## 8. Inputs and actual review record

The full logarithmic initial form used in (ES10) is DP46, §4, (UI16)–(UI19), including the integral contracted inverse maps and the common-uniformizer identity for \(\mu\). Its frame invariance is §5, (UI20). The two-variable version (ES11) is DP51, §2, (HA7) and the following proof paragraph. The harmonic coefficient identity is proved again in the short exact algebra (ES17), and the algebraic `HaO` scope is DP51 §5. The integral projective interpolation is DP56(a), and the actual theta pullback and arithmetic approximation are DP54.

The new exponential initial-form lemma, all exact coefficient and factorial valuations, the diagonal-correction calculation, and the linear square-level choice are proved in this memo. Their actual complete-read events, snapshots and hashes are recorded separately. No numerical experiment, Lean execution or machine formalization is claimed.
