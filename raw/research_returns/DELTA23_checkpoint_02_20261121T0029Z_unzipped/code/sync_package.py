"""Stage the current research documents. This does not create/save a checkpoint."""
from pathlib import Path
import shutil, csv, json, hashlib

root=Path(__file__).resolve().parents[2]
work=root/'work'; out=work/'package'
for name in ('proofs','agents','records','code','notes'):
    (out/name).mkdir(parents=True,exist_ok=True)
sources={
 'local_symbols.tex':work/'notes/local_symbols.tex',
 'kubota_test.tex':work/'notes/kubota_test.tex',
 'second_quaternion.tex':work/'notes/second_quaternion.tex',
 'prime_three_symbols.tex':work/'notes/prime_three_symbols.tex',
 'transvection_rigidity.tex':work/'notes/transvection_rigidity.tex',
 'order_five_frame.tex':work/'agents/five_level_six/order_five_frame.tex',
 'order_five_arithmetic.tex':work/'agents/five_level_six/order_five_arithmetic.tex',
 'order_five_comparison_draft.tex':work/'agents/five_level_six/order_five_comparison_draft.tex',
 'level_six.tex':work/'agents/five_level_six/level_six.tex',
 'symplectic_collapse.tex':work/'agents/five_level_six/symplectic_collapse.tex',
 'descendant_characters.tex':work/'agents/characters/proofs/descendant_characters.tex',
 'adelic_frames.tex':work/'agents/characters/proofs/adelic_frames_draft.tex',
 'four_point_central_flips.tex':work/'agents/pentagon/four_point_central_flips.tex',
 'affine_cubic_detector.tex':work/'agents/pentagon/affine_cubic_detector.tex',
 'twisted_affine_obstruction.tex':work/'agents/pentagon/twisted_affine_obstruction.tex',
 'krammer_cubic_extension.tex':work/'agents/pentagon/krammer_cubic_extension.tex',
 'krammer_quotient_extension.tex':work/'agents/five_level_six/krammer_quotient_extension.tex',
 'krammer_mixed_correlation.tex':work/'agents/characters/proofs/krammer_mixed_correlation.tex',
 'krammer_pentagon_count.tex':work/'agents/pentagon/krammer_pentagon_count.tex',
 'krammer_three_pair_commonword.tex':work/'agents/pentagon/krammer_three_pair_commonword.tex',
 'krammer_all_five_commonword.tex':work/'agents/pentagon/krammer_all_five_commonword.tex',
 'cubic_detector_216.tex':work/'agents/pentagon/cubic_detector_216.tex',
 'krammer_s4_obstruction.tex':work/'agents/five_level_six/krammer_s4_obstruction.tex',
 'krammer_solvable_correlation.tex':work/'agents/five_level_six/krammer_solvable_correlation.tex',
 'krammer_induced_frame_ambiguity.tex':work/'agents/five_level_six/krammer_induced_frame_ambiguity.tex',
 'krammer_s3_obstruction.tex':work/'agents/five_level_six/krammer_s3_obstruction.tex',
 'level_six_congruence.tex':work/'agents/five_level_six/level_six_congruence.tex',
 'krammer_harmonic_cover.tex':work/'agents/five_level_six/krammer_harmonic_cover.tex',
 'cyclic12_cover.tex':work/'agents/five_level_six/cyclic12_cover.tex',
 'induced_s4_and_relative_homology.tex':work/'agents/characters/proofs/induced_s4_and_relative_homology.tex',
 'cubic_dessin_rational_quotient.tex':work/'agents/characters/proofs/cubic_dessin_rational_quotient.tex',
 'distribution_no_go.tex':work/'notes/distribution_no_go.tex',
 'cubic_descent.tex':work/'agents/five_level_six/cubic_descent.tex',
 'hurwitz_finite_escape.tex':work/'agents/pentagon/hurwitz_finite_escape.tex',
 'krammer_nielsen_perfect.tex':work/'agents/characters/proofs/krammer_nielsen_perfect.tex',
 'cubic_descent_harmonic.tex':work/'agents/pentagon/cubic_descent_harmonic.tex',
 'cubic_descent_full.tex':work/'agents/five_level_six/cubic_descent_full.tex',
}
for name,path in sources.items():
    if path.exists(): shutil.copy2(path,out/'proofs'/name)
for name in ('agents','records','code','notes'):
    for path in (work/name).rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts: continue
        if path.suffix in ('.pyc','.zip'): continue
        dest=out/name/path.relative_to(work/name)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,dest)
shutil.copy2(work/'RUN_START.txt',out/'RUN_START.txt')
events=[]
for path in [work/'records/root_check_events.tsv',*sorted((work/'agents').glob('*/CHECK_EVENTS.tsv'))]:
    if not path.exists(): continue
    with path.open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            events.append({
              'statement_id':row.get('statement_id',''),
              'date':row.get('date',row.get('date_utc','')),
              'who_model_effort_run':row.get('who_model_effort_run',row.get('who','')),
              'type':row.get('type',''),
              'outcome':row.get('outcome',''),
              'locator_or_method':row.get('locator_or_method',row.get('locator',''))})
keys=['statement_id','date','who_model_effort_run','type','outcome','locator_or_method']
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=keys,delimiter='\t');writer.writeheader();writer.writerows(events)
manifest=[]
for path in sorted(out.rglob('*')):
    if path.is_file() and path.name!='PACKAGE_MANIFEST.json':
        manifest.append({'path':str(path.relative_to(out)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(out/'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Staged {len(manifest)} files and {len(events)} check events; no checkpoint saved.')
