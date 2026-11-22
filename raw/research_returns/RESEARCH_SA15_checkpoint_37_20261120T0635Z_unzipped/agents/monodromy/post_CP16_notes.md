# Post-CP16 candidate work

2026-11-19T14:51:36.511933+00:00

New source only, without editing frozen references: Ekedahl and van der Geer (2009), Cycle Classes of the E-O Stratification on the Moduli of Abelian Varieties, original published PDF https://van-der-geer.nl/strata_PiM269.pdf ; web turn891811006view0. Retained in sources_post_CP16, including full text and rendered original pages607,608,620,624 actually viewed. Read Prop6.1 and proofp601; Thm8.2/Cor8.4 proofs607--608; Thm11.4(i)619 and Thm11.5/Ex11.6p620; Ex12.2p623--624. Large-p converse explicitly excluded from use. Read original Stacks0559 full statement/proofs freshly at turn700618156view0.

Searches: system2 abelian surfaces p rank one stratum irreducible smooth nonordinary divisor Oort Chai; p-rank strata A_g geometrically irreducible f positive theorem. Verified with system1 Ekedahl van der Geer cycle classes Ekedahl Oort strata Theorem11.5 irreducible pdf, and Oort stratification moduli abelian varieties smooth Ekedahl Oort stratum theorem2001. The Chai/Oort journal abstract opened but is not used in this candidate.

Candidate: generic_nonordinary_ppav_groups_post_CP16_candidate.tex; extra bibliography references_post_CP16.bib. Exact generic scope includes every geometric component for f0, not a false irreducibility assumption. Main image argument counts full frame components, avoiding a global basis of invariant covectors. A finite set of degrees yields nonempty opens and finite-field examples; no countable intersection conclusion.

Separate universal mixed degree-one local exploration: code/explore_mixed_universal_Q_point.py and pencil version retained with outputs. Q-point s=(z³/a,z,0,0,1,0,0,0,1), D=z³/a, stable pairing=(a⁴+a³z⁴+z¹⁰)/(a²z³), a nonzero polynomial in z for every a≠0. No full group assertion from this local computation. Earlier failed diagonal-point trials retained; cause was nonsymmetric Ro and incorrect assumption the chosen point lay on Q.

## 2026-11-19T14:54:06.919526+00:00 — source overstatement and scope repairs

Parent independently viewed original EvdG p624 and caught that its sentence claiming all four genus-two final flag covers have degree one is too broad: the ordinary stratum has degree p+1, as shown by the p623 pushdown table and the gamma formula immediately following on p624. The superspecial flag fibre likewise is not a singleton. Our uses concern only the two middle strata, where the canonical line is unique; the corrected proof now establishes that fact via finite etaleness and one geometric point. Exact pre-correction draft retained as generic_nonordinary_ppav_groups_post_CP16_failed_scope.tex. The current candidate also states reduced locally Noetherian base for the high-image vector bundle argument (RD correction), and explicitly retains the fixed-subgroup bound in its open conjugacy conclusion (root clarification). These are corrections, not promotions.

## 2026-11-19T15:00:30.308722+00:00 — complete audit and promotion

Root full independent proof/source PASS is recorded at 14:57:39.714409 UTC in root outputs/root_generic_nonordinary_ppav_audit.json. RD independently passed the entire proof and source chain. I read Example 3.4 p589 and the full Proposition 4.5/Lemma 4.6 proofs pp592–594, and added their exact canonical-rank-set argument for the two middle flags. The source parenthesis incorrectly writes semisimple rank g−f; the proof imports only the canonical rank-set formula, while stable rank is f (also explicit p594). All-five theorem statements are now Proved. Renamed generic_nonordinary_ppav_groups_post_CP16_candidate.tex to generic_nonordinary_ppav_groups.tex because both complete independent audits passed; all existing label identifiers retained. The exact pre-correction failed_scope draft remains retained. Main fixed nongeneric mixed-modulus and arbitrary-X structural gates remain open.

## 2026-11-19T15:23:25.665382+00:00 — every fixed mixed modulus, degree one

The full degree-one GL8 theorem now has complete independent root and RD proof/source/code audits. Root recorded at15:22:49.551136UTC; exact proof combines uniform D²Q, generic stable loss one on smooth Q, full order128 inertia from independent nonsquare residues, exceptional Lang-rank dimension at most8, irreducible nonzero Lang cover, and elementary generation from full root groups. No finite-group classification is needed. Root independently supplied the rank-two Gram-map argument; the author independently audited it and reran its exact auxiliary certificate without altering author outputs. All six mathematical assertions promoted; existing labels retained. Renamed mixed_degree_one_uniform_inertia_candidate.tex to mixed_degree_one_uniform_full_groups.tex solely because both complete independent audits passed. The previous source-scope failed draft is unrelated and remains retained. All exploratory programs (including failed diagonal Q-point choices and finite F2 rank probes) and original outputs remain in the archive; no finite-field probe substitutes for the universal proof. The canonical promoted file is now frozen for CP17.

