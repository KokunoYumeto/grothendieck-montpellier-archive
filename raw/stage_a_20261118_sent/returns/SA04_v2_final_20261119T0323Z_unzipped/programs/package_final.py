"""Package the completed dossier, its audit records and programs as SA04.zip.

Original attachments, external primary-source copies, raw web captures, caches
and earlier checkpoint ZIPs are deliberately excluded. No checkpoint is created.
"""
from pathlib import Path
import json,csv,datetime,hashlib,zipfile
W=Path(__file__).resolve().parents[1];ROOT=W.parent;F=W/'final';OUT=ROOT/'SA04.zip'
validation=json.loads((F/'FINAL_VALIDATION.json').read_text())
assert validation['passed'],validation['errors']
assert not OUT.exists(),'Final archive already exists; inspect before replacing it.'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (W/'progress.log').open('a') as log:
 for stage,description in [
 ('STAGE_1_COMPLETE','All432 indexed notes manually compared with source passages; all59 root transcription-derived and6 supplemental items have no invented index rows; final source locator reconciliation passed.'),
 ('STAGE_2_COMPLETE','All372 final claims have searched fates, exact source statuses, saved calculation/proof evidence and reference qualifications. All items, claims and references have check events.'),
 ('STAGE_3_COMPLETE','131 consolidated historical problems; settled questions, present open scope and identification limits distinguished. Exact duplicate Verschiebung question consolidated.'),
 ('STAGE_4_COMPLETE','163 reading alarms with concrete locators; Pro/Codex alternatives preserved; no source transcription modified.'),
 ('STAGE_5_COMPLETE','90 typed links;31 external-project leads extracted separately; checked folder and published endpoints distinguished from unavailable-project leads.'),
 ('STAGE_6_COMPLETE','30 directions ranked by interest and few-hour feasibility; all source IDs checked; no further direction developed.'),
 ('FINAL_VALIDATION','Entry bijection, schemas, identifiers, citation keys, event taxonomy/coverage, claim-search coverage, source boundaries/hashes and computation outputs all pass.'),
 ('END','Research and final review complete; final archive packaging begins. Stage completion times are recorded here because the research streams overlapped; no unobserved earlier stage-start time is invented.')]:
  log.write(now+'\t'+stage+'\t'+description+'\n')
files=[];excluded=[];names=set()
for p in sorted(W.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(W)
 if rel.parts[0]=='evidence' or p.name=='search_capture.json' or '__pycache__' in rel.parts or p.suffix.lower() in {'.zip','.pdf','.dvi','.png','.jpg','.jpeg'}:
  excluded.append(str(rel));continue
 # Packaging receipt is created after the archive; it cannot hash itself.
 if rel==Path('outputs/final_package.json') or rel==Path('outputs/final_package_stdout.json'):continue
 arc=str(Path(*rel.parts[1:])) if rel.parts[0]=='final' else str(rel)
 assert arc not in names,arc
 names.add(arc);files.append((p,arc))
required={'SA04_dossier.md','SA04_entries.tsv','SA04_items.json','SA04_claims.json','SA04_problems.json','SA04_readings.tsv','SA04_links.tsv','SA04_directions.md','SA04_references.bib','CHECK_EVENTS.tsv','progress.log'}
assert required<=names,required-names
manifest={'created_utc':now,'archive':'SA04.zip','status':'completed','counts':validation['counts'],'directions':30,'overview_words':validation['overview_words'],'source_inputs':'Original user archives and standalone instructions are identified in SOURCE_MANIFEST.json and not copied as input files. Line-numbered source-read outputs are retained as audit-program output.','external_sources':'Primary PDFs/OCR and raw web captures are excluded; bibliography and search ledgers preserve exact references, checked scope and retrieval metadata.','earlier_checkpoints':[r['checkpoint'] for r in csv.DictReader((W/'CHECKPOINTS.tsv').open(),delimiter='\t')],'exclusions':excluded,'files':[{'path':arc,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p,arc in files]}
with zipfile.ZipFile(OUT,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p,arc in files:z.write(p,arc)
 z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(OUT) as z:
 assert z.testzip() is None
 assert required<=set(z.namelist())
 assert len(z.namelist())==len(set(z.namelist()))
 assert not any(n.endswith('.zip') for n in z.namelist())
 for r in manifest['files']:
  data=z.read(r['path']);assert len(data)==r['bytes'];assert hashlib.sha256(data).hexdigest()==r['sha256']
 assert len(list(csv.DictReader(z.read('SA04_entries.tsv').decode().splitlines(),delimiter='\t')))==432
receipt={'file':str(OUT),'created_utc':now,'bytes':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'files':len(files)+1,'all_member_hashes_verified':True,'zip_crc_verified':True,'only_final_download':'SA04.zip'}
(W/'outputs/final_package.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
