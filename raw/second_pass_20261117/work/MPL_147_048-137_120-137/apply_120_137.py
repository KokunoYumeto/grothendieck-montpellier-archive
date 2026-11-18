import os

SRC = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/returns/MPL_147_048-137_unzipped/pages/"
OUT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_147_048-137/"

CH = {
120: [
 (r"""\deleted{\unsure{Et}} Et plus""", r"""\deleted{\unsure{Et}} et plus"""),
 (r"""\text{ au dessus de }\unsure{D_d}""", r"""\text{ au dessus de }\unsure{D_1|D_d}"""),
 (r"""\substack{\mathrm{can}\\\unsure{b|a}}""", r"""\substack{\mathrm{can}\\\unsure{1|4}}"""),
 (r"""$D_d\xrightarrow{\mathrm{id}}\deleted{\unsure{D_d}}$""", r"""$D_d\xrightarrow{\unsure{i_d|\mathrm{id}}}\deleted{\unsure{D_d}}\unsure{X}$"""),
 (r"""les \unsure{images} $x_i$""", r"""les \deleted{$x_i$} \unsure{images} $x_i$"""),
],
121: [
 (r"""$X=D_0\simeq\unsure{\mathbb E^2|E^2}$""", r"""$X=D_0\simeq\mathbb E^2$"""),
],
123: [
 (r"""\text{ (ou des }\unsure{\pi_1|\pi_0}\text{)}""", r"""\text{ (ou des }\pi_1\text{)}"""),
 (r"""\Pi\unsure{P_d^*|P''_d}$ \margin{(un couple)} pour $d$ variable. Considérons donc""",
  r"""\Pi P_d^*$ pour $d$ variable. Considérons donc \inserted{un couple}"""),
],
125: [
 (r"""P_d\mathbin{\unsure{\times|\otimes}}_{D_d}D_{d,d'}""", r"""P_d\mathbin{\unsure{\otimes|\times}}_{D_d}D_{d,d'}"""),
],
126: [
 (r"""(dans \unsure{tt|tte} sa force\ldots)""", r"""(dans tt sa force\ldots)"""),
],
127: [
 (r"""\unsure{s'induit|induite}""", r"""\unsure{induite|s'induit}"""),
 (r"""--- je me \unsure{dispenserai|dispense} de""", r"""--- \unsure{je|p.} me \unsure{dispenser|dispense} de"""),
 (r"""\inserted{$\Theta_d$ \deleted{\unsure{(cf)}}}""", r"""\inserted{$\Theta_d$ \deleted{\unsure{$(D(d))$|(cf)}}}"""),
 (r"""\deleted{On \deleted{pose alors}""", r"""\deleted{On \deleted{\unsure{posera|pose} alors}"""),
],
128: [
 (r"""\text{ens des « drapeaux de}""", r"""\text{ens des ``\deleted{\illegible{1}}drapeaux de}"""),
 (r"""d_*\text{ » de l'ens fini}""", r"""d_*\text{'' de l'ens fini}"""),
],
129: [
 (r"""\inserted{applications « premier sommet »}""", r"""\inserted{morphismes ``premier sommet''}"""),
 (r"""\overbrace{P_{d_0}}^{G_{d_0}\text{-torseur}}""", r"""\overbrace{P_{d_0}}^{G_d\text{-torseur}}"""),
 (r"""\text{sur }\unsure{D_{d_0}|d_0}\text{, par }""", r"""\text{sur }\unsure{D_0|D_{d_0}}\text{, par }"""),
],
130: [
 (r"""de $D_{d_0}^{\unsure{\circ|0}}$ et $D_{d_0}^*$ \unsure{etc.} sont nuls""",
  r"""de $D_{d_0}^{\unsure{\circ|*|0}}$ et \unsure{$D^*_{d_0,-,d_r}$|$D_{d_0}^*$ etc.} sont nuls"""),
 (r"""\deleted{\unsure{D^*_{d_0,\ldots,d_r}}=}""", r"""\deleted{\unsure{T^*_{d_0,\ldots,d_r}|D^*_{d_0,\ldots,d_r}}=}"""),
 (r"""\overbrace{T_{d_0}}^{\text{syst. loc.}}""",
  r"""\overbrace{T_{d_0}}^{\text{syst. loc.\ \inserted{$(\overset{\mathrm{loc}}{\simeq}\mathbf Z^{d_0})$}}}"""),
 (r"""\inserted{$(\overset{\mathrm{loc}}{\simeq}\mathbf Z^{d_0})$}
de sorte que""", r"""de sorte que"""),
 (r"""\unsure{G_{\Delta_r}}&=""", r"""G_{\Delta_r}&="""),
],
131: [
 (r"""\widetilde\Pi_{\unsure{\Delta_r}}&=""", r"""\widetilde\Pi_{\Delta_r}&="""),
 (r"""Notons « pour mémoire »""", r"""Notons ``pour mémoire''"""),
 (r"""« dépendance
simpliciale »""", r"""``dépendance
simpliciale''"""),
 (r"""(\unsure{par|car}""", r"""(par"""),
],
132: [
 (r"""$D_d^*!$ sur $D_{\unsure{\Delta_r|\Delta}}$""", r"""\unsure{$D'^*_d$|$D_d^*!$} sur $D_{\unsure{d|\Delta}}$"""),
],
134: [
 (r"""(« hom de dégénérescence »)""", r"""(``hom de dégénérescence'')"""),
],
135: [
 (r"""\uline{est \unsure{un|une}}""", r"""\uline{est un}\deleted{\unsure{e}}"""),
 (r"""\{d_0\unsure{\geq|>}d_1\cdots>d_r\}""", r"""\{d_0>d_1\cdots>d_r\}"""),
 (r"""(« opération
face »)""", r"""(``opération
face'')"""),
 (r"""« face de codim $1$ »""", r"""``face de codim $1$''"""),
],
136: [
 (r"""D_{\unsure{\widetilde d_*}}""", r"""D_{\widetilde d'_*}"""),
 (r"""le « squelette
de dim $p$ » de""", r"""le ``squelette
de dim $p$'' de"""),
],
137: [
 (r"""D_{\unsure{\widetilde d_*}}""", r"""D_{\widetilde d'_*}"""),
],
}

os.makedirs(OUT, exist_ok=True)
total = 0
for n in range(120, 138):
    name = "MPL_147_048-137_scan%d.tex" % n
    with open(SRC + name, encoding="utf-8", newline="") as f:
        t = f.read()
    for old, new in CH.get(n, []):
        c = t.count(old)
        assert c == 1, (n, c, old)
        for s in (old, new):
            assert "\t" not in s and "\r" not in s and "\x08" not in s and "\x0c" not in s, (n, s)
        t = t.replace(old, new)
        total += 1
    with open(OUT + name, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    flags = []
    if "«" in t or "»" in t:
        flags.append("guillemets left")
    if t.count("{") != t.count("}"):
        flags.append("brace count %d/%d" % (t.count("{"), t.count("}")))
    print(n, len(CH.get(n, [])), " ".join(flags))
print("replacements", total)
