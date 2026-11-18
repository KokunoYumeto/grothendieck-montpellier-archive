"""Apply the second-pass corrections to the first-pass page files of block MPL_142_001-093_019-037.

Each replacement must match exactly once in its file; otherwise the script stops without writing.
Unchanged scans are copied byte for byte. Output: second_pass/out/MPL_142_001-093/.
"""
import os, sys

ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_142_001-093_unzipped/pages/MPL_142_001-093_scan{}.tex"
DST = ROOT + "/second_pass/out/MPL_142_001-093/MPL_142_001-093_scan{}.tex"
SCANS = ["019", "020", "021", "022", "024", "025", "026", "027", "028", "029",
         "030", "031", "032", "033", "034", "035", "036", "037"]

R = {
    "019": [
        (r'''\operatorname{Aut}(\widehat{\unsure{X|Y}},T)''',
         r'''\operatorname{Aut}(\widehat{\unsure{Y|X}},T)'''),
    ],
    "020": [
        (r'''avec \unsure{une|les} \unsure{propriété|propriétés} de transitivi-''',
         r'''avec \deleted{\unsure{une|les}} propriétés de transitivi-'''),
        (r'''té \unsure{évidentes|évidents}, pour''',
         r'''té \unsure{évidents|évidentes}, pour'''),
    ],
    "024": [
        (r'''six flèches $b_i^\omega$ : \deleted{\unsure{$R$}}''',
         r'''six flèches $b_i^\omega$ : \deleted{$\unsure{Q|R}$}'''),
        (r'''l_0l_1l_\infty=1\}''',
         r'''l_\infty l_1l_0=1\}'''),
        (r'''Les relations 2bis deviennent''',
         r'''Les relations 2(b) deviennent'''),
    ],
    "025": [
        (r'''on ne sait pas alors \unsure{exprimer}, en termes''',
         r'''on ne sait pas alors exprimer, en termes'''),
        (r'''\inserted{du groupoïde $\widehat{\mathrm{II}}_J$}''',
         r'''\inserted{du groupoïde $\widehat{\mathrm I}_J$}'''),
        (r'''les sous-groupoïdes $\widehat{\mathrm{II}}_{J,i}$, où $\widehat{\mathrm{II}}_{J,i}$ est engendré''',
         r'''les sous-groupoïdes $\widehat{\mathrm I}_{J,i}$, où $\widehat{\mathrm I}_{J,i}$ est engendré'''),
        (r'''La condition : $\mathrm{II}_{J,i}$ \deleted{défini} donné par''',
         r'''La \unsure{restriction|condition} \unsure{à|:} $\mathrm I_{J,i}$ \deleted{défini} donné par'''),
        (r'''=\varphi_i^{\omega'}(l_\infty^\gamma)a_i^\omega''',
         r'''=\varphi_i^{\omega'}(l_0^\gamma)a_i^\omega'''),
        (r'''(\tau_\infty\beta)b_i^\omega\bigr)}''',
         r'''(\sigma_\infty\beta)b_i^\omega\bigr)}'''),
        (r'''Les équations sur $(p,\beta)$ équivalent à \unsure{sont|$\longrightarrow$}''',
         r'''Les équations sur $(p,\beta)$ \unsure{équivalent à|expriment 2} \unsure{sont|$\longrightarrow$}'''),
    ],
    "026": [
        (r'''\deleted{Les relations $(2)$ deviennent} \inserted{La} partie $(2)$ devient automatique, pour écrire commodément la partie $(3)$, introduit les''',
         r'''\inserted{\unsure{Dans}} Les relations \inserted{$(2)$} \deleted{deviennent} la partie $(a)$ devient automatique, pour écrire commodément la partie $(b)$, \unsure{on} introduit les'''),
        (r'''\widetilde a_{\unsure{\omega\omega'i}}^\omega''',
         r'''\widetilde a_{\unsure{\omega^2i|\omega'i}}^\omega'''),
        (r'''\underbrace{\varepsilon_0\sigma_\infty}_{\rho^{-1}}''',
         r'''\overbrace{\varepsilon_0\sigma_\infty}^{\rho^{-1}}'''),
    ],
    "027": [
        (r'''On prend un autom. $u$ du groupoïde''',
         r'''On prend un autom. \inserted{$u$} du groupoïde'''),
        (r'''\deleted{\unsure{les groupoïdes}} $\mathrm{II}_{J,i}$''',
         r'''\deleted{\unsure{engendrés|les groupoïdes}} $\mathrm{II}_{J,i}$'''),
        (r'''Les relations à satisfaire sont alors déjà écrites''',
         r'''Les relations à satisfaire \deleted{\unsure{sont}} alors déjà écrites'''),
    ],
    "028": [
        (r'''\widetilde\alpha\rho^{-1}(\widetilde\alpha)\rho^{-2}(\widetilde\alpha)=1,''',
         r'''\widetilde\alpha\rho^{-1}(\unsure{\widehat\alpha|\widetilde\alpha})\rho^{-2}(\unsure{\widehat\alpha|\widetilde\alpha})=1,'''),
        (r'''équivaut alors à un $\widetilde\alpha\in\widehat\Pi_{0,3}$''',
         r'''équivaut à \unsure{celle} d'un $\widetilde\alpha\in\widehat\Pi_{0,3}$'''),
        (r'''\widetilde\alpha\varepsilon_0(\widetilde\alpha)l_0=\eta^{-1}l_0^p\eta\qquad(p=2\gamma+1)\ ;''',
         r'''(\unsure{30})\qquad\widetilde\alpha\varepsilon_0(\widetilde\alpha)l_0=\eta^{-1}l_0^p\eta\qquad(p=2\gamma+1)\ ;'''),
    ],
    "031": [
        (r'''On \deleted{\unsure{aura donc}} les relations''',
         r'''On \deleted{\unsure{aura donc}} \inserted{a} les relations'''),
        (r'''Considérons maintenant les ss-groupes de''',
         r'''Considérons maintenant \unsure{le|les} ss-\unsure{groupoïde|groupes} de'''),
    ],
    "032": [
        (r'''\inserted{\unsure{simplet.}}''',
         r'''\inserted{simpl tr.}'''),
    ],
    "033": [
        (r'''par les isomorphismes''',
         r'''par \unsure{ces|les} isomorphismes'''),
    ],
    "036": [
        (r'''formule (55) \deleted{\unsure{se}} s'écrit alors''',
         r'''formule (55) \unsure{se}\deleted{\unsure{t}} récrit alors'''),
        (r'''(61)\qquad\alpha'=\rho(''',
         r'''(61)\qquad\uline{\alpha'}=\rho('''),
    ],
    "037": [
        (r'''\unsure{s'effectue} par''',
         r'''\unsure{s'exprime|s'effectue} par'''),
    ],
}

def main():
    outputs = {}
    total = 0
    for s in SCANS:
        with open(SRC.format(s), encoding="utf-8", newline="") as f:
            text = f.read()
        for old, new in R.get(s, []):
            n = text.count(old)
            if n != 1:
                sys.exit("scan %s: %d matches for %r" % (s, n, old))
            text = text.replace(old, new)
            total += 1
        outputs[s] = text
    os.makedirs(os.path.dirname(DST.format("000")), exist_ok=True)
    for s, text in outputs.items():
        with open(DST.format(s), "w", encoding="utf-8", newline="") as f:
            f.write(text)
    print("replacements applied:", total)
    for s in SCANS:
        with open(SRC.format(s), encoding="utf-8", newline="") as f:
            a = f.read()
        with open(DST.format(s), encoding="utf-8", newline="") as f:
            b = f.read()
        print(s, "changed" if a != b else "same", len(R.get(s, [])), "replacements")

main()
