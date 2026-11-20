# What the second passes changed in our first readings

8093 changes in 29 collation tables (`SP_CHANGES.tsv`, one row each).

| class | changes |
|---|---|
| content | 6216 |
| doubt only | 1621 |
| markup only | 111 |
| inserted/placed | 73 |
| struck/live | 59 |
| ill resolved | 13 |

## By the run's own kind

| kind | content | doubt only | markup only | inserted/placed | struck/live | ill resolved |
|---|---|---|---|---|---|---|
| misread symbol or index | 1071 | 260 | 31 | 14 | 1 | 0 |
| omission | 897 | 311 | 21 | 8 | 30 | 1 |
| misread word | 813 | 381 | 5 | 17 | 4 | 0 |
| drawing or diagram | 1127 | 6 | 6 | 0 | 0 | 2 |
| readable ink left as \ill{} | 523 | 244 | 6 | 2 | 10 | 6 |
| insertion or placement | 548 | 30 | 9 | 11 | 1 | 1 |
| other | 341 | 111 | 18 | 10 | 1 | 1 |
| abbreviation expanded or spelling modernised | 284 | 170 | 3 | 4 | 0 | 0 |
| deletion state (struck given live or live given struck) | 342 | 62 | 3 | 3 | 6 | 2 |
| text not on the page | 164 | 15 | 4 | 1 | 0 | 0 |
| deletion state | 106 | 31 | 5 | 3 | 6 | 0 |

## Where nobody doubted

Content changes at places witness C had not marked: 3993 of 6216. Of these, witness H had the same reading as C and no doubt mark either: 1380 (both witnesses wrong the same way, nobody doubting; rows with `c_equals_h` = yes, `c_marked` = no, `h_marked` = no in SP_CHANGES.tsv).

| kind | C unmarked | C and H agree, both unmarked |
|---|---|---|
| drawing or diagram | 1038 | 542 |
| misread symbol or index | 641 | 214 |
| omission | 517 | 232 |
| insertion or placement | 436 | 66 |
| misread word | 429 | 151 |
| other | 251 | 88 |
| readable ink left as \ill{} | 185 | 0 |
| deletion state (struck given live or live given struck) | 156 | 24 |
| abbreviation expanded or spelling modernised | 146 | 40 |
| text not on the page | 143 | 8 |
| deletion state | 51 | 15 |

Examples where C and H agreed, both unmarked (ours = theirs → final):

