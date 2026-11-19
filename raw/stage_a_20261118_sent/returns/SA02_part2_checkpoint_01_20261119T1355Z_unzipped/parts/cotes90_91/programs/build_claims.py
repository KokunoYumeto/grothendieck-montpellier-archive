"""Serialize manually read, researched and scoped claims. Code only formats records."""
from build_records import ROOT,OUT,loc,dump,table
claims=[]
def C(n,it,cote,scans,his,statement,status,comp,cl,fate,date,refs,confidence='high',present=None):
    if isinstance(it,int):it=[it]
    if isinstance(refs,str):refs=refs.split(';') if refs else []
    claims.append(dict(id=f'CL-SA02-{n}',items=[f'SA02-{i}' for i in it],cote=str(cote),scans=scans,lines=loc(cote,scans),his_statement=his,statement=statement,status_on_pages=status,computation=comp,**{'class':cl},fate=fate,fate_date=date,present_status='As of 2026-11-19: '+(present or fate),refs=refs,confidence=confidence))
V='verification.md §V';P='programs/verify_computations.py; outputs/verify_computations.txt'
C(500,501,90,[2],'Cond. équivalentes a) b) c) d)',
  'For a flat module M over a nonfield Dedekind domain A with fraction field K, the text equates finite saturation of every finite submodule with exclusion of the specified p-divisible submodules, absence of K in each M_p, and a directed union of finite saturated submodules.',
  'false as stated; stated without proof on the page',V+'01; C01 in '+P,'C',
  'The exclusion conditions do not imply finite saturation. M=Σ_p(1/p)Z⊂Q is a countable flat counterexample satisfying both exclusion conditions. The finite-saturation/projectivity part survives separately in CL-SA02-501. Duong–Hai §3.1 and Raynaud Chapter II establish nearby saturated-stage/Mittag-Leffler results, not this false equivalence. No exact published occurrence of this counterexample was identified by the recorded searches.',
  'Manuscript undated; Raynaud 1972; Duong–Hai circulated 2013, published 2018; refutation checked 2026-11-19','DuongHai2018;Raynaud1972')
C(501,501,90,[2],'Ces cond. sont satisfaites si les formes linéaires séparent',
  'Finite saturation is equivalent to a directed union of finite saturated submodules; separating A-linear forms imply it. For countably generated M it implies projectivity and hence separation by linear forms.',
  'stated without proof; valid surviving part of the preceding package',V+'01 gives the exhaustion, split inclusions and finite-dimensional dual argument.','B',
  'Independently reproved here. The countable projectivity mechanism is part of the Mittag-Leffler theory in Raynaud 1972 Chapter II Proposition 1 and Duong–Hai 2018 Proposition 3.1.5. Their coalgebra hypotheses are retained; they do not validate the deleted implication of CL-SA02-500.',
  'Raynaud–Gruson 1971; Raynaud exposition 1972; Duong–Hai 2013/2018','Raynaud1972;DuongHai2018')
C(502,502,90,[4],'faire l’argument',
  'If B is a flat coalgebra over a Dedekind domain and every finite submodule has finite saturation, saturating a finite subcoalgebra gives a finite saturated subcoalgebra. Every finite submodule is therefore contained in such a stage under the coalgebra-generation input.',
  'proof sketched; tensor-saturation argument explicitly deferred',V+'02 proves the tensor intersections and stability; the fundamental finite-subcoalgebra input is checked against the later reference.','B',
  'Duong–Hai §3.1 Lemmas 3.1.2 and 3.1.4 supply the saturation and tensor-intersection argument over a Dedekind ring. The finite-saturation assumption remains essential and is not replaced by 90/2(b),(c).',
  'Circulated 2013; published 2018','DuongHai2018')
C(503,503,90,[6],'N engendre l’algèbre B',
  'A finite projective stable submodule of the coordinate algebra of an affine group, containing algebra generators, gives a faithful representation after every base change. The group and coordinate algebra are of finite type in this assertion.',
  'proved there by testing arbitrary algebra-valued points',V+'02; coefficient/counit proof independently rechecked.','A',
  'SGA3 VIB 11.11 gives the field linearity theorem; the projective-coordinate-module extension and precise base restrictions appear in revised VIB §§11,13. This exact generating-submodule implication is elementary and remains valid. It is weaker than the cancelled faithful-flat assertion CL-SA02-508.',
  'SGA3 I published 1970; revised extensions dated separately in editorial notes','SGA3VIB1970;SGA3VIB2024')
C(504,504,90,[6],'syst. projectif strict',
  'Every affine group scheme over a field is a filtered inverse limit of finite-type affine group schemes with faithfully flat transition maps.',
  'stated without proof; inductive is corrected to projective',
  'Read original SGA3 VIB 11.13 and its reduction to 11.14, matching affine and field hypotheses; not a new proof of Hopf faithful flatness.','A',
  'Exact published match: original SGA3 VIB 11.13, with 11.14 supplying faithful flatness from injective Hopf algebra maps. The original header says this exposition was rewritten and does not correspond to the oral seminar; the date of the oral SGA3 seminar is therefore not used as the circulation date of this proposition.',
  'SGA3 I publication 1970; first circulation of this exact rewritten formulation not established','SGA3VIB1970')
C(505,505,90,[8,10],'i-admissible',
  'For a directed saturated system B=colim B_i of finite projective coalgebras, a finite B-comodule factors through some B_i; B_i-comodules are modules over the dual algebra B_i^∨, compatibly with the stated transition functors.',
  'proof sketched',V+'14: finite coefficients, tensor injectivity and dual-basis equivalence.','B',
  'Established finite-projective coalgebra duality and local-finiteness mechanism; Duong–Hai §§2–3 gives the Dedekind formulation. No claim is made that arbitrary flat coalgebras possess the required saturated stages.',
  'Classical finite coalgebra duality; modern exact Dedekind treatment 2013/2018','DuongHai2018;SGA3VIB2024')
