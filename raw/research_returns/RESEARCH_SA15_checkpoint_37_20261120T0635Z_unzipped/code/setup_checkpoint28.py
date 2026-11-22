"""Create CP28 workflows after CP27 release; explicit identifiers only."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import re

w = Path(__file__).resolve().parents[1]
c = w / 'code'
required = ['agents/reduction_descent/B_terminal_frobenius_pair.tex']
sources = {
    'prepare_checkpoint28.py': 'prepare_checkpoint27.py',
    'finalize_checkpoint28.py': 'finalize_checkpoint27.py',
    'archive_checkpoint28.py': 'archive_checkpoint27.py',
    'verify_program_paths28.py': 'verify_program_paths27.py',
    'render_qa28.py': 'render_qa27.py',
}
for name in sources:
    assert not (c / name).exists(), name
for rel in required:
    assert (w / rel).exists(), rel
    assert r'\status{Candidate' not in (w / rel).read_text(), rel
snap = w / 'outputs/checkpoint28_workflow_setup'
search = w / 'notes/ROOT_SEARCH_LOG_28.md'
assert not snap.exists()
assert not search.exists()


def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


def identifiers(text):
    substitutions = {
        'checkpoint27': 'checkpoint28',
        'checkpoint_27': 'checkpoint_28',
        'Checkpoint27': 'Checkpoint28',
        'CP27': 'CP28',
        'qa27': 'qa28',
        'update_current27': 'update_current28',
        "'checkpoint':27": "'checkpoint':28",
    }
    pattern = re.compile('|'.join(re.escape(k) for k in
                                 sorted(substitutions, key=len, reverse=True)))
    return pattern.sub(lambda m: substitutions[m.group()], text)


originals = {new: (c / old).read_text() for new, old in sources.items()}
prepare = identifiers(originals['prepare_checkpoint28.py'])
a = prepare.index('required=')
b = prepare.index('\nfor rel in required:', a)
prepare = prepare[:a] + 'required=' + repr(required) + prepare[b:]

finalize = identifiers(originals['finalize_checkpoint28.py'])
finalize = once(finalize, 'RESEARCH_SA15_checkpoint_26.zip',
                'RESEARCH_SA15_checkpoint_27.zip')
finalize = once(finalize, 'new identifiers since checkpoint26',
                'new identifiers since checkpoint27')
finalize = finalize.replace('progress_review_18.json', 'progress_review_19.json')
finalize = once(finalize, "assert review['review']==18", "assert review['review']==19")
finalize = once(finalize, "{'review':18,", "{'review':19,")
finalize = once(finalize, '2026-11-19T22:50:40+00:00',
                '2026-11-19T23:50:40+00:00')
a = finalize.index('Checkpoint28 is archived only at or after')
last = 'No review or archive is represented as completed before its actual execution.'
b = finalize.index(last, a) + len(last)
finalize = finalize[:a] + (
    'Checkpoint28 is archived only at or after23:50:40UTC on19November2026. '
    'Actual review19 was recorded at {review_actual.isoformat()}, read directly '
    'from notes/progress_review_19.json; its recorded no-movement streak is '
    "{review['no_movement_streak']}. The next actual review20 is due00:50:40UTC "
    'on20November2026 and checkpoint29 is due00:35:40UTC on20November2026. '
    + last) + finalize[b:]
a = finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b = finalize.index("assert (w/'RESEARCH_SA15_report.md')", a)
finalize = finalize[:a] + '''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint28 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are explicitly enumerated in notes/checkpoint28_changes.md and in the retained '
            'checkpoint28 integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Actual review19 was recorded at '+review_actual.isoformat()+
            '; the next actual review20 is due00:50:40UTC on20November2026 and '
            'checkpoint29 is due00:35:40UTC on20November2026. '
            'This snapshot does not replace an actual review.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
''' + finalize[b:]

archive = '''"""Archive CP28 after its due time, actual review19, and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-19T23:50:40+00:00')
review=json.loads((w/'notes/progress_review_19.json').read_text())
assert review['review']==19
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-19T23:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint28.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_28.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','28'),('verify_checkpoint_archive.py','28')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify = identifiers(originals['verify_program_paths28.py'])
render = identifiers(originals['render_qa28.py'])

