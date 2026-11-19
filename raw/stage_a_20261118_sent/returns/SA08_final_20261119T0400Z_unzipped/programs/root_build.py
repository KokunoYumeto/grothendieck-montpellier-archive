"""Serialize the individually authored Codex claim/problem/reading adjudications.

This program does not infer claims, verdicts or fates from headings or keywords.
The full three Codex transcriptions were read before these records were written.
"""
import json,csv,pathlib,datetime
R=pathlib.Path(__file__).resolve().parents[1];O=R/'work/root';O.mkdir(exist_ok=True)
claims=[];problems=[];readings=[];links=[];events=[]
WHO='GPT-6 Astra Pro; effort not exposed by runtime; SA08/root'
DATE='2026-11-19'
def add(n,folder,scans,lines,his,statement,status,comp,cls,fate,date,refs,confidence='high',event='used and rechecked in this run'):
 ident=f'SA08-C{n}'
 claims.append(dict(id=ident,items=[],cote=136,scans=scans,lines=[{'file':f'codex/{folder}_transcription.tex','lines':lines}],his_statement=his,statement=statement,status_on_pages=status,computation=comp,**{'class':cls},fate=fate,fate_date=date,present_status=f'As of November 2026: {fate.split(" Search:")[0]}',refs=refs,confidence=confidence))
 events.append([ident,DATE,WHO,event,comp+' | '+status+'; the source match is not a wholesale re-proof of the cited theorem.'])

add(901,'K136-01',[328],'2–54','The half-class equation is cancelled; the degree is left as 2g−2 / g−1 alternatives.',
 'For a Fuchsian surface representation in PSL2(R), the Euler number has magnitude 2g−2. On a lift to SL2(R), the defining oriented two-plane representation has half that Euler number because the projective boundary action doubles the circle weight. Orientation fixes the sign. No canonical choice of lift or algebraic splitting is implied.',
 'open on the pages; competing normalization, with a cancelled equation at line21',
 'codex_proof_checks.md §3 and the elementary circle-cover calculation: z↦z² pulls the Euler generator back to twice itself. No numerical claim about a chosen orientation is certified.',
 'E','The circle-weight distinction is classical; the manuscript has not fixed which bundle its symbol names. The contemporary oper/jet interpretation of326–327 is a separate restricted comparison. Search: primary flat-bundle/oper sources, late package literature audit; root_web_015–024 for the connected mathematical setting.',
 {'known_before':'1975','manuscript_date':'not independently fixed'},['BHR2021'],'medium','targeted proof check')
add(902,'K136-01',[329,332],'55–103;161–206','F(M)=Hom(A,M); compatible tensor products correspond to a coalgebra law on A.',
 'For k-modules, a coassociative counital comultiplication on A defines the convolution lax monoidal structure on Hom_k(A,−). Associativity, unit and symmetry correspond to coassociativity, counit and cocommutativity. This is not a PD structure by itself.',
 'proof sketched','codex_proof_checks.md §1; substitute Δ into (f⊗g)Δ and compare the two triple composites. Yoneda recovers Δ from the universal value.',
 'E','The ordinary convolution/Yoneda statement is standard. Roby supplies polynomial-law language for the extra operations, with no automatic upgrade from an arbitrary coalgebra. Search: root_web_022–024; Roby1963 ChaptersIII–IV.',{'publication':'1963 antecedent'},['Roby1963','Kelly1982'],'high','targeted proof check')
add(903,'K136-01',[329,330,332,333],'73–154;161–268','Additional maps u_p:A→Γ^p(A) are required to be compatible with multiplication and composition.',
 'The proposed enrichment is a family of natural degree-p polynomial operations on the representable functor Hom(A,−), with prescribed product and iterated-PD compatibilities. Roby represents each homogeneous law by Γ^p; coherence is additional data. General existence and uniqueness are not consequences of the ordinary coalgebra structure.',
 'open on the pages','codex_proof_checks.md §1; coefficient tests in root_checks.json/334_nested_PD. The literal rank-one nonuniqueness example on324 is in late/proofs.md; it does not refute stronger naturality requirements.',
 'C','Polynomial-law representability and flat convolution cases are developed; the exact manuscript family with all requested universal compatibilities is not identified with a later classification theorem. Search: root_web_022–024, Roby1963 IV.1, later divided-power/coalgebra searches and the late package audit.',{'antecedent':'1963','exact_full_statement':'no matching publication located'},['Roby1963','StacksPD'],'medium')
add(904,'K136-01',[330,331],'104–160','The Sym-based construction is struck through;331 contains only a fragment.',
 'Over a Q-algebra symmetrization identifies symmetric invariants/coinvariants and divided powers, using factorial denominators. This argument cannot be used integrally. The struck-through construction is withdrawn, not an asserted integral theorem.',
 'corrected by himself later on the same leaf: lines126–151 are cancelled;331 does not complete it',
 'The n=2 invariant/coinvariant comparison multiplies the rank-one generator by2. Reduction mod2 makes this noninvertible; standard factorial comparison in codex_proof_checks.md §1.',
 'E','The rational comparison is standard; its integral limitation was already part of divided-power theory. No fate is assigned to the cancelled sketch as if it were a theorem. Search: root_web_014,022–024; Roby1963 III–IV and Stacks23.2.',{'publication':'1963 antecedent'},['Roby1963','StacksPD'])
add(905,'K136-01',[333,334,335],'207–377','F(J)→F(A) is questioned; the polynomial-law extension is meant to preserve PD axioms.',
 'For F=Hom_k(A,−), an ideal inclusion remains injective. For a general additive F, preservation of monomorphisms is a separate condition. A functor on homogeneous polynomial laws satisfying identity, composition, sums and the specified multiplicative compatibility transports a PD system; additivity alone does not.',
 'proof sketched, with an explicit monomorphism question at334',
 'codex_proof_checks.md §1: left exactness of Hom checked elementwise. The proposed transport is conditional on each displayed compatibility, not proved for arbitrary F.',
 'C','The Hom subcase and universal representation of polynomial laws are established; the manuscript broadens F without supplying all exactness/coherence hypotheses. Search: root_web_014,022–024; Roby1963 IV.1 and III.3–4.',{'antecedent':'1963','general_unqualified_version':'not valid'},['Roby1963','StacksPD'],'high','targeted proof check')
add(906,'K136-01',[333,334,335],'227;317;349–351','γ^p(γ^q x) is assigned denominator (p!)^q q!; a later line writes λ^p x^p.',
 'The corrected nesting coefficient is (pq)!/[p!(q!)^p]. Scalar homogeneity is γ_p(λx)=λ^pγ_p(x). The transcribed nesting denominator belongs to the reversed order, and the missing divided-power parentheses change the scalar formula.',
 'false as transcribed; no manuscript ink decision',
 'root_checks.json/334_nested_PD gives10 versus15 at(p,q)=(2,3); codex_proof_checks.md §1 proves the universal integral identity and checks the product expansion.',
 'E','The correct axioms are known before these notes. The exact coefficient discrepancy is a reading alarm, not a new conjecture. Search: root_web_014,022; Stacks Definition23.2.1(3),(5), Roby1963.',{'antecedent':'Cartan1954–55 / Roby1963'},['StacksPD','Roby1963'],'high','refuted, refined statement in SA08-C906 statement field')
