# Adds the results of RESEARCH_SA08 (final of 19 Nov 2026, 10:27 UTC) to RESEARCH_SA09 as background, carries SA08's open
# item C.3 into SA09 as A.5, and adds the check of SA08's D-031 (Caradot-Lin, Prop. 3.10) as A.6.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 19 Nov 2026, on the model of a6d42bf6's add_sa10_results_to_prompts.py.
# Usage: python -I -B add_sa08_results_to_sa09.py
# It backs up PROMPT.md once (PROMPT_before_SA08_results_20261119.md), always rebuilds from that backup, writes
# SA08_RESULTS_20261119.md and SA08_final_paper_tex.zip into the build folder, and writes PROMPT.md in place.
import csv, hashlib, io, os, re, shutil, sys, zipfile
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents/'
FIN = D + 'grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped/'
SA08 = D + 'results_register/horizontal/sweep3/SA08/'
B = D + 'pro_prompt_builds/RESEARCH_SA09/'
res = {r['id']: r for r in csv.DictReader(open(FIN + 'RESEARCH_SA08_results.csv', encoding='utf-8', newline=''))}
run = list(csv.DictReader(open(FIN + 'CHECK_EVENTS.tsv', encoding='utf-8', newline=''), delimiter='\t'))
TOK = re.compile(r'(?<![A-Za-z0-9-])([A-D]-?\d+[A-Z]?)(?![A-Za-z0-9])')
norm = lambda s: s.strip().upper().replace('-', '')
cell = lambda s: ' '.join(s.replace('|', '/').split())

INTAKE = {   # the intake's check events (INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv) that bear on a statement
    'A-004': 'INT-SA08-E01 (independent re-proof: holds)',
    'A-026': 'INT-SA08-E02 (independent re-proof of part 1: holds); E03, E04 (computations: hold); '
             'E20 (targeted proof check of part 2, the reduction to the circle and the torus: holds)',
    'D001': 'INT-SA08-E13 (targeted check that the exact-adjoint mechanism is in the Pro notes of MPL_136_235-281, N32-N33: '
            'holds; the proof itself not re-derived)',
    'D002': 'INT-SA08-E13 (the mechanism is that of N32-N33: holds; the proof not re-derived)',
    'D003': 'INT-SA08-E13 (the mechanism is that of N32-N33: holds; the proof not re-derived)',
    'D005': 'INT-SA08-E13 (the localizing Serre closure is that of N71: holds; the proof not re-derived)',
    'C04': 'INT-SA08-E14 (targeted proof check of the notion of flasque only: the constant k is not flasque in the '
           'manuscript\'s sense; C04 itself not rechecked)',
}


def run_checks(i):
    c = Counter()
    for e in run:
        if norm(i) in {norm(t) for t in TOK.findall(e['statement_id'])}:
            c[' '.join(e['type'].split()).lower()] += 1
    return '; '.join('%d %s' % (n, t) for t, n in sorted(c.items())) or 'none recorded'


GROUPS = [
    ('For A.3 and L2: what the PD cochains of cote 136 recover', [
        'A-002', 'A-003', 'A-004', 'A-014', 'A-015', 'A-017', 'A-018', 'A-019', 'A-020', 'A-025', 'A-026', 'D-026',
        'D001', 'D002', 'D003', 'D004', 'D005', 'D006', 'D006E', 'D006M']),
    ('For A.1: natural PD laws on convolution algebras', ['D007', 'D008', 'D009', 'D010', 'D011', 'D012']),
    ('For A.4: flasqueness and contraction of simplicial modules', ['C02', 'C03', 'C04', 'C05']),
    ('For A.5: his uniqueness conjecture of cote 136 over Z (item C.3 of RESEARCH_SA08)', [
        'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21',
        'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36',
        'D022', 'D023', 'D-027', 'D-028', 'D-029', 'D-030', 'D-032']),
    ('For A.6: the check of D-031', ['D-031']),
]

