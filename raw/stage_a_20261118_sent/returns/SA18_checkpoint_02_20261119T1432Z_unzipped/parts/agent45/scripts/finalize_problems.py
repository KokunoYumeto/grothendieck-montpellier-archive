"""Hand-edited prose and exact-source refinements for the problem index."""
from pathlib import Path
import json
OUT=Path(__file__).resolve().parents[1]
ps=json.loads((OUT/'problems.json').read_text())
by={int(p['id'].split('-')[-1])-45000:p for p in ps}
def put(n,stated,today,art,worth,refs=None):
    by[n].update(as_he_states=stated,plausible_today=today,state_of_art='As of 19 November 2026: '+art,worth=worth)
    if refs is not None: by[n]['refs']=refs
put(29,'Equation (34) is deferred to §6, no. 4; the subsequent pairing is expressly said not to determine contraction uniquely.',
    'For finite projective modules, perfect duality proves the shuffle and contraction identities. For arbitrary modules, define contraction by the coproduct and then verify its pairing property.',
    'The exterior-algebra identities are standard. The universal shuffle argument and the finite coefficient certificates in exterior_checks.py verify the manuscript conventions; the example M=Z/2 explains the nonuniqueness warning.',
    'A sign and index appendix would help the next scan review; the identities themselves are settled.')
put(30,'Lemmas 1–4 try to lift torsors by reducing an epimorphism to commutative kernels, smooth parts, and radicial parts.',
    'Retain the perfect-field hypothesis in the Grothendieck–Springer theorem. An imperfect-field statement in flat cohomology must quantify the vanishing for every required twist and extension.',
    'Flicker–Scheiderer–Sujatha, Introduction and §3, gives the developed perfect-field result. The manuscript’s Cartan-normalizer argument fails under its natural reading; that proof failure alone does not refute the theorem being sought.',
    'A focused audit could identify the first reduction that needs an extra hypothesis.')
put(31,'Conjugacy of Cartan subalgebras is invoked to deduce N_G(h)K=G.',
    'Distinguish conjugacy under G from conjugacy under the infinitesimal normal subgroup K. The former does not imply the displayed equality.',
    'For G=SL₂ over an algebraically closed field of characteristic p>2, K=ker(F), and h=Lie(T), the reduced part of N_G(h)K is N_G(T), which is smaller than G. SGA3 VIIA §7 supplies the height-one group-scheme setting.',
    'An explicit correction is useful because it isolates a failed proof step without overstating the conclusion.')
put(32,'The page asserts H^i(k,α_p)=0 for all i and reduces finite commutative coefficients to Brauer vanishing.',
    'Replace all i by i≥2 unless k is perfect. For μ_p, retain the relevant Brauer hypotheses in flat cohomology.',
    'The flat Frobenius sequence and Stacks Proposition 35.9.3 give H¹(k,α_p)=k/k^p and H^i(k,α_p)=0 for i≥2. Harari Remark 2.52 explains why ordinary p-cohomological dimension does not control every flat coefficient over an imperfect field.',
    'Checking the quantifier on the scan could resolve the discrepancy immediately.', ['AG45-StacksQC','AG45-Harari2024'])
put(33,'An algebraic kernel should have a neutral H² class under the vanishing hypotheses; the proof proceeds by induction.',
    'For perfect fields of cohomological dimension at most one, use continuous algebraic kernels and the Grothendieck–Springer neutrality theorem. Other bases and topologies require separate statements.',
    'Flicker–Scheiderer–Sujatha §1 repairs a continuity issue in Springer’s formulation, and §3 gives the theorem. The implication “perfect group, therefore centreless” in the draft is false: SL₂(F₅) is a counterexample.',
    'Comparing the draft induction with the published kernel formalism would clarify both the mathematical correction and its history.')
put(34,'Can a kernel on a site be represented by a group sheaf? The I/Z and normalizer quotient labels remain uncertain.',
    'Specify the band and its outer action. Realizing a band by a group and neutralizing a gerbe are different obstruction problems.',
    'Giraud’s book supplies the general framework; its metadata and chapter structure were checked. CCMT §3.5 was read for the relevant nonabelian exact-sequence formalism. The damaged label prevents matching a unique obstruction theorem.',
    'Recovering the notation is the necessary first step; the general theory already exists.')
put(35,'A characteristic-two matrix example is intended to show that a radical is not defined over k; later root criteria are cancelled.',
    'Separate the scheme-theoretic centre, which is defined over k, from its geometrically reduced connected part, which may fail to descend over an imperfect field.',
    'The displayed defining ideal verifies this distinction directly. Modern algebraic-group theory treats the central subgroup scheme and smooth geometric radical separately. The cancelled root criterion is not retained as a theorem.',
    'The small explicit example could make the terminology and the reason for imperfect-field hypotheses clear.')