add(907,'K136-01',[337],'381–441','rg(Γ^pΦ_[N]⊗Λ^qΨ_[N])=C_pq binom(N+p,p+q); τ^(p−1) is uncertain.',
 'For free ranks N+1,N, the rank equals binom(N+p,p)binom(N,q)=binom(p+q,p)binom(N+p,p+q). For p≥1 the latter binomial expands by Pascal with coefficients binom(p−1,j) at N+1. These are rank equalities; a natural decomposition of objects is a separate claim.',
 'proved there for the numerical calculation; the object decomposition is tentative',
 'root_checks.json/337_rank_and_shift:1377 rank cases,1080 shift cases; codex_proof_checks.md §2 gives the factorial/Pascal proof.',
 'E','The numerical identities are standard and correct with p−1; the suggested representation-theoretic decomposition is not established by them. Search: root_web_014,019,022 and Roby1963 basis theoremIV.2; BMT2016 for distinct derived decompositions.',{'antecedent':'1963 basis theorem'},['Roby1963','BMT2016'],'high','independent re-proof')
add(908,'K136-01',[338,341],'442–517;636–683','C^m_n is rank one in n=m,m+1; a displayed exterior term has no normalization mark.',
 'Normalized Λ^rΨ has one rank-one term in degree r; normalized Λ^rΦ has rank-one terms in degrees r−1,r. Unnormalized Λ^(m+1)k^(m+2) has rankm+2. The case conditions at341:678 need normalization and consistent indexing.',
 'proof sketched, with conflicting cases and an unnormalized rank expression',
 'root_checks.json/338_341_normalized_ranks gives56 exact matrix-rank checks; codex_proof_checks.md §3 separates the normalized and unnormalized objects.',
 'E','Dold–Kan and the exterior models are classical. The precise transcription cases cannot all be true as printed. Search: root_web_014,016–017,019; DoldPuppe1961 §3 and Stacks019G.',{'publication':'DoldPuppe1961'},['DoldPuppe1961','StacksDoldKan'],'high','computation or formal certificate')
add(909,'K136-01',[339,340,342],'518–635;684–744','F_X(M)=Hom(X,M); transformations to the simplex functor recover X.',
 'For all simplicial k-modules, F_X is represented by k[X], and Nat_k(F_X,F_Δn)=Hom(k[Δn],k[X])=k[X_n]. This exact Yoneda statement is valid for infinite X as well. It must not be replaced by a claim about all maps between restricted cochain realizations.',
 'proof sketched','codex_proof_checks.md §3: evaluate a transformation at id_k[X], then recover it by naturality; no finite duality is needed.',
 'E','Enriched Yoneda gives the exact full-functor statement. Restricted operation/cochain reconstruction remains a different problem. Search: root_web_022–024 and Kelly1982 §§1.9,5.35 (late source audit).',{'antecedent':'Yoneda1950s; exposition1982'},['Kelly1982'],'high','independent re-proof')
add(910,'K136-01',[339],'528–587','An arbitrary k-additive F is said to be determined by the C^i.',
 'A determination theorem needs continuity/density conditions or a restricted functor category. Over a field, evaluation followed by identity and algebraic double dual agree on finite-dimensional tests but differ on infinite-dimensional values; mere additivity is insufficient.',
 'false as an unrestricted assertion',
 'codex_proof_checks.md §3: the identity→double-dual example is additive, agrees on finite free test values, and fails for an infinite-dimensional vector space.',
 'C','Classical density gives repaired versions under colimit-preservation. The exact unrestricted wording is false; no later theorem can settle that wording affirmatively. Search: root_web_022–024; Kelly1982 free-cocompletion results; comparison Mandell2006 has wholly different E∞ hypotheses.',{'density_antecedent':'before1975','modern_comparison':'2006'},['Kelly1982','Mandell2006'],'high','refuted, refined statement in SA08-C910 statement field')
add(911,'K136-01',[339,340,341,342],'575–744','The calculation reaches a bidual k^(X_n)→Hom(Hom(k^(X_n),k),k).',
 'Finite-dimensional duality identifies the two expressions over a field; infinite algebraic biduality does not. Cochain reconstruction must retain a continuous dual/topology, finite-projective hypothesis, or the original representable functor. This is an obstruction to the proposed shortcut, not to Yoneda.',
 'open on the pages; the bidual issue is visible in the calculation',
 'codex_proof_checks.md §3; distinguish direct sums from products and algebraic from continuous duals. No unjustified reflexivity assumption is used.',
 'C','Finite and continuous versions are classical; homotopy reconstruction from E∞ cochains is established only under its own finite-type/nilpotence hypotheses and does not prove this bare PD/cochain assertion. Search: root_web_003–013 (Mandell),022–024 and Kelly1982.',{'Mandell_first_circulation':'2003-11-03','Mandell_publication':'2006'},['Kelly1982','Mandell2006'],'high','targeted proof check')
add(912,'K136-02',[343],'2–62','Multiplicative natural maps are intended to recover maps of spaces.',
 'For diagonal free coalgebras over a nonzero connected commutative ring, counital coalgebra maps are set maps, degreewise and compatibly in the simplicial setting. Over a disconnected ring orthogonal idempotent combinations are additional group-like elements. This does not assert that a truncated list of cochain operations already characterizes all natural maps.',
 'open on the pages; unrestricted coefficient statement would be false',
 'root_checks.json/343_disconnected_base; codex_proof_checks.md §3 proves the coefficient equations and checks F2×F2 with two distinct basis elements.',
 'E','The connected-base refinement follows from the elementary group-like calculation; broader homotopy recovery belongs to more structured later theories. Search: root_web_022–024 (coalgebras), Mandell2006 comparison.',{'classical_refinement':'before1975','comparison':'2006'},['Kelly1982','Mandell2006'],'high','independent re-proof')
add(913,'K136-02',[343],'35–49','colim Hom→Hom(lim…) is marked Iso?',
 'Interchange of Hom with a filtered colimit requires the appropriate finite-presentation/compactness condition on the argument. An infinite direct sum mapping identically into the union of its finite partial sums does not factor through one partial sum.',
 'open on the pages','codex_proof_checks.md §3 gives the explicit infinite-direct-sum counterexample. It refutes an unrestricted affirmative answer, not a specified finite subcase.',
 'E','Compactness and Kan-extension formulations are established. The actual source/target limits must be reconstructed before applying them. Search: Kelly1982 §§4.13,4.50–51 in late source audit; root_web_022–024.',{'exposition':'1982','antecedent':'classical'},['Kelly1982'],'high','targeted proof check')
add(914,'K136-02',[345],'63–105','An affine-simplex torsor and its colimit realization are compared; the homotopy assertion has a question mark.',
 'The simplex affine space is a torsor for the rank-m quotient Ψ_m, after choosing the dual convention. A chosen origin trivializes it; no canonical origin is implied. A homotopy comparison for a colimit over all simplices requires a specified realization functor and weak-equivalence claim, absent here.',
 'open on the pages','codex_proof_checks.md §4 verifies rankm and the role of an origin. No unspecified realization is certified.',
 'F','The elementary torsor is identifiable, but the intended general comparison does not determine a unique theorem. Search: DoldPuppe1961, Sullivan1977 realization, Kelly1982, root_web_014–024; no exact hypothesis-complete match located.',{'identification':'insufficient data as of2026-11'},['DoldPuppe1961','Sullivan1977','Kelly1982'],'medium')
