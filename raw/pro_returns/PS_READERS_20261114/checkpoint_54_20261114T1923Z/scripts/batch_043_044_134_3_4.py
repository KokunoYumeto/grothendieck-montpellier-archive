import json,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,TEXT

def commit(c):
 (OUT/'review_notes'/f"{c['key']}.json").write_text(json.dumps(c,ensure_ascii=False,indent=2))
 save_review(c)

key='ps_134-3_043';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for n,l in enumerate(s.splitlines(),1):
 a=l.replace(r'A^{\wedge}',r'A^{\hand{\wedge}}').replace(r'C^{\wedge}',r'C^{\hand{\wedge}}')
 if a!=l:edits.append([l,a,f'The presheaf carets on source line {n} are small pen additions, separate from the typed category letters.'])
edits += [
 [r'\unsure{with}','with','The live word reads with despite the machine overprint on w.'],
 [r'\unsure{asphéric|aspheric}','asphéric','A distinct acute accent stands above e; the accented source spelling is retained.'],
 [r'\unsure{transforms}','transforms','The live first letter is t over an older j-like form, and the full word transforms is legible.'],
 [r'$\underline{e}_o \hand{\wedge} \underline{e}_1',r'$\underline{e}_o \hand{\cap} \underline{e}_1','The intersection sign is a rounded cap, not an angular wedge.'],
 [r'$e_o \hand{\wedge} e_1 = \emptyset$ .',r'$e_o \hand{\cap} e_1 = \emptyset$ .','The repeated intersection sign is a rounded cap.'],
 [r'$e_o \hand{\wedge} e_1 = \emptyset_{\hand{\mathcal{A}}}',r'$e_o \hand{\cap} e_1 = \emptyset_{\hand{\mathcal{A}}}','The last displayed-in-prose intersection sign again has a rounded cap shape.'],
 [r'\margin{($A^{\hand{\wedge}}$) circled}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {$A^{\wedge}$};\end{tikzpicture}}}','Replace the editorial word circled by the actual oval around the handwritten A-caret.'],
 [r'\margin{(sieve) circled}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,inner sep=3pt] (n) {sieve};\end{tikzpicture}}}','Reconstruct the circled marginal sieve as an oval graphic without invented parenthesized editorial prose.'],
 [r'category\inserted{C}',r'category\inserted[typed]{C}','The interlinear capital C is typed; the adjacent comma and positioning curve are handwritten.'],
 [r'M\over{\illegible{1}}{o}re',r'M\over{\unsure{Q}}{o}re','The older letter has a round body and descending tail resembling Q; it remains tentative below the corrective o.']
]
commit(dict(key=key,edits=edits,diffs={
2211:['it follows','The typed statement proceeds directly to the equation without that.'],
2216:[r'category\inserted[typed]{C}\hand{,}','The C is typed above category; the comma is penned.','correct layer attribution'],
2217:[r'crible [=sieve]','The inline insertion has square brackets, and a separate oval encloses sieve in the margin.'],
2220:['handwritten deltas, caps, arrows, carets and category symbols','The signs originally called wedges at the three intersections are visibly rounded caps; other hand symbols retain their separate provenance.','correct intersection glyphs'],
2221:['oval enclosing A-caret','The handwritten A with a small caret sits inside a closed marginal oval; the editorial word circled is removed.','reconstruct graphic'],
2222:['oval enclosing sieve','The handwritten word sieve is enclosed by a marginal oval, reconstructed graphically.','reconstruct graphic']
},unsure=[
['with','The live w and following ith are readable through overtyping.'],
['asphéric','The acute accent over e is separately visible.'],
['transforms','The live word reads transforms even though an older j-like descender survives.']
],illegible=[
[r'\illegible{1}','The heavy handwritten 3 obscures its preceding digit.'],
[r'\illegible{1}','The old character below object is densely pen-cancelled and cannot be recovered.'],
[r'\unsure{Q}','A round letter with a descending tail suggests Q, but its overprint makes this a doubtful reading.']
],notes=[
'The word with is legible; only the w is overtyped.',
'The typed ly small in any case.) is a continuation above the line; the long curve places it after essential and does not cancel supposed to be essential.',
'The old character under the pen 3 remains illegible.',
'The accent over e is distinct, so asphéric is retained literally.',
'Transforms is legible as the live reading. The overtyped letter in subobjects leaves that whole word readable.',
'The complete final three-line passage is pen-cancelled by horizontal and diagonal lines. The nested machine cancellation of has the advantage remains inside it.'
],evidence='Both halves inspected with a detail sheet for with, T3, asphéric, transforms, the old object, More and the inserted C. The continuation essential/ly small is typed above the line and placed with pen curves. The three intersection glyphs are rounded caps. Two oval marginal annotations are reconstructed rather than described as circled. The C after category is typed; object and [=sieve] are cursive. The Lawvere-element display retains the slash notation I x F / F and the representability insertion. The three-line ending is completely cancelled, including the earlier machine deletion within it. The old numeral and old object remain unreadable, and the old More letter is only tentatively Q.'))

