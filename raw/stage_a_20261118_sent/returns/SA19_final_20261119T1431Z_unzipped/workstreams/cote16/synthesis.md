# SA19, cote 16: source audit and mathematical synthesis

**Completed audit:** 19 November 2026. **Scope:** entries 1–43 and 80–84 of the mixed package `MPL_16+47+54+44`; all mathematical material on its cote-16 pages, including unindexed remarks. This worker contributes 48 entry decisions, 40 consolidated items, 84 claim records and 37 problem or documentary-lead records. The full formulas, hypotheses, checks and reference keys are in the accompanying registers. The problem count includes settled questions, missing-context problems and bibliographic tasks; it is not a count of 37 presently open conjectures of Grothendieck.

## 1. What was actually read

The package-level `cotes=44` index field does not locate these entries. Their actual source is cote 16. Every assigned note entry was compared with its cited passage in the supplied transcription, its original notes and doubts, and the applicable changes and checked notes in all six second-pass files. This included the complete cote-16 text, lines 1–2050, under 54 supplied scan markers: 1, 3–23 and 25–56. Markers 2 and 24 are absent from the supplied transcription. The short title or identification pages were read as such, rather than silently excluded from coverage. `reading_coverage.tsv` records the actual boundaries and the limits of the evidence.

No Montpellier manuscript image was supplied. Consequently, a mathematically necessary replacement remains a proposed mathematical reconstruction unless the supplied second pass has already settled the reading. The images rendered and checked during this run are images of published books and papers. They provide publication evidence; they do not authorize an independent decision about manuscript ink. This distinction is especially important for the circled “Non,” the confirmed word *homogènes*, the competing `Vider|Virer` reading, indices in the hyperplane formulas, and the Coates-letter date.

The 48 entry verdicts are 35 kept, 7 corrected and 6 merged. The consolidated items are SA19-101–140. Each verdict has a reason drawn from its actual passage; none was generated from a keyword rule. Claim IDs are CL-SA19-201–284. Their literature classes are A: 14; B: 34; C: 9; D: 14; E: 8; F: 5. These classes describe the searched fate under the prompt's taxonomy, not the strength of an independent proof and not authorship. In particular, a false draft formulation may belong to a later published mathematical development, and a correct theorem may still have unidentified typescript provenance.

## 2. The physical package contains several distinct intellectual units

The material closest to SA19's Picard/Jacobian theme is the local Picard–Brauer–discriminant sequence on scans 19, 21 and 23, together with the reused cohomological fragment on scans 28 and 30 and the Picard/Albanese constructions discussed in the letters. The substantial Lefschetz-operator and standard-conjecture drafts are relevant contextual material, but they should not be made into Jacobian-representability claims. The module and sheaf injectivity typescripts, derived-Hom fragment, EGA galley, SGA 3 correction, Karoubi announcement and Bourbaki editorial sheets have their own sources and hypotheses.

| Material | Supplied locations | Identified status and principal caution |
|---|---|---|
| Graded rings, Lefschetz strings, projectors and universal algebra | 3–18, 20, 22; later 51, 53, 55 | Substantial mathematical draft; literal integral normalization and several support formulas fail |
| Picard, Brauer, Kummer and discriminant pairings | 19, 21, 23 | Exact reused portions of *Brauer III*, §8; the publication itself preserves a comparison gap |
| Hodge-algebra and four-form experiments | 25, 27, 29 | Explicit algebraic questions; earlier-run examples depend on an explicitly chosen operator convention |
| SGA 3 correction | 26 | Exact generic-Cartan spreading paragraph located in XV, Proposition 6.2(iii) |
| English cohomological fragment and bibliography | 28, 30 | Author and full theorem hypotheses not identified |
| Hyperplane formulary | 33–34, 36, 38, 40, 42 | Formal operator identities checked with endpoints and variance stated |
| Karoubi page | 35 | Named foreign author's announcement, compared with his expanded 1968 paper |
| Injective and derived-Hom typescripts | 37, 39, 41 | Exact mathematical counterparts in Matlis and Hartshorne; draft provenance remains separate |
| EGA galley | 43 | Separability obstruction valid; proposed deletion and missing continuation not reconstructed |
| Coates letters | 44–50 | Standard-conjecture program with self-corrections and draft notation |
| Bourbaki editorial material | 52, 54, 56 | Classical local algebra and proposed exposition; detached statements need their missing assumptions |

