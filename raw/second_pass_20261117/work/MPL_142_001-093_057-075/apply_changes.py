"""Second pass MPL_142_001-093, scans 057-075: apply the checked changes and write the outputs.

Every replacement must occur exactly the stated number of times; brace balance must be unchanged;
no control characters may enter the text. Writes the 18 page files and the changes table once.
"""
import os, sys, re

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = BASE + "/returns/MPL_142_001-093_unzipped/pages/MPL_142_001-093_scan{}.tex"
OUT = BASE + "/second_pass/out/MPL_142_001-093"
SCANS = ["057", "058", "059", "060", "061", "062", "063", "064", "066",
         "067", "068", "069", "070", "071", "072", "073", "074", "075"]

# (scan, place, old, new, count, evidence, confidence)
CH = [
("057", "after “structures,”, replacement words",
 r"\deleted{ce qui fait} donc pour $\forall$",
 r"\deleted{ce qui fait} \inserted{donc pour} $\forall$", 1,
 "“donc” and “pour” are written small above the struck “ce qui” and “fait”, with a caret stroke descending from them; they are an insertion, not line text (m057, tile 2).", "medium"),
("057", "diagram (37), top-left cell",
 r"\&\Pi_{03}\arrow[dl,",
 r"\unsure{\checkmark|\vee}\&\Pi_{03}\arrow[dl,", 1,
 "A heavy v-shaped tick stands left of Π_{03} in the empty top-left cell of the diagram (m057, tile 4); the first pass left it out. Whether it is a tick or a caret is not clear.", "medium"),
("058", "first display",
 r"u_r:\widetilde{\mathcal G}_3\xrightarrow{\sim}\widetilde{\mathcal G}_J",
 r"u_r:\widetilde{\mathcal G}_3\xrightarrow{\sim}\widetilde{\mathcal G}_3", 1,
 "Both subscripts are the same two-bowled 3, identical to the subscript of G̃_3 two lines below; the J of G̃_J on 057 is a hooked ɟ with a flat top (m058a, tile 1; m058d, tile 3).", "high"),
("058", "left diagonal NB, word after “lacets”",
 r"\unsure{tournant|fondés}",
 r"\unsure{standard|tournant|fondés}", 1,
 "Rotated crops show an s, a crossed t, a hump, an ascending d and a tail (“st–d–”), the form of “standard” on 059 and 062; there is no initial f or t-o-u (m058c; m_final, tile 6).", "low"),
("059", "stabiliser sentence",
 r"font un groupe",
 r"\unsure{font un} groupe", 1,
 "Three short word units (g·-d, a–d, d–s) stand before “gr·-pe ≃ Z/2×Z/2”; the first pass's two words do not account for them, and no reading was found (m059b, tile 3; m070, tile 6).", "low"),
("060", "line 1",
 r"\operatorname{int}(\tau_\infty)$",
 r"\operatorname{int}(\unsure{\sigma\tau_\infty|\tau_\infty})$", 1,
 "Inside the second parenthesis a closed round letter precedes τ_∞; its top may join the bar of the τ (m060, tile 1).", "low"),
("060", "(40), struck sign before σ̃_i",
 r"=\deleted{\unsure{\tau}}\underbrace",
 r"=\deleted{\unsure{\varepsilon|\tau}}\underbrace", 1,
 "The struck sign is an open ε crossed by a vertical stroke, unlike the τ of “τσ_i” just below (m060, tile 3).", "low"),
("061", "“voisinage immédiat”",
 r"au ``voisinage'' immédiat de ces",
 r"au ``voisinage\unsure{''|``} immédiat'' de ces", 1,
 "A double closing quote stands after “immédiat”; between the two words there is only a single high stroke (m062, tile 1).", "medium"),
("063", "NB, the standard region",
 r"$\widetilde\Sigma_{r_0}$ standard",
 r"$\widetilde\Sigma_{\unsure{r_\varepsilon|r_0}}$ standard", 1,
 "After the r of the subscript stands a heavy ε-shaped glyph, not the small round 0 of R_0, S_0 on the same page (m063, tile 2).", "low"),
("063", "orientation clause",
 r"un isom $\varepsilon\simeq\uline{\varepsilon}$",
 r"un isom $\unsure{\uline{\varepsilon}|\uline{\omega}}\simeq\uline{\varepsilon}$", 1,
 "The first sign is underlined like the second; it is a small open letter (ε or ω). Two lines lower the same isomorphism is written “ω̲ ≃ ε̲” (m063, tile 3).", "low"),
("063", "last paragraph, identification map",
 r"via $\psi_r$,",
 r"via $\unsure{\Psi_r|\psi_r}$,", 1,
 "The letter has a wide cup whose arms reach well beyond the stem, the form of the capital Ψ_r of (42) on 062 and of the left label of (44) on 064; the ψ of (43) on the same page is narrow (m063, tile 4).", "medium"),
("064", "(44), left diagonal label",
 r"\unsure{\Psi|\psi}_i^\omega",
 r"\Psi_i^\omega", 1,
 "A large Ψ with a wide cup, clearly bigger than the lowercase ψ labels of the vertical and right arrows of the same diagram (064, top half; compare m063, tile 4).", "medium"),
("064", "insertion after the second diagram",
 r"\inserted{via $\widetilde b_{i\omega}$.}",
 r"\inserted{Via $\widetilde b_{i\omega}$.}", 1,
 "The V is a capital, as tall as the ascender of the b (m_final, tile 4).", "medium"),
("066", "pencil note, top left",
 r"\margin{(\unsure{38|39} pages)}",
 r"\margin{(\unsure{38|39} \unsure{pages|pags})}", 1,
 "Only p, a, g and a final s are visible; there is no e (m066, tile 1). The same form as the pencil note on 002 in the first block.", "low"),
("066", "title, line 2",
 r"les actions du groupe de Galois",
 r"les actions \unsure{de groupes|du groupe} de Galois", 1,
 "The word after “actions” has the d-and-loop form of “de” in “de groupoïdes” two lines lower, not the two humps of “du”; the next word ends in “pe” with a final hook (m066, tile 3).", "low"),
("066", "title, line 3",
 r"\unsure{compactifiés|complétés}",
 r"compactifiés", 1,
 "The second half of the word has a tall t and an f with a descender loop; “complétés” has neither (m066, tile 3).", "medium"),
("067", "paragraph 1",
 r"avant tout aux cas où",
 r"avant tout \unsure{des|aux} cas où", 1,
 "The word begins with an ascending d-stroke; “aux” has no ascender (m067, tile 1).", "medium"),
("067", "paragraph 3",
 r"(ou $=$ seulement topologique)",
 r"(ou \unsure{$\overline{\mathrm m}$|$=$} seulement topologique)", 1,
 "The sign is a wavy m with a bar above it, not his two parallel strokes for “même” (m067, tile 3).", "low"),
("067", "last paragraph",
 r"directement en fonction du $\mathbb C$-schéma",
 r"directement en termes du $\mathbb C$-schéma", 1,
 "The word starts with a crossed t, then e, two humps and “es”; the tall stroke through it is the descender of the q of “qui” in the line above, and there is no initial f (m070, tile 5; m067, tile 2).", "medium"),
("068", "after “et qui \\deleted{déf}”",
 r"pour $\forall x\in X=X(\mathbb C)$",
 r"pour tt $x\in X=X(\mathbb C)$", 1,
 "Two parallel slanting stems joined by a crossbar: his “tt”, as in “pour tt x ∈ I∖x_0” on 071, not the converging V of ∀ (m067, tile 4).", "medium"),
("071", "paragraph 2, first words",
 r"Il apparaît que sous des conditions",
 r"\unsure{Je trouvait|Il apparaît} que sous des conditions", 1,
 "The first word is a J with a crossbar followed by a small e-loop; the verb has no long pp descenders and ends “-vait” (m071, tile 1).", "low"),
("071", "struck item after “En termes des g_l(u),”",
 r"\deleted{\unsure{$g_l(u)$}},",
 r"\deleted{\unsure{$f_l(u)$|$g_l(u)$}},", 1,
 "The struck symbol has a tall ascender above the line, like his f and unlike the g just before it (m071, tile 2).", "low"),
("072", "struck paragraph, first line",
 r"La formule (6) peut s'exprimer",
 r"La formule \unsure{(10)|(6)} peut s'exprimer", 1,
 "A 1 stands after the opening parenthesis, followed by a retraced 0 or 6 (m072, tile 1).", "low"),
("072", "struck paragraph, display label",
 r"(12)\qquad g_l:\Gamma",
 r"\unsure{(17)|(12)}\qquad g_l:\Gamma", 1,
 "The second digit has a top bar and a slanting stem with no base stroke: a 7 (m072, tile 2).", "low"),
("072", "struck paragraph, insertion",
 r"\inserted{sur qui opère $\Gamma$,}",
 r"\inserted{\unsure{avec op. de|sur qui opère} $\Gamma$,}", 1,
 "The insertion reads as a short word, an abbreviation ending in a point and “de” before Γ (m072, tile 3); “opère” is not visible.", "low"),
("072", "struck paragraph, five occurrences",
 r"\widehat{\Pi}_1(X,y)",
 r"\widehat{\pi}_1(X,y)", 5,
 "The vertex group is written with a small, curled lowercase π under the hat, as in (8) on 070; the Π̂_1(X) of the Hom subscripts is the capital (m_final, tiles 1–3).", "medium"),
("075", "(22)",
 r"\overset{\psi=\Pi_1(f)}{\unsure{\mathbin{-}|\longrightarrow}}",
 r"\overset{\psi=\Pi_1(f)}{\longrightarrow}", 1,
 "At 3× the right end of the line under ψ=Π_1(f) carries a small arrowhead (m075, tile 1).", "medium"),
("075", "first struck clause before (28)",
 r"est bijectif}",
 r"\unsure{soit|est} bijectif}", 1,
 "The struck verb after Π_0(X) has four letters, s-o-i-t, as in “soit tel que” on the same line (m_final, tile 5).", "low"),
]

