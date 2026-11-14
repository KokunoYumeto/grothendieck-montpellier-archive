import re,sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_069';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',r'\\hand{\\ensuremath{\1}}',line)
 new=new.replace(r'A\^{}',r'$A^{\hand{\wedge}}$').replace(r'^{\wedge}',r'^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf carets are pen. Repair text-mode empty accents and nested math delimiters, retaining the typed base letters and slash positions.'])
up=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,0)--(.2,0) .. controls (0,0) and (0,.2) .. (0,.4)--(0,1.4);\end{tikzpicture}}}'
down=r'\margin{\diagram{\begin{tikzpicture}\draw[->] (.6,1.4)--(.2,1.4) .. controls (0,1.4) and (0,1.2) .. (0,1)--(0,0);\end{tikzpicture}}}'
edits += [
 [r'\mspage{69}',r'\mspage{\hand{69}}','The folio is handwritten.'],
 [r'\inserted{\unsure{those}}',r'\inserted{as}','The insertion has two letters, a and s; the trailing curve is the placement mark. It does not spell those.'],
 [r'\unsure{which}',r'\over[typed]{what}{which}','The live word which has typed i/c over a/t, while the final h extends the old what. The differing serif impressions are readable.'],
 [r'a \hand{t}est category',r'a \over[typed]{t}{t}est category','The t has displaced typewriter impressions, rather than a pen stroke.'],
 [r'coun\hand{t}erexample',r'coun\over[typed]{t}{t}erexample','The doubled t crossbars and serif stem are typewriter impressions.'],
 [r'any \hand{t}est category',r'any \over[typed]{t}{t}est category','The t is a repeated typewriter impression, as in the earlier test on this page.'],
 [r'T\over{\unsure{a}}{2}',r'T\over[typed]{a}{2}','Both old a and new 2 are clear typewriter impressions, the 2 displaced upward.'],
 [r'\xout{\illegible{1}}',r'\xout{subob}','The cancelled fragment reads subob, with the two b ascenders and middle o still clear.'],
 [r'ha\over{\unsure{t}}{v}e',r'h\over[typed]{\unsure{q}}{a}\over[typed]{t}{v}e','The v is typed over t. A separate descender remains beneath a, tentatively from an old q, and is retained with uncertainty.'],
 [r'N\over{\unsure{e}}{o}w',r'N\over[typed]{e}{o}w','The old e crossbar and displaced typed o are both visible.'],
 [r'requi\over{\unsure{t}}{r}ement',r'requi\over[typed]{\unsure{t}}{r}ement','The live r has typewriter serifs; the old t-like impression remains uncertain.'],
 [r'th\over{\unsure{a}}{e}n',r'th\over[typed]{\unsure{a}}{e}n','The final e is a typed overprint; the old a-like lower impression is still not secure.'],
 [r'up\over{\unsure{n}}{o}n',r'up\over[typed]{n}{o}n','The old n stems and new typed o can be separated in the enlargement.'],
 [r'\margin{\hand{\ensuremath{\uparrow}}}',up,'The source mark has a lower horizontal tail joined to the upward shaft; reconstruct the bent arrow, not a bare glyph.'],
 [r'\margin{\hand{\ensuremath{\downarrow}}}',down,'The second mark has an upper horizontal tail joined to the downward shaft; retain the actual bent-arrow form.']
]
# Margin math is not nested in hand in the original; use its exact current form.
edits[-2][0]=r'\margin{$\uparrow$}'
edits[-1][0]=r'\margin{$\downarrow$}'
save_review({'key':key,'edits':edits,'diffs':{
 2715:[r'\inserted{as}','The enlarged insertion reads as, not those; its terminal sweep is the insertion curve.','correct transcription'],
 2725:[r'T\over[typed]{a}{2}','The old a is recoverable and the new 2 is typed above it.','correct transcription'],
 2729:[r'h\over[typed]{\unsure{q}}{a}\over[typed]{t}{v}e','The replacement v and its old t are typed; a separate old descender under a remains doubtful.','correct transcription'],
 2731:[r'N\over[typed]{e}{o}w','The e-to-o change is typed overprinting.','correct transcription'],
 2735:['T 2 for test categories','There is no is between T 2 and for on the source.'],
 2736:[up+' ; '+down,'The two marks are separate bent arrows with horizontal tails, reconstructed graphically.','correct transcription'],
 2737:['40.','The source contains only the number 40 and the ensuing prose, without the witness’s descriptive title.'],
 2742:[r'Finall\over{\unsure{x}}{y} we are reduced','The typed are is present. The pen y is clear, but the earlier letter remains obscured.']
 },'unsure':[['as','The two hand letters are a and s; the following curve is a placement stroke.'],[r'\over[typed]{what}{which}','The typed a/t lower layer and i/c upper layer settle the final word and the old what.'],['a','The old a is visible below the typed 2.'],['t','The old t crossbar remains above the new typed v.'],['e','The old e is visible behind the displaced typed o.'],[r'\unsure{t}','The old t-like impression under requirement remains uncertain.'],[r'\unsure{a}','The old character under the new e in then remains uncertain.'],['n','The old n stems are visible beneath the typed o.'],[r'\unsure{x}','The old character under the hand y is too densely overlapped to settle.']],
 'illegible':[['subob','The five-character cancelled fragment is legible, including its two b ascenders.']],
 'notes':[
 'The membership sign is pen. The comma following the parenthesis overwrites a visible typed a, as transcribed.',
 'The inserted word is as, not those; the final sweep is an insertion mark.',
 'Which is typed over what; the changed a/t and i/c positions are distinguishable.',
 'The t repetitions and the replacements in T2, have, Now, requirement, then and upon are typed. Earlier characters are recovered where visible and kept uncertain otherwise; the final y of Finally is pen.',
 'The small isolated dot before Cx(A/a) remains visible and is retained without interpreting its purpose.',
 'Both margin marks have bent horizontal tails; they were reconstructed as graphics rather than plain up/down glyphs.'
 ],'evidence':'Both full halves and twelve local enlargements inspected. The first insertion reads as, producing and as maps ... all those; the witness-based those was wrong. Several supposed pen repairs are typed overprints, including which over what and 2 over a. The cancelled subob fragment is recovered. The universal counterexample takes the slice over a homotopy interval, whose disjoint nonempty endpoint subobjects obstruct total asphericity. The sentence comparing strictness still lacks is, as on the scan. The two bent margin arrows are distinct graphic annotations. Section 40 begins with the aspheric projection argument, and its final are in we are reduced is plainly present.'})

