"""Record observations only after the operator has actually opened each image."""
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parents[1]
stem,owner=sys.argv[1:3]
selection=json.loads((P/'records'/('QA_SELECTION_'+stem+'.json')).read_text())
pdf=P/selection['pdf'];sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert sha==selection['pdf_sha256']
chosen={r['page']:r for r in selection['selections']}
changed=set()
for auditfile in (P/'records').glob('RASTER_EQUIVALENCE_'+stem+'_*.json'):
    audit=json.loads(auditfile.read_text())
    if audit.get('new_pdf_sha256')==sha and audit.get('audit_complete') is True:
        changed.update(audit.get('changed_pages',[]))
target=P/'records'/('FINAL_VISUAL_QA_'+stem+'_'+owner+'.json')
old=json.loads(target.read_text()) if target.exists() else {'pdf':selection['pdf'],'pdf_sha256':sha,'entries':[]}
assert old['pdf_sha256']==sha
entries={r['page']:r for r in old['entries']}
for observation in json.load(sys.stdin):
    page=observation['page']
    if page in chosen:row=dict(chosen[page])
    else:
        assert page in changed,'An extra page must be a changed page from a verified current-PDF raster audit'
        row={'pdf':selection['pdf'],'pdf_sha256':sha,'page':page,'key':None,
             'image':f'qa/rendered/final_{stem}/page_{page:04d}.png',
             'reasons':['changed page after final visual repairs; fresh current-PDF image inspection']}
    row['viewed']=True;row['image_opened']=True;row['direct_image_opened']=True
    row['inspection_method']='actually opened current-PDF page image'
    row['observation']=observation['observation'];assert row['observation'].strip()
    row['image_sha256']=hashlib.sha256((P/row['image']).read_bytes()).hexdigest()
    entries[page]=row
old['entries']=[entries[p] for p in sorted(entries)]
target.write_text(json.dumps(old,indent=2)+'\n')
print(json.dumps({'file':str(target.relative_to(P)),'recorded_pages':sorted(entries)}))
