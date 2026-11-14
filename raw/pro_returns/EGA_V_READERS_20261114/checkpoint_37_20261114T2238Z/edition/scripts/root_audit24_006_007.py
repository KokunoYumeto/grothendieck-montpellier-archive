"""Record full visual comparison of cote24 sites6--7, including the drawn diagram."""
from pathlib import Path
import csv
from audit_record import source_path,save,aggregate
from root_review_support import ReviewedPage
ROOT=Path(__file__).resolve().parents[1]
notes={r['key']:r['notes'].split(' | ') for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(),delimiter='\t')}
for n in (6,7):
 key=f'ega24_24_{n:03}';p=ReviewedPage(source_path(key).read_text())
 if n==6:
  for before,after in [
   (r'S^1 = P^V \to S',r'S^1 = PV \to S'),
   (r'P^V{}_{S1}',r'P^V{}_{S}1'),
   (r'E^V{}_{S1}',r'E^V{}_{S}1'),
   (r'P_{S1} = P \times_S P^V',r'P_S 1 = P x_S PV'),
   (r'and $\underline{P}^V$ defined',r'and $\underline{P}V$ defined'),
   (r'over $P^V$,',r'over $PV$,'),
   (r'$P^V$ over S',r'$PV$ over S'),
   (r'S \xrightarrow{\xi} P^V',r'S \xrightarrow{\xi} PV'),
   (r'point of $P^V$',r'point of $PV$'),
   (r"S' \xrightarrow{\xi} \underline{P}^V",r"S' \xrightarrow{\xi} \underline{P}V")]:
   p.change(before,after,'The full scan and enlarged index crops were compared occurrence by occurrence: baseline capital V is retained where full-height; the visibly raised V in the diagonal-section expressions remains raised. In S1, S is lowered and the full-size1 returns to the main baseline.','notation-placement-corrected',count=1)
  p.change(r'\underset{S}{\times}',r'\underset{S}{x}','The pairing has a typed lowercase x for the product; the draft multiplication glyph is replaced by the visible letter.','letterform-corrected',count=1)
  p.change(r'X \underset{P}{\times}',r'X \underset{P}{X}','The last line has two full-height capital X forms, the second carrying P below; the typed product letter is retained.','letterform-corrected',count=1)
  p.change(r'f^{-1}',r'f{-1}','The -1 in the final line is full-size on the baseline, as the image shows.','notation-placement-corrected',count=1)
  p.change(r'H_\xi',r'H\xi','Every xi after H starts at the text cap level and uses its normal descender; no reduced or lowered index is visible.','notation-placement-corrected')
  p.change(r'\underline{Y}_\xi',r'\underline{Y}\xi','The final xi after the underlined Y is typed at full size on the body line.','notation-placement-corrected',count=1)
  p.change('% NOTE: a white box covers the end of this last typed line, after "to relate"; the rest of the line is hidden.',r'\illegible{?}'+'\n% NOTE: an opaque white rectangle follows "to relate"; any underlying text and its word count are unreadable.','The visible occluded area is given a linked unknown-extent mark, without restoring any words.','gap-marked',count=1)
  observations=[
   'The upper6 has a regular serif printed form; no pen addition is visible.',
   'A separate typed S stands below and a little to the right of the underlined H; the existing underset representation retains it.',
   'The two standalone S1 forms have a raised full-size1. They are numerals1, not primes. The1 after lowered S in PS1/EVS1 returns to the main line and is now encoded accordingly.',
   'The V placement varies: the two diagonal-section expressions have raised V, while the standalone PV forms use a full-height baseline capital V. Product characters x or X are retained as letters where the image shows them.',
   'The inclusion curve between Hxi and PS prime is thick, irregular pen; its subset reading is clear.',
   'Both xi labels over the arrows are regular typed Greek forms. They remain typed.',
   'The primes after lowered S are at the main character height, as encoded; they are not moved inside a newly invented index.',
   'The opaque rectangle after to relate is visible; no underlying letter or word count is recoverable.',
   'Only the short inclusion sign is handwritten in the body; there is no long handwritten passage.'
  ]
  p.note('7--30','Complete text and formulas','All words, parentheses, punctuation, S/1/prime forms, arrow labels and product letters were checked in both full images and the enlarged index/pairing crops.','confirmed','The opening NB continues the final NB at French site5; no omitted paragraph is inferred from the preceding English page break.','full-text')
  p.note('occluded last-line end','White box after to relate','French counterpart: cote25/site6, et notamment de mettre en relations le propriétés de X et des Yxi; the English sentence continues at cote24/site7.','cross-reference','The source passage locates the gap but supplies no conjectural words beneath the English rectangle.','cote24-crossreference')
  p.note('24','section of underlined P_S prime over S prime','Blass has P without the dual mark here; the corresponding checked French cote25/site6 has the dual mark over P.','comparison-recorded','The missing dual mark is recorded as an observed witness difference and is not supplied.','cote24-comparison')
 else:
  p.change(r"f_S{}'\,{}^{-1}",r"f_S{}'\,{-1}",'The first displayed -1 is typed at full size on the main baseline.','notation-placement-corrected',count=1)
  for before,after in [(r'$P^V$ and',r'$PV$ and'),(r'$P^V$, one',r'$PV$, one'),(r'$XP^V$',r'$XPV$')]:
   p.change(before,after,'The full-height capital V is on the main line in this occurrence; no raised mathematical dual is supplied.','notation-placement-corrected',count=1)
  p.change(r'\begin{tikzcd}',r'\begin{tikzcd}[arrows={blue}]','Every connector in the diagram has uneven pen strokes and handwritten arrowheads. The nodes are typed. Applying the established arrow-only pen color records this layer without coloring the typed nodes.','handwritten-layer-restored',count=1)
  p.change(r'\underline{P}^V',r'\underline{P}V','All four diagram P/V pairs have a full-size baseline V; the existing underline belongs to P.','notation-placement-corrected')
  for a,b in [(r'H_\xi',r'H\xi'),(r'Y_\xi',r'Y\xi'),(r'G_\xi',r'G\xi')]:
   p.change(a,b,'Each typed xi in the running text, displayed formulas and typed diagram nodes is full-size on the character line; its descender is retained without making a smaller subscript.','notation-placement-corrected')
  observations=[
   'The first x after the equality is lowercase, and the later X is uppercase. The large gap before Hxi remains. The full-size baseline -1 is now encoded literally.',
   'All four arrow positions remain blank: S prime to S, Hxi to P_S prime, P_S prime to P, and S prime to PV. No faint arrow or pen addition is visible.',
   'XPV is a continuous typed string with no product sign. V is a full-height baseline capital.',
   'All diagram connectors are handwritten. The two middle verticals, Hxi--H, and S--PV have no discernible arrowhead; all other heads and their directions agree with the retained diagram.',
   'The two-line penned note reads * ASK AG if Module always means coherent or quasi-coherent sheaf of modules. Module alone is underlined. It corresponds to the typed body asterisk.',
   'The bottom note is short, though spread over two lines; no additional long handwritten passage is present.'
  ]
  p.note('7--43','Complete prose, formulas, diagram and footnote','Both full halves were read, every diagram object and connector followed, every blank arrow position inspected, and both handwritten footnote lines transcribed literally.','confirmed','The enlarged first product confirms lower/uppercase letters and the baseline -1; no absent arrow is reconstructed.','full-text')
  for where,english,french in [
   ('12','change S prime [blank] S','cote25/site6, the final base-change arrow S prime to S'),
   ('13a','Hxi [blank] P_S prime','cote25/site7, first arrow in the opening composed morphism'),
   ('13b','P_S prime [blank] P','cote25/site7, second arrow in the opening composed morphism'),
   ('18','xi: S prime [blank] PV','cote25/site7, the general xi arrow before the displayed base-change equation')]:
   p.note(where,english,'The blank corresponds to '+french+'.','cross-reference','The checked French locates the unfilled English arrow position; the English blank is preserved.','cote24-crossreference')
  p.note('43','* ASK AG if Module always means coherent or quasi-coherent sheaf of modules.','French counterpart: cote25/site7, Enfin, si F est Module sur X.','cross-reference','The translator’s full handwritten question is kept and its source phrase identified without answering it.','cote24-crossreference')
  p.note('19--20','F...over XPV; G...over Y; G...over underlined H','French cote25/site7 has F sur X, Gxi sur Yxi, and underlined G over the doubtful underlined M|H. The English omits the xi indices in these prose names and prints XPV.','comparison-recorded','The exact English typing and the French doubt remain in their respective witnesses.','cote24-comparison')
 assert len(observations)==len(notes[key]),(key,len(observations),len(notes[key]))
 for i,(before,seen) in enumerate(zip(notes[key],observations),1):p.note(f'NOTES item{i}',before,seen,'checked','Each concern was examined during the full visual comparison.','NOTES')
 text,decisions=p.finish();save(key,text,decisions,0,'All lines in both full scan halves read against the transcription; index and product crops also inspected; site7 diagram and handwritten query read in full.')
print(aggregate())
