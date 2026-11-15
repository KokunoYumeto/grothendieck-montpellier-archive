"""Integrate the tested mechanical layout pipeline into all checked source pages.

Run once after the completed page reviews and local proof repairs are frozen.
Every text hunk receives a CHECK_DECISIONS row, with hashes guarding replay.
"""
from pathlib import Path
import csv,difflib,hashlib,json
from build_readers import normalize,repair_diagram_separators,repair_macro_layout,preserve_front_lineation,local_layout_repairs
P=Path(__file__).resolve().parents[1];R=P/'records'
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def write_tsv(path,fields,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
files=sorted((P/'checked_pages').glob('*.tex'))
if len(files)!=706:raise SystemExit('All 706 checked source pages are required before integration.')
state_path=R/'SOURCE_NORMALIZATION.json'
if state_path.exists():
    state=json.loads(state_path.read_text())
    for path in files:
        assert digest(path.read_text())==state['pages'][path.stem]['after_sha256'],path.stem
    print(json.dumps({'already_integrated':True,'pages':len(files)}));raise SystemExit(0)
decisions=[];fixes=[];pages={};outputs={}
for path in files:
    key=path.stem;raw=path.read_text();start=len(fixes)
    out=local_layout_repairs(preserve_front_lineation(repair_macro_layout(repair_diagram_separators(normalize(raw,key,fixes),key,fixes),key,fixes),key,fixes),key,fixes)
    outputs[path]=out
    before=raw.splitlines(keepends=True);after=out.splitlines(keepends=True);ordinal=0
    for tag,i,j,k,l in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        if tag=='equal':continue
        ordinal+=1
        decisions.append({'key':key,'cote':key.split('_')[1],'site':int(key.rsplit('_',1)[1]),'line':i+1,
          'transcription_reading':''.join(before[i:j]),'image_reading':''.join(after[k:l]),'arxiv_reading':'',
          'decision':'mechanical source integration; reading unchanged',
          'reason':'Integrate the already tested normalization and local typesetting repairs into the canonical checked page. The associated TYPESETTING_FIXES_NORMALIZATION entries explain the mechanical operations; no source reading is newly inferred.',
          'source_id':f'MECH:{key}:integrated:{ordinal}'})
    pages[key]={'before_sha256':digest(raw),'after_sha256':digest(out),'changed':raw!=out,'recorded_hunks':ordinal,'mechanical_operations':len(fixes)-start}
for path,out in outputs.items():path.write_text(out)
write_tsv(R/'CHECK_DECISIONS_NORMALIZATION.tsv',['key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','source_id'],decisions)
write_tsv(R/'TYPESETTING_FIXES_NORMALIZATION.tsv',['reader','page_key','source_line','what_was_wrong','what_was_done'],fixes)
state={'complete':True,'pages':pages,'changed_pages':sum(p['changed'] for p in pages.values()),'recorded_hunks':len(decisions),'mechanical_operations':len(fixes)}
state_path.write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({k:v for k,v in state.items() if k!='pages'}))
