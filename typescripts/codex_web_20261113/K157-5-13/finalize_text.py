"""Prepare descriptive apparatus from the visually read page files; no OCR or TeX execution."""
from pathlib import Path
import re, csv, hashlib, json
from workflow import OUT, TASK, argument, inventory, utc, log

NOTATION = r'''# K157-5-13 — notation and doubts

## Notation table

This is the reconciled table after the image-first audit. It supersedes the preliminary readings in `notation_working.md`; that file preserves the history of revisions. Locations refer to the manuscript's approximate lines or named blocks, not to a printed edition. The supplied preceding material has no K157-5-01–12 folders. The available K157-4-04 table and the other supplied cote-157 tables were read before the first page, but no reading was imported against the present ink.

| Scans and location | LaTeX reading and every recurring alternative | Ink and reconciliation |
|---|---|---|
| 197, lines 4–11; 198, opening paragraph | `K` / `\mathscr K` | K has long oblique arms, without a decisive script loop. First occurrence on each page marked; later same-form K uses the first candidate. |
| 197–212, throughout | `M`, `C`, `F`, `X`, `x`; `M_\pi`, `\mathrm{Filt}^\pi` | Plain capitals. M's pi is below, Filt's pi above. Every local prime and nested exponent was read separately; no regularization of differing bounds. |
| 198, displayed powerset; 199, middle paragraph | `\mathscr P` / `\mathfrak P` / `\mathrm P` | Returning upper curve and lower stroke do not decide the alphabet. First occurrence on each page marked. This powerset glyph is not transferred to the plain P of P(pi) on 209–210. |
| 197, last paragraph; 200, item 3; 203, proof; 206, opening display; 212, right note | `i`, `X_i`, `x_i`, `i\in I`, `i\in C/x` | Short stems without descenders. The source's lower/upper case X/x retained. |
| 201, construction, lines 10–18; 209, sideways margin | `j`, `J`, `X_j`, `j\mapsto X_j` | The lower j has a descender. 209's initial J/I remains local doubt; it is not silently resolved by the later j. |
| 201, construction; 205, slice display; 206, first display; 208, cardinal I display | `I` / `\bar I` | Detached-looking horizontal may be a capital-I serif or a separate bar. First such occurrence on each page marked. Elsewhere clear plain I is retained. |
| 198–199, cardinal calculations | `J'`, `J'_0`, `E_0`, `\pi_0`, `\operatorname{card}`, `\mathrm{Aut}` | Prime and lower zero are distinct. 199's initial parenthesis remains `E_0)|(E_0)`; no missing left parenthesis silently supplied. |
| 200–212, cardinal bounds | `\pi`, `\pi'`, `\pi_0`, `\pi_1`, `\pi_2` | Separate strokes for primes and low indices; overwritten positions carry local alternatives. 200's long exponent and 206's bound remain whole-expression doubts. |
| 200, heading and labels; 201–202, references | `4.5.5|4.5.6`, `a'|a''`, `c|\sigma` | Heading and prime count read locally, not corrected to later references. 202's first a=>c and final a''=>c deliberately differ. |
| 202, C-definition | `\mathrm{Ens}(\leq\pi_0)|\mathrm{Ens}(\pi_0)` | Possible inequality survives in a retouched parenthesis. First card(X) and later card X retain their differing brackets. |
| 203, lemma and functor category; 204, evaluation and adjunction | `\mathscr E` / `\mathcal E` / `E` | Looped category capital differs from the three-bar object E and two-bar functor F. First live category occurrence on each page marked. A separate cancelled E on 204 has its own uncertainty. |
| 203, middle paragraph | `\mathcal U` / `U` | U ornament is not decisive; first occurrence marked. |
| 203–204, functor categories | `\underline{\mathrm{Hom}}(C,\mathscr E)`, `\widehat C`, `\mathrm{Fl}`, `\mathrm{Ob}` | Underline on category Hom and roof on C retained. Fl and Ob are read separately; the cancelled Ob/Fl alternative on 203 remains local. |
| 204, top diagram and evaluation | `e|\mathbf e`; `\varepsilon_x|\epsilon_x`; `\varepsilon_x^*`, `\varepsilon_{x*}` | Upper star denotes the ink's evaluation label, lower star the adjoint label. Two retouched lower stars beside evaluation x are recorded as deleted. No star moved for mathematical reasons. |
| 205, proposition and proof | `\mathrm{Ind}'_{\pi_0}(C)`, `\operatorname{Sup}` | Prime after Ind and low pi-zero; Sup has a tall initial S. |
| 206, lemma; 207, first bound | `\pi^*|\pi^+|\pi^\sharp` | Raised decoration has crossing strokes; star is ink-first, plus and sharp remain possible. Repetitions follow the first candidate. Clear single prime strokes on 207 remain primes. |
| 206, final construction | `\widehat C(\pi^*)|\widehat C(\leq\pi^*)`; `C^\circ|C^0` | Possible inserted inequality and small ring/zero remain uncertain. A cancelled lower zero is preserved. |
| 207, natural transformations | `C|G` after F; then C in Hom(F,C) | Open curved second capital favours C from ink, although the function of the letter does not select its name. |
| 208, lower construction | `I'_0|I'` | Low mark intersects the serif; not harmonized with adjacent formulas. |
| 209, assertion a and family c | `\varphi|\phi`, `u_\alpha|f_\alpha` | Curved phi and heavily retouched family letter remain marked. b' has plain I twice; b'' has I'. |
| 209–211, conditions | `P(\pi)`, `\mathrm{Filt}'{}^\pi` | P plain. Prime immediately after Filt differs from unprimed Filt. All occurrences checked independently. |
| 211, final paragraph | `\neq|\not\geq|\not\leq` at first relation; later `\neq` | First relation overwritten; second has a clearer slash across equality. |
| 212, first paragraph | first `\geq|>`; lower `\pi_0|\pi_1` | Retouched family relation and dense subscript unresolved; cancelled glyph before the live geq recorded separately. |
| 201, proof chain; 210 and 212, diagrams | `\Rightarrow`, `\longrightarrow`, `\simeq`, `\approx` | Double versus single shafts and arrow direction retained. 212 has seven arrows in the six-object diagram and one final arrow. The source stroke after b'' remains dash/point, not an invented arrow. |
| Throughout | `\varinjlim`, locally uncertain `\varinjlim|\varprojlim` in cancelled material on 203 | Underarrows read from their heads. Source line breaks alone govern aligned displays. |
| Throughout | `\uline`, `\uuline`, `\deleted`, `\inserted`, `\margin` | Underlines are distinct from cancellations and insertion leaders. All sheets are handwritten; no redundant handwritten wrapper. Sideways and slanted notes were rotated and read in their own direction. |
| Prose throughout | French accents and source abbreviations | Reduced endings retain local doubts. The table below does not use grammatical or mathematical expectations to replace ink. Source punctuation is retained, including doubtful closing bracket on 207 and brace on 212. |

## Table of doubts

Each occurrence is listed, including uncertainty within a deletion. The position names the source block and approximate manuscript line when known; the TeX line is an additional reproducible locator. Alternatives are those in the final text. A single reading with no alternative is still uncertain. “Ink-first only” means the surrounding text does not independently settle the strokes, not that the reading is secure.

| Scan | Approximate source line / block; TeX line | Ink-first reading | Other ink-permitted candidates | Confidence | Context preference and reason |
|---|---|---|---|---|---|
'''

