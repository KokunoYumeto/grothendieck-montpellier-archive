# SA16 — Courbes elliptiques

## Consolidated dossier of the Montpellier archive, cotes 62, 63 and 64

**Mathematical and bibliographic status: 19 November 2026.** This dossier consolidates every one of the 366 indexed Pro-note entries against its actual diplomatic transcription passage, and reads every supplied Codex continuation. It provides a claims map, a problem index, mathematical reading alarms, checked links, separate prior-project leads, reproducible checks and ranked tasks for subsequent work. The notes have been treated as reports to test, not as substitutes for the manuscript passages.

The central line of work is the construction and description of elliptic curves from intrinsic data: the identity divisor and its pole filtration; a three-point étale divisor on a genus-zero curve; its orientation, quadratic covers and tangent square roots; and, in cote 64, the finite geometry of level two and level four leading to a symmetric Legendre pinning. Around that line are classical analytic calculations, local reduction formularies, modular-form congruences, Hodge-splitting questions and reused algebraic drafts. Those adjacent materials are included on their own terms. A connection with La Longue Marche or Les Dérivateurs is retained only with its actual provenance and scope.

### The supplied corpus and its order

| Cote | Supplied folders | Main sequence of work |
|---|---|---|
| 62 | `MPL_62_002-050`; `K62-01`, `K62-02`, `K62-03` | Relative elliptic construction; trisections and anharmonic invariants; completion and valuation sheets; classical elliptic functions and their normalizations |
| 63 | `H63-01` through `H63-09`; `K63-01`, `K63-02` | Tate and Deligne formularies; Atkin congruences; cohomological notes and CM tables; Hodge and real-structure calculations; deformation and specialization fragments |
| 64 | `MPL_64_002-039`, `MPL_64_040-077`, `MPL_64_078-115`, `MPL_64_116-157` | Four-sets, squares and cubes; mod-four modules; conics and covers; tangential Kummer data; Legendre pinning; Weierstrass construction; analytic drafts; quadratic normalization |

These are **19 supplied transcription files**. `SA16_folder_coverage.tsv` records every filename, physical line count, actual scan labels and checksum. `SA16_source_manifest.tsv` records the rest of the supplied source files. The catalogue's page/transcription totals are historical metadata: for example, its cote 64 row lists zero transcribed pages while naming four supplied Pro packages. Those totals have not been substituted for the actual file inventory. Gaps between scan labels do not authorize reconstruction of absent pages. No second-pass correction files are supplied for this topic, so there is no unincorporated second-pass reading to privilege.

The mathematical leaves are generally undated. Dates printed on reused circulars or notices date those printed sheets, not automatically the mathematics written on them. Printed page numbers and physical scan order are also distinct. The dossier retains both where they matter and does not manufacture a composition chronology.

**Authorship is especially consequential in cote 63.** Tate's reduction algorithm, Deligne's formulary and Atkin's conjectures retain those authors. Their presence in Grothendieck's archive is evidence of the material he kept, not proof that he originated every statement in the packet. His own Hodge-splitting and deformation questions are identified separately. The SGA 6 specialization question is matched to his published work, while its later solution is attributed to Fulton. [C-SA16-801–836, C-SA16-843–855, C-SA16-859–860; Tate1975; Deligne1975; Atkin1968; Atkin1969; SGA6; Fulton1975.]

### Principal conclusions

**The relative elliptic construction is mathematically recoverable with its hypotheses made explicit.** The first cote's normal line is the tangent line, and its differential line is the dual. The cohomology/base-change step needs the actual relative theorem; constant fibre dimensions alone do not justify it over a nonreduced base. The pole filtration, graded multiplication, cubic embedding and characteristic restrictions can be checked without attributing modern stack language to the source. The corrected relative proof is given alongside the precise EGA paragraphs. [C-SA16-1–8; EGAIII2 §§7.7–7.9; StacksWeierstrass.]

**Several cross-folder repetitions expose genuine differences that a merger must preserve.** Cote 62 correctly records the coefficient `−n` and its characteristic dependence in the graded invariant derivative; cote 64 later draws unrestricted coefficient-one arrows. The same item now shows both occurrences, while the valid theorem and defective later formula retain separate claims. Likewise, fixed-orientation `mu2` pinnings and the stronger varying-orientation `mu4` construction are related but not interchangeable. The full characteristic-`p` derivative kernel is different again: the condition that `p` not divide the filtration index does not make that kernel constant. [SA16-8; C-SA16-5, C-SA16-517–520; SA16-298; C-SA16-298, C-SA16-504–505.]

**The geometric tangent-root equivalence is settled in its stated scope; the symmetric pinning scale remains a precise comparison task.** Over a base with two invertible, fix a smooth proper genus-zero curve with a cubic étale branch triple and a disjoint section. Elliptic double covers with those identified branch data form the same groupoid as square roots of the tangent line at that section, with the recorded norm convention. The local Legendre comparison, its automorphism sheaves and effective descent are proved and independently reviewed in this run. The author nevertheless postpones the particular symmetric normalization in scan 100, equation 73, and scan 121, condition 83c. The existence of ordinary Legendre structures from suitable level-four data is already in Conrad; it must not be advertised as an open problem. [C-SA16-293, C-SA16-505, C-SA16-515, C-SA16-535; MP-SA16-97, MP-SA16-161, MP-SA16-164–165; AntieauMeier2020 §4; ConradLevel §§2–3.]

**Exceptional fibres must retain their scheme structure and arithmetic form.** Dual numbers disprove the replacement of a full exceptional invariant fibre by its reduced orbit. A cyclotomic stabilizer need not be a constant cyclic group over an unsplit field. In characteristic five, the bare six-point octahedron acquires 120 projective symmetries while its opposition-preserving group has 24. The corrected relative theorem retains that opposition. None of these observations is the same as the characteristic-three equianharmonic fixed scheme or the mixed-characteristic-two deformation calculation. [C-SA16-15, C-SA16-25–26, C-SA16-263, C-SA16-363, C-SA16-506, C-SA16-851–852.]

**Two broad assertions require explicit corrections, rather than a vague missing-proof label.** The general tangential Kummer category allows an inertia embedding incompatible with the torsor; a concrete `C2²` example refutes essential surjectivity under the written hypotheses. Atkin's arbitrary-subgroup Fourier-span assertion is false if “integral” means ordinary integer coefficients in the fixed standard cusp parameter. The level-three counterexample and its reflection argument are complete. The valid refinement uses algebraic integers in a suitable number field and a full lattice in each fixed-weight, bounded-pole space; the standard `Gamma0(q)` function specialization, with `q` prime, does admit the integer-span statement. The source's intended ring remains interpretive. [C-SA16-291, C-SA16-391, C-SA16-859; MP-SA16-95, MP-SA16-261.]

**The partition Hecke conjecture at thirteen has a verified later resolution.** The original all-exponent conjecture is compared with Garvan and Shomanov's preprint of 15 April 2025 and its 2026 publication. The proof was checked in the 2025 preprint; the 2026 publication metadata was separately verified. Other Atkin assertions retain their own quantifiers: Guerzhoy's 2010 rates concern `j`, and an eventual threshold does not establish every sharp iteration depth or every function class on the archival page. The exact finite `U13` checks are corroboration within their recorded range, not a universal proof. [C-SA16-827–829, C-SA16-834–836; AtkinOBrien1967; GarvanShomanov2025; GarvanShomanov2026; Guerzhoy2006; Guerzhoy2010.]

**The Hodge questions divide into a tractable analytic statement and a harder algebraicity converse.** The zeros of the almost holomorphic `E2*` expression are proved to be exactly the modular orbits of the square and equilateral lattices. The real-structure sign and claimed bound are checked separately; an actual elliptic lattice refutes the bound. Katz proves the CM-to-algebraicity direction, but the exact converse is still a question in the opened sources. The searches through 19 November 2026 identified no verified resolution. That is reported with medium confidence in exhaustive current status, not converted into a certified claim of global openness. [C-SA16-843–848; MP-SA16-265–269; Katz1976; Bertrand1978; Waldschmidt2004; Spence2018.]

**Several apparent open steps are already closed by the supplied continuation or by an exact later source.** The promised `Q0` is defined on scan 78. The branch-restriction and secant-addition arguments are completed in cote 64; its product-action error is explicitly withdrawn. The crossed specialization draft matches SGA 6, Exposé X §7.14, and Fulton proves specialization on integral Chow groups for flat quasi-projective schemes over an excellent DVR. Conversely, the author's later retraction of four distinct deformation tangents is itself false in the specified mixed-characteristic model. An authorial correction is evidence about the page's history, not automatic mathematical validation. [SA16-297; MP-SA16-166–167, MP-SA16-171, MP-SA16-277; C-SA16-851–852, C-SA16-855.]

### How to read the consolidation

`SA16_entries.tsv` has exactly one verdict for each indexed source entry. “Kept” means that the report survives with its stated attribution and qualifications; it does not mean that every mathematical sentence on the page is true. A note can accurately report an incorrect formula. `SA16_items.json` groups identical objects, questions and readings, retaining all original source-entry IDs. Five further cross-package item mergers were made after reading both passages. Two exact claim repetitions were merged separately. `SA16_id_aliases.tsv` preserves retired identifiers, and `occurrence_history` preserves differing original assessments. Related problems whose hypotheses or requested conclusions differ were linked without being merged; all 98 problem identifiers remain.

The claims register includes labelled current refinements and earlier-run comparisons where they are needed to explain a source claim. It is consequently not a count of original theorems by Grothendieck. The literal source statement, the reconstructed modern statement, status on the pages, computation, literature fate and current status have separate fields. Classes A–F describe that literature relationship; they do not grade correctness. A class C record can contain a now-settled restricted statement and an unresolved identification, or two interpretations with different fates. A class F record signals an unidentifiable formulation, not an unknown theorem silently invented to fill it.

