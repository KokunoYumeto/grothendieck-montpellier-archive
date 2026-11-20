# What the second passes changed in our first readings

9880 changes in 45 collation tables (`SP_CHANGES.tsv`, one row each).

| class | changes |
|---|---|
| content | 7575 |
| doubt only | 2011 |
| markup only | 121 |
| inserted/placed | 92 |
| struck/live | 65 |
| ill resolved | 16 |

## By the run's own kind

| kind | content | doubt only | markup only | inserted/placed | struck/live | ill resolved |
|---|---|---|---|---|---|---|
| misread symbol or index | 1395 | 366 | 35 | 18 | 1 | 0 |
| omission | 1131 | 391 | 22 | 9 | 32 | 1 |
| misread word | 959 | 452 | 5 | 19 | 6 | 1 |
| drawing or diagram | 1305 | 10 | 6 | 2 | 0 | 2 |
| readable ink left as \ill{} | 648 | 319 | 8 | 5 | 12 | 8 |
| insertion or placement | 626 | 36 | 9 | 15 | 1 | 1 |
| abbreviation expanded or spelling modernised | 373 | 193 | 3 | 5 | 0 | 0 |
| other | 381 | 114 | 20 | 10 | 1 | 1 |
| deletion state (struck given live or live given struck) | 413 | 79 | 3 | 5 | 6 | 2 |
| text not on the page | 195 | 16 | 4 | 1 | 0 | 0 |
| deletion state | 149 | 35 | 6 | 3 | 6 | 0 |

## Where nobody doubted

Content changes at places witness C had not marked: 5038 of 7575. Of these, witness H had the same reading as C and no doubt mark either: 1528 (both witnesses wrong the same way, nobody doubting; rows with `c_equals_h` = yes, `c_marked` = no, `h_marked` = no in SP_CHANGES.tsv).

