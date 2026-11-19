"""Render a document-wide sample including every newly integrated proof family."""
from pathlib import Path
import concurrent.futures,subprocess,time,json,re
ROOT=Path(__file__).resolve().parents[1];started=time.perf_counter()
aux=(ROOT/'logs/RESEARCH_SA22_paper.aux').read_text()
labels={match[1]:int(match[3]) for match in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{(\d+)\}',aux)}
info=subprocess.run(['pdfinfo',str(ROOT/'RESEARCH_SA22_paper.pdf')],capture_output=True,text=True,check=True).stdout
total=int(re.search(r'Pages:\s+(\d+)',info)[1])
selected=['A1-Earle-Marden-original','A2b-image','A2-collar-explicit',
          'A6-model-system','A6-model-specialization','B1b-fermat',
          'C-literal-class','C-packed-asymmetry']
pages=sorted({1,4,total,total-10,*[labels[label] for label in selected if label in labels]})
# Include the new model-counterexample page regardless of its final label suffix.
pages=sorted(set(pages)|{page for label,page in labels.items() if label.startswith('A6-') and ('fibre-counter' in label or 'special-fibre' in label)})
def render(page):
    start=time.perf_counter();prefix=ROOT/'qa'/f'paper_cp04_{page:03d}'
    result=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','85',
                           '-singlefile','-png',str(ROOT/'RESEARCH_SA22_paper.pdf'),str(prefix)],capture_output=True,text=True)
    return dict(page=page,exit_code=result.returncode,seconds=time.perf_counter()-start,stderr=result.stderr,path=str(prefix)+'.png')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:results=list(executor.map(render,pages))
output=dict(pdf_pages=total,pages=len(pages),selected_labels={key:labels.get(key) for key in selected},
            seconds=time.perf_counter()-started,renders=results)
(ROOT/'code/root_render_checkpoint04_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
