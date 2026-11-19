"""Serialize the author's actual questions and unfinished verifications, manually read."""
import pathlib,json
out=pathlib.Path(__file__).parent
claims={c['id']:c for c in json.loads((out/'claims.json').read_text())}
problems=[]
def add(n,title,ids,his,today,state,worth,why=None):
 cs=[claims['CL-SA19-'+str(i)] for i in ids]
 occ=[dict(cote='43',scans=c['scans'],lines=c['lines'],claim=c['id']) for c in cs]
 refs=list(dict.fromkeys(r for c in cs for r in c['refs']))
 problems.append(dict(id=f'MP-SA19-{n:03d}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,
  state_of_art='As of19November2026: '+state,
  why_open=why or 'The supplied sheets show a question, conditional passage or unfinished verification. No opened source establishes a historical reason for its abandonment; the mathematical obstruction described here is this run’s diagnosis, not a biographical explanation.',
  worth=worth,refs=refs))

add(120,'Unfinished converse for congruence subgroups',[601,602],
 'Scan8 ends the converse sentence after the proposed containment of a congruence subgroup.',
 'For a number field, the finite-index subgroup of units contains a congruence subgroup; insert Chevalley’s power-congruence theorem with denominators excluded.',
 'Chevalley1951 TheoremI supplies the missing implication; Milne CFTV identifies the idelic ray quotient. This is a closed verification, not an open class-field theorem.',
 'Low research interest but high editorial value: a short exact reference closes the unfinished sentence.')
add(121,'Fundamental two-extension and higher cohomology comparison',[610,611],
 'Scans32–35 propose prolonging the sequence, a direct formula for the degree-two class, a converse “sous des conditions convenables”, and higher comparisons “et sans doute”.',
 'Fix the coefficient category and topology, a pointed smooth curve with modulus, and the Picard/generalized-Jacobian complex; then formulate the exact derived comparison degree by degree.',
 'Koszul1954 gives the generalized-Jacobian construction, Serre1960 the specific pro-quasi-algebraic category, and Ribeiro–Rosengarten2026 TheoremsA–B precise extension sheaves. None identifies every unlabelled higher comparison on these sheets.',
 'High interest, moderate short-run feasibility: a category and degree dictionary can turn the diagrams into testable propositions.')
add(122,'Characterization of the map to the Witt ring',[612],
 'The question mark on37 concerns the map to the Witt ring and its characterization; its exact reach is uncertain.',
 'Use one λ-series convention, with Witt addition equal to series multiplication, and specify the p-typical projection before claiming uniqueness.',
 'Cartier1967 §§1–2 identifies generalized Witt and λ-ring operations and states the F,V laws; C2 independently checks the characteristicp identities. The remaining issue is the exact manuscript convention.',
 'Moderate editorial interest and high feasibility: identify the convention and rewrite the universal property without changing the source.')
add(123,'Admissibility and cohomology through limits',[613,614,615],
 'Scan40 marks the limit passage with a circled question and inserts that the proposed resolution may fail admissibility.',
 'Specify admissible objects and exactness in the chosen pro-category; compute finite étale coefficients by Frobenius coinvariants and retain H²(Fq,Z)=Q/Z for discrete Z.',
 'Serre1960 §§2–3 proves properties of his pro-quasi-algebraic category. The direct continuous-cohomology countercheck in C3 blocks the unrestricted constant-Z vanishing. No category-independent interchange theorem follows.',
 'High interest and high diagnostic feasibility: identify exactly which resolution leaves the admissible category.')
add(124,'Simplicial quotients and totalization signs',[619,620],
 'The interior-face quotient has a degeneracy reservation; scan64 asks “cosimplicial ?!” and the differential displays have inconsistent signs.',
 'Use the normalized cosimplicial adèle complex, prove a proposed quotient is stable under all required maps, and use a graded commutator differential with Θ²=0.',
 'Yekutieli2003 §1 supplies the standard adelic resolution, while C5 checks finite concatenation and refutes the printed unsigned totalization. The draft’s special quotient requires an additional compatibility proof.',
 'High interest and high short-run feasibility: a small-dimensional comparison can isolate whether the quotient is a variant of the standard complex.')
