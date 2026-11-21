"""Prepare the apparatus from personally read and audited pages; no recognition or TeX."""
from pathlib import Path
import re
from workflow import OUT,TASK,argument,inventory

NOTATION=r'''# K157-5-14 — notation and doubts

## Notation table

This reconciled table supersedes the preliminary entries in `notation_working.md`, which remains as a record of first-pass readings. It starts from K157-5-13's notation table, but every entry below was checked on the present scans. The supplied other cote-157 tables are documentary background, never sources of missing readings. Locations identify the source block; the doubt table also gives reproducible TeX line numbers.

| Scans / location | LaTeX reading and recurring alternatives | Ink and reconciliation |
|---|---|---|
| 213–228, category and object names | `M`, `C`, `S`, `A`, `B`, `I`, `J`, `x`, `y` | Plain handwritten letters. Heavy retracing is not treated as blackboard type. Local cancelled capitals remain separately doubtful. |
| 213, upper presentation and J-map | `I`, `I'`, `J`, `x_i`, `x_J` | Capital J has a hook; lower i has no descender. The plain I continues the preceding task's indexing notation. |
| 213, middle cardinal display | `\mathscr P` / `\mathfrak P` / `\mathrm P`, subscript `f` | Curled powerset capital agrees with the alphabet ambiguity on 198–199. It differs from plain `P(\pi)` in the proof below. |
| 213–228, limit signs | `\lim`, `\underline{\lim}`, `\varinjlim`, `\varprojlim` as drawn | No arrow supplied from the mathematics. Bare lim on 213's middle display and 215's last formula; flat underbars in much prose; clear right heads in many displays. Scan 219 opens with a left head and then has right heads. |
| 214–215, family diagrams | `\alpha`, `\beta`, first `\sigma` / `\gamma`; `u`, first `v` / `\nu`, `w` / `\omega` | Alpha and beta distinguished by their loops. The small curled third index remains doubtful once per page. Different cancelled lambda-like ink on 215 has its own doubt. |
| 214–215, arrows | single arrows; 215 upper `Rightarrow`; unheaded lower diagonal | Shaft count and heads retained. The first map on 215's final line permits a doubly capped unheaded stroke or mapsto; not changed to fit the functor. |
| 214, final diagram; 228, Hom calculation | clockwise vertical `\in` above `\mathrm{Ob}\,C_0` or `M_0` | The short sign has the prongs of rotated membership, not a vertical arrow. Reproduced by rotated TikZ labels/nodes. |
| 215 and 220, presentation formulas | first `x'` / `x^i` / `x_i`; later clear `x_i` | High dot and short right stroke do not securely decide prime versus index in those individual positions. Nearby clear subscripts do not erase this doubt. |
| 216, functors; 225, transfinite factorization | first `\varphi` / `\phi` | Open loop and descending stem favour varphi. Source subscripts are retained independently; the factorizing subscript on 225 is alpha, though its codomain is C-alpha-prime. |
| 216, final condition chain | first `2'` / `1'`; later `2'` | The same recurring doubtful label is marked once. Its later repetition uses the ink-first candidate, as required by the recurring-glyph rule. |
| 217, lemma introduction and conditions a,b | `M_0^{\sharp}` / `M_0^*` | Forked raised sign. Condition c and the final assumption have plain M-zero; the decoration is not supplied there. Final equality has a separate zero/pi doubt. |
| 216–223, filtration notation | `\mathrm{Filt}'{}^\pi`, `\mathrm{Filt}^\pi`, `M_\pi` | Prime and upper/lower placement read separately. Scan 218's first stability clause has lower pi on Filt, while the subsequent occurrences have upper pi. |
| 220, first Filt expression | following `\sharp` / `\natural` / `\S` | Extra crossed/looped mark is retained locally; its attachment is not silently regularized. It is absent from the final Filt expression on that page. |
| 218, inserted cardinal condition | `\pi=\pi_0` / `\pi\geq\pi_0`; separate `\pi_0` / `\pi_p` | Tiny strokes are unresolved. These readings cannot support a confident convention or error claim. |
| 219, group example | `G_0`, `G_1`, `H`, `u_0`, `u_1`, first `h` / `u`, `e` | Zeros/ones are numerals, not i/j. G has a return bar; H has two stems. Diagonal is unheaded, the parallel injections and e-to-H have heads. |
| 219, prose shorthand; 226–227, majorations | `\overline{\mathrm m}` / `\simeq`; later `=` / `\bar m` | The drawn forms differ. The probable meaning même is recorded only in the abbreviation list; no expansion or forced normalization in the transcription. |
| 221, index-family calculation | `B=\coprod B_\alpha`, then `\operatorname{card}D` | Final audit distinguished the single-bowl D from B; the mismatch is kept. The next pi at the edge remains doubtful. |
| 222, inserted qualification | `\mathrm{Fl}` / `\mathbb F\mathrm l`; `\mathrm{Ob}`; lower `i` in `I` | Possible double stroke on F is local, not a page-wide alphabet change. Lower i has no descender. |
| 223, heading and chain | `proto-topos` / `prototopos`; `\mathrm{PTA}`; label alpha / a | Heading hyphen remains uncertain; plain capitals in PTA. No asterisk retained as a chain-label candidate after enlarged inspection. |
| 223–224, equivalence diagrams | `\approx` | Two wavy strokes, rather than a wavy stroke above a straight bar. This differs from the clear simeq signs elsewhere. |
| 223 and 228, universe letter | `U` / `\mathcal U` / `\mathscr U` | Ornament is not decisive. Plain U is ink-first here, unlike the earlier task's first calligraphic candidate on 203; no convention is imposed across the difference. |
| 223–228, canonical functors | `\mathrm{Ind}'_{\pi_0}(C)` or `(M_0)` | Separate prime and low pi-zero in the main functors. Scan 224's margin has pi without zero; scan 228's final Hom subscript has `\mathrm{Ind}_{\pi}(M)`, without prime or zeros. |
| 224, preservation condition | `\rho` / `\varphi` / `\phi` | Closed upper loop and descending stem favour rho; the category-theoretic role does not settle the glyph. |
| 224–227, ordinal stages | `\alpha`, `\alpha'`, `\alpha+1`, `\alpha_0`; `\bar I_{\alpha_0}` | Prime, plus-one, and zero read separately. Scan 225's union has independent alpha-prime/star/sharp and alpha-prime/beta-prime doubts. The later factorization and successor object are not harmonized. |
| 225, first closure bound | `\leq\pi` | No zero is visible in this first bound; later bounds are pi-zero. Kept as written. |
| 225, lemma number and initial article | `4.6.` followed by `1` / deleted `1`, then `2`; La/Toute and state alternatives | Retracing and a lower grey stroke do not securely decide cancellation. No missing dot is invented between 1 and 2. |
| 225–227, reduced-cardinal operator | first `\operatorname{card\,rél}` / `\operatorname{card\,réd}`; later `red` and `réd` | Scan 225 has one accented e and an uncertain final l/d, not two e's. Scan 226 has clear terminal d without acute accent. Scan 227 alternates accented and unaccented forms according to the ink. |
| 226, reduced category and closure | `A_0`, `C'_0` / `C_0`, `\bar I`; corollary `C_0` / `C` | Both A subscripts are independent zeros. First C-prime partly intersects a leader; later prime is clear. Bar above I is detached from its serif. Corollary's small low loop favours zero despite the later C. |
| 227, successor estimate and products | `C_\alpha`; `\pi_0\cdot\pi_0`; `\pi'_0\pi_1^{\pi_0}` | No +1 supplied in the successor estimate. Visible multiplication dots are retained; no dot inserted in the final product. |
| 228, foot Hom display | first colimit `j` / `i` in I; later `i` and `j`; comma left, semicolons right | First index has a descending hook; all subsequent indices checked independently. Each right-hand separator has a distinct upper dot and lower comma. |
| Throughout | source underlining, cancellations, insertions, margins | Every page is handwritten in the manuscript hand. No whole-page handwritten wrapper. Oblique notes were rotated; ambiguous reinstatement/insertion boundaries remain explicit state alternatives. |

## Table of doubts

Every actual doubt macro is listed, including those in cancelled material. TeX comments are not counted. Alternatives are split at the outer level, so nested state macros stay together. Confidence concerns the reading, not mathematical truth. A single candidate still marks unresolved strokes. “No independent context preference” means context supplies no additional way to distinguish the visible candidates.

| Scan | Approximate source block / line; TeX line | Ink-first reading | Other ink-permitted candidates | Confidence | Context preference and reason |
|---|---|---|---|---|---|
'''