original_consolidate = (c / 'consolidate.py').read_text()
consolidated = original_consolidate
if "'B_terminal_frobenius_pair.tex'" not in consolidated:
    consolidated = once(consolidated, "'B_iterated_high_quotient.tex']:",
                        "'B_iterated_high_quotient.tex',\n"
                        "                    'B_terminal_frobenius_pair.tex']:")
consolidated = once(consolidated, r'\\path{notes/ROOT_SEARCH_LOG_27.md}',
                    r'\\path{notes/ROOT_SEARCH_LOG_27.md}, and' + '\n' +
                    r'\\path{notes/ROOT_SEARCH_LOG_28.md}')
generated = dict(zip(sources, [prepare, finalize, archive, verify, render]))
for name, text in generated.items():
    tree = ast.parse(text, filename=name)
    for node in ast.walk(tree):
        if (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                and node.value.id == 'hashlib'):
            assert node.attr == 'sha256', (name, node.attr)
    assert set(re.findall(r'sha\d+', text)) <= {'sha256'}, name
    assert 'pdf_sha268' not in text and 'pdf_sha267' not in text, name
ast.parse(consolidated, filename='consolidate.py')
assert 'RESEARCH_SA15_checkpoint_27.zip' in finalize
assert 'new identifiers since checkpoint27' in finalize
assert 'progress_review_19.json' in finalize and 'progress_review_19.json' in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-19T23:50:40+00:00' in finalize
assert archive.count('2026-11-19T23:50:40+00:00') == 2
assert 'update_current28.py' in prepare and 'update_current28.py' in finalize
assert 'asserted integral inverse formula' in render and '173' not in render
assert 'checkpoint29 is due00:35:40UTC on20November2026' in finalize
assert 'progress_review_18.json' not in finalize + archive
assert 'Actual review18' not in finalize
assert '22:50:40' not in finalize + archive
assert '23:05:40' not in finalize + archive
assert all('hashlib.sha256' in generated[n] for n in
           ['finalize_checkpoint28.py', 'archive_checkpoint28.py', 'render_qa28.py'])

snap.mkdir()
(snap / 'consolidate.before.py').write_text(original_consolidate)
for new, old in sources.items():
    (snap / old).write_text(originals[new])
for name, text in generated.items():
    (c / name).write_text(text)
(c / 'consolidate.py').write_text(consolidated)
search.write_text('# Root source and search log: checkpoint28\n\n'
                  'No new root source-read or search entry has yet been recorded in this dated log. '
                  'Actual accesses must be added with their precise scope; this setup stub makes no access claim.\n')
record = {
    'status': 'PASS',
    'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Workflow setup, AST and semantic hash/time/path checks only. No preparation, build, render, finalization, review or archive executed.',
    'generated_scripts': list(generated),
    'required_canonical_inputs': required,
    'generated_sha256': {name: hashlib.sha256(text.encode()).hexdigest()
                         for name, text in generated.items()},
    'consolidate_before_sha256': hashlib.sha256(original_consolidate.encode()).hexdigest(),
    'consolidate_after_sha256': hashlib.sha256(consolidated.encode()).hexdigest(),
    'previous_checkpoint_for_statement_ids': 27,
    'actual_review_required': 19,
    'review_due_utc': '2026-11-19T23:50:40+00:00',
    'archive_not_before_utc': '2026-11-19T23:50:40+00:00',
    'next_review_due_utc': '2026-11-20T00:50:40+00:00',
    'next_checkpoint_due_utc': '2026-11-20T00:35:40+00:00',
    'semantic_checks': [
        'Only designated checkpoint identifiers replaced; no bare digit substitution.',
        'Every hashlib call is sha256 and all hash keys remain pdf_sha256.',
        'Finalizer requires actual review19 timestamp at or after its due time and no later than execution.',
        'Archive requires its due time and exactly the review19 timestamp retained by final QA.',
        'Statement comparison uses immutable checkpoint27 ZIP and archive cannot overwrite checkpoint28.',
        'QA locates the historical overflow paragraph from actual PDF text, not a fixed page number.',
        'Dates across midnight are explicit; no future review or archive is represented as completed.',
        'Only the promoted B75 canonical is newly required; isolated research is not promoted.'
    ]
}
(snap / 'setup_record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
