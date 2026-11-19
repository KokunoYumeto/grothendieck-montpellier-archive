INCOMPLETE

| Item | Outcome | Statement labels | Exact state / gate |
|---|---|---|---|
| A.1 | Open main theorem; corrected unramified corollary proved | A:unramified-corollary; A:pro7-representability; A:hensel-remaining-gate | Actual7-to-local-model implication remains. The proposed henselized counterexample now satisfies every other axiom and is nonrepresentable; arbitrary fpqc equalizer descent is its sole remaining gate. Missing finiteness in8 is only a wording defect. |
| A.2 | Refuted L2; independence example proved | A:L2-counterexample; A:ind-thickening | The supported subgroup H satisfies1–6 and finite-type8, including every noetherian adic4, but fails actual7 over Fp[[t]]. Two independent full-axiom audits passed. |
| A.3 | Known / Refuted with corrected theorem | A:completion-descent; A:nonfinite-descent; A:polarized-descent | Completion descent holds; nonfinite quasi-projective descent fails; exact positive replacements proved. |
| A.4 | Proved in every stated rank; audit passed | A4:finite-descent-theorem; A4:all-primes | Independent audit separates fixed finite rank, every finite rank, and arbitrary free rank. Boundary comparison is false for every prime; the finite semi-local theorem survives. |
| A.5 | Known under explicit projectivity convention | A5:projectivity; A5:fixed-projective-space; A5:correspondences | Relative ample line bundle and finite locally free projective bundle; fixed global dimension needs an additional bound. |
| B.1 | Proved / Known | B:NiceV; B:Kummer; B:DVR-classification | All-ring integral and isogeny answers proved; complete-DVR derivation from opened classification theorems written with residue hypotheses explicit. |
| B.2 | Known with source derivation | B:NiceIV | Connected and dual-connected alternatives treated through the exact nilpotent-display theorem. |
| B.3 | Nonvanishing and positive union proved; raw-union closure gate open | B:finite-PD; B:largest-literature-class; B:closure-reduction; B:positive-exclusion | Opened-source union and exclusions written. Finite direct-product closure and filtered-colimit closure of the raw union are each equivalent to PF union PE being contained in QSyn; that inclusion is not settled. The etale-local envelope has proved finite-product and etale stability. |
| B.4 | Proved / literal L6 refuted | B:Delta; B:coLie-Dieudonne; B:L6-refutation | Complex, descent and corrected classical-module comparison written; the literal Delta tensor formula is refuted. |
| C.1 | Open all-ring classification; full new family computed | C:allrings_obstructions; C:dualnumber_C2_ring; C:divisible_nil_invariance | The entire degree-two ring over A[epsilon]/epsilon², for a characteristic-zero DVR with uniformizer2, is computed, including every generic-kernel generator and tensor product. Divisible nil directions preserve the positive answer. An intrinsic necessary-and-sufficient condition for arbitrary k remains. |
| C.2 | Refuted with explicit replacement | C:distinguished_ring; C:lambda_failure; C:partition_formula | Ring and operations determined; special lambda claim fails by finite certificates. |
| C.3 | Lambda criterion settled; full modular/general-base ring open | C:BO_field_lambda; C:BO_affine_lambda; C:BO_lowrank_base; C:BO_Qalgebra | Special iff m≤2 or the base with2 invertible is a Q-algebra. Low-rank rings over all bases and all ranks over Q-algebras determined. Modular indecomposable/general-base classification remains. |
| C.4 | Proved in the explicitly stated categories | C:formal-noncommutative-unipotent; C:baseline-free-realization | Noncommutative unipotent splitting proved for connected finite-type formal groups over perfect fields, all p including2; algebraically closed case separately stated. Complete baseline-free ordinary-group criterion proved, also for constant group schemes. No unproved arbitrary group-scheme representability claim. Earlier smooth-kernel failure is over Fp. |
| D.1 | Proved under manuscript hypotheses | D:fixed; D:rank; D:quotient-polarization | Irreducible-fibre rank and normalized height proved; reducible-fibre correction explicit. |
| L1 | Open unconditional scope; full conditional proof written | A:local-models-suffice | Uniform Artin--Rees propagation proves open modularity locus once actual local models exist. The actual7-to-local-model gate remains. |
| L2 | Refuted, every prime | A:L2-counterexample | H(R)={x:x^p=0 and x in tRx} has strengthened adic effectivity but fails actual modularity propagation. The corrected positive criterion retains a separate propagation axiom, as in A:pro7-representability. |
| L3 | Known with hypotheses checked | A:completion-descent | Murre Section4 case(d) supplies exactly the needed completion descent. |
| L4 | Proved and strengthened to every prime | A4:all-primes; A4:boundary | The lead asking for failure at2 is proved; the earlier R2 assertion of validity in odd characteristic is refuted. |
| L5 | Proved / Known | B:NiceV; B:NiceIV | Uniform square-zero Hom bound handles2; both nonnilpotent-PD alternatives have exact source derivations. |
| L6 | Refuted with corrected comparison | B:Delta; B:coLie-Dieudonne; B:L6-refutation | The manuscript uses the finite Dieudonne module M, not Delta, in the tensor formula. |
| L7 | Refuted with explicit replacement | C:distinguished_ring; C:lambda_failure; C:partition_formula | Two natural prelambda structures fail special identities; ring and plethysm described. |
| L8 | Proved | C:charzero_lambda | Characteristic-zero semisimple universal orthogonal representations transfer special identities to split WG. |
| L9 | Refuted with corrected criteria | C:central_twists; C:isoclinism_counterexample | Crossed modules omit Hall commutator compatibility; finite groups distinguish them. |
| L10 | Proved under explicit normalization | D:height; D:quotient-polarization | Local inverse intersection matrices give the component pairing; mobile polarization scale is fixed. |

