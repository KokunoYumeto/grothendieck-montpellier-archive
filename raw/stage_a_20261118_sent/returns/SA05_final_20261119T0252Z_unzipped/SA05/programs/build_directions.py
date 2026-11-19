#!/usr/bin/env python3
"""Serialize the editorially ranked future tasks; do not develop their mathematics."""
from pathlib import Path
import json,re,datetime
B=Path(__file__).resolve().parents[1]
directions=[]
def d(title,interest,reach,items,claims,problems,establish,known,first,limit):
 directions.append(dict(rank=len(directions)+1,title=title,interest=interest,reach=reach,
  items=['SA05-'+str(x) for x in items],claims=['SA05-C'+str(x) for x in claims],
  problems=['MP-SA05-'+(str(x).zfill(2) if x<100 else str(x)) for x in problems],
  would_establish=establish,known=known,first_step=first,one_run_limit=limit))

d('A common convention for graded correspondences and exchange',5,5,[1005,1011,1012,1022,2006,2007,2018],[1001,1002,1003,1004,1005,1006,1007,1022,1023,1024,1025,2003,2004,2005,2006,2013],[1001,1002,1008,1009,2002,2005],
 'A single variance, degree, symmetry and gauge convention supporting composition, units, graphs and tensor products, with every exchange square stated.',
 'The ordinary even construction is established; the all-degree tensor formula was itself rejected in the manuscript. A Cartesian square alone does not imply the required exchange identity in an arbitrary gauged category. Hua’s checked theorem is ungraded and has explicit axioms.',
 'Tabulate the maps and degrees at11/002–012 and044–048, list the squares used by the associativity and graph proofs, and choose one odd-degree test object.',
 'A complete convention and finite axiom inventory is realistic. A general new base-change theorem is outside this task.')
d('A concordance of weight, level, coniveau and the two dimension filtrations',5,5,[5,8,38,40,54,3018,3025,3026],[6,9,50,53,3021,3022,3033,3034,3035,3036],[2,15,16,3006,3013,3021],
 'A definition and implication table showing which filtration is used on each leaf, how Tate twist acts, and what a realization theorem actually implies.',
 'Early D is Tate-stable; late type is bounded untwisted source dimension. Hodge and weight bounds do not by themselves identify geometric motivic level or coniveau. The2026 abelian statements affect specified subcases only.',
 'Place the generators at12/035–036 beside12/125, then compare the unit, the Tate line, elliptic H1 and a normal-crossing top class before mapping theorem dependencies.',
 'A reliable concordance and hypothesis graph can be completed in hours. Equality of the general conjectural filtrations cannot be inferred from it.')
d('Corrected global and local bounds for varying geometric coefficients',5,5,[62,3015,3016,3022,3024],[75,76,3015,3017,3028,3030,3032],[18,3005,3010],
 'An exact table of valid coarse bounds, disproved sharper bounds and the separate surviving coefficient-level questions.',
 'Legendre satisfies the relevant strict geometric coefficient hypothesis and gives the obstructing weight4 or weight0 terms. Constant coefficients, finite monodromy, boundary unipotence and arithmetic invariants require different statements.',
 'Write the local and global hypotheses side by side and preserve the documentary change from assertion at51 to question at108; then choose one corrected target with a specified monodromy condition.',
 'A short counterexample-and-correction companion is feasible. A new general geometric-level theorem requires additional input.')
d('The kernel of the realized diagonal algebra',5,4,[2010,2012,2014],[2007,2008,2009,2010,2011,2012,2013],[2003,2004],
 'The relation ideal of the diagonal diagram algebra in one fixed graded Poincaré algebra and number of factors.',
 'The audited P1 example disproves the unrestricted word “basis”; it does not classify the kernel. Hua’s multigraph multiplication rule does not assert faithfulness of every realization.',
 'Fix a coefficient field, a normalized top class and a model with nonzero odd cohomology, and specify the realization homomorphism before seeking relations.',
 'A small explicitly bounded case is realistic; arbitrary varieties and all factor counts are a separate research programme.')
