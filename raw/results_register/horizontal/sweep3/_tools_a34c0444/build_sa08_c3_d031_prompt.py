# Builds pro_prompt_builds/RESEARCH_SA08_C3_D031/: one small Pro prompt for C.3 (RESEARCH_SA08's open item) and the check
# of D-031 (Caradot-Lin, arXiv:2511.22614v4, Prop. 3.10), with a small input ZIP.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 19 Nov 2026. Usage: python -I -B build_sa08_c3_d031_prompt.py
# The procedure sections are copied word for word from pro_prompt_builds/RESEARCH_SA08/PROMPT.md (the prompt as sent),
# with only the file prefix changed.
import csv, hashlib, io, os, re, sys, zipfile
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents/'
F8 = D + 'grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped/'
F9 = D + 'grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA09_final_20261119T1146Z_unzipped/RESEARCH_SA09/'
H = D + 'results_register/horizontal/sweep3/'
OUT = D + 'pro_prompt_builds/RESEARCH_SA08_C3_D031/'
PFX = 'RESEARCH_SA08_C3_D031'
ZIPNAME = PFX + '_inputs.zip'
os.makedirs(OUT, exist_ok=True)

# ---------- the statements and files the two items need
r8 = list(csv.DictReader(open(F8 + 'RESEARCH_SA08_results.csv', encoding='utf-8', newline='')))
IDS8 = (['C%02d' % i for i in range(6, 37)] + ['D022', 'D023', 'D-027', 'D-028', 'D-029', 'D-030', 'D-031', 'D-032'])
rows8 = [r for r in r8 if r['id'] in IDS8]
assert len(rows8) == len(IDS8), sorted(set(IDS8) - {r['id'] for r in rows8})
secs = set()
for r in rows8:
    secs |= set(re.findall(r'sections/([A-Za-z0-9_]+\.tex)', r['where_proved']))
secs.add('D_rejected_lifting_source.tex')
secs = sorted(s for s in secs if os.path.isfile(F8 + 'sections/' + s))
TOK = re.compile(r'(?<![A-Za-z0-9-])([A-D]-?\d+[A-Z]?)(?![A-Za-z0-9])')
norm = lambda s: s.strip().upper().replace('-', '')
want = {norm(i) for i in IDS8}
ce8 = list(csv.reader(open(F8 + 'CHECK_EVENTS.tsv', encoding='utf-8', newline=''), delimiter='\t'))
ce8 = [ce8[0]] + [e for e in ce8[1:] if want & {norm(t) for t in TOK.findall(e[0])}]
rep = open(F8 + 'RESEARCH_SA08_report.md', encoding='utf-8').read()
gates = rep[rep.index('## Proved obstructions, approaches and remaining gates'):]
r9 = list(csv.DictReader(open(F9 + 'RESEARCH_SA09_results.csv', encoding='utf-8', newline='')))
IDS9 = ['A2.1', 'A2.2', 'A2.3', 'A2.4', 'A2.5', 'A2.6', 'A3.1', 'A3.2', 'A3.3', 'A3.4', 'A3.5']
rows9 = [r for r in r9 if r['id'] in IDS9]
assert len(rows9) == len(IDS9)
st9 = {r['id']: ' '.join(r['statement'].split()).rstrip('.') for r in rows9}


def csvtext(fields, rows, delim=','):
    b = io.StringIO(); w = csv.writer(b, delimiter=delim, lineterminator='\n')
    w.writerow(fields)
    for r in rows:
        w.writerow([r[f] for f in fields] if isinstance(r, dict) else r)
    return b.getvalue().encode('utf-8')


members = []          # (arcname, bytes, origin)
O8 = 'research_returns/RESEARCH_SA08_final_20261119T1027Z_unzipped/'
O9 = 'research_returns/RESEARCH_SA09_final_20261119T1146Z_unzipped/RESEARCH_SA09/'
for s in secs:
    members.append(('SA08/sections/' + s, open(F8 + 'sections/' + s, 'rb').read(), O8 + 'sections/' + s))
members.append(('SA08/RESEARCH_SA08_results_C3_D031.csv', csvtext(list(r8[0].keys()), rows8),
                O8 + 'RESEARCH_SA08_results.csv, the rows ' + ', '.join(IDS8)))
members.append(('SA08/CHECK_EVENTS_C3_D031.tsv', csvtext(None, ce8, '\t') if False else
                ('\n'.join('\t'.join(e) for e in ce8) + '\n').encode('utf-8'), O8 + 'CHECK_EVENTS.tsv, the rows of those statements'))
members.append(('SA08/report_gates.md', gates.encode('utf-8'), O8 + 'RESEARCH_SA08_report.md, its last section'))
for f in ['RESEARCH_SA08_references.bib', 'logs/D_lifting_counterexample.json', 'code/D_lifting_counterexample.py']:
    members.append(('SA08/' + f, open(F8 + f, 'rb').read(), O8 + f))
for s in ['A2.tex', 'A3.tex']:
    members.append(('SA09/sections/' + s, open(F9 + 'sections/' + s, 'rb').read(), O9 + 'sections/' + s))
