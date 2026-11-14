from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from audit_record import save,source_path

def finish(site, changes, rows, notes):
 key=f'ega24_24_{site:03}'
 if (Path(__file__).parent/(key+'.json')).exists(): return
 s=source_path(key).read_text()
 origins=[i for i,l in enumerate(s.splitlines(keepends=True),1) for _ in l]
 touched=[False]*len(s)
 decisions=[]
 for line,before,after,reason in changes:
  positions=[];start=0
  while True:
   at=s.find(before,start)
   if at<0:break
   positions.append(at);start=at+1
  if not positions:raise ValueError((site,line,before))
  at=min(positions,key=lambda x:(abs(origins[x]-line),sum(touched[x:x+len(before)]),x))
  if origins[at]!=line:raise ValueError(('wrong line',site,line,origins[at],before))
  s=s[:at]+after+s[at+len(before):]
  origins[at:at+len(before)]=[line]*len(after)
  touched[at:at+len(before)]=[True]*len(after)
  decisions.append(dict(line=line,before=before,image=after,decision='corrected_from_scan',reason=reason,category='reading_change'))
 for line,before,image,decision,reason in rows:
  decisions.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category='visual_check'))
 s=s.replace('not yet checked by eye.','checked against both supplied scan parts; see CHECK_DECISIONS.tsv.')
 return save(key,s,decisions,0,notes)

finish(26,[],[
(5,r'\mspage{26}','26 in a serif face distinct from the body type','confirmed','Both digits read directly; the image does not settle the separate stamping/printing process.'),
(13,r'\uline{5.2}','5.2 with a straight typed underline','confirmed','The heading and its underline are plainly visible in the upper image.'),
(18,r'O_{X_{k(s)}}(1)','O with X below and k(s) on a further lowered baseline','confirmed','The s in the lowest index is lowercase; preserve its placement and the capital S in the two preceding k(S) indices.'),
(23,r'F_{Pv_{S}}','F with Pv below and a further S beneath Pv','confirmed','The anomalous lower S is visibly placed under the Pv of F, not beneath the earlier tensor product; no relocation supplied.'),
(22,r'{\o}^{-1}; \underline{L}^{-1}','The -1 groups are raised slightly above the ordinary baseline','confirmed','Both placements were compared with the surrounding typed text; existing exponent encoding retained.'),
(25,r'\mathrm{id}_{\underline{F}_{P^v}}','Underlined F below id; P below F with a raised v','confirmed','The three vertical levels and the raised v are visible. The other Pv expressions have v at their local P baseline.'),
(16,r'{\o}; \xi; \otimes; \to','Printed slashed oval, Greek letters, tensor signs, and arrows','confirmed','Their repeatable mechanical outlines and impression match the typed symbol element; no handwriting added.'),
(26,'Mike*','Mike followed by a typed asterisk; no corresponding footnote on this page','retained_query_with_french_crossreference','Cote 25 site 22, §5.2: «où la notation (-1,-1) s’explique d’elle-même, comme dirait Mike.» The starred Blass wording is preserved, not filled from the French.'),
(30,"in an S' over S).?)","in an S' over S).?) with a visibly typed question mark and closing parenthesis",'retained_query_with_french_crossreference',"Cote 25 site 22, §5.2: «de P à valeurs dans un S' sur S», followed by a cancelled doubtful ?? and punctuation in the French record. Blass's printed query remains exactly as typed."),
(7,'Opening paragraph through E is also open','Text translates the end of the relocated §5.1 paragraph','comparison_note','Cote 25 site 21 has «Nous donnerons d’abord des critères pour que U soit ouvert» and «alors E est également ouvert» in the cancelled paragraph that site 22 calls «le texte barré par erreur». Blass gives the paragraph here before 5.2.'),
(33,'All margins','Blank lower margin and two small brown/black top-left specks','confirmed','Both images inspected to their borders; the specks lack letter or symbol structure, and there is no handwritten text on this page.')
],'Both supplied images read completely, once for the overlap, including every prose line, formula, nested index, punctuation mark, and all margins. No source-reading change was required; unusual typed placements and both translator queries were retained with French-site references.')

finish(27,[
(10,'regular if the',r'regular if\unsure{,|\hand{,}} the','A small comma-shaped mark is visible immediately after if. Its print/pen layer is not secure, so both layer readings are retained rather than omitting it.'),
(27,r'O$_{\mathrm{III}}$',r'o$_{\mathrm{III}}$','The reference begins with the small oval of a lowercase o, at the height of the o in from, unlike the uppercase O in the preceding paragraph. Preserve the typed lowercase letter.'),
(31,'associated cycles',r"associated cycles\unsure{'|\hand{'}}",'A small raised oblique tick follows the final s, visible in enlargement. It is retained as an apostrophe-shaped mark with the writing layer unsettled.')
],[
(5,r'\mspage{27}','27 in a separate serif face','confirmed','Both digits checked in the upper right; exact manufacturing process remains unasserted.'),
(7,r'\uline{in}','in underlined','confirmed','The underline is a straight typewriter rule.'),
(16,r'\uline{Proposition 5.3}','Complete heading underlined','confirmed','All letters, number, and underline checked.'),
(24,r'\uline{Proof}','Proof underlined','confirmed','Straight underline visible.'),
(30,r'\uline{to}','to underlined','confirmed','The underline is visible under both letters.'),
(8,'id_F tensor ? *','Typed question mark and asterisk after the tensor sign','retained_query_with_french_crossreference','Cote 25 site 22, end of §5.2: «au conayau de id_F⊗φ», followed by F⊗L⁻¹ → F. Blass’s printed ? * remains unchanged.'),
(27,'11.3 and o_III...','Typed incomplete reference with three periods','retained_query_with_french_crossreference','Cote 25 site 23, proof of 5.3(a), reads «résulte de 11.3. (et même de E_III ... dans le cas S loc noeth)». The French itself leaves an incomplete reference, and its E is not substituted for Blass’s o.'),
(31,'Par. 3)*','The asterisk after the parenthesis has a typed star shape','retained_query_with_french_crossreference','Cote 25 site 23, proof of 5.3(b): «(en vertu du par.3) les images inverses des cycles ... associés à F». The reference and star are preserved without completion.'),
(38,r'\margin{* illegible, ask A.G. or figure out.}','Handwritten footnote, every word and punctuation visible','confirmed_query_with_french_crossreference','The cursive note is at the foot of the page. The typed starred query after id_F⊗ corresponds to cote 25 site 22, «au conayau de id_F⊗φ»; the star after Par.3 corresponds to cote 25 site 23, «en vertu du par.3». No answer is inserted into Blass’s wording.'),
(19,'F_K(xi) and later F_k(eta)','Capital K in the proposition; lowercase k in the proof','confirmed','Character heights distinguish the two; each source case is preserved.'),
(22,'P_s v; F_P v; Pv','The v is on the local baseline of P, not a raised dual mark','confirmed','Each occurrence was inspected in both images, including the overlapping line.'),
(33,'Z_ik(eta) cap Y = Z_ik(eta)','A plain typed equality, no cancelling slash','comparison_note','The source is preserved. Cote 25 site 23, corresponding proof of 5.3(b), has a handwritten ≠ in «Z_i k(η) ∩ Y ≠ Z_i k(η)». This comparison does not replace Blass’s sign.'),
(35,'varnothing without subscript','Plain slashed oval without eta below','comparison_note','Blass’s glyph is retained. The corresponding cote 25 site 23 line has φ with handwritten η subscript in «ce qui prouve que φ_η ne s’annule...».'),
(36,'Other formula signs and margins','Typed symbols and otherwise blank margins','confirmed','All prose, indices, tensor signs, intersections, and arrow directions read; top-left isolated speck carries no text. Only the footnote is securely handwritten.')
],'Both scan parts read completely, including all prose and formulas, overlap, footnote, and page borders. Enlarged the small mark after if, incomplete reference, and tick after cycles. Blass queries cross-referenced to checked French sites 22–23; the equality and unindexed final section symbol remain as printed.')