add(915,'K136-02',[345],'106–142','The circle is expressed by an equalizer and a complex k→k with zero arrow.',
 'For the standard simplicial circle with one vertex and one nondegenerate edge, normalized chains and cochains have k in degrees0,1 and zero differential. This finite example is compatible with the equalizer description.',
 'computation sketched','codex_proof_checks.md §4: both endpoints of the nondegenerate edge are the unique vertex, so the boundary is v−v=0.',
 'E','This is a standard simplicial calculation, with no consequence for the unrestricted realization conjecture. Search: DoldPuppe1961 §3, Stacks019G; root_web_014,016–017.',{'antecedent':'before1975'},['DoldPuppe1961','StacksDoldKan'],'high','independent re-proof')
add(916,'K136-02',[346],'143–250','dδ+δd=Θ; δλ+λδ=μ_T; dμ_f−μ_fd=μ_f′λ and weight commutators.',
 'On a free divided-power de Rham algebra, d is the PD derivative, δ Euler contraction, λ wedge with dT, μ multiplication in Γ(T), and Θ total weight. The listed anticommutators and commutators hold. They give a spanning/reordering system, not by themselves linear independence of normal forms.',
 'proof sketched; normal-form independence not proved',
 'root_checks.json/346_PD_Koszul_operators:1596 exact identities; codex_proof_checks.md §5 gives the generator/derivation proof over Z.',
 'E','These are the PD form of the standard Cartan/Koszul identities. Modern derived PD treatments preserve the total-weight condition. Search: Roby1963, BMT2016 Prop6.6, Cartan1955; root_web_014,019–024.',{'antecedent':'1954–55 and1963','modern_exposition':'2016'},['Roby1963','BMT2016','Cartan1955XI'],'high','independent re-proof')
add(917,'K136-02',[346],'251–316','A return arrow for Γ^pΦ⊗Φ→Γ^pΦ⊗Ψ is marked ?; the final sum contains Σq_α.',
 'The displayed derivative-style lift projects to p times the identity in weightp. It becomes a right inverse after division byp whenp is a unit. The formula is not a universal integral splitting, and the page does not prove another one.',
 'open on the pages; the displayed formula fails as an unscaled right inverse',
 'root_checks.json/346_proposed_splitting uses(q1,q2)=(2,1), yielding3 and hence0mod3. codex_proof_checks.md §5 proves the factorΣqα=p.',
 'C','The p-invertible repair is immediate; integral splitting and naturality require separate arguments. Search: BMT2016 Koszul/PD complexes and root_web_019–024; no exact general natural splitting theorem located.',{'partial_result':'classical whenp invertible','general_integral':'not settled by matched sources'},['BMT2016','Roby1963'],'high','targeted proof check')
add(918,'K136-02',[348,350],'317–373;402–439','Definition of a demi-algèbre différentielle; products have a closed factor.',
 'Under the written Leibniz, graded-commutativity and two-closed-factor associativity axioms, the partial product descends to an associative graded-commutative product on cohomology. Strict odd-square vanishing requires the written extra axiom. This conclusion does not construct the partial products for the proposed universal model.',
 'definition and proof sketched','codex_proof_checks.md §6 proves well-definedness by(da)z=d(az), then associativity on cycle representatives.',
 'D','The elementary cohomology consequence is verified here. Exact half-dga searches found no later treatment matching all of this leaf’s axioms and universal model; this is a bounded negative identification, not a novelty claim. Search: root_web_019,022–024, Cartan1976 and Cenkl1989 for distinct partial/weighted multiplicative solutions.',{'searched_through':'2026-11-19','exact_literature_match':'not located'},['Cartan1976','Cenkl1989'],'medium','independent re-proof')
add(919,'K136-02',[350],'402–439','0→kT→Φ→Ψ→0; C^i=Λ^(i+1)Φ and Z^i≃Λ^iΨ.',
 'For the simplex extension, or a locally split rank-one extension with flat quotient, wedge byT gives the exact exterior complex. Cycles identify with Λ^iΨ through T∧− with the indicated degree shift.',
 'proof sketched','codex_proof_checks.md §6: useΦ=kT⊕Ψ locally, split each exterior power into two summands, and identify the differential. Flatness/local splitting are retained.',
 'E','This is the standard Koszul/exterior resolution, within the stated flat/split hypotheses. Search: Roby1963, BMT2016 Prop6.6 andRemark6.7; root_web_019–024.',{'antecedent':'before1975','modern_source':'2016'},['BMT2016','Roby1963'],'high','independent re-proof')
add(920,'K136-02',[352],'459–481','Can the product on cycles be extended? The ambiguity is Hom(Z^(i+1)⊗Z^j,Z^(i+j)).',
 'Under tensor exactness, a lift of the cycle product has an Ext¹ obstruction. If that obstruction vanishes, the possible lifts form a torsor under the displayed Hom group. Associativity, graded symmetry and naturality impose further conditions. The Hom group alone is not an existence proof.',
 'open on the pages','codex_proof_checks.md §6 derives the obstruction and torsor from the Hom long exact sequence. No value of the obstruction for the full universal model is invented.',
 'C','The obstruction-theoretic framework is standard. The exact universal half-dga extension is not matched to a theorem. Cartan/Cenkl solve different weighted multiplicative problems, and Cenkl’s strict-cochain obstruction cannot be applied without checking its axioms. Search: root_web_014,019,022–024.',{'framework':'classical','exact_model':'not identified as settled by2026-11'},['Cartan1976','Cenkl1989','Kelly1982'],'medium','targeted proof check')
add(921,'K136-02',[349,351],'374–401;440–458','English donor: Heisenberg matrices, nonabelian periods, and an iterated-integral correction.',
 'Closed1-formsω1,ω2 andη withdη=ω1∧ω2 define the triangular flat connection with the appropriate sign. Its path holonomy has the Heisenberg product; the iterated integral supplies the cross term. All diagonal entries are1. The bottom-right0 at349 would make the matrix singular.',
 'proof sketched in reused English typescript; matrix reading at349 is false',
 'codex_proof_checks.md §7 checks determinant, matrix multiplication, flatness and the path-concatenation cross term.',
 'E','The exact donor belongs to Sullivan’s Differential Forms and the Topology of Manifolds, Tokyo1973 proceedings published1975; the author’s typescript and bibliography were opened. It is not a new Grothendieck result. Search: root_web_024 and early Sullivan source audit.',{'conference':'1973','publication':'1975','typeset_draft_circulation':'no separate exact date established'},['Sullivan1975'],'high','targeted proof check')
