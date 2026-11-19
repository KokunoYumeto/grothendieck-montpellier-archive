"""Compile authored English overview and exact register counts; infer no verdicts."""
from pathlib import Path
import json,csv,re,collections,datetime
W=Path(__file__).resolve().parents[1];F=W/'final'
body=(W/'parts/root/dossier_body.md').read_text()
counts=json.loads((W/'outputs/assembly_validation.json').read_text())['counts']
body+='\n## 10. Final register counts\n\nThese counts describe the final consolidated registers. Component audit files retain their earlier local counts as provenance. A status on the pages is distinct from a literature class and from present truth.\n\n'
def table(headers,rows):
 return '| '+' | '.join(headers)+' |\n|'+'|'.join('---' for _ in headers)+'|\n'+''.join('| '+' | '.join(map(str,row))+' |\n' for row in rows)+'\n'
body+=table(['Register','Count'],[(a,counts[k]) for a,k in [('Indexed source entries','entries'),('Consolidated items','items'),('Claim records, including explicit audit refinements','claims'),('Historical problems and questions','problems'),('Undecided scan-reading alarms','readings'),('Links','links'),('Check events','events'),('Bibliography records','references')]]+[('Ranked future directions',30),('Catalogue rows inventoried',30),('Other-part catalogue rows, inventory only',27)])
body+='### Entry verdicts\n\n'
body+=table(['Verdict','Count'],[(v,counts['verdicts'].get(v,0)) for v in ['kept','merged','corrected','withdrawn','rests on a misreading']])
body+='The zero count in the last category does not imply that no mathematical reading alarm exists. The supplied notes often already identify the defect, or their conditional interpretation is retained with a correction.\n\n### Item kinds\n\n'
kinds=['conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other']
body+=table(['Kind','Count'],[(v,counts['item_kinds'].get(v,0)) for v in kinds])
body+='There are 65 transcription-derived or audit-supplement items without invented index rows. The 89 nested cote98 items deliberately repeat their composite parent’s source-entry ID; this does not create extra verdict rows.\n\n### Claims by literature class\n\n'
classes={'A':'Exact assertion in his own published work; attribution and chronology qualified','B':'Developed by others into an established result','C':'Partly developed, or an exact broader scope remains unsupported','D':'Exact development not located after the recorded search','E':'Previously known or standard in the stated setting','F':'Not identifiable as one precise retained theorem'}
body+=table(['Class','Meaning','Count'],[(k,v,counts['claim_classes'].get(k,0)) for k,v in classes.items()])
body+='The three class-D records are C-SA04-659,660,669: the doubtful local-ring effectivity lemma, the uniform-neighbourhood question, and the countable-avoidance lemma. The last has a completed proof in this audit; class D concerns its exact bibliographic match.\n\n### Claims by status on the pages\n\n'
statuses=['proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages']
body+=table(['Status','Count'],[(v,counts['claim_statuses'].get(v,0)) for v in statuses])
body+='The false-as-stated count includes conditional literal readings and reused printed material. It is not a count of certain errors by Grothendieck. Counterexamples and the exact hypotheses they test are given in the corresponding records and proof appendices.\n\n### Links and bibliography\n\n'
body+=table(['Link kind','Count'],[(v,counts['link_kinds'].get(v,0)) for v in ['folder','published work','our projects']])
body+=table(['Reference status','Count'],[(v,counts['reference_verification'].get(v,0)) for v in ['verified','unverified']])
body+='The four unverified original works are Cohen1959, HillePhillips1957, Spencer1969 and RWanderley1981. The Wanderley offprint is supplied evidence; its external reference lacks an opened reliable URL or DOI. The other records distinguish later checked citations from an original text not opened.\n\n'
events=list(csv.DictReader((F/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
body+='### Check events by actual operation\n\n'
body+=table(['Operation','Count'],sorted(collections.Counter(e['type'] for e in events).items()))
body+='Each event’s outcome states its scope. These totals count logged operations, not independent theorems or independent human reviewers.\n'
(F/'SA04_dossier.md').write_text(body)
report={'compiled_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'words':len(body.split()),'source':'parts/root/dossier_body.md','counts_source':'outputs/assembly_validation.json','characters':len(body)}
(W/'outputs/dossier_compilation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
