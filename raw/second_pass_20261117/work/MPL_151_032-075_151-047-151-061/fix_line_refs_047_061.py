"""Correct line references in this block's changes and notes files (each replacement must match exactly once)."""
import io
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'out', 'MPL_151_032-075'))
FIXES = {
    'MPL_151_032-075_151-047-151-061_changes.md': [
        ('| 1 | 047 | l. 9, "X étant', '| 1 | 047 | l. 10, "X étant'),
        ('| 10 | 051 | l. 10, "non dégénérés', '| 10 | 051 | l. 11, "non dégénérés'),
        ('| 11 | 051 | l. 14, end of the NB sentence', '| 11 | 051 | l. 15, end of the NB sentence'),
        ('| 25 | 056 | NB, l. 14,', '| 25 | 056 | NB, l. 16,'),
    ],
    'MPL_151_032-075_151-047-151-061_notes_checked.md': [
        ('"de façon bien connue" (048 l.28)', '"de façon bien connue" (048 l.29)'),
        ('(049 l.25 and l.32;', '(049 l.25 and l.33;'),
        ('"sont strictement croissants" (051 l.14,', '"sont strictement croissants" (051 l.15,'),
        ('X_Δ0×X_Δ0" (051 l.16–17,', 'X_Δ0×X_Δ0" (051 l.17–18,'),
        ('now settled\n  (052 l.6, #12)', 'now settled\n  (052 l.7, #12)'),
        ('la relation (20)" (052 l.9)', 'la relation (20)" (052 l.11)'),
        ('formelle\'\' :" (052 l.10;', 'formelle\'\' :" (052 l.12;'),
        ('(20) stands on 051 l.34', '(20) stands on 051 l.31'),
        ('pas un espace semi-simplicial" (056 l.14)', 'pas un espace semi-simplicial" (056 l.16)'),
        ('``bord\'\'" (l.14, #25)', '``bord\'\'" (l.16, #25)'),
        ('**056-02**. **Keep.** 056 l.16 unchanged.', '**056-02**. **Keep.** 056 l.18 unchanged.'),
    ],
}
for name, pairs in FIXES.items():
    path = os.path.join(BASE, name)
    text = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            print('NOT APPLIED (%d matches) in %s: %r' % (n, name, old))
            continue
        text = text.replace(old, new)
    io.open(path, 'w', encoding='utf-8', newline='').write(text)
    print('done', name)