add(125,'Which topology makes the path algebra the right operator algebra?',[616,621,622],
 'Scans64–69 compare several topologies and a path/flag algebra with endomorphisms of the residue complex; convergence and the comparison remain unsettled.',
 'For finite-type schemes over a perfect field, compare a precisely specified Beilinson adelic DG algebra with its action on the residue complex; ask separately which continuous operators its image contains.',
 'Yekutieli2003 Theorem0.1 proves the action. Braunling–Groechenig–Wolfson2016 Theorems0.1–0.2 compare three specified operator algebras and identify higher local-field factors under excellence/reducedness. Full End equality for the manuscript’s unspecified topology is not thereby proved.',
 'Very high interest with moderate short-run feasibility: a two-dimensional flag can decide the correct topology and likely strength of the comparison.')
add(126,'Local Jacobian representing supported cohomology',[624,626],
 'Scans75–76 assert the local Jacobian universal formula after the scalar calculation; the canceled draft on72 questions the cohomological index.',
 'For a regular local ring over an algebraically closed field, first fix Zariski or flat cohomology and prove pro-representability on an explicitly small category of commutative groups; scalar local cohomology alone does not suffice.',
 'SGA2 gives local-cohomology concentration and its support shift; Serre1960 supplies a particular pro-category. Contou-Carrère2013 establishes the formal-curve universal property for commutative smooth targets over noetherian bases, a dimension-one result.',
 'Very high interest but limited few-hour reach: reconstruct the exact proposed functor and compare the dimension-one case before making a higher-dimensional claim.')
add(127,'The proposed Weil site and its derived direct images',[627,634],
 'Scan77 tentatively says the method works less well;92 questions the covering class and reduction conditions, and93 asks “Quels sont les foncteurs dérivés ??”.',
 'Choose a topology and a morphism of sites j first, then compute R^i j_* on specified coefficient classes; distinguish discrete étale coefficients from infinitesimal flat groups.',
 'The opened SGA1 and SGA3 results govern established étale and flat/formal categories, but do not identify this draft site. C6 refutes the unrestricted fppf vanishing of positive cohomology for linear groups. ClassificationF reflects underdetermination, not a claim of a currently unsolved theorem.',
 'High foundational interest with high first-step feasibility: a site dictionary may reveal that different drafts are being combined.')
add(128,'Purity or extension for radicial groups',[629],
 'Scan79 asks “[et si G est radiciel ? …]” and leaves the following cohomology map unfinished.',
 'State a finite flat purity or extension theorem with explicit regularity, codimension, cohomological degree and group-scheme hypotheses.',
 'SGA1 IX4.10 proves étale invariance under radicial universal homeomorphisms, which does not preserve αp as flat data. SGA3VIIA separates infinitesimal group schemes. The page does not yet determine one exact modern purity statement.',
 'Moderate interest and high clarification feasibility: extract the exact domain, puncture and coefficient before a theorem search.')
add(129,'The curve Jacobian complex and relative unipotent term',[630],
 'Scan80 marks spectral terms with questions;81–82 start an unfinished valuation-ring and relative unipotent construction.',
 'Define the curve/modulus complex with its degree piece, proper multiplicative homology and relative Witt term, then compare its cohomology with supported cohomology in a fixed category.',
 'Classical generalized Jacobians, Cartier1967 Witt operations and Contou-Carrère2013 formal-curve Jacobians establish components. No opened result identifies the entire unnamed complex with all the displayed spectral terms.',
 'High interest and moderate feasibility: reconstruct its two-term or three-term truncation before seeking a full derived model.')