key='ps_134-3_070';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\to(?![A-Za-z])',r'\\hand{\\to}',line)
 new=new.replace(r'\ar[',r'\ar[color=blue,')
 if new!=line:edits.append([line,new,'All arrows on this line are hand-drawn. Mark their provenance blue while leaving typed objects and typed labels plain; diagram topology is unchanged.'])
edits += [
 [r'functor\unsure{k}',r'functork','The final pale character has a clear k stem and two diagonal arms; retain the literal stray k.'],
 [r'\xout{xhx}',r'\xout{the}','The cancelled word has the t stem/crossbar, h ascender and e bowl of the.'],
 [r'morphism of topoi',r'morphism of topo\over[typed]{i}{i}','The final i has repeated typewriter impressions, especially its dot and top serif; no separate circumflex is visible.'],
 [r'$C^{\wedge}$\hand{$\hat{}$}',r'$C^{\hand{\overset{\wedge}{\wedge}}}$','The scan has two distinct pen carets, one immediately above the other to the right of C. Preserve both and repair the empty-accent macro.'],
 [r'by small categories',r'by sm\over[typed]{\unsure{m}}{a}ll categories','The a in small overlaps earlier m-like typewriter strokes; the earlier letter is retained tentatively rather than flattened.'],
 [r'T\inserted{h}e proposition',r'T\over[typed]{h}{h}e proposition','The two displaced h impressions have typewriter serifs. This is typed overprinting, not an interlinear handwritten insertion.'],
]
first_diagram = "\\diagram{\\begin{tikzcd}[column sep=tiny]\nX' "
edits.append([first_diagram, "% Hand-drawn arrows are marked blue; typed objects remain plain.\n" + first_diagram, "Document the provenance convention for the mixed diagrams."])
save_review({'key':key,'edits':edits,'diffs':{
 2743:['functork  i.e.','The trailing k is a visible typed character; no comma replaces it.','correct transcription'],
 2748:[r'$C^{\hand{\overset{\wedge}{\wedge}}}$','Both carets are actual pen marks in a vertical stack above C. The initial transcription’s empty hat macro did not represent their placement correctly.','correct transcription'],
 2750:[r'\hand{fxid_c}','The upper arrow label is hand and its c subscript is lowercase; preserve that literal form.'],
 2752:[r'T\over[typed]{h}{h}e','The h is a repeated, displaced typed impression, rather than a hand insertion.','correct transcription']
 },'unsure':[['k','The k stem and upper/lower diagonals are clear despite the pale impression.'],[r'\unsure{E}','The earlier capital beneath C has obscured middle strokes; E remains possible but cannot be securely distinguished from another capital.']],
 'illegible':[[r'\illegible{1}','The old word after the quoted phrase is crossed by multiple strokes. Initial n/a-like remnants are visible, but the complete word is not safely recoverable.']],
 'notes':[
 'The trailing character is a literal typed k, not a comma.',
 'The cancelled word before an identity is recoverable as the.',
 'The old capital under C remains uncertain. The x and C subscript in the displayed product are ink-dark hand repairs, as transcribed.',
 'The final i of topoi is reinforced by a typed overprint; there is no independent circumflex above it.',
 'The final reading moreover is clear despite overlapping e/o impressions, whose separate prior sequence is not recoverable. Small has an old m-like impression beneath a, retained tentatively as a typed overprint.',
 'The crossed word before and how far remains illegible after enlargement; no context-based expansion is supplied.'
 ],'extra_records':[{'source_id':'OBS:ps_134-3_070:1','before':r'Y_{/U} \to U','after':r'Y_{/U} \hand{\to} U','decision':'retain apparent authorial slip','reason':'The displayed target is visibly U, although the described localization of the topos Y should have target Y. Preserve the source U and flag it in the section guide.','line':26}],
 'evidence':'Both complete halves and ten local details inspected. The proof introduces weak equivalence relative to a base topos, reduces the product claim over C to categories C/c with final elements, and uses the projection square. Every diagram arrow is pen; f and F in the first two triangles are typed, while the labels of the final square are hand. The top-right prime in that square is cancelled. The localization arrow literally targets U, an apparent source slip. Two separate handwritten carets above C are retained. The initial stray k and cancelled the are recovered; the old capital under C and the struck final word remain doubtful. The last The has a typed h overprint.'})
