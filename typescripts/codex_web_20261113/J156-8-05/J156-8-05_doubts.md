# J156-8-05 — notation and doubts

| Source inspected | Visible notation | LaTeX reading | Candidates / checks |
|---|---|---|---|
| 34, heading and opening lines | Magasins, magasin; Mag L 1, Mag L 2 | text Magasins; Mag L 1, Mag L 2 | Title enlarged; the medial strokes read as -gasin-, not magma. |
| 34, line 2 and definition display | doubled left angle with small circle above | `\overset{\circ}{\ll}` | Circle belongs over relation, not X or Y. |
| 34, line 2 and definition display | vertical strokes with circle between | `\mathrel{\vert\circ\vert}` (page uses literal bars) | Separate from parallel without circle. |
| 34, middle three-line display | two opposed angle strokes | `\unsure{\gtrless\|\bowtie}` | Recurring ambiguous relation: first reading gtrless; mark first occurrence on each page. |
| 34, same display | plain doubled left angle | `\ll` | No circle in this row. |
| 34, same display | two vertical strokes | `\parallel` | No central circle. |
| 34, same display | X and Y with wavy tops | `\widetilde X`, `\widetilde Y` | Tildes, not bars. |
| 34, middle lower formulas | omb and a raised circle | `\mathrm{omb}(X)^\circ` | Small circle, not zero; empty-set mark contrasted with possible zero in later prose. |
| 34, left margin (iii), (iv) | FigMag / Fig with lower mag | `\mathrm{FigMag}`, `\mathrm{Fig}_{\mathrm{mag}}` | (iii) ambiguous baseline; (iv) visibly lower smaller letters. Do not enforce identical typography. |
| 34, bottom | tilde F; I; X with i | `\widetilde F`, `I`, `X_i` | Roman mathematical capitals; i has dot and no descender. |
| 34, definition | two small opening/closing strokes | &#96;&#96;trivial'' | Double quotation marks. |
| 35, first display and throughout | looped Greek letter with long descending stem | `\varphi` | Checked individually at first map and in tilde-F equation; not roman p. |
| 35, middle and proposition | X_i, X_j | `X_i`, `X_j` | i dotted without descender; j has long descending hook. |
| 35, restriction displays | I with lower ≤ i; tilde i; M with lower ≤ X_i | `I_{\leq i}`, `\widetilde i`, `M_{\leq X_i}` | ≤ inside subscript, not a separate relation in the map. |
| 35, figure criterion | opposed-angle relation | `\unsure{\gtrless\|\bowtie}` | Same ambiguity as 34, marked at first occurrence. |
| 36, proof | primed indices i', j'; X', Y' | `X_{i'}`, `X_{j'}`, `i'`, `j'` | Primes on index letters in proof; primes on X/Y in hypotheses. No double prime substituted. |
| 36, proof display | set difference followed by intersection without parentheses | `\widetilde X_i\setminus\widetilde X_i\cap\widetilde X_j` | No grouping parentheses added. |
| 36, morphism conditions | circle over doubled left angle and circle between bars | same as 34 | Rechecked on a), b), c); unadorned ll occurs only below. |
| 36, last central display | parallel in source, opposed-angle in target | `X\parallel Y\overset{?}{\Longrightarrow}X'\gtrless Y'` | Deliberately retained unlike relations; both arrows have question marks. |
| 37, statement d) and corollaries | tilde on X followed by prime | `\widetilde X'` | Distinct from tilde F; prime kept outside the tilde. |
| 37, Corollaire 1 | Fig(M) | `\mathrm{Fig}(M)` | No mag subscript visible on this page; not supplied from 34. |
| 37, Cor 3 | two-headed equivalence arrows | `\Longleftrightarrow` | The live ≤ and parallel rows are equivalences; the preceding preserved-relations rows are one-way. |
| 37, dated margin | 12 or 11 .7.86 | `\unsure{12\|11}.7.86` | Day's second digit uncertain; July and 86 clear. |
| 38, corollaries and square | F,G; F',G'; tilde F/G | roman `F,G` and `\widetilde F`, `\widetilde G` | Capital G can resemble C, but opening curve and lower/right spur visible. Compared with the following pages; no alphabet change. |
| 38, example | Figél or Figéle | `\unsure{\mathrm{Fig\acute{e}l}\|\mathrm{Fig\acute{e}le}}` | One acute established in audit; final e uncertain. Annotation reads figures ensemblistes élémentaires. |
| 38, example and two bottom formulas | Mulomb or Muloms | `\unsure{\mathrm{Mulomb}\|\mathrm{Muloms}}` | Last stroke resembles b written as a tall closing curve; mark at first occurrence each page. |
| 38, bottom formulas | capital Omb, superscript circle | `\mathrm{Omb}`, `\mathrm{Omb}^\circ` | Capital O here unlike lower-case omb on 34; no unification of case. |
| 39, main equivalence | crossed existential | `\nexists Z\in M` | Vertical stroke crossing the E-shaped quantifier; negation preserved. |
| 39, middle proof | circled-ll canceled, circled-bars in pencil at left with pointer | `Z\deleted{\overset{\circ}{\ll}}\inserted{\mathrel{\vert\circ\vert}}Z` | Insertion follows pointer to the relation, not an independent margin assertion. |
| 39, lower third | lower-case x,y; L | `x,y\in L` | Keep lower case in this paragraph, distinct from upper-case X,Y above. |
| 40, axiom labels | Mag 1', Mag 2', Mag 3', Mag 4' | prime after numeral, in math for prime | Primes individually checked; no factorial or superscript 1 substituted. |
| 40, hierarchy | Magens1, Magens2 | `\unsure{\mathrm{Magens}}1`, `\mathrm{Magens}2` | Abbreviated handwritten sequence, not expanded. |
| 40, hierarchy | upward doubled arrows between successive rows | `\arrow[u,Rightarrow]` | Bottom-to-top direction; left braces accompanied by M/L notes. |
| 41, example 2 | lower-case mulomb/muloms, lower-case omb | `\mathrm{mulomb}`, `\mathrm{omb}` | Lower-case initial m/o is clear, distinct from 38–39. |
| 41, top map | Figél or Figéle | `\unsure{\mathrm{Fig\acute{e}l}\|\mathrm{Fig\acute{e}le}}` | The larger occurrence supports one acute over the first e; the audited reading agrees with scan38. |
| 41, example 3 | dark overwritten E' | `\unsure{E\|\mathbb{E}}'` | Multiple strokes may be a correction or deliberate doubling; no confident blackboard claim. Target E single-stroked. |
| 41, bottom | Figel | `\mathrm{Figel}` | No clear accent in either bottom occurrence. |
| 36, slanted left note; 37, dated margin; 39, final paragraph | paired small quote strokes | double TeX quotes | Around image inverse (endings uncertain), sous-mag., and quasi-ensembliste; added missing pairs in final review. |
| 34–41, capitals in headings, maps and formulas | M,L,I,F,G,X,Y,Z,E and Mag/Fig names | ordinary mathematical capitals; text names in upright roman | No script/calligraphic alphabet established; the first E′ on 41 is the sole unresolved ordinary/doubled candidate. Hand retracing is not automatically blackboard. |
| 35–36, indices and proof | i,j,i′,j′ | `i,j,i',j'` | j has a descender; i does not. Each occurrence checked, including the prime on the index rather than on X. |
| 34–41, short forms in prose | ens., ds, tjrs, i.e., isom., Mag, Fig | copied with local punctuation | Expansions below are editorial suggestions only; none is inserted in the transcription. |

## Doubts, in source order

The first candidate is the ink-based reading, not a contextual correction. Confidence concerns that reading. Approximate body-line counts begin below the manuscript page number; sloping marginal lines are counted separately. The block description and exact line number in the individual page `.tex` file provide additional locators. Every explicit uncertainty in the final page files is listed, including uncertainty inside cancellations. For a recurring ambiguous glyph, later unmarked occurrences on that page inherit the first occurrence’s candidates in the notation table. A single-candidate row means that no second defensible reading was recovered, not that the reading is certain.

| ID | Scan | Approx. line / block; page-file line | Reading | Other ink-allowed candidates | Confidence | Context preference and reason |
|---|---|---|---|---|---|---|
| D001 | 34 | main ll.1–5; Magasins triviaux; tex l.6 | `vérifie` | none securely recoverable | medium | The following que-clause is a verification claim; this supports vérifie, but the medial strokes are compressed. |
| D002 | 34 | main ll.8–9; Ce magasin ne satisfait; tex l.15 (canceled) | `tout` | none securely recoverable | low | The canceled or revised clause permits this short word; the local ink does not establish a stronger alternative. |
| D003 | 34 | main ll.8–9; Ce magasin ne satisfait; tex l.15 (canceled) | `fig.` | none securely recoverable | low | The crossed fragment is isolated. The neighboring figure vocabulary supports fig., but does not resolve the lost strokes. |
| D004 | 34 | main ll.8–9; Ce magasin ne satisfait; tex l.15 (canceled) | `éléts` | none securely recoverable | low | The following minimaux supports an abbreviation of éléments; the exact abbreviated ending is obscured. |
| D005 | 34 | main ll.10–12; X ll Y iff X le Y; tex l.21 | `\gtrless` | `\bowtie` | medium | The repeated relation contrasts with parallel and circle-bars. Context identifies its role, but does not decide between the two drawn opposed-angle forms. |
| D006 | 34 | main ll.10–12; X ll Y iff X le Y; tex l.22 | `,,,` | none securely recoverable | medium | Placement repeats the preceding tjrs satisfait line. The low repeated strokes look like ditto marks; their exact punctuation is uncertain. |
| D007 | 34 | upper-left margin ll.1–7; NB Conditions équivalentes; tex l.40 | `équivalentes` | none securely recoverable | low | The numbered conditions and the explicit comparison with preceding conditions support équivalentes; sloping compressed strokes remain uncertain. |
| D008 | 34 | upper-left margin ll.1–7; NB Conditions équivalentes; tex l.43 | `\mathrm{FigMag}` | `\mathrm{Fig}_{\mathrm{Mag}}` | low | Both identify the nearby figures notation. Context cannot decide baseline letters versus a subscript; the next occurrence visibly uses lower-case mag below the line. |
| D009 | 34 | upper-left margin ll.1–7; NB Conditions équivalentes; tex l.43 | `initiales` | `filtrantes` | low | The later closed-part wording on scan35 makes initiales plausible, but the margin ink remains compatible with filtrantes; no contextual substitution is made. |
| D010 | 34 | middle-left margin ll.1–6; Ces conditions impliquent; tex l.49 | `sont` | none securely recoverable | low | The following équivalentes needs a linking verb and supports sont; the word is reduced to strokes. |
| D011 | 34 | middle-left margin ll.1–6; Ces conditions impliquent; tex l.49 | `équivalentes` | none securely recoverable | low | The numbered conditions and the explicit comparison with preceding conditions support équivalentes; sloping compressed strokes remain uncertain. |
| D012 | 34 | middle-left margin ll.1–6; Ces conditions impliquent; tex l.51 (canceled) | `\gtrless` | none securely recoverable | low | A crossed relation sits next to the live ≤. The repeated opposed-angle sign is the best visual candidate, but the strike obscures its interior. |
| D013 | 34 | main ll.17–23; La condition Mag L 1; tex l.54 | `0` | `\varnothing` | medium | omb(X) is written as a set, so context favors the empty-set sign. The local round glyph could still be a zero; zero stays first because of its visible shape. |
| D014 | 34 | main ll.17–23; La condition Mag L 1; tex l.54 | `signifie` | none securely recoverable | medium | The following que-clause gives the meaning of Mag L 1; this favors signifie without settling every letter. |
| D015 | 34 | main ll.17–23; La condition Mag L 1; tex l.54 | `quasiment` | `pratiquement` | medium | Both can qualify jamais. The first strokes favor quasiment; context does not select between them. |
| D016 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `généraux` | none securely recoverable | low | The phrase familles de magasins permits généraux. The heavily compressed ending is not independently secure. |
| D017 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `combinatoires` | none securely recoverable | low | It modifies maquettes before de figures; combinatoires fits, but the slanted medial strokes are weak. |
| D018 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `appeler` | none securely recoverable | low | The following naming construction un tel magasin une maquette supports appeler; no additional word is supplied. |
| D019 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `simplement` | none securely recoverable | low | The local naming sentence permits simplement, but context does not establish the letters. |
| D020 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `m.` | none securely recoverable | low | The preceding maquette may explain m.; the abbreviation itself is too short to establish an expansion. |
| D021 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `squelette` | none securely recoverable | low | The final parenthesis concerns the maquette terminology. That makes squelette possible, but the visual reading remains low-confidence. |
| D022 | 34 | lower-left margin ll.1–10; Les magasins triviaux; tex l.59 | `catégorique` | none securely recoverable | low | The final parenthetical qualifier admits catégorique. Several strokes are merged; context alone is not decisive. |
| D023 | 34 | main ll.24–25; Figure indexée; tex l.62 | `munie` | none securely recoverable | medium | A figure followed by an isomorphism permits munie d’un isom.; compressed strokes keep the word doubtful. |
| D024 | 34 | main ll.26–27; I isomorphic to tilde F; tex l.65 (canceled) | `\in` | none securely recoverable | low | This small canceled sign precedes the I–F map. No surrounding syntax decides its former role. |
| D025 | 35 | main ll.4–5; qui est croissante; tex l.11 (canceled) | `comme` | none securely recoverable | low | The canceled connector before avec has no secure syntactic continuation. No contextual preference beyond the tentative visible word. |
| D026 | 35 | main ll.10–11; et b) varphi(I) est une figure; tex l.23 (canceled) | `Je dis que` | none securely recoverable | low | A discarded introduction to the two conditions could read Je dis que. Cancellation prevents a secure word-by-word reading. |
| D027 | 35 | main l.12; 1 degrees forall i j; tex l.27 | `\gtrless` | `\bowtie` | medium | The repeated relation contrasts with parallel and circle-bars. Context identifies its role, but does not decide between the two drawn opposed-angle forms. |
| D028 | 35 | main l.12; 1 degrees forall i j; tex l.27 (canceled) | `\text{i.e.}` | none securely recoverable | low | A short explanatory marker is canceled after the relation. i.e. is plausible, but the strike removes much of it. |
| D029 | 35 | main ll.14–15; La première condition; tex l.33 (canceled) | `a)` | none securely recoverable | low | The nearby lettered conditions support a), but the overwritten/canceled label is not fully visible. |
| D030 | 35 | main l.18; En d'autres termes; tex l.44 | `je` | none securely recoverable | medium | The phrase dis following this short word favors je. Its first stroke is reduced. |
| D031 | 35 | main l.23; tilde i equals I le i; tex l.56 (canceled) | `\mathrm{de}` | none securely recoverable | low | The canceled prefix before the displayed map resembles de; no intact surrounding syntax settles it. |
| D032 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `bijective` | none securely recoverable | low | The replacement = un isom. and the map support a discarded bijective condition; the crossed ending is uncertain. |
| D033 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `compatible` | none securely recoverable | low | The following aux relations d’ordre supports compatible; the strike crosses its middle. |
| D034 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `toujours` | `tjrs` | low | Both mean the same thing in the canceled parenthesis. Context cannot distinguish full spelling from abbreviation. |
| D035 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `aux` | none securely recoverable | low | It links compatible and relations; context favors aux, but only partial strokes survive. |
| D036 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `relations` | none securely recoverable | low | The following d’ordre supports relations. The cancellation leaves the medial letters uncertain. |
| D037 | 35 | main ll.24–25; soit bijective; tex l.59 (canceled) | `d'ordre` | none securely recoverable | low | The surrounding order-isomorphism wording supports d’ordre; the crossed fragment is not fully clear. |
| D038 | 35 | main ll.26–27; c) Si i not equal j; tex l.62 | `:` | none securely recoverable | medium | A separator occurs before the conclusion. The dot pattern could be a colon, but no alternative punctuation is securely recoverable. |
| D039 | 36 | main ll.1–3; En effet b) implique; tex l.5 (canceled) | `les` | none securely recoverable | low | It begins a canceled noun phrase before X_i; les is visually plausible, without an intact grammatical continuation. |
| D040 | 36 | main ll.1–3; En effet b) implique; tex l.5 (canceled) | `figures` | none securely recoverable | low | The discarded phrase concerns X_i. figures is plausible from surviving strokes, but not inferred as a mathematical requirement. |
| D041 | 36 | main ll.1–3; En effet b) implique; tex l.5 | `\gtrless` | `\bowtie` | medium | The repeated relation contrasts with parallel and circle-bars. Context identifies its role, but does not decide between the two drawn opposed-angle forms. |
| D042 | 36 | main ll.5–8; Or par b); tex l.11 (canceled) | `a)` | none securely recoverable | low | The nearby lettered conditions support a), but the overwritten/canceled label is not fully visible. |
| D043 | 36 | main ll.5–8; Or par b); tex l.11 (canceled) | `Y` | none securely recoverable | low | The nearby paired X/Y formulas favor Y. Retracing or cancellation prevents a confident glyph reading. |
| D044 | 36 | main ll.9–16; Variante polyédrale; tex l.14 (canceled) | `mag` | none securely recoverable | low | The discarded Morphismes de heading permits a shortened magasin word; the written ending is unclear and is not expanded. |
| D045 | 36 | main ll.9–16; Variante polyédrale; tex l.14 (canceled) | `est une` | none securely recoverable | low | Only a canceled phrase remains after Cela. No grammatical reconstruction is used to complete it. |
| D046 | 36 | main ll.9–16; Variante polyédrale; tex l.14 | `se fera` | none securely recoverable | medium | The following sans frais supports se fera; the compressed two-word group remains uncertain. |
| D047 | 36 | main ll.9–16; Variante polyédrale; tex l.14 (canceled) | `tout` | none securely recoverable | low | The canceled or revised clause permits this short word; the local ink does not establish a stronger alternative. |
| D048 | 36 | main ll.9–16; Variante polyédrale; tex l.14 | `ceci est` | `sera` | medium | Both would lead into automatique; the visible compressed group does not securely decide its length or internal division. |
| D049 | 36 | main ll.9–16; Variante polyédrale; tex l.14 (canceled) | `\widetilde E` | none securely recoverable | low | The overwritten sign before live tilde F resembles a tilde E. The replacement gives no proof of the earlier letter. |
| D050 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `comorphismes` | none securely recoverable | low | The subsequent discussion of image inverse and the later use of comorphisme support this reading; the slanted lettering is compressed. |
| D051 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `ressemble` | none securely recoverable | low | The words plus aux propriétés support ressemble; several letters are reduced to a continuous line. |
| D052 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `image` | `images` | low | The quoted expression with application favors singular image inverse. The terminal stroke is weak, so the plural remains an ink-level candidate. |
| D053 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `inverse` | `inverses` | low | The same quoted expression favors singular inverse; the final curve does not securely rule out a plural s. |
| D054 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `étalages` | `étalées` | low | The map between the two tilde F objects does not define the noun locally. Neither candidate is selected by context. |
| D055 | 36 | left margin ll.1–11; Peut-être vaut-il mieux; tex l.48 | `fixé un` | none securely recoverable | low | The following M→M′ permits fixé un, but does not establish all strokes in the slanted phrase. |
| D056 | 36 | right margin ll.1–10; Est-on trop exigeant; tex l.50 | `surtout` | `seulement` | medium | Both can qualify the case of a plongement. The ending and adjacent pointer are compressed; no decisive contextual preference. |
| D057 | 36 | right margin ll.1–10; Est-on trop exigeant; tex l.50 (canceled) | `aussi` | none securely recoverable | low | The inserted seulement revises a short crossed word. aussi is the best surviving reading, but replacement meaning does not prove it. |
| D058 | 37 | main ll.1–2; Il semble qu'il manque; tex l.5 (canceled) | `semble` | none securely recoverable | low | The canceled opening Il … qu’il manque supports semble; it remains obscured by the strike. |
| D059 | 37 | dated left margin ll.1–7; dated condition d); tex l.18 | `12` | `11` | low | Only the day’s second digit is uncertain. The neighboring month/year do not choose between 12 and 11. |
| D060 | 37 | dated left margin ll.1–7; dated condition d); tex l.18 | `rester` | `être` | low | Both fit devrait … facultative. Retracing favors rester slightly, but context cannot settle the verb. |
| D061 | 37 | dated left margin ll.1–7; dated condition d); tex l.18 | `facultative` | none securely recoverable | low | The note questions the necessity of condition d), which supports facultative; the slanted ending is compressed. |
| D062 | 37 | dated left margin ll.1–7; dated condition d); tex l.18 | `sous-mag.` | none securely recoverable | low | The sentence about closure and the nearby magasin terminology support sous-mag.; the exact abbreviated spelling remains uncertain. |
| D063 | 37 | dated left margin ll.1–7; dated condition d); tex l.18 | `\leq` | `\Delta` | low | The words fermés par favor an order relation such as ≤. The angular shape also admits Δ; its orientation is not regularized from context. |
| D064 | 37 | main ll.9–14; Immédiat par la proposition; tex l.24 (canceled) | `si` | none securely recoverable | low | The crossed short word lies between X,Y∈F and X≠Y. si is plausible, but its original syntactic role is unfinished. |
| D065 | 37 | main ll.9–14; Immédiat par la proposition; tex l.24 (canceled) | `Montrons que` | none securely recoverable | low | The canceled proof start has these plausible surviving strokes; the later live replacement does not settle them. |
| D066 | 37 | main l.15; Corollaire 2; tex l.27 (canceled) | `\gtrless` | `\bowtie` | low | The repeated relation contrasts with parallel and circle-bars. Context identifies its role, but does not decide between the two drawn opposed-angle forms. |
| D067 | 37 | main l.15; Corollaire 2; tex l.27 | `Y` | none securely recoverable | medium | The nearby paired X/Y formulas favor Y. Retracing or cancellation prevents a confident glyph reading. |
| D068 | 37 | main ll.18–20; En effet X relation Y; tex l.36 (canceled) | `on a` | none securely recoverable | low | A canceled proof step follows Si X parallel Y. on a is possible, but the strike obscures the connector. |
| D069 | 37 | main ll.18–20; En effet X relation Y; tex l.36 (canceled) | `on aura` | none securely recoverable | low | The crossed continuation before Inf(X,Y) admits on aura; the unfinished clause does not settle the reading. |
| D070 | 37 | main ll.23–27; deleted relations then two equivalences; tex l.46 (canceled) | `X\gtrless Y` | none securely recoverable | low | The canceled fragment resembles the relation already used in the neighboring rows. This is a visual candidate, not a restored mathematical condition. |
| D071 | 37 | right margin ll.1–3; se généralise; tex l.51 | `se généralise` | none securely recoverable | medium | The following aux sous-figures quelconques de F supports se généralise; the small right-margin writing remains uncertain. |
| D072 | 37 | main ll.28–31; La première; tex l.54 | `*` | none securely recoverable | medium | A small added mark is above première. A star is visually plausible; no matching reference is securely identified on these pages. |
| D073 | 37 | main ll.28–31; La première; tex l.54 | `équivalence` | none securely recoverable | medium | Two displayed equivalences precede the sentence. That supports équivalence; the compressed strokes remain doubtful. |
| D074 | 37 | main ll.28–31; La première; tex l.54 (canceled) | `provient` | none securely recoverable | low | The crossed verb resembles the live provient in the next sentence. That comparison favors this reading, without recovering every crossed stroke. |
| D075 | 37 | main ll.28–31; La première; tex l.54 | `vue` | `vu` | medium | The feminine équivalence favors vue, but the terminal e is weak. Both forms remain in the transcription. |
| D076 | 38 | main ll.1–2; Cor.4 Soient F G; tex l.5 | `\gtrless` | `\bowtie` | medium | The repeated relation contrasts with parallel and circle-bars. Context identifies its role, but does not decide between the two drawn opposed-angle forms. |
| D077 | 38 | main ll.1–2; Cor.4 Soient F G; tex l.5 | `Soient` | `Soit` | medium | Two objects F′ and G′ favor Soient grammatically; the ending is compressed and Soit remains a visual candidate. |
| D078 | 38 | main ll.11–17; J'ai pas l'impression; tex l.25 (canceled) | `ceci à supprimer` | none securely recoverable | low | The discarded phrase follows supprimer. The repetition makes this possible, but the cancellation leaves several letters unresolved. |
| D079 | 38 | main ll.19–20; M to Figele M; tex l.36 | `\mathrm{Fig\acute{e}l}` | `\mathrm{Fig\acute{e}le}` | medium | The annotation figures … élémentaires supports a Figél abbreviation but does not choose a terminal e. Only one acute is established in the larger occurrences. |
| D080 | 38 | main ll.19–20; M to Figele M; tex l.36 | `\mathrm{Mulomb}` | `\mathrm{Muloms}` | medium | The related Omb notation favors a final b, but its handwritten closing curve can resemble s. Case follows the local ink. |
| D081 | 39 | main l.2; deleted Mulomb equivalence; tex l.8 (canceled) | `\mathrm{Mulomb}` | `\mathrm{Muloms}` | low | The related Omb notation favors a final b, but its handwritten closing curve can resemble s. Case follows the local ink. |
| D082 | 39 | main ll.3–4; Mulomb disjointness equivalences; tex l.13 (canceled) | `M_{\overset{\circ}{\ll}X}` | none securely recoverable | low | The preceding page’s M subscript formula makes this plausible. The crossed local form still needs a doubt mark. |
| D083 | 39 | main l.6; Est-ce; tex l.21 (canceled) | `que` | none securely recoverable | low | It accompanies the canceled Est-ce. Grammar favors que, but the compact scribble is not securely readable. |
| D084 | 39 | added line below main l.8; i.e. X Y pas minoré; tex l.29 | `ds` | `dans` | medium | The sentence means the same with an abbreviation or the full word. Context cannot decide how many letters were written. |
| D085 | 39 | main ll.15–16; Ça ne marche que; tex l.38 (canceled) | `ne marche que` | none securely recoverable | low | The discarded Ça-clause permits these words, but the long strike removes important interior strokes; no completion follows them. |
| D086 | 39 | main ll.17–21; Mais notons que; tex l.41 (canceled) | `?` | none securely recoverable | low | The mark is retraced or partly canceled. Neither the punctuation role nor a different symbol is established by context. |
| D087 | 39 | main ll.17–21; Mais notons que; tex l.41 | `dérivables` | `divisibles` | low | The local pages do not supply a definition that selects either adjective. The visible middle letters permit both candidates. |
| D088 | 40 | main l.4; star disjointness definition; tex l.8 | `ds` | `dans` | medium | The sentence means the same with an abbreviation or the full word. Context cannot decide how many letters were written. |
| D089 | 40 | main ll.6–9; Les axiomes; tex l.14 | `?` | none securely recoverable | medium | The mark is retraced or partly canceled. Neither the punctuation role nor a different symbol is established by context. |
| D090 | 40 | main ll.6–9; Les axiomes; tex l.14 | `un .` | `un \textquotesingle` | low | The next line mentions primes, so a prime is contextually plausible. The local mark looks like a low dot; that reading stays first. |
| D091 | 40 | main ll.6–9; Les axiomes; tex l.14 | `près` | none securely recoverable | medium | The preceding à un … construction favors près. The small word’s accent and interior strokes are not fully secure. |
| D092 | 40 | main ll.6–9; Les axiomes; tex l.14 (canceled) | `est` | none securely recoverable | low | The canceled Mag 3′ clause permits est; the remainder of that discarded statement is not reconstructed. |
| D093 | 40 | main ll.6–9; Les axiomes; tex l.14 (canceled) | `\&` | none securely recoverable | low | A small canceled connector resembles an ampersand. No local wording uniquely decides it. |
| D094 | 40 | main ll.6–9; Les axiomes; tex l.14 (canceled) | `donne une condition supplémentaire` | none securely recoverable | low | The replacement résulte de revises the axiom’s status, making this discarded wording plausible. The long cancellation leaves it low-confidence. |
| D095 | 40 | main l.10; Autre; tex l.17 (canceled) | `Autre` | none securely recoverable | low | A short canceled heading resembles Autre. No continuation survives to decide it. |
| D096 | 40 | main ll.11–13; Proposition; tex l.20 | `(*)` | none securely recoverable | medium | The earlier displayed definition is labeled (*), which favors the same reference here; the local star is heavily retraced. |
| D097 | 40 | main l.16; Mag 3 prime; tex l.29 (canceled) | `\forall X,Y,\ X\overset{\circ}{\ll}Y` | none securely recoverable | low | Only fragments of the crossed Mag 3′ formula are visible. The quantifier, separator and repeated variables are tentative; no axiom is reconstructed from mathematics. |
| D098 | 40 | main ll.17–22; C'est pourtant aussi simple; tex l.32 | `pourtant` | none securely recoverable | medium | The enlarged word has a long initial stem and more strokes than tout. The sentence permits pourtant; its interior remains compressed. |
| D099 | 40 | main ll.17–22; C'est pourtant aussi simple; tex l.32 | `Magquens` | none securely recoverable | low | The following page24 reference and quasi-ensembliste row make a contraction plausible. The exact letter sequence is not fully resolved. |
| D100 | 40 | main ll.17–22; C'est pourtant aussi simple; tex l.32 | `noti-magasins` | `anti-magasins` | low | The hierarchy concerns kinds of structures, but that context does not securely identify this unusual compound. Both visual candidates remain. |
| D101 | 40 | main ll.23–26 / left labels; hierarchy of magasins; tex l.37 | `principales` | `princip.` | medium | Both fit bornes and have the same meaning. The question is full spelling versus abbreviation, which context cannot decide. |
| D102 | 40 | main ll.23–26 / left labels; hierarchy of magasins; tex l.39 | `\mathrm{Magens}` | none securely recoverable | medium | Its row is explicitly ensemblistes; this supports Magens as the written abbreviation, while its compressed middle remains uncertain. |
| D103 | 41 | main l.2; varphi M to Figele L; tex l.8 | `\mathrm{Fig\acute{e}l}` | `\mathrm{Fig\acute{e}le}` | medium | The annotation figures … élémentaires supports a Figél abbreviation but does not choose a terminal e. Only one acute is established in the larger occurrences. |
| D104 | 41 | main l.2; varphi M to Figele L; tex l.8 | `\mathrm{mulomb}` | `\mathrm{muloms}` | medium | The adjacent omb notation favors final b; the closing curve also permits s. The initial m is lower-case here. |
| D105 | 41 | main l.2; varphi M to Figele L; tex l.8 | `X` | none securely recoverable | medium | The element-map source is X, so context favors X in the target. The target glyph itself is heavily retraced. |
| D106 | 41 | main ll.3–6; Ce n'est défini; tex l.13 | `ds` | `dans` | medium | The sentence means the same with an abbreviation or the full word. Context cannot decide how many letters were written. |
| D107 | 41 | main l.11; disjoint mulomb equivalence; tex l.32 | `\varnothing` | none securely recoverable | medium | The other disjointness formulas use the empty-set sign, which favors it here. The extreme-right edge clips part of this particular sign. |
| D108 | 41 | main l.14; Cela nous montre; tex l.42 (canceled) | `montre` | none securely recoverable | low | The next sentence says nous montrent. That comparison supports montre in the crossed earlier start, but the ending is obscured. |
| D109 | 41 | main ll.20–22; Exemple 3; tex l.47 | `E` | `\mathbb{E}` | medium | The target E and the two bottom E occurrences are plain. That favors a retraced ordinary E, but intentional doubling cannot be excluded locally. |

