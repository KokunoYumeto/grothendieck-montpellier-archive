"""Create CP29 workflows after CP28 release using explicit identifier changes."""
from pathlib import Path
import ast
import datetime
import hashlib
import json
import re

w = Path(__file__).resolve().parents[1]
c = w / 'code'
required = ['agents/reduction_descent/B_first_wild_irreducible_image.tex']
sources = {
    'prepare_checkpoint29.py': 'prepare_checkpoint28.py',
    'finalize_checkpoint29.py': 'finalize_checkpoint28.py',
    'archive_checkpoint29.py': 'archive_checkpoint28.py',
    'verify_program_paths29.py': 'verify_program_paths28.py',
    'render_qa29.py': 'render_qa28.py',
}
for name in sources:
    assert not (c / name).exists(), name
for rel in required:
    assert (w / rel).exists(), rel
    assert r'\status{Candidate' not in (w / rel).read_text(), rel
snap = w / 'outputs/checkpoint29_workflow_setup'
search = w / 'notes/ROOT_SEARCH_LOG_29.md'
assert not snap.exists()
search_before = search.read_bytes() if search.exists() else None


def once(text, old, new):
    assert text.count(old) == 1, (old, text.count(old))
    return text.replace(old, new)


def identifiers(text):
    substitutions = {
        'checkpoint28': 'checkpoint29',
        'checkpoint_28': 'checkpoint_29',
        'Checkpoint28': 'Checkpoint29',
        'CP28': 'CP29',
        'qa28': 'qa29',
        'update_current28': 'update_current29',
        "'checkpoint':28": "'checkpoint':29",
    }
    pattern = re.compile('|'.join(re.escape(k) for k in
                                 sorted(substitutions, key=len, reverse=True)))
    return pattern.sub(lambda m: substitutions[m.group()], text)


originals = {new: (c / old).read_text() for new, old in sources.items()}
prepare = identifiers(originals['prepare_checkpoint29.py'])
a = prepare.index('required=')
b = prepare.index('\nfor rel in required:', a)
prepare = prepare[:a] + 'required=' + repr(required) + prepare[b:]

finalize = identifiers(originals['finalize_checkpoint29.py'])
finalize = once(finalize, 'RESEARCH_SA15_checkpoint_27.zip',
                'RESEARCH_SA15_checkpoint_28.zip')
finalize = once(finalize, 'new identifiers since checkpoint27',
                'new identifiers since checkpoint28')
# CP29 precedes review20. Its required actual review is still review19.
a = finalize.index('Checkpoint29 is archived only at or after')
last = 'No review or archive is represented as completed before its actual execution.'
b = finalize.index(last, a) + len(last)
finalize = finalize[:a] + (
    'Checkpoint29 is archived only at or after00:35:40UTC on20November2026. '
    'Completed actual review19 was recorded at {review_actual.isoformat()}, read directly '
    'from notes/progress_review_19.json; its recorded no-movement streak is '
    "{review['no_movement_streak']}. The next actual review20 is due00:50:40UTC "
    'on20November2026 and checkpoint30 is due01:20:40UTC on20November2026. '
    'Checkpoint29 does not require or report completion of the later review20. '
    + last) + finalize[b:]
a = finalize.index("with (w/'PROGRESS_LEDGER.md').open('a') as f:")
b = finalize.index("assert (w/'RESEARCH_SA15_report.md')", a)
finalize = finalize[:a] + '''with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\\n## '+now+': checkpoint29 current-gate snapshot\\n\\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are explicitly enumerated in notes/checkpoint29_changes.md and in the retained '
            'checkpoint29 integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Completed actual review19 was recorded at '+review_actual.isoformat()+
            '; the next actual review20 is due00:50:40UTC on20November2026 and '
            'checkpoint30 is due01:20:40UTC on20November2026. '
            'Checkpoint29 is due00:35:40UTC, before review20; this snapshot does not replace '
            'an actual review or report review20 early.\\n\\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\\n')
''' + finalize[b:]