C(506,506,90,[10,12],'projectif de t.f.',
  'Under those finite projective dual-coalgebra stages, a finite equivariant module is a quotient of an equivariant module finite projective over the base; the relative version additionally assumes suitable finite locally free covers on the indicated base.',
  'proof sketched; the relative base letter is uncertain',V+'14 gives U_i^r→M; the relative statement is retained conditionally on its written cover hypothesis.','B',
  'The finite-module construction is valid. Revised SGA3 VIB 13.7 treats finite comodules over projective coalgebras and supplies projective covers; it is a later editorial result, not attributed to the original 1970 proposition without qualification. The unqualified infinite-module variant is false: CL-SA02-512.',
  'Original manuscript undated; revised SGA3 VIB checked in the 2024 version','SGA3VIB2024;DuongHai2018')
C(507,507,90,[10],'si G est de t.f.',
  'For a finite-type flat affine group over the Dedekind base, the manuscript relates the finite-saturation condition to every irreducible component having nonempty fibres everywhere on the base.',
  'stated without proof; finite type is explicit',
  'Compared to the associated-point and henselization formulation of purity in Raynaud Chapter II, not silently identified with it. Disappearing-component example in V03.','C',
  'Raynaud 1972 Chapter II Theorem 1 characterizes projectivity of a flat finite-type-algebra module by purity, formulated after henselization using associated points. Duong–Hai §3.1 gives related special-local-finiteness results. These establish a precise nearby theorem, but the bare component statement requires checking geometric/henselian components and embedded associated points; the recorded searches did not identify an exact theorem with only the manuscript wording.',
  'Raynaud 1972; Duong–Hai 2013/2018; exact component formulation unresolved in this audit','Raynaud1972;DuongHai2018','medium')
C(508,508,90,[14],'G→Aut(N) … fidèlement plat',
  'The wholly crossed-out proposition asserts that the representation afforded by a stable generating module is faithfully flat onto its full automorphism group.',
  'corrected by himself later/on the same sheet: whole proposition withdrawn; false as stated',V+'02; C02 in '+P,'C',
  'False, as diag(1,z^−1,z):G_m→GL_3 shows. The surviving faithful representation is CL-SA02-503, and the affine inverse-limit theorem CL-SA02-504 uses a different faithfully-flat statement between finite-type quotient groups. Cancellation is preserved and no live conjecture is fabricated.',
  'Withdrawal on 90/14; refutation checked 2026-11-19','SGA3VIB1970;SGA3VIB2024')
C(509,509,90,[14,18,20,22,24],'un plus petit sous-module',
  'Under the stated finite locally free/projective coordinate-coalgebra hypotheses, an arbitrary quasi-coherent submodule F of an equivariant module E has a smallest equivariant quasi-coherent envelope inside E; the text claims flat-base-change compatibility.',
  'proof sketched through successive rewritten versions',V+'14: contraction by the projective coalgebra dual proves the algebraic envelope statement.','A',
  'Original SGA3 VIB 11.8 treats a free coordinate module; revised 11.8 gives the projective-coalgebra extension and explicit base-change compatibility. Revised 11.10.1 warns that flatness alone does not suffice and gives Gabber/Serre counterexamples. These exact scope differences are retained.',
  'Original SGA3 I 1970; projective extension identified in revised editorial text, 2024 version checked','SGA3VIB1970;SGA3VIB2024')
C(510,510,90,[14,18,20],'réunion filtrante',
  'Equivariant quasi-coherent modules are unions of finite-type equivariant submodules under the quasi-compactness and finite-coalgebra/local-projectivity hypotheses of each version.',
  'proof sketched; hypotheses revised and one version cancelled',V+'14 establishes the algebraic finite-envelope step; global hypotheses compared separately.','A',
  'SGA3 VIB 11.9–11.10 is the published relative local-finiteness discussion; the revised text separates projective from merely flat coalgebras and from noetherian-base finiteness. Different drafts are not amalgamated into an unconditional theorem.',
  'SGA3 I 1970; revised version 2024 checked','SGA3VIB1970;SGA3VIB2024','medium')
C(511,[506,510,511],90,[10,12,16,18], 'engendré par un … localement libre de type fini',
  'The finite-type version of the equivariant resolution assertion uses a finite coalgebra stage and the assumed availability of finite locally free ordinary covers; only the finite input is claimed here.',
  'proof sketched in the finite-type versions; reconstruction of a valid restricted formulation',V+'03 and V14 separate the finite construction from the false universal quantifier.','B',
  'Finite projective comodule covering is established under projective coordinate-coalgebra assumptions; revised SGA3 VIB 13.7 supplies a precise modern statement. No blanket resolution property for arbitrary flat group schemes or all quasi-coherent modules follows.',
  'Revised SGA3 VIB 2024 version checked','SGA3VIB2024')
C(512,510,90,[16],'tt O_X-G-module',
  'As transcribed, every equivariant quasi-coherent module is a quotient of a finite locally free equivariant module, although the hypothesis supplies such covers only for finite-type ordinary modules.',
  'false as stated; no finite-type qualifier in the conclusion',V+'03: trivial group over a point and ⊕_n k.','C',
  'False by an elementary dimension obstruction. The finite-type repair CL-SA02-511 is supported by the adjacent text and later projective-coalgebra results, but it is not inserted into the transcription.',
  'Refuted 2026-11-19; finite-type development in revised SGA3','SGA3VIB2024')
