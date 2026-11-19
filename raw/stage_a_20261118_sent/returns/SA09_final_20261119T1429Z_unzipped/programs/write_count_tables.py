#!/usr/bin/env python3
"""Render the reconciled counts, without assigning or changing any verdict."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'counts.json').read_text())
def table(head,rows):
 return '| '+ ' | '.join(head)+' |\n|'+ '|'.join('---' for _ in head)+'|\n'+''.join('| '+' | '.join(map(str,row))+' |\n' for row in rows)
out=[]
out.append(table(['Measure','Count'],[
 ('Indexed source entries',c['entries']),('Canonical items',c['items']),
 ('Canonical claim records',c['claims']),('Problems',c['problems']),
 ('Readings awaiting images',c['readings']),('Ranked global directions',c['directions']),
 ('Checked correspondence rows',c['links']),('Original project-lead inventory rows',c['reported_project_leads']),
 ('Bibliographic records',c['references']),('Check events',c['check_events'])]))
out.append('The 216 canonical claim records include one explicitly identified Sullivan-insert provenance record (CL-SA09-137-052). Thus 215 records concern Grothendieck\'s manuscript assertions, computations or identifiable programmes; the provenance record is not credited as his original theorem. The fifth, unindexed packet contributes claims and problems but no invented verdict rows. Six item identifiers and one duplicate claim identifier are retired through explicit aliases, leaving all original component records recoverable.\n')
out.append('#### Entry verdicts\n\n'+table(['Verdict','Count'],[(k,c['verdicts'].get(k,0)) for k in ['kept','merged','corrected','withdrawn','rests on a misreading']]))
out.append('A zero in the last row does not mean that no mathematical reading alarm was found: without the scans, suspected readings remain conditional. Their evidence is retained in the 173-row reading register. Corrected and withdrawn verdicts retain their original reasons and source locations.\n')
out.append('#### Item kinds\n\n'+table(['Kind','Count'],[(k,c['item_kinds'].get(k,0)) for k in ['conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other']]))
class_names={'A':'In his own later published work','B':'Developed by others into established results','C':'Partly developed; exact limitation recorded','D':'No development located after the stated search','E':'Known before the manuscript context','F':'Not identifiable at the required precision'}
out.append('#### Claims by literature class\n\n'+table(['Class','Meaning','Count'],[(k,class_names[k],c['claim_classes'].get(k,0)) for k in 'ABCDEF']))
out.append('Classes concern development and provenance, not truth. In particular, class A may record a later published continuation of a programme without claiming that every hoped-for theorem was proved; class C may contain a refuted broad statement with a valid restricted result. First circulation and publication dates remain distinct in the individual records.\n')
out.append('#### Claims by status on the pages\n\n'+table(['Reporting group','Count'],[(k,c['claim_status_groups'].get(k,0)) for k in ['proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','not identifiable']]))
out.append('`claim_status_groups.tsv` gives the explicit, individually reviewed grouping used only for these counts. The complete `status_on_pages` string remains unchanged in every claim. Thus conditional failures under a literal reading remain conditional; a construction stated to work is grouped with statements without proof; and the single isolated fragment that cannot be formulated is listed separately. The 40 records grouped as false as stated include qualified or reading-dependent failures and are not 40 unconditional judgments about the autograph.\n')
body='\n'.join(out)
p=R/'SA09_dossier.md';s=p.read_text()
start='<!-- BEGIN COUNT TABLES -->';end='<!-- END COUNT TABLES -->'
if '{{COUNT_TABLES}}' in s:s=s.replace('{{COUNT_TABLES}}',start+'\n'+body+'\n'+end)
elif start in s:s=s[:s.index(start)]+start+'\n'+body+'\n'+end+s[s.index(end)+len(end):]
else:raise ValueError('No count-table insertion point')
p.write_text(s)
print(json.dumps({'entries':c['entries'],'items':c['items'],'claims':c['claims'],'directions':c['directions'],'status_total':sum(c['claim_status_groups'].values()),'check_events':c['check_events']},indent=2))
