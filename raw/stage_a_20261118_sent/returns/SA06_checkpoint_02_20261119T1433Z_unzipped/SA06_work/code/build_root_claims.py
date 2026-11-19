#!/usr/bin/env python3
"""Claim ledger authored after source reading, proofs, computations and research.

No status/fate is inferred by a classifier. Mechanical reuse of already checked
locators avoids introducing a second, inconsistent source-coordinate system.
"""
from pathlib import Path
import json,csv
W=Path(__file__).resolve().parents[1];P=W/'parts/root';I={r['id']:r for r in json.loads((P/'items.json').read_text())}
C=[];E=[];S=[]
WHO='GPT-6 Astra Pro; effort not exposed; SA06-part2/root'
def claim(n,items,statement,status,klass,fate,refs,search,comp=None,confidence='high',words=None,where=None,proof=None):
 ids=[f'SA06-{i}' for i in items];src=[I[i] for i in ids];sid=f'C-SA06-{n}'
 loc=where or {'cote':'15','scans':sorted({p for a in src for p in a['scans']}),'lines':[a['lines'] for a in src]}
 C.append(dict(id=sid,items=ids,**loc,his_statement=words if words is not None else ' | '.join(a['his_words'] for a in src),statement=statement,status_on_pages=status,
  computation={'certificate':'code/root_computations.py','output':'parts/root/root_computations_output.json','sections':comp} if comp else {'kind':'conceptual argument; no numerical computation on which this claim rests','proof':proof or 'See source comparison and explicit argument in fate; no claim of machine proof.'},
  **{'class':klass},fate=fate+' Search: '+search+'.',fate_date={'assessment':'2026-11-19','first_circulation_and_publication':'See the separate, source-verified dates for each cited work in SA06_references.bib and REFERENCE_AUDIT.json; unknown circulation dates are not inferred from publication.'},present_status='As of November2026: '+fate,refs=refs,confidence=confidence))
 E.append(dict(statement_id=sid,date='2026-11-19',who=WHO,type='used and rechecked in this run',outcome='Read the cited transcription passage and checked the exact scope against '+', '.join(refs)+'. '+fate))
 if comp:E.append(dict(statement_id=sid,date='2026-11-19',who=WHO,type='computation or formal certificate',outcome='Exact checks in root_computations.py, sections '+', '.join(comp)+'. Scope and hypotheses are recorded in the output; finite checks are not labelled universal proofs.'))
 if proof:E.append(dict(statement_id=sid,date='2026-11-19',who=WHO,type='independent re-proof',outcome=proof))
 if status.startswith('false'):E.append(dict(statement_id=sid,date='2026-11-19',who=WHO,type='refuted, with refined statement '+ids[0],outcome=fate+' The refined modern statement and scope are in '+ids[0]+'. No ink is changed.'))
 S.append(dict(statement_id=sid,search_ids=search,refs='; '.join(refs),result=fate))

brand='root_search_002/003/006/007/008/009; targeted Brandt/norm/Deuring queries in web, zbMATH-indexed search, arXiv and MathOverflow; backward references in Voight and Deuring; SGA4XVIII original'
torus='root_search_004/005/006/007/010/011/012/013; positive-involution, Serre-group and rational-density sources; author bibliographies and cited predecessors'
analytic='root_search_006/009; BourbakiVarietes1967_1971 independently opened/read by cote15_middle; backward source comparison and exact algebraic checks'
fibre='root_search_001/002/003/004/005/009/010/011/014; Oda, Lang, GrothdeRham, Deligne–Milne, Milne gerbes, Stacks; zbMATH direct query failed and its indexed search yielded no additional exact result'

claim(700,[706],
 'For a degree-n central algebra/order category equipped with the proposed norm line, scalar λ acts on the norm by λ^n; after trivializing that line its scalar automorphisms are μ_n.',
 'stated without proof','B',
 'The scalar-band calculation is established by the determinant/norm character and the fppf Kummer sequence. It does not prove that the entire manuscript category is a locally nonempty μ_n-gerbe on an unspecified site.',
 ['StacksKummer','Voight2021'],brand,proof='A scalar λ on a rank-n object has determinant λ^n. Norm-preserving scalars are exactly the kernel of the n-th-power map G_m→G_m, namely μ_n. No choice of topology removes the need for local existence of objects.')
