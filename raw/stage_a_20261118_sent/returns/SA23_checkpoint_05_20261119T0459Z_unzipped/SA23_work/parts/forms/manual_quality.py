"""Manually assigned record categories and individual problem judgments.

The numeric assignments below were authored from the source readings and claim
assessments. No keyword or heading classifier is used. Run after all builders.
"""
from pathlib import Path
import json,datetime
BASE=Path(__file__).resolve().parents[1]
NAMES={'p':'proved there','s':'proof sketched','a':'stated without proof','c':'corrected by himself later','f':'false as stated','o':'open on the pages','r':'present-run refinement'}
MAPS={
 'forms':{
  1:'s',2:'f',3:'s',4:'f',5:'s',6:'s',7:'o',8:'s',9:'s',10:'c',11:'o',12:'c',13:'s',14:'c',15:'s',16:'s',17:'f',18:'s',19:'s',20:'f',21:'f',22:'c',23:'o',24:'o',25:'f',26:'c',27:'s',28:'o',29:'f',30:'s',31:'s',32:'f',33:'s',34:'a',35:'a',36:'c',37:'c',38:'o',39:'o',40:'a',41:'c',42:'o',43:'o',44:'o',45:'s',46:'s',47:'a',48:'o',49:'o',50:'a',51:'c',52:'o',53:'s',54:'o',55:'p',56:'p',57:'p',58:'o',59:'s',60:'s',61:'o',62:'s',63:'p',64:'o',65:'s',66:'f',67:'o',68:'a',69:'a',70:'o',71:'s',72:'s',73:'f',74:'o',80:'f',81:'s',82:'f',83:'s',84:'o',85:'o'
 },
 'spaces':{
  1:'s',2:'o',3:'p',4:'s',5:'o',6:'a',7:'p',8:'p',9:'s',10:'o',11:'o',12:'s',13:'o',14:'c',15:'o',16:'p',17:'a',18:'a',19:'p',20:'f',21:'o',22:'s',23:'p',24:'s',25:'o',26:'a',27:'o',28:'s',29:'s',30:'o',31:'a',32:'a',33:'o',34:'s',35:'o',36:'o',37:'a',38:'a',39:'s',40:'f',41:'s',42:'a',43:'o',44:'p',45:'s',46:'s',47:'a',48:'a',49:'o',50:'s',51:'a',52:'s',53:'o',54:'s',55:'o',56:'a',57:'s',58:'f',59:'a',60:'s',61:'o',62:'a',63:'a',64:'a',65:'a',66:'s',67:'a',68:'a',69:'a',70:'p',71:'o',72:'f',73:'p',74:'o',75:'o',76:'a',77:'s',78:'s',79:'o',80:'o',81:'o',82:'s',83:'p',84:'s'
 },
 'bt':{
  1:'o',2:'a',3:'s',4:'p',5:'c',6:'s',7:'s',8:'s',9:'p',10:'f',11:'a',12:'f',13:'o',14:'c',15:'a',16:'a',17:'a',18:'s',19:'o',20:'s',21:'o',22:'s',23:'f',24:'a',25:'f',26:'s',27:'r',28:'f',29:'a',30:'a',31:'s',32:'a',33:'p',34:'p',35:'p',36:'p',37:'s',38:'p',39:'a',40:'p',41:'p',42:'f',43:'p',44:'p',45:'p',46:'p',47:'a',48:'p',49:'p',50:'p',51:'p',52:'p',53:'a',54:'p',55:'o',56:'a',57:'o',58:'a',59:'a',60:'a',61:'o',62:'o',63:'o',64:'a',65:'a',66:'f',67:'a',68:'s',69:'o',70:'o',71:'o',72:'a',73:'a',74:'o',75:'p',76:'r',77:'o',78:'r',79:'c',80:'r',81:'r',82:'r',83:'a',84:'o',85:'r',86:'r',87:'a',88:'o',89:'a'
 }
}
WORTH={
 'forms':{
  1:'Commentary correction only: the degree-one case fixes the dual convention, while the Cartier and flatness qualifiers must be written before any divisor comparison.',
  2:'Scan and commentary work are worthwhile because the isolated-point counterexample isolates exactly the missing irreducibility clause; no new Bertini theorem is needed.',
  3:'Inspect the historical definitions first, since modern scheme terminology cannot determine the intended coherent-module property from these words alone.',
  4:'A bounded explanatory repair is worthwhile because the false generic-combination shortcut is replaced by a concrete incidence-dimension argument.',
  5:'Commentary only: the primary-field lemma has an exact checked modern proof, so the useful task is a hypothesis-matched insertion and historical reference.',
  6:'Commentary only: the finite component graph proves the claim once the finite-image exceptional family is stated correctly.',
  7:'A bounded formulation task is worthwhile because the product counterexample distinguishes intrinsic connectedness dimension from image-dimension connectedness.',
  8:'An editorial crosswalk to EGA IV3 is worthwhile because the missing list determines whether one gets constructibility or proper-flat openness.',
  9:'A broader formulation is worth attempting only after specifying image-dimension hypotheses; the proper connectedness theorem itself is already established.',
  10:'Commentary and scan clarification suffice: the parameter and finite-étale constructions are proved, while the unreadable integrality reservation changes the iteration.',
  11:'A targeted historical example search is worthwhile because the adjacent proper/projective contradiction is explicit but its intended counterexample is not supplied.',
  12:'Scan first: the surviving positive-dimensional-image statement already proves the useful codimension bound, and the unreadable threshold cannot be inferred uniquely.',
  13:'Scan first: the depth examples are understood but do not recover the missing five-line footnote or identify its intended variety.',
  14:'A bounded geometric rewrite is worthwhile because the principal-ideal calculation is clear while the global component clause is textually incomplete.',
  15:'Scan and comparison work are worthwhile because the depth obstruction is explicit but the omitted Z_n strata prevent a faithful iff theorem.',
  16:'A diagram commentary is worthwhile: the conormal theorem is known, and fixing duals and twists would make this manuscript proof checkable line by line.',
  17:'High-value correction work is worthwhile because characteristic-two parity changes the theorem and the later authorial correction can be aligned with Katz’s exact statement.',
  18:'A bounded scope analysis is worthwhile because the étale-isogeny example disproves the nonimmersion extension while preserving embedded reflexivity.',
  19:'Commentary only: Katz’s explicit Fermat example answers the request and the retracted terminology should be explained rather than redeveloped.',
  20:'Scan first, followed by a precise sufficient-condition comparison: the damaged indices and withdrawn converse do not support a new conjecture as written.',
  21:'A focused exceptional-locus comparison is worthwhile because Benoist and Poonen–Slavov require hypotheses that differ from the draft’s morphism generality.',
  22:'A bounded fixed-base analysis is worthwhile because a divisorial base component is a concrete obstruction and the quotient-image field controls the moving part.',
  23:'An editorial reconstruction is worthwhile only when labelled as such; the published ordinary-pencil theorem is available but the missing manuscript conclusion is not.',
  24:'Commentary only: the polynomial-ratio computation is explicit, and the useful work is retaining the quasi-finiteness and fixed-base restrictions.',
  25:'Scan first: a heading and illegible theorem do not identify a mathematical problem strong enough for further development.',
  26:'Scan and commentary only: the deleted-point example determines why a closure bar matters, without adjudicating whether it was in the ink.',
  27:'Commentary only for the regular rank-two blowup lemma; the cancelled higher-rank heading needs its original text before a stronger task can be posed.',
  28:'A bounded corrective note is worthwhile because the infinite projective-space cover disproves quasi-compactness and the determinant restores the Plücker target.',
  29:'A precise functorial formulation is worthwhile because flatness and the degree-one Hilbert polynomial are needed to turn the programme into a correct intrinsic criterion.',
  30:'Commentary only: the category-of-simplices and local-integral-coefficient Whitehead argument are known, but their naturality and π1 assumptions should be made explicit.',
  31:'Editorial reconciliation is worthwhile because the two marginal corrections distinguish derived limits from local-system cohomology and prevent a false coefficient definition.',
  32:'A bounded hypothesis task is worthwhile because local contractibility and derived Ext comparison must be specified before the proposed topos equivalence is meaningful.',
  33:'A short corrective comparison is worthwhile because the acyclic noncontractible example separates abelian tests from the missing nonabelian local-system information.',
  34:'A definitions task is worthwhile because strict multiple categories and strict globular categories have different nerve constraints even before weak morphisms are introduced.',
  35:'Commentary only: the superline self-commutor gives the exact obstruction, and the deleted strict-commutativity strengthening should stay deleted.',
  36:'A small model comparison is worthwhile because resolutions and globularity determine which RHom truncation the proposed higher-category statement can represent.',
  37:'Commentary only for the negative answer: the1963 A4-not-A5 example settles it, while a useful modern comparison must retain the full A-infinity structure and structured maps.',
  38:'A historical construction comparison is worthwhile because Quillen and Segal realize different parts of the programme and Schlichting shows why the exact input structure matters.',
  39:'A bounded axiomatic rewrite is worthwhile because the two bordism witnesses omit different product/Gysin compatibilities that affect the universal property.',
  40:'Commentary only after fixing the intended multiplicativity: the homotopy-ring and E-infinity versions already have different checked answers.',
  41:'A restricted naturality question is worth posing only after naming a class of maps; the unrestricted version is already excluded by RP²→point.',
  42:'Commentary only: duality and finite-free Kunneth give the correspondence calculation once compactness, shifts and idempotent completion are stated.',
  43:'Scan first and then a bounded normal-bundle test: the literal embedded-submanifold criterion fails on RP¹⊂RP², so an intended framing condition must be established.',
  44:'Commentary only: series composition determines the coproduct, and fixing the coaction convention resolves the remaining ambiguity.',
  45:'A formulation task may be worthwhile after S(X) is repaired, because the proposed realization category and its exact completion are currently not defined.',
  46:'A short normalization check suffices: the altered lower-degree binomial changes an error constant but does not threaten the positive leading-term argument.',
  47:'Historical commentary is worthwhile because Friedlander supplies the completed étale route while Quillen’s1971 proof is methodologically different.',
  48:'Commentary only: the checked later theorem already specifies the allowed primes and finite obstruction groups that the draft compresses.',
  49:'A targeted literature identification is worthwhile because the stronger representability conjecture is not equivalent to the fibration theorem used in the Adams proof.',
  50:'A bounded comparison of the original and Friedlander constructions is worthwhile because functorial rigidification, not the K_0 algebra, is the remaining historical gap.',
  51:'Scan and commentary only: the two exact sequences force the final dual and tensor factors, and the symbolic identity is already verified.',
  52:'A precise complete-Hopf-algebroid formulation is worthwhile because the one-object inverse construction does not by itself settle source/target balancing in the stated category.',
  53:'A bounded duality task is worthwhile because replacing finite projectivity by flatness changes the continuous dual and completion operations used in the construction.',
  54:'Scan and commentary only: the rank-three exterior-algebra counterexample proves the missing degree-one square-zero condition is essential.',
  55:'Commentary only once the hypothesis is repaired: the Jacobiator is exactly the degree-one square of the exterior derivation.',
  56:'A focused archival and primary-literature task is worthwhile because the exact flat-conormal quantifier attributed to Quillen has not been matched by the checked projective or derived theorems.',
  57:'A definitions task is worthwhile because the source itself asks for PD compatibility and leaves the positive-characteristic theorem as an empty heading.',
  58:'A bounded comparison is worthwhile after settling the integration category, since the standard Taylor theorem does not by itself prove the flat-conormal extension.',
  59:'Scan and commentary only: the graded sign and alternating arguments are fixed by the curvature calculation, while the opposite overall convention is harmless.',
  60:'Scan and commentary only: d+x dy gives a counterexample under all the strong smooth characteristic-zero hypotheses, isolating the missing integrability adjective.',
  61:'A focused comparison theorem is worth formulating only after the formal groupoid and module hypotheses are fixed; the current bare topos question is underdetermined.',
  62:'A short coefficient-detection note is worthwhile because the rational Moore-space example refutes the literal assertion and separates it from an integral Whitehead theorem.',
  63:'Commentary and scan work suffice: the chosen-basis chart is valid, while an arbitrary extension supplies only a retraction torsor without a canonical origin.',
  64:'Commentary only for the false general bound: the exact blowup counterexample and the later fiber-jump theorem are checked, so the useful task is a hypothesis-matched concordance.',
  65:'Scan and commentary work are worthwhile because the node argument proves the component bound once the damaged separability or dual-defect hypothesis is recovered.',
  66:'A bounded formulation task is worthwhile because the normal-case divisor test is clear but the adjective and normalization reduction prevent certification of the entire iff.',
  67:'Commentary only: the integer-poset filtered-colimit point proves non-fullness explicitly and separates topos functoriality from nerve full faithfulness.'
 },
 'spaces':{
  1:'Commentary only: the adjunction and sheafification give the missing inverse image, but the manuscript’s left/right adjoint labels must be kept consistent.',
  2:'A bounded correction is worthwhile because the product theorem is established while the proposed two-direct-image membership test has an explicit counterexample.',
  3:'Scan first: cancellation and the fragmentary diagram leave no precise pseudolimit theorem to develop without inventing hypotheses.',
  4:'A focused comparison is worthwhile because the space product and localic/topos product agree under specific compactness assumptions rather than universally.',
  5:'Commentary only for the proved refinement; a new task is justified only if its locally closed compact-point hypothesis is deliberately weakened.',
  6:'A bounded hypothesis audit is worthwhile because finite and infinite products use different covering and quasi-compactness arguments.',
  7:'A concrete locale example task is worthwhile because the blanket infinite-discrete claim is too broad and the countable and uncountable cases behave differently.',
  8:'A bounded counterexample-and-repair note is worthwhile because an inverse limit with essential transitions can fail to remain a presheaf topos.',
  9:'Commentary only: density and left Kan extension identify the correct preservation condition; the unfinished cocontinuity inference should not be repeated.',
  10:'Commentary only: the localization universal property answers the question under the exact colimit-preservation hypotheses.',
  11:'A short correction is worthwhile because cover-epimorphism preservation alone misses relations needed for descent, and the small counterexample identifies the gap.',
  12:'Commentary only: the neighborhood proof settles the preorder adjunction once the specialization-order convention is fixed.',
  13:'Commentary only: directed irreducible closed sets give the point description, and the order orientation must remain explicit.',
  14:'Commentary only: the minimal-element argument and descending-chain condition prove the stated classical-poset equivalence.',
  15:'A definitions note is worthwhile because localic presheaf topoi, sober spatial representatives and essential points are related but distinct conditions.',
  16:'A bounded correction is worthwhile because essential geometric morphisms give the proposed preorder correspondence, whereas arbitrary geometric morphisms do not.',
  17:'A focused frame calculation is worthwhile because finite-meet preservation is proved but arbitrary-join preservation depends on the intended tensor-product topology.',
  18:'Commentary only: Morita cancellation is established with the comparison datum, and removing that rigidification changes the uniqueness assertion.',
  19:'Scan first: the torsor/complex diagram does not identify a unique theorem or its coefficient and degree conventions.',
  20:'Commentary only: sober-space recovery follows from completely prime filters, while the source’s practical-scope caveats should be retained.',
  21:'Commentary only: the required axioms are the established Giraud characterization, not a new open existence theorem.',
  22:'A bounded scope note is worthwhile because geometric theories have classifying topoi but the parenthetical arbitrary-structure extension lacks that guarantee.',
  23:'A formulation task is worthwhile only after specifying the structure assignment and its change-of-topos compatibility; the source explicitly assumes existence.',
  24:'A short obstruction note is worthwhile because product closure rules out fields as an ordinary algebraic theory, and the pointwise ring-map condition is weaker.',
  25:'Scan and cancellation commentary only: the field-recognition example belongs to a withdrawn construction and does not supply a surviving general criterion.',
  26:'A precise reconstruction comparison is worthwhile because set-valued models alone do not determine the required pseudofunctorial structure without the stated compatibility data.',
  27:'Commentary only for dependent product: local cartesian closure gives the right adjoint, while the unfinished sums heading has no recoverable additional theorem.',
  28:'A technical editorial note suffices because fixed universes and small generating sites control the sheafification colimits; no new mathematics is proposed.',
  29:'Commentary only: the tensor-faithfulness proof settles sufficiency of the maximal-ideal fiber test for a flat module.',
  30:'A bounded distinction is worthwhile because topological descent of subsets and effective descent of locally closed subschemes require different hypotheses.',
  31:'A focused hypothesis check is worthwhile because formal lifting properties require the correct fpqc locality statement rather than an analogy with smoothness.',
  32:'Commentary only: the standard equalizer construction explains effective descent of quasi-coherent modules and clarifies the pedagogical request.',
  33:'A correction note is worthwhile because quasi-compact immersions descend in the checked theorem, while the unqualified arbitrary-immersion version is false.',
  34:'A focused example comparison is worthwhile because descending an already specified ample bundle differs from descending mere projectivity or effectivity of all schemes.',
  35:'Commentary only: the checked universal-homeomorphism criterion supplies the deferred converse with its integrality and surjectivity requirements.',
  36:'Commentary only: the diagonal/graph factorization proves the exercise once the class of morphisms is stable under composition and base change.',
  37:'Commentary only: the finite principal-open equalizer criterion is the standard Zariski sheaf condition on affines.',
  38:'Commentary only: prime contraction gives the closure formula directly, and the nilpotent-kernel condition gives the dominance criterion.',
  39:'A short illustrative example is worthwhile because tensor products of residue fields explain why point-set fiber products are not usually cartesian.',
  40:'Commentary only: the missing object is the ring coequalizer with the indicated two maps, once the diagram’s variance is made explicit.',
  41:'Commentary only: orthogonal idempotents prove the finite-product ring formula and expose any unjustified infinite-family extension.',
  42:'A bounded quotient comparison is worthwhile because affine colimits can collapse orbit information that a sheaf or geometric quotient retains.',
  43:'Commentary only: the finite localization equalizer proof supplies the omitted affine sheaf argument without changing the presheaf construction.'
 }
}
counts={}
for owner,mp in MAPS.items():
 p=BASE/owner;cs=json.loads((p/'claims.json').read_text());seen=set()
 for c in cs:
  n=int(c['id'].rsplit('-',1)[1]);seen.add(n)
  c['status_category']=NAMES[mp[n]]
  c['status_assignment']='Manually assigned from direct source reading and the retained detailed status; not keyword-classified. A false statement may be a transcription-dependent claim rather than an adjudication of the ink.'
  c['record_origin']='source assertion'
  if owner=='bt':
   if n in (27,76,78,80,81,85,86):c['record_origin']='earlier-run idea'
   elif n in (13,23,25,66,82):c['record_origin']='present-run reconstruction'
   c['source_author']='Jean-Pierre Serre (with Tate and other attributions retained in the text)' if 32<=n<=64 or n==89 else 'Alexander Grothendieck'
   if c['record_origin']!='source assertion':c['source_author']='Earlier Pro notes/current SA23 check, as distinguished in statement and status_on_pages'
  elif owner=='forms':
   c['source_author']='Daniel G. Quillen' if 55<=n<=63 else ('Alexander Grothendieck, in Piotr Blass’s English translation' if n<=33 or n in (81,82,83,84) else 'Alexander Grothendieck’s notes, with Quillen/Artin–Mazur and other attributions retained')
  else:c['source_author']='Alexander Grothendieck'
 assert seen==set(mp),(owner,seen^set(mp))
 (p/'claims.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n')
 (p/'manual_status_categories.json').write_text(json.dumps({c['id']:{'status_category':c['status_category'],'record_origin':c['record_origin'],'source_author':c['source_author']} for c in cs},ensure_ascii=False,indent=2)+'\n')
 counts[owner]={'claims':len(cs)}
 if owner in WORTH:
  ps=json.loads((p/'problems.json').read_text());seen=set()
  for q in ps:
   n=int(q['id'].rsplit('-',1)[1]);seen.add(n);q['worth']=WORTH[owner][n]
  # The final provenance audit may already have moved reader tasks out of MPs.
  assert seen<=set(WORTH[owner]),(owner,seen-set(WORTH[owner]))
  (p/'problems.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
  counts[owner]['individual_problem_judgments']=len(ps)
 with (p/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' Manual status/origin categories saved; detailed source status preserved.\n')
import runpy
for owner in ['bt','spaces']:
 runpy.run_path(str(BASE.parent/'integration/apply_bt_spaces_problem_origins.py'))['apply_owner'](owner)
print(json.dumps(counts,ensure_ascii=False))
