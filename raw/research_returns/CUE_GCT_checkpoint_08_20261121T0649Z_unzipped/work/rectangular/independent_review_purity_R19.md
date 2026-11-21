# Independent whole-proof review: R-19

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

**PASS.** I read the complete `r19_fragment.tex` proof and independently rederived its support constraints, cofactor identities, coefficient transformations, evaluation determinant, and final dimension inequalities. This is a targeted mathematical proof review, not formal verification or an external certification. No numerical matrix rerun was needed.

## Simultaneous row and column support

The chosen centers are spaced by three, including the last-to-first cyclic gap, since `3a_m<=m`. Their row triples are disjoint. A foreign forward chord can enter columns `a,a+1` only from centers `a-2,a-1`; a foreign backward or third chord can enter them only from `a+1,a-1`. These forbidden centers are absent. Thus both the two-row and the two-column support conditions hold simultaneously.

The three complementary permanent factorizations for the column pair are correct. Direct expansion gives the two displayed identities with right sides `-2qr ell_a S` and `2qr v_a S`. Together with the independently checked row identities from R-18, these put all four polynomial families into one differential image for nonzero `epsilon`.

At zero, the unique complementary cycle matching gives exactly the displayed products for `C` and `D`. Their counts are respectively two or one extra diagonal factors and one or two extra cycle factors, giving the common bidegree `(m-k,k)`. The range `5<=k<=m-5` avoids all deleted-row/column coincidences.

## Column coefficient identities and shifts

At center zero the diagonal factors are the stated `A_C` and `A_D`. For `M=m-k`, the shifted base product `tilde A` has roots `q^2,...,q^(M+1)`. The first polynomial identity follows because `delta_0+delta_1=1` and `delta_0(q/K)+delta_1 q=1`. For the quadratic identity, the proposed coefficients sum to one; evaluations at `x/y=1,q` verify the other two conditions and hence the identity. All denominators are nonzero in the stated range.

Writing `r+s=t` gives the common coefficient factor `q^((2-k)t)`, so multiplying the two column vectors by `X^(k-2)` is correct. The three shifts of the original `C` root list and the two shifts of the `D` root list yield exactly the five-factor products displayed in the proof. This includes the endpoint `k=5`, where `J=1`. The two old columns and two row columns are `J v_(k-3)v_(k-2)` times the four independent R-18 cubics, so their quintics span the specified four-dimensional subspace.

## Independent evaluation-determinant derivation

Let `a=K/q^3`, `b=K/q^2`, and abbreviate the quintic products multiplying `eta_0,eta_1,delta_0,delta_1` by `P,R,B,Q`, respectively:

`P=v_-2 v_-1 v_0 v_1 v_k`,
`R=v_-1 v_0 v_1 v_(k-3) v_(k+1)`,
`B=v_-1 v_0 v_1 v_(k-2) v_k`,
`Q=v_0 v_1 v_(k-3) v_(k-1) v_(k+1)`.

The factors vanishing at `a,b` reduce the determinant to

`X^-1[eta_0 delta_1 P(a)Q(b)-delta_0 eta_1 B(a)R(b)] -delta_0 eta_0 B(a)P(b)`.

The coefficient of `X^-1` vanishes: `eta_0 delta_1=delta_0 eta_1`, and

`P(a)/B(a)=-(K-q)/(K(q-1))`,
`Q(b)/R(b)=-K(q-1)/(K-q)`.

For the remaining constant term, direct factor evaluation gives

`B(a)=K^2(q-1)^2(q^2+q+1)(K-q^2)(K-q^3)(K-q^4)/q^15`,

`P(b)=-K(q-1)(q+1)(K-1)(K-q)(K-q^2)(K-q^3)/q^10`.

Multiplying by `-delta_0 eta_0` yields exactly the stated determinant with denominator `q^27(K-1)(qK-1)`. The six factors `K-q^j`, `0<=j<=4`, and the denominator factors have the required nonvanishing; `q+1` and `q^2+q+1` are nonzero since the order of `q` is at least ten. Thus the two column quintics complement the four row quintics to all of `Sym^5 C^2`, uniformly in the character parameter.

## Six-coordinate and Fourier arguments

For `5<=k,t<=m-5`, the coefficient interval contains six consecutive indices `b,...,b+5` with `0<=b<=k-5`. The multiplication-by-`J` matrix on those indices is, up to signs and transpose, the dual Jacobi–Trudi determinant for `(6^b)` in `N=k-5` variables. Its Weyl numerator exponents lie in `[0,N+5]=[0,k]`, below the order `m`, so they give distinct roots and a nonzero Vandermonde. The case `N=0` is the identity matrix case. Consequently restriction to the available character coordinates retains the six-column independence.

Each relation among translated normal vectors gives four separate equations in each character. The centers give distinct powers of `q`, and the `a_m` consecutive characters `5,...,a_m+4` are available because `a_m<=m-9`. Four invertible Vandermonde systems therefore give `4a_m` independent normal classes in each of `m-9` bidegrees. All four families deform polynomially, so one augmented coefficient minor remains nonzero at a common generic nonzero parameter; ranks from different pencils are not added.

## Dimension and padding bounds

The differential argument proves `dim P_(m,4)>=2m^2+2+4a_m(m-9)`. The padding inequality implies the strict dimension gap required by R-14/G-10. Moreover

`n^2 <= 5m^2/3-6m+1 <16m^2/9`,

so `n<4m/3` and the stable padded point required by G-11 exists. The asymptotic surplus is `4m^2/3+O(m)`, giving the stated ratio below `sqrt(5/3)`. The proof correctly retains the earlier stronger bounds at some finite sizes and makes no claim about a polynomial algorithm for discovering the relevant multiplicities.