claim(701,[706,708,709],
 'The norm-rigidified Deuring categories and their equivalence categories admit the proposed μ_n-gerbe description, with a canonical identification of two Picard actions and a coherent lift of ordinary equivalences.',
 'open on the pages','C',
 'Gerbes, Picard stacks and normed invertible-bimodule models provide established formalism, but the exact integral comparison and its action/coherence data were not located as a published theorem matching these pages. The page itself assumes a canonical norm object and marks the action comparison unchecked; no novelty is inferred from this bounded search.',
 ['SGA4XVIII1973','Voight2021','MilneGerbes2003'],brand,confidence='medium')
claim(702,[707],
 'The displayed right-exact norm-rigidified sequence ending in Ram is valid when the obstruction Ram→Pic(A)/n vanishes; in general the last zero must be replaced by that obstruction group/map.',
 'stated without proof; displayed right endpoint requires a norm-line obstruction to vanish','C',
 'The general omitted obstruction is the norm-line class modulo n-th powers. In the later principal bases Z, Z[1/p] and Z_p it vanishes, so this is a necessary qualification rather than a counterexample to those special cases. Standard Kummer and invertible-ideal descriptions supply the refined sequence.',
 ['StacksKummer','Voight2021'],brand,proof='Changing a representative by an invertible central lineL changes its norm by L^n. Thus the norm class modulo nPic(A) is well-defined on the ramification quotient; a trivialized-norm representative exists exactly when this class vanishes. The kernel is the Kummer group of normed lines. This proves the obstruction formulation, without asserting an explicit nonzero obstruction for every order.')
claim(703,[710,711],
 'For the ramified quaternion maximal order over Z_p, m²=pO and Nrd(m)=pZ_p; the norm-trivialized class(m,p) has order2 and splits the local extension by unit square classes.',
 'proof sketched','E',
 'The ideal/norm identities are classical quaternion-order facts; the split normed class follows directly from them. The nontrivial real quaternionic Brauer class remains a different datum.',
 ['Deuring1941','Voight2021'],brand,proof='The local radical is generated by a uniformizer of valuation1/2, hence m²=pO and its reduced norm generates pZ_p. Squaring(m,p) yields(pO,p²), which is norm-trivialized by multiplication by the central scalarp because Nrd(p)=p². Its image in the ramification Z/2 is nonzero, so its order is exactly2.')
claim(704,[712],
 'The unit-square-class factor has size2 at oddp and4 atp=2; the split local normed Brandt group therefore has size4 or8 respectively.',
 'stated without proof through the displayed group formula','E',
 'The p-adic square criterion verifies the sizes; μ2-Kummer is fppf in the dyadic case. Odd-prime étale reasoning cannot simply be copied at2.',
 ['StacksKummer','StacksHenselian','Voight2021'],brand,comp=['unit_square_classes'],proof='For oddp a unit is a square precisely when its residue in F_p* is a square, by simple-root Hensel lifting. For2, every odd square is1mod8; successive lifting shows every1mod8 unit is a square. Hence Z_2*/Z_2*² is represented by1,3,5,7. Multiply by the split ramification factor of order2.')
claim(705,[713],
 'The displayed quotient Γ′/⟨(p,(0,1),p)⟩ is represented uniquely by the zero ramification coordinate, with formula(u,v,e,w)↦(u p^(−e),v,w).',
 'proof sketched','B',
 'This is a valid elementary quotient calculation under the displayed product/splitting. It removes one class coordinate, not the remaining equivalence-groupoid automorphisms; the written ring is an integral product with a real factor.',
 ['Voight2021','StacksKummer'],brand,proof='Every element has ramification coordinatee∈Z/2. Multiplication by the distinguished generator to powere kills it and changes the away coordinate byp^e. The real sign ofp is positive. The generator has order2 modulo unit squares, so the construction is independent of the representative ofe and has an evident inverse from the zero-coordinate subgroup.')
