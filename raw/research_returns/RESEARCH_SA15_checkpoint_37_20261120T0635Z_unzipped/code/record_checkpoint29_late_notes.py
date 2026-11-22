"""Record completed promotions and separately audited post-freeze work without changing the PDF."""
from pathlib import Path
import datetime,json,hashlib
w=Path(__file__).resolve().parents[1]
record=w/'outputs/checkpoint29_late_notes.json'
assert not record.exists()
text='''
### Exact promotions and separate work after the PDF freeze

The canonical B81 promotion was completed at00:21:31.933277UTC on20November2026; its source SHA256 is db363c4208ce514cd8bc07d8a8f55178461760282a2991548218e047a6030e83. The canonical uniform norm13 promotion followed at00:21:37.481581UTC; its source SHA256 is bd2e45677ef91d1109c433e3e15464b0116241bc10e26a25254d1fd931ce294f. Both were included in the subsequently built and visually verified660-page PDF. These exact records resolve the historical pending-promotion wording above.

The separate B82 candidate concerning nontrivial residual wild inertia passed the complete companion proof/code audit at00:29:58.926559UTC and the complete root audit at00:31:46.620358UTC. A direct determinant congruence replaced an unnecessary square-character/twist argument; the old audited bytes and exact diff are retained. The companion inspected this sole change at00:31:40.413283UTC. Final candidate SHA256 is594f019abab5cd378c489671f7ff021c7e0e446ac53166f696dafa035f0f761b. Its unchanged certificate took0.42271842100308277s in the author run,0.3949265940027544s in the root isolated rerun and0.39488881299621426s in the companion rerun. All mathematical fields agreed and author bytes were preserved. It checks3 symbolic identities,17,664 terminal matrices,1,723,680 outside-line images,23 maximal planes,24 layer rows,71,456 congruence pairs,3,628 integrality rows and35,000 rows each for high-line mismatch and opposite-break recovery. There were no failed executions in these audits. This is a candidate audit retained after the PDF freeze, not a numbered theorem or current-gate promotion in checkpoint29. Its proposed conclusion and exact residual-tame/larger-image limits are in the retained candidate and audits.

Norm17 exploratory sources and outputs are also retained, including a repaired coefficient-extraction failure. Their current necessary x-coordinate conditions leave exceptional moduli and prove no uniform norm17 theorem. The separate quotient/Lie outline for a later ramification step and the twisted cross-Cartier route likewise remain exploratory. None is counted as checkpoint29 main-gate movement.

Further original-source reading is recorded in notes/ROOT_SEARCH_LOG_29.md. The complex general-surface Severi result does not apply to every fixed characteristic-two surface. The generic-curve Prym argument similarly requires a moduli and monodromy hypothesis not supplied by a fixed surface linear system. These are comparison routes, with the actual passages read and unread dependencies distinguished; no result from them was imported into the frozen PDF.
'''
for rel in ['notes/checkpoint29_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(text)
record.write_text(json.dumps({'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Report and provenance only; PDF, canonical mathematics and numbered results unchanged.',
 'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()},indent=2)+'\n')
print(record.read_text())
