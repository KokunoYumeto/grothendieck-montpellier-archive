"""Retrieve primary URLs discovered by web search, with bounded requests."""
from pathlib import Path
import subprocess,json,datetime,concurrent.futures
P=Path(__file__).resolve().parents[1]
urls={
 'SGA4II':'https://www.math.polytechnique.fr/~laszlo/sga4/SGA4-2/sga42.pdf',
 'SGA2':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/SGA2.pdf',
 'MilneAV':'https://www.jmilne.org/math/CourseNotes/AV.pdf',
 'Kleiman1968':'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf',
 'EGAIV2':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAIV.2.pdf',
 'EGFS2025Matroids':'https://arxiv.org/pdf/2507.15704',
 'EGFS2025Prym':'https://arxiv.org/pdf/2512.04902'
}
def fetch(k,u):
 p=P/'research'/f'{k}.pdf';t=P/'research'/f'{k}.txt'
 r=subprocess.run(['curl','-L','--fail','--max-time','55','--connect-timeout','15','-sS',u,'-o',str(p)],capture_output=True,text=True)
 d=dict(key=k,url=u,date=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode,error=r.stderr)
 if r.returncode==0:
  q=subprocess.run(['pdftotext','-layout',str(p),str(t)],capture_output=True,text=True)
  d.update(bytes=p.stat().st_size,text_chars=len(t.read_text(errors='replace')) if t.exists() else 0,extraction_returncode=q.returncode)
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(lambda kv:fetch(*kv),urls.items()))
(P/'audit'/'fetch_more_output.json').write_text(json.dumps(rows,indent=2))
print(json.dumps(rows,indent=2))