claim(706,[714],
 'Frobenius acts trivially on the quotient of rigidified comparison classes, as calculated from the specified translation.',
 'proof sketched','C',
 'The quotient-level calculation is valid. No source found in the targeted search identifies it with a completed coherent descent theorem for exactly these integral categories; the gerbe action still needs its2-isomorphisms and cocycle.',
 ['SGA4XVIII1973','MilneGerbes2003'],brand,proof='The induced Frobenius translation is the generator killed in the quotient of C-SA06-705, so it is identity on the quotient set of classes. This proves only the π0 statement.')
claim(707,[715],
 'The written formula F_{p^n}=F_p[T]/Φ_{p^n−1}(T) is false for generalp,n; it becomes a finite field after choosing a suitable irreducible factor, with compatible embeddings still additional data.',
 'false as stated','C',
 'Atp=2,n=3 the quotient is F8×F8, with all stated arithmetic hypotheses satisfied. The corrected factor construction is standard finite-field theory. No alleged canonical system follows from the wrong quotient.',
 ['Lang1956','Deuring1941'],brand,comp=['cyclotomic_F2_n3'])
claim(708,[716,717],
 'After passing to the relevant connected2-category, equivalence classes and1-morphism classes are unique but the remaining2-automorphism group isZ/2; a canonical torsor does not itself supply a point.',
 'corrected by himself later: scan46 cancellation and scan48 π2/sign statement; scan48 canonical point deleted','B',
 'The residual-automorphism and torsor distinctions are valid in modern gerbe theory. Milne’s later gerbe uniqueness theorems likewise state their residual automorphisms explicitly, but do not identify the exact integral Deuring datum here.',
 ['SGA4XVIII1973','MilneGerbes2003'],brand)
claim(709,[718,719,710],
 'Neutrality of a comparison gerbe does not imply neutrality of either real endpoint; scalar signs, sign torsors and a quaternionic Brauer class are distinct degrees of data.',
 'stated without proof','B',
 'Established by the torsor/gerbe distinction and the real quaternionic Brauer class. The manuscript’s two neutrality statements do not contradict each other.',
 ['DeligneMilne1982','Deuring1941','GrothBrauerII1966'],brand,proof='If two banded gerbes are equivalent, their equivalence category can have an object even if neither gerbe has an object over the base. For μ2 data, automorphisms, torsors and gerbe classes occur in degrees0,1,2 respectively; equality of the underlying two-element sets supplies no canonical identification across degrees.')
claim(710,[720,721],
 'Determine the distinguished determinant orientation ξ_p of the slope-one-half rank-two crystal and its compatibility with the reduced-norm functor on Morita bimodules.',
 'open on the pages','C',
 'Oda Cor5.11 establishes the precise abelian-variety deRham/Dieudonné comparison, and Prop3.24 controls polarization pairings. These provide a candidate geometric determinant identification, not the specific integral norm/Morita compatibility asked for here. The exact latter theorem was not located in the searched primary sources.',
 ['Oda1969','Deuring1941','Voight2021'],brand+'; Oda exact Cor5.11/Prop3.24',comp=['slope_half_rank2'],confidence='medium')
claim(711,[722,723],
 'Frobenius descent withF²+p=0 yields an action of the quadratic order Z[F], and extends to the maximal order only when the additional integral endomorphism belongs to End(E).',
 'false as stated if the written ring of integers is automatic','C',
 'Thep=7 curve y²=x³+x has trace0 and henceF²+7=0, but(1+F)/2 is not integral because Frobenius does not fix all geometric2-torsion. Thus the maximal-order assertion requires an extra embedding/divisibility hypothesis; invertible-module twisting then uses that specified order.',
 ['Deuring1941','Silverman2009','Voight2021'],brand,comp=['maximal_order_p7'])
