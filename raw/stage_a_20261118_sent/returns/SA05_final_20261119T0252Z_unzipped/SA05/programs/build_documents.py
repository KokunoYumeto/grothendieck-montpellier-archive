#!/usr/bin/env python3
"""Assemble the authored overview with final counts and exact source orientation."""
import json,csv,re,zipfile,hashlib,datetime,collections
from pathlib import Path
B=Path(__file__).resolve().parents[1];W=B.parent
counts=json.loads((B/'counts.json').read_text())
claims=json.loads((B/'SA05_claims.json').read_text())
refs=json.loads((B/'SA05_reference_ledger.json').read_text())
dirs=json.loads((B/'SA05_directions.json').read_text())
aliases=json.loads((B/'SA05_aliases.json').read_text())
idmap={**aliases['items'],**aliases['claims'],**aliases['problems']}
def canon(s,m):
 while s in m:s=m[s]
 return s
text=(B/'SA05_dossier_base.md').read_text()
text=re.sub(r'MP-SA05-\d+|SA05-C\d+|SA05-\d+',lambda m:canon(m.group(),idmap),text)
for old,new in sorted(aliases['references'].items(),key=lambda p:-len(p[0])):
 text=re.sub(r'(?<![A-Za-z0-9_-])'+re.escape(old)+r'(?![A-Za-z0-9_-])',new,text)
def table(rows,head):
 return ['| '+' | '.join(head)+' |','|'+'|'.join('---' for _ in head)+'|']+['| '+' | '.join(map(str,r))+' |' for r in rows]
tail=['## 9. Final counts and verification scope','',
 'These counts refer to the canonical tables. Source-specific audit copies retain their earlier IDs and snapshot counts; the alias and partition ledgers explain the joins. A corrected-entry verdict concerns the earlier note, whereas a claim status concerns the source assertion under its recorded interpretation. They are different classifications.','']
tail+=table([
 ('Indexed entries, all with passage-based verdicts',counts['entries']),
 ('Consolidated substantive items',counts['items']),
 ('Claim records, including explicitly labelled current refinements',counts['claims']),
 ('Current-run refinement records',sum(c['status_category']=='current-run refinement' for c in claims)),
 ('Problem records',counts['problems']),('Unresolved scan-reading alarms',counts['readings']),
 ('Ranked future directions; none developed',len(dirs)),
 ('Checked folder/published-work link rows',counts['links']-counts['project_leads']),
 ('Separate prior-project leads (also labelled in the combined links file)',counts['project_leads']),
 ('Unavailable archive-target leads, excluded from checked links',counts['separate_unavailable_archive_leads']),
 ('Unverified published backward-reference leads',counts['separate_unverified_reference_leads']),
 ('Recorded check events',counts['events']),('Search-ledger rows',counts['search_rows']),
 ('Canonical bibliography records',len(refs)),
 ('References with an opened URL/DOI to their stated extent',sum(r['note']=='verified' for r in refs)),
 ('References explicitly marked unverified',sum(r['note']=='unverified' for r in refs)),
 ('Merged item / claim / problem aliases',f"{counts['merged_item_aliases']} / {counts['merged_claim_aliases']} / {counts['merged_problem_aliases']}")],['Measure','Count'])
tail+=['','### Entry verdicts','']
tail+=table([(k,counts['verdicts'].get(k,0)) for k in ['kept','merged','corrected','withdrawn','rests on a misreading']],['Verdict','Entries'])
tail+=['','The final table uses “corrected” for substantive repairs to earlier notes, including overstatement or misinterpretation. The reason column records the precise correction. The zero standalone “withdrawn” count does not mean that no source statement was withdrawn: authorial withdrawals have their own item kind and claim status below.','',
 '### Item kinds','']
tail+=table(sorted(counts['item_kinds'].items()),['Kind','Items'])
tail+=['','### Historical-development classes','',
 'The first count includes all canonical records. The second excludes the40 explicitly labelled current-run refinements and therefore includes the remaining source assertions and expressly labelled comparison/boundary records. Neither column should be read as a count of proved theorems.','']