add(130,'fppf, fpqc, perfect objects and limit continuity',[631,632],
 'Scan84 asks which functors commute with filtered ring limits and which flat coverings to use, then instructs calculations of Ext in the corresponding categories.',
 'Separate finite-presentation continuity from fpqc descent, and distinguish perfection of smooth groups from a category retaining nonreduced finite group schemes.',
 'EGAIV3 8.8.2–8.8.3 proves finite-presentation descent and Hom continuity; SGA1VIII proves descent; Serre1960 explicitly works with quasi-algebraic objects. Killing radicial phenomena changes the relevant Ext questions.',
 'High interest and high feasibility: an operational dictionary will prevent several false transfers between categories.')
add(131,'Exact shifts in the local duality formulation',[633],
 'Scans89–90 formulate local duality with supports and derived Hom, including canceled implications and uncertain shifts.',
 'For each specified coefficient category and regular local geometry, derive the shift from the localization triangle and the chosen dualizing object; retain finite/constructible and completeness assumptions.',
 'Tate1963 verifies arithmetic finite-coefficient duality with its own degrees; SGA2 verifies coherent local duality. These are not interchangeable, and the Pro43 support-duality claims supply the close manuscript comparison.',
 'Very high interest and high diagnostic feasibility: a regular one-dimensional test determines the first shift unambiguously.')
add(132,'Abelian-variety global duality and finiteness of Sha',[640],
 'Scan146 tentatively extends the finite-module global sequence to abelian varieties with a finiteness hypothesis on the Tate–Shafarevich group.',
 'State Cassels–Tate duality with its divisible kernels and write any full finite perfect pairing conditionally on the required finiteness; do not derive general Sha finiteness from formal analogy.',
 'Tate1963 §3 explicitly separates the pairing from conditional consequences. The run’s dated2026 search found no verified theorem removing the general finiteness hypothesis; inaccessible2026 preprints are not credited as settlements.',
 'High mathematical interest but low few-hour feasibility for the general conjecture; a conditional-statement audit is a tractable editorial task.')
add(133,'Retained finite-model Serre algebra versus actual monodromy',[643,644,645],
 'Scans151–156 build a field-independent algebra by retaining finite models while passing to large fields.',
 'Define the model system and identify its stabilized finite-model Lie algebra; distinguish it from Lie of the Galois image over an arbitrary infinite extension.',
 'EGAIV3 8.8.2 supports descent of finite diagrams; Serre1968 I§1.1 proves finite-type field-extension invariance. C11 shows actual monodromy can disappear over an algebraic closure, so the retained-model object is additional data.',
 'High interest and high feasibility: an explicit cyclotomic example tests the definition and its invariance without attempting a new general theorem.')
add(134,'Lie algebras and germs of subgroups',[646],
 'Scan158 asks when the subgroup/Lie-algebra construction has the proposed finiteness or openness consequences.',
 'Require a finite-dimensional l-adic analytic group and closed subgroup; under the stated elementwise power condition, the subgroup has full Lie algebra and is open.',
 'Serre1968 I§1.1 supplies the l-adic Lie setting. The logarithm proof in C11 verifies the restricted assertion; the compact torsion product demonstrates that general compactness is insufficient.',
 'Moderate interest and high feasibility: write the exact analytic lemma and document the hypothesis missing from the broader wording.')
add(135,'Height-one Hom cells with abelian targets',[649],
 'The αp/A and μp/A cells on162 retain deleted formulas and question marks;163 proposes Lie-kernel formulas.',
 'Over characteristicp, identify Hom(αp,A) with ker(x↦x^[p]) and Hom(μp,A) with ker(x↦x^[p]−x) in the restricted Lie scheme, preserving nonreduced structure.',
 'SGA3VIIA7.2 and8.1.1–8.1.2 establish the restricted-Lie adjunction and height-one correspondence. The field-point calculation alone would lose infinitesimal factors; the table audit records the functors.',
 'High explanatory interest and high feasibility: a supersingular and an ordinary elliptic example make the two kernels visibly different.')