# Research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); inherited effort. No priority is claimed.

Continuation snapshot: 2026-11-19T14:30:26.779697+00:00. This is an active, incomplete research state. Continuation started at 14:06:58 Europe/Berlin on 19 November 2026; its first three-hour review is due at 17:06:58. Checkpoints continue every45 minutes from number03.

## Proof and source record

The paper states each proved claim with its actual scope. Component notes in `notes/` record source locators, attempted approaches, failures, and remaining gates. `CHECK_EVENTS.tsv` preserves actual checks; an independent proof audit is not claimed when only the writing agent checked its own argument. The bibliography marks sources opened or not opened. Original attached files and fetched manuscript/source PDFs are excluded from this package.

## Computations and reproduction

Every mathematical computation below has its source in `code/` and its exact output in `logs/`. A filename stem denotes those two paths unless a distinct output is named. Bounds belong to the program, not to the theorem: the all-prime and unrestricted statements have mathematical proofs in the paper. Searches with no finding are recorded as bounded negative searches. Wall times are in seconds and depend on this execution environment.

| Program / output stem | Exact scope and counts | Outcome and time |
|---|---|---|
| `A_finite_certificates` | F2[t,e]/(t³,te,e²), 16 elements, 4,096 triples | Finite truncation checks of NR example pass; 0.037414 s. |
| `A4_all_primes_boundary` | p=2,3,5; coefficient rings of size4,27,3125; normalized units2,9,625 | Additive and logarithmic boundaries differ at all three primes. Timed reproduction 0.040836 s. |
| `A4_cech_counterexample` | F2 punctured-plane example, 1,024 polynomial checks through total degree3 | Canonical comparison fails; timed reproduction 0.052530 s. |
| `A4_amitsur_search`, output `A4_amitsur_search_8` | Exponent bound8; 65 algebras, 221 ideals | No finding within this search; 0.126156 s. |
| `A4_amitsur_random`, output `A4_amitsur_random_10_2000` | Seed1729, exponent bound10, attempt budget2,000, 498 distinct tests | No finding; 2.843559 s. |
| `A4_closed_covers`, outputs `_3_4_3000`, `_3_6_10000`, `_4_4_10000` | Respectively3 variables/nilpotence4/3,000 attempts;3/6/10,000;4/4/10,000. Distinct tests2,847;9,292;9,947. Nonzero additive boundaries198;1,140;399 | No unequal-image finding; 2.435135;244.611250;22.876920 s. |
| `A4_multivariable`, outputs `_2_4_10000`, `_2_6_3000`, `_2_6_double_10000`, `_2_6_maximal_10000` | Seed92019. Two variables; nilpotence4 or6. Attempts10,000;3,000;10,000;10,000. Distinct tests2,634;1,158;3,643;3,111. Nonzero boundaries0;2;16;20 | No unequal-image finding; 6.198103;37.531276;118.250570;89.528330 s. |
| `B_finite_certificates`, output `.jsonl` | Original p2 detector:512 ring/64 ideal elements;32,768 additivity,131,072 scalar,1,024 product,1,024 composition checks. Mod4 Kummer test and299,592 carry triples. Derived-complex dimension check | All pass; 0.272800 s total. The strengthened all-prime proof and p3 checks follow below. |
| `B_finish_PD_detector` | p2:512 scalars,64 ideal elements,131,072 scalar checks,16,384 additive checks. p3:19,683 scalars,729 ideal elements,86,093,442 scalar checks,3,188,646 additive checks. All product/composition axioms and six base/prime images of tau | Every tau image is the nonzero basis vector uv; 0.094406 s at2 and5.816666 s at3. |
| `B_finish_PD_product_ideal` | Exploratory presentation for Fp[x,y,z]/(xy,xz); p=2,3,5; all1,331 multidegrees with coordinates0–10 for each prime | Nonzero kernel diagnostics at2; none at3,5 in these bounds. Universality of presentation not proved, so no PD-torsion-free theorem inferred; 1.026500 s. |
| `C_finite_certificates` | C2 two-set product4/subsets6; S4/V4 action on6 two-subsets, product36 and symmetric square666; Cp at3 with dimensions4,3 and tensor12, exterior matrices up to220 | Lambda defects and exact C2 relation verified; 0.653155 s. |
| `C_group_certificates` | Two groups of order729,531,441 additivity triples each;8 twist groups with512 triples each;16-element ring with4,096 triples; Frobenius p=2,3,5,7, levels1–3 | Rank distributions16+64 versus0+80, twists and Frobenius witnesses pass; 0.053675 s. |
| `C_involution_certificate` | 49 linear-factor pairs modulo2, exact symbolic matrix identities | Local characteristic-zero witness verified; timed reproduction0.519012 s. |
| `C_characteristic2_quadratic` | 1,024 candidate forms,2 compatible with the pure-submodule test,0 invariant under all required isometries | Characteristic-two obstruction verified; timed reproduction0.028580 s. |
| `C_orthogonal_certificate` | p=3,5,7; standard dimensions7,9,11; tensor dimensions49,81,121; largest exterior dimensions35,10,35 | Orthogonal witnesses pass; 0.036431;0.025561;0.158671 s. |
| `C_torsion_trace_certificate` | 81-element ring,531,441 triples,36 S3 multiplication pairs | Torsion trace witness passes; 1.230169 s. |
| `C_finish_lowrank_lambda` | Six O3/O4 witnesses at p=3,5,7; tensor dimensions30,40,90,140,182,336; invariant forms checked | Previously missing low ranks fail special lambda identities; 0.631044 s total. |
| `C_finish_bockstein` | 260 rank1/2 matrices,30 involutions,1,808 block candidates,652 admissible extensions; exact cycle/twist/parity and rank4 order-two checks | Bockstein invariant and flat nilpotent witness pass; 0.192191 s. |
| `C_finish_dualnumber_ring` | 6,736 extension candidates among7 endpoints,197 admissible;292 quiver pairs through dimension(2,2),2,076 invariant-subspace lifts;7 nonzero irreducibles of degree≤4,49 tensor identities | Every primary parity, including the earlier invisible trace-zero example, and every tested tensor identity pass; 0.437312 s. |
| `C4_finish_realization_certificate` | Nonzero obstruction:32 crossed-module identities,16 cocycle quadruples,2 possible trivializations.512 cochains yield16 cocycles/8 marked classes/4 admissible classes,8,192 associativity triples. Order54 example with nonabelian derived subgroup of order27:157,464 triples | H3 obstruction, exact centre/derived criteria, and complete finite comparisons pass; 0.265219 s. |
| `D_pencil_checks` | Conic pencil:4 base points,3 reducible fibres,NS rank5. Elliptic-product pencil:6 base points,6 reducible fibres,NS rank8; exact resultants and intersection matrices | Corrected mobile ranks0, versus uncorrected3 and6; timed reproduction0.635696 s. |

