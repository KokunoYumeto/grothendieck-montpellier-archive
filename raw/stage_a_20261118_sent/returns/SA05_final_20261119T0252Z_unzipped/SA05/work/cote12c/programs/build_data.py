"""Serialize manually curated late-cote12 judgments; never infer verdicts from headings.
All prose below was composed after reading entries and source passages in full.
"""
import csv,json
from pathlib import Path
BASE=Path('SA05/work/cote12c'); BASE.mkdir(parents=True,exist_ok=True)
P='sources/texts/pro/MPL_12_099-149_transcription.tex'
PK='MPL_12_099-149#'
items=[]; claims=[]; problems=[]; events=[]
def add(n,src,kind,loc,words,statement,reconstruction,check='agrees',reason=''):
    scans=[]; lines=[]
    for scan,interval in loc:
        scans.append(scan); lines.append({'file':P,'scan':scan,'lines':interval})
    items.append(dict(id=f'SA05-{n}',sources=[PK+str(k) for k in src],kind=kind,cote=12,scans=scans,lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))

add(3001,[1],'idea of the earlier run',[(99,'7-46'),(140,'1179-1237'),(149,'1598-1625')], 'No manuscript quotation for the results-register statuses.',
 'The earlier run records contextual projects and internal status labels; none becomes a manuscript theorem or a checked external theorem merely by being listed.',
 'Current consolidation retains LM6 A.22/A.50, LM7 C.1/C.5/C.8/E.23, FLAGGED_149 B9, ANABELIAN_SUCCESSOR A.3, LM1 A.8, WG2 and returned-package IDs solely as provenance leads.', 'not on the page', 'The entry itself labels these as prior-run material; its status labels have no primary witness in this part.')
add(3002,[2,96,97,100,101,102],'title, date or page count',[(99,'2-46'),(139,'1170-1177'),(143,'1328-1335'),(149,'1595-1625')], 'Filtration et poids; Motifs lisses; Enveloppes pseudo-abéliennes',
 'The retained faces comprise weights/admissibility, smooth integral motifs, and the opening of abstract pseudo-abelian envelopes. There are36 retained scan faces, not51 continuous manuscript pages. Internal numbers and headings do not assert a total length.',
 'Current inventory uses scanpage markers; manuscript titles are distinguished from archive names and the unsupplied later continuation of the envelope unit.', reason='The text supports the three units; no period conjecture or motivic Galois exact sequence occurs in these retained faces.')
add(3003,[3],'unpursued implication',[(99,'24-27'),(105,'139-179'),(106,'185-215')], 'Nombres de Betti virtuels de Serre',
 'The alternating dimensions of weight-graded compactly supported cohomology define additive virtual Betti numbers after a compatible weight formalism is supplied; this invariant loses extension data.',
 'The additive formula is a present reconstruction of a named programme, not a displayed formula on99.', reason='The earlier note accurately separates the named programme from the reconstruction and from any birational reconstruction claim.')
add(3004,[4,61],'self-flagged step',[(140,'1179-1206'),(142,'1319-1327')], "il n'est pas du tout clair comment définir l'image inverse",
 'Generic-field rational motives together with unramified l-adic lattices do not yet define specialization to a closed point, hence do not supply arbitrary base pullback.',
 'A field extension can define generic pullback; a closed-point specialization needs additional geometry. Modern six-operation theories are comparisons, not substitutes for this definition.', reason='The source explicitly describes this obstacle; the earlier-run links are retained separately.')
add(3005,[5],'unproved claim',[(99,'24-25'),(105,'168-179'),(106,'187-215')], 'le plus grand quotient ... de poids i',
 'For proper singular X, the quotient H^i(X)/W_{i-1} is the image in H^i(Y) for a proper surjective smooth Y→X; for smooth open X, the weight-i subspace is the image from a smooth proper compactification.',
 'The modern canonical weight-filtration statement distinguishes a quotient on the proper side from a subspace on the smooth-open side.', reason='The directional distinction matches the plan and worked argument; it is not an injection of all singular cohomology into a resolution.')
add(3006,[6],'self-flagged step',[(101,'53-99')], 'inj?',
 'For X=P²−{a,b}, T two lines meeting away from a,b, Y=T−{a,b}, U=P²−T, one has Hc¹(X)=Hc¹(Y)=Q and Hc¹(U)=Hc¹(normalization Y)=0. The proposed normalization injection is false.',
 'Hua supplied the earlier reconstruction; this run rederives localization with the exact incidence assumptions and preserves malformed diagram arrows.', reason='The counterexample tests the question as written; it does not silently repair its diagram.')
