#!/usr/bin/env python3
"""Idempotent integration of completed, refereed results before checkpoint07."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
p = root / 'RESEARCH_SA08_C3_D031_paper.tex'
s = p.read_text()
for anchor, new in [
    ('A_uniform_tail_reduction', 'A_single_disk_gate'),
    ('B_bounded_free_flatness', 'B_tensor_boundary_defect'),
    ('B_tensor_boundary_defect', 'B_flat_boundary_extension'),
    ('B_complete_relative', 'A_hadamard_image'),
    ('A_weight_frobenius_saturation', 'A_all_weight_frobenius'),
    ('A_deep_tail_H2', 'B_saturated_tail_nonflat'),
    ('A_closed_boundary_cells', 'A_integral_period_transfer'),
    ('A_integral_period_transfer', 'A_prime_transfer'),
    ('A_prime_transfer', 'B_partial_source_tensor'),
    ('B_partial_source_tensor', 'A_single_cell_cleanup'),
    ('A_single_cell_cleanup', 'A_mixed_cell_cleanup'),
]:
    line = '\\input{sections/' + new + '}'
    assert (root / 'sections' / (new + '.tex')).exists(), new
    if line not in s:
        old = '\\input{sections/' + anchor + '}'
        assert old in s, anchor
        s = s.replace(old, old + '\n' + line)
p.write_text(s)

p = root / 'sections/A_prime_transfer.tex'
s = p.read_text().replace('144 exact checks', '150 exact checks').replace('0.097051051', '0.104388505')
p.write_text(s)

p = root / 'notes/A_root_CHECK_EVENTS.tsv'
with p.open(newline='') as f:
    old_events = list(csv.DictReader(f, delimiter='\t'))
new_events = [
    ('A-L16', 'targeted proof check', 'Read full proof: split constants, exact boundary sequences, lower-degree tensor exactness and precise top-degree Tor term; actual multiplication-by-T counterexample verified.'),
    ('A-L17', 'targeted proof check', 'Checked AT23 strict disk change, all-simplex H1-H3 vanishing, complete low arity calculation and actual mod2 H3 generator; finite150-check certificate read.'),
    ('A-L18', 'targeted proof check', 'Read full proof and opened Herscovich-Rey primary source after Lemma2.1 p4; verified bounded-below graded flat implies free argument, then exact fiber and boundary comparisons.'),
    ('A-L19', 'targeted proof check', 'Full proof read: arity-one minimum lattice RC survives all based saturation stages; C modp is nonzero, killed by T^(p-1), and outside T image; exact coefficient-module sequence gives actual nonflatness.'),
    ('AT22', 'targeted proof check', 'Full proof checked: integral coefficient resolution retaining named cycles, J identities, all-lift localized period invariance, exact mod2 localization isomorphism and explicit integral U,V primitive pair.'),
    ('AT23', 'targeted proof check', 'Full proof checked: typed integral PD change and inverse, complete odd/even disk cohomology, actual other-prime torsion, saturation fixedness and infinite partial family; no completed-source claim.'),
    ('A-S09-26', 'targeted proof check', 'Checked strict Hadamard maps and coefficient factorials, rational monomial injection and integral strict image isomorphism, full based closure in larger ambient rational algebra, and row-zero Tor witness.'),
    ('A-WF02', 'targeted proof check', 'Full proof checked19:44UTC: identity on Z_p by all residue quotients, common coefficient c in pR, cancellation in S, explicit integral b_r, F^r injectivity and zero image in every completion quotient.'),
    ('A-S09-27', 'targeted proof check', 'Full proof checked19:44:49UTC against A004: d+2 graph/pullback bounds, literal low-weight coefficient pieces, both internal-source implications, support/flatness and infinite-rank versus rank-one properness witness.'),
    ('AT24', 'targeted proof check', 'Full proof and precision additions checked19:51UTC: actual free source carrier, old-x correction, low arity complexes, first-skeleton retract, homogeneous saturation in simplex2, normalized repair primitives, fixed-cutoff union and exact scope of horizontal restoration.'),
    ('AT25', 'targeted proof check', 'Full mixed-family proof checked19:51UTC: simultaneous free carrier, exact cross matrix (1,-1),(1,1), diagonal injections, form(b)<arity face normalization and torsionfree conclusion for z, common cutoff and homogeneous saturation. Higher-simplex vertical comparison remains unproved.'),
]
known = {(x['statement_id'], x['type'], x['outcome']) for x in old_events}
with p.open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for sid, typ, outcome in new_events:
        if (sid, typ, outcome) not in known:
            w.writerow([sid, '2026-11-19', 'GPT-6 Astra (OpenAI), Pro mode, RESEARCH_SA08_C3_D031/root', typ, outcome])

p = root / 'RESEARCH_SA08_C3_D031_report.md'
s = p.read_text()
s = s.replace('A-S09-24 reduces this exactly to sources and targets internal to C^[d]: free first skeleton and global coefficient exactness through any fixed finite degree d. That restricted assertion remains undecided.', 'A-S09-27 reduces this exactly to sources and targets internal to the proper smaller class E^[d]: one first-skeleton disk per weight from a cutoff N, global coefficient exactness through d, and rows through d+2 exact from N. The target pair can share N; the source has its own cutoff. This restricted assertion remains undecided.')
s = s.replace('144 exact assertions for p=2,3,5 and arities0–8; integral PD change and inverse, chain identities, complete H4 Smith matrices | 0.09705105099419598', '150 exact assertions for p=2,3,5 and arities0–8; integral PD change and inverse, chain identities, complete H4 Smith matrices and mod2 H3/H4 ranks | 0.10438850500213448')
rows = [
    '| A: single-disk internal common-source gate | Proved | A-S09-27 gives the proper restriction E^[d] of C^[d], actual target replacements with one common P(N), internal source replacement, and an explicit infinite-rank properness witness. |',
    '| A: tensor exactness at the last comparison degree | Proved with exact defect | A-L16 identifies the top group as Tor1 of the next cokernel; A-L17 realizes nonzero mod2 H3 in an actual partial PD source. |',
    '| A: flat-term extension of boundary flatness | Proved | A-L18 extends the exact boundary and tensor results to bounded-below termwise S-flat complexes; A-L19 proves the specified fully saturated resolved-tail zero-form module is not S-flat. |',
    '| A: integral quadratic period repair | Proved | AT22 constructs the integral coefficient resolution and actual primitive pair; localization modulo2 transfers the checked zero residue back to Z with its stated bounds. |',
    '| A: prime transfer in a two-cell repair | Proved | AT23 gives an actual integral PD change and computes torsion at every other prime, including unbounded degree-four defects in the specified partial family. |',
    '| A: Hadamard image and full based closure | Refuted as the stated common-target repair | A-S09-26 identifies the strict image with G tensor_S G and proves its full based closure is unchanged, retaining the exact prime-power horizontal Tor. |',
    '| A: all weight-preserving Dieudonne Frobenii | Refuted as completed admissible replacements in the stated setting | A-WF02 proves that every such F over Z, Z_(p) or Z_p kills all original positive-weight coefficients under the actual saturation-completion map. |',
    '| A: iterative low-degree cleanup in simplex two | Proved in its stated source class | AT24–25 construct actual carriers, simultaneous repairs and full based saturation for one cell and for a family of free C21 cells over Z_(2), giving global-weight comparison through degree three in simplex two. Higher-simplex vertical exactness and stability under later degree-four repairs remain unproved. |',
]
anchor = '| B: exact v4 statement and conventions |'
pos = s.index(anchor)
for row in rows:
    if row not in s:
        s = s[:pos] + row + '\n' + s[pos:]
        pos += len(row) + 1
p.write_text(s)

p = root / 'sections/A_unresolved.tex'
s = p.read_text()
old = '''The strongest proved reduction is now A-S09-24.  For each fixed
$d\\geq0$, both source and targets may be taken in the proper full
subcategory $\\mathcal C^{[d]}$, with vertical coefficient comparison
through degree $d$ in every weight and simplex.  The proof supplies
the actual weight-tail maps, the functors $R T_N$, and a finite-word
comparison proving equivalence of the all-arrow localizations.
This is a reduction for every fixed finite $d$; no object exact
in every degree is produced by an infinite iteration.'''
new = '''The strongest proved common-source reduction is A-S09-27.
For each fixed $d\\geq0$, source and targets may be taken in the
proper full subcategory $\\mathcal E^{[d]}\\subset\\mathcal C^{[d]}$.
Its first skeleton is the specified $P(N)$ with one disk in every
weight at least $N$; its coefficient comparison holds through $d$
in every weight, and its rows through $d+2$ are exact from $N$.
The two targets can have the same $N$, while the internal source
has its own cutoff. All replacement arrows and both directions
are explicit. This internal common-source assertion remains open.
The terminal-localization gate remains A-S09-24, with the actual
functors $R T_N$ and its finite-word localization comparison.
Each reduction concerns a fixed finite $d$; no single object exact
in every degree is produced by these comparisons.'''
if old in s:
    s = s.replace(old, new)
else:
    assert 'strongest proved common-source reduction is A-S09-27' in s
p.write_text(s)
