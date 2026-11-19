"""Inventory source files and catalogue scope, without inferring judgments."""
from pathlib import Path
import csv,hashlib,json,re
W=Path(__file__).resolve().parents[1];ROOT=W.parent;F=W/'final';F.mkdir(exist_ok=True)
rows=[]
for line in (ROOT/'source/SA04_texts/TOPIC.md').read_text().splitlines():
 if not line.startswith('|'):continue
 cols=[x.strip() for x in line.strip('|').split('|')]
 if not cols[0].isdigit():continue
 rows.append(dict(cote=cols[0],catalogue_title=cols[1],catalogue_pages=cols[2],catalogue_Pro=cols[3],catalogue_Codex=cols[4],catalogue_API=cols[5],supplied_scope=cols[6],audit_scope='transcription/claims audit in this part' if cols[0] in ['93','98','100'] else 'catalogue inventory only; explicitly allocated to another part'))
with (F/'SOURCE_SCOPE.tsv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');writer.writeheader();writer.writerows(rows)
manifest=[]
for base in ['SA04_texts','SA04_notes','SA04_PROMPT']:
 for p in sorted((ROOT/'source'/base).rglob('*')):
  if not p.is_file():continue
  raw=p.read_bytes();entry={'file':str(p.relative_to(ROOT/'source')),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
  if p.suffix in ['.tex','.md','.tsv']:
   text=raw.decode('utf-8-sig');entry['lines']=len(text.splitlines())
   if p.suffix=='.tex' and p.name!='PREAMBLE.tex':
    cote=None;scans=[]
    for lineno,line in enumerate(text.splitlines(),1):
     m=re.search(r'\\cotefile\{([^}]+)\}',line)
     if m:cote=m[1]
     for n in re.findall(r'\\scanpage\{(\d+)\}',line):scans.append({'cote':cote,'scan':n,'line':lineno})
    entry['scan_markers']=scans
  manifest.append(entry)
for name in ['PROMPT(20261119-011401).md','README(20261119-011401).md']:
 p=ROOT/'upload'/name;raw=p.read_bytes();manifest.append({'file':'upload/'+name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'role':'standalone instruction;45-minute checkpoint cadence is authoritative'})
(F/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
(F/'READ_ME.md').write_text('''# SA04 dossier

Start with **SA04_dossier.md**. The five main data registers, reading alarms, links, ranked directions and bibliography sit beside it. `CHECK_EVENTS.tsv` records what was actually checked; textual comparison, proof, computation and use of a reference are different events.

The indexed-entry universe is exactly432 rows. The eight cote98 index entries are composite headings; their89 nested notes are individually reviewed as leaf items, while each parent receives only one indexed verdict. Additional transcription-derived items have no invented index rows. `ID_ALIASES.tsv` documents three exact final cross-stream consolidations and one reassigned source-entry association.

`SOURCE_SCOPE.tsv` inventories all30 catalogue rows. Only93,98 and100 belong to this part’s main folder audit. The separate cote161-5 is included because the second93 package and its indexed notes contain it. Cotes8,9 and4 in the mixed unindexed package are contextual; the cote100 portion begins at its own marker. Files for the other27 topic cotes are not supplied in this part, and their mathematics is not claimed to have been audited here. Scan numbers are not physical-page counts. No scan images or second-pass changes were supplied.

`parts/` preserves the detailed stream analyses, mathematical proofs, source comparisons and search ledgers. These working records retain their pre-consolidation identifiers; resolve aliases through `ID_ALIASES.tsv`. They are audit provenance, not alternative final verdict tables. `programs/` and `outputs/` preserve the written calculation/serialization/retrieval programs and their saved outputs. External primary-source PDFs/OCR and the original user attachments are not duplicated. Source hashes and scan-marker locations are in `SOURCE_MANIFEST.json`.

Reproduction: extract the original supplied archives into `source/SA04_texts`, `source/SA04_notes` and `source/SA04_PROMPT`, place this ZIP’s contents in `SA04_work`, and run the Python programs from their documented workspace root. Python3 and SymPy are used for exact algebra; external-source fetch/OCR helpers additionally use their named tools. Computational outputs identify the exact finite test range. A finite test is not a proof of an unrestricted statement unless the accompanying algebraic argument establishes it.

All source line numbers count UTF-8 text lines from1. `pro/` and `codex/` are relative to `source/SA04_texts`. A scan-reading alternative is never a decision about ink. A literature classD is a recorded unsuccessful exact-match search, not proof of historical absence; classF is an identification/formulation limit. Bibliography `note={verified}` means the recorded link or DOI was opened; each `annote` states whether that opening checked metadata, a theorem, or a proof passage.

Model: GPT-6 Astra Pro. The platform did not expose a numerical reasoning-effort setting; no effort label is invented. Audit reference date:19November2026. Progress and checkpoint timestamps areUTC.
''')
print(json.dumps({'topic_rows':len(rows),'main_cotes':sum(r['cote'] in ['93','98','100'] for r in rows),'other_part_rows':sum(r['cote'] not in ['93','98','100'] for r in rows),'source_files':len(manifest)}))
