"""Capture, package, and verify the complete two-archive delivery."""
from pathlib import Path
import argparse,csv,hashlib,json,shutil
from archive_contents import capture,prepare,write_captured_zip,files
from verify_final_archives import verify

P=Path(__file__).resolve().parents[1]
STEMS=['PS_EN_diplomatic','PS_EN_corrected_apparatus','PS_EN_reading','PS_EN_master_annotated','PS_GUIDE']
EN_FILES={f'readers/{stem}.{extension}' for stem in STEMS for extension in ['tex','pdf']}|{'README.md','TYPESETTING_REPORT.md','APPARATUS_COUNTS.md'}

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,default=P.parent);parser.add_argument('--restore-test',action='store_true',help='Compatibility option: full restoration and final-publication verification always run.');args=parser.parse_args()
 gate=json.loads((P/'records/FINAL_QA_GATE.json').read_text());assert gate['complete'],gate['issues']
 for relative,expected in gate['validated_input_sha256'].items():
  path=(P/relative).resolve();assert path.is_relative_to(P)
  assert hashlib.sha256(path.read_bytes()).hexdigest()==expected,'QA evidence changed: '+relative
 privacy=json.loads((P/'records/PRIVACY_AUDIT.json').read_text());assert privacy['complete'] and not privacy['issues']
 coverage=json.loads((P/'records/COVERAGE_AUDIT.json').read_text());assert coverage['complete'] and coverage['checked_page_files']==706
 replay=json.loads((P/'records/CHANGE_REPLAY_AUDIT.json').read_text());assert replay['equal_pages']==706 and not replay['exceptions']
 omissions=list(csv.DictReader((P/'records/FINAL_OMISSIONS.tsv').open(),delimiter='\t'));excluded=set()
 for row in omissions:
  relative=row['path'];source=P/relative;replacement=P/row['replacement']
  assert relative not in excluded and source.suffix=='.pdf' and source.parent!=P/'readers'
  assert source.resolve().is_relative_to(P) and replacement.resolve().is_relative_to(P)
  assert row['replacement'] in EN_FILES and replacement.suffix=='.pdf'
  assert source.stat().st_size==int(row['bytes']) and hashlib.sha256(source.read_bytes()).hexdigest()==row['sha256']
  assert hashlib.sha256(replacement.read_bytes()).hexdigest()==row['replacement_sha256'] and row['reason']
  excluded.add(relative)
 assert excluded=={p.relative_to(P).as_posix() for p in P.rglob('*.pdf') if p.parent!=P/'readers'}
 args.destination.mkdir(parents=True,exist_ok=True)
 destinations=[args.destination/'PS_READERS_EN.zip',args.destination/'PS_READERS_RECORDS.zip']
 assert not any(p.exists() for p in destinations),'Final archive destinations already exist; select a fresh destination.'
 plan={'archives':{'PS_READERS_EN.zip':sorted(EN_FILES),'PS_READERS_RECORDS.zip':'Every remaining project file except explicitly superseded intermediate PDFs, with exact-byte duplicate images represented by records/FILE_ALIASES.tsv.'},'excluded':'Original supplied inputs, earlier ZIP archives, interpreter bytecode caches, and the exact superseded intermediate PDF versions listed in records/FINAL_OMISSIONS.tsv.','intermediate_pdf_omissions':len(excluded),'snapshot':'All file bytes are captured before manifests and archive members are written.','extraction':'Extract both ZIPs into the same directory, then run python3 scripts/restore_file_aliases.py.','verification':'Run python3 scripts/verify_final_archives.py PS_READERS_EN.zip PS_READERS_RECORDS.zip --restore --final-gate with paths to the two archives.','qa_gate_sha256':hashlib.sha256((P/'records/FINAL_QA_GATE.json').read_bytes()).hexdigest()}
 (P/'records/FINAL_ARCHIVE_PLAN.json').write_text(json.dumps(plan,indent=2)+'\n')
 with capture(P,excluded=excluded) as snapshot:
  prepared=prepare(snapshot);allfiles=files(snapshot)
  en=[p for p in allfiles if p.relative_to(snapshot).as_posix() in EN_FILES]
  assert len(en)==len(EN_FILES)
  records=[p for p in allfiles if p not in en]
  write_captured_zip(snapshot,destinations[0],en,prepared)
  write_captured_zip(snapshot,destinations[1],records,prepared)
  result=verify(destinations,restore=True,final_gate=True)
  for name in ['FILE_ALIASES.tsv','ARCHIVE_CONTENTS.tsv']:shutil.copyfile(snapshot/'records'/name,P/'records'/name)
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
