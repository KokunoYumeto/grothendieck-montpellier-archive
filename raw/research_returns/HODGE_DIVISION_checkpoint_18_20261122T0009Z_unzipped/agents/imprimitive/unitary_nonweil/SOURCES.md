# Sources for D-UNW-01–03

Author: `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION. Recorded from the clock at **2026-11-21 20:04:20 UTC**.

## Larsen–Tiep, 2024

**Published result:** M. Larsen and P. H. Tiep, *Uniform character bounds for
finite classical groups*, Annals of Mathematics 200 (2024), 1–70,
DOI `10.4007/annals.2024.200.1.1`.

Publisher record read:
https://annals.math.princeton.edu/2024/200-1/p01 . It records acceptance on
12 March 2024 and online publication on 3 July 2024. The author's selected
publication list independently identifies the publication:
https://sites.math.rutgers.edu/~pht19/papers_selected.html .

Full text actually read: accepted author version, dated 14 March 2024,
https://arxiv.org/pdf/2403.09046 . The local copy is in `cache/`, 616335 bytes,
SHA-256 `70d2546d2a0f01f8e701aa718201216f2b334b6cd074c12b41c2c59e0b7cdd4f`.
Theorem 4.4 and its complete proof, numbered pp. 19–20, and Theorem 5.5
and its complete proof, numbered pp. 25–26, were read. The displayed
constant on p. 26 was also visually inspected in a rendered page.

The used input is the exact theorem with
`sigma = 1/(6507*2^21*10^18) > 7*10^-29`. The new proof safely uses
`sigma0=10^-29`. Its extraction is independently checked by integer
arithmetic in `check_constants.py`. The supporting constants are
`C=2^14*10^12`, `gamma=1/(2^13*10^12)`.

**Boundary:** attempts to obtain the typeset journal PDF did not succeed:
two guessed publisher URLs returned 404 and a JSTOR attempt returned HTML.
The exact outcomes are retained in `publisher_attempts.json`. The new
proof cites author-version page locators and verified publication metadata;
it does not claim a journal-page-image read or a new proof of the cited
classification/counting inputs inside the published theorem.

## Guralnick–Larsen–Tiep, 2020

**Published full text actually read:** R. M. Guralnick, M. Larsen and
P. H. Tiep, *Character levels and character bounds*, Forum of Mathematics,
Pi 8 (2020), e2, 81 pages, DOI `10.1017/fmp.2019.9`.

https://www.cambridge.org/core/services/aop-cambridge-core/content/view/77A6CCCB36F94337FD1DAA7F67B40379/S205050861900009Xa.pdf/character_levels_and_character_bounds.pdf

The local publisher PDF has 848881 bytes and SHA-256
`0726271e666bd5eb736ff91ea031ef83bb072f2e10f27b664c217d7702926c32`.
Fresh complete reads covered Definition 2 and Lemma 7.1 (pp. 51–52),
Theorem 7.3 with proof (p. 52), the entire unitary dual-pair argument
in §8.3 (pp. 65–67), and Corollary 8.6 with proof (pp. 67–68).
Theorem 1.3's displayed denominator on p. 4 was visually inspected:
the unitary lower bound uses `1/[2(q+1)]`.

The essential new low-level calculation uses exact (8.18), p. 66,
and its tail estimate (8.17), p. 65. The complete argument verifies
the even-q range `j^2+j <= n-1`, the irreducibility and exhaustion of
the true-level characters, and the same-degree extension of an SU
character at level `j<n/2`. This avoids using the weaker 2.43 corollary
at the problematic-looking endpoint q=2, level 2.

## Cover classification and previously reviewed bridges

Hiss–Husen–Magaard, *Imprimitive irreducible modules for finite
quasisimple groups*, Memoirs AMS 234 (2015), no. 1104,
DOI `10.1090/memo/1104`; author version
https://arxiv.org/pdf/1211.6350v2 . The ordinary-cover paragraph on
numbered p. 4 and complete exceptional-multiplier list, Chapter 5,
Table 1, p. 35, were freshly reread from the shared full author text.
No listed unitary exception has natural dimension above six.
The standard universal-cover interpretation outside this complete
exception list is used as the same known classification input already
reviewed for D-BI-19/20.

The actual intermediate Hurwitz factorization, polarized Shapiro
comparison and Euler identity are the previously proved source bridge.
D-BI-19 supplies transitive quasisimple factors in the primitive
factorwise tensor-indecomposable case. D-BI-24 excludes the large-rank
unitary Weil alternative; D-BI-20 supplies q<=27 only in its stated
nonsplit main-source scope. Those hypotheses have not been widened.

## New proof and computation scope

`unitary_nonweil_section.tex` contains the complete new argument and
its explicit limits. `check_constants.py` is an exact rational/integer
certificate of the constants and polynomial reductions. It has actually
run and passed. It does not enumerate the enormous finite range, check
all character tables, or replace the universal proof by sampled ranks.
No independent peer review is claimed at this author freeze.