`SA16_readings.tsv` contains mathematical alarms, all **undecided on the ink**. No original manuscript scans were supplied and no diplomatic transcription was changed. A printed parallel can itself contain an error, as the Deligne comparison illustrates. The mathematics may identify a correct alternative but cannot decide whether the fault belongs to the ink, the transcription, an omitted convention or a genuinely false assertion. Strong dependence and high mathematical confidence are therefore compatible with an unresolved reading.

`SA16_links.tsv` preserves checked folder/publication comparisons and the explicitly attributed earlier-project leads. The latter are also isolated in `SA16_our_projects.tsv`. Their local anchors and note reports were read; absent external LM, Dérivateurs, S6/S20, WG and other research endpoints have not been certified. Keeping such a lead does not establish the external theorem or its reported project status. The related-claim/problem navigation files record the reasons that similar passages were linked rather than merged.

Every claim has a searched-fate mapping. The audit records cover zbMATH-targeted searches, arXiv, MathOverflow, Numdam, EGA/SGA, primary papers and author bibliographies, with backward reference-following where needed. Repository failures and missing exact arguments from some initial discovery batches are stated rather than reconstructed. A bibliography entry marked `verified` means that an identified URL was successfully opened; its `verification_scope` says whether the opened material was a proof, statement, metadata record or bibliography. Nine originals or leads remain explicitly unverified. No inaccessible original is presented as a read proof, and no Lean certificate was executed.

The computation records distinguish universal symbolic identities, complete finite enumerations, finite modular-congruence experiments and numerical analytic checks. The CM evaluations include an analytic tail bound but not interval-certified floating-point rounding. The initial Hodge checking matrix contained a sign error; independent review found it, the corrected assertions pass, and the rejected residual is retained. The first `U13` method note named the wrong modular polynomial even though the implementation used the right one; the prose and a loop endpoint were corrected and the revised outputs independently inspected. Those audit corrections concern this run, not the manuscript ink.

The four chapters below give the subject-level findings in source order. Their component counts are explicitly **before global mergers**; the authoritative consolidated counts appear at the end. Original local identifiers in ranges remain resolvable through the alias table. Detailed proofs, exact search logs, programs and outputs are retained under `work/`. Paths beginning `parts/` in an original component use `work/` as their root; unprefixed `code/` and `outputs/` paths are relative to that component's directory. The excluded external research cache is represented by URLs, hashes and access records, not by bundled copies of third-party publications.


---

## 1. Cote 62 — the relative construction, trisections and analytic continuation

**Component audit before the final cross-package mergers.** The final counts at the end are authoritative. Detailed proof and output paths for this chapter are rooted at `work/parts/cote62/`.

Run **SA16-2026-11-19-cote62**, GPT-6 Astra Pro, effort inherited/unspecified. Status dated **19 November 2026**. This chapter preserves its component audit; final mergers and counts are in the consolidated registers.

### Coverage and the meaning of the registers

All **103** entries in `MPL_62_002-050` were read against their actual passages and consolidated into **97** items. There are90 kept verdicts,7 corrected verdicts and6 mergers. The source index sometimes cites the wrong scan: the registers use the actual `\scanpage` marker and one-based physical line in the named transcription, rather than silently repeating the index metadata. The Pro doubts file and all three Codex note files were also read. Codex notes supply leads but receive no invented entry-verdict rows.

The mathematical reading covers the complete supplied Pro transcription and all of `K62-01`, `K62-02` and `K62-03`, through scan97. The catalogue page count and the last scan number are different kinds of metadata. Reused typescripts also have their own printed pagination, often in reverse logical order. None is used to invent a drafting chronology.

The claim register contains **79 claim families**. A family can include several equivalent formulas, a calculation and its application, or a correct theorem with a defective auxiliary sentence. The30 families marked `false as stated` concern a **literal transcription or a specific subsidiary assertion**. They are not a count of30 established errors in Grothendieck’s ink. Each has a separate refined-statement ID and a specified mathematical obstruction; proposed ink alternatives remain undecided. Other page statuses are19 proof sketches,14 proofs,7 statements without proof,7 open steps and2 later corrections. These numbers are counts of the consolidation units, not a substitute for the individual findings.

There are31 problem records and83 mathematical reading alarms. Every claim and problem has explicit search IDs and opened-reference keys. `search_log.tsv` contains exact requests, repository coverage, authored evidence summaries and retrieval failures. Raw third-party response bodies and the full downloaded EGA PDF remain outside the deliverables; request metadata, opened URLs, dates, hashes and exact theorem audits are retained. `check_events.tsv` distinguishes passage comparison, targeted proof checking, independent reconstruction, computation and refutation. A numerical residual is never labelled a proof for every parameter.

### 1. The relative elliptic construction

The first coherent argument starts with the identity divisorD, its positive pole filtration and its normal line. Its intrinsic line is the tangent line `Lie(C/S)`; the invariant differential line is its dual. The notation must not be silently inverted to fit a later Fourier interpretation. The relevant comparisons are SA16-1–10 and C-SA16-1–5, especially Pro physical lines12–155, scans4–8.

For `E_n=f_*O(nD)`, the genus-one ranks are `(n,0)` for positive n, `(1,1)` at zero and `(0,−n)` for negative n. The relative statement needs a cohomology/base-change theorem. Over a nonreduced base, constant fibre dimensions alone do not establish it. The check in P1 instead uses vanishing in the complementary degree and, at n=0, the unit section and universal `H⁰=O`. The original EGA III-2 paragraphs were read:7.7.5(II),7.7.10,7.8.4,7.8.6 and7.9.9. In particular7.8.4 makes the reducedness qualification explicit. The modern perfect-complex formulation was checked separately. This completes MP-SA16-01 without pretending that the manuscript’s short fibre calculation already proves the relative theorem. [EGAIII2; StacksBaseChange]

The divisor sequence yields `gr₁=0` and `gr_n=Lie^n` for n≥2. Invariant differentiation has leading coefficient−n. This explains both invertibility when n is a unit and the vanishing of the leading symbol in characteristic dividing n; it does not imply that the entire derivative vanishes. The omitted definition is supplied by localization alongD. These are checked reconstructions, not evidence that the pages already contain Dieudonné operators. [C-SA16-3, C-SA16-5; P1]

The filtered algebra is generated in pole orders2 and3, whereas its homogeneous section ring needs degrees1,2,3. Confusing these two rings makes the statement about `E₃` literally false. The degree-three embedding is a plane cubic with the identity as a flex. The affine polynomial and its homogenization disagree by the missing `eyz²` term, and `P(E₃)` has relative dimension2. These are strong mathematical alarms whose ink remains unchecked. The standard Weierstrass atlas, its discriminant and triangular coordinate group were matched exactly to the opened primary construction. [SA16-6,12–18; C-SA16-4,6–8; StacksWeierstrass]

The smoothness condition is that the discriminant be a **unit**. The full general Weierstrass discriminant was independently recomputed by completing the square and taking the discriminant of the resulting cubic. Completing the square requires2 invertible, depressing the cubic requires3 invertible, and setting a weight12 discriminant to one requires a finite flat root cover which is étale when12 is invertible. None of these facts proves the tentative minimum-parameter expectation on scan15: the class of admissible atlases and framings has not been specified. That question remains classF, not an unproved assertion about the dimension of elliptic moduli. [C-SA16-8,10–12; MP-SA16-06,08; StacksKummer]

The one-line general-genus suggestion has a real published mechanism in Grothendieck’s Hilbert-scheme theorem, but its marking, boundedness and stability conditions are absent from the leaf. It is therefore classC with an explicit formulation gap. Exposé221, Theorem3.2 was read; a broad historical resemblance is not promoted to an exact all-genus moduli theorem. [C-SA16-9; MP-SA16-07; GrothHilbert1961]

### 2. Trisections, the anharmonic invariant and descent

The central invariant convention is

\[
i(t)=-\frac{((t+1)(2t-1)(t-2))^2}{27t^2(t-1)^2}
      =1-\frac{j_{\rm classical}}{1728}.
\]

The script checks all six anharmonic transformations, their complete composition table, the branch factorization, the commuting involution `σ(t)=(t−2)/(2t−1)` and `i(σ(t))=1/i(t)`. The cubic discriminant and depression were redone before comparing the scratch formulas, because the source changes invariant conventions and contains incompatible literal coefficients. [C-SA16-16–21; code/check_math.py; DLMF233; DLMF2315]

The normalizer is S₃×C₂ over every base with6 invertible, including nonreduced bases. P2 proves this relative statement using fppf-local matrix lifts, two scalar commutation signs and the trace of the product of the standard involutions. The centralizer is the constant two-element group generated byσ; innerness of every automorphism ofS₃ finishes the normalizer. Beauville’s opened reference establishes the field comparison; the relative argument is our independent proof. The same centralizing involution descends to an intrinsic operation on unpointed trisections, applying it twice returns the original trisection, and its fixed quadratic divisor descends to an étale bisection. It does not preserve the openU used for a pointed trisection. [C-SA16-19,78; MP-SA16-12,31; P2; Beauville2010]

The degree-three cyclic quotient ramifies at the cyclotomic pair, while the harmonic triples ramify in the following degree-two quotient. The proper genus-zero quotient itself cannot be a torsor under an affine group. The continuation on scans52 and54 explicitly removes infinity and then centres the trisection by its barycentre; it corrects the earlier incomplete statement. The intermediate multiplicative torsor likewise requires removing its zero and infinity. Both endpoints of these internal links were read. [SA16-25,44–48,65,67; C-SA16-13,14,20; K62-01 physical lines11–13,53–58]

