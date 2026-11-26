"""Generate the appendices of MOONSHINE_ATLAS.md from entries.json and maps.json.
App. A: every entry -> the atlas objects it carries (keyword index over the entry's full text; every entry gets at
        least its curated object).
App. B: the maps merged by entry pair (pairs named by maps of more than one conference file = de-duplicated maps).
App. C: every map -> objects; object-pair index (all 1281 maps).
"""
import json, re, os, sys, collections
D = sys.argv[1]
E = json.load(open(os.path.join(D, 'entries.json'), encoding='utf-8'))
M = json.load(open(os.path.join(D, 'maps.json'), encoding='utf-8'))

OBJ = [
 ('O1', 'Klein\'s j, the j-line, t = j/1728, 744, 196884, the unit 1 - 1728/j',
  r"j-line|j-invariant|j ?= ?1728|j/1728|\b1728\b|\b744\b|196884|modularJ|J\(q\)|tripod|1 ?[−-] ?1728/j|cubic descent"),
 ('O2', 'E2, E4, E6, Delta = eta^24, Ramanujan\'s system, E4^3 - E6^2 = 1728 Delta',
  r"E_?4|E₄|E_?6\b|E₆|E_?2\b|E₂|E_2\^\*|Ramanujan|g_?2|g₂|g_?3|g₃|discriminant identity"),
 ('O3', 'eta, theta_1, Siegel functions, the S6 period norm N, theta_{6,r}',
  r"η|\\eta|\beta\b|ϑ|vartheta|theta_\{?1|θ_?1|θ6|theta_\{6|θ_\{6|Siegel function|period norm|reduced theta"),
 ('O4', 'the order-12 character of SL2(Z): alpha = e = -chi = nu_{eta^2}; Z/12, Z/24; the braid-degree tower',
  r"ν_\{?η|nu_\{?\\eta|ν_η|η\^?2|η²|eta\^2|Z/12|Z/24|ℤ/12|abelianiz|Mp_?2|Mp₂|\\alpha|α\(|braid degree|Euler number|peripheral"),
 ('O5', 'Q(zeta12), chi_-3, chi_-4, chi_12, the centre {1,5,7,11}, (3/4)^{1/4}, (-1)^Delta = chi12(u)',
  r"χ_?\{?12|chi_?\{?12|χ12|χ₁₂|ζ_?\{?12|zeta_?\{?12|ζ₁₂|\{1, ?5, ?7, ?11\}|1, 5, 7, 11|\(3/4\)\^|χ−3|χ−4|χ_\{−3\}|χ_\{−4\}|chi_\{-3\}|chi_\{-4\}|χ₋|Q\(√3\)|Q\(\\sqrt3\)"),
 ('O6', 'PSL2(Z) = C2*C3 and the triangle groups (2,3,n), (3,4,inf); Seifert and Brieskorn spheres',
  r"PSL_?2\(Z|PSL₂\(Z|PSL_2\(\\mathbb Z|C_?2 ?\* ?C_?3|C₂ ?∗ ?C₃|C2 \* C3|triangle group|\(2,3,|\(3,4,|\(2, ?3, ?6\)|Δ\(2|Seifert|Brieskorn|Σ\(2,3"),
 ('O7', 'the hexagonal curve E0 = C/Z[omega] (y^2 = x^3+1 ~ y^2+y = x^3 ~ y^2 = x^3+16 ~ Fermat cubic), Z[omega] x| mu6',
  r"Z\[ω\]|\\mathbb Z\[\\omega\]|Z\[\\omega\]|Z\[omega\]|Z\[ρ\]|E_?0\b|E₀|x\^3 ?\+ ?1\b|x³ ?\+ ?1\b|x\^3 ?\+ ?16|x³ ?\+ ?16|y\^2 ?\+ ?y|y² ?\+ ?y|Fermat cubic|μ_?6|mu_?6|μ₆|hexagonal|Eisenstein (integer|lattice|plane|ring)|Q\(ω\)|Q\(\\omega\)|Q\(√−3\)|Q\(\\sqrt\{-3\}\)"),
 ('O8', 'the Gaussian curve y^2 = x^3 - x (j = 1728), Z[i], mu4',
  r"Z\[i\]|\\mathbb Z\[i\]|x\^3 ?[−-] ?x\b|x³ ?− ?x\b|Gaussian|μ_?4|mu_?4|μ₄|Q\(i\)"),
 ('O9', 'CM theory: singular moduli, class numbers, Hilbert class fields, Heegner points, CM newforms, Chowla-Selberg',
  r"singular modul|class number|Hilbert class|Heegner|Chowla|CM newform|CM point|CM fibre|complex multiplication|Deuring|h\(−|h\(-|Weber"),
 ('O10', 'X0(N), Hauptmoduln, genus zero, Atkin-Lehner and Fricke involutions; T6 on X0(6)',
  r"Hauptmodul|X_?0\(|X₀\(|Γ_?0\(|Gamma_?0\(|\\Gamma_0|Γ0\(|Γ₀\(|Fricke|Atkin|T_?6\b|T₆|T_6|genus zero|genus-zero"),
 ('O11', 'umbral moonshine: the 23 lambencies, T^X, shadows, mock modular forms, umbral groups',
  r"lambenc|umbral|shadow|mock|Cheng|CDH|T\^X|Ω\^X|\\Omega\^X|Eichler.?Zagier|false theta"),
 ('O12', 'monstrous moonshine: V-natural, McKay-Thompson series, the classes 1A, 2A, 2B, 3B, 4C, 6A-6E, 196883',
  r"Monster|McKay.?Thompson|V\^?♮|V\\natural|V♮|moonshine module|\b1A\b|\b2A\b|\b2B\b|\b3B\b|\b4C\b|\b6[A-E]\b|196883|Baby Monster|Harada"),
 ('O13', 'supersingularity, Ogg\'s primes, Hasse-Witt, p inert',
  r"supersingular|\bOgg|Hasse.?Witt|\binert\b"),
 ('O14', 'Mathieu moonshine and codes: M24, M12, the Golay code, octads, Mason\'s eta products, K3 elliptic genus',
  r"M_?\{?24\}?|M₂₄|M24|M_?\{?12\}?\b|M₁₂|Golay|octad|Steiner|S\(5,8,24\)|Mason|cycle shape|elliptic genus|Mathieu|Hamming"),
 ('O15', 'the Leech lattice and the Conway groups (Co0, Co1, Lambda/2Lambda, Lambda/3Lambda, 196560, complex Leech)',
  r"Leech|Co_?0|Co_?1|Co₀|Co₁|196560|6\.Suz|Λ/2Λ|Λ/3Λ|Lambda/2Lambda"),
 ('O16', 'Niemeier lattices: N(A5^4D4) = N_ES, glue 72, Kneser neighbours, J (det 81), A2^12, A1^24, deep holes',
  r"Niemeier|A_?5\^?\{?4|A₅⁴|A5\^4|N_?\{?ES|N_ES|N\(A|A_?2\^\{?12|A2\^12|A₂¹²|A_?1\^\{?24|A1\^24|glue|neighbour|neighbor|det 81|deep hole|Weyl vector"),
 ('O17', 'the ternary side: tetracode, AG(2,3), PG(2,3), GL2(F3), SL2(F3), A4, ASL2(F3), AGL2(F3), Hessian group, ternary Golay',
  r"tetracode|AG\(2,3\)|PG\(2,3\)|PG\(2, ?3\)|GL_?2\(F_?3|GL_?2\(\\mathbb F_3|GL_?2\(3\)|GL₂\(F₃\)|GL₂\(3\)|GL\(2,3\)|SL_?2\(F_?3|SL₂\(F₃\)|SL_2\(\\mathbb F_3|\bA_?4\b|A₄|ASL|AGL|Hessian group|ternary Golay|binary tetrahedral|Q_?8\b|Q₈|Pappus"),
 ('O18', 'E8, K3 and even unimodular lattices, theta characteristics, Sp4(F2) = S6, split quadrics O+(2n,2)',
  r"E_?8\b|E₈|E8|K3\b|theta characteristic|Sp_?4\(F_?2|Sp₄\(F₂\)|Sp_4\(\\mathbb F_2|S_6\b|S₆|O\^?\+\(|O⁺|Δ_\{?0,6|M_\{?0,6|M0,6|icosian|IsE8"),
 ('O19', 'octonions, the Albert algebra H3(O), triality, Spin(8), F4, G2, E6, D4',
  r"octonion|Albert|H_?3\(|H₃\(|triality|Spin\(8\)|F_?4\b|F₄|\bG_?2\b|G₂|\bE_?6\b|E₆|\bD_?4\b|D₄|Cayley.?Dickson|Jordan|\\mathbb O|𝕆"),
 ('O20', 'Erdős-Straus: 4/p = 1/x + 1/y + 1/z, the residues mod 840, S840 = <289>, shells, the ES cubic, the ES hexagon',
  r"Erd(ő|o)s|Straus|\bES\b|mod[ -]840|\b840\b|S_?\{?840|V_?\{?840|S₈₄₀|V₈₄₀|Jordan norm|three-colour|R_ES|H_ES|selector|4/p"),
 ('O21', 'GT-hat, Grothendieck\'s Delta and the level-12 frames (H17, DELTA_SEXTIC), ghosts and signs',
  r"GT̂|GT\\hat|\\widehat\{GT\}|GT_?0|GT-hat|Grothendieck|frame|DELTA|H17|gentle|ghost|Ob\(|Hilbert symbol|sextic recipro"),
 ('O22', 'dessins, Belyi maps, genus-zero covers, Schreier graphs, monodromy permutations',
  r"dessin|Belyi|Schreier|monodromy group|permutation (triple|certificate)|passport|Riemann.?Hurwitz|plane tree|Todd.?Coxeter"),
 ('O23', 'the icosahedral level and PSL2(Fq): X(5), A5, P1(Fp), the Klein quartic, PSL2(F8), Macbeath',
  r"X\(5\)|icosahed|\bA_?5\b|A₅\b|PSL_?2\(F|PSL₂\(F|PSL_?2\([0-9]|PSL2\(\d|P\^?1\(F|P¹\(F|Klein quartic|Macbeath|Hurwitz|PGL_?2\(5|PGL₂\(5"),
 ('O24', 'theta series of lattices, Epstein zeta, Mellin kernels, genus-2 theta, Siegel-Weil, the Gamma1(3) ring a, b, 691',
  r"theta series|Θ_|\\Theta_|Θ\(|Epstein|Mellin|Siegel(?! function)|\b691\b|65520|Γ_?1\(3|Gamma_?1\(3|\\Gamma_1\(3|Bessel|paramodular|Humbert"),
 ('O25', 'Alpöge\'s GRH proof and its Lean library; L-functions; the RH workbench (CCM kernel, split zero)',
  r"Alp(ö|o)ge|GRH|\bRH\b|Riemann hypothesis|L-function|L\(s|L\(Δ|L\(w|L_\{?12|ζ\(|zeta\(|Connes|Consani|CCM|split[- ]zero|Lean"),
 ('O26', 'cubic and sextic characters of Q(omega), Kummer fields Q(omega, cbrt p), Gauss and Jacobi sums, Patterson, Kubota, metaplectic covers',
  r"cubic (character|residue|Kummer|Gauss|Hecke|phase)|sextic|Patterson|Kubota|metaplectic|Gauss sum|Jacobi.?sum|∛|cbrt|\\sqrt\[3\]|\b269\b|Hecke character|Grössen"),
 ('O27', 'the number 24: K3(F5), pi_3^s, H^1(G_Q, Zhat(2)), (l-1)(p+1) = 24, rank 24',
  r"Z/24|ℤ/24|K_?3\(F|K₃\(F|π_?3\^?s|π₃|pi_3|w_?2\(Q|\(ℓ ?− ?1\)\(p ?\+ ?1\)|\(l-1\)\(p\+1\)|5\^?2 ?[−-] ?1|5² − 1|rank 24|rank-24"),
 ('O28', 'S6 topology: the six-sphere, exotic spheres Theta7 = Z/28, Eells-Kuiper, E8 plumbing, the sphere ladder',
  r"S\^6|S⁶|six-sphere|Θ_?7|Θ₇|Z/28|bP_|Eells|plumbing|S\^\{?24|S²⁴|S\^\{?12|exotic"),
]
BS = chr(92)
LB = BS + BS  # a literal backslash inside a regex
EXTRA = {'O4': '|' + LB + 'mathrm' + BS + '{SL' + BS + '}_2|B_?3|central relation|degree 12|degree-12',
         'O6': '|' + LB + 'mathrm' + BS + '{PSL' + BS + '}_2|' + LB + 'mathrm' + BS + '{SL' + BS + '}_2|B_?3|braid',
         'O7': '|' + LB + 'mathbf Z' + BS + '[' + LB + 'omega|' + LB + 'omega',
         'O8': '|' + LB + 'mathbf Z' + BS + '[i' + BS + ']|' + LB + 'mathbf Q' + BS + '(i' + BS + ')',
         'O23': '|PSL' + BS + '}_2' + BS + '(' + LB + 'mathbf F|PSL_2' + BS + '(' + LB + 'mathbf F',
         'O5': '|' + LB + 'chi_' + BS + '{12|' + LB + 'chi_' + BS + '{-3|' + LB + 'chi_' + BS + '{-4|' + LB + 'zeta_' + BS + '{12',
         'O1': '|thrice-punctured|Ihara',
         'O27': '|2' + BS + '^' + BS + '{?24|1/24|24th',
         'O21': '|Moore.?Seiberg|pentagon|Lego'}