key='ps_134-3_044'
commit(dict(key=key,edits=[
 [r'te\unsure{st} categories','test categories','The lower overlapping s and t are readable as the end of test.'],
 [r'\xout{xxpax}',r'\xout{\unsure{topos}}','The crossed base word has a clear central p and a shape compatible with topos; it is not a literal sequence xxpax. The full old reading remains doubtful.'],
 [r'\hand{(}\inserted{34}\xout{xxxx}\hand{)}',r'\hand{(}\inserted{34}\xout{\illegible{1}}\hand{)}','The row of x-overstrikes conceals an older group beneath the hand call 34; the x characters should not be presented as a securely read old word.'],
 [r"\xout{xxx}\inserted[typed]{yesterday's}",r"\xout{the}\inserted[typed]{yesterday's}",'The old word the is visible through the three cancelling x characters.'],
 [r'\margin{/ (!35)}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\draw (0,-.35)--(.15,.55);\draw (0,-.15)--(.12,-.27);\node[anchor=west] (n) at (.28,.18) {(!35)};\end{tikzpicture}}}','Reconstruct the left-margin long stroke and the single legible (!35) call in their relation.'],
 [r'exist\inserted{\unsure{(!35)}}',r'exist\deleted{\illegible{1}}','The mark after exist is a dense pen cancellation with no readable (!35); the actual new call is in the margin. Remove the duplicate inferred call and retain the unreadable cancelled group.'],
 [r'\xout{xx}\inserted[typed]{from}',r'\xout{in}\inserted[typed]{from}','The old in is visible below the x-overstrike and the typed replacement from.'],
 [r'fibere\over{\illegible{1}}{d}',r'fibere\over{a}{d}','The old a has a visible round body below the added d ascender.'],
 [r'mo\over{\illegible{1}}{n}omorphism',r'mo\over{i}{n}omorphism','The old i is indicated by its surviving dot and straight stem inside the new n.'],
 [r'c\over{\illegible{1}}{o}fibration',r'c\over{\unsure{o}}{o}fibration','The base appears to be a round o, but the thick retracing prevents secure recovery.'],
 [r'A\^{} defined',r'$A^{\hand{\wedge}}$ defined','The small raised caret after A is handwritten, not an ordinary text accent.'],
 [r'between  A\^{} and',r'between  $A^{\hand{\wedge}}$ and','The second small presheaf caret is also a pen addition.']
],diffs={
2226:['handwritten call (34) over an obscured cancelled group','Only the call is present; the witness footnote prose is not on this page.'],
2232:['single marginal (!35), with a cancelled unreadable body mark after exist','The margin supplies a clear exclamation-marked 35 call. The body lattice is a cancellation, not a second legible copy of the call.','correct transcription and placement']
},unsure=[
['st','The displaced typed s and t are readable.'],
[r'\unsure{--}','The few tiny marks at the left edge may be dashes or stray marks; they remain doubtful.'],
['marginal (!35); body cancellation unreadable','The marginal call is legible; the dense crossed body mark cannot itself be read as (!35).']
],illegible=[
['a','The old a body is visible beneath the correcting d.'],
['i','The old i dot and stem survive inside the n.'],
[r'\unsure{o}','The base of the round retraced o remains uncertain.']
],notes=[
'The word test is recoverable from the lower s/t overprint. The long angled pen stroke after categories remains as a visible separator/placement mark without an inferred word.',
'The small left-edge dashes remain uncertain marks.',
'The hand closing parentheses after T1 and T3 are superposed on dense old marks; the additional outer closing parenthesis is clearly visible.',
'The legible new call is (!35) in the left margin. After exist the old group is pen-cancelled and unreadable; the duplicate inferred call has been removed. The line-end one remains clipped.',
'The small h beneath The is a pen correction/retracing of the word and is retained.',
'The old in below from is recoverable. The a cancellations before well known and (M,W) remain machine deletions.',
'The tiny dot between extra and condition is isolated and supplies no defensible textual character.',
'The noted right-edge truncations are retained without inferred completions.'
],evidence='Both halves inspected, with detail crops of the old word under modelizers, calls 34 and 35, the words under yesterday\'s/from, and fibered/monomorphism/cofibration corrections. Test is legible. Modelizers, yesterday\'s, from and practical are typed interlinear additions; with is cursive. The single clear (!35) is marginal, while the mark after exist is heavily crossed and cannot be read; the earlier duplicated call is corrected. The text literally claims finite direct and inverse limits in (Hot), says expanding, looking, occured and does\'nt, and uses who of j_A; none is silently repaired. The old a under d and i under n are recoverable; the o base remains doubtful.'))