## 2026-11-19T15:53:01.331715+00:00 — uniform fixed-modulus degree two promoted

Canonical file mixed_degree_two_uniform_full_groups.tex replaces mixed_degree_two_wreath_grid_candidate.tex on root authorization after complete root/RD proof/source/code passes. All six stable assertion/scope identifiers retained. Root audit15:51:50.923536UTC; own exact graph0.0001956549967871979s, root0.00013814800331601873s,RD0.00010532900341786444s, original output preserved. OC independently passed every mathematical argument, with source/code supplement pending. The proof obtains all gluing translations via labelled hyperplane monodromy, then compares opposite-Picard-twist boundary families through a common grid using only its constant finite Lang part (rank30 versus generic34). Every proper invariant subspace contains K32, and the elementary blocks plus transvection classification give the full two-covector stabilizer.

Discarded un-twisted grid idea: distinct3+3 partitions of six distinct elliptic points cannot each have both triples equivalent to3O, because Sym²H0(3O)→H0(6O) is injective and line factorization is unique. This was caught before the written proof; the actual proof uses opposite Picard twists, with their source systems translated copies of the already proved degree-one family. No invalid un-twisted comparison was used. Higher fixed-modulus degrees remain a separate gate; this promotion does not assert them.

OC source/code supplement completed immediately after promotion: complete independent PASS, exact author-preserving graph rerun0.00010262399882776663s; fresh sources0BMB/0BTN/09ZS and original Kantor–Seressp22 actually read/viewed. Canonical status now records all three full audits.

## 2026-11-19T16:26:39.864908+00:00: strip promotion and rename

The complete candidate `mixed_three_by_b_strip_groups_candidate.tex` was renamed to `mixed_three_by_b_strip_groups.tex` after full independent root, reduction/descent and obstructions/crystals proof audits. The candidate filename is superseded; no mathematical passage was removed. Existing label identifiers ending `-candidate` are retained for stable cross-references, while each substantive statement visibly says Proved. Header was shortened for layout. The finite certificate checks only b=4..32 and the triple-label coinvariants; the universal conclusions rely on the written proofs. Root/RD code reruns preserved author output. This proves only first-factor degree3 strips, not all balanced higher degrees.

## 2026-11-19T16:52:20.616270+00:00: degree-three chord separability repair

The original degree-three draft was preserved exactly as `mixed_degree_three_norm_groups_failed_separability_scope.tex` before replacing the invalid inference “generic injectivity implies separability” in characteristic two. Root and RD independently flagged it. The corrected candidate differentiates the two chord incidences: a zero chord differential would force tangency at both distinct points, contradicting total line/cubic intersection degree3. Generic injectivity plus this separate separability proof now gives degree1. No theorem was promoted before the correction.

## 2026-11-19T17:00:20.468671+00:00 — Degree-three norm theorem promoted

Created canonical `mixed_degree_three_norm_groups.tex` after complete root audit at2026-11-19T16:59:48.082057UTC (`outputs/root_d3_norm_audit.json`) and complete reduction/descent proof/code PASS. The complete candidate is retained unchanged as `mixed_degree_three_norm_groups_candidate.tex`; the earlier pre-separability-correction draft remains `mixed_degree_three_norm_groups_failed_separability_scope.tex`. Existing labels are preserved; the canonical file changes statuses and records exact audit/run scope, with no mathematical passage removed. Root independently checked all exceptional jet strata, translated-cover pure gluing, common partial normalizations and group closure. RD independently reran all729 graph cases in0.06837776099564508s; monodromy read the entire parent program and reran it output-only redirected in0.0629995989947929s. Parent output SHA256632f6e03547f5a040ad1f78ec01780d1d32597d43f9e250d7ae5aef47195ce92 preserved. This solves balanced degree3 for every ordinary modulus; higher odd degrees remain open.

## 2026-11-19T17:10:36.572040+00:00 — Post-CP19 wording precision

In canonical degree-three proof, replaced exactly `For a noninvariant source the translated intersection is finite.` with `For a smooth irreducible noninvariant source the translated intersection is finite; the generic source has these properties by the contact-system smoothness argument below.` The old unrestricted sentence is false for a reducible source sharing a component with its translate. The proof already establishes generic contact-source smoothness and ampleness gives connectedness/irreducibility, so the theorem is unchanged. Complete prior canonical retained at `history/mixed_degree_three_norm_groups_pre_qualifier_20261119T1706.tex`; delivered CP19 archive remains immutable. Root authorized this clarification after archive release.

