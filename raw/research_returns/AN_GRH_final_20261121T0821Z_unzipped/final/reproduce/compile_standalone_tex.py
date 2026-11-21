#!/usr/bin/env python3
"""Compile an isolated snapshot with installed XeTeX; never edit its source.

Example from the package directory:
  python reproduce/compile_standalone_tex.py --source AN_GRH.tex --build-dir /tmp/an_grh_build

This workflow needs xetex, xelatex, the standard LaTeX packages named in the
source, Latin Modern fonts, and pdfinfo. It makes no network requests and
performs no privileged or system-wide installation. On the audit runtime,
process-local TEXMF roots enable filesystem lookup because the packaged
ls-R database links are dangling. A local format is generated when absent.
The resulting PDF is a compile-check artifact until visual QA is completed.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess, time

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--source',type=Path,required=True)
 p.add_argument('--build-dir',type=Path,required=True)
 p.add_argument('--format-dir',type=Path)
 p.add_argument('--texmf-root',action='append',default=[])
 p.add_argument('--max-passes',type=int,default=4)
 a=p.parse_args(); source=a.source.resolve(); build=a.build_dir.resolve(); build.mkdir(parents=True,exist_ok=True)
 fmt_dir=(a.format_dir or build).resolve(); fmt_dir.mkdir(parents=True,exist_ok=True)
 snapshot=build/'AN_GRH.tex'
 if snapshot==source: raise SystemExit('The build source must be an isolated copy, not the original path.')
 shutil.copy2(source,snapshot); source_hash=sha(snapshot)
 env=os.environ.copy()
 roots=[str(Path(x).resolve()) for x in a.texmf_root] or [str(x) for x in map(Path,('/usr/share/texlive/texmf-dist','/usr/share/texmf','/etc/texmf')) if x.is_dir()]
 if roots:env['TEXMF']='{'+','.join(roots)+'}'
 env['TEXMFVAR']=str(build/'texmf-var'); env['TEXMFCONFIG']=str(build/'texmf-config')
 manifest={'source':str(source),'snapshot_sha256':source_hash,'snapshot_bytes':snapshot.stat().st_size,'build_dir':str(build),'format_dir':str(fmt_dir),'environment_overrides':{k:env[k] for k in ('TEXMF','TEXMFVAR','TEXMFCONFIG') if k in env},'attempts':[]}
 def record(): (build/'BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
 def run(args,cwd,logname):
  start=time.time(); logfile=build/logname
  with logfile.open('w') as log:
   try:r=subprocess.run(args,cwd=cwd,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180,text=True); code=r.returncode
   except subprocess.TimeoutExpired:code=124
  item={'command':args,'cwd':str(cwd),'exit_code':code,'seconds':round(time.time()-start,3),'log':logname}; manifest['attempts'].append(item); record(); print(json.dumps(item),flush=True)
  if code: raise SystemExit('Compilation failed; inspect '+str(logfile))
 fmt=fmt_dir/'xelatex.fmt'
 if not fmt.exists():run(['xetex','-ini','-etex','-jobname=xelatex','-progname=xelatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape','xelatex.ini'],fmt_dir,'format_build.stdout.log')
 manifest['format_sha256']=sha(fmt)
 args=['xelatex','-fmt='+str(fmt),'-interaction=nonstopmode','-halt-on-error','-file-line-error','-no-shell-escape','AN_GRH.tex']
 stable=False
 for attempt in range(1,a.max_passes+1):
  run(args,build,f'pass{attempt}.stdout.log')
  log=(build/'AN_GRH.log').read_text(errors='replace'); shutil.copy2(build/'AN_GRH.log',build/f'pass{attempt}.tex.log')
  needs_rerun=bool(re.search(r'Rerun to|get cross-references right|Rerun LaTeX|Table widths have changed|Label\(s\) may have changed',log))
  if not needs_rerun:stable=True; break
 info=subprocess.run(['pdfinfo',str(build/'AN_GRH.pdf')],env=env,text=True,capture_output=True,timeout=30)
 (build/'pdfinfo.txt').write_text(info.stdout+info.stderr)
 warning_lines=[line for line in log.splitlines() if any(x in line for x in ('Warning','Overfull','Underfull','Missing character','Undefined control sequence'))]
 manifest.update({'passes':attempt,'stable':stable,'page_count':int(re.search(r'^Pages:\s+(\d+)',info.stdout,re.M)[1]) if info.returncode==0 else None,'pdf_sha256':sha(build/'AN_GRH.pdf'),'source_matches_current':sha(source)==source_hash,'warnings':warning_lines,'overfull_hboxes':re.findall(r'Overfull \\hbox \(([^)]+)\)([^\n]*)',log),'undefined_references':bool(re.search(r'undefined references|Citation .*undefined|Reference .*undefined',log))})
 record(); print(json.dumps({k:v for k,v in manifest.items() if k not in ('attempts','environment_overrides')},indent=2),flush=True)
 if not stable or manifest['undefined_references']:raise SystemExit('PDF generated, but references or layout tables have not stabilized.')
if __name__=='__main__':main()
