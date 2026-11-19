# F.3 exhaustive assertion inventory

154 requested source entries are represented by 307 individually adjudicated rows. The extraction includes 52 notes [I], 94 notes [II] (including MB03b), and eight cote-18 standing-question rows.

The complete source text is preserved in `audit_notes_source.json`, with metadata in `audit_notes_entries.csv`. The CSV `audit_claims.csv` is the machine-readable assertion inventory. Every source entry has at least one row, and the build script checks complete coverage and unique assertion identifiers.

Statuses record the mathematical result and do not reverse the historical cancellation or uncertainty in the original-note-kind column. OPEN records the exact remaining obligation; DOCUMENTARY-GAP and READING are not claims that an unseen proof or handwritten sign has been checked. NAMED-CONJECTURE-IMPLICATION records only the proved implication.

Supplemental proofs F.3.1–F.3.34 are in `agent_audit.md`, the research addenda, and `../output/RESEARCH_SA07/sections/F_audit.tex`; other identifiers refer to the current manuscript. No scans were supplied initially. Targeted original cote14, cote16 and cote18 pages were subsequently acquired and visually inspected; cote15 was also acquired for the remaining definition search, with exact page access recorded in the source ledgers; no full archival reading is implied. The CSV adds original-assertion check-event links and canonical dependencies through `build_triangle_check_events.py`; the corresponding event rows are in `triangle_comparison_audit_CHECK_EVENTS.tsv` and the dated addenda `audit_next_CHECK_EVENTS.tsv` and `audit_postcheckpoint_CHECK_EVENTS.tsv`, and `audit_after04_CHECK_EVENTS.tsv`, and `audit_after05_CHECK_EVENTS.tsv`, and `audit_after06_CHECK_EVENTS.tsv`, and `audit_after07_CHECK_EVENTS.tsv`, and `audit_after08_CHECK_EVENTS.tsv`, and `audit_after09_CHECK_EVENTS.tsv`, and `audit_after10_CHECK_EVENTS.tsv`, and `audit_after10b_CHECK_EVENTS.tsv`.

## Status totals

| Status | Rows |
|---|---:|
| DOCUMENTARY-GAP | 9 |
| NAMED-CONJECTURE-IMPLICATION | 1 |
| OPEN | 28 |
| PROVED | 195 |
| READING | 30 |
| REFUTED | 44 |

## I.P01 — Six conjectural realization descriptions

Witness: `18/005:L2–16`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 485.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P01.01 | OPEN | Betti–de Rham realization data classify the proposed global motives. | B.2.1; F.3.4 | Specify the global category and essential image, then prove full faithfulness and essential surjectivity; the local comparison does not supply this global statement. |
| I.P01.02 | OPEN | Betti–Hodge realization data classify the proposed global motives. | C.1.1–C.1.2; F.3.4 | General category and essential image remain unspecified; Hodge fullness for algebraic-cycle correspondences requires the indicated cycle-surjectivity statement. |
| I.P01.03 | OPEN | Bare Hodge structures classify the proposed global motives. | C.1.1–C.1.2; F.3.4 | Determine the intended category and the image; general motivic Hodge fullness remains unresolved. |
| I.P01.04 | OPEN | Betti–Gauss–Manin realization data classify the proposed global motives. | B.2.2; F.3.4 | Specify base, connection, integral or rational data, and geometric essential image. |
| I.P01.05 | OPEN | Betti–Tate realization data classify the proposed global motives. | D.3.2; F.3.6 | Known abelian Hom theorems do not provide the unspecified global category and essential image. |
| I.P01.06 | OPEN | Filtered crystalline realization data classify the proposed global motives. | B.1.5; B.2.3 | The proved local admissible categories must not be substituted for an unspecified global motivic essential image. |

## I.P02 — Missing local analogues

Witness: `18/005:L18–28`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 495.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P02.01 | PROVED | Local description 1′ has a period-ring reconstruction using admissible filtered modules and Galois representations. | B.2.1 | The manuscript's unspecified global analogue is not identified with this local construction. |
| I.P02.02 | PROVED | Relative local comparison supplies the stated smooth proper version of 4′, retaining connection and filtration. | B.2.2 | No arbitrary geometric essential-image classification is inferred. |
| I.P02.03 | PROVED | Passing up to isogeny changes lattices to rational representations; finite extension changes good to potentially good reduction data. | B.1.1–B.1.2; B.2.3 | The descent datum must remain in the potentially crystalline category. |

## I.P03 — Filtered crystals require an essential-image condition

Witness: `18/005:L18–26`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 505.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P03.01 | PROVED | Weak admissibility gives the exact rational crystalline or semistable essential-image condition. | B.1.5; B.2.1 | Retain N in the semistable case and N=0 in the crystalline case. |
| I.P03.02 | REFUTED | Every filtered Frobenius module as displayed is admissible without numerical conditions. | B.1.5, rank-one t_H=1,t_N=0 example | No missing weak-admissibility premise may be silently supplied to the witness. |
| I.P03.03 | REFUTED | The Frobenius semilinearity can always be placed on the ramified coefficient field itself. | B.1.5, p=2 cubic-extension example | Use Frobenius on K_0 and the filtration after scalar extension to K. |

## I.P04 — The precise scope of Oda’s comparison

Witness: `18/005:L18–26; 18/011:L5–7`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 515.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P04.01 | PROVED | M(A[p]) is canonically H^1_dR(A/k) over a perfect characteristic-p field, including p=2. | F.3.1; Oda Corollary 5.11, p.131 | Scope is abelian H^1 over a perfect residue field. |
| I.P04.02 | PROVED | Oda's map identifies the Dieudonné submodule with the Hodge extension maps. | F.3.1 | No canonical splitting is asserted. |
| I.P04.03 | PROVED | The mixed-characteristic lift and rational Galois realization require the additional reconstruction maps stated in B. | B.1.1–B.2.3 | Oda's residue-field comparison is not used as a substitute for those maps. |

## I.P05 — The ℓ-adic line in a p-divisible list

Witness: `18/005:L20–26`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 525.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P05.01 | REFUTED | The ℓ-adic Tate module for ℓ≠p faithfully retains a p-divisible group. | B.1.3 | The literal prime remains ℓ in the transcription; the faithful mixed-characteristic replacement uses p. |
| I.P05.02 | READING | The frozen local list writes ℓ although its surrounding vector space is p-adic. | Frozen witness 18/005:L20–26; original cote18 PDF5/archive p.4 | Original question leaf visually inspected at180dpi on19November2026; the displayed prime supports the frozen ell-adic reading. The mathematical correction still retains the literal prime and uses p in the faithful replacement. |

## I.P06 — Recovering the cyclotomic kernel requires a hypothesis

Witness: `18/006:L35–45`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 535.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P06.01 | PROVED | The cocycle formula gives φ=u on ker χ. | B.4.1–B.4.2 | None. |
| I.P06.02 | PROVED | ker χ∩ker φ=ker χ∩ker u and χ descends along u exactly when ker u⊆ker χ. | B.4.2 | None. |
| I.P06.03 | REFUTED | ker u=ker χ∩ker φ follows from the displayed formula alone. | B.4.2, explicit C_2 counterexample | The missing containment must be established in any intended application. |

## I.P07 — Integral specialization is a separate problem

Witness: `18/007:L10–17`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 545.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P07.01 | PROVED | Integral specialization CH^r(X_η)→CH^r(X_s) is a ring homomorphism for X smooth over a DVR. | F.3.8; Fulton Proposition and Corollary 20.3, pp.398–399 | Integral coefficients and the closure multiplicities are retained. |
| I.P07.02 | PROVED | For a complete DVR and ℓ invertible there, geometric specialization commutes with the integral ℓ-adic cycle class. | F.3.8; Fulton Example 20.3.5, p.400 | Smooth proper hypotheses give the cohomology specialization isomorphism. |
| I.P07.03 | READING | The annotated fallback uses raw cycles and inserts the smooth proper hypothesis. | Frozen witness 18/007:L10–17 | The historical caveat remains even after a modern proof in the stated DVR setting. |

## I.P08 — An explicit weakening on the annotated typescript

Witness: `18/007:L10`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 555.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P08.01 | READING | The same sheet weakens the assertion to a tentative expectation. | Frozen witness 18/007:L10 | No revision chronology beyond the recorded insertion/deletion is inferred. |
| I.P08.02 | PROVED | The weakened wording is compatible with the raw-cycle square and does not refute integral Chow specialization. | F.3.8; Fulton 20.3 | The historical wording is retained; the modern theorem is separately proved. |

## I.P09 — An index problem in the associated-graded twist

Witness: `18/009:L2,8–21`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 565.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P09.01 | REFUTED | A Tate twist leaves the weight-graded index unchanged. | F.2.1, E=Q(0), n=−1 | Use Gr_i^W(E(n))=(Gr_{i+2n}^W E)(n). |
| I.P09.02 | PROVED | The weight and Hodge filtration shift by 2n and n respectively under E(n). | F.2.1 | None. |

## I.P10 — Filtrations and splittings have different parameter spaces

Witness: `18/011:L20–38, L46–49`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 575.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P10.01 | PROVED | Fil and Big are the flag and splitting homogeneous spaces with dimensions u and 2u. | A.1.1 | Use the stated pure semisimple category and its type/reflex-field forms. |
| I.P10.02 | PROVED | Big→Fil is a torsor under a relative varying unipotent group, with U on a chosen fibre. | A.1.1 | A globally fixed U-action is not supplied by the homogeneous construction. |
| I.P10.03 | PROVED | g=l+2u and b=l+u for the cocharacter parabolic and its Levi. | A.1.1 | Mixed nonreductive categories require another argument. |

## I.P11 — The two descriptions of Q require clarification

Witness: `18/011:L6, L25–29, L38, L51–52`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 585.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P11.01 | PROVED | Normalized splitting space Q has dimension u; the expanded H′ space has dimension u+1 with its Tate parameter. | A.1.2 | Retain the parameter and distinguish the two actual maps. |
| I.P11.02 | PROVED | The expanded space maps to the Tate image T_0 with fibre Q. | A.1.2 | The identification T_0≃G_m depends on the specified embedding. |

## I.P12 — A possible reflex-field interpretation of the type field

Witness: `18/011:L24, L30–31, L63`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 595.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P12.01 | PROVED | The flag type and bigrading type descend to the appropriate reflex/type field or finite union over Q. | A.1.1 | Do not assume each chosen connected type is a Q-form. |
| I.P12.02 | READING | The margin's coefficient field and equivariance formula have diplomatic alternatives. | Frozen witness 18/011:L14–23 | The mathematical form construction does not decide the ink. |

## I.P13 — A direction discrepancy in the filtration map

Witness: `18/011:L30, L36`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 605.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P13.01 | PROVED | The natural margin morphism is the forgetful map Big→Fil. | A.1.2 | None. |
| I.P13.02 | REFUTED | A canonical equivariant inverse or section Fil→Big exists when u>0. | A.1.2, Levi/parabolic obstruction and GL_2 example | The reverse reading only yields a map of types, not the asserted section. |

## I.P14 — A Tate-character section does not establish centrality in the full group

