"""Manually chosen bounded tasks; this file only serializes their ranking."""
import json,pathlib
P=pathlib.Path(__file__).resolve().parent
def I(ns):return [f'SA23-{n}' for n in ns]
def C(ns):return [f'C-SA23-groupes-{n:03d}' for n in ns]
def M(ns):return [f'MP-SA23-groupes-{n:02d}' for n in ns]
directions=[]
def add(n,title,interest,progress,items,claims,problems,establish,known,residual,first):
    directions.append(dict(id=f'D-SA23-groupes-{n:02d}',title=title,interest=interest,feasible_progress_in_one_run=progress,items=I(items),claims=C(claims),problems=M(problems),what_it_would_establish=establish,known=known,residual=residual,first_step=first,origin='Present-run research-direction proposal from the cited archival records; not a claim of novelty.'))

add(1,'A complete bounded mixed-envelope construction',5,3,
 [906,919,921,923],[22,23,24,25,82,88,90,91,101,114],[9,10,43,48,49,50,51,71,72],
 'One precise universal envelope, with explicit operations, relations, 2-cells, and a proved stopping bound, for a single chosen small doctrine.',
 'Kelly’s bounded completion and comodel results, modern sketchability theorems, and the exact biadjoint comparison explain substantial parts of the proposal. The cylinder/fold encodings and regular-cofinality repair are checked.',
 'The manuscript does not define every successor operation, prove local smallness for its unrestricted doctrine, or show that a small faithful basis generates operations. These are separate obligations.',
 'Choose finite limits together with one explicitly bounded class of colimits. Define the missing K step and preexactness, then list the universal property required at each successor stage before taking any transfinite union.')
add(2,'An exact cardinal dictionary for accessibility and filtration',4,5,
 [906,915,917],[23,65,66,68,69],[33,38],
 'A corrected translation of every cardinal quantifier on these pages into presentability ranks, directedness, and the sharply-larger relation.',
 'The countable-power counterexample, the singular-cardinal diagonal argument, and the distinction between filtered and aleph-one-directed presentations are proved. The checked modern rank theorem supplies the valid restricted statement.',
 'This is a commentary task with known mathematical outcomes. A sharper positive bound must state its cardinal-arithmetic hypothesis; the source’s exponent estimate cannot be simplified by notation alone.',
 'Make a table of the source symbols pi, pi-prime, and cofinality bounds, translate each to a regular-cardinal convention, and attach the two explicit counterexamples at the failed quantifiers.')
add(3,'Separate faithful bases, Morita equivalence, and reconstruction',5,4,
 [918,920,921,923,924],[76,77,83,84,85,91,93,94,95,101,104],[46,47,51,53,54,60,61],
 'A precise comparison of detection of transformations, generation under operations, Cauchy completion, and recovery of a theory from its Set models.',
 'Finite-limit recovery from finitely presentable models is established. Even finite sets give the Morita counterexample; the two-element object in FinSet opposite detects transformations without generating the product theory; the abelian-group example separates models from flat points.',
 'The intrinsic construction category Sigma on the late sheet is unfinished. No existing theorem is applied to it before its required preservation and accessibility properties are specified.',
 'Put FinSet opposite, its even-cardinality subcategory, and the finite-product theory of abelian groups in one explicit comparison table. Compute each basis closure, Karoubi completion, model category, and flat-point category.')
add(4,'Replace noetherian fppf point tests by an exact local model',4,4,
 [910],[38,40,41],[19],
 'A concise explanation of why noetherian tests miss nilpotents and how a genuinely fppf-local test ring repairs that failure.',
 'Schröer’s noetherian classification and the dual-number sieve give a complete negative answer to the noetherian proposal. Gabber–Kelly’s table deliberately treats other topologies under its stated hypotheses.',
 'A useful follow-up can work through one nonnoetherian fppf-local construction; it should not promise a new classification of all fppf points.',
 'Start with the dual numbers over an algebraically closed field, identify the noncovering reduced sieve, and follow the exact construction of a local object that detects it in the opened fppf source.')
add(5,'Internal component bounds and the torsor of decompositions',4,3,
 [913,914],[56,57,58],[27],
 'A precise internal statement relating a finite Boolean idempotent algebra, a bound on connected factors, and the torsor of ordered decompositions.',
 'The ordinary ring statement is proved, including the necessary finiteness of the Boolean algebra. Exact component rank is not preserved by arbitrary filtered colimits. Once a torsor is given, its pullback property follows from finite limits and epimorphisms.',
 'The construction of the sheaf of all decompositions through the proposed largest locus has not been shown to commute with inverse image. A chosen decomposition and an unstructured exact-rank property have different morphisms.',
 'Write the rank-at-most-n condition as an explicit coherent formula, construct ordered decompositions for n=2 in a sheaf topos, and compare the result with the source’s e-prime-n before considering arbitrary base change.')
