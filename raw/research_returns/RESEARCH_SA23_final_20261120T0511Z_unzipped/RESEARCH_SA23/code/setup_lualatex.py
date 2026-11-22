"""Repair the minimal LuaLaTeX runtime locally, without system changes."""
from pathlib import Path
import urllib.request,re,subprocess,hashlib,json,time
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
target=root/'runtime'
target.mkdir(exist_ok=True)
url='https://deb.debian.org/debian/pool/main/t/texlive-base/'
records=[]
try:
    with urllib.request.urlopen(url,timeout=30) as response: html=response.read().decode()
    names=sorted(set(re.findall(r'href="(texlive-luatex_[^"]+_all\.deb)"',html)))
    if not names: raise RuntimeError('No texlive-luatex package in official pool')
    compatible=[name for name in names if '2022' in name]
    name=(compatible or names)[-1]
    with urllib.request.urlopen(url+name,timeout=30) as response: data=response.read()
    dest=target/name;dest.write_bytes(data)
    subprocess.run(['dpkg-deb','-x',str(dest),str(target/'debian_compatible')],check=True,capture_output=True)
    records.append({'url':url+name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':'downloaded and extracted'})
except Exception as e: records.append({'status':'failed','error':str(e)})
record={'records':records,'seconds':time.perf_counter()-start}
(root/'logs'/'setup_lualatex.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2),flush=True)