Witness: `18/011:L27–29, L38`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 615.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P14.01 | PROVED | A filtration-splitting cocharacter has a Levi centralizer and is central in that Levi. | A.1.1; F.3.3 | It need not be central in the full group. |
| I.P14.02 | REFUTED | The splitting j with εj=id can be identified with the central cohomological weight cocharacter. | F.3.3, GL_2 matrices and εw=t² | Specify the Tate exponent and group containing the cocharacter. |

## I.P15 — The explicit strong period conjecture

Witness: `18/011:L65–76`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 625.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P15.01 | REFUTED | The joint splitting/period field always has transcendence degree g+u. | A.2.5–A.2.6 | Real non-CM elliptic curves have joint field k(α), so the universal extra u fails. |
| I.P15.02 | PROVED | The algebraic image dimension is g+v for the exact joint-conjugate parameter 0≤v≤u. | A.2.2 | Equality at the arithmetic comparison point is a separate period-genericity assertion. |

## I.P16 — The listed consequences follow conditionally from maximality

Witness: `18/011:L49–56, L67–76`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 635.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P16.01 | PROVED | The maximally large composite degree forces the proposed smaller degrees by image bounds and field towers. | A.2.4 | This is the stated implication; it does not establish its premise. |
| I.P16.02 | PROVED | The exact corrected relative image dimensions are v,b+v,u for K/α,K/β,K/γ. | A.2.2–A.2.4 | Actual-point equalities require the named genericity input. |

## I.P17 — The denominators K|k remain a reading question

Witness: `18/011:L70–71`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 645.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P17.01 | REFUTED | The uppercase-K denominator can be used literally for the requested relative transcendence degrees. | A.1.2 | It either is ill-typed or collapses the numerator field over itself; the lowercase-k reading is separately stated. |
| I.P17.02 | READING | The lowercase k and uppercase K readings remain transcription alternatives. | Frozen witness 18/011:L65–76; original cote18 PDF11/archive p.10, lower crop at300dpi | Two independent visual inspections favor uppercase K in the first two consequence denominators: their straight stems and rightward arms differ from the rounded lowercase k in the boxed base field and third consequence. This qualified glyph preference does not prove field containment. Both mathematical readings and A.1.2 remain recorded. |

## I.P18 — The cancelled normalized version is a distinct conjectural witness

Witness: `18/012:L2–24; compare 18/011:L65–76 and 18/013:L4–6`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 655.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P18.01 | READING | The whole normalized-period draft on 18:12 is cancelled. | Frozen witness 18/012:L2–24 | Do not infer a revision chronology or rejection of truth from adjacency to live sheets. |
| I.P18.02 | OPEN | The cancelled normalized period degree is dim G−1 with only the normalization relation. | A.2.4; A.4.9 | The normalization symbol and arithmetic independence are not established by the draft. |

## I.P19 — The group-generation consequence needs the density interpretation

Witness: `18/012:L9–11`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 665.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P19.01 | PROVED | A point with full normalized Zariski locus generates that normalized algebraic group. | A.4.9; A.5.1 | This is the locus-containment implication, not the arithmetic premise. |
| I.P19.02 | OPEN | Semisimplicity and transcendence of π alone prove the cancelled full-group generation claim in its undefined normalization. | F.3.5; A.1.2 | Specify the point, normalization, central quotient, and Tate character before the literal general assertion is defined. |
| I.P19.03 | PROVED | The specified full elliptic period locus generates its motivic torsor. | A.4.9 | No equality of that locus with the torsor is inferred. |

## I.P20 — Schneider’s theorem does not establish the proposed equality

Witness: `18/012:L13–22`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 675.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P20.01 | OPEN | Four normalized non-CM elliptic periods have transcendence degree 3 with determinant one the sole relation. | A.4.9; G, Grothendieck 1966 p.102 note 10 | This full normalized period-independence assertion is not proved here and is excluded as a target A.4(a). |
| I.P20.02 | PROVED | Schneider's theorem gives the algebraic-period-ratio CM criterion used for the flag field. | A.3.1 | It does not by itself supply the full normalized degree 3 assertion. |

## I.P21 — The transcendental-j line changes the base-field problem

Witness: `18/012:L23, L25–26`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 685.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P21.01 | OPEN | Adjoining transcendental j to the normalized tuple gives the cancelled total degree 4. | A.5.4; D.5.4 | The undefined pre-minimal condition and base-field quantifiers must be fixed; the universal unqualified version has the counterexamples cited. |
| I.P21.02 | REFUTED | The extra condition π transcendental over k suffices for every proposed full period or openness conclusion. | D.5.4 | The exact Tate counterexample retains the stipulated transcendence. |
| I.P21.03 | READING | The margin contains an algebraic-τ special case and a deleted question concerning π over k. | Frozen witness 18/012:L23,L25–26 | The normalization and intended scope remain undecided. |

## I.P22 — The live elliptic period conjecture is explicit

Witness: `18/013:L2–6`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 695.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P22.01 | PROVED | For a single CM elliptic curve over Qbar the full period field has transcendence degree 2. | A.4.3; A.2.7 | This theorem is not generalized to arbitrary CM products. |
| I.P22.02 | OPEN | For a non-CM elliptic curve the full period field has transcendence degree 4. | A.4.9; G | Excluded target A.4(a); neither torsor generation nor flag transcendence proves it. |

## I.P23 — Generation of the elliptic period locus is weaker than genericity

Witness: `18/013:L8–10`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 705.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P23.01 | PROVED | Translating the period locus by an algebraic point defines the algebraic subgroup and torsor it generates. | A.4.9 | Existence of the algebraic point follows from nonempty finite-type Qbar locus. |
| I.P23.02 | PROVED | For one elliptic curve that generated torsor is the full motivic torsor. | A.4.9, Kreutz–Shiga–Vignéras theorem in the manuscript's exact version | No full period-genericity consequence is asserted. |

## I.P24 — The Hodge-splitting question matches Katz’s later question

Witness: `18/013:L12`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 715.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P24.01 | OPEN | An algebraic Hodge splitting for a non-CM elliptic curve over Qbar is impossible. | A.4.1, A.4.8, A.4.10–A.4.13 | Exact remaining obligation is transcendence of the splitting scalar, equivalently the stated χ* value; the functional theorem does not prove that specialization. |
| I.P24.02 | PROVED | The scalar/formula reduces the manuscript's question to Katz's specified algebraicity question. | A.4.1; A.4.8 | No priority or historical dependency claim follows. |

## I.P25 — The CM margin has an eigenspace proof

Witness: `18/013:L14`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 725.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P25.01 | PROVED | A CM elliptic curve has an algebraic Hodge splitting because its CM eigenspaces are algebraic. | A.4.2 | None. |
| I.P25.02 | PROVED | The CM splitting can be nonzero; zero has the classified special j-invariants. | A.4.4–A.4.7 | The phrase algebraic does not mean zero in a chosen de Rham basis. |

## I.P26 — The normalization and base-field notation remain unresolved

Witness: `18/012:L5–9, L15–22`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 735.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P26.01 | PROVED | The Legendre relation supplies the Tate determinant and a specified normalization can remove it. | A.1.3; A.4.1; G | This calculation does not identify the unknown handwritten normalizing symbol. |
| I.P26.02 | READING | The ζ/ξ, square-root, and pre-minimal/pre-maximal readings are unresolved. | Frozen witness 18/012:L5–9,L15–22 | Need the missing definition or original witness; preserve both alternatives. |

## I.P27 — The local scalar is computed; globalization remains to be justified

Witness: `18/015:L16–24; 18/017:L4–17`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 745.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P27.01 | PROVED | The local residue/Thom comparison gives the cycle factor (2πi)^p in de Rham-to-Betti direction. | F.1.1 | Use the inverse factor for α in the manuscript's direction. |

## I.P28 — The transversal dimension conflicts with an isolated-point intersection

Witness: `18/015:L19`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 755.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P28.01 | PROVED | A smooth transversal meeting a codimension-p subvariety at an isolated transverse point has dimension p. | F.3.9, tangent-space dimension calculation | The formula uses ordinary complex dimensions. |
| I.P28.02 | READING | The frozen transversal is labelled X′ of dimension n−p. | Frozen witness 18/015:L19; original cote18 PDF15/archive p14 at170dpi | Original scan independently inspected by root and period_triangle: codimension p and the written exponent n−p are clear, while n is not defined on the leaf. The ordinary dimension calculation in F.3.9 gives p; retain the written label and its unstated intended convention. |

## I.P29 — The degree in the global Gysin diagram needs collation

Witness: `18/017:L21–25`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 765.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P29.01 | PROVED | Proper Gysin of relative codimension p shifts degree by 2p and gives α_Y f_*=(2πi)^−p f_* α_X. | F.1.2 | Retain dimensions, sign convention, and Tate target. |
| I.P29.02 | REFUTED | The displayed global codimension-p Gysin map has shift p in ordinary singular-cohomology grading. | F.1.2; frozen witness 18/017:L21–25 | The earlier local 2p is the ordinary degree; retain an unspecified regrading as a reading possibility. |

## I.P30 — The author explicitly requests the final argument

Witness: `18/015:L20; 18/017:L2, L25`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 775.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P30.01 | PROVED | The local residue calculation extends to one universal scalar λ=2πi, with its p-th power in codimension p. | F.1.1 | Local orientation, products, supports, and extension across singular loci are all verified there. |
| I.P30.02 | PROVED | The local-to-global comparison commutes with support maps and gluing, and yields the complete Gysin diagram. | F.1.1–F.1.2 | None in the stated smooth ambient setting. |
| I.P30.03 | READING | The uncertain marginal request for reasoning and the unfinished global-commutativity sentence are completed in the witness. | Frozen witness 18/015:L20 and 18/017:L2,L25 | They remain incomplete documentary evidence; the proof is supplied separately. |

## I.P31 — An abstract lattice and its comparison embedding are separate data

Witness: `18/009:L5; 18/011:L61; 18/017:L11–17`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 785.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P31.01 | PROVED | The abstract integral Betti module and its comparison embedding have the stated Tate scaling. | B.3.1; F.1.4–F.1.6 | Record both module and actual embedded lattice. |
| I.P31.02 | REFUTED | The unscaled integral lattice is universally equal to the algebraic de Rham lattice. | B.3.1, P^1 example | The comparison coefficient (2πi)^−1 is retained. |

## I.P32 — Equality of the modified splittings is extra compatibility

Witness: `18/006:L12, L14, L17, L21–24, L27, L31`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 795.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P32.01 | PROVED | The two-splitting construction yields the displayed cocycle once the compatibility equation is imposed. | B.4.1 | The compatibility equation is explicitly separate from centralization. |
| I.P32.02 | REFUTED | Centralizing the two chosen subtori by itself implies their claimed equality. | B.4.1, explicit C_2 example | The additional compatibility map must be checked. |

## I.P33 — The analytic quotient has a standard conditional justification

Witness: `18/006:L3–4, L43–45`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 805.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.P33.01 | PROVED | A continuous finite-dimensional p-adic image of a profinite group is a compact p-adic analytic group. | B.4.3 | All primes, including 2; finite dimensionality is essential to this argument. |
| I.P33.02 | REFUTED | Sen's inertia statement implies that the entire Galois image has algebraic Lie algebra in the asserted generality. | B.4.3, unramified Q_5 example | Keep inertia and full Galois image separated by the actual restriction map. |
| I.P33.03 | REFUTED | The same analyticity conclusion holds for an unrestricted proalgebraic realization image. | B.4.4, unramified Artin tower plus Tate character | The exact natural semilinear extension has both required splittings and image Z_ell times Z_p^times; its inverse-limit topology has no open pro-p subgroup for ell not equal to p. Every finite object is crystalline. |

