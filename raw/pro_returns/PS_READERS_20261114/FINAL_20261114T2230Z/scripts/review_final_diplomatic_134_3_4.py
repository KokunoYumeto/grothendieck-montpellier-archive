"""Record only diplomatic-PDF pages actually opened during the final visual check.

Use `next` to list unreviewed selections. Use `record` with a JSON list on stdin,
each item containing page, viewed:true and a page-specific observation, only
after the corresponding image has actually been opened. No view is inferred
from this script, rendering, image existence or extracted text.
"""
from pathlib import Path
import argparse,hashlib,json,sys
P=Path(__file__).resolve().parents[1];R=P/'records'
a=argparse.ArgumentParser();a.add_argument('command',choices=['next','record']);a.add_argument('--limit',type=int,default=6);args=a.parse_args()
selection=json.loads((R/'QA_SELECTION_PS_EN_diplomatic.json').read_text())
pdf=P/selection['pdf'];digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest==selection['pdf_sha256'],'The diplomatic PDF changed after the selection was prepared.'
target=R/'FINAL_VISUAL_QA_diplomatic_134_3_4.json'
evidence=json.loads(target.read_text()) if target.exists() else {'pdf':selection['pdf'],'pdf_sha256':digest,'entries':[]}
assert evidence['pdf_sha256']==digest,'Existing observations concern a different PDF snapshot.'
entries=evidence['entries'];by_page={x['page']:x for x in selection['selections']}
if args.command=='record':
    incoming=json.load(sys.stdin)
    for item in incoming:
        assert item.get('viewed') is True,'Actual image review must be explicitly affirmed.'
        page=item['page'];assert page in by_page,('Not a selected page',page)
        observation=item['observation'].strip();assert observation,('Missing page-specific observation',page)
        row=by_page[page];image=P/row['image'];assert image.exists(),('Missing rendered image',row['image'])
        entry={'pdf':selection['pdf'],'pdf_sha256':digest,'page':page,'image':row['image'],'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'key':row['key'],'viewed':True,'observation':observation}
        entries[:]=[x for x in entries if x['page']!=page];entries.append(entry)
    entries.sort(key=lambda x:x['page']);target.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
done={x['page'] for x in entries if x.get('viewed') is True}
remaining=[x for x in selection['selections'] if x['page'] not in done]
print(json.dumps({'reviewed':len(done),'selected':len(by_page),'remaining':len(remaining),'next':remaining[:args.limit]},ensure_ascii=False,indent=2))
