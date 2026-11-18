# Second pass MPL_142_001-093, scans 038-056: apply the corrections and write the reports.
# The character U+00A4 stands for a backslash in every string below (no literal backslash in this file).
import hashlib
import os

B = chr(92)
NL = chr(10)
ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_142_001-093_unzipped/pages"
OUT = ROOT + "/second_pass/out/MPL_142_001-093"
SCANS = ["038", "039", "040", "041", "042", "044", "045", "046", "047", "048", "049", "050",
         "051", "052", "053", "054", "055", "056"]


def u(s):
    return s.replace("¤", B)


# (scan, old, new, expected number of occurrences)
CH = [
    ("038", "¤margin{¤uline{NB} les $b_i^¤omega$ reliant directement les $¤unsure{Q_i|R_i}$ sont ici inutiles}",
            "¤margin{¤uline{NB} les $b_i^¤omega$ reliant directement les $Q_i$ sont ici inutiles}", 1),
    ("038", "ayant les $¤unsure{¤Rightarrow|=}$ ¤deleted{¤unsure{dits}} sommets",
            "ayant les ¤unsure{$=$s|$¤Rightarrow$} ¤deleted{¤unsure{dits}} sommets", 1),
    ("038", "¤&P_¤infty^¤omega¤arrow[d,", "¤&P_{¤unsure{¤infty}}^¤omega¤arrow[d,", 1),
    ("041", "¤inserted{¤unsure{ces|ceci}¤ ¤unsure{signes|suppose}¤ ¤unsure{n'ont pas|implique}}",
            "¤inserted{¤unsure{ces|ceci}¤ ¤unsure{suppose|signes}¤ ¤unsure{implique|n'ont pas}}", 1),
    ("048", "¤operatorname{Rev¤,¤text{ét}}(¤widetilde¤Sigma^¤circ)", "¤operatorname{Rev¤,¤text{et}}(¤widetilde¤Sigma^¤circ)", 1),
    ("048", "¤operatorname{Rev¤,¤text{ét}}(¤Sigma^*)", "¤operatorname{Rev¤,¤text{et}}(¤Sigma^*)", 1),
    ("049", "en pratique peut-être des parties", "en ¤unsure{partant|pratique} peut-être des parties", 1),
    ("049", "¤unsure{J|I}", "J", 2),
    ("049", "¤unsure{notions|notations}", "¤unsure{notations|notions}", 1),
    ("050", "U_i¤cap¤overline T_{¤Sigma_{¤mathbb R},R_i}", "U_i¤cap T_{¤Sigma_{¤mathbb R},R_i}", 1),
    ("050", "_{T^U_{¤Sigma_{¤mathbb R},R_i}}", "_{TU_{¤Sigma_{¤mathbb R},R_i}}", 1),
    ("050", "U_i¤cap¤overline T¤Sigma_i=T^U¤Sigma_i", "U_i¤cap T_{¤Sigma_i}=TU_{¤Sigma_i}", 1),
    ("050", "on a $T^U¤Sigma_i¤simeq¤uline{¤varepsilon}$", "on a $TU_{¤Sigma_i}¤simeq¤uline{¤varepsilon}$", 1),
    ("050", "une orientation sur ¤unsure{le}, i.e.", "une orientation sur ¤unsure{le|la} ¤unsure{sphère}, i.e.", 1),
    ("050", "¤in¤unsure{J|I}", "¤in J", 2),
    ("050", "¤unsure{J|I}=", "J=", 1),
    ("051", "(20)¤qquad¤uline{¤omega}¤simeq¤{¤pm1¤}", "(20)¤qquad¤uline{¤bar¤omega}¤simeq¤{¤pm1¤}", 1),
    ("051", "¤text{i.e. on dispose }", "¤text{¤unsure{i.e.} on dispose }", 1),
    ("051", "¤margin{Il s'agit d'un ¤unsure{cercle}, ¤unsure{qui est déterminé|qui est déjà muni}",
            "¤margin{Il s'agit d'¤uline{¤unsure{arcs}} de ¤unsure{l'un des} ¤unsure{cercles}, ¤unsure{qui sont déterminés|qui est déjà muni}", 1),
    ("051", "b_i^¤omega:Q_i¤longrightarrow R_{¤omega i}^{¤omega'}", "b_i^¤omega:Q_i¤longrightarrow R_{¤omega'i}^{¤omega'}", 1),
    ("051", "savoir $R_{¤omega i}^{¤omega'}$", "savoir $R_{¤omega'i}^{¤omega'}$", 1),
    ("051", "¤inserted{$U_i¤subset$} $¤widetilde¤Sigma¤setminus¤Sigma^*$",
            "¤inserted{$U_i¤subset$} $¤unsure{¤partial}¤widetilde¤Sigma¤setminus¤Sigma^*$", 1),
    ("052", "qui sont simplement connexes -- obtenus", "qui soient simplement connexes -- obtenus", 1),
    ("052", "¤unsure{b_i|b_j}^{¤deleted{¤unsure{¤omega}}}", "b_i^{¤deleted{¤unsure{¤omega}}}", 1),
    ("052", "{$¤unsure{Q_k|Q_j}$}; ¤node[above] at (1.25,.22) {$¤unsure{Q_j|Q_k}$}",
            "{$Q_k$}; ¤node[above] at (1.25,.22) {$Q_j$}", 1),
    ("052", "¤varphi_{i,x}¤text{ ou }¤varphi_i&:", "¤text{¤unsure{resp.}}¤ ¤varphi_{i,x}¤text{ ou }¤varphi_i&:", 1),
    ("053", "en composant des isoms 30, suivant", "en composant des isoms (30) suivant", 1),
    ("054", "le point base $a$ ($=R_i^¤varepsilon$", "le point base $x$ ($=R_i^¤varepsilon$", 1),
    ("054", "pour préciser les groupes $¤Pi_1$", "pour préciser le ¤unsure{groupe|groupes} $¤Pi_1$", 1),
    ("055", "avec le ¤unsure{formulaire géométrique|formulaire de génération}", "avec le formulaire ¤unsure{familier|géométrique}", 1),
    ("056", "de $¤Pi_{03}$ en (32)", "de $¤Pi_{03}$ ¤unsure{dans|en} (32)", 1),
    ("056", "par transport des structures comme", "par transport ¤unsure{de structure|des structures} comme", 1),
]

