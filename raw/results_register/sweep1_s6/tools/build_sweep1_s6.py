"""Sweep 1, scope s6: placements, merges, flag verdicts and check counts for the S6 rows of REGISTER.tsv.

Written by Claude Opus 5.5 at effort max (sweep 1, scope s6), 18 Nov 2026. Read-only on the register, the returns and
the S6 check ledger; writes only into results_register/sweep1_s6/. Run: python -I -B tools/build_sweep1_s6.py
"""
import csv, os, re, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import load, CP35
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORT = CP35.replace('S6_06_BLIND_results.csv', 'S6_06_BLIND_report.md')
rows, cp, flags, edges, led = load()
R = {r['tag']: r for r in rows}
# the four rows cp35 adds after the register's cp33 table
for rid in ['P3K.113', 'P3K.114', 'P3K.115', 'P3K.116']:
    c = cp[rid]
    R['S6_06_BLIND:' + rid] = {'tag': 'S6_06_BLIND:' + rid, 'run': 'S6_06_BLIND', 'id': rid, 'status': c['status'],
                               'statement': c['statement'], 'where_proved': c['where_proved'], 'depends_on': c['depends_on'],
                               'notes': 'cp35 only (not in the register, which holds cp33)', 'cp35_only': True}

# ---------------------------------------------------------------- 1. the outline
CH = {
 'S0.1': 'The construction of [AC26] and the conventions',
 'S0.2': 'The dictionary with [E26]: line-bundle quotient, mu, lambda0',
 'S0.3': 'The literature on these structures: DGKX, Viaclovsky, Yang (audits and comparisons)',
 'S1.1': 'Canonical bundle, anticanonical ring and the intrinsic fibration',
 'S1.2': 'Hodge numbers and the direct images',
 'S1.3': 'Frolicher, Bott-Chern, Aeppli; special Hermitian metrics',
 'S1.4': 'Tangent cohomology, Kodaira-Spencer, the Kuranishi space; stability of the fibration',
 'S1.5': 'Twisted tangent cohomology H^i(T_X (x) M)',
 'S1.6': 'Automorphisms, real structures and real loci',
 'S1.7': 'Special fibres, the cusp fibre W, curves and surfaces in X',
 'S2.1': 'The classification X_c = X_c\' iff c\'-c in 2Z; the punctured w-disc',
 'S2.2': 'All discrete data and the other families (twists, Engel u, X_{3k,4l}, two-parameter, combs)',
 'S2.3': 'Deformation invariance of the multiplicity pair; smooth specializations',
 'S2.4': 'The parameter space in numbers: beta, M, the norm D and its level sets',
 'S2.5': 'The boundary |w| = 216',
 'S2.6': 'The limit w -> 0: Engel\'s Conjecture 8.2 and the absence of a filling',
 'S2.7': 'Periods and the monodromy group; Klingler\'s question; the period derivative',
 'S2.8': 'Arithmetic of the family: torsion locus, CM fibres, heights, transcendence',
 'S3.1': 'The circle quotient, Engel\'s map S^6 -> S^3, and the classes in pi_6',
 'S3.2': 'A CW structure adapted to f',
 'S3.3': 'The local Kummer cover of the cusp',
 'S3.4': 'The monodromy in Theta_7',
 'S4.1': 'Members with pi_1 = Z/|p| and their universal covers',
 'S4.2': 'Other rational elliptic surfaces with MW = Z: the six-manifolds and the sphere families',
 'S4.3': 'The conifold transition to S^3 x S^3',
 'S4.4': 'The fibre-product fourfold and fivefold',
 'S4.5': 'The three-connected complex fourfold fibred in 3-tori',
 'S5.1': 'The conormal step and the fibre groups (CDP20 p. 692, Prop. 7.3, Rem. 7.2, 7.4)',
 'S5.2': 'Singular fibre supports: normalization, conductor, excluded germs',
 'S5.3': 'Counterexamples that do not use S^6',
 'S5.4': 'Euler numbers of fibres; the sign theorem c_3 in {0,2}',
 'S5.5': 'The general fibre of the algebraic reduction',
 'S5.6': 'The tangent index and the corrected Theorem 2.2',
 'S5.7': 'The monodromy gap: CDP Lemma 4.2 and its corrections',
 'S5.8': 'Trivial monodromy',
 'S5.9': 'Algebraic dimension of complex structures on S^6; CDP98 Lemma 1.5, Prop. 1.1',
 'S5.10': 'Unrestricted torus degenerations: the fibres that occur',
 'SZ.1': 'The sectorial count of geodesic arcs (side lane, no map to X)',
 'SZ.2': 'The lattice J between Leech lattices (side lane, no map to X)',
 'Q.1': 'Pm | prec, p_j = 1 | C_max in polynomial time (not S6)',
}
PART = {'S0': 'S0 Conventions, the construction and the literature', 'S1': 'S1 One member X_c: its complex geometry',
        'S2': 'S2 The family of complex structures on S^6', 'S3': 'S3 Topology: maps, homotopy classes, mapping classes',
        'S4': 'S4 Other manifolds from the construction', 'S5': 'S5 Campana-Demailly-Peternell after S^6',
        'SZ': 'SZ Side lanes of the S6 workbench (no map to X)', 'Q': 'Q Outside the S6 tag space: scheduling (Q03)'}

