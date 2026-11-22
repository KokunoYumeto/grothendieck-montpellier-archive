"""Prepare CP32 workflows with actual review22 and exact archive time gates."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json,re
w=Path(__file__).resolve().parents[1];c=w/'code'
sources={
 'prepare_checkpoint32.py':'prepare_checkpoint31.py',
 'finalize_checkpoint32.py':'finalize_checkpoint31.py',
 'archive_checkpoint32.py':'archive_checkpoint31.py',
 'verify_program_paths32.py':'verify_program_paths31.py',
 'render_qa32.py':'render_qa31.py'}
for name in sources:assert not(c/name).exists(),name
snap=w/'outputs/checkpoint32_workflow_setup';assert not snap.exists()
def identifiers(text):
 subs={'checkpoint31':'checkpoint32','checkpoint_31':'checkpoint_32',
  'Checkpoint31':'Checkpoint32','CP31':'CP32','qa31':'qa32',
  'update_current31':'update_current32',"'checkpoint':31":"'checkpoint':32"}
 pat=re.compile('|'.join(re.escape(k) for k in sorted(subs,key=len,reverse=True)))
 return pat.sub(lambda m:subs[m.group()],text)
originals={new:(c/old).read_text() for new,old in sources.items()}
prepare=identifiers(originals['prepare_checkpoint32.py'])
start=prepare.index('required=');end=prepare.index('\nfor rel in required:',start)
required=['agents/reduction_descent/B_p5_cyclotomic_break_three_example.tex']
prepare=prepare[:start]+'required='+repr(required)+'\n'+prepare[end:]
finalize=identifiers(originals['finalize_checkpoint32.py'])
finalize=finalize.replace('RESEARCH_SA15_checkpoint_30.zip','RESEARCH_SA15_checkpoint_31.zip')
finalize=finalize.replace('new identifiers since checkpoint30','new identifiers since checkpoint31')
finalize=finalize.replace('progress_review_21','progress_review_22').replace('review21','review22')
finalize=finalize.replace("assert review['review']==21","assert review['review']==22")
finalize=finalize.replace("'review':21","'review':22")
finalize=finalize.replace('2026-11-20T01:50:40+00:00','2026-11-20T02:50:40+00:00')
a=finalize.index('Checkpoint32 is archived only at or after')
last='No review or archive is represented as completed before its actual execution.'
b=finalize.index(last,a)+len(last)
finalize=finalize[:a]+(
 'Checkpoint32 is archived only at or after02:50:40UTC on20November2026. '
 'Completed actual review22 was recorded at {review_actual.isoformat()}, read directly '
 'from notes/progress_review_22.json; its recorded no-movement streak is '
 "{review['no_movement_streak']}. The next actual review23 is due03:50:40UTC "
 'and checkpoint33 is due03:35:40UTC on20November2026. '
 'Checkpoint32 requires the actual review22 and cannot be finalized before that review. '+last)+finalize[b:]
a=finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b=finalize.index("assert (w/'RESEARCH_SA15_report.md')",a)
finalize=finalize[:a]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint32 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. Audited additions '
            'and retained unsuccessful approaches are recorded in notes/checkpoint32_changes.md. '
            'Candidate work is not promoted by this snapshot. Completed actual review22 '
            'was recorded at '+review_actual.isoformat()+
            '; the next actual review23 is due03:50:40UTC and checkpoint33 is due03:35:40UTC '
            'on20November2026. Checkpoint32 is due02:50:40UTC.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+finalize[b:]
archive='''"""Archive CP32 only after its due time, actual review22 and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T02:50:40+00:00')
review=json.loads((w/'notes/progress_review_22.json').read_text())
assert review['review']==22
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T02:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint32.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_32.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','32'),('verify_checkpoint_archive.py','32')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify=identifiers(originals['verify_program_paths32.py'])
render=identifiers(originals['render_qa32.py'])
generated=dict(zip(sources,[prepare,finalize,archive,verify,render]))
for name,text in generated.items():
 ast.parse(text,filename=name)
 assert set(re.findall(r'sha\d+',text))<={'sha256'},name
