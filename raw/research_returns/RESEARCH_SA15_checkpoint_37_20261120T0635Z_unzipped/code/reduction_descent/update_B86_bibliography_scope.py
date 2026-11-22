from pathlib import Path
from datetime import datetime,timezone
import re,json,hashlib,difflib
own=Path(__file__).resolve().parents[1]
path=own/'reduction_descent.bib';before=path.read_bytes();s=before.decode()
history=own/'notes/B86_bibliography_scope';assert not history.exists();history.mkdir()
additions={
 'Stacks032A':' Fresh B86 read on 20 November 2026: complete Theorem10.160.8 and full proof, including the mixed-characteristic coefficient-ring induction and final surjectivity argument. Root and companion independently reopened and read the same full proof in their complete B86 audits at01:16:53.905061 and01:16:55.519857 UTC. Linked formal-smoothness dependency proofs are not claimed as newly reread.',
 'ColmezCorpsLocaux':' Fresh B86 read on 20 November 2026: complete Proposition2.12 and its tame-uniformizer Hensel proof on printedp11; complete Proposition3.7 and its two-divisibility norm-polynomial proof on printedpp14--15. Opening local-field definition and Section3 hypotheses allow arbitrary perfect residue; no finite-residue hypothesis is imported. Theorem3.10 and Proposition3.13 full proofs were also reread, but B86 uses only the direct quotient-average formula. Root and companion independently reopened and verified these original passages in their complete B86 audits at01:16:53.905061 and01:16:55.519857 UTC.'}
for key,addition in additions.items():
    m=re.search(r'@\w+\{'+key+r',.*?(?=\n@|\Z)',s,re.S);assert m
    entry=m.group(0)
    note=re.search(r'note=\{([^}]*)\}',entry,re.S);assert note
    assert 'Fresh B86 read' not in note.group(1)
    newentry=entry[:note.start(1)]+note.group(1)+addition+entry[note.end(1):]
    s=s[:m.start()]+newentry+s[m.end():]
(history/path.name).write_bytes(before)
(history/'scope.diff').write_text(''.join(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile='bibliography.before',tofile='bibliography.after')))
path.write_text(s)
record={'status':'BIBLIOGRAPHY_SCOPE_UPDATED','actual_utc':datetime.now(timezone.utc).isoformat(),
        'path':str(path),'keys':list(additions),'before_sha256':hashlib.sha256(before).hexdigest(),
        'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'prior_and_diff':str(history),
        'scope':'All older read scopes preserved verbatim; only exact fresh B86 original reads and independent verification appended. No immutable checkpoint30 file changed.'}
(own/'outputs/B86_bibliography_scope_update.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