# rules: (run, id regex, chapter, section); first match wins
RULES = [
 # S6_01_INVARIANTS
 ('S6_01_INVARIANTS', r'A2\.3$', 'S0.2', 'mu is the elliptic logarithm of the Mordell-Weil generator'),
 ('S6_01_INVARIANTS', r'A2\.1$', 'S2.7', 'The period derivative and the Kodaira-Spencer divisor of f'),
 ('S6_01_INVARIANTS', r'A1\.', 'S1.2', 'Direct images of O, Omega^1, Omega^2 (logarithmic frames)'),
 ('S6_01_INVARIANTS', r'A2\.', 'S1.2', 'The decisive scalar mu\'(z_2) and the rank of kappa_1'),
 ('S6_01_INVARIANTS', r'A3\.', 'S1.2', 'The Hodge diamond and its generators'),
 ('S6_01_INVARIANTS', r'A4\.', 'S1.2', 'Torsion of Omega^p_{X/B}; errata to [AC26] Rem. 1.3, 9.21'),
 ('S6_01_INVARIANTS', r'B1\.0$', 'S0.2', 'Marked lattice, theta line bundle and contracting scale'),
 ('S6_01_INVARIANTS', r'B1\.|B2\.1$', 'S1.2', 'The other members: twists and multiplicities (3k,4l)'),
 ('S6_01_INVARIANTS', r'B2\.2$', 'S1.1', 'The anticanonical ring of X_{3k,4l}'),
 ('S6_01_INVARIANTS', r'B3\.', 'S4.1', 'Universal covers: complex invariants'),
 ('S6_01_INVARIANTS', r'C1\.', 'S1.3', 'The Frolicher spectral sequence'),
 ('S6_01_INVARIANTS', r'C2\.', 'S1.3', 'Bott-Chern and Aeppli numbers'),
 ('S6_01_INVARIANTS', r'C3\.[5-7]$', 'S1.3', 'Special Hermitian metrics'),
 ('S6_01_INVARIANTS', r'C3\.', 'S1.3', 'The Bott-Chern algebra, the Picard map and the non-Kahler degrees'),
 ('S6_01_INVARIANTS', r'D[123]\.', 'S1.4', 'h^i(T_X), H^1(T_X) and the Kuranishi germ'),
 ('S6_01_INVARIANTS', r'D4\.', 'S1.5', 'Jump loci and torsion stalks of the twisted tangent sheaves'),
 ('S6_01_INVARIANTS', r'E1\.', 'S1.4', 'Small deformations keep the fibration'),
 ('S6_01_INVARIANTS', r'E2\.', 'S2.2', 'Viaclovsky\'s combs X_m'),
 # S6_02_FAMILY
 ('S6_02_FAMILY', r'A\.1\.1$', 'S1.1', 'omega_X = O(-2S_2), the anticanonical ring, f = |-2K|'),
 ('S6_02_FAMILY', r'A\.1\.2$', 'S2.1', 'Finite base changes and the product covers'),
 ('S6_02_FAMILY', r'A\.4\.1$', 'S2.1', 'Albanese curves and j-functions'),
 ('S6_02_FAMILY', r'A\.4\.2$', 'S1.4', 'The Kodaira-Spencer class of d/dc'),
 ('S6_02_FAMILY', r'A\.4\.3$', 'S0.3', 'Viaclovsky\'s and Yang\'s methods compared'),
 ('S6_02_FAMILY', r'A\.5\.2$', 'S1.4', 'h^i(T_X), H^1(T_X) and the Kuranishi germ'),
 ('S6_02_FAMILY', r'A\.', 'S2.1', 'Necessity (deck lifts), sufficiency (even shifts) and the classification'),
 ('S6_02_FAMILY', r'B\.1\.', 'S0.2', 'Line-bundle quotient, MW = Z[mu], lambda0 = 1'),
 ('S6_02_FAMILY', r'B\.2\.', 'S2.2', 'All (3,4) twist and cusp data; Engel\'s u'),
 ('S6_02_FAMILY', r'B\.3\.', 'S2.2', 'Coprime (3k,4l): the classification'),
 ('S6_02_FAMILY', r'B\.4\.', 'S1.6', 'Aut(X_c) = C*; conjugation and the real members'),
 ('S6_02_FAMILY', r'C\.1\.', 'S2.4', 'beta^part and the special values'),
 ('S6_02_FAMILY', r'C\.2\.', 'S2.4', 'M = -(3/pi) log 6 and the radius 216'),
 ('S6_02_FAMILY', r'C\.3\.', 'S2.5', 'Degeneration at the boundary; the natural boundary'),
 ('S6_02_FAMILY', r'C\.4\.', 'S1.7', 'The cusp fibre W_c and its gluing units'),
 ('S6_02_FAMILY', r'D\.1\.', 'S1.7', 'Elliptic quotients, abelian fibres, NS(F_t)'),
 ('S6_02_FAMILY', r'D\.2\.', 'S1.7', 'Curves and surfaces in X'),
 ('S6_02_FAMILY', r'E\.1\.', 'S2.6', 'Engel\'s untwisted family X(u) at u = 0'),
 ('S6_02_FAMILY', r'E\.2\.2$', 'S3.4', 'Sphere monodromy: first descriptions'),
 ('S6_02_FAMILY', r'E\.2\.', 'S2.6', 'The S^6 family at w = 0: partial filling and nonexistence'),
 ('S6_02_FAMILY', r'F\.3\.3$', 'S2.7', 'The period derivative and the Kodaira-Spencer divisor of f'),
 ('S6_02_FAMILY', r'F\.3\.', 'S2.7', 'The period map: injectivity and limits'),
 ('S6_02_FAMILY', r'F\.', 'S2.7', 'The monodromy group Gamma; proper discontinuity on the period domain'),
 # S6_02_PUSH
 ('S6_02_PUSH', r'A\.3\.', 'S2.6', 'Engel\'s Conjecture 8.2: the Euler-number obstruction'),
 ('S6_02_PUSH', r'A\.', 'S2.6', 'Engel\'s untwisted family X(u) at u = 0'),
 ('S6_02_PUSH', r'B\.', 'S2.6', 'The S^6 family at w = 0: partial filling and nonexistence'),
 ('S6_02_PUSH', r'C\.[12]\.', 'S3.4', 'Eells-Kuiper invariant and the untwisted coboundary'),
 ('S6_02_PUSH', r'C\.3\.1[23]$', 'S3.1', 'The Seifert quotient extended over the cusp'),
 ('S6_02_PUSH', r'C\.', 'S3.4', 'The original family: two methods, class 0 (reference fan)'),
 ('S6_02_PUSH', r'D\.4\.', 'S2.4', 'Level sets of D and its critical points'),
 ('S6_02_PUSH', r'D\.', 'S2.5', 'No extension through |w| = 216; Hausdorff and Chabauty limits'),
 ('S6_02_PUSH', r'E\.1\.', 'S2.2', 'Higher twists: the dictionary to Viaclovsky'),
 ('S6_02_PUSH', r'E\.2\.1$', 'S1.4', 'The other members'),
 ('S6_02_PUSH', r'E\.2\.', 'S2.3', 'The multiplicity pair is a deformation invariant'),
 ('S6_02_PUSH', r'E\.3\.', 'S0.3', 'DGKX versions 1 and 2 audited'),
 ('S6_02_PUSH', r'E\.4\.', 'S2.4', 'M = -(3/pi) log 6 and the radius 216'),
 ('S6_02_PUSH', r'E\.5\.', 'S2.2', 'Viaclovsky\'s two-parameter family'),
 # S6_03_CDP
 ('S6_03_CDP', r'A\.[12]\.', 'S5.1', 'The conormal filtration, the section criterion, beyond normal crossings'),
 ('S6_03_CDP', r'A\.3\.', 'S5.1', 'Multiple fibres (CDP20 Rem. 7.2, 7.4)'),
 ('S6_03_CDP', r'A\.4\.', 'S5.1', 'CDP20 Prop. 7.3 and the torsion-free cotangent assertion'),
 ('S6_03_CDP', r'A\.5\.', 'S5.2', 'Normalization, conductor and the persistent obstruction'),
 ('S6_03_CDP', r'B\d', 'S5.3', 'The nodal family and its compact version'),
 ('S6_03_CDP', r'C\.1\.', 'S5.6', 'The tangent index and generic vanishing'),
 ('S6_03_CDP', r'C2[a-d]$', 'S5.4', 'Euler localization, semistable models, normal jets'),
 ('S6_03_CDP', r'C\.2\.NC\.', 'S5.4', 'Normal-crossings fibres'),
 ('S6_03_CDP', r'C\.2\.G\.', 'S5.4', 'The sign theorem'),
 ('S6_03_CDP', r'C\.2\.UN\.', 'S5.10', 'Unrestricted torus degenerations'),
 ('S6_03_CDP', r'C\.2\.', 'S5.4', 'Irreducible and reducible supports: Euler signs'),
 ('S6_03_CDP', r'C\.3\.', 'S5.5', 'General fibres: tori, Hopf, Kodaira, bielliptic, Inoue'),
 ('S6_03_CDP', r'C4[a-g]$', 'S5.6', 'The corrected Theorem 2.2'),
 ('S6_03_CDP', r'C5[a-c]$', 'S5.6', 'Twists and resonance lengths'),
 ('S6_03_CDP', r'D\.1\.14$', 'S2.7', 'The monodromy group Gamma; proper discontinuity on the period domain'),
 ('S6_03_CDP', r'D\.1\.', 'S5.7', 'Coinvariants, the corrected count and the coherent restriction'),
 ('S6_03_CDP', r'D\.2\.', 'S5.8', 'Trivial monodromy: existence and c_3 = 0'),
 ('S6_03_CDP', r'E(4|5|6|7|10)$', 'S1.4', 'Small deformations keep the fibration'),
 ('S6_03_CDP', r'E(8|16|18)$', 'S2.7', 'The period derivative and the Kodaira-Spencer divisor of f'),
 ('S6_03_CDP', r'E9$', 'S1.4', 'h^i(T_X), H^1(T_X) and the Kuranishi germ'),
 ('S6_03_CDP', r'E(11|13|14|15)$', 'S1.4', 'The other members'),
 ('S6_03_CDP', r'E19$', 'S2.2', 'All (3,4) twist and cusp data; Engel\'s u'),
 ('S6_03_CDP', r'E\d', 'S5.9', 'Algebraic dimension; CDP98 Lemma 1.5 and Proposition 1.1'),
 # S6_04_MAPS_MANIFOLDS
 ('S6_04_MAPS_MANIFOLDS', r'A\.[12]\.', 'S3.1', 'The circle quotient, its non-extension, the repaired map'),
 ('S6_04_MAPS_MANIFOLDS', r'A\.3\.', 'S1.6', 'Antiholomorphic involutions and real loci'),
 ('S6_04_MAPS_MANIFOLDS', r'B\.[1-4]\.', 'S3.1', 'Classes in pi_6(S^3), pi_6(S^2), pi_6(S^4)'),
 ('S6_04_MAPS_MANIFOLDS', r'B\.5\.', 'S3.2', 'Cells from the three fillings and the pair of pants'),
 ('S6_04_MAPS_MANIFOLDS', r'B\.6\.', 'S3.4', 'Original and X_{3k,4l} families: the conifold route (reference fan)'),
 ('S6_04_MAPS_MANIFOLDS', r'C\.', 'S3.3', 'The corrected Kummer map and its globalizations'),
 ('S6_04_MAPS_MANIFOLDS', r'D\.1\.', 'S4.1', 'Universal covers: topology and smooth type'),
 ('S6_04_MAPS_MANIFOLDS', r'D\.2\.[1-4]$', 'S4.2', 'The Oguiso-Shioda list: configurations and the bounded slice'),
 ('S6_04_MAPS_MANIFOLDS', r'D\.2\.([5-9]|1[0-2])$', 'S4.2', 'Named families: pi_1 and integral homology'),
 ('S6_04_MAPS_MANIFOLDS', r'D\.2\.', 'S4.2', 'All profiles: integral homology and smooth types'),
 ('S6_04_MAPS_MANIFOLDS', r'D\.3\.', 'S4.3', 'The moving-zero family and its smoothing'),
 ('S6_04_MAPS_MANIFOLDS', r'E\.1\.', 'S4.4', 'The fourfold Z: model and homology'),
 ('S6_04_MAPS_MANIFOLDS', r'E\.2\.1$', 'S4.4', 'The fourfold Z: complex invariants'),
 ('S6_04_MAPS_MANIFOLDS', r'E\.', 'S4.4', 'Fibre products in general; the shifted fivefold'),
 ('S6_04_MAPS_MANIFOLDS', r'F\.1\.', 'S4.5', 'Euler number and characteristic-number congruences'),
 ('S6_04_MAPS_MANIFOLDS', r'F\.2\.', 'S4.5', 'Classification of the monodromy tuples'),
 ('S6_04_MAPS_MANIFOLDS', r'F\.3\.', 'S4.5', 'Periods and the holomorphic filling'),
 ('S6_04_MAPS_MANIFOLDS', r'F\.4\.', 'S4.5', 'Diffeomorphism type'),
 # S6_05_ARITHMETIC
 ('S6_05_ARITHMETIC', r'A\.', 'SZ.1', None),
 ('S6_05_ARITHMETIC', r'B\.', 'SZ.2', None),
 ('S6_05_ARITHMETIC', r'C\.2\.1$', 'S2.1', 'Albanese curves and j-functions'),
 ('S6_05_ARITHMETIC', r'C\.2\.2$', 'S1.6', 'Antiholomorphic involutions and real loci'),
 ('S6_05_ARITHMETIC', r'C\.[138]\.', 'S2.4', 'The norm D: Green function, local expansions, bounds'),
 ('S6_05_ARITHMETIC', r'C\.[45]\.', 'S2.8', 'The torsion locus of P; CM fibres'),
 ('S6_05_ARITHMETIC', r'C\.6\.', 'S2.8', 'Heights, ranks and BSD at the CM fibres'),
 ('S6_05_ARITHMETIC', r'C\.7\.', 'S2.8', 'Transcendence of the norm'),
 # S6_06_BLIND
 ('S6_06_BLIND', r'P1B\.|P1\.[1-3]$', 'S4.5', 'The monodromy tuple (blind)'),
 ('S6_06_BLIND', r'P1\.(4|5|7|8|15|16|18)$', 'S4.5', 'Periods and the rank-three subbundle (blind)'),
 ('S6_06_BLIND', r'P1\.(9|11)$', 'S4.5', 'The Kuhn cusp (blind)'),
 ('S6_06_BLIND', r'P1\.(10|12|13|19)$', 'S4.5', 'Topology of M (blind)'),
 ('S6_06_BLIND', r'P1\.(6|14)$', 'S4.5', 'Diffeomorphism type (blind)'),
 ('S6_06_BLIND', r'P1', 'S4.5', 'Complex invariants and the family in c (blind)'),
 ('S6_06_BLIND', r'P2\.1[01]$', 'S2.6', 'Engel\'s untwisted family X(u) at u = 0'),
 ('S6_06_BLIND', r'P2\.', 'S2.6', 'The S^6 family at w = 0: partial filling and nonexistence'),
 ('S6_06_BLIND', r'P3F\.(1|18|19|20|26|29|33|34)$', 'S4.2', 'Sphere families from other sources (blind run)'),
 ('S6_06_BLIND', r'P3R\.', 'S3.4', 'The Eells-Kuiper formula and the sixfold residues'),
 ('S6_06_BLIND', r'P3', 'S3.4', 'Blind run: reference fan, physical line, every fan'),
 ('S6_06_BLIND', r'P4\.[1-5]$', 'S5.8', 'The explicit identity-monodromy threefold (blind)'),
 ('S6_06_BLIND', r'P4\.14$', 'S5.1', 'CDP20 Prop. 7.3 and the torsion-free cotangent assertion'),
 ('S6_06_BLIND', r'P4\.1[6-9]$', 'S5.2', 'Excluded germs in torus degenerations'),
 ('S6_06_BLIND', r'P4', 'S5.4', 'The sign theorem in the irreducible and normal-crossings scope (blind)'),
 ('S6_06_BLIND', r'P5\.[1-4]$', 'S1.4', 'h^i(T_X), H^1(T_X) and the Kuranishi germ'),
 ('S6_06_BLIND', r'P5\.5$', 'S1.6', 'Aut(X_c) = C*; conjugation and the real members'),
 ('S6_06_BLIND', r'P5\.6$', 'S2.1', 'Necessity (deck lifts), sufficiency (even shifts) and the classification'),
 ('S6_06_BLIND', r'P5\.7$', 'S0.3', 'DGKX versions 1 and 2 audited'),
 ('Q03_DEPOSIT', r'.', 'Q.1', None),
]
SZ_SEC = {('S6_05_ARITHMETIC', 'A.1'): 'Bijection to (s,t,z), exact counts', ('S6_05_ARITHMETIC', 'A.2'): 'The lattice Gamma and its orbifold',
          ('S6_05_ARITHMETIC', 'A.3'): 'Unrestricted count', ('S6_05_ARITHMETIC', 'A.4'): 'Arc-restricted count: exponents',
          ('S6_05_ARITHMETIC', 'A.5'): 'Square-root question: mean square, Omega results'}
