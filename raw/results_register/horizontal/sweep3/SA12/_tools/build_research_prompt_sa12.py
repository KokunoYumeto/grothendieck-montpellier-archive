# Build a research prompt folder for GPT-6 Astra (ChatGPT Pro mode) from a topic's sweep-3 files (agent a6d42bf6, 19 Nov 2026).
# Copied and adapted for SA12 by the SA12 lead a65dbdc241d1a129a (Claude Opus 5.5 at effort max), 19 Nov 2026.
# usage: python -I -B build_research_prompt.py SA10|SA11|SA21
# Reads research_prompts/RESEARCH_<topic>_body.md (hand-written: title, attached files, sources, results, leads, the Parts)
# with the markers {{OUTCOME}}, {{RULES}}, {{DELIVER}}; fills them with the standard paragraphs taken from
# claude_tools/push_rule_pro_prompts.py (PUSH, THREE_HOUR) and claude_tools/prompts/checkpoint_rule.py (clause, FAILURE);
# writes TO_SEND/11_Finish_prompts/RESEARCH_<topic>/PROMPT.md and the background ZIP(s) listed in BUNDLES; runs both lints.
import glob, importlib.util, io, os, re, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents'
H = D + '/results_register/horizontal'
T = H + '/sweep3/SA12/_tools'
def mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
LINT = D + '/claude_tools/push_rule_pro_prompts.py'
pr = mod('pr', LINT); ck = mod('ck', D + '/claude_tools/prompts/checkpoint_rule.py')
topic = sys.argv[1]; NAME = 'RESEARCH_' + topic
OUT = D + '/pro_prompt_builds/' + NAME          # 19 Nov ~02:4x UTC (main session): builds go here, never into TO_SEND
WORK = OUT + '_work'
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
import hashlib, datetime

OUTCOME = pr.PUSH.strip() + '\n\n' + pr.THREE_HOUR.strip() + '\n\n' + f'''What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for every dimension
proved in low dimension without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made
and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `{NAME}_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.'''

RULES = '''## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the axioms assumed, the class of structures, finiteness and dimension
   hypotheses). Do not replace it by a convenient special case. If you prove a special case, name it as one and keep
   the general statement on your list.
2. Type every map and relation you introduce: source, target, the category or ordered set in which it lives, and each
   extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "refine to") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism; equivalence of categories or of topoi; an
   isomorphism of group schemes against a bijection on points or on tangent spaces; a homeomorphism against an
   isomorphism of schemes; topological finite generation against finite presentation.
5. Check the edge cases in scope: l = 2 with real points or orderable residue fields; l equal to a residue
   characteristic, and l nilpotent; characteristic 0 against characteristic p; non-reduced, non-normal and
   non-quasi-excellent noetherian bases; dimension 0, 1 and 2; non-separated and non-quasi-compact schemes; torsion
   sheaves that are not constructible; group schemes that are not smooth (alpha_p, mu_p) or not reduced.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.'''

DELIVER = f'''## What to deliver

One ZIP containing:
- `{NAME}_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `{NAME}_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `{NAME}_references.bib`: each entry marked opened / not opened.
- `{NAME}_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
  statement number); then what you read, what you computed (every program with its scope, counts and run time), and
  every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's check events carry ids such as MPL_31_002-051 (31:23) or codex K31-02 (31:85), and its items ids such as SA12-39; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

{ck.FAILURE}

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

{ck.clause(NAME)} Keep every checkpoint ZIP, and the final ZIP, under 500 MB.'''

body = io.open(T + f'/research_prompts/{NAME}_body.md', encoding='utf-8').read()
for k, v in (('{{OUTCOME}}', OUTCOME), ('{{RULES}}', RULES), ('{{DELIVER}}', DELIVER)):
    assert k in body, k; body = body.replace(k, v)
io.open(OUT + '/PROMPT.md', 'w', encoding='utf-8', newline='\n').write(body)

# background ZIP(s): BUNDLES[topic] = list of (zip name suffix, [(arcname prefix, glob pattern or file)])
S3 = H + '/sweep3/' + topic
def topic_files():
    out = [('study/' + os.path.basename(p), p) for p in sorted(glob.glob(S3 + '/*.md') + glob.glob(S3 + '/*.tsv')) if not os.path.basename(p).startswith('TASK_STATE')]
    out += [('study/readings/' + os.path.basename(p), p) for p in sorted(glob.glob(S3 + '/readings/*')) if os.path.isfile(p)]
    out += [('study/sweep2_WHAT_IS_WHERE.md', H + '/sweep2/' + topic + '/WHAT_IS_WHERE.md')]
    return out
