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
T = sys.argv[1]; topic = os.path.basename(os.path.normpath(T))
p = os.path.join(T, 'DELIVERABLES.tsv')
L = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip()]
head = L[0]
if 'translate_to' not in head: head += ['translate_to', 'why']
w = len(head); i_t, i_w = head.index('translate_to'), head.index('why'); n = 0
for r in L[1:]:
    r += [''] * (w - len(r))
    rule = RULES.get((topic, r[0]))
    if rule: r[i_t], r[i_w] = rule; n += 1
    else: print('no rule for', topic, r[0], r[1])
with open(p, 'w', encoding='utf-8', newline='\n') as f:
    for r in [head] + L[1:]: f.write('\t'.join(r[:w]) + '\n')
print(topic, 'rows with targets:', n)
