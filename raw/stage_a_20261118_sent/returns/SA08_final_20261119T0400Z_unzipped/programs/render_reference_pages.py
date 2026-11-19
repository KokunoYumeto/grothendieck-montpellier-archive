"""Render selected published-source pages for formula collation; no manuscript scans are supplied."""
import argparse,pathlib,json,fitz
p=argparse.ArgumentParser();p.add_argument('pdf');p.add_argument('pages',type=int,nargs='+');a=p.parse_args()
src=pathlib.Path(a.pdf);out=src.with_suffix('');out.mkdir(exist_ok=True)
d=fitz.open(src)
for n in a.pages:
 f=out/f'verify_{n:03d}.png';d[n-1].get_pixmap(dpi=180).save(f)
 print(json.dumps({'source':str(src),'pdf_page':n,'image':str(f)}))
