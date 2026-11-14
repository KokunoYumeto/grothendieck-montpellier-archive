import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT,OUT

def hupper():return r'T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\mathrm h}$e'
variants=[]
key='ps_134-4_040';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[
 [r'an\xout{y}',r'an\deleted{y}','The y is crossed by an irregular pen zigzag, not regular machine x impressions.'],
 [r'\xout{\unsure{any}}',r'\xout{any}','Any is legible beneath the typewriter x row.'],
 ['The condition',hupper()+' condition','Two small upper pen marks stand over the typed h; a small lower dash is also retained.'],
 [hupper()+' condition',hupper().replace(r'\mathrm h',r'\underset{\hand{-}}{\mathrm h}')+' condition','The separate short dash under h is visible beneath the pair of upper marks.'],
 ['The only standart',hupper()+' only standart','The h has two small upper pen marks; the letter itself remains typed.'],
 [r'\xout{xxx}',r'\xout{\illegible{1}}','The machine x row hides an unreadable earlier run; its lower text is not literally xxx.'],
 ['M admits finite products',r'M \over{a}{a}dmits finite products','The initial a of admits is pen-retraced over the typed a.'],
 [r'\inserted{(highly non auto-dual}',r'\inserted{\unsure{highly|highty} non auto-dual}','The initial curve is continuous with the placing line beneath the phrase, not an independent opening parenthesis. The l/t-shaped letter in the first word remains doubtful.'],
 [r'axiom\deleted{\unsure{s}}',r'axiom\unsure{\over{s}{s}}','The terminal cell is a compact dark pen-marked shape without an independently secure cancellation stroke. Preserve the doubtful live s/ink layer instead of silently deleting it.']
]
step=r'\diagram{\begin{tikzpicture}[baseline=-.3ex,x=1em,y=1ex]\draw[color=blue,line width=.5pt] (0,0)--(.12,2.5);\draw[color=blue,line width=.5pt] (.13,0)--(.25,2.5);\end{tikzpicture}}'
edits.append([r'\hand{$|$}',step,'The mark consists of two steep pen strokes joining the end-of-line rules: it is a paragraph instruction, not a textual vertical bar.'])
# Each nested math delimiter repair is recorded independently.
for i,m in enumerate(re.findall(r'\\hand\{\$([^$]+)\$\}',src),1):
 old=r'\hand{$'+m+'$}';new=r'\hand{\ensuremath{'+m+'}}'
 # Repeated identical tokens are changed one occurrence at a time by a full line.
for line in src.splitlines():
 if r'\hand{$' in line and r'\hand{$|$}' not in line:
  new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
  # Whole-line repairs must include prior changed words on this line.
  for old,after,_ in edits:
   if old in line:line=line.replace(old,after);new=new.replace(old,after)
  if line!=new:edits.append(['\n'+line+'\n','\n'+new+'\n','Use ensuremath instead of nested dollar delimiters inside handwriting macros; all symbols and their provenance remain unchanged.'])