put(36,'The map from the flag variety to a Grassmannian should be a closed immersion when the Lie normalizer equals the Borel; several rank criteria are cancelled.',
    'For a proper flag scheme, geometric injectivity and an injective tangent map suffice. The tangent condition involves the normalizer of Lie(B), and can fail in small characteristic.',
    'SGA3 XXII and Conrad §5.2 establish the flag scheme. The displayed sl₂ calculation in characteristic two exhibits failure of this particular Grassmannian immersion.',
    'A rank-one classification could be completed in a few hours and would separate a bad embedding from failure of the flag variety itself.')
put(37,'The note sketches smoothness of Pic⁰ or Picτ near an abelian fibre; a proposed finite torsion bound is cancelled.',
    'Use the precise proper, flat, and smooth hypotheses for Picard representability and openness. Do not infer locally constant Néron–Severi rank in every family.',
    'FGA VI and Kleiman §§5–6 give the Picard-component framework. The isolated-fibre and cancelled finite-bound formulations require the actual surviving hypotheses.',
    'A comparison with c49 and the published Picard construction would resolve the intended scope.')
put(38,'The author says that he does not know whether coherent cohomology, Picard representability, and smoothness at the unit hold without projectivity.',
    'These statements hold for arbitrary abelian schemes. Projectivity remains a separate property.',
    'Lan Theorem 1.3.2.3 and Proposition 2.1.5.14 give the modern statements, with their historical references. Kleiman Remark 5.24 records nonprojective abelian schemes even over dual numbers in characteristic zero.',
    'The question is settled and historically useful: a commentary should give three positive answers without adding a false projectivity inference.')
put(39,'The margin asks for a version over a local base with nilpotent radical; the F/G reading in the flatness lemma is uncertain.',
    'First recover the Noetherian module lemma, then state any Artinian variant with finite-presentation or explicit Tor hypotheses.',
    'Stacks Lemma 10.99.1 and Lemmas 10.99.9–10 give the fibre-injectivity and associated-graded mechanisms. They cannot decide which letter was written.',
    'A short algebra and scan review could produce a precise lemma; an unrestricted version should not be supplied.')
put(40,'Translation invariance should imply algebraic triviality; part of the proof is deferred.',
    'For an abelian scheme, rigidified primitive line bundles correspond to Pic⁰ and to extensions by G_m.',
    'Lan §1.3.2 and §3.2.3, and Booher §2 on Barsotti–Weil, give the completed construction with rigidification.',
    'This is a commentary task: state the field argument and the relative sheaf convention precisely.')
put(41,'A category with duality κ and an antisymmetric object N(A) is introduced, but its signs are unfinished.',
    'With standard biduality, polarizations are symmetric. A signed biduality could change the formal adjective and must be specified before comparing formulas.',
    'Lan Lemma 1.3.2.13 verifies symmetry from the Poincaré bundle. The incomplete κ convention does not identify a unique published abstract category.',
    'A notation audit tied to the c50 block matrix is more useful than extending an unspecified categorical programme.')
put(42,'The mixed-characteristic specialization example is questioned; an equal-characteristic moving-line construction is then added.',
    'The α_p² construction over k[[t]] gives finite flat subgroups whose generic intersection is trivial and whose special fibres coincide.',
    'The Hopf-algebra calculation verifies the moving-line construction. Koizumi–Shimura, pp. 204–205, also gives a mixed-characteristic example of a subgroup whose specialization is a multiple of a smooth subgroup. Extending a homomorphism need not preserve closed immersion.',
    'A complete presentation of the author’s repair and its historical counterpart would be useful.', ['AG45-SGA3VIIA','AG45-KS1959'])
put(43,'Can normality of S be replaced by reducedness? The margin proposes a unibranch condition.',
    'Geometric unibranchness and the finite unramified extension criterion are relevant. A merely reduced base can have branch-gluing obstructions.',
    'Bertolin Propositions 1.3.1 and 1.3.5 use the unramified Hom scheme and geometric unibranchness, citing EGA IV 18.10.1. This does not establish every subgroup-extension statement over an arbitrary reduced base.',
    'A nodal-base counterexample or a corrected subgroup theorem would make a manageable separate task.', ['AG45-Bertolin2009','AG45-EGAIV4'])
put(44,'Can a proper group scheme over a characteristic-zero base have a greatest abelian subscheme, especially when the base is reduced?',
    'Over a characteristic-zero field, the identity component of a proper group scheme is an abelian variety. Over a base, flatness and control of component dimension are additional issues.',
    'SGA3 VIB gives relative connected components under explicit flatness or smoothness hypotheses. It does not settle the unrestricted proper, possibly nonflat question as written.',
    'Begin by testing a proper group with jumping fibre dimension and formulate the required hypotheses.')
