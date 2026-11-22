#!/usr/bin/env python3
"""Repair this session's rootless TeX font map; ordinary TeX Live needs no repair."""
from pathlib import Path
import os, subprocess, json, hashlib, time
root=Path(__file__).resolve().parents[1]
p=root.parent/'.tex-runtime'
start=time.perf_counter()
out=p/'var/fonts/map/pdftex/updmap/pdftex.map'
out.parent.mkdir(parents=True,exist_ok=True)
base=p/'root/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts'
parts=[base/(n+'.map') for n in ('cm','cmextra','symbols','euler','latxfont')]
out.write_text('\n'.join(v.read_text() for v in parts))
env=os.environ.copy();env['TEXMFCNF']=str(p)+':'+str(p/'root/usr/share/texlive/texmf-dist/web2c')
subprocess.run(['mktexlsr',str(p/'var')],env=env,check=True)
checks={}
for font in ('pdftex.map','cmmi10.pfb'):
 r=subprocess.run(['kpsewhich',font],env=env,capture_output=True,text=True,check=True)
 checks[font]=r.stdout.strip()
record={'date_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'outcome':'PASS','scope':'Regenerate rootless map from installed Type1 font maps and refresh filename database. Two earlier failed builds are retained. No mathematical source change.', 'files':checks,'map_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'seconds':time.perf_counter()-start}
(root/'logs/rootless_font_map_repair.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
