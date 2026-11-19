# Authorial questions, including steps resolved or withdrawn later in the same
# supplied sequence. Source occurrences are exact, not inferred from headings.
def problem(key,title,claimkeys,as_he,plausible,state,worth,refs,why=None):
    occ=[]
    for keyc in claimkeys:
        cl=next(x for x in claims if x['local_key']==keyc)
        occ.append({'claim_id':cl['id'],'cote':cl['cote'],'scans':cl['scans'],'lines':cl['lines'],'his_words':cl['his_statement']})
    return Pr(key,title,occ,as_he,plausible,state,why or 'The supplied pages give no historical explanation for abandonment. A gap in the manuscript is not evidence of a later research decision.',worth,refs)

problem('lang_lemma','The zero-differential Lang lemma and finite fixed points',['lang_etale','fixed_points_finiteness','quotient_open'],
 'Extract a lemma: for a smooth group and an endomorphism with zero differential, the associated Lang map is étale and, in the connected case, surjective; identify the fixed subgroup and quotient.',
 'For a smooth S-group with geometrically connected fibres and df=0, the Lang map is étale surjective. Its fixed subgroup is étale; finiteness additionally follows in the finite-type finite-field case.',
 'Lang1956, Theorem1, proves the connected finite-field case. The tangent/open-orbit argument in proofs.md §2 verifies the stated extension. Stacks025F, Theorem41.14.1, identifies an étale monomorphism with an open immersion. Infinite constant groups show why finite cannot be inferred from étale.',
 'Only a short proof-and-conventions commentary is needed; the qualified theorem is established.', ['Lang1956','Stacks025F','Stacks047J'],
 'The author requests a lemma, then immediately uses it; the supplied sequence does not record later abandonment.')
problem('frobenius_module','How much finiteness forces a Frobenius-fixed module to be a vector bundle?',['frobenius_fixed_module_question','unit_frobenius_equivalence'],
 'Can a module equipped with an isomorphism to its Frobenius transform fail to be locally free?',
 'A finitely presented R-module M over any characteristic-p ring with F_R^*M≅M is locally free. Finite generation alone is insufficient.',
 'Stacks07Z6, Lemmas15.8.4 and15.8.8, supplies base change of Fitting ideals and the local-freeness criterion. The Fitting/Nakayama deduction and a cyclic nonfree module over a perfect valuation ring are written out in proofs.md §3. Lang1956 gives the finite-rank étale-local trivialization.',
 'Worth a bounded note separating finite presentation, finite generation and arbitrary rank; no open finite-presentation theorem remains.', ['Stacks07Z6','Stacks0EBU','Lang1956'])
problem('cancelled_kernel','The cancelled finite Frobenius-kernel assertion',['frobenius_kernel_cancelled','height_frobenius'],
 'The provisional assertion on scan17 asks for finite presentation/radicial surjectivity of Uν(G), then is struck out; scan19 replaces it by height and augmentation-ideal statements.',
 'For an affine group in characteristic p, ker F^ν is cut out by the Frobenius power of the augmentation ideal. Finite locally free conclusions require the corresponding smooth/flat finite-type assumptions.',
 'SGA3VIIA §4 and §7 establish Frobenius kernels and height-one finite-flat theory. This resolves the qualified replacement, not every clause of the deleted sentence.',
 'Useful as a record of self-correction and a scan check; it is not a live conjecture to revive.', ['SGA3VIIA'],
 'It is explicitly withdrawn on scan17 and replaced on scan19; this is a same-text withdrawal, not an inferred historical reason.')
problem('picp_dlog','Injectivity and image of logarithmic differentiation on Pic[p]',['dlog_injective','cartier_fixed_picp','bad_dlog_quotient'],
 'Is the displayed map from p-torsion invertible sheaves to global differentials injective, and is its image given by Cartier-fixed forms? The proof tries to replace a normal local ring by a regular one.',
 'For smooth proper X over a perfect field of characteristic p, Pic(X)[p] identifies with the global closed one-forms fixed by Cartier, with the appropriate Frobenius-semilinear convention. A normal singular X needs a specified differential sheaf and an additional argument.',
 'Cartier1958, the logarithmic differential criterion near printedpp200–203, and Oda1969, §5, give the smooth and proper comparison. Oda Cor5.11 concerns A[p] and H¹dR(A), while Cor5.12 for a general smooth proper X uses a smaller iterated-Cartier-stable space. The literal K*/O* injection is false because t^p has zero dlog.',
 'Worth developing the exact singular-normal boundary, after the local-ring passage and differential notation are checked on the scans.', ['Cartier1958','Oda1969'])
