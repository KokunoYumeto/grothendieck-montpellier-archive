"""Prepare CP36 after the immutable CP35 save; no review/build/archive is executed."""
from pathlib import Path
import ast, datetime, difflib, json, re
w=Path(__file__).resolve().parents[1]; c=w/'code'
mapping={f'{stem}36.py':f'{stem}35.py' for stem in ['prepare_checkpoint','finalize_checkpoint','verify_program_paths','render_qa','archive_checkpoint']}
names=list(mapping)+['update_current36.py']
assert all(not(c/n).exists() for n in names)
folder=w/'outputs/checkpoint36_workflow_setup'; assert not folder.exists()
def ids(text):
 changes={'checkpoint35':'checkpoint36','checkpoint_35':'checkpoint_36','Checkpoint35':'Checkpoint36','CP35':'CP36','qa35':'qa36','update_current35':'update_current36',"'checkpoint':35":"'checkpoint':36"}
 pattern=re.compile('|'.join(re.escape(k) for k in sorted(changes,key=len,reverse=True)))
 return pattern.sub(lambda m:changes[m.group()],text)
originals={new:(c/old).read_text() for new,old in mapping.items()}
generated={new:ids(text) for new,text in originals.items()}
final=generated['finalize_checkpoint36.py']
final=final.replace('RESEARCH_SA15_checkpoint_34.zip','RESEARCH_SA15_checkpoint_35.zip').replace('since checkpoint34','since checkpoint35')
final=final.replace('progress_review_24','progress_review_25').replace("review['review']==24","review['review']==25").replace("'review':24","'review':25")
final=final.replace('2026-11-20T04:50:40','2026-11-20T05:50:40')
a=final.index('Checkpoint36 is archived only at or after')
ending='No review or archive is represented as completed before its actual execution.'
b=final.index(ending,a)+len(ending)
final=final[:a]+("Checkpoint36 is archived only at or after05:50:40UTC on20November2026. Completed actual review25 was recorded at {review_actual.isoformat()}, read directly from notes/progress_review_25.json; its no-movement streak is {review['no_movement_streak']}. The next checkpoint37 is due06:35:40UTC and the next actual review26 is due06:50:40UTC. This checkpoint does not claim that either future event has occurred. "+ending)+final[b:]
a=final.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b=final.index("assert (w/'RESEARCH_SA15_report.md')",a)
final=final[:a]+'''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint36 current-gate snapshot\\n\\n'
            'This is a snapshot, not an hourly review. Audited additions and retained '
            'unsuccessful approaches are in notes/checkpoint36_changes.md. Candidate '
            'work is not promoted by this snapshot. Completed actual review25 was '
            'recorded at '+review_actual.isoformat()+
            '; checkpoint37 is due06:35:40UTC and actual review26 is due06:50:40UTC '
            'on20November2026. Checkpoint36 and actual review25 are due05:50:40UTC.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
'''+final[b:]
generated['finalize_checkpoint36.py']=final
archive=generated['archive_checkpoint36.py']
archive=archive.replace('after05:05:40','after05:50:40').replace('T05:05:40','T05:50:40')
archive=archive.replace('progress_review_24','progress_review_25').replace("review['review']==24","review['review']==25").replace('T04:50:40','T05:50:40').replace('review24','review25')
archive=archive.replace("('checkpoint.py','35')","('checkpoint.py','36')").replace("('verify_checkpoint_archive.py','35')","('verify_checkpoint_archive.py','36')")
generated['archive_checkpoint36.py']=archive
generated['update_current36.py']='''"""Refresh CP36 from explicitly promoted canonical inputs only."""
from pathlib import Path
import subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/update_current35.py')],cwd=w,check=True)
p=w/'RESEARCH_SA15_report.md';text=p.read_text()
marker='\\n## Checkpoint 36 work: primitive sources and the remaining wild image\\n'
if marker in text:text=text.split(marker)[0]
p.write_text(text+marker+'\\n'+(w/'notes/checkpoint36_changes.md').read_text())
assert p.read_text().startswith('INCOMPLETE\\n\\n| Item |')
print('CP36 initial wrapper refreshed; candidates do not change a gate.')
'''
consolidate=c/'consolidate.py';before=consolidate.read_text();needle=r'\path{notes/ROOT_SEARCH_LOG_35.md}'
assert before.count(needle)==1 and 'ROOT_SEARCH_LOG_36.md' not in before
after=before.replace(needle,needle+'\n'+r'\path{notes/ROOT_SEARCH_LOG_36.md}')
for name,text in generated.items():ast.parse(text,filename=name)
ast.parse(after)
assert 'progress_review_25.json' in final+archive and 'progress_review_26.json' not in final+archive
assert 'RESEARCH_SA15_checkpoint_35.zip' in final and "('checkpoint.py','36')" in archive
assert 'T05:50:40' in archive and 'checkpoint37 is due06:35:40' in final
for rel in ['checkpoint36_changes.md','ROOT_SEARCH_LOG_36.md','checkpoint36_promoted_inputs.json']:
 assert not(w/'notes'/rel).exists()
