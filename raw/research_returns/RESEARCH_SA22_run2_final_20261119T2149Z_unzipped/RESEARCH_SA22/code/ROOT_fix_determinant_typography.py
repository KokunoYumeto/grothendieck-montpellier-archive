#!/usr/bin/env python3
"""Split the two unbreakable certificate filenames; preserve the audited proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time

root=Path(__file__).resolve().parents[1]
start=datetime.now(timezone.utc)
clock=time.perf_counter()
path=root/'notes/C_KnudsenMumford_sign_fragment.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(path)=='d6dbc83a97741ade21f2ab4efd93e42eda483309629989b771db5a60052fa3ac'
old=r'''The exact certificates \texttt{C\_determinant\_scope\_certificate.py}
and \texttt{C\_trace\_invariance\_certificate.py} record, respectively,
35 and 22 passing assertions: the explicit derived-tensor dimensions
and 16-matrix trace example, then all 16 simultaneous-centralizer
cases.  They do not replace the general proofs above.'''
new=r'''Two further exact certificates supplement these proofs:
\begin{itemize}
\item \path{code/C_determinant_scope_certificate.py} records
35 passing assertions for the explicit derived-tensor dimensions and
the 16-matrix trace example.
\item \path{code/C_trace_invariance_certificate.py} records
22 passing assertions, including all 16 simultaneous-centralizer cases.
\end{itemize}
The certificates do not replace the general proofs above.'''
text=path.read_text()
assert text.count(old)==1
backup=root/'notes/determinant_typesetting_before/C_KnudsenMumford_sign_fragment.tex'
assert not backup.exists()
backup.parent.mkdir()
backup.write_bytes(path.read_bytes())
before=sha(path)
path.write_text(text.replace(old,new,1))
audit=root/'notes/ROOT_determinant_integration_audit.md'
with audit.open('a') as out:
    out.write('\n## Subsequent typesetting-only correction\n\n'
              'The first integrated build exposed one80.84181pt overflow on PDFpage159, '
              'caused by placing two unbreakable certificate filenames in one paragraph. '
              'Root split their descriptions into separate list entries, with breakable paths. '
              'All five statement/proof blocks are unchanged. The exact frozen proposal '
              'bytes are retained at `notes/determinant_typesetting_before/'
              'C_KnudsenMumford_sign_fragment.tex`; the live included fragment now has '
              'this typography correction. The first build and its failed publication '
              'gate remain in `logs/build_runs/20261119T211052Z/`. '
              'A fresh build and actual inspection are required.\n')
record={'started_utc':start.isoformat(),'finished_utc':datetime.now(timezone.utc).isoformat(),
        'elapsed_seconds':time.perf_counter()-clock,'source_sha256_before':before,
        'source_sha256_after':sha(path),'backup':str(backup.relative_to(root)),
        'overflow_before_pt':80.84181,'overflow_before_pdf_page':159,
        'scope':'Certificate-path line breaking only; no mathematical statement, proof or execution count changed.'}
(root/'logs/ROOT_determinant_typography_fix.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