# placements I changed by reading (how = read), with the reason
READ_OVERRIDE = {
 'S6_01_INVARIANTS:A2.3': 'read: the identification of mu (the period section is +/-P*) is part of the [AC26]-[E26] dictionary; same as S6_02_FAMILY B.1.3',
 'S6_01_INVARIANTS:A2.1': 'read: the determinant identity is the period derivative of f; same object as S6_02_FAMILY F.3.3 and S6_03 E8',
 'S6_01_INVARIANTS:B1.0': 'read: dictionary data, used by every later chapter',
 'S6_02_FAMILY:A.4.3': 'read: a comparison with the literature, not a result about X',
 'S6_02_FAMILY:E.2.2': 'read: a mapping-class statement; belongs with the Theta_7 chapter',
 'S6_03_CDP:D.1.14': 'read: the monodromy group of the construction itself; same as S6_02_FAMILY F.1.1',
 'S6_03_CDP:E19': 'read: topology of the twist data of X, not CDP',
 'S6_03_CDP:E9': 'read: tangent cohomology of X; same as S6_01 D1.3',
 'S6_02_PUSH:C.3.12': 'read: about Engel Remark 8.3 (the Seifert map), not the Theta_7 class',
 'S6_02_PUSH:C.3.13': 'read: about Engel Remark 8.3 (the Seifert map), not the Theta_7 class',
 'S6_02_PUSH:E.2.1': 'read: tangent cohomology of the coprime members',
 'S6_05_ARITHMETIC:C.2.2': 'read: real structures of X_c',
 'S6_06_BLIND:P5.6': 'read: the classification theorem (blind)',
 'S6_06_BLIND:P5.7': 'read: comparison with DGKX',
 'S6_06_BLIND:P4.14': 'read: about CDP20 Prop. 7.3',
}
for t in ['S6_03_CDP:E4', 'S6_03_CDP:E5', 'S6_03_CDP:E6', 'S6_03_CDP:E7', 'S6_03_CDP:E10']:
    READ_OVERRIDE[t] = 'read: stability of the torus fibration under deformation; belongs with S1.4 (same theme as S6_01 E1.1)'
for t in ['S6_03_CDP:E8', 'S6_03_CDP:E16', 'S6_03_CDP:E18', 'S6_02_FAMILY:F.3.3']:
    READ_OVERRIDE[t] = 'read: Kodaira-Spencer rank divisor of the period family of f'
for t in ['S6_03_CDP:E11', 'S6_03_CDP:E13', 'S6_03_CDP:E14', 'S6_03_CDP:E15']:
    READ_OVERRIDE[t] = 'read: tangent cohomology and Kuranishi space of other torus-fibred structures on S^6'
for i in ['1', '18', '19', '20', '26', '29', '33', '34']:
    READ_OVERRIDE['S6_06_BLIND:P3F.' + i] = 'read: topology of sphere families from other sources (input to Part 3)'
for i in ['16', '17', '18', '19']:
    READ_OVERRIDE['S6_06_BLIND:P4.' + i] = 'read: excluded singular germs'
for t in ['S6_05_ARITHMETIC:C.2.1']:
    READ_OVERRIDE[t] = 'read: Albanese invariants of the family'

def place(r):
    for run, rx, ch, sec in RULES:
        if r['run'] == run and re.match(rx, r['id']):
            if sec is None:
                if run == 'Q03_DEPOSIT':
                    m = re.match(r'(\d+)\.', r['id']); sec = f"Section {m.group(1)} of the post" if m else 'Main theorem and sources'
                else:
                    sec = SZ_SEC.get((run, r['id'][:3]), 'Construction, J, overlattices, stabilizers' if r['id'].startswith('B') else 'Count')
            return ch, sec
    return None, None

# ---------------------------------------------------------------- 2. merges
SHORT = {'S6_01': 'S6_01_INVARIANTS', 'S6_02': 'S6_02_FAMILY', 'S6_02_PUSH': 'S6_02_PUSH', 'S6_03': 'S6_03_CDP',
         'S6_04': 'S6_04_MAPS_MANIFOLDS', 'S6_05': 'S6_05_ARITHMETIC'}
