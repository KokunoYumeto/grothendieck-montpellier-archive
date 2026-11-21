# Independent review of P-F12

Reviewer: GPT-6 Astra Pro; reasoning effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-20 UTC.

## Scope and result

I read the entire current `work/positivity_ph3.tex`, including its hypotheses, proof, encoding assertion, parameter discussion, and diagnosis of the numerator index in GCT VI. I independently rechecked each inference against the statement of P-F11 already audited in `cross_positivity_modular_review.md`. This is an **independent-agent targeted whole-proof check**, not a formal proof certificate and not a claim of a fully different proof of P-F12. Result: **PASS** after the author clarified the degenerate zero-ray convention and stated dominant integral weights explicitly.

## Mathematical audit

1. Complete reducibility bounds the branching multiplicity by the ambient irreducible dimension. The Weyl product has degree exactly the number of positive roots pairing nontrivially with the dominant weight: every such slope is positive, and all other factors equal one. Applying the semisimple formula to the derived Lie algebra handles connected reductive groups; the central character contributes no dimension.
2. The progression argument bounds the number of factors in **any** positive rational form, including repeated weights and a numerator with gaps. With `L=lcm(a_j)` and one positive numerator entry, the displayed injection from weak compositions of `k` into denominator solutions proves growth of order at least `k^(r-1)` along a progression. There is no cancellation because the numerator is nonnegative. This forces `r-1 <= d_lambda`. Counting the first `r-1` denominator variables gives the matching upper bound and therefore `deg f=r-1`. Neither the size of `L` nor the Weyl leading constant enters the bound.
3. The properness bound from global quasi-polynomiality is exactly `deg N < sum a_j`; it does not assert `deg N <= deg f`. Combining it with P-F11 yields the strict displayed inequality. The case `r=1` and the torus case `d_lambda=0` remain valid.
4. The root counts in the four classical series give the stated quadratic rank bound. The source definition of `rank(x)` includes the ranks of both ambient and subgroup, so the claimed PH3-to-PH2 scope is preserved. The Kronecker restriction realization is a connected reductive case.
5. The coefficient bound `N_i <= f(i)` follows from the denominator's nonnegative expansion and constant term one. The specialized Weyl product gives the displayed bound for `GL_m`, including the empty partition and `m=1`. Since the number of coefficients is less than `rA+1`, the total encoding length is polynomial in the **numeric** parameter `A`, in `m`, and in `log(lambda_1+1)`. No inference from small `log A` alone is made.
6. The use of P-F2 is conditional on a supplied positive form; the existential conclusion and lack of a polynomial-time construction or equality certificate are stated separately. The warning about the compressed inner-weight encoding is necessary and correct: a bound polynomial in `dim GL(V_mu)` need not be polynomial in the binary description of `mu`.
7. The final KM contradiction is correct. A degree-one quasi-polynomial would have two denominator factors by the proved degree count. If the positive numerator were `1+cT`, vanishing at one forces `c=0` and both weights at least two. Values at two and three force one weight of each size, whose coefficient at four is one, contradicting the KM value two. This justifies the claimed index clash in the printed displays, without rejecting the actual Cohen--Macaulay positive numerator theorem.

## Degenerate-ray convention

The literal branching function always has `f(0)=1`. If all positive-degree multiplicities vanish, the function is an isolated delta at zero, so it is not a global quasi-polynomial on the nonnegative integers. For example, use the identity embedding of `GL_1` with weights one and two. The author's revised text now handles the positive-degree zero ray by zero constituent polynomials and index zero, and explicitly excludes its isolated origin from the proposition's global-quasi-polynomial hypothesis. The main proposition and its use on nonzero rays are unaffected. This qualification also avoids silently applying the properness argument to the constant Hilbert series `1`.

## Sources directly checked

- Borcherds--Haiman--Reshetikhin--Serganova--Johnson-Freyd, *Lectures in Lie Groups and Quantum Groups*, Part I (2016), Theorem **6.1.1.30**, printed pp. **102--103**. I opened and located the actual theorem and proof at <https://math.berkeley.edu/~serganov/261/part1.pdf>; own retrieval refs `turn898211497view0`, `turn626532291view0`. It states the semisimple Weyl dimension formula for dominant integral highest weight. The extension to reductive groups is justified in the proof under review.
- Supplied GCT VI `sources/LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex`: labels `dintropos1`, `hph1plethysmintro`, `phph2nonstdplethysmrevised`, `hPH3plethysmminimal`, `phph2`, `phph3`, and the subgroup input specification. I also checked the corresponding text extraction `work/positivity_sources/GCTVI.txt`, verifying Hypotheses **1.6.4**, **1.6.6**, **1.6.7**, **3.3.3**, **3.3.4**, Section **3.4**, Theorem **1.6.1(d)**, equation **(4.4)**, Corollary **4.1.5**, and the remark in Section **4.2.2**, printed p. **73**, that PH2 may follow from PH3. This is a source-text inspection, not a new visual inspection of the PDF pages.

## Remaining scope

The proof establishes an implication and an explicit quantitative bound; it does not prove PH3, construct its positive form uniformly, establish the stronger compressed PH1 encoding, or make a historical-priority assertion. No remaining mathematical gap was found in this reviewed version.
