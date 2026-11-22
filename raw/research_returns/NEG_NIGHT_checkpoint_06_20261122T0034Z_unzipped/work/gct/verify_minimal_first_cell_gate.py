"""Exact projection of the complete NN-G035 necessary mass certificate.
The arbitrary-degree irreducibility and polynomial exclusions are NN-G036.
"""
from pathlib import Path
import json

source=json.loads(Path('work/gct/closed_mass_gate_2744_certificate.json').read_text())
removed=[r for r in source['bases'] if r['g1']==64]
rows=[r for r in source['bases'] if r['g1']>64]
assert len(removed)==5 and len(rows)==38
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in rows)==348
triples=sorted({(r['g1'],r['d1'],r['u1']) for r in rows})
assert len(triples)==20 and min(r['score_min'] for r in rows)==1932
out={'removed_g1_64_base_rows':5,'remaining_base_rows':38,
     'remaining_auxiliary_increment_pairs':348,'first_cell_mass_triples':triples,
     'necessary_closed_table_score_lower_bound':1932,
     'known_actual_closed_table_score_upper_bound':2744,
     'scope':'Finite projection only; NN-G036 proves why every removed actual branch is the2744 attainer. No realizability asserted for remaining mass data.'}
Path('work/gct/minimal_first_cell_gate_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
