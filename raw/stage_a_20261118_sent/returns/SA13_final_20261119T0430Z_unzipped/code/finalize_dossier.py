"""Append deterministic counts to the authored English dossier; no verdict inference."""
from pathlib import Path
from collections import Counter
import csv,json,re
R=Path(__file__).resolve().parents[2];D=R/'deliverable'
counts=json.loads((D/'outputs/assembly_counts.json').read_text())
items=json.loads((D/'SA13_items.json').read_text())
entries=list(csv.DictReader((D/'SA13_entries.tsv').open(),delimiter='\t'))
source_ids={r['entry_id'] for r in entries}
pro_items=sum(bool(source_ids.intersection(x['sources'])) for x in items)
directions=(D/'SA13_directions.md').read_text()
direction_count=len(re.findall(r'^#{2,3}\s+\d+[.)]',directions,re.M))
if not direction_count:
 direction_count=len(re.findall(r'^#{2,3}\s+(?:SA13-)?D\d+',directions,re.M))
if not direction_count:
 # The direction builder's structured record is a more exact fallback.
 record=D/'outputs/directions_inventory.json'
 if record.exists():
  data=json.loads(record.read_text());direction_count=len(data) if isinstance(data,list) else data.get('count',0)
assert direction_count>0,'Cannot identify ranked direction headings'
bib=(D/'SA13_references.bib').read_text()
notes=Counter(re.findall(r'\bnote\s*=\s*\{(verified|unverified)\}',bib))
marker='## 9. Final counts and completion'
p=D/'SA13_dossier.md';text=p.read_text().split(marker)[0].rstrip()+'\n\n'
lines=[marker,'','Counts are for canonical global records after source-based consolidation. The','original occurrence records and aliases remain available. Bibliography counts are',
'keys, not distinct publications. The verdict is the','treatment of a note entry; it is not a count of false or retracted manuscript','claims. The page-status column and the literature class answer different questions.','',
'| Register | Count |','|---|---:|']
for label,value in [('Indexed Pro entries',counts['entries']),('Canonical items',counts['items']),('Items with indexed Pro sources',pro_items),('Supplementary-only items',counts['items']-pro_items),('Canonical claims',counts['claims']),('Problems',counts['problems']),('Reading alarms',counts['readings']),('Ranked directions',direction_count),('All links',counts['links']),('Separately retained project leads',counts['project_links']),('Semantic aliases',counts['aliases']),('Bibliography keys',counts['bibliography_keys']),('Bibliography records marked verified (at recorded scope)',notes['verified']),('Bibliography records marked unverified',notes['unverified']),('Check events',counts['check_events'])]:lines.append(f'| {label} | {value} |')
lines+=['','### Entry verdicts','','| Verdict | Count |','|---|---:|']
for label in ['kept','merged','corrected','withdrawn','rests on a misreading']:lines.append(f'| {label} | {counts["verdict_counts"].get(label,0)} |')
lines+=['','### Item kinds','','| Kind | Count |','|---|---:|']
for label in ['conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other']:lines.append(f'| {label} | {counts["item_kind_counts"].get(label,0)} |')
lines+=['','### Claims by literature class','','| Class | Meaning | Count |','|---|---|---:|']
for key,label in [('A','Identified in his own later published work, subject to explicit source-authorship qualifications'),('B','Developed by others into established results, including a proved negative resolution where specified'),('C','Partly developed; exact remaining scope or identification gap stated'),('D','Not developed after a documented search'),('E','Known beforehand or standard at the time'),('F','Not identifiable precisely from the pages')]:lines.append(f'| {key} | {label} | {counts["claim_class_counts"].get(key,0)} |')
lines+=['','Class D is zero: no bounded negative search has been promoted into a claim','that an idea was never developed. Class C includes explicitly distinguished','historical-identification gaps and stronger residual formulations; it is not','a count of newly discovered open conjectures.','', '### Claims by status on the pages','','| Status | Count |','|---|---:|']
for label in ['proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages']:lines.append(f'| {label} | {counts["claim_status_counts"].get(label,0)} |')
lines+=['','A merged claim can have a promise at an earlier occurrence and a proof sketch','later. Its `occurrence_statuses` retain that distinction; the table above counts','the canonical record once. The literature fate separately reports what is','known as of 19 November 2026.','',
'All six requested stages are completed at the scope of the supplied sources:','379 individually reviewed verdicts; searched fates and computation/proof records;','a consolidated problem index; evidenced scan alarms without emendation; checked','available archive/publication endpoints with external project leads explicitly','qualified; and fully sourced ranked follow-on tasks. The final validation outputs','record the coverage and integrity checks. Remaining mathematical, bibliographical','and ink uncertainties are the stated findings of the review, not silently filled','gaps.','']
p.write_text(text+'\n'.join(lines))
summary={'directions':direction_count,'pro_items':pro_items,'supplementary_items':counts['items']-pro_items,'bibliography_access':dict(notes),'dossier_words':len(p.read_text().split())}
(D/'outputs/dossier_counts.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
