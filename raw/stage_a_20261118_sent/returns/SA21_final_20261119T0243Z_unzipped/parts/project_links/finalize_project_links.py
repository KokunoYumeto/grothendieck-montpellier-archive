"""Validate endpoint bookkeeping and record source hashes/ordinal conventions.
No mathematics, result status, or target identity is inferred by this program.
"""
from pathlib import Path
import csv, json, hashlib, collections
P=Path(__file__).parent
B=Path('/workspace/scratch/4017236f14bf')
rows=json.loads((P/'project_targets.json').read_text())
notes=B/'sources/notes/pro/MPL_156-1+156-2_notes.md'
source_lines=notes.read_text().splitlines()
for row in rows:
    for occ in row['source_occurrences']:
        n=occ['line']; assert 1<=n<=len(source_lines)
        ordinal=sum(x.startswith('### ') for x in source_lines[:n])
        assert occ['note_id']==f'MPL_156-1+156-2#{ordinal}',(row['id'],occ,ordinal)
assert len(rows)==54
coverage=list(csv.DictReader((P/'context_coverage.tsv').open(),delimiter='\t'))
assert len(coverage)==sum(x.startswith('**Context:**') for x in source_lines)==125
assert all(r['target_ids'] for r in coverage)

def heading_count(path,line):
    lines=path.read_text().splitlines()[:line]
    return {'level3_count':sum(x.startswith('### ') for x in lines),
            'level2_count':sum(x.startswith('## ') for x in lines),
            'levels2_and3_count':sum(x.startswith(('## ','### ')) for x in lines)}
ordinal_checks={
 'MPL147_register_section69':heading_count(B/'prior_context_138/extracted/MPL_147_138-190_notes.md',286),
 'SA21_register_section122':heading_count(notes,943),
}
assert ordinal_checks['MPL147_register_section69']['levels2_and3_count']==69
assert ordinal_checks['MPL147_register_section69']['level3_count']==65
assert ordinal_checks['SA21_register_section122']['levels2_and3_count']==122
assert ordinal_checks['SA21_register_section122']['level3_count']==116
(P/'ordinal_checks.json').write_text(json.dumps(ordinal_checks,indent=2)+'\n')

checked=[
 'sources/notes/pro/MPL_156-1+156-2_notes.md',
 'prior_context/extracted/README.md',
 'prior_context/extracted/notes/RESULTS_STATE.md',
 'prior_context/extracted/DOSSIER_STATEMENTS_WITH_STATUS.md',
 'prior_context/extracted/NEW_RESULTS.md',
 'prior_context/extracted/companion/chunks/DER_XVI.tex',
 'prior_context_138/extracted/README.md',
 'prior_context_138/extracted/notes/RESULTS_STATE.md',
 'prior_context_138/extracted/MPL_147_138-190_notes.md',
]
manifest=[]
for name in checked:
    data=(B/name).read_bytes()
    manifest.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                     'lines':len(data.decode('utf-8-sig').splitlines())})
(P/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
raw=[*sorted(P.glob('*.numbered.txt')),
     *(P/name for name in ['context_navigation.txt','context_navigation.json',
       'narrow_candidates_output.txt','open_missing_candidates_output.txt',
       'secondary_candidates_output.txt'])]
raw_digests=[]
for f in raw:
    data=f.read_bytes()
    raw_digests.append({'path':f.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                        'delivery':'exclude duplicated source excerpts; original paths and search/line locators retained'})
(P/'raw_read_output_manifest.json').write_text(json.dumps(raw_digests,indent=2)+'\n')
(P/'DELIVERY_EXCLUSIONS.txt').write_text('\n'.join(r['path'] for r in raw_digests)+'\n')
out={'validation':'passed','targets':len(rows),
     'status_counts':dict(collections.Counter(r['match_status'] for r in rows)),
     'context_paragraphs':len(coverage),'all_source_note_ordinals_valid':True,
     'ordinal_checks':ordinal_checks,
     'search_file_count':len(json.loads((P/'search_manifest.json').read_text())),
     'check_event_rows':len(list(csv.DictReader((P/'check_events.tsv').open(),delimiter='\t'))),
     'program_outputs_do_not_prove_return_mathematics':True}
(P/'audit_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