def split_outer(s):
    out=[];start=0;depth=0;i=0
    while i<len(s):
        if s[i]=='\\':i+=2;continue
        if s[i]=='{':depth+=1
        elif s[i]=='}':depth-=1
        elif s[i]=='|' and depth==0:out.append(s[start:i]);start=i+1
        i+=1
    return out+[s[start:]]

def cell(s):return s.replace('|','&#124;').replace('\n',' ')

CONTEXT={
 r'\mathscr P|\mathfrak P|\mathrm P':'The finite-subset role supports a powerset symbol, but does not decide its drawn alphabet.',
 'n|3':'The progression of powers suggests a variable n; the small raised form still permits 3.',
 r',|+\cdots|\cdots':'The cardinal sum permits continuation dots, but the right-edge marks do not secure a plus sign or exclude a comma.',
 'indexé par|indexé sur':'Both prepositions fit the indexing phrase; no independent context preference.',
 r'x_\alpha\times_x x_\alpha|x_\alpha\times x_\alpha':'The surrounding fibre-product construction favours the lower x; its separate stroke is uncertain here.',
 'de|vers':'The described arrows point toward the represented object, favouring vers in sense; the shorter ink favours de.',
 r')|\}':'The opening parenthesis favours a parenthesis; a cusp in the ending still permits a brace.',
 r'\times|<':'The product context favours times; the reduced crossing can also look like a less-than sign.',
 'utilisons|utilise':'The following first-person plural choisissons favours utilisons; the compressed ending itself remains doubtful.',
 r'\sigma|\gamma':'Either Greek letter can label the third index; no mathematical choice settles its loop.',
 r'v|\nu':'Both can label this component; the two-stroke Latin v is ink-first.',
 r'w|\omega':'Both can label this component; the angular w is ink-first.',
 '2|3':'Counting two component choices suggests 2, but this does not resolve the dense raised ink.',
 r'\alpha_\beta|\alpha':'Mapping the object alpha to x-alpha favours plain alpha; the extra low stroke is retained in the ink-first candidate.',
 r'\mathrel{\vert\!-\!\vert}|\mapsto':'Functor notation suggests mapsto; the drawn right end is capped rather than securely headed.',
 "x'|x^i|x_i":'The indexed family favours x-sub-i; the local high dot and right stroke favour a prime or raised i from ink.',
 r'\longrightarrow|\mathrel{-}':'A functor calls for an arrow in meaning, but the right end is not visually decisive.',
 "2'|1'":'The nearby condition chain favours the first 2-prime reading; the small overwritten digit remains unresolved.',
 'standart|standard':'Ordinary spelling favours standard; the terminal stroke looks t-like. This remains a reading question, not a spelling-error claim.',
 r'x\cdot|x_i':'The family notation favours x-sub-i, but the first mark appears dot-like rather than a secure lower stem.',
 'le|la':'Agreement with sous-catégorie favours la; the visible reduced article is not changed for grammar.',
 'formée|fermée':'The phrase des objets favours formée; the first vowel is compressed and does not conclusively rule out fermée.',
 '0|\\pi':'The named subcategory is M-zero in the assumptions, favouring zero; the low retouched glyph also permits pi.',
 '3|B':'The numbered implications of 4.5.13 favour 3; the closed upper/lower loops resemble B.',
 'ici|i.e.':'The explanatory clause permits both ici and i.e.; punctuation and reduced strokes remain uncertain.',
 r'\pi=\pi_0|\pi\geq\pi_0':'Either restricts the surrounding assertion; no mathematical inference is used to choose the tiny relation.',
 r'\pi_0|\pi_p':'The established cardinal is pi-zero, favouring zero in context; the small downstroke still permits p.',
 'structures|structure':'The construction can be read with either number; the word ending is too reduced to settle it grammatically.',
 'discrète|abstraite':'Both are plausible in the surrounding description; their meanings do not decide the obscured internal strokes.',
 'g|e':'The phrase exacte à g suggests gauche; the looped letter itself can resemble e.',
 "à une limite|d'une limite|non évidente":'The insertion is highly compressed and its precise qualification of the family is unsettled; no context-based reconstruction is adopted.',
 r'\overline{\mathrm{m}}|\simeq':'The prose meaning suggests même; this explains the barred-m abbreviation but does not erase the sign alternative.',
 'données|donnés':'Agreement with injections favours données; the final e/s sequence is not certain enough for a grammatical claim.',
 'h|u':'The source calls its element h again in the same example, favouring h; this first loop can resemble u.',
 'p.ex.|i.e.':'The parenthetical connection may be explanatory or exemplary; context does not decide the abbreviated strokes.',
 'stricte|strictes':'Agreement with the singular family favours stricte; the terminal strokes still permit a plural ending.',
 'universelles|universelle':'Agreement with famille favours universelle; the ink-first terminal s is not silently removed.',
 'strictes|stricte':'The rewritten phrase la famille favours stricte; the surviving ending can also belong to the preceding plural construction.',
 'a|c':'The earlier indexed-presentation condition suggests a-double-prime; the small initial has a c-like alternative.',
 "l'ens|l'une":'The following des flèches favours the abbreviated ensemble; internal strokes remain compressed.',
 'où|ou':'The clause introducing an equality favours où; the accent itself remains uncertain.',
 'sur|\\deleted{sur}':'The preposition fits the sentence; a nearby line leaves its live versus cancelled state unresolved.',
 'équivaut|équivaut à':'The following clause favours an explicit connector, but no à is supplied unless the ink permits it.',
 'meilleur|meilleure':'Agreement with the understood catégorie would favour meilleure; the writer may be referring to M-pi itself. The ending is unresolved.',
 'catégoriques|catégorique':'The singular point de vue favours catégorique; the last reduced stroke still permits s.',
 'tautologique|catégorique':'The contrast with explicit criteria favours non tautologique; this does not settle the compressed middle letters.',
 "d'existence|d'exactitude":'The phrase refers to additional hypotheses on M, but that role does not decide which kind; existence remains ink-first.',
 'égale|égal':'An understood sous-catégorie favours égale; the final stroke is not used for an agreement-error claim.',
 r'\mathrm{Fl}|\mathbb{F}\mathrm{l}':'The count is of arrows Fl I; context does not decide whether the F is double-stroked or merely retraced.',
 'presque|précisément|puisque':'The rewritten explanation could favour précisément or puisque; the reduced first reading remains presque.',
 'proto-topos|prototopos':'Both name the same heading; only the presence of a tiny hyphen is at issue.',
 'étant|était':'The appended clause favours étant syntactically; the last strokes do not decisively exclude était.',
 '1|0':'The following explicit cutoff pi-one favours 1, but this first tiny digit independently permits zero.',
 r'\alpha|a':'This is an isolated chain label; context does not decide Greek versus Latin.',
 'accessibles|accessible':'Agreement with objets favours accessibles; the final small stroke remains uncertain.',
 '1°)|a)':'The subsequent numbered conclusions favour 1°); the dense shape also permits a).',
 'formée|formé':'Agreement with sous-catégorie favours formée; the last e is reduced.',
 'équiv.|équivalente':'The margin compresses its ending; the probable meaning équivalente does not justify expanding an abbreviation.',
 r'\rho|\varphi|\phi':'Any of the letters can name this functor; the closed upper loop favours rho without semantic correction.',
 'grdes|grds':'The plural feminine limites would favour grdes; the abbreviation’s tiny ending does not decide it.',
 'page|pge':'The meaning page is clear; the possible abbreviated spelling remains as ink.',
 "\\alpha'|\\beta'":'The union is indexed by alpha-prime, favouring the same letter in C; a longer left descender still permits beta-prime here.',
 '1|\\deleted{1}':'A lower grey stroke might cancel the first 1 or belong to its foot; the later numbering does not settle the state.',
 r'\operatorname{card\,rél}|\operatorname{card\,réd}':'The definition on 226 favours reduced-cardinal réd in meaning; the earlier final letter still looks l-like.',
 'pl|de':'The raised two-letter addition precedes baseline d’une; pleine is plausible in context, but a compressed de remains possible.',
 "C'_0|C_0":'The newly generated subcategory is distinguished later by a prime; the first possible prime intersects a leader.',
 'représentables|représentées':'Both fit limits considered in M; the reduced ending is not decided by that context.',
 'C_0|C':'The conclusion refers to C, favouring C as the new closure category; the low closed loop here favours C-zero from ink.',
 '=|\\bar m':'The prose il en est de / la ... majoration favours the abbreviation même; the written mark resembles equality.',
 r'\pi_1|\pi':'The majoration is expressed with pi-one, favouring that index; the tiny low stroke remains uncertain.',
 'Le|La':'A reference to the numbered item favours Le; the article’s end is reduced.',
 'la|le':'Agreement with majoration favours la; the ending remains doubtful.',
 'on a|...':'The sentence reads naturally with on a. The alternative denotes actual dot/dash-like ink, not an editorial omission or placeholder.',
 'stricte|strictement':'The recurring phrase strictement génératrice favours the adverb; the compressed insertion looks shorter and is retained as stricte first.',
 '2|4':'The nearby proposition’s second assertion suggests 2; the written internal reference also permits 4, and the extra 2° is retained.',
 'j|i':'The x_i family and later inverse limit over i suggest i; the first colimit index itself has a descending j-like hook.',
 ',|.':'The text continues beyond this page, permitting a comma; the small final tail remains uncertain.'
}

