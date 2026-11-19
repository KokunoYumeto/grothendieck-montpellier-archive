#!/usr/bin/env python3
"""Retain only bounded target-query/access metadata from the Library check.

Per root's explicit instruction, unrelated fuzzy snippets and file contents are
not included in the deliverable. This script removes them from the temporary
search-response artifacts while preserving the actual requests and result
counts. It performs no Library operations and changes no mathematical data.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'work/integration'
NOW=datetime.now(timezone.utc).isoformat(timespec='seconds')


def unwrap(value):
    while isinstance(value,dict) and 'results' not in value and 'structuredContent' in value:
        value=value['structuredContent']
    return value


batches=[]
for i in range(1,6):
    path=ROOT/f'logs/early_project_library_search_{i:03d}.json'
    raw=json.loads(path.read_text())
    if raw.get('access_metadata_only'):
        batch=raw
    else:
        result=raw['result']
        assert result['status']=='fulfilled'
        body=unwrap(result['value'])
        results=body.get('results') or []
        title_results=body.get('retrieval_title_results') or []
        batch={
            'access_metadata_only':True,
            'batch':i,
            'request':raw['request'],
            'successful_tool_response':not result['value'].get('isError',False),
            'returned_ranked_records':len(results),
            'returned_fuzzy_title_records':len(title_results),
            'continuation_available':bool(body.get('next_cursor')),
            'external_connectors_accessed':body.get('external_connectors_accessed'),
            'resolved_exact_target_count':0,
            'response_assessment':('No exact-title results.' if i<=2 else
                'Returned indirect references in prior prompts or unrelated fuzzy candidates; no named target document itself was resolved.'),
            'full_content_reads':0,
            'preservation_note':'Unrelated fuzzy snippets, file identities and other file contents omitted from deliverable by explicit root instruction. Actual requests and aggregate access outcomes retained.'
        }
        path.write_text(json.dumps(batch,ensure_ascii=False,indent=2)+'\n')
    batches.append(batch)

audit={
    'audit_utc':NOW,
    'scope':'Bounded read-only available-file check for the exact project/context targets named in the SA08 project-link table; not a search for mathematical novelty.',
    'targets':['La Longue Marche','Les Dérivateurs','README.md sections S6/S11','WG2','PATHS A.5/A.6','PRETOT','TOTASPH','hua_project/136.modern.tex','ps_chapters_VI_VII/ps6.tex','notes/RESULTS_STATE.md'],
    'method':'Exact quoted title/filename searches followed once by simpler target-equivalent content/short-name queries. Ranked follow-up results were bounded by top_k20 (or10 for RESULTS_STATE). No broad inventory, archive expansion, other-project investigation, or mathematical import was undertaken.',
    'counts':{'search_calls':len(batches),'query_objects':sum(len(b['request']['search_query']) for b in batches),
              'ranked_records_returned':sum(b['returned_ranked_records'] for b in batches),
              'exact_targets_resolved':0,'target_documents_read':0,'library_mutations':0},
    'conclusion':'The exact external targets were not resolved by this bounded available-file search. This does not establish that they are absent from every location, unindexed archive or other account. The reported cross-project links remain provenance-only leads, with no newly verified second endpoint.',
    'limitations':['Title searches returned no exact matches.','Shorter retries surfaced indirect mentions in prior prompts and unrelated fuzzy results, not the target documents.','Some retry responses exposed continuation cursors; the bounded check did not exhaust those ranked result streams.','Search snippets were not treated as a substitute for reading the cited target passage.','No supplied attachment was opened through Library.'],
    'batches':batches,
    'suggested_prose':'The exact external targets were not resolved by a bounded search of the available files; their reported links therefore remain provenance-only, without a verified second endpoint.',
    'logs':[f'logs/early_project_library_search_{i:03d}.json' for i in range(1,6)]
}
(OUT/'project_access_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
rows=[]
for b in batches:
    for q in b['request']['search_query']:
        rows.append('| '+q['q'].replace('|','\\|')+' | '+('Title/filename' if q.get('search_title_only') else 'Short/content retry')+' | '+str(b['batch'])+' |')
md='''# Bounded project-target access audit

Date: 19 November 2026. Checker: GPT-6 Astra Pro; effort not exposed by runtime; SA08/early.

**Conclusion:** The exact external targets were not resolved by this bounded available-file search. This is an access limit, not evidence that the documents are unavailable everywhere. The reported project links remain provenance-only; no new mathematical implication or two-endpoint result was accepted.

The check covered La Longue Marche, Les Dérivateurs, README sections S6/S11, WG2, PATHS, PRETOT/TOTASPH, and the named `136.modern.tex`, `ps6.tex` and `RESULTS_STATE.md` context files. Exact title/filename searches returned no matches. One simpler retry per target family returned prior prompts mentioning those projects or unrelated fuzzy candidates, not the target documents themselves. Those snippets were not used as source evidence.

There were five search calls and 21 query objects. The ranked retries were deliberately bounded (20,20 and10 records); continuation streams were not exhausted. No target document was read, no attached source was opened through Library, and no Library item was changed. Unrelated snippets and other file contents have been omitted from the retained audit.

| Query | Mode | Batch |
|---|---|---|
'''+ '\n'.join(rows)+'''

Exact request options and aggregate outcomes are retained in `project_access_audit.json` and `logs/early_project_library_search_001.json` through `_005.json`. These are access metadata only.

Suggested dossier sentence: “The exact external targets were not resolved by a bounded search of the available files; their reported links therefore remain provenance-only, without a verified second endpoint.”
'''
(OUT/'project_access_audit.md').write_text(md)
print(json.dumps({'audit_utc':NOW,**audit['counts'],'conclusion':audit['conclusion']},ensure_ascii=False,indent=2))
