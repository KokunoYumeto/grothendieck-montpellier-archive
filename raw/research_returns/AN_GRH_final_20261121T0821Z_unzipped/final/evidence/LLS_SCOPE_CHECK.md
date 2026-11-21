# Follow-up: does LLS supply the desired uniform coefficient 2?

## Source-based answer

**Not as an immediately applicable all-modulus coefficient-2 theorem with a small finite exceptional range.** The relevant general-subgroup result is Theorem 1.1, not Theorem 1.4 or the quadratic-nonresidue corollary. Theorem 1.1 does imply coefficient 2 for all sufficiently large moduli, and admits the explicit criterion below, but its displayed bound can exceed coefficient 2 even above 10^16. Thus checking N<3000 would not complete a uniform coefficient-2 argument.

The primary current text checked is the authors' revised arXiv v3, dated December 2016:
https://arxiv.org/pdf/1309.3595
Web source: turn114912261view1; its page2 was also visually inspected (turn585610294view0).
The authors' revision notice is at https://arxiv.org/abs/1309.3595 (turn888603384view0): the error was in Lemma6.1 and affected asymptotic Theorems1.2 and1.3; those are corrected in v3. Theorem1.1 has the same statement in the older author-hosted PDF and v3. We did not retrieve the full separate 2017 corrigendum, and do not claim to have read it. Its official metadata is Math.Comp.86(2017),2551–2554, DOI https://doi.org/10.1090/mcom/3261 .

## Exact general-subgroup theorem

For q>=3000 and every proper H<(Z/qZ)^*, assuming Dirichlet GRH, Theorem1.1(1) gives a prime ell not dividing q, with ell outside H, satisfying

    ell <= (log q+B(q))^2,
    A(q) = max(0, 2 log log q - 8/5 - sum_{p|q} log(p)/(p-1)),
    B(q) = max(0, 2 log log q + 3
                  + 2 omega(q) (log log q)^2 / log q - 2 A(q)).

Consequently a strict coefficient-2 generator certificate follows whenever

    B(q) < (sqrt(2)-1) log q.

That criterion is sufficient, not necessary. As with Bach, proper-subgroup exclusion proves generation by the primes up to the stated bound. If B(q)=0, the stronger bound (log q)^2 applies.

Theorem1.1(2) gives ell <= (log q)^2 under the additional hypothesis that q has no prime divisor below (log q)^2. This covers large prime moduli and suitably rough composite moduli. It does not cover moduli with small factors2,3,5 merely because their numerical value is large.

Corollary1.1 is restricted to quadratic nonresidues for prime q>=5; it is not an all-character or all-subgroup statement for arbitrary composite q. Theorem1.4 addresses a prescribed coset with a bound depending on the subgroup index, so it does not state a uniform coefficient-2 generation result either.

## Exact checks showing the finite-range obstacle

`check_lls_bound_scope.py` evaluates the displayed Theorem1.1 expression with rational logarithm intervals. It was run successfully. These are **checks of the size of an upper-bound expression, not counterexamples to actual prime generation**.

| q | Factorization | Enclosure for (log q+B(q))^2/(log q)^2 |
|---|---|---|
| 30030 | 2*3*5*7*11*13 | approximately [4.987435583,4.987435667] |
| 13082761331670030 | product of the first14primes, through43 | approximately [2.023032672,2.023032686] |

The assertions that both ratios exceed2 are exact rational comparisons in the executable. Both moduli violate the rough-modulus hypothesis of part(2). Therefore a direct attempt to combine the displayed LLS bounds with verification only below3000 does not establish the requested uniform coefficient2. Further work would have to control the exceptional arithmetic factorization patterns or verify the outstanding moduli by a separate theorem/certificate.

## A fully explicit but coarse sufficient-large-modulus consequence

One can prove, from Theorem1.1, that coefficient2 holds for every integer N>=exp(300). This is a new elementary deduction, not a threshold quoted from LLS, and it leaves an enormous finite interval; it does not change the final paper's all-modulus coefficient3 statement.

Proof. Let L=log N>=300 and l=log L. Since 2^{omega(N)}<=N and log2>2/3,

    B(N) <= 2l+3+2 omega(N) l^2/L < 3l^2+2l+3.

The function F(L)=(3(log L)^2+2log L+3)/L is decreasing for L>=300, because

    F'(L)=-(3log L-1)(log L-1)/L^2 < 0.

Also log300<6: the factorial series gives e>8/3, and (8/3)^6>300. Hence

    F(300)<(3*36+2*6+3)/300=41/100.

It follows that B(N)<(41/100)L, and Theorem1.1 supplies a coprime prime outside any proper subgroup with

    ell <= (L+B(N))^2 < (141/100)^2 L^2
         = (19881/10000)L^2 < 2L^2.

The same proper-subgroup argument proves generation. All inequalities and the whole deduction were checked. This deliberately coarse threshold is not advertised as competitive or as a completed all-N coefficient2 theorem.

## Integration recommendation

Keep the final paper's main result unchanged: Bach3 for all moduli under the stipulated Alpoge input; elementary coefficient2 for the2/3-smooth and5-power families; exact coefficient2 at the53identified numerical moduli. A short note may add the exact LLS criterion above, with current arXiv v3 as the primary locator. Do not cite the old author-hosted PDF's superseded asymptotic constants from Theorems1.2/1.3.
