from pathlib import Path
import csv

root=Path('RESEARCH_SA23'); notes=root/'notes'
events=[]
def add(id,kind,outcome):
    events.append([id,'2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories',kind,outcome])
add('SA23-31','used and rechecked in this run','Scope limited to accessibility sheets055-062 in the K161-2-04 group: exact Ind/presentability conditions and cardinal assertions rechecked in cat:I1-I12; broader ring-object material not included in this event')
add('SA23-53','used and rechecked in this run','Accessible-category headings expanded using actual transcription055-062 and original scans055,060-062; cat:I1-I12 prove corrected equivalences, exact cardinal closure, good-rank Fil equality and functor equivalences; all-ranks assertion refuted')
add('SA23-54','used and rechecked in this run','Original161-2/112 and supplied transcription checked; cat:I6 proves fixed-object relative classifier and full pseudopullback property for the stated small finite-limit/geometric scope')
add('SA23-36','used and rechecked in this run','Original161-5/023-029 and supplied Pro witness checked; cat:J1-J9 give exact torsor/relative-cohomology classification, fixed-data slope counterexample, actual-BT uniqueness, literal all-HT obstruction and ICM comparison')
add('SA23-38','used and rechecked in this run','Original162-5/022-031 checked; cat:L1-L8 correct d-square, prove symmetry and inverse, and derive flat pro-algebra equivalence and coefficient/crystal statements with exact limit qualifications')
add('SA23-52','used and rechecked in this run','Documentary scope only: directly inspected original162-5/002 title Le Tapis de Quillen, notes d Alexandre (1968), and /020 eleven-item publications list with1970 preprint and final To appear; no dating of all mathematical sheets inferred from that list')
for id in ['SA23-A-14','SA23-A-15','SA23-A-16','SA23-A-18','SA23-A-19']:
    add(id,'targeted proof check','Independent final adversarial category-agent audit passed; localization/completion, unbounded residue-field detection, Ext-limit vanishing, flat deformation and both topological projectivity conditions checked; details notes/category_root_A23_audit.md')
for id in ['SA23-A-06','SA23-A-07','SA23-A-08','SA23-A-09']:
    add(id,'targeted proof check','Independent category-agent audit of finite-relative/infinite-absolute p-rank branch and finite-p-basis positive lift passed; compositum union and nonzero infinitely divisible differential checked; notes/category_root_A23_audit.md')
p=notes/'category_CHECK_EVENTS.tsv'; old=p.read_text()
with p.open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for event in events:
        if event[-1] not in old or event[0] not in old:
            w.writerow(event)
# Correct the older combined ID by a superseding current event; retain its historical record.
with p.open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['SA23-38;SA23-52','2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories','targeted proof check','Superseded for identifier precision by the separate SA23-38 mathematical and SA23-52 documentary current-run events; do not treat the combined token as an independent earlier ID'])

p=notes/'category_corrections.tsv'
with p.open(newline='') as f:
    r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row['id']=='CAT-CL03':
        row['prior_statement']='Flat theorem and crystals described in a suitable topos without fixing a completion model'
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

p=notes/'category_progress.md'
s=p.read_text()+'\n## Independent final A.2/A.3 audit\n- Root requested an adversarial pass; no mathematical issue found. Exact source scopes and all completion, unbounded-derived, flatness and projectivity steps checked in notes/category_root_A23_audit.md.\n- Separate current-run events now preserve SA23-31,SA23-53,SA23-54,SA23-36,SA23-38 and documentary SA23-52 with scope limits. Original162-5/002 and020 documentary pages inspected.\n- Algebra agent independently passed I12 and J9; L5 coordinate-proalgebra arrow convention now explicit. That agent is recording its own audit events.\n'
p.write_text(s)
print('Added',len(events),'scoped sweep-ID and independent A.2/A.3 targeted proof events')
