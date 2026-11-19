# Cote 62: consolidation and mathematical audit

Run **SA16-2026-11-19-cote62**, GPT-6 Astra Pro, effort inherited/unspecified. Status dated **19 November 2026**. This is the cote62 component of the SA16 dossier; the root merge supplies cross-cote consolidation.

## Coverage and the meaning of the registers

All **103** entries in `MPL_62_002-050` were read against their actual passages and consolidated into **97** items. There are90 kept verdicts,7 corrected verdicts and6 mergers. The source index sometimes cites the wrong scan: the registers use the actual `\scanpage` marker and one-based physical line in the named transcription, rather than silently repeating the index metadata. The Pro doubts file and all three Codex note files were also read. Codex notes supply leads but receive no invented entry-verdict rows.

The mathematical reading covers the complete supplied Pro transcription and all of `K62-01`, `K62-02` and `K62-03`, through scan97. The catalogue page count and the last scan number are different kinds of metadata. Reused typescripts also have their own printed pagination, often in reverse logical order. None is used to invent a drafting chronology.

The claim register contains **79 claim families**. A family can include several equivalent formulas, a calculation and its application, or a correct theorem with a defective auxiliary sentence. The30 families marked `false as stated` concern a **literal transcription or a specific subsidiary assertion**. They are not a count of30 established errors in Grothendieck’s ink. Each has a separate refined-statement ID and a specified mathematical obstruction; proposed ink alternatives remain undecided. Other page statuses are19 proof sketches,14 proofs,7 statements without proof,7 open steps and2 later corrections. These numbers are counts of the consolidation units, not a substitute for the individual findings.

There are31 problem records and83 mathematical reading alarms. Every claim and problem has explicit search IDs and opened-reference keys. `search_log.tsv` contains exact requests, repository coverage, authored evidence summaries and retrieval failures. Raw third-party response bodies and the full downloaded EGA PDF remain outside the deliverables; request metadata, opened URLs, dates, hashes and exact theorem audits are retained. `check_events.tsv` distinguishes passage comparison, targeted proof checking, independent reconstruction, computation and refutation. A numerical residual is never labelled a proof for every parameter.

## 1. The relative elliptic construction

The first coherent argument starts with the identity divisorD, its positive pole filtration and its normal line. Its intrinsic line is the tangent line `Lie(C/S)`; the invariant differential line is its dual. The notation must not be silently inverted to fit a later Fourier interpretation. The relevant comparisons are SA16-1–10 and C-SA16-1–5, especially Pro physical lines12–155, scans4–8.

For `E_n=f_*O(nD)`, the genus-one ranks are `(n,0)` for positive n, `(1,1)` at zero and `(0,−n)` for negative n. The relative statement needs a cohomology/base-change theorem. Over a nonreduced base, constant fibre dimensions alone do not establish it. The check in P1 instead uses vanishing in the complementary degree and, at n=0, the unit section and universal `H⁰=O`. The original EGA III-2 paragraphs were read:7.7.5(II),7.7.10,7.8.4,7.8.6 and7.9.9. In particular7.8.4 makes the reducedness qualification explicit. The modern perfect-complex formulation was checked separately. This completes MP-SA16-01 without pretending that the manuscript’s short fibre calculation already proves the relative theorem. [EGAIII2; StacksBaseChange]

The divisor sequence yields `gr₁=0` and `gr_n=Lie^n` for n≥2. Invariant differentiation has leading coefficient−n. This explains both invertibility when n is a unit and the vanishing of the leading symbol in characteristic dividing n; it does not imply that the entire derivative vanishes. The omitted definition is supplied by localization alongD. These are checked reconstructions, not evidence that the pages already contain Dieudonné operators. [C-SA16-3, C-SA16-5; P1]

The filtered algebra is generated in pole orders2 and3, whereas its homogeneous section ring needs degrees1,2,3. Confusing these two rings makes the statement about `E₃` literally false. The degree-three embedding is a plane cubic with the identity as a flex. The affine polynomial and its homogenization disagree by the missing `eyz²` term, and `P(E₃)` has relative dimension2. These are strong mathematical alarms whose ink remains unchecked. The standard Weierstrass atlas, its discriminant and triangular coordinate group were matched exactly to the opened primary construction. [SA16-6,12–18; C-SA16-4,6–8; StacksWeierstrass]

The smoothness condition is that the discriminant be a **unit**. The full general Weierstrass discriminant was independently recomputed by completing the square and taking the discriminant of the resulting cubic. Completing the square requires2 invertible, depressing the cubic requires3 invertible, and setting a weight12 discriminant to one requires a finite flat root cover which is étale when12 is invertible. None of these facts proves the tentative minimum-parameter expectation on scan15: the class of admissible atlases and framings has not been specified. That question remains classF, not an unproved assertion about the dimension of elliptic moduli. [C-SA16-8,10–12; MP-SA16-06,08; StacksKummer]

The one-line general-genus suggestion has a real published mechanism in Grothendieck’s Hilbert-scheme theorem, but its marking, boundedness and stability conditions are absent from the leaf. It is therefore classC with an explicit formulation gap. Exposé221, Theorem3.2 was read; a broad historical resemblance is not promoted to an exact all-genus moduli theorem. [C-SA16-9; MP-SA16-07; GrothHilbert1961]

## 2. Trisections, the anharmonic invariant and descent

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

## 3. The reused algebra sheets

The completion and valuation pages are substantive parts of the folder, not disposable paper backs. Their printed order differs from scan order. The Artin–Rees fragment, strict completion arguments, noetherian lifting and the continuation on scans51,53,55 have been compared across both available endpoints. [SA16-74–103; C-SA16-29–44]

