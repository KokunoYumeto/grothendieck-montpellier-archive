from pathlib import Path
import subprocess,json,sys
out=Path(__file__).resolve().parents[1]/'outputs'
key=sys.argv[1]; pages=sys.argv[2:]
logs=[]
for page in pages:
 cmd=['pdftoppm','-f',page,'-l',page,'-scale-to','1600','-png','-singlefile',str(out/(key+'.pdf')),str(out/(key+'_p'+page))]
 r=subprocess.run(cmd,capture_output=True,text=True); logs.append({'cmd':cmd,'exit':r.returncode,'stderr':r.stderr})
print(json.dumps(logs)); (out/(key+'_render_log.json')).write_text(json.dumps(logs,indent=2)+'\n')