## Apparent slips and irregularities kept as written

These are apparent irregularities, not claims that the author made an error. There is no securely established spelling slip that has been silently corrected.

| Scan / approximate location | As written and retained | Apparently intended, if any | Why it is noted |
|---|---|---|---|
| 34, main l.13 | `L = ens des éléments minimaux de X` | Possibly `de M` | The surrounding set is M; the visible final character looks X. It stays X. |
| 35, main l.18 | `X → X_i` | Possibly `i → X_i` | The indexing maps elsewhere use i. The local source glyph looks X; it is not corrected from the expected map. |
| 35, main ll.24–25 | `soit` followed by a canceled parenthesis and live `= un isom. d'ensembles ordonnés)` | No completed grammatical reconstruction | The final closing parenthesis follows a partly canceled opening clause. The deletion boundary and live closing mark are retained. |
| 36, bottom questioned display | `X parallel Y ?⇒ X′ opposed-angle Y′` | Possibly a parallel relation on the right, but not established | The two relation shapes differ visibly. The author also marks the implication with a question mark. |
| 38, main l.11 | `J'ai pas l'impression` | Formal `Je n'ai pas` would be a modernization | No n′ is securely visible; the colloquial wording is kept. |
| 40, main ll.6–7 | tentative `à un . près avec les '` | The dot may instead be a prime | This remains a reading doubt, not a repaired phrase. |
| 41, main l.13 | final `mulomb Y` without parentheses | Possibly `mulomb(Y)` | Earlier instances have parentheses; this one visibly lacks them. |

