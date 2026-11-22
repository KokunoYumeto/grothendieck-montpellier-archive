# Primary-source and supplied-input log

HODGE_DIVISION; `/root/imprimitive`; 2026-11-21; GPT-6 Astra Pro, effort inherited/not exposed.
The native URLs below are the source identifiers for the final bibliography. Browser reference IDs record retrieval provenance; they are not bibliographic titles. A source listed as background or statement-only is not marked independently reproved.

## Imprimitive representations and cyclic-cover period maps

1. **G. I. Lehrer and D. E. Taylor, _Unitary Reflection Groups_, Cambridge University Press, 2009.** Chapter 2, sections 1--3, pp.23--27; Proposition 2.10 with the correction in the authors' errata dated 5 February 2025. Used for conventions and context for monomial induction/irreducibility. The exact representation, induced map, character field, rational projector, and polarization comparison used here are proved in D-IM-01.
   - Author errata: https://www.maths.usyd.edu.au/u/don/papers/errata-uggr.pdf
   - Official contents: https://assets.cambridge.org/97805217/49893/frontmatter/9780521749893_frontmatter.pdf
   - Browser provenance: `turn649657737search8`, `turn649657737search7`.
   - The erratum states that G(m,p,n) is imprimitive for n>1 and irreducible for m>1 except (m,p,n)=(2,2,2). Our ranks and d avoid the exception.

2. **J. B. Lewis and J. Wang, “The Hurwitz action in complex reflection groups,” _Combinatorial Theory_ 2(1), 2022.** Section 2.1: the groups G(m,p,n) and their two reflection types. Used and rechecked for conventions, not for a dominance assertion.
   - Published repository: https://escholarship.org/uc/item/4xg2m191
   - Author conference version, section 2: https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2021/19Lewis.pdf
   - Browser provenance: `turn649657737search3`, `turn649657737search10`, `turn211488526search38`.

3. **H. Lange and A. Ortega, “Prym varieties of cyclic coverings,” _Geometriae Dedicata_ 150 (2011), 391--403, doi:10.1007/s10711-010-9512-9.** Proposition 4.1 and proof, author PDF pp.7--10: the codifferential is multiplication of eigendifferentials. Read in full for the exact restriction to the primitive conjugate pair. This is the smooth codifferential input in D-IM-05. D-IM-06 separately derives the two unequal branch-exponent version; the uniform-branch convention of this paper is not silently extended.
   - Author version: https://arxiv.org/pdf/0805.1020
   - Browser provenance: `turn308732096view0`, `turn873414231view1`.
   - Proposition 5.5 and Lemma 5.4 were also inspected: their genus threshold does not cover the genus-six rank-15 witness, so they are not used to bypass its calculation.

4. **B. Farb and D. Margalit, _A Primer on Mapping Class Groups_, Princeton University Press, 2012.** Proposition 6.2, printed p.166 (primitive homology classes represented by nonseparating curves); Theorem 6.4, p.170 (surjectivity onto the integral symplectic group); Theorem 4.6 and Fact 4.7, around pp.97--98 (Birman exact sequence and point-pushing). Used and rechecked in the irreducibility argument of D-IM-07; the required point-push effect on cyclic characters is explicitly proved there.
   - Author's publication page: https://www.math.uchicago.edu/~farb/books.html
   - Book PDF consulted: https://euclid.nmu.edu/~joshthom/teaching/ma589/farbmarg.pdf
   - Browser provenance: `turn940858109view0`, `turn834090210view0`, `turn834090210view1`, `turn813666201view2`.

5. **Stacks Project, Deformation Theory, section 93.10.** Lemma 93.10.3, tag 0E3V, and section tag 0E3S were located as background for deformations of a morphism. D-IM-07 gives the elementary Cech obstruction argument itself, so no unverified stronger smoothness theorem from this source is assumed.
   - https://stacks.math.columbia.edu/tag/0E3V
   - https://stacks.math.columbia.edu/tag/0E3S
   - Browser provenance: `turn479736444search29`, `turn479736444search27`.

6. **Supplied HODGE_DIVISION_ATTACK_20261121.md.** Propositions O, O', Corollary O'', and Lemma Dom. Used as the stated problem inputs. Our new proof is an actual factorization of the natural imprimitive variation through cyclic-cover moduli, not an inference that a source dimension inequality is sufficient. D-IM-03G also records the limitation of the reflection classification once nonreflection local monodromies are allowed.

## Semiregularity and the CM sixfold construction

