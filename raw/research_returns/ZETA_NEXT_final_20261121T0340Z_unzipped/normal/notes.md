# Normal-field investigation

## Settled quantitative route

- NX01: kappa_K > 1/(173 log D_K) for every normal K != Q under the supplied Alpoge theorem. Exact constant is 4 C4, where C4=2 exp(21/8+(gamma+2 log 2)/(4 log 3)).
- NX02: arbitrary degree n fields get 1/(173 n! log D_K). Galois-closure discriminant comparison uses Stark Lemma 7; zero transfer uses Aramata--Brauer, as in Stark Lemma 8's proof.
- NX03: combine with Louboutin 2001 Theorem 1(1) to get explicit two-sided Brauer--Siegel and the normal-family asymptotic.
- NX04: unconditional Minkowski class-number upper bound separates the earlier sufficient-power application from the new lower-bound result.

## Source verification

Stark original volume downloaded from GDZ, article extracted from PDF scans 142--159. Visually inspected printed pages 138--141, 143, 145--146, 148. In particular Lemma 8 is p145 and Theorem 1' p148, so both requested locators are confirmed. Lemma 9 is about real zeros of the quotient zeta_K/zeta_k, not every zero of zeta_K.

Garcia--Lee arXiv:2007.10313v4 section 3 pp16--17 confirms C4=43.1621149807...; its separate concern about c8=pi/6 is irrelevant to the zero-excluded branch used here.

## Routes tried

1. Direct source extraction: first article-specific URL returned 404; GDZ volume worked. Text absent in image PDF, so source constants were verified visually from rendered pages.
2. Independent Hadamard-product estimate: a disk free of zeros of radius 1/(4G logD) gives a safe weaker residue constant e^-7/(4G logD), using termwise comparison of positive real parts in the logarithmic derivative. Superseded by the stronger checked Stark constant; not promoted as an extra finding or as an independent re-proof of Stark.
3. Modern residue literature: Garcia--Lee gives the exact usable C4. The c8 branch was expressly not imported.

## Completed proof checks

The complete NX01--NX04 proofs were reread by their author and independently read by the CM agent; see the merged CHECK_EVENTS.tsv and cm/normal_review.md. The Louboutin primary-source upper bound was checked, and its bibliography alias corrected. The printed Stark locators and original constants were inspected as described above. No mathematical gap remained in these statements. The exact rational script audit/check_stark_constant.py independently certifies the numerical inequality 4*C4<173; it does not formalize Stark's theorem.
