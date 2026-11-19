# Part C working proof and status record

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), subagent part_c_algebra, 2026-11-19. No priority claim.

## Current results (11:13 UTC; 12:13 Europe/Berlin)

- C.1(a): complete proof prepared: exp/log for derivations raising a nilpotent ideal filtration and automorphisms identical on the associated graded; arbitrary commutative Q-algebras, no Noetherian or finite type hypothesis.
- C.1(b): complete criterion prepared: an automorphism equal to identity modulo a nilpotent ideal I is exp of a uniformly nilpotent derivation exactly when its action on I/I² is uniformly unipotent. A differential automorphism has order ≤n iff its difference ideal J has J^(n+1)=0. Square-zero extensions exhibit arbitrary invertible conormal actions, and locally unipotent but not uniformly unipotent actions.
- C.1(c): complete locally nilpotent intertwining proof prepared via pointwise polynomial logarithms.
- C.1(d): universal bijectivity on arbitrary module functors is false. Formal injectivity fails for F(R)=R_red. Formal and ordinary surjectivity fail for F(R)=R⊕Ω_(R/Q), with action (a,ω)↦(a,ω+a dλ). An intrinsic logarithmic image criterion will distinguish the general functor case; for quasicoherent functors formal actions are arbitrary endomorphisms and ordinary actions locally nilpotent endomorphisms, proved by coefficient comparison.
- C.2(a), L8 implication: REFUTED, robustly, by G=Z/4 and G~=Z/8 centered intervals. All chain, symmetry, convolution closure, torsion equivariance, translation alignment axioms hold, and all cardinalities occur. f=1_{0,1} and equimeasurable h=1_{0,2} have triple-convolution maxima 3 and 4. Complete integer certificate in code/part_c_finite_checks.py.
- C.2(b): exact manuscript reading remains a gate. Literal axioms lack nonemptiness/fullness; if {}_2G is the subgroup of elements of order dividing two, existence of even sparse systems is trivial exactly when this set is a subgroup, and every abelian group qualifies. A strengthened cardinality-complete classification must not be silently substituted. Original scan 17 is being fetched.
- C.2(c): full theorem proved: pretasse symmetry for all nonnegative finitely supported functions is equivalent to G being abelian. For any noncommuting a,b take f(e)=1,f(a)=2,g(b)=1,g(a^-1 b)=2. Then max f*g=5 and max g*f=4. The S3 instance is also a tasse/non-tasse asymmetry; all 900 rearrangement pairs verified.

## Sources opened

- Stacks Project, Section 10.133, tag 09CH, Definition 10.133.1 and Lemma 10.133.2; https://stacks.math.columbia.edu/tag/09CH ; tool ref turn945542563view0. This gives the differential-operator convention used. Our iterated commutator calculation is included in full.
- J.S. Milne, Basic Theory of Affine Group Schemes, version 1.00, 11 March 2012, Chapter VIII §2 Example 2.1 and footnote 1 on printed p.113; https://www.jmilne.org/math/CourseNotes/AGS.pdf ; tool refs turn945542563view1, turn308590984view1. The footnote explicitly handles Q-algebras and modules not necessarily finitely generated via locally nilpotent endomorphisms.
- EGA IV4, NUMDAM metadata opened at https://www.numdam.org/item/PMIHES_1967__32__5_0/ ; tool ref turn945542563view2. Full PDF web open failed because 49,852,990 bytes exceeds tool limit. Subsequently the original PDF was downloaded locally and its extracted text opened: Proposition16.8.8 pp42–43, and Proposition16.8.9 p43. The recursive commutator criterion and the expanded identity agree with the direct proof used here. Download checksum and runtime are in code/part_c_fetch_sources_output.json.
- University of Montpellier archive index opened https://grothendieck.umontpellier.fr/archives-grothendieck/ ; tool ref turn575484835view0; HTML downloaded. It identifies root /68.pdf through embedded viewer data-src. Original PDF download in progress.
- Michel Hua's project repository root opened https://github.com/Commutator-IO/grothendieck-project ; tool ref turn434272976view0. No mathematical claim taken from it yet. Direct source retrieval attempts failed.

## Inputs checked

- `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_68_033-056+162-1+162-6_transcription.tex`, scans 36–46, especially lines 240–278, 388–420, 437–507.
- `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_66+68_002-032_transcription.tex`, scans 15–22, especially lines 507–573 and 635–726.
- `inputs/RESEARCH_SA22_study/study/readings/68_images.md`, decisions on pretasse/tasse and the existing S3 claim. Mathematical checks done independently; original handwritten word readings not yet independently confirmed.

## Computation record

