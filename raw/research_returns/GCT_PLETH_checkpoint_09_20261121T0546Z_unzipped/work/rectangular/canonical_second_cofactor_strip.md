# The full second-cofactor strip below the square bound

## R-030. Statement

For all integers
\[
r\ge2,\qquad 1\le j\le r-1,\qquad r+j\text{ odd},
\tag{CS.1}
\]
put
\[
a=r+1,\quad b=r^2-r+j,\quad H=r^2+j,
\qquad
\lambda=(H,(H-1)^{r-2},H-3,j+1).
\tag{CS.2}
\]
The normalized canonical map
\(h_{b,a}:\operatorname{Sym}^b\operatorname{Sym}^aV
\to\operatorname{Sym}^a\operatorname{Sym}^bV\)
has target and image multiplicity exactly one at \(\lambda\),
in every dimension where this Schur functor is nonzero.

The first endpoint \(j=1\) is in R-027 and the odd-\(r\)
endpoint \(j=2\) is R-029. The proof below establishes the full
range (CS.1), including the critical degree \(b=r^2-1\) at
\(j=r-1\). No historical novelty claim is made.

## 1. Actual polynomial, complement, and lower canonical map

Retain the determinant \(D\), last two cofactor rows \(y,z\)
and polynomial \(\mathcal S\) defined in (SE.2). The highest
polynomial is
\[
F=D^{j-1}\mathcal S\prod_i y_i^{r-2}=F_{r+1,H,r}.
\tag{CS.3}
\]
The exponent is nonnegative. The literal raising substitutions and
column-permutation calculation BS.8–BS.9 give precisely the slot
degree \(b\), the row weights (CS.2), and slot symmetry, since
\(H\) is odd. The complementary-column perfect pairing and
primitive Young projectors BS.10–BS.15 identify its multiplicity
with the unique highest wedge (SE.3). Hence the target multiplicity
is one; this includes \(r=2\), where that complement is \((3,3)\).

The exact retained-slot/common-polarization annihilator inclusion
K.16–K.22 applies because
\[
b-r=(r-1)^2+j-1\ge(r-1)^2.
\tag{CS.4}
\]
The lower canonical map is surjective by Sra's Theorem 1.3.
Thus a nonzero value of
\((T_{r,r,b}\otimes1)\delta F\) proves the actual image
multiplicity. We compute its coefficient
\([x_1^r\cdots x_r^r w^j]F\), with the first \(r\) first-row
bases zero and the retained slot's first-row coordinate equal to
\(w\). Its total first-row degree is exactly \(H\).

## 2. Literal matrix and both coefficient terms

Use exactly the matrix (SE.5): \(a_i=2+\zeta_i\),
\(\zeta_i^r=-1\), \(a_{r+1}=0\); \(b_i=0\) for
\(i\le r\), \(b_{r+1}=1\); reference column 1; rows
\((a_i^e-a_1^e)\), \(2\le e\le r-1\), then \(b_i\),
then \(a_i-a_1\). Its inverse-transpose construction and
Vandermonde proof remain valid at \(r=2\), with the first row
list empty. Put \(\eta=(\det A)^{-1}\),
\(S=\sum_{i\le r}x_i\), \(Z=\sum_{i\le r}a_ix_i\), and
\(s=S+w\). The actual cofactors are (SE.6).

Set \(Q=(z-2s)^r+s^r\) and \(Q_i=Q/(z-a_i s)\).
Multiplying those cofactors gives the polynomial identity
\[
F=(-1)^{r-2}\eta^{H-1}s^{j-1}Z^{r-2}
\left(wS^2Q(s,Z)^{r-1}
 +Zw^2Q(s,Z)^{r-2}\sum_i x_iQ_i(s,Z)\right).
\tag{CS.5}
\]
This is (SE.7) with its determinant power and general parity
retained. It keeps the contribution from every summand of
\(\mathcal S\).

Put \(N=r^2+j-3\). The Leibniz and apolar adjoint calculations
of (SE.8)–(SE.10) give the exact coefficient
\[
\frac{(-1)^{r-2}\eta^{H-1}}{(j-1)!(r!)^r}
\left(A_j+r(j-1)B_j\right),
\tag{CS.6}
\]
where, after the determinant-one translation and with
\(Q_0=z^r+s^r\),
\[
A_j=\left\langle (z+2s)^{j-1}\partial_z^2(Q_0^r),
 s^{j-1}(z+2s)^{r-2}Q_0^{r-1}\right\rangle_N,
\tag{CS.7}
\]
\[
B_j=\sum_i\left\langle (z+2s)^{j-2}Q_0^{r-1}q_i,
 s^{j-1}(z+2s)^{r-1}Q_0^{r-2}q_i\right\rangle_N
\quad(j\ge2),
\tag{CS.8}
\]
and \(B_1=0\). Here
\(q_i=\sum_{t=0}^{r-1}\zeta_i^t s^t z^{r-1-t}\).
In particular \(\sum_i\zeta_i^{t+u}\) is \(r\) at zero,
\(-r\) at \(r\), and zero otherwise in this range.
The normalization in (CS.6) comes from the two derivatives of
\(w\)-orders \(j-1,j-2\) and from differentiating each
\(x_i\) in the second term: the latter gives the factor \(r\).

