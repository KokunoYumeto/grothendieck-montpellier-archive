"""Create CP26 workflows only; preserve CP25 and never build or archive here."""
from pathlib import Path
import ast
import datetime
import hashlib
import json

w = Path(__file__).resolve().parents[1]
code = w / 'code'
required = [
    'agents/monodromy/nonordinary_rank_one_bad_five_kernel.tex',
    'agents/reduction_descent/B_one_slope_quotient.tex',
    'agents/reduction_descent/B_next_tame_boundary.tex',
]
names = ['prepare_checkpoint26.py', 'finalize_checkpoint26.py',
         'archive_checkpoint26.py', 'verify_program_paths26.py', 'render_qa26.py']
for name in names:
    assert not (code / name).exists(), name
for rel in required:
    assert (w / rel).exists(), rel
    assert '\\status{Candidate' not in (w / rel).read_text(), rel
snapshot = w / 'outputs/checkpoint26_workflow_setup'
assert not snapshot.exists(), snapshot
search_log = w / 'notes/ROOT_SEARCH_LOG_26.md'
assert not search_log.exists(), search_log

def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)

original = (code / 'consolidate.py').read_text()
consolidated = once(original,
    "'monodromy/nonordinary_odd_theta_nodality_reduction.tex']:",
    "'monodromy/nonordinary_odd_theta_nodality_reduction.tex',\n"
    "                  'monodromy/nonordinary_rank_one_bad_five_kernel.tex']:")
consolidated = once(consolidated,
    "'B_initial_tame_sector.tex']:",
    "'B_initial_tame_sector.tex',\n"
    "                    'B_one_slope_quotient.tex',\n"
    "                    'B_next_tame_boundary.tex']:")
consolidated = once(consolidated,
    r'\\path{notes/ROOT_SEARCH_LOG_25.md}',
    r'\\path{notes/ROOT_SEARCH_LOG_25.md}, and' + '\n' +
    r'\\path{notes/ROOT_SEARCH_LOG_26.md}')

def checkpoint_names_25_to_26(text):
    # Replace only designated checkpoint/workflow identifiers, never digits in hashes.
    for old_name, new_name in [
        ('checkpoint25', 'checkpoint26'), ('checkpoint_25', 'checkpoint_26'),
        ('Checkpoint25', 'Checkpoint26'), ('CP25', 'CP26'), ('qa25', 'qa26'),
        ('update_current25', 'update_current26'), ("'checkpoint':25", "'checkpoint':26")]:
        text = text.replace(old_name, new_name)
    assert 'sha266' not in text
    return text

prepare = checkpoint_names_25_to_26((code / 'prepare_checkpoint25.py').read_text())
start = prepare.index('required=')
end = prepare.index('\nfor rel in required:', start)
prepare = prepare[:start] + 'required=' + repr(required) + prepare[end:]

finalize = checkpoint_names_25_to_26((code / 'finalize_checkpoint25.py').read_text())
finalize = once(finalize, "RESEARCH_SA15_checkpoint_24.zip", "RESEARCH_SA15_checkpoint_25.zip")
finalize = once(finalize, 'new identifiers since checkpoint24', 'new identifiers since checkpoint25')
finalize = once(finalize,
    'now=datetime.datetime.now(datetime.timezone.utc).isoformat()',
    '''now_dt=datetime.datetime.now(datetime.timezone.utc)
now=now_dt.isoformat()
review=json.loads((w/'notes/progress_review_17.json').read_text())
assert review['review']==17
review_actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
review_due=datetime.datetime.fromisoformat('2026-11-19T21:50:40+00:00')
assert review_due<=review_actual<=now_dt, (review_due,review_actual,now_dt)''')
finalize = once(finalize,
    "dest.write_text(json.dumps(qa,indent=2)+'\\n')",
    "qa['required_actual_review']={'review':17,'actual_utc':review_actual.isoformat(),'source':'notes/progress_review_17.json'}\n"
    "dest.write_text(json.dumps(qa,indent=2)+'\\n')")
old_timing = ('Checkpoint26 is archived only at or after21:35:40UTC. '
              'Actual review16 was recorded20:50:41.784886UTC, with movement and zero no-movement streak. '
              'The next actual review17 is due21:50:40UTC and checkpoint26 is due22:20:40UTC. '
              'No early review or early archive is represented as completed.')
new_timing = ('Checkpoint26 is archived only at or after22:20:40UTC. '
              'Actual review17 was recorded at {review_actual.isoformat()}, read directly from '
              'notes/progress_review_17.json; its recorded no-movement streak is '
              "{review['no_movement_streak']}. The next actual review18 is due22:50:40UTC "
              'and checkpoint27 is due23:05:40UTC. No review or archive is represented as '
              'completed before its actual execution.')
