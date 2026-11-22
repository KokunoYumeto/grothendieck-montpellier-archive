"""Prepare CP37 integration without executing any future checkpoint or review."""
from pathlib import Path
import datetime,json,hashlib,difflib,re
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
prior=w/'notes/checkpoint37_setup_priors';assert not prior.exists();prior.mkdir()
inputs={
 'agents/monodromy/prime5_exceptional_wall.tex':'b6ade31cdd499c79e6cd5228c4e33012c0ce9987e3cc82a10fec85635e47451a',
 'agents/obstructions_crystals/A4_type_1_5_evaluation_fibres.tex':'28c0e3f266f06c3b86ef30ed39496446dab8a2564588f6f9b8e3ed0a5623ddd4',
 'notes/primitive_elliptic_double_cover.tex':'c8f0564f8761a67bef88d29ec566f40afe582161a60d8c8f8b93c4273484369b',
 'agents/reduction_descent/B_valuation_one_irreducible.tex':'824d34f2edd04fc578057fc212ca4d7d9e6be4cff8f9141fea525f7e1b673ba9',
 'agents/reduction_descent/B_second_wild_trace_arc.tex':'594cd071143ebdaa9ed6592f1279f18444095ab5188f50f9fa054f2050eb3f96'}
for rel,digest in inputs.items():
 assert hashlib.sha256((w/rel).read_bytes()).hexdigest()==digest,rel
 assert '\\status{Candidate' not in (w/rel).read_text(),rel
(w/'notes/checkpoint37_promoted_inputs.json').write_text(json.dumps(list(inputs),indent=2)+'\n')
(w/'notes/checkpoint37_promoted_hashes.json').write_text(json.dumps(inputs,indent=2)+'\n')
p=w/'code/consolidate.py';old=p.read_text();(prior/'consolidate.py').write_text(old)
needle="   generic_ppav=a/'monodromy/generic_nonordinary_ppav_groups.tex'"
addition="""   for cp37_path in [a/'monodromy/prime5_exceptional_wall.tex',
                       a/'obstructions_crystals/A4_type_1_5_evaluation_fibres.tex',
                       w/'notes/primitive_elliptic_double_cover.tex']:
    assert cp37_path.exists() and '\\\\status{Candidate' not in cp37_path.read_text()
    out.write('\\n'+cp37_path.read_text()+'\\n')
"""
assert old.count(needle)==1
new=old.replace(needle,addition+needle)
needle="                    'B_first_wild_cyclotomic_different.tex']:"
assert new.count(needle)==1
new=new.replace(needle,"                    'B_first_wild_cyclotomic_different.tex',\n                    'B_valuation_one_irreducible.tex',\n                    'B_second_wild_trace_arc.tex']:")
p.write_text(new)
(prior/'consolidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='CP36',tofile='CP37')))
for name in ['prepare_checkpoint','render_qa','verify_program_paths']:
 src=w/f'code/{name}36.py';dst=w/f'code/{name}37.py';assert not dst.exists()
 text=src.read_text().replace('CP36','CP37').replace('checkpoint36','checkpoint37').replace('qa36','qa37').replace('current36','current37')
 dst.write_text(text)
src=(w/'code/finalize_checkpoint36.py').read_text()
text=src.replace('CP36','CP37').replace('checkpoint36','checkpoint37').replace('checkpoint_35','checkpoint_36').replace('checkpoint35','checkpoint36').replace('Checkpoint36','Checkpoint37').replace('qa36','qa37').replace('QA36','QA37').replace('current36','current37').replace("'checkpoint':36","'checkpoint':37")
text=text.replace('Checkpoint37 is archived only at or after05:50:40UTC on20November2026.','Checkpoint37 is archived only at or after06:35:40UTC on20November2026.')
text=text.replace('The next checkpoint37 is due06:35:40UTC and the next actual review26 is due06:50:40UTC.','The next checkpoint38 is due07:20:40UTC and the next actual review26 is due06:50:40UTC.')
text=text.replace("'; checkpoint37 is due06:35:40UTC and actual review26 is due06:50:40UTC '","'; checkpoint38 is due07:20:40UTC and actual review26 is due06:50:40UTC '")
text=text.replace("'on20November2026. Checkpoint37 and actual review25 are due05:50:40UTC.\\n\\n'+","'on20November2026. Checkpoint37 is due06:35:40UTC; actual review25 was completed earlier.\\n\\n'+")
(w/'code/finalize_checkpoint37.py').write_text(text)
text=(w/'code/archive_checkpoint36.py').read_text().replace('CP36','CP37').replace('checkpoint36','checkpoint37').replace('checkpoint_36','checkpoint_37')
text=text.replace('after05:50:40UTC','after06:35:40UTC')
text=text.replace("assert now>=datetime.datetime.fromisoformat('2026-11-20T05:50:40+00:00')","assert now>=datetime.datetime.fromisoformat('2026-11-20T06:35:40+00:00')")
text=text.replace("('checkpoint.py','36')","('checkpoint.py','37')").replace("('verify_checkpoint_archive.py','36')","('verify_checkpoint_archive.py','37')")
(w/'code/archive_checkpoint37.py').write_text(text)
# The earlier failed promotion controller is preserved exactly, with its actual output.
p=w/'code/promote_root_primitive_double_cover.py'
line="new=re.sub(r'\\\\status\\{Candidate[^}]*\\}',r'\\\\status{Proved under the stated hypotheses; independently audited.}',new)\n"
before=p.read_text();assert before.count(line)==1
(prior/'promote_root_primitive_double_cover_attempt01.py').write_text(before.replace(line,''))
(prior/'promote_root_primitive_double_cover_attempt01.stderr.txt').write_text('Traceback (most recent call last):\n  File "/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/code/promote_root_primitive_double_cover.py", line 43, in <module>\n    assert \'\\\\status{Candidate\' not in new\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nAssertionError\n')
(prior/'promote_root_primitive_double_cover_attempt01.stdout.txt').write_text('')
record={'status':'SETUP ONLY; NO FUTURE REVIEW OR ARCHIVE EXECUTED','actual_utc':stamp,'promoted_inputs':inputs,'new_labels':sum(len(re.findall(r'\\label\{', (w/p).read_text())) for p in inputs),'checkpoint_due':'2026-11-20T06:35:40+00:00','next_review_due':'2026-11-20T06:50:40+00:00','last_actual_review':'notes/progress_review_25.json','retained_failure':'Root promotion status assertion failed before any mutation; exact prior and stderr retained.'}
(w/'notes/checkpoint37_setup.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
