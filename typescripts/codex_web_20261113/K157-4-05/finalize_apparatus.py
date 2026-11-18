"""Assemble the reviewed page files and index their explicit doubt marks; no OCR or compilation."""
from pathlib import Path
import csv, re, json

OUT = Path(__file__).resolve().parent
ID = 'K157-4-05'

def macro_occurrences(s, name):
    for m in re.finditer(r'\\' + name + r'\{', s):
        start = m.end(); depth = 1; i = start
        while i < len(s) and depth:
            if s[i] == '\\':
                z = re.match(r'\\(?:[A-Za-z]+|.)', s[i:])
                i += len(z.group()) if z else 1
                continue
            if s[i] == '{': depth += 1
            elif s[i] == '}': depth -= 1
            i += 1
        if depth: raise ValueError((name, m.start(), 'unclosed'))
        yield m.start(), i, s[start:i-1]

def cell(s):
    return s.replace('|', '&#124;').replace('\n', ' ').replace('`', '&#96;')

def explanation(scan, arg):
    if arg.startswith('-|'):
        return 'The shaft is visible; a separate arrowhead is not secure. The functor/map context favours an arrow, but the dash remains first.'
    if arg in ("G'|C'", "C'|G'", 'G|C'):
        return 'The inward return distinguishing G from C is weak at this occurrence. Nearby G notation favours G; the first candidate follows the local contour.'
    if arg in (r'\Psi|\Upsilon',):
        return 'Curved arms and a central descending stroke admit both Greek capitals. The drawn fork, not its expected name, determines its arrows; context does not settle the letter.'
    if arg in (r'\circ|o', r'\circ|o|\'') or arg.startswith(r'\circ|'):
        return 'A small raised ring or bent stroke is visible. Opposite/topological-category usage favours a circle, but does not determine its exact shape.'
    if arg in (r'*|\circ', r'*|\alpha', r'W|*', r'f|\circ'):
        return 'The raised/lowered or crossed mark has competing contours. The surrounding functor notation suggests a star (or W in the crossed superscript); cancellation and position are preserved independently.'
    if arg == r's\backslash' or arg == r'I|s\backslash':
        return 'Reading beneath cancellation: the visible slash/crossed upright supports the listed candidate(s), but not a confident reconstruction. No mathematical inference is made from deleted ink.'
    if 'accordé' in arg:
        return 'Extremely compressed and retraced opening wording. The existence-of-limits clause supplies a topic, but does not distinguish these candidates. Earlier Diag-complète hypotheses were discarded in the audit.'
    if arg == '(f)|(f\')':
        return 'The source arrow is f-prime, so context favours (f-prime); no separate prime is secure in this argument. The visible unprimed candidate stays first.'
    if 'Holim' in arg:
        return 'Initial tall stem and upper return can be H or R. The leftward limit arrow is clear; context does not warrant substituting a conventional operator name.'
    if 'standard' in arg:
        return 'The final letter may be d or t. Ordinary French favours standard; the spelling question is not resolved from grammar.'
    if 'différents' in arg:
        return 'Enlarged crop has two tall crossed/looped strokes, favouring différents; compressed interior strokes leave distincts possible. Both fit the surrounding clause.'
    if 'exercice' in arg:
        return 'Small inserted writing above the sufficiency proof. The initial group may include dernier; the insertion stroke fixes its location but does not resolve its wording.'
    if arg == r'1|0|\rho':
        return 'The first A-subscript has a short looping contour. The X_1/B_1 column favours 1, but 0 and rho are graphically possible.'
    if 'fibrants|fibrantes' in arg:
        return 'The reduced ending does not decide whether an e is present. Agreement with the mathematical noun is not used to normalize it.'
    if arg == "i'|i''":
        return 'One raised prime is clear and the second is not. The earlier chosen i-double-prime favours that interpretation; the uncertain local mark is retained.'
    if arg == "70|78":
        return 'Overwritten manuscript page number. The surrounding sequence 69,71 favours 70; the final loops also admit 78.'
    if 'Quel allonge' in arg:
        return 'Split marginal comment, right edge then left continuation; only ment has a separate underline. Very low confidence in the compressed first portion; no secure alternative.'
    if 'trouvé|essayé' in arg:
        return 'Contracted verb before de faire un contre-exemple. Either changes what the author says he attempted; context is not used to decide it.'
    if 'donné|' in arg:
        return 'Joined final strokes do not determine gender/number. Agreement is left unresolved, not diagnosed as an authorial slip.'
    if 'axiomes' in arg:
        return 'An extra small rounded/descending group appears after the literal equals sign. A ça-like candidate is included; syntax does not settle the ink.'
    if 'connait' in arg or "s'il" in arg:
        return 'A small high mark has uncertain association; a separate circumflex over connait is not decisive. The accented spelling is contextually expected but not imposed.'
    if 'mathbb' in arg:
        return 'A parallel/retraced stem can be intentional doubling or a retrace. The local alphabet candidates remain explicit; earlier notation tables do not decide this occurrence.'
    if 'des $+$' in arg:
        return 'Compressed connecting words between the explicit plus/minus signs. Duality suggests an interchange, but the two phrase readings remain unresolved.'
    if '|' in arg:
        return 'Compressed or crossed strokes admit the listed candidates. No additional preference can be justified from surrounding text without overriding the ink.'
    return 'Tentative reading of reduced or cancelled strokes; no secure additional candidate. Context may make the word plausible but does not establish its letters.'