## Abbreviations encountered — proposed expansions only

Local punctuation varies and is preserved in the LaTeX. Entries here explain possible meanings, not instructions to expand the text.

| Written form | Proposed expansion / uncertainty |
|---|---|
| `Def`, `déf` | définition; an abbreviation label over a defining equivalence |
| `ens.`, `ens` | ensemble / ensembles, depending on the phrase |
| `ds` | dans; some occurrences cannot be distinguished from the compressed full word |
| `tjrs` | toujours |
| `i.e.`, `i.e` | id est |
| `NB` | nota bene |
| `isom.`, `isom` | isomorphisme; occasionally qualifying an ordered-set map |
| `il f et s` | il faut et suffit |
| `qed` | quod erat demonstrandum |
| `Cor.`, `cor`, `Cor` | corollaire |
| `Dém` | démonstration |
| `prop` | proposition |
| `p.` | page |
| `suiv.` | suivante |
| `Mag`, doubtful canceled `mag` | magasin(s), also the prefix of an axiom name |
| `Mag L 1`, `Mag L 2` | labels of magasin conditions; L is retained as a label, not expanded |
| `Fig`, `fig.` | figure(s) |
| `FigMag`, `Fig_mag` | figure(s) of a magasin, tentatively; the baseline/subscript variants are not regularized |
| `Figél`, `Figéle`, `Figel` | the annotation on 38 suggests figures élémentaires; accent/ending variations remain visible readings |
| `Magens` | probably a magasin-ensembliste axiom prefix; not expanded in the text |
| `Magquens` | probably a quasi-ensembliste magasin label; exact letters are doubtful |
| `omb`, `Omb` | probably ombre; these pages give set formulas but do not spell out the name |
| `mulomb`, `Mulomb` (alternative final s) | probably a multiple-ombre construction; exact expansion is not stated on these pages |
| `m.` | possibly maquette; very uncertain in the lower margin of 34 |
| `sous-mag.` | sous-magasin(s) |
| `éléts` | éléments; canceled abbreviation is doubtful |
| `appli.` | application |
| `val.` | valeurs |
| `princip.` | principales |
| `Inf` | infimum, as an operator in a canceled line |
| `OK` | conventional acknowledgment; not expanded |

## Legibility and limits

The displayed mathematics and large headings are generally more legible than the prose. The weakest readings are the slanted lower margin of 34, the canceled parenthesis on 35, the polyhedral sentence and margins on 36, the dated note on 37, the crossed starts on 39, and the canceled axiom and short parenthesis on 40. The right edge of a formula on 41 clips the final sign. All such regions are represented; readable guesses remain explicitly marked. No OCR, external transcription, or mathematical reconstruction was used. The second reading and the final comparison found corrections, but the remaining uncertainty marks should not be mistaken for resolved readings. The supplied preamble is unchanged and the files were not compiled.