## 3. Two finite integer sums

Define \(f_N(p)=(-1)^p p!(N-p)!\). The parity condition makes
\(N\) even, so this is also the apolar sign in terms of the
\(z\)-degree. Exact exponent matching modulo \(r\) in (CS.7)
gives
\[
\begin{aligned}
\mathcal A={}&\sum_{i=1}^r\sum_{\ell=0}^{j-1}
\binom ri\binom{r-1}{r-i}
\binom{j-1}\ell\binom{r-2}{j-1-\ell}\,
(ri)(ri-1)f_N(ri-2+\ell),\\
A_j={}&2^{r-2}\mathcal A.
\end{aligned}
\tag{CS.9}
\]
For \(j\ge2\), define
\[
\begin{aligned}
\mathcal B={}&\sum_{\ell=0}^{j-2}
\binom{j-2}\ell\binom{r-1}{j-1-\ell}
\Bigg[
\sum_{v=0}^{r-2}\binom{r-1}v\binom{r-2}{r-2-v}
 f_N(rv+r-1+\ell)\\
&\hspace{16mm}-
\sum_{v=1}^{r-1}\binom{r-1}v\binom{r-2}{r-1-v}
\sum_{t=1}^{r-1}f_N(rv+r-1-t+\ell)
\Bigg],\\
B_j={}&r\,2^{r-2}\mathcal B.
\end{aligned}
\tag{CS.10}
\]
Put \(\mathcal B=0\) at \(j=1\). To check these ranges,
the extra exponents in (CS.7) sum to \(j-1\). In (CS.8)
they also sum to \(j-1\), while the two root exponents sum
either to zero or to \(r\). Their largest possible extra sum
is \(j+r-3\), so no other congruence class representative is
possible. The two root sums give the two signed terms in
(CS.10). All powers of 2 are exactly \(2^{r-2}\).

Thus it suffices to prove the unconditional strict inequality
\[
\boxed{\mathcal A+r^2(j-1)\mathcal B>0.}
\tag{CS.11}
\]
We prove it by explicit bounds for \(r\ge10\), and give the
complete finite integer certificate for \(2\le r\le9\).

## 4. Endpoint and interior bounds for the first sum

Write \(M_0=r^2(r^2-1)N!\). The absolute terms of
\(\mathcal A\) at \(i=r\) strictly increase with \(\ell\).
Indeed their consecutive ratio is
\[
\frac{(j-1-\ell)(r^2-1+\ell)}
{(\ell+1)(r-j+\ell)}
\ge\frac{N}{(j-1)(r-2)}>1
\quad(\ell<j-1).
\tag{CS.12}
\]
The last term is positive, because its exponent is \(N\),
which is even. Pairing backwards gives the endpoint contribution
at least
\[
M_0\left(1-\frac{(j-1)(r-2)}{N}\right)
\ge M_0\frac{5r-8}{r^2+r-4}
\ge M_0\frac3r.
\tag{CS.13}
\]
At \(j=1\) the endpoint is exactly \(M_0\). The last
inequality follows from \((r-4)(2r-3)\ge0\), and the middle
one uses the maximum permitted \(j=r-1\).

For every \(1\le i\le r-1\), binomial convolution gives
\[
\binom N{ri-2+\ell}
\ge\binom{r^2-2}{ri-2}\binom{j-1}\ell,
\quad
\binom{r^2-2}{ri-2}
=\frac{ri(ri-1)}{r^2(r^2-1)}\binom{r^2}{ri}.
\tag{CS.14}
\]
The derivative factor in (CS.9) cancels against this exact
binomial ratio. Use
\(\binom{r^2}{ri}\ge\binom ri^r\),
\(\binom{r-1}{r-i}\le\binom ri\),
\(\binom ri\ge r\), and sum the remaining binomial in
\(\ell\). The total absolute interior contribution, divided
by \(M_0\), is at most
\[
(r-1)2^{r-2}r^{2-r}<\frac1{r^2}\qquad(r\ge10).
\tag{CS.15}
\]
For the strict bound, write it as
\((r-1)r^2(2/r)^r/4\). Since \(r\ge10\), it is at most
\(64/r^5<1/r^2\), by replacing the exponent \(r\) by 8
and using \(r-1<r\).