## I.M01 — The category is used, not constructed from Lefschetz rings

Witness: `15/219:L8–10;18/011:L5–8`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 817.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M01.01 | PROVED | The usual pure-motive construction specifies cross-variety correspondences, composition, tensor product, summands, and twists. | F.3.4; F.1.3 | None for the named modern categories. |
| I.M01.02 | DOCUMENTARY-GAP | The historical category used on these sheets was constructed from the earlier Lefschetz operator rings. | F.3.4; supplied witness | The pages use the category without the required construction; need the missing construction and its maps. |

## I.M02 — The elliptic period SL₂ is not the Lefschetz action

Witness: `18/012:L13–22;18/013:L4`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 827.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M02.01 | PROVED | The Lefschetz sl_2 action on H^1 of an elliptic curve is zero while the specified standard period SL_2 action is nonzero. | F.3.3 | The conclusion concerns these representations and is proved by their operators. |

## I.M03 — Three kinds of grading and the Tate character

Witness: `18/011:L25–29,38`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 837.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M03.01 | PROVED | A tensor-compatible weight grading corresponds to a central cocharacter. | F.3.3; Deligne–Milne Definition 5.1 | None. |
| I.M03.02 | PROVED | εw=t² for the cohomological weight convention, whereas the specified splitting satisfies εj=t. | F.3.3 | A change of Tate convention reverses both signs consistently; it does not remove the factor 2. |
| I.M03.03 | PROVED | The cohomological, Cartan, and filtration-splitting gradings have the displayed comparison maps. | F.3.3 | The unspecified historical lift still needs its intended group. |

## I.M04 — Only part of the A–D dictionary is established

Witness: `15/215:L3–5;context16/044–050`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 847.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M04.01 | PROVED | The operational manuscript A and C match printed Lefschetz A and inverse-Lefschetz B respectively. | F.3.5; Grothendieck 1969 pp.195–197 | This matches the operational statements, not every unidentified occurrence of a letter. |
| I.M04.02 | DOCUMENTARY-GAP | Manuscript B and D have securely identified standalone definitions matching printed D and C. | F.3.5; original cote 14 pp.43–44; complete Coates letters of 1966 and 1967 | The 27 August 1965 letter explicitly defines B by positivity on cycles modulo algebraic equivalence. Its cycle-class quotient to cohomological algebraic classes is constructed. The particular B and D in the 1967 Coates letter still lack standalone definitions in the inspected text; no uniform dictionary is inferred from the letters alone. |

## I.M05 — The singular-hypersurface programme needs the missing cote 14 witness

Witness: `15/223:L2;15/227:L3–5;context16/047`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 857.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M05.01 | DOCUMENTARY-GAP | Cote 14 carries out the suggested singular-hypersurface reduction. | Supplied context 16:47; complete Coates 1967 letter p.4; F.3.14; original cote14 PDFs111–113 and131 | The normalization map from every smooth integral projective variety to an integral hypersurface is constructed in F.3.14, with an exact nodal-cubic cohomology comparison. Original cote14 PDFs111–113 contain cycle-Lefschetz and punctured-cone formulations; PDF131 has a generic-member/base-locus diagram. These inspected pages have not identified the proposed historical standard-conjecture reduction. That documentary execution remains open. |
| I.M05.02 | READING | The proposed smooth-hypersurface reduction is withdrawn because of the simply-connected obstruction. | Supplied context 16:47 | No later construction is inferred from the distinct smooth-projective archimedean question. |

## I.M06 — The local extension and the arithmetic motivic exact sequence

Witness: `18/006:L2–14,41–45;15/215:L18–21`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 867.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M06.01 | PROVED | The local extension has kernel G′(C), quotient π, and the two splitting maps used in B. | B.4.1 | Its literal kernel and quotient are retained. |
| I.M06.02 | PROVED | Rational Nori motivic Galois groups have the exact arithmetic base-change sequence with proconstant Galois quotient. | F.3.4; Kahn 2025 Theorems 5.10 and 10.2 | No canonical split or identity-component identification is supplied. |
| I.M06.03 | DOCUMENTARY-GAP | The local displayed sequence itself is a written proof of the arithmetic motivic sequence. | F.3.4; typed local and arithmetic arrows | The witness contains no functor identifying those sequences; the modern arithmetic theorem provides a separate stated comparison. |

## I.M07 — Nori/Ayoub comparison and algebraic correspondences

Witness: `15/213:L18–27;18/011:L5–8`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 877.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M07.01 | PROVED | Ayoub's and Nori's Betti Hopf algebras are identified by inverse constructed maps for principal ideal coefficient domains. | F.3.4; Choudhury–Gallauer Theorem 9.1 | Keep the fixed embedding and coefficient hypotheses. |
| I.M07.02 | PROVED | The pure rational Nori category is equivalent to the André motivated category. | F.3.4; Arapura Theorem 6.4.1 | Algebraic correspondences map to motivated correspondences under the specified functor. |
| I.M07.03 | OPEN | Every motivated correspondence is represented by an algebraic cycle in the general categories at issue. | C.1.2; F.3.4–F.3.5 | The corresponding standard/Hodge cycle-surjectivity obligations remain. |

## I.M08 — Fullness of Hodge realization remains a separate assertion

Witness: `15/213:L32–37;15/215:L3–5,23–26`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 887.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M08.01 | PROVED | Hodge realization is full on the specified pure abelian Nori/André subcategory. | F.3.4; Arapura Corollary 7.1.4; C.1.1 | Retain the real descent data in C.1.1 when over R. |
| I.M08.02 | OPEN | The analogous general Nori Hodge realization is full with a characterized essential image. | F.3.4; Arapura Conjectures 7.1.1–7.1.2 | General fullness and the unspecified essential image remain unresolved. |

## I.M09 — Integral finiteness and positive characteristic need separate arguments

Witness: `15/213:L5–14;15/223:L6–17;15/211:L8–10,33–36`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 897.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M09.01 | OPEN | The manuscript's integral fibre-functor forms satisfy a finiteness theorem. | F.3.12; F.3.13; Gille–Moret-Bailly Proposition 5.1; Borel 1963 Theorem 5.1 | The arithmetic finiteness theorem, tensor-torsor equivalence, adelic-genus map, and closed finite-presentation automorphism model for an admissibly generated integral stage are proved. The remaining historical gate is identification of the particular M_alpha with that exact category. Over S-integers fpqc locality already implies fppf locality. Unrestricted proalgebraic finiteness has the explicit product-mu_2 counterexample. |
| I.M09.02 | PROVED | The abelian characteristic-p Dieudonné realization and the mixed-characteristic integral local categories have the specified data. | F.3.1; B.1.5; B.2.3 | This proves the named comparison categories only. |
| I.M09.03 | OPEN | Arbitrary positive-characteristic crystalline points classify the proposed integral motives. | B.3.4; F.3.4 | Specify geometric essential image and the F,V,filtration conditions; no such global classification is proved. |

## I.M10 — Numerical semisimplicity does not identify the cohomological category

Witness: `15/213:L18–27;18/012:L9–11`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 907.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M10.01 | PROVED | Homological equivalence maps to numerical equivalence by the quotient on cycle classes. | F.3.5 | None. |
| I.M10.02 | PROVED | Rational numerical motives are semisimple. | F.3.5; Jannsen Theorem 1 | This theorem does not create a cohomology realization on the quotient. |
| I.M10.03 | OPEN | Cohomology factors through numerical motives in the full proposed generality. | F.3.5; F.3.35; F.3.36 | F.3.35 proves the arbitrary-characteristic abelian dimension<=4 case and its stated dim<=2 generator category. F.3.36 proves characteristic-zero numerical=homological equivalence for every smooth projective variety of dimension<=4 and every abelian variety in arbitrary dimension, with full tensor/category/projector comparison on abelian motives. The kernel-annihilation condition on all remaining relevant smooth-projective products is still open. |

## I.M11 — The normalized group does not determine the central Tate data

Witness: `18/011:L27–29;18/012:L9–22`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 917.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.M11.01 | REFUTED | Fixed normalized SL_2 data determine the full GL_2 group and its Tate character uniquely. | F.3.5, GL_2 versus G_m×SL_2 | Their explicit central isogeny squares the Tate coordinate, displaying the missing data. |
| I.M11.02 | PROVED | Full-group generation must retain the central Tate character and its normalization. | F.3.5; A.1.2; A.4.9 | The literal undefined normalization remains as in I.P26. |

## I.B01 — Tate and anabelian Hom recover different kinds of morphism

Witness: `15/213:L32–37;15/215:L3–5;15/227:L3`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 929.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.B01.01 | PROVED | Tate's finite-field Hom theorem identifies the integral Hom module with Galois-equivariant Tate-module maps. | F.3.6; Tate 1966 Main Theorem | The prime is different from the field characteristic. |
| I.B01.02 | PROVED | Mochizuki's sub-p-adic curve Hom theorem identifies dominant morphisms with the specified open fundamental-group homomorphisms. | F.3.6; Mochizuki Theorem A | Keep openness, geometric-inner quotient, and stated curve/base hypotheses. |
| I.B01.03 | PROVED | The relation between these nonlinear and linear maps is geometric abelianization followed by the Albanese/Jacobian map. | F.3.6 | Not every Jacobian map is a curve map; multiplication by 2 provides the specified counterexample. |

## I.B02 — Semisimplicity does not imply a trivial centre

Witness: `15/195:L23;15/213:L22–30`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 939.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.B02.01 | REFUTED | Semisimplicity of the representation category forces a trivial centre. | F.3.5, Rep(G_m) | The character decomposition and the conjugation kernel are explicit. |
| I.B02.02 | PROVED | For centre-free geometric curve groups, the arithmetic extension is the pullback of Aut→Out along the outer Galois action. | F.3.6; Mochizuki Lemma 1.3.1 and Corollary 1.3.2 | This uses centre-freeness, not semisimplicity of a linear category. |

## I.B03 — Polarization and real-section reconstruction impose different conditions

Witness: `15/203:L9–24;15/215:L23–26;15/217:L3–8`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 949.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.B03.01 | PROVED | A real algebraic Tannakian category is polarizable exactly when its band has a compact real form in the stated theorem. | F.3.7; Deligne–Milne Theorem 4.17(a) | Retain the theorem's algebraic real-category scope. |
| I.B03.02 | PROVED | Real hyperbolic-curve sections recover connected components of the real locus. | F.3.6; Pál Theorem 1.3 and Example 5.8 | They are component classes, not all individual real points. |
| I.B03.03 | PROVED | The positive Weil form in the real motivic comparison is constructed by the stated involution. | C.5.1; F.3.7 | The real involutions alone are not used as an unexplained polarization. |

## I.B04 — Non-Tate weights give a precise cuspidal-inertia criterion

