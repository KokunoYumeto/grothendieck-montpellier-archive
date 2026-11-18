# apply_addendum2.py: second set of corrections after the CTRL-148_SOL62 comparison (17 Nov 2026).
DST = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
F = "MPL_148_029-072_148_scan%03d.tex"
R = {
46: [(r"\margin{MD = ``modulaire'' ! Mumford--Deligne}", r"\margin{MD = ``modulaire'' ou Mumford--Deligne}")],
48: [(r"le droit d'échange,", r"le droit \unsure{d'échange|d'échanger},"),
     (r"\uline{sommes} \inserted{\uline{\unsure{discrète|disjointes}}}", r"\uline{\unsure{somme|sommes}} \inserted{\uline{\unsure{discrète|directe|disjointes}}}")],
49: [(r"--- i.e. $\Sigma=\varnothing$", r"--- \unsure{i.e.|ici} $\Sigma=\varnothing$")],
51: [(r"arête ordinaire, implique que", r"arête ordinaire, indique que"),
     (r"serait unifiée par un", r"serait remplacée par un")],
52: [(r"qui sera important sans doute", r"qui sera \unsure{importante|important} sans doute"),
     (r"toute description algébrico-combinatoire", r"toute description-\unsure{traduction} algébrico-combinatoire"),
     (r"les \uline{graphes pondérés à repères} correspondants.", r"le \uline{graphe pondéré à repères} correspondant.")],
54: [(r"Au niveau des sommets \inserted{(repères)},", r"Au niveau des \deleted{repères} \inserted{sommets},")],
56: [(r"\inserted{i.e. telles que $r(a)>0$}", r"\inserted{du $\Gamma$, i.e. telles que $r(a)>0$}"),
     (r"redonne l'objet de départ $(X,\Sigma,R)$.", r"redonne l'objet de départ $(X,\unsure{\widetilde\Sigma|\Sigma},R)$.")],
}
n_rep = 0
for n, reps in R.items():
    p = DST + F % n
    t = open(p, encoding="utf-8").read()
    for old, new in reps:
        c = t.count(old)
        assert c == 1, ("scan %d: %d matches for %r" % (n, c, old[:70]))
        t = t.replace(old, new)
        n_rep += 1
    open(p, "w", encoding="utf-8", newline="").write(t)
    print(n, "ok", t.count("{") - t.count("}"))
print("replacements", n_rep)
