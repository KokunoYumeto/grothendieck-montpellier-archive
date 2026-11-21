#!/usr/bin/env python3
"""Create the root check records and root question rows for the final merge."""
import csv
from datetime import datetime, timezone
from pathlib import Path

base=Path(__file__).resolve().parents[1]
# The timestamp is the actual recorded check event. Recreating the table is
# not a new mathematical check and must not silently replace its date.
now='2026-11-21T03:33:45Z'
columns=['statement_id','date_utc','who','model','effort','run','type','method','outcome']
rows=[]
def event(sid,kind,method,outcome):
    rows.append(dict(zip(columns,[sid,now,'/root','GPT-6 Astra Pro','not exposed by runtime',
                                  'ZETA_NEXT',kind,method,outcome])))

proofs={
'NX01':'Entire proof: Stark zero window, quadratic descent, A nonvanishing, exact C4 extraction, class-number normalization and K=Q exception.',
'NX02':'Entire proof: discriminant of compositum of conjugates, m/n integral exponent, Aramata–Brauer zero transfer, interval direction and exceptional-zero alternative.',
'NX03':'Entire proof: Louboutin upper bound, roots-of-unity degree estimate, signature inequality and effective limiting error.',
'NX04':'Entire proof: Minkowski ideal norm, factorial bound, Euler-factor coefficient domination and induction on ideal count.',
'NC01':'Entire revised proof including quadratic strengthening: relative regulator cancellation, D_E/D_F inequality, log powers, epsilon absorption and discriminant cutoff.',
'NC02':'Entire proof: Stark Lemma9 for quotient, uniqueness of possible zero, Wei constants, both height normalizations, averaged Colmez isolation of a type.',
'NC03':'Entire proof: all ideal quotients over one K, automatic E-linearity, counting direction, explicit GR input, logarithm absorption, field of moduli.',
'NC04':'Entire proof: maximal order over same K, actual product and geometric simplicity, repeated components, bounded height of B, N*O subset R, all powers and orbit degree.',
'NX-L01':'Entire proof: gluing, all commuting Frobenius maps, flatness/finite type, point-count scissors, elliptic numerator, no cancellation, nonseparated scope.',
'NX-L02':'Entire final proof: strict-p completed colimit, perfectoid integral/plus hypotheses, principal-open gluing and valuation tilde-limit, noetherian constant model, Galois action, finite coefficients, Fitting and inverse-limit passage.',
'NX-L03':'Entire proof: Borger separated hypotheses and potential Tate representations, stable summand and inertia, semisimplicity, hereditary continuous Frobenius category, actual versus canonical local factors.',
'NX-L04':'Entire proof: mu_p power lifts, geometric point counts, two inertia orbits, correction 1-t, case p=2.',
'NX-L05':'Entire proof: integral blowup and flatness, two-component reduced special fibre, section and surjective H2 restriction, P1-bundle H3, generic vanishing and obstruction.',
'NX-L06':'Entire proof: global primitive Dirichlet factors, finite correction, local integer lines and global half-integer lines, meromorphic cancellation and A endpoints.',
'NX-L07':'Entire proof: integer-ring endomorphisms injective via norm/minimal polynomial, field automorphisms preserve integral closure, mod5 nilpotent Frobenius, residue-degree local factors.',
'NG01':'Entire proof: semisimple absolute-Hodge category, identity MT group, characteristic derived group, full-group stable projector, CM characterization/maximality and compatible factors; separate fixed-l qualification.',
'NG02':'Entire proof and refinements: normalization/completion scissors and signs, component action, Jacobian splitting, coefficient commutant, noncancellation; final nonseparated affine-stratum extension reread separately.',
'NG03':'Entire proof: symplectic primitive strings, absolute-Hodge projectors, all indices and signs, Tate shifts, Lie-invariant formula and representation-input limitation.',
'NG04':'Entire proof: maximal-torus zero weights and pair permutation signs, polarization invariant, primitive ranks and complete list.',
'NG05':'Entire proof: character coefficient difference, GL2 descent, derived invariants, all shifts and multiplicities, E^2 specialization and continuation source scope.',
'NG06':'Entire proof: rational extreme eigenspaces, determinant types, torus group, absolute-Hodge projector, finite conjugate sum and averaging/descent.',
'NG07':'Entire proof plus Zarhin exact source statement: absolute simplicity and non-CM, differential orders/eigenvalues, signature, normalized full endomorphism algebra and projector over Q, primitive contraction.',
}
for sid,method in proofs.items():
    role='Author whole-proof rereading' if sid.startswith('NX0') else 'Independent-reader whole-proof check'
    event(sid,'targeted proof check',role+'. '+method,
          'PASS: no mathematical gap found in the stated scope. Not a proof-assistant formalization or an independent re-proof of cited literature.')

