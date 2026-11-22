"""Create CP27 workflows only. Explicit identifiers; never substitute bare digits."""
from pathlib import Path
import ast,datetime,hashlib,json,re
w=Path(__file__).resolve().parents[1]
c=w/'code'
required=['agents/reduction_descent/B_first_level_mixed_boundary.tex']
names=['prepare_checkpoint27.py','finalize_checkpoint27.py','archive_checkpoint27.py','verify_program_paths27.py','render_qa27.py']
for name in names:assert not (c/name).exists(),name
for rel in required:
    assert (w/rel).exists(),rel
    assert r'\status{Candidate' not in (w/rel).read_text(),rel
snap=w/'outputs/checkpoint27_workflow_setup';assert not snap.exists()
search=w/'notes/ROOT_SEARCH_LOG_27.md';assert not search.exists()

def once(text,old,new):
    assert text.count(old)==1,(old,text.count(old))
    return text.replace(old,new)

def identifiers(text):
    # Each matched token is replaced once. Hash algorithm names are untouched.
    substitutions={'checkpoint26':'checkpoint27','checkpoint_26':'checkpoint_27',
                   'Checkpoint26':'Checkpoint27','CP26':'CP27','qa26':'qa27',
                   'update_current26':'update_current27',"'checkpoint':26":"'checkpoint':27"}
    pattern=re.compile('|'.join(re.escape(k) for k in sorted(substitutions,key=len,reverse=True)))
    return pattern.sub(lambda m:substitutions[m.group()],text)

originals={name:(c/name.replace('27','26')).read_text() for name in names}
prepare=identifiers(originals['prepare_checkpoint27.py'])
a=prepare.index('required=');b=prepare.index('\nfor rel in required:',a)
prepare=prepare[:a]+'required='+repr(required)+prepare[b:]

finalize=identifiers(originals['finalize_checkpoint27.py'])
finalize=once(finalize,'RESEARCH_SA15_checkpoint_25.zip','RESEARCH_SA15_checkpoint_26.zip')
finalize=once(finalize,'new identifiers since checkpoint25','new identifiers since checkpoint26')
finalize=finalize.replace('progress_review_17.json','progress_review_18.json')
finalize=once(finalize,"assert review['review']==17","assert review['review']==18")
finalize=once(finalize,"{'review':17,","{'review':18,")
finalize=once(finalize,"2026-11-19T21:50:40+00:00","2026-11-19T22:50:40+00:00")
start=finalize.index('Checkpoint27 is archived only at or after')
end=finalize.index('No review or archive is represented as completed before its actual execution.',start)+len('No review or archive is represented as completed before its actual execution.')
finalize=finalize[:start]+('Checkpoint27 is archived only at or after23:05:40UTC. '
 'Actual review18 was recorded at {review_actual.isoformat()}, read directly from '
 'notes/progress_review_18.json; its recorded no-movement streak is '
 "{review['no_movement_streak']}. The next actual review19 is due23:50:40UTC "
 'and checkpoint28 is due23:50:40UTC. No review or archive is represented as '
 'completed before its actual execution.')+finalize[end:]
start=finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
end=finalize.index("assert (w/'RESEARCH_SA15_report.md')",start)
finalize=finalize[:start]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint27 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are explicitly enumerated in notes/checkpoint27_changes.md and in the retained '
            'checkpoint27 integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Actual review18 was recorded at '+review_actual.isoformat()+
            '; the next actual review19 and checkpoint28 are due23:50:40UTC. '
            'This snapshot does not replace an actual review.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+finalize[end:]

archive='''"""Archive CP27 after its due time, actual review18, and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-19T23:05:40+00:00')
review=json.loads((w/'notes/progress_review_18.json').read_text())
assert review['review']==18
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-19T22:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint27.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_27.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','27'),('verify_checkpoint_archive.py','27')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify=identifiers(originals['verify_program_paths27.py'])
render=identifiers(originals['render_qa27.py'])

original_consolidate=(c/'consolidate.py').read_text()
consolidated=once(original_consolidate,
 "'B_marked_quotient_sector.tex']:",
 "'B_marked_quotient_sector.tex',\n                    'B_first_level_mixed_boundary.tex']:")
consolidated=once(consolidated,r'\\path{notes/ROOT_SEARCH_LOG_26.md}',
 r'\\path{notes/ROOT_SEARCH_LOG_26.md}, and'+'\n'+r'\\path{notes/ROOT_SEARCH_LOG_27.md}')

generated=dict(zip(names,[prepare,finalize,archive,verify,render]))
for name,text in generated.items():
    tree=ast.parse(text,filename=name)
    for node in ast.walk(tree):
        if isinstance(node,ast.Attribute) and isinstance(node.value,ast.Name) and node.value.id=='hashlib':
            assert node.attr=='sha256',(name,node.attr)
    assert set(re.findall(r'sha\d+',text))<= {'sha256'},name
    assert 'pdf_sha267' not in text and 'pdf_sha266' not in text,name
ast.parse(consolidated,filename='consolidate.py')
assert 'RESEARCH_SA15_checkpoint_26.zip' in finalize
assert 'new identifiers since checkpoint26' in finalize
assert 'progress_review_18.json' in finalize and 'progress_review_18.json' in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-19T22:50:40+00:00' in finalize
assert '2026-11-19T23:05:40+00:00' in archive
assert 'update_current27.py' in prepare and 'update_current27.py' in finalize
assert 'asserted integral inverse formula' in render and '173' not in render
assert 'checkpoint28 is due23:50:40UTC' in finalize
assert 'progress_review_17.json' not in finalize+archive
assert '21:50:40' not in finalize+archive
assert '22:20:40' not in finalize+archive

snap.mkdir()
(snap/'consolidate.before.py').write_text(original_consolidate)
for name,text in originals.items():(snap/name.replace('27','26')).write_text(text)
for name,text in generated.items():(c/name).write_text(text)
(c/'consolidate.py').write_text(consolidated)
search.write_text('# Root source and search log: checkpoint27\n\n'
 'No new root source-read or search entry has yet been recorded in this dated log. '
 'Actual accesses must be added with their precise scope; this setup stub makes no access claim.\n')
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Workflow setup, AST and semantic hash/time/path checks only. No build, render, finalization, review or archive executed.',
 'generated_scripts':names,'required_canonical_inputs':required,
 'generated_sha256':{name:hashlib.sha256(text.encode()).hexdigest() for name,text in generated.items()},
 'consolidate_before_sha256':hashlib.sha256(original_consolidate.encode()).hexdigest(),
 'consolidate_after_sha256':hashlib.sha256(consolidated.encode()).hexdigest(),
 'previous_checkpoint_for_statement_ids':26,'actual_review_required':18,
 'review_due_utc':'2026-11-19T22:50:40+00:00','archive_not_before_utc':'2026-11-19T23:05:40+00:00',
 'next_review_due_utc':'2026-11-19T23:50:40+00:00','next_checkpoint_due_utc':'2026-11-19T23:50:40+00:00',
 'semantic_checks':['Only designated checkpoint identifiers replaced; no bare digit substitution.',
 'Every hashlib call is sha256 and all hash keys remain pdf_sha256.',
 'Finalizer requires actual review18 timestamp between due time and current time.',
 'Archive requires due time and the exact review18 timestamp recorded by final QA.',
 'Statement comparison uses immutable checkpoint26 ZIP.',
 'QA locates the old overflow paragraph dynamically from its actual PDF text.',
 'Only the promoted B72 canonical is newly required; no isolated A3 candidate is included.']}
(snap/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
