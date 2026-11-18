"""List every \\unsure{...} left in the corrected pages 16/037-053, with Hua's reading where consulted."""
BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/"
OUT = BASE + "out/MPL_16+47+54+44/MPL_16+47+54+44_16_scan%03d.tex"
DST = BASE + "work/MPL_16+47+54+44_16-037-16-053/unresolved.md"

# (scan, substring of the unsure content) -> Hua batch reading (his page = our scan - 1)
HUA = {
    (38, "j|i"): "Hua batch-02 p. 37 reads P^i here",
    (38, "n+1|n-1"): "Hua batch-02 p. 37 reads n-1",
    (38, "n-1|n+1"): "Hua batch-02 p. 37 reads n+1 and takes the whole sum with its range as struck",
    (38, "prem."): "Hua batch-02 p. 37 reads the boxed lines differently ('Par la meme verification ...')",
    (40, "2n|n"): "Hua batch-02 p. 39 reads 2n",
    (40, "i|j"): "Hua batch-02 p. 39 reads p^j_X",
    (40, "\\Lambda|L"): "Hua batch-02 p. 39 has no inserted operator",
    (40, "<|\\leq"): "Hua batch-02 p. 39 reads '0 <= i+j <= n-1'",
    (40, "\\forall"): "Hua batch-02 p. 39 reads 'pour les i+j <= n'",
    (40, "rest. en susp."): "Hua batch-02 p. 39 reads 'les memes [ill] [ill]'",
    (40, "=2n"): "Hua batch-02 p. 39 reads 2n as struck",
    (42, "i|*"): "Hua batch-03 p. 41 reads phi_*",
    (42, "polarisons"): "Hua batch-03 p. 41 reads 'qui [ill] dans ... L_X(x)1+1(x)L_Y' (not adopted: the ink has xi-shaped letters)",
    (42, "=n"): "Hua batch-03 p. 41: index illegible",
    (42, "1|2"): "Hua batch-03 p. 41 reads H^{2(n-1)}",
    (42, "pour une suite"): "Hua batch-03 p. 41 reads 'pour une suite decroissante de sections hyperplanes non singulieres' (first reading here)",
    (42, "des sections"): "Hua batch-03 p. 41: see the line 45 entry",
    (44, "i|1"): "Hua batch-03 p. 43 reads C^{n-1}_chi",
    (45, "n|O|0"): "Hua batch-03 p. 44: struck, illegible",
    (45, "Ces"): "Hua batch-03 p. 44 reads Ces",
    (45, "\\ell|l"): "Hua batch-03 p. 44: these two subscripts are not inked",
    (46, "dim|car"): "Hua batch-03 p. 45 reads car",
    (46, "thhe"): "Hua batch-03 p. 45 reads 'tthe'",
    (46, "thenproof"): "Hua batch-03 p. 45 reads 'thenproof'",
    (46, "\\tau"): "Hua batch-03 p. 45 reads tau-equi.",
    (46, "equiv."): "Hua batch-03 p. 45 reads 'tau-equi. = numer. equivalence'",
    (46, "H^i(X)"): "Hua batch-03 p. 45 reads H^i(X)",
    (47, "Soc."): "Hua batch-03 p. 46 reads Soc.",
    (47, "wihl"): "Hua batch-03 p. 46 reads will",
    (47, "biratmonally"): "Hua batch-03 p. 46 reads birationally",
    (48, "\\ell|1"): "Hua batch-03 p. 47: no subscript inked on C here",
    (48, "the|an"): "Hua batch-03 p. 47 reads 'an'",
    (48, "u|w"): "Hua batch-03 p. 47 reads u",
    (48, "h|b"): "Hua batch-03 p. 47 reads b",
    (49, "\\delta|d|j"): "Hua batch-03 p. 48 reads j",
    (50, "j|i"): "Hua batch-03 p. 49 reads i (2i, H^{i+2})",
    (50, "crittval"): "Hua batch-03 p. 49 reads crittval",
    (50, "+|*"): "Hua batch-03 p. 49 reads phi^+",
    (50, "C|A"): "Hua batch-03 p. 49 reads C",
    (51, "gpe"): "Hua batch-03 p. 50 reads gpe",
    (51, "{!}"): "Hua batch-03 p. 50 reads 'L,' without a mark",
    (51, "<|\\leq"): "Hua batch-03 p. 50 reads <=",
    (51, "J^i"): "Hua batch-03 p. 50 reads zeta^i (uncertain)",
    (51, "élémentaires|décomposition"): "Hua batch-03 p. 50 reads elementaires",
    (53, "prouvé"): "Hua batch-03 p. 52: illegible",
    (53, "p_i|\\rho_i"): "Hua batch-03 p. 52 reads p_i",
    (53, "p_j|\\rho_j"): "Hua batch-03 p. 52 reads p_j",
    (53, "p_k|\\rho_k"): "Hua batch-03 p. 52 reads p_k",
    (53, "n-k-j|n-k+j"): "Hua batch-03 p. 52 reads zeta^{n-k+j}",
    (53, "qui est nul"): "Hua batch-03 p. 52 reads '[ill] est nul sur'",
    (53, "de noyau|des mêmes"): "Hua batch-03 p. 52 reads 'des memes N'",
    (53, "ainsi|aussitôt"): "Hua batch-03 p. 52 reads 'aussitot' (struck)",
    (53, "coïncide"): "Hua batch-03 p. 52 reads 'coincide avec 1' (struck)",
}
NO_HUA = {37, 39, 41, 43, 52}  # typescripts and the EGA IV galley: Hua's project does not transcribe them


