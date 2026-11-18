# Second pass, block MPL_16+47+54+44_16-037-16-053: changes

Cote 16, "Formalisme algébrique des correspondances ...", scans 37-53 (the end of the folder). Checker: Claude (Claude Opus 5.5 at effort max), 17 Nov 2026, from the scan images. First pass: GPT-6 Astra (ChatGPT Pro mode).

What the block holds: Grothendieck's handwritten sheets on the hyperplane-section reduction of C(X) (scans 38, 40, 42) and on the Lemme of the ring of correspondences (51, 53), written on the backs of reused leaves; three upside-down pages of an English typescript on injective modules and Ext (37 = p. -8-, 39 = -7-, 41 = -5-); an EGA IV galley with his corrections (43, "- IV - 977 - 12 -"); the carbon copies of two typed letters to Coates, dated in his hand "4.1.67" (44-47) and "6.1.1966" (48-50); a Bourbaki "Tribu n° 65" page (52).

Method: both halves of every scan read against the first pass line by line; 15 montages of enlarged crops (rotated where needed) for every place where the first pass and my reading disagreed or a symbol decides the mathematics. Crops and scripts: `second_pass/work/MPL_16+47+54+44_16-037-16-053/`. All corrections were applied by exact replacement, each asserted by its count (`apply.py`). Line numbers below are those of the corrected files (same as the first pass, except scan 52 from line 14 on, one line fewer).

Second witness (lesson 1): Michel Hua's project, `transcripts/16/batch-02.fr.tex` (his pp. 37, 39 = our scans 38, 40) and `batch-03.fr.tex` (his pp. 41, 43-50, 52 = our scans 42, 44-51, 53; his page p is our scan p+1). His project does not transcribe the typescripts (37, 39, 41, 52) or the EGA IV galley (43). I read the ink first and opened his text only for the places still open and the places where my reading and the first pass disagreed; nothing of his conventions or wording is copied. Where his reading settles or supports a place, the evidence column says so.

## Counts

- Scans: 17, all checked.
- Change rows: 61. Reading changes: 48 (high 10, medium 27, low 11). Convention rows: 13 (typographic normalisation to the first treatment, high).
- Unresolved places (`\unsure` marks): first pass 197 (not counting the 42 repetitions of its watermark guess on scan 42); after my image pass 186; after consulting Hua 187 (his reading settled 4: scan 42 l. 44 two marks, 51 l. 9 "élémentaires", 53 l. 3 "Alg"; it put 5 confident first-pass readings in doubt: 42 l. 6 and l. 34, 50 l. 9 twice, 53 l. 17). Plus 1 unmarked place (scan 52, pencil scribble). 50 of the marks are one recurring question, the parameter glyph ℓ|χ of the letters.
- Edition matters on these scans: only @1109 (16/039, Matlis 1958 for the injective-hull statements), a companion cross-reference with no reading involved; it is carried into the notes check.

## Conventions (lesson 2)

The first pass treats four features in two ways; I used the treatment of their first occurrence and normalised the rest (13 rows marked "convention"):
- typed φ (the typewriter ø of the letters) as `\varphi`, as on scan 45 and for every handwritten φ in the cote; `\phi` on 46, 49, 50 changed;
- the typed product letter as `X\mathrm{x}X`, as on 44-45 (doubts file: "typed x glyph retained as upright x, not supplied cross sign"); `\times` on 46, 47, 49, 50 changed (typed products only; the handwritten × of scan 42 stays `\times`);
- a plain dash without arrowhead as `\mathbin{-}`, as on 42 and 45 (and 16/020); `\mathrel{-}` on 46, 48, 49, 51, 53 changed;
- the handwritten date at the head of a letter as `\margin{...}`, as on 44; scan 48 changed.

## Change table