problem('cartier_transpose','What transposes the restricted p-operation?',['restricted_p_transpose'],
 'Seek an operation on differential forms dual to D↦D^p; the last word may say the attempt should succeed or fail.',
 'There is no naive O-linear transpose because the restricted p-operation is not O-linear. Cartier identities provide the correctly semilinear nonlinear relation under smoothness.',
 'Cartier1958 constructs the Cartier operator and logarithmic criterion. SGA3VIIA §7 gives the p-Lie correspondence with finite-flat hypotheses. The D=∂t, (tD)^p=tD test in proofs.md §7 rules out the naive O-linear interpretation.',
 'A short scan-led reconstruction is worthwhile; the polarity of the final word must be read before treating it as an abandoned idea.', ['Cartier1958','SGA3VIIA'])
problem('height_one_scope','The cotangent description of height-one groups',['height_one_dictionary','height_one_commutativity'],
 'Encode a height-one group by a cotangent module with operations dual to the bracket and p-operation, with commutativity detected by the vanishing bracket.',
 'The restricted-Lie/height-one equivalence holds for the appropriate finite locally free objects in characteristic p. Arbitrary quasi-coherent modules require a separate formulation.',
 'SGA3VIIA Theorem7.4 and Remark7.5 give the precise finite-flat equivalence; the adjacent nonflat example explains why those qualifications cannot be erased.',
 'Useful for a precise commentary linking46:22 to54:5–7; a new unrestricted theorem is not supported by these pages.', ['SGA3VIIA'])
problem('verschiebung_base','Extending the Verschiebung construction beyond a field',['verschiebung_symmetric','verschiebung_FV','verschiebung_base_extension'],
 'The typescript constructs V over a characteristic-p field by symmetric tensor powers, proves the multiplication-by-p identity, and points toward base extension and duality.',
 'For a commutative flat group scheme over a characteristic-p base, Verschiebung is defined with the usual Frobenius twist and FV=VF=[p]; for finite locally free groups it is dual to Frobenius.',
 'SGA3VIIA §§4.3.1–4.3.3 gives these base-ring and duality statements. The multinomial divisibility used in the field construction is recomputed in checks.py; no missing sender or date is inferred.',
 'Worth an exposition of the complete four-page construction and its finite-flat extension; the mathematical identity is established.', ['SGA3VIIA'])
problem('topos_converse','How much of Frobenius comparison survives for arbitrary topoi?',['topos_b_implies_a','topos_converse'],
 'Which of the abstract Frobenius conditions imply one another, and does the converse hold without further hypotheses?',
 'The étale-topos comparison is valid for schemes in characteristic p. The proposed general ringed-topos converse must specify the category, Frobenius action and representability assumptions.',
 'Stacks03SL §64.3 proves the scheme-theoretic comparison including the coefficient identification. SGA5XV treats the Frobenius/cohomology setting. These do not by themselves identify every abstract condition in the manuscript; the broader literal converse remains unidentifiable at that scope.',
 'First recover the exact axioms from the ink; no useful new theorem can be formulated until that ambiguity is removed.', ['Stacks03SL','SGA5XV'])
problem('gluing_scope','The incomplete gluing and cohomology setup',['gluing_H0','gluing_cohomology'],
 'Prove a restriction comparison on H⁰, and then on cohomology, by gluing sheaves along Y and an auxiliary space denoted by a bar.',
 'An equalizer description and derived comparison hold once the actual gluing square, adjoints and base-change assumptions are specified. The supplied selection does not determine all of them.',
 'The opened sheaf formalism in MilneEC §§7–12 and SGA4Sheaves supplies equalizers, exact sequences and derived-image methods. It does not settle an unidentified square. The word conoyau on46:37 is inconsistent with the displayed embedding and should be checked against noyau.',
 'A scan-and-context recovery task is worthwhile; broad recollement analogies should wait for the square to be identified.', ['SGA4Sheaves','MilneEC'],
 'The proof refers to preceding hypotheses not fully recoverable from the selected pages; no claim of authorial abandonment is made.')