7. **R.-O. Buchweitz and H. Flenner, “A semiregularity map for modules and applications to deformations,” _Compositio Mathematica_ 137 (2003), 135--210, doi:10.1023/A:1023999012081.** Section 4.1 and Proposition 4.2, pp.166--167: trace of the exponential Atiyah class and its compatibility with contraction/obstruction. The statement applies to perfect complexes. Read the statement and proof. These are the precise trace identities used in D-SR-02; no inference from an arbitrary K-class to semiregularity is made.
   - Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/semiregularity_map_for_modules_and_applications_to_deformations.pdf
   - Browser provenance: `turn227892964view0`, `turn751535265view2`, `turn922834815view2`.

8. **R.-O. Buchweitz and H. Flenner, “The global decomposition theorem for Hochschild (co-)homology of singular spaces via the Atiyah--Chern character,” _Advances in Mathematics_ 217 (2008), 243--281, doi:10.1016/j.aim.2007.06.013.** Proposition 6.2.1 and Theorem 6.4.2 in the author version (pp.29 and 31): the classical semiregularity map factors through Hochschild homology, and evaluation followed by trace is contraction with the Chern character. Exact statements and proof context were checked. The journal and DOI were verified separately at the publisher; page numbers just given refer to the explicit author PDF, not an assumed journal pagination.
   - Author PDF: https://arxiv.org/pdf/math/0606730
   - Publisher: https://www.sciencedirect.com/science/article/pii/S0001870807002083
   - Browser provenance: `turn227892964view1`, `turn751535265view3`, `turn751535265view4`, `turn922834815view3`, `turn368944151search0`.

9. **S. Mukai, “Duality between D(X) and D(Xhat) with its application to Picard sheaves,” _Nagoya Mathematical Journal_ 81 (1981), 153--175, doi:10.1017/S002776300001922X.** Theorem 2.2, p.156: the Poincare Fourier--Mukai equivalence and its inverse. Equation (3.1), p.158: exchange of translations and tensoring by degree-zero line bundles. Both exact statements were checked in the published text. The latter is the input that proves ordinary negative self-Ext still vanishes after the explicit isogeny pullback in D-SR-04.
   - Published PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf
   - Browser provenance: `turn227892964search5`, `turn368944151view2`, `turn368944151view3`, `turn922834815view0`, `turn922834815view1`.
   - A direct open initially timed out; the indexed published full text was then opened at the exact theorem and equation. No successful direct file download is claimed.

10. **A. Beauville, “Some surfaces with maximal Picard number,” _Journal de l'Ecole polytechnique -- Mathematiques_ 1 (2014), 101--116, doi:10.5802/jep.5.** Section 4, Lemma 2, p.106, and Example 3, p.107: the Fermat quartic Jacobian is isogenous to the cube of C/(Z+iZ). Read the exact example. D-SR-04 additionally verifies the polarization factor 2 and degree 8 from the three double quotient maps; those quantitative refinements are not attributed to the example without proof.
   - Published PDF: https://www.numdam.org/article/JEP_2014__1__101_0.pdf
   - Browser provenance: `turn382741429view0`, `turn493572167view0`, `turn493572167view1`.

11. **A. Perry, “The semiregularity theorem for equivariant noncommutative varieties,” arXiv:2604.00511v2, 24 June 2026.** Theorem 1.2, p.3; Remarks 2.3 and 2.5, p.5; Definition 2.6 and Lemma 2.7, pp.5--6. Theorem 1.2 is the stated S-14 deformation input. The remarks identify the categorical trace with the classical trace and state functoriality. The definition/lemma distinguishes ordinary, G-, and weak G-semiregularity. Exact current-version statements were read. This is an arXiv preprint; no refereed publication status is asserted.
   - https://arxiv.org/abs/2604.00511
   - https://arxiv.org/html/2604.00511v2
   - Browser provenance: `turn275914326view1`, `turn742813632view0`, `turn493572167view2`.
   - We do not use Perry section 1.1's account of Markman's construction as a premise for D-SR-01--04. It suggested the search; the new ideal, trace, full-character, and CM-transport arguments are written in full.
   - For the zero-B-field refinement D-SR-06, the proof of Theorem 1.2 in section 6.2, printed pp.26--28 of v2, was read in full. Taking the Kummer class zero and the lift parameter n=1 keeps the ambient category untwisted; Corollary 5.17's band pushout preserves zero. This verifies an ordinary perfect-complex deformation, rather than assuming that a general twisted conclusion is automatically ordinary.
   - PDF: https://arxiv.org/pdf/2604.00511v2 . Additional browser provenance: `turn378606164view0`, `turn654347447view2`, `turn524533165view0`, `turn976520825view0`, `turn532030542view0`.

