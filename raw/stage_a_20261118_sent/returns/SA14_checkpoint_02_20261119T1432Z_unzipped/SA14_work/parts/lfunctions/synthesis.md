# Cote 60: functional equations and the reused algebra sheets

This part consolidates all 139 indexed entries from `MPL_60_002-035` and `MPL_60_036-070`, after reading the complete notes, both complete transcriptions and both doubts files. It preserves two distinct bodies of material: Grothendieck's handwritten functional-equation investigation, and the printed Bourbaki drafts/editorial material on reused sheets. Physical reuse does not make the printed assertions his handwritten claims, and a printed imprint does not date the handwriting.

All line references are one-based physical lines of the named supplied `.tex` file. Scan numbers are its `\scanpage` values. There are no scans in the supplied materials, so the mathematical alarms are not decisions about ink and no transcription has been altered.

## 1. The handwritten line of work, in its own order

The opening pages develop characteristic functions of finite-dimensional endomorphisms: exterior traces give the determinant, symmetric traces give its reciprocal, exact sequences give ordinary multiplication, and tensor products give the operation now described by rational Witt multiplication. The λ/σ convention is revised in the text. The deleted generating identity is therefore retained as a withdrawal, not promoted into a competing surviving theorem. These calculations do not require semisimplicity (C-SA14-401–405; Deligne1973Constants §§10.3–10.5 and BGT2013Endomorphisms §§5–6).

The next step introduces Frobenius, motives, weights and selfduality. These pages use different hypotheses at different points. Purity controls complex absolute values. Rationality constrains the determinant. A perfect pairing supplies coefficient selfduality. Its alternating symmetry gives a positive normalized determinant. The later phrase admitting selfduality must remain attached to the earlier calculation. The independent rank-one and symmetric-pairing tests show the boundaries of these implications; they do not refute the rational polarized motivic setting. For q=p^a, rationality only forces a·rank·weight even, rather than rank·weight even by itself (C-SA14-406–416; CALC-03; Deligne1974WeilI and Deligne1980WeilII).

The proper functional equation is then derived from duality and alternating determinants. The text visibly replaces “compactifiable” by “proper.” In the nonproper case it introduces the difference between ordinary and compactly supported cohomology. Its natural derived representative is Cone(RΓ_c→RΓ), and dualizing this cone gives the shift−1 asked about on the page. The later discussion of cohomology at infinity is consistent with that convention. A¹ and G_m supply complete tests of the boundary factors. In particular, the two normalized determinants are reciprocal; their literal equality on scan27 fails for A¹. The proposed boundary “type” bound is a separate matter: no sufficient definition of type is present here (C-SA14-417–426,447; MP-SA14-403–405; proof_notes.md §§2–4).

The curve discussion turns from a generic representation to its extension across closed points. Ordinary inertia invariants are not exact. The skyscraper cokernel Q measures the failure and contributes a local factor. The literal restriction of its support to points where the quotient representation is ramified is too strong: a tame nontrivial extension of unramified endpoints already gives nonzero Q. The correct bound uses failure of exactness and is contained in the ramification locus of the middle representation. This example is mixed; it is not offered against a pure geometrically semisimple setting (C-SA14-427–432; CALC-07).

The author first proposes using global composition factors, then rejects that recipe for lack of locality and étale compatibility. The subsequent construction is local: pass to a normal subgroup of inertia acting unipotently, use a stable filtration and average over the finite quotient. This yields an additive virtual class independent of the chosen subgroup. It does not generally give a tensor fibre functor. The separate defect α need not be additive; the combination μ is additive and, under the stated quasi-unipotent hypotheses, vanishes by dévissage. That vanishing is our consequence of the stated construction, not an assertion that the author explicitly withdrew μ (C-SA14-433–441).

The final local calculations ask for the modified Euler characteristic and determinant, reaching a remaining sign. The exact curve answers are matched to the GOS framework and Laumon's sign-sensitive epsilon-product theorem, with closed-point degrees, an additive character and a differential retained. Several later displays lose a Tate shift that the defining μ formula requires. The ending normalization problem is more restricted than an ordinary rational cocycle equation: the correction must have lower niveau. The unrestricted rational solutions are elementary and are computed here, but the supplied text does not identify the allowed subgroup well enough to solve its actual restriction (C-SA14-442–451; MP-SA14-407–412; search groups LF-S04–06).

## 2. What the reused printed material contains

The even-numbered and intervening reused pages range much more widely. They include a covering-ratio/ultrafilter construction of Haar integration; finite-length duality over a PID and injectivity; trace-dual orders, differents, conductors and local Gorenstein criteria; determinantal ideals; formal power-series rings; characteristic-two derivations and divisor class groups; rank reduction and reflexive lattices; scalar extension/restriction; cyclotomic and differential examples; and editorial reports. These are indexed with explicit printed-source attribution.

Several assertions absent from the original note headings were therefore added to the claims map. The complete printed corpus is not reduced to an appendix title or a script-generated catalogue. Proofs and exact source matches are in `proof_notes.md` §§5–13 and `literature_notes.md` §§3–5. The particularly useful distinctions are these:

| Issue | Checked conclusion | Records |
|---|---|---|
| “Degree” defined by a least primary-power exponent | It is not local colength: the cusp ideal t⁴C has least exponent3 but colength4. | C-SA14-462–463,562; CALC-11 |
| Global conductor expressed through trace duals | It needs reflexivity of C or height-one localization. A characteristic-zero full order has conductor (x,y)B but B*:C*=B. | C-SA14-467,564; CALC-21 |
| Different multiplier criterion | The exact local converse D:D=C iff the canonical trace dual is invertible has an independent socle proof. | C-SA14-563; proof_notes.md §6 |
| Quotient criterion C*/C≅C/D | Both directions are proved, including semilocal orders, by regular trace on the Artinian fibre. | C-SA14-472; proof_notes.md §6 |
| Hensel factorization | The printed residual factorization needs a coprimality condition; X²−p supplies a counterexample to the literal version. | C-SA14-501; CALC-19 |
| Companion formal series | The nonnegative range fails; the separate within-block hint divides by the wrong variable. The positive-exponent theorem has a full corrected block proof. | C-SA14-503,565,567; CALC-22,25 |
| Fitting quotient inclusion | Fitting ideals increase under a quotient; the adjacent extension convolution remains valid. | C-SA14-546–547; CALC-13 |
| Relative lattice monotonicity | Signed exponents allow failure unless N⊂M. | C-SA14-488–489; CALC-13 |
| Reflexive evaluation test | Finite torsion-free E is enough; E is projective iff E*⊗E is reflexive. | C-SA14-550–551 |
| Hom–Ext reflexivity test | The literal statement needs E≠0; with that condition the implication is proved. | C-SA14-556 |
| Finite normal extension | Height-one formulas survive while codimension-two tensor and reflexivity defects may remain. | C-SA14-531–537,548–549; CALC-15 |

The strongest new source identification came from following Samuel's references backward. The exact unit-logarithmic-derivative lemma and N(i,j) subgroup occur in his Dubreil exposé and official TIFR lectures. The weighted-cyclic criterion, including both printed alternatives, occurs in TIFR Theorem8.1 and *Méchants anneaux*, Proposition2. The latter's Proposition1 explicitly requires positive exponents, corroborating the formal-series repair. These are established printed assertions, not previously unknown problems. The cut derivation fragment on scan36 also matches a published example, but its missing antecedents are labelled as an external reconstruction (C-SA14-492–497,514–515,518,565).

Chronology remains separate from identification. The Dubreil talk is dated19November1962, but the surviving text cites1965 publications. That surviving revision cannot simply be assigned the talk date. The secure1964 publications and later exact statements are reported without dating the handwriting or claiming historical influence.

## 3. What was retained and corrected in the earlier notes

Most earlier entries already made useful distinctions: proper versus nonproper duality, purity versus selfduality, normalized versus raw eigenvalues, boundary cone versus virtual difference, ordinary invariants versus averaging, and printed versus handwritten content. Merging repeated questions removes duplication without erasing the places where the argument changes.

The one source-entry verdict changed to “corrected” is `MPL_60_002-035#72`. Its broad order discussion was sound, but it omitted the global nonreflexive conductor defect. Other mathematical repairs generally confirm concerns already raised in the notes, so they do not require changing those note verdicts to “corrected.” A false literal formula and a correct note that diagnoses it are different objects in this dossier.

The earlier context comparisons are retained with strict limits. Oda and Jannsen provide verified published endpoints; the absent cote16/44/47/54 passages and named research registers do not become checked merely because a related publication was opened. The LM7, WG2, Hua and other project leads remain in their own table. No arithmetic section problem, motivic-category plan or height programme receives a status upgrade from these pages.

## 4. Completion and counts

The six stages are complete for the two assigned packages. Completion here means every supplied entry has a read verdict, every extracted claim has a searched fate, every explicit calculation has a saved check or a precisely identified missing antecedent, every source-limited problem is represented, and checked links are distinguished from unavailable endpoints. It does not mean that absent definitions, missing scans or the standard conjectures have been supplied.

| Register | Count and disposition |
|---|---|
| Source entries | 139:77 in the first package and62 in the second |
| Consolidated items | 93 |
| Entry verdicts | 92 kept;46 merged;1 corrected |
| Claims | 167, IDs C-SA14-401 through C-SA14-567 |
| Claims by class | A9;B13;C3;D0;E131;F11 |
| Status on pages | 12 proved there;75 proof sketched;54 stated without proof;13 false as stated;8 open on the pages;5 corrected by himself later |
| Problems | 16, including separately attributed printed/editorial questions |
| Scan-reading alarms | 53; none adjudicated without images |
| Checked links | 24, each with read endpoints |
| Quarantined context groups | 14, in a separate table |
| Ranked directions | 7, each with item, claim and problem IDs |
| Bibliography | 43 records:42 verified at the stated scope;1 unverified lead |
| Computation sections | 25, with saved code and all assertions passing |

ClassE labels the classical and printed corpus; it does not establish that an undated handwritten page follows a particular publication. ClassF marks incomplete source predicates or antecedents. No failed first search is used to claim novelty, and no classD assertion is manufactured.

The research files include the full proof commentary, exact literature comparison, source-read logs, search-to-claim mapping, check-event ledger and reproducible calculations. The log distinguishes documentary concordance from proof checking. Finite computations certify the stated examples; general conclusions have separate arguments or exact published theorem matches. Whole external PDFs are not redistributed in this part; their verified URLs and locators are recorded.