TAIL=r'''

There are no `\illegible` marks in this task. All difficult mathematical places have an ink-first reading with explicit alternatives, including state alternatives where cancellations or insertion spans are unresolved.

## Apparent slips kept as written

This is a register of apparent local discrepancies, not an independent validation of the proofs. Any item resting on a doubtful or cancelled reading has at most low confidence.

| Scan / location | As written | Apparently intended / reading question | Reason and confidence |
|---|---|---|---|
| 213, powerset display | one opening parenthesis after P-f and two closing parentheses around Fl I | possibly remove one closing parenthesis | Visible delimiter mismatch retained; high confidence in the ink, no mathematical correction made. |
| 215, last sentence | completion of 1° | possibly the subpart currently being proved rather than another numbered part | Number is kept; organization alone is insufficient to call it an error. Reading/organization question. |
| 218, first stability clause | Filt-prime with lower pi | upper pi as in subsequent occurrences | Placement differs locally; medium confidence as a notational slip, not a convention change. |
| 221, cardinal calculation | card D after B is defined | card B | The next sentence again says indexed by B; D was read distinctly in the audit. Medium confidence local letter slip. |
| 223, return to 4.3.6 | “si on n'admet que” followed by the cardinal-power condition | a different intended qualification is possible | No missing pas is supplied. This is a reading/meaning question, not an asserted repair. The open parenthesis is also kept unclosed. |
| 225, first bound | cardinal at most pi, then bounds with pi-zero | perhaps pi-zero in the first bound | No zero seen there; medium confidence local notational mismatch. |
| 225, factorization and next stage | varphi-alpha to C-alpha-prime, followed by C-alpha-plus-one | possibly a matching primed stage | Source subscripts are kept; low confidence because adjacent corrections and the bound-index reading are unsettled. |
| 225, lemma number | 4.6. followed by ambiguous live/cancelled 1 and then 2 | possibly 4.6.1.2 | No dot or deletion supplied from the later reference. Low-confidence numbering/state question. |
| 226, corollary category | C-zero/C, followed by le/la | possibly C and la | Both positions carry doubt. They are reading questions, not a grammatical error claim. |
| 226, corollary prose | “il en est de” followed by equals/barred-m and another “de C” | perhaps a repeated de | Both de's are live in the ink. Expansion of the shorthand is uncertain, so no confident grammatical correction is asserted. |
| 227, successor estimate | card red C-alpha | card red C-alpha-plus-one | The sentence applies the successor clause after assuming the bound for C-alpha; medium confidence local index slip. The majoration itself is expressly questioned by the author. |
| 228, opening conclusion | C=M-pi | C=M-pi-zero | The proposition and subsequent sentences use pi-zero; medium confidence local missing zero. |
| 228, foot Hom subscript | Ind-pi(M), without prime or zeros | perhaps Ind-prime-pi-zero(M-zero) | Compare the canonical functor immediately above; medium confidence notational mismatch. No symbol supplied in the frozen text. |
| 228, first colimit index | j/i in I, object x-i | i in I | Context favours i, but the hook looks j-like; low-confidence reading question, not a proven index error. |

## Abbreviations encountered

Expansions are aids in this list only and are not inserted into the diplomatic text.

| Written form | Probable expansion or function |
|---|---|
| cat.; sous-cat.; Cat; Gr | catégorie; sous-catégorie; named categories of categories and groups in the example |
| ens; ens.; élém. | ensemble; éléments |
| str.; pl.; gén. | strict/strictement; plein/pleinement; générateur/génératrice, according to the phrase |
| ép.; épim.; hom. | épimorphique/épimorphisme; homomorphisme |
| syst.; hyp; hyp.; top.; alg. | système; hypothèse; topologie; algébrique |
| tt; grd; grdes; grds | tout; grand; grandes/grands |
| card; card red; card réd; doubtful card rél | cardinal; reduced cardinal as defined on 226; accent and final-letter variations retained |
| Ob; Fl; Hom; Ind; Filt | source object/arrow/morphism and construction names; no new definition supplied |
| nb; nb.; tjs | nombre; toujours |
| prop.; th.; dém.; Dém; cf; cf.; p.; pge | proposition; théorème; démonstration; compare; page |
| i.e.; p.ex.; NB; qed; o.K/o.k | id est; par exemple; nota bene; quod erat demonstrandum; assent marker |
| chgt./chgts.; repr.; équiv.; préc. | changement(s); représentable/représenté; équivalente; précédente |
| barred m, or equals/barred-m alternative | probably même; the drawn forms stay distinct |
| pro.b.blement / prob.blement / prob.blemt | probablement; the written compression and dots are not expanded in the text |
| PTA; SGA | source acronym and title abbreviation; numerical references kept exactly as read |
| par./pr. at the end of 220's proof | possible proof-ending abbreviation; expansion unresolved |

## Legibility and limits

The main prose and diagrams are largely readable, but endings and mathematical subscripts are often reduced to a stroke. Least secure are the crossed reconstruction on 215, the slanted correction and interlinear qualification on 219, possible reinstatement marks on 221, crowded rewrites on 222–223, the cancelled ordinal note and lemma article on 225, the majoration notes on 226–227, and the overlapping hypotheses on 228. All sixteen pages and their three strips were viewed in order; the second pass began from the images before the page file was opened, with blind word/accent lists, actual times, and formula inventories. No OCR, recognition library, PDF text, external edition, web source, or TeX compilation was used. Explicit doubts are unresolved readings, not a guarantee that every remaining confident stroke is error-free.
'''