finish(28,[
(9,r'P^{\vee}',r'P\mathrm{v}','The v is a typed lowercase letter on the baseline of P; it is not raised. Restore the visible placement.'),
(11,r'P^{\vee}',r'P\mathrm{v}','The second Pv also has a baseline v, with its bottom aligned to P.'),
(17,r'P^{\vee}',r'P\mathrm{v}','The Pv in Remark 5.5 has a baseline typed v.'),
(27,r'\hand{$\Phi$}',r'$\Phi$','The enlarged capital Phi has symmetrical elliptical sides and mechanically formed top and bottom serifs, like the typed symbol element. It is typed, not a handwritten insertion.')
],[
(5,r'\mspage{28}','28 in a separate serif face','confirmed','Both digits read in the top-right margin.'),
(7,r'\uline{Corollary 5.4}','Heading and straight underline','confirmed','All letters and number checked.'),
(15,r'\uline{Remark 5.5}','Heading and straight underline','confirmed','All letters and number checked.'),
(34,r'\uline{Theorem 5.6}','Heading and straight underline','confirmed','All letters and number checked.'),
(9,r'\varnothing_{\xi}','Typed slashed oval followed by lowered xi','confirmed','The smaller slashed oval remains distinct in form from the later capital Phi; neither is normalized.'),
(12,'P is flat over S','The printed capital is P','comparison_note','Cote 25 site 23, Corollary 5.4, has the handwritten insertion «et F plat sur S». Blass’s P is preserved as typed.'),
(20,'a little less evidently','The complete phrase is typed','comparison_note','Cote 25 site 23, Remark 5.5, says «et on peut évidemment dans ce critère remplacer k(ξ) par une extension arbitraire de k(ξ)». Blass’s qualification «a little less» remains unchanged.'),
(22,'extension of k(xi).','The closing parenthesis of the earlier parenthesis is absent','confirmed','The line ends with a period only; no close delimiter supplied.'),
(25,'Cohen-Macauley','Cohen-Macauley with an e before y','confirmed','The typed spelling is secure and retained.'),
(32,'12.1.1* and 12.1.4*','Both asterisks are typed','retained_query_with_french_crossreference','Cote 25 site 24, preceding Theorem 5.6: «Utilisant maintenant 12.1.1. et 12.1.4., on obtient». Both starred Blass references remain.'),
(32,r'\uline{locate reference}','locate reference underlined within parentheses','retained_query_with_french_crossreference','This printed translator instruction accompanies the references to cote 25 site 24, «Utilisant maintenant 12.1.1. et 12.1.4.». It is preserved with its underline.'),
(40,r'\margin{* Ask AG about reference.}','Handwritten * Ask AG about reference. at the foot','confirmed_query_with_french_crossreference','All words and the final period are legible in the lower image. The note refers to the starred 12.1.1 and 12.1.4 references corresponding to cote 25 site 24.'),
(38,'Remaining prose, formulas, and margins','All ordinary text and symbols match; margins blank apart from note and one top-left speck','confirmed','Both scan parts and overlap read completely, with capitals, indices, every delimiter, and all section references checked.')
],'Both supplied images read in full, with overlap once and all margins. Enlarged the capital Phi to distinguish its typed serifs from handwriting. Corrected three baseline v placements and the Phi layer only; preserved Blass’s wording, missing parenthesis, and queries with French-site references.')

finish(29,[
(8,r'P^{\vee}',r'P\mathrm{v}','The typed lowercase v is on the ordinary P baseline.'),
(9,r'F_{K(\xi)}',r'F_{k(\xi)}','The first index has a lowercase k, distinctly unlike the later capital K in Corollary 5.7.'),
(13,r'P^{\vee}',r'P\mathrm{v}','The Pv after the arrow has a baseline v, not an exponent.'),
(13,r'F_{\underline{P}^{\vee}}',r'F_{\underline{P}}\mathrm{v}','The enlarged formula shows underlined P lowered below F, while v is on the same text level as the v of the preceding Pv. Preserve the separate baseline v.'),
(19,r'P^{\vee}',r'P\mathrm{v}','The Pv in the corollary also has a baseline v.'),
(26,r'[\uline{fascicule}]',r'[\uline{fascicule}','Only the opening square bracket is printed; after fascicule the scan has a comma, not a closing bracket.')
],[
(5,r'\mspage{29}','29 in a separate serif face','confirmed','The number is printed, with no pen strokes discernible.'),
(15,r'\uline{Corollary 5.7}','Heading and straight underline','confirmed','All heading characters read directly.'),
(21,r'\uline{anyway}','anyway with a typewriter underline','confirmed','The underline is plainly present.'),
(26,r'\uline{fascicule}','The French word is underlined inside an unclosed opening bracket','confirmed_query_with_french_crossreference','Cote 25 site 24, editorial paragraph after 5.7: «une simple référence à des conditions énumérées dans un autre fascicule». Blass’s chapter [fascicule gloss is retained, including its missing closing bracket.'),
(12,r'$U_{P}$ \quad $U$','A blank between U_P and U, containing no ink','retained_gap_with_french_crossreference','Cote 25 site 24, proof of 5.6: «on a U_P ⊂ U (notation de 5.3. a))», with a handwritten inclusion sign. The Blass blank is not filled.'),
(9,r'\o_{\xi}','Typed slashed oval with xi below','confirmed','The symbol is a mechanically printed slashed oval, not handwriting.'),
(20,r'F_{K(\xi)}','Capital K in the corollary','confirmed','The height and diagonals distinguish K from the earlier lowercase k.'),
(19,'(resp. Y)','Y without xi below','comparison_note','Cote 25 site 24, Corollary 5.7, has «G_ξ (resp. Y_ξ)». Blass’s missing subscript is retained.'),
(20,'and that is F_K(xi) regular','No section symbol appears between that and is','retained_gap_with_french_crossreference','Cote 25 site 24, Corollary 5.7, reads «et que φ_ξ soit F_k(ξ)-régulière». Blass’s wording and the absent φ_ξ are preserved.'),
(29,'Other lines and margins','No handwritten material; text ends after Seidenberg','confirmed','Every remaining word, formula, index, and delimiter checked in both images. The lower half is blank; small edge specks are not letters.')
],'Both supplied images read completely, including the blank lower half and all margins. Enlarged the F/P/v placement. Corrected typed v positions, one K/k reading, and a supplied closing bracket; kept the empty inclusion slot and incomplete corollary wording with exact French references.')

