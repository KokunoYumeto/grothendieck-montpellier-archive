"""Save root's complete cote24 sites22--23 image comparison."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (22,23):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==22:
  p.change(r'\unsure{Ask}',r'\unsure{Ask|ADK}','The enlarged handwritten word has a closed middle loop and an angular final k/K. Ask remains plausible, but the ADK-like letterform already noted in NOTES is not securely excluded. Both candidates are retained.','doubt-expanded',count=1)
  observations=[
   'The v following each underlined P is a full-size main-baseline lowercase v; it is retained. Attached xi is lower than the standalone xi, despite its full-size type element.',
   'The bottom note and its star are handwritten. Enlarging it confirms the unresolved closed middle loop: Ask and the ADK-like form remain possible. The star follows Par.9 in the body.',
   'The page number22 is clear in a serif type distinct from the monospaced body; no pen correction is established.',
   'The sole handwritten note is short.'
  ]
  p.note('7--40','Complete constructibility discussion and marginal query','All words, Greek letters, cases, underline extents, punctuation and index positions were read against both complete image halves; the note was magnified.','confirmed','The extra xi before k algebraically closed, the missing article in spectrum of field k, and both leads or reduces remain literal.','full-text')
  p.note('11,40','Par.9.* and handwritten Ask/ADK A.G.','French counterpart: cote25/site18, en appliquant le par.9 in4.1.','cross-reference','The typescript query is preserved and linked to its French passage without supplying a reference.','cote24-crossreference')
  p.note('13--18','G; following sections','French cote25/site18 has a doubtful F/E at the finite-presentation hypothesis, then G_xi, and says dans les deux numeros suivants. Blass prints G and following sections without two.','comparison-recorded','The visible letter and wording differences are recorded without changing either text.','cote24-comparison')
  p.note('29--32','which for xi k algebraically closed; leads or reduces','French cote25/site18 has pour k algebriquement clos, with no xi there, and revient a envisager; Blass supplies two English alternatives in the running line.','comparison-recorded','The extra xi and both underlined alternatives are retained.','cote24-comparison')
 else:
  p.change(r'\unsure{O|0}','O','A same-scale enlarged comparison with the final bound on this very page shows a round, shorter O in characteristic O and a taller, narrower numeral0 in the bound. The visible letter O is retained literally.','resolved-from-image',count=1)
  observations=[
   'A paired enlargement shows the characteristic character to be the round letter O, visibly unlike the taller narrow0 at the foot. The transcription now gives O without mathematical normalization.',
   'The f(Z) bar is a straight even rule like the typed overlines elsewhere, and no separate pen stroke is visible; the unmarked overline is retained.',
   'The number23 is clear in a serif face distinct from the monospaced body; the scan does not establish stamping as its production method.',
   'No handwritten words, corrections or other pen additions were found in either complete half.',
   'No long handwritten passage occurs.'
  ]
  p.note('7--37','Proposition4.2, proof and Regret','Every list item, hypothesis, letter, symbol, heading, bar and punctuation was read against both full images.','confirmed','Cohen Macauley, correspsonding, F is satisfied at P and the literal O are kept. The ordinary G/F alternation and underlining are not normalized.','full-text')
  p.note('11--15','algebraic scheme; coprof; Cohen Macauley','French cote25/site19 has preschema, coppof and Cohen-Macaulay respectively.','comparison-recorded','The English words and spelling remain as typed.','cote24-comparison')
  p.note('24--27','F is satisfied at P; characteristic O; unramified','French cote25/site19 says F satisfasse a P, has numeral0, and replaces immersion by an unresolved handwritten un ramifie/non ramifie. Blass prints the reversed English wording, letter O, and unramified.','comparison-recorded','The English does not settle the French uncertain hand, and no mathematical repair is introduced.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','This listed issue was individually examined in the complete scan comparison.','NOTES')
 text,ds=p.finish();save(key,text,ds,0,'Both complete scan halves read line by line; site22 query and site23 O/0 pair additionally magnified.')
print(aggregate())
