# What the second passes changed in our first readings

13667 changes in 61 collation tables (`SP_CHANGES.tsv`, one row each).

| class | changes |
|---|---|
| content | 10129 |
| doubt only | 3013 |
| markup only | 229 |
| inserted/placed | 171 |
| struck/live | 94 |
| ill resolved | 31 |

## By the run's own kind

| kind | content | doubt only | markup only | inserted/placed | struck/live | ill resolved |
|---|---|---|---|---|---|---|
| misread symbol or index | 1966 | 609 | 49 | 21 | 3 | 0 |
| omission | 1496 | 532 | 54 | 17 | 38 | 2 |
| misread word | 1231 | 699 | 17 | 26 | 7 | 1 |
| drawing or diagram | 1829 | 18 | 8 | 4 | 0 | 4 |
| readable ink left as \ill{} | 742 | 461 | 13 | 7 | 18 | 17 |
| insertion or placement | 804 | 76 | 27 | 63 | 3 | 2 |
| abbreviation expanded or spelling modernised | 496 | 252 | 12 | 5 | 0 | 0 |
| other | 485 | 154 | 28 | 15 | 1 | 1 |
| deletion state (struck given live or live given struck) | 530 | 116 | 5 | 9 | 16 | 2 |
| text not on the page | 367 | 37 | 7 | 1 | 0 | 2 |
| deletion state | 182 | 59 | 9 | 3 | 8 | 0 |
| diagram or graphic sign | 1 | 0 | 0 | 0 | 0 | 0 |

## Where nobody doubted

Content changes at places witness C had not marked: 6800 of 10129. Of these, witness H had the same reading as C and no doubt mark either: 2150 (both witnesses wrong the same way, nobody doubting; rows with `c_equals_h` = yes, `c_marked` = no, `h_marked` = no in SP_CHANGES.tsv).

| kind | C unmarked | C and H agree, both unmarked |
|---|---|---|
| drawing or diagram | 1655 | 687 |
| misread symbol or index | 1244 | 449 |
| omission | 971 | 400 |
| misread word | 679 | 200 |
| insertion or placement | 616 | 84 |
| other | 374 | 129 |
| readable ink left as \ill{} | 318 | 0 |
| text not on the page | 311 | 60 |
| abbreviation expanded or spelling modernised | 305 | 82 |
| deletion state (struck given live or live given struck) | 229 | 36 |
| deletion state | 97 | 23 |
| diagram or graphic sign | 1 | 0 |

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