finish(30,[
(29,r'\longrightarrow',r'\hand{\longrightarrow}','The first arrow from Y to Pv has a continuous irregular shaft and a separately drawn open head; it is handwritten in the typed gap.'),
(31,r'\longrightarrow',r'\hand{\longrightarrow}','The long thin shaft and open arrowhead after underlined Y are drawn in pen, not with the typewriter symbol element.'),
(35,r'\longrightarrow',r'\hand{\longrightarrow}','The arrow in the final proof sentence is also handwritten; its rightward direction is clear.')
],[
(5,r'\mspage{30}','30 in a separate serif face','confirmed','Both digits read in the upper-right margin.'),
(7,r'\uline{Section 6}','Section heading underlined','confirmed','Heading and straight underline checked.'),
(9,r'\uline{Connectedness of an arbitrary hyperplane section}','Complete title underlined','confirmed','All words and the final period outside the underline read directly.'),
(16,r'\uline{Proposition 6.1}','Heading underlined','confirmed','Number and underline checked.'),
(25,r'\uline{Proof}','Proof underlined','confirmed','Straight typewriter rule visible.'),
(35,r'\uline{all}','all underlined','confirmed','Underline is confined to the word.'),
(36,r'\uline{q. ed.}','q. ed. underlined, then a further period','confirmed','Both internal points and the extra external period are printed and retained.'),
(19,'[x X proper over k suppose]*','Typed bracketed phrase, x, and asterisk','retained_query_with_french_crossreference','Cote 25 site 25, Proposition 6.1, reads «On suppose S=Spec(k), k un corps ... alg clos», followed by handwritten «X propre sur S» before «que pour toute composante irréductible». Blass’s bracketed query is retained verbatim, including k and suppose, with no footnote supplied on this page.'),
(22,'dim f(Z) <= 0','No overbar on f(Z)','comparison_note','Cote 25 site 26 opens with «dim» followed by a handwritten bar over f(Z) and ≤0. Blass’s unbarred f(Z) remains.'),
(29,'if Y is proper over k','The word is if','comparison_note','Cote 25 site 26 gives «car Y est propre sur k, l’étant sur X qui l’est sur k». Blass’s if remains, without changing it to because.'),
(33,'Pv; dot below unibranch','Baseline typed v; isolated tiny fleck below r','confirmed','The v positions were checked throughout. The fleck under r has no letter or punctuation placement and remains untranscribed.'),
(39,'Remaining page and margins','Complete prose and formulas match; no other handwriting','confirmed','Read every index, inequality, Greek letter, and reference, including 3.3, 15.6.3, and 4.4; all margins inspected.')
],'Both images read completely, including overlapping lines and margins. Three unmarked pen arrows identified and marked. The proposition’s bracketed query is cross-referenced to French site 25; unbarred f(Z) and the word if are retained with comparison notes to French 26.')

finish(31,[],[
(5,r'\mspage{31}','31 in a separate serif face','confirmed','Upper-right digits read directly.'),
(15,r'\uline{Section 7}','Section 7 underlined','confirmed','Typed heading and straight rule are visible.'),
(17,r'\uline{Application to the construction of hyperplane sections and}','First title line underlined','confirmed','Every word and the complete underline checked.'),
(18,r'\uline{multisections of specified type.}','Second title line, including period, underlined','confirmed','The underline continues to the printed period.'),
(19,r'\uline{7.1}','7.1 underlined','confirmed','Number and short rule read directly.'),
(22,r'P^{v}','P followed by a slightly raised typed v','confirmed','The first v is higher than the later baseline v occurrences; existing placement retained.'),
(28,r'Pv_s; Pv','Later occurrences have the v on the local baseline','confirmed','Both v shapes and the lowered s were checked separately.'),
(32,r'\S{}','A printed section sign, visibly distinct from the xi symbols','comparison_note','Cote 25 site 27, §7.1, reads «la section ξ est une section de E sur U». Blass’s § sign remains exactly as typed.'),
(28,'point xi of the fiber','The first point is xi without 0, followed later by xi_0','comparison_note','Cote 25 site 27 has the insertion «tout point ξ_0 de la fibre». Blass omits the initial index while using 0 in the later two occurrences; no index is supplied.'),
(13,'No. (or section)','Typed explanatory parenthesis retained','comparison_note','Cote 25 site 26 ends this paragraph «dans un même n°». Blass’s extra parenthesis is preserved.'),
(24,'eta and xi symbols','Typed Greek characters with consistent mechanical outlines','confirmed','Each eta, xi, and membership sign compared with its surrounding letters; no handwriting identified.'),
(35,'All other text and margins','Prose and formulas match; lower margin blank','confirmed','Both complete images inspected. Isolated small edge and margin flecks have no secure textual form; no content omitted.')
],'Both supplied images read fully, including the end of §6 and the opening of §7.1, every formula and subscript, and all margins. No reading change required. The typed section sign and missing initial 0 were preserved and compared with French site 27.')

