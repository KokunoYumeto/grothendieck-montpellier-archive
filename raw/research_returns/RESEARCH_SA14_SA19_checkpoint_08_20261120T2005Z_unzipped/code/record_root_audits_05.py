"""Append actual root proof/source checks completed after checkpoint04."""
from pathlib import Path
import csv, datetime

root=Path(__file__).resolve().parents[1]
p=root/'CHECK_EVENTS.tsv'
rows=list(csv.DictReader(p.open(),delimiter='\t'))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[
 ('E4.T-independent','independent re-proof','PASS: projectivity-free numerical-triviality closedness over arbitrary scheme bases. Complete trait proof, Zheng alteration, weighted intersection matrix, negativity lemma and constructible descent audited; work/root/E4_tauclosed_audit.md.'),
 ('J6L-independent','independent re-proof','PASS: conditional incidence Lefschetz theorem with algebraic lowering correspondence. Exact degree detection and low/high-range correspondence identities checked; work/root/J6L_audit.md.'),
 ('A2-Lipman-shortcut','used and rechecked in this run','Opened Lipman1976 Proposition2.5 pp30–32 and Corollary2.11 p33. Nilpotent Picard comparison does not eliminate finite etale p-primary component kernels; no unconditional A2 inference made.'),
 ('A2-Kweon-status','used and rechecked in this run','Opened Kweon arXiv2008.01908v2 §7 pp16–19, especially Question7.7; point injectivity and closed embedding are separate questions. A3 answers the latter negatively, not the former.'),
 ('A2D-independent','independent re-proof','BCE independently checked the conormal dlog argument, finiteness of smooth bad hyperplanes, exact rank a−1, and determinantal height bound; no gap found. work/root/A2_determinantal.tex.'),
 ('F4-F5-F6-independent','independent re-proof','PASS: full twisted-H1 proof, abelian-inertia fixed-cover construction, Frobenius projection formula, complement-count criterion and pro-p-by-virtually-abelian consequence. Primary Suzuki2023 §§2–3 reopened; work/root/F5_audit.md.'),
 ('J6P-J6Z-independent','independent re-proof','PASS within smooth-axis/codimension-two/generic-member scope. Trace spread, blowup signs, Picvar absorption, Lang–Neron argument and top-target surjectivity checked; source gates opened. work/root/J6P_J6Z_audit.md.')
]
seen={(r['statement_id'],r['outcome']) for r in rows}
for ident,kind,outcome in checks:
 if (ident,outcome) not in seen:
  rows.append(dict(statement_id=ident,date=now,who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited, not exposed',type=kind,outcome=outcome))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
 w.writeheader();w.writerows(rows)
print({'time_utc':now,'events':len(rows),'checks_considered':len(checks)})
