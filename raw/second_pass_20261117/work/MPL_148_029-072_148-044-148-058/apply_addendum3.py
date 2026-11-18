# apply_addendum3.py: third set of corrections after the CTRL-148_2 comparison (GPT-6.2 Astra at reasoning effort max), 18 Nov 2026.
DST = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
F = "MPL_148_029-072_148_scan%03d.tex"
R = {
44: [(r"c'est le \unsure{gr.} $\mathcal T^\pm$", r"c'est le \unsure{gros|gr.} $\mathcal T^\pm$")],
46: [(r"rigidifie, \illegible{1} $\widetilde\Sigma$\ldots{}", r"rigidifie, \unsure{mais} aussi $\widetilde\Sigma$\ldots{}"),
     (r"\unsure{par|que} $R$ ``\unsure{découpage|découpe}''}", r"que $R$ ``découpe''}")],
48: [(r"$C$ \deleted{\unsure{$\in A$|est un}}", r"$C$ \deleted{\unsure{est un|$\in A$}}"),
     (r"le droit \unsure{d'échange|d'échanger},", r"le droit \unsure{d'échanger|d'échange},"),
     (r"\uline{0-isomorphisme} \unsure{?},", r"\uline{0-isomorphisme} \deleted{\unsure{)|?}},"),
     (r"\deleted{\unsure{La preuve}} :", r"\deleted{\unsure{Prop.|La preuve}} :"),
     (r"\uline{Remarque}. Dans", r"\uline{Remarques}. Dans"),
     (r"\inserted{\uline{\unsure{discrète|directe|disjointes}}}", r"\inserted{\uline{\unsure{directe|discrète|disjointes}}}")],
49: [(r"X\deleted{\unsure{\Sigma}}\text{ connexe}", r"X\deleted{\unsure{est}}\text{ connexe}"),
     (r"\deleted{Il} \inserted{Le graphe} est donc", r"\deleted{Il} \inserted{Ce graphe} est donc")],
50: [(r"l'\unsure{un|ens} des", r"l'\unsure{ens|un} des")],
51: [(r"\unsure{du contour|des contours} correspondant", r"\unsure{des contours|du contour} correspondant"),
     (r"i.e. les }C\in\pi_0(\unsure{\partial}X))$}", r"i.e. les }\in\pi_0(\unsure{\partial}X))$}")],
53: [(r"alors on \unsure{aura|devra} \unsure{par|pouvoir} donc aussi", r"\deleted{\unsure{alors}} on \unsure{aura|devra} \deleted{\unsure{par}} donc aussi"),
     (r"\unsure{pour|sur} une composante $C$", r"\unsure{sur|pour} une composante $C$"),
     (r"les repères \unsure{dans} \deleted{\unsure{ce}} $C$", r"les repères de \deleted{\unsure{ce}} $C$")],
54: [(r"de \deleted{\unsure{comp.}} conn. de $\Sigma'$ i.e. une partie", r"de comp. conn. de $\Sigma'$ i.e. à une partie"),
     (r"Au niveau des \deleted{repères} \inserted{sommets},", r"Au niveau des \inserted{sommets} (repères),")],
55: [(r"\deleted{$A\amalg R'$} \inserted{$R'\amalg\Sigma'$}", r"\deleted{$A'\amalg R'$} \inserted{$R'\amalg\Sigma'$}"),
     (r"\deleted{\unsure{de} $A\amalg\vec R$}", r"\deleted{\unsure{de} $A\amalg R$}")],
56: [(r"\deleted{\uline{affaiblissement de}}", r"\deleted{\uline{affaiblissement \unsure{et|ou} de}}"),
     (r"redonne l'objet de départ $(X,\unsure{\widetilde\Sigma|\Sigma},R)$", r"redonne l'objet de départ $(X,\Sigma,R)$"),
     (r"\margin{\deleted{arêtes} \deleted{\unsure{effectivement}} cercles marqués, \unsure{comme} \uline{arêtes} sur $\Sigma$}", r"\margin{\deleted{arêtes} cercles \deleted{\unsure{marqués|effectifs|repères}} \inserted{effectivement} marqués, corr. \uline{arêtes} sur $\Sigma$ \unsure{que}}"),
     (r"(\uline{NB} \unsure{elle est réunion|elles se déduisent|elles sont les intersections} des cercles eff. marqués, et \unsure{non|sont} des intervalles ouverts)", r"(\uline{NB} \unsure{elle est réunion|elles se trouvent sur|elles sont les intersections|elles se déduisent} des cercles eff. marqués, et sont des intervalles ouverts)")],
57: [(r"se borner par la suite", r"se borner \unsure{par|pour} la suite"),
     (r"$(a\in A)$ \unsure{connus} sous", r"$(a\in A)$ concernés sous"),
     (r"$\mathbb Z_a/r(a)\deleted{\unsure{\mathbb Z\mathbin{\wedge}\omega(a)}}$", r"$\mathbb Z_a/r(a)\deleted{\unsure{\mathbb Z/r(a)}}$")],
58: [(r"ce qui au niveau du graphe revient", r"ce qui au niveau des graphes revient"),
     (r"\deleted{\unsure{Les marq., par un}}", r"\deleted{Ici encore, pour \unsure{un|une} \illegible{1}}"),
     (r"\deleted{où il y a \unsure{tel et un}}", r"où \deleted{il y a \unsure{bel et bien|tel et un}}"),
     (r"$C$ est effectivement marqué i.e.", r"\inserted{$C$ est effectivement marqué} i.e."),
     (r"un ens. fini, \deleted{)} en plus) peut se récupérer,", r"un ens. fini, \deleted{)} \unsure{en plus|à isom près|ou pas}) peut se \unsure{réverser|renverser|inverser},")],
}
n_all = 0
for scan, pairs in R.items():
    p = DST + F % scan
    with open(p, encoding="utf-8") as fh:
        t = fh.read()
    for old, new in pairs:
        c = t.count(old)
        assert c == 1, (scan, old, c)
        t = t.replace(old, new)
        n_all += 1
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
print("applied", n_all)
