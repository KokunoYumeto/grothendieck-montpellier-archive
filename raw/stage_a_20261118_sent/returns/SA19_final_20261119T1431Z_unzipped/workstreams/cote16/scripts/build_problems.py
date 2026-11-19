"""Problem index, written from questions/unfinished steps and labelled editorial leads."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[]
def p(n,title,scans,claims,as_he,plausible,state,why,worth,refs):
    rows.append(dict(id=f'MP-SA19-{n}',title=title,occurrences=[dict(cote=16,scans=scans,claims=[f'CL-SA19-{x}' for x in claims])],as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open=why,worth=worth,refs=refs))
K='Kleiman1968';S='Stacks2026'
p(40,'Algebraic inverse Lefschetz operators',[9,10,33,42,44,45,46,48,49,50,51,53,55],[204,205,239,240,247,253],
 'The correspondence ring should contain inverses of the complementary-degree Lefschetz isomorphisms, equivalently normalized lowering and the primitive projectors; the letter calls this C.',
 'For every smooth projective X over a field with a specified Weil cohomology, each inverse to L^(n−i) is induced by a rational algebraic correspondence: modern standard conjecture B. Hard Lefschetz and algebraicity are separate.',
 'Kleiman1968 Proposition2.9 gives equivalences; Theorem2.13 gives product/hyperplane reductions. Deligne1980 Theorem4.1.1 proves rational ell-adic hard Lefschetz, not B. Ancona et al.2025 prove specified LSV/Lagrangian cases, not the universal claim.',
 'The obstruction is existence of algebraic correspondences. No source says the general conjecture was dropped; it remains an active problem.',
 'Worth a focused historical/formal reconstruction, while a general proof is far beyond a short research run.', [K,'Deligne1980','AnconaEtAl2025'])
p(41,'Definition and normalization of the universal integral model',[10,14,15,16],[207,208,209,210,279],
 'The definition numbered6.5 is unfinished; the exterior model is said to work over Z and to give a universal algebra.',
 'A valid normalized integral string algebra is ∏ Mat_(n−i+1)(Z); its relation to the literal ordinary exterior-contraction order must be specified rather than assumed.',
 'The factorial and contraction counterchecks refute the literal model. The earlier notes’ replacement is proved in proof_checks§3 with exact certificates. Kleiman1968 supplies the formal rational/cohomological framework, not an identification of these integral orders.',
 'The pages leave the normalization incomplete and contain incompatible claims; no documentary reason for abandonment is known.',
 'Worth a bounded editorial task to compare lattices and operator conventions, with no claim that the repaired model is his unwritten definition.', [K])
p(42,'Uniqueness when only the raising operator is specified',[16,17],[210,211,212],
 'Could there be at most one map Φ→E taking the universal L to L without a prescribed grading? He answers Non on scan17.',
 'Uniqueness can hold with the appropriate prescribed graded projectors; it is false without them, already for n=1.',
 'Source own negative answer, independently certified by Ad(1+tL) on Mat₂(Z)×Z. Kleiman’s graded formalism is consistent with the qualified uniqueness.',
 'Resolved negatively on the same page, not a surviving open conjecture.',
 'Worth recording the short counterexample in a companion, not launching a separate attempt to prove the rejected claim.', [K])
p(43,'Recovering degree and primitive projectors inside a correspondence ring',[5,6,7,8,11,12,17,51,53,55],[202,203,206,212,253,254,255,280],
 'Give an existence/uniqueness induction recovering π_i and the elementary primitive projectors from homogeneous inverse maps.',
 'Under finite grading and two-sided inverse identities, use two-sided truncated blocks T_kL^(n−k)T_k and T_kw_kT_k, followed by supported primitive differences.',
 'Kleiman1968 Lemma3.15 and Proposition2.9 give the formal theorem. This run proves the explicit repaired induction and refutes the one-sided cutoff on H*(P²).',
 'The written proof has an off-by-one terminal step and a missing target cutoff. Neither is a reason to regard the theorem itself as false.',
 'Worth immediate editorial repair with the source formulas and reconstructed proof displayed separately.', [K])
p(44,'Characterizing Lefschetz elements by top powers',[18,20,22],[213,214,215],
 'Can nonvanishing or being a basis of E^(2n) for L^n characterize Lefschetz elements?',
 'Such a criterion needs additional control of all middle-degree maps; it fails even in the displayed six-dimensional commutative graded algebra.',
 'The manuscript’s own presentation has ranks1,2,2,1; L is Lefschetz while L′ has rank-one middle map and the same nonzero cube. Exact matrices certify every relation.',
 'The proposed converse is rejected on scan22 by his own example.',
 'Worth retaining as a clean warning against endpoint-only tests; additional classification is a new task.', [K])
p(45,'Rational dependence of lowering on the raising operator',[20,22],[214],
 'The scratch formula is Λ=Ω(L)Δ(L)^(−N), with Ω,Δ,N undefined.',
 'On a specified finite free graded module, inverse matrices depend regularly after inverting determinants of all relevant Lefschetz blocks; a universal expression needs an explicit parameter algebra and normalization.',
 'Formal inverse/characteristic-polynomial methods appear in Kleiman1968. No exact theorem matching the undefined scratch expression was identified in title, formula or backward-reference searches.',
 'The source is unfinished; no evidence establishes why it was not pursued.',
 'Worth a small reconstruction only after the parameter space and coefficient ring have been fixed from the scans.', [K])
p(46,'Infinite orbits in the four-form Hodge-algebra model',[27,29],[226,227,228],
 'The orbits of ξ and φ̌ under u should be infinite when dimV≥4, or perhaps6.',
 'For the explicitly reconstructed operator U=(Λ²φ♯)Q♭, dimension6 suffices with Q nondegenerate, Q(ξ,ξ)=1 and φ nondegenerate; the sharp dimension4 threshold and the literal tensor convention remain separate.',
 'The earlier-run rational six-dimensional example is independently rechecked in the full15×15 space. Exact literature searches found no matched published resolution. Positivity/geometric realization are not asserted.',
 'The author explicitly doubts the threshold and leaves u’s tensor normalization compressed; those are genuine limits on identification.',
 'Worth a short convention-and-threshold task after an ink check; the existing dimension6 certificate prevents needless rediscovery.', [K])
p(47,'Unbounded cyclic spans of those orbits',[29],[229],
 'The orbit spans should have unbounded dimension as dimV grows.',
 'For the earlier normalized U, the proposed family has cyclic span dimension at least m in dimV=4m, with a normalized nondegenerate four-form model.',
 'The supplied earlier-run family is checked by a general Vandermonde/open-condition argument and exact m=2,3,4 cases. No exact publication of the family was identified.',
 'No source records why the manuscript claim was left unproved; the normalization remains the decisive interpretation issue.',
 'Worth including the already available proof under its explicit convention, with further geometric constraints reserved for another task.', [K])
p(48,'Associativity and norm constraints in Hodge-algebra data',[25,27,29],[223,224,225,226,227],
 'He writes a boxed associativity condition, a four-form reformulation, an isotropic-line example and the claim that a suitable norm-one ξ yields any φ up to scalar.',
 'Keep associativity separate from nondegeneracy. For the final norm-one choice require the inverse image of φ to have nonzero norm in the appropriate square class.',
 'Direct algebra verifies the associativity criterion, Poincaré/Lefschetz conditions and isotropic example. The norm-one assertion is not valid over an arbitrary field without qualifications. No exact later classification was identified.',
 'The norm qualification is absent; the parameter-space classification is an earlier-run research suggestion, not a stated theorem of his.',
 'Worth a narrowly labelled editorial clarification; moduli or geometric realization should be a separate research project.', [K])
p(49,'Discriminant pairing versus local étale duality',[19,23],[216,217,218,222],
 'The notes ask whether exceptional-lattice self-duality equals the quotient pairing coming from local cohomological duality; his published continuation explicitly leaves this verification undone.',
 'For the precise complete normal local surface setup, identify NS(U)_n and Pic(U)^0[n] as exact annihilators and compare the quotient pairing with xᵀQ⁻¹y, including twists and sign conventions.',
 'BrauerIII§8.4pp148–151 sets up the problem; Remark8.5p151 admits the missing check. Suzuki2024 Proposition11.10 gives an explicit analogous intersection/duality compatibility in a mixed-characteristic p-primary setting; its hypotheses are not the same as the original equal-characteristic char0 statement.',
 'The published text identifies the check and says it was not done, while expecting no difficulty. This documents a historical proof gap, not by itself a presently open theorem.',
 'Worth a focused comparison of the exact pairings and later proofs; its statement is concrete and directly connected to local Picard/Brauer theory.', ['Grothendieck1968BrauerIII','Mumford1961','Suzuki2024'])
p(50,'Characteristic and residue-field extensions of local Picard–Brauer duality',[19,23],[216,218,222],
 'The published continuation says characteristic0 enters through local duality, expects removal of that restriction, and asks about non-algebraically-closed residue fields such as finite fields.',
 'Separate prime-to-characteristic étale duality from p-primary duality, and retain complete normal two-dimensional local hypotheses; finite/perfect residue fields require Galois or algebraic-group structure.',
 'BrauerIII Remark8.5 states the old purity obstacle. Suzuki2024 develops mixed-characteristic perfect-residue-field Picard–Brauer duality, Theorem1.6 and §11, building on Saito1986/1987. Exact comparison with the old pairings is a further task.',
 'The reason given in1968 is missing cohomological purity in regular dimension2; the modern arithmetic setting has additional p-primary structures.',
 'Worth a literature-matching task, not a blanket claim that the old statement is either wholly open or wholly solved.', ['Grothendieck1968BrauerIII','Suzuki2024'])
p(51,'Hyperplane operator formulary and its boundaries',[33,34,36,38,40,42],[233,234,235,236,237,238,239],
 'Derive the restriction/Gysin/primitive and lowering formulas needed to transfer algebraicity along a smooth hyperplane.',
 'Use finite Lefschetz strings with the extra primitive middle summand on Y; all formulas must respect endpoint supports and the strict inequality in projector transfer.',
 'Kleiman1968Proposition2.12 and Theorem2.13 establish the formal reductions. This run checks all displayed compressed identities and demonstrates the false non-strict boundary extension.',
 'The pages revise symbols and endpoints repeatedly; this is a draft proof problem, not an unresolved geometric theorem once hypotheses are fixed.',
 'Worth a companion formulary with explicit domains and endpoint projectors.', [K])
p(52,'Strong from weak Lefschetz through product-cycle conditions',[42,45,46],[239,240],
 'He proposes equivalent conditions using B(Y) together with critical algebraic-cycle Lefschetz conditions on X×X or X×Y, and then flags.',
 'The product and universal quantifiers must be retained: A(k) over all varieties is equivalent to B(k), whereas A(X) for one variety does not imply B(X) by this argument.',
 'Kleiman1968Theorem2.13 and3.16 are the exact developed results. No missing inverse cycle is produced without the product hypothesis.',
 'The formal reduction was developed; the cycle existence input remains conjectural generally.',
 'Worth a precise dependency diagram in the future companion, with no new proof program launched here.', [K])
p(53,'The A′ and A″ critical weak variants',[50],[251],
 'He asserts that two critical weak lifting conditions on successive products imply the full Lefschetz cycle relation.',
 'A consistent cohomological-degree convention should recover a theorem of the product/hyperplane type; the current H^i versus2i and j/i expressions cannot all be used literally.',
 'Kleiman1968Theorem2.13 is the precise nearby theorem. This run does not claim that it decides the ambiguous draft letters or inequalities.',
 'The difficulty here is identifying a coherent source statement, rather than a new obstacle in the published formal proof.',
 'Worth an ink-first transcription task followed by exact matching to the published theorem.', [K])
p(54,'Independence of the chosen cohomology theory',[44,46],[243],
 'He retracts the hasty positive-characteristic assertion that the stated cycle conditions are independent of ell or the Weil cohomology.',
 'Under numerical=homological equivalence and the relevant standard/positivity hypotheses, the correspondence category and conditions admit the desired independence; unconditional universality is stronger.',
 'Kleiman1968Theorem3.16 gives conditional independence. Jannsen1992 proves semisimplicity for numerical motives and a conditional nilpotent kernel, not the full homological conclusion.',
 'The letter itself identifies lack of a proof in characteristicp; no later numerical theorem removes every condition.',
 'Worth a historical hypothesis audit; a general independence proof is not a short task.', [K,'Jannsen1992'])
p(55,'Polarization independence in positive characteristic',[44,45],[241,243],
 'If Coates cannot prove independence of A and C from ξ in characteristicp, the possible dependence should be pointed out.',
 'Modern inverse-Lefschetz B is polarization independent under its formal hypotheses; an independently stated cycle condition A must be matched to its exact definition and any index assumption.',
 'Kleiman1968Proposition2.10 proves the relevant inverse-Lefschetz polarization independence. The draft’s undefined B/D letters are not translated by letter alone.',
 'This is a specific doubt in the letter, later resolved in the formal B setting; the page does not supply definitions for every letter.',
 'Worth a small exact-notation concordance, not a universal equivalence assertion.', [K])
p(56,'Rational characteristic polynomials in positive characteristic',[48,49],[247,248,284],
 'He hopes the characteristic0 simplification from an algebraic isomorphism to its inverse could also be obtained in arbitrary characteristic.',
 'Require rational characteristic polynomials of the relevant algebraic endomorphisms, or a precise theorem guaranteeing them in the chosen cohomology; then Cayley–Hamilton gives the inverse.',
 'Kleiman1968Propositions2.7 and2.9 provide the conditional result. Katz–Messing1974Theorem2(1)–(2),pp76–77, directly read with proof, gives finite-field characteristic-polynomial integrality for integral correspondences and rational Künneth projectors. It does not establish all-field homological= numerical equivalence.',
 'The draft correctly isolates the coefficient issue; later finite-field results cover a specified setting.',
 'Worth matching the exact finite-field theorem and its descent hypotheses before broadening the letter’s assertion.', [K,'KatzMessing1974'])
p(57,'Positivity and semisimple correspondence algebras',[49],[249],
 'He asks that C(X) plus the index relation on X×X imply semisimplicity of correspondence classes.',
 'For the algebraic adjoint involution and a positive rational trace form, prove finite-dimensionality and kill the radical by its trace norm.',
 'Kleiman1968Theorem3.12/Lemma3.13 establish it; this run independently supplies the radical and rational Gram-matrix arguments. Jannsen1992 concerns numerical motives separately.',
 'The requested formal result was developed. The geometric positivity assumptions remain nontrivial in positive characteristic.',
 'Worth a concise proof in the companion with the conditional assumptions visible.', [K,'Jannsen1992'])
p(58,'Algebraic left and right inverses',[49],[248,250],
 'He expects an algebraic monomorphism to have an algebraic left inverse, and dually a right inverse for an epimorphism, apparently needing the index relation.',
 'Assume algebraic adjoints and positivity in the correspondence setting containing both source and target; then (u*u)^−1u* supplies the left inverse.',
 'Kleiman1968Theorem3.14 develops the result. Semisimplicity of a single unrelated endomorphism algebra alone does not control all off-diagonal correspondences.',
 'The source already distinguishes isomorphisms from injections; the latter need stronger ambient data.',
 'Worth a categorical hypothesis clarification and the explicit splitting formula.', [K])
p(59,'Deriving the Weil bounds from cycle conjectures',[50],[252],
 'He requests an extra paragraph deducing the Weil conjectures from draft C and A.',
 'State the precise positivity-bearing package, such as algebraic Lefschetz operators plus I(X×X), rather than relying on undefined letters.',
 'Kleiman1968Theorem4.7 develops the conditional argument. Deligne’s later proof of Weil bounds does not prove the whole standard-conjecture package.',
 'The program was developed conditionally and later the bounds were proved by a different method; no source supports identifying the two achievements.',
 'Worth a clear logical-history paragraph; no new general Weil proof is needed.', [K,'Deligne1980'])
p(60,'One-cycles on threefolds and the dimension-five critical case',[46,47],[244,240,282,283],
 'He says the main difficulty already arises for1-cycles on threefolds, and the first critical A case in characteristic0 is dimension5, notably X×Y for a threefold and hyperplane surface.',
 'Retain rational coefficients and the distinction between cycle-Lefschetz A and inverse-correspondence B; the product condition of dimension5 would provide B for the threefold.',
 'Kleiman1968Theorem2.13 gives this implication; low-degree algebraicity via Picard/Albanese is in2A9–2A10. Modern special cases do not settle all smooth projective threefolds.',
 'The manuscript identifies the first nontrivial codimension beyond divisors; the general algebraic-cycle existence remains difficult.',
 'Worth a targeted known-case inventory, not a claim that low-dimensional hard Lefschetz settles the algebraic inverse.', [K,'AnconaEtAl2025'])
p(61,'A singular-variety reformulation after the hypersurface obstruction',[47],[246],
 'After Serre’s simply-connectedness objection to the smooth-hypersurface reduction, he says singular hypersurfaces and a reformulation of standard conjectures for singular varieties would be needed.',
 'Specify a cohomology/cycle theory for singular spaces and the desired resolution or intersection-cohomology functoriality; ordinary smooth-projective statements cannot simply be copied.',
 'SGA1X3.4 and3.8–3.9 provide the birational/specialization framework underlying the obstruction. No unique singular-variety conjecture is formulated on the page.',
 'The smooth reduction is explicitly abandoned because it would force trivial fundamental group; the singular replacement is only a program.',
 'Worth an editorial history note; choosing a modern singular theory is a separate research task.', ['SGA1'])
p(62,'Hodge’s surface projectors and their reception',[47],[245],
 'Tate reports the1938Hodge surface correspondence result; Grothendieck asks why it was neglected for nearly thirty years.',
 'Identify precisely which projectors Hodge constructs and document their reception through contemporaneous citations; do not infer reception from a single letter.',
 'The supplied title/volume/pages and Kleiman1968 attribution identify the paper. The original Hodge full text and broad reception record were not obtained in this run.',
 'The concern is historical, not a mathematical conjecture; no reason for the claimed neglect is established.',
 'Worth a bounded bibliographic task once the original article is accessible.', ['Hodge1938',K])
p(63,'Whether to remove the EGA galley’s part(ii)',[43],[262,263],
 'The margin says Vider|Virer(ii) sauf raison sérieuse; the continuation of the attempted quotient reduction is absent.',
 'Recover the exact galley conclusion and compare with EGAIV4Remark18.11.6–18.11.7 before judging whether the reduction is useful or correct.',
 'The separability obstruction and local quotient identity are checked. A translation proxy locates the published neighborhood, but no manuscript ink or deletion causality is decided.',
 'The source itself proposes deletion; it does not state the serious reason that would justify retention.',
 'Worth an editorial comparison with the original printed EGA and galley images.', ['EGAIV4',S])
p(64,'SGA3 correction sheet and edition concordance',[26],[230],
 'He lists precise corrections to SGADXV,XVI,XVII, including generic Cartan spreading and several cross-references.',
 'Map each old typescript page/line to the original1970edition and annotated reprint, retaining later editorial changes separately.',
 'The substantive Cartan paragraph matches XVProposition6.2(iii); XV–XVIIintro documents Raynaud’s composition from1964Groth notes. Exact all-line edition concordance remains documentary.',
 'These are production corrections, not unresolved structural group-scheme conjectures.',
 'Worth a bounded edition audit; the mathematical claim already has a precise published locator.', ['SGA3II1970'])
p(65,'The way-out-functor RHom exercise',[41],[260,261],
 'The reused text leaves the coherent-RHom corollary as a way-out-functor exercise under alternatives(a) and(b).',
 'Prove coherence for D⁻_coh×D⁺_coh, and the stated finite Ext-amplitude alternative; do not omit boundedness.',
 'Stacks0D0C and0G4H provide modern precise results. This run independently checks finite-diagonal/truncation reasoning and gives a field counterexample to the unrestricted extension.',
 'The source labels it an exercise; there is no evidence it remained a research problem.',
 'Worth writing the short proof if used in the companion; provenance of the reused sheet remains separate.', [S,'Hartshorne1966'])
p(66,'Transitivity of the different with complete-intersection hypotheses',[52],[266],
 'Dire ce qu’on sait; if C is a local complete intersection over B, the transitivity formula works.',
 'Fix the kind of different and require a finite flat lci tower with the needed generic separability for a trace interpretation; then the Jacobian block determinant gives the product formula.',
 'Stacks49.2,49.9,49.12 provide the canonical comparisons and lci equality. The exact isolated generality is not determined by the note; the triangular model is exactly checked.',
 'This is an expository TODO with missing ambient chapter assumptions, not evidence of a false general theorem by him.',
 'Worth recovering the Bourbaki draft’s assumptions before compiling a precise statement.', [S])
p(67,'Kähler different versus trace different',[52],[265,267],
 'Define the Dedekind different by trace and show agreement with Kähler’s for DVRs, using the cited chapter theorem and dévissage.',
 'Assume finite DVR extension with separable fraction-field extension; distinguish the trace, Noether and Kähler definitions and the lci comparison.',
 'Stacks49.8–49.12 supplies exact modern hypotheses and comparisons; the source expressly treats an existing theorem.',
 'The open step is presentation of a classical theorem in a missing draft, not a new conjecture.',
 'Worth a compact glossary and hypothesis table, not a new theorem hunt.', [S])
p(68,'Nilpotent invariance as an appendix',[54],[274],
 'On essaiera de mettre l’appendice: finite étale algebras over A and A/I are equivalent for nilpotent I; see SGA.',
 'State an equivalence of categories induced by reduction, with no assertion of equal rings or unique representatives.',
 'SGA1 and EGAIV4§18.1 give the historical setting; Stacks0BQB and04DY prove the precise and stronger modern invariance.',
 'An expository inclusion decision; mathematically established.',
 'Worth including the exact categorical statement if needed for the chapter’s flow.', ['SGA1','EGAIV4',S])
p(69,'The monogenicity lemma and finite-field obstruction',[52,54,56],[268,278],
 'He proposes R monogenic iff maximal ideals are homogènes, and infers a rational generator from a nonzero discriminant polynomial.',
 'Recover the intended word and field hypotheses. Local standard étaleness is valid; global monogenicity of products needs enough distinct residue-field generators.',
 'F₂³ is a complete exact counterexample to the naive principaux repair and to rational-point inference from a nonzero polynomial. Stacks03PA gives the valid local monogenic theorem.',
 'Confirmed ink has no supplied grading, and the ambient Bourbaki hypotheses are missing.',
 'Worth an ink/context check before proposing any corrected global lemma.', [S])
p(70,'Tame Kummer exposition and canonical complex monodromy',[52],[269,270],
 'Include the root-of-uniformizer description for complete totally tamely ramified extensions, and the Riemann-surface generator exp(2πi/n).',
 'Keep total tameness and completeness; add roots of unity for a cyclic Kummer assertion. Canonical generator belongs to the oriented complex local model.',
 'Sutherland2021Theorem11.10 and its complete-DVR proof directly verify the uniformizer result. The arithmetic statement does not acquire a canonical generator merely from tameness.',
 'An expository TODO; no source indicates a surviving conjecture.',
 'Worth a short hypothesis clarification if the chapter is edited.', ['Serre1962','Sutherland2021',S])
p(71,'Main-theorem and automorphism-group editorial refinements',[54],[272],
 'Add improvements depending on the main theorem; extend a proposition on automorphism groups to the noetherian nonreduced case, referring to Tribu64.',
 'The missing source propositions and hypotheses must be recovered before a theorem can be stated.',
 'EGAIV§18 and SGA1 supply nearby local-structure/descent theory, but the detached proposition numbers do not identify exact refinements.',
 'The statement is absent, so its fate cannot be classified more strongly than unidentified.',
 'Worth only after locating Tribu64 and the referenced Bourbaki version.', ['EGAIV4','SGA1'])
p(72,'Global finite-étale criterion from fibres',[54,56],[273,275,281],
 'The detached finite-fibre equivalence is written without flatness, although scan56 explicitly includes flatness in the definition of étale.',
 'For finite flat finitely presented B/A, finite étale fibres give finite étaleness; determine whether the detached draft already assumed flatness.',
 'Stacks02GU gives the exact criterion. A=k[t],B=A×A/(t) refutes the literal unqualified version with every hypothesis checked.',
 'Missing context or a mathematical omission; no scan evidence decides which.',
 'Worth an editorial cross-reference to scan56 and the explicit counterexample.', [S])
p(73,'Reused English cohomology-vanishing fragment',[28,30],[231],
 'A reused typescript proves H^r(A,G)=0 for r>2 by missing Theorems1,4 and Proposition14 and Tate/Shatz duality; its author is not identified.',
 'Recover the topology, class of groups and local-base assumptions before stating or using the theorem.',
 'Shatz1966 publisher metadata and the explicit1964/1959 backward citations were checked as leads; no exact text match was found. This is classF provenance, not a new Grothendieck conjecture.',
 'The page is detached from its definitions; no mathematical failure is inferred.',
 'Worth a short bibliographic reconstruction if this reused text is retained in the companion.', ['Shatz1964','Shatz1966','Tate1959'])
p(74,'Amitsur-complex acyclicity in that fragment',[28,30],[232],
 'Proposition15 states acyclicity of the face-map complex H^s(K^⊗r,G_m) for purely inseparable K/k and s>0, without the preceding cohomology convention.',
 'Identify the intended flat/Grothendieck cohomology and preceding comparison theorem before claiming acyclicity in another theory.',
 'Rosenberg–Zelinsky1962 is the explicit backward reference; primary introduction and acyclicity lemmas were opened. They are not by themselves an exact match to the detached Proposition15.',
 'Provenance and hypotheses are missing; the fragment gives no proof on this page.',
 'Worth only as a targeted source-identification task, not an unsupported general theorem.', ['RosenbergZelinsky1962','Shatz1966'])
p(75,'Provenance of the Matlis and sheaf-injective sheets',[37,39,41],[257,258,259,260,261],
 'The reused English text recalls Matlis and derives injective sheaves/RHom facts. No author is named in the supplied fragment.',
 'Match exact Lemma3.3,Proposition3.4,Corollary2.2 against the appropriate duality draft or edition, independently of the mathematical verification.',
 'Matlis1958Theorem2.5,Proposition3.1,Theorem3.10 are exact prior sources. Hartshorne1966II7.5–7.6pp122–124 and7.17pp131–132 now directly match the mathematical text and its proof. Full original proofs were read; exact preliminary typescript identity remains unproved.',
 'This is an editorial identification problem, not a mathematical question of Grothendieck.',
 'Worth a bounded archival/bibliographic task to prevent false authorship.', ['Matlis1958','Hartshorne1966',S])
p(76,'Karoubi’s Banach-category cohomology program as reused context',[35],[256],
 'The sheet explicitly names Max Karoubi and proposes higher K-groups with Bott-periodicity properties.',
 'Read the original announcement and expanded categorical hypotheses rather than attributing the program to Grothendieck.',
 'Karoubi1966announcement identified; expanded1968§2.3results read. The supplied sheet contains definitions, not a new Jacobian theorem.',
 'The program was developed by its named author; no open SA19 theorem follows from the reused page.',
 'Worth a brief provenance note, with no independent SA19 research direction.', ['Karoubi1966','Karoubi1968'])
(root/'problems.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(f'Wrote {len(rows)} individually formulated problem/editorial records.')