add(6,'Formal smoothness and formal étaleness with fixed hypotheses',4,3,
 [914],[62],[30],
 'A logical and categorical formulation of the relative algebra properties that the source groups together, with each lifting quantifier and finiteness assumption explicit.',
 'The opened Stacks results identify formal smoothness, formal étaleness, finite presentation, and the ordinary local criteria. The source’s general list does not itself establish a geometric classifier for every property.',
 'Quantification over arbitrary square-zero extensions is not automatically a geometric formula. The correct restricted presentation must be fixed before claiming inverse-image stability.',
 'Fix a finitely presented A-algebra B. Write its square-zero lifting condition in terms of a finite presentation and compare that condition with the exact smooth/étale criteria before changing the base to an arbitrary topos.')
add(7,'A worked inverse image of stacks and relative classifier',4,4,
 [925,926],[105,106,107,113],[62,63,64,65],
 'One complete example of the comma-opposite 2-Kan extension, stackification, and the relative classifying 2-pullback with fixed underlying objects.',
 'The corrected Yoneda statement holds for representables in the stated comparison. The stack inverse image requires the opposite comma category and stackification. The fixed-object classifier follows from the checked topos 2-pullback theorem.',
 'The final notation for a stack of slice topoi is not sufficiently developed to identify a theorem. That endpoint must remain separate from the valid structure-stack construction.',
 'Choose a finite group action or a two-object algebraic structure on a simple site, write the actual descent groupoids, and compute the universal property of the relative 2-pullback.')
add(8,'Self-braiding, inverse pairings, and graded orientations',3,5,
 [902],[10,11],[5],
 'A short common-invariant companion to the inverse-pairing question, the graded determinant conventions, and the Picard-groupoid obstruction.',
 'The scalar epsilon(L), its square-one identity, the permutation-parity formula, and psi=epsilon(L) times the reversed pairing are proved. Both other archival endpoints have been read.',
 'The strictification question on the forms pages is stronger than the pairing calculation. The source’s sign exponent remains an ink question; parity 0/1 must not silently replace a written numerical sign.',
 'Write the coherence diagram for the inverse pairing, evaluate it on an odd superline, and place the exact source formulas beside the graded-orientation and Picard self-commutor passages.')
directions[-1]['related_archival_records']=['C-SA23-forms-041','C-SA23-misc-034','C-SA23-misc-037']
add(9,'Identify the filtered-F-crystal comparison before testing it',3,2,
 [904],[17],[7],
 'An identifiable statement with a specified base, tensor categories, admissibility condition, and comparison functor.',
 'The adjacent tensor-grading/cocharacter identity is settled. Liu’s theorem concerns crystalline lattices of weights 0 and 1 under its exact discretely valued base hypotheses; it does not identify arbitrary filtered F-crystals or every Hodge–Tate object.',
 'The final group symbols and the proposed equivalence are insufficiently specified in the supplied transcription. This is a scan-first identification task, not a claim that the modern Barsotti–Tate comparison remains open.',
 'Collate scan 17’s final comparison symbols and the linked Barsotti–Tate generator passages, then write the source and target categories and their admissibility restrictions in full.')
directions[-1]['related_archival_records']=['C-SA23-groupes-016','SA23-265','C-SA23-bt-065','C-SA23-bt-066','C-SA23-bt-067','C-SA23-bt-068','C-SA23-bt-069','C-SA23-bt-070','C-SA23-bt-071','MP-SA23-bt-21','MP-SA23-bt-22','MP-SA23-bt-23']
add(10,'Bicolimits and tensors for one accessible-category convention',4,2,
 [915,916],[73,74],[34,39],
 'A theorem or counterexample for a single specified bicolimit or tensor operation, with rank and morphism conventions fixed.',
 'The flexible-limit results and the locally presentable tensor construction are established. The checked finitary-doctrine bicolimit theorems concern more structured 2-categories than an unrestricted reading of Acc.',
 'The source’s broad bicolimit claim and merely accessible tensor interpretation are not settled by those nearby results. Changing between accessible and strongly accessible morphisms changes the question.',
 'Choose either a bicategorical pushout of fixed-rank accessible functors or a tensor universal property. State the objects, 1-cells, 2-cells, and allowed rank enlargement before looking for a construction.')