add(922,'K136-02',[353],'482–501','English donor Theorem D identifies the smooth model with the rational model tensored with R.',
 'For a smooth manifold with the required finite-type triangulation, the smooth de Rham and real piecewise-polynomial models are quasi-isomorphic and have isomorphic minimal models. Interpreting the model as the full real/rational homotopy type requires nilpotent finite-type hypotheses (in particular the simply connected case stated on the leaf). Separately, the finitely generated torsion-free nilpotent quotients of the fundamental group embed as lattices in their real Malcev completions. The nilmanifold example is not the entire scope of TheoremD.',
 'proof sketched on this donor leaf using smooth triangulation, three cohomology models and uniqueness; part of Sullivan’s text',
 'Sullivan author typescript PDFp8 matched word-for-word to scan353; the three-algebra diagram and uniqueness argument are present. No finite arithmetic computation underlies the model theorem. Distinguish the cdga comparison, its nilpotent homotopy interpretation and the following lattice assertion.',
 'E','Sullivan’s Tokyo lecture text supplies the exact earlier statement; the systematic rational-homotopy exposition is Sullivan1977. Search: root_web_024 and early donor collation, root_web_003–013 Sullivan1977.',{'conference':'1973','publication':'1975; expanded treatment1977'},['Sullivan1975','Sullivan1977'])
add(923,'K136-02',[355],'502–595','Universal additive cocompletion and an adjoint diagram are explored.',
 'For a small k-linear category, its category of k-linear presheaves has the appropriate free cocompletion property; extension and restriction are related by Kan adjunctions when their size/existence hypotheses hold. The page’s partly drawn target categories do not identify every displayed arrow uniquely.',
 'proof sketched; some arrows are not specified','Yoneda/Kan universal-property argument, with variance and size conditions retained; late/proofs.md §9 and codex_proof_checks.md §3.',
 'E','Kelly1982 Th5.35 and §§4.13,4.50–51 give the exact categorical framework. It does not by itself settle the extra PD operation language. Search: late Kelly audit; root_web_022–024.',{'publication':'1982 exposition of earlier category theory'},['Kelly1982'],'medium','targeted proof check')
add(924,'K136-02',[357,358,360],'596–743;842–892','Eilenberg–Zilber–Cartier comparison; shuffle is commutative, Alexander–Whitney is not.',
 'Normalized chains of the diagonal of a multisimplicial object and the total normalized multicomplex are naturally chain-homotopy equivalent. Shuffle is associative and symmetric with Koszul signs; AW is coassociative and generally not symmetric. These maps provide the cup product and K(A,i)⊗K(B,j)→K(A⊗B,i+j).',
 'reviewed with proof sketches; the explicit AW sign needs correction',
 'root_checks.json/357_AW_sign checks the first nontrivial chain identity; codex_proof_checks.md §8. Higher theorem matched to DoldPuppe1961 §2 and Breen1978 Th2.16, not reproved wholesale.',
 'E','The comparison and its natural homotopies were known before these notes; Breen1978 gives a precise later formulation including Cartier’s multisimiplicial version. Search: root_web_014,017,024.',{'antecedent':'DoldPuppe1961','later_exposition':'Breen1978'},['DoldPuppe1961','Breen1978','SchwedeShipley2003'],'high','targeted proof check')
add(925,'K136-02',[357],'641–652;697–706','h′−h=dm+md for a next homotopy; AW includes an extra(−1)^i.',
 'With homological degree conventions, a degree2 homotopy has differentialdm−md. Standard AW has no additional(−1)^i in its front/back sum. A different convention must be specified before retaining either transcribed sign.',
 'false under the conventional differential used in this check; ink/convention unresolved',
 'codex_proof_checks.md §8 derivesDh=dh−(−1)^|h|hd; root_checks.json/357_AW_sign exhibits boundarydifference2((0,1)−(1,1)) overZ.',
 'E','The corrected signs follow from the standard Hom/tensor differential and Eilenberg–Zilber formulas. Search: DoldPuppe1961 §2, Breen1978 §II; root_web_014,017,024.',{'antecedent':'1961 or earlier'},['DoldPuppe1961','Breen1978'],'high','refuted, refined statement in SA08-C925 statement field')
add(926,'K136-02',[360],'842–892','The Hom complex is first asserted acyclic “pour tout X”, then changed to “pour X variable”.',
 'A complex of natural cochain operations can be resolved by acyclic models. The endomorphism complex for one fixedX need not be acyclic: its identity acts nontrivially on any nonzero cohomology. The correction changes the quantifier and the object.',
 'corrected by himself later: line880 versus889',
 'codex_proof_checks.md §8: chooseX=S¹, whose identity induces the identity onH¹ and cannot be null-homotopic. The natural-operation theorem is source-matched separately.',
 'E','The amended acyclic-model setting is classical; the withdrawn fixed-space formulation is false. Search: DoldPuppe1961 §2, Breen1978 Th2.16 and SteenrodEpstein1962 construction chapters; root_web_014–024.',{'antecedent':'1962 or earlier'},['DoldPuppe1961','Breen1978','SteenrodEpstein1962'],'high','targeted proof check')
add(927,'K136-02',[359,360],'744–892','W_n=Z[EΣ_n] and higher commutativity homotopies act on tensor powers.',
 'A free group-ring resolution and an equivariant acyclic-model operation construction produce the higher cochain operations in each arity. To infer an E∞ algebra one must additionally check compatible operadic composition across arities. The displayed sketches alone do not perform that check.',
 'proof sketched for aritywise operations; full coherence not established on the pages',
 'The bar resolution is contractible before taking coinvariants by inserting the identity in the free simplicial model; action freeness is direct. No whole-operation-complex freeness or operadic coherence is inferred from that contraction.',
 'C','Classical Steenrod constructions and later E∞ models provide established arity/coherence theories, but the manuscript sketches are not identified with a fully verified operad action. Search: root_web_014–024; SteenrodEpstein1962, Breen1978, Mandell2006.',{'operations':'by1962','homotopy_reconstruction':'2003 preprint/2006 publication'},['SteenrodEpstein1962','Breen1978','Mandell2006'],'medium','targeted proof check')
add(928,'K136-02',[361],'893–912','A signed formula definingP^i has its sign exponent left blank;Σ_n andΣ_p are interchanged.',
 'The operation is intended to use a p-fold equivariant construction and a cyclic subgroup ofΣ_p. Without the omitted exponent and consistent arity, the exact cochain formula is not specified.',
 'open on the pages; formula incomplete','No computation can fill an unwritten exponent. Degree/arity check flags theΣ_n/Σ_p mismatch; standard formulas are comparison material only.',
 'F','The intended Steenrod operation is recognizable but this exact formula is not identifiable. Search: SteenrodEpstein1962 and Breen1978 §IV; root_web_015–024. No sign is supplied as if it were manuscript text.',{'standard_theory':'by1962','literal_formula':'underdetermined'},['SteenrodEpstein1962','Breen1978'],'high')

add(929,'K136-03',[362],'2–60','“Formule de Décalage (Quillen–Bousfield) [cf thèse Illusie]”; initial formulas are cancelled.',
 'For a finitely generated projectiveR-moduleM over a commutativeR, L_iΓ^d(M,n)≅L_(i+d)Λ^d(M,n+1)≅L_(i+2d)Sym^d(M,n+2), compatibly with the graded algebra structures. These are derived functors, and cohomological shift notation must be translated explicitly.',
 'corrected by himself later on the leaf; boxed formula replaces cancelled attempts',
 'codex_proof_checks.md §9 checks the shift by weightd rather than n; compare BMT2016 Prop3.5 equation(3-9). No unresolved-complex version is inferred.',
 'E','The leaf names earlier Quillen–Bousfield/Illusie results. BMT2016 Prop3.5 states the precise projective-module version and attributes IllusieI4.3.2. Search: root_web_014–020 and middle source audit.',{'antecedent':'Illusie1971','checked_later_formulation':'2016-02-29'},['BMT2016','DoldPuppe1961'],'high','targeted proof check')
