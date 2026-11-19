"""Assemble audited source and index uncertainties; no OCR, outside text or TeX engine."""
from pathlib import Path
import csv,re,json
OUT=Path(__file__).resolve().parent
ID='K157-4-07'
SCANS=list(range(98,107))+list(range(108,115))

def macros(s,name):
 for m in re.finditer(r'\\'+name+r'\{',s):
  i=m.end();start=i;depth=1
  while i<len(s) and depth:
   if s[i]=='\\':
    z=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);i+=len(z.group()) if z else 1;continue
   if s[i]=='{':depth+=1
   elif s[i]=='}':depth-=1
   i+=1
  if depth:raise ValueError((name,m.start(),'unclosed'))
  yield m.start(),i,s[start:i-1]

def branches(s):
 result=[];start=0;depth=0;i=0
 while i<len(s):
  if s[i]=='\\':
   m=re.match(r'\\(?:[A-Za-z]+|.)',s[i:]);i+=len(m.group()) if m else 1;continue
  if s[i]=='{':depth+=1
  elif s[i]=='}':depth-=1
  elif s[i]=='|' and depth==0:result.append(s[start:i]);start=i+1
  i+=1
 result.append(s[start:]);return result

def cell(s):return s.replace('|','&#124;').replace('\n',' ').replace('`','&#96;')
def grounds(n,a):
 if n==111 and a=='machine|mochine':return 'The second letter has a darkened round bowl; a/o cannot be separated securely. The phrase à écrire favours machine, but it does not remove the ink uncertainty.'
 if n==113 and a=='Juin|juin':return 'Tall undotted initial stem and low return favour capital J; the rapid hand also admits j. The leader attaches after Mai, before the parenthesis. No year is supplied.'
 if n==106:return 'A small closed loop after the h-like ascender favours ho-. The shorter h- form is retained as an alternative; the title does not establish a convention by itself.'
 if n==112 and a=='X_{20}|X_{22}':return 'The final numeral is closed and looped, favouring 0; nearby open 2 forms differ. The nine-object grid pattern favours 22 contextually, but does not override this locus.'
 if n==112 and r'\mathrm{id}' in a:return 'The first short stem has no separately secure dot; i, 1 and l remain candidates. Repeated Z(delta) objects favour id contextually but do not supply the missing dot.'
 if n==108 and a==r'\Lambda|X':return 'The local first limb rises like Lambda; X remains possible under retracing. Nearby pair arguments favour X, but each occurrence was read independently.'
 if n==108 and a=='D|B':return 'A broad bowl without a secure middle waist favours D; surrounding row patterns favour B but do not settle this capital.'
 if n==110 and a in ('X_{00}|X_{10}','q_0|q_1','r_2|r_0','X_{22}|X_{21}'):return 'Local index shape determines the first candidate. Parallel grid/fibre formulas suggest the alternative, but that pattern has not been used to rewrite the ink.'
 if 'varinjlim' in a or 'underline{\\lim}' in a:return 'The lower limit stroke has no decisive or only a weak arrowhead. Inductive-system prose favours a right-arrow limit; the observed local stroke determines candidate order.'
 if 'mathscr' in a or 'mathcal' in a or 'mathbb' in a:return 'Looped/retraced strokes admit the listed alphabet candidates. The form was compared with nearby occurrences; its role does not determine ordinary, script, Greek or double-stroked lettering.'
 if n in (98,99,100,102) and ('a petite' in a or 'moitié' in a or 'supprime' in a or 'élém' in a):return 'The interlinear or angled writing was enlarged and its leader followed. Reduced middle/end strokes remain uncertain. No argument has supplied an omitted word or chosen an attachment.'
 if r'\deleted' in a:return 'Superposed or hatched ink leaves the predecessor and/or cancellation state unresolved. Alternatives refer to one physical locus, not multiple successive corrections.'
 if any(x in a for x in ('arrow','relbar',r'{-}',r'\circ',r'\bullet',r'\vdots')):return 'Endpoint, loop, point or shaft shape remains unresolved at this locus. A conventional diagram would favour a familiar arrow or vertex, but the drawing itself controls the candidates.'
 if n==110 and a in ('ont|sont','image|images','dans|ds','iso.','induisent','précise','sont des fibrations'):return 'Very rapid lower prose reduces several letters/endings to a continuous stroke. Grammar or the fibre argument does not make an unseen letter certain.'
 if '|' in a:return 'The local reduced, crossed or overwritten strokes admit these retained alternatives. No further secure contextual preference; see the scan-specific audit for the exact enlargement and state.'
 return 'Tentative reading of reduced or cancelled strokes. No secure additional candidate; plausibility alone does not establish the missing detail.'

