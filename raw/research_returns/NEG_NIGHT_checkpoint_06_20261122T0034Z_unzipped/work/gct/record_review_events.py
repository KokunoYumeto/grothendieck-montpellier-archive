"""Record reviews actually performed, using the task clock supplied by caller."""
from pathlib import Path
import csv,sys
if len(sys.argv)!=2:raise SystemExit('Pass clock__curr_time output.')
now=sys.argv[1];rows=[]
def event(ids,typ,out,evidence):rows.append([ids,now,'GPT-6 Astra Pro (inherited)','not exposed by runtime','/root/gct',typ,out,evidence])
event('NN-S001–NN-S011','targeted proof check','Read all three root chapters and checked proofs and prose; no error found; subsequence indexing and phase wording clarifications sent.','work/gct/root_proof_review.md')
event('corpus03;corpus04','targeted proof check','Full reads completed; finite-prime boundary proof has multiplier/corner gap, recorded as NN-QG016. The boundary theorem itself is not refuted. Support linearization refined by NN-G005.','work/gct/notes.md; SOURCE_READS.tsv')
event('COUNTING-Thm4(c);COUNTING-Thm4(e)','refuted, with refined statement id','Rational-basis finite-Tate inference refuted by NN-G008. Completion convention and pole recovery corrected by NN-G006.','work/gct/chapter.tex NN-G006,NN-G008')
event('COUNTING-Thm5','used and rechecked in this run','Regular-matrix proof checked and refined to an additive tensor subcategory and split K0; no Karoubi/abelian/simple-unit inference.','work/gct/chapter.tex NN-G010')
event('P-F31;P-F56;P-F57;PLE-F5;PLE-F8','carried as background without fault found','Read stated source ranges and used as designated GCT inputs; no claim of a full independent re-proof of every input.','work/gct/SOURCE_READS.tsv')
event('GCT_PLETH-G036–G040','carried as background without fault found','Intake read in full; parameter-restricted positive-formula assertions retained at statement level only.','work/gct/notes.md')
event('SGA3-I4.7.2–3;EGAII2.4.7;EGAII2.5.2','used and rechecked in this run','Opened primary edition text and checked the exact comodule, grading, Veronese and associated-sheaf locators.','work/gct/notes.md; web source URLs')
event('ARCHIVE-cote2-scan17;ARCHIVE-cote43-scan37;ARCHIVE-cote133-scan19;ARCHIVE-cote133-scan28','used and rechecked in this run','Full supplied transcriptions read, including deletions/uncertainty marks. No manuscript-image verification or positivity implication claimed.','work/gct/source_inputs/RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/supplied_sources/')
event('NSRH-F03;NSRH-F04;NSRH-F17;NSRH-F50','used and rechecked in this run','Criterion hypotheses and Gaussian path-sign construction read; pointwise and dual bounds remain explicit requirements. F50 full proof read.','work/gct/SOURCE_READS.tsv')
with Path('work/gct/CHECK_EVENTS.tsv').open('a') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
print('Appended',len(rows),'actual review/background events')