assert 'RESEARCH_SA15_checkpoint_31.zip' in finalize
assert 'progress_review_22.json' in finalize+archive
assert 'progress_review_21.json' not in finalize+archive
assert "assert review['review']==22" in finalize and "assert review['review']==22" in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-20T02:50:40+00:00' in finalize+archive
assert 'update_current32.py' in prepare+finalize
assert '02:05:40' not in finalize+archive
snap.mkdir()
for new,old in sources.items():
 (snap/old).write_text(originals[new])
 assert(snap/old).read_bytes()==(c/old).read_bytes()
for name,text in generated.items():(c/name).write_text(text)
consolidate=c/'consolidate.py';before=consolidate.read_text()
needle="'ROOT_SEARCH_LOG_31.md'"
assert before.count(needle)==1 and 'ROOT_SEARCH_LOG_32.md' not in before
after=before.replace(needle,needle+",'ROOT_SEARCH_LOG_32.md'")
ast.parse(after)
(snap/'consolidate.before.py').write_text(before)
(snap/'consolidate.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
consolidate.write_text(after)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
log=w/'notes/ROOT_SEARCH_LOG_32.md';assert not log.exists()
log.write_text('''# Root search log, checkpoint32\n\nActual research continuation after the successful checkpoint31 save. General A.3, A.4, higher-dimensional B.3 and general B.4 remain open. No priority claim is made.\n\n## Hasse-divisor algebra\n\nThe exact universal Moore remainder modulo the Fermat cubic was reconstructed, and its full-coordinate-torus coefficient conditions were retained. This is exploratory exact algebra, not a Cartier or monodromy theorem. The prior support classification does not itself imply the same classification for divisibility by a fixed cubic.\n\n## Literature searches in this interval\n\nBoth web search systems were used for Heisenberg-invariant cubics in P8, the base locus of the five invariant cubics, 81 linear spaces, Coble cubics in characteristic two, and Fermat divisibility. Search results led to Beauville's Coble paper and the Benedetti--Manivel--Tanturri Coble geometry paper, but no full new proof was read or imported in this interval. The previously read Coble sources retain their earlier explicitly limited characteristic scope; no characteristic-two extension is inferred from these search results.\n\nA further search for Pfaffian Cremona maps, height-two submaximal Pfaffian ideals, and analytic spread returned Russo--Simis Example2.5 and later generic-height Rees-ring work. The result assumes height3; it does not establish the missing height condition. No new theorem is cited as solving that gate.\n\n## Explicit cyclotomic base\n\nThe root read the complete B89 proof and checker and reread the complete internal B60 lower-break and B88 tame-scaling proofs. The unchanged independent check passed. This realizes the necessary base/cyclotomic data only; it does not realize an ambiguous height-two pair.\n''')
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('\n## Checkpoint31 preservation and next gates\n\nCheckpoint31 was archived and manifest-verified after02:05:40UTC, saved successfully and delivered as its own immutable ZIP. It has34,581,553bytes,2,829members,2,828manifest hashes, and SHA25609d8ce9622002684825e86d1eb910e9a9b2675f6057afc74a4367c2d22434c5d. Its700-page paper,876numbered statements and2,553check events remain available unchanged in that checkpoint. The current report table now escapes literal vertical bars in mathematical linear-system notation so that Markdown columns remain intact. This formatting correction changes no mathematical assertion.\n\nNext actual review22 and checkpoint32 are both due02:50:40UTC on20November2026. Workflow creation is not an actual review, PDF build, finalization or checkpoint. The next review23 is due03:50:40UTC and checkpoint33 is due03:35:40UTC.\n')
record={'status':'PASS','actual_utc':now,'generated_scripts':list(generated),
 'scope':'Setup and syntax/time/path checks only; no build, actual review, finalization or archive executed.',
 'generated_sha256':{name:hashlib.sha256(text.encode()).hexdigest() for name,text in generated.items()},
 'required_canonical_inputs':required,'previous_checkpoint_for_statement_ids':31,
 'actual_review_required':22,'archive_not_before_utc':'2026-11-20T02:50:40+00:00',
 'required_review_due_utc':'2026-11-20T02:50:40+00:00',
 'next_review_due_utc':'2026-11-20T03:50:40+00:00',
 'next_checkpoint_due_utc':'2026-11-20T03:35:40+00:00'}
(snap/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