claim(712,[724],
 'An additive idempotent-complete category admits tensoring with finite projective modules over End(X); the canonical map P⊗X→Hom(P∨,X) is an isomorphism and P↦P⊗X is fully faithful on the corresponding generated subcategory.',
 'proof sketched','E',
 'This is the finite-projective Morita/Yoneda construction. The missing sentence after Pro61 is supplied by B15-01 scan63; the manuscript’s additional relative “jolie” converse still needs its exact finiteness/commutant hypotheses.',
 ['SGA4XVIII1973','Voight2021'],brand,proof='WriteP as the image of an idempotente on O^r. Split the corresponding idempotent onX^r. Free modules give the tensor–dual-Hom comparison, and passage to direct summands gives it forP. Morphisms are the matching matrix cornersfM_{s×r}(O)e, proving full faithfulness with consistent handedness. A strict generator makes every object a retract of a finite sum and gives essential surjectivity.')
claim(713,[725,726],
 'The action of autoequivalences on strict-generator classes has stabilizer described by outer automorphisms of the endomorphism order, followed by pointed-set fibres and order-type orbits.',
 'proof sketched','E',
 'The group-action and Morita descriptions are established. The sequence is not a sequence of groups after the isomorphism-class terms, and arbitrary ideal-class quotients must not be confused with the Picard group.',
 ['Voight2021'],brand,proof='Choose a strict generatorX. An autoequivalence preserving its isomorphism class yields an automorphism ofEnd(X), well-defined modulo inner automorphisms from changingX≅F(X). Conversely twist the module action by such an automorphism. The remaining fibres are exactly stabilizer orbits, which proves pointed-set exactness without imposing nonexistent group laws.')
claim(714,[727,731],
 'Under generic innerness, invertible bimodules admit embedded ideal representatives and isomorphisms are central scalar multiplications; automorphisms of the unit are central integral units.',
 'proof sketched','E',
 'Voight18.4.3–18.4.6 gives the exact scalar quotient in the central-simple setting: generic scalarsF* and unit stabilizerR*. The page’s generic-inner hypothesis cannot be dropped for arbitrary algebras.',
 ['Voight2021'],brand,proof='A generic bimodule trivialization identifies the bimodule with a full latticeI⊂E. A generic E–E-bimodule endomorphism ofE is multiplication by an element ofZ(E), hence an isomorphismI→J is a nonzero central scalar carryingI toJ. Scalars fixingO areZ(O)*. The quotient on classes is therefore byZ(E)*, not onlyZ(O)*.')
claim(715,[728],
 'The ramification quotient of two-sided ideal classes modulo central ideals is the sum of local exponent groups Z/e_vZ in the maximal-order Dedekind setting.',
 'stated without proof','E',
 'Classical maximal-order ideal theory establishes the quotient; for quaternion algebras over global fields Voight18.3.8/18.4.9 gives the explicitZ/2 factors. The tentative identification with the whole local Brauer group is too broad: residues and unramified terms must be specified.',
 ['Voight2021','GrothBrauerII1966'],brand)
claim(716,[729],
 'The supersingular endomorphism quaternion algebra is ramified atp and∞, and forp>3 the automorphism orders atj=0,1728 are6,4.',
 'false as stated on the literal split/reversed-orders reading','C',
 'Deuring’s classification and SilvermanIII10.1 give the corrected assertions. The literal word “splitté” and reversed4,6 assignment are scan alarms; characteristics2and3 have separate exceptional cases.',
 ['Deuring1941','Voight2021','Silverman2009'],brand,comp=['exceptional_j'])
