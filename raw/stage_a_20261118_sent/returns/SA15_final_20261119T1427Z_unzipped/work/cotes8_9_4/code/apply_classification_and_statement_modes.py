"""Apply the root-agreed C070 chronology correction and statement labels."""
import csv
import json
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
claims=json.loads((BASE/'claims.json').read_text())
for c in claims:
    c['his_statement_mode']='report of the transcribed statement'
    if c['id'] in {'P894-C077','P894-C078','P894-C082'}:
        c['statement_mode']='present-run refinement of the reported source cue; not an additional manuscript assertion'
    else:
        c['statement_mode']='modern formulation of the manuscript assertion or question, with corrections and reconstructions identified separately'
    if c['id']=='P894-C070':
        c['class']='B'
        c['fate']=('Serre’s 1958 construction supplies the historical free-quotient surface, not a 1958 crystalline-cohomology theorem. '
            'Berthelot–Esnault–Rülling §9.2 verifies its later cohomological use. The stated crystalline torsion and ker φ '
            'conclusions are independently derived in this run from the later published crystalline base-change and '
            'stable-augmentation framework, with the admitted integral-Lefschetz hypotheses retained. '
            'No first publication or historical priority is assigned to that exact corollary.')
        c['fate_date']=('Underlying construction: Serre’s Mexico 1956 lecture, published 1958. '
            'Stable augmentation: SGA 7 II, XXII, published 1973; crystalline framework checked in Illusie 1976. '
            'Later verification of the construction: Berthelot–Esnault–Rülling 2012. '
            'Exact implications independently derived here on 2026-11-19; their first publication is not established.')
        c['present_status']='As of November 2026: '+c['fate']
        c['refs']=list(dict.fromkeys(c['refs']+['KatzSGA7XXII','Illusie1976']))
(BASE/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')

path=BASE/'check_events.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
event={'statement_id':'P894-C070','date':'2026-11-19',
       'who':'GPT-6 Astra Pro; effort setting not exposed; SA15-20261119/cotes8_9_4',
       'type':'used and rechecked in this run',
       'outcome':'Chronology and attribution audit: changed the full row from E to B. Serre 1958 is the source of the surface construction, while the crystalline torsion consequence uses later crystalline/stable-augmentation results and this run’s explicit derivation. This is not a new re-proof event or a claim that Serre published crystalline cohomology in 1958.'}
if event not in rows:rows.append(event)
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)
report={'class_correction':{'P894-C070':'E -> B'},
        'his_statement_mode_records':len(claims),
        'all_his_statement_fields_are_reports_not_unmarked_verbatim_quotes':True,
        'refinement_statement_modes':['P894-C077','P894-C078','P894-C082'],
        'package_check_events':len(rows)}
(BASE/'outputs/classification_and_statement_modes.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
