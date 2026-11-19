# Independent C.1f, C.4, and E.3e review

Agent: /root/frobenius  
Date: 2026-11-19  
Parent/master files were not edited.

## 1. C.1f incidence blow-up induction

**Independent check passed.** We checked the complete induction in
../cycles/cycles.tex, including the explicit blow-up projections added
to the current version.

If \(X_{2i-1}\) is a smooth Cartier divisor in a smooth Tate-motive
\(R_{2i}\), then \(X_{2i-1}\times\{0\}\) is the regular zero scheme of the
two-component section of
\(\operatorname{pr}_1^*O(X_{2i-1})\oplus\operatorname{pr}_2^*O(1)\) on
\(R_{2i}\times P^1\). The incidence equation in the projective bundle of
lines is exactly the Rees-algebra presentation of its blow-up. Thus the
new blow-up is a smooth Cartier divisor in a Tate-motive ambient variety
of one higher dimension. There is no unsupported small-codimension
embedding claim.

For the codimension-two centre, the blow-up formula and its displayed
forward/inverse maps are correctly typed. The exceptional self-intersection
has the required minus sign; its pushforward is the identity on the
centre. These algebraic correspondences preserve algebraic equivalence.
The unique Griffiths summand therefore moves from degree \(i\) to
\(i+1\), while the ambient part stays finite dimensional. Multiplication
by projective space gives the claimed string of Griffiths groups in
degrees \(i+1,\ldots,n-i\). The source in degree \(i\) remains finite
dimensional and the target in degree \(n-i\) infinite dimensional.
This validates all \(1\le i<n/2\).

## 2. New C.4 deliverables and proved results

C4_additions.tex contains C.4h–l and an unnumbered remaining-work paragraph.
C4_references.bib adds only the two
new keys; the other keys already occur in the cycles bibliography.

1. Scalar factorizations through finite products of Jacobians form
   an ideal \(I_J(A)=s_J(A)\mathbb Z\). Its generator is one exactly when
   \(A\) is an actual direct summand. Duality preserves it and products
   take the least common multiple.
2. In every characteristic, \(s_J(A)\mid(2g-1)!\). This follows from the
   explicit integer composite in Scavia–Suzuki Proposition 3.4,
   applied to the Poincaré line bundle on \(A\times\widehat A\).
   No unproved integral Hodge conjecture is used.
3. For \(g\le3\), \(s_J(A)\) also divides
   \(\delta(A)=\gcd_{L\in\mathrm{Pic}(A)}\chi(L)\). Mumford's group-scheme
   principalization has degree \(\chi(L)\), and Oort–Ueno identifies the
   principally polarized quotient with a product of Jacobians.
4. Consequently
   \(s_J(A)\mid\gcd((2g-1)!,\delta(A))\).
   Different polarizations may be used at different primes. A finite
   Bézout combination of the resulting maps gives one exact retraction.
5. Surface case: the sufficient local checks are at 2 and 3. Threefold
   case: 2, 3, and 5. The check at the characteristic is retained for
   characteristic 2 or 3. We use group-scheme kernels throughout.
6. A surface with NS rank one and primitive type \((1,d)\) is settled
   whenever \(\gcd(d,6)=1\). For a complex threefold with primitive type
   \((1,d_2,d_3)\), the sufficient test is
   \(\gcd(d_2d_3,30)=1\).
7. For NS-rank-one complex surfaces with End equal to \(\mathbb Z\),
   the identity coefficients obtainable from products of divisors
   on \(A\times\widehat A\) form exactly \(\gcd(6,d)\mathbb Z\).
   This is a limitation of that subring, not a counterexample for all
   algebraic curves.

The strongest isogeny formulation retains kernel exponents: if
\(A\to B\) has kernel killed by \(e\), then
\(eI_J(B)\subset I_J(A)\) and conversely. For a separable polarization
of type \((d_1,\ldots,d_g)\), one may use \(e=d_g\). Inseparable cases
use the actual kernel group scheme, or the always valid degree bound.

## 3. What remains unproved

### Priority and targeted-search record

No priority or novelty claim is made for the factorial bound, the
scalar-factorization ideal, or the polarization gcd criterion. These are
elementary quantitative deductions from the opened Matsusaka formula,
principalization, and the low-dimensional Jacobian theorem. Searches for
the exact direct-summand formulation and its nonprincipal surface and
threefold variants found Beckmann–de Gaay Fortman, Voisin, and
Scavia–Suzuki; their exact theorems are identified above. The search
neither established that these elementary deductions are new nor
established a published resolution of every residual small-prime case.
Accordingly we record them as proved deductions and reserve every
priority judgment.

We have not shown that every nonprincipally polarizable surface or
threefold has \(s_J=1\), nor produced one with \(s_J>1\). In particular,
the computations do not settle generic type \((1,2)\) or \((1,3)\)
surfaces.

The following proposed shortcuts were checked and do not close the gap:

- Integral Hodge for curves on \(A\) alone: the converse to the
  direct-summand condition in the opened theorems requires a unimodular
  line bundle. Without one, the criterion is on \(A\times\widehat A\).
- All rational Hodge classes are generated by divisors: rational
  generation does not imply integral generation; the explicit
  divisor-product lattice has the residual index above.
- Choosing many principalizations: if \(\ell\mid\delta(A)\), no
  prime-to-\(\ell\) isogeny from \(A\) to a principally polarized
  variety of the same dimension exists. Pulling back the principal
  polarization would contradict the definition of \(\delta(A)\).
  Thus merely varying these quotients cannot remove that prime.
