"""Serialize manually selected literal Codex quotations.

The passages were read in full. This program checks copying and locators; it
does not select claims, infer mathematical verdicts, or repair source readings.
"""
from pathlib import Path
import csv
import json

B = Path('/workspace/scratch/7feb9690b71f/SA08_work')
OUT = B / 'work/late'
WHO = 'GPT-6 Astra Pro; effort not exposed by runtime; SA08/late'
specs = []

def Q(n, file, passages, voice='authorial working text'):
    specs.append((n, file, passages, voice))

Q(921, 2, [(452, 452, r'The third integral is a homotopy invariant of \(\gamma\) because \(d\eta=\omega_1\wedge\omega_2\).')],
  'English donor typescript')
Q(922, 2, [(489, 489, r'The algebraic model of the \(C^{\infty}\) de Rham complex \(\Lambda^{M}(x_{1},\,x_{2},\,\ldots : d)\) is isomorphic to the model of the rational homotopy type \(\Lambda(x_{1},\,x_{2},\,\ldots : d)\) tensored by the real numbers.')],
  'English donor typescript')
Q(923, 2, [(506, 507, None)])
Q(924, 2, [(637, 638, None), (844, 844, None), (847, 848, None)])
Q(925, 2, [(651, 652, None), (704, 704, None)])
Q(926, 2, [(880, 880, None), (887, 887, None), (889, 889, None)])
Q(927, 2, [(752, 754, None), (763, 764, None)])
Q(928, 2, [(907, 909, None)])
Q(929, 3, [(3, 3, None), (50, 50, None)])
Q(930, 3, [(69, 69, r'du moins pour $M$ concentré en un seul degré')])
Q(931, 3, [(82, 82, None), (91, 91, r'\pi_i\operatorname{SYM}^{\infty}X'), (92, 92, None)])
Q(932, 3, [(64, 64, None), (80, 80, r"D'où une graduation (dite la graduation par le poids sur l'homologie des esp d'E.M).")])
Q(933, 3, [(131, 131, None), (133, 133, None)])
Q(934, 3, [(173, 175, None), (207, 207, None)])
Q(935, 3, [(200, 200, None)])
Q(936, 3, [(233, 233, None), (479, 480, None)])
Q(937, 3, [(240, 243, None)])
Q(938, 3, [(301, 301, r'\underset{\text{dual de $A$}}{A_{*}}'), (302, 304, None)])
Q(939, 3, [(311, 311, None), (315, 315, None)])
Q(940, 3, [(426, 428, None)])
Q(941, 3, [(433, 434, None), (437, 437, None)])
Q(942, 3, [(447, 449, None), (452, 452, None)])
Q(943, 3, [(527, 530, None), (533, 533, None)])
Q(944, 3, [(516, 516, None), (520, 522, None)])
Q(945, 3, [(555, 555, None), (562, 564, None), (570, 571, None)])
Q(946, 3, [(596, 598, None), (659, 659, None)])
Q(947, 3, [(671, 671, None), (685, 685, None)])
Q(948, 3, [(701, 702, None)])
Q(949, 3, [(721, 721, None)])
Q(950, 3, [(726, 728, None)])
Q(951, 3, [(802, 803, None), (836, 836, None)])
Q(952, 3, [(823, 823, None)])
Q(953, 3, [(825, 825, None), (829, 829, None)])
Q(954, 3, [(882, 882, None)])
Q(955, 3, [(893, 893, None), (896, 896, None)])
Q(956, 3, [(902, 903, None)])
Q(957, 3, [(938, 938, None)])
Q(958, 2, [(308, 308, None)])

