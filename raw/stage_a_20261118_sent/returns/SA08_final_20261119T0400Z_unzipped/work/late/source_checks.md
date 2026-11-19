# Additional primary-source checks

2026-11-19; GPT-6 Astra Pro; effort not exposed by runtime; SA08/late.

## SGA4 III

Downloaded the original scan from https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-3.pdf (45,109,645 bytes) to `work/late/sga4-3.pdf`. Rendered PDF377 and378 with `pdftoppm -f N -l N -scale-to 2000 -png -singlefile` and inspected the images. PDF377 is published374, XVII internal123, not published372 as the preliminary estimate suggested. XVII5.5.2.4 states Gamma and symmetric tensors commute with filtered colimits and preserve free/flat modules. 5.5.2.5 gives Gamma^n(M)→TS^n(M) and explicitly says it is an isomorphism for finite free, hence flat M. PDF378/published375 has the direct-sum splitting 5.5.2.6, base change5.5.2.7, and the bilinear pairing5.5.2.8. These are the exact ingredients used in the flat convolution repair, not a verbatim statement of the assembled Hom theorem.

## Garvin et al. 1998

The web fetch returned403, but `urllib.request.urlretrieve('https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf', 'SA08_work/work/late/Garvin1998.pdf')` succeeded (269,119 bytes). `pdftotext -layout` produced `Garvin1998.txt`; all8pages169–176 were read. Proposition3.1pp173–174 proves the fixed-length Poincare lemma over any commutative unital coefficient ring. Proposition3.2pp174–175 proves q-extendability. Remark3.3(i)p175 explicitly gives failure of(q+1)-extendability through the volume form in degree q. Theorem4.1p175 and Theorem4.2p176 use **p<q**, and4.2 is for every simplicial set K. It uses normalized integration q! times the ordinary integral. The following Theorem4.3 says 'up to degree q'; this imprecise wording is not used to assert the boundary p=q beyond the preceding exact theorem. Introductionpp169–170 distinguishes Miller's finite-complex result from Cartan§7's arbitrary-simplicial sketch. Publication1998; no separate first-circulation date established. Full source is now verified, superseding earlier access-limit notes in raw search logs.

## Limited accesses

The same urllib attempt for Tate1967 at the Boston University URL returned503; Gressman's lecture page returned403. Their mathematical statements are not promoted to full-text verification from search snippets. The original SGA7 quotations of Tate remain verified as source dependencies; an exact modern theorem or historical original must be distinguished from those quotations.

## Quantifier correction

The new F2 uniqueness counterexample for scan324 checks composition for p,q>=1 and products also at zero. If the author intended the q=0 composition constraint, the example fails its augmentation condition. The proof memo and claim C257 explicitly state this boundary. Full additive naturality on all coefficient modules is also not satisfied by that alternative family. This is a bounded counterexample, not an unconditional rejection of an unspecified uniqueness convention.

## Nonlinear normalization and the late universal-property comparison

The original Breen–Mikhailov–Touzé article was opened at
https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf. Proposition3.5 and Corollary3.6
on printedp270 were read with their actual hypotheses: a finitely generated
projective module over a commutative ring for the displayed décalage
isomorphisms. The independent calculation in
programs/late_quadratic_normalization.py gives
N Gamma²(Psi) = [k --(-2)→ k] in degrees2→1. It does not follow merely
by treating Gamma as additive. The ordinary-K interpretation of scan239
is therefore withdrawn; the diplomatic Pi/K alternative is retained.

Touzé's The universal property of strict polynomial functors,
arXiv2607.00631, first posted1July2026, was opened and the introduction
pp1–5, including the statements of Proposition1, Example2, Lemma3,
Definition4, Theorems5 and9, and Remark11, was read. No complete proof
read is claimed. Its ground-field, exact-tensor and target-category
hypotheses make this a bounded comparison to the programme on315–325,
not a theorem identifying the manuscript's unspecified arbitrary-ring
operation category. Exact queries and returned source text are saved in
research/late_web_029.json through late_web_032.json.
