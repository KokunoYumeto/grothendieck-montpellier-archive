import json,csv,re
from pathlib import Path
from build_claims import claims,items,F
P=Path(__file__).parent
def tsv(name,header,rows):
 with (P/name).open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
# Manual mathematical alarms; no proposed change is applied to a transcription.
rows=[
('161-3',4,'3a:19','Hom(φ(x),y)','Hom(y,φ(x))','Representable functors testing a limit are covariant in φ; scan 6 uses the latter direction.','high'),
('161-3',6,'3a:153','adjoint à droite v*','adjoint à gauche','v* is the left adjoint of v_*.','high'),
('161-3',6,'3a:153','C→F','C^op→F','Objects are presheaves in the stated variable.','high'),
('161-3',10,'3a:366','O(X)×O(Y) injects into O(X×Y)','basis functor with empty rectangles identified','All (∅,V) and (U,∅) map to the same empty open.','high'),
('161-3',10,'3a:366-372','Top(X×Y) for separate-cover topology','product topos until π′ is introduced','The later comparison distinguishes those topologies.','high'),
('161-3',13,'3a:519','sup W','sup V_λ','The family being joined is indexed by λ.','medium'),
('161-3',13,'3a:522,542','z∈W; W×tail','z∈U; U×tail where used','The subsequent neighborhood argument has this type.','medium'),
('161-3',15,'3a:567','fix i∈I−J(z), J(z) finite','fix i∈J(z)','Product basic opens restrict finitely many coordinates; the written set is generally not open.','high'),
('161-3',20,'3a:831','β codomain Hom(C,E)','Hom(Sh(C),E)','β is extension, not restriction.','high'),
('161-3',24,'3b:83','O_x contains y iff y≥x','y≤x','The definition immediately preceding is O_x={y:y≤x}.','high'),
('161-3',24,'3b:155','présobre','T0 in modern terminology','The stated condition is injectivity of x↦closure{x}; do not replace historical terminology silently.','medium'),
('161-3',26,'3b:169-177','cofiltered criterion without nonemptiness','nonempty and downward directed','The empty space satisfies the pairwise condition vacuously but is not irreducible.','high'),
('161-3',27,'3b:218-225','each point of X essential','each point of sob(X), if this is δ','Context compares the sobrification; the symbol affects the equivalence.','high'),
('161-3',27,'3b:247-256','all morphisms in preorder 2-equivalence','essential geometric morphisms','A nonprincipal point of the Alexandrov poset Z is a counterexample for all geometric morphisms.','high'),
('161-3',29,'3b:326-332','3+6cos3θ in cancelled norm','3+6cosθ for the displayed common inner products','Gram matrix computation yields 3+6t. Entire passage remains cancelled.','high'),
('161-3',29,'3b:381','α(X′×Y)','γ(X′×Y)','α is defined on O(X), whereas the rectangle belongs to O(X×Y).','high'),
('161-3',31,'3b:447','automorphism of F local inner','algebra automorphism of End(F)','The Skolem–Noether argument concerns the endomorphism algebra.','high'),
('161-3',32,'3b:460-527','dk−|+kd','dh+hd for cochain degree −1 homotopy','The degree convention is not specified, so the sign cannot be adjudicated from algebra alone.','high'),
('161-3',33,'3b:593-601','unique up to unique isomorphism','unique with G⊗E≅F compatibility','Scalar automorphisms survive if the compatibility is forgotten; positive rank also matters.','high'),
('161-3',35,'3b:614','Γ(F)=Hom(F,constant 1)','Hom(1,F)','Hom(F,1) is always a singleton; global sections need not be.','high'),
('161-3',35,'3b:673','displayed sobrification adjunction','Hom(sob X,Z)=Hom(X,Z) for sober Z','The left-adjoint direction fixes domains.','high'),
('161-3',39,'3b:880','neighborhoods of y contain x','neighborhoods of x contain y','x∈closure{y} gives the latter and the map F_x→F_y.','high'),
('161-3',39,'3b:885','x≤y convention','track local convention; opposite to scan 24','No global standardization across sheets is licensed.','high'),
('161-3',40,'3b:959','u bijective','underlying spectral map bijective, residue fields unchanged','Ring map can be a nontrivial nilpotent thickening.','high'),
('161-3',42,'3c:49','bijective iff C field, cancelled','commutative von Neumann regular C','F2×F3 passes. This may be author error in a discarded argument rather than transcription error.','high'),
('161-3',43,'3c:88','every preorder space embeds in Sierpiński power','every T0 space, or T0 quotient','The target is T0 and cannot contain indistinguishable distinct points as a subspace.','high'),
('161-3',51,'3c:276','ε∈Γ(G/H) in B_G','section of underlying object in E','eH is generally not G-fixed.','high'),
('161-3',52,'3c:311','fiber over (X,e)','fiber over (Z,e)','X=G/H while the sheaf base is Z.','high'),
('161-3',53,'3c:332','limit over C/F for Hom(R,F)','category of elements C/R','The indexing object for restriction to a sieve is R.','high'),
('161-3',53,'3c:332,340','missing product in Čech equalizer term','products over covering members and overlaps','All parallel overlap restrictions must be present.','high'),
('161-3',54,'3c:355','finer than canonical among corrections','subcanonical, hence no finer than canonical','Fully faithful representables force the stated direction.','high'),
('161-3',55,'3c:373','sheaf (separated) iff injective (bijective)','bijective (injective)','The two conditions are reversed in the parenthetical order.','high'),
('161-4',3,'4a:22','fiber criterion for M without flatness','for flat M','Z⊕Z/2 has every fiber nonzero but is not flat.','high'),
('161-4',3,'4a:36','suffices M′⊗B=0','≠0','The goal is nonvanishing for a nonzero cyclic submodule.','high'),
('161-4',3,'4a:42','points maximaux','generic under generization convention','Flat maps do not generally preserve closed points; terminology must be checked.','high'),
('161-4',4,'4a:84','K=ker u after base change','ker(A′→C′)','The second kernel belongs to the base-changed ring.','medium'),
('161-4',5,'4a:127','f quasi-compact iff f′','g quasi-compact iff g′ in this diagram','f names the covering base change in the same sentence.','high'),
('161-4',6,'4a:246','arbitrary immersion descends fpqc','quasi-compact immersion, or fppf cover','Explicit infinite-prime counterexample; ink must decide authorial qualification.','high'),
('161-4',7,'4a:282','L on both sides of base-change equivalence','L′ on the pulled-back side','The base-change diagram fixes the two schemes.','medium'),
('161-4',7,'4a:294','only failures projective/quasi-projective','examples, not exhaustive classification','Arbitrary immersions provide another failure.','high'),
('161-4',9,'4a:373','closed + quasi-projective implies projective','universally closed, or proper','A1 over a field is a counterexample for merely closed.','high'),
('161-4',10,'4a:407','L^n0 very ample for n≥n0','L^n','The quantified n does not appear in the written bundle power.','medium'),
('161-4',10,'4a:432','⇒ or ⇏','retain the uncertain sign','The composition theorem depends on the exact quasi-compact hypotheses.','high'),
('161-4',11,'4a:507','gf finite type ⇒f quasi-separated','f finite type in the parenthesis','The standard cancellation result pairs quasi-compact and finite type.','medium'),
('161-4',15,'4a:696-698','Γ(U_f,O_X), U_f possibly on Y','Γ(φ⁻¹D(f),O_X)','The localization map must land on an open of X.','medium'),
('161-4',17,'4a:774','to be a sheaf iff sheaf and affine open cover','to be representable by a scheme','The stated condition is the preceding representability criterion.','high'),
('161-4',18,'4b:14','Hom_top(E,A)','Hom_top(E,PSh(A))','A is a small finite-limit category, not the target topos.','high'),
('161-4',18,'4b:70-79','p_* and q_* membership criterion','pullback-subtopos/sheaf conditions, not direct-image tests','Arrow-category square counterexample is in compute_checks.','high'),
('161-4',20,'4b:141','k[I] for function algebra','k^I; preserve historical bracket notation','Modern group algebra notation would reverse the intended Hopf construction.','medium'),
('161-4',22,'4b:220','Spec ∏_I A_i=⊔ Spec A_i','finite I from context','Infinite products have nonprincipal ultrafilter points.','high'),
('161-4',24,'4b:346','algebras over A','algebras over k','A is a variable coordinate algebra; k is the base.','medium'),
('161-4',29,'4b:563-568','idempotent formula for arbitrary I','finite I as preceding context','Infinite sums of idempotents are not algebraic ring operations.','high'),
('161-4',30,'4b:620','prime ideals containing A','containing J_S','A itself is not contained in a prime ideal of a unital ring.','high'),
('161-4',31,'4b:702','f_i∈I','f_i∈A','I is the indexing set, A the ring.','medium'),
('161-4',32,'4b:750','A_f→A_g','A_g→A_f under f≺g','The open inclusion reverses ring maps.','high'),
]
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],[list(r)+['high' if r[-1]=='high' else 'medium'] for r in rows])
# Historical task inventory. The final manual provenance overlay below separates
# actual source questions from reader-generated checks without changing claims.
pg=[(2,'Missing inverse image of a product morphism'),(1,'Product universal property and incomplete essential-image test'),(4,'Cancelled general-limit descent construction'),(5,'When products of spaces and topoi agree'),(7,'Compact-point refinement on locally closed subspaces'),(8,'Infinite product comparison'),(9,'Infinite discrete counterexamples'),(10,'Inverse limits of essential topoi'),(12,'Cocontinuity of extension from a site'),(13,'Descent of cocontinuity through localization'),(14,'Sufficiency of sending covers to epimorphisms'),(15,'Preorder–topology adjunction'),(16,'Irreducibles and points of Alexandrov spaces'),(17,'Sobriety and descending chains'),(18,'Spatial presheaf topoi and essential points'),(19,'Correct morphisms in the preorder equivalence'),(20,'Extension of frame maps from rectangles'),(22,'Morita cancellation and rigidified uniqueness'),(23,'Higher torsor/hypercohomology fragment'),(26,'Bijectivity in recovery of a sober space'),(28,'Sufficient axioms for a topos'),(29,'Scope of classifying structures'),(30,'Conditional representation of a structure theory'),(31,'Fields and algebraic theories'),(32,'Cancelled field-recognition construction'),(33,'Reconstruction from set-valued models'),(39,'Dependent product and sums of topoi'),(45,'Universe bounds in sheafification'),(46,'Sufficiency of the faithful-flat fiber test'),(49,'Locally closed subsets under descent'),(51,'Descent of formal smoothness'),(52,'Meaning of effective quasi-coherent descent'),(54,'Descent of arbitrary immersions'),(57,'Effectivity of scheme descent data'),(58,'Converse characterization of universal homeomorphisms'),(62,'Diagonal/section/equalizer exercise'),(67,'Ring formulation of Zariski sheaves'),(70,'Closure of an affine image'),(69,'Examples of non-cartesian point-set fiber products'),(75,'Missing algebra in the equalizer square'),(77,'Idempotents and coproduct points'),(76,'Finite relations and geometric quotients'),(79,'The omitted affine sheaf proof')]
problems=[]
for i,(g,title) in enumerate(pg,1):
 cs=[c for c in claims if f'SA23-{700+g}' in c['items']]
 problems.append({'id':f'MP-SA23-spaces-{i:02d}','title':title,'occurrences':[{'claim':c['id'],'cote':c['cote'],'scans':c['scans'],'lines':c['lines']} for c in cs],'as_he_states':' '.join(c['his_statement']+' — '+c['status_on_pages'] for c in cs),'plausible_today':' '.join(c['statement'] for c in cs),'state_of_art':' '.join(c['id']+': '+c['fate'] for c in cs),'why_open':'The supplied leaves do not document a historical reason for leaving this step open. Cancellation, an unfinished proof, a pedagogical instruction, and a genuine missing hypothesis are distinguished in status_on_pages; no motive is inferred.','worth':'Worth a focused commentary or hypothesis check as ranked in directions.md; a solved exercise is not proposed as a new research problem.','refs':sorted({r for c in cs for r in c['refs']})})
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
links=[
('folder','161-3 scan 4, 3a:1-52','161-4 scans 16,18, 4a:731-750;4b:1-79','Same product-topos construction; later fragment has a false direct-image membership test.','Both complete source ends read; mathematical agreement is qualified.','Codex lead notes, unindexed'),
('folder','161-3 scan 6, 3a:180-183','161-3 scan 7, 3a:184-225','The announced product equivalence is proved on the next supplied leaf.','Explicit continuation and shared notation.','Codex K161-3-01'),
('folder','161-3 scans 11–12,3a:434-480','161-3 scan 29,3b:258-283,346-383','Frame extension tests the same product-locale comparison.','Both ends read; inferred mathematical link, not a written cross-reference.','Codex K161-3-01;K161-3-02'),
('folder','161-3 scan 21,3a:936-945','161-3 scan 22,3b:1-9','Cover-epimorphism sufficiency question continues into the next file and breaks off.','Both ends read; marginal non retained.','Codex K161-3-01;K161-3-02'),
('folder','161-3 scan 27,3b:226-256','161-3 scans 41,49,3c:24-31,235-247','Spatial presheaf topoi and minimal-neighborhood points recur; scan 49 supplies basis proof.','Both ends read; repeated subject merged.','Codex K161-3-02;K161-3-03'),
('folder','161-3 scan 40,3b:937-969','161-3 scan 42,3c:34-49','Field theory investigation and cancelled regular-ring test.','Both ends read; cancelled status and counterexample preserved.','Codex K161-3-02;K161-3-03'),
('folder','161-3 scans 31,33,3b:385-458,529-601','161-4 scan 6,4a:190-259','Module descent underlies gluing of the local Morita construction.','Both ends read; inferred mathematical relationship only.','Codex K161-3-02;K161-4-01'),
('folder','161-4 scan 5,4a:174-178','161-4 scan 6,4a:228,246-248','Immersion descent is first questioned, then asserted with arbitrary inserted.','Both ends read; assertion is false without extra restriction.','Codex K161-4-01'),
('folder','161-4 scans 15,17,4a:704-789','161-4 scans 31,32,4b:683-778','The ring sheaf condition is explicit in the later principal-open construction.','Both ends read.','Codex K161-4-01;K161-4-02'),
('folder','161-3 scan 35,3b:640-685','161-4 scan 31,4b:658-681','General sobrification versus sobriety of Spec A.','Both ends read; same irreducible-closed/generic-point criterion.','Codex K161-3-02;K161-4-02'),
('published','161-3 product scans 4–12','Lafforgue 2024 slides 47–48','Product-site theorem and local-compactness comparison.','Exact source slides opened, not merely title-matched.','spaces_Lafforgue2024'),
('published','161-3 infinite discrete scans 13,15','Heckmann 2014 online / 2015 issue, abstract and theorem subject','Countably presented locales are spatial; countable Baire test refutes blanket nonspatiality.','Publisher metadata and exact abstract opened; application proved in proof_checks.','spaces_Heckmann2015'),
('published','161-3 sober spaces scans 35,37,39','SGA IV 4.2.1–4.2.4;7.1.6','Sobrification and category of points.','Selected printed pages checked; bibliography verified at publisher.','spaces_SGA4I'),
('published','161-4 scan 5 formal smoothness question','Stacks tag06CM, Lemma10.138.16','Faithfully flat descent of formal smoothness without finite presentation.','Statement and full proof read, including arbitrary-projectivity descent.','spaces_StacksFormal'),
('published','161-4 scans 5,6 immersion assertion','Stacks tags02L8,02YL; comment11722 dated2026-08-28','Quasi-compact positive result, fppf version, and independently checked arbitrary-immersion counterexample.','Current comment date is not claimed as historical priority.','spaces_StacksImmersion'),
('published','161-4 scan10 margin EGAII4.5','EGAII §4.5','Explicit authorial cross-reference for ampleness criteria.','Both endpoints checked: original EGAII4.5.2,4.5.5–4.5.8 and4.6.11–4.6.13(ii), with manuscript scan10.','spaces_EGAII'),
]
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
tsv('project_leads.tsv',['from','to_project','lead','source_note','status'],[])
who='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner spaces'
events=[]
for c in claims:
 events.append((c['id'],'2026-11-19',who,'source and hypothesis comparison',c['status_on_pages']))
 events.append((c['id'],'2026-11-19',who,'mathematical argument check',c['computation']))
for name in json.loads((P/'compute_checks.output.json').read_text()):events.append((name,'2026-11-19',who,'executed exact computation','See compute_checks.py and compute_checks.output.json; scope stated per block.'))
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
print(f'Saved {len(problems)} problems, {len(rows)} readings, {len(links)} links, {len(events)} check events')
import runpy
runpy.run_path(str(P.parents[1]/'integration/apply_bt_spaces_problem_origins.py'))['apply_owner']('spaces')
runpy.run_path(str(P/'audit_publication_classes.py'))['save_audit']()