blind = []  # (earlier tag, verdict, blind rows)
for l in open(REPORT, encoding='utf-8').read().splitlines():
    m = re.match(r'\|\s*(S6_0\d(?:_PUSH)?)\s+([A-Za-z0-9.]+)\s*\|(.*)\|(.*)\|\s*([^|]*)\|\s*$', l)
    if not m: continue
    tag = SHORT[m.group(1)] + ':' + m.group(2)
    brows = re.findall(r'\b(P\d[A-Z]?\.\d+)\b', m.group(4))
    blind.append((tag, m.group(5).strip(), brows))
merges = []
def M(canon, member, rel, why):
    merges.append((canon, member, rel, why))
for tag, verdict, brows in blind:
    for b in brows:
        bt = 'S6_06_BLIND:' + b
        if verdict.startswith('agrees in') or verdict.startswith('agrees on') or verdict.startswith('agrees for'):
            M(tag, bt, 'weaker', f'blind independent re-derivation of the earlier row in a restricted scope (report: "{verdict[:70]}")')
        elif verdict.startswith('agrees'):
            if R.get(bt, {}).get('status') == 'Refuted':
                M(tag, bt, 'same', 'blind re-derivation; the S6_06 row is a corrected historical row (17 Nov physical-line correction) whose retained part (the zero reference-fan conclusion) agrees')
            else:
                M(tag, bt, 'same', 'blind independent re-derivation (S6_06_BLIND report, stated-value table: agrees)')
        elif verdict.startswith('disagrees') and tag == 'S6_04_MAPS_MANIFOLDS:D.2.11':
            M(bt, tag, 'weaker', 'the blind "disagrees" is against the one-line summary, which drops the hypothesis gcd(n,3k) = 1; as printed (S6_04 sections/manifolds.tex l. 2156-2185) D.2.11 is the case g = gcd(3k,n,3d) = 1 of the blind formula H_2 = H_3 = Z/|n| + Z/g, so the two agree on its scope (CORRECTIONS.md, item 1)')
        elif verdict.startswith('disagrees'):
            M(bt, tag, 'refuted by', 'blind run disagrees: explicit counterexample in the S6_06 row (see CORRECTIONS.md)')
