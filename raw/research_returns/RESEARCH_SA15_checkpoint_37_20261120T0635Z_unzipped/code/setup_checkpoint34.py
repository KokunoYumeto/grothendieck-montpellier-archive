"""Prepare CP34 and convergence safeguards; no build, review or archive is executed."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json,re
w=Path(__file__).resolve().parents[1];c=w/'code'
mapping={f'{stem}34.py':f'{stem}33.py' for stem in ['prepare_checkpoint','finalize_checkpoint','verify_program_paths','render_qa']}
names=list(mapping)+['archive_checkpoint34.py','update_current34.py']
assert all(not(c/n).exists() for n in names)
snap=w/'outputs/checkpoint34_workflow_setup';assert not snap.exists()
def ids(text):
 changes={'checkpoint33':'checkpoint34','checkpoint_33':'checkpoint_34','Checkpoint33':'Checkpoint34','CP33':'CP34','qa33':'qa34','update_current33':'update_current34',"'checkpoint':33":"'checkpoint':34"}
 pattern=re.compile('|'.join(re.escape(k) for k in sorted(changes,key=len,reverse=True)))
 return pattern.sub(lambda m:changes[m.group()],text)
originals={new:(c/old).read_text() for new,old in mapping.items()}
generated={new:ids(text) for new,text in originals.items()}
finalize=generated['finalize_checkpoint34.py']
finalize=finalize.replace('RESEARCH_SA15_checkpoint_32.zip','RESEARCH_SA15_checkpoint_33.zip').replace('since checkpoint32','since checkpoint33')
finalize=finalize.replace('progress_review_22','progress_review_23').replace("review['review']==22","review['review']==23").replace("'review':22","'review':23")
finalize=finalize.replace('2026-11-20T02:50:40','2026-11-20T03:50:40')
a=finalize.index('Checkpoint34 is archived only at or after');ending='No review or archive is represented as completed before its actual execution.'
b=finalize.index(ending,a)+len(ending)
finalize=finalize[:a]+("Checkpoint34 is archived only at or after04:20:40UTC on20November2026. Completed actual review23 was recorded at {review_actual.isoformat()}, read directly from notes/progress_review_23.json; its no-movement streak is {review['no_movement_streak']}. The next actual review24 is due04:50:40UTC and checkpoint35 is due05:05:40UTC. This checkpoint precedes review24 and does not claim that future review has occurred. "+ending)+finalize[b:]
a=finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:");b=finalize.index("assert (w/'RESEARCH_SA15_report.md')",a)
finalize=finalize[:a]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint34 current-gate snapshot\\n\\n'
            'This is a snapshot, not an hourly review. Audited additions and retained '
            'unsuccessful approaches are in notes/checkpoint34_changes.md. Candidate '
            'work is not promoted by this snapshot. Completed actual review23 was '
            'recorded at '+review_actual.isoformat()+
            '; review24 is due04:50:40UTC and checkpoint35 is due05:05:40UTC '
            'on20November2026. Checkpoint34 is due04:20:40UTC.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+finalize[b:]
generated['finalize_checkpoint34.py']=finalize
render=generated['render_qa34.py']
needle='matched=[]';assert needle in render
render=render.replace(needle,"first_body_page=next((p for level,title,p in toc if level==1),1)\npages.update(range(1,first_body_page+1))\n"+needle)
generated['render_qa34.py']=render
archive=ids((c/'archive_checkpoint33.py').read_text())
archive=archive.replace('after03:35:40','after04:20:40').replace('T03:35:40','T04:20:40').replace('progress_review_22','progress_review_23').replace("review['review']==22","review['review']==23").replace('T02:50:40','T03:50:40').replace('review22','review23').replace("('checkpoint.py','33')","('checkpoint.py','34')").replace("('verify_checkpoint_archive.py','33')","('verify_checkpoint_archive.py','34')")
generated['archive_checkpoint34.py']=archive
generated['update_current34.py']='''"""Refresh CP34 from explicitly promoted canonical inputs only."""
from pathlib import Path
import subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current33.py')],cwd=w,check=True)
p=w/'RESEARCH_SA15_report.md';text=p.read_text()
marker='\\n## Checkpoint 34 work: exceptional Lang modules and actual wild fields\\n'
if marker in text:text=text.split(marker)[0]
p.write_text(text+marker+'\\n'+(w/'notes/checkpoint34_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\\n\\n| Item |')
print('CP34 initial wrapper refreshed; unpromoted work does not change any gate.')
'''
consolidate=c/'consolidate.py';before_con=consolidate.read_text();needle=r'\\path{notes/ROOT_SEARCH_LOG_33.md}'
assert before_con.count(needle)==1 and 'ROOT_SEARCH_LOG_34.md' not in before_con
after_con=before_con.replace(needle,needle+'\n'+r'\\path{notes/ROOT_SEARCH_LOG_34.md}')
builder=c/'build_paper.py';before_build=builder.read_text()
needle="run(command);run(command)\n(out/'build_console.txt')";assert needle in before_build
after_build=before_build.replace(needle,"""run(command);run(command)
extra_convergence_passes=0
while 'Label(s) may have changed' in (root/'RESEARCH_SA15_paper.log').read_text(errors='replace'):
    if extra_convergence_passes>=3:
        (out/'build_console.txt').write_text('\\n'.join(log))
        (out/'build_failure.json').write_text(json.dumps({'seconds':round(time.monotonic()-start,3),'reason':'cross-reference convergence did not stabilize','extra_convergence_passes':extra_convergence_passes},indent=2)+'\\n')
        raise RuntimeError('Cross-reference convergence did not stabilize after three extra passes')
    run(command)
    extra_convergence_passes+=1