HEAD = ('# Results of RESEARCH_SA08 that this prompt builds on\n\n'
        'RESEARCH_SA08 is the research run on the divided-power de Rham complex of cote 136 of the Grothendieck archive, by '
        'GPT-6 Astra (ChatGPT Pro mode), final of 19 Nov 2026, 10:27 UTC. Its report is headed INCOMPLETE: the run stopped '
        'under its two-review rule with C.3 (carried into this prompt as A.5) and the dating lead L7 undecided. It was taken '
        'in on 19 Nov 2026 by Claude Opus 5.5 at effort max (agent a34c04448e8299803); the intake is '
        '`intake/INTAKE_RESEARCH_SA08_20261119.md` in `SA08_final_paper_tex.zip`, with its check events in '
        '`intake/INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv`.\n\n'
        'Each row gives the statement id of that run, the statement, its status, where its proof is in the paper (the LaTeX '
        'is in `SA08_final_paper_tex.zip`), the check events the run recorded for it, counted by type, and the checks of the '
        'intake. A statement with no intake check has only the run\'s own checks: check it as you use it and record that '
        'check in your CHECK_EVENTS.tsv.\n')
COLS = '| id | statement | status | proof in | checks by the run | checks by the intake |\n|---|---|---|---|---|---|\n'


def results_md():
    out = HEAD
    for title, ids in GROUPS:
        out += '\n## %s\n\n' % title + COLS
        for i in ids:
            r = res[i]
            out += '| %s | %s | %s | %s | %s | %s |\n' % (i, cell(r['statement']), cell(r['status']), cell(r['where_proved']),
                                                         run_checks(i), cell(INTAKE.get(i, 'not checked by the intake')))
    return out


TOP = ['RESEARCH_SA08_paper.tex', 'RESEARCH_SA08_paper.bbl', 'RESEARCH_SA08_references.bib', 'RESEARCH_SA08_results.csv',
       'RESEARCH_SA08_corrections.tsv', 'CHECK_EVENTS.tsv', 'RESEARCH_SA08_report.md', 'PROGRESS_LEDGER.md']
SKIP_LOG = re.compile(r'ocr|fetch|download|source', re.I)   # fetched literature stays out; computation logs go in


def members():
    out = [(FIN + f, f) for f in TOP]
    for sub in ('sections', 'notes', 'code'):
        for f in sorted(os.listdir(FIN + sub)):
            if os.path.isfile(FIN + sub + '/' + f):
                out.append((FIN + sub + '/' + f, sub + '/' + f))
    for f in sorted(os.listdir(FIN + 'logs')):
        p = FIN + 'logs/' + f
        if os.path.isfile(p) and os.path.getsize(p) < 300_000 and not SKIP_LOG.search(f):
            out.append((p, 'logs/' + f))
    for f in ['INTAKE_RESEARCH_SA08_20261119.md', 'INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv',
              'intake_scripts/intake_checks_20261119.py', 'intake_scripts/intake_checks_20261119_output.txt']:
        out.append((SA08 + f, 'intake/' + os.path.basename(f)))
    return out


def texzip(path):
    buf = io.BytesIO(); man = ['path\torigin\tsha256']
    mem = members()
    assert any(a == 'logs/D_lifting_counterexample.json' for _, a in mem)
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for src, arc in mem:
            data = open(src, 'rb').read()
            z.writestr(arc, data)
            origin = ('research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped/%s (GPT-6 Astra, ChatGPT Pro mode)' % arc
                      if not arc.startswith('intake/') else
                      'results_register/horizontal/sweep3/SA08/%s (Claude Opus 5.5 at effort max, a34c04448e8299803)'
                      % src.split('/SA08/')[1])
            man.append('%s\t%s\t%s' % (arc, origin, hashlib.sha256(data).hexdigest()))
        z.writestr('MANIFEST.tsv', '\n'.join(man) + '\n')
    open(path, 'wb').write(buf.getvalue())
    assert len(buf.getvalue()) < 10_000_000
    return len(mem), len(buf.getvalue())


HEADER_OLD = '  - what the universal cosimplicial object with its Γ-operations recovers of a space.\n'
HEADER_NEW = HEADER_OLD + (
    '  - carried over from RESEARCH_SA08 (cote 136): his uniqueness conjecture for admissible generalized de Rham theories\n'
    '    over Z (A.5), and a check of that run\'s refutation of a published lifting proposition (A.6).\n')

BULLET = (
    '- **`SA08_RESULTS_20261119.md` and `SA08_final_paper_tex.zip`: the results of RESEARCH_SA08 that this prompt builds\n'
    '  on.**\n'
    '  - RESEARCH_SA08 is the research run on the divided-power de Rham complex of cote 136 (GPT-6 Astra, ChatGPT Pro mode,\n'
    '    final of 19 Nov 2026, 10:27 UTC). `SA08_RESULTS_20261119.md` lists the results used here by statement id, each\n'
    '    with its status, where its proof is, and its checks.\n'
    '  - `SA08_final_paper_tex.zip` holds that run\'s paper (`RESEARCH_SA08_paper.tex` with `sections/`), its results\n'
    '    register, corrections, check events, report and progress ledger, its proof notes (`notes/`), its programs\n'
    '    (`code/`), the small logs of its computations (`logs/`; the fetched sources are left out), and our intake of it\n'
    '    (`intake/`). `MANIFEST.tsv` gives the origin and SHA-256 of every file.\n'
    '  - The section "Results of RESEARCH_SA08" below places this prompt on them. A.5 and A.6 come from that run.\n')