C(513,512,90,[20,22],'ils sont adjoints',
  'For the written relatively ample invertible sheaf and quasi-coherent category, graded sheafification is exact and left adjoint to the left-exact graded section functor; the counit is an isomorphism, so the section functor is fully faithful.',
  'proof sketched',
  'Adjunction checked by the canonical local degree-zero localization maps; exactness of sheafification is localization exactness. The graded section functor need not be exact.','E',
  'This is the section/sheafification formalism of ample invertible sheaves and Proj, already part of EGA II. A modern exact restatement is sought in the Stacks ample/Proj sections; the two functors and their different exactness assertions are kept separate.',
  'EGA II 1961; no date assigned to this manuscript sequence','StacksAmple;EGAII','medium')
C(514,513,90,[22,24],'d’où par minimalité lui est égal',
  'A smallest equivariant graded envelope, when it exists under the coalgebra hypotheses, sheafifies to the desired equivariant envelope; twists and the counit identify it with the original module envelope.',
  'proof sketched',
  'Conditional adjunction/minimality argument rechecked using CL-SA02-509 and CL-SA02-513; no existence under flatness alone asserted.','A',
  'The mechanism combines the published graded ample formalism with SGA3 VIB stable-envelope results. It is established with those hypotheses; no separate later theorem matching this precise draft was identified.',
  'EGA II 1961; SGA3 I 1970','EGAII;SGA3VIB1970;SGA3VIB2024','medium')
C(515,514,90,[24,25],'L est G-linéarisé',
  'A G-linearized relatively ample invertible sheaf permits transferring finite equivariant generation and covering statements between twists and graded sections, subject to the earlier base-resolution assumptions.',
  'proof sketched; remaining wording is a rewrite plan',
  'Checked that linearization is necessary to place all twists in the equivariant category; no unrestricted resolution property inferred.','C',
  'Published equivariant generation results occur in SGA3 VIB and later resolution-property literature. The exact global cover assumptions in this moving draft are not stabilized on the page, so only the conditional implication is retained as established.',
  'SGA3 I 1970 and revised VIB; exact draft dating unavailable','SGA3VIB2024','medium')
C(516,519,90,[7,9,13],'A^h',
  'The henselization is the filtered colimit of pointed étale neighbourhood algebras, with the local mapping universal property into henselian local algebras.',
  'construction and proof sketched',
  'Compared construction and universal property with EGA IV4 §§18.6,18.8; pointed residue-field choices distinguished for strict henselization.','A',
  'Published as EGA IV4 §18.6 (henselization) and §18.8 (strict henselization). Original indexed passages 18.6.6 and 18.8.12–16 were checked, with original volume metadata opened; full volume page delivery was blocked by size.',
  'EGA IV4 1967; manuscript undated','EGAIV4')
C(517,519,90,[7,9],'fidèlement plat; noethérien',
  'The local henselization map is faithfully flat, preserves the residue field, and is noetherian when the original local ring is noetherian.',
  'proof sketched',
  'Statement-level comparison to EGA IV4 henselization properties; no new proof of noetherian descent.','A',
  'EGA IV4 §§18.6–18.8 supplies these properties with the local-ring hypotheses. Strict henselization uses the chosen separable residue extension instead of preserving the original residue field.',
  '1967','EGAIV4')
C(518,519,90,[7,9],'B fini sur A',
  'For a finite A-algebra over a local base, henselization decomposes along the finitely many closed-fibre points and is compatible with the corresponding finite-base-change decomposition.',
  'proof sketched',
  'Finite decomposition and local universal-property match checked against EGA IV4 18.6.6; finiteness retained.','A',
  'Exact finite-algebra henselization formalism appears in EGA IV4 18.6.6 and the surrounding semilocal discussion. It is not an arbitrary base-change claim.',
  '1967','EGAIV4')
C(519,519,90,[9,11,13],'réduit; normal',
  'For a noetherian local ring A, reducedness and normality pass to its henselization (and the corresponding strict henselian variant under its stated hypotheses).',
  'proof sketched',
  'Compared original EGA IV4 indexed propositions 18.6.9 and 18.8.12; no formal-fibre excellence assumption silently added to the henselization theorem.','A',
  'EGA IV4 18.6.9 and 18.8.12 publish the reduced/normal statements. These differ from the completion statements, which require formal-fibre hypotheses.',
  '1967','EGAIV4')
C(520,519,90,[9,11,13],'fibres régulières de dimension 0',
  'The noetherian henselization/strict-henselization maps have geometrically regular zero-dimensional fibres; the written regularity, R_n, S_n and Cohen–Macaulay assertions use this flat local map.',
  'stated with proof sketch and references within the draft',
  'Property list compared to EGA IV4 18.8.12–13; completion not substituted for henselization.','A',
  'Published in EGA IV4 18.8.12–13 and surrounding propositions. Exact original indexed passages were read; the full original PDF could not be opened due to size, so this is indexed-primary-text verification, not image inspection.',
  '1967','EGAIV4')
C(521,519,90,[13],'Ass(A^h)',
  'Associated primes of the noetherian strict henselization lie over and detect the corresponding associated primes of A by contraction; the printed expression p∈A is a type error for a contraction.',
  'stated without a full proof; reading alarm in the formula',
  'Matched contraction formulation to EGA IV4 18.8.14; algebraic type of the displayed expression checked.','A',
  'EGA IV4 18.8.14 gives the associated-prime statement. The likely p∩A reading remains an unadjudicated ink question.',
  '1967','EGAIV4')
C(522,519,90,[11,13],'unibranche … irréductible',
  'For the standing noetherian henselian local ring, unibranchness is equivalent to irreducibility of its spectrum; equivalently a general noetherian local ring is unibranch when its henselization has the relevant irreducibility property.',
  'stated in a continuing local/henselian context',
  'Standing henselian hypothesis read on 90/13 and matched to EGA IV4 18.8.16; isolated-line generalization rejected.','A',
  'EGA IV4 18.8.16 is the published match. Dropping henselianity from the local assertion would change it and is not done here.',
  '1967','EGAIV4')
