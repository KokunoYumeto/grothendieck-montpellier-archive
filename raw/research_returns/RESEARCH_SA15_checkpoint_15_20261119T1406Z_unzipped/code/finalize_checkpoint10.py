"""Record actual checkpoint-10 visual inspection and refresh its report."""
from pathlib import Path
import csv, datetime, json, subprocess, sys

w = Path(__file__).resolve().parents[1]
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
root_pages = [1,14,24,28,39,55,70,85,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143]
oc_pages = [144,145,146,147,148,151,190,191]
rd_pages = [192,193,194,195,199,258]
qa = dict(checkpoint=10, observed_utc=now, result="PASS", pdf_pages=258,
          root_actually_viewed_pages=root_pages,
          obstruction_crystal_actually_viewed_pages=oc_pages,
          reduction_descent_actually_viewed_pages=rd_pages,
          total_distinct_pages=len(set(root_pages + oc_pages + rd_pages)),
          criteria="Legible typography, no clipping or overlaps, complete formulas and tables. Root viewed montages 1-6 individually after a prior multi-image result was truncated; the truncated result was not counted.")
(w/'outputs/visual_qa_checkpoint10.json').write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a', newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP10-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
      'artifact verification',
      'PASS: final PDF 258 pages, 1979949 bytes; build 27.433 s, zero overfull boxes and undefined references/citations; 38 actual rendered-page inspections (24 root, 8 obstruction/crystal, 6 reduction/descent). outputs/visual_qa_checkpoint10.json.'])
note = '\nFinal build passed in27.433 seconds:258 pages,1,979,949 bytes, no overfull boxes, no undefined references, and no undefined citations. All38 selected rendered pages were actually inspected:24 by the root,8 by the obstruction/crystal agent, and6 by the reduction/descent agent. Typography, displayed formulas, page breaks, and bibliography passed. A truncated multi-image tool response was not counted; the root subsequently viewed all six assigned montages individually. The exact page lists and observation time are retained in outputs/visual_qa_checkpoint10.json.\n'
with (w/'notes/checkpoint10_changes.md').open('a') as f: f.write(note)
subprocess.run([sys.executable,str(w/'code/merge_registers.py')],check=True,cwd=w)
subprocess.run([sys.executable,str(w/'code/update_current10.py')],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
    f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
