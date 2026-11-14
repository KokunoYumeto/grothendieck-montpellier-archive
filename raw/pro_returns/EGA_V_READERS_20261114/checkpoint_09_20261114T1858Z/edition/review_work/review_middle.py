from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_record import save,source_path

def finish(site,changes,rows,lines,notes):
 key=f'ega25_25_{site:03}'
 if (Path(__file__).parent/(key+'.json')).exists(): return
 s=source_path(key).read_text()
 decisions=[]
 for line,before,after,reason in changes:
  if before not in s: raise ValueError((site,before))
  s=s.replace(before,after,1)
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
(8,r'\inserted[typed]{de dimension m(r-m),}','Typed insertion after rationelles)','confirmed','The lower placement curve attaches there; the separate upper slash opens the des/fibres spacing.'),
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
