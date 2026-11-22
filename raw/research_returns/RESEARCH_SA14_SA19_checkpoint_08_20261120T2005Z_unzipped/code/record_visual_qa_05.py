"""Record the explicit visual review completed for checkpoint05."""
from pathlib import Path
import datetime,hashlib,json,csv
root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA14_SA19_paper.pdf'
pages=[1,16,20,25,32,36,37,40,49,50,51,52,57,60,61,62,63,64,70,78,83,90,94,95,96,97,98,100,103,111,119,120,124,128]
q=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),page_count=128,pages_visually_inspected=pages,
 inspection_method='All nine rendered four-page contact sheets explicitly viewed. Includes every page with an overflow above2pt in the first build and a sample across all Parts and the register/bibliography.',
 overfull_paragraphs_gt_2pt_before_correction=5,maximum_overfull_pt_before=12.08731,
 overfull_gt_2pt_after=0,overfull_total_after=3,maximum_overfull_pt_after=1.8769,
 missing_characters=0,undefined_citations=0,undefined_references=0,
 assessment='Readable mathematics, no clipping or unresolved references. New E4, F and J proofs and A2D inspected. Local line-breaking fixes preserved all mathematical claims. Research remains explicitly INCOMPLETE.')
(root/'code/visual_qa_05.json').write_text(json.dumps(q,indent=2)+'\n')
p=root/'CHECK_EVENTS.tsv';rows=list(csv.DictReader(p.open(),delimiter='\t'))
event=dict(statement_id='E4.S-independent',date=q['time_utc'],who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited, not exposed',type='targeted proof check',outcome='PASS: explicit cuspidal degeneration, free quotient and rigidified Pic-tau product; fibrewise smoothness and relative smoothness distinguished. work/root/E4_smoothness_audit.md; separate DGJ full audit saved.')
if not any(r['statement_id']==event['statement_id'] for r in rows):rows.append(event)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps(q,indent=2))
