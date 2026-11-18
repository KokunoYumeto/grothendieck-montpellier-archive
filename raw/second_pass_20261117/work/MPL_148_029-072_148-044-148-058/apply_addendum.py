# apply_addendum.py: corrections to the second-pass output after the CTRL-148 comparison (17 Nov 2026, scan-checked).
DST = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_148_029-072/"
F = "MPL_148_029-072_148_scan%03d.tex"
R = {
44: [
 (r"\margin{Finalement, \unsure{tout pris en détail|pour \illegible{1} travaux}, \unsure{au point de vue" + "\n" + r"œcuménique|\illegible{1} ultérieurs}, il semble que \unsure{c'est le cas} $\mathcal T^\pm$ qui \unsure{offre|soit}",
  r"\margin{Finalement, tant qu'on ne travaille pas au point de vue" + "\n" + r"arithmétique, il semble que c'est le \unsure{gr.} $\mathcal T^\pm$ qui \unsure{sera|offre|soit}"),
 (r"\deleted{\unsure{d'où}} c'est lui qui", r"\deleted{\unsure{tout|d'où}} c'est lui qui"),
 (r"et le \unsure{groupoïde|groupe} orienté \unsure{s'appelle|s'appellera} $\mathcal T^+$.}",
  r"et le \unsure{gr.\ or.|groupoïde|groupe} orienté de s'appeler $\mathcal T^+$.}"),
 (r"\margin{\unsure{Canulé}, \unsure{si on ne se borne|n'a un sens} à des surfaces connexes!}",
  r"\margin{\unsure{Canulé|Cautèle}, \unsure{si on ne se borne|désormais borner|n'a un sens} à des surfaces connexes!}"),
],
48: [
 (r"S=\pi_0(X\setminus\widetilde\Sigma)", r"S=\pi_0(X\deleted{\unsure{,}}\setminus\widetilde\Sigma)"),
 (r"$C$ \deleted{\unsure{est un}}\inserted{$\in\pi_0(\widetilde\Sigma)$}", r"$C$ \deleted{\unsure{$\in A$|est un}}\inserted{$\in\pi_0(\widetilde\Sigma)$}"),
 (r"\inserted{\uline{disjointes}}", r"\inserted{\uline{\unsure{discrète|disjointes}}}"),
],
50: [(r"une telle structure supplémentaire en prenant", r"une telle structure supplémentaire :")],
51: [(r"Il peut être plus commode dans la donnée d'ensemble de la structure,", r"Il peut être plus commode de la donner d'emblée dans la structure,")],
53: [(r"mais cet affaiblissement, si pour une composante $C$ \unsure{donnée} de $\Sigma^+$, l'on \unsure{doive|doit} ``gommer'' \uline{tous} les repères de \deleted{\unsure{ce}} $C$ --- \unsure{alors} c'est au contraire",
      r"mais cet affaiblissement, \unsure{pour|sur} une composante $C$ \unsure{donnée} de $\Sigma^+$, lorsqu'on ``gomme'' \uline{tous} les repères \unsure{dans} \deleted{\unsure{ce}} $C$ --- \unsure{sinon} c'est au contraire")],
55: [(r"cette opération consiste à exclure \deleted{les}", r"cette opération consiste à enlever \deleted{les}")],
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
