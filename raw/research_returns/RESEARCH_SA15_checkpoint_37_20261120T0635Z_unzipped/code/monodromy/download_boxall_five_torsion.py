from pathlib import Path
import urllib.request,subprocess
root=Path(__file__).resolve().parent.parent
p=root/'sources/boxall_grant_leprevost_2001_five_torsion.pdf'
p.parent.mkdir(parents=True,exist_ok=True)
url='https://euclid.colorado.edu/~grant/publications/5torsion_points_on_curves_of_genus_2.pdf'
with urllib.request.urlopen(url,timeout=30) as r:p.write_bytes(r.read())
subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
print({'saved':str(p),'bytes':p.stat().st_size})