| # | Scan | Place | First pass | Corrected | Evidence (what the image shows) | Confidence |
|---|---|---|---|---|---|---|
| 1 | 37 | l. 8, proof of Lemma 3.3, twice | `\overline{\{\unsure{X\|x}\}}` | `\overline{\{X\}}` | Page rotated 180° and enlarged 1.5×: in both braces a capital X, as tall as the X of "x∈X" on the same line; Prop. 3.4 (l. 16) has a small x. A typing error of the typescript (the point is x), kept as typed. | high |
| 2 | 38 | l. 2, first glyph | `\deleted{\unsure{A}}` | `A` | A bold, overtraced capital A with its crossbar and no strike line: a label, as "A) ... B)" in the formulary of scan 33. Hua batch-02 p. 37 reads "A)". | medium |
| 3 | 38 | l. 2 | `(\unsure{\alpha})` | `(\alpha)` | A loop with crossing tail (α), as the (α) of scan 36; Hua reads (α). | medium |
| 4 | 38 | l. 4 | `L_X^jP^i(X),` | `L_X^jP^{\unsure{j\|i}}(X),` | Enlarged 2×: the superscript of P is the same looped glyph with descender as the j of L just before it; at l. 12 and l. 19 the superscript of P is a short i. Hua reads P^i here. | medium |
| 5 | 38 | l. 8 | `\uline{L_X^jP^i(X)}` | `\uline{L_X^jP^j(X)}` | Enlarged 1.6×: the same j-glyph on P as on L. Hua reads L^j_X P^j(X). His slip for P^i, kept as written. | medium |
| 6 | 38 | l. 9 | `\coprod_{i\geq n+1}P^{\unsure{j\|i}}(X)\oplus E^{n-1}` | `\coprod_{i\geq n+1}P^j(X)\oplus E^{(n-1)}` | The same j-glyph on P; the exponent of E opens with a parenthesis, as on the left of the line, its end cut by the sheet edge. Hua reads P^j(X) ⊕ E^{(n-1)}. | medium |
| 7 | 38 | l. 12, subscript | `i+j\leq n-1` | `i+j=n-1` | Enlarged 2.5×: two short parallel strokes, an equals sign, not his ≤. Hua reads i+j = n-1. | medium |
| 8 | 38 | l. 15 | `P^i(X)+E^{n-1}=\coprod` | `P^i(X)+E^{n-1}\simeq\coprod` | Enlarged 2.5×: a wavy upper stroke over a straight one (≃). Hua reads ≃. | medium |
| 9 | 38 | l. 49, left margin | `\Longleftarrow\quad\Lambda_Y^m\varphi^*=\varphi^*\Lambda_X^m(\operatorname{id}-\bar\Sigma)` | `\Lambda_Y^m\varphi^*=\varphi^*\Lambda_X^m(\operatorname{id}-\bar\Sigma)\quad\Longleftarrow` | Enlarged 2×: the double arrow runs from the brace to the margin formula, its head at the left end touching the formula; on the page the formula stands left of the arrow, as its target. | high |
| 10 | 40 | l. 5, under the left underbrace | `\substack{L_X\Lambda_X\\=\\...}` | `\substack{L_X\Lambda_X\\\Vert\\...}` | A vertical double stroke (equality written vertically), rendered `\Vert` by the first pass for the same sign on l. 26. | high |
| 11 | 40 | l. 36 | `\inserted{\unsure{L\|\Lambda}}` | `\inserted{\unsure{\Lambda\|L}}` | Enlarged 1.1×: two strokes meeting at the top, the left one long (Λ-shaped); the margin "L?" (l. 39) queries it. Hua shows no inserted operator. Both alternatives kept, order changed. | low |
| 12 | 42 | l. 6 | `\text{égal à }` | `\text{égal : }` | Enlarged 1.1×: two dots one above the other after "égal". Hua reads "égal :". | medium |
| 13 | 42 | l. 6 | `\Lambda_X\varphi_i` | `\Lambda_X\varphi_{\unsure{i\|*}}` | A small stroke with dots under φ, unlike the clear stars of l. 12. Hua reads φ_*. | low |
| 14 | 42 | l. 34 | `p_n^X` | `p_{\unsure{n}}^X` | The index under p is a small unclear mark. Hua: illegible. | low |
| 15 | 42 | l. 44, struck | `X\unsure{\sim}Y,\ \unsure{Y_\alpha}` | `X\times Y,\ Y\times` | Enlarged 1.5-2×: a cross between X and Y and after the second Y, as in "X×Y" on l. 38. Hua reads "X×Y, Y×" struck. | medium |
| 16 | 42 | l. 45 | `les uns sont \unsure{des sections} des autres, hyperplans non singuliers.` | `\unsure{pour une suite décroissante de sections hyperplanes non singulières\|les uns sont des sections des autres, hyperplans non singuliers}.` | Enlarged 2×: the long word of the second line is one word, d + accent, a c early and a t near its end ("décroissante"), then "de" and a word ending in s; the last line ends "singuli..s". Hua reads "pour une suite décroissante de sections hyperplanes non singulières", which parallels the typed (v) on 16/045 l. 29. Both readings kept. | low |
| 17 | 42 | ll. 48-89, repeated light-blue printing | `\unsure{Condor\|Cordor\|Concorde}` (42 nodes) | `Gevaert` | The diagonal printing reads "Gevaert" plainly in several places on both halves (the paper's brand). | high |
| 18 | 43 | l. 9, left margin | `\uline{\unsure{Virer\|Vider}} (ii) sauf \unsure{raison} sérieuse !` | `\uline{\unsure{Vider\|Virer}} (ii) sauf raison sérieuse !` | Rotated 62° and enlarged: the third letter of the underlined word has a tall ascender (d); "raison" reads r-a-i-s-o-n. | medium |
| 19 | 43 | l. 7 | `l'homomorphisme canonique ;` | `l'homomorphisme \unsure{canpnique\|canonique} ;` | Enlarged 2.4×: the typed word is c-a-n-p-n-i-q-u-e, a p with descender in fourth place. | medium |
| 20 | 45 | l. 2 | `\unsure{A\|Q}_{...}(X,` | `A_{...}(X,` | Enlarged 2.5×: a pointed A with a heavier overstrike. Hua reads A. | medium |
| 21 | 45 | l. 6 | `(verieté` | `(varieté` | Enlarged 2.5×: v-a-r-i-e-t-é. | high |
| 22 | 45 | l. 29 | `suite décroissante` | `suite décorissante` | Enlarged 2.5×: the typed word is d-é-c-o-r-i-s-s-a-n-t-e. Hua reads "décorissante". | high |
| 23 | 46 | l. 4 | `(X\times Y)`, `(Y\times Z)` | `(X\mathrm{x}Y)`, `(Y\mathrm{x}Z)` | Convention (typed product). | high (convention) |
| 24 | 46 | l. 17 | `(\mathrm{i})\longrightarrow(\mathrm{iii})` | `(\mathrm{i})\Longrightarrow(\mathrm{iii})` | Enlarged 1.1×: a double-shafted arrow, as after (iii) on the same line. Hua reads ⟹. | medium |
| 25 | 46 | l. 22, twice | `in arbitrary dimension` | `in arbitray dimension` | Enlarged: a-r-b-i-t-r-a-y, the last letter overtyped; "In arbitrary caracteristics" on the same line is spelled in full. Hua reads "arbitray". | high |
| 26 | 46 | l. 15 | `\phi` (6) | `\varphi` | Convention (typed φ). | high (convention) |
| 27 | 46 | l. 11 | `\mathrel{-}` (3) | `\mathbin{-}` | Convention (plain dash). | high (convention) |
| 28 | 47 | l. 3 | `the $\pi_1$ for a surface` | `the $\pi_i$ for a surface` | Enlarged 3×: the subscript has a separate round dot (i), unlike the flagged 1 of π_1 in the list on 16/046 l. 22 (enlarged 2.5× for comparison). Hua reads π_i. | medium |
| 29 | 47 | l. 7 | `Kleimann's` | `Kleiman\deleted{n}'s` | Enlarged 2.5×: the letter before 's is a dark overstrike, an n typed over with x, the typist's deletion used throughout these letters. Hua reads "Kleimann's". | medium |
| 30 | 47 | l. 5 | `$X\times Y$` | `$X\mathrm{x}Y$` | Convention (typed product). | high (convention) |
| 31 | 48 | l. 3 | `6.1.1966` (plain line) | `\margin{6.1.1966}` | Convention (date at the head, as on 44 l. 2); the reading 6.1.1966 confirmed enlarged 3×. | high (convention) |
| 32 | 48 | l. 7 | `` ``motive-theoretically'' `` | `` ``motive-theor\deleted{\unsure{i}}etically'' `` | Enlarged 2.5×: a letter x-ed out between r and e. Hua reads "theorietically". | medium |
| 33 | 48 | l. 9 | `the following conditions` | `the follwing conditions` | Enlarged 1.6×: f-o-l-l-w-i-n-g. Hua reads "follwing". | high |
| 34 | 48 | l. 15 | `\unsure{the} algebraic isomorphism` | `\unsure{the\|an} algebraic isomorphism` | Enlarged 3×: typed "an" under an inked overwrite. Hua reads "an". | low |
| 35 | 48 | ll. 13, 15 | `\mathrel{-}` (4) | `\mathbin{-}` | Convention (plain dash). | high (convention) |
| 36 | 49 | l. 5 | `preliminaray` | `preliminar\deleted{\unsure{a}}y` | Enlarged 1.3×: one letter between r and y x-ed out. Michel Hua checked "preliminary condition" on the facsimile (batch-03 header). | medium |
| 37 | 49 | ll. 7, 9 (3 places) | `\unsure{\delta\|d}` | `\unsure{\delta\|d\|j}` | Enlarged 2.5×: an overtyped letter with a bowl and a descender, also in the typed insertion. Hua reads j. | low |
| 38 | 49 | l. 11 | `\phi` | `\varphi` | Convention (typed φ). | high (convention) |
| 39 | 49 | l. 11 | `I(X\times X)` | `I(X\mathrm{x}X)` | Convention (typed product). | high (convention) |
| 40 | 49 | ll. 7, 9 | `\mathrel{-}` (2) | `\mathbin{-}` | Convention (plain dash). | high (convention) |
| 41 | 50 | l. 11 | `\unsure{crittcal\|critical}` | `\unsure{crittval\|critical}` | Enlarged 3×: the letter before "al" is a v, not a c; overtyped letters in the middle. Hua reads "crittval". | medium |
| 42 | 50 | l. 15 | `follows from the conjunction of` | `follows from the conjuction of` | Enlarged 2.5×: c-o-n-j-u-c-t-i-o-n. Hua reads "conjuction". | high |
| 43 | 50 | l. 9 | `if $2j\geq n-1$` ... `$H^{j+2}(X)$` | `if $2\unsure{j\|i}\geq n-1$` ... `$H^{\unsure{j\|i}+2}(X)$` | Enlarged 1.2×: both letters are overtyped (bold, j and i superposed). Hua reads 2i and H^{i+2}(X), which agrees with "H^i(Y)" at the end of the definition. | low |
| 44 | 50 | l. 11 | `\phi` (2) | `\varphi` | Convention (typed φ). | high (convention) |
| 45 | 50 | ll. 13, 15 | `\times` (11) | `\mathrm{x}` | Convention (typed product). | high (convention) |
| 46 | 51 | l. 3 | `du groupe abélien` | `du \unsure{gpe\|groupe} abélien` | Enlarged 1.5×: a word of three letters (g, p, e), as short as "du". Hua reads "gpe". | medium |
| 47 | 51 | l. 9 | `les facteurs \unsure{élémentaires} $\unsure{\xi^j\|\xi_j}P^i$` | `les facteurs élémentaires $\xi^jP^i$` | Enlarged 1.4×: the j stands at the top right of ξ, level with the top of P; the word opens with his é-loop, as on l. 17. Hua reads "facteurs élémentaires ζ^jP^i". | medium |
| 48 | 51 | l. 19 | `les $\unsure{\xi^j\|\xi_j}P^i$` | `les $\xi^jP^i$` | Same placement as l. 9. Hua reads ζ^jP^i. | medium |
| 49 | 51 | l. 17 | `facteurs \unsure{décomposition\|élémentaires}` | `facteurs \unsure{élémentaires\|décomposition}` | Enlarged 2.2×: the word opens with the same é-loop (read d' by the first pass) as "élémentaires" on l. 9. Hua reads "élémentaires". | low |
| 50 | 51 | l. 8, margin | `(et vice \unsure{versa})` | `(et vice versa)` | Rotated 32° and enlarged 2.2×: "(et vice versa)". | medium |
| 51 | 51 | l. 15 | `\mathrel{-}` | `\mathbin{-}` | Convention (plain dash). | high (convention) |
| 52 | 52 | ll. 7, 9, 13 | `\unsure{Filting\|Fitting}` (3) | `Filting` | Typed F-i-l-t-i-n-g in all three places (enlarged); a typing error for Fitting, kept. | high |
| 53 | 52 | l. 13 | `\margin{\unsure{!}}` as a paragraph after "de $\Omega_A(B)$ :" | `\margin{\unsure{!}}` before "p. f." in "une algèbre de p. f. sur $A$" | Enlarged 3×: the marks (a short upright with a dot below, and a short bar) stand in the interline above "p. f." of that line. | medium |
| 54 | 53 | l. 3 | `\in\unsure{\operatorname{Alg}\|A}` | `\in\operatorname{Alg}` | Enlarged 1.1×: A, an l crossed by the loop of the g, and g. Hua reads "Alg". | medium |
| 55 | 53 | l. 7 | `k'\unsure{\leq\|<}k` | `k'\leq k` | Enlarged 2×: his ≤ (ε-like), unlike the plain < of "k'<k" on l. 3. Hua reads ≤. | medium |
| 56 | 53 | l. 7 | `H^{\unsure{j\|i}}` | `H^j` | Enlarged 2×: the superscript has the descender of the j in "j≠k" just after it. Hua reads H^j. | medium |
| 57 | 53 | l. 11 | `u_{\unsure{k\|n}}` | `u_k` | Enlarged 2×: the subscript has the form of the k of T_k. Hua reads u_k. | medium |
| 58 | 53 | l. 13 | `\deleted{\unsure{ainsi}}` | `\deleted{\unsure{ainsi\|aussitôt}}` | Struck, not settled by the ink. Hua reads "aussitôt". | low |
| 59 | 53 | l. 17 | `\inserted{de noyau $N$,}` | `\inserted{\unsure{de noyau\|des mêmes} $N$,}` | Enlarged 2.4×: under the stroke, "d.." and a word of humps. Hua reads "des mêmes N". | low |
| 60 | 53 | l. 17 | `\deleted{\unsure{coïncide à} ...}` | `\deleted{\unsure{coïncide à\|coïncide avec} ...}` | Struck. Hua reads "coïncide avec 1". | low |
| 61 | 53 | l. 3 | `\mathrel{-}` | `\mathbin{-}` | Convention (plain dash). | high (convention) |

## Places checked and left as the first pass read them

Enlarged and confirmed, or a second-witness reading not adopted because the ink does not support it:
- 38 l. 2 "s'identifie" (Hua "s'interprète": the word ends -fie with the f's descender); l. 11 "(qui n'est d'ailleurs autre que ... comme il se doit)" (Hua "qui n'a d'... isomorphe par ... il y a droit": not supported); l. 13 "On retrouve"; l. 55 φ^* twice (Hua concurs).
- 39 k(𝔭) and 𝔭 both handwritten script p; "0 ⊆ E^1".
- 40 l. 2 "On conclut du premier groupe" (Hua "des premières ... que": not supported); l. 19 "Aussi" (Hua "Ainsi": ambiguous, kept); l. 21 "projection sur partie évanescente" (Hua "supplémentaire": the word opens with an accented é); l. 9 "[Plus gén." kept as read by the first pass and Hua, though my enlargement (2.6×) shows an initial with a loop at the top and a small second letter, closer to "Rem": a doubt not marked in the text, noted here.
- 42 l. 16-17 ξ_X⊗1 + 1⊗ξ_Y (Hua L_X⊗1 + 1⊗L_Y: the letters are ξ-shaped); l. 36 "Donc est algébrique" (a short word between Donc and algébrique; Hua illegible).
- 44-50 the parameter glyph, kept `\unsure{\ell|\chi}` (Hua χ); 44 l. 9 C^{n-\unsure{i|1}} (Hua C^{n-1}_χ).
- 48 l. 17 Hamilton-Cayley: the exponents of the first line have an open bowl (h), the "(-1)^b" of the second line a closed b; kept `\unsure{u|w}^{\unsure{h|b}}` (Hua u^b, u^{b-1}). l. 9 C_{\unsure{\ell|1}}: a typed mark stands under the C (Hua: no subscript inked).
- 50 l. 11 "pretend\inserted{ed}ly": typed p-r-e-t-e-n-d-l-y with "ed" inked above (Hua "prentenedly": not supported).
- 53 l. 13 "(donc descendante" (Hua "ou": the word opens with d).
- 51 l. 9 L\unsure{!}: a slanted stroke with a small loop at its foot (Hua "L,").

