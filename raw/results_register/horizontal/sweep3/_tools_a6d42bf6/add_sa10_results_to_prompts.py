# Adds the results of RESEARCH_SA10 (final of 19 Nov 2026) as background to RESEARCH_SA11 and RESEARCH_SA20.
# Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026. Usage: python -I -B add_sa10_results_to_prompts.py
# It backs up each PROMPT.md, writes SA10_RESULTS_20261119.md and SA10_final_paper_tex.zip into each build folder,
# and inserts one attachment bullet and one section into each PROMPT.md (written in place).
import csv, hashlib, io, os, shutil, zipfile
D = 'C:/Users/user/Documents/'
FIN = D + 'grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA10_final_20261119T0540Z_unzipped/'
INT = D + 'results_register/horizontal/sweep3/SA10/INTAKE_RESEARCH_SA10_20261119_CHECK_EVENTS.tsv'
res = {r['id']: r for r in csv.DictReader(open(FIN + 'RESEARCH_SA10_results.csv', encoding='utf-8'))}
run = list(csv.DictReader(open(FIN + 'CHECK_EVENTS.tsv', encoding='utf-8'), delimiter='\t'))
mine = list(csv.DictReader(open(INT, encoding='utf-8'), delimiter='\t'))

def checks(i):
    from collections import Counter
    c = Counter(e['type'] for e in run if e['statement_id'].strip() == i)
    r = '; '.join('%d %s' % (n, t) for t, n in sorted(c.items())) or 'none recorded'
    m = [e for e in mine if any(p.strip().split(' ')[0] == i for p in e['statement_id'].replace(';', ',').split(','))]
    k = ', '.join('%s (%s: %s)' % (e['id'], e['type'], e['outcome'].split('. ')[0].split(': ')[0]) for e in m) or 'not checked by the intake'
    return r, k

HEAD = ('# Results of RESEARCH_SA10 that this prompt builds on\n\n'
        'RESEARCH_SA10 is the research run on the stratified spaces of cotes 150-151 of the Grothendieck archive, by GPT-6 Astra '
        '(ChatGPT Pro mode), final of 19 Nov 2026, 05:40 UTC. It was taken in on 19 Nov 2026 by Claude Opus 5.5 at effort max '
        '(agent a6d42bf6fe2b0d8a8). Each row gives the statement id of that run, the statement, its status, where its proof is '
        'in the paper (the LaTeX is in `SA10_final_paper_tex.zip`), the check events the run recorded for it, and the checks of '
        'the intake (type and outcome). A statement with no intake check has only the run\'s own checks: check it as you use it '
        'and record that check in your CHECK_EVENTS.tsv.\n\n'
        '| id | statement | status | proof in | checks by the run | checks by the intake |\n|---|---|---|---|---|---|\n')
K10 = ('| INT-SA10-K10 | For X = C with X_0 = {0} < X_1 = R < X_2 = C, the homotopy colimit of the homotopy types of the tubes '
       'of 151/057-061 (all pairs and triples, all inclusions) has first rational Betti number 4 (successor tubes only: 2); X is '
       'contractible. So the stones fail at the level of homotopy types as well as for sheaves. | computation of the intake '
       '(Bousfield-Kan double complex; the program gives 1, 0 on the actual Cech diagram of A1.2) | intake file '
       'INTAKE_RESEARCH_SA10_20261119_hocolim.py (not attached) | none | INT-SA10-E42 (computation or formal certificate: holds; '
       'the homotopy types of the tubes are a hand argument) |\n')

def table(ids, extra=''):
    out = HEAD
    for i in ids:
        r = res[i]; a, b = checks(i)
        cell = lambda s: s.replace('|', '/').replace('\n', ' ')
        out += '| %s | %s | %s | %s | %s | %s |\n' % (i, cell(r['statement']), cell(r['status']), cell(r['where_proved']), a, cell(b))
    return out + extra

TEX = ['RESEARCH_SA10_paper.tex', 'sections_A.tex', 'B_levels.tex', 'B56.tex', 'C_sections.tex', 'C1_collage_B.tex',
       'C4_path_proof_B.tex', 'C4_collar_proof_B.tex', 'C5_Hurewicz_C.tex', 'unresolved.tex', 'RESEARCH_SA10_references.bib',
       'references_A.bib', 'B_references.bib', 'references_B56.bib', 'C_references.bib', 'references_C5_Hurewicz.bib',
       'references_supplement.bib', 'RESEARCH_SA10_results.csv']

