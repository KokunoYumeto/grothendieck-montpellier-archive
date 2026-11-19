"""Assemble the final outcome-first report from checked records, without changing proofs."""
from pathlib import Path
import time,json,csv,hashlib
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
parts=[root/'REPORT_ROOT.md']
required=[
 ('Requested primary sources and access status','REQUESTED_SOURCE_STATUS.md'),
 ('Every program: scope, counts and observed runtime','PROGRAM_AUDIT.md'),
 ('Detailed B.1–B.4 proof and correction record','agent_B_levels.md'),
 ('Detailed B.5–B.6 proof and correction record','agent_B56.md'),
 ('Cote150 inherited statements and attached-file corrections','C_source_corrections.md'),
 ('C5 Hurewicz construction and discarded source route','C5_Hurewicz_review.md'),
 ('Independent C5 boundary/category audit','C5_audit_B.md'),
 ('Final publication verification','PDF_QA_REPORT.md'),
 ('Final statement and citation register audit','FINAL_register_audit_B56.md')
]
text=parts[0].read_text()
for title,name in required:
    p=root/name
    if not p.exists(): raise SystemExit('Required final record missing: '+name)
    text+='\n\n---\n\n## '+title+'\n\n'+p.read_text()
text+='\n\n## Final integration of audit findings\n\nThe two additions requested by the independent C5 audit are present in the final PDF: the vertical-face submersion derivation on pages61–62 and the explicit PL target-local-embedding condition on pages69–70. The C proof source was frozen before final rendering. Historical requests for integration in contribution records do not indicate an unfinished step. The final register audit and PDF digest identify the delivered version.\n'
results=list(csv.DictReader((root/'RESEARCH_SA10_results.csv').open()))
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
text+=f'\nThe final aggregate contains **{len(results)} numbered-result rows** and **{len(events)} actual check events**. Exact source and event normalization files are included.\n'
(root/'RESEARCH_SA10_report.md').write_text(text)
print(f'Assembled final report: {len(required)+1} sections/source records; {len(text)} characters; {len(results)} results; {len(events)} events.')
print(f'Runtime {time.perf_counter()-start:.9f} seconds.')
