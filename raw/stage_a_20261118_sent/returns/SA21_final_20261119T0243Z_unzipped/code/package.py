"""Package authored work and reproducibility evidence; never bundle source inputs.

Invoke only at the requested45-minute checkpoints or at final delivery.
Externally retrieved full publications are research inputs, not deliverables.
Search requests, URLs, source reference IDs, byte counts and hashes are retained;
raw publisher text is replaced by that retrieval metadata in the ZIP only.
"""
from pathlib import Path
import argparse,hashlib,json,re,zipfile

R=Path(__file__).resolve().parents[1]
def sha(b):return hashlib.sha256(b).hexdigest()
def external_input(p):
 s=p.as_posix(); n=p.name.lower()
 if '__pycache__' in p.parts or p.suffix.lower() in ['.pyc','.pdf','.png','.jpg','.jpeg','.lean','.zip','.html']:return True
 if p.suffix.lower()=='.txt' and (R/p).with_suffix('.pdf').exists():return True
 if 'primary' in p.parts and p.suffix.lower() in ['.txt','.html']:return True
 if n in ['birkhoff1948.txt','stong1966.txt','kochen_specker1967.txt']:return True
 if 'project_links' in p.parts and (n.endswith('.numbered.txt') or n in ['context_navigation.txt','context_navigation.json','narrow_candidates_output.txt','secondary_candidates_output.txt','open_missing_candidates_output.txt']):return True
 return False
def retrieval_json(p,obj):
 s=p.as_posix()
 return isinstance(obj,dict) and (any(k in obj for k in ['result','results','response']) and ('request' in obj or 'query' in obj) or ('content' in obj and 'isError' in obj)) or bool(re.search(r'/(?:web_\d+|(?:open|search)_[A-Z][A-Z0-9]*_\d+|(?:search|open)_\d+)\.json$',s))
def source_echo(p):
 return ('read_outputs' in p.parts and p.suffix=='.txt') or bool(re.match(r'J156-\d+-\d+_read\.txt$',p.name)) or (str(p.parent)=='outputs' and bool(re.match(r'(?:entries|text|doubts|index)_\d+_\d+\.txt$',p.name))) or str(p)=='parts/cotes_9_14_18/source_checks.txt'
def sanitize(p,b):
 if source_echo(p):
  cleaned={'output_kind':'source-reading echo metadata','original_output_bytes':len(b),'original_output_sha256':sha(b),'original_output_line_count':b.count(b'\n'),'preservation_note':'This executed reading output reproduced the attached source text. Its content is omitted from the package to avoid copying the original inputs. Full-reading coverage, line maps, hashes and curated claim/reading decisions are retained. Reproduce the verbatim output with the preserved reader program and the original attached source.'}
  return (json.dumps(cleaned,ensure_ascii=False,indent=2)+'\n').encode(),True
 if p.suffix!='.json':return b,False
 try:o=json.loads(b)
 except Exception:return b,False
 if not retrieval_json(p,o):return b,False
 st=json.dumps(o,ensure_ascii=False)
 request=o.get('request',o.get('queries',o.get('query',{'urls':o.get('urls')} if o.get('urls') else None))) if isinstance(o,dict) else None
 urls=sorted(set(re.findall(r'https?://[^\s\"<>\)\]\\]+',st)))
 refs=sorted(set(re.findall(r'turn\d+[a-z]+\d+',st)))
 errors=sorted(set(re.findall(r'[^\n]{0,50}(?:403|404|502|503|DisabledError|not accessible|Failed to fetch)[^\n]{0,110}',st)))[:20]
 cleaned={'request':request,'source_urls':urls,'tool_reference_ids':refs,'retrieved_payload_sha256':sha(b),'retrieved_payload_bytes':len(b),'access_error_indicators':errors,'preservation_note':'Retrieval metadata retained. Full third-party or recovered-context response text omitted; curated mathematical assessments and precise locators are in the claims, bibliography and source-check reports. Any preserved request was executed, not merely proposed.'}
 return (json.dumps(cleaned,ensure_ascii=False,indent=2)+'\n').encode(),True
def main():
 ap=argparse.ArgumentParser();ap.add_argument('output');ap.add_argument('--kind',choices=['checkpoint','final'],required=True);ap.add_argument('--utc',required=True);a=ap.parse_args()
 out=Path(a.output).resolve();assert out.parent!=R and not out.exists(), 'Never overwrite a checkpoint or an existing package.'
 records=[];excluded=[]
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(R.rglob('*')):
   if not p.is_file():continue
   rel=p.relative_to(R)
   if external_input(rel):excluded.append({'path':str(rel),'reason':'external publication/input, cache, or nested archive'});continue
   b=p.read_bytes();packed,redacted=sanitize(rel,b)
   z.writestr(str(rel),packed)
   records.append({'path':str(rel),'bytes':len(packed),'sha256':sha(packed),'retrieval_text_replaced_by_metadata':redacted})
  manifest={'package_kind':a.kind,'created_utc':a.utc,'file_count':len(records),'files':records,'excluded_inputs':excluded,'input_restore':'Use the originally attached SA21_notes.zip and SA21_texts.zip. Additional prior-context source identity is in audit/prior_context_manifest.json; external sources are reproducible from URLs and fetch scripts.'}
  z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 with zipfile.ZipFile(out) as z:assert z.testzip() is None
 print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'sha256':sha(out.read_bytes()),'authored_and_evidence_files':len(records),'external_inputs_omitted':len(excluded)},indent=2))
if __name__=='__main__':main()