add(3007,[7,8,24],'unproved claim',[(104,'102-127'),(108,'282-286'),(114,'435-453')], 'semi-simplicité utilisée!',
 'Purity of a lisse sheaf over a finite field implies geometric semisimplicity on a normal base, not arithmetic semisimplicity. A two-dimensional unipotent Frobenius self-extension of Q_l has pure eigenvalue weight0 and is arithmetically nonsplit. Filtration devissage in Cor5.2 does not make every admissible extension strictly special.',
 'The distinction between geometric and arithmetic representations is modern terminology applied to the manuscript qualifications.', reason='The notes correctly detect the distinction; the extension is not a counterexample to geometric semisimplicity or the arithmetic semisimplicity conjecture for smooth proper cohomology.')
add(3008,[9],'conjecture',[(104,'125-127')], 'extension ... poids0 ... poids1',
 'For lisse pointwise pure sheaves F,G on a smooth finite-field variety, a nonzero Ext¹(F,G) requires wt(F)≥wt(G); a geometrically nonsplit extension requires strict inequality. The tentative opposite-order extension is incompatible with these hypotheses.',
 'The claimed direction is evaluated with extension0→G→E→F→0; different arithmetic base hypotheses are not covered.', reason='The sentence is tentative, not an asserted example; modern Ext weight restrictions decide the finite-field lisse reading.')
add(3009,[10],'unproved claim',[(104,'102-125'),(105,'134-180'),(106,'181-219'),(107,'224-251'),(108,'254-255')], 'poids entre0 et i',
 'Constant-coefficient cohomology has different compact, smooth ordinary, proper and singular bounds. For dimX=n, Hc^i has weights max(0,2(i−n))..i; smooth H^i has weights i..min(2i,2n). Hodge level bounds are numerical realization statements; the stronger geometric-generation bounds retain their motivic hypotheses.',
 'Modern statements use finite-field eigenvalue weights or complex mixed Hodge structures; the manuscript admits strong resolution and its motivic framework.', reason='The note correctly refuses to identify all support conventions; the top-two-piece wording on105 requires a separate alarm.')
add(3010,[11],'unproved claim',[(105,'152-166'),(106,'185-210')], 'dégénérescence E₂',
 'For the alternating normal-crossing boundary-strata sequence with E₂^{p,q} pure of weightq, all differentials dr for r≥2 vanish by incompatible weights. The earlier d1 need not vanish.',
 'Indexing is kept distinct from the local Leray sequence116–120, whose d2 can be nonzero.', reason='The original note is correct only with that spectral sequence and its purity input specified.')
add(3011,[12,23],'self-flagged step',[(105,'134-135'),(113,'418-424'),(127,'951-959')], 'résolution des singularités forte; fini plat radiciel',
 'The proof uses a resolution with relative normal crossings after generic reduction, base shrinking/stratification and possible inseparable extension. Invariance of the étale topos under a universal homeomorphism does not itself construct this model.',
 'de Jong alterations provide a different rational-coefficient method; they are not the same birational resolution hypothesis.', reason='The source states resolution as an input and flags the radicial step, so neither can be erased from the reconstructed proof.')
add(3012,[13],'self-flagged step',[(107,'224-232')], 'X non séparé; niveaux≤2n−i?',
 'For smooth nonseparated X, a Cech argument gives bounds depending on the cover; the sharper degree-dependent level bound is posed as a question. Compact support is not supplied by the then-used separated formalism.',
 'Deligne HodgeIII8.3.7 constructs nonseparated mixed Hodge structures but explicitly leaves the smooth weight inequality there unproved; this is not a modern universal solution of the manuscript level question.', reason='The note preserves both the question and the support-formalism limit.')
add(3013,[14],'unproved claim',[(108,'258-280'),(114,'430-447'),(122,'858-882')], 'Leray ... Deligne',
 'For a proper smooth projective morphism and a relative ample class satisfying hard Lefschetz, Rp_*Q_l splits in the derived category into its higher direct images, noncanonically in general. Composite Leray sequences degenerate and coefficient cohomology is a direct summand of total-space cohomology.',
 'Deligne1968 supplies the exact derived splitting criterion; hard Lefschetz and the existence of the motivic object are separate inputs.', reason='The notes correctly identify more than a numerical degeneration; the hypotheses must remain explicit.')
add(3014,[15],'reading question',[(109,'298-304')], 'poids≤2Inf(i,n)',
 'The paragraph announces coefficients of weightj but the displayed ordinary-cohomology bounds omitj. On a point with F=H¹(E), i=n=0,j=1, nonzero weight1 contradicts upper bound0.',
 'The point/elliptic test is an independent reconstruction; no missing term is inserted into the transcription.', reason='Both Pro and Codex preserve the omission and question mark; the literal formula is false.')
add(3015,[16,18],'self-flagged step',[(108,'282-284'),(113,'410-415')], 'borne inférieure ... j?',
 'For the Legendre family overF5 on P¹−{0,1,∞}, F=R¹π_*Q_l is strictly special weight1, yet Hc¹ contains two weight0 boundary invariant lines. Thus a lower boundw≥j fails; the printedw≥2(i−n)=0 is compatible.',
 'This run verifies the exact family, split multiplicative reduction at0,1, no global invariants, and the localization injection. It is not a lower-bound assertion for ordinary cohomology.', reason='The earlier notes correctly distinguish supports and supply a genuine all-hypotheses example.')
