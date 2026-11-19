"""Manually authored self-directed-problem, mathematical-reading and link registers."""

def P(n,title,nums,words,modern,state,why,worth,refs):
    problem(n,title,[f'C-SA14-{x:03d}' for x in nums],words,modern,state,why,worth,refs)

P(601,'Independence and intrinsic meaning of the resolution construction',[601,602,605],
  '“one should check that ... Q together with (10) does not depend on the choice of the resolution” (57:5–6); the coefficient-field dependence is explicitly retained.',
  'Compare local Picard sheaves from two proper regular models by a common dominating model, while fixing the coefficient field and the topology on test algebras.',
  'Boutot gives intrinsic local-Picard theory in specified settings; Kollár states the S₂, pure-dimensional geometric hypotheses. Lipman supplies the local-Artin comparison.',
  'No longer an open existence program in those settings. The letter’s unrestricted completed tensor-product formulation still needs its exact hypotheses, and independence of a model is not independence of a coefficient field.',
  'High editorial value; first write the comparison diagram including the twisted exceptional lattice and Brauer boundary.',
  ['R_Boutot1978','R_Kollar2014','R_Lipman1976'])
P(603,'Positive exceptional model and stabilization',[603],
  '“replacing if necessary X by a suitable model dominating it ... J/J² [is] an ample sheaf” (57:7).',
  'Ask for a projective birational model with an invertible exceptional ideal of ample conormal, and separately prove stabilization of its formal Picard system.',
  'The conditional stabilization follows from Serre vanishing and square-zero units; surface negativity and local Picard theory provide established cases.',
  'The computation proves the consequence, not the existence of the required model in every version of the letter’s hypotheses.',
  'Medium; determine the intended birational/projectivity assumptions before any new theorem is sought.',
  ['R_Lipman1976','R_Kollar2014','R_Boutot1978'])
P(604,'Exceptional lattice injectivity in higher dimension',[604],
  '“It would be nice to have a proof in general ... negative definiteness of an intersection matrix Xᶦ.Cʲ?” (57:8).',
  'Under precise projective birational hypotheses, test whether exceptional Cartier divisors inject into the special-fibre Néron–Severi group.',
  'Normal surface negative definiteness proves the stated surface case. General local-Picard quotient descriptions require their specified geometric assumptions.',
  'A general higher-dimensional negativity theorem has not been matched to the exact draft formulation by this search.',
  'Medium; identify a modern negativity lemma whose hypotheses match the chosen model, then compare its kernel with the lattice in the letter.',
  ['R_Lipman1975','R_Kollar2014','R_Boutot1978'])
P(605,'Functor on arbitrary test algebras',[605],
  'The formula (18) is offered “more or less”; the actual Picard interpretation on57:9–11 is proved only for noetherian geometrically regular test algebras.',
  'Specify the topology and derived or ordinary completed base change before extending the representing-property claim to all algebras.',
  'The intrinsic functor exists in Boutot’s setting. The letter itself distinguishes sheafification from actual Picard groups and records a Brauer obstruction.',
  'The wider test-category assertion is not verified merely by checking geometric points or tangent spaces.',
  'High for consolidation; compare the exact functor in Boutot with formula(18), one test-category restriction at a time.',
  ['R_Boutot1978','R_Kollar2014','R_Lipman1976'])
P(606,'Mixed-characteristic Artin-base Picard group',[606],
  '“Let A be a local Artin ring with perfect residue field k ... Give a natural construction” (57:11), followed by the Greenberg ring-functor candidate on57:12.',
  'Construct the locally algebraic group of a proper scheme over a local Artin ring through the relevant Greenberg/Witt-vector functor and compare rational points.',
  'Lipman1976 identifies Grothendieck’s September1969 question and answers it; Theorem1.2 and§5 give the construction and Theorem7.5 the descent obstruction.',
  'Solved in the cited hypotheses. The source’s original literal injection must be read together with its obstruction statement.',
  'High historical match; first align the letter’s formula(22) with Lipman’s exact sequence.',
  ['R_Lipman1976'])
P(608,'Cube calculation and the correspondence splitting',[607,608],
  'The pages solve the recurrence for αₙ and repeatedly recompute the n-factor formula; the exact product sequence is marked “split” when all factors have sections (57:15–19).',
  'Use unordered pairs and normalized restrictions to write the cube identity and the Picard-product decomposition with the precise properness and H⁰ assumptions.',
  'Classical cube theory; coefficients were independently recomputed. The correspondence functor’s infinitesimal rigidity is separate from its general separatedness.',
  'No open arithmetic recurrence remains. Pair-index ink and the scope of representability are editorial checks.',
  'High for error prevention; verify n=3 before interpreting the general exponent formula.',
  ['R_Milne2008','R_Murre1966'])
P(609,'Extend an abelian group law through a proper smooth family',[609],
  '57:33 states the one-abelian-fibre theorem;57:41 reduces closedness to aDVR and says the argument is known but “à développer”.',
  'Fix a section of a smooth proper family and establish that the abelian-scheme locus is open and closed; distinguish the projective theorem from the full proper formulation.',
  'GIT6.14 and Genestier–Ngô2.4.1 give the projective statement. Their infinitesimal andDVR lemmas match the draft’s intermediate steps.',
  'The opened projective theorem alone does not certify the wider proper statement. The source’s uniqueness proof is stronger than its written existence argument.',
  'High historical reconstruction; locate the proper-family extension theorem and compare the section and connected-base hypotheses.',
  ['R_GIT1994','R_GenestierNgo','R_Milne2008'])
