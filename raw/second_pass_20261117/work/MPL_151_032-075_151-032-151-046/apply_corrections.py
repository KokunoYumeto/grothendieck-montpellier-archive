"""Apply the second-pass corrections of block MPL_151_032-075_151-032-151-046 (scans 32-46).

Reads each first-pass page file, applies exact replacements (each old string must occur exactly once),
writes the corrected file under second_pass/out/MPL_151_032-075/ with the same name.
"""
import os, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
SRC = os.path.join(BASE, 'returns', 'MPL_151_032-075_unzipped', 'pages')
OUT = os.path.join(BASE, 'second_pass', 'out', 'MPL_151_032-075')

R = {
 32: [
  ("étant plutôt de nature heuristique", "était plutôt de nature heuristique"),
  ("{} \\arrow[d, shift left=.4ex, \"{\\unsure{\\text{homo-topisme}}}\"'] \\\\\nY \\arrow[u, shift left=.4ex]",
   "{} \\\\\nY \\arrow[u, \"{\\unsure{\\text{homo-topisme}}}\"]"),
  ("$V^*_{z,\\unsure{Z|X}}$", "$V^*_{z,Z}$"),
  ("profinis; et", "profinis, et"),
 ],
 33: [
  ("en l'ens. des \\unsure{nb", "en l'\\unsure{ens.|un} des \\unsure{nb"),
 ],
 34: [
  ("\\pi_i(V^*_{\\unsure{Z,z|z,Z}})\\quad", "\\pi_i(V^*_{\\unsure{Z,z|z,Z}}]\\quad"),
 ],
 35: [
  ("$\\unsure{\\mathcal F|\\mathfrak F}$} de la cat. des", "$\\unsure{\\mathcal F|\\mathfrak F}$} dans la cat. des"),
  ("($\\unsure{\\leftrightarrow|\\rightarrow}$ un rev. \\inserted{étale}",
   "(\\unsure{$\\leftrightarrow$|$\\rightarrow$|en} un rev. \\inserted{étale}"),
  ("($\\unsure{\\leftrightarrow|\\rightarrow}$ un rev. étale",
   "(\\unsure{$\\leftrightarrow$|$\\rightarrow$|donc} un rev. étale"),
 ],
 36: [
  ("\\unsure{cela veut} que", "\\unsure{cela veut|cela dit} que"),
  ("pour \\deleted{les applic. à} Géométrie", "pour \\unsure{la|les} \\deleted{applic. à} Géométrie"),
 ],
 37: [
  ("vertical de \\unsure{(2)|(20)} est", "vertical de (2) est"),
 ],
 38: [
  ("\\unsure{complètement|canoniquement}", "complètement"),
  ("\\unsure{décrit|déduit}", "décrit"),
  ("(14) \\deleted{\\unsure{avec $\\pi_1(Y)$", "(19) \\deleted{\\unsure{avec $\\pi_1(Y)$"),
  ("($D=\\pi_1(V^*_{Y,X})\\xrightarrow{\\sim}", "($D\\Rightarrow\\pi_1(V^*_{Y,X})\\xrightarrow{\\sim}"),
  ("(\\text{resp. }i_*(a)\\longrightarrow c", "(\\text{resp. }\\unsure{j|i}_*(a)\\longrightarrow c"),
 ],
 39: [
  ("les $\\sigma\\in D$ et", "les $\\gamma\\in D$ et"),
  ("trivial (\\unsure{connu}),", "trivial (\\unsure{$\\infty$-connexe|connu}),"),
 ],
 40: [
  ("\\unsure{\\cong|\\simeq}", "\\cong"),
  ("principe devrait ``tenir compte''", "principe semblait ``tenir compte''"),
  ("$\\pi_{\\unsure{1|i}}$", "$\\pi_1$"),
 ],
 41: [], 42: [], 43: [],
 44: [
  ("dices fini) des groupoïdes", "dices fini) de groupoïdes"),
  ("de techniques \\unsure{bi-}", "de techniques $\\frac12$-"),
 ],
 45: [
  ("\\unsure{relatifs}", "\\unsure{relatifs|relatives}"),
  ("devront ``faisceautiser sur $X$", "seront ``\\unsure{faisceautisés|faisceautisées} sur $X$"),
 ],
 46: [
  ("\\arrow[dl,\"a\"']", "\\arrow[dl,\"{\\unsure{a|\\sigma}}\"']"),
  ("X_{\\Delta_1}\\xrightarrow{a}X_{\\Delta_0}", "X_{\\Delta_1}\\xrightarrow{\\unsure{a|\\sigma}}X_{\\Delta_0}"),
 ],
}

def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for n in range(32, 47):
        name = 'MPL_151_032-075_151_scan%03d.tex' % n
        with open(os.path.join(SRC, name), encoding='utf-8', newline='') as f:
            text = f.read()
        nl = '\r\n' if '\r\n' in text else '\n'
        work = text.replace('\r\n', '\n')
        for old, new in R[n]:
            c = work.count(old)
            if c != 1:
                print('ABORT scan %d: %r occurs %d times' % (n, old, c)); sys.exit(1)
            work = work.replace(old, new)
            total += 1
        if nl == '\r\n':
            work = work.replace('\n', '\r\n')
        dst = os.path.join(OUT, name)
        if os.path.exists(dst):
            print('ABORT: %s already exists' % dst); sys.exit(1)
        with open(dst, 'w', encoding='utf-8', newline='') as f:
            f.write(work)
        print(name, len(R[n]), 'replacements')
    print('total replacements', total)

if __name__ == '__main__':
    main()
