"""Inspect only public book/author pages for an accessible primary theorem text."""
from pathlib import Path
import urllib.request, time, json, re, hashlib, html
root=Path(__file__).resolve().parents[1]
folder=root/'notes/geometry_FC_preview'
folder.mkdir(exist_ok=True)
urls=[
 'https://books.google.com/books?id=qJr6CAAAQBAJ&pg=PA5',
 'https://www2.math.upenn.edu/~chai/720f21/math720f21.html',
]
records=[]
for n,url in enumerate(urls):
    started=time.perf_counter()
    record={'url':url}
    try:
        with urllib.request.urlopen(url,timeout=30) as response:
            content=response.read()
            record.update(status=response.status, final_url=response.url,
                          bytes=len(content),elapsed_seconds=time.perf_counter()-started,
                          sha256=hashlib.sha256(content).hexdigest())
        target=folder/f'public_{n}.html'
        target.write_bytes(content)
        source=content.decode('utf-8','replace')
        title=re.search(r'<title[^>]*>(.*?)</title>',source,re.S|re.I)
        record['title']=html.unescape(title.group(1)) if title else None
        record['relevant_links']=[html.unescape(a) for a in re.findall(r'<a\b[^>]*>.*?</a>',source,re.I|re.S)
             if re.search(r'Faltings|Chai|Degeneration|\.pdf|PA5|content',a,re.I)][:50]
        record['image_urls']=re.findall(r'<img[^>]*src=["\']([^"\']+)',source,re.I)[:20]
        record['text_excerpt']=html.unescape(re.sub(r'<[^>]+>',' ',source))[:3000]
    except Exception as e:
        record.update(error=repr(e),elapsed_seconds=time.perf_counter()-started)
    records.append(record)
(root/'logs/geometry_FC_public_preview.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