P(610,'Which groups have dense prime-to-characteristic torsion?',[610,614],
  'The proposed no-additive-factor criterion is rejected on57:44: “Or ça ...” is followed by the vector-extension counterconsideration;57:51 introduces “très rigide”.',
  'Classify the smooth commutative groups satisfying the exact finite-torsion and schematic-density conditions, keeping connectedness and the prime quantifiers explicit.',
  'Brion’s anti-affine classification explains the characteristic-zero vector extensions; SGA3XI§6 supplies the finite-level density framework.',
  'The withdrawn necessity is not open. The draft adjective combines several conditions and must be defined before it can be compared with a modern classification.',
  'Medium; translate the definition into separate density, finiteness and smooth-subgroup requirements.',
  ['R_Brion2009','R_SGA3XI'])
P(612,'Spread rigid subgroup schemes over primary extensions',[612,614,683],
  '57:49 admits the spreading-out rigidity step,57:51 strengthens the definition, and57:53–58 distinguishes descent of support from descent of the subgroup.',
  'Determine when a closed subgroup after a primary extension descends, and when only its smooth reduced support is constant.',
  'SGA3 has precise torsion-density, transporter, quotient and field-extension results; the general draft chain still depends on an admitted lemma.',
  'The gap is a precise hypothesis comparison. A finite radicial residual quotient can survive even when support is fixed.',
  'Medium; state the spread-out lemma without the undefined adjective and compare it with SGA3XI6.2.',
  ['R_SGA3XI','R_SGA3VIA','R_SGA3VIB'])
P(613,'Can rigidity force the kernel to be open?',[613],
  'The proposition on57:51 asserting a universally open kernel is crossed out;57:52 exhibits the limiting elliptic graph example.',
  'Identify exactly which flatness or torsion hypotheses prevent specialization of a kernel from acquiring extra components.',
  'The proposed universal statement is already refuted by the author. SGA3 separates openness, flatness and topological surjectivity.',
  'Not an unsolved conjecture. The remaining task is to preserve the correction and its relation to the earlier unramified-ambient lemma.',
  'High editorial value, low research priority; compare the two ambient group schemes in the purported contradiction.',
  ['R_SGA3VIA','R_SGA3VIB'])
P(615,'Relative Albanese when the Picard identity component is not proper',[615,670],
  '57:60–63 constructs homogeneous and inhomogeneous Albanese objects and asks how far the relative existence argument extends.',
  'Seek a base-change-compatible family of maximal abelian subvarieties ofPic^τ and dualize it to an Albanese torsor, rather than taking a Chevalley quotient.',
  'Laurent–Schröer2024 Th10.2 supplies this criterion; Th7.2 and Cor10.5 handle field-extension and proper-field cases.',
  'Solved subject to the existence of the indicated family. The criterion itself explains why arbitrary degeneration does not automatically give a relative Albanese scheme.',
  'High; first compare the universal mapping property and maximal-subgroup condition with the draft’s minimal-subgroup construction.',
  ['R_LaurentSchroer2024'])
P(616,'Picard smoothness over nonreduced characteristic-zero bases',[616],
  '57:64 asks whether the characteristic-zero smoothness and cohomological-flatness argument persists over a nonreduced base.',
  'Distinguish Pic⁰ from the full Picard space, and specify whether the family is smooth proper or merely has smooth group fibres.',
  'Deligne1968 Th5.5 and Kleiman5.21 yield smoothPic⁰ in the smooth characteristic-zero setting; Kleiman5.22 gives jumping full-Picard components.',
  'The identity-component question is settled. A statement about the whole Picard scheme is false without further hypotheses.',
  'High; compare the exact object denotedPic in the sheet with the identity component in the published theorem.',
  ['R_Deligne1968','R_Kleiman2005','R_FGA236'])
P(618,'Numerical equivalence, boundedness and finite curve tests',[618,619,685],
  '57:71–72 asks which finiteness assertions follow from the equivalence criteria and records Kleiman’s route through numerical classes.',
  'Compare numerical triviality withτ-triviality, establish uniform bounds on geometric NS groups, and test bounded subsets ofPic by degrees on finitely many curves.',
  'FGA236 addendum and SGA6XIII3.6,4.7,5.1–5.4 contain the precise theorems. XIII5.3 directly corrects the factor-two formula on57:70.',
  'The principal numerical theorems are settled. The isolated external criterion(ii) on57:72 remains underidentified because its antecedent is not supplied.',
  'High historical match; align each numbered statement with its published counterpart rather than treating finiteness as a single assertion.',
  ['R_FGA236Addendum','R_SGA6'])
P(620,'Proper-surjective Picard pullback',[620],
  'The July18,1962 Murre letter asserts finite-type pullback, affineness over fields and generic relative quasi-affineness (57:73–79).',
  'State pullback in the contravariant direction and distinguish finite type, quasi-affine and affine relative representability.',
  'SGA6XII Th1.1 and Cor1.5 give the exact generic and field statements; the full original pages were inspected.',
  'Settled in those forms. General-base affineness is the distinct MP-SA14-677.',
  'High; use the actual theorem hypotheses in every occurrence of the Murre-letter statement.',
  ['R_SGA6','R_Kleiman2005'])
P(621,'Universal flattening for proper nonprojective schemes',[621,679],
  '“Problem A” asks for representability of the base-change functor that makes a coherent sheaf flat (57:74–79).',
  'Represent universal flattening as a monomorphism locally of finite type, keeping properness or an appropriate purity substitute.',
  'Murre1965§3(A) Th2/Cor1 supplies the proper case; Stacks05PS gives the finite-presentation version.',
  'Solved. A flattening blowup or a convenient stratification is not by itself the universal object asked for.',
  'High; compare the functors on arbitrary test schemes before comparing constructions.',
  ['R_Murre1966','R_StacksFlattening'])
P(624,'Local Picard group of an affine cone',[624,625],
  '57:185–192 asks how the cone calculation changes on completing the local ring, after quotienting by the hyperplane class.',
  'Separate the punctured whole cone, the punctured local spectrum and its completion, and compute the positive-twist infinitesimal layers.',
  'Kollár’s cone example and the formal-neighbourhood calculation provide explicit formulas. For a plane curve, the characteristic-zero correction has dimension binomial(d−1,3).',
  'The curve calculation is settled; the source’s degree≥6 example is sufficient, not minimal. Higher-dimensional obstruction groups need a separate analysis.',
  'High for interpretation; test a smooth plane quartic first, where the correction is already one-dimensional.',
  ['R_Kollar2014','R_EGAII','R_Boutot1978'])