(out/'build_console.txt')""")
after_build=after_build.replace("'undefined_citations':'There were undefined citations' in final}","'undefined_citations':'There were undefined citations' in final,\n         'extra_convergence_passes':extra_convergence_passes,'latex_passes':3+extra_convergence_passes,\n         'rerun_warning':'Label(s) may have changed' in final}")
paper=w/'RESEARCH_SA15_paper.tex';before_paper=paper.read_text()
needle='\\setcounter{tocdepth}{2}\n';assert before_paper.count(needle)==1 and '\\renewcommand*\\l@subsection' not in before_paper
after_paper=before_paper.replace(needle,needle+'\\makeatletter\n\\renewcommand*\\l@subsection{\\@dottedtocline{2}{1.5em}{3.5em}}\n\\makeatother\n')
for n,t in generated.items():ast.parse(t,filename=n)
ast.parse(after_con);ast.parse(after_build)
assert 'progress_review_23.json' in finalize+archive and 'progress_review_24.json' not in finalize+archive
assert 'RESEARCH_SA15_checkpoint_33.zip' in finalize and "('checkpoint.py','34')" in archive
assert 'T04:20:40' in archive and 'checkpoint35 is due05:05:40' in finalize
for rel in ['checkpoint34_changes.md','ROOT_SEARCH_LOG_34.md','checkpoint34_promoted_inputs.json']:
 assert not(w/'notes'/rel).exists()
snap.mkdir()
for new,old in mapping.items():(snap/old).write_text(originals[new])
for name,before,after in [('consolidate.py',before_con,after_con),('build_paper.py',before_build,after_build),('RESEARCH_SA15_paper.tex',before_paper,after_paper)]:
 (snap/(name+'.before')).write_text(before)
 (snap/(name+'.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
for n,t in generated.items():(c/n).write_text(t)
consolidate.write_text(after_con);builder.write_text(after_build);paper.write_text(after_paper)
(w/'notes/checkpoint34_promoted_inputs.json').write_text('[]\n')
(w/'notes/checkpoint34_changes.md').write_text('''# Checkpoint 34 continuation

The work remains INCOMPLETE. General A.3, A.4, higher-dimensional B.3 and general B.4 remain open. A.5 remains completely settled. No candidate or numerical necessary pattern changes an outcome before its full proof audits and explicit promotion.

## Preserved checkpoint 33

Checkpoint 33 was verified at 03:37:05.476477 UTC on 20 November 2026 and successfully saved and delivered afterward. Its immutable ZIP has 38,670,512 bytes and 3,083 members (3,082 manifest hashes), SHA256 382b943b7d689d2754d70aeba3a1ae1b820189ff5c42c0eeee85847af7e99875. The final converged PDF has 731 pages, 5,123,512 bytes and SHA256 ea99a27826f7221acc327cb54ded638c46928e93ec6a531fca57b7c0cdba0c7e. It contains 915 numbered statements, 2,715 check events and 835 exported agent program/output files. All 34 selected final images were actually inspected, including five contents pages corrected by the extra convergence pass. Two compilation attempts succeeded; no box exceeded 2pt, the only residual overflow was 0.41342pt, and there were no missing references, citations or glyphs. The failed page-equivalence assertion that detected the contents change was preserved with exact code/output and its correction. The archive ran slightly after its 03:35:40 schedule to complete these real final-image checks; no early archive was made.

## Current timing and setup

Actual review 23 is due 03:50:40 UTC; checkpoint 34 is due 04:20:40 UTC. Review 24 is due 04:50:40 UTC and checkpoint 35 is due 05:05:40 UTC. This setup is not a review, build, finalization or archive. The builder now continues until its cross-reference rerun notice clears, with retained output and a bounded failure guard. The contents number column has been widened for three-digit subsection numbers, and the next visual sample will include every contents page. These layout safeguards change no mathematics.

## Active unpromoted work

The complete odd-cover deck-slice proof is under root audit and gives a candidate quotient-dimension bound of eight. Its broader odd-source variant is a separate candidate. Part B research is investigating the remaining (5,45) crossing via actual point fields, cyclic characters and ramification; no exclusion is claimed until its complete proof and exact supplement pass independent audits.
''')
(w/'notes/ROOT_SEARCH_LOG_34.md').write_text('''# Root source and search log, checkpoint 34

The checkpoint 33 original-source readings and exact searches remain in notes/ROOT_SEARCH_LOG_33.md. No new external theorem is imported merely by this workflow setup. New source accesses and unsuccessful routes will be recorded here with their actual scopes.
''')
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'generated_scripts':names,
 'archive_not_before_utc':'2026-11-20T04:20:40+00:00','completed_review_required':23,
 'next_review_due_utc':'2026-11-20T04:50:40+00:00','next_checkpoint_due_utc':'2026-11-20T05:05:40+00:00',
 'convergence_guard_added':True,'contents_number_column_em':3.5,
 'scope':'Syntax-checked setup only; no new build, review, finalization or archive was run.'}
(snap/'record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
