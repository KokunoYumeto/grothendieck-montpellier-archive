"""Final coverage and delivery checks. This does not replace mathematical review."""
from pathlib import Path
from collections import Counter
import csv,json,re,hashlib
R=Path(__file__).resolve().parents[2];D=R/'deliverable'
def J(p):return json.loads((D/p).read_text())
def T(p):return list(csv.DictReader((D/p).open(),delimiter='\t'))
issues=[];checks={}
required=['SA13_dossier.md','SA13_entries.tsv','SA13_items.json','SA13_claims.json','SA13_problems.json','SA13_readings.tsv','SA13_links.tsv','SA13_directions.md','SA13_references.bib','CHECK_EVENTS.tsv','progress.log']
for f in required:
 if not (D/f).is_file() or not (D/f).stat().st_size:issues.append('Missing or empty required file: '+f)
base=J('outputs/validation.json')
if not base['passed'] or base['warnings']:issues.append('Assembly validation has unresolved issues or warnings')
items=J('SA13_items.json');claims=J('SA13_claims.json');problems=J('SA13_problems.json')
ids={x['id'] for x in items+claims+problems};aliases={x['alias']:x['canonical'] for x in T('SA13_aliases.tsv')}
valid_ids=ids|set(aliases)
for c in claims:
 if not c['items']:issues.append('Claim without originating item: '+c['id'])
for alias,target in aliases.items():
 if target not in ids:issues.append('Alias target missing: '+alias)
bib=(D/'SA13_references.bib').read_text();bibkeys=set();verification=Counter()
for block in re.split(r'(?m)(?=^@\w+\{)',bib):
 m=re.match(r'@\w+\{([^,]+),',block.strip())
 if not m:continue
 key=m.group(1);bibkeys.add(key)
 n=re.search(r'\bnote\s*=\s*\{(verified|unverified)\}',block)
 if not n:issues.append('Bibliography note not in exact required format: '+key);continue
 verification[n.group(1)]+=1
 if n.group(1)=='verified' and not re.search(r'\b(?:url|doi)\s*=\s*\{[^}]+\}',block):issues.append('Opened bibliography entry lacks URL/DOI: '+key)
for fname in ['SA13_dossier.md','SA13_directions.md']:
 text=(D/fname).read_text()
 for ident in re.findall(r'(?<![A-Za-z0-9-])(?:C-SA13-\d{3}|MP-SA13-\d+|SA13-\d+)',text):
  if ident not in valid_ids:issues.append('Unresolved ID in '+fname+': '+ident)
 for key in re.findall(r'`((?:RC_|P4_|P2_|SGA|Stacks|ILO|Illusie|Koblitz)[A-Za-z0-9_]*)`',text):
  if key not in bibkeys:issues.append('Unresolved bibliography key in '+fname+': '+key)
directions=(D/'SA13_directions.md').read_text()
parts=re.split(r'(?m)^#{2,3}\s+(D\d+[^\n]*)\n',directions)
direction_count=0
for i in range(1,len(parts),2):
 heading,body=parts[i:i+2];direction_count+=1
 for typ,pattern in [('item',r'(?<![A-Z-])SA13-\d+'),('claim',r'C-SA13-\d{3}'),('problem',r'MP-SA13-\d+')]:
  if not re.search(pattern,body):issues.append(heading+' lacks '+typ+' origin')
 for field in ['Interest','First concrete step']:
  if field.lower() not in body.lower():issues.append(heading+' lacks '+field)
if not direction_count:issues.append('No individually ranked directions found')
counts=J('outputs/dossier_counts.json')
if direction_count!=counts['directions']:issues.append('Direction count disagrees with dossier')
events=T('CHECK_EVENTS.tsv');allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
for e in events:
 if e['type'] not in allowed:issues.append('Unexpected check-event type: '+e['type'])
 if 'GPT-6 Astra Pro' not in e['who'] or 'configured effort not exposed' not in e['who']:issues.append('Unexpected model/effort reporting: '+e['who'])
 if not re.fullmatch(r'2026-11-19',e['date']):issues.append('Unexpected event date: '+e['date'])
inventory=J('outputs/source_inventory.json')
for name,digest in inventory['source_sha256'].items():
 p=R/'sources'/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:issues.append('Source changed or missing: '+name)
checks.update(required_files=len(required),source_hashes_checked=len(inventory['source_sha256']),source_scan_occurrences=len(inventory['pages']),entries=base['entries'],items=len(items),claims=len(claims),problems=len(problems),directions=direction_count,bibliography_verification=dict(verification),check_events=len(events),canonical_aliases=len(aliases))
report={'passed':not issues,'checks':checks,'issues':list(dict.fromkeys(issues)),'scope':'Structural coverage, source immutability and delivery consistency only. Mathematical evidence is in the reviewed records, proofs and check events.'}
(D/'outputs/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