12. **C. Birkenhake and H. Lange, _Complex Abelian Varieties_, second edition, Springer, 2004.** Proposition 11.2.1 (Poincare formula), and the classical Lefschetz very-ampleness theorem in section 4.5 (Theorem 4.5.1 in the 1992 edition). These are classical background inputs for [C]=Theta^2/2 and 3Theta very ample. The original book proposition text was not directly retrieved in this run; the Poincare formula is also used with an exact primary locator in Schoen1988, Corollary3.1 proof p.25, referencing Griffiths--Harris p.350. Do not record an independent full-proof check of the book.
   - Publisher metadata: https://link.springer.com/book/10.1007/978-3-662-06307-1
   - For the precise very-ampleness statement in an accessible primary paper, see the next item.

13. **T. Bauer and T. Szemberg, “On tensor products of ample line bundles on abelian varieties,” _Mathematische Zeitschrift_ 223 (1996), 79--85.** Theorem 1.1(b): a tensor product of three ample line bundles is very ample. The accessible author text was read, so taking all three line bundles equal supplies the needed 3Theta fact without relying on an uninspected book theorem.
   - Author paper copy surfaced at: https://www.academia.edu/12442452/On_tensor_products_of_ample_line_bundles_on_abelian_varieties
   - Browser provenance: `turn922834815search0` (full paper text, including theorem and proof). Its hosting is secondary, but the text itself is the authors' primary research paper.

14. **Supplied DEG_L.tex, S-14.** The entire proposition and proof were read. Its hypotheses are the full even character exp(B)ch(E)=lambda t+P(theta), ordinary negative-self-Ext vanishing, and weak semiregularity for an actual coherent target translation/tensor action. D-SR-01--04 constructs the object and verifies all three; the rank is zero and S-14 explicitly does not require nonzero rank. Supplied S-09 remains only a K-class projector and is not used to infer semiregularity.

## Cross-audit of the G34 proof

15. **C. Schoen, “Hodge classes on self-products of a variety with an automorphism,” _Compositio Mathematica_ 65 (1988), 3--32.** Simple branch tuple definition and Theorem 2.0, p.11; Corollary 3.1 and proof, pp.24--25. Read these exact passages while checking D-G34-04--06. They cover all primitive cyclotomic determinant lines for paired branch exponents. The local repair in the G34 agent's D-G34-04 is separately proved; no invalid prime-quotient choice from the printed Lemma 2.8 is used.
   - Published PDF: https://www.numdam.org/item/CM_1988__65_1_3_0.pdf
   - Local copy/text: `../sixfolds/sources/Schoen1988.pdf`, `../sixfolds/sources/Schoen1988.txt`.
   - Browser provenance: `turn275914326view0`.

## Sources inspected but not premises

- Markman, supplied `LIT_Markman_Hodge_abelian_fourfolds_2502.03415/250531.tex`: the genus-three secant construction, generic torsion-orbit conditions, and Yoneda-algebra arguments were inspected as leads. They are not used as theorem premises in D-SR-01--04. The new proof first descends the curve ideal and allows a rank-zero complex, so the good theta-incidence conditions and reflexive-sheaf realization are unnecessary.
- Caldararu--Willerton, “The Mukai pairing. I. A categorical approach,” _New York Journal of Mathematics_ 16 (2010), 61--98, Theorem 6 and section 7: located as published background for categorical functoriality. Not yet read in full; no check event claims otherwise. https://nyjm.albany.edu/j/2010/16-6p.pdf
- Lange--Ortega, “On the Prym map of cyclic coverings,” _Archiv der Mathematik_ 111 (2018), 621--631, Proposition 3.3/Corollary 3.2: inspected for sixfold coverage and passed to the sixfold agent; not needed for our genus-six/genus-five exact certificates.

## General monomial sixfold sources and the determinant audit