para_before=r'\uline{sums in M,} which'+'\n'+r"we finally introduced by the end of yesterday's \uline{reflection.}"+step
para_after="sums in M, which\nwe finally introduced by the end of yesterday's reflection."+r'\par'
save_review({'key':key,'edits':edits,'diffs':{
 3886:['Connected pen rules under sums in M and reflection, with a double rising stroke','The rules form the stepped paragraph instruction before To come. Its graphic remains diplomatic; an explicit author-instruction variant supplies the paragraph in corrected forms.']
 },'unsure':[
 [r'\unsure{_{,}}','The lower comma-like cell has a compact ink layer; neither its exact earlier sign nor cancellation is secure. Its doubtful subscript reading remains.'],
 ['any','The a, n and y descender are readable beneath the x row.'],
 [r'\unsure{\over{s}{s}}','The dark terminal cell lacks a securely distinguishable cancellation stroke, so it remains a doubtful live s/ink layer.']
 ],'illegible':[[r'\illegible{1}','The small lower symbol is covered by pen scribbling; no secure former letter can be separated.']],
 'notes':[
 'The upper line reaches the clipped edge after isomor; no independent hyphen can be established, so none is added.',
 'The lower comma-like mark after q remains doubtful with its dense ink layer; it is not silently removed.',
 'Both The forms have paired upper h marks; The condition also has a short lower dash.',
 'The y after an is pen-cancelled; the later any resolves under machine strikes. The short row after I conceals an unreadable earlier run.',
 'The terminal s-like cell after axiom is blackened without a secure separate cancellation stroke. It remains live with doubt.',
 'The left curve belongs to the continuous placing line. The first word has a doubtful l/t-shaped stroke, retained as highly|highty.',
 'The two end-of-line rules and the doubled steep stroke form a paragraph instruction before To come, preserved graphically and applied by an explicit variant.',
 'The lower scribbled symbol remains illegible.',
 'The archive folio 40 is handwritten.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_040:paragraph','before':para_before,'after':para_after,'line':37,'decision':'master author instruction','reason':'The connected stepped rules instruct a paragraph before To come; the corrected forms apply it, while the diplomatic form preserves the graphic.'},
 {'source_id':'OBS:ps_134-4_040:letters','before':'R and L are associated','after':'R and L are associated','line':10,'decision':'retain author notation','reason':'The pair just discussed is (R,W); the source visibly substitutes L in this prose sentence. Preserve and flag the variable slip.'},
 {'source_id':'OBS:ps_134-4_040:closing_sign','before':'C_o set display ends with a parenthesis','after':'C_o set display ends with a parenthesis','line':17,'decision':'retain author notation','reason':'The opening set brace is not matched by a closing brace; a second typed closing parenthesis is visible instead. Preserve this source delimiter slip.'}
 ],'evidence':'Both original halves and nine enlarged panels inspected. The manuscript says R and L where the pair was R and W, and the displayed set ends with a typed parenthesis instead of a brace. The lower comma-like mark after q remains doubtful. The first cancelled y is penned; the later any is readable under machine strikes. The two The forms carry upper h marks and The condition a lower dash. Admits has a pen-retraced a. The interlinear phrase begins with a continuous placing curve rather than a textual parenthesis, and its highly/highty letter remains uncertain. The dark final cell of axiom does not securely establish deletion. The connected end-of-line rules and doubled rising stroke are an authorial paragraph instruction. The lower scribbled symbol remains unreadable. Nested math delimiters are repaired without changing readings.'})
variants.append({'key':key,'before':para_before,'after':para_after,'kind':'author paragraph instruction','reason':'Apply the paragraph break directed by the connected stepped pen rules before To come.','source_id':'OBS:ps_134-4_040:paragraph'})