add(3016,[17,19],'self-flagged step',[(108,'279-280'),(120,'800-805')], '2n+j?; 2i+j?; 2Inf(i,n)+j?',
 'For the same strictly special elliptic coefficient system, local H¹(I,F)=Q_l(−2) at split multiplicative boundary points. Global H¹(U,F) surjects onto Q_l(−2)². Both proposed global bounds and the local bound give3 for i=n=j=1, while weight4 occurs.',
 'The local Tate calculation and global Leray edge map are rederived here. This disproves the questioned sharpenings, not the constant-coefficient local bound.', reason='The old notes are right on the counterexample, with geometric/arithmetic Frobenius conventions kept fixed.')
add(3017,[20,91],'reading question',[(112,'370-382'),(113,'402-404')], '2n−Φ={n−i}; check F(−n)',
 'Dualizing weighti and twisting by−n gives weight2n−i. The displayed set-builder loses a factor2; the negative twist on113 is necessary for the displayed weightν+2h.',
 'Test Q_l withn=1 gives Q_l(−1), weight2. This is a mathematical alarm, not an ink decision.', reason='H01 duplicates these sign/index issues and is merged; the Codex alternatives do not settle the ink.')
add(3018,[21],'self-flagged step',[(111,'350-356'),(112,'386-390')], "il n'est pas tautologique; plus fort que la conjonction",
 'Existence of separate geometric filtrations with weights inΦ andΦ′ need not formally give one with weights in their intersection; separate weight and geometric-level witnesses need not give a joint witness. Canonical realization weight filtrations address only the numerical part.',
 'No general equivalence between geometric generation and Hodge bounds is inferred.', reason='The exact logical warning is on both pages and is stronger than a request for numerical weight bookkeeping.')
add(3019,[22],'withdrawn in the same text',[(108,'258-263'),(113,'406-424'),(114,'451-453')], 'par dévissage (possible ici?); strictement spécial',
 'The broad coefficient hypothesis is replaced by F a direct summand of R^jg_*Q_l for g projective smooth. Cor5.2 attempts recovery for filtered special subquotients under the semisimplicity part of Tate.',
 'Subquotients cannot be passed through a derived cohomological functor as if direct summands; a filtration devissage needs long exact sequences.', reason='The deletion, replacement and conditional recovery are all preserved rather than flattened into one theorem.')
add(3020,[25],'reading question',[(114,'457'),(129,'987-989'),(131,'999-1019')], 'sans conj. type Tate [Pro] / sous conj. type Tate [Codex]',
 'Cor5.3 asserts preservation of effective admissibility by R^if_!, but the two independent transcriptions disagree whether the assertion is without or under Tate-type conjectures. The later proof attempt expressly reaches a complete-reducibility obstruction.',
 'Current correction to the earlier note: unconditional authorship is unresolved; both variants and their mathematical obligations are recorded.', 'overstates', 'W20 treats the Pro sans reading as certain. Codex K12-07 line427 reads sous; the scan must decide.')
add(3021,[26],'reading question',[(115,'461-467')], 'niveaux≤2(n−i+j)',
 'The literal formula fails for a proper smooth elliptic curve withn=i=1,j=0, whose H¹ has level1. The earlier2n−i+j expression gives1.',
 'The correct-looking expression is a proposed alternative for the scan reader, not a diplomatic correction.', reason='The old note accurately identifies the counterexample and compares the earlier formula.')
add(3022,[27,28,29],'unproved claim',[(116,'502-540'),(118,'574-693'),(120,'784-795')], 'niveaux≤Inf(i,n−1)',
 'For a positive-dimensional regular-source immersion with closure dimensionn and a proper normal-crossing resolution isomorphic over the source, the local Leray Hodge terms give level≤min(i,2n−1−i), hence≤min(i,n−1), and weights≤2min(i,n). The identity of a point falsifies the unqualified n=0 formula.',
 'The Hodge inequality is rederived from proper-fibre dimensions. Its identification with the manuscript geometric-level class is left conditional, not proved by Hodge numbers.', reason='The three notes merge into one claim with an explicit positive-dimension hypothesis and realization boundary.')
add(3023,[30],'reading question',[(120,'771-780')], "poids2n s'identifie avec [Pro] / intervient avec [Codex]",
 'An E₂ top-weight contribution need not survive. Blow up the origin ofA² and then a point of the exceptional divisor: E₂^{0,2}=Q_l(−2), but R²j_*Q_l at the origin is0, so a nonzero d2 kills it.',
 'Only the strong Pro identification is refuted. Codex K12-08 line214 does not assert equality with the abutment.', 'overstates', 'W25 correctly calculates the example but attributes the stronger wording without noting the independent intervient variant.')