Witness: `15/195:L21–23;15/205:L4–13`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 959.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.B04.01 | PROVED | Number fields have Stix's non-Tate-weight property for abelian Tate modules. | F.3.6; Stix Definition 26 and its following example | The good-prime Frobenius-weight argument gives the required Hom vanishing. |
| I.B04.02 | PROVED | Cyclotomic normalization in Stix includes both open arithmetic image and the cyclotomic character action. | F.3.6; Stix Definition 29 | Both premises are necessary to apply the cited characterization as stated. |
| I.B04.03 | PROVED | The nontrivial closed pro-ℓ subgroups of geometric π_1 with that normalization are exactly subgroups of cusp inertia. | F.3.6; Stix Theorem 30 | Keep the non-Tate and curve hypotheses. |

## I.B05 — The open LM6 normalizer item needs an additional character step

Witness: `15/227:L3`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 969.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.B05.01 | REFUTED | The truncated LM6 A.50 proof supplies the missing cyclotomic-character step for LM6 A.22. | F.3.10; F.3.15-F.3.17; full LM6 A.50 pp.33-34 and A.22 pp.16-17; F.3.18; F.3.19; F.3.20; F.3.21; F.3.22; F.3.23; F.3.24; F.3.25; F.3.26; F.3.27; F.3.28; F.3.29; F.3.30; F.3.31; F.3.32; F.3.33; F.3.34 | F3.10 retains the exact N to NA repair of the original A50 proof. The claim that the truncated A50 proof itself supplies the missing A22 step remains refuted. The new F3.32 proof supplies the previously missing all-genus actual single-line obstruction and resolves the original CM full-profinite common-kernel subgroup assertion through F3.31, independently of that truncated derivation. The exact seven-row polynomial identity, actual arithmetic maps and final I intersection R=1 map are all proved and independently checked. F3.33 now proves the general affine number-field classification and the corresponding common-kernel exclusion through its explicit covering maps. Earlier progress and stopping-point notes are preserved verbatim in work/audit_after11_superseded_scopes.json. F3.34 independently reconstructs the specific all-genus R-vanishing step from six actual Johnson brackets, determinant-203784 and the older published multiplicity bound; the 2026 sketch supplies the formula attribution, while the older dimension input remains explicit. |
| I.B05.02 | READING | LM6 A.22 and A.50 keep their register statuses rather than acquiring referee-approved status here. | Full LM6 archive and results-state register; F.3.10; F.3.15-F.3.17; F.3.18; F.3.19; F.3.20; F.3.21; F.3.22; F.3.23; F.3.24; F.3.25; F.3.26; F.3.27; F.3.28; F.3.29; F.3.30; F.3.31; F.3.32; F.3.33; F.3.34 | The original LM6 register is preserved as a documentary reading: it labels A22 Open and retains its separate A50 status. In the present manuscript F3.32 now proves the original CM full-profinite common-kernel subgroup assertion by a new all-genus scalar certificate and the F3.31 actual witness maps. This does not assign referee-reviewed status to the supplied LM6 file or certify every other LM6 assertion. The separate A20 integral class4 lift and kappa/48 normalization retain their earlier scope. F3.33 now proves the general affine number-field classification and the corresponding common-kernel exclusion through its explicit covering maps. Earlier progress and stopping-point notes are preserved verbatim in work/audit_after11_superseded_scopes.json. F3.34 independently reconstructs the specific all-genus R-vanishing step from six actual Johnson brackets, determinant-203784 and the older published multiplicity bound; the 2026 sketch supplies the formula attribution, while the older dimension input remains explicit. |

## I.X01 — An explicit normalized-j test family

Witness: `15/225:L16`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1243.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.X01.01 | PROVED | The displayed elliptic family has classical j=1728t and the stated nonzero discriminant off its excluded parameters. | E.3.1 | Retain normalized versus classical j. |

## I.X02 — The integral Hodge structure separates points in the test family

Witness: `15/225:L3,16`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1253.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.X02.01 | PROVED | The labelled integral Hodge realization of an elliptic curve determines its complex torus and j. | E.3.1 | The rational Hodge realization gives the isogeny class instead; the precise integral map is used. |
| I.X02.02 | PROVED | An integral Hodge isomorphism and the rational version have their respective lattice and isogeny consequences. | E.3.1; D.5.2 | Do not replace an embedded integral lattice by its rational span. |

## I.X03 — A conditional separation of chosen complex embeddings

Witness: `15/225:L3,9,16;15/227:L3`. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1263.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.X03.01 | PROVED | Agreement on all labelled elliptic-family integral Hodge tests forces equality of the field embeddings. | E.3.1 | The common labels and the Hodge data are essential to the argument. |

## II.C01 — The cycle-class scalar becomes explicit

Witness: `18/019`, first three displays; `18/021`, NB. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 72.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C01.01 | PROVED | The untwisted codimension-p cycle comparison under σ:C→k has scalar σ(2πi)^−p. | F.1.1; F.1.4 | None. |
| II.C01.02 | PROVED | The same factor is global and valid for singular algebraic cycles in a smooth ambient variety. | F.1.1 | None. |

## II.C02 — The final minus sign has a scope problem

Witness: `18/019`, final paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 78.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C02.01 | PROVED | Changing σ to σc multiplies a codimension-p cycle class by (−1)^p. | F.1.4 | None. |
| II.C02.02 | REFUTED | That change always supplies one minus sign, independent of p. | F.1.4, point class in P^2 | The single minus is valid for the adjacent p=1 example and other odd p. |

## II.C03 — The uncertain support arrow remains a real reading question

Witness: `18/021`, first diagram, upper left arrow. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 84.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C03.01 | PROVED | The support-to-ordinary cohomology arrow is the natural localization map and commutes with comparison. | F.1.1 | None. |
| II.C03.02 | READING | The faint arrow or equality sign on 18:21 is securely deciphered by the mathematics. | Frozen witness 18/021 | It is not deciphered; retain the diplomatic alternatives. |

## II.C04 — The proper-map display adds the missing degree shift

Witness: `18/023`, boxed diagram. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 90.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C04.01 | PROVED | A proper morphism of relative codimension p has Gysin degree shift 2p and comparison factor (2πi)^−p. | F.1.2 | All r, including odd r and negative p, are included with the stated dimensions. |
| II.C04.02 | PROVED | The Gysin comparison is compatible with composition and its exponents add. | F.1.2 | None. |

## II.C05 — Correspondence functoriality is the bridge actually drawn

Witness: `18/025`, inserted formula, two comparison diagrams and lower margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 96.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C05.01 | PROVED | Correspondence action is p_2*(p_1* x cup cl(z)) of degree 2r−2dim X. | F.1.3 | Retain target Tate twist r−dim X. |
| II.C05.02 | PROVED | The cycle and projection scalars cancel for degree-zero correspondences and after the indicated general twist. | F.1.3 | None. |
| II.C05.03 | READING | The handwritten exponent and last Ω-subscript are unambiguous. | Frozen witness 18/025; F.1.3 | They remain recorded readings; the typed correction is proved separately. |

## II.C06 — The orientation choice has an exact Tate-line map

Witness: `18/027–029`, $H^2(\mathbf P^1)$ and the first formula on 029. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 102.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C06.01 | PROVED | Changing i to −i reverses the oriented P^1 generator and the comparison scalar together. | F.1.1; F.1.4 | The unoriented embedded lattice is unchanged. |
| II.C06.02 | PROVED | ξ(Z(−1)) is the rank-one Tate lattice with its specified comparison coefficient. | A.1.3; F.1.1 | No unscaled identification is inserted. |

## II.C07 — “Primitifs” needs a specified ambient lattice

Witness: `18/029`, second paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 108.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C07.01 | PROVED | As complete archimedean topologies vary, comparison generators of the P^1 line are exactly the vectors with transcendental coefficient. | F.1.5 | The base is an abstract field isomorphic to C. |
| II.C07.02 | REFUTED | Every nonzero vector of the one-dimensional de Rham line is such a comparison generator. | F.1.5, coefficient 1 | Algebraic nonzero coefficients do not occur. |
| II.C07.03 | PROVED | For a fixed cyclic lattice the primitive elements are its two generators. | F.1.5 | Primitive requires that lattice to be specified. |
| II.C07.04 | READING | The word primitifs or possibles is fixed by this calculation. | Frozen witness 18/029 | Both readings remain; their mathematical interpretations are separately resolved. |

## II.C08 — Real descent of the integral lattice is already present

Witness: `18/029`, final paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 114.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.C08.01 | PROVED | The embedded diagonal integral Betti lattice is stable under real Galois action in the finite and de Rham factors. | F.1.6 | Use the rational real Frobenius on Betti and semilinear descent on de Rham. |

## II.RH03 — Fixed topology and transport of the Hodge splitting

Witness: 18/032:L9–16; 033:L2–4; 039:L4–28. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 122.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH03.01 | PROVED | Two compatible complex identifications for one complete archimedean topology differ by identity or conjugation. | C.4.1 | This is the fixed-topology statement, not all abstract field automorphisms. |
| II.RH03.02 | PROVED | The transported Hodge decomposition changes by the indicated semilinear map and interchange of Hodge indices. | C.4.1; C.1.1 | None. |

## II.RH04 — The commuting conjugations have a concrete fixed-space description

Witness: 18/033:L6; 035:L7–9; 037:L11–20. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 128.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH04.01 | PROVED | The two real involutions commute and f_∞ is their rational linear quotient under comparison. | C.1.1; C.2.1; B.3.2 | Keep coefficient conjugation and rational real Frobenius typed separately. |
| II.RH04.02 | PROVED | The twisted real form is V^+⊗R plus iV^−⊗R inside V_C. | C.2.1 | None. |
| II.RH04.03 | PROVED | Integral Betti–étale comparison identifies the relevant finite realizations and real action. | D.1.1; F.1.6; SGA 4 XVI Theorem 4.1 | Use finite torsion coefficients and inverse limit as stated. |

## II.RH05 — The normalizer formula and Hodge fullness are stated together

Witness: 18/034:L17–35; 037:L23–29. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 134.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH05.01 | PROVED | The real Hodge realization of the specified abelian absolute-Hodge category is full and faithful. | C.1.1 | The functor retains the involution and morphism compatibility. |
| II.RH05.02 | OPEN | The analogous algebraic-cycle homological realization is full for all motives without a cycle-surjectivity premise. | C.1.2 | The precise Hodge-cycle surjectivity on tensor constructions is the remaining obligation. |
| II.RH05.03 | PROVED | The group is generated by its connected component and the real Frobenius in the specified category. | C.1.3 | No statement for an arbitrary undefined motivic category is inferred. |

## II.RH06 — The displayed natural isomorphism has a minus-minus tensor defect

Witness: 18/035:L9–24. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 140.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH06.01 | PROVED | The vector-space projection V^+ plus V^−→V^+ plus iV^− has the computed minus-times-minus tensor defect. | C.2.1 | The corrected tensor constraint and Isom torsor are retained. |
| II.RH06.02 | PROVED | The corresponding fibre-functor torsor is the inflation of the real C_2 cocycle to Q(i). | C.2.1 | A point requires triviality of that actual torsor class. |

## II.RH07 — The tentative tensor nonisomorphism is detected on an Artin line

Witness: 18/035:L26; 037:L20. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 146.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH07.01 | PROVED | For the nontrivial real Artin character the torsor is x²=−1 and has no Q-point. | C.2.2 | This is an explicit obstruction on the Artin subcategory. |
| II.RH07.02 | PROVED | For a pure Tate category the torsor is trivial, with the computed tensor-compatible choice. | C.2.2 | The naive projection need not be the compatible choice. |
| II.RH07.03 | PROVED | Non-CM and CM elliptic tests have the stated distinct torsor outcomes via their actual tensor subcategories. | C.2.2 | The CM obstruction is detected by the indicated Artin summand. |