sources={
'STARK-1974-LEMMA3':('Original facsimile printed pp139–140; visual reading of zero rectangle and real simple exception.','At most one zero in Re>=1-1/(4logD), |Im|<=1/(4logD), real and simple.'),
'STARK-1974-LEMMA4':('Original facsimile printed pp140–141, equation11 and C4=2C3; Garcia–Lee §3 pp16–17 cross-check.','Exact residue branch kappa>C4^-1(1-beta1) verified; no c8 branch used.'),
'STARK-1974-EQ7':('Original printed p139 equation7 and p141, with c1=0,c2=2/log3; numerical expression independently recomputed.','C4=2exp(21/8+(gamma+2log2)/(4log3)); rounded 173 denominator certified separately.'),
'STARK-1974-LEMMA7':('Original printed p143 visually read; applied to a<=n conjugates of K in normal closure.','D_L divides product D_Ki^(m/n_i); exponent am/n<=m<=n! verified.'),
'STARK-1974-LEMMA8':('Original printed p145: statement and complete descent proof read.','Requested locator verified. Constants 4 for normal, 4n! otherwise; real exceptional zero descends to quadratic subfield.'),
'STARK-1974-LEMMA9':('Original printed pp145–146: complete statement and proof read and quotient/imaginary-quadratic scope checked.','The zero belongs to zeta_E/zeta_F; threshold 1/(16g! logD_E) gives imaginary quadratic descent used in NC02.'),
'STARK-1974-THEOREM1PRIME':('Original printed p148 equations24–25 visually checked against requested locator.','Correct statement locator confirmed; used branch is effective zero-free branch, not tentative c8 evaluation.'),
'GARCIA-LEE-2020-EQ1-S3':('Primary arXiv2007.10313v4 equation1 p2, §3 pp16–17, local PDF text.','Analytic class-number normalization and C4 extraction match original Stark; separate c8 warning not imported.'),
'ARAMATA-BRAUER-AS-USED-BY-STARK':('Stark Lemma8 proof p145 names/uses entire quotient for normal closure over K.','Hypothesis L/K normal checked; quotient entireness used for zeros, not residue inequalities. No original Aramata/Brauer proof re-read.'),
'MILNE-ANT-4.3':('Official ANT.pdf version3.08, Theorem4.3 printed70/PDF72; exact Minkowski norm statement checked.','Matches NX04 input.'),
'LOUBOUTIN-2001-T1-E21':('Primary published paper Theorem1(1) p1195; equation21 p1200, including visually checked formula.','Upper residue and relative class-number normalization agree with NX03/NC01.'),
'WEI-2021-P5.3':('Primary v1 Proposition5.3 pp19–20 including proof estimate and displayed constants.','NC02 uses the averaged formula argument, no individual Colmez hypothesis.'),
'YUAN-ZHANG-2018-T1.1':('Primary pp534–535, normalization and theorem1.1.','Squared norm and averaged formula verified.'),
'GR-PERIODS-2014-T1.1-S2.3':('Primary theorem1.1 p345 and §2.3 pp351–352.','Universal lower height, normalization shift, product additivity checked.'),
'GR-POLARISATIONS-2014-T1.4':('Primary constants p2058 and statement p2060, including source image.','General-dimensional isogeny bound with alpha=1024g^3 and B=(14g)^(64g^2); not the elliptic-only CMH theorem.'),
'TSIMERMAN-2018-S2.2-L4.1':('Primary §2.2 p382 and full Lemma4.1 p384.','Ideal class and norm dictionary, and all-endomorphism/all-polarization definition field bound verified.'),
'REMOND-2017-T1.1-T1.2':('Primary author preprint opening convention and Theorems1.1–1.2 pp1–2; maximal-order and same-field scope checked.','Replacement and product decomposition support NC04 without conductor-dependent extension.'),
'BORGER-6.1-6.2':('Supplied lrfoe13.tex and primary §6 Theorem6.1/Corollary6.2 read with separatedness hypothesis.','Generic abelian Galois action and potential integral-Tate splitting verified in scope.'),
'SCHOLZE-2011-LOCAL-LIMIT-INPUTS':('Primary author text: Def5.1(ii),Thm5.2,Prop5.13(i),Rem5.14,Lem6.2,Thm7.12,Def7.14,Thm7.17,Cor7.18–19,Thm9.7; hypotheses compared with NX-L02.','Checked statements as used; no re-proof of foundational perfectoid theorems claimed. Independent detailed challenge also in cm/lambda_L2_review.md.'),
'HUBER-1994-REMARK4.6':('Primary Remark4.6(iv)(d), printed544; noetherian proper hypothesis checked.','NX-L02 descends constant model to Fp[[u]] before base change.'),
'DELIGNE-MILNE-6.5-6.23-6.25':('Official corrected tc2012.pdf: semisimplicity, descent sequence, full faithful Hodge realization.','Correct abelian-type absolute-Hodge scope; finite component group retained.'),
'COMMELIN-4.14-4.16':('Primary 2019 paper: Remark4.14, §4.16 and their CM characterization.','Identity motivic group and torus criterion support NG01; no MTC assumed.'),
'ZARHIN-1.1-1.3.1':('Primary arXiv math/0103203v2 PDFp2 opened in root: exact theorem and xn-x-1 example read.','Applies to p=3,n=5; End_geometric=Z[zeta3], simple dimension4.'),
}
for sid,(method,outcome) in sources.items():
    event(sid,'used and rechecked in this run',method,outcome)

