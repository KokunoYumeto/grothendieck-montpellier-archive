"""Final provenance serialization of manually read Codex subject families.

This creates no indexed-note verdicts. Group membership is an explicit human
assessment, not an inference from headings or keywords.
"""
import json, pathlib
P=pathlib.Path(__file__).resolve().parent
claims=json.loads((P/'claims.json').read_text())
items=json.loads((P/'items.json').read_text())
families=[
 (1201,[*range(40,49),56],'Euclidean icosahedra, their symmetry groups and tangent-frame bundle','Paraphrase: construct the neighbouring fivefold cap, determine its rotations, and recover the full graph symmetry group.'),
 (1202,[49,50,51,52],'Cyclotomic angle algebra and inversion invariants','Paraphrase: identify the inversion-fixed angle algebra and its trace, norm and descent properties.'),
 (1203,[53],'The incomplete rectangular-cover construction of a frame coproduct','Paraphrase: prove that the displayed map preserves arbitrary joins under the proposed covering conditions.'),
 (1204,[54,55,57],'Homogeneous sets, the five-object action and normalizer labels','Paraphrase: identify equivariant maps and determine whether the induced five-object permutation action is faithful.'),
 (1205,[58,59],'Arithmetic existence and conjugacy of icosahedra','Paraphrase: formulate arithmetic icosahedra, their orthogonal conjugacy and finite stabilizers.'),
 (1206,[60,61],'Functor topoi, their direct images and the product assertion','Paraphrase: compute the direct image and ask whether the functor topos is a product of topoi.'),
 (1207,list(range(62,72)),'Ribbon neighbourhoods, surface embeddings and mapping-class stabilizers','Paraphrase: classify graph embeddings using regular neighbourhoods, complementary surfaces and induced fundamental-group maps.'),
 (1208,[72,73,74],'Coset descriptions of graph automorphisms and edge endpoints','Paraphrase: characterize loop reversal and injectivity of the pair-of-endpoints map in a homogeneous graph.'),
]
items=[x for x in items if not 1201<=int(x['id'].split('-')[-1])<=1208]
for n,ns,title,words in families:
    subset=[c for c in claims if int(c['id'].split('-')[-1]) in ns]
    lines=list(dict.fromkeys(l for c in subset for l in c['lines']))
    scans=sorted(set(s for c in subset for s in c['scans']))
    ident=f'SA23-{n}'
    items.append(dict(id=ident,sources=[],kind='other',cote=['161-6'],scans=scans,lines=lines,
        his_words=words,statement=title,
        reconstruction='Additional subject item from fully read Codex transcriptions; it has no indexed Pro note entry and adds no Stage 1 verdict row.',
        check='agrees',check_reason='The underlying passages were read in full and their mathematical claims, cancellations, reading alarms and searches are recorded separately. This item consolidates their subject provenance.',
        record_origin='source subject',claim_ids=[c['id'] for c in subset]))
    for c in subset:c['items']=[ident]
literal_selections={1201:(1,14),1202:(1,249),1203:(1,326),1204:(1,636),1205:(2,294),1206:(2,393),1207:(2,437),1208:(2,714)}
for item in items:
    n=int(item['id'].split('-')[-1])
    if n in literal_selections:
        part,line=literal_selections[n]
        fn=f'sources/texts/codex/K161-6-{part:02d}_transcription.tex'
        quote=(P.parents[2]/fn).read_text().splitlines()[line-1]
        item['source_paraphrase']=item['his_words']
        item['his_words']=quote
        item['source_quotations']=[dict(file=fn,physical_lines=str(line),literal_excerpt=quote)]
for c in claims:
    c['record_origin']='source assertion'
    c['reconstruction_boundary']='The historical assertion is recorded in his_statement. The modern hypotheses, independent proofs, counterexamples and conditional repairs in statement and computation are present-run reconstructions unless explicitly attributed to a checked source. The conditional K1 lead in C-SA23-misc-037 is not asserted as a counterexample or as a manuscript statement.'
