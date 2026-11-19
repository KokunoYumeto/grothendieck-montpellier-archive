"""Record actual additional displayed chunks and source passages, not search hits."""
import csv
from pathlib import Path
P=Path(__file__).resolve().parents[1]
reader='GPT-6 Astra Pro; effort not exposed; SA14-20261119; picard_lefschetz'
rows=[
('MPL_57_271-315_transcription.tex','Rereads1–158;159–424 (truncated display not counted as a fresh full reading);425–720;720–1011','Rechecked exact physical line locators, the definition of good, the relative-constants Zariski lemma, component corrections and question lists against the already complete first reading.'),
('MPL_57_271-315_notes.md','Rereads1–133;129–178','Compared henselian, quotient and early late-Picard notes with their actual passages.'),
('MPL_58_020-067_transcription.tex','Rereads114–151;674–689;1706–1753','Specialization hypotheses, local Hom wording, and the complete surviving Brauer/R_p printed fragment rechecked.'),
('MPL_58_020-067_notes.md','Reread421–520','Cone, parafactorial, normalization and external-project notes compared with their separate endpoints.'),
('MPL_57_271-315_doubts.md','Reread400–524','Late question-list uncertainty and prior-transcriber provenance rechecked; no scan inspected.'),
('MPL_58_020-067_doubts.md','Reread400–576','Graded signs, missing cone definitions and categorical ambiguity rechecked; no scan inspected.'),
('K58-02_transcription.tex (root-owned Codex source)','Displayed physical lines65–225, including scans13,15,17','Read for parent C652 comparison. Finite avoidance sets, cutting converse and induction direction match SGA2 XIII2.1; no parent file edited.'),
('Grothendieck1961EGAII','Text4.5.1–5;4.6.8–12;8.7.2–8.8.6; local extracted lines3600–3685,3920–3972,7715–8100; PDFphysical173/178 = printed176/181 images','Actual eventual very-ampleness and cone contraction/direct-image assumptions read. Visual8.7.5/8.8.6 corroboration; not a whole-book read.'),
('Grothendieck1962FGA236','§§1.1–1.12,2.1–2.10,3.1–3.10,4.1–4.2; PDFphysical3–4/15–16 = printed222–223/234–235 images','Read statement text and context; visual sigma/tau definitions and conjectural clauses checked. Primary-image inspection concerns the published paper, not manuscript scans.'),
('Grothendieck1962FGA236Complement','Entire pp303–307, especially statements(i)–(ix)','Read exact announced finiteness/numerical-equivalence statements and the nonreduced-example correction.'),
('Grothendieck1968SGA2','IX2.1–2.2;X2.3–2.6;XI2.1–2.2,3.4–3.5,3.13,3.18;XII§1,3.1–3.2,5.2–5.6;XIII2.1–2.6,3.1,§5','Actual formal comparison, Picard, parafactorial, existence, graded and connectedness statements read with hypotheses. No claim of re-proving every published theorem.'),
('Grothendieck1968SGA2','Additional displayed lines6784–6951 of reedition; XIII2.1 and following converse originalpp177–178/reedition139–140/PDF147–148','Read converse and its proof for root C652. Read2.2–2.6/3.1 context; ordinary/geometric-fibre qualification remains explicit.'),
('RaynaudKleiman1971SGA6XII','Primary scan printed595–598 = PDF598–601;1.1,1.2,1.3,1.4,1.5,1.6,1.7','All four images read. Generic relative quasi-affineness distinguished from affine pullback over a field. Title reread at PDF598.'),
('Kleiman1971SGA6XIII','Primary scan printed635–636,647–648,650–652 = PDF638–639,650–651,653–655;3.6,3.7,4.7,4.8,5.1–5.4','Seven images read for exact finite-type, tau, NS and Betti formulas. A frontmatter-only copy and unread OCR are not counted as theorem checks.'),
('Raynaud1974Lefschetz','I§0;I1.1,1.3,1.4,1.5,1.6','Read quotient-of-regular ambient condition, closures meeting/missing divisor and depth ranges.'),
('Artin1969Approximation','Theorems1.6,1.8,1.10;§3.8','Read finite-order approximation and algebraization context; not an exact Picard-group equality theorem.'),
('Elkik1973Henselian','III.1 Theorem3 pp569–573;Corollary1 p573;following lemma and unnumbered Picard corollary','Exact punctured Picard isomorphism read. Boutot attribution is a backward lead, not an opened earlier proof.'),
('Ferrand2003Pinching','2.2;Theorem5.4;6.2;6.3;7.1','Actual descent, pinching existence, nonprojective examples and affine-orbit criterion read.'),
('Traverso1970Seminormality','Theorem3.6 and its reduced/noetherian/finite-normalization hypotheses','Actual Picard homotopy-invariance theorem read; consequences in P17 separately labelled deductions.'),
('MaulikPoonen2012NS','Proposition3.6;Examples3.10–3.12, especially full Example3.12;arXiv version metadata','Read exact tame specialization statement and actual p-primary CM example. Earlier cited mechanisms were not all independently retrieved.'),
('Oda1969Dieudonne','Proposition4.9 p113;Corollaries5.11–5.12 p131;publication/receipt metadata','Read full p-torsion group-scheme and stable-subspace hypotheses.'),
('Suzuki2023FundamentalGroups','Introduction,Conjecture1.1 and Theorem1.2 p2;arXiv version history and publication metadata','Full pi1 conjecture separated from proved maximal pro-nilpotent quotient. Current bounded searches do not certify a2026 open status.'),
('Laudal1965Limits','§1.1;Corollary1.3.2;Roos entries in bibliography','Read exact diagram-category/spectral-sequence framework and backward bibliography. Original Roos articles not read.'),
('DemazureGrothendieck1970SGA3II','ExposéVIII Proposition7.2;ExposéX Remark8.7, originalpp120–122/reedition97–98','Read actual characteristic-zero monomorphism theorem and smooth-group rank semicontinuity statement; merely flat extension called probable. Editorial query is not proof.'),
('Kleiman2005Picard','§2;§3;4.8;4.9;4.18/4.18.5;5.4;5.6–5.7;6.16;6.18–6.20;6.28;Answers4.2–4.16 especially4.15','Read actual hypotheses and theorem statements. Additional reread of4.8 verifies the projective flat geometrically integral separatedness case.'),
('Brauer1951GroupRings','pp237–241 and247–250, especially§2.6 p241 and Theorem p250','Read character lattice, exact hyperelementary definition and Schur-index detection statement.'),
('Fontaine1971Decomposition','§6 Corollary1 p168;§7.2–§8.2 pp173–179, Theorems5/5prime and§8.2 Corollary1','Read the actual R_p definition and local-field consequences, not inferred from the detached manuscript proof.'),
('Stacks0312;Stacks0FCC;Stacks07QX','Tags0312,0FCC,07QX, displayed statements and proofs/context','Actual flat-associated-prime, depth-localization and henselian approximation results read.'),
('StacksAlgebra','Tags07P2,037P,05DW,030W,00FV;037P reread','Actual p-basis, relative-constant, separability and finite-type-field statements read.00FV deliberately rejected as a match for the different Zariski coefficient lemma.'),
('StacksDivisors','Tags0BE0,0EBK,0B8I,0BD6,0D2S,0B44','Actual divisor, invertible-module and proper-relative-ample statements/proofs read.0D2S/0B44 supply P32 hypotheses.'),
('PROMPT(20261119-130057).md;WORK_PROTOCOL.md','Entire prompt and25-line protocol reread during final audit','Schemas, six-stage completion requirements, provenance and check-event type rules confirmed.')
]
f=P/'read_log.tsv'
with f.open() as h:old=list(csv.DictReader(h,delimiter='\t'))
seen={(x['file'],x['actual_chunks_read']) for x in old}
for name,chunks,result in rows:
    if (name,chunks) not in seen:old.append(dict(date='2026-11-19',reader=reader,file=name,actual_chunks_read=chunks,result=result))
with f.open('w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=['date','reader','file','actual_chunks_read','result'],delimiter='\t');w.writeheader();w.writerows(old)
print('Actual reading records:',len(old))