notation=r'''# K157-4-07 — Final reading apparatus

## Notation table

This table records the audited readings. All supplied images were read personally in one stream. The completed K157-4-06 table was consulted before scan 98 and remains in `preceding_notation_K157-4-06.md`; the earlier cote-157 comparison work is documented in the package logs. Earlier transcriptions supplied notation comparisons, never words. The first-reading apparatus is retained separately as historical evidence; where it differs, the audited page files, this table and the audit are authoritative for this delivery.

A recurring unresolved glyph is marked at its first matching occurrence on a page; subsequent matching forms use the first candidate. Visibly different local forms remain distinguished. Limits with blunt bars are not silently made into directed limits; a crossed exponent is not made live. The cross-page comparison preserves the distinctions below rather than imposing agreement on different ink.

| Scan / approximate manuscript locus | LaTeX reading / candidates | Ink and reconciliation |
|---|---|---|
| 98 definition and both squares; 99–105 constructions | Ordinary `C,E,I,J,M,X,Y,Z`; category `\underline M` versus plain `M` | Lower bars and underlines checked separately. Continues K157-4-06 where the shapes agree; E's lower bar distinguishes it from F. |
| 98 first display / arrow target | `x` / `\chi`; `\alpha` / `u`; raised `{-}\,\smile` / `r\,u` | Two crossed curved strokes, reduced loop, and detached dash/cup. The last two marks were restored above the target triple in the audit. |
| 98 small square | `\lambda x_{i',i}` / `\lambda^{i'}_{,i}` / `\lambda_{i',i}` | Higher i-prime, lower comma-i and curved intervening stroke retain their possible placements. |
| 98 lower square; 99 first limit | `\mathscr F` / `\mathscr G` / `\xi` | Retraced double loop; the same candidate order is retained on both pages. Plain F in scan 99 prose is a visibly different form and remains plain. |
| 98 lower square right side | `x:X\longmapsto X_i` / i at the argument | Capital-like crossing retained first, even though the index interpretation favours i. |
| 99 first limit / second index | blunt `\underline{\lim}` / `\varinjlim`; `\partial` / Z / alpha / J; membership or cancelled I/J | Lower-stroke head and overwritten index are separate doubts. Extra index loop/state was restored in the audit. |
| 99 main prose and crossed lower block | `\underline M^\pi/E\relbar E` / arrow; literal `de =`; `C^\alpha` | Baseline bar without a secure head, written equals shorthand and raised alpha remain literal. No normalization from the cancelled argument. |
| 100 set and order definition | `\widetilde C_i`, `C'_i`, `\operatorname{Fl}`, `i\leq j`, `C'_j` | Waves, primes and cardinal bound `\leq\pi` read independently. i is short/dotted, j descends; no interchange from a neighbouring formula. |
| 100 lemma and interline | `M^{\deleted{\pi/\ast}}`; target `p:\widetilde C\to C` | Hatched old exponent is cancelled, not live. The target is visibly C; I is only a possible mathematical reading question, not a transcription. |
| 100 inserted family | `C'_{i,\alpha}` versus `C'_{iA}`, `C'_{i\alpha}` | The comma is present only where written. An extra prime on one tilde-C occurrence remains a local alternative. |
| 101 opening display | old alpha under `Z_{C'_i}`; `\neq` / `)=` / `=` | Audit puts the crossed-equality-like form first from its strokes. Parentheses are not repaired to reconstruct a formula. |
| 101 lower display / prose | `\operatorname{Ob}C_i`; deleted old star/pi before live pi; `\in` / `\in_\varphi`; `\widetilde C_M` | Ob and old exponent are present; no inferred i is added to C-tilde-M. The small low loop at membership remains doubtful. |
| 102 limits and inserted bound | arrowed and blunt limits distinguished; `X_{\alpha_B}`; `\alpha_B` above borne sup | First blunt form marked; later matching bars use the first candidate. B is an ordinary capital. |
| 102 revised conclusion / slanted note | inserted “la deuxième moitié de” / “la première moitié de”; literal `I` grand devant `I`; `a_\pi` / `a^\pi` / a | The omitted deuxième/première word was restored in the audit. Both capital I forms are retained. Rotated marginal reading remains qualified. |
| 103 nested indices | `I'_{\widetilde i}` / `J'_{\widetilde i}`; `X_{\widetilde i}`; `\widetilde I_M`, `\widetilde I_0`, `i_0` | Serif I versus hooked J, raised waves and low M/zero individually checked. Heavy index is not assigned blackboard type. |
| 103 crossed majorant sentence | `I'\deleted{\subset/\in}I` | Additional serif I and overwritten relation restored inside the cancelled sentence. Only plus is struck in the later “grand élément”. |
| 104 first limit / implication | blunt limit / arrowed limit; `a\overset{?}{\Longrightarrow}b`; `a_\pi\Longrightarrow b_{\pi'}` | Source question mark and changed cardinal parameter retained. Doubt marks are not confused with his question. |
| 104 hypotheses / cancelled ordinal argument | `E_\pi`, `\mathrm{Filt}^\pi`; pi-primes; `\pi'\leq/={\rm card}\,\alpha'` | Subscript versus exponent and every prime checked. Whole ordinal attempt remains cancelled; the angled inequality is first in its local doubt. |
| 105 representations and bounds | first `=` versus second `\simeq`; `i_{I'}` nested in `X_{i_{I'}}`; `I` / Delta | No extra prime is supplied to i. I's retraced triangular form is a local doubt, not a new convention. |
| 105 final arrows / corrections | lambda / simeq / sim label; mu / u; `str.` / `stri.`; `quelqs` / quelques / quelque | The shortened word is retained first, not expanded. Its insertion and the crossed cofinale/cofinalement stand after “une partie J' de J”. |
| 106 title | `\overline{\underline{\mathrm{XIV}}}`; h-cartésiens; ho-cocartésiens / h-cocartésiens | Separate overline and underline. Acute accents checked separately; small closed loop favours ho-. No date or own-page number. |
| 108 top chains | Sigma, Omega, superscripts 1/2; i,j,d and p,q,partial labels | j has a descender; i does not. Greek capitals are read from their shape, not substituted for script letters. Parenthesized functor labels remain parenthesized. |
| 108 large array | pi indices 2/1 and A/B doubt; older pi_-1/pi_1 forms under later zeros; circled final node | Each row checked independently, including rows whose second/third indices differ from the first. Two-headed arrows remain two-headed. |
| 108 upper-right continuation | C,Lambda/X and D/B,X; clipped last parenthesis | Audit puts Lambda and D first from local strokes; the familiar X/B pattern remains only an alternative. A headless transverse curved stroke and one upward head were restored. |
| 108 NB formula | S / script S / blackboard S; Omega exponent k/h/m; plus/wedge; final summand m/k | Retracing leaves the S alphabet unresolved. i,j and all exponent/subscript positions remain independent; no degree formula is imposed. |
| 108 lower sketches and table | overwritten Y; detached B-column stroke; upward/0/circle/downward mark | Ruled boundaries, detached continuation and hollow pointed mark are represented without assuming exactness. |
| 109 typed A 3 | occurence, aigüë; spaced phrases and ordinary capitals | One r in occurence; two dots on both u and e in aigüë, rechecked enlarged. No bold or mathematical alphabet is inferred from heavy typing. |
| 110 upper drawings | delta/r, initial Z/lambda, Z'_0, barred Z'_1/Sigma'_1, e/epsilon, 2/question | Whole abandoned construction remains cancelled. Primes and overlapping roof vertices are retained. |
| 110 right small diagram | 11/tt; dot over X_00; separate point over two-way/rightward shaft | The restored point and weak left head are explicit doubts. They are not silently regularized to a one-way square. |
| 110 main grid | `\Omega(X_{20})`; row-three X_00/X_10; q_0/q_1; boxed X_22; three braces | Literal 20 remains. Wavy e-arrow and headless upper wave are drawn as waves; delta diagonal is dashed. |
| 110 lower prose / final span | `X_{1,2}` with comma; `r_2` / `r_0`; X_22/X_21; alpha_1 and alpha_0 | Local doubtful indices remain independent of the final span's clear r_0 and X_22. Cancelled first list and overwritten old letters remain cancelled. |
| 111 typed 422 | rattrapper, résouds, s'élimer, remâchage; machine/mochine | Literal double p and ds ending retained. Darkened a/o is explicit. Spaced vivable and le remain spaced; reverse arrows are not foreground deletions. |
| 112 top diagrams | varnothing/phi; literal line/right-arrow before T; two source question marks | Maps-to bar and both questions are visible. Hom(S,T), delta-to-p_1 and the separate old equality remain struck. |
| 112 right diagrams | product underbrace; separate X_20; id/1d/ld; [q_1]; barred X_20/X_20 | No equality invented under the brace; short verticals without heads remain headless. Local first stem of id is doubtful. |
| 112 lower grid | top-right X_20/X_22; p_1/1; colon/vdots; curly left arrow/epsilon | Closed final numeral first, despite contextual 22. Four dotted diagonals, two dashed paths, terminal closed loop and extra return/parallel strokes are included. |
| 113 typed A 2 / addition | `\inserted{\handwritten{et Juin/juin}}`; compréhension; plait | Leader attaches after Mai before the parenthesis. Final n was enlarged; plait has no circumflex. Spaced text and unusual comma spacing retained. No year inferred. |
| 114 unlabelled sketches | open circle/0; first dark point bullet/circle; explicit TikZ paths | No object names, alphabet or indices supplied. Clipped/incomplete edges, looped/filled vertices, retraced shafts, the short upward arrow and separate double-headed downward stroke are preserved geometrically. |

## Doubts

Each explicit `\unsure` occurrence in the audited page files is indexed below, including crossed text and uncertainty about correction state. The source-file line plus neighbouring text identifies the approximate manuscript locus; the scan-specific audit supplies the crop and position discussion. Alternatives split only at the outer macro level, so nested state alternatives remain intact. Confidence refers to decipherment, not mathematical truth. Unresolved entries are conservatively labelled low. The notation table and audit distinguish uncertainty repeated from the same glyph from visibly different local writing.

| Scan | Source line and nearby text | First reading | Other retained candidates | Confidence | Context preference / grounds |
|---|---|---|---|---|---|
'''