| kind | C unmarked | C and H agree, both unmarked |
|---|---|---|
| drawing or diagram | 1205 | 581 |
| misread symbol or index | 886 | 262 |
| omission | 697 | 253 |
| misread word | 533 | 154 |
| insertion or placement | 496 | 69 |
| other | 287 | 109 |
| readable ink left as \ill{} | 277 | 0 |
| abbreviation expanded or spelling modernised | 210 | 45 |
| deletion state (struck given live or live given struck) | 190 | 26 |
| text not on the page | 169 | 11 |
| deletion state | 88 | 18 |

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
| `unsure→` | 218 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| `[→` | 114 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→retained` | 113 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/73 |
| `→d` | 110 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| `→l` | 92 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `→e` | 89 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-04/67 |
| `doubtful→` | 87 | SP31_CW_156-3 J156-3-03/22, SP58_CW_156-5 J156-5-06/42, SP58_CW_156-5 J156-5-06/42 |
| `omitt→curv` | 78 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| `→n` | 77 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/68 |
| `s→` | 65 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127 |
| `→_:` | 64 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/129, SP02_CW_10+12 B12-01/69 |
| `?]→` | 62 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→ain` | 61 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10 |
| `e→` | 58 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/67 |
| `→.` | 57 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-05/74 |
| `→rawn` | 57 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `→𝒞:` | 54 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `→s` | 53 | SP02_CW_10+12 B10-01/33, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-04/61 |
| `→unsure` | 50 | SP04_CW_156-4+156-6 J156-4-01/6, SP04_CW_156-4+156-6 J156-4-01/8, SP04_CW_156-4+156-6 J156-4-02/10 |
| `.→` | 49 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/121 |
| `→(` | 48 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
| `d→` | 47 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
| `→i` | 46 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `sert→` | 45 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→)` | 45 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/134 |
| `→Creta` | 45 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→a` | 44 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/48 |
| `é→e` | 43 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56 |
| `r→` | 43 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `→t` | 42 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/65 |
| `→tw` | 41 | SP02_CW_10+12 B10-04/67, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/75 |
| `→𝔹:` | 39 | SP02_CW_10+12 B10-03/51, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66 |
| `→r` | 38 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/44 |
| `→,` | 38 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-05/75 |
| `→deleted` | 37 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/119 |
| `o→` | 35 | SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72 |
| `→Cr` | 35 | SP02_CW_10+12 B10-07/104, SP04_CW_156-4+156-6 J156-4-06/46, SP12_CW_45+46+53+57+63 J53-01/6 |
| `rl→ta` | 35 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `→guidedrawn` | 34 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `?→` | 34 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `→f` | 33 | SP02_CW_10+12 B10-07/108, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-10/131 |
| `und→Cr` | 31 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `→sh` | 30 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-04/64 |
| `→C` | 30 | SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/75 |
| `→Cretaine` | 30 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-01/7 |
| `a→` | 29 | SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/75 |
| `t→` | 29 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-08/122 |
| `tt→d` | 28 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `→-` | 27 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47 |
| `→ed` | 27 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/77 |
| `co→` | 27 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `m→spag` | 26 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `→,canceled` | 26 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
| `à→:` | 26 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `→o` | 25 | SP02_CW_10+12 B10-01/41, SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-03/51 |
| `→Cret` | 25 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `del→Cr` | 24 | SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→,deleted` | 24 | SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `a→.` | 24 | SP02_CW_10+12 B10-09/123, SP04_CW_156-4+156-6 J156-4-07/56, SP12_CW_45+46+53+57+63 J53-01/4 |
| `→;` | 23 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-04/25, SP14_CW_13+15+26+35+48+66+97+123+162 J13-03/31 |
| `m→` | 22 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/87 |
| `→'` | 21 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `,→` | 21 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-02/9 |
| `n→` | 21 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/107, SP02_CW_10+12 B10-08/118 |
| `→u` | 20 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-05/70 |
| `ag→` | 20 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| `i→` | 19 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-05/75 |
| `→Cre` | 19 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `→,cancelled` | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/80 |
| `mitt→ngcurv` | 18 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `uncertain→` | 18 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77 |
| `→inserted` | 18 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-05/34 |
| `→c` | 17 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/115 |
| `→;tikzpicture` | 17 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/98 |
| `u→` | 16 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-06/83, SP02_CW_10+12 B12-01/69 |
| `→h` | 16 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/68 |
| `x→` | 16 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `→p` | 15 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-06/82, SP02_CW_10+12 B10-06/87 |
| `→overlap` | 15 | SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79, SP02_CW_10+12 B10-06/81 |
| `c→` | 15 | SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B12-01/98, SP12_CW_45+46+53+57+63 J53-01/5 |
| `→cancelled` | 15 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105 |
| `om→gu` | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
| `]→` | 15 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/40, SP04_CW_156-4+156-6 J156-4-06/42 |
| `r→v` | 15 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `ξ→ζ` | 15 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
| `→ained` | 14 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
| `l→` | 14 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/26 |
| `→tai` | 14 | SP04_CW_156-4+156-6 J156-4-05/41, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-02/10 |
| `→tained` | 14 | SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/8 |
| `s→d` | 14 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `u→Cretai` | 14 | SP12_CW_45+46+53+57+63 J53-01/8, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `→doubtful` | 14 | SP58_CW_156-5 J156-5-06/42, SP59_CW_71 J71-01/10, SP59_CW_71 J71-02/17 |
| `,→;` | 13 | SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/60 |
| `m→n` | 13 | SP02_CW_10+12 B10-05/72, SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→e/` | 13 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78 |
| `ef→` | 13 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `→,doubtful` | 13 | SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/36, SP58_CW_156-5 J156-5-05/36 |
| `→w` | 12 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-04/68, SP04_CW_156-4+156-6 J156-4-06/47 |
| `-→` | 12 | SP02_CW_10+12 B10-03/55, SP12_CW_45+46+53+57+63 J53-03/22, SP35_CW_156-7 H156-01/7 |
| `h→` | 12 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/72, SP31_CW_156-3 J156-3-03/25 |
| `mi→r` | 12 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/106 |
| `→ne` | 12 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/11 |
| `→underlined` | 12 | SP02_CW_10+12 B10-06/77, SP04_CW_156-4+156-6 J156-4-05/35, SP04_CW_156-4+156-6 J156-4-05/36 |
| `unsu→` | 12 | SP02_CW_10+12 B10-09/127, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/3 |
| `a→e` | 12 | SP04_CW_156-4+156-6 J156-4-04/26, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `(→` | 12 | SP12_CW_45+46+53+57+63 J53-04/23, SP12_CW_45+46+53+57+63 A57-01/6, SP38_CW_75 J75-02/12 |
| `no→Cretai` | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| `⊗→` | 11 | SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-09/126, SP02_CW_10+12 B10-09/126 |
| `→|` | 11 | SP02_CW_10+12 B10-05/75, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19, SP35_CW_156-7 H156-01/4 |
| `→cal` | 11 | SP02_CW_10+12 B10-07/108, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/10 |
| `→le` | 11 | SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/13 |
| `ou→` | 11 | SP04_CW_156-4+156-6 J156-4-02/15, SP04_CW_156-4+156-6 J156-4-02/15, SP12_CW_45+46+53+57+63 J53-01/8 |
| `o→Cretained` | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| `-sid→l` | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| `righ→labela` | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| `→x` | 11 | SP12_CW_45+46+53+57+63 A57-01/13, SP44_CW_36 A36-01/13, SP44_CW_36 A36-01/13 |
| `′→'` | 11 | SP34_CW_156-5 J156-5-04/28, SP34_CW_156-5 J156-5-04/28, SP35_CW_156-7 H156-01/6 |
| `→TikZl` | 10 | SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/46 |
| `om→T` | 10 | SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/48 |
| `→bracketinTikZ` | 10 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `t→rok` | 10 | SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B10-07/103 |
| `)→` | 10 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/132, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40 |
| `+→` | 10 | SP02_CW_10+12 B10-10/131, SP41_CW_81 J81-05/35, SP41_CW_81 J81-05/37 |
| `calligraphic→𝒞:` | 10 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| `𝒞:→` | 10 | SP04_CW_156-4+156-6 J156-4-07/55, SP31_CW_156-3 J156-3-01/3, SP51_CW_134-2 H134-06/180 |
| `→inTikZ` | 10 | SP04_CW_156-4+156-6 J156-4-08/64, SP32_CW_156-3 J156-3-04/33, SP37_CW_71 J71-05/36 |
| `→eta` | 10 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/11 |
| `l→Cr` | 10 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/10 |
| `o→Cretai` | 10 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/10 |
| `v→n` | 10 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/14 |
| `t→ach` | 10 | SP12_CW_45+46+53+57+63 J53-05/33, SP12_CW_45+46+53+57+63 A57-01/6, SP12_CW_45+46+53+57+63 A57-01/7 |
| `→uncertain` | 10 | SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/48 |
| `→ra` | 10 | SP12_CW_45+46+53+57+63 A57-01/13, SP12_CW_45+46+53+57+63 A57-02/20, SP14_CW_13+15+26+35+48+66+97+123+162 H66-01/2 |
| `^→` | 10 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40, SP32_CW_156-3 J156-3-05/38, SP32_CW_156-3 J156-3-05/38 |
| `cabl→tt` | 10 | SP70_C13_142 142/29, SP70_C13_142 142/29, SP70_C13_142 142/29 |
| `appl→wr` | 10 | SP70_C13_142 142/29, SP70_C13_142 142/29, SP70_C13_142 142/29 |
| `→tentative` | 10 | SP71_C13_142 142/55, SP71_C13_142 142/56, SP71_C13_142 142/56 |
| `→gh` | 9 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-09/127 |
| `→plain` | 9 | SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-09/125 |
| `→overlapqualified` | 9 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76 |
| `→wi` | 9 | SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133 |
| `→m` | 9 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/130 |
| `→et` | 9 | SP02_CW_10+12 B10-09/125, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/12 |
| `→b` | 9 | SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-01/6, SP14_CW_13+15+26+35+48+66+97+123+162 B15-01/82 |
| `e→a` | 9 | SP02_CW_10+12 B12-02/123, SP04_CW_156-4+156-6 J156-4-08/64, SP12_CW_45+46+53+57+63 J53-02/12 |
| `f→` | 9 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/10 |
| `|→` | 9 | SP12_CW_45+46+53+57+63 J53-01/6, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/17, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `p→` | 9 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/24, SP12_CW_45+46+53+57+63 J53-04/28 |
| `r→n` | 9 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-03/22 |
| `→ned` | 9 | SP12_CW_45+46+53+57+63 J53-02/13, SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22 |

## Content changes: word-level (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
|  → Cretained | 28 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12 |
|  → deleted | 24 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18 |
| commentonly → mspage | 23 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
|  → canceled | 21 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-09/123 |
| omitted → curvedguidedrawn | 20 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76 |
|  → cancelled | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-06/80 |
| ξ → ζ | 18 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
|  → retained | 16 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/106 |
|  → doubtful | 16 | SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/36 |
| omitted → guidedrawn | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
| none → Cretained | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
|  → S | 11 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/43 |
| omitted →  | 11 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-10/131 |
| X →  | 11 | SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-03/19 |
| à →  | 11 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-08/58 |
| o → Cretained | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| right sidetag → labelatleft | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
|  → o | 10 | SP02_CW_10+12 B10-02/45, SP04_CW_156-4+156-6 J156-4-05/41, SP44_CW_36 A36-01/11 |
|  → F | 10 | SP02_CW_10+12 B10-05/71, SP04_CW_156-4+156-6 J156-4-01/3, SP04_CW_156-4+156-6 J156-4-06/48 |
|  → G | 10 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/128 |
| G →  | 10 | SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9 |
| asapplicable → aswritten | 10 | SP70_C13_142 142/29, SP70_C13_142 142/29, SP70_C13_142 142/29 |
|  → M | 9 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
|  → C | 9 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/125, SP02_CW_10+12 B10-10/133 |
| L → calL | 9 | SP04_CW_156-4+156-6 J156-4-05/41, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/11 |
|  → i | 8 | SP02_CW_10+12 B10-04/63, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| calligraphicP → P | 8 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| k → Cretained | 8 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/12 |
| right sidetag → typed atleft | 8 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| n →  | 8 | SP48_CW_104 H104-01/5, SP60_CW_71 J71-06/47, SP65_C13_16 16/20 |
| j → J | 8 | SP51_CW_134-2 H134-05/175, SP51_CW_134-2 H134-05/176, SP51_CW_134-2 H134-05/176 |
| unsure →  | 7 | SP04_CW_156-4+156-6 J156-4-01/6, SP12_CW_45+46+53+57+63 J53-02/10, SP33_CW_156-5 J156-5-01/8 |
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
|  → X | 6 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/127 |
| S →  | 6 | SP04_CW_156-4+156-6 J156-4-03/24, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/5, SP44_CW_36 A36-01/14 |
| x →  | 6 | SP04_CW_156-4+156-6 J156-4-06/44, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/41, SP57_CW_97+123+162-1+162-6 C123-01/16 |
| sss → Cretained | 6 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-05/29 |
| X o → Cretained | 6 | SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/13 |
| omitted → ngExtraStro | 6 | SP31_CW_156-3 J156-3-02/11, SP31_CW_156-3 J156-3-02/15, SP31_CW_156-3 J156-3-02/17 |
|  → controls and | 6 | SP36_CW_71 J71-01/6, SP46_CW_37 B37-04/74, SP52_CW_156-4+156-6 J156-4-09/71 |
| i →  | 6 | SP39_CW_75 J75-04/28, SP44_CW_36 A36-01/14, SP45_CW_37 B37-02/25 |
| doubtful →  | 6 | SP58_CW_156-5 J156-5-05/37, SP58_CW_156-5 J156-5-05/39, SP58_CW_156-5 J156-5-06/42 |
| doubtfulbold plainGamma → boldGamma | 6 | SP71_C13_142 142/69, SP71_C13_142 142/69, SP71_C13_142 142/69 |
| absent →  | 5 | SP02_CW_10+12 B10-03/57, SP41_CW_81 J81-05/37, SP41_CW_81 J81-05/37 |
| omitted → curvedinsertionguidedrawn | 5 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| otimes →  | 5 | SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-08/117 |
| mu → muusingfirstqualifiedcandidate | 5 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118 |
| omitted → localcurvedguidedrawn | 5 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
|  → A | 5 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/127 |
| unsureà colon →  | 5 | SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/11 |
| la → le | 5 | SP04_CW_156-4+156-6 J156-4-04/26, SP37_CW_71 J71-05/36, SP51_CW_134-2 H134-06/183 |
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
| Q →  | 4 | SP02_CW_10+12 B12-02/102, SP44_CW_36 A36-01/14, SP69_C13_141+142 142/17 |
|  → j | 4 | SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| G → C | 4 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP35_CW_156-7 H156-01/6 |
| singleunderline → doubleunderline | 4 | SP04_CW_156-4+156-6 J156-4-08/58, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/3 |
| X k → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/13 |
| G → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/32 |
| donc → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-04/27, SP12_CW_45+46+53+57+63 J53-05/31, SP12_CW_45+46+53+57+63 J53-05/31 |
| s → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/6 |
| comma → Cretained | 4 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/32, SP12_CW_45+46+53+57+63 A57-01/6 |
| lettero → Cretained | 4 | SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/3, SP12_CW_45+46+53+57+63 A57-01/3 |
| underlinedO U → Cretained | 4 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| omitted → raStrongExtra | 4 | SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/12, SP31_CW_156-3 J156-3-03/18 |
|  → underlined | 4 | SP35_CW_156-7 H156-01/8, SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9 |
|  → Noterminalsemicolon | 4 | SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6 |
| n → bottom | 4 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| doubtful → deleted | 4 | SP64_C13_15+16 15/191, SP64_C13_15+16 15/191, SP64_C13_15+16 15/193 |
| ωi → ω'i | 4 | SP70_C13_142 142/26, SP70_C13_142 142/26, SP70_C13_142 142/26 |
| standard → standart | 4 | SP71_C13_142 142/59, SP71_C13_142 142/59, SP71_C13_142 142/61 |
|  → B | 3 | SP02_CW_10+12 B10-01/41, SP48_CW_104 H104-01/4, SP66_C13_16+120+136 120/6 |
|  → H | 3 | SP02_CW_10+12 B10-02/42, SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/23, SP48_CW_104 H104-01/8 |
| omitted → TikZangularlowerbracketanddiagonalinsertionstroke | 3 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
|  → m | 3 | SP02_CW_10+12 B10-03/55, SP35_CW_156-7 H156-01/4, SP51_CW_134-2 H134-05/176 |
| omitted → curvedinsertionhookinTikZ | 3 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| à → a | 3 | SP02_CW_10+12 B10-04/63, SP47_CW_103 H103-01/9, SP51_CW_134-2 H134-06/180 |
| r →  | 3 | SP02_CW_10+12 B10-04/64, SP43_CW_29+32 C29-04/38, SP71_C13_142 142/63 |
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
| A →  | 3 | SP02_CW_10+12 B10-10/135, SP43_CW_29+32 C29-04/83, SP62_CW_162-1+162-6 H162-02/4 |
|  → tikzpicture | 3 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-02/123, SP57_CW_97+123+162-1+162-6 C123-02/23 |