UNRESOLVED = [
"**057**: “le transport des structures”: the endings of “de(s)” and “structure(s)” are strokes; the singular of the label of (37) is possible.",
"**057**: “la donnée du repère r”: “du|des” and the ending of “repère” not settled.",
"**057**: exponent of τ in the definition of G̃_J (kept sg g|α; “sg g” and an α are written over each other); the 0 of “α=0” carries a bar; “g^{(ε)}_ε = id_ε” kept with its doubt.",
"**057**: struck word after “vu que”: a g followed by a stroke (“gr”?); kept as g.",
"**058**: top insertion: the strokes read “a–n = ε p–r(r)”; neither “au = ε près” nor “avec = ε pour r” fits every stroke (kept).",
"**058**: left margin, order of “ψ_r, ψ_{r'}”: both subscripts carry a mark; the order may be ψ_{r'}, ψ_r as on 059.",
"**058**: NB: first superscript of ψ_ε (i,ω | ω,ω); the phrase “(donc au détriment de …)”; the struck word before “l'orientation” begins with a d (“suivant” kept).",
"**058**: “p.r. au|du grand cercle méridien” (the y-descender of “symétrie” crosses the letter).",
"**059**: “Donc” before u_r: the ink begins with a crossed t (“thi–a,”); no reading found.",
"**059**: “font un groupe”: see change 5.",
"**059**: base point Q_∞|R_∞ (overwritten); struck superscript of ψ_{r'} (ε or ω).",
"**060**: under (40), “autour du grand cercle” may read “autour des grand cercles”; kept.",
"**060**: “capturent”: the letter after p is a dotted i or a t-bar; kept.",
"**061**: “et se trouve sur|par suite sur Σ̃”: the ink reads “et se(s) tr· un sur”; neither alternative fits every stroke.",
"**061**: “tronc|vrai”: only “tronc” fits the letters; kept with its doubt.",
"**061**: label of the hatched region in the figure (first pass D̃_r): a heavily retraced capital with top and bottom bars.",
"**061**: last argument of (41) Σ_+|Σ_r and the exponents of S_i in the contour.",
"**062**: drawing label C_r|Σ_r (the ink looks like C_r); superscript of Π in (42).",
"**063**: first R of the paragraph (R_i^ω; the superscript is retraced, ∞- or ωω-like); “point|points R”.",
"**066**: 38|39; the faint pencil mark at the top right (kept as a doubtful 5).",
"**068**: a parenthesised digit, possibly “(4)”, stands among the rotated margin lines left of the Hom display, which has no label in the transcription; the isolated “b” after “transcendant :”.",
"**069**: connectors of “^uλ : ^ux — ^uy si λ : x → y”: both end in a hooked y with no clear head; the first pass gives only the second an arrow.",
"**070**: struck word before “par les formules (8)” (kept as “fonctoriquement”; f, e, l, o, n, c, t, a descender and -es are visible); “rationnels sur X|K” (the ink is an X).",
"**071**: diagram labels l'|l and l''|l'; overwritten left member of (10).",
"**072**: “développer”; label of the iterated display (13)|(12) (074 cites it as “(12)”); index n−2.",
"**073**: labels (14), (16), (17) (overwritten digits).",
"**074**: margin “nécessaire”, “donnant”, “X|x_0”; the struck word before “chemin” may be “du” rather than “au”.",
"**075**: target π_i|π_α in (25); double-struck or plain I.",
]

