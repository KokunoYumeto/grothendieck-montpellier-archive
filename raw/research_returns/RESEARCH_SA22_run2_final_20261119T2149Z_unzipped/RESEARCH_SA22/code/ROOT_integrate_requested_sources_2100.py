#!/usr/bin/env python3
"""Integrate five precisely scoped access entries and a checked Kleiman citation.

This is source-record maintenance, not a mathematical gate change. Original
bytes are preserved, and the script refuses duplicate or unexpected edits.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import time

root=Path(__file__).resolve().parents[1]
started=datetime.now(timezone.utc)
timer=time.perf_counter()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bib=root/'ROOT_references.bib'
part=root/'sections/part_B.tex'
text=bib.read_text()
bproposal=(root/'notes/B_Lieberman_Kleiman1994_sources.md').read_text()
blocks=re.findall(r'```bibtex\n(.*?)\n```',bproposal,re.S)
assert len(blocks)==1
bentries=blocks[0]
letter=(root/'notes/A567_Knudsen_sign_access_entries.bib').read_text()
sga=r'''
@book{ROOT_SGA45_1977,
 author={Deligne, Pierre},
 title={Cohomologie {\'e}tale ({SGA} 4{\textonehalf})},
 series={Lecture Notes in Mathematics},volume={569},
 publisher={Springer},year={1977},
 url={https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf},
 note={Opened, limited scope: original 316-page scan acquired. PDF pp. 1--7 were actually read: title, introduction printed pp. III--IV, contents, and the complete guide Un fil d'Ariane, printed pp. 1--3. The cover names Deligne with Boutot, Grothendieck, Illusie and Verdier as collaborators. No body exposition or full-volume reading is claimed, and no theorem is imported from the front matter. Exact receipt and scope: notes/ROOT\_SGA45\_SGA5\_source\_audit.md}
}

@book{ROOT_SGA5_1977,
 author={Grothendieck, Alexander},
 editor={Illusie, Luc},
 title={Cohomologie {$\ell$}-adique et fonctions {$L$} ({SGA} 5)},
 series={Lecture Notes in Mathematics},volume={589},
 publisher={Springer},year={1977},
 url={https://library.slmath.org/nonmsri/sga/sga5/SGA5.pdf},
 note={Opened, limited scope: original 496-page scan acquired. PDF pp. 1--9 and 11--12 were actually read: title and copyright, complete introduction printed pp. III--VII, bibliography p. VIII, SGA list p. IX, and contents/dependency diagram pp. XI--XII. The original explicitly identifies Grothendieck as director and Illusie as editor. No complete mathematical exposition or full-volume reading is claimed, and no theorem is imported from this front-matter audit. Exact receipt and scope: notes/ROOT\_SGA45\_SGA5\_source\_audit.md}
}
'''
addition=bentries+'\n\n'+sga+'\n'+letter
keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',addition)
assert len(keys)==5 and len(set(keys))==5
for key in keys:
    assert not re.search(r'@\w+\s*\{\s*'+re.escape(key)+r'\s*,',text),key
old=r'Opened: complete original 37-page publisher PDF acquired. Original printed pp. 19--23 and 40--43 were visually read, including the graded-line definitions, strict diagram qualification, Definition 4 and Theorem 2. The remaining pages and full dependency proofs were not read in this follow-up. Requested background only; no determinant theorem from this source is used as a proof input in Parts C.1--C.2. Exact access and reading scope is recorded in notes/ROOT\_Knudsen\_Raynaud\_source\_audit.md'
new=r'Opened: the complete original article, all 37 printed pages 19--55, was directly read from page images by the algebra agent, completed 19 November 2026 at 20:54:37 UTC. This later full reading supersedes, without erasing, the earlier selected-page reading record. It includes the source proof text and explicit omissions, not a claim that all external dependencies were reopened. The strict-diagram qualification on p. 41 and restrictions on ordinary derived triangles on pp. 43--46 remain essential. The printed sign on p. 20, unrestricted ordinary base-change assertion on p. 46 and scalar/trace-zero decomposition on p. 52 are separately checked with explicit corrections. No determinant theorem from this source is used as a proof input in Parts C.1--C.2. Exact full scope: notes/C\_KnudsenMumford1976\_full\_reading.md'
assert text.count(old)==1
newtext=text.replace(old,new,1).rstrip()+'\n\n'+addition.strip()+'\n'
parttext=part.read_text()
anchor=r"Lieberman's Lefschetz theorem for abelian varieties, as recorded in Kleiman \cite[Theorem 2A11]{BKleiman1968}, makes the algebraic Lefschetz decomposition available."
replacement=anchor+r" The later original account also gives this input in Kleiman \cite[Theorem~4-1 and Proposition~4-3(2)(c), pp.~14--16]{BKleiman1994}; its Proposition~5-1, p.~17, formulates the positivity implication on homological algebraic classes."
assert parttext.count(anchor)==1
partnew=parttext.replace(anchor,replacement,1)
history=root/'notes/requested_source_integration_before'
assert not history.exists()
history.mkdir()
before={str(p.relative_to(root)):sha(p) for p in (bib,part)}
for p in (bib,part):
    dest=history/p.relative_to(root)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(p.read_bytes())
bib.write_text(newtext)
part.write_text(partnew)
record={
 'started_utc':started.isoformat(),
 'finished_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-timer,
 'added_keys':keys,
 'updated_reading_scope':'ROOT_KnudsenMumford1976',
 'citation_added_at':'sections/part_B.tex, proof of B:abelian',
 'source_hashes_before':before,
 'source_hashes_after':{str(p.relative_to(root)):sha(p) for p in (bib,part)},
 'gate_movement':False,
 'publication':'Fresh bibliography merge, build and actual visual QA required.'
}
(root/'logs/ROOT_requested_source_integration_2100.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
