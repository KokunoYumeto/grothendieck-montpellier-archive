"""Restore statement-label aux input while removing only invalid natbib date entries."""
from pathlib import Path
import datetime,difflib,json
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP36_layout_repair'
original=(folder/'RESEARCH_SA15_paper.aux').read_text()
lines=original.splitlines(True)
bad=[x for x in lines if 'NAT@force@numbers' in x or '\\bibcite{KleimanPicardScheme}' in x]
assert len(bad)==2
new=''.join(x for x in lines if x not in bad)
(w/'RESEARCH_SA15_paper.aux').write_text(new)
(folder/'aux_restore.diff').write_text(''.join(difflib.unified_diff(lines,new.splitlines(True),fromfile='failed_aux',tofile='restored_label_aux')))
r={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'preserved_failure':'outputs/checkpoint36_prepare_attempt02.stdout.txt and .stderr.txt',
 'reason':'The preparation pipeline reads the preceding aux for statement numbering before the TeX build. Removing the entire generated aux therefore failed during preflight, before any second build attempt. Restore its exact statement labels while dropping only the invalid empty-year bibliography entry and its NAT@force@numbers line.',
 'removed_exact_lines':bad,'new_mathematics':False,'second_TeX_attempt_yet_started':False}
(folder/'aux_restore_record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
