# Add or refresh the columns translate_to and why in a topic's DELIVERABLES.tsv (agent a6d42bf6, horizontal sweep 3, 19 Nov 2026).
# usage: python -I -B add_translation_targets.py <topic dir>   (idempotent; run after write_tables.py and merge_readings.py)
# Sources: knowledge/03_archive/translation_targets.md (the main session's assessment, 18 Nov) and the user's points in
# memory translation-targets-by-field.md. The originals are French, so French readers read the transcription itself; French
# is a target for our own companion and results, not for his text. English comes first for every stretch.
# Never automatic: each target is weighed against the same compute spent on SGA/EGA in that language before it is used.
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
TAME = 'tame topology and o-minimality: the Lojasiewicz school (Krakow) for Polish; Shiota\'s tame topology (Nagoya) for Japanese; real algebraic geometry in Madrid for Spanish; the stratification and singularity school of Sao Carlos for Brazilian Portuguese'
FINITE = 'finite topological spaces and Alexandrov spaces: the Buenos Aires school (Minian, Barmak: Algebraic topology of finite topological spaces, LNM 2032, 2011) for Spanish'
RULES = {
 ('SA21', '156-1 + 156-2'): ('English; Polish; Japanese; Spanish; Brazilian Portuguese', 'one-dimensional forms and networks, the first case of his tame axiomatics: ' + TAME + '. Elementary enough for students, where Spanish and Brazilian Portuguese reach the largest communities'),
 ('SA21', '156-3'): ('English; Polish; Spanish; Japanese; Brazilian Portuguese', 'the o-minimal line written down in June 1986 (tame parts = finite unions of points and intervals): the model-theoretic and o-minimal communities, Polish first (Lojasiewicz school; model theory in Wroclaw); ' + TAME),
 ('SA21', '156-4'): ('English; Polish; Japanese; Spanish; Brazilian Portuguese', 'contrees and their axioms, the supports, the Hauptvermutung as an axiom: ' + TAME + '. The event-structure link (H1) is read in English by its community (Aarhus, Cambridge)'),
 ('SA21', '156-5'): ('English; Spanish; Polish; Japanese; Brazilian Portuguese', 'the set-theoretic model and its ultratopologies (preorders, T0 Alexandrov topologies): ' + FINITE + '; then ' + TAME),
 ('SA21', '156-6'): ('English; Polish; Japanese; Spanish; Brazilian Portuguese', 'the atelier, refinement primitive, T0 Alexandrov language: ' + TAME + '; ' + FINITE),
 ('SA21', '156-7'): ('English; Polish; Japanese; Spanish; Brazilian Portuguese', 'ateliers, polyhedral and simplicial conditions, supports and his counterexamples to distributivity: ' + TAME + '; ' + FINITE),
 ('SA21', '156-8'): ('English; Spanish; Polish; Japanese; Brazilian Portuguese', 'magasins and maquettes (finite T0 spaces; oriented maquettes as Serre graphs and cell complexes): ' + FINITE + ' first; then ' + TAME),
 ('SA21', '156-9'): ('English; Spanish; Polish; Japanese; Brazilian Portuguese', 'ortholattices and the orthomodular law, comparability magasins: the quantum-logic schools of Bratislava, Prague and Cagliari/Florence read English at research level, so Slovak, Czech and Italian are weighed and not proposed; ' + FINITE + '; ' + TAME),
 ('SA10', '150'): ('English; Japanese; Brazilian Portuguese; Spanish; Polish', 'stratified spaces, conical neighbourhoods and the moduli of stable curves (folios 9, 15-16): the Teichmuller and anabelian line at RIMS Kyoto for Japanese; the Sao Carlos stratification school for Brazilian Portuguese; Madrid and Zaragoza for Spanish; the Lojasiewicz school for Polish'),
 ('SA10', '150 + 151'): ('English; Japanese; Brazilian Portuguese; Spanish; Polish', 'the end of the stratification notes and the beginning of the stratified topos: as for cote 150; the topos-theoretic side is read in English and French'),
 ('SA10', '151'): ('English; Japanese; Brazilian Portuguese; Spanish; Polish', 'the stratified topos of 1981, its gluing of tubes and its Teichmuller programme (151/44): Japanese first, for the Teichmuller-tower and anabelian community at RIMS Kyoto; then the stratification schools (Sao Carlos, Madrid, Krakow)'),
 ('SA10', '152 + 120'): ('English; Spanish; Polish; Japanese', 'plane trees (dessins d\'enfants: Madrid, besides France) and his tame-geometry axioms M1-M11 (Krakow, Nagoya)'),
 ('SA11', '154'): ('English; Spanish; Japanese; Brazilian Portuguese', 'pseudoline arrangements, oriented matroids and the surface of relative positions (Esquisse section 8): Santander (Santos) and Madrid for Spanish; discrete and computational geometry in Japan; Berlin (Ziegler) and Paris (Las Vergnas) read English and French; Brazilian Portuguese for the student community'),
 ('SA11', '121'): ('English; Polish; Japanese; Spanish; Brazilian Portuguese', 'his axiomatics of tame spaces (adapted partitions, triangulation): ' + TAME),
 ('SA11', '121 + 153 + 155'):('English; Japanese; Polish; Spanish', 'tame spaces (cote 121: Krakow, Nagoya, Madrid), analysers and plethories (cote 153, read in English), Tannakian duality and bialgebroids (cote 155: Takeuchi\'s school in Japan, besides Germany and France)'),
}

