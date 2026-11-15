from review_root import review

leftold="\\margin{The ``if'' results from \\unsure{considerations} (iii) in prop. 2' as $i_A^*$ will transform maps in \\uline{W} into $\\underline{W}_A$-\\unsure{spheric|aspheric} maps}"
leftnew="\\margin{The ``if'' results from criterion (iii) in prop. 2 -- as $i_A^*$ will transform maps in \\uline{W} into \\uline{$\\underline{W}_A$-\\unsure{spheric|aspheric}} maps}"
rightold=r"\inserted{(i') the functor $i_A^*$ transforms maps in \uline{W} into $\underline{W}_A$-aspheric maps. (And we may even restrict to \unsure{$C\to e$} for \unsure{C in Cat}, with C having \unsure{a final object}, i.e. stating that $i_A^*(C)$ is $\underline{W}_A$-\unsure{asph.} \uline{over $e_A$}.)}"
rightnew=r"\margin{(i') the functor $i_A^*$ transforms maps in \uline{W} into $\underline{W}_A$-aspheric maps. (And we may even restrict to $C\to e$ in Cat, with C having a final object, i.e. stating that $i_A^*(C)$ is $\underline{W}_A$-asph. \uline{over} $\uline{e}_{A^{\unsure{\wedge|\circ}}}$}"
review('ps_134-4_086',owner='134_4_tail',changes=[
 (r'A is a \xout{xxxx} \uline',r'A is a \xout{test} \uline','The old t ascenders and e/s bodies are visible under the regular x strikes.'),
 (r'if it is a \xout{xxxx}',r'if it is a \xout{test}','The second cancelled four-letter word likewise reads test.'),
 (r'weak $\underline{W}$-test\xout{x}',r'weak $\underline{W}$-test\xout{\unsure{-|=}}','The extra cancelled cell contains short horizontal impressions, plausibly a hyphen or equals; the cancelling x is not itself the old text.'),
 (r'$A_{/a}$ \xout{xxx} for',r'$A_{/a}$ \xout{are} for','The old a bowl, r shoulder and e crossbar can be read under the x strikes.'),
 (r'\inserted{\uline{W}-}',r'\inserted[typed]{\uline{W}-}','The raised W and hyphen are regular typing with a handwritten placement curve.'),
 (r'\xout{Proposition\unsure{xx|2}}',r'\xout{Proposition \unsure{2|3}}','The old final digit has a partly obscured curved upper and lower body; retain 2/3 uncertainty rather than literal cancellation x characters.'),
 (leftold,leftnew,'The rotated left note says criterion, not considerations; an independent reading confirms it. The stroke after prop.2 is a dash. The final W_A-aspheric/spheric phrase is underlined and remains lexically doubtful.'),
 (r'\unsure{model}','model','All five pen letters are legible. The initial m is heavily retraced but not cancelled.'),
 ('THe following',r'T\over[typed]{h}{\unsure{H|h}}e following','The initial cell contains overlapping regular h and H-like impressions; their final case is not forced from the sentence.'),
 (rightold,rightnew,'The handwritten condition is in the right margin. It reads restrict to C-to-e in Cat, with no extra for C. Its final raised mark after subscript A remains uncertain; no invisible closing parenthesis is supplied.'),
 ('(ii)  The  Lawvere',r'(ii)  T\over[typed]{h}{\unsure{H|h}}e  Lawvere','The h has a regular raised H-like impression, whose final case remains uncertain.'),
 (r'\unsure{products|producte}','products','The last typed letter has the two lobes of s, partly crossed by the separate handwritten note, not e.'),
 ('(iii)  There exists',r'(iii)  T\over[typed]{h}{\unsure{H|h}}ere exists','The h again has a regular raised H-like overprint; preserve its final-case uncertainty.'),
 (r'all products axI  $\underline{W}$-aspheric.',r'all products axI  $\underline{W}$\unsure{\rlap{\hand{(}}-}aspheric.','A tall curved pen stroke crosses the typed hyphen. Preserve the combined visible graphic without interpreting it as a new mathematical condition.'),
 ('The obvious implications',r'T\over[typed]{h}{\unsure{H|h}}e obvious implications','The initial h/H overlap is restored with the same scoped case uncertainty.'),
 (r'\xout{xxxx}  by the criterion',r'\xout{i\illegible{1}}  by the criterion','A dotted initial i survives the cancellation, but the rest of the old run is not securely readable.'),
 (r'\xout{(ix)}',r'\xout{(i\illegible{1})}','The initial i and parentheses are readable, but the next old character is obscured by a regular x.'),
 ('(cf. page 62)',r'(cf. \over{p}{p}age 62)','The p has an irregular pen retracing with a long lower stroke.'),
 ('and satisfies',r'and \over[typed]{s}{\unsure{S|s}}atisfies','The first s has a regular capital-S-like overprint; the final case remains uncertain.'),
 (r'\xout{Corollaryx2x}',r'\xout{\uline{Corollary} 2}','The old heading reads Corollary2, with an underline under Corollary; the x characters are cancellation impressions.'),
 (r'\uline{Remark}  In',r'\uline{R\over[typed]{\unsure{h}}{e}mark}  In','An older raised h-like impression is visible above and within e; it remains doubtful because it approaches the preceding cancelled heading.'),
 ('is equivalent to',r'is equivalent \over[typed]{y}{t}o','A regular y descender and upper arms remain visible under the final t.'),
 ('resp. of I.',r'resp. o\over{f}{f} I.','The f has a continuous pen retracing through its upright and lower curve.'),
 (r'$A^\wedge$\xout{x}',r'$A^\wedge$\deleted{\xout{\illegible{1}}}','The regular x cancellation has an additional long pen strike. The earlier cell under both layers remains unreadable.'),
 ('of page 166',r'of page \over{1}{1}66','The leading1 is retraced by a heavy pen upright and foot.'),
 ("isn't equivalent", "is'nt equivalent",'The apostrophe stands before n on the scan. Restore the author spelling rather than the draft normalized placement.')
 ],doubts={'unsure':[
 (r'\unsure{2|3}','doubt revised','The final cancelled heading digit remains ambiguous between the visible curved shapes of2 and3.'),
 ('criterion','doubt resolved with corrected reading','The rotated word has the compact criterion outline and -ion ending; independent inspection agrees.'),
 (r'\unsure{spheric|aspheric}','doubt retained','The small initial pen strokes after the hyphen do not clearly separate a from s.'),
 ('model','doubt resolved','All five letters are legible despite the heavily retraced m.'),
 (r'$C\to e$','doubt resolved','The capital C, arrow and e are legible in the enlarged right margin.'),
 ('in Cat','doubt resolved with corrected reading','The note reads in Cat; the draft extra for C is absent.'),
 ('a final object','doubt resolved','The split handwritten phrase a final object is readable across its two lines.'),
 ('asph.','doubt resolved','The abbreviated asph. and its final point are legible.'),
 ('products','doubt resolved','The final typed s is visible beneath the separate marginal handwriting.')
 ]},notes=[
 'The left note says criterion(iii) in prop.2 followed by a dash. The last spheric/aspheric word remains doubtful, and its underline is restored.',
 'The right note has C-to-e in Cat, with C having a final object, followed by the asph. abbreviation. The extra draft for C and supplied closing parenthesis are removed. A raised final mark after A is retained as a local graphic doubt.',
 'The word model is live. Its m is retraced, but there is no cancellation through the word.',
 'All four h/H cells retain their regular overprint uncertainty. The initial s of satisfies is similarly layered. The final old character in the struck label after criterion remains unreadable.',
 'The pen curve across the final W-aspheric hyphen is retained as a doubtful composite graphic. The separate slash after A-caret in the remark is already present and is retained.',
 'The lower-left86 is handwritten archive foliation.'
 ],summary='Both halves, twenty details and both enlarged marginal notes inspected, with an independent reading of the two notes. Resolved criterion, model, products and most of the right-hand condition; retained its final raised-mark doubt and the left note aspheric/spheric doubt. Recovered the cancelled test/test/are headings, restored typed W insertion and several letter/graphic layers, and replaced literal cancelling xs by readable or explicitly unreadable old text. Restored is-nt from the scan. The additional local-test condition is now an anchored marginal note, with no unprinted closing parenthesis supplied. The implication ii-to-i and the full strict-total-asphericity qualification remain as written.',differences={
 4708:('iff it is a local W-test','the typescript reads as our transcription','The source has both f letters of iff and the pronoun it.'),
 4710:(leftnew,'our transcription corrected','The omitted left margin says criterion(iii), not considerations, and has a dash after prop.2; the last word remains doubtful.'),
 4711:(rightnew,'our transcription corrected','The omitted right marginal condition has C-to-e in Cat and the final-object qualification. The draft extra words and closing parenthesis are not on the scan.'),
 4718:(r'(ii)\hand{$\Rightarrow$}(i)','the typescript reads as our transcription','The source clearly gives ii implies i, whereas the witness repeats i on both sides.'),
 4719:('(cf. prop.1),','the typescript reads as our transcription','The source has both the closing parenthesis and comma.'),
 4725:(r'\margin{$\|$}','the typescript reads as our transcription','Two parallel pen strokes stand in the left margin beside the final conclusion.')
 })