add(930,'K136-03',[363],'63–80','The comparison for complexes is qualified “du moins pour M concentré en un seul degré”.',
 'A specified simplicial homotopy survives application of any functor, but quasi-isomorphisms of arbitrary unresolved complexes need not survive a nonlinear functor. Derived Sym,Λ,Γ require an appropriate simplicial/projective resolution. The page explicitly retains the one-degree qualification.',
 'open on the pages outside the stated one-degree case',
 'codex_proof_checks.md §9 checks the difference between applying a functor to homotopy equations and deriving it. Middle/proofs and middle computation audit give the concrete Γ²/Sym² normalized-differential comparison.',
 'C','Dold–Puppe and derived décalage establish the resolved statements; a blanket componentwise construction is invalid. Grothendieck’s later PursuingStacks§111 explicitly retracts such an unresolved use. Search: root_web_014–020, early PursuingStacks audit.',{'antecedent':'1961','own_later_retraction':'1983 manuscript;2021 arXiv transcription'},['DoldPuppe1961','BMT2016','PursuingStacks2021'],'high','targeted proof check')
add(931,'K136-03',[363],'81–128','Dold–Thom: π_i Sym∞X≃H_iX; Sym∞M(G,n)≃K(G,n).',
 'For a connected based CW complexX, the positive homotopy groups of its infinite symmetric product are its reduced integral homology. Thus a Moore space with only reducedH_n=G gives an Eilenberg–Mac Lane space after infinite symmetric product, with the ordinary connectivity/realization assumptions.',
 'stated as a known theorem; no new proof on this page',
 'Matched DoldThom1958 Th6.10 and its Moore-space application§7; no computation beyond the one-nonzero-homology consequence is claimed as independently proved.',
 'E','Exact classical theorem, not a conjecture from this folder. Search: root_web_025–028; primary Annals paper and Thom’s own bibliography opened.',{'announcement':'1956 is referenced by later bibliography; exact announcement text not collated','publication':'1958-03'},['DoldThom1958','ThomBibliography1988'])
add(932,'K136-03',[363],'63–128','L_rSym*≃L_rZ[−] and a weight grading on Eilenberg–Mac Lane homology.',
 'Dold–Puppe relates the group-ring/symmetric-power constructions to H_*(K(G,n);Z). For arbitraryG the natural weight filtration has associated graded described by derived divided powers; a functorial splitting needs additional hypotheses. For free abelianG the splitting is functorial in the checked later formulation.',
 'stated with a one-degree qualification; functorial splitting not proved',
 'Compare the stated one-degree construction against DoldPuppe1961 §8 and BMT2016 introduction(1-1),(1-2),AppendixB. Do not replace an associated-graded identity by an arbitrary-group canonical direct sum.',
 'C','The derived-filtration result is established; the unrestricted natural grading suggested by the page is stronger. BMT2016 expressly distinguishes freeG from a nonfunctorial splitting for generalG. Search: root_web_014,017,019–021,025–028.',{'antecedent':'1961','precise_later_functoriality':'2016'},['DoldPuppe1961','BMT2016'],'high')
add(933,'K136-03',[363,372],'129–136;592–666','H_(n+r)K(M,n)→H_(n+r+1)K(M,n+1), r<n.',
 'For the reduced nonadditive construction in the Eilenberg–Mac Lane situation, suspension is an isomorphism below degree2n and an epimorphism at2n. Writing the degree asn+r yieldsr<n for the isomorphism range.',
 'stated without proof as known stability',
 'DoldPuppe1961 §8.3 checked with q=n+r; the inequality transforms q<2n exactly tor<n. Endpoint epimorphism is not promoted to isomorphism.',
 'E','Classical Dold–Puppe suspension theorem; the page’s corrected range is consistent with it. Search: root_web_017 and the Cartan1955 stable-group sources in020–021.',{'publication':'1961; antecedent Cartan1954–55'},['DoldPuppe1961','Cartan1955XI'],'high','targeted proof check')
add(934,'K136-03',[364,365,371],'137–236;471–512','Degrees ofP^i andβ; Cartan formula; Adem and admissibility.',
 'For oddp the reduced powerP^i has degree2i(p−1),β has degree1, and their compositions satisfy the odd-prime Adem relations. Atp=2,Sq^i has degreei. Cartan’s product formula uses the corresponding graded signs and instability restrictions.',
 'reviewed without full proof; some coefficients/excess bounds are schematic',
 'The explicit low Adem error is checked separately inSA08-C935. Degree and parity consistency were checked against Milnor1958 §2 and SteenrodEpstein1962; no unstated full relation is reconstructed.',
 'E','Classical Steenrod-algebra structure, predating these sheets. Search: root_web_015–021,024 and the opened primary Milnor/Serre/Cartan papers.',{'publication':'1953–62'},['Milnor1958','SteenrodEpstein1962','Serre1953'])
add(935,'K136-03',[365],'196–202','Sq¹Sq²=Sq³+Sq²Sq¹(?)',
 'With right-to-left composition the correct relation isSq¹Sq²=Sq³. On t∈H¹(RP∞;F2), the left side andSq³t vanish whileSq²Sq¹t=t⁴≠0.',
 'false as stated; he marks it with a question mark',
 'root_checks.json/365_Adem_counterexample; codex_proof_checks.md §10. The coefficient ring, generator degree and composition order are explicit.',
 'E','The correct relation is an ordinary Adem relation known before these pages. Search: root_web_015–021; SteenrodEpstein1962 ChapterI and Serre1953.',{'antecedent':'1950s; textbook1962'},['SteenrodEpstein1962','Serre1953'],'high','refuted, refined statement in SA08-C935 statement field')
add(936,'K136-03',[365,371],'215–236;471–535','Free algebra on admissible monomials of excess<n;371 adds the odd-prime excess=n terms ending inβ.',
 'The cohomology of K(Fp,n) is the free graded-commutative algebra on the appropriate admissible operations on the fundamental class, with the prime-dependent excess convention and odd-prime boundary qualification. A formula depending only onHom(G,R) does not extend without qualification to arbitrary abelianG or infinite-dimensional coefficient data.',
 'corrected/qualified later at371; arbitrary-G extension is not justified',
 'Matched Serre1953 §2 and Cartan1955 IX–X. root_supplement_checks.json comparesBZ/2 andBZ/4 only for an arbitrary-G interpretation; it is not a counterexample under an elementary-Fp-vector-space hypothesis.',
 'E','The prime-field theorem is classical; the later leaf supplies an important omitted qualification. For finite-dimensional elementaryFp groups use products and Künneth; arbitraryG requires additional Bockstein/group data. Search: root_web_019–021,025–028.',{'publication':'1953;1954–55'},['Serre1953','Cartan1955IX','Cartan1955X'],'high','targeted proof check')
