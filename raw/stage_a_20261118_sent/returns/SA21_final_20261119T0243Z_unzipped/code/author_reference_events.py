"""Serialize the root's final bibliography/access checks; no new theorem claims."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]
rows=[]
for key in ['Raney1952','DeJonghTroelstra1966','Dacey1968']:
    rows.append({'statement_id':key,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; /root SA21 final audit','type':'carried as background without fault found','outcome':'Bibliographic/access audit only: earlier-reader access attempts and the unverified BibTeX status were inspected. The original work was not opened successfully, no original theorem from it is used in any claim or problem, and no proof check or exact result match is asserted. Retained solely as an explicitly unverified backward-reference lead.'})
for key,detail in [
 ('Ischi2010','Root reopened publisher landing page: online20January2011, issueDecember2010, volume64 pp379–396, DOI10.1007/s00012-011-0108-5; chronology rechecked, theorem check remains the IX reader’s primary-PDF event.'),
 ('DomenachLeclerc2001','Root reopened publisher landing page: March2001, Order18 pp89–104, DOI10.1023/A:1010662327346, abstract scope arbitrary biclosed relations/Galois connections. Full theorem check remains the IX reader’s primary-author-version event.'),
 ('CoeckeMoore2000','Root arXiv abstract reopening returned DisabledError. No new theorem check is claimed by root; successful primary-PDF check is documented by the IX reader.')]:
    rows.append({'statement_id':key,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; /root SA21','type':'used and rechecked in this run' if key!='CoeckeMoore2000' else 'carried as background without fault found','outcome':detail+' Retrieval metadata: sources_web/root_open_028.json.'})
p=R/'parts/root/additional_reference_events.tsv'
for key,detail in [
 ('Jenca2026','Root reopened the primary publisher page: title N-free Posets and Orthomodularity, Order43 article11, published5February2026. The abstract concerns incomparability; no unrestricted strict-comparability theorem is inferred. The P4 example check remains the final IX reader’s primary-text event.'),
 ('JencaCorrection2026','Root reopened the correction publisher page, published11August2026. This is a bibliographic/version check only; no uninspected corrected theorem is used. The earlier primary-PDF access limitation remains explicit.')]:
    rows.append({'statement_id':key,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; /root SA21','type':'used and rechecked in this run','outcome':detail+' Retrieval metadata: sources_web/root_open_029.json.'})
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'additional_reference_events':len(rows),'output':str(p.relative_to(R))}))