add(3024,[31],'self-flagged step',[(120,'821-837')], 'peut on remplacer par n−1 ... ?',
 'For j:G_m→A¹, nonempty fibres have dimension0 but the boundary R¹j_*Q_l=Q_l(−1) has weight2. Actual fibre dimension cannot replace the local closure/ambient parameter in the weight bound without qualification.',
 'The example tests a naive interpretation; the marginal wording does not fix which proposed bound is being replaced.', reason='The note appropriately limits its refutation to the naive substitution.')
add(3025,[32],'unpursued implication',[(112,'386-390'),(125,'897-918')], "G′(−k); fibres ... dim≤d",
 'Hodge level, coniveau, Tate-stable geometric level on112 and the source-dimension type on125 are distinct. The late type is not the Tate-stable early D_i convention at12/035–036.',
 'The present run explicitly localizes the earlier note distinction to the changing definitions; no blanket contradiction with the early packet.', reason='The late definition controls source dimension; the early definition must be crosslinked as a separate convention.')
add(3026,[33,34],'reading question',[(133,'1039-1052'),(137,'1148-1155')], 'd+d′−1; en tensorisant par Q_l(−1)',
 'With late type defined by smooth projective sources of dimension≤d, R^dj_*Q_l for j:G_m^d→A^d has origin stalkQ_l(−d), weight2d, so cannot have type≤d−1. A Tate twist can raise this type by1.',
 'The counterexample uses a finite-field base to retain Frobenius; it does not refute the Tate-stable early type definition or Hodge-level bounds.', reason='The notes are retained with the local-definition qualifier supplied by comparison with early cote12.')
add(3027,[35,36,92],'self-flagged step',[(135,'1100-1119'),(137,'1120-1169')], 'à vérifier / développer; qui sont traités / qu’on sait traiter',
 'The reduction to coefficient dimension1 is explicitly left to check/develop. For a proper curve family the Leray rowsq=0,1,2 leave three filtration subquotients; the middle row hasE3=E∞, but the outer rows may be smaller subquotients ofE₂.',
 'Hua’s reported reste à traiter is not an independent attached witness. Both attached versions express that the remaining pieces are known/treated, not that the whole proof is complete.', reason='The notes correctly keep three layers and an unresolved reduction; numbering and last-word alternatives remain scan questions.')
add(3028,[37],'unproved claim',[(125,'913-918')], 'il suffit ... les fibres géométriques',
 'A bare geometric stalk is only a vector space and cannot certify arithmetic geometric origin or Frobenius weight. A fibrewise type criterion must retain arithmetic descent data or a relative presentation.',
 'Q_l andQ_l(−1) at a geometric point have the same underlying one-dimensional vector space but differ over a finite field.', reason='The earlier note rightly warns against taking the geometric-fibre slogan literally after forgetting all descent.')
add(3029,[38,103],'idea of the earlier run',[(116,'502-540'),(120,'784-795')], 'No Durfee or Saito theorem is stated on these leaves.',
 'For an isolated boundary point of a complex n-fold with smooth punctured neighborhood, link cohomology has weights≤i fori<n and>i fori≥n. This is the isolated-point specialization of Durfee–Saito semipurity, not the general immersion-level theorem.',
 'Durfee1983 metadata and local construction are a literature lead; where full text is not obtained no numbered theorem is certified.', reason='The note’s restricted comparison is sound and the separate bibliographic limitation merges into the same evidence unit.')
add(3030,[39,40],'idea of the earlier run',[(142,'1295-1312')], 'pleinement fidèle',
 'Tate–Faltings Hom for abelian varieties and anabelian Hom for hyperbolic curves have distinct hypotheses and targets. Multiplication by2 on a Jacobian generally does not come from a curve self-map of a smooth projective curve of genus≥2.',
 'The nonlinear comparison belongs to earlier project context. Riemann–Hurwitz forces a nonconstant self-map in genus≥2 to degree1, whereas[2] is not a polarization-preserving automorphism.', 'not on the page','Only the weight-one motivic full-faithfulness claim is written here; the anabelian pair is a prior-run comparison.')
add(3031,[41],'idea of the earlier run',[(140,'1182-1187'),(149,'1610-1625')], 'isomotif semi-simple',
 'Semisimplicity in a characteristic-zero neutral Tannakian category corresponds to pro-reductivity; it does not imply a trivial centre. The Tate category has groupG_m.',
 'A centre-free geometric fundamental-group comparison remains an external anabelian lead.', 'not on the page','The logical distinction is valid, but no centre-free group claim occurs in this manuscript unit.')