# the manual lineage (read): canonical, member, relation (member relative to canonical), reason
MANUAL = [
 ('S6_01_INVARIANTS:D1.3', 'S6_02_FAMILY:A.5.2', 'same', 'h^i(T_X) = (1,1,1,0) and the smooth Kuranishi disc, derived independently in the two runs of 12 Nov'),
 ('S6_01_INVARIANTS:D1.3', 'S6_03_CDP:E9', 'same', 'the CDP run quotes the original-family tangent cohomology (status Known, from R2/R3)'),
 ('S6_01_INVARIANTS:D1.3', 'S6_06_BLIND:P5.3', 'same', 'blind control: (1,1,1,0) from the construction alone'),
 ('S6_01_INVARIANTS:D1.3', 'S6_02_PUSH:E.2.1', 'stronger', 'the same tangent cohomology for every coprime (3k,4l)'),
 ('S6_01_INVARIANTS:D1.3', 'S6_03_CDP:E11', 'stronger', 'coprime multiplicities and nonzero affine twists'),
 ('S6_01_INVARIANTS:D3.1', 'S6_06_BLIND:P5.4', 'same', 'blind control: smooth one-dimensional Kuranishi germ, c-family miniversal'),
 ('S6_01_INVARIANTS:D3.1', 'S6_02_FAMILY:A.5.2', 'same', 'smooth reduced Kuranishi disc, miniversality'),
 ('S6_01_INVARIANTS:D2.1', 'S6_02_FAMILY:A.4.2', 'weaker', 'A.4.2 gives KS(d/dc) != 0; D2.1 gives that it generates H^1(T_X)'),
 ('S6_02_FAMILY:B.4.1', 'S6_06_BLIND:P5.5', 'same', 'blind control: Aut(X_c) = C/Z = C* for every admissible twist'),
 ('S6_02_FAMILY:A.5.1', 'S6_06_BLIND:P5.6', 'same', 'blind: X_c = X_c\' iff c - c\' in 2Z'),
 ('S6_02_FAMILY:B.3.1', 'S6_02_PUSH:E.1.2', 'refines', 'the same 2klZ period, with the full higher-twist criterion in Viaclovsky coordinates'),
 ('S6_02_FAMILY:B.3.1', 'S6_06_BLIND:P3K.11', 'same', 'closed higher parameter w_h = exp(-pi i c/(KL)) is the 2KL period restated'),
 ('S6_02_FAMILY:C.2.3', 'S6_02_PUSH:E.4.3', 'same', 'M = -(3/pi) log 6 attained only at t = 1, recertified (19701 Arb boxes, E.4.1-E.4.2)'),
 ('S6_02_FAMILY:C.2.3', 'S6_02_FAMILY:C.2.1', 'weaker', 'two-sided bounds superseded by the exact value'),
 ('S6_02_FAMILY:C.2.3', 'S6_02_FAMILY:C.2.2', 'weaker', 'local maximum at t = 1 superseded by the global statement'),
 ('S6_02_FAMILY:C.2.3', 'S6_05_ARITHMETIC:C.8.15', 'refines', 'no other coarse critical point; L decreases strictly on every ray from t = 1'),
 ('S6_02_FAMILY:C.2.3', 'S6_02_PUSH:D.4.7', 'refines', 'no additional critical points near i, rho or the cusp (Arb certificates)'),
 ('S6_02_FAMILY:B.1.3', 'S6_01_INVARIANTS:A2.3', 'same', 'the period section is +/- P*, hence wp_tau(mu) = 0'),
 ('S6_02_FAMILY:F.1.1', 'S6_03_CDP:D.1.14', 'same', 'the monodromy group is the index-twelve kernel in the delta-vector stabilizer'),
 ('S6_02_FAMILY:F.3.3', 'S6_01_INVARIANTS:A2.1', 'same', 'the period derivative determinant vanishes (order 2) at z_1 and nowhere else'),
 ('S6_02_FAMILY:F.3.3', 'S6_03_CDP:E8', 'same', 'theta determinant with the wp correction: the same rank divisor'),
 ('S6_02_FAMILY:A.3.1', 'S6_02_PUSH:C.3.5', 'same', 'the even-shift maps: the same result is in DGKX v1 (Known there)'),
 ('S6_02_FAMILY:C.3.4', 'S6_02_PUSH:D.1.1', 'stronger', 'j(Alb S_2(w)) = J(iw/216), no meromorphic continuation through any point of |w| = 216'),
 ('S6_02_FAMILY:C.3.4', 'S6_05_ARITHMETIC:C.2.1', 'same', 'Albanese nomes and continuation radius'),
 ('S6_02_PUSH:D.1.3', 'S6_02_FAMILY:C.3.3', 'settled by', 'C.3.3 left the compact boundary filling open; D.1.3 proves that none exists through any boundary point'),
 ('S6_02_PUSH:A.3.2', 'S6_06_BLIND:P2.11', 'same', 'blind: the central space of Conjecture 8.2 has virtual Euler number 0 (agrees)'),
 ('S6_02_PUSH:A.3.2', 'S6_02_FAMILY:E.1.5', 'settled by', 'E.1.5 left a filling with central fibre Q open; A.3.2 shows Q cannot be a central fibre of X(u)'),
 ('S6_02_PUSH:A.2.2', 'S6_06_BLIND:P2.10', 'same', 'proper flat filling of the untwisted family at u = 0 (two P^1-bundles plumbed)'),
 ('S6_02_PUSH:B.4.33', 'S6_06_BLIND:P2.7', 'stronger', 'blind: no filling for every admissible (3,4) twist, not only the sphere members'),
 ('S6_02_PUSH:B.4.33', 'S6_06_BLIND:P2.9', 'stronger', 'blind: also every coprime (3k,4l) family'),
 ('S6_02_PUSH:B.4.33', 'S6_02_FAMILY:E.2.3', 'settled by', 'E.2.3 left the sphere central fibre unconstructed; B.4.33 proves no filling exists'),
 ('S6_02_PUSH:B.4.33', 'S6_02_PUSH:B.4.1', 'same', 'the refuted row restates the nonexistence as the refutation of the requested filling'),
 ('S6_02_PUSH:B.4.33', 'S6_02_PUSH:B.5.1', 'same', 'idem, for the requested central fibre'),
 ('S6_02_PUSH:C.3.24', 'S6_02_PUSH:C.3.27', 'same', 'second method (direct characteristic index): one-loop class 0'),
 ('S6_02_PUSH:C.3.24', 'S6_04_MAPS_MANIFOLDS:B.6.21', 'same', 'third route (fixed-circle conifold replacement): class 0'),
 ('S6_02_PUSH:C.3.24', 'S6_02_FAMILY:E.2.2', 'weaker', 'E.2.2 describes the mapping class; the residue was not evaluated there'),
 ('S6_06_BLIND:P3K.73', 'S6_02_PUSH:C.3.24', 'refines', 'C.3.24 holds for the reference fan of [AC26]; K73/K74 compute every periodic fan of the original loop, and other fans give nonzero classes (e.g. 26 on T_2): the hypothesis "reference fan" must be stated'),
 ('S6_06_BLIND:P3K.73', 'S6_04_MAPS_MANIFOLDS:B.6.24', 'refines', 'idem for the coprime (3k,4l) families: zero for the reference fan only'),
 ('S6_04_MAPS_MANIFOLDS:B.6.24', 'S6_04_MAPS_MANIFOLDS:B.6.2', 'same', 'B.6.2 is the summary row of B.6.16-B.6.25'),
 ('S6_02_PUSH:C.3.22', 'S6_06_BLIND:P3F.10', 'same', 's_delta = -2, p_rel = -24 on the page, J = 0 (squares unaffected by the physical-line correction)'),
 ('S6_04_MAPS_MANIFOLDS:B.6.10', 'S6_06_BLIND:P3F.6', 'weaker', 'blind agrees on genus 3, twelve I_1, signature -8, height 2; the deck/Hodge character list was not compared'),
 ('S6_06_BLIND:P3K.68', 'S6_04_MAPS_MANIFOLDS:B.6.17', 'corrects', 'B.6.17 displays the meridian-one (U) values p_1 = -4y; in the physical line M the pair is (k,l) = (1,4); the index and the class 0 are unaffected'),
 ('S6_06_BLIND:P3K.68', 'S6_04_MAPS_MANIFOLDS:B.6.20', 'corrects', 'idem: l = -4, k = -1 are the U values; physical (1,4)'),
 ('S6_06_BLIND:P3K.68', 'S6_06_BLIND:P3K.9', 'corrects', 'P3K.9 displays (k,l) = (-6,-24) and (-1,-4): meridian-one convention (report, item 3.3); physical pair (1,4)'),
 ('S6_06_BLIND:P3K.68', 'S6_06_BLIND:P3K.6', 'refuted by', 'the run\'s own correction of 17 Nov: the meridian-one Thom line is the dual of the physical line'),
 ('S6_06_BLIND:P3K.74', 'S6_06_BLIND:P3K.33', 'refuted by', 'original K=L=1 shorter loop on T_2: class 26, not 0'),
 ('S6_06_BLIND:P3K.74', 'S6_06_BLIND:P3F.53', 'refuted by', 'primitive OS45: class 3, not 25'),
 ('S6_06_BLIND:P3K.74', 'S6_06_BLIND:P3K.36', 'refuted by', 'corrected Liu-Rollenske u = w^2 on T_2: class 26'),
 ('S6_06_BLIND:P3K.74', 'S6_06_BLIND:P3K.37', 'refuted by', 'OS49 k = 1 shorter loop on T_-: class 27'),
 ('S6_06_BLIND:P3F.33', 'S6_04_MAPS_MANIFOLDS:D.2.11', 'weaker', 'P3F.33: the OS49 cap is free exactly when gcd(k,n,d) = 1 and (3 does not divide n or 3 | k); D.2.11 assumes gcd(n,3k) = 1, a special case; outside it (e.g. (m,n,d) = (9,3,1)) the blind run finds the extra Z/3'),
 ('S6_06_BLIND:P3F.36', 'S6_04_MAPS_MANIFOLDS:D.2.27', 'refines', 'D.2.27 (no sphere from I_1^* profiles) holds only in its "natural filling sector"; the corrected-line weighted I_1^* constructions give spheres'),
 ('S6_06_BLIND:P3F.36', 'S6_04_MAPS_MANIFOLDS:D.2.28', 'refines', 'the count "5 profiles admit none" is sector-dependent'),
 ('S6_04_MAPS_MANIFOLDS:D.2.1', 'S6_06_BLIND:P3F.1', 'same', 'eight MW = Z rows, 21 configurations (blind agrees)'),
 ('S6_04_MAPS_MANIFOLDS:F.4.1', 'S6_06_BLIND:P1.14', 'same', 'blind: oriented diffeomorphic to 3HP^2 # (-HP^2)'),
 ('S6_04_MAPS_MANIFOLDS:F.4.1', 'S6_06_BLIND:P1.6', 'stronger', 'P1.6 settles the homotopy-sphere ambiguity: (3HP^2#-HP^2)#Sigma^8 = 3HP^2#-HP^2'),
 ('S6_04_MAPS_MANIFOLDS:F.2.6', 'S6_06_BLIND:P1.12', 'same', 'torsion-free homology, H_4 = Z^4, three-connected'),
 ('S6_04_MAPS_MANIFOLDS:F.1.1', 'S6_06_BLIND:P1.9', 'same', 'Kuhn cusp filling, Euler number 6d'),
 ('S6_04_MAPS_MANIFOLDS:E.1.3', 'S6_06_BLIND:P1.11', 'same', 'index-one Kuhn cusp: homology ranks (1,3,9,9,10,3,1)'),
 ('S6_04_MAPS_MANIFOLDS:F.3.5', 'S6_06_BLIND:P1.7', 'same', 'exterior-square quotient of the genus-two pencil'),
 ('S6_04_MAPS_MANIFOLDS:F.3.6', 'S6_06_BLIND:P1.8', 'same', 'global holomorphic periods with transversality; the blind run first corrects the rank of P (P1.5)'),
 ('S6_06_BLIND:P1.5', 'S6_04_MAPS_MANIFOLDS:F.3.6', 'corrects', 'the construction formula as handed on (P = image of l_0 ^ H with H of rank two) gives rank two, not three; F.3.6\'s conclusion stands through P1.8'),
 ('S6_04_MAPS_MANIFOLDS:F.2.1', 'S6_06_BLIND:P1B.1', 'same', 'unimodular normal form of the square-zero rank-three cusp'),
 ('S6_04_MAPS_MANIFOLDS:F.2.2', 'S6_06_BLIND:P1B.2', 'same', 'thirty-eight cyclotomic characteristic polynomials'),
 ('S6_03_CDP:C.2.G.1', 'S6_06_BLIND:P4.58', 'weaker', 'blind: the sign theorem when every reduced fibre support is irreducible or normal crossings'),
 ('S6_03_CDP:D.2.7', 'S6_06_BLIND:P4.5', 'same', 'blind: the explicit identity-monodromy threefold has a = 1, c_3 = 0, b_3 = 2'),
 ('S6_03_CDP:D.2.2', 'S6_03_CDP:D.2.4', 'weaker', 'normal-crossings case of the trivial-monodromy statement'),
 ('S6_01_INVARIANTS:E2.2', 'S6_03_CDP:E15', 'stronger', 'combs: the same h(T) = (2m+1, 8m+1, 6m+1, 0) and a smooth miniversal germ of dimension 8m+1'),
 ('S6_03_CDP:E15', 'S6_01_INVARIANTS:E2.3', 'settled by', 'E2.3 left the comb Kuranishi space open (88 <= dim Def <= 97 at m = 12); E15 proves it smooth of dimension 97 = 8m+1 (scope: E2.1 needs m >= 12, E15 says "positive combs")'),
 ('S6_04_MAPS_MANIFOLDS:D.1.3', 'S6_01_INVARIANTS:B3.3', 'same', 'universal cover: Betti numbers (1,0,n-1,0,n-1,0,1)'),
 ('S6_04_MAPS_MANIFOLDS:A.1.2', 'S6_02_PUSH:C.3.12', 'same', 'the literal Seifert quotient of [E26] Rem. 8.3 does not extend continuously over W'),
 ('S6_04_MAPS_MANIFOLDS:A.2.1', 'S6_02_PUSH:C.3.13', 'same', 'a smooth repaired delta-invariant map X_c -> S^3 extending the quotient'),
 ('S6_04_MAPS_MANIFOLDS:B.6.1', 'S6_02_PUSH:C.3.4', 'same', 'sixfold base change leaves two residues differing by 14'),
 ('S6_02_FAMILY:D.1.2', 'S6_05_ARITHMETIC:C.4.3', 'refines', 'the torsion locus is algebraic, with explicit radical field and relation'),
 ('S6_02_FAMILY:D.1.1', 'S6_05_ARITHMETIC:C.4.4', 'refines', 'exact values and division loci through order 8 (the two 6P = O values among them)'),
 ('S6_02_FAMILY:B.4.2', 'S6_04_MAPS_MANIFOLDS:A.3.1', 'refines', 'two conjugacy classes of antiholomorphic involutions; fixed loci are mod-2 homology spheres'),
 ('S6_02_FAMILY:B.4.2', 'S6_05_ARITHMETIC:C.2.2', 'same', 'real locus and antiholomorphic involutions (cites S6_02 B.4.2)'),
 ('S6_02_PUSH:B.4.19', 'S6_06_BLIND:P2.3', 'same', 'proper smooth partial filling over (P^1 x Delta_r) minus (infinity,0)'),
 ('S6_02_PUSH:B.4.18', 'S6_06_BLIND:P2.1', 'same', 'the corner family over the (q,r) bidisc, with the collar term'),
 ('S6_02_PUSH:B.4.18', 'S6_06_BLIND:P2.2', 'refines', 'explicit origins; radial class -pn gamma (the readers\' lead had +pn); the sign does not affect B.4.33'),
]
for m in MANUAL: M(*m)
seen = set(); MERGES = []
for m in merges:
    k = (m[0], m[1])
    if k in seen: continue
    seen.add(k); MERGES.append(m)

