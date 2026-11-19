"""Serialize manually ranked directions and genuine additional Codex subjects.

No indexed note verdict is generated or changed. Explicit subject clusters and
ratings below were assigned after reading the source and the finished registers.
"""
import json
import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
claims = json.loads((HERE / 'claims.json').read_text())
by_claim = {int(c['id'].rsplit('-', 1)[1]): c for c in claims}
items = json.loads((HERE / 'items.json').read_text())

# Each tuple is a manually identified source subject, not a keyword grouping.
subjects = [
    (1301, 'The proposed non-Cohen–Macaulay locus construction', [77],
     'The fibre-product depth calculation is distinct from the preliminary choice of a normal projective example with the required isolated bad locus.'),
    (1302, 'Finite-order jets, prolonged actions and natural constructions', [39,40,41,44,45],
     'The principal-parts and action constructions lead to the explicit finite-order natural-functor question. The unrelated inseparable-curve and differential-equalizer leaves are excluded.'),
    (1303, 'The withdrawn nonlinear compactness proposition EGA0.19.3.12', [53],
     'The source criticizes the use of linear compactness for algebra-homomorphism equations. The final errata withdraw the proposition; its exact replacement remains a separate task.'),
    (1304, 'Lê Dũng Tráng’s meromorphic-denominator corrections', [46],
     'Preserve the printed authorship and 11 January 1968 letter date; the issue is restriction-stable denominators and the resulting stalk and section identifications.'),
    (1305, 'Koszul regularity and the nonnoetherian immersion definition', [49],
     'This is the Deligne–Berthelot correction of the regular-immersion definition, later matched to SGA6 VII1.1–1.5.'),
    (1306, 'Deligne’s separation and finite-presentation kernel objections', [50,51],
     'Keep the A-submodule versus B-submodule distinction, the immersion hypothesis in the final print, and the separate finite-presentation kernel counterexample.'),
    (1307, 'The regular-sequence comparison without separation', [52,58],
     'The two letter occurrences concern the same implication in EGAIV19.5.5; the final proof is expressly credited to Deligne.'),
    (1308, 'Deligne’s numbered EGA errata and proof-simplification proposals', [61],
     'This editorial subject preserves distinct component claims: locality, dimension, differential sign, localization, formal-projectivity simplifications, and the incorrect completion equality.'),
    (1309, 'Reused Artin constructibility and derived-comparison drafts', [70,97],
     'Preserve Artin’s published authorship, the difference between the cancelled and final derived statement, and the underdetermined handwritten R1/base-change addition.'),
    (1310, 'Graded algebra extensions and section independence', [78,79,80,81,82],
     'One consecutive statement sequence: augmentation compatibility, triangular section changes, Poincaré ranks, flatness questions and polynomial sections. False literal variants remain explicit.'),
    (1311, 'Rings of definition for structures without automorphisms', [86],
     'The cote26 plan does not specify a full descent problem; uniqueness and effectivity remain separate.'),
    (1312, 'Hilbert and Picard representability without projectivity', [87],
     'The source records partial results. Modern algebraic-space statements do not imply unrestricted scheme representability.'),
    (1313, 'The dual of a nonprojective abelian scheme', [88],
     'The plan marks this answered by Raynaud. The original attribution/date remains separate from the modern existence statement.'),
    (1314, 'Quotients without a flatness hypothesis', [89],
     'A quotient category and replacement hypotheses are missing; the verified free flat group theorem is only a constrained neighboring result.'),
    (1315, 'The quotient by GLn acting without fixed points', [90],
     'Keep the quoted source phrase distinct from scheme-theoretic freeness; the latter is a precise modern sufficient hypothesis.'),
    (1316, 'Moduli of general varieties and abelian schemes', [91],
     'This is the explicit broad moduli question, with boundedness, polarization and automorphisms not fixed by the source.'),
    (1317, 'Principal bundles and the finite structural-group subcase', [92,93],
     'Preserve the curve/reductive-group scope of the verified stack theorem and the difference between finite étale and finite flat groups.'),
    (1318, 'Vector bundles on relative projective lines', [94],
     'The source itself asks whether the problem is ill-posed. Fibrewise splitting over a field does not settle varying-base classification.'),
    (1319, 'Unpolarized formal moduli of an abelian variety', [95],
     'The affirmative annotation is retained; the verified marked deformation theorem has dimension g squared, while polarized deformations are a separate problem.'),
    (1320, 'The theorem of the square without projectivity', [96],
     'Keep the nonprojective square question distinct from the verified existence of a cube-theorem chapter and from an unread exact numbered proof.'),
]
existing = {i['id']: i for i in items}
for number, title, ns, qualification in subjects:
    cs = [by_claim[n] for n in ns]
    ident = f'SA23-{number}'
    row = {
        'id': ident, 'sources': [], 'kind': 'other',
        'subkind': 'additional Codex subject; no indexed Stage1 entry',
        'cote': sorted({str(c['cote']) for c in cs}),
        'scans': [c['scans'] for c in cs],
        'lines': [f"{c['source']}:{c['lines']}" for c in cs],
        'additional_sources': sorted({c['source'] for c in cs}),
        'his_words': cs[0].get('his_words', cs[0].get('his_statement', '')),
        'statement': title, 'reconstruction': qualification,
        'claims': [c['id'] for c in cs],
        'check': 'agrees',
        'check_reason': 'Additional subject consolidated from the already fully read Codex transcription and completed claim register; no Pro note verdict is created.',
    }
    existing[ident] = row
    for c in cs:
        if ident not in c['items']:
            c['items'].append(ident)
items = list(existing.values())
(HERE/'items.json').write_text(json.dumps(items, ensure_ascii=False, indent=2)+'\n')
(HERE/'claims.json').write_text(json.dumps(claims, ensure_ascii=False, indent=2)+'\n')

