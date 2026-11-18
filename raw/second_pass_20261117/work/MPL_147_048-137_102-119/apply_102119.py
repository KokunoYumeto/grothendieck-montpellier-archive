"""Apply the second-pass corrections for MPL_147_048-137 scans 102-119.

Each specific replacement must match exactly the expected number of times; the script
stops before writing anything if one does not. Output: second_pass/out/MPL_147_048-137/.
"""
import os
import sys

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
SRC = ROOT + "returns/MPL_147_048-137_unzipped/pages/"
OUT = ROOT + "second_pass/out/MPL_147_048-137/"
NAME = "MPL_147_048-137_scan{}.tex"

SPEC = {
    102: [
        (r"est un morph. de norm. strict ssi", r"est un morph. de norm. \unsure{stricts|strict} ssi", 1),
    ],
    103: [
        (r"$\unsure{S|\mathcal S}\Pi M_G$", r"$S\Pi M_G$", 1),
        (r"\arrow[rr,leftrightarrow]", r"\arrow[rr]", 1),
        (r'\arrow[d,"\unsure{\sim|\wr}"]', r'\arrow[d,"\wr"]', 2),
        (r"est \unsure{réduite|réduit} à celle", r"est \unsure{réduit|réduite} à celle", 1),
    ],
    104: [
        (r"\inserted{effets \deleted{\unsure{sur}} en $\Pi_1M$ des}",
         r"\inserted{effets \deleted{\unsure{l'interaction}} en $\Pi_1M$ des}", 1),
        (r"\deleted{\unsure{covariances}} \unsure{commutation|covariances} de (148)",
         r"\deleted{\unsure{covariances}} commutation de (148)", 1),
        (r"\Pi_1M_{\unsure{\alpha|g_\alpha},\widehat I_\alpha}", r"\Pi_1M_{\alpha,\widehat I_\alpha}", 1),
    ],
    105: [
        (r"\inserted{\unsure{au delà de}}", r"\inserted{\unsure{au delà} \deleted{de}}", 1),
        (r"\Gamma'_G", r"\Gamma^!_G", 2),
    ],
    106: [
        (r"(hyp. purement locale en $(X,D)$, par définition)",
         r"(hyp. purement locale en $(X,D)$), par définition)", 1),
        (r"\unsure{l'hyp.} \unsure{analytiques|analytique}", r"l'hyp. \unsure{analytiques|analytique}", 1),
    ],
    107: [
        (r"compatibles avec \unsure{foncts} codim", r"compatibles aux \unsure{foncts} codim", 1),
    ],
    108: [
        (r"\deleted{formé des couples}\inserted{dont la fibre en} un pt",
         r"\deleted{formé des couples}\inserted{dont la fibre} en un pt", 1),
        (r"compatible \deleted{\unsure{avec|aux}} fonctions codim",
         r"compatible \unsure{aux|\deleted{avec}} fonctions codim", 1),
    ],
    109: [
        (r"(degré maximal de codim $d$)", r"(drapeau maximal de codim $d$)", 1),
        (r"\overset{\deleted{\unsure{\sim}}}{D'_d}", r"\overset{\deleted{\unsure{\sim}}}{D^!_d}", 2),
    ],
    110: [
        (r"D_J\simeq\unsure{\widetilde D'_d|\widetilde{\widetilde D}_d}\mathbin{\unsure{\wedge|\times}}_{(\unsure{\mathfrak S|\mathcal S}_d)_{D_d}}H(J).",
         r"D_J\simeq\overset{\deleted{\unsure{\sim}}}{D^!_d}\mathbin{\wedge}_{(\mathfrak S_d)_{D_d}}H(J).", 1),
        (r"(D_d,\unsure{\widetilde D'_{d'}|\widetilde D'_d})",
         r"(D_d,\overset{\deleted{\unsure{\sim}}}{D^!_{d'}})", 1),
    ],
    111: [
        (r"\inserted{($\unsure{\le|\ne}d$)}", r"\inserted{($\unsure{\ne|\le}d$)}", 1),
        (r"l'inclusion $\{x\}\subset J'$}}", r"l'inclusion $\{x\}\hookrightarrow J'$}}", 1),
        (r"\deleted{(\unsure{si|et} $\delta=1$)}", r"\deleted{(\unsure{si|et} $\delta=d$)}", 1),
        (r"D_{d,\delta}\simeq\unsure{\widetilde D'_d|\widetilde{\widetilde D}_d}\mathbin{\unsure{\wedge|\times}}_{(\unsure{\mathfrak S|\mathcal S}_d)_{D_d}}\mathcal P_\delta",
         r"D_{d,\delta}\simeq\overset{\deleted{\unsure{\sim}}}{D^!_d}\mathbin{\wedge}_{(\mathfrak S_d)_{D_d}}\mathcal P_\delta", 1),
        (r"\inserted{\unsure{de codim} $d'=\operatorname{cod}(e')$,}",
         r"\inserted{\unsure{où|un|de codim} $d'=\operatorname{cod}(e')$,}", 1),
    ],
    112: [
        (r"\unsure{\widetilde D'_d|\widetilde{\widetilde D}_d}\wedge_{\unsure{\mathfrak S|\mathcal S}_d}\mathcal P_\delta(I_d)",
         r"\overset{\deleted{\unsure{\sim}}}{D^!_d}\wedge_{\mathfrak S_d}\mathcal P_\delta(I_d)", 1),
    ],
    114: [
        (r"est un mono $\leftarrow$, et", r"est un mono $\unsure{\hookrightarrow|\leftarrow}$, et", 1),
        (r'''\arrow[dl,"\unsure{\sigma|s}"']''', r'''\arrow[dl,"\sigma"']''', 1),
        (r"(D_{**},\unsure{\sigma|s})", r"(D_{**},\sigma)", 1),
        (r"morphisme ``\unsure{identique}''", r"morphisme ``\unsure{identité|identique}''", 1),
        (r"\deleted{Et} Ces données", r"\deleted{\unsure{Toutes}} ces données", 1),
    ],
    115: [
        (r"pour $\forall S$,", r"pour tt $S$,", 1),
        (r"\margin{ceci conséquence de c) ci-dessous (\unsure{trop fort?|thm prouvé?})}",
         r"\margin{\unsure{ce sera} conséquence de c) ci-dessous (\unsure{thm prouvé?|trop fort?})}", 1),
        (r"(\unsure{\sigma|s},b)", r"(\sigma,b)", 1),
        (r"\hfill\Rightarrow\text{ une identité)}", r"\hfill\unsure{\Rightarrow|\text{est}}\text{ une identité)}", 1),
    ],
    116: [
        (r"un rev. $D'_d$ principal de groupe $\unsure{G_d|\mathfrak S_d}$",
         r"un rev. $D^!_d$ principal de groupe $\mathfrak S_d$", 1),
        (r"que ``les flèches sont", r"que ``\unsure{tt|les} flèches sont", 1),
    ],
    117: [
        (r"D'_", r"D^!_", 11),
        (r"\unsure{\mathfrak S_d|G_d}", r"\mathfrak S_d", None),
        (r"\unsure{\mathfrak S_{d'}|G_{d'}}", r"\mathfrak S_{d'}", None),
    ],
    119: [
        (r"pour $\unsure{\forall|\mathrm{tt}}\,d$ on a", r"pour tt $d$ on a", 1),
        (r"\margin{$D$ est une catég.", r"\margin{$\mathcal D$ est une catég.", 1),
    ],
}
GLOBAL = [(r"\unsure{\mathfrak S|\mathcal S}", r"\mathfrak S")]