P(626,'Punctured henselization versus completion',[626],
  '57:194: “Il est possible que la dernière flèche ...” proposes Picard invariance under completion of the henselian pair.',
  'Compare isomorphism classes of line bundles on the complement of the defining ideal in a noetherian henselian pair and its completion.',
  'Elkik1973III.1 Th3 and the corollariespp573–574 give the Picard comparison.',
  'Solved under the cited henselian/noetherian hypotheses. This does not assert equality of unit groups or full faithfulness of the line-bundle groupoid.',
  'High exact match; quote the corollary with its puncture and completion ideal.',
  ['R_Elkik1973'])
P(627,'The σ² torsion-rank criterion for families of abelian components',[627],
  '57:196,198 proposes a criterion with n divisible byσ² for fibrewise abelian varieties to assemble into a subgroup scheme.',
  'Fix the finite component-quotient length and the flatness/reduced-base assumptions before translating the tentative rank test.',
  'SGA3 component theory and Laurent–Schröer’s maximal-abelian-family criterion are relevant; no identicalσ² test was located.',
  'The diagram is partly underdetermined, and the numerical test is not proved by the structural references alone.',
  'Medium; recover the exact maps and meanings ofσ from the original scans before attempting a modern theorem.',
  ['R_SGA3VIB','R_LaurentSchroer2024'])
P(629,'Finiteness of the torsion-component locus',[629,631],
  '57:203–212 studiesΓ^τ, bounded torsion exponents and the prime-to-characteristic locus, with a marginal request to provePic^τ quasi-compact.',
  'Separate general group-scheme component statements from the special boundedness theorem for the Picard functor.',
  'FGA’s addendum and SGA6XIII establish Pic^τ finite type; SGA3 handles the field component quotient.',
  'The Picard theorem is settled. Literal component criteria such as “one aⁿ is closed” are insufficient and remain reading alarms.',
  'Medium; test the proposed general criterion on a discrete étale group before invoking Picard-specific boundedness.',
  ['R_SGA3VIA','R_FGA236Addendum','R_SGA6'])
P(630,'Finite type from openness and proper fibres',[630,684],
  '57:208–209 gives a finite-type criterion and then a constructible-subset version, crossing out “universally” in the first statement.',
  'Prove relative quasi-compactness by spreading a proper generic piece and using openness or generization lifting to eliminate the remainder.',
  'The scheme version has an independent noetherian-induction proof and belongs to EGA’s properness criteria; the exact subset formulation was not identified verbatim.',
  'The remaining issue is the structure carried by the constructible subset, not the elementary induction once that structure is supplied.',
  'Medium; formulate the subset version as a locally closed subspace before comparing EGA references.',
  ['R_EGAIV3','R_Kleiman2005'])
P(633,'What does the degenerating conic show?',[632,633],
  'The nonrepresentability argument on57:217–218 is withdrawn, and57:219 says the many-origin scheme represents the functor.',
  'Compute special bidegrees, identify classes of equal generic degree and glue one origin for each special multidegree.',
  'The explicit computation gives a nonseparated representable Picard scheme. Vertical component self-intersections are−1.',
  'No surviving nonrepresentability conjecture remains in this example.',
  'High editorial priority; preserve the cancellation and the final many-origin construction together.',
  ['R_FGA236','R_Kleiman2005'])
P(635,'Closed-cover Čech computation for three lines',[635],
  '57:224 proposes H¹(X,O_X)≅H¹(X₁⊔X₂⊔X₃/X,G_a) and adds a strict-descent justification.',
  'Test whether the closed component cover computes coherent cohomology, especially when all three pairwise intersections coincide.',
  'Atτ=0 the proposed naive Čech complex hasH¹=0, whereas a plane cubic hasH¹(O)=k. Both calculations are supplied.',
  'The proposed method is false in this literal form; a correct resolution must include the nonexactness of the closed-cover complex.',
  'High; inspect the common-intersection stalk first and retain the counterexample as a warning against closed-cover Čech arguments.',
  ['R_EGAI'])
P(641,'Kummer transgression and the generalized Jacobian torsor',[640,641],
  '57:142–145 asks whether the low-degree transgression class equals the Kummer boundary of the generalized degree-one Picard torsor.',
  'Compare the low Postnikov class ofRf_!μ_n with the boundary of the relevant semiabelian torsor, retaining a nonempty finite étale puncture and n invertible.',
  'MVW gives the generalized-Jacobian/Kummer identification over fields; Harari–Szamuely and Petrov–Skorobogatov give closely matching arithmetic extension/transgression formulas.',
  'The full relative compact-support statement and its sign were not identified verbatim. Field and semiabelian results do not automatically settle every base in the draft.',
  'High; fix the cohomological triangle and boundary convention, then compare the two cocycles.',
  ['R_MVW2006','R_HarariSzamuely2009','R_PetrovSkorobogatov2026'])
P(642,'When is the Picard group of a singular curve abelian?',[642],
  '57:147–151 revises the graph and singularity contributions to the Picard dimension;57:151 states the converse under the indicated singularity restrictions.',
  'Use normalization and the incidence graph to separate torus and unipotent ranks ofPic⁰.',
  'For a reduced proper connected curve over an algebraically closed field, the normalization exact sequence gives the ranks; nodal compact type means the dual graph is a tree.',
  'The normalization calculation is settled. The local symbolμ must not be identified simultaneously with branch number andδ-invariant.',
  'High; test an ordinary node and a cusp before reading the general formula.',
  ['R_Kleiman2005'])