spec = mod('spec', T + f'/research_prompts/{NAME}_files.py')
zips = {'study': topic_files()}
# the broad layer (memory broad-context-for-pro-notes): the neighbouring topics SGA, Picard, crystals, descent, EGA
broad = []
for other in ('SA13', 'SA14', 'SA15', 'SA17', 'SA23'):
    if other == topic: continue
    for fn in ('STUDY.md', 'HUNCHES.md', 'RESEARCH_PACKAGES.md'):
        broad.append((f'broad/{other}/{fn}', H + f'/sweep3/{other}/{fn}'))
zips['broad'] = broad
for zname, items in spec.ZIPS.items():
    zips.setdefault(zname, []).extend(items)
sizes = []
for zname, items in zips.items():
    zp = OUT + f'/{NAME}_{zname}.zip'
    seen = set(); man = ['path\torigin\tsha256']
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED) as z:
        for arc, p in items:
            if arc in seen or not os.path.isfile(p): continue
            seen.add(arc); z.write(p, arc)
            man.append('%s\t%s\t%s' % (arc, p.replace(D, 'Documents'), hashlib.sha256(open(p, 'rb').read()).hexdigest()))
        z.writestr('MANIFEST.tsv', '\n'.join(man) + '\n')
    sizes.append((os.path.basename(zp), len(seen), os.path.getsize(zp)))
    print(os.path.basename(zp), len(seen), 'files', round(os.path.getsize(zp) / 1e6, 2), 'MB')
    assert os.path.getsize(zp) < 10_000_000, 'over the 10 MB upload limit'
r1 = subprocess.run([sys.executable, '-I', '-B', LINT, '--lint-math', OUT + '/PROMPT.md'], capture_output=True, text=True)
r2 = subprocess.run([sys.executable, '-I', '-B', D + '/claude_tools/paper_completeness_lint.py', OUT + '/PROMPT.md'], capture_output=True, text=True)
print('lint-math:', r1.stdout.strip().splitlines()[-1] if r1.stdout.strip() else r1.stderr[-400:])
print(r1.stdout.strip()[:1500] if r1.returncode else '')
print('paper lint:', (r2.stdout.strip() or r2.stderr.strip())[-1500:])
print('PROMPT.md words:', len(body.split()))
files = sorted(os.listdir(OUT)); assert len(files) <= 20 and all(os.path.isfile(OUT + '/' + f) for f in files)
lint1 = (r1.stdout.strip().splitlines() or ['?'])[-1]; lint2 = (r2.stdout.strip().splitlines() or ['?'])[-1]
readme = f'''# {NAME}: research prompt for GPT-6 Astra (ChatGPT Pro mode)

Built {datetime.datetime.utcnow():%Y-%m-%d %H:%M} UTC by Claude Opus 5.5 at effort max (agent a65dbdc241d1a129a, the lead of SA12
in sweep 3, wave 1), at the main session's word (19 Nov 2026), from `results_register/horizontal/sweep3/{topic}/` and the
builder `results_register/horizontal/sweep3/SA12/_tools/build_research_prompt_sa12.py` (adapted from agent a6d42bf6's).

- **What it is:** {body.splitlines()[0].lstrip('# ').strip()}
- **Account:** the one the main session assigns (Pro hours were left on account 4 when it was built).
- **What to send:** all {len(files)} files of `pro_prompt_builds/{NAME}/`, no text.
- **Lint:** `push_rule_pro_prompts.py --lint-math`: {lint1}; `paper_completeness_lint.py`: {lint2}.
- **Sizes:** PROMPT.md {os.path.getsize(OUT + '/PROMPT.md'):,} bytes ({len(body.split()):,} words); ''' + '; '.join(f'{n} {k} files, {s/1e6:.2f} MB' for n, k, s in sizes) + '''.
- **ZIPs:** LaTeX and text only; each has `MANIFEST.tsv` at its root (path, origin, SHA256).
'''
open(D + f'/pro_prompt_builds/{NAME}.README.md', 'w', encoding='utf-8', newline='\n').write(readme)
print('README written; folder files:', len(files))
