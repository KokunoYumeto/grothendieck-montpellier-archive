import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_149'
r=[
(r'\mspage{10}',r'\mspage{\hand{10}}'+'\n'+r'\margin{\unsure{$\diagdown$}}','The folio10 is handwritten. A long diagonal pen/pencil stroke crosses the full text; its textual status is unresolved, so the stroke is retained as an uncertain marginal mark with the existing extent note.'),
(r'\mspage{149}',r'\mspage{\hand{149}}','The lower149 is handwritten.'),
(r'\unsure{admirable|admitable}',r'admitable','The fifth consonant is a typed t with an upright and crossbar; the visible spelling admitable is retained.'),
(r'\inserted{a)}',r'\inserted[typed]{a)}','The inserted a) has the typewriter face and a pen placement bracket.'),
(r'\inserted{b)}',r'\inserted[typed]{b)}','The inserted b) is typed above the line.'),
(r'\inserted{sous-}',r'\inserted[typed]{sous-}','Sous- is typed interlinearly; its brace is handwritten.'),
(r'\inserted{sur A/I}',r'\inserted[typed]{sur A/I}','Sur A/I is typed above the baseline with a hand bracket.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The four long arrows are drawn by hand.'),
(r'\to ',r'\hand{\to} ','The augmentation arrow is handwritten.'),
(r'\longrightarrow} \underline{I}/\underline{I}^2 \]',r'\longrightarrow} \underline{I}/\underline{I}^2 \]\margin{\unsure{$\prime$}}','A short isolated vertical pen tick is visible to the right of this display; its meaning is unclear and it is retained as an uncertain mark.')]
d={8:'The printed word is admitable with a visible t, not a clear r; its source spelling is retained.',11:'The oblique pen slash separates qui and revient and is retained.',20:'The inserted a) is typed, with a pen bracket.',21:'The inserted b) is typed above the line.',23:'De type is a handwritten insertion, both words legible.',26:'Sous- is a typed insertion with a handwritten brace.',28:'The check over the parenthesized quotient is handwritten; a separate small pen tick at the right of the display is also retained as uncertain.',30:'The check over the parenthesized quotient is handwritten.',32:'Sur A/I is typed above the baseline, with a hand bracket.',33:'The inserted symbol has the pen-written phi oval and stem; the following l’homomorphisme correspondant is cancelled with typed x strokes.',34:'The final dual check is handwritten.'}
n=['The diagonal stroke crosses from Arrivé to the foot through the whole text. Its cancellation/use-mark function cannot be settled; a visible uncertain marginal sign and the descriptive source comment retain that ambiguity without silently deleting the page.','The letterform reads typed t; admitable is retained.','The short slash after qui is a pen-written separator.','All three dual checks are handwritten.','The inserted base symbol is phi, with a visible oval and stem.','The handwritten insertion reads de type.','The right edge clips non dégé; no unseen hyphen is supplied.','The full cancelled phrase l’homomorphisme correspondant is legible beneath its x strokes.','Both10 and149 are handwritten folios.','Both halves and every typed baseline, interlinear insertion, formula and marginal stroke were read.']
e=[dict(line=25,before=r'à un noyau engendré par $\theta^2$',image=r'à un noyau engendré par $\theta^2$',decision='preserved',reason='The scan visibly prints à and theta squared in this wording; neither the accent nor the object named after par is silently replaced.',category='source-wording')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