P(644,'Dimension of the moduli strata in the curve sketches',[644],
  '57:153,155 adds the component contributions3gᵢ−3+νᵢ and then introduces unfinished corrections for unstable rational components.',
  'For stable graphs compute3g−3−e; treat automorphisms and unstable vertices in a distinct stack-theoretic formulation.',
  'The stable-graph count is standard and independently checked. The unspecified drawings do not determine a universal formula for the unstable cases.',
  'No open stable dimension formula remains; the unstable correction symbols are an identification task.',
  'Medium; label every vertex, branch and automorphism dimension in one of the drawn examples.',
  ['R_KnudsenMumford1976'])
P(646,'Projective frames versus unmarked embedded varieties',[646],
  '57:158–162 compares special line bundles, Brauer–Severi bundles and a projective-linear quotient; a marginal condition invokes automorphisms ofX.',
  'Specify whether the moduli object remembers the marked mapX→P or only its Hilbert image, and keep cohomological flatness ofH⁰.',
  'The framed complete-linear-system construction is standard FGA/GIT. Marked embeddings have freePGL action under universalH⁰(O)=O; unmarked images may have stabilizers.',
  'The issue is a change of moduli problem, not a missing general representability theorem.',
  'High; write the two functors and their automorphism groups before taking a quotient.',
  ['R_FGA232','R_GIT1994','R_Kleiman2005'])
P(647,'Check the tangent and obstruction diagram for Div→Pic',[647],
  '57:164 labels the tangent spaces and says various cohomology vanishings imply smoothness.',
  'Derive the diagram from0→O_X→L→N_D→0 and distinguish relativeDiv/Pic from absoluteDiv/S obstructions.',
  'Kleiman5.11 and5.18 give the published tangent theory; the long exact sequence is recomputed here.',
  'Settled. The terminal H¹(O) in the second row must beH²(O) mathematically, without deciding the unreadable ink.',
  'High as a reading check; reconstruct the long exact sequence before comparing subscripts.',
  ['R_FGA236','R_Kleiman2005'])
P(649,'Regularity in codimension one and rational-map extension',[648,649],
  '57:166–171 introduces pseudo-morphisms and asks for polar-locus descriptions while the target’s affine qualifier is altered.',
  'Separate uniqueness from schematic density, extension at codimension-one points to proper targets, and global regularity of functions on normal schemes.',
  'EGA provides the rational-map framework. R₁ alone lacksS₂ and does not give the intersection property for functions; a projective target can have codimension-two indeterminacy.',
  'The overly broad statements are refuted by explicit examples; the qualified standard results are settled.',
  'High; test the punctured nonnormal surface ring and the rational mapP²⇢P¹ before merging the assertions.',
  ['R_EGAI','R_EGAIV4'])
P(651,'Local connectedness under successive cuts',[650,651,652],
  '58:3–17 develops and repeatedly revises the connectedness-dimension induction, including a finite set of points to avoid and a converse.',
  'State the complete-local connectedness theorem with initial connectedness and component-dimension assumptions, then distinguish sufficient and necessary conditions.',
  'SGA2XIII Th2.1 and its following converse discussion are the direct published match. The initial unqualified lemma is false without connectedness.',
  'The main theorem is published; the draft’s reversed inequality and incomplete induction are reading/proof-status issues.',
  'High historical match; compare the hypotheses line by line withXIII2.1 instead of only citing a generic connectedness theorem.',
  ['R_SGA2'])
P(653,'Finite generation of the local fundamental group',[653],
  '58:19 reduces to normal dimension2 and conjectures finite generation for complete local rings with algebraically closed residue field.',
  'Ask topological finite generation of the full étale fundamental group of the connected punctured spectrum, with the noetherian and dimension conditions explicit.',
  'SGA2XIII3.1 records the full problem. Suzuki2023 proves the maximal pro-nilpotent quotient is finitely generated under the stated complete-local hypotheses.',
  'The cited partial theorem does not settle the full profinite group. Results for tame quotients or special singularities also do not imply the full assertion.',
  'High research relevance, but first check the exact full-group status after2023 and separate all quotient variants.',
  ['R_SGA2','R_Suzuki2023'])
P(655,'Determinant descent without a chosen point',[655,656,657],
  '59:2–6 asks to detail descent of the determinant’s NS class and to verify the sign in the resulting three-torsor trivialization.',
  'Fix a determinant convention and normalized Poincaré bundle, then compare the basepoint change by exponent−χ and the induced contracted-torsor cocycle.',
  'Knudsen–Mumford supplies determinant functors and base change; the draft’s NS independence follows. The exact canonical three-torsor comparison was not located verbatim.',
  'Existence of equal cohomology classes is weaker than an equality of canonical rigidified sections; that last comparison remains explicitly unverified here.',
  'High; write one Čech cocycle for changing the basepoint and check its signs against the determinant convention.',
  ['R_KnudsenMumford1976','R_Mukai1981','R_PoonenStoll1999'])
P(658,'GRR calculation and the curve-theta sign',[658,659,668],
  '59:6–9 asks for direct calculation and explicitly says to verify the sign;59:16 repeats the curve calculation for a complex of rankρ.',
  'Compute the degree-two component of the Fourier–GRR transform, retaining the rank and whetherdet* meansdet or its inverse.',
  'The exterior-algebra calculation gives½p_*(D²a_{n−1}). For the standard alternating determinant it is the negative theta class on a curve; the inverse determinant reverses this.',
  'No convention-independent sign verdict is possible from an ambiguousdet* symbol. The missing rankρ is independently refuted by a rank-two example.',
  'High; fix the determinant convention before comparing the curve and abelian examples.',
  ['R_KnudsenMumford1976','R_Mukai1981','R_Beauville1983'])