C(523,519,90,[13],'géométriquement unibranche',
  'A noetherian local ring is geometrically unibranch precisely when its strict henselization has irreducible spectrum.',
  'stated without full proof in the list',
  'Exact statement compared to original indexed EGA IV4 18.8.15.','A',
  'EGA IV4 18.8.15 publishes this criterion; reducedness versus integral-domain wording is retained as a separate distinction when nilpotents are present.',
  '1967','EGAIV4')
C(524,520,90,[11,13],'fibres formelles … normales',
  'The completion comparisons of normality/integrality/unibranchness are conditional on the formal-fibre hypotheses written in the draft, unlike the unconditional noetherian henselization properties.',
  'proof sketched; hypothesis wording unstable',
  'Compared with EGA IV4 formal-fibre and henselization results; no claim that universally catenary means separable formal fibres.','C',
  'EGA supplies precise formal-fibre criteria, but the draft bundles several hypotheses and uses a mathematically incorrect parenthetical equivalence. The separable/reduced formal-fibre version of the connectedness result is isolated in CL-SA02-532; ambiguous normal/integral variants require scan-level recovery before an exact theorem can be assigned.',
  'EGA IV4 1967; exact ambiguous draft formulation unresolved','EGAIV4','medium')
C(525,516,90,[3,4],'schéma profini; fini',
  'The finite/profinite limit argument uses finite-type fibres and a henselian base to descend a finite collection of clopen data; it does not assert that every profinite scheme is finite.',
  'proof sketched in the connectedness argument',
  'Finite-presentation descent matched to EGA IV3 limits and Stacks 01ZC/01ZM; the finite-stage quantifier is retained.','A',
  'The relevant finite-presentation limit theorem is EGA IV3 §8, with exact modern statements Stacks 01ZC and 01ZM. An infinite profinite set remains an immediate obstruction to the unqualified paraphrase.',
  'EGA IV3 1966; Stacks current text checked 2026-11-19','EGAIV3;Stacks01ZC;Stacks01ZM','medium')
C(526,516,90,[3,4],'limite … artiniens',
  'The connectedness proof passes through the inverse system of Artinian thickenings of a noetherian local base and its completion, with the properness/finite-type assumptions of that argument.',
  'proof sketched',
  'Checked that completion and nilpotent thickenings preserve the underlying closed fibre; algebraization is a separate properness input.','A',
  'This is the formal-functions/proper connectedness mechanism used in EGA; EGA IV4 §18.9 contains the resulting étale and connectedness comparisons. It is not a claim that arbitrary schemes are recovered from thickenings without properness.',
  'EGA III/IV 1961–1967','EGAIV4','medium')
C(527,516,90,[3,4],'composantes connexes',
  'For the proper object over the henselian local base in this argument, passage to completion and to the closed fibre detects connected components under the written hypotheses.',
  'proof sketched',
  'Matched connected-component use to EGA IV4 §18.9; exact properness and henselian assumptions carried.','A',
  'Published henselian proper-base comparison in EGA IV4 §18.9; the completion step cannot be imported into an arbitrary nonproper morphism.',
  '1967','EGAIV4','medium')
C(528,517,90,[3,5],'pleinement fidèle',
  'Under the connected formal-fibre and finiteness hypotheses of the local-base comparison, restriction of the relevant étale objects is fully faithful; the draft explicitly moves from separated étale objects to all étale objects.',
  'proof sketched; strongest endpoint stated without a complete written proof',
  'Original indexed EGA IV4 18.9.5 p.151 and 18.9.10 p.156 opened through search; hypotheses compared, not just the phrase fully faithful.','A',
  'EGA IV4 18.9.5 is the published full-faithfulness theorem, and 18.9.10 states the weakening to geometrically connected formal fibres. It includes the extension from separated to all étale objects. The draft’s local hypotheses must remain attached.',
  '1967','EGAIV4','medium')
C(529,516,90,[3,4],'X−x connexe',
  'The punctured-spectrum/closed-fibre connectedness step is a lemma inside the proper henselian formal-fibre argument, not an unconditional connectedness theorem for every punctured local scheme.',
  'proof sketched with an invocation to detail',
  'Compared its place in the proof to the published EGA IV4 18.9 sequence; no independent proof claimed for an unread implicit lemma.','A',
  'Its established setting is the EGA IV4 connectedness comparison. A standalone endpoint with omitted depth, irreducibility or formal-fibre assumptions is not asserted.',
  '1967','EGAIV4','medium')
C(530,516,90,[5],'f^−1(x) géométriquement connexe',
  'The connectedness theorem concerns the written proper/flat finite-type family over a local base and uses geometric connectedness of the relevant fibre and formal fibres to control neighbouring fibres.',
  'stated with a sketch and a reference to future rédaction',
  'Hypothesis-by-hypothesis comparison with EGA IV4 18.9.7–10; the draft parenthesis is not treated as a definition.','A',
  'EGA IV4 §18.9 gives the completed local connectedness theorem. The original indexed 18.9.9 says universally Japanese and geometrically reduced formal fibres; universally catenary is not a synonym.',
  '1967','EGAIV4','medium')
C(531,516,90,[5],'toutes les fibres … connexes',
  'For the specified henselian local setting, geometric connectedness detected on the closed fibre propagates through the connectedness comparison under the stated proper/flat and formal-fibre conditions.',
  'stated without a separate full proof',
  'Compared to EGA IV4 18.9.7 and surrounding hypotheses; retained as a scoped corollary, not a statement for arbitrary morphisms.','A',
  'Published local connectedness results cover the proper henselian formulation; no stronger nonproper statement is inferred from the abbreviated page.',
  '1967','EGAIV4','medium')