## II.RH08 — The cohomology-of-real-points line needs its superscript resolved

Witness: 18/035:L13–21; 040:L21–28. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 152.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH08.01 | REFUTED | Cohomology of X(R) always equals the conjugation invariants in H*(X(C),Q). | F.3.7, P^1_R and Spec C/R | The restriction maps in both counterexamples are computed. |
| II.RH08.02 | PROVED | For P^1_R the conjugation quotient is a closed disk with rational cohomology equal to the invariant part. | F.3.7, sphere-to-hemisphere quotient map | This calculates the quotient example actually asserted by the note. |
| II.RH08.03 | READING | The superscript star or zero and the intended fixed-locus versus quotient convention are undecided. | Frozen witness 18/035:L13–21 and 18/040:L21–28 | Both counterexamples retain the diplomatic alternatives rather than assigning a new meaning to the manuscript. |

## II.RH09 — The reality of the period point is sharper than triviality of its torsor

Witness: 18/036:L2–19; 037:L17–20. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 158.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH09.01 | PROVED | The actual period comparison α has real coefficients exactly when f_∞=1. | C.3.2 | This is a statement about the actual comparison point. |
| II.RH09.02 | PROVED | The existence of a real point of the comparison torsor means triviality of its real torsor class and need not make α real. | C.3.2 | The torsor point and the specified comparison point are different maps. |

## II.RH10 — The even-Tate converse fails on the Artin–Tate summand

Witness: 18/036:L21–29; 038:L16. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 164.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH10.01 | REFUTED | Only sums of even Tate powers have f_∞=1. | C.3.1, odd Artin–Tate example | The tensor sign computation supplies the counterexample. |
| II.RH10.02 | PROVED | In the specified real abelian absolute-Hodge category, f_∞=1 exactly for the stated Artin–Tate sums. | C.3.1 | Retain that category and its real descent involution. |

## II.RH11 — The abstract group Gm does not determine real Frobenius

Witness: 18/036 diagram. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 170.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH11.01 | PROVED | An abstract quotient G_m does not by itself specify the image of f_∞. | C.3.1; F.3.5 | On μ_2×G_m the characters (a,t)↦t and (a,t)↦at have different real signs. |

## II.RH12 — The centrality margin requires the meaning of “Q tordu”

Witness: 18/036:L31. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 176.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH12.01 | PROVED | Central f_∞ has the Artin–Tate characterization in the stated categories. | C.3.3 | The homological version has the separately stated fullness hypothesis. |
| II.RH12.02 | READING | The expression Q tordu has one uniquely established tensor-category meaning in the witness. | Frozen witness 18/037:L16–21 | Its readings are retained and matched to the explicit Artin–Tate construction. |

## II.RH13 — The maximal-compact normalizer discussion is withdrawn on the sheet

Witness: 18/038:L20–44. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 182.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH13.01 | REFUTED | The raw centralizer or two-element normalizer of the Weil element in G(R) is always compact. | F.3.7, pure Tate G_m | The weight torus itself is the explicit noncompact subgroup. |
| II.RH13.02 | PROVED | After the weight quotient in the polarizable setting, C²=1 and its centralizer is maximal compact on each finite tensor-generator quotient. | F.3.7 | The positive-form proof supplies the needed hypotheses and actual subgroup. |
| II.RH13.03 | READING | The maximal-compact paragraph and its change from G to G/im(w) are withdrawn on the sheet. | Frozen witness 18/038:L20–44 | The modern proof does not reverse the recorded cancellation. |

## II.RH14 — A real form in de Rham cohomology is constructed even without real descent of X

Witness: 18/039:L17; 040:L15–28. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 188.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH14.01 | PROVED | Betti and de Rham real structures are related by κ_D=α f_∞ κ_B α^−1. | C.2.1; C.4.1; B.3.2 | None. |
| II.RH14.02 | PROVED | The de Rham Hodge splitting β is R-rational and R(γ)=R(α). | C.4.2; F.3.7 | This does not establish Qbar-rationality of β. |

## II.RH15 — The p,q degree in the boxed inclusions is a frozen reading question

Witness: 18/040:L33–35; 041:L6–12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 194.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH15.01 | PROVED | The Hodge (p,q) summand belongs to total degree p+q with the typed comparison target. | A.1.1; C.4.1 | None. |
| II.RH15.02 | READING | The doubtful total-degree superscript is decided by direct scan inspection. | Frozen witness 18/041 | No such inspection occurred; retain the alternative and the typed mathematical formula. |

## II.RH16 — The final totally-real-field assertion has an embedding calculation

Witness: 18/041:L20–26. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 200.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH16.01 | PROVED | The intersection of all real closures determined by complex embeddings is the totally real algebraic subfield in the stated sense. | C.4.1 | Use the exact scalar-field intersection and embeddings specified there. |

## II.RH17 — The p-adic questions remain questions on this package's list

Witness: 18/043:L20–22. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 206.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH17.01 | PROVED | Problem 3 has the stated p-adic period-ring, good-reduction, semistable, and relative comparisons. | B.3.3; B.2.1–B.2.3 | The appropriate extra structures and coefficient rings are retained. |
| II.RH17.02 | PROVED | Problem 4 has the characteristic-p crystalline, rigid, and prismatic structures within their exact hypotheses. | B.3.4 | No undeclared geometric essential-image classification is inferred. |

## II.RH18 — Oda directly addresses the earlier p-torsion extension question

Witness: 18/043; CT54/003,005,007. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 212.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH18.01 | PROVED | A[p] determines the canonical characteristic-p de Rham Hodge extension for an abelian variety over a perfect field. | F.3.1 | This is Oda's canonical module comparison, not a canonical vector-space splitting. |

## II.RH19 — Polarization and real Frobenius meet in the positive Weil form

Witness: 18/034 normalizer formula; 037; 038 cancelled normalizers. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 218.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH19.01 | PROVED | The stated Weil form is positive definite after the prescribed involution and sign normalization. | C.5.1 | Its scalar Tate value is normalized exactly as in that proof. |

## II.RH20 — The nonlinear real-section map has a precise linear image

Witness: 18/034,037 real Frobenius; 039–040 real descent. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 224.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.RH20.01 | PROVED | Real hyperbolic-curve section classes recover real connected components. | F.3.6; Pál Theorem 1.3 | Individual points are not recovered by the component set. |
| II.RH20.02 | PROVED | The conjugation action on geometric abelianization is independent of the section class. | F.3.6, inner-conjugation calculation | The full abelianized extension or section cocycle can contain more data; only the action is computed. |

## II.P01 — The new problem sheet supplies the programme for the lattice construction

Witness: 18/043:L8–22. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 232.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P01.01 | PROVED | The Betti–de Rham comparison, including real structures and splittings, is constructed with the stated dependence on topology. | A.1–A.2; B.3.1–B.3.2; C.4 | The original question status remains part of the witness. |
| II.P01.02 | PROVED | The Betti–ℓ-adic comparison and embedded integral lattices have the exact coefficient maps in D. | D.1.1; F.1.6 | The original question status remains part of the witness. |
| II.P01.03 | PROVED | The de Rham–p-adic comparison has the specified admissible period-ring constructions. | B.2.1–B.2.3; B.3.3 | These constructions are supplied here, not read into the historical sheet. |
| II.P01.04 | PROVED | Characteristic-p cohomology has the listed crystalline, rigid, and prismatic realizations with their exact hypotheses. | B.3.4; F.3.1 | The question marks in the witness are retained. |

## II.P02 — The product-of-elliptic-curves dimension count is explicit

Witness: 18/045:L2–14. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 238.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P02.01 | PROVED | For two non-CM geometrically nonisogenous elliptic curves, the product motivic group has dimension 7 and the product parabolic dimension 5. | D.2.1; D.3.2 | CM or isogenous cases need their different groups; the numerical assertion is not unconditional in E,E′. |
| II.P02.02 | PROVED | The written filtration map has a geometric source and target of the displayed dimensions. | D.2.1; A.1.1 | These dimensions alone do not compute the undefined coefficient field K. |

## II.P03 — The author explicitly rejects a dimension-six count for this K

Witness: 18/045:L12; earlier witness reported in PN P18, 18/012:L2–24. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 244.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P03.01 | DOCUMENTARY-GAP | The field K on 18:45 is defined well enough to test the numerical value 6. | D.2.1 | Its generators and base field are absent; retain the exact source gate. |
| II.P03.02 | REFUTED | Lead H5 validly refutes the full period conjecture from the displayed number 6. | D.2.1 | The omitted field definition prevents that inference. |

## II.P04 — The relative-position quotient accounts for the bound (n−1)d

Witness: 18/047:L12–20,42; 18/049:L2. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 250.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P04.01 | PROVED | The simultaneous relative quotient has dimension at most (n−1)dim G with the stated exact quotient map. | D.1.2 | Actual transcendence-degree equality requires the corresponding genericity input. |

## II.P05 — The literal products leave a topology question

Witness: 18/047:L18; 18/049:L8–12; 18/051:L10–12; 18/055:L4. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 256.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P05.01 | PROVED | The finite coefficient rings Q⊗Zhat, A_f, and the full product of Q_ℓ have the exact embeddings specified in D. | D.1.1 | Do not use an unqualified product sign for all three. |
| II.P05.02 | REFUTED | The full product of Q_ℓ can replace the restricted finite adeles in the compact-open arguments. | D.1.1, additive-group and tuple (1/ℓ) tests | The compact-open and integrality conditions require the restricted product. |

## II.P06 — “Tate renforcée” is stated as adelic finite index

Witness: 18/049:L4–5. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 262.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P06.01 | REFUTED | The general strengthened Tate statement gives finite-index adelic image for the entire motivic group. | D.4.2, the actual Tate motive Q(-2) | With its stated integral group model G_m, the image is (Zhat^times)^2, of infinite index by the square-class quotient at arbitrarily many odd primes. The map from the Q(-1) tensor group is explicitly t to t^2. D.3.2 retains the named elliptic open-image cases. |
| II.P06.02 | PROVED | The stated non-CM elliptic and independent-product cases have the requisite open images. | D.3.2 | All named hypotheses of the opened theorems are retained. |

## II.P07 — The componentwise-generic coset lemma is expressly admitted

Witness: 18/049:L5–13; 18/051:L2,10. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 268.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P07.01 | PROVED | Every coset of an open compact subgroup contains a point generic over a countable coefficient field. | D.3.1 | The proof uses the exact adelic setting and Baire/measure argument stated there. |
| II.P07.02 | PROVED | The same argument gives simultaneous genericity against the specified countable family. | D.3.1 | None. |

## II.P08 — A complete integral-product test of the coset lemma for Gm

Witness: 18/049:L8–12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 274.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P08.01 | PROVED | For G_m the generic-coset argument can avoid each countably many polynomial zero conditions inside the indicated unit neighbourhood. | D.3.1 | This is the torus instance, not density of Q×. |

## II.P09 — The approximation hypothesis has a concrete scalar obstruction