CHANGES_MD = """# Second pass, MPL 142, scans 038–056: changes

Second pass by Claude Opus 5.5 at effort max (13 November 2026, no sub-agents), checked against the scan images. The first pass was made by GPT-6 Astra (ChatGPT Pro mode). The corrected page files are in `second_pass/out/MPL_142_001-093/` under their first-pass names; scans whose file is a plain copy of the first pass are listed below. Image names such as `038_b` mean `second_pass/img/MPL_142_001-093/MPL_142_001-093_scan038_b.jpg`. The enlarged crops are `second_pass/work/MPL_142_001-093_038-056/m01.png` … `m34.png` and `v01.png` … `v05.png`; each tile is labelled `scan:x0,y0,x1,y1:scale[:rotation]` in full-page pixels (script `montage.py`, specs `spec1.txt` … `spec4.txt`). The changes were applied by `apply_changes.py` in the same folder, which checks that every replaced string occurs exactly as often as expected and that brace balance is unchanged.

How the pages were read: both halves of every scan were read once; for 038–041 and 044 both halves were read a second time, for 045–047 the whole page plus the margin crops (m12, m15, m16), and for 042 only the crop of its first line (m17, tile 7). Scans 048–056 were read once in halves, with the crops listed in the table.

**Counts:** 18 scans, 30 changes (high 4, medium 15, low 11), 26 unresolved places. Scans 039, 040, 042, 044, 045, 046 and 047 are unchanged.

## Changes

| # | Scan | Place | First pass | Corrected | Evidence (what the image shows) | Conf. |
|---|---|---|---|---|---|---|
| 1 | 038 | NB margin beside the drawing VII | `… directement les $¤unsure{Q_i¤|R_i}$ sont ici inutiles` | `… directement les $Q_i$ sont ici inutiles` | 038_b: a round bowl with a tail, the same Q as in $Q_{¤omega'i}$ of the margin diagram above; no R leg. | medium |
| 2 | 038 | "IV ayant les … sommets" | `$¤unsure{¤Rightarrow¤|=}$` | `¤unsure{$=$s¤|$¤Rightarrow$}` | 038_b, m17 tile 2: two parallel strokes whose right end curls down into an s, no arrowhead. "=" is his sign for "même" in the same paragraph ("graphe de = nom"), so "les =s sommets" is "les mêmes sommets". | low |
| 3 | 038 | margin diagram, top object | `P_¤infty^¤omega` | `P_{¤unsure{¤infty}}^¤omega` | 038_a, m17 tile 1: under the P only a heavy dark blob; no legible ∞. Doubt mark added. | low |
| 4 | 041 | insertion above (*) | `¤unsure{signes¤|suppose}¤ ¤unsure{n'ont pas¤|implique}` | `¤unsure{suppose¤|signes}¤ ¤unsure{implique¤|n'ont pas}` | 041_b: the second word starts with s and two descending strokes (pp), no g; the third starts "im" with a p descender and an l ascender. Order of the alternatives changed; not settled. | low |
| 5 | 048 | (13), second and third functor | `¤operatorname{Rev¤,¤text{ét}}` (twice) | `¤operatorname{Rev¤,¤text{et}}` | m18 tile 6: the first "ét" has an accent; the second and third "et" have none. | medium |
| 6 | 049 | first paragraph | `en pratique peut-être des parties` | `en ¤unsure{partant¤|pratique} peut-être des parties` | v01 tile 2: p, a low stroke, a tall peaked t, then a loop with a long bar (his final t). There is no q descender, so "pratique" does not fit; "en partant …, et en les faisant" matches the gerund that follows. | medium |
| 7 | 049 | "(Σ, …)" and "… ⊂ Σ" | `¤unsure{J¤|I}` (twice) | `J` | 049_a, 049_b, m19 tile 4: a top bar and a stem curling left at the foot, his J of 044; his I on 046/047 has a foot bar. | medium |
| 8 | 049 | last sentence | `¤unsure{notions¤|notations}` | `¤unsure{notations¤|notions}` | v01 tile 3: after "no" two tall crossed t stems; "notions" has one t. | low |
| 9 | 050 | (18) | `U_i¤cap¤overline T_{¤Sigma_{¤mathbb R},R_i}` | `U_i¤cap T_{¤Sigma_{¤mathbb R},R_i}` | m19 tile 7: a plain capital T; the stroke above it is the descender of the q of "canonique" on the line above. | medium |
| 10 | 050 | (18), label under the brace | `T^U_{¤Sigma_{¤mathbb R},R_i}` | `TU_{¤Sigma_{¤mathbb R},R_i}` | m19 tile 8: T and U of the same height on the line, the subscript after them; the same TU as in (12) on 047. | high |
| 11 | 050 | margin (19) | `U_i¤cap¤overline T¤Sigma_i=T^U¤Sigma_i` | `U_i¤cap T_{¤Sigma_i}=TU_{¤Sigma_i}` | m20 tile 1, m27 tile 1: a T with Σ_i set lower as its subscript, then TU of equal height with subscript Σ_i; no overline, no raised U. | medium |
| 12 | 050 | margin (19), "on a …" | `$T^U¤Sigma_i¤simeq¤uline{¤varepsilon}$` | `$TU_{¤Sigma_i}¤simeq¤uline{¤varepsilon}$` | m27 tile 1, as in row 11. | medium |
| 13 | 050 | "une orientation sur …, i.e." | `sur ¤unsure{le}, i.e.` | `sur ¤unsure{le¤|la} ¤unsure{sphère}, i.e.` | v02 tiles 3 and 4: "sur l…" ends the line; the next line starts with a word s-p-h-è-r-e and a comma before "i.e.". The first pass left the word out. | low |
| 14 | 050 | (16) twice and "… = {0,1,∞}" | `¤unsure{J¤|I}` (three times) | `J` | 050_a, m27 tile 2: the same hooked J as on 049. | medium |
| 15 | 051 | cancelled (20) | `¤uline{¤omega}¤simeq¤{¤pm1¤}` | `¤uline{¤bar¤omega}¤simeq¤{¤pm1¤}` | v03 tile 1: the first omega has a bar on top as well as the underline (the roofed omega of 044 and 055); the omega of "ω̲ ⥲ ε̲" at the end of the line has none. | high |
| 16 | 051 | cancelled (20), after "{±1}," | `¤text{i.e. on dispose }` | `¤text{¤unsure{i.e.} on dispose }` | v03 tile 1: a short word with b, r and a dotted i, then a raised "de.", on a rising diagonal with an arrow up to the right; no clear "i.e.". Doubt mark added. | low |
| 17 | 051 | diagonal margin, opening | `Il s'agit d'un ¤unsure{cercle}, ¤unsure{qui est déterminé¤|qui est déjà muni}` | `Il s'agit d'¤uline{¤unsure{arcs}} de ¤unsure{l'un des} ¤unsure{cercles}, ¤unsure{qui sont déterminés¤|qui est déjà muni}` | v05 (rotated): "d'" is followed by an underlined short word (a or o, r, c, s), then "de" with "l'" above the next word; the next line begins "cercles," and "qui sont". The rest of the note was not re-read. | low |
| 18 | 051 | (24) | `b_i^¤omega:Q_i¤longrightarrow R_{¤omega i}^{¤omega'}` | `b_i^¤omega:Q_i¤longrightarrow R_{¤omega'i}^{¤omega'}` | m20 tile 3: the subscript of R is ω, apostrophe, i, with ω′ above the R. The geometry gives the same endpoint (notes, S2.2). | high |
| 19 | 051 | end of the paragraph after (24) | `savoir $R_{¤omega i}^{¤omega'}$` | `savoir $R_{¤omega'i}^{¤omega'}$` | m20 tile 4: the same subscript, with a mark between ω and i. | medium |
| 20 | 051 | last line | `$¤widetilde¤Sigma¤setminus¤Sigma^*$` | `$¤unsure{¤partial}¤widetilde¤Sigma¤setminus¤Sigma^*$` | v03 tile 2: a small ∂ (a reversed 6 with a top tail) right before Σ̃, apart from the curve of the insertion "U_i ⊂". | medium |
| 21 | 052 | first paragraph | `qui sont simplement connexes` | `qui soient simplement connexes` | v03 tile 4: six letters s, o, dotted i, e, n, t. | high |
| 22 | 052 | (27), second line | `¤unsure{b_i¤|b_j}` | `b_i` | m21 tile 5: a short stroke with a dot and a small foot to the right, no descender; the j of "j ∈ J∖{i}" below it descends. The mathematics wants b_j (N052.4); the ink has b_i. | medium |
| 23 | 052 | second drawing, the two Q labels | `¤unsure{Q_k¤|Q_j}`, `¤unsure{Q_j¤|Q_k}` | `Q_k`, `Q_j` | m22 tile 4: the left subscript has the looped k of the label R_k^{ω′} below it; the right one descends like the j of R_j^ω. | low |
| 24 | 052 | (29), between its two lines | (absent) | `¤text{¤unsure{resp.}}¤ ` before `¤varphi_{i,x}` | v03 tile 3: a small "resp." (r, e-s, p with descender, period) written between the two lines of (29), at their left. | low |
| 25 | 053 | sentence before the graph | `des isoms 30, suivant` | `des isoms (30) suivant` | m22 tile 5: "(" joined to the 3, then "0)"; no comma. | medium |
| 26 | 054 | paragraph after (31) | `le point base $a$` | `le point base $x$` | m23 tile 5: two back-to-back c strokes, his x (as in "x ∈ Σ̃_ω" on 052); not a closed a. | medium |
| 27 | 054 | paragraph after (31) | `pour préciser les groupes $¤Pi_1$` | `pour préciser le ¤unsure{groupe¤|groupes} $¤Pi_1$` | m23 tile 3: "le" with no s at the line end; the end of "groupe" is a stroke. | low |
| 28 | 055 | first line | `¤unsure{formulaire géométrique¤|formulaire de génération}` | `formulaire ¤unsure{familier¤|géométrique}` | m24 tile 2: the word after "formulaire" starts with the same looped f, then a short a-m group, a dotted i, a tall l, a dotted i and "er"; there is no g, é or q. | medium |
| 29 | 056 | first paragraph | `de $¤Pi_{03}$ en (32)` | `de $¤Pi_{03}$ ¤unsure{dans¤|en} (32)` | m25 tile 3: a d with a long horizontal tail (his "dans"), not the hump of "en". | medium |
| 30 | 056 | line before (36) | `par transport des structures comme` | `par transport ¤unsure{de structure¤|des structures} comme` | m25 tile 5: a short d with one stroke, and "structure" ends without a visible s; 049 has "par transport de structure". | low |

## Places still unresolved

Every other first-pass doubt mark in these scans was compared with the halves and left as it was, because the ink does not decide it. The places below were examined closely and could not be settled.

1. 038, margin diagram: the subscript of P^ω (now marked, row 3).
2. 041 and 042, equation labels (76|75) and (76′|75′): the second digit has a flat top stroke like his 5, but (75) is already used on 040; left as the first pass had them.
3. 041, the three-word insertion above (*) (row 4).
4. 044, a small word written above the start of "conformes" (two lines under "directs") is not in the transcription and could not be read.
5. 048, last line: "fictive"; the ending (a u-shaped v and a hump) can also be read "fiction".
6. 048, first line: "¤unsure{les¤|des} équivalences".
7. 049: "¤unsure{partant¤|pratique}" (row 6).
8. 049: "¤unsure{notations¤|notions}" (row 8).
9. 050, between margin (19) and "sur cette variété": a long stroke runs through or under a few words ending in "qui"; whether they are struck, and whether they belong to the margin or to the main text, is not settled; they are not transcribed.
10. 050, margin (19), "par les P_ε et Q_i": a struck superscript on P_ε is not transcribed.
11. 050: a crossed S-like sign at the left of "J = {0,1,∞}" is not transcribed.
12. 050, drawing: the quarter-arc labels a_i^{±±} were not re-checked one by one; the first pass's doubt marks stand.
13. 050: "¤unsure{le¤|la} ¤unsure{sphère}" (row 13).
14. 051, cancelled (20): the word after "{±1}," (row 16).
15. 051, diagonal margin: everything after "qui sont déterminés" (row 17).
16. 051, margin (27): the source superscript ω|ω′. With (24) corrected, ω is the type-consistent value (notes, N051.2); the ink is still undecided.
17. 052, margin to (27): the letters c|b in "supp c_i^ω ∪ supp c_i^{ω′}".
18. 052, bottom margin: "transition|trivialisation".
19. 052: the insertion "connexes et à" and the place it belongs.
20. 054, (32): a heavily struck sign between "G_3^*," and "P^+", under the insertion "×{1,τ}", is not transcribed.
21. 054, last relation of the presentation: σ̃_∞(σ̃_∞) = 1 | σ̃_∞(σ_∞) = 1.
22. 055, first line: SL(2,ℤ)|GL(2,ℤ).
23. 055, τ_∞(l_∞): the first factor l_0|l_0^{-1}.
24. 055, margin: ρ(ε_i|l_i′).
25. 056, last paragraph: "¤unsure{valeur}"; the ink looks like a word in é-l-…-nt (perhaps "élément"), which would not agree with "une".
26. 056, last paragraph: the sign after "correspondent à ω" (⇒ or a flourish).
"""