add(136,'The four difficult internal Hom types',[650],
 'Scans162–163 flag Hom(Ga,αp), End(Ga), Hom(Ga,V), Hom(V,V), plus related αp/V and A/V cells, as difficult or uncertain.',
 'Use additive p-polynomials for End(Ga), coefficient equations a_i^p=0 for Ga→αp, and V=D(Ga) in formal Cartier duality; define Ga→V through bilinear characters rather than assigning it Ga.',
 'SGA3VIIB2.2.2 and4.2 give formal duality and Lie adjunction. C8 refutes the Ga identification by its field points, and the200-cell audit gives exact functor descriptions. The abbreviations Imm/Imm² remain an ink question.',
 'Very high editorial interest and high feasibility: a common functor convention resolves many apparent contradictions in the table.')
add(137,'Questioned unipotent geometric Ext entries',[652,680],
 'Scan164 asks for Ext¹(αp,αp), Ext¹(αp,Ga), Ext¹(Ga,αp), and Ext¹(Ga,Ga), and says to consult Serre for explicit calculations.',
 'Over algebraically closed characteristicp k: Ext¹(αp,αp)=k⊕k, the two mixed αp/Ga groups are k, and Ext¹(Ga,Ga)=k[F]e in geometric Yoneda extensions.',
 'Finite Dieudonné classification gives the two-parameter self-extension. Hazewinkel–Oort1972b Lemma2.1 supplies the Witt generator theorem; C16 checks the Frobenius deductions. Fanelli–Schröer2020 p8 directly confirms the αp/Ga dimension citing Oort1966.',
 'High explanatory value and high feasibility: the remaining work is to align scalar actions and manuscript notation, not to claim these geometric groups remain open.')
add(138,'Mixed extensions involving abelian varieties',[653,654,681],
 'Scan164 proposes finite-kernel expressions for the μp/A, αp/A, Gm/A and Ga/A cells, while leaving several entries or finiteness claims canceled or incomplete.',
 'Keep the direction of each extension fixed; prove the Ga/A reduction to A[p] separately, and identify the exact algebraic Yoneda category and finite-kernel transitions for the other cells.',
 'Barsotti–Weil and additive extensions in the opposite direction are verified through Ribeiro–Rosengarten. C16 proves Ext¹(Ga,A[p])≅Ext¹(Ga,A). Oort1966 chapters13–14 are a verified bibliographic destination, but its inaccessible exact mixed-cell theorem text is not treated as read. Oort–Oda1968 concerns Ext² of abelian varieties, not these degree-one cells.',
 'Very high interest and moderate feasibility: checking Oort’s exact table against the original arrows is a sharply bounded next task.')
add(139,'Higher Ext and the canceled nonvanishing note',[654],
 'Scan164 cancels an uncertain Ext² note and asks for explicit extension calculations; the canceled sentence is not a live conjecture.',
 'Separate algebraic Yoneda Ext from internal fppf Ext and compute only after fixing both arguments, base and degree.',
 'Oort–Oda1968 proves Ext²_alg(A,B)=0 over algebraically closed positive-characteristic fields. Ribeiro–Rosengarten2026 TheoremB proves internal Ext²(A,Gm)=0 over every base, while recording higher-degree nonvanishing. Thus neither blanket higher vanishing nor blanket nonvanishing is justified.',
 'High editorial value and high feasibility: a category-by-degree comparison removes a recurrent source of mistaken conclusions.')
add(140,'Associativity, unit and inverse for a primitive torsor',[655],
 'Scan169 lists the checks of associativity, unit and existence of a symmetry; the first two are argued and the inverse is referred to Serre p183.',
 'Under normalized rigidity for G^r→γ, r=1,2,3, a pointed primitive γ-torsor has a unique commutative extension structure; retain flatness and torsor hypotheses.',
 'The page’s proof is substantial. C9 independently completes the inverse/commutativity argument. Ribeiro–Rosengarten TheoremA confirms the role of analogous rigidity conditions. The exact Serre page183 was not accessible, so that bibliographic endpoint remains unverified.',
 'Moderate research interest but high editorial value: present the finished proof and identify precisely where each rigidity hypothesis enters.')