## 2026-11-19T17:16:01.198598+00:00 — All odd fixed mixed-product degrees promoted

Canonical `mixed_all_odd_norm_groups.tex` created from the complete retained candidate after root full proof/source/code PASS2026-11-19T17:15:03.727853UTC (`outputs/root_mixed_all_odd_audit.json`, seven labels) and reduction/descent complete independent PASS. All existing labels retained. The candidate remains unchanged, while the canonical statuses and verification scope are promoted. Author graph run0.03620041400426999s; independent root0.050087591996998526s and RD0.04048306200274965s, outputSHAc46c99f35de230257145e19e8f77ce798a77e021818bfc1f91ab9f35c98c7b58 preserved. The proof treats simultaneous all-type norm geometry and universal common graphs; the nine finite cases are supporting only. This settles all odd balanced degrees for every fixed ordinary modulus, not arbitrary ambient monodromy.

## 2026-11-19T17:25:18.766648+00:00 — Bounded elliptic secant literature search retained

The earlier post-CP18 exploratory search used queries `elliptic normal curve characteristic 2 symmetric determinantal secant variety Cartier matrix`, `elliptic curve Frobenius pushforward theta divisor symmetric matrix characteristic two secant`, `Thomas Fisher higher secant varieties elliptic normal curve pdf characteristic symmetric determinant`, and `Frobenius Cartier symmetric matrix elliptic normal curve characteristic two secant theta characteristic`. Primary author result was https://www.dpmms.cam.ac.uk/~taf1000/papers/hsecenc.pdf and its author HTML page. Search results identified the arbitrary-characteristic scope and secant resolutions, but PDF and HTML web opens timed out; a bounded urllib download returned HTTP503. No PDF was saved and no theorem from this source was imported into a proof. The empty exploratory source directory was retained. This was abandoned in favour of the explicit norm/common-graph proof, which closed the all-odd product gate.

## 2026-11-19T17:32:20.494722+00:00 — All even and all balanced mixed degrees promoted

Created canonical `mixed_all_even_groups.tex` from retained `mixed_all_even_wreath_groups_candidate.tex`; every existing label is unchanged. Complete root audit at2026-11-19T17:28:40.525639UTC (`outputs/root_mixed_all_even_audit.json`) and complete RD audit at2026-11-19T17:31:32.194594UTC both pass all six statements. Both unequal lifted wreath directions, ambient gluing columns, actual blocks, rank-dropping finite Lang comparison, two internal projections and arithmetic descent were independently checked. Author root graph run0.015011039999080822s; monodromy0.013861629995517433s; RD0.013912451002397574s. Author outputSHA3ad394f4666204684491520985198c95d4012ac997dced5835031ec678fe2f42 preserved. The finite range2,4,...,20 supports graph arithmetic only. Together with the promoted all-odd norm theorem this closes balanced all-degree monodromy for every fixed ordinary times supersingular product. Arbitrary nonproduct ambient A4 remains open.

## 2026-11-19T17:36:56.255511+00:00 — All smooth theta fixed-point jets promoted

Created canonical `nonordinary_ppav_fixed_point_jets.tex`, retaining the complete candidate and every label. Root read/rederived the full proof and entire original theta-jet section and passed all three assertions; RD complete proof/dependency PASS at2026-11-19T17:34:25.277598UTC. The proof uses first-order translation, not an unverified integration of vector fields, and separately establishes nonzero Cartier rank by the genus-two canonical square-ratio contradiction. No numerical test is needed or claimed. This is a geometric refinement toward fixed nonproduct monodromy, not itself a full-image result or separately counted main-gate closure.

## 2026-11-19T17:49:36.619132+00:00 — Post-CP20 universal nonordinary degree-one inertia candidate

The new file `nonordinary_ppav_uniform_Q_inertia_candidate.tex` is separate from the frozen CP20 paper. It proves generic stable loss one on the universal smooth Hermitian cubic via a symbolic pencil and an equal-cubes normal-form reduction; exact certificates and outputs are retained. The final corollary is only a full elementary order128 inertia subgroup. Exceptional Lang-incidence compatibility remains the precise global gate.

Executed initial code `ppav_theta_Q_pencil_pfaffians.py` is retained unchanged; its complete strengthened version has a separate filename. The finite GF8 exploration is retained unchanged. Failed weight2/weight4 and all-binary-support isotropic-pencil searches raised their final assertion and produced no certificate; exact executed sources are retained under `history/ppav_theta_equal_cubes_pencil_failed_*.py`, with failure notes under `outputs`. They were superseded by a directly verified GF8 witness, not silently reclassified as successful.