Witness: 18/051:L4–8. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 280.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P09.01 | REFUTED | Diagonal Q× is dense in A_f×. | D.4.1, explicit neighbourhood obstruction | The restricted multiplicative topology and global rational unit constraints are retained. |
| II.P09.02 | PROVED | The connected affine groups satisfying the approximation property have the criterion stated in D. | D.4.1 | The reductive/unipotent quotient and simply connected covers are handled by the cited exact criterion. |

## II.P10 — The changes of place depend on M, and one word reverses the expectation

Witness: 18/051:L8. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 286.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P10.01 | PROVED | Plain integral comparison data do not universally recover an archimedean place, even with all specified tests. | E.2.1; D.6.1 | The concrete pair of places and compatible comparison maps are constructed. |
| II.P10.02 | READING | The est/pas reading in the place-dependence sentence is resolved by the counterexample. | Frozen witness 18/051; original cote18 PDF51/archive p.50, lower crop at300dpi | Two independent inspections of the original full page and lower crop do not securely distinguish est from pas. The clear est above supplies a comparison but does not settle the disputed stroke. Both readings and their mathematical analyses are retained; the counterexample does not decide paleography. |

## II.P11 — The claimed equivalence keeps two named inputs

Witness: 18/051:L10–12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 292.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P11.01 | PROVED | The margin equivalence is true for the precise two-input formulations stated in D. | D.4.2 | The exact subgroup and closure conditions must be included. |
| II.P11.02 | REFUTED | The broader reading of that equivalence without those inputs is universally true. | D.4.2, explicit counterexamples | The proof identifies the failed implication for each reading. |

## II.P12 — The automorphism group contains an explicit geometric kernel

Witness: 18/053:L14–18,27–33; 18/061:L17. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 298.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P12.01 | PROVED | Restriction Aut(k/k_0)→Gal(k_0bar/k_0) is surjective with kernel Aut(k/k_0bar) in the stated algebraically closed setting. | D.5.1 | No topology is suppressed. |
| II.P12.02 | PROVED | For positive transcendence degree the pointwise topology on the abstract automorphism group need not be compact. | D.5.1 | The translation family gives the explicit obstruction. |

## II.P13 — The diagonal integral ambiguity is the mechanism for uniqueness

Witness: 18/055:L13–15; 18/057:L4–8. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 304.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P13.01 | PROVED | A fixed integral comparison matrix maps diagonally through Z→Z_ℓ and its ambiguity is determined by that integral structure. | D.5.1; D.1.1 | This computes the map after a comparison exists. |
| II.P13.02 | REFUTED | Such an integral comparison exists for every pair of relevant places or elliptic realizations. | D.5.2 | The CM ideal-class example gives the exact obstruction. |

## II.P14 — The cardinal-two statement is cancelled and has a precise stabilizer test

Witness: 18/055:L24–34; 18/057:L4–12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 310.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P14.01 | PROVED | The fibre stabilizer is Γ∩{id,c_v}; its cardinality is one or two according to the base-fixing condition. | D.5.1 | The erased universal cardinality two is replaced by this exact formula. |
| II.P14.02 | READING | The fibre-cardinality-two passage is cancelled. | Frozen witness 18/057 | Cancellation is retained. |

## II.P15 — Inversion gives the exact morphism between the two cocycle conventions

Witness: 18/057:L20–26; 18/059:L2. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 316.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P15.01 | PROVED | The two multiplication conventions are related by inversion and have the specified cocycle equations. | A.5.3; D.5.1 | Do not interchange left and right cocycles without this conversion. |

## II.P16 — The torsor identification is marked “À vérifier / OK”

Witness: 18/059:L2–5. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 330.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P16.01 | PROVED | The actual tensor-Isom scheme descends as the stated fpqc torsor. | A.5.1; D.5.1 | Use effective algebraic descent, not arbitrary set-theoretic Aut(k/k_0) data. |
| II.P16.02 | REFUTED | An arbitrary abstract automorphism descent datum on the unspecified object is effective algebraic descent. | F.3.11, discontinuous action on a two-point finite etale scheme | The exact semilinear action uses a discontinuous quotient of the multiquadratic Galois group and cannot descend. The actual tensor-Isom fpqc torsor of II.P16.01 remains proved; it is not identified with the counterexample. |

## II.P17 — A written period-genericity conjecture is present on scan 059

Witness: 18/059:L7–12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 336.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P17.01 | PROVED | Genericity over k_0 and closedness after scalar extension to k are related by the exact period-locus base-change maps. | A.5.1 | Keep the base fields in each closure. |

## II.P18 — The correction of multiplication order yields a checkable orbit map

Witness: 18/061:L2,9. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 342.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P18.01 | PROVED | For φ(σ)=(σg)^−1g the orbit map x↦x^−1g has inverse y↦gy^−1, giving the exact image-locus formula. | A.5.1 | None. |
| II.P18.02 | PROVED | The resulting locus formula gives the precisely stated density criterion. | A.5.1 | It is a criterion, not proof that every arithmetic point meets its genericity premise. |

## II.P19 — Minimal transcendence degree of a definition field does not erase the π qualification

Witness: 18/053:L14; 18/059:L12. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 357.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P19.01 | PROVED | A field of definition can absorb a transcendental comparison parameter even for a genuine motive. | A.5.4; D.5.4 | The explicitly constructed elliptic/Tate examples determine the resulting cocycle image. |
| II.P19.02 | REFUTED | The unfinished π qualification is sufficient for the universal intended conclusion. | D.5.4 | The displayed strengthened counterexample preserves π transcendental over the chosen field. |

## II.P20 — The semidirect product realizes the cocycle as an actual homomorphism

Witness: 18/057:L22–26; 18/061:L11–17. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 369.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P20.01 | PROVED | The cocycle defines a homomorphism only after passage to the stated semidirect product. | A.5.3 | The group law and action are explicit. |
| II.P20.02 | REFUTED | The same cocycle is automatically a homomorphism into G with its ordinary multiplication. | A.5.3, translation example | The cocycle action cannot be omitted. |

## II.P21 — Openness of the adelic closure is the author's expectation

Witness: 18/061:L17–18. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 375.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P21.01 | REFUTED | The Euclidean/adelic closure of the image is universally open as expected in the sheet. | D.5.3, Tate counterexample | The exact remaining elliptic image question is separately recorded there. |

## II.P22 — The place-change formula gives the exact cohomology-class relation

Witness: 18/062:L5–42. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 381.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P22.01 | PROVED | Changing the place changes the cocycle by the explicitly computed cochain/conjugacy transport. | D.5.1 | The chosen identifications are included in the formula. |

## II.P23 — Assessment of the supplied Hua synopsis

Witness: 18/047,053,055,057,059,061,062. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 387.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P23.01 | DOCUMENTARY-GAP | The condensed Hua synopsis contains a complete proof of all its descent, action, and density assertions. | A.5.1–A.5.3; D.5.1 | Only its fully stated components are proved; obtain any missing quantified statement before assigning a theorem status. |

## II.P24 — The current torsor witness has a checked modern comparison

Witness: 18/059:L4–11. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 393.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P24.01 | PROVED | The Bost–Charles tensor-Isom torsor construction gives the stated algebraic maps and orbit closure. | A.5.1 | The actual period locus and its generated torsor are retained separately. |

## II.P25 — Grothendieck's own printed period witness can be cited directly

Witness: 18/045:L12; 18/059:L7; compare earlier PN P20 and P22, 18/012–013. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 399.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P25.01 | PROVED | The exact printed period-independence witness is Grothendieck 1966, p.102 note 10. | G and its source record | This is a checked literature witness, not a date for the archive sheet. |

## II.P26 — Density of the image has an explicit test against density of its generated subgroup

Witness: `18/059`, “image Zariski dense”; `18/061`, corrected coboundary. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 405.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.P26.01 | PROVED | The actual cocycle image and the subgroup it generates can have different Zariski closures. | A.5.2, quadratic-field G_m example | The image is the explicit two-point set; its generated subgroup is dense. |

## II.MB01 — An explicit realization morphism connects correspondence calculations to the later motive notation

Witness: 18/025, “\(\xi(z)(x)=\operatorname{pr}_{2*}(\operatorname{pr}_1^*(x)P_{\mathrm{top}}(z))\)”; 18/027, “sur la catégorie des motifs”. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 413.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB01.01 | PROVED | A codimension-r correspondence from X acts in degree i+2r−2dim X and twist r−dim X. | F.1.3 | None. |
| II.MB01.02 | PROVED | Correspondence composition and comparison compatibility follow from the triple-product push–pull formula. | F.1.3 | None. |

## II.MB02 — The generated category supplies a concrete target for the correspondence programme

Witness: 18/055, “motifs subordonnés à \(M\)”; 18/037, “\(G=\operatorname{Aut}^{\otimes}(T_B)\)”. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 419.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB02.01 | PROVED | Tensor automorphisms satisfy g_N ω(a)=ω(a)g_M on each morphism. | F.3.4 | None. |
| II.MB02.02 | PROVED | The neutral rigid abelian fibre-functor construction reconstructs C as Rep(G). | F.3.4; Deligne–Milne Theorem 2.11 | The category and fibre-functor hypotheses are part of the statement. |

## II.MB03 — The partial-inverse lowering operator has an explicit rational conversion to the \(\mathfrak{sl}_2\) lowering operator

Witness: 18/027, \(H^2(\mathbf P^1)=\mathbf Z(-1)\), provides a new elementary test object; the relevant operator formulas are CT16/013–014 and 033. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 425.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB03.01 | PROVED | The specified E,F,H matrices satisfy the three sl_2 commutator identities on every primitive string. | F.3.2, basis-vector proof and exact certificate | None. |
| II.MB03.02 | PROVED | The partial-inverse lowering operator and sl_2 lowering operator have the displayed rational conversion coefficients. | F.3.2 | The operator normalization is specified, not silently replaced. |
| II.MB03.03 | REFUTED | Those formulas yield equality of the integral operator rings without further divisibility conditions. | F.3.2, m=2 modulo 2 counterexample | The rational denominators are essential on the chosen lattice. |

## II.MB03b — The two rational operator images have explicit matrix units

Witness: CT16/013–018,033; current 18/027. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 431.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB03b.01 | PROVED | B_m=BΛ^mTE^mB projects to the bottom of the unique length-m string. | F.3.2 | None. |
| II.MB03b.02 | PROVED | E^b B_m Λ^a are the matrix units identifying Q[E,Λ] with the product of full matrix algebras. | F.3.2 | Multiplicity spaces carry the identity action. |
| II.MB03b.03 | PROVED | Casimir and H interpolation recover the same matrix units from E,F,H over Q. | F.3.2 | The equality is of actual subalgebras of End(W). |

## II.MB04 — \(\mathbf P^1\) gives both the failed factorization and the surviving relation

Witness: 18/027, “\(\xi(\mathbf Z(-1))\)”. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 437.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB04.01 | PROVED | The displayed P^1 Lefschetz representation cannot factor through diag(1,z), since it moves the unit vector. | F.3.3 | This is the precise failed factorization, not a categorical unrelatedness assertion. |
| II.MB04.02 | PROVED | The Tate torus conjugates E and F by z and z^−1, and E:h^0→h^2(1) is equivariant. | F.3.3 | None. |

## II.MB05 — Cohomological grading and Lefschetz Cartan grading differ by a computed scalar

