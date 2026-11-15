import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_093';edits=[
 [r'bootstraps\unsure{,}',r'bootstrap\over[typed]{s}{s}\unsure{,}','The final s has repeated type impressions. The possible following comma is at the clipped edge and remains uncertain.'],
 [r'$A\longrightarrow B^{\wedge}$',r'$A\hand{\longrightarrow} B^{\wedge}$','The functor arrow is hand-drawn.'],
 [r'the\xout{t} so-called',r'th\unsure{\over[typed]{a}{e}}\xout{t} so-called','The lower a of that remains visible beneath a possible e overprint, while the final t has a regular machine-x cancellation. Preserve the a/e layering doubt.'],
 ['finally more psychological',r'finally \over{m}{m}ore psychological','The initial m is retraced in pen over type.'],
 ['One point which',r'O\unsure{\over[typed]{n}{n}}e point which','The n has raised repeated impressions, whose exact order remains uncertain.'],
 [r'namely, \inserted{which}',r'namely, \inserted[typed]{which}','Which is typed above the line. Its continuous placing curve leaves the following will live.'],
 [r'point \inserted{on}',r'point \inserted[typed]{on}','On is typed interlinearly, with only the placing curve in pen.'],
 [r'\xout{decision}',r'\xout{decision\unsure{s}}','Decision is readable under the x row; an additional final s-like cell is present but remains uncertain.'],
 ['about '+r'\xout{(Cat)}'+'\nthe special', 'about '+r'\deleted{\xout{(Cat)}}'+'\nthe special','The first cancelled Cat has an additional long irregular pen stroke over its machine row.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4817:['Number 66 only, with overwritten second digit','There is no descriptive section title on the page.'],
 4820:['I thought next thing','There is no the before next.'],
 4824:['the particular case of M','Of is clearly typed and must remain.']
 },'unsure':[
 [r'\unsure{,}','The final dark projection is clipped at the edge; the comma remains tentative.'],
 [r'\unsure{ew}','The live pen ew is clear, but the older letters are too overlaid to settle.']
 ],'notes':[
 'The terminal s of bootstraps has repeated typing. The possible comma is clipped and remains doubtful.',
 'The old a is visible beneath a possible e overprint, and the t is machine-cancelled. Retain the a/e layer uncertainty instead of printing a confident the.',
 'The interlinear M,W parenthesis is typed, with a pen placing curve. Which and on later on the page are likewise typed additions.',
 'The new ew is legible pen, while its old typed layer remains doubtful. The earlier cancelled decision has an additional tentative final s.',
 'The pencil archive folio 93 is visible at lower left.'
 ],'evidence':'Both original halves and ten enlarged panels inspected. The date 9.4 and rewritten section number are visible. The clipped ending of bootstraps has repeated s impressions and an uncertain possible comma. The functor arrow is penned. The patch before so-called has an old a beneath a possible e and a separately machine-cancelled t, so its old/new vowel layer remains doubtful. More has a pen m retracing, and One a doubtful repeated n layer. The M,W insertion, which, and on are typed; their placing curves do not cancel following live words. Really essential and First of all are handwritten, with the final comma of the latter independent of its placing curve. The new ew of review is clear, but the old letters remain doubtful. The cancelled decision has a further tentative s-like cell. The first deleted Cat has an added pen strike. The source next thing and case of M are retained.'})