def bal(s):
    return s.count("{") - s.count("}")

def code(s):
    s = s.replace("|", "\\|")
    runs = [len(m) for m in re.findall(r"`+", s)]
    n = (max(runs) + 1) if runs else 1
    fence = "`" * n
    pad = " " if (s.startswith("`") or s.endswith("`") or n > 1) else ""
    return fence + pad + s + pad + fence

def main():
    texts = {}
    for n in SCANS:
        with open(SRC.format(n), encoding="utf-8", newline="") as f:
            texts[n] = f.read()
    orig_bal = {n: bal(t) for n, t in texts.items()}
    for i, (n, place, old, new, cnt, ev, conf) in enumerate(CH, 1):
        for s in (old, new):
            if any(ord(c) < 32 for c in s):
                sys.exit(f"change {i}: control character in string {s!r}")
        if bal(old) != bal(new):
            sys.exit(f"change {i}: brace balance differs between old and new")
        k = texts[n].count(old)
        if k != cnt:
            sys.exit(f"change {i} ({n}): old string found {k} times, expected {cnt}: {old!r}")
        texts[n] = texts[n].replace(old, new)
    for n in SCANS:
        if bal(texts[n]) != orig_bal[n]:
            sys.exit(f"scan {n}: brace balance changed")
    os.makedirs(OUT, exist_ok=True)
    for n in SCANS:
        with open(OUT + f"/MPL_142_001-093_scan{n}.tex", "w", encoding="utf-8", newline="") as f:
            f.write(texts[n])
    conf_count = {"high": 0, "medium": 0, "low": 0}
    for c in CH:
        conf_count[c[6]] += 1
    changed = sorted({c[0] for c in CH})
    unchanged = [n for n in SCANS if n not in changed]
    L = []
    L.append("# Second pass, MPL 142, scans 057–075: changes")
    L.append("")
    L.append("Second pass by Claude Opus 5.5 at effort max (13 November 2026), checked against the scan images. "
             "The first pass was made by GPT-6 Astra (ChatGPT Pro mode). The corrected page files are in "
             "`second_pass/out/MPL_142_001-093/` under their first-pass names (scan 065 is blank and has no file). "
             "The evidence images are the enlarged crops `second_pass/work/MPL_142_001-093_057-075/m057.png` … `m_final.png`; "
             "each tile is labelled `scan:x0,y0,x1,y1:scale[:rotation]` in full-page pixels. The script that applied the "
             "changes is `apply_changes.py` in the same folder; it checked that every replaced string occurs exactly the "
             "stated number of times and that brace balance is unchanged.")
    L.append("")
    L.append(f"**Counts:** {len(SCANS)} scans, {len(CH)} changes (high {conf_count['high']}, medium {conf_count['medium']}, "
             f"low {conf_count['low']}); {len(UNRESOLVED)} places unresolved. Scans {', '.join(unchanged)} are unchanged.")
    L.append("")
    L.append("## Changes")
    L.append("")
    L.append("| # | Scan | Place | First pass | Corrected | Evidence (what the image shows) | Conf. |")
    L.append("|---|---|---|---|---|---|---|")
    for i, (n, place, old, new, cnt, ev, conf) in enumerate(CH, 1):
        o = code(old) + (f" (×{cnt})" if cnt > 1 else "")
        L.append(f"| {i} | {n} | {place} | {o} | {code(new)} | {ev} | {conf} |")
    L.append("")
    L.append("## Places still unresolved")
    L.append("")
    for i, u in enumerate(UNRESOLVED, 1):
        L.append(f"{i}. {u}")
    L.append("")
    with open(OUT + "/MPL_142_001-093_057-075_changes.md", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))
    print("changes:", len(CH), conf_count, "unresolved:", len(UNRESOLVED), "unchanged:", unchanged)

main()