Ordering a trisection gives anS₃ torsor. Adding a disjoint section gives an equivariant map into `U=P¹−{0,1,∞}`, hence the quotient-stack formulation `[U/S₃]`. The elementary descent argument is recorded on objects and morphisms in P2; the general torsor formalism was checked in Stacks95.15. A field theorem does not settle this relative assertion automatically. [C-SA16-22; StacksQuotient]

Three qualifications materially change the exceptional classifications:

1. **Nilpotents:** over `k[ε]/ε²`, `t=−1+ε` has invariant0 without being the constant harmonic orbit. At a cyclotomic rootρ, `t=ρ+ε` similarly has invariant1. The entire exceptional fibre therefore cannot be replaced by its reduced residual gerbe. The vanishing orders2 and3 are verified symbolically.
2. **Arithmetic stabilizer:** the invariant1 stabilizer has a cyclotomic twist. The triple of roots of `x³−1`, marked at infinity overQ, has automorphism group schemeμ₃, which is not the constantC₃. A chosen cyclotomic splitting is required before writing a constantC₃ classification.
3. **Two quadratic covers:** the fixed bisection has classi, but the sign quotient of the ordering torsor has class−3i. The alternating polynomial gives `r²=−27i`. The two covers coincide only after the appropriate extra splitting, not by notation alone.

These are separate findings, not three versions of one missing assumption. [C-SA16-15,25,26; MP-SA16-11; StacksKummer; P2]

For a normal noetherian integral base, finite generic separable data admit finite normalization, but the normalization must still be étale everywhere. Once the **full ordering torsor** extends étale, integrality extends the equivariant map toU; a merely extended cubic algebra is a weaker datum. Divisorial parity/cube conditions are valid local tame tests at0 and1. On singular normal bases they need not be sufficient: P3 checks the normal complete ring `k[[x,y,z]]/(xy−z²)` with `i=x`. The associated square-root cover is unramified in codimension one but fails at the closed point. SGA1 X.3.1 has a regular target, exactly the hypothesis that this example lacks. [C-SA16-23,24; MP-SA16-17; StacksNormalFinite; SGA1]

The elliptic-to-trisection construction forgets centralμ₂. The square-root-line description in P2 is our explicit modern reconstruction, grounded in the coordinate weights and Kummer theory. AOV AppendixA provides the abstract rigidification theorem; its2014 corrigendum was opened and concerns other propositions. Neither source is presented as a commentary on these manuscript leaves. [C-SA16-27; AOV2008; AOVCorr2014]

Hua’s November2026 reconstruction is unusually close: §50, Theorem50.1 treats the invariant and six alternatives over a field of characteristic different from2 and3. It also explicitly places the general-base conic/trisection descent outside its Lean verification. No Lean code was run here. The independent symbolic identities in this part establish their stated rational algebra, and the source’s certification boundary is retained. [Hua2026; searchS62-017]

### 3. The reused algebra sheets

The completion and valuation pages are substantive parts of the folder, not disposable paper backs. Their printed order differs from scan order. The Artin–Rees fragment, strict completion arguments, noetherian lifting and the continuation on scans51,53,55 have been compared across both available endpoints. [SA16-74–103; C-SA16-29–44]

The topology convention permits complete nonseparated quotients. The series criterion and coefficientwise formal-series topology are correct in that convention. A reversed filtration inequality is false literally. Completion is exact for the specified strict sequences; arbitrary continuous maps or arbitrary composites of strict maps do not satisfy the proof shortcut. Explicit counterexamples are recorded with all topologies specified. The finite-module completion/tensor identity needs no Jacobson hypothesis, while faithful flatness does. [C-SA16-30–39; P4; StacksTopological; StacksCompletion]

The enveloping-algebra corollary needs finite generation of the Lie algebra over the noetherian coefficient ring. An infinite-dimensional abelian Lie algebra gives an immediate counterexample to the unrestricted reading. The finite-module proof uses a quotient of the symmetric algebra and does not need an unnecessarily strong PBW freeness assumption. Sierra–Walton was opened for the finite-dimensional direction and the Witt counterexample; an unsupported converse in a lecture exercise was deliberately not adopted. [C-SA16-35; SierraWalton2014; Starr2022]

The valuation sheets distinguish incomparability from independence. Full arbitrary approximation requires independence in higher rank; two rank-two valuations sharing a nontrivial coarsening illustrate the difference. The fundamental inequality, torsion value-group quotient, residue algebraicity and finite-extension discreteness were checked. An infinite algebraic extension can lose discreteness. ADF’s precise approximation theorem and its backward references were read, alongside the primary valuation-ring constructions. [C-SA16-42–44; P5; ADF2020; StacksValuations; StacksEF]

The place-extension theorem has stronger quantifiers than a generic reference to valuation domination: an arbitrary map from a subring to a fixed algebraically closed field extends to a place with that same target. This exact theorem and proof were located and read in Deuring’s1959 TIFR lectures and Gardam’s2023/2024 notes. P5 checks the manuscript’s alternative maximal-subextension proof while keeping its initial valuation-extension theorem as an explicit input. The marginal discussion about retaining or moving the theorem is an editorial problem, separately recorded. [C-SA16-79; MP-SA16-30; Deuring1959; Gardam2024]

The exact identity of typescript numbers272 and276 remains unverified. The institutional Delsarte inventory was found, but its PDF returned403. A pencilled name or rédaction number is not sufficient to assign authorship, date, or a Bourbaki seminar exposé. This is a bibliographic limitation, not a missing mathematical check of the printed algebra. [MP-SA16-24,29; DelsarteInventoryUnverified]

### 4. The classical analytic continuation

Scans59–97 explicitly present classical formulas. Their claim class is predominantlyE, supported by exact modern formulas and their backward references, not by a novelty inference from vocabulary. The period convention is a rank-two lattice with halfperiodsω₁,ω₂; two merely distinct periods do not suffice. The two repeated expositions were compared before proposing corrections. [C-SA16-45–77; DLMF chapters20,22,23; Sutherland2023; Dummit2023]

The universal arguments in P6–P7 cover divisor and residue constraints, the field `C(wp,wp′)`, regularized lattice sums, the cubic differential equation, zeta/sigma quasiperiods, Hermite decomposition, addition laws, theta reindexing and Jacobi differential relations. Exact symbolic calculations and numerical checks are separately labelled in the saved output. Numerical tests use60-digit working precision and recorded nonspecial complex inputs; they support sign/normalization diagnoses without replacing the analytic argument.

The principal reading alarms include a missing square on `wp′`, a factorial and derivative-order mismatch in Hermite decomposition, sigma called even, a missing minus in sigma quasiperiodicity, a positive exponential incompatible with the stated divisor convention, exchanged modular special values, wrong coefficient28 in the second invariant, and inconsistent period primes or sigma denominators. The cancelled argument asserting even degree for every elliptic function is refuted by `wp′`, of degree3; its cancellation remains visible. [C-SA16-49,51–54,61,69–75; readings.tsv]

Two findings deserve particular care. The apparently suspicious Gaussian/theta identity on scan87 is **correct literally** after a bilateral reindexing, so no minus sign was changed. Conversely, for the source convention `K″=−K−iK′`, the shift is `dn(u+K″)=−ik′sn(u)/cn(u)`; the literal positive sign fails the recorded nonspecial numerical test. The invariant convention on scans92–93 is `J=j/1728`, giving `J(i)=1` and `J(exp(πi/3))=0`, whereas the earlier rational invarianti is `1−J`. [C-SA16-66,71,74; outputs/math_checks.txt]

The global lattice classification and uniformization were matched to Sutherland Lecture15, Theorem15.5, Lemma15.9 and Corollary15.12. Lecture14 alone was not cited as if it contained the complete theorem. The author of the Northeastern notes was verified as Evan Dummit. Historical Whittaker–Watson metadata and DLMF’s section-specific backward references were checked; no direct reading of that book’s inaccessible large historical PDF is claimed. [Sutherland2023L15; Dummit2023; WW1927Metadata]

### Links, limits and next-use instructions

`links.tsv` contains34 direct links with both available endpoints checked and101 explicitly marked prior-context leads. The latter preserve the earlier notes’ named runs and comparisons, but their external LM, Dérivateurs, S6, WG and other-cote endpoints are absent from this packet. They must remain in the separate “our projects” table and cannot be reported as established cross-project results. The final registers include the separately reviewed cross-cote comparisons with both available endpoints read.

No manuscript image was supplied, so all83 reading alarms remain undecided and no transcription was modified. Publication priority for undated sheets is not inferred from later occurrences of a theorem. No current open-problem status is assigned merely because a search failed. The two classF entries are formulation gaps; the classC general-genus sentence lacks a specified moduli problem. The ranked next tasks are in `directions.md`; none has been developed as a new research project in this consolidation.


## 2. Cote 63 — formularies, congruences and Hodge questions

**Component audit before the final cross-package mergers.** The final counts at the end are authoritative. Detailed proof and output paths for this chapter are rooted at `work/parts/cote63/`.

Status date: **19 November 2026**. All eleven supplied Codex folders were read, including their short notes and the full corresponding diplomatic transcriptions. This cote has no Pro entries in `NOTES_INDEX.tsv`, so it contributes no artificial entry-verdict rows. Together with the independent two-claim supplement, it contributes 60 claim records, 38 authorial or copied-author problem records, 48 reading alarms and 15 direct folder/publication links before the global merge. The `attribution` field is essential: the copied Tate, Deligne and Atkin papers retain their authorship.

