"""Serialize individually formulated claims after reading and exact checks."""
from pathlib import Path
import json,csv,datetime
W=Path(__file__).resolve().parents[1]
items=json.loads((W/'items.json').read_text())
by_source={v:x for x in items for v in x['sources']}
claims=[]
def C(num,ns,words,statement,status,comp,cl,fate,refs,family,confidence='high'):
    its=[]
    for n in ns:
        x=by_source[f'MPL_84_146-193#{n}']
        if x not in its:its.append(x)
    claims.append(dict(id=f'CL-SA02-{num}',items=[x['id'] for x in its],cote='84',
      scans=sorted({s for x in its for s in x['scans']}),lines=list(dict.fromkeys(l for x in its for l in x['lines'])),
      his_statement=words,statement=statement,status_on_pages=status,
      computation=comp+' See programs/recompute.py, outputs/recomputed.json and proof_checks.md.',
      **{'class':cl},fate=fate+' Search record: literature_search.tsv, family '+family+'.',
      fate_date={'qf':'Loos1996 (March); detailed follow-up1997; Voight first arXiv submission20 April2015, publicationAugust2016, corrected version17 January2021',
       'chi':'Pirashvili first arXiv submission9 April2016, v2 18 September2016; online20 June2018, printJanuary2019; exact manuscript-wide identification not found',
       'formal':'Classical elementary and homological algebra; no priority date inferred from this undated manuscript; references checked19 November2026',
       'dual':'Loos1996/1997 establish the quadratic product; exact pairing presentation checked independently19 November2026; broader identification not established',
       'unfinished':'No identifiable complete proposition; searches completed19 November2026',
       'count':'Elementary finite enumeration; checked19 November2026'}[family],
      present_status='As of19 November2026: '+fate,refs=refs,confidence=confidence))

C(200,[3],r'b=b_1b_2',
 'In local rank-one coordinates for chi-trivialised extensions, the product parameter is b1*b2; under bi↦bi+chi*ui it changes by chi*(u1*b2+b1*u2+chi*u1*u2). The chi/gamma glyph on146 remains conditional.',
 'proof sketched','Exact target and transition identities: local_groupoid_target, pushout_splitting_increment.',
 'C','The coordinate law is verified. The later quadratic/torsor constructions are partial comparators, not an identification of every chi-extension or its arrows. Earlier scans67–80 contain more of the author’s own pushout construction and are handled in the root consolidation.',
 ['Loos1997','Pirashvili2019'],'chi')
C(201,[6],r'gamma chi=2; sigma_i=I-gamma pi_i',
 'For pi_i²=chi*pi_i, sigma_i²−I=gamma*(gamma*chi−2)*pi_i. Thus gamma*chi=2 suffices. It need not be necessary for a degenerate pi_i.',
 'proof sketched','involution_defect; four-term symmetrizer expansion.',
 'C','The operator assertion is correct with its scalar condition. Pirashvili’s pq+2=0 has the same parameter equation after p=−chi,q=gamma, but his objects additionally carry quadratic Galois data and a unit discriminant; no categorical identification follows from the scalar resemblance.',
 ['Pirashvili2019','Loos1997'],'chi')
C(202,[7],r'lambda²+1=chi; lambda mu=−1; mu²=gamma',
 'The second displayed ansatz implies gamma*(chi−1)=1. Only if the first ansatz is imposed simultaneously does one obtain gamma=1 and chi=2.',
 'stated without proof','second_ansatz Groebner reduction proves the polynomial consequence; no division is used.',
 'F','The equations are consistent as a separate ansatz. Searches did not identify a named construction with exactly these variables and hypotheses; it is not legitimate to combine separate attempts without saying so.',
 ['Pirashvili2019'],'unfinished')
C(203,[8],r'H_i = noyau de ...',
 'A scalar-endomorphism sheaf and an exact sequence modulo scalar identities are proposed. The kernel arrow is unfinished. For a locally split extension with specified endpoint scalar actions, a sheaf-level triangular model has kernel Hom(M,L); global-section surjectivity is an additional assertion.',
 'open on the pages','No certificate for an unspecified kernel. The conditional triangular model is checked separately.',
 'F','The incomplete definition prevents a unique proposition being identified. Extension formalism supplies a conditional reconstruction, not the missing definition.',
 ['Stacks010I'],'unfinished','medium')