P(660,'Universal-curve Picard sections and Franchetta',[660],
  '59:10 asks that sections of the universal curve’s Picard functor be generated byK, including a marked point wheng=1.',
  'Distinguish relative Picard sections from actual line bundles and include marked-point generators and low-genus exceptions.',
  'Schröer’s strong Franchetta theorem covers the stated generic-curve setting forg≥3. The literal marked genus-one claim is false:K is trivial but the marked point has degree1.',
  'The broad draft is not uniformly true. The relation between generic statements and sections on the entire moduli stack needs its own comparison.',
  'High; resolve the genus-one exception first and then state the genus≥3 theorem with its marking and field assumptions.',
  ['R_Schroer2003'])
P(661,'Which grading does the Chow Fourier transform reverse?',[661],
  '59:10 says that expD transforms degreei into complementary degreen−i.',
  'Distinguish cohomological degree from the Beauville bigrading of rational Chow groups.',
  'Beauville1986 Prop1 givesCH^p_s→CH^{g−p+s}_s. Complementary codimension is the s=0 specialization.',
  'The unrestricted Chow statement is false; the corrected graded statement is established.',
  'High; test a nonzeroPic⁰ class, whose Beauville grade is1, before applying complementary codimension.',
  ['R_Beauville1983','R_Beauville1986'])
P(662,'Double determinant polarization and its sign',[662],
  '59:10–11 says “faire calcul direct ... attention aux signes” and then writesφ(φ(δ))=δχ(δ)^{n−2}.',
  'Separate the positive adjugate operationδ↦−φ(δ) fromφ itself.',
  'With the standard determinant,φ=−adj andφ² has factor(−1)^g. The positive adjugate squared has the source’s positive factor.',
  'The literal formula mixes two operations. Explicit diagonal calculations settle the algebra once a convention is fixed.',
  'High; useg=3 and a principal polarization as the first sign test.',
  ['R_Mukai1981','R_Beauville1983','R_Beauville1986'])
P(663,'Primitivity of the universal dual polarization',[663],
  '59:11 expects the constructed polarization on the dual to be indivisible and generate the universal NS sections for the given degree.',
  'Fix the full polarization type, not only its degree, and compare the adjugate polarization with the primitive dual type.',
  'The type(1,2,2) has adjugate type(4,2,2), divisible by2. Thus the literal indivisibility expectation fails.',
  'The primitive-generator version is a corrected moduli question; recent principal-level Franchetta results do not establish arbitrary-type statements.',
  'High; compute Smith invariants of the polarization map before making a universal generator claim.',
  ['R_FringuelliPirisi2019','R_Laga2025'])
P(664,'Annihilator gcd versus canonical torsor trivialization',[664,665],
  '59:12–14 compares powersλ and writesppcm after a crossed-outpgcd, while seeking canonical sections of polarization torsors.',
  'Compute the common annihilator ideal generated byλ^g−λ^{g−1}, and separately ask whether the induced trivializations are compatible.',
  'For g≥2 the gcd is2; forχλ^g−λ^{g−1} it is1 whenχ is even and2 whenχ is odd. Class annihilation does not select a canonical section.',
  'The arithmetic is settled by an elementary proof. The asserted evenχ⇒2-divisible polarization is false, already in type(1,2).',
  'High; replace the arithmetic question by the ideal of annihilators while preserving the separate coherence question.',
  ['R_PoonenStoll1999','R_Laga2025'])
P(666,'Compare two canonical doubled-polarization constructions',[666,673],
  '59:28: “Vérifier que c’est la section ... canonique définie pour toute sectionδ ...”.',
  'Compare the section of the doubled theta torsor from inversion with the normalized Poincaré pullback representing2λ.',
  'Poonen–Stoll and Alexeev give the canonical2λ construction. For Jacobians, Serre duality identifies the doubled theta torsor section withK_C.',
  'The all-base symbol-level comparison needs compatible rigidifications; merely proving2c_λ=0 does not prove equality of the two sections.',
  'High; compare the normalized fibre at the identity in both constructions.',
  ['R_PoonenStoll1999','R_Alexeev2002','R_Laga2025'])
P(667,'Additivity in the coefficient complex',[667,668],
  '59:15–17 generalizes the construction to a perfect complex and marks an additivity claim in the margin.',
  'UseK₀-additivity inF and retain polynomial dependence on the tensor classδ of a line bundle.',
  'Knudsen–Mumford gives determinant additivity; Fourier–GRR makesφ homogeneous of degreeg−1 inδ for abelian varieties.',
  'The claim ofNS-additivity is false forg≥3. The correctedK₀ statement is established.',
  'High; testφ(2δ) on a principally polarized threefold before accepting the wordhomomorphism.',
  ['R_KnudsenMumford1976','R_Mukai1981','R_Beauville1986'])
P(669,'Tensor/translation equivariance signs',[669],
  '59:18–20 twice requests verification of the signs in basepoint change and Pic⁰ translation.',
  'With the positive kernel and h_M(β)=t_β*M⊗M^{-1}, the Picard-class difference is +h_M(β); the manuscript minus agrees if its tilde map is −h_M.',
  'Mukai1981§3(3.1) supplies the exchange. The support of t_β*D moves by−β but gives no further minus in h_M; the explicit dictionary is in C-SA14-669.',
  'The sign is convention dependent; the draft does not contain the requested completed check.',
  'High; compare the fibre of the transformed family atx with the old family atx+β.',
  ['R_Mukai1981','R_KnudsenMumford1976'])
P(670,'Albanese duality from a chosen abelian subfunctor',[615,670,671],
  '59:20–25 proposes starting the Albanese theory from B→Pic_X and asks how far the universal property extends to commutative groups.',
  'Use a chosen abelian schemeB and its dual torsor recipient; treat arbitrary commutative group targets as a separate extension with extra hypotheses.',
  'The abelian-target universal property is established in Milne and Laurent–Schröer. Proper connected varieties have no nonconstant maps to affine groups over a field, but that observation is not a blanket relative theorem.',
  'The unrestricted target category in the margin is not fixed, so it is not declared solved by the abelian theorem.',
  'Medium; specify whether targets are smooth connected group schemes and whether the base is a field.',
  ['R_Milne2008','R_LaurentSchroer2024'])