Witness: 18/027, Tate object; 18/034, \(\varepsilon:G\to\mathbf G_m\) in the margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 443.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB05.01 | PROVED | λ_X(t)=t^−d w_X(t), and both conjugate a degree-j endomorphism by t^j. | F.3.3 | None. |
| II.MB05.02 | PROVED | The tensor weight gives εw=t², while the specified filtration splitting gives εj=t. | F.3.3 | The Levi and full-group domains are stated explicitly. |

## II.MB06 — The elliptic \(\mathrm{SL}_2\) factors have a direct action test

Witness: 18/045, “\(G\overset{\mathrm{isog.}}{\simeq}\mathrm{Sl}(2)\times\mathrm{Sl}(2)\times\mathbf G_m\)”; the non-isogeny words remain uncertain in the frozen reading. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 449.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB06.01 | PROVED | The Lefschetz operators vanish on elliptic H^1, so the nontrivial standard period action is not their action. | F.3.3 | The exact matrices and target degrees prove the comparison. |

## II.MB07 — A partial A–D dictionary is supported by operators, not by matching letters

Witness: current 18/025–027 uses correspondence realizations but supplies no A–D definition; the operative historical statements are CT16/044–049. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 455.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB07.01 | PROVED | The operational first and third manuscript letters have the two printed standard-conjecture matches. | F.3.5; I.M04 | Only the matched operational definitions are asserted. |
| II.MB07.02 | DOCUMENTARY-GAP | The remaining two letter identifications have secure definitions in this packet. | F.3.5; I.M04; original cote 14 pp.43–44 and complete Coates letters | The newly opened 1965 Serre letter defines its B by primitive positivity, with an explicit cycle-class quotient to the cohomological convention. The specific B and D of the 1967 Coates letter still lack standalone definitions in the inspected sources. |

## II.MB08 — The singular-hypersurface programme has one direct supplied witness and an absent target

Witness: CT16/047, “work also with singular ones”; current 18/025–027 does not mention such a reduction. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 461.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB08.01 | DOCUMENTARY-GAP | The cote14 pages implement the proposed singular-hypersurface programme. | I.M05.01; F.3.14; original cote14 PDFs111–113 and131; complete Coates 1967 letter p.4 | F.3.14 supplies the exact finite normalization map and the nodal ordinary-cohomology comparison. The newly inspected original Lefschetz and generic-member pages have not identified execution of the particular historical standard-conjecture proposal; this documentary gate remains. |

## II.MB09 — The arithmetic motivic sequence over \(\mathbf Q\) has explicit functors and a checked modern source

Witness: 18/034, “\(G/G^0\)”; 18/057, \(\varphi_v:\operatorname{Gal}(k/k_0)\to G(k)\). Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 467.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB09.01 | PROVED | The rational arithmetic Nori motivic sequence is exact with proconstant Galois quotient. | F.3.4; Kahn 2025 Theorems 5.10,10.2 | The 2025 proof fixes the older normality gap. |
| II.MB09.02 | OPEN | That sequence has a canonical splitting or kernel equal to the identity component in the unspecified generality. | F.3.4 | Neither property is supplied by exactness; the intended additional statement must be specified and proved. |

## II.MB10 — Nori/Ayoub provides a Hopf-algebra isomorphism for the group question

Witness: 18/037, “\(G=\operatorname{Aut}^{\otimes}(T_B)\)”; 18/055, tensor-generated category. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 473.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB10.01 | PROVED | The Ayoub–Nori Hopf maps are inverse over the stated principal ideal coefficient domain. | F.3.4; Choudhury–Gallauer Theorem 9.1 | None within the source's hypotheses. |
| II.MB10.02 | PROVED | The pure rational Nori–André comparison is an equivalence compatible with Betti realization. | F.3.4; Arapura Theorem 6.4.1 | No equality of all motivated and algebraic cycles is inferred. |

## II.MB11 — Hodge fullness is explicitly a conjectural input on the new sheet

Witness: 18/034, “pleinement fidèle en vertu des conj. de Hodge”. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 479.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB11.01 | PROVED | Hodge realization is full on the specified abelian-generated pure category. | F.3.4; Arapura Corollary 7.1.4; C.1.1 | None within that scope. |
| II.MB11.02 | OPEN | General Nori Hodge fullness and the proposed general essential image are established. | F.3.4; Arapura Conjectures 7.1.1–7.1.2 | The conjectural fullness and essential-image obligations remain. |

## II.MB12 — Numerical semisimplicity is linked by the quotient on correspondence spaces

Witness: 18/025, cohomological correspondence action; 18/037, tensor automorphisms. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 485.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB12.01 | PROVED | The homological-to-numerical quotient is the surjective identity-on-cycles map. | F.3.5 | None. |
| II.MB12.02 | PROVED | The numerical category is semisimple; cohomology descends exactly when the quotient kernel acts trivially. | F.3.5; Jannsen Theorem 1 | The factorization criterion is proved as an equivalence of the actual maps. |
| II.MB12.03 | OPEN | The kernel-annihilation criterion holds on every relevant product without further input. | F.3.5; F.3.35; F.3.36 | F.3.35 proves the arbitrary-characteristic abelian dimension<=4 case and its stated dim<=2 generator category. F.3.36 proves characteristic-zero numerical=homological equivalence for every smooth projective variety of dimension<=4 and every abelian variety in arbitrary dimension, with full tensor/category/projector comparison on abelian motives. The kernel-annihilation condition on all remaining relevant smooth-projective products is still open. |

## II.MB13 — The Hom comparison has a common number-field base and an abelianization morphism

Witness: 18/027, \(\ell\)-adic comparison; 18/055, generated category; earlier map-reconstruction wording is PN A39 (15/227). Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 491.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB13.01 | PROVED | Curve-to-Jacobian abelianization relates Mochizuki's nonlinear Hom map to Tate/Faltings linear Hom maps. | F.3.6 | The primes and field hypotheses of each theorem are retained. |
| II.MB13.02 | REFUTED | Every Jacobian linear map in those Hom spaces arises from a curve morphism. | F.3.6, multiplication by 2 and Riemann–Hurwitz | This explicit obstruction is the only non-surjectivity conclusion used. |

## II.MB14 — Semisimplicity and centres can be compared through conjugation

Witness: 18/027, Tate object; 18/037, \(G=\operatorname{Aut}^{\otimes}(T_B)\). Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 497.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB14.01 | REFUTED | Semisimplicity implies centre-freeness. | F.3.5, G_m character decomposition | None. |
| II.MB14.02 | PROVED | The centre-free geometric fundamental group gives the pullback reconstruction through Aut→Out. | F.3.6 | The homomorphism, its kernel, and its surjectivity are explicit. |

## II.MB15 — The weight obstruction and the cyclotomic conjugation map must both be retained

Witness: 18/027, Tate line; 18/057, arithmetic cocycle. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 503.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB15.01 | PROVED | Stix's cusp-inertia criterion requires non-Tate weights, open normalizer image, and cyclotomic conjugation. | F.3.6; Stix Definitions 26,29 and Theorem 30 | None for the fully stated criterion. |
| II.MB15.02 | REFUTED | The truncated LM6 statements already supply every premise of that criterion. | F.3.10; F.3.15-F.3.17; full LM6 A.50 pp.33-34; Nakamura1994 Theorem2.1.1 p94; F.3.18; F.3.19; F.3.20; F.3.21; F.3.22; F.3.23; F.3.24; F.3.25; F.3.26; F.3.27; F.3.28; F.3.29; F.3.30; F.3.31; F.3.32; F.3.33; F.3.34 | The truncated statements do not contain all maps and premises of the old proposed criterion, so that claim remains refuted. F3.32 now supplies a complete new route for the original CM full-profinite subgroup problem: the exact all-genus single-line q6 theorem, actual F3.31 proper-homology/normal-core/filling composite, and I intersection R=1. The former arbitrary-cover CM-factor/paired-orbit and all-s matrix obligations are superseded by this single-line proof. F3.33 now proves the general affine number-field classification and the corresponding common-kernel exclusion through its explicit covering maps. Earlier progress and stopping-point notes are preserved verbatim in work/audit_after11_superseded_scopes.json. F3.34 independently reconstructs the specific all-genus R-vanishing step from six actual Johnson brackets, determinant-203784 and the older published multiplicity bound; the 2026 sketch supplies the formula attribution, while the older dimension input remains explicit. |

## II.MB16 — Integral comparisons on 18/055 carry additional data visible in the formula

Witness: 18/055, “\(M_w^{\mathbf Z}=gM_v^{\mathbf Z}\)” and “mod. multiplication à droite … \(G(\mathbf Z)\)”; 18/049, “Tate renforcée”. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 509.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.MB16.01 | PROVED | An integral group comparison transports a chosen integral representation and its lattice. | F.3.4; Choudhury–Gallauer Theorem 9.1 | None. |
| II.MB16.02 | REFUTED | The rational representation or Hopf comparison by itself chooses the required integral lattice and all its forms. | F.3.4; D.5.2 | A lattice and its equivalence relation are extra specified data. |

## II.SF10 — 18/034, final sentence

Witness: 18/034, final sentence. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 697.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF10.01 | OPEN | The Hodge-fullness conjecture in the general algebraic-cycle setting is settled by the real formulation. | C.1.2; II.RH05 | The exact cycle-surjectivity premise remains. |
| II.SF10.02 | PROVED | The abelian absolute-Hodge real formulation is fully faithful with its stated essential image. | C.1.1 | None within that category. |

## II.SF11 — 18/035, tensor question

Witness: 18/035, tensor question. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 703.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF11.01 | PROVED | The naive projection has the minus-times-minus tensor defect, repaired by the specified tensor structure. | C.2.1; II.RH06 | None. |

## II.SF12 — 18/035, final paragraph

Witness: 18/035, final paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 709.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF12.01 | PROVED | The Artin and Tate tests determine the nontrivial and trivial fibre-functor torsor examples respectively. | C.2.2; II.RH07 | Do not use the naive projection as a tensor isomorphism. |

## II.SF13 — 18/036, cancelled opening argument

Witness: 18/036, cancelled opening argument. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 715.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF13.01 | READING | The stronger HC/even-Tate paragraph is deleted in the frozen witness. | Frozen witness 18/037 | Retain cancellation even where its surviving mathematical claims have counterexamples. |
| II.SF13.02 | REFUTED | The cancelled even-Tate conclusion holds universally. | C.3.1 | The Artin–Tate counterexample applies to the indicated conclusion. |

## II.SF14 — 18/036, live converse and lower margin; 18/038, restatement

Witness: 18/036, live converse and lower margin; 18/038, restatement. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 721.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF14.01 | REFUTED | The live even-Tate iff claim holds in the stated real motivic category. | C.3.1 | Use the proved Artin–Tate replacement. |
| II.SF14.02 | PROVED | The correct f_∞=1 criterion is the specified Artin–Tate decomposition. | C.3.1 | Retain the category hypotheses. |

## II.SF15 — 18/038, lower paragraph

Witness: 18/038, lower paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 727.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF15.01 | READING | The maximal-compact normalizer discussion and its weight quotient are withdrawn. | Frozen witness 18/038; II.RH13 | No uncancellation is inferred from a modern proof. |
| II.SF15.02 | PROVED | The weight-zero centralizer is maximal compact under the polarizable finite-generator hypotheses. | F.3.7 | The raw group has the explicit Tate counterexample. |