add(3032,[42],'idea of the earlier run',[(141,'1277-1291')], 'No real-section statement on these leaves.',
 'A polarization ofH¹ is not a section of the arithmetic fundamental-group extension overR. For a smooth projective geometrically connected real curve of genus≥1, the real section theorem recovers connected components ofX(R), not individual real points.',
 'The comparison is credited to the earlier run; Stix2008 Theorem26 is checked only with its exact hypotheses.', 'not on the page','The attached manuscript gives a weight-one group-scheme functor, not a real-section theorem.')
add(3033,[43,44,45],'idea of the earlier run',[(115,'461-469'),(141,'1252-1255')], 'le poids',
 'At a good finite place, weight separates a toric cyclotomic realization from an abelian weight-one realization. Vanishing of that linear map does not classify subgroups invisible in all tested abelian quotients, nor solve a prime-to-p point-detection problem.',
 'LM6 A.22/A.50, LM7 and FLAGGED_149 B9 remain unverified internal project leads; no status is upgraded.', 'not on the page','The weight calculation is relevant background, while the nonlinear claims are absent from the source.')
add(3034,[46],'conjecture',[(140,'1182-1187')], 'deux nb premiers l distincts',
 'For a semisimple rational motive overK, smoothness over normal integralS is defined by unramified realizations on everyS[1/l]. The manuscript conjectures one eligible prime can suffice when invertible everywhere, or two distinct primes suffice in general.',
 'The one-prime assertion is proved forH¹ of abelian varieties over traits by NOS; no general arbitrary-motive/base theorem is inferred from compatible Frobenius polynomials.', reason='The quantifiers and residue-characteristic exclusions are essential and are retained.')
add(3035,[47,48],'unproved claim',[(140,'1189-1206'),(140,'1228-1230')], 'provient d’un isomorphisme sur Z_l; Hom ... type fini',
 'The almost-all-prime integral condition needs a common reference lattice system. Without it, standard source lattices and targetl⁻¹Z_l at every prime give a Hom subgroup ofQ containing1/l for every prime, hence not finitely generated.',
 'This is a counterexample to the weakened interpretation, not to a correctly specified almost-all-prime reference axiom.', reason='The notes correctly identify the missing definition and delimit their lattice example.')
add(3036,[49],'unproved claim',[(140,'1228-1234')], 'est pleinement fidèle',
 'For connected normalS, G_K surjects ontoπ₁(S), so maps between unramified realization systems are detected generically. Given the assumed rational abelian motive category and exact realizations, kernels and cokernels are componentwise.',
 'The proof is formal conditional on the category and reference lattices; it is not a construction of that rational motivic category.', reason='The full-faithful/full-abelian claim is weaker than extension closure and is supported by the displayed data.')
add(3037,[50],'unproved claim',[(140,'1234-1237'),(141,'1242-1245')], 'ss-catégorie abélienne épaisse',
 'If épaisse means closed under all extensions inside the generic integral category, it is false: a nontrivial unipotentF_l² representation of tameC_l inertia extends two constantF_l objects but is ramified.',
 'UseS=SpecC[[t]], K=C((t)), the covert^(1/l), rational part0 and finite l-primary realization. The endpoints are smooth integral torsion motifs; the middle object is only generic. The weaker subquotient-closed assertion survives.', reason='The exact interpretation being refuted is explicit; historical usage of épaisse requires an ink/context check.')
add(3038,[51],'unproved claim',[(140,'1237'),(141,'1242-1245')], 'la catégorie quotient est équivalente',
 'Finite torsion realization systems form the kernel of rationalization. The asserted Serre quotient equivalence follows once exactness, essential surjectivity and clearing denominators of rational morphisms hold with a fixed reference system.',
 'A conditional categorical proof is supplied; extension closure in the larger generic category is irrelevant to the internal Serre quotient.', reason='The note accurately separates the quotient from the failed ambient thickness assertion.')
add(3039,[52],'unpursued implication',[(141,'1247-1250')], 'une ⊗-catégorie avec Hom',
 'Componentwise integral tensor product and internal Hom exist in the intended lattice model. Nonzero finite torsion objects are not dualizable:Hom_Z(Z/l,Z)=0, so this is not a rigid neutral Tannakian category.',
 'The nonrigidity inference is ours/earlier run; the manuscript claims tensor withHom, not rigidity.', reason='The note is a valid guard against adding an unwritten Tannakian assertion.')
add(3040,[53],'unproved claim',[(141,'1257-1259')], 'Tout schéma propre et lisse X sur S définit des motifs',
 'Every proper smoothS-scheme is asserted to yield integral cohomological objects, and analogous relative étale-site objects. Proper smooth base change gives the unramified l-adic systems; rational motive existence and the common integral structure remain assumptions.',
 'Hua’s reported projective-only paraphrase is narrower than both attached source versions.', reason='The earlier note correctly preserves proper rather than silently narrowing the source to projective.')
