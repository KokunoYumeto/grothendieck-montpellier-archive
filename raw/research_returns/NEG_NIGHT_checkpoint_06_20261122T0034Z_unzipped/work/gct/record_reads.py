from pathlib import Path
import csv,hashlib,shutil
R=Path('work/gct');S=Path('sources')
records=[]
def add(file,coverage,scope):
    p=S/file
    if not p.exists():
        records.append([file,coverage,scope,'MISSING_LOCATOR','']);return
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    records.append([file,coverage,scope,h,str(len(p.read_text(errors='replace').splitlines()))])
    dst=R/'source_inputs'/file;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst)
full=['OURS_split_zero_corpus/03_split_zero_defect_preprint.tex','OURS_split_zero_corpus/04_primitive_support_defects_preprint.tex','OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md','OURS_E4_RANK_FOUR_20261121.md','OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md','OURS_CONSULT_a0805369_GCT_SUPPORT.md','OURS_CONSULT_a8d75352_NSRH_WEIL.md','OURS_INTAKE_ALPOGE_GCT_20261121_part4.md','OURS_INTAKE_GCT_PLETH_20261121_part4.md','RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/positivity_ph3.tex','RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/positivity_actual_plethysm.tex','RETURN_GCT_NSRH_checkpoint_09_20261121T0545Z/finding_F50.tex','LIT_Fischer_Ikenmeyer_plethysm_complexity/sections/results.tex','OURS_E4_scripts/e4lib.py','OURS_E4_scripts/gram_signpoint.py','OURS_E4_scripts/cell_c3_check.py','OURS_E4_scripts/hexagon.py','OURS_E4_scripts/e3_fast.py']
for file in full:add(file,'entire file','read in full; not by itself a proof certification')
for file in ['consult_a157422a_counting_checks.py','consult_a157422a_dimension_ring_search.py','consult_a157422a_dimension_ring_verify.py','consult_a157422a_dimension_ring_unimodal.py','dimension_ring_minimal_pairs.py','dimension_ring_minimal_pairs.out']:
    add('OURS_counting_scripts/'+file,'entire file','read supplied implementation/output; reused functions only where labelled')
partial=[('LIT_Mulmuley_GCT_VI_flip_via_positivity/main.tex','750–865; 1160–1600','definitions and hypotheses'),('LIT_Ikenmeyer_Mulmuley_Walter_Kronecker_vanishing/main.tex','240–390','result statements and support context'),('LIT_Burgisser_Ikenmeyer_Panova_no_occurrence/main.tex','255–405','result statement and orbit-closure definitions'),('RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/positivity_actual_cubic_pole.tex','1–200','P-F31 theorem/proof and consequences'),('RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/positivity_paired_wave.tex','1–130; 260–365; 430–460; 560–660','P-F56 statement and exact bounds m,o,t; contraction-gate context'),('RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/positivity_dyadic_dominance.tex','1–175','P-F57 theorem and near-increment proof; theorem otherwise accepted as designated input'),('RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/work/plethysm.tex','1–80; 410–570; 715–770','lambda dictionary, D5 model, archive locator inventory'),('RETURN_GCT_NSRH_checkpoint_09_20261121T0545Z/GCT_NSRH.tex','170–332','F01–F04 and F17 criteria'),('OURS_E4_scripts/e3_constants.json','all 132 entries parsed exactly','computational source read; domination/parity comparison'),('OURS_E4_scripts/e3_reproduce.py','prefix ending at w0=max','used by exact supplied tensor-Hecke arithmetic')]
for x in partial:add(*x)
for file in ['ARCHIVE_2_scan017.tex','ARCHIVE_43_scan037.tex','ARCHIVE_133_scan019.tex','ARCHIVE_133_scan028.tex']:
    add('RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/supplied_sources/'+file,'entire supplied transcription','read complete transcription, not manuscript image')
with (R/'SOURCE_READS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['file','coverage','scope','sha256','file_lines']);w.writerows(records)
print('Recorded',len(records),'source readings; missing locators:',[r[0] for r in records if r[3]=='MISSING_LOCATOR'])