The current transcription dates the two Coates letters 4 January 1967 and 6 January 1966. The latter is confirmed by the second pass; the apparent thematic continuity is not evidence for changing it to 1967. Likewise, the current surface-projector reading is π_i rather than the earlier π_1. These are documentary facts. They should not be silently replaced by an editor's preferred chronology or a mathematically convenient subscript.

## 3. The central Picard–Brauer finding: a published gap, with a later precise analogue

The three reused sheets are identifiable at formula level in Grothendieck's *Le groupe de Brauer. III. Exemples et compléments*: scan 21 corresponds to the §8.1 material on printed pages 143–145, scan 23 to §8.2 on pages 146–147, and scan 19 to the local-surface discussion on pages 148–151. The complete surrounding hypotheses, not merely the detached formulas, were read in the primary volume (Grothendieck, 1968, §§8.1–8.5).

The local discriminant discussion assumes a complete normal noetherian local ring of dimension two with algebraically closed residue field, a chosen coefficient field, and a proper birational regular resolution that is an isomorphism over the punctured spectrum. The exceptional intersection lattice has a finite discriminant group. Its elementary pairing is independently checked here: if Q is a nonsingular integral symmetric matrix, then

\[
D_Q=\mathbb Z^r/Q\mathbb Z^r,\qquad
b_Q(\bar x,\bar y)=x^tQ^{-1}y\pmod{\mathbb Z}
\]

is well-defined and perfect. The blowup matrix is integrally congruent to Q⊕(−1), so its discriminant pairing is unchanged. This proves the lattice statement and the indicated blowup calculation; resolution independence additionally uses the relevant common-domination result. Mumford's negative-definiteness and topological cokernel calculations supply a separate complex-analytic comparison, with their original scope retained (Mumford, 1961, pp. 6, 10–11).

Neither elementary calculation proves that the cohomological Picard pairing is the discriminant pairing. On printed page 150, Grothendieck asks for mutual annihilation and compatibility of the induced quotient pairing with the intersection discriminant. Remark 8.5 on page 151 explicitly states that the verification was not done: “Le rédacteur avoue qu'il ne l'a pas faite.” CL-SA19-222 therefore remains class C, with the exact historical gap preserved. A published assertion accompanied by this admission cannot be promoted into an established comparison merely by citing the same page. Conversely, the historical admission does not show that the precise question is still open in 2026.

A particularly relevant later primary theorem was found and read in full: Suzuki (2024), Proposition 11.10, pp. 500–501, with Proposition 11.2 on p. 495. Its proof compares a cohomological component pairing and an intersection discriminant pairing through Kummer theory, cup products, traces, a tame symbol and a valuation identified with an intersection number. Its hypotheses are mixed characteristic (0,p), a perfect residue field, and the specified p-primary theory for a complete normal two-dimensional local ring. This is an exact mathematical analogue, not an automatic proof of the old coefficient-field/equal-characteristic formulation. MP-SA19-49–50 and the first proposed next task state the remaining comparison problem precisely.

The Kummer pages also require a distinction between finite coefficients and limits. The finite-n sequence joins Pic/n, H²(μ_n) and Br[n]. An ℓ-adic Tate-module or rational-cohomology statement needs the preceding finiteness and Néron–Severi conventions. The finite discriminant quotient on the reused Brauer sheet also has an ℓ-primary qualification suppressed in the published notation. That omission is not uniquely an error introduced by the supplied transcription. The c43/132–133 cross-link was read at both ends and kept at the finite-Kummer level unless the additional hypotheses are explicitly restored.

## 4. Lefschetz algebra: formal mathematics survives several literal errors

The primitive decomposition follows from the actual hard-Lefschetz isomorphisms of the graded module. It does not require semisimplicity of a correspondence algebra. The unit-step lowering operator sends L^jp to L^{j−1}p and kills the primitive bottom. Its degree is −2, and the endpoint identities are LΛ=1−p_bottom and ΛL=1−p_top. These give direct checks of the draft's kernel, image and endpoint claims. They also expose errors that cannot be dismissed as harmless notation.

First, the proposed integral exterior model fails already on the top power. For ξ=Σe_j∧f_j one has ξ^n=n!·vol. The map from the bottom exterior power to the top is not an integral isomorphism for n≥2. Ordinary contraction also has coefficients j(n−j+1), so it is not unit-step lowering even after rationalization. The normalized integral-string model in the earlier notes is a different construction. Its full matrix-unit argument is proved here and gives