C(204,[9],r'u+sigma(u)=(lambda(u)+mu(u))I',
 'For a triangular scalar-endomorphism algebra, sigma(u)=trace(u)I−u is an anti-involution. The manuscript writes its trace-sum identity; anti-multiplicativity is a reconstruction.',
 'stated without proof','triangular_trace_anti_involution, triangular_trace_double_involution, triangular_Cayley_Hamilton.',
 'E','This is the elementary adjugate calculation. Loos1997§2.1 gives the corresponding standard conjugation for genuine rank-two quadratic algebras; it does not identify the unfinished H with such an algebra.',
 ['Loos1997'],'formal')
C(205,[11,49],r'bar(bar(x))=x; pi=2I−F',
 'If pi²=2*pi, then I−pi is an involution over any commutative base. For general chi the defect is (chi−2)pi.',
 'proved there','chi2_involution and involution_defect.',
 'E','The integral identity is correct; division by two is unnecessary. Standard quadratic conjugation is the relevant specialization, while the manuscript itself visibly sets chi=2.',
 ['Loos1997'],'formal')
C(206,[12],r'deleted 2chi=chi; replaced chi=chi; o.K.',
 'The displayed scalar polynomial −chi*(1−gamma*chi)+2chi*(1−gamma*chi)+gamma*chi² is identically chi. The contradictory intermediate equality is withdrawn.',
 'corrected by himself later (within152, lines305–317)','corrected_scalar_identity.',
 'E','The corrected arithmetic is valid. No general comparison theorem follows from this one boundary equation; searches found no independent historical proposition to attach to this scratch correction.',
 ['Stacks010I'],'formal')
C(207,[18,21,22,30,31],r'alpha=−chi gamma=−chi beta; beta=gamma; beta+delta chi=1',
 'Universal coefficient comparison yields alpha=−chi*(1−delta*chi), beta1=beta2=1−delta*chi. For an individual module, scalar annihilation of id or im(pi) does not imply scalar vanishing without faithfulness. Cancelling chi from chi*(beta−gamma)=0 is invalid in general.',
 'false as stated if the coefficient implications are asserted for arbitrary individual modules; valid as universal coefficient conditions',
 'full_F_boundary_columns and coefficient_cancellation_counterexamples over Z/4; remaining strict residual saved in full_F.',
 'C','The universally sufficient family is valid. The stronger scalar deductions need stated hypotheses. The related pq condition in Pirashvili does not justify cancellation for these arbitrary modules.',
 ['Pirashvili2019','Stacks00NV'],'chi')
C(208,[14,19],r'I+sigma_1 tensor sigma_2; o.K.',
 'At chi=2, delta=1 the four-term operator 2I−pi1⊗I−I⊗pi2+pi1⊗pi2 equals I+(I−pi1)⊗(I−pi2). The expression cancelled on152 is restored and checked on156.',
 'corrected by himself later (152→156); proved there after specialization',
 'symmetrizer_at_chi2_delta1.',
 'E','The operator identity is exact. The quadratic realization has the established counterpart described in literature_results.md, but that does not settle the arbitrary-chi comparison.',
 ['Loos1997','Voight2016'],'formal')
C(209,[15,16,17],r'indetermination ... Hom(M1 tensor M2,L1 tensor L2)',
 'If one endpoint-fixing map between two extensions exists, all such maps form a torsor under Hom(M1⊗M2,L1⊗L2). Additional trivialisation compatibility may cut down that set. The unknown last column on154 remains an existence task.',
 'proof sketched; existence of the displayed map remains open',
 'Proof in proof_checks.md§5: subtract maps, factor through the quotient, then through the subobject.',
 'E','This is standard extension algebra, with existence explicitly separated from the Hom-valued ambiguity. Stacks010I provides the precise fixed-endpoint category.',
 ['Stacks010I'],'formal')
