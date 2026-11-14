import re,sys,json
from pathlib import Path
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_073';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'^{\wedge}',r'^{\hand{\wedge}}').replace(r'\longrightarrow {W_{Cat}}',r'\hand{\longrightarrow} {W_{Cat}}')
 if new!=line:edits.append([line,new,'The presheaf carets and the displayed localization arrow are handwritten. The arrow’s thick shaft and asymmetric point differ from typed letters.'])
edits += [
 [r'\mspage{73}',r'\mspage{\hand{73}}','The folio is handwritten.'],
 [r'(Hot). The only',r'(Hot). T\over[typed]{h}{h}e only','The h has vertically displaced typewriter impressions, including the upper remnant.'],
 [r'that this inclusion',r'that th\over[typed]{e}{i}s inclusion','The old e bowl and crossbar remain under the typed dotted i.'],
 [r'for instance from (Cat)',r'for instance from \over{A}{(}Cat)','The opening parenthesis is drawn over a clearly visible typed capital A.'],
 [r'\unsure{are|and}',r'\over[typed]{\illegible{1}}{are}','The final visible letters read are: the middle letter has the r shoulder, and the last has no d ascender. Earlier overprinted letters cannot be separated securely.'],
 [r'\over{$f$}{$F$}',r'\over[typed]{$f$}{$F$}','The uppercase F has typewriter serifs and is typed over the lower f, rather than penned.'],
 [r'iff for any object',r'iff f\unsure{\over[typed]{ro}{or}} any object','The two cells after f contain overlapping r/o impressions. The likely correction fro to for cannot be ordered with complete confidence, so retain uncertainty on the typed overprint.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2795:[r'\over[typed]{\illegible{1}}{are}','The final word reads are, not and; the preceding overprinted layer remains unreadable.','correct transcription'],
 2796:[r'\over[typed]{$f$}{$F$}','The final uppercase F is a typed overprint.','correct transcription'],
 2798:[r'$W^{-1}M \hand{\to} W^{-1}M$','Both occurrences of M are visibly present in the source.']
 },'unsure':[[r'\over[typed]{\illegible{1}}{are}','The final r shoulder and the absence of a d ascender settle are. The earlier typed layer cannot be fully read.']],
 'illegible':[],
 'notes':[
 'The right edge still clips the listed line endings; no missing letters or punctuation are supplied beyond the scan.',
 'The final visible word is are, with an unreadable earlier typewritten layer retained beneath it.',
 'Below, two, by localization, F and now are typed insertions. Both when replacements and induced are pen. Their existing placement is confirmed.',
 'The inline arrows and the arrow in the large localization display are all hand-drawn; the latter was previously left plain.',
 'The underlines are pen strokes, with long slightly wavering runs and separately drawn endpoints. Their existing underline macros are retained.'
 ],'evidence':'Both original halves and six enlarged details inspected. The discussion separates canonical comparisons of modelizing functors from the conjecture that an objectwise-identity endofunctor of Hot must be naturally isomorphic to the identity. Typed additions below, two, by localization, F and now are confirmed. The word before quasi-inverse finally reads are, though its earlier overprint is unreadable. The uppercase F over f is typed. The for/fro cells contain a newly retained uncertain typed transposition. The opening parenthesis of the first (Cat) in the example replaces a typed A. The general full-subcategory argument retains both source and target M in the localized endofunctor; the displayed arrow and all presheaf carets are pen.'})

key='ps_134-3_074';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line
 if line.startswith("and h'"):new=new.replace(r'\longrightarrow',r'\mathrel{\rule{.45cm}{.35pt}}')
 new=new.replace(r'\hat{}',r'^{\hand{\wedge}}')
 for macro in ('longrightarrow','longmapsto','to'):
  new=re.sub(r'\\'+macro+r'(?![A-Za-z])',r'\\hand{\\'+macro+'}',new)
 if new!=line:edits.append([line,new,'The ordinary arrows and raised carets are pen. In the first handwritten insertion the connecting stroke has no visible arrowhead, so reproduce the actual horizontal bar instead of supplying one.'])
paragraph=r'\begin{tikzpicture}[baseline=-.2ex]\draw[color=blue] (0,0)--(.25,0)--(.25,.4)--(.6,.4);\end{tikzpicture}'
edits += [
 [r'\mspage{74}',r'\mspage{\hand{74}}','The folio is handwritten.'],
 [r'is a modelizer, this implies',r'is a mode\unsure{\over[typed]{h}{l}}izer, this implies','The l-position contains h/l-like typewriter impressions. Their layer order is not fully secure, so retain the visible ambiguity instead of flattening to modelizer.'],
 [r'\inserted{inclusion}',r'\inserted[typed]{inclusion}','The interlinear inclusion is typed above a pen placement curve.'],
 [r'to the modelizer (Cat)',r'to \over[typed]{\unsure{M}}{t}he modelizer (Cat)','The t overlaps a larger old capital-like impression, tentatively M; both have typewriter serifs.'],
 [r'(\S. \over{5}{3}7)',r'(\hand{\S}. \over{5}{3}\over{7}{7})','The section sign and both final digits are pen. The first digit overwrites typed 5; the second retraces typed 7.'],
 [r'\inserted{modelizer}',r'\inserted[typed]{modelizer}','The replacement modelizer is typed above the cancelled test category.'],
 [r'The same of course',r'T\over[typed]{h}{h}e same of course','The small upper and lower h remnants are displaced typewriter impressions.'],
 [r'\inserted{the test category}',r'\inserted[typed]{the test category}','The whole interlinear phrase is typed.'],
 [r'\over{O}{o}ne natural',r'one natural','The apparent extra stroke over o belongs to the descending g of the typed interlinear category above it. There is no independent O-to-o correction in one.'],
 [r'ordered set\inserted{\deleted{(or at least ``locally ordered\'\')}}',r'ordered set \inserted{\deleted{(or at least ``locally ordered\'\')}}','Preserve a literal word boundary before the cancelled interlinear parenthesis.'],
 [r'\inserted{algebraic}',r'\inserted[typed]{algebraic}','The added algebraic is typed; its placement curve passes above models rather than cancelling that word.'],
 [r'(\S.\unsure{22})',r'(\hand{\S}.\over{\unsure{1}}{2}\over{2}{2})','The final handwritten reference is 22. A first old numeral remains tentative as 1; the second 2 is retraced.'],
 [r'\inserted{a suitable}',r'\inserted[typed]{a suitable}','The interlinear a suitable is typed over the cancelled the.'],
 [r'\deleted{page 53}\inserted{section 35}',r'\deleted{page 53} \inserted{section 35}','Keep a literal space between the deleted reference and its replacing whole phrase.'],
 [r'\hand{$\rfloor$}',paragraph,'The mark is a stepped paragraph-break sign with two horizontal arms and an upward vertical, not a floor bracket. Preserve the graphic in diplomatic and apply the break through the master variant.'],
 [r'categor\hand{y}',r'categor\over{y}{y}','The final y is penned over a typed y at the clipped edge, rather than supplied in a blank.']
]
# Quote-bearing source text is represented literally, without accent escapes.
for edit in edits:
 edit[0]=edit[0].replace("\\'", "'");edit[1]=edit[1].replace("\\'", "'")
