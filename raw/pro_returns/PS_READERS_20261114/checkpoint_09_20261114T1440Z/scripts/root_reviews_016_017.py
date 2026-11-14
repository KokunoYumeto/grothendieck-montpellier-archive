from review_root import review, macro_occurrences, TEXT
import re

def ds(key,name,reasons,resolved=None):
    s=(TEXT/'transcription/ps_pages'/(key+'.tex')).read_text();o=macro_occurrences(s,name);resolved=resolved or {}
    assert len(o)==len(reasons),(key,name,len(o),len(reasons))
    return [(resolved.get(i,x['source']),'doubt resolved' if i in resolved else 'doubt retained',reason) for i,(x,reason) in enumerate(zip(o,reasons),1)]

def arrow_changes(key,changes):
    s=(TEXT/'transcription/ps_pages'/(key+'.tex')).read_text()
    for a,b,_ in changes:s=s.replace(a,b,1)
    for line in s.splitlines():
        new=re.sub(r'(?<!\\hand\{)\\(longrightarrow|rightarrow|longmapsto|mapsto|to)\b',lambda m:r'\hand{'+m[0]+'}',line)
        if new!=line:changes.append((line,new,'The arrows on this line are hand drawn on the scan; their shafts and heads are now marked as handwriting without changing direction or endpoints.'))
    return changes

k='ps_134-2_016'
changes=[
    (r'\unsure{and}',r'\deleted{\unsure{and}}','The typed and before the added list is crossed by diagonal pen strokes; it must not remain live text. The obscured letters remain doubtful.'),
    (r'\unsure{\hand{,}}',r'\hand{,}','The small right-edge mark above expressing is visibly a curved comma.')
]
src=(TEXT/'transcription/ps_pages'/(k+'.tex')).read_text()
o=next(o for o in macro_occurrences(src,'hand') if o['argument'].startswith(r'$\left\{'))
changes.append((o['source'],r'\hand{'+o['argument'][1:-1]+'}','Mechanical: remove dollar delimiters nested inside the displayed handwritten conditions.'))
review(k,changes=arrow_changes(k,changes),doubts={'unsure':ds(k,'unsure',[
    'The final letters in the heavily typed demonstrative remain ambiguous between the recorded alternatives.',
    'The typed conjunction is cancelled by pen; its obscured letters remain doubtful.',
    'The handwritten u/v form in the third source term remains ambiguous even in enlargement; the mathematics is not used to decide it.',
    'The isolated curved mark at the far right is a comma.',
    'The cancelled letter inside defined is too dark to settle.',
    'The overtyped letter inside inversion remains doubtful.',
    'The first right-side factor has a dark overprint/retracing; the proposed u-to-v replacement remains doubtful.',
    'The cancelled letter in complemented remains obscured.',
    'The ending of ensue has a dark extra/retraced stroke; the final letter remains marked.'
],{4:r'\hand{,}'}),'illegible':[]},notes=[
    'The upper folio is handwritten 4 and the lower folio handwritten 16. Archive site 17 carries folio 3, so the archival order reverses these two leaves.',
    'The typed demonstrative remains too overworked to settle that versus this.',
    'Enlargement does not securely distinguish u-prime from v-prime in the third source term; the doubt remains.',
    'The right factor is overprinted/retraced; its existing uncertainty remains. Both factors on the left carry separate inversion marks on the scan.',
    'The isolated hand mark above the expressing line is a clear comma.',
    'The end of ensue remains dark and overworked; the source nevertheless continues natural-ly, not naturality.',
    'The cancelled e of withe remains identifiable. The other three internal overstrikes remain doubtful.',
    'The faint background marks beside the Godement relation are reverse-side show-through, not forward-facing mathematical content.'
],summary='Both halves and enlarged Godement/inversion crops reviewed. Restored cancellation of and, resolved the isolated comma, marked pen arrows, and repaired nested math delimiters. Eight doubts remain. The archive places this folio4 before folio3; both numbered leaves are preserved in archive order. Apparent tautological inversion wording is preserved.',differences={
56:('as set of objects','the typescript reads as our transcription','The typed phrase has no a after as; the witness inserts it.'),
57:(r'F_{i-\hand{\ell}+1} \hand{\to} \ldots F_{i-1}','the typescript reads as our transcription','There is an arrow before the dots but no arrow between the dots and the next F term on the scan.'),
59:(r'u,u\prime,v,v\prime\in F_i','the typescript reads as our transcription','The handwritten list has four variables, with a single prime on the last v and a membership sign; the witness string has a malformed extra prime/in sequence.'),
61:(r's_\nu(\unsure{u\prime|v\prime})','the typescript reads as our transcription','The pen form remains ambiguous between u and v. The arXiv v-prime cannot settle the scan.'),
62:(r'\deleted{implying}','the typescript reads as our transcription','The typed implying is struck horizontally and replaced above by expressing; the witness retains implying.'),
63:(r'\inserted{expressing}','the typescript reads as our transcription','The handwritten replacement expressing is fully visible above the cancelled word; the witness omits it.'),
65:(r'(\check v *_\ell \check u)=\check{\unsure{\over{u}{v}}} *_\ell \check u','the typescript reads as our transcription','The scan contains a complete right-hand product, with an uncertain overwritten first letter; arXiv replaces that product by a question mark. The separate checks on both left-hand factors are preserved.'),
71:(r'will ensu\unsure{e} natural-ly by','the typescript reads as our transcription','The next line starts ly by, so the word is naturally, not the witness naturality. The preceding overworked ending remains doubtful.')
})