### 1. Tate’s local formulary

The first two H folders contain Tate’s text on generalized Weierstrass equations and reduction. Their sequence runs from integral invariants through coordinate changes and minimal equations to the formal group, Haar measure, reduction types and the algorithm. These are copied mathematical sources in Grothendieck’s papers. Classifications of their later publication are not claims that Grothendieck originated Tate’s algorithm. [C-SA16-801–811; Tate1975 §§1–8.]

The integral identities were recalculated as polynomial identities over the integers. The general coordinate substitution was expanded independently, rather than checked by substituting a few curves. The short equation in the copied formulary fixes the sign convention for `c6`. The later generic `j` model uses the opposite sign from one literal formula in the transcription; the refined equation is C-SA16-803. The formal local coordinate calculation recomputes the series through the displayed order and the line-intersection Vieta sum. Its invariant differential has coefficient `2a3` in degree three. The handwritten qualification “sauf erreur” remains a source status, while the exact residuals and suggested alternatives are separate. [C-SA16-802–803,807; `c63_algebra.py`.]

The reduction table was read in full, including its component labels. Smith forms of the A, D and E intersection lattices reproduce the cyclic factors used in the geometric component groups. This algebraic certificate does not by itself prove the geometric Kodaira–Néron classification. The local measure computation distinguishes good, split multiplicative, nonsplit multiplicative and additive reduction. Ogg’s formula is checked against the tame rows; its wild form remains a theorem used from the classification. The twelve-torsion statement needs the page’s additive hypothesis and residue characteristic different from two and three. In that case `E0(K)` is uniquely twelve-divisible and the component quotient is killed by twelve, so each component has a unique twelve-torsion representative. An unrestricted statement for every reduction type would be false. [C-SA16-808–810; Tate1975 §§5–6; `c63_kodaira.py`.]

### 2. Deligne’s relative construction and modular forms

H63-03–04 continue a text headed with Deligne’s name. The published comparison is the 1975 *Formulaire*, with a checked 1968 IHES preprint record. Its relative construction uses the identity divisor, cohomology and base change, the regular differential line and the cubic embedding. These are closely related to cote 62, but include singular genus-one fibres. The base-change hypotheses were compared with the actual EGA III-2 paragraphs; constant fibre ranks alone were not treated as sufficient over a nonreduced base. [C-SA16-812–814; Deligne1968; Deligne1975 §1; EGAIII2 §§7.7–7.9.]

The short form needs two and three invertible; the `d6=0` gauge needs two and `c4` invertible. Small-characteristic normal forms, nodal/cuspidal tests and the automorphism groups have separate hypotheses. Equality of `j` gives geometric isomorphism classes, but at exceptional points it does not guarantee a faithfully flat isomorphism torsor for arbitrary infinitesimal families. The explicit dual-number example makes that distinction visible. Likewise, the generic automorphism group scheme is constant of order two; its sections over a disconnected base need not consist of only two globally constant choices. [C-SA16-815–821,840–841; Deligne1975 §§2–5; `c63_more_algebra.py`.]

The ring of integral modular forms and the mod-two/mod-three rings were matched with Deligne’s Propositions 6.1–6.2. The Hasse section, the Hasse–Witt map and the canonical ordinary lift are not interchangeable assertions. Katz supplies the intrinsic Frobenius interpretation and Serre–Tate deformation framework. A sign discrepancy is retained: the archived formula says `b2`, whereas the printed Remark 6.3 says `−b2`. Their zero divisors agree; equality of normalized sections requires fixing the convention. Another omitted subscript on the coordinate-change page occurs in the printed original too. A published parallel therefore cannot automatically decide whether the diplomatic transcription misread the ink. [C-SA16-822–823; Deligne1975 pp.69–71; Katz1973 §2.0; Katz1981SerreTate.]

### 3. Atkin’s experimental congruences and their different later fates

H63-05–07 contain Atkin’s expositions, not Grothendieck conjectures. They distinguish older partition congruences, numerical experiments on `j`, finite-level Hecke identities, higher-prime eigensystems and conjectural uniformity. A single broad label “proved by p-adic modular forms” would erase several real quantifier differences. [C-SA16-824–836; Atkin1968; Atkin1969.]

The literal seven-part of the early Ramanujan statement fails at `n=243`: the exact partition number has seven-adic valuation two while `24n−1` is divisible by `7³`. The known corrected exponent is recorded. Euler’s recurrence and an independent inverse-product calculation agree through index 3000. The progression `p(206839n+2623)=0 mod17` was checked at `n=0,1,2`; this finite calculation does not replace an all-index theorem. Atkin’s archived 1969 exposition records it. A later 2022 article repeats the progression but supplies a mismatched 1954 bibliography pointer; that later citation cannot safely establish its first-publication date. [C-SA16-824,831–832; Atkin1967_11; EichhornEngleKronholm2022, equation (2); DLMF27Partitions, 27.14.6.]

The partition Hecke conjecture for every power of thirteen now has a verified later resolution: Garvan and Shomanov’s preprint was first submitted on 15 April 2025, with publication in *Advances in Mathematics* 490 (2026), article 110840. The all-exponent statement, the normalized partition convention and the excluded auxiliary primes were compared with the original Atkin–O’Brien formulation. The 1967 paper had proved the first two exponents; the later work closes the stated all-exponent conjecture. This is one of the clearest changes of status that a present-day companion must report. [C-SA16-828; MP-SA16-254; AtkinOBrien1967 §1.2 and §5; GarvanShomanov2025 §4; GarvanShomanov2026.]

For `j`, Guerzhoy’s 2006 theorem gives eventual normalized congruences under stated rationality and pole hypotheses. The 2010 paper gives quantitative bounds specifically for `j`: its displayed theorem covers primes five, seven and eleven, and its following remark gives exponent `m−C` at thirteen, seventeen, nineteen and twenty-three. This does not justify the same rate for every function `F`, nor the sharp assertion `C=0` everywhere. Katz’s 1973 §3.13 precisely identifies the thirteen-adic eigenfunction and its uniqueness in the specified unit-root cusp space. Literal uniqueness of arbitrary functions modulo congruence conditions is false unless a residue class or normalized eigenline is specified. [C-SA16-827,829,834–836; Guerzhoy2006; Guerzhoy2010; Katz1973, Lemma 3.13.4, Remark 3.13.5 and Theorem 3.13.7; SerrePadic1973 §1.1.]

The saved exact `U13` computation uses Newton traces on the level-thirteen modular equation, with enough modulus retained before every division. The method is described in `u13_method.md`; Maier’s normalization was read from Tables 2, 4 and 5 of the correct 2009 paper. It independently checks the first two U iterates by direct q-series and reproduces the six very large-index valuation examples on scan 46. After an independent boundary-index review, it tests 1,715 normalized Hecke pairs at each exponent one through eight, all passing. These are exact finite checks. They do not constitute a proof for every exponent or coefficient. At prime twenty-nine the saved matrix has `M^840=I`, hence `M^841=M`; it does not have a period asserted to be 841. [C-SA16-827,829; `c63_u13.py`, `c63_algebra.py`.]

The independent coverage audit added two short assertions as separate records. The broad claim that entire forms on every congruence subgroup are spanned by forms with integral Fourier series is false if integral means ordinary integers in the standard cusp parameter. The explicit level-three conjugate subgroup and shifted j function give a complete counterexample. The algebraic-integer lattice formulation, with weight and cusp-pole bounds fixed, is established; the standard Gamma0(q) function case, with q prime, also admits the integer-span assertion. The source's intended ring is left interpretively undecided. The simple-spectrum lemma is independently proved by Hensel lifting and Lagrange projectors on a specified finite free module after a splitting coefficient extension. It does not construct the required modular-form module or Hecke lifts. [C-SA16-859–860; MP-SA16-261; work/parts/cote63_supplement/proof_notes.md; Katz1973; Stein2007; KurthLong2007; MilneMF2017.]

### 4. CM tables and the Hodge-splitting questions

H63-08 contains cohomological program notes, a class-number-one table, bibliography and reused correspondence. The nine imaginary quadratic fields and thirteen class-number-one orders are distinct lists. Reduced primitive forms were enumerated, and the displayed singular moduli were evaluated with an analytic bound for the omitted Fourier tail. Floating-point rounding was not interval-certified, and numerical agreement does not prove integrality or completeness. Stark’s own historical account provides the checked account of Heegner, Baker and Stark; the original inaccessible articles remain marked accordingly. [C-SA16-837–839,856; Stark2007; `c63_numerics.py`.]

K63-01–02 contain Grothendieck’s own questions about the de Rham Hodge decomposition, quasiperiods, the real structure and a discriminant-normalized phase. With an algebraic Weierstrass model and differential fixed, the shift into the antiholomorphic line is the almost holomorphic weight-two Eisenstein expression. A complete independent Fourier argument proves that its zeros are exactly the modular orbits of the square and equilateral lattices. The proof uses a dominant first sine term and a uniform rational tail bound, then monotonicity on the two remaining vertical boundaries. It is not inferred from a numerical plot. A second agent independently checked its inequalities and modular fixed-point argument. [C-SA16-843–844; MP-SA16-265; Katz1976 §§1.2–1.3; `hodge_proof.md`.]