claim(717,[730],
 'Supersingular elliptic-curve classes correspond to oriented maximal quaternion orders; forgetting orientation identifies the Frobenius-paired classes. An orientation-reversing order automorphism exists exactly when the correspondingj lies inF_p.',
 'stated without proof','E',
 'Voight42.4.8 gives the equivalence after quotienting curve isomorphisms by±1;42.4.6 gives the two orientations. Frobenius interchanges these, proving the statedj/F_p condition. The unfinished final unit question remains unidentifiable as a full assertion.',
 ['Deuring1941','Voight2021'],brand,proof='A maximal order has two residue-field orientationsO→F_p²→Fbar_p. Their exchange corresponds to the Frobenius twist of the curve. The underlying oriented objects become isomorphic exactly when E≅E^(p), equivalent overFbar_p toj(E)^p=j(E). This proves the criterion for the orientation-reversing coset, retaining reduced isomorphisms±1.')
claim(718,[733],
 'Invertible two-sided ideals commute under condition(C); maximal orders over a Dedekind domain satisfy(C).',
 'stated without proof for the classical example; hypothesis in the general argument','E',
 'The maximal-order case is exactly the classical prime-ideal factorization theorem, verified in Voight18.3.4. General nonmaximal orders need not satisfy it; the subsequent Picard construction is conditional.',
 ['Voight2021'],brand)
claim(719,[734,735],
 'Under(C), the embedded-ideal model defines a strictly commutative Picard groupoid attached to Z(E)*→I(O); the transported bimodule commutor is μ_JI^−1μ_IJ.',
 'proof sketched','B',
 'The construction is a direct instance of the two-term Picard formalism in SGA4XVIII1.4.11–1.4.15. It establishes the stated commutor under(C), not an elementwise flip of arbitrary noncommutative bimodules. No independent priority claim is made for this manuscript model.',
 ['SGA4XVIII1973','Voight2021'],brand,proof='Objects are the abelian groupI(O), arrowsI→J are centralz withJ=zI, and tensor is product on objects/scalars. All constraints can be identities in this model. Invertibility identifiesI⊗J withIJ; transporting the identityIJ=JI yieldsμ_JI^−1μ_IJ. Associativity, symmetry and hexagons reduce to equality of the same multiplication map. Kernel/cokernel giveπ1=Z(O)* andπ0=I(O)/Z(E)*.')
claim(720,[736,740],
 'The transported Brandt commutativity constraint is independent of the strict generator, with coherent composition of Morita transports.',
 'proof sketched','B',
 'The particular generator-change proof is valid under(C). It follows explicitly from the ideal multiplication identities and is consistent with established Morita/Picard formalism. It does not depend on the broader unchecked autoisomorphism bracket.',
 ['SGA4XVIII1973','Voight2021'],brand,proof='For a connecting invertible idealP, T_P(I)=PIP^−1. The multiplication identificationT_P(IJ)=T_P(I)T_P(J) transports both commutors to the same product. T_QT_P=T_QP by cancellation; replacingP byPS changesT_P only by conjugation withS, which is trivial onI(O) under(C). These are the needed coherence identities.')
claim(721,[737,738],
 'A fixed monoidal autoequivalence of a Picard groupoid need not preserve its specified commutor; a suitable new tensorator may turn the same underlying functor into a symmetric one.',
 'false as stated on the broad Pro autoisomorphism reading; Codex auto-intérieurs alternative unresolved','C',
 'The explicitF2³ example exhaustively verifies all groupoid and coherence hypotheses and refutes the broad fixed-tensorator assertion. The alternative reading “inner” is not refuted. Changing the tensorator repairs this example but creates a different monoidal functor.',
 ['SGA4XVIII1973'],brand+'; targeted monoidal-autoisomorphism/commutativity-constraint queries root_search_010',comp=['Picard_counterexample'],confidence='high')
claim(722,[739,741],
 'A connected2-groupoid over a point is reconstructed from torsors under the coherent automorphism Picard groupoid of a chosen object; the stated base-change construction works when the same structural hypotheses survive.',
 'stated without proof','B',
 'The pointwise torsor statement is formal and established. A sitewise version additionally requires descent/local connectedness; the manuscript explicitly retains the base-change hypothesis and supplies no automatic preservation theorem for arbitrary base change.',
 ['SGA4XVIII1973','DeligneMilne1982'],brand,proof='For a chosen objectc, composition givesHom(c,d) a simply transitiveAut(c)-action. A torsor yields the corresponding object in the connected delooping via contracted products. Evaluation/composition give mutually inverse equivalences up to their canonical2-isomorphisms. Over a site one must impose effective descent; this proof only treats the pointwise statement.')