problem('bs_divisors','Brauer–Severi spaces of divisors of arbitrary degree',['bs_degree_one','divisor_symmetric_power','divisor_functor'],
 'The margin asks whether the degree-one divisor construction extends to degree n; the continuation46:58–60 carries it out.',
 'For a Brauer–Severi scheme P/S, the degree-n divisor parameter space is obtained from the appropriate symmetric/divided-power representation; its Brauer obstruction is n[P], with quotient/dual conventions fixed.',
 'BrauerI1966 §1 gives the connecting obstruction and its additive behaviour; BrauerII1966 treats the linear-system interpretation. The manuscript continuation itself resolves the original n-question. In characteristic p, a canonical identification Sym^n(E*)≅Sym^n(E)* cannot be inserted without checking the tilde convention.',
 'Worth a complete conventions audit and scan check of the symmetric-power notation; the existence question is resolved in the supplied continuation.', ['BrauerI1966','BrauerII1966','Stacks01OA','StacksDividedPowers'],
 'It did not remain open in this sequence: the later scans58–60 develop the construction anticipated on41 and45.')
problem('bs_linear','Does the resulting monomorphism have to be a linear embedding?',['linear_mono_gap'],
 'Conclude that the map from a Brauer–Severi space into a projective bundle is a linear embedding from its monomorphism property.',
 'A projective-space monomorphism is linear only with a degree-one condition, for example pullback of O(1)≅O(1). A Veronese embedding refutes the bare implication.',
 'Stacks01OA §27.21 gives the universal quotient description and determines the necessary invertible sheaf. BrauerII1966 §0 supplies the correct degree-one splitting criterion. proofs.md §11 checks the quadratic Veronese counterexample.',
 'A short repair identifying the missing degree-one input would improve the commentary and may close the local argument.', ['Stacks01OA','BrauerII1966'])
problem('picard_flatness','Weakening the hypotheses in the Picard linear-system argument',['weakened_picard_hypotheses','linebundle_descent_49'],
 'The author questions which flatness and cohomological hypotheses are really needed for the linear-system/Picard construction.',
 'Retain properness and the specific cohomological flatness/base-change and fibrewise linear-system hypotheses actually used; weakened assumptions must be checked on each direct-image and descent step.',
 'FGA236, Picard VI, and StacksProjection give the published Picard and projection/base-change mechanisms. They support the stated sufficient hypotheses but do not prove every abbreviated weakening in the margin.',
 'Worth a bounded hypothesis audit after the crossed-out flatness phrase is checked; avoid elevating the margin to an established minimal theorem.', ['FGA236','StacksProjection'])
problem('progroup_kappa','The doubtful κ-equivalence for pro-groups',['progroup_full_faithful','progroup_affine','progroup_kappa'],
 'Compare group objects in pro-schemes with proobjects in group schemes and ask whether κ is an equivalence; the word douteux is explicitly attached to the equivalence.',
 'Full-faithfulness follows under the stated lim-colim and strict-system conditions. Essential surjectivity must be restricted to a defined class of systems, such as the affine group setting with its finiteness conditions.',
 'Serre1960 §2 constructs a category of commutative pro-quasi-algebraic groups over an algebraically closed field; it deliberately perfects away inseparable phenomena. Perrin1976 Theorem2.4.1 and §4 treat quasi-compact group-scheme approximation. Neither is automatically the illegible C,C′ equivalence of this page.',
 'High value as a scan-led reconstruction of κ and its exact categories; no claim of an unsolved modern pro-group theorem is warranted.', ['Serre1960','Perrin1976'])
problem('topological_brauer','Do all torsion topological Brauer classes come from matrix bundles?',['brauer_torsion_realization'],
 'For a topological space X, does every torsion class in H²(X,C*) lie in the image of the Brauer group of matrix-algebra bundles?',
 'Yes for finite CW complexes and, in the standard topological sheaf interpretation, compact spaces treated by the cited theorem; false for arbitrary infinite CW complexes.',
 'BrauerI1966 records Serre’s finite-CW result. HornbostelSchroer2015 proves the compact-space equality and Theorem3.1 gives Br(K(Z/n,2))=0 although its cohomological Brauer group is Z/n. Continuous-function C* sheaves and constant C* coefficients must be distinguished.',
 'A historical explanation is worthwhile; the unrestricted question has a known negative answer, so a new task should focus on a clearly bounded class of spaces.', ['BrauerI1966','HornbostelSchroer2015'])