C(210,[23,24,48],r'Je dis que E1^vee wedge E2^vee ≅ (E1 wedge E2)^vee',
 'A natural duality for the manuscript product is asserted, with a finite-local-freeness correction and determinant twists. A correct version requires finite projectivity of all dualized terms and a descended perfect pairing for the specific product.',
 'stated without proof; hypotheses partly corrected on160',
 'The chi=2 quadratic specialization is independently completed by integral_descended_pairing and both boundary certificates. General-chi identification is not certified.',
 'C','Ordinary tensor/determinant duality is established. The precise quadratic specialization is verified here; the unrestricted product-duality assertion remains sensitive to the signs and definitions. Loos provides the quadratic tensor category, not an automatic proof for every manuscript extension convention.',
 ['Loos1997','Stacks0FNJ','Stacks00NV'],'dual','medium')
C(211,[25,26,27,28,29],r'pi prime=pi−(chi−1)I; (2−chi)x2+pi2(x2)',
 'The shifted operator restricts to I on L and (1−chi)I on the quotient. Its tensor symmetrizer has the extra mixed term (2−chi)x2. The table called pi prime on164 instead has matrix [[chi,tau],[0,0]], so its name must not be transported literally from162.',
 'proved there for the mixed restriction; the factorization and lifting arrows remain open',
 'Complementary matrices and full_F; direct restriction on u1⊗x2 gives the stated residual.',
 'C','The local residual is verified and explains the chi=2 specialization. Searches of chi-scindage, quadratic tensor comparisons and the backward literature identify no result that removes it without additional structure.',
 ['Loos1997','Pirashvili2019'],'chi')
C(212,[32,33,34],r'F22=0; F21=alpha1 tensor alpha2; F12=psi1 tensor psi2',
 'A map from the displayed pushout to the pullback is determined by four blocks satisfying four squares. Setting the three displayed blocks as indicated fixes both endpoints; two squares then vanish because psi_i*alpha_i=0. The remaining F11 still has to be constructed.',
 'proof sketched; two squares checked there',
 'Universal-property proof and full_F_boundary_columns; the omitted MM restrictions are explicitly recorded.',
 'E','The block reduction is valid formal extension algebra. It establishes neither existence of the final block nor its canonicity.',
 ['Stacks010I'],'formal')
C(213,[35,37,39,223],r'une application can. d’extensions de E1 vee E2 dans E1 wedge E2',
 'Under the identity-endpoint reading of168 and the equality branch of170, an all-chi comparison between the specified pushout and pullback extensions is claimed. This universal strict comparison is false: the locally split chi=0 elliptic-curve example gives classes e and−e.',
 'open on168; stated without proof on170; false under the specified universal fixed-endpoint interpretation',
 'pushout_splitting_increment, pullback_splitting_increment, comparison_shear_obstruction; complete hypothesis check in proof_checks.md§2.',
 'C','The stated universal strict version is refuted conditionally on the endpoint reading. A sign-adjusted comparison, a restriction chi*delta=2, and the earlier pushout monoidal construction are different statements. The specialized literature does not identify the unrestricted claim.',
 ['Stacks010I','Stacks0B3A','Stacks0BY6','Pirashvili2019'],'chi','high for the conditional counterexample; medium for the ink interpretation')
C(214,[36,38],r'On definit ... extensions ... chi-trivialisations',
 'Given the written chi-trivialisation identities and universally injective inclusions, the indicated tensor boundary rows and their pushout/pullback module extensions can be formed. Locally split finite-projective inputs suffice. Further trivialisation and coherence assertions require their own checks.',
 'stated without proof; diagrams give the construction',
 'Local normal form and exactness argument in proof_checks.md§§1–2. The comparison is separately tested.',
 'C','The module constructions follow formal exactness and universal properties. Later quadratic products support the specialization, while generic Picard-stack theory does not identify these two specific products.',
 ['Stacks010I','Stacks00NV','Loos1997'],'chi')
