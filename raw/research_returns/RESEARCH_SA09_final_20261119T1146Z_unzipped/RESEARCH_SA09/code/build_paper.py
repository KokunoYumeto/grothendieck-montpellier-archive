"""Build the integrated paper with LuaLaTeX and retain complete build logs."""
from pathlib import Path
import subprocess, json, re, time, shutil
from tex_runtime import environment
ROOT=Path(__file__).resolve().parents[1]
name='RESEARCH_SA09_paper'
commands=[['lualatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],
          ['bibtex',name],
          ['lualatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],
          ['lualatex','-interaction=nonstopmode','-halt-on-error',name+'.tex']]
if (ROOT/(name+'.aux')).exists():
 # Refresh bibliography before reading a previous .bbl, which may have
 # been generated from a bibliography whose TeX escaping was just fixed.
 commands=[['bibtex',name]]+commands
records=[]
for i,cmd in enumerate(commands,1):
 start=time.perf_counter()
 result=subprocess.run(cmd,cwd=ROOT,env=environment(),capture_output=True,text=True)
 (ROOT/'logs'/f'integrated_build_{i}.txt').write_text(result.stdout+result.stderr)
 entry={'step':i,'command':cmd,'exit_code':result.returncode,'runtime_seconds':round(time.perf_counter()-start,6)}
 if cmd[0]=='lualatex' and (ROOT/(name+'.log')).exists():
  log=(ROOT/(name+'.log')).read_text(errors='replace')
  shutil.copyfile(ROOT/(name+'.log'),ROOT/'logs'/f'integrated_build_{i}.log')
  widths=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
  entry.update(overfull_hbox_count=len(widths),over_2pt_count=sum(x>2 for x in widths),widths_pt=widths,
      missing_characters=len(re.findall('Missing character:',log)),
      undefined_references=bool(re.search('There were undefined references',log)),
      pages=re.findall(r'Output written on .*?\((\d+) pages',log))
 records.append(entry)
 print(json.dumps(entry),flush=True)
 (ROOT/'logs'/'integrated_build.json').write_text(json.dumps(records,indent=2))
 if result.returncode:
  print('\n'.join((result.stdout+result.stderr).splitlines()[-20:]))
  raise SystemExit(result.returncode)