put(45,'Existence of Hom is assumed conditionally; local unramifiedness and local properness are queried.',
    'For abelian schemes A and B over S, Hom(A,B) is represented by a separated unramified scheme, locally of finite presentation and essentially proper.',
    'Bertolin Proposition 1.3.1 gives the result using Artin representability, rigidity, and the Néron property. Each geometric fibre is a constant group scheme; its rank need not be constant as the base point varies.',
    'The result is settled; careful explanation of essential properness would improve the manuscript commentary.', ['AG45-Bertolin2009'])
put(46,'The generic relative curve is invoked as known to exist; generation and surjectivity remain questions.',
    'Construct a smooth relative curve whose generic Jacobian surjects onto A_K under the precise regular-in-codimension-one and geometric-integrality hypotheses, including any necessary base extension and descent.',
    'Koizumi–Shimura Theorem 4, p. 200, proves good reduction of a quotient once that curve has been constructed. The exact weakened singular hypotheses in the Bertini step are not established by this quotient theorem. Koizumi 1960 remains a historical lead with metadata verified but full text inaccessible.',
    'Isolate the Bertini step as one task; it is the gap rather than the known quotient criterion.', ['AG45-KS1959','AG45-Koizumi1960','AG45-Robert2023'])
put(47,'The proposed relative abelian part of Pic⁰ uses constancy of dimension; a margin asks whether it works for a nonsmooth family.',
    'For a smooth proper family in characteristic zero, Pic⁰ is an abelian scheme. For fibres only normal or smooth in codimension one, constancy of Picard dimension and the scheme-theoretic immersion require separate arguments.',
    'FGA VI and Kleiman give the smooth proper case and precise more general hypotheses. The broader singular-fibre formulation remains explicitly uncertain in the manuscript.',
    'A hypothesis audit of c51:19–22 would prevent an overly broad relative Picard theorem.')
put(48,'After prime-to-p torsion is excluded, the author says that the remaining case needs closer inspection.',
    'The remaining finite kernel is p-primary. In positive characteristic this does not imply that it is trivial.',
    'The prime-to-p étale torsion argument proves the reduction. The α_p collisions on c51:13 explain why infinitesimal p-primary kernels require additional control.',
    'An explicit family could identify the missing smoothness condition and delimit the characteristic-zero proof.')
put(49,'Is Picτ proper? Is Pic a disjoint union of proper open subschemes? A margin warns about families that exist only formally.',
    'State properness and finite-type criteria with their geometric-integrality or normality hypotheses. Openness of components, jumping components, and algebraization are separate assertions.',
    'FGA VI and Kleiman §§5–6 give precise criteria. They do not imply the sweeping conclusion after the manuscript’s hypotheses are cancelled.',
    'Split the question into properness, openness, and component decomposition before looking for examples.')
put(50,'Study kernels and images of homomorphisms of abelian or multiabelian schemes over nonreduced bases.',
    'Flatness and constant-rank hypotheses are needed to ensure that an image or quotient remains an abelian scheme; arbitrary kernels may jump.',
    'Lan’s isogeny theory and Robert Proposition 2.3.15 give positive cases. The α_p collision provides a concrete obstruction to preserving a generic closed immersion.',
    'One deformation calculation with finite flat kernels could make this broad programme precise.')
put(51,'A preabelian scheme over a regular base is declared projective and isotrivial under its translation group.',
    'Recover the definition of preabelian and the local or global meaning of projective. Representability of the torsor and the existence of a polarization cannot be omitted.',
    'Raynaud’s 1970 book, Chapters XII–XIII, develops nonprojective examples and abelian torsors; its contents were verified. Kleiman Remark 5.24 and BCS §4.2 provide exact modern boundaries. The manuscript’s terminology is insufficient for a unique theorem.',
    'A terminology and locality audit is needed before proposing a corrected theorem.')
put(52,'The bad-reduction locus for a torsor should have pure codimension one; H¹(S,G) should inject into H¹(K,G).',
    'For regular S, a closed subset Z of codimension at least two, and an abelian scheme G/S, restriction gives an equivalence of the categories of G-torsors on S and on S minus Z.',
    'Bouthier–Česnavičius–Scavia §4.2, formula (4.2.0.1), proves this using finite flat torsor purity and generic full faithfulness. It does not assert that a new abelian scheme extends.',
    'The question is settled and should anchor the distinction from abelian-model purity.', ['AG45-BCS2025'])
put(53,'The final question asks for analogous purity of good reduction for abelian schemes.',
    'Add healthy-regularity or explicit ramification hypotheses. Regular mixed-characteristic bases without such conditions admit counterexamples.',
    'Vasiu–Zink Theorem 3, Corollaries 4–5, and Theorem 28 give positive criteria and counterexamples. Their regular two-dimensional example refutes unrestricted extension from a punctured spectrum.',
    'A direct comparison with fixed-group torsor purity would clarify an easy but consequential conflation.')
