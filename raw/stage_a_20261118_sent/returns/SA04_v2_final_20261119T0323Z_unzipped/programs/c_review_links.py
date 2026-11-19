"""Review root folder-link identifier correspondence, not manuscript mathematics."""
from pathlib import Path
import json,csv,re
root=Path('/workspace/scratch/594d1dc856a9/SA04_work')
part=root/'parts/root'
items={r['id']:r for r in json.loads((part/'items.json').read_text())}
claims={r['id']:r for r in json.loads((part/'claims.json').read_text())}
for row in csv.DictReader((part/'links.tsv').open(),delimiter='\t'):
    if row['kind']!='folder':continue
    print('FROM:',row['from'])
    print('TO:',row['to'])
    print('REGISTER ITEM REFERENCES:',row['note_ids'])
    for token in re.findall(r'C-SA04-\d+(?:/\d+)*',row['from']+' '+row['to']):
        first,*extra=token.split('/')
        for cid in [first]+['C-SA04-'+n for n in extra]:
            if cid not in claims:
                print('  EXTERNAL CLAIM',cid);continue
            c=claims[cid]
            print('  CLAIM:',cid,'cote',c['cote'],'scans',c['scans'],'items',c['items'])
    print()
review='''# Coordinating folder-link identifier review

Date: 19 November 2026. This is an identifier/register consistency check, not a new proof check of source passages not independently read by this subagent.

- The Cartier/Frobenius row names coordinating claims C-SA04-630 and C-SA04-631. Both claim records point to **SA04-623**, cote 93 scan **178**; the earlier link text used scans 179–181 and item SA04-621.
- The universal-vector-extension row names C-SA04-641, C-SA04-643 and C-SA04-644. Their source items are respectively **SA04-629, SA04-630 and SA04-631**, scans 194–198. SA04-628 concerns the preceding étale-trivial rank-one objects.
- The cote 100 folder row correctly uses source items **SA04-639/641** and target items **SA04-654/655** for the named claims.
- The Manin row's coordinating claim C-SA04-620 points to **SA04-617**, scans 156–160, with the identity at scan 159 line 215. Item SA04-618 concerns the following Gauss–Manin construction.
- Its part-C target lies in **cote 93**, not cote 161-5: periods scans 222–230, P93 lines 31–223, items SA04-408–419 and claims C-SA04-402–411; principal parts and operators scans 231–233, lines 224–315, items SA04-420/423/424 and claims C-SA04-412–418. The distinct strict-projective-system assertion C-SA04-417 is at scan 233 lines 308–312.

These replacements were communicated to the coordinating agent. The saved program output records the root table as it stood when inspected; the coordinating agent owns the changes to that table.
'''
(root/'parts/c/root_links_review.md').write_text(review)
print(review)
