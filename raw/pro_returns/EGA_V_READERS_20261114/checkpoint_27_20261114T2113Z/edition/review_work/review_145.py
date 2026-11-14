import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
k='ega25_25_145'
r=[
(r'\margin{6}',r'\mspage{\hand{6}}','The upper6 is a handwritten folio.'),
(r'\mspage{145}',r'\mspage{\hand{145}}','The lower145 is handwritten.'),
(r'\xout{\illegible{1}} où',r'\xout{\unsure{mixte}} où','Enlargement allows mixte under the typewriter cancellation, but the first letters remain obscured, so the candidate stays doubtful.'),
(r"\inserted{d'une identité de}",r"\inserted[typed]{d'une identité de}",'The insertion uses the typewriter face, with a pen brace; vue is not crossed out.'),
(r'\unsure{m|r}',r'm','Each rank symbol and the four exterior-power exponents visibly have the two-humped typed m; no r form is visible there.'),
(r'\bigwedge^{m} R$)',r'\bigwedge^{m} M$)','The final object in the Hom expression visibly has a broad typed capital M, rather than the narrower R used elsewhere on the same page.'),
(r'(\bigwedge^{r} R)$\hand{\illegible{1}}',r'(\bigwedge^{r} R^{\hand{\illegible{1}}})$','The unresolved mark is physically above/over R, not a separate baseline word after the parenthesis; its reading remains illegible.'),
(r'\inserted{sous-}',r'\inserted[typed]{sous-}','Sous- is typed above préschéma; only the insertion bracket is pen-written.'),
(r'\inserted{\unsure{espace annelé}}',r'\inserted{espace annelé}','Both words of the handwritten replacement are legible.'),
(r'\inserted{M}',r'\inserted[typed]{M}','The capital M is typewritten above libre de, with a pen placement mark.'),
(r'On est alors',r'O\over{n}{n} est alors','The n in On has a small handwritten n-like reinforcement immediately below it, which the source omitted.'),
(r'P et Q de rangs respectifs',r'P et Q de rangs res\over{\unsure{p|s}}{p}ectifs','A long pen descender rewrites p in respectifs; the obscured typed underletter remains uncertain.'),
(r'\phi',r'\hand{\phi}','Each phi is handwritten in its typewriter blank.'),
(r' \in ',r' \hand{\in} ','The membership sign is handwritten.'),
(r'\longrightarrow',r'\hand{\longrightarrow}','The long arrows are pen strokes.'),
(r'\rightarrow',r'\hand{\rightarrow}','The exterior-power arrow is handwritten.'),
(r'\bigwedge',r'\hand{\bigwedge}','Every exterior-product wedge is drawn by hand; the exponents remain typed.'),
(r'\simeq',r'\hand{\simeq}','The isomorphism sign at the left of the formula is handwritten.'),
(r'\underline{\Omega}',r'\underline{\hand{\Omega}}','The Omega letters are handwritten within otherwise typed objects.'),
(r'\overset{\vee}{\underline{P}}',r'\overset{\hand{\vee}}{\underline{P}}','The dual check above P is handwritten.')]
d={5:'The upper6 is a handwritten page number.',9:'The x-cancelled word allows the tentative reading mixte after enlargement; it remains doubtful.',16:'D’une identité de is typed above vue with a pen brace; des is x-cancelled and vue remains live.',23:'The rank letter is a typed m with two humps, even though later exponents use r.',24:'Both exterior-power exponents in this line are typed m; the wedges and arrow are handwritten.',25:'Both exponents are typed m; the final object reads typed capital M, and is preserved as such.',26:'The mark over R remains illegible and is positioned above R; the final dual check is handwritten. Sous- is typed above the line with a pen leader.',32:'Mu is handwritten. The small pen reinforcement under the n of On is retained.',35:'Préschéma is crossed out by hand; espace annelé is legible handwritten replacement. The inserted M is typed, with a pen leader.',38:'The lower145 is handwritten.'}
n=['The upper6 and lower145 are handwritten folios.','A crop permits tentative mixte through the x strokes, so the illegible mark becomes an uncertain reading rather than confident text.','D’une identité de is typed with a hand brace; vue remains uncancelled.','The glyphs visibly read m in the rank sentence and four exterior-power exponents; the later q-r and r are also retained exactly, without mathematical repair.','Q and R are heavily typed but identifiable; the last Hom object has an M-shaped glyph and is corrected to M. The V in the subscript is overprinted but still legible.','The mark over R is still unreadable; its superscript placement is retained. The check over the final Q is handwritten.','Sous- is typewritten, with a pen insertion mark.','Mu is handwritten; the small n-like pen mark under On is recorded as reinforcement.','Espace annelé is legible handwriting; M is a typed insertion.','The pen descender rewrites p in respectifs; the obscured typed letter is left p/s uncertain.','Both image parts, all formulas, cancellation layers and margins were read.']
e=[dict(line='23–26',before='q et m; exterior exponents m; later q-r and r',image='q et m; exterior exponents m; later q-r and r',decision='preserved',reason='The page changes from m to r in the displayed exterior-power identification. The visible symbols are retained and the discrepancy is reserved for the guide.',category='mathematical-slip'),dict(line=25,before=r'\bigwedge^m R',image=r'\bigwedge^m M',decision='corrected',reason='The scan ends the Hom expression with capital M. The neighboring formula uses R; that discrepancy is preserved rather than reconciled.',category='mathematical-slip')]
x=complete(k,r,d,n,e);print(k,len(x['decisions']))