finish(32,[
(16,r'S^1','S1','The digit 1 sits on the baseline after S, not in a superscript position.'),
(17,r'S^1','S1','The second S1 also has a baseline digit 1.'),
(19,r'S^1','S1','The S1 at the end of the line is printed with a baseline 1.'),
(19,r'\leftrightarrow',r'\hand{\unsure{\leftrightarrow|\rightarrow}}','The dark irregular arrow is drawn or retraced by hand; its left tip may be a small left head or only a thickened tail. Retain both directions permitted by that tip.'),
(20,r'\dashrightarrow',r'\unsure{\hand{\dashrightarrow}|\dashrightarrow}','The repeated arrow at the next line begins with a segmented shaft and an open right head. Its layer is not fully secure in the enlargement; retain a pen/typed alternative rather than assert it is wholly typed.'),
(25,r'k^1','k1','The digit after k is on the baseline.'),
(27,r'S^1','S1','The digit after S is on the baseline.'),
(28,r'k^1','k1','The first k1 in this line has a baseline digit.'),
(28,r'S^1_s','S1_s','S and 1 share the baseline; only s is lowered.'),
(28,r'k^1','k1','The k1 inside Spec also has a baseline digit.'),
(29,r's^1','s1','The numeral follows the lowercase s at the baseline.'),
(29,r'S^1','S1','The numeral follows the capital S at the baseline.'),
(30,r'S^1','S1','The last S1 also has a baseline numeral.')
],[
(5,r'\mspage{32}','32 in a separate serif face','confirmed','Both digits read in the upper-right margin.'),
(15,'(by successive approximations ???)*','Three typed question marks, then parenthesis and typed asterisk','retained_query_with_french_crossreference','Cote 25 site 28, §7.1: «construire de proche en proche une “multisection” S′ de X». Blass’s alternative translation and question marks remain verbatim.'),
(35,r"\margin{* Translator's note.}","Handwritten * Translator's note.",'confirmed_query_with_french_crossreference','Every word and the apostrophe are legible at the foot of the page. This note corresponds to the starred «by successive approximations ???» translating «de proche en proche» on cote 25 site 28.'),
(18,r'\underline{P}','P underlined','confirmed','Short typed rule directly below the property letter.'),
(18,'con / shouned','The broken wording is con at one line end and shouned at the next','confirmed','No hyphen or other completion appears; the unexpected spelling is retained.'),
(17,r'\to','The short arrow to U is typed','confirmed','Mechanical shaft and balanced head match the typed arrow in the last base-change formula.'),
(28,r'\xrightarrow{\sim}','A typed horizontal line, a raised tilde, and a greater-than arrow tip','confirmed','All three components are visible and support the existing isomorphism-arrow rendering.'),
(28,'residual extension k1','Only k1 is printed, with no /k','comparison_note','Cote 25 site 28 has «l’extension résiduelle k′/k». The missing denominator is not supplied in Blass.'),
(31,'[un remords Fr]','Typed French gloss in square brackets','retained_query_with_french_crossreference','Cote 25 site 29 begins «Je dois cependant d’abord signqler un remords à 4.2. et 4.3.» Blass’s French gloss and the repeated should have been wording are retained.'),
(33,'Remaining prose and margins','All remaining words, symbols, and references match','confirmed','Every line of both scans was read, including the overlap, the duplicated arrow across the line break, the footnote, and all page borders.')
],'Both images read fully. Enlarged the digit placements and both split-line arrows. Corrected baseline 1 characters and preserved explicit arrow-layer/direction uncertainty. All translator queries and the French gloss have French-site references; source wording and missing /k remain.')

finish(33,[],[
(5,r'\mspage{33}','33 in a separate serif face','confirmed','Both digits read in the upper-right margin.'),
(7,r'\overset{\vee}{\underline{P}}','A V-shaped mark centered above underlined P','confirmed','Enlargement shows the paired straight strokes of the printed symbol; no secure pen evidence. Its above-letter position is preserved, unlike the later baseline v occurrences.'),
(10,r'\underline{P}\mathrm{v}','Only P underlined, v on the baseline','confirmed','The same placement occurs again in the proposition; both were checked.'),
(14,r'\uline{Proposition 7.2}','Heading and straight underline','confirmed','All heading characters checked.'),
(29,r'\uline{Proposition 7.3}','Heading underlined, followed by an external period','confirmed','Underline and punctuation placement read directly.'),
(17,'presentation finite and flat','The second finite is printed','comparison_note','Cote 25 site 29 states «F de présentation finie et plat sur S». Blass’s repeated finite is retained.'),
(23,r'Y_{\xi,\ s}; G_{\xi(s)}','First subscript is xi, s; second is xi(s)','comparison_note','Cote 25 site 29 has the handwritten indices Y_{ξ,ξ(s)} and G_{ξ(s)}. Blass’s simpler first index is preserved.'),
(24,r'F_{\xi,s}','F carries xi,s without the further xi(s)','comparison_note','Cote 25 site 29 reads F_{ξ,ξ(s)}-régulière. The Blass subscript is retained exactly.'),
(21,'U of s in E','The typed ambient letter is E','confirmed','This is visibly E, also present as E in the corresponding French site 29; no substitution is made.'),
(31,'properties (i) to (v) of 4.3','The last Roman item is (v)','confirmed','The full range and both references 4.3/4.2 checked; no inferred renumbering applied.'),
(32,'the reservation.")','Period, double quote, close parenthesis in that order','confirmed','The unusual punctuation is visibly printed and retained.'),
(24,'Greek letters, inequalities, and arrow','Mechanically printed symbols','confirmed','Every xi, phi, membership, less-than-or-equal sign, and the final rightward arrow checked against the page; no omitted handwritten mark found.'),
(32,'Remaining text and margins','Full prose matches; margins otherwise blank','confirmed','Both supplied images read throughout. Small edge specks have no textual structure, and the lower area is blank.')
],'Both scan parts read completely, with all words, formulas, nested indices, punctuation, headings, and margins. Enlarged the centered V-shaped mark. No source-reading change required; repeated wording and index differences from French site 29 are preserved and recorded.')