## 5. An absolute bound for the second sum

Assume \(j\ge2\); the term is zero at \(j=1\).
First separate the endpoint \(v=r-1\) in the second line of
(CS.10). Put \(h=j-1-\ell\), so \(1\le h\le j-1\).
Its absolute value divided by \(N!\) is at most
\[
\sum_{h=1}^{j-1}\binom{j-2}{h-1}\binom{r-1}h
\sum_{t=1}^{r-1}\binom N{t+h-1}^{-1}.
\tag{CS.16}
\]
In this range \(t+h-1\le2r-4\), and the consecutive ratios
of the reciprocal binomial coefficients are at most
\[
\frac{2r-3}{N-2r+4}\le\frac2{r-1}.
\]
The inner sum in (CS.16) is therefore at most
\((r-1)/(r-3)\) times \(\binom Nh^{-1}\).
Set \(\tau=(r-1)/N<1/(r-1)\). Termwise comparison of
falling factorials gives
\(\binom{r-1}h/\binom Nh\le\tau^h\).
Summing now bounds (CS.16) by
\[
\frac{r-1}{r-3}\tau(1+\tau)^{j-2}
<\frac6{r-1}.
\tag{CS.17}
\]
Here \((1+1/(r-1))^{r-1}<3\): expand by binomials, bound
the coefficient of degree \(q\) by \(1/q!\), and bound
the sum for \(q\ge2\) by \(\sum_{q\ge2}2^{1-q}=1\),
strictly at some terms. Also \((r-1)/(r-3)\le2\).

All remaining terms have the following elementary bound. Put
\(M=r^2-1\). Binomial convolution yields
\[
\binom N{p_0+\ell}\ge\binom M{p_0}\binom{j-2}\ell.
\tag{CS.18}
\]
It cancels the first binomial in the outer sum of (CS.10);
the sum of the second binomial is at most \(2^{r-1}\).
For its first inner sum, put \(i=v+1\), so \(1\le i\le r-1\).
The exact ratio is
\[
\frac{\binom{r-1}{i-1}\binom{r-2}{i-1}}
{\binom M{ri-1}}
=\frac{i(r-i)}{r(r-1)}
\frac{\binom ri^2}{\binom{r^2}{ri}}
\le r^{2-r}.
\tag{CS.19}
\]

For the second inner sum, now \(1\le v\le r-2\) and
\(rv\le p_0\le r(v+1)-2\). A binomial row is unimodal,
because its consecutive ratio \((M-p)/(p+1)\) decreases with
\(p\); so its minimum on this interval is at an endpoint. At those
endpoints, the exact adjacent-factor formulas give
\[
\binom M{rv}\ge r^{-2}\binom{r^2}{rv},\qquad
\binom M{r(v+1)-2}\ge r^{-2}\binom{r^2}{r(v+1)}.
\tag{CS.20}
\]
For the second inequality, put \(q=r(v+1)\); its ratio is
\(q(q-1)/(r^2(r^2-q+1))\ge r^{-2}\), since \(q\ge2r\).
Let \(C_v=\binom rv\). The numerator weight satisfies
\[
\binom{r-1}v\binom{r-2}{v-1}
\le C_vC_{v+1}\le r\min(C_v,C_{v+1})^2.
\]
The first inequality follows from including the chosen subsets
in sets of sizes \(r\), and the second from the adjacent
binomial ratio, which lies between \(1/r\) and \(r\).
Using \(\binom{r^2}{ri}\ge C_i^r\) and
\(C_i\ge r\) in (CS.20) consequently bounds each such
weight/denominator ratio by \(r^{5-r}\).

There are \(r-1\) terms of the first kind and
\((r-2)(r-1)\) of the second. Their combined bound, divided by
\(N!\), is therefore
\[
2^{r-1}\bigl((r-1)r^{2-r}
 +(r-2)(r-1)r^{5-r}\bigr)<\frac{513}{r^3}
\quad(r\ge10).
\tag{CS.21}
\]
For a direct numerical-free check, replace \((2/r)^r\) by
\((2/r)^{10}\). The two terms are then at most
\(512/r^7<1/r^3\) and \(512/r^3\), respectively.
Combining (CS.17),(CS.21), and
\(6/(r-1)\le20/(3r)\), gives
\[
\frac{|\mathcal B|}{N!}
<\frac{20}{3r}+\frac{513}{r^3}
\le\frac{3539}{300r}<\frac{12}{r}.
\tag{CS.22}
\]
Since \((j-1)/(r^2-1)<1/r\), this proves
\[
\frac{|r^2(j-1)\mathcal B|}{M_0}<\frac{12}{r^2}.
\tag{CS.23}
\]
Together (CS.13),(CS.15),(CS.23) imply
\[
\frac{\mathcal A+r^2(j-1)\mathcal B}{M_0}
>\frac3r-\frac{13}{r^2}>0\qquad(r\ge10).
\tag{CS.24}
\]