## Content changes: the differing pieces (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
| `unsure→` | 223 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| `.→` | 172 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/121 |
| `→_:` | 116 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/129, SP02_CW_10+12 B12-01/69 |
| `[→` | 116 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `→retained` | 115 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/73 |
| `→d` | 112 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/63 |
| `→.` | 107 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-05/74 |
| `→e` | 104 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-04/64, SP02_CW_10+12 B10-04/67 |
| `→l` | 103 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `doubtful→` | 97 | SP31_CW_156-3 J156-3-03/22, SP58_CW_156-5 J156-5-06/42, SP58_CW_156-5 J156-5-06/42 |
| `s→` | 91 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127 |
| `→n` | 87 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/68 |
| `e→` | 84 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/67 |
| `→,` | 78 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-05/75 |
| `omitt→curv` | 78 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| `→s` | 72 | SP02_CW_10+12 B10-01/33, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-04/61 |
| `→)` | 72 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/134 |
| `π→Π` | 69 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| `→(` | 63 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
| `→ain` | 62 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10 |
| `?]→` | 62 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-04/31 |
| `é→e` | 59 | SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56, SP02_CW_10+12 B10-03/56 |
| `→𝔹:` | 58 | SP02_CW_10+12 B10-03/51, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66 |
| `∅→φ` | 58 | SP114_CW_156-5 J156-5-04/27, SP114_CW_156-5 J156-5-04/27, SP114_CW_156-5 J156-5-04/27 |
| `→rawn` | 57 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `d→` | 56 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-02/47 |
| `→𝒞:` | 55 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `r→` | 54 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `→a` | 53 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/48 |
| `→i` | 50 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `→unsure` | 50 | SP04_CW_156-4+156-6 J156-4-01/6, SP04_CW_156-4+156-6 J156-4-01/8, SP04_CW_156-4+156-6 J156-4-02/10 |
| `→t` | 47 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/65 |
| `o→` | 46 | SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72 |
| `→r` | 45 | SP02_CW_10+12 B10-02/42, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/44 |
| `sert→` | 45 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→Creta` | 45 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→𝔉:` | 44 | SP117_CW_97+123+162-1 C123-01/2, SP57_CW_97+123+162-1+162-6 C123-01/2, SP57_CW_97+123+162-1+162-6 C123-01/19 |
| `→tw` | 41 | SP02_CW_10+12 B10-04/67, SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/75 |
| `→-` | 40 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/46, SP02_CW_10+12 B10-02/47 |
| `→f` | 39 | SP02_CW_10+12 B10-07/108, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-10/131 |
| `-→` | 38 | SP02_CW_10+12 B10-03/55, SP12_CW_45+46+53+57+63 J53-03/22, SP35_CW_156-7 H156-01/7 |
| `,→` | 38 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-09/129, SP114_CW_156-5 J156-5-04/26 |
| `→deleted` | 37 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/119 |
| `)→` | 37 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/132, SP114_CW_156-5 J156-5-04/33 |
| `à→:` | 37 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `t→` | 35 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-08/122 |
| `→Cr` | 35 | SP02_CW_10+12 B10-07/104, SP04_CW_156-4+156-6 J156-4-06/46, SP12_CW_45+46+53+57+63 J53-01/6 |
| `rl→ta` | 35 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `a→` | 34 | SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/75 |
| `→guidedrawn` | 34 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/75 |
| `?→` | 34 | SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/18 |
| `→;` | 33 | SP117_CW_97+123+162-1 H97-01/19, SP117_CW_97+123+162-1 C123-01/18, SP12_CW_45+46+53+57+63 J53-01/4 |
| `→2` | 31 | SP02_CW_10+12 B10-01/40, SP114_CW_156-5 J156-5-04/30, SP45_CW_37 B37-01/3 |
| `und→Cr` | 31 | SP12_CW_45+46+53+57+63 J53-03/16, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `…→-` | 31 | SP74_C13_143+145 143/29, SP80_C13_147 147/128, SP80_C13_147 147/128 |
| `→sh` | 30 | SP02_CW_10+12 B10-03/52, SP02_CW_10+12 B10-03/54, SP02_CW_10+12 B10-04/64 |
| `→'` | 30 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/66, SP02_CW_10+12 B10-05/69 |
| `→C` | 30 | SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-05/75 |
| `a→.` | 30 | SP02_CW_10+12 B10-09/123, SP04_CW_156-4+156-6 J156-4-07/56, SP114_CW_156-5 J156-5-04/32 |
| `→Cretaine` | 30 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-01/7 |
| `n→` | 29 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/107, SP02_CW_10+12 B10-08/118 |
| `tt→d` | 28 | SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| `→u` | 27 | SP02_CW_10+12 B10-01/40, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-05/70 |
| `→o` | 27 | SP02_CW_10+12 B10-01/41, SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-03/51 |
| `→ed` | 27 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/77 |
| `co→` | 27 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `(→` | 27 | SP114_CW_156-5 J156-5-04/31, SP117_CW_97+123+162-1 C123-01/16, SP12_CW_45+46+53+57+63 J53-04/23 |
| `m→spag` | 26 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
| `→,canceled` | 26 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
| `i→` | 25 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/65, SP02_CW_10+12 B10-05/75 |
| `→|` | 25 | SP02_CW_10+12 B10-05/75, SP117_CW_97+123+162-1 C123-02/23, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19 |
| `→Cret` | 25 | SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6 |
| `del→Cr` | 24 | SP02_CW_10+12 B10-05/75, SP04_CW_156-4+156-6 J156-4-02/10, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→,deleted` | 24 | SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18, SP04_CW_156-4+156-6 J156-4-03/19 |
| `m→` | 23 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/87 |
| `→;tikzpicture` | 23 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-01/98 |
| `→in` | 23 | SP02_CW_10+12 B12-02/123, SP04_CW_156-4+156-6 J156-4-07/52, SP116_CW_75 J75-01/6 |
| `_:→` | 23 | SP04_CW_156-4+156-6 J156-4-07/52, SP04_CW_156-4+156-6 J156-4-07/57, SP115_CW_156-7 H156-01/2 |
| `→c` | 22 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/115 |
| `uncertain→` | 22 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77 |
| `o→c` | 22 | SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/48 |
| `u→` | 21 | SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-06/83, SP02_CW_10+12 B12-01/69 |
| `→inserted` | 21 | SP02_CW_10+12 B10-08/119, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-05/34 |
| `]→` | 20 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/40, SP04_CW_156-4+156-6 J156-4-06/42 |
| `ag→` | 20 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
| `→3` | 20 | SP45_CW_37 B37-01/3, SP73_C13_142+143 142/111, SP73_C13_142+143 142/111 |
| `→h` | 19 | SP02_CW_10+12 B10-02/49, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/68 |
| `rawn→` | 19 | SP02_CW_10+12 B10-05/72, SP12_CW_45+46+53+57+63 J53-05/32, SP12_CW_45+46+53+57+63 J53-05/34 |
| `→Cre` | 19 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `c→` | 19 | SP02_CW_10+12 B10-07/103, SP02_CW_10+12 B12-01/98, SP12_CW_45+46+53+57+63 J53-01/5 |
| `'→` | 19 | SP02_CW_10+12 B10-09/128, SP04_CW_156-4+156-6 J156-4-07/52, SP12_CW_45+46+53+57+63 J53-04/26 |
| `_→` | 19 | SP12_CW_45+46+53+57+63 A57-01/4, SP31_CW_156-3 J156-3-01/3, SP31_CW_156-3 J156-3-01/5 |
| `→4` | 19 | SP45_CW_37 B37-02/30, SP57_CW_97+123+162-1+162-6 C123-02/40, SP72_C13_142 142/81 |
| `→0` | 19 | SP48_CW_104 H104-01/5, SP66_C13_16+120+136 120/21, SP72_C13_142 142/97 |
| `→join` | 19 | SP81_C13_147+148 148/9, SP81_C13_147+148 148/18, SP81_C13_147+148 148/18 |
| `→,cancelled` | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/80 |
| `mitt→ngcurv` | 18 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62 |
| `→1` | 18 | SP02_CW_10+12 B10-08/116, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 H162-01/4 |
| `→6` | 17 | SP02_CW_10+12 B10-01/40, SP75_C13_145 145/13, SP78_C13_147 147/75 |
| `x→` | 17 | SP02_CW_10+12 B10-05/75, SP115_CW_156-7 H156-01/7, SP12_CW_45+46+53+57+63 J53-01/6 |
| `l→` | 17 | SP02_CW_10+12 B10-05/75, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/26 |
| `→5` | 17 | SP02_CW_10+12 B10-08/116, SP46_CW_37 B37-04/74, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| `î→i` | 17 | SP02_CW_10+12 B10-10/135, SP116_CW_75 J75-01/3, SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/39 |
| `→''` | 17 | SP04_CW_156-4+156-6 J156-4-01/2, SP04_CW_156-4+156-6 J156-4-01/4, SP04_CW_156-4+156-6 J156-4-07/52 |
| `′→'` | 17 | SP114_CW_156-5 J156-5-04/28, SP114_CW_156-5 J156-5-04/31, SP115_CW_156-7 H156-01/9 |
| `r→v` | 17 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `(→;` | 17 | SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12 |
| `:→` | 17 | SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12 |
| `→8` | 17 | SP78_C13_147 147/75, SP79_C13_147 147/86, SP81_C13_147+148 148/5 |
| `→p=round,` | 17 | SP81_C13_147+148 148/9, SP81_C13_147+148 148/18, SP81_C13_147+148 148/18 |
| `→cancelled` | 16 | SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/105 |
| `ou→` | 16 | SP04_CW_156-4+156-6 J156-4-02/15, SP04_CW_156-4+156-6 J156-4-02/15, SP12_CW_45+46+53+57+63 J53-01/8 |
| `G→C` | 16 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP115_CW_156-7 H156-01/5 |
| `)→retained` | 16 | SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12, SP40_CW_81 J81-02/12 |
| `.→,` | 15 | SP02_CW_10+12 B10-02/47, SP02_CW_10+12 B10-10/136, SP43_CW_29+32 C29-05/114 |
| `,→;` | 15 | SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-02/48, SP02_CW_10+12 B10-04/60 |
| `→p` | 15 | SP02_CW_10+12 B10-04/63, SP02_CW_10+12 B10-06/82, SP02_CW_10+12 B10-06/87 |
| `→ne` | 15 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/11 |
| `→overlap` | 15 | SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79, SP02_CW_10+12 B10-06/81 |
| `om→gu` | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
| `c→C` | 15 | SP02_CW_10+12 B10-09/125, SP40_CW_81 J81-02/15, SP42_CW_29 A29-01/3 |
| `a→e` | 15 | SP04_CW_156-4+156-6 J156-4-04/26, SP12_CW_45+46+53+57+63 A57-01/10, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/18 |
| `→tai` | 15 | SP04_CW_156-4+156-6 J156-4-05/41, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-02/10 |
| `s→d` | 15 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-01/7 |
| `ξ→ζ` | 15 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
| `→ained` | 14 | SP02_CW_10+12 B10-05/74, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
| `→tained` | 14 | SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/5, SP12_CW_45+46+53+57+63 J53-01/8 |
| `u→Cretai` | 14 | SP12_CW_45+46+53+57+63 J53-01/8, SP12_CW_45+46+53+57+63 J53-03/22, SP12_CW_45+46+53+57+63 J53-04/23 |
| `t→rved` | 14 | SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 J53-04/28, SP12_CW_45+46+53+57+63 J53-04/28 |
| `→doubtful` | 14 | SP58_CW_156-5 J156-5-06/42, SP59_CW_71 J71-01/10, SP59_CW_71 J71-02/17 |
| `→w` | 13 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-04/68, SP04_CW_156-4+156-6 J156-4-06/47 |
| `h→` | 13 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/72, SP31_CW_156-3 J156-3-03/25 |
| `m→n` | 13 | SP02_CW_10+12 B10-05/72, SP12_CW_45+46+53+57+63 J53-01/4, SP12_CW_45+46+53+57+63 J53-01/6 |
| `→e/` | 13 | SP02_CW_10+12 B10-05/76, SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78 |
| `ef→` | 13 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/9 |
| `é→è` | 13 | SP14_CW_13+15+26+35+48+66+97+123+162 H48-01/3, SP38_CW_75 J75-02/15, SP40_CW_81 J81-02/15 |
| `t→rve` | 13 | SP35_CW_156-7 H156-01/7, SP64_C13_15+16 16/008, SP64_C13_15+16 16/008 |
| `→,doubtful` | 13 | SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/36, SP58_CW_156-5 J156-5-05/36 |
| `mi→r` | 12 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/106 |
| `→underlined` | 12 | SP02_CW_10+12 B10-06/77, SP04_CW_156-4+156-6 J156-4-05/35, SP04_CW_156-4+156-6 J156-4-05/36 |
| `unsu→` | 12 | SP02_CW_10+12 B10-09/127, SP12_CW_45+46+53+57+63 J53-01/3, SP12_CW_45+46+53+57+63 J53-01/3 |
| `→le` | 12 | SP02_CW_10+12 B10-09/129, SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/13 |
| `→:` | 12 | SP04_CW_156-4+156-6 J156-4-03/23, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/49, SP64_C13_15+16 15/191 |
| `→``` | 12 | SP04_CW_156-4+156-6 J156-4-04/31, SP04_CW_156-4+156-6 J156-4-06/48, SP35_CW_156-7 H156-01/3 |
| `𝒞:→` | 12 | SP04_CW_156-4+156-6 J156-4-07/55, SP31_CW_156-3 J156-3-01/3, SP51_CW_134-2 H134-06/180 |
| `→C's` | 12 | SP117_CW_97+123+162-1 C123-02/40, SP117_CW_97+123+162-1 C123-02/40, SP117_CW_97+123+162-1 C123-02/40 |
| `f→` | 12 | SP12_CW_45+46+53+57+63 J53-01/6, SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-02/10 |
| `no→Cretai` | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| `→x` | 12 | SP12_CW_45+46+53+57+63 A57-01/13, SP44_CW_36 A36-01/13, SP44_CW_36 A36-01/13 |
| `→|→` | 12 | SP38_CW_75 J75-02/14, SP72_C13_142 142/83, SP72_C13_142 142/83 |