def doubts():
    rows=[]
    for p in sorted((OUT/'pages').glob('*.tex')):
        s=p.read_text();scan=int(re.search(r'scan(\d+)',p.name)[1]);pos='opening'
        cancelled=[]
        for m in re.finditer(r'\\deleted\{',s):
            _,end=argument(s,m.end());cancelled.append((m.start(),end))
        for m in re.finditer(r'^% element: ([^|]+)\|([^|]+)\|([^\n]+)|^%[^\n]*|\\unsure\{',s,re.M):
            if m.group(1):pos=m.group(2).strip();continue
            if m.group().startswith('%'):continue
            a,_=argument(s,m.end());alts=split_outer(a);line=s[:m.start()].count('\n')+1
            crossed=any(lo<m.start()<hi for lo,hi in cancelled)
            conf='low' if crossed or len(alts)>2 or any(k in pos for k in ['slanted','margin','cancelled','overwritten']) else 'medium'
            ctx=CONTEXT.get(a,'No independent context preference; reduced or overlapping strokes leave the ink-first reading uncertain.')
            if crossed:ctx='Cancelled/overwritten reading; the surviving live text cannot restore the hidden strokes. '+(CONTEXT.get(a,''))
            if '\\deleted{' in a or '\\inserted{' in a:
                conf='low';ctx='State/extent question: syntax may suggest a live phrase, but the intersecting lines or raised placement do not settle its cancellation/insertion boundary.'
            if a.startswith('U|'):ctx='The universe role permits all listed alphabets; the drawn ornament does not decide them.'
            if 'lim' in a and '|' in a and len(a)<75:ctx='The surrounding colimit discussion favours a right arrow, but the local bar/end strokes are retained independently; no head is supplied from context.'
            if a in [r'\forall|\mathrm{tt}',r'tt|$\forall$',r'tt|tout|$\forall$','Tout|tt','tout|tt']:
                ctx='The quantifying meaning is clear; context does not decide the written abbreviation versus symbol or full word.'
            if a.startswith('prob.') or a.startswith('pro.b.'):
                ctx='The meaning probablement is probable, but compressed letters and dots favour an abbreviation from ink.'
            rows.append(f'| {scan} | {cell(pos)}; TeX {line} | `{cell(alts[0])}` | '+(' ; '.join('`'+cell(x)+'`' for x in alts[1:]) or 'none identified')+f' | {conf} | {cell(ctx)} |')
    (OUT/f'{TASK}_doubts.md').write_text(NOTATION+'\n'.join(rows)+TAIL)
    return len(rows)