- deletion state: SP02_CW_10+12 B10-01/33, 10.1, word immediately after j in I: `deux` → `deu\deleted{s}\inserted{\handwritten{x}}`
- deletion state: SP02_CW_10+12 B10-01/37, 10.10 heading, third letter of deux: `deux` → `de\deleted{\unsure{v|y}}\inserted{\handwritten{u}}x`
- deletion state: SP02_CW_10+12 B10-01/40, transition, second catégorie: overprinted fourth letter: `catégorie` → `cat\deleted{\unsure{u}}\inserted{é}gorie`
- deletion state: SP02_CW_10+12 B10-01/40, transition, opening parenthesis before second10 reference: `(` → `\deleted{\unsure{6|b}}\inserted{\handwritten{(}}`
- deletion state: SP02_CW_10+12 B10-01/41, principal-bundle paragraph, second letter of fibré: `fibré` → `f\deleted{o}\inserted{i}bré`
- misread symbol or index: SP02_CW_10+12 B10-02/42, second EGA number: `8.8.3` → `8 8.3`
- omission: SP02_CW_10+12 B10-02/42, la before propriété: `la` → `l\deleted{\unsure{j|f}}\inserted{a}`
- omission: SP02_CW_10+12 B10-02/43, first proof paragraph, physical break after quasi-: `quasi-séparé` → `quasi-\linebreak -séparé`
- drawing or diagram: SP02_CW_10+12 B10-02/44, joining stroke inside préschéma: `omitted` → `TikZ joining stroke between p and r`
- drawing or diagram: SP02_CW_10+12 B10-02/45, first insertion enclosure: `omitted` → `TikZ bracket and anchor`
- drawing or diagram: SP02_CW_10+12 B10-02/45, second insertion bracket: `omitted` → `TikZ hooked bracket`
- misread symbol or index: SP02_CW_10+12 B10-02/45, composition sign: `\circ` → `\unsure{o|\circ}`
- drawing or diagram: SP02_CW_10+12 B10-02/45, diagram left vertical shaft: `single vertical shaft and downward arrowhead` → `downward arrow with a second short, parallel headless shaft`
- drawing or diagram: SP02_CW_10+12 B10-02/46, Notons qu’ insertion marks: `omitted` → `TikZ pale caret before replacement`
- drawing or diagram: SP02_CW_10+12 B10-02/46, End formula insertion marks: `omitted` → `TikZ shallow lower brace with central dip`
- other: SP02_CW_10+12 B10-02/46, consequence end-line division: `opérations` → `opéra-\linebreak tions`
- other: SP02_CW_10+12 B10-02/47, deleted proof-opening punctuation: `.` → `\unsure{,|.}`
- other: SP02_CW_10+12 B10-02/47, first paragraph end-line division: `opération` → `opé-\linebreak ration`
- other: SP02_CW_10+12 B10-02/47, lemma end-line division: `définissant` → `définis-\linebreak sant`
- other: SP02_CW_10+12 B10-02/47, proposition end-line division: `devienne` → `de-\linebreak vienne`
- other: SP02_CW_10+12 B10-02/48, remark punctuation after de S: `,` → `\unsure{;|,}`
- misread symbol or index: SP02_CW_10+12 B10-02/48, inserted sentence terminal punctuation: `period` → `\unsure{;|!}`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-02/48, reference abbreviation overprinting: `Exp.` → `E\deleted{xp}\inserted{XP}.`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-02/49, overlapping letter in condition iv vectoriel: `vectoriel` → `vec\deleted{o}\handwritten{t}oriel`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-02/49, overlapping initial letter of condition iv dimension: `dimension` → `\deleted{\unsure{t|d}}\inserted{d}imension`
- omission: SP02_CW_10+12 B10-02/50, overtyped condition label after Comme: `v` → `\deleted{g}v`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-02/50, overlapping letter in quasi-compact before inserted et sépar: `compact` → `compa\deleted{\unsure{t}}\handwritten{c}t`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/51, first noetherian spelling: `noethérien` → `n\oe{} thérien`
- misread word: SP02_CW_10+12 B10-03/51, condition iii initial word: `On` → `\unsure{G|O}n`
- misread symbol or index: SP02_CW_10+12 B10-03/51, last handwritten base S: `S` → `\unsure{\mathbb{S}|S}`
- omission: SP02_CW_10+12 B10-03/51, marks around On before a alors: `On only` → `On with lower handwritten n and short upper dash/dot in TikZ`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-03/51, overlapping letters in quasi-séparé: `quasi-séparé` → `quasi-s\deleted{p}\handwritten{é}\deleted{\unsure{é|e}}\handwritten{p}aré`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/52, top noetherian spelling: `noethérien` → `n\oe{} thérien`
- deletion state (struck given live or live given struck): SP02_CW_10+12 B10-03/52, overprinted pair in structure: `structure` → `s\unsure{\deleted{rt}\inserted{tr}|\deleted{tr}\inserted{rt}}ucture`
- misread symbol or index: SP02_CW_10+12 B10-03/53, new character-map initial: `\widetilde{\lambda}` → `\unsure{\lambda|\widetilde{\lambda}|\chi}`
- misread word: SP02_CW_10+12 B10-03/54, first Soient: `Soient` → `So\unsure{e|i}ent`
- misread word: SP02_CW_10+12 B10-03/54, overworked letter in final axiome: `axiome` → `L'axio\begin{tikzpicture}[x=1cm,y=1cm,baseline=(a.base)]\node[inner sep=0pt] (a) at (0,0) `
- omission: SP02_CW_10+12 B10-03/55, faint extra plus before sum: `one plus` → `++`
- omission: SP02_CW_10+12 B10-03/55, closing mark after handwritten adjective: `omitted` → `)`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/55, handwritten semi invariants spacing: `semi-invariants` → `semi invariants`
- misread word: SP02_CW_10+12 B10-03/55, final quptient spelling: `quotient` → `quptient`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/56, opening representation accent: `représentation` → `representation`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/56, opening lineaire accent: `linéaire` → `lineaire`
- misread word: SP02_CW_10+12 B10-03/56, cancelled NB1 lineaire accent: `linéaire` → `lin\unsure{e|é}aire`
- misread word: SP02_CW_10+12 B10-03/56, cancelled NB2 demonstration accent: `démonstration` → `d\unsure{e|é}monstration`
- abbreviation expanded or spelling modernised: SP02_CW_10+12 B10-03/56, cancelled NB3 general accents: `général` → `general`
- misread symbol or index: SP02_CW_10+12 B10-03/57, middle base-change product: `\otimes` → `\unsure{\oslash|\otimes}`
- text not on the page: SP02_CW_10+12 B10-04/67, right-edge final word: `manque` → `manqu`
- insertion or placement: SP02_CW_10+12 B10-05/73, Galois capital position: `ordinary baseline G` → `raised G`
- deletion state: SP02_CW_10+12 B10-06/83, correspondance line break: `correspondance` → `corres + cancelled p + pondance`
- insertion or placement: SP02_CW_10+12 B10-08/121, outer closing parenthesis after equality: `ordinary )` → `handwritten )`
- insertion or placement: SP02_CW_10+12 B10-08/121, multiplications corrected cells: `multiplications` → `mu\rlap{\handwritten{l}}t\rlap{\handwritten{t}}liplications`
- insertion or placement: SP02_CW_10+12 B12-01/97, replacement above dernière: `\deleted{dernière}\inserted{\handwritten{cohomologie}}` → `\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{dernière`
- insertion or placement: SP02_CW_10+12 B12-01/97, développé and connecting stroke: `était\inserted{\handwritten{développé}} également` → `\mbox{\begin{tikzpicture}[baseline=(left.base)]
\node[inner sep=0] (left) {était};
\node[a`
- insertion or placement: SP02_CW_10+12 B12-01/97, replacement above limitée: `\deleted{limitée}\inserted{\handwritten{sujette à caution}}` → `\mbox{\begin{tikzpicture}[baseline=(old.base)]
\node[inner sep=0] (old) {\deleted{limitée}`
- text not on the page: SP14_CW_13+15+26+35+48+66+97+123+162 H97-01/2, signature after initial P: `J-P.` → `J-P`
- text not on the page: SP38_CW_75 J75-01/8, Punctuation after A in first slanted row: `\forall a\in A,` → `\forall a\in A`
- text not on the page: SP38_CW_75 J75-02/12, Second opening parenthesis before bijectif: `(bijectif)` → `bijectif)`
- text not on the page: SP42_CW_29 A29-01/11, Paragraph 1, line 8, after first ramification: `ramification.` → `ramification`
- text not on the page: SP47_CW_103 H103-02/13, Punctuation after exister: `exister.` → `exister`

