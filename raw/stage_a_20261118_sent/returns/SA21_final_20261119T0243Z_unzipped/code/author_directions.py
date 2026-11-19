"""Ranked tasks authored from the completed checks; no task is developed here."""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[1]
alias={x['source_id']:x['canonical_id'] for x in csv.DictReader((R/'audit/problem_aliases.tsv').open(),delimiter='\t')}
directions=[]
def D(rank,title,interest,reach,items,claims,problems,establish,known,first,limit):
 directions.append(dict(rank=rank,title=title,interest=interest,few_hour_reach=reach,items=items,claims=claims,problems=[alias[p] for p in problems],source_problem_ids=problems,what_it_would_establish=establish,known=known,first_concrete_step=first,scope_limit=limit))
D(1,'Fix the final spatial-atelier theorem and its axiom versions','very high','high for a finite core',['SA21-1','SA21-16'],['C-SA21-7-048','C-SA21-7-050','C-SA21-8-018R','C-SA21-9-023','C-SA21-9-028'],['MP-SA21-7-15','MP-SA21-8-05','MP-SA21-9-07'],
 'A theorem with fixed incidence, refinement, common-face orthogonality and support data, plus a proved reconstruction from ordered deployments.',
 'The dense support representation survives and the ordinary downset core is classical. Comparable-pair orthogonality and deployment injectivity alone do not replace common-face orthogonality. The words atelier/magasin change at IX38–41.',
 'Make one version table ending with IX, list the exact hypotheses used by each reconstruction arrow, and isolate the compatible finite-figure subtheorem.',
 'Stage1 items are program/early-terminology anchors only; the mathematical sources of this later task are the listed Codex claims. Do not silently conjoin axioms from different drafts.')
D(2,'Identify the exact support condition behind local complements','very high','high for implications and small countermodels',['SA21-1','SA21-16'],['C-SA21-4-034','C-SA21-4-035','C-SA21-7-041','C-SA21-7-043','C-SA21-7-045'],['MP-SA21-4-12','MP-SA21-7-13'],
 'A precise sufficient condition for the local relative-complement identity, separated from global Booleanity and faithful realization.',
 'The global Boolean conjecture and the stated L1 rescue have checked finite countermodels. Orthomodularity repairs a specific lattice identity; optional absorption is stronger/different and fails in the P4 certificate. Later IX commensurability tests further constrain a repair.',
 'Write the exact local equation and compare each explicitly retained support/absorption condition against it, beginning with P4 and the later IX finite certificates.',
 'Do not reopen refuted unconditional versions or equate faithful with fully faithful external support.')
directions[-1]['claims']+=['C-SA21-9-092','C-SA21-9-103','C-SA21-9-105','C-SA21-9-106','C-SA21-9-126']
directions[-1]['problems']+=[alias[p] for p in ['MP-SA21-9-22','MP-SA21-9-24','MP-SA21-9-25','MP-SA21-9-31']]
directions[-1]['source_problem_ids']+=['MP-SA21-9-22','MP-SA21-9-24','MP-SA21-9-25','MP-SA21-9-31']
D(3,'Complete the corrected correspondence and support-functor dictionary','very high','high for an exact theorem comparison',['SA21-1','SA21-16'],['C-SA21-8-035','C-SA21-9-028','C-SA21-9-030','C-SA21-9-030R','C-SA21-9-052','C-SA21-9-055','C-SA21-9-056','C-SA21-9-058','C-SA21-9-060','C-SA21-9-066'],['MP-SA21-9-08','MP-SA21-9-13','MP-SA21-9-15','MP-SA21-9-17'],
 'A typed category distinguishing set-valued correspondences, induced join maps, orthogonal adjoints, complement-preserving maps and their compositions.',
 'The IX95/97 correction adds singleton-generator compatibility, and the normalized correspondence theorem is now independently checked. Domenach–Leclerc and Coecke–Moore give exact closed-fiber and canonical-category comparisons; Paseka–Vetterlein treats a different single-valued adjointable class. The universal Hom orthocomplement and the stated general span factorization are refuted, so any geometric restriction must be explicit.',
 'Transcribe the repaired conditions into a two-column dictionary with domains/codomains, then verify each composition statement using only those conditions.',
 'Closure preservation, join preservation, orthocomplement preservation and preservation of top are different requirements. The failed general Hom/spatios expectation is not a premise.')
