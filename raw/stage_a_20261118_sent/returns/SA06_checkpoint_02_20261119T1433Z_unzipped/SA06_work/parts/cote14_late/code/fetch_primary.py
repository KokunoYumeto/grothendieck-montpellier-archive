"""Download already discovered primary-source PDFs and preserve extraction provenance."""
from pathlib import Path
import urllib.request, concurrent.futures, subprocess, json, datetime
P=Path(__file__).resolve().parents[1]
SOURCES={
 'Jannsen1992':'https://epub.uni-regensburg.de/26642/1/jannsen10.pdf',
 'Huber2020':'https://www.uni-muenster.de/FB10/mjm/vol_13/mjm_vol_13_16.pdf',
 'Ayoub2026':'https://user.math.uzh.ch/ayoub/PDF-Files/Anabel.pdf',
 'MumfordOda':'https://www.dam.brown.edu/people/mumford/alg_geom/papers/AGII.pdf',
 'GrothMumford':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/AGMumford.pdf',
 'DELV2011':'https://www.math.stonybrook.edu/~roblaz/Reprints/Debarre.Ein.Laz.Voisin.PNAV.pdf',
 'SGA3XIII':'https://wstein.org/sga/SGA3/Expo13.pdf',
 'EGAIV1':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAIV.1.pdf',
 'GrothHilbert1961':'https://numdam.org/article/SB_1960-1961__6__249_0.pdf',
 'BhattDeJong2014':'https://www.numdam.org/item/10.24033/asens.2228.pdf',
 'PatelRavindra2014':'https://www.math.purdue.edu/~patel471/inflift.pdf',
 'Kahn2021':'https://webusers.imj-prg.fr/~bruno.kahn/preprints/letter-Murre.pdf',
 'Kunnemann1993':'https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf',
}
def fetch(pair):
 key,url=pair; pdf=P/'research'/f'{key}.pdf'; txt=pdf.with_suffix('.txt')
 row=dict(key=key,url=url,accessed=datetime.datetime.now(datetime.timezone.utc).isoformat())
 try:
  if not pdf.exists():
   b=urllib.request.urlopen(url,timeout=50).read()
   if not b.startswith(b'%PDF'):raise ValueError('not a PDF')
   pdf.write_bytes(b)
  subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],check=True,capture_output=True)
  row.update(bytes=pdf.stat().st_size,text_chars=len(txt.read_text()),status='downloaded and extracted')
 except Exception as e:row.update(status='error',error=f'{type(e).__name__}: {e}')
 return row
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: rows=list(ex.map(fetch,SOURCES.items()))
 (P/'research'/'downloads.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(rows,ensure_ascii=False,indent=2))
