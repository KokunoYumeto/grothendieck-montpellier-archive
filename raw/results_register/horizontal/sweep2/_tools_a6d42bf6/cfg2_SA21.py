# Sweep 2, SA21 gap entries (56 Codex notes on the sheets, cote 156 parts 7-9 and H156-01): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
import re
DATE = '2026-11-18'
ITEMS2 = []
PART_ITEM = {'7': 'SA21-10', '8': 'SA21-15', '9': 'SA21-10'}
SHORT = {'SA21-10': 'ateliers: the axioms At, sub-ateliers, saturation, magmas with strata, disjunctors, morphisms', 'SA21-15': '156-8: magasins and oriented multistrata, polyhedral ateliers, homomorphisms, lieux, supports',
         'SA21-11': 'documentary of cote 156'}
OBJ_UPDATE = {
 'SA21-10': 'ateliers (workshops): not defined in 156-1, 156-2 (D16); defined and used in 156-6 ("Analysis situs (deuxième mouture)"), 156-7 ("Analysis Situs (troisième mouture)", Chap VII, 23 June 1986) and 156-9 (GF IX, 5-15 July 1986): sub-ateliers, the axioms At, saturation, spatial ateliers, multiombre and ombres, quasi-correspondences, disjunctors and "Spotos", magmas with strata, morphisms of ateliers',
 'SA21-11': 'documentary: covers, title sheets, dates and pagination of cote 156; the 1986 series marked GF (or CF) III to IX bis, 8 June to 15 July 1986; reused Récoltes et Semailles typescript leaves (typed p. 936 with note 171(i), 1985; typed pp. 951-953 and 1074-1088, 6 and 8 May 1986)',
 'SA21-15': '156-8 (CF VIII, 27 June - 4 July 1986): magasins généraux and oriented multistrata ("magasins orienteurs"), polyhedral ateliers, homomorphisms of magasins and ateliers, axioms for lieux and the gluing of refinements, supports and constructible supports, the magma associated with an ordered set; elementary figures',
}

def place(g):
    i = g['entry_id']; f = g['folder']; k = int(i.split('#')[1])
    m = re.match(r'J156-(\d+)-', f)
    part = m.group(1) if m else '7'
    it = PART_ITEM[part]
    cote = '156-' + part
    if k == 2:
        return dict(item='SA21-11', cote=cote, kind='Codex notes on the sheets: title sheets, dates and page counts', object=f'documentary of cote {cote} ({f}): title sheets, dates and pagination',
                    basis='entry-read', note=f'compact read (dates, quoted titles); subject item {it}')
    return dict(item=it, cote=cote, kind='Codex notes on the sheets: steps the pages mark as unverified', object=f'{SHORT[it]} ({f}): steps the pages mark as unverified', basis='entry-read', note='opening read')