The question whether an algebraic de Rham splitting forces CM is much harder. Katz’s Lemma 4.0.7 proves the CM direction; Question 4.0.8 states the converse. Bertrand’s 1978 Conjecture 3 and Waldschmidt’s 2004 page 277 preserve the exact question. Spence’s 2018 result on maximal special subvarieties does not classify every individual algebraic pair of modular values. The targeted searches through 19 November 2026 identified no verified resolution. The dossier therefore reports an unresolved or uncertified exact converse, with medium confidence in exhaustive current status; it does not infer global openness solely from a failed search. Algebraicity in a Betti basis is not a substitute for algebraicity in de Rham cohomology. [C-SA16-845; MP-SA16-266; Katz1976; Bertrand1978; Waldschmidt2004; Spence2018; supplement_katz/review.md.]

The real-structure calculation corrects the literal scalar sign and refutes the proposed bound by the actual lattice parameter `τ=3i`. With the declared convention, `4ρσ=|α|²−1`. The invariant phase away from the two zero orbits is

\[
\operatorname{phase}\!\left(\frac{E_2^*(\tau)^6}{\Delta(\tau)}\right).
\]

It is real analytic and modular invariant; it has not been made into a holomorphic rational function of `j`. The first checking draft itself contained an incorrect lower-right minus sign in its general conjugation matrix. Independent review caught it. The corrected matrix has `+conjugate(α)`, satisfies `M conjugate(M)=I` and determinant one, and is now asserted in two programs. The rejected residual is retained as an audit artifact. That checking error has no authority over the unknown ink. [C-SA16-847–848; MP-SA16-268–269.]

### 5. Deformation divisors and reused specialization sheets

The final elliptic leaves study `c4=0`, `c6=0`, completed deformations at two and three, and a level-three CM branch. Explicit Weierstrass equations redo the divisor multiplicities and tangent factors. The earlier statement of four distinct tangents is mathematically correct; the later retraction to coincident tangents is refuted by the exact factors. The associated local action contains a nontrivial transvection. These conclusions concern the specified two-dimensional deformation model, not the one-dimensional quadratic-order node test in cote 64. The fixed-base extension of a `μ3` automorphism and the bad reduction of the displayed `j=0` curve at three are checked separately. [C-SA16-849–853,857–858; MP-SA16-270–276; Hua2026 §18; ArtebaniDolgachev2009 §2; Katz1981SerreTate.]

The crossed specialization fragment has now been identified exactly. Its draft number `(7.11.2)` is not the matching published number: Grothendieck’s SGA 6, Exposé X §7.14, equations `(7.14.1–2)` and the final paragraph contain the same cycle-specialization question and the same rational-equivalence obstruction. Fulton’s 1975 §§4.1–4.4 prove specialization for flat quasi-projective schemes over an excellent DVR. His manuscript was received on 20 August 1974. Thus class A records the question’s publication in Grothendieck’s own work; its subsequent solution is by another author. The crossed draft is neither a proof nor a counterexample. [C-SA16-855; MP-SA16-277; SGA6; Fulton1975.]

The neighboring Banach-algebra fragment is independently checked by the Neumann-series argument, while the undefined spectral-radius symbol stays a reading problem. The dated letter is correspondence provenance, not a theorem by its addressee. Deuring’s bibliographic title is identified with the 1941 Hamburg paper, while the supplied later year and page data remain a reading/bibliography alarm. [C-SA16-854,856; MP-SA16-278; BanachAlgebraSource; Deuring1941; SerreBourbaki1973.]

### Audit boundaries

Every claim has a searched-fate mapping. The reference registry states whether the opened object was a proof, a theorem statement, an author bibliography or publisher metadata. Some early request arguments were not saved verbatim; their returned URLs, retrieval identifiers and hashes are retained without inventing the missing arguments. The later exact requests and scoped source audits cover each mathematical family. All diplomatic reading alarms remain undecided because manuscript scans are absent. The future tasks in the global ranked directions are not developed here.


## 3. Cote 64, scans 2–77 — finite geometry and relative covers

**Component audit before the final cross-package mergers.** The final counts at the end are authoritative. Detailed proof and output paths for this chapter are rooted at `work/parts/cote64_early/`.

Run: **SA16-2026-11-19-cote64-early**. Model: GPT-6 Astra Pro; reasoning effort inherited/unspecified. Mathematical status date: **19 November 2026**.

### Coverage and provenance

This portion covers all **129 indexed Pro-note entries** in `MPL_64_002-039` (63 entries) and `MPL_64_040-077` (66 entries). Both full diplomatic transcriptions, all note entries and both doubts tables were read. The comparisons use actual transcript passages, with filenames and one-based physical line locators. No manuscript images or second-pass corrections are supplied for these two packages, so every ink question remains unresolved and the transcriptions have not been edited.

The work contains **104 consolidated items**, **65 claim records**, **17 problem records**, **39 mathematical reading alarms**, and **7 ranked directions**. The entry verdicts are 103 kept, 25 merged into an existing item, and one corrected. Most notes accurately identify an issue even where the manuscript’s literal statement is false; an “agrees” source comparison therefore does not certify the mathematics. Items 201–304 are stable identifiers. Claim records also include labelled corrections and earlier-run reconstructions; these are not passed off as additional manuscript theorems.

The manuscript’s claims, the earlier runs’ ideas, the current proofs and the external literature remain distinct. In particular, the 129 contextual fields preserved in `context_leads.tsv` are earlier-run leads. Their local manuscript anchors were read, but the absent LM, S6/S20 and research-register endpoints were not searched in an inaccessible archive or treated as verified results.

### The author’s sequence of work

The first packet begins with a four-element set, its regular Klein subgroup and its three partitions. The author immediately corrects “vector space” to “affine space” and “normalizer” to “centralizer.” He then passes between four-sets, abstract groups of type S₄ and the four Sylow-3 subgroups. Only isomorphisms are allowed: the margin explicitly says so. The uncertain numeral “three” in the Sylow reconstruction cannot be mathematically correct.

The next sequence develops a square through its vertices, opposition, edges, flags, rotations and reflections. It compares orientation, diagonal and codiagonal torsors and follows their behavior under duality. Several apparently unfinished steps close locally: the convention check is completed on scan 14; the question about recovering a dihedral group is answered by the reflection-square construction on scan 17. The printed commutator-only presentation, taken literally, is incomplete. Its intended finite group needs order and opposition relations as well.

The subgroup and cube section counts 30 subgroups in 11 conjugacy classes, asks for their inclusion diagram, and compares ten transitive cube-feature sets. The current certificate supplies the entire subgroup poset and all ten stabilizer descriptions. It also isolates a genuine negation problem: a face diagonal’s rotational stabilizer is generated by a double transposition and lies in the normal Klein subgroup. The two six-point covers of the three partitions must be distinguished; their stabilizers are C₄ and a nonnormal Klein group, respectively.

The module section fixes Λ=Z/4. It introduces the 16 zero-sum triples lifting the three nonzero elements of a two-dimensional F₂-space, the canonical decomposition of its endomorphisms, the resulting four-set and square, and the natural geometric characters of GL₂(Λ). The exact action has order 96 and identifies the group with S₄×_{C₂}D₈. Its projective action has order 48. A face has two zero-sum lifts, exchanged by the central sign. The reduction sequence for GL₂ splits, while that for SL₂ does not; this is compatible with the existence of proper supplements in the latter group.

Scans 37–38 ask when projective mod-four data lift through the central extension. The manuscript reduces this to lifting diagonal and codiagonal torsors to a square. The current cocycle proof computes the obstruction c∪d. Its vanishing is a torsor-by-torsor question; it does not make the universal central extension split.

The second packet first repeats the endomorphism decomposition and then moves from finite octahedra to six points on a conic. A Klein action has the local fixed-pair model {0,∞}, {1,−1}, {i,−i} when 2 is invertible. Preserving those three opposite pairs gives 24 symmetries. Forgetting the pairing is unsafe in characteristic 5: the six points become P¹(F₅), with 120 projective symmetries and five regular oppositions. The text rejects some intermediate arithmetic but does not retract the false bare-divisor conclusion.

The ensuing constructions use a cubic étale algebra, its trace conic and coordinate squares; three four-covers related by Klein twisting; and a genus-one torsor with involution. Locally an involution is x↦a−x, with fixed locus [2]⁻¹(a). This identifies the torsor as a twist of its Jacobian and gives the canonical quotient coordinate 2x−a. The “almost cartesian” diagram is geometrically explained by the two branches of v²=u², with an explicit qualification over nonnormal bases.

The author then asks for doubling intrinsic to four-point geometry. The canonical Klein quotient supplies it, and the following pages calculate

\[
F_t(z)=t\frac{(z^2-2z+t)^2}{(z^2-2tz+t)^2}.
\]

The final formula is correct. A radical and an intermediate sign are not; their correction is a mathematical alarm for the later image check. Iteration is valid, but its full fiber is a divisor with multiplicities, not generally the reduced scheme image of torsion points.

Finally, scans 71–77 introduce a tame cover with a marked ramification point, its tangent-power map, the inertia embedding and its relative torsor class. The broad categorical target lists these data independently. That literal formulation is false: the embedding has to agree with the inertia determined by the cover. The intended quadratic elliptic specialization is valid and leads to a square-root line, an orientation twist and the pinning. The promised standard square Q₀ is defined immediately afterward, at scan 78 of the supplied continuation; it is not an abandoned construction.

### Main mathematical findings

#### Finite structures are mostly correct, with several sharp local corrections

The computations exhaust S₄, D₈, all 16 endomorphisms over F₂ and all 96 invertible matrices over Z/4. They recover the author’s group orders, two invariant planes, derived groups, centers, character relations, five subgroup intersections and frame/face counts. These are complete finite calculations, not samples. The source files and outputs also retain the complete subgroup list and 66 cover relations.

The reflection-square equivalence is correct because four noncentral involutions generate D₈ and its eight automorphisms give every square symmetry. The functor from a square to its automorphism group is a different construction and loses the antipodal automorphism. The literal incomplete presentation has an infinite cyclic quotient; the repaired one is recorded separately as C-SA16-322.

