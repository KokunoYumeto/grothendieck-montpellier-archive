from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_record import save,source_path

def finish(site,changes,rows,lines,notes):
 key=f'ega25_25_{site:03}'
 if (Path(__file__).parent/(key+'.json')).exists(): return
 s=source_path(key).read_text()
 origins=[i for i,l in enumerate(s.splitlines(keepends=True),1) for _ in l]
 touched=[False]*len(s)
 decisions=[]
 for line,before,after,reason in changes:
  if before not in s: raise ValueError((site,before))
  occurrences=[]
  start=0
  while True:
   at=s.find(before,start)
   if at<0:break
   occurrences.append(at);start=at+1
  at=min(occurrences,key=lambda x:(abs(origins[x]-line),sum(touched[x:x+len(before)]),x))
  s=s[:at]+after+s[at+len(before):]
  origins[at:at+len(before)]=[origins[at]]*len(after)
  touched[at:at+len(before)]=[True]*len(after)
  decisions.append(dict(line=line,before=before,image=after,decision='corrected_from_scan',reason=reason,category='reading_change'))
 for line,before,image,decision,reason in rows:
  decisions.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category='visual_check'))
 s=s.replace('not yet checked by eye.','checked against both supplied scan parts; see CHECK_DECISIONS.tsv.')
 return save(key,s,decisions,lines,notes)

finish(63,[
(7,r'\hand{\unsure{n}}',r'\hand{n}','The small n above the wedge has the continuous pen stroke visible in the upper image.'),
(16,r'\inserted{\unsure{(à fibres géom. connexes}}',r'\inserted{\unsure{(à fibres géom. connexes.|à fibres géom. connexes.}}','The magnified insertion shows all four words and its final dot; the left curved stroke may be a parenthesis or part of the insertion sign, so doubt is retained with both readings.'),
(18,r'\inserted{S-}',r'\inserted[typed]{S-}','S and hyphen above isomorphes have typewriter outlines; the curved placement stroke is handwritten.'),
(30,r"d'autre\xout{s}",r"d'autre\deleted{s}",'The final s is covered by a short irregular pen cancellation, not repeated typewriter x characters.'),
(31,r've\unsure{c}toriel',r've\unsure{c|d}toriel','The overwritten letter has a visible vertical ascender; c and d remain possible layers.'),
(31,r"\xout{\unsure{V(E''⊗E')}}",r"\deleted{\unsure{V(E''⊗E')}}",'The formula is cancelled by irregular handwritten loops and diagonal pen strokes.'),
(36,r'\xout{\illegible{1}} k',r'\xout{tout} k','The four underlying typewriter letters t-o-u-t remain legible beneath the row of x characters.')
],[
(5,r'\mspage{58}','58 in pen','confirmed','Top right number read directly.'),
(7,r'\hand{\unsure{n}}','Handwritten n above wedge','confirmed','Both the writing layer and the letter n checked in the upper image.'),
(9,r'\unsure{présentation|présantation}','Overtyped e/a after prés','retained_uncertain','Both candidate vowel shapes survive the typewriter overstrike.'),
(10,r'\xout{\unsure{localement sur S,}}','Typewriter cancellation over localement sur S,','retained_uncertain','All underlying letters are not separately legible; the supplied candidate is compatible with the ink.'),
(15,r'\xout{de type fini,}','de type fini, cancelled by x characters','confirmed','Letters and x cancellation are visible.'),
(16,r'\uline{lisse}','Straight underline under lisse','confirmed','Upper image shows the underline.'),
(20,r'\xout{sommes directes}','sommes directes cancelled by x characters','confirmed','The underlying two words remain readable.'),
(23,r'0 \rightarrow \underline{E}\' \relbar \underline{E} \relbar \underline{E}\'\' \longrightarrow 0','0, E prime, E, E double prime, 0; middle connectors lack clear arrowheads','confirmed','The exact sequence checked character by character; no mathematical completion supplied.'),
(25,r'\xout{\illegible{1}}','A short typewritten x cancellation','retained_illegible','Underlying word remains too obscured to recover.'),
(29,r'\uline{par immersions\n ouvertes}','Wavy pen underline continuing across the line break','confirmed','Underline appears beneath both words and ouvertes on next line.'),
(31,r"\unsure{V(E''⊗E')}",'Cancelled V-formula with indistinct primes','retained_uncertain','Pen cancellation crosses the primes and tensor sign; the formula cannot be settled from the image.'),
(34,r's $\in$ S','s followed by the typed membership surrogate (- and S','confirmed','The glyph records the visible typewriter membership notation; no new symbol introduced.'),
(37,'fnfini; Grassn','fnfini; Grassn with n at baseline','confirmed','Both unusual spellings/placements are printed in the scan and retained.'),
(39,r'\mspage{63}','63 in pencil','confirmed','Bottom-left archive foliation checked.')
],29,'Both scan parts read line by line; upper/lower overlap counted once. Enlarged insertion and cancelled vector-bundle formula inspected. All text, margins, and formulas compared.')
finish(64,[
(17,r'D\unsure{e}',r'D\unsure{e|g}','The overtyped second letter has an e bowl and a lower g-like loop; neither layer is clear enough to settle.'),
(19,r'\xout{Xx=xresp xxxvide=xxx}',r'\xout{\unsure{(resp. vide)}}','The visible x characters are cancellation marks; resp and vide are visible below them, with parentheses doubtful.'),
(29,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The V-shaped dual mark above E is a free pen stroke; E and its underline are typed.'),
(30,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The dual mark on the numerator E is handwritten; the letter is typed.'),
(30,r'\check{\underline{G}}',r'\overset{\hand{\vee}}{\underline{G}}','The dual mark on denominator G is handwritten; the letter is typed.'),
(30,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The final dual E in this line carries a handwritten V mark.'),
(33,r'\xout{(x=1)xmx}',r'\xout{\unsure{(r-1)-m}}','Typewriter x cancellation overlays a parenthesized r-1 and m; the connecting minus is partly obscured.'),
(33,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual mark above the typed P before the comma is handwritten.'),
(34,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual mark over P in P et P is a fine pen stroke.'),
(36,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The dual mark in the last display is handwritten.'),
(29,r'\simeq',r'\hand{\simeq}','The first displayed isomorphism sign is drawn by hand.'),
(36,r'\simeq',r'\hand{\simeq}','The last displayed isomorphism sign is drawn by hand.')
],[
(5,r'\unsure{57}','Clipped top-right number compatible with 57','retained_uncertain','Upper edge removes part of the digits.'),
(11,r'\inserted{(mais sans imposer le rang de $\underline{G}$)}','Handwritten parenthetical insertion with G underlined','confirmed','All words and the insertion attachment before est appelé are legible.'),
(11,'sous-variété','sous-variété at right edge','confirmed','Final accented letter is clipped; the page comment remains.'),
(20,r'\xout{x}','Dark x-like mark at end of variable','retained_uncertain','The cancellation/overtyping is retained; the curved insertion line also meets this place.'),
(20,r'\inserted[typed]{$(n\geqslant 1)$}','Typed (n greater-or-equal 1) above line','confirmed','Monospaced letters and handwritten placement stroke are distinguishable; insertion belongs before the stop.'),
(27,r'\inserted[typed]{de rang r}','Typed de rang r above line','confirmed','Every word and insertion point after libre checked.'),
(27,r'soit $\underline{E}$ son dual','soit E son dual, E underlined without a dual mark','confirmed','The missing accent is visible as an absence in the typed line; no mathematical correction made.'),
(29,'Grass_n(E)','First displayed E has no underline; opening parenthesis overtyped','confirmed','The formula retains the visibly plain E. The damaged parenthesis remains a parenthesis reading.'),
(30,'quotient','quotient with overtyped letters','confirmed','The complete word remains legible beneath the overtyping.'),
(32,r'\inserted[typed]{duale $L^{o}$}','Typed duale L with raised small o','confirmed','The insertion stroke puts it after linéaire; the overtyped letters in linéaire remain readable.'),
(33,r'\inserted{i.e. de codim relative m+1 dans $\check{P}$}','Handwritten i.e. de codim relative m+1 dans dual P','confirmed','Wording, plus sign, and V-shaped mark over P read directly.'),
(34,'ainsi,','ainsi followed by edge-clipped punctuation','retained_uncertain','Right edge cuts the terminal stroke; supplied comma is retained.'),
(38,r'\mspage{64}','64 in pencil','confirmed','Bottom foliation read directly.')
],30,'Both scan parts read completely with overlap counted once; all insertions, overwritten words, dual marks, and displayed isomorphisms inspected. The unaccented E in soit E son dual is retained as printed.')
finish(65,[
(8,r'\unsure{permettant|permettamt}','permettant','The final n and t are separately visible despite the overtyping.'),
(12,r'\xout{xxxxx}',r'\xout{dans}','The underlying d-a-n-s is legible in the upper scan beneath x cancellation.'),
(13,r'\xout{qxx}',r'\xout{\unsure{que}}','q and traces consistent with u-e remain under the two x characters; retain doubt.'),
(23,r'\xout{\unsure{nt}}',r'\xout{nt}','The two cancelled letters after sera are legible.'),
(23,r'\xout{\unsure{s}}',r'\xout{s}','The cancelled final s of rédigés is legible.'),
(25,r'\xout{xxbxix}',r'\xout{\illegible{1}}','The cancellation characters do not supply a readable underlying word; preserve an illegibility mark instead of printing x marks as words.'),
(29,r'\unsure{\bullet}',r'\unsure{\bullet|*}','The small subscript may be a point or an asterisk; both visible possibilities are retained.'),
(34,r'\uline{Grass}$_{n}(\underline{E})$',r'\uline{Grass}$_{\unsure{n}}(\underline{E})$','The index after the coproduct summand Grass is not clearly separated from its underline; retain the source candidate with doubt.')
],[
(6,r'\unsure{33}','Only lower portions of two top-edge digits','retained_uncertain','Upper crop prevents a secure reading.'),
(6,r'\hand{60}','60 in pen','confirmed','Full number at upper right is legible.'),
(8,r'\over{L}{\unsure{l}}','Typed initial with small pen correction above','retained_uncertain','The pen mark supports a lowercase l but does not clearly erase all of the capital form.'),
(8,r'\hand{\check{}}P','Pen V accent above typed P','confirmed','V stroke is handwritten and centered above P.'),
(8,r'\hand{,} after P','Pen comma after P','confirmed','Comma sits below the typed baseline.'),
(8,r'\xout{xxxSi}','x cancellation before the repeated S','retained_uncertain','Underlying first word remains obscure; no additional letters supplied.'),
(8,r'\hand{,} after disons','Pen comma at right edge','confirmed','Lower curve remains visible at the edge.'),
(11,r'\xout{\unsure{va}}','Overtyped va position in sous-variété','retained_uncertain','v/a strokes cannot be separated from cancellation.'),
(11,r'\over{u}{û}','Pen circumflex over typed u','confirmed','Circumflex is written above the typewriter letter.'),
(14,r'\margin{|}','Vertical pen stroke in left margin','confirmed','Stroke spans the following parenthetical lines.'),
(14,r'\inserted[typed]{sous-}','Typed sous- above variété','confirmed','Monospaced insertion retained at its marked location.'),
(14,r'\inserted[typed]{L de P}','Typed L de P above détermine','confirmed','Insertion line attaches before détermine.'),
(14,r'\hand{,}','Pen comma after inserted P','confirmed','Comma and attachment curve checked.'),
(15,r'\unsure{G}','Underlined overtyped quotient letter G with another bowl','retained_uncertain','G remains plausible; underlying letter cannot be recovered securely.'),
(17,r'\hand{\hookrightarrow}','Pen inclusion arrow from P(G prime) toward P(G)','confirmed','Hook and right-pointing direction visible.'),
(18,r'\hand{\rightarrow}','Pen arrow from P(G prime) to P(G)','confirmed','Rightward arrow direction checked.'),
(19,r'\hand{\rightarrow}','Pen arrow from G to G prime','confirmed','Rightward arrow direction checked.'),
(17,'ssi','ssi at right crop','confirmed','Visible letters agree with the transcription.'),
(25,r'\deleted{12. ...}','Whole section-12 heading struck by long pen line','confirmed','Heading reads Ratrappage de résultats ... sur les sections linéaires; cancellation covers the complete heading.'),
(27,r'\hand{Il me semble commode d\'introduire}','Handwritten first line','confirmed','Each word read directly in enlarged crop.'),
(28,r'\hand{aussi le foncteur}','Handwritten second line','confirmed','All words read directly.'),
(29,r'\hand{Grass...ens des Modules quotients}','Handwritten displayed functor and definition','confirmed','Grass underlined, E underlined, S prime, equality and the words checked.'),
(30,r'\hand{loc. libres (de rang}','Handwritten next line','confirmed','Abbreviation and open parenthesis retained.'),
(31,r'\hand{non précisé) de E_S prime}','Handwritten next line','confirmed','Words, close parenthesis, E underline and S prime index checked.'),
(33,r'\hand{Alors ... est représentable par}','Handwritten next line','confirmed','Wording verified; doubtful Grass subscript remains marked.'),
(33,r'\unsure{*}','Small star-like subscript','retained_uncertain','Two small strokes could also be a point with a tail.'),
(34,r'\hand{coprod...Les sous-variétés linéaires}','Handwritten coproduct and next phrase','confirmed','Coproduct has n greater-or-equal 0; sous-variétés linéaires has the long underline.'),
(35,r'\hand{de P(E) sont en fait définis par les}','Handwritten next line','confirmed','The masculine définis is visible and retained.'),
(36,r'\hand{sections de Grass...sur S [NB. le}','Handwritten next line','confirmed','Square bracket before NB retained.'),
(36,r'\unsure{*}','Small star-like Grass subscript','retained_uncertain','Index remains too small for certainty.'),
(37,r'\hand{rang i.e. la dim relative peut varier si S non connexe)}','Handwritten final line','confirmed','All words and the closing parenthesis checked; mixed bracket styles retained.'),
(39,r'\hand{65}','65 in pencil at bottom left','confirmed','Number read directly.')
],28,'Both parts read fully, including ten-line handwritten addition and cancelled heading. Handwritten addition enlarged and reread. All typed and handwritten arrows compared for direction; unresolved subscripts retained.')
finish(66,[
(14,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent over P is a handwritten V, distinguishable from the typed letter.'),
(14,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The dual accent over underlined E is handwritten.'),
(19,r'\mathrm{Gr}_{\unsure{m+1}}(\check{\underline{E}})',r'\mathrm{Gr}_{m\deleted{\unsure{+1}}}(\overset{\hand{\vee}}{E})','Enlarged crop shows a plain typed m followed by a pen cancellation over the doubtful +1. The dual V is handwritten and the E at this occurrence has no underline.'),
(23,r'$P_S$',r"$P_{S'}$",'The prime after subscript S is visible in the scan.'),
(24,r'$P_S$',r"$P_{S'}$",'The prime after subscript S is also visible at the second occurrence.'),
(28,r'\check{\underline{G}}',r'\overset{\hand{\vee}}{\underline{G}}','The V accent above G is handwritten.'),
(29,r'\check{G}_T \longrightarrow',r'\overset{\hand{\vee}}{G}_T \hand{\longrightarrow}','Both the dual mark and the displayed arrow are handwritten; G itself lacks an underline in this display.'),
(31,r'\unsure{du|da}','da','The enlarged word shows the typed a, with its closed bowl and upper arch; the printed da is retained.'),
(31,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The V accent above E is a separate pen stroke.'),
(31,r'\underline{G}_T{}^{\vee}',r'\underline{G}_T\mathrm{v}','The scan places an ordinary typed lowercase v on the baseline after G subscript T; it is not raised as an exponent.'),
(32,r'\longrightarrow',r'\hand{\longrightarrow}','The displayed arrow is drawn with a continuous pen stroke.'),
(34,r'\phi^m \in \Gamma',r'\hand{\phi}^m \hand{\in} \hand{\Gamma}','The phi, membership sign, and capital Gamma are handwritten between the typed letters and delimiters.')
],[
(5,r'\hand{\unsure{21}}','Clipped pen folio at top right','retained_uncertain','The first digit is cut by the upper page edge; 21 remains the supplied visible candidate.'),
(7,r'\uline{Généralisation de résultats antérieurs aux sections linéaires}','Typed section title with underline','confirmed','All words and the section number 12 checked.'),
(13,r'\xout{\unsure{de rang}}','Typewriter cancellation over de rang','retained_uncertain','Some underlying letter strokes remain merged with the x marks.'),
(20,r'\inserted{G}','Handwritten underlined G above quotient','confirmed','Caret attaches G after quotient; all visible letters retained.'),
(20,'canoniqu','Right-edge clipped canoniqu','confirmed','No missing final letter supplied.'),
(21,r'\xout{\unsure{La relation di}}','Typewriter cancellation before Le préschéma','retained_uncertain','Underlying letters support the proposed phrase; the end is indistinct.'),
(26,r'\xout{E}','E cancelled before T','confirmed','The typewriter cancellation and repeated T are visible.'),
(36,r'\hand{66}','66 in pencil','confirmed','Bottom-left foliation read directly.'),
(9,'All ordinary text and notation','All lines including rank r+1 followed later by rank r','confirmed','The rank switch and the typed soit F are preserved exactly; no mathematical repair is inferred.')
],29,'Both scan parts fully read; enlarged the cancelled Grass index and da/G_T v line. Confirmed primes after S, all dual marks and arrows, and the baseline v. No mathematical normalization applied.')
finish(67,[
(5,r'\unsure{56}',r'\unsure{62}','The surviving lower curves of the clipped pen number support 62; the top remains missing, so uncertainty stays.'),
(9,r'$\phi^{m}$',r'$\hand{\phi}^{m}$','The phi is a handwritten looped glyph; superscript m is typed.'),
(13,r'\xout{\unsure{Y}}',r'\deleted{\unsure{\underline{Y}}}','The cancellation is an irregular pen stroke over an underlined letter, not typewriter x marks.'),
(13,r'\inserted{sur P}',r'\inserted[typed]{sur P}','Both words use typewriter glyphs above the line; only the placement curve is handwritten.'),
(14,r"\inserted{sur $P_{S'}$}",r"\inserted[typed]{sur $P_{S'}$}",'The inserted sur and P with S prime are typed above the line.'),
(29,'co mme','comme','The word has continuous ordinary typewriter spacing in the scan.'),
(33,r'\inserted{P-}',r'\inserted[typed]{P-}','P and hyphen have typewriter outlines; the caret is handwritten.'),
(34,r'\unsure{1}','1','The separate typewritten digit beneath Grass is legible; its anomalous position is retained.'),
(35,r'\xout{xxxxxx}',r'\xout{\unsure{est un}}','The underlying est is clear; the following two cancelled letters support un but are not fully separable.'),
(35,r'\simeq',r'\hand{\simeq}','The overtraced isomorphism symbol is written by hand.'),
(35,r'\underline{\Omega}',r'\hand{\underline{\Omega}}','The large Omega and its underline are drawn in pen.'),
(35,r'\longrightarrow \mathcal{O}_{X}(1)',r'\hand{\longrightarrow} O_{X}(1)','The arrow is handwritten and the target is an ordinary typewriter O with no script alphabet or underline.')
],[
(7,'préschémad’incidence','Overtyped pr, no gap before d’incidence','confirmed','The typed collision and spacing are retained.'),
(12,r'\hand{\zeta}','Pen zeta after lorsque','confirmed','Handwriting and glyph shape checked.'),
(12,r'\unsure{\mathrm{Gr}}','Overtyped first letter of Gr','retained_uncertain','G/overstrike remains indistinct; the supplied reading is not silently resolved.'),
(13,r'\hand{\zeta}','Pen zeta as subscript of Y superscript m','confirmed','Position and glyph read directly.'),
(17,r'\margin{$|$}','Long pencil rule beside autocritique paragraph','confirmed','The rule spans this paragraph and ends near the next one.'),
(17,r'\xout{xx}','Two x cancellation impressions after une','confirmed','Visible cancellation impressions retained; underlying content cannot be recovered.'),
(20,r'\xout{x}','One cancelled terminal impression after quoi','confirmed','Scan shows this small overstrike at right.'),
(25,r'\hand{.}','Pen stop after the exponent identity','confirmed','Terminal stop at right edge is visible.'),
(27,r'\unsure{e}','Final letter at clipped right edge','retained_uncertain','The page edge cuts most of the final letter.'),
(34,r'\xout{\$}','Overtyped glyph before opening parenthesis','retained_uncertain','The dollar-like overstrike remains visible; its layer is not fully separable.'),
(34,r'\hand{\vee}','Pen V dual mark above F','confirmed','Ink and centered placement checked.'),
(35,r'\hand{,}','Pen comma at end of last line','confirmed','Comma read in enlarged lower crop.'),
(37,r'\mspage{67}','67 in pencil','confirmed','Bottom-left archive number read directly.')
],29,'Both complete parts and lower-line enlargement read. Notational self-criticism paragraph checked in full; proposed X notation and its printed identity retained, with no asserted mathematical correction.')
finish(68,[
(7,'avec des fibres',r'avec des\hand{/}fibres','A pen slash separates the typed des/fibres collision; mark the inserted space rather than silently printing it as original typing.'),
(11,r'\margin{|}grassmani',r'grassmani','This is the continuation of the single pencil bracket anchored on the preceding line, not a second marginal note.'),
(12,r'\margin{|}par toi',r'par toi','The pencil bracket continues to this line; do not duplicate it as a third note.'),
(21,r'\leqslant',r'\hand{\leqslant}','The comparison sign is a free pen stroke.'),
(21,r'\hand{\unsure{1}}',r'\hand{1}','The handwritten digit has a clear upright stroke and foot.'),
(22,r'\xout{xxxxxx}',r'\xout{section}','The underlying s-e-c-t-i-o-n remains readable through the typewriter x marks.'),
(24,r'\unsure{eu}',r'\unsure{eu|uu}','The overtyped middle vowel supports either the supplied eu or the visibly repeated u form.'),
(25,r'\xout{\illegible{1}}',r'\unsure{il}','The terminal word shows overtyped i/l-like strokes without a row of x cancellation; retain it as a live doubtful reading.'),
(28,'$<$ 0',r'$\hand{<}$ 0','The less-than sign is handwritten.'),
(29,r'\leqslant',r'\hand{\leqslant}','The second comparison sign in the quoted replacement is handwritten.'),
(31,'$>$ 0',r'$\hand{>}$ 0','The greater-than sign is a handwritten pair of strokes.'),
(31,r'\geqslant',r'\hand{\geqslant}','The greater-or-equal sign is handwritten.'),
(33,r'\leqslant',r'\hand{\leqslant}','The final less-or-equal sign is handwritten.')
],[
(5,r'\mspage{63}','63 in pen','confirmed','Both digits are visible at top right.'),
(8,r'\inserted[typed]{de dimension m(r-m),}','Typed insertion after rationelles)','confirmed','The lower placement curve attaches there; the separate upper pen slash is preserved at the des/fibres boundary.'),
(10,r'\margin{|}','Single pencil bracket spanning three lines','confirmed','Bracket begins beside comme and ends beside par toi; extent recorded once.'),
(11,r'\xout{z}','Overtyped letter inside grassmaniennes','retained_uncertain','The small crossed glyph remains compatible with z but is not cleanly separable.'),
(11,r'\over{\unsure{f}}{f}','Retouched f of finir','retained_uncertain','Pen retouch is visible, while the original glyph remains partly hidden.'),
(11,r'\over{\unsure{gu}}{\unsure{g}}','Pen correction over middle of maguifiés','retained_uncertain','The visible pen descender supports g; the obscured typed letters and intended result are not reconstructed.'),
(15,r'\hand{\vee}','Pen dual sign over underlined G','confirmed','V stroke directly visible; tiny dot near E is a nonalphabetic mark, recorded in this decision.'),
(21,r'\xout{dimxx}','Typewriter-cancelled material before dim x bar','retained_uncertain','Underlying word remains mixed with x impressions; supplied visible transcription is retained.'),
(25,r'\xout{i}','Overtyped i in fait','confirmed','Extra i impression cancelled in the scan.'),
(28,r'\xout{\unsure{x}}','Crossed glyph inside signifie','retained_uncertain','The overwritten glyph is still indistinct.'),
(29,r'\xout{mxx}','Cancelled m and following impressions','retained_uncertain','Underlying following characters cannot be separated from cancellation.'),
(36,r'\margin{68}','Pencil archive foliation 68','confirmed','Content read directly; supplied margin macro retained.'),
(9,'c as; propositi on; r emplaçant; s emble; d ’un','Irregular typewriter spacing','confirmed','Spacing checked against the scan and preserved; no language standardization applied.')
],28,'Both complete scan parts read; all comparison signs checked for writing layer. The author’s references 2.1 through 2.12, jokes, spelling, and rank/dimension notation are retained. Pencil bracket treated as one note.')
finish(69,[
(5,r'\mspage{69}',r'\mspage{64}','The upper-right pen folio reads 64; 69 is the separate archive number at the bottom.'),
(7,r'\inserted{\unsure{plus bas}}',r'\inserted{plus bas}','Both handwritten words and insertion curve before commentaires are clear.'),
(22,r'\unsure{du|da}','da','The typewritten second letter is a, including its bowl; retain the printed da.'),
(28,r'$\phi$',r'$\hand{\phi}$','The phi at the beginning of the paragraph is handwritten.'),
(28,r'$\phi^{(m)}$',r'$\hand{\phi}^{(m)}$','The phi is handwritten and its parenthesized superscript is typed.'),
(29,r'\xout{\unsure{et la condition}}',r'\xout{et la condition}','All underlying words can be read through the x cancellation.'),
(30,r'$\phi^m_',r'$\hand{\phi}^m_','The phi in the specialized section is handwritten.'),
(32,r'$\phi$',r'$\hand{\phi}$','The phi in section phi is handwritten.'),
(33,r'\margin{$\|$} cela',r'ce\deleted{\ }la','The scan shows ce and la separated in typing, joined by a pen stroke that removes the space. The same marginal bar is already anchored on the preceding line.'),
(34,r'\margin{$\|$} $\underline{F}$',r'$\underline{F}$','The single marginal bar continues; a duplicate note is removed.'),
(35,r'\margin{$\|$} suite',r'suite','The single marginal bar continues to this line; a fourth duplicate note is removed.')
],[
(8,r'\hand{\leqslant}','Pen less-or-equal sign','confirmed','Both angled sign and lower stroke appear handwritten.'),
(9,r'\hand{\leqslant}','Second pen less-or-equal sign','confirmed','Stroke shape and placement checked.'),
(9,r'\xout{x}','Terminal cancellation after quel','confirmed','Typewriter overstrike retained.'),
(10,r'\xout{2x}','Cancelled 2 and impression before 2.17','confirmed','Both printed cancellation and replacement reference checked.'),
(10,r'\hand{\leqslant}','Third pen less-or-equal sign','confirmed','Stroke shape and placement checked.'),
(13,r'\hand{\geqslant}','Pen greater-or-equal sign','confirmed','The full comparison sign is drawn by hand.'),
(14,r'\hand{?}','Small pen question mark over hypersurfaces','confirmed','Question mark has a visible hook; retain at that word.'),
(15,r'\xout{x}','Cancellation after s’en','confirmed','Small typewriter overstrike retained.'),
(18,r'\hand{\geqslant} first','Pen comparison after f(X)','confirmed','Read directly.'),
(18,r'\hand{\geqslant} second','Pen comparison after f(X_i)','confirmed','Read directly; index i and bound 2 retained.'),
(19,r'\hand{\geqslant}','Pen comparison before m+1','confirmed','Read directly.'),
(19,r'\xout{x}','Cancellation after la','confirmed','Typewriter overstrike retained.'),
(19,r'\hand{\unsure{C alphabets}}','Large looped pen C-like symbol','retained_uncertain','The shape supports the supplied script/fraktur possibilities; no alphabet normalization.'),
(20,r'\hand{\leqslant}','Pen comparison in dim f(Z)','confirmed','Read directly.'),
(25,r'\hand{\geqslant m+1}','Whole handwritten bound greater-or-equal m+1','confirmed','Sign, m, plus and 1 are all written by hand.'),
(28,r'\xout{est un préschéma}','est un préschéma under typewriter x marks','confirmed','Underlying words remain readable.'),
(29,r'\xout{au dessus de}','au dessus de under typewriter x marks','confirmed','Underlying words remain readable.'),
(30,r'\hand{\xi} first','Handwritten specialized-section index','confirmed','Looped Greek letter and position checked without changing the supplied glyph.'),
(30,r'\xout{\unsure{(m)}}','Upper cancelled parenthesized m-like group','retained_uncertain','Typewriter cancellation obscures the parenthesis and one stroke.'),
(30,r'\xout{\illegible{1}}','Lower cancelled group','retained_illegible','Dense x impressions prevent recovery.'),
(30,r'\hand{\xi} in k()','Handwritten point symbol in first residue field','confirmed','Glyph checked against the repeated occurrences on the same line.'),
(30,r'\hand{\otimes}','Handwritten tensor product sign','confirmed','Circled cross lies after (1).'),
(30,r'\hand{\xi} second k()','Handwritten point symbol in tensor subscript','confirmed','Glyph and subscript placement checked.'),
(30,r'\hand{\xi} in G()','Handwritten point symbol in G parentheses','confirmed','Glyph and parentheses checked.'),
(30,r'\hand{\xi\in}','Handwritten point symbol and membership sign','confirmed','Both strokes are handwritten.'),
(32,r'\margin{$\|$}','Single shaded double vertical bar across final four lines','confirmed','One marginal mark is anchored here with extent described in this record.'),
(37,r'\mspage{69}','69 in pencil at bottom','confirmed','Archive foliation read directly.')
],28,'Both images read in full; every displayed inequality and the long tensor-expression line checked. Four duplicate encodings of one marginal stroke reduced to one; handwritten word-joining correction recorded.')
finish(70,[
(13,r'$\phi_',r'$\hand{\phi}_','The phi before the point subscript is handwritten.')
],[
(5,r'\mspage{65}','65 in pen','confirmed','Upper-right number read directly.'),
(7,r'\hand{/}','Pen slash between base and choisie','confirmed','Slash marks the typewritten word boundary and is retained visibly.'),
(10,r'\xout{généralisation}','Typed généralisation cancelled with x impressions','confirmed','Every underlying letter remains readable.'),
(10,r'\inserted[typed]{\xout{variante pour le}}','Typed variant above the line, itself cancelled by typewriter x marks','confirmed','The layered correction is visible independently of the final insertion.'),
(11,r'\inserted[typed]{généralisation au}','Typed final insertion above cas','confirmed','Curved pen line places it before cas.'),
(12,r'\xout{au}','Typed au cancelled before cas','confirmed','Cancellation matches the duplicated au in the final insertion.'),
(12,r'\xout{\unsure{Sm}}','Cancelled short typed group','retained_uncertain','Underlying letters remain obscured; no new reading supplied.'),
(12,r'\inserted[typed]{(S_m)}','Typed parenthesized S subscript m above line','confirmed','Letter, subscript, and parentheses checked.'),
(13,r'\hand{\xi}','Pen point subscript','confirmed','Loops and subscript position checked.'),
(15,r'\unsure{m|p}','Overtyped letter in Théorème','retained_uncertain','Descender and m-like arches overlap.'),
(17,r'\uline{Proposition}','Wavy handwritten underline below Proposition','confirmed','All letters remain readable through the underlining.'),
(17,r'\hand{\geqslant}','Pen comparison before m+1','confirmed','Sign read directly.'),
(18,r'\hand{\leqslant}','Pen comparison before m-1','confirmed','Sign read directly.'),
(22,r'\unsure{a}','Overtyped a position in notation','retained_uncertain','Extra letter impressions prevent a unique layer reading.'),
(26,r'\unsure{a}','Overtyped l/a before cancelled hypothèse','retained_uncertain','The supplied final a reading remains compatible with ink.'),
(26,r'\xout{hypothèse}','Typed hypothèse cancelled','confirmed','The full word can be read beneath x marks.'),
(26,r'\hand{\xi}','Point subscript on first Y','confirmed','Handwritten Greek glyph read directly.'),
(26,r'\hand{>}','Handwritten comparison on first Y line','confirmed','Right-pointing greater-than sign checked.'),
(26,r'\unsure{1}','Right-edge clipped digit after dim X-','retained_uncertain','Last digit is cut; certainty not increased.'),
(27,r'\hand{\xi}','Point subscript on second Y','confirmed','Handwriting read directly.'),
(27,r'\hand{>} first','Greater-than sign after second Y','confirmed','Direction checked.'),
(27,r'\over{1}{m}','Pen m over typed digit','confirmed','The two-humped m and remaining upright of the typed 1 are visible.'),
(27,r'\hand{>} second','Greater-than sign in f(X_i)>0','confirmed','Direction and adjacent zero checked.'),
(28,r'\hand{\geqslant}','Pen greater-or-equal sign','confirmed','Sign read directly.'),
(31,r'\hand{/}','Pen slash between doute and un','confirmed','Word-boundary mark retained.'),
(32,r'\inserted{30,}','Pen insertion 30 comma before 31','confirmed','Caret and all three characters read directly.'),
(32,r'\hand{;}','Handwritten semicolon after closing parenthesis','confirmed','Dot and lower comma both present.'),
(33,r'\hand{il n’est d’ailleurs sans doute pas indispensable de}','First handwritten continuation line','confirmed','Every word checked, including pas.'),
(34,r'\hand{faire cet exercice, s’il te barbe de le faire.}','Second handwritten continuation line','confirmed','Every word and punctuation checked.'),
(36,r'\mspage{70}','70 in pencil','confirmed','Bottom-left foliation read directly.')
],29,'Both complete image parts read, including the two handwritten continuation lines. All layered corrections around généralisation and condition (S_m) checked in sequence; every formula sign inspected.')
finish(71,[
(7,'Pour autant que je puisse voir',r'\unsure{Pour autant|Pour étant autant} que je puisse voir','The dense cancellation leaves additional letters between Pour and autant; retain both the original reading and the visible possible intervening word.'),
(9,r'\unsure{e)}','e)','The letter and closing parenthesis are readable beneath the cancellation.'),
(12,r'\inserted{également}',r'\inserted[typed]{également}','The insertion consists of monospaced typewriter letters with a handwritten placement bracket.'),
(25,r'\xout{\illegible{1}}',r'\xout{\unsure{généraux}}','Visible letters under the typewriter cancellation support généraux; some middle strokes remain obscure.'),
(28,r'\hand{(}','% NOTE: the curved stroke before Dans is the insertion attachment, not a content parenthesis.\n','The curved stroke joins the interlinear insertion to its location; it supplies no separate parenthesis.'),
(28,r'\inserted{$=V^o$}',r'\inserted[typed]{$=V^o$}','The equals sign, serif V, and raised round o are typewritten above the line.'),
(29,r'\unsure{singuliers}',r'\unsure{singuliers|sigguliers}','The overtyped n/g position permits both the original reading and the visibly doubled-g form.'),
(29,r'$\phi^m$',r'$\hand{\phi}^m$','Phi is handwritten while the superscript m is typed.'),
(34,r'\xout{\illegible{3}}',r'\xout{\unsure{2, et X non vide}}','The cancelled line shows 2, et X and non-vide-like letters; retain a doubtful rather than certain recovery.'),
(35,r'\hand{(}','% NOTE: the curved stroke before coupent is the attachment of the interlinear insertion.\n','The curve connects the insertion and is not an independently written parenthesis.')
],[
(5,r'\mspage{66}','66 in pen','confirmed','Top-right number read directly.'),
(7,r'\xout{Pour ... notamment}','Long first line cancelled with x impressions','confirmed','All visible underlying words compared; initial ambiguity is separately marked.'),
(8,r'\xout{exact}','Interlinear exact cancelled','confirmed','The word exact remains legible.'),
(9,r'\xout{8.7 ... quelconque,}','Second full cancelled line','confirmed','Wording through n’admet pas d’analogue évident pour m quelconque read beneath cancellation.'),
(11,r'\unsure{el}','Overtyped pair in développements','retained_uncertain','Middle letters remain merged.'),
(12,"s'apdapter","s'apdapter",'confirmed','The extra p is visible; no spelling repair.'),
(17,r'\unsure{x}','Small x-like impression after D’autre','retained_uncertain','Mark sits below baseline; layer remains uncertain.'),
(18,'mieux; exercices; faite','Overtyped words still legible','confirmed','All three words read in context from the images, not repaired from expectation.'),
(27,r'\hand{\longrightarrow}','Handwritten f-arrow X to P','confirmed','Direction checked.'),
(28,r'\inserted[typed]{à composantes de dimension ... m.}','Typed interlinear addition','confirmed','Words and insertion location before Dans read directly.'),
(28,r'\hand{\geq}','Pen greater-or-equal sign inside typed insertion','confirmed','Both sign and bound m checked.'),
(28,r'\hand{.}','Pen stop after insertion','confirmed','Dot is visible beside S comma.'),
(28,r'\xout{xxx}','Cancelled impressions below new V superscript o','confirmed','Typewriter x cancellation retained.'),
(30,r'\hand{\xi} first','Handwritten point in ordered pair','confirmed','Glyph, comma, and parentheses checked.'),
(30,r'\hand{\xi} second','Handwritten index of L','confirmed','Subscript position checked.'),
(34,r'\inserted[typed]{est quelconqué}','Typed interlinear phrase with final accent','confirmed','Insertion is typed; supplied accented ending remains as visible.'),
(34,r'\hand{\longrightarrow}','Handwritten projection arrow to X','confirmed','Rightward direction checked.'),
(35,r'\inserted{\unsure{passant par x et qui}}','Handwritten insertion over coupent','retained_uncertain','The word forms support the reading; compressed pen strokes prevent full certainty.'),
(36,r'\hand{\unsure{\ni x}}','Pen contains sign and x after T','retained_uncertain','Direction appears to be contains; the small interior stroke is indistinct.'),
(38,r'\margin{71}','71 in pencil','confirmed','Bottom-left archive number read directly.')
],30,'Both images fully read, with the top cancelled paragraphs and lower insertion layers checked. Attachment curves distinguished from textual parentheses; all retained doubtful readings remain explicit.')
finish(72,[
(13,r'$\underline{X}$x',r'\xout{$\underline{X}$}','The underlined X is overtyped with x cancellation; it must not remain live text.'),
(13,r'\xout{xxxxxxxxx}',r'\xout{autre que}','The underlying autre que is readable through the x marks.'),
(15,'filtration du','filtration da','The second letter of the typed word is an a; retain the printed grammatical slip.'),
(16,'L variables',r'L v\unsure{a}riables','The a position is overtyped/weak and cannot be securely separated from adjacent letters.'),
(20,r'\margin{$|$} le lemme','le lemme','This line continues the one pencil bracket anchored above; no second marginal note.'),
(20,r'\hand{\unsure{)}}',r'\hand{\unsure{)|\S}}','The dark curved mark can be read as a parenthesis or section-like stroke; retain both candidates.'),
(21,r'\margin{$|$} rait','rait','The same pencil bracket continues; remove duplicate encoding.'),
(22,r'\margin{$|$} nes','nes','The same pencil bracket ends here; remove duplicate encoding.'),
(23,r'L \geqslant',r'L \hand{\geqslant}','The comparison sign after the intersection expression is handwritten.'),
(30,r'$\geqslant 4$',r'$\hand{\geqslant} 4$','The comparison before 4 is a pen addition.'),
(32,r'$\geqslant$ 2',r'$\hand{\geqslant}$ 2','The comparison before 2 is handwritten.')
],[
(5,r'\mspage{67}','67 in pen','confirmed','Number read directly.'),
(7,r'\hand{\zeta}','Handwritten point symbol','confirmed','Glyph and baseline placement checked.'),
(8,r'\hand{\cap}','Small pen intersection sign','confirmed','Curved connecting strokes distinguish it from neighboring typed letters.'),
(8,r'\hand{\zeta}','Handwritten subscript of L','confirmed','Glyph and position checked.'),
(9,r'\unsure{è|e}','Damaged accent/letter at end of normale','retained_uncertain','Small upper stroke does not securely distinguish an accent from the overtype.'),
(12,r'\hand{\zeta} first','Point symbol after first L','confirmed','Read directly.'),
(12,r'\hand{\cap}','Intersection sign in T_x intersection L','confirmed','Pen stroke and position checked.'),
(12,r'\hand{\zeta} second','Point symbol after second L','confirmed','Read directly.'),
(12,r'\hand{\geqslant}','Pen greater-or-equal sign','confirmed','Direction and lower stroke checked.'),
(12,r'\hand{)}','Faint curved closing stroke after n-m+2','confirmed','Curved mark is present and retained without inferring its role.'),
(13,r'\xout{\unsure{mx}}','Cancelled short material before est','retained_uncertain','Underlying letters remain obscured.'),
(13,r'\inserted{exactement}','Handwritten exactement before l’ensemble','confirmed','Word and attachment curve read directly.'),
(14,r'\xout{\unsure{i}}','Overtyped glyph in vérification','retained_uncertain','The cancelled glyph remains compatible with i.'),
(14,r'\unsure{t}','Right-edge final t in demanderait','retained_uncertain','Edge cuts its extremity.'),
(15,r'\xout{xx}','Short cancelled group after da','retained_uncertain','Underlying word not securely recoverable.'),
(15,r'\unsure{shhéma|schéma}','Overtyped word with doubled h-like strokes','retained_uncertain','Both readings remain consistent with visible layers.'),
(15,r'\xout{xxxxx}','Cancelled group after les','retained_uncertain','Dense overstrike prevents a safe recovery.'),
(19,r'\margin{$|$}','One pencil bracket alongside four lines','confirmed','Anchor and extent checked; duplicate encodings removed.'),
(22,r'\hand{)}','Handwritten closing parenthesis after nes','confirmed','Closing stroke clearly visible.'),
(22,r'\xout{V(k)}','Cancelled baseline V(k)','confirmed','Typed predecessor and raised replacement are visible.'),
(23,r'\hand{\cap}','Pen intersection sign','confirmed','Read directly.'),
(24,r'\xout{dim ... formula}','Cancelled two-line dimension formula','retained_uncertain','Legible dim, V(k), and portions of the polynomial remain; doubtful original candidate retained.'),
(26,r'\hand{\leqslant} first','Pen inequality k less-or-equal m','confirmed','Read directly.'),
(26,r'\hand{\leqslant} second','Pen inequality k less-or-equal r-m','confirmed','Read directly.'),
(27,r'\xout{xx}','Cancelled impressions after d','confirmed','Overstrike retained.'),
(29,r'\xout{x}','Cancelled character inside grassmaniennes','confirmed','Overstrike retained.'),
(31,r'\hand{\geqslant}','Pen codimension bound before 4','confirmed','Read directly.'),
(32,r'\inserted[typed]{de Grass^m}','Typed insertion before de codimension','confirmed','Handwritten loop places it immediately after d’ensembles.'),
(32,r'\xout{xxx}','Cancelled group before oublier','retained_uncertain','Underlying content not separately legible.'),
(35,r'\hand{\unsure{gé}}','Retouched ending of envisagé','retained_uncertain','Pen and typed strokes overlap; original candidate remains marked.'),
(37,r'\mspage{72}','72 in pencil','confirmed','Bottom foliation read directly.')
],30,'Both images read completely. Cancellation of initial underlined X corrected; all incidences and dimension formulas checked character by character. Authorial qualifications sauf erreur and references to complements §16 retained.')
finish(73,[
(10,r'\unsure{e}',r'\unsure{e|g}','The overwritten letter has an e top and a lower g-like bowl; keep both visible possibilities.'),
(11,r'$\phi^m$',r'$\hand{\phi}^m$','The phi is drawn by hand, with typed superscript m.'),
(12,r'\inserted{pré}',r'\inserted[typed]{pré}','The inserted prefix is typewritten above schéma and has a handwritten placement curve.'),
(20,r'\inserted{géométrique}',r'\inserted[typed]{géométrique}','The entire inserted word uses the typewriter face; the placement curve is handwritten.'),
(23,r'\inserted{de}',r'\inserted[typed]{de}','The inserted de is typed above the line.'),
(24,r'\xout{xxxxxx}',r'\xout{un peu}','Underlying un peu remains readable below the x impressions.'),
(36,r'\unsure{ariét}',r'\over{\unsure{ariét}}{\unsure{ariét}}','The middle of sous-variétés contains pen retouches over the typewritten letters; the exact underlying and final letters remain uncertain.')
],[
(5,r'\mspage{68}','68 in pen','confirmed','Top-right folio read directly.'),
(7,r'\xout{v}','Overtyped group in relativement','retained_uncertain','The cancellation layer is visible; exact overwritten character remains unclear.'),
(7,r'\xout{xx}','Typewriter cancellation after en','confirmed','Two overstrike impressions read directly.'),
(12,r'\hand{\cup}','Handwritten union sign','confirmed','Open U-shaped pen stroke checked.'),
(13,r'\hand{\longrightarrow}','Handwritten arrow to Grass','confirmed','Rightward direction checked.'),
(13,r'\unsure{r}','Retouched r of Grass','retained_uncertain','Upper dash and lower r-like overtype remain visible; no layer reconstruction forced.'),
(15,r'\hand{)}','Pen closing parenthesis adjacent to typed closing parenthesis','confirmed','Both closing strokes are present, so both retained.'),
(17,r'\margin{|}','Long pencil rule beside paragraph','confirmed','Runs from De cette façon through un corps.'),
(17,r'\margin{+}','Small cross-like mark beside Il at right edge','confirmed','Mark is visible beside the word and retained.'),
(18,r'\xout{xxx}','Cancelled short word before utilisant','retained_uncertain','Underlying word remains obscure.'),
(19,r'\xout{structure}','Typewriter-cancelled structure','confirmed','Complete word read beneath cancellation.'),
(20,r'\deleted{et qui}','et qui crossed by pen','confirmed','Cancellation is irregular pen ink over the typewritten words.'),
(20,r'\inserted{cela}','Handwritten cela above deleted words','confirmed','Insertion replaces the cancelled phrase.'),
(20,r'\inserted{encore}','Handwritten encore after implique','confirmed','Word and placement curve checked.'),
(29,r'\unsure{tte}','Retouched ending of cette','retained_uncertain','Dense overtyping/retouch obscures the ending; no doubt removed.'),
(30,r'\hand{,}','Pen comma after tion','confirmed','Curved pen stroke read directly.'),
(30,r'\xout{mêm}','Cancelled abbreviated même-like word','confirmed','Visible m-ê-m retained; no additional letter supplied.'),
(38,r'\margin{73}','73 in pencil','confirmed','Bottom-left archive foliation read directly.'),
(18,'Right-edge words','utilisant, dans, des, une partially clipped','confirmed','Visible portions agree with source; edge damage noted, not filled from an edition.')
],29,'Both scan parts completely read; every typed/pen insertion compared. Supersingular passage and the author’s qualified discussion of possible generalizations retained exactly; no conjectural mathematics promoted to a theorem.')
finish(74,[
(5,r'\unsure{61|6}',r'\unsure{69|61|6}','The clipped second figure has a long descending stroke and traces of an upper loop; add 69 as an ink-supported reading without settling the cut number.'),
(9,r'\longrightarrow X',r'\hand{\longrightarrow} X','The first projection arrow is handwritten.'),
(15,r'\longrightarrow Q',r'\hand{\longrightarrow} Q','The arrow to Q is drawn by hand.'),
(17,r'de dim $n \geq m$',r'de dim $n \hand{\geq} m$','The comparison sign in the otherwise typed insertion is handwritten.'),
(18,r'\zeta}\in Q',r'\zeta}\hand{\in} Q','Membership after the first point symbol is a pen addition.'),
(20,r'\zeta}\in T',r'\zeta}\hand{\in} T','Membership after the next point symbol is handwritten.'),
(22,r'X$\rightarrow$P',r'X$\hand{\rightarrow}$P','The arrow in f:X to P is handwritten.'),
(23,r'\zeta}\in$',r'\zeta}\hand{\in}$','Membership before T minus T1 is handwritten.'),
(25,r'$\longrightarrow$',r'$\hand{\longrightarrow}$','The arrow in the restored nonramification hypothesis is handwritten.'),
(26,r'$\phi_{n}f$',r'$\hand{\phi}_{n}f$','The phi in the Veronese-composition notation is handwritten.'),
(26,r'n $\geq$2',r'n $\hand{\geq}$2','The lower-bound comparison is handwritten.'),
(26,r'$\phi_{n}$',r'$\hand{\phi}_{n}$','The repeated phi is handwritten.'),
(34,r'\cap Z',r'\hand{\cap} Z','The intersection sign in the last typed line is handwritten.'),
(34,r'$\geq$ q',r'$\hand{\geq}$ q','The final codimension comparison is handwritten.')
],[
(5,r'\hand{page number}','Pen folio clipped by top edge','confirmed','Writing layer confirmed; reading remains marked.'),
(11,r'\unsure{àu}','Overtyped accented a/u phrase','retained_uncertain','Ink above a and adjacent u cannot be assigned to a unique corrected spelling.'),
(12,r'\unsure{C}','Overtyped last factor in X times_P C','retained_uncertain','C-like letter is visible under an overstrike; no mathematical substitution.'),
(13,r'\over{10}{\unsure{18}}','Pen retouch over reference number 10','retained_uncertain','Second figure has overlapping loops; 18 remains a doubtful reading.'),
(14,r'\xout{r}','Cancelled terminal r after inclure','confirmed','Typewriter cancellation visible.'),
(17,r'\inserted[typed]{de dim ...}','Typed dimension insertion','confirmed','Wording and n/m letters checked; hand comparison separately marked.'),
(17,r'\xout{toutes}','Typewriter-cancelled toutes','confirmed','Word readable beneath x marks.'),
(17,r'\inserted[typed]{propre et}','Typed propre et above line','confirmed','Placement before géom irréd checked.'),
(18,r'\inserted[typed]{T}','Typed T after l’ensemble','confirmed','Insertion attachment checked.'),
(18,r'\hand{\zeta}','Pen point symbol in Q','confirmed','Glyph and position checked.'),
(18,r'\inserted[typed]{pas}','Typed pas after n’est','confirmed','Placement curve checked.'),
(19,r'\hand{\zeta} first','Pen point symbol in first k()','confirmed','Read directly.'),
(19,r'\hand{\zeta} second','Pen point symbol in second k()','confirmed','Repeated field notation retained exactly.'),
(19,r'\inserted[typed]{et de codim 1 dans Q}','Typed interlinear codimension addition','confirmed','All words and attachment after k(zeta) checked.'),
(19,r'\xout{pour}','Cancelled pour','confirmed','Underlying word readable.'),
(20,r'\inserted[typed]{T1}','Typed T with raised 1','confirmed','Insertion before des checked.'),
(20,r'\hand{\zeta}','Pen point symbol in T','confirmed','Read directly.'),
(21,r'\xout{r}','Cancelled first r before rare','confirmed','Small overstrike visible.'),
(21,r'\xout{\unsure{ainsi ... est}}','Long cancelled typed clause','retained_uncertain','Several variables and words remain obscured; source candidate retained with doubt.'),
(22,r'\xout{\unsure{n’admet que des points de}}','Cancelled following clause','retained_uncertain','Word sequence remains compatible with visible letters but not fully separable.'),
(23,r'\hand{\zeta}','Pen point symbol before T minus T1','confirmed','Read directly.'),
(24,r'\margin{|}','Pencil rule beside the restored hypotheses','confirmed','Runs from point non lisse through following argument lines.'),
(24,r'\hand{\zeta} index','Pen subscript on X superscript (m)','confirmed','Position and glyph checked.'),
(24,r'\hand{\zeta} field','Pen point symbol in k()','confirmed','Read directly.'),
(25,r'\xout{de}','Cancelled de before arrow','confirmed','Underlying word visible.'),
(27,r'\xout{semble}','Cancelled first semble','confirmed','Full word visible; later sem-ble retained.'),
(29,r'\xout{``supers}','Cancelled quoted prefix before Singulier','confirmed','Prefix cancellation and capital S checked.'),
(29,r'\unsure{double quote}','Overtyped closing quote near colon','retained_uncertain','Punctuation layers remain merged.'),
(31,r'\inserted{rait}','Handwritten rait after reste','confirmed','Caret and four letters checked.'),
(34,r'\unsure{Z|C}','Overtyped letter inside Q()','retained_uncertain','Z/C candidates remain supported by ink.'),
(35,r'\inserted{Q(C); de plus ...}','Complete handwritten final line','confirmed','Every word, Q(C), intersection Z, and final quoted assez général checked; final variable is Z in the source and retained.'),
(37,r'\hand{74}','74 in pencil','confirmed','Bottom-left archive number read directly.')
],31,'Both complete scan parts read, including the full handwritten ending. Every typed insertion and pen relation sign checked. The printed references and repeated k(zeta), including possible mathematical slips, are preserved.')

def finish_reviewed(site,changes,notes,summary):
 """Record occurrences only after this reviewer has completed the full visual comparison."""
 import re,csv
 key=f'ega25_25_{site:03}'
 src=source_path(key).read_text()
 rows=[]
 reasons={'hand':'Pen strokes, glyphs, and position compared with the scan.','over':'Underlying typing and superimposed pen correction compared.','inserted':'Insertion wording, writing layer, and attachment compared.','margin':'Marginal content and its line of attachment compared.','deleted':'Pen cancellation and the underlying content compared.','xout':'Typewriter cancellation and readable underlying text compared.'}
 pat=re.compile(r'\\(hand|over|inserted|margin|deleted|xout|unsure|illegible)\b')
 for m in pat.finditer(src):
  pos=m.end();name=m[1]
  if name=='inserted' and pos<len(src) and src[pos]=='[':
   close=src.find(']',pos);pos=close+1
  end=pos
  for arg in range(2 if name=='over' else 1):
   while end<len(src) and src[end].isspace():end+=1
   if end>=len(src) or src[end]!='{':break
   depth=1;end+=1
   while end<len(src) and depth:
    if src[end]=='\\':end+=2;continue
    if src[end]=='{':depth+=1
    elif src[end]=='}':depth-=1
    end+=1
  literal=src[m.start():end];line=src.count('\n',0,m.start())+1
  change=next((c for c in changes if literal in c[1] or (c[1] in literal and c[0]==line)),None)
  if change: rows.append((line,literal,change[2],'corrected_from_scan',change[3]))
  elif name=='unsure': rows.append((line,literal,literal,'retained_uncertain','The scan comparison does not remove the stated doubt; all printed candidates remain marked.'))
  elif name=='illegible':rows.append((line,literal,literal,'retained_illegible','The obscured source characters remain unreadable in the supplied images.'))
  else:rows.append((line,literal,literal,'confirmed',reasons[name]))
 rows.extend(notes)
 count=sum(bool(l.strip()) and not l.lstrip().startswith(('%',r'\scanpage')) for l in src.splitlines())
 return finish(site,changes,rows,count,summary)

finish_reviewed(75,[
(7,r'\uline{Morphismes élémentaires et théorème de M. Artin}',r'\uline{Morphismes élémentaires et théorème de} M. \uline{Artin}','The underline stops before M. and resumes under Artin; do not underline the intervening M.'),
(9,r'f:X\to Y',r'f:X\hand{\to} Y','The arrow in the definition is handwritten.'),
(10,r'\unsure{élém}','élém','The four underlying letters and accents are readable through cancellation.'),
(10,r'\unsure{un}','un','Both cancelled letters are visible.'),
(11,r"X'\to X",r"X'\hand{\to} X",'The arrow is handwritten; its target is visibly X, retained as printed.'),
(13,r'\unsure{étale sur}','étale sur','Both words are readable beneath x cancellation.'),
(13,r'Z\to Y',r'Z\hand{\to} Y','The arrow is drawn by hand.'),
(17,r'X\to \mathrm{Spec}',r'X\hand{\to} \mathrm{Spec}','The structural-morphism arrow is handwritten.'),
(23,r'\unsure{peutxsuppo}',r'\unsure{peut suppo}','The x impressions cancel the text; they are not part of the readable underlying words.'),
(26,r'\unsure{peutxsupposer}','peut supposer','The underlying phrase is readable; the x impressions are cancellation marks.'),
(26,r'$n>0$',r'$n\hand{>}0$','The comparison sign within the typed insertion is handwritten.'),
(27,r'U\to V',r'U\hand{\to} V','The arrow is handwritten.'),
(29,r'\unsure{Lorsque n=1}','Lorsque n=1','The full cancelled phrase can be read beneath the x marks.')
],[
(5,'Top and bottom foliation','70 above;75 below','confirmed','Both numbers read directly from the images.'),
(19,'Typed theorem insertions','(M.Artin), géom. irréd., parfait infini','confirmed','Every word, typing layer, and insertion curve inspected.'),
(23,'Handwritten rewrite','il revient au / même de','confirmed','Both parts read directly above the cancelled opening.'),
(25,'Layered deleted passage and typed addition','On peut supposer évidemment X lisse, et; et affine','confirmed','Both passages are crossed by pen; the interlinear et affine is typed.'),
(31,'Retouched l in n’exclut','Pen retouch over the letter','confirmed','Letter and writing layer checked.'),
(29,'qu’alors correction','Apostrophe-like pen stroke over e','confirmed','Both layers retained in the overwrite macro.'),
(11,'Definition target','X prime to X','confirmed','The scan explicitly prints X as target. This is retained and will be noted in the guide alongside the Y-based definition.')
],'Both complete image parts read, including every cancelled phrase and layered proof correction. All morphism arrows checked for direction, target, and handwriting; no mathematical substitution applied.')
finish_reviewed(76,[
(10,r'$n \geqslant 2$',r'$n \hand{\geqslant} 2$','The composite greater-or-equal sign consists of pen strokes.'),
(13,r'\unsure{lisse et}','lisse et','Both cancelled words are readable.'),
(13,'affine donc quasi-projectif',r'affine donc quasi-\unsure{projectif|prowjectif}','An extra w-like impression is visible near pro/jectif; retain both readings rather than normalize the word.'),
(16,r'U \to V',r'U \hand{\to} V','The arrow is handwritten.'),
(21,r'$\geqslant 2$',r'$\hand{\geqslant} 2$','The codimension comparison is handwritten.'),
(21,r'\unsure{Soit Noter qui}',r"\unsure{Soit Noter qu'on}",'The visible ending is qu followed by an apostrophe-like impression and on, under x cancellation.'),
(22,r'\longrightarrow P^r',r'\hand{\longrightarrow} P^r','The immersion arrow is handwritten.'),
(25,r'$n > 0$',r'$n \hand{>} 0$','The greater-than sign is handwritten.'),
(28,r'x \notin Y',r'x \hand{\notin} Y','Membership and its cancellation stroke are pen additions.'),
(29,r'$\leqslant$',r'$\hand{\leqslant}$','The first lower dimension comparison is handwritten.'),
(30,r'Z \subset Y',r'Z \hand{\subset} Y','The inclusion sign is a pen stroke.'),
(31,r'$\leqslant$',r'$\hand{\leqslant}$','The final dimension comparison is handwritten.')
],[
(5,'Foliation','71 above;76 below','confirmed','Both handwritten numbers read directly.'),
(7,r'\unsure{K|k}','Overtyped K/k first character','retained_uncertain','Both uppercase and lowercase traces remain visible.'),
(21,'Cancelled draft phrases','Soit Noter qu’on; On voit on peut; supposer que X n’est contenu dans Alors','retained_uncertain','Each phrase compared directly; dense x impressions still obscure individual letters.'),
(24,'P superscript r','Retouched/underlined P and handwritten r','confirmed','Letter and raised pen r checked.'),
(29,'Right marginal mark','Small rising arrow/check-like stroke','retained_uncertain','The mark is visible, but its precise shape remains doubtful.'),
(15,'Underlined tout and et','Short underlines under both words','confirmed','Both underlines visibly present.'),
(10,'Comparison glyph layers','Inequalities have pen strokes','corrected_from_scan','Inspection contradicts the earlier NOTES suggestion of typed composite signs; handwriting marked.')
],'Both images fully read. The cancelled draft material, normalisation argument, all inequalities, inclusion and nonmembership signs, and final paragraph compared line by line.')
finish_reviewed(77,[
(10,r'X\supset Y\supset Z',r'X\hand{\supset} Y\hand{\supset} Z','Both inclusion signs are handwritten.'),
(12,r'\hand{\unsure{s}}',r'\hand{s}','The added final s of lisses is clear.'),
(13,r'p$>$0',r'p$\hand{>}$0','The characteristic comparison is handwritten.'),
(14,r'X$\rightarrow$P',r'X$\hand{\rightarrow}$P','The immersion arrow is handwritten.'),
(14,r'$\phi_n i$',r'$\hand{\phi}_n i$','Phi is a pen glyph.'),
(18,r'L_o \cap Z = \emptyset',r'L_o \hand{\cap} Z = \hand{\emptyset}','Intersection and empty-set signs are drawn by hand.'),
(20,r'L_o \cap X',r'L_o \hand{\cap} X','The intersection sign in b) is handwritten.'),
(22,r'L_o \cap Y',r'L_o \hand{\cap} Y','The intersection sign in c) is handwritten.'),
(28,r'U$\longrightarrow$V',r'U$\hand{\longrightarrow}$V','The arrow is handwritten.'),
(29,r'$L_o\cap Y$',r'$L_o\hand{\cap} Y$','The intersection symbol in the deleted sentence is handwritten.'),
(32,r"l'on ait  $C \cap Y = \emptyset$",r"\deleted{l'on ait  $C \hand{\cap} Y = \hand{\emptyset}$}",'The long pen cancellation visibly crosses this complete clause too; it must not remain live. The intersection and empty-set glyphs were hand-completed before cancellation.'),
(33,r'X$\cap$C',r'X$\hand{\cap}$C','The intersection sign is handwritten.'),
(40,r'Q$\longrightarrow$',r'Q$\hand{\longrightarrow}$','The immersion arrow is handwritten.')
],[
(5,'Foliation','72 above;77 below','confirmed','Both pencil/pen numbers read directly.'),
(11,'Interlinear dimension condition','de dimensions n,n-1 et less-or-equal n-2','confirmed','Typed words and handwritten inequality distinguished; attachment before X-Z verified.'),
(31,'New handwritten choice of C','ne rencontrant pas l’ensemble fini ... (L_o intersection Y) union {x}','confirmed','All readable letters and symbols checked; the scribbled deleted word remains illegible.'),
(32,'Extent of long deletion','Includes l’on ait C intersection Y equals empty','corrected_from_scan','The horizontal cancellation crosses these letters and signs, contrary to the prior note’s live reading.'),
(32,'Handwritten et x notin C','Insertion above cancelled clause','confirmed','The added words and symbols remain above the cancellation line; placement before cancelled même retained.'),
(36,'Overtyped C/E','C/E layered glyph','retained_uncertain','The two candidate shapes remain merged.'),
(24,'Overtyped ordinary words','parfait, codimension, projectif, Grass','confirmed','Their visible final letters compared; readable words retained without expansion.')
],'Both complete images read, with close attention to the long cancellation crossing the C-intersection-Y clause. Every intersection, inclusion, empty-set and arrow glyph checked; all new and cancelled writing layers retained.')
finish_reviewed(78,[
(7,r'\unsure{qui|qbi} sont aussi des sous-schémas fermés \inserted{disjoints} de $\underline{X}^{n-1}_Q$ ;','% NOTE: this complete typed interlinear addition is encoded at its insertion point below.','The long pen attachment places the top typed line after T_Q, not before inverses.'),
(9,r'$\underline{T}^{n-1}_Q$ , soient',r'$\underline{T}^{n-1}_Q$ , \inserted[typed]{\unsure{qui|qbi} sont aussi des sous-schémas fermés \inserted[typed]{disjoints} de $\underline{X}^{n-1}_Q$ ;} soient','The complete top line is a typed insertion at this point; disjoints is itself a typed insertion above that line.'),
(16,r'\unsure{le morphisme}','le morphisme','Both words remain legible beneath typewriter cancellation.'),
(18,r'X\cap L_o',r'X\hand{\cap} L_o','The intersection sign is handwritten.'),
(21,r'\unsure{pré}','pré','The three cancelled letters and accent are visible.'),
(22,r'\xout{\illegible{1}} posant',r'\xout{en} posant','The underlying en is legible.'),
(23,r'\xout{\illegible{1}} le morphisme',r'\xout{Et} le morphisme','The cancelled capital E and t are readable.'),
(23,r'\xout{\illegible{1}} U est aussi',r'\xout{un} U est aussi','The underlying un is readable through the x impressions.'),
(23,r'U\to V',r'U\hand{\to} V','The arrow is handwritten.'),
(24,r"\inserted{$X''=$}",r"\inserted[typed]{$X''=$}",'The X double-prime equals insertion has monospaced typewriter glyphs; its placement curve is handwritten.'),
(24,r'\underline{Y}^{n-1}_Q - \underline{T}^{n-1}_Q',r'\underline{Y}^{n-1}_Q - \underline{\unsure{T|Z}}^{n-1}_Q','The third numerator letter is overtyped and shows T/Z layers; mark the uncertainty.'),
(25,r"$X''\to$",r"$X''\hand{\to}$",'The comparison arrow is handwritten.'),
(26,r'_Q \to$',r'_Q \hand{\to}$','The arrow to X-T is handwritten.'),
(27,r'$L_o\cap X$',r'$\unsure{L|E}_o\hand{\cap} X$','The overtyped first letter has L/E traces and the intersection sign is handwritten.')
],[
(5,'Foliation','73 above;78 below','confirmed','Both pen/pencil folios read directly.'),
(7,'Top typed insertion','qui/qbi ... fermés disjoints ...','retained_uncertain','Exact insertion point established by the framing line; first word remains overtyped.'),
(10,'Replacement of construction','hypothèse essentiellement','retained_uncertain','The long pen phrase is compatible with the reading; cramped middle strokes remain doubtful.'),
(11,'Four zeta subscripts','Pen zeta with typed subscript o','confirmed','Each of the four occurrences inspected for writing layer and position.'),
(22,'Four short x-outs','en; unread group after Z prime; Et; un','corrected_from_scan','Three groups can be recovered; the group at the end of the U-definition line remains illegible.'),
(16,'Neighborhood ambient letter','V ... dans X','confirmed','The scan prints X here although the surrounding paragraph uses Q; retained without mathematical repair.')
],'Both complete image parts read; the top interlinear line was followed along its attachment to the correct location. Every cancellation, point subscript, comparison arrow, and overtyped letter checked.')
finish_reviewed(79,[
(9,r'L\unsure{,}',r'$L_{\hand{\eta}}$','The mark after L is the small handwritten point index, placed below the baseline, not a comma.'),
(9,r'\inserted{ainsi que le contenu dimensionnel de b) \unsure{c)} (pour toute immersion projective donnée)} cela résulte',r'\inserted[typed]{ainsi que le contenu dimensionnel de b) c)} cela résulte \inserted[typed]{(pour toute immersion projective donnée)}','The two additions are typed and have separate attachment points: the first after a), the parenthesis after cela résulte.'),
(10,r'\hand{[}aussitôt','aussitôt','The bracket at this location is the attachment of the typed parenthetical insertion, not a separate content bracket.'),
(18,r'X$\rightarrow$ P',r'X$\hand{\rightarrow}$ P','The arrow is handwritten.'),
(19,r'x $\in$P(k)',r'x $\hand{\in}$P(k)','The membership sign is handwritten.'),
(19,r"\inserted{tel que x n'appartienne à l'image d'aucune composante de X de dim $<$ m ,}",r"\inserted[typed]{tel que x n'appartienne à \unsure{l'|m'}image d'aucune composante de X de dim $\hand{<}$ m ,}",'The whole interlinear condition is typed, except the comparison sign; the first letter before image is overtyped and remains uncertain.'),
(20,r'd\unsure{e}','de','The second letter is readable as typed e.'),
(20,r'\xout{xxxxx}',r'\xout{sous}','The cancelled underlying word sous is legible.'),
(21,r'\xout{unexvariété}',r'\xout{une variété}','The x characters are cancellation, separating the underlying words rather than part of them.'),
(21,r'\inserted{x}',r'\inserted[typed]{x}','The inserted x has typewriter serifs.'),
(22,r'\xout{linéairexdonnéexdexcodimensionxm+1,}',r'\xout{linéaire donnée de codimension m+1,}','The underlying complete phrase is readable; embedded cancellation x marks are not letters in that phrase.'),
(22,r'\inserted{\unsure{\&}}',r'\inserted[typed]{\&}','The raised ampersand is clearly typewritten.'),
(24,r'$\phi_{n}f$',r'$\hand{\phi}_{n}f$','The phi is handwritten.'),
(24,r'$\geq$ 2',r'$\hand{\geq}$ 2','The comparison sign is handwritten.'),
(27,r'dim T $\geq$',r'dim T $\hand{\geq}$','The comparison is handwritten.'),
(27,r'\text{sing}}\rightarrow',r'\text{sing}}\hand{\rightarrow}','The arrow from the singular locus is handwritten.'),
(29,r'$\phi_{n}f$',r'$\hand{\phi}_{n}f$','The repeated phi is handwritten.'),
(29,r'n$\geq$2',r'n$\hand{\geq}$2','The repeated comparison is handwritten.'),
(30,r'\deleted{\unsure{on a}}',r'\deleted{on a}','The short cancelled words on a remain clearly visible.'),
(35,r'\unsure{75}','79','The pencil archive foliation has a closed 9 loop and descending stroke.')
],[
(5,'Upper folio','74','confirmed','Both digits read directly.'),
(9,'Insertion attachment paths','Two distinct typed additions near a), cela résulte and aussitôt','corrected_from_scan','The long bracket paths were traced to their endpoints; no words omitted.'),
(20,'Point symbols','Hooked eta at generic-point occurrences','confirmed','All four visible point symbols checked against the scan.'),
(19,'Long added condition','Typed tel que x ... dim less than m','confirmed','Complete condition read; doubtful initial letter in image explicitly retained.'),
(27,'codimension correction','co added before dim; n- deleted before2','confirmed','Both handwritten operations and resulting visible layers checked.'),
(14,'Left marginal rules','Short bracket at projection-conique discussion; long bracket beside remords','confirmed','Positions and extents checked.'),
(13,'Actual square brackets','Opening before Il pourrait, closing after à part','confirmed','These literal pen brackets remain; the insertion-attachment bracket before aussitôt was removed.')
],'Both full scan parts read and long insertion connectors traced. All dimensional conditions, point subscripts, and cancelled phrases checked; the remords references to §§8 and9 retained exactly.')
finish_reviewed(80,[
(8,r'codi\xout{me}nsion',r'\unsure{codimension|codimemsion}','The middle letters are overtyped without a distinct x cancellation; retain their ambiguity instead of deleting me in the corrected reading.'),
(11,r'\xout{xxxxxx}',r'\xout{\unsure{voire}}','Underlying letters support voire, with r obscured by cancellation.'),
(12,r"L'\cap H",r"L'\hand{\cap} H",'The intersection sign is handwritten.'),
(21,r'$\geqslant$',r'$\hand{\geqslant}$','The comparison sign is drawn by hand.'),
(22,r'x\in H_',r'x\hand{\in} H_','The membership sign is handwritten.'),
(24,r'\eta}\in T',r'\eta}\hand{\in} T','The membership sign after the generic point is handwritten.'),
(24,r'\xout{xxxxxxxxxxxxx}',r'\xout{\unsure{(ensemblistement)}}','The cancelled word is readable as ensemblistement, while surrounding parentheses remain partly obscured.'),
(25,r'\xout{xxxx}',r'\xout{tout}','The four cancelled letters spell tout.'),
(25,r'z\in X(\unsure{k})',r'z\hand{\in} X(k)','The membership sign is handwritten; the typewritten k is readable despite overtyping.'),
(25,r'\xout{xxx}',r'\xout{son}','The cancelled s-o-n is legible before l’espace.'),
(30,r'\xout{xxxxx}',r'\xout{entre}','The five underlying letters are readable.'),
(31,r'z\in X(k)',r'z\hand{\in} X(k)','The membership sign is handwritten.'),
(10,r'du \xout{xx}',r'du \xout{\unsure{le}}','The upper short cancelled group supports le with the second letter obscured.'),
(32,r'point,\xout{xx}',r'point,\xout{\unsure{le|de}}','The lower cancelled group allows le or de.')
],[
(5,'Foliation','75 above;80 below','confirmed','Both handwritten numbers checked.'),
(7,'Point index','Eta/xi-like hooked glyph','retained_uncertain','The supplied two candidates remain compatible with the handwritten shape.'),
(7,'Left margin rule','Long vertical bracket beside first paragraph','confirmed','Extent read from top through on en forme.'),
(12,'Cancelled letter before a section','x cancellation over l-like glyph','retained_uncertain','Retain supplied doubtful l without restoring expected wording.'),
(13,'Overtyped ordinary words','puis, linéaires, par, presque, ce qui est loisible','confirmed','Visible final words compared with the images.'),
(21,'Inserted Q and dual P','Q after l’hyperplan; V accent over P','confirmed','Both pen additions and their attachment checked.'),
(22,'Point symbols on H and generic point','Handwritten subscripts and interlinear eta','confirmed','Each occurrence compared; forms preserved.'),
(25,'Typed parenthetical insertion','(supposant k alg clos, ce qui est loisible)','confirmed','All words and placement after cancelled tout checked.'),
(27,'Singular-locus arrow','Pen arrow toward T','confirmed','Direction checked; existing TeX syntax defect left for mechanical cleanup.'),
(28,'Braces and quotations','Both pairs of braces around x; quotations around duale; closing parenthesis','confirmed','Every pen mark read directly.'),
(30,'Inserted T and orthogonal','Pen additions at duale and before à Q','confirmed','Words and placement curves checked.')
],'Both scan halves read completely. The induction paragraph and duality argument checked word by word and formula by formula; readable struck words recovered without restoring cancelled text to the live reading.')
finish_reviewed(81,[
(8,r'dim.$>0$',r'dim.$\hand{>}0$','The comparison sign is handwritten.'),
(12,r'\unsure{part}','part','The four letters p-a-r-t remain legible beneath the typewriter cancellation.'),
(13,r'\inserted{non singulière}',r'\inserted[typed]{non singulière}','The inserted words are monospaced typing above the line; the curve after P belongs to their placement line.'),
(14,r'\xout{xx}',r'\xout{\unsure{si}}','The short cancelled group shows an i and an s-like first character; preserve doubt.'),
(15,r'$\phi_n f$',r'$\hand{\phi}_n f$','Phi is a handwritten glyph.'),
(15,r'$n\geq 2$',r'$n\hand{\geq} 2$','The greater-or-equal sign is handwritten.'),
(18,r'que k \xout{xx}',r'que k \xout{\illegible{1}}','The two cancellation x characters obscure the underlying group; they are not content letters.'),
(21,r'\xout{xxx}',r'\xout{ici}','The underlying i-c-i is legible beneath the x cancellation.'),
(25,r'\xout{xx} \inserted{pour}',r'\xout{\unsure{en}} \inserted[typed]{pour}','The cancelled group resembles en; pour is a typed interlinear insertion with a handwritten placement curve.')
],[
(5,'Foliation','76 above;81 below','confirmed','Both numbers read directly.'),
(8,r'\unsure{$X$|$C$}','Superposed X/C-like typewriter letter','retained_uncertain','The final typing order is not separable from the image.'),
(11,'Cancelled example','(et pour faire un exemple où où ce fait se produit, en car 0 disons, on part d’une sous-variété T de','confirmed','Both complete cancelled lines read through the x impressions; repeated où retained.'),
(13,'Stroke after P','Continuation of insertion attachment','confirmed','It joins the placement curve for non singulière; no separate exponent read.'),
(24,'Overtyped ordinary words','montrent; une extension; polyélementaires; faible; subsiste','confirmed','Each word compared directly without normalizing its spelling.'),
(34,'Added remark label','c) with arrow to the gap after donnée','confirmed','The pen arrow points to the blank location recorded as an insertion.'),
(36,'Remark renumbering and addition','c overwritten d; donner in pen','confirmed','Both corrections and their placement checked.')
],'Both full images read, including the cancelled example, all hypotheses and finite-extension notation, and the marginal insertion of c). All text, margins, symbols and corrections compared.')
finish_reviewed(82,[
(7,r'f:X\to S',r'f:X\hand{\to} S','The structural arrow is handwritten.'),
(8,r'\unsure{xxxSxxixixquxxxX}',r'\unsure{sur S tel que X}','Readable underlying letters support this cancelled phrase; cancellation x marks are not content.'),
(9,r'\unsure{géomé}','géomé','The cancelled five-letter abbreviation is readable.'),
(10,r's\in S',r's\hand{\in} S','The membership sign is handwritten.'),
(10,r'x\in S',r'x\hand{\in} S','The second membership sign is handwritten.'),
(12,r'V\longrightarrow U',r'V\hand{\longrightarrow} U','The long arrow is handwritten.'),
(14,r'\unsure{aixxdesxfibresxde}','ait des fibres de','The underlying cancelled words are legible; x characters belong to the strike-out.'),
(14,r'\inserted{\unsure{satisfasse}}',r'\inserted{satisfasse}','The complete handwritten word is readable above the pen-deleted soit tel que.'),
(19,r'$\emptyset$ une partie',r'$\hand{\unsure{\phi|\emptyset}}$ une partie','The finite-part symbol is handwritten and resembles the author’s looped phi as well as a slashed circle; preserve alphabet uncertainty.'),
(20,r'$\emptyset$ soit contenu',r'$\hand{\unsure{\phi|\emptyset}}$ soit contenu','The repeated finite-part symbol has the same pen form.'),
(20,r'\xout{xxx}',r'\xout{\illegible{1}}','The underlying word cannot be separated from the three x impressions.'),
(21,r'$\emptyset$ admet',r'$\hand{\unsure{\phi|\emptyset}}$ admet','The repeated finite-part symbol is handwritten; retain the two glyph readings.'),
(22,r'$\emptyset$ formé',r'$\hand{\unsure{\phi|\emptyset}}$ formé','The symbol within the typed interlinear sentence is hand-completed.'),
(24,r'\unsure{t}%',r'\unsure{t|-}%','A t-like overstrike and end-of-line hyphen occupy the same place; both visible alternatives retained.'),
(25,r'$\emptyset\cup Y$',r'$\hand{\unsure{\phi|\emptyset}}\hand{\cup} Y$','The finite-part symbol and union sign are handwritten.'),
(25,r'$x_i\in\emptyset$\inserted{$^{\unsure{(\bar{k})|(k)}}$}',r'$x_i\hand{\in}\hand{\unsure{\phi|\emptyset}}$\inserted[typed]{$(\overset{\hand{-}}{k})$}','Membership and finite-part signs are handwritten. The interlinear (k) is typed, with a pen bar; its attachment puts it after the symbol, without making it an exponent.'),
(29,r'\xout{\unsure{lxsxlx}}\hand{\unsure{,}}',r'\xout{\unsure{les $L$}}\unsure{\hand{,}|$_i$}','The cancelled group supports les L. The small lower glyph may be a comma-like pen mark or the original subscript i; retain both readings.'),
(35,r'\xout{xxxxxx}',r'\xout{\unsure{ouverts}}','The underlying cancelled word resembles ouverts; x impressions still obscure individual letters.'),
(35,r'\inserted{\unsure{$/U$|$U$}}',r'\inserted{$U$}','The pen glyph is U; the slash-like lower stroke is its insertion attachment.')
],[
(5,'Foliation','77 above;82 below','confirmed','Both handwritten numbers read directly.'),
(9,'pré and ne rencontrant pas S prime et','Typed interlinear insertions','confirmed','Wording, typewriter layer, and attachment points checked.'),
(11,r'\unsure{un}','Overtyped un-like word','retained_uncertain','The second character has merged lower strokes; doubt retained.'),
(21,'fondamental; ouverts','Overtyped but readable words','confirmed','The final letters support the source readings; systême retained as printed.'),
(22,'Interlinear sentence','Evidemment on peut supposer finite-part formé de points fermés.','confirmed','Whole typed sentence read; fermés underline checked, placement after polyélémentaires verified.'),
(28,'générique and following génér-','Two overtyped words','retained_uncertain','The first remains readable; the second ending stays marked because of dense overprinting.'),
(28,'pour une telle C; alors','Handwritten insertion and pen deletion','confirmed','Both layers and their attachment read directly.'),
(29,'Codimensions n-1 and n','L_i first of codimension n-1; later L of codimension n','confirmed','Both printed indices checked and preserved without mathematical repair.'),
(18,'Remark labels','c), then e)','confirmed','Both letters are typed as transcribed.')
],'Both image parts fully read, including the general-base variant, finite-set refinement, all pen symbols and typewriter cancellations. The raised typed (k) addition was followed to its insertion point; no change inferred from mathematical expectation.')
finish_reviewed(83,[
(5,r'\unsure{78 bis}',r'\unsure{78 bis|77 bis}','The second digit is overwritten; its visible strokes allow both 8 and 7, while bis is clear.'),
(9,r'\xout{xxxxx}',r'\xout{comme}','The underlying c-o-m-m-e is legible beneath the typewriter x cancellation.'),
(11,r'\xout{xxxxxxxxxxxxxx}',r'\xout{\unsure{homotopiquement}}','The underlying letters support homotopiquement, but several middle and terminal strokes remain obscured by cancellation.')
],[
(9,'i not equal overwritten1','Pen not-equal and 1 over an unreadable typed character','retained_illegible','Both handwritten signs are clear; the underlying typed character cannot be recovered securely.'),
(10,'Donc insertion','Donc above the deleted comme d’ailleurs','confirmed','It replaces the crossed connective before U with the visible attachment at that location.'),
(10,'Semicolon correction','Pen mark over typed comma after libres','confirmed','Both layers retained as an overwrite.'),
(11,'un, quotation marks, comma, underlines','Typed un; pen opening and closing quotes and comma; underlines beneath classifiant and pour','confirmed','Every mark compared directly; nearby x impressions belong to the cancelled word.'),
(12,'Underlined C power n','Typed C with underline and raised n','confirmed','Alphabet, underline and exponent read directly.'),
(14,'Pi occurrences','All five pi signs hand-completed','confirmed','Each glyph and subscript checked.'),
(16,'Lower scan','Blank except pencil83','confirmed','Entire lower half and all margins inspected; no omitted continuation.')
],'Both complete images read, including the largely blank lower scan. All homotopy indices, pen overwrites and cancellations were inspected; the underlying character beneath 1 remains unreadable.')
finish_reviewed(84,[
(17,r'\longrightarrow P(G)',r'\hand{\longrightarrow} P(G)','The first displayed arrow is handwritten.'),
(18,"qui s 'appelera","qui s'appelera",'The scan has no extra word space between s and the apostrophe.'),
(21,r'\xout{Q(G)xx}',r'\xout{\unsure{Q(G)}}','The cancelled underlying expression supports Q(G); the terminal x impressions are cancellation marks.'),
(22,r'\inserted{pré}',r'\inserted[typed]{pré}','The interlinear pré is typewritten.'),
(22,r'\inserted{fermé}',r'\inserted[typed]{fermé}','The interlinear fermé is typewritten; its placement curve is pen.'),
(24,r'\xout{Gxx}',r'\xout{\unsure{Gr|G}}','The struck short group has a clear G and a possible r under the cancellation; retain both candidates.'),
(24,r'P(G) \longrightarrow',r'P(G) \hand{\longrightarrow}','The second displayed arrow is handwritten.'),
(31,r'\xout{Ixix}',r'\xout{\unsure{Ici,}}','The cancelled letters support Ici with a possible comma; keep uncertainty at the terminal mark.'),
(32,r'\xout{dexM}',r'\xout{de M}','The readable underlying words are de M; the intervening x is a cancellation impression.'),
(36,r'P - C \longrightarrow Q(C) \subset',r'P - C \hand{\longrightarrow} Q(C) \hand{\subset}','The final arrow and inclusion sign are handwritten.')
],[
(5,'Foliation','78 above;84 below','confirmed','Both numbers read directly.'),
(10,'Left marginal double rule','Two pencil strokes beside NB paragraph','confirmed','Extent and placement checked.'),
(11,'sorite; grassmannien','sorite readable; overtyped n in grassmannien','retained_uncertain','The first word is clear; the supplied doubt at the doubled n remains.'),
(14,'Codimension insertion','i.e. de codimension m+1 dans P','confirmed','Typed wording and attachment after S checked.'),
(17,'P in final P(G)','Overtyped capital P','confirmed','The readable outer letter remains P; no alternative substituted.'),
(24,'Grass index','r-m+1 with overtyped m','confirmed','All signs and indices compared directly.'),
(29,'Cancelled opening character','Parenthesis-like overstrike before Plus','retained_uncertain','The original bracket shape remains obscured.'),
(31,'au sens foncteurs insertion','Typed parenthesis attached after L’image','confirmed','Long placement curve traced to L’image, not to the preceding de P(G).'),
(32,'Dimension insertion','Typed de la dimension voulue after L','confirmed','Words and attachment checked.'),
(25,'Printed spelling and spacing','otebnu; d e; i/e.; la joined to projection','confirmed','These visible page forms retained without normalization.')
],'Both full scan parts read, including all three displays, every rank/index and the complete marginal and interlinear layers. The insertion paths were traced separately and the page spellings retained.')
finish_reviewed(85,[
(8,r'codi\unsure{mmm}sion',r'codi\unsure{amn|men|mmm}sion','The three overtyped middle letters allow these readings; none is settled from the ink.'),
(9,r'entend\xout{x}',r'entend\xout{\unsure{s}}','The cancelled final character resembles s beneath the x impression.'),
(13,r'X \longrightarrow P',r'X \hand{\longrightarrow} P','The morphism arrow is handwritten.'),
(15,r'\longrightarrow\ P - C \ \longrightarrow\ Q(C)',r'\hand{\longrightarrow}\ P - C \ \hand{\longrightarrow}\ \hand{Q}(C)','Both arrows and the Q of the last object are hand-completed; the parentheses and C are typed.'),
(16,r'\xout{x:}',r'\xout{\unsure{t|t:}}','The overstruck end of the line contains a t-like stem and a colon-like remnant; preserve both readings.'),
(17,r'\unsure{$p^{f}_{C}$|$p^{\Sigma}$}',r'\unsure{$p^{f}_{C}$|$p^{\Sigma}_{C}$}','The C subscript is visible beneath the first p independently of its overwritten exponent.'),
(17,r'\hand{(}On fera','On fera','The long curve beginning before On is the placement boundary of the preceding insertion, not a literal opening parenthesis.'),
(18,r'f^{-1}(C)=\emptyset',r'f^{-1}(C)=\hand{\emptyset}','The empty-set sign is hand-completed.'),
(19,r'\hand{\unsure{)}}',r'\hand{\unsure{/|)}}','The isolated faint stroke is straighter than a clear parenthesis; retain slash and parenthesis candidates.'),
(25,r'''\begin{tikzcd}
X & \underline{X}^{(m)}_{\xout{\unsure{Q}}Q(C)} = \underline{X}^{(m)}x_{\mathrm{Grass}^{m}}Q(C) \arrow[l, "q"'] \arrow[d, "p\xout{\unsure{z}}"'] \\
 & Q(C) \quad .
\end{tikzcd}''',r'''\begin{array}{ccc}
X & \overset{q}{\hand{\longleftarrow}} & \underline{X}^{(m)}_{\unsure{Q|G}(C)} = \underline{X}^{(m)}x_{\mathrm{Grass}^{m}}\hand{Q}(C) \\
 & & p\xout{\unsure{z}}\quad\hand{\downarrow} \\
 & & \hand{Q}(C) \quad .
\end{array}''','The diagram has a leftward q arrow and downward p arrow, both in pen. Q in the rightmost and lower Q(C) is handwritten. The first Q(C) index is a single overtyped Q/G-like glyph, not a separate cancelled Q followed by Q; the label after p remains uncertain.'),
(31,r'\xrightarrow{\ \sim\ }',r'\hand{\xrightarrow{\ \sim\ }}','Both the isomorphism arrow and its tilde are handwritten.'),
(33,r'f^{-1}(\xout{\unsure{Q}}C)',r'f^{-1}(\unsure{C|Q})','The argument is a single overtyped C/Q-like character; the scan does not contain two successive letters here.'),
(34,r'identificatio\xout{\unsure{n}}n','identification','The final word is legible as identification; no distinct cancelled n before a second n is visible.'),
(35,r'\ \subset\ ',r'\ \hand{\subset}\ ','The inclusion sign is handwritten.'),
(37,r'f:X\rightarrow P',r'f:X\hand{\rightarrow} P','The final morphism arrow is handwritten.')
],[
(5,'Foliation','79 above;85 below','confirmed','Both handwritten numbers read directly.'),
(9,'Right crop after qu','Only part of final e visible','retained_uncertain','The cropped-letter doubt and explanatory comment remain.'),
(17,'Handwritten notation addition','notée p with overwritten exponent and C subscript; ou p_C^X ou simplement p_C','retained_uncertain','All words and the two clear notations read; the first exponent remains overwritten.'),
(17,'Long line over On fera attention','Insertion connector','corrected_from_scan','Its continuation encloses the added notation and lands before On; it does not cancel the typed sentence.'),
(26,'Diagram indices and label','Q/G in first index; cancelled z-like character beside p','retained_uncertain','Each enlarged directly; original letterforms cannot be completely separated.'),
(34,r'simp\unsure{be|le}','Overtyped b/l-like glyph','retained_uncertain','The competing stem and bowl remain visible.'),
(36,'ou p_C addition','Handwritten phrase before comma after p_C^X','confirmed','Placement curve and all letters checked.'),
(37,'Comma after X','Pen comma','confirmed','The added mark is visible below baseline.')
],'Both complete scan parts read, with enlarged inspection of the long insertion, the full diagram, and overtyped lower words. Arrow directions, primes, indices and all margins checked; uncertainty retained where the ink remains merged.')
finish_reviewed(86,[
(7,r'p$_{\unsure{\xout{C}}}$',r'p$_{\deleted{\unsure{C}}}$','The small index is crossed by irregular pen hatching; C remains only a doubtful reading.'),
(13,r'p\unsure{ro}jection',r'p\unsure{ro|oo}jection','The overwritten middle pair allows ro and oo; retain the visible alternatives.'),
(15,r'k$\rightarrow$k',r'k$\hand{\rightarrow}$k','The extension arrow is handwritten.'),
(15,r'\inserted{alors}',r'\inserted[typed]{alors}','The interlinear word alors is typed; its attachment line is pen.'),
(15,r'X$_{k(\hand{\eta})}$',r'X$_{k(\hand{\unsure{\eta|y}})}$','The repeated generic-point glyph has the same eta/y ambiguity as the first occurrence.'),
(16,r'\unsure{ar}guments',r'\unsure{ar|aa}guments','The first two overtyped letters also permit aa; the word is not silently normalized.'),
(20,r'infinité\hand{)} \inserted{de}',r'infinité) \inserted[typed]{de}','The enlarged image shows a typed closing parenthesis and typed de; the thin adjacent line is their insertion connector.'),
(20,r'\uline{définie\xout{s} sur}',r'\uline{définie\xout{s}} \uline{sur}','The two words have separate underlines.'),
(24,r'\margin{|} eau','eau','This occurrence repeats the single continuous marginal rule already encoded at its first line.'),
(25,r'\margin{|} utilisées','utilisées','This occurrence repeats the same continuous marginal rule.'),
(26,r'\unsure{13.3}','13.3','All digits and the decimal point remain legible through the cancellation.'),
(28,r'F^{(m)}_{Q(C)}',r'F^{(m)}_{\hand{Q}(C)}','The Q index is hand-completed; F, parentheses and C are typed.'),
(28,r'\underline{\underline{X}}^{(m)}_{Q(C)}',r'\underline{X}^{(m)}_{\hand{Q}(C)}','Enlargement shows one heavy underline beneath X, not two distinct lines; Q is a pen glyph.'),
(29,r'\widetilde{X(C)}',r'\overset{\hand{\sim}}{X}(C)','The pen tilde is over X alone, leaving (C) outside its span.'),
(29,r'\widetilde{F(C)}',r'\overset{\hand{\sim}}{F}(\unsure{C|O})','The pen tilde is over F alone. The parenthesized letter is overtyped and allows C/O.'),
(30,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The standalone X tilde is handwritten.'),
(30,r'\widetilde{F}',r'\overset{\hand{\sim}}{F}','The standalone F tilde is handwritten.')
],[
(5,'Top folio','Clipped80-like number','retained_uncertain','Only lower portions of the digits are available.'),
(14,'Grassmannian argument','Overtyped E/P glyph','retained_uncertain','Both candidates remain visible.'),
(15,'Ambient X in generic-centre sentence','X subscript k(point)','confirmed','The scan prints X, retained despite the surrounding projective-space notation.'),
(25,'Cancelled reference','(dém. de /13.3','retained_uncertain','The wording before the number remains crossed and partly obscured; the number itself was recovered.'),
(23,'Marginal rule','One continuous pencil line over three text lines','corrected_from_scan','Repeated encodings reduced to its first attachment.'),
(30,'n’en apostrophe','Overtyped apostrophe-like mark','retained_uncertain','The tiny merged strokes do not settle its exact form.'),
(31,'Replacement of précédent','Small pen ici-like word','retained_uncertain','The middle pen strokes remain cramped; original doubt retained.'),
(19,'Page spellings','standart; enfih; sensée; d es','confirmed','These are visible in the scan and remain unchanged.'),
(36,'Lower folio','86','confirmed','Pencil digits read directly.')
],'Both complete images read, with enlarged inspection of the parenthesis/insertion and X underline. Every reference, exponent, generic-point glyph, tilde and cancellation checked; one continuous marginal rule encoded once.')
changes87=[
(8,r'}$\hand{)} ,',r'}$ ,','The extra mark is the already-transcribed closing parenthesis of k(point), followed by the typed comma; no second parenthesis is present.'),
(12,r'\xout{\illegible{1}}',r'\xout{\unsure{que|(cf}}','The obscured short group allows que or an opening (cf; these ink-based candidates replace complete illegibility.'),
(14,r'pré\xout{\unsure{s}}cise',r'pré\unsure{c|s}ise','The scan has one overtyped c/s position, without a separate cancelled letter before it.'),
(15,r'la section $\phi_',r'la section $\hand{\phi}_','Phi is handwritten.'),
(16,r'$_{\hand{y}}$ ;',r'$_{\hand{y}}$ \over{;}{\unsure{;|,}}','The semicolon is touched by a pen hook; whether it remains a semicolon or becomes a comma cannot be settled.'),
(17,r'(\hand{C_y})\to X',r'(\hand{C_y})\hand{\to} X','The short comparison arrow is handwritten.'),
(18,r'X\times_P C',r'Xx_P C','The product sign is a typed lowercase x, retained as the visible alphabet.'),
(18,r'\xout{\illegible{2}}',r'\xout{\unsure{D’autre part,}}','The underlying words D’autre part can be read; the terminal punctuation remains obscured.'),
(19,r') = \emptyset',r') = \hand{\emptyset}','The empty-set sign is handwritten.'),
(20,r'\xrightarrow{\sim}',r'\hand{\xrightarrow{\sim}}','The isomorphism arrow and tilde are handwritten.'),
(20,r'\hand{\unsure{)}}projection',r'\over{p}{\unsure{p}}rojection','The pen mark retouches the initial p of projection; it is not a separate parenthesis.'),
(22,r'\longrightarrow Q(C_',r'\hand{\unsure{\longrightarrow|\relbar}} \hand{Q}(C_','The connector is handwritten, with an indistinct arrowhead; Q is hand-completed.'),
(27,r'f:X$\to$P',r'f:X$\hand{\to}$P','The arrow in the quasi-finite example is handwritten.'),
(29,r'\longrightarrow \over{Q}{Q}',r'\hand{\longrightarrow} \over{Q}{Q}','The arrow to the retouched Q is handwritten.'),
(30,r'$\leqslant$ m',r'$\hand{\leqslant}$ m','The b) comparison sign is handwritten.'),
(30,r'et si les fibres non vides des $X_i$ sur P sont \unsure{tts} de dimen d, alors',r'et si les fibres non vides des $X_i$ sur P sont \unsure{ttes|tts} de dim d, alors;','The enlarged line reads the abbreviation dim, without en; its final mark is semicolon-like. The abbreviation for toutes remains ttes/tts.'),
(30,r'les fibres de $p_C$ \inserted{non vides}',r'les fibres \inserted{non vides} de $p_C$','The circled non vides attaches after fibres, before de p_C.'),
(30,r'\inserted{$\colon X_{k(y)}\to Q(C_y)$}',r'\inserted{$\colon X_{k(\unsure{\eta|y})}\to Q(C_{\unsure{\eta|y}})$}','The marginal formula has the same looped point glyph as the running formulas; retain its eta/y ambiguity.'),
(31,r'\unsure{k$(y)$}',r'\unsure{k$(\eta)$|k$(y)$}','The struck field argument carries a looped eta/y-like point glyph.'),
(31,r'resp. quasi-fini}}].',r'resp. quasi-fini}}\hand{]}.','The closing square bracket is handwritten.'),
(32,r'\margin{\unsure{resp. quasi-fini}}','% NOTE: the circled right-margin resp. quasi-fini is already encoded in the preceding insertion.','This is the same circled phrase already placed after the final inserted fini; a third occurrence would duplicate the scan.'),
(36,r'\xout{xxxxxxxxxxxx} ','','These x impressions duplicate the cancellation already represented over correspondant à un; there is no extra underlying twelve-character group.')
]
import re
src87=source_path('ega25_25_087').read_text()
for m in re.finditer(r'\\hand\{(?:\$)?y(?:\$)?\}',src87):
 line=src87.count('\n',0,m.start())+1
 after=r'\hand{\unsure{\zeta|y}}' if line==36 else r'\hand{\unsure{\eta|y}}'
 changes87.append((line,m[0],after,'The pen point glyph is looped and allows the indicated Greek/Latin readings; its alphabet is not silently fixed.'))
for m in re.finditer(r'\\widetilde\{X\}',src87):
 changes87.append((src87.count('\n',0,m.start())+1,m[0],r'\overset{\hand{\sim}}{X}','The tilde above X is handwritten.'))
for m in re.finditer(r'\\hand\{C_y\}',src87):
 changes87.append((src87.count('\n',0,m.start())+1,m[0],r'\hand{C_{\unsure{\eta|y}}}','The hand-completed C carries the same ambiguous point subscript.'))
finish_reviewed(87,changes87,[
(5,'Foliation','81 above;87 below','confirmed','Both numbers read directly.'),
(7,'Three comparison signs','Greater-or-equal; less-or-equal; less-than','confirmed','All three are pen glyphs with the source directions.'),
(15,'Module loc libre insertion','Typed above cancelled fibré vectoriel','confirmed','Whole phrase and the two writing layers compared.'),
(16,'Zero-scheme C','Typed C retraced in pen','confirmed','The letter remains C; only its writing layer is corrected.'),
(24,'Proposition opening','Cancelled a) Si dim X; merged e/ou before plus','retained_uncertain','Cancelled phrase legible; the very small overwrite before plus remains uncertain.'),
(27,'avec d=0','Moved pen insertion, with its earlier right-margin occurrence crossed out','confirmed','Both instances read and retained in their respective states.'),
(30,'Revised b) hypothesis','et si les fibres non vides des X_i sur P sont ttes/tts de dim d, alors;','corrected_from_scan','Entire long pen line read at enlargement and followed to the beginning of les fibres.'),
(31,'Revised conclusion','Two resp. quasi-fini additions; deletion includes si X est propre sur k(point) et; replacement f:X to P est fini','retained_uncertain','The cancellation visibly crosses si; it is not restored from syntax. The two abbreviated pen phrases remain marked, and their duplicate third encoding was removed.'),
(26,'Right edge','Terminal dimension d and quasi-fini reach the crop','confirmed','All visible letters checked; no unseen continuation supplied.'),
(34,'Proof deletion','se ramène ... composantes irréd., /au cas ... irréductible','confirmed','Both complete struck lines read; On and the following Dans remain live.')
],'Both complete scan parts read; the dense b) revision, all marginal formulas, cancellation extents and attachment curves were enlarged and traced. Every formula, index and arrow compared; no grammatical or mathematical reconstruction supplied.')
changes88=[
(11,r'\subset L_',r'\hand{\subset} L_','The inclusion sign is handwritten.'),
(13,r')$\to$k',r')$\hand{\to}$k','The field-extension arrow is handwritten.'),
(15,r'\xout{dimxXx$_{P}$C}',r'\xout{dim $Xx_PC$}','The cancellation x marks are separated from the readable product notation beneath them.'),
(15,r'\xout{(avecxlaxconventionxque}',r'\xout{(avec la convention que}','The complete cancelled wording is legible; the x impressions are not letters in the phrase.'),
(18,r'\xout{alorsxxxlimagexde}',r"\xout{alors l'image de}",'The cancelled underlying words and apostrophe are readable.'),
(19,r'\xout{f(X)xxf$_{k(\ )}$xxxx}',r'\xout{\unsure{$f(X)\ f_{k(\ )}$}}','The repeated x impressions obscure the remainder of the attempted expression; retain the visible formula as doubtful.'),
(19,r') \cap L_',r') \hand{\cap} L_','The intersection sign is handwritten.'),
(21,r'\neq \emptyset',r'\hand{\neq} \hand{\emptyset}','Both non-equality and empty-set glyphs are handwritten.'),
(23,r'f:X$\to$P',r'f:X$\hand{\to}$P','The structural arrow is handwritten.'),
(23,r'\inserted{(resp quasi-fini)}',r'\inserted[typed]{(resp quasi-fini)}','The parenthetical addition is typed above the line, with a pen attachment.'),
(24,r'\longrightarrow Q(C_',r'\hand{\unsure{\longrightarrow|\relbar}} Q(C_','The handwritten connector has no separately secure arrowhead in this image; retain arrow and bar candidates.'),
(24,r'surjectif\hand{(}resp.',r'surjectif(resp.','The opening parenthesis is typed on the baseline.'),
(27,r'\inserted{quasi-}',r'\inserted[typed]{quasi-}','The prefix quasi- is typed above fini; its connector is pen.'),
(28,r'\xout{enfinxdoncxsurjectif}',r'\xout{enfin donc surjectif}','All underlying words are legible beneath typewriter cancellation.'),
(29,r'\xout{doncxfex}',r'\xout{\unsure{donc fe}}','The cancelled group reads donc followed by fe-like letters; the unfinished ending remains uncertain.'),
(31,r'\longrightarrow Q(C_',r'\hand{\unsure{\longrightarrow|\relbar}} Q(C_','This second connector likewise has a faint or absent arrowhead; both readings remain marked.'),
(34,r'\unsure{\varphi^{-1}_{\xi}}',r'\varphi^{(m)}_{\xi}','The enlarged pen superscript is (m), not -1; the phi and point subscript are legible.'),
(34,r'\unsure{$F_{\xi}$}',r'\unsure{$F_{k(\xi)}$|$F_{\xi}$}','The small subscript includes a k-like stem and closing parenthesis; add the better-supported longer reading while retaining uncertainty.'),
(34,r'Q(C_{y})',r'Q(C_{\unsure{\eta|y}})','The point glyph in the inserted formula shares the running eta/y ambiguity.'),
(38,r'\hand{(}et à fortiori plat\hand{)}',r'(et à fortiori plat)','These parentheses are typed on the baseline; their shapes and weight match the surrounding typing.'),
(40,r'\xout{xxxx}',r"\xout{\unsure{l'hy}}",'The underlying fragment shows l, apostrophe-like mark, h and y; the cancellation prevents a fully certain reading.')
]
import re
src88=source_path('ega25_25_088').read_text()
for m in re.finditer(r'\\times',src88):
 changes88.append((src88.count('\n',0,m.start())+1,m[0],'x','The product marker is a typed lowercase x, not a separately drawn multiplication glyph.'))
for m in re.finditer(r'\\over\{>\}\{\$\\geqslant\$\}',src88):
 changes88.append((src88.count('\n',0,m.start())+1,m[0],r'\hand{$\geqslant$}','The angle and the added lower stroke both have pen contours; no separate typed greater-than glyph is visible.'))
for m in re.finditer(r'\\hand\{y\}',src88):
 changes88.append((src88.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\eta|y}}','The looped handwritten generic-point glyph allows eta or y; retain the alphabet ambiguity noted for this page.'))
changes88.append((27,r'\hand{k(y)}',r'\hand{k(\unsure{\eta|y})}','The wholly handwritten subscript contains the same ambiguous point glyph.'))
for letter in ['X','F']:
 for m in re.finditer(r'\\widetilde\{'+letter+r'\}',src88):
  changes88.append((src88.count('\n',0,m.start())+1,m[0],r'\overset{\hand{\sim}}{'+letter+'}','The tilde is handwritten.'))
finish_reviewed(88,changes88,[
(5,'Foliation','82 above;88 below','confirmed','Both numbers read directly.'),
(7,'Upper right crop','First two lines meet cut edge','confirmed','The visible endings were read and the source crop comment retained.'),
(18,'d+1 writing layers','Typed d followed by pen +1','confirmed','The distinction is visible in the enlarged upper image.'),
(19,'Overwritten lower bound','Pen1 over typed0-like glyph','confirmed','The hand stroke and underlying loop compared; both layers retained.'),
(34,'Full handwritten insertion','qui donne un résultat plus fort ... les phi^(m)_xi ... F_k(xi)-réguliers','corrected_from_scan','Every word of both handwritten lines was read at enlargement; the superscript correction is scan-supported and the small F subscript remains doubtful.'),
(34,'Cross-reference','page21, avant5.6; à inclure dans14.3','confirmed','All printed and inserted reference numbers read directly.'),
(30,'Overtyped ordinary words','dominant; Cohen-Macaulay; irréductible; morphisme','confirmed','Each final word remains legible; no new spelling supplied.'),
(15,'Missing generic-point index in dim display','dim underlined X^(m+1) without index','confirmed','No generic-point index is visible in that displayed occurrence; retained as printed.')
],'Both scan parts read completely; all dimension arguments, cancellation fragments and the two-line handwritten addition were inspected at enlargement. The phi exponent is corrected to (m); remaining F-subscript and point-alphabet doubts stay explicit.')
changes89=[
(5,'% NOTE: the top right corner is cut off at the edge of the scan; only the lower part of a number is visible there (probably the page number)','% NOTE: the top right corner cuts the upper parts of the folio digits.\n'+r'\mspage{\hand{\unsure{83}}}','The two surviving lower curves support83, but the upper halves are cut off; retain doubt.'),
(13,r'f:X\longrightarrow P',r'f:X\hand{\longrightarrow} P','The upper structural arrow is handwritten.'),
(14,r'''\inserted[typed]{étudiées au nº12.}
fié,''',r'''fié, \inserted[typed]{étudiées au nº12.}''','The typed interlinear addition belongs after fié,; the source had placed it inside the hyphenated word.'),
(17,r'\inserted[typed]{sur $X(C_{\hand{y}})$}',r'\inserted[typed]{sur $\overset{\hand{\sim}}{X}(C_{\hand{y}})$}','A small pen tilde is visible above X in the typed addition.'),
(18,r'''que si \uline{les dimensions des composantes} de X sont $\geq$ m, alors\hand{)}
(ou montrerait, si nous ne la faisons pas)''',r'''% NOTE: the typed interlinear dimension condition is placed at the endpoint of its pen connector below.
(ou montrerait, si nous ne la faisons pas) \inserted[typed]{que si les dimensions des composantes de X sont $\hand{\geq}$ m, alors}''','The entire dimension-condition line is typed between the ordinary baselines; its enclosing connector lands after the parenthesis. The long lower stroke and final curve are attachment marks, not a literal underline or closing parenthesis.'),
(19,r"Z'\subset Z",r"Z'\hand{\subset} Z",'The inclusion sign is handwritten.'),
(20,r'$\geq 2$',r'$\hand{\geq} 2$','The codimension comparison is handwritten.'),
(23,r'\unsure{ayant}','ayant','The cancelled underlying word ayant is legible.'),
(25,r'$\phi_n f$',r'$\hand{\phi}_n f$','Phi is handwritten.'),
(25,r'$(n\geq 2)$',r'$(n\hand{\geq} 2)$','The comparison sign is handwritten.'),
(27,r'dim X $\leqslant$ m',r'dim X $\hand{\leqslant}$ m','The upper less-or-equal sign is handwritten.'),
(31,r'f:X\longrightarrow P',r'f:X\hand{\longrightarrow} P','The proposition arrow is handwritten.'),
(31,r'dim X $\leqslant$ m',r'dim X $\hand{\leqslant}$ m','The proposition comparison sign is handwritten.'),
(33,r'\margin{\unsure{X?}}',r'\margin{\unsure{*?|X?}}','The marginal mark has crossed diagonal and transverse strokes; a star and X remain possible before the faint question mark.'),
(34,r'dimension $\leqslant$ m-1',r'dimension $\hand{\leqslant}$ m-1','The dimension comparison is handwritten.'),
(35,r')) \cap T_',r')) \hand{\cap} T_','The intersection sign is handwritten.'),
(35,r'= \emptyset',r'= \hand{\emptyset}','The empty-set sign is handwritten.'),
(37,r'\unsure{même|aussi}',r'\unsure{\ensuremath{=}|même|aussi}','The compact pen mark has two nearly horizontal strokes and does not securely spell either full word; add the literal equals-like candidate.'),
(37,r'$p_{C_y}^{-1}\,p_{C_y}(T_{k(y)})$',r'$p_{C_{\unsure{\eta|y}}}^{-1}\,p_{C_{\unsure{\eta|y}}}(T_{k(\unsure{\eta|y})})$','The three point glyphs in the handwritten continuation have the same eta/y ambiguity as the running text.')
]
import re
src89=source_path('ega25_25_089').read_text()
for m in re.finditer(r'\\hand\{y\}',src89): changes89.append((src89.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\eta|y}}','The looped handwritten generic-point glyph permits eta and y.'))
for m in re.finditer(r'\\hand\{\(y\)\}',src89): changes89.append((src89.count('\n',0,m.start())+1,m[0],r'\hand{(\unsure{\eta|y})}','The parenthesized pen point glyph permits eta and y.'))
for m in re.finditer(r'\\hand\{\\zeta\}',src89): changes89.append((src89.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\xi|\zeta}}','The vertically curled pen point glyph permits xi or zeta; its alphabet remains explicitly uncertain.'))
finish_reviewed(89,changes89,[
(16,'Q(C ) without point index','Blank after C','confirmed','The scan has no visible generic-point subscript in this occurrence.'),
(17,'Two placement curves','sur tildeX(C) and the dimension-condition line','corrected_from_scan','Each curve traced independently to its endpoint; neither is treated as a cancellation.'),
(17,'Overtyped ordinary words','Et; esquissée; codimension; fibres; notamment; est défini','confirmed','Final words compared directly, with no new reading supplied from context.'),
(23,'Second cancelled word after nécessairement','Dense six-character cancellation','retained_illegible','The visible fragments do not settle a complete word; the illegibility mark remains.'),
(29,'doit and est','Handwritten additions before être and laissée','confirmed','Both words and attachment strokes read directly.'),
(33,'Revised item a)','Si f est une immersion; radiciel i.e. géométriquement injectif','confirmed','All handwritten words and the full deletion of un monomorphisme read.'),
(37,'Final continuation','et compact doubtful mark en les pts de p inverse p(T)','retained_uncertain','Both pen lines read at enlargement; the compact mark remains unresolved rather than expanded.'),
(38,'Bottom folio','83','confirmed','The pencil number is83 even though the archive site is89; retained as written.')
],'Both full scan parts read, including the complete last handwritten continuation. The interlinear condition was moved only after its attachment path was traced. Every inequality, point index, deletion and margin was inspected; unresolved compact writing remains marked.')
changes90=[
(5,r'\unsure{87}',r'\unsure{84|87}','The clipped last digit allows a vertical-stem4 as well as7; the upper part is missing.'),
(7,r'dim X $\leqslant$ m-1',r'dim X $\hand{\leqslant}$ m-1','The comparison sign is handwritten.'),
(8,r'\xout{\illegible{1}}',r'\xout{\unsure{et}}','The short cancelled group supports e-t, with part of the first letter obscured.'),
(8,r'f:X $\to$ P',r'f:X $\hand{\to}$ P','The immersion arrow is handwritten.'),
(8,r'Y\hand{$_y$}',r'Y\hand{$_{\unsure{\eta|y}}$}','The handwritten generic-point subscript allows eta or y.'),
(10,r"$p'_{C_y} : X_{k(y)} \to Y_y$",r"$p'_{C_{\hand{\unsure{\eta|y}}}} : X_{k(\hand{\unsure{\eta|y}})} \hand{\to} Y_{\hand{\unsure{\eta|y}}}$",'The three point subscripts and the arrow are handwritten; the generic glyph remains eta/y.'),
(11,r"p'^{-1}_{C_y}p'_{C_y}(x)",r"p'^{-1}_{C_y}(p'_{C_y}(x))",'The handwritten formula contains a visible outer pair of parentheses around p prime of x; restore that pair.'),
(15,r'\uline{et séparable}',r'\inserted[typed]{et séparable}','The phrase is a typed interlinear addition with an enclosing placement curve; the lower stroke is not a separate underline.'),
(23,r'\xout{PxxxQxx}',r'\xout{\unsure{P Q}}','The underlying P and Q are visible, while intervening characters are obscured by x cancellation.'),
(24,r'\inserted{dans X}',r'\inserted{\unsure{donc|dans} X}','The pen word has an open final c-like curve; donc is better supported, but dans remains possible.'),
(24,r'\xout{\unsure{sur}}',r'\xout{sur}','The underlying three cancelled letters are legible.'),
(28,r'\unsure{, xx que}',r'\unsure{), ou que}','The cancelled group contains a closing parenthesis and ou que-like letters; x impressions are cancellation marks.'),
(32,r'\xout{XxxxxQx}',r'\xout{\unsure{X Q}}','X and Q remain readable in the cancelled expression; intervening marks do not settle the connector.'),
(32,r'X $\to$ Q $\simeq$',r'X $\hand{\to}$ Q $\hand{\simeq}$','The arrow and isomorphism sign are handwritten.'),
(34,r'$\xrightarrow{\sim}$',r'$\hand{\xrightarrow{\sim}}$','The final isomorphism arrow is handwritten.'),
(35,r'\xout{x pourxxxvariablexdans}',r'\xout{\unsure{, pour variable dans}}','The readable cancelled words are pour variable dans; the leading punctuation is obscured.'),
(37,r'ramification de p$_{C_{\hand{y}}}$ pour \hand{y} variable',r'ramification de p$_{C_{\hand{\xi}}}$ pour \hand{\xi} variable','These two lower point glyphs have the vertically curled xi form, unlike the looped generic-centre glyph in the preceding line.')
]
import re
src90=source_path('ega25_25_090').read_text()
for m in re.finditer(r'\\hand\{y\}',src90):
 if src90.count('\n',0,m.start())+1!=37: changes90.append((src90.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\eta|y}}','The looped generic-point glyph allows eta or y.'))
# Only remaining bare point symbols occur inside the fully handwritten continuation.
changes90.extend([
(10,r'de $X_{k(y)}$ au dessus',r'de $X_{k(\unsure{\eta|y})}$ au dessus','The point inside the handwritten field argument allows eta/y.'),
(11,r"$p'_{C_y}$",r"$p'_{C_{\unsure{\eta|y}}}$",'The handwritten morphism index has the same ambiguous point glyph.'),
(11,r"p'^{-1}_{C_y}(p'_{C_y}(x))",r"p'^{-1}_{C_{\unsure{\eta|y}}}(p'_{C_{\unsure{\eta|y}}}(x))",'Both point indices in the handwritten inverse-image expression allow eta/y.')
])
finish_reviewed(90,changes90,[
(11,'Barred compact symbol after et','Barred m-like glyph, also compatible with nr','retained_uncertain','The pen bar is clear; the joined lower strokes do not settle the abbreviation.'),
(17,'Cancelled handwritten dans','Short crossed word before sur','retained_uncertain','The supplied candidate remains compatible with the underlying strokes.'),
(14,'Irreducibility and separability additions','Typed irréductible repeated above cancellation; et séparable added before de dimension','confirmed','Both insertion layers and their positions checked.'),
(20,'que and nécessairement','Typed additions with pen connectors','confirmed','Every word and endpoint inspected.'),
(28,'Overtyped words','monomorphisme; dimensions','confirmed','Final word readings are visible beneath the overtyping.'),
(33,'Reference','Chap VIII !','confirmed','Roman numeral and exclamation mark read directly.'),
(37,'Last two additions','sur k; un ouvert de','confirmed','Both handwritten phrases read, along with the barred-k point sets.'),
(38,'Underlined conclusion and deletion','admet aucun and point fixe underlined; point fermé de X comme deleted','confirmed','The whole final line and its layered cancellation checked.'),
(40,'Lower folio','90','confirmed','Pencil digits read directly.')
],'Both complete scan parts read, including the full added proposition ending, all corollary revisions and the final ramification discussion. Enlarged parentheses and cancellation checked; shorthand and clipped folio uncertainties remain explicit.')
changes91=[
(7,r'\unsure{actuel}','actuel','The six cancelled letters are legible beneath the x impressions.'),
(11,r'''\diagram{\begin{tikzcd}
X \arrow[d] & \widetilde{X}(C) \arrow[l] \arrow[d] \\
S & Q(C) \arrow[l]
\end{tikzcd}}''',r'''\diagram{\begin{array}{ccc}
X & \hand{\longleftarrow} & \overset{\hand{\sim}}{X}(C) \\
\hand{\downarrow} & & \hand{\downarrow} \\
S & \hand{\longleftarrow} & \hand{Q}(C)
\end{array}}''','All four arrows and the tilde are drawn by hand; the Q is hand-completed. Arrow directions and object positions are preserved.'),
(15,r'C \in \mathrm{Grass}',r'C \hand{\in} \mathrm{Grass}','The membership sign is handwritten.'),
(15,r'\inserted{plus généralement}',r'\inserted[typed]{plus généralement}','The interlinear words are typewritten, with a pen placement curve.'),
(16,r'T \to S',r'T \hand{\to} S','The base-change arrow is handwritten.'),
(17,r'''\diagram{\begin{tikzcd}
X_T \arrow[d] & \widetilde{X}(C_{\hand{$\zeta$}}) = \widetilde{X_T}(C_{\hand{$\zeta$}}) \arrow[l] \arrow[d] \\
T & Q(C_{\hand{$\zeta$}}) \arrow[l]
\end{tikzcd}}''',r'''\diagram{\begin{array}{ccc}
X_T & \hand{\longleftarrow} & \overset{\hand{\sim}}{X}(C_{\hand{\unsure{\xi|\zeta}}}) = \overset{\hand{\sim}}{X}_T(C_{\hand{\unsure{\xi|\zeta}}}) \\
\hand{\downarrow} & & \hand{\downarrow} \\
T & \hand{\longleftarrow} & \hand{Q}(C_{\hand{\unsure{\xi|\zeta}}})
\end{array}}''','The four arrows, two tildes, Q and point subscripts are handwritten. The second tilde lies over X alone; the curled point glyph permits xi/zeta.'),
(21,r'T \longrightarrow \mathrm{Grass}',r'T \hand{\longrightarrow} \mathrm{Grass}','The universal-base arrow is handwritten.'),
(23,r'''\diagram{\begin{tikzcd}
X_{\underline{T}} \arrow[d] & \widetilde{X}(\underline{C}) \arrow[l] \arrow[d] \\
\underline{T} & Q(\underline{C}) \arrow[l]
\end{tikzcd}}''',r'''\diagram{\begin{array}{ccc}
X_{\underline{T}} & \hand{\longleftarrow} & \overset{\hand{\sim}}{X}(\underline{C}) \\
\hand{\downarrow} & & \hand{\downarrow} \\
\underline{T} & \hand{\longleftarrow} & \hand{Q}(\underline{C})
\end{array}}''','All arrows, the tilde and Q are handwritten; the typed underlines on T and C are retained.'),
(28,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The next displayed X tilde is handwritten.'),
(28,r'\longrightarrow Q(C_',r'\hand{\longrightarrow} \hand{Q}(C_','The comparison arrow and Q are handwritten.'),
(29,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The final X tilde is handwritten.'),
(29,r'\longrightarrow Q(\underline{C})',r'\hand{\longrightarrow} \hand{Q}(\underline{C})','The final comparison arrow and Q are handwritten.'),
(30,r'\xout{xxxx}',r'\xout{\illegible{1}}','The four x impressions do not yield a secure underlying word; preserve an illegibility mark.'),
(32,r'$Q$ doit',r'$\hand{Q}$ doit','The standalone Q naming the functor is handwritten.'),
(32,r'\inserted{de foncteurs}',r'\inserted[typed]{de foncteurs}','The words de foncteurs are typed above the line; the enclosing connector is pen.'),
(33,r'\mathrm{Grass}^{m+1}(P) \longrightarrow',r'\mathrm{Grass}^{m+1}(P) \hand{\longrightarrow}','The functor arrow is handwritten.')
]
# Point occurrences outside the replaced diagrams.
changes91.extend([
(16,r'\hand{$\zeta$}',r'\hand{$\unsure{\xi|\zeta}$}','The curled point glyph allows xi or zeta.'),
(21,r'\hand{$\zeta$}',r'\hand{$\unsure{\xi|\zeta}$}','The repeated curled base-change point glyph allows xi or zeta.'),
(28,r'\hand{\unsure{$\eta$|$\zeta$}}',r'\hand{\unsure{\eta|y|\zeta}}','The first generic-fibre index is looped; eta/y are plausible, while the source zeta candidate remains marked.'),
(28,r'\hand{\unsure{$\eta$|$\zeta$}}',r'\hand{\unsure{\eta|y|\zeta}}','The second generic-fibre index repeats the same uncertain looped glyph.')
])
finish_reviewed(91,changes91,[
(5,'Foliation','85 above;91 below','confirmed','Both handwritten numbers read directly.'),
(16,'Grassmannian argument overwrite','T-like pen glyph over typed P','retained_uncertain','The dark merged character supports T but its underlying strokes remain intertwined.'),
(21,'Deleted (P)','Crossed parenthetical P','retained_uncertain','Irregular crossed strokes remain compatible with the source pen-deletion encoding; no secure separate series of typed x impressions was resolved.'),
(21,'Final s in changements','Handwritten final s','confirmed','Pen addition visible at the end of the typed word.'),
(9,'Overtyped ordinary words','explications; les diagrammes; diagramme; implique; naturel','confirmed','All final words read directly; overtyping does not prevent these readings.'),
(11,'Three complete squares','Leftward horizontal arrows; downward vertical arrows','confirmed','Every object, underlined base, equality, index and arrow direction in all three diagrams compared.'),
(35,'Section boundary','15 begins after the functor paragraph','confirmed','The heading and opening line of section15 read fully.')
],'Both complete scan parts read. All three square diagrams, the universal-base argument, point glyphs, pen corrections and typed insertions were compared. The end of section14 and beginning of section15 are both covered.')
changes92=[
(7,r'\inserted{pour}',r'\inserted[typed]{pour}','The interlinear pour is typed; the curved stroke places it between que and la and does not delete la.'),
(10,r'\over{an}{\unsure{è}}',r'\over{an}{è}','The pen grave accent and e-shaped correction are readable over the typed an.'),
(21,r'\inserted{commutatif}',r'\inserted[typed]{commutatif}','The word commutatif is typewritten above the line; its connector ends before de without deleting it.'),
(25,r'''\begin{tikzcd}
P & \underline{P} \arrow[l] \arrow[d] \\
S \arrow[u, dash] & G \arrow[l]
\end{tikzcd}''',r'''\begin{array}{ccc}
P & \hand{\longleftarrow} & \underline{P} \\
\hand{\vert} & & \hand{\downarrow} \\
S & \hand{\longleftarrow} & G
\end{array}''','All connectors are handwritten. The left vertical stroke has no secure arrowhead; the other three directions are clear.'),
(32,r'grasm\unsure{a}nienne',r'grasm\unsure{a|à}nienne','A small accent-like mark sits above a; plain a and à remain possible.'),
(33,r'\longrightarrow P\times_S G',r'\hand{\longrightarrow} Px_S G','The arrow is handwritten and the product marker is a typed lowercase x.'),
(34,r'\inserted{schéma des paramètres d\'une}',r'\inserted[typed]{schéma des paramètres d\'une}','The whole interlinear phrase is typewritten, with a pen placement line.')
]
# Use double-quoted Python strings for the literal apostrophe in the insertion.
changes92[-1]=(34,"\\inserted{schéma des paramètres d'une}","\\inserted[typed]{schéma des paramètres d'une}",'The whole interlinear phrase is typewritten, with a pen placement line.')
import re
src92=source_path('ega25_25_092').read_text()
for m in re.finditer(r'\\hand\{(?:\$)?\\zeta(?:\$)?\}',src92):
 changes92.append((src92.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\xi|\zeta}}','The curled handwritten point glyph allows xi or zeta; retain the alphabet ambiguity.'))
finish_reviewed(92,changes92,[
(5,'Foliation','86 above;92 below','confirmed','Both numbers read directly.'),
(15,'Clipped line ending','cel at the right edge','confirmed','The crop comment remains; no unseen hyphen or letters supplied.'),
(23,'Diagram label','(D) in pen at the left','confirmed','Both parentheses and D checked.'),
(35,'Family notation','P with lower s k(point), and incidence P with underline','confirmed','Every index, underline and field argument compared.'),
(38,'Closing parenthesis after Spec(k)','Additional pen closing parenthesis','confirmed','The sloping pen stroke closes the earlier textual parenthesis.'),
(40,'Overtyped dessus and P','Readable final words and P','confirmed','Final forms checked beneath the overtyping.'),
(34,'Page spacing and spellings','d es; lescas lesplus; familled e; d e','confirmed','The visible spaced/joined forms are retained without normalization.'),
(13,'Named correspondents and references','Serre, Zariski; sections4 and6','confirmed','Both names and section references read directly.')
],'Both full image parts read. The generalization discussion, complete square diagram, all parameter-space indices and every interlinear insertion were checked; the left diagram connector remains arrowless.')
changes93=[
(7,r'\longrightarrow \unsure{P}_T',r'\hand{\longrightarrow} \unsure{P|B}_T','The arrow is handwritten; the target capital shows superposed P/B bowls.'),
(10,r'f:X \longrightarrow P',r'f:X \hand{\longrightarrow} P','The morphism arrow is handwritten.'),
(10,r'X\times_P\underline{P}',r'Xx_P\underline{P}','The product marker is the typed lowercase x.'),
(12,r'''\diagram{\begin{tikzcd}
X \arrow[d] & \underline{X} \arrow[l, dash] \arrow[d] \\
S & G \arrow[l]
\end{tikzcd}}''',r'''\diagram{\begin{array}{ccc}
X & \hand{\unsure{\longleftarrow|\relbar}} & \underline{X} \\
\hand{\downarrow} & & \hand{\downarrow} \\
S & \hand{\longleftarrow} & G
\end{array}}''','The connectors are pen strokes. The upper connector has a faint left-end hook, so left-arrow and bar remain possible; the other three directions are clear.'),
(26,r'\underline{P} \longrightarrow P',r'\underline{P} \hand{\longrightarrow} P','The projection arrow is handwritten.'),
(27,r'\uline{à fibres géométrique\xout{x}ment irréductibles de dimension N-m}',r'\uline{à fibres géométrique\xout{\unsure{s}}ment irréductibles de dimension} N-m','The underline ends before N-m; the cancelled intraword character resembles s beneath x overprinting.'),
(28,r'\underline{X} \longrightarrow X',r'\underline{X} \hand{\longrightarrow} X','The base-changed projection arrow is handwritten.'),
(29,'envisagées',r'\unsure{envisaagées|envisagées}','The enlarged word shows extra a-like impressions; preserve both readings rather than silently select the regular spelling.'),
(29,'changment',r'\unsure{changment|chqngment}','The overtyped second vowel has a q-like lower stroke; both visible readings remain.'),
(29,r"s'applique\xout{x}ront",r"s'applique\xout{\unsure{r|s}}ront",'The cancelled extra character has r/s-like traces under x; do not print the cancellation x as the underlying text.'),
(34,r'$d < m$',r'$d \hand{<} m$','The dimension comparison is handwritten.'),
(34,r'$< N$',r'$\hand{<} N$','The second comparison is handwritten.'),
(35,r'\underline{Z} \longrightarrow G',r'\underline{Z} \hand{\longrightarrow} G','The arrow is handwritten.'),
(36,r'= \emptyset',r'= \hand{\emptyset}','The first empty-set sign is handwritten.'),
(37,r'\overline{f(Z)}',r'\overset{\hand{\rule{1.8em}{0.35pt}}}{f(Z)}','The closure bar is drawn by hand above typed f(Z); only the bar is marked as handwritten.'),
(37,r'= \emptyset',r'= \hand{\emptyset}','The second empty-set sign is handwritten.'),
(38,r'\inserted{sur (D)}',r'\inserted[typed]{sur (D)}','The phrase sur (D) is typed above the line with a pen placement curve.'),
(38,r'\neq \emptyset',r'\hand{\neq} \hand{\emptyset}','The live non-equality and empty-set signs are handwritten.'),
(39,r'\neq \emptyset',r'\hand{\neq} \hand{\emptyset}','The same signs in the cancelled sentence were handwritten before cancellation.')
]
import re
src93=source_path('ega25_25_093').read_text()
for m in re.finditer(r'\\hand\{(?:\$)?\\eta(?:\$)?\}',src93):
 changes93.append((src93.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\eta|y}}','The looped handwritten generic-point glyph permits eta or y, as noted for this page.'))
finish_reviewed(93,changes93,[
(5,'Foliation','87 above;93 below','confirmed','Both numbers read directly.'),
(7,'End of fermée','Overtyped final é/e at the right crop','retained_uncertain','The two supplied endings remain possible.'),
(24,'Cancelled interlinear phrase','de dimen','confirmed','Typed phrase and x cancellation read directly.'),
(29,'ici et plus tard','Handwritten insertion before sont','confirmed','All words and its placement curve inspected.'),
(38,'Revised inequality','Greater-or-equal over an indistinct earlier angle','retained_uncertain','Final hand inequality is clear; the underlying less-than candidate remains uncertain.'),
(39,'Deleted final clause','et de façon plus précise ... Pour la propriété ...','confirmed','Cancellation extends over the complete clause but leaves terminal il live.'),
(18,'Overtyped words','toutes; ce raisonnement','confirmed','Final word readings remain legible at enlargement.')
],'Both complete scan parts read; the square diagram, all flatness and dimension hypotheses, every index and the final deleted clause were checked. Enlarged overtyped spellings are preserved with explicit doubt rather than regularized.')
changes94=[
(7,r'\unsure{résultait}','résultait','The complete word is readable despite the overtyping.'),
(8,r'\neq \emptyset',r'\hand{\neq} \hand{\emptyset}','The non-equality and empty-set signs are handwritten.'),
(8,r'\xout{xxx}',r'\xout{\illegible{1}}','The right-edge cancelled fragment cannot be recovered as a word; the visible x impressions are cancellation.'),
(11,r'P \times_S T',r'Px_S T','The product marker in the cancelled formula is a typed lowercase x.'),
(12,r'} \rightarrow G',r'} \hand{\rightarrow} G','The arrow following the generic-fibre Z is handwritten; its source and target are retained as printed.'),
(18,r'\unsure{éggalement|également}',r'\unsure{éégalement|éggalement|également}','The initial overprinting also supports a repeated accented e; retain all visible candidates.'),
(18,r'f:X $\longrightarrow$ P',r'f:X $\hand{\longrightarrow}$ P','The nonramified-morphism arrow is handwritten.'),
(20,r'$x \in P(k)$',r'$x \hand{\in} P(k)$','The membership sign is handwritten.'),
(20,r'$n \geqslant m$',r'$n \hand{\geqslant} m$','The comparison within the typed insertion is handwritten.'),
(21,r'\inserted{E(x,V)}',r'\inserted[typed]{E(x,V)}','The interlinear E(x,V) consists of typed characters; the enclosing placement curve is pen.'),
(21,r'\hand{\xi} \in G(k)',r'\hand{\xi} \hand{\in} G(k)','The membership sign beside the handwritten point is itself handwritten.'),
(22,r'\inserted{\unsure{z}}',r'\inserted[typed]{\unsure{z|g}}','The raised glyph has typewriter serifs and overprinted z/g-like strokes; the connector is pen.'),
(22,r'\xout{en lequel on ait bien $\underline{P}$ P soit ramifié}',r'\deleted{\xout{en lequel on ait bien $\underline{P}$ P soit ramifié}}','A continuous pen stroke crosses the already typewriter-cancelled clause and extends beyond its final letters.'),
(25,r'\underline{P}_{\hand{\xi}} \rightarrow P',r'\underline{P}_{\hand{\xi}} \hand{\rightarrow} P','The first tangent-condition morphism arrow is handwritten.'),
(25,r'T_z(\underline{P}\ ) \rightarrow T_x(P)',r'T_z(\underline{P}\ ) \hand{\rightarrow} T_x(P)','The tangent-space arrow is handwritten.'),
(26,r'\underline{P}_{\hand{\xi}} \rightarrow P',r'\underline{P}_{\hand{\xi}} \hand{\rightarrow} P','The parenthetical morphism arrow is handwritten.'),
(28,r'\inserted{\unsure{constructible}}',r'\inserted{constructible}','The full handwritten replacement word is legible above the cancelled typed fermé.'),
(29,r'\unsure{\over{+}{-}}',r'\unsure{\over{+}{-}|+}','The added stroke may change plus to minus, but a surviving plus remains possible from the ink; the arithmetic is not used to choose.'),
(29,r'\xout{xx}',r'\xout{\unsure{un}}','The short cancelled group resembles un beneath the two x impressions.'),
(29,r"l'appli\unsure{:}",r"l'appli\unsure{:|-}",'The cut line ending permits a colon-like mark or a damaged hyphen.'),
(31,r'\inserted{fermé E}',r'\inserted[typed]{fermé E}','The interlinear fermé E is typewritten.'),
(31,r'\inserted{x}',r'\inserted[typed]{x}','The raised x is a typed character with a pen attachment.'),
(31,r'\underline{X} \longrightarrow G',r'\underline{X} \hand{\longrightarrow} G','The first lower arrow is handwritten.'),
(32,r'\underline{P} \longrightarrow',r'\underline{P} \hand{\longrightarrow}','The second lower arrow is handwritten.'),
(32,r'\unsure{\over{G}{G}}',r'\over{G}{G}','The retouched letter is clearly G; both typed and pen layers are retained.'),
(32,r'\underline{P} \longrightarrow P',r'\underline{P} \hand{\longrightarrow} P','The third lower arrow is handwritten.'),
(33,r'\unsure{\over{+}{-}}',r'\unsure{\over{+}{-}|+}','The repeated sign has the same plus/minus ambiguity; do not settle it from the displayed arithmetic.')
]
import re
src94=source_path('ega25_25_094').read_text()
for m in re.finditer(r'\\hand\{\\eta\}',src94): changes94.append((src94.count('\n',0,m.start())+1,m[0],r'\hand{\unsure{\eta|y}}','The handwritten generic-point glyph has the looped eta/y form.'))
finish_reviewed(94,changes94,[
(5,'Foliation','88 above;94 below','confirmed','Both handwritten numbers read directly.'),
(7,'spécifil/spécifiq','Overtyped ending of the adjective','retained_uncertain','The source alternatives remain compatible with the last crowded letter.'),
(8,'Zrréductible','Initial capital Z-like typewriter glyph','confirmed','The unusual initial is visible and retained.'),
(9,'Three cancelled draft lines','pour tout La précision ... de dimension incidenceP P x_S T ...','confirmed','Every readable word, symbol and line of the long typewriter cancellation was compared.'),
(18,'Nous with lowered o','o genuinely below the ordinary baseline','confirmed','Enlargement confirms the unusual lowered letter; source subscript form retained.'),
(19,'Two additions','Handwritten incidenceP to P x_k G quasi-fini; typed algebraically-closed-field parenthesis','confirmed','All symbols and both attachment points read directly.'),
(28,'Constructibility layers','Typed constructible cancelled; typed fermé inserted and pen-deleted; handwritten constructible restored','confirmed','All three layers are present in the image.'),
(29,'Two N-n sign occurrences','Plus/overwritten-minus ambiguity','retained_uncertain','Each glyph was checked from its own ink; the dimension calculation supplies no reading decision.'),
(25,'Tangent source','T_z of underlined P without point subscript','confirmed','No missing point index supplied.'),
(33,'Final parentheses','Both large parentheses handwritten','confirmed','They enclose the complete X-dimension clause.')
],'Both complete image parts read, including all three cancelled draft lines and the differential condition. All tangent maps, indices, layered constructibility revisions and the two ambiguous arithmetic signs were inspected separately.')
finish_reviewed(95,[
(7,r'dim $P$',r'dim $\unsure{P|G}$','The capital after dim is overtyped and has P/G-like traces; retain both rather than choose from the dimension argument.'),
(7,r'\hand{$y$}',r'\hand{\unsure{\eta|y}}','The first handwritten point subscript is looped and permits eta/y.'),
(7,r'= \emptyset',r'= \hand{\emptyset}','The empty-set sign is handwritten.'),
(7,r'\hand{$y$}',r'\hand{\unsure{\eta|y}}','The second point subscript repeats the same looped glyph.'),
(7,r'lisse\hand{.}\inserted{\unsure{sur $k(y)$}}',r'lisse\inserted{sur $k(\unsure{\eta|y})$}\hand{.}','The words sur and k(parenthesized point) are readable. The connector attaches after lisse and before the full stop; only the point alphabet remains doubtful.'),
(15,r'\unsure{infini}','infini','The six underlying letters are legible beneath the typewriter cancellation.'),
(17,r'\unsure{et 7.5.}','et 7.5.','The cancelled connective, numerals and points are readable.')
],[
(5,'Foliation','89 above;95 below','confirmed','Both handwritten numbers read directly.'),
(7,'fortiori and dimension capital','fortiori readable; capital P/G overtyped','retained_uncertain','The ordinary word is clear; the overtyped capital is kept uncertain.'),
(13,'Cancelled word after redites','Underlying word remains obscured','retained_illegible','Individual fragments do not settle a complete word.'),
(18,'Short cancellation before c’est','One or two obscured characters','retained_illegible','The x impressions prevent a secure underlying reading.'),
(18,'une application and de','Two typed interlinear insertions; de nature remains live','confirmed','Both additions and their connectors checked; no cancellation crosses de nature.'),
(22,'Overtyped words and preserved spelling','résultats; respris; allure; essayant; conséquence; et; variante','confirmed','Every word compared in the lower scan; respris retained as printed.'),
(27,'Section references','2.12–2.18;4;5;7.1–7.4;3and6;8.7c twice','confirmed','All numbers and the cancelled7.5 checked directly.'),
(30,'End of text and lower margin','Complete ending avec plus de détails ... particulières; blank remainder','confirmed','All text and the full lower blank region inspected.')
],'Both complete scan parts read, including the upper-margin addition and the whole closing paragraph of section15. All references and cancellations checked; unresolved words and the overtyped dimension capital remain marked.')

finish_reviewed(96,[],[
(6,r'\mspage{96}','96 in pencil at foot','confirmed','Both numerals are plainly legible; no other writing appears on either scan part.'),
(5,'NOTES: tiny specks','Isolated dark speck in upper image; two isolated specks at lower right/centre','confirmed','All surrounding blank areas inspected: the dots do not form glyphs or lines of writing.')
],'Both full images inspected from upper edge through lower edge and every margin; only the handwritten archive number96 is present. The isolated specks noted in NOTES were inspected individually.')
finish_reviewed(97,[
(11,r'\unsure{§ 2)}',r'\unsure{§ 2)|§ 21}','The last heading mark can also be a faint 1; no secure choice can be made from the supplied image.'),
(21,r'\xout{\illegible{3}}',r'\unsure{\xout{\illegible{3}}}','The dense faint beginning may be a typewriter cancellation, but its precise extent and underlying words cannot be verified; mark the cancellation itself uncertain.'),
(25,r'\xout{\illegible{4}}',r'\unsure{\xout{\illegible{4}}}','The suspected cancellation between the two rest. fragments is too pale to establish its extent securely.'),
(27,r'\xout{\illegible{2}}',r'\unsure{\xout{\illegible{2}}}','The faint group after S_i may be struck out, but neither the underlying words nor cancellation extent is secure.')
],[
(7,'NOTES: faint lines above heading','Two faint upper lines with an additional displaced trace','retained_illegible','Original and contrast-enhanced channel views inspected; isolated strokes do not permit recovery of words.'),
(11,'NOTES: main heading and second line','Heading underlines visible; words remain tentative','retained_uncertain','Every word position was inspected; the supplied readings cannot be confirmed letter by letter at this contrast.'),
(15,'NOTES: subsection headings','Faint underlined lines with recognisable projectifs fragments','retained_uncertain','Neither the full words nor their punctuation can safely be resolved from this image.'),
(19,'NOTES: proposition line','Faint Proposition 1.1-shaped group with underline','retained_uncertain','Numbering, words and rank condition remain uncertain; the next page is not substituted as evidence.'),
(21,'NOTES: suspected cancellations','Three dense faint groups retained with uncertain cancellation scope','retained_uncertain','All three groups were separately inspected in the original and enhanced views.'),
(26,'Formula rows','S_i, inverse-image and f-star fragments remain faint','retained_uncertain','Each visible subscript and superscript location was compared; no additional legibility was gained for a secure correction.'),
(29,'Corollary paragraphs','All lines, prime groups, rank numerals and references remain tentative','retained_uncertain','The pale trace preserves the line layout but does not settle all individual characters.'),
(38,'Last formula and following line','Fragmented formula and de la forme-like ending','retained_uncertain','The lower scan and its enhancement were inspected across the full line; the unreadable groups stay marked.'),
(41,'NOTES: faint star and final paragraph','Small cross/star-like trace; Un autre-like opening','retained_uncertain','The mark and the final two pale lines remain too faint to resolve.'),
(45,'NOTES: archive number','97 in pencil','confirmed','Both digits are clear in the lower image; complete lower margin inspected.')
],'Both supplied images inspected in full, then all faint lines inspected again in blue-channel local-contrast views and compared with the source line by line. The page remains severely illegible: the inspection does not certify the uncertain words as recovered. All existing uncertain readings and illegible groups are retained; the suspected cancellation scopes are now also explicitly uncertain. No text was imported from another page.')
finish_reviewed(98,[
(11,r'\deleted{\over{C}{\unsure{+}}\uline{artier},',r'\hand{\unsure{+|t}}\deleted{\uline{Cartier},','The small free pen sign is above the final part of Cartier, not a replacement of its initial C; the whole word is readable beneath diagonal cancellation strokes. The sign permits plus/t readings.'),
(17,r'\inserted{\unsure{fini}} $\geqslant 2$',r'\hand{fini} $\hand{\geqslant 2}$','fini and the comparison with2 are pen writing in the blank on the line; fini is legible and has no separate insertion caret.'),
(19,r'\margin{*}',r'\margin{\unsure{*|+}}','The marginal mark has cross/star-like strokes with short adjacent dashes; its exact glyph is doubtful.'),
(20,r'n\in\underline{Z}',r'n\hand{\in}\underline{Z}','The membership sign in the indexing subscript is handwritten.'),
(21,r'\unsure{pour tout n}',r'pour tout n','The underlying words and n can be read beneath the typewriter x cancellation.'),
(24,r'\unsure{et la classe}',r'et la classe','All three underlying words are legible through the x impressions.'),
(29,r'$\geqslant 2$',r'$\hand{\geqslant} 2$','The comparison in the rank list is handwritten, while the adjacent2 is typed.'),
(30,r'S^{i}',r'S^{\unsure{i|n}}_{\unsure{a|n}}','The enlarged image shows a crowded raised i/n-like group and a separate dark lower a/n-like overprint; both positions are preserved without resolving the overtyping.'),
(37,r'n\in\underline{Z}',r'n\hand{\in}\underline{Z}','The membership sign in Corollary1.3 is a pen addition.'),
(39,r'de \underline{L}.',r'de \underline{L}.\margin{\ensuremath{\swarrow}}','The long diagonal pen stroke terminates below this line in a leftward/downward arrowhead; record the graphic without assigning deletion scope to the body.'),
(42,r'Pic(S)$\longrightarrow$',r'Pic(S)$\hand{\longrightarrow}$','The first Picard-group arrow is drawn by hand.'),
(42,r'\underline{Z} $\longrightarrow$',r'\underline{Z} $\hand{\longrightarrow}$','The second Picard-group arrow is handwritten.'),
(42,r'Pic(\unsure{P})',r'Pic(\unsure{P|R|E})','The overtyped target capital contains P/R-like strokes and traces compatible with E; no choice is made from the map.'),
(42,r', le premier',r', le premier\margin{\ensuremath{\swarrow}}','A second diagonal pen stroke crosses the last paragraph and ends at a thick leftward/downward point in the lower margin.'),
(43,r'\margin{98}',r'\margin{\unsure{$\backslash$|1}}\margin{98}','A separate short curved descending pen stroke appears below the arrow terminal. Backslash-like mark and numeral1 remain possible; its graphic presence is explicit without assigning a function.')
],[
(5,'Foliation and manuscript label','1 above; Nouveau EGA V;98 below','confirmed','All three handwritten items read directly.'),
(7,'Replacement title','Faisceaux inversibles et diviseurs sur les fibrés projectifs et multiprojectifs. Systèmes linéaires de diviseurs.; cancelled familles de','confirmed','Every word of the upper handwritten title and its separate cancellation checked.'),
(8,'NOTES: diagonal marks','Two long diagonal strokes with thick lower-left terminals','retained_uncertain','Their graphic direction is clear; a scope of deletion over the body is not securely established, so no body passage is newly marked deleted.'),
(10,'NOTES: IV20/21','Typed0 densely overwritten by pen1-like stroke','confirmed','The typed oval survives beneath the added vertical stroke; source overwrite retained.'),
(14,'Applicationx and groupe','Final typed x cancellation; pen-cancelled groupe; slash after des','confirmed','All three revision marks and both title underlines inspected.'),
(18,'Cancelled rank condition','n’est nul en aucun point','confirmed','The underlying phrase remains readable under the x row.'),
(20,'NOTES: short cancelled group','Underlying word obscured by four x-like impressions','retained_illegible','The fragments do not establish a complete word.'),
(22,'NOTES: cancelled formula line','Typewriter cancellation plus long irregular pen loops','retained_uncertain','The candidate formula and restriction phrase remain partly obscured; both cancellation layers are present.'),
(23,'Twist in theorem','Typed O_P(1) followed by f-star(M)(n)','confirmed','The apparent1/n difference is visibly present and is retained.'),
(28,'NOTES: en somme insertion','le in pen; préschéma typed; shared curve before somme','confirmed','The curve attaches between en and somme.'),
(35,'Nonempty addition','non vide typed above connexe','confirmed','Characters and pen connector checked.'),
(43,'Bottom margin','98 plus diagonal terminal and a short pen tick','confirmed','Entire lower and side margins inspected; the short tick below the terminal has no secure textual reading.')
],'Both complete image parts read line by line, including all title revisions, the long cancelled formula, every prime/index and both lower paragraphs. Diagonal graphics are recorded with their positions; no unsupported deletion of the whole page is inferred. Enlarged title, cancellation and S-index crops inspected.')
changes99=[
(8,r'f:P\longrightarrow S',r'f:P\hand{\longrightarrow} S','The structural-morphism arrow is handwritten.'),
(10,r'\underline{Z} \longrightarrow',r'\underline{Z} \hand{\longrightarrow}','The arrow in formula(x) is handwritten.'),
(12,r'1.\unsure{1}.',r'1.\unsure{1|4}.','The last digit has superimposed1/4-like strokes; retain both candidates.'),
(12,r'\uline{Corollaire} 1.4.',r'\uline{Corollaire} 1.4.\margin{\ensuremath{\swarrow}}','The upper diagonal pen stroke terminates beside this heading with a lower-left arrowhead.'),
(17,r'$\geqslant 2$',r'$\hand{\geqslant} 2$','The rank comparison is handwritten.'),
(17,r'1.\unsure{4}.',r'1.\unsure{4|3}.','The overtyped numeral has a4 shape with an additional curved trace compatible with3.'),
(26,r'$\geqslant$1',r'$\hand{\geqslant}$1','The dimension comparison is handwritten.'),
(26,r'$\geqslant$2',r'$\hand{\geqslant}$2','The second comparison in the same line is handwritten.'),
(27,r'$\geqslant$0',r'$\hand{\geqslant}$0','The comparison after m-n is handwritten.'),
(27,r'd $>$0',r'd $\hand{>}$0','The strict comparison is handwritten.'),
(30,r'n\in\underline{Z}',r'n\hand{\in}\underline{Z}','The membership sign in the family subscript is a pen addition.'),
(32,r'\underline{L} \simeq',r'\underline{L} \hand{\xrightarrow{\sim}}','The lower horizontal stroke has a rightward arrowhead, with a handwritten tilde above it.'),
(33,r'\xrightarrow{\sim}',r'\hand{\xrightarrow{\sim}}','The displayed isomorphism arrow and tilde are drawn by hand.'),
(33,r'\unsure{L|E}',r'\unsure{L|E|M}','The enlarged overtyped capital also has an M-like pair of stems; the ink does not settle the letter.'),
(34,r'\xrightarrow{\sim}',r'\hand{\xrightarrow{\sim}}','The arrow and its tilde are pen strokes.'),
(35,r'\xrightarrow{\sim}',r'\hand{\xrightarrow{\sim}}','The arrow and tilde before f-star are handwritten.'),
(36,r'isomorphe (\,',r'isomorphe \unsure{(|à}\,','The opening-parenthesis position contains an overtyped à-like character; both visible readings are preserved.'),
(37,r'\xleftarrow{\sim}',r'\hand{\xleftarrow{\sim}}','The final isomorphism arrow points left, and both it and the tilde are handwritten.'),
(37,r'\underline{O}_S',r'\underline{O}_{\unsure{S|S_S}}','The image shows two vertically displaced S impressions below/right of O; retain the possible repeated subscript rather than silently collapse it.'),
(37,r'(xx).',r'(xx).\margin{\ensuremath{\backslash}}','The second long pen stroke continues diagonally down-right to the lower edge; its graphic is recorded without assigning a deletion scope.')
]
# Uniquely contextual replacements avoid marking the just-added arrows twice.
changes99[12]=(33,r'M \xrightarrow{\sim}',r'M \hand{\xrightarrow{\sim}}','The displayed isomorphism arrow and tilde are drawn by hand.')
changes99[14]=(34,r'$\underline{L} \xrightarrow{\sim}',r'$\underline{L} \hand{\xrightarrow{\sim}}','The arrow and its tilde are pen strokes.')
changes99[15]=(35,r'$\underline{L}(-n) \xrightarrow{\sim}',r'$\underline{L}(-n) \hand{\xrightarrow{\sim}}','The arrow and tilde before f-star are handwritten.')
finish_reviewed(99,changes99,[
(5,'NOTES: whole-page diagonal strokes','Upper diagonal ends at Corollary1.4; lower diagonal runs to bottom edge','retained_uncertain','The lines are real pen marks, but their intended deletion scope is not established by the strokes; body text is retained.'),
(6,'Foliation','2 above;93 below','confirmed','The bottom number visibly reads93 despite the archive site99.'),
(10,'NOTES: product and cancelled characters','Typed x after Pic(S), followed by dense cancellation','retained_uncertain','The first x is separately visible; the following underlying group remains partly obscured.'),
(12,'Nonempty condition','Handwritten si S not equal empty set','confirmed','All words and both symbols of the insertion read directly.'),
(13,'Corollary revision','Typed injectif above cancelled un isomorphisme; pen-cancelled non vide after connexe','confirmed','Insertion and cancellation layers checked independently.'),
(16,'Marginal bracket','One handwritten opening square bracket','confirmed','It stands beside Lorsqu’on; no closing mate is visible on this page.'),
(18,'Typed qualification','si S est connexe, mais','confirmed','Words are typed above the line after surjectif, with a handwritten attachment.'),
(19,'NOTES: injectif/bijectif','Crowded initial letters of the live word','retained_uncertain','The initial overtyping does not settle the two readings.'),
(20,'Cancelled kernel description','à Z resp. à Pic(S)xZ lorsque E est de rang1 resp. de rang0)','confirmed','Every word and index in the cancelled typed line was read; source contents retained.'),
(32,'NOTES: f-star overwrite','Lower typed star-like group; raised pen star','confirmed','Both positions are visible; source overwrite macro retained.'),
(33,'Formula(xx) alphabet','Initial M lacks underline; inner letter is overtyped','confirmed','The un-underlined M is retained and the inner letter remains doubtful.'),
(37,'NOTES: final word','isomorphisme/isemorphisme','retained_uncertain','The partly overtyped vowel remains uncertain in the enlarged scan.'),
(37,'References','1.1,1.2,1.4 and literal(réf)','confirmed','All references compared, with the two overtyped numeral positions separately doubtful.')
],'Both full images read line by line and all margins inspected. The proof formulas were enlarged to check arrowheads, underlines, the f-star overwrite, overtyped letters and displaced S impressions. The long graphics have no imposed deletion interpretation.')
finish_reviewed(100,[
(7,'% NOTE: a single long handwritten diagonal stroke crosses the whole page from top to bottom; it is transcribed as a deletion of each paragraph','% NOTE: a single long handwritten diagonal stroke crosses the whole page from top to bottom; its function as a cancellation is uncertain. The graphic is recorded at the end of the page without assigning deletion scope to all paragraphs.','The visible diagonal does not establish a paragraph-wide author deletion; its uncertain function is explicitly recorded.'),
(8,r'\deleted{Prouvons',r'Prouvons','Remove the unsupported whole-paragraph deletion wrapper; only the diagonal graphic is certain.'),
(12,r'f^{-1}(U)$.}',r'f^{-1}(U)$.','Close removal of the unsupported first whole-paragraph deletion wrapper.'),
(14,r'\deleted{\hand{\unsure{[}}',r'\hand{\unsure{[|(}}','Remove unsupported paragraph-wide deletion; the separate opening bracket-like pen mark remains uncertain, including a parenthesis-like candidate.'),
(18,r'endeux pas:}',r'endeux pas:','Close removal of the second unsupported whole-paragraph deletion wrapper.'),
(20,r'\deleted{a) S',r'a) S','Remove unsupported whole-paragraph deletion of the field-case proof; preserve its local cancellations separately.'),
(37,r'associé sur P}',r'associé sur P\margin{\ensuremath{\backslash}}','The long diagonal continues through this ending to the lower edge. Record its graphic without treating all proof text as certainly deleted.'),
(11,r's $\in$ S',r's $\hand{\in}$ S','The membership sign is a pen stroke.'),
(12,r'n $\in \underline{Z}$',r'n $\hand{\in} \underline{Z}$','The membership sign before the underlined Z is handwritten.'),
(12,r'\underline{L}\,|\,',r'\underline{L}\,\hand{|}\,','The restriction bar after L is drawn by hand.'),
(12,r'\underline{O}_P(n)\,|\,',r'\underline{O}_P(n)\,\hand{|}\,','The second restriction bar is handwritten.'),
(14,r'$\geq$ 2',r'$\hand{\geq}$ 2','The greater-or-equal sign is handwritten.'),
(15,r'$\leq$ 1',r'$\hand{\leq}$ 1','The less-or-equal sign is handwritten.'),
(15,r'\hand{\unsure{]}}.',r'\hand{\unsure{]|)}}.','The overwritten closing mark permits a bracket or parenthesis; neither layer is fully clear.'),
(22,r"\inserted{$L'$}",r"\inserted[typed]{$L'$}",'The interlinear L-prime has typewriter serifs; the placement stroke is handwritten.'),
(22,r'\tilde{L}',r'\overset{\hand{\sim}}{L}','The tilde above the typed L is drawn by hand.'),
(24,r'\inserted{q:}',r'\inserted[typed]{q:}','The q and colon are typed; the curved insertion mark is pen.'),
(24,r'\longrightarrow P_k^r',r'\hand{\longrightarrow} P_k^r','The projection arrow is handwritten.'),
(25,r'$\to E^{r+1}$',r'$\hand{\to} E^{r+1}$','The immersion arrow is handwritten.'),
(26,r'\inserted{affine}',r'\inserted[typed]{affine}','All six letters of affine are typed above the line.'),
(28,r'$\geq$ 2',r'$\hand{\geq}$ 2','The dimension comparison is a pen addition.'),
(28,r"\tilde{L'}",r"\overset{\hand{\sim}}{L'}",'The tilde above L-prime is handwritten.'),
(29,r'module inversible M sur',r'module inversible \unsure{M|N} sur','The heavy overtyped capital has M/N-like diagonal traces; no algebraic identification is used to settle it.'),
(31,r'L $\to$ M',r'L $\hand{\to}$ M','The homomorphism arrow is handwritten.'),
(34,r'étant factoriel, L est',r'étant factoriel, \over{L}{L} est','The capital L is reinforced by a broad pen vertical and lower horizontal stroke over its typed form.')
],[
(5,'Foliation','3 above;100 below','confirmed','Both handwritten numbers read directly.'),
(7,'NOTES: diagonal','Single continuous pen line from upper text through lower edge','retained_uncertain','Its presence is certain; its function is unresolved. The source’s blanket deletion interpretation is withdrawn, with parent auditor agreement.'),
(15,'NOTES: bracket-like marks','Opening and closing marks around the rank observation','retained_uncertain','Both forms remain crowded, with possible typed parenthesis remnants.'),
(17,'NOTES: projective-space exponent','r followed by typewriter-cancelled+1 and a pen bracket-like mark','retained_uncertain','The exponent cancellation is visible; the adjacent pen mark remains doubtful.'),
(22,'NOTES: L-prime insertion','Typed L-prime with a pen attachment; handwritten tilde on the following L','confirmed','Typing and pen layers checked separately in the upper/lower overlap.'),
(27,'NOTES: factoriel overtyping','factori, cancelled e-like character, el','retained_uncertain','The crowded underlying letter remains uncertain.'),
(29,'NOTES: cancellation after inversible','Underlying short group remains obscured','retained_illegible','The visible fragments do not yield a secure complete reading.'),
(30,'NOTES: q-prime/q-star','Overtyped q with small raised mark','retained_uncertain','The raised mark remains compatible with prime/star; no choice from the formula is made.'),
(32,'NOTES: cancellation before points','Two-word-length x-cancelled group','retained_illegible','The surviving fragments do not settle the words.'),
(34,'NOTES: libre underline','One nearly horizontal underline','confirmed','The underline is present; no additional underline is added.'),
(18,'Spelling and reference','bréveté; précédons endeux pas; par.8','confirmed','These printed forms and the reference are retained exactly.'),
(37,'Proof ending','entant que module gradué ... le Module associé sur P','confirmed','Complete lower line and all margins inspected; sentence continues beyond the page.')
],'Both full scan parts read, including every local cancellation, the field-case proof, all ring indices and all handwriting. The single diagonal is recorded with uncertain function; it is not sufficient evidence to suppress all body paragraphs. No proof wording or mathematical notation is normalized.')
finish_reviewed(101,[
(8,r'est isomorphe',r'\margin{\ensuremath{/}}est isomorphe','The upper-left margin has an oblique pen stroke and an adjoining narrow loop; record the visible oblique graphic.'),
(11,r'\tilde{L}',r'\overset{\hand{\sim}}{L}','The tilde above L is handwritten.'),
(11,r'\unsure{q}',r'\unsure{q|i|4}','The first operator letter is overtyped with q/i/4-like remnants; no choice is made from the formula.'),
(12,r'\inserted{de rang 1}',r'\inserted[typed]{de rang 1}','The enlarged insertion has typewriter serifs on every letter and numeral; the curved attachment is pen.'),
(12,r'\deleted{comme Module}',r'comme Module','The curve belongs to the de rang1 insertion and ends above the initial M; it does not cancel the words comme Module, whose remaining letters have no strike-through.'),
(13,r'\hand{:}',r'\unsure{\hand{:}|\over{.}{:}}','The raised dot is a pen addition; the lower dot could be the original full stop. Both possible layering readings remain explicit.'),
(13,r'gradué \ par le raisonnement indiqué',r'gradué \ par le raisonnement indiqué\margin{\ensuremath{\swarrow}}','The long upper diagonal terminates below this line with an arrow-like lower-left head.'),
(16,r'\ CQFD',r'\ CQFD\margin{\ensuremath{/}}','A shorter oblique pen stroke crosses the cohomology line; its function is left unspecified.'),
(20,r'Z(S) \longrightarrow',r'Z(S) \hand{\longrightarrow}','The displayed homomorphism arrow is handwritten.'),
(21,r'\inserted{les}',r'\inserted[typed]{les}','The interlinear les is typed, not handwritten.'),
(21,r'\xout{xxxxx}',r'\xout{\illegible{1}}','The five x impressions cancel an underlying word that cannot be securely recovered; they are not literal content.'),
(21,r'\underline{n} \in Z(S)',r'\underline{n} \hand{\in} Z(S)','The membership sign is handwritten.'),
(21,r'\xout{etx}',r'\xout{\unsure{et|etu}}','The crowded ending after eff has et/etu-like traces under the cancellation; a literal final x is not secure.'),
(21,r'\inserted{aux}',r'\inserted[typed]{aux}','All three letters of aux are typed above the cancelled word.'),
(21,r'\xout{xxx}',r'\xout{une}','The underlying u-n-e can be read beneath the x impressions.'),
(21,r'n\in\underline{Z}',r'n\hand{\in}\underline{Z}','The membership in the indexing subscript is handwritten.'),
(22,r'\xout{xxxfaçonxxque}',r'\xout{de façon que}','The underlying phrase is legible; the x characters are cancellation marks.'),
(22,r'\xout{xx}',r'\xout{en}','Both underlying letters e-n are visible beneath the short cancellation.'),
(23,r'\inserted{restr à}',r'\inserted[typed]{restr à}','The abbreviation and preposition are typed; no full word is supplied for the abbreviation.'),
(23,r'\xout{valeurxsur}',r'\xout{valeur sur}','The x between the two underlying words is a cancellation impression, not content.'),
(25,r'\underline{Z}(S) \longrightarrow',r'\underline{Z}(S) \hand{\longrightarrow}','The arrow in(x bis) is handwritten.'),
(27,r'S $\neq \emptyset$',r'S $\hand{\neq \emptyset}$','Both the inequality and empty-set symbol are handwritten.'),
(28,r'\inserted[typed]{resp. connexe}\hand{)}',r'\inserted[typed]{resp. connexe}','The curve after connexe is the insertion connector returning before alors; there is no independent closing-parenthesis glyph at that point.'),
(29,r'\underline{Z} \to \underline{Z}(S)',r'\underline{Z} \hand{\to} \underline{Z}(S)','The arrow is handwritten.'),
(29,r'n \in \underline{Z}',r'n \hand{\in} \underline{Z}','The membership sign is handwritten.'),
(36,r'\underline{Z}_S \longrightarrow',r'\underline{Z}_S \hand{\longrightarrow}','The final canonical-morphism arrow is handwritten.'),
(37,r'\xout{xxxxZxSxdéfinixpar}',r'\xout{\unsure{sur} \underline{Z} S défini par}','The cancelled group visibly contains underlined Z, S, défini par; its opening resembles sur but remains doubtful.'),
(37,r'dans le schéma',r'dans le schéma\margin{\ensuremath{\backslash}}','The lower long diagonal continues from Variante through the final line and lower margin; record the graphic without assigning cancellation scope.')
],[
(5,'Foliation','4 above;101 below','confirmed','Both handwritten numbers read directly.'),
(7,'NOTES: diagonal strokes','Four principal oblique marks, including upper-left looped mark','retained_uncertain','Every stroke and terminal inspected; their purpose is not established as author deletion.'),
(10,'First Gamma formula','q with subscript star in the source','confirmed','The unusual subscript-star placement is visibly present and is retained.'),
(11,'estb','Typed estb','confirmed','The final b is visibly printed and retained.'),
(12,'NOTES: de rang1/comme Module','Typed addition with a curved insertion connector; comme Module remains live','corrected_from_scan','The enlarged crop separates the connector from any deletion stroke; no separate cancellation crosses the phrase.'),
(15,'Proof references','ChapII;III4.6.5;III2','confirmed','Every numeral and chapter designation checked directly.'),
(21,'NOTES: ouvert(s)','Final letter clipped at right edge','retained_uncertain','The rightmost trace does not settle the full s confidently.'),
(28,'NOTES: resp. connexe attachment','Typed addition after S not equal empty set, before alors','confirmed','Its curve returns to the start of alors; the source’s separate closing-parenthesis character is unsupported.'),
(30,'Overtyped readable words','dans;CQFD;surjective;Chap;sous;s’énonce','confirmed','Each listed word read in its own position; their overtyping does not prevent the readings.'),
(33,'Picard-scheme reference','ChapV and1.1','confirmed','Both references are printed as transcribed; no later chapter number supplied.')
],'Both complete images and all margins read; the typed insertions and their curved connectors were enlarged. The previously asserted cancellation of comme Module is removed because the line is an insertion connector. All formulas, underlines, indices, references, clipped letters and diagonal graphics were inspected separately.')
finish_reviewed(102,[
(12,r'dim P$\geq$1',r'dim P$\hand{\geq}$1','The dimension comparison is handwritten.'),
(12,r'P $\leq$ \unsure{0|D}',r'P $\hand{\leq}$ D','The comparison is handwritten. The following typed glyph has the straight left stem and serifs of capital D; retain that visible letter without changing it from the mathematics.'),
(17,r'dim$\leq$0',r'dim$\hand{\leq}$0','The comparison in the next dimension clause is handwritten.'),
(19,r'\xout{\unsure{xximage}}',r"\xout{l'image}",'The underlying l-apostrophe-image is readable beneath the x cancellation.'),
(20,r'\unsure{par|pr}',r'\unsure{pr|par}','The pen sequence most directly reads pr, with a possible compressed middle a; retain both without expanding the abbreviation.'),
(20,r'$\longrightarrow$Pic(P)',r'$\hand{\longrightarrow}$Pic(P)','The Picard homomorphism arrow is handwritten.'),
(21,r'f^*(\underline{M})(n)',r'f^*(\underline{M})\unsure{(|\otimes}n)','The second opening-parenthesis position is heavily overprinted and has a crossed-circle trace; both parenthesis and tensor-like readings remain possible.'),
(23,r'$\geq$1',r'$\hand{\geq}$1','The rank comparison is handwritten.'),
(23,r'à isomorphisme unique',r'à isomorphisme unique\margin{\ensuremath{/}}','The first long diagonal terminates below this line, near rang; its oblique graphic is recorded without a deletion scope.'),
(28,r'$\neq$ 0',r'$\hand{\neq}$ 0','The nonzero condition is handwritten.'),
(29,r'dim $\geq$1',r'dim $\hand{\geq}$1','The fibre-dimension comparison is handwritten.'),
(31,r'dans la démonstration).',r'dans la démonstration).\margin{\ensuremath{\swarrow}}','The second diagonal terminates at the reference1.2 with a hook/arrow-like lower-left end.'),
(35,r"g:P$\to$P'",r"g:P$\hand{\to}$P'",'The morphism arrow is handwritten.'),
(35,r"\mathcal{O}_{P'}(1)$)} sur P",r"\mathcal{O}_{P'}(1)$)} sur P\margin{\ensuremath{/}}",'The third diagonal terminates beneath définis in this line; its graphic is recorded separately from the words.')
],[
(5,'Foliation','5 above;102 below','confirmed','Both numbers read directly.'),
(6,'NOTES: three diagonals','Three continuous oblique pen strokes and their lower terminals','retained_uncertain','Their shapes and extents are visible; no whole-page deletion is inferred.'),
(7,'Spacing and unusual wording','s ection; est degré; lowercase p; s e mettre; prihcipe','confirmed','Each form is visibly present. Enlargement confirms the h-like letter in prihcipe and the separated s e.'),
(15,'NOTES: clipped fibre word','Visible fibr, with page edge cutting off the remainder','confirmed','No missing letters are supplied from context.'),
(19,'NOTES: la classe','Typed insertion above cancelled l’image','confirmed','Both typing layers and the cancellation were read.'),
(20,'NOTES: handwritten PicS insertion','Pic S cross {n}, then pr/par; connector before l’homomorphisme','retained_uncertain','The formula is legible; the final short word remains doubtful. Heavy ink at l-prime is part of the insertion region and does not settle a new word.'),
(24,'NOTES: left margin rule','One vertical pen bar covering the parenthetical revision','confirmed','Its extent from près through the next L-clause checked; no duplicated bars are added.'),
(26,'Revision statement','tout L inversible sur S','confirmed','The page visibly says sur S; this is retained despite the preceding discussion of modules on P.'),
(29,'Rank gloss','Handwritten i.e. le rang de E partout greater-or-equal2','confirmed','Every word and the comparison in the insertion read directly.'),
(31,'NOTES: reference1.2','Typed2 partly crossed by diagonal hook','confirmed','The numeral itself remains legible; no new reference is supplied.'),
(35,'Final insertion','Parenthesized isomorphism with g-star scriptO_P-prime(1)','confirmed','Both parentheses, the prime, star, script letter and index read from the pen addition.')
],'Both full scan parts and every margin read. Enlarged insertion, parenthesis overprint, separated s/e and prihcipe inspected. All three diagonal graphics are retained with unresolved function; the source’s surS and D are not mathematically emended.')
finish_reviewed(103,[
(8,r'f^{\hand{*}}_{*}',r'f^{\hand{*}}_{\hand{*}}','Both upper and lower star marks are drawn with broad pen strokes; retain both positions.'),
(8,r'\longleftarrow',r'\hand{\longleftarrow}','The first arrow is handwritten and points left.'),
(8,r'\unsure{associé}',r'\unsure{associé|assooié}','The enlarged overtyping leaves a closed o-like bowl at the expected c position; retain the visible alternative.'),
(9,r"f^{*}(\underline{E}') \to",r"f^{*}(\underline{E}') \hand{\to}",'The associated-map arrow is handwritten.'),
(10,r"g\colon P \to P'",r"g\colon P \hand{\to} P'",'The first g arrow is handwritten.'),
(10,r"\underline{O}_{P'}(1)",r"\underline{O}_{P\unsure{(|'}}(1)",'The mark following the subscript P descends as an opening parenthesis; the source prime remains an alternative. No index is corrected from the intended pullback.'),
(12,r'dimension $\geq 1$',r'dimension $\hand{\geq} 1$','The comparison inside the typed insertion is handwritten.'),
(12,r'$n \geq 0$',r'$n \hand{\geq} 0$','The consequent comparison is handwritten.'),
(13,r'\xout{$\underline{O}_P(n)$}',r'\deleted{$\underline{O}_P(n)$}','The cancelled formula has irregular diagonal pen strokes rather than a row of typewriter x characters.'),
(13,r'P $\geq 1$',r'P $\hand{\geq} 1$','The dimension comparison is handwritten.'),
(14,r'$n \geq 0$',r'$n \hand{\geq} 0$','The section-degree comparison is handwritten.'),
(14,r'\xout{aussi}',r'\deleted{aussi}','The word is crossed by a continuous pen stroke ending in a heavy vertical flick.'),
(15,r'dim $\geq 1$',r'dim $\hand{\geq} 1$','The fibre-dimension comparison is handwritten.'),
(17,r'\over{g}{S}',r'\unsure{S|g}','The enlarged group consists of superimposed typewriter S/g impressions, not a handwritten replacement; both letters are retained as an uncertain overprint.'),
(17,r"g\colon P \to P'",r"g\colon P \hand{\to} P'",'The second g arrow is handwritten.'),
(19,r"\underline{E}' \to \underline{M}",r"\underline{E}' \hand{\to} \underline{M}",'The arrow defining u is handwritten.'),
(20,r"f^{*}(\underline{E}') \to",r"f^{*}(\underline{E}') \hand{\to}",'The corresponding-epimorphism arrow is handwritten.'),
(22,r'\mathrm{cl}(\underline{M}) \in',r'\mathrm{cl}(\underline{M}) \hand{\in}','The membership sign is handwritten.'),
(24,r'\mathrm{I}\,(S,\underline{O}_S)^{*}',r'\mathrm{I}\,(S,\underline{O}_S)^{\hand{*}}','The first unit-group star has visibly extended freehand arms.'),
(25,r'\mathrm{I}\,(S,\underline{O}_S)^{*}',r'\mathrm{I}\,(S,\underline{O}_S)^{\hand{*}}','The repeated unit-group star is also handwritten.'),
(25,r'au\xout{x}',r'au\xout{\unsure{t|x}}','The small overprinted final character has a t-like stem/crossbar as well as x-like traces; its underlying letter is uncertain.'),
(26,r"g\colon P \to P'",r"g\colon P \hand{\to} P'",'The arrow in the description of g is handwritten.'),
(28,r'\hand{$|$}',r'\hand{/}','The separator is a short slanting pen stroke, not an upright vertical bar.'),
(32,r"\underline{E}' \to \underline{M}",r"\underline{E}' \hand{\to} \underline{M}",'The degree-zero quotient arrow is handwritten.'),
(32,r'\inserted{\unsure{surjectifs} i.e. partout non nuls}',r'\inserted{\uline{surjectifs} i.e. partout non nuls,}','The handwritten word surjectifs is legible and underlined; the addition ends with a visible handwritten comma.'),
(33,r"g\colon P \to P'",r"g\colon P \hand{\to} P'",'The final g arrow is handwritten.'),
(35,r'\inserted{S-}',r'\inserted[typed]{S-}','The S and hyphen have typewriter shapes; only their placement curve is pen.'),
(35,r'\uline{morphismes de  degré} 0',r'\uline{morphismes de  degré 0}','The underline continues beneath the0 in the image.'),
(35,r'\uline{sont les morphis-}%',r'\uline{sont les morphis-}\margin{\ensuremath{\backslash}}%','The single long diagonal extends through the last line to the bottom edge; record the graphic with no imposed deletion scope.')
],[
(5,'Foliation','6 above;103 below','confirmed','Both handwritten numbers read directly.'),
(6,'NOTES: long diagonal','Continuous down-right pen line','retained_uncertain','Its function is not securely a whole-page deletion; text stays available.'),
(12,'NOTES: degree hypothesis insertion','Typed et P est à fibres de dimension, with pen comparison','confirmed','The overtyped dimension is readable; the connector attaches after the degree-n clause.'),
(16,'Projection-formula display','All f-star positions, both tensor signs, underlined Sym and superscript n','confirmed','Every symbol compared; no mathematical changes made.'),
(24,'Unit-group notation','Capital I in both occurrences','confirmed','The printed I is retained without replacing it by another alphabet or function symbol.'),
(26,'Line ending','automor followed by phismes on the next line, with no visible hyphen','confirmed','No continuation hyphen is supplied.'),
(29,'Isomorphism at end of NB','Handwritten right arrow, tilde and f subscript star','confirmed','All three marked symbols and the closing parenthesis read directly.'),
(31,'Numbered case','Handwritten1)','confirmed','Both numeral and parenthesis checked.'),
(32,'NOTES: deleted phrase and replacement','partout non nuls crossed by pen; surjectifs underlined in replacement','confirmed','The deletion and insertion are separate visible layers; both are preserved.'),
(35,'Final underlines','morphismes de degré0;de;dans;sont les morphis-','confirmed','Each underlined interval checked against the scan.')
],'Both full images read and all margins inspected. Enlarged associated-word, S/g overprint, P-index and handwritten surjectivity addition compared. Every morphism arrow, star noted in NOTES, underline and local cancellation was checked; diagonal function remains unresolved.')
finish_reviewed(104,[
(8,r'\unsure{partout surjec}',r'partout surjec','The underlying cancelled phrase and abbreviated ending are readable beneath the x marks.'),
(8,r"\underline{E}'\to \underline{E}",r"\underline{E}'\hand{\to} \underline{E}",'The first quotient arrow is handwritten.'),
(9,r'\unsure{$g$}',r'\unsure{$g$|$f$}','The letter is overtyped with g/f-like traces; retain both.'),
(9,r"$P\to P'$",r"$P\hand{\to} P'$",'The arrow beside the overtyped g is handwritten.'),
(10,r'P(\underline{E})\xrightarrow{\sim}',r'P(\underline{E})\hand{\xrightarrow{\sim}}','The first composition arrow and tilde are handwritten.'),
(10,r"\underline{M})\to P(\underline{E}')",r"\underline{M})\hand{\to} P(\underline{E}')",'The second composition arrow is handwritten.'),
(12,r"\underline{E}'\to\underline{E}",r"\underline{E}'\hand{\to}\underline{E}",'The epimorphism arrow is handwritten.'),
(14,r"g:P\to P'",r"g:P\hand{\to} P'",'The degree-one g arrow is handwritten.'),
(19,r"\inserted{\unsure{définis par} $\underline{E}$, $\underline{E}'$ \unsure{loc. libres de type fini},}",r"\inserted{définis \unsure{pr|par} $\underline{E}$, $\underline{E}'$ loc. libres de type fini.}",'The enlarged addition clearly gives définis and loc. libres de type fini, ending in a point; the short preposition looks pr with par still possible.'),
(19,r'S-isomorphisme $g$:',r'S-isomorphisme $\unsure{g|f}$:','The theorem’s g has the same crowded typewriter overprint as the earlier occurrence.'),
(19,r"$P\xrightarrow{\sim}P'$",r"$P\hand{\xrightarrow{\sim}}P'$",'The theorem’s isomorphism arrow and tilde are handwritten.'),
(20,r'P(\underline{E})\xrightarrow{\sim}',r'P(\underline{E})\hand{\xrightarrow{\sim}}','The repeated first composition arrow and tilde are handwritten.'),
(20,r"\underline{M})\to \underline{P}",r"\underline{M})\hand{\to} \underline{P}",'The second composition arrow is handwritten; the target P is visibly underlined.'),
(20,r'\inserted{$\underline{M}$ est un Module inversible sur S,}',r'\inserted[typed]{$\underline{M}$ est un Module inversible sur S,}','The whole interlinear sentence is typewritten; the attachment curve is pen.'),
(22,r"E'\xrightarrow{\sim}",r"E'\hand{\xrightarrow{\sim}}",'The u arrow and tilde are handwritten; the initial E-prime has no underline and is retained so.'),
(22,r'fibres de \unsure{P}',r'fibres de \unsure{P|p}','The overprinted capital has a lower p-like stem as well as P; neither layer is suppressed.'),
(23,r'dim $\geq 1$',r'dim $\hand{\geq} 1$','The fibre-dimension comparison is handwritten.'),
(28,r'$P\geq 1$.',r'$P\hand{\geq} 1$.','The comparison inside the typed insertion is handwritten.'),
(30,r'comm\xout{ex}e',r'comm\unsure{e|a}\xout{\unsure{e|x}}','The enlargement shows two overprinted positions after comm: a live e/a-like position and a final x-cancelled e/x-like position. No additional final live e appears after the cancellation.'),
(31,r'\underline{O}_{\unsure{P}}',r'\underline{O}_{\unsure{P|E}}','The subscript includes P/E-like superimposed traces; both remain explicit.'),
(31,r"$P\to P'$",r"$P\hand{\to} P'$",'The proof’s g arrow is handwritten.'),
(35,r"g:P\to P'",r"g:P\hand{\to} P'",'The corollary’s arrow is handwritten.'),
(36,r's\in S',r's\hand{\in} S','The membership sign is handwritten.'),
(37,r"\underline{E}|U \simeq E'|U",r"\underline{E}\hand{|}U \hand{\simeq} E'\hand{|}U",'Both restriction bars and the central isomorphism sign are handwritten; no arrowhead is supplied where the lower stroke is plain.')
],[
(5,'Foliation','7 above;104 below','confirmed','Both numbers read directly.'),
(7,'Opening underlines and case number','mes;constants underlined;2) typed','confirmed','The continuation from103 and case number are read as printed.'),
(11,'Spelling and spacing','d euxième;la premier;can de ChapII','confirmed','These source forms are visible and retained.'),
(19,'NOTES: first insertion','Handwritten defining-module qualification','retained_uncertain','All words are now readable except the abbreviated preposition pr/par.'),
(20,'NOTES: underlined target P','Target P in the theorem composition has a short underline','confirmed','The underlining is visible in both image parts.'),
(21,'NOTES: deuxième/dauxième','Overprinted first vowel','retained_uncertain','Both stated readings remain compatible with the ink.'),
(21,'Cancelled canonique','canonique under typewriter x cancellation','confirmed','All underlying letters remain legible.'),
(28,'NOTES: et bien sur insertion','Typed sentence after corps, with handwritten comparison and connector','confirmed','The insertion point and every word checked; sur remains unaccented as printed.'),
(32,'Clipped word','local followed by a partial edge trace','confirmed','The supplied comment records the cut; no unseen e is supplied.'),
(35,'Handwritten S-','S-hyphen inserted before isomorphisme','confirmed','Both characters and the placement mark checked.'),
(37,'Final alphabet and continuation','Underlined E, plain E-prime, mod mult par un élément','confirmed','The differing underlines and the complete last line are retained.')
],'Both full images and all margins read. Enlarged handwritten hypothesis and comm-word overprint compared. Every arrow, inequality, subscript, restriction bar, underline, cancellation and insertion layer was checked; unresolved overtyping remains marked.')
finish_reviewed(105,[
(7,r'\Gamma(U,\underline{O}_U)^*',r'\Gamma(U,\underline{O}_U)^{\hand{*}}','The first raised unit-group star is handwritten.'),
(13,r's $\in$ S',r's $\hand{\in}$ S','The membership sign is a pen addition.'),
(14,r'\underline{E}|U',r'\underline{E}\hand{|}U','The restriction bar is handwritten.'),
(15,r'\Gamma(U,\underline{O}_U)^*',r'\Gamma(U,\underline{O}_U)^{\hand{*}}','The second raised star is handwritten.'),
(18,r"\margin{le faire ! c'est",r"\margin{\uline{le faire} ! \unsure{C|c}'est",'The margin instruction le faire is underlined; the following initial has an enlarged C/c form that remains uncertain.'),
(18,r'\unsure{$P(\underline{E}\otimes\underline{E}^{\vee})$|$P(\underline{E}\otimes\underline{E})$}',r'\unsure{$P(\underline{E}^{\vee}\otimes\underline{E})$|$P(\underline{E}\otimes\underline{E})$}','The small V-like mark is above the first E, not the second. Its interpretation as a dual accent remains uncertain, so both marked/unmarked readings remain.'),
(18,r'défini par la non annulation',r'défini \unsure{pr|par} la non annulation','The pen preposition most directly resembles pr; a compressed par remains possible and is not expanded silently.'),
(18,r"``déterminant'' ---}",r"``déterminant'' - - - -}",'The margin ends in four separated short pen dashes, rather than one continuous long dash.'),
(19,r'\unsure{préschéma}',r'p\over{r}{\unsure{r|e}}éschéma','The surrounding typed letters are clear. A thick pen retouch overlays the r position with r/e-like loops; the doubt is localized to that overwritten character.'),
(20,r'\inserted{pré}',r'\inserted[typed]{pré}','The first interlinear pré has typewriter serifs and a pen placement curve.'),
(22,r'\inserted{pré}',r'\inserted[typed]{pré}','The second pré is also typed above the line.'),
(24,r'\underline{E}\simeq\underline{O}',r'\underline{E}\hand{\simeq}\underline{O}','The isomorphism sign is handwritten.'),
(26,r'S\to\mathrm{Spec}',r'S\hand{\to}\mathrm{Spec}','The base-change arrow is handwritten.'),
(26,r'\unsure{du}',r'du','Both underlying letters can be read through the typewriter cancellation.'),
(26,r'\unsure{e}',r'é','The cancelled final letter has a visible acute accent; it is é.'),
(27,r'\unsure{\over{p}{P}}',r'\unsure{P|p}','The capital/lowercase forms are superimposed typewriter impressions with serifs, not a securely handwritten replacement. Both case readings remain explicit.')
],[
(5,'Foliation','8 above;105 below','confirmed','Both handwritten numbers read directly; complete lower blank region inspected.'),
(13,'vosinage','Typed vosinage','confirmed','The missing second i is visible in the page’s spelling and is retained.'),
(17,'NOTES: circled phrase','Oval surrounds on déduit peut déduire facilement','confirmed','The oval emphasizes the wording; the only local typewriter deletion is déduit.'),
(18,'NOTES: full marginal note','Instruction, open-subscheme formula, determinant condition and four dashes','retained_uncertain','The entire diagonal note was read in the original and rotated enlargement. Only capital case, dual-mark presence and the short preposition remain doubtful.'),
(19,'NOTES: préschéma retouch','Pen ink over the r position','retained_uncertain','The looped overwritten letter is not securely identifiable as a single replacement character.'),
(21,'NOTES: linéaire mark','Small isolated spot below the a region','confirmed','It has no secure letter, accent or cancellation shape; the word remains linéaire.'),
(22,'Cancelled old terminology','classiquement le (préschéma','confirmed','The full typed cancellation and its opening parenthesis read directly.'),
(24,'NOTES: notation addition','et se note GP(E) typed; comma and attachment curve handwritten','confirmed','Both writing layers and the attachment before Lorsque checked.'),
(27,'Underlining','Groupe Projectif underlined once;absolu twice','confirmed','All three underline strokes are visible and retained.'),
(27,'Section ending','End of1.9 followed by blank lower page','confirmed','No further text or margin note appears below the final sentence apart from foliation.')
],'Both full image parts and every margin inspected. The entire handwritten side note was enlarged and rotated for reading; the location of its possible dual accent was corrected. The lower blank area was fully inspected. Every insertion, overwrite, cancellation, underline and doubt in NOTES has an explicit decision.')
finish_reviewed(106,[
(11,r'rang $\geqslant$ 2',r'rang $\hand{\geqslant}$ 2','Both the angle and lower bar have free pen strokes; the adjacent2 is typed.'),
(14,r'section $\phi$',r'section $\hand{\phi}$','The section symbol is filled in by hand.'),
(20,r'\simeq',r'\hand{\simeq}','The first isomorphism sign is handwritten.'),
(20,r'\underline{O}_P(n)) \simeq',r'\underline{O}_P(\unsure{n|m})) \hand{\simeq}','The twist letter is overtyped with n/m-like traces; the second isomorphism sign is handwritten.'),
(21,r'\xout{de} $\phi$',r'\xout{de} $\hand{\phi}$','The phi after the cancelled de is handwritten.'),
(23,r'que $\phi$ est',r'que $\hand{\phi}$ est','The transversality-test phi is handwritten.'),
(24,r'$\neq$0',r'$\hand{\neq}$0','The inequality sign is a pen addition.'),
(24,r's$\in$S',r's$\hand{\in}$S','The membership sign is handwritten.'),
(25,r'\hand{\unsure{ss}}',r'\hand{ss}','The two small handwritten s characters are readable; the preceding s is typed.'),
(26,r'\check{\underline{M}}',r'\overset{\hand{\vee}}{\underline{M}}','The dual accent above typed underlined M is handwritten.'),
(26,r'\longrightarrow \underline{Sym}',r'\hand{\longrightarrow} \underline{Sym}','The universally-injective-map arrow is handwritten.'),
(29,r'\longrightarrow \underline{M}',r'\hand{\longrightarrow} \underline{M}','The transposed-map arrow is handwritten.'),
(34,r'\inserted{décomposition}',r'\inserted[typed]{décomposition}','The replacement word has typewriter serifs and fixed spacing; the surrounding cancellation is pen.'),
(34,r'\deleted{partition}',r'\xout{partition}','The local cancellation over partition consists of typewriter x impressions, within the larger pen-deleted passage.'),
(35,r'\deleted{(n N) tel}',r'\deleted{\unsure{(n N)|n N)} tel}','The leftmost curved/vertical mark belongs to the enclosing pen line; an underlying opening parenthesis cannot be established securely. No membership sign is supplied.')
],[
(5,'Foliation','9 above;106 below','confirmed','Both handwritten numbers read directly.'),
(11,'Section number2.1','Handwritten2.1.','confirmed','Numerals and points checked.'),
(12,'NOTES: overtyped words','déterminer and Div(P/S)','confirmed','Every letter remains readable through the typewriter overprinting.'),
(13,'Nonnegative-divisor insertion','Handwritten greater-or-equal0','confirmed','Both signs and the attachment after relatifs checked.'),
(20,'NOTES: stars and display label','Two pen subscript stars and handwritten(*)','confirmed','Each marked star and both parentheses inspected.'),
(21,'Module letter','Section de E as printed','confirmed','The letter is underlined E in the scan; it is not replaced by L from the preceding sentence.'),
(22,'NOTES: inserted phi','Pen phi above the beginning de M tensor Sym','confirmed','Its position completes the preceding d’une section phrase.'),
(26,'Alphabets in symmetric powers','Un-underlined E in the first map; underlined E in its transpose','confirmed','The difference is visible and retained.'),
(33,'Divisor formula','O subscript X, with underlined D in parentheses','confirmed','The printed X is retained without changing it to P.'),
(33,'NOTES: deleted ending','From Ainsi through tel, with local typed partition cancellation and typed decomposition insertion','confirmed','The horizontal pen strokes cross the words and enclose all three lines; the entire local deletion is visible.'),
(35,'NOTES: n and N','No secure membership sign between n and N','confirmed','Only the enclosing cancellation stroke traverses that gap.')
],'Both complete scan parts and all margins read. The two displayed dual maps, every phi, comparison, index and alphabet were checked. The bottom local deletion and both its earlier typing revisions were inspected separately; no missing membership sign is inferred.')
finish_reviewed(107,[
(7,r'D $\geq 0$',r'D $\hand{\geq} 0$','The angle and lower stroke of the first comparison are handwritten.'),
(7,r'$n \geq 0$',r'$n \hand{\geq} 0$','The second comparison is handwritten.'),
(7,r'n \unsure{<} 0',r'n \hand{\unsure{<|\leq}} 0','The sign is a heavily blotted pen angle with an indistinct lower stroke; strict and weak readings remain possible from the ink.'),
(9,r'$\geq 0$',r'$\hand{\geq} 0$','The next nonnegativity comparison is handwritten.'),
(10,r'n \in \underline{N}',r'n \hand{\in} \underline{N}','The first membership sign is handwritten.'),
(10,r'n \in \underline{N}',r'n \hand{\in} \underline{N}','The second membership sign is handwritten.'),
(10,r'\underline{L}|P|S_n',r'\underline{L}\hand{|}P\hand{|}S_n','Both restriction bars are pen additions; the printed nesting is preserved.'),
(12,r'tifs $\geq 0$',r'tifs $\hand{\geq} 0$','The first comparison on this line is handwritten.'),
(12,r'relatifs $\geq 0$',r'relatifs $\hand{\geq} 0$','The second comparison on this line is handwritten.'),
(17,r'\mathrm{Div}^{n}(\unsure{P}/S)',r'\mathrm{Div}^{\unsure{n|m}}(\unsure{P|E|R}/S)','The superscript and argument are both typewriter overprints; n/m and P/E/R-like traces remain visible.'),
(17,r'relatifs $\geq 0$',r'relatifs $\hand{\geq} 0$','The proposition’s nonnegativity comparison is handwritten.'),
(22,r'\unsure{devine}',r'\unsure{devine|devien}','The last two letter positions are overtyped with e/n shapes in both orders; no confident order is imposed.'),
(27,r'\xout{xx}',r'\deleted{\xout{\illegible{1}}}','The short group has typewriter x impressions with additional pen hatching/loops; its underlying word remains unreadable.'),
(27,r'\mathrm{Div}^{+}_{\unsure{P}/S}',r'\mathrm{Div}^{+}_{\unsure{P|E|R}/S}','The subscript capital is overtyped with the same P/E/R-like remnants.'),
(31,r'\underline{\mathrm{Div}}^{+}_{\unsure{P}/S}',r'\underline{\mathrm{Div}}^{+}_{\unsure{P|E|R}/S}','The second subscript capital is also overtyped and remains uncertain.'),
(31,r'\xout{xxxxx}',r'\xout{entre}','The underlying e-n-t-r-e can be read beneath the row of x impressions.'),
(32,r'\underline{\mathrm{Sym}}^{n}_{P/S}(\underline{E})',r'\underline{\mathrm{Sym}}^{n}_{\underline{P}/S}\unsure{\xout{(}|I^{\hand{*}}_{\hand{*}}}\underline{E})','The P in the subscript has a separate short underline. Before E is an overprinted parenthesis/I-like group with upper and lower crosses; both ink-based readings are retained instead of silently supplying an ordinary opening parenthesis.'),
(32,r'n \in \underline{N}',r'n \hand{\in} \underline{N}','The final n-membership sign is handwritten.'),
(33,r'i \in I',r'i \hand{\in} I','The membership sign in the family index is handwritten.')
],[
(5,'Foliation','10 above;107 below','confirmed','Both handwritten numbers read directly.'),
(7,'NOTES: on avait/n’avait','Small handwritten insertion above si n','retained_uncertain','The first short sequence remains compatible with both source readings.'),
(8,'NOTES: Grâce à','Overtyped G/A region and faint à','confirmed','The completed reading Grâce à is supported; no separate cancelled letter is asserted.'),
(9,'Decomposition wording','décomposition de D en somme disjointe d’ouverts S_n','confirmed','The source says de D, not de S; this is retained. Enlarged S-index shows n clearly.'),
(11,'Cancelled end of relatifs','rela followed by two x impressions at line end','confirmed','No continuation hyphen is supplied beyond the visible marks.'),
(13,'NOTES: tèxte and margin strokes','Vowel with stray accent-like trace; two slanting near-vertical margin strokes','retained_uncertain','The word candidates remain; both margin strokes are present.'),
(19,'NOTES: dual accents','All six V-shaped dual accents are handwritten','confirmed','Each was inspected in its own formula, including the dual M.'),
(22,'Reference(*)','Literal parenthesized star','confirmed','It refers back to the display on106 as printed.'),
(32,'NOTES: Sym subscript and overprint','P/S remains in the source formula; following group is crowded','retained_uncertain','The unusual subscript is retained. Its underline and the following crossed group are now explicitly recorded.'),
(33,'Multiprojective opening','Finite family(E_i), P_i and fibre product P','confirmed','All i indices, the plural Modules and the start of2.5 read directly.'),
(36,'NOTES: clipped endings','correspondan;loc;représentable;inv and final continuation','confirmed','Only visible text is retained; no missing endings or hyphens are supplied.')
],'Both full image parts read; enlarged S-index, devine overprint, short cancellation and final Sym formula inspected. Every dual accent, inequality, membership, index, reference and margin stroke was compared. Printed deD and the extra Sym subscript remain unaltered as mathematical statements.')
finish_reviewed(108,[
(7,r'\inserted{inversible}',r'\inserted[typed]{inversible}','The inserted word is typewritten; its curved attachment is pen.'),
(8,r'i \in I',r'i \hand{\in} I','The membership sign in the first index set is handwritten.'),
(8,r'\in \underline{Z}^I',r'\hand{\in} \underline{Z}^I','The membership before Z-to-I is handwritten.'),
(13,r'rang $\geq$2',r'rang $\hand{\geq}$2','The rank comparison is handwritten.'),
(15,r'\underline{n} \in \underline{Z}^I',r'\underline{n} \hand{\in} \underline{Z}^I','The membership after the open-set notation is handwritten.'),
(16,r'\underline{L}|P|S_{\underline{n}}',r'\underline{L}\hand{|}P\hand{|}S_{\underline{n}}','Both restriction bars after L are handwritten.'),
(17,r'\underline{O}_P(\underline{n})|P|S_n',r'\underline{O}_P(\underline{n})\hand{|}P\hand{|}S_n','The two restriction bars are pen strokes; the final n lacks the underline used elsewhere and is retained as printed.'),
(22,r'\underline{n} = (n_i)_{i \in I} \in',r'\underline{n} = (\unsure{h|n}_i)_{i \hand{\in} I} \hand{\in}','The component letter is overtyped with h/n-like traces. Both membership signs in this multidegree line are handwritten.'),
(22,r'\underline{Z}\hand{\unsure{$^{*}$}}',r'\underline{Z}^{\hand{\unsure{*|x|z}}}','The small raised pen mark has crossed/zigzag strokes, compatible with star, x or z; its identity remains uncertain.'),
(25,r'$P_i$\xout{x}',r'$P_i$\xout{\illegible{1}}','The isolated x impression cancels a small underlying character that cannot be recovered securely; it is not taken as literal x content.'),
(28,r'\longrightarrow P',r'\hand{\longrightarrow} P','The section-induced morphism arrow is handwritten.'),
(30,r'h_i^{*}',r'h_i^{\hand{*}}','The pullback star is handwritten.'),
(35,r"d'un fibré multiprojectif dans un autre",r"d'un fibré m\over{y}{\unsure{u|y}}ltiprojectif dans un autre",'The first occurrence has a typed y-like descender with a broad pen retouch at its upper fork; the replacement u/y shape remains doubtful.')
],[
(5,'Foliation','11 above;108 below','confirmed','Both handwritten numbers read directly.'),
(9,'Cancelled désignerons','désignerons under typewriter x cancellation','confirmed','Every underlying letter is readable.'),
(10,'Tensor display','Both tensor products, all i indices and O_S under the second tensor sign','confirmed','The displayed base-index placement is retained exactly.'),
(14,'NOTES: le overprint','l has an additional typewriter impression','confirmed','The completed reading le is supported by the surviving strokes.'),
(16,'NOTES: cancelled quantifier','pour tout underlined n in underlined Z-to-I, un','confirmed','All words and symbols of the typewriter-cancelled phrase were compared.'),
(17,'Statement formula','O_P(n) restriction without a displayed M factor','confirmed','The formula visibly has no M tensor factor here; none is supplied.'),
(20,'Number2.7','Handwritten2.7 with a placement curve','confirmed','Digits, points and attachment read directly.'),
(21,'NOTES: inversible overtyping','Crowded s/i region in inversible','confirmed','The complete word is readable; no extra character is separately secure.'),
(22,'NOTES: raised mark','Cross/zigzag above Z beside the opening parenthesis','retained_uncertain','Enlargement does not settle its identity; its raised position is retained.'),
(25,'Cancelled section notation','Extra small group after P_i and cancelled h_i before display','confirmed','The local typewriter cancellations are visible; h_i beneath its cancellation is readable.'),
(30,'NOTES: degree formula argument','Underlined L/E overprint','retained_uncertain','Both source alternatives remain supported by the superimposed strokes.'),
(31,'Author’s qualification','n_i described as locally constant maps from S to Z','confirmed','All words and both indices in the qualification read directly.'),
(36,'Lower continuation','Determination of morphisms and automorphisms; Plus intéressant pour nous,','confirmed','Every final line and the lower margin inspected.')
],'Both complete images and all margins read. Enlarged restriction index, multidegree overprint and retouched multiprojectif spelling inspected. The absent M factor and the un-underlined final n in2.6 are retained; no mathematical repair is made.')
finish_reviewed(109,[
(7,r'résult\unsure{ant}',r'résult \unsure{ant|aht}','The enlargement shows a genuine blank after résult, followed by crowded ant/aht-like overprinting; retain the spacing and doubt.'),
(8,r'détermination des diviseurs',r'déter\over{m}{m}ination des diviseurs','A small pen stroke reinforces the top of the typed m; the word itself remains readable.'),
(8,r'$\geqslant 0$',r'$\hand{\geqslant} 0$','The nonnegativity sign is handwritten.'),
(9,r'2.8.',r'\inserted[typed]{2.8.}','The number is placed above the paragraph and joined to Si by a curved pen insertion mark.'),
(13,r'\underline{n}\in\underline{N}^{I}',r'\underline{n}\hand{\in}\underline{\unsure{N|M}}^{I}','The membership sign is handwritten; the underlined capital has N/M-like overprint traces.'),
(15,r'\simeq',r'\hand{\simeq}','The isomorphism sign in the displayed formula is handwritten.'),
(16,r'\xout{\illegible{3}}',r'\xout{ou à Künneth}','All three underlying words, including the umlaut and final th, are readable in the enlarged cancellation.'),
(17,r'f_*(\underline{D})',r'f_{\hand{*}}(\underline{D})','The first direct-image star is handwritten.'),
(17,r'f_*(\underline{O}_P',r'f_{\hand{*}}(\underline{O}_P','The second direct-image star is handwritten.'),
(17,r'\bigotimes_i',r'\hand{\bigotimes}_i','The large tensor-product circle and cross are freehand; the i index is typed.'),
(20,r'on a\xout{x} une',r'on a\xout{\illegible{1}} une','The extra x impression cancels a short underlying character that cannot be securely recovered.'),
(23,r'de $\bigotimes_i',r'de $\hand{\bigotimes}_i','The proposition’s large tensor-product sign is hand-drawn.'),
(29,r'projectif $P(\bigotimes_i',r'projectif $P(\hand{\bigotimes}_i','The representing-bundle tensor-product sign is hand-drawn.'),
(30,r'\underline{n}\in\underline{N}^{I}',r'\underline{n}\hand{\in}\underline{N}^{I}','The final membership sign is handwritten.'),
(36,r'Pour ceci',r'P$_o$ur ceci','The o of Pour is visibly lowered below the baseline; preserve that placement.'),
(37,r'X \to S',r'X \hand{\to} S','The proper-flat morphism arrow is handwritten.')
],[
(5,'Foliation','12 above;109 below','confirmed','Both handwritten numbers read directly.'),
(7,'Reference to resultant/discriminant','par.25','confirmed','The number25 is clearly printed and is retained.'),
(10,'NOTES: overtyped words and clipped edges','définit;étan;ramené','confirmed','The legible portions are read as printed; no clipped final letters are supplied.'),
(15,'First displayed sheaf','L=O_X(D)','confirmed','The subscript is X in the source; it is not changed to P.'),
(17,'Second displayed direct image','f-star of underlined D','confirmed','The operand visibly reads D rather than L; no mathematical substitution is made.'),
(18,'Printed spelling','Proéédant maintenaht;reppaler','confirmed','All three unusual forms read directly and retained.'),
(20,'Abbreviations','corr biun can;can isomorphe;can représentable;can repr','confirmed','No abbreviation is expanded in the French source.'),
(23,'NOTES: dual accents','Two handwritten V-shaped exponents after E_i','confirmed','Each accent and its i subscript inspected.'),
(30,'NOTES: derniers overtyping','rni/mmi alternatives in the middle of the word','retained_uncertain','The crowded letter sequence does not settle the supplied candidates.'),
(34,'Picard-scheme notation','Underlined Pic with P/S subscript and four points','confirmed','Alphabet, subscript and punctuation checked.'),
(38,'NOTES: final et underline','One horizontal underline beneath et','confirmed','The stroke lies directly under both letters; the underlining is retained.')
],'Both full images and all margins read. Enlarged resultant spacing/overprint and Künneth cancellation inspected. Every tensor sign, direct-image star, dual accent, multidegree index and reference was checked. The printed O_X(D), f-star(D), misspellings and lowered o are preserved.')
finish_reviewed(110,[
(11,r'f_{*}(\underline{O}_X)\overset{\sim}{\longleftarrow}',r'f_{\hand{*}}(\underline{O}_X)\overset{\hand{\sim}}{\hand{\longleftarrow}}','The subscript star, tilde and left-directed arrow are pen strokes.'),
(14,r'\underline{M}\simeq f_{*}',r'\underline{M}\hand{\simeq} f_{\hand{*}}','The displayed isomorphism sign and direct-image star are handwritten.'),
(16,r'\inserted[typed]{\xout{$\underline{\phi}$x}}',r'\inserted[typed]{\xout{\unsure{$\underline{\phi}$|ø}\illegible{1}}}','The interlinear group is typed and cancelled; its slashed underlined circle does not securely distinguish phi from ø, and the following underlying character is obscured by x cancellation.'),
(17,r"d'une section\xout{s} $\phi$",r"d'une section\xout{s} $\hand{\phi}$",'The main phi has a continuous slanting pen stem and oval, unlike the separate typed interlinear group.'),
(18,r'\xout{f$_*$($\underline{L}\otimes\underline{M}$)xxxxf$_*$($\underline{L}$)$\otimes$Mxx}',r'\xout{\unsure{f$_*$}($\underline{L}\otimes\underline{M}$)\illegible{1}\unsure{f$_*$}($\underline{L}$)$\otimes$M\illegible{1}}','The cancelled formula retains readable f, L, M and tensor signs; x impressions obscure the relation and final group, and neither star is separately secure under cancellation.'),
(18,r"qu'il \xout{xixx}",r"qu'il \xout{\illegible{1}}",'The four x impressions do not yield a secure underlying word; retain illegibility rather than literal cancellation characters.'),
(22,r'f_{*}(\underline{L}\otimes\underline{G})\simeq',r'f_{\hand{*}}(\underline{L}\otimes\underline{G})\hand{\simeq}','The direct-image star and isomorphism sign in this formula are hand-drawn.'),
(24,r'pro\xout{x}cédé brévété',r'pro\xout{é}cédé bréveté','The enlarged scan shows an accented é beneath the local x cancellation, and the middle e of bréveté has no accent.'),
(25,r'changement de\xout{x} base',r'changement de\xout{\illegible{1}} base','The small cancelled character after de remains unreadable.'),
(26,r'la donnée de $\phi$ équivaut à \xout{xx}',r'la donnéé de $\hand{\phi}$ équivaut à \xout{\unsure{un}}','Both final e letters carry visible acute accents; phi is handwritten. The cancelled short word is compatible with un but remains marked uncertain.'),
(27,r'\psi : Q \longrightarrow M',r'\hand{\psi} : Q \hand{\longrightarrow} M','The psi-like glyph and right-directed arrow are pen strokes.'),
(28,r'pour que $\phi$',r'pour que $\hand{\phi}$','This phi is handwritten.'),
(29,r'est que $\phi$',r'est que $\hand{\phi}$','This phi is handwritten.'),
(30,r'$\neq 0$ \xout{xix}',r'$\hand{\neq} 0$ \xout{\illegible{1}}','The inequality sign is pen; the x-cancelled word immediately after zero remains unreadable.'),
(30,r'termes de $\psi$',r'termes de $\hand{\psi}$','The first psi on this line is handwritten.'),
(31,r'$\psi$ est surjectif, donc que \xout{Mxxxx} $\psi$',r'$\hand{\psi}$ est surjectif, donc que \xout{M\illegible{1}} $\hand{\psi}$','Both psi glyphs are handwritten. Only the first M of the cancelled group is securely legible.'),
(32,r'S. On obtient',r'S. O$\unsure{\overset{\illegible{1}}{n}_{\unsure{n|\sim}}|n}$ obtient','A small unreadable raised group and an n/tilde-like lower impression sit above and below the n of On; the crowded ink is explicitly retained without assigning an intended correction.'),
(34,r'2.1\unsure{1}',r'2.1\unsure{\over{1}{2}|1}','The last typed 1 has a curved pen stroke above and a slanting terminal resembling 2; the correction is recorded but remains uncertain.'),
(34,r'\xout{xxx X/S}',r'\xout{sur X/S}','The underlying s-u-r and X/S are readable beneath the x impressions.'),
(36,r'tel\unsure{\xout{s}|s}',r'tel\unsure{\hand{s}|\deleted{s}}','The last s position carries a thick slanting pen shape; an added s and a pen-cancelled s cannot be securely distinguished, so uncertainty is retained.')
],[
(5,'Foliation','13 above;110 below','confirmed','Both handwritten numbers read directly.'),
(7,'Mathematical wording','sous-groupe Div^L(X/S) de Div^+(X/S)','confirmed','The printed word sous-groupe and both exponents are retained without substituting terminology.'),
(9,'Tensor base and Module','L tensor over O_X M; M inv sur S','confirmed','The X subscript and the base S are both printed as recorded; no repair is made.'),
(17,'NOTES: phi and psi layer','Main phi and psi glyphs are handwritten; the cancelled interlinear symbol is typed','corrected_from_scan','Continuous thin pen curves and long slanted stems distinguish the main symbols from the monospaced overstruck interlinear group.'),
(20,'NOTES: variable letter','Underlined N/G overprint','retained_uncertain','The enlarged letter retains conflicting vertical, diagonal and rounded traces; neither candidate is removed.'),
(22,'Formula alphabets','Underlined Q but plain G in Hom(Q,G)','confirmed','The visible difference in underlining is preserved.'),
(24,'Reference and argument','Chap III par7; loc noethérien qualification; formation of Q and base change','confirmed','The reference and every word of the parenthetical qualification read directly.'),
(34,'NOTES: proposition correction','Typed2.11 with pen2-like overwrite on last1','retained_uncertain','The source cannot securely decide the intended final numbering from ink alone.'),
(35,'NOTES: overtyped words','positifs, correspondant, changement, transversalement, biunivoque and la','confirmed','The complete recorded words remain legible under their local typewriter overprints.'),
(36,'NOTES: final s','Pen s-shaped stroke at tels','retained_uncertain','The scan does not settle whether the stroke adds or cancels the final letter.')
],'Both complete scan parts and all margins read. Enlarged interlinear symbol, cancelled formula, several lower cancellations, On overprint, variable N/G, proposition number, final s, donnéé and bréveté inspected. Every formula, alphabet, morphism sign and reference checked; no mathematical or grammatical normalization applied.')
finish_reviewed(111,[
(7,r'la sedtion $\phi$',r'la sedtion $\hand{\phi}$','The phi beside sedtion is written with a free pen stem and oval.'),
(7,r'\unsure{$\psi$} : $Q\longrightarrow\underline{M}$',r'$\hand{\psi}$ : $Q\hand{\longrightarrow}\underline{M}$','The first psi is a pen glyph matching the other visible psi forms; the arrow is handwritten and Q is plain.'),
(10,r'\underline{O}_S\xrightarrow{\sim}f_*(\underline{O}_X)',r'\underline{O}_S\overset{\hand{\sim}}{\hand{\longrightarrow}}f_{\hand{*}}(\underline{O}_X)','The tilde, arrow and subscript star are handwritten.'),
(13,r'k(s)\xrightarrow{\sim}',r'k(s)\overset{\hand{\sim}}{\hand{\longrightarrow}}','Both strokes of the isomorphism arrow are handwritten.'),
(14,r's\in S',r's\hand{\in} S','The membership glyph is handwritten.'),
(15,r"S'\rightarrow S",r"S'\hand{\rightarrow} S",'The base-change arrow is handwritten.'),
(16,r'X\longrightarrow S',r'X\hand{\longrightarrow} S','The structural-morphism arrow is handwritten.'),
(16,r'\xout{plat}',r'\deleted{plat}','The cancellation consists of looping diagonal pen strokes rather than a uniform row of typed x characters.'),
(19,r'\xout{\unsure{Ce foncteur}}',r'\xout{Ce foncteur}','Both underlying words are readable beneath the typed cancellation.'),
(21,r'fibré projectif $\underline{P}(\underline{Q})$',r'fibré projectif $\underline{P}(\underline{\unsure{Q|A}})$','The argument has an oval Q impression with A-like interior strokes from overtyping; both candidates are retained.'),
(23,r'\xout{\unsure{fibré}}',r'\xout{schéma}','The enlarged cancellation shows s-c-h-é-m-a, including h ascender and accented é.'),
(26,r'Pour le cas',r'P$\unsure{\underset{\cap}{o}|o}$ur le cas','A second curved impression is visible immediately below the o of Pour; its function remains uncertain and its position is recorded.'),
(26,r'un monomorphisme',r'un \unsure{monomorphisme}','Several middle letters have conflicting typewriter impressions and a descender under the first o; retain the intended-looking word as an uncertain reading.'),
(28,r'\mathrm{Div}^{L}_{X/S}\longrightarrow',r'\mathrm{Div}^{L}_{X/S}\hand{\longrightarrow}','The monomorphism arrow is handwritten.'),
(32,r'une section de $P(\underline{Q})$',r'une section de $P(\underline{\unsure{Q|A}})$','P is visibly plain; the argument repeats the crowded Q/A-like overprint.'),
(33,r"d'où une section $\phi$",r"d'où une section $\hand{\phi}$",'The phi in this sentence is handwritten.'),
(33,r'\inserted{sous-}',r'\inserted[typed]{sous-}','The letters of sous- are monospaced typing; only the curved attachment is pen.'),
(34,r'$\underline{U}$',r'$\unsure{\overline{U}|U}$','The U position has a high horizontal impression rather than a separate lower underline; the presence of an overbar remains uncertain.'),
(34,r'rendre $\phi$',r'rendre $\hand{\phi}$','The final phi is handwritten.'),
(36,r'\unsure{provieht|provient}',r'provieht','The enlarged letter has a full ascender and the bowl of h; the printed spelling is provieht.')
],[
(5,'Foliation','14 above;111 below','confirmed','Both handwritten numbers read directly.'),
(7,'Opening spelling','sedtion','confirmed','The letter after se is visibly d; the spelling is preserved.'),
(10,'NOTES: clipped vrai','vrai at right edge','confirmed','Only these visible letters are retained; a missing final e is not supplied.'),
(13,'Cohomology exponent and label','H raised small o; label(xxx)','confirmed','Both the exponent shape and the three literal x characters in the label are visible.'),
(14,'Cross-references','III7;2.12;Theorem2.13','confirmed','The numbers are read from this page; the uncertain previous-page numbering is not imposed on them.'),
(21,'Representing object','Open retrocompact sub-prescheme of P(Q)','confirmed','The exact qualifiers and both underlines were compared with the scan.'),
(23,'NOTES: typed replacement','fibré above cancelled schéma','corrected_from_scan','The insertion is typed and the underlying cancelled word is legible as schéma.'),
(32,'NOTES: plain P','P in une section de P(Q) has no underline','confirmed','This difference from the other occurrences is retained.'),
(36,'NOTES: provieht','Clear typed h in provieht','corrected_from_scan','Magnification resolves the draft’s h/n doubt in favor of the visible h.'),
(37,'Proof reference','cf par.11 ...','confirmed','The reference, ellipsis and closing parenthesis are retained without completion.'),
(39,'Lower conclusion and margin','Reduction au cas noethérien; otherwise blank lower margin','confirmed','All final text and the full bottom edge were inspected.')
],'Both complete scans and every margin read. Enlarged cancellations, Q overprint, U position, Pour impression, monomorphisme and provieht inspected. Every morphism sign, phi/psi, formula index, underlining and reference compared; the printed spellings and uncertain overprints are preserved.')
finish_reviewed(112,[
(7,r'\hand{3)}',r'\hand{\unsure{3|2})}','The large handwritten section digit has overlapping 2/3-like strokes; its intended value is not imposed from the following pages.'),
(7,r'\unsure{morphismes}','morphismes','All letters of the handwritten title word are readable.'),
(7,r'\unsure{projectifs}','projectifs','The second handwritten title line clearly reads projectifs.'),
(8,r'\deleted{16. Traductions en langage de systèmes linéaires.}',r'\deleted{16. \uline{Traductions en langage de systèmes linéaires.}}','The typed title is both underlined and crossed by a separate horizontal cancellation; 16 lies outside the underline.'),
(11,r'\xout{xxxxxxx}',r'\xout{\unsure{visieurs}}','The underlying sequence resembles visieurs, with visible i-s-i and final s beneath cancellation; the first and middle letters remain doubtful.'),
(12,r'\hand{\unsure{$^{3}$}}',r'\hand{\unsure{$^{3}$|$^{z}$}}','The small pen mark above the typed x has a double-bent 3/z-like shape; both candidates remain possible.'),
(13,r'\hand{(}intersection',r'intersection','The curved stroke joins the interlinear replacement to the baseline; it does not separately form a textual opening parenthesis.'),
(13,r'\xout{xxxxxxxxxxx}',r'\xout{transversale}','The full word transversale is readable beneath the typed x cancellation.'),
(14,r'ou \xout{xxx}',r'ou \xout{\illegible{1}}','The cancelled three-character group does not yield a secure underlying word.'),
(15,r'\hand{(}par rapport',r'par rapport','This curved stroke is the placement connector for loc de prés finie, not a textual parenthesis.'),
(17,r'\inserted{de ses}',r'\inserted[typed]{de ses}','Both inserted words have typewriter letterforms; the attachment curve is handwritten.'),
(25,r'\inserted{\unsure{\S\ n$^{\circ}$2}}',r'\inserted{\unsure{cf|\S}\ n$^{\circ}$2}','The initial pen ligature can be read as cf or a section sign; n, the raised circle and2 are clear.'),
(31,r'$x\in X$',r'$x\hand{\in} X$','The membership sign is handwritten.'),
(31,r"``point fixe'' \xout{pour}pour",r"``\uline{point fixe}'' \unsure{pour|pous}",'Point fixe has a visible underline. The following word occupies one overprinted footprint, with r/s-like final traces; the draft incorrectly duplicated pour as two successive words.'),
(32,r'pr_1^{-1}(x)\subset D',r'pr_1^{-1}(x)\hand{\subset} D','The inclusion sign is a continuous pen curve.'),
(33,r'pr_1(\xout{X}X\times_S T - D)',r'pr_1(\unsure{X}\times_S T - D)','Only one crowded capital position precedes the typed multiplication x; two sequential X characters are not visible. The surviving X reading remains uncertain.'),
(34,r'T\longrightarrow S',r'T\hand{\longrightarrow} S','The arrow to S is handwritten.')
],[
(5,'Foliation','15 above;112 below','confirmed','Both handwritten numbers read directly.'),
(7,'NOTES: heading and box','Boxed Nos3,4; revised handwritten title; unreadable cancelled initial group','confirmed','All title words and the box were inspected; the obscured initial group remains illegible.'),
(10,'NOTES: cancellation scope','Crossed preliminary passage from Soit X through au plus tard dans V','confirmed','Several intersecting diagonal strokes hatch the whole passage and terminate within its boundaries, with further repeated local slashes across the last lines; the block deletion is supported by this pattern.'),
(12,'NOTES: marginal mark','Small pencil r-like trace beside positifs','retained_uncertain','The faint mark remains compatible with r or an incidental stroke.'),
(12,'Parameter in the preliminary definition','paramétrée par S','confirmed','The typescript visibly says S here; it is retained.'),
(13,'Handwritten replacement','un diviseur de Cartier rel. à T, i.e. qui est','confirmed','Every handwritten word, abbreviation and punctuation mark read directly.'),
(15,'Fibre formula','X with nested T,t and s,k(t) indices','confirmed','The exact letters, positions and equality were compared; no missing comma or notation is supplied.'),
(19,'NOTES: contravariant','Extra i cancelled in contravariant','confirmed','The local typed cancellation is visible in addition to the block hatching.'),
(20,'NOTES: absent arrow','f:X followed by space and S','confirmed','The gap contains no separately drawn morphism arrow; none is supplied.'),
(23,'Planned dependency','ChapIII;possible inclusion inIII and at latestV','confirmed','The references and the whole proposed representability discussion were read beneath the crossing strokes.'),
(29,'NOTES: clipped line','sous-enten at right edge','confirmed','The source retains the visible portion and its clipping comment.'),
(32,'Handwritten qualification','ensemblistement','confirmed','The complete word and its insertion point after D are clear.'),
(33,'Fixed-point wording','points non fixes est le complémentaire de pr1(...)','confirmed','The displayed description is kept exactly as printed; no mathematical reversal is made.'),
(36,'Final insertion','Z after ensemble','confirmed','The capital Z and its curved placement marker were read directly.')
],'Both complete image parts and all margins read. Enlarged heading digit, three cancellations, positifs annotation, cf/section-sign note, overprinted pour and X position inspected. The repeated block hatching is retained as deletion, while two insertion connectors are no longer encoded as textual parentheses. All lower definitions, formulas and qualifications checked without normalization.')
finish_reviewed(113,[
(7,r'\xout{\unsure{Parxsymétxiex}}',r'\xout{Par symétrie,}','The underlying words and final comma are readable beneath typed cancellation; the x impressions are not part of the words.'),
(8,r'diviseurs de X-Z paramétrée',r'diviseurs de $\overset{\hand{\unsure{r}}}{X}-Z$ paramétrée','A small r-like pen mark sits above X; its uncertain shape and position are now recorded.'),
(11,r'\inserted{plat}',r'\inserted[typed]{plat}','The inserted plat is typewritten; the curved stroke provides its attachment before loc.'),
(12,r'\inserted{et géom irréd}',r'\inserted[typed]{et géom irréd}','The whole inserted phrase is typed, with a pen attachment after(S1).'),
(13,r'T \longrightarrow X',r'T \hand{\longrightarrow} X','The projection arrow is handwritten.'),
(15,r'\inserted{au point $z \in$ supp D}',r'\inserted[typed]{au point $z \hand{\in}$ supp D}','The insertion is typed apart from its membership glyph and placement curve.'),
(15,r'\xout{\unsure{f=0}}',r'\xout{f=0}','The cancelled f, equality and0 are legible.'),
(15,r'$\phi = 0$',r'$\hand{\phi} = 0$','Phi is handwritten.'),
(16,r'$x\in X$',r'$x\hand{\in} X$','This membership sign is handwritten.'),
(16,r'$s\in S$',r'$s\hand{\in} S$','This membership sign is handwritten.'),
(16,r'\xout{\unsure{identiquement nulle}}',r'\xout{identiquement nulle}','Both cancelled words are readable under the x impressions.'),
(17,r'nilpo\xout{\unsure{n}}tente',r'nilpo\xout{n}tente','The cancelled extra n is legible in the enlarged word.'),
(17,r'D = V(\phi_x)',r'D = V(\hand{\phi}_x)','Phi in V(phi_x) is handwritten; the x index is typed.'),
(17,r'\xout{\unsure{serait}}',r'\xout{serait}','The cancelled word before the typed contiendrait insertion is legible.'),
(20,r'$\phi_x$',r'$\hand{\phi}_x$','The phi before the regularity formula is handwritten.'),
(20,r'\underline{O}_{T_{s\ k(x)}}',r'\underline{O}_{T_{\xout{s}\ k(\unsure{x})}}','The nested s is covered by a typed x cancellation and the x in k(x) is heavily overprinted; those visible layers are preserved.'),
(21,r'\xout{\unsure{un morphisme}}',r'\xout{un morphisme}','Every underlying letter of the cancelled phrase is readable.'),
(22,r'X \longrightarrow \mathrm{Div}_{T/S} \quad ,',r'X \hand{\longrightarrow} \mathrm{Div}_{T/S} \quad \hand{,}','Both the displayed arrow and the small comma are pen marks.'),
(23,r'\hand{D}ans',r'\over{D}{D}ans','The pen D lies over a visible typed D; both layers are retained.'),
(23,r'famille de diviseurs de X peut',r'famille de \unsure{diviseurs} de X peut','An overprint in the middle of diviseurs leaves the exact underlying letter sequence uncertain.'),
(26,r'X - Z \longrightarrow',r'X - Z \hand{\longrightarrow}','The second displayed arrow is handwritten.'),
(27,r'X pa\xout{r} X-T',r'X pa\unsure{r|m} X-T','The last letter position in par has overlapping r/m-like impressions, rather than a securely separate x cancellation.'),
(32,r'\xout{de T/S paramétrée par X est} \deleted{évidemment sans points fixes, et on}',r'\xout{de T/S paramétrée par X }\deleted{\xout{est év}idemment sans points fixes, et on}','Enlargement shows typed x cancellation continuing through év, while the pen line already crosses est; the two cancellation layers overlap.'),
(35,r'\inserted{U}',r'\inserted[typed]{U}','The inserted capital U has typed serifs; the V-shaped attachment is pen.'),
(35,r'D|(U\times_S T)',r'D\hand{|}(U\times_S T)','The restriction bar is handwritten.'),
(36,r'\inserted{tel que son symétrique ${}^{t}D$}',r'\inserted[typed]{tel que son symétrique ${}^{t}D$}','All words and the raised t in this insertion are typed; the enclosing placement curve is handwritten.')
],[
(5,'Foliation','16 above;113 below','confirmed','Both pen folio numbers read directly.'),
(11,'NOTES: loc and insertion curve','loc remains live','confirmed','The line above loc belongs to the plat attachment and does not cancel the letters.'),
(17,'Formula gap','pr1 inverse(x), then D=V(phi_x), with no relation supplied in the gap','confirmed','The visible blank before D is preserved.'),
(17,'NOTES: clipped end','ensemblist with uncertain cancelled terminal e','retained_uncertain','The edge and overstrike do not settle the final underlying letter.'),
(18,'NOTES: first nested s','Typed cancellation over s in T subscript','confirmed','The enlarged index supports the recorded x cancellation.'),
(27,'Printed replacement target','X-T','confirmed','The last letter is visibly T; it is retained despite X-Z in the preceding display.'),
(28,'Cancelled intermediate sentence','si D est sans points fixes,','confirmed','Every underlying word read beneath the typed x row.'),
(30,'Cancelled paragraph','Notons en passant ... transpose D ... correspondence ... sans points fixes','confirmed','All underlying words, raised t, interlinear X-Z and continuation were read across both cancellation layers.'),
(33,'NOTES: biunivo/que boundary','Typed x row ends after biunivo; pen crosses que and following text','confirmed','The literal division in the draft remains compatible with the enlarged boundary; pen and typed strokes also overlap locally to its left.'),
(35,'NOTES: di-vi-seur','The vi group is covered by typed x impressions','confirmed','The local cancellation is visible in the enlarged word.'),
(36,'NOTES: quoted soit','Dark marks adjoining soit and the insertion curve','retained_uncertain','The word soit is clear, but the quotation-mark strokes cannot be cleanly separated from the insertion connector; the existing uncertainty remains.'),
(37,'End and margins','par U/S; otherwise blank lower margin','confirmed','Final line and all surrounding margins inspected.')
],'Both complete scans and all margins read. Enlarged opening cancellation, raised mark above X, nilpontente, nested fibre indices, par overprint, diviseur, quoted soit and layered cancellation boundaries inspected. Typed insertions are distinguished from their pen placement curves. No arrow or relation is supplied in an empty gap, and printed X-T is retained.')
finish_reviewed(114,[
(8,r'à fibres $(S_1)$',r'à fibres $(S_1\unsure{)|r}$','The closing-parenthesis position also contains a typed r-like impression; retain the overprint rather than silently discarding it.'),
(9,r'D \rightsquigarrow {}^{t}D',r'D \hand{\rightsquigarrow} {}^{t}D','The wavy stem and right arrowhead are hand-drawn.'),
(12,'se débarasser',r'se \unsure{débarasser|débarrasser}','The a/r region is overtyped; the enlarged ink supports both spellings without securely resolving the extra-r question.'),
(15,r'au\xout{x} sens',r'au\xout{\illegible{1}} sens','The extra typed x cancels an underlying character that cannot be securely read.'),
(19,r'\xout{\unsure{exemple}}',r"\xout{\unsure{exemple|l'exempl}}",'The cancelled group has a tall initial l-like trace and a final punctuation-like impression; exemple remains possible but the l-exempl sequence cannot be excluded.'),
(19,r'$T \to S$',r'$T \hand{\to} S$','The morphism arrow is handwritten.'),
(21,r"$X-\overline{Z'}$",r"$X-\overset{\hand{\relbar}}{Z'}$",'The closure bar above Z-prime is a thick pen stroke.'),
(22,r'\xout{\unsure{assure}}',r'\xout{assure}','The underlying a-s-s-u-r-e is readable beneath the x impressions.'),
(23,r'\unsure{$=$}',r'$\hand{\unsure{=|\ne}}$','The dense pen sign has two horizontal strokes and an oblique trace; equality and a slashed equality remain possible from the ink.')
],[
(5,'Foliation','17 above;114 below','confirmed','Both handwritten numbers read directly.'),
(15,'NOTES: membership signs','All six membership glyphs are handwritten','confirmed','Each epsilon-like sign and its neighboring variable was inspected separately.'),
(16,'Typed insertion and deletions','par rapport à X en tous; cancelled de Cartier and en','confirmed','The insertion letters are typed, its attachment is pen, and both local cancellations are visible.'),
(17,'Revised regularity phrase','n-prime and pas cancelled; de Cartier crossed by pen','confirmed','The underlying negative phrasing and the two writing layers remain recorded.'),
(18,'Printed spacing','s ens','confirmed','The enlargement shows a blank between s and ens; it is preserved.'),
(19,'NOTES: obscured word','Cancelled group before égal','retained_uncertain','The enlarged underlying sequence remains ambiguous; no single word is asserted.'),
(20,'Cancelled transition','et on obtient','confirmed','All three underlying words read directly.'),
(23,'Fixed-points parenthesis','point fixes in the singular before the doubtful relation sign','confirmed','The printed singular point is retained.'),
(25,'Typed base-change qualification','pour T/S plat loc de prés finie,','confirmed','Every word, abbreviation and the final comma read in the typed insertion.'),
(30,'NOTES: deleted paragraph','Le petit sorite ... relatifs, et familles algébriques de diviseurs','confirmed','Horizontal pen lines and a bracket bound the paragraph, with internal diagonal hatching; the full deletion and nested typed algébriques cancellation are supported.'),
(31,'Proposed relocation','par.19, intersections complètes relatives','confirmed','The cancelled authorial instruction and its exact paragraph reference were read directly.'),
(33,'NOTES: live addition and margin','Un oubli remains outside the deletion; double long marginal stroke','confirmed','The deletion ends after diviseurs; the live addition and both marginal strokes were inspected.'),
(34,'Final continuation','Formation of Z compatible avec','confirmed','Every final word and the bottom margin were read; no continuation is supplied.')
],'Both complete scans and all margins read. Enlarged first(S1) closing overprint, débarasser, s ens spacing, cancelled word before égal, assure and the relation between the two fixed-point notions inspected. The bottom deletion is bounded by explicit horizontal strikes and a bracket; Un oubli remains live. All membership signs and formula indices compared.')
finish_reviewed(115,[
(6,r'\inserted[typed]{(supposé ouvert, p ex T/S plat lpf.}\inserted{lorsque $T \to S$ est surjectif\unsure{)}}',r'\inserted[typed]{(supposé ouvert, p ex T/S plat lpf.}','The typed, circled qualification attaches after X-Z. The separate handwritten surjectivity qualification has its own attachment after rel à S on the next line and is moved there.'),
(7,r'dans X rel à S. Ce dernier fait résulte du \xout{la compa-}',r'dans X rel à S\inserted{lorsque $T \to S$ est surjectif\unsure{)}}. Ce dernier fait résulte \unsure{du|de} \xout{la compa}%','The lower placement curve meets the baseline after S. The u/e of the following short word is overprinted; no hyphen is visible after the cancelled compa at the edge.'),
(8,r'$s \in S$',r'$s \hand{\in} S$','The membership sign is handwritten.'),
(13,r'\check{F}',r'\overset{\hand{\vee}}{F}','The dual accent above F is handwritten.'),
(14,r'X-Z \longrightarrow P(n)',r'X-Z \hand{\longrightarrow} P(n)','The arrow to P(n) is handwritten.'),
(14,r'\xout{\unsure{a}}',r'\xout{\unsure{a|q}}','The cancelled character after dit has a descending right trace compatible with q as well as the draft a reading.'),
(16,r'$X \neq \emptyset$',r'$X \hand{\neq} \hand{\emptyset}$','Both the inequality and the slashed empty-set circle are pen marks.'),
(16,r'$X-Z \neq \emptyset$',r'$X-Z \hand{\neq} \hand{\emptyset}$','The second inequality and empty-set sign are handwritten.'),
(20,r'P(n) \longrightarrow \mathrm{Div}_{\check{P}/S}',r'P(n) \hand{\longrightarrow} \mathrm{Div}_{\overset{\hand{\vee}}{P}/S}','The displayed arrow and the dual accent in the subscript are handwritten.'),
(21,r'\check{F}',r'\overset{\hand{\vee}}{F}','The dual F in the notation paragraph carries a handwritten V accent.'),
(21,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual P in the same paragraph carries a handwritten V accent.'),
(24,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent in the definition of the parameter bundle is handwritten.'),
(26,r'X-Z \longrightarrow P',r'X-Z \hand{\longrightarrow} P','The displayed arrow after the handwritten f is drawn by hand.'),
(27,r'\xout{\unsure{li}}',r'\deleted{\xout{\unsure{li}}}','The small typed cancellation is additionally covered by short diagonal pen hatching; the underlying li reading remains uncertain.'),
(28,r'\unsure{pseudo-morphisme}',r'pseudo-morphisme','Every letter of the interlinear replacement pseudo-morphisme is readable in the enlarged pen note.'),
(28,r'rel.: S',r'rel.\unsure{:|à} S','The mark after rel. is a short stacked/slanting pen group; colon and à remain possible.'),
(30,r'$D\,|(X-Z)x_S\check{P}$',r'$D\,\hand{|}(X-Z)x_S\overset{\hand{\vee}}{P}$','The restriction stroke and dual accent are handwritten; the baseline product x is typed.'),
(30,r'id_{\check{P}}',r'id_{\overset{\hand{\vee}}{P}}','The dual accent on the subscript P is handwritten.'),
(31,r"d'in\unsure{cid}\xout{\unsure{e}}ence",r"d'in\unsure{c}id\deleted{\unsure{e}}ence",'The i and d in the first crowded group are readable, while c remains doubtful. The extra following e-like character is crossed with a heavy pen stroke, not a typed x row.'),
(31,r'$Px_S\check{P}$',r'$Px_S\overset{\hand{\vee}}{P}$','The dual P in the ambient product carries a handwritten V accent.'),
(32,r'f: X-Z \longrightarrow P',r'f: X-Z \hand{\longrightarrow} P','The final arrow is handwritten.')
],[
(5,'Foliation','18 above;115 below','confirmed','Both handwritten numbers read directly.'),
(6,'NOTES: first qualification','Typed open parenthesis and text inside a pen enclosure','confirmed','Every typed word and lpf. were read; no typed closing parenthesis is supplied from the enclosing bubble.'),
(7,'NOTES: surjectivity addition','lorsque T to S est surjectif; curve reaches after rel à S','corrected_from_scan','The handwriting and its own attachment were inspected separately from the circled typed note; the possible terminal parenthesis remains doubtful.'),
(8,'Reference and cancelled dependency','par.11; cancelled la compatibilité avec changement de base','confirmed','The complete underlying phrase and the reference were read across the line break.'),
(12,'Replacement of devient','Pen-cancelled devient with handwritten est','confirmed','Both the old word and its replacement are clear.'),
(13,'Representation notation','Sum of P(Sym^n(dual F))=P(n)','confirmed','The exact position of the dual accent inside the symmetric power, all parentheses and the equality were checked.'),
(21,'Notation and cancelled instruction','P=P(dual F), Q=P(F)=dual P; cancelled par.19 example instruction','confirmed','All capitals, dual marks, indices and the reference are retained as scanned.'),
(23,'Definition underlining','système linéaire ... sur; paramétré ... projectif; toute famille ...; sur; paramétrée par; qui soit de degré; définisse','confirmed','Each separate underline span was compared; the X/S and degree numeral1 lie outside the recorded underline spans.'),
(27,'NOTES: nonempty-fibres insertion','et lorsque les fibres de dual P sont tous not-empty','confirmed','The complete handwriting, dual accent and inequality were read; the connector reaches the position after diviseurs.'),
(28,'NOTES: pseudo-morphism note attachment','Connector also reaches the end of the following rationelle parenthesis','retained_uncertain','The note is clearly an addition to the rational-map description, but its exact insertion point relative to the parenthetical phrase remains uncertain; the draft placement is retained provisionally.'),
(28,'Cancelled handwritten word','Heavy horizontal pen cancellation under pseudo-morphisme','retained_illegible','The underlying word remains unreadable despite enlargement.'),
(31,'NOTES: incidence and H','Crowded c, cancelled extra e-like letter, handwritten underlined H','retained_uncertain','The unresolved letters remain marked; H and its underline are clear.'),
(33,'Final continuation and margins','famille sans ... continues beyond the page','confirmed','All last words and the lower blank margin were inspected.')
],'Both complete scans and all margins read. The two top insertions and their separate attachments, the full pseudo-morphism note, incidence overtyping, small cancellations, every dual accent and all arrows were inspected. The exact lower note attachment and several letters remain uncertain. Every underlined definition span and all source references were checked.')
finish_reviewed(116,[
(7,r'\xout{xxixxxxxxx}',r'\xout{uniquement}','The underlying word uniquement is readable beneath the typed x row.'),
(7,r'f:X $\longrightarrow$ P',r'f:X $\hand{\longrightarrow}$ P','The first morphism arrow is handwritten.'),
(8,r'\xout{xx}obtient',r'\deleted{\xout{\illegible{1}}}obtient','The small group has typed x marks and additional diagonal pen hatching; the underlying letters remain unreadable.'),
(10,r'f:X $\longrightarrow$ P',r'f:X $\hand{\longrightarrow}$ P','The second morphism arrow is handwritten.'),
(10,r'\xout{xx}$(fx_S',r'\deleted{\xout{\illegible{1}}}$(fx_S','This small cancelled group also has both typed and pen cancellation; no underlying word is secure.'),
(11,r'\xout{xxx} relatif',r'\xout{sur} relatif','The underlying s-u-r is legible.'),
(11,r'$Xx_S\check{P}$',r'$Xx_S\overset{\hand{\vee}}{P}$','The dual accent over this P is a free V-shaped pen stroke, despite the NOTES suggestion that it was typed.'),
(11,r'par rapport à $\check{P}$',r'par rapport à $\overset{\hand{\vee}}{P}$','The second dual accent in the line is likewise handwritten.'),
(14,r'\over{\unsure{1}}{3}.1.',r'\over{\unsure{1|2}}{3}.\hand{1}.','The first underlying digit remains obscured by the large pen3, with1/2-like remnants. The following1 is also a tall freehand numeral.'),
(15,r'\inserted{sans points fixes}',r'\inserted[typed]{sans points fixes}','The inserted words are typed; their curved placement stroke is pen.'),
(16,r'f: X $\longrightarrow$ P',r'f: X $\hand{\longrightarrow}$ P','The proposition’s arrow is handwritten.'),
(16,r'$s\in S$',r'$s\hand{\in} S$','The membership sign is handwritten.'),
(18,r"f(X')\subset P_{\bar{k}}",r"f(X')\hand{\subset} P_{\bar{k}}",'The inclusion sign is handwritten.'),
(19,r'\xout{(xx}',r'\xout{(NB}','The cancelled opening parenthesis and letters N,B are readable.'),
(19,r'\xout{xxxxxxx}',r'\xout{\unsure{intégres|intègres}}','The cancelled word is readable apart from the acute/grave direction of its accent; both candidates are retained.'),
(19,r'\xout{xexsimplifie}',r'\xout{se simplifie}','The underlying se simplifie is legible.'),
(20,r'\xout{xx} s',r'\xout{et} s','The cancelled conjunction et is legible.'),
(23,r'\xout{xx} lorsque',r'\xout{en} lorsque','The underlying e and n are visible beneath cancellation.'),
(23,r'Z $\neq \emptyset$',r'Z $\hand{\neq}\hand{\emptyset}$','The inequality and slashed empty-set circle are handwritten.'),
(24,r'\xout{D}la famille',r'\unsure{D|l}a famille','D and l occupy one overprinted character position before a; the draft’s separate cancelled D plus la incorrectly duplicated that position.'),
(25,r'\inserted{est de dim relative 0}',r'\inserted[typed]{est de dim relative 0}','The insertion is typed and its connector falls after the live =S.'),
(27,r'\xout{Txxxxlxxppx}',r"\xout{Tout l'app\illegible{1}}",'Tout and the beginning l-app are visible beneath cancellation; the following underlying character remains unreadable.'),
(28,r'X-D $\longrightarrow$ S',r'X-D $\hand{\longrightarrow}$ S','The projection arrow is hand-drawn, including its thick right head.'),
(28,r'\xout{(mêmexxxx}',r'\xout{(même en}','The parenthesis and the words même en are readable beneath the x row.'),
(31,r'\xout{xxxmorphisme}',r'\xout{ce morphisme}','The underlying ce morphisme is readable.'),
(31,r'\xout{xlxsxxpas}',r"\xout{n'est pas}",'The cancelled n-prime-est pas is readable.'),
(34,r'\xout{h}linéaires',r"\unsure{h|l}i\unsure{\'n|n}éaires",'The first letter position has h/l-like overtyping, rather than an extra separate h. A displaced accent-like stroke appears above n; its relation to that letter remains uncertain.'),
(34,r"\uline{``sans composante fixe''}",r"``\uline{sans composante fixe}''",'The underline spans the words but does not extend beneath the opening and closing quotation marks.'),
(35,r'\unsure{étaht|étant}',r'étaht','The letter after éta has a clear ascender and h shape.')
],[
(5,'Foliation','19 above;116 below','confirmed','Both handwritten numbers read directly; the bottom number remains in the existing margin macro.'),
(11,'NOTES: Cette correction','Underlying ci remains doubtful; pen tte, condition and separate se are clear','retained_uncertain','Every layer and the left-margin se attachment were inspected; the obscured original ci is not resolved.'),
(14,'NOTES: proposition number','Pen3 and1, with uncertain underlying first digit','retained_uncertain','The overwritten first digit cannot be recovered uniquely from the enlargement.'),
(17,'Algebraic-closure notation','k bars and all fibre indices','confirmed','Every small bar, prime, X/P distinction and nesting was read in its own occurrence.'),
(19,'NOTES: typed intègres and parentheses','Typed interlinear intègres; pen opening and closing parentheses','confirmed','Both the replacement word and the enclosing pen parentheses were inspected.'),
(20,'Printed phrasing','s’énoncé; not a silently regularized verbal form','confirmed','The final acute accent is visible and is retained.'),
(25,'NOTES: relative-dimension insertion','=S remains visible and uncancelled','confirmed','The insertion follows S; it does not visibly replace the equality or the letter.'),
(25,'Small terminal mark','Pen point after de','confirmed','The small isolated point is present at the line end.'),
(31,'NOTES: overprinted words','biunivoque;paramétré;aucun;disant;également;X-D;composante','confirmed','The completed readings remain legible; the local overprints were inspected, including the D in X-D.'),
(35,'Continuation and lower margin','étaht donné une famille(non néc linéaire)','confirmed','Every final word, abbreviation and the lower margin was read.')
],'Both complete scan parts and all margins read. Enlarged short cancellations, uniquement, Cette, proposition digits, Tout l-app fragment, même en and the final linéaires overprint inspected. All dual accents, arrows, membership, inclusion and empty-set signs were checked. Unreadable fragments and the uncertain first digit remain marked.')
finish_reviewed(117,[
(15,r'X \longrightarrow S',r'X \hand{\longrightarrow} S','The structural-morphism arrow is handwritten.'),
(18,'connaissance du morphisme',r'connaissance d\unsure{u|a} morphisme','The enlarged vowel is a/u overtyping; neither reading is imposed.'),
(18,r'X - Z \longrightarrow P',r'X - Z \hand{\longrightarrow} P','The arrow associated with D is handwritten.'),
(20,r'domain\xout{x}e',r'domain\xout{t}e','A tall t ascender and crossbar remain visible beneath the extra typed x.'),
(27,r'\xout{xxx}',r'\xout{\unsure{corr|core}}','The cancelled group shows c-o-r and a final r/e-like letter; both readings remain uncertain.'),
(28,r"X-Z' \longrightarrow P",r"X-Z' \hand{\longrightarrow} P",'The arrow associated with D-prime is handwritten.'),
(35,r'\margin{\unsure{cf}\ \S 20.11.}',r'\margin{$|$\ cf\ \S 20.11.}','The marginal note reads cf section20.11 and is accompanied by a long vertical pen bar spanning the last three lines; the bar is now explicitly recorded.')
],[
(5,'Foliation','20 above;117 below','confirmed','Both handwritten folio numbers read directly.'),
(8,'Printed spelling','dodimension','confirmed','The initial d is visible and is not replaced by c.'),
(8,'NOTES: clipped terminal letters','Final s in des and e in stable','retained_uncertain','The right edge cuts the letters; the source doubts remain.'),
(10,'Definition wording','sans composante fixe ... si elle est sans composante fixe','confirmed','The repeated wording and the displayed codimension comparison are retained exactly.'),
(15,'NOTES: proposition number','Typed2 with unreadable pen replacement and curved slash','retained_illegible','Magnification confirms the heavy overwritten group but does not recover its intended number.'),
(16,'NOTES: syst-e-ême','Extra e covered by typed x cancellation','confirmed','The extra underlying e remains visible.'),
(17,'NOTES: handwritten relations and duals','Both dual accents; inequality, inclusion, intersection, union and membership signs','confirmed','Each occurrence and its direction or operation was checked against the scan.'),
(20,'Replacement terminology','Pen pseudo-morphisme replacing application rationelle; typed rel à S and domaine','confirmed','All words, quotation marks and their separate writing layers were read directly.'),
(23,'Reference revision','Pseudo-morphismes replaces applications rationelles; section20.10 replaces SGAD XVIII no1','confirmed','Both the cancelled reference and the new handwritten reference were read in full.'),
(25,'Cancelled relocation and live punctuation','Last no of paragraph11 on densité schématique; Il faut prouver que.','confirmed','The complete cancelled instruction and the live terminal period after que are present.'),
(26,'NOTES: une','Final e cancelled with pen','confirmed','The small pen stroke crosses the e, leaving un.'),
(26,'Cancelled hypothesis','U est un ouvert de X schématiquement relativement dense','confirmed','The entire phrase was read beneath the typed x row.'),
(31,'Cancelled set formula','X-(Z u Z-prime)=d’autre part','confirmed','All visible letters, parentheses and the typed u surrogate were retained under cancellation.'),
(35,'NOTES: final marginal reference','cf section20.11 with long vertical bar','corrected_from_scan','The enlarged ligature resolves cf and reveals the full separate bar.'),
(36,'Final restriction and margins','Restriction to X-Z-double-prime; blank lower margin','confirmed','All final indices, punctuation and margins inspected.')
],'Both complete scans and all margins read. Enlarged overwritten proposition number, du/da, domaine extra t, cancelled corr/core and cf20.11 margin note inspected. Every handwritten set sign, dual accent, morphism arrow, quotation and replacement reference checked. The proposition replacement remains unreadable; no number is supplied by inference.')
finish_reviewed(118,[
(7,r'ce qui entrainera',r'\margin{$|$}\margin{$\wr$}ce qui entrainera','A long left bracket and a separate wavy near-vertical pen line through the text span this passage through the end of the lemma proof; their graphic presence is recorded without assigning deletion or relocation as certain.'),
(8,r'\underline{J}\to i_',r'\underline{J}\hand{\to} i_','The first canonical-map arrow is handwritten.'),
(8,r'\underline{J}|X-Z',r'\underline{J}\hand{|}X-Z','The restriction bar in the first formula is handwritten.'),
(9,r'X-Z"\to X',r'X-Z"\hand{\to} X','The immersion arrow is handwritten.'),
(10,r'\underline{J}\to\underline{O}_X',r'\underline{J}\hand{\to}\underline{O}_X','The map from J to O_X has a handwritten arrow.'),
(10,r'i_{\hand{*}}',r'i_{\hand{\unsure{*|\relbar}}}','The small subscript after this i is a dense pen wedge with a horizontal terminal; star and a short bar-like mark remain possible.'),
(11,r'\underline{J}\,|\,X-Z" \longrightarrow \underline{O}_X\,|\,X-Z"',r'\underline{J}\,\hand{|}\,X-Z" \hand{\unsure{\longrightarrow|\relbar}} \underline{O}_X\,\hand{|}\,X-Z"','Both restriction bars are pen. The connector has a right terminal tick but no secure arrowhead, so arrow and bar readings remain marked.'),
(11,r'\unsure{et}',r'\over{e}{\unsure{e|a}}t','The first letter has a heavy pen loop/retouch over typed e, with an a-like lower trace; t is clear.'),
(12,r'\xout{fibresxde}',r'\xout{fibres de}','The two underlying words are readable; the interword x is cancellation rather than literal text.'),
(12,r'$x\in Z" \Rightarrow',r'$x\hand{\in} Z" \hand{\Rightarrow}','The membership and implication signs are handwritten.'),
(12,r'\underline{J}_{s\,\hand{\unsure{*}}} \geqslant',r'\underline{J}_{s\,\hand{\unsure{*|x}}} \hand{\geqslant}','The small pen mark after s has crossed strokes compatible with star or x; the inequality is also handwritten.'),
(13,r'\hand{\unsure{3.2|3.1}}',r'\hand{3.2}','The enlarged final numeral has the curved top and rightward lower foot of2; the lemma number is readable as3.2.'),
(13,r'$X\to S$',r'$X\hand{\to} S$','The lemma’s structural arrow is handwritten.'),
(15,r'\margin{\unsure{$\downarrow$ \S 20 !!}}',r'\margin{cf\ \S 20.11}','The enlarged marginal ligature reads cf, followed by section20.11, within an oval pen enclosure; the two final strokes are digits1,1.'),
(16,r'$x\in X$',r'$x\hand{\in} X$','The first membership sign in the lemma is handwritten.'),
(16,r'$s\in S$',r'$s\hand{\in} S$','The second membership sign in the lemma is handwritten.'),
(16,r'F_{s\,\hand{\unsure{*}}}\geqslant 1',r'F_{s\,\xout{\unsure{n|x}}}\hand{\geqslant} 1','The small group after s has serifed typewriter impressions resembling a cancelled n/x, rather than a handwritten star. The following inequality is pen.'),
(16,r'F_s \geqslant 2',r'F_s \hand{\geqslant} 2','The second depth inequality is handwritten.'),
(17,r'F\to i_',r'F\hand{\to} i_','The canonical-map arrow in the lemma is handwritten.'),
(17,r'(F|X-T)',r'(F\hand{|}X-T)','The restriction bar in the lemma is handwritten.'),
(18,r'X-T\to T',r'X-T\hand{\to} T','The immersion arrow is handwritten; its printed target T is retained.'),
(22,r'F \geqslant \mathrm{prof}_x F_s',r'F \hand{\geqslant} \mathrm{prof}_x F_s','The depth comparison in the proof is handwritten.'),
(23,r'$x\in X$',r'$x\hand{\in} X$','This membership sign is handwritten.'),
(23,r'$s\in S$',r'$s\hand{\in} S$','This membership sign is handwritten.'),
(23,r'F_s \geqslant 1',r'F_s \hand{\geqslant} 1','The first lower bound in the proof is handwritten.'),
(23,r'(resp.$\geqslant 2$)',r'(resp.$\hand{\geqslant} 2$)','The parenthesized lower bound is handwritten.'),
(23,r'$x\in T$',r'$x\hand{\in} T$','The final membership sign in the proof is handwritten.'),
(28,r'\xout{\unsure{Z}}\inserted{X-Z}',r'\deleted{\unsure{Z}}\inserted[typed]{X-Z}','The old Z-like character is obscured by pen hatching; the replacement X-Z is typed with a curved pen attachment.'),
(28,r'domain\xout{e}',r'domain\unsure{\xout{e}|e}','The final e position is overtyped, but a separate x cancellation cannot be cleanly distinguished; both cancellation and live-e readings remain possible.'),
(29,r'$U\supset X-Z$',r'$U\hand{\supset} X-Z$','The inclusion sign is handwritten.'),
(30,r'$U\longrightarrow P$',r'$U\hand{\longrightarrow} P$','The arrow to P is handwritten.'),
(30,r'\xout{xfamillex}',r'\xout{\unsure{e} famille}','The underlying famille is readable, with an uncertain extra e-like character before it; the x marks are not retained as literal letters.'),
(31,r'U\unsure{/}S',r'U\unsure{/|x}S','A slash and an x-like overprint occupy the separator position; both readings are retained.'),
(31,r'\check{P}',r'\overset{\hand{\vee}}{P}','The parameter-bundle dual accent is handwritten, contrary to the NOTES suggestion.'),
(31,r"D'|(X-Z)\times_S\check{P}",r"D'\hand{|}(X-Z)\times_S\overset{\hand{\vee}}{P}",'The first restriction bar and dual accent in the equality are handwritten.'),
(31,r'D|(X-Z)\times_S\check{P}',r'D\hand{|}(X-Z)\times_S\overset{\hand{\vee}}{P}','The second restriction bar and dual accent are handwritten.'),
(32,r'D|U\times_S\check{P}',r'D\hand{|}U\times_S\overset{\hand{\vee}}{P}','The next restriction bar and dual accent are handwritten.'),
(33,r'D|U\times_S\check{P}',r'D\hand{|}U\times_S\overset{\hand{\vee}}{P}','The final restriction bar and dual accent are handwritten.'),
(34,r'Z\cap U=\emptyset',r'Z\hand{\cap} U=\hand{\emptyset}','The intersection and empty-set signs are handwritten.')
],[
(5,'Foliation','21 above;118 below','confirmed','Both handwritten page numbers read directly.'),
(7,'NOTES: long bracket and wavy line','Left bracket and internal wavy pen line from opening through lemma proof','retained_uncertain','Their shapes and full extents were inspected. The ink alone does not settle whether they request deletion, relocation or another editorial operation; the body remains live.'),
(8,'NOTES: clipped isomor-p','A cancelled p at the right edge','confirmed','The visible underlying p and its cancellation are retained.'),
(13,'NOTES: lemma number','3.2','corrected_from_scan','Magnification resolves the final handwritten digit as2.'),
(15,'NOTES: marginal reference','cf section20.11 in an enclosing arc','corrected_from_scan','The ligature and all four digits were compared directly with the neighboring-page handwriting.'),
(16,'NOTES: stroke before prof','Faint short diagonal with a hooked upper terminal','retained_uncertain','It remains an uncertain pen mark rather than a supplied mathematical sign.'),
(16,'Lemma quantifier','For every x in X above s in S','confirmed','The printed X is retained, without changing it to T.'),
(18,'Lemma immersion target','i:X-T to T','confirmed','The displayed target is visibly T; it is preserved without mathematical correction.'),
(22,'NOTES: right-margin point','A separate point after pour tout','confirmed','The point is visible and remains in the source line.'),
(24,'Proof references','par.6;par.5;proposed paragraph11 placement','confirmed','Every reference and the complete noetherian-reduction qualification were read.'),
(27,'Internal references','prop.2 and proposition1','confirmed','These printed numbers are retained despite the revised numbering elsewhere.'),
(34,'Final spelling','point fixes in the singular','confirmed','The printed wording and final cqfd are retained.')
],'Both complete images and all margins read. Enlarged marginal reference, lemma number, two small depth-index groups, direct-image subscript, et retouch and cancelled Z inspected. Every arrow, restriction, dual accent, inequality, inclusion, intersection and membership was checked. The long graphical marks have unresolved function; printed X-quantification and target T remain unchanged.')
finish_reviewed(119,[
(5,r'\margin{\unsure{2/2}}',r'\margin{\unsure{22|2/2}}','Two2-like digits are visible, but the descending enclosure line passes between them; the separation may be graphic rather than a written slash.'),
(6,r'\margin{(trait vertical au crayon dans la marge gauche, le long du premier paragraphe)}',r'\margin{$|$}','The source’s descriptive sentence is editorial rather than manuscript text. A pencil bar is visibly present beside the opening paragraph and is represented graphically.'),
(7,r'\deleted{\unsure{3}}',r'\deleted{\unsure{3|2}}','The cancelled digit retains both3-like and2-like traces beneath pen hatching.'),
(9,r'récip\unsure{r}oque',r'récip\unsure{r|p}oque','The overprinted letter contains both an r shoulder and a p-like lower trace.'),
(10,r'\unsure{\hand{3}}3.',r'\hand{3}\unsure{\over{2}{3}|3}.','The first large pen3 is readable; the following crowded numeral may be a3 over2 or a repeated3. No separating point is supplied.'),
(10,r'$X \to S$',r'$X \hand{\to} S$','The structural arrow is handwritten.'),
(11,r'\check{P}',r'\overset{\hand{\vee}}{P}','The first dual accent is handwritten.'),
(11,r'\check{E}',r'\overset{\hand{\vee}}{E}','The dual E in Q=P(dual E) has a pen V accent.'),
(11,r'\xout{\unsure{vectoriel sur}}',r'\xout{vectoriel sur}','Both underlying words are readable beneath typed cancellation.'),
(12,r'\check{E}',r'\overset{\hand{\vee}}{E}','The dual accent in F=dual E is handwritten.'),
(13,r'$\emptyset$',r'$\hand{\unsure{\phi|\emptyset}}$','The first set symbol is a handwritten oval with an oblique stem extending above and below; phi and the draft empty-set reading remain candidates.'),
(13,r'\inserted{$D$ \deleted{\unsure{E}}}',r'\inserted[typed]{$D$ \deleted{\unsure{E}}}','The added D and the cancelled E-like character have typed serifs; their placement curve and local cancellation are pen.'),
(13,r'\xout{\unsure{sur}}',r'\xout{sur}','The underlying s-u-r is readable.'),
(14,r'$z \in Z$',r'$z \hand{\in} Z$','The membership sign is handwritten.'),
(15,r'\underline{O}_{X_s} \geqslant 2',r'\underline{O}_{X_s} \hand{\geqslant} 2','The first depth comparison is handwritten.'),
(15,r'\xout{\unsure{Alors}}',r'\xout{Alors}','The cancelled Alors is legible.'),
(16,r'D \in \emptyset',r'D \hand{\in} \hand{\unsure{\phi|\emptyset}}','The cancelled line contains a pen membership sign and the oval-stemmed set glyph; the remaining uncertainty of the whole line is retained.'),
(17,r'Soit $\emptyset$',r'Soit $\hand{\unsure{\psi|\emptyset}}$','The second set symbol has an open fork/u-like body crossed by a stem, visibly different from the oval symbol; psi and the draft reading remain candidates.'),
(18,r'\inserted{$f$}',r'\inserted[typed]{$f$}','The inserted f has typewriter serifs; only its placement slash is pen.'),
(19,r'$z \in X$-$U$',r'$z \hand{\in} X$-$U$','The membership sign in the second condition is handwritten.'),
(19,r'$\Longrightarrow$',r'$\hand{\Longrightarrow}$','The implication arrow is handwritten.'),
(19,r'\underline{O}_{X_s} \geqslant 2',r'\underline{O}_{X_s} \hand{\geqslant} 2','The second depth comparison is handwritten.'),
(19,r'\inserted{$\surd$,',r'\inserted{$\unsure{\surd}$,','The marginal note starts with an editorial check-like stroke ending in a small loop; its conventional surd-like transcription remains explicitly uncertain.'),
(20,r'D \rightsquigarrow f_D',r'D \hand{\rightsquigarrow} f_D','The wavy arrow in the natural map is handwritten.'),
(20,r'de $\emptyset$  dans $\emptyset$',r'de $\hand{\unsure{\phi|\emptyset}}$  dans $\hand{\unsure{\psi|\emptyset}}$','The source and target repeat the distinct oval and forked pen set glyphs, respectively.'),
(22,r'D \in \emptyset',r'D \hand{\in} \hand{\unsure{\phi|\emptyset}}','The membership and the oval set glyph are handwritten.'),
(24,r'\xout{\unsure{Dif}}',r'\deleted{\unsure{Dif}}','The small old group is cancelled by diagonal pen strokes; its letters remain uncertain.'),
(26,r"Pour qu'une f $\emptyset$ appartienne à provienne d'une $D$ $\emptyset$, il",r"Pour qu'une f $\hand{\unsure{\psi|\emptyset}}$ appartienne à provienne d'une $D$ $\hand{\unsure{\phi|\emptyset}}$, il",'Both distinct pen set glyphs can be recognized within the typed-cancelled line; the line’s remaining original uncertainty is retained.'),
(27,r'f \in \emptyset',r'f \hand{\in} \hand{\unsure{\psi|\emptyset}}','The first membership in(b) and its forked set glyph are handwritten.'),
(27,r'$z \in X$-$U$',r'$z \hand{\in} X$-$U$','The membership before X-U is handwritten.'),
(28,r'\underline{O}_{X_s,z} \geqslant 2',r'\underline{O}_{X_s,z} \hand{\geqslant} \unsure{2|0}','The inequality is pen; the bound is overtyped with a circular0-like impression over a2-like form, so both readings are retained.'),
(28,r'\xout{\unsure{et existe}}',r'\xout{(il en existe}','The enlargement shows the opening parenthesis and the three words il en existe beneath cancellation.'),
(29,r'D \in \emptyset',r'D \hand{\in} \hand{\unsure{\phi|\emptyset}}','The membership and oval set glyph in the criterion are handwritten.'),
(30,r'\deleted{\unsure{$f_U$ satisfasse la condition énoncée dans 3.1. et que}}',r'\deleted{$f_U$ satisfasse la condition énoncée dans 3.1. et que}','All words and the3.1 reference are readable beneath the long pen cancellation.'),
(31,r'f_U^*(\underline{O}_P(1))',r'f_U^{\hand{\unsure{*|\bullet}}}(\underline{O}_P(1))','The raised pen mark is a dense rounded point without secure star arms; star and point readings remain possible.'),
(31,r'$U \to P$',r'$U \hand{\to} P$','The map defining the pullback has a handwritten arrow.'),
(32,r'\deleted{\unsure{$f_U$ satisfasse la condition énoncée dans 3.1 et}}',r'\deleted{$f_U$ satisfasse la condition énoncée dans 3.1 et}','The second cancelled handwritten condition is fully readable, including its final et.'),
(33,r'\xout{\unsure{que}}',r'\xout{en ait}','The underlying five-letter sequence reads en ait, rather than que.'),
(33,r'i_*(\underline{L}_U)',r'i_{\hand{*}}(\underline{L}_U)','The direct-image star is handwritten.'),
(33,r'$U \to X$',r'$U \hand{\to} X$','The immersion arrow is handwritten.'),
(39,r'$s \in S$',r'$s \hand{\in} S$','The final membership sign is handwritten.')
],[
(5,'NOTES: top foliation','22/2-slash-2 candidates','retained_uncertain','The annotation enclosure crosses between the two digit shapes; the exact foliation reading remains doubtful.'),
(7,'Authorial opening','répens; éculée et pisseuse; mi chemin','confirmed','Every word of the author’s criticism is preserved as written.'),
(10,'NOTES: proposition numbering','Two adjacent3-like figures with an uncertain underlying2','retained_uncertain','Magnification does not justify supplying a missing separator or a single normalized proposition number.'),
(13,'NOTES: two set glyphs','Oval-stemmed and forked-stemmed pen symbols','corrected_from_scan','The distinct shapes and handwritten layer are preserved throughout instead of conflating both as a single typed empty-set sign.'),
(15,'Cancelled image notation','s followed by cancelled =g(z))','retained_uncertain','The underlying letters and parentheses remain crowded under the typed cancellation; the source uncertainty is retained.'),
(16,'NOTES: cancelled long map sentence','D, set glyph, associons, morphisme correspondant, f, X-Z, P and considérée','retained_uncertain','The main fragments are readable, but cancellation obscures connecting signs and some letters; the full original uncertainty is retained rather than completing the sentence.'),
(18,'NOTES: mark after S and dom correction','Obscured old mark; typed f insertion; handwritten U= and overwrite at dom','retained_uncertain','The old mark cannot be identified securely. U= is clear; the overwritten dom/U region remains uncertain.'),
(19,'NOTES: marginal condition and matching mark','f_U=f restriction U, arrow to dual P, non-degeneration condition in3.1','confirmed','Every word, the dual accent and the reference were read in the two-line marginal note. Its matching looped stroke is visible after the depth bound.'),
(26,'NOTES: cancelled opening of(b)','Pour qu’une f ... appartienne à provienne d’une D ..., il','retained_uncertain','The unusual sequence is visibly present; no grammatical completion or mathematical simplification is made.'),
(29,'NOTES: small terminal sign','Small uncertain check-like pen mark after que','retained_uncertain','The tiny right-edge mark remains too dense for a secure glyph reading.'),
(38,'NOTES: final cancelled hand mark','Small heavily crossed symbol after dans','retained_illegible','The underlying handwritten character remains unreadable.'),
(39,'Final continuation','Condition on fibres satisfying(S2); normals and geometric normals','confirmed','All final lines, indices, qualifiers and the bottom margin were inspected.')
],'Both complete scan parts and all margins read. Enlarged proposition figures, réciproque overprint, mark after S, dom/U revision, bound2/0, il en existe, en ait and both cancelled handwritten conditions inspected. Both distinct pen set-glyph families, every dual accent, morphism sign, depth index and marginal insertion were compared. Remaining uncertainty is explicitly preserved.')
finish_reviewed(120,[
(5,r'\unsure{27}',r'\unsure{23|27}','The two clipped top-right digits show a2 and a second figure with3-like curves crossed by the enclosure line;27 remains possible.'),
(7,r'$\geq 2$',r'$\hand{\geq} 2$','The opening codimension comparison is handwritten.'),
(7,r'\xout{\illegible{2}\unsure{(comme dans les cas envisa}}',r'\xout{ou encore (comme dans les cas envisa}','Magnification resolves the cancelled words ou encore and the entire visible continuation through envisa; no missing ending is supplied.'),
(8,r'\xout{familles}',r"$\hand{\unsure{\phi|\emptyset}}$ est alors l'ensemble des \xout{familles}",'The draft omitted the visible opening phrase before familles. Its set symbol is the oval-stemmed pen glyph from119; the following words are typed.'),
(8,r'\inserted{syst lin}',r'\inserted[typed]{syst lin}','Both abbreviated words are typed above the cancelled familles, with a pen attachment curve.'),
(9,r'$\emptyset$',r'$\hand{\unsure{\psi|\emptyset}}$','The cancelled phrase has the forked-stemmed pen set glyph, as in119.'),
(10,r'\inserted{pour}',r'\inserted[typed]{pour}','The inserted pour is typed; its placement stroke is pen.'),
(11,r'$\to$',r'$\hand{\to}$','The arrow in f:X to P is handwritten.'),
(11,r'$\geq$',r'$\hand{\geq}$','The second codimension comparison is handwritten.'),
(12,r'$\emptyset$',r'$\hand{\unsure{\psi|\emptyset}}$','The live set glyph after dans ce cas has the same forked pen form.'),
(16,r'i_*(\underline{L}_U)',r'i_{\hand{*}}(\underline{L}_U)','The first direct-image star is handwritten.'),
(17,r'\xout{pour le\unsure{x} il faut} \inserted[typed]{la cond. envisagée est inv. par}',r'\xout{pour le\unsure{x} il faut}','The replacement phrase is typed above the cancelled line beginning il suffit and attaches after donc; its earlier position before base S prime misrepresented the insertion.'),
(18,r'\inserted{\unsure{du moins si $U\to X$ est quasi-compact, cas auquel on se ramène sans difficultés}}',r'\inserted{du moins si $U\to X$ est quasi-compact, cas auquel on se ramène sans \unsure{difficultés}}','The boxed handwritten note is readable through sans; its final clipped word remains doubtful. Matching looped signs attach it after réf.'),
(18,r'donc \xout{il suffit de trouver un morphisme} fid plat qu cpc',r'donc \inserted[typed]{la cond. envisagée est inv. par} \xout{il suffit de trouver un morphisme}','The interlinear replacement belongs after donc. The boxed fid plat qu cpc is moved by a downward arrow to after changement de base, and is encoded there separately.'),
(19,r'changement de base.',r'changement de base \inserted[typed]{fid plat qu cpc}.','The drawn arrow lands immediately after base and before the full stop; all four abbreviated groups are typed.'),
(20,r"i'_*(\underline{L}'_U)",r"i'_{\hand{*}}(\underline{L}'_U)",'The next direct-image star is handwritten.'),
(22,r"i'_*(\underline{L}'_U\otimes_{S'}M')\simeq i'_*(\underline{L}'_U)",r"i'_{\hand{*}}(\underline{L}'_U\otimes_{S'}M')\hand{\simeq} i'_{\hand{*}}(\underline{L}'_U)",'Both stars and the isomorphism sign in the projection formula are pen additions.'),
(22,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent under the first O is handwritten.'),
(23,r"i'_*(\underline{N}')",r"i'_{\hand{*}}(\underline{N}')",'The direct-image star before N prime is handwritten.'),
(24,r')^*(',r')^{\hand{*}}(','The pullback star in the displayed definition of N prime is handwritten.'),
(24,r'\check{P}',r'\overset{\hand{\vee}}{P}','A small pen V is visible over this P in the product index.'),
(25,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent after sur is handwritten.'),
(27,r'\deleted{\xout{\illegible{1}}}',r'\deleted{\xout{\illegible{1}\unsure{D N P}\illegible{1}\unsure{Or}}\unsure{S}}','The cancellation contains D-, N-, P- and Or-like fragments, with a separate S-like typed impression below. Pen loops and raised typed x impressions obscure the remaining characters; no coherent expression is reconstructed.'),
(27,r'D$\in\emptyset$',r'D$\hand{\in}\hand{\unsure{\phi|\emptyset}}$','Membership and the oval-stemmed set glyph are handwritten.'),
(28,r'D$|$U$\times_S\check{P}$',r'D$\hand{|}$U$\times_S\overset{\hand{\vee}}{P}$','The first restriction bar and dual accent in this line are pen.'),
(28,r'\underline{N}|U\times_S\check{P}',r'\underline{N}\hand{|}U\times_S\overset{\hand{\vee}}{P}','The second restriction bar and dual accent are pen.'),
(30,r'\xout{\illegible{1}}',r"\xout{qu'on aura}",'The underlying cancelled phrase is readable as qu’on aura.'),
(30,r'\to',r'\hand{\to}','The structural arrow in the application of the lemma is handwritten.'),
(31,r"i'_*(\underline{N}')\simeq\underline{N}",r"i'_{\hand{*}}(\underline{N}')\hand{\simeq}\underline{N}",'The first star and isomorphism sign in this line are pen.'),
(31,r"i'_*(\underline{N}')",r"i'_{\hand{*}}(\underline{N}')",'The second direct-image star in this line is handwritten.'),
(32,r'D$\in\emptyset$',r'D$\hand{\in}\hand{\unsure{\phi|\emptyset}}$','The final membership and oval-stemmed set glyph are handwritten.'),
(37,r'\margin{\unsure{Rq compliquée} \unsure{Il faut expliquer} \illegible{2} \unsure{$f\times\mathrm{id}$} \unsure{si $p^{-1}(H)$} \unsure{est défini} \illegible{1} \unsure{diviseur rel.} \unsure{à la condition} \illegible{3} \unsure{diviseur relatif} \unsure{$X\times P$} \unsure{/P} \illegible{2}}',r'\margin{\deleted{\unsure{Rq compliquée}} \unsure{Il} faut \unsure{exprimer|expliquer} \illegible{1} $(f_U\times_S\mathrm{id}_P)^{-1}(H)$ \unsure{qui} est défini comme \unsure{diviseur} rel. à P \unsure{grâce} à la condition \illegible{3} \unsure{$f_U$} \unsure{se prolonge en} \unsure{un} diviseur relatif /P \unsure{à} $X\times_S P$ \unsure{/P} \deleted{\illegible{2}} \unsure{*}}','Both rotated halves of the long note were read baseline by baseline. The inverse-image formula, est défini comme, rel. à P, à la condition, diviseur relatif /P and X times_S P are readable. Several line beginnings meet the cut edge; doubtful words and intervening illegibility remain marked. First and final lines carry separate horizontal pen cancellation; the final star-like mark is also preserved.')
],[
(8,'NOTES: sont correction','Small pen loop and stroke over the n position','retained_uncertain','The original ie candidate cannot be resolved into two secure letters; the uncertain insertion remains.'),
(18,'NOTES: S prime to S gap','A blank space between the two typed S letters','confirmed','No connecting arrow is present in either supplied scan.'),
(18,'NOTES: boxed note attachment','Matching looped strokes after réf and at the top note','confirmed','The complete connector and top enclosure were traced; clipped foliation remains separately uncertain.'),
(22,'prèndra/prendra','Small accent-like impression above e','retained_uncertain','The mark cannot be cleanly separated from nearby ink; both original readings remain.'),
(26,'N without prime','Typed underlined N','confirmed','There is no prime at this occurrence; it is retained.'),
(27,'Inverse-image notation','(f_U times id_P)(H), without an exponent','confirmed','The main-body formula visibly lacks the inverse-image exponent that is present in the margin note; none is supplied.'),
(27,'NOTES: cancelled cluster','Typed x impressions above; S-like impression below; crossing pen loops','retained_uncertain','The writing layers and surviving fragments were inspected in an enlarged crop, without reconstructing the old expression.'),
(30,'Lemma reference','Handwritten3.2 after lemme','confirmed','Both digits and decimal point are visible.'),
(34,'NOTES: Cartier cancellation','Local wavy pen stroke through Cartier','confirmed','The bounded word cancellation is distinct from the long marginal note enclosure.'),
(34,'Final product factors','X times_S P, twice, with plain P','confirmed','No dual accent is visible over either of these final P occurrences.'),
(35,'NOTES: final D','Handwritten D followed by a full stop','confirmed','The capital is pen; the following point is separate.'),
(37,'NOTES: long marginal note','Upper and lower halves overlap; all visible baselines and marks inspected','retained_uncertain','The note is partly cut at the page edge. Its surviving words, formula, two local cancellations and enclosing bracket are recorded; no missing wording is supplied.'),
(39,'Foliation','120 below','confirmed','The bottom-left archive number and surrounding blank margin were inspected.')
],'Both full scan parts and all margins read, including the complete long angled note in two enlarged rotated views. The omitted opening phrase, placement of the typed base-change revisions, every arrow, star, dual accent, restriction and comparison were checked. Main-body and marginal inverse-image formulas are retained with their visible differences; clipped and obscured text remains explicitly uncertain.')
finish_reviewed(121,[
(8,'éléments',r'\unsure{éléments}','The middle letters are overtyped with an extra e-like impression; the word remains a supported but uncertain reading.'),
(8,r'$\in$',r'$\hand{\in}$','The membership sign after s is handwritten.'),
(10,r'\longrightarrow',r'\hand{\longrightarrow}','The base-change arrow is handwritten.'),
(10,'plus haut',r'plus \unsure{haut}','The first two letters of haut contain overlapping h/a-like impressions; the whole word remains marked.'),
(11,'diviseur',r'di\unsure{v}iseur','The v position retains an additional dot/stem impression from overtyping; the reading is explicitly uncertain.'),
(12,'rédiger',r'\unsure{r}édiger','The initial r is overprinted with another curved impression; the supported r reading remains marked.'),
(13,'démonstration',r'démons\unsure{t|s}ration','The character after the first s contains both the t crossbar and an s-like lower impression.'),
(14,'dégager',r'déga\unsure{ge}r','The adjacent g/e positions are merged by overtyping; their reading is preserved with doubt.'),
(15,r'\margin{\unsure{voir aussi}',r'\margin{$|$}\margin{\unsure{voir aussi}','A long pencil line begins beside the corollary and continues down to the paragraph beginning On utilise; its presence was omitted from the transcription.'),
(15,r'$\to$',r'$\hand{\to}$','The arrow in g:X to S is handwritten.'),
(16,r'$\in$',r'$\hand{\in}$','The membership sign in x in Z is handwritten.'),
(16,r'prof$_x$',r'prof$_{\unsure{x|s}}$','The depth subscript is heavily overtyped, with an x-like upper crossing and s-like lower curve; no unique glyph is secure.'),
(16,r'\geq 2',r'\hand{\geq} 2','The depth comparison is handwritten.'),
(17,r"\inserted[soit U=X-Z et i:U$\to$X l'immersion c an.]",r"\inserted[typed]{soit U=X-Z et i:U$\hand{\to}$X l'immersion c an.}",'The interlinear sentence is typed, with a handwritten arrow. Its malformed optional-argument encoding is replaced by the insertion macro’s typed form; the visible c an spacing remains.'),
(19,r'\inserted[de t.f]',r'\inserted[typed]{de t.f}','The qualification is typed above L, with a pen placement curve.'),
(20,r'\underline{L}|U',r'\underline{L}\hand{|}U','The restriction bar is handwritten.'),
(20,r'\inserted[a)]',r'\inserted[typed]{a)}','The label a) is typed above le foncteur; the attachment is pen.'),
(20,r'\rightsquigarrow',r'\hand{\rightsquigarrow}','The wavy functor arrow is handwritten.'),
(21,r'\unsure{quelque}','quelque','All letters of the cancelled quelque can be read in the enlargement.'),
(21,r'\xout{xxxx}',r'\xout{on a}','The underlying cancelled group reads on a; the x impressions are cancellation marks.'),
(22,r'\underline{L} \to',r'\underline{L} \hand{\to}','The canonical-map arrow is handwritten.'),
(22,r"\inserted[Pour que $\underline{L}$ soit de rang n, il f et s que $\underline{L}'$ le soit.]",r"\inserted[typed]{Pour que $\underline{L}$ soit de rang n, il f et s que $\underline{L}'$ le soit.}",'The whole rank sentence is typed with a long pen attachment after isomorphisme.'),
(22,r'\hand{(} b)',r'b)','The curved stroke before b) is the end of the long insertion connector, rather than a literal opening parenthesis.'),
(27,r'\inserted[lequel sera alors unique,]',r'\inserted[typed]{lequel sera alors unique,}','The uniqueness phrase is typed between the lines.'),
(27,r'\hand{|} Pour',r'Pour','The vertical stroke is the placement connector for the preceding insertion; it is not a literal bar in the sentence.'),
(28,r'\inserted{\unsure{que}}',r'\inserted{que}','The enlarged pen word has the q descender and joined u/e strokes; que is readable.'),
(30,r'\xout{xxx}',r'\xout{con}','The underlying three letters c-o-n remain visible beneath the x cancellation.'),
(34,r"$\emptyset \to$ \unsure{$\emptyset'$|$\emptyset$}",r'$\hand{\unsure{\phi|\emptyset}} \hand{\to} \hand{\unsure{\psi|\emptyset}}$','Both set symbols and the arrow are pen. The target has the forked-stemmed form; enlargement shows its raised terminal belongs to the glyph and supplies no separate prime.'),
(36,r'$\emptyset$',r'$\hand{\unsure{\phi|\emptyset}}$','The final set glyph repeats the oval-stemmed handwritten symbol.')
],[
(5,'Foliation','24 above;121 below','confirmed','Both handwritten numbers and the surrounding margins were read.'),
(10,'Lemma reference','4.2.','confirmed','The inserted first digit is visibly4. It remains4.2 despite the later3.2 references on the same page.'),
(11,'Equivalence abbreviation','sss','confirmed','All three letters are s and carry an underline; no conventional abbreviation is substituted.'),
(15,'NOTES: margin reference','voir aussi candidate;section20 with obscured following numeral;20.11','retained_uncertain','The initial words and first final numeral are crowded or overwritten. The second reference20.11 is clear.'),
(18,'Cancelled sentence','Soit L un Module loc libre sur U=X-Z, alors L prime','confirmed','All words, both L occurrences, prime and equality were read beneath cancellation.'),
(19,'Cancelled sentence continuation','est isomorphe à la restriction','confirmed','Every underlying word remains readable.'),
(22,'Typed rank insertion','Pour que L soit de rang n, il f et s que L prime le soit.','confirmed','The entire line and the long attachment ending after isomorphisme were inspected.'),
(23,'Base in(b)','Module loc libre sur X','confirmed','The printed base is X; no substitution of U is made.'),
(25,'Mark after D prime','A thin diagonal pen slash','retained_uncertain','The stroke is visible between D prime and sur; no precise editorial function is assigned.'),
(27,'NOTES: et égal and bottom line','et égal;matching looped b;à l’adhérence schématique de D prime dans X.','confirmed','The two parts and their matching reference signs support the existing joined insertion; every word of the lower note was read.'),
(28,'Relative-divisor sentence','Pour que D prime ... il f.et s.que D le soit','confirmed','The direction and both primes were read as printed.'),
(33,'NOTES: local factoriality insertion','les anneaux locaux de X factoriels,(par exemple;X régulier;closing parenthesis','confirmed','All handwriting and the frame around X régulier were read; the old parenthetical example is locally struck through.'),
(34,'NOTES: possible prime on target set','No detached prime;forked pen glyph','corrected_from_scan','The enlarged upper-right stroke is continuous with the target glyph. The alphabetic identity remains uncertain.'),
(36,'Final continuation','Regular scheme locally of finite type over a field k;projective bundle over k','confirmed','All final lines, including the open sentence continuing on122, were read.')
],'Both complete scan parts and all margins read. Enlarged overtyped words, depth subscript, cancelled groups, marginal reference, set glyphs and complete bottom note inspected. Every insertion attachment, arrow, restriction, index and local cancellation was compared; malformed insertion encodings were corrected without changing their visible wording.')
_122_original=source_path('ega25_25_122').read_text().splitlines()
finish_reviewed(122,[
*[(n,_122_original[n-1],_122_original[n-1][9:-1],'This line lies under the long crossing diagonals, including an arrow-like terminal. The ink does not establish deletion as their unique function; remove the outer deletion scope while retaining all local cancellations and recording the graphic marks.') for n in range(22,39)],
(8,"l'ensemble Ø",r"l'ensemble $\hand{\unsure{\psi|\emptyset}}$",'The set symbol is the forked-stemmed pen form, with its alphabetic identity still uncertain.'),
(9,r'$P_{\unsure{\bar{k}}}$',r'$\unsure{\overline{P}|P}_{\bar{k}}$','The bar over the subscript k is clearly visible. P carries a small extra upper stroke and crossed bowl, so a decorated/plain P ambiguity remains explicit.'),
(10,r'\inserted[typed]{lorsque les anneaux locaux de X sont factoriels.}','', 'This typed replacement is placed immediately after En effet by its position above the cancelled opening, rather than at the end of the preceding paragraph.'),
(12,r'En effet,',r'En effet, \inserted[typed]{lorsque les anneaux locaux de X sont factoriels.}','Restore the typed replacement at its visible attachment after En effet.'),
(12,r'X étant régulier, X en est de même de \unsure{X $X_S$}',r'X étant régulier, \unsure{il|X} en est de même de \unsure{$X\times_S P$}','The cancelled opening after the comma is obscured and permits il/X. The following product has a visible subscript S and final P; the whole product remains doubtful beneath cancellation.'),
(14,r'X\unsure{x}P',r'\unsure{$X\times_S P$}','The final factor P and a subscript S survive within the crossed product; all of this cancelled product remains explicitly uncertain.'),
(18,r'\deleted{\unsure{un Mémoire inédit lorsque n° ultérieur}}',r'\deleted{\unsure{un Mémoire} \illegible{1} \unsure{dans un} n° \unsure{ultérieur}}','The horizontal pen strike obscures the middle wording. The visible connector supports dans un rather than lorsque, and n° is clear; the remaining candidate words and unreadable group stay marked.'),
(22,'La proposition',r'\margin{\unsure{$\times\quad\times\quad\nearrow$}}La proposition','Represent the long crossing diagonals and arrow-like terminal graphically, with their editorial function unresolved.'),
(23,r'D \quad Ø',r'$D\quad\hand{\unsure{\phi|\emptyset}}$','The first lower set glyph is an oval-stemmed pen symbol; the blank before it remains blank.'),
(28,r'D \quad Ø',r'$D\quad\hand{\unsure{\phi|\emptyset}}$','The second lower set glyph repeats the oval-stemmed pen form, again without a membership sign in the gap.'),
(29,r'\inserted[typed]{can isomorphe à} \hand{)}','', 'The typed replacement can isomorphe à belongs before the live la restriction on the following line. The right-hand curve is its placement connector, not a literal closing parenthesis.'),
(30,r'\xout{autre que} la restric-',r'\xout{autre que} \inserted[typed]{can isomorphe à} la restric-','The interlinear phrase attaches immediately before la restriction; all three words are typed.'),
(32,r'\xout{\unsure{n°1}}',r'\xout{n°1}','The cancelled number and degree sign are readable beneath the x impressions.'),
(34,r'do\unsure{ç}c',r'do\unsure{n|ç}c','The overtyped character has an n shoulder and a hooked lower stroke; retain both candidates.'),
(34,r'\unsure{prolongeant|prolongeaant}','prolongeant','The enlarged word has a single a position after ge; no second a occupies a separate typewriter position.'),
(35,r'\underline{O}_{\unsure{P}}',r'\underline{O}_{\overset{\hand{\unsure{\vee|/}}}{P}}','P itself is clear. A faint pen tick above it can be an incomplete dual V or a slash-like mark, so only the decoration remains uncertain.')
],[
(5,'Foliation','25 above;122 below','confirmed','Both manuscript and archive numbers were read directly.'),
(7,'Spelling','systêmes; rationelles; later systême and suurs','confirmed','The visible spellings and accents are preserved.'),
(9,'NOTES: handwritten continuation','sur barred k ne se factorisent par aucun hyperplan de P with barred-k subscript','confirmed','Every word, both bars over k and the final period were read in an enlargement. The extra mark on P remains uncertain.'),
(12,'NOTES: upper deletion','Typed x cancellation plus several looping pen strokes and a lower horizontal strike','confirmed','The bounded cancellation runs from X étant régulier through the codimension phrase. It is retained independently of the lower diagonal marks.'),
(14,'NOTES: word before de les','An obscured short cancelled group','retained_illegible','Even enlarged, the remaining impressions do not yield a secure word; the illegibility marker remains.'),
(15,'NOTES: codimension relation gap','codim(X-U,X), blank,2','confirmed','No comparison sign is supplied in the visible blank.'),
(19,'Auslander–Buchsbaum reference','Typed Chap III phrase cancelled;pen cf section20','confirmed','The local cancellation, replacement and all surrounding letters were read. The slash-like stroke within anneau is retained without assigning a lexical function.'),
(22,'NOTES: lower block marks','Several long crossing diagonals;lower-right arrow-like terminal','retained_uncertain','The marks were traced across the whole block. Their function remains unresolved, so the full body is retained and its former blanket deletion status removed.'),
(23,'NOTES: two D-to-set gaps','No membership sign in either blank','confirmed','Both visible spaces are preserved despite the neighboring set glyphs.'),
(27,'Formula L_U superscript x = f(O_P(1))','Typed superscript x and no raised pullback star after f','confirmed','Both positions were inspected; no mathematical symbol is supplied.'),
(27,'Right edge','interprétation punctuation clipped;constructio at the next edge','confirmed','Only the supplied visible characters are retained, with no completion of the cut word.'),
(30,'Older cancelled text','l’image inverse de L and n prime/autre que cancellations','confirmed','The underlying words and the retained ou presque phrase were read individually.'),
(31,'NOTES: dual marks','Small pen V over both P occurrences','confirmed','Their shapes and placements in U times_S P and X times_S P were inspected.'),
(35,'NOTES: isomorphism gap','L tensor O_P(1), blank,N','confirmed','No relation sign is visible in the gap; it remains blank.'),
(36,'NOTES: final formula gaps','L, blank,pr_1(N),semicolon','confirmed','The formula has no equality, direct-image subscript or other connecting sign added by the typist; the spaces remain.'),
(38,'Final text and margins','suurs D.;long marks;otherwise blank lower margin','confirmed','The last word, full stop, all pen terminals and remaining blank space were inspected.')
],'Both complete scans and all margins read. Enlarged handwritten qualification, upper typed cancellations, cancelled hand reference, donc/prolongeant and faint P decoration inspected. Every line of the lower paragraph remains recorded; the long diagonal marks have unresolved function, while local cancellations and all absent relation signs are preserved.')
finish_reviewed(123,[
(11,r"\unsure{\check{P}}$ l'étant.",r"\check{P}$ l'étant\unsure{,|.}",'The final target is a handwritten P with a V above it; no X-shaped target remains. The terminal punctuation is a small falling stroke, compatible with comma or point.'),
(11,r"\deleted{En effet,} d'après",r"\deleted{En effet,}\hand{et,} d'après",'A small handwritten et and comma appear immediately after the cancelled En effet; the draft omitted them.'),
(11,r'\over{nº2}{\unsure{\S 20.3}}',r'\over{nº2}{\S 20.3}','The pen section sign and digits20.3 are readable over and to the right of the typed reference.'),
(12,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent on the first body product is handwritten.'),
(13,r'\check{P}',r'\overset{\hand{\vee}}{P}','The next product has a handwritten dual accent.'),
(14,r'\phi',r'\hand{\phi}','The symbol defining the regular section is handwritten.'),
(15,r'\check{P}',r'\overset{\hand{\vee}}{P}','The parameter P has a pen dual accent.'),
(16,r'\phi_t',r'\hand{\phi}_t','The first phi in condition1 is pen; its index t is typed.'),
(16,r't\in\check{P}',r't\hand{\in}\overset{\hand{\vee}}{P}','The membership and dual accent in the parameter condition are handwritten.'),
(16,r'par $\phi$',r'par $\hand{\phi}$','The next phi in condition1 is handwritten.'),
(16,r'$Xs_S\check{P}$',r'$Xs_S\overset{\hand{\vee}}{P}$','The dual accent on the product is pen; the visible typed s after X is retained.'),
(16,r'au dessus de $\check{P}$',r'au dessus de $\overset{\hand{\vee}}{P}$','The final dual accent in this line is handwritten.'),
(17,r'\phi',r'\hand{\phi}','The phi in the regularity parenthesis is handwritten.'),
(17,r'x\in X',r'x\hand{\in} X','The membership in condition2 is handwritten.'),
(18,r'\xout{xxxx}',r'\xout{sont}','The underlying word sont is readable beneath the typed cancellation.'),
(18,r'\check{P}',r'\overset{\hand{\vee}}{P}','The product has a pen V above P.'),
(19,r"d'un $\underline{N}$",r"d'un $\underline{\unsure{N|E}}$",'This underlined capital is heavily overtyped and contains both N- and E-like strokes; it remains uncertain.'),
(19,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent in the projective-bundle phrase is handwritten.'),
(23,r'\simeq',r'\hand{\simeq}','The displayed isomorphism sign is handwritten.'),
(23,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual accent in the display is handwritten.'),
(24,r'\simeq',r'\hand{\unsure{\simeq|\longrightarrow}}','The connector has two short left strokes and a heavy right terminal; isomorphism sign and arrow readings cannot be cleanly separated.'),
(24,r'pr_{1*}',r'pr_{1\hand{*}}','The direct-image star is handwritten, while pr and1 are typed.'),
(25,r'\check{P}',r'\overset{\hand{\vee}}{P}','The P of O_P(-1) has a handwritten dual accent.'),
(25,r'\phi',r'\hand{\phi}','This phi is handwritten.'),
(26,r'\check{P}',r'\overset{\hand{\vee}}{P}','The next O_P(1) has a pen dual accent.'),
(28,r'pr_{1*}',r'pr_{1\hand{*}}','The first direct-image star in the crowded line is handwritten.'),
(28,r'\underline{O}_{\hand{$X\times_S\check{P}$}}',r'\underline{O}_{\over{P}{\unsure{X\times_S\check{P}}}}','The first circled index has a visible old typed P and a crowded pen product correction. Its reading remains uncertain; the old layer is retained and the nested dollar encoding is removed.'),
(28,r'\unsure{pr}_*',r'\unsure{\over{pr}{\illegible{1}}|pr}_{\hand{*}}','The pr-like group is overwritten by pen strokes that do not yield a secure replacement. The star is clearly pen.'),
(28,r'\underline{O}_{\hand{$\check{P}$}}',r'\underline{O}_{\unsure{\over{X\times_S P}{\check{P}}}}','The second circled index contains crossed product-like characters and a pen P correction. The ordering of its layers is uncertain, so the complete old/new candidate remains marked.'),
(28,r"\deleted{\xout{xx$\underline{L}$x$\otimes$xx$\underline{E}$xxxi.e.xxd'unxhomomorphisme}}",r"\deleted{\xout{$\unsure{=}\underline{L}\otimes_{\underline{O}_S}\overset{\hand{\unsure{\vee}}}{\underline{E}}$ i.e. d'un homomorphisme}}",'The cancelled expression contains a readable O_S tensor subscript omitted by the draft. L, tensor, E and the following words are readable; the initial equality and small upper mark on E remain uncertain.'),
(29,r'\deleted{\xout{$\underline{E}$x$\underline{E}$xxxx$\otimes$}}',r'\deleted{\xout{$\underline{\unsure{E|R}}$ $\underline{E}$ \illegible{1} $\otimes$}}','The first underlined capital has a bowl and lower leg beneath cancellation, allowing E/R; the second E and final tensor sign are readable. The intervening group remains obscured.'),
(29,r'\unsure{pr}_*',r'\unsure{\over{pr}{\illegible{1}}|pr}_{\hand{*}}','The next pr-like operator is likewise overwritten by pen, with an unreadable replacement and a clear pen star.'),
(29,r'\check{P}',r'\overset{\hand{\vee}}{P}','The product index has a pen dual accent.'),
(29,r'\simeq',r'\hand{\simeq}','The following isomorphism sign is handwritten.'),
(29,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The V over E is handwritten; its X index is typed.'),
(30,r'\phi',r'\hand{\phi}','The final phi in this argument is handwritten.'),
(30,r'\xout{xxxx}',r'\xout{un h}','The underlying cancelled group reads un h, with all three letters visible beneath the x marks.'),
(30,r'g^*(\underline{E})\to',r'g^{\hand{*}}(\underline{E})\hand{\to}','Both the raised pullback star and the following arrow are handwritten.'),
(31,r'\inserted{u:}',r'\inserted[typed]{u:}','The interlinear u and colon have typewriter forms; the attachment curve is pen.'),
(31,r'\underline{E}\to g_*(\underline{L})',r'\underline{E}\hand{\to} g_{\hand{*}}(\underline{L})','The arrow and direct-image star are handwritten.'),
(31,r'$g:X\to S$',r'$g:X\hand{\to} S$','The arrow defining g is handwritten.'),
(35,r'\check{P}',r'\overset{\hand{\vee}}{P}','The last dual accent on the page is handwritten.')
],[
(5,'Foliation','26 above;123 below','confirmed','Both numbers and all surrounding margins were read.'),
(7,'NOTES: heading number','Handwritten4 over typed7','confirmed','The old horizontal/diagonal7 and added4 strokes remain distinguishable.'),
(11,'NOTES: complete top insertion','Nous pouvons supposer évidemment dual P to S surjectif;Alors X times_S dual P to dual P l’étant','confirmed','Every word and all three P positions were read in the enlarged insertion. Its long bracket attaches before the cancelled En effet.'),
(11,'NOTES: tick between en and termes','Raised V of the first P in the inserted note','confirmed','Its alignment with the handwritten P below identifies its position within the insertion; no separate textual tick is added.'),
(14,'Cancelled En ver','Partly readable En ver with terminal cancellation','retained_uncertain','The candidate remains compatible with the underlying letters; no continuation to vertu is supplied.'),
(16,'Printed product','Xs_S P with a pen dual accent','confirmed','The typed s after X is visible and retained.'),
(19,'Overtyped le','Crowded first letter of le','retained_uncertain','The original uncertainty remains; the glyph is not normalized.'),
(23,'NOTES: tensor base','Overprinted S/X index','retained_uncertain','Both outlines remain visible in the enlarged formula.'),
(25,'NOTES: la/le insertion','Looped l and small closed terminal','retained_uncertain','The second letter does not securely distinguish a from e; both candidates remain.'),
(27,'NOTES: marginal formula','O indexed by X times_S dual P, followed by(1)','confirmed','The entire handwritten marginal formula, underline and index were read.'),
(28,'NOTES: circled formulas','Two index corrections with overlapping old and new layers','retained_uncertain','The circles enclose corrections rather than deleting the whole formulas. Their old/new readings remain explicitly uncertain.'),
(29,'Reference','III2','confirmed','The printed chapter and number are clear and retained.'),
(34,'NOTES: final comma','Pen comma at the right edge after fibre','confirmed','The falling stroke is visible even though close to the crop.'),
(36,'Final field expression','E(s) tensor over k(s) k','confirmed','E is plain at this occurrence; every parenthesis and index was read.')
],'Both full scan parts and all margins read. Enlarged top insertion, reference correction, et addition, cancelled phrases, all three crowded operator/index expressions and the marginal formula inspected. Every phi, dual accent, membership, arrow, tensor base and direct/pullback star was checked. Old/new layers and ambiguous connector shapes remain marked.')
finish_reviewed(124,[
(7,r't\in E(s)',r't\hand{\in} E(s)','The membership sign in the opening condition is handwritten.'),
(8,'la section',r'la \unsure{se}ction','The initial s/e pair is overtyped and partly merged; the supported se reading remains marked.'),
(8,'régulière',r'\unsure{ŕ|é}égulière','The first character contains r/e-like overtyping and a separate acute stroke above it, followed by the next accented e. The double accent positions are preserved instead of normalizing the word.'),
(10,r'\unsure{\over{ha}{h}}',r'\over{\unsure{ah|ha}}{\unsure{ha|h}}','Two typed letter positions and overlapping pen h/a-like strokes are visible. The underlying order and the exact scope of the pen correction remain uncertain.'),
(12,'Soit',r'Soi\deleted{\unsure{a}}\hand{t}','After Soi a dark pen-covered a-like impression remains, followed by a separate clearly handwritten t. Both layers are retained.'),
(12,r'$g:X\to S$',r'$g:X\hand{\to} S$','The structural arrow in the proposition is handwritten.'),
(17,r'\underline{E}\to g_*(\underline{L})',r'\underline{E}\hand{\to} g_{\hand{*}}(\underline{L})','The arrow and the direct-image star defining u are handwritten.'),
(18,r's\in S',r's\hand{\in} S','This membership sign is handwritten.'),
(19,r'k\unsure{(s)}',r'k\unsure{\over{(s)}{\illegible{1}}}','The parenthesized group carries a heavy lower pen retouch. The typed(s) reading remains possible, but the overlying pen group is unreadable.'),
(20,'la section','la sedtion','The enlarged third letter has the upright ascender and bowl of typed d. The scanned spelling sedtion is restored.'),
(24,r's\in S',r's\hand{\in} S','The lower membership sign is handwritten.'),
(24,r'\rightarrowtail',r'\hand{\rightarrow}','The enlargement shows a plain rightward pen arrow starting at the closing parenthesis of E(s); there is no separate tail glyph.'),
(25,r'\deleted{\unsure{et}}',r'\deleted{\unsure{et|ou}}','The pen-cancelled two-letter group also permits ou; its upper crossing strokes do not distinguish the alternatives securely.'),
(27,r'\unsure{\overset{\hand{\vee}}{P}}',r'\overset{\hand{\vee}}{P}','The enlarged subscript shows a clear typed P and a separate two-stroke pen V; this occurrence is resolved.'),
(29,r'\longrightarrow',r'\hand{\longrightarrow}','The arrow defining f in the corollary is handwritten.'),
(34,r'\xrightarrow{\ \sim\ }',r'\hand{\xrightarrow{\ \sim\ }}','The displayed arrow and its upper tilde are handwritten.'),
(34,r'g_*(\underline{L}',r'g_{\hand{*}}(\underline{L}','The direct-image star in the last formula is handwritten.')
],[
(5,'Foliation','27 above;124 below','confirmed','Both page numbers and the complete margins were inspected.'),
(7,'Opening spelling','condition e’exprime','confirmed','The first letter is e as printed; it is retained.'),
(8,'Opening section argument','u(s)','confirmed','The parenthesized character is visibly s, while the later statement has u(t); neither occurrence is changed to match the other.'),
(10,'NOTES: habitude correction','Overlapping typed and pen letters before bitude','retained_uncertain','The enlarged correction does not settle both layers or justify a normalized spelling.'),
(12,'NOTES: revised proposition number','Hand4 over typed5;unchanged .1','confirmed','The old and added numeral strokes are distinct.'),
(13,'Base of projective bundle','P=P(E),un fibré projectif sur X','confirmed','The printed base is X; it is preserved without mathematical substitution.'),
(14,'NOTES: marginal qualification','partout not-equal0 i.e.P à fibres non vides','confirmed','Every handwritten word and sign was read; the bracket lands immediately after fini. The following dual accents and comma are pen.'),
(19,'NOTES: field extension insertion','Handwritten k after conque;separate margin point','confirmed','The k and its attachment are clear; the separate point remains represented in the margin.'),
(22,'Cancelled fibre condition','(S_1) et géom irréd','confirmed','All letters, index1 and parentheses remain readable beneath typed cancellation.'),
(24,'Injection formula','u(s):E(s) to H^0(X_s,L_s)','confirmed','Exponent0, both s indices and all arguments were inspected.'),
(25,'NOTES: revised internal reference','Hand4 over typed5 in4.1','confirmed','The same numeral change is visible independently of the proposition heading.'),
(27,'Inserted section symbol','Pen phi attached after évidente by a forked placement sign','confirmed','The symbol and both attachment strokes were read; the following tensor base is O_S.'),
(29,'NOTES: revised corollary number','Hand4 over typed5 in4.2','confirmed','The old and new digits are visible; the following2 is typed.'),
(29,'NOTES: right edge','présentati followed by a faint short hyphen','confirmed','The cut line-ending stroke remains visible and is retained.'),
(30,'Printed spelling','géométriquemeht','confirmed','The h is printed at the penultimate consonant position and remains unchanged.'),
(31,'Unrevised internal reference','comme dans5.1.','confirmed','This reference has no handwritten4 correction and is retained as5.1.'),
(34,'Structural map in corollary and formula','f in the hypothesis;g star in the display','confirmed','Both printed letters were read and preserved.'),
(35,'Final continuation','systêmes linéaires de diviseurs sur X paramétrés','confirmed','The full last line and its cancellation of familles were inspected; the sentence continues on125.')
],'Both complete scan parts and all margins read. Enlarged overtyped opening words, habitude/Soit corrections, k(s) retouch, sedtion, injection arrow, cancelled hand word and dual P inspected. Every numeral revision, index, arrow, star and marginal qualification was checked. Printed e’exprime, u(s), sur X, géométriquemeht,5.1 and the f/g variation remain preserved.')
finish_reviewed(55,[
(9,r'n > 0',r'n \hand{>} 0','The opening greater-than sign is handwritten.'),
(10,r'P \to P(n)',r'P \hand{\to} P(n)','The immersion arrow is handwritten.'),
(11,r'p_*(\underline{O}_P(n))',r'\unsure{p|f}_{\hand{*}}(\underline{O}_P(n))','The operator letter is typed over another f/p-like impression; the star is a separate pen addition.'),
(12,r'P \to S',r'P \hand{\to} S','The structural arrow defining p is handwritten.'),
(12,r'S\xout{o}i\xout{t}',r'S\deleted{o}i\deleted{t}','The old o and t are obscured by thick irregular pen strokes, rather than rows of typed x marks.'),
(12,r'X\to P',r'X\hand{\to} P','The arrow defining f is handwritten.'),
(13,r'X \to P(n)',r'X \hand{\to} P(n)','The composed-map arrow is handwritten.'),
(14,r'\xout{\unsure{f}}',r'\deleted{\unsure{f}}','The final small f-like group is crossed by thick pen strokes; its reading remains uncertain.'),
(17,r'\xout{\unsure{lexmorp}}',r'\xout{le morp}','The underlying letters read le morp; the interword x belongs to the cancellation.'),
(17,r'\longrightarrow',r'\hand{\longrightarrow}','The arrow from the singular locus is handwritten.'),
(17,r'\overset{\hand{$\vee$}}{X}',r'\overset{\hand{\vee}}{\unsure{P|R|X}}','The target capital has an upper bowl and crossed lower strokes, compatible with P/R/X; its pen dual accent is clear. The draft’s certain X is not supported by the overprinted glyph.'),
(18,r'\xout{estxunxmorphismexinsépa}',r'\xout{est un morphisme insépa}','All underlying words and the cut fragment insépa are readable; x impressions are cancellation marks.'),
(20,'dimension impaire',r'dimension i\unsure{m}paire','The m position is overtyped beneath the long pen cancellation; the surrounding letters are clear.'),
(24,r'X\to P',r'X\hand{\to} P','The arrow in Proposition9.2 is handwritten.'),
(25,r'n \geq 2',r'n \hand{\geq} 2','The lower bound on n is handwritten.'),
(25,r'X \to P(n)',r'X \hand{\to} P(n)','The second arrow in the proposition is handwritten.'),
(27,r'\hand{$\xi \in$}',r'\hand{$\unsure{\xi|\zeta} \in$}','The long hooked pen point symbol admits xi/zeta readings; its membership sign is clear.'),
(27,r'\geq 2',r'\hand{\geq} 2','The codimension comparison is handwritten.'),
(28,r'Y_{\hand{$\xi$}}',r'Y_{\hand{\unsure{\xi|\zeta}}}','The section index repeats the hooked pen symbol; its alphabetic uncertainty is preserved.'),
(30,r'\xout{plusxunxseulxpointxnonxlissex}',r'\xout{plus un seul point non lisse}','The cancelled phrase is readable word by word; its x marks are not literal text.'),
(30,'lesquels sont',r'l\unsure{es}quels \unsure{son}t','The first e/s pair and the son group are merged by typewriter overprinting; the supported letters remain marked.'),
(31,r'\xout{etxrationnelsxsurxk(xx)x}',r'\xout{et \unsure{rationnel|rationnels} sur k(\illegible{1})}','The words et, sur and k parentheses are readable, but the final number of rationnel and the cancelled argument remain obscured.'),
(32,r'\hand{$\xi$}',r'\hand{$\unsure{\xi|\zeta}$}','The field argument repeats the same uncertain pen point symbol.')
],[
(5,'Foliation','50 above;55 below','confirmed','Both handwritten page numbers and full margins were inspected.'),
(9,'Symmetric-power notation','First E plain;following displayed E underlined','confirmed','The different visible underline layers are retained.'),
(12,'NOTES: missing equality','No equality before Sym^n(E)','confirmed','The line starts with the symmetric-power expression; no relation sign is supplied.'),
(14,'Cancelled au','Readable au under cancellation','confirmed','Both old letters were inspected.'),
(15,'Cancelled général and later gênant','Both words readable','confirmed','The first is cancelled; the second remains live with its printed accent.'),
(17,'Cross-reference','8.12.b)','confirmed','Every digit and the parenthesis were read.'),
(20,'NOTES: quadric revision','Local pen deletion through r=2m+1;hand dans P^3','confirmed','The full cancelled dimension phrase and the replacement placement after it were read; its mathematical wording is preserved.'),
(26,'Reference and spelling','condition équivalentes de8.8','confirmed','The singular condition and printed reference remain unchanged.'),
(28,'NOTES: n prime insertion','Pen n apostrophe between ou and admet','confirmed','The curved attachment and both characters were inspected.'),
(29,'Typed inserted line','nombre fini de points non lisses,','confirmed','The entire interlinear phrase is typed and replaces the following cancelled condition.'),
(33,'NOTES: cancelled word after façon à','éviter candidate beneath dense typed x marks','retained_uncertain','Magnification does not separate every underlying letter; the original candidate remains marked.'),
(33,'NOTES: marginal double stroke','Two long pencil strokes beside the NB continuation','confirmed','Their full extent from the NB block to the last line was inspected.'),
(34,'NOTES: vérifiaation/vérification','Overtyped a/c position','retained_uncertain','Both source candidates remain compatible with the merged character.'),
(35,'Internal references','8.8(ii bis) and9.1','confirmed','The condition label and paragraph reference were read directly.'),
(37,'Final continuation','Sections of X by degree-hypersurfaces;sentence continues','confirmed','All final words, punctuation and the bottom edge were inspected.')
],'Both complete images and every margin read. Enlarged p/f operator, pen-cancelled Soit, final f-like mark, le morp, overtyped dual target, impaire, point glyphs, les/son overprints and cancelled concluding phrases inspected. All arrows, indices, comparisons, insertion paths and references were checked; no missing equality or mathematical correction was supplied.')
finish_reviewed(56,[
(7,r'\xout{\illegible{1}}',r'\xout{secti\unsure{o|n}}','The enlarged cancellation reveals s-e-c-t-i; the final rounded two-stroke letter permits o or n. No further letter is supplied.'),
(9,r'\xout{xx} Supposons',r'\xout{et} Supposons','Both underlying letters e and t remain legible.'),
(9,r'\inserted{X géom irréd et}',r'\inserted[typed]{X géom irréd et}','Every inserted letter has a typewriter outline; the surrounding attachment curve is pen.'),
(9,r'$\geq$ 2,',r'$\hand{\geq}$ \unsure{2},','The comparison is pen. The following digit is overprinted and retains a supported but uncertain 2 reading.'),
(9,r'\xout{xx} soit',r'\xout{et} soit','The cancelled word is readable as et.'),
(9,r'x$\in$X(k)',r'x$\hand{\in}$X(k)','The membership sign is a separate curved pen glyph.'),
(9,r'\xout{xx}',r'\xout{et}','The last cancellation on the proposition line also exposes e and t.'),
(10,r'\xout{xxxx} a)',r'\xout{\unsure{soit}} \inserted[typed]{a\hand{)}}','The cancelled group supports soit but its first letter remains obscured. The raised a is typed, and its heavy closing parenthesis is pen.'),
(10,r'n$\geq$2',r'n$\hand{\geq}$2','The enlarged cancelled clause contains a handwritten greater-or-equal sign; its short lower stroke is separate from the long cancellation.'),
(10,r'\over{ant}{ons}',r'\over{a}{o}n\over{t}{s}','The pen corrections lie over a and t; the intervening n remains typed.'),
(12,r'\xout{xxx}',r'\xout{est}','The underlying e-s-t can be read beneath the cancellation.'),
(12,r'\hand{\xi}',r'\hand{\unsure{\xi|\zeta}}','The long hooked pen index admits xi and zeta readings, as on the preceding page.'),
(14,r'$\bar{k}$',r'$\overset{\hand{\scriptscriptstyle -}}{k}$','The bar over the cancelled typed k is handwritten.'),
(14,r'n$\geq$2',r'n$\hand{\geq}$2','The comparison in the cancelled hypothesis is handwritten.'),
(15,r'\xout{\unsure{ou si n$\geq$3,}}',r'\xout{ou si n$\hand{\geq}$3,}','The enlarged old clause yields ou si n, the handwritten comparison, and 3 with comma.'),
(16,r'n$\geq$2',r'n$\hand{\geq}$2','The comparison in the second pen-cancelled clause is handwritten.'),
(16,r'\over{ant}{ons}',r'\over{a}{o}n\over{t}{s}','The second ending again has pen o over a and s over t, with the n left typed.'),
(16,r'\inserted{(linéaire)}',r'\inserted[typed]{(linéaire)}','The second parenthetical insertion is typewritten; its bracket of attachment is pen.'),
(17,r'\xout{\illegible{1}} $f_n$',r"\xout{\unsure{l'immer}} $f_n$",'The cancelled prefix is compatible with l apostrophe immer; its first letters remain partly merged with the x marks.'),
(17,r'$f_n$ \xout{\illegible{1}}',r'$f_n$ \xout{qui pa}','The following cancellation clearly exposes qui pa; no completion is supplied.'),
(18,r'\xout{\illegible{1}}',r'\xout{contenant}','Every letter of contenant can be read beneath the x row.'),
(19,r'\inserted{sur L}',r'\inserted[typed]{sur L}','The inserted words are typed and the pen bracket attaches them immediately before s’annulent.'),
(20,r'\hand{\xi}',r'\hand{\unsure{\xi|\zeta}}','This handwritten section index repeats the uncertain hooked point glyph.'),
(22,r'\xout{etxfxxxx}',r'\xout{et f non}','The underlying cancelled words read et f non.'),
(22,r'n$\geq$3',r'n$\hand{\geq}$3','The greater-or-equal comparison in c is handwritten.'),
(23,r'\hand{\xi}',r'\hand{\unsure{\xi|\zeta}}','The index has the same unresolved xi/zeta form.'),
(25,r'\hand{\xi}',r'\hand{\unsure{\xi|\zeta}}','The last section index on the page again repeats that pen form.'),
(29,r'\xout{xxx}',r'\xout{une}','The underlying u-n-e are readable in the enlarged cancellation.'),
(30,r'$T_1,..,T_r$',r'$\unsure{T|X}_1,..,\unsure{T|X}_r$','Both coordinate capitals show a T-shaped upper bar with crossed X-like lower strokes; the overprinted letter layers remain uncertain.'),
(35,r'\unsure{c)}',r'\unsure{c|b})','The overtyped clause label contains a c bowl and a second stem compatible with b; the parenthesis itself is clear.'),
(37,r'\xout{\illegible{1}}',r'\xout{seulement}','All letters of seulement are readable beneath the cancellation.')
],[
(5,'Foliation','51 above;56 below','confirmed','Both handwritten numbers and the complete margins were inspected.'),
(9,'NOTES: bold2','Overprinted digit after dim f(X) comparison','retained_uncertain','The visible outline supports2 but does not securely recover the earlier impression.'),
(9,'NOTES: Soit n greater-or-equal2','Handwritten insertion attached after X(k),','confirmed','All characters and both arms of the long attachment bracket were followed to the comma.'),
(10,'NOTES: first Considérons','Pen C and two corrected ending letters','confirmed','The enlarged old and new letter strokes were compared separately.'),
(10,'First linear insertion','Handwritten(linéaire)','confirmed','Both parentheses, the accent and the placement after famille were read.'),
(12,'Cancelled intègre','Readable word crossed by typewriter x marks','confirmed','The cancellation mode and all underlying letters were checked in the enlarged crop.'),
(14,'NOTES: cancelled b hypothesis','Si f(X) n’est pas contenu dans un plan défini sur barred k,et n comparison2,','confirmed','The full cancelled line, final comma and the following continuation were read.'),
(16,'NOTES: second Considérons','Pen C and corrected a/t positions','confirmed','The second correction was inspected independently of the first.'),
(17,'Printed agreement','sections hyperplanes...définis','confirmed','The masculine ending remains as printed.'),
(19,'n-formes insertion','Handwritten n and hyphen','confirmed','The forked caret attaches immediately before formes.'),
(20,'définit/est revision','Pen-cancelled définit and hand est above it','confirmed','Both layers and the attachment position were read.'),
(22,'NOTES: c insertion','ou f(X) pas contenu dans un plan défini sur barred k.','confirmed','Every handwritten word, both formula parentheses, the bar and the terminal point were inspected; the bracket attaches after n comparison3,.'),
(23,'NOTES: tangentielles','Cancelled handwritten word above génériques','retained_uncertain','The horizontal stroke obscures internal letters; the existing candidate remains marked.'),
(24,'NOTES: punctuation after en x','A heavy falling comma over the point position','retained_uncertain','The comma is visible but the underlying point cannot be separated securely; the over-period candidate remains uncertain.'),
(24,'Handwritten quotation marks','Two pen marks before tangentes and two after x','confirmed','Their position relative to the underline and comma was checked.'),
(24,'Printed wording','de ladite followed by définit on next line','confirmed','No missing noun is supplied between the two printed lines.'),
(30,'NOTES: degree comparison','Handwritten less-or-equal over a dense ink blot','retained_illegible','The upper angle and lower stroke were inspected; the underlying character remains unreadable.'),
(31,'Rational expressions','Q(t)/P(t) and R(t)/P(t)','confirmed','Every letter, parenthesis and slash was compared with the scan.'),
(32,'Coordinate tuple','t=(t_1,..,t_r)','confirmed','The lower-case coordinates and all indices were read separately from the overprinted capitals above.'),
(35,'Linear equations','T_1,..T_s=0','confirmed','These later T capitals are clear; their indices, equality and zero remain unchanged.'),
(37,'NOTES: final degree','Handwritten3 in a typed blank','confirmed','The single digit and surrounding degree phrase were read.'),
(37,'Final insertion','Handwritten éventuellement before de prendre','confirmed','The complete word and curved attachment were inspected.')
],'Both complete images and all margins read. Enlarged every dense cancellation, both corrected Considérons endings, the overprinted numeral and coordinate capitals, the cancelled tangentielles, punctuation, degree comparison and clause label. All section indices, comparisons, typed/pen insertion layers and attachment points were checked; unresolved old letter layers remain marked.')
finish_reviewed(57,[
(5,r'\unsure{92}',r'\unsure{52|92}','The surviving lower hook of the first folio digit permits5 as well as9; its top is clipped. The second digit2 is clear.'),
(7,r'\geqslant',r'\hand{\geqslant}','The first dimension comparison is handwritten.'),
(8,r'\geqslant',r'\hand{\geqslant}','The transcendence-degree comparison is handwritten.'),
(10,r'\xout{\unsure{mais en ayant soin de prendre} \unsure{$t_1$}}',r'\xout{mais en ayant soin de prendre $t_1$}','The enlarged cancellation exposes every word and the final t with lowered1.'),
(11,r'\not\subset',r'\hand{\not\subset}','The noncontainment glyph after f(X) is pen, including its diagonal stroke.'),
(16,"par f de",r"par \over{\unsure{f}}{f} de",'The visible f is handwritten over a dark typed impression compatible with f; the old letter remains uncertain.'),
(23,r'\inserted{si dim L $=2$} ',r'','The insertion’s bracket lands after the opening parenthesis before prendre on the next line, not before évidamment.'),
(24,'( prendre',r'( \inserted{si dim L $=2$} prendre','The entire si dim L=2 note belongs at the visible attachment immediately before prendre.'),
(25,r'$Q/P = T_r$',r'$\unsure{Q}/\unsure{P} = T_r$','Both letters in the quotient are overprinted; Q and P remain supported readings but their earlier impressions cannot be separated.'),
(26,r'$T_{r-2}$, $T_{r-1}$, $T_r$ lin.',r'$T_{r-2}$, $T_{r-1}$, $T_r$ sont lin.','The rotated upper margin reveals the omitted handwritten sont after the last coordinate.'),
(26,r'$Q=\unsure{T_{r-1}^{\,2}}$',r'$Q=T_{r-1}^{\,2}$','The rotated note clearly shows Q equal to T with lower r-1 and raised2.'),
(26,r'$R=\unsure{T_{r-2}^{\,2}}$}',r'$R=T_{r-2}^{\,2}$.}','The corresponding R formula clearly has lower r-2 and raised2, followed by a pen point.'),
(30,r'\unsure{8.181|8.18}',r'\unsure{8.181|8.18L|8.18}','The extra overtyped character has a long lower right foot compatible with L as well as the supplied1/stray-mark readings.'),
(36,r'\deleted{\uline{Théorème}}',r'\over{\uline{\unsure{Corollaire}}}{\uline{Théorème}}','The title contains a readable handwritten Théorème over a longer typed word compatible with Corollaire. This is an overwritten title; the old word remains uncertain.'),
(36,r'$f:X\to P$',r'$f:X\hand{\to} P$','The arrow in the final proposed statement is handwritten.'),
(37,r'\hand{\unsure{X}}',r'\hand{X}','The separate inserted X after ramifié is clear.'),
(37,r'\geqslant',r'\hand{\geqslant}','The dimension comparison in the final statement is handwritten.'),
(38,'non immersion',r'\unsure{non|une} \unsure{imm|immer}','The first short word has unresolved connected arches. The next word is visibly abbreviated after imm/immer; the full word immersion is not written.')
],[
(5,'Foliation and margin','Clipped upper number;57 in pencil below','confirmed','The complete page edges and both numbers were inspected; the upper reading remains explicitly doubtful.'),
(9,'Three explicit polynomials','P=T_1,Q=T_1 squared,R=T_1T_2','confirmed','Each variable, exponent,index and equality was read; the overprinted T outlines still support T.'),
(12,'Index variation','An index i between1 and s,followed by t_s','confirmed','The printed s indices in this and the following line were checked and preserved.'),
(14,'Cancelled degree clause','avec n=2 même au lieu de n=3,','confirmed','The full two-line clause is crossed by local horizontal pen strokes.'),
(16,'L insertion','Handwritten L after image','confirmed','The letter stands above the word boundary before par.'),
(16,'NOTES: long cancellation','ce qui exige...que X.','confirmed','The cancellation has continuous horizontal boundary strokes and linked side curves enclosing the whole passage, in addition to its diagonals; the full underlying text was read.'),
(18,'Internal typed cancellation','Lorsque dim X','confirmed','The nested typewriter cancellation is independently visible inside the pen-cancelled block.'),
(19,'Bracketed exceptional case','Pen opening bracket before Lorsque dim X=2 and closing bracket after irréductible)','confirmed','Both bracket strokes and the entire intervening explanation were inspected.'),
(21,'Printed spelling and agreement','formé;concourran-tes','confirmed','The masculine form and double-r spelling are retained.'),
(23,'Printed spelling','évidamment','confirmed','The visible vowel sequence remains unchanged.'),
(24,'NOTES: cancelled group after P formula','Dense x marks and overprinted strokes','retained_illegible','The underlying characters remain unreadable in the enlargement; no mathematical completion is supplied.'),
(25,'Explicit quotient identities','Q/P=T_r and R/P=T_(r-1)','confirmed','The overprinted numerator/denominator of the first quotient remain marked; all other displayed symbols are clear.'),
(26,'NOTES: marginal insertion','si dim L greater-or-equal3,alors T_(r-2),T_(r-1),T_r sont lin.indép.sur L et on prendra the three squared-coordinate expressions','confirmed','The rotated note was read across both scan parts, including the terminal point. Matching oblique strokes with dots attach it after alg ind.'),
(26,'Cancelled proposed remark','On pourrait signaler...dans un plan.','confirmed','The entire three-line remark is bounded and horizontally struck in pen; every underlying word was read.'),
(32,'Unfinished Corollaire9.4','Cancelled opening(Pour X propre sur k','confirmed','No statement follows the heading beyond this cancelled opening; nothing is completed editorially.'),
(34,'Internal cross-reference','9.2.','confirmed','All digits and punctuation were read.'),
(36,'Geometric-integrality insertion','Handwritten(et géom intègre)','confirmed','All words,parentheses and the attachment after propre were read.'),
(37,'NOTES: final handwritten addition','en signalant le résultat sur a pi-like symbol and question punctuation','retained_uncertain','Every readable word was checked; the original pi_1 candidate remains uncertain because the joined strokes and lowered mark are indistinct.'),
(38,'NOTES: last parenthesis','variété des pts singuliers de f-candidate','retained_uncertain','The words are readable, while the heavily retraced final f-like glyph remains doubtful.'),
(38,'Last arrow','X to P in the handwritten line','confirmed','The direction and the two capital letters were inspected.')
],'Both full scan parts and every margin read. Enlarged the cancelled opening phrase, polynomials, retouched f and Q/P, clipped folio, reference suffix, overwritten title and both final handwritten lines. The complete three-line vertical note was rotated and read across the two images. Clear bounded cancellations remain distinct from insertion brackets; unresolved old layers and abbreviated final wording remain marked.')
finish_reviewed(58,[
(11,r'\hand{(}\inserted[typed]{Supposons S=Spec(k),}\hand{)}',r'\inserted[typed]{Supposons S=Spec(k),}','The large curves connect the typed insertion to the position before On sait; they are attachment strokes, with no separate literal parentheses.'),
(11,r'\hand{\unsure{11}}',r'\hand{12}','The enlarged handwritten reference has a straight1 followed by the curved upper and angled lower strokes of2.'),
(13,r'\inserted{de choses}',r'\margin{$/$}\inserted{de choses}','The long pencil diagonal beside the upper paragraph is now explicitly represented; its full extent was inspected.'),
(13,r'\over{t}{ent}',r'\over{t}{\unsure{ent}}','The pen ending is compatible with ent, but the merged initial loop and old t prevent a fully secure separation.'),
(14,r'\xout{\illegible{1}}',r'\deleted{\unsure{et}}','The two old impressions support et beneath irregular pen loops and strokes, rather than a clean row of typed x marks.'),
(14,r'$\geqslant$',r'$\hand{\geqslant}$','The codimension comparison is handwritten.'),
(15,r'\xout{xxxxx}',r'\xout{et il}','The underlying letters and interword space of et il are legible.'),
(15,r'\overline{Z}',r'\overset{\hand{\scriptscriptstyle -}}{Z}','The bar above this Z is handwritten.'),
(16,r'\xout{xxxxxxxx}',r'\xout{\unsure{e|c}tte con}','The cancellation exposes t-t-e, a space and c-o-n after an uncertain initial e/c-like glyph; no missing prefix or completion is supplied.'),
(17,r'doite L dans',r'doite L \margin{\unsure{$-$|$\wedge$}}dans','A short pen stroke lies above the a of dans. Its flattened bar/circumflex shape and unresolved function are represented as a graphic note.'),
(18,r'\overline{Z}',r'\overset{\hand{\scriptscriptstyle -}}{Z}','The lower Z also has a handwritten bar.'),
(18,r"\hand{(}\inserted[typed]{de sections hyperplanes de X\hand{''}}\hand{)}",r"\inserted[typed]{de sections hyperplanes de X\hand{''}}",'The surrounding curves form one insertion bracket attaching after linéaire; the closing quotation marks are separate pen strokes.'),
(19,r'pré\unsure{s}chéma',r'prés\unsure{c|f}héma','The s is readable; the following position carries a c bowl and a taller f-like overlapping stroke.'),
(22,r'\hand{$\xi$}',r'\hand{$\unsure{\xi|\zeta}$}','The section index is the hooked pen point symbol whose xi/zeta reading remains unresolved.'),
(22,r'\hand{$\xi \in$}',r'\hand{$\unsure{\xi|\zeta} \in$}','The parenthetical point symbol has the same uncertain alphabetic form; its membership sign is clear.'),
(23,r'\deleted{deux}',r"\xout{\unsure{d'un|deux}}",'The old four-position group is crossed by typewriter x marks. Its middle strokes permit d apostrophe un as well as the draft’s deux reading.'),
(23,r'\hand{(}\inserted[typed]{où S est un}\hand{)}',r'\inserted[typed]{où S est un}','These curves are the attachment for the typed insertion before corps, without separate parentheses.'),
(23,r'\xout{Maisxprécédantxxxxxx}',r'\xout{Mais précédant comme}','The entire cancelled phrase can be read in the enlargement; preceding/précédant spelling is preserved as printed.'),
(24,r'\unsure{F}',r'\unsure{F|T}','The overprinted capital in f() has both an F-like middle bar and a T-like upper crossbar.'),
(24,r'$>$',r'$\hand{>}$','The positive-dimension comparison is handwritten.'),
(26,r'\emptyset_{\hand{$\xi$}}',r'\hand{\unsure{\phi|\emptyset}}_{\hand{\unsure{\xi|\zeta}}}','Both the oval-stemmed symbol and its hooked index are handwritten; their alphabetic identifications remain explicitly uncertain.'),
(31,r'$\rightarrow$',r'$\hand{\rightarrow}$','The structural arrow from X to S is handwritten.'),
(34,r'de\xout{x}s',r'de\unsure{\xout{x}s|s\xout{x}}','The s and x impressions overlap at the end of de; their order cannot be separated securely in the enlarged word.')
],[
(5,'Foliation','53 above;58 below','confirmed','Both handwritten numbers and all margins were inspected.'),
(7,'Section title','Pinceaux de sections hyperplanes,et fibrations de variétés éclatées','confirmed','The full title, both underlines and the clipped last letters were read.'),
(9,'All dual accents','Pen V marks over each P in the paragraph','confirmed','Every occurrence was inspected separately; all supplied handwritten accent layers remain.'),
(10,'Property insertion','Handwritten P after constructible','confirmed','The letter and its oblique attachment before the comma are clear.'),
(11,'NOTES: faisans/faisons','Overprinted a/o position','retained_uncertain','The merged bowl retains both candidates; no spelling normalization is made.'),
(11,'Cancelled suivant','Readable word under short pen loops','confirmed','The cancellation is local and its complete underlying word was inspected.'),
(13,'NOTES: de choses','Two handwritten words in the left margin','confirmed','Both words attach before qui; the separate long pencil rule is recorded independently.'),
(14,'NOTES: opening quotation mark','Two small pen strokes above the cancelled first t','confirmed','The separate x-cancelled t and the live following t remain distinct.'),
(16,'Printed final letter','ne rencontrant pas k','confirmed','The final letter is k, as printed; it is not replaced by Z.'),
(17,'Printed spelling','doite','confirmed','No r is present in this word.'),
(18,'NOTES: old closing quote','Dark pen cancellation over the quote after linéaire','confirmed','The old mark remains under the localized blot; the new closing quotes stand after the inserted X.'),
(19,'NOTES: quelconque and final point','Stray cancelled f;small point at the right edge','confirmed','The f impression and terminal point were inspected. The point’s writing instrument is not securely distinguishable.'),
(20,'Cross-references','nºs8 et9','confirmed','Both section numbers are clear.'),
(24,'Reference and cancelled X','8.2.,with a pen comma;cancelled X before pour','confirmed','The numerical reference, comma and underlying X were read directly.'),
(25,'Combined property','P prime = P + condition de régularité','confirmed','The prime,equality,plus and full condition were inspected.'),
(27,'Procedure reference','7.1.','confirmed','All digits and punctuation were checked.'),
(30,'Paragraph reference','par.5','confirmed','The printed reference remains unchanged.'),
(33,'NOTES: last marginal rule','One long near-vertical pencil stroke','confirmed','Its full extent beside the final four lines was inspected.'),
(36,'Final parenthesis and wording','propriétés modulées followed by a handwritten close parenthesis','confirmed','The complete final line and pen closing mark were read.')
],'Both full images and every margin read. Enlarged reference12, faisans/faisons, the corrected ending, all dense cancellations, preschéma overprint, the short mark over dans, f(F/T), the oval/index glyphs and the fused s/x word. Every insertion bracket was followed to its attachment; unsupported literal parentheses were removed while separate quotation marks were retained.')
finish_reviewed(59,[
(5,r'\mspage{59}',r'\mspage{54}','The upper folio has a clear5 followed by an open angular4; the lower archive number is59.'),
(10,r'\check{P}',r'\overset{\hand{\vee}}{P}','The dual mark over P is handwritten.'),
(13,'Une autre',r'\margin{\unsure{$-\,\cdot$}}\margin{\unsure{\illegible{1}}}Une autre','A short dash-and-point-like mark lies above Une, and a separate obscured cluster lies below its n. Both previously omitted marks are represented without assigning them a textual function.'),
(14,r'\check{\underline{E}}',r'\overset{\hand{\vee}}{\underline{E}}','The V above the underlined E is handwritten.'),
(15,r'\xout{x}',r'\deleted{\unsure{n}}','The cancelled character after E shows two upright strokes and an n-like arch under a thick irregular pen stroke.'),
(17,r'\longrightarrow',r'\hand{\longrightarrow}','The first arrow in the composed map is handwritten.'),
(17,r'\longrightarrow',r'\hand{\longrightarrow}','The second connector is also handwritten; its right terminal has a small raised arrow stroke.'),
(21,r'\longrightarrow',r'\hand{\longrightarrow}','The arrow in the twisted homomorphism is handwritten.'),
(23,r'\xout{Supposonsxx Pour}',r'\xout{Supposons Pour}','The old words are readable beneath the typewriter cancellation; the intervening x characters are cancellation marks.'),
(24,'images dans',r'image\unsure{s|d} dans','The final character is darkly retraced, with both an s-like lower loop and a d-like rising stroke.'),
(24,r'\hand{\unsure{\^{}}}',r'\hand{\unsure{$\curvearrowleft$|$\widehat{\ }$}}','The small pen mark above O has a curved lower body and a leftward point; its shape also permits the original accent candidate, and its function remains unresolved.'),
(25,r'\over{\unsure{nt}}{nt}',r'\unsure{\over{nt}{nt}|nt}','The typed nt is readable beneath two slanted pen strokes. A replacement by nt remains possible, but the pen strokes do not securely establish that operation; the live ending is retained.'),
(25,r'\xout{x}condition',r'\deleted{\unsure{x}}\unsure{c}ondition','The first x-like group is crossed by pen; the adjacent first letter of condition is overprinted and remains a c candidate.'),
(27,r'\inserted{$\otimes\ \underline{O}_{X}/J$}',r'\inserted[typed]{$\otimes\ \underline{O}_{X}\hand{/}J$}','The tensor mark, O with its underline and X, and J have typewriter forms; the unusually long slash and surrounding attachment curve are pen.'),
(27,r'\to \underline{J}',r'\hand{\to} \underline{J}','The arrow to the quotient of J is handwritten.'),
(27,r'\longrightarrow X',r'\hand{\longrightarrow} X','The arrow from T to X is handwritten.'),
(28,r'\margin{|}',r'\margin{$\|$}','Two long pencil strokes run beside the whole NB block, rather than an independent single stroke on each source line.'),
(28,r'\xout{xxxxxx}',r'\xout{aurait}','The underlying a-u-r-a-i-t is readable beneath the cancellation.'),
(29,r'\margin{|} ',r'','This line lies alongside the same pair of continuous pencil strokes already recorded at the start of the NB block.'),
(29,r'\underline{G} \to',r'\underline{G} \hand{\to}','The arrow in the general homomorphism is handwritten.'),
(30,r'\margin{|} ',r'','This is the final line alongside that continuous pair of pencil strokes; a third independent mark is not present.'),
(32,r'\longrightarrow',r'\hand{\longrightarrow}','The arrow of the pencil’s canonical projection is handwritten.')
],[
(7,'Opening reference','9.5.','confirmed','The requested reformulation and its precise number were read.'),
(10,'NOTES: paragraph number','Hand1 before typed0.2.','confirmed','The first numeral is a straight continuous pen stroke.'),
(11,'Raised notation and spelling','L with raised o;quélconque','confirmed','The raised round letter and the printed accent are preserved.'),
(12,'Fibre product display','T=X x_P L with raised o','confirmed','The x is a typed lowercase x; its P subscript and both capital letters were checked.'),
(13,'NOTES: marks at Une','One short upper mark and a dark lower cluster','retained_uncertain','The enlargement does not reveal a secure word or correction in either; the newly explicit graphic records preserve their presence.'),
(15,'Rank statement','F underlined as a locally direct factor of underlined E,rank2','confirmed','All underlines and the final digit were inspected.'),
(19,'NOTES: J insertion and right edge','Typed J above image;cut l’homomo at the right','confirmed','The inserted capital is clear; no unseen hyphen or continuation is supplied at the edge.'),
(22,'Typed Supposons insertion','Supposons above the cancelled opening','confirmed','All letters and its replacement location were read.'),
(24,'Ordered-base insertion','Handwritten tot.ordonnée','confirmed','The abbreviation,point,accent and attachment after base were read.'),
(24,'leurs/les revision','Pen-cancelled leurs with hand les above','confirmed','Both complete words and the cancellation stroke were inspected.'),
(24,'NOTES: mark above O','Small curved arrow/accent-like pen mark','retained_uncertain','The scan supports its presence and position but does not establish a mathematical meaning.'),
(25,'NOTES: ending of forment','Typed nt crossed or retouched by slanted pen strokes','retained_uncertain','The former certain replacement claim has been weakened to preserve the unresolved function of the pen strokes.'),
(27,'NOTES: tensor insertion placement','Formula above choisie et,with bracket ending after F_X(-1)','confirmed','The full bracket was followed to the line below; it attaches before the rightward arrow.'),
(27,'Quotient and ideal notation','J/J squared;V(J)=T','confirmed','The displayed J letters are underlined,including the exponent2 denominator; the inserted denominator J above lacks an underline.'),
(28,'NB block','General homomorphism with G locally free on préschéma X','confirmed','Every word and the closing parenthesis on the third line were read.'),
(31,'NOTES: changed statement label','Typewriter-cancelled Proposition;live underlined Théorème10.2','confirmed','The cancelled word,live title and every digit are clear.'),
(33,'NOTES: uniqueness insertion','Handwritten de façon unique','confirmed','All words and the curved attachment immediately before au were read.'),
(35,'Lower foliation','59 in pencil','confirmed','The bottom number and surrounding blank margin were inspected.')
],'Both complete images and all margins read. Enlarged the two marks near Une, cancelled character after E, second displayed arrow, final character of images, curved mark above O, ending of forment, first condition characters, typed/pen tensor insertion and all cancelled words. Every formula index, underline, arrow and insertion endpoint was checked; unresolved mark functions remain explicit.')
finish_reviewed(60,[
(9,r'\hand{(}que  si S=Spec(k)\hand{)}',r'que  si S=Spec(k)','The long curve before que and the stroke meeting the closing typed parenthesis of Spec(k) belong to the cancelled interlinear insertion’s attachment. They do not provide separate literal parentheses around this clause.'),
(10,r' \inserted{(\unsure{notamment pour S.3.|notamment pour 5.3.})}',r'','The note’s bracket descends to the end of the following paragraph-reference group, rather than attaching after vérifiée.'),
(11,r'ra\xout{t}trappages',r'rat\xout{t}rappages','The first t after ra is clear; the following second t carries the overstrike. The cancellation is placed on that second occurrence.'),
(11,r"\inserted{\unsure{l'avant}}",r'\hand{12}','The enlarged group before cancelled suivant is the handwritten digits1 and2, not a word.'),
(11,r'\deleted{suivant}',r'\deleted{suivant}\inserted{\unsure{notamment pour S.3.|notamment pour 5.3.}}','The enlarged note’s lower branch lands immediately after the cancelled suivant and before the typed closing parenthesis. Its surrounding curves are attachment strokes, without separate literal parentheses.'),
(13,r'\xout{\unsure{étaient}}',r'\xout{étaient}','All seven letters and the acute accent are readable beneath the typed cancellation.'),
(14,r'\inserted[typed]{de même type mais\hand{,}}',r'\inserted[typed]{de même type mais}','The apparent comma at the right is the raised end of the continuous insertion bracket; no separate comma is present.'),
(15,r'\hand{$\zeta\in$}',r'\hand{$\unsure{\xi|\zeta}\in$}','The point symbol has the hooked xi/zeta form; the adjacent membership sign is a separate pen curve.'),
(15,r'\phi_{\hand{\zeta}}',r'\hand{\unsure{\phi|\emptyset}}_{\hand{\unsure{\xi|\zeta}}}','The oval-stemmed main symbol and the hooked index are both handwritten, with alphabetic readings left uncertain.'),
(15,r'k(\hand{\zeta})',r'k(\hand{\unsure{\xi|\zeta}})','The field argument repeats the same uncertain pen point symbol.'),
(23,r'\hand{(}géom',r'géom','The opening curved stroke is part of the insertion bracket, not a parenthesis in its text.'),
(23,r'\xout{\illegible{1}}',r'\xout{connexe}','The full underlying word connexe is legible beneath the x marks.'),
(23,r'di\xout{p}m',r'di\unsure{m|p}','The m and p occupy one overprinted position; the scan does not show a separate cancelled p followed by a separate m.'),
(23,r'$\geq$2 \hand{)}',r'$\hand{\geq}$2','The comparison is handwritten; the closing curve is the end of the insertion bracket, without a separate literal parenthesis.'),
(24,r'\deleted{\illegible{1}}2',r'\unsure{\deleted{\illegible{1}}|\hand{\geq}}2','The compact ink cluster before2 could be a cancelled sign or a retraced greater-or-equal mark. Neither its old character nor its function is secure.'),
(27,r'\xout{\unsure{contraire si dim X}}',r'\xout{contraire si dim X}','Every word and the final capital X are readable under the typewriter cancellation.'),
(28,r'\inserted[typed]{\hand{(}sont géom intègres, et  dont toutes les fibres \hand{)}}',r'\inserted[typed]{sont géom intègres, et  dont toutes les fibres}','Both outside curves are joined to the insertion rule and its fork after fibres; no separate literal parentheses occur.')
],[
(5,'NOTES: upper scratched note','Dense cancelled pen group inside an oval,with a line descending toward the opening paragraph','retained_illegible','The enlargement does not recover a secure complete word; both the cancelled group and its linking line were inspected.'),
(5,'Foliation','55 above;60 below','confirmed','Both numbers and all surrounding margins were read.'),
(8,'NOTES: cancelled interlinear line','Long handwritten group with loops and repeated crossing strokes','retained_illegible','The entire line was enlarged. Its individual letter strokes do not support a secure continuous reading; the source’s approximate illegibility count remains.'),
(10,'Dual accent','Pen V above P','confirmed','The accent and its alignment with the typed P were checked.'),
(11,'NOTES: note text and reference','Handwritten12 before suivant;note reads notamment pour S/5.3.','retained_uncertain','The reference12 is resolved, while the first character within S.3./5.3. remains ambiguous. The note’s attachment was traced separately from its wording.'),
(14,'NOTES: typed insertion','de même type mais before distincte','confirmed','All words and the start of the attachment curve are clear.'),
(15,'NOTES: writing layers','Oval-stemmed symbol,index and membership are pen','confirmed','The full formula and each hand-drawn stroke were compared directly.'),
(16,'Recapitulative wording','Il fallait inclure la condition...','confirmed','The cut inclu/re and the full following line are retained.'),
(17,'Cancelled duplicated opening','D’autre part,on peut noter','confirmed','Every word is readable beneath the typewriter cancellation.'),
(18,'Numbered references','10.2 and9.5,with repeated9.5 and10.2 below','confirmed','Each occurrence and its punctuation was checked independently.'),
(23,'Geometric-connectedness insertion','géom,cancelled connexe,live conn X de dim-comparison2','confirmed','The complete typed addition and its fork between lisse and sur were read; the overprinted m/p remains marked.'),
(24,'Nonempty insertion','Typed non vide','confirmed','The words attach after the cancelled partout and before de codimension.'),
(25,'Cancelled interlinear phrase','puisse être','confirmed','Both words and the accent are readable.'),
(26,'Cancelled old qualification','(ce qui n’exclut pas qu’il soit vide) et il implique au','confirmed','Every word,parenthesis and cancellation was inspected across the full line.'),
(28,'NOTES: added fibre clause','Typed sont géom intègres,et dont toutes les fibres','confirmed','The note attaches after the first fibres; the preceding long slash-like mark is independently visible between les and fibres.'),
(28,'Printed repeated wording','sont lisses sont au plus un nombre fini','confirmed','Both printed sont occurrences are present and remain unchanged.'),
(29,'Cancelled singular-point wording','non lisse(et','confirmed','The two words and opening parenthesis are readable under the x marks.'),
(30,'est/étant revision','Cancelled typed est;typed étant above','confirmed','All letters,accent and the replacement location were checked.'),
(31,'à peine/tout juste revision','Pen-cancelled à peine;hand tout juste above','confirmed','Both complete phrases and the local cancellation were read.'),
(34,'Final punctuation','Pen comma after dim d-1','confirmed','The falling stroke is separate from the typed1.'),
(35,'Last handwritten line','pouvant avoir des singularités ordinaires.','confirmed','Every word,accent and terminal point was read in full.')
],'Both complete images and all margins read. Enlarged both heavily cancelled handwritten groups, the actual reference12 and its attached S/5.3 note, the misplaced cancellation in rattrappages, the typed insertion endpoint, all dense cancellations, the m/p overprint and the ink cluster before codimension2. Every insertion bracket and formula writing layer was checked; repeated printed wording and unresolved signs remain intact.')
changes61=[]
for ln,line in enumerate(source_path('ega25_25_061').read_text().splitlines(),1):
 if 12<=ln<=26 and line.startswith(r'\deleted{') and line.endswith('}'):
  changes61.append((ln,line,line[len(r'\deleted{'):-1],'The block carries two long crossing diagonals, including a curved lower terminal, without a secure whole-block deletion boundary. Their editorial function remains unresolved. Retain this fully read line and its local cancellations while recording the diagonals separately.'))
changes61 += [
(7,r'\unsure{10.2.}',r'\over{8}{10}.2.','The enlargement separates a typed8 from the added pen1 and enclosing0; the .2. remains typed.'),
(8,'qui est tout',r'\margin{|}qui est tout','The long thin pencil rule begins beside this line and continues down to the later isomorphism paragraph; it was previously omitted from the transcription.'),
(9,r'\xout{xx}',r'\xout{\unsure{le}}','The old two-letter group supports le, with its first letter still merged into the cancellation strokes.'),
(12,r'\uline{Proposition}',r'\margin{|}\margin{\unsure{$\backslash\,/$}}\uline{Proposition}','A shorter thick pencil stroke and the separate crossing pen diagonals begin beside this block. Their presence is recorded without treating the diagonals as certain deletion.'),
(12,r'\unsure{10.3.}',r'\over{8}{10}.3.','The proposition number independently shows typed8 overwritten by handwritten10.'),
(13,r'\underline{G}\to',r'\underline{G}\hand{\to}','The arrow defining u is handwritten.'),
(14,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The first tilde above X is handwritten.'),
(15,r'\underline{G}_P\to',r'\underline{G}_P\hand{\to}','The canonical-map arrow is handwritten.'),
(16,r'0\to\underline{H}-\underline{G}_P\to\underline{O}_P(1)\to 0',r'0\hand{\to}\underline{H}\hand{\unsure{\relbar|\to}}\underline{G}_P\hand{\to}\underline{O}_P(1)\hand{\to}0','All connectors are pen. The first,third and last have visible arrow terminals; the H-to-G connector has only a small lower hook, leaving a bar/arrow reading unresolved.'),
(17,r'\underline{G}_P \to',r'\underline{G}_P \hand{\to}','The arrow defining u_P is handwritten.'),
(17,'Idéal',r'Idéa\unsure{l|m}','The last letter is overprinted with an m-like second stem; l and m remain visible candidates.'),
(17,r'\subset\underline{O}_P',r'\hand{\subset}\underline{O}_P\margin{\unsure{$\smile$}}','The containment sign is handwritten. A separate small curved pen stroke lies above this O and below the preceding final0; its function remains unresolved.'),
(18,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The second tilde above X is handwritten.'),
(20,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The third tilde above X is handwritten.'),
(21,'est localement',r'est\margin{\unsure{o|\illegible{1}}} localement','A faint rounded trace follows est. Its o-like shape is recorded separately without reading it as part of the word.'),
(21,r'\xout{xxx}',r'\xout{\unsure{$u_P$}}','The two-level cancellation exposes a u-like upper letter and a lowered P-like bowl; the formula candidate remains uncertain.'),
(21,r'\underline{H}\to',r'\underline{H}\hand{\to}','The arrow from H to O_P is handwritten.'),
(22,r'\xout{\unsure{t}}',r'\xout{t}','The cancelled t after le is readable in the enlarged crop.'),
(22,r'\widetilde{X}',r'\overset{\hand{\sim}}{X}','The final tilde in the crossed block is handwritten.'),
(24,'deuxième',r'deuxiè\unsure{m|p}e','The penultimate consonant position contains overlapping m/p outlines; no spelling is selected silently.'),
(28,r'\unsure{\leqslant}',r'\hand{\leqslant}','Both strokes of the handwritten less-or-equal sign are clear.'),
(29,r'\xout{\unsure{ex}}',r'\deleted{\xout{\unsure{ex}}}','The old prefix has typewriter cancellation and a separate looped pen retouch over its first character; the ex reading remains uncertain.'),
(29,r'\emptyset',r'\hand{\unsure{\emptyset|\phi}}','The oval crossed by an oblique stem is handwritten; empty-set/phi alphabetic readings remain explicit.'),
(30,r'\to X',r'\hand{\to} X','The arrow of the displayed pencil is handwritten.'),
(30,r'\unsure{;}',r'\hand{;}','The enlarged punctuation has a separate upper point and a falling lower comma; it is a pen semicolon.'),
(33,r'\unsure{10.4.}',r'\over{8}{10}.4.','The corollary number has a clear typed8 under handwritten10.'),
(33,r'\unsure{10.2.}',r'\over{8}{10}.2.','The adjacent reference independently has the same visible old8/new10 revision.'),
(34,r'\xout{dimensionxxx}',r'\xout{dimension\illegible{1}}','Dimension is readable; the further x marks do not yield secure underlying letters and are represented as an unreadable continuation.'),
(36,r'$X\to P^1$',r'$X\hand{\to}P^1$','The final morphism arrow is handwritten.')
]
finish_reviewed(61,changes61,[
(5,'Foliation','56 above;61 below','confirmed','Both handwritten numbers and the complete margins were read.'),
(7,'NOTES: revised numbers','Typed8 overwritten by pen10 in four places','confirmed','Each of the four number groups was enlarged and inspected separately; their following .2,.3,.4,.2 remain typed.'),
(12,'NOTES: crossed block','Two long diagonals across the proposition and its drafting note','retained_uncertain','The descending and ascending strokes were followed through both images. The lower-left terminal curves back; their role as deletion or relocation is not securely determined.'),
(12,'Nested cancellation','Underlined E cancelled before underlined G','confirmed','The old letter and its underline are visible beneath the local cancellation.'),
(13,'Ideal definition','Underlined J=u(G),with G plain inside the parentheses','confirmed','This visible underline difference remains unchanged.'),
(16,'Exact-sequence wording and display','The printed words suite exacte precede all five terms','confirmed','Every term,index and connector was checked; the uncertain middle connector is not completed mathematically.'),
(17,'NOTES: small mark near O_P','Shallow curved pen stroke between the previous0 and the next O','retained_uncertain','Its location is clear but it does not establish an accent or other mathematical operation.'),
(19,'Local cancellation in régulier','Cancelled re before the live word','confirmed','Both letters and the following quotation marks were inspected.'),
(21,'NOTES: mark after est','Faint rounded trace','retained_uncertain','The enlarged trace remains too faint to settle as a letter or stray mark.'),
(22,'Printed internal spacing','d es and e st','confirmed','The extra spaces are visible in the scan and remain; they are not joined editorially.'),
(24,'Drafting note','Le premier énoncé...je ne l’ai pas fait en détail...','confirmed','Every word of all three lines was read through the diagonals; the note remains available with the rest of the block.'),
(28,'Inserted hypothesis','Handwritten S=Spec k et X est de','confirmed','The complete insertion and its placement over the locally cancelled les fibres de X/S sont de were read.'),
(30,'Underlining','L indexed under Y;isomorphisme underlined','confirmed','Both underline placements were inspected.'),
(31,'Reference','9.2.','confirmed','All digits and punctuation are clear.'),
(33,'Corollary opening','Smooth geometrically connected curve in projective space over an infinite field','confirmed','The complete opening text and its continuation on the next line were compared word by word.'),
(34,'NOTES: n comparison','Handwritten greater-or-equal2','confirmed','The upper angle and separate lower stroke are visible; no distinct old typed comparison is recoverable.'),
(36,'Final continuation','ce morphisme est','confirmed','The page ends after these words; the sentence continues on62.')
],'Both complete scan parts and every margin read. All lines under the two diagonals were read, including the complete exact sequence and drafting note; their function remains unresolved and the body is retained. Enlarged all revised numbers, cancelled letters, Idéal/deuxième overprints, small marks, local prefix cancellation, comparisons, punctuation and internal spaces. Every tilde,arrow,index and underline was checked.')
finish_reviewed(62,[
(7,r'\hand{d}',r'\over{\illegible{1}}{d}','The added d sits over a separate typed impression; its earlier letter cannot be securely recovered.'),
(8,r'\hand{$-$}\unsure{alg}',r'\margin{\unsure{$-$}}\unsure{a|q}l\unsure{g|f}','The small pen bar lies above the first letter. That letter has an a bowl with a q-like lower trace; the final letter contains g/f overprinting. The bar’s function remains unresolved.'),
(8,r"\inserted{k'=}",r"\inserted[typed]{k'=}",'The inserted k,prime and equality are typed; only the attachment curve is pen.'),
(8,r'\xout{\illegible{3}}',r'\xout{\unsure{consiste en} \unsure{r|n}+2 point}','The enlarged cancellation yields a consiste en candidate, a partly obscured r/n before the clear+2, and the readable final point. No plural ending is supplied.'),
(9,r"\inserted{k'-}",r"\inserted[typed]{k'-}",'The prefix is typed above isomorphe and attached by a pen curve.'),
(9,r"\inserted{Spec(k')}",r"\inserted[typed]{Spec(k')}",'The complete replacement scheme expression has typewriter forms.'),
(15,r'\uline{Grassmaniennes}.',r'\uline{Grassmaniennes}.\margin{\unsure{$\prime\,\prime$}}\margin{\unsure{$\smile\,\smile$}}','Two small upper marks and two faint lower curved traces occur at the r/underline position. Their presence is recorded as uncertain graphic marks without assigning an accent or textual meaning.'),
(15,r'\deleted{Ratrapages.}',r'\deleted{\uline{Ratrapages}.}','The old heading has a separate straight underline beneath its letters, in addition to the looped pen cancellation.'),
(18,'0 ou r-1',r'0 ou \unsure{t|r}-1','The first letter before minus1 has a tall t-like cross-stroke and an r-like shoulder; the overprinted reading remains uncertain.'),
(19,r'\inserted{de}',r'\inserted[typed]{de}','Both inserted letters are typed; the two sloping attachment strokes are handwritten.'),
(20,'sorties',r'\unsure{sorties|sorttes}','The middle letter position has a full t-like crossbar over the supplied i reading; the surrounding letters are clear.'),
(26,r'\hand{,}',r'','The apparent comma before Considérons is the dark lower tip of the continuous insertion bracket, without a separate punctuation stroke.'),
(27,r'\longrightarrow',r'\hand{\longrightarrow}','The functor arrow is handwritten.'),
(28,'Modules quotients',r'\unsure{M|P}odules quotients','The initial capital has overlapping M and P outlines, including a lowered P-like stem.'),
(30,'le réprésente',r'le réprésente\xout{\unsure{r}}','A separate dark cancelled character follows the final e; its visible upper shoulder supports r but remains uncertain.'),
(32,'naturels',r'naturel\unsure{s}','The final s position is densely overprinted; its supplied reading remains marked.'),
(33,r'\longrightarrow',r'\hand{\longrightarrow}','The morphism to the rank-one Grassmannian has a handwritten arrow.'),
(33,r'{\textstyle\bigwedge}',r'{\textstyle\hand{\bigwedge}}','The first exterior-power angle is hand-drawn, independently of its handwritten n.'),
(33,r'{\textstyle\bigwedge}',r'{\textstyle\hand{\bigwedge}}','The second exterior-power angle is also hand-drawn.'),
(35,r'{\textstyle\bigwedge}',r'{\textstyle\hand{\bigwedge}}','The exterior-power angle before G is handwritten; its raised n is typed.'),
(36,r'{\textstyle\bigwedge}',r'{\textstyle\hand{\bigwedge}}','The last exterior-power angle is handwritten; its raised n is typed.'),
(37,r'\xout{\illegible{1}}',r'\xout{\unsure{une}}','The cancelled group before immersion supports u-n-e, with the last letter still partly obscured.'),
(37,r'\underline{Grass}_n',r'\underline{Grass}_{\hand{n}}','The final Grass subscript is a long retraced pen n, extending below the typed baseline.')
],[
(5,'Foliation','57 above;62 below','confirmed','Both handwritten numbers and all page margins were inspected.'),
(7,'NOTES: degree insertion','Typed de degré with pen d over an unreadable old letter','confirmed','The phrase attaches after étale; the new writing layer and old impression are now separately represented.'),
(8,'NOTES: alg marks','Short upper bar and lower trace at a;g/f overprint','retained_uncertain','All marks were enlarged; none is reassigned to an overline on the later k(s).'),
(9,'NOTES: d minus2','Handwritten d over a possible old n','retained_uncertain','The new d and minus2 are clear; the underlying n candidate remains doubtful.'),
(9,'Local cancellations','k(s),un,and final k','confirmed','Each old group and its typewriter cancellation was inspected independently.'),
(10,'Double-point algebra','I indexed by k prime = Spec k prime[t]/(t squared)','confirmed','Every prime,index,bracket,parenthesis and exponent was read.'),
(12,'Explanatory wording','En langage de Papa','confirmed','The capital P and complete two-line explanation are clear.'),
(13,'Printed spacing and term','c e point;quadratique in quotation marks','confirmed','The visible additional space inside c e is retained; neither term nor punctuation is normalized.'),
(15,'NOTES: title marks','Small paired marks above and below the r of Grassmaniennes','retained_uncertain','Their strokes were inspected at enlargement, but they do not establish a changed letter or accent.'),
(15,'Cancelled old heading','Ratrapages.','confirmed','The spelling with a single p and the local looped cancellation were read.'),
(17,'NOTES: couramment','Overprinted middle consonants,still readable as couramment','confirmed','The complete word remains legible without selecting another spelling.'),
(19,'NOTES: final quelques','Word partly clipped at the right edge','confirmed','The surviving strokes support the supplied word; no extra punctuation is supplied.'),
(23,'Printed spelling','quelcohques','confirmed','The tall h is visible in the word and remains unchanged.'),
(26,'NOTES: base letter','Dense S/X overprint','retained_uncertain','Neither proposed letter can be separated securely from the other impression.'),
(26,'Inserted integer condition','Typed et n un entier0 with handwritten greater-than sign and typed final point','confirmed','All words and the bracket attachment before Considérons were read; the greater-than sign lies before0.'),
(27,'Functor category notation','(Sch) indexed /S with raised o,to(Ens)','confirmed','The slash,index,raised round character and both parentheses were checked.'),
(28,'NOTES: libres','Final s close to the right crop','confirmed','Its two surviving left curves remain readable as s.'),
(29,'Quotient rank','rank n of underlined E indexed S prime','confirmed','The rank letter,index and prime are clear.'),
(30,'NOTES: spelling of réprésente','Both written acute accents remain','confirmed','The source’s accent pattern is preserved; the additional cancelled final character is now explicit.'),
(31,'Printed internal spacing','r eprésentabilité','confirmed','The enlarged word shows an extra gap after the initial r,which is retained.'),
(33,'NOTES: exterior powers','First two n labels are pen;last two are typed','confirmed','Each label and its separate wedge stroke was inspected independently.'),
(36,'NOTES: final pen mark','Question-like retraced mark after the quotient expression','retained_uncertain','The upper crossed strokes and large lower point remain compatible with the source question-mark candidate,without settling its function.'),
(36,'Reference','Séminaire Cartan','confirmed','Both words and the accent were read; no external edition is used.'),
(37,'Printed agreement','immersion fermées','confirmed','The singular noun and plural adjective are both visible and remain as written.'),
(37,'Final continuation','de sorte que Grass_n(E)','confirmed','The page ends after this expression and continues on63.')
],'Both complete images and all margins read. Enlarged the degree correction, alg marks, cancelled fibre description, title traces, t/r dimension letter, sorties overprint, base letter, Modules capital, clipped libres, final réprésente character, naturels, internal spacing, final question-like mark and Grass index. All arrows, exterior-power signs,primes,indices and insertion layers/attachments were checked.')