for name,data in [('items.json',items),('claims.json',claims)]:
    (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def C(ns):return [f'C-SA23-misc-{n:03d}' for n in ns]
def M(ns):return [f'MP-SA23-misc-{n:02d}' for n in ns]
def I(ns):return [f'SA23-{n}' for n in ns]
directions=[
 dict(id='D-SA23-misc-01',title='A precise arithmetic icosahedron moduli statement',interest=5,feasible_progress_in_one_run=3,
 items=I([1202,1205]),claims=C([49,50,51,52,58,59]),problems=M([13,14,17]),
 first_step='Collate scan 22’s uncertain base and group notation, then specify the quadratic form and configuration functor over a base with 2 and 5 invertible.',
 known='The cyclotomic angle algebra, inversion invariants even in characteristic 2, and the polar identities are checked. Existing finite-group-scheme theorems have different hypotheses.',
 residual='The archival all-base existence, orthogonal conjugacy and stabilizer assertions lack a sufficiently specified moduli problem. A single run can formulate the exact statement and test bad fibres, not promise an all-base classification.'),
 dict(id='D-SA23-misc-02',title='Differential automorphisms and the corrected unipotence implications',interest=4,feasible_progress_in_one_run=5,
 items=I(list(range(321,327))),claims=C(list(range(21,30))),problems=M([4]),
 first_step='Write the difference-ideal criterion, bounded-unipotence sufficiency, dual-number counterexample and filtration-raising repair in one theorem-and-counterexample sequence.',
 known='The mathematical correction chain is checked by independent arguments and the exact later Zhao source.',
 residual='The remaining work is an expository companion preserving the author’s withdrawal and reassertion. It is not a new theorem project.'),
 dict(id='D-SA23-misc-03',title='Which module-valued functors are detected by nilpotent tests?',interest=4,feasible_progress_in_one_run=3,
 items=I([313,316,317,318,319]),claims=C([*range(11,21),39]),problems=M([2,3]),
 first_step='Separate quasi-coherent module functors, internal Hom functors and arbitrary semilinear functors, and state a candidate nilpotent-detection condition.',
 known='The unrestricted assertion is false; coefficient calculations and the arbitrary-module classification settle important special cases.',
 residual='A useful restricted theorem needs a precisely chosen functor category. The reduction functor is a mandatory test against an overbroad condition.'),
 dict(id='D-SA23-misc-04',title='Recover the intended rectangle-cover axiom for frames',interest=4,feasible_progress_in_one_run=3,
 items=I([1203,1206]),claims=C([53,60,61]),problems=M([12,18,19]),
 first_step='Read the ink for scans 13–16’s missing axiom (e), then compare its rectangular-cover condition with the independently read bifaisceau/product construction in cote 161-3.',
 known='The functor-category product theorem and the right Kan direct image are established; the proposed frame supremum calculation has a conditional proof.',
 residual='The missing covering axiom cannot be reconstructed merely by choosing a condition that would make the proof work. A bounded task begins with collation.'),
 dict(id='D-SA23-misc-05',title='An exact dictionary for graph embeddings and mapping-class stabilizers',interest=3,feasible_progress_in_one_run=5,
 items=I([1207]),claims=C(list(range(62,72))),problems=M(list(range(20,26))),
 first_step='Work out a two-loop bouquet in a torus, including its rotation system, boundary cycles, induced fundamental-group map and stabilizer, with explicit peripheral conventions.',
 known='For finite graphs in compact oriented surfaces the relevant isotopy characterization and restriction-bundle mechanism are checked against exact sources.',
 residual='The useful task is a complete archival-to-modern comparison and example. Infinite-type, punctured and boundary variants require their own hypotheses.'),
 dict(id='D-SA23-misc-06',title='Orientation conventions and determinant normalization',interest=3,feasible_progress_in_one_run=4,
 items=I(list(range(327,342))),claims=C(list(range(30,39))),problems=M([5,6,7]),
 first_step='Write the two normal-order conventions and the comparison t_n=(-1)^{n(n+1)/2}, then distinguish natural rank-one normalization from objectwise normalization.',
 known='The sign model, graded-line symmetry and determinant-coherence comparisons are checked. Groupes self-braiding and forms Picard-groupoid passages give a verified common invariant.',
 residual='A concise companion is feasible. The unfinished I(omega,omega-prime) requires an ink reading, and a conditional K1 twist remains a lead until an actual ring and character are exhibited.'),
 dict(id='D-SA23-misc-07',title='Resolve the special icosahedral coset and normalizer labels',interest=3,feasible_progress_in_one_run=3,
 items=I([1204,1208]),claims=C([54,55,57,72,73,74]),problems=M([16,26]),
 first_step='Collate the unnamed subgroups on scan 20, realize each explicitly in A5 or the full symmetry group, and compute its normalizer and core.',
 known='The general homogeneous-set, loop-reversal and endpoint-injectivity criteria are proved; the generic normalizer equality has a counterexample.',
 residual='The special intended instance can be settled only after the subgroup labels are known. The generic counterexample does not refute every possible icosahedral interpretation.'),
]
(P/'directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')
md=(P/'directions.md').read_text()
md=md.replace('When a direction comes solely from the additional Codex transcriptions, there is no Stage-1 indexed item; that absence is stated instead of inventing a note provenance.','Additional Codex subject items SA23-1201–1208 provide item provenance for the fully read cote 161-6 passages. They have no indexed Pro note sources and add no Stage 1 verdict rows; the 45 original indexed-note items remain distinct. Numerical scores and exact individual identifiers are in directions.json.')
md=md.replace('No Stage-1 item; C-SA23-misc-049','SA23-1202,1205; C-SA23-misc-049').replace('No Stage-1 item; C-SA23-misc-053','SA23-1203,1206; C-SA23-misc-053').replace('No Stage-1 item; C-SA23-misc-062','SA23-1207; C-SA23-misc-062').replace('No Stage-1 item; C-SA23-misc-054','SA23-1204,1208; C-SA23-misc-054')
(P/'directions.md').write_text(md)
coverage=(P/'coverage.md').read_text()
if '## Additional Codex subject provenance' not in coverage:
    coverage+='\n## Additional Codex subject provenance\n\nThe final provenance pass adds eight subject items, SA23-1201–1208, for the already fully read cote 161-6 passages and claims 040–074. Their sources arrays are empty because they do not derive from indexed Pro note entries. There are therefore 53 subject items in this part, of which exactly 45 arise from the 53 indexed notes. The 53 entry-verdict rows, 74 claims and 27 problem records are unchanged. Every claim records its source-assertion origin and distinguishes the present reconstruction in its proof field.\n'
    (P/'coverage.md').write_text(coverage)
print(json.dumps({'items':len(items),'indexed_note_items':45,'additional_Codex_items':8,'claims':len(claims),'directions':len(directions)}))
counts=json.loads((P/'counts.json').read_text())
counts.update(items=53,indexed_note_items=45,additional_Codex_items=8,directions=7)
(P/'counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