16. **E. Looijenga, “Prym representations of mapping class groups,” _Geometriae Dedicata_ 64 (1997), 69--83, doi:10.1023/A:1004909416648.** Proposition 2.2 and Theorem 2.4, author version p.5; Proposition 4.2 and the proof of Proposition 2.2, pp.8--9; section 4.4, Corollary 4.5, Lemma 4.6 and the genus-at-least-three proof of Theorem 2.4, pp.10--12. All these statements and the relevant proofs were read. They give the actual hyperbolic cyclotomic intersection module and the full lifted mapping-class image, which are the published inputs for D-MON-02. The new commutant, full endomorphism, induction and dominance deductions are proved separately in `monomial_sixfold_section.tex`.
   - Author page: https://webspace.science.uu.nl/~looij101/downloadable-research-paper.html . Browser provenance `turn985387300view0`, link54.
   - Author source successfully downloaded: https://webspace.science.uu.nl/~looij101/pr2.ps . Local immutable original `sources/Looijenga1997.ps`; converted PDF and extracted text `sources/Looijenga1997-author.pdf` and `.txt`. The author version has14 pages, so cited page numbers are explicitly author-version locators, not inferred journal pages.
   - Official university publication record: https://research-portal.uu.nl/en/publications/prym-representations-of-mappings-class-groups/ . Browser provenance `turn985387300view1`. Its separate PDF link returned403; no successful download from that link is claimed.
   - Philipp Bader, “Prym representations of the handlebody group,” _Geometriae Dedicata_218,59 (2024), Theorem1.5, was read as an independent statement check of Looijenga's Theorem2.4, not as a replacement for reading the original. Publisher https://link.springer.com/article/10.1007/s10711-024-00911-5 ; browser provenance `turn457210188view0`, `turn457210188view1`.

17. **M. Dettweiler and S. Wewers, “Variation of parabolic cohomology and Poincare duality,” _Seminaires et Congres_13 (2006),145--164.** Theorem2.5, author-version p.12, and its complete proof pp.13--14 were read during the whole-proof audit of D-DET-01--03. The right-action convention and cocycle quotient on pp.2--3 were also read. The exact Hermitian-dual specialization and the sign relative to the triangular form were re-derived in `DETERMINANT_BARRIER_PEER_AUDIT.md`.
   - Author PDF: https://arxiv.org/pdf/math/0411119 ; direct browser provenance `turn734901050view0`.
   - Publisher: https://smf.emath.fr/node/43624 ; browser provenance `turn229941329search1`.

## Citation discipline

The proof files distinguish source facts from new proofs. Check-event types describe the work actually performed. Exact finite-field determinants and exact exterior-algebra identities are computation certificates, not proof-assistant formalizations. No unrefereed Markman, Severn, or 032 theorem is silently promoted to a published premise.

## Final E8 transfer and nonsplit lattice audits

- **Landherr1935**, original paper pp.246–247, classification by real signatures and determinant norm classes, including the induction/local-global argument: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf . DOI10.1007/BF02940728. Browser provenance `turn665811765view0`. Local sibling source SHA-256 `ccfaea6449b2d70fd3093551694bc7062548e88bc330ec8ef476612fdb34050f`. Full used argument read; quantitative denominator bound is new and not attributed to Landherr.
- **Truong2020**, Lemma2.2 and its full used degree proof, author p.13: https://arxiv.org/pdf/1605.05049 . Published Crelle758(2020),139–182, DOI10.1515/crelle-2017-0052. Browser provenance `turn470381437view0`, `turn180430472view0`, `turn180430472view1`. Used for improper intersection expressed by bounded effective positive and negative pieces.
- **Supplied SQ3**, HECKE_DIV.tex in RETURN_HECKE_DIV_final_20261121T0204Z: complete integer column-lattice proof read. Its printed determinant-character identity is not silently treated as a full module identity; D-E8-XFER01 proves the latter variant from the integer lemma and Brauer integral induction.
- Further exact primary locators and used-proof scope for Deligne1974III, Shioda–Katsura1979, Tseng2010, Bakker–Brunebarbe–Tsimerman, Catanese–Dettweiler2014, and the E8 ODE sources are preserved in BRANCH_EXPONENT_SUPPLY_PEER_AUDIT.md, E8_GRR_PEER_AUDIT.md, and e8_period_bibitems.tex.

## Nielsen rank algorithm: Romagny--Wewers (2006)

Published complete EMIS copy: https://emis.de/ft/47206 . Read Theorem 3.1, Propositions 3.2/3.4 (pp. 319--321), Theorem 4.3 with its construction (pp. 323--327), Theorem 4.11 (pp. 328--331) and Remark 4.15. Used for finite algebraic definition and comparison of algebraic and topological Hurwitz covers. No direct unspecified SGA field-of-definition assertion; no BPR/QE input remains in the proof. Exact monodromy uses the separately proved rational Rouche subdivision. Full copyrighted PDF is a source cache, not a deliverable.

## Rank-five inducing reduction and recent peer reviews