SECTION = (
    '## Results of RESEARCH_SA08 that this prompt builds on (added 19 Nov 2026)\n\n'
    'Added by Claude Opus 5.5 at effort max (agent a34c04448e8299803) from its intake of RESEARCH_SA08. That run, by GPT-6\n'
    'Astra (ChatGPT Pro mode), worked on cote 136, the divided-power de Rham complex that cote 137 builds on. Cite its\n'
    'results by statement id. Each row of `SA08_RESULTS_20261119.md` says what was checked, by the run and by the intake.\n'
    'Check each result you use as you use it, and record that check in CHECK_EVENTS.tsv.\n\n'
    'They settle no item of this prompt outright. They place Part A as follows; Part B is untouched.\n\n'
    '**Changed: restate these before you work on them.**\n'
    '- **A.3.** Cote 136\'s weighted PD cochains already recover RΓ(X, Z) with its product, and H^*(X, Z) (D006); the E∞\n'
    '  cochain algebra after enhancement (D006E); and the integral weak homotopy type of a nilpotent space of finite type\n'
    '  (A-018, D006M, through Mandell 2006). Their comparisons with Horel, Toën, Cartan, numerical spaces and filtered\n'
    '  circles are A-019. R5 transports the weight-n PD de Rham complex to τ_{≤n}C^•. So A.3 is now: determine whether\n'
    '  that transport carries the cup product of R4 and the Γ-operations of A.1, prove it or show where it fails, and\n'
    '  derive from D006E and A-018 what C^*(X, Z) recovers. Answer his question of 137:39 and L2 on that basis.\n'
    '- **No binomial filtration.** There is no natural, exhaustive, filtered numerical cochain algebra over Int(Z), with\n'
    '  R-bilinear products, whose associated graded is the PD cochain algebra compatibly with coefficients (A-026; the\n'
    '  intake checked both parts). The coefficient statement gr Int(Z) = Γ_Z(T) holds (A-015); the ordinary numerical\n'
    '  associated graded is A-017; a weaker total and shadow lift exists (D-026); T = 1 gives Sullivan\'s polynomial forms\n'
    '  (A-025). In A.3, compare C^*(X, Z) with Horel\'s binomial rings through these, not through a filtered lift.\n'
    '- **Literal and graded cochains.** For infinite X they differ (A-002 to A-004). Say which one each statement of\n'
    '  cote 137 means.\n\n'
    '**Tools for the other items of Part A.**\n'
    '- **A.1.** The natural PD laws on a convolution algebra Hom(A, J) are given by an explicit equation set P(A) (D007).\n'
    '  A flat coalgebra has exactly one (D008); a finite nonflat coalgebra over Z/4 has none (D009); the two relations of\n'
    '  136/324 do not determine them (D010, D011); the dual laws are the typed divided copowers (D012). On 136/334 his\n'
    '  coefficient for γ^p(γ^q(x)) is the one for the opposite order; the right one is (pq)!/(p!(q!)^p) (correction D-C15\n'
    '  of RESEARCH_SA08). Check the composition through α_{q,p} on 137:75-86 for the same slip.\n'
    '- **A.4.** Slice acyclicity of a simplicial module is normalized acyclicity (C02). A flat tensor-universally flasque\n'
    '  simplicial module need not be additively contractible (C03, C04). Positive divided and exterior powers of flat\n'
    '  acyclic simplicial modules are flat tensor-universally flasque (C05). These bear on "flasque" in Lemma 2 and on\n'
    '  "ils seront même str. spéciaux!" (R2).\n\n'
    '**Added from RESEARCH_SA08.**\n'
    '- **A.5** carries over that run\'s one open mathematical item, his uniqueness conjecture for admissible generalized\n'
    '  de Rham theories over Z (cote 136, scans 117-121). Cote 137\'s universal objects (C^*, the Σ-exact property, the\n'
    '  Γ-operations) are tools that run did not have.\n'
    '- **A.6** is a check of that run\'s refutation of a published proposition (D-031).\n\n'
    '**Open:** A.1-A.6 and B.1-B.4, with the restatements above, and the Leads L1-L5 as they stand.\n\n')

