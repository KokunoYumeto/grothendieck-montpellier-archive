#!/usr/bin/env python3
"""Merge the four SA08 source bibliographies without changing their claim files.

This is a metadata/key audit, not a mathematical proof check. Original input
records and hashes are retained in the machine-readable audit. All references
used by the current agent claims/problems and aggregate output are checked.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
WORK = ROOT / 'work' / 'integration'
WORK.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
NOW = datetime.now(timezone.utc).isoformat(timespec='seconds')
TODAY = NOW[:10]


def braced(text, start):
    assert text[start] == '{'
    depth, i = 1, start + 1
    while i < len(text):
        if text[i] == '\\':
            i += 2
            continue
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if not depth:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError('Unclosed brace at offset ' + str(start))


def parse_bib(text):
    records = []
    pos = 0
    while (match := re.search(r'(?m)^\s*@([A-Za-z]+)\s*\{', text[pos:])):
        start = pos + match.end() - 1
        body, pos = braced(text, start)
        key, body = body.split(',', 1)
        fields, i = {}, 0
        while i < len(body):
            while i < len(body) and (body[i].isspace() or body[i] == ','):
                i += 1
            if i == len(body):
                break
            m = re.match(r'([A-Za-z][A-Za-z_0-9]*)\s*=\s*', body[i:])
            if not m:
                raise ValueError(f'Cannot parse {key}: {body[i:i+80]!r}')
            name, i = m.group(1).lower(), i + m.end()
            if body[i] == '{':
                value, i = braced(body, i)
            elif body[i] == '"':
                j = i + 1
                while j < len(body):
                    if body[j] == '\\':
                        j += 2
                        continue
                    if body[j] == '"':
                        break
                    j += 1
                value, i = body[i+1:j], j+1
            else:
                j = body.find(',', i)
                if j < 0:
                    j = len(body)
                value, i = body[i:j].strip(), j
            if name in fields:
                raise ValueError(f'Duplicate field {key}/{name}')
            fields[name] = value.strip()
        records.append({'type': match.group(1).lower(), 'key': key.strip(), 'fields': fields})
    return records


SPECIAL = {
    'Garvin1998': 'GarvinEtAl1998',
    'SGA7IX': 'SGA7IX1972',
    'BreenMikhailovTouze2016': 'BMT2016',
    'PursuingStacks2021': 'GrothendieckPS1983',
    'SGA4III': 'SGA4XVII',
    'StacksDoldKan': 'Stacks019G',
    'StacksPD': 'Stacks07GK',
}


def canonical(key):
    bare = key[5:] if key.startswith('late_') else key
    return SPECIAL.get(bare, bare)


def refkeys(value):
    keys = set()
    if isinstance(value, list):
        for v in value:
            keys |= refkeys(v)
    elif isinstance(value, dict):
        for k, v in value.items():
            if k == 'refs':
                if isinstance(v, list):
                    assert all(isinstance(x, str) for x in v), repr(v)
                    keys.update(v)
                elif isinstance(v, str):
                    keys.add(v)
                else:
                    raise ValueError('Unexpected refs value: ' + repr(v))
            else:
                keys |= refkeys(v)
    return keys


records, inputs, used_by = [], {}, defaultdict(list)
for role in ['root', 'early', 'middle', 'late']:
    path = ROOT / 'work' / role / 'references.bib'
    raw = path.read_text()
    group = parse_bib(raw)
    inputs[str(path.relative_to(ROOT))] = {
        'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'records': len(group)
    }
    for record in group:
        record['role'] = role
        record['input'] = str(path.relative_to(ROOT))
        records.append(record)
    for name in ['claims.json', 'problems.json']:
        path = ROOT / 'work' / role / name
        data = json.loads(path.read_text())
        for row in data:
            for key in refkeys(row):
                used_by[key].append({'file': str(path.relative_to(ROOT)), 'id': row.get('id', '')})

# Also inspect already-generated aggregate files without modifying them.
aggregate_used = {}
for name in ['SA08_claims.json', 'SA08_problems.json']:
    path = OUT / name
    if path.exists():
        aggregate_used[name] = sorted(refkeys(json.loads(path.read_text())))
        for key in aggregate_used[name]:
            used_by.setdefault(key, [])

all_keys = {r['key'] for r in records} | set(used_by) | set(SPECIAL)
aliases = {k: canonical(k) for k in sorted(all_keys)}
groups = defaultdict(list)
for record in records:
    groups[canonical(record['key'])].append(record)
for key in groups:
    aliases[key] = key
aliases = dict(sorted(aliases.items()))

missing = sorted({canonical(k) for k in used_by} - set(groups))
if missing:
    raise ValueError('Used keys absent from all bibliographies: ' + repr(missing))

merged, conflicts = {}, []
for key, source_records in sorted(groups.items()):
    fields, source_fields, annotations = {}, {}, []
    for record in source_records:
        f = record['fields']
        scope = ' '.join(f[x] for x in ['annotation', 'annote', 'verification_scope'] if f.get(x))
        old_note = f.get('note', '')
        if old_note not in ['verified', 'unverified', '']:
            scope = (scope + ' ' + old_note).strip()
        if scope:
            annotations.append(record['role'].capitalize() + '-package audit: ' + scope)
        for name, value in f.items():
            if name in ['annotation', 'annote', 'verification_scope', 'note']:
                continue
            if name not in fields:
                fields[name] = value
                source_fields[name] = record['input']
            elif fields[name] != value:
                conflicts.append({'key': key, 'field': name, 'chosen': fields[name],
                                  'alternative': value, 'alternative_source': record['input']})
    fields['note'] = 'verified' if any(r['fields'].get('note') == 'verified' for r in source_records) else 'unverified'
    fields['annotation'] = ' '.join(annotations)
    merged[key] = {'type': source_records[0]['type'], 'key': key, 'fields': fields,
                   'source_fields': source_fields}


def override(key, **values):
    if key not in merged:
        raise KeyError(key)
    for name, value in values.items():
        if name == 'entrytype':
            merged[key]['type'] = value
        elif value is None:
            merged[key]['fields'].pop(name, None)
        else:
            merged[key]['fields'][name] = value


# Exact dependency access checks from logs/early_bib_dependencies_*.json.
override('EGAIII', entrytype='article',
    author='Grothendieck, Alexander',
    title='Éléments de géométrie algébrique III: Étude cohomologique des faisceaux cohérents, première partie',
    journal="Publications Mathématiques de l'IHÉS", volume='11', pages='5--167',
    year='1961', doi='10.1007/BF02684273',
    url='https://www.numdam.org/item/PMIHES_1961__11__5_0/', note='verified',
    annotation='Primary Numdam bibliographic record opened during the final reference audit; title, volume, pages, year and DOI verified. Written with the collaboration of Jean Dieudonné. Verification is metadata only. Section 5.4.1 is a dependency named in the opened SGA7 passage; that EGA theorem and its proof were not separately read in this run.')
override('Tate1967', author='Tate, John T.',
    url='https://link.springer.com/chapter/10.1007/978-3-642-87942-5_12',
    doi='10.1007/978-3-642-87942-5_12', editor='Springer, T. A.',
    publisher='Springer', address='Berlin, Heidelberg', note='verified',
    annotation='Publisher chapter and parent-book metadata opened during the final reference audit: pp.158--183, original publication1967, conference1966. The2013 electronic date and2014 softcover date are reissues. Verification is metadata only: the original BU-hosted PDF repeatedly failed to open. Exact full-faithfulness hypotheses used here are checked in opened LevinTate Theorem1.2 p.3 and the SGA7 dependency, not represented as a new reading of Tate original Theorem4.')
override('Atiyah1957', url='https://celebratio.org/Atiyah_MF/article/36/',
    doi='10.2307/1992969', note='verified',
    annotation='The author Complete Bibliography on Celebratio was opened during the final reference audit; entry7 verifies the1957 Transactions article,85(1),181--207, and DOI10.2307/1992969. This is bibliography/metadata verification only. The AMS original PDF and DOI route10.1090/S0002-9947-1957-0086359-5 failed to open. The historical theorem was not read directly; the degree obstruction is proved independently in the late proof memorandum, and BHR2021 provides the opened modern jet/oper comparison. Do not confuse this article with the short1958 conference item of the same title.')
override('Miller1978', url=None, doi=None, note='unverified',
    annotation='Bibliographic identity, Topology17(1978),193--203, is confirmed in the opened original Cartan1976 note added in proof and Garvín et al.1998 reference6. Cartan documents a circulating preprint before December1976; an exact first-circulation date is not established. Original Miller text and publisher metadata were not successfully opened despite title, DOI and primary-site searches. Candidate DOI10.1016/S0040-9383(78)90025-3 and its no-S variant did not resolve here and are not adopted as verified identifiers. No newly read Miller theorem is claimed; precise comparison hypotheses in the dossier rest on Cartan and Garvín. Evidence URL: https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf.')
override('Swan1975', url=None, note='unverified',
    annotation='Bibliographic metadata, Topology14(1975),271--273, is confirmed in the opened Garvín et al.1998 reference9. The original Swan article and publisher metadata were not opened, so this historical lead is marked unverified for original access. Exact comparison assertions in this dossier are supported by the opened Cartan1976 and Sullivan primary texts. Evidence URL: https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf.')
override('Cartier1957', pages='426--428', note='verified',
    annotation='The official IHES author bibliography was opened by middle and independently reopened during final reference integration. Entry3 verifies title, C. R. Acad. Sci. Paris244(1957),426--428. This is bibliographic metadata verification only; the original note was not obtained. The particular polynomial Cartier calculation used in the dossier has an independent proof in the middle mathematical memorandum. No general derived Cartier theorem is inferred from this bibliography check.')

# Remove stale access failures or future promises from shared records; retain the
# exact stronger access scope in the final integrated record, not in every agent.
override('Roby1963', annotation='Primary Numdam metadata and the full original PDF were opened/downloaded by root. The polynomial-law representation in IV.1 p.266 and the free-module invariant-tensor comparison in IV.5 p.272 were followed; exact flat-module statements are also visually checked in SGA4XVII5.5.2.3--5.5.2.8. Late-agent initial PDF failure was superseded by the shared download. This does not automatically check every inhomogeneous super-PD axiom on manuscript scan217, or a general Hom-convolution theorem. Full original: https://www.numdam.org/item/ASENS_1963_3_80_3_213_0.pdf.')
override('GarvinEtAl1998', url='https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf',
    annotation='Full original eight-page article downloaded by late agent and read independently by early and middle agents. Proposition3.2 pp.174--175 gives q-extendability; Remark3.3(i) p.175 shows failure of(q+1)-extendability. Theorem4.2 p.176 applies to any simplicial set over a commutative unital ring in the strict range p<q; q! normalizes integration and is not inverted in the ring. Theorem4.3 wording up to degree q is not used to enlarge the explicit strict bound. Initial403 attempts were superseded by successful download. No separate first-circulation date established.')
override('SGA4XVII', publisher='Springer',
    annotation='Original SGA4III scan downloaded. Late agent visually checked printedpp374--375/PDF377--378, ExposéXVII internalpp123--124, §§5.5.2.3--5.5.2.8: Gamma represents homogeneous polynomial laws, preserves flat modules, equals invariant tensors on flat modules, and satisfies the stated splitting/base-change formulas. Root shorthand SGA4III is canonicalized to this actual chapter source; no claim that the entire volume or every result was read.')
override('Stacks09PF', author='{The Stacks Project Authors}', title='Section 23.6: Tate resolutions',
    annotation='Official tag09PF opened on19November2026. Middle agent read Definition23.6.1 and the even/odd graded extension. Late agent read Definition23.6.5 and its following warning: differential compatibility alone does not imply that divided powers descend through boundaries; Lemma23.6.6 supplies a sufficient case. No reliance is placed on the coefficient-free iteration formula printed in Example23.6.3.')
for key in merged:
    if key.startswith('Stacks'):
        merged[key]['fields']['author'] = '{The Stacks Project Authors}'
        merged[key]['fields']['urldate'] = '2026-11-19'
    if merged[key]['fields'].get('eprint'):
        merged[key]['fields'].setdefault('archiveprefix', 'arXiv')

# Dold audit scope was corrected before integration; guard against stale input.
dold = merged['DoldSteenrod1961']['fields']['annotation']
assert '258--263' in dold and '258--268' not in dold, dold

# Do not turn an opened third-party discussion into a primary research proof.
override('InfiniteHeightMO2022', annotation='The cited MathOverflow discussion was opened as a search lead. It supplies an explicit presentation of an element of infinite height with no coherent divisible subgroup. The presentation, quotient and relevant claims were proved independently in the early proof memorandum; the discussion is not treated as a primary published theorem source or as evidence of novelty.')

FIELD_ORDER = ['author', 'editor', 'title', 'booktitle', 'journal', 'series', 'volume', 'number',
               'publisher', 'institution', 'address', 'year', 'month', 'pages', 'doi',
               'eprint', 'archiveprefix', 'url', 'urldate', 'zbl', 'note', 'annotation']


def render(record):
    f = record['fields']
    names = [x for x in FIELD_ORDER if x in f] + sorted(set(f) - set(FIELD_ORDER))
    return '@' + record['type'] + '{' + record['key'] + ',\n' + ',\n'.join(
        '  ' + ('archivePrefix' if name == 'archiveprefix' else name) + ' = {' + f[name] + '}' for name in names
    ) + '\n}\n'


bib = ('% SA08 integrated bibliography; audit date ' + TODAY + ' UTC.\n'
       '% note verifies access to the cited URL/DOI; annotation states the exact scope.\n'
       '% Metadata verification and theorem-source reading are not independent proof checks.\n'
       '% Original-access failures and unverified historical leads are retained explicitly.\n\n'
       + '\n'.join(render(merged[k]) for k in sorted(merged, key=str.casefold)))
(OUT / 'SA08_references.bib').write_text(bib)
(WORK / 'reference_aliases.json').write_text(json.dumps(aliases, ensure_ascii=False, indent=2) + '\n')

# Round-trip checks are limited to actual risks: balanced syntax, unique keys,
# required note values, missing used citations, and URLs on verified records.
roundtrip = parse_bib(bib)
assert len(roundtrip) == len(merged)
assert len({r['key'] for r in roundtrip}) == len(merged)
for record in roundtrip:
    assert record['fields']['note'] in ['verified', 'unverified']
    assert record['fields'].get('annotation'), record['key']
    if record['fields']['note'] == 'verified':
        assert record['fields'].get('url') or record['fields'].get('doi'), record['key']

# Bibliographic verification events: these report what was actually checked,
# not a proof of a reference's mathematical theorem. Full theorem-use events
# remain in each agent's CHECK_EVENTS.tsv and are independently merged by root.
event_rows = []
for key in sorted(merged):
    record = merged[key]
    f = record['fields']
    roles = sorted({r['role'] for r in groups[key]})
    if key in ['EGAIII', 'Tate1967', 'Atiyah1957', 'Cartier1957']:
        roles.append('early final integration (new metadata open)')
    event_rows.append({
        'statement_id': key,
        'date': TODAY,
        'who': 'GPT-6 Astra Pro; effort not exposed by runtime; SA08/early bibliography integration',
        'type': 'used and rechecked in this run' if f['note'] == 'verified' else 'carried as background without fault found',
        'outcome': ('Bibliography integration and key/metadata audit only; no new proof check. '
                    + ('Access verification recorded by ' + ', '.join(roles) + ' source audits. ' if f['note'] == 'verified' else 'Original access or precise bibliographic identity remains unverified as specified. ')
                    + f['annotation'])
    })
with (WORK / 'REFERENCE_CHECK_EVENTS.tsv').open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=['statement_id', 'date', 'who', 'type', 'outcome'], delimiter='\t')
    writer.writeheader()
    writer.writerows(event_rows)

audit = {
    'generated_utc': NOW,
    'purpose': 'Canonical bibliography and citation-key audit; not a mathematical proof check.',
    'inputs': inputs,
    'counts': {'input_records': len(records), 'canonical_records': len(merged),
               'aliases': len(aliases), 'used_input_keys': len(used_by),
               'used_canonical_keys': len({canonical(k) for k in used_by}),
               'verified': sum(r['fields']['note'] == 'verified' for r in merged.values()),
               'unverified': sum(r['fields']['note'] == 'unverified' for r in merged.values()),
               'reference_events': len(event_rows)},
    'used_by': dict(sorted(used_by.items())),
    'aggregate_used_keys_at_audit': aggregate_used,
    'missing_used_references': missing,
    'unverified': [k for k in sorted(merged) if merged[k]['fields']['note'] == 'unverified'],
    'metadata_field_differences': conflicts,
    'input_records': records,
    'canonical_records': merged,
    'additional_access_logs': ['logs/early_bib_dependencies_opens.json', 'logs/early_bib_dependencies_search.json',
                               'logs/early_bib_dependencies_follow.json', 'logs/early_bib_dependencies_metadata.json',
                               'logs/early_bib_cartier_metadata.json'],
    'checks': {'balanced_bibtex_roundtrip': True, 'unique_keys': True,
               'all_used_keys_resolved': not missing, 'verified_entries_have_url_or_doi': True,
               'annotations_retained': True, 'Dold_scope_258_263': True},
}
(WORK / 'reference_audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: audit[k] for k in ['generated_utc', 'counts', 'missing_used_references', 'unverified', 'checks']}, ensure_ascii=False, indent=2))
