"""Create CP31 workflows from immutable CP30 scripts, with exact time gates."""
from pathlib import Path
import ast,datetime,hashlib,json,re
w=Path(__file__).resolve().parents[1];c=w/'code'
required=['agents/reduction_descent/B_first_wild_diagonal_projection.tex',
 'agents/reduction_descent/B_first_wild_cyclotomic_quotient.tex',
 'sections/A_theta_torsion_avoidance.tex',
 'agents/monodromy/principal_theta_Cartier_bridge.tex',
 'agents/obstructions_crystals/A4_Moore_singular_parameters.tex',
 'agents/monodromy/ppav_twisted_Cartier_Moore.tex']
optional=['agents/reduction_descent/B_p5_tame_full_first_layer.tex']
sources={'prepare_checkpoint31.py':'prepare_checkpoint30.py',
 'finalize_checkpoint31.py':'finalize_checkpoint30.py',
 'archive_checkpoint31.py':'archive_checkpoint30.py',
 'verify_program_paths31.py':'verify_program_paths30.py',
 'render_qa31.py':'render_qa30.py'}
for name in sources:assert not(c/name).exists(),name
for rel in required:
 assert(w/rel).exists(),rel
 assert '\\status{Candidate' not in(w/rel).read_text(),rel
snap=w/'outputs/checkpoint31_workflow_setup';assert not snap.exists()
def once(text,old,new):
 assert text.count(old)==1,(old,text.count(old))
 return text.replace(old,new)
def identifiers(text):
 subs={'checkpoint30':'checkpoint31','checkpoint_30':'checkpoint_31',
  'Checkpoint30':'Checkpoint31','CP30':'CP31','qa30':'qa31',
  'update_current30':'update_current31',"'checkpoint':30":"'checkpoint':31"}
 pattern=re.compile('|'.join(re.escape(k) for k in sorted(subs,key=len,reverse=True)))
 return pattern.sub(lambda m:subs[m.group()],text)
originals={new:(c/old).read_text() for new,old in sources.items()}
prepare=identifiers(originals['prepare_checkpoint31.py'])
a=prepare.index('required=');b=prepare.index('\nfor rel in required:',a)
prepare=prepare[:a]+'required='+repr(required)+'\nfor optional in '+repr(optional)+''':
    p=w/optional
    if p.exists() and '\\\\status{Candidate' not in p.read_text():required.append(optional)
'''+prepare[b:]
finalize=identifiers(originals['finalize_checkpoint31.py'])
finalize=once(finalize,'RESEARCH_SA15_checkpoint_29.zip','RESEARCH_SA15_checkpoint_30.zip')
finalize=once(finalize,'new identifiers since checkpoint29','new identifiers since checkpoint30')
finalize=finalize.replace('progress_review_20','progress_review_21').replace('review20','review21')
finalize=once(finalize,"assert review['review']==20","assert review['review']==21")
finalize=once(finalize,"'review':20","'review':21")
finalize=once(finalize,'2026-11-20T00:50:40+00:00','2026-11-20T01:50:40+00:00')
a=finalize.index('Checkpoint31 is archived only at or after')
last='No review or archive is represented as completed before its actual execution.'
b=finalize.index(last,a)+len(last)
finalize=finalize[:a]+(
 'Checkpoint31 is archived only at or after02:05:40UTC on20November2026. '
 'Completed actual review21 was recorded at {review_actual.isoformat()}, read directly '
 'from notes/progress_review_21.json; its recorded no-movement streak is '
 "{review['no_movement_streak']}. The next actual review22 is due02:50:40UTC "
 'and checkpoint32 is due02:50:40UTC on20November2026. '
 'Checkpoint31 requires the already completed review21 and does not report '
 'completion of the later review22. '+last)+finalize[b:]
a=finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b=finalize.index("assert (w/'RESEARCH_SA15_report.md')",a)
finalize=finalize[:a]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint31 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are enumerated in notes/checkpoint31_changes.md and the retained checkpoint31 '
            'integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Completed actual review21 was recorded at '+review_actual.isoformat()+
            '; the next actual review22 and checkpoint32 are due02:50:40UTC '
            'on20November2026. Checkpoint31 is due02:05:40UTC. This snapshot does not '
            'replace an actual review or report review22 early.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+finalize[b:]
archive='''"""Archive CP31 after its due time, actual review21 and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T02:05:40+00:00')
review=json.loads((w/'notes/progress_review_21.json').read_text())
assert review['review']==21
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-20T01:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint31.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_31.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','31'),('verify_checkpoint_archive.py','31')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify=identifiers(originals['verify_program_paths31.py'])
render=identifiers(originals['render_qa31.py'])
generated=dict(zip(sources,[prepare,finalize,archive,verify,render]))
for name,text in generated.items():
 tree=ast.parse(text,filename=name)
 for node in ast.walk(tree):
  if isinstance(node,ast.Attribute) and isinstance(node.value,ast.Name) and node.value.id=='hashlib':
   assert node.attr=='sha256',(name,node.attr)
 assert set(re.findall(r'sha\d+',text))<={'sha256'},name
 assert not re.search(r'pdf_sha(?!256)\d+',text),name
assert 'RESEARCH_SA15_checkpoint_30.zip' in finalize
assert 'new identifiers since checkpoint30' in finalize
assert 'progress_review_21.json' in finalize+archive
assert 'progress_review_22.json' not in finalize+archive
assert "assert review['review']==21" in finalize and "assert review['review']==21" in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-20T01:50:40+00:00' in finalize
assert archive.count('2026-11-20T02:05:40+00:00')==1
assert archive.count('2026-11-20T01:50:40+00:00')==1
assert 'update_current31.py' in prepare and 'update_current31.py' in finalize
assert 'asserted integral inverse formula' in render
assert 'checkpoint32 is due02:50:40UTC' in finalize
assert '01:20:40' not in finalize+archive
snap.mkdir()
for new,old in sources.items():
 (snap/old).write_text(originals[new])
 assert(snap/old).read_bytes()==(c/old).read_bytes(),old
for name,text in generated.items():(c/name).write_text(text)
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Workflow setup and exact AST/time/path/hash checks only. No build, finalization, review or archive executed. Previous executed scripts retained unchanged.',
 'generated_scripts':list(generated),'required_canonical_inputs':required,
 'optional_canonical_inputs':optional,
 'generated_sha256':{name:hashlib.sha256(text.encode()).hexdigest() for name,text in generated.items()},
 'previous_checkpoint_for_statement_ids':30,'actual_review_required':21,
 'required_review_due_utc':'2026-11-20T01:50:40+00:00',
 'archive_not_before_utc':'2026-11-20T02:05:40+00:00',
 'next_review_due_utc':'2026-11-20T02:50:40+00:00',
 'next_checkpoint_due_utc':'2026-11-20T02:50:40+00:00'}
(snap/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