The topology convention permits complete nonseparated quotients. The series criterion and coefficientwise formal-series topology are correct in that convention. A reversed filtration inequality is false literally. Completion is exact for the specified strict sequences; arbitrary continuous maps or arbitrary composites of strict maps do not satisfy the proof shortcut. Explicit counterexamples are recorded with all topologies specified. The finite-module completion/tensor identity needs no Jacobson hypothesis, while faithful flatness does. [C-SA16-30–39; P4; StacksTopological; StacksCompletion]

The enveloping-algebra corollary needs finite generation of the Lie algebra over the noetherian coefficient ring. An infinite-dimensional abelian Lie algebra gives an immediate counterexample to the unrestricted reading. The finite-module proof uses a quotient of the symmetric algebra and does not need an unnecessarily strong PBW freeness assumption. Sierra–Walton was opened for the finite-dimensional direction and the Witt counterexample; an unsupported converse in a lecture exercise was deliberately not adopted. [C-SA16-35; SierraWalton2014; Starr2022]

The valuation sheets distinguish incomparability from independence. Full arbitrary approximation requires independence in higher rank; two rank-two valuations sharing a nontrivial coarsening illustrate the difference. The fundamental inequality, torsion value-group quotient, residue algebraicity and finite-extension discreteness were checked. An infinite algebraic extension can lose discreteness. ADF’s precise approximation theorem and its backward references were read, alongside the primary valuation-ring constructions. [C-SA16-42–44; P5; ADF2020; StacksValuations; StacksEF]

The place-extension theorem has stronger quantifiers than a generic reference to valuation domination: an arbitrary map from a subring to a fixed algebraically closed field extends to a place with that same target. This exact theorem and proof were located and read in Deuring’s1959 TIFR lectures and Gardam’s2023/2024 notes. P5 checks the manuscript’s alternative maximal-subextension proof while keeping its initial valuation-extension theorem as an explicit input. The marginal discussion about retaining or moving the theorem is an editorial problem, separately recorded. [C-SA16-79; MP-SA16-30; Deuring1959; Gardam2024]

The exact identity of typescript numbers272 and276 remains unverified. The institutional Delsarte inventory was found, but its PDF returned403. A pencilled name or rédaction number is not sufficient to assign authorship, date, or a Bourbaki seminar exposé. This is a bibliographic limitation, not a missing mathematical check of the printed algebra. [MP-SA16-24,29; DelsarteInventoryUnverified]

## 4. The classical analytic continuation

Scans59–97 explicitly present classical formulas. Their claim class is predominantlyE, supported by exact modern formulas and their backward references, not by a novelty inference from vocabulary. The period convention is a rank-two lattice with halfperiodsω₁,ω₂; two merely distinct periods do not suffice. The two repeated expositions were compared before proposing corrections. [C-SA16-45–77; DLMF chapters20,22,23; Sutherland2023; Dummit2023]

The universal arguments in P6–P7 cover divisor and residue constraints, the field `C(wp,wp′)`, regularized lattice sums, the cubic differential equation, zeta/sigma quasiperiods, Hermite decomposition, addition laws, theta reindexing and Jacobi differential relations. Exact symbolic calculations and numerical checks are separately labelled in the saved output. Numerical tests use60-digit working precision and recorded nonspecial complex inputs; they support sign/normalization diagnoses without replacing the analytic argument.

The principal reading alarms include a missing square on `wp′`, a factorial and derivative-order mismatch in Hermite decomposition, sigma called even, a missing minus in sigma quasiperiodicity, a positive exponential incompatible with the stated divisor convention, exchanged modular special values, wrong coefficient28 in the second invariant, and inconsistent period primes or sigma denominators. The cancelled argument asserting even degree for every elliptic function is refuted by `wp′`, of degree3; its cancellation remains visible. [C-SA16-49,51–54,61,69–75; readings.tsv]

Two findings deserve particular care. The apparently suspicious Gaussian/theta identity on scan87 is **correct literally** after a bilateral reindexing, so no minus sign was changed. Conversely, for the source convention `K″=−K−iK′`, the shift is `dn(u+K″)=−ik′sn(u)/cn(u)`; the literal positive sign fails the recorded nonspecial numerical test. The invariant convention on scans92–93 is `J=j/1728`, giving `J(i)=1` and `J(exp(πi/3))=0`, whereas the earlier rational invarianti is `1−J`. [C-SA16-66,71,74; outputs/math_checks.txt]

The global lattice classification and uniformization were matched to Sutherland Lecture15, Theorem15.5, Lemma15.9 and Corollary15.12. Lecture14 alone was not cited as if it contained the complete theorem. The author of the Northeastern notes was verified as Evan Dummit. Historical Whittaker–Watson metadata and DLMF’s section-specific backward references were checked; no direct reading of that book’s inaccessible large historical PDF is claimed. [Sutherland2023L15; Dummit2023; WW1927Metadata]

## Links, limits and next-use instructions

`links.tsv` contains34 direct links with both available endpoints checked and101 explicitly marked prior-context leads. The latter preserve the earlier notes’ named runs and comparisons, but their external LM, Dérivateurs, S6, WG and other-cote endpoints are absent from this packet. They must remain in the separate “our projects” table and cannot be reported as established cross-project results. The root merge can add links between cotes62,63,64 once both ends have been read there.

No manuscript image was supplied, so all83 reading alarms remain undecided and no transcription was modified. Publication priority for undated sheets is not inferred from later occurrences of a theorem. No current open-problem status is assigned merely because a search failed. The two classF entries are formulation gaps; the classC general-genus sentence lacks a specified moduli problem. The ranked next tasks are in `directions.md`; none has been developed as a new research project in this consolidation.