d('Coherent integral lattices and rationalization',5,4,[3035,3036,3037,3038,3039,3063],[3041,3042,3043,3044,3045],[3016],
 'A conditional integral category with precise denominator control and separately proved Hom finiteness, kernels, cokernels, internal Hom and rational quotient properties.',
 'Arbitrary prime-by-prime lattices can yield a Hom subgroup of Q containing1/l for every prime. Ambient extension closure already fails for simple finite torsion examples. The rational motive category remains an assumed input.',
 'Define reference systems and their allowed equivalence relation, then test tensor, Hom, kernels and cokernels on rational lines, Z/l and mixed lattice systems.',
 'A rigorous conditional axiom package is plausible in one run. It would be our reconstruction, not a recovered theorem on the pages.')
d('Weight-one essential image, extension and purity: an exact case table',5,4,[3034,3042,3043,3044],[3040,3048,3049,3050,3051],[3015,3017,3018,3019],
 'A historically ordered account separating traits, low ramification, higher-dimensional nonextension, extension of morphisms and independence of a detecting prime.',
 'The Néron–Ogg–Shafarevich criterion, the extension theorem for already existing maps, finite-étale purity and Vasiu–Zink’s object counterexamples have different hypotheses. All-prime unramifiedness alone does not settle the unrestricted mixed-characteristic local-base question.',
 'Read the exact de Jong–Oort1997§6 source and available earlier purity references, then align each theorem with the source’s base, prime order and object-versus-morphism wording.',
 'A dependable history and hypothesis table is feasible. The broad one-prime criterion for arbitrary motives is not a few-hour target.')
d('The absolute unit and its finite-field comparison',5,4,[71,73,74,75,76],[88,89,90,91,92,93,94],[25,26,27],
 'A consistent small formal model of the proposed absolute cohomology, stating exactly which continuity, odd-unit and duality axioms can coexist.',
 'The written degree-multiplication restrictions and H1(Fq,Q)=Q have nonzero direct limit. Ordinary profinite rational cohomology, Weil-group cohomology and Weil-étale motivic cohomology are different inputs. The odd identification also needs a normalization.',
 'Extract only the unit calculations and transition maps from60–71 and the reused69 continuation, then compare them with the precisely checked finite-field Weil-étale splitting.',
 'A complete incompatibility/dependency table and a bounded replacement model are realistic. The full absolute motivic heart is not constructed by that comparison.')
d('Sha, Brauer and constant Jacobians with degree conventions fixed',5,4,[79,80,81,82,83,84,85,86,87],[98,99,100,101,102,103,104,105,106,107,108,109,110,111],[28,29,30,31],
 'A single exact-sequence companion distinguishing rational points, torsor groups, Tate modules, finite errors and Brauer residues over curves.',
 'The inverse-Kummer constant-Jacobian counterexample contradicts literal H2-vanishing without assuming Sha finiteness. Removing r≥1 closed points gives Brauer corank r−1 through normalized local invariants. Singular proper schemes need not satisfy the smooth high-degree weight vanishing.',
 'Draw the Kummer and localization sequences with coefficients and bases fixed, mark every inverse-limit hypothesis, and separate the global-function-field rank equivalence from full BSD.',
 'A complete corrected curve case and comparison table is realistic. The general finiteness conjectures remain outside this task.')
d('Analytic Galois Lie algebras versus algebraic monodromy',5,4,[67,68,69,70],[83,84,85,86,87],[24],
 'A precise reconstruction target distinguishing analytic invariants, associative envelopes, Zariski groups and a proposed motivic Lie object.',
 'The double-centralizer argument recovers an algebra under semisimplicity; it does not select individual cycles or recover the group. A procyclic finite-field image can have analytic dimension1 and algebraic torus dimension2.',
 'State the four objects and their comparison maps for the checked elliptic Frobenius example, then specify which one the l-independent proposal is intended to realize.',
 'A clean conditional theorem and counterexample boundary can be written in hours. General l-independence remains a larger problem.')
