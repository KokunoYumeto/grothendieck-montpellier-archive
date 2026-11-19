"""Serialize two checks actually performed during the independent final audit."""
from pathlib import Path
import csv,json

P=Path(__file__).parent
who='GPT-6 Astra Pro; inherited effort not separately exposed; /root/cotes_156_8_9 final independent audit'
rows=[
 dict(statement_id='Birkhoff1948',date='2026-11-19',who=who,
      type='used and rechecked in this run',
      outcome='Rechecked the primary-book chapter heading and exact polarity/Galois sections in the supplied reader cache: parts/cotes_3_5/outputs/birkhoff1948.txt:3855–3857,4234–4389,4886–4887. Correct locator is Chapter IV, not V; IV §5 Theorem9 and Corollary pp54–56, §6 Theorem10 p56. The null-element convention is explicit at4322–4324. Corrected this part’s authoritative curation, generated records, bibliography, narrative and proof audit. This is a locator/source-scope check, not a new proof of the whole book.'),
 dict(statement_id='C-SA21-9-054',date='2026-11-19',who=who,
      type='targeted proof check',
      outcome='Directly read J156-9-12_transcription.tex:242–355 (IX95–97), compared the inserted generator equality at253–257 with its explicit acknowledgment at351–355, and checked the corrected equivalence for arbitrary set-valued correspondences. Orthogonality-fiber closure supplies the pretranspose; testing perpendiculars gives all-subset closure commutation; joins plus generator equality recover that formula, including the empty subset. Details in parts/final_audit/assessment.md §6. Join preservation alone and complement preservation remain distinct. Earlier question MP-SA21-9-08 is updated without changing its original source statement.')
]
with (P/'supplemental_check_events.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
print(json.dumps({'supplemental_events':len(rows),'statement_ids':[r['statement_id'] for r in rows],
                  'scope':'one primary locator check; one targeted check of the corrected IX proposition'},indent=2))
