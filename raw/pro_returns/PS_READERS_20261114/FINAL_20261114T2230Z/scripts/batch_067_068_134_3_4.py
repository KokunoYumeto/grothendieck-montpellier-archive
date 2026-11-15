import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_067';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A^\wedge',r'A^{\hand{\wedge}}')
 for macro in ('longrightarrow','in','cap','emptyset'):
  new=re.sub(r'\\'+macro+r'(?![A-Za-z])',r'\\hand{\\'+macro+'}',new)
 if new!=line:edits.append([line,new,'The arrows, membership, rounded intersection cap, empty-set sign and raised carets are pen. The cap is not the typed caret suggested in NOTES.'])
edits += [
 [r'\mspage{67}',r'\mspage{\hand{67}}','The folio is handwritten.'],
 [r'\xout{givexrisexto}',r'\xout{give rise to}','The underlying words give rise to remain readable under the typewriter cancellation; the intervening x shapes are cancellation strokes.'],
 [r'\xout{\unsure{inxAt}}',r'\xout{in $A^{\hand{\wedge}}$}','The cancelled phrase is in A with a separate raised pen caret; the original transcription mistook the caret/strike for a final t.'],
 [r'\unsure{\over{(}{f}}',r'\over{\unsure{f}}{f}','The new f is clear. Thin lower serif-like remnants favour an old f rather than an opening parenthesis, but the earlier character remains uncertain.'],
 [r'\unsure{Thexmax}',r'\unsure{The mat}','The partly cancelled phrase shows The followed by mat-like letters; separate the cancellation x strokes from that still-tentative underlying reading.'],
 [r'\unsure{asyeli}',r'acycli','The old partial word has a c, descending y, second c, l and dotted i: acycli.'],
 [r'\unsure{anxelementxxarx}',r'an element arr','The cancelled text reads an element arr; its visible word spaces and r shoulders can be separated from the x overstrikes.'],
 [r'(\unsure{\S}.\hand{\unsure{37}})',r'(\hand{\unsure{\S}}.\hand{3}\over{\unsure{0}}{7})','The final reference number is 37. Its section-like sign is handwritten but still graphically doubtful; a rounded old numeral beneath 7 remains tentative as 0.'],
 [r'Th\over{\unsure{is}}{us}',r'Th\over{is}{us}','The old dotted i and the old s curves are discernible below the pen us.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2678:[r'(\hand{\unsure{\S}}.\hand{3}\over{\unsure{0}}{7})','The visible final number is 37, with a still-doubtful handwritten section-like sign and a rounded old numeral beneath 7. Do not replace this by the witness’s page reference.','correct transcription'],
 2680:[r'\over{\unsure{f}}{f}or','The live f is pen; the old impression is not secure enough to settle as an opening parenthesis.','correct transcription'],
 2682:[r'Th\over{is}{us}','The typed is under the replacement us is recoverable.','correct transcription'],
 2683:[r'over e\hand{,} \deleted{...}','The visible comma precedes the large boxed-and-diagonally-cancelled passage. No period replaces it on the scan.'],
 2685:['insuring','The source clearly types insuring.']
 },'unsure':[[r'in $A^{\hand{\wedge}}$','The words and A are legible; the upper mark is a separate pen caret.'],[r'\over{\unsure{f}}{f}','The new f is secure; the old lower impression remains doubtful.'],[r'\unsure{The mat}','The underlying phrase remains only partly secure after the cancellation strokes are distinguished.'],['acycli','The partial word acycli is legible under the overstrike.'],['an element arr','The cancelled words and the final arr fragment are readable.'],[r'\hand{\unsure{\S}}','The sign is a handwritten S-like section sign, but its exact glyph is still uncertain.'],[r'37; old numeral under 7: \unsure{0}','The new 3 and 7 are clear; the old rounded impression under 7 is not.'],[r'\unsure{$e_0=e_1$ i.e. I=$e_0$xI}','The heavily overtyped and further boxed cancellation still prevents recovery of the entire formula; retain the original tentative span.'],['is','The old dotted i and s survive beneath the added us.']],
 'illegible':[],
 'notes':[
 'The final reference number is 37. The S-like section glyph remains doubtful, and the rounded prior numeral under 7 is newly retained with uncertainty.',
 'The new f is pen; lower remnants favour a typed f but do not settle the old character.',
 'The old letters is beneath the handwritten us are recovered.',
 'Give rise to, in A-hat, acycli and an element arr are recovered. The The mat fragment and the long old formula remain uncertain; no missing words are invented.',
 'The full block from unless through p.53 is bounded by pen lines and crossed by two diagonals. Its trivial insertion is typed, as transcribed.',
 'The endpoint-intersection glyph is a thick rounded handwritten cap, clearly unlike a typewriter caret.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_067:1','before':'this condition follows from the existence of the homotopy and the sections of any a in A over e','after':'this condition follows from the existence of the homotopy and the sections of any a in A over e','decision':'retain apparent authorial overstatement','reason':'After cancellation of the following exception paragraph, this assertion remains live. With A terminal and I=e, the contraction/section assumptions hold but the two coincident endpoints are not disjoint. Preserve the source and discuss the qualification in the guide.','line':25}],
 'evidence':'Both original halves and nine local details inspected. The proposition obtains total asphericity by contracting each representable through the fixed homotopy interval. Several machine-cancelled readings are recovered, including in A-hat and acycli. The reference points to 37, though the section glyph and an old numeral remain uncertain. The endpoint intersection is a rounded pen cap. The complete exception discussion is boxed and diagonally deleted, including the comparison with p.53. The preceding general claim about endpoint separation remains live and is flagged separately as too broad without its cancelled exception. In the terminology paragraph, Thus overwrites a readable This, the margin X is present, and insuring remains literal.'})