# SA04 (wave 1, 19 Nov 2026): keyed on the cote (the first token of cote_part); same rule: where the topic is most studied.
PADIC = 'p-adic Hodge theory and crystals: the Kato-Tsuji school (Tokyo, Kyoto) for Japanese; the p-adic Hodge and arithmetic geometry groups of Beijing and Shanghai for Chinese; Bonn, Harvard and Cambridge read English'
POLY = 'abstract regular polytopes and maps: the UNAM school (Hubard, Pellicer; Mexico City and Morelia) for Spanish; Toronto/Boston (McMullen, Schulte), Auckland (Conder) and Bratislava/Banska Bystrica (Siran, Nedela) read English'
DESS = 'regular maps, dessins and congruence questions: Madrid (Gonzalez-Diez, Girondo) for Spanish; the Moscow school of Shabat and Zvonkin for Russian; Southampton (Jones, Singerman) reads English'
PREFIX = {
 ('SA04', '93'): ('English; Japanese; Chinese', PADIC),
 ('SA04', '161-5'): ('English; Japanese; Chinese', PADIC + '. The offprints (161-5/3-22) are Serre\'s printed texts: cited, never translated by us'),
 ('SA04', '69'): ('English; Japanese; Chinese', 'the 27 lines, E6 and generalized quadrangles: the Bannai school of algebraic combinatorics (Japan) for Japanese; algebraic combinatorics in China for Chinese; Ghent (Thas, Van Maldeghem) reads English'),
 ('SA04', '74'): ('English; Japanese; Chinese', 'as for cote 69 (the series of trialitarian graphs, 3-nets and loops); loop theory (Prague, Denver) reads English'),
 ('SA04', '70'): ('English; Spanish', POLY),
 ('SA04', '72'): ('English; Spanish', POLY),
 ('SA04', '73'): ('English; Spanish; Brazilian Portuguese', 'elementary polygon geometry, close to teaching: ' + POLY + '; Brazilian Portuguese for the student community'),
 ('SA04', '76'): ('English; Spanish', POLY),
 ('SA04', '77'): ('English', 'quadratic forms and quadratic algebras over a base (Knus, Loos, Voight, Wood): a community that reads English; the French original serves France and Switzerland'),
 ('SA04', '78'): ('English; Spanish; Brazilian Portuguese', 'a course on regular polygons over rings (Nov-Dec 1977): students first, where Spanish and Brazilian Portuguese reach the largest communities; ' + POLY),
 ('SA04', '79'): ('English; Spanish; Russian', DESS),
 ('SA04', '80'): ('English; Spanish; Japanese; Brazilian Portuguese', 'pseudoline arrangements and oriented matroids, as for cote 154 (SA11): Santander and Madrid for Spanish; discrete geometry in Japan; Brazilian Portuguese for the student community'),
 ('SA04', '82'): ('English', 'rank-3 quadratic modules and the forms of SO(3) over a base: read in English'),
 ('SA04', '85'): ('English; Spanish; Russian', DESS),
 ('SA04', '86'): ('English; Spanish', POLY), ('SA04', '87'): ('English; Spanish', POLY), ('SA04', '88'): ('English; Spanish', POLY), ('SA04', '89'): ('English; Spanish', POLY),
 ('SA04', '161-1'): ('English', 'SA23\'s topic in sweep 2-3: its assessment applies'), ('SA04', '161-2'): ('English', 'SA23\'s topic: its assessment applies'),
 ('SA04', '161-3'): ('English', 'SA23\'s topic: its assessment applies'), ('SA04', '161-4'): ('English', 'SA23\'s topic: its assessment applies'),
 ('SA04', '161-6'): ('English; Spanish', 'the Euclidean icosahedron and graphs in surfaces: ' + POLY),
 ('SA04', '94'): ('English', 'representability of linear functors (EGA III 7.7): foundations read in English and French'),
 ('SA04', '97'): ('English', 'Chern classes of representations and Fuchsian groups: read in English'),
 ('SA04', '98'): ('English', 'norms and bounded families (SGA 4 XVII, SGA 6 XIII): read in English and French'),
 ('SA04', '100'): ('English; Japanese; Chinese', 'good reduction of abelian schemes through p-divisible groups: ' + PADIC),
 ('SA04', '101'): ('English; Japanese; Spanish', 'local cohomology and Gorenstein rings: the Goto school of Cohen-Macaulay and Gorenstein rings (Japan) for Japanese; commutative algebra in Barcelona and Valladolid for Spanish; India (TIFR, CMI) reads English'),
 ('SA01', '71'): ('English; Spanish; Brazilian Portuguese', 'plane polygons and the polygonal Jordan theorem (a 1976 manuscript by another author, with margins): elementary geometry close to teaching, where Spanish and Brazilian Portuguese reach the largest student communities'),
 ('SA01', '72'): ('English; Spanish', POLY),
 ('SA01', '75'): ('English; Spanish; Brazilian Portuguese', 'the DEA course Geometries combinatoires (1977-78): students first; ' + POLY),
 ('SA01', '81'): ('English; Spanish; Russian', 'plane trees, non-crossing partitions and folded discs, the combinatorics behind dessins: ' + DESS),
 ('SA01', '83'): ('English; Japanese', '2x2 matrices, Azumaya algebras of rank 4 and trace invariants: the invariant-theory community reads English; the Japanese school of quaternion orders and arithmetic of quadratic forms for Japanese'),
 ('SA01', '93'): ('English; Japanese; Chinese', 'projective connections, opers and uniformization in characteristic p: the Mochizuki school (RIMS Kyoto: p-adic Teichmuller theory, dormant opers) for Japanese; ' + PADIC),
 ('SA02', '84'): ('English; Japanese', 'quadratic covers, their contracted product and Arf invariants over a base: the community of quadratic forms and quadratic rings (Knus, Loos, Voight, Wood) reads English; the Japanese school of quadratic forms and arithmetic invariants for Japanese'),
 ('SA02', '90'): ('English', 'representations of flat affine group schemes over a Dedekind ring and the equivariant resolution property (Serre 1968, Thomason 1987): read in English and French'),
 ('SA02', '91'): ('English', 'Hom functors and flattening without projective hypotheses (Raynaud-Gruson): read in English and French'),
 ('SA04', '102'): ('English', 'Pour EGA VI: foundations read in English and French'),
}
T = sys.argv[1]; topic = os.path.basename(os.path.normpath(T))
p = os.path.join(T, 'DELIVERABLES.tsv')
L = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip()]
head = L[0]
if 'translate_to' not in head: head += ['translate_to', 'why']
w = len(head); i_t, i_w = head.index('translate_to'), head.index('why'); n = 0
for r in L[1:]:
    r += [''] * (w - len(r))
    rule = RULES.get((topic, r[0])) or PREFIX.get((topic, r[0].split(' ')[0]))
    if rule: r[i_t], r[i_w] = rule; n += 1
    else: print('no rule for', topic, r[0], r[1])
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    for r in [head] + L[1:]: f.write('\t'.join(r[:w]) + '\n')
print(topic, 'rows with targets:', n)
