# Spectral and prolate module: review notes

Input A is stipulated. No Lean checker or formal verification of A was run. The module uses only its zeta component; the primitive Dirichlet extension of the strict finite-window argument belongs to AC-T13 in the trace module.

## Main mathematical findings

The strongest quantitative consequence is AC-S05. With L=log(lambda), every fixed r-th eigenvalue of the finite-window closed Weil form satisfies

`0 < a_r(L) <= C_r lambda^(4r+5) exp(-2*pi*lambda^2)`.

The r=1 bound is explicit for lambda>=2, with constant `1024*pi^4*B/c0`, where B is the absolutely convergent sum of reciprocal squared nonzero zero ordinates, with multiplicity, and c0 is the integral of |K|^2 over [-log 2,log 2]. Thus RH implies mu_lambda decreases to zero; the converse is S25 Corollary3.8. Strict positivity under RH was already stated in S21's introduction; compact resolvent and attained minima are S25 results. We claim no priority for those facts.

The test space consists of sharp cutoffs of K,K',...,K^(r-1), not only K. The transforms are polynomial multiples of Xi, hence vanish on the zero multiset. The discontinuities are included in the bounded-variation derivative. Smooth approximants converge in the full logarithmic Weil form norm at rate O(delta log(1/delta)), which justifies the form-domain step. The Gram matrix of the uncut derivatives is positive definite and the cutoff Gram matrices converge, giving the r-dimensional min-max bound.

The kernel coefficient in the supplied S25 equation `ku` gives Xi/4 with its stated Fourier convention. AC-S04 computes the correct normalization explicitly. This scalar does not change the zeros or invalidate a statement allowing arbitrary nonzero normalization.

AC-S13 completes the trial-function convergence estimate, including the Gaussian tail in the E summation: on any closed horizontal strip |Im z|<=b<1/2 the error is O_b(lambda^(b-1/2)). The actual minimum eigenvector is not identified by this estimate. AC-S07 gives a precise additional sufficient gate: a weighted-L1 trial limit and Rayleigh defect small relative to the first spectral gap, with the explicitly displayed window/normalization factor. All fixed low eigenvalues collapse, so a small Rayleigh quotient alone is insufficient.

AC-S06 establishes fixed-window subsequential form and L2 convergence; simple minimum gives full phase-normalized convergence, and evenness makes the finite determinant theorem applicable eventually. The source's boundary normalization requires additional trace regularity and is not silently substituted for L2 normalization.

AC-S08 is an explicit zero-built diagonal Hilbert realization, with exact multiplicities, regularized determinant, and O_R(log T/T) cutoff determinant convergence. It is not an identification with the prime-built geometric spaces or their finite matrices.

Semilocal scaling remains absolutely continuous; a real symmetric polynomial-core prolate expression has self-adjoint extensions by equal deficiency indices, without uniqueness or a claimed zeta spectrum. The finite-prime density deformation prevents the proposed transport of number operators. The printed Jacobi sl2 assignments in S23 have a factor4 commutator defect; corrected compact generator 2(N+c) gives a family, and c=1/4 requires the actual even metaplectic normalization. AC-S12 proves only the imaginary-axis differential-expression/Liouville calculation; it does not identify spectral domains by an illegitimate Hilbert-space analytic continuation.

## Literal attached-source locators

All paths below are relative to `/workspace/scratch/13c475a9e807/sources`.

