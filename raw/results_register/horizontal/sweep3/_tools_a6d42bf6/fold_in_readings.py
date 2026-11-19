# Fold the readings decided on the native scans by the sweep-3 block readers (19 Nov 2026) into the second-pass page files,
# in second_pass/out and in the archive clone, and log each change in the block's *_changes.md (agent a6d42bf6, at the
# main session's word of 19 Nov ~03:3x UTC). Only readings decided on the ink; no mathematical correction.
# usage: python -I -B fold_in_readings.py [--apply]
import io, os, sys
sys.stdout.reconfigure(encoding='utf-8')
APPLY = '--apply' in sys.argv
D = 'C:/Users/user/Documents'
ROOTS = [D + '/grothendieck_archive_transcription_20261110/second_pass/out/{pkg}',
         D + '/github_backup_20261113/grothendieck-montpellier-archive/packages/{pkg}/second_pass']
P1, P2, P3 = 'MPL_150_001-043', 'MPL_150_044-084', 'MPL_150_085-099+151_001-031'
R = {'a': 'a00ca4596e2185740', 'b': 'a81a7989e5a443c82', 'c': 'a1826390c189eb13e', 'd': 'a7e8cd48a67cebfa2',
     'e': 'a3c1b6772b35008a9', 'g': 'abca10fad1b368563', '151b': 'a0370fd91592796de'}
# (package, cote, scan, block changes file suffix, old, new, correction id, reader key)
CH = [
 (P1, '150', 2, '150-001-150-016', r'b) $\Sigma_{jk}\longrightarrow\Sigma_k$', r'b) $\Sigma_{\unsure{ik|jk}}\longrightarrow\Sigma_k$', 'SA10-K150a-02', 'a'),
 (P1, '150', 8, '150-001-150-016', r'$\unsure{\Sigma_{012}|\Sigma_{12}}\longrightarrow\Sigma_{12}$', r'$\Sigma_{012}\longrightarrow\Sigma_{12}$', 'SA10-K150a-10', 'a'),
 (P1, '150', 8, '150-001-150-016', r'\Sigma_{012}\longrightarrow\Sigma_{\unsure{02|2}}$', r'\Sigma_{012}\longrightarrow\Sigma_{\unsure{2|02}}$', 'SA10-K150a-11', 'a'),
 (P1, '150', 14, '150-001-150-016', r'i.e. (\unsure{7|8}) devient faux', r'i.e. (7) devient faux', 'SA10-K150a-15', 'a'),
 (P1, '150', 18, '150-017-150-030', r'les $\unsure{Y_i|T_i}$ sont coniques', r'les $Y_i$ sont coniques', 'SA10-K150b-03', 'b'),
 (P1, '150', 19, '150-017-150-030', r'\unsure{\deleted{globalement}|\uline{globalement}} loc. triviale', r'\deleted{globalement} loc. triviale', 'SA10-K150b-07', 'b'),
 (P1, '150', 22, '150-017-150-030', r"s'il est \inserted{$\exists\lambda", r"s'il \inserted{$\exists\lambda", 'SA10-K150b-12', 'b'),
 (P1, '150', 27, '150-017-150-030', r'\unsure{\dot E_J|E_J}\cap\dot T', r'\dot E_J\cap\dot T', 'SA10-K150b-04 (reading part)', 'b'),
 (P1, '150', 34, '150-031-150-043', r'\unsure{j|i},j\in I^*', r'j,j\in I^*', 'SA10-K150c-03', 'c'),
 (P2, '150', 44, '150-044-150-057', r'$\Sigma_*^{\leq \unsure{z|2}}\longrightarrow I^{\leq \unsure{j|2}}$', r'$\Sigma_*^{\leq z}\longrightarrow I^{\leq j}$', 'SA10-K150d-10', 'd'),
 (P2, '150', 47, '150-044-150-057', r"\longrightarrow\unsure{\Sigma_{d'}|\Sigma_d}$ soit", r"\longrightarrow\Sigma_{d'}$ soit", 'SA10-K150d-01', 'd'),
 (P2, '150', 48, '150-044-150-057', r'est \unsure{stricte|saturée}, i.e.', r'est stricte, i.e.', 'SA10-K150d-12', 'd'),
 (P2, '150', 63, '150-058-150-071', r'd) $\uline{\unsure{s|b}}:', r'd) $\uline{s}:', 'SA10-K150e-05', 'e'),
 (P2, '150', 66, '150-058-150-071', r'$\unsure{b_{ki}|b_{ik}}:\unsure{\Sigma_{ki}}', r'$b_{ik}:\unsure{\Sigma_{ki}}', 'SA10-K150e-04 (reading part)', 'e'),
 (P2, '150', 67, '150-058-150-071', r'$\unsure{s_{ij}|s_{jk}}:\unsure{\Sigma_{ik}|\Sigma_{jk}}\longrightarrow\Sigma_j$', r'$s_{ij}:\unsure{\Sigma_{ik}|\Sigma_{jk}}\longrightarrow\unsure{\Sigma_i|\Sigma_j}$', 'SA10-K150e-10', 'e'),
 (P3, '150', 95, '150-085-150-099', r'\unsure{partie ouverte|pro-vois ouvert} de $X$ est \unsure{normale|normal}', r'partie ouverte de $X$ est normale', 'SA10-K150g-14', 'g'),
 (P3, '151', 20, '151-018-151-031', r'X_3\arrow[r,"\unsure{p_1|\delta_1}"]\&X_2\\', r'''X_3\&X_2\arrow[l,hook',"\unsure{\delta_1|p_1}"']\\''', 'SA10-K151b-01', '151b'),
 (P3, '151', 25, '151-018-151-031', r'X_3\arrow[r,"{\delta_1=d=((x,y)\longmapsto(x,y,y))}"]\&X_2\arrow[d,dash,"\delta_0"]\\', r'''X_3\&X_2\arrow[l,hook',"{\delta_1=d=((x,y)\longmapsto(x,y,y))}"']\arrow[d,dash,"\delta_0"]\\''', 'SA10-K151b-02', '151b'),
 (P3, '151', 25, '151-018-151-031', r'\text{si }\unsure{i=1|i=2}', r'\text{si }i=1', 'SA10-K151b-03', '151b'),
]
OPEN = {
 (P1, '150-001-150-016'): ['016 l.27 (margin): `\\uline{\\unsure{strict|pur}}` left as it is: the native scan does not decide it; it needs the user\'s eye (reader a00ca4596e2185740).'],
 (P3, '151-001-151-017'): ['The letter conventions ζ|ξ and 𝔖|𝒢 of cote 151 (about 92 doubt marks over 151/001-031) are left as they are: they need a human look at a sample of the scans.'],
 (P3, '151-018-151-031'): ['The letter conventions ζ|ξ and 𝔖|𝒢 of cote 151 (about 92 doubt marks over 151/001-031) are left as they are: they need a human look at a sample of the scans (reader a0370fd91592796de).'],
}
changed = set(); rows = {}
for pkg, cote, sc, blk, old, new, cid, rk in CH:
    for root in ROOTS:
        base = root.format(pkg=pkg)
        p = f'{base}/{pkg}_{cote}_scan{sc:03d}.tex'
        t = io.open(p, encoding='utf-8', newline='').read()
        n = t.count(old)
        if n != 1:
            print('MISMATCH', n, p, old[:60]); continue
        line = t[:t.index(old)].count('\n') + 1
        if APPLY:
            io.open(p, 'w', encoding='utf-8', newline='').write(t.replace(old, new, 1)); changed.add(p)
        rows.setdefault((base, pkg, blk), []).append((f'{cote}/{sc:03d}', f'l.{line}', old, new, cid, R[rk]))
    print('ok', pkg, cote, sc, cid)