finalize = once(finalize, old_timing, new_timing)
ledger_start = finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
ledger_end = finalize.index("assert (w/'RESEARCH_SA15_report.md')", ledger_start)
finalize = finalize[:ledger_start] + '''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint26 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The proved additions '
            'include the explicit rank-one five-kernel counterexample, the one-slope quotient '
            'recovery theorem at e=p squared-1, and the next tame boundary '
            'e=(p+2)(p-1). The bad-kernel example does not rule out a good incoming neighbour. '
            'General A.3/A.4, the primitive mixed restricted-cup nonvanishing gate, '
            'higher-dimensional B.3 and other exact B.4 indices remain open. '
            'Actual review17 was recorded at '+review_actual.isoformat()+
            '; the next actual review18 is due22:50:40UTC and checkpoint27 is due23:05:40UTC. '
            'This snapshot does not replace either actual review.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
''' + finalize[ledger_end:]

archive = '''"""Archive CP26 only after its due time, actual review17, and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-19T22:20:40+00:00')
review=json.loads((w/'notes/progress_review_17.json').read_text())
assert review['review']==17
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-19T21:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint26.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_26.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','26'),('verify_checkpoint_archive.py','26')]:
    cmd=[sys.executable,str(w/'code'/name)]
    if arg is not None:cmd.append(arg)
    subprocess.run(cmd,check=True,cwd=w)
'''

verify = checkpoint_names_25_to_26((code / 'verify_program_paths25.py').read_text())
render = '''"""Render CP26 additions and dynamically located overflow text for actual QA."""
from pathlib import Path
import json,re,hashlib,datetime
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
attempts=sorted((w/'outputs').glob('checkpoint26_integration_attempt*.json'))
assert attempts
integration=json.loads(attempts[-1].read_text());assert integration['build_exit_code']==0
titles=[]
for rel in integration['promoted_files']:
    titles.extend(re.findall(r'\\\\subsection\\{([^}]+)\\}',(w/rel).read_text()))
def key(s):return s.split('\\\\(')[0].strip()
pages={n for n in [1,14,28,55,85,126,len(d)-1,len(d)] if 1<=n<=len(d)}
matched=[]
for j,(level,title,start) in enumerate(toc):
    if any(title.startswith(key(t)) for t in titles):
        end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==len(titles),{'titles':titles,'matched':matched}
# The historical 0.41342pt paragraph moves as sections are added: locate its text.
phrase='asserted integral inverse formula'
overflow_pages=[i+1 for i,p in enumerate(d) if phrase in ' '.join(p.get_text().split())]
assert len(overflow_pages)==1,overflow_pages
pages.update(overflow_pages)
folder=w/'outputs/qa26';assert not folder.exists();folder.mkdir()
pending_path=w/'outputs/visual_qa26_pending.json';assert not pending_path.exists()
for n in sorted(pages):
    d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'rendered_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'pages_in_pdf':len(d),'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),
        'pages_rendered':sorted(pages),'new_subsections':matched,
        'overflow_location_phrase':phrase,'exact_remaining_overflow_pages':overflow_pages,
        'manual_visual_review':'PENDING'}
pending_path.write_text(json.dumps(record,indent=2)+'\\n')
print(json.dumps(record,indent=2))
'''

generated = dict(zip(names, [prepare, finalize, archive, verify, render]))
for name, text in generated.items():
    ast.parse(text, filename=name)
ast.parse(consolidated, filename='consolidate.py')
assert 'RESEARCH_SA15_checkpoint_25.zip' in finalize
assert 'progress_review_17.json' in finalize and 'progress_review_17.json' in archive
assert '23:05:40' in finalize and '22:50:40' in finalize
assert '173' not in render

snapshot.mkdir()
(snapshot/'consolidate.before.py').write_text(original)
for old in ['prepare_checkpoint25.py','finalize_checkpoint25.py','archive_checkpoint25.py',
            'verify_program_paths25.py','render_qa25.py']:
    (snapshot/old).write_bytes((code/old).read_bytes())
for name,text in generated.items():
    (code/name).write_text(text)
(code/'consolidate.py').write_text(consolidated)
search_log.write_text('# Root source and search log: checkpoint26\n\n'
                      'No new root search entry has yet been recorded in this dated log. '
                      'Actual source reads and searches must be added with their precise scope; '
                      'this setup stub makes no source-access claim.\n')
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status':'PASS','scope':'Workflow creation and static syntax checks only; no build, finalization, archive, or review executed.',
        'generated_scripts':names,'required_canonical_inputs':required,
        'consolidate_before_sha256':hashlib.sha256(original.encode()).hexdigest(),
        'consolidate_after_sha256':hashlib.sha256(consolidated.encode()).hexdigest(),
        'generated_sha256':{n:hashlib.sha256(t.encode()).hexdigest() for n,t in generated.items()},
        'previous_checkpoint_for_statement_ids':25,'actual_review_required':17,
        'review_due_utc':'2026-11-19T21:50:40+00:00','archive_not_before_utc':'2026-11-19T22:20:40+00:00',
        'next_review_due_utc':'2026-11-19T22:50:40+00:00','next_checkpoint_due_utc':'2026-11-19T23:05:40+00:00'}
(snapshot/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