claim(723,[744],
 'Commutation of finitely generated embedded ideals is detected at every localization; under Dedekind hypotheses local invertible ideals can be extended to global ones. Completion variants retain their own extension/descent hypotheses.',
 'proof sketched','E',
 'The sufficient local-to-global direction is elementary equality of finite submodules; Dedekind ideal extension proves the converse for localizations. Faithfully flat completion detects equality but does not automatically globalize arbitrary completed objects. The two witnesses differ in the marginal hypotheses.',
 ['Voight2021'],brand,proof='IfI_pJ_p=J_pI_p at every prime, the finite module(IJ+JI)/IJ and its analogue moduloJI have all localizations zero and hence vanish. Over a Dedekind base prescribe the given local ideal at one prime and the unit ideal elsewhere; intersect the resulting local lattices insideE. Local principality implies invertibility, so a global(C) hypothesis tests the chosen local pair. This does not assert the analogous extension from every completion without further work.')
claim(724,[746],
 'The real unitary group of a positive adjoint algebra is compact; for a connectedQ-torus its rational points are Zariski dense, so polynomial identities extend from them.',
 'proof sketched','E',
 'The compactness argument is valid for the real group. MilneAG14.42 supplies the exact rational-density condition. Neither compactness of the rational-point set nor density for disconnected multiplicative-type groups follows.',
 ['MilneCM2020','MilneAG2015'],torus,proof='Choose a faithful positive adjoint representation. The form||a||²=Tr(a′a) is positive definite. Ifu′u=1, then||u||²=dimV; the unitary locus is a closed subset of that finite-dimensional sphere and is compact. Density ofT(Q) for aQ-torus is invoked only in the separate algebraic-identity step.')
claim(725,[747,748,749],
 'A finite-dimensional commutative positive-involutionQ-algebra is a product of totally real fields with identity involution and CM fields with complex conjugation; the manuscript’s CM-only statement needs an exclusion of real factors.',
 'false as stated if all factors are required to be CM','C',
 'MilneCM1.36–1.40 gives the precise classification. The unit-object algebraQ is an immediate counterexample to a CM-only conclusion under the algebraic hypotheses actually written. Its unitary factor isμ2, so finite sign data are lost by omission.',
 ['MilneCM2020'],torus,proof='Positivity eliminates a nonzero nilpotent ideal: fornonzeroa in it, a′a has positive trace and is nonzero, and repeated squaring of the self-adjoint element never vanishes. The algebra is therefore a product of fields. OverR positivity forbids exchanged factors and leaves(R,id) or(C,conjugation); transitivity of embeddings of each number field yields the real/CM alternatives. The exampleB=Q shows the extra CM-only assertion fails.')
claim(726,[750],
 'The algebra generated by G(Q) determines the represented group only with sufficient rational-point density; disconnected multiplicative-type bands may be invisible to those points.',
 'stated without proof on the page; missing connectedness qualification','C',
 'MilneAG14.42 verifies density for tori. The3-torsion subgroup of the norm-oneQ(i)-torus is nontrivial but has only the identityQ-point, so the proposed method cannot see every disconnected band. This is a formal representation example, not a realized geometric-motive counterexample.',
 ['MilneAG2015','MilneCM2020'],torus,comp=['norm_character_lattices'])
claim(727,[751,754],
 'The written similitude equation on a CM fieldL/K gives relative normε and absolute normε^[K:Q]; on a real identity-involution factor it givesρ²=ε. The multiplier’s weight convention must be fixed.',
 'open on the pages in the final NB','B',
 'The norm identities are exact algebraic consequences. They do not by themselves settle whetherε means the Tate character, a weight-w multiplier, or another normalization in the manuscript.',
 ['MilneCM1981','MilneCM2020','DeligneMilne1982'],torus,comp=['norm_character_lattices'],proof='Forρ valued inL*, the involution identity saysN_L/K(ρ)=ε embedded diagonally inK*. ApplyingN_K/Q yieldsN_L/Q(ρ)=ε^[K:Q]. If the involution is identity the first equation isρ²=ε. Any replacement ofε byε^w is a convention choice that must be supplied separately.')