The natural mod-four scalar quotient from an earlier context was independently checked locally in C-SA16-307. Its formula is GL₂(F₂)-equivariant, has scalar kernel and gives the required two-dimensional quotient. This does not verify the missing LM/R17 endpoint.

#### The characteristic-5 exception changes the geometric classification

C-SA16-263 is refuted over Spec F₅, which satisfies the page’s 2-invertibility assumption. The explicit map z↦2z+1 preserves the six points but changes opposition. The structured group remains finite étale of rank 24 over Z[1/2]; the universal bare stabilizer has a special fiber of size 120 and is not flat. Inverting 5 restores the equality for the bare divisor. C-SA16-363 states the corrected alternative.

The four-cover/conic formulation is proved using a reference conic and signed permutation symmetries. It is a statement about forms and étale descent, so rational sections of a normalizer need not form a constant S₄ on every split projective line. Over the real numbers the anisotropic reference conic and the split line have different rational forms. The uncertain orientation insertion is kept open for the ink.

#### The unrestricted tangential Kummer category has a concrete counterexample

Take S=Spec C, X=A¹, t=0 and G=C₂². Let X′ be the disjoint union of two copies of A¹_y, with x=y² and action (a,b)·(y,e)=((−1)^a y,e+b). It is finite locally free of degree four, smooth over S, a G-torsor away from zero and tame of index two at the marked point (0,0). The transcript imposes no connectedness hypothesis.

Its actual inertia is the first factor. The listed target conditions allow the same torsor class but the second factor as the chosen μ₂ embedding. Every separately written condition still holds, yet the datum cannot come from a pointed cover. This is a failure of essential surjectivity, checked against all hypotheses, not merely a concern that “ad hoc” morphisms were left unspecified. C-SA16-391 proves the necessary compatibility condition and leaves the full repaired arbitrary-group category as a precise follow-up task.

For G=μ₂ there is no competing inertia embedding. The four-branch double cover and its tangent square root have the same μ₂ twisting and automorphisms, giving the valid special case C-SA16-293. A bare root object nevertheless has μ_n automorphisms, so uniqueness has to refer to the full specified comparison.

#### Doubling, norm and pinning need their conventions retained

The symbolic calculation verifies the duplication function, all three Klein invariances, coprimality and marked values. For m=2^n with n≥1 and 2 invertible, its geometric fiber over the distinguished branch value has degree m², four multiplicity-one points and multiplicity two at the remaining sign pairs, hence m²/2+2 support points. The second iterate at t=2 is factored exactly as an independent check. C-SA16-382 records the divisor statement separately from a reduced-image reading.

The local determinant norm in x=u y^n is N(y)=(−1)^{n−1}x/u. The sign between a norm normalization and a leading-jet normalization must not be silently erased. The proof and sample companion-matrix determinants are both saved.

The tangent line formula is obtained from the rank-two projective tangent calculation and the determinant of the permutation representation of a cubic cover. No division by three is required, so characteristic 3 is included. The μ₄ twist squares to the orientation twist, and compatible pinnings form a μ₂-torsor. There are two geometric choices, but no arbitrary-base global section is promised.

### Literature findings and their limits

The 65 claims are classified **E: 33**, **B: 12**, **C: 16**, **D: 3**, **F: 1**, and **A: 0** in this portion. Class D is used cautiously for an exact notation or groupoid package not located as an independently developed theorem; it is not a statement that the underlying elementary mathematics is unknown. Class C includes partly matched canonical constructions, corrected relative statements and a genuinely unfinished general categorical formulation. Class F applies only to an illegible marginal promise; its surrounding finite mathematics has been checked.

Burnside1897 provides opened historical finite-group passages. BrauJones2016 gives the matching mod-four split group and invariant-plane table, but not every canonical torsor dictionary in the manuscript. DetinkoFlanneryHulpke2018 uses “proper supplement,” which cannot be converted into “complement.” The MathOverflow correction chain was followed to that primary source and the small SL case was proved directly.

Beauville2010 gives the field normalizer and rationality restrictions, with a prime-to-characteristic convention. Hua2026 §42 proves the characteristic-5 exception and expressly leaves the relative correspondence and μ₄ strictification unproved. This dossier treats Hua as a November 2026 primary reconstruction/preprint; it does not claim to have run its Lean source. The relative proofs here are separately labelled current work.

SGA1 was read at the exact descent, associated-bundle and tame-cover results. EGA II’s tautological quotient and projective universal property were read directly after downloading the source; those passages fix conventions and do not themselves state the manuscript’s orientation formula. Stacks Kummer theory supplies the exact root-isomorphism torsor, while AntieauMeier2020 supplies the labelled Legendre atlas and its twisted S₃ action. ConradLevel Proposition 3.2 already constructs ordinary Legendre structure from suitable level-four data. The later problem is consequently the particular symmetric normalization, not the existence of any canonical level-four construction.

First circulation and publication are separated where verified: Brau–Jones 2014 / electronic 2015 / volume 2016; Beauville 2009 / 2010; Detinko–Flannery–Hulpke 2016 / 2018, with an opened 2022 revision; Milnor 2004 / 2006; Antieau–Meier 2016 / 2020. Conrad’s handout is left undated. The reused Thaler circular dated 9 March 1982 is not treated as the composition date of every manuscript leaf.

Two bibliography entries remain explicitly `unverified`: Ledet’s exact proposed section could not be opened despite verified landing metadata, and the original Lattès 1918 volume exceeded the web reader’s size limit. Neither inaccessible result carries a mathematical conclusion here. The bibliography has 23 entries; the reference audit identifies what was actually read, its hypotheses and its permitted use.

### Audit and reproducibility

`search_log.tsv` records the exact saved queries and source requests, repository names, retrieval identifiers and outcomes. It includes zbMATH Open, arXiv, MathOverflow, Numdam, EGA/SGA and author/published-work bibliographies as appropriate. A direct zbMATH request did not yield an accessible review; an unsuccessful repository query is not represented as a database result. The earliest three discovery requests were not saved verbatim, and this is stated rather than reconstructed; later recorded queries and primary openings cover every claim. `claim_search_coverage.tsv` maps all 65 claims to coherent search families and their exact follow-ups.

`check_events.tsv` distinguishes passage comparison, independent proof, finite or symbolic calculation, reference use and refutation. A source-note comparison is labelled “used and rechecked in this run,” with an explicit warning that it is not a proof check. The reference events similarly distinguish a targeted calculation from carrying a broader theorem as background. No formal-verification claim is made.

The five substantive programs are `finite_groups.py`, `cube_and_pgl.py`, `symbolic_checks.py`, `kummer_counterexample.py` and `scalar_quotient.py`. Their outputs are saved alongside the complete subgroup and Hasse tables. The first symbolic implementation failures are retained as an audit trail; corrected assertions pass. The authoring scripts merely serialize manually made decisions and do not assign verdicts from headings or keywords.

The verified-link portion contains ten within-archive links and eleven literature links, with both relevant endpoints read. Its continuation anchors include scans 78–82, 93 and 94. The 129 prior-context rows remain separately identified leads, not claimed completed endpoint checks. The cross-package proposals have been adjudicated in the consolidated registers and alias table; their manual reviews are retained.

Full retrieved publication text and downloaded external PDFs are excluded from the deliverable tree. Search output files retain requests, source identifiers, URLs and the researcher’s concise findings. The complete current work, computation outputs and review history accompany this dossier.


## 4. Cote 64, scans 78–157 — pinning, analytic drafts and normalization

**Component audit before the final cross-package mergers.** The final counts at the end are authoritative. Detailed proof and output paths for this chapter are rooted at `work/parts/cote64_late/`.

This portion consolidates all 63 entries of `MPL_64_078-115_notes.md` and all 71 entries of `MPL_64_116-157_notes.md`. Both complete Pro transcriptions and both complete doubts tables were read. Each verdict was made against the actual passage, with 1-based physical transcript line numbers. The source files contain diplomatic uncertainty and deletion markers; this run changes none of them. The Codex notes are documentary leads integrated in the topic-wide registers.

The dominant unfinished task is a **canonical symmetric passage from relative level-four data to Legendre pinning**. The author determines a line and several symmetry laws, but explicitly postpones its tensor-square scale. Much of the rest is completed mathematics, sometimes with a correction already made on the page: cubic coordinates and addition, complex structures and framed analytic families, then quadratic orders and their normalization. The distinctions between an original statement, an authorial correction, an earlier run’s extension, a modern source and this run’s reconstruction are recorded separately in the items, claims, problems and check events.

### 1. The author’s line of work

#### The standard square, twists and the pinned moduli problem

Scans 78–100 continue the earlier square and level-four geometry. The standard square `Q0` supplies the scalar twist used in the tangent line. Scan 78’s rotation group is μ4: the misleading star is already deleted. The polynomial model `s⁴=−4`, with `i=−s²/2`, is a useful earlier-run example that this run verifies; the manuscript itself specifies the sides and their rotation relation. It is not permissible to turn that example into a quotation from the page. See SA16-501–503 and C-SA16-501–502.

The text distinguishes three related structures. With an orientation identification α fixed, pinnings form a μ2-torsor. Allowing α to vary gives the stated μ4-torsor. Adding an ordering of the three nonzero two-torsion points gives the combined rigid moduli problem. This ordering matters: the uncombined pinned problem can retain a cyclic order-three stabilizer at an equianharmonic parameter. The characteristic-three fixed scheme needs its own treatment, because its defining quadratic becomes a repeated factor. It is a different issue from the characteristic-five exception to an earlier bare-octahedron assertion. See C-SA16-503–506 and the crosslinks to scans 48–53.