nonref=[c for c in claims if c['status_category']!='current-run refinement']
nr=collections.Counter(c['class'] for c in nonref)
labels={'A':'In his own later published work','B':'Developed by others into established results','C':'Partly developed; precise residue recorded','D':'No exact development found in the bounded recorded search','E':'Known before or standard at the time','F':'Exact assertion or provenance not identifiable from the supplied pages'}
tail+=table([(k,labels[k],counts['claim_classes'].get(k,0),nr.get(k,0)) for k in 'ABCDEF'],['Class','Meaning','All records','Excluding current refinements'])
tail+=['','### Status on the pages or explicit comparison status','']
tail+=table(list(counts['claim_statuses'].items()),['Status category','Claims'])
tail+=['','The46 false-as-stated records retain their exact interpretation, counterexample hypotheses and corrected target. Conditional reading cases remain conditional. The40 present refinements are separately identified and never represented as ink on the manuscript. A refutation event points to a real statement ID; the audit corrected pseudo-IDs, self-targets and targets that had different mathematical scope.','',
 '### Bibliographic exceptions and reproducibility','',
 'The following records remain explicitly unverified as direct external references: '+', '.join('`'+r['key']+'`' for r in refs if r['note']=='unverified')+'. A checked later comparison, attached primary transcription or publisher metadata is described at its actual extent and does not silently turn an inaccessible original into a read source. In particular, the full attached Delzant transcription was read even though its strict external-link status remains unverified.','',
 'The programs serialize manually authored judgments, perform explicit algebraic and finite computations, check source locators and validate joins. They do not generate note verdicts by keyword matching. `SA05_source_guide.md` explains the physical line system and restoration layout. `SA05_source_manifest.json` compares every extracted source byte-for-byte with the supplied archives. `programs/outputs/` and the scope output directories retain the actual execution reports. The archive manifest records each delivered file and its hash.','',
 'Completed stages: entry checking and consolidation; claims and searched fate; problems and opened-source status; undecided reading alarms; checked links plus separately labelled unavailable leads; ranked future tasks. No manuscript text was amended, no unavailable endpoint was invented, and no source proof or formal certificate is credited beyond the recorded check extent.','']
text=text.replace('<!-- FINAL_COUNTS -->','\n'.join(tail))
(B/'SA05_dossier.md').write_text(text)

# Independently establish source preservation against the supplied ZIP bytes.
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attachments':[],'source_files':[]}
for name,sub in [('SA05_notes.zip','notes'),('SA05_texts.zip','texts')]:
 a=W/'upload'/name;manifest['attachments'].append({'name':name,'sha256':hashlib.sha256(a.read_bytes()).hexdigest(),'bytes':a.stat().st_size})
 with zipfile.ZipFile(a) as z:
  for member in z.infolist():
   if member.is_dir():continue
   data=z.read(member);p=W/'sources'/sub/member.filename
   if not p.is_file():raise ValueError('Missing extracted source '+str(p))
   digest=hashlib.sha256(data).hexdigest();current=hashlib.sha256(p.read_bytes()).hexdigest()
   if digest!=current:raise ValueError('Source differs from attachment: '+str(p))
   manifest['source_files'].append({'file':str(p.relative_to(W)),'archive':name,'member':member.filename,'bytes':len(data),'sha256':digest,'unchanged':True})
