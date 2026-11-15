import sys,json,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-4_060'
marks=r'\unsure{T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\underset{\hand{\scriptscriptstyle,}}{\mathrm h}}$e}'
edits=[
 ['present,  in terms',r'present,  i\over[typed]{a}{n} terms','The n has a round a-shaped lower typed impression.'],
 [r'h\xout{mm}',r'h\xout{\unsure{om|mm}}','The cancelled run begins with a rounded cell, but its two lower letters cannot securely be separated as om or mm.'],
 [r'\inserted{finite}',r'\inserted[typed]{finite}','Finite is typed above the line and has a pen placing curve.'],
 [r'\unsure{\over{in}{by}|in}',r'\over{\unsure{in}}{by}','The live by is clear, including its long y descender; the lower in remains tentative. Preserve the resulting source phrase by terms.'],
 ['The generalities',marks+' generalities','The recurring paired upper marks and lower spot around h are retained under a provenance doubt.'],
 [r'$W\subset F\hand{\ell}(M)$',r'$W\hand{\subset} F\over{l}{\ell}(M)$','The inclusion sign is penned, and Fl has typed l under a separate pen slash.'],
 [r'next\inserted{, \unsure{one},}',r'next\inserted{, one,}','The handwritten o, n and final looped e resolve, along with the flanking commas.'],
 [r'connec\xout{\illegible{1}}%'+'\n'+r'ted',r'connec\xout{t\illegible{1}}\hand{-}%'+'\n'+r'ted','The old t is visible before the clipped remaining cancelled cell. A short pen continuation hyphen is separately visible above the cancelled run; preserve it diplomatically and join the word in the explicit corrected variant.'],
 [r'p\unsure{\over{p}{o}}or',r'p\unsure{\over[typed]{p}{p|o}}or','The second cell has a clear typed p descender. A distinct live o impression cannot be separated securely, so retain p/o and the uncertainty of the putative overprint.'],
 [r'suppose\unsure{\over{\illegible{1}}{d}}',r'suppose\over{d}{d}','The old typed d and its dark pen retracing are separately recognizable.'],
 [r'\margin{60.}',r'\margin{\over{\unsure{59}}{60}.}','The section number is penned over faint older digit forms; 59 is a candidate but remains doubtful.'],
 [r'every\xout{\illegible{1}}',r'ever\over{y}{y}\xout{\unsure{it}}','The y is pen-retraced. The cancelled following lower letters look like it but are not fully separable beneath the x row.'],
 [r'A \unsure{\hand{$\circ$}}made',r'A $\underset{\unsure{\hand{\circ}}}{\mathrm m}$ade','The small round mark is below the first m of made, not an independent symbol preceding the word; preserve its uncertain provenance and form at that position.'],
 [r'\inserted{On the other hand,} \unsure{\over{The}{the}}',r'\inserted{On the other hand} \over{The}{the}','The live pen the over typed The is legible. The apparent final comma belongs to the upturned end of the continuous placing curve, with no separate punctuation.'],
 [r'\deleted{\unsure{however}}',r'\over{\unsure{on the other hand}}{however}','However is visibly live handwriting over the beginning of a longer typed phrase; the later part of that phrase is crossed. On the other hand is the strongest old candidate, retained as a whole-span doubt. Do not delete the live however.'],
 ['The standart arguments',r'T\over[typed]{h}{H}e standart arguments','The h has a regular capital H impression over it.']
]
joinbefore=r'connec\xout{t\illegible{1}}\hand{-}%'+'\n'+'ted'
conf={'key':key,'edits':edits,'diffs':{
 4227:['parenthesis followed by namely','There is no comma after the closing parenthesis.'],
 4228:['objects such that','There is no X after objects.'],
 4231:[r'\over{\unsure{in}}{by} terms','The live b and descending y are clear; do not substitute the witness in.'],
 4232:['about relationship','No the is typed after about.'],
 4233:[r'next\inserted{, one,}','The handwritten one and both commas are visible; the word is absent from the witness.'],
 4237:['who was supposed','The source plainly types who.'],
 4238:['Marginal rewritten number 60; no section title','Only the section number occurs; do not import the witness title.'],
 4242:[r'\over{The}{the} condition','The live handwritten the remains after the added On the other hand phrase, although the witness omits it.']
 },'unsure':[
 [r'\over{\unsure{in}}{by}','The live by resolves; the earlier typed in remains doubtful under it.'],
 ['one','The three pen letters resolve in the enlarged panel.'],
 [r'\unsure{\over[typed]{p}{p|o}}','The second cell retains a visible p descender; an independent live o overprint is not secure.'],
 [r'\over{d}{d}','Both the typed d and its pen retracing are visible.'],
 [r'\underset{\unsure{\hand{\circ}}}{\mathrm m}','The round mark is below m, with its precise form and pen-versus-typed provenance uncertain.'],
 [r'\over{The}{the}','The lower typed The and live pen the can be separated.'],
 [r'\over{\unsure{on the other hand}}{however}','The new handwritten however is live. The longer crossed old phrase remains tentative and is retained as a whole-span doubt.']
 ],'illegible':[
 [r't\illegible{1}','The old t is visible, followed by an unreadable cancelled remainder at the clipped edge.'],
 ['d','The lower typed d resolves beneath the pen retracing.'],
 [r'\unsure{it}','The old two-letter candidate it is partly visible through the x row, but remains uncertain.']
 ],'notes':[
 'The first in has typed n over a, with the lower rounded a shape visible.',
 'The extra run after h is machine-cancelled; its om/mm reading remains uncertain.',
 'The live word before terms is by; the lower in is still tentative. Finite above the preceding line is typed.',
 'The generalities has the recurring paired upper marks and lower spot whose provenance is uncertain. The last The has a regular H over h.',
 'The Fl l is typed with a pen slash; the inclusion is also handwritten.',
 'The added one and its commas resolve in the enlarged panel.',
 'The old t after connec resolves, but the clipped following cancelled cell remains unreadable. A separate short pen continuation hyphen is visible above it.',
 'The second poor cell retains a typed p descender; whether an o was separately overprinted remains uncertain. Both layers of the final d of supposed resolve.',
 'Every has a pen y retracing, followed by a machine-cancelled tentative it.',
 'The round mark is below the first m of made; its exact provenance remains doubtful.',
 'The live handwritten however replaces a longer crossed typed phrase. On the other hand is retained only as a tentative old reading; cancelling however would discard visible live text.',
 'The continuation begins with a baseline hyphen in the left margin before ted ones; its position is preserved in the source.',
 'The lower pencil archive folio 60 is distinct from the rewritten section number 60 above.'
 ],'extra_records':[{'source_id':'OBS:ps_134-4_060:connected_join','before':joinbefore,'after':'connected','decision':'apply physical continuation in corrected forms','reason':'Join connec/ted after removing the cancelled old letters and the pen line-end hyphen; retain the pen mark in diplomatic form.'}],
 'evidence':'Both original halves and fourteen enlarged panels inspected. In has typed n over a. The cancelled extra run after h remains om/mm. Finite is typed interlinearly, whereas assuming is penned. The live by before terms resolves, but the lower in remains tentative. The source relationship has no added article; the Fl slash and inclusion are pen. The insertion one and both commas resolve. The clipped connected continuation has a readable cancelled t, unreadable remainder and separate pen hyphen. Poor retains an unresolved p/o typed-layer question, while supposed has a clear pen d over typed d. The rewritten section number has a doubtful old layer. Every has pen y and a tentative cancelled it. The small circle is positioned below m in made. On the other hand has no independent final comma: its hook is a placing curve, and the live lowercase the is clear over typed The. Most materially, however is live handwriting over a longer cancelled old phrase; the old phrase is only tentatively on the other hand. No speculative mathematical correction is made to the generalization about arbitrary pi-zero functors.'}
save_review(conf)
v={'key':key,'before':joinbefore,'after':'connected','kind':'author word join','reason':'Join the physical connec/ted continuation, omitting the cancelled old letters and the penned line-end hyphen only in corrected forms.','source_id':'OBS:ps_134-4_060:connected_join'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';old=json.loads(p.read_text());old=[x for x in old if x['source_id']!=v['source_id']];old.append(v);p.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);n=0
for m in re.finditer(r'(?<!\\)[{}]',s):
 n+=1 if m.group()=='{' else -1
 assert n>=0,(key,m.start())
assert n==0,(key,n)