# ---------------------------------------------------------------- 3. flag verdicts
def statement(t): return re.sub(r'\s+', ' ', R[t]['statement']) if t in R else ''
PURE_REFUTATION = {  # refuted rows whose statement is itself the refutation (a true negative result), read
 'S6_02_FAMILY:F.2.1', 'S6_02_PUSH:B.1.1', 'S6_02_PUSH:B.3.1', 'S6_02_PUSH:E.5.1', 'S6_03_CDP:C2b', 'S6_03_CDP:E12',
 'S6_04_MAPS_MANIFOLDS:B.6.7', 'S6_04_MAPS_MANIFOLDS:F.2.3', 'S6_05_ARITHMETIC:C.8.9', 'S6_06_BLIND:P1.5'}
HIST_PREFIX = re.compile(r'(Physical-line correction|Audit correction|Proved counterexample)')
SIGNED = re.compile(r'(class\s*\\?\(?-?\d|physical (integer|class)|\(k,\s*\\?ell\)\s*=|\(k,\\ell\)=|A\^\{?\\rm phys|A\^\{\\rm phys\}|=\s*-?\d+\s*\\pmod\{?28|\[\\Phi\]\s*=)')
FLAG_NOTE = {
 'S6_02_FAMILY:F.2.2': 'uses the infinite stabilizer of F.2.1 to cut the largest proper open set',
 'S6_02_PUSH:B.1.2': 'uses the twelve-cycle filling that B.1.1 proves in place of the refuted product assertion',
 'S6_02_PUSH:B.3.2': 'the corrected assembly is built because the plain cusp model cannot glue (B.3.1)',
 'S6_02_PUSH:B.3.3': 'uses the gluing obstruction of B.3.1',
 'S6_02_PUSH:B.4.9': 'uses the peripheral obstruction of B.3.1 as a constraint on logarithmic homomorphisms',
 'S6_02_PUSH:B.4.19': 'uses the twelve-cycle filling of B.1.1',
 'S6_02_PUSH:E.5.3': 'uses the corrected source surface (III* and the rank data) of E.5.1',
 'S6_03_CDP:C.2.UN.2': 'uses the negative-Euler counterexamples of C2b',
 'S6_03_CDP:E2': 'uses the torsion-sensitive base-change formula that replaces CDP98 Lemma 1.5 (E12)',
 'S6_04_MAPS_MANIFOLDS:B.6.8': 'generalizes the order-6 affine defect of B.6.7 to all X_{3k,4l}',
 'S6_04_MAPS_MANIFOLDS:F.2.39': 'includes the cusp-filling data that F.2.3 shows to be necessary',
 'S6_05_ARITHMETIC:C.8.10': 'uses the corrected identity proved in C.8.9',
 'S6_06_BLIND:P1.8': 'uses the corrected rank-three bundle P of P1.5',
 'S6_06_BLIND:P3K.9': 'displays (k,l) = (-6,-24) and (-1,-4), which the report (item 3.3) identifies as the meridian-one U values; the physical pair is (1,4). The index (4k-l)/24 = 0 and the class 0 are convention-free. Restate the pair with its convention.',
 'S6_06_BLIND:P3K.28': 'a signed formula labelled A^phys that cites P3K.6 but not K68/K69; it is used by K73 after the correction, so it is probably restated, but the row should cite K68',
 'S6_06_BLIND:P3F.21': 'states page squares (s_delta = -14, p_rel = -72) and semifreeness only, which the correction retains; the class 4 of this family is in P3F.25 (corrected)',
 'S6_06_BLIND:P3K.47': 'a nonexistence statement about a plumbing product, from the retained pairs of K45/K46; does not use a class value',
 'S6_06_BLIND:P3K.53': 'construction row (source, cap, continuation); does not state a class value from K41',
 'S6_06_BLIND:P3K.38': 'uses the thirty branches (constructions) of P3F.53, which the correction retains; the old values are replaced by K74',
 'S6_06_BLIND:P3F.51': 'coverage statement over sources and constructions, retained by K27/K29/K30',
}
FV = []
for f in flags:
    if f['flag'].startswith('proved; no check'): continue
    t = f['tag']; r = R[t]; dep = re.sub(r'\s+', ' ', r['depends_on'])
    if f['flag'].startswith('proved item cites'):
        cited = [c.strip() for c in f['detail'].split(',')]
        st = statement(t)
        if t in FLAG_NOTE and all(c in PURE_REFUTATION for c in cited):
            v = 'sound: uses the refutation'; note = FLAG_NOTE[t]
        elif all(c in PURE_REFUTATION for c in cited):
            v = 'sound: uses the refutation'; note = 'the cited refuted row states the refutation itself'
        else:
            hist = [c for c in cited if HIST_PREFIX.search(statement(c))]
            cites68 = bool(re.search(r'P3K\.6[89]\b', dep))
            via = [d for d in re.findall(r'P3[FK]\.\d+', dep) if re.search(r'P3K\.6[89]\b', re.sub(r'\s+', ' ', R.get('S6_06_BLIND:' + d, {}).get('depends_on', '')))]
            if t in FLAG_NOTE:
                v = 'needs restatement' if t.endswith('P3K.9') else ('probably sound; add the K68 citation' if t.endswith('P3K.28') else 'sound: uses only parts the correction retains')
                note = FLAG_NOTE[t]
            elif t in ('S6_06_BLIND:P3K.68', 'S6_06_BLIND:P3K.69', 'S6_06_BLIND:P3K.74'):
                v = 'sound: uses the refutation'; note = 'this row is the correction (it proves the cited rows wrong)'
            elif cites68:
                v = 'sound: cites the corrected transfer'; note = 'cites P3K.68/69, which prove the physical-line dictionary; the historical claims are used only through it'
            elif via:
                v = 'sound via a corrected row'; note = 'reaches the physical-line transfer through ' + ', '.join(sorted(set(via))[:4])
            elif SIGNED.search(st):
                v = 'needs a look'; note = 'states a signed class value and cites a historical (pre-correction) row without K68/K69'
            else:
                v = 'sound: uses only parts the correction retains'; note = 'the cited rows retain constructions, topology, page squares, collars and zero classes; this row states none of the corrected signed values'
        FINAL = {  # read after the script's first pass
         'S6_06_BLIND:P3K.28': ('sound: the text invokes K68', 'the statement says "By the actual dual-line and inverse-closing map P3K.68, the physical Hopf-gluing class is A^phys mod 28"; K68 is missing only from depends_on'),
         'S6_06_BLIND:P3K.65': ('sound: convention-free method', 'OS49 classes (-3k, -k on the negative fan T_-, 0 on T_+) are assigned by the relative diffeomorphism and the oriented central generator, not through a chosen line; the w-loop class 27 at k = 1 agrees with K74 in the physical convention'),
         'S6_06_BLIND:P3F.27': ('sound: quotes convention-free values', 'quotes the zero positive-fan index (P3F.31) and the negative-fan class -3 of P3K.65, which is convention-free'),
         'S6_06_BLIND:P3F.31': ('sound: quotes convention-free values', 'index zero (unchanged under M <-> M^-1) and the class -3 of P3K.65'),
         'S6_06_BLIND:P3K.11': ('needs restatement', 'displays (k,l) = (-KL,-4KL) in the rotating framing of P3K.9, i.e. the meridian-one U convention; the physical pair is (KL,4KL). The return index 0 is convention-free'),
        }
        if t in FINAL: v, note = FINAL[t]
        FV.append((t, 'proved item cites a refuted row (' + f['detail'][:160] + ')', v, r['where_proved'][:120], note))
    else:
        d = f['detail']
        DEPV = {
         'S6_02_FAMILY:A.4.1': ('own section', 'C.1 = the run\'s Part C.1 (rows C.1.1, C.1.2): the interval certificate'),
         'S6_02_FAMILY:B.1.4': ('own section', 'C.1 = rows C.1.1, C.1.2 (the cusp branch of the theta formula)'),
         'S6_02_PUSH:B.4.15': ('own section', 'B.1 = rows B.1.1, B.1.2 (the twelve-cycle filling)'),
         'S6_02_PUSH:D.4.1': ('own section', 'E.4 = rows E.4.1-E.4.3 (Arb certificate of the maximum)'),
         'S6_02_PUSH:D.4.8': ('own section', 'E.4 = rows E.4.1-E.4.3'),
         'S6_02_PUSH:E.2.23': ('literature', 'Demailly, Complex analytic and differential geometry, Ch. II, 4.19 and 7.6/7.12'),
         'S6_02_PUSH:E.3.1': ('literature', 'Banica-Stanasila, Algebraic methods in the global theory of complex spaces, III.4.10 and III.4.12'),
         'S6_03_CDP:D.2.5': ('own section', 'C.1 = rows C.1.1-C.1.3 (tangent index)'),
         'S6_04_MAPS_MANIFOLDS:B.4.1': ('own section', 'B.1 = rows B.1.1, B.1.2 (the class 6 nu\')'),
         'S6_04_MAPS_MANIFOLDS:B.6.11': ('another run', 'K13 A2.2 and A4.1 = S6_02_PUSH:A.2.2 (untwisted semistable fillings) and S6_02_PUSH:A.4.1 (their homology)'),
         'S6_04_MAPS_MANIFOLDS:B.6.23': ('own rows, typo', 'B6.22, B6.20 = S6_04 B.6.22, B.6.20 (dot missing)'),
         'S6_04_MAPS_MANIFOLDS:D.2.17': ('own row, typo', 'D2.16 = S6_04 D.2.16'),
         'S6_04_MAPS_MANIFOLDS:D.2.21': ('own row, typo', 'D2.20 = S6_04 D.2.20'),
         'S6_04_MAPS_MANIFOLDS:E.2.6': ('nothing in the register', 'B.5.13 is not a row (Part B.5 has B.5.1, B.5.2 only); an internal label of the return\'s section file'),
         'S6_04_MAPS_MANIFOLDS:E.2.10': ('own section', 'B.5 = rows B.5.1, B.5.2 (cusp and cap van Kampen)'),
         'S6_04_MAPS_MANIFOLDS:E.2.14': ('nothing in the register', 'B.5.16 is not a row; an internal label of the return'),
         'S6_04_MAPS_MANIFOLDS:E.2.16': ('own section', 'B.5 = rows B.5.1, B.5.2'),
         'S6_05_ARITHMETIC:C.2.2': ('another run', 'S6_02 B.4.2 = S6_02_FAMILY:B.4.2 (conjugation and real members)'),
         'S6_05_ARITHMETIC:C.6.R3': ('literature', 'Gross-Zagier, Invent. Math. 84 (1986), Ch. I, (7.3)'),
         'S6_05_ARITHMETIC:C.8.9': ('own section', 'C.3 = rows C.3.1, C.3.2 (local theta expansions)'),
         'S6_05_ARITHMETIC:C.7.5': ('own section', 'C.6 = rows C.6.1-C.6.5, C.6.R*, C.6.T* (numerical height data)'),
         'S6_05_ARITHMETIC:C.7.9': ('own section', 'C.4 = rows C.4.1-C.4.5 (torsion formulas)'),
        }
        v, note = DEPV.get(t, ('unread', ''))
        FV.append((t, 'dependency names no id of the run (' + d + ')', v, r['where_proved'][:120], note))