The five inherited certificates that had no recorded elapsed time were reproduced only to fill that reporting gap. `logs/finish_missing_certificate_timings.json` records each return code, exact source SHA-256, elapsed time, and separate `_finish_timed.txt` output. This does not upgrade the scope of any certificate.

Source-access and production programs are separate from mathematical certificates. `A_inspect_sources.py`, `B_read_manuscript_ranges.py`, `B_fetch_sources.py`, `B_finish_fetch_sources.py`, and `download_source.py` fetch, extract or inspect sources; their logs and exact locators are retained. They do not prove a theorem. `prepare_tex_runtime.py` records package names, hashes and timings in `logs/tex_runtime_fetch*.json` (recorded runs11.534803,7.880543 and22.738112 s). `build_paper.py` records every compiler pass, return code, overflow and elapsed time in the dated build JSON/text logs. `render_pdf_qa.py` and `render_finish_pdf_qa.py` record page selections; the visual checks are human-facing model inspections, not automatic proof tests. `integrate.py` merges catalogs and checks identifiers; `update_status.py` is the inherited report generator, superseded for this continuation by `finish_report.py`; `checkpoint.py` writes immutable archives and exact manifests. These editorial and production operations are never counted as mathematical progress. Where a historical source-access operation recorded no elapsed time, we leave that fact explicit rather than invent a runtime.

