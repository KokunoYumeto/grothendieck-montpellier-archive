"""Record explicitly authored observations after opening final guide page images."""
from pathlib import Path
import argparse,hashlib,json
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('observations',help='JSON list of page, observation, status; pages must actually have been opened');args=a.parse_args()
selection=json.loads((P/'records/QA_SELECTION_PS_GUIDE.json').read_text())
pdf=P/selection['pdf'];assert hashlib.sha256(pdf.read_bytes()).hexdigest()==selection['pdf_sha256'],'PDF changed after page selection'
selected={r['page']:r for r in selection['selections']}
new=json.loads((P/args.observations).read_text());dest=P/'records/FINAL_VISUAL_QA_guide_134_5_6.json'
old=json.loads(dest.read_text()) if dest.exists() else []
ids={(r['pdf_sha256'],r['page']) for r in old}
for x in new:
 assert x['page'] in selected and x['status'] in ['pass','issue'] and x['observation'].strip()
 assert x.get('image_opened') is True,'An observation must attest actual opening, not selection alone'
 row=dict(selected[x['page']]);assert (P/row['image']).exists()
 row.update(x);row['viewed']=True;row['reviewer']='134_5_6'
 identity=(row['pdf_sha256'],row['page']);assert identity not in ids,'Do not overwrite a prior observation silently'
 old.append(row);ids.add(identity)
dest.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print('Recorded observations:',len(old),'for final PDF',selection['pdf_sha256'])