add(3041,[54],'reading question',[(141,'1261-1285')], 'E_l=Hom(...,Q_l/Z_l); extension ... parR¹',
 'For0→A⁰→A→F→0, dualizing the l-primary torsion sequence gives0→Hom(F(l),Q_l/Z_l)→E_l→H¹(A⁰,Z_l)→0. The finite component contribution is the kernel.',
 'The margin’s verbal extension order reverses ordinary French convention; the displayed construction may be correct and only the prose loose.', reason='The note’s algebra is correct; neither this run nor Hua may reverse the displayed definition silently.')
add(3042,[55],'unproved claim',[(142,'1295-1296')], 'On se ramène ... SpecK',
 'The contravariant weight-one functor is asserted fully faithful. Generic rational h¹ morphisms, simultaneous integral lattice conditions, finite components and extension of an already-existing generic homomorphism toS are distinct ingredients.',
 'For abelian schemes the normal-base extension theorem is checked in Faltings1986§2Lemma1; this does not prove essential surjectivity or reconstruct all disconnected group extensions from the one sentence.', reason='The note correctly distinguishes full faithfulness from the separate object-extension question.')
add(3043,[56,57,58,59,60,63],'withdrawn in the same text',[(140,'1185-1187'),(142,'1298-1317')], 'Il faut; La question si ... suffisante; peut-être pas ... dim2',
 'Weight-one effectivity and all-prime nonramification are necessary; sufficiency is explicitly questioned after emphatic words are deleted. Mixed-characteristic regular-local dimension2 counterexamples exist and satisfy all the stated nonramification conditions. Ifp∉m^p, abelian schemes on the punctured spectrum do extend.',
 'The exact all-prime comparison uses finite-étale purity for l≠p andS[1/p]⊂U for l=p. The quoted high-ramification example is classical Raynaud–Gabber, subsequently proved in Vasiu–Zink; no first-date2010 claim. Prime index/order reduction remains separately unresolved.', 'understates','The prior note is mathematically sound on nonextension but needs earlier-history attribution and the prime-index/order variant.')
add(3044,[62],'reading question',[(142,'1309-1317')], 'critique|néronique [Pro] / mézigues [Codex]',
 'The unnamed characteristic-zero criterion and the prime index/order wording cannot be securely identified from the two transcriptions. The mathematical extension issue is retained independently.',
 'No author or theorem is supplied by guessing the name; the scans must decide.', reason='The earlier note rightly withholds attribution, and Codex adds a materially different reading.')
add(3045,[64,65,73,74],'self-flagged step',[(144,'1346-1382'),(146,'1451-1472')], 'au grain de sel; équivalence',
 'For an additive categoryC, its idempotent completionKar(C) is universal by equivalence of categories of additive functors to an idempotent-complete additive target. Finite biproducts matter. The source weighs equivalence rather than a literal bijection of functor objects and has an unresolved variance/deletion.',
 'The coherent2-categorical formulation is the present reconstruction of the written universal property; semisimplicity is not needed to split projectors.', reason='The notes correctly preserve the weakened/equivalence reading and the additivity hypothesis.')
add(3046,[66],'unpursued implication',[(145,'1391-1400')], 'End(X) ... dimension finie',
 'In an additiveF-linear category, Hom(X,Y) is a matrix corner ofEnd(X⊕Y). Thus finite-dimensional End for every object already implies finite-dimensional Hom; the deleted extra condition is redundant.',
 'Without finite biproducts this argument is unavailable; individual End rings alone do not control all Hom spaces.', reason='The note’s redundancy argument exactly uses the source’s intended additive setting.')
add(3047,[67,68],'unproved claim',[(145,'1403-1409'),(146,'1427-1472')], 'Hom((X,p),(X′,p′)); ImH(p)',
 'Intertwiners satisfyingap=p′a modulo maps withap=p′a=0 identify canonically withp′Hom(X,X′)p. Objects(X,p), identitiesp, and composition form the idempotent completion; every projector splits before any semisimplicity hypothesis.',
 'The standard corner formulation is equivalent to the manuscript quotient, not an alternative definition that ignores the quotient.', reason='The earlier notes correctly separate the universal splitting construction from the subsequent abelianness proof.')
add(3048,[69],'unproved claim',[(147,'1478-1538')], 'uvu=u; vuv=v',
 'In a finite-dimensional semisimple endomorphism algebra, a rectangular morphismu has a reflexive generalized inversev. Thenvu anduv are projectors and their complementary images give kernel/cokernel; the proof can be written without assuming the category already abelian.',
 'The circular-sounding word in the manuscript is avoided by working in matrix corners before naming kernels. Exact rational-matrix checks supplement the general algebra proof.', reason='The note accurately reconstructs the intended semisimple-ring argument.')
add(3049,[70,71],'reading question',[(148,'1565-1583')], 'Tout morphisme; v=inj₂ u pr₂',
 'A general map splits asA⊕B→B⊕C with an isomorphismu onB. Its reverse uses the projection onto the first summandB ofB⊕C; the displayedpr₂ is ill-typed with the written ordering.',
 'The alternative ispr₁. Hua’s reported restriction to monomorphisms is not the source reading; both attached versions say every morphism.', reason='The two notes concern one normal-form argument and merge without changing the source.')
