#!/usr/bin/env python3
"""Manual problem-index judgments; occurrences and references are serialized mechanically."""
import json,pathlib
r=pathlib.Path(__file__).resolve().parents[1];cs={x['id']:x for x in json.loads((r/'claims.json').read_text())};it={x['id']:x for x in json.loads((r/'items.json').read_text())};out=[]
def P(n,title,claims,plausible,why,worth,extra_items=()):
 cc=[cs[f'CL-SA12-{x}'] for x in claims];ii=list(dict.fromkeys([i for c in cc for i in c['items']]+[f'SA12-{x}' for x in extra_items]));items=[it[i] for i in ii]
 out.append(dict(id=f'MP-SA12-{n:02}',title=title,occurrences=[dict(item=i['id'],cote=i['cote'],scans=i['scans'],lines=i['lines']) for i in items],as_he_states=' '.join(c['his_statement']+': '+c['statement'] for c in cc),plausible_today=plausible,state_of_art=' '.join(c['id']+': '+c['present_status'] for c in cc),why_open=why,worth=worth,refs=list(dict.fromkeys(k for c in cc for k in c['refs']))))
P(51,'Formal tame inertia, the homotopy boundary, and nonsplitting',[201,203,204],
 'Keep the sequence pi_2(D)→T^(p-prime)→pi_1(U)→pi_1(D)→1, the cyclotomic action and the normal-bundle Chern class. Vanishing pi_2 makes inertia injective but does not split its extension. A P1 degree-zero normal bundle gives an infinite inertia Tate module.',
 'The source supplies a sequence and calls a curve extension trivial; it gives no proof eliminating the H² extension obstruction. No psychological reason is inferred.',
 'Worth a short explanatory companion: the finite formal elliptic cover makes the precise failure checkable without inventing a new research conjecture.')
P(52,'The arithmetic tame second homotopy question',[205],
 'Specify S, coefficient primes, allowed inertia and real places before asking for a K(pi,1) comparison or pi_2. Schmidt’s pro-p results after enlarging S are an established special case, not a calculation for every original all-prime tame site.',
 'The leaf ends with explicit question marks. Opened literature does not document why this exact formulation was dropped.',
 'Worth a focused formulation audit; a few hours can isolate one fixed prime and one arithmetic site, not solve every version.')
P(53,'Arithmetic finiteness, nonabelianity, and the infinite place',[206],
 'A cubic with squarefree discriminant229 and three real roots has a nonabelian S3 splitting field with tame ramification; a claim of universal abelianity therefore fails under that allowed-prime convention. Finiteness is a different question.',
 'The negative clause differs between the two transcriptions, so the source question cannot be sharpened by silently choosing fini or abélien.',
 'Worth scan collation first, because different readings ask genuinely different arithmetic questions.')
P(54,'Semiglobal Abhyankar and commuting branch inertia',[207],
 'Under regularity, a strict normal-crossing boundary, henselian connected-cover control and indices invertible on the base, local Kummer covers give commuting branch factors; no arithmetic centrality follows automatically.',
 'The page promises a proof; later SGA/Schmidt sources give the local mechanism, but every semiglobal convention must be retained.',
 'Worth a bounded comparison of the exact henselian-pair convention with the final tame-cover category.')
P(55,'Kummer Chern classes versus lifting extensions',[201,211],
 'For chosen identifications of inertia with roots of unity, the lifting gerbe of the prescribed finite quotient is compared with the gerbe of roots of O(D_i); the sign follows the chosen transition-equation convention.',
 'The source marks the comparison as desired, and cancellations affect the coefficient group. It does not fix every sign/trivialization in the surviving text.',
 'Worth a finite-level Čech comparison; the Codex201 gerbe construction gives an actual archival continuation, not a modern analogy.')
P(56,'Formal-scheme and locally ringed-topos variants',[208],
 'Choose a site with effective descent and the required purity/Kummer local models before extending the construction; no universal theorem for every locally ringed topos is supported.',
 'The surviving text is a programme and supplies no complete hypotheses; no opened source explains its abandonment.',
 'Low priority until the intended category is identified, because otherwise a research run would formulate its own problem.')