## Content changes: word-level (ours → final), most frequent first

| ours → final | rows | examples |
|---|---|---|
| π → Π | 58 | SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
|  → φ | 52 | SP02_CW_10+12 B10-10/131, SP114_CW_156-5 J156-5-04/27, SP114_CW_156-5 J156-5-04/27 |
|  → Cretained | 28 | SP12_CW_45+46+53+57+63 J53-02/10, SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/12 |
|  → retained | 26 | SP02_CW_10+12 B10-05/73, SP02_CW_10+12 B10-07/105, SP02_CW_10+12 B10-07/106 |
|  → deleted | 24 | SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-08/120, SP04_CW_156-4+156-6 J156-4-03/18 |
| commentonly → mspage | 23 | SP02_CW_10+12 B10-06/77, SP02_CW_10+12 B10-06/78, SP02_CW_10+12 B10-06/79 |
|  → canceled | 21 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123, SP02_CW_10+12 B10-09/123 |
| omitted → curvedguidedrawn | 20 | SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/75, SP02_CW_10+12 B10-05/76 |
|  → cancelled | 18 | SP02_CW_10+12 B10-02/44, SP02_CW_10+12 B10-06/80, SP02_CW_10+12 B10-06/80 |
| ξ → ζ | 18 | SP64_C13_15+16 15/185, SP64_C13_15+16 15/185, SP64_C13_15+16 15/185 |
| à →  | 17 | SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-05/38, SP04_CW_156-4+156-6 J156-4-08/58 |
|  → doubtful | 16 | SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/35, SP58_CW_156-5 J156-5-05/36 |
|  → rotate | 16 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
| omitted →  | 15 | SP02_CW_10+12 B10-02/50, SP02_CW_10+12 B10-03/55, SP02_CW_10+12 B10-10/131 |
| omitted → guidedrawn | 15 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-07/106 |
|  → controls and | 14 | SP36_CW_71 J71-01/6, SP46_CW_37 B37-04/74, SP52_CW_156-4+156-6 J156-4-09/71 |
| X →  | 13 | SP02_CW_10+12 B10-10/133, SP02_CW_10+12 B10-10/133, SP04_CW_156-4+156-6 J156-4-03/19 |
|  → linewidth pt | 13 | SP52_CW_156-4+156-6 J156-4-09/72, SP57_CW_97+123+162-1+162-6 C123-02/22, SP81_C13_147+148 148/18 |
| absent →  | 12 | SP02_CW_10+12 B10-03/57, SP41_CW_81 J81-05/37, SP41_CW_81 J81-05/37 |
| G →  | 12 | SP115_CW_156-7 H156-01/8, SP35_CW_156-7 H156-01/9, SP35_CW_156-7 H156-01/9 |
| none → Cretained | 12 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/30, SP12_CW_45+46+53+57+63 J53-05/31 |
| i →  | 12 | SP39_CW_75 J75-04/28, SP44_CW_36 A36-01/14, SP45_CW_37 B37-02/25 |
|  → S | 11 | SP02_CW_10+12 B10-01/34, SP02_CW_10+12 B10-02/43, SP02_CW_10+12 B10-02/43 |
| a →  | 11 | SP02_CW_10+12 B10-03/57, SP31_CW_156-3 J156-3-03/25, SP32_CW_156-3 J156-3-05/39 |
| o → Cretained | 11 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/6 |
| right sidetag → labelatleft | 11 | SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
|  → o | 10 | SP02_CW_10+12 B10-02/45, SP04_CW_156-4+156-6 J156-4-05/41, SP44_CW_36 A36-01/11 |
|  → m | 10 | SP02_CW_10+12 B10-03/55, SP35_CW_156-7 H156-01/4, SP51_CW_134-2 H134-05/176 |
|  → M | 10 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-10/133 |
|  → F | 10 | SP02_CW_10+12 B10-05/71, SP04_CW_156-4+156-6 J156-4-01/3, SP04_CW_156-4+156-6 J156-4-06/48 |
|  → G | 10 | SP02_CW_10+12 B10-07/106, SP02_CW_10+12 B10-09/128, SP02_CW_10+12 B10-09/128 |
|  → C | 10 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/125, SP02_CW_10+12 B10-10/133 |
| connaît → connait | 10 | SP116_CW_75 J75-01/3, SP38_CW_75 J75-01/3, SP72_C13_142 142/82 |
| asapplicable → aswritten | 10 | SP70_C13_142 142/29, SP70_C13_142 142/29, SP70_C13_142 142/29 |
| L → calL | 9 | SP04_CW_156-4+156-6 J156-4-05/41, SP31_CW_156-3 J156-3-02/10, SP31_CW_156-3 J156-3-02/11 |
|  → ex | 9 | SP35_CW_156-7 H156-01/9, SP74_C13_143+145 143/16, SP74_C13_143+145 143/16 |
| black → gray | 9 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
|  → i | 8 | SP02_CW_10+12 B10-04/63, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
|  → A | 8 | SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/124, SP02_CW_10+12 B10-09/127 |
|  → tikzpicture | 8 | SP02_CW_10+12 B12-01/97, SP02_CW_10+12 B12-02/123, SP57_CW_97+123+162-1+162-6 C123-02/23 |
| calligraphicP → P | 8 | SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21, SP04_CW_156-4+156-6 J156-4-03/21 |
| S →  | 8 | SP04_CW_156-4+156-6 J156-4-03/24, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/5, SP44_CW_36 A36-01/14 |
| x →  | 8 | SP04_CW_156-4+156-6 J156-4-06/44, SP115_CW_156-7 H156-01/6, SP115_CW_156-7 H156-01/7 |
| k → Cretained | 8 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/12 |
| right sidetag → typed atleft | 8 | SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4, SP12_CW_45+46+53+57+63 A57-01/4 |
|  → de | 8 | SP45_CW_37 B37-01/13, SP52_CW_156-4+156-6 J156-4-09/71, SP72_C13_142 142/90 |
|  → at | 8 | SP46_CW_37 H37-01/52, SP57_CW_97+123+162-1+162-6 H162-01/4, SP73_C13_142+143 142/113 |
| n →  | 8 | SP48_CW_104 H104-01/5, SP60_CW_71 J71-06/47, SP65_C13_16 16/20 |
| j → J | 8 | SP51_CW_134-2 H134-05/175, SP51_CW_134-2 H134-05/176, SP51_CW_134-2 H134-05/176 |
| unsure →  | 7 | SP04_CW_156-4+156-6 J156-4-01/6, SP12_CW_45+46+53+57+63 J53-02/10, SP33_CW_156-5 J156-5-01/8 |
| de → Cretained | 7 | SP12_CW_45+46+53+57+63 J53-01/7, SP12_CW_45+46+53+57+63 J53-02/11, SP12_CW_45+46+53+57+63 J53-02/11 |
| stable → st bl | 7 | SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29, SP12_CW_45+46+53+57+63 J53-05/29 |
| underlinedO → Cretained | 7 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/7, SP12_CW_45+46+53+57+63 A57-01/7 |
|  → Noterminalcomma | 7 | SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6, SP40_CW_81 J81-01/6 |
| n → f | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| n → u | 7 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| doubtful →  | 7 | SP58_CW_156-5 J156-5-05/37, SP58_CW_156-5 J156-5-05/39, SP58_CW_156-5 J156-5-06/42 |
|  → aligned | 7 | SP75_C13_145 145/13, SP75_C13_145 145/18, SP75_C13_145 145/18 |
| SE → S E | 7 | SP75_C13_145 145/25, SP75_C13_145 145/25, SP75_C13_145 145/25 |
| omitted → curvedinsertionbracketinTikZ | 6 | SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/60 |
| omitted → longcurvedbracketinTikZ | 6 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/63 |
| r →  | 6 | SP02_CW_10+12 B10-04/64, SP43_CW_29+32 C29-04/38, SP71_C13_142 142/63 |
|  → e | 6 | SP02_CW_10+12 B10-05/70, SP02_CW_10+12 B10-05/74, SP02_CW_10+12 B10-05/74 |
| omitted → mspage | 6 | SP02_CW_10+12 B10-05/71, SP02_CW_10+12 B10-05/72, SP02_CW_10+12 B10-05/73 |
|  → X | 6 | SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/127 |
| A →  | 6 | SP02_CW_10+12 B10-10/135, SP43_CW_29+32 C29-04/83, SP62_CW_162-1+162-6 H162-02/4 |
|  → j | 6 | SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22, SP04_CW_156-4+156-6 J156-4-03/22 |
| G → C | 6 | SP04_CW_156-4+156-6 J156-4-04/28, SP04_CW_156-4+156-6 J156-4-04/29, SP115_CW_156-7 H156-01/5 |
| F →  | 6 | SP04_CW_156-4+156-6 J156-4-07/53, SP04_CW_156-4+156-6 J156-4-07/57, SP115_CW_156-7 H156-01/5 |
|  → E | 6 | SP117_CW_97+123+162-1 C123-02/28, SP41_CW_81 J81-05/38, SP47_CW_103 H103-01/2 |
|  → ε | 6 | SP12_CW_45+46+53+57+63 J53-04/25, SP38_CW_75 J75-01/3, SP41_CW_81 J81-04/33 |
| sss → Cretained | 6 | SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-04/26, SP12_CW_45+46+53+57+63 J53-05/29 |
| X o → Cretained | 6 | SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/10, SP12_CW_45+46+53+57+63 A57-01/13 |
|  → circle | 6 | SP14_CW_13+15+26+35+48+66+97+123+162 B15-01/59, SP52_CW_156-4+156-6 J156-4-09/71, SP52_CW_156-4+156-6 J156-4-09/72 |
| omitted → ngExtraStro | 6 | SP31_CW_156-3 J156-3-02/11, SP31_CW_156-3 J156-3-02/15, SP31_CW_156-3 J156-3-02/17 |
|  → Z | 6 | SP38_CW_75 J75-01/8, SP38_CW_75 J75-01/9, SP38_CW_75 J75-02/13 |
| insertionwithoutdrawnleader → insertionwithdrawnleader | 6 | SP64_C13_15+16 16/003, SP64_C13_15+16 16/003, SP64_C13_15+16 16/003 |
| insertionwithoutdrawnleader → insertionwithcurvedleader | 6 | SP64_C13_15+16 16/008, SP64_C13_15+16 16/008, SP64_C13_15+16 16/008 |
| insertedreadingwithoutdrawnleader → insertedreadingwithcurvedleader | 6 | SP64_C13_15+16 16/010, SP64_C13_15+16 16/010, SP64_C13_15+16 16/010 |
|  → tt | 6 | SP66_C13_16+120+136 120/24, SP71_C13_142 142/52, SP72_C13_142 142/90 |
| π →  | 6 | SP70_C13_142 142/50, SP71_C13_142 142/55, SP71_C13_142 142/57 |
| doubtfulbold plainGamma → boldGamma | 6 | SP71_C13_142 142/69, SP71_C13_142 142/69, SP71_C13_142 142/69 |
| q → pd | 6 | SP80_C13_147 147/108, SP80_C13_147 147/108, SP80_C13_147 147/108 |
|  → and | 6 | SP82_C13_148 148/24, SP82_C13_148 148/26, SP82_C13_148 148/26 |
| gray → black | 6 | SP83_C13_148+149 148/69, SP83_C13_148+149 148/69, SP83_C13_148+149 148/69 |
|  → egible | 5 | SP02_CW_10+12 B10-05/69, SP63_C13_15 15/142, SP80_C13_147 147/123 |
| omitted → curvedinsertionguidedrawn | 5 | SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-07/104, SP02_CW_10+12 B10-08/116 |
| otimes →  | 5 | SP02_CW_10+12 B10-08/115, SP02_CW_10+12 B10-08/116, SP02_CW_10+12 B10-08/117 |
| mu → muusingfirstqualifiedcandidate | 5 | SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118, SP02_CW_10+12 B10-08/118 |
| omitted → localcurvedguidedrawn | 5 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/122, SP02_CW_10+12 B10-09/123 |
|  → a | 5 | SP02_CW_10+12 B10-09/127, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H13-01/19 |
| D →  | 5 | SP04_CW_156-4+156-6 J156-4-01/2, SP04_CW_156-4+156-6 J156-4-01/3, SP117_CW_97+123+162-1 C123-01/3 |
| unsureà colon →  | 5 | SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/10, SP04_CW_156-4+156-6 J156-4-02/11 |
| la → le | 5 | SP04_CW_156-4+156-6 J156-4-04/26, SP37_CW_71 J71-05/36, SP51_CW_134-2 H134-06/183 |
|  → P | 5 | SP04_CW_156-4+156-6 J156-4-07/54, SP14_CW_13+15+26+35+48+66+97+123+162 H48-01/5, SP31_CW_156-3 J156-3-01/2 |
| g → Cretained | 5 | SP12_CW_45+46+53+57+63 J53-02/9, SP12_CW_45+46+53+57+63 J53-04/25, SP12_CW_45+46+53+57+63 J53-04/28 |
| ext → Cretained | 5 | SP12_CW_45+46+53+57+63 J53-02/12, SP12_CW_45+46+53+57+63 J53-02/13, SP12_CW_45+46+53+57+63 J53-02/13 |
| underlinedO X → Cretained | 5 | SP12_CW_45+46+53+57+63 A57-01/5, SP12_CW_45+46+53+57+63 A57-01/8, SP12_CW_45+46+53+57+63 A57-01/8 |
|  → l | 5 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-03/37, SP38_CW_75 J75-01/9, SP72_C13_142 142/78 |
|  → et | 5 | SP14_CW_13+15+26+35+48+66+97+123+162 J13-04/40, SP38_CW_75 J75-02/14, SP40_CW_81 J81-02/17 |
| notrepresented →  | 5 | SP47_CW_103 H103-02/13, SP47_CW_103 H103-02/13, SP47_CW_103 H103-02/14 |
| Omitted → TikZapproximationinanuncertaintywrapper nocompletedtextualreading | 5 | SP47_CW_103 H103-02/14, SP47_CW_103 H103-02/14, SP47_CW_103 H103-02/14 |
|  → headless | 5 | SP48_CW_104 H104-01/5, SP48_CW_104 H104-01/5, SP48_CW_104 H104-01/5 |
| n → top | 5 | SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40, SP57_CW_97+123+162-1+162-6 C123-02/40 |
| j →  | 5 | SP58_CW_156-5 J156-5-05/40, SP74_C13_143+145 143/9, SP75_C13_145 145/27 |
|  → unresolved | 5 | SP63_C13_15 15/165, SP66_C13_16+120+136 136/328, SP66_C13_16+120+136 136/328 |
|  → d | 5 | SP67_C13_136 136/342, SP80_C13_147 147/125, SP80_C13_147 147/125 |
| π π → Π Π | 5 | SP72_C13_142 142/93, SP72_C13_142 142/93, SP72_C13_142 142/94 |
| ellipse → controls | 5 | SP81_C13_147+148 148/18, SP82_C13_148 148/24, SP82_C13_148 148/26 |
|  → H | 4 | SP02_CW_10+12 B10-02/42, SP114_CW_156-5 J156-5-04/27, SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/23 |
| omitted → curvedattachmentinTikZ | 4 | SP02_CW_10+12 B10-03/57, SP02_CW_10+12 B10-04/60, SP02_CW_10+12 B10-04/61 |
|  → I | 4 | SP02_CW_10+12 B10-04/60, SP48_CW_104 H104-01/6, SP78_C13_147 147/68 |
| omitted → curvedbracketinTikZ | 4 | SP02_CW_10+12 B10-04/61, SP02_CW_10+12 B10-04/62, SP02_CW_10+12 B10-04/67 |
| sigma → σσ σ | 4 | SP02_CW_10+12 B10-04/68, SP02_CW_10+12 B10-05/69, SP02_CW_10+12 B10-05/70 |
|  → Q | 4 | SP02_CW_10+12 B10-05/70, SP73_C13_142+143 143/6, SP74_C13_143+145 143/30 |
|  → comma | 4 | SP02_CW_10+12 B10-05/70, SP14_CW_13+15+26+35+48+66+97+123+162 J13-02/11, SP14_CW_13+15+26+35+48+66+97+123+162 J13-05/47 |
| omitted → curvedlocalinsertionguide | 4 | SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/121, SP02_CW_10+12 B10-08/121 |
|  → u | 4 | SP02_CW_10+12 B10-09/127, SP02_CW_10+12 B10-09/128, SP48_CW_104 H104-01/5 |
| Q →  | 4 | SP02_CW_10+12 B12-02/102, SP44_CW_36 A36-01/14, SP69_C13_141+142 142/17 |
| singleunderline → doubleunderline | 4 | SP04_CW_156-4+156-6 J156-4-08/58, SP04_CW_156-4+156-6 J156-4-08/58, SP14_CW_13+15+26+35+48+66+97+123+162 H35-01/3 |
