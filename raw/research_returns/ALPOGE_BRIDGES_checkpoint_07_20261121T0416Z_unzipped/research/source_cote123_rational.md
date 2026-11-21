# Cote 123: rational singularities of all adjoint-quotient fibres

Run: /root/source_and_masullo within ALPOGE_BRIDGES. Model: GPT-6 Astra Pro. Effort: not exposed. Date: 21 November 2026 UTC.

## Result and exact original scope

Finding **F-SM-23**, completely stated and deduced in source_cote123_rational.tex, closes the rational-singularity question in Grothendieck's letter to Kostant dated 22 October 1969. The original begins in the complex setting, physical page 22 / handwritten page 21; the question appears on physical page 23 / handwritten page 22. It covers the fibres of the Lie-algebra adjoint quotient and, for a simply connected group, the group adjoint quotient. Its criterion is the vanishing of the higher direct images of the structure sheaf on a resolution.

This is a classical affirmative result. The contribution here is exact attribution and a complete short reduction of the group statement to the established unipotent theorem. It does not depend on Alpöge, Masullo, GRH, a positivity assumption, or an unproved interchange of operators. No positive-characteristic or general non-simply-connected extension is claimed.

## Checked primary inputs

| Input | Exact locator and role | Primary source |
|---|---|---|
| Lie-algebra fibres | Kraft–Procesi (1982), §0.3 p.540: reduced normal complete intersections. §0.4 p.540: these fibres have rational singularities. §0.2 explicitly begins with a reductive complex group, so the introductory assertion is not limited to the paper's later classical-group classification. | [Primary paper PDF](https://www.math.utah.edu/~ptrapa/math-library/kraft-procesi/kraft-procesi.pdf); [publisher DOI](https://doi.org/10.1007/BF02565876). |
| Semisimple-part map | Kraft–Procesi, §0.2 pp.539–540: the algebraic map from a conjugacy-class closure to its closed semisimple class, with the fibre identified in the centralizer. | Same primary paper; both pages visually inspected. |
| Nilpotent/unipotent rational singularities | Hesselink (1976), Theorem A and §2 p.249: proper smooth birational resolution with direct image O and no higher direct images, for a split reductive group in characteristic zero. §2 constructs the equivariant Springer resolution. | [Publisher-version author repository PDF](https://pure.rug.nl/ws/files/3449114/1976MathAnnHesselink.pdf); [DOI](https://doi.org/10.1007/BF01360956). |
| Group fibre geometry | Steinberg (1965), Theorem 6.1(b) p.62; Theorem 6.11 p.64; §6.16 p.65; Theorem 8.1 p.70. These supply the r coordinate equations, codimension r, the unique dense regular class, codimension-two complement, and full Jacobian rank there. Reducedness and normality follow by the written commutative-algebra argument. | [Numdam primary PDF](https://www.numdam.org/item/PMIHES_1965__25__49_0.pdf); [DOI](https://doi.org/10.1007/BF02684397). Pages 62, 64 and 70 also visually inspected. |
| Semisimple centralizer | Steinberg (1965), §2.7 and Remark 2.10 p.53. The latter explicitly states connectedness for simply connected groups, with its proof deferred. This is an adopted established structural input, not a reconstructed proof. | Same primary paper. The later full Steinberg 1968 source was identified, but its primary PDF returned 403; no claim to have read that proof is made. |
| The particular resolution | Steinberg (1976), Corollary 6.4 p.223, attributed to Grothendieck: the multiplicative simultaneous-resolution fibre is a desingularization of a regular-class closure. | Local primary PDF and OCR in research/root_sources; [DOI](https://doi.org/10.1007/BF01390010). |
| Independence of resolution | Glazer (2019), §2A p.488, explicitly states equivalence of the criterion for some and for every resolution, citing KKMSD I.3 pp.50–51. | [Primary journal PDF](https://msp.org/ant/2019/13-2/ant-v13-n2-p07-s.pdf); [DOI](https://doi.org/10.2140/ant.2019.13.485). |

Hesselink's exact theorem and construction were inspected in the primary PDF text, not inferred from a search snippet. genui{"citation":{"ref":"turn877965077view0"}} Steinberg's theorem statements were checked against the primary article and the relevant page images. genui{"citation":{"refs":["turn586115391view0","turn586115391view1","turn586115391view2","turn586115391view3"]}} The Kraft–Procesi and Steinberg 1976 DOI metadata were checked against the publisher. genui{"citation":{"refs":["turn684166019view0","turn684166019view1"]}} The resolution-independence formulation was checked directly in Glazer. genui{"citation":{"ref":"turn581915126view1"}}

## Complete deduction and its nontrivial checks

For the group fibre F, the r equations in the smooth group form a local regular sequence because their height is r. Thus F is Cohen–Macaulay. Steinberg's differential criterion makes it generically reduced, so there are no nilpotents; the codimension-two singular complement then gives normality by Serre's criterion.

Choose the unique semisimple closed orbit represented by s, and put L = Z_G(s). The semisimple-part morphism identifies F with the associated variety G ×^L U(L). The statement is scheme-theoretic: its pullback to the smooth torsor G → G/L is G × j⁻¹(s), which is reduced; descent makes the fibre reduced as well.

The L-equivariant Hesselink resolution of U(L) induces a resolution of this associated variety. Étale locally on G/L it is a product with the original resolution. Flat base change therefore transports both the degree-zero direct image and every higher-direct-image vanishing. Faithfully flat descent returns those assertions to F. Independence of resolution applies the result to the precise resolution mentioned in Steinberg's Corollary 6.4.

The source statement “there is a desingularization” is kept distinct from the vanishing of its higher direct images. The latter does not follow merely from having constructed a resolution.

## Checking status

The drafter performed a complete rereading of the full written deduction and its hypotheses on 21 November 2026 at 00:33:55 UTC. The record is a targeted whole-proof self-check of the deduction, plus direct checking of the named primary statements. It is not an independent reproof of the classical theorems or a formal kernel check. Root was asked to perform an independent whole-proof reading.

The bibliography with full APA entries is included in the TeX module. The downloaded source PDFs are research references; no wholesale reproduction of them is necessary in the final deliverable.