d('Primitive Tate strings and the two associated graded rings',4,5,[40,41,42,43],[53,54,55,56,57,58,59],[16],
 'A coherent algebraic presentation preserving the unit, negative Tate powers and the distinction between weight grading and early D-grading.',
 'The literal alpha=0 subtraction and polynomial wording after inversion fail elementary tests. Early D is unchanged by Tate twist, whereas weight moves by2.',
 'List simple-object Tate orbits under the stated semisimplicity assumptions, choose the primitive boundary convention, and test multiplication before identifying either associated graded ring.',
 'A conditional normal-form account is highly feasible; it must not silently resolve the ink or claim the general category exists.')
d('A Karoubi-envelope companion with a separate geometric application test',4,5,[3045,3046,3047,3048,3049,3050,3051,3052,3053,3055],[3052,3053,3054,3055,3056,3057,3058,3059,3060,3061],[3020],
 'A short noncircular proof of the abstract envelope, corner morphisms, kernels/cokernels, finite length, tensor extension and characteristic-zero Schur operations.',
 'The formal results were independently checked against Demazure and Jannsen. Jannsen’s numerical-motive theorem is distinct from identifying a homological category or obtaining all standard conjectures.',
 'Begin with the manuscript’s quotient of intertwiners and prove its equivalence to the corner description, recording the projection typing alarm before choosing modern notation.',
 'A complete expository companion is highly feasible. The concluding geometric application must retain its exact hypotheses.')
d('Integral quadric normalizations and degeneration',4,5,[2036,2042,2046,2050,2052,2053],[2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037],[2008,2009,2010,2011,2012,2013,2014],
 'One dimension-indexed table of rulings, restriction, Gysin, primitive generators, local groups and specialization.',
 'The integral ruling basis differs from the sum/difference sublattice by index2. Finite2-primary coefficients can have an adjacent group. The monodromy claim requires ordinary smoothing or regular total space; square base change removes the naive conclusion.',
 'Fix integral ruling classes, coefficient rings and relative dimension, then place all source formulas in that convention and list the remaining scan signs.',
 'A complete corrected classical table is feasible. This is a normalization and exposition task, not an open calculation of quadric cohomology.')
d('The nested-torus assertion and its maximal-torus correction',4,5,[2071,2081],[2047,2048,2049],[2017],
 'An independently reviewable correction note with explicit lattice data and the exact valid maximal-torus version.',
 'The broad wording fails for the checked nested tori in SL4. Conjugacy in the centralizer proves the maximal-torus statement. The checked re-edition retains the broad text, but the original printing has not been collated.',
 'Inspect the original1970 page against the re-edited witness, then present the counterexample and corrected hypotheses without depending on an attribution of the textual defect.',
 'The mathematical note is highly feasible; edition history depends on obtaining the original page. No contact with editors is part of this proposed task.')
d('The determinant series and endomorphism Grothendieck ring',4,5,[93,94,95,96,97],[118,119,120,121,122,123,124,125],[33],
 'A companion distinguishing finite-dimensional field objects from projective modules, zero eigenvalues from automorphisms, and virtual semisimplification from Jordan data.',
 'The zero-operator class lies in the determinant kernel; over a field the reduced description is exact. Reciprocal factors, the lambda sign and the weight-shift Euler parity have separate corrections. Equal power traces do not recover nilpotent Jordan structure.',
 'Specify the exact category over a field first, prove its factorization map and kernel, then add only the ring generalization supported by a newly opened exact source.',
 'The field companion is highly feasible. The unverified Almkvist bibliographic lead must be opened before relying on the full ring theorem.')
d('Positive cones and the precise semisimplicity mechanism',4,4,[88,89,90,91,92],[112,113,114,115,116,117],[32],
 'A conditional cone formalism with correct Tate targets, parity, real topology and a clearly stated nondegeneracy-to-splitting argument.',
 'The manuscript already assumes a semisimple setting. Weight zero alone does not make an object trivial, and invariance alone does not make a form positive. The Hodge and abelian standard-conjecture comparisons have stated scopes.',
 'Separate existence of positive forms from their closure properties, realify each form space, and test the tensor and orthogonal-complement axioms on the unit and h1 of an elliptic curve.',
 'A precise conditional reconstruction is feasible. It does not prove the general positivity conjecture.')