## 6. Exhaustive smaller parameters and the exact conclusion

There are exactly twenty pairs in (CS.1) with \(2\le r\le9\).
Their full exact positive integers are recorded in the table appended
below, generated from the displayed finite sums (CS.9),(CS.10).
For each pair, the companion program also expands the two complete
binary pairings (CS.7),(CS.8) separately and checks equality with
those sums. Thus this finite step is a reproducible exact integer
certificate, with all parameter pairs and values supplied.

Equations (CS.6),(CS.9),(CS.10) give the literal coefficient
\[
\boxed{
\frac{(-1)^{r-2}\eta^{H-1}2^{r-2}}{(j-1)!(r!)^r}
\left(\mathcal A+r^2(j-1)\mathcal B\right)\ne0.}
\tag{CS.25}
\]
The uniform bound and the exhaustive finite certificate prove its
nonvanishing for every stated parameter. The highest multiplicity
pairing, exact annihilator map and lower-map range (CS.4) then
prove R-030. All constructions commute with characteristic-zero
field extension and ambient-space inclusion, as in R-028 and R-029.

The lower-map primary input remains Sra, *The q-Foulkes problem III:
On Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
All additional maps and scalar factors are the actual cofactor,
Young-projector, retained-slot and apolar morphisms proved above.
The independent audit is `verify_second_cofactor_strip.py`, with
exact binary and literal-minor receipts named
`SECOND_COFACTOR_STRIP_BINARY_CHECK.tsv` and
`SECOND_COFACTOR_STRIP_LITERAL_CHECK.tsv`.

### Complete small-parameter integer certificate

The following number is (CS.25) after removing its nonzero signed
\(\eta^{H-1}\) factor. Every displayed number is a positive
integer. Decimal digits are grouped in blocks of three for readability. It includes the factor \(2^{r-2}/((j-1)!(r!)^r)\).

| r | j | Positive coefficient after removing the nonzero signed eta factor |
|---:|---:|---:|
| 2 | 1 | 8 |
| 3 | 2 | 23 328 |
| 4 | 1 | 254 822 400 |
| 4 | 3 | 23 482 368 000 |
| 5 | 2 | 105 462 680 400 000 000 |
| 5 | 4 | 9 013 985 580 600 000 000 |
| 6 | 1 | 42 723 642 031 055 513 540 812 800 |
| 6 | 3 | 21 370 543 932 252 982 904 698 060 800 |
| 6 | 5 | 2 013 250 309 035 912 916 893 097 574 400 |
| 7 | 2 | 10 160 607 303 670 416 270 020 588 947 601 778 278 400 |
| 7 | 4 | 3 370 587 174 858 215 820 736 421 348 489 478 144 000 000 |
| 7 | 6 | 366 120 803 047 691 343 176 713 153 543 311 074 525 184 000 |
| 8 | 1 | 1 162 606 348 436 923 479 519 760 349 831 637 949 278 437 611 929 600 000 |
| 8 | 3 | 1 928 940 089 042 056 048 115 936 261 626 758 472 695 991 009 227 571 200 000 |
| 8 | 5 | 571 022 990 525 822 292 583 783 949 648 106 707 314 198 795 348 082 688 000 000 |
| 8 | 7 | 72 222 987 449 617 993 587 491 669 788 025 345 886 795 053 445 357 785 579 520 000 |
| 9 | 2 | 497 116 640 826 042 691 474 802 511 294 742 444 624 174 913 077 129 137 522 046 702 387 200 000 000 |
| 9 | 4 | 461 016 503 608 441 965 265 209 101 648 245 471 439 371 174 982 599 425 982 312 624 988 160 000 000 000 |
| 9 | 6 | 135 223 645 522 697 751 163 724 001 906 584 067 146 510 492 379 736 391 492 135 800 438 303 948 800 000 000 |
| 9 | 8 | 19 885 485 881 296 602 875 815 148 928 023 208 548 092 194 225 018 973 144 378 395 314 655 095 193 600 000 000 |