carried={
'ALPOGE-A':('Supplied ALPOGE_Main.lean endpoints and ALPOGE_Statements.lean predicates read; Remark step20 p4 locator retained.','Theorem status accepted as explicitly instructed; no Lean rebuild, source-level proof recheck, or IA01 re-audit.'),
'ZETA_TWO-IA01-CONDITIONAL_AUDIT':('Prompt instruction and supplied predecessor/intake.','Accepted unchanged; audit deliberately not repeated.'),
'MASULLO-M-MDOC01':('ZETA_TWO MDOC01; draft §1.2 p12, intended empty Theorem13.3.1.2 p522, §14.1.2 p528.','Conditional all-unitary-Hecke claim only; documentary status carried, not promoted to proved numbered theorem.'),
'ANDERSON-1986-C5.7.2-R5.7.3':('ZETA_TWO CM01 and intake exact locator printed181/PDF30.','Same-weight Hecke factorization carried; no independent re-proof or original complete proof check in this run.'),
'ZETA_TWO-ZT01-ZT04-ZT05':('Supplied paper and intake: abelian transfer, actual finite factor, deleted-prime example.','Established statements retained and used, without repeating their proofs.'),
'ZETA_TWO-ZT06-ZT08-SV01-SV02':('Supplied paper/intake gap and determinant/extension distinctions.','Gap restricted exactly as intake; NG01 closes abelian-type splitting only.'),
'SA06-B4e-B4c':('INTAKE_RESEARCH_SA06_20261120 §1 rowsB4a–g and §4.1 final class-number paragraph.','Sufficient expression carried at supplied statement level; B4c remains refuted. No full SA06 proof claimed read.'),
'ARCHIVE-15-70':('ZETA_TWO intake §5.4, SA06 A8a.','Cote15 scan70 carried for A8a only; no new scan read or separate A8c locator.'),
'ARCHIVE-34-64-74':('ZETA_TWO AR01 and intake §1,§5.5.','Struck Remark1.17 and equation2.5.5 readings unchanged; no new scan inspection.'),
'ARCHIVE-60-3-5-7-9':('ZETA_TWO AR01/IMPLICATIONS §5; exact scans3,5,7(archivep6),9(archivep8).','Exterior/determinant/reciprocity and explicit Weil hypothesis carried, no new transcription.'),
'ARCHIVE-153-3':('DP_MULT archive reading and DP11 context: PDFscan3/archivep2.','Binomial-polynomial locator carried; not a bad-fibre theorem.'),
'DP_MULT-DP11':('Supplied DP_MULT and intake verdict table.','Identity-Adams binomial equivalence retained; not generalized to every lambda-ring.'),
}
for sid,(method,outcome) in carried.items():
    event(sid,'carried as background without fault found',method,outcome)