# ---------------------------------------------------------------- 4. check counts per row
blind_by_tag = collections.defaultdict(list)
for tag, verdict, brows in blind: blind_by_tag[tag].append(verdict)
cmpcol = 'stated_value_compared (run and id)'
for rid, c in cp.items():
    for mm in re.finditer(r'(S6_0\d(?:_PUSH)?)\s+([A-Z][A-Za-z0-9]*(?:\.[A-Za-z0-9]+)+)', c[cmpcol]):
        tag = SHORT[mm.group(1)] + ':' + mm.group(2)
        a = c['agrees_with_stated_value']
        if tag not in blind_by_tag: blind_by_tag[tag].append('row ' + rid + ': ' + a[:40])
MY_CHECKS = collections.Counter()
CE = [  # tag, type, outcome, what was read
 ('S6_06_BLIND:P1.19', 'computation', 'agrees: alternating sum of the chain ranks (4,26,87,162,200,156,79,23,3) is 6 = chi(M_c)', 'register row'),
 ('S6_04_MAPS_MANIFOLDS:B.5.1', 'computation', 'agrees: cell counts (5,20,45,56,42,17,3) give Euler characteristic 2 = chi(S^6)', 'register row'),
 ('S6_06_BLIND:P1.11', 'computation', 'agrees: ranks (1,3,9,9,10,3,1) give 6 = 6d at d = 1 (S6_04 F.1.1); the cusp carries all of chi(M) = 6, as the multiple fibres have chi = 0', 'register rows P1.11, S6_04 E.1.3, F.1.1'),
 ('S6_04_MAPS_MANIFOLDS:E.1.3', 'computation', 'agrees: same ranks, chi = 6, consistent with chi(Z) = 6 in E.1.4 (the small resolution of the fibre product replaces W x I_1, of Euler number 2, by the Kuhn fibre)', 'register rows E.1.1-E.1.4'),
 ('S6_01_INVARIANTS:A3.1', 'computation', 'agrees: sum (-1)^(p+q) h^{p,q} = 2 = chi(S^6); Serre symmetry h^{p,q} = h^{3-p,3-q} holds', 'register row; S6 survey F1'),
 ('S6_01_INVARIANTS:C3.4', 'computation', 'agrees: Delta^k = h_BC^k + h_A^k - 2b_k from the workbench numbers h_BC = (1,0,2,2,2,2,1), h_A = (1,2,2,2,2,0,1) gives (0,2,4,4,4,2,0), the stated formula at h = 1', 'register row; S6 survey F7'),
 ('S6_02_FAMILY:C.2.3', 'computation', 'agrees: e^{-pi M} = 216 and |lambda_0| e^{-2 pi M} = 6^6 = 46656 with lambda_0 = 1 (B.1.4), the two stated radii', 'register rows C.2.3, B.1.4'),
 ('S6_06_BLIND:P3R.2', 'independent re-proof', 'agrees: 6a = b in Z/28 forces b even; for b = 2r, 3a = r mod 14 and 3^{-1} = 5 mod 14, so a in {5r, 5r+14}', 'register rows P3R.2, S6_04 B.6.1, S6_02_PUSH C.3.4'),
 ('S6_04_MAPS_MANIFOLDS:B.6.1', 'independent re-proof', 'agrees (same arithmetic as P3R.2)', 'register row'),
 ('S6_02_PUSH:C.3.22', 'computation', 'agrees: J = (p_rel - 12 s_delta)/24 = (-24+24)/24 = 0 with C.3.18, C.3.21; for (3k,4l) (P3F.17) (-24kl+24kl)/24 = 0; for OS47 (P3F.21) (-72+168)/24 = 4, the class P3F.25 states after the correction', 'register rows C.3.18-C.3.22, P3F.10, P3F.17, P3F.21, P3F.25'),
 ('S6_06_BLIND:P3F.2', 'independent re-proof', 'agrees for the original page: h(mP) = m^2 h(P) = 2 chi + 2 (mP).O with chi = 1, h(P) = 2 gives (mP).O = m^2 - 1, so P.O = 0 and s_delta = (P-O)^2 = -2 - 2P.O = -2', 'prompt of S6_06 Part 3 (readers\' lead); register rows'),
 ('S6_06_BLIND:P2.2', 'targeted proof check', 'agrees: Delta_R F = a n gamma - 6an(n-1) delta with a = -p (P2.1) gives the radial class -pn gamma mod delta; the sign is immaterial to P2.7 and to S6_02_PUSH B.4.33, which need only pn != 0', 'register rows P2.1, P2.2, P2.7'),
 ('S6_04_MAPS_MANIFOLDS:D.1.4', 'computation', 'agrees: Tors H_2 = Tors H_3 = Z/d as Poincare duality and UCT require; Betti (1,0,d-1,0,d-1,0,1) of D.1.3 give chi = 2d, as D.1.1 states', 'register rows D.1.1-D.1.4, S6_01 B3.3'),
 ('S6_06_BLIND:P3F.34', 'computation', 'agrees with duality: H_1 = H_4 = Z/|n| and H_2 = H_3 = Z/|n| + Z/g are compatible with Poincare duality and UCT; at n = +-1, g = 1 and the member is a homotopy sphere. The g-term itself was not recomputed (contradicts S6_04 D.2.11 for g = 3)', 'register rows P3F.33, P3F.34, S6_04 D.2.11'),
 ('S6_06_BLIND:P1.14', 'targeted proof check', 'agrees: 3HP^2 # (-HP^2) has H^4 = Z^4 with form I_{3,1}, signature 2, chi = 6, w_2 = 0, matching P1.12, P1.13', 'register rows P1.12-P1.14'),
 ('S6_02_PUSH:A.4.2', 'computation', 'agrees: Betti (1,1,8,14,8,1,1) give chi(X(u)) = 2', 'register row'),
 ('S6_02_FAMILY:E.1.4', 'computation', 'agrees: (1,1,8,7,10,0,1) give chi(Q) = 12, as stated (Q is singular, so no duality is expected)', 'register row'),
 ('S6_02_PUSH:A.4.8', 'computation', 'agrees: the Betti tuple (1,1,8+k+m,7,9k+t4-2m-1,0,k+m) sums to 11k + t4, the central Euler number of A.4.7', 'register rows A.4.7, A.4.8'),
 ('S6_03_CDP:E15', 'targeted proof check', 'consistent: dim H^1(T) = 8m+1 = 97 at m = 12 is the upper end of S6_01 E2.3\'s bracket 88 <= dim Def <= 97; E15 asserts the germ is smooth (proof not read). Scope differs: S6_01 E2.1 needs m >= 12', 'register rows S6_01 E2.1-E2.4, S6_03 E15'),
 ('S6_03_CDP:E3', 'targeted proof check', 'agrees in its logic: E2 gives c_3 = 0 for a nonholomorphic algebraic reduction with b_2 = 0, while c_3(S^6) = 2; Moishezon needs b_2 > 0; hence a in {0,1} (E2 itself not reread)', 'register rows E2, E3, E12'),
 ('S6_02_FAMILY:F.1.1', 'used and rechecked', 'agrees with S6_03 D.1.14 (same index-twelve kernel), two runs', 'register rows'),
 ('S6_04_MAPS_MANIFOLDS:D.2.11', 'targeted proof check', 'statement as printed assumes gcd(n,3k) = 1; then g = gcd(3k,n,3d) = 1 and the blind formula of P3F.34 gives exactly H_1..H_4 = Z/|n|: no disagreement on its scope. The register one-liner drops the hypothesis', 'S6_04 sections/manifolds.tex l. 2156-2200; S6_06 P3F.29, P3F.33, P3F.34'),
 ('S6_06_BLIND:P3F.33', 'targeted proof check', 'consistent with D.2.11: gcd(n,3k) = 1 implies 3 does not divide n and gcd(k,n) = 1, so the cap is free', 'register rows; S6_04 manifolds.tex l. 2156'),
 ('S6_05_ARITHMETIC:C.5.1', 'targeted proof check', 'the statement is "no t outside {0,1} with E_t CM and P_t torsion" (Bourdon-Clark-Stankewicz 2017, Thm 4.15(a)); consistent with the dense torsion locus of S6_02_FAMILY D.1.2. The register one-liner reads as if torsion alone occurred only at 0, 1', 'S6_05 sections/C_special.tex l. 766-780'),
 ('S6_03_CDP:C.2.INT.3', 'targeted proof check', 'the theorem assumes H^2(Y;Q) = 0 (through C.2.INT.1-2); with that hypothesis it does not conflict with the negative Euler numbers of C2b, C.2.UN.2 and C.2.UN.4 (blow-ups, b_2 > 0). The register one-liner omits the hypothesis', 'S6_03 sections/part_C2_interfaces.tex l. 1-11, 155-162, 379-390'),
 ('S6_02_PUSH:E.5.1', 'targeted proof check', 'consistent with S6_04 D.2.6: the source surface is III* + 3 I_1 (Euler 9+1+1+1 = 12); "ranks one, one, two" are the toric ranks of the three degenerate threefold fibres, as in the prompt\'s "one hexagonal, two rank-one"', 'register rows; S6_1 prompt text'),
 ('S6_04_MAPS_MANIFOLDS:E.1.4', 'computation', 'agrees: the literal fibre product X x_P1 S has Euler number e(W) e(I_1) = 2 x 1 = 2 and is singular (xy = uv along the double curves of W); the small resolution replaces W x I_1 by the Kuhn fibre of Euler number 6 (E.1.3), giving chi(Z) = 6 as stated', 'register rows E.1.1-E.1.4'),
]
for t, *_ in CE: MY_CHECKS[t] += 1
def ledger_counts(run, rid):
    ents = led.get((run, rid), [])
    docs = set(); blind21 = False
    for e in ents:
        for part in e['checks'].split(' || '):
            m = re.match(r'checked in (\S+)', part)
            if m: docs.add(m.group(1))
            if 'blind re-derivation' in part: blind21 = True
    return len(ents) > 0, docs, blind21