add(141,'Perfection in the Artin–Schreier Ext formula',[657],
 'Scan170 displays a perfection formula and an uncertain parenthesis that may reserve additional noetherian hypotheses.',
 'Over perfect k, primitive Artin–Schreier extensions give Ext¹(Ga,Z/p)≅k; over a general base state the sheaf/perfection and base-change formulation before extending the formula.',
 'Grothendieck’s Chevalley exposé7 pp8–9 contains the primitive-polynomial argument. The perfect-field calculation is checked in C9; the unreadable qualifier prevents an unrestricted relative theorem from being attributed to the sheet.',
 'High interest and high feasibility for clarifying the exact relative formulation; ink verification remains essential for the parenthesis.')
add(142,'Extension of F/V classification to infinite objects',[658],
 'Scan173 questions implications between F,V monicity/epicity/invertibility, asks whether V is unipotent, and hopes the following tables remain essentially valid;180 questions a rational-point condition.',
 'Use finite-type/perfect-field or finite-height hypotheses for each row and distinguish local nilpotence from a uniform exponent on infinite ind/formal objects.',
 'SGA3VIIA–VIIB establish finite infinitesimal and formal-group frameworks. They do not automatically justify all ind/pro extrapolations; C14 supplies a concrete failure of uniform nilpotence.',
 'High interest and moderate feasibility: a row-by-row category dictionary is tractable, while a general glued classification is a separate project.')
add(143,'Gluing formal and algebraic Dieudonné categories',[659,671,672],
 'Scan183 asks how to glue, what finite-type modules over the displayed ring mean, and suggests an endomorphism interpretation;197–202 return to reasonable formal modules.',
 'Fix covariance, the completed Dieudonné ring, admissible modules and topology; construct an exact comparison with an explicitly defined category of commutative formal/algebraic extensions.',
 'SGA3VIIB provides formal groups and hyperalgebras; Oort–Oda1968 p82 states a precise completed Dieudonné ring; Gabriel1962 provides the abelian-category framework. These cover ingredients, not an automatic interpretation of every draft completion.',
 'Very high conceptual interest but moderate few-hour feasibility: write a functor and test it on finite local-local groups before any general equivalence.')
add(144,'Affine group approximation over a field',[660],
 'Scans185–186 ask whether an affine group is pro-algebraic and whether its Hopf algebra is built from finite subcoalgebras;192 answers the field case.',
 'Over a field, use finite-dimensional subcoalgebras and finitely generated Hopf subalgebras; for groups the Hopf closure includes antipodes.',
 'SGA3VIB11.13 and MilneAGS VIII4.6,8.1–8.2 give the field theorem. C12 rechecks the finite-coefficient proof. This is a resolved question on the later sheet, not an outstanding research problem.',
 'Low research novelty but high editorial priority: merge the earlier question with its later affirmative resolution.')
add(145,'Finite coalgebra approximation over arbitrary rings',[661],
 'Scans186 and191–192 ask whether the finite-rank-coalgebra condition is superfluous and suggest broader hypotheses such as A free.',
 'Formulate local finiteness with explicit purity, finite projectivity and tensor-injectivity conditions; distinguish it from mere existence of cofree coalgebras or finite-presentation approximation of affine schemes.',
 'Barr1974 proves general coalgebra existence results. Kihara2016’s opened abstract states local finiteness for projective corings over semihereditary bases. Neither the field theorem nor those hypotheses settle the exact unrestricted free-over-ring wording.',
 'Very high interest and moderate short-run feasibility: locate or construct the first tensor-purity obstruction for one chosen nonnoetherian base.')
add(146,'Topological hyperalgebras and Cartier duals over rings',[662],
 'Scan187 considers interpreting further topological hyperalgebras, and188–189 explicitly says that the required topology/coalgebra condition is not guaranteed.',
 'Over an artinian base, impose topological flatness and use the pseudocompact dual; over more general rings identify the necessary projective or reflexivity hypotheses.',
 'SGA3VIIB2.2.1–2.2.2 proves the formal/affine duality with those conditions. Álvarez–Sancho–Sancho2007 gives a functorial version under its specified hypotheses. The source’s conditional general-ring step remains conditional.',
 'High interest and moderate feasibility: translate one topological algebra on the page into the exact SGA3 hypotheses.')
