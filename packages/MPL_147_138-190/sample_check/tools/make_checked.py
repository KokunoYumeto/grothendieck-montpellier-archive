# Writes pages_checked/ for the three packages (first-pass page with the corrections of the sample check applied)
# and prints words and doubt marks per checked page.
# usage: python -I -B make_checked.py <returns_dir>
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wc_tex import count

ret = sys.argv[1]
FIX = {
    'MPL_147_138-190': {
        139: [(r'entièrement trivial', r'essentiellement trivial')],
        162: [(r'ce qui implique qu', r'ce qui indique qu')],
        165: [],
        189: [],
    },
    'MPL_149_001-090': {
        4: [],
        45: [(r'initiale ainsi corrigée', r'initiale revue et corrigée'),
             (r'E_{K\'}^\circ\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}',
              r'E_{K\'}^{\deleted{\circ}}\longrightarrow\Gamma_{\overline{\mathbb Q}/\mathbb Q}')],
        48: [],
        89: [],
    },
    'MPL_149_091-136': {
        92: [(r'\unsure{\mathcal E_{f_\eta}|\mathcal E_{f_K}}', r'\mathcal E_{f_K}'),
             (r'\unsure{\mathcal E_{U_K}|\mathcal E_{U_\eta}}', r'\mathcal E_{U_K}'),
             (r'\unsure{\mathcal E_K|\mathcal E_\eta}', r'\mathcal E_K'),
             (r'\unsure{\mathcal E_{U_\eta}|\mathcal E_{U_K}}', r'\mathcal E_{U_K}'),
             (r'\unsure{\mathcal E_\eta|\mathcal E_K}', r'\mathcal E_K'),
             (r'\unsure{\mathcal E_{\overline K}|\mathcal E_{\overline\eta}}', r'\mathcal E_{\overline K}'),
             (r'\unsure{entière|intégrale}', r'\unsure{normale}'),
             (r'(\unsure{20|29})', r'(29)')],
        106: [(r'(\unsure{\text{Schémas}|\text{Sch conn}})', r'(\text{Sch conn})')],
        121: [],
        135: [],
    },
}
BS = chr(92)
for pkg, pages in FIX.items():
    tot = 0
    print(pkg)
    for n, fixes in pages.items():
        src = os.path.join(ret, pkg + '_unzipped', 'pages', '%s_scan%03d.tex' % (pkg, n))
        s = open(src, encoding='utf-8').read()
        first = s
        for a, b in fixes:
            a = a.replace(BS + "'", "'"); b = b.replace(BS + "'", "'")
            if s.count(a) != 1:
                print('   !! %03d: %d occurrence(s) of %r' % (n, s.count(a), a))
            s = s.replace(a, b)
        out = os.path.join(ret, pkg + '_check', 'pages_checked', '%s_scan%03d.tex' % (pkg, n))
        open(out, 'w', encoding='utf-8', newline='').write(s)
        w = count(s)[0]
        tot += w
        un = len(re.findall(BS + BS + r'unsure\{', first)); una = len(re.findall(BS + BS + r'unsure\{[^{}]*\|', first))
        il = len(re.findall(BS + BS + r'illegible', first)); de = len(re.findall(BS + BS + r'deleted\{', first))
        print('   %03d words %d (first pass %d); first-pass marks: unsure %d (with alternative %d), illegible %d, deleted %d; fixes %d' % (n, w, count(first)[0], un, una, il, de, len(fixes)))
    print('   total words', tot)