notation = r'''# K157-4-05 — Final reading apparatus

## Notation table

This table records readings of the images, not mathematical conventions. Scan numbers refer to the archive PDF; locations are approximate manuscript regions. The first candidate in a local doubt mark follows the ink. Distinct shapes are not forced into one alphabet merely because their roles coincide.

Before scan 66, the notation tables of K157-4-01 through K157-4-04 and the concluding folders of the other parts, K157-1-17, K157-2-28 and K157-3-23, were consulted. The complete extracted tables and their index are retained as documentation; extraction is not a claim that all 72 earlier tables or their source scans were read. Earlier material is not a source of words for these pages.

| Scan and location | LaTeX reading and candidates | Visible evidence; reconciliation |
|---|---|---|
| 66 heading; 70 upper/margin; 77 lower; 81 final display | `C,\mathrm{TC},F,\mathrm{TF},W,M` | Open C; T cap; F with two bars; ordinary single-outline W/M. Consistent with K157-4-04 where the ink agrees. Final scan 81 is literally TF=F∩C. |
| 66 heading and first paragraph | `\mathrm{Diag},\mathrm{Cat}` | Individual capital followed by compact lowercase letters; no script or Greek capital substituted. |
| 66 definition; 67 first paragraph; 79 lower | `quillénisation`, `admissible`, `localiseur` | The first contracted quillénisation is qualified; later clearer forms were read separately. Terminology agrees with K157-4-04, without using that agreement to restore unread strokes. |
| 66 upper display; 67 localization; 74 diagram | `I,I'; M(I)_f,M(I)_c` | I has cap and foot; prime is raised; f/c are below the closing parenthesis. |
| 69 union; 74 first paragraph | `I` / `\mathbb I` | Local parallel uprights may be doubling or retracing, flagged at the occurrence. Other I’s with one main stem remain plain. Earlier doubled-I candidates (K157-1-17) do not resolve them. |
| 67 diagram; 68 corollary; 75–79 | `\mathrm{HO}_W` | Two full-size capitals H and O, W below. Agrees with K157-4-04; differs from mixed-case Ho recorded in K157-4-03. The new ink controls. |
| 66–81 functor expressions | `u_*`, `u^*`, `u_*^f`, `u_*^W`, `u_W^*` | Placement read separately: lower star, upper star, upper f/W, and lower W. Scan 74 prose has u_* without the diagram’s upper f. |
| 67 diagram; 79 first line | `u_{\unsure{*|\circ}}^W` | Tiny crossed/round lower mark remains ambiguous. Later clear stars on the same page are retained as stars. |
| 66 upper parentheses; 68/74/79 slice expressions | `I'_{/i}`, `I'_{/s}`; cancelled `s\backslash` / `I` prefixes | Slash lies low; i is dotted without descent, s hooked. Cancelled prefixes remain deleted and are never used as live notation. |
| 67 b); 69 partition; 72–74 | `I^\circ` / `I^o`; `M_1^\circ` / `M_1^o` / prime | Small raised rings/bent strokes. Rechecked independently, consistent with earlier opposite-circle ambiguities in K157-1-17 and K157-2-28. In scan 73 the second closed piece is I_2 without a supplied circle. |
| 66–68; 80–81 | `\varprojlim`, `\varinjlim` | Left arrow beneath lim for inverse limits; right arrow for final filtered colimits on scans 80–81. |
| 68 first display | `\operatorname{Holim}` / `Rolim` | Initial upright/return ambiguous; long arrow below points left. The definition label is def without a supplied accent. |
| 68 corollary | `\mathrm{Der}\,1,2,4,5` | Ordinary D and lowercase er; digits separately read; no doubled D. |
| 69,70,73 fork name | `\Psi` / `\Upsilon` | Curved arms and descending centre. First occurrence on each page marked; the fork arrows visibly point from 0 to 1 and 2. |
| 70–72 diagrams | `X_\bullet,Y_\bullet; A_i,B_i,X_i,Y_i` | Bullet is a filled low dot. Actual diagram indices are digits 0,1,2,3; first A index on 70 admits 1/0/rho. |
| 70–71 arrows | `\alpha_1,\alpha_2; h_1,h_0,h_2; p_1^X,p_2^X,p_1^Y,p_2^Y` | Digits below, X/Y above; all diagram arrow directions checked individually. Prose p index 1/2 on 71 is unresolved. |
| 71 upper diagram | `A_1` to `X_1` with `dash` | Blunt terminal stroke; no arrowhead supplied. Tiny label below TC is a cancelled i candidate. |
| 72 lower condition; 73 proof | `(\alpha)` | Lowercase looped alpha, not digit 0 or a script capital. Vertical marginal emphasis stroke on 72 is represented separately. |
| 75–79 Hom expressions | `F,F',G'` / `C'` | F has bars; G’s inward return is often weak. Scan 75 first doubtful argument has C′ first from its open contour; first doubtful arguments on 76–79 have G′ first. Clearer return-stroke occurrences remain G′. This is local shape variation, not a convention change. |
| 75–78 formula labels | `(\alpha)`, `(\alpha\alpha)`, `(\alpha\ \text{bis})` | Alpha labels distinct from multiplication stars. Scan 78 reference still admits alpha-alpha/alpha. |
| 75 top diagram | `u_W^{*}` / `u_W^{\deleted{c}*}` | Heavy upper mark may be a thick star or a cancelled c plus star. Cancellation status itself is uncertain. |
| 75–76 relations | `R,R'`, `R\leq\alpha(R')` | Upright capital R, separate prime; inequality points left with lower bar. No script R substituted. |
| 76 arrow annotation | `u^*u_*G\to G` | No primes visible in this annotation, despite primed G in nearby Hom objects; preserved literally. |
| 77 definitions and square; 78 continuation | `i',i''; \lambda,\mu; f'\mapsto f'\circ i'', f\mapsto f\circ i'` | i’s have dots and no j descenders. One lower prose i′/i″ is marked independently. Lambda/mu have distinct handwritten shapes. |
| 79 products; 80 systems | `f_i,X_i,Y_i; p_n` / `\rho_n` | Dotted i without descender; n has no dot. p/rho first labelled system arrow remains ambiguous. |
| 80 upper and lower text | `\mathbb N` | Parallel left strokes are visible; ordinary order m≤n preserved. |
| 81 group-category example | `B_G` / `B_C`, then `G` | First low open contour ambiguous; full-size G nearby clearer. |
| 81 simplex-category example | `\mathbb{\Delta}` / `\Delta`, `[1]`, `\Delta^0,\Delta^1` | Parallel left edge on each triangular capital; first occurrence qualified. Square brackets at baseline; 0/1 raised. |
| 81 dual question | `u_!^W` | Exclamation mark below u, W above; dot distinguishes ! from a prime. |
| 67,72 quoted text | double backticks/apostrophes | Double quotation strokes retained, without substituting guillemets. |
| 66–81 short strokes and graphs | `-` / `\to`; solid, dashed, dotted, hooked arrows | Short heads uncertain locally; not harmonized from a functor’s expected direction. Scan 75 bottom-left arrow points left; scan 80 gap before X_n has no connector. |

## Doubts

Every explicit `\unsure` occurrence in the final page files is indexed below, including those inside deletions and insertions. “Line” is the stable line number in that scan’s page file, followed by a short textual context; this is more precise than guessing manuscript line numbers across overlapping crops. Alternatives are exhaustive among the candidates retained from the ink, not a claim that no other reading is possible. Confidence refers to the reading, not to its mathematical plausibility. No doubtful or cancelled reading supports an error claim above low confidence.

| Scan | Line and nearby text | First reading | Other retained candidates | Confidence | Context preference / grounds |
|---|---|---|---|---|---|
'''

