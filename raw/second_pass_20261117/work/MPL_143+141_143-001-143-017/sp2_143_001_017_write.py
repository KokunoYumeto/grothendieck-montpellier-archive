# Second pass MPL_143+141 block 143-001-143-017: apply corrections and write outputs.
# The character U+00A4 stands for a backslash everywhere below; it is converted at write time.
import os, sys, hashlib

BS = chr(92)
NL = chr(10)
ROOT = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110"
SRC = ROOT + "/returns/MPL_143+141_unzipped/pages"
OUT = ROOT + "/second_pass/out/MPL_143+141"

def L(s):
    return s.replace("¤", BS)

R = [
# scan, old, new
(2, "Si $¤unsure{X=}¤overline X$", "Si $¤unsure{X=|¤deleted{X}}¤overline X$"),
(2, "¤margin{Question : ¤unsure{comme} ¤illegible{1} ?}", "¤margin{Question : ¤unsure{comme|d'indice fini} ¤illegible{1} ?}"),
(2, "¤Gamma(¤unsure{X},¤mathcal O_{¤unsure{X}})", "¤Gamma(¤unsure{X}_{¤mathrm{red}},¤mathcal O_{¤unsure{X}})"),
(2, "Les sous-extensions $K$ de", "(3) Les sous-extensions $K$ de"),
(2, "du corps de base $¤overline{¤mathbf Q}$ de $¤overline X$", "du ¤unsure{groupe|corps} de base $¤overline{¤mathbf Q}$ de $¤overline X$"),
(2, "(¤unsure{4})¤qquad", "(4)¤qquad"),
(2, "¤unsure{de gr. prof.}}", "¤unsure{de gr. prof.|de projectivité}}"),
(2, "réduit¤margin{?} et loc. de t.f.", "réduit¤margin{?} et ¤uline{loc. de t.f.}"),
(2, "¤uline{Supposons $X$ connexe} ¤deleted{¤unsure{et}}¤inserted{$¤ne¤varnothing$}.", "¤uline{Supposons $X$ connexe} ¤inserted{$¤ne¤varnothing$}, et"),
(2, "$¤widetilde X¤xrightarrow{h}X$", "$¤widetilde X¤xrightarrow{¤unsure{h|¤text{de}}}X$"),
(2, "¤deleted{$X$}, et ¤deleted{considérons} posons", "$X$, et ¤deleted{considérons} posons"),
(2, "¤mathcal E_X=¤operatorname{Aut}(¤widetilde X/X)", "¤mathcal E_X=¤operatorname{Aut}(¤widetilde X¤unsure{¤deleted{/}}X)"),
(3, "(NB. Si $G_X$ est" + NL + "¤margin{$X$ est de t.f. $/¤overline{¤mathbf Q}$ et ¤unsure{sép.}}" + NL,
    "(NB. Si ¤inserted{$X$ est de t.f. $/¤overline{¤mathbf Q}$ et ¤unsure{sép.|si}} $G_X$ est" + NL),
(3, "qu'un hom. mod conjugaison", "qu'un hom. mod composition"),
(3, "¤unsure{aux} autom intérieurs", "¤unsure{avec un|aux} autom intérieurs"),
(4, "$¤Gamma'$ assez petit," + NL + "$¤Gamma'¤mathbin{-}", "$¤Gamma'$ assez petit," + NL + "¤inserted{de $¤xi$} $¤Gamma'¤mathbin{-}"),
(5, "(¤unsure{avec variation à} ss groupe d'indice", "(¤unsure{mod} restriction à ss groupe d'indice"),
(5, "¤deleted{$¤unsure{X|X'}$}", "¤deleted{$¤unsure{X|X'|X_I}$}"),
(5, "$¤mathcal G_{X';X}$", "$¤mathcal G_{¤unsure{X;X|X';X|X;X'}}$"),
(5, "¤inserted{ou plus précisément", "¤inserted{¤unsure{--|ou} plus précisément"),
(6, "et on a encore un germe de relèvement", "et on a encore un germe de ¤deleted{hom} ¤inserted{relèvement}"),
(6, "(¤unsure{éventuellement} mod comp.", "(¤unsure{circonstanciellement} mod comp."),
(6, "(¤mathcal G_{X'}¤mathbin{-})¤Gamma", "(¤mathcal G_{X'}¤longrightarrow)¤Gamma"),
(6, "sur $¤pi_1(X')$ est compatible avec la famille", "sur $¤pi_1(X')$, est compatible avec la famille"),
(7, "dans ``l'extension" + NL + "¤unsure{étale|totale}'' définie par", "dans ``l'extension''" + NL + "définie par"),
(7, "¤inserted{minimaux}", "¤inserted{maximaux}"),
(7, "(par transport de structure)", "¤unsure{(par transport de|qui transporte la} structure)"),
(7, "sa fibre dans $¤widetilde X'(I)$, ¤inserted{(c'est un espace hom.", "sa fibre dans $¤widetilde X'(I)$, ¤unsure{on} ¤inserted{(C'est un espace hom."),
(8, "¤margin{¤unsure{ici il est supposé} $¤dim X=1$", "¤margin{¤unsure{ici il faut supposer|ici il faudrait|ici il est supposé} $¤dim X=1$"),
(8, "¤deleted{¤unsure{On voit les structures}} ¤inserted{Donc $¤mathcal G'$}", "¤deleted{¤unsure{D.} Voici les structures} ¤inserted{¤unsure{Donc} $¤mathcal G'$}"),
(9, "¤bigl(¤widetilde X'(j)¤longrightarrow¤operatorname{Hom}(¤mathcal G'_j,", "¤bigl(¤widetilde X(j)¤longrightarrow¤operatorname{Hom}(¤mathcal G'_j,"),
(9, "¤inserted{et $¤mathcal G'_j$ le stab.", "¤inserted{et $¤mathcal G_j$ le stab."),
(9, "¤deleted{¤unsure{se prolongeant} dans", "¤deleted{¤unsure{se prolongeant|s'inscrivant} dans"),
(9, "¤uuline{Récapitulons.} On se donne :", "¤uuline{Récapitulons.} On a donc :"),
(9, "lisse en les pts minimaux}", "lisse en les pts maximaux}"),
(9, "J¤subset X'(¤overline{¤mathbf Q}),¤quad¤text{où }", "J¤underset{¤text{¤illegible{1}}}{¤subset}X'(¤overline{¤mathbf Q}),¤quad¤text{où }"),
(10, "¤mathcal G'¤mathbin{¤unsure{-|¤to}}¤Gamma", "¤mathcal G'¤longrightarrow¤Gamma"),
(10, "¤mathcal G'¤arrow[r,dash]¤&¤Gamma", "¤mathcal G'¤arrow[r]¤&¤Gamma"),
(10, "¤unsure{restrictions} des corps de base", "¤unsure{restrictions|variétés} des corps de base"),
(10, "¤pi_1(X')¤mathbin{¤unsure{-|¤to}}¤mathcal E'", "¤pi_1(X')¤longrightarrow¤mathcal E'"),
(11, "¤widetilde X'(I)¤mathbin{-}¤operatorname{Hom}", "¤widetilde X'(I)¤longrightarrow¤operatorname{Hom}"),
(11, "¤mathcal G'_{¤unsure{gj|j}}", "¤mathcal G'_{j}"),
(12, "``groupo-théorétique''", "``¤unsure{gruppentheoretisch}''"),
(12, "¤unsure{propre autant}", "¤unsure{propre autant|projectif}"),
(12, "¤unsure{enlevés|exclus}", "enlevés"),
(13, "considérons une ¤unsure{rationalisation} de la situation", "considérons une restriction de la situation"),
(13, "¤forall¤,¤unsure{¤gamma|¤sigma}¤in", "¤forall¤,¤gamma¤in"),
(13, "¤simeq¤operatorname{Ens}(¤pi_1)", "¤simeq¤operatorname{Ensf}(¤pi_1)"),
(14, "et ¤unsure{les} isomorphismes (11)", "et ¤unsure{les} ¤deleted{¤unsure{appl.}} isomorphismes (11)"),
(14, "¤unsure{itou|idem}", "itou"),
(15, "Réconstruction du ¤unsure{I|1}-groupoïde fondamental $¤Pi_1(X';J)$", "Réconstruction ¤unsure{des|du} ¤unsure{I|1}-groupoïde ¤unsure{fondamentaux|fondamental} $¤Pi_1(X';J)$"),
(15, "donc on peut écrire, indépendamment", "donc on peut dire, indépendamment"),
(16, "On voit que l'on a (grâce", "On ¤unsure{note|voit} que l'on a (grâce"),
(17, "un groupoïde ¤inserted{connexe},", "un groupoïde ¤inserted{¤unsure{non vide|$¤ne¤varnothing$}} connexe,"),
]

