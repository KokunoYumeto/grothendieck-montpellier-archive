# C.3bf: exact source and validation record

Final mathematical scope: **k = algebraic closure of F5 and every N >= 4**. The specified deformation of the Segre cone has an injected (Z/5)^3 in the ordinary integral Picard restriction kernel. Ordinary equivalence is realized by actual fixed-product proper-curve line-bundle families. No rational failure, extension to another characteristic, dimension-three assertion, or higher Chow-product nonvanishing is included in this result.

Final proof: `C3_integral_picard_kernel.tex`. The draft filename is a comment-only supersession record. The result was registered at **2026-11-19T13:56:53.521192+00:00** after complete parent and two peer reviews. The parent recorded scheduled review9 as YES at13:57:12, precisely for this integral degree-one change.

## Newly opened primary inputs

| Key | Exact inspected source and locus | Scope used |
|---|---|---|
| D_BrionIsogenyII | Michel Brion, *Commutative algebraic groups up to isogeny. II*, full35-page author revision at https://www-fourier.univ-grenoble-alpes.fr/~mbrion/isogeny_II_rev.pdf; Section3.2.3, equation(3.8), authorp23. The arXiv metadata identifies v2,11April2017, arXiv1612.03634v2. The author's publication list identifies Contemporary Mathematics705(2018),1–36. | Bifunctorial Ext1(A,Ga)=H1(A,O). This displayed statement and its following positive-characteristic paragraph occur BEFORE the subsequent characteristic-zero restriction. The proof does not import the later characteristic-zero universal-vector-extension theorem. Parent independently opened this exact page. No fresh original Oort1966 inspection is claimed. |
| D_HaconPatakfalvi2014v2 | ChristopherD.Hacon and ZsoltPatakfalvi, full34-page arXiv1310.2996v2,20February2014, https://arxiv.org/pdf/1310.2996v2. Lemma2.3.1 and Proposition2.3.2 with full proof, authorp12; Lemma2.3.3 pp12–13. | Coherent Frobenius bijectivity implies ordinarity and etaleness of Verschiebung. The cited numbering is explicitly v2; the v1 numbering is not substituted. The present owner opened the full source. Parent's separate direct arXiv request failed, and is not recorded as a fresh parent source inspection. |
| D_BrionCoherent2012 | MichelBrion, full18-page arXiv1204.2628v2,29July2012, https://arxiv.org/pdf/1204.2628v2. Theorem1.1 authorp1 and its proof in Section5.1, pp15–16. Author publication metadata: Algebra and Representation Theory16(2013),1449–1467. | Exterior-algebra description of coherent cohomology, applied to an abelian variety, to pass from degree-one Frobenius bijectivity to all degrees. |

The alternative exact Ext input in Brion's full74-page *Some structure theorems for algebraic groups*, authorpp47–48 and Remarks5.3.3(i), was also freshly opened and read by this owner and by Frobenius. It was replaced in the final citation by the more sharply located isogenyII equation(3.8); this is a source substitution, not a new theorem. The course source explicitly confirms the all-characteristic scope of the Ext classification.

## Previously opened inputs reused with explicit proof checks

- Milne, *Jacobian Varieties*, Lemma9.5: the Abel map identifies coherent H1 of the Jacobian and curve. Existing key D_MilneJacobians2021.
- Illusie1972, Theorem2.6 and formula(2.7.2), printedpp166–167: mixed Atiyah/Kodaira–Spencer obstruction for line-bundle deformation. Existing key D_Illusie1972Torsors. The final proof also spells out the relevant mixed Kunneth factor and the pullback killed by Verschiebung.
- Elkik1973, unnumbered Picard corollary on printedp573: the noetherian henselian-pair puncture comparison. Existing D_Elkik1973, used for both source and target. The same exact input was already fully checked in C.3p and the subsequent completion arguments.
- Proper formal existence, Popescu smooth approximation of the excellent completion map, descent of finite-presentation line-bundle data, and smooth lifting for the henselian pair(R,m²): exactly the already proved and source-audited C.3w/C.3az machinery. The prescribed first jet is included in the descended finite data.
- The explicit contraction and Jacobian-ring calculation of C.3m are rederived in characteristic five. The only scalar division required is by4, which remains invertible.

## Superseded passages and exact repair history

The earliest draft contained an unnecessary assertion identifying the entire local-Picard identity component with the computed formal vector extension. That assertion was removed before certification. The proof instead constructs a proper curve through0 and the selected finite-kernel point, then constructs its actual line-bundle family.

An intermediate first-lift argument neutralized the Picard gerbe over that curve, with band Gm times an additive group. Both peers checked it, and their13:49–13:50 receipts remain historical records. The final13:53 revision uses a shorter direct argument: pull the normalized Poincare bundle back by Verschiebung, whose pullback kills its only mixed first-order obstruction; normalize the resulting actual V2-family by its fibre at0. No separate gerbe-neutralization citation is needed or claimed in the final proof.

Higher parameter-family uniqueness is not asserted. H2(V×P,L^n)=0 for n>=2 supplies existence; the individual endpoint classes are unique because H1(V,L^n)=0. Completion injectivity and the nonzero exceptional Neron–Severi class then prove the actual endpoint statements.

## Retained finite program

- Source: `code/check_C3bf_integral_picard.py`.
- Complete standard output: `code/check_C3bf_integral_picard.out`.
- Structured certificate: `output/C3bf_integral_picard_certificate.json`.
- Original start: **2026-11-19T13:51:48.836254+00:00**.
- Actual runtime: **0.07533210799738299 seconds**.
- Outcome: **41 checks passed; zero failed**.

This verifies the exact Hasse–Witt matrix2I3 with determinant3 modulo5, the identity matrix of the three degree-five Jacobian-ring classes, the Segre polynomial identities and split section, representative dimension identities, and125 distinct constant-group points. It does not substitute for the geometric, Picard, formal, approximation, or actual-family arguments. Parent and Frobenius read the code and output; neither claimed a rerun. The original certificate and timing were not overwritten.

## Independent reviews and formatting

- Parent: `research/notes/ROOT_C3bf_INDEPENDENT_REVIEW.md`, full mathematical and targeted source/certificate approval; parent canonical event retained in the root register.
- Cycles: `../cycles/C3bf_integral_picard_independent_REVIEW.md` and its CHECK_EVENTS.tsv. Original actual-curve proof pass13:49:28; final direct-Poincare replacement independently passed13:53:54.
- Frobenius: `../frobenius/C3bf_integral_picard_kernel_independent_REVIEW.md` and its CHECK_EVENTS.tsv. Full revised proof and fresh exact Ext input checked; final direct-Poincare replacement also separately passed. The review does not claim an independent finite-program execution.
- Four-pass standalone compilation is retained in `output/compile_C3bf_recovery.json`, with every command's stdout and runtime. The first successful build had a7.43558pt heading overflow; its complete record is preserved as `output/compile_C3bf_initial.json`. The heading alone was shortened before the final formatting pass. No mathematical content changed.
