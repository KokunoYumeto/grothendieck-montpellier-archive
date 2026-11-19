"""Final authored corrections and structural audit of the p4 dossier.

Run after build_codex.py and build_codex_aux.py. Decisions below are explicit
human-readable authored amendments; the validator never chooses verdicts.
Raw retrieved text is kept outside the deliverable. Mathematical checks are
separate executable programs, not inferred from successful JSON validation.
"""
from pathlib import Path
from collections import Counter
import csv, json, re, shutil

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[2]
WHO = 'GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p4'
DATE = '2026-11-19'

def read_json(name):
    return json.loads((OUT/name).read_text())

def write_json(name, rows):
    (OUT/name).write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')

def read_tsv(name):
    with (OUT/name).open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def write_tsv(name, fields, rows):
    with (OUT/name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        w.writeheader(); w.writerows(rows)

items, claims, problems = [read_json(x+'.json') for x in ('items','claims','problems')]
I = {x['id']: x for x in items}
C = {x['id']: x for x in claims}
P = {x['id']: x for x in problems}

# Exact short witness: the earlier Ker string was interrupted by diplomatic
# deletion markup. The replacement occurs literally in the recorded range.
I['SA13-414']['his_words'] = r'w_n:\Gamma_n'
C['C-SA13-414']['his_statement'] = r'w_n:\Gamma_n'

for c in claims:
    c['computation_base'] = 'shards/p4/'
for n in (419, 420, 423):
    refs = C[f'C-SA13-{n}']['refs']
    if 'P4_ColliotTheleneSkorobogatov' not in refs:
        refs.append('P4_ColliotTheleneSkorobogatov')

C['C-SA13-807']['class'] = 'E'
C['C-SA13-833']['class'] = 'B'
C['C-SA13-833']['computation'] = 'proof_audit.md §12 gives the principal-class proof and checks the scope counterexample.'
C['C-SA13-814']['computation'] = 'proof_audit.md §12: finite image including torsion and ℓ=2.'
for field in ('fate','present_status'):
    C['C-SA13-814'][field] = C['C-SA13-814'][field].replace('Reduction modulo ℓ (modulo4 when ℓ=2)', 'Reduction modulo ℓ, including ℓ=2,')
C['C-SA13-818']['computation'] = 'proof_audit.md §§12–13 documents the filtration proof and the printed-source error.'
for n in (824,826,827,828,829,830,831,832,834):
    C[f'C-SA13-{n}']['computation'] = C[f'C-SA13-{n}']['computation'].replace('§13', '§12')
P['MP-SA13-235']['state_of_art'] = ('The Artin–Schreier example in proof_audit.md §12 disproves the broad interpretation. '
    'The inherited coefficient scope is a reading problem; the repaired assertion for coefficients extending to X '
    'is verified. It is not an unresolved modern theorem.')

# The local cycles always exist. Properness belongs to the identification of
# global hypercohomology with the global specialization cone.
proper_statements = {
802: 'For X/S proper, localization, filtered colimits and proper base change give the global triangle RΓ(Xs,Φman)→RΓ(Xs,Λν)→RΓ(X_Kbar,Λν)→RΓ(Xs,Φman)[1]. Without properness the local triangle Φman→ΛXs→RΨΛ→ remains valid; sheafwise Φman=Cone(ΛXs→RΨΛ)[−1].',
804: 'For X/S proper, the local-to-global spectral sequence H^p(Xs,Φman^q_ν)⇒Φman^(p+q)_ν has global specialization-cone abutment. For general X/S the hypercohomology spectral sequence still exists, with abutment H^(p+q)(Xs,Φman), but it is not automatically the cone comparing whole special- and generic-fibre cohomology. The stalk construction is étale local on X.',
809: 'If X/S is proper and the nonsmooth locus in Xs is finite, the global specialization-cone group Φman^i_ν is the direct sum of the corresponding geometric stalks. The finite-support hypercohomology collapse itself does not require properness; properness identifies that hypercohomology with the global specialization cone.',
812: 'For X/S proper and U⊂Xη open, put Y=X−U. The filtered support complexes RΓ_Yα(Xα,Λν) give a global specialization cone with generic term RΓ(U_Kbar,Λν), and their restriction to Xs gives the local spectral sequence. The local sheaf construction remains defined without properness, but the global comparison requires it.',
815: 'For X/S proper and gα:U_Kα→X, the filtered colimits of R^qgα*Λν restricted to Xs define Ψ^q_ν; proper base change and Leray give H^p(Xs,Ψ^q_ν)⇒H^(p+q)(U_Kbar,Λν). Without properness these sheaves and their hypercohomology sequence remain defined, but that generic-fibre abutment is not automatic.'
}
prefix = 'Let S be a strictly henselian trait, with residue characteristic exponent p, generic field K and separable closure Kbar; let ℓ≠p and Λν=Z/ℓ^(ν+1). '
for n, statement in proper_statements.items():
    c = C[f'C-SA13-{n}']
    c['statement'] = prefix + statement
    if '§20' not in c['computation']:
        c['computation'] += ' Properness is checked separately in proof_audit.md §20.'
    warning = ' Properness is essential for this global identification; the local construction is unrestricted. See the smooth nonproper P¹-minus-a-special-point counterexample in proof_audit.md §20.'
    if warning not in c['fate']:
        c['fate'] += warning
    c['present_status'] = 'As of 19 November 2026: ' + c['fate']
for n in (478,482):
    if 'Global specialization comparisons require X/S proper.' not in I[f'SA13-{n}']['reconstruction']:
        I[f'SA13-{n}']['reconstruction'] += ' Global specialization comparisons require X/S proper; local cycle triangles do not.'

write_json('items.json', items)
write_json('claims.json', claims)
write_json('problems.json', problems)

# Bibliography annotations are our own concise source-inspection descriptions.
bib_path = OUT/'references.bib'
bib = bib_path.read_text()
bib = bib.replace('Locators2.9.4--2.9.6 and3.6.5.',
    'Original-image locators2.9.4 printed174,2.9.6 printed176 and3.6.5 printed205 (physical PDF pages179,181,210) checked.')
bib = bib.replace('Locators1.1.4,1.3--1.4,2.2.8,2.3.11,4.10--4.14 and7.1(b), printedp300.',
    'Checked locators1.1.4 printed220,1.3--1.4 printed222--225,2.2.8 printed241--242; original4.7--4.14 read from selected page OCR with key images checked:4.10 printed272,4.11 printed273--275,4.12 printed275--276,4.13 printed276,4.14 printed276--278. Original7.1(b) printed300 visually checked. Related2.3.11 is a discovery locator only.')
bib_path.write_text(bib)

def field_value(block, name):
    m = re.search(r'(?m)(?:^|,)\s*'+re.escape(name)+r'\s*=\s*\{', block)
    if not m: return ''
    start = m.end(); depth = 1
    for i in range(start, len(block)):
        if block[i] == '{' and (i == 0 or block[i-1] != '\\'): depth += 1
        elif block[i] == '}' and (i == 0 or block[i-1] != '\\'):
            depth -= 1
            if not depth: return block[start:i]
    raise AssertionError(('unbalanced BibTeX field', name))

references = {}
for m in re.finditer(r'(?m)^@[^\{]+\{([^,]+),([\s\S]*?)(?=\n@|\Z)', bib):
    references[m.group(1)] = m.group(0)

search_rows = read_tsv('search_log.tsv')
for row in search_rows:
    if row['search_id'] == 'P4-S07' and 'Final original-source check:' not in row['outcome']:
        row['queries'] += '; final exact searches: SGA7 IX 12.1; Grothendieck 12.1 Picard SGA'
        row['outcome'] += (' Final original-source check: routine search had irrelevant matches and the stronger search returned an unreliable AI retypesetting, which was excluded as authority. '
            'The original PDF was instead rendered and IX12.1–12.2, printed465–469, read directly. '
            'The curve/index hypotheses agree with the scoped comparison; original12.1.5 omits the principal-fibre relation, so the independent quotient calculation controls that formula.')
write_tsv('search_log.tsv',['search_id','date','queries','sources','outcome','claim_ids','reference_keys'],search_rows)

source_scope = dict(date=DATE,
    original_url='https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf',
    sha256='17286b0f0bec451068e0a5fa2c39e93de28e7c1ecee6739487cfac11c03c8dab',
    physical_page_rule='printed page + 5',
    original_pages_read=[
        dict(locator='VII2.9.4,2.9.6,3.6.5',printed=[174,176,205],method='Original images checked; earlier selected surrounding OCR read.'),
        dict(locator='VIII1.1.4,1.4',printed=[220,224,225],method='Original images and surrounding passages checked.'),
        dict(locator='VIII4.7–4.14',printed=list(range(269,279)),method='All selected OCR read, with key formula/hypothesis images272 and276 checked.'),
        dict(locator='VIII7.1(b)',printed=[300],method='Original image checked.'),
        dict(locator='IX2.4,2.6(a)',printed=[338,341,342],method='Original image338 and full OCR341–342 checked.'),
        dict(locator='IX12.1–12.2',printed=list(range(465,470)),method='Full original OCR read; images465–467 checked. The missing principal relation in12.1.5 is explicitly qualified.')],
    code='code/ocr_sga.py; code/inspect_original_sources.py',
    execution_note='An initial default-thread OCR invocation for physical324,346,347 stalled and was interrupted with exit130. The same pages completed successfully after OMP_THREAD_LIMIT=1; the retained source judgments use the completed output.',
    raw_location='Working source images and OCR are intentionally excluded from the deliverable.',
    limits='A checked locator is not approval of every formula in the volume. Raw OCR errors are resolved by original-image inspection where material.')
(OUT/'outputs/final_original_scope_audit.json').write_text(json.dumps(source_scope,ensure_ascii=False,indent=2)+'\n')

event_fields = ['statement_id','date','who','type','outcome']
events = read_tsv('check_events.tsv')
# The former standalone numerical example C445 was consolidated into C444.
# C444 already carries this same computation event; remove the stale ID.
events = [e for e in events if e['statement_id'] != 'C-SA13-445']
# Rebuild only the explicit finalization events. Original proof-check events
# remain separate and retain their precise descriptions.
events = [e for e in events if not e['outcome'].startswith(('Item source comparison only.', 'Reference inspection only.', 'Final properness audit.', 'Original-source formula check.'))]
for item in items:
    scope = ('Earlier-project context retained as an unavailable backing-source lead; no manuscript proposition or external proof is certified.'
        if item.get('kind') == 'our projects' else
        'The supplied note and quoted transcription range were compared, including carried hypotheses and cancellations. This event certifies that comparison only; mathematical proof checks belong to the linked claim events.')
    events.append(dict(statement_id=item['id'], date=DATE, who=WHO,
        type='carried as background without fault found', outcome='Item source comparison only. '+scope))
for key, block in references.items():
    annotation = field_value(block, 'annote')
    note = field_value(block, 'note')
    events.append(dict(statement_id=key, date=DATE, who=WHO,
        type='carried as background without fault found' if note == 'unverified' else 'used and rechecked in this run',
        outcome='Reference inspection only. '+annotation+' This is a bibliographic/source-scope event, not an independent proof certificate.'))
for n in proper_statements:
    events.append(dict(statement_id=f'C-SA13-{n}', date=DATE, who=WHO,
        type='targeted proof check', outcome='Final properness audit. X=P¹_S minus one closed special-fibre point is smooth, so local vanishing cycles are zero, but Xs=A¹ and Xbarη=P¹ have different H². The global comparison therefore retains properness. See proof_audit.md §20.'))
events.append(dict(statement_id='P4_SGA7IX', date=DATE, who=WHO,
    type='targeted proof check', outcome='Original-source formula check. Original IX12.1.5 printed466 omits the relation generated by the principal special fibre. For X=P¹_S its literal isomorphism would be Z≅0. C-SA13-415 already uses the correct quotient Z^I/Z(d_i), independently checked. See proof_audit.md §4; this does not invalidate the separately scoped implication chain and Picard/Néron conclusions.'))
write_tsv('check_events.tsv', event_fields, events)

# Raw source transcriptions/tool payloads are reproducible working evidence,
# not deliverable prose; retain metadata, code and our actual check outputs.
raw = ROOT/'work/p4_primary/raw_web'; raw.mkdir(parents=True, exist_ok=True)
for path in (OUT/'outputs').glob('web_*.json'):
    shutil.move(str(path), str(raw/path.name))
for pattern in ('sga7_intro_physical_*.txt', 'sga7_physical_*.txt'):
    for path in (OUT/'outputs').glob(pattern):
        shutil.move(str(path), str(ROOT/'work/p4_primary'/path.name))

errors = []
def require(condition, detail):
    if not condition: errors.append(detail)

for name, rows in (('items',items),('claims',claims),('problems',problems)):
    ids = [r['id'] for r in rows]
    require(len(ids)==len(set(ids)), ('duplicate IDs', name))
pages = json.loads((ROOT/'work/pages.json').read_text())
source_text = {}
locators = 0
for row in items+claims+problems:
    locations = row.get('lines', row.get('occurrences', []))
    for loc in locations:
        locators += 1
        source = ROOT/'sources/texts'/loc['file']
        require(source.exists(), (row['id'], 'missing source', str(source)))
        if not source.exists(): continue
        if loc['file'] not in source_text:
            source_text[loc['file']] = source.read_text().splitlines()
        lines = source_text[loc['file']]
        require(1<=loc['start']<=loc['end']<=len(lines), (row['id'], 'range', loc))
        matching = [p for p in pages if p['file']==loc['file'] and int(p['cote'])==int(loc['cote']) and int(p['scan'])==int(loc['scan']) and p['start']<=loc['start'] and loc['end']<=p['end']]
        require(bool(matching), (row['id'], 'scan-range mismatch', loc))
    quote = row.get('his_words', row.get('his_statement'))
    if quote is not None:
        if not quote:
            require(row['id'] in ('SA13-475','SA13-476'), (row['id'], 'unexpected empty quote'))
        else:
            text = '\n'.join('\n'.join(source_text[l['file']][l['start']-1:l['end']]) for l in locations)
            require(quote in text, (row['id'], 'quote not literally in located passage', quote))

searches = read_tsv('search_log.tsv')
search_ids = {s['search_id'] for s in searches}
for c in claims:
    require(c['class'] in 'ABCDEF', (c['id'],'class',c['class']))
    require(bool(c['search_ids']), (c['id'],'missing search'))
    for ref in c['refs']: require(ref in references,(c['id'],'missing reference',ref))
    for ref in c['search_ids']: require(ref in search_ids,(c['id'],'missing search',ref))
    for ref in c['items']: require(ref in I,(c['id'],'missing item',ref))
    require(c['computation_base']=='shards/p4/',(c['id'],'computation base'))
for p in problems:
    for ref in p['refs']: require(ref in references,(p['id'],'missing reference',ref))
    for ref in p.get('claims',[]): require(ref in C,(p['id'],'missing claim',ref))

types = {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
targets = set(I)|set(C)|set(P)|set(references)
event_targets = {e['statement_id'] for e in events}
for e in events:
    require(e['type'] in types, ('illegal event type',e))
    require(e['statement_id'] in targets, ('unknown event target',e['statement_id']))
for key in set(I)|set(C)|set(references): require(key in event_targets,('no event',key))
entries = read_tsv('entries.tsv')
require(len(entries)==103,('entry count',len(entries)))
require(len({e['entry_id'] for e in entries})==103, 'duplicate entry IDs')
require({int(e['entry_id'].split('#')[-1]) for e in entries}==set(range(1,104)), 'incomplete entry ordinal set')
for e in entries:
    require(e['item_id'] in I,('entry missing item',e))
    require(e['verdict'] in {'kept','merged','corrected','withdrawn','rests on a misreading'},('entry verdict',e))

summary = dict(date=DATE, items=len(items), claims=len(claims), problems=len(problems),
    entries=len(entries), readings=len(read_tsv('readings.tsv')), links=len(read_tsv('links.tsv')),
    references=len(references), search_groups=len(searches), check_events=len(events),
    checked_source_locators=locators, source_files=len(source_text),
    classes=dict(sorted(Counter(c['class'] for c in claims).items())),
    statuses=dict(sorted(Counter(c['status_on_pages'] for c in claims).items())),
    verdicts=dict(sorted(Counter(e['verdict'] for e in entries).items())),
    event_types=dict(sorted(Counter(e['type'] for e in events).items())),
    intentional_quote_exceptions=['SA13-475','SA13-476'], errors=errors,
    scope='Structural checks only. Mathematical proof and computation scope remains in individual events and proof_audit.md.')
(OUT/'outputs/final_validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
assert not errors, errors
