# Sweep 2 part 2, SA11 (cotes 121, 153, 154, 155): agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026
DATE = '2026-11-18'
TITLE = 'SA11: tame topology (cote 121), the pseudoline surface (cote 154), analysers and tensor categories (cotes 153, 155)'
INTRO = '''
The topic is "Espaces stratifiés", part 2. It holds:
- **Cote 121:** the later drafts of his tame-topology axioms.
- **Cote 154:** the combinatorial surface of relative positions of one more projective pseudoline (the Esquisse, section 8), worked through deployments, the disk model, polygon transport and sweeps.
- **Cotes 153 and 155:** analysers and the rigidity of tensor categories. They are algebra, filed here by catalogue order.

The shared package MPL_81_038-055+154_046-076 (cote 154, scans 46-76) is also indexed under SA01.

Heavy notes: the Pro packages MPL_121_049-073+153+155 and MPL_154_* (GPT-6 Astra, ChatGPT Pro mode). Light notes: Work and Codex K154-01_3, K154-02.
'''
ORDER = [
 ('Tame topology (cote 121) and the requested comparisons', ['SA11-3', 'SA11-4', 'SA11-1', 'SA11-2']),
 ('The surface of relative positions of a pseudoline (cote 154)', ['SA11-8', 'SA11-9', 'SA11-10', 'SA11-11', 'SA11-12', 'SA11-13', 'SA11-14', 'SA11-16', 'SA11-17', 'SA11-19', 'SA11-20']),
 ('Algebra filed here: analysers and tensor categories (cotes 153, 155)', ['SA11-5', 'SA11-6']),
 ('Reading questions, documentary and apparatus', ['SA11-15', 'SA11-18', 'SA11-7']),
]
DEPS = [
 ('SA11-9', 'SA11-8', 'his page', '154/1-45: deployments of the relative-position surface'),
 ('SA11-10', 'SA11-9', 'his page', '154/20-44: specialization and generization of deployments; weights and the polygon invariant'),
 ('SA11-11', 'SA11-8', 'his page', '154: local gluing of the cellular surface'),
 ('SA11-12', 'SA11-11', 'his page', '154: the disk model refines the local gluing'),
 ('SA11-13', 'SA11-9', 'his page', '154/71-88: the deployment by two cellular graphs K and L'),
 ('SA11-14', 'SA11-11', 'his page', '154/62-65: transport along edges and its dihedral monodromy'),
 ('SA11-16', 'SA11-8', 'his page', '154/127-176: the cartographic dictionary of the surface'),
 ('SA11-17', 'SA11-9', 'his page', '154/127-176: the sweeps sigma_0 and sigma_1 and the endpoint construction'),
 ('SA11-19', 'SA11-8', 'his page', '154/127-176: pencils of pseudolines'),
 ('SA11-20', 'SA11-8', 'his page', '154/46-76: the natural-map schemes on the surface'),
 ('SA11-4', 'SA11-3', 'our note', 'the comparisons take the cote 121 axiomatics'),
]
RELATED = [
 ('SA11-6', 'SA11-5', 'our note', 'the same package: analysers and the Tannakian-type duality of cotes 153 and 155 (H00N, H00O)'),
 ('SA11-8', 'SA04-28', 'our note', 'the pseudoline systems of cote 80 (= H02W)'),
 ('SA11-8', 'SA01-9', 'a proof (ours)', 'the same package entries, indexed under SA01'),
 ('SA11-3', 'SA10-19', 'our note', 'cote 120 (H00K) and cote 121 (H00M)'),
 ('SA11-1', 'SA10-2', 'our note', 'the requested question on tubulure and ombre (H05G)'),
 ('SA11-2', 'SA10-3', 'our note', 'the Remords (H00L)'),
 ('SA11-5', 'SA08-6 (cote 133: binomial and lambda-rings)', 'our note (broad agent)', 'a link inferred by the broad agent, not merged'),
]
CLAIMS = [
 ['SA11-C1', 'the polygon invariant determines the deployment (expected injective)', '154/20-44', 'SA11-10', 'none', 'conjecture (his)', 'his page', 'MPL_154_001-045 notes'],
 ['SA11-C2', 'the rotation formula: frozen rho_som rho_f = sigma_2 sigma_0 = sigma; Hua reads rho_f = sigma_2 sigma_0', '154/032', 'SA11-15', 'none; the normalized products agree; the scan decides the first factor', 'reading conflict (open)', 'our note', 'MPL_154_001-045 Q07'],
 ['SA11-C3', 'the axiomatics of moderate spaces (adapted partitions, graphs, conservativity, effective epimorphisms, triangulation)', '121/49-73', 'SA11-3', 'none; several axioms unfinished or self-flagged', 'his claim (stated)', 'his page', 'MPL_121_049-073+153+155 notes'],
]
CORR = [
 ['SA11-K1', 'SA11-8', 'MPL_81_038-055+154_046-076', 'placement', 'indexed under SA01 and SA11', 'cote 154, scans 46-76: SA11 only', 'sweep 1', 'placement'],
 ['SA11-K2', 'SA11-15', '154/032 (Q07)', 'reading conflict (open)', 'frozen rho_som rho_f = sigma_2 sigma_0 = sigma; Hua: rho_f = sigma_2 sigma_0', 'undecided: the scan decides the first factor', 'MPL_154_001-045 Q07', 'not decided (scan not viewed)'],
 ['SA11-K3', 'SA11-15', '154/044 (Q13)', 'editorial status', 'the struck 0/1 definition of epsilon(s), restored editorially by Hua', 'not a reading question: the definition is struck on this leaf', 'MPL_154_001-045 Q13', 'our note'],
 ['SA11-K4', 'SA11-5', 'cotes 153, 155', 'placement', 'filed under stratified spaces by catalogue order', 'algebra: lambda-rings and plethories (H00N); Tannakian duality (H00O)', 'sweep 1', 'placement'],
]
CHECKS3 = []
