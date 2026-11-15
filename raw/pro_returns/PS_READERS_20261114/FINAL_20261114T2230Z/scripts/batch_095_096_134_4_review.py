import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_095'
edits=[
 [r'$X\longrightarrow Y$',r'$X\hand{\longrightarrow} Y$','The first arrow is drawn in pen.'],
 [r"X\times_{Y}Y'\longrightarrow",r"X\mathrm{x}_{Y}Y'\hand{\longrightarrow}",'The product sign is a typed lowercase x and the arrow is handwritten.'],
 [r'$f: X\to Y$',r'$f: X\hand{\to}Y$','The inline arrow is handwritten.'],
 [r'aspheric,\unsure{of|or} universally',r'aspheric, of universally','The scan plainly has a typed f with a tall stem and top hook. Remove the unjustified alternative r and retain of diplomatically.'],
 [r'$\over{X}{Y}_{/\over{x}{y}}\to\over{X}{Y}$',r'$\unsure{\over{X}{Y}}_{/\over{x}{y}}\hand{\to}\unsure{\over{X}{Y}}$','The lower y and arrow are penned. The capital X/Y layers are visible, but their dense serif-like impressions do not securely establish typed versus pen provenance; retain that scope of doubt.'],
 [r"$Y'\to Y$",r"$Y'\hand{\to}Y$",'The base-change arrow is handwritten.'],
 [r'$X\to e$',r'$X\hand{\to}e$','The arrow to the final object is handwritten.'],
 ['corresponding map is aspheric',r'\over[typed]{i}{c}orresponding map is aspheric','A lower dotted i remains visible beneath the regular typed c at the start of corresponding.'],
 ['\npheric over $e$','\n'+r'pheric over $\unsure{\over{e}{e}}$','The final-object e has a dense upper/left overlay; the apparent e retracing and its provenance remain explicitly uncertain.'],
 [r'F\unsure{\ell}((Cat))',r'F\over{l}{\ell}((Cat))','A regular typed l with lower foot is crossed/retraced by an oblique handwritten stroke. Preserve both layers, rather than a free uncertain letter.'],
 [r'\inserted{except that,}',r'\inserted[typed]{except that,}','Except that, is typed above the line; its descending and upturned ends form one pen placing curve. The following if needed remains live.'],
 [r'\uline{$\underline{W}$-aspheric} or',r'\uline{$\underline{W}$-as\unsure{\over[typed]{p}{p}}heric} or','The p has vertically displaced regular-looking impressions with an extra upper loop; retain the repetition/provenance doubt.'],
 [r'\xout{between}\inserted{with}',r'\xout{between}\inserted[typed]{with}','With is typed interlinearly above the typewriter-cancelled between.'],
 [r'\over{p}{t}erminology',r'\over[typed]{p}{t}erminology','Both p and t have regular typewriter forms; preserve the typed overprint rather than classify t as handwriting.'],
 [r'\hand{$\simeq$}',r'\hand{\ensuremath{\simeq}}','Repair nested math delimiters while preserving the handwritten isomorphism sign.'],
 [r'$f: F\to G$',r'$f: F\hand{\to}G$','The presheaf-map arrow is handwritten.'],
 [r'A_{/F}\longrightarrow \deleted{\illegible{1}}',r'A_{/F}\hand{\longrightarrow} \deleted{\xout{\illegible{1}}}','The arrow is penned. The old symbol has both a regular x row and heavy diagonal pen cancellation; its reading remains illegible.'],
 ['The map will be called',r'\over{\unsure{T|D}}{T}he map will be called','The broad irregular live T bar is penned over a dense old initial cell; the earlier T/D reading remains uncertain.']
]
save_review({'key':key,'edits':edits,'diffs':{
4864:['of','The typed tall f is clear; the diplomatic reading is of. An explicit isolated-slip variant changes this conjunction to or only in the corrected forms.','settled on image; isolated slip recorded'],
4868:['final object of (Cat)','The typescript has no e after final object.'],
4869:['turns out that','That is present in clear typing.'],
4870:['called simply','The terminal ed of called is visible.'],
4871:['if needed','Needed is fully typed; the preceding insertion is typed and its placing curve does not cancel if.'],
4872:['typed interlinear except that,','All letters are regular type, with a pen placing curve.','correct provenance'],
4873:['as well as','Both words well and as are clear at the right of the line.'],
4875:['upon perfect coherence','Upon is present in the typescript.'],
4876:['typed interlinear with above machine-cancelled between','The regular typewritten letters of with are distinct from the x row below.','correct provenance'],
4877:['terminology used','There is no just on the page.']
},'unsure':[
['of','The f has a clear tall stem, crossbar and top hook; it is not r. The isolated conjunction slip is handled separately in the corrected forms.'],
[r'\over{l}{\ell}','The lower typed l and a separate oblique pen stroke are both visible.']
],'illegible':[
[r'\illegible{1}','The dense diagonal pen cancellation and typewriter x impressions do not permit a secure earlier symbol.']
],'notes':[
'The complete lower sequence f prime should be aspheric. When this condition is satisfied, we is readable beneath the regular x row, including its punctuation.',
'The scan reads of plainly. The corrected or is an isolated typing-slip variant grounded also in the same-page live or in or what amounts and or any base change.',
'The lower y and the arrow are handwritten; both capital X/Y layers remain visible, but their provenance is not secure enough to remove the newly scoped doubts.',
'The typewritten l has a separate slanted pen stroke and is encoded as an overwritten l rather than silently regularized.',
'The marks after time, zer and Similarly are regular machine-x cancellations over commas; the initial diplomatic encodings are retained.',
'The old display symbol is still unreadable. Both the machine row and the added pen scribble are represented.',
'The fine bowed line below map in is an underline, not a cancellation: the typed letters remain entirely live.',
'The handwritten archive folio 95 is visible at the bottom left.'
],'extra_records':[
{'source_id':'OBS:ps_134-4_095:of_or','before':'aspheric, of universally aspheric','after':'aspheric, or universally aspheric','decision':'isolated typing slip in corrected forms','reason':'The image unequivocally types of, but the either/or contrast and the immediately stated first/second cases require the conjunction. The same page correctly types or in or what amounts and or any base change; preserve of diplomatically and record the corrected-only variant.'}
],'evidence':'Both original halves, twelve enlarged detail panels and seven supplemental panels inspected. The long cancelled sentence resolves as f prime should be aspheric. When this condition is satisfied, we. The live of has a clear typed f and is retained diplomatically; a separately recorded isolated-slip variant supplies or only in corrected forms. The product mark is a typed x and all map arrows on the page are penned. The lower localization y is penned, while the dense capital X/Y overprints retain a provenance doubt. Corresponding has a typed c over i. The e over the point and the p of the first W-aspheric retain overlay doubts. The l of Fl has an oblique pen stroke. Except that, and with are typed interlinear additions, whereas when and both is insertions are handwritten. The placing curve for except that does not cancel if needed. Terminology has a regular typed t over p. The final display has both machine and pen cancellation over an unrecoverable old symbol, and the last T is penned over a doubtful old T/D cell. The scanned omissions/additions relative to the witness, including no e after final object, that, called, needed, as well as, upon, and no just, are retained.'})
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';vs=json.loads(p.read_text());v={'key':key,'before':'aspheric, of universally aspheric','after':'aspheric, or universally aspheric','kind':'isolated typing slip','reason':'Either/or and the explicit first/second cases settle the conjunction; correct or occurs on the same page. Typed of stays diplomatic.','source_id':'OBS:ps_134-4_095:of_or'};vs=[x for x in vs if x['source_id']!=v['source_id']]+[v];p.write_text(json.dumps(vs,ensure_ascii=False,indent=2)+'\n')