problem('brauer_fixed_degree','Realization with a prescribed projective degree',['brauer_fixed_degree'],
 'Is every H²(X,Z/n) class the central obstruction of a projective bundle of the indicated rank n?',
 'The degree must in general be divisible by the topological index, which can exceed the period even on a finite CW complex.',
 'AntieauWilliams2014 constructs a finite six-dimensional CW complex with a period-two class of index eight. This refutes the fixed-degree inference while leaving the arbitrary-degree finite-CW theorem intact. HornbostelSchroer2015 separates finite and infinite complexes.',
 'Worth tracing the precise central extension and rank convention on scans65–67; the unrestricted fixed-degree conjecture is refuted.', ['AntieauWilliams2014','HornbostelSchroer2015'])
problem('torsion_multipliers','Torsion group multipliers and finite projective representations',['group_multiplier_torsion'],
 'For an arbitrary discrete group π, is every class in H²(π,Q/Z) realized by a finite-dimensional projective representation?',
 'Finite groups admit finite-dimensional twisted regular representations, but arbitrary infinite groups do not have this property.',
 'HornbostelSchroer2015 §5 studies infinite elementary abelian groups. The explicit multiplier on ⊕(C₂×C₂) in proofs.md §18 restricts on its first m pairs to a nondegenerate twisted group algebra M_(2^m)(C), forcing every representation dimension to be divisible by2^m for all m. Thus no nonzero finite-dimensional projective representation exists.',
 'A compact counterexample commentary would settle the manuscript’s unrestricted question; finer classes of groups require a new scoped task.', ['HornbostelSchroer2015'])
problem('all_multipliers','Arbitrary complex group multipliers',['group_multiplier_general'],
 'If the torsion question fails, could every class in H²(π,C*) at least be realized by some finite-dimensional projective representation?',
 'No: a finite-dimensional multiplier class has finite order dividing the dimension, by taking determinants.',
 'BrauerI1966 §1 gives the central obstruction framework. The π=Z² multiplier with commutator scalar2 in proofs.md §18 would require matrices UV=2VU, hence2^d=1 by determinants, impossible for d>0.',
 'This requires only a short explicit negative answer, with the constant-coefficient group-cohomology category stated.', ['BrauerI1966','HornbostelSchroer2015'])
problem('restriction_nonsmooth','Restriction of scalars and nonsmooth coefficient groups',['restriction_cohomology','norm_kernel','reduced_nonsmooth_norm'],
 'Does the H¹ comparison under restriction of scalars extend beyond smooth groups, especially to radicial, commutative or nonproper groups?',
 'The smooth finite-extension étale-torsor comparison is valid. Nonsmooth group schemes require fppf cohomology and cannot be treated by the same étale lifting argument.',
 'MilneAG2017 §2i constructs restriction of scalars; MilneEC §§8–12 supplies the étale direct-image formalism. SGA3VI_A §1 exhibits reduced nonsmooth groups over imperfect fields. The notebook’s degree-p norm kernel supplies the relevant obstruction example; exponent one alone does not make the norm the pth power.',
 'Worth formulating and checking the exact fppf comparison for the specific finite inseparable extension, without importing the smooth proof unchanged.', ['MilneAG2017','MilneEC','SGA3VI_A'])
problem('finite_field_h90','The finite-field gap in the algebra Hilbert90 proof',['h90_algebra','twisted_Lang_finite'],
 'The determinant/averaging proof works over an infinite base field; the author asks how to handle finite fields and invokes a twisted Lang argument.',
 'For a finite-dimensional algebra with a compatible semilinear action of a finite Galois group, H¹ of the unit group is trivial. Over a finite field the unit group is a connected smooth open in its affine algebra space, so Lang applies.',
 'Lang1956 Theorem1 proves the needed finite-field surjectivity. MilneAG2017 supplies the algebraic-group form, and SerreGC records nonabelian twisting and Hilbert90. proofs.md §20 checks the finite-dimensionality and factor order rather than importing the erroneous displayed simplification.',
 'A bounded repair of the finite-field proof is worthwhile; no unresolved Hilbert90 theorem remains under the retained finite-dimensional hypothesis.', ['Lang1956','MilneAG2017','SerreGC'])