k='ps_134-2_017'
src=(TEXT/'transcription/ps_pages'/(k+'.tex')).read_text()
old=r'\[ k^i_1 : F_i \longrightarrow F_{i+1} \qquad (i \in \underline{N}) \quad \hand{, notation $id_a = k^i_1(a)$,} \]'+'\n'+r'and the symmetry map (passage to the inverse) \hand{$\check{u} = inv_i(u)$}'
new=r'\[ k^i_1 : F_i \longrightarrow F_{i+1} \qquad (i \hand{\in} \underline{N}) \]'+'\n'+r'\margin{, notation $id_a = k^i_1(a)$, $\check{u} = inv_i(u)$}'+'\n'+r'and the symmetry map (passage to the inverse)'
changes=[
    (r'\mspage{2)}',r'\mspage{\hand{2)}}','The upper-left 2) is handwritten.'),
    (r'\margin{3}',r'\mspage{\hand{3}}','The centered handwritten 3 is a folio, not a prose marginal note; the upper-left 2) is also retained.'),
    (r'\unsure{nction|notion}',r'nction','The enlarged typewritten second letter is an open c, not a closed o.'),
    (r'\unsure{\in}',r'\hand{\in}','The membership symbol is a clear hand-drawn epsilon-like inclusion sign; the typeset natural-number symbol remains typed.'),
    (old,new,'The two handwritten notation formulas occupy one right marginal block beside the maps. They are restored as a marginal note; the membership sign in the identity-map domain is also handwritten.'),
    (r'\inserted{, etc}',r'\hand{,} \inserted[typed]{etc}','The comma is handwritten, but etc above the line is monospaced typing with a placement curve.'),
    (r'(F_i, \unsure{s}^i_{\hand{\ell}})_{u,v}',r'(\underset{u,v}{F_i}, \over[typed]{\unsure{s}}{t}^i_{\hand{\ell}})','Enlargement shows t as the overlying typed letter in the first factor; the underlying character remains doubtful. The typed u,v stand below F_i, not as an index after the closing parenthesis.'),
    (r'\inserted{$\overset{i}{\underset{\ell}{*}}$-composition of}',r'\inserted[typed]{$\hand{\overset{i}{\underset{\ell}{*}}}$-composition of}','Composition of is typed above the cancelled operation; the star and its labels are handwritten.')
]
review(k,changes=arrow_changes(k,changes),doubts={'unsure':ds(k,'unsure',[
    'The terminal punctuation at the far right of the first line remains clipped/indistinct.',
    'The enlarged second letter is open on the right and reads c; the typed word is nction.',
    'The membership sign is legible and handwritten.',
    'The very faint opening curve before F_i may belong to background/show-through; its doubt remains.',
    'The third letter of exehan/exchan is densely overtyped; the alternative remains.',
    'The overlying typed letter is t; the underlying s-like trace remains uncertain and is now represented as an overwritten doubtful letter.'
],{2:'nction',3:r'\hand{\in}',6:r'\over[typed]{\unsure{s}}{t}'}),'illegible':ds(k,'illegible',[
    'The old mark between the and the replacement composition expression is heavily crossed and cannot be read.',
    'The cancelled prefix before the final source equation is too densely worked to recover.'
])},notes=[
    'The upper-left 2), centered3 and lower-left17 are all handwritten. The centered3 is encoded as a source folio; all three are preserved. It precedes site16’s folio4 in the letter’s internal sequence.',
    'The original closing parenthesis after isomorphism remains visible; the new hand parenthesis abuts it without a secure cancelling stroke. Both remain.',
    'Nction is clear in enlargement; the heavily overtyped third letter of exehan/exchan remains uncertain.',
    'Both membership symbols have pen-drawn curves and are now marked as handwriting.',
    'The first factor ends with an overprinted t, with an uncertain old s-like form. U,v are typed below the F_i. The dark final s of gets is retained as s without inventing an earlier reading.',
    'The small strokes over They and The, and the blot in the first relation, do not establish additional words. Their surrounding printed readings remain.',
    'The handwritten i is attached to the star in the display and remains there, not in the preceding prose.'
],summary='Both halves and enlarged formulas/letters checked. Restored handwritten arrow and membership provenance, typed interlinear material, the marginal notation block and folio3. Resolved nction; recovered overprinted t in the first composition factor, retaining doubt on its underletter. Six doubts remain. The bottom handwritten target formula retains s_1 on its second right-side factor.',differences={
79:(r'\deleted{for} \hand{as}','the typescript reads as our transcription','The word for is crossed out and replaced by handwritten as, not the witness to.'),
81:(r'id_a = k^i_1(a)','the typescript reads as our transcription','The marginal identity notation visibly begins id; the witness omits the initial i.'),
84:('composition','the typescript reads as our transcription','The typed word is composition; the witness compoisition introduces a transposition absent from the scan.'),
88:(r'(u,v)\longmapsto(v\overset{i}{*}_\ell u:(\underset{u,v}{F_i},\over[typed]{\unsure{s}}{t}^i_\ell)\times_{F_{i-\ell}}(F_i,s^i_\ell)\longrightarrow F_i','our transcription corrected','The first map label is overprinted t, while its old s-like form remains doubtful. U,v are lowered under the first F_i. The source also has a handwritten i above the composition star and lacks the witness closing parenthesis after u.'),
89:(r'\margin{$\overset{i}{\underset{\ell}{*}}$ / $\underset{\ell}{*}$}','the typescript reads as our transcription','The left margin compares the two star notations across a horizontal separator; the witness omits this hand notation.'),
90:(r'\deleted{\illegible{1}} \inserted[typed]{$\hand{\overset{i}{\underset{\ell}{*}}}$-composition of} \xout{operation}','our transcription corrected','The source preserves the cancelled operation and an older unreadable mark. Composition of is a typed interlinear replacement with a handwritten labelled star; arXiv reduces the wording to composition of.'),
94:(r'\deleted{\illegible{1}}','the typescript reads as our transcription','The cancelled prefix is visible before the source equation and remains unreadable; the witness omits it.')
})