def esc(s): return s.replace('|', '\\|')
for (base, pkg, blk), rr in rows.items():
    f = f'{base}/{pkg}_{blk}_changes.md'
    sec = ['', '## Fold-in of 19 Nov 2026: readings decided on the native scan in sweep 3, round 2', '',
           'Folded in by Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8) at the main session\'s word. Only readings decided on the ink;',
           'the mathematical corrections of the same readings are in `results_register/horizontal/sweep3/SA10/readings/` and are not applied here.', '',
           '| Scan | Line | Before | After | Decided by | Date |', '|---|---|---|---|---|---|']
    for sc, ln, old, new, cid, rid in rr:
        sec.append(f'| {sc} | {ln} | `{esc(old)}` | `{esc(new)}` | {rid} (Claude Opus 5.5 at effort max), sweep 3 reading, {cid} | 2026-11-19 |')
    for o in OPEN.get((pkg, blk), []):
        sec += ['', '**Open (left as it is):** ' + o]
    if APPLY:
        t = io.open(f, encoding='utf-8', newline='').read()
        if 'Fold-in of 19 Nov 2026' not in t:
            io.open(f, 'a', encoding='utf-8', newline='').write('\n'.join(sec) + '\n'); changed.add(f)
# open items in blocks without changes
for (pkg, blk), oo in OPEN.items():
    for root in ROOTS:
        base = root.format(pkg=pkg)
        if (base, pkg, blk) in rows: continue
        f = f'{base}/{pkg}_{blk}_changes.md'
        sec = ['', '## Fold-in of 19 Nov 2026: readings decided on the native scan in sweep 3, round 2', '', 'No reading of this block was changed in the fold-in.'] + sum([['', '**Open (left as it is):** ' + o] for o in oo], [])
        if APPLY:
            t = io.open(f, encoding='utf-8', newline='').read()
            if 'Fold-in of 19 Nov 2026' not in t:
                io.open(f, 'a', encoding='utf-8', newline='').write('\n'.join(sec) + '\n'); changed.add(f)
print('\n'.join(sorted(changed)) if changed else 'dry run: nothing written')
