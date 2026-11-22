from pathlib import Path
from datetime import datetime, timezone
import csv

root = Path('/workspace/scratch/6b22741c5cd2/RESEARCH_SA20')
own = root / 'agents/singularities_duality'
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
draft = (own / 'logs/A137_base_four_component_image_draft.tex').read_text()
assert 'Two lifts of the same endpoint isotopy' in draft
assert 'Apply the common-collar normalization to this' in draft
part = own / 'part_base_four_component_image.tex'
assert not part.exists()
part.write_text('% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n'
                '\\subsection{The full component image, with its endpoint condition retained}\n\n'
                + draft[draft.index(r'\begin{saresult}'):])

with (own / 'results.csv').open('a', newline='') as f:
    csv.writer(f).writerow([
        'A.137',
        'For closed real PL4 base the image on concordance components is the kernel of a relative KS homomorphism from the endpoint-PL-image subgroup to H2(B;Z2)/image(pi0 beta)',
        'Proved under stated hypotheses',
        'agents/singularities_duality/part_base_four_component_image.tex A.137',
        'A.135; A.136; KS1977 EssayV relative1.5 p229;3.2 pp240-241;5.6 pp252-253',
        '119/148; 121/002-003; A.1(b); Lead L1',
        'Complete necessary-and-sufficient component-image criterion, with ordinary four-dimensional endpoint image and beta image unevaluated. The quotient inside the endpoint-image subgroup is finite elementary abelian2 of order at most2^b2. No surjectivity of lambda or full main-row closure.'
    ])
rows = [
    ('A.137', 'singularities_duality', 'complete proof and source-scope audit',
     'PASS: relative structure zero-test with entire boundary PL; affine KS action trivial by exact cohomology sequence; explicit ordinary endpoint traces; arbitrary lift independence; fixed-boundary Q family; exact kernel and finite elementary2 quotient. No smooth4 comparison used.'),
    ('A.137', 'root', 'independent complete proof audit received',
     'FULL PASS of updated complete draft: relative orbit zero-test, affine KS rule and trivial action, explicit E/Q paths, lift independence, exact kernel, finite quotient; no source gap or unwarranted surjectivity. Promotion authorized before checkpoint13 freeze.'),
    ('A.137', 'higher_comparison2', 'independent complete proof audit received',
     'FULL PASS, both minor explicitness repairs incorporated. Audit at agents/higher_comparison/A137_independent_audit.md; verifies endpoint choices, KS cocycle, all beta values as traces, subgroup homomorphism, and finite quotient.'),
    ('A.1(b)', 'singularities_duality', 'original-source scope audit',
     'Opened OPR current40-page author PDF; visually checked printed9-10 and official Crelle accepted31October2026 metadata. Fixed-entire-boundary smooth criterion and block Q convention retained. GN Remark1.7p4/3.13p20 explicitly deny complete TOP4 two-invariant classification. See logs/OPR_2026_and_GN_scope_audit.md.')
]
with (own / 'checks.tsv').open('a') as f:
    for sid, who, kind, outcome in rows:
        f.write('\t'.join([sid, now, who, kind, outcome]) + '\n')

bib = own / 'references.bib'
b = bib.read_text()
assert 'OrsonPowellRandalWilliams2026' not in b
b += r'''

@unpublished{OrsonPowellRandalWilliams2026,
 author={Orson, Patrick and Powell, Mark and Randal-Williams, Oscar},
 title={Smoothing topological pseudo-isotopies of 4-manifolds},
 year={2026},
 eprint={2507.16984},
 archivePrefix={arXiv},
 url={https://www.maths.gla.ac.uk/~mpowell/smoothing_pseudo_isotopies.pdf},
 note={OPENED: current full public author PDF,40pages,645923bytes. Printedpp9--10 visually inspected; TheoremB p2, Lemma3.2 pp7--9, Lemma3.3 p9 and Theorem3.5 p10 read. The zero-obstruction isotopy is relative to the entire boundary with smooth endpoint maps; Section2 uses block spaces and does not compute ordinary concordance components. Official Glasgow record397578 independently opened: accepted by Crelle on31October2026; no final volume or pages claimed. Small source correction: p10 F composed with inverse(f0 times id) has top f1 composed with inverse(f0), although the next sentence drops that inverse. Accessed2026-11-19.}
}
'''
bib.write_text(b)
with (own / 'report.md').open('a') as f:
    f.write(f'''\n## {now} — A.137: complete component-image criterion, unresolved inputs retained\n\nFor closed real PL four-manifolds, A.137 now complements A.136's based-fibre model with a necessary-and-sufficient criterion for the image on ordinary concordance components. First the top map must be TOP-isotopic to a PL map. After choosing that endpoint isotopy, the boundary-PL cylinder has a relative Kirby--Siebenmann class in H2(B;Z2). Its class modulo the image of pi0 beta is independent of all endpoint choices and of the free-top concordance component. It defines a homomorphism on the subgroup of components satisfying the endpoint condition, and its kernel is exactly the PL image.\n\nIn particular the PL image is normal inside that endpoint subgroup and their quotient embeds in H2(B;Z2)/image(pi0 beta). This quotient is a finite elementary abelian2 group, of order at most2^b2. No surjectivity to that cohomology quotient is asserted. The exact ordinary automorphism endpoint-image predicate and the beta image remain unevaluated in general; this does not complete original A1(b). The proof uses ambient five-dimensional relative PL structures only after both boundary maps are PL, and supplies explicit ordinary endpoint traces and fixed-boundary path corrections. Root and the independent higher-comparison reviewer both passed the full proof.\n\nThe fresh OPR accepted2026 source and GN original were audited separately in logs/OPR_2026_and_GN_scope_audit.md. OPR's smooth zero-obstruction statement requires the entire boundary already smooth. GN expressly retains a kernel of double suspension invisible to its two invariants. Neither is silently converted into a complete ordinary TOP4 concordance computation.\n''')
(own / 'logs/A137_promotion_receipt.txt').write_text(
    now + '\nPromoted after root and independent full audit.\n'
    'New part: agents/singularities_duality/part_base_four_component_image.tex\n'
    'Updated own references.bib/results.csv/checks.tsv/report.md. Root should input afterA136.\n')
print(now)
