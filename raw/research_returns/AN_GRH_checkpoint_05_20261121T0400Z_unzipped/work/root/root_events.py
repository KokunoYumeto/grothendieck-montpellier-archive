import json
from pathlib import Path
out=Path('/workspace/scratch/63b175cc138c/final/evidence/root_check_events.json')
e=[]
who='GPT-6 Astra Pro; effort not exposed; AN_GRH /root'
def ev(s,t,o,p):e.append(dict(statement_id=s,date='2026-11-21',who_model_effort_run=who,type=t,outcome=o,evidence=p))
proof='targeted proof check'
used='used and rechecked in this run'
comp='computation or formal certificate'
bg='carried as background without fault found'
for s in ['S01','S02']:
 ev(s,proof,'Whole written source-status/scope argument read; PASS within explicitly stipulated A and conditional M conventions. Primitive Dirichlet factors retained.','proof_sources/premises_section.tex')
ev('MASULLO:13.3.1.2',used,'Extracted and rendered supplied PDF page522; heading has no theorem statement. Chapter14 begins nextpage. No whole-draft proof review claimed.','Supplied MasulloPDF,p522; S01')
ev('MASULLO:§1.2',bg,'All-field Hecke-GRH scope used only as the draft claim M; not certified as proved.','Supplied Masullo draft§1.2; incomplete13.3.1.2')
ev('ALPOGE:Main/Statements',used,'All supplied declaration names and critical-strip definitions inspected. The theorem is accepted per user instruction. No Lean build or175187-file rescan performed.','source/ALPOGE_Main.lean; source/ALPOGE_Statements.lean')
for s in ['A01','A02','A03','A04','A05']:
 ev(s,proof,'Whole reconstructed proof read; PASS with exact hypotheses. A02 is a conditional application of a cited analytic theorem, not a reproof of its sieve. A05 retains full arithmetic quotient.','proof_sources/a1_section.tex')
ev('A06',proof,'Whole new proof read, including curve geometry, scalarFrobenius, theta identification, two-representation bound and six-prime obstruction; PASS. Positive-rank restricted scope remains open.','proof_sources/b23_section.tex')
ev('A06',comp,'Ran newly written standard-library certificate: exactly sixprimecandidates and their exactorders; only419 primitive; allthree displayed differences equal2; PASS.','certificates/A06/check_theta_obstruction.py; check_theta_obstruction.out')
ev('ANABELIAN_A1:B.23',proof,'Read entire recovered proof, including all conductor and Bezout implications. No mathematical gap found. Source theorem is stronger than A06.','recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex:B.23')
ev('B23-GEOMETRY',comp,'New independent exact implementation ran successfully: Rabin irreducibility, elliptic-map polynomial identity, birational coordinate, nonzero quintic coefficient, reduced rational-coordinate denominator=psi_n² at191 and229.','certificates/A06/check_b23_geometry.py; check_b23_geometry.out')
for s in ['G01','G02','G03','G04','G05']:
 ev(s,proof,'Entire final statement and proof read; PASS. G02 uses a commutative finite ring. G03 concludes semisimplification and uses the representation algebra lattice. G05 includes exact order-discriminant and nonempty-class checks.','proof_sources/effective_galois.tex')
ev('G-ARBITRARY-BASE',proof,'Whole normal-closure/degree-one-prime argument read; PASS. It does not bound Hilbert-specialization height or quotientdepth.','proof_sources/effective_galois.tex:Arbitrary number-field bases')
for s in ['T01','T02','T03','T04','T05','T06']:
 ev(s,proof,'Entire final statement/proof read; PASS for the stated source scope. T04 carries the explicitly identified E.1 primitivity input; T02 does not independently prove E.58. Direct certificates do not claim an exhaustive missing GT register.','proof_sources/GT_section.tex')
for s in ['R01','R02','R03']:
 ev(s,proof,'Whole source-scope assertion and appended proof read; PASS. Lang-quotient data and geometric nontriviality are explicit; availability is not all-proof correctness.','proof_sources/row_audit.tex; reproduce/assemble_paper.py')
