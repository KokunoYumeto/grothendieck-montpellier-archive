"""Create CP30 workflows from preserved CP29 sources, with explicit time gates."""
from pathlib import Path
import ast,datetime,hashlib,json,re
w=Path(__file__).resolve().parents[1];c=w/'code'
required=['agents/reduction_descent/B_first_wild_reducible_terminal.tex',
          'agents/reduction_descent/B_first_wild_swapped_quotients.tex',
          'agents/obstructions_crystals/A4_ss_product_dual_Cartier.tex']
sources={'prepare_checkpoint30.py':'prepare_checkpoint29.py',
 'finalize_checkpoint30.py':'finalize_checkpoint29.py',
 'archive_checkpoint30.py':'archive_checkpoint29.py',
 'verify_program_paths30.py':'verify_program_paths29.py',
 'render_qa30.py':'render_qa29.py'}
for name in sources:assert not(c/name).exists(),name
for rel in required:
 assert(w/rel).exists(),rel
 assert '\\status{Candidate' not in(w/rel).read_text(),rel
snap=w/'outputs/checkpoint30_workflow_setup';assert not snap.exists()
def once(text,old,new):
 assert text.count(old)==1,(old,text.count(old))
 return text.replace(old,new)
def identifiers(text):
 substitutions={'checkpoint29':'checkpoint30','checkpoint_29':'checkpoint_30',
  'Checkpoint29':'Checkpoint30','CP29':'CP30','qa29':'qa30',
  'update_current29':'update_current30',"'checkpoint':29":"'checkpoint':30"}
 pattern=re.compile('|'.join(re.escape(k) for k in sorted(substitutions,key=len,reverse=True)))
 return pattern.sub(lambda m:substitutions[m.group()],text)
originals={new:(c/old).read_text() for new,old in sources.items()}
prepare=identifiers(originals['prepare_checkpoint30.py'])
a=prepare.index('required=');b=prepare.index('\nfor rel in required:',a)
prepare=prepare[:a]+'required='+repr(required)+'''
for optional in ['agents/reduction_descent/B_tame_residual_one_prime_recovery.tex']:
    p=w/optional
    if p.exists() and '\\\\status{Candidate' not in p.read_text():required.append(optional)
'''.replace('\\\\status','\\\\status')+prepare[b:]
finalize=identifiers(originals['finalize_checkpoint30.py'])
finalize=once(finalize,'RESEARCH_SA15_checkpoint_28.zip','RESEARCH_SA15_checkpoint_29.zip')
finalize=once(finalize,'new identifiers since checkpoint28','new identifiers since checkpoint29')
finalize=finalize.replace('progress_review_19','progress_review_20').replace('review19','review20')
finalize=once(finalize,"assert review['review']==19","assert review['review']==20")
finalize=once(finalize,"'review':19","'review':20")
finalize=once(finalize,'2026-11-19T23:50:40+00:00','2026-11-20T00:50:40+00:00')
a=finalize.index('Checkpoint30 is archived only at or after')
last='No review or archive is represented as completed before its actual execution.'
b=finalize.index(last,a)+len(last)
finalize=finalize[:a]+(
 'Checkpoint30 is archived only at or after01:20:40UTC on20November2026. '
 'Completed actual review20 was recorded at {review_actual.isoformat()}, read directly '
 'from notes/progress_review_20.json; its recorded no-movement streak is '
 "{review['no_movement_streak']}. The next actual review21 is due01:50:40UTC "
 'and checkpoint31 is due02:05:40UTC on20November2026. '
 'Checkpoint30 requires the already completed review20 and does not report '
 'completion of the later review21. '+last)+finalize[b:]
a=finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b=finalize.index("assert (w/'RESEARCH_SA15_report.md')",a)
finalize=finalize[:a]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint30 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are enumerated in notes/checkpoint30_changes.md and the retained checkpoint30 '
            'integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Completed actual review20 was recorded at '+review_actual.isoformat()+
            '; the next actual review21 is due01:50:40UTC and checkpoint31 is due02:05:40UTC '
            'on20November2026. Checkpoint30 is due01:20:40UTC. This snapshot does not '
            'replace an actual review or report review21 early.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+finalize[b:]
archive='''"""Archive CP30 after its due time, completed review20 and actual final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T01:20:40+00:00')
review=json.loads((w/'notes/progress_review_20.json').read_text())
assert review['review']==20
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T00:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint30.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_30.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','30'),('verify_checkpoint_archive.py','30')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify=identifiers(originals['verify_program_paths30.py'])
render=identifiers(originals['render_qa30.py'])
generated=dict(zip(sources,[prepare,finalize,archive,verify,render]))
for name,text in generated.items():
 tree=ast.parse(text,filename=name)
 for node in ast.walk(tree):
  if isinstance(node,ast.Attribute) and isinstance(node.value,ast.Name) and node.value.id=='hashlib':
   assert node.attr=='sha256',(name,node.attr)
 assert set(re.findall(r'sha\d+',text))<={'sha256'},name
 assert not re.search(r'pdf_sha(?!256)\d+',text),name
assert 'RESEARCH_SA15_checkpoint_29.zip' in finalize
assert 'new identifiers since checkpoint29' in finalize
assert 'progress_review_20.json' in finalize+archive
assert 'progress_review_21.json' not in finalize+archive
assert "assert review['review']==20" in finalize and "assert review['review']==20" in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-20T00:50:40+00:00' in finalize
assert archive.count('2026-11-20T01:20:40+00:00')==1
assert archive.count('2026-11-20T00:50:40+00:00')==1
assert 'update_current30.py' in prepare and 'update_current30.py' in finalize
assert 'asserted integral inverse formula' in render
assert 'checkpoint31 is due02:05:40UTC' in finalize
assert '00:35:40' not in finalize+archive
snap.mkdir()
for new,old in sources.items():
 (snap/old).write_text(originals[new])
 assert(snap/old).read_bytes()==(c/old).read_bytes(),old
for name,text in generated.items():(c/name).write_text(text)
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Workflow setup, AST and exact time/path/hash checks only. No build, render, finalization or archive executed. Prior scripts preserved; consolidate.py unchanged.',
 'generated_scripts':list(generated),'required_canonical_inputs':required,
 'optional_canonical_inputs':['agents/reduction_descent/B_tame_residual_one_prime_recovery.tex'],
 'generated_sha256':{name:hashlib.sha256(text.encode()).hexdigest() for name,text in generated.items()},
 'previous_checkpoint_for_statement_ids':29,'actual_review_required':20,
 'required_review_due_utc':'2026-11-20T00:50:40+00:00',
 'archive_not_before_utc':'2026-11-20T01:20:40+00:00',
 'next_review_due_utc':'2026-11-20T01:50:40+00:00',
 'next_checkpoint_due_utc':'2026-11-20T02:05:40+00:00'}
(snap/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