finish(34,[],[
(5,r'\mspage{34}','34 in a separate serif face','confirmed','Both digits read directly.'),
(7,'[illegible]','Literal typed [illegible] after s in S','retained_query_with_french_crossreference','Cote 25 site 29, insertion at the end of 7.3: «et dans le cas (v), pour tout s∈S, et tte comp. irréductible Z de X_s, on ait dim f(Z)≥2». The translator’s placeholder remains.'),
(9,'[[illegible]]','Literal typed double square brackets around illegible','retained_query_with_french_crossreference','Cote 25 site 29, marginal note: «[N.B. Pour (v) cf 12.2.1. (x) et (xi) ...]». The printed placeholder corresponds to the French cf; it is not replaced.'),
(10,r'\uline{illegible}','The word illegible is typed and underlined','retained_query_with_french_crossreference','Cote 25 site 29, continuation of the marginal note: «On peut donc ajouter [un|une] autre cas à 4.3. par 12.2.1. [(x)]», with the article and final reference remaining doubtful in the checked French. Blass’s wording «in the other case ... or ...» is preserved.'),
(11,'marginal remark largely illegible in preceding square brackets','Literal typed translator explanation','retained_query_with_french_crossreference','The whole preceding bracketed remark corresponds to the handwritten N.B. beside 7.3 on cote 25 site 29. The translator’s explanation remains part of his text.'),
(13,'Text crossed out','Literal typed words, with no actual cancellation on this Blass line','retained_query_with_french_crossreference','Cote 25 site 29 has the cancelled paragraph beginning «On notera que nous avons exclus les propriétés (v) et (vi) de 4.3», continuing into site 30 with the Stein-factorisation passage and ending «Ce fait mérite d’être signalé au moins en remarque». Blass reports this cancellation rather than translating the paragraph here.'),
(15,r'\uline{Proposition 7.4}','Heading underlined','confirmed','Every letter, numeral, and underline checked.'),
(19,r'\uline{for\nexample}','for and example separately underlined across the line break','confirmed','Both visible underlines correspond to the existing two-line macro content.'),
(21,'S1---> U','Baseline 1 followed by three typed hyphens and a greater-than sign','confirmed','All characters are mechanical type, and the arrow direction is rightward.'),
(22,'X x_S S1; section over S1','Lowercase x with lowered S, wide gaps, and baseline digit 1 in both S1 groups','confirmed','The spacing and character levels agree with the source; no multiplication symbol substituted.'),
(23,r'S$^1$','The 1 after S is distinctly raised at this occurrence','confirmed','This placement differs visibly from the preceding baseline S1 groups and is retained.'),
(23,r'\uline{X\ \ U}.*','Underline extends under X, an empty gap, and U; typed period and asterisk follow','retained_gap_with_french_crossreference','Cote 25 site 30, Proposition 7.4, also reads «de X U.» with no visible intervening sign in the checked French. The Blass gap remains unresolved and unfilled.'),
(35,r'\margin{* unclear, ask a.g.}','Handwritten * unclear, ask a.g.','confirmed_query_with_french_crossreference','Every word, lowercase initials, comma, and point read in the lower margin. It accompanies the starred X U at Blass line 23, corresponding to cote 25 site 30 «de X U.».'),
(33,'Remaining text and margins','All other prose and symbols match; no other handwriting','confirmed','Read every line of both scans, including inequalities, indices, references, g’s arrow, X|U, the two proof paragraphs, and page borders.')
],'Both supplied scan parts read completely. All literal translator placeholders, the report of crossed-out French text, and the X U gap were retained and each linked to the exact French site and context. Mixed baseline/raised digit placements and the full handwritten footnote were checked. No source-reading change required.')

finish(35,[],[
(5,r'\mspage{35}','35 in a separate serif face','confirmed','Both digits read in the upper-right margin.'),
(7,r'\uline{Remark 7.5}','Heading underlined','confirmed','All heading characters and the straight rule checked.'),
(11,'(but non-projective) S,','No over or on before S','comparison_note','The source wording is preserved. Cote 25 site 30, Remark 7.5, continues after «mais non projectif» with a clipped «su» at the edge and S on the next line.'),
(15,'......','Six printed periods after S','confirmed','All six dots counted directly in the upper image.'),
(17,'ILLEGIBLE *','Literal uppercase typed query with asterisk','retained_query_with_french_crossreference','Cote 25 site 30, lower marginal note: «Possibilité d’éviter un ensemble [fini|donné] ...». This is the corresponding untranscribed note at the end of Remark 7.5; Blass’s query remains verbatim.'),
(17,'Lower scan and other margins','Lower scan entirely blank apart from isolated paper specks','confirmed','Both images opened and inspected to every border. No footnote or handwriting follows the printed query.')
],'Both supplied images read and inspected completely. The short Remark 7.5, exact punctuation, literal ILLEGIBLE query, and all blank lower and side margins checked. No source-reading change required; the query is linked to the doubtful French marginal note on site 30.')

def amend(tag,site,changes,rows,summary):
 import json
 key=f'ega24_24_{site:03}'
 record_path=Path(__file__).parent/(key+'.json')
 rec=json.loads(record_path.read_text())
 if tag in rec.get('amendments',[]):return
 p=Path(__file__).parents[1]/'checked_pages'/(key+'.tex')
 lines=p.read_text().splitlines(keepends=True)
 decisions=[{k:v for k,v in d.items() if k!='id'} for d in rec['decisions']]
 for line,before,after,reason in changes:
  if before not in lines[line-1]:raise ValueError((site,line,before,lines[line-1]))
  lines[line-1]=lines[line-1].replace(before,after,1)
  decisions.append(dict(line=line,before=before,image=after,decision='corrected_after_focused_placement_review',reason=reason,category='reading_change'))
 for line,before,image,decision,reason in rows:
  decisions.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category='placement_confirmation'))
 new=save(key,''.join(lines),decisions,0,rec['visual_notes']+' '+summary)
 new['amendments']=rec.get('amendments',[])+[tag]
 record_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')

amend('individual_typewriter_placement',26,[
(15,r'X_{Pv}',r'X_P\mathrm{v}','Focused enlarged comparison with the preceding baseline Pv shows only P lowered after X; v is at the main text level. This supersedes the earlier general formula confirmation.'),
(23,r'O_{Pv}',r'O_P\mathrm{v}','Only P is lowered after O; the v bottom aligns with the main line, as in the adjacent over.'),
(23,r'F_{Pv_{S}}',r'F_{\underset{S}{P}}\mathrm{v}','The enlarged group shows P lowered below F, S directly beneath P, and v at the main text level. This supersedes the earlier nested Pv/S confirmation and retains all three visible levels.'),
(24,r'X_{Pv}',r'X_P\mathrm{v}','The repeated X group has lowered P and a main-level v.'),
(25,r'F_{Pv}',r'F_P\mathrm{v}','The first F group in this line has lowered P and main-level v.'),
(25,r'F_{Pv}',r'F_P\mathrm{v}','The second F group repeats the same lowered-P/main-v placement.')
],[
(7,r'Y_{\xi}; G_{\xi}','Attached xi characters are lowered relative to the surrounding Latin baseline','confirmed_after_paired_glyph_review','Compared enlarged Yxi/Gxi with standalone xi on line 17: standalone xi begins above the P cap height, attached xi near/below the adjacent cap height. Retain the actual index shifts.'),
(17,r'{\o}_{\xi}','Xi after the slashed oval is lowered relative to standalone xi in the same line','confirmed_after_paired_glyph_review','Same-line paired glyphs establish the downward shift; full-size glyph alone was not used as evidence.'),
(19,r'Y_{\xi}','Lowered xi after Y','confirmed_after_paired_glyph_review','The attached glyph sits lower than standalone xi in the immediately preceding formula lines.'),
(25,r'\mathrm{id}_{\underline{F}_{P^v}}','F below id, P on a further lower level, v raised from that P','confirmed_after_paired_glyph_review','The enlarged whole formula confirms that this v placement differs from the main-level v after F elsewhere on the line.'),
(26,r'G_{\xi}','Xi after G lowered','confirmed_after_paired_glyph_review','Compared with standalone xi at the end of the next line; the attached glyph starts lower.'),
(27,r'F_{k(\xi)}','Both k(xi) groups are lowered after F','confirmed_after_paired_glyph_review','The k baselines and the xi tops sit lower than the standalone xi following where in the same line; both index encodings retained.')
],'A further paired-glyph placement review retained the observed Greek subscript shifts and corrected six P/v groups; each amendment has its own superseding decision.')