P(57,'From the finite-coefficient H² functor to pi₂',[210],
 'On FinAb, H¹(X,C)=0 for every coefficient C implies left exactness and strict prorepresentability. A further theorem must identify the resulting proobject with the chosen étale-homotopy pi₂.',
 'The page states prorepresentability in a few lines and changes from a simply connected object to a universal procover without supplying the comparison theorem.',
 'Worth a precise companion proof that separates the elementary categorical result from the homotopy comparison.')
P(58,'Inertia functoriality and the Remords',[211,212,246,247],
 'An equivariant extension sends stabilizers into stabilizers. Common Tate-sheaf trivializations are needed to state conjugacy of homomorphisms rather than merely conjugacy of inertia subgroups. A square multiplicity matrix is invertible on the prime-to-p Tate lattice iff its determinant is ±p^r.',
 'The explicit Remords revises the strength of the formulation. Schematic density proves uniqueness of extension, not existence.',
 'Worth a short source-to-SGA comparison retaining all basepoint and trivialization choices.')
P(59,'Does uniqueness of the infinitesimal kernel require reducedness?',[221,222],
 'No: an infinitesimal normal subgroup with finite étale quotient is unique without reducedness. Reducedness instead matters for pointed rigidity. Admissibility descends faithfully flatly using that uniqueness.',
 'The author asks S réduit? beside the kernel assertion and separately corrects the direction of the descent implication.',
 'Closed by the independent proof here; useful as a clean explanatory distinction in the companion.')
P(60,'Pointed rigidity and minimality for finite group schemes',[214,215,224],
 'Retain a connected reduced base and a structural category closed under the equalizers/images actually used. Arbitrary variable-base finite-flat groups do not satisfy these closure conditions; constant k-group maps are a narrower category.',
 'The letter calls its hypotheses temporary and later restarts the proof. The nonflat equalizer/cusp obstruction explains a logical gap, not the author’s undocumented motivation.',
 'Worth a hypothesis table comparing the letter, its restart and Nori’s final field-based theory.')
P(61,'The homotopy sequence for infinitesimal fundamental groups',[216],
 'Use Zhang Theorem2.1 with proper separable f, reduced connected locally noetherian schemes over a perfect field, irreducible base, geometric connectedness and the required base-change/normality condition on every saturated torsor.',
 'The manuscript explicitly inserts conjecture. The opened modern theorem provides exact extra hypotheses rather than an unconditional family theorem.',
 'Worth an exact archival-to-modern theorem comparison; the general slogan alone is no longer an open problem.')
P(62,'Uniform variation in proper smooth families',[217],
 'Distinguish homotopy exactness, invariance under algebraically closed field extension, and constancy in families. The strong hope is false: SGA1’s editorial note records Artin’s counterexample, and Pauly gives smooth base-extension counterexamples.',
 'SGA1 explicitly records the later obstruction to the strong hope. No claim is made about the date of Artin’s unpublished example beyond the publication that records it.',
 'Worth a companion warning with precise counterexample scope, not a new attempt to prove the unrestricted assertion.')
P(63,'Proper Künneth for the finite group-scheme fundamental group',[218],
 'For proper connected reduced schemes with rational basepoints over an algebraically closed field, the established Nori Künneth theorem applies; nonproper products require additional conditions and may fail.',
 'The source labels the formula conjectural; Mehta–Subramanian2002 and the opened Zhang discussion establish its proper fate.',
 'Closed in the stated proper setting; a short run can map the historical hypotheses and the nonproper obstruction.')
P(64,'The abelian-variety formula lim A[n]',[219],
 'For an abelian variety A with the origin as basepoint, multiplication isogenies dominate pointed finite-group torsors, giving the inverse system A[n] with the appropriate multiplication transitions.',
 'The letter presents the expected formula without the later argument; Nori1983 is the exact published theorem.',
 'Closed as a theorem; useful for a historical comparison, not a priority claim for this dossier.')