Primary-source lookup on Hecke-orbit transfer: the Chai–Oort survey/book URLs returned403; no theorem from them was imported. The original D’Addezio–vanHoften arXiv2205.10344v2 full PDF was opened and introductory pp1–5 read: its own theorem assumesp>2, while its introduction attributes the Siegelp2 theorem to Chai–Oort; v2 explicitly records a prior rigidity gap in v1. No Hecke result is used by the new inertia proof.

## 2026-11-19T17:56:55.221916+00:00 — Universal nonordinary Q-inertia promotion

`nonordinary_ppav_uniform_Q_inertia.tex` is the proved canonical copy after complete root, reduction/descent and obstructions/crystals proof/source/code audits. The exact candidate file is retained unchanged; only the status header changes in the canonical copy, and all three stable label identifiers retain their existing suffix. The conclusion is the full order128 elementary geometric inertia subgroup for every fixed nonordinary principal surface in degree one; Lang connectivity and the full global image remain explicitly open. Root audited17:54:50.737761UTC; RD17:56:26.985557UTC; OC full pass received before promotion. No new monodromy conclusion is imported from the late Coble literature.

The fixed-point theta jet promotion earlier also has the precise root full-audit timestamp17:34:09.959630UTC, outputs/root_nonordinary_theta_jets_audit.json, supplementing the recorded RD17:34:25.277598UTC.

## 2026-11-19T18:24:25.743903+00:00 Conditional polar Lang argument

Saved `nonordinary_ppav_polar_Lang_conditional_candidate.tex` with the full third-derivative compatibility lemma, conditional GL8 closure and the exact failure of original-tensor stability to imply polar stability. The latter is proved by the irreducible Fermat-cubic coefficient hypersurface, without an unverified finite reflection-list formula. No actual Cartier locus satisfying the extra hypothesis is asserted. Root supplied the third-derivative idea. AV access note updated to record OC actual18:09 primary reads only. New search results read: RS published original Prop2.9/2.10; unrelated search leads not imported.

## 2026-11-19T18:32:30.972366+00:00 Universal two-rank-zero polar candidate

Saved `p_rank_zero_ppav_degree_one_groups_candidate.tex`. Exact symbolic action matrix has the constant-one81x81 minor deleting rows467,478,578 for every a,b,c; source and output retained. Freshly read RS original Proposition2.13 fullproof, Proposition3.8 fullproof and Corollary5.6, supplementing prior source reads. The candidate transfers equality of Coble cubics to their polar tensors, without asserting equality of marked trivectors. Root and RD audits requested; no promotion before independent checks. Discovery probes retained unchanged.

## 2026-11-19T18:37:54.661609+00:00 Universal two-rank-one polar candidate

Saved `p_rank_one_ppav_degree_one_groups_candidate.tex`. All smooth f1 curves normalize to y²+xy=x5+a x3+b x with b nonzero; exact81minor deleting123,345,356 is b^4. Program uses77unitpivots and one explicit4minor. Initial generated assertion syntax error retained verbatim in history plus diagnostic; successful canonical execution0.01662725299684098s. Earlier inline residual-discovery source/output retained as actual executed program version. This would extend the f0 candidate to all fixed nonordinary ppav degree1, not higher degrees. The prior finite c9=c15=1 example with polarLie2 was singular at(1,1), so is not a smooth-curve counterexample; its output is retained unchanged.

## 2026-11-19T18:39:17.749265+00:00 Conditional and all-f0 degree-one promotion

Root+RD+OC full proof/source/code audits passed. Canonical `nonordinary_ppav_polar_Lang_conditional.tex` and `p_rank_zero_ppav_degree_one_groups.tex` created; exact audited candidate files retained unchanged. Only visible statuses, completed-check paragraph and the conditional section forward pointer changed. All seven labels retained verbatim. The all-f1 extension remains Candidate until its independent audits.

## 2026-11-19T18:40:49.734186+00:00 All fixed nonordinary ppav degree-one promotion

Root, RD and OC complete proof/source/code audits passed. Promoted canonical `p_rank_one_ppav_degree_one_groups.tex`, preserving the exact audited Candidate file. Only visible status and completed-check paragraph changed; all four labels retained. This proves geometric=arithmetic GL8 in degree one for every fixed nonordinary ppav surface in characteristic2. Higher fixed nonproduct degrees remain the next gate.

2026-11-19T18:41:13.710021+00:00: Updated only stale forward-scope remarks in the promoted conditional/f0 canonical files after the all-nonordinary degree1 theorem was proved. Prior canonical versions retained as history/pre_f1_closure_*.tex and exact diff history/f1_closure_forward_references.diff. No proof or hypothesis changed.

