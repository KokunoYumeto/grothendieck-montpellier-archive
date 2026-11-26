"""Audit availability and byte identity, without evaluating mathematical claims."""
from pathlib import Path
import csv,json,re,hashlib,zipfile,collections
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'deliverable';SRC=ROOT/'source'
def tsv(name,fields,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
archive=ROOT/'upload/SA03_Gomtrie_et_topologie_combinatoire_part3.zip'
inventory=[]
with zipfile.ZipFile(archive) as z:
    for name in sorted(z.namelist()):
        if name.endswith('/'):continue
        original=z.read(name);p=SRC/name;actual=p.read_bytes()
        inventory.append(dict(file=name,bytes=len(actual),sha256=hashlib.sha256(actual).hexdigest(),unchanged=actual==original))
assert all(x['unchanged'] for x in inventory),'A supplied source was modified'
tsv('SOURCE_MANIFEST.tsv',['file','bytes','sha256','unchanged'],inventory)
markers=[];files=[];cote_scans=collections.defaultdict(set);witness=collections.defaultdict(set)
owners={
 'MPL_91_019-058':'a','MPL_91_059-098':'b','MPL_91_099-143':'c','MPL_93_002-046':'d',
 **{f'K91-{i:02d}':('a' if i<=4 else 'b' if i<=7 else 'c') for i in range(1,11)},
 **{f'K93-{i:02d}':('a2' if i<=3 else 'b2' if i<=6 else 'c2' if i<=9 else 'd') for i in range(1,13)}}
for p in sorted((SRC/'SA03_texts').glob('*/*_transcription.tex')):
    rel=p.relative_to(SRC).as_posix();text=p.read_text();lines=text.splitlines()
    cote=int(re.search(r'\\cotefile\{(\d+)\}',text).group(1))
    found=[(int(m.group(1)),i+1) for i,line in enumerate(lines) if (m:=re.search(r'\\scanpage\{(\d+)\}',line))]
    package=p.name.removesuffix('_transcription.tex');source_type=p.parent.name
    files.append(dict(file=rel,cote=cote,witness=source_type,owner=owners[package],lines=len(lines),scan_markers=len(found),scans=','.join(str(n) for n,_ in found),coverage='Entire supplied file read by assigned owner; see part reading logs and source-read outputs.'))
    for j,(scan,start) in enumerate(found):
        end=found[j+1][1]-1 if j+1<len(found) else len(lines)
        markers.append(dict(cote=cote,scan=scan,file=rel,line_start=start,line_end=end,owner=owners[package]))
        cote_scans[cote].add(scan);witness[(cote,source_type)].add(scan)
tsv('TRANSCRIPTION_COVERAGE.tsv',['file','cote','witness','owner','lines','scan_markers','scans','coverage'],files)
tsv('SCAN_LOCATORS.tsv',['cote','scan','file','line_start','line_end','owner'],markers)
topic=[]
for line in (SRC/'SA03_texts/TOPIC.md').read_text().splitlines():
    if not re.match(r'\|\s*\d+\s*\|',line):continue
    cells=[s.strip() for s in line.strip('|').split('|')]
    cote=int(cells[0]);n=int(cells[2]);scans=sorted(cote_scans[cote])
    topic.append(dict(cote=cote,catalogue_title=cells[1],catalogue_pages=n,topic_pro=cells[3],topic_codex=cells[4],topic_api=cells[5],in_this_run=cells[6],
      supplied_unique_scan_numbers=len(scans),supplied_scans=','.join(map(str,scans)),
      catalogue_numbers_without_transcription=','.join(str(x) for x in range(1,n+1) if x not in scans),
      scope='Part 3: all supplied transcriptions read; absent scan numbers are availability gaps, not silently reconstructed.' if cote in {91,93} else 'Other part of SA03. Catalogue row audited; no transcription supplied and no claim imported.'))
tsv('TOPIC_COVERAGE.tsv',list(topic[0]),topic)
summary=dict(input_files=len(inventory),all_input_files_unchanged=True,topic_cotes=len(topic),transcription_files=len(files),
    pro_transcriptions=sum(x['witness']=='pro' for x in files),codex_transcriptions=sum(x['witness']=='codex' for x in files),
    transcription_scan_markers=len(markers),unique_scans_by_cote={str(c):len(s) for c,s in sorted(cote_scans.items()) if s},
    unique_scans_by_witness={f'{c}_{w}':len(s) for (c,w),s in sorted(witness.items())},
    no_scan_images_supplied=True,no_second_pass_files_supplied=True,
    note='Catalogue totals are not scan-marker totals; numbers not represented by a transcription are explicitly listed. Codex counts in TOPIC are historical inventory columns, not a count of the Codex files actually attached.')
(OUT/'outputs/source_audit.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
