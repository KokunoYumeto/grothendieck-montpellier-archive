import sys,re,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
key='ps_134-6_079'
edits=[
 [r"(41')\xout{)}",r"(41\hand{')}\xout{)}",'The short raised prime and the new curved closure are penned; the later old typed closure is separately machine-cancelled.'],
 ['is none  other',r'is no\over{ne}{ne}  other','The final n/e have thick irregular pen retracings over the visible type, especially the enlarged loop of e. Independent inspection agrees.'],
 ['canonical isomorphism  when',r'canonical isomorphis\over[typed]{p}{m}  when','The final m lies over a regular older p with its lower descender still visible.'],
 ['  when we know',r'  \over[typed]{o}{w}hen we know','The initial w has an overlapping regular rounded o impression.'],
 [r'\hat{A},\hat{B}',r'A^{\hand{\wedge}},B^{\hand{\wedge}}','Both carets have broad joined pen strokes above and to the right of the typed letters. Preserve their hand provenance and superscript placement.'],
 [r'\hand{\varepsilon}_{\hand{A}}',r'\hand{\varepsilon}_{A}','The first epsilon is handwritten, but its subscript A has regular typewriter serifs and is plain typing.'],
 [r'\inserted{phism}',r'\inserted[typed]{phism}','The completion phism is typed above the line. The surrounding curved stroke places it after isomor, so the letters must join in the corrected reading.']
]
save_review({'key':key,'edits':edits,'diffs':{
 8425:['equally an e quivalence','The source has an, not and. Its internal gap in e quivalence is also visible and retained.'],
 8434:['an object in A','The preposition is plainly typed in, rather than the witness of.'],
 8431:['handwritten epsilon with typed subscript A','The subscript A has regular serifed type, while epsilon and the mapsto arrow are penned.','correct provenance'],
 8437:['typed interlinear phism','The completion has regular typewriter forms, with a pen placing curve.','correct provenance'],
 8424:['replaces diplomatically; replaced in corrected forms','The source types replaces. The same line correctly types replaced in the parallel parenthesis and the preceding with B construction requires that participle.','isolated typing slip recorded']
 },'notes':[
 'The old a is crossed by several irregular pen passes, and the new the is handwritten above it with a placing curve. The existing deletion-plus-insertion reading is retained.',
 'The prime and live closure are penned after the typed 41; the further old typed closure carries a regular machine x strike.',
 'The final n/e of none are pen retracings, not simply repeated typing. The final m of the later isomorphism has a typed p beneath it; the following when also has typed w over o.',
 'Both occurrences of e quivalence have a genuine internal gap, retained as scanned.',
 'Both carets in44 are handwritten, independently confirmed from their broad joined strokes. Their typed A and B stay plain, as does the serifed A subscript on the first epsilon.',
 'The pencil archive folio 79 is visible at lower left.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-6_079:replaces','before':'with B replaces by A','after':'with B replaced by A','decision':'isolated typing slip in corrected forms','reason':'The image visibly types replaces, but the same line has the correctly typed replaced in the directly parallel clause A replaced by B. Preserve the physical s diplomatically and use d only in corrected forms.'}
 ],'evidence':'Both original halves and eight enlarged panels inspected. The handwritten the replaces a crossed typed a. The revised41prime label has a pen prime and new pen closure before a separately machine-cancelled old typed closure. The final n/e of none are penned over visible typing, independently confirmed. Isomorphism has a typed p-to-m overlay and when has w over o. Both hats in44 are broad joined pen strokes above plain typed letters, also independently confirmed, while the first epsilon subscript A is regular typing. Phism is a typed interlinear completion and joins directly to isomor. The two internal gaps in e quivalence, the possessive apostrophes, the extra closing parenthesis after (B,A), and other literal source wording remain. The single replaces/replaced slip has direct same-word and parallel-construction evidence on this very line and is recorded only for corrected forms. The page establishes the symmetric set-valued cosheaf pairing, reduces it by twofold use of proposition3 to representables, and gives a*b^o=Hom_A(b,a). The final evaluation formulas continue on398.'})
v={'key':key,'before':'with B replaces by A','after':'with B replaced by A','kind':'isolated typing slip','reason':'The same line has the correctly typed replaced in the directly parallel clause A replaced by B; preserve replaces only diplomatically.','source_id':'OBS:ps_134-6_079:replaces'}
p=OUT/'records/MASTER_VARIANTS_134_3_4.json';vs=json.loads(p.read_text());vs=[x for x in vs if x['source_id']!=v['source_id']]+[v];p.write_text(json.dumps(vs,ensure_ascii=False,indent=2)+'\n')