tail = r'''
## Slips kept as written

These are textual discrepancies retained in the transcription. Mathematical assessment belongs in the post-freeze notes. No accent, agreement, or spelling error is attributed to the author where the ink remains unresolved.

| Scan / approximate locus | As written | Apparently intended / reading question | Grounds and confidence |
|---|---|---|---|
| 70, corollary before a) | `Pour X_bullet soit fibrant` | `Pour que X_bullet soit fibrant` | Repeated crop inspection finds no que between Pour and X. A likely omitted word; medium confidence in the omission as a slip, with the literal reading retained. |
| 78, lower representability paragraph | `adjoint à D.` then `cet adjoint à gauche` | The second may have intended à droite | Both words are clear and were reread. Apparent internal wording discrepancy, retained; assessment deferred to notes. |
| 81, last display | `TF=F∩C` | Possible intended `TF=F∩W`; no change | C is visibly different from the preceding W. Whether the intended class definition is the usual one is a mathematical question for the notes, not a licence to change C. |
| 76, composite arrow annotation | `u^*u_*G→G` with no primes | Nearby objects use G′ | Missing primes may be informal notation or a slip; low confidence in any error claim. |
| 73, reducible case | `I_1^circle,I_2` | Second raised circle might have been intended | The second circle is absent in the ink; no symbol supplied. Low-confidence notation question. |

## Abbreviations met

Expansions are proposed here only. They are never inserted into the transcription.

| Written form | Proposed expansion | Representative scans |
|---|---|---|
| th.; th.-scholie | théorème; théorème-scholie | 66,68,74,79 |
| prop.; cor.; Cor.; dém. | proposition; corollaire; démonstration | 66,70,71 |
| cat.; Cat; Diag | catégorie; catégories; diagrammes / diagram-shape category | 66,73,79,81 |
| ens.; sous-ens | ensemble; sous-ensemble | 67,74,80 |
| Ob | objets | 66,77 |
| noeth.; top. | noethérien; topologique | 67 |
| tt; tte; ttes | tout; toute; toutes | 67,73,76 |
| croiss.; str. | croissante; strictement | 67,73 |
| pt; élémᵗ | point; élément | 67,68,73 |
| immers. | immersions | 66 |
| hom.; iso; isom. | homomorphisme; isomorphisme | 68,71,75,78 |
| adj.; à D. | adjonction / adjoint; à droite | 68,77,78 |
| comp.; comm.; diagr. | compatible; commutatif; diagramme | 70,74,76,78 |
| mbres | membres | 75,76 |
| hyp.; suppl. | hypothèse(s); supplémentaire(s) | 74,76 |
| p.; p.ex.; resp; i.e. | page; par exemple; respectivement; id est | 66–78 |
| viz. | videlicet | 72 |
| NB; OK | nota bene; okay | 66,70,71 |
| tjrs; syst.; gén.; autom. | toujours; systèmes; générateurs; automorphismes | 78,80,81 |
| literal `=` in prose; `=s` | même; mêmes | 73,74,78,80 |

## Legibility and limits

All sixteen sheets were viewed whole and in all three supplied thirds, then independently reread crop-first. The audit retains actual times and rejected preliminary hypotheses; a supplemental comparison was added for the shorter audit intervals. The fast prose, heavily cancelled starts, tiny slanted notes, and local arrowheads are less secure than the larger formulas. In particular scan 66’s opening revision, scan 70’s exercise insertion and margin, scan 75’s overwritten localization diagram, scan 77’s small parenthesis, scan 78’s marginal comment, and scan 80’s compressed phrase before axiomes remain low confidence.

No OCR, outside transcription, web source, or LaTeX compiler was used. A zero count of `\illegible` means that tentative candidates could be offered at every doubtful locus; it does not imply certainty or the absence of transcription errors. Original first-reading hypotheses are retained separately as historical working documentation and are superseded by this register and the final page files.
'''