add(11,'A density and exact-Kan-extension companion',3,5,
 [903,905,916],[14,15,18,19,20,21,70],[6,8,36],
 'An exact statement separating density, left-exact comodel relations, pointwise Kan extension, and the false cofinality shortcut.',
 'The pointwise formula, restriction full faithfulness, and topos-target exactness are checked. Kelly’s comodel criterion gives the exact essential image. Explicit examples refute the source’s broader comma-finality and variance shortcuts.',
 'The remaining value is explanatory and historical. Any new theorem would need an additional, explicitly chosen target category beyond the already matched setting.',
 'Draw the actual two comma categories in the source, verify their variance on a small example, and state precisely which colimit relations a functor on the dense subcategory must preserve.')
add(12,'A pseudofield and field-classifier algebraic companion',3,5,
 [911,922],[46,48,96,97,98,99,100],[22,55,56,57,58,59],
 'A complete chain from the quasi-inverse equations and absolute-flat reflection to the corrected sheaf classifier of fields.',
 'The Chinese-remainder presentation, uniqueness of quasi-inverses, reflection properties, and the corrected field topology match exact published sources. The canceled presheaf assertion is false, and regular-element invertibility is not geometric in the unqualified sense.',
 'The proposed extension to every balanced bicomplete category lacks the needed exactness hypotheses. A worked categorical variant must name those hypotheses rather than extrapolate from topoi.',
 'Present the two-component affine scheme and its universal quasi-inverse equations explicitly, then calculate the covering families that distinguish pseudofields from fields and preserve the canceled source passage beside its replacement.')

# The final source-origin audit moves merely editorial questions out of Stage 3.
redirects=json.loads((P/'problem_editorial_redirects.json').read_text())
ed=json.loads((P/'editorial_tasks.json').read_text())
for d in list(directions):
    d['editorial_tasks']=[redirects[x] for x in d['problems'] if x in redirects]
    d['problems']=[x for x in d['problems'] if x not in redirects]
    if not d['problems']:
        for e in ed:
            if e['id'] in d['editorial_tasks']:e['proposed_followup']=d
        directions.remove(d)
    if d['id']=='D-SA23-groupes-12':
        d['claims'].append('C-SA23-groupes-115')
        d['known']+=' The zero-dimensional ring site has enough points by the exact separable-topos theorem, after its countability hypotheses are checked.'
(P/'editorial_tasks.json').write_text(json.dumps(ed,ensure_ascii=False,indent=2)+'\n')
directions.sort(key=lambda d:(-d['interest'],-d['feasible_progress_in_one_run'],d['id']))
for rank,d in enumerate(directions,1):d['rank']=rank
ids={x['id'] for x in json.loads((P/'items.json').read_text())}
cids={x['id'] for x in json.loads((P/'claims.json').read_text())}
mids={x['id'] for x in json.loads((P/'problems.json').read_text())}
for d in directions:
    assert set(d['items'])<=ids,d['id']
    assert set(d['claims'])<=cids,d['id']
    assert set(d['problems'])<=mids,d['id']
(P/'directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')
md=['# Ranked directions — cotes 161-1 and 161-2','',
 'Scores run from 1 to 5. Interest measures the mathematical and archival value of the precise task; one-run progress measures how much a research session of a few hours could establish. A high progress score may indicate a valuable settled companion, not a new theorem. These are proposed tasks only: none is developed as a new project in this dossier. Every direction has source item, claim, and problem provenance.','',
 '| Rank | Direction | Interest | Progress in one run |','|---:|---|---:|---:|']
for d in directions:md.append(f"| {d['rank']} | {d['title']} | {d['interest']} | {d['feasible_progress_in_one_run']} |")
for d in directions:
    md+=['',f"## {d['rank']}. {d['title']}",'',
      f"**Identifier:** {d['id']}. **Scores:** interest {d['interest']}/5; progress {d['feasible_progress_in_one_run']}/5.",'',
      '**Source items:** '+', '.join(d['items'])+'.','',
      '**Claims:** '+', '.join(d['claims'])+'.','',
      '**Problems:** '+', '.join(d['problems'])+'.','',
      '**What it would establish:** '+d['what_it_would_establish'],'',
      '**Known:** '+d['known'],'','**Residual:** '+d['residual'],'',
      '**First step:** '+d['first_step']]
    if d.get('related_archival_records'):md+=['','**Verified related archival records:** '+', '.join(d['related_archival_records'])+'. The claims remain distinct unless root records an exact occurrence merge.']
    if d.get('editorial_tasks'):md+=['','**Related editorial tasks:** '+', '.join(d['editorial_tasks'])+'. These are our verification or identification tasks, not authorial questions.']
(P/'directions.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'directions':len(directions),'ids_and_numeric_scores':'validated'}))