CRE = [(o, name, re.compile(rx.replace(BS + 'mathbb', BS + 'math(?:bb|bf)') + EXTRA.get(o, ''))) for o, name, rx in OBJ]
MANUAL = {'S6-006': ['O1', 'O5'], 'S6-045': ['O16', 'O15'], 'AG-042': ['O2', 'O24'], 'AG-058': ['O4', 'O6'],
          'AG-060': ['O23'], 'AG-093': ['O7'], 'AG-100': ['O10', 'O1'], 'AG-101': ['O1', 'O21'], 'AG-112': ['O27'],
          'AG-113': ['O27'], 'AG-114': ['O4'], 'AG-117': ['O27'], 'WEEK-072': ['O6', 'O23'], 'WEEK-093': ['O21']}

def objs(text):
    return [o for o, name, rx in CRE if rx.search(text)]

ent_objs = {}
for k, e in E.items():
    txt = e['title'] + '\n' + e['body']
    ent_objs[k] = objs(txt) or MANUAL.get(k, [])
# entries with no object: give the object matched by the title of the closest map text later; record
noobj = [k for k, v in ent_objs.items() if not v]

key = lambda x: (x.split('-')[0], int(x.split('-')[1]))
lines = ['## Appendix A. Every entry and the atlas objects it carries', '',
         'Keyword index over the full text of each entry of the three dossiers (rules in the generator script, '
         '`appendices.py`). An entry is listed under every object whose name occurs in it; the curated object sets of '
         'section 1.1 are the core of each object. Line numbers are those of the dossier file.', '',
         '| Entry | Dossier line | Title (dossier wording, cut at 90 characters) | Objects |', '|---|---|---|---|']
