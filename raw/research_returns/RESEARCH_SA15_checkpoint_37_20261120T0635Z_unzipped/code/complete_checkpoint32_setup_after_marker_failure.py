"""Complete the interrupted CP32 setup, preserving its exact failed execution."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1];c=w/'code'
snap=w/'outputs/checkpoint32_workflow_setup';assert snap.is_dir()
failed=c/'setup_checkpoint32.py'
copy=c/'audit_snapshots/setup_checkpoint32_failed01.py';assert not copy.exists()
shutil.copy2(failed,copy)
for suffix in ['stdout.json','stderr.txt']:
 src=w/f'outputs/checkpoint32_setup.{suffix}'
 dst=w/f'outputs/checkpoint32_setup_failed01.{suffix}'
 assert not dst.exists();shutil.copy2(src,dst)
names=['prepare_checkpoint32.py','finalize_checkpoint32.py','archive_checkpoint32.py',
       'verify_program_paths32.py','render_qa32.py']
for name in names:ast.parse((c/name).read_text(),filename=name)
finalize=(c/'finalize_checkpoint32.py').read_text()
archive=(c/'archive_checkpoint32.py').read_text()
assert 'RESEARCH_SA15_checkpoint_31.zip' in finalize
assert 'progress_review_22.json' in finalize+archive
assert 'progress_review_21.json' not in finalize+archive
assert "assert review['review']==22" in finalize and "assert review['review']==22" in archive
assert '2026-11-20T02:50:40+00:00' in finalize+archive
assert '02:05:40' not in finalize+archive
consolidate=c/'consolidate.py';before=consolidate.read_text()
needle=r'\\path{notes/ROOT_SEARCH_LOG_31.md}'
assert before.count(needle)==1 and 'ROOT_SEARCH_LOG_32.md' not in before
after=before.replace(needle,needle+'\n'+r'\\path{notes/ROOT_SEARCH_LOG_32.md}')
ast.parse(after)
(snap/'consolidate.before.py').write_text(before)
(snap/'consolidate.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
consolidate.write_text(after)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
log=w/'notes/ROOT_SEARCH_LOG_32.md';assert not log.exists()
log.write_text('''# Root search log, checkpoint32

Actual research continuation after the successful checkpoint31 save. General A.3, A.4, higher-dimensional B.3 and general B.4 remain open. No priority claim is made.

## Hasse-divisor algebra

The exact universal Moore remainder modulo the Fermat cubic was reconstructed, and its full-coordinate-torus coefficient conditions were retained. This is exploratory exact algebra, not a Cartier or monodromy theorem. The prior support classification does not itself imply the same classification for divisibility by a fixed cubic.

## Literature searches in this interval

Both web search systems were used for Heisenberg-invariant cubics in P8, the base locus of the five invariant cubics,81 linear spaces, Coble cubics in characteristic two, and Fermat divisibility. Search results led to Beauville's Coble paper and the Benedetti--Manivel--Tanturri Coble geometry paper, but no full new proof was read or imported in this interval. Previously read Coble sources retain their earlier explicitly limited characteristic scope; no characteristic-two extension is inferred from these search results.

A further search for Pfaffian Cremona maps, height-two submaximal Pfaffian ideals, and analytic spread returned Russo--Simis Example2.5 and later generic-height Rees-ring work. The result assumes height3; it does not establish the missing height condition. No new theorem is cited as solving that gate.

## Explicit cyclotomic base

The root read the complete B89 proof and checker and reread the complete internal B60 lower-break and B88 tame-scaling proofs. The unchanged independent check passed. This realizes the necessary base/cyclotomic data only; it does not realize an ambiguous height-two pair.
''')
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('''
## Checkpoint31 preservation and next gates

Checkpoint31 was archived and manifest-verified after02:05:40UTC, saved successfully and delivered as its own immutable ZIP. It has34,581,553bytes,2,829members,2,828manifest hashes, and SHA25609d8ce9622002684825e86d1eb910e9a9b2675f6057afc74a4367c2d22434c5d. Its700-page paper,876numbered statements and2,553check events remain unchanged in that checkpoint. The current report table now escapes literal vertical bars in mathematical linear-system notation so that Markdown columns remain intact. This formatting correction changes no mathematical assertion.

The initial checkpoint32 setup created its five workflow scripts, then stopped at an administrative assertion expecting a quoted search-log list item in consolidate.py. The actual entry is LaTeX prose. No mathematical assertion failed and no build or archive ran. The exact failed script and streams are retained. A separate completion script checked the generated workflows and inserted the correct LaTeX path marker, preserving the prior file and diff.

Next actual review22 and checkpoint32 are both due02:50:40UTC on20November2026. Workflow creation is not an actual review, PDF build, finalization or checkpoint. The next review23 is due03:50:40UTC and checkpoint33 is due03:35:40UTC.
''')
record={'status':'PASS_AFTER_RETAINED_ADMINISTRATIVE_MARKER_FAILURE',
 'actual_completion_utc':now,'generated_scripts':names,
 'scope':'Workflow setup only; no build, review, finalization or archive executed.',
 'generated_sha256':{name:hashlib.sha256((c/name).read_bytes()).hexdigest() for name in names},
 'failed_script':str(copy.relative_to(w)),
 'failed_stderr':'outputs/checkpoint32_setup_failed01.stderr.txt',
 'failure_reason':'Expected quoted list marker; actual consolidate.py contains a LaTeX prose path.',
 'consolidate_before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'consolidate_after_sha256':hashlib.sha256(after.encode()).hexdigest(),
 'required_canonical_inputs':['agents/reduction_descent/B_p5_cyclotomic_break_three_example.tex'],
 'previous_checkpoint_for_statement_ids':31,'actual_review_required':22,
 'archive_not_before_utc':'2026-11-20T02:50:40+00:00',
 'required_review_due_utc':'2026-11-20T02:50:40+00:00',
 'next_review_due_utc':'2026-11-20T03:50:40+00:00',
 'next_checkpoint_due_utc':'2026-11-20T03:35:40+00:00'}
(snap/'setup_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