add(937,'K136-03',[366,368],'237–279;344–392','Bar/Tor spectral sequence fromK(Fp,n) toK(Fp,n+1); multiplicative bar construction.',
 'For the connected augmented simplicial algebra/group model, the reduced bar construction gives the classifying-space step, and the multiplicative spectral sequence has a Tor term under the stated flatness/Künneth conditions. It must not be collapsed without a degree or differential argument.',
 'proof sketched as review','DoldPuppe1961 §§6–8 and Cartan1955 IX–XI compared; chain-level shuffle supplies the product. No universal collapse is asserted in this dossier.',
 'E','The bar construction and these Eilenberg–Mac Lane calculations are classical. The manuscript’s1954 label points to the Cartan seminar, whereas Serre’s modulo2 paper appeared1953. Search: root_web_014,017,019–021.',{'Serre_publication':'1953','Cartan_seminar':'1954–55','DoldPuppe_publication':'1961'},['DoldPuppe1961','Cartan1955IX','Cartan1955XI','Serre1953'])
add(938,'K136-03',[367,371],'280–343;483–512','A_*=Sym(ξ_i)⊗Λ(τ_j), with the Milnor coproduct formulas.',
 'At oddp, the dual Steenrod algebra has polynomialξ_i,i≥1, degree2p^i−2, and exteriorτ_j,j≥0, degree2p^j−1. At2 it is polynomial withdegrees2^i−1. The coproduct is the displayed Frobenius-weighted sum, subject to switching tensor order when conjugate generators are used.',
 'stated as known; no new full proof',
 'root_checks.json/367_Milnor_coproduct verifies12 coproduct-coassociativity cases; codex_proof_checks.md §10 gives the triple-index argument. The algebra-identification theorem was source-matched, not independently reproved.',
 'E','Milnor1958 gives the exact Hopf-algebra theorem and formulas. Search: root_web_015–017,019–021,024.',{'received':'1957-05-15','publication':'1958-01'},['Milnor1958'],'high','computation or formal certificate')
add(939,'K136-03',[367],'307–330','L Sym^r is written zero unless r=p^s, in a discussion of stable operations.',
 'This is meaningful as a positive-weight statement about stable derived symmetric powers in characteristicp; it is false as an assertion about all unstable derived symmetric powers. In degree-zero input, Sym^r(V) is usually nonzero for everyr. The stable/reduced qualification is essential.',
 'ambiguous compressed statement; false without the nearby stable interpretation',
 'Counterexample:V=Fp in degree0 givesSym^r(V)=Fp for r=2p−1 (and many non-p-powers). Stable interpretation compared with DoldPuppe1961 §§10–11 and BMT2016 Frobenius-weight discussion.',
 'E','Stable additive/p-power weight behavior is classical; the unrestricted formula is not. Search: root_web_014,017,019–021; the precise stable functor and positiveweight must be retained.',{'antecedent':'1961 or earlier','modern_comparison':'2016'},['DoldPuppe1961','BMT2016'],'medium','targeted proof check')
add(940,'K136-03',[370],'420–444','E(R) is perfect; forR local, E=SL; K1=GL/E.',
 'For every unital ring the stable elementary group is perfect, using a spare matrix index. For a commutative local ring, E(R)=SL(R) by row reduction. StableK1 isGL/E; finite-rank statements or noncommutative determinants require their own conventions.',
 'stated without proof','root_checks.json/370_elementary_perfectness verifies[e12(a),e23(1)]=e13(a) symbolically; codex_proof_checks.md §11 explains stabilization and local row reduction.',
 'E','These are standard K1 facts predating the folder. Search: root_web_025–028, Milnor1971 bibliographical trail and Merkurjev’s author survey§1.',{'antecedent':'by1971'},['MerkurjevSurvey','MilnorK1971'],'high','independent re-proof')
add(941,'K136-03',[370],'420–454','K2(R) is the kernel of the universal central extension ofE(R).',
 'For a unital ring, the stable Steinberg groupSt(R)→E(R) is the universal central extension and its kernel isK2(R). This stable theorem is not an assertion for every small-rank Steinberg group.',
 'stated without proof as background','The elementary perfectness prerequisite was independently checked inSA08-C940. The universal-central-extension theorem was matched to the source, not re-proved.',
 'E','Milnor’s theorem is standard before1975; the opened author survey gives the exact stable statement and citesMilnor1971 Th5.10. Search: root_web_026–028 and the primary author bibliography trail.',{'publication':'1971'},['MerkurjevSurvey','MilnorK1971'])
add(942,'K136-03',[370],'445–470','ForX a scheme, H^i(X,K_j)⇒K_(j−i)(X); H^i(X,K_i)=cycles modulo equivalence.',
 'For a regular scheme of finite type over a field, the Zariski K-sheaves and Gersten resolution give Bloch’s formulaH^i(X,K_i)=CH^i(X); Quillen’s coniveau spectral sequence converges in finite dimension and its sheaf identification uses the Gersten hypothesis. General K-theory descent has a separate Brown–Gersten formulation. The bare phraseX un schéma is insufficient.',
 'stated without the necessary hypotheses',
 'Matched Quillen1973 §7 Th5.4,Prop5.8,Th5.11,Th5.19; no proof of the general Gersten conjecture is claimed. Degreej−i checked against the cohomological spectral-sequence indexing.',
 'E','The regular geometric statements were published1973 and were already available. More general scheme claims need separate descent and regularity assumptions; they are not proved by this leaf. Search: root_web_025–028, including Brown’s own bibliography and Quillen original.',{'conference':'Seattle1972','publication':'1973','digital_release':'2006 is not first circulation'},['Quillen1973','BrownGersten1973'],'high','targeted proof check')
add(943,'K136-03',[371],'517–535','In the stable part: H_(n+2)=G/2G,H_(n+3)={}_2G,H_(n+4)=G/2G⊕G/3G,H_(n+5)={}_2G+{}_3G.',
 'These four formulas hold in the displayed stable rangei<n for their respective offsetsi=2,3,4,5. Thusn≥6 is sufficient to use all four simultaneously. The direct sums are sums of abelian groups with the usual prime quotient/torsion functors.',
 'stated without proof, with an explicit stable-range restriction',
 'root_supplement_checks.json computes low Bockstein images and UCT on cyclic groups; codex_proof_checks.md §10 gives the general UCT argument using Cartan’s stable integral coefficient calculation.',
 'E','These are low-degree consequences of Cartan1955XI §6 Th2. Modern BMT2016 AppendixB gives more precise functorial tables in its free-group scope. Search: root_web_019–021.',{'antecedent':'1954–55','modern_tables':'2016'},['Cartan1955XI','BMT2016'],'high','targeted proof check')