- Zarhin's trick: the principalizable product has dimension \(8g\),
  so the dimension-three Jacobian theorem no longer applies.
- Engel–de Gaay Fortman–Schreieder 2026: the opened theorem concerns a
  very general ppav of dimension at least four. Its hypotheses do not
  automatically include the restricted family \(A\times\widehat A\).
  A separate degeneration argument is necessary.
- Rational Tate results for abelian varieties over finite fields do
  not themselves supply integral all-prime curve classes or eliminate
  the characteristic-prime condition in Scavia–Suzuki.

These statements distinguish a proof gap in this contribution from a
claim that the cases are known to be open in the literature. Further
non-divisorial degeneration or geometric constructions remain under
investigation at the parent's request.

## 4. Finite calculation

Run:

    python research/agents/frobenius/code/verify_c4_exterior.py

Output:

- output/verify_c4_exterior.json
- output/verify_c4_exterior.txt

The script computes in the exact exterior algebra over \(\mathbb Z[d]\).
It checks the factorial normalization for dimensions 1–4, verifies
\(D\widehat D P=-dP^3/6\), and computes the cross component of all ten
degree-three divisor monomials. Only the coefficients \(6\) and
\(-d\) are nonzero. It also checks three finite Bézout examples.
This is a certificate for the stated lattice calculation, not a
computation of the full Chow group.

## 5. E.3e independent review

**Independent check passed.** We checked
../cycles/effectivity_albanese.tex, E.3e, and independently opened
Bloch's original 1979 paper.

The repair from generator-wise torsion to specialization of the
entire torsion relation is valid. Spreading the Albanese map alongside
the parameter variety avoids assuming that formation of Albanese is
unchanged without verification. Integral \(H^1\) base change makes
\(\mathrm{Alb}(T_s)\to B_s\) a prime-to-\(\ell\) isogeny, so the
specialized degree-zero cycle has prime-to-\(\ell\) Albanese class.
Over \(\overline{\mathbb F}_p\), its Chow class is torsion. Roitman's
prime-to-\(p\) theorem kills its \(\ell\)-primary component. The total
specialized relation remains \(\ell\)-primary, hence is zero. Bloch
Proposition 3.8 then kills the generic torsion Abel–Jacobi class.
Propositions 3.5 and 3.9 and Theorem 4.2 justify the final application
to an abelian parameter variety. Taking Tate modules causes no
additional torsion issue because the source is an abelian variety.

Only editorial suggestion sent: replace “choose finitely many
expressions” by “choose an expression” before \(z=\sum W_*\nu\).

## 6. Opened-source ledger

Every source below was independently opened by this agent for this
review; the exact portions were read. Source discovery pages alone
were not treated as proof sources.

| Citation key | Primary source and opened locator | Web reference |
|---|---|---|
| cyScaviaSuzuki2025 | https://arxiv.org/html/2507.09821v2, Theorem 1.1 and following paragraph; Proposition 3.4, especially (3.1)–(3.3); proof of Corollary 1.3 | turn358199100view1; turn730273396view3 |
| cyBeckmannFortman2023 | https://www.cambridge.org/core/journals/compositio-mathematica/article/integral-fourier-transforms-and-the-integral-hodge-conjecture-for-onecycles-on-abelian-varieties/AC12934E24BDAA5B2CD04372A3090416, Theorem 1.1; Proposition 4.5; Theorem 5.2 | turn163112525view2; turn358199100view0 |
| cyVoisin2024 | https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/PAMQ-20-5-a14-VOISIN.pdf, Theorem 1.4; Proposition 2.1, Remark 2.2, Corollary 2.5 | turn558734681view1; turn219171750view1 |
| frC4Mumford1970 | https://djvu.online/file/2tC7xp3dbqGCh, §23 Theorem 2 and corollary p.231; Theorem 4 pp.233–234; Corollary 1 p.234. Page images 119 and 120 opened and visually checked | turn877907092view0; turn896973874view1; turn896973874view2 |
| frC4Milne1986 | https://jmilne.org/math/xnotes/AVs.pdf, corrected 2022 text, §8 after Proposition 8.1 p.12; Remarks 16.12–16.13 p.34 | turn942895776view1; turn626959589view0 |
| cyOortUeno1973 | https://ir.cwi.nl/pub/27912/27912.pdf, Theorem 4, printed preprint p.2 (PDF p.3). The CWI file is a preprint, not the published pp.377–381 layout. Local page rendering corrected the earlier mistaken p.381 locator; see C4_prym_REVIEW.md. | turn843934373view0; turn626959589view2; local output/oort-title-3.png |
| cyEngelFortmanSchreieder2026 | https://arxiv.org/html/2507.15704v3, Theorem 1.1, Corollaries 1.2 and 1.5, Theorems 1.6–1.10 | turn896973874view0 |
| cyBloch1979 | https://www.numdam.org/article/CM_1979__39_1_107_0.pdf, Proposition 3.5 p.115; Proposition 3.8 pp.117–118; Proposition 3.9 pp.118–119; Theorem 4.2 p.119 | turn595124458view0; turn353797351view0 |

Discovery/auxiliary cross-check opened but not needed in the final
proof: Brian Conrad, Polarizations, p.9, cites Mumford Corollary 1
p.234; https://virtualmath1.stanford.edu/~conrad/vigregroup/vigre04/polarization.pdf,
turn730273396view2. William Stein's Mumford scan index was opened,
but its 83 MB PDF exceeded the web tool limit; the readable primary
scan and page images above replaced it.
