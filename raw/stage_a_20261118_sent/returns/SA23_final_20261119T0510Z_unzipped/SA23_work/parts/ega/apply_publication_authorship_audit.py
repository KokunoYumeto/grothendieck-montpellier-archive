"""Apply five manually reviewed A-to-B publication-authorship corrections.

Class A means a checked match in Grothendieck's own published work. An
expose written by another author remains class B even when based on his
unpublished notes. This overlay preserves all source authors and quotations.
Run after the source/literature builders and before the problem-origin overlay.
"""
from pathlib import Path
import collections, csv, json

HERE = Path(__file__).resolve().parent
PARTS = HERE.parent
WORK = PARTS.parent
DATE = '2026-11-19'

DECISIONS = {
    'analysis_curves': {
        13: ('Michèle Raynaud', 'AC_RaynaudSGA2XIV', 'XIV Proposition 1.1 and Corollary 1.4'),
        15: ('Michèle Raynaud', 'AC_RaynaudSGA2XIV', 'XIV Théorème 1.8, reprint pp.165–167'),
        18: ('Michèle Raynaud', 'AC_RaynaudSGA2XIV', 'XIV Corollary 1.3 and restriction argument'),
        19: ('Michèle Raynaud', 'AC_RaynaudSGA2XIV', 'XIV Proposition 1.1, Corollary 1.4, Théorème 1.8'),
    },
    'ega': {
        49: ('Pierre Berthelot', 'SGA6VII', 'Exposé VII, printed pp.416–421: Definition 1.1, Proposition 1.3, Definition 1.4, 1.4.2–3 and Proposition 1.5'),
    },
}
NOTES = {
    'analysis_curves': "Class B follows the printed authorship of Michèle Raynaud's Exposé XIV. Its footnote credits Grothendieck's unpublished notes, but no separately checked publication by Grothendieck himself is matched here; the dossier's class A is not relative to the author of an attached source.",
    'ega': "Class B follows the printed authorship of Pierre Berthelot's Exposé VII. The checked Koszul replacement is not thereby a match in Grothendieck's own published work; the opened Stacks comparison does not supply such a match either.",
}

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def write_tsv(path, fields, rows):
    with path.open('w') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)

report = []
for owner, decisions in DECISIONS.items():
    part = PARTS / owner
    claims = json.loads((part / 'claims.json').read_text())
    by_id = {int(c['id'].rsplit('-', 1)[1]): c for c in claims}
    old_to_new_fates = {}
    for number, (author, ref, locator) in decisions.items():
        claim = by_id[number]
        assert ref in claim['refs'], (claim['id'], ref)
        old = claim['fate']
        note = NOTES[owner]
        fate = old if note in old else old.rstrip() + ' ' + note
        old_to_new_fates[old] = fate
        claim['class'] = claim['classification'] = 'B'
        claim['fate'] = fate
        if 'literature_fate' in claim:
            claim['literature_fate'] = fate
        claim['publication_authorship_audit'] = {
            'date': DATE,
            'previous_classification': 'A',
            'corrected_classification': 'B',
            'matched_publication_author': author,
            'reference': ref,
            'locator': locator,
            'reason': note,
            'source_authorship_and_mathematical_assessment_unchanged': True,
        }
        report.append({'id': claim['id'], **claim['publication_authorship_audit']})
    dump(part / 'claims.json', claims)

    log_path = part / 'search_log.jsonl'
    log = [json.loads(s) for s in log_path.read_text().splitlines()]
    for row in log:
        for number in decisions:
            claim = by_id[number]
            if row.get('id') == 'FATE-' + claim['id']:
                row['match_and_limit'] = claim['fate']
                row['classification'] = 'B'
                row['publication_authorship_audit'] = claim['publication_authorship_audit']
            elif row.get('id') == 'AC-FATE-' + f'{number:03}' and owner == 'analysis_curves':
                row['matched'] = claim['fate']
                row['classification'] = 'B'
                row['publication_authorship_audit'] = claim['publication_authorship_audit']
    log_path.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in log))

    links_path = part / 'links.tsv'
    links = list(csv.DictReader(links_path.open(), delimiter='\t'))
    if links:
        fields = list(links[0])
        for row in links:
            if row.get('what') in old_to_new_fates:
                row['what'] = old_to_new_fates[row['what']]
        write_tsv(links_path, fields, links)

    events_path = part / 'check_events.tsv'
    events = list(csv.DictReader(events_path.open(), delimiter='\t'))
    fields = list(events[0])
    target_ids = {by_id[n]['id'] for n in decisions}
    event_type = 'publication authorship classification audit'
    events = [e for e in events if not (e['statement_id'] in target_ids and e['type'] == event_type)]
    for number, (author, ref, locator) in decisions.items():
        claim = by_id[number]
        events.append({
            'statement_id': claim['id'], 'date': DATE,
            'who': 'GPT-6 Astra Pro; effort not independently exposed; SA23-20261119; owner ega',
            'type': event_type,
            'outcome': 'Manual correction A→B against the already opened primary work: ' + ref + '; ' + locator + '. ' + NOTES[owner] + ' Source quotations, source authorship, hypotheses and proof assessments are unchanged.',
        })
    write_tsv(events_path, fields, events)

dump(WORK / 'integration/ega_publication_authorship_audit.json', {
    'date': DATE,
    'definition': "A is a checked match in Grothendieck's own later published work; B is established by another author.",
    'decisions': report,
    'scope': 'Five exact already-opened publication matches; no new search or mathematical claim.',
})
print(json.dumps({'corrected_claims': [x['id'] for x in report],
                  'classes': {owner: dict(collections.Counter(c['class'] for c in json.loads((PARTS / owner / 'claims.json').read_text()))) for owner in DECISIONS}}, ensure_ascii=False))
