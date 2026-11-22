"""Adopt the actual converged PDF, preserving the detected contents difference."""
from pathlib import Path
import datetime,hashlib,json,re,shutil
w=Path(__file__).resolve().parents[1];diag=w/'outputs/checkpoint33_aux_stability'
r=json.loads((diag/'record.json').read_text());compare=json.loads((diag/'page_stability.json').read_text())
assert r['aux_identical'] and not r['rerun_warning']
assert compare['different_pages']==[2,3,4,5,6] and compare['selected_pages_pixel_identical']
prior=json.loads((w/'outputs/checkpoint33_integration_attempt01.json').read_text())
folder=w/'outputs/checkpoint33_build_attempt02';assert not folder.exists();folder.mkdir()
shutil.copytree(w/'sections',folder/'sections')
for name in ['RESEARCH_SA15_paper.tex','RESEARCH_SA15_references.bib']:
 shutil.copy2(w/name,folder/name)
(w/'RESEARCH_SA15_paper.pdf').rename(diag/'CP33_pre_convergence.pdf')
shutil.copy2(diag/'RESEARCH_SA15_paper.pdf',w/'RESEARCH_SA15_paper.pdf')
(diag/'RESEARCH_SA15_paper.pdf').rename(diag/'CP33_converged_diagnostic.pdf')
for suffix in ['log','aux','toc','out','bbl']:
 p=diag/f'RESEARCH_SA15_paper.{suffix}'
 if p.exists():shutil.copy2(p,w/p.name)
log=(w/'RESEARCH_SA15_paper.log').read_text()
boxes=[{'kind':m.group(1),'points':float(m.group(2)),'context':log[m.start():m.start()+320]} for m in re.finditer(r'Overfull \\([hv])box \(([-\d.]+)pt too (?:wide|high)\)',log)]
summary={'seconds':r['seconds'],'overfull_boxes':boxes,'over_2pt':sum(b['points']>2 for b in boxes),
 'pdf_bytes':(w/'RESEARCH_SA15_paper.pdf').stat().st_size,'undefined_references':'There were undefined references' in log,
 'undefined_citations':'There were undefined citations' in log,'rerun_warning':'Label(s) may have changed' in log,
 'scope':'One additional successful convergence pass after the initial full three-pass build.'}
assert not summary['rerun_warning'] and not summary['over_2pt']
(w/'outputs/build_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
shutil.copy2(diag/'stdout.txt',w/'outputs/build_console.txt')
for rel in ['outputs/build_summary.json','outputs/build_console.txt','RESEARCH_SA15_paper.log','RESEARCH_SA15_paper.aux']:
 shutil.copy2(w/rel,folder/Path(rel).name)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
integration={'integration_started_utc':r['actual_utc'],'complete_utc':now,'promoted_files':prior['promoted_files'],
 'build_exit_code':0,'actual_build_snapshot':str(folder.relative_to(w)),'attempt':2,
 'scope':'Adopted the independently executed isolated convergence pass; no further mathematical source change.',
 'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()}
(w/'outputs/checkpoint33_integration_attempt02.json').write_text(json.dumps(integration,indent=2)+'\n')
(w/'outputs/qa33').rename(w/'outputs/qa33_preconvergence')
(w/'outputs/visual_qa33_pending.json').rename(w/'outputs/visual_qa33_pending.preconvergence.json')
render=w/'code/render_qa33.py';shutil.copy2(render,diag/'render_qa33.before_convergence.py')
t=render.read_text();assert '1,14,28,55,85,126,len(d)-1,len(d)' in t
render.write_text(t.replace('1,14,28,55,85,126,len(d)-1,len(d)','1,2,3,4,5,6,14,28,55,85,126,len(d)-1,len(d)'))
oldqa=w/'notes/qa33_root_actual_review.json';oldqa.rename(w/'notes/qa33_root_actual_review.preconvergence.json')
with (w/'notes/checkpoint33_changes.md').open('a') as f:
 f.write('\n### Detected and repaired contents convergence\n\nThe initial successful full build retained a rerun warning. An isolated successful extra LuaLaTeX pass took '+str(r['seconds'])+' seconds, reached byte-stable auxiliary labels and cleared that warning. A complete page comparison found actual contents-entry differences on pages2--6; the earlier29 inspected pages were pixel-identical. The page-comparison assertion therefore failed, as correctly retained in its exact source and stderr. Its optimistic scope string was not accepted as a result: status DIFFERENCE and its explicit page list govern that failed check. We adopted the converged PDF, preserved both logs and all old QA records, and required new final-image inspections including all five changed contents pages. The old and duplicate diagnostic PDFs are excluded from the archive; all diagnostic code, output, and the failed assertion remain. The final dossier records two successful compilation attempts and one failed page-equivalence check, not a failed mathematical certificate.\n')
print(json.dumps(integration,indent=2))