## Content changes: the differing pieces (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
| `unsure→` | 183 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| `→retained` | 108 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/73 |
| `→d` | 104 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| `[→` | 99 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→e` | 79 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-04/67 |
| `omitt→curv` | 78 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| `→l` | 78 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `→n` | 64 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/68 |
| `?]→` | 62 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→ain` | 60 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10 |
| `s→` | 59 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127 |
| `→rawn` | 57 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `e→` | 52 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/67 |
| `→𝒞:` | 52 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `→.` | 48 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-05/74 |
| `→Creta` | 45 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `sert→` | 44 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/6 |
| `r→` | 42 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `→s` | 40 | SP02_CW_10+12 B10-01/33, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-04/61 |
| `→i` | 40 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `d→` | 39 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
| `→a` | 38 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/48 |
| `.→` | 38 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/121 |
| `→t` | 38 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/65 |
| `é→e` | 37 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56 |
| `→(` | 37 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
| `→𝔹:` | 36 | SP02_CW_10+12 B10-03/51, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66 |
| `→r` | 35 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/44 |
| `→Cr` | 35 | SP02_CW_10+12 B10-07/104, SP04_CW_156-4+156-6 J156-4-06/46, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→tw` | 34 | SP02_CW_10+12 B10-04/67, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/75 |
| `→guidedrawn` | 34 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `rl→ta` | 34 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `o→` | 32 | SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72 |
| `→)` | 32 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/134 |
| `→f` | 32 | SP02_CW_10+12 B10-07/108, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-10/131 |
| `und→Cr` | 31 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `→,` | 30 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-05/75 |
| `→Cretaine` | 30 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-01/7 |
| `→deleted` | 29 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/119 |
| `→C` | 28 | SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/75 |
| `tt→d` | 28 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `→unsure` | 28 | SP04_CW_156-4+156-6 J156-4-01/6, SP04_CW_156-4+156-6 J156-4-01/8, SP04_CW_156-4+156-6 J156-4-02/10 |
| `a→` | 27 | SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/75 |
| `→ed` | 27 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/77 |
| `co→` | 27 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `→sh` | 26 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-04/64 |
| `m→spag` | 26 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `→,canceled` | 26 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
| `→_:` | 26 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/129, SP02_CW_10+12 B12-01/69 |
| `→Cret` | 25 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→-` | 24 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47 |
| `t→` | 24 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-08/122 |
| `del→Cr` | 24 | SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→o` | 23 | SP02_CW_10+12 B10-01/41, SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-03/51 |
| `→,deleted` | 23 | SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `a→.` | 23 | SP02_CW_10+12 B10-09/123, SP04_CW_156-4+156-6 J156-4-07/56, SP12_CW_45+46+53+57+63 J53-01/4 |
| `?→` | 23 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `→;` | 22 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-04/25, SP14_CW_13+15+26+35+48+66+97+123+162 J13-03/31 |
| `à→:` | 21 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `ag→` | 20 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| `→Cre` | 19 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `m→` | 18 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/87 |
| `→,cancelled` | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/80 |
| `n→` | 18 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/107, SP02_CW_10+12 B10-08/118 |
| `mitt→ngcurv` | 17 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `i→` | 17 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-05/75 |
| `→;tikzpicture` | 17 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/98 |
| `→u` | 16 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-05/70 |
| `uncertain→` | 16 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77 |
| `→p` | 15 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-06/82, SP02_CW_10+12 B10-06/87 |
| `→c` | 15 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/115 |
| `x→` | 15 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `,→` | 15 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-02/9 |
| `→overlap` | 15 | SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79, SP02_CW_10+12 B10-06/81 |
| `om→gu` | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
| `→h` | 14 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/68 |
| `→ained` | 14 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
| `c→` | 14 | SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B12-01/98, SP12_CW_45+46+53+57+63 J53-01/5 |
| `→tai` | 14 | SP04_CW_156-4+156-6 J156-4-05/41, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-02/10 |
| `→tained` | 14 | SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/8 |
| `s→d` | 14 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `u→Cretai` | 14 | SP12_CW_45+46+53+57+63 J53-01/8, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `r→v` | 14 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `u→` | 13 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-06/83, SP02_CW_10+12 B12-01/69 |
| `→'` | 13 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `→e/` | 13 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78 |
| `→inserted` | 13 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-05/34 |
| `,→;` | 12 | SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/60 |
| `m→n` | 12 | SP02_CW_10+12 B10-05/72, SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6 |
| `unsu→` | 12 | SP02_CW_10+12 B10-09/127, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/3 |
| `ef→` | 12 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `no→Cretai` | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| `⊗→` | 11 | SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126 |
| `→|` | 11 | SP02_CW_10+12 B10-05/75, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19, SP35_CW_156-7 H156-01/4 |
| `l→` | 11 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/26 |
| `→cancelled` | 11 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105 |
| `→cal` | 11 | SP02_CW_10+12 B10-07/108, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/10 |
| `a→e` | 11 | SP04_CW_156-4+156-6 J156-4-04/26, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `o→Cretained` | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| `righ→labela` | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| `-sid→l` | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| `→x` | 11 | SP12_CW_45+46+53+57+63 A57-01/13, SP44_CW_36 A36-01/13, SP44_CW_36 A36-01/13 |
| `→w` | 10 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-04/68, SP04_CW_156-4+156-6 J156-4-06/47 |
| `→TikZl` | 10 | SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/46 |
| `om→T` | 10 | SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/48 |
| `→bracketinTikZ` | 10 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `h→` | 10 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/72, SP31_CW_156-3 J156-3-03/25 |
| `mi→r` | 10 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/106 |
| `calligraphic→𝒞:` | 10 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| `→eta` | 10 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/11 |
| `l→Cr` | 10 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/10 |
| `o→Cretai` | 10 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/10 |
| `v→n` | 10 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/14 |
| `t→ach` | 10 | SP12_CW_45+46+53+57+63 J53-05/33, SP12_CW_45+46+53+57+63 A57-01/6, SP12_CW_45+46+53+57+63 A57-01/7 |
| `→ra` | 10 | SP12_CW_45+46+53+57+63 A57-01/13, SP12_CW_45+46+53+57+63 A57-02/20, SP14_CW_13+15+26+35+48+66+97+123+162 H66-01/2 |
| `-→` | 9 | SP02_CW_10+12 B10-03/55, SP12_CW_45+46+53+57+63 J53-03/22, SP35_CW_156-7 H156-01/7 |
| `t→rok` | 9 | SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B10-07/103 |
| `→ne` | 9 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/11 |
| `→overlapqualified` | 9 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76 |
| `→wi` | 9 | SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133 |
| `→le` | 9 | SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/13 |
| `+→` | 9 | SP02_CW_10+12 B10-10/131, SP41_CW_81 J81-05/35, SP41_CW_81 J81-05/37 |
| `ou→` | 9 | SP04_CW_156-4+156-6 J156-4-02/15, SP04_CW_156-4+156-6 J156-4-02/15, SP12_CW_45+46+53+57+63 J53-01/8 |
| `r→n` | 9 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-03/22 |
| `→ned` | 9 | SP12_CW_45+46+53+57+63 J53-02/13, SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22 |
| `→Cretai` | 9 | SP12_CW_45+46+53+57+63 J53-04/23, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26 |
| `inline→a` | 9 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9, SP12_CW_45+46+53+57+63 A57-01/9 |
| `→uncertain` | 9 | SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/48 |
| `→C's` | 9 | SP31_CW_156-3 J156-3-02/13, SP31_CW_156-3 J156-3-02/15, SP31_CW_156-3 J156-3-02/16 |
| `→|S` | 8 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/44 |
| `→TikZ` | 8 | SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-03/52 |
| `t→curv` | 8 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-07/106 |
| `→gh` | 8 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-09/127 |
| `only→` | 8 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| `→qualified` | 8 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/79 |
| `→and` | 8 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/76, SP12_CW_45+46+53+57+63 A57-02/21 |
| `→tyretained` | 8 | SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/83, SP02_CW_10+12 B10-06/84 |
| `mit→la` | 8 | SP02_CW_10+12 B10-06/86, SP02_CW_10+12 B10-07/103, SP12_CW_45+46+53+57+63 J53-04/28 |
| `mitt→calcurv` | 8 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-08/120 |
| `]→` | 8 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/40, SP04_CW_156-4+156-6 J156-4-06/42 |
| `→at` | 8 | SP04_CW_156-4+156-6 J156-4-06/49, SP35_CW_156-7 H156-01/5, SP45_CW_37 B37-02/23 |
| `p→C` | 8 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/14 |
| `f→` | 8 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/10 |
| `|→` | 8 | SP12_CW_45+46+53+57+63 J53-01/6, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/17, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `l→Creta` | 8 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/14 |
| `p→` | 8 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/24, SP12_CW_45+46+53+57+63 J53-04/28 |
| `c→Cret` | 8 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/15, SP12_CW_45+46+53+57+63 J53-03/16 |
| `→ined` | 8 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/15, SP12_CW_45+46+53+57+63 J53-03/22 |
| `𝒞→𝔹` | 8 | SP12_CW_45+46+53+57+63 J53-05/33, SP12_CW_45+46+53+57+63 J53-05/34, SP12_CW_45+46+53+57+63 J53-05/34 |
| `-si→ype` | 8 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |

## Content changes: word-level (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
|  → Cretained | 28 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12 |
|  → deleted | 24 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18 |
| commentonly → mspage | 23 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
|  → canceled | 21 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-09/123 |
| omitted → curvedguidedrawn | 20 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76 |
|  → cancelled | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-06/80 |
|  → retained | 15 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/106 |
| omitted → guidedrawn | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
| none → Cretained | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
|  → S | 11 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/43 |
| o → Cretained | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| right sidetag → labelatleft | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
|  → o | 10 | SP02_CW_10+12 B10-02/45, SP04_CW_156-4+156-6 J156-4-05/41, SP44_CW_36 A36-01/11 |
| à →  | 10 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-08/58 |
| omitted →  | 9 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-10/131 |
|  → M | 9 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
|  → F | 9 | SP02_CW_10+12 B10-05/71, SP04_CW_156-4+156-6 J156-4-01/3, SP04_CW_156-4+156-6 J156-4-06/48 |
|  → G | 9 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/128 |
| L → calL | 9 | SP04_CW_156-4+156-6 J156-4-05/41, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/11 |
| G →  | 9 | SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9 |
|  → i | 8 | SP02_CW_10+12 B10-04/63, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
|  → C | 8 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/125, SP02_CW_10+12 B10-10/133 |
| calligraphicP → P | 8 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| k → Cretained | 8 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/12 |
| right sidetag → typed atleft | 8 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| j → J | 8 | SP51_CW_134-2 H134-05/175, SP51_CW_134-2 H134-05/176, SP51_CW_134-2 H134-05/176 |
| X →  | 7 | SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-03/19 |
| de → Cretained | 7 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
| stable → st bl | 7 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29 |
| π → Π | 7 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| underlinedO → Cretained | 7 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/7, SP12_CW_45+46+53+57+63 A57-01/7 |
|  → Noterminalcomma | 7 | SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6 |
| n → f | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| n → u | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| omitted → curvedinsertionbracketinTikZ | 6 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| omitted → longcurvedbracketinTikZ | 6 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/63 |
|  → e | 6 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| omitted → mspage | 6 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73 |
| sss → Cretained | 6 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-05/29 |
| X o → Cretained | 6 | SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/13 |
| omitted → ngExtraStro | 6 | SP31_CW_156-3 J156-3-02/11, SP31_CW_156-3 J156-3-02/15, SP31_CW_156-3 J156-3-02/17 |
|  → controls and | 6 | SP36_CW_71 J71-01/6, SP46_CW_37 B37-04/74, SP52_CW_156-4+156-6 J156-4-09/71 |
| absent →  | 5 | SP02_CW_10+12 B10-03/57, SP41_CW_81 J81-05/37, SP41_CW_81 J81-05/37 |
| omitted → curvedinsertionguidedrawn | 5 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| otimes →  | 5 | SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-08/117 |
| mu → muusingfirstqualifiedcandidate | 5 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118 |
| omitted → localcurvedguidedrawn | 5 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
|  → X | 5 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/127 |
|  → A | 5 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/127 |
| unsureà colon →  | 5 | SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/11 |
| F →  | 5 | SP04_CW_156-4+156-6 J156-4-07/53, SP04_CW_156-4+156-6 J156-4-07/57, SP35_CW_156-7 H156-01/5 |
|  → P | 5 | SP04_CW_156-4+156-6 J156-4-07/54, SP14_CW_13+15+26+35+48+66+97+123+162 H48-01/5, SP31_CW_156-3 J156-3-01/2 |
| g → Cretained | 5 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/25, SP12_CW_45+46+53+57+63 J53-04/28 |
| ext → Cretained | 5 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/13, SP12_CW_45+46+53+57+63 J53-02/13 |
| underlinedO X → Cretained | 5 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
|  → Z | 5 | SP38_CW_75 J75-01/8, SP38_CW_75 J75-01/9, SP38_CW_75 J75-02/13 |
| notrepresented →  | 5 | SP47_CW_103 H103-02/13, SP47_CW_103 H103-02/13, SP47_CW_103 H103-02/14 |
| Omitted → TikZapproximationinanuncertaintywrapper nocompletedtextualreading | 5 | SP47_CW_103 H103-02/14, SP47_CW_103 H103-02/14, SP47_CW_103 H103-02/14 |
|  → headless | 5 | SP48_CW_104 H104-01/5, SP48_CW_104 H104-01/5, SP48_CW_104 H104-01/5 |
| n → top | 5 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| a →  | 4 | SP02_CW_10+12 B10-03/57, SP31_CW_156-3 J156-3-03/25, SP32_CW_156-3 J156-3-05/39 |
| omitted → curvedattachmentinTikZ | 4 | SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61 |
| omitted → curvedbracketinTikZ | 4 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/67 |
| sigma → σσ σ | 4 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/69, SP02_CW_10+12 B10-05/70 |
|  → comma | 4 | SP02_CW_10+12 B10-05/70, SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/11, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/47 |
| omitted → curvedlocalinsertionguide | 4 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/121 |
|  → u | 4 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/128, SP48_CW_104 H104-01/5 |
|  → a | 4 | SP02_CW_10+12 B10-09/127, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19 |
|  → j | 4 | SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| S →  | 4 | SP04_CW_156-4+156-6 J156-4-03/24, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/5, SP44_CW_36 A36-01/14 |
| la → le | 4 | SP04_CW_156-4+156-6 J156-4-04/26, SP37_CW_71 J71-05/36, SP51_CW_134-2 H134-06/183 |
| X k → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/13 |
| G → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/32 |
| donc → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-04/27, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/31 |
| s → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/6 |
| comma → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/32, SP12_CW_45+46+53+57+63 A57-01/6 |
| lettero → Cretained | 4 | SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/3 |
| underlinedO U → Cretained | 4 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| omitted → raStrongExtra | 4 | SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/12, SP31_CW_156-3 J156-3-03/18 |
| i →  | 4 | SP39_CW_75 J75-04/28, SP44_CW_36 A36-01/14, SP45_CW_37 B37-02/25 |
|  → Noterminalsemicolon | 4 | SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6 |
| n → bottom | 4 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
|  → H | 3 | SP02_CW_10+12 B10-02/42, SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/23, SP48_CW_104 H104-01/8 |
| omitted → TikZangularlowerbracketanddiagonalinsertionstroke | 3 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
|  → m | 3 | SP02_CW_10+12 B10-03/55, SP35_CW_156-7 H156-01/4, SP51_CW_134-2 H134-05/176 |
| omitted → curvedinsertionhookinTikZ | 3 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| à → a | 3 | SP02_CW_10+12 B10-04/63, SP47_CW_103 H103-01/9, SP51_CW_134-2 H134-06/180 |
|  → x | 3 | SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-10/132, SP02_CW_10+12 B12-01/97 |
| cancelleduncertainprime → cancelleduncertainprimeretained | 3 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/73 |
| omitted → longcurvedguidedrawn | 3 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/127 |
| omitted → longbentguidedrawn | 3 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76 |
| uncertains → uncertainsretained | 3 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76 |
|  → comma point | 3 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/79 |
| omitted → tracedrawnwithoutinterpretation | 3 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105 |
| μ → μretained | 3 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/120, SP02_CW_10+12 B10-08/121 |
| x → xretained | 3 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/120, SP02_CW_10+12 B10-08/120 |
| ou →  | 3 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118, SP04_CW_156-4+156-6 J156-4-03/24 |
| comment → mspage | 3 | SP02_CW_10+12 B10-08/120, SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/122 |
|  → inserted | 3 | SP02_CW_10+12 B10-09/125, SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-07/51 |
| qualifiedsigma → sigma canceled | 3 | SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126 |
| qualifiedsigma → sigma | 3 | SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126 |
|  → tikzpicture | 3 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-02/123, SP57_CW_97+123+162-1+162-6 C123-02/23 |
| D →  | 3 | SP04_CW_156-4+156-6 J156-4-01/2, SP04_CW_156-4+156-6 J156-4-01/3, SP57_CW_97+123+162-1+162-6 C123-01/3 |
| unsure →  | 3 | SP04_CW_156-4+156-6 J156-4-01/6, SP12_CW_45+46+53+57+63 J53-02/10, SP33_CW_156-5 J156-5-01/8 |
| unsurescriptF F → scriptF | 3 | SP04_CW_156-4+156-6 J156-4-02/12, SP04_CW_156-4+156-6 J156-4-02/13, SP04_CW_156-4+156-6 J156-4-02/16 |
| G → C | 3 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP35_CW_156-7 H156-01/6 |
| x →  | 3 | SP04_CW_156-4+156-6 J156-4-06/44, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/41, SP57_CW_97+123+162-1+162-6 C123-01/16 |
| omitted → tworulesinTikZ | 3 | SP04_CW_156-4+156-6 J156-4-07/50, SP04_CW_156-4+156-6 J156-4-07/50, SP04_CW_156-4+156-6 J156-4-07/50 |
| singleunderline → doubleunderline | 3 | SP04_CW_156-4+156-6 J156-4-08/58, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/3 |
| sur → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/31 |
| géom → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-01/8, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/14 |
| red → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/14, SP12_CW_45+46+53+57+63 J53-02/14 |
| qu cpct → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/15 |
| schém → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/15 |
| insertedk → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/13 |
|  → k | 3 | SP12_CW_45+46+53+57+63 J53-02/13, SP34_CW_156-5 J156-5-04/33, SP34_CW_156-5 J156-5-04/33 |
| et → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-02/14, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/31 |
| underlinedNB → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26 |
| circled prime → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-04/24, SP12_CW_45+46+53+57+63 J53-04/25, SP12_CW_45+46+53+57+63 J53-04/26 |
| y λ → Cretained | 3 | SP12_CW_45+46+53+57+63 J53-04/25, SP12_CW_45+46+53+57+63 J53-04/25, SP12_CW_45+46+53+57+63 J53-04/25 |
