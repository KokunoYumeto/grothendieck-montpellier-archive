"""Render final count tables without altering any mathematical assessment."""
from pathlib import Path
import json,re,csv,collections
B=Path(__file__).resolve().parents[1];c=json.loads((B/'SA19_counts.json').read_text())
with (B/'SA19_folder_coverage.tsv').open() as f:coverage=list(csv.DictReader(f,delimiter='\t'))
with (B/'SA19_bibliography_audit.tsv').open() as f:bibs=list(csv.DictReader(f,delimiter='\t'))
directions=len(re.findall(r'^### RD-SA19-',(B/'SA19_directions.md').read_text(),re.M))
c['directions']=directions;c['supplied_faces_read']=sum(int(r['faces']) for r in coverage)
c['unverified_reference_records']=sum(r['verification']=='unverified' for r in bibs)
(B/'SA19_counts.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
lines=['| Register | Final count |','|---|---:|',f"| Indexed entries, each assigned exactly once | {c['source_entries']} |",f"| Consolidated items | {c['items']} |",f"| Claim records, including explicitly labelled reconstructions | {c['claim_records']} |",f"| Source-assertion records, including reused material | {c['claim_records']-c['claim_origins']['supplementary reconstruction']} |",f"| Supplementary reconstruction records | {c['claim_origins']['supplementary reconstruction']} |",f"| Problems, open steps and documentary questions | {c['problems']} |",f"| Reading alarms | {c['reading_alarms']} |",f"| Checked folder/publication links | {c['verified_links']} |",f"| Separate external-project lead groups | {c['external_project_leads']} |",'| Separate unread-publication comparison leads | 1 |',f"| Ranked directions | {directions} |",f"| Bibliography records | {c['bibliography_records']} |",f"| Check events | {c['check_events']} |",f"| Supplied transcription faces read | {c['supplied_faces_read']} |",'', 'Entry verdicts: '+ '; '.join(f'**{n} {k}**' for k,n in c['entry_verdicts'].items())+'.','', '| Class | Meaning | All claim records | Source-assertion records only |','|---|---|---:|---:|']
names={'A':'Later own published work','B':'Established development by others','C':'Partial development / exact formulation still qualified','D':'No exact later development located in recorded searches','E':'Earlier or explicitly attributed background','F':'Not sufficiently identifiable'}
for k in names:lines.append(f"| {k} | {names[k]} | {c['claims_by_class'].get(k,0)} | {c['source_claims_by_class'].get(k,0)} |")
lines+=['','| Page status | Count |','|---|---:|']
for k,n in c['claims_by_page_status'].items():lines.append(f'| {k} | {n} |')
lines+=['','| Item kind | Count |','|---|---:|']
for k,n in c['item_kinds'].items():lines.append(f'| {k} | {n} |')
lines+=['','The counts measure adjudicated records, not independent theorems. Several table claims contain separately audited cells, and the problem index includes resolved and false questions. The eight supplementary records are CL-SA19-056, 279–281, 459–460, 465 and 467. Their origin is explicit; they are not attributed to the manuscript.', '',f"Bibliographic URL verification: {c['bibliography_records']-c['unverified_reference_records']} verified and {c['unverified_reference_records']} explicitly unverified. Access depth remains separately recorded. Raw workstream counts precede the five cross-package item merges, one repeated-claim merge and one repeated-problem merge."]
p=B/'SA19_dossier.md';t=p.read_text();t=re.sub(r'<!-- COUNTS_START -->.*?<!-- COUNTS_END -->','<!-- COUNTS_START -->\n'+'\n'.join(lines)+'\n<!-- COUNTS_END -->',t,flags=re.S);p.write_text(t)
print(json.dumps(c,ensure_ascii=False,indent=2))