add(944,'K136-03',[371],'509–535','“l’homologie est entierement de torsion premiere”; a sum ofG/pG and{}_pG is proposed.',
 'The stable degree-zero piece isG and degreeone iszero; only the positive stable offsets≥2 have Cartan’s prime-torsion description. Unstably, free divided-power pieces and extension/functoriality data occur. The unrestricted sentence is false.',
 'false if read without the immediately following stable qualification',
 'root_supplement_checks.json/371_unqualified_prime_torsion:K(Z,2)=CP∞ hasH_(2r)=Z; alsoH_n(K(Z,n))=Z. These counterexamples satisfy the stated arbitrary-abelianG wording but lie outside a correctly restricted positive stable claim.',
 'E','Cartan’s original theorem already separates these cases. The dossier preserves the restricted correct interpretation and flags the missing qualifier. Search: root_web_019–021; Cartan1955XI §6.',{'publication':'1954–55'},['Cartan1955XI'],'high','refuted, refined statement in SA08-C944 statement field')
add(945,'K136-03',[371],'536–591','Two Bocksteins are derivations, one sendsτ0→1, the otherτ_j→ξ_j; conjugation exchanges descriptions.',
 'On the appropriate odd-prime Milnor-dual models, the two left/right Bockstein actions are graded derivations with the stated generator behavior after consistent conjugation and quotient/subalgebra conventions. The analogousp=2 formulas use the different polynomial generator system. The homology statement needs reduced/stable degrees and the exact kernel/image object.',
 'proof sketched with compressed category and generator conventions',
 'codex_proof_checks.md §10 and root_supplement_checks.json redo the low-degree differential consequence. Do not apply theodd-primeτ description literally atp=2 or identify an entire unstable algebra withA_*.',
 'E','The operations and conjugation are classical; exact form checked against Milnor1958 and Cartan1955XI, and the later BMT Bockstein exposition. Search: root_web_015–021,024.',{'publication':'1954–58','modern_exposition':'2016'},['Milnor1958','Cartan1955XI','BMT2016'],'medium','targeted proof check')
add(946,'K136-03',[372],'592–666','Cartan givesH_*(K(G,n),H)≃H_*(K(H,n),G), under unspecified hypotheses and “r assez petit”.',
 'There is a stable comparison explained by symmetry ofHG∧HH, in a common stability range. The unrestricted unstable statement is false: n=1,G=Z,H=Z/2,degree3 gives0 on the left andZ/2 on the right. The manuscript itself warns that hypotheses and a small range are needed.',
 'open on the pages as to exact hypotheses; unrestricted extension false',
 'root_checks.json/372_unstable_symmetry_counterexample uses the periodic resolution ofC2; codex_proof_checks.md §10. Stable interpretation is a modern reconstruction, not his explicit theorem statement.',
 'C','Cartan/Dold–Puppe give stable comparison machinery; the exact cited Cartan theorem with the leaf’s unspecified hypotheses was not isolated. Search: root_web_019–021,025–028, including Cartan’s original seminar and MO discovery search. No global unstable symmetry is claimed.',{'classical_sources':'1954–61','exact_locator_for_his_allusion':'not established'},['Cartan1955XI','DoldPuppe1961'],'medium','targeted proof check')
add(947,'K136-03',[373],'667–686','A canonical free-abelian resolution is drawn; K(G,n)=G⊗Λ^nΨ.',
 'The free-abelian-group/forgetful adjunction gives an augmented simplicial cotriple resolution, contractible after forgetting by its extra degeneracy. K(G,n) can be represented by the simplicial module corresponding under Dold–Kan toG[n], including the exteriorΨ model. Z^G must mean the free abelian group onG here, not the full product of copies ofZ.',
 'construction sketched','Extra-degeneracy identities give a simplicial contraction before applying additive normalization; Dold–Kan identifies the one-degree chain model. The notation ambiguity is retained as a reading alarm.',
 'E','These resolutions and normalized models are classical; Breen1978 §III gives a precise resolution framework for sheaf Ext. Search: root_web_014–024, DoldPuppe1961§3 and Breen1978.',{'antecedent':'by1961','later_application':'1978'},['DoldPuppe1961','Breen1978'],'high','targeted proof check')
add(948,'K136-03',[373],'687–717','r=min(n+2p−1,2n+p−1) forK(Z,n)∧K(G,p)→ZK(G,n+p).',
 'The types of∧,Z[−] andr-qis must be fixed. Under the literal space-smash plus integral-homology reading, the bound fails forG=Z,n=p=4: reducedH10 ofK(Z,4)∧K(Z,4) is(Z/2)^2, whereasH10K(Z,8)=Z/2, although10<11. A simplicial-linear tensor interpretation is a different statement and is not reconstructed silently.',
 'false under the literal space-smash/homology interpretation; intended categorical typing incomplete',
 'Supplemental counterexample usesSA08-C943 (offset2 stable for4 and8) and integral Künneth: only degrees(4,6),(6,4) contribute, with no Tor in totaldegree10. See codex_proof_checks.md §15 and root_supplement_checks.json.',
 'F','Dold–Puppe suspension/Cartan stability do not identify this untyped bound as written. Search: root_web_014–021,025–028; no exact bound with matching source/target conventions located. The diagnostic counterexample rules out one natural reading.',{'exact_statement':'not identifiable as of2026-11'},['DoldPuppe1961','Cartan1955XI'],'medium','targeted proof check')
add(949,'K136-03',[374],'718–730','H(X,R)=H(X,Fp)⊗R for anFp-algebraR.',
 'This coefficient comparison holds with sufficient finite-type/finite-dimensional hypotheses. It fails for arbitraryX,R: forX countably discrete,R=Fp[u],the sequence(1,u,u²,…) inH0(X;R) has no preimage inFp^N⊗R, whose elements have uniformly bounded polynomial degree.',
 'false without finiteness hypotheses',
 'root_checks.json/374_base_change_counterexample; codex_proof_checks.md §12 verifies the exact map and the unbounded-degree witness.',
 'E','The required tensor/product distinction and universal-coefficient restrictions are standard. Breen’s sheaf argument uses its own finiteness/acyclicity hypotheses, not this unrestricted formula. Search: root_web_013–024, Breen1978§I.',{'antecedent':'standard before1975','precise_application':'Breen1978'},['Breen1978'],'high','refuted, refined statement in SA08-C949 statement field')
add(950,'K136-03',[374],'726–819','P_R^i=P^i⊗1 fori>0, whileP_R^0=1⊗F; operations on the structural sheaf.',
 'For the usualp-power operations withFp-algebra coefficients, scalars transform by Frobenius for everyi. Atp=3,R=F3[u],z∈H2(CP∞;F3), P1(uz)=u³z³, notuz³. A separately chosenR-linear extension would not have the same power-operation axioms. In a toposP0 acts as Frobenius, so it need not be the identity.',
 'false for usual operations under the opening scalar formula; structural-sheafP0 observation is correct',
 'root_checks.json/374_Frobenius_semilinearity; codex_proof_checks.md §12. Degree2 top-power axiom supplies the test, withu³−u nonzero.',
 'B','Breen1978§IV constructs the extended operations with FrobeniusP0 on ring objects. It confirms the sheaf phenomenon while requiring the semilinearity correction or an explicit different convention. Search: root_web_013–024; Milnor1958§2 power axiom.',{'publication':'1978','earlier_topological_axioms':'1950s'},['Breen1978','Milnor1958'],'high','refuted, refined statement in SA08-C950 statement field')
