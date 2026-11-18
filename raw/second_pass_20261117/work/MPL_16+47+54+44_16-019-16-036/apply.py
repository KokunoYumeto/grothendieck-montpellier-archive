# Second pass, block MPL_16+47+54+44_16-019-16-036: apply the corrections to the first-pass page files,
# write the corrected files, count doubt marks, and build the changes file from changes_head.md.
import os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SRC = os.path.join(ROOT, 'returns', 'MPL_16+47+54+44_unzipped', 'pages')
OUT = os.path.join(ROOT, 'second_pass', 'out', 'MPL_16+47+54+44')
HERE = os.path.dirname(os.path.abspath(__file__))
SCANS = ['019', '020', '021', '022', '023', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036']
CROSS = r"\margin{\figure{\begin{tikzpicture}\draw (0,0)--(.18,.22);\draw (.03,.2)--(.16,.05);\end{tikzpicture}}}"

R = {
 '019': [(r"dont l'\unsure{ordre} n'est autre", r"dont l'ordre n'est autre", 1)],
 '020': [(r"\bar L'{}^2=\unsure{\overline{\bar L'}|\bar L'}", r"\bar L'{}^2=\bar L'", 1),
         (r"L^2,L',LL'.\qquad L'", r"L^{\unsure{4|2}},L',LL'.\qquad L'", 1)],
 '021': [(r"de torsion de $\uline Z_\ell$-module de type fini", r"de torsion du $\uline Z_\ell$-module de type fini", 1),
         (r"dans \deleted{les suites exactes}\inserted{la suite exacte} de Kummer",
          r"dans la\deleted{\unsure{s}} suite\deleted{\unsure{s}} exacte\deleted{\unsure{s}} de Kummer", 1),
         (r"\uline{groupe de Néron--Sévéri}", r"\uline{groupe de Néron-Sévéri}", 1)],
 '022': [(r"=L_0^{\unsure{n|\prime n}}\circ\alpha\beta\pi_0=\alpha\beta L_0^n.", r"=L_0^{\unsure{n|\prime n}}\alpha\beta\pi_0=\alpha\beta L_0^n.", 1),
         (r"$L_0^{\unsure{\prime n|n}}$ et $\Lambda_0^{\unsure{\prime n|n}}$ sont des bases",
          r"$\unsure{L_0^{\prime n}|L_0^n|L'{}^n}$ et $\unsure{\Lambda_0^{\prime n}|\Lambda_0^n|\Lambda'{}^n}$ sont des bases", 1),
         ("\nD'où\n" + r"\diagram{", "\n" + r"\unsure{D'où|Donc}" + "\n" + r"\diagram{", 1),
         (r"On \unsure{veut|peut} prouver", r"On \unsure{veut|peut|sait} prouver", 1),
         (r"projectif de type fini sur $A$. \unsure{Ça|Ce} ne marche", r"projectif de type fini sur \unsure{$k$|$A$}. Ça ne marche", 1),
         (r"\text{de base}", r"\text{\unsure{de|dont} base}", 1),
         (r"\text{degré}&0&2&4&", r"\text{deg:}&0&2&4&", 1)],
 '023': [(r"\margin{$\times$}", CROSS, 3)],
 '025': [(r"\deleted{\unsure{donc}}\ i=1", r"\deleted{\unsure{donc|dont}}\ i=1", 1),
         (r"\unsure{\rho'|\rho^1}(w,x)", r"\unsure{\rho'|\rho^1|\rho}(w,x)", 1),
         (r"\unsure{\langle x,y'\rangle|+\langle x,y'\rangle}\xi^2",
          r"\unsure{\langle x,y'\rangle|+\langle x,y'\rangle|\deleted{+}\langle x,y'\rangle|\deleted{-}\langle x,y'\rangle}\xi^2", 1),
         (r"\unsure{Quelle que soit la donnée} de", r"\unsure{Quels que soient les choix|Quelle que soit la donnée} de", 1),
         (r"\margin{Exprime aussi", r"\margin{exprime aussi", 1),
         (r"\text{ssi}\quad", r"\text{\unsure{sss|ssi}}\quad", 1),
         (r"\text{non dég ssi}\quad", r"\text{non dég \unsure{sss|ssi}}\quad", 1),
         (r"\uline{\text{it\unsure{ou}}}", r"\uline{\text{\unsure{itou|idem}}}", 1)],
 '026': [(r"Page 4. Après l\inserted{'}énoncé", r"Page 4. Aprés l\inserted{'}énoncé", 1),
         (r"dans le \unsure{diogramme|diagramme}:", r"dans le diagramme:", 1)],
 '027': [(r"$(H^1)\unsure{H^3|(H^1)^3}=0$", r"$(H^1)\unsure{H^3|(H^1)^3|{}^{\deleted{\otimes}3}}=0$", 1),
         (r"non dég. \unsure{étant donné}, et supposons", r"non dég. \unsure{étant donné|étant donnée}, et supposons", 1),
         (r"une droite isotrope $D$ dans", r"une droite isotrope \inserted{$D$} dans", 1),
         (r"\uline{Condition de non dégénérescence}", r"\uline{\unsure{Conditions|Condition} de non dégénérescence}", 1),
         (r"\varphi(x,y)=Q(\alpha(xy),\xi)", r"\varphi(x,y)=Q(\alpha(x\wedge y),\xi)", 1)],
 '029': [(r"($V$ est de dim paire)", r"(\unsure{$W$|$V$} \unsure{est|étant} de dim paire)", 1),
         (r"\unsure{au facteur scalaire}", r"\unsure{au facteur scalaire|à un facteur scalaire}", 2)],
 '033': [(r"\sum_{\unsure{0\leq i\leq2n}}", r"\sum_{0\leq i\leq2n}", 2),
         (r"\inserted{\unsure{3*|3'}})", r"\inserted{\unsure{3*|3'|\deleted{3}*}})", 1),
         (r"\deleted{\unsure{4L_X(\mathrm{id}_X-\phi_*\Lambda_Y\phi^*)+2(\mathrm{id}_X-\phi_*\Lambda_Y\phi^*)L_X}}",
          r"\deleted{\unsure{4L_X(\mathrm{id}_X-\phi_*\Lambda_Y\phi^*)+2(\mathrm{id}_X-\phi_*\Lambda_Y\phi^*)L_X|L_X(\mathrm{id}_X+\phi_*\Lambda_Y\phi^*)+(\mathrm{id}_X+\phi_*\Lambda_Y\phi^*)L_X}}", 1),
         (r"H^{\unsure{(2n)-2|(2n)+2}}", r"H^{\unsure{(2n)-2|(2n)+2|(2n+1)-2}}", 1)],
 '034': [(r"\deleted{\unsure{\text{si }i}}", r"\deleted{\unsure{\text{si }i|\text{si }i=n-1}}", 1),
         (r"\uline{\unsure{Cor}}\qquad Notons", r"\uline{\unsure{Cor}}\qquad \unsure{Non|Notons} ---", 1),
         (r"\inserted{\unsure{égal à celui de $L_X$, i.e.}}", r"\inserted{\unsure{égal à celui de $L_X$, i.e.|cf. 2 : celui de $L_X$, i.e.}}", 1),
         (r"\varphi_{n-1}:H^{n-1}(Y)", r"\varphi_{\unsure{n-1|*}}:H^{n-1}(Y)", 1)],
 '036': [(r"(\unsure{\alpha})\qquad H^*(Y)", r"(\unsure{\alpha|b})\qquad H^*(Y)", 1),
         (r"\text{si }\unsure{n+1}\leq i\leq2n.", r"\text{si }\unsure{n+1|\deleted{n+1}}\leq i\leq2n.", 1),
         (r"\unsure{variante}", r"\unsure{variante|variantes}", 1)],
}

def marks(text):
    """Every \\unsure{...} and \\illegible{...} with its line and its enclosing deleted/inserted/margin frames."""
    res, stack, i, n = [], [], 0, len(text)
    while i < n:
        c = text[i]
        if c == '\\':
            m = re.match(r'\\([A-Za-z]+)', text[i:])
            if not m:
                i += 2
                continue
            name, j = m.group(1), i + m.end()
            if j < n and text[j] == '{':
                if name in ('unsure', 'illegible'):
                    depth, k = 0, j
                    while k < n:
                        if text[k] == '\\':
                            k += 2
                            continue
                        if text[k] == '{':
                            depth += 1
                        elif text[k] == '}':
                            depth -= 1
                            if depth == 0:
                                break
                        k += 1
                    ctx = sorted(set(s for s in stack if s in ('deleted', 'inserted', 'margin')))
                    res.append((text.count('\n', 0, i) + 1, name, text[j + 1:k], ctx))
                    i = k + 1
                    continue
                stack.append(name)
                i = j + 1
                continue
            i = j
            continue
        if c == '{':
            stack.append(None)
        elif c == '}' and stack:
            stack.pop()
        i += 1
    return res

ok = True
tot_fp = tot_new = 0
rows = []
unres = []
for s in SCANS:
    name = 'MPL_16+47+54+44_16_scan%s.tex' % s
    with open(os.path.join(SRC, name), encoding='utf-8') as f:
        old = f.read()
    new = old
    for a, b, cnt in R.get(s, []):
        found = new.count(a)
        if found != cnt:
            print('MISMATCH scan', s, 'expected', cnt, 'found', found, ':', a[:70])
            ok = False
            continue
        new = new.replace(a, b)
    if old.count('\n') != new.count('\n'):
        print('LINE COUNT CHANGED', s)
        ok = False
    # brace balance check
    if new.count('{') - new.count('\\{') != new.count('}') - new.count('\\}'):
        print('BRACE IMBALANCE', s)
        ok = False
    fp, nw = len(marks(old)), len(marks(new))
    tot_fp += fp
    tot_new += nw
    rows.append((s, fp, nw))
    for line, kind, content, ctx in marks(new):
        where = (' (in ' + ', '.join('\\' + c for c in ctx) + ')') if ctx else ''
        if kind == 'illegible':
            unres.append('- scan %s, l.%d: `\\illegible{%s}`%s' % (s, line, content, where))
        else:
            unres.append('- scan %s, l.%d: `%s`%s' % (s, line, content.replace('`', "'"), where))
    if ok and '--check' not in sys.argv:
        with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
            f.write(new)

table = ['| Scan | First pass | After this pass |', '|---|---:|---:|']
table += ['| %s | %d | %d |' % r for r in rows]
table.append('| **Total** | **%d** | **%d** |' % (tot_fp, tot_new))
print('\n'.join(table))
if ok and '--check' not in sys.argv:
    with open(os.path.join(HERE, 'changes_head.md'), encoding='utf-8') as f:
        head = f.read()
    head = head.replace('@@N0@@', str(tot_fp)).replace('@@N2@@', str(tot_new)).replace('@@N1@@', str(tot_fp + 2))
    head = head.replace('@@COUNTS@@', '\n'.join(table)).replace('@@UNRESOLVED@@', '\n'.join(unres))
    with open(os.path.join(OUT, 'MPL_16+47+54+44_16-019-16-036_changes.md'), 'w', encoding='utf-8', newline='') as f:
        f.write(head)
    print('written; unresolved entries:', len(unres))
print('OK' if ok else 'FAILED')