C(215,[41,202],r'u=2u1u2+b2u1+b1u2; u²+bu+c=0',
 'For Ai=R[ui]/(ui²+bi*ui+ci), the tensor element V satisfies V²+b1*b2*V+b1²*c2+b2²*c1−4c1*c2=0. The abstract product remains a free quadratic algebra over every commutative ring.',
 'stated with computations; proof sketched',
 'quadratic_product_relation; affine_generator_change and transformed coefficient certificates.',
 'B','Exact established counterpart: Loos1997§§2.8–2.10 and Voight2016 Construction3.14. The generator identifications are explicit in literature_results.md; this is mathematical correspondence, not a documented influence claim.',
 ['Loos1996','Loos1997','Voight2016'],'qf')
C(216,[42],r'delta=delta1 delta2',
 'The quadratic discriminants multiply. Consequently the product is finite etale exactly when both factors are, by the quadratic discriminant criterion; the latter consequence is reconstructed.',
 'proved there as the displayed polynomial identity',
 'multiplicative_discriminant; finite_field_enumerations give illustrations only.',
 'B','The exact counterpart is Voight Lemma3.23, including the determinant-line identification; Loos1997§2.10 gives the corresponding discriminant behavior.',
 ['Voight2016','Loos1997'],'qf')
C(217,[43,44,46,76,203],r'injectif sauf si car.2 et b1=b2=0; ca croule',
 'Over a field the stated tensor-image exception is exact. Over an arbitrary ring the kernel is Ann_R(2,b1,b2)*U, and split injectivity is equivalent to (2,b1,b2)=R. The abstract monic algebra is unaffected.',
 'stated without proof; correct over fields; false as a complete exception over all rings',
 'quadratic_maps kernel proof, small_ring_kernel_sizes; Z/4,b_i=c_i=0 kills nonzero2U.',
 'B','The abstract-versus-realized distinction is explicit in Voight Remark3.17 and Loos1997§2.8/Proposition2.9. The exact general-ring annihilator criterion is this run’s coefficient proof, not attributed to either paper.',
 ['Voight2016','Loos1997'],'qf')
C(218,[45],r'f^arrow=f+bar f; quotient map2',
 'With the explicit maps i and q reconstructed from the local bases, i*q=I+sigma1⊗sigma2, q*i=2I and T²=2T. Thus this operator is not generally an idempotent.',
 'proof sketched in the diagrams',
 'symmetrizer_factorization, reverse_composite_2, symmetrizer_squared.',
 'C','The algebra product and canonical tensor map have established counterparts. The exact drawn factorization is checked here under specified bases; uncertain arrow labels are not identified solely from a matrix match.',
 ['Voight2016','Loos1997'],'dual')
C(219,[47],r'pi=chi id−f',
 'For an exact sequence0→L→E→M→0, an endomorphism f vanishing on L and inducing chi*I on M determines pi=chi*I−f landing in L and restricting to chi*I on L, and conversely. The two inconsistent L/L-prime domain labels remain unresolved readings.',
 'proof sketched','Formal subtraction and factorization through the kernel/quotient; no invertibility hypothesis.',
 'E','This equivalence is formal exact-sequence algebra. It is valid with the corrected domain types explicitly stated as a reconstruction.',
 ['Stacks010I'],'formal')
C(220,[50,51,52],r'u1*u2−b1b2=u; deleted2',
 'The constant coefficient of q(u1⊗u2) in the displayed dual bases is b1*b2 and its U-coefficient is1. The earlier value2 is cancelled on the page.',
 'corrected by himself later (within176); proved there in the dual-basis calculation',
 'quadratic_maps, integral_descended_pairing; q(u1*u2)=U+b1*b2.',
 'B','The corrected generator agrees with Voight’s tensor generator after the essential shift; Loos uses the conjugate convention stated in literature_results.md.',
 ['Voight2016','Loos1997'],'qf')
C(221,[53],r'u1*u2−Tr1(u1)Tr2(u2)=2 dot ...',
 'The trace reformulation on176 ends after2 times an unspecified expression. Its right-hand side is not supplied.',
 'open on the pages','No computation can check an omitted right-hand side; adjacent completed identities are independently checked.',
 'F','The exact claim is not identifiable from this unfinished display. Related product formulas do not license completing it in the transcription.',
 ['Voight2016','Loos1997'],'unfinished')
