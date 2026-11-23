# What the second passes changed in our first readings

19483 changes in 84 collation tables (`SP_CHANGES.tsv`, one row each).

| class | changes |
|---|---|
| content | 14059 |
| doubt only | 4485 |
| markup only | 449 |
| inserted/placed | 265 |
| struck/live | 158 |
| ill resolved | 67 |

## By the run's own kind

| kind | content | doubt only | markup only | inserted/placed | struck/live | ill resolved |
|---|---|---|---|---|---|---|
| misread symbol or index | 2947 | 913 | 79 | 32 | 8 | 2 |
| omission | 2157 | 749 | 139 | 26 | 47 | 4 |
| misread word | 1697 | 1090 | 26 | 29 | 11 | 2 |
| drawing or diagram | 2257 | 22 | 11 | 4 | 0 | 4 |
| readable ink left as \ill{} | 910 | 701 | 33 | 7 | 28 | 42 |
| insertion or placement | 1081 | 135 | 44 | 122 | 5 | 2 |
| abbreviation expanded or spelling modernised | 753 | 334 | 17 | 7 | 0 | 1 |
| other | 662 | 202 | 59 | 21 | 2 | 1 |
| deletion state (struck given live or live given struck) | 635 | 137 | 9 | 11 | 32 | 2 |
| text not on the page | 618 | 77 | 18 | 1 | 1 | 4 |
| deletion state | 320 | 125 | 14 | 5 | 24 | 2 |
| literal ink correction | 10 | 0 | 0 | 0 | 0 | 0 |
| punctuation or continuation mark | 3 | 0 | 0 | 0 | 0 | 0 |
| punctuation omission | 2 | 0 | 0 | 0 | 0 | 0 |
| literal punctuation correction | 2 | 0 | 0 | 0 | 0 | 0 |
| independent reading correction | 1 | 0 | 0 | 0 | 0 | 1 |
| diagram or graphic sign | 1 | 0 | 0 | 0 | 0 | 0 |
| supplied indices | 1 | 0 | 0 | 0 | 0 | 0 |
| misread words | 1 | 0 | 0 | 0 | 0 | 0 |
| punctuation | 1 | 0 | 0 | 0 | 0 | 0 |

## Where nobody doubted

Content changes at places witness C had not marked: 9404 of 14059. Of these, witness H had the same reading as C and no doubt mark either: 3241 (both witnesses wrong the same way, nobody doubting; rows with `c_equals_h` = yes, `c_marked` = no, `h_marked` = no in SP_CHANGES.tsv).

