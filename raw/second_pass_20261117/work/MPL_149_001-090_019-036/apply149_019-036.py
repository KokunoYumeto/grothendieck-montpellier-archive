"""Apply the second-pass corrections to the first-pass page files of MPL_149_001-090, scans 019-036,
and write every page (changed or not) to second_pass/out/MPL_149_001-090/ under its first-pass name.
Each replacement must match exactly once, or the script stops without writing anything."""
import pathlib, sys

ROOT = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SRC = ROOT / "returns/MPL_149_001-090_unzipped/pages"
OUT = ROOT / "second_pass/out/MPL_149_001-090"

R = {
    19: [
        (r"par voie \unsure{profinie} une extension", r"par voie profinie une extension"),
        (r"\deleted{par} en considérant", r"\deleted{par} considérant"),
        (r"$\pi_K\unsure{\neq}\pi_1(K)$", r"$\pi_K\neq\pi_1(K)$"),
        (r"ou bien \unsure{plutôt|parfois}, par le topos", r"ou bien parfois, par le topos"),
    ],
    20: [
        (r"(non précisé d'avance) de} $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$ opère",
         r"(non précisé d'avance) de} $\unsure{\Pi|\Gamma}_{\overline{\mathbb Q}/\mathbb Q}$ opère"),
        (r"$\pi'\unsure{-|\longrightarrow}\pi$ y commute", r"$\pi'-\pi$ y commute"),
        (r"les $B_K$, $B_{K'}$, et $B_K-B_{\mathbb Q}$", r"les $B_K$, $B_{K'}$ et $B_K-B_{\mathbb Q}$"),
        (r"l'hom d'extensions \inserted{extérieures}", r"l'hom d'extensions \inserted{(extérieures)}"),
    ],
    22: [
        (r"des extensions de t.f. de $Q$ vers", r"des extensions de t.f. de $\mathbb Q$ vers"),
        (r"n'est pas spécial à $Q$", r"n'est pas spécial à $\mathbb Q$"),
        (r"\deleted{commutatif}", r"\deleted{correspondant}"),
        (r"soit commutatif) alors $f=g$.", r"\unsure{est|soit} commutatif) alors $f=g$."),
        (r"deux clôtures alg. de $K$, $\bar K$, $\widetilde{\bar K}$ de $K$",
         r"deux clôtures alg. de $\unsure{K_\varepsilon|\bar K}$, $\unsure{K|\widetilde K}$ de $K$"),
        (r"d'identifier $E_{\bar K/K}$ et $E_{\widetilde{\bar K}/K}$)",
         r"d'identifier $E_{\bar K/K}$ et $E_{\widetilde K/K}$)"),
        (r"\margin{\unsure{i.e.} induisant l'identité sur les clôtures alg. $\bar Q$ de $Q$ dans $\bar K$ et $\widetilde{\bar K}$, identifiées à celle dans $\bar K'$.}",
         r"\margin{induisant ``l'identité'' sur les clôtures alg. \deleted{\unsure{et|de}} $\overline{\mathbb Q}$ de $\mathbb Q$ dans $\bar K$ et $\widetilde K$, identifiées à celle dans $\bar K'$.}"),
        (r"\unsure{en} \unsure{donc} \unsure{plus}}", r"\unsure{en} \unsure{donc} \unsure{plus} \unsure{conclusion}}"),
        (r"$\overline{\mathbb Q}$ fixée, de $Q$, en disant", r"$\overline{\mathbb Q}$ fixée, de $\mathbb Q$, en disant"),
        (r"(avec opérateurs $\Gamma_{\bar Q/Q}$)", r"(avec opérateurs $\Gamma_{\overline{\mathbb Q}/\mathbb Q}$)"),
        (r"extension finie de $Q$.}", r"extension finie de $\mathbb Q$.}"),
    ],
    23: [
        (r"\pi_1(\bar U_i\deleted{\unsure{\bar\eta|\bar K}},\bar\eta)",
         r"\pi_1(\bar U_i\deleted{\unsure{\bar\eta|\bar K}},\unsure{\bar\eta|\bar K})"),
        (r"$\forall i,\ f|A_i=g|A_i$",
         r"$\forall i,\ \overset{f_i}{\overline{f|A_i}}=\overset{g_i}{\overline{g|A_i}}$"),
        (r"\pi_1(\bar U_i)\deleted{\unsure{K|\bar\eta}}", r"\pi_1(U_i)\deleted{\unsure{K|\bar\eta}}"),
        (r"comme hom de groupes extérieurs.", r"(comme hom de groupes extérieurs."),
        (r"(\unsure{d'où|càd} $f=g$)", r"(d'où $f=g$)"),
    ],
    24: [
        (r"\deleted{est un \unsure{schéma de groupe}}", r"\deleted{est \unsure{une|un} extension \unsure{d'une|d'un}}"),
    ],
    25: [
        (r"\varphi=\unsure{\psi|\varphi}", r"\varphi=\unsure{\varphi|\psi}"),
    ],
    26: [
        (r"\inserted{\unsure{voit}}", r"\inserted{voit}"),
    ],
    27: [
        (r"$y\unsure{\longrightarrow|\mapsto}y$", r"$y\longrightarrow y$"),
        (r"$y\unsure{\longmapsto|\longrightarrow}y+a$", r"$y\longmapsto y+a$"),
        (r"\unsure{SQS} que $X$ est une variété", r"OPS que $X$ est une variété"),
    ],
    28: [
        (r"\unsure{non complètes}", r"non complètes"),
    ],
    29: [
        (r"\deleted{\unsure{SPS|SQS} de plus", r"\deleted{OPS de plus"),
        (r"$\pi_1(\overline X)$ à centre trivial", r"$\pi_1(\overline X)$ a centre trivial"),
    ],
    30: [
        (r"(extérieures, \inserted{donc", r"(``extérieures, \inserted{donc"),
        (r"\unsure{ont par des|ont pu être}", r"ont pu \unsure{être}"),
    ],
    32: [
        (r"il \unsure{suffirait|suffira} $K$", r"il suffirait $K$"),
        (r"sous \unsure{cette forme} ce", r"sous cette forme ce"),
    ],
    35: [
        (r"du th. 3 en car. $p>0$ \inserted{de son cor. en} nous fait",
         r"du th. 3 \unsure{ou|en} \inserted{de son cor. en} car. $p>0$ nous fait"),
        (r"car pour \unsure{Artin}, il faudrait", r"car pour \unsure{être} à \unsure{l'aise|l'air}, il faudrait"),
        (r"\uline{\unsure{parfait|profini}}", r"\uline{parfait}"),
    ],
}

texts = {}
n_changes = 0
for n in range(19, 37):
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