CC = []
recheck_already = 0; blind_compared = 0
for t in sorted(R):
    r = R[t]
    if r['run'] == 'S6_06_BLIND' or r['run'] == 'Q03_DEPOSIT':
        continue
    inled, docs, b21 = ledger_counts(r['run'], r['id'])
    bl = blind_by_tag.get(t, [])
    bverdict = bl[0] if bl else ''
    nb = 1 if (bl or b21) else 0
    total = len(docs) + (1 if inled else 0) + nb + MY_CHECKS.get(t, 0)
    if bl or b21:
        blind_compared += 1
        if docs: recheck_already += 1
    CC.append((t, r['status'], len(docs), 1 if inled else 0, bverdict[:60] if bl else ('agrees (cp21)' if b21 else ''), MY_CHECKS.get(t, 0), total, '; '.join(sorted(docs))[:300]))
# S6_06 rows: an agreeing earlier derivation is an independent derivation of the same statement
agree_with = collections.defaultdict(set)
for canon, member, rel, why in MERGES:
    if member.startswith('S6_06_BLIND:') and rel in ('same', 'weaker') and not canon.startswith('S6_06_BLIND:'):
        agree_with[member].add(canon)
for t in sorted(R):
    r = R[t]
    if r['run'] == 'S6_06_BLIND':
        a = sorted(agree_with.get(t, []))
        CC.append((t, r['status'], 0, 0, ('agrees with ' + ', '.join(a))[:60] if a else '', MY_CHECKS.get(t, 0),
                   (1 if a else 0) + MY_CHECKS.get(t, 0), 'its Pro intake (from cp11 on) is running; field expert aa7b8224 (Claude Fable 5.2 at effort max) read up to cp11' if r['id'] < 'P3' else ''))
    elif r['run'] == 'Q03_DEPOSIT':
        CC.append((t, r['status'], 1, 0, '', MY_CHECKS.get(t, 0), 1 + MY_CHECKS.get(t, 0),
                   'reviews/Q03_DEPOSIT_PEER_REVIEW_20261115/PEER_REVIEW_Q03_20261115.md (Claude Fable 5.2 at effort max: targets A, B confirmed; not a line-by-line re-proof of Sections 2-8); earlier: three checks of the 23 Oct return by Claude Opus 5.5 at effort max (Message Batches API)'))

# ---------------------------------------------------------------- write
def w(name, header, data):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t', lineterminator='\n'); wr.writerow(header)
        for d in data: wr.writerow(d)
P = []
for t in sorted(R, key=lambda x: (x.split(':')[0], [int(p) if p.isdigit() else p for p in re.split(r'(\d+)', x.split(':')[1])])):
    r = R[t]; ch, sec = place(r)
    how = 'read' if t in READ_OVERRIDE else 'script'
    note = READ_OVERRIDE.get(t, '').replace('read: ', '')
    if r.get('cp35_only'): note = (note + '; ' if note else '') + 'added in cp35 (12:08 UTC); not in the register (cp33)'
    P.append((t, PART[ch.split('.')[0]], ch + ' ' + CH[ch], sec, how, note))
w('PLACEMENT.tsv', ['tag', 'part', 'chapter', 'section', 'how placed', 'note'], P)
w('MERGES.tsv', ['canonical tag', 'member tag', 'relation (member relative to canonical)', 'reason'], MERGES)
w('FLAG_VERDICTS.tsv', ['tag', 'flag', 'verdict', 'place', 'note'], FV)
w('CHECK_EVENTS.tsv', ['statement tag', 'date', 'who', 'type', 'outcome', 'what was read'],
  [(t, '2026-11-18', 'Claude Opus 5.5 at effort max, sweep 1, scope s6', ty, out, rd) for t, ty, out, rd in CE])
w('CHECK_COUNTS.tsv', ['tag', 'status', 'intake/review documents that checked it (S6 ledger, distinct)', 'S6_09 writing run (1 = in its inventory)',
                       'S6_06_BLIND blind comparison', 'sweep 1 checks', 'total check events counted', 'documents'], CC)
cnt = collections.Counter(p[2].split(' ')[0] for p in P)
print('placed', len(P), 'read', sum(1 for p in P if p[4] == 'read'))
print('merges', len(MERGES), collections.Counter(m[2] for m in MERGES))
print('flags', len(FV), collections.Counter(v[2] for v in FV))
print('blind compared (rows of S6_01..05)', blind_compared, 'of which already checked by an intake', recheck_already)
print('chapters', sorted(cnt.items()))
print('check totals', collections.Counter(min(c[6], 5) for c in CC))