folder.mkdir()
for new,old in mapping.items():(folder/old).write_text(originals[new])
(folder/'consolidate.py.before').write_text(before)
(folder/'consolidate.py.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
for name,text in generated.items():(c/name).write_text(text)
consolidate.write_text(after)
(w/'notes/checkpoint36_promoted_inputs.json').write_text('[]\n')
(w/'notes/checkpoint36_changes.md').write_text('''# Checkpoint 36 continuation

The work remains INCOMPLETE. General A.3, A.4, higher-dimensional B.3 and general B.4 remain open. A.5 is completely settled. An isolated candidate, a necessary bound and a complete full-image theorem retain their exact scopes.

## Preserved checkpoint 35

Checkpoint35 was verified at05:05:51.543529 UTC on20November2026 and successfully saved and delivered afterward. Its immutable ZIP has43,270,155bytes and3402members (3401 manifest hashes), SHA256 4b89ef83380fc0b5aab648e254070efd1f05d4a3df521e6d75aa917aa71ad675. The final paper has765pages,5,341,815bytes and SHA256 d951489941df01521c8f1309fa88a77580a9cc0248672284f0bfaf9cc649d738. There are959 numbered statements,2904 check events at archiving and894 exported agent program/output files. The finalizer's earlier export count is explicitly time-dependent: later isolated candidate/audit work was also retained before archiving without promotion. All38 selected final images were actually opened and inspected, including every contents page, every new subsection, the remaining overflow paragraph and the final bibliography. Twenty-seven statement identifiers were added and none removed; each new identifier has an event.

The only actual build succeeded in82.296seconds with four LuaLaTeX passes including one convergence pass. It has no unresolved reference/citation, missing glyph or rerun notice. There were zero boxes above2pt and a sole residual0.41342pt paragraph, which was actually inspected. The initial truncated root and monodromy image calls were not credited; every affected page was reopened completely.

## Current timing

Checkpoint36 and actual review25 are both due05:50:40UTC. Completed actual review24 occurred at04:52:15.131064UTC and recorded qualifying A.4/B.4 reductions, with no-movement streak0. After checkpoint36, checkpoint37 is due06:35:40UTC and actual review26 is due06:50:40UTC. This setup executes none of those future events.

## Work at the preceding freeze

The primitive globally generated type(1,3) theorem was written with exact stability, Cartier, smoothing and Lang-slice proofs. Its monodromy companion audit passed before checkpoint35 archiving; the full root proof/source/code audit passed afterward, at05:07:53.887641UTC. Its38-identity unchanged isolated rerun took0.06900425799540244seconds. Promotion is a separate recorded operation. This special source theorem does not close degree17 or general A.4.

The B96 selected-high-point candidate and its exact finite supplement were frozen and retained as unpromoted work in checkpoint35. It uses an actual selected quotient125 point from the original125 comparison, with no assumption of all quotient125 torsion. Its independent audits and any eventual gate change must be separately recorded. The totally ramified hypothesis was made explicit in the abstract coefficient lemma, with prior/diff retained.
''')
(w/'notes/ROOT_SEARCH_LOG_36.md').write_text('''# Root source and search log, checkpoint 36

Earlier exact original-source accesses remain in ROOT_SEARCH_LOG_35.md and the prior logs. The root primitive audit uses the already opened full higher-dimensional Sun filtration proof, with its exact passage scope in notes/CP35_primitive_source_scope/record.json. It uses the previously audited original AV theta-descent facts. The new proof itself supplies surface Frobenius stability, the effective-divisor inequality, the complete principal-theta alternative, nodal smoothing and both explicit Lang restrictions. No new external opening is claimed by this setup.
''')
r={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'generated_scripts':names,'archive_not_before_utc':'2026-11-20T05:50:40+00:00',
 'completed_review_required':25,'review25_due_utc':'2026-11-20T05:50:40+00:00',
 'next_checkpoint_due_utc':'2026-11-20T06:35:40+00:00','next_review_due_utc':'2026-11-20T06:50:40+00:00',
 'scope':'Generated scripts syntax-checked before mutation. No review, build, finalization or archive executed.'}
(folder/'record.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