P(65,'Witt modules and the three-piece p-primary expectation',[220],
 'A definite comparison requires specifying the infinitesimal, étale and multiplicative parts, the ground field, and the exact module category. The fragment alone does not specify one theorem.',
 'The letter says Cartier should have done it and predicts a uniform application; no precise citation or full construction is present.',
 'Defer mathematical development until the intended Cartier/Dieudonné statement is identified; the present residual is bibliographic and formulational.')
P(66,'Arithmetic versus geometric finite-group-scheme invariants',[248],
 'Keep the k-group-scheme theory with its rational/geometric basepoint conventions separate from descent of the geometric object and from arbitrary base extension.',
 'The letter deletes a centre-of-Galois formulation and says the arithmetic definition is obscure. Later counterexamples show base extension is substantive.',
 'Worth a controlled comparison using the published18August1959 letter and one exact modern definition.')
P(67,'Can equalizers be used in the variable-base minimality proof?',[223,224],
 'Require closure under finite-flat equalizers, or change the structural category/topology. Over k[t], Eq(0,[t] on alpha_p) is not flat; on the reduced cusp, distinct S-maps can have identical pointed pushforwards.',
 'The argument calls a coincidence scheme a torsor before establishing flatness; the later source inserts a category-closure axiom.',
 'Worth a short negative-example companion; it isolates precisely why a plausible proof does not work over an arbitrary base.')
P(68,'Complete the monic-factor argument',[226],
 'For connected A, comaximal factors of a monic principal ideal in A[T] have unique monic generators. CRT makes each quotient finite projective of constant rank; Cayley–Hamilton supplies the generator.',
 'The page explicitly leaves a petite vérification and ends mid-sentence. The next leaf contains diagrams, not the missing proof.',
 'Closed by an independent proof here; no further research task is needed beyond exposition.')
P(69,'The provisional étale representability criterion',[227],
 'Keep limit compatibility, descent/localization, complete-local rigidity, separation and finite geometric fibres with algebraically closed extension invariance distinct; compare each axiom with the exact SGA3XI criterion before claiming equivalence.',
 'The source restarts an induction proof and leaves parts incomplete. The broad modern representability framework does not certify this exact list.',
 'Worth a bounded axiom-by-axiom comparison with SGA3XI; its first step is a logical implication table.')
P(70,'Gluing local étale models',[228],
 'Local models must extend to actual neighbourhoods with compatible overlaps. Values only over local schemes do not by themselves give an open global subobject.',
 'A marginal insertion adds neighbourhood data; the earlier paraphrase omitted it. The source’s alleged Je ne suis pas sûr quotation is absent from the attached witnesses.',
 'Worth an explanatory repair preserving the added hypothesis; the bare omitted-hypothesis formulation is false.')
P(71,'Representability of the relative pointed-torsor functor',[229],
 'The question concerns fixed finite étale G and a proper flat f with section and universal f_*O_X=O_S. Finiteness of fibres and the claimed étale/quasi-finite representation must be established in this relative variable, independently of prorepresentability in G.',
 'The page explicitly asks est-il représentable?? and Cas fini??; neither group-variable prorepresentability nor constructibility proves the full relative claim.',
 'Worth a focused comparison with the precise proper/separable SGA1 cases and SGA3 representability criteria.')
P(72,'Which punctured local object has two inertia generators?',[236],
 'Spec C[[x,y]] has trivial étale pi₁, whereas deleting xy=0 gives the normal-crossing two-inertia model in characteristic0.',
 'The page labels the unpunctured spectrum next to the rank-two expression; an omitted boundary is plausible but cannot be supplied without the scan.',
 'Scan collation is the first task; no mathematical development should rest on the current literal label.')
P(73,'Local and global Bertini variants',[240,241,242,243],
 'Keep geometric irreducibility, image-dimension bounds, local normal/unibranch/smooth conditions, properness and base-field extension separate. A Grassmannian incidence argument handles connected special sections; arbitrary special sections cannot simply be iterated as irreducible ones.',
 'The pages list variants with brief reasons and cross-references; an exact unchanged printed home for the entire local-property list was not established.',
 'Worth a theorem concordance with all quantifiers; this is a better bounded task than a general new Bertini theorem.')