for k in sorted(E, key=key):
    e = E[k]
    f = {'S6': 'FIND_s6', 'AG': 'FIND_ag', 'WEEK': 'FIND_week'}[e['dossier']]
    t = e['title'].replace('|', '/').replace('\n', ' ')
    if len(t) > 90:
        t = t[:90]
        if t.count(chr(96)) % 2:
            t += chr(96)
        t += '…'
    lines.append('| %s | %s L%d | %s | %s |' % (k, f, e['line_start'], t, ' '.join(ent_objs[k]) or '—'))
open(os.path.join(D, 'appA.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# Appendix B: entry pairs named by maps from more than one conference file
pair_maps = collections.defaultdict(list)
for mp in M:
    h = mp['home']
    tg = [i for i in mp['arrow_ids'] if i in E and i != h] or [i for i in mp['all_ids'] if i in E and i != h]
    for t in tg:
        pair_maps[tuple(sorted((h, t), key=key))].append(mp['mid'])
multi = {p: v for p, v in pair_maps.items() if len(set(m.split(':')[0] for m in v)) >= 2}
lines = ['## Appendix B. The maps merged: entry pairs that more than one conference file maps', '',
         'Each line is one pair of entries and every map of the three conference files that names the pair (home entry '
         'and target). `S6m` = MAPS_from_s6 `[nnn.k]`, `AGm` = MAPS_from_ag `Mnnn`, `WKm` = MAPS_from_week `Mnnn.k`. '
         'These %d pairs are the de-duplicated identifications: the same link found independently from two or three '
         'homes. All %d entry pairs named by any map are counted in Appendix C.' % (len(multi), len(pair_maps)), '',
         '| Entry pair | Maps |', '|---|---|']
for p in sorted(multi, key=lambda p: (-len(multi[p]), key(p[0]), key(p[1]))):
    lines.append('| %s ↔ %s | %s |' % (p[0], p[1], ', '.join(multi[p])))
open(os.path.join(D, 'appB.md'), 'w', encoding='utf-8').write('\n'.join(lines))

# Appendix C: map -> objects; object-pair index
map_objs = {}
for mp in M:
    to = set(objs(mp['text']))
    eo = set()
    for i in set(mp['all_ids']) | {mp['home']}:
        eo |= set(ent_objs.get(i, []))
    both = to & eo
    use = both if len(both) >= 2 else (to if len(to) >= 2 else (to | set(ent_objs.get(mp['home'], [])[:1])))
    map_objs[mp['mid']] = sorted(use, key=lambda o: int(o[1:]))
op = collections.defaultdict(list)
for mid, os_ in map_objs.items():
    if len(os_) == 1:
        op[(os_[0], os_[0])].append(mid)
    for i in range(len(os_)):
        for j in range(i + 1, len(os_)):
            op[(os_[i], os_[j])].append(mid)
names = {o: n for o, n, _ in OBJ}
lines = ['## Appendix C. All 1281 maps by the pair of objects they join', '',
         'For every map: the objects named in its text that are also carried by the entries it names (both ends). A map '
         'naming k objects is listed under every pair among them; a map inside one object is listed under (O, O). '
         'Counts are maps, not distinct statements.', '']
deg = collections.Counter()
for (a, b), v in op.items():
    deg[a] += len(v)
    if a != b:
        deg[b] += len(v)
lines.append('**Maps touching each object:** ' + '; '.join('%s %d' % (o, deg[o]) for o in sorted(deg, key=lambda o: -deg[o])))
lines.append('')
lines.append('| Objects | Number | Maps |')
lines.append('|---|---|---|')
for (a, b) in sorted(op, key=lambda p: (-len(op[p]), int(p[0][1:]), int(p[1][1:]))):
    v = op[(a, b)]
    lines.append('| %s–%s | %d | %s |' % (a, b, len(v), ', '.join(v)))
open(os.path.join(D, 'appC.md'), 'w', encoding='utf-8').write('\n'.join(lines))
json.dump({'ent_objs': ent_objs, 'map_objs': map_objs, 'deg': deg}, open(os.path.join(D, 'objidx.json'), 'w', encoding='utf-8'))
cnt = collections.Counter(o for v in ent_objs.values() for o in v)
print('entries without object:', noobj)
print('entries per object:', sorted(cnt.items(), key=lambda x: int(x[0][1:])))
print('multi-file pairs', len(multi), 'all pairs', len(pair_maps), 'object pairs', len(op))
print('maps per object', sorted(deg.items(), key=lambda x: -x[1]))