## II.SF16 — 18/039, opening and final paragraphs

Witness: 18/039, opening and final paragraphs. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 733.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF16.01 | PROVED | Fixed-topology complex transport uses only identity and conjugation and preserves the stated integral lattice. | C.4.1; F.1.6 | Do not extend this two-element ambiguity to all abstract embeddings. |

## II.SF17 — 18/043, problem 3

Witness: 18/043, problem 3. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 739.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF17.01 | PROVED | Problem 3 admits the stated local comparison constructions. | B.3.3 | All coefficient, reduction, filtration, and descent hypotheses remain. |

## II.SF18 — 18/043, problem 4

Witness: 18/043, problem 4. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 745.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF18.01 | PROVED | Problem 4 admits the specified characteristic-p cohomology and Frobenius structures. | B.3.4 | No universal motivic classification is asserted. |

## II.SF19 — 18/045, upper calculation

Witness: 18/045, upper calculation. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 751.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF19.01 | DOCUMENTARY-GAP | The formula involving K on 18:45 has a fully specified field and degree. | D.2.1 | Recover K's generators and base field. |

## II.SF21 — 18/049, first paragraph

Witness: 18/049, first paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 763.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF21.01 | REFUTED | The strengthened Tate open-image assertion holds for every motive. | D.4.2, Q(-2) and the central isogeny t to t^2 | The actual image in the stated integral G_m model is (Zhat^times)^2, whose square-class quotients at arbitrarily many odd primes prove infinite index. The named elliptic statements in D.3.2 remain proved. |
| II.SF21.02 | PROVED | Those named elliptic cases satisfy the needed open-image hypotheses. | D.3.2 | None within the exact theorem scopes. |

## II.SF22 — 18/049, lemma; 18/051, opening and margin

Witness: 18/049, lemma; 18/051, opening and margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 769.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF22.01 | PROVED | An open compact coset contains a point with the stated maximal algebraic independence over a countable field. | D.3.1 | None. |

## II.SF24 — 18/051, approximation argument

Witness: 18/051, approximation argument. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 781.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF24.01 | PROVED | The precise approximation property has the connected-affine-group criterion and counterexamples in D. | D.4.1 | No universal approximation is asserted. |

## II.SF25 — 18/051, bracketed expectation

Witness: 18/051, bracketed expectation. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 787.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF25.01 | READING | The dependence sentence admits the recorded est/pas alternatives. | Frozen witness 18/051; original cote18 PDF51/archive p.50; II.P10.02 | Original page and lower300dpi crop were independently inspected by root and period_triangle on19November2026. The disputed word remains unsafe; keep both alternatives. The mathematical plain-data counterexample is E.2.1. |
| II.SF25.02 | REFUTED | The strongest plain integral-data reading universally recovers the archimedean place. | E.2.1; D.6.1 | The actual compatible counterexample is constructed. |

## II.SF26 — 18/051, margin

Witness: 18/051, margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 793.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF26.01 | PROVED | The exact two-input equivalence asserted in the margin is valid in the formulations of D. | D.4.2 | Broader readings have the displayed counterexamples. |

## II.SF27 — 18/055, category-generated comparison

Witness: 18/055, category-generated comparison. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 799.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF27.01 | REFUTED | The desired integral comparison exists without an integral-lattice obstruction. | D.5.2 | The CM ideal-class example is the counterexample. |
| II.SF27.02 | PROVED | Once a comparison exists its ambiguity and finite realizations are given by the stated integral maps. | D.5.1; D.1.1 | Existence is not inferred from that ambiguity computation. |

## II.SF28 — 18/055, boxed note and following map

Witness: 18/055, boxed note and following map. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 805.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF28.01 | READING | The universal two-point fibre statement is cancelled. | Frozen witness 18/057 | Retain cancellation. |
| II.SF28.02 | PROVED | The exact stabilizer formula determines when the fibre has one or two elements. | D.5.1 | The conjugation must fix the base in the two-element case. |

## II.SF29 — 18/057, cocycle display

Witness: 18/057, cocycle display. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 811.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF29.01 | PROVED | The cocycle and left/right conversion are the exact formulas of A.5.3 and D.5.1. | A.5.3; D.5.1 | None. |

## II.SF30 — 18/059, torsor paragraph and margin

Witness: 18/059, torsor paragraph and margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 817.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF30.01 | PROVED | The actual tensor-Isom object is an algebraic torsor with the stated descent maps. | A.5.1; D.5.1 | This does not certify arbitrary abstract automorphism data as effective descent. |

## II.SF31 — 18/059, genericity paragraph

Witness: 18/059, genericity paragraph. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 823.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF31.01 | PROVED | The genericity condition translates to the precise orbit-locus statement. | A.5.1 | The arithmetic genericity premise remains the named period assertion. |
| II.SF31.02 | OPEN | That period-genericity premise holds for every motive in the proposed scope. | A.2.4; A.5.1 | Only the established cases and the requested implication are proved. |

## II.SF32 — 18/059, unfinished margin

Witness: 18/059, unfinished margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 829.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF32.01 | PROVED | The π qualification is necessary in the exhibited Tate situation but insufficient for the proposed universal conclusion. | D.5.4 | The two exact examples retain the field definitions. |
| II.SF32.02 | READING | The margin's unfinished condition has a uniquely determined complete formulation. | Frozen witness 18/060 | It does not; preserve the unfinished expression. |

## II.SF33 — 18/061, first corrected formula

Witness: 18/061, first corrected formula. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 835.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF33.01 | PROVED | The action/cocycle pair is a homomorphism into the specified semidirect product. | A.5.3 | The ordinary-product homomorphism claim has the explicit counterexample. |

## II.SF34 — 18/061, final expectation and margin

Witness: 18/061, final expectation and margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 841.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF34.01 | REFUTED | The predicted Euclidean/adelic openness holds universally. | D.5.3 | The remaining specific elliptic assertion is recorded separately. |

## II.SF35 — 18/062, upper margin

Witness: 18/062, upper margin. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 847.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF35.01 | PROVED | The two place-dependent cocycles are related by the computed cochain transport. | D.5.1 | The comparison choices are part of the formula. |

## II.SF36 — 18/062, cancelled and boxed formulas

Witness: 18/062, cancelled and boxed formulas. Source: `background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md`, line 853.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| II.SF36.01 | PROVED | Place change gives the stated conjugacy/translation relation on the relevant images and closures. | D.5.1 | The unresolved reading of any truncated synopsis is not promoted to an additional theorem. |
| II.SF36.02 | READING | The live boxed change-of-trivialization formula retains the final inverse omitted in the cancelled line. | Frozen witness 18/062 | Both the cancellation and the corrected expression remain recorded. |

## I.ST01 — “Descriptions conjecturales” (twice); “Par quoi remplacer 1′,4′ ?? ”

Witness: 18/005:L2–28. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1318.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST01.01 | PROVED | The proposed local descriptions receive the exact rational, integral, and relative realization constructions of B. | B.1–B.3; F.3.1 | The six unspecified global essential images remain open as in I.P01. |
| I.ST01.02 | OPEN | Those local theorems establish all six global motivic classification claims. | I.P01; F.3.4 | Specify and characterize each global essential image. |

## I.ST02 — `\deleted{on est}\inserted{il semble qu’on sera}`; “on n’a pas développé”; “laisse au … lecteur … d’écrire”

Witness: 18/007:L10,17. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1319.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST02.01 | PROVED | Integral Chow specialization and its geometric ℓ-adic cycle-class square hold in the smooth proper complete-DVR setting. | F.3.8; I.P07; Fulton 20.3 | The SGA 6 mirror omits printed p.580; Fulton and Stacks supply the checked modern theorem. |

## I.ST03 — “Conj. de transcendance forte”; “alors ?”

Witness: 18/011:L65–76. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1320.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST03.01 | PROVED | The typed triangle, group dimensions, and exact conjugate-joint image dimensions are as in A. | A.1.1–A.2.4 | The unsupported universal g+u assertion is refuted in A.2.5. |
| I.ST03.02 | NAMED-CONJECTURE-IMPLICATION | The named joint period conjecture gives the corrected actual-point transcendence-degree table. | A.2.4 | This is a proved implication, not a proof of its arithmetic premise. |

## I.ST04 — “Conjecture … de transcendance”; “du moins si”; “Corollaire … Si G connexe”

Witness: 18/012:L5–11. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1321.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST04.01 | READING | The normalized-period draft remains wholly cancelled with its uncertain normalization. | I.P18; I.P26 | No chronology or resolved normalization is inferred. |
| I.ST04.02 | OPEN | The cancelled full normalized period-independence assertion is established. | I.P18–I.P21 | The specified arithmetic assertion is not proved; excluded full non-CM target remains excluded. |

## I.ST05 — “Contient le th. de Schneider”; “Si l’invariant j est transcendant”; `\unsure{connu!}`; deleted “π non Alg. sur k?”

Witness: 18/012:L13–26. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1322.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST05.01 | OPEN | The cancelled elliptic normalized independence, including its transcendental-j total-degree version, is established by Schneider's theorem. | I.P20–I.P21; A.3.1; G | The stronger independence is not proved; the field and normalization remain unspecified in the margins. |
| I.ST05.02 | READING | The uncertain known remark and deleted π-over-k question constitute a completed proof. | Frozen witness 18/012:L13–26 | They keep their own uncertain and deleted status. |

## I.ST06 — “4 ou 2?”; “A-t-on H=G”; “Peut-on avoir …”

Witness: 18/013:L6,9,12. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1323.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST06.01 | PROVED | The CM elliptic full period field has degree 2, and the elliptic period locus generates the full motivic torsor. | A.4.3; A.4.9 | These answer two precisely scoped parts of the live questions. |
| I.ST06.02 | OPEN | The non-CM full degree 4 is established. | I.P22; A.4.9 | That full period target is excluded and is not proved by torsor generation. |
| I.ST06.03 | OPEN | The non-CM algebraic Hodge splitting is impossible. | I.P24; A.4.13 | The scalar/χ* arithmetic specialization obligation remains. |

## I.ST07 — “pourvu … qu’il … existe un multiplicateur … λ^p”

Witness: 18/015:L20. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1324.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST07.01 | PROVED | There is one universal cycle-comparison multiplier λ=2πi, yielding λ^p in codimension p. | F.1.1 | Products, orientations, and supports provide the global proof. |

## I.ST08 — `\unsure{faire le raisonnement}`; “Provient de la comm. de”

Witness: 18/017:L2,25. Source: `background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md`, line 1325.

| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |
|---|---|---|---|---|
| I.ST08.01 | PROVED | The unfinished local-to-global commutativity argument is supplied by the support-localization and Gysin proofs. | F.1.1–F.1.2 | The proof is present here; the manuscript's sentence remains unfinished. |
| I.ST08.02 | READING | The marginal faire le raisonnement and final Provient de la comm. de have secure complete readings. | Frozen witness 18/017:L2,L25 | Retain both uncertainty and incompleteness. |

The all-genus completion and supersession records are in `audit_after11_CHECK_EVENTS.tsv`; earlier scope notes are retained verbatim in `audit_after11_superseded_scopes.json`.

The independent R-detector reconstruction and current source-dependency records are in `audit_after12_CHECK_EVENTS.tsv`.