NOTES=r'''# K157-5-14 — page-borne notes

## Steps the pages themselves mark as unverified

- **218, lower paragraph:** “J'ai l'impression qu'il est” with inserted “un peu” and “plus général que le cas B)”; the proposed implication B implies C and failure of its converse are presented tentatively.
- **219, opening:** “je doute que la condition B) soit tjs satisfaite pour ces catégories.”
- **219, upper paragraph:** “je ne crois pas que les familles épimorphiques” (cancelled doubtful strictes) “soient universelles.” The slanted correction says “c'est faux !”; its cancelled wording and short connector remain doubtful, followed by “mais vrai dans le cas particulier plus bas.” This is the author's qualification, not an adjudication by the transcriber.
- **223, opening:** the earlier demonstration is called “incomplète (et erronée”; the author says the claimed cardinal filtration “est une filtration cardinale” is “faux” under his following written qualification. The transcription preserves the unclosed parenthesis and does not add a missing pas.
- **225, slanted note:** “? Un peu court. Il faut invoquer le fait que” the ordinal-index set is grand devant pi-zero; the short word and cancelled final parenthesis remain doubtful.
- **226, slanted note:** “Cette majoration n'est pas prouvée, et” a doubtful abbreviation of probablement, followed by doubtful “fausse”, “si on ne fait pas” and “strictes” in “des hypothèses un peu plus strictes”. The uncertainty of those words is explicit in the transcription.
- **227, slanted note:** “majoration” with doubtful “non prouvée”, a doubtful probablement abbreviation, “fausse, cf” doubtful “annotation” “ci-dessus.”

## Title sheets, dates and page counts

- **223:** section heading “4.6. Caractérisation des cat. proto-topos/prototopos (dém. de/du 4.3.6)”, with the indicated reading alternatives.
- **213–228:** author's consecutive manuscript page numbers **129–144**. The pencil archive numbers **212–227** are retained only in TeX comments, as requested.
- Separate title sheets: **none**. Dates: **none**. Explicit total page-count declarations: **none**. All sixteen are handwritten subject notes, not numbered typescript sheets or letters.
'''

if __name__=='__main__':
    print('Doubt rows:',doubts())
    (OUT/f'{TASK}_notes.md').write_text(NOTES)
    print('Inventory rows:',inventory())
