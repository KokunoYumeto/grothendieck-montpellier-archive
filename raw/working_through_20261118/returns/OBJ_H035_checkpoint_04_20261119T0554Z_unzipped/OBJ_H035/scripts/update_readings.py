"""Record visual decisions made by the model; this does not recognize text."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
path = root / 'READINGS.tsv'
with path.open() as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['scan'] == '020':
        row.update(reading='R inserted; Tor(F); first graded coefficient uncertain',
            what_the_mathematics_expects='Tor(R), and flatness of gr_J(R) as well as gr_J(A)',
            scan_shows='94_020_R_F_gr.jpg: inserted R and displayed F are clear; the overworked first graded symbol is not securely distinguishable as O_X or a coefficient letter',
            decision='Withdraw the earlier overconfident gr O_X reading; retain the definite R/F mismatch and leave the graded symbol unresolved',
            confidence='high for R/F; low for the graded symbol')
extra = [
 ('002','8–15','Omega with raised 1 and an uncertain following mark','The conormal module I/I^2 in the affine augmented-algebra realization','94_002_cover_invariants.jpg shows Omega^1 followed by an unidentifiable parenthesized-looking mark; no definition','Do not identify the last mark or attribute the conormal construction to the cover','high for Omega^1; low for following mark'),
 ('003','8–13','faithfully flat B; left exact F in the representability equivalence','Descent requires the left exactness clause','94_003_lemma1.jpg and full page show the faithful-flat qualification and equivalence arrangement','Retain the clause; do not assert descent of an arbitrary set functor from its restriction alone','high'),
 ('005','7–8','un f ... tels que (contracted handwriting)','Singular tel que','94_005_singular_f_agreement.jpg shows singular un f and a contracted ending compatible with the transcribed tels','Agreement correction is editorial; no mathematical quantifier changes','high for agreement; medium for expanded spelling'),
 ('005','18–20','F(M) finite over Ahat; it suffices when M is finite over A','Finite original-ring test modules are sufficient','94_005_prop4_finite_values.jpg clearly includes the parenthetical sufficiency qualification','Retain the weaker sufficient finiteness assumption; do not require finiteness for every formal module','high'),
 ('006','22','exists f ... tels que (contracted handwriting)','Singular tel que','94_006_singular_f_agreement.jpg has a singular quantified element and the same contracted form as scan 5','Editorial agreement correction only; missing nonzero condition is a separate row','high for agreement; medium for expanded spelling'),
 ('007','21','mark after est representable','No mathematical expectation can identify punctuation','94_007_question_mark.jpg shows a marginal mark next to reworking, not an unambiguous question mark','Do not count this as a securely written conjecture','low'),
 ('008','6–7m','normal locus of each integral quotient contains a dense open','Normality does not supply the missing finite-value condition','Full scan 8 shows the interlinear normal-locus qualification','Retain qualification; the Z counterexample meets it','high'),
 ('008','11','constant et egale / egal','Masculine egal agrees with rang','94_008_egal_egale.jpg has a terminal curl; egale remains plausible, egal cannot be excluded','Retain doubtful reading; do not certify a grammatical slip from mathematics','low'),
 ('010','2','last parameter index s / n','The same final index as the parameter sequence on the left','94_010_parameter_index.jpg shows a tight loop more compatible with s than the broad n on the left','Retain s-first uncertainty; reconstruction uses the same parameter list explicitly','medium for s-first; no secure resolution'),
 ('011','18','de between U and X, possibly cancelled','An inclusion U in X or the ordinary phrase U de X','94_011_de_cancellation.jpg shows de with a dark horizontal baseline stroke; cancellation cannot be certified independently of the transcription','Retain cancellation uncertainty; do not count a secure omitted-preposition error','low'),
 ('012','5–8','f(x)=0 implies x=0','Both directions, or separately f(0)=0','94_012_abs_definition.jpg shows the one-way implication; no separate f(0)=0 at this locus','Retain literal axioms and exhibit constant-one counterexample','high'),
 ('012','21–23','tout element n.1 est une racine de unite','Every nonzero element of the prime field','94_012_root_unity_exponent.jpg shows no nonzero qualifier','Keep wording; n=p refutes supporting sentence; corrected corollary proved','high'),
 ('012','24–25','real power','Strictly positive real exponent','94_012_root_unity_exponent.jpg gives real power without a positivity restriction','Add positivity only in the corrected definition, not the reading','high'),
 ('012','26–30','absolute values on Q; proof stops at On en deduit','Trivial class plus p-adic and archimedean classes','Full typescript shows no visible nontriviality restriction and ends mid-proof','Include trivial class in corrected theorem; completed proof is ours; authorship of inserted leaf unestablished','high for text; authorship unknown'),
 ('013','16m','a expliciter dune autre facon','An editorial request for another formulation','94_013_expliciter_margin.jpg reads the phrase beside condition a) of the cancelled corollary','Record explicit reformulation request, not a mathematical conjecture','high'),
 ('024','15–16','Murre, th. 3','Closed-subscheme representability for the condition Y_T=X_T','94_024_Murre.jpg clearly names Murre and theorem 3','Matched to Bourbaki exposition 294, Theorem 3, printed p.255; retain the proper/noetherian contextual hypotheses','high'),
]
for scan,line,reading,expected,shows,decision,confidence in extra:
    rows.append(dict(zip(fields,['94',scan,line,reading,expected,shows,decision,confidence])))
rows.sort(key=lambda row:(int(row['scan']),row['line']))
with path.open('w') as stream:
    writer=csv.DictWriter(stream,fields,delimiter='\t')
    writer.writeheader();writer.writerows(rows)
print('Recorded',len(rows),'reading rows; original transcriptions unchanged.')