1. `part_c_finite_checks.py` exhaustively checks C4: 8 chain fibres, 20 symmetry atoms, 400 convolution atom pairs with exact nonnegative cone decompositions, 64 translation-alignment pairs, 16 torsion-equivariance pairs; all set cardinalities 1–4 occur. It verifies the Condition K counterexample and the two-factor majorization failure.
2. Same program checks S3 multiplication, asymmetry maxima 5/4, and 900 pairs of rearrangements for the packed forward pair. Integer arithmetic only.
3. First output-generation run incorrectly serialized the S3 variable f under the C4 record after variable reuse; all mathematical assertions had passed correctly. Fixed by retaining c4_f and reran; current JSON/TXT outputs are correct. This was an output bug, not a false mathematical certificate.

## Approaches/gates

- No incomplete mathematical step is labelled proved in the final section fragment.
- The C4 certificate refutes L8 without needing the ambiguities concerning infinite groups or fullness.
- Axiom 17c uses an undefined B family in the supplied transcription; use A in its natural type-correct reading, and state it. If it refers to a second independently chosen family, the same C4 example takes B=A.
- Condition K is evaluated on the union of fibre cones, which is convolution stable. If 'span' instead means its full nonnegative linear span, the counterexample persists because it contains these functions.

## Completed Part C section (11:24 UTC)

The section fragment has 16 numbered statements, with individual rows in checks/part_c_results.csv and events in checks/part_c_events.tsv. It gives all C.1(a)–(d) proofs and exact image criteria; C.2(a)/L8 is refuted and replaced by the exact pairwise-majorization criterion; C.2(c) is classified for every group. C.2(b) is fully answered for the literal axioms, with the explicit interpretation of {}_2G as inherited two-torsion: systems exist iff involutions commute pairwise, and in particular for every abelian group. No cardinality-complete classification is claimed or substituted for that statement.

Original 68.pdf is now downloaded (17,815,903 bytes, 56 pages). Scans 017, 044, 045, 046 were visually inspected. Scan017 confirms i:{}_2G≃kerρ, two clauses called d), no completed fullness/nonemptiness condition, and an unfinished final bracket. The source image is in qa/cote68_scan017_bottom_rotated.png for independent checking. Since the scans are source material, the parent should decide whether to exclude the full PDF from the final deliverable as requested for input/source scans; mathematical proof and evidence notes remain in the package.

HLP original-book scan downloaded and visually opened: printed pp.261–262, Theorems368–369, at local PDF pages274–275. The exact source confirms the theorem locator. Primary Stacks Definition10.133.1 and Lemma10.133.2 tags09CI/09CJ checked. Milne ChapterVIII Example2.1 (not2.2) and footnote1 on p.113 opened through the web PDF; local download HTTP406 is recorded and does not change opened status.

### Corrections and refinements to supplied files

- `study/HUNCHES.md`, lines108–113, H22-9: the implication to ConditionK is false; exact C4 counterexample C-K-counter. The surviving consequence is C-chain-true, and the missing property is characterized by C-K-replacement.
- `study/STUDY.md`, lines661–663: the proposed implication is now refuted, not an unresolved deduction from the axioms. The original scan has no complete fullness axiom.
- `study/STUDY.md`, line680, and `study/CORRECTIONS.tsv`, row/line11: “only for M finitely generated” is too strong if read as a necessary condition. Exact criterion: every locally nilpotent endomorphism of M must be uniformly nilpotent. For K=Q[x], M=⊕_{n≥0}K/(x−n), M is not finitely generated but every locally nilpotent endomorphism is zero. Proof included in C-qcoh.
- `MPL_68_033-056+162-1+162-6_transcription.tex`, lines388–420: general module functors need extra conditions; the universal bijectivity expectation is refuted by C-functor-counter and classified by C-functor-criterion. This is a mathematical answer to the question, not a change of handwritten reading.
- Same transcription, lines437–507: existing differential-automorphism corrections are independently re-proved and sharpened to the exact conormal criterion C-differential. C-filtered is the corrected theorem using (iii′).
- `study/STUDY.md`, lines654–655: existing S3 asymmetry is rechecked and strengthened to the exact “all functions iff G abelian” criterion, including infinite groups.

### Additional exact finite computation

`part_c_extensions.py` checks two nonisomorphic extensions of C2. For each: 4 chains,6 symmetric atoms,36 convolution atom pairs,16 alignments,8 kernel-equivariance pairs. All positive cardinalities occur. Runtime is recorded in its JSON output. The script is standalone and does not import or rerun the first certificate.

### Literature-search provenance

Searches used combinations of: “exponential logarithm automorphism nilpotent derivation Q algebra differential operator”; “locally nilpotent endomorphisms representations additive group arbitrary module characteristic zero”; “finite groups rearrangement inequality convolution majorization nested sets ConditionK”; “rearrangement cyclic composite subgroup counterexample”; and “Gabriel 1932 rearrangement Fourier coefficients”. The searches found the standard exp/action classification in Milne and the classical rearrangement theorem in HLP. No priority or novelty claim is made for the conormal criterion, arbitrary-functor counterexamples, C4 witness, or group symmetry criterion. Their proofs are supplied in full instead of being attributed to an unopened source.
