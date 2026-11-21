# Independent complete proof review: R-35

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Actual review completed: 2026-11-21 06:48:23 UTC.

Reviewed file: `work/rectangular/r35_fragment.tex`, SHA256 `7eb8eaab5cd91fc8be425f5b2291384fd1dca8ca296619dd01d29ac267a32189`.

**Outcome: PASS, complete written proof read and its new deduction independently rederived, using the cited classical Behrend bound as an input.**

The floor defining L gives 3L+2 at most (m-1)/2, so both sides of a modular progression relation lie in the same interval from zero to m-1. Hence the relation is an ordinary integer equality, including the equal-endpoint case when m is even. The two possible mixed progressions are both excluded by the displayed bounds: a small middle term cannot have a translated endpoint, and a translated middle term has doubled value at least 4L+6 while any endpoint sum involving a small term is at most 3L+3. The shifted set therefore preserves the full strong modular condition and retains zero and one.

Its Cartesian square has the same condition, contains the three required Fermat labels, and every retained-label subset gives the stated row counts via the fully checked R34 theorem. For large m, L is at least m/7 (for example the elementary floor estimate already suffices for m at least 77). Squaring the cited Behrend bound, using log L at most log m, and absorbing the factor 49 into the absolute exponential constant gives the exact nearly quadratic lower bound. The upper bound follows from the interval size and is strictly below m squared. The fixed-delta consequence follows once sqrt(log m) is at least C/delta.

The proof correctly retains separate permanent/determinant witnesses and makes no unpadded rectangular period-one or fixed-positive-density assertion. I did not reopen Behrend's original pages during this review; their exact theorem and author-recorded primary reading are treated as the stated established input. No new density estimate, historical-priority claim or numerical computation is certified here.