review('ps_134-4_087',owner='134_4_tail',changes=[
 (r'B\over{\unsure{o}}{o}th',r'B\unsure{\ensuremath{\underset{\frown}{\overset{\smile}{\mathrm o}}}}th','The base is a plain typed o with a separate cup above and cap below, not a securely identified pen replacement of one letter by another.'),
 (r'\xout{\unsure{andxha}xxxx}',r'\xout{and hence}','The old run reads and hence through the regularly spaced x strikes; the remaining x after it cancels blank space.'),
 (r'\xout{W}If',r'\over[typed]{W}{I}f','The W and I occupy one regular typewriter cell. This is an overprint, not a separately cancelled W before If.'),
 (r'\uline{test} \uline{category}',r'\uline{\over[typed]{o}{t}est} \uline{category}','The initial t is printed over a clear rounded o, with both regular impressions visible.'),
 (r'(Hot$_{W}$)',r'(H\unsure{\ensuremath{\overset{\smile}{\mathrm o}}}t$_{\underline{W}}$)','Restore the detached upper cup over o and the underline beneath the regular typed subscript W; the cup provenance remains uncertain.'),
 (r'\xout{andxmoreover}',r'\xout{and moreover}','The x characters separate the cancelled words mechanically; the old words themselves are and moreover.'),
 (r'\xout{$\underline{W}$xxisxsaturated}',r'\xout{$\underline{W}$ is saturated}','Restore the readable old word spacing instead of printing the cancelling xs as letters.'),
 (r'requi\unsure{t|r}ement',r'requi\unsure{\over[typed]{r}{t}}ement','The cell contains a regular r shoulder and a taller t stem/crossbar; preserve the superposition with uncertain order.'),
 (r'\xout{2Hx}',r'\xout{2H}','The old2 and H are readable; the final x is a cancellation impression over blank space.'),
 (r'\unsure{we}',r'\over[typed]{i}{w}e','A clear old i dot and stem remain within the final regular w, followed by plain e.'),
 (r'\xout{alxx}',r'\xout{al\illegible{1}}','The a and tall l are readable; the following old letters are obscured by regular x strikes and the clipped right edge.')
 ],doubts={'unsure':[
 ('o with separate upper/lower graphic marks','doubt narrowed','The base letter is clearly o; the separate cup/cap marks remain of uncertain provenance and interpretation.'),
 ('and hence','doubt resolved with corrected reading','The e,n,c,e sequence after h is readable under the regular x cancellation.'),
 (r'\unsure{a}','doubt retained','The old bowl and right stem under the pen e remain partly blackened; a is plausible but not certain.'),
 (r'\unsure{\over[typed]{r}{t}}','doubt revised','Both regular r/t impressions are visible; their overwrite order remains uncertain.'),
 (r'\unsure{5}','doubt retained','The old numeral under pen6 is heavily covered;5 is plausible but not securely established.'),
 (r'\over[typed]{i}{w}e','doubt resolved','The old i dot/stem and live regular w/e are separately visible.')
 ]},notes=[
 'Both has plain typed o plus a detached cup above and cap below. The graphics remain doubtful rather than being treated as a confirmed letter correction.',
 'The subscript W is regular typing and underlined. The detached cup above Hot is preserved with uncertain provenance.',
 'The initial I of If is typed over W in a single cell; there is no separate cancelled W.',
 'The initial t of test is typed over a clear o.',
 'The tiny isolated mark near and has no readable letter shape or identifiable correction trajectory; it is not transcribed as a new character.',
 'The first letter of we is regular w over an old dotted i, now resolved.',
 'Both thin pen slashes separating A-caret from the following word are retained as visible source marks.',
 'The lower-left87 is handwritten archive foliation.'
 ],summary='Both halves and ten enlarged details inspected. Resolved cancelled and-hence, the W-to-I and o-to-t typed overprints, and i-to-w in we. Preserved the independent upper/lower o graphics, the r/t order in requirement, the old a under pen e and old5 under pen6. Recovered cancellation word spacing and marked the clipped old run after i_A as unreadable. The final paragraph explicitly identifies a possibly missing hypothesis on i_A-star in the earlier theorem, and this author reconsideration is reserved for the guide without altering either theorem.',differences={
 4738:(r'\xout{2H}','our transcription corrected','The cancelled old run consists of readable2 and H. The final regular x is the cancellation mechanism; the witness omits the entire struck run.')
 })