key='ps_134-3_068';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'A\^{}',r'$A^{\hand{\wedge}}$').replace(r'A\hat{}',r'A^{\hand{\wedge}}')
 for macro in ('to','subset','in','emptyset'):
  new=re.sub(r'\\'+macro+r'(?![A-Za-z])',r'\\hand{\\'+macro+'}',new)
 if new!=line:edits.append([line,new,'Repair text-mode empty accents and nested math delimiters; mark the scanned carets, arrows, inclusion/membership and empty-set signs as hand, retaining typed letters.'])
edits += [
 [r'\mspage{68}',r'\mspage{\hand{68}}','The folio is handwritten.'],
 [r'\margin{\unsure{w.t.c. good in the} \illegible{1} \unsure{for $\Delta$!}}',r'\margin{w.t.c. good \unsure{notion} for \unsure{$\Delta^{+}$}}','Rotation shows w.t.c., good and for securely. The intervening cursive word is tentatively notion; the final raised cross is not an exclamation mark, but its precise superscript remains doubtful. Do not invent an additional unread word.'],
 [r'\hand{\unsure{$(^{15})$}}',r'\hand{$(^{45})$}','The first numeral has a crossbar and descending right stem; the raised call is 45, not 15.'],
 [r'M\hand{\unsure{$\check{}$}}ore',r'M\ensuremath{\overset{\hand{\scriptscriptstyle\smile}}{\mathrm{o}}}re','The small pen mark is a curved cup above the o, rather than a check after M; represent its visible shape and placement without assigning a verbal meaning.'],
 [r'\unsure{ly}',r'ly','The cancelled l stem and y descender are both clear.'],
 [r'indeed\inserted{a}',r'indeed\inserted[typed]{a}','The raised a is typed above the pen placement slash.'],
 [r'homot\hand{o}py',r'homot\over{o}{o}py','The pen o lies over an earlier typed o rather than in a blank.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2689:['not necessarily an elementary one','Necessarily is fully typed, with the ly ending.'],
 2693:['(presumably we will not have to work with this condition really)','The typed parenthetical is live and not crossed out; retain it despite omission in the witness.'],
 2694:[r'\hand{$(^{45})$}','The raised handwritten call reads 45 on enlargement.','correct transcription'],
 2695:[r'\margin{X}','The pale handwritten X is present beside the wide-sense terminology.'],
 2696:[r'\margin{w.t.c. good \unsure{notion} for \unsure{$\Delta^{+}$}}','Two rotated enlargements establish the short structure and rule out an exclamation mark. The faint word and raised cross remain uncertain.','correct transcription'],
 2702:[r'\inserted[typed]{a}','The added a is a typewriter impression above a pen placement mark.','correct transcription'],
 2706:['endowed with final element','There is no article before final element.'],
 2708:[r'Ker $\hand{\delta}_o,\hand{\delta}_1 = \hand{\emptyset}_{A^{\hand{\wedge}}}$','The scan has no parentheses around the two delta arguments; their first subscript is the round o/zero form, retained as the source transcription’s o.']
 },'unsure':[[r'w.t.c. good \unsure{notion}','The abbreviation and good are clear; the faint cursive word is tentatively notion, not securely in the.'],[r'for \unsure{$\Delta^{+}$}','For and Delta are clear. The raised cross is not an exclamation mark but its precise intended sign remains uncertain.'],['45','The first numeral is a crossed 4; the second is 5.'],[r'\overset{\hand{\scriptscriptstyle\smile}}{\mathrm{o}}','The pen cup is visibly above the o, with no angular check stroke.'],['ly','The cancelled l and y are readable.']],
 'illegible':[[r'\unsure{notion}','There is a single faint cursive word after good; the supposed extra unread word is not a distinct additional span. Retain the tentative reading notion.']],
 'notes':[
 'The margin is w.t.c. good, a faint word tentatively notion, and for Delta with a raised cross. The uncertain word and superscript are retained; no extra word is invented.',
 'The handwritten call is 45, with raised digits inside long parentheses.',
 'The mark is a small curved cup above the o of More, reproduced as a graphic accent.',
 'The old ending ly after general is legible and remains machine-cancelled.',
 'The cancelled za after modeli and r after asphe are partially clipped but retain the visible letter shapes expected by those readings; no extra clipped character is supplied.'
 ],'evidence':'Both full halves, seven detail crops and a second enlarged rotation of the margin inspected. The paragraph distinguishes strict, wide-sense and local test categories and provisionally extends the terminology to general topoi. Its parenthetical presumably statement is uncancelled. The handwritten call is 45. The marginal note is partly recovered but its notion-like word and Delta superscript remain doubtful. The small mark over More is a cup over o, and the added article after indeed is typed. The counterexample proposal literally says endowed with final element, writes Ker without parentheses and preserves squarrable; the final word is clipped after carte as recorded.'})
