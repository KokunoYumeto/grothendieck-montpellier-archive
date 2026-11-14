import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT,occurrences
key='ps_134-3_033';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure');edits=[]
def e(a,b,r):edits.append([a,b,r])
e(u[0][0],'e','The enlarged overstrike has the crossbar and open counter of e; the live word is feel.')
e(r'\margin{$\uparrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw[->] (1.7,0)--(.2,0) .. controls (0,0) and (0,.2) .. (0,.5)--(0,2.1);\end{tikzpicture}}}','The upper margin mark is an upward arrow with a bent lower arm running beneath ving., not an isolated vertical arrow.')
e(r'\margin{$\downarrow$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw[->] (1.7,0)--(.2,0) .. controls (0,0) and (0,-.2) .. (0,-.5)--(0,-2.8);\end{tikzpicture}}}','The second margin mark begins with a horizontal arm above section29 and descends to the displayed functor; reconstruct its bent-arrow shape.')
e(r'\margin{$\|$}',r'\margin{\diagram{\begin{tikzpicture}[x=1em,y=1em]\draw (0,0)--(0,-3.7);\draw (.17,0)--(.17,-3.7);\end{tikzpicture}}}','The margin has two long parallel pen lines spanning the underlined basic-modelizer passage.')
for no in [9,16,17,18,22,24,41,44]:
 a=s.splitlines()[no-1]
 # Already-edited margin is excluded from this separate formula replacement.
 if no==16:a=a[a.index('(**)'):]
 b=a.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}').replace(r'\mapsto',r'\hand{\mapsto}').replace(r'\subset',r'\hand{\subset}').replace(r'^{\wedge}',r'^{\hand{\wedge}}')
 e(a,b,'The formula arrows, hat or subset strokes in this line are handwritten additions to typed letters; formula content is preserved.')
e(r'\inserted{i:}',r'\inserted[typed]{i:}','The i colon is typed in the interlinear space, with a pen placement curve.')
e(r'\mathrm{F}\!\not{\mathrm{l}}(M)',r'\mathrm{F}\over{l}{l}(M)','The diagonal is a pen retracing of the typed l in Fl, not a mathematical negation slash.')
e(r'i_{\mathrm{F}\!\not{\mathrm{l}}}^{-1}',r'i_{\mathrm{F}\over{l}{l}}^{-1}','The indexed Fl has the same hand-retraced l; replace the misleading negation markup while preserving the glyph layering.')
conf=dict(key=key,edits=edits,diffs={
2014:['as I already felt yesterday','The typed adverb is already, not readily.'],
2018:[r'\inserted{$j_{p,q}$}','The penned adjoint name is inserted above the line; its curved placement stroke does not cancel and.'],
2019:['Section number29 only','The scan has the overwritten section number and no prose title.'],
2022:[r'\inserted[typed]{i:}','The i colon has typewriter letterforms and is placed by a pen curve.','correct provenance'],
2026:['Selective underlining and a long marginal double bar retained','The parenthetic comments, category names in parentheses and small are not covered by the author\'s underlines; do not extend emphasis over the full passage as in the witness.']},
unsure=[['e','Enlargement resolves the live e in feel despite an old overtyped trace.'],[u[1][0],'The large handwritten29 obscures the older digits; the tentative26 cannot be securely confirmed.'],[u[2][0],'Heavy ink between model and preser leaves the canceled character unreadable as a definite s.'],[u[3][0],'The old trace under/next to the final r of however remains ambiguous even enlarged.']],
illegible=[],notes=[
'The overprinted e in feel is legible in enlargement and the doubt is removed.',
'The curved stroke from j_pq is an insertion stroke; and remains live.',
'The two bent margin arrows and the horizontal arms are reconstructed; the separate long marginal double bar is also drawn.',
'The earlier section digits remain obscured beneath29.',
'The canceled letter after model remains doubtful under dense ink.',
'The l in Fl is retraced by a pen diagonal; the source negation markup is replaced by overwritten-letter markup in both appearances.',
'The words whole, category, commutative, Criterion, upon and just remain legible despite mechanical overstrikes; however retains doubt only in its canceled old character.'],
evidence='Both halves inspected and crops checked for feel, section29, the model-preser cancellation and however. Feel resolves; the three older canceled/overwritten readings remain doubtful. Already is clear against witness readily. The inserted j_pq is pen, its curve leaves and live, while i colon is typed. The upper and lower margin arrows each have a horizontal bent arm; they and the long double vertical emphasis bar are reconstructed. Formula arrows and accents are hand additions. Both Fl l strokes are pen retracings rather than negation signs. The major basic-modelizer statement has selective author underlines leaving its parenthetical qualifications plain; the witness\'s broader emphasis is not adopted. The cohomology display has H^i, inverse image f^-1 and the indicated restrictions on locally constant coefficients.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2));save_review(conf)
