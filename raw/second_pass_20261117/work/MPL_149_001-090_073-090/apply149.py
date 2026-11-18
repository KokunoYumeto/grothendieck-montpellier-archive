"""Apply the second-pass corrections to the first-pass page files of MPL_149_001-090, scans 073-090,
and write every page of the block (changed or not) to second_pass/out/MPL_149_001-090/ under its first-pass name.
Each targeted replacement must match exactly once; each global replacement must match at least once.
If any check fails, the script stops without writing anything."""
import pathlib, sys

ROOT = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SRC = ROOT / "returns/MPL_149_001-090_unzipped/pages"
OUT = ROOT / "second_pass/out/MPL_149_001-090"

QG = [r"\unsure{q|g}", r"\unsure{g|q}"]

# (old, new) pairs: exactly one occurrence each, applied in order
R = {
    73: [
        (r"s'annule sur $I_x$, i.e.", r"s'annule \unsure{sur|dans} $I_x$, i.e."),
        (r"est définie en $x$. Ceci implique", r"est définie en $x$. Ceci \unsure{impliquera|implique}"),
    ],
    74: [
        (r"(que la section $\unsure{\psi|\varphi}$ de", r"(que la section $\psi$ de"),
        (r"$(0,\unsure{1})$", r"$(0,1)$"),
    ],
    76: [
        (r"on supp. que $(g,\nu)\neq(0,1)$", r"on suppose $(g,\nu)\neq(0,1)$"),
        (r"\deleted{disjointe}\inserted{de $X/S$ distincte des} $\unsure{q|g}_i$",
         r"\deleted{disjointe}\inserted{de $X/S$ distincte} des $\unsure{q|g}_i$"),
        (r"\deleted{Considérons} \inserted{Donc si $\eta=S\setminus\{s\}$}",
         r"\deleted{Considérons} \inserted{\deleted{Donc}} \inserted{Si $\eta=S\setminus\{s\}$}"),
    ],
    77: [
        (r"Soit $\unsure{\mu|n}=\operatorname{long}", r"Soit $\mu=\operatorname{long}"),
    ],
    78: [
        (r"-- car $\unsure{\nu|\mu}$ est la longueur", r"-- car $\nu$ est la longueur"),
    ],
    79: [
        (r"les ``sections de décomposition'' de l'extension", r"les ``sections de 2ième espèce'' de l'extension"),
        (r"1-\pi-E_U\longrightarrow E_S-1", r"1-\pi-E_U-E_S-1"),
    ],
    80: [
        (r"(16)\quad 0\longrightarrow\operatorname{Pic}(S)_n\longrightarrow H^2(S,\mu_n)",
         r"(16)\quad 0-\operatorname{Pic}(S)_n-H^2(S,\mu_n)"),
        (r"(17)\quad 0\longrightarrow", r"(17)\quad 0-"),
        (r"\varprojlim\operatorname{Pic}_n\ (=\operatorname{Pic}/n\operatorname{Pic})",
         r"\varprojlim(\operatorname{Pic}_n=\operatorname{Pic}/n\operatorname{Pic})"),
    ],
    81: [
        (r"\unsure{\gamma_i|q_i}\in\operatorname{Pic}(S)", r"\gamma_i\in\operatorname{Pic}(S)"),
    ],
    82: [
        (r"sss $\unsure{\gamma_i|q_i}=0$", r"sss $\gamma_i=0$"),
        (r"le long de $\unsure{q|g}_i(S)$", r"le long de $\unsure{g|g_i}(S)$"),
        (r"$\unsure{J_i/J_i^2|I_i/I_i^2}$", r"$J_i/J_i^2$"),
        (r"\quad 0\longrightarrow\deleted{\unsure{H^0(S)_n}}", r"\quad 0-\deleted{\unsure{H^0(S)_n}}"),
    ],
    83: [
        (r"qui opère \deleted{dans}\inserted{donc} $k(\widetilde x)", r"qui opère \inserted{donc} dans $k(\widetilde x)"),
    ],
    84: [
        (r"\unsure{(7)}\quad 1-I_{\widetilde x}", r"(7)\quad 1-I_{\widetilde x}"),
    ],
    85: [
        (r"quand $\unsure{\gamma_i|q_i}=0$", r"quand $\gamma_i=0$"),
    ],
    86: [
        (r"de $T$ sur $\unsure{I|S}$", r"de $T$ sur $I$"),
    ],
    88: [
        (r"E_{U_{\widetilde K}} \arrow[r] \arrow[d] \&", r"E_{U_{\widetilde K}} \arrow[r,dash] \arrow[d] \&"),
    ],
    89: [
        (r"(\inserted{\uline{non}} stricte)", r"(\inserted{\uline{\unsure{pas|non}}} stricte)"),
    ],
    90: [
        (r"$\kappa_i\circ(\mu\operatorname{id}_T)$", r"$\kappa_i\circ(\mu\circ\operatorname{id}_T)$"),
        (r"$\mu\in\mathbb N^{\unsure{+|*}}$", r"$\mu\in\mathbb N^{*}$"),
        (r"notre scindage de \inserted{$E_{U_\eta}$ sur $E_K$, ou} $E_{U_{\widetilde K}}$",
         r"notre scindage \inserted{$E_{U_\eta}$ sur $E_K$, ou} de $E_{U_{\widetilde K}}$"),
    ],
}

# global replacements (every occurrence; at least one required), applied after R
G = {
    76: [(q, "g") for q in QG],
    77: [(r"\unsure{\mathcal I|\mathcal J}", r"\mathcal J")] + [(q, "g") for q in QG],
    78: [(r"\unsure{\mathcal I|\mathcal J}", r"\mathcal J")] + [(q, "g") for q in QG],
    79: [(q, "g") for q in QG],
    81: [(q, "g") for q in QG],
    86: [(q, "g") for q in QG],
    87: [(r"\unsure{\widetilde O|\widetilde S}", r"\widetilde O")],
    88: [(r"\unsure{\widetilde O|\widetilde S}", r"\widetilde O")],
}

pages, errors, report = {}, [], []
for n in range(73, 91):
    name = f"MPL_149_001-090_scan{n:03d}.tex"
    with open(SRC / name, encoding="utf-8", newline="") as fh:
        t = fh.read()
    for old, new in R.get(n, []):
        c = t.count(old)
        if c != 1:
            errors.append(f"scan{n:03d}: {c} matches for {old!r}")
            continue
        t = t.replace(old, new)
    total = {}
    for old, new in G.get(n, []):
        c = t.count(old)
        total[old] = c
        t = t.replace(old, new)
    for key in {k for k, _ in G.get(n, [])}:
        pass
    # each global family must have matched at least once on its page
    fam = {}
    for old, new in G.get(n, []):
        fam.setdefault(new, 0)
        fam[new] += total[old]
    for new, c in fam.items():
        if c < 1:
            errors.append(f"scan{n:03d}: global replacement to {new!r} matched nothing")
        report.append(f"scan{n:03d}: {c} occurrence(s) -> {new}")
    if "\\unsure{q|g}" in t or "\\unsure{g|q}" in t:
        errors.append(f"scan{n:03d}: q|g doubt left")
    pages[name] = t

if errors:
    print("NOT WRITTEN:\n" + "\n".join(errors))
    sys.exit(1)
OUT.mkdir(parents=True, exist_ok=True)
for name, t in pages.items():
    with open(OUT / name, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
print("\n".join(report))
print(f"wrote {len(pages)} pages to {OUT}")