D(4,'Settle global orientation for one fixed network axiom system','high','moderate; a decisive small model is plausible',['SA21-5','SA21-8','SA21-30','SA21-31'],['C-SA21-1-011','C-SA21-1-024','C-SA21-1-025'],['MP-SA21-003','MP-SA21-007'],
 'Either coherent two-class orientation transport or a countermodel satisfying the exact chosen branch and extension axioms.',
 'The transport-graph obstruction is elementary; the single-segment order theorem is settled. The manuscript itself says the general verification is missing, and the matched2026 result explicitly excludes it.',
 'Define every transport edge and its inverse from the fixed axioms, then reduce the issue to a stated family of closed walks.',
 'Do not assume the transport graph is connected merely because a different incidence relation is connected; do not identify a diagnostic with a proof of zero holonomy.')
D(5,'Finish the equal-endpoint segment lemma at singular ends','high','moderate to high for the precise lemma',['SA21-8','SA21-23','SA21-35','SA21-36'],['C-SA21-1-013','C-SA21-1-014','C-SA21-1-029','C-SA21-1-031','C-SA21-1-032'],['MP-SA21-009','MP-SA21-010'],
 'A complete equal-endpoint branch/intersection theorem with a stated weak or strong F6 convention, or a counterexample.',
 'Weak and strong F6 differ at singular endpoints. The existing two-maxima example proves that distinction but does not refute the equal-endpoint lemma. The supplied final argument stops mid-formula.',
 'Prove or refute the general regular-end prolongation lemma first, then mark the exact step requiring whole-support containment in the equal-endpoint proof.',
 'A circle-versus-line classification is a later task, not an automatic consequence of this local lemma.')
D(6,'Make the full spectral cut a defined topological object','high','moderate for compact conic examples',['SA21-65','SA21-66','SA21-71','SA21-72','SA21-73'],['C-SA21-2-038','C-SA21-2-039','C-SA21-2-042','C-SA21-2-043','C-SA21-2-044'],['MP-SA21-017','MP-SA21-018','MP-SA21-019'],
 'A rigorous full-cut construction over A, with separate regularity and connectedness transfer theorems for the partial cut.',
 'The relative-Stone boundary convention and the sheaf comparison are clear. The global rive spectrum and the étalé space of elements are different. Neither Boolean duality nor the injective rive map supplies the entire cut topology.',
 'Define the full cut on a compact finite PL pair and prove its map to X is unchanged off A and has the intended relative spectral fiber over A.',
 'Use the tripod contraction counterexample to prevent a blanket end-reduction step; do not claim the maille iff theorem from the birive notation alone.')
D(7,'Prove the exact category-level cutting and gluing theorem','high','high once morphisms are fixed',['SA21-51','SA21-52','SA21-53','SA21-75','SA21-88'],['C-SA21-2-018','C-SA21-2-019','C-SA21-2-020','C-SA21-2-046'],['MP-SA21-013','MP-SA21-021'],
 'A precise equivalence for ordered compatible cuts and labeled gluing data, with the two-node symmetry addressed under fixed admissibility assumptions.',
 'Closed-piece reassociation and the n+1/n count are checked. The pages do not specify a morphism category; isotopy classes retain different coherence from actual homeomorphisms.',
 'Choose compact Hausdorff or finite PL ficelles and endpoint-preserving homeomorphisms, then write cutting and pushout functors and their unit/counit maps.',
 'Treat the maille symmetry only after the full-cut definition is available; ordinary set disjointness is insufficient.')
D(8,'Complete the interval and half-interval support calculus','high','high for bounded finite cases',['SA21-10','SA21-22','SA21-53'],['C-SA21-7-024','C-SA21-8-044','C-SA21-8-052','C-SA21-9-005','C-SA21-9-013'],['MP-SA21-7-09','MP-SA21-8-15','MP-SA21-9-03'],
 'An exact theorem for formal endpoints, omitted points, half intervals, irredundant representatives and least closed constructible supports.',
 'The proper-interval relational core has an exact literature comparison; the manuscript adds point strata and half intervals. Hypothesis H and the restart allowing extremal half intervals must be retained.',
 'Make an endpoint/degenerate-symbol table and test the least-closure step for bounded posets satisfying H before treating the general infinite case.',
 'Empty ordinary set interior does not erase a formal interval stratum, and total-order conclusions must not be imposed on every poset.')
D(9,'Separate local lattice morphisms from global figure morphisms','high','high for a preservation table',['SA21-1','SA21-16'],['C-SA21-6-013','C-SA21-6-018','C-SA21-7-018','C-SA21-8-022','C-SA21-8-030R'],['MP-SA21-6-03','MP-SA21-7-07','MP-SA21-8-06','MP-SA21-8-10'],
 'Necessary and sufficient compatibility/face-lifting conditions for a stratum map to induce the desired global figure map.',
 'Complete downset homomorphisms have a known order-theoretic description. Local isomorphisms do not guarantee global faithful realization. Face bijection becomes optional in a later margin, and mere monotonicity does not preserve compatible joins.',
 'Write the preservation table with and without the optional face-bijection clause, including a zero image and a composite elementary image.',
 'The later IX elementary-or-zero claim must be compared with the corrected VIII figure pullback at its actual typing; changed conventions are not automatically contradictions.')