save_review({'key':key,'edits':edits,'diffs':{
 2801:[r"and h'\inserted{$:M\mathrel{\rule{.45cm}{.35pt}}M'$}",'The handwritten connecting mark between the two Ms is a plain horizontal stroke without a visible arrowhead.','correct transcription'],
 2802:[r'\inserted[typed]{inclusion}','The inserted word is typed above a pen placement line.','correct transcription'],
 2803:[r'(\hand{\S}. \over{5}{3}\over{7}{7})','The final section number is 37, with both digits and the section sign penned.','correct transcription'],
 2806:[r'\inserted[typed]{modelizer}','The replacement word is typed, not handwritten.','correct transcription'],
 2808:[r'\inserted[typed]{the test category}','The phrase is typed above the line.','correct transcription'],
 2810:[r"\inserted{\deleted{(or at least ``locally ordered'')}}",'The entire handwritten parenthetical is crossed by a heavy horizontal pen line and remains deleted.'],
 2811:[r'\inserted[typed]{algebraic}','The interlinear algebraic has typewriter serifs; models is not cancelled.','correct transcription'],
 2812:[r'\inserted[typed]{a suitable} \deleted{the}','The replacement phrase is typed; the old the is cancelled by pen.','correct transcription'],
 2814:[paragraph,'The source contains a stepped paragraph-break mark. It is retained graphically and applied only in the master variant.','correct transcription'],
 2815:[r'\margin{X}','A separate X stands beside the T1 + T3 sentence.'],
 2816:['(just T 1 + T 3 )','The source has a plus sign between T1 and T3, not to.']
 },'unsure':[[r'22; earlier first digit \unsure{1}','The final reference is 22; the first lower old digit remains tentative as 1.']],
 'illegible':[],
 'notes':[
 'The modelizer letter contains overlapping h/l-like impressions; their order remains uncertain and is now marked explicitly.',
 'The cancelled final s in functors and models is machine-overstruck; both cancellations are retained.',
 'The t in the overlaps a larger capital-like typed impression, tentatively M, which remains doubtful.',
 'The final section reference is 37, with hand sign and digits; its 3 overlies typed 5 and its 7 retraces a typed 7.',
 'There is no independent O-to-o correction in one: the extra upper ink is the descending g of category in the inserted line above.',
 'Models remains live; the pen curve belongs to the placement of the typed algebraic above it.',
 'The final reference is 22, with an uncertain old first numeral and a retraced second 2.',
 'The first letter of in is a pen dotted i over an old o, as the source macro records.',
 'The displaced h remnants around The are typed overprinting and have been represented.',
 'The final y has a pen retracing over the typed y; the right edge remains clipped without adding further text.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_074:1','before':'which are quasi-inverse to each other','after':'which are quasi-inverse to each other','decision':'retain apparent authorial overstatement','reason':'In the preceding general setup, g h-prime equals h, and only the induced h being an autoequivalence was assumed. Quasi-inverseness requires its comparison to the identity, which the later intended application does have. Preserve the wording and flag this distinction in the guide.','line':6}],
 'evidence':'Both original halves, nine detail crops and a further enlargement around one inspected. The horizontal connector in the first handwritten insertion lacks a visible arrowhead. Inclusion, modelizer, the test category, algebraic and a suitable are typed additions. The apparent O-to-o in one comes from the descending g of the insertion above and has been removed. The final section references are 37 and 22, with a remaining doubt about the old first digit under the latter. Models is not cancelled; the locally ordered parenthetical is. The stepped paragraph mark is reconstructed and has an applied master break. The preliminary quasi-inverse assertion is preserved but separately qualified for its general hypotheses; its intended i_A i-star application has the needed identity comparison.'})
vpath=Path('PS_READERS_WORK/records/MASTER_VARIANTS_134_3_4.json');v=json.loads(vpath.read_text());v=[x for x in v if x.get('source_id')!='DIFF:2814'];v.append({'key':key,'before':paragraph,'after':'\n\n','kind':'authorial paragraph break','reason':'The stepped pen mark between the sentences calls for a paragraph break. Diplomatic retains the actual mark.','source_id':'DIFF:2814'});vpath.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