## Corrections, with attached file and line

All locators in this table refer to the unchanged attached files, with paths relative to the supplied bundle. Line numbers are therefore reproducible and do not shift when our working paper grows. `first prompt` means `RESEARCH_SA17_first_run_PROMPT.md`; `study` and `transcriptions` mean their corresponding unpacked attachment directories. We do not silently alter the supplied transcriptions.

| Attached file and original line | Correction and mathematical consequence |
|---|---|
| First prompt93–94 (R2); study/readings/K126-K132.md626–627,998–999,1036; K126-K132_CORRECTIONS.tsv15 (CR014) | “Fine in odd characteristic” was only asserted in the model k[s]/s² in the reading; the prompt dropped that qualification. The claimed canonical comparison fails for every p, by A4:all-primes. The all-rank finite semi-local theorem is proved separately and survives this failure. |
| First prompt131 (L4); checkpoint02/RESEARCH_SA17/RESEARCH_SA17_report.md22 | L4 asks for failure at2 and is proved, strengthened to every p. Its former “Refuted” label was wrong; R2 is the refuted assertion. |
| study/STUDY.md343–344 (SA17-14); transcriptions/MPL_131_transcription.tex335 | The study's “complete local domains” does not transcribe “irreducible”. The irreducible reading fails with an embedded associated prime (A:NR-counterexample); the integral reading makes this displayed nonzero-ideal test vacuous. Murre's unique-associated-prime condition is the corrected substantive statement (A:NR-density). |
| transcriptions/MPL_131_transcription.tex61,304,321; checkpoint02 report5 | Scan2 has a finite test scheme; scan14 omits the qualification on Z. A:8-literal refutes unrestricted wording only. It does not refute the intended finite-type theorem, whose sufficiency remains separately under investigation. |
| First prompt135–136 (L6); study/STUDY.md150–151; transcriptions/MPL_129_077-115_transcription.tex474–486 | The tensor formula uses the finite Dieudonne module M. The lead substituted Delta*(G), producing a false formula. B:coLie-Dieudonne gives the corrected comparison; B:L6-refutation records the concrete derived-complex discrepancy. |
| study/readings/K126-K132.md989 (hunch2) | Hironaka's deleted-point counterexample has fibres of dimension≤1 over a threefold base. It refutes the predicted relative-dimension≤1 answer; it does not refute a separate one-dimensional-base claim. A:nonfinite-descent and A:polarized-descent state the negative and positive results with their exact hypotheses. |
| First prompt229; transcriptions/MPL_133_transcription.tex1367–1405; checkpoint02 report17 | The page adds no perfect-field hypothesis. The Galois-twisted multiplicative counterexample refutes the requested smooth-kernel assertions over Fp. Over algebraically closed fields that multiplicative extension splits up to isogeny. The noncommutative unipotent alternative is now proved over perfect fields in the explicitly stated finite-type formal category, by C:formal-noncommutative-unipotent. |
| First prompt124–125 (L1); study/STUDY.md394–400,414 | The naive induction identifies modularity after a closed base change with the original locus, losing transverse infinitesimal information. It is insufficient. A:uniform-AR and A:local-models-suffice give a complete repair conditional on actual local representing schemes; the remaining actual7-to-local-model implication is still stated as a gate. |
| First prompt L2; transcriptions/MPL_131_transcription.tex308 (scan14 margin); checkpoint02 report20 | The marginal word “Non” alone did not decide L2. A:L2-counterexample now does: all noetherian adic effectivity holds while actual7 fails. This is a proved mathematical refutation, not an inference from handwriting. |
| study/STUDY.md449–460 and its cote131 literature discussion | Murre, Bourbaki294, is the published form of the cote131 programme. Its unramified theorem, Corollary2, and Section4 descent theorem are opened and matched hypothesis by hypothesis. Its note states the locally quasi-finite programme without supplying a proof of the remaining literal7 gate. |
| transcriptions/K127-01_transcription.tex65; study/readings/K126-K132.md358; intake204,267–269 | The ink is Gamma(Y,O_Y), without a prime, as decided in the supplied intake at600dpi. The intended mathematical condition needs Gamma(Y',O_Y'), because Gamma(Y,O_Y)=A for Y=SpecA. This is an author's slip; the corrected mathematical expression must not be presented as the literal ink. |
| study/readings/K126-K132.md412–416,994 | The comparison in127 Lemma1.3 is now proved directly by A4:flatclosure, for any f and retrocompact U. It is no longer an open step, and the conductor route suggested in the reading is not needed. |
| checkpoint02 report8 and19 | The all-rank theorem and the uniform Artin–Rees step were awaiting a second audit. Both now have targeted independent audits, full proofs, and separate check events. Fixed rank, all finite ranks and arbitrary free ranks retain their different quantifiers. |
| checkpoint02 report12; results_B.csv row B:crystal-counterexamples | The crystalline refutation formerly depended on a detector with no second-party check. B:finite-PD now has a separate all-prime proof audit and exhaustive p2,p3 verification on all three bases. This dependency is discharged, rather than hidden by a stronger label. |
| checkpoint02 report9,11–12,14 and the listed Known rows | A citation alone was insufficient. The paper now writes the derivation from each opened source, as indexed below. Residue-field, reducedness, finiteness and target-category hypotheses are retained. |
| checkpoint02/CHECK_EVENTS.tsv71–72,74,87–89,92 (own-proof labels),79,83,85,90,97 (locator-only types),91,93,99 (mixed types), and the complete47-entry normalization log | Own work is not described as a second-party check. All47 historical nonstandard types were retyped into the six allowed categories, preserving the old text in each outcome and in `logs/finish_check_type_normalization.json`. New C4 own-proof events were also corrected; root independent audits remain separate events. |
| checkpoint02 report74–76 | The corrections stub is replaced by this file-and-line table. No earlier proof is silently claimed checked because its summary was read. |

