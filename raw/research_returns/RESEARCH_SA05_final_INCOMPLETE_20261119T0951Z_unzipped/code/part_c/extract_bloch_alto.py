"""Read the library's primary OCR HTML pages; preserve extracted full text.
A preliminary BeautifulSoup attempt failed (dependency absent), and a strict
XML attempt failed because these are multiple HTML fragments, not ALTO XML.
The standard-library HTML parser below handles that format.
"""
from pathlib import Path
from html.parser import HTMLParser
class P(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,data):
  if data.strip():self.parts.append(data.strip())
for p in sorted((Path(__file__).resolve().parents[2]/'part_c'/'sources').glob('gdz_bloch*.html')):
 q=P();q.feed(p.read_text());t=' '.join(q.parts)
 p.with_suffix('.txt').write_text(t)
 print(p.name,t)
