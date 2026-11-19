#!/usr/bin/env python3
"""Reproduce the final spacing-only pass over the authored English overview."""
from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[1]
p=R/'SA09_dossier.md';s=p.read_text()
months='January|February|March|April|May|June|July|August|September|October|November|December'
s=re.sub(r'(\d)('+months+r')(\d{4})',r'\1 \2 \3',s)
s=re.sub(r'(\d)('+months+r')\b',r'\1 \2',s)
s=re.sub(r'\b(date|level|before|exponent|and)(?=\d)',r'\1 ',s)
s=s.replace("Schinzel's1977","Schinzel's 1977").replace("Belyi's1978","Belyi's 1978").replace('),247–256', '), 247–256').replace('*,479–522','*, 479–522').replace('),293–375','), 293–375').replace('(pp.5–48)','(pp. 5–48)').replace('\n\n- Yagasaki','\n- Yagasaki')
p.write_text(s)
result={'scope':'Root English overview only','dates_and_spacing':'corrected','source_files_modified':0}
(R/'outputs/final_typography.json').write_text(json.dumps(result)+'\n')
print(json.dumps(result))
