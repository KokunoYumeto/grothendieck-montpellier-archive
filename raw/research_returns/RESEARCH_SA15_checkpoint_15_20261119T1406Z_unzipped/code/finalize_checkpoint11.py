"""Record actual checkpoint11 visual QA and refresh its current report."""
from pathlib import Path
import csv,datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
root=[1,14,24,28,39,55,70,85,148,149,150,151,152,153,154,155]
oc=[156,157,158,159,160,161,162,163]
rd=[164,165,167,211,212,213,214,215]
mono=[216,221,281]
qa=dict(checkpoint=11,observed_utc=now,result='PASS',pdf_pages=281,
 root_actually_viewed_pages=root,obstruction_crystal_actually_viewed_pages=oc,
 reduction_descent_actually_viewed_pages=rd,monodromy_actually_viewed_pages=mono,
 total_distinct_pages=len(set(root+oc+rd+mono)),
 criteria='All nine montages actually viewed separately by assigned agents; legible typography and formulas, no clipping, overlap, missing glyphs or margin failures. The root viewed montages1-4, OC5-6, RD7-8, monodromy9.')
(w/'outputs/visual_qa_checkpoint11.json').write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['CP11-VISUAL-QA',now,
  'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
  'artifact verification',
  'PASS: final PDF281 pages2133847bytes, build28.172s, zero overfull boxes and undefined references/citations. All35 selected pages actually viewed (root16, OC8, RD8, monodromy3). Full page list in outputs/visual_qa_checkpoint11.json. Prior failed bibliography-underscore build transcript retained; repaired canonical note and final rebuild passed.'])
note='\n## Final checkpoint verification\n\nThe final paper has281 pages and2,133,847 bytes. The reproducible build passed in28.172 seconds with no overfull boxes, unresolved references or unresolved citations. All35 selected rendered pages were actually inspected, including the complete new sections:16 by the root,8 by the obstruction/crystal agent,8 by reduction/descent and3 by monodromy. The exact page lists and observation time are retained in outputs/visual_qa_checkpoint11.json. An initial bibliography-underscore build failure was repaired; its complete transcript remains in outputs/build_console_cp11_failed_bib_underscore.txt.\n\nThe final register contains319 numbered statements; the source census has139 rows, including the explicit unused Hua witness. The code export copied106 agent program/output files verbatim in addition to root programs and outputs. The local self-tacnode monodromy argument remains a clearly labelled, unintegrated candidate; no global Hasse-divisor or higher-degree full-image conclusion is inferred from it.\n'
with (w/'notes/checkpoint11_changes.md').open('a') as f:f.write(note)
subprocess.run([sys.executable,str(w/'code/merge_registers.py')],check=True,cwd=w)
subprocess.run([sys.executable,str(w/'code/update_current11.py')],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
 f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