claim(728,[752],
 'Reconstructing the characterε from norm characters is an integral divisibility problem in the character group; uniqueness for tori follows if a root exists, while disconnected torsion may destroy it.',
 'open on the pages','B',
 'The character-lattice dictionary resolves the algebraic part. Coprime norm degrees allow a Bézout reconstruction; otherwise rational division need not lie in the integral lattice. This does not identify the manuscript’s group with a universal Serre group.',
 ['MilneAG2015','MilneCM1981'],torus,proof='For a torusX*(T) is torsion-free, so dχ=η has at most one solution, and it has one exactly whenη∈dX*(T). Ifd_iχ=η_i withgcd(d_i)=1, chooseintegersa_i withΣa_id_i=1 and obtainχ=Σa_iη_i. For a disconnected diagonalizable group the character group may have torsion, so multiplication byd need not be injective.')
claim(729,[753],
 'The weight cocharacter lift has an integral obstruction; compactness of the real kernel gives at most one split lift with prescribed composite, but does not prove existence.',
 'open on the pages','B',
 'The norm torusRes_Q(i)/Q G_m gives an explicit obstruction: aQ-cocharacter has norm exponent2n, hence no norm section. A weight-two lift exists. The uniqueness assertion follows from absence of split cocharacters in a compact real torus.',
 ['MilneAG2015','MilneCM1981'],torus,comp=['norm_character_lattices'],proof='Galois swaps the two coordinates ofX_*(Res_Q(i)/Q G_m), so invariant cocharacters are(n,n); the norm sums them. Two lifts differ by a cocharacter into the kernel. A nonzeroR-split cocharacter in a compact real torus would have unbounded real image, impossible.')
claim(730,[757],
 'For the actual representation trace on a field factorL acting onV, Tr_V(a)=dim_L(V)Tr_L/Q(a).',
 'stated without proof','E',
 'The trace proportionality is established under the representation hypothesis. It is not a consequence of positivity of an arbitrary linear functional alone.',
 ['MilneCM2020'],torus,proof='Choose anL-basis ofV. Multiplication bya hasdim_L(V) identicalQ-linear blocks, each with traceTr_L/Q(a). Their traces add, giving the asserted proportionality.')
claim(731,[760],
 'The literal square-root majorant solution has prefactorpα; the initial-value differential equation requires1/(pα).',
 'false as stated','C',
 'Exact differentiation gives the wrong initial derivative multiplied byp²α². Replacing the prefactor by1/(pα) solves the displayed equation identically on the chosen local square-root branch. The printed-source identity of the recycled draft remains unverified.',
 ['BourbakiVarietes1967_1971'],analytic,comp=['ODE_initial_derivative'])
claim(732,[761],
 'The binomial identity on the reused sheet requires coefficients binom(2n,n)/(2n−1); the literal denominator-free formula is false.',
 'false as stated','C',
 'The exactx² coefficient is−8 instead of0. The corrected formal square-root series verifies the equation; this is a scan alarm and not an edit of the diplomatic text.',
 ['BourbakiVarietes1967_1971'],analytic,comp=['binomial_identity'])
claim(733,[762],
 'To dominate coefficients byMα^n with denominator(1−αt), α must be sufficiently large relative to the original coefficient growth, not arbitrarily small.',
 'false as stated on the α assez petit reading','C',
 'The geometric-series counterexampleβ^n disproves the small-α wording. Standard majorant arguments work after the direction is corrected or the denominator convention is changed; the ink decides which.',
 ['BourbakiVarietes1967_1971'],analytic,comp=['majorant_direction'])
