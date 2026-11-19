"""Serialize the completed, manually reasoned registers into review aids.

This script does not assign a verdict, mathematical status, fate, or direction.
It only indexes the assessments already authored in records_*.py.
"""
import collections, csv, datetime, json, pathlib, re

P=pathlib.Path(__file__).resolve().parent
ROOT=P.parents[2]
claims=json.loads((P/'claims.json').read_text())
items=json.loads((P/'items.json').read_text())
problems=json.loads((P/'problems.json').read_text())
searches=[json.loads(s) for s in (P/'search_log.jsonl').read_text().splitlines()]
def table(name):
    with (P/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
events=table('check_events.tsv')
readings=table('readings.tsv')
links=table('links.tsv')
bib=(P/'references.bib').read_text()
refkeys=re.findall(r'@\w+\{([^,]+),',bib)
calc=json.loads((P/'computations/check_groupes.output.json').read_text())
claimmap={c['id']:c for c in claims}

# Quotations are checked against the selected source lines. Comments describing
# the transcription layout are not part of the author's quoted words.
qa=json.loads((P/'quotation_audit.json').read_text())
for q in qa:
    lines=(ROOT/q['source_file']).read_text().splitlines()
    chosen='\n'.join('\n'.join(lines[a-1:b]) for a,b in q['selected_lines'])
    assert all(x in chosen for x in q['literal_fragments']), q['id']
for c in claims:
    assert 'Paraphrase:' not in c['his_statement'],c['id']
    assert '%' not in c['his_statement'],c['id']
    assert all(r in refkeys for r in c['refs']),(c['id'],c['refs'])
    assert any(c['id'] in s['claims'] for s in searches),c['id']
    assert any(e['statement_id']==c['id'] for e in events),c['id']
for p in problems:assert all(r in refkeys for r in p['refs']),(p['id'],p['refs'])

search_map={c['id']:[dict(search_record=i+1,query=s['query'],opened=s['opened'],limits=s.get('limits','')) for i,s in enumerate(searches) if c['id'] in s['claims']] for c in claims}
(P/'claim_search_map.json').write_text(json.dumps(search_map,ensure_ascii=False,indent=2)+'\n')

refinements=[]
for e in events:
    match=re.search(r'RF-SA23-groupes-\d+',e['type'])
    if match:
        c=claimmap[e['statement_id']]
        refinements.append(dict(id=match.group(),source_claim=c['id'],record_origin='present-run reconstruction',statement=c['statement'],proof_or_counterexample=c['computation']['proof_or_check'],refs=c['refs']))
refinements=list({x['id']:x for x in refinements}.values())
(P/'refinements.json').write_text(json.dumps(refinements,ensure_ascii=False,indent=2)+'\n')

proof=['# Indexed verification certificates — cotes 161-1 and 161-2','',
 'These are the arguments, counterexamples, and exact-scope audits performed in this run, dated 19 November 2026. They are present reconstructions; they do not amend the transcription. A certificate for a question may establish a conditional result, refute an overbroad formulation, or identify the unfilled hypothesis. It does not assert that every historical question is solved.','',
 'The extended arguments for the delicate cases are in [extended_proofs.md](extended_proofs.md). Executed finite and symbolic checks are in [check_groupes.py](check_groupes.py), with their actual [output](check_groupes.output.json). Nineteen program sections cover twenty-three claim identifiers. Finite checks certify the named examples and identities only.','',
 'Bibliographic keys refer to `../references.bib`; exact opened passages and quantifier comparisons are in `../search_log.jsonl` and `../claim_search_map.json`. A quotation below is a literal excerpt of the supplied transcription. Its separate English paraphrase, full source locator, page status, and competing readings remain in `../claims.json`.','']
for c in claims:
    proof+=['## '+c['id'],'',
        '**Source:** '+ '; '.join(c['lines'])+'.','',
        '**Literal excerpt:**','', '```tex',c['his_statement'],'```','',
        '**Precise statement or question:** '+c['statement'],'',
        '**Check and its limit:** '+c['computation']['proof_or_check'],'',
        '**Literature match:** '+c['fate'],'',
        '**References:** '+', '.join(c['refs'])+'.','']
    if c['computation'].get('checks'):
        proof+=['**Executed checks:** '+ '; '.join(c['computation']['checks'])+'. See the program and output linked above.','']
    proof+=['**Recorded event types:** '+ '; '.join(dict.fromkeys(e['type'] for e in events if e['statement_id']==c['id']))+'.','']
(P/'computations/proof_certificates.md').write_text('\n'.join(proof)+'\n')

# Each source block was actually read; interval coverage merely records that
# completed reading and does not turn a read into a mathematical check.
files=[('K161-1-01',727,24),('K161-2-01',534,29),('K161-2-02',808,21),('K161-2-03',860,22),('K161-2-04',538,26),('K161-2-05',340,25),('K161-2-06',473,25),('K161-2-07',726,47)]
readlog=[json.loads(s) for s in (P/'read_logs/reads.jsonl').read_text().splitlines()]
read_coverage=[]
for stem,n,nn in files:
    for folder,suffix,total in [('texts','transcription.tex',n),('notes','notes.md',nn)]:
        filename=f'sources/{folder}/codex/{stem}_{suffix}'
        entries=[r for r in readlog if r['path']==filename]
        covered=set()
        for r in entries:covered.update(range(r['first_line'],r['last_line']+1))
        missing=sorted(set(range(1,total+1))-covered)
        assert not missing,(filename,missing)
        read_coverage.append(dict(file=filename,physical_lines=total,read_log_records=len(entries),missing_lines=missing))
(P/'read_coverage.json').write_text(json.dumps(read_coverage,ensure_ascii=False,indent=2)+'\n')

counts=dict(indexed_entries=0,additional_source_items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),references=len(refkeys),search_events=len(searches),searched_claims=len(search_map),check_events=len(events),claim_classes=dict(collections.Counter(c['class'] for c in claims)),claim_statuses=dict(collections.Counter(c['status_category'] for c in claims)),transcription_files=8,transcription_physical_lines=5006,companion_note_files=8,companion_note_physical_lines=219,executed_program_sections=len(calc),claims_with_executed_program=len({cid for x in calc for cid in x['claims']}),refined_statement_records=len(refinements))
counts['editorial_tasks']=len(json.loads((P/'editorial_tasks.json').read_text()))
if (P/'authorship_audit.json').exists():counts['class_A_authorship_audited']=json.loads((P/'authorship_audit.json').read_text())['retained_A']
if (P/'directions.json').exists():counts['directions']=len(json.loads((P/'directions.json').read_text()))
(P/'counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')

