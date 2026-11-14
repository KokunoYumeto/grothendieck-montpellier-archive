"""Authored documentary links; no similarity-based acceptance or new scan attestation."""
from pathlib import Path
import csv,json,os,hashlib
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'records/NOTES_CROSSWALK_middle.tsv'
with (ROOT/'records/NOTES_COVERAGE.tsv').open() as f:
 concerns={r['concern_id']:r for r in csv.DictReader(f,delimiter='\t')}
# This timestamp records the explicit mapping/provenance entry, not a new scan review.
mapping_record_time=datetime.now(timezone.utc).isoformat()
rows={}
if TARGET.exists():
 with TARGET.open() as f: rows={r['concern_id']:r for r in csv.DictReader(f,delimiter='\t')}
def add(cote,site,entries):
 key=f'ega{cote}_{cote}_{site:03}'
 record=json.loads((ROOT/'review_work'/f'{key}.json').read_text())
 valid={d['id'] for d in record['decisions']}
 for n,nums,reason in entries:
  cid=f'{key}-N{n:03}'
  ids=' '.join(f'{key}-D{i:04}' for i in nums)
  assert all(i in valid for i in ids.split()),(cid,ids)
  row=dict(concern_id=cid,decision_ids=ids,reason=reason)
  if cid in rows:
   assert all(rows[cid].get(k)==v for k,v in row.items()),(cid,'conflict')
   row=rows[cid]
  concern=concerns[cid]
  digest=hashlib.sha256(concern['concern'].encode()).hexdigest()
  assert digest==concern['concern_sha256'],(cid,'concern hash mismatch')
  if row.get('concern_sha256'): assert row['concern_sha256']==digest,(cid,'changed concern')
  row['concern_sha256']=digest
  row['reviewer']='GPT-6 Astra / middle'
  row['reviewed_utc']=row.get('reviewed_utc') or mapping_record_time
  rows[cid]=row

