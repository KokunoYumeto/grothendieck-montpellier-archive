"""Align the finalizer's prose with the three observed build attempts."""
from pathlib import Path
w=Path(__file__).resolve().parents[1]
p=w/'code/finalize_checkpoint18.py';s=p.read_text()
old="The subsequent complete build took {build['seconds']} seconds. The first successful and final log contain {len(build['overfull_boxes'])} overfull box, maximum {qa['max_overfull_points']}pt, zero above2pt, and no undefined references, citations or missing glyphs."
new="The first successful build took {initial['seconds']} seconds and had two boxes above2pt, a40.82396pt long bold status and a7.21278pt exact-sequence display. Root actually viewed their original pages243 and245, retained in outputs/checkpoint18_overflow_evidence. The audit explanation was moved into ordinary prose and the display split into two lines, without mathematical change. The final build took {build['seconds']} seconds and contains {len(build['overfull_boxes'])} overfull box, maximum {qa['max_overfull_points']}pt, zero above2pt, and no undefined references, citations or missing glyphs."
assert old in s;s=s.replace(old,new)
s=s.replace("All {paths['referenced_program_paths']} literal printed program paths resolve.","All {paths['referenced_program_paths']} literal printed program paths resolve. Four older texttt references missed by the earlier path-only audit received exact byte-identical aliases; the initial failed path check and repair mapping are retained, and no mathematical program was rerun for this repair.")
p.write_text(s)
print('Finalizer now records the actual first failure, first successful overflows and final clean build.')