2026-11-19T19:08:28.550247+00:00: Odd-block candidate product nodality sharpened to exact rank5 on axes and explicit finite cross-tangency equations offaxes, as independently requested by root/RD. Prior draft and exact diff retained in history; no statement scope change.

2026-11-19T19:10:28.922943+00:00: Promoted canonical `nonordinary_ppav_odd_natural_blocks.tex` after complete root/RD audits. Exact candidate retained; only status changed. This proves actual GL8 blocks in every odd degree, not full images.

## 2026-11-19T19:11:56.873213+00:00 Three-theta conditional reduction

Saved `nonordinary_three_theta_graph_reduction_candidate.tex`: general normal-base clopen Lang closure, exact odd-labelled graph proof, and conditional full-image assembly. Source lifts constrained by sumr=0 stay in one source system; heart span is codimension1, sufficient to force a global hyperplane and contradict exact odd covectors. Explicit unproved inputs include theta self-triples/transversality and full productnode/shear image. No blanket d3 theta-goodness claim: pair transversality does not exclude triples. Parent supplied clopen closure approach and cross-branch discussion; all are written for independent audit.

## 2026-11-19T19:39:18.674252+00:00 — clopen graph reduction and characteristic-two trigonal exclusion

Promoted the two candidate files to canonical copies listed in outputs/post_CP22_graph_trigonal_promotions.json after root and RD complete independent audits. Exact candidates remain unchanged. The graph theorem retains both explicit geometric hypotheses; no unconditional higher-degree image is inferred. The Galois proof gives unconditional three-torsion theta nodality. The separate direct-coordinate proof was independently fully read and its entire universal program rerun (0.07797064899932593 seconds), author output preserved. Fresh Stacks0C1B and09DX statements and full proofs were opened and read; references appended from the retained post-CP22 fragment. One failed apply_patch context match changed no Galois text and was corrected immediately. No mathematical failure occurred.

## 2026-11-19T19:41:30.597299+00:00 — degree-three node/gluing candidate

Complete six-assertion candidate nonordinary_ppav_degree_three_node_gluing_candidate.tex saved for root/RD audit. New proofs: finite three-dimensional eigenmaps for each order-three translation; double theta-difference cover with characteristic-two inertia; two-transitive eighteen-node covers and independent factor transpositions; normal-Lang finite-torsor extension of the split quotient and selected-edge star forcing every gluing heart. The final GL80 theorem currently assumes a nonproduct three-neighbour; root separately proves existence. No promotion before audits. Exact 81-case graph supplement passed at19:41:14.217748UTC in0.012680367006396409seconds; dimensions76/72/68/75 and star8/10.

Search/source audit: engine2 queries on genus-two characteristic-two triple ramification and torsion packets found no imported uniform theorem. Opened Dolgachev–Lehavi arXiv0710.1298v3, introduction characteristic-not-two restriction and full Proposition3.1 pp9–10; its pair count does not by itself exclude triple coalescences and was not used. Opened Stacks0C1B full section/proofs and09DX full lemma/proof; only standard Riemann–Hurwitz/different and Kummer constructions used in own proof. Relevant web refs: turn476913893view0, turn449922432view1, turn829347511view0, turn280895633view0, turn280895633view1. The speculative isotropy exclusion was rejected: the sign-corrected Weil pairing on a common trigonal pencil is instead1. The successful characteristic-two Cartier proof replaces it.

## 2026-11-19T19:45:01.518160+00:00 — degree-three node/gluing promotion

Canonical nonordinary_ppav_degree_three_node_gluing.tex promoted after complete root/RD mathematical/source/code passes. Exact audited candidate c3d91895a234cb851d0023803bbb3692324d484fa92a6ba671dfc3302358a8e8 retained unchanged; all six stable labels retained. Root separately supplies nonproduct three-neighbour existence, yielding all fixed nonordinary degree-three images. No higher odd multiplier is claimed.

## 2026-11-19T19:57:59.521677+00:00 — Fixed nonordinary ppav degree two

Complete candidate nonordinary_ppav_degree_two_wreath_theta_candidate.tex saved for root and OC audits. The graph certificate was actually run and passed in 0.00013906999811297283 seconds. The six-theta stable rank is 25+5f, below generic33+f; only clopen finite-Lang transport is used. No all-degree conclusion is inferred.

## 2026-11-19T20:02:27.725392+00:00 — All fixed nonordinary ppav degree-two promotion