for name in ['PROMPT(4).md','README(3).md','SA05_PROMPT.zip']:
 p=W/'upload'/name;manifest['attachments'].append({'name':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
manifest['all_supplied_sources_unchanged']=True
(B/'SA05_source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
catalog=json.loads((B/'programs/outputs/source_catalog.json').read_text())
guide=['# SA05 — source coordinates and reproducibility','',
 'This archive contains the completed dossier and its audit trail. The supplied attachments are deliberately not copied into it. Paths beginning `sources/` refer to the safely extracted originals beside the `SA05/` directory. All source bytes match the original data archives; hashes and the comparison result are in `SA05_source_manifest.json`.','',
 '## Reading the coordinates','',
 'A line number is a1-based physical file line. It is different from scan number, manuscript foliation and reused typescript pagination. A `\\scanpage{N}` marker starts a physical scan section. A section ends just before the next marker, or at end of file. Repeated/reused material can have different scan labels in different witnesses.','',
 '| Short locator | Exact relative file |','|---|---|',
 '| Pro early | `sources/texts/pro/MPL_12_002-050_transcription.tex` |',
 '| Pro middle | `sources/texts/pro/MPL_12_051-098_transcription.tex` |',
 '| Pro late | `sources/texts/pro/MPL_12_099-149_transcription.tex` |',
 '| K11-01 through K11-04 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |',
 '| K12-01 through K12-09 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |',
 '| B12-01 and B12-02 | Same prefix plus `_transcription.tex` in `sources/texts/codex/` |','',
 'The final audit replaced inaccurate draft Codex offsets in the root records with explicit whole physical scan-section ranges, while retaining the more precise Pro spans. Claims and problems inherit these corrected item locators. `work/root/source_guide_aliases.json` contains the complete alias/section map; the before/after records are in `work/root/outputs/codex_locator_initial_*.json` and the latest audit TSVs. B12 sections never enter the K12 replacement lookup. For example, B12 scan066 and K12 scan072 remain two independently located witnesses of reused text, not one physical scan.','',
 'A missing K12 section is stated explicitly; it can still have a Pro or B12 witness. No source was altered to harmonize a sign, index, deleted word or page label. The earlier scope files and authoring programs remain audit provenance; the final canonical tables and the documented repair step control the delivered locators.','',
 '## Supplied transcription inventory','']
guide+=table([(r['file'].replace('sources/texts/',''),r['lines'],', '.join(s['scan'] for s in r['scans'])) for r in catalog if r['file'].startswith('sources/texts/') and r['file'].endswith('_transcription.tex')],['Source file','Physical lines','Literal scan markers'])
guide+=['','## Which tables control interpretation','',
 '`SA05_entries.tsv` is the380-row entry ledger. `SA05_items.json`, `SA05_claims.json` and `SA05_problems.json` contain canonical IDs. `SA05_aliases.json` records redirects and partial source partitions. Merged records retain source-specific formulations and documentary changes. Historical reference aliases do not collapse different editions or different works.','',
 '`SA05_links.tsv` has the required three kinds. Only its folder/published-work rows are counted as checked two-ended links. Prior-project associations are also exported to `SA05_project_leads.tsv`. Absent archive targets and the unverified SGA4 backward reference are in separate lead files.','',
 '`SA05_reference_ledger.json` preserves all bibliography witnesses, edition/version limits and additional reopened passages. `SA05_searches.tsv` maps each claim to actual performed searches and their checked extent; inherited family URLs are provenance, not a claim that every result supports every assertion. `CHECK_EVENTS.tsv` distinguishes source comparison, proof checks, independent deductions, executed computations and refutations.','',
 '## Restore and reproduce','',
 'Place the five original attachments in `upload/` beside this unzipped `SA05/` directory. Run `python SA05/programs/bootstrap.py` if `sources/` needs reconstructing; it safely extracts the archives. The separate uploaded `PROMPT(4).md` supplies the later45-minute checkpoint rule. The older packaged prompt is retained only as supplied input.','',
 'The existing authoring files contain the manually made judgments. `python SA05/work/root/run_all.py` regenerates the root scope, repairs its Codex locators and executes its exact checks. Other scope run/build programs and their recorded outputs are retained. The refinement-supplement builder has a deliberate duplicate-ID guard and should not be blindly rerun after central incorporation.','',
 'For the final canonical build, run `programs/consolidate.py`, `programs/consolidate_references.py`, `programs/build_directions.py`, then `programs/build_documents.py` from the `SA05/` path as shown by the build report, followed by `programs/validate_final.py`. These programs use the existing approved joins and authored judgments; they do not search or reinterpret the manuscript automatically. The final archive includes all authored programs and their saved outputs.','',
 'Fetched full published texts are not redistributed. Raw web-result bodies under the search caches are replaced inside the ZIP by source-access audit records containing URLs, retrieval IDs and hashes. The authored query ledgers, checked theorem statements, own proofs, conclusions and limits are preserved. This replacement is a packaging operation only and does not change the completed literature judgments.','']
(B/'SA05_source_guide.md').write_text('\n'.join(guide))
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'dossier_words':len(text.split()),'directions':len(dirs),'source_files_compared':len(manifest['source_files']),'all_sources_unchanged':True}
(B/'programs/outputs/build_documents.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
