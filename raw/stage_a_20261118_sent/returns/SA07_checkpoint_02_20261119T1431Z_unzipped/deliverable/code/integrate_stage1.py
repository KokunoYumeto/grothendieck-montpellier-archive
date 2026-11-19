"""Integrate individually authored note verdicts and explicit manual duplicate decisions.

This script checks identity/coverage only. It makes no mathematical or textual verdict.
Run from the restored workspace with the input ZIP extracted to work/ and the
package reader records under agents/. The final dossier retains these records.
"""
import copy,csv,json,re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'deliverable'
sources=[('p15','items_partial.json','entries_partial.tsv'),('p16','items.json','entries.tsv'),('p18','items.json','entries.tsv')]
items=[];entries=[]
for owner,ip,ep in sources:
    folder=ROOT/'agents'/owner
    for x in json.loads((folder/ip).read_text()):
        y=copy.deepcopy(x);y['reader']=owner;items.append(y)
    entries.extend(csv.DictReader((folder/ep).open(),delimiter='\t'))

index=list(csv.DictReader((ROOT/'work/SA07_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected={x['entry_id'] for x in index}
assert len(expected)==len(index)==339
assert len(entries)==339 and {x['entry_id'] for x in entries}==expected
assert len({x['entry_id'] for x in entries})==339
byid={x['id']:x for x in items}
assert len(byid)==len(items)
occ=Counter(s for x in items for s in x['sources'])
assert set(occ)==expected and set(occ.values())=={1},occ
for e in entries: assert e['entry_id'] in byid[e['item_id']]['sources'],e

decisions=json.loads((D/'evidence/manual_merge_decisions.json').read_text())
aliases={};alias_rows=[];merge_events=[]
for m in decisions:
    ids=[m['target']]+m['merge'];members=[byid[x] for x in ids]
    target=byid[m['target']]
    target['source_assessments']=[copy.deepcopy(x) for x in members]
    target['sources']=list(dict.fromkeys(s for x in members for s in x['sources']))
    target['cote']=sorted(set(str(c) for x in members for c in (x['cote'] if isinstance(x['cote'],list) else [x['cote']])),key=int)
    target['scans']=list(dict.fromkeys(str(s) for x in members for s in (x['scans'] if isinstance(x['scans'],list) else [x['scans']])))
    target['lines']=m['locations']
    target['his_words']=' | '.join(x['id']+': '+x['his_words'] for x in members)
    for k in ['statement','reconstruction','check','check_reason']:target[k]=m[k]
    if m['kind']:target['kind']=m['kind']
    target['merge_reason']=m['reason'];target['reader']='root, with package readers'
    for old in m['merge']:
        aliases[old]=m['target'];alias_rows.append([old,m['target'],m['reason']]);del byid[old]
    merge_events.append([m['target'],m['date'],m['reader'],'used and rechecked in this run',
      'Documentary duplicate check: each source note and the cited manuscript passages were read. '+m['reason']+' '+m['check_reason']+' This event is not an independent proof of every external theorem in the item.'])

for e in entries:
    old=e['item_id'];e['item_id']=aliases.get(old,old)
    if old in aliases:
        if e['verdict']=='kept' or e['verdict'].startswith('merged'):e['verdict']='merged'
        e['reason']+=' Root duplicate check: '+old+' is consolidated into '+e['item_id']+'; see manual_merge_decisions.json.'
    elif e['verdict'].startswith('merged'):e['verdict']='merged'
    assert e['verdict'] in ['kept','merged','corrected','withdrawn','rests on a misreading'],e

ordered=sorted(byid.values(),key=lambda x:int(x['id'].split('-')[-1]))
for x in ordered:
    if not isinstance(x['cote'],list):x['cote']=[str(x['cote'])]
    if not isinstance(x['scans'],list):x['scans']=[str(x['scans'])]
    if not isinstance(x['lines'],list):x['lines']=[str(x['lines'])]

entryorder={x['entry_id']:i for i,x in enumerate(index)}
entries.sort(key=lambda x:entryorder[x['entry_id']])
def tsv(path,head,rows):
    with path.open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)

(D/'SA07_items.json').write_text(json.dumps(ordered,ensure_ascii=False,indent=2)+'\n')
tsv(D/'SA07_entries.tsv',['entry_id','item_id','verdict','reason'],[[e[k] for k in ['entry_id','item_id','verdict','reason']] for e in entries])
tsv(D/'SA07_aliases.tsv',['retired_item_id','canonical_item_id','reason'],alias_rows)
tsv(D/'root_records/merge_check_events.tsv',['statement_id','date','who','type','outcome'],merge_events)
report={'entries':len(entries),'input_items':len(items),'manual_merge_families':len(decisions),'absorbed_items':len(aliases),'items':len(ordered),
 'verdicts':dict(Counter(x['verdict'] for x in entries)),'kinds':dict(Counter(x['kind'] for x in ordered)),
 'text_checks':dict(Counter(x['check'] for x in ordered)),'source_coverage':'Every one of the339 index entries occurs once in the verdict table and once among item sources.'}
(D/'evidence/stage1_counts.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