def cell(s):
    return s.replace('|','&#124;').replace('\n',' ')

def doubts():
    rows=[]
    for p in sorted((OUT/'pages').glob('*.tex')):
        s=p.read_text(); scan=int(re.search(r'scan(\d+)',p.name)[1]); pos='opening'
        cancelled=[]
        for m in re.finditer(r'\\deleted\{',s):
            _,e=argument(s,m.end());cancelled.append((m.start(),e))
        for m in re.finditer(r'^% element: ([^|]+)\|([^|]+)\|([^\n]+)|\\unsure\{',s,re.M):
            if m.group(1):pos=m.group(2).strip();continue
            a,e=argument(s,m.end()); alts=a.split('|'); line=s[:m.start()].count('\n')+1
            crossed=any(lo<m.start()<hi for lo,hi in cancelled)
            conf='low' if crossed or any(t in pos for t in ['margin','diagonal','edge','foot']) or len(alts)>2 else 'medium'
            ctx='Ink-first only; the compressed or retouched strokes do not independently decide the reading.'
            if crossed:ctx='Cancelled reading; surrounding live text does not recover the obscured strokes.'
            if a==r'4.5.5|4.5.6':ctx='Later references favour 4.5.6; the heading itself still permits 4.5.5, which remains first.'
            elif a==r'\pi_0|\pi_1':ctx='The preceding cardinal hypotheses may suggest pi-zero; the low overwritten stroke itself remains undecided.'
            elif a==r'\mathscr E|\mathcal E|E':ctx='The category role distinguishes this from object E but does not decide the drawn alphabet; script E remains ink-first.'
            elif a==r'\}|)':ctx='An opening parenthesis would favour a closing parenthesis; the visible cusp favours a brace, which remains first.'
            elif a=='une connue|bien connue|connue':ctx='Idiomatic French may favour bien connue; the visible initial strokes favour une connue. This is a reading question, not a spelling correction.'
            elif a=='épimorphique strict|épimorphique stricte|épimorphiques stricte':ctx='Agreement with famille would favour stricte; the ending is not clear enough to change the ink-first strict.'
            elif a==r'C|G' and scan==207:ctx='Either letter can name the second functor; no mathematical preference decides the open curved stroke.'
            elif a.startswith('I|'):ctx='The role as an indexing category allows either notation; a serif versus an overbar is an ink question.'
            elif a=='grd|grand' or a=='grd|grde|grand':ctx='The context supplies the meaning grand/grande devant, but does not justify expanding compressed grd in the transcription.'
            rows.append(f'| {scan} | {cell(pos)}; TeX {line} | `{cell(alts[0])}` | '+(' ; '.join('`'+cell(x)+'`' for x in alts[1:]) or 'none identified')+f' | {conf} | {ctx} |')
    tail=r'''

The single `\illegible{3}` is in scan 203's densely cancelled middle paragraph (near the former conditions). The remaining ink of approximately three prose words could not be separated at maximum enlargement. It is not a mathematical symbol or a diagram omission. The surrounding readable words and cancelled mathematical expressions are transcribed with explicit alternatives.

## Apparent slips kept as written

| Scan / location | As written | Apparently intended | Reason and confidence |
|---|---|---|---|
| 204, adjunction display | right inner `\varepsilon_{x*}(F)` | possibly `\varepsilon_{x*}(E)` | The two-bar F is retained. The question of the argument's type is reserved for the post-freeze mathematical notes; this table makes no proof claim. |
| 204, product formula | `E^{\mathrm{Hom}(x,y)}` with left argument `y|x` | possibly reversed Hom arguments | A variance question, not a transcription repair; the uncertain left argument caps any error claim at low confidence. |

Other tempting “corrections” remain reading questions: the 200 proposition number, the final subscript on 202, the second functor letter and altered label on 207, the repeated ordonnée on 209, and compressed agreements throughout. No grammatical slip is asserted on the basis of an uncertain ending.

## Abbreviations encountered

Expansions are conjectural aids here only; they are not inserted into the transcription.

| Written form | Probable expansion or function |
|---|---|
| cat.; sous-cat. | catégorie; sous-catégorie |
| str.; gén. | strictement/strict according to phrase; génératrice |
| ens; Ens | ensemble(s); category of sets when a mathematical name |
| tt; tte; quelc. | tout; toute; quelconque |
| grd; grde | grand; grande |
| card; Ob; Fl; Aut; Hom | cardinal; objets; flèches; automorphismes; morphismes |
| Filt; Ind | The manuscript's named classes/construction; no expansion of their mathematical definition is supplied here. |
| p.; pg; p. ex. | page; page; par exemple |
| cf.; loc. cit.; resp. | confer/comparer; loco citato; respectivement |
| prop.; cor.; dém.; Dém. | proposition; corollaire; démonstration |
| NB; i.e.; ssi | nota bene; id est; si et seulement si |
| AQT | Proof-ending initials; their expansion is not established by these pages and is left unresolved. |
| chgt | changement |
| reven. à | probably revenant/revenons à; the dot and competing word endings remain in the doubt table |
| SGA | Source's title abbreviation, left as written, with tome/section numerals preserved |

## Legibility and limits

The sheets are readable working notes, but their rapid hand frequently reduces word middles and endings to single strokes. The least secure material is the long sideways note on 197, the diagonal NB on 200, the overwritten middle of 203, the high cardinal decorations on 206–207, the long marginal addition on 209, and compressed prose and overwritten relations on 211. All sixteen whole pages and their three strips were viewed in order. The second reading was image-first with separate blind word lists, enlarged and rotated checks where needed, formula inventories, and recorded actual times. One prose-only illegible mark remains; numerous explicit alternatives are an honest record of unresolved ink, not claims of an error-free edition. No OCR, external edition, PDF text layer, web source, or TeX compilation was used.
'''
    (OUT/f'{TASK}_doubts.md').write_text(NOTATION+'\n'.join(rows)+tail)
    return len(rows)

if __name__=='__main__':
    print('Doubt rows:',doubts())
    print('Inventory rows:',inventory())
