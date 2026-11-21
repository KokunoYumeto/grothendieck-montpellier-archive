# Independent audit of integral classification at Vandiver primes

Reviewer `/root/archive_kummer`, GPT-6 Astra Pro. Date: 21 November 2026. The complete `work/integral_classification_section.tex` was read, with a fresh primary-source check of the needed class-group statements.

**PASS**, relative to the already proved Vandiver kernel theorem, Brown rational freeness, and exact outer-filtration comparison. The conclusion is infinitely many nonzero finite even Lie-indecomposable quotients at each irregular Vandiver prime, not a location or order for the first defect.

## Source checks

Sharifi's complete Iwasawa notes were downloaded from https://www.math.ucla.edu/~sharifi/iwasawa.pdf to `work/sharifi_full_iwasawa.pdf`, with local extracted text. The full statement and proof of Proposition3.4.1 were read on printedpp90–91: minus class-group extension maps are injective, and norm projections from the minus Iwasawa module are surjective, in the odd-prime CM cyclotomic setting. The full statement and proof of Proposition3.4.7 and Corollary3.4.8 were read on printedp92: the actual p-ramified plus module is the Pontryagin dual of the direct-limit minus class group with Tate twist, and is pseudo-isomorphic to the inverted minus unramified Iwasawa module with twist. These are exactly the two uses in the TeX.

Sharifi2002 Theorem1.1 on p2 of `work/sharifi_galstr.txt` was freshly reread with its preceding definitions of primitive actual-image generators. It supplies the regular-prime conclusion after Brown's rational theorem. No integral freeness is obtained merely by forgetting rational coefficients.

## Proof reconstruction

1. At an irregular Vandiver prime, the base p-class group is nonzero and entirely minus. Injectivity into the direct limit and Kummer duality make Mplus nonzero. The previously checked freeness of H makes its abelianization Zp-torsionfree. The pseudo-isomorphism with Xminus, together with mu=0, gives finite generation of Mplus overZp. It therefore has positive finite free rank.

2. If M^n is the image of F^nH in Hab, it is closed because the source is compact. For any putative nonzero element in everyM^n, the fibers F^nH∩pi^-1(x) are nested nonempty compact sets. Their common point lies in the trivial filtration intersection, a contradiction. Thus the image filtration is separated. This compactness step is essential and is explicitly present.

3. In each degree, grH maps onto grM. Every group commutator has zero image inM, so this map factors through the Lie abelianization. Complex conjugation acts on degree n by(-1)^n. The integral idempotents(1±c)/2 preserve M^n and its quotient, so plus associated-graded pieces vanish in odd degrees.

4. Each grH_n is a finite free Zp-module, as a submodule of the finite free outer Johnson module. In a fixed degree only finitely many pairs of positive weights can bracket to that degree. Their images are finitely generated, hence closed, and tensoring withQp commutes with the resulting quotient. Brown rational freeness makes the even abelianization of grH_Qp zero. Every even integral indecomposable quotient is consequently a finite p-group, and its quotient grMplus_n is finite as well.

5. If only finitely many even grMplus pieces were nonzero, parity would make the entire filtration on Mplus stationary after some point. Its intersection is zero, so the stationary term would be zero. The finitely many earlier finite quotients would then make Mplus finite, contradicting its positive free rank. Therefore infinitely many even pieces are nonzero, and surjectivity from the Lie indecomposables gives the claimed infinitely many finite torsion quotients.

6. Homogeneous odd Lie generators can contribute only odd classes in Lie abelianization; all even Lie words are brackets. Any nonzero even indecomposable quotient therefore excludes every collection of homogeneous odd integral generators. This is stronger than disproving one prescribed normalization, and the proof establishes that stronger statement.

The theorem's numerical scope and the separate p2 result agree with the integrated prior results. Neither a converse from kernel equality to Vandiver nor an unspecified first-defect weight is asserted.

## Version

Reviewed SHA256: `7971e3d3e986d94127e61db9eb765847a95392e933b3aa0bb5302f9803715174`.