coverage=['# Coverage and completion — Groupes part','',
 '**Scope:** all supplied transcriptions and Codex companion notes for cotes 161-1 and 161-2. The archive catalogue lists 19 leaves for 161-1 [173] and 111 leaves for 161-2; neither is dated in the supplied topic inventory. The actual assignment contains eight transcription files, not seven. There are no indexed Pro entries in this part, so `entries.tsv` deliberately has its header and no verdict rows. The 27 additional archival subject items have empty `sources` arrays.','',
 '## Full source reading','',
 '| File stem | Transcription physical lines | Companion-note physical lines | Completion |','|---|---:|---:|---|']
for stem,n,nn in files:coverage.append(f'| {stem} | {n} | {nn} | Entire text and note read |')
coverage+=['','Total: **5,006 transcription lines and 219 companion-note lines**. `read_logs/reads.jsonl` records source hashes and complete intervals, and `read_coverage.json` verifies their union. The eight `analysis_*.md` ledgers preserve the manual mathematical assessments made during reading. The end of file 06 was read again in short blocks after a combined tool output was truncated. Quotations were then checked against the actual source lines, with the choices recorded in `quotation_audit.json`. No scan, no `second_pass` file, and no unprovided leaf was used.','',
 '## Completed stages','',
 '1. **Source items:** 27 additional subject items, SA23-901–927; no new Stage 1 indexed verdicts. Each has a literal excerpt and source coordinates. These source items supplement the already completed indexed core. Root integration may merge genuinely repeated subject occurrences with other owners while preserving this owner witness.','',
 f'2. **Claims:** {len(claims)} claims, C-SA23-groupes-001–115, each with a manually assigned page status, precise modern statement, literal source excerpt, reconstruction boundary, searched fate, exact references, confidence, and a recorded check event. The {len(searches)} search records map to every claim. `claim_search_map.json` makes that mapping explicit. Every computation is either an executed symbolic/finite check or a written general proof or scope audit; the index is `computations/proof_certificates.md`.','',
 f'3. **Questions:** {len(problems)} authorial problem records, including actual live questions, canceled doubts, explicit deferred steps, and unfinished programmes. The final origin audit moved eleven bare assertions or correction histories out of Stage3 and narrowed seven mixed records to their real author cues. Thirteen editorial tasks retain those checks and two separated portions without labeling them author questions. Every retained occurrence preserves its drafting status. Individual development judgments distinguish settled commentary, bounded residual mathematics, and scan-first identification. `flag_coverage.md` lists every problem and all recorded source occurrences; `problem_origin_audit.json` and `problem_editorial_redirects.json` make the distinction inspectable.','',
 '4. **Reading alarms:** 59 records. Mathematical evidence raises an alarm; no uncertainty or cancellation was settled by looking at ink. Literal quotation fields retain `deleted`, `inserted`, and `unsure` markup where present.','',
 '5. **Links:** 10 verified links: seven archival-folder links and three exact published-work links. Both archival endpoints were read. The links to the self-braiding, graded-orientation, and Barsotti–Tate passages keep distinct questions distinct. The companion Codex notes provide no prior-project context packet, so no link to La Longue Marche, Les Dérivateurs, S6, or a named earlier research run is invented. `project_links.tsv` is empty apart from its schema.','',
 '6. **Directions:** the ranked, bounded tasks in `directions.md` and `directions.json` cite actual item, claim, and problem IDs, and give numerical interest and one-run progress scores, known results, residual issues, and the first concrete step. No direction was developed as a new research project here.','',
 '## Counts and interpretation','',
 '| Claim class | Count |','|---|---:|']
