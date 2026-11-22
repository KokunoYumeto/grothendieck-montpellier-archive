"""Read actual first-page PDF links in the existing Grothendieck bibliography."""
from pathlib import Path
import datetime,json,time,fitz
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
source=root/'sources/algebra_history_AG_bibliotex.pdf'
doc=fitz.open(source)
links=[]
for entry in doc[0].get_links():
    if 'uri' in entry:
        rect=entry['from']
        context=doc[0].get_textbox(fitz.Rect(0,rect.y0-22,doc[0].rect.width,rect.y1+2))
        links.append({'uri':entry['uri'],'context':context})
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'source':str(source.relative_to(root)),'physical_pages_inspected_as_text':[1],
        'links':links,'elapsed_seconds':time.perf_counter()-start}
(root/'logs/root_1954_notes_locate.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