tail=r'''
## Slips kept as written / reading questions

The following forms remain unchanged. Mathematical alternatives below are reading or notation questions, not established errors. No claim depending on a doubt mark or a cancelled passage is assigned more than low confidence. Literal typed spellings were re-examined in the second reading before being listed.

| Scan / locus | As written | Possible intended form / question | Grounds and limit |
|---|---|---|---|
| 100 displayed projection | `p:\widetilde C\to C` | Perhaps target I | The preceding sentence indexes the fibres by i in I. The written C is retained; no proof-based correction. |
| 102 last paragraph | “I grand devant I” | Perhaps second I should be pi | Both glyphs look like serif I. The following page returns to I grand devant pi; this is only an internal comparison. |
| 101 first formula | neq / closing-parenthesis-plus-equals / equals | Equality may be intended | Crossed/overwritten locus. Low-confidence reading question only. |
| 104 hypothesis | “tt élément ... sont” | Agreement question | Abbreviated handwriting and the following plural phrase make an authorial-error claim unsafe. No ending corrected. |
| 108 NB and array | k/h/m, m/k; row and tail indices/letters | Familiar degree/row patterns suggest alternatives | Readings themselves are doubtful, so no formula correction is asserted. |
| 110 main grid and lower prose | X_00/X_10, q_0/q_1, r_2/r_0, X_22/X_21 | Parallel formulas suggest second candidates | Low-confidence questions, kept separate from the clear final span. |
| 112 lower grid top right | X_20/X_22 | X_22 fits the surrounding grid pattern | Closed numeral favours 0 locally; the pattern does not authorize repair. |
| 109 first/last prose | occurence; aigüë | occurrence; aiguë are conventional spellings | Literal letters and both diaereses were checked on enlarged crops. No normalization in the transcription. |
| 111 middle prose | rattrapper; résouds | rattraper; résous are conventional spellings | Rechecked double p and d+s ending. These are typed forms, not conjectural handwritten endings. |
| 111 middle prose | s'élimer; remâchage | No correction proposed | Unusual vocabulary is retained; it is not automatically a slip. |
| 113 last paragraph | plait | Traditional spelling plaît; no error asserted | Absence of circumflex checked against the visible circumflex in paraît-il above. |

## Abbreviations met

Expansions here are suggestions for this list only; none is inserted into the transcription.

| Written form | Suggested expansion | Locus |
|---|---|---|
| i.e. / i.e | id est / c'est-à-dire | 98; 104–105 |
| syst. / syst.. | système | 99, 102–103 |
| ens / ens. / l'ens | ensemble / l'ensemble | 99–104 |
| tt | tout / toute | 99–105; number and gender depend on the written phrase |
| élém | élément | 100 interline, reading doubtful |
| pt | point | 100 alternative reading only |
| cf | confer / voir | 99 crossed paragraph |
| lui-m. | lui-même | 99 crossed paragraph |
| supp. | supposé / supposons | 99 angled warning, uncertain |
| NB | nota bene | 99, 104, 108 |
| ssi | si et seulement si | 100 order relation |
| sup | supérieure / supremum | 102 |
| filtr. | filtration | 103 |
| hyp. / l'hyp. | hypothèse | 104 |
| parf. | parfaitement | 104 crossed modifier |
| p. | page | 104 reference to 90 |
| qed | quod erat demonstrandum | 104 opening |
| grand dev. | grand devant | 104 crossed ordinal argument |
| str. / stri. | strictement | 105 insertion |
| quelqs | quelques | 105 insertion, ending doubtful |
| homs | homomorphismes | 105 unfinished final line |
| Hom | homomorphismes | 112 cancelled label |
| ds | dans | 110 alternative abbreviated reading |
| iso. | isomorphismes | 110 final prose, reduced ending |
| id | identité | 112 arrow-label candidate, not securely distinguished from 1d/ld |

## Legibility and limits

Scans 98–105 are rapid working notes with extensive cancellation and interlinear or slanted revision. The weakest textual loci are the footer of 98, both angled notes and the abandoned argument of 99, the inserted parenthesis on 100, the lower insertions on 102 and 105, and the final cancelled ordinal chain on 104. The diagrams on 108, 110 and 112 are generally well contrasted, but overwritten indices, alphabet choices, small arrowheads and incomplete edges remain less secure than their broad structure. Scan 114 has no object labels: its TikZ transcription preserves observed geometry and uncertainty without claiming a categorical interpretation.

The reused typescripts (109, 111, 113) are clearer; scan 111 has dark show-through obscuring part of machine/mochine. Their literal spellings, spaced emphasis, punctuation and scan order are retained. Scan 113's single handwritten insertion is the only foreground handwritten addition to these typed pages. The cover title on 106 is clear apart from its second prefix. All images were inspected personally; no OCR, outside text, web source or TeX compilation was used. The audit records actual start/end times, formula registers and every revision. Static validation establishes source balance and recognized commands, not a rendered layout or a proof of the mathematics.
'''.replace('pla\\u00eet','plaît')