C(222,[54,55,56],r'Il y a a ecrire quatre compatibilites; f−f^arrow; OK',
 'Four pairing compatibilities are announced, three enumerated. The literal Pro identity f−Tf=Tr(f)1 fails even over Q. Codex reads f+conjugate(f), which yields the standard boundary identity. The third equation also requires the tensor boundary domain.',
 'open on the pages; one local OK; a literal interpretation is false',
 'raw_Pro_178_literal_counterexample and both boundary pairing certificates.',
 'F','A unique full authorial proposition cannot be recovered from the conflicting signs/operator readings. The consistent chi=2 reconstruction is proved separately; it does not decide the manuscript.',
 ['Loos1997','Voight2016'],'unfinished','medium')
C(223,[57],r'A=(A1 tensor A2) amalg_boundary O; E similarly',
 'The trace pushout of the rank-three boundary inside A1⊗A2 is a locally free rank-two module; the paired E pushout has the corresponding extension. This module presentation alone does not yet supply multiplication.',
 'stated without proof; explicit presentations',
 'qA,qE presentation matrices and relation matrices; local bases are exhibited in proof_checks.md§4.',
 'E','The rank calculation and universal property are elementary. The quadratic algebra structure is supplied by the separately checked product, with the literature counterpart in Loos and Voight.',
 ['Stacks010I','Loos1997','Voight2016'],'formal')
C(224,[58,59,60],r'les deux sont transposes; accouplement',
 'For E_i=A_i^vee, conjugations and their tensor symmetrizers are adjoint. The newly defined product pairing has tensor block T^t plus three scalar/line blocks; unchanged ordinary brackets cannot simply be invariant under T.',
 'stated without proof; formula sketched','integral_descended_pairing; adjoint matrix and all four blocks in proof_checks.md§4.',
 'C','Adjointness is formal and the specified quadratic pairing is verified. The exact broader product-duality identification is not supplied by the generic finite-projective tensor-Hom theorem.',
 ['Stacks0FNJ','Loos1997'],'dual')
C(225,[61,62,64,65],r'deleted one-half trace; on veut que ce soit',
 'The desired pairing must annihilate both pushout relation submodules. With the intrinsic symmetrizer and the stated cross blocks at chi=2, it descends and has matrix I2 in the abstract dual bases, so is perfect without inverting2. Half-trace attempts and unfinished right-hand sides are not retained as proofs.',
 'open on the pages; normalization attempt cancelled; requirements stated',
 'integral_descended_pairing, all_A_boundary_pairings, all_E_boundary_pairings, duality_factor_2.',
 'C','The quadratic case is independently established here under explicit finite-local-freeness and pairing assumptions. Literature supplies the quadratic tensor product; no exact general-chi pairing theorem matching every drawn convention was identified.',
 ['Loos1997','Voight2016','Stacks0FNJ'],'dual')
C(226,[66,67,68],r'E1 wedge E2 ->? E1 tensor E2; OK',
 'The return map is questioned; one mixed boundary is checked. The displayed table(2,0,0,2u1u2) is correct for b1=b2=0. The lift-change formula has two mixed terms and2u1u2; the repeated u2 in the next line is a type mismatch.',
 'open on the pages; one boundary computation proved there',
 'quadratic_maps with b1=b2=0; full_F at chi=2; pushout_splitting_increment specialized to2.',
 'C','All boundary conditions for the declared chi=2 map are verified in this run. The specialized zero-entry table is not an identity for arbitrary b_i; the questionable indices remain scan work.',
 ['Loos1997','Voight2016'],'dual')
C(227,[69,70,71],r'A^vee ≅ (f,lambda), f(x_i)=lambda Tr_i(x_i)',
 'The dual of the pushout is the pairs(f,lambda) whose restriction to the boundary equals lambda times its trace. Compressed f(x_i) means f(x1,1) or f(1,x2). The prior doubled two-functional conditions and attempted E→A^vee are cancelled.',
 'corrected by himself later (within188); live annihilator condition stated',
 'Relation annihilator proof: Hom of a cokernel is the kernel of the transpose relation map; all_A_boundary_pairings.',
 'E','The live conditions are the standard universal property of the dual of a quotient. Their identification with the particular E requires the separate descended-pairing check.',
 ['Stacks010I','Stacks0FNJ'],'formal')