- **A. M. Cohen, Finite complex reflection groups, Ann. Sci. ENS 9 (1976), 379--436.** Primary published PDF https://www.numdam.org/article/ASENS_1976_4_9_3_379_0.pdf . Freshly read §1.4(ii),(vi), pp381--382 (including the proof of vi); Lemma2.12 p391 and Proposition2.13 pp391--392 with their proofs; exact K5 root model §4.15 pp409--410, Table4.16 and its K5 degree/order proof pp411--413; complete rank-five classification argument §5.10 pp430--432; Theorem5.12 and normalizer Proposition5.14 p435. The published classification is an explicit theorem input, not claimed newly reproved. Browser provenance turn360230688view0, earlier turn850202576view0.
- **Cohen 1978 erratum**, Ann. Sci. ENS 11 (1978), p613, read in full: https://www.numdam.org/article/ASENS_1978_4_11_4_613_0.pdf . The corrected normalizer theorem has only the rank-three G25 exception; the obsolete rank-four exception is not used. Browser provenance turn360230688view1.
- **G. Malle 1999**, Rationality and fake degrees, Table8.2 p675 and the exact splitting-field explanation p676 freshly read while auditing BI13. The locally cached original is research/sources/Malle1999.pdf; its extracted text is sibling bireflection/sources/Malle1999_review.txt. The argument uses these published splitting-field entries and Cohen's explicit root models, not a claimed independent classification.
- **J. Lewis and V. Reiner, Circuits and Hurwitz action in finite root systems, NYJM22 (2016).** Corollary1.4 p1459, Proposition4.1 p1473, and complete used equal-pair extraction proof §4.3 pp1480--1481 read. Primary published PDF https://nyjm.albany.edu/j/2016/22-63v.pdf . The theorem is applied only to real finite reflection groups. It is not silently extended to G33.
- **D. Mumford, Abelian varieties**, original scan https://wstein.org/edu/Fall2003/252/references/mumford-abvar/Mumford-Abelian_Varieties.pdf . Read §16 vanishing theorem and proof pp150--153 and the complex Hermitian-index corollary with proof pp162--163, including visual checks of the original spreads. Used in the E813/E815 peer audits for nondegenerate index2 line bundles and all Pic0 twists. The large PDF could not be opened by web extraction, but the complete local original scan was available and inspected. No independent proof of every earlier book dependency is claimed.
- **Supplied DEG_L S-21**, complete proof freshly reread for E815, particularly equations S21.6--7. Its identity-sector induction/forgetting calculation and categorical Riemann--Roch give the two-object cross-Euler formula directly. The supplied proof's Perry/Shklyarov inputs are retained with their stated publication status; this audit is not a new direct reading of all those external papers.

## Sporadic complete-table input and small Lie-field peer audit

- **CTblLib 1.3.11**, dated2025-05-25 in its author PackageInfo, official author archive <https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbllib-1.3.11.tar.gz>. Complete retained mathematical inputs and exact source strings in sporadic/character_inputs.json and coverage.json; archive SHA-256f201e9da571c681a7bbfb1e4683bdb2c80a23b005099ed0453521f59cb443434. All38 tables identify the published ATLAS as origin. Manual3.7-3 and3.7-6 explain multiplier/outer metadata and ATLAS provenance; root additionally checked3.7-5. The group identifications and complete ATLAS tables are explicit input, not inferred from orthogonality. Retrieval hashes and build notes are retained outside the excluded dependency cache.
- **Hoffman2000, Lübeck2001, Hiss–Husen–Magaard2015, White2013**: complete fresh primary locators, used statement/proof scope and degree-table qualifications are recorded in audit_lie_small_fields/PEER_AUDIT.md. Hoffman only supplies its published classical rows; Lübeck's published Th2.1/Section5 supplies exceptional minima. The complete exceptional-cover list removes the potential central-cover gap.

## 2026-11-21: G2/triality and linear-Weil audit

The complete new all-field G2/triality source log, exact table locators, frozen official mathematical inputs, and explicit access limitations are in `lie_small_fields/g2_triality_sources.md`. The independent whole-proof and fresh numerical audit of D-BI-23 is in `audit_linear_weil/PEER_AUDIT.md`. These records distinguish published input, author derivation, actual rerun, and independent arithmetic reconstruction.

## 2026-11-21: complete even-characteristic C2/C3 inputs

Full scope, source corrections, explicit dissertation status, exact all-field coefficient proof, complete small outer tables, failed stronger estimates and deterministic certificate hashes are in `lie_small_fields/even_symplectic_sources.md`. New proof D-ESC-01--03 is submitted for independent whole review; no independent PASS is yet claimed.