ITEMS = (
    '- **A.5 (carried over from RESEARCH_SA08, its item C.3).** His uniqueness conjecture for admissible generalized de\n'
    '  Rham theories (cote 136, scans 117-121: "connexe et simplement connexe ?", conjectures a) and b)), over Z. Prove it\n'
    '  or refute it over Z, with the correct statement proved in its place.\n'
    '  - **Settled by RESEARCH_SA08.** Strict common-source equalization, the strict form of b), fails over every nonzero\n'
    '    ring (C07). The special universally flasque category has a contractible nerve (C06); so does the eventual\n'
    '    admissible category over a Q-algebra under uniform hypotheses (C08). Common sources and terminal localization\n'
    '    hold for explicit eventual-admissible theories over Z_(p)-algebras and over rings of positive characteristic (C09,\n'
    '    C10), and for generalized admissible strict PD theories over every ring with finitely many noninvertible rational\n'
    '    primes (C16, C17).\n'
    '  - **The item.** Common sources and terminal localization over rings with infinitely many noninvertible primes,\n'
    '    beginning with Z. Keep the two assertions apart.\n'
    '  - **The gate, as that run left it.** C30 builds a common source over Z from p-local admissible repairs\n'
    '    P_p → E_p → A_p, B_p whose first map is an isomorphism below a form degree d_p, with d_p → ∞. C32 builds terminal\n'
    '    localization in the same way from local repairs of the pair target A ×_k B and of the homotopy equalizer H(f, g).\n'
    '    C34 weakens the data to the finite form truncations of P with compatible target maps. None of these local\n'
    '    completions is constructed, and neither their existence nor their necessity is proved.\n'
    '  - **What was tried, and where it failed** (statement ids of that run):\n'
    '    - ordinary tensor products: prime-power Tor in unbounded weights (C11);\n'
    '    - independently marked free PD disks over Z: admissible only for the weight-one disk, and no map to A_N for\n'
    '      N > 1 (D022, D023);\n'
    '    - projection-preserving arithmetic gluing with unbounded first flasque weights (C12);\n'
    '    - the standard tails as an initial family (C13);\n'
    '    - free linear-disk replacements and free resolutions of the tails (C14, C15);\n'
    '    - ordinary common-target pushouts: unbounded degree-one cohomology, even rationally (C19);\n'
    '    - naive PD indecomposables, which are not invariant (C26), and a simple arity-homology pattern (D032);\n'
    '    - delayed p-local closures, which come without compatible target maps (C18);\n'
    '    - the global partial model, which needs floor((d+1)/2)! inverted (C21);\n'
    '    - automatic extension of a prescribed bar boundary: a counterexample over Z_(2) (C31);\n'
    '    - adjoining rational halves of odd products (C35);\n'
    '    - the finite-arity bar extensions (C24, C25, C27-C29, C36), which do not meet infinitely many eventual bounds at\n'
    '      once;\n'
    '    - a fixed finitely generated group of operations as the invariant: it cannot detect moving primes (C33);\n'
    '    - the lifting proposition of Caradot and Lin as stated (D-031; see A.6).\n'
    '  - **What this prompt adds.** Cote 137 builds the universal cosimplicial object C^* = DP(C^•), its Σ-exact universal\n'
    '    property (R3, A.2) and the Γ-operations (A.1, A.3). Determine whether they give the common source or the terminal\n'
    '    object over Z, or an invariant that separates admissible theories.\n'
    '  - **Where that run\'s state is,** in `SA08_final_paper_tex.zip`: `notes/C_findings.md`,\n'
    '    `notes/C_finite_prime_proof.md`, `notes/C_global_partial_model.md`, `notes/C_local_completion_attempts.md`,\n'
    '    `notes/C_terminal_repair_reduction.md`, `notes/D_arithmetic_repair_gluing.md`, `notes/D_global_local_repair_gate.md`,\n'
    '    `notes/D_final_local_repair_attempts.md`, `notes/B_C3_completion_after_C34.md`, and the other `notes/B_C3_*`,\n'
    '    `notes/C_*` and `notes/D_*` files they cite; the matching files in `sections/`; the C and D022-D032 rows of\n'
    '    `RESEARCH_SA08_results.csv` and of its `CHECK_EVENTS.tsv`; the reviews of 08:21-10:21 UTC in its\n'
    '    `PROGRESS_LEDGER.md`; and the section "Proved obstructions, approaches and remaining gates" of its\n'
    '    `RESEARCH_SA08_report.md`.\n'
    '- **A.6 (a check carried over from RESEARCH_SA08).** That run refutes Proposition 3.10 of A. Caradot and Z. Lin,\n'
    '  "Differential graded algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4: its statement\n'
    '  D-031, "unrestricted termwise-free chain-map lifting is false", proved in `sections/D_rejected_lifting_source.tex`,\n'
    '  with the program output `logs/D_lifting_counterexample.json`. The counterexample is an explicit square-zero PD DGA\n'
    '  projection from an identity disk to its lower-degree sphere, whose closed generator has no chain lift. The run\n'
    '  states that their Theorem 3.15, which assumes an acyclic target resolution, is not refuted. Check this\n'
    '  independently:\n'
    '  - fetch the arXiv LaTeX source of v4 and quote, with section, page and equation numbers, the exact statement of\n'
    '    Proposition 3.10, the definitions it uses (termwise freeness, Section 2.1) and the degree conventions;\n'
    '  - verify every hypothesis of Proposition 3.10 on the counterexample, and the impossibility of the lift, by hand and\n'
    '    by a program;\n'
    '  - determine which results of that paper use Proposition 3.10, Theorem 3.15 included, and whether the counterexample\n'
    '    reaches them;\n'
    '  - determine the hypothesis under which the lifting of Proposition 3.10 holds (an acyclic or cofibrant one, for\n'
    '    instance), and prove that corrected statement.\n'
    '  The item is done when the refutation is confirmed with these locators and the corrected statement is proved, or\n'
    '  when the refutation is shown wrong at an exact step. Record the check under the statement id D-031 in\n'
    '  CHECK_EVENTS.tsv.\n')