def flush():
 temp=TARGET.with_suffix('.tmp')
 with temp.open('w') as f:
  w=csv.DictWriter(f,fieldnames=['concern_id','decision_ids','reason','concern_sha256','reviewer','reviewed_utc'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows[k] for k in sorted(rows))
 os.replace(temp,TARGET)
 print(len(rows),'authored mappings saved')

add(25,55,[
(1,[53,52],'The foliation decision explicitly reads50 above and55 below; the bottom55 margin entry independently records its placement.'),
(2,[64,48],'The decisions identify both long pencil strokes beside the NB continuation and the marginal double-stroke attachment.'),
(3,[3,55],'The operator decision retains p/f uncertainty and identifies the pen star; the separate missing-equality decision explicitly says no relation precedes Sym^n(E).'),
(4,[5,24,25],'The individual o and t cancellations in Soit are recorded as irregular pen deletions, leaving Si; this supersedes the proposed typewriter-layer reading.'),
(5,[8,27,28],'The final f-like group after the composite-map phrase is retained as doubtful and its cancellation is identified as pen.'),
(6,[11, 68, 17, 19, 23],'D0011 records the pen accent above the doubtful target capital; D0068 precisely records the separate pen vee above P in P(n), superseding the unrelated rationale repeated in D0039. D0017/D0019/D0023 preserve the hooked point-symbol xi/zeta uncertainty in its three occurrences.'),
(7,[9,31],'The cancelled lexmorp proposal is resolved as le morp; the apparent interword x belongs to cancellation.'),
(8,[13,35,37,59],'The full local pen-deletion scope through r=2m+1 and the inserted dans P^3 attachment are recorded, together with the uncertain overwritten m in impaire.'),
(9,[61,43],'The n-apostrophe insertion and curved attachment between ou and admet are explicitly recorded.'),
(10,[62,44],'Both entries identify the complete interlinear phrase as typewritten and record its replacement position.'),
(11,[21],'The decision records overprinting in es of lesquels and son of sont and preserves both local doubts.'),
(12,[63,65,50,51],'The cancelled éviter candidate remains uncertain under dense x marks; the independent a/c overprinting in vérifiaation/vérification retains both alternatives.'),
(13,[53,59,61,64],'This is a source scope flag. The recorded handwriting inventory consists of folios, local rewrites/insertions and marginal strokes; these entries document those features without asserting a new long handwritten passage.')
])
add(25,56,[
(1,[89],'The foliation decision explicitly confirms51 above and56 below, both handwritten, after inspection of the complete margins.'),
(2,[4,90],'The digit after dim f(X) remains an uncertain2; the earlier overprinted impression is not recovered. The comparison sign is separately identified as pen.'),
(3,[91],'The decision follows both arms of the insertion bracket to the comma after X(k) and records the full handwritten Soit n≥2 phrase.'),
(4,[10,17,92,96],'Both Considérons corrections were inspected independently: pen C, o over a, and s over t, while the intervening n remains typed.'),
(5,[13,15,95],'The cancelled b hypothesis is read in full, its k bar is pen, and the next old clause is resolved as ou si n≥3 with pen comparison.'),
(6,[22],'The words sur L are identified as typed and their pen bracket is attached immediately before s’annulent.'),
(7,[100],'The complete c insertion, including barred k and final point, is recorded with attachment after n≥3.'),
(8,[101],'The cancelled pen word above génériques retains the tangentielles candidate because its internal letters remain obscured.'),
(9,[102,103],'The comma over the old point remains layer/undertext uncertain, while both pairs of pen quotation marks and their placement are independently recorded.'),
(10,[105],'The decision identifies the pen less-or-equal over the blot and explicitly leaves its underlying character unreadable.'),
(11,[30],'The c/b alternative in the clause label is retained from the visible bowl and second stem; the closing parenthesis is secure.'),
(12,[109],'The final degree3 is explicitly identified as a handwritten digit in a typed blank.'),
(13,[89,91,100,110],'The source scope flag is linked to the page’s recorded handwriting inventory: folios, a bracketed hypothesis, the short c insertion and the final one-word insertion. No additional long block is inferred.')
])
add(25,57,[
(1,[1,50],'The clipped upper digit permits52 or92, replacing the former single92 candidate; the lower pencil57 and full margins are recorded.'),
(2,[4],'The cancelled phrase after fait pareil is resolved word by word, including the final t with lowered1.'),
(3,[55,56,57],'The long cancellation is supported by continuous horizontal boundaries and linked side curves around ce qui exige...que X, with the nested typed cancellation and exceptional-case bracket separately recorded.'),
(4,[10,11,12,62],'The rotated marginal note is read across both scans; sont is restored, the Q/R squares are resolved, and matching oblique dotted marks attach the note after alg ind.'),
(5,[9,60,61],'The post-P-formula cancellation remains unreadable, while the overprinted Q/P letters retain explicit doubts; the two quotient identities are separately recorded.'),
(6,[13],'The final reference character retains1/L/stray-mark alternatives, with8.18 also retained; no reference repair is made.'),
(7,[67,68,18],'The result-on-pi-like-symbol query and the final f candidate remain doubtful. The same final handwritten block also records the abbreviated imm/immer reading without spelling it out.'),
(8,[62,63,67,68],'The affirmative long-handwriting flag is documented by the fully read rotated marginal paragraph, cancelled multi-line remark, and final handwritten lines.')
])
add(25,58,[
(1,[73],'Every dual accent over P is explicitly inventoried as a pen V, with occurrences inspected separately.'),
(2,[2,75],'The former11 candidate is resolved as handwritten12; the independent a/o overprinting in faisans/faisons remains doubtful.'),
(3,[77,4],'The two marginal words de choses attach before qui, while the overwritten ending of aurait retains uncertain ent.'),
(4,[5,78],'The old group after codim is retained as doubtful et under pen cancellation; the opening quote is separately identified above the cancelled t.'),
(5,[10],'The previously unrepresented stroke above dans is encoded as a doubtful bar/circumflex graphic note, with its function unresolved.'),
(6,[81,12],'The old quote is locally cancelled, the phrase is a typed insertion attached after linéaire, and the replacement closing quotation marks are separate pen strokes.'),
(7,[13,82],'The overprinted position in préschéma retains c/f; the stray cancelled f in quelconque and the terminal point are inspected, with the point’s writing instrument unresolved.'),
(8,[19],'The overprinted capital in f() retains F/T alternatives based on its middle and upper bars.'),
(9,[88,68],'The full near-vertical pencil rule beside the final four lines and its margin encoding are recorded.'),
(10,[71],'The foliation decision confirms handwritten53 above and58 below and includes the surrounding margins.'),
(11,[71,73,77,89],'The scope flag is linked to the recorded inventory of folios, short dual accents, the two-word marginal insertion, and the final closing mark; it does not introduce a new long-text classification.')
])
add(25,59,[
(1,[44],'The paragraph-number decision identifies the initial1 as pen before typed0.2.'),
(2,[11,53],'The small mark above O is retained as a curved arrow/accent alternative; its mathematical function remains unresolved.'),
(3,[12,54],'The typed nt is readable, but the slanted pen strokes do not securely establish replacement; the former definite overwrite is weakened explicitly.'),
(4,[13,58],'The x-like character before condition is pen-cancelled and the adjacent c remains doubtful; the changed label is independently read as cancelled Proposition and live Théorème10.2.'),
(5,[49],'The right-edge fragment l’homomo is recorded without supplying an unseen hyphen or completion.'),
(6,[3,47],'Both the upper dash/point and separate lower obscured cluster around Une are represented graphically without assigning textual meaning.'),
(7,[59],'The uniqueness phrase is read in full and its curved attachment is followed immediately before au.'),
(8,[14,55],'The formula’s typed and pen components are distinguished, and the bracket is followed from above choisie et to after F_X(-1), before the arrow.'),
(9,[17,19,21],'The scan decision identifies one continuous pair of pencil strokes beside the NB block and removes the duplicate single-mark encodings on its later lines.'),
(10,[60,1],'The lower pencil59 is recorded separately from the corrected upper folio54.'),
(11,[47,53,55,59,60],'The page’s handwritten inventory consists of local marks, a tensor attachment, a short uniqueness phrase and foliation; these records document the source’s no-long-handwriting scope flag.')
])
add(25,60,[
(1,[71,72],'The dense cancelled pen group inside its oval and its descending link are explicitly recorded as unrecovered; the55/60 foliation is separately confirmed.'),
(2,[73],'The whole cancelled interlinear handwritten line was enlarged but yielded no secure continuous reading; the approximate illegibility count remains.'),
(3,[74,75,2,5],'The P accent is pen and the note retains S.3./5.3.; the attachment is corrected from after vérifiée to after cancelled suivant and before the typed close parenthesis.'),
(4,[3,4,75],'The proposed l’avant is resolved as handwritten12, and the struck t in rattrappages is placed on the second typed t.'),
(5,[8,9,10,77],'The main oval-stemmed glyph, hooked index, field argument and membership sign are all pen; phi/empty-set and xi/zeta uncertainties remain.'),
(6,[15],'The ink cluster before2 retains both a cancelled unreadable sign and a retraced greater-or-equal reading; its function is unresolved.'),
(7,[84,16],'The old qualification beginning ce qui n’exclut pas... and the separate contraire si dim X continuation are read through the cancellation; the latter uncertainty is resolved.'),
(8,[17,85,86],'The typed clause attaches after the first fibres, its bracket is distinguished from parentheses, and the repeated sont lisses sont au plus wording is explicitly preserved.'),
(9,[91],'The final handwritten line is transcribed word by word, including the accent and terminal point.'),
(10,[71,73,91],'The scope metadata is linked to the actual handwritten-block inventory: the scratched upper note, cancelled interlinear group and final short line. No additional continuous handwritten exposition is asserted.')
])
add(25,61,[
(1,[78,1,14,86],'The diagonals across the proposition and drafting note were followed through both scans. Their function remains unresolved, so the line-by-line whole-block deletions are removed while local cancellations remain; the end of the drafting note is explicitly read.'),
(2,[16],'The long thin pencil rule from the upper paragraph toward the later isomorphism paragraph is newly recorded as a marginal stroke.'),
(3,[76],'The handwritten56 and61 and their surrounding margins are explicitly confirmed.'),
(4,[77,15,19,40,41],'All four number groups are resolved independently as typed8 overwritten by pen10, with the following decimal portions unchanged.'),
(5,[25,34,29,32,84],'The Idéal l/m and deuxième m/p positions remain doubtful, the trace after est remains graphic/letter uncertain, and the cancelled t after le is resolved.'),
(6,[26,82],'The shallow curved mark near O_P is recorded with its position but no asserted accent or mathematical function.'),
(7,[35,39,91],'The less-or-equal, final greater-or-equal2 and semicolon are all identified as pen; the comparison decision does not recover a separate old typed sign.'),
(8,[76,78,87],'The source scope flag is linked to the recorded folios, diagonal and marginal marks, and short handwritten hypothesis; the text under the diagonals is typed and remains live.')
])
add(25,62,[
(1,[1,51],'The phrase de degré is typed, attaches after étale, and ends in a pen d over an unrecovered old impression.'),
(2,[2,52],'The upper bar and lower trace around alg are recorded with a/q and g/f doubts; they are not reassigned to k(s).'),
(3,[4],'The formerly unreadable cancellation yields doubtful consiste en, doubtful r/n before clear+2, and point without an added plural ending.'),
(4,[53,54],'The new d over doubtful n is distinguished from the clear minus2, and k(s), un and final k cancellations are individually recorded.'),
(5,[7,8,58,59],'The small upper/lower title marks remain graphic uncertainties; Ratrapages is read with its separate underline and looped pen cancellation.'),
(6,[63,64,12],'The base letter remains S/X doubtful; the integer-condition insertion is typed with a pen greater-than sign, while the proposed comma is rejected as the bracket tip.'),
(7,[70,18,19],'The first two n labels and their wedge strokes are pen; the later two n labels are separately recorded as typed.'),
(8,[71],'The final retraced question-like mark is retained with unresolved function after the quotient expression.'),
(9,[60,61,11,14,66,68,15,16],'The concern’s several words have separate decisions: couramment and the clipped quelques/libres remain readable; sorties/sorttes, initial M/P of Modules and final s of naturels remain doubtful; réprésente retains both accents and its newly explicit cancelled trailing r.'),
(10,[50],'Both folios57 and62 and the complete margins are explicitly recorded.'),
(11,[50,51,58,64,70,71],'The scope flag is linked to the local handwritten inventory: folios, degree letter, title marks, comparison sign, exterior-power labels and final graphic mark; no additional long prose block is inferred.')
])
add(25,63,[
(1,[1,9],'The small raised n over the wedge is resolved and its continuous pen stroke is recorded.'),
(2,[10],'The overwritten e/a after prés remains an explicit présentation/présantation doubt.'),
(3,[11],'The candidate localement sur S remains compatible with the cancellation but not every underlying letter is separately recoverable.'),
(4,[2],'The insertion’s words and final dot are read, while the left curve remains a parenthesis/attachment alternative.'),
(5,[3],'The S and hyphen are identified as typewritten, with a pen placement curve; this revises the proposed hand-letter layer.'),
(6,[14],'Both words sommes directes are readable under typewriter x cancellation.'),
(7,[16],'The short cancellation after rang n remains unreadable; no underlying word is supplied.'),
(8,[5,6,18],'The letter in vectoriel retains c/d; the V-formula is pen-cancelled and its primes/tensor details remain unresolved.'),
(9,[17],'The wavy pen underline is followed across par immersions and the next-line ouvertes.'),
(10,[19],'The typed (- membership surrogate is explicitly recorded; the mathematical membership encoding is documented without adding a new source symbol.'),
(11,[8,21],'The top pen58 and lower pencil63 are separately recorded.'),
(12,[15],'The exact sequence is inspected term by term and the two middle connectors remain without clear arrowheads.'),
(13,[2,3,17,8,21],'The scope flag is linked to the short insertion, placement stroke, underline and folios; the complete page record reports both parts and all margins read.')
])
add(25,64,[
(1,[13,25],'The clipped upper folio retains the57 candidate, while lower64 is read in pencil.'),
(2,[3,4,5,6,8,9,10,23,27,28],'The E/G/P dual marks are individually identified as pen, including those in the quotient expression. The later placement amendments preserve the distinction between the pen insertion’s internal accent and the next live P accent.'),
(3,[20],'The first displayed E remains plain without underline, and the overtyped opening delimiter remains a parenthesis reading.'),
(4,[17,18,22],'The three insertions are typed with pen attachment strokes; n≥1 lands before the stop, de rang r follows libre, and duale L with raised o follows linéaire.'),
(5,[2,7],'The two cancelled strings are recovered only as doubtful (resp. vide) and (r-1)-m; cancellation x marks are not printed as lexical content.'),
(6,[1],'The second letter in De retains e/g alternatives from the merged bowl and lower loop.'),
(7,[21,22],'Quotient and linéaire remain readable through overtyping; the latter is also checked with its attached duale insertion.'),
(8,[19],'The underlined E in soit E son dual visibly lacks a dual accent, and none is supplied.'),
(9,[24],'The terminal punctuation after ainsi is edge-clipped; the comma reading is retained explicitly.'),
(10,[14,17,18,22,23,25],'The recorded pen material consists of local parenthetical/phrase insertions, accents and foliation; the complete-page visual record includes all text and margins without an additional long handwritten block.')
])
add(25,65,[
(1,[9,10,40],'Only lower portions of the uncertain typed top digits survive; the hand60 and lower pencil65 are independently read.'),
(2,[1,11,12,13,15],'Permettant is resolved, the initial L/l correction remains doubtful, and the P dual accent and both commas are individually identified as pen.'),
(3,[16,17],'The va position remains obscured by cancellation, while the circumflex over typed u is clearly pen.'),
(4,[20,21,22],'The quotient G remains uncertain over another bowl; the L de P insertion is typed, with pen comma and attachment before détermine.'),
(5,[23,24,25],'The inclusion hook and both subsequent rightward arrows are each inspected for layer and direction.'),
(6,[26],'The visible right-cropped letters agree with ssi; the edge condition is explicitly recorded.'),
(7,[7,8,30,33,34,35,38],'The general-functor subscripts retain point/star alternatives, and the coproduct n retains uncertainty where it merges with the underline; the surrounding formula lines are individually read.'),
(8,[35],'The long underline beneath Les sous-variétés linéaires is recorded with the coproduct line.'),
(9,[6],'The string xxbxix does not yield a readable underlying word and is replaced by an illegibility mark.'),
(10,[27,28,29,30,31,32,33,35,36,37,39],'The complete section12 heading is struck by a long pen line, and the following handwritten replacement passage is documented line by line, including its final mixed bracket.'),
(11,[28,29,30,31,32,33,35,36,37,39],'The affirmative flag is supported by the separately recorded full handwritten addition, from its introductory sentence through its final rank parenthesis.')
])
add(25,66,[
(1,[13],'The upper pen folio is clipped;21 remains the recorded candidate without increased certainty.'),
(2,[3],'The last Gr index is resolved as plain m followed by pen-cancelled doubtful+1; the same entry records plain E and its pen dual accent.'),
(3,[15,18],'Both cancelled phrases have separate records: de rang remains partly merged with x marks, and La relation di retains an indistinct ending.'),
(4,[16,17],'The caret attaches a handwritten underlined G after quotient; the right-edge canoniqu fragment is left incomplete.'),
(5,[8,1,2,6,7,9,12],'Da is resolved as printed; the dual accents and final phi, membership sign and Gamma are pen, revising the proposed typed layers.'),
(6,[20],'The bottom-left66 is explicitly recorded as pencil.'),
(7,[13,16,20,21],'The source scope flag is linked to the local handwriting and complete-text inventory, including the short G insertion and folios.')
])
add(25,67,[
(1,[1],'The clipped pen folio is revised to a doubtful62 from the surviving lower curves; its top remains absent.'),
(2,[13],'The overtyped pr and the collision before d’incidence are explicitly retained.'),
(3,[15],'The first letter of Gr remains overtyped and unresolved; no unique replacement is chosen.'),
(4,[3,14,16],'The old underlined letter is pen-cancelled and remains doubtful; both zeta occurrences are separately recorded as pen with their positions.'),
(5,[4,5],'Both sur insertions are identified as typed, with handwritten placement curves; the second retains S prime.'),
(6,[17],'The long pencil rule spans the autocritique paragraph and ends near the next one.'),
(7,[8,22,23],'The separate digit1 beneath Grass is secure and its anomalous position retained; the dollar-like overstrike and pen F dual accent are independently recorded.'),
(8,[10,11,24],'The overtraced isomorphism sign, underlined Omega and terminal comma are all recorded as pen.'),
(9,[25],'The lower67 is explicitly read as pencil.'),
(10,[4,5,17,23,24,25],'The metadata flag is linked to the actual inventory of local insertions, rule, accents, punctuation and foliation; no additional hand paragraph is inferred.')
])
add(25,68,[
(1,[14,25],'The top pen63 is read directly and the bottom pencil68 is retained as a margin entry.'),
(2,[1,15],'The typed dimension phrase attaches after rationelles); the separate pen slash remains visible at des/fibres instead of being treated as the phrase’s insertion target.'),
(3,[18,19],'The retouched f and the middle gu/g correction are separately recorded; original letters and intended resulting word are not reconstructed beyond the visible doubts.'),
(4,[17],'The crossed internal glyph remains compatible with z but is not fully separable from overprinting.'),
(5,[20],'The G dual accent is pen, while the tiny dot near E is recorded as a nonalphabetic mark.'),
(6,[5,27],'The final1 is resolved as handwritten, with the later placement amendment confirming the separate pen comparison on that line.'),
(7,[7,8],'The middle name vowels retain eu/uu alternatives; the final il is a live doubtful overprint rather than a typewriter cancellation.'),
(8,[23],'The crossed glyph within signifie remains indistinct; no extra letter is supplied.'),
(9,[26],'Every listed spacing artifact is explicitly checked and preserved.'),
(10,[16,2,3],'One pencil bracket spans the three lines; later duplicate margin encodings are removed.'),
(11,[14,15,16,18,19,20,25],'The scope flag maps to the recorded local handwriting inventory and folios; the actual extent is documented without assigning a new long-text threshold.')
])
add(25,69,[
(1,[2],'Plus bas is resolved and its pen curve places it before commentaires.'),
(2,[12,13,16,17,20,21,22,25,26],'The comparison signs are individually recorded as wholly handwritten, including their angled and lower strokes; the final m+1 bound is also wholly pen.'),
(3,[18],'The small question mark over hypersurfaces is explicitly read with its hook and attachment.'),
(4,[24],'The looped C-like glyph retains its script/fraktur alphabet alternatives without normalization.'),
(5,[3],'The second typed vowel is resolved as a, preserving da.'),
(6,[9],'The pen joining stroke is encoded as removal of the typed space between ce and la.'),
(7,[27,28,6,30,31],'The three cancelled phrases are readable, while the upper parenthesized m-like group remains doubtful and the lower stacked group remains illegible.'),
(8,[29,32,33,34,35,36],'Each xi occurrence, the tensor sign and membership sign is individually recorded as pen with its position.'),
(9,[37,38,10,11],'One shaded double bar spans the final lines and duplicate margin entries are removed; the lower69 is pencil.'),
(10,[2,18,24,37,38],'The flag is linked to short pen insertions/symbols and marginal marks within the complete page record; no separate long handwritten prose is asserted.')
])
add(25,70,[
(1,[2,31],'The top65 and bottom70 are separately read as pen/pencil foliation.'),
(2,[4,5,6,7],'The old généralisation, cancelled typed variante pour le, final typed généralisation au and cancelled old au are individually recorded in their visible layer order.'),
(3,[8,9],'The cancelled short Sm candidate remains obscured, while the inserted parenthesized S_m is read as typed.'),
(4,[10,13,14,18,19,21,22,24,25],'The Greek point indices and each listed comparison are individually recorded as pen, with directions and adjacent bounds checked.'),
(5,[11],'The overlapping m/p position in Théorème remains doubtful.'),
(6,[12],'The wavy underline is handwritten and the whole word Proposition remains legible; no alternate spelling is selected.'),
(7,[15],'The overwritten a position in notation retains its doubt.'),
(8,[16,17],'The article position remains doubtful while the full cancelled hypothèse is legible under x marks.'),
(9,[20],'The final digit after dim X- is clipped and retains its1 candidate without increased certainty.'),
(10,[23],'The pen m and surviving upright of the old typed1 are separately visible and recorded.'),
(11,[27,28],'The30-comma insertion and caret before31, and the independent terminal semicolon, are both pen.'),
(12,[29,30,2,31],'The metadata flag is linked to the two explicitly read closing handwritten lines and folios; these decisions document their actual extent without imposing a numerical long-handwriting threshold.')
])
add(25,71,[
(1,[1,2,12,13,14],'The cancelled opening retains its initial phrase alternatives; exact and the e) in8.7 are resolved, and the remaining cancelled wording is recorded through quelconque.'),
(2,[15],'The merged pair in développements retains its local el reading uncertainty.'),
(3,[16],'The extra p in s’apdapter is visibly retained without a spelling repair.'),
(4,[18],'Mieux, exercices and faite are individually legible through their overtyping.'),
(5,[17],'The small x-like mark below the baseline after D’autre retains uncertain production layer.'),
(6,[5,6,19,20,21,22,23],'The dimension phrase is typed, its comparison and f-arrow are pen, and the curve is an attachment rather than a parenthesis. The proposed handwritten=V^o is corrected to a typed insertion above the cancelled impressions.'),
(7,[7],'The overprinted n/g position retains singuliers/sigguliers alternatives.'),
(8,[8,24,25],'Phi and both xi occurrences are separately identified as pen; the m exponent remains typed.'),
(9,[4,9],'The first cancellation supports doubtful généraux and the later one supports doubtful2, et X non vide; neither recovery is made certain.'),
(10,[10,28],'The insertion remains a doubtful reading of passant par x et qui; its curve is recorded as an attachment rather than content punctuation.'),
(11,[29],'The sign’s direction appears to be contains and x is present, but the small interior stroke remains doubtful.'),
(12,[11,30],'The upper66 and lower pencil71 are separately confirmed.'),
(13,[19,20,21,28,29,30],'The flag is linked to the documented local insertions, mathematical symbols and foliation; their actual scope is recorded without inventing a longer hand passage.')
])
add(25,72,[
(1,[12,42],'The top67 and lower pencil72 are independently read.'),
(2,[13,14,15,17,18,19,32],'The point symbols and all listed intersection signs are individually recorded as pen, with their baseline or subscript positions.'),
(3,[21],'The faint closing curve after n-m+2 is retained without assigning a mathematical or editorial role.'),
(4,[1,22,2],'The underlined X is corrected to cancelled text, the short mx candidate remains obscured, and the following cancellation is resolved as autre que.'),
(5,[27],'Both shhéma and schéma remain compatible with the merged typewriter layers.'),
(6,[6,30],'The mark after the reference retains parenthesis/section-sign alternatives; the later closing parenthesis after nes is secure pen.'),
(7,[33],'The cancelled two-line dimension expression retains its doubtful candidate because only dim, V(k) and parts of the polynomial are securely visible.'),
(8,[39],'The typed de Grass^m insertion is placed immediately after d’ensembles, before de codimension, by the connecting loop.'),
(9,[41],'The retouched ending of envisagé remains doubtful where pen and type overlap.'),
(10,[29,5,7,8],'One pencil bracket spans the four lines, and duplicate margin entries at the following lines are removed.'),
(11,[21,23,29,39,41,42],'The scope flag is linked to the recorded local curves, insertion, bracket, ending retouch and foliation within the complete page review.')
])
add(25,73,[
(1,[9],'The overtyped group in relativement is recorded with unresolved underlying character rather than a normalized spelling.'),
(2,[1],'The second letter before loc cit retains e/g alternatives.'),
(3,[11,12],'The union sign and rightward arrow to Grass are independently identified as pen.'),
(4,[13],'The upper dash and lower retouch around r are recorded without forcing a reconstruction of the letter layers.'),
(5,[14],'A pen closing parenthesis is present beside the typed one, and both are retained.'),
(6,[15,16],'The long pencil rule’s full paragraph extent and the separate right-edge cross beside Il are recorded.'),
(7,[22,23,26],'The ending of cette remains doubtful, the comma after tion is pen, and the right-edge decision records clipping without supplying unseen text or punctuation.'),
(8,[7],'The middle ariét group is encoded as an uncertain pen-over-type retouch, with both layers unresolved.'),
(9,[26, 27],'D0026 explicitly records the clipped utilisant/dans/des/une group. The focused D0027 separately records the visible l/e and surviving s curves of les at the Grass-arrow line edge, retaining the existing word without supplying anything beyond the clipped glyph.'),
(10,[8,25],'The top68 and lower pencil73 are separately read.'),
(11,[15,16,20,21,25],'The scope flag maps to the actual local pen inventory: marginal marks, two short insertions and foliation, within the complete-page record.')
])
add(25,74,[
(1,[1,15],'The clipped pen number retains69/61/6 alternatives from the surviving loop and descender; its hand layer is secure.'),
(2,[16],'The accented a/u phrase remains overprinted and no unique corrected spelling is chosen.'),
(3,[17],'The last factor retains its overtyped C-like candidate without mathematical substitution.'),
(4,[18],'The old typed10 and pen retouch are recorded, with18 still doubtful because of merged loops.'),
(5,[4,20],'The dimension phrase is typed but the comparison is resolved as handwritten greater-or-equal.'),
(6,[20,22,23,25,28,30],'Each listed insertion is separately recorded as typed, with its attachment; the raised1 of T1 is retained.'),
(7,[33,34],'Both cancelled clauses retain their doubtful candidate wording and obscured variables; the record does not promote the partly recoverable formula to certainty.'),
(8,[36],'The pencil rule’s extent beside the restored hypotheses is explicitly described.'),
(9,[41,42],'The cancelled quoted prefix and capital S are read, while the closing-quote layers near the colon remain merged.'),
(10,[44],'The letter in Q() retains Z/C alternatives from the overprint.'),
(11,[45],'The full final handwritten line is read, including Q(C), the intersection with Z, quoted assez général, and its final Z.'),
(12,[36,43,45,46],'The metadata flag is linked to the marginal rule, local rait insertion, single final handwritten line and foliation; their actual extent is recorded without a new threshold claim.')
])
add(25,75,[
(1,[46],'The foliation entry reads70 above and75 below directly from both handwritten numbers; it does not infer an archival role for either.'),
(2,[47,49,39,41],'The theorem insertions are individually read with typing layer and curves; et affine is identified as typed and pen-cancelled; que si n>0 and the inserted et are recorded at their respective attachments, with the greater-than sign identified as pen.'),
(3,[3,4,6,22,23,9,10,13],'The cancelled élém, un, étale sur, peut supposer and Lorsque n=1 are resolved as readable; multip-élémentaire and the shorter peut suppo retain their recorded doubts. Cancellation x impressions are not incorporated into the underlying words.'),
(4,[18,19],'The cancellation after connexes is recorded with the comma candidate still explicitly doubtful.'),
(5,[45,50],'Both records identify the l in n’exclut as a pen retouch over the typed letter.'),
(6,[44,51],'The overwrite entry retains the typed e and apostrophe-like pen stroke in qu’alors.'),
(7,[30,31,32,48],'The two handwritten parts il revient au and même de are read above the cancelled on...es and ramené à openings; the separate cancellation and attachment entries preserve both layers.'),
(8,[46,47,48,49,50,51],'The scope flag is linked to the recorded folios, interlinear insertions, short handwritten rewrite and local retouches; these document the actual handwriting extent without a new numerical length criterion.')
])
add(25,76,[
(1,[27],'Both handwritten folios are read as71 above and76 below; the decision makes no unsupported assignment of archival roles.'),
(2,[13,28],'The opening K/k overtyping retains both case candidates because both traces remain visible; no order of impression is asserted.'),
(3,[2,6,20,21,22,23,29],'The general cancellation concern is linked to the individual entries for all four listed draft phrases; lisse et is resolved while the denser phrases retain the recorded uncertainties.'),
(4,[2,15,16],'The cancelled lisse et is directly resolved as readable through the x impressions.'),
(5,[6,18,19,29],'The ending is revised to doubtful Soit Noter qu’on, with the apostrophe-like impression and on recorded rather than the earlier qui proposal.'),
(6,[20,21,29],'On voit on peut remains explicitly doubtful under dense cancellation, as the phrase-specific entry records.'),
(7,[22,23,29],'The full cancelled supposer que X n’est contenu dans Alors remains doubtful; the existing record expressly retains the obscured letters.'),
(8,[24,30],'The decision identifies the raised r as handwritten and the P as retouched or underlined, preserving the observed production uncertainty.'),
(9,[25,26,31],'The right marginal mark remains a doubtful rising arrow/check-like stroke; its shape is not resolved into a certain function.'),
(10,[1,5,10,12,33],'The comparison-layer decision explicitly supersedes the NOTES suggestion of typed composites and identifies the inequalities as pen strokes; their individual occurrences are also recorded.'),
(11,[32],'The short underlines beneath tout and et are explicitly confirmed.'),
(12,[27,30,31,32,33],'The scope flag is connected to the recorded folios, raised r, marginal mark, underlines and comparison strokes, documenting local handwriting without claiming a newly read long passage.')
])
add(25,77,[
(1,[14,41,42],'The two folios are directly read as72 above and77 below; their observed locations are recorded without inferring an author/archive classification.'),
(2,[16,17,24,25,43],'The typed dimension insertion is attached before X-Z by the recorded bracket; the less-or-equal and greater-or-equal signs are individually recorded as handwritten.'),
(3,[2,20,21],'The final handwritten s of lisses is resolved as clear, removing the earlier letter doubt.'),
(4,[11,29,30,31,32,33,34,35,36,44,45,46],'The audit explicitly extends the long cancellation through l’on ait C∩Y=∅, superseding the NOTES live reading. It records the et x∉C insertion above that clause before cancelled même, and preserves the illegible deleted word inside the new finite-set phrase.'),
(5,[38,47],'The overtyped C/E remains a merged layered glyph with both candidates retained.'),
(6,[48],'The four ordinary words parfait, codimension, projectif and Grass are explicitly compared and retained from their readable final letters.'),
(7,[42,43,44,45,46],'The scope flag is linked to the actual folios, dimension insertion, handwritten finite-set phrase and local cancellation/insertion records; no numerical threshold for long handwriting is inferred.')
])
add(25,78,[
(1,[1,2,40],'The framing curve fixes the complete top typed line after T_Q before soient; the overtyped qui/qbi doubt remains. Disjoints is also identified as a typed insertion above that line.'),
(2,[18,19,20,41],'The cancelled construction and handwritten hypothèse essentiellement replacement are recorded together; the cramped middle strokes leave the replacement explicitly doubtful.'),
(3,[3,5,6,7,8,43],'Le morphisme and pré are resolved as readable, and the four short x-outs are individually inventoried as en, an unread group after Z prime, Et and un. The specific inventory D0043 governs the remaining illegible group.'),
(4,[21,22,23,26,42],'All four zeta occurrences are individually checked, and the summary records pen zeta with typed subscript o.'),
(5,[11,14],'The overtyped T/Z in the difference and L/E in L_o∩X are explicitly retained as alternatives; the intersection sign is identified as pen.'),
(6,[15,38,39],'Both handwritten folios are read as73 above and78 below.'),
(7,[39,40,41,42],'The scope flag is tied to the recorded folios, typed-line attachment, short handwritten replacement and pen zeta inventory, documenting actual layers rather than positing a new long passage.')
])
add(25,79,[
(1,[20,21,56,57,58],'The upper folio is read74; the lower is corrected to79 from its closed9 loop and descending stroke, superseding the75 candidate.'),
(2,[1,2,3,59,64],'The audit traces separate attachments for the two typed additions, placing the first after a) and the parenthesis after cela résulte. The mark after L is a lowered handwritten eta; actual square brackets before Il pourrait and after à part are distinguished from the insertion connector.'),
(3,[35,43,48,51,60],'All four generic-point symbols are explicitly inventoried as hooked handwritten eta forms; the individual positions remain recorded.'),
(4,[6,34,61],'The complete condition is identified as typed with a handwritten comparison sign and retained at its bracket attachment after P(k). The overtyped initial before image remains l’/m’ doubtful.'),
(5,[7,8,36,37],'The e of de is resolved as readable, and the following x-cancelled word is recovered as sous.'),
(6,[12,41,42],'The raised ampersand is resolved as clearly typewritten, superseding the handwritten/doubtful proposal.'),
(7,[15,19,45,46,49,50,62],'The co insertion and n- deletion are individually recorded, together with the handwritten comparison; the cancelled on a is resolved as readable.'),
(8,[28,44,63,64],'The short and long left marginal brackets have their extents recorded; the separate literal square brackets are retained at their actual endpoints.'),
(9,[59,60,62,63,64],'The scope flag is tied to recorded attachment paths, point glyphs, local codimension correction and marginal brackets; the long verbal additions are explicitly typed.')
])
add(25,80,[
(1,[14,51,52],'The recorded folios read75 at the top and80 at the lower left, both handwritten.'),
(2,[15,54],'The vertical margin bracket is explicitly followed from the first line through on en forme.'),
(3,[16,17,53],'The hooked point index retains eta/xi uncertainty; neither candidate is silently resolved.'),
(4,[1,18],'The audit replaces an unsupported deletion of me by a live codimension/codimemsion overtyping doubt, preserving the visible middle-letter ambiguity.'),
(5,[22,23,55],'The cancelled letter before a section remains doubtful l-like under x cancellation; expected wording is not restored.'),
(6,[56],'The individual overtyped words puis, linéaires, par, presque and ce qui est loisible are explicitly compared and retained as readable final words.'),
(7,[4],'The comparison sign in codim T≥2 is identified as drawn by hand.'),
(8,[27,28,31,57,58],'The pen Q after l’hyperplan, V-shaped accent over P and interlinear eta are recorded with their attachments; the documentary link preserves the recorded glyph forms.'),
(9,[29,30,31,32,58],'The H subscripts and generic-point symbols are each compared as handwritten forms, with their existing positions preserved.'),
(10,[8,35,59],'The complete typed parenthesis and its placement after cancelled tout are explicitly recorded; the earlier xxxx group is resolved to tout.'),
(11,[9,36],'The typewritten k in X(k) is resolved as readable despite overtyping, and the adjacent membership sign is identified as pen.'),
(12,[39,60],'The singular-locus arrow is recorded as a pen arrow directed toward T.'),
(13,[40,41,43,44,45,46,48,49,50,61,62],'Both brace pairs, the quotations, closing parenthesis, inserted T and orthogonal are individually recorded as pen marks or insertions, including their positions.'),
(14,[52,54,57,58,61,62],'The scope flag is connected to the recorded folios, margin bracket, point symbols and short pen additions; their extent is documented without a new long-handwriting threshold.')
])
add(25,81,[
(1,[11,27],'The superposed X/C remains doubtful because the final typing order cannot be separated from the image.'),
(2,[2,12,13,14,28],'Both complete cancelled example lines are explicitly read, including the repeated où; part is resolved as readable through the x impressions.'),
(3,[3,15,29],'The small stroke after P is identified as the continuation of the placement curve for typed non singulière; the audit reads no separate exponent there.'),
(4,[30],'The listed overtyped words montrent, une extension, polyélementaires, faible and subsiste are individually compared without spelling normalization.'),
(5,[10,22,23,25,26,31,32],'The added c) arrow points to the gap after donnée, the next typed c is overwritten d, and both folios76/81 are directly read; these entries record locations without assigning unproved archival roles.'),
(6,[26,29,31,32],'The scope flag is linked to the folios, insertion connector, added label and local renumbering/word addition actually documented on this page.')
])
add(25,82,[
(1,[20,50,51],'Both handwritten folios are read77 above and82 below.'),
(2,[2,3,21,22,23,24],'The first cancelled phrase is recovered as doubtful sur S tel que X, while the cancelled abbreviation géomé is resolved as readable; cancellation x marks are removed from the proposed underlying wording.'),
(3,[25,52],'Pré is explicitly identified as a typed interlinear insertion with its attachment checked.'),
(4,[7,8,28,29,30,31,32],'The cancelled phrase is resolved as ait des fibres de, and handwritten satisfasse is read above the pen-deleted soit tel que.'),
(5,[33],'The less-or-equal sign is recorded as handwritten.'),
(6,[54],'Fondamental and ouverts are explicitly checked as overtyped but readable final words; the recorded source spelling is preserved.'),
(7,[14,36],'The line-ending t-like overstrike and hyphen are retained as t/hyphen alternatives at the same position.'),
(8,[16,37,38],'The audit identifies typed interlinear (k) with a pen bar, attached after the finite-part symbol without exponent placement; the membership and finite-part glyphs are separately handwritten and the latter remains phi/empty-set doubtful.'),
(9,[17,41,42,43,44,45,56],'The first générique is readable; the next ending remains doubtful under dense overprinting. The preceding cancellation supports les L and the small lower mark retains comma/subscript-i alternatives.'),
(10,[19,48,49],'The final pen glyph is resolved as U; the slash-like stroke is recorded as its insertion attachment.'),
(11,[59],'The remark-label decision explicitly confirms typed c), then e).'),
(12,[51,52,55,57,19],'The scope flag is tied to the documented folios, typed interlinear material, short handwritten correction and final U insertion, preserving their actual writing layers.')
])
add(25,83,[
(1,[1,4,5],'The overwritten upper folio retains78 bis/77 bis alternatives; bis is clear while the second digit is unresolved.'),
(2,[24,31],'The lower pencil83 is explicitly read, and the lower scan is recorded as otherwise blank; no archival role is inferred.'),
(3,[7,8,9,25],'The not-equal sign and replacement1 are clear pen forms; the underlying typed character remains illegible.'),
(4,[12,13,14,26,27],'Donc is recorded above the deleted comme d’ailleurs at the connective before U; the semicolon is a pen correction over the typed comma after libres.'),
(5,[3,16,17,18,20,21,28],'Typed un, pen quotations/comma and the classifiant/pour underlines are individually recorded. Nearby x impressions belong to the cancelled homotopiquement candidate, whose obscured letters remain doubtful.'),
(6,[6,11,19,22,23,29,30],'All five pi signs are recorded as hand-completed; the C in C^n is explicitly read as typed, underlined and followed by raised n.'),
(7,[25,26,27,28,30,31],'The scope flag is tied to the recorded local pen corrections and glyphs; the lower half is explicitly documented as blank except for its folio.')
])
add(25,84,[
(1,[11,27,28],'The foliation entries read78 above and84 below from the handwritten numbers.'),
(2,[12,29],'The two pencil strokes beside the NB paragraph have their extent and placement explicitly checked.'),
(3,[13,30],'Sorite is resolved as readable; the overtyped n in grassmannien remains doubtful.'),
(4,[15,31],'The full typed codimension insertion and its attachment after S are explicitly recorded.'),
(5,[24,26,35,36],'The placement curves are traced to L’image for au sens foncteurs and to L for de la dimension voulue; the former is not attached to the preceding de P(G).'),
(6,[20,21,34],'The cancelled opening before Plus remains a doubtful parenthesis-like shape under overstrike.'),
(7,[33],'The second Grass index is read r-m+1, retaining the visibly overtyped m.'),
(8,[32],'The overtyped capital in the first displayed P(G) remains readable as P without substitution.'),
(9,[28,29,31,35,36],'The scope flag is tied to the recorded folios, double margin rule and attachment curves for explicitly typed insertions.')
])
add(25,85,[
(1,[37],'The foliation decision directly reads79 above and85 below.'),
(2,[1,16],'The middle group retains amn/men/mmm alternatives; the audit does not normalize the word to codimension.'),
(3,[2,17,18,38],'The overstruck final letter of entend is a doubtful s under cancellation; the right crop exposes only part of the final e after qu, whose doubt remains.'),
(4,[5,19],'The end-of-line overstrike is recorded as a t-like stem with possible colon remnant, retaining t/t: alternatives.'),
(5,[6,21,22,39],'The full handwritten notation addition is read. The first p has a visible C subscript and an unresolved f/Sigma-like overwritten exponent; both later notations remain clear.'),
(6,[7,23,40],'The long curve is explicitly traced as the notation-insertion connector landing before On; the typed sentence remains live on this visual evidence.'),
(7,[9,24,25],'The isolated faint stroke retains slash/closing-parenthesis alternatives.'),
(8,[10,12,41],'The diagram has one overtyped Q/G-like index glyph and a cancelled doubtful z-like mark beside p; the later argument is one overtyped C/Q glyph. No doubled letters are introduced from the former encoding.'),
(9,[34,42],'The competing b/l-like stem and bowl in simpbe/simple remain unresolved.'),
(10,[35,43],'Handwritten ou p_C is explicitly attached before the comma after p_C^X.'),
(11,[36,44],'The added comma after X is identified as a pen mark below the baseline.'),
(12,[37,39,40,43,44],'The scope flag is linked to the recorded folios, handwritten notation phrase, its connector and two short final additions, without an invented length criterion.')
])
add(25,86,[
(1,[18,19,50,51,59],'The clipped upper folio remains an uncertain80-like reading based on lower digit portions; the lower pencil86 is clear.'),
(2,[1,20,21],'The p index is recorded as doubtful C crossed by irregular pen hatching, superseding the typewriter-cancellation proposal.'),
(3,[2,27],'The overtyped pair in projection retains ro/oo alternatives rather than silently adopting the expected word.'),
(4,[28,52],'The Grassmannian argument retains the visible E/P overtyping alternatives.'),
(5,[5,29,30,32],'Both handwritten point glyphs retain eta/y ambiguity, including the repeated occurrence in the X subscript.'),
(6,[6,33],'The first two letters of arguments retain ar/aa alternatives under overtyping.'),
(7,[7,35,36,37],'The closing parenthesis and inserted de are identified as typed, with a thin pen connector; the following typed de remains cancelled.'),
(8,[11,42,43,44,45,54],'The cancelled wording before the reference stays doubtful as (dém. de, while13.3 is recovered as readable.'),
(9,[13],'The enlarged audit records one heavy underline beneath X, superseding the proposed double line; its Q index is hand-completed.'),
(10,[14,15,16,17],'All four tildes are identified as pen; the first two span X or F alone, leaving parentheses outside. The C/O overtyping inside F(C) remains doubtful.'),
(11,[46,56],'The apostrophe-like mark in n’en remains unresolved under merged overtyping.'),
(12,[47,48,49,57],'The small handwritten ici-like replacement above cancelled précédent retains its cramped-stroke doubt.'),
(13,[9,10,39,40,41,55],'The margin mark is one continuous pencil rule across three lines; repeated encodings are reduced to its first attachment.'),
(14,[51,55,57,59,14,15,16,17],'The scope flag is linked to the recorded folios, single margin rule, short replacement and pen tildes, preserving the observed handwriting extent.')
])
add(25,87,[
(1,[121,122],'Both folios are directly read as81 above and87 below; their documentary roles are not inferred.'),
(2,[51,52,53,123],'The three opening comparisons are individually recorded as pen greater-or-equal, less-or-equal and less-than signs.'),
(3,[1,57],'The apparent extra parenthesis is identified as the existing closing parenthesis of k(point), followed by a typed comma; no second parenthesis is read.'),
(4,[2,59,60],'The cancelled short group before dans5.3 gains ink-based que/(cf candidates, both still doubtful.'),
(5,[3,63,64],'Précise contains one overtyped c/s position; the earlier separate cancelled-letter encoding is removed.'),
(6,[5,70,125],'The C is explicitly recorded as typed and retraced in pen; the adjacent touched semicolon retains semicolon/comma alternatives.'),
(7,[8,78,79],'The cancelled phrase before dans le cas is recovered as doubtful D’autre part, with punctuation still obscured.'),
(8,[11,84,85],'The mark is recorded as a retouch of the initial p of projection, preserving its doubt rather than adding a separate parenthesis.'),
(9,[89,90,91,92,126],'The cancelled a) Si dim X is read; the tiny e/ou overwrite before plus remains uncertain in both layers.'),
(10,[15,16,17,18,19,20,21,105,106,107,109,111,128,129],'The dense b) revision is documented by its comparison, full inserted hypothesis, non vides attachment, marginal morphism,0-to-d overwrite, deleted quasi-finite clause and revised conclusion; unresolved point and abbreviation readings remain explicit.'),
(11,[16,101,102,128],'The whole inserted hypothesis is read and traced to les fibres. The wording is dim d, with ttes/tts uncertainty and a semicolon-like final mark; the earlier dimen expansion is removed.'),
(12,[18,104],'The marginal morphism insertion remains at the recorded p_C attachment, with eta/y alternatives preserved in both point occurrences.'),
(13,[107,111,129,21],'The audit records two doubtful resp. quasi-fini additions and removes only the duplicate third encoding of the same circled right-margin phrase.'),
(14,[20,111,129],'The replacement f:X→P est fini and its handwritten closing bracket are recorded; the two abbreviated qualification phrases remain doubtful.'),
(15,[128,129,130],'This request to check the dense lines is linked to the explicit full-hypothesis and full-conclusion enlargement records, together with the cropped-edge inventory.'),
(16,[130],'The terminal dimension d and quasi-fini are recorded as reaching the cut edge; no unseen continuation is supplied.'),
(17,[122,124,127,128,129],'The scope flag is linked to the actual folios, typed Module insertion, moved pen phrase and longer revised b) material; no new length threshold is imposed.')
])
add(25,88,[
(1,[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46],'The occurrence-specific decisions preserve eta/y ambiguity throughout the looped generic-point glyphs, including the wholly handwritten k(point) subscript.'),
(2,[27,28,29,60,63,102],'All three questioned comparisons are identified as wholly pen-drawn angles and lower strokes; the proposed underlying typed greater-than layer is not supported.'),
(3,[82,112],'The lower bound is recorded as pen1 over a typed0-like loop, with both layers retained.'),
(4,[76,77,111],'The enlarged audit explicitly distinguishes typed d from handwritten +1 and records the adjacent pen comparison.'),
(5,[17,18,19,98,99,100,113,114],'Both handwritten insertion lines are fully recorded. The phi superscript is corrected to(m), the F subscript retains F_k(xi)/F_xi alternatives, and the reference numbers remain page21 before5.6 and14.3.'),
(6,[115],'Dominant, Cohen-Macaulay, irréductible and morphisme are individually compared as readable overtyped final words.'),
(7,[108,109],'The lower folio is read88, together with the upper82, without inferring archival ownership.'),
(8,[109,111,112,113],'The scope flag is linked to the recorded folios, pen numerical corrections and the explicitly read two-line handwritten insertion, documenting actual extent without inventing a length classification rule.')
])
add(25,89,[
(1,[1,85,93],'The cropped upper number remains doubtful83 from surviving lower curves. The lower number is explicitly83 despite the archive site89 and is retained as written.'),
(2,[3,43],'The typed étudiées au nº12 addition is placed after fié, rather than inside the split word ramifié.'),
(3,[4,5,47,49,87],'The two pen curves are traced independently: sur tildeX(C) and the complete typed dimension condition. The latter attaches after the parenthesis; its long lower stroke and final curve are connectors, with no literal underline or extra closing parenthesis.'),
(4,[88],'The listed overtyped wording is explicitly compared as Et, esquissée, codimension, fibres, notamment and est défini; final readable forms are retained without contextual supplementation.'),
(5,[8,57,58,59,60,89],'Ayant is recovered as legible under cancellation; the second dense six-character group after nécessairement remains illegible.'),
(6,[18,83,84,92],'The compact mark after et retains equals-like/même/aussi alternatives. The full handwritten continuation is recorded without expanding that unresolved mark into a certain word.'),
(7,[14,69,70],'The left marginal mark retains star-question/X-question alternatives from its crossed strokes.'),
(8,[87,90,91,92,93],'The scope flag is linked to the actual insertion curves, short additions, revised item a), final two pen lines and lower folio; no new length threshold is inferred.')
])
add(25,90,[
(1,[1,26,78],'The clipped upper number retains84/87 alternatives; the lower pencil90 is directly read.'),
(2,[36,70],'The barred m-like/nr-like compact glyph remains unresolved: its bar is clear but the joined lower strokes do not settle the abbreviation.'),
(3,[42,43,44,71],'The crossed handwritten word before sur retains doubtful dans, with its cancellation and insertion layers recorded.'),
(4,[3,9,11,12,13,28,29,50,53,54,55,56,59],'The separate strikeouts are mapped to doubtful et at the opening, doubtful P Q before the projective notation, readable sur after lisse, doubtful ), ou que after précédent, and doubtful X Q in the later formula. Obscured connectors remain unfilled.'),
(5,[74],'The overtyped final readings monomorphisme and dimensions are explicitly confirmed from the visible letters.'),
(6,[8,47,49,72,73,77],'Et séparable and nécessairement are identified as typed additions with pen placement curves; the final admet aucun and point fixe underlines are explicitly recorded with the intervening deletion.'),
(7,[70,71,72,73,76,77,78],'The scope flag is tied to the recorded short pen additions, typed insertion connectors, underlined conclusion and folio, retaining the documented writing layers.')
])
add(25,91,[
(1,[42],'The foliation decision directly reads85 above and91 below.'),
(2,[1],'The six cancelled letters of actuel are resolved as legible beneath the x impressions.'),
(3,[43],'The Grassmannian argument is recorded as a T-like pen glyph over typed P, with intertwined underlying strokes rather than a reconstructed typing order.'),
(4,[44],'The crossed(P) remains compatible with pen deletion; the audit resolves no separate series of typed x impressions.'),
(5,[19,20],'Both generic-fibre indices retain eta/y/zeta alternatives, explicitly recording the looped glyph and the prior zeta candidate.'),
(6,[45],'The final s in changements is explicitly identified as a pen addition.'),
(7,[46],'The five listed ordinary words are directly checked as readable final forms beneath their overtyping.'),
(8,[42,43,44,45,47],'The scope flag is linked to the folios, local overwrite/deletion, final s and the pen arrows/glyphs in all three fully compared squares.')
])
add(25,92,[
(1,[35,36],'Both handwritten folios are directly read as86 above and92 below.'),
(2,[1,16],'Pour is identified as typed above the line; its curved placement stroke ends between que and la and leaves la live.'),
(3,[2,17,18],'The pen e-shaped correction and grave accent over typed an are resolved as readable è.'),
(4,[37],'The right edge is recorded as ending at cel; no unseen hyphen or continuation is supplied.'),
(5,[3,19],'Commutatif is identified as a typed insertion whose pen connector ends before de without deleting it.'),
(6,[4],'The complete diagram record preserves the left vertical stroke without a secure arrowhead and the three other visible arrow directions.'),
(7,[5,21],'The mark above a retains plain-a/à alternatives in grasmanienne.'),
(8,[29,40],'The additional closing parenthesis after Spec(k) is explicitly identified as pen and attached to the earlier textual opening.'),
(9,[8,9,10,11,12,13,14,15,25,39],'The family-notation decision checks the lowered s k(point) and underlines; each pen point glyph retains xi/zeta ambiguity, and the membership sign is separately recorded as handwritten.'),
(10,[42],'The visible familled e and d e spacing is explicitly retained with the other page-specific joins and spaces.'),
(11,[41],'The final dessus reading is directly checked beneath its overtyping.'),
(12,[34],'The de before(absolu) is specifically recorded as typewriter-cancelled.'),
(13,[36,38,39,40,1,3,7],'The scope flag is linked to the recorded folios, pen diagram label and glyphs, closing parenthesis and connectors for typed insertions.')
])
add(25,93,[
(1,[1,25,26,27],'The handwritten point subscript retains xi/zeta uncertainty, while the target capital retains P/B overtyping alternatives and the arrow is identified as pen.'),
(2,[28,44],'The overtyped final é/e at the right crop leaves the fermée/fermé endings unresolved.'),
(3,[29,30,45],'The interlinear de dimen is explicitly read as a typed phrase with typewriter cancellation.'),
(4,[6,10],'The intraword cancelled characters retain doubtful s in géométriquement and r/s in s’appliqueront; the visible x impressions are treated as cancellation marks.'),
(5,[8,9,49],'Envisaagées/envisagées and changment/chqngment remain explicit overtyping alternatives; toutes and ce raisonnement are separately read as legible final words.'),
(6,[36,39,40,47],'The less-than sign is recorded as handwritten; the later clear pen greater-or-equal overlies an indistinct earlier angle whose less-than candidate remains doubtful.'),
(7,[20,21,22,23,34,35,37,41],'The looped point glyphs are recorded occurrence by occurrence as eta/y alternatives, including the lower occurrence beyond the three listed in the note.'),
(8,[43],'The two folios are read87 above and93 below.'),
(9,[43,46,47,4],'The scope flag is tied to the recorded folios, short handwritten insertion, revised inequality and pen diagram connectors.')
])
add(25,94,[
(1,[1,31,32,79],'Résultait is resolved as readable; the crowded final letter of spécifil/spécifiq remains doubtful.'),
(2,[28,29,30,80],'The unusual typed Z-like initial of Zrréductible is preserved, and the three handwritten point subscripts retain eta/y ambiguity.'),
(3,[6,42,43],'The first word retains éégalement/éggalement/également alternatives, adding the visible repeated accented-e candidate; maàntenant/maintenant remains unresolved.'),
(4,[44,45,83],'The handwritten incidence morphism and typed algebraically-closed-field parenthesis are separately recorded with both attachment points checked.'),
(5,[18,27,64,65,73,74,85],'Both N-n sign positions are checked independently and retain surviving-plus/overwritten-minus alternatives. The dimension arithmetic is explicitly not used to settle either reading.'),
(6,[12,17,51,52,58,59,60,61,62,84],'The raised point glyph is identified as typed z/g with a pen connector. The constructibility correction retains all three layers: cancelled typed constructible, inserted typed fermé with pen deletion, and clear handwritten constructible.'),
(7,[25,70,71],'The retouched G is resolved as clear, retaining its typed and pen layers.'),
(8,[77,78],'The folios are directly read88 above and94 below.'),
(9,[78,83,84,87],'The scope flag is linked to the folios, handwritten morphism insertion, constructible replacement and large final pen parentheses, preserving their documented extent.')
])
add(25,95,[
(1,[5,11,12,13],'Sur k(parenthesized point) is resolved as readable and placed after lisse before the pen full stop; only eta/y in the point glyph remains doubtful.'),
(2,[1,8,30],'The less-than sign is pen, fortiori is readable, and the dimension capital retains P/G overtyping alternatives without a contextual choice.'),
(3,[7,14,15,22,23,31],'The word after redites remains illegible; the cancelled et7.5 is resolved as readable in full.'),
(4,[24,25,26,27,32,33],'The short opening cancellation remains unreadable; une application and de are typed interlinear insertions, and de nature is explicitly recorded as live.'),
(5,[34],'The lower-scan overtyped words are individually read, including the unchanged source spelling respris.'),
(6,[29],'Both folios are directly read89 above and95 below.'),
(7,[29,33,36,5],'The scope flag is linked to the folios, short margin addition, connectors for typed insertions and explicitly inspected blank lower remainder.')
])
add(25,96,[
(1,[1],'The pencil96 at the foot is plainly read, and the record explicitly states that neither scan part contains other writing.'),
(2,[2],'The three isolated specks and their locations are individually inventoried; surrounding blank areas were inspected and no glyph or writing line was read.'),
(3,[1,2],'The no-long-handwriting flag follows the recorded whole-page blankness apart from pencil96 and isolated nonwriting specks.')
])
add(25,97,[
(1,[57,58,59,60,61,62,63,64,65],'The pale-page concern is linked to the explicit regional audit of upper traces, headings, proposition, suspected cancellations, formula rows, corollaries and final lines. The records state that original and enhanced views did not settle the unresolved readings; no next-page text was substituted.'),
(2,[57],'The two upper lines and displaced trace were inspected in original and enhanced channel views; isolated strokes still do not yield words.'),
(3,[1,58,59,60],'The heading underlines are visible but wording remains tentative; the heading-number alternatives include §2)/§21, and Proposition1.1-shaped wording/rank condition remain uncertain.'),
(4,[2,3,4,61],'All three dense faint groups are separately recorded with uncertain cancellation scope and illegible underlying content.'),
(5,[65],'The small cross/star-like trace and Un autre-like final opening remain too faint to resolve after inspection of both final lines.'),
(6,[66],'The pencil97 is explicitly read with the complete lower margin inspected.'),
(7,[57,58,59,60,61,62,63,64,65,66],'The scope flag is linked to the complete regional inventory of faint typed content and the clear pencil folio; it supplies no claim that faint wording became legible.')
])
add(25,98,[
(1,[11,15,52,61,62],'Both long diagonals are recorded with lower-left terminals and no securely established deletion scope over the body. The separate lower tick remains backslash-like/1 doubtful; its graphic presence does not assign a textual function.'),
(2,[1,19,21,22,23,53],'The title retains typed0 under a pen1-like overwrite. The free sign above the final part of Cartier retains plus/t alternatives and is not treated as a replacement of its initial C.'),
(3,[2,28,29],'Fini and the comparison with2 are read as pen writing in the baseline blank; fini is resolved as legible without an insertion caret.'),
(4,[55,56,5,34,35,39,40,41,57,6,43,44],'The rank-condition cancellation is read as n’est nul en aucun point; the short four-x group remains unreadable; pour tout n and et la classe are recovered; the long restriction/formula candidate remains partly obscured under both typed and pen cancellation.'),
(5,[7,45,46,59],'Handwritten le and typed préschéma share the documented curve attaching between en and somme; their order is retained.'),
(6,[9],'The S index has a crowded raised i/n group and a separate lower a/n overprint; both positions and uncertainties are preserved.'),
(7,[14,48],'The Pic target capital retains P/R/E overtyping alternatives without selection from the mathematical map.'),
(8,[49,50,61],'The lower handwritten98 is directly read with the other foliation and full bottom-margin inventory.'),
(9,[50,51,52,59,60,61],'The scope flag is connected to the actual handwritten replacement title, folios, local insertions and diagonal graphics; it does not recast the page-wide strokes as body deletion or impose a new length threshold.')
])
add(25,99,[
(1,[4,20,43],'Both diagonals are recorded by their endpoints; the upper has a lower-left arrowhead and the lower continues to the foot. Their intended deletion scope remains unresolved, so body text stays live.'),
(2,[45],'The first typed x after Pic(S) is separately visible; the following dense cancelled group remains partly obscured.'),
(3,[3,6,55],'The two reference positions retain1/4 and4/3 alternatives respectively; the general reference inventory does not override those local doubts.'),
(4,[50],'The crowded initial overtyping of the live injectif/bijectif word remains unresolved.'),
(5,[52],'The record explicitly distinguishes the lower typed star-like group from the raised pen star and retains the overwrite.'),
(6,[14,53],'The inner underlined capital in formula(xx) retains L/E/M alternatives; the separately noted initial M remains un-underlined.'),
(7,[17,54],'The last word retains isomorphisme/isemorphisme uncertainty, and the earlier opening-parenthesis position retains parenthesis/à overtyping alternatives.'),
(8,[44,48],'The lower number is visibly93 despite archive site99; the single opening square bracket beside Lorsqu’on has no visible closing mate on this page.'),
(9,[43,44,46,48,52],'The scope flag is tied to folios, diagonal graphics, a short nonempty-condition insertion, margin bracket and star overwrite, with no new claim about a long handwritten passage.')
])
add(25,100,[
(1,[46],'The folios are directly read3 above and100 below.'),
(2,[1,2,3,4,5,6,7,47],'The record explicitly withdraws paragraph-wide deletion wrappers because the continuous diagonal alone does not establish authorial cancellation scope. Its graphic remains recorded through the lower edge.'),
(3,[4,14,48],'The opening and closing marks around the rank observation retain bracket/parenthesis alternatives, with possible typed-parenthesis remnants unresolved.'),
(4,[49],'The r exponent is followed by typewriter-cancelled+1 and a separate doubtful pen bracket-like mark.'),
(5,[15,16,22,50],'The inserted L-prime is identified as typed with a pen attachment; the tilde on the following L and the later L-prime are explicitly handwritten.'),
(6,[51],'The crowded letter in factori...el remains a doubtful cancelled e-like character; no expected spelling is used to recover it.'),
(7,[23,52],'The cancelled group after inversible remains unreadable, while the heavy live capital before sur retains M/N alternatives.'),
(8,[53],'The overtyped q carries a raised mark compatible with prime/star; the formula does not decide the reading.'),
(9,[54],'The two-word-length cancelled group before points remains unresolved from its surviving fragments.'),
(10,[55],'The audit records one nearly horizontal underline under libre. This entry establishes its presence without settling a separate typed-versus-pen production claim.'),
(11,[46,47,48,49,50,55],'The scope flag is linked to the actual folios, diagonal, brackets, insertion connector, tildes and underline; the uncertain diagonal function remains explicit.')
])
add(25,101,[
(1,[47],'Both folios are read4 above and101 below.'),
(2,[1,7,8,28,48],'The four principal oblique marks and their terminals are explicitly inventoried; their purpose is not established as author deletion, so no body-wide cancellation is inferred.'),
(3,[2,3,49],'The tilde on L is handwritten, and the overtyped operator retains q/i/4 alternatives. The adjacent Gamma formula has a visibly lower star, preserved in its own recorded position.'),
(4,[4,5,51],'De rang1 is identified as typed with a pen connector. The curve ends above the initial M and does not cross the remaining comme Module letters; the unsupported local deletion is removed.'),
(5,[6],'The colon retains pen-colon/pen-addition-over-typed-full-stop alternatives because the lower dot’s layer is unresolved.'),
(6,[10,11,13,14,15,53],'Les and aux are identified as typed insertions; the five-x group remains unreadable, the ending after eff retains et/etu alternatives, another short cancellation yields une, and the right-edge final s remains clipped and doubtful.'),
(7,[23,54],'Typed resp. connexe attaches after S≠empty set before alors; the returning curve is not encoded as an independent closing-parenthesis glyph.'),
(8,[27,55],'The listed overtyped ordinary words remain readable. The final cancelled run yields doubtful sur followed by underlined Z, S and défini par, with cancellation x impressions removed from the proposed content.'),
(9,[47,48,51,54],'The scope flag is connected to the folios, oblique graphics and connectors for typed insertions, preserving their actual layers and unresolved functions.')
])
add(25,102,[
(1,[9,12,14,27],'All three oblique strokes are recorded separately with their lower terminals; their shapes do not establish whole-page deletion, and the body remains live.'),
(2,[32],'The single vertical pen bar is explicitly followed across the parenthetical revision from près through the later L-clause.'),
(3,[2],'The comparison is pen and the following glyph is resolved as capital D from its stem and serifs, without mathematical normalization to0.'),
(4,[4,30],'The underlying cancelled l’image is recovered, with typed la classe recorded as the insertion above it.'),
(5,[5,31],'The inserted Pic S cross{n} is legible and attaches before l’homomorphisme; pr/par remains doubtful, and heavy ink at l-prime does not justify a new word.'),
(6,[7],'The overprinted opening-parenthesis position retains parenthesis/tensor-like alternatives from its crossed-circle trace.'),
(7,[12,35],'The typed2 of1.2 remains readable under the diagonal hook; its reference is retained.'),
(8,[29],'The crop leaves fibr visible and removes the remainder; no unseen letters are supplied.'),
(9,[26],'The folios are directly read5 above and102 below.'),
(10,[26,27,31,32,34,36],'The scope flag is tied to the folios, diagonals, local handwritten Picard/rank/isomorphism additions and vertical rule, without assigning new deletion or length scope.')
])
add(25,103,[
(1,[29,49],'The continuous down-right diagonal is recorded through the lower edge; its function does not securely establish whole-page deletion and the text remains live.'),
(2,[1,3],'Associé/assooié remains an overtyping doubt, and both upper and lower f stars are identified as broad pen marks in their visible positions.'),
(3,[7,50],'The degree hypothesis is typed, dimension remains readable under overtyping, and its handwritten comparison and connector place it after the degree-n clause.'),
(4,[19,20,52],'Both unit-group stars are recorded as handwritten with extended freehand arms; the underlying function letter remains capital I.'),
(5,[23],'The separator between sections and inversibles is recorded as a short slanting pen stroke rather than an upright bar.'),
(6,[25,56],'The full handwritten replacement is resolved as underlined surjectifs i.e. partout non nuls, ending in a comma; the earlier partout non nuls has its own pen cancellation.'),
(7,[48],'The foliation decision reads6 above and103 below.'),
(8,[48,49,50,54,55,56],'The scope flag is tied to the folios, diagonal, connector for a typed hypothesis, local isomorphism signs, case number and handwritten replacement phrase.')
])
add(25,104,[
(1,[1],'The cancelled partout surjec is resolved as readable, retaining its abbreviated ending.'),
(2,[3,10],'Both overtyped g positions retain g/f alternatives, including the theorem occurrence.'),
(3,[9,43],'The defining-module addition is read as handwritten définis pr/par E,E-prime loc. libres de type fini with a final point; only the abbreviated preposition remains doubtful.'),
(4,[13,44],'The theorem-composition target P is explicitly confirmed as underlined in both image parts.'),
(5,[45],'The overprinted first vowel retains deuxième/dauxième alternatives.'),
(6,[16],'The capital after fibres de retains P/p overtyping alternatives from its lower stem.'),
(7,[20],'The O subscript retains P/E superimposed traces; neither layer is silently selected.'),
(8,[18,47],'The typed et bien sur sentence attaches after corps; the comparison and connector are pen, and source sur remains unaccented.'),
(9,[40],'The two folios are directly read7 above and104 below.'),
(10,[40,43,44,47,49],'The scope flag is linked to the recorded folios, short handwritten qualification and S-hyphen addition, underlining and connector for the typed sentence.')
])
add(25,105,[
(1,[35],'Both handwritten folios read8 above and105 below; the lower blank region was included in the record.'),
(2,[5,6,7,8,37,38],'The full diagonal note and its circled target are read. Le faire is underlined; the possible dual mark sits above the first E, with marked/unmarked alternatives retained; C/c and pr/par remain doubtful, and four separate terminal dashes are preserved.'),
(3,[9,39],'The pen retouch is localized over the typed r of préschéma and retains r/e-like alternatives without treating the whole word as uncertain or certainly deleted.'),
(4,[42],'Et se note GP(E) is typed; its comma and curve are pen, with attachment before Lorsque explicitly checked.'),
(5,[14,15],'The cancelled du is resolved as readable and the final cancelled letter of appelé is identified as é from its visible accent.'),
(6,[16,43],'The initial case in Projectif remains P/p typewriter overprinting rather than a certain pen replacement; Groupe Projectif has one underline and absolu two.'),
(7,[40],'The small spot beneath the a region has no secure letter, accent or cancellation shape; linéaire is retained.'),
(8,[35,38,42,43,44],'The scope flag is linked to the fully read marginal note, local notation addition, underlines and explicitly blank lower page; no new length classification is asserted.')
])
add(25,106,[
(1,[1],'Both parts of the rank comparison are identified as free pen strokes, with the adjacent2 typed.'),
(2,[37],'Déterminer and Div(P/S) are explicitly checked letter by letter as readable through overprinting.'),
(3,[4,39],'Both subscript stars and the display label(*) are pen; the twist letter retains n/m overtyping alternatives.'),
(4,[9],'The sequence is resolved as a typed s followed by two clear handwritten s characters.'),
(5,[41],'The pen phi above the start of de M tensor Sym is explicitly attached to complete d’une section.'),
(6,[13,14,15,44,45],'The entire local deletion from Ainsi through tel is recorded across three lines. Within it partition has typed x cancellation and décomposition is a typed insertion; the opening-parenthesis position remains doubtful and no membership sign is supplied between n and N.'),
(7,[35],'Both handwritten folios are read9 above and106 below.'),
(8,[35,36,38,39,41,44],'The scope flag is linked to the folios, handwritten section number and symbols, inserted phi and locally deleted ending with typed internal revisions.')
])
add(25,107,[
(1,[1,2,3,20,21,22,39],'The handwritten on avait/n’avait insertion remains doubtful; both greater-or-equal signs are pen, while the blotted final comparison retains strict/weak less-than alternatives.'),
(2,[40],'The overtyped G/A region and faint à support the completed Grâce à reading without a separate invented cancellation.'),
(3,[24,25,43],'The vowel retains tèxte/texte alternatives, and both slanting near-vertical marginal strokes are explicitly present.'),
(5,[27,28,30,31,34,37,44],'All six dual accents are recorded as handwritten at their individual formula positions, including the accent over M.'),
(7,[14,15,17,46],'Both Div subscripts retain P/E/R overprinting alternatives. The unusual P/S subscript on Sym remains, its P underline is recorded, and the following parenthesis/I-like crossed group remains explicitly doubtful.'),
(8,[48],'The listed right-edge endings correspondan, loc, représentable and inv are recorded as clipped; no missing endings or hyphens are supplied.'),
(9,[38],'The folios are directly read10 above and107 below.'),
(10,[38,39,43,44],'The scope flag is linked to the folios, short handwritten opening insertion, marginal strokes and six dual accents, with the existing uncertainties retained.')
])
add(25,108,[
(1,[26],'The handwritten folios are directly read11 above and108 below.'),
(2,[29],'The extra typewriter impression on l is recorded, while the surviving strokes support le.'),
(3,[30],'The complete cancelled quantifier is read as pour tout underlined n in underlined Z-to-I, un, with every word and symbol checked.'),
(4,[33],'The crowded s/i region still supports the complete inversible reading; no separate extra letter is securely recovered.'),
(5,[8,9,34],'The component letter retains h/n overtyping alternatives, and the raised pen mark above Z retains star/x/z possibilities at its observed height.'),
(6,[36],'The underlined argument in the degree formula retains L/E alternatives from superimposed strokes; no order of typing is asserted.'),
(7,[26,32,34,35,38],'The scope flag is tied to the folios, handwritten2.7 placement, raised mark, local cancellations and complete lower continuation/margin inventory.')
])
add(25,109,[
(1,[24],'Both folios are directly read12 above and109 below.'),
(2,[1],'The ending retains ant/aht overtyping alternatives and the visible blank after résult is preserved.'),
(3,[2],'The small pen stroke reinforces the top of the typed m in détermination, whose word reading remains clear.'),
(4,[4],'The typed2.8 is encoded as an insertion above the paragraph, with its curved pen connector to Si.'),
(5,[26],'Définit and the visible clipped portions étan and ramené are read directly; no cut-off final letters are supplied.'),
(6,[5],'The underlined capital retains N/M overprint alternatives; its adjacent membership sign is pen.'),
(7,[7],'The full cancelled ou à Künneth is recovered, including the umlaut and final th.'),
(8,[10,12,13],'All three large tensor-product circle/cross signs are individually identified as hand-drawn; the first i index is explicitly typed.'),
(9,[31],'Both V-shaped exponents after E_i are recorded as pen, with their i subscripts checked.'),
(10,[32],'The middle of derniers retains rni/mmi alternatives; the expected word does not settle the overprinting.'),
(11,[15,34],'The o of Pour is visibly lowered and preserved; the underline lies directly beneath both letters of et and remains encoded.'),
(12,[24,31,34,2,4],'The scope flag is linked to the folios, local retouch, number connector, dual accents and final underline, documenting the observed handwriting.')
])
add(25,110,[
(1,[4,10,11,12,13,15,16,42],'The main phi and psi glyphs are identified as handwritten from their continuous curves and slanting stems; the separate cancelled interlinear symbol is typed and remains ambiguous. This supersedes a uniform typed slashed-letter description.'),
(2,[3,42],'The cancelled interlinear group retains underlined-phi/ø alternatives and an unreadable following character under x cancellation.'),
(3,[43],'The underlined variable retains N/G overprinting alternatives from conflicting straight and rounded traces.'),
(4,[18,46],'The final typed1 in2.11 has a pen2-like overwrite, but corrected2/unchanged1 numbering remains uncertain from the ink.'),
(5,[20,48],'The final s-shaped pen stroke retains addition/cancellation alternatives; neither state is silently selected.'),
(6,[47],'Positifs, correspondant, changement, transversalement, biunivoque and la are explicitly checked as readable final words beneath local overprints.'),
(7,[39],'The folios are directly read13 above and110 below.'),
(8,[39,42,46,48],'The scope flag is linked to the folios, handwritten main symbols and local numeral/letter corrections, with their remaining uncertainties preserved.')
])
add(25,107,[
(4,[10,26,51],'The Div exponent/argument retain their recorded n/m and P/E/R overprints; a focused follow-up now explicitly records the adjacent des as readable under crowded d/e overprinting.'),
(6,[12,29,52,53,54,55,56,57],'Devine/devien retains its earlier doubt. Focused enlarged follow-up records tout, Proposition, Sym and canoniquement as readable; it adds localized c/b uncertainty in préschéma and s/d uncertainty in sur from their merged letter shapes.')
])
add(25,111,[
(1,[2],'The opening psi is resolved as a pen glyph matching the other forms; its arrow is pen and Q is explicitly plain.'),
(2,[32],'Only vrai is visible at the right edge; no missing final e is supplied.'),
(3,[9,11,36],'Ce foncteur is recovered as readable; the other cancelled word is corrected to schéma, with typed fibré inserted above it.'),
(4,[20,38],'The h/n doubt is resolved as visible h with a full ascender and bowl, preserving the source spelling provieht.'),
(5,[12,13],'The o of Pour has a separate curved lower impression of uncertain function, and monomorphisme remains doubtful under conflicting middle-letter overprinting.'),
(6,[15,37],'The P in une section de P(Q) is explicitly plain; its argument retains the separately observed Q/A overprint doubt.'),
(7,[30],'The folios are directly read14 above and111 below.'),
(8,[30,33,36,37,40],'The scope flag is tied to the folios, local symbols/typed replacement and the complete lower text and blank-margin inventory.')
])
add(25,112,[
(1,[72,79],'The preliminary block cancellation is supported by several intersecting strokes hatching the passage and ending within it, plus repeated local slashes. The entire text through au plus tard dans V and its references was read beneath them.'),
(2,[1,2,3,71],'The complete revised handwritten title and boxed Nos3,4 are inspected; morphismes and projectifs are resolved as readable, the initial cancelled group remains illegible, and the section digit retains2/3 alternatives.'),
(3,[12,60,61,62],'The initial ligature retains cf/section-sign alternatives; n, its raised circle and2 are clear.'),
(4,[6,29,30,31,32,33,34,73],'The typed x cancellation and raised pen3/z alternatives are separately recorded. The faint marginal r-like trace remains compatible with a letter or incidental stroke.'),
(5,[78],'The gap between f:X and S contains no separately drawn arrow, and no arrow is supplied.'),
(6,[53,54,77],'The extra i in contravariant is specifically recorded as locally typewriter-cancelled within the larger hatched block.'),
(7,[80],'The right crop ends at sous-enten, with no hidden ending supplied.'),
(8,[70],'The folios are directly read15 above and112 below.'),
(9,[70,71,72,75,81,83],'The scope flag is linked to the documented title, local handwritten replacements and qualifications, folios and block cancellation; it imposes no new length threshold.')
])
add(25,113,[
(1,[27,63,64],'Both pen folios are read16 above and113 below.'),
(2,[43,44,67,76],'The focused edge record now covers all four endings: localemen and morph without supplied continuation, ensemblist with a doubtful cancelled e, and the partly clipped but visible upper/lower remnants of the closing parenthesis after S_1.'),
(3,[1,7,11,12,14,17],'Par symétrie, f=0, identiquement nulle, serait, un morphisme and the extra cancelled n are each recovered as readable under their typewriter cancellation.'),
(4,[20,22,59,73],'Diviseurs retains a middle-letter overprint doubt; vi in the later di-vi-seur is explicitly typewriter-cancelled; par retains r/m alternatives rather than a separate deletion.'),
(5,[16,45,68],'Both questioned nested s positions are recorded as typewriter-cancelled; the x inside the O subscript field argument remains overprinted and doubtful.'),
(6,[23,53,54,55,56,71,72],'The whole cancelled paragraph is read; the x row ends after biunivo while pen crosses que, and typed cancellation continues through év while the pen line already crosses est. Both overlapping layers are preserved.'),
(7,[2],'The previously unencoded tick is recorded above X as a small doubtful r-like pen mark.'),
(8,[62,74],'Soit is clear, while its dark quotation-like marks cannot be cleanly separated from the insertion connector; the existing quotation uncertainty remains.'),
(9,[3,30,65],'Plat is a typed insertion whose pen connector passes above loc; loc remains live because no deletion crosses its letters.'),
(10,[64,65,71,74,75],'The scope flag is tied to the folios, local connector, fully read cancelled paragraph, quotation uncertainty and complete lower margin.')
])
add(25,114,[
(1,[2],'The wavy stem and right arrowhead from D to transpose D are explicitly hand-drawn.'),
(2,[36],'All six epsilon-like membership signs are individually inspected as pen glyphs with their neighboring variables.'),
(3,[3],'The overtyped a/r region retains débarasser/débarrasser alternatives without resolving the extra-r question from spelling expectations.'),
(4,[5,40,48],'The cancelled group before égal retains exemple/l’exempl alternatives; the later literal-apostrophe cleanup changes encoding only.'),
(5,[8],'The cancelled assure is resolved as readable beneath the x impressions.'),
(6,[9,42],'The dense pen relation retains equality/slashed-equality alternatives; the preceding singular point fixes is preserved as printed.'),
(7,[44,45,46],'Horizontal strokes, bracket and internal hatching support deletion of the complete Le petit sorite paragraph. The relocation instruction and nested typed cancellation are read, while Un oubli and both marginal strokes remain outside the deletion.'),
(8,[35],'The folios are directly read17 above and114 below.'),
(9,[35,36,44,46,47],'The scope flag is linked to the folios, membership glyphs, bounded paragraph cancellation, live addition and final continuation/margin inventory.')
])
add(25,115,[
(1,[49],'The folios are directly read18 above and115 below.'),
(2,[1,2,50,51],'The circled typed qualification attaches after X-Z, while the separate handwritten surjectivity clause attaches after rel à S. Its possible closing parenthesis remains doubtful; no typed close is inferred from the enclosing bubble.'),
(3,[6],'The cancelled character after dit retains a/q alternatives from its descending right trace.'),
(4,[19,60],'The i and d are readable, c remains doubtful, and the extra e-like character has pen cancellation. The adjoining handwritten underlined H is clear.'),
(5,[15,16,58,59],'Pseudo-morphisme is resolved as readable above an illegible cancelled handwritten word. Its connector also reaches the end of the rationelle parenthesis, so exact attachment remains uncertain and the prior placement is retained provisionally; rel. keeps colon/à alternatives.'),
(6,[57],'The entire nonempty-fibres insertion and its dual/inequality signs are read, with the connector reaching after diviseurs.'),
(7,[14],'The short li candidate remains doubtful under typed cancellation and additional pen hatching.'),
(8,[49,50,51,57,58,59,61],'The scope flag is linked to folios, two distinct qualifications, nonempty-fibres and pseudo-morphism additions and the complete final-margin inventory; actual attachment doubts remain explicit.')
])
add(25,116,[
(1,[65,66],'Both folios read19 above and116 below, with the bottom number retained in its margin encoding.'),
(2,[7,8,32,45,56],'All five questioned dual accents are individually recorded as pen, including the two that NOTES proposed might be typed.'),
(3,[36,37,38,39,40,67],'The underlying ci remains doubtful; pen tte, inserted condition, cancelled se and its separate left-margin replacement are recorded with their attachments.'),
(4,[9,41,42,68,76],'The number retains a pen3 over an uncertain1/2 and a following pen1. A focused follow-up now records the title’s final overprinted letter as n/h from its tall h-like stem; it does not assert a handwritten word correction.'),
(5,[74],'The complete list biunivoque, paramétré, aucun, disant, également, X-D and composante is explicitly checked as readable beneath local overprints.'),
(6,[50,70],'The inserted intègres is explicitly typewritten above the locally cancelled word.'),
(7,[48,53,70],'Both enclosing parentheses around the Lorsque sentence are recorded as pen.'),
(8,[23],'The X-D to S arrow is hand-drawn, including its thick rightward head.'),
(9,[21,57,72],'The typed relative-dimension insertion follows the live=S; neither the equality nor S is visibly cancelled.'),
(10,[29,64,75],'The letter after éta is resolved as h with a full ascender, preserving étaht and the complete final qualification.'),
(11,[66,67,68,70,72,75],'The scope flag is linked to the folios, local rewrite/number correction, pen parentheses, typed-insertion connector and final lower-margin inventory.')
])
add(25,117,[
(1,[45],'The folios are directly read20 above and117 below.'),
(2,[47],'The clipped final s of des and e of stable retain their source doubts because the right edge removes parts of the letters.'),
(3,[49],'The typed2 is covered by an unreadable pen replacement and curved slash; magnification does not yield an intended number.'),
(4,[51],'The inventory explicitly checks both dual accents and every inequality, inclusion, intersection, union and membership sign as pen, retaining their directions/operations.'),
(5,[2,50],'The vowel in du retains u/a overprinting alternatives; the extra e in systeême is recorded as visible under typed x cancellation.'),
(6,[55],'The final e of une is explicitly pen-cancelled, leaving un.'),
(7,[7,58],'The enlarged margin note is resolved as cf§20.11 and its separate long vertical bar is recorded across the final three lines.'),
(8,[45,49,51,52,53,55,58,59],'The scope flag is linked to folios, local numeral/word/reference revisions, pen symbols and the fully inspected final margin; no new length threshold is asserted.')
])
add(25,118,[
(1,[1,70],'The left bracket and separate internal wavy line are recorded through the lemma proof. Their deletion/relocation/other editorial function remains unresolved, and body text stays live.'),
(2,[14,73],'The diagonal enclosed marginal note is resolved as cf§20.11; its final strokes are digits1,1 rather than exclamation marks.'),
(3,[12,72],'The lemma number is resolved as handwritten3.2 from the curved top and rightward lower foot of2.'),
(4,[11,17,74],'The J subscript mark retains handwritten star/x alternatives; the F subscript group is identified as typed cancelled n/x rather than a pen star. The preceding prof mark remains an uncertain hooked diagonal without an assigned mathematical sign.'),
(5,[71],'The clipped terminal p after isomor and its cancellation are explicitly recorded at the right edge.'),
(6,[8],'The first letter of et is a pen retouch over typed e with e/a alternatives; the final t is clear.'),
(7,[28],'The old doubtful Z-like glyph has pen hatching; X-Z is a typed replacement with a pen attachment.'),
(8,[33],'The U/S separator retains slash/x overprinting alternatives.'),
(9,[34,35,36,37,38],'All five dual accents on P are individually identified as handwritten, superseding the NOTES typed-layer suggestion.'),
(10,[77],'The separate far-right point after pour tout is explicitly visible and retained.'),
(11,[69],'The folios are directly read21 above and118 below.'),
(12,[69,70,72,73,74,77],'The scope flag is tied to the folios, bracket/wavy graphics, lemma number, marginal reference and short marks, preserving their actual unresolved functions.')
])
add(25,119,[
(1,[23,106],'The entire two-line top condition is read, including the restriction formula, arrow to dual P and3.1 reference. Its matching looped check-like stroke occurs after the depth bound, fixing the attachment while the sign shape remains doubtful.'),
(2,[1,99],'The top folio retains22/2-slash-2 alternatives because the annotation enclosure passes between the two digit shapes.'),
(3,[3],'The pen-cancelled digit after proposition retains3/2 alternatives.'),
(4,[5,101],'The first pen3 is readable; the next crowded numeral retains3-over-2/repeated3 alternatives. No separating point or normalized number is supplied.'),
(5,[4],'The overtyped letter in réciproque retains r/p alternatives from its shoulder and lower trace.'),
(6,[11,17,18,25,26,28,29,33,102],'The two set symbols are distinguished throughout as oval-stemmed phi/empty-set and forked psi/empty-set pen glyphs, preserving both shape and alphabet uncertainty rather than conflating them as typed circles.'),
(7,[19,105],'The inserted f is typed with a pen placement slash; the older mark after S remains obscured rather than securely identified as a typed star.'),
(8,[105],'U= is clear handwriting, while the overwritten dom/U region remains uncertain.'),
(9,[9,13,16,32,38,103,104,107],'Short cancellations are individually recovered where legible. The long D-associons sentence retains uncertainty in obscured connectors; the cancelled Pour qu’une f sequence is preserved with its visible unusual wording and distinct set glyphs.'),
(10,[34,37],'Both pen-cancelled f_U conditions are fully recovered, including the3.1 references and their respective final et que/et endings.'),
(11,[108],'The tiny right-edge mark after que remains an uncertain dense check-like pen stroke.'),
(12,[109],'The small heavily crossed handwritten character after dans remains illegible.'),
(13,[99,106,108,109,110],'The scope flag is linked to the foliation, two-line marginal condition, short unresolved marks and complete lower continuation, without imposing a new length classification.')
])
add(25,120,[
(1,[1,13,89],'Matching looped signs place the boxed handwritten note after réf. Its final clipped word remains doubtful, and the separately clipped top folio retains23/27 alternatives.'),
(2,[3],'The cancelled text after X_s is recovered as ou encore(comme dans les cas envisa through its visible ending; no hidden continuation is added.'),
(3,[87],'The pen loop/stroke over the n position does not securely resolve the proposed ie into two letters; the original insertion uncertainty remains.'),
(4,[12,14,15],'La cond. envisagée est inv. par is typed and attaches after donc; the separately boxed typed fid plat qu cpc moves by its arrow after changement de base before the full stop.'),
(5,[88],'The two typed S letters have a blank between them, with no connecting arrow in either scan.'),
(6,[32,98],'Both rotated halves of the long margin note are read baseline by baseline. Secure surviving words and the inverse-image formula are retained; clipped beginnings, unresolved words, local opening/final cancellations and final star-like mark stay explicit.'),
(7,[18,21,22,25,26,96],'The questioned dual accents in the projection/definition/restriction formulas are individually identified as pen. Both final X-times-S-P factors have visibly plain P without a dual accent.'),
(8,[23,93],'The cancelled cluster retains D/N/P/Or-like fragments and a separate S-like typed impression below. Raised typed x impressions and crossing pen loops obscure the rest, so no coherent former expression is supplied.'),
(9,[95],'Cartier has a bounded local wavy pen cancellation, separately recorded from the marginal-note enclosure.'),
(10,[97],'The final D is handwritten and followed by a separate full stop.'),
(11,[99],'The lower handwritten120 and surrounding blank margin are explicitly inspected.'),
(12,[32,98,89],'The yes-long-handwriting flag is linked to the fully inspected long vertical note, including both rotated halves and all surviving baselines, and the separately attached boxed top note.')
])
add(25,121,[
(1,[24,25,83],'Typed lequel sera alors unique and handwritten et égal are joined to the bottom à l’adhérence schématique line by matching looped b signs. The full lower wording is read and the connector is not treated as a literal bar.'),
(2,[77],'The margin retains doubtful voir aussi and an obscured first section20 suffix; the second reference20.11 is clear.'),
(3,[9],'The omitted pencil bar is explicitly recorded from the corollary down to the paragraph beginning On utilise.'),
(4,[74],'The folios read24 above and121 below, with surrounding margins inspected.'),
(5,[1,4,5,6,7,8],'Each listed overtyped word has its own decision: éléments and haut remain doubtful, and localized v, r, t/s and ge doubts are preserved in diviseur, rédiger, démonstration and dégager.'),
(6,[14,15,17,22,24,80],'All five insertions are identified as typed and attached individually: soit U=X-Z, de t.f, a), the complete rank sentence after isomorphisme and the uniqueness phrase. Their pen connectors remain separate from textual punctuation.'),
(7,[85],'The full local-factoriality addition, frame around X régulier and closing parenthesis are read; the older parenthetical example is locally cancelled.'),
(8,[28,86],'The target set glyph is the forked pen form with no detached prime; its raised terminal belongs to the glyph, while psi/empty-set identity remains uncertain.'),
(9,[26,84],'The pen que is resolved as readable from its q descender and joined u/e; the complete relative-divisor sentence and both primes are checked.'),
(10,[36,53,56],'The three encoded i subscript stars are individually recorded as pen strokes at their actual positions.'),
(11,[74,77,80,83,85,87],'The scope flag is linked to folios, the marginal reference, typed rank insertion, joined bottom note, local-factoriality handwriting and complete final continuation.')
])
add(25,122,[
(1,[19,86],'Every word of the handwritten continuation and both bars over k are read. The added upper mark/crossed bowl on P leaves decorated/plain P alternatives explicit.'),
(2,[22,23,87,88],'The bounded upper passage has both typed x cancellation and looping pen strokes. Its initial il/X and two X-times-S-P products remain doubtful, and the short group before de les remains illegible.'),
(3,[24],'The crossed handwritten line retains doubtful un Mémoire, an unreadable middle group, doubtful dans un and ultérieur around clear n°; no coherent missing phrase is reconstructed.'),
(4,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,25,91],'The lower block’s long diagonals include an arrow-like terminal and do not establish deletion as their unique function. The audit removes the blanket wrappers, retains the body and all local cancellations, and records the graphics with uncertain function.'),
(5,[26,27,89,92,97,98],'Every listed gap is explicitly preserved: the codimension comparison, both D-to-set memberships, the tensor-to-N relation and final L-to-pr_1(N) relation are not supplied.'),
(6,[33,96],'Both product P letters have small pen V accents; the O subscript P is clear but its faint upper tick retains V/slash alternatives.'),
(7,[90],'The slash-like stroke inside anneau is retained as a visible mark without assigning it a lexical function.'),
(8,[28,29],'Typed can isomorphe à is placed immediately before la restriction. The right-hand curve is its insertion connector, so the earlier separate closing parenthesis is removed.'),
(9,[94],'The right-edge interpretation punctuation is clipped and the next word stops at constructio; no cut-off ending is supplied.'),
(10,[84],'The folios are directly read25 above and122 below.'),
(11,[84,86,87,90,91,96,99],'The scope flag is linked to the folios, handwritten continuation, local cancellation/reference marks, unresolved block diagonals, dual accents and full lower-margin inventory.')
])
add(25,123,[
(1,[4,5,7,9,11,12,16,18,20,23,25,33,35,42,73,80],'The occurrence-specific decisions identify the P dual accents and the V over underlined E as pen, including the complete upper insertion and marginal formula; existing doubtful crossed correction layers remain explicit.'),
(2,[72],'The heading has a handwritten4 over a distinguishable typed7.'),
(3,[3],'The section sign and20.3 are resolved as readable over/to the right of the typed nº2.'),
(4,[1,73],'The last target in the full top insertion is resolved as handwritten P with a V, without a remaining X candidate; its terminal comma/point remains doubtful.'),
(5,[78],'The display tensor-base index retains S/X overprint alternatives.'),
(6,[22,26,27,28,29,30,31,32,80,81],'The margin formula is fully read. Both circled index corrections retain overlapping old/new layers; both pr-like operators have unreadable pen overwrites and clear pen stars. The cancelled formula gains its visible O_S tensor subscript while uncertain initial relation, E decoration and obscured intervening text remain marked.'),
(7,[74],'The apparent tick is identified by alignment as the raised V over the first P in the inserted note, with no extra textual tick supplied.'),
(8,[83],'The final falling stroke after fibre at the right edge is explicitly a pen comma.'),
(9,[79],'The short handwritten article retains la/le alternatives because the small terminal does not securely distinguish a from e.'),
(10,[71,72,73,80,81,83,84],'The scope flag is linked to folios, heading overwrite, complete top note, marginal/circled formula corrections and final comma/expression inventory.')
])
add(25,124,[
(1,[2,3],'The initial se of section remains overprinted and doubtful. Régulière retains the r/e-like first glyph with its separate acute stroke and the following accented e, preserving both accent positions.'),
(2,[4,44],'The habitude correction retains uncertain typed ah/ha order and pen ha/h scope; the overlapping layers do not justify normalized spelling.'),
(3,[5,45,51,53,56],'Soit is recorded as Soi plus a pen-cancelled doubtful a-like impression and separate handwritten t. Hand4 replaces typed5 in the proposition, internal4.1 and corollary4.2, while comme dans5.1 remains uncorrected.'),
(4,[47],'The complete handwritten nonempty-fibres qualification attaches after fini; all words/signs, following dual accents and comma are recorded as pen.'),
(5,[9,48],'The inserted k after conque and its attachment are clear; the separate retouch over typed(s) remains an unreadable pen group with the underlying(s) candidate retained.'),
(6,[10],'The third letter is resolved as typed d with ascender and bowl, restoring the literal spelling sedtion.'),
(7,[13,14,52],'The cancelled handwritten connective retains et/ou alternatives; phi and its forked attachment after évidente are clear, and the O subscript is resolved as typed P with a separate pen V.'),
(8,[54],'The faint short hyphen after présentati remains visible at the cut edge and is retained.'),
(9,[41,44,45,47,48,51,52,53,58],'The scope flag is linked to folios, local word/number corrections, marginal qualification, inserted field/section symbols and the complete continuation into125.')
])
flush()
