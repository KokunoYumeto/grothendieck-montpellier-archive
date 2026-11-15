import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT
key='ps_134-3_028';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
def e(a,b,r):edits.append([a,b,r])
# One formula occurrence per source line, recorded separately.
for no in [9,19,20,23,24,31,32,33,35,37,41,43,45]:
 a=s.splitlines()[no-1];b=a.replace(r'\to',r'\hand{\to}').replace(r'B^\wedge',r'B^{\hand{\wedge}}')
 e(a,b,'The formula arrows on this line are hand drawn; each hat over B is penned over the typed letter. Formula content and direction are unchanged.')
e(r'\[ M^{\hand{\sim}} = (M,T_B)^{\hand{\sim}} \to (\mathrm{Hot}) \quad , \]',r'\[ M^{\hand{\sim}} = (M^{\hand{\unsure{\sim}}},T_B)^{\hand{\sim}} \hand{\to} (\mathrm{Hot}) \quad , \]','The first display has a faint small wave above the inner M/comma, omitted from the supplied transcription; retain it with doubt because it may be an erased misplaced tilde. The arrow is clearly handwritten.')
e(r'\inserted{directly}',r'\inserted[typed]{directly}','Directly has typewriter letters above the line; the curved placement stroke is handwritten.')
conf=dict(key=key,edits=edits,diffs={
1907:['when observing that for any','The typed that is clearly present before for.'],
1908:['a category B into M','The typewritten preposition is into.'],
1914:['assumpti-on','The line ends assumpti- and the next begins on, followed by a comma; the noun is singular.'],
1916:[r'\inserted{gradually}','The interlinear gradually is small cursive handwriting with its own insertion stroke.'],
1917:[r'\margin{$\lrcorner\!\ulcorner$}\uline{indeed.}\hand{$\rfloor\!\lceil$}','The scan has a stepped double vertical paragraph sign after indeed and a matching mark in the margin; the visible instruction is preserved.'],
1919:['forget about fully','The scan contains no article between about and fully.'],
1922:[r'\inserted[typed]{directly}','Directly is typewritten, unlike gradually above.','correct provenance'],
1923:[r'a \hand{``}test category\hand{\'\'}'.replace("\\'","'"),'The opening and closing paired pen strokes are visible above the typed test category.'],
1925:[r'whi\hand{?}ch','A small penned query sits above the end of which; its body overlaps c/h without replacing the typed word.']},
unsure=[],illegible=[],notes=[
'The typed x after ries has a dark vertical pen stroke through it; the deletion is retained.',
'A faint additional wave above the inner M/comma is visible; it is now preserved as an uncertain handwritten tilde rather than silently omitted.',
'The mirrored stepped paragraph marks and the underline beneath indeed match the supplied symbolic rendering; the instruction is kept visible.',
'The slash after M extends toward the caret on the next line; both and the left-margin call27 are retained as visible note-placement marks.',
'The parenthesized call26 and comma are handwritten, with the 6 clearly closed; the source reading is retained.'],
evidence='Both halves inspected in full. Upper: that, into, and singular assumption are clear; the source spellings overenthousiastic and Tt remain. The x after categories is cancelled by pen. The first display has the already transcribed large tildes plus a faint extra wave over the inner M/comma, now kept with uncertainty. Formula arrows and hats are hand additions throughout; gradually is cursive. Lower: the mirrored stepped paragraph sign after indeed is visible, the is deleted before stacks, fully faithfullness has no inserted article, directly is typed interlinear, and possibly is typed over the cancelled probably. The query above which, paired quotation marks around test category, note26 and note27 with slash/caret placement marks are all retained. No reading is supplied for the faint wave beyond its visible tilde-like shape.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