### Search-qualified novelty and attribution

The refutation of cote128 Lemma1 in every positive characteristic is **new as far as we searched**; this is not a priority claim. The exact search record is `logs/A4_finish_novelty_search.json`. It includes English and French queries for non-flat descent, square-zero units, additive versus multiplicative cocycles, logarithmic derivatives, and the explicit relation ya−xb. We opened Beauville–Laszlo's 1995 descent lemma and Michel Hua's project, Section12, printed pp73–74 of its current public document. The latter leaves this lemma and the ensuing infinitesimal theorem unverified and discusses the logarithmic boundary; it does not provide this all-prime counterexample. We credit that comparison of stated scope to **Michel Hua's project**. Our counterexample and proof are given in full and do not use its unverified statements as mathematical authority. Murre294 is an identification of the published programme, not a new theorem or a priority assertion by us.

### Derivations for the requested Known rows

| Statement | Opened source and exact deduction written in the paper |
|---|---|
| A:completion-descent | Murre294 Section4, theorem(d); complete noetherian local base change is faithfully flat and the separated locally quasi-finite scheme is locally finitely presented. Descent of the two morphism properties gives precisely the asserted scheme. |
| A:etale-corollary | Murre Corollary2, printed p247, after A:artinian-tests extends the infinitesimal condition from Artinian rings to all nilpotent thickenings. The individual F1–F6 identifications are written. |
| A:polarized-descent | Original SGA1 VIII7.7–7.10, printed pp172–175; finite locally free descent and descent of an ample invertible sheaf are distinguished from ineffective unpolarized nonfinite descent. |
| A4:artinianflat | Stacks051E, Lemma10.101.7; applies to arbitrary modules and an injective Artinian base map. Detection of zero modules is proved separately. |
| A5:projectivity | Milne and Conrad exact polarization/projectivity locators in sections/A45.tex; the normalized Poincare pullback gives an ample bundle, its cube gives a finite locally free pushforward and a projective-bundle immersion. A fixed global projective dimension is a separate bound. |
| B:square-zero-Hom | Lau, Relations, Lemmas3.2–3.3; pointwise lifting and p-killed kernels produce the uniform Hom bound by a written descent argument. |
| B:effectivity | de Jong1995 Lemma2.4.4; finite projective Hopf algebras and all structure maps are lifted level by level. The proof explicitly explains why no noetherian restriction is needed here. |
| B:NiceIV | The exact nilpotent-display equivalence is applied to connected groups, then Cartier duality gives the dual-connected alternative; arbitrary PD powers are allowed only with the stated group-theoretic alternative. |
| B:positive-crystals | Anschuetz–Le Bras Theorem4.74, Lau7.6,7.9,9.3,9.5, de Jong–Messing4.6; the paper distinguishes the ordinary and divided targets and proves each permitted passage. The reduced excellent PD-torsion-free deduction is now separately proved. |
| B:divided-target | Lau9.3 retains divided Frobenius; pPhi1=Phi cannot recover it in a p-torsion envelope. Corollary9.5 is used with its exact Hom bound, not promoted to integral ordinary fullness. |
| B:DVR-classification | Breuil4.2.2.9 and Kisin AppendixA.2,A.5,A.6; the window/crystalline module comparison and p2 qualification are written, with perfect residue field explicit. |
| C:DVR | Burroughs Proposition1.1/Theorem1.2 for Z; the DVR proof separately lifts and compares lattices, avoiding a false unrestricted Dedekind-ring paraphrase. |
| C:field_WG_structure; C:algebraically_closed_WG | The opened hermitian-category decomposition is applied to the endomorphism division algebra of each self-dual indecomposable. Over an algebraically closed field it gives symmetric, alternating and nonself-dual basis contributions separately. This does not classify all modular indecomposables. |
| D:local | Pepin2012 Theorem2.2.1, Corollary2.2.2 and Theorem4.1.1, with the opened polarization/sign conventions; solving the fibre intersection matrix gives the local correction, the Neron symbol and the component-group denominator bound. |