add(951,'K136-03',[374,375],'790–848','The Witt-vector extension is contrasted with Ext inFp-vectorial sheaves.',
 'W2 gives a nontrivial extension ofGa byGa in abelian sheaves; multiplication byp onW2 is nonzero. ThereforeW2 is not anFp-module object and is not an extension in theFp-linear sheaf category. Vanishing ofExt1 in that latter category is compatible with the Witt extension.',
 'category distinction explicitly present on the pages',
 'codex_proof_checks.md §13 checks the middle-object category. Breen1978 printedp40 explicitly makes the same distinction; the published page was visually inspected.',
 'B','Breen’s exact category distinction and odd-Ext theorem establish this interpretation. Treating the Witt extension as a refutation ofFp-linearExt1=0 would be a misreading. Search: root_web_013–024.',{'publication':'1978'},['Breen1978'],'high','targeted proof check')
add(952,'K136-03',[375,376],'820–940','Fori>1,the higherExt is killed locally by a power of Frobenius.',
 'In Breen’sFp-linear big-site setting with structural sheafGa and his affine-space/acyclicity hypotheses, each positive even Ext group isF-torsion with an explicit exponent; odd groups vanish. OverFp,degree2j hasF-nilpotence exponentv_p(j)+1. The theorem must not be transferred to arbitrary sites or abelian-sheafExt unchanged.',
 'open on the pages; an induction and final formula are attempted',
 'The exact published nilpotence exponent is compared inroot_checks.json/376_Breen_exponent_comparison. Source hypotheses checked inBreen1978Th1.3; no independent re-proof of the full Ext calculation.',
 'B','Breen1978Th1.3 proves the precise theorem underA1,A2; the final computation in this manuscript has a one-step exponent discrepancy. Search: root_web_013–024, visually checked printedp40 andp47.',{'publication':'1978','first_preprint_circulation':'not established from opened sources'},['Breen1978'],'high')
add(953,'K136-03',[375],'841–865','For the perfect site, higherExt vanishes.',
 'For a perfectFp-algebraR,on the big perfect étale site, Ext^i_Fp(Ga,Ga)=0 fori>0 andEnd(Ga)=R[F,F^−1] withFa=a^pF. The analogous abelian-sheaf statement has different degree-one behavior and must be stated separately.',
 'stated as a corollary of the Frobenius-torsion proposal',
 'Matched Mathew2022TheoremA.1 exactly; compared coefficient categories withBreen1978introduction. No wholesale re-proof of the perfect-site theorem.',
 'B','Breen’s perfect-site vanishing is established; Mathew provides a modern proof and explicitly separates it from the nonperfect-site calculation. Search: root_web_013–018,024; MathewAppendixA and bibliographyBreen1981.',{'Breen_Orsay_course':'1976–77 noted in1978 introduction','Breen_publication':'1981','Mathew_first_arXiv':'2022-05-23','Mathew_version_used':'v3,2022-11-12'},['Breen1978','Breen1981','Mathew2022'],'high')
add(954,'K136-03',[376],'866–889','Lemma1: the edge mapδ in the spectral-sequence induction is zero.',
 'The edge-map vanishing is a specific compatibility in the proposedExt induction, with source and target depending on the preceding construction. The final Ext theorem does not alone prove this chosen chain-level edge map vanishes; the manuscript supplies only the abbreviated argument.',
 'proof sketched; not a complete independent proof on the leaf',
 'Matched the role of the edge map againstBreen1978canonical resolution andfundamental spectral sequence§§III,V–VII. Missing choices are not filled from the final answer.',
 'C','Breen proves the global Ext theorem by a detailed spectral-sequence calculation. An exact identification of this sketch’sδ with one of his maps requires a separate comparison. Search: root_web_013–024,Breen§§III,V–VII.',{'global_theorem':'1978','specific_sketch':'not independently completed here'},['Breen1978'],'medium','targeted proof check')
add(955,'K136-03',[376],'890–901','Lemma2 compares a power operation to tensoring withF; the proof writes onlyP0.',
 'The displayed calculation verifies theFrobeniusP0 case under the stated ring-object construction. A formula for all higher powers requires the higher-operation compatibility, including semilinearity and degree indexing, which is not written in this proof.',
 'underproved on the pages: theP0 instance is checked, arbitrary-index statement is not',
 'codex_proof_checks.md §§12–13: distinguishP0frompositive powers; use the semilinearity test inSA08-C950. No extrapolation from index0.',
 'C','Extended Steenrod operations are developed inBreen1978§IV, but the exact all-index edge-map comparison is not identified solely from this sketch. Search: root_web_013–024,Breen§IV and later spectral-sequence sections.',{'publication':'1978','literal_proof_scope':'index0'},['Breen1978'],'medium','targeted proof check')
add(956,'K136-03',[376],'902–907','Ext odd=0; Ext^(2i)=k[F]/F^v_p(i).',
 'Overk=Fp,in theFp-linear big-site category ofBreen’s theorem, Ext^(2j+1)(Ga,Ga)=0 andExt^(2j)(Ga,Ga)=Fp[F]/(F^(v_p(j)+1)) forj>0. The transcribed denominator omits+1 and would makeExt2zero. Generalbasecoefficients require thetwisted(F,Fop)-bimodule formulation.',
 'false as transcribed in the exponent; no manuscript ink decision',
 'root_checks.json/376_Breen_exponent_comparison comparesdegrees2–16 atp2. PublishedBreenp40formula visually inspected; p116 relations also showv_p(j)+1. codex_proof_checks.md §13.',
 'B','Breen1978 provides the exact corrected group calculation. HisYoneda algebra multiplication is explicitly left conjectural there (Conj7.12), so the group theorem is not a full multiplicative classification. Search: root_web_013–024.',{'publication':'1978','first_circulation':'not established'},['Breen1978'],'high','refuted, refined statement in SA08-C956 statement field')
add(957,'K136-03',[376],'908–940','A final bar/Koszul spectral-sequence calculation is begun and left in draft form.',
 'The last diagram suggests computing the remaining Ext via bar resolutions and a Koszul-type algebra. It does not specify a completed differential calculation or a proof of degeneration/product extensions. Its intended group answer can be compared withBreen; its multiplicative conclusion cannot be recovered from the fragment alone.',
 'open on the pages; unfinished calculation',
 'CompareBreen1978§V(characteristic2),§VII(odd characteristic),Remark7.11,Conj7.12. This audit checks the distinction between group/bimodule andYoneda-algebra results rather than inventing missing differentials.',
 'C','The Ext groups andF-actions are established byBreen1978. The fragment’s particular bar/Koszul route and any fullYoneda-algebra assertion remain incompletely identified; no subsequent exact settlement was located in the bounded follow-up search. Search: root_web_013–028,Breenbibliography,MathewAppendixA (which expressly does not recover the nonperfect calculation).',{'group_calculation':'1978','perfect_site_reproof':'2022','exact_multiplicative_fate':'not established in this search'},['Breen1978','Mathew2022'],'medium')

def write():
 (O/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
 (O/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
 for name,header,rows in [('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings),('links.tsv',['kind','from','to','what','evidence','note_ids'],links),('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)]:
  with (O/name).open('w',newline='') as f:
   w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
 print(json.dumps({'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links),'events':len(events)},ensure_ascii=False))
if __name__=='__main__':write()