def main():
 assert 'transcription frozen' not in (OUT/'progress.log').read_text(), 'Frozen source must not be rewritten'
 old=OUT/f'{ID}_doubts.md';hist=OUT/f'{ID}_first_reading_apparatus.md'
 if not hist.exists():hist.write_text('# HISTORICAL — superseded first-reading observations\n\n'+old.read_text())
 pages=[OUT/f'pages/{ID}_157-4_scan{n:03}.tex' for n in SCANS]
 body=[]
 for p,n in zip(pages,SCANS):
  s=p.read_text()
  for a,b,arg in macros(s,'unsure'):
   line=s.count('\n',0,a)+1
   context=s[max(s.rfind('\n',0,a)+1,a-30):min(len(s),b+30)]
   candidates=branches(arg)
   body.append(f'| {n} | l.{line}: `{cell(context)}` | `{cell(candidates[0])}` | '+('; '.join('`'+cell(x)+'`' for x in candidates[1:]) or 'none secure')+f' | low | {grounds(n,arg)} |')
 old.write_text(notation+'\n'.join(body)+'\n'+tail)
 (OUT/f'{ID}_transcription.tex').write_text('\\cotefile{157-4}\n'+'\n'.join(p.read_text().rstrip()+'\n' for p in pages))
 (OUT/f'{ID}_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{'+ID+'_transcription}\n\\end{document}\n')
 p=OUT/f'{ID}_inventory.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
 def key(r):
  m=re.search(r'-(\d+)([a-z]*)$',r['element']);v=int(m.group(1))+(ord(m.group(2))-96)/10 if m.group(2) else int(m.group(1))
  if r['element']=='110-06b':v=7.2
  return int(r['scan']),v
 rows.sort(key=key)
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 print(json.dumps({'pages':len(pages),'unsure_rows':len(body),'inventory_rows':len(rows)}))
if __name__=='__main__':main()
