import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.normpath(os.path.join(here, '..', '..', '..'))
out = os.path.join(root, 'second_pass', 'out', 'MPL_150_001-043')
fp = os.path.join(root, 'returns', 'MPL_150_001-043_unzipped', 'pages')
os.makedirs(out, exist_ok=True)
text = open(os.path.join(here, 'combined_corrected.tex'), encoding='utf-8').read()
parts = re.split(r'^%%%%FILE (\S+)\n', text, flags=re.M)
files = dict(zip(parts[1::2], parts[2::2]))
keys = [r'\unsure{X|si}', 'tel que l', 'p_{jk}', r'\deleted{\unsure{$X$}}', 'équisingulière', 'suite.', r'\unsure{k|h}',
        r'\mathcal E_i)', r'\deleted{\beta}', r'\Longrightarrow\quad X_i\supset', 'Les }X_', r'\textcircled{d}', r'\textcircled{\unsure{c}}',
        r'(I\supset I', r'\deleted{$X_i$}', r'\underset{\substack{\Vert\\beta}}{i}', 'clair aussi sur (19)', r'\dot T_\beta=\dot X', 'germes de', r'\deleted{\mathcal E}B',
        'n-1}}', 'poin', 'ne se donne', 'par dessus', r'\deleted{\illegible{1}}', r'\unsure{p}', 'si on veut', 'signifie par', "d''|d'", 'sans plus', r'\inserted{\(i\)}',
        'ce dernier', 'réduit', '1|2', 'car|Comme', r'immersion \deleted', r'\underline{i}', 'Catégorie dans', 'au dessus de la catégorie', "15'", r'plongement \deleted',
        r'strict \unsure', r'C_{\Sigma,d,d', 'standart}', '24|29']
tot_u = tot_i = tot_u0 = tot_i0 = 0
for name, body in files.items():
    body = body if body.endswith('\n') else body + '\n'
    open(os.path.join(out, name), 'w', encoding='utf-8', newline='\n').write(body)
    old = open(os.path.join(fp, name), encoding='utf-8').read()
    bal = body.count('{') - body.count('}')
    u, i = body.count(r'\unsure{'), body.count(r'\illegible{')
    u0, i0 = old.count(r'\unsure{'), old.count(r'\illegible{')
    tot_u += u; tot_i += i; tot_u0 += u0; tot_i0 += i0
    nl, ol = body.splitlines(), old.splitlines()
    changed = sum(1 for a, b in zip(nl, ol) if a != b) + abs(len(nl) - len(ol))
    print(f'{name}: lines {len(ol)}->{len(nl)}, brace balance {bal}, unsure {u0}->{u}, illegible {i0}->{i}, differing lines ~{changed}')
    for k in keys:
        for n, line in enumerate(nl, 1):
            if k in line:
                print(f'   L{n}: [{k}]')
                break
print('TOTAL unsure', tot_u0, '->', tot_u, '; illegible', tot_i0, '->', tot_i)
print(sorted(os.listdir(out)))
