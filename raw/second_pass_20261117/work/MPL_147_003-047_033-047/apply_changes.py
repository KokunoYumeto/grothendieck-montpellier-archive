"""Second pass, MPL_147_003-047 scans 033-047: copy the first-pass page files to second_pass/out and
apply the corrections settled against the scans. Each old string must occur exactly once."""
import os
import re

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
SRC = BASE + "returns/MPL_147_003-047_unzipped/pages/"
OUT = BASE + "second_pass/out/MPL_147_003-047/"

CHANGES = {
    "033": [
        (r"""$\unsure{\widehat\mu_\alpha|\widetilde\mu_\alpha}=""", r"""$\widetilde\mu_\alpha="""),
        (r"""\text{nb de}\allowbreak\text{ arcs de }G""", r"""\text{nb }\unsure{\text{d'arcs}|\text{de arcs}}\text{ de }G"""),
    ],
    "034": [
        (r"""on \deleted{\unsure{se}} donne""", r"""on \deleted{\unsure{fix|se}} donne"""),
        (r"""S_{(\alpha)}\xrightarrow{\unsure{\gamma_\alpha|g_\alpha}}\mathbb N""", r"""S_{(\alpha)}\xrightarrow{\gamma_\alpha}\mathbb N"""),
        (r"""tel que $\unsure{\gamma_\alpha|g_\alpha}(\beta)=0$""", r"""tel que $\gamma_\alpha(\beta)=0$"""),
        (r"""on \deleted{\unsure{se donne}} choisit une \inserted{nouvelle} ``origine''""",
         r"""on \deleted{\unsure{se donne}} ``choisit une \inserted{nouvelle} origine''"""),
        (r"""de façon symétrique la relation""", r"""de façon \unsure{simplifiée} la relation"""),
    ],
    "035": [
        (r"""une \unsure{extension|catégorie} de la notion""", r"""une \unsure{extension} de la notion"""),
    ],
    "038": [
        (r"""(cela \unsure{définir|définit} juste""", r"""(cela \unsure{défini|définit} juste"""),
        (r"""&\qquad\sigma_{\widetilde A'}|\widetilde B'\text{ et à }""",
         r"""&\qquad\unsure{\text{à}}\ \sigma_{\widetilde A'}|\widetilde B'\text{ et à }"""),
        (r"""définie et lue de façon""", r"""définie et \unsure{lue} de façon"""),
    ],
    "040": [
        (r"""(donc l'extrémité \inserted{$(^{+})$} aussi)""", r"""(donc l'extrémité aussi)"""),
        (r"""d) le genre du MD-graphe $\underline G'(\alpha)$ est égal""", r"""d) le genre du MD-graphe $\underline G(\alpha)$ est égal"""),
        (r"""+h_1(G'(\alpha))=g_\alpha.""", r"""+h_1(G(\alpha))=g_\alpha."""),
    ],
    "041": [
        (r"""\Big)+h_1(G'(\alpha))""", r"""\Big)+h_1(G(\alpha))"""),
    ],
    "042": [
        (r"""(50)\qquad\widetilde A\simeq\widetilde B'""", r"""(50)\qquad\widetilde A^{\deleted{\unsure{'}}}\simeq\widetilde B'"""),
    ],
    "043": [
        (r"""c'est plus une somme amalgamée""", r"""c'est \unsure{plus|bien} une somme amalgamée"""),
        (r"""\text{Graphe }\deleted{\unsure{\text{ponctuel}}}""", r"""\text{\unsure{(graphe|Graphe} }\deleted{\unsure{\text{ponctuel}}}"""),
    ],
    "045": [
        (r"""(55)\qquad G'\longrightarrow G_0\unsure{\longrightarrow|{-}}G,""",
         r"""(55)\qquad G'\unsure{\longrightarrow|{-}}G_0\unsure{\longrightarrow|{-}}G,"""),
    ],
    "046": [
        (r"""est l'ens des flèches $\in\widetilde B'$ d'origine""", r"""est l'ens des flèches \unsure{de|$\in$} $\widetilde B'$ d'origine"""),
        (r"""la prop. \unsure{de ce|du} n° 3""", r"""la prop. du n° 3"""),
        (r"""de la maquette $\underline{\unsure{G|G'}}(\alpha)$""", r"""de la maquette $\underline G^{\deleted{\unsure{'}}}(\alpha)$"""),
    ],
}


def main():
    os.makedirs(OUT, exist_ok=True)
    total_changes = 0
    total_unsure_before = 0
    total_unsure_after = 0
    for n in range(33, 48):
        scan = f"{n:03d}"
        name = f"MPL_147_003-047_scan{scan}.tex"
        with open(SRC + name, encoding="utf-8", newline="") as f:
            text = f.read()
        before = len(re.findall(r"\\unsure\{", text))
        balance0 = text.count("{") - text.count("}")
        for old, new in CHANGES.get(scan, []):
            k = text.count(old)
            if k != 1:
                raise SystemExit(f"scan {scan}: old string found {k} times: {old}")
            text = text.replace(old, new)
            total_changes += 1
        after = len(re.findall(r"\\unsure\{", text))
        total_unsure_before += before
        total_unsure_after += after
        if text.count("{") - text.count("}") != balance0:
            raise SystemExit(f"scan {scan}: brace balance changed by the edits")
        with open(OUT + name, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print(scan, "changes", len(CHANGES.get(scan, [])), "unsure before", before, "after", after)
    print("total changes", total_changes, "unsure before", total_unsure_before, "after", total_unsure_after)


if __name__ == "__main__":
    main()