amend('individual_typewriter_placement',27,[],[
(19,r'\varnothing_{\xi}; F_{K(\xi)}','Xi after the slashed oval and the K(xi) group are lowered','confirmed_after_paired_glyph_review','Compared with the standalone xi after image in the same line; both attached glyph positions begin lower.'),
(22,r'X_{k(\eta)}','k(eta) lowered after X','confirmed_after_paired_glyph_review','The index level is lower than the standalone eta at the end of the preceding line; full-size type alone does not determine the encoding.'),
(30,r'F_{k(\eta)}','k(eta) lowered after F','confirmed_after_paired_glyph_review','The lowered k baseline and eta body agree with the other genuine indices.'),
(32,r'Z_{ik(\eta)}','ik(eta) lowered after Z','confirmed_after_paired_glyph_review','The initial i, following k, and eta are on the lower index level in the enlarged formula.'),
(33,r'Z_{ik(\eta)}','Both repeated ik(eta) groups lowered','confirmed_after_paired_glyph_review','Both occurrences inspected separately against the same-line capital Z and ordinary text.'),
(36,r'Z_{ik(\eta)}','Final ik(eta) group lowered','confirmed_after_paired_glyph_review','The final occurrence has the same actual shift; no baseline conversion made.')
],'Additional paired-glyph review confirmed each Greek attachment and its surrounding Latin index level; no further reading change.')

amend('individual_typewriter_placement',28,[],[
(9,r'\varnothing_{\xi}; F_{k(\xi)}','Both attached xi positions lowered','confirmed_after_paired_glyph_review','Compared with standalone xi after set of in the same line; the attached glyphs start distinctly lower.'),
(20,r'F_{k(\xi)}; H_{\xi}','Both index groups lowered','confirmed_after_paired_glyph_review','Compared with standalone xi at the preceding line end and the following baseline k(xi); keep the observed subscript positions.')
],'Additional paired-glyph placement review confirmed the actual lowered Greek attachments; no further change.')

amend('individual_typewriter_placement',29,[],[
(8,r'G_{\xi}; Y_{\xi}','Xi lowered after G and after Y','confirmed_after_paired_glyph_review','Compared enlarged attachments with standalone xi in the preceding line; both are shifted downward.'),
(9,r'\o_{\xi}; F_{k(\xi)}','The section’s xi and k(xi) group are lowered','confirmed_after_paired_glyph_review','The same-line Latin letters establish the index level, and standalone xi supplies the glyph-height comparison.'),
(19,r'G_{\xi}','Xi after G lowered relative to standalone xi in the same line','confirmed_after_paired_glyph_review','The two glyphs are directly comparable on one baseline; retain the index.'),
(20,r'F_{K(\xi)}','K(xi) lowered','confirmed_after_paired_glyph_review','Capital K and xi both occupy the index level after F; the capital itself remains.')
],'Additional paired-glyph placement review confirmed every attached xi; no further change.')

amend('individual_typewriter_placement',30,[],[
(22,r'\underline{Y}_{\xi}','Xi lowered after Y','confirmed_after_paired_glyph_review','Compared directly with standalone xi after every in the same line; attached xi begins lower.'),
(30,r'Y_{\eta}','Eta lowered after Y','confirmed_after_paired_glyph_review','The eta body begins below the Y cap top and extends below its baseline, with the same shift as confirmed k(eta) indices on page 27.')
],'Additional focused placement review confirmed the Greek indices; no further change.')

amend('individual_typewriter_placement',31,[],[
(30,r'\xi_0','0 lowered after xi','confirmed_after_paired_glyph_review','The numeral is visibly on a lower baseline than the standalone xi; the same position recurs on line 32.'),
(34,r'\underline{Y}_{\xi}','Xi lowered after Y','confirmed_after_paired_glyph_review','Compared against the earlier standalone xi and xi_0 glyphs: the attached xi begins lower.'),
(35,r'Y_{\xi(t)}','Xi and (t) on the lowered level after Y','confirmed_after_paired_glyph_review','The enlarged last line shows the parentheses and t aligned with the lowered xi body, not the main prose baseline.')
],'Additional paired-glyph review confirmed the final Y indices and the lowered 0; no further change.')

amend('individual_typewriter_placement',32,[],[
(12,r'Y_\xi; G_\xi','Both xi attachments are lowered','confirmed_after_paired_glyph_review','Their starting heights are below the adjacent capitals; the standalone xi_0 in the opening line supplies the glyph comparison.'),
(13,r'Y_\xi','Repeated xi lowered after Y','confirmed_after_paired_glyph_review','The repeat was checked independently in the enlarged crop.')
],'Additional paired-glyph placement review confirmed the Greek attachments; no further change.')

amend('individual_typewriter_placement',33,[],[
(7,r'G_\xi; \underline{Y}_\xi','Both xi attachments lowered relative to standalone xi in the same line','confirmed_after_paired_glyph_review','Direct same-line comparison establishes the downward shift.'),
(23,r'Y_{\xi,\ s}; G_{\xi(s)}','The xi,s and xi(s) groups occupy lowered levels','confirmed_after_paired_glyph_review','Compared the enlarged groups with standalone xi on the prior page lines and the local capitals; retain the literal index contents.'),
(24,r'\phi_{\xi(s)}; F_{\xi,s}','The xi(s) and xi,s groups are lowered','confirmed_after_paired_glyph_review','Their glyph tops and Latin s baselines have the same downward shift as the preceding line’s indices.'),
(25,r'G_\xi; Y_\xi','Both final xi attachments are lowered','confirmed_after_paired_glyph_review','Each was inspected against the same-line capitals and the prior standalone glyph.')
],'Additional paired-glyph review confirmed each attached Greek level; no further change.')

