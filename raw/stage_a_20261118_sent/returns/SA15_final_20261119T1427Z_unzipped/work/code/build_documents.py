"""Assemble the authored English narrative and ranked task list.

Only ID transport, heading levels and exact count tables are automated.
The prose, priorities and mathematical judgments were written by the readers.
"""
from pathlib import Path
from collections import Counter
import json,re,csv
B=Path(__file__).resolve().parents[2];W=B/'work';D=B/'deliverables'
ids=json.loads((D/'SA15_id_map.json').read_text())
stats=json.loads((D/'SA15_counts.json').read_text())
def remap(text,package=None):
 if package:
  text=re.sub(r'(?<![A-Za-z0-9_-])([IC]\d{3}|P0\d{2})(?!\w)',lambda m:package+'-'+m.group(),text)
 def sub(m):
  assert m.group() in ids,('Unknown authored reference',m.group())
  return ids[m.group()]
 return re.sub(r'P(?:56|67|78|894)-[ICP]\d{3}',sub,text)
def package_prose(folder,pref):
 s=(W/folder/'narrative.md').read_text()
 s=s.split('\n',1)[1].lstrip()
 if pref=='P56':s=s[s.index('## Cote 5:'):]
 s=re.sub(r'(?m)^## ', '### ',s)
 return remap(s,pref)
def table(title,counts,order=None):
 a=['### '+title,'','| Category | Count |','|---|---:|']
 for k in order or sorted(counts):a.append('| '+k+' | '+str(counts.get(k,0))+' |')
 a+=['| **Total** | **'+str(sum(counts.values()))+'** |','']
 return '\n'.join(a)
counts=['| Record | Final count |','|---|---:|',
 f"| Supplied indexed entries, each adjudicated once | {stats['indexed_entries']} |",
 f"| Additional in-scope note entries, each adjudicated once | {stats['supplementary_in_scope_entries']} |",
 f"| Total entry verdicts | {stats['indexed_entries']+stats['supplementary_in_scope_entries']} |",
 f"| Consolidated items | {stats['items']} |",
 f"| Claims, including explicitly labelled refinements and earlier-note checks | {stats['claims']} |",
 f"| Claims with a recorded fate search | {stats['claims_with_search_evidence']} |",
 f"| Problems, including resolved and withdrawn questions | {stats['problems']} |",
 f"| Undecided mathematical reading alarms | {stats['readings']} |",
 f"| Links with both endpoints checked | {stats['verified_links']} |",
 f"| Separate unverified endpoint leads | {stats['unverified_link_leads']} |",
 f"| Named external-project leads found in supplied in-scope notes | {stats['project_leads']} |",
 f"| Ranked directions | {stats['directions']} |",
 f"| Bibliographic keys | {stats['references']} |",
 f"| Keys with a verified opened URL/DOI | {stats['verified_references']} |",
 f"| Check events | {stats['check_events']} |",
 f"| Cote 100 entries inventoried outside the topic | {stats['excluded_cote100_entries']} |",'']
verdict_order=['kept','merged','corrected','withdrawn','rests on a misreading']
counts+=['### Verdicts','','| Verdict | Supplied index | Supplementary entries | Total |','|---|---:|---:|---:|']
for k in verdict_order:
 a=stats['indexed_verdicts'].get(k,0);b=stats['supplementary_verdicts'].get(k,0)
 counts.append(f'| {k} | {a} | {b} | {a+b} |')
counts+=['',table('Items by kind',stats['item_kinds']),
 table('Claims by fate class',stats['claim_classes'],['A','B','C','D','E','F']),
 table('Claims by documentary-status census',stats['claim_status_census'],
 ['proved there','proof sketched','stated without proof','corrected or withdrawn by himself',
 'false as stated','open on the pages','mixed or conditional page status','insufficient text','present-run refinement']),
 table('Claim-record provenance',stats['claim_origin_census'])]
counts+=['The provenance categories describe the records, not publication-priority claims. '
 f"The {stats['claim_origin_census']['present-run refinement']} present-run refinements include precise restatements of some earlier-run diagnostics. "
 'The status bucket “insufficient text” comprises nine earlier-run-only records that have no '
 'historical page-proof status and three inadequately identified manuscript statuses. '
 'It does not mean twelve missing source passages. The separate modern-validity column in '
 '`SA15_status_census.tsv` retains refutations of documentary-open or retracted assertions.', '']
counts.append(f"The item count is {stats['raw_items']} independently curated records minus three "
 'cross-package identity overlaps. The claim count is '
 f"{stats['raw_claims']} raw records minus two overlapping parts of the continuous co-Lie "
 f"calculation. All {stats['raw_problems']} precise problem formulations remain separate "
 'after cross-review; related questions are linked without being identified merely '
 'because they share a technique or later reference.')
counts.append('')
front=(W/'dossier_front.md').read_text().replace('{{P56_NARRATIVE}}',package_prose('cotes5_6','P56')).replace('{{P67_NARRATIVE}}',package_prose('cotes6_7','P67'))
middle=(W/'root_narrative.md').read_text().replace('{{P894_NARRATIVE}}',(W/'c894_narrative.md').read_text())
back=(W/'dossier_back.md').read_text().replace('{{COUNTS}}','\n'.join(counts))
dossier=remap(front+'\n'+middle+'\n'+back)
dossier=dossier.replace('DeJong1993','deJong1993')
assert '{{' not in dossier
(D/'SA15_dossier.md').write_text(dossier)
directions=remap((W/'directions_draft.md').read_text())
assert len(re.findall(r'(?m)^## \d+\.',directions))==stats['directions']
(D/'SA15_directions.md').write_text(directions)
(D/'progress.log').write_text((W/'progress.log').read_text())
print(json.dumps({'dossier_words':len(dossier.split()),'directions_words':len(directions.split()),
 'directions':stats['directions'],'items':stats['items'],'claims':stats['claims'],
 'problems':stats['problems']},ensure_ascii=False))
