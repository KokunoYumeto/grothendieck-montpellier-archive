"""Diagnose the persistent LaTeX rerun warning without touching the reviewed PDF."""
from pathlib import Path
import datetime,difflib,hashlib,json,os,shutil,subprocess,time
w=Path(__file__).resolve().parents[1]
folder=w/'outputs/checkpoint33_aux_stability';assert not folder.exists();folder.mkdir()
for suffix in ['aux','toc','bbl','blg','out']:
 p=w/f'RESEARCH_SA15_paper.{suffix}'
 if p.exists():shutil.copy2(p,folder/p.name)
before=(w/'RESEARCH_SA15_paper.aux').read_bytes()
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
local=w.parent/'.tex-runtime';env=os.environ.copy()
env['TEXMF']='{'+','.join(map(str,[local,local/'texmf-dist',w,Path('/usr/share/texmf'),Path('/usr/share/texlive/texmf-dist')]))+'}'
env['TEXFORMATS']=str(w)+':'+env.get('TEXFORMATS','')
command=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(folder),'RESEARCH_SA15_paper.tex']
start=time.perf_counter();run=subprocess.run(command,cwd=w,env=env,capture_output=True,text=True);elapsed=time.perf_counter()-start
(folder/'stdout.txt').write_text(run.stdout);(folder/'stderr.txt').write_text(run.stderr)
after=(folder/'RESEARCH_SA15_paper.aux').read_bytes() if (folder/'RESEARCH_SA15_paper.aux').exists() else b''
diff=''.join(difflib.unified_diff(before.decode().splitlines(True),after.decode().splitlines(True),fromfile='reviewed-current.aux',tofile='isolated-rerun.aux'))
(folder/'aux.diff').write_text(diff)
rec={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':run.returncode,'seconds':elapsed,
     'current_pdf_sha256':pdfhash,'current_pdf_preserved':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==pdfhash,
     'aux_identical':before==after,'aux_diff_lines':len(diff.splitlines()),'rerun_warning':'Label(s) may have changed' in run.stdout,
     'scope':'Isolated artifact diagnosis only; the reviewed master PDF and its auxiliary files are untouched.'}
(folder/'record.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
assert run.returncode==0
assert rec['current_pdf_preserved']