NOTES_MD = """# Notes checked: MPL 142, scans 038–056

This is the second-pass check by Claude Opus 5.5 at effort max (13 November 2026). It covers the first-pass research notes by GPT-6 Astra (ChatGPT Pro mode) in `returns/MPL_142_001-093_unzipped/MPL_142_001-093_notes.md`, items N038.1–N056.2 (scan 043 is blank). Each note was checked against the corrected transcription in this folder (see `MPL_142_001-093_038-056_changes.md`).

**Result:** 49 notes: 48 kept, 1 corrected (N051.2), none dropped. Four notes of my own are added at the end, labelled S2.

## First-pass notes

- **N038.1** (038, unproved claim: IV and VIII are two generating graphs of one groupoid). **Keep.** The quoted words are unchanged. The doubtful sign in "IV ayant les … sommets" now reads "=s" (his "=" for "même": "les mêmes sommets"), with "⇒" kept as the alternative; that reading states outright what the note infers, that IV and VIII have the same vertices.
- **N038.2** (038, reading question: the untilded d in (66′)). **Keep.** The image confirms d_i^ω without tilde in (66′) and in the product beside it, and tildes in (67′).
- **N039.1** (039, conjecture: β′ is eliminated). **Keep.** (69)–(70) and both "inutile!" margins are unchanged.
- **N039.2** (039, own idea: restriction under strict symmetry). **Keep.** Text unchanged.
- **N040.1** (040, unproved claim: independence of the relators). **Keep.** The marginal index "(ωi|i, ω′)" is still doubtful, as the note says.
- **N040.2** (040–041, unproved claim: eliminating ξ_1). **Keep.** (73)–(75) and the first display of 041 are unchanged.
- **N041.1** (041, unproved claim: β_1 = β′ only on the solution locus). **Keep.** The insertion above (*) now leans to "ces|ceci suppose implique" (alternatives reordered); the logic the note checks does not depend on it.
- **N041.2** (041, unproved claim: the identity behind (79)). **Keep, with a caution.** The note uses ε_0σ_∞ = ρ^{-1}, which is what (75′) needs (σ_∞ε_0^{-1} = ρ). That relation belongs to the notation of the calculations before 044. The new definition on 055, ε_0 = σ_∞ρ, gives σ_∞ε_0 = ρ instead, and with it (75′) would need σ_∞ρ^{-1}σ_∞ = ρ, which is false in PSL_2(ℤ). See S2.1.
- **N042.1** (042, own idea: the one-equation locus). **Keep.** Text unchanged.
- **N044.1** (044, unproved claim: Γ ≃ G_J × {1,τ}). **Keep.** The sign before 1 in "autom. +|≠ 1" is still undecided; the group S_3 × C_2 does not depend on it.
- **N044.2** (044, conjecture: equivalence with (J, ω̲̄)). **Keep.** Text unchanged.
- **N044.3** (044, unproved claim: uniqueness of the metric). **Keep.** Text unchanged.
- **N044.4** (044, unpursued implication: the Stokes convention). **Keep.** The end of the Stokes margin is still uncertain.
- **N045.1**, **N045.2**, **N045.3** (045). **Keep.** Text unchanged; the doubtful third vertex index R_{n|h} does not affect N045.2.
- **N046.1**, **N046.2**, **N046.3** (046). **Keep.** Text unchanged.
- **N046.4** (046–047, reading question: J and I). **Keep, updated.** The second pass reads the hooked J in "(Σ, J)" and "J ⊂ Σ" on 049 and in (16) and "J = {0,1,∞}" on 050. The letter I with a foot bar remains only in (10) on 046 and (12) on 047, which is where the note's point applies.
- **N047.1**–**N047.5** (047). **Keep.** Text unchanged.
- **N048.1**, **N048.2**, **N048.3** (048). **Keep.** The only change on 048 is the missing accent of "Rev et" (twice).
- **N049.1** (049, unproved claim: which 1-connected subsets). **Keep.** The corrected reading "en partant|pratique peut-être des parties 1-conn. de Σ*, et en les faisant ``déborder'' sur Σ̃" describes the procedure the note makes precise: start from 1-connected parts of Σ* and extend them over the boundary (S2.4).
- **N049.2** (049, conjecture: invariant constructions). **Keep.** "notations|notions" reordered; the programme is the same.
- **N050.1** (050, conjecture: the hemispheres and S_i^ε). **Keep.** The NB is unchanged; (19) now reads S_i^ε ∈ U_i ∩ T_{Σ_i} = TU_{Σ_i}, which is the two-point restriction the note relies on.
- **N050.2** (050–055, unpursued implication: three orientation torsors). **Keep, strengthened.** The cancelled (20) on 051 reads ω̲̄ ≃ {±1} (an orientation of Σ), not ω̲ ≃ {±1}: he fixed the orientation of the surface to get ω̲ ⥲ ε̲ and then struck it out. That is the note's statement that fixing a surface orientation identifies the first two torsors.
- **N051.1** (051, unproved claim: the torsor claims). **Keep.** Text unchanged.
- **N051.2** (051, reading question: the type of b̃). **Correct.** The inconsistency came from a misreading of (24). The ink gives b_i^ω : Q_i → R_{ω′i}^{ω′} (also at "savoir R_{ω′i}^{ω′}"). Then b_i^{ω′} : Q_i → R_{ωi}^{ω}, and b̃_i^ω = b_i^ω (b_i^{ω′})^{-1}, read right to left (first (b_i^{ω′})^{-1}), runs R_{ωi}^{ω} → R_{ω′i}^{ω′}: the endpoints declared in margin (27), with source superscript ω (the ink there is still between ω and ω′). Read left to right the product is not composable. Corrected note: (24) and (27) are type-consistent under right-to-left composition; the comparison with the direction drawn on 064 remains to be made.
- **N051.3** (051, reading question: endpoints of c and d). **Keep.** With "∂" now read before Σ̃, the last sentence puts the endpoints of the c and d paths on the boundary ∂Σ̃: right for d (endpoint S_i on U_i), and in plain conflict with (25) for c.
- **N051.4** (051, unpursued implication: τ fixes b but inverts local loops). **Keep.** Text unchanged.
- **N052.1** (052, unproved claim: simple connectivity). **Keep.** The opening sentence reads "cinq ouverts … qui soient simplement connexes", a requirement; "Ce sont bien des ouverts simplement connexes" is the claim the note's proof is for.
- **N052.2** (052, unproved claim: density and connectedness). **Keep.** The margin is unchanged.
- **N052.3** (052, reading question: the cut removes its centre). **Keep.** Text unchanged.
- **N052.4** (052, reading question: b_i or b_j). **Keep, updated.** The ink gives b_i (a short dotted stroke, no descender), so the written formula repeats b_i for every j. That the intended cut is b_j is the note's research point; the transcription keeps the ink.
- **N052.5** (052, unproved claim: maximality). **Keep.** Text unchanged.
- **N053.1**, **N053.2** (053). **Keep.** The reference now reads "isoms (30)".
- **N054.1**, **N054.2** (054). **Keep.** The base point after (31) is x, not a; this does not touch the presentation.
- **N055.1** (055, reading question: −I in the loop product). **Keep.** The first line now reads "avec le formulaire familier dans Π̃_{0,3} ≃ SL|GL(2,ℤ)": the table is presented as familiar formulas; the SL|GL doubt and the note's −I point stand.
- **N055.2** (055, unproved claim: the automorphism table). **Keep.** Text unchanged.
- **N056.1**, **N056.2** (056). **Keep.** "dans (32)" and "de structure|des structures" do not affect them.

## Notes of my own (S2)

- **S2.1** (041 and 055, unpursued implication; mine). The second line of (75′) on 041 needs σ_∞∘ε_0^{-1} = ρ, that is ε_0 = ρ^{-1}σ_∞, in the notation of 038–042. On 055 the new notation defines ε_0 = σ_∞ρ = (ρ^{-1}σ_∞)^{-1}: the new ε_0 is the inverse of the element (75′) uses, so l_0 = ε_0^2 becomes the inverse of the old square. This is one concrete case of the change of notation announced in the 044 margin ("Attention, notations …"): formulas from 038–042 should not be carried into the notation of 044–056 without this check. Confidence: high for the algebra; the definition of ε_0 before 038 was not checked in this block.
- **S2.2** (051, own idea; mine). The corrected endpoint of b_i^ω is forced by the geometry. Q_i = −R_i lies on the arc of Σ_ℝ between R_{ωi} and R_{ω²i}; going from Q_i in the direction ω one reaches R_{ω²i} = R_{ω′i}, arriving along the tangent direction ω′ (the one pointing back to Q_i), that is at the boundary point R_{ω′i}^{ω′} of (18). This gives a check of the ink of (24) that does not use the ink. Confidence: high, given (16), (18) and ω acting on J by the cyclic order.
- **S2.3** (051, 055, 056, unpursued implication; mine). The cancelled (20) and the pinning r = (i, ω, ω̄) of 055 use the same datum: an orientation ω̄ of Σ identifies ω̲ with ε̲ through ω̲ ∧ ε̲ ∧ ω̲̄ = 1 (044). The counts on 056 follow from the product J × ω̲ × ω̲̄ (12 elements) with ε = ω ∧ ω̄: for a fixed pole P_ε, i and ω are free and ω̄ is determined (six choices); for a fixed Q_i, ω and ω̄ are free (four); with ω̄ fixed, three and two. This is the elementary count behind N056.2. Confidence: high.
- **S2.4** (049 and 052, own idea; mine). "en partant … des parties 1-conn. de Σ*, et en les faisant déborder sur Σ̃" suggests a precise class of base objects: an open 1-connected A ⊂ Σ* together with the open boundary arcs of U_i in the closure of A in Σ̃. The five regions of 052 (Σ̃ minus cuts) are of this kind, and the section argument of N049.1 then applies once the boundary conventions questioned in N052.3–N052.4 are fixed. Confidence: medium.
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    by_scan = {}
    for scan, old, new, n in CH:
        by_scan.setdefault(scan, []).append((u(old), u(new), n))
    report = []
    for scan in SCANS:
        name = "MPL_142_001-093_scan%s.tex" % scan
        with open(os.path.join(SRC, name), encoding="utf-8", newline="") as f:
            text = f.read()
        bal0 = text.count("{") - text.count("}")
        nrep = 0
        for old, new, n in by_scan.get(scan, []):
            c = text.count(old)
            if c != n:
                raise SystemExit("scan %s: expected %d occurrence(s), found %d: %r" % (scan, n, c, old))
            text = text.replace(old, new)
            nrep += 1
        bal1 = text.count("{") - text.count("}")
        if bal0 != bal1:
            raise SystemExit("scan %s: brace balance changed %d -> %d" % (scan, bal0, bal1))
        if "¤" in text:
            raise SystemExit("scan %s: placeholder left" % scan)
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
            f.write(text)
        report.append("%s changes=%d sha256=%s" % (name, nrep, hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]))
    for fname, body in (("MPL_142_001-093_038-056_changes.md", CHANGES_MD),
                        ("MPL_142_001-093_038-056_notes_checked.md", NOTES_MD)):
        body = u(body)
        with open(os.path.join(OUT, fname), "w", encoding="utf-8", newline="") as f:
            f.write(body)
        report.append("%s bytes=%d rows=%d" % (fname, len(body.encode("utf-8")), body.count(NL + "| ")))
    print(NL.join(report))


if __name__ == "__main__":
    main()