d('Fibre-functor torsors, neutrality and arithmetic splitting',4,4,[9,10,11,12,13,14,15,16,17,18,22],[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[5,6,7,8,9],
 'An exact dependency chart separating a tensor category, a fibre functor, its torsor, the Artin comparison and a chosen arithmetic splitting.',
 'Neutral reconstruction, torsor representability and finite-generator criteria are established with Tannakian hypotheses. The supersingular quaternion obstruction and a nonsplit torus-lattice sequence show why stronger conclusions need extra assumptions.',
 'Normalize the variance of every fibre functor and list what each assertion needs: characteristic, connectedness, finite type, a chosen point or a splitting.',
 'A bounded theorem-by-theorem companion is feasible. General period genericity and existence of the full motive category remain separate.')
d('The general-base programme and modern six operations',4,4,[26,27,28,29,30,31,32,33],[35,36,37,38,39,40,41,42,43,44],[11,12],
 'A comparison of each proposed abelian general-base axiom with an exact modern triangulated or realization-level theorem.',
 'Six operations, continuity and relative motivic Galois constructions have precise modern versions. They do not automatically construct the manuscript’s abelian heart, finite-dimensional absolute theory or all proposed comparison functors.',
 'Make an axiom table with base, coefficients, variance and target category, then align the checked Cisinski–Déglise and Ayoub statements one at a time.',
 'A complete hypothesis map is realistic. Existence of a general motivic t-structure is not a short residual exercise.')
d('Restricted birational reconstruction and the scissors quotient',4,3,[49,50,51,52],[65,66,67,68,69,70,71],[20,21],
 'A well-posed restricted functor or field-reconstruction statement that survives the section/retraction and rational-homological tests.',
 'A nondominant section can compose with a projection to the identity. Rational realization can erase the Enriques obstruction. Brackets in the source may mean a purely transcendental field extension, so the polynomial-units argument is conditional. Nonruledness alone does not prove a graded scissors class is nonzero.',
 'Fix the allowed maps and the exact quotient/equivalence relation, adjudicate the bracket notation from scans when available, then choose one restricted reconstruction target.',
 'A sharp formulation and boundary examples are feasible. A general birational or anabelian reconstruction theorem is not promised.')
d('Finite-set reconstruction versus Frobenius and special power systems',4,4,[1025,1026,1027,1033],[1031,1032,1033,1034,1035],[1011,1012,1013,1014],
 'A three-way theorem comparison: finite-projective Frobenius data, special commutative ungraded systems with multiplicative gauges, and the wider unfinished graded theory.',
 'Kock’s exact Frobenius result and Hua2026 Theorem1.2 settle restricted statements. The partition-system example disproves unrestricted evaluation at a point. Reported Lean verification was not executed in this run.',
 'Collate the source’s specialness, empty-set and gauge hypotheses against the checked version, then formulate the residual graded or degenerate question without importing omitted axioms.',
 'A precise comparison is feasible; a classification of the wider systems is not already supplied by the cited restricted theorem.')
d('Curve reduction with the corrected late type target',4,3,[3019,3026,3027],[3023,3024,3025,3035,3036,3037,3038],[3003,3007,3013,3014],
 'A complete conditional proof audit of geometric-type preservation, or an explicit minimal missing lemma.',
 'The late minus-one target fails for the torus embedding example. The compact-support two-row and proper three-row Leray arguments differ; the formal middle-row E3=E∞ statement does not itself identify geometric type.',
 'Rewrite135–137 as functors and filtrations, marking each use of subquotients, direct summands, semisimplicity and a curve reduction.',
 'A complete audit is possible. An unconditional new closure theorem may not follow from the available inputs.')
d('The relative L-function programme with generic-fibre equivalence fixed',4,3,[97,98,99],[124,125,126,127,128],[34],
 'A precise candidate invariant modulo proper-closed-base contributions, with the actual smoothness, properness and weight cutoffs stated.',
 'Trace formulas and rationality give exact related results, while the source’s proposed quotient and final adjective list remain unresolved. The highest-weight cutoff needs the coefficient weight shift.',
 'Choose a base and coefficient category, define the subgroup of boundary contributions, and test generic-fibre invariance on a single fibration with a controlled bad fibre.',
 'A meaningful definition and finite set of tests are feasible. No exact general published invariant with all source rules was identified in the bounded search.')
d('A versioned audit of the2026 abelian implications',4,4,[56,3025,3054],[3004,3022,3024,3056],[3021],
 'A version and hypothesis map from each announced CM/abelian theorem to the manuscript’s relevant subcases.',
 'The6October CM-Hodge preprint and9November Milne report were opened and their exact statements checked. Their long new proofs were not independently audited here. Rational CM Hodge, finite-field abelian Tate and abelian standard-conjecture statements must remain distinct from arbitrary varieties and integral cycles.',
 'Obtain the original version history and compare revisions, then open the earlier implication papers and corrigenda before choosing one bounded implication chain to audit.',
 'A source/version map is realistic. A full proof review of the53-page new preprint is a separate longer task.')
d('The exact total-space integrality question in the cancelled EGA draft',4,3,[1053,1054,1055],[1062,1063,1064,1065,1066,1067,1090],[1020,1021],
 'An exact theorem comparison specifying whether a published result answers the intended total-space assertion under the missing base and flatness hypotheses.',
 'The literal unreduced formulation is false. Murayama’s checked corollary concerns all fibres, while its warning excludes a naive domain-ascent shortcut. A fibrewise theorem is not automatically the desired total-space theorem.',
 'Obtain final EGAIV2§7.9 and its localization references, then state and test the bridge from fibrewise punctual integrality to the intended total-space conclusion.',
 'A source-and-hypothesis decision is feasible. The dossier does not claim the intended question is still open in the literature.')
d('The separating-family and generic-freeness draft',4,4,[1052],[1060,1061],[1019],
 'The correct module, localization and missing hypotheses of the reused algebra lemma, compared with final EGAIV3.',
 'The attached witnesses share the malformed B_h/A_h expression but assign different scan labels. EGAIV3 11.9.7–11.9.10 and the separate11.9.8 question provide bounded comparisons, not permission to replace ink.',
 'Recover the preceding proposition and inspect the source scan, then compare the support-induction argument with the final printed proof.',
 'An exact editorial reconstruction is highly feasible once those witnesses are available; no new generic-freeness theorem is required.')
d('Nilpotent density and its inherited hypothesis',4,4,[1058],[1077,1089],[1023],
 'A corrected ordinary lifting lemma and a separate assessment of the universal-relative variant.',
 'The square-zero example disproves the literal ordinary assertion. SGA3II IX4.2 supplies a sufficient locally-free-layer condition. The example does not settle the universally dense relative formulation.',
 'Read the preceding manuscript context for that layer condition and then state the relative version independently, with its base-change quantifier.',
 'A precise editorial correction and one bounded relative test are feasible; the two assertions must not be merged.')
d('Delzant’s two questions and the exact comparison maps',3,5,[2088,2089,2093,2094],[2056,2057,2058,2059,2060,2061,2062,2063,2064,2065],[2019,2020],
 'A historical companion explaining the passage from the rank-zero ideal in GW to the fundamental ideal in W and the actual degree-two symbol comparison.',
 'Milnor and Merkurjev settle the relevant questions, but merely naming the later theorem omits a necessary ideal identification. The attached offprint was read; its strict external bibliography status remains unverified. The exact Springer1959 normalization still needs direct source inspection.',
 'Obtain the exact Springer passage and original offprint record, then present the comparison square and separate first circulation from publication.',
 'A concise companion is feasible. It is documentary completion, not a new open norm-residue problem.')
d('Rational attainment in the GIT exercise',3,5,[1039,1040],[1042,1043,1044],[1015,1016],
 'A self-contained proof with all nonemptiness, rational-weight and norm hypotheses explicit.',
 'Finite rational polyhedral faces give the relevant bounded optimization argument; a stronger instability theorem is not a substitute for proving this exact exercise. Empty direction spaces and irrational norms require separate treatment.',
 'State the direction space and norm precisely, reduce to faces, and list the assumptions under which a rational maximizing ray exists.',
 'A complete short proof is realistic. It should be presented as completion of a classical exercise.')
d('GIT physical pagination and the determinant-cone continuation',3,4,[1050,2021,2022,2024,2025],[1058,1059,2016,2017,2020,2021],[1018,2006],
 'A page-order concordance and exact coordinate collation of the already established configuration criterion.',
 'Both attached continuation pieces were read. Missing3.5/3.16 and incomplete OCR leave documentary gaps; they do not make the classical criterion open. The separating functional must be nonzero, and stability differs from semistability.',
 'Match opening and closing sentences to a specific edition or typescript state and retrieve the missing physical pages before filling any local formula.',
 'A concordance is feasible; full collation depends on the missing pages. Diagonal partitions and GIT R-partitions stay separate.')
d('The reflection typescript: faulty equality, valid corollary and provenance',3,4,[2113,2114],[2071,2072,2073,2074,2075,2076,2077,2078,2079],[2024],
 'A correction companion distinguishing the chamber complement, false dual-angle equality and true nonnegative-angle corollary.',
 'The essential A3 calculation refutes the equality; inverse-Gram positivity supplies the corollary. The affine local-finiteness proof can be completed under properness. Exact identification of numbered typescript383 is still unverified.',
 'Collate III-2 andIII-5 against the original scans and a candidate edition, then write the corrected proof without attributing the reused typescript to Grothendieck.',
 'The bounded mathematics is feasible; provenance depends on finding the actual numbered document.')
d('The two reported Deligne manuscripts and their chronology',3,3,[2111,2112],[2069,2070],[2022,2023],
 'A dated source chain for the perfect-complex lambda report and the separate conditional Leray/Lefschetz report.',
 'The lambda report already announces a solution within its written scope. The Leray report needs a relative operator. Modern theorem statements do not identify the manuscript Grothendieck had seen or its circulation date.',
 'Compare B12/121 and123 with SGA6 editorial material and Deligne1968, adding contemporary correspondence only if subsequently supplied.',
 'A documentary concordance may be completed in hours; the undated reports must not inherit the secretary letter’s27March1968 date.')
d('The selected-map and nonadditive variants as exact axiom questions',3,3,[1017,1018,1023],[1010,1011,1012,1029],[1006,1007,1010],
 'A minimal statement of the allowed maps and operations that the unfinished variants retain.',
 'The source leaves these variants open. The ordinary correspondence theory and special finite-set theorem do not settle omitted variance, additivity or base-change requirements.',
 'Extract the surviving operations and every explicit cancellation, then formulate one small category in which those axioms can be tested.',
 'An exact formulation is plausible; a complete new general theory is not a one-run promise.')
d('The English cycle-class sheet and its conventions',3,3,[1059],[1078,1079,1080],[1024],
 'A secure identification of the sheet and a bounded commentary on its trace, cycle and twist conventions.',
 'The familiar cycle-class construction does not identify authorship or justify using Poincaré duality on arbitrary singular cycles. The preceding conventions and exact document remain missing.',
 'Search by opening and closing wording and recover the preceding page before comparing the displayed trace argument with an exact published source.',
 'A source-identification and scope decision is feasible if the witness is found; no attribution should be inferred merely from its archival location.')
d('The pure-category presentation and its omitted compatibilities',3,3,[1,4,20],[1,5,27],[1,3],
 'A finite list of the relations needed to turn the proposed generators, Künneth data and inverted Tate projector into a precise universal construction.',
 'Later correspondence and universal constructions impose cycle maps and composition compatibility explicitly. Numerical semisimplicity and faithful classical realizations are separate assertions.',
 'Write the proposed presentation in generators and relations, mark each relation actually on the pages, and compare a single chosen modern realization category.',
 'A presentation audit is realistic. It should not be advertised as construction of all conjectural pure motives.')
d('Two decisive readings before further local arguments',4,1,[3020,3023],[3025,3029],[3007,3009],
 'A scan-based decision between sans/sous and s’identifie/intervient, which changes the strength of two assertions.',
 'The diplomatic witnesses disagree. The double-blowup counterexample refutes whole-term identification, not the weaker assertion that a term contributes to a spectral sequence. Mathematical plausibility cannot settle the glyphs.',
 'Once original scans114 and120 are available, inspect both exact phrases beside the two transcriptions and record visual evidence before editorial interpretation.',
 'Reach is1/5 with the present attachments and5/5 after the scans are supplied. This direction is ranked last operationally because its first required evidence is absent.')

aliases=json.loads((B/'SA05_aliases.json').read_text())
all_alias={**aliases['items'],**aliases['claims'],**aliases['problems']}
def canon(x):
 while x in all_alias:x=all_alias[x]
 return x
for x in directions:
 for f in ['items','claims','problems']:x[f]=list(dict.fromkeys(canon(z) for z in x[f]))
ids={k:{x['id'] for x in json.loads((B/('SA05_'+k+'.json')).read_text())} for k in ['items','claims','problems']}
for x in directions:
 for k in ids:
  bad=set(x[k])-ids[k]
  if bad:raise ValueError((x['title'],k,sorted(bad)))
out=['# SA05 — ranked directions for later work','',
 'These are proposed tasks arising from the completed consolidation, dated **19 November 2026**. None is developed here. The counterexamples, recomputations and proof checks in the dossier belong to the verification of existing assertions, not execution of these future tasks. Each task below names its items, claims and problem records; the latter provide exact source and literature references.','',
 'Interest and reach use separate ordinal scores from1 to5:5 is highest. The overall order weighs centrality to the manuscript, mathematical value and the likelihood of a useful result in a run of a few hours. It is an editorial ranking, not a measured score. A source-access dependency can lower immediate reach even when a reading is mathematically decisive.','',
 '| Rank | Direction | Interest | Reach in a few hours |','|---:|---|:---:|:---:|']
for x in directions:out.append(f"| {x['rank']} | {x['title']} | {x['interest']}/5 | {x['reach']}/5 |")
for x in directions:
 out+=['',f"## {x['rank']}. {x['title']}",'',
  '**Origin.** Items '+', '.join(x['items'])+'; claims '+', '.join(x['claims'])+'; problems '+', '.join(x['problems'])+'.','',
  '**Would establish.** '+x['would_establish'],'','**Known input and boundary.** '+x['known'],'',
  '**First concrete step.** '+x['first_step'],'','**One-run outcome.** '+x['one_run_limit']]
out+=['','## Separate documentary and prior-project leads','',
 'Unavailable cote16/47/54 and other archive targets are listed in `SA05_unavailable_archive_leads.tsv`. Their first step is retrieval of the exact witness. They are not counted as checked two-ended links. The WG2, S6, La Longue Marche, Dérivateurs and other run associations made by the earlier notes remain in `SA05_project_leads.tsv`, with their stated status. None has been promoted to a new theorem or used to dictate the ranking above.','',
 'The original scope-specific direction lists remain in `work/cote11a/`, `work/cote11b/` and `work/cote12c/` as provenance. The present list consolidates their overlaps and adds the middle-cote12 directions; canonical IDs supersede temporary aliases in those audit copies.','']
(B/'SA05_directions.md').write_text('\n'.join(out))
(B/'SA05_directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'directions':len(directions),'all_live_ids_valid':True,'future_tasks_executed':0}
(B/'programs/outputs/build_directions.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