key='ps_134-4_096'
edits=[
 [r'\xout{\unsure{W}}aspheric',r'\xout{$\underline{W}$\unsure{-}}aspheric','The crossed prefix contains an underlined typed W and another cancelled cell consistent with its hyphen. W resolves; the old hyphen remains doubtful.'],
 [r'\unsure{beaause|because}',r'be\unsure{a|c}ause','The doubt is confined to the third letter: its dark a-like bowl and possible earlier c are not securely separable.'],
 [r"$\unsure{G'}\hand{\to}G$",r"$\over[typed]{F}{G}'\hand{\to}G$",'A regular G overlies the straight stem and bars of an F; the prime is clear.'],
 [r'\unsure{Of} course',r'\unsure{\over[typed]{B}{O}}\over[typed]{f}{f} course','The initial cell has both O- and B-like regular outlines, with unresolved order. The f has a repeated regular type impression. Preserve the initial layer doubt.'],
 [r'\xout{\unsure{would}}',r'\xout{would}','All five lower letters of would resolve beneath the regular x row.'],
 [r'\xout{\unsure{notion of a}}',r'\xout{notion of a}','The lower notion of a is readable beneath cancellation.'],
 [r'\inserted[typed]{\xout{\unsure{word}} word}',r'\inserted[typed]{\xout{word} word}','The cancelled interlinear word resolves; it is followed by a second clear live word, both typed.'],
 [r'the \xout{\illegible{1}} two',r'the \xout{noti\unsure{o|n}} two','The partial old run begins noti; its final rounded/shouldered cell remains uncertain. Do not supply an unseen complete notion.'],
 [r'\xout{$A_{/F}$ \illegible{2} (Cat) being in $\underline{W}$}',r'\xout{$A_{/F}$ \illegible{1} e in (Cat) being in $\underline{W}$}','The old e in resolves before Cat. The intervening cancelled space/run after A/F gives no secure arrow or word and remains one illegible unit.'],
 [r'are\inserted{$\underline{W}$-} aspheric',r'are \inserted[typed]{$\underline{W}$-}aspheric','The raised W- is regular typing, with a separately dark underbar. Its placement does not cancel the final e of are; restore the word boundary before the prefix.']
]
save_review({'key':key,'edits':edits,'diffs':{
4882:['word','The live interlinear typed word is unambiguous, and its previous cancelled duplicate also resolves.'],
4887:['namely the map','The is clearly typed; there is no that.'],
4892:['typed interlinear W-','The raised W and hyphen are regular type. Keep the ordinary underline and the word boundary before the inserted prefix.','correct provenance'],
4895:[r'aspheric\hand{)}. A third','A large handwritten closing parenthesis is clearly present before the period.']
},'unsure':[
[r'$\underline{W}$\unsure{-}','The underlined W resolves; the additional cancelled cell is compatible with a hyphen but remains uncertain.'],
[r'be\unsure{a|c}ause','Only the third letter is uncertain, with a dark a-like bowl and possible overprinted c.'],
[r"\over[typed]{F}{G}'",'The capital G, underlying F and prime can all be distinguished.'],
[r'\unsure{\over[typed]{B}{O}}\over[typed]{f}{f}','O/B outlines and the repeated f are visible; the first-cell order remains doubtful.'],
['would','All five lower letters are recoverable.'],
['notion of a','The baseline cancellation still exposes the complete phrase.'],
['word','The cancelled upper word has recoverable w-o-r-d shapes, including the terminal d ascender.']
],'illegible':[
[r'noti\unsure{o|n}','The first four characters resolve, but the final cell does not support a unique reading.'],
[r'\illegible{1} e in','The e in is readable before Cat; the preceding x row does not reveal a secure underlying mark or word.']
],'notes':[
'The underlined W prefix is visible beneath cancellation; its following possible hyphen remains doubtful.',
'The third letter of because/beaause has overlapping a/c-like impressions. Narrow the doubt without normalizing it to the witness.',
'The G-prime is a regular typed G over F, with a clear independent prime.',
'The machine-cancelled would is fully readable.',
'The baseline notion of a and the cancelled upper word both resolve. The live upper word is typed and distinct from the witness work.',
'The short run before two resolves partly as noti with a doubtful last o/n. In the longer cancellation, e in resolves; the preceding segment remains illegible.',
'The small separate oblique mark immediately before the opening parenthesis is visible and is retained as a handwritten mark; it does not cancel the parenthesis.',
'The pencil archive folio 96 is visible at lower left.'
],'evidence':'Both original halves, twelve initial detail panels and five larger supplemental panels inspected. The cancelled first prefix has an underlined W and a doubtful additional hyphen cell. The uncertain third vowel/consonant of beaause/because is narrowed rather than normalized. G prime resolves as typed G over F; the Of initial retains O/B order doubt and f has repeated type. Would, notion of a, and the cancelled interlinear word resolve; the second live word is plainly typed. Are even is handwritten over hand-struck implies; the small oblique mark before the parenthesis remains distinct. The cancelled short run before two is only partly recoverable as noti plus a doubtful final cell. The long cancellation has readable e in before Cat, but the earlier run is still illegible. The two star labels, display arrows, e and equals A of the second display, comma after the cancelled parenthesis, and both closing parentheses are handwritten. The last raised W- is typed and does not cancel are. The absolute and relative asphericity statements, the absence of an added W before aspheric after the second display, and the terminal comma before the next page remain literal.'})
for k in ['ps_134-4_095','ps_134-4_096']:
 s=(OUT/'checked_pages'/f'{k}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  n+=1 if m.group()=='{' else -1
  assert n>=0,(k,m.start())
 assert n==0,(k,n)