members.append(('SA09/RESEARCH_SA09_results_A2_A3.csv', csvtext(list(r9[0].keys()), rows9),
                O9 + 'RESEARCH_SA09_results.csv, the rows ' + ', '.join(IDS9)))
for d, f in [('SA08', 'INTAKE_RESEARCH_SA08_20261119.md'), ('SA08', 'INTAKE_RESEARCH_SA08_20261119_CHECK_EVENTS.tsv'),
             ('SA09', 'INTAKE_RESEARCH_SA09_20261119.md'), ('SA09', 'INTAKE_RESEARCH_SA09_20261119_CHECK_EVENTS.tsv')]:
    members.append(('intakes/' + f, open(H + d + '/' + f, 'rb').read(), 'results_register/horizontal/sweep3/%s/%s' % (d, f)))
buf = io.BytesIO(); man = ['path\torigin\tsha256']
with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
    for arc, data, origin in members:
        z.writestr(arc, data)
        man.append('%s\t%s\t%s' % (arc, origin, hashlib.sha256(data).hexdigest()))
    z.writestr('MANIFEST.tsv', '\n'.join(man) + '\n')
open(OUT + ZIPNAME, 'wb').write(buf.getvalue())

# ---------- the prompt
src = open(D + 'pro_prompt_builds/RESEARCH_SA08/PROMPT.md', encoding='utf-8', newline='').read()
assert '\r' not in src


def section(head, nxt):
    a = src.index('\n' + head) + 1
    b = src.index('\n' + nxt, a) + 1 if nxt else len(src)
    return re.sub(r'RESEARCH_SA08(?!_C3)', PFX, src[a:b])


OUTCOME = section('## What the outcome must be', '## Parts')
RULES = section('## Rules of proof', '## What to deliver')
DELIVER = section('## What to deliver', None)

HEAD = (
    '# ' + PFX + ': Grothendieck\'s uniqueness conjecture for admissible generalized de Rham theories over Z (cote 136, '
    'scans 117-121), and a check of Caradot-Lin, arXiv:2511.22614v4, Proposition 3.10\n\n'
    '**What is to be settled, in two Parts:**\n'
    '- **A.** His uniqueness conjecture for admissible generalized de Rham theories (cote 136, scans 117-121), over Z: the\n'
    '  one open mathematical item of RESEARCH_SA08, its C.3. A is the main question.\n'
    '- **B.** A check of RESEARCH_SA08\'s refutation of Proposition 3.10 of A. Caradot and Z. Lin, "Differential graded\n'
    '  algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4 (its statement D-031).\n\n'
    'For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `' + PFX + '`.\n\n'
    '**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a34c04448e8299803, on 19 Nov 2026, from its\n'
    'intakes of RESEARCH_SA08 and RESEARCH_SA09. The main session (Claude Opus 5.5 at effort max) decided on this prompt.\n\n'
    '## What is attached\n\n'
    '- **`' + ZIPNAME + '`: the parts of two research runs that the items need, and our intakes of them.**\n'
    '  - `SA08/`: from the final of RESEARCH_SA08 (GPT-6 Astra, ChatGPT Pro mode, 19 Nov 2026, 10:27 UTC), the TeX\n'
    '    sections in which every statement named below is proved (`SA08/sections/`); the rows of its results register\n'
    '    and of its check events for those statements (`RESEARCH_SA08_results_C3_D031.csv`, `CHECK_EVENTS_C3_D031.tsv`);\n'
    '    the last section of its report, on the gates and the approaches tried (`report_gates.md`); its bibliography; and\n'
    '    the program and output of the D-031 counterexample (`code/D_lifting_counterexample.py`,\n'
    '    `logs/D_lifting_counterexample.json`).\n'
    '  - `SA09/`: from the final of RESEARCH_SA09 (GPT-6 Astra, ChatGPT Pro mode, 19 Nov 2026, 11:46 UTC), the sections\n'
    '    A2 and A3 and the rows A2.1-A3.5 of its results register.\n'
    '  - `intakes/`: our intakes of both finals, with their check events, by Claude Opus 5.5 at effort max (Anthropic).\n'
    '  - `MANIFEST.tsv` gives the origin and SHA-256 of every file.\n'
    '- **No literature is attached.** Fetch the sources listed under "Sources", preferring the arXiv LaTeX source.\n\n'
    '## Where this comes from\n\n'
    'RESEARCH_SA08 worked on cote 136 of the Grothendieck archive, his divided-power de Rham complex of 1975-76. It\n'
    'settled every item but C.3 and stopped under its two-review rule; its report is headed INCOMPLETE. RESEARCH_SA09\n'
    'worked on cote 137, where he builds the integral framework of the same programme: the walking complex, the universal\n'
    'cosimplicial object and its Γ-operations. It settled all its items in 43 minutes. Our intakes checked parts of both;\n'
    'what they checked, and what they did not, is in `intakes/`. Every statement of either run that you use is checked\n'
    'by you where you use it (Rules of proof, 7). Cite them by statement id: C06, D-031, A3.2, and so on.\n\n')