The modular group calculation is concrete. After choosing `i`, the stabilizer is

\[
D'_3=S_3\times_{C_2}C_4\cong C_3\rtimes C_4.
\]

Its order is twelve, its centre has order two, its commutator subgroup is `C3`, and its abelianization is `C4`. A transposition lifts to order four, so its central extension of `S3` does not split. The full finite group was enumerated, and the tangent and quotient-tangent characters were checked. These checks establish the finite group and the displayed characters; they do not identify an arithmetic Galois image or the monodromy of an external family. See C-SA16-507–510 and `proof_notes.md`, §§1–2.

The reconstruction of an elliptic curve from the cubic étale set `J`, the disjoint section `t` and the pinning data is stated at scans 83 and 94–95. The elementary part is precise: after one square root of a line has been fixed, all its square roots form the groupoid of μ2-torsors. The team’s early64 proof, independently read and checked here, also establishes the geometric elliptic/branch-data to tangent-square-root equivalence: locally both sides are the same μ2 twist groupoid, their automorphism sheaves match, and the equivalence descends. The particular symmetric `Q0`-twisted pinning normalization remains a separate comparison. The opened modern references provide ordinary Legendre models and a twisted descent action, but do not themselves assert this exact symmetric normalization. That is the meaning of class C here; it is not a claim that ordinary Legendre or level-four representability is an unsolved problem. See C-SA16-504–505, 509–512, MP-SA16-161 and [AntieauMeier2020, §4; ConradLevel, §§2–3].

At scans 98–100 the author writes coordinate conditions for the pinning. They determine a one-dimensional kernel, not its scale. Equation 73 is still to be expressed. The same issue returns at scan 121 as condition 83c and is explicitly postponed. The cyclic-difference calculations on scans 123–126 determine the line and its basis signs; they do not close that gap. The continuation across the package boundary is one problem, MP-SA16-164, within the level-four construction MP-SA16-165. A canonical ordinary level-four construction in the opened literature is a comparison target; matching its ordering, tangent variance and symmetric fourth-root action is a separate task. This remains the highest-priority direction in `directions.md`.

#### Pole filtrations, Weierstrass coordinates and the group law

The title at scan 101 starts the explicit Weierstrass construction. Scans 102–115 use the spaces `F_n=H⁰(E,O(nO))`, the invariant derivation associated to a tangent vector, parity under negation and the resulting cubic. The standard algebraic content is recoverable, but several distinctions must be preserved.

For ordinary principal parts, the associated graded derivation has coefficient `−n`. A multiplicatively rescaled convention changes this to `−nc`; no such convention makes every graded coefficient equal to one while retaining multiplication and the Leibniz rule. The all-degree assertion is therefore defective independently of the choice of normalization. In contrast, the leading coefficient of the cubic is convention-dependent: ordinary principal parts lead to the familiar factor four, while the rescaling `ε_n=(−1/2)^n pp_n` makes the particular cubic monic. The text does not explicitly state which normalization it is using. An unconditional instruction to replace every monic cubic by one with factor four would go beyond the evidence. See C-SA16-517–518, 523 and the associated readings.

The constant-kernel statement requires a characteristic restriction. For a nonzero invariant derivation over an algebraically closed field of odd characteristic `p`,

\[
\ker(D|F_n)=\{g^p:g\in F_{\lfloor n/p\rfloor}\}.
\]

The first nonconstant example is `x^p`, of pole order `2p`. It remains in `F_(2p+1)`, so the proposed rescue “p does not divide n” does not work. The filtered union and the graded section ring must also be separated. The latter has constants in every degree: its kernel is `k[S]` in characteristic zero and `R^p[S]` over a perfect field of characteristic `p`. These are mathematical reconstructions, not readings of additional ink. See C-SA16-519–520, [Stacks031W], and the direct argument in `proof_notes.md`, §4.

The coordinate construction needs a nonzero tangent vector. Scan 105 does not visibly state that qualification, whereas scan 115 calls the vector a basis. At zero the proposed coordinate basis collapses. The cubic degree, the constant sign, the ambiguous exponent on the `a2` term and the prime/double-prime mark all have exact algebraic tests. Their compatible alternatives are in `readings.tsv`; the tests do not decide which marks were written.

Several apparent open steps are actually completed on the pages. Scan 106 finishes the restriction-to-branch-points argument with a Vandermonde determinant. Scans 110–111 repair the determinant criterion by inserting distinctness and explain why repeated rows fail. Scans 112–113 derive the third secant intersection and state the final domain `x(P)≠x(Q)`. The displayed point is the negative of the sum. The tangent continuation retained in the notes is an earlier-run addition, independently checked here, not a separate manuscript formula. See MP-SA16-166–167 and C-SA16-524–530.

Scans 115–118 continue one calculation across the package boundary. For a root `r` of the cubic and the other roots `u,v`, translation by `(r,0)` descends to

\[
\sigma_r(z)=r+\frac{(r-u)(r-v)}{z-r}.
\]

Its fixed values give the halves of the corresponding two-torsion point. The undivided expression covers `r=0`; an expression containing `a3/r` requires that qualification. The correctly expanded radical is

\[
(r-u)(r-v)=-(a_1r+2a_2-3uv).
\]

The later written plus sign gives `−34` instead of `2` at roots `1,2,3`. This is a decisive mathematical alarm, while the scan still has to decide the mark. The distinctness hypothesis of the earlier determinant proposition is satisfied in the half-division application because the three doubles are different. See C-SA16-532–535 and SA16-534, 537, 561.

#### Two analytic drafts and their corrections

After title sheets and reused printed notices, scans 131–152 describe complex tori, lattice frames, the upper half-plane and a nonzero tangent vector. The physical sequence is retained even where exposition would be smoother in a different order. The title’s doubtful page count does not authorize reordering or discarding a sheet.

The first draft transports a complex structure through the real-part map. Its second formula requires an inverse for type correctness. With the stated line convention `L_z=C(z,1)`, direct computation gives

\[
J_z=\frac1{\operatorname{Im}z}
\begin{pmatrix}
-\operatorname{Re}z&|z|^2\\
-1&\operatorname{Re}z
\end{pmatrix}.
\]

The induced orientation is opposite to the one initially asserted. The author himself withdraws that assertion and later considers the other line convention. The first displayed period `−\bar z` is antiholomorphic in the stated parameter; the second draft uses a holomorphic `τ`. These are two formulations with a visible correction, not one silently modernized family. See C-SA16-540–544, MP-SA16-168–169 and [Hain2008, §§2.3–2.4].

The subsequent action formulas work after their conventions are fixed. The right change of a Torelli frame produces `(dτ+b)/(cτ+a)`; an explicitly defined anti-automorphism converts it to the usual left action. The automorphy factor and the semidirect action on lattice translations were recomputed. The symbol `τ∞` is a determinant-minus-one matrix in this calculation. Its infinity subscript does not make it the arithmetic inertia source mentioned in an unavailable La Longue Marche passage.

The total elliptic family over the upper half-plane has fundamental group `Z²`. The simply connected covering base of the elliptic moduli stack is the framed base itself, the upper half-plane. The coarse parameter also has a different covering theory because it forgets stabilizers. Similarly, the once-punctured torus has free group `F2` and rank-two abelianization; the first draft’s rank-one parenthesis is false. The second formulation omits it. Explicit lifts of modular generators were computed and their relations checked modulo inner automorphisms. The full discrete outer-automorphism theorem is used from the opened primary literature, rather than claimed as a new theorem proved by those word calculations. See C-SA16-548–550 and [BuxErshovRapinchuk2011, §3].

Finally, two separately free actions need not have a free product action. The pair `(-1,-I)` fixes the doubly framed base and acts as negation on the elliptic fibre. Removing zero leaves three fixed two-torsion points. Scan 152 already notices the obstruction and deletes the erroneous assertion. MP-SA16-171 records the correction as closed, with both places retained.

#### Quadratic orders and the arithmetic appendix

Scans 154–157 contain a separate algebraic line of work. The uncertain hypothesis “anneau jauge” is not deciphered here. Under the **DVR** interpretation, with uniformizer `π`, the local normality criterion has a short proof. In odd residue characteristic, `A[S]/(S²−a)` is normal precisely when `v(a)≤1`. A unit is étale; valuation one gives a DVR; larger valuation leaves the integral element `S/π` missing. The necessity fails for a regular local ring of higher dimension: `Q[[x,y,S]]/(S²−xy)` is normal although `xy` lies in the square of the maximal ideal. Thus the ring hypothesis is mathematically consequential. See C-SA16-555 and MP-SA16-172’s background.

For a dyadic unit, nonsquare residue gives a normal DVR with inseparable residue extension, which is not étale. In the square-residue case choose `α` and put `b=α²−a`. The class of `b` modulo `m²` is independent of the lift. Normality holds exactly when that class is nonzero. If it vanishes, `(S−α)/π` is integral and missing from the order. The completion formula is valid as a `T`-adic completion; identifying it with the local completion needs the topology comparison made in `proof_notes.md`, §10. Noncompleteness of `A` alone does not invalidate it.

The additional description as an ordinary node needs a stronger hypothesis. The tangent quadratic has distinct geometric lines exactly when `v(2)=1`. Both an equal-characteristic-two cusp and a ramified mixed-characteristic example refute the unrestricted assertion. This is a statement about the singularity type, not a counterexample to the DVR normality test. The c63 deformation-divisor question is related, but it has a different ambient ring and cannot be decided by importing this one-dimensional calculation.