P(74,'Tame Lefschetz with a boundary',[244],
 'For regular proper pairs with strict normal crossings, use Esnault–Kindler Theorem1.1: Lef gives surjectivity, Leff plus meeting effective divisors gives isomorphism. Retain the draft’s own codimension/transversality conditions when comparing.',
 'The draft proof refers to tame specialization and Bertini. Later formulations use explicit hypotheses, not every possible boundary convention.',
 'Worth a short comparison of the archival and modern boundary conditions; core results are established.')
P(75,'Vanishing-cycle conjugacy in characteristic two',[245],
 'For every Lefschetz pencil on a smooth projective variety over an algebraically closed field, vanishing cycles with finite coefficients of order prime to the characteristic are conjugate up to sign; the required vanishing-cohomology hypotheses remain for irreducibility.',
 'The manuscript expressly leaves the characteristic2/odd-total-dimension case open. Deligne1980 handles sufficiently general pencils; Orgogozo2005/2006 §11 settles all pencils, with Gabber’s2005 monodromy-image argument.',
 'Closed: retain as a strong example of a historical question whose modern answer is more complete than the original SGA account.')
P(76,'Uniform completion on the reused sheet',[251],
 'Minimal Cauchy filters yield the separated completion, with entourages defined on the completion itself. The X and W symbols in the composed relation must be collated.',
 'The reused typescript cuts off during the argument; this is not evidence that completion was an open theorem.',
 'Low priority beyond attribution and the two notation alarms; the mathematical construction is classical.')
P(77,'The relative étale Künneth diagram',[252],
 'Under proper separable surjective f with universally connected fibres, use the homotopy exact sequences to obtain surjectivity; retain the displayed fibre-injectivity or section condition for the isomorphism.',
 'Two parallel leaves sketch the argument with changes of notation. No failure is inferred from the duplicate draft alone.',
 'Worth a short diagram proof with the nonabelian exactness conditions explicitly checked.')
P(78,'Finite-group quotients of nonseparated étale schemes',[255],
 'The finite étale version has a clopen free locus and finite étale quotient. For general nonseparated étale schemes the doubled-origin involution disproves the claimed open free locus.',
 'The source has a tentative cas fini qualification. Its intended placement is mathematically decisive.',
 'Closed as a diagnostic; the next useful step is scan collation of that qualification.')
P(79,'Direct images and relative Hom of finite covers',[258,260],
 'Proper dominant maps to connected normal locally noetherian targets have finite-index pi₁ image. General universally open f_* representability needs a precise category; Gabber constructibility alone is weaker than finite étale local constancy.',
 'The source moves from the proper/normal claim to a question about universal openness. The nodal example warns against dropping normality.',
 'Worth isolating one exact representability functor and testing its local constancy, not extrapolating from constructibility.')
P(80,'Strict prorepresentability for infinite discrete groups',[261,262],
 'SGA3X6.2 gives strict prorepresentability of representable pointed constant-group torsors over connected locally noetherian S. The appropriate ordinary group limit recovers discrete homomorphisms, not all continuous Set maps.',
 'A cancelled limit argument is replaced by a component/DVR argument. The final printed theorem and its representability caveat must both be retained.',
 'Worth a clean comparison with Bhatt–Scholze7.4.6; it prevents conflation of group and Set criteria.')
P(81,'Five topology classes and effectiveness',[264],
 'Finite étale torsors descend in the usual compatible topologies. Infinite fpqc torsor sheaves, representable torsors and geometric coverings need not be identified without effectivity and representability hypotheses.',
 'The source expressly marks effectivity as a question. SGA3X’s corrected footnote preserves this distinction rather than resolving every draft C1–C5 claim.',
 'Worth a tightly scoped comparison of one pair of classes; first identify the precise meanings of C1–C5 from the leaf.')