def texzip(path):
    buf = io.BytesIO(); man = ['path\torigin\tsha256']
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in TEX:
            data = open(FIN + f, 'rb').read()
            z.writestr(f, data)
            man.append('%s\tresearch_returns/RESEARCH_SA10_final_20261119T0540Z_unzipped/%s (GPT-6 Astra, ChatGPT Pro mode)\t%s'
                       % (f, f, hashlib.sha256(data).hexdigest()))
        z.writestr('MANIFEST.tsv', '\n'.join(man) + '\n')
    open(path, 'wb').write(buf.getvalue())
    assert len(buf.getvalue()) < 10_000_000

BULLET = ('- **`SA10_RESULTS_20261119.md` and `SA10_final_paper_tex.zip`:** the results of RESEARCH_SA10 (stratified spaces, '
          'cotes 150-151) that this prompt builds on, by statement id with status and checks, and the LaTeX of that run\'s paper '
          'with its results register. The section "Results of RESEARCH_SA10" below places this prompt on them.\n\n')
INTRO = ('## Results of RESEARCH_SA10 that this prompt builds on (added 19 Nov 2026)\n\n'
         'Added by Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8) from its intake of RESEARCH_SA10, the run of GPT-6 '
         'Astra (ChatGPT Pro mode) on the stratified spaces of cotes 150-151, final of 19 Nov 2026. `SA10_RESULTS_20261119.md` '
         'lists the results used here by statement id, each with its status and its checks; `SA10_final_paper_tex.zip` holds '
         'the paper with every proof. Cite them by statement id. Check each one you use as you use it, and record that check in '
         'CHECK_EVENTS.tsv.\n\n')
SEC = {'RESEARCH_SA11': INTRO + (
    'They settle no item of this prompt and change none of its questions: every item and lead below stays as it is. They bear '
    'on A.1 and A.2 as tools and cautions.\n'
    '- 𝒳 is glued from the discs Δ_D along a finite diagram of closed embeddings. A finite diagram of closed embeddings, even '
    'over a finite meet-semilattice, need not embed its members in its colimit (A4.2: seven indices, nineteen points, a '
    'two-point colimit). The exact criterion is that no zigzag of identifications joins two distinct points of one member, and '
    'the cartesian-meet condition X_{i∧j} ≅ X_i ×_{X_k} X_j implies it (A4.3). Prove by one of these that each disc, edge and '
    'vertex embeds in 𝒳 before you use it. A4.1 gives the topology of the colimit of a locally finite closed family.\n'
    '- A homotopy type is glued from pieces by an honest open cover or a full Čech diagram (A1.2, A1.5, B2.1); the colimit of '
    'ordinary topoi does not preserve shape (B2.2: Set ← BC₂ → Set). Compute the homotopy type of 𝒳 (L1) from a cell '
    'structure or an open cover.\n'
    '- That 𝒳 is a surface is a statement about its local links, separate from its combinatorics (C3.01, C3.04).\n\n'),
  'RESEARCH_SA20': INTRO + (
    'RESEARCH_SA10 settled the questions on the stratified spaces of cotes 150-151 that overlap Part A here. They place Part A '
    'as follows; Parts B-E are untouched, and the items of Part A keep their wording.\n\n'
    '**Settled: cite them, check them against his pages, and do what remains (A.6).**\n'
    '- The recollement of 039 for sheaves of sets is B1.1, an unconditional closed-open recollement by triples '
    '(L, E, E → i⁻¹j_*L), with A3.2 (the left adjoint j_!, and when restriction to the open union is an equivalence). What '
    'remains of the first bullet of A.6 is the six-functor version in the derived setting and its match with his formulas on '
    '039.\n'
    '- For smooth Thom-Mather spaces, "control data ⟷ manifolds with fibred boundaries and compatible corners" is the '
    'resolution theorem C2.05, a known result (Albin 2016, Th. 6.3; Albin-Leichtnam-Mazzeo-Piazza, Props. 2.2-2.7; '
    'Albin-Brasselet-Piazza, Th. 2.10 and 2.13; Mather, §7). Cite it with these locators and do not re-prove it. The second '
    'bullet of A.6 is then: state his data of 041-047 exactly, prove that they are the data of that theorem or name the '
    'hypothesis they lack, and prove the reconstruction outside it: n strata in his own form, and the PL and topological '
    'versions.\n'
    '- For the groupoid data of 043 in general: a full span of groupoids determines the two-stratum homotopy pushout when every '
    'piece is a K(π,1) (B4.1); the full flag diagram reconstructs X under pairwise asphericity (B4.2); forgetting the gluing '
    'coherence changes the space, Hopf S³ against S² × S¹ (B4.3); sets see π₀ of the exit mapping spaces and groupoid stacks '
    'see π₁ (B3.1, B3.2). What remains of the third bullet is dimension 2, worked out from these.\n\n'
    '**Changed: restate these points before you work on the items they touch.**\n'
    '- Pair pieces do not glue. For X = ℂ ⊃ ℝ ⊃ {0}, the diagram of all pair and triple tubes of 151/057-061 has neither Sh(X) '
    'as colimit (A1.3) nor the homotopy type of X as homotopy colimit (INT-SA10-K10: first Betti number 4 against 0). What '
    'glues is the tubes W_i of the strata in the whole space, chosen at once, with their actual pairwise and triple '
    'intersections (A1.2); A1.5 decides which pieces can be dropped. If 041-047 glue n strata along pair data, state the '
    'reconstruction theorem of A.6 with these overlaps.\n'
    '- Control data include π-control as an axiom, since the bare intersection conditions do not imply it (C2.01, C2.02); the '
    'whole radial collar germ, since one radius level does not determine control (C2.03); and the regular source bundles, '
    'since the bare recapitulation is not Thom-Mather data (C2.04).\n'
    '- Collars and manifoldness are hypotheses, not consequences. A homotopically stratified set need have no conical collar '
    '(C4.04, Quinn\'s shrinking hedgehog). Weak conical data do not give fibrancy (C1.01). A precylindrical stratification need '
    'not be a manifold with corners; C3.04 is the exact local criterion. In TOP neither manifold fibres nor manifold faces '
    'follow from the face conditions, while PL bundles and smooth submersions with those conditions give them (C5.03-C5.05; '
    'the matrix C5.08). State in which category each step of A.1, A.2 and A.6 is proved.\n'
    '- A locally finite closed family is the colimit of its pieces (A4.1), but a finite diagram of closed embeddings over a '
    'meet-semilattice need not embed its members (A4.2); the cartesian-meet condition repairs it (A4.3), and closure of the '
    'strata under binary intersection is (24) of 151/054 with an empty-bottom qualification (A4.4). This bears on the '
    'intersection axiom of A.3(c) and on the reconstruction of A.4.\n'
    '- Lower unions defined by supports do not commute with inverse images, and those defined by the order do (A2.2); the tubes '
    'of an open difference of cribles can change homotopy type (A3.1). This bears on "commuting with restriction to opens" in '
    'A.5 (049).\n\n'
    '**Open:** A.1-A.5 and A.7, as they stand with the restatements above. RESEARCH_SA10 worked in TOP, PL and smooth, not in '
    'an o-minimal structure, and it did not treat concordance spaces, rigidified collars or the cascade of 119/149-150.\n\n')}