put(54,'An automorphism lemma and its duality reduction remain to be formulated.',
    'For a curve of genus at least two, an automorphism acting trivially on its Jacobian is the identity. A translation preserving its Abel–Jacobi image is consequently zero.',
    'Milne, Jacobian Varieties, Theorem 12.1 and its faithful-action consequences give the standard result. The manuscript’s Lefschetz argument requires 2−2g, not 2g−2.',
    'A correct sign and an explicit functor statement would complete a useful explanatory lemma.')
put(55,'The general criterion for passing from embedded curves to their translation quotient is left to extract.',
    'Under the specified marking or level structure, quotient the connected Abel–Jacobi Hilbert component by its free Jacobian translation action.',
    'Ricolfi Theorem 3.6 and §3.2 identify the quotient factor with the Torelli fibre in characteristic different from two. The manuscript’s auxiliary functors still require explicit definitions.',
    'Matching the functors to Ricolfi’s fibre is a bounded task that could make the descent argument reviewable.')
put(56,'Duality compatibilities should be written explicitly; the hyperelliptic cokernel is assigned dimension one.',
    'The Torelli codifferential is multiplication Sym² H⁰(K_C)→H⁰(K_C²). In characteristic different from two, the cokernel has dimension g−2 for a hyperelliptic curve and is zero for a nonhyperelliptic curve.',
    'Ricolfi §1 and Theorem 1.1 give the tangent criterion. The double-cover calculation in math_checks.py verifies the genus dependence directly.',
    'An explicit duality diagram would turn a misleading dimension assertion into a precise map.')
put(57,'The first radicial assertion is withdrawn, and the hyperelliptic fibre is described as dual numbers.',
    'In characteristic different from two, the fibre is Spec k[s₁,…,s_(g−2)]/(s₁,…,s_(g−2))². Dual numbers occur exactly when g=3.',
    'Ricolfi Theorem 3.6 and §3.2 determine the scheme structure using Oort–Steenbrink’s local Torelli theorem. Tangent dimension alone would not prove the square-zero equations.',
    'The exact correction is settled and merits prominent commentary alongside the separate sign ambiguity.')
put(58,'The good-reduction argument uses minimal theta degree and irreducibility of theta to extend the curve.',
    'Retain the principal polarization and a special fibre that is a smooth curve’s polarized Jacobian. Good reduction of the Jacobian alone permits reducible stable curves of compact type.',
    'Ricolfi Theorem 1.2 gives the minimal-class input. The compact-type reduction discussion in Robert §3.2 explains the product obstruction; its stronger “iff absolutely simple” sentence is not used. The exact DVR descent hypotheses remain part of the comparison.',
    'Check the descent step and the indecomposable polarization condition in one focused run.')
put(59,'Corollary 2 is marked “faux sous cette forme”.',
    'Strong Torelli reconstructs curves geometrically, but a prescribed polarized-Jacobian isomorphism may require multiplication by −1. Any marked descent statement must respect this ambiguity.',
    'Milne Theorem 12.1(b) gives the sign distinction between hyperelliptic and nonhyperelliptic curves; Ricolfi §2 gives the local quotient framework.',
    'A corrected corollary and descent diagram would explain the author’s withdrawal without reinstating it.')
for p in ps:
    p['state_of_art']=p['state_of_art'].replace('As of19November2026:', 'As of 19 November 2026:')
c=next(c for c in json.loads((OUT/'claims.json').read_text()) if c['id']=='CL-SA18-45204')
ps.append(dict(id='MP-SA18-45060',title='Completion invariance of local torsor obstructions',occurrences=[{'claim':c['id'],'cote':c['cote'],'scans':c['scans'],'lines':c['lines']}],as_he_states='The local obstruction quotient for an abelian torsor is said not to change after completing the discrete valuation ring.',plausible_today='Specify whether the ring is henselian or excellent, and compare H¹(K,G)/H¹(R,G) with the completed pair. Distinguish this quotient from H¹(K,G) itself.',state_of_art='As of 19 November 2026: Česnavičius’s 2020 report, Theorems 1.4 and 2.1, gives completion and henselian-pair invariance for specified cohomological functors. The smooth quasi-affine hypothesis in Theorem 2.1(a) excludes an abelian scheme, and the finite-flat statement is in degrees at least two. These results therefore do not settle the unrestricted quotient written here. BCS §4.2 is torsor purity across codimension at least two, a different operation.',why_open='The margin does not state the needed local hypotheses; no historical explanation for leaving it open was found.',worth='Worth a separate local-cohomology audit because completion invariance must not be inferred from the purity theorem.',refs=['AG45-Cesnavicius2020','AG45-BCS2025']))
(OUT/'problems.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'problems':len(ps),'hand_edited_rows':31,'new_problem':'MP-SA18-45060'}))