ITEMS = (
    '## Parts\n\n'
    '**A. The uniqueness conjecture over Z. A is the main question.**\n'
    '- **A (RESEARCH_SA08\'s item C.3).** His uniqueness conjecture for admissible generalized de Rham theories (cote 136,\n'
    '  scans 117-121: "connexe et simplement connexe ?", conjectures a) and b)), over Z. Prove it or refute it over Z,\n'
    '  with the correct statement proved in its place.\n'
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
    '    - naive PD indecomposables, which are not invariant (C26), and a simple arity-homology pattern (D-032);\n'
    '    - delayed p-local closures, which come without compatible target maps (C18);\n'
    '    - the global partial model, which needs floor((d+1)/2)! inverted (C21);\n'
    '    - automatic extension of a prescribed bar boundary: a counterexample over Z_(2) (C31);\n'
    '    - adjoining rational halves of odd products (C35);\n'
    '    - the finite-arity bar extensions (C24, C25, C27-C29, C36), which do not meet infinitely many eventual bounds at\n'
    '      once;\n'
    '    - a fixed finitely generated group of operations as the invariant: it cannot detect moving primes (C33);\n'
    '    - the lifting proposition of Caradot and Lin as stated (D-031; see B).\n'
    '  - **The new tools, proved by RESEARCH_SA09 on cote 137.** Cote 137 builds the universal cosimplicial object\n'
    '    C^* = DP(C^•), its Σ-exact universal property and its Γ-operations. RESEARCH_SA09 proved:\n'
    '    - A2.2: ' + st9['A2.2'] + ';\n'
    '    - A3.1: ' + st9['A3.1'] + ';\n'
    '    - A3.2: ' + st9['A3.2'] + '.\n'
    '    Determine whether they give the common source or the terminal object over Z, or an invariant that separates\n'
    '    admissible theories.\n'
    '  - **Where that run\'s state is:** `SA08/sections/` (the proofs of every statement named here),\n'
    '    `SA08/RESEARCH_SA08_results_C3_D031.csv`, `SA08/CHECK_EVENTS_C3_D031.tsv` and `SA08/report_gates.md`.\n\n'
    '**B. The check of D-031.**\n'
    '- **B (a check carried over from RESEARCH_SA08).** That run refutes Proposition 3.10 of A. Caradot and Z. Lin,\n'
    '  "Differential graded algebras with divided powers and homotopy Lie algebras", arXiv:2511.22614v4: its statement\n'
    '  D-031, "unrestricted termwise-free chain-map lifting is false", proved in `SA08/sections/D_rejected_lifting_source.tex`,\n'
    '  with the program `SA08/code/D_lifting_counterexample.py` and its output `SA08/logs/D_lifting_counterexample.json`.\n'
    '  The counterexample is an explicit square-zero PD DGA projection from an identity disk to its lower-degree sphere,\n'
    '  whose closed generator has no chain lift. The run states that their Theorem 3.15, which assumes an acyclic target\n'
    '  resolution, is not refuted. Check this independently:\n'
    '  - fetch the arXiv LaTeX source of v4 and quote, with section, page and equation numbers, the exact statement of\n'
    '    Proposition 3.10, the definitions it uses (termwise freeness, Section 2.1) and the degree conventions;\n'
    '  - verify every hypothesis of Proposition 3.10 on the counterexample, and the impossibility of the lift, by hand and\n'
    '    by a program of your own;\n'
    '  - determine which results of that paper use Proposition 3.10, Theorem 3.15 included, and whether the counterexample\n'
    '    reaches them;\n'
    '  - determine the hypothesis under which the lifting of Proposition 3.10 holds (an acyclic or cofibrant one, for\n'
    '    instance), and prove that corrected statement.\n'
    '  The item is done when the refutation is confirmed with these locators and the corrected statement is proved, or\n'
    '  when the refutation is shown wrong at an exact step. Record the check under the statement id D-031 in\n'
    '  CHECK_EVENTS.tsv.\n\n'
    '## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)\n\n'
    '- A. Caradot and Z. Lin, "Differential graded algebras with divided powers and homotopy Lie algebras",\n'
    '  arXiv:2511.22614v4: Section 2.1, Proposition 3.10, Theorem 3.15, and every result that uses Proposition 3.10 (B).\n'
    '- For A: the works that RESEARCH_SA08 cites in its sections, listed in `SA08/RESEARCH_SA08_references.bib` with that\n'
    '  run\'s notes on which it opened; G. Horel, "Binomial rings and homotopy theory"; M. Mandell, "Cochains and homotopy\n'
    '  type", Publ. Math. IHÉS 103 (2006); SGA 4, exposé V (flasque sheaves).\n\n')

prompt = HEAD + OUTCOME + ITEMS + RULES + DELIVER
open(OUT + 'PROMPT.md', 'w', encoding='utf-8', newline='').write(prompt)
print('sections', len(secs), secs)
print('rows SA08', len(rows8), '; check events', len(ce8) - 1, '; SA09 rows', len(rows9))
print('zip', ZIPNAME, len(buf.getvalue()), 'bytes,', len(members) + 1, 'members; PROMPT.md words', len(prompt.split()))