\[
\prod_{i=0}^{n}\operatorname{Mat}_{n-i+1}(\mathbb Z),
\qquad
\operatorname{rank}=\frac{(n+1)(n+2)(2n+3)}6.
\]

CL-SA19-279 records that earlier-run replacement; it is not attributed to the unfinished literal exterior-algebra definition. The confirmed draft bound 2n−i is wrong for these strings, whose exponent bound is n−i. The n=1 conjugation calculation also verifies the source's rejection of uniqueness from L alone: an ungraded automorphism can fix L and alter Λ and the grading.

Second, the intrinsic-projector argument contains several independent support issues. The induction base i=n−1 leaves three central degrees, not only the middle one. An identity using 1−Σπ_{i,α} is an identity on M^i; globally its identity must be replaced by π_i. The scan-12 inverse exponent must be compared with n−(i−2α)=n−i+2α; the supplied negative-sign reading remains an alarm rather than a new ink decision. The inverse criterion on scan 17 places the wrong endpoint projector on one side. Finally, the one-sided cutoff on scan 53 does not annihilate every unwanted degree. The H*(P²) certificate satisfies the indicated inverse assumptions and directly refutes that global assertion.

The corrected outer-projector induction inserts a cutoff on both sides of both raising and inverse blocks. Its proof is written in `proof_checks.md` and isolated as CL-SA19-280, a reconstruction made in this run. The actual theorem has published counterparts in Kleiman's formalism, but this does not make the draft's displayed proof correct (Kleiman, 1968, Proposition 2.9 and Lemma 3.15).

The hyperplane calculations were checked on entire primitive strings, including their endpoints and the extra primitive middle summand on the hyperplane. In particular, with restriction ρ and Gysin γ,

\[
\Lambda_Y=\rho\Lambda_X^2\gamma,
\qquad
\rho\Lambda_X\gamma=1-p_E.
\]

Restrictions do not commute with lowering at an original top endpoint. The transfer formula on scan 40 requires its strict boundary condition, and the two-pullback expression on scan 38 is not composable in its written variance. The product and flag formulas were therefore compared with source and target degrees displayed. These are formal conditional identities. They establish neither the existence of algebraic cycles representing Λ nor a converse hyperplane implication without the product-cycle hypotheses in the letters (Kleiman, 1968, Proposition 2.12 and Theorem 2.13).

The six-dimensional example on scan 22 is the author's own obstruction to a proposed top-power-only criterion. The exact multiplication matrices verify that L is Lefschetz while L′ is not, although their nonzero cubes agree. This belongs to the manuscript's self-correction history, not to the earlier run's conjectural extrapolations.

## 5. Four-form experiments: valid conditional examples and a new obstruction

The scan-25 construction separates three requirements. Poincaré duality is controlled by the nondegeneracy of Q, hard Lefschetz by the nondegeneracy of φ, and associativity by the displayed four-variable identity. The first two do not imply the third. The earlier notes' small counterexample has been rechecked. The isotropic-line construction on scan 27 gives the stated zero four-form under its explicit characteristic and sign conventions.

The claimed recovery of an arbitrary nondegenerate φ from a norm-one vector needs an extra hypothesis. The new counterexample here respects the full four-form constraint: on Λ² of a six-dimensional space the form Q has determinant 15552, the induced φ has determinant 36/25, but the vector ξ inducing it has Q(ξ,ξ)=0. Rescaling cannot make this norm one, even after an algebraic closure. This is a decisive audit counterexample to the unqualified assertion, recorded in CL-SA19-227; it is not a claim of geometric realization.

The positive orbit examples in the earlier notes were also checked at full matrix level, under their explicitly normalized convention U=(Λ²φ♯)Q♭. The six-dimensional example has a nondegenerate 15×15 Q, norm-one ξ and a nonzero cyclic-rank minor. The already proposed family has unbounded cyclic-span dimension, established by a general Vandermonde/open-condition argument and supplemented by finite exact examples. CL-SA19-228–229 retain both origins: the questions are on the source pages; these particular constructions came from the earlier run. The dimension-four threshold, the exact tensor-square convention on scan 29 and the relevant W/V parenthesis remain unsettled. None of these algebraic examples establishes that such a model is the cohomology algebra of a smooth projective variety.

## 6. The letters and the later standard-conjecture literature