problem('twisting_converse','Which isomorphisms of twists recover a cocycle?',['twists_converse_naturality'],
 'If all G-sets twisted by two cocycles are isomorphic, does that force the cocycles to be conjugate?',
 'A natural isomorphism of the twisting functors gives the correct converse. Separate, non-natural isomorphisms for every G-set are insufficient.',
 'SGA3I and SerreGC give the torsor/twisting formalism. The C₅ example in proofs.md §20 checks the failure of the pointwise version by comparing every transitive C₅-set.',
 'Worth checking whether the text intended natural isomorphisms; the distinction can be resolved in a short commentary.', ['SGA3I','SerreGC'])
problem('cyclic_quotient','The unfinished quotient criterion for periodic cyclic H¹',['quotient_H1_criteria','periodic_colimit'],
 'Derive injectivity and surjectivity of H¹ across1→G′→G→G″→1 for a periodic automorphism using twisted norm maps.',
 'A lift α of a quotient cocycle must be corrected by t∈G′ satisfying the twisted norm equation with right side N_T(α)^{-1}. Existence and conjugacy obstructions belong to the appropriate twisted kernel.',
 'SerreGC’s nonabelian exact-sequence/twisting formalism gives the corrected obstruction language. MilneCFT II§4 gives continuous finite-quotient passage. The free-word computation in proofs.md §21 records the actual noncommutative equation; it does not turn the incomplete final sentence into a theorem.',
 'A short task could finish a precisely stated criterion once the final indexing and factor order are recovered from the scan.', ['SerreGC','MilneCFT','SGA3I'])
problem('semilocal_scope','The semilocal Hilbert90 theorem after deleting finiteness',['semilocal_deleted_finite','completion_intertwiner','inertia_reduction'],
 'Show injectivity into inertia/residue H¹ and into completion, with a finite-module assumption visibly deleted although the proof later uses it.',
 'A valid finite-module theorem must retain noetherian completion and invariant-base hypotheses; the arbitrary-algebra version is false.',
 'StacksCompletion gives flat completion and the finite-module control used by the proof. SerreGC gives twisting and field Hilbert90. The explicit O=C, A=C[t,t⁻¹], conjugation plus t↦t⁻¹ example has trivial inertia and a nontrivial cocycle t, so it refutes the broad statement after the deletion.',
 'High value: a single run could locate the maximal theorem actually supported by the written proof and distinguish it from the refuted generalization.', ['StacksCompletion','SerreGC'])
problem('invariant_residue','Does trivial residue action give invariant lifts?',['invariant_residue_false','invariants_noetherian_false'],
 'The margin asks, with ??, whether O^Γ→O/m is onto when Γ acts trivially on the residue field; the proof also assumes noetherianity and finiteness over invariants.',
 'Neither assertion holds for an arbitrary finite action on a noetherian ring. Surjectivity must be assumed or supplied by an invariant coefficient-field/lifting theorem.',
 'GiokasSingh2024 Theorem2.1 gives regular-local examples with nonnoetherian invariants and cites Nagata/Nagarajan predecessors. The dual-number action t↦t+ε over F_p(t) in proofs.md §22 has invariant residue image F_p(t^p), strictly smaller than the residue field; a countably generated p-basis gives an Artinian noetherian ring with nonnoetherian invariants.',
 'Worth a short counterexample appendix and a careful rewrite of every later argument that uses these assumptions.', ['GiokasSingh2024'])
problem('sylow_detection','Residue and Sylow detection in nonabelian H¹',['sylow_detection'],
 'The revised theorem seeks injectivity, with bijectivity crossed out, from residue H¹ and p-Sylow H¹ under an explicit invariant-lifting hypothesis.',
 'The additive restriction map is injective when the subgroup index is invertible. Nilpotent induction proves a neutral-fibre statement under finite-module and lifting hypotheses; full injectivity additionally requires the corresponding hypotheses after twisting.',
 'SerreGC and MilneCFT II give restriction/corestriction and twisting. The arithmetic identity cor∘res=[Γ:P] proves the additive step. These sources do not justify the manuscript’s full broad algebra statement after its finiteness assumption has been deleted.',
 'Worth completing a finite-module, twist-stable version; the first task is to spell out exactly which invariant lifts survive twisting.', ['SerreGC','MilneCFT','SGA3I'])
