"""Record the environment used for the saved computations and source rendering."""
import importlib.metadata,json,platform,shutil,subprocess,sys
versions={}
for name in ['sympy','numpy','scipy','pypdf','pdfplumber','Pillow']:
 try:versions[name]=importlib.metadata.version(name)
 except importlib.metadata.PackageNotFoundError:versions[name]='not installed'
commands={}
for name,args in [('pdftoppm',['-v']),('pdftotext',['-v']),('tesseract',['--version']),('dvitype',['--version'])]:
 path=shutil.which(name)
 if path:
  p=subprocess.run([path]+args,capture_output=True,text=True)
  commands[name]={'path':path,'version_first_line':(p.stdout or p.stderr).splitlines()[0],'exit_code':p.returncode}
print(json.dumps({'python':sys.version,'platform':platform.platform(),'packages':versions,'source_rendering_tools':commands,'scope':'Environment metadata, not a mathematical test or proof.'},ensure_ascii=False,indent=2))