add(3050,[72],'unproved claim',[(147,'1539-1549')], 'noethérien et artinien',
 'An idempotent-complete additiveF-linear category with everyEnd finite-dimensional semisimple is semisimple abelian; each object decomposes into finitely many simple summands and has finite ascending and descending chains of subobjects.',
 'Finite-dimensionality limits orthogonal nonzero idempotents. Chain conditions follow after constructing subobjects, not merely from an unexplained abelian assumption.', reason='The note correctly identifies the algebraic finiteness argument.')
add(3051,[75],'unproved claim',[(149,'1598-1616')], 'bifoncteur biadditif; associativité; commutativité',
 'A biadditive functor extends to idempotent completions by applying it to projectors. A symmetric monoidal structure extends with inherited associativity, symmetry and unit constraints, and the inclusion is symmetric monoidal.',
 'This is a formal extension theorem; it does not construct duals or a fibre functor.', reason='The note keeps the genuine monoidal conclusion separate from the unwritten Tannakian one.')
add(3052,[76],'unproved claim',[(149,'1616-1625')], 'caractéristique0; puissances extérieures; symétriques',
 'In aQ-linear idempotent-complete symmetric monoidal category, the symmetric and alternating averaging idempotents inQ[S_r] split, giving symmetric/exterior powers and Schur summands. Over general coefficients the necessary denominators may fail.',
 'The exact r=3 projector calculation is a certificate; the general proof is group-algebra averaging.', reason='The note correctly retains characteristic0 and does not assert identical integral behavior.')
add(3053,[77],'idea of the earlier run',[(145,'1391-1409'),(147,'1478-1549')], 'No explicit cote16 reference on these leaves.',
 'The earlier run links the abstract completion to correspondence rings in cote16/018,049. Those endpoints are not attached in this part, so the link remains a retrieval lead.',
 'Hua’s geometric example after149 is outside the supplied source, not a continuation we have read.', 'not on the page','Only the source side of the proposed archive link is available.')
add(3054,[78],'idea of the earlier run',[(145,'1391-1409'),(146,'1466-1468')], 'abélienne semi-simple',
 'Jannsen1992 proves semisimplicity of numerical pure motives, and Lemma2 supplies the abstract End-ring criterion. It does not prove semisimplicity of homological motives without equality of numerical and homological equivalence.',
 'The modern theorem supplies a conditional geometric application of the manuscript formal architecture, not all standard conjectures.', reason='The note’s precise limitation matches the opened theorem.')
add(3055,[79,88],'idea of the earlier run',[(149,'1610-1625')], '⊗-catégorie',
 'TheP¹ Lefschetzsl₂ raises/lowers cohomological degree and moves the unit summand, whereas a central motivic weight cocharacter and tensor automorphisms preserve it. A symmetric monoidal idempotent completion is not yet a rigid neutral Tannakian category.',
 'TheP¹ matrices are rechecked; this is a negative comparison with earlier project context, not a manuscript inclusion theorem.', 'not on the page','No identification of Lefschetzsl₂ with the motivic Galois group appears in these leaves.')
add(3056,[80],'idea of the earlier run',[(99,'36-46'),(145,'1391-1400')], 'Conjectures standard',
 'The prior A–D lettering table is a cross-package research lead. Operational matches require the defining draft on one side and printed definitions on the other; unprovided cote14/117 cannot certify the remaining identifications.',
 'Root-owned earlier cote11/12 statements are the available manuscript witnesses. This late item supplies only its reference/programme context.', 'not on the page','The letter dictionary is not written on this selection and is not independently completed by the note.')
add(3057,[81],'idea of the earlier run',[(107,'235-251'),(116,'502-540')], 'No cote14 citation on these leaves.',
 'A proposed link between cote16/047 singular-hypersurface work and cote14 remains external because neither target passage is attached here. General singular-cohomology themes alone do not prove the claimed resumption.',
 'The lead is retained for retrieval only.', 'not on the page','The prior note properly withholds a primary-witness verdict on the missing endpoint.')
add(3058,[82,83],'idea of the earlier run',[(149,'1610-1625')], 'No motivic Galois exact sequence on these leaves.',
 'With neutral compatibleQ-valued fibre functors and effective finite Galois descent, the rational Nori sequence1→G(Qbar)→G(Q)→Gal(Qbar/Q)→1 is exact. Its Artin quotient is not automatically the component quotient; splitting and geometric-kernel connectedness are additional assertions.',
 'Kahn2025§5.8,Thm5.10,Thm10.2 are a later comparison, not Grothendieck’s statement here. The initial2023 circulation date and2025 revision/publication are distinct.', 'not on the page','The note correctly separates exactness from connectedness; its exact theorem is verified using the author arXiv final version.')