OVERRIDE = {
 'codex:H156-01#2': dict(note='"Analysis Situs (troisième mouture)", "Chap VII", 23 juin: the third version, after 156-4 (10 June) and 156-6 (18 June)'),
 'codex:J156-8-01#2': dict(flag='a link across folders', note='CF VIII; "Magasins généraux"; "Multistrates orientés - magasins orienteurs"; a reused typescript p. 936 with note 171(i) "L\'ancêtre", 1 March and 2-8 May 1985, citing "L\'Apothéose", "Les joyaux", "La maffia": Récoltes et Semailles (my identification)'),
 'codex:J156-9-15#1': dict(note='113: "pas OK!"; 112-114: the cancelled reused typescript qualifies historical claims ("J\'en doute fortement à présent")'),
 'codex:J156-9-15#2': dict(flag='a link across folders', note='typed pp. 951-953 ("6 mai 1986") and 1074-1088 ("8 mai 1986"), NA 20, NA 27: the Récoltes et Semailles typescript (my identification), cancelled and reused'),
 'codex:J156-9-01#2': dict(note='"GF IX"; 5 and 15 July 1986: the series runs to 15 July'),
 'codex:J156-8-02#2': dict(note='27 juin; "Cas des figures", "Recollement des raffinements", "Axiomes pour les Lieux"'),
 'codex:J156-7-12#1': dict(note='97-99: "Faux" beside the proposed formal lemma and lemma 3; "Mais c\'est faux!": his own corrections'),
}
CROSS2 = {'SA21-11': 'the Récoltes et Semailles typescript also in cote 84 (= H01T; SA02-6, SA01-37)', 'SA21-15': 'SA21-6 (= H0KJ; lieux and cuttings, 156-1/2)', 'SA21-10': '= H0K9'}
ITEM_FLAGS2 = {'SA21-11': 'a link across folders (Récoltes et Semailles typescript in cotes 84 and 156)'}
FLAGS2 = [
 ['a link across folders', 'codex:J156-8-01#2 (156-8, scan 5); codex:J156-9-15 (156-9, scans 112-114)', 'Reused typescript leaves in cote 156: typed p. 936 with note 171(i) "L\'ancêtre" (1 March and 2-8 May 1985), citing "L\'Apothéose", "Les joyaux", "Le jour de gloire", "La maffia"; typed pp. 951-953 and 1074-1088 dated 6 and 8 May 1986, cancelled, with historical claims qualified "J\'en doute fortement à présent". The cited titles identify Récoltes et Semailles (my identification), the typescript also reused in cote 84 (= H01T). Terminus post quem May 1986 for these GF sheets.', 'entries read'],
 ['a link across folders', 'codex:H156-01#2 (156-7, scan 2)', '"Analysis Situs (troisième mouture)", Chap VII, 23 June: the third version, after the première mouture (156-4, 10 June) and the deuxième mouture (156-6, 18 June). The GF series also runs to GF IX, 15 July 1986 (J156-9-01).', 'entry read'],
 ['a link across folders', 'codex:J156-8-02#2, J156-8-04#2, J156-8-07#2, J156-8-15#2 (156-8)', '156-8 returns to the lieux of 156-1/2 ("Axiomes pour les Lieux", "Recollement des raffinements") and introduces magasins, polyhedral ateliers and constructible supports: SA21-15 joins SA21-6 (cuttings and lieux) and SA21-10 (ateliers).', 'entries read'],
 ['a link across folders', 'codex steps entries of J156-7-12, J156-9-04, J156-9-08, J156-9-14, H156-01', 'His own "Faux", "Mais c\'est faux!" and "pas OK!" marks beside lemmas and formulas in 156-7 and 156-9: self-corrections recorded by the Codex notes.', 'entries read'],
]
CHECKS2 = []
NOTES2 = '''
## Sweep 2, part 1: the gap entries (18 Nov 2026)

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. There were 56 gap entries, the Codex notes on the sheets of 28 folders: H156-01, five of 156-7, ten of 156-8 and twelve of 156-9. Sweep 1 missed these 27 J156 folders because their files use a different heading level. All are placed:

| Entry | Item |
|---|---|
| Steps entries, 156-7 and 156-9 | SA21-10 |
| Steps entries, 156-8 | SA21-15 |
| Title-sheet entries | SA21-11 |

I extended the objects of SA21-10, SA21-11 and SA21-15.

**What the entries add:**
- H156-01 is "Analysis Situs (troisième mouture)", Chap VII, 23 June 1986, the third version after 156-4 and 156-6.
- 156-8 (CF VIII) holds:
  - the magasins and oriented multistrata;
  - polyhedral ateliers and homomorphisms of magasins and ateliers;
  - axioms for lieux;
  - constructible supports.
- The series runs to GF IX on 15 July 1986.
- Reused typescript leaves in 156-8 and 156-9 are Récoltes et Semailles. That is my identification, from the cited titles "L'Apothéose", "Les joyaux" and "La maffia". The leaves are typed p. 936 (1985) and pp. 951-953 and 1074-1088 (6 and 8 May 1986), the same typescript as in cote 84 (= H01T).
- His own "faux" marks appear on several leaves.

**Basis:** 56 entry-read (the openings of the steps entries; the dates and titles of the title-sheet entries).

**Checks:** none.

**What part 2 should take from here:** the mathematics of 156-7 to 156-9 is still read only at stage A, with these notes as the guide. In particular:
- the magasins and ateliers;
- the lieux axioms;
- the third Analysis Situs.
'''