P(671,'Canonical curve duality versus theta polarization',[671,673],
  '59:24–25 asks whether the canonical duality is the theta polarization and tentatively inserts a sign;59:27 repeats “question de signe”.',
  'Compare the diagonal-induced map with t_x^*L⊗L^{-1} after fixing the Albanese/Picard torsor action.',
  'Jacobian autoduality is classical. The theta-pair formulation andL↦K⊗L^{-1} give concrete checks.',
  'No intrinsic negative-polarization conclusion follows from translating versus pulling back the divisor; the conventions have to be matched.',
  'High; calculate the degree-one Abel map for a pointed curve and compare the two induced homomorphisms.',
  ['R_Milne2008','R_PoonenStoll1999','R_Alexeev2002'])
P(672,'Canonical theta torsor for a principally polarized abelian scheme',[672],
  '59:26–28 constructs the unique A-equivariant pair(P,Θ) and its identification withPic^δ.',
  'State the principal-polarization theta-pair equivalence over the base and distinguish it from arbitrary polarization-type torsor existence.',
  'Alexeev2002§3.0.5–3.0.10 gives the explicit construction and equivalence. Laga2025 shows why broad arbitrary-type extrapolations require care.',
  'The principal theorem is established; modern arbitrary-type obstructions do not contradict it.',
  'High historical match; compare the evaluation-at-zero divisor in the two constructions.',
  ['R_Alexeev2002','R_Laga2025'])
P(674,'General separatedness of the correspondence functor',[674,608],
  '“I am convinced however that Corr is always separated” (57:23);57:32 asks the same question and proposes a fundamental-group specialization route.',
  'For proper flatX,Y with universalH⁰=O, determine separatedness of normalized divisorial correspondences, including reducible fibres and algebraic-space Picard functors.',
  'Murre1965 Th4 assumes separatedness and records the unrestricted assertion as a problem; separatedPic of either factor is a sufficient case. Modern algebraic-space representability suggests a route through the letter’s pre-ét case.',
  'The cited Murre theorem does not by itself settle the general question. The full modern comparison is being treated as an exact-hypothesis question, not inferred from the theorem title.',
  'High; check whether Artin’s Picard-space theorem supplies every hypothesis of the letter’s pre-ét argument.',
  ['R_Murre1966','R_FGA232','R_Kleiman2005'])
P(676,'Local Picard theory without regular puncture',[676],
  '57:13 conjectures a localPicard scheme without regularU and proposes countability/separable-extension invariance whenH²_m(A)=0.',
  'Separate existence, tangent identification, discreteness, countability of components and invariance after completed scalar extension.',
  'Boutot/Kollár establish a substantial geometric version underS₂, pure dimension≥3 and essential finite type over a field.',
  'Tangent vanishing alone proves neither representability nor countability; the unrestricted complete-local formulation is not verified by that result.',
  'High; begin by matching the exact test functor and coefficient-field assumptions, then examine countability independently.',
  ['R_Boutot1978','R_Kollar2014'])
P(677,'A relative quasi-affine but non-affine Picard pullback',[677],
  '57:74 asks for a counterexample over a dimension-one base, either smooth projective birational or finite normal; the handwritten duplicate qualifies the smooth case.',
  'Find a family satisfying the requested hypotheses for which the induced Picard pullback is quasi-affine but not affine.',
  'SGA6XII Remark1.7 still leaves general relative affineness open there. The targeted search found no exact matching counterexample.',
  'This is bounded non-identification, not a claim of global mathematical novelty or current unsolved status.',
  'Medium; first check the correction “impossible ifX smooth” in the duplicate and narrow to the surviving finite-normal configuration.',
  ['R_SGA6','R_Murre1966','R_Kleiman2005'])
P(681,'Incomplete acyclic line-bundle moduli sketch',[681],
  '57:16 ends “Une telle donnée ...” before giving the alleged equivalence.',
  'Specify the marked section, acyclicity, base-change hypotheses and quotient relation before asking representability.',
  'FGA’s Div/Pic construction is a plausible surrounding framework; the exact unfinished functor is not identified.',
  'The obstacle is missing formulation, not evidence of an open representability theorem.',
  'Low research priority; consult the scan and adjacent sheets first.',
  ['R_FGA232','R_Kleiman2005'])
P(682,'An abstract functorial rigidity criterion',[682,678],
  '57:30–32 says to reformulate the theorem, leaves the valuative condition blank and ends “Demander Mumford”.',
  'Give an exact functor category and conditions making the fibrewise constancy locus both open and closed.',
  'Representable group targets satisfy standard rigidity; Murre’s criterion gives a precise related representability theorem.',
  'The blank closedness condition is essential. An open locus on a connected base need not equal the entire base.',
  'Medium; write the missing valuative statement before seeking a modern generalization.',
  ['R_Murre1966','R_Milne2008'])

P(686,'Locally free conormal module and smoothness in characteristic zero',[686],
  '57:64 asks whether a group scheme over a base with characteristic-zero residue fields is smooth along its unit when its conormal module is locally free.',
  'Add the explicit local finite-presentation hypothesis along the unit, then the stated condition is equivalent to smoothness there.',
  'SGA3 VI B Proposition1.6 states exactly this equivalence; the proof uses the invariant-differential pullback and the EGA IV smoothness criterion.',
  'Settled in the later published theorem. No flatness assumption needs to be invented to apply that proposition.',
  'High historical value, low new-research value; align this question with Proposition1.6 and keep it distinct from the full Picard-functor question.',
  ['R_SGA3VIB','R_EGAIV4'])

