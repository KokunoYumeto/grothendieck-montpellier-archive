"""Consolidate the last checked results; mark final only after the binding review."""
from pathlib import Path
import argparse, csv, json, runpy, sys

parser=argparse.ArgumentParser()
parser.add_argument('--final',action='store_true')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
saved_argv=sys.argv
sys.argv=[str(root/'code/update_report_06.py')]
runpy.run_path(str(root/'code/update_report_06.py'),run_name='__main__')
sys.argv=saved_argv
path=root/'RESEARCH_SA08_report.md'
text=path.read_text()
lines=text.splitlines()
for i,line in enumerate(lines):
    if line.startswith('| C.3 |'):
        lines[i]=('| C.3 | Not fully settled; finite-prime case proved | '
          'C17 proves common sources and terminal localization for finitely many noninvertible rational primes. C30, C32 and C34 give sufficient local-completion constructions for arbitrary k; C34 retains only finite form truncations, but their admissible completions are unconstructed. Z remains the smallest unsettled base. C31 and C35 refute the specified extension shortcuts; C33 limits a proposed operation invariant. |')
text='\n'.join(lines)+'\n'

source_marker='## Computation record'
source='''The final source checks opened Serre's 1953 primary paper at ChapterI Section6.1, printed p264, and ChapterII Section6 Proposition8, p271; C33 uses its finite-generation statement with the explicit Künneth and universal-coefficient reduction. The replacement-theorem search also opened Menichi, Section7 and Proposition8.3; Scott's proof of Anick's theorem and Theorem1.1; Scheerer–Tanré, pp376–377 and Construction2.2/Proposition2.4; Hanke, Section3 and Definition4.1/Theorem4.6; Brantner–Campos–Nuiten, Propositions4.31 and5.16 and Theorems4.33,4.35,5.20 in the inspected author manuscript; and Fresse, Section0.11. Their different arrow directions, coefficient conventions, algebraic categories, connectedness assumptions and degree ranges are recorded in the source notes. None supplies the required classical strict local completion. Unlocated or blocked texts, including Halperin's unpublished notes, were not used as theorems. All added bibliography entries identify their actual opened scope.

'''
if source not in text:text=text.replace(source_marker,source+source_marker)

marker='Source download, source inspection, OCR, registry consolidation, and packaging scripts are also retained.'
extra='''Further checked work after checkpoint06:

- D006E received a fresh adversarial audit of the exact unbounded adjunctions, tensor-ideal localization, coherent algebra cone and homotopy-limit comparison. Its new explanatory paragraph checks the factor-two colax comparison for coefficient extraction and distinguishes recovered higher operations from forgetting the weights. A001–A013 were also reread directly, including the arbitrary-base and complete-topology arguments. These are proof checks, not new numerical experiments.
- B_fetch_serre1953.py retrieved and identified one primary PDF, 767,254 bytes, with a SHA256 receipt and 10.171391 seconds recorded. The complete publication is excluded from the ZIP; the inspected locators and retrieval record are retained.
- B_fetch_relative_literature.py's retained final pass checked five source requests: three already-downloaded primary PDFs were hash-validated, Hanke's PDF was downloaded, and the Anick publisher request returned403. Per-request times and hashes are recorded in B_relative_literature_fetch.json; the already-downloaded checks are not represented as fresh download timings.

'''
counter=root/'logs/C_rational_saturation_countercheck.json'
if counter.exists():
    data=json.loads(counter.read_text())
    elapsed=next((data[k] for k in ('runtime_seconds','elapsed_seconds','seconds') if k in data),None)
    extra+=('- C_rational_saturation_countercheck.py: 85 exact monomials and 743 Leibniz pairs, with the coefficient certificate for the p=2, weight-two rational-saturation obstruction of C35; '
            +(f'{elapsed:.6f} seconds. ' if elapsed is not None else 'The elapsed time is recorded in the receipt. ')
            +'The full output gives the basis, odd product, doubled-image calculation and finite residue check. It refutes that rational-saturation extension, not C3.\n\n')
if 'Further checked work after checkpoint06:' in text:
    a=text.index('Further checked work after checkpoint06:');b=text.index(marker,a)
    text=text[:a]+extra+text[b:]
else:text=text.replace(marker,extra+marker)