key='ps_134-6_080'
edits=[
 [r'F \unsure{\hand{*}} b^{o}',r'F \underset{\hand{\unsure{\illegible{1}}}}{*} b^{o}','The live star has regular typewriter bars. A separate blackened pen mark lies below it; preserve that unreadable mark without asserting a cancellation or replacing the live star.'],
 [r'b^{o} \hand{\simeq} F(b)',r'b^{o} \underset{\hand{\unsure{\illegible{1}}}}{\hand{\simeq}} F(b)','A separate dark lower pen mark is visible beneath the live wave-and-bar sign. Its identity and layer chronology remain unresolved.'],
 [r'\unsure{As|We}',r'\unsure{\over[typed]{We}{As}}','The opening two cells contain regular W/A and e/s impressions. Preserve the candidate We-to-As layering under a whole doubt instead of resolving its order from grammar.'],
 [r'interested\inserted{here}',r'interested \inserted[typed]{here}','Here is typed above the line with a pen placing curve. Preserve the actual word boundary before it.'],
 [r'pairing\inserted[typed]',r'pairing \inserted[typed]','The parenthetical insertion is a separate phrase; preserve its boundary after pairing.'],
 [r'\[ A^{\wedge o} \times B^{\wedge o} \longrightarrow',r'\[ A^{\wedge o} \times B^{\wedge o} \hand{\longrightarrow}','The arrow in48 has a thick pen shaft and hand-drawn head.'],
 [r'\[ A^{\wedge o} \to B^{\wedge}',r'\[ A^{\wedge o} \hand{\to} B^{\wedge}','The first arrow of the displayed adjoint pair is penned.'],
 [r'B^{\wedge o} \to A^{\wedge}',r'B^{\wedge o} \hand{\to} A^{\wedge}','The second arrow of the displayed adjoint pair is penned.'],
 [r'\mathrm{Hom}}^{!!}',r'\mathrm{Hom}}^{\hand{!!}}','Both raised exclamation marks in the dual-equivalence display are handwritten.'],
 [r'\xrightarrow{\approx}',r'\overset{\unsure{\approx}}{\hand{\longrightarrow}}','The arrow is clearly pen-drawn. The two evenly weighted waves could be regular typing or neat pen; preserve scoped provenance uncertainty without altering the relation.'],
 [r'= B \times A \longrightarrow',r'= B \times A \hand{\longrightarrow}','The arrow of the co-pairing display is handwritten.'],
 [r'(b^{o},a) \longrightarrow',r'(b^{o},a) \hand{\longrightarrow}','The final arrow is hand-drawn and has no mapsto source bar.'],
 [r'\[ A^{\wedge o} \times B^{\wedge o}',r'\[ A^{\wedge o} \mathrm{x} B^{\wedge o}','The product mark in48 is a regular typed lowercase x, preserved as such.'],
 [r'\mathrm{Hom}}(A^{o}\times B^{o}',r'\mathrm{Hom}}(A^{o}\mathrm{x} B^{o}','The product mark in the right Hom object is a typed lowercase x.'],
 [r'\[ A^{o} \times B^{o}',r'\[ A^{o} \mathrm{x} B^{o}','The first product mark of the co-pairing domain is a typed lowercase x.'],
 [r'= B \times A',r'= B \mathrm{x} A','The second product mark of that domain is also a typed lowercase x.'],
 [r'\margin{\unsure{other description of (48) via $\times$} \unsure{cf. 397}}',r'\margin{other description (48) via $\times$ cf 397}','The rejoined and rotated pencil note has other, then description, then (48) via a cross. No separate of is visible. Independent inspection confirms description and cf397; the source has no additional of.'],
 [r'\margin{$\times$ \unsure{cf. p. 404-405}}',r'\margin{$\times$ cf p. 40\unsure{4|9}-405}','The lower pencil note has a separate cross and cf p. followed by a range ending405. The last digit of the first endpoint remains doubtful between4 and9; no separate dot after cf is visible.'],
 [r'\xout{\unsure{maps}}',r'\xout{homo}','The four lower letters resolve as h-o-m-o beneath the regular x row, rather than the draft maps.'],
 ['The symmetry',r'T\over[typed]{h}{h}e symmetry','The h has two regular lowercase h impressions at different vertical positions; retain the repeated typed layer.'],
 [r'\inserted{\uline{Case}} \hand{(}',r'\inserted{\uline{Case}} ','The long left hook before2 is continuous with the placing curve beneath Case. It is not a separate textual opening parenthesis; the short underline under Case is independently visible and remains.'],
 [r'2\textsuperscript{o}).',r'2\textsuperscript{\uline{o}}).','The small typed o has a distinct lower horizontal stroke, so its underline is preserved.'],
 ['formula(12)(page',r'formula(12\over{)}{)}(page','The closing parenthesis after12 is retraced with a thick pen stroke over its typed form.']
]
save_review({'key':key,'edits':edits,'diffs':{
 8440:[r'\unsure{\over[typed]{We}{As}} we are mainly interested','The two overprinted cells are present before the independent typed we. Their order remains doubtful; they cannot be omitted as in the witness.'],
 8444:[r'(b^o,a)\hand{\longrightarrow}\mathrm{Hom}(b,a)','The pen arrow has a head and shaft but no source bar; preserve the ordinary arrow rather than mapsto.'],
 8450:['No separate opening parenthesis before2','The apparent parenthesis is the left hook of a continuous pen placing curve. The witness omission happens to agree with the visible text, but the decision follows the curve itself.','correct placing mark'],
 8453:[r'other description (48) via $\times$; cf 397','The note was rejoined across the two halves and rotated. The word of is unsupported; description and cf397 are independently confirmed from the actual crop.','correct and retain scoped doubt'],
 8454:[r'$\times$ cf p. 40\unsure{4|9}-405','The lower note is present; its first endpoint remains uncertain and the end405 is legible.','retain scoped doubt'],
 8441:['typed interlinear here','The added word is typed and the pen curve places it before in.','correct provenance'],
 8442:['Two typed stars; pen equivalence signs and separate unreadable lower marks','The first star is regular typing. The second is also typed but has a separate dark pen mark below it, as does the following live relation.','correct provenance and preserve marks']
 },'unsure':[
 [r'\underset{\hand{\unsure{\illegible{1}}}}{*}','The live star resolves as typed; the separate lower pen mark remains unreadable.'],
 [r'\unsure{\over[typed]{We}{As}}','The W/A and e/s forms are visible, but their layer order is not securely established.'],
 [r'other description (48) via $\times$','The rejoined crop and independent inspection support other description (48) via the cross. No separate of is visible.'],
 ['cf 397','The visible terminal angled7 and the independent inspection settle cf397; no separate dot after cf is visible.'],
 [r'cf p. 40\unsure{4|9}-405','The end405 is clear, while the last digit of the first endpoint is less secure.'],
 ['homo','The first old letter has a tall h stem, followed by o, the two humps of m, and a final rounded o.']
 ],'notes':[
 'The opening word contains overlapping regular We/As impressions. Its order is not resolved merely by the sentence grammar.',
 'Both stars of47 have regular typewriter forms. A separate unreadable pen mark lies under the second star, and another under the following live handwritten relation. Neither is silently discarded or assigned a secure cancellation boundary.',
 'The Hom display arrow and both exclamation marks are clearly penned. The two evenly weighted waves do not securely distinguish typing from neat pen, independently confirmed; only their provenance remains doubtful.',
 'Both faint pencil notes were separately enlarged and rotated; the upper one was rejoined across the two halves. Its unsupported of is removed; description and cf397 are independently confirmed, while the lower endpoint retains4/9 doubt on its last digit and405 resolves.',
 'The main number398 is typed, and the archive folio80 is pencilled at lower left.'
 ],'evidence':'Both original halves, eleven detail panels and two separate enlarged rotated pencil-note panels inspected; the upper note was rejoined across the image split. The opening word has uncertain typed We/As layers. Here is typed above the line and needs a word boundary; the parenthetical bi-sheaf insertion is also separate from pairing. Both stars in47 are typed, with distinct unreadable lower pen marks under the second star and its following handwritten relation. The display arrows throughout this page are pen-drawn, and the dual-Hom exclamation marks are handwritten. Its approximate sign has unresolved typed-versus-neat-pen provenance, independently confirmed. Product marks in the relevant displays are literal typed x letters. The final co-pairing arrow lacks a mapsto bar. The upper pencil note has no independently visible of; description and cf397 are independently confirmed. The lower note clearly ends405 but its first endpoint retains a scoped4/9 doubt on its last digit. The cancelled word before maps resolves as homo. The initial h of The symmetry has repeated typed impressions, and the parenthesis after12 is pen-retraced. The Case insertion has an independent underline plus a longer placing curve whose left hook is not a textual parenthesis; the ordinal o is underlined. The page gives the representable evaluation formulas, sketches the opposite-variance bi-sheaf and common category E(A), and begins the Ab specialization without completing it on this page.'})

for key in ['ps_134-6_079','ps_134-6_080']:
 s=(OUT/'checked_pages'/f'{key}.tex').read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);level=0
 for m in re.finditer(r'(?<!\\)[{}]',s):
  level+=1 if m.group()=='{' else -1
  assert level>=0,(key,m.start())
 assert level==0,(key,level)