C(532,516,90,[5],'universellement caténaire (i.e. fibres formelles séparables)',
  'The parenthetical identifies universal catenarity with separability of formal fibres; the intended application is geometric connectedness of formal fibres under a stronger finiteness/separability condition.',
  'false equivalence in the wording; application proof sketched',
  'Original EGA IV4 18.9.9 p.156 explicitly uses universally Japanese, not universally catenary. No ink correction made.','C',
  'The published theorem EGA IV4 18.9.9 supplies the corrected universally-Japanese/formally-geometrically-reduced formulation; 18.9.10 isolates geometrically connected formal fibres. The transcription is flagged, not silently emended.',
  '1967; wording alarm recorded 2026-11-19','EGAIV4')
C(533,518,90,[5],'caractéristique 0',
  'The crossed-out characteristic-zero criterion was an attempted strengthening within the formal-fibre connectedness discussion.',
  'corrected by himself later/on the same sheet: cancelled',
  'Textual cancellation checked; no independent proof of the cancelled incomplete hypothesis package.','F',
  'The exact cancelled formulation is not recoverable with sufficient precision to identify a theorem. EGA IV4 18.9.9–10 gives surviving precise hypotheses, but characteristic zero alone is not substituted for them. Searches recorded under the formal-fibre family.',
  'Cancellation undated; EGA IV4 1967','EGAIV4','low')
C(534,522,91,[5,6],'monomorphisme',
  'For a locally finite-type scheme over a locally noetherian base, the functor criterion characterizes separated unramified representability/monomorphism through the listed finite-limit, infinitesimal and local conditions; conditions are not collapsed to pointwise injectivity.',
  'theorem stated; proof program and a stronger version proposed',
  'Matched the individual condition list to Murre Theorem 1, pp.243–246; no new proof of the full representability theorem.','A',
  'Murre reports Grothendieck’s unramified-functor representability theorem with conditions F1–F8. The exact locally-noetherian and separated hypotheses are retained. Murre is the checked exposition of the result, not proof that every proposed weakening was established.',
  'Murre talk May 1965; publication 1966; manuscript date unspecified','Murre1966','medium')
C(535,524,91,[7],'7) en renforçant',
  'The draft proposes replacing one representability axiom by a stronger condition to extend the theorem, and introduces essential freeness as a sufficient module condition.',
  'open on the pages; a proposed stronger criterion',
  'Compared only the completed axiom system in Murre and essential-free uses in SGA3 VIII/XI; no proof of the proposed replacement supplied.','C',
  'Murre Theorem 1 establishes the full standard criterion. SGA3 VIII 6.4 and XI 6.1 use essential freeness for closed representability. They do not by themselves establish that this isolated replacement axiom suffices in all contexts of the draft.',
  'Murre 1965/1966; SGA3 publication 1970','Murre1966;SGA3VIII2011;SGA3XI2011','medium')
C(536,525,91,[7],'condition (L)',
  'The written condition (L) is an adic/local lifting or representability condition with modified quantifiers in the margin; its exact strength must be matched to the stated test algebras.',
  'stated; wording revised',
  'Compared to Murre F3, the adic condition used in flattening, without identifying differently quantified clauses.','C',
  'Murre §3(A), Theorem 2, gives an exact adic criterion for flattening representability. The draft’s altered condition (L) is retained as its own formulation until the marginal attachment is checked.',
  'Murre 1965/1966','Murre1966','medium')
C(537,526,91,[8,9],'U=G_T',
  'Condition (R) excludes a proper open subgroup after the specified local base change when it contains the entire closed fibre; the equivalent tests in the draft use complete/noetherian local probes and finite-type hypotheses.',
  'definition and equivalences sketched',V+'03 supplies a fully checked failure example; equivalence of all listed test categories is not claimed independently.','C',
  'Later SGA3 representability results use related purity/essential-freeness or schematic-density hypotheses. No exact universal identification of this condition (R) with a modern named condition was found. In particular SGA3’s root-datum condition (R) is a different use of the letter and was excluded.',
  'Manuscript undated; SGA3 1970; Raynaud purity 1972','SGA3XI2011;Raynaud1972','medium')
C(538,[527,545],91,[8,9],'exemples',
  'The listed positive examples of (R) are intended to cover finite, proper/connected and fibrewise-controlled groups; the disappearing-component flat finitely presented group violates (R).',
  'examples asserted with abbreviated justifications',V+'03 verifies the negative example; each positive example retained only with its written hypotheses.','C',
  'Finite/proper cases are consistent with closedness and purity; SGA3 XI 6.1–6.8 proves representability under precise schematic-density or smooth connected-fibre hypotheses. The arbitrary flat-group extension is false, as R×K shows.',
  'SGA3 1970; Raynaud 1972; negative example checked 2026-11-19','SGA3XI2011;Raynaud1972','medium')
C(539,528,91,[9,10],'lieu où … égaux',
  'For a group satisfying the written rigidity condition, the equality subfunctor of two actions/morphisms is claimed to be represented by a closed subscheme under the separated/finite-type hypotheses.',
  'proof sketched through representability criterion',
  'Compared exact completed special cases in SGA3 XI 6.1 and 6.8, not equated to all groups satisfying the draft’s (R).','C',
  'SGA3 XI 6.1 proves the closed vanishing/equality functor for finite flat torsion kernels forming a schematically dense family; 6.8 treats a smooth source with geometrically connected nonempty fibres. These are established precise cases. The full draft condition-(R) formulation remains without an exact checked identification.',
  'SGA3 III publication 1970; revised text checked','Murre1966;SGA3XI2011','medium')