IDS = {'RESEARCH_SA11': ['A1.2', 'A1.5', 'A4.1', 'A4.2', 'A4.3', 'A4.4', 'B2.1', 'B2.2', 'C3.01', 'C3.04'],
       'RESEARCH_SA20': ['A1.2', 'A1.3', 'A1.5', 'A2.2', 'A3.1', 'A3.2', 'A4.1', 'A4.2', 'A4.3', 'A4.4', 'B1.1', 'B3.1', 'B3.2',
                         'B4.1', 'B4.2', 'B4.3', 'C1.01', 'C1.B3', 'C2.01', 'C2.02', 'C2.03', 'C2.04', 'C2.05', 'C3.01', 'C3.04',
                         'C4.04', 'C5.02', 'C5.03', 'C5.04', 'C5.05', 'C5.08']}
for name in IDS:
    B = D + 'pro_prompt_builds/' + name + '/'
    P = B + 'PROMPT.md'
    bak = B + 'PROMPT_before_SA10_results_20261119.md'
    if not os.path.exists(bak):
        shutil.copyfile(P, bak)
    t = open(bak, encoding='utf-8').read()
    assert t.count('\n## Where this comes from') == 1 and t.count('\n## Leads') == 1
    t = t.replace('\n## Where this comes from', '\n' + BULLET.rstrip('\n') + '\n\n## Where this comes from', 1)
    t = t.replace('\n## Leads', '\n' + SEC[name] + '## Leads', 1)
    with open(P, 'w', encoding='utf-8', newline='') as f:     # in place: hard links to this file keep pointing at it
        f.write(t)
    open(B + 'SA10_RESULTS_20261119.md', 'w', encoding='utf-8', newline='').write(
        table(IDS[name], K10 if name == 'RESEARCH_SA20' else ''))
    texzip(B + 'SA10_final_paper_tex.zip')
    print(name, 'PROMPT.md words', len(t.split()), '; files', sorted(os.listdir(B)))