P(82,'The spectral-sequence calculation of pi₂',[265],
 'Fix the universal procover, coefficient category and indexing; use H¹-vanishing to extract the intended low-degree exact sequence. The written H¹=lim H² is not taken literally as a theorem.',
 'The diagram is incomplete and changes cohomological degrees/indices. The later Artin–Mazur framework supplies a language, not the missing source formula.',
 'Worth scan collation and an exact spectral-sequence reconstruction before broader arithmetic applications.')
P(83,'Nonabelian H¹ and fibration diagrams',[266],
 'Effective descent describes pointed torsors by nonabelian cocycles. Any fibration exact sequence needs the exact morphism, basepoint, band/action and cover hypotheses.',
 'The leaves supply diagrams without a complete theorem statement; no opened source proves every unspecified diagram.',
 'Low priority until the intended objects are identified; otherwise the task would create its own conjecture.')
P(84,'Simplicial components and finite presentation bounds',[267,269],
 'For a universal effective descent cover with the stated open component conditions and connected simplicial quotient, SGA3X6.1–6.3 gives the component-nerve presentation; contracting the marked fibre requires its connectedness and simple connectedness.',
 'The draft marks a proof to supply. The corrected edition clarifies necessary component assumptions and extra basepoint generators.',
 'Worth a small explicit example of the final presentation; no claim that every written generator count is automatically exact.')
P(85,'The effective subfunctor of descent data',[268],
 'Separate strict prorepresentability of all formal descent data from effectivity in schemes and representability of arbitrary fpqc torsor sheaves.',
 'The margin may say resolved or affirmative, but its wording is uncertain. It cannot be used as proof of a general theorem.',
 'Worth a source-limited effectivity audit, beginning with the corrected SGA3X footnote and one chosen topology.')
P(86,'The three-condition Set-functor criterion',[270],
 'The stated sufficiency criterion is false. For K_n=N^n, F(I)=colim Hom(K_n,I) is left exact and preserves intersections, all limit projections are onto, yet x↦x_(x0+1) is continuous on N^N without factoring through a fixed prefix. Uniform continuity or a finite compact system repairs this test.',
 'The source states three conditions but supplies no argument controlling nonuniform continuous maps. No claim is made that the author knew this counterexample.',
 'Worth a concise counterexample companion; broader repaired representability theorems are separate research tasks.')
P(87,'Limits of continuously represented functors',[271],
 'For an actual diagram of spaces, colimits with the final topology represent the pointwise limit of continuous-map functors. For arbitrary natural transformations between such functors, full faithfulness must be justified separately.',
 'The sketch moves from a space diagram to a category-of-functors claim; the missing realization of arbitrary natural transformations is a distinct issue.',
 'Worth a narrowly defined categorical check after settling the precise morphisms in the manuscript’s category.')
P(88,'From groups to categories in the component construction',[272],
 'The component nerve gives an established group presentation; a category-valued extension needs specified objects, morphisms, descent and equivalences.',
 'The last lines state a direction rather than a precise conjecture. No publication is treated as an exact solution solely because it concerns higher categories.',
 'Defer until a concrete statement is extracted; no open-problem novelty is asserted.')
P(89,'Finite type from finite components over a Japanese base',[273],
 'A separated locally quasi-finite morphism with finitely many irreducible components over a locally noetherian universally Japanese base is finite type. Normalize the components, use finite normalization over the base and the local birational open-immersion theorem, then descend quasi-compactness.',
 'The intended theorem has a proof, but a displayed arrow from the base normalization to X has the wrong general direction; a strict open immersion already disproves that arrow.',
 'Closed by the corrected proof; useful as a companion example of a valid theorem with an invalid proof step.')
P(90,'The anonymous local pairing fragment',[239],
 'Only after identifying j0, its normalization and its domain can one formulate the final vanishing assertion. Néron pairings and Pépin’s intersection description are exact related objects but not a verified identification of this sheet.',
 'The typescript begins and ends in mid-argument, and its source was not identified by the logged backward searches.',
 'Worth a bibliographic attribution task; mathematical development before identification would risk proving the wrong statement.')
(r/'problems.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'problems':len(out),'ids':[out[0]['id'],out[-1]['id']]}))