## Typesetting verification

The 63-page LuaLaTeX PDF passed build-log and visual checks at the second checkpoint. The initial complete build had 2 boxes above2pt, and a subsequently added display introduced1 more; all3 were repaired. The final build has0 overfull boxes above2pt (one residual1.40959pt box), no undefined references and no missing glyph warnings. We rendered and inspected26 pages, covering every former-overflow location and a spread sample across the document. Exact PDF hash, pages and build logs are recorded in logs/pdf_qa_passed.json. Later revisions require fresh verification.

## Continuation proof movements — 2026-11-19T13:37:08.436154+00:00

The unramified corollary is now independent of the unresolved main theorem. The generic Artinian quotient argument establishes the exact missing implication to Murre F8. The Artin--Rees local-to-global route is written fully in the paper, and the strengthened pro-modular version of7 has a complete induction/gluing proof. The literal actual-modularity condition is not silently replaced by that stronger condition.

The new independent PD audit and p2,p3 certificate validate the crystalline refutation. The new orthogonal witnesses settle every remaining rank in the special-lambda question, including rank3. Their integral hyperbolic lifts and the equivariant torsor transfer extend the criterion to every affine base with2 invertible. These are genuine item movements; the surviving ring-classification and formal-group gates remain explicit.

## Historical audit-label corrections