ev('HOoley:1967',used,'Required Kummer Dedekind family checked against primary Russiantranslation§7 and modern Fan–PollackTheorem1.1; originalEnglish publisherPDF unavailable. Analytic proof not independently redone.','Hooley1967§7; Matematika12:1(1968),p47; FanPollack2025Thm1.1')
ev('FanPollack:Thm1.1',used,'Primary author/arXiv theorem inspected for fixedbase2 asymptotic and error. Used as cited theorem under its exact GRH family.','https://arxiv.org/abs/2505.05601v2')
ev('Goldfeld:1968-Theorem',used,'Primary fourpage paper inspected: theorem averages integerbasea; not a theorem for fixedbase2 on curve-selectedprimes.','Goldfeld1968,p223; https://www.math.columbia.edu/~goldfeld/ArtinsConjecture.pdf')
ev('Lenstra:1977-Thm3.1,4.1,4.2',used,'Primary text inspected for fixed finite Frobenius constraint and separate positive-density conditions; does not encode the unprovided theta-support condition.','https://www.numdam.org/item/SDPP_1976-1977__18_1_A11_0.pdf')
ev('PopSaidi:2003-Cor2.3,Prop2.4',used,'Read statements and relevant proof: pairwise prime orders means pairwise coprime orders in the construction, not prime integer orders. Cover changes genus and does not give A03 incidence.','https://library.slmath.org/books/Book41/files/pop.pdf')
ev('Saidi:2005-Prop2.2,Thm2.3',used,'Primary text inspected: theta-avoidance/new-ordinary criteria and upper bounds for nonordinary covers do not give universal nonordinary or primitive-zero existence.','https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/manuscripta.pdf')
ev('ST2009:§1',used,'Primary published version read at Definitions1.3,1.5,1.10, Remark1.2, Lemma1.7 and Proposition1.8(vi); checked uniform finite exceptional support and actual normalizer hypotheses.','https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/publRIMS.pdf')
ev('Conrad:Thm2.1',used,'Primary theorem and hypotheses inspected: finitely generated regular extension, perfect algebraically closed constantfield inK; Lang–Neron input matches A05.','https://math.stanford.edu/~conrad/papers/Kktrace.pdf')
ev('WeilI:1.5.1,1.6',used,'Primary trace formula and purity locators read; used for finite-field curveH1 and pointcounts, not analyticGRH.','https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf')
ev('MilneLEC:7.9,14.2,14.9,14.10',used,'Primary Kummer/Artin–Schreier, curvecohomology and cover-tower spectralsequence formulations inspected; flat versus etale characteristicp distinction retained.','https://www.jmilne.org/math/CourseNotes/LEC.pdf')
for loc in ['IX.4.10','IX.6.1','IX.6.4','X.3.8','X.3.9','XIII.2.12']:
 ev('SGA1:'+loc,used,'Primary recomposed SGA1 locator checked against the actual use. No stronger completion, ramification or base-change scope asserted.','https://arxiv.org/pdf/math/0206203')
ev('G-CHEB',used,'Primary theorem5.1,p1729 and specified analytic scope inspected; exactconstants4,2.5,5 and degree-one condition retained; noArtinholomorphy.','BachSorenson1996Theorem5.1; §2lastparagraphp1720')
ev('G-MW1,G-MW2',used,'Primary Theorems1/2 and analytic input inspected; exactconstants964,5760 and482,2880; non-CM Q-scope retained.','https://doi.org/10.1112/blms.13002')
ev('CLASSICAL-BACKGROUND',bg,'Riemann–Roch, Hilbert90, finite-field Kummer theory, characteristiczero Brauer–Nesbitt and Mordell–Weil used as classical background; no new proof of these general theorems claimed. Specialized deductions are proved in A01/A05/G03.','AN_GRH.tex proofs; source-specific cited background')
ev('TRANSCRIPTION',proof,'All six supplied transcriptions read for the proposed corrections. Mathematical typing/convention issues separated from authorial lapse; no handwritten scan was available.','TRANSCRIPTION_NOTES.tsv; source/ARCHIVE_149_scan033.tex–scan038.tex')
ev('SOURCE-RECOVERY-PC',used,'Attempted exact prior-work recovery query after loading PersonalContext instructions. Tool returned Personal context is disabled. Recorded as blocked, not zero results.','LEDGER.md; evidence/ROW_AUDIT_NOTES.md')
ev('TEX-BUILD',comp,'LuaLaTeX could not find lualatex.fmt; Tectonic bundle fetch returnedHTTP403. NoPDFcompilation or visualQA claim.','evidence/build/latex_pass1.log; README.md')
out.write_text(json.dumps(e,indent=2,ensure_ascii=False)+'\n')
print(len(e),'root check events')