for k,v in sorted(counts['claim_classes'].items()):coverage.append(f'| {k} | {v} |')
coverage+=['','Class C includes a developed restricted theorem whose hypotheses do not establish the unrestricted source wording, a refuted wording with its precise repair, and a remaining formulation gap. It does not mean that every such record is a currently open problem. The two F records are the unidentified comparison endpoint (017) and detached formulas (111). Searches were completed for both; absence of a theorem matching undefined notation is recorded as an identification limit, not as evidence of novelty. No undated sheet is assigned priority from its catalogue position.','',
 '| Page-status category | Count |','|---|---:|']
for k,v in counts['claim_statuses'].items():coverage.append(f'| {k} | {v} |')
coverage+=['',f"There are {len(events)} check-event rows, {len(refkeys)} verified bibliography records, {len(searches)} search records, and {len(calc)} executed program sections covering {counts['claims_with_executed_program']} claims. Reference verification means the identified URL or DOI and stated passage were opened to the degree recorded; a metadata-only item is not used as a proof. The Bird thesis download failures, blocked zbMATH records, and broad but unmatched searches remain visible in the search log. Opened external PDFs and full texts are stored under `external/` as working evidence and are excluded from the final ZIP by root integration.",'',
 '## Genuine limits retained','',
 'The categories and functor in the last filtered-F-crystal comparison are not specified well enough to identify an equivalence. The detached cohomology/ring-topology formulas do not determine a theorem. The mixed-doctrine construction leaves its successor operation and several size/preservation hypotheses open. The internal connected-component assignment, formal smoothness/étaleness quantifiers, and final stack of topoi require a chosen precise formulation. These are the mathematical and textual outcomes of completed reading and searches; they are not unperformed source work.','',
 'Root owns final integration, cross-owner duplicate decisions, the combined dossier, checkpoints, and the single final ZIP. This part makes no Library mutation.']
coverage+=['','## Publication authorship audit','',
 'All fourteen class-A records have an exact authorship audit in `authorship_audit.json`. Their SGA 4 counterpart is in Exposé IV, Topos, whose original printed p.299 explicitly names A. Grothendieck and J. L. Verdier as joint authors. This is not an inference from the volume editors. The separate credits to Giraud and Artin on p.300 and to J.-E. Roos in Exercise7.6(d), p.415, remain explicit; class A does not assert sole discovery or manuscript priority. No mathematical statement or class count changed in this bounded audit.']
(P/'coverage.md').write_text('\n'.join(coverage)+'\n')

flags=['# Authorial question and correction coverage','',
 'This is an index of the manually assessed problem records, not a question-mark search. Withdrawn, answered, corrected, and still-open occurrences are retained. The strongest supported and modern plausible formulations, literature, and individual worth judgments are in `problems.json`.','',
 '| Problem | Title | Source occurrences and drafting status |','|---|---|---|']
for p in problems:
    loc=[]
    for o in p['occurrences']:
        loc.append(f"{o.get('file','')}:{o.get('lines','')}; scans {o.get('scans',o.get('scan',''))}; {o.get('drafting_status','recorded in source')}")
    flags.append('| '+p['id']+' | '+p['title'].replace('|','\\|')+' | '+'<br>'.join(loc).replace('|','\\|')+' |')
(P/'flag_coverage.md').write_text('\n'.join(flags)+'\n')
with (P/'project_links.tsv').open('w',newline='') as f:csv.writer(f,delimiter='\t').writerow(['kind','from','to','what','evidence','note_ids'])

now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (P/'progress.log').open('a') as f:f.write(now+' | Saved full source/claim/problem/quotation audits, indexed proof certificates, literal quotations, reference/search maps, flag coverage, and final stage counts.\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
