"""Write exact attached-file/line correction records from searchable anchors."""
from pathlib import Path
import csv
from time import perf_counter

start=perf_counter()
root=Path(__file__).resolve().parents[1]
workspace=root.parent
reading='inputs/RESEARCH_SA23_study/readings/C_22_23_26_161-5.md'
prompt='upload/PROMPT(20261120-001045).md'
packages='inputs/RESEARCH_SA23_study/RESEARCH_PACKAGES.md'
checks='inputs/RESEARCH_SA23_study/CHECK_EVENTS.tsv'
trans_c='inputs/RESEARCH_SA23_transcriptions/codex/K23-03_transcription.tex'
trans_g='inputs/RESEARCH_SA23_transcriptions/codex/K23-05_transcription.tex'
specs=[
 ('ALG-COR-01',prompt,'The counterexample to 0_IV 19.3.12',
  'The supplied results summary calls the nonlinear-compactness example a counterexample to 0_IV 19.3.12.',
  'It refutes the printed nonlinear compactness step. The proposition itself is true by the square-zero linear-compactness and closed-power proof.',
  'SA23-D-1--SA23-D-4','mathematical correction'),
 ('ALG-COR-02',reading,'**0_IV 19.3.12 "est canulé".**',
  'The reading reports the letter calling 19.3.12 canule and concluding there is no hope.',
  'The quotation accurately reports the objection, but cannot be used as a false-theorem verdict. Distinguish the invalid proof from the true lifting theorem.',
  'SA23-D-3--SA23-D-4','interpretive correction; quotation retained'),
 ('ALG-COR-03',checks,'Deligne\'s counterexample to the compactness needed',
  'The prior check certifies the polynomial compactness counterexample.',
  'That check remains valid; its scope is the proof step only. The implication that the stated lifting theorem is false is refuted.',
  'SA23-D-3--SA23-D-4','scope clarification'),
 ('ALG-COR-04',prompt,'- 0_IV 19.3.12, 19.5.5, 19.5.6',
  '19.5.5 and 19.5.6(ii) are grouped under 0_IV.',
  'The letter concerns IV 19.5.5 and IV 19.5.6(ii), printed pp.206--209. Actual 0_IV 19.5.5 is a remark and 19.5.6 is the proof of 19.5.3, printed p.94.',
  'SA23-D-5--SA23-D-6','locator correction'),
 ('ALG-COR-05',packages,'- **0_IV:** 19.3.12; 19.5.5',
  'RP3 groups the filtered and graded results under 0_IV.',
  'Read IV for 19.5.5 and 19.5.6(ii), as in ALG-COR-04.',
  'SA23-D-5--SA23-D-6','locator correction'),
 ('ALG-COR-06',reading,'- In the noetherian case the three variants',
  'The three notions of regularity are said to agree in the Noetherian case.',
  'For sequences require a Noetherian local ring, a finite nonzero module, and elements of the maximal ideal (or the appropriate Jacobson-radical version). Noetherianity alone does not suffice; a product-ring counterexample is given.',
  'SA23-C-6','missing hypotheses'),
 ('ALG-COR-07',reading,'the transitivities of 19.1.5',
  'Both additional transitivities are expected without Noetherian hypotheses.',
  'The split-conormal converse with I and J Koszul-regular is true. The other converse is false even for a local ring and split conormal sequence; the idealization example verifies every hypothesis.',
  'SA23-C-4--SA23-C-5','refuted expectation'),
 ('ALG-COR-08',reading,'**Link.** This is the origin',
  'The PS is identified as the origin of SGA6 VII Koszul-regular immersions.',
  'The mathematical identification is exact, and the proposed EGA IV19.1.8 appears in print. The PS describes ongoing seminar work and a prior Berthelot verification; a claim that the PS was the first invention is stronger than this witness. Causal adoption is not inferred merely from matching definitions.',
  'SA23-C-2--SA23-C-6;notes/algebra_SGA6_historical_gate.md','historical scope correction'),
 ('ALG-COR-09',reading,'- **③ P_B',
  'The Hilbert-series upper bound and converse from equality are stated without the surjectivity hypothesis.',
  'Require surjectivity of v, equivalently the kernel condition together with composite augmentation. Splitting alone does not imply the inequality, and equal Hilbert series alone does not imply v is an isomorphism; finite counterexamples are certified.',
  'SA23-G-3--SA23-G-4','mathematical correction'),
 ('ALG-COR-10',checks,'K23-05 (23:96-97)',
  'The earlier check declares both the kernel criterion and Hilbert-series assertion correct given composite augmentation.',
  'Composite augmentation repairs the kernel equivalence. The Hilbert assertion additionally needs surjectivity of v; the three finite G4 counterexamples distinguish the missing hypotheses.',
  'SA23-G-3--SA23-G-4','refined prior check'),
 ('ALG-COR-11',trans_g,'inverse à gauche',
  'u:C to B is called an inverse a gauche of the surjection phi:B to C.',
  'The intended section identity is phi composed with u equals id_C, so u is a right inverse of phi. A left inverse would instead satisfy u composed with phi equals id_B; combined with the stated surjectivity that would force phi to be an isomorphism. The original handwriting confirms the gauche wording.',
  'SA23-G-1','inverse-side correction; original physical96 inspected'),
 ('ALG-COR-12',reading,'- **His question.** Under the good conditions',
  'The first open implication is A flat over K implies C flat over B.',
  'This direction is false even under the very good conditions. The exact replacement is C flat over B iff A=K; the other two implications are true, with the equivalences in G1.',
  'SA23-G-1--SA23-G-2','settlement of the recorded question'),
 ('ALG-COR-13',reading,'- **Identification (my inference; locator unverified).**',
  'The minimal Cohen factorization comparison is an unverified inference.',
  'The identification is verified from the opened Nasseh--Sather-Wagstaff Definitions2.3,2.5 and Fact2.6(a); minimality gives exactly the degrees0,1 condition. AFH1994 itself remains explicitly marked not opened.',
  'SA23-B1-1','verified identification'),
 ('ALG-COR-14',trans_c,'$0$. Alors on prouve',
  'The transcription reads that the exterior complex is zero in degree0.',
  'Taken literally as H0=0 this requires the unit ideal; taken as a zero degree0 term it requires the zero ring. The positive-homology reading agrees with original EGAIV19.1.8 and SGA6VII1.1. Original physical53 has the same visible blank before0; a missing positive-degree sign is an editorial reconstruction, not recovered ink.',
  'SA23-C-1','original-source and mathematical correction'),
 ('ALG-COR-15',reading,'- At the re-edition, revise 0_IV 15:',
  'The PS forecasts replacing regular-sequence hypotheses throughout zero-IV section15 by Koszul-regularity.',
  'The unrestricted forecast is false in15.1.19: A=M=k[t], Fn=t^nM, f=(0,1-t) has separated prefix filtrations and contractible associated-graded Koszul complex, but H1=k. A finite-module variant has nonzero associated-graded H0; completeness gives a valid repair.',
  'SA23-C-9','refuted forecast with complete counterexamples and repair'),
]
rows=[]
for identifier,file,anchor,old,new,evidence,kind in specs:
    lines=(workspace/file).read_text().splitlines()
    matches=[i+1 for i,line in enumerate(lines) if anchor in line]
    if len(matches)!=1:
        raise ValueError((identifier,file,anchor,matches))
    rows.append([identifier,file,str(matches[0]),old,new,evidence,kind])
dest=root/'notes/algebra_corrections.tsv'
with dest.open('w',newline='') as stream:
    writer=csv.writer(stream,delimiter='\t')
    writer.writerow(['id','attached_file','line','prior_claim','correction','evidence','scope'])
    writer.writerows(rows)
print('Exact attached-file anchors verified:',len(rows))
print('Output:',dest)
print('Elapsed seconds:',round(perf_counter()-start,6))