| kind | C unmarked | C and H agree, both unmarked |
|---|---|---|
| drawing or diagram | 2026 | 792 |
| misread symbol or index | 1912 | 826 |
| omission | 1381 | 590 |
| misread word | 912 | 268 |
| insertion or placement | 819 | 113 |
| other | 520 | 200 |
| text not on the page | 513 | 146 |
| abbreviation expanded or spelling modernised | 509 | 210 |
| readable ink left as \ill{} | 374 | 0 |
| deletion state (struck given live or live given struck) | 262 | 50 |
| deletion state | 155 | 34 |
| literal ink correction | 10 | 8 |
| punctuation or continuation mark | 3 | 3 |
| punctuation omission | 2 | 0 |
| literal punctuation correction | 2 | 0 |
| diagram or graphic sign | 1 | 0 |
| supplied indices | 1 | 1 |
| independent reading correction | 1 | 0 |
| punctuation | 1 | 0 |

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
- text not on the page: SP114_CW_156-5 J156-5-04/26, cancelled item b, punctuation between G and il: `$G$, il` → `$G$ il`
- text not on the page: SP14_CW_13+15+26+35+48+66+97+123+162 H97-01/2, signature after initial P: `J-P.` → `J-P`
- text not on the page: SP38_CW_75 J75-01/8, Punctuation after A in first slanted row: `\forall a\in A,` → `\forall a\in A`
- text not on the page: SP38_CW_75 J75-02/12, Second opening parenthesis before bijectif: `(bijectif)` → `bijectif)`
- text not on the page: SP42_CW_29 A29-01/11, Paragraph 1, line 8, after first ramification: `ramification.` → `ramification`
- punctuation or continuation mark: SP96_WK_1 1/73, D02, product continuation: `\rho_{i_1}(w)\ldots\rho_{i_m}(w)` → `\rho_{i_1}(w)\mathord{-}\rho_{i_m}(w)`
- punctuation or continuation mark: SP96_WK_1 1/73, attainment paragraph, punctuation after Prouvons: `Prouvons maintenant` → `Prouvons, maintenant`
- punctuation or continuation mark: SP96_WK_1 1/73, last line, terminal punctuation: `la formule (18).` → `la formule (18),`
- supplied indices: SP96_WK_1 1/75, opening display, two repeated upper summation limits: `\sum_1^n\log(1+r\rho_i(u+v))\leq\sum_1^n\log(1+r\rho_i(u))+\sum_1^n\log(1+r\rho_i(v))` → `\sum_1^n\log(1+r\rho_i(u+v))\leq\sum_1\log(1+r\rho_i(u))+\sum_1\log(1+r\rho_i(v))`
- literal ink correction: SP96_WK_1 1/77, independent audit B04, continuation marks: `\ldots` → `i=1,\mathord{.}\,\mathord{-}n`
- literal ink correction: SP96_WK_1 1/77, independent audit B05, continuation marks: `\ldots` → `\wedge\mathord{-}\wedge`
- literal ink correction: SP96_WK_1 1/77, independent audit B07, continuation marks: `\ldots` → `\wedge\mathord{-}\wedge`
- literal ink correction: SP96_WK_1 1/77, independent audit B10, continuation marks: `\ldots` → `\wedge\mathord{-}\wedge`
- literal ink correction: SP96_WK_1 1/77, independent audit B17, continuation marks: `\ldots` → `\wedge\mathord{-}\wedge`
- literal ink correction: SP96_WK_1 1/77, independent audit B19, continuation marks: `\ldots` → `\wedge\mathord{-}\wedge`

