"""Record completed root audits; do not substitute source checks for proof checks."""
from pathlib import Path
import csv,datetime
root=Path(__file__).resolve().parents[1]
p=root/'CHECK_EVENTS.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[
('E4.Curve-root','targeted proof check','PASS: full curve schematicity proof and exact BLR/Stacks source hypotheses checked; work/root/E4Curve_F7_D4b_audits.md. Higher-dimensional question retained.'),
('F7-F7a-F7b-root','independent re-proof','PASS: coefficient semistability, uniform Frobenius-pole bound, relative complement counting, and geometric extension scope; exact proper-henselian and proper-pi1 sources opened. work/root/E4Curve_F7_D4b_audits.md.'),
('D4b-root','targeted proof check','PASS: D4a forbids the Albanese-fibration lift; exact Partsch2013 pp102–106 checked, and connected-target/etale-source inference separately refuted. work/root/E4Curve_F7_D4b_audits.md.'),
('J6C-root','independent re-proof','PASS: all geometric fibres integral, total and generic varieties smooth, normal ruling degree -2, point-blowup invariance, and actual Picard-test composite [-2]. Literal middle fixed-part clause at44:4 refuted. work/root/J6C_audit.md.')]
seen={(r['statement_id'],r['outcome']) for r in rows}
for ident,kind,outcome in checks:
 if (ident,outcome) not in seen: rows.append(dict(statement_id=ident,date=now,who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited, not exposed',type=kind,outcome=outcome))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print({'time_utc':now,'events':len(rows),'checks_considered':len(checks)})