The draft letters use a notation in which inverse-Lefschetz algebraicity is called C; the later conventional letter is B. Every comparison in this audit uses the actual definition and quantifiers rather than matching a single letter. Cycle-Lefschetz A in dimensions at most four is also not the universal inverse-correspondence theorem for every fourfold. The low-dimensional and Picard/Albanese arguments were checked against Kleiman's Theorem 2A9 and Corollary 2A10, including the cohomological hypotheses (Kleiman, 1968).

Several directions have exact later developments. The rational-characteristic-polynomial/Cayley–Hamilton argument for inverse correspondences is valid once its operator order and rational coefficients are fixed. The finite-field completion in Katz and Messing's Theorem 2 was read in the original five-page paper, including the proof: for the stated smooth projective absolutely irreducible varieties over a finite field, Künneth projectors are polynomials in Frobenius and the characteristic polynomials of integral correspondences have integral coefficients independent of the chosen cohomology. CL-SA19-284 retains the finite-field restriction; it does not settle every suggested general-field extension (Katz & Messing, 1974, pp. 76–77).

The same primary paper supplies firm chronology. Its p. 73 attributes hard Lefschetz to Deligne and its bibliography identifies the Cambridge lectures of 4–11 July 1973; the paper was received on 8 August 1973. Thus the theorem's circulation is directly documented by 1973. The 1980 date of the complete *Weil II* treatment is not the first-circulation date. Deligne's Theorem 4.1.1 proves rational ℓ-adic hard Lefschetz; it does not prove algebraicity of inverse correspondences (Deligne, 1980, p. 217).

The source's positivity-to-semisimplicity and splitting arguments were checked with all the necessary ambient correspondence hypotheses. A finite-dimensional positive trace algebra has zero radical; the rational finite-dimensionality step also needs its own argument when the algebra is embedded in an ℓ-adic endomorphism space. Jannsen's later theorem proves semisimplicity for numerical motives. Its comparison with a homological realization and the possible nilpotent kernel must not be replaced by an assertion that all homological semisimplicity or cohomology independence is settled (Jannsen, 1992, Theorem 1 and Corollary 1).

The general standard-conjecture program remains distinct from these results. The recent primary theorem found for LSV tenfolds and specified Lagrangian fibrations has special hypotheses; it is not a universal solution (Ancona et al., 2025). The letters' withdrawal of a cohomology-independence claim is preserved. So is Serre's fundamental-group objection to the proposed smooth-hypersurface reduction: the proper regular birational statement and the characteristic-sensitive specialization theorems were checked in SGA 1, X.3.4 and X.3.8–3.9, with XI.1.1 for projective space. The subsequent suggestion of singular hypersurfaces remains a program requiring definitions, not an established reduction.

## 7. Contextual material: exact identifications and remaining limits

The module and sheaf injectivity pages have strong mathematical matches. The original 1966 *Residues and Duality*, II §7, was directly read from a downloaded scan. Proposition 7.6 reproduces the stalk-adjunction mechanism. Proposition 7.17, pp. 131–132, supplies the locally-noetherian quasi-coherent injectivity/decomposition equivalences, and Theorem 7.18 on p. 133 proves that an injective hull of a quasi-coherent sheaf is quasi-coherent. Matlis's explicitly cited module results were also read in their original paper. Gabriel's category conventions were checked rather than silently passing from quasi-coherent sheaves to all modules (Gabriel, 1962; Hartshorne, 1966; Matlis, 1958).

The modern preservation of injectivity from quasi-coherent sheaves to all module sheaves was checked explicitly in Lunts and Schnürer (2016), Theorem 2.1 and proof, following its backward references to Hartshorne. The old remark on Hartshorne's p. 135 is not carried forward as a modern uncertainty. Yet mathematical identity does not prove the author or exact date of the detached preliminary typescript. The derived-Hom sheet also retains its boundedness and finiteness assumptions; the infinite-product counterexample refutes an unbounded extrapolation, not the stated qualified theorem.

The other English fragment remains unidentified. Rosenberg and Zelinsky's cited paper was opened and its exact acyclicity hypotheses read, while the Shatz and Tate references were pursued as backward leads. They do not uniquely determine the detached Proposition 15 or its topology. Unopened original items are marked unverified. Hodge's 1938 article is likewise a precise bibliographic lead with inaccessible original text in this run; the letter's report of historical neglect is not proved from the existence of that citation.

