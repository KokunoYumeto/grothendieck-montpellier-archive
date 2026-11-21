"""Verify an immutable deliverable ZIP against every recorded member hash."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
p=Path(sys.argv[1]).resolve();receipt=Path(sys.argv[2]).resolve()
sha=lambda data:hashlib.sha256(data).hexdigest()
with zipfile.ZipFile(p) as z:
 names=z.namelist();assert len(names)==len(set(names));assert all(n.startswith('KTOWER/') and '..' not in Path(n).parts for n in names)
 assert not any(n.lower().endswith('.zip') for n in names)
 for n in ['KTOWER.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md','PACKAGE_MANIFEST.json']:assert 'KTOWER/'+n in names,n
 m=json.loads(z.read('KTOWER/PACKAGE_MANIFEST.json'))
 assert len(m['files'])+1==len(names)
 for row in m['files']:
  data=z.read('KTOWER/'+row['path']);assert len(data)==row['bytes'] and sha(data)==row['sha256'],row['path']
 pdf='KTOWER/KTOWER.pdf' in names
 if pdf:
  q=json.loads(z.read('KTOWER/PDF_REVIEW.json'))
  assert q['complete_visual_review'] and q['tex_sha256']==sha(z.read('KTOWER/KTOWER.tex')) and q['pdf_sha256']==sha(z.read('KTOWER/KTOWER.pdf'))
  assert b'%%EOF' in z.read('KTOWER/KTOWER.pdf')[-100:]
  assert q['pages']==len(q['pages_rendered'])
 rv=json.loads(z.read('KTOWER/PROGRESS_REVIEWS.json'))['reviews']
 r={'verified_utc':datetime.now(timezone.utc).isoformat(),'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'manifest_files':len(m['files']),'all_member_hashes_match':True,'all_required_deliverables':True,'nested_zips':False,'optional_pdf_included':pdf,'pdf_exact_review_match':pdf,'pdf_pages':q['pages'] if pdf else None,'latest_review_in_archive':rv[-1]['number'],'archive_created_utc':m['created_utc']}
receipt.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