def unsures(line):
    out, i = [], 0
    key = "\\unsure{"
    while True:
        k = line.find(key, i)
        if k < 0:
            return out
        j, depth = k + len(key), 1
        while j < len(line) and depth:
            depth += {"{": 1, "}": -1}.get(line[j], 0)
            j += 1
        out.append(line[k + len(key):j - 1])
        i = j


rows, ell = [], {}
for scan in range(37, 54):
    for n, line in enumerate(open(OUT % scan, encoding="utf-8").read().split("\n"), 1):
        for u in unsures(line):
            if u.startswith("\\ell|\\chi"):
                ell.setdefault(scan, []).append(n)
                continue
            hua = "not transcribed by Hua's project (typescript / galley)" if scan in NO_HUA else ""
            for (s, sub), txt in HUA.items():
                if s == scan and ((sub.startswith("=") and u == sub[1:]) or (not sub.startswith("=") and sub in u)):
                    hua = txt
                    break
            rows.append("| %d | %d | `%s` | %s |" % (scan, n, u.replace("|", " / "), hua or "-"))

with open(DST, "w", encoding="utf-8") as f:
    total = len(rows) + sum(len(v) for v in ell.values())
    f.write("## Places still unresolved\n\n")
    f.write("Every `\\unsure{...}` left in the corrected pages (%d marks), plus one unmarked place. "
            "The first reading in each mark is the ink's; Hua's reading is given where his transcription "
            "covers the page (his page p is our scan p+1).\n\n" % total)
    f.write("**Recurring parameter glyph `\\unsure{\\ell|\\chi}` (%d marks, one reading question).** "
            "The typed letters carry an inked subscript and parameter, a slanted stroke with a hook at the top and a "
            "low crossing stroke: a cursive l with a collapsed loop or a chi. Hua batch-03 (pp. 43-49) reads chi "
            "throughout and says it is inked by hand; the handwritten subscripts in (v) on 16/045 l. 27 are short "
            "l-like strokes, and the mathematics (independence of the cohomology theory, char. 0 by Betti "
            "cohomology) is l-adic. Lines: %s.\n\n" % (
                sum(len(v) for v in ell.values()),
                "; ".join("16/%03d l. %s" % (s, ", ".join(str(x) for x in v)) for s, v in sorted(ell.items()))))
    f.write("| Scan | Line | Marked reading (alternatives separated by /) | Second witness |\n|---|---|---|---|\n")
    f.write("\n".join(rows) + "\n")
    f.write("| 52 | 37 | (unmarked) a faint pencil scribble in the left margin beside n° 5 (Compléments), "
            "a small loop and a wavy stroke; not transcribed, perhaps not writing | not transcribed by Hua's project |\n")
print(len(rows), "rows;", sum(len(v) for v in ell.values()), "ell|chi marks")
