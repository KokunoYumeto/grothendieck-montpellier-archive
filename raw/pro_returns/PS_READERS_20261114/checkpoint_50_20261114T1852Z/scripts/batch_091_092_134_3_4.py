import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_091'
edits=[
 [r'th\over{\unsure{a}}{a}t',r't\over{h}{h}\over{\unsure{a}}{a}t','The h as well as a is retraced in pen; the older a-cell remains obscured.'],
 [r'cour\over{\unsure{s}}{s}e',r'cour\over[typed]{s}{s}e','Two displaced typed s impressions are visible; this is not a handwritten s.'],
 [r're\over{\unsure{fl}}{fl}ection',r're\over{fl}{fl}ection','The old typed f and l remain visible under the larger penned replacements.'],
 [r'one \over{\unsure{m}}{m}ain',r'one \over[typed]{a}{m}ain','The first cell of main has an old typed a under the retyped m.'],
 [r'\xout{appears}\inserted[typed]{gets emphasized}',r'\xout{appears} \inserted[typed]{gets emphasized}','The replacement phrase starts a separate word after the cancelled phrase.'],
 [r'\inserted[typed]{relevant\hand{,}}',r'\inserted[typed]{relevant}','The apparent comma is the hooked end of the insertion curve, not separate punctuation.'],
 [r'we\over{\unsure{l}}{l}l',r'we\over[typed]{e}{l}l','An old e bowl and crossbar remain under the typed l.'],
 [r'eve\over{\unsure{n}}{n}',r'eve\over[typed]{j}{n}','The lower j hook and upper dot are visible beneath the typed n.'],
 [r'semisim\deleted{\unsure{m}}plicial',r'semisim\deleted{m}plicial','The extra m is readable beneath its short pen cancellation.'],
 [r'\over{\unsure{W}}{w}ith',r'\over{\unsure{W}}{w}\over{i}{i}th','The i is also pen-retraced; the older W/w cell remains obscured.'],
 [r'compact \over{\unsure{o}}{o}nly',r'compact \over[typed]{\unsure{o}}{o}nly','The repeated rounded impressions and baseline serif are typewriter impressions, although the lower reading remains doubtful.'],
 [r'ord\over{\unsure{rr}}{er}ed',r'ord\over[typed]{\unsure{re}}{er}ed','Both corrected cells are typewritten. The visible lower strokes plausibly give the transposed re, but that lower layer remains uncertain.'],
 [r'1\over{\unsure{7}}{8}',r'1\over{7}{8}','The typed 7 remains visible inside the large penned 8.'],
 [r'\over{\unsure{wh}}{wh}ether',r'\over[typed]{wh}{wh}ether','The repeated w peaks and doubled h ascenders are typed, with the same letters in both impressions.'],
 [r'preci\over{\unsure{s}}{z}e',r'preci\over[typed]{\unsure{s}}{z}e','The dark z consists of regular type impressions. Its older rounded lower layer may be s and remains doubtful.'],
 [r'1\over{\unsure{8}}{9}',r'1\over{8}{9}','The two typed loops of 8 are clear under the penned 9.'],
 [r'topolog\over{\unsure{y}}{y}',r'topolog\over{j}{y}','The lower typed character has a dot and j stem; the long replacement y is penned.'],
 [r'\over{\unsure{19}}{20}',r'\over{19}{20}','The original typed 1 and 9 remain visible beneath the hand 20.'],
 [r'o\over{\unsure{n}}{f} the reflection',r'o\over{f}{f} the reflection','The lower typed glyph has the hook and crossbar of f, not n; the later f is drawn larger in pen.'],
 [r'2\over{\unsure{0}}{1}',r'2\over{0}{1}','The old typed zero is a clear oval around the penned 1.'],
 [r'\mspage{91}',r'\mspage{\hand{91}}','The lower-left foliation is handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{3099:[r'M \hand{\longrightarrow} (\mathrm{Hot})','The arrow is penned; Hot is typed with its parentheses.']},'unsure':[
 [r'\unsure{a}','The older cell under the hand a remains obscured.'],
 [r'\unsure{.}','The scan cuts the line just after moment, so the period is unconfirmed.'],
 ['s','The repeated typed s impressions are separable.'],
 ['fl','The old serifed f and l are visible under pen retracing.'],
 [r'\unsure{a}','The first letter of are is heavily overdrawn and the lower letter remains uncertain.'],
 [r'\unsure{5}','The pen 3 covers the older digit too heavily to settle whether it was 5.'],
 ['a','The first main cell has a typed a under m.'],
 [r'\unsure{a}','The black deletion before compare still masks the underlying character.'],
 ['e','An e bowl and crossbar remain visible under the typed l.'],
 ['j','The old j descender and dot survive beneath n.'],
 ['m','The cancelled extra m retains its two arches.'],
 [r'\unsure{W}','The underlying capital-or-lowercase w shape is not separable from the pen correction.'],
 [r'\unsure{a}','The older glyph under the closing parenthesis is concealed by dark pen.'],
 [r'\unsure{6}','The old digit under the new 7 is not securely distinguishable; no chronological inference settles it.'],
 [r'\unsure{o}','The overlapping rounded type impressions do not securely identify the older letter.'],
 [r'\unsure{re}','The lower type looks like re under er, but the overlap prevents certainty.'],
 ['7','The typed 7 is visible within the larger pen 8.'],
 ['wh','The two sets of matching typed w/h strokes are visible.'],
 [r'\unsure{y}','The category ending is pen-retraced too heavily to recover its lower letter.'],
 [r'\unsure{s}','The live z is typewritten; the older rounded letter remains uncertain.'],
 ['8','The two old typed loops are visible.'],
 ['j','The old printed dot and stem identify j under the handwritten y.'],
 ['19','The old 1 and 9 are both partly exposed beneath the penned 20.'],
 ['f','The lower typed hook and crossbar identify f.'],
 ['0','The typed oval is clearly visible around the new 1.']
 ],'notes':[
 'Each listed retouch was inspected in enlarged detail. Course, main, well, even, only and whether are typed overprints; reflection, that, are, category and topology include pen retracing. The older obscured cells remain marked.',
 'The old 7, 8, 19 and 0 are visually recoverable beneath 18, 19, 20 and 21. The older digit beneath 17 remains uncertain; it was not supplied by sequence alone.',
 'All four interlinear phrases are typed. The apparent punctuation after relevant is its placement hook and has been removed as a false comma; the independent comma after appears is retained as transcribed.',
 'The end after moment is clipped, leaving the final period uncertain.',
 'The thick deletion before compare remains unreadable enough to retain the tentative a.',
 'The live z is composed of type impressions; the lower s-like character is still doubtful.',
 'The er correction is typed, with tentative transposed re below; uncertainty is retained.',
 'The lower-left 91 is penned.'
 ],'evidence':'Both original halves and 25 labelled enlarged details inspected. The repeated s of course, a-to-m in main, e-to-l in well, j-to-n in even, matching wh overprint and the z of precize are typewriter layers. Reflection has readable typed fl under pen retracing; the h of that and i of with are also penned. The extra m in semisimplicial is readable under its cancellation. Relevant has only a placement hook after it. Note numbers 18, 19, 20 and 21 preserve visible older 17, 18, 19 and 20; the lower digit under 17 remains doubtful. Topology has a typed j beneath pen y, and of has typed f beneath pen f. The clipped period and several dense lower layers remain uncertain.'})