def main():
    old = OUT / f'{ID}_doubts.md'
    historical = OUT / f'{ID}_first_reading_apparatus.md'
    if not historical.exists():
        historical.write_text('# HISTORICAL — superseded working readings\n\nThis is the first-reading apparatus before the final audit reconciliation. Do not use its superseded readings in preference to the final doubts file.\n\n' + old.read_text())
    # A literal manuscript parenthesis must not be a TeX math-mode closing command.
    q = OUT / 'pages' / f'{ID}_157-4_scan067.tex'
    s = q.read_text().replace(r'\unsure{\)}', r'\unsure{)}')
    q.write_text(s)
    files = sorted((OUT/'pages').glob('*.tex'))
    alltext = '\n'.join(q.read_text().rstrip()+'\n' for q in files)
    (OUT/f'{ID}_transcription.tex').write_text(alltext)
    (OUT/f'{ID}_standalone.tex').write_text('\\input{PREAMBLE.tex}\n\\begin{document}\n\\input{'+ID+'_transcription}\n\\end{document}\n')
    body = []
    for q in files:
        scan = int(re.search(r'scan(\d+)',q.name).group(1)); s = q.read_text()
        for start,end,arg in macro_occurrences(s,'unsure'):
            line = s.count('\n',0,start)+1
            context = s[max(s.rfind('\n',0,start)+1,start-32):min(end+32,s.find('\n',end) if '\n' in s[end:] else len(s))]
            candidates = arg.split('|')
            body.append(f'| {scan} | l.{line}: `{cell(context)}` | `{cell(candidates[0])}` | {"; ".join("`"+cell(c)+"`" for c in candidates[1:]) or "none secure"} | low | {cell(explanation(scan,arg))} |')
    old.write_text(notation+'\n'.join(body)+'\n'+tail)
    # Normalize permitted metadata and separate formerly combined elements.
    inv=OUT/f'{ID}_inventory.csv'
    with inv.open(newline='') as f: rows=list(csv.DictReader(f)); cols=list(rows[0])
    for r in rows:
        r['sheet_kind']='text'
        if r['element']=='072-02':r['first_words_or_objects']='fait que'
        if r['element']=='072-13':r['first_words_or_objects']='(α)'
        if r['element']=='075-03':r['first_words_or_objects']='possible cancelled c in upper star: state uncertain'
        if r['element']=='079-05':r['first_words_or_objects']='d’un/d’une plus doubtful est/et beneath crossing'
    if not any(r['element']=='072-02b' for r in rows):
        rows.append(dict(zip(cols,['157-4','72','text','Grothendieck','072-02b','deletion','top within inserted l’hyp.','inutile/utilisée before pertinente','yes'])))
        rows.append(dict(zip(cols,['157-4','72','text','Grothendieck','072-13b','insertion','foot after I','=I0/Icircle','yes'])))
    position_order={'066-audit-01':6.5,'066-audit-02':11.5,'070-audit01':9.5,'072-audit01':6.5,'072-supp01':9.5,'077-audit01':17.5,'072-02b':2.5,'072-13b':13.5}
    def key(r):
        el=r['element']; ordinal=position_order.get(el)
        if ordinal is None:
            m=re.search(r'(\d+)$',el); ordinal=int(m.group(1)) if m else 999
        return int(r['scan']),ordinal
    rows.sort(key=key)
    with inv.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
    print(json.dumps({'pages':len(files),'unsure_rows':len(body),'inventory_rows':len(rows)},indent=2))

if __name__=='__main__':main()