event('NX01-CONSTANT-CERTIFICATE','computation or formal certificate',
      'Ran audit/check_stark_constant.py: exact Fraction arithmetic bounds harmonic gamma, logarithmic tails, exponential Taylor tail.',
      'PASS: 4*C4<173 with rational acceptance comparisons. A numerical certificate, not a proof-assistant formalization.')
event('NG02-NONSEPARATED','targeted proof check',
      'Read entire final NG02.4 deduction: disjoint affine neighbourhoods of one-dimensional generic points; zero-dimensional finite complement; spread scissors; same function fields.',
      'PASS: all finite-type dimension<=1 Q-schemes covered by separated strata, without assuming compactification of a nonseparated curve.')
event('PAPER-SCOPE-AND-LOCATORS','targeted proof check',
      'Entire front/tail and IMPLICATIONS read against all findings and predecessor locator limits; incorporated independent scope review.',
      'PASS: separates proved statements, outside-scope amendments, abstract input-dependent computation, and conditional M conclusions.')

with (base/'audit/root_checks.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns,delimiter='\t');w.writeheader();w.writerows(rows)

qs=[
('Q1-NORMAL','PROMPT task1 first bullet; ZETA_TWO IA05; Stark Lemma8 p145 and Theorem1prime p148',
 'What explicit effective lower bound for h_K R_K follows for every normal field?',
 'proved','NX01: kappa>1/(173logD), class-number formula gives the displayed hR lower bound; Q handled separately.'),
('Q1-CLOSURE','PROMPT task1 first bullet; Stark Lemma7 p143 and Lemma8 p145',
 'How does the bound pass to arbitrary fixed-degree fields and CM fields?',
 'proved','NX02: zero transfer through the Galois closure yields kappa>1/(173 n! logD), with explicit CM hR specialization.'),
('Q1-BRAUER-SIEGEL','PROMPT main question; Louboutin Theorem1(1) p1195',
 'Can the Brauer-Siegel conclusion be made quantitatively effective?',
 'proved','NX03: exact two-sided error interval; normal n/logD->0 families and arbitrary fixed-degree families.'),
('Q1-STARK-CONSTANTS','PROMPT requested locators; Stark equations7,11,24–25',
 'Are the requested original locators and residue constant actually checked?',
 'proved','NX01 source extraction and exact rational certificate: C4=2exp(21/8+(gamma+2log2)/(4log3)); 4C4<173. No c8 branch used.'),
('Q1-SUFFICIENT-POWER','SA06 intake §4.1 B4e; ZETA_TWO IAQ008–012',
 'Does bounding the class-number contribution to the old sufficient power need a new RH lower bound?',
 'proved','NX04: unconditional h<=sqrtD(1+0.5logD)^(n-1), usable in the previously established finite expression. B4c stays refuted.'),
('Q1-AO-SCOPE','PROMPT orbit consequence; Tsimerman §6.3/6.5 and Binyamini §1.2/1.4',
 'Which part of the cited Andre-Oort proof is made effective by the new bounds?',
 'proved','NC03–NC04 make every arithmetic CM-orbit constant explicit. They do not supply algorithms for the separate counting/family steps as stated; effective modular-curve replacement cited.'),
]
with (base/'audit/root_questions.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['id','source_and_locator','question','state','finding_ids_or_current_gate']);w.writerows(qs)
print('Root records:',len(rows),'check events;',len(qs),'question rows; recorded',now)