def fname(n):
    return "MPL_143+141_143_scan%03d.tex" % n

texts = {}
for n in range(1, 18):
    with open(os.path.join(SRC, fname(n)), encoding="utf-8", newline="") as f:
        t = f.read()
    assert "¤" not in t, n
    texts[n] = t
orig = dict(texts)
crlf = {n: ("\r\n" in texts[n]) for n in texts}

errors = []
for (n, old, new) in R:
    o, w = L(old), L(new)
    t = texts[n]
    if crlf[n]:
        o = o.replace(NL, "\r" + NL); w = w.replace(NL, "\r" + NL)
    c = t.count(o)
    if c != 1:
        errors.append((n, c, old[:70]))
        continue
    texts[n] = t.replace(o, w)
if errors:
    for e in errors:
        print("MISMATCH", e)
    sys.exit(1)

def marks(t):
    return t.count(BS + "unsure{") + t.count(BS + "illegible{")

os.makedirs(OUT, exist_ok=True)
tot_o = tot_n = 0
per = []
for n in range(1, 18):
    with open(os.path.join(OUT, fname(n)), "w", encoding="utf-8", newline="") as f:
        f.write(texts[n])
    mo, mn = marks(orig[n]), marks(texts[n])
    tot_o += mo; tot_n += mn
    per.append("%03d:%d->%d" % (n, mo, mn))
print("files written; doubt marks first pass -> corrected:", tot_o, "->", tot_n)
print(" ".join(per))

md_changes = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sp2_143_001_017_changes.txt"), encoding="utf-8").read()
md_notes = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sp2_143_001_017_notes.txt"), encoding="utf-8").read()
md_changes = md_changes.replace("@@MARKS_FP@@", str(tot_o)).replace("@@MARKS_NEW@@", str(tot_n)).replace("@@MARKS_PER@@", " ".join(per))
for name, content in (("MPL_143+141_143-001-143-017_changes.md", md_changes), ("MPL_143+141_143-001-143-017_notes_checked.md", md_notes)):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
        f.write(L(content))
print("md written")
for n in range(1, 18):
    print(fname(n), hashlib.sha256(texts[n].encode("utf-8")).hexdigest()[:16], "changed" if texts[n] != orig[n] else "same")
