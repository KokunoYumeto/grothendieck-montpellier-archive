"""Render the final CP20 pages and compare them with actually reviewed first-build images."""
from pathlib import Path
import json,hashlib,datetime
import fitz
w=Path(__file__).resolve().parents[1]
prior=json.loads((w/'outputs/visual_qa20_pending.json').read_text())
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');assert len(d)==prior['pages_in_pdf']
folder=w/'outputs/qa20_final';assert not folder.exists();folder.mkdir()
same=[];changed=[]
for num in prior['pages_rendered']:
    name=f'page_{num:03d}.png';target=folder/name
    d[num-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(target)
    initial=w/'outputs/qa20'/name
    pair={'page':num,'initial_sha256':hashlib.sha256(initial.read_bytes()).hexdigest(),
          'final_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
    (same if pair['initial_sha256']==pair['final_sha256'] else changed).append(pair)
record=dict(prior);record['manual_visual_review']='PENDING FINAL CHANGED IMAGE INSPECTION'
(w/'outputs/visual_qa20_final_pending.json').write_text(json.dumps(record,indent=2)+'\n')
comparison={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status':'BYTE COMPARISON COMPLETE','same':same,'changed':changed,
            'scope':'Exact rendered-image comparison only. Prior actual inspection and fresh inspection of changed images are separately recorded.'}
(w/'outputs/checkpoint20_QA_image_comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
print(json.dumps({'same_pages':[x['page'] for x in same],'changed_pages':[x['page'] for x in changed],
                  'pdf_pages':len(d)},indent=2))
