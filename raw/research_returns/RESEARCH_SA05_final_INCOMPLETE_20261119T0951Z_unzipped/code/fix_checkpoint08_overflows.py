"""Repair the two observed CP08 first-build overflows without changing proofs."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[1]
path=root/'sections/b1_limit_diagnostics.tex'
old='''The exact finite programs and outputs are
\\texttt{part\\_b/code/kummer\\_limit\\_counterexample.py} and
\\texttt{part\\_b/code/frobenius\\_completion\\_counterexample.py}, with
their correspondingly named \\texttt{.txt} outputs in
'''
new='''The exact finite programs are
\\begin{quote}
\\small
\\path{part_b/code/kummer_limit_counterexample.py}\\\\
\\path{part_b/code/frobenius_completion_counterexample.py}
\\end{quote}
with their correspondingly named \\texttt{.txt} outputs in
'''
text=path.read_text()
assert old in text
path.write_text(text.replace(old,new))
old='''Write $M=\\Hom(H_V,H_S)$ and $N=\\Hom(H_S,H_V)$ for algebraic
homological correspondences. The pairing
'''
new='''For algebraic homological correspondences, put
\\[
 M=\\Hom(H_V,H_S),\\qquad N=\\Hom(H_S,H_V).
\\]
The pairing
'''
for filename in ['sections/part_c.tex','part_c/c4_target_positivity.tex']:
    path=root/filename
    text=path.read_text()
    assert old in text,filename
    path.write_text(text.replace(old,new))
out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),
         initial_overfull_pt=[108.63458,5.84212],
         repairs=['B1 code paths on separate breakable lines',
                  'C4 correspondence spaces moved to a display'],
         mathematical_change=False,final_verification='Recorded separately after rebuilding and visual inspection.')
(root/'code/fix_checkpoint08_overflows_output.json').write_text(json.dumps(out,indent=2)+'\n')
path=root/'RESEARCH_SA05_report.md'
path.write_text(path.read_text()+'''

### Checkpoint08 first-build typesetting repairs

The first expanded build had two overfull horizontal boxes, of 108.63458pt and 5.84212pt. The B1 program paths were put on separate breakable lines, and the C4 pair of correspondence spaces was moved to a display. These changes alter no mathematical claim. Final counts and inspection are recorded in the checkpoint08 verification entry after the corrected build.
''')
print(json.dumps(out,indent=2))