## Content changes: the differing pieces (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
| `.→` | 350 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/121 |
| `unsure→` | 223 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| `→_:` | 216 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/129, SP02_CW_10+12 B12-01/69 |
| `→,` | 165 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-05/75 |
| `∅→φ` | 163 | SP100_CW_81 J81-06/43, SP100_CW_81 J81-06/43, SP100_CW_81 J81-06/43 |
| `→.` | 157 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-05/74 |
| `…→-` | 153 | SP74_C13_143+145 143/29, SP80_C13_147 147/128, SP80_C13_147 147/128 |
| `→d` | 133 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| `e→` | 131 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/67 |
| `→𝒞:` | 130 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `[→` | 126 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→e` | 122 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-04/67 |
| `s→` | 118 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127 |
| `→retained` | 115 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/73 |
| `→l` | 108 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `→)` | 106 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/134 |
| `→n` | 104 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/68 |
| `é→e` | 104 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56 |
| `doubtful→` | 97 | SP31_CW_156-3 J156-3-03/22, SP58_CW_156-5 J156-5-06/42, SP58_CW_156-5 J156-5-06/42 |
| `,→` | 95 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-09/129, SP114_CW_156-5 J156-5-04/26 |
| `→s` | 94 | SP02_CW_10+12 B10-01/33, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-04/61 |
| `→-` | 92 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47 |
| `π→Π` | 92 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| `→(` | 86 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
| `omitt→curv` | 78 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| `)→` | 74 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/132, SP101_CW_29 C29-01/15 |
| `→a` | 67 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/48 |
| `→r` | 65 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/44 |
| `d→` | 65 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
| `→t` | 63 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/65 |
| `(→` | 63 | SP102_CW_29+32 C29-06/121, SP102_CW_29+32 C29-06/121, SP102_CW_29+32 C29-06/121 |
| `→𝔹:` | 62 | SP02_CW_10+12 B10-03/51, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66 |
| `→ain` | 62 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10 |
| `?]→` | 62 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→i` | 59 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `r→` | 58 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `→rawn` | 57 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `-→` | 56 | SP02_CW_10+12 B10-03/55, SP102_CW_29+32 C32-01/12, SP102_CW_29+32 C32-01/12 |
| `o→` | 55 | SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72 |
| `→;` | 55 | SP117_CW_97+123+162-1 H97-01/19, SP117_CW_97+123+162-1 C123-01/18, SP12_CW_45+46+53+57+63 J53-01/4 |
| `t→` | 51 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-08/122 |
| `→2` | 50 | SP02_CW_10+12 B10-01/40, SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119 |
| `→unsure` | 50 | SP04_CW_156-4+156-6 J156-4-01/6, SP04_CW_156-4+156-6 J156-4-01/8, SP04_CW_156-4+156-6 J156-4-02/10 |
| `…→-,-` | 49 | SP80_C13_147 147/129, SP80_C13_147 147/129, SP80_C13_147 147/129 |
| `à→:` | 48 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `a→` | 46 | SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/75 |
| `sert→` | 45 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→Creta` | 45 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `]→` | 44 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/40, SP04_CW_156-4+156-6 J156-4-06/42 |
| `→tikzpicture` | 44 | SP102_CW_29+32 C32-01/10, SP102_CW_29+32 C32-01/13, SP102_CW_29+32 C32-01/10 |
| `→𝔉:` | 44 | SP117_CW_97+123+162-1 C123-01/2, SP57_CW_97+123+162-1+162-6 C123-01/2, SP57_CW_97+123+162-1+162-6 C123-01/19 |
| `→→-` | 43 | SP65_C13_16 16/51, SP66_C13_16+120+136 120/3, SP66_C13_16+120+136 120/11 |
| `→f` | 42 | SP02_CW_10+12 B10-07/108, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-10/131 |
| `→u` | 41 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-05/70 |
| `→'` | 41 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `→tw` | 41 | SP02_CW_10+12 B10-04/67, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/75 |
| `'→` | 41 | SP02_CW_10+12 B10-09/128, SP04_CW_156-4+156-6 J156-4-07/52, SP101_CW_29 C29-02/21 |
| `_:→` | 39 | SP04_CW_156-4+156-6 J156-4-07/52, SP04_CW_156-4+156-6 J156-4-07/57, SP102_CW_29+32 C29-06/123 |
| `a→.` | 38 | SP02_CW_10+12 B10-09/123, SP04_CW_156-4+156-6 J156-4-07/56, SP114_CW_156-5 J156-5-04/32 |
| `→o` | 37 | SP02_CW_10+12 B10-01/41, SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-03/51 |
| `→deleted` | 37 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/119 |
| `→|` | 37 | SP02_CW_10+12 B10-05/75, SP101_CW_29 C29-03/33, SP102_CW_29+32 C32-01/12 |
| `n→` | 37 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/107, SP02_CW_10+12 B10-08/118 |
| `→Cr` | 35 | SP02_CW_10+12 B10-07/104, SP04_CW_156-4+156-6 J156-4-06/46, SP12_CW_45+46+53+57+63 J53-01/6 |
| `rl→ta` | 35 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `i→` | 34 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-05/75 |
| `→guidedrawn` | 34 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `?→` | 34 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `→1` | 33 | SP02_CW_10+12 B10-08/116, SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119 |
| `→;tikzpicture` | 33 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/98 |
| `ξ→ζ` | 33 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
| `.→,` | 31 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-10/136, SP101_CW_29 A29-01/80 |
| `und→Cr` | 31 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `→sh` | 30 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-04/64 |
| `→C` | 30 | SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/75 |
| `→Cretaine` | 30 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-01/7 |
| `→3` | 29 | SP45_CW_37 B37-01/3, SP73_C13_142+143 142/111, SP73_C13_142+143 142/111 |
| `→6` | 28 | SP02_CW_10+12 B10-01/40, SP75_C13_145 145/13, SP78_C13_147 147/75 |
| `→c` | 28 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/115 |
| `tt→d` | 28 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `co→` | 28 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `′→'` | 28 | SP102_CW_29+32 C32-01/9, SP102_CW_29+32 C32-01/14, SP102_CW_29+32 C32-01/14 |
| `…→·-` | 28 | SP89_C13_149+150 150/7, SP91_C13_150 150/78, SP92_C13_150+151 150/79 |
| `→ed` | 27 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/77 |
| `𝒞:→` | 27 | SP04_CW_156-4+156-6 J156-4-07/55, SP31_CW_156-3 J156-3-01/3, SP51_CW_134-2 H134-06/180 |
| `m→spag` | 26 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `→,canceled` | 26 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
| `…,→-` | 26 | SP74_C13_143+145 143/29, SP74_C13_143+145 143/29, SP74_C13_143+145 143/29 |
| `m→` | 25 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/87 |
| `→h` | 25 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/68 |
| `l→` | 25 | SP02_CW_10+12 B10-05/75, SP100_CW_81 J81-07/54, SP100_CW_81 J81-07/54 |
| `e→é` | 25 | SP102_CW_29+32 C32-01/13, SP41_CW_81 J81-05/35, SP71_C13_142 142/59 |
| `→4` | 25 | SP102_CW_29+32 C32-01/15, SP45_CW_37 B37-02/30, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| `→Cret` | 25 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `_→` | 25 | SP12_CW_45+46+53+57+63 A57-01/4, SP31_CW_156-3 J156-3-01/3, SP31_CW_156-3 J156-3-01/5 |
| `'→"reading":"` | 25 | SP40_CW_81 J81-03/26, SP40_CW_81 J81-03/26, SP40_CW_81 J81-03/26 |
| `u→` | 24 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-06/83, SP02_CW_10+12 B12-01/69 |
| `,→;` | 24 | SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/60 |
| `h→` | 24 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/72, SP102_CW_29+32 C29-06/123 |
| `del→Cr` | 24 | SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→,deleted` | 24 | SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `c→C` | 24 | SP02_CW_10+12 B10-09/125, SP100_CW_81 J81-06/45, SP100_CW_81 J81-06/45 |
| `→in` | 24 | SP02_CW_10+12 B12-02/123, SP04_CW_156-4+156-6 J156-4-07/52, SP116_CW_75 J75-01/6 |
| `→0` | 24 | SP48_CW_104 H104-01/5, SP66_C13_16+120+136 120/21, SP72_C13_142 142/97 |
| `ou→` | 23 | SP04_CW_156-4+156-6 J156-4-02/15, SP04_CW_156-4+156-6 J156-4-02/15, SP100_CW_81 J81-06/43 |
| `→\` | 23 | SP45_CW_37 B37-02/30, SP73_C13_142+143 142/112, SP73_C13_142+143 142/115 |
| `x→` | 22 | SP02_CW_10+12 B10-05/75, SP101_CW_29 C29-03/29, SP101_CW_29 C29-03/31 |
| `uncertain→` | 22 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77 |
| `c→` | 22 | SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B12-01/98, SP100_CW_81 J81-06/46 |
| `→|→` | 22 | SP102_CW_29+32 C29-06/123, SP102_CW_29+32 C29-06/123, SP102_CW_29+32 C29-06/123 |
| `o→c` | 22 | SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/48 |
| `→5` | 21 | SP02_CW_10+12 B10-08/116, SP46_CW_37 B37-04/74, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| `→inserted` | 21 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-05/34 |
| `→m` | 21 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/130 |
| `1→2` | 21 | SP100_CW_81 J81-07/54, SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119 |
| `→9` | 21 | SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119 |
| `→''` | 20 | SP04_CW_156-4+156-6 J156-4-01/2, SP04_CW_156-4+156-6 J156-4-01/4, SP04_CW_156-4+156-6 J156-4-07/52 |
| `→:` | 20 | SP04_CW_156-4+156-6 J156-4-03/23, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/49, SP64_C13_15+16 15/191 |
| `a→e` | 20 | SP04_CW_156-4+156-6 J156-4-04/26, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `ag→` | 20 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| `en→` | 20 | SP32_CW_156-3 J156-3-05/36, SP38_CW_75 J75-01/8, SP38_CW_75 J75-02/14 |
| `S→G` | 20 | SP82_C13_148 148/33, SP92_C13_150+151 151/3, SP92_C13_150+151 151/3 |
| `o→ô` | 20 | SP89_C13_149+150 150/14, SP89_C13_149+150 150/14, SP89_C13_149+150 150/15 |
| `→g` | 19 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-06/84 |
| `rawn→` | 19 | SP02_CW_10+12 B10-05/72, SP12_CW_45+46+53+57+63 J53-05/32, SP12_CW_45+46+53+57+63 J53-05/34 |
| `→Cre` | 19 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `;→` | 19 | SP02_CW_10+12 B10-08/116, SP14_CW_13+15+26+35+48+66+97+123+162 B15-01/82, SP14_CW_13+15+26+35+48+66+97+123+162 H26-01/11 |
| `î→i` | 19 | SP02_CW_10+12 B10-10/135, SP116_CW_75 J75-01/3, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/39 |
| `…→` | 19 | SP39_CW_75 J75-04/27, SP39_CW_75 J75-04/27, SP39_CW_75 J75-04/27 |
| `:→` | 19 | SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12 |
| `𝔉→𝒞` | 19 | SP73_C13_142+143 142/108, SP92_C13_150+151 151/3, SP92_C13_150+151 151/3 |
| `→8` | 19 | SP78_C13_147 147/75, SP79_C13_147 147/86, SP81_C13_147+148 148/5 |
| `→join` | 19 | SP81_C13_147+148 148/9, SP81_C13_147+148 148/18, SP81_C13_147+148 148/18 |
| `→,cancelled` | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/80 |
| `mitt→ngcurv` | 18 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `è→ê` | 18 | SP02_CW_10+12 B12-02/123, SP02_CW_10+12 B12-02/123, SP101_CW_29 C29-01/14 |
| `G→C` | 18 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP115_CW_156-7 H156-01/5 |
| `→[` | 18 | SP04_CW_156-4+156-6 J156-4-05/37, SP04_CW_156-4+156-6 J156-4-05/40, SP04_CW_156-4+156-6 J156-4-05/41 |
| `|→` | 18 | SP100_CW_81 J81-06/48, SP12_CW_45+46+53+57+63 J53-01/6, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/17 |
| `r→v` | 18 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `1→` | 18 | SP12_CW_45+46+53+57+63 J53-05/30, SP82_C13_148 148/24, SP82_C13_148 148/24 |
| `…→--` | 18 | SP81_C13_147+148 147/136, SP81_C13_147+148 147/136, SP89_C13_149+150 149/134 |
| `→p=round,` | 18 | SP81_C13_147+148 148/9, SP81_C13_147+148 148/18, SP81_C13_147+148 148/18 |
| `b→` | 17 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B12-01/98, SP115_CW_156-7 H156-01/3 |
| `→wi` | 17 | SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133 |
| `→]` | 17 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-06/46, SP35_CW_156-7 H156-01/5 |
| `s→d` | 17 | SP101_CW_29 C29-01/16, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→7` | 17 | SP102_CW_29+32 C32-01/10, SP78_C13_147 147/75, SP81_C13_147+148 148/5 |
| `→de` | 17 | SP14_CW_13+15+26+35+48+66+97+123+162 H26-01/9, SP35_CW_156-7 H156-01/3, SP38_CW_75 J75-02/10 |
| `(→;` | 17 | SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12 |