problem('quotient_example','The attempted nonrepresentable quotient example',['quotient_counterexample_attempt'],
 'Construct a quotient obstruction by taking a free projective-linear action and descending an ample bundle, then conclude the quotient is affine.',
 'The group and free locus must first be identified. For the literal natural PGL action on P^N, N≥1, the free locus is empty; ample does not imply affine.',
 'SGA3VI_A and Perrin1976 give genuine quotient and image results under their stated assumptions. Neither repairs this construction. The stabilizer dimension N²+N and the example P¹ with O(1) independently invalidate its two literal steps.',
 'Recover the uncertain group notation from the scan before spending a research run on the construction.', ['SGA3VI_A','Perrin1976'])
problem('group_components_general','Are components of arbitrary group schemes irreducible and quasi-compact?',['group_neutral_component'],
 'The author questions the connected-component/irreducible-component identification, cancels several interim corollaries and later corrects the proof.',
 'For every group scheme over a field, the neutral component is a closed normal geometrically irreducible quasi-compact subgroup; components are irreducible and quasi-compact. Local finite type additionally makes them open.',
 'Stacks047J Lemmas39.7.9–39.7.11 proves the arbitrary group-scheme result. SGA3VI_A §2.3–2.4 treats the locally finite-type version. Perrin1976 develops the general approximation framework.',
 'A useful historical commentary can show exactly which generality the later theorem reaches; it is not an unresolved component theorem.', ['Stacks047J','SGA3VI_A','Perrin1976'])
problem('specialization_stability','Specialization, generization and neutral-component invariance',['specialization_converse_false','group_open_component_products'],
 'The author replaces an open-and-closed hypothesis by stability under specialization in a claimed criterion for G⁰-invariance, and asks to understand an implication about products of opens.',
 'One-sided specialization stability does not imply G⁰-invariance: {0}⊂G_a is closed but not translation-stable. A clopen or two-sided specialization/generization formulation needs the actual orbit hypotheses.',
 'SGA3VI_A §2 and Stacks047J establish component/orbit facts. The literal Cartesian U×V-closed assertion also fails for punctured affine opens; an intended multiplication image UV is a different statement and is not refuted by that example.',
 'Worth a scan-led correction of the connective and product symbol; avoid replacing the text silently.', ['SGA3VI_A','Stacks047J'])
problem('group_image','Closed images, universal generization and translated flatness',['group_hom_flatness','group_image_closed'],
 'Is the image of a group morphism specialization-stable, and can the flatness/generization argument be made universal? The margin says yes but leaves a proof obligation.',
 'For finite-type group morphisms the standard flat image and closed-subgroup theorems apply. The arbitrary quasi-compact extension requires the appropriate scheme-theoretic image and approximation theorem.',
 'SGA3VI_A §2.5 gives finite-type image and flatness results; Perrin1976 Theorems4.1.4 and4.2.1 treat quasi-compact approximation and quotients. Their hypotheses are retained explicitly. A translation argument alone does not replace the universal base-change proof.',
 'A bounded task could write the general theorem with its exact approximation hypotheses and resolve the target/source generic-point slip.', ['SGA3VI_A','Perrin1976'])
problem('group_devissage','How broad is the proposed devissage of general groups?',['group_devissage'],
 'Decompose groups through the reduced neutral group, components, Frobenius-height pieces, abelian varieties, semisimple groups, tori and possibly twisted additive groups.',
 'Chevalley structure applies to connected smooth finite-type groups; over perfect fields smooth connected unipotent groups admit appropriate G_a filtrations. Such a filtration is not an assertion that every unipotent group is a product of additive groups.',
 'MilneAG2017 gives the smooth finite-type structure and unipotent theory; SGA3VIIA gives infinitesimal height-one theory; Perrin1976 supplies quasi-compact approximation. These are compatible ingredients rather than one unconditional decomposition.',
 'Worth a scope table in the folder commentary; no new research direction should be based on a nonexistent direct-product theorem.', ['MilneAG2017','SGA3VIIA','Perrin1976'])