C(228,[72,73,74,75],r'Tr(lambda u+mu)=−lambda beta+2mu; N=...; u defined by pairings',
 'For A=R[U]/(U²+beta*U+c), trace(lambda*U+mu)=2mu−lambda*beta and norm=mu²−lambda*mu*beta+lambda²*c. Perfect dual bases characterize U uniquely; coefficient names are reversed relative to176.',
 'proof sketched; norm sign uncertain; generator question stated',
 'trace_lambda_u_mu, norm_lambda_u_mu, norm_multiplication_matrix; integral_pairing.',
 'E','The determinant calculation and dual-basis uniqueness are elementary. Standard conjugation in Loos1997§2.1 supports the same convention; the uncertain minus sign remains for ink review.',
 ['Loos1997'],'formal')
C(229,[78,79],r'u2² unsure{+|=} beta_{1|2}u2+gamma2=0; u=2uu prime+',
 'The second monic equation has uncertain operation and indices, and the product generator expression is unfinished. Earlier completed product formulas suggest a consistent reconstruction, not a completed assertion on192.',
 'open on the pages','affine_generator_change and quadratic_product_relation apply only to the stated coherent convention.',
 'F','No unique complete proposition is identifiable from these marks. The established product law remains a comparator rather than an ink emendation.',
 ['Loos1997','Voight2016'],'unfinished','medium')
C(230,[184],r'les2^6 combinaisons possibles de suites de six signes',
 'There are64 ordered sequences of six binary signs, including the two constant sequences. This finite statement is separate from claims about divination, archetypes or medical efficacy.',
 'stated without proof','editorial_counts enumerates all64 six-bit tuples.',
 'E','Elementary enumeration, explicitly reproduced. The public R&S text confirms the attribution and wording; no scientific endorsement of the surrounding worldview is inferred.',
 ['GrothendieckRS'],'count')
C(231,[4,29],r'displayed complementary matrices',
 'The displayed complementary matrices have sum chi*I, zero mixed products and square chi times themselves. At146 chi=2. These identities are implications of the written matrices rather than separately formulated authorial theorems.',
 'computations displayed without a separate theorem','P+Q, PQ, QP, P_squared, Q_squared.',
 'E','These are elementary matrix identities, valid over any commutative base. The precise names of the operators are not harmonized across leaves.',
 ['Loos1997'],'formal')
C(232,[10],r'deleted compatibility assertion and diagram',
 'The compatibility assertion cancelled on150 has no live complete proposition recoverable from the deleted fragment; later170 is a separate live comparison assertion.',
 'corrected by himself later (cancelled on150)','No computation attached to unidentified cancelled prose.',
 'F','Searches of the surrounding chi-extension problem found specialized comparators only. A historical fate cannot be assigned to a sentence whose complete mathematical content is not recoverable.',
 ['Pirashvili2019','Loos1997'],'unfinished','low')
C(233,[20],r'bar(X_i)=x_i−pi_i(x_i)=opening brace',
 'The new conjugation expression stops at an opening brace; no additional right-hand identity is present.',
 'open on the pages','The adjacent complete symmetrizer is checked separately; an unfinished expression is not a failed identity.',
 'F','No complete claim can be matched. Literature on conjugation supplies nearby valid formulas but cannot supply the absent right side.',
 ['Loos1997'],'unfinished')
C(234,[24],r'Hom(E1,k) tensor Hom(E2,k) ≅ Hom(E1 tensor E2,k)',
 'For finite projective E1,E2, the natural tensor-Hom map identifies their tensor dual with the dual of the tensor product. Ordinary determinant duality in rank two is also valid. Neither formal fact identifies the manuscript’s separate product without descent.',
 'stated without proof','Local dual-basis proof and determinant-one pairing criterion in proof_checks.md§§4–5.',
 'E','Established finite-projective duality. The checked Stacks references state the exact dualizability framework; no claim of a new historical theorem is inferred.',
 ['Stacks00NV','Stacks0FNJ'],'formal')

(W/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
print(f'Serialized {len(claims)} claims with searched-fate family assignments.')