finish(36,[],[
(5,r'\mspage{36}','36 in a separate serif face','confirmed','Both digits read directly.'),
(7,r'\uline{Section 8}','Section heading underlined','confirmed','Full heading and rule visible.'),
(9,r'\uline{Dimension of the set of exceptional hyperplanes}','Full title underlined','confirmed','Every word and the uninterrupted underline checked.'),
(11,r'\uline{8.1}','8.1 underlined','confirmed','Number and underline checked.'),
(29,r'\uline{writing up}','writing up underlined','confirmed','Underline covers both words.'),
(35,r'\uline{8.2}','8.2 underlined','confirmed','Number and underline checked.'),
(12,'the set of xi ... such that the set / of xi ... such that','The phrase is repeated across the two lines','comparison_note','Cote 25 site 31, 8.1, has one «l’ensemble des ξ∈P tels que Y ait une certaine propriété P». Blass’s repeated wording is preserved.'),
(14,r'{}_{\eta}','Eta printed lower than the prose baseline after generic point','confirmed','Its upper body is at the Latin baseline level and its descender extends below, unlike standalone xi elsewhere; retain the empty-base subscript encoding.'),
(20,'a better upper bound','The words upper bound are printed','comparison_note','Cote 25 site 31 changes majoration by handwritten aj→in to «minoration» of this codimension. Blass’s upper bound is retained as his wording.'),
(26,'[omitted ask Grothendieck]*','Literal typed query spanning the two lines, with typed asterisk','retained_query_with_french_crossreference','Cote 25 site 31, 8.1: «cf n°» followed by cancelled «suivant» and four inserted dashes, then «pour des exemples». The French also leaves the number unspecified; Blass’s query remains.'),
(30,'N0','N followed by a baseline zero-shaped digit','confirmed','The zero is full-height at the N baseline; it is neither a small superscript o nor an abbreviation silently expanded.'),
(33,'Redactor decidetur (Latin).','Printed Latin phrase and explanatory parenthesis','comparison_note','Cote 25 site 31 ends the paragraph «Redactor decidetur.» without the parenthetical language label. Blass’s addition remains.'),
(25,r'Y_{\xi}','Xi lowered after Y','confirmed_after_paired_glyph_review','Same-line comparison with standalone xi in the following parentheses confirms the index shift.'),
(35,r'Y_{\xi}','Xi lowered after Y in the dimension formula','confirmed_after_paired_glyph_review','Same-line standalone xi after set of begins higher; retain the genuine subscript.'),
(12,'Pv throughout','Lowercase v at the ordinary P baseline','confirmed','Each occurrence was inspected separately; only P is underlined where shown.'),
(36,'Remaining text and margins','All other prose, formulas, and references match','confirmed','Both images read fully with overlap once and all margins. No handwritten material or footnote is visible on this page.')
],'Both supplied images read completely, including every repeated phrase, formula, index, heading, query, and margin. Paired glyphs confirm the Greek levels. No source-reading change required; the omitted-reference query and upper-bound wording are compared with French site 31.')

finish(37,[],[
(5,r'\mspage{37}','37 in a separate serif face','confirmed','Both digits read directly.'),
(7,'[illegible] [is it two ask Grothendieck]*','Two literal typed bracketed queries and a typed asterisk','retained_query_with_french_crossreference','Cote 25 site 32, 8.2, reads «pour toute composante irr X_i de X, on ait dim f(X_i) > 0». Both Blass placeholders, including his candidate two, remain unchanged.'),
(10,r'\rightarrow','Short mechanically printed rightward arrow','confirmed','The shaft and balanced arrowhead agree with the typewriter symbol element.'),
(13,r'Z_{\xi}; Y_{\xi}','Both xi attachments are lowered relative to standalone xi in the same line','confirmed_after_paired_glyph_review','The attached glyphs start lower than the xi inside the following parenthesis; retain the actual index levels.'),
(15,r'T_{k(\xi)}; Y_{\xi}','T in a different larger serif face, with lowered k(xi); Y with lowered xi','confirmed','All letters and index levels are visible; the larger T remains a typed capital, without a hand marker.'),
(20,'first announcement','Words printed in a different proportional face','confirmed','The words are fully legible and mechanically typed; no handwriting or omission inferred.'),
(23,r'\phi_{\xi}; F_{k(\xi)}','Printed phi and lowered xi; lowered k(xi) after F','confirmed_after_paired_glyph_review','Same-line standalone xi supplies the reference height. The glyphs are typed, not pen additions.'),
(25,'N05','N followed by a baseline zero and 5','confirmed','The three typed characters are retained; no number-sign normalization made.'),
(29,r'\overset{\mathrm{v}}{\underline{P}}','A typed small v centered above underlined P','confirmed','Its elevated central position is clear; later Pv groups have baseline v.'),
(30,r'G_{k(\xi)}','The first module letter is G, with lowered k(xi)','comparison_note','Cote 25 site 33 reads «coprof_y F_{k(ξ)} = coprof_y G_ξ». Blass’s first G remains as typed.'),
(31,'if coprof F <= n in particular if F is Cohen-Macauley','This wording has no intervening bound for coprof G','comparison_note','Cote 25 site 33 continues after coprof F≤n with «alors pour ξ∈P−Z, on a coprof G_ξ ≤ n; en particulier...». Blass’s shorter sentence and Cohen-Macauley spelling are preserved.'),
(33,'[illegible ask Grothendieck]*','Literal typed query after F is (S_k)','retained_query_with_french_crossreference','Cote 25 site 33, handwritten insertion before 8.3: «Enfin, si F est (S_k), on sait que G_ξ est (S_{k−1}) pour ξ∈P−Z (réf E_IV)». Blass leaves the middle words as a query; no completion inserted.'),
(35,r'S_{k-1}; O_{IV}','S with lowered k−1, and O with lowered IV','confirmed_query_with_french_crossreference','The same French insertion on cote 25 site 33 ends with the incomplete reference E_IV, with IV underlined. Blass’s O_IV is preserved, and no reference number supplied.'),
(37,r'\margin{* Ask AG.}','Handwritten * Ask AG. at the foot','confirmed_query_with_french_crossreference','All letters and the final point are visible. The note accompanies the two starred places corresponding to cote 25 site 32’s dim f(X_i)>0 and site 33’s «on sait que G_ξ est».'),
(32,r'G_{\xi}','Lowered xi after G, compared with preceding standalone xi','confirmed_after_paired_glyph_review','The two glyph positions on this same line show the genuine index shift.'),
(35,'All remaining text and margins','Every remaining line agrees with the source','confirmed','Both scans read completely, including Greek glyphs, Roman indices, all inequality signs, the superscript v, the footnote, and all margins.')
],'Both supplied images read fully, including this pilot page’s previously transcribed passages. Each translator query has a specific French-site reference. All altered typefaces and Greek index levels inspected; enlarged the G_k(xi) group. No source-reading change required, and the G/F difference and omitted coprofundity clause are recorded without repair.')