C(540,528,91,[9,10],'centralisateurs',
  'Centralizers of the indicated group action are closed-representable under the draft’s finite-type, separatedness and rigidity assumptions.',
  'stated with proof sketch',
  'Matched centralizer as an equality functor and opened SGA3 XI 5.3, 6.2 and 6.5.','C',
  'SGA3 XI establishes closed centralizers for multiplicative-type and torsion-dense groups under its exact hypotheses, with smoothness under additional hypotheses. Those are stronger specified cases, not a validation of every proposed condition-(R) generalization.',
  '1970; revised edition 2011 text checked','SGA3XI2011;Murre1966','medium')
C(541,529,91,[10,11],'transporteurs',
  'The transporter subfunctor is closed-representable under the indicated rigidity and finiteness hypotheses, with analogous variants proposed.',
  'proof sketched; variants proposed',
  'Opened and matched SGA3 XI Theorem 6.2 and §6.4; retained finite-presentation of the subgroup immersion in the nonnoetherian variant.','C',
  'SGA3 XI 6.2 proves the transporter theorem for the specified commutative H with finite flat schematically dense torsion kernels; §6.4 allows a nonnoetherian base change when the subgroup immersion is finitely presented. This is a precise developed family, not the full raw condition-(R) claim.',
  'SGA3 III 1970; revised edition 2011','SGA3XI2011','medium')
C(542,530,91,[11],'sans hypothèse noethérienne',
  'The author asks for nonnoetherian variants of the equality/centralizer/transporter representability assertions by retaining suitable finiteness conditions.',
  'open on the pages',
  'Compared SGA3 XI §6.4 and EGA/Stacks finite-presentation descent; exact finite-presentation replacement identified.','C',
  'SGA3 XI §6.4 proves a nonnoetherian base-change version for the schematic-density setting, with finitely presented closed immersion and quasi-compactness for a single finite detecting stage. The full generality of the draft’s (R) condition was not located.',
  'SGA3 III 1970; current limit statements checked 2026-11-19','SGA3XI2011;Stacks01ZM','medium')
C(543,531,91,[11,12],'platification universelle',
  'For a finite-type morphism over a locally noetherian base and a coherent module, the flattening functor is representable precisely under the stated adic condition; properness is a sufficient case.',
  'theorem stated with reference to the general criterion',
  'Read Murre §3(A), Theorem 2 and Corollary 1, matching the flattening functor rather than a blowup construction.','A',
  'Murre pp.253–254 reports the exact Grothendieck universal-flattening theorem. Raynaud–Gruson later developed purity and flattening by blowups; Raynaud 1972 Chapter IV Theorem 1 is a checked account of blowup flattening, which changes the base and is not the same functor-representability statement.',
  'Murre talk 1965/publication 1966; Raynaud–Gruson 1971; Raynaud 1972','Murre1966;Raynaud1972;RaynaudGruson1971')

# Exact passage refinement after a second source comparison.
by_id={int(c['id'].rsplit('-',1)[1]):c for c in claims}
def U(n,**kw):
    if 'fate' in kw and 'present_status' not in kw:kw['present_status']='As of 2026-11-19: '+kw['fate']
    if 'scans' in kw:kw['lines']=loc(90,kw['scans'])
    by_id[n].update(kw)