gate_marker='The outstanding constructive task is therefore'
a=text.index(gate_marker)
b=text.index('\n\nL7:',a)
end='''C33 proves the precise moving-prime module example and shows that the localizing shadow quotient erases it. A fixed finitely generated ordinary operation group is detected by finitely many primes, so it cannot supply the sought moving-prime invariant under the stated localization and naturality hypotheses. No admissible counterexample is extracted from that module example.

C34 proves a genuine weakening of C32's sufficient data: at each prime only the finite form truncation of P and its map to the target must be retained. The higher relations and higher map values of P may be discarded. An independent rational elementary source and a two-edge simplicial path replace the missing full map. The local object must nevertheless be a full admissible theory in every weight and simplex, and the agreement depths must tend to infinity with the prime. Neither existence nor necessity of those completions is proved, and no new coefficient case of C3 follows.

C35 refutes a different proposed shortcut, adjoining rational halves of products of odd parameters. The counterexample uses the standard admissible target over Z_(2), an acyclic parameter row in weight two and an acyclic output row in weight four. A specified product is an integral basis monomial, so it has no required half. This verifies a failed universal extension construction even in those stable rows; it is not a counterexample to global uniqueness.

The remaining original assertion is still common-source existence and terminal localization over rings with infinitely many noninvertible rational primes. The smallest unsettled base is Z. The next constructive step would be to prove a local finite-form completion theorem satisfying C34, with actual target maps and uniform bounds, or to find an invariant of admissible theories that yields a counterexample. The attempted primitive attachments, brutal high-tail cones, image quotients, naive cancellation, ordinary pushouts, fixed primary-operation invariants and cited replacement theorems all have their precise failure or missing hypothesis recorded. None is presented as an actual obstruction to C3 unless its statement expressly says so.

The formal no-movement count is one after the09:21 review. The10:21 review must apply the user's rule to the original questions; these weaker sufficient constructions are not automatically counted as a strictly smaller main-question gate.'''
text=text[:a]+end+text[b:]
text=text.replace('C29 proves a relative extension theorem under its stated dimension bound.',
 'C29 proves a relative extension theorem under its stated dimension bound. C36 proves its arbitrary-base extension and the sharper absolute n≤pq and relative n<pq ranges over every Z_(p)-algebra, using derived scalar extension of the universal degreewise-free arity complexes. These remain finite-arity statements; the relative case retains the entire prescribed boundary.')

qa_start=text.index('## Typesetting status')
qa_end=text.index('## Proved obstructions, approaches and remaining gates',qa_start)
qa=text[qa_start:qa_end]
qa=qa.replace('The approved current LuaLaTeX build has ',
              'Build37 introduced a 6.2839 pt overflow in the revised abstract; its opening sentence was shortened, and that location was added to the inspection anchors. The approved current LuaLaTeX build has ')
qa=qa.replace('The approved current LuaLaTeX build has ', 'The final provenance edit clarifies that original scan images were inspected while their retrieval records, rather than the scans themselves, accompany the archive. The final page renderings were compared with the preceding explicitly inspected set; the changed documentary page was inspected again. The approved current LuaLaTeX build has ')
text=text[:qa_start]+qa+text[qa_end:]
text=text.replace("Dokas–Frankland–Ikonicoff's primary arXiv source", "Dokas–Frankland–Ikonicoff's primary arXiv paper")

if args.final:
    review=json.loads((root/'logs/PROGRESS_REVIEW_03.json').read_text())
    if review.get('consecutive_no_movement')!=2 or not review.get('stop_required'):
        raise RuntimeError('Finalization requires the completed binding second no-movement review.')
    text=text.replace('This is a working checkpoint, not a completed return. Proofs being consolidated in the paper are also retained in full in notes/.',
       'This final package is INCOMPLETE. The10:21 UTC review was the second consecutive formal review without qualifying movement, so the requested stop rule was applied. C.3 and L7 remain undecided; their exact states and the work that would be needed next are retained. Full proof notes, failed routes and check records are included.')
    text=text.replace('The formal no-movement count is one after the09:21 review. The10:21 review must apply the user\'s rule to the original questions; these weaker sufficient constructions are not automatically counted as a strictly smaller main-question gate.',
       'The formal10:21 review found no qualifying movement since09:21. C30–C35 establish conditional constructions and precise failures of proposed methods, but do not close either requested open row or prove a demonstrably strictly smaller original C3 gate. The count reached two consecutive no-movement reviews, and investigation stopped as required. This package remains INCOMPLETE; no conjecture is presented as settled by the stop rule.')
    text=text.replace('# RESEARCH_SA08 working report','# RESEARCH_SA08 final report — incomplete')
    text=text.replace('Further requested bibliography is still being fetched and checked; no unopened work is treated as an opened proof.',
       'The source-access record identifies the requested works that could be opened and those that remained unavailable; no unopened work is treated as an opened proof.')
    inventory=root/'notes/OPERATIONAL_PROGRAMS.md'
    if not inventory.exists():
        raise RuntimeError('The operational-program inventory must be included in the final report.')
    marker='## Corrections to the supplied materials'
    if '## Operational program record' in text:
        a=text.index('## Operational program record');b=text.index(marker,a)
        text=text[:a]+text[b:]
    inventory_text=inventory.read_text()
    if inventory_text.startswith('# '):
        inventory_text=inventory_text.split('\n',1)[1].lstrip()
    text=text.replace(marker,'## Operational program record\n\n'+inventory_text+'\n\n'+marker)
    for before,after in [('the10:21','the 10:21'),('formal10:21','formal 10:21'),('since09:21','since 09:21'),('the09:21','the 09:21'),('checkpoint06','checkpoint 06'),('The10:21','The 10:21')]:
        text=text.replace(before,after)
path.write_text(text)
print(json.dumps({'final':args.final,'report':path.name,
 'statement_rows':len(list(csv.DictReader((root/'RESEARCH_SA08_results.csv').open()))),
 'check_events':len(list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))),
 'remaining_requested_rows':['C.3','L7']},indent=2))