key='ps_134-4_041';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
old=src[src.index(r'\diagram{'):src.index(r'\end{tikzcd}}')+len(r'\end{tikzcd}}')]
new=old.replace(r'\arrow[',r'\arrow[color=blue, ').replace(r', "\hand{}"\'','')
edits.append([old,'% Hand-drawn arrows are marked blue; typed objects remain plain.\n'+new,'Every arrow is drawn in pen, while the Hom/Q/L objects are typed except the explicitly handwritten equalities. Arrow topology and labels are retained.'])
edits += [
 [r'vertical\xout{\unsure{ll}}',r'vertical\xout{\unsure{l}}','There are only two l cells after vertica: the live final l and one overtyped extra cell. Independent review confirms the count; its old l remains tentative.'],
 [r'T\unsure{h|H}e main fact',r'T\over[typed]{h}{H}e main fact','Regular serifed capital H is typed over lowercase h, with both impressions visible. Preserve the final typed capital rather than normalizing it.'],
 [r'\xout{\unsure{putxn}}',r'\xout{\unsure{puton}}','The cancelled fourth cell has an o-like lower curve; the run appears puton without a secure space, but remains doubtful.'],
 [r'\unsure{which}',r'\over[typed]{t}{w}hich','The live word is which: a typed w covers an earlier t whose ascender and crossbar remain visible.'],
 [r'relations\hand{,} or homotopism',r'relations\hand{,} \over{or}{or}\hand{\ensuremath{\circ}}\diagram{\begin{tikzpicture}[baseline=-.3ex,x=1em,y=1ex]\draw[color=blue,line width=.5pt] (0,-.6)--(0,2.8);\draw[color=blue,line width=.5pt] (-.13,-.1)--(.14,.05);\end{tikzpicture}} homotopism','Or is pen-retraced. A separate small loop and tall stroke with a low crossbar follow it; preserve these graphics without construing a cancellation.'],
 [r's\colon L(M)\to Q(M)',r's\colon L(M)\hand{\to} Q(M)','The inline arrow is penned.'],
 [r'M_h \to M_R',r'M_h \hand{\to} M_R','The first displayed comparison arrow is penned.'],
 [r'M_h \to M_W',r'M_h \hand{\to} M_W','The second displayed comparison arrow is penned.'],
 [r'M\to M\'',r'M\hand{\to} M\'','The later inline functor arrow is drawn in pen.'],
 ['provided we assume $R$',r'provided we assume $\over[typed]{R}{R}$','The R has two displaced serifed type impressions.']
]
edits=[[(v.replace("\\'","'") if isinstance(v,str) else v) for v in e] for e in edits]
caption='(weak homotopy '+r'\hand{|}'+' (contractibility\ninterval struc- '+r'\hand{|}'+' structures)\ntures) '+r'\hand{|}'
caption_new=r'\begin{tabular}{@{}l@{\quad}c@{\quad}l@{}}\shortstack[l]{(weak homotopy\\interval struc-\\tures)} & \hand{\vrule width .4pt height 4ex depth 1.2ex} & \shortstack[l]{(contractibility\\structures)}\end{tabular}'
edits.append([caption,caption_new,'The caption divider is one continuous vertical pen line between two text blocks, not three literal vertical-bar characters.'])
save_review({'key':key,'edits':edits,'diffs':{
 3895:['One continuous pen line between the two captions','The line separates the weak-interval and contractibility captions and is retained as a graphic rule.'],
 3901:['only and three both underlined','Each word has its own visible pen underline.'],
 3905:['which naturally','The live which is typed, with w over t; the witness substitutes that.']
 },'unsure':[
 [r'\unsure{notions}','The old word is heavily zigzag-cancelled; notions remains the strongest candidate but its middle/end letters are not all separable.'],
 [r'\unsure{déployer}','The cancelled first word has the length and surviving ascenders/descenders of déployer, but its ink overlaps retain doubt.'],
 [r'\unsure{l}','Only one extra l-sized cell follows vertical; the overprinted old cell remains tentative.'],
 [r'\over[typed]{h}{H}','The two serifed type impressions are lowercase h and capital H, with the heavier complete H uppermost.'],
 [r'\unsure{puton}','The old fourth cell has an o-like curve, but the cancelled run remains uncertain.'],
 [r'\over[typed]{t}{w}hich','The live w and the lower t ascender/crossbar are both visible.']
 ],'notes':[
 'The old notions remains doubtful beneath a heavy pen zigzag. The right-edge structuring word is clipped and the visible stru/tures sequence is retained.',
 'The first cancelled margin word still tentatively reads déployer. The following note about spreading the diagram is legible.',
 'The word has one extra overtyped l cell after vertical, not two; independent inspection confirms the count.',
 'Which has a regular typed w over an earlier t.',
 'THe is a typed H over lowercase h, not a secure pen correction to a lowercase final form.',
 'The archive folio 41 is handwritten.'
 ],'evidence':'Both original scan halves, the six-panel detail sheet and five additional enlarged panels inspected. The top graph has pen arrows and pen r/s labels, with typed principal objects and the marked handwritten equalities. Its caption divider is one continuous line. The marginal instruction to spread the diagram is clear except its first cancelled word. Notions under the bracketed caption remains doubtful. Or is pen-retraced and is followed by an independent loop and tall low-crossed stroke, not a secure cancellation. Vertical has one extra overprinted l cell, independently corroborated. The main paragraph begins with typed capital H over lowercase h. The cancelled puton remains tentative. Which resolves to typed w over t, and only and three both retain underlining. All four remaining comparison arrows are drawn in pen, and R has a displaced typed impression.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());ids={v['source_id'] for v in variants};p.write_text(json.dumps([v for v in old if v['source_id'] not in ids]+variants,ensure_ascii=False,indent=2)+'\n')