- S21: `LIT_CC_spectral_triples_zeta_cycles/Spectraltriples.tex`, arXiv:2106.01715, https://arxiv.org/abs/2106.01715 . Proposition2.1 `Hilbert`, Proposition2.3 `Hilbert1`, Proposition4.1 `propDpert`, Proposition4.2 `propDpert1`, Theorem6.4 `spectralreal`, Corollary6.5 `repetitions`. Its source contains inactive/older duplicated material later in the file, so references use the active main text.
- S22: `LIT_CC_Hochschild_trace_zeta_cycles/Hochschild-zeta.tex`, arXiv:2207.10419, https://arxiv.org/abs/2207.10419 . Theorem1.2 `spectralreal1intro`, Proposition4.2 `laplacian`, Corollary4.3 `rhequiv`, Theorem5.4 (its label `spectralreal1` is commented out), Remark `remtauto`. The local quotient and nilpotent action are explicitly in the proofs.
- S23: `LIT_CCM_zeta_zeros_prolate/mainc2m24fine.tex`, arXiv:2310.18423, https://arxiv.org/abs/2310.18423 . `prolop`, `httransfo`, `numberN`, `fourierfmuall`, `groundstate`, `httransfoS`, `tauS`, `hermsemiloc`, `care`, `isosonin`, `propbb`, `wlambdconj1`, `h`, `hhk`, `aak`, `eplusminusricu`, `coefffixed`, `dzero`, `b-k`. The source's theorem and proposition counters differ; literal labels avoid false renumbering.
- S25: `LIT_CCM_zeta_spectral_triples/mc2arXiv.tex`, arXiv:2511.22755, https://arxiv.org/abs/2511.22755 . Proposition3.3 `Hilbert`, Proposition3.4 `Hilbert1`, Proposition3.5 `compres`, Theorem3.6 `thmsmallest`, Corollary3.7 `lowest`, Corollary3.8 `strange`, `monotone`; Definition5.3 `even-simple`, Lemma5.4 `key`, Theorem5.10 `finmain`; section7 `outlook`, `mhat`, `ku`, `emap`, Lemma7.1 `hermfact`, Lemma7.2 `meixnerlem`, Lemma7.3 `hermfact1`; section8 `missing`.

## Primary external references used

- Carneiro, Chandee, Milinovich, *Bounding S(t) and S1(t) on the Riemann hypothesis*, https://arxiv.org/pdf/1309.1526 . Equation(1) is the zero-counting formula and Theorem2 (PDF p2) bounds S(t) by `(1/4+o(1))*log(t)/loglog(t)` under RH. Its jump gives the multiplicity bound used in AC-S03. The count of distinct ordinates, not only the count with multiplicity, is essential.
- Optional alternative for the same Jensen contradiction: Conrey, *At least two fifths of the zeros of the Riemann zeta function are on the critical line*, Bull.AMS20(1),1989, Theorem1,p79; author copy https://aimath.org/~kaur/publications/21.pdf . Primary search returned the theorem; direct opening failed. The main written RH proof can use the fully opened 1309.1526 source instead, so this optional reference is not required.
- Connes--Moscovici, *The UV prolate spectrum matches the zeros of zeta*, PNAS119(22),2022,e2123174119, https://doi.org/10.1073/pnas.2123174119 . Author-hosted March3,2022 draft: https://alainconnes.org/wp-content/uploads/PNAS_030322.pdf . Theorem1.6 and Corollary1.7 give the classical operator facts. Theorem5.1 and equation(33) need version/normalization care; see the unchecked file. Earlier version: https://arxiv.org/pdf/2112.05500 .
- Ramis, Richard-Jung, Thomann, *New eigenfunctions for the negative part of the Connes--Moscovici prolate spectrum*, C.R.Math363(2025),1065--1081, https://doi.org/10.5802/crmath.780 . Primary article https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.780/ ; PDF https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.780.pdf . Theorem14 gives the imaginary-axis characterization with a parity exchange; Corollary15,p1076 proves all nonclassical eigenvalues negative. Proposition16 states an entire determinant of order at most1/2; its zero simplicity is conjectural, so it is not imported as proved.

## Checks actually performed

The new proofs AC-S01--AC-S13 were read in full and checked manually, including multiplicity, normalization, interval length, endpoint jumps, form norm, min-max dimension, phase choices, and operator domains. The symbolic certificate script checks the finite algebra only. It is not a numerical or formal proof of the analytic assertions. The script and its JSON output are included under `scripts/` and `evidence/`.

The initial pdflatex attempt failed because the executable could not find its format/config files. Setting `TEXMFDIST=/usr/share/texlive/texmf-dist` and `TEXMF=/usr/share/texlive/texmf-dist` restored lookup and allowed a local format build. Root owns final compilation. No successful final-document compilation is claimed by this note.

No Grothendieck archive cote was supplied or verified for these analytic statements; none is invented. The local-jet/associated-graded discussion distinguishes an analytic topos representation from finite-field etale cohomology and its weight formalism.