directions[-1]['claims']+=['C-SA21-9-116','C-SA21-9-120','C-SA21-9-121']
directions[-1]['problems'].append(alias['MP-SA21-9-28'])
directions[-1]['source_problem_ids'].append('MP-SA21-9-28')
D(10,'Specify admissible restrictions and geometric subdivision extensions','medium-high','moderate; high for one model category',['SA21-25','SA21-26','SA21-27','SA21-39'],['C-SA21-1-018','C-SA21-4-019','C-SA21-4-021','C-SA21-6-036','C-SA21-6-039'],['MP-SA21-005','MP-SA21-4-08'],
 'A restriction/extension theorem in a stated category, with an exact description of which exterior incidence data survive.',
 'Arbitrary réseau restriction fails. The concrete preorder model has a replacement construction, while strict simplicial elementary fillers can fail. Opened simultaneous/normal triangulation results do not imply canonical uniqueness.',
 'Choose one of order-convex interval models or finite PL figures, write the closure requirements, and compare the desired relative extension with the exact triangulation theorem.',
 'Restriction of a réseau and extension of a figure subdivision are related design problems, not already the same theorem.')
D(11,'Control infinite figures and compactology','medium-high','moderate for one exact model',['SA21-1','SA21-16','SA21-69'],['C-SA21-6-003','C-SA21-6-040','C-SA21-7-012','C-SA21-9-019','C-SA21-9-020'],['MP-SA21-6-10','MP-SA21-7-05','MP-SA21-9-05'],
 'A precise family-closure and finite-subcover axiom compatible with one geometric or ordered model.',
 'Finite type, finite deployment and admitted infinite families differ. The checked stationary-family lemma uses complete join-primality. The Borel–Lebesgue/richness clause is announced but not fully specified.',
 'Choose bounded intervals or finite polyhedra, define the covers by subdivisions, and state the finite-subcover property before deriving consequences.',
 'Compactness of a conic base alone does not make the rive algebra finite; the earlier Cantor example is only a warning about that inference.')
D(12,'Recover the appropriate topology of actual ficelle places','medium-high','moderate for a separation criterion',['SA21-10','SA21-12','SA21-53','SA21-54'],['C-SA21-3-015','C-SA21-3-016','C-SA21-3-017'],['MP-SA21-3-05','MP-SA21-3-06','MP-SA21-3-07'],
 'Additional hypotheses under which the canonical tronçon topology has the separation or closure properties required by the geometric interpretation.',
 'Twin rational points refute T0/sobriety in a general abstract model; a strict-coordinate order gives a Hausdorff nontotal model. The author subsequently shifts to moderated rather than ordinary closure.',
 'Compare specialization and interval neighborhoods in one actual ficelle model with those in the two counterexamples, keeping the chosen topology fixed.',
 'Do not infer totality from T1 or sobriety from closed singletons; the erroneous neighboring SGA example is excluded.')
D(13,'State a bounded two-dimensional maquette comparison','medium','moderate for definitions, low for a universal theorem',['SA21-1','SA21-16','SA21-89'],['C-SA21-8-002','C-SA21-8-003'],['MP-SA21-8-01'],
 'A precise comparison with a selected class of finite oriented cell complexes that records loops and repeated face incidences.',
 'The dimension-one graph encoding is classical. The regular CW face-poset theorem has different hypotheses and does not identify the unspecified two-dimensional maquette category.',
 'Specify the cells, orientation reversal, permitted multiplicities and attaching data of the smallest2-dimensional examples.',
 'A finite number of objects does not remove automorphism or endomorphism data; do not replace the category by a poset without a theorem.')
D(14,'Choose geometric correspondence classes after the universal obstructions','high','high for precise exclusions and a restricted example class',['SA21-1','SA21-16'],['C-SA21-9-058','C-SA21-9-060','C-SA21-9-063','C-SA21-9-066','C-SA21-9-086'],['MP-SA21-9-14','MP-SA21-9-15','MP-SA21-9-16','MP-SA21-9-17','MP-SA21-9-20'],
 'A delimited class of geometric support lattices and maps for which a specified product or graph factorization could hold.',
 'The full join-map Hom lattice need not admit any order-reversing bijection; OR-product closure differs from closed-fiber closure; the stated universal span fails for every possible intermediate object in the checked example. These unrestricted questions already have negative answers.',
 'List the support lattices and morphisms of three actual manuscript model classes, then determine which of the existing obstructions each excludes.',
 'Do not advertise a new unrestricted factorization conjecture. A weaker map class or product convention must be named before asking for a positive theorem.')