overrides = {}
audit = []
events = []
for n, file, passages, voice in specs:
    fn = f'codex/K136-0{file}_transcription.tex'
    lines = (B / 'sources/texts' / fn).read_text().splitlines()
    fragments = []
    locators = []
    for a, b, selection in passages:
        passage = '\n'.join(lines[a-1:b])
        fragment = passage.strip() if selection is None else selection
        assert fragment in passage, (n, a, b, fragment)
        fragments.append(fragment)
        locators.append({'file': fn, 'lines': str(a) if a == b else f'{a}–{b}'})
    quote = ' … '.join(fragments)
    if voice == 'English donor typescript':
        quote = f'English donor typescript: “{quote}”'
    sid = f'SA08-C{n}'
    overrides[sid] = {'his_statement': quote, 'quotation_lines': locators}
    audit.append({'id': sid, 'voice': voice,
                  'literal_fragments': fragments, 'quotation_lines': locators,
                  'method': 'Manual selection after full passage reading; exact copying checked programmatically. No source emendation.'})
    events.append({
        'statement_id': sid,
        'date': '2026-11-19',
        'who': WHO,
        'type': 'used and rechecked in this run',
        'outcome': f'Literal brief quotation manually selected from the actual transcription and checked against its exact lines. Voice: {voice}. Deleted, inserted and doubtful readings remain visible. This event certifies source fidelity, not the mathematical assertion.',
        'refined_statement_id': '',
        'evidence': '; '.join(f"{x['file']}:{x['lines']}" for x in locators)
    })

(OUT/'root_quotes_late_part.json').write_text(json.dumps(overrides, ensure_ascii=False, indent=2)+'\n')
(OUT/'root_quote_audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2)+'\n')
with (OUT/'root_quote_events.tsv').open('w') as f:
    w = csv.DictWriter(f, list(events[0]), delimiter='\t', lineterminator='\n')
    w.writeheader()
    w.writerows(events)
print(json.dumps({'quotes': len(overrides), 'range': 'SA08-C921–958',
                  'literal_fragments': sum(len(x['literal_fragments']) for x in audit),
                  'source_fidelity_events': len(events)}, indent=2))

# The middle colleague manually read and selected C901–920. I independently
# read the three complete Codex transcriptions and checked these selections
# before this merge. Copy checking below is additional provenance validation.
middle_path = B/'work/middle/root_quote_candidates.json'
if middle_path.exists():
    middle = json.loads(middle_path.read_text())
    assert set(middle) == {f'SA08-C{i}' for i in range(901, 921)}
    peer_events = []
    for sid, rec in middle.items():
        parts = rec['his_statement'].split(' … ')
        assert len(parts) == len(rec['quotation_lines']), sid
        for fragment, loc in zip(parts, rec['quotation_lines']):
            a, *rest = loc['lines'].replace('–', '-').split('-')
            b = rest[0] if rest else a
            source = (B/'sources/texts'/loc['file']).read_text().splitlines()
            assert fragment in '\n'.join(source[int(a)-1:int(b)]), sid
        peer_events.append({
            'statement_id': sid, 'date': '2026-11-19', 'who': WHO,
            'type': 'used and rechecked in this run',
            'outcome': 'Independently read the actual source passage and checked the middle colleague’s manually selected literal quotation and exact locators. This is a source-fidelity review, not another mathematical proof.',
            'refined_statement_id': '',
            'evidence': '; '.join(f"{x['file']}:{x['lines']}" for x in rec['quotation_lines'])
        })
    merged = {**middle, **overrides}
    assert set(merged) == {f'SA08-C{i}' for i in range(901, 959)}
    merged['SA08-C953']['lines'] = [
        {'file': 'codex/K136-03_transcription.tex', 'lines': '825–830'}]
    (B/'work/root/quote_overrides.json').write_text(
        json.dumps(merged, ensure_ascii=False, indent=2)+'\n')
    with (B/'work/middle/root_quote_candidates_events.tsv').open() as f:
        middle_events = list(csv.DictReader(f, delimiter='\t'))
    all_events = middle_events + events + peer_events
    with (B/'work/root/quotation_CHECK_EVENTS.tsv').open('w') as f:
        w = csv.DictWriter(f, list(events[0]), delimiter='\t',
                          lineterminator='\n', extrasaction='ignore')
        w.writeheader()
        w.writerows(all_events)
    print(json.dumps({'merged_root_quotes': len(merged),
                      'quotation_events': len(all_events),
                      'C953_general_locus_corrected': '825–830'}, indent=2))