finish(38,[
(34,r'\margin{* ask AG}',r'\margin{* ask A\unsure{.}G}','The enlarged footnote has a dark small point below the gap between A and G. It may be punctuation or an isolated pen touch, so retain it as a doubtful period rather than omit it.')
],[
(5,r'\mspage{38}','38 in a separate serif face','confirmed','Both digits read directly.'),
(7,r'\uline{8.3}','8.3 underlined','confirmed','Number and rule checked.'),
(9,'[illegible ask Grothendieck]*','Literal typed query after for','retained_query_with_french_crossreference','Cote 25 site 33, opening of 8.3, replaces cancelled words with an insertion whose first four words remain illegible, followed by «en général», then «même si F=O_X, k=1». The French does not settle all the queried wording; Blass’s placeholder is preserved.'),
(11,'2 ???)','Three typed question marks after 2, closing parenthesis','retained_query_with_french_crossreference','Cote 25 site 33, opening of 8.3, has typed insertion «k=2,» before «X étant géométriquement intègre et géométriquement normal de dim.3». The Blass questions remain.'),
(13,r'X C \underline{P}v','Capital C and baseline v in the displayed formula','confirmed','The C is a typed letter; no inclusion symbol or raised exponent supplied.'),
(18,r'X C\underline{P}v','Capital C next to underlined P with baseline v','confirmed','The tighter gap is visibly printed and retained; the formula’s characters remain distinct.'),
(15,'pressing; Cohen-Macauley','Both spellings are printed','confirmed','The clear scan supports pressing and the extra e in Macauley; no spelling repair made.'),
(20,'they are met (S_2)','The word is met','comparison_note','Cote 25 site 33 says «ne sont pas (S_2) en x». Blass’s printed met is preserved; no mathematical or linguistic substitution supplied.'),
(16,r'Y_{\xi}','Xi typed at a lowered level after Y','confirmed_after_paired_glyph_review','Compared with standalone exceptional xi later on the page; the attached glyph starts lower.'),
(25,'in this direction along these lines?','Printed alternative wording ending in a question mark','retained_query_with_french_crossreference','Cote 25 site 33, insertion: «Cf ... 8.5. plus bas pour ... résultat général précis dans cette voie». Blass’s tentative double rendering is retained.'),
(27,'Footnote(?) Fairly illegible ask Grothendieck*','Literal typed translator note','retained_query_with_french_crossreference','The following If F is (S_k) and gap marker correspond to the lower handwritten addition on cote 25 site 33, beginning «Si F est (S_k), que l’ens. des ξ∈P...». The exact scope of Blass’s Footnote(?) label is not asserted beyond this adjacent passage.'),
(29,'If F is (S_k) [illegible]','Typed incomplete opening and placeholder','retained_query_with_french_crossreference','Cote 25 site 33, lower insertion: «Si F est (S_k), que l’ens. des ξ∈P tels que φ_ξ soit F_k(ξ)-régulier et G_ξ soit (S_k) ait un complémentaire de codim ≥2,»; the French itself ends with a comma. No continuation is invented for either witness.'),
(30,'Illegible Gap 5 lines.','Literal typed gap description','retained_gap_with_french_crossreference','The same lower handwritten insertion on cote 25 site 33, ending «complémentaire de codim ≥2,», precedes site 34 «Signalons le résultat dimensionnel suivant». Blass’s five-line description is retained as his text.'),
(34,r'\margin{* ask AG}','Handwritten ask and capital initials, with a doubtful point between them','confirmed_query_with_french_crossreference','The note accompanies the page’s starred questions: cote 25 site 33 opening of 8.3 and its lower handwritten addition. The word ask and both initials are secure; the small point is explicitly doubtful.'),
(32,'Remaining text and margins','All other words, formulas, and punctuation match','confirmed','Both images read fully including the space occupied by the reported gap, every margin, and the complete footnote. The larger Greek glyphs are typed.')
],'Both supplied images read completely. Every literal query and gap marker is preserved with its corresponding French site 33 context, including that witness’s own surviving uncertainty. Enlarged the footnote and retained its small doubtful point. No grammatical or mathematical repair made.')

finish(39,[],[
(5,r'\mspage{39}','39 in the separate serif face','confirmed','Both digits read in the upper-right margin.'),
(7,r'\uline{Proposition 8.4}','Proposition 8.4 with straight typed underline','confirmed','Every heading character and the underline are visible.'),
(24,r'\uline{Lemma 8.4.1}','Lemma 8.4.1 with straight typed underline','confirmed','Heading and numbering read directly.'),
(13,r'\unsure{$|$|1}','An isolated vertical stroke after the inequality','retained_uncertainty','The stroke has no secure serif or upper flag. A vertical bar and a 1 made with another type element remain possible; the uncertainty in NOTES is retained.'),
(18,r'\unsure{$|$|1}','A second isolated vertical stroke after component','retained_uncertainty_with_french_crossreference','The stroke again lacks a secure distinguishing serif. It precedes Blass’s query corresponding to cote 25 site 34, the inserted continuation «irr X_j de X telle que codim(T_i,X_j)=k, et [deleted dim f(X_j)] = 0». Neither the stroke nor the query is resolved by substitution.'),
(13,r'\overset{\text{v}}{\underline{P}}','A typed v centered half a line above underlined P','confirmed','The raised v is visibly different in position from the baseline v of the other Pv groups; preserve the individual placements.'),
(9,'T; xi; phi','Printed serif T and mechanically formed Greek characters','confirmed','The alternate type element is consistent in all three T positions noted in NOTES. Xi attached to T and Y is lowered relative to the standalone xi on the same line; all existing subscripts retained. Phi in the lemma is typed.'),
(12,'[rare Fr]','The bracketed French gloss is printed exactly','retained_gloss_with_french_crossreference','Cote 25 site 34, Proposition 8.4: «Z est une partie constructible rare de P». Blass’s own gloss is retained.'),
(18,'[illegible is there an insert a footnote ask Grothendieck].*','Complete printed query and terminal asterisk','retained_query_with_french_crossreference','Cote 25 site 34 places a typed continuation at the top of the sheet, linked by a handwritten placement stroke after «une composante»: «irr X_j de X telle que codim(T_i,X_j)=k, et [deleted dim f(X_j)] = 0», then the handwritten parenthesis beginning «i.e. si f est quasi-fini et k>0». Blass’s uncertainty about an insertion or footnote is preserved; no text is inserted into his gap.'),
(43,r'\margin{$*$ Ask Grothendieck}','Handwritten star and Ask Grothendieck','confirmed_query_with_french_crossreference','Every letter is legible at the foot of the lower scan. The note points to the printed star after the query corresponding to the relocated continuation on cote 25 site 34, Proposition 8.4.'),
(28,'codim (Y, X) >= K','Underlined Y and a capital K','comparison_note','The capital K is visibly full-height and is preserved. Cote 25 site 34, Lemma 8.4.1, likewise has the unexpected Y but reads a lowercase k in «Supposons dodim(Y,X)≥k». No mathematical correction is supplied.'),
(41,'Remaining text and margins','All words, indices, signs, and delimiters match the transcription','confirmed','Read both full scans including overlap, every underlined Y/P, T_i placement, all four displayed relations, the cut-off sentence at codim, footer, and page borders. Small isolated edge specks have no textual shape.')
],'Both scan parts read in full, including all proposition and lemma text, every formula and index, the raised v, both uncertain vertical strokes, and the handwritten footnote. All translator queries and the French gloss are cross-referenced to checked French site 34; no reading change was required.')