GLOBE=r'\mathord{\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.5ex]\draw (0,0) ellipse (.72 and .95);\draw (0,-.95) .. controls (-.75,-.15) and (-.2,.65) .. (0,.95);\end{tikzpicture}}'
key='ps_134-3_092';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=re.sub(r'\\hand\{\$([^$]+)\$\}',lambda m:r'\hand{\ensuremath{'+m.group(1)+'}}',line)
 new=new.replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'B^{\wedge}',r'B^{\hand{\wedge}}').replace(r'(B_{/a})^{\wedge}',r'(B_{/a})^{\hand{\wedge}}')
 if new!=line:edits.append([line,new,'The presheaf hats are penned. Replace nested math delimiters and empty accents without changing the visible formula.'])
edits += [
 [r'irrele\over{\illegible{1}}{v}ant',r'irrele\over{\unsure{u}}{v}ant','The lower glyph has a rounded bottom suggestive of u, but remains uncertain beneath the pen v.'],
 [r'8$^{\text{o}}$',r'8$^{\underline{\mathrm{o}}}$','The raised typed o has a short underline, visible as an ordinal mark.'],
 [r'\hand{/}for',r'\hand{/} for','The slash marks the boundary before the separate word for.'],
 [r'(! $^{2',r'(\hand{!} $^{2','The exclamation sign beside the renumbered note is written in pen.'],
 [r'\over{with}{to}',r'\deleted{wi}\over{th}{to}','The initial wi is crossed separately; the handwritten to occupies the two old th cells.'],
 [r'hand\over{\illegible{1}}{y}',r'hand\over{\unsure{y}}{y}','The lower typed y-like arms are partly visible but cannot be separated securely from the pen y.'],
 [r'ins\over{\illegible{1}}{t}ead',r'ins\over[typed]{o}{t}ead','The old rounded o is clear beneath a regular typed t.'],
 [r'\over{\illegible{1}}{e}ligible',r'\over{a}{e}\over{l}{l}igible','The first typed a is corrected to e in pen; the following l is also pen-retraced over a visible typed l.'],
 [r'\margin{39 or}',r'\margin{\diagram{\begin{tikzpicture}[baseline=(n.base)]\node[inner sep=1pt] (n) {39 or};\draw (n.center) ellipse [x radius=1.8em,y radius=1.1em];\end{tikzpicture}}}','The separate marginal 39 or is enclosed by a pen oval. It is distinct from the above-line insertion and both are retained.'],
 [r'se\over{\illegible{1}}{c}tion',r'se\over{\unsure{c}}{c}tion','The old rounded cell under c is partly exposed but remains uncertain.'],
 [r'$M \to B^{\hand{\wedge}}$',r'$M \hand{\to} B^{\hand{\wedge}}$','The arrow in note 27 is drawn in pen.'],
 [r'\unsure{cf.}',r'\over{\unsure{c}}{c}f.','The final cf. is readable; the c has an obscured older layer that remains doubtful.'],
 [r'\hand{\unsure{,}}',r'\hand{\begin{tikzpicture}[x=.8em,y=.8ex,baseline=-.3ex]\draw (.6,.65)--(0,.35)--(.42,.05);\draw (.56,-.05)--(.18,-.25) .. controls (-.03,-.48) and (.25,-.76) .. (.33,-.56);\end{tikzpicture}}','The right-edge sign has several angular strokes and a hooked lower part; it is not a comma. Reconstruct the visible graphic.'],
 [r'\hand{)}are',r'\hand{)} are','The added closing parenthesis and following are require a word boundary.'],
 [r'\hand{\unsure{$\emptyset$}}',r'\hand{\ensuremath{'+GLOBE+'}} ','The symbol has the closed oval and inner arc of the hemisphere symbol on the preceding note pages, not an empty-set slash.'],
 [r'\over{C}{\v{C}}',r'$\overset{\hand{\vee}}{\mathrm{C}}$','The C is typed; only the small hacek above it is penned.'],
 [r'\mspage{92}',r'\mspage{\hand{92}}','The lower-left foliation is handwritten.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3110:['integrators','The typed word has its r before the final s.'],
 3119:[r'\hand{cf. section} \inserted{39 or} \hand{44).}','The handwritten word section is singular; the marginal circled 39 or and above-line insertion are both present.'],
 3122:['Angular hand sign after (Cat)','The sign is present but has multiple strokes and a lower hook, not a comma. It is reconstructed as a graphic.','correct transcription']
 },'unsure':[
 [r'\over{\unsure{c}}{c}f.','The final cf. is readable, but the c hides an older letter.'],
 ['Reconstructed angular pen sign','The visible mark is multi-stroke and cannot be represented as a comma.'],
 ['Handwritten hemisphere symbol with inner arc','The outline and separate inner arc match the clear hemisphere symbols on pages 89 and 90.']
 ],'illegible':[
 [r'\unsure{u}','The rounded lower glyph is tentatively u, still uncertain.'],
 [r'\illegible{1}','The earlier digit is covered by the handwritten 2; its sequence alone does not settle it.'],
 [r'\illegible{1}','The old final s-cell is at the clipped right edge and cannot be recovered beneath the pen.'],
 [r'\unsure{y}','The old y-like arms remain only partly visible.'],
 ['o','The round closed old o is distinct beneath the typed t.'],
 ['a','The typed a shape is visible beneath the penned e.'],
 [r'\unsure{c}','The lower round c-like cell remains only partly exposed.']
 ],'notes':[
 'All listed notes are present and retained, including the whole added note 28-prime and the unfinished note 32.',
 'Here I am confusing is readable under the machine x row; the old digit under the handwritten 2 remains illegible. The adjacent exclamation is penned.',
 'Instead has typed o-to-t overprinting; eligible has pen a-to-e and l retracing. The singular section reference is followed by an above-line 39 or, and a distinct circled duplicate appears in the left margin.',
 'The old es is visible under the pen ing, and the separately inserted is remains live.',
 'The full handwritten line is legible; the final cf. can be read, with an uncertain lower layer under c.',
 'The symbol is the hemisphere outline with its inner arc, matching the preceding pages.',
 'The equivalence symbol has two wavy strokes and a lower straight stroke, consistent with approxeq. Both hats are penned.'
 ],'evidence':'Both original halves and twelve enlarged details inspected. The word integrators is complete; the internal blank in comme nts is left literal. The obsolete cellular-structure discussion is followed by the proper-map correction and the later test-category terminology. Instead has typed o/t layers, whereas eligible has pen corrections over a and l. The two instances of 39 or are separate, with the marginal one circled. The note-27 arrow and all hats are penned. The whole note 28-prime is retained; cf. is readable but has an uncertain older c-layer. The mark after (Cat) is an angular graphic rather than a comma. The note-31 symbol is the same inner-arc hemisphere symbol as before. The typed C of Cech remains plain under its pen hacek.'})
