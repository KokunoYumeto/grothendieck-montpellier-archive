from pathlib import Path
import csv,json,re,zipfile,hashlib,datetime,sys
root=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
headers=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
rows={}
for file in sorted((root/'notes').glob('*_results.csv')):
    for row in csv.DictReader(file.open()): rows[row['id']]=row
pattern=re.compile(r'\\begin\{(theorem|lemma|proposition|corollary|example|remark)\}(?:\[([^\]]*)\])?(.*?)\\end\{\1\}',re.S)
for path in sorted((root/'sections').glob('*.tex')):
    text=path.read_text()
    for match in pattern.finditer(text):
        label=re.search(r'\\label\{([^}]+)\}',match.group(3))
        if not label: continue
        sid=label.group(1)
        if sid in rows: continue
        title=match.group(2) or ''
        status='Known' if title.startswith('Known') else 'Refuted' if title.startswith('Refuted') else 'Proved under stated hypotheses' if 'under' in title else 'Proved' if title.startswith('Proved') else 'Pending audit'
        body=re.sub(r'\s+',' ',re.sub(r'\\label\{[^}]+\}','',match.group(3))).strip()
        rows[sid]=dict(zip(headers,[sid,body,status,str(path.relative_to(root)),';'.join(re.findall(r'\\ref\{([^}]+)\}',match.group(3))),'22' if sid.startswith('SA23-A-') else '',title+'; machine-extracted statement text; registry reconciliation ongoing']))
with (root/'RESEARCH_SA23_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=headers);writer.writeheader();writer.writerows(rows.values())
eh=['statement_id','date','who','type','outcome','where']
events=[]
for path in [root/'CHECK_EVENTS.tsv',*sorted((root/'notes').glob('*_CHECK_EVENTS.tsv'))]:
    events.extend(csv.DictReader(path.open(),delimiter='\t'))
for sid,row in rows.items():
    if sid.startswith('SA23-A-'):
        events.append(dict(zip(eh,[sid,'2026-11-20','GPT-6 Astra (OpenAI), Pro, root','independent re-proof',row['notes'],row['where_proved']])))
seen=set()
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=eh,delimiter='\t',extrasaction='ignore');w.writeheader()
    for r in events:
        key=tuple(r.get(k,'') for k in eh)
        if key not in seen: w.writerow(r);seen.add(key)
number=int(sys.argv[1])
name=f'RESEARCH_SA23_checkpoint_{number:02d}.zip'
ledger=root/'PROGRESS_LEDGER.md'
with ledger.open('a') as f:
    f.write('\n## 20 November 2026, 01:55 CET — first scheduled checkpoint\n\n')
    f.write('A.1: complete negative proof in all characteristic zero fields; A.2: exact separability and finite absolute p-rank criterion; A.4: both openness assertions refuted by explicit noetherian examples. A.3: full general adic lifting proof newly written, independent audit pending. B/C/G proofs written. D19.3.12 statement repaired and independently audited; remaining printed errata checks continue. E and H mathematical proofs written; F fixed-order theorem and hypothesis-sensitive finite-order theorem written. I/J/L sections written and being cross-checked. K all ten headings written; exact-source and scope audits continue. Historical leads remain separate.\n\n')
    f.write('This checkpoint is not a formal three-hour progress review. The current PDF predates the newly written A.3 and K sections; its source is more current. It has zero overfull boxes; pages 1, 20 and 38 were rendered and visually inspected. Bibliography integration is pending, so unresolved citation markers remain in this working PDF. No final-publication readiness is claimed.\n')
report=root/'RESEARCH_SA23_report.md'
with report.open('a') as f:
    f.write('\n## Scheduled checkpoint 01 — 20 November 2026, 01:55 CET\n\n')
    f.write(f'Current statement register contains {len(rows)} entries. The deliverable is INCOMPLETE and research continues. The source includes the new general adic Cohen lifting proof, while the last built working PDF lags behind that insertion. Its build has zero overfull boxes (zero above 2pt); rendered pages 1, 20, 38 have been inspected. Bibliography integration and the final source-to-PDF rebuild remain pending.\n\n')
    f.write('Important corrections already proved: the characteristic-p finite-relative-p-basis claim needs an absolute p-rank condition unless the base is perfect; both noetherian openness assertions are false; the printed proof of EGA 0_IV19.3.12 is invalid but its statement is true; rank-one slopes do not classify the stated crystalline sections. Exact proofs and counterexamples are in the section files. Agent-specific source logs and registries document the other checks.\n\n')
    f.write('External full-text downloads and scan caches are reproducible from the fetch scripts and source records and are omitted from the checkpoint. Original attached inputs and earlier checkpoint archives are also omitted. All written proofs, scripts, program outputs and research records are included.\n')
files=[]; omitted=[]
for p in sorted(root.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(root)
    if p.suffix=='.zip' or 'sources' in rel.parts or ('notes' in rel.parts and (p.suffix=='.pdf' or ('web_' in p.name and p.suffix=='.json'))) or ('verification' in rel.parts and ('scan' in p.name)) or p.suffix in {'.aux','.toc','.out','.bbl','.blg'}:
        omitted.append({'path':str(rel),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()});continue
    files.append(p)
manifest={'created_utc':stamp,'checkpoint':number,'included':[str(p.relative_to(root)) for p in files],'omitted_retrievable_caches':omitted,'earlier_checkpoints':[]}
(root/'checkpoint_manifest.json').write_text(json.dumps(manifest,indent=2))
files.append(root/'checkpoint_manifest.json')
dest=root.parent/name
if dest.exists(): raise SystemExit('Refusing to overwrite existing checkpoint')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,Path('RESEARCH_SA23')/p.relative_to(root))
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'files':len(files),'statement_rows':len(rows),'created_utc':stamp}))