Canonical `nonordinary_ppav_degree_two_wreath_theta.tex` promoted after complete root and OC proof/source/code audits. Exact audited candidate 0f44cc19553f6b576a702cadef61a8ec7dcb35b747bb0db43c0bfff947a5af9f retained unchanged. All labels retained; only short proved statuses and actual check runtimes appended. This establishes the full stabilizer in degree two, not all higher degrees. Separate even-addition candidate is outside CP23.

2026-11-19T20:07:21.348975+00:00: Removed two literal exponent commas in the separate even-addition candidate, introduced by string escaping; exact pre-correction draft and diff retained in history. No mathematical change. RD complete symbolic proof audit passed, with no new source/program run claimed.

## 2026-11-19T20:10:31.703272+00:00 — Even addition promotion

Canonical nonordinary_ppav_even_addition.tex promoted after complete root/RD independent proof passes. Exact corrected candidate retained; five labels unchanged. This proves full even-degree stabilizers whenever both odd addends already have full images, in particular d=3^i+3^j. It does not assert all even degrees. No new finite run was needed for the symbolic extension.

## 2026-11-19T20:36:22.731773+00:00 — Bounded fifth-torsion census promotion

Promoted nonordinary_five_theta_self_isogenies.tex after full parent proof/source/code audit. Exact candidate retained. Four stable labels unchanged; only statuses, actual completed-check scope and exported code paths changed. This is a fixed-source geometric certificate, not a full-image theorem. Separate universal f0 nodality/four-value candidate remains unpromoted.

## 2026-11-19T20:41:02.823072+00:00 — Uniform five-theta geometry promotion

Promoted nonordinary_uniform_five_theta_geometry.tex after full root/RD proof/code audits. Exact final candidate retained. Only statuses, exported paths and completed-check paragraph changed. Stable labels unchanged. Uniform nodal five-self-isogeny and four-value theorem do not themselves assert monodromy. Initial coefficient-domain setup failure retained separately.

## 2026-11-19T20:53:03.927075+00:00 — Good-theta norm transfer promoted

Promoted nonordinary_good_theta_norm_transfer.tex after the full root and obstruction/crystal proof audits. Exact candidate retained; the literal plus-sign typo draft and exact correction diff are in history/. The promoted proof includes the node product, all type hearts, actual source block, and clopen rank-drop comparison for an arbitrary good odd theta kernel. Combined with the proved uniform five-self-isogeny, it proves every fixed two-rank-zero degree 3^i5^j and sums of two such degrees. Fixed two-rank-one degree five remains a separate gate. No new finite experiment is used. Stable labels were preserved.

## 2026-11-19T21:20:08.686834+00:00 — Norm-seven interpolation and exploratory failures

Isolated candidate nonordinary_seven_q8_interpolation_candidate.tex records universal Q8 parameters, Rosati norm7 and exact residual quadratic. Seventeen exact identities passed at20:59:00.912911UTC in0.2739150630077347s. Triple-fibre exclusion remains unresolved. The first rational-coordinate setup failed at the coefficient field gcd; exact v1 source/traceback retained. Version2 was interrupted without output and is explicitly recorded as such, never as a completed test. The separate odd-plus-even parabolic obstruction is recorded in post_CP24_odd_even_boundary_obstruction.tex.

## 2026-11-19T21:52:33.231150+00:00 — Universal norm-seven candidate and retained calculations

The full candidate is frozen for independent root/RD/OC audits. Universal cleared-polynomial arithmetic treats both A(L) cases, and the combined bad-r radical has degree97. All three r choices can be bad only at z^3+z^2+1=0; the normal-form presentation argument avoids that locus. No promotion is claimed before audits. The fixed-C0 elimination and its squarefree48-root/involution/ordinate checks are retained as backup but are not inputs to the universal proof. Every substantive program/output and the two API-only failed verifier versions are listed in outputs/post_CP25_norm_seven_research_record.json. Earlier timeout/field-domain failures remain in history and outputs. No failed mathematical assertion was silently removed.

## 2026-11-19T21:55:56.758981+00:00 — Uniform norm-seven theorem promoted

The exact candidate is preserved. The canonical proof includes all exceptional fibres and both universal resultant gates; finite-C0 probes are explicitly not proof inputs. Only statuses, exported program paths and the audit remark changed. All f0 odd degrees 3^i5^j7^k and sums of two such degrees now follow. The finite membership census through1000 puts the next degrees outside these families at odd11 and even92; these are unresolved degrees, not counterexamples. Fixed f1 degree5 remains separate.

## 2026-11-19T21:56:41.208617+00:00 — Uniform-seven integration and scope correction

Added the canonical theorem to the consolidation list and CP26 required inputs under parent authorization. The earlier odd-kernel scope sentence saying degree7 was not supplied now refers forward to the proved f0 self-isogeny. The f1 degree5 incoming-neighbour gate is explicitly preserved. Exact prior bytes and diffs of all three touched files are retained in history; see outputs/uniform_seven_integration_wiring.json.

