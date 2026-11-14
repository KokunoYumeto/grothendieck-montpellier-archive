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
(10,r'au dessus}',r'au dessus}','The two-line pen continuation and its break were checked.'),
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
(28,r'\inserted{le}\inserted[typed]{préschéma}somme',r'\inserted{le}\inserted[typed]{préschéma}somme','The handwritten le and typed préschéma share an attachment curve immediately before somme; their source order is correct.'),
(29,r'$\geqslant 2$',r'$\hand{\geqslant} 2$','The comparison in the rank list is handwritten, while the adjacent2 is typed.'),
(30,r'S^{i}',r'S^{\unsure{i|n}}_{\unsure{a|n}}','The enlarged image shows a crowded raised i/n-like group and a separate dark lower a/n-like overprint; both positions are preserved without resolving the overtyping.'),
(37,r'n\in\underline{Z}',r'n\hand{\in}\underline{Z}','The membership sign in Corollary1.3 is a pen addition.'),
(39,r'de \underline{L}.',r'de \underline{L}.\margin{\ensuremath{\swarrow}}','The long diagonal pen stroke terminates below this line in a leftward/downward arrowhead; record the graphic without assigning deletion scope to the body.'),
(42,r'Pic(S)$\longrightarrow$',r'Pic(S)$\hand{\longrightarrow}$','The first Picard-group arrow is drawn by hand.'),
(42,r'\underline{Z} $\longrightarrow$',r'\underline{Z} $\hand{\longrightarrow}$','The second Picard-group arrow is handwritten.'),
(42,r'Pic(\unsure{P})',r'Pic(\unsure{P|R|E})','The overtyped target capital contains P/R-like strokes and traces compatible with E; no choice is made from the map.'),
(42,r', le premier',r', le premier\margin{\ensuremath{\swarrow}}','A second diagonal pen stroke crosses the last paragraph and ends at a thick leftward/downward point in the lower margin.')
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