D(15,'Define intrinsic constructible supports and the subdivision localization map','high','moderate for a precise finite formulation',['SA21-1','SA21-16'],['C-SA21-9-107','C-SA21-9-108','C-SA21-9-125','C-SA21-9-126'],['MP-SA21-9-26','MP-SA21-9-31'],
 'A precise localization of a fixed figure category at subdivisions, together with a typed support map and a test of thinness or order reflection.',
 'The final pages propose partial Boolean operations and ask whether subdivision localization is thin. General fraction calculus has exact hypotheses; neither that calculus nor the support notation supplies the required Ore conditions or faithfulness.',
 'Fix one finite atelier and its admitted figures, state the subdivision arrows, and compare two explicit zigzags with equal support.',
 'Keep the partial operation domain and the choice of admitted figures visible. This task does not claim the entire moderated constructible algebra exists.')
D(16,'Construct one universal excision with the final zero convention','high','moderate for maquettes and a constrained second model',['SA21-1','SA21-16'],['C-SA21-8-027','C-SA21-8-028','C-SA21-9-120','C-SA21-9-121','C-SA21-9-122','C-SA21-9-123','C-SA21-9-124'],['MP-SA21-8-08','MP-SA21-8-09','MP-SA21-9-28','MP-SA21-9-29'],
 'A quotient universal property in a specified pointed atelier category, with an exact kernel and an explicit comparison to deletion or restriction.',
 'The maquette deletion construction has an independent proof. A bare pointed morphism can have a kernel that is not double-polar closed. The set-figure excision proposal depends on whether closed or open support is being killed.',
 'Write the universal property with the IX134 zero relations, check it in the maquette case, and state the additional support condition before attempting a set-figure quotient.',
 'A lattice quotient, a categorical localization and deletion of strata are distinct constructions; no common identification is assumed.')
D(17,'Make support presentations independent of redundant points and zeros','medium-high','high for a categorical dictionary',['SA21-1','SA21-16'],['C-SA21-9-040','C-SA21-9-042','C-SA21-9-044','C-SA21-9-045','C-SA21-9-048','C-SA21-9-055'],['MP-SA21-9-11','MP-SA21-8-11'],
 'Exact functors comparing redundant disjoncteur presentations, deletion or addition of null points, and a chosen modern orthoset category.',
 'Support ortholattices survive deletion of universally orthogonal points and appropriate dense restrictions. The canonical point relation is only a preorder until equal supports are identified. Modern unique-zero conventions are different from arbitrary E0.',
 'Specify the quotient by equal singleton supports and the delete/adjoin-zero maps, then check preservation of the normalized correspondence class.',
 'The object-level lattice isomorphism does not by itself establish an equivalence for every proposed raw point-map category.')
# Editorial ranking: mathematical interest, then attainable progress in one run.
rank_order=[1,2,3,14,4,5,6,7,15,9,16,8,10,11,12,17,13]
byrank={d['rank']:d for d in directions}
directions=[byrank[k] for k in rank_order]
for rank,d in enumerate(directions,1):d['rank']=rank
(R/'audit/directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')
out=['# SA21: ranked research directions','',
 'These are separate task specifications arising from the consolidation. No direction is developed here. Interest orders the list; the reach column estimates what one focused run of a few hours could reasonably settle. A high reach does not promise a solution to an unrestricted program.',
 '',
 'For directions grounded in later Codex-only cotes, Stage1 items SA21-1 and SA21-16 supply the opening program and the scope of its early vocabulary. They are context anchors, not fabricated indexed notes about those later pages. The listed claim and problem IDs provide the direct mathematical evidence.',
 '',
 '|Rank|Direction|Interest|Reach in a few hours|','|---:|---|---|---|']
for d in directions:out.append(f'|{d["rank"]}|{d["title"]}|{d["interest"]}|{d["few_hour_reach"]}|')
for d in directions:
 out+=['',f'## {d["rank"]}. {d["title"]}','',
  '**Origins.** Items: '+', '.join(d['items'])+'. Claims: '+', '.join(d['claims'])+'. Problems: '+', '.join(d['problems'])+'.','',
  '**What it would establish.** '+d['what_it_would_establish'],'',
  '**Known starting point.** '+d['known'],'',
  '**First concrete step.** '+d['first_concrete_step'],'',
  '**Scope.** '+d['scope_limit']]
(R/'SA21_directions.md').write_text('\n'.join(out)+'\n')
print(json.dumps({'ranked_directions':len(directions),'every_direction_has_item_claim_problem_ids':True}))