# Explicit ratings and exact provenance; numbers are judgments, not a label parser.
specs = [
    (1,5,3,[1301],[77],[41]),
    (2,5,3,list(range(128,135)),[18,19,20,55,56,57,58,59,60],[5,27,28,29,30]),
    (3,5,3,[1302],[39,40,41,44,45],[16,17]),
    (4,5,3,[1303],[53],[26]),
    (5,4,5,[140,141,142],[21,22,23],[6,9]),
    (6,4,4,[1304],[46],[20]),
    (7,4,3,[1303,1305,1306,1307,1308,1309],[49,50,51,52,53,58,61,70,97],[23,24,25,26,31,37]),
    (8,3,3,[111],[6],[3]),
    (9,3,2,[118,119,120,121,152,165],[27,31],[11]),
    (10,5,3,list(range(1311,1321)),list(range(86,97)),list(range(48,59))),
    (11,3,4,[1310],list(range(78,83)),[42,43,44]),
    (12,3,4,[143,144,149,150,151],[26,30],[10,12]),
]
# This serializer constructs the original twelve manually authored directions;
# the approved provenance overlay separates Stage6 from editorial directions.
# Read the preserved authored input, not the post-audit seven-direction output.
authored=HERE/'provenance/pre_origin_audit/directions.md'
md=(authored if authored.exists() else HERE/'directions.md').read_text()
sections = re.split(r'(?m)^## (\d+)\. ', md)[1:]
by_rank = {}
for j in range(0,len(sections),2):
    rank=int(sections[j]); body=sections[j+1]; title, body=body.split('\n',1)
    by_rank[rank]=(title.strip(),body)

def prose(body,label,nextlabel=None):
    start=body.index(f'**{label}.**')+len(f'**{label}.**')
    end=body.find(f'**{nextlabel}.**',start) if nextlabel else len(body)
    text=body[start:end].strip()
    # Remove the trailing old shorthand citation; exact IDs are serialized below.
    return re.sub(r'\s*\[(?:SA23|C-SA23|MP-SA23)[^\]]*\]\s*$', '',text).strip()

directions=[]
for rank,interest,progress,ii,cc,pp in specs:
    title,body=by_rank[rank]
    directions.append({
        'id':f'D-SA23-ega-{rank:02}', 'rank':rank, 'title':title,
        'interest':interest, 'feasible_progress_in_one_run':progress,
        'items':[f'SA23-{n}' for n in ii],
        'claims':[f'C-SA23-ega-{n:03}' for n in cc],
        'problems':[f'MP-SA23-ega-{n:02}' for n in pp],
        'known':prose(body,'Known','First step'),
        'residual':prose(body,'What it would establish','Known'),
        'would_establish':prose(body,'What it would establish','Known'),
        'first_step':prose(body,'First step'),
        'rating_qualification': 'Progress is for one bounded run. Any ink collation requires the missing scans; current numeric rating includes that access limit.' if rank in [7,11,12] else 'Progress rates a bounded deliverable, not resolution of the broad program.'
    })

all_items={i['id'] for i in items};all_claims={c['id'] for c in claims}
all_problems={p['id'] for p in json.loads((HERE/'problems.json').read_text())}
for d in directions:
    assert set(d['items'])<=all_items,(d['id'],'items')
    assert set(d['claims'])<=all_claims,(d['id'],'claims')
    assert set(d['problems'])<=all_problems,(d['id'],'problems')
(HERE/'directions.json').write_text(json.dumps(directions,ensure_ascii=False,indent=2)+'\n')

# Replace only the provenance/rating table; authored explanatory paragraphs stay.
table=['| Rank | Direction | Interest (1–5) | One-run progress (1–5) | Exact source IDs |',
       '|---|---|---|---|---|']
for d in directions:
    ids='; '.join(d['items']+d['claims']+d['problems'])
    table.append(f"|{d['rank']}|{d['title']}|{d['interest']}|{d['feasible_progress_in_one_run']}|{ids}|")
intro='# Ranked directions from cotes22,23 and26\n\nThese are separate future tasks. Numeric ratings are manual judgments from1(low) to5(high). Progress concerns a bounded single run, with missing scans taken into account. Additional Codex subjects SA23-1301–1320 have no indexed Stage1 entries; the69 indexed subjects and82 entry verdicts are unchanged. Exact machine-readable provenance is in directions.json.\n\n'
md=intro+'\n'.join(table)+'\n\n'+md[md.index('## 1.'):]
# Remove unrelated intervening leaves from the finite-order direction shorthand.
md=md.replace('[C-SA23-ega-039–045; MP-SA23-ega-16–19]', '[SA23-1302; C-SA23-ega-039–041,044–045; MP-SA23-ega-16–17]')
(HERE/'directions.md').write_text(md)

# Additional subject records require their own text-concordance events after a
# full rebuild. Existing claim proof events are not upgraded or duplicated.
event_path=HERE/'check_events.tsv'
if event_path.exists():
    events=list(csv.DictReader(event_path.open(),delimiter='\t'))
    fields=list(events[0])
    seen={e['statement_id'] for e in events}
    for number,title,ns,qualification in subjects:
        ident=f'SA23-{number}'
        if ident not in seen:
            events.append({'statement_id':ident,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega','type':'text concordance and subject consolidation','outcome':'Genuine additional Codex subject from the previously completed full source reads. '+qualification+' Existing claim assessments preserved; no indexed note verdict created.'})
    with event_path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'additional_subjects':len(subjects),'indexed_subjects':sum(bool(i['sources']) for i in items),'total_items':len(items),'directions':len(directions),'unresolved_ids':0}))