The Bourbaki pages contain useful elementary checks and two decisive qualification failures. Fitting ideals are computed over the module's correct ring; the Kähler different is Fitt₀ over B of Ω_{B/A}. Transitivity, trace-different identifications, tame extensions and standard étale neighborhoods each require their specific hypotheses. F₂³ is finite étale with principal maximal ideals but not monogenic. A×A/(t) over A=k[t] has finite étale fibres without flatness. The latter explains why the flatness condition visible on scan 56 must be retained in a valid reconstructed criterion, CL-SA19-281. The former does not authorize changing the confirmed word *homogènes* into a preferred alternative. The local structure also distinguishes étale from unramified: an unramified neighborhood is a quotient of a standard étale algebra, whereas the étale case has the standard étale presentation itself. The full monogenic-subalgebra proof was read in Stacks10.152.1; the source’s minimal-polynomial terminology over a general base remains qualified. The missing chapter and “Tribu64” reference remain documentary tasks.

For the EGA galley, the local separability obstruction is correct and matches the identified §18.11.6 neighborhood. The original published PDF is substantially larger than the web extraction limit; the bibliography states exactly which primary metadata and which secondary transcription were inspected. The incomplete quotient reduction and proposed deletion of (ii) are not reconstructed into a surviving theorem. This is a remaining documentary limitation, not a reason to suppress the correctly checked local algebra.

## 8. Provenance of the audit's additions

| Claim records | Origin that must survive consolidation |
|---|---|
| CL-SA19-279 | Earlier run's normalized integral-string model, independently proved here; not the literal exterior draft |
| CL-SA19-280 | This run's two-sided projector repair |
| CL-SA19-281 | This run's reconstructed flat finite-fibre criterion retaining visible source flatness |
| CL-SA19-228–229 | Source questions; earlier-run positive examples and family rechecked conditionally |
| CL-SA19-227 | Source assertion; this run's four-form norm-zero counterexample refutes the unqualified version |
| CL-SA19-231–232 | Reused English fragment, unidentified author |
| CL-SA19-256 | Explicitly Karoubi's announcement |
| CL-SA19-257–261 | Reused English injectivity/derived-Hom material; 259 explicitly recalls Matlis; mathematical Hartshorne lineage is not proof of draft authorship |

There are therefore 84 audit claim records, not 84 newly authored assertions of Grothendieck. Source assertions, prior classical results recalled by a source, source questions, the earlier run's constructions and this run's repairs remain visible in separate fields and in this map.

## 9. Verification and next tasks

The executable exact certificates have 16 named sections. They include integral factorials and contraction coefficients, normalized-string matrix units, the n=1 conjugation, the wrong endpoint projector, the blowup congruence, the author's six-dimensional Lefschetz counterexample, hyperplane endpoints, the projective-plane cutoff counterexample, associativity and isotropic examples, the full four-form norm-zero obstruction, the earlier orbit example and family, exhaustive F₂³ nonmonogenicity, a triangular Jacobian and a symbolic Cayley–Hamilton check. Every program actually run and every output is retained. Finite checks are not presented as universal proofs; the general arguments are in `proof_checks.md`.

The structural validator checks schemas, all assigned entries, IDs and foreign keys, reference and event closure, claim coverage in the search log, all supplied scan markers and the recorded output invariants. It does not certify mathematical truth or perform source reading. Those judgments were made individually and remain inspectable in the registers. The final counts are 56 reading alarms, 27 checked links, one separate publication-comparison lead, 28 bibliography entries, 179 check events and 29 research-log rows.

The ranked next tasks are fully specified in `directions.md`. The first is the exact Picard-pairing comparison, followed by a corrected projector companion, identification of the intended integral algebra, the four-form convention and smallest dimension, a Coates-letter definition/chronology concordance, recovery of the Bourbaki assumptions, typescript identification, the original Hodge paper, and the abandoned hypersurface reduction. These are proposed subsequent tasks; no new research program is claimed to have been completed here.

No assigned entry makes a concrete external-project link to La Longue Marche, Les Dérivateurs or a named S6 run. The “S6” heading in the notes is a local section heading. Accordingly `our_projects.tsv` is empty apart from its schema. The dossier preserves that absence instead of constructing a thematic cross-project lead.

### Citation and evidence files

Full bibliographic data, URLs, dates and reading qualifications are in `references.bib`. The exact theorem-to-claim mappings are in `claims.json` and `links.tsv`; the actual queries and outcomes are in `research_log.tsv`. `primary_reading_Brauer.md`, the OCR outputs, the saved web responses and the published-page images preserve the primary checks. Bibliographic identification, reading a theorem statement, reading its proof, independent re-proof and computation are different events in `CHECK_EVENTS.tsv`.