def balance(s):
    t = s.replace(r"\{", "").replace(r"\}", "")
    return t.count("{") - t.count("}")


results = {}
problems = []
for n in range(102, 120):
    with open(SRC + NAME.format(n), encoding="utf-8") as f:
        text = f.read()
    new = text
    log = []
    for old, rep, want in SPEC.get(n, []):
        c = new.count(old)
        if (want is not None and c != want) or c == 0:
            problems.append(f"{n}: expected {want}, found {c}: {old}")
        new = new.replace(old, rep)
        log.append(f"  {c}x {old[:70]}")
    for old, rep in GLOBAL:
        c = new.count(old)
        if c:
            new = new.replace(old, rep)
            log.append(f"  {c}x [global] {old}")
    if balance(new) != balance(text):
        problems.append(f"{n}: brace balance changed {balance(text)} -> {balance(new)}")
    left = [w for w in ("D'_", r"\Gamma'", r"\unsure{\mathfrak S|", "|G_d}", "leftrightarrow") if w in new]
    results[n] = (text, new, log, left)

if problems:
    print("NOT WRITTEN:")
    print("\n".join(problems))
    sys.exit(1)

os.makedirs(OUT, exist_ok=True)
for n, (text, new, log, left) in results.items():
    with open(OUT + NAME.format(n), "w", encoding="utf-8", newline="") as f:
        f.write(new)
    print(f"scan {n}: {'changed' if new != text else 'unchanged'}; remaining markers: {left}")
    for line in log:
        print(line)