47 historical events used nonstandard labels or placed a locator in the type column. They are now retyped using the six permitted categories. Every original type/locator is retained in its outcome and in `logs/finish_check_type_normalization.json`, which records exact component-file lines. Own proofs remain expressly own work; an outline check remains only an outline check. No additional independent verification is invented. The merged `CHECK_EVENTS.tsv` is regenerated from these preserved component records.

### Continuation PDF verification, checkpoint 03

The continuation PDF has 76 pages. We inspected 28 selected pages covering the additions, the opening material, and the bibliography. The LuaLaTeX/BibTeX build completed without undefined-reference warnings; the largest overfull box is 1.40959 pt, below the specified 2 pt limit. The exact PDF hash and inspected pages are recorded in `logs/pdf_qa_passed.json`.

## Continuation movement — L2 settled

At 14:27 UTC we completed A:L2-counterexample. The simple supported subgroup H, not the henselized quotient candidate, satisfies every required axiom except7 and has full noetherian adic effectivity. The fixed principal ideal (tx) is the decisive Krull-intersection step. Two separate agents independently checked all axioms. Main A.1 remains open at its distinct local-model/fpqc gate. The C4 proofs and the full degree-two dual-number representation ring have also passed independent targeted audits. These are working movements, not the first formal three-hour review, which remains due at16:06:58 UTC.

### Continuation PDF verification, checkpoint 04

The updated PDF has101 pages. The final build completed in33.313182 s, with0 boxes above2pt, maximum1.40959pt, no missing glyphs and no undefined references. The first attempted build exposed one malformed matrix row separator and a font-dependent accent construction; both were repaired before the clean rebuild. Root rendered and directly inspected40 pages on ten contact sheets, including the complete L2 and henselized-candidate arguments, the new B union arguments, the dual-number ring and nil-invariance, the C4 constructions and formal lemmas, earlier Parts, and the bibliography. No clipping or collisions were found. The exact hash, pages and compiled-source hashes are in `logs/pdf_qa_passed.json`; checkpoint03 QA is preserved separately.