SOURCE = (
    '- A. Caradot and Z. Lin, "Differential graded algebras with divided powers and homotopy Lie algebras",\n'
    '  arXiv:2511.22614v4 (A.6): Section 2.1, Proposition 3.10, Theorem 3.15. For A.5, the sources that RESEARCH_SA08\n'
    '  cites are in its `RESEARCH_SA08_references.bib` and `notes/*.bib`, with that run\'s notes on which it opened.\n')

RULE5_OLD = 'the levels 2, 4 and 8 of the Kummer tower.'
RULE5_NEW = ('the levels 2, 4 and 8 of the Kummer tower; Z and the other rings with infinitely many\n'
             '   noninvertible primes (A.5).')
RULE7_OLD = '   corrections, and the Leads (inferences by Claude, Anthropic)'
RULE7_NEW = '   corrections, the results of RESEARCH_SA08, and the Leads (inferences by Claude, Anthropic)'

P = B + 'PROMPT.md'
bak = B + 'PROMPT_before_SA08_results_20261119.md'
if not os.path.exists(bak):
    shutil.copyfile(P, bak)
t = open(bak, encoding='utf-8', newline='').read()
assert '\r' not in t
for old, n in [(HEADER_OLD, 1), ('\n\n## Where this comes from', 1), ('\n\n## Leads', 1), ('\n\n**B. Cote 138.**', 1),
               ('\n\n## Rules of proof', 1), (RULE5_OLD, 1), (RULE7_OLD, 1)]:
    assert t.count(old) == n, old
t = t.replace(HEADER_OLD, HEADER_NEW, 1)
t = t.replace('\n\n## Where this comes from', '\n' + BULLET + '\n## Where this comes from', 1)   # last bullet of the list
t = t.replace('\n\n## Leads', '\n\n' + SECTION + '## Leads', 1)
t = t.replace('\n\n**B. Cote 138.**', '\n' + ITEMS + '\n**B. Cote 138.**', 1)          # after A.4, same list
t = t.replace('\n\n## Rules of proof', '\n' + SOURCE + '\n## Rules of proof', 1)         # last source bullet
t = t.replace(RULE5_OLD, RULE5_NEW, 1)
t = t.replace(RULE7_OLD, RULE7_NEW, 1)
with open(P, 'w', encoding='utf-8', newline='') as f:     # in place: hard links to this file keep pointing at it
    f.write(t)
with open(B + 'SA08_RESULTS_20261119.md', 'w', encoding='utf-8', newline='') as f:
    f.write(results_md())
n, size = texzip(B + 'SA08_final_paper_tex.zip')
print('PROMPT.md words', len(t.split()), '; zip members', n, 'bytes', size, '; files', sorted(os.listdir(B)))