# Mathematical alarms only. No scan images were supplied and no transcription is edited.
reading('A57-01',4,40,'kernel in the definition ofQ','cokernel of the exceptional lattice map, if this is the intended construction','C-SA14-601/602: the displayed quotientPic(X)/D and the subsequent exact sequence require a cokernel. Mathematical candidate only; ink unresolved.')
reading('A57-01',7,90,'R^4 f_* in the coherent-support argument','R^1 f_*','C-SA14-603/605: the group of global sections is explicitlyH¹(X,O_X). The cohomological degree must be1 in that argument.')
reading('A57-01',11,165,'Pic(U completed-base-change)/Pic(B) identified withQ(B) without qualification','an injection with descent obstruction on the stated test category','C-SA14-602/605: the next sentence retainsBr(B), and earlier pages retain the twisted-lattice obstruction. Do not erase these qualifications.')
reading('A57-02',20,9,'Y→Z in the faithfully-flat factorization','X→Z','C-SA14-679 and Murre§3A Cor2: the factorization of f:X→Y has sourceX and quotientZ.')
reading('A57-02',20,13,'G finite type; conclusionG/H flat','addG-flatness for the flatness conclusion','C-SA14-680: Spec k[[π]][x]/(πx,x^p), withH=e, meets the written assumptions and is not flat. This is an omitted-hypothesis alarm.')
reading('A57-02',77,97,'Pic_X/S→Pic_X/S forf:X′→X','Pic_X/S→Pic_X′/S','C-SA14-620; typed duplicate57:74 line54 has the contravariant targetX′, confirmed by SGA6XII1.1.')
reading('K57-01',25,333,'f₂:X₂→X','f₂:X₂→G','C-SA14-678: both factors in the product decomposition take values in the target groupG.')
reading('K57-01',26,360,'f−f₂p₂ while the group need not be commutative','ordered product f·(f₂p₂)^{-1}, with the chosen factor order fixed','C-SA14-678: the source explicitly warns about noncommutativity; additive symbols conceal an order convention.')
reading('K57-01',26,362,'invocation of hypothesis c) absent from the surviving displayed theorem','identify the intended connectedness/density hypothesis from the edits','C-SA14-678: the proof uses c) to pass from a neighbourhood to the whole product. Do not manufacture a unique full statement from the fragment.','high','low')
reading('K57-01',27,372,'g:X→Y althoughg(X_y)⊂Z_y','g:X→Z','C-SA14-678: the finite-image and factorization statements requireg to take values inZ.')
reading('K57-01',32,491,'u₂:X→G in the second product factor','u₂:Y→G','C-SA14-682: u₂ is composed with the projectionX×Y→Y.')
reading('K57-01',32,495,'L a line bundle onX, trivialized on two axes ofX×Y','L onX×_S Y','C-SA14-674: both the restrictions and generic triviality are stated on the product.')
reading('K57-02',44,274,'uncertain noncommutative in the power-map proposition','commutative, or a substantially different statement','C-SA14-611: the smooth characteristic-zero groupGL₂ has a positive-dimensional family of involutions. The ambiguous word cannot be settled from mathematics alone.','critical','medium')
reading('K57-03',51,28,'all connected closed subgroup schemes in the very-rigid definition','clarify whether smooth/reduced connected subgroups are intended','C-SA14-614: μ_p⊂G_m in charp has no schematically dense prime-to-p torsion. The intended subgroup class is essential.')
reading('K57-03',58,228,'surjective homomorphism of base-flat groups, thereforeflat','fpqc or schematically faithful quotient hypothesis','C-SA14-613/683: Spec k→α_p is topologically surjective and both objects are flat overk, but the map is not flat.')
reading('K57-04',68,81,'(D−K)·H≥0 suffices to eliminateH⁰(K−D)','strictly positive in this Riemann–Roch argument','C-SA14-617: D=K=−3H onP² satisfies the displayed nonstrict conditions but has no sections.')
reading('K57-04',68,85,'χ(D)≥0 impliesh⁰(D)>0','χ(D)>0 after the dual term is killed','C-SA14-617: a nonnegative lower bound does not force positive dimension. Both strict inequalities hold for the eventual ample twists used later.')
reading('K57-04',68,87,'the conditions hold forΔ numerically equivalent to0','the conditions hold forD+Δ','C-SA14-617: intersection numbers and Euler characteristic are transferred fromD toD+Δ, not toΔ alone.')
reading('K57-04',70,129,'b₁=b₃=dimPic','b₁=b₃=2dimPic⁰_red','C-SA14-619; abelian-surface Betti vector(1,4,6,4,1), and SGA6XIII5.3.')
reading('K57-04',70,133,'b₂=E−2+2p withp=dimPic','b₂=E−2+4p','C-SA14-619: alternating sum of Betti numbers and the primary SGA6XIII5.3 formula agree.')
reading('K57-06',206,428,'one aⁿ is closed as a torsion criterion','the intended finite-orbit or bounded-exponent condition must be recovered','C-SA14-629: points of an étale component group are already closed over an algebraically closed field, even for nontorsion components.')
reading('K57-06',206,438,'existence of an open subgroupH containing the powers','require the finiteness condition that makes the criterion nonvacuous','C-SA14-629: H=G otherwise satisfies the condition for every element; the adjacent finite-type subset formulation is meaningful.')
reading('K57-07',214,45,'Picard restriction targetH¹(O_X′₀)','H¹(O*_X′₀)','C-SA14-632: the map classifies line bundles, so its coefficient sheaf is the multiplicative units.')
reading('K57-07',215,58,'D₁ restricted toD₁ has degree+1','degree−1','C-SA14-632: D₁+D₂ is a principal fibre andD₁D₂=1, henceD₁²=−1. Exact intersection calculation supplied.')
reading('K57-07',217,96,'restriction toH¹(U,O*) in the kernel description','restriction toH¹(X_U,O*)','C-SA14-632: the kernel concerns line bundles on the total family restricted away from the special fibre, not just line bundles on the base.')
reading('K57-07',217,104,'not representable, withpas deleted','representable, as in the surviving sentence and final57:219 construction','C-SA14-633: authorial cancellation is mathematical provenance, not an invitation to restore the withdrawn word.')
reading('K57-07',220,141,'absolutePic of a relative cone isZ','relativePic, or impose a base with trivialPic','C-SA14-634: pullbacks from a base withPic(S)≠0 provide an omitted summand.')
reading('K57-07',221,153,'generic quadricPic=Z² without field/splitting qualifiers','geometric or split smooth quadric, withchar≠2 in this equation','C-SA14-634: a nonsplit quadric or characteristic2 is not the displayed split smooth example.')
reading('K57-07',224,227,'H¹ coherent cohomology computed by the closed component Čech complex','closed-cover descent needs additional exactness; the literal computation fails','C-SA14-635: atτ=0 naiveČechH¹=0 while the plane cubic hasH¹(O)=k.','critical','high')
reading('K57-08',136,103,'Cohen–Macaulay over a regular local ring meansfree','maximal Cohen–Macaulay, for a finite module','C-SA14-638: k overk[[t]] is Cohen–Macaulay of dimension0 and is notfree.')
reading('K57-08',138,141,'L⊗f*(g*L) in normalization','L⊗f*(g*L)^{-1}','C-SA14-639: pulling the proposed normalization back byg must giveO_S.')
reading('K57-09',153,101,'sum overg_i≥1 plus a separate elliptic sum','g_i≥2 in the first sum, if the separate elliptic term is retained','C-SA14-644: otherwise elliptic vertices are counted twice inΣ(3g_i−3+ν_i).')
reading('K57-09',159,380,'products c_i a_j alone generate the algebra','retain the original algebra generators as well as generators of the nilpotent ideal','C-SA14-645: A=k[ε]/ε²,B=A[t]; reducing the proposed products moduloε cannot generatet. PublishedEGA0.7.5.5 retains the algebra generators.')
reading('K57-09',160,429,'rankN direct image followed by targetP^N','clarify rankN versus projective dimensionN−1','C-SA14-646: projectivizing a rankr vector bundle has fibreP^{r−1}; this may be a notation convention rather than an ink error.')
reading('K57-10',164,49,'H¹(O_X) afterH¹(L|D)','H²(O_X)','C-SA14-647: the long exact sequence of0→O_X→L→N_D→0 determines the next degree.')
reading('K57-10',170,144,'dropping the affine-target restriction in the polar-locus statement','retain affine target for regular-function detection; proper targets allow codimension-two indeterminacy','C-SA14-649: [x:y]:P²⇢P¹ has a single codimension-two basepoint.')
reading('K58-01',3,11,'dimension bounds alone imply connected punctured hypersurface','also require the relevant connectedness of the original puncture','C-SA14-650: the complete fibre product of two three-dimensional regular locals has disconnected puncture and disconnected cuts.','critical','high')
reading('K58-02',13,75,'connected in dimension≤k−1','connected in dimension≥k−1, if the inductive lower-bound statement is intended','C-SA14-651/652: SGA2XIII2.1 and the induction require a lower connectedness bound; scan inspection remains necessary.')
reading('K59-01',9,303,'determinant class equals positive theta without declared convention','standard alternatingdet gives−theta; inversedet gives+theta','C-SA14-659: independent exterior-algebra andGRR calculation. The ambiguousdet* notation must be resolved before any source emendation.')
reading('K59-01',10,317,'universalPic sections generated byK, including markedgenus1','add the marked-point generator and separate low genera','C-SA14-660: on the universal pointed elliptic curveK is trivial, whileO(mark) has degree1.','critical','high')
reading('K59-01',10,319,'Chow codimensioni maps tog−i in all grades','CH^i_s maps toCH^{g−i+s}_s','C-SA14-661: Beauville1986 Prop1; a nonzeroPic⁰ class gives the first discrepancy.')
reading('K59-01',11,368,'φ(φ(δ))=δχ(δ)^{g−2}','factor(−1)^g forφ=−adj, or use the positive adjugate twice','C-SA14-662: diagonal matrices ing=2,3,4 were recomputed; theg=3 sign differs.')
reading('K59-01',11,373,'dual adjugate polarization always indivisible','divide by the appropriate elementary-divisor factor; fix polarization type','C-SA14-663: type(1,2,2) gives adjugate(4,2,2), divisible by2.')
reading('K59-01',13,432,'ppcm ofλ^g−λ^{g−1} equals2','pgcd for g≥2','C-SA14-664: all these numbers are even and their gcd is2; their least common multiple is not2.')
reading('K59-01',13,452,'evenχ impliesδ is divisible by2','no such implication; keep torsor annihilation separate','C-SA14-665: type(1,2) hasχ=2 and primitiveδ.','critical','high')
reading('K59-01',14,495,'ppcm after deletedpgcd forχλ^g−λ^{g−1}','pgcd of the annihilator family','C-SA14-664: the ideal generated by the annihilating integers is the relevant object; its positive generator is1 or2 according to parityχ.')
reading('K59-01',14,508,'Pic_B^δ withδ anNS class onA','verify whetherδ′ onB orPic_A^δ is intended','C-SA14-664/666: the polarization class and the base of its Picard component must have matching domains.','high','low')
reading('K59-02',16,68,'rankρ term becomes1 in the curve Chern character','ch(F)=ρ+c₁(F)','C-SA14-668: rank-twoO⊕O already gives a contradiction to the following rank-one formula.')
reading('K59-02',16,82,'χ_F=1−g+d+c and unchangedtheta class','χ_F=ρ(1−g+d)+c andtheta class multiplied byρ','C-SA14-668: exact curveRiemann–Roch calculation, including elliptic rank-two example; theta equality at line88.')
reading('K59-02',17,114,'Chern-character sum beginning ati=1','include the rank terma₀','C-SA14-667/668: in dimension1 the omitted term supplies the entire Fourier degree-two contribution.')
reading('K59-02',17,129,'homomorphism in the line-bundleNS class','polynomial map inδ; additivity is inK₀ coefficientF','C-SA14-667: on a principally polarized threefoldφ(2δ)=4φ(δ), not2φ(δ).')