## 2026-11-19T22:34:07.027054+00:00 — Nine-theta norm transfer promoted

The exact seven-label audited candidate and all earlier versions remain unchanged. The canonical proof replaces the individual-theta nodality hypothesis with three movable cubic components. All selected18-edge pair lifts and the72/90 stars are justified over the full normal Lang scheme, without identifying stable fibres at rank drop. The complete root and OC audits passed. Every even degree on every fixed f0 principal surface is now proved; the fixed f0 odd11 and fixed f1 odd5 gates remain. The bounded graph and5000-degree arithmetic checks are supplements only. Consolidation and CP27 preflight now include the canonical file; exact prior bytes and diffs are retained.

## 2026-11-19T22:42:08.929350+00:00 — Arbitrary odd nonproduct neighbours promoted

The exact candidate and initial arithmetic wording remain preserved. Full scheme-theoretic dual-kernel connectedness is explicitly proved, rather than attributed to the weaker exercise statement. Unique mixed elliptic axes and their common principal degree imply at most one bad product quotient at each odd prime. Composition and polarized duality give every incoming odd multiplier. Root and OC full proof/source audits passed; no numerical check was necessary. Consolidation and CP27 preflight are wired with prior bytes and diffs retained.

## 2026-11-19T22:48:03.970684+00:00 — Uniform cubic-component norm transfer promoted

The exact candidate remains unchanged. The extension uses e cubic components for any already full odd source degree e>=3, with type size18e², selected S18 pair lifts, and36(e−1) star entries. The source and target ranks drop by(e−1)(2−f); only clopen finite-Lang intersections are transported. Root and OC independently rederived the complete symbolic proof. No new numerical experiment or finite extrapolation was used. The resulting fixed f0 odd family is every odd number divisible by3,5,or7;11 remains the first unresolved odd degree. Exact consolidation/preflight before bytes and diffs are retained.

Actual record time: 2026-11-19T23:04:04.808527+00:00

## Post-CP27 triple-packet inertia obstruction

The earlier speculative ordinary-triple pure-translation route does not follow from stable-rank loss. Under a smooth constant-p-rank normalization over a strictly henselian trait, with all generic node branch sections marked over the trait, normalization F2-torsors and their branch fibres extend and trivialize over the trait. Every generic nodal gluing sign can therefore be chosen over the fraction field. Some choices fail the cycle relation after a triple collision and do not extend over the singular special fibre, but they still have trivial generic inertia. This is loss of finite Lang sections at the special fibre, not necessarily ramification. The proposed use of a triple collision alone to produce a nonzero pure translation is withdrawn as an inference; no proved statement depended on it. A complete descent proof may be recorded separately by root.

The first universal norm-eleven quintic calculation passed the monic-quintic and polynomial-u stage, then reached its 60-second time limit during characteristic-polynomial elimination. Its exact executed source and output are preserved as history/post_CP26_eleven_universal_quintic_v1_timeout.py/.json. No geometric conclusion is inferred. The rational parametrization t=v^2, r=v^2+v removes the quadratic coefficient extension and is a possible computational simplification only.

## 2026-11-19T23:28:03.745136+00:00 — Norm-eleven computation provenance

The initial rational-function/primitive-pseudo-remainder runs each reached their60-second cap; exact source/output versions are preserved. A FLINT wrapper initially failed only when serializing fmpz degree objects; its exact source/stdout/stderr are preserved before the integer-conversion correction. A finite-field consistency hypothesis incorrectly treated the generic triple equations as sufficient without checking c3!=0; its failed assertion is retained, and the corrected direct calculation confirms c3=c2=0 with nonzero separate exceptional condition. No promoted claim used that inference. The final complete candidate and all outputs are explicit Candidates pending independent proof audits. The environment uses python-flint0.9.0 installed outside the checkpoint tree; requirements and the exact command are retained.

## 2026-11-19T23:30:57.340146+00:00 — Uniform norm-eleven theorem promoted

Every fixed indecomposable f0 ppav has a nodal polarized eleven-self-isogeny with120nodes. Every fixed f0 odd degree divisible by3,5,7,or11 is full; every even degree was already full. Remaining first f0odd13, f1degree5/8.

The exact candidate remains byte-identical. All earlier executed versions, failures, discovery resultants, coefficient inputs, factorization outputs and independent Bezout reconstructions remain retained. Three obsolete canonical degree-eleven scope sentences were replaced only with forward references and the new degree-thirteen residual gate; exact prior files and diffs are retained. Both complete proof audits passed before promotion; no numerical sampling or unproved orbit-size assertion is used.