problem('reduced_group','Does reduced imply geometrically reduced for finite-type groups?',['reduced_group_imperfect','group_smoothness_equiv'],
 'The margin asks whether reducedness suffices for the separable/geometrically reduced condition.',
 'Yes over a perfect field for locally finite-type groups; no over an imperfect field.',
 'SGA3VI_A §1 and StacksGroupSmooth prove the perfect-field theorem. The subgroup x^p−ay^p=0 over F_p(a) is reduced and becomes nonreduced after adjoining a pth root of a; the group law and base-change factorization are checked in proofs.md §25.',
 'A short example resolves the author’s question and links it to46:71; no unrestricted positive claim remains.', ['SGA3VI_A','StacksGroupSmooth'])
problem('geometric_component_tests','The corrected geometric irreducibility and connectedness tests',['geometric_irred_rectification','geometric_connected_subscheme','sepclosed_connected_products'],
 'Determine when a geometrically irreducible/connected subscheme forces the ambient scheme to have the same geometric property; extend a product argument beyond the locally finite-type case.',
 'Retain connectedness or irreducibility of the ambient scheme and the nonempty/unique-geometric-component hypothesis actually used. Product tests quantify over nonempty connected or irreducible test schemes, not all schemes.',
 'Stacks0361 and Stacks0364 establish the field-extension and product criteria, including the relevant subspace tests. The author’s real cone and this run’s disconnected-union examples show why the omitted hypotheses matter. The general product projection is universally open for field bases, supplying the quotient-topology step.',
 'Worth a precise logical rewrite and scan check of the reversed implication, with the corrected theorem separated from the literal text.', ['Stacks0361','Stacks0364'])
problem('component_continuity','Continuity and representability of the component quotient',['component_universal_quotient','component_continuity_question','proetale_dictionary'],
 'For quasi-compact X, construct the maximal ind-étale component algebra and show that the Galois action on geometric components is continuous; scan15 asks for the continuity argument.',
 'For qcqs schemes, the affine profinite component quotient has geometrically connected fibres and the continuous Galois description. The quasi-compact-only wording and arbitrary locally pro-étale conventions need a separate proof.',
 'Stacks0BQA and StacksProetale give the relevant spectral/profinite and pro-étale constructions; SGA1V gives the finite Galois dictionary. Serre1960 concerns its own pro-quasi-algebraic category. None should be cited as settling an unspecified topology on all component spaces.',
 'High value for a bounded research run: isolate whether quasi-separatedness is essential to this exact component construction and recover the topology intended on scan15.', ['Stacks0BQA','StacksProetale','SGA1V','Serre1960'])
problem('character_representability','Representability of Hom(G,G_m) beyond finite-flat and diagonalizable groups',['hom_representability_question','characters_diagonalizable','cartier_duality_finite'],
 'The line asks if the character functor is representable, but its deletion/insertion and the example G=G_m are mutually inconsistent as transcribed.',
 'For diagonalizable groups the character group is the associated locally constant character sheaf; finite locally free commutative groups have finite locally free Cartier duals. Broader character-functor representability requires its own hypotheses.',
 'SGA3VIII §1–3 gives diagonalizable and finite Cartier duality; SGA3VIIA gives the finite-flat Hopf dual and examples. These establish the clear clauses but cannot determine the polarity of the corrupted general sentence.',
 'Read the ink first; mathematical reconstruction alone cannot decide whether pas was cancelled or inserted.', ['SGA3VIII','SGA3VIIA','SGA3I'])
problem('monoid_GL','The affine-monoid GL_n assertion and its explicit correction',['monoid_false_GL','two_point_bialgebra','monoid_matrix_embedding','affine_group_approximation'],
 'A letter questions an asserted embedding of every affine finite-type monoid into GL_n and suggests End(M) instead; the reply replaces GL_n by M_n.',
 'Every affine finite-type monoid over a field admits a closed embedding in a matrix monoid M_n; a group embeds in GL_n. The two-point monoid with absorbing0 has no group embedding.',
 'The supplied letter dated15June1973, the reply at53:22 and the proof at53:31 form a complete internal correction. Brion2014 and MilneAG2017 give the finite-coefficient linearization argument; the two-point bialgebra has no antipode.',
 'A historically useful resolved problem: establish the correspondent’s identity from the scan and document the three stages of the correction.', ['Brion2014','MilneAG2017','SGA3I'],
 'The author corrects it in the supplied text, changing GL_n to M_n; the later coefficient proof implements that correction.')