add(3059,[84,85],'idea of the earlier run',[(99,'7-46'),(149,'1598-1625')], 'No period-conjecture statement on these leaves.',
 'The modern period conjecture says that the complex comparison point ofIsom⊗(ωdR,ωB) is Zariski generic overQ. The reported18/059 transcendence conjecture is only an unavailable archive lead.',
 'André2010§1.4 states the modern comparison; the existence of a tensor category is not evidence for its truth.', 'not on the page','No source quotation is manufactured for the missing period statement.')
add(3060,[86],'idea of the earlier run',[(145,'1391-1409'),(149,'1610-1625')], 'abélienne semi-simple',
 'Arapura’s pure Nori/André comparison applies with rational coefficients over a subfield ofC and smooth bases. Motivated correspondences need not be known algebraic; the comparison does not settle standard conjectures.',
 'The exact later theorem is separate from the manuscript’s algebraic-correspondence programme.', reason='The prior note’s scope matches Theorem6.4.1, with the base/realization hypotheses explicit.')
add(3061,[87],'idea of the earlier run',[(149,'1610-1625')], 'No Nori–Ayoub comparison on these leaves.',
 'Choudhury–Gallauer2017Thm9.1 compares Nori and Ayoub Hopf algebras by inverse maps for a field embedded inC and coefficientPIDΛ. TheQ case gives the stated motivic Galois group isomorphism, without semisimplifying all mixed motives or proving cycle conjectures.',
 'The theorem is a later comparison first circulated2014; this run retains the strongerPID formulation only as an accurately sourced addition.', 'not on the page','The external comparison is real but not attributable to the manuscript.')
add(3062,[89,90],'idea of the earlier run',[(140,'1189-1206'),(141,'1257-1259'),(141,'1277-1285')], 'si carK=0; Tout schéma propre et lisse',
 'Oda1969Cor5.11 identifies the Dieudonné module of thep-kernel of an abelian variety over a perfect field withH¹dR, respecting the Hodge filtration. Cor5.12 gives an injection for a general proper smoothX withX(k)≠∅, not a universal isomorphism.',
 'The rational-point hypothesis, absent from the earlier ODA2 wording, is restored. Cote54/005–007 is unavailable and remains an external link; no characteristic-p extension of the manuscript definition is claimed.', 'understates','The comparison is valid but the exact general-case theorem assumes a rational point, explicitly on printedp131.')
add(3063,[93],'reading question',[(140,'1179-1187'),(141,'1261-1291'),(142,'1295-1296')], 'isomotif semi-simple surS; E_l; u_l',
 'The rational object is defined generically overK while the first line may say surS; symbols for its integral realization functor and restriction map vary. These affect type checking, not merely typography.',
 'Keep both transcriptions and assign no new base category by conjectural normalization.', reason='The earlier note’s symbol/base alarms are retained as scan questions.')
add(3064,[94,95],'self-flagged step',[(104,'127'),(108,'258-286'),(113,'418-424'),(120,'800-837'),(122,'886-890'),(135,'1117-1119'),(142,'1305-1327'),(144,'1375-1382')], 'possible ici?; à expliciter; à vérifier',
 'The two summary entries index explicit questions and admitted inputs already represented in the substantive items and problems. They do not introduce independent mathematical claims.',
 'Current consolidation maps every distinct self-flag to its own problem and records any additional claim directly from the source.', reason='These index rows merge into the substantive coverage register, rather than duplicate every question as another item.')
add(3065,[98,99],'title, date or page count',[(119,'694-756')], '20.3.68;1.Korrektur;Local Cohomology',
 'The reused printed cover concerns Hartshorne’s notes of Grothendieck’s local-cohomology seminar, Lecture Notes in Mathematics41, printed1967, with a proof mark20March1968. It is not a manuscript date for the surrounding weight sheets.',
 'Unretained faces121/123 mentioned by the earlier return are not inspected; no content is reconstructed from their mention.', reason='The note accurately separates printed bibliography, proof mark and surrounding manuscript chronology.')
add(3066,[],'reading question',[(111,'318-322')], 'si i=0 ... équivaut à:F localement constant',
 'Under the displayedQ_l-subquotient definition, specialweight0 means finite monodromy, not arbitrary lisse monodromy. An infinite unipotent Frobenius self-extension onSpecFq is lisse but not a subquotient ofR⁰ of a smooth projective map.',
 'This source claim was not isolated by the indexed notes. CodexK12-07L301 has a deleted warning about the converse; its separate rational-descent objection does not preventQ_l-representations of a finite group being subquotients of its regular representation.', 'overstates','The source’s surviving iff needs a restricted locally-constant convention or a correction; no scan decision is made.')

def save_items():
    (BASE/'items.json').write_text(json.dumps(items,indent=2,ensure_ascii=False)+'\n')
save_items()
