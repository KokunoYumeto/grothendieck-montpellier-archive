"""Render selected PDF pages for explicit visual inspection; images are scratch only."""
from pathlib import Path
import sys,subprocess,json,hashlib,datetime
root=Path(__file__).resolve().parents[1];pdf=root/'RESEARCH_SA14_SA19_paper.pdf'
run=sys.argv[1];pages=[int(x) for x in sys.argv[2:]]
out=root/'tmp/pdfs'/('qa_'+run);out.mkdir(parents=True,exist_ok=True)
for page in pages:
    command=['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1400','-singlefile','-png',str(pdf),str(out/f'page-{page:02d}')]
    subprocess.run(command,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
report=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pages_rendered=pages,render_directory=str(out),visual_inspection='Pending explicit image inspection; rendering alone is not visual QA.')
(root/'code'/f'render_qa_{run}_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