key='ps_134-4_094'
phrase='the main emphasis in choice of terminology'
callout=r'\diagram{\begin{tikzpicture}[baseline=(p.base)]\node[inner sep=3pt] (p) {'+phrase+r'};\draw[color=blue,line width=.45pt,rounded corners=3pt] (p.south west)--(p.north west)--(p.north east)--(p.south east)--([xshift=-4em]p.south east)--([xshift=-4.2em,yshift=-1.4ex]p.south east)--([xshift=-4.4em]p.south east)--cycle;\end{tikzpicture}}'
edits=[
 [r'me,\xout{\illegible{1}}',r'me,\xout{to call}','The lower words to call resolve beneath the typewriter row.'],
 [r'which \xout{\illegible{1}}',r'which \xout{\unsure{may}}','The clipped old run looks like may, but the last cell is too obscured to settle.'],
 [r'\xout{\illegible{1}} spontaneously',r'\xout{surely} spontaneously','The old surely is fully readable beneath the machine cancellation.'],
 [r'intuitions \xout{\illegible{1}}',r'intuitions \xout{and}','The old and resolves under its regular x row.'],
 [r'and of \xout{\illegible{1}}',r'and of \xout{categ}','The lower c-a-t-e-g run is readable, including the final g descender.'],
 ['(small) categories',r'(s\over[typed]{\unsure{ma}}{ma}ll) categories','The ma cells have dense regular overprints, with the earlier layer still tentative.'],
 [phrase,callout,'Reconstruct the pen enclosure and its descending placement point around the typed phrase, preserving its original physical order. The author-directed transposition is recorded separately for corrected forms.'],
 [r'throughout\hand{,}through',r'throug\over[typed]{h}{h}out\hand{,} through','The h has repeated type impressions. Preserve the actual boundary after the added comma.'],
 [r'wording\hand{,}the',r'wording\hand{,} the','Restore the boundary after the handwritten comma.'],
 [r'\xout{\unsure{technical}}',r'\xout{technical}','All lower letters of technical resolve under the regular machine row.'],
 [r'topologists\hand{,}in',r'topologists\hand{,} in','Restore the boundary after the handwritten comma.'],
 [r'topoi,\inserted{or}',r'topoi, \inserted{or}','Restore the boundary before the inserted conjunction.'],
 ['self is visibly',r'self is \over[typed]{s}{v}isibly','The first v overlies a rounded typed s whose lower curve remains visible.'],
 ['in the context\nof topological',r'in the cont\over{ex}{ex}t'+'\nof topological','The ex of context is retraced in dark pen over its typed letters.'],
 [r'\xout{, \unsure{par}}',r'\deleted{\xout{, p\unsure{ar}}}','The initial old p resolves, while ar remains obscured. The cancellation also has a separate diagonal pen stroke across the comma and toward the letters.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4848:['have told us','Us is clearly typed, not the witness me.'],
 4844:['The enclosed phrase is moved to just before should','The pen enclosure has a downward placing point before should on the following line. The diplomatic order is preserved, and the explicit corrected variant applies the transposition.']
 },'unsure':[
 ['technical','The entire cancelled word resolves beneath the regular x row.'],
 [r'p\unsure{ar}','The initial p is legible; the following two letters remain obscured.']
 ],'illegible':[
 ['to call','Both old words are readable under the typewriter cancellation.'],
 [r'\unsure{may}','The clipped run is compatible with may but not securely recoverable.'],
 ['surely','The six letters and final y descender are clear through the x row.'],
 ['and','All three old letters resolve.'],
 ['categ','The c-a-t-e-g sequence and final g descender resolve beneath the strike.']
 ],'notes':[
 'The geometri/co-topological and situ/ations continuations remain joined without supplying unseen hyphens. The final word context is readable and has pen ex retracing.',
 'Technical resolves. After vious one the old p resolves, ar remains doubtful, and the comma and letters have both machine and pen cancellation.',
 'The complete typed phrase is enclosed by a pen contour with a descending placing point before should. Its original order is preserved diplomatically and its movement is specified as a complete balanced variant.',
 'All four emphasized spans the, aspheric map, proper and any have visible underscoring. The rules are retained as source emphasis; no new verbal annotation is supplied from their shape.',
 'Maps of is typed above the line and is placed by a continuous pen curve, as encoded.',
 'The pencil folio 94 is visible at lower left.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_094:spontaneously','before':'spontaneously','after':'spontaneously','decision':'retain; cross-page spelling evidence','reason':'The entire word is clearly and correctly typed. It supplies same-word evidence for the isolated spantaneously on reviewed 134-2/034, without changing either authorial spelling silently.'},
 {'source_id':'OBS:ps_134-4_094:phrase_transposition','before':'Enclosed phrase before in a context','after':'Enclosed phrase immediately before should','decision':'apply author instruction in corrected forms','reason':'The downward placement point explicitly moves the phrase past the intervening context clause; the complete balanced before/after span is in MASTER_VARIANTS_134_3_4.json.'}
 ],'evidence':'Both original halves, eleven initial detail panels and four targeted supplemental panels inspected. To call, surely, and, categ and technical resolve beneath machine cancellation, while the clipped may and later ar remain doubtful. Spontaneously is clearly typed with the correct spelling and is recorded as cross-page evidence. Small has dense ma type overlays; throughout has repeated h; visibly has typed v over s; context has pen ex retracings. The typed main-emphasis phrase is enclosed and moved by a pen point to before should, while the diplomatic word order remains literal. Maps of is typed above the line. Precisely, where the latter, or, here, the name, and and particular are handwritten additions; their placement curves do not cancel the following live words. The cancellation after vious one has both machine and pen strokes. The source us, handfull, inapropriateness, developped and apostrophe order are retained.'})
p=OUT/'checked_pages'/f'{key}.tex';s=p.read_text();before=callout+'\nin a context where working with small categories as ``spaces\'\', should';assert before in s
after='in a context where working with small categories as ``spaces\'\',\n'+phrase+' should'
v={'key':key,'before':before,'after':after,'kind':'author phrase transposition','reason':'The pen enclosure and descending placing point move the whole main-emphasis phrase to before should, after the context clause.','source_id':'OBS:ps_134-4_094:phrase_transposition'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
for k in ['ps_134-4_093','ps_134-4_094']:
 s=(OUT/'checked_pages'/f'{k}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(k,m.start())
 assert n==0,(k,n)