U(516,scans=[25],his_statement='Hom.loc(hA,B) ≃ lim Hom.loc(A_lambda,B)',statement='For a local ring A, the filtered pointed étale-neighbourhood construction hA is henselian and gives a bijection Hom_loc(hA,B)≅Hom_loc(A,B) for henselian local B. If A is already henselian, A→hA is an isomorphism. The semilocal henselization is the product of the local henselizations.',computation='On 90/25, the local Hom inverse-limit formula and the proof that A→A_lambda is an isomorphism for henselian A were checked; semilocal construction distinguished from the cancelled hybrid property.')
U(517,scans=[23,25],statement='For a semilocal ring A with radical r, hA is faithfully flat and semilocal, has the same residue product A/r, and has the same r-adic completion. If A is noetherian, hA is noetherian. For local A, A/m^n→hA/(m hA)^n is an isomorphism for every n≥1.',computation='90/25 proves the associated-graded quotients by flatness and the unchanged residue field, then inducts on n; this finite-filtration argument was independently checked. Noetherianity is cited on 90/23.')
U(518,scans=[17,23],statement='For A semilocal and B semilocal integral over A, B⊗_A hA≅hB. For strict henselization, finite B/A gives the local-factor decomposition after a chosen separable closure of the residue field; 90/17 extends that proof to integral semilocal B whose residue extensions have finite separable degree.',computation='The paired local universal-property maps w,w′ on 90/17 were read: both composites are identities by the same fixed residue embedding. The integral semilocal hypotheses on 90/23 are stronger than arbitrary base change but weaker than finite B/A.',fate='EGA IV4 18.6.8 and 18.8.10 publish the integral/finite semilocal compatibility. The separate ordinary and strict constructions and the finite separable residue-degree qualification are retained.')
U(519,scans=[17,21,23],statement='For any semilocal ring A, hA is reduced (respectively normal) if and only if A is; the corresponding strict henselization statement also holds. Noetherianity is added only for the subsequent fibre-finiteness assertion.',computation='Faithfully-flat descent proves necessity. The sufficiency proof on 90/21 uses filtered étale local algebras and stability of reducedness/normality; transitions and components must be read with the appropriate domain hypothesis.')
U(520,scans=[13,17,19,21],statement='For noetherian semilocal A, every fibre of hA/A and hsA/A is a finite product of separable algebraic field extensions. Consequently, for local noetherian A, Cohen–Macaulayness, S_n, regularity and R_n hold for A if and only if they hold for its ordinary or strict henselization.',computation='The fibre statement and the four equivalences are written on 90/13,17,19,21; noetherianity is retained. Exact formula for flat local transfer matched to EGA IV4 18.6.9–10 and 18.8.12–13.')
U(521,scans=[13,19],statement='For noetherian semilocal A and p in Spec(hA) or Spec(hsA), p is associated if and only if p∩A is associated to A. The strict-henselian witness on 90/13 prints p∈A, while the ordinary witness 90/19 supplies the correctly typed contraction.')
U(522,scans=[11,19],statement='For any local ring A, unibranchness (respectively reduced unibranchness) is equivalent to irreducibility (respectively integrality) of Spec(hA), and to the analogous condition for every strictly essentially étale local A-algebra with unchanged residue field. For henselian local A this is equivalent to irreducibility of Spec(A).')
U(523,scans=[13],statement='For any local ring A, geometric unibranchness (respectively reduced geometric unibranchness) is equivalent to irreducibility (respectively integrality) of Spec(hsA), and to the analogous condition for every essentially étale local A-algebra. A chosen separable residue closure defines hsA.')
U(524,scans=[11],his_statement='fibres formelles … géométriquement intègres',statement='If A is a henselian noetherian local ring with geometrically normal formal fibres, all its formal fibres are geometrically integral. If A is also integral, its completion is integral, and Frac(A) is algebraically closed in Frac(Â), with separable extension.',status_on_pages='proof sketched with the integral completion corollary and fraction-field consequence',**{'class':'A'},computation='The reduction to integral finite A-algebras, completion integrality and the geometrically integral generic-fibre implication were read separately on 90/11; no universal-catenarity equivalence is needed for this theorem.',fate='EGA IV4 18.9.1–3 publishes precisely this three-part sequence. These are completion statements under geometrically normal formal fibres, distinct from the noetherian henselization properties.',present_status='As of 2026-11-19: established under the stated geometrically normal formal-fibre hypothesis.',confidence='high')
U(525,scans=[19,21],items=['SA02-520'],his_statement='Si Y=lim Y_alpha est noethérien, Y est fini et discret',statement='An inverse limit of finite discrete topological spaces which is noetherian is finite and discrete.',computation='Independent proof: the inverse limit is compact Hausdorff; every subset of a noetherian space is quasi-compact, hence closed in this Hausdorff space. Thus the space is discrete, and compactness makes it finite.',fate='This elementary profinite/noetherian lemma is published as EGA IV4 18.6.9.2. It has no finite-type or properness hypothesis on a family of schemes.',refs=['EGAIV4'],present_status='As of 2026-11-19: established and independently reproved here.',confidence='high')
U(526,scans=[21],items=['SA02-520'],his_statement='B=lim B_alpha … noethérien, alors B est artinien',statement='A filtered colimit B of Artinian rings is Artinian if B is noetherian. If all transition maps are injective, the number of local factors eventually stabilizes, and the filtered limits of those factors are the local factors of B.',computation='Independent proof: every prime chain in B contracts to equal primes at all Artinian stages, so dim(B)=0; noetherian dimension zero implies Artinian. Injectivity preserves nonzero factor idempotents; the finite limit spectrum separates its points at finitely many stages, forcing eventual stabilization.',fate='Exact published match EGA IV4 18.6.9.1. Injectivity is required for the factor-stabilization conclusion, not for the first Artinian conclusion; flat transitions are not an extra hypothesis in the text.',refs=['EGAIV4'],present_status='As of 2026-11-19: established; two conclusions and their distinct hypotheses checked.',confidence='high')
U(527,scans=[9],his_statement='U ↦ g^-1(U) … bijection',statement='Let A be henselian noetherian local with geometrically normal formal fibres, A′=Â, X any A-scheme, X′=X⊗A A′. Pullback bijects clopen subsets of X and X′. If X is locally connected, π0(X′)→π0(X) is bijective.',computation='Independent check of the written proof: completion is faithfully flat and quasi-compact; its geometrically connected fibres make each clopen subset of X′ saturated, and quotient topology descends it. Local connectedness then identifies components with clopens.',fate='EGA IV4 18.9.4 publishes this arbitrary-X statement; 18.9.10 weakens formal geometric normality to geometric connectedness. No properness or finite-type assumption on X is part of the displayed result.',present_status='As of 2026-11-19: established with the stated formal-fibre hypotheses; no properness restriction added.',confidence='high')
U(528,scans=[7,9,15],statement='Under the hypotheses of CL-SA02-527, base change X′=X⊗AÂ induces a fully faithful functor from all étale X-schemes to all étale X′-schemes. Separatedness is first used for the target in a proof and then removed by descent of the open graph.',computation='Read the graph argument on 90/7 and its continuation on 90/15; fpqc descent of the open saturated graph and of its projection isomorphism proves full faithfulness. No essential-surjectivity assertion survives the cancelled fragment.',confidence='high')
U(529,scans=[3],his_statement='prof B=prof A+prof(B⊗A k)',statement='For the flat local map of noetherian local rings in the connectedness theorem, depth(B)=depth(A)+depth(B⊗A k). If A is an integral one-dimensional local ring and the fibre is reduced, depth(B)≥2 unless the fibre is zero-dimensional; if A is normal of dimension≥2, depth(B)≥2. After the Japanese normalization reduction, the exceptional case A DVR and closed fibre a field makes B a DVR.',computation='The depth formula and reduced-fibre depth-zero alternative were independently checked. In the final case the maximal ideal of B is generated by the DVR parameter, which is a non-zero-divisor by flatness, so B is regular local of dimension one. The invoked punctured-spectrum connectedness theorem is checked as a reference, not reproved.',fate='This is the proof mechanism of EGA IV4 18.9.7–11, using Hartshorne connectedness and normalization. Missing comparison signs and the 19.9.7/18.9.7 numeral remain reading alarms.',confidence='high')
U(530,scans=[5],his_statement='Théorème 18.9.7',statement='Let A→B be a local homomorphism of noetherian local rings, flat with geometrically reduced fibres. Assume A geometrically unibranch, or A unibranch and κ(B)/κ(A) primary. Then the generic fibre of Spec(B)→Spec(A) is connected, and Spec(B)−T is connected for every closed T lying above a proper closed subset of Spec(A).',computation='Exact hypotheses transcribed from 90/5 and compared to EGA IV4 18.9.7. This is a local-ring theorem: no properness or finite-type condition is inserted.',fate='Published as EGA IV4 18.9.7, with corollaries 18.9.8–11. The manuscript’s séparables fibres are read in the contemporary geometrically-reduced sense, not as an étale hypothesis.',confidence='high')
U(531,scans=[5],his_statement='Corollaire 18.9.8',statement='Let A→B be a flat local homomorphism of noetherian local rings with geometrically reduced fibres. If A is strictly henselian, or A is henselian and κ(B)/κ(A) is primary, every fibre of Spec(B)→Spec(A) is geometrically connected.',computation='Read finite local base-change reduction to the integral-base generic-fibre theorem; no properness or finite-type hypothesis added.',fate='Published as EGA IV4 18.9.8 under these exact local-ring hypotheses.',confidence='high')
U(533,scans=[9],his_statement='il est possible que si le corps résiduel … car. nulle … induit',statement='A cancelled remark suggests a characteristic-zero strengthening of the étale base-change functor, but ends after the word induit and supplies no conclusion.',computation='Textual incompleteness and cancellation checked at 90/9; neither equivalence nor essential surjectivity can be reconstructed from this fragment.',fate='Not identifiable as a mathematical claim with a conclusion. EGA IV4 18.9.6 is the relevant published location to compare, but no missing conclusion is invented from it.',confidence='high')
U(534,scans=[5,6],his_statement='Pour que produit_(X/S) Y/X soit représentable',statement='Let X→S be flat of finite type with S locally noetherian, and Y→X a finite-type monomorphism (the displayed closed-immersion case is secure). The subfunctor of base changes over which Y_T=X_T is representable iff it commutes with adic inverse limits of Artinian rings; for a closed immersion it is represented by a closed subscheme of S.',computation='Read the eight numbered checks, especially flatness under injective finite Artinian base extension and schematic density in check 7. Exact closed-immersion result matched to Murre §3(B) Theorem 3, p.255.',fate='Murre §3(B) Theorem 3 proves the closed-immersion formulation and proper-source sufficient case. The broader immersion/monomorphism variants on the page are not all identified with that theorem without checking their altered hypotheses.',refs=['Murre1966'],**{'class':'C'},confidence='high')
U(535,scans=[7],his_statement='7° sous la forme plus forte … propre; ess. libre',statement='For closed Y⊂X with X flat over S, equality after restriction to a schematically dense open U⊂T forces Y_T=X_T. The draft uses this stronger condition toward properness of the equality functor and obtains generic representability after making X essentially free over a dense open.',computation='Independent density check: flatness preserves schematic density, and a closed subscheme containing the dense open X_U must be all X_T. The generic essential-freeness input is cited as EGA IV §11, not proved on this page.',fate='Murre §3(B) Theorem 3 establishes the resulting closed representability with the adic condition; SGA3 VIII 6.4 supplies the essential-free closed-functor construction. The manuscript’s proof of this implication is valid under its schematic-density hypothesis.',status_on_pages='proof sketched; a valid stronger step, followed by a cancelled corollary',**{'class':'A'})
U(536,scans=[8],statement='Condition (L) says: for every local noetherian S-scheme T (a complete local ring with algebraically closed residue field is said to suffice), if Y_T contains the stated infinitesimal/open neighbourhood of the special fibre of X_T, then Y_T=X_T. The neighbourhood phrase is uncertain; the intended adic-limit equivalence is explicit.')
U(538,scans=[8,9],statement='The condition-(R) tests are asserted to hold if G has connected fibres, or if finite S-schemes G_i mapping to G have geometric-fibre translates G_(i,s)·G_s^0 covering G_s for every geometric s. The family need not be finite and its members were corrected from groups to schemes. The group R×K in V03 violates (R).')
U(540,scans=[9,10],statement='For u:H→G with H flat finite type satisfying (R) and G locally noetherian, the live statement represents Cent_G(u) as a subscheme of G; it is closed if G/S is separated. The unconditional closed version on 91/9 is cancelled.',fate='SGA3 XI gives established centralizer results for multiplicative-type and torsion-dense sources with exact hypotheses. These support specified cases; the general manuscript condition-(R) theorem and its nonseparated version have not been located in exactly the same formulation.')
U(541,scans=[10],statement='For u:H→G as in CL-SA02-540 and a finite-type subgroup K⊂G, the inclusion transporter is representable and is a subscheme/closed subscheme when K is. If also K is flat satisfying (R) and u is an immersion, the equality transporter is finite type over G, with the corresponding immersion/closedness conclusion; the normalizer is the H=K case.')


# Original EGA IV4 obtained by root and actual text read in this run.
for n in range(516,534):
    if n in by_id:
        c=by_id[n]
        c['computation'] += ' Original EGA IV4 inspected locally in reference_cache/EGAIV4.txt, §§18.6 and 18.8–18.9 (printed pp.137–157); prior indexed-only access limitation resolved.'
        for key in ['fate','present_status']:
            c[key]=c[key].replace('Original indexed passages 18.6.6 and 18.8.12–16 were checked, with original volume metadata opened; full volume page delivery was blocked by size.','Original §§18.6 and 18.8–18.9 were read from the downloaded original PDF text; metadata and original Numdam URL were opened.').replace('Exact original indexed passages were read; the full original PDF could not be opened due to size, so this is indexed-primary-text verification, not image inspection.','Exact original printed pp.149–150 were read from the downloaded original PDF text.').replace('Original indexed EGA IV4','Original EGA IV4')

dump('claims.json',claims)
print(f'Stage2 serialized current claim records: {len(claims)}')