problem('cancellative_monoid','Are finitely presented cancellative monoid schemes groups over every base?',['cancellative_monoid'],
 'The side remark asserts this for a finitely presented monoid over a ring with monomorphic left translations, for example a subfunctor of a group.',
 'The finite-type algebraic-monoid theorem over a field follows from unit/idempotent theory. The exact arbitrary-base scheme statement must be proved or supplied with additional hypotheses.',
 'Brion2014 §2 proves the algebraic-monoid unit/idempotent results over the stated field/variety base. Searches for the all-base-ring formulation did not locate an exact theorem; unrelated monoid schemes over F₁ are not evidence for this claim.',
 'Worth a focused theorem-or-counterexample search after fixing left cancellation versus two-sided cancellation and the fp/flatness hypotheses.', ['Brion2014'])
problem('coaction_question','The question mark in the action/coaction calculation',['actions_coactions'],
 'Check the expansion of g_M(g′_M x) and identify the corresponding coassociativity identity.',
 'For every module M and affine monoid Spec A, linear actions on the quasi-coherent module functor correspond to counital coassociative coactions M→M⊗A.',
 'SGA3I §§4.7.2–4.7.3 proves the same equivalence. The manuscript continues past the question mark and performs the comparison; proofs.md §30 and checks.py recheck the order of the tensor factors.',
 'Resolved in the supplied argument; include it in the commentary as a checked intermediate question, not a live research problem.', ['SGA3I'],
 'The question mark is followed by the calculation on the next lines; no later abandonment is involved.')
problem('subcoaction_uniqueness','When is the induced submodule coaction unique?',['submodule_coaction','quotient_coactions'],
 'The diagram asks for a unique coaction on M″ and then lists tensor-injectivity conditions.',
 'Injectivity of i⊗A gives uniqueness; injectivity also after tensoring by A again transfers coassociativity. Flatness of A or suitable purity of i is sufficient.',
 'WisbauerCoalgebras §7.6 gives the subcomodule criterion and tensor-purity issue. The quotient version uses right exactness and is separate. The two diagram chases are written in proofs.md §30.',
 'Resolved with the stated sufficient conditions; a future task need only identify whether the handwritten list intends necessary conditions.', ['WisbauerCoalgebras','SGA3I'],
 'The page itself supplies sufficient conditions after posing the question.')
problem('arbitrary_intersections','Arbitrary intersections of stable submodules under flatness alone',['intersection_subcomodules','dual_module_stability'],
 'The margin deletes finite from the intersection assertion while retaining flatness of the coalgebra.',
 'Finite intersections are preserved under flat tensoring. Arbitrary intersections of subcomodules hold under local-projectivity/direct-sum-of-finite-projectives conditions by dual-module stability; the flat-only coalgebra assertion requires separate verification.',
 'WisbauerCoalgebras §§1.21 and7 gives finite-intersection and tensor-purity tools; the direct-sum coefficient criterion proves the stronger-hypothesis result. General Mittag-Leffler/intersection results concern modules, and a Z→Q tensor example alone is not a coalgebra counterexample.',
 'High value for one focused run: find an exact flat-coalgebra counterexample or prove the missing coalgebra-specific intersection argument.', ['WisbauerCoalgebras','MittagLeffler2026'])
problem('tensor_functor_scheme','Does arbitrary scheme representability of W(M) force finite projectivity?',['tensor_functor_representability','linear_spec_sym'],
 'Prove that the tensor functor W(M) is representable only when M is finite projective; the written proof uses preservation of products and affine/module-scheme duality.',
 'W(M) is a module scheme V(N) iff M is finite projective. To use the word representable without that qualifier, show that any representing scheme is necessarily an affine module scheme.',
 'ModuleSchemes2009 Theorem1.1 proves exactly the module-scheme equivalence and Corollary1.2 its Hom/tensor criterion. SGA3I gives V(M)=Spec Sym M and finite-projective vector schemes. The extra arbitrary-scheme implication is separated from the published theorem actually opened.',
 'A short representability audit is worthwhile; it should first prove or locate the affineness step instead of assuming it.', ['ModuleSchemes2009','SGA3I'])