## Content changes: word-level (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
|  → φ | 152 | SP02_CW_10+12 B10-10/131, SP100_CW_81 J81-06/43, SP100_CW_81 J81-06/43 |
| π → Π | 79 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| ξ → ζ | 38 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
|  → Cretained | 28 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12 |
|  → retained | 26 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/106 |
| nothing →  | 26 | SP81_C13_147+148 147/134, SP82_C13_148 148/44, SP82_C13_148 148/44 |
|  → at | 25 | SP46_CW_37 H37-01/52, SP57_CW_97+123+162-1+162-6 H162-01/4, SP73_C13_142+143 142/113 |
|  → deleted | 24 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18 |
|  → tikzpicture | 24 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-02/123, SP57_CW_97+123+162-1+162-6 C123-02/23 |
| commentonly → mspage | 23 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| absent →  | 22 | SP02_CW_10+12 B10-03/57, SP41_CW_81 J81-05/37, SP41_CW_81 J81-05/37 |
| i →  | 22 | SP39_CW_75 J75-04/28, SP44_CW_36 A36-01/14, SP45_CW_37 B37-02/25 |
|  → canceled | 21 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-09/123 |
| X →  | 21 | SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-03/19 |
| omitted → curvedguidedrawn | 20 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76 |
| à →  | 20 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-08/58 |
| omitted →  | 19 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-10/131 |
|  → cancelled | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-06/80 |
| S → G | 18 | SP82_C13_148 148/33, SP92_C13_150+151 151/3, SP92_C13_150+151 151/3 |
|  → doubtful | 16 | SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/36 |
|  → rotate | 16 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
| omitted → guidedrawn | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
|  → linewidth pt | 15 | SP100_CW_81 J81-07/54, SP52_CW_156-4+156-6 J156-4-09/72, SP57_CW_97+123+162-1+162-6 C123-02/22 |
|  → controls and | 15 | SP36_CW_71 J71-01/6, SP46_CW_37 B37-04/74, SP52_CW_156-4+156-6 J156-4-09/71 |
|  → o | 14 | SP02_CW_10+12 B10-02/45, SP04_CW_156-4+156-6 J156-4-05/41, SP101_CW_29 C29-03/29 |
|  → m | 14 | SP02_CW_10+12 B10-03/55, SP35_CW_156-7 H156-01/4, SP51_CW_134-2 H134-05/176 |
| a →  | 13 | SP02_CW_10+12 B10-03/57, SP31_CW_156-3 J156-3-03/25, SP32_CW_156-3 J156-3-05/39 |
|  → C | 13 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/125, SP02_CW_10+12 B10-10/133 |
|  → i | 12 | SP02_CW_10+12 B10-04/63, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| G →  | 12 | SP115_CW_156-7 H156-01/8, SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9 |
| connaît → connait | 12 | SP116_CW_75 J75-01/3, SP38_CW_75 J75-01/3, SP72_C13_142 142/82 |
| none → Cretained | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| m →  | 12 | SP63_C13_15 15/165, SP80_C13_147 147/123, SP85_C13_149 149/39 |
|  → S | 11 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/43 |
|  → F | 11 | SP02_CW_10+12 B10-05/71, SP04_CW_156-4+156-6 J156-4-01/3, SP04_CW_156-4+156-6 J156-4-06/48 |
|  → A | 11 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/127 |
|  → E | 11 | SP117_CW_97+123+162-1 C123-02/28, SP41_CW_81 J81-05/38, SP47_CW_103 H103-01/2 |
| o → Cretained | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| right sidetag → labelatleft | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
| n →  | 11 | SP48_CW_104 H104-01/5, SP60_CW_71 J71-06/47, SP65_C13_16 16/20 |
|  → aligned | 11 | SP75_C13_145 145/13, SP75_C13_145 145/18, SP75_C13_145 145/18 |
|  → M | 10 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
|  → egible | 10 | SP02_CW_10+12 B10-05/69, SP63_C13_15 15/142, SP80_C13_147 147/123 |
|  → e | 10 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
|  → G | 10 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/128 |
|  → X | 10 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/127 |
| x →  | 10 | SP04_CW_156-4+156-6 J156-4-06/44, SP100_CW_81 J81-06/46, SP115_CW_156-7 H156-01/6 |
| déf → def | 10 | SP34_CW_156-5 J156-5-04/30, SP77_C13_147 147/45, SP89_C13_149+150 150/3 |
|  → ex | 10 | SP35_CW_156-7 H156-01/9, SP74_C13_143+145 143/16, SP74_C13_143+145 143/16 |
|  → Σ | 10 | SP40_CW_81 J81-02/15, SP41_CW_81 J81-04/27, SP41_CW_81 J81-04/27 |
| asapplicable → aswritten | 10 | SP70_C13_142 142/29, SP70_C13_142 142/29, SP70_C13_142 142/29 |
| la → le | 9 | SP04_CW_156-4+156-6 J156-4-04/26, SP37_CW_71 J71-05/36, SP51_CW_134-2 H134-06/183 |
| L → calL | 9 | SP04_CW_156-4+156-6 J156-4-05/41, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/11 |
|  → de | 9 | SP45_CW_37 B37-01/13, SP52_CW_156-4+156-6 J156-4-09/71, SP72_C13_142 142/90 |
| j → J | 9 | SP51_CW_134-2 H134-05/175, SP51_CW_134-2 H134-05/176, SP51_CW_134-2 H134-05/176 |
| ij → i j | 9 | SP73_C13_142+143 142/115, SP73_C13_142+143 142/116, SP73_C13_142+143 142/121 |
| black → gray | 9 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
| r →  | 8 | SP02_CW_10+12 B10-04/64, SP43_CW_29+32 C29-04/38, SP71_C13_142 142/63 |
| calligraphicP → P | 8 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| S →  | 8 | SP04_CW_156-4+156-6 J156-4-03/24, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/5, SP44_CW_36 A36-01/14 |
| k → Cretained | 8 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/12 |
| right sidetag → typed atleft | 8 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
|  → l | 8 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-03/37, SP38_CW_75 J75-01/9, SP40_CW_81 J81-03/23 |
| j →  | 8 | SP58_CW_156-5 J156-5-05/40, SP74_C13_143+145 143/9, SP75_C13_145 145/27 |
| i e → ie | 8 | SP72_C13_142 142/80, SP72_C13_142 142/80, SP72_C13_142 142/86 |
|  → I | 7 | SP02_CW_10+12 B10-04/60, SP48_CW_104 H104-01/6, SP78_C13_147 147/68 |
|  → x | 7 | SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-10/132, SP02_CW_10+12 B12-01/97 |
|  → u | 7 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/128, SP48_CW_104 H104-01/5 |
|  → a | 7 | SP02_CW_10+12 B10-09/127, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19 |
| unsure →  | 7 | SP04_CW_156-4+156-6 J156-4-01/6, SP12_CW_45+46+53+57+63 J53-02/10, SP33_CW_156-5 J156-5-01/8 |
| G → C | 7 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP115_CW_156-7 H156-01/5 |
| système → systême | 7 | SP101_CW_29 C29-01/14, SP101_CW_29 C29-01/17, SP101_CW_29 C29-01/17 |
| de → Cretained | 7 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
|  → ε | 7 | SP12_CW_45+46+53+57+63 J53-04/25, SP38_CW_75 J75-01/3, SP41_CW_81 J81-04/33 |
| stable → st bl | 7 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29 |
| underlinedO → Cretained | 7 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/7, SP12_CW_45+46+53+57+63 A57-01/7 |
| m m →  | 7 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/25, SP86_C13_149 149/77, SP87_C13_149 149/79 |
|  → Z | 7 | SP38_CW_75 J75-01/8, SP38_CW_75 J75-01/9, SP38_CW_75 J75-02/13 |
|  → Noterminalcomma | 7 | SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6 |
| n → f | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| n → u | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| doubtful →  | 7 | SP58_CW_156-5 J156-5-05/37, SP58_CW_156-5 J156-5-05/39, SP58_CW_156-5 J156-5-06/42 |
| SE → S E | 7 | SP75_C13_145 145/25, SP75_C13_145 145/25, SP75_C13_145 145/25 |
| omitted → curvedinsertionbracketinTikZ | 6 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| omitted → longcurvedbracketinTikZ | 6 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/63 |
| omitted → mspage | 6 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73 |
| A →  | 6 | SP02_CW_10+12 B10-10/135, SP43_CW_29+32 C29-04/83, SP62_CW_162-1+162-6 H162-02/4 |
|  → j | 6 | SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| F →  | 6 | SP04_CW_156-4+156-6 J156-4-07/53, SP04_CW_156-4+156-6 J156-4-07/57, SP115_CW_156-7 H156-01/5 |
|  → Y | 6 | SP102_CW_29+32 C29-06/121, SP102_CW_29+32 C29-06/121, SP102_CW_29+32 C29-06/121 |
| Y → SY YS | 6 | SP102_CW_29+32 C29-07/128, SP102_CW_29+32 C29-07/128, SP102_CW_29+32 C29-07/128 |
| sss → Cretained | 6 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-05/29 |
| X o → Cretained | 6 | SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/13 |
|  → et | 6 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40, SP38_CW_75 J75-02/14, SP40_CW_81 J81-02/17 |
|  → circle | 6 | SP14_CW_13+15+26+35+48+66+97+123+162 B15-01/59, SP52_CW_156-4+156-6 J156-4-09/71, SP52_CW_156-4+156-6 J156-4-09/72 |
| omitted → ngExtraStro | 6 | SP31_CW_156-3 J156-3-02/11, SP31_CW_156-3 J156-3-02/15, SP31_CW_156-3 J156-3-02/17 |
| Σ →  | 6 | SP40_CW_81 J81-02/16, SP91_C13_150 150/56, SP91_C13_150 150/58 |
|  → Completeselectedstatesinsourceorder | 6 | SP40_CW_81 J81-03/25, SP40_CW_81 J81-03/25, SP40_CW_81 J81-03/25 |
| même →  | 6 | SP52_CW_156-4+156-6 J156-4-08/65, SP73_C13_142+143 143/5, SP82_C13_148 148/33 |
| insertionwithoutdrawnleader → insertionwithdrawnleader | 6 | SP64_C13_15+16 16/003, SP64_C13_15+16 16/003, SP64_C13_15+16 16/003 |
| insertionwithoutdrawnleader → insertionwithcurvedleader | 6 | SP64_C13_15+16 16/008, SP64_C13_15+16 16/008, SP64_C13_15+16 16/008 |
| insertedreadingwithoutdrawnleader → insertedreadingwithcurvedleader | 6 | SP64_C13_15+16 16/010, SP64_C13_15+16 16/010, SP64_C13_15+16 16/010 |
|  → tt | 6 | SP66_C13_16+120+136 120/24, SP71_C13_142 142/52, SP72_C13_142 142/90 |
| π →  | 6 | SP70_C13_142 142/50, SP71_C13_142 142/55, SP71_C13_142 142/57 |
| doubtfulbold plainGamma → boldGamma | 6 | SP71_C13_142 142/69, SP71_C13_142 142/69, SP71_C13_142 142/69 |
| q → pd | 6 | SP80_C13_147 147/108, SP80_C13_147 147/108, SP80_C13_147 147/108 |
|  → and | 6 | SP82_C13_148 148/24, SP82_C13_148 148/26, SP82_C13_148 148/26 |
| gray → black | 6 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
| r π → at Π | 6 | SP93_C13_151 151/33, SP93_C13_151 151/33, SP93_C13_151 151/33 |
| o →  | 5 | SP02_CW_10+12 B10-04/62, SP04_CW_156-4+156-6 J156-4-05/41, SP115_CW_156-7 H156-01/9 |
|  → N | 5 | SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-09/125, SP97_WK_1 1/99 |
| omitted → curvedinsertionguidedrawn | 5 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| otimes →  | 5 | SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-08/117 |
| mu → muusingfirstqualifiedcandidate | 5 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118 |
| omitted → localcurvedguidedrawn | 5 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
| D →  | 5 | SP04_CW_156-4+156-6 J156-4-01/2, SP04_CW_156-4+156-6 J156-4-01/3, SP117_CW_97+123+162-1 C123-01/3 |
| unsureà colon →  | 5 | SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/11 |
|  → P | 5 | SP04_CW_156-4+156-6 J156-4-07/54, SP14_CW_13+15+26+35+48+66+97+123+162 H48-01/5, SP31_CW_156-3 J156-3-01/2 |
| lafamille → lafamill | 5 | SP102_CW_29+32 C29-05/115, SP102_CW_29+32 C29-05/115, SP102_CW_29+32 C29-05/115 |
| ainsiqueφafterthecommafollowingde → ainsiqueφafterthedoubtfulf beforethedoubtfulest | 5 | SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119, SP102_CW_29+32 C29-06/119 |
