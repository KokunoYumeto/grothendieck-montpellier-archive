"""Apply the second-pass corrections to the first-pass page files of MPL_149_001-090, scans 001-018,
and write every page (changed or not) to second_pass/out/MPL_149_001-090/ under its first-pass name.
Each replacement must match exactly once, or the script stops without writing anything."""
import pathlib, sys

ROOT = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SRC = ROOT / "returns/MPL_149_001-090_unzipped/pages"
OUT = ROOT / "second_pass/out/MPL_149_001-090"

R = {
    3: [
        (r"il est \unsure{antiéquivalent} canoniquement", r"il est antiéquivalent canoniquement"),
        (r"la \unsure{variance} des clôtures", r"la variance des clôtures"),
    ],
    4: [
        (r"ou \unsure{rev.} universel de $B_{K'}$", r"ou rev. universel de $B_{K'}$"),
        (r"ou clôture \deleted{sép.}\inserted{$\bar K'$} de $K'$)", r"ou clôture sép.\inserted{$\bar K'$} de $K'$)"),
        (r"(associé, en prenant $\bar K^{\deleted{\unsure{\prime}}}=$ clôture \inserted{alg.}\deleted{sép} de $K$ dans $\bar K'$)",
         r"(associé, \unsure{on|en} prend $\bar K^{\deleted{\unsure{\prime}}}=$ clôture \inserted{alg} sép de $K$ dans $\bar K'$)"),
    ],
    5: [
        (r"clôture \inserted{alg.} sép. de $K$ dans $K'$", r"clôture \inserted{alg} sép. de $K$ dans $K'$"),
        (r"est \unsure{tjs} un sous-groupe", r"est bien un sous-groupe"),
    ],
    7: [
        (r"\Pi_K&\unsure{\cong|\simeq}\varprojlim\Pi_{K_i}", r"\Pi_K&\cong\varprojlim\Pi_{K_i}"),
        (r"B_K&\unsure{\cong|\simeq}\varprojlim B_{K_i}", r"B_K&\cong\varprojlim B_{K_i}"),
        (r"de corps de type fini vers celle des corps", r"de corps de type fini, vers celle des corps"),
    ],
    8: [
        (r"\unsure{aux-|au-}", r"aux-"),
        (r"clôture alg. quelq. $\overline", r"clôture alg. \unsure{quelc.|quelq.} $\overline"),
    ],
    9: [
        (r"\unsure{ce sont} les morphismes (de topos", r"\unsure{ce sont} les \deleted{\unsure{f}}morphismes (de topos"),
        (r"\unsure{domineront|dominent} la situation", r"domineront la situation"),
    ],
    10: [
        (r"\margin{\uline{\unsure{NB}} $\pi_{\bar K/K}=(1)$", r"\margin{\uline{NB} $\pi_{\bar K/K}=(1)$"),
        (r"des \unsure{inclusions|immersions} ouvertes", r"des inclusions ouvertes"),
        (r"donc les $U_j\unsure{-|\longrightarrow}U_i$", r"donc les $U_j\unsure{\lhook\joinrel\relbar|\hookrightarrow}U_i$"),
        (r"\mathbb Q}/\mathbb Q$, extension finie", r"\mathbb Q}/\mathbb Q$, \unsure{u} extension finie"),
    ],
    12: [
        (r"&\simeq\varprojlim_i\widehat{\pi_1(U_i(\mathbb C),\bar\eta)}", r"&\simeq\varprojlim_i\pi_1(U_i(\mathbb C),\bar\eta)^{\wedge}"),
    ],
    13: [
        (r"et de $E_{\bar K/K}$ $\unsure{\ell|:}$", r"et de $E_{\bar K/K}^{\unsure{\ell}}$"),
    ],
    15: [
        (r"et on admet que le centre d'un groupe profini libre", r"et on admet que \unsure{le|son} centre d'un groupe profini libre"),
    ],
    16: [
        (r"\inserted{\unsure{!|à} isom unique près,}", r"\inserted{à isom unique près,}"),
    ],
    17: [
        (r"en termes de l'\uline{action extérieure}", r"en termes de \deleted{\unsure{ain}} l'\uline{action extérieure}"),
    ],
    18: [
        (r"\uline{pro-galoisiens}", r"\uline{pro-}galoisiens"),
        (r"Ils \unsure{sont|seront} décrits", r"Ils sont décrits"),
    ],
}

texts = {}
n_changes = 0
for n in range(1, 19):
    name = f"MPL_149_001-090_scan{n:03d}.tex"
    t = (SRC / name).read_text(encoding="utf-8")
    for old, new in R.get(n, []):
        c = t.count(old)
        if c != 1:
            sys.exit(f"scan {n:03d}: pattern found {c} times: {old}")
        t = t.replace(old, new)
        n_changes += 1
    texts[name] = t

OUT.mkdir(parents=True, exist_ok=True)
for name, t in texts.items():
    (OUT / name).write_text(t, encoding="utf-8", newline="\n")
print("pages written:", len(texts), "replacements:", n_changes)
for n in R:
    print(f"scan {n:03d}: {len(R[n])}")