archive = '''"""Archive CP29 after its due time, completed review19, and final-image QA."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
assert now>=datetime.datetime.fromisoformat('2026-11-20T00:35:40+00:00')
review=json.loads((w/'notes/progress_review_19.json').read_text())
assert review['review']==19
actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
assert datetime.datetime.fromisoformat('2026-11-19T23:50:40+00:00')<=actual<=now
qa=json.loads((w/'outputs/visual_qa_checkpoint29.json').read_text())
assert qa['status']=='PASS'
assert qa['required_actual_review']['actual_utc']==actual.isoformat()
assert hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()==qa['pdf_sha256']
assert not(w.parent/'RESEARCH_SA15_checkpoint_29.zip').exists()
for name,arg in [('merge_registers.py',None),('export_agent_programs.py',None),
                 ('checkpoint.py','29'),('verify_checkpoint_archive.py','29')]:
    command=[sys.executable,str(w/'code'/name)]
    if arg is not None:command.append(arg)
    subprocess.run(command,check=True,cwd=w)
'''
verify = identifiers(originals['verify_program_paths29.py'])
render = identifiers(originals['render_qa29.py'])
generated = dict(zip(sources, [prepare, finalize, archive, verify, render]))

for name, text in generated.items():
    tree = ast.parse(text, filename=name)
    for node in ast.walk(tree):
        if (isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                and node.value.id == 'hashlib'):
            assert node.attr == 'sha256', (name, node.attr)
    assert set(re.findall(r'sha\d+', text)) <= {'sha256'}, name
    assert not re.search(r'pdf_sha(?!256)\d+', text), name
assert 'RESEARCH_SA15_checkpoint_28.zip' in finalize
assert 'new identifiers since checkpoint28' in finalize
assert 'progress_review_19.json' in finalize and 'progress_review_19.json' in archive
assert 'progress_review_20.json' not in finalize + archive
assert "assert review['review']==19" in finalize and "assert review['review']==19" in archive
assert 'review_actual<=now_dt' in finalize
assert '2026-11-19T23:50:40+00:00' in finalize
assert archive.count('2026-11-20T00:35:40+00:00') == 1
assert archive.count('2026-11-19T23:50:40+00:00') == 1
assert 'update_current29.py' in prepare and 'update_current29.py' in finalize
assert 'asserted integral inverse formula' in render and '173' not in render
assert 'checkpoint30 is due01:20:40UTC on20November2026' in finalize
assert all('hashlib.sha256' in generated[n] for n in
           ['finalize_checkpoint29.py', 'archive_checkpoint29.py', 'render_qa29.py'])

snap.mkdir()
for new, old in sources.items():
    (snap / old).write_text(originals[new])
    assert (snap / old).read_bytes() == (c / old).read_bytes(), old
for name, text in generated.items():
    (c / name).write_text(text)
if search_before is None:
    search.write_text('# Root source and search log: checkpoint29\n\n'
                      'No new root source-read or search entry has yet been recorded in this dated log. '
                      'Actual accesses must be added with their precise scope; this setup stub makes no access claim.\n')
else:
    (snap / 'ROOT_SEARCH_LOG_29.existing.md').write_bytes(search_before)
    assert search.read_bytes() == search_before
record = {
    'status': 'PASS',
    'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Workflow setup, AST and semantic hash/time/path checks only. No preparation, build, render, finalization, review or archive executed. consolidate.py was not mutated; its B79 promotion wiring belongs to the root-authorized reduction/descent agent.',
    'generated_scripts': list(generated),
    'required_canonical_inputs': required,
    'required_input_scope': 'B79 has both complete audits and its proved canonical exists. Setup and prepare29 separately require the actual file and reject Candidate status.',
    'generated_sha256': {name: hashlib.sha256(text.encode()).hexdigest()
                         for name, text in generated.items()},
    'setup_program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'existing_root_search_log_preserved': search_before is not None,
    'root_search_log_sha256': hashlib.sha256(search.read_bytes()).hexdigest(),
    'previous_checkpoint_for_statement_ids': 28,
    'actual_review_required': 19,
    'required_review_due_utc': '2026-11-19T23:50:40+00:00',
    'archive_not_before_utc': '2026-11-20T00:35:40+00:00',
    'next_review_due_utc': '2026-11-20T00:50:40+00:00',
    'next_checkpoint_due_utc': '2026-11-20T01:20:40+00:00',
    'semantic_checks': [
        'Only designated checkpoint identifiers replaced; no bare digit substitution.',
        'Every hashlib call is sha256 and all hash keys remain pdf_sha256.',
        'Finalizer requires completed review19 at or after its actual due time and no later than execution.',
        'Archive waits until Nov20 00:35:40 and requires exactly the review19 timestamp retained by final QA.',
        'Later review20 is not an execution prerequisite and is never represented as completed early.',
        'Statement comparison uses immutable checkpoint28 ZIP; checkpoint29 ZIP cannot be overwritten.',
        'All four owner actual-page records and the final PDF hash remain required.',
        'Historical overflow location is found from actual PDF text, not a fixed page number.',
        'All five prior source scripts are preserved byte-for-byte in the setup folder.'
    ]
}
(snap / 'setup_record.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