## 2026-11-19T23:49:04.473213+00:00 — post-CP28 norm-thirteen exploration (unpromoted)

Universal interpolation for 3+2g and exact resultants are retained under code/post_CP28_thirteen_*. The five-presentation gcd is exactly D12^5+H4^12, so the initial parameter method leaves mu^5=1. A full-ordinate finite probe and separate binary-only verifier now exhibit an exact four-point fibre on that exceptional surface. This refutes nodality for the selected 3+2g map; it does not rule out another norm-thirteen quaternion representation. The initial field-truthiness error and all prior outputs are retained with an explicit repair record. No frozen CP28 theorem/table is changed.

## 2026-11-20T00:21:37.481581+00:00 — Uniform norm-thirteen theorem promoted

Every fixed indecomposable two-rank-zero ppav has a nodal polarized thirteen-self-isogeny with 168 nodes. For complete |3dTheta| systems every fixed f0 odd degree divisible by 3,5,7,11,13 is full GL; all even f0 degrees were already full. First remaining f0 odd degree17; f1 degree5/even8 unchanged.

The exact audited candidate remains byte-identical. Every earlier executed version, failed or timed-out calculation, four-point packet, coefficient input and exact output is retained. The original 3+2g choice is explicitly false at the exceptional modulus and is replaced there by the independently verified three-anticommuting-unit map. Three obsolete degree-thirteen scope sentences were replaced by forward references and the degree-seventeen residual gate; their prior bytes and exact diffs are retained. Root and OC completed full proof and reconstructive-code audits before promotion. No sampling or unproved specialization inference is used.

## 2026-11-20T01:18:44.228826+00:00 — Norm17 remains open; two exact C0 choices fail

The generic 4+g parameter elimination and the clean mu210/mu88 exceptional models are retained, without a complete promoted theorem. On C0, the first 3+2g+2h choice has an exact five-point residual packet, and the new 1+2(g1+g2+g3+g4) choice has an exact three-point packet. The final checker proves squarefreeness, exclusion of the diagonal and poles, and equality of L,M,nu with L nonzero; the geometric interpretation is written separately in post_CP30_seventeen_C0_failed_maps.tex. The latter interpolation has a repeated pole factor, whose eleven-point reduced support was handled explicitly. All source/output stages remain retained. No CP30 canonical or main-gate statement was changed.

The 40-basis Moore necessary-product shortcut was independently refuted by OC: its necessary locus is larger than the 81 alternating planes. Their complete determinant now supplies a stronger universal one-zero chart; several-zero charts and the actual Cartier/theta identification remain separate. The principal theta-addition/Cartier connection argument is still a lead only.

## 2026-11-20T01:35:30.066376+00:00 — Principal theta Cartier bridge promoted

Principal f0 theta-square Cartier coefficient and conditional auxiliary-cover dual rank only; no full monodromy theorem or fixed-target conclusion. The exact candidate remains byte-identical. The canonical status and completed-audit paragraph are the only proof-text changes. Narrow consolidation and bibliography changes have exact prior files and diffs. The printed local-local character sentence is replaced by an explicit universal-character argument, not silently imported.

## 2026-11-20T01:45:07.155996+00:00 — Twisted Cartier/Moore assembly promoted

Exact twisted Cartier/Moore coefficients and maximal dual alternating rank for every fixed odd principal-cube degree. No new full monodromy degree or generic-curve rank theorem is inferred. The exact candidate is retained unchanged; the canonical replaces only status/audit wording and makes the already-audited cubic embedding reference explicit. All prior consolidation and bibliography bytes and exact diffs are retained. No proof passage or executed program was removed.

## 2026-11-20T01:55:31.549024+00:00 — Conditional Cartier kernel-wall inertia promoted

Maximal kernel variation forces stable loss one, and any nonempty common Cartier wall supplies a full hyperplane radical. Wall nonemptiness and global generation remain unproved requirements; no unconditional monodromy degree added. The exact candidate remains unchanged. Status, completed-audit wording and an explicit common-incidence reference are the only canonical text changes. Prior shared-file bytes and exact diffs are retained; no proof or executed program was removed.

## 2026-11-20T02:42:48.656272+00:00 — Uniform odd full-inertia wall promoted

For every odd etale principal-cube pullback and every fixed odd principal-cube degree, the maximal common-rank wall is nonempty and supplies full hyperplane inertia. No global generation, connectedness, irreducibility or new exact full-image degree is claimed. The exact candidate and prior shared include file are retained with diffs. Only short proved statuses and completed audit metadata were changed in the canonical theorem. No previous canonical proof was modified and no mathematical experiment was rerun.