claim(734,[763],
 'For analytic equations with invertible Jacobian in the unknowns, the normalized formal implicit solution is unique degree by degree, and a convergent majorant gives a local analytic solution with uniqueness.',
 'proof sketched','E',
 'The implicit-function result is classical; Bourbaki§1.5 and§3.2 provide the checked analytic counterpart. The manuscript’s finite-dimensional complete-valued-field setting and the degree≥2 remainder condition are retained.',
 ['BourbakiVarietes1967_1971'],analytic,proof='Normalize the unknown-linear part to the identity. In total degreen, every nonlinear monomial containing an unknown coefficient uses only coefficients of degrees<n, because the remainder has order≥2 and the unknown series has no constant term. Thus recursion gives a unique formal solution. The stated majorant dominates these coefficients on a smaller polydisc, proving convergence; the inverse-function uniqueness gives the analytic uniqueness. The formal recursion alone does not prove convergence.')
claim(735,[763],
 'The integrability defect in the Frobenius construction satisfies a homogeneous linear ODE and vanishes by its zero initial value.',
 'proof sketched','E',
 'This is the ordinary analytic Frobenius theorem, with its coefficient compatibility and local analytic existence assumptions. Bourbaki§9.3.3/9.3.7–9.3.8 is the exact modern counterpart; no arithmetic Frobenius assertion is involved.',
 ['BourbakiVarietes1967_1971'],analytic,proof='Differentiate the proposed integral solution in a transverse variable and subtract the prescribed component. The chain rule and the displayed Frobenius compatibility cancel the inhomogeneous terms, leavingw′=A(t)w. Sincew(0)=0, uniqueness for the analytic linear initial-value problem givesw=0. This proves the local compatibility step, with the index-correction alerts kept separate.')
claim(736,[761,759],
 'Near the unit of a commutative complete normed algebra of characteristic≠2, the chosen continuous square root is unique; sums/products of convergent majorants dominate the corresponding series.',
 'proved there, apart from the separate misprinted binomial coefficient','E',
 'The local uniqueness and majorant operations are valid. The erroneous displayed coefficient does not invalidate the separate factorization proof of uniqueness once a root has been constructed.',
 ['BourbakiVarietes1967_1971'],analytic,proof='Ifg²=g1² and both equal1 at0, commutativity gives(g−g1)(g+g1)=0. The second factor is close to2 and is invertible on a smaller neighbourhood, so the roots agree. Majorant addition follows from the triangle inequality; product majorants follow by the finite coefficient convolution and absolute convergence.')
claim(737,[764],
 'For an odd primep, −1 is a square modulo p exactly whenp≡1 mod4; the Pro/Codex scratch lines differ in negation and congruence sign.',
 'stated without proof; exact scratch reading uncertain','E',
 'The quadratic-residue criterion is classical and verifies the coherent alternatives. It does not decide whether the manuscript is listing two cases or contains a missed negation.',
 ['Deuring1941'],analytic+'; original Pro77 and CodexK15-02 scan77 compared',comp=['Legendre_minus1'],proof='The cyclic groupF_p* has orderp−1. Its unique element−1 of order2 is a square precisely when4 dividesp−1. The calculation applies only to oddp.')
claim(738,[765],
 'For the inclusion of the small étale site into the big étale site, the pullback on sheaves is fully faithful and the canonical cohomology comparisons are isomorphisms.',
 'proof sketched','A',
 'The detached leaf matches Grothendieck’s SGA4VII Proposition4.1 at both statement and comorphism/Leray proof. Both sites use the étale topology; the comparison is not a universal étale–fppf assertion.',
 ['SGA4VII1972'],analytic+'; root_search_006/007/008/010 SGA4VII original and published numbering')

def save():
 (P/'claims.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n')
 for name,rows,fields in [('claim_events.tsv',E,['statement_id','date','who','type','outcome']),('claim_searches.tsv',S,['statement_id','search_ids','refs','result'])]:
  with (P/name).open('w') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
 print({'root_claims':len(C),'events':len(E),'searched':len(S)})
if __name__=='__main__':save()