The proposed finite exceptional nonnormal locus disappears once all height-one local rings are normal: the quadratic hypersurface satisfies `S2`, and the normality criterion applies. The full primary theorem and proof in EGA IV2, 5.8.6, printed p.108, were opened and checked. Its application here is explicit in `proof_notes.md`, §11.

The last global assertion is true after the order and its normalization are distinguished. Let `P=εqQ` be squarefree in `Z[T]`, with positive content `q` and primitive `Q`, and suppose it defines a genuine quadratic field over `Q(T)`. Generic étaleness of the normalization over every integer fibre is equivalent to `q=1` and

\[
P=r^2+4h,\qquad r,h\in\mathbf Z[T].
\]

The integral generator `u=(S+r)/2` gives the full normalization

\[
\mathbf Z[T,u]/(u^2-ru-h).
\]

Its discriminant is `P`, so it is finite étale on `D(P)`. Necessity, globalization of the square congruence and normality of this order are proved in this run; the manuscript merely asserts sufficiency. The source comparison identifies the classical ingredients, without claiming to locate the first occurrence of this specialized global formulation. See C-SA16-560–561, MP-SA16-172 and [Voight2016, Lemmas 3.7, 3.10 and Proposition 3.13].

The signed radicand matters. An unsigned `Q=1` cannot distinguish `P=3` and `P=−1`; whether the author’s `Q` abbreviates the full radicand remains an ink question. In the example `T(T−λ)`, the square condition modulo four is exactly `4|λ`, while the displayed congruence modulo two only asks that `λ` be even. At infinity `x=1/T` gives `(S/T)²=1−λx`. The opposite written sign fails at `λ=4,x=0`, where it gives the dyadically ramified field `Q(i)`. For the corrected sign and `λ=4m`, the normalized chart `u²−u+mx=0` is étale on the specified open and splits at infinity. Identifying the unnamed exceptional `λ` with `1728` is an earlier-run interpretation, not a manuscript value.

### 2. What the earlier notes got right, and what changed in scope

The supplied notes are generally careful about the division between manuscript, correction and new calculation. Consequently the verdict table has 99 kept entries and 35 merged entries, with no entries discarded merely because they are speculative or documentary. “Kept” preserves the attributed report; it does not endorse an unavailable external theorem or promote an earlier-run calculation to manuscript content.

The most valuable corrections already recognized by the notes survive independent checking: the tensor-square factor, positive-characteristic kernel, determinant distinctness, fourth-division signs, analytic orientation and antiholomorphic parameter, rank-two abelianization, product-action fixed points, DVR hypothesis, ordinary-node qualification, signed mod-four test and infinity sign. The present run supplies new executions and proof records rather than inheriting their certificates.

Topic-wide access changes several packet boundaries. Earlier square and level-four passages, the later normalization deferral, the second analytic draft and the arithmetic appendix are now available and read at both endpoints. Their former “outside this packet” labels are replaced by exact folder links. Original files from La Longue Marche, Les Dérivateurs, cotes 93/159 and the earlier modernization are still not supplied. Their 21 leads remain in `our_project_links.tsv`, with the precise note report checked and the original endpoint explicitly unavailable. No absent proof or project status is certified.

A source check also found a bounded defect in a modern comparison: the literal strict `C2×S3` quotient in Hain’s Proposition 3.15 has the wrong harmonic stabilizer. The manuscript audit does not rely on that quotient. Its independent counterexample is R-SA16-L64-Hain315; the other period and frame results are used at their separate stated scope. The public November 2026 modernization is credited as a comparison, with no Lean certificate claimed.

### 3. Coverage, classes and verification

| Register | Count |
|---|---:|
| Source entries | 134 |
| Items | 99 |
| Entry verdicts: kept / merged | 99 / 35 |
| Component claim records | 66 |
| Claims class E / C / F | 56 / 6 / 4 |
| Authorial problems, including closed steps | 12 |
| Reading alarms, all ink-unresolved | 75 |
| Folder / published-work / external-project links | 16 / 5 / 21 |
| Ranked directions | 7 |
| Exact computation groups rerun | 31 |
| Bibliographic records: verified / primary-text-unverified | 25 / 2 |
| Check events | 340 |

The claim statuses on the pages are: 13 proved there, 27 proof sketched, 7 stated without proof, 5 corrected by the author later, 11 false under the specified literal or unrestricted reading, and 3 open on the pages. The four F classifications concern the unstated principal-part convention, the uncertain ring hypothesis, the signed-radicand abbreviation and the undefined cancelled diagram. A false literal reading is not evidence that the transcription’s uncertain mark has been deciphered.

All 66 claims have exact search-group mappings in `claim_search_coverage.tsv`. The searches, actual batched results and opened locators are recorded in `search_log.tsv`, `search_requests.json` and `literature_notes.md`. A failed targeted search is not used as proof of absence. The two unverified bibliography entries are backward historical leads whose original texts were not opened; the mathematical statements actually used are supported by opened modern primary sources and the independent arguments specified in the check events.

The computations are exact symbolic identities, complete finite-group enumerations, free-word reductions and explicitly scoped characteristic-p calculations. The universal Hasse recurrence is proved separately from the sample primes. The single initial implementation failure was a zero-matrix comparison requiring entrywise simplification in Sympy; the corrected run passed all 31 groups. No Lean library, inherited research script or manuscript scan was audited. The complete proof supplement, code and output are retained with the tables.

Printed notices on scans 124, 127 and 157 document the sheets’ reuse. Their dates do not establish mathematical composition dates. The doubtful leading digit before the June 1981 notice date remains unresolved, and no chronology is inferred from it.


## 5. Consolidated counts and completion record

These counts describe the final registers after five item mergers, two claim mergers and the two additional cote 63 claims. Component audit files remain unchanged in their identity and retain the original assessments for traceability. A claim record may include an explicit current refinement; the total is not a count of original theorems by one author.

| Register | Count |
| --- | --- |
| Indexed source entries | 366 |
| Entry verdict rows | 366 |
| Consolidated items | 295 |
| Canonical claim/refinement records | 268 |
| Source claim records with searched-fate mappings | 270 |
| Merged problem index, including closed authorial steps | 98 |
| Mathematical reading alarms; ink unresolved | 245 |
| Ranked future tasks | 23 |
| Supplied transcription files covered | 19 |
| Bibliographic records | 138 |
| Check events | 1422 |

### Entry verdicts

| Verdict | Count |
| --- | --- |
| kept | 287 |
| merged | 71 |
| corrected | 8 |
| withdrawn | 0 |
| rests on a misreading | 0 |

A source entry can be kept while reporting a false formula accurately. Authorial withdrawals are retained as source history, including the item kind below; they do not require withdrawing the note that correctly reports them. The eight corrected entry verdicts therefore measure corrected reports, not the number of mathematical defects or reading alarms.

### Item kinds

| Kind | Count |
| --- | --- |
| conjecture | 1 |
| idea of the earlier run | 53 |
| other | 12 |
| reading question | 59 |
| self-flagged step | 32 |
| title, date or page count | 17 |
| unproved claim | 76 |
| unpursued implication | 36 |
| withdrawn in the same text | 9 |

### Literature classes

| Class | Meaning | Count |
| --- | --- | --- |
| A | In his own published work; chronology qualified for undated leaves | 3 |
| B | Developed by others into established results | 57 |
| C | Partly matched or developed; exact remaining distinction recorded | 30 |
| D | Exact package not identified as developed in the recorded searches | 3 |
| E | Classical or standard mathematics known before the manuscript context | 167 |
| F | Not identifiable precisely from the pages | 8 |

Class A does not automatically mean that a later printed question was already solved there: C-SA16-855 distinguishes its publication in SGA 6 from Fulton’s subsequent solution. Class D is a bounded literature-search assessment, not a proof of historical absence. Class C is not synonymous with a currently open theorem.

### Status on the pages

| Reviewed status family | Count |
| --- | --- |
| corrected by author | 9 |
| earlier-run/current reconstruction | 12 |
| false literal/unrestricted statement | 58 |
| mixed/uncertain | 25 |
| open on pages | 21 |
| proof sketched | 66 |
| proved there | 34 |
| stated/construction without full proof | 43 |

These editorial groups were assigned after reading every status field, with the full statements inspected for mixed cases. The exact `status_on_pages` wording is preserved, including differing occurrences of merged claims. The group assignments and reasons are in `SA16_claim_status_groups.tsv`; the full exact-status frequency table is in `SA16_counts.json`. A false literal/unrestricted statement is not an adjudicated error in the handwritten ink.

### Links, source access and verification

| Category | Count |
| --- | --- |
| Folder/claim/problem comparisons with available endpoints read | 103 |
| Published-work comparisons with cited scopes read | 30 |
| Earlier-project context leads, separately tabulated | 251 |
| Total link rows | 384 |
| References marked verified at the stated access scope | 129 |
| References/originals explicitly unverified | 9 |

All prior-project rows preserve their note IDs and reported run names. The absence of the original other-project endpoint remains explicit; these rows do not count as completed external theorem checks. The exact query and access logs, separate proof supplements, complete finite certificates and rejected checking drafts are included.

### What the next run can use

For a companion edition, begin with the relevant canonical item and claim, follow its source-entry IDs and physical locators, and inspect the unresolved reading rows against the original scans. For research, take one of the 23 tasks in `SA16_directions.md`; each states its origins, known input, target and first concrete step. For bibliographic verification, use `SA16_references.bib` together with `SA16_reference_audit.json`, whose occurrence-specific access scopes prevent a metadata opening from becoming a claimed proof reading. For reproducibility, use the program and saved output named in each check event. The diplomatic sources themselves remain the supplied attachments.