add(147,'Does artinianity make ordinary limits fully faithful?',[664,665],
 'Scan191 asks whether artinian objects suffice for Pro(C)→C′ to be fully faithful.',
 'Include continuity in the target realization, or use the appropriate pro-Yoneda embedding; artinianity alone does not control maps of underlying limits.',
 'C12 gives Pro(FinSets)→Sets as a complete counterexample, with an abelian-vector-space variant. Serre1960 and Gabriel1962 supply the correct pro/Ind setting. The literal sufficient condition is refuted.',
 'High editorial value and high feasibility: record the counterexample and replace the vague criterion by the exact category needed for group schemes.')
add(148,'Is the proposed extension category abelian?',[667],
 'Scan193 says one wants to combine the categories by extensions and calls the result “présumée abélienne”.',
 'Specify objects, admissible ind/pro systems and morphisms; prove kernels and cokernels exist in that category and that image and coimage agree.',
 'Serre’s pro-quasi-algebraic groups, SGA3 formal groups and Oort’s algebraic groups are established but distinct categories. The page does not fix which extension completion is meant, so no exact theorem can yet be identified.',
 'Very high conceptual interest, limited few-hour reach beyond a precise definition and elementary closure tests.')
add(149,'The action on U and reasonable Dieudonné modules',[671,673],
 'Scan199 circles an uncertain “décrire/définir l’action de A ??”; nearby sheets sketch reasonable modules and finiteness conditions.',
 'Give the module action with one covariance convention, retain the injective-hull assumptions used in the artinian argument, and require elementwise F,p nilpotence on the union U.',
 'Oort–Oda1968 and SGA3VIIB provide precise module settings. C14 verifies the displayed normal forms and refutes a uniform nilpotence reading. Gabriel1962’s actual finite-length hypotheses cannot be replaced by the false socle criterion on196.',
 'High interest and high feasibility for a convention/action audit, with a broader equivalence deferred to a separate task.')
add(150,'Picard–Brauer construction in the preliminary Tate sketch',[674,675],
 'Scan204 labels the argument “schéma préliminaire”;205 forms the torsor/Picard obstruction pairing.',
 'Use the Poincaré biextension to define H¹(S,A)×A∨(S)→H²(S,Gm), keeping the difference between relative Picard points and actual line bundles.',
 'Tate1963 gives the duality interpretation, and Ribeiro–Rosengarten TheoremA verifies the extension-sheaf description. The degree-one pairing remains valid without an unjustified all-degree RHom concentration.',
 'High explanatory value and high feasibility: give the obstruction map with explicit descent data and compare it to the Yoneda product.')
add(151,'Complete cohomology for finite coverings',[676],
 'Scan205 says “Il semble, quand S′ est fini sur S” and proposes pairings that “il faudrait comprendre”.',
 'Start with a finite Galois covering and its finite group action for Tate cohomology; a general finite flat morphism requires a separately defined norm/descent complex.',
 'Tate1963 uses complete cohomology with finite group actions. SGA1 gives the covering/descent setting. Neither supplies a complete cohomology theory from finiteness of a morphism alone.',
 'High interest and moderate feasibility: formulate and test the finite-Galois case before exploring a finite-flat generalization.')
add(152,'Independence of the final Albanese-kernel pairing',[677,678,679],
 'Scan208 announces invariance after replacing the Poincaré divisor by a principal modification and stops at “on obtient”.',
 'Carry a compatible rational section or biextension trivialization when changing the divisor; verify the resulting cancellation on the specified Albanese-kernel cycles, with strict local units where used.',
 'Deligne1991 §1 and Tate1963 support normalized local/biextension pairings. C15 computes the uncanceled h(z) factor and the ordinary-unit counterexample. No exact completion of this last manuscript formula was found in the opened sources.',
 'Very high interest and high feasibility: finish the choice-independence calculation after stating all normalization data.')

(out/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'problems':len(problems),'first':problems[0]['id'],'last':problems[-1]['id'],'authorial_flags_only':True}))
