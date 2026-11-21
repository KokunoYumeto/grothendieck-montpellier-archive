# SF-E832R. The uniformly reversed elliptic star is also excluded

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION
/root/sixfolds. Date: 2026-11-21.

**Status:** independently whole-reviewed by /root and /root/g34_eightfolds;
both mathematical reviews PASS on frozen draft
`dc18d6bf237e6133a4f86a74c466d3962380a2b8cbb48f440931012bc8877446`.
All reviewers: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION,
21 November 2026. No new computation is needed or claimed.
The frozen E832 base proof is unchanged. This adds the opposite
uniform sign, not arbitrary mixed-sign or multicenter line configurations.

## 1. Exact reversed architecture

Retain the actual unit F on the smooth complete-intersection surface
S with D=k theta, k>0. Consider any actual coherent extension

\[
 0\longrightarrow A\longrightarrow E\longrightarrow B\longrightarrow0,
 \qquad A=(F\otimes L)^{\oplus r}
          \oplus\bigoplus_j L_j^{\oplus n_j},
 \qquad B=M^{\oplus n_0},
 \tag{E832R.1}
\]

where r and n0 are positive, each n_j is positive, and

\[
 c_1(L_j)=\alpha+P_j,\quad\alpha=c_1(M),
 \qquad P_j\ge0,\quad\operatorname{rank}P_j\le1.
 \tag{E832R.2}
\]

The free total rank is m=n0+sum_j n_j, and R=r+m. An empty sum is permitted.
In the opposite-slope realization, M is the single negative free center,
and the positive free classes have nonzero rank-one differences of positive
theta-degree from it, so(E832R.2) is automatic. The sheaf E has no weakly
semiregular balanced lift with normalized character R v_q, q nonzero,
for any algebraic rational B field and any specified coherent effective
finite action in E825's scope.

## 2. Complete proof

Include the quotient free terms with P0=0. The actual K0 identity from
(E832R.1) and the fact P_j²=0 give the free character
exp(alpha)(m+H), with H=sum_j n_j P_j semipositive. After a rational B
shift replace alpha by alpha+B and put u=c1(L)+B. The unit contributes
r exp(u) through its second Chern character, exactly as computed in E832.
The normalized first Chern equation is

\[
 ru+m\alpha+H=0.
 \tag{E832R.3}
\]

Thus the completed-square form in E832.9 is

\[
 b=\alpha+\frac r m u=-\frac{H}{m}\le0.
 \tag{E832R.4}
\]

The same degree-two calculation gives
b²-kappa u²=d(theta_+²+theta_-²), with kappa=rR/m² positive and d=Rq/m
nonzero. Put b'=−b. Then b' is semipositive and b'²=b², so it satisfies
the identical compound-square equation.

The exact defect interface must still be checked for this reversed
filtration. Since B is locally free, (E832R.1) splits locally. Relative to
these splittings the FF diagonal transition is that of F tensor L to
multiplicity r. The other diagonal blocks are free, and the extra
extension terms go from the free B part to A. E825's multiplicative ell
map kills every off-diagonal free-to-unit or free-to-free term, as well as
products factoring through a free module. After removing the fixed F
comparisons, its resulting cocycle is precisely the line cocycle of L
to multiplicity r. Hence Qtilde=L^r on S2 and its determinant extends to
r c1(L) on X.

If a balanced weakly semiregular lift existed, E825.3--4 would therefore
force u−7D/2 to have zero mixed RM blocks and zero trace on each rank-two
RM plane. The two traces of u are7k>0. The semipositive lemma of E832§3
applies to b',u,kappa,d and gives a contradiction. This proof uses the
intrinsic E825 condition on E; it does not require an extra action on the
chosen extension filtration or its local direct summands.

## 3. Boundary and checks

Together with the base theorem this covers stars with either uniform
semipositive sign. When different leaves have different signs, the sum
H need not be semipositive or seminegative and this proof does not apply.
Multiple centers, different unit characters and arbitrary gluing with an
unproved defect determinant remain outside. No new source, numerical
premise, finite action or successful seed is introduced. The only added
algebra is b'=-b and b'²=b²; the exact reversed A/B interface has been
supplied explicitly above.
