# Independent review: integral cubic exceptional lattice

Completed: 2026-11-19T15:05:34.758696+00:00.
Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not exposed.

## Reviewed material and decision

Full current `agents/cycles/exceptional_cubic_lattice_draft.tex`, its entire retained Python certificate, and the aggregate plus all nine case summaries of the current JSON output were read. **PASS** for the auxiliary integral Chow assertion: for two smooth cubic surfaces and any line bundle on a smooth projective curve, multiplication by the stated L is injective from CH^2(P^1×W1×W2×C) to CH^3. This is an auxiliary check for C.3bk; it does not certify the combined local counterexample by itself.

## Complete proof check

1. A cubic is the blow-up of P^2 in six points over the algebraically closed field. Apply the integral codimension-two blow-up formula after product with an arbitrary smooth scheme T. The centre is point×T, its normal bundle is a constant rank-two bundle, and the exceptional new summand is exactly E_i×CH(T). The projective-bundle formula and self-intersection give the stated integral external-product ring, not a general Kunneth assertion.
2. For gamma=gamma0+h gamma1 and h^2=0, L gamma=0 implies gamma0=-c gamma1 and c^2 gamma1=0.
3. The Picard decomposition gamma1=d1+d2+lambda is integral. The pure cubic degree-three terms are 3 d2+2(a.d1)b and 3 d1+2(b.d2)a. Pairing gives 2x+y=x+2y=0 over Z. Thus x=y=0, and torsion-free cubic Picard lattices give d1=d2=0.
4. The remaining pure coefficients give 3 lambda=0. A coefficient E_i×E_j in a×b is one, so the mixed term gives 2 lambda=0. The Bezout identity 3-2=1 kills lambda in the full Picard group, including every p-primary torsion element. No integer is reduced modulo the characteristic.

## Fresh exact primary-source inspection

* Jiang, published Cambridge primary HTML, Section 1.2 conventions, Theorem 2.4 with its displayed maps and proof, and Section 2.3/Theorem 2.8(3) with its displayed maps and decomposition. The ground field is unrestricted in the conventions. The blow-up theorem applies to a codimension-r locally complete intersection centre; our smooth point-product centres satisfy that hypothesis. URL: https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/on-the-chow-theory-of-projectivizations/3DA5197C99935D82CCB4E359214AF439 . Fresh retrievals `turn514555530view0`, `turn514555530view1`, `turn457846617view0`, `turn457846617view1`.
* Stacks, Lemma 42.36.2, Tag 02TX, full statement and proof freshly read: https://stacks.math.columbia.edu/tag/02TX . Retrieval `turn457846617view2`.
* Huybrechts, Chapter 4, Proposition 2.4, p.178: the all-characteristic cubic blow-up description is a prior independently read input from C.3bi/bj; no fresh reopening in this short review is claimed.

## Finite computation scope

The current certificate started at 2026-11-19T15:03:32.933566+00:00 and reports 31 passes, zero failures, runtime 0.7236748529976467 seconds. I read the full program and all nine case summaries, without rerunning it. The six-case earlier output read before compaction is superseded by this explicitly identified nine-case expansion. The raw multiplication matrices are retained by the author; I did not manually inspect every entry of the largest sparse matrix.

The code uses the exact integral cubic basis, integral unit row/column elimination, then exact Smith normal form. All six original and three added m=0 cases are full column rank. In particular r=3,m=1 has 15 unit Smith entries; r=3,m=0 has one factor 3; r=4,m=1 has factors 3 and 9. These finite observations do not establish integral Lefschetz in arbitrary degrees. They are consistent with, and not substitutes for, the complete r=3,m=1 proof above.
