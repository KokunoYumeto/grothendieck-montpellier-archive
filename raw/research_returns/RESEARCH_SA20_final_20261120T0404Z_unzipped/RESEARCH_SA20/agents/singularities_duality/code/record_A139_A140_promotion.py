from pathlib import Path
from datetime import datetime, timezone
import csv
import json

root = Path('/workspace/scratch/6b22741c5cd2/RESEARCH_SA20')
own = root / 'agents/singularities_duality'
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
specs = [
    ('A139_TOP_sphere_stabilization_draft.tex',
     'part_TOP_sphere_stabilization.tex',
     'The ordinary TOP sphere space and finite-rank stabilization'),
    ('A140_OPR_obstruction_realization_draft.tex',
     'part_four_obstruction_realization.tex',
     'Realizing the four-dimensional component obstruction')
]
for draftname, partname, heading in specs:
    source = (own / 'logs' / draftname).read_text()
    assert source.count(r'\begin{proof}') == source.count(r'\end{proof}') == 1
    assert source.count(r'\begin{saresult}') == source.count(r'\end{saresult}') == 1
    target = own / partname
    assert not target.exists(), target
    target.write_text('% AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n'
                      + r'\subsection{' + heading + '}\n\n'
                      + source[source.index(r'\begin{saresult}'):])

with (own / 'results.csv').open('a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([
        'A.139',
        'Ordinary TOP concordances of S^n are the based fibre of actual finite-rank stabilization Y_n to Y_(n+1); PL and TOP S4 concordance groups vanish in degrees0 through3',
        'Proved under stated hypotheses',
        'agents/singularities_duality/part_TOP_sphere_stabilization.tex A.139',
        'A.128; A.132; KL1966I Lemma3 pp11-13; Salvatore-Turchin2026 Section3.4; KS1977 V5.5 p251; GGHKP2026 Theorem1.3',
        '119/148; 121/002-003; A.1(b); Lead L1',
        'n>=2; global compact-open TOP groups and zero-section-fixing common-parameter germs. Actual stabilization map identified by ray translation and equivariant coordinate isotopy. No pi4 vanishing or general low-dimensional computation.'
    ])
    writer.writerow([
        'A.140',
        'OPR quadratic-assembly hypothesis realizes the Bockstein-kernel part of the component obstruction; no2torsion gives the exact quotient, and simply connected PL4 bases have connected ordinary TOP concordance space and J_B=H2(B;Z2)',
        'Proved under stated hypotheses',
        'agents/singularities_duality/part_four_obstruction_realization.tex A.140',
        'A.136; A.137; OPR2026 Theorem2.3(D) p6 and Definition5.8 pp21-22; KS1977 I p39,V5.6; GGHKP2026 Theorem1.5',
        '119/148; 121/002-003; A.1(b); Lead L1',
        'Closed connected oriented real PL4. Source Ls/Lq notation discrepancy made explicit; actual quadratic Definition5.8 used. Ordinary TOP loops surject onto H2 and PL loops vanish, so base automorphism pi1 comparison fails for S2xS2. No PL concordance-component or smooth-isotopy conclusion. Finite base1465 checks PASS.'
    ])

root_cert = json.loads((root / 'logs/check_A140_product_spheres.json').read_text())
author_cert = json.loads((own / 'logs/check_A140_product_spheres_author.json').read_text())
assert root_cert['checks'] == author_cert['checks'] == 1465
assert root_cert['failures'] == author_cert['failures'] == 0
events = [
    ('A.139', 'singularities_duality', 'complete proof and original-source audit',
     'PASS: common finite-parameter TOP globalization; global and spherical germ kernels; ordinary disk kernel with free outer face; orthogonal quotient; ray translation; exact stabilization coordinate calculation; safe S4 degrees0-3.'),
    ('A.139', 'root', 'independent complete proof audit received',
     'FULL PASS of numbered candidate, after reading KL1966I pp11-13 and Salvatore-Turchin2026 Section3.4; finite-rank and ordinary-family conventions retained. Promotion authorized.'),
    ('A.139', 'higher_comparison2', 'independent complete proof audit received',
     'FULL PASS at agents/higher_comparison/A139_independent_audit.md; explicit zero-section convention verified in final numbered candidate. Prior A132 E-K and finite-rank inputs are identified dependencies, not claimed newly reopened.'),
    ('A.140', 'singularities_duality', 'complete proof and source-notation audit',
     'PASS: triple relative KS connecting map proves class equality; smooth-G normalization makes both endpoints literally id; OPR block realization feeds lambda only; GGHKP ordinary paths yield actual loop traces; no smoothing of PL isotopies. Def5.8 quadratic Lq convention retained with exact printed Ls discrepancy explained.'),
    ('A.140', 'root', 'independent complete proof and source audit received',
     'FULL PASS subject to final notation and finite certificate; both completed. Root reopened OPR Definition5.8 pp21-22, exact theorem2.3(D), KS p39 and GGHKP1.5. Promotion authorized.'),
    ('A.140', 'higher_comparison2', 'independent complete proof audit received',
     'FULL PASS at agents/higher_comparison/A140_independent_audit.md; relative obstruction equality, explicit G normalization, general lambda range, and actual ordinary-loop surjection all verified. Finite certificate supplied separately by root.'),
    ('A.140', 'root', 'exact finite product-sphere certificate',
     f"PASS1465 checks,0 failures,{root_cert['elapsed_seconds']}s; code/check_A140_product_spheres.py and logs/check_A140_product_spheres.json. f=(16,84,216,240,96), Betti_mod2=(1,0,2,0,1), all96facets and all nonmaximal link homologies. Product PL type and pi1 established mathematically, not inferred from homology."),
    ('A.140', 'singularities_duality', 'independent program reading and saved rerun',
     f"PASS1465 checks,0 failures,{author_cert['elapsed_seconds']}s; own logs/check_A140_product_spheres_author.json. Read exact Fraction-free mod2 bit elimination, staircase construction, all boundaries and links; finite base only, not a computation of TOP loops."),
    ('C.U001', 'singularities_duality', 'fresh original-source retrieval attempt',
     '20:41UTC both-engine exact-title/PDF pass found only metadata/citing papers and no new observed public original URL. Own logs/C_original_retrieval_2041.md. Hartshorne1968 Prop4.3/Th7.5 original gate unchanged.'),
    ('C.U002', 'singularities_duality', 'fresh original-source retrieval attempt',
     '20:41UTC both-engine exact-title/PDF pass found only metadata/citing papers and no new observed public original URL. Own logs/C_original_retrieval_2041.md. Ogus1973 Section3 original gate unchanged.')
]
with (own / 'checks.tsv').open('a') as f:
    for sid, who, kind, outcome in events:
        f.write('\t'.join([sid, now, who, kind, outcome]) + '\n')

bib = own / 'references.bib'
b = bib.read_text()
assert 'KuiperLashof1966I,' not in b and 'SalvatoreTurchin2026,' not in b
b += '\n' + (own / 'logs/references_A139_pending.bib').read_text()
b = b.replace('Published online3March2026; independently checked',
              'Theorem1.5 and the bottom-plus-side definition also freshly reopened: the entire ordinary TOP pseudo-isotopy of every compact simply connected4-manifold is isotopic to identity relative to bottom and sides. Published online3March2026; independently checked')
b = b.replace('Official Glasgow record397578 independently opened:',
              'Theorem2.3(D) p6, Definition5.8 p21 and proofp22 freshly inspected for A.140: the theorem prints an Ls codomain, while the specified quadratic assembly definition and proof use Lq; A.140 uses the latter and explains the discrepancy. The block-loop realization is not treated as an ordinary loop without the separate simply connected theorem. Official Glasgow record397578 independently opened:')
bib.write_text(b)

with (own / 'report.md').open('a') as f:
    f.write(f'''\n## {now} — A.139 and A.140: finite-rank sphere model and four-dimensional realization\n\nA.139 identifies the whole ordinary TOP sphere concordance space with the based fibre of the actual finite-rank stabilization Y_n to Y_(n+1), for n at least2. Finite-family germ globalization is taken from the opened Kuiper--Lashof original; the map itself is identified by translation along the fixed cone ray and an orthogonally equivariant local coordinate isotopy. The safe S4 consequence is vanishing only in degrees0 through3, in both PL and TOP. This is a sphere model, not a replacement of the general remaining low-dimensional problem by stable groups.\n\nA.140 proves that the OPR six-dimensional invariant equals Poincare duality applied to the relative PL-structure difference, via the exact triple connecting map. Under the actual quadratic assembly hypothesis of Definition5.8, the block theorem realizes the Bockstein-kernel subgroup in the range of A.137's lambda. If first homology with Z_(2) coefficients has no2-torsion, lambda is onto and the previous injection is the exact quotient H2(B;Z2)/J_B. The ordinary endpoint-image predicate and J_B remain unevaluated in general. The printed theorem/definition Ls/Lq convention discrepancy is stated explicitly.\n\nFor a closed simply connected PL4 base, the corrected GGHKP full pseudo-isotopy theorem gives pi0 P_TOP=1. Combining it with the realization gives J_B=H2(B;Z2). More strongly, ordinary TOP automorphism loops surject onto this cohomology group through their cylinder traces, while PL loops map to zero. Thus Aut_PL to Aut_TOP is not pi1-surjective for S2xS2. This does not infer any smooth isotopy comparison or compute pi0 P_PL. The explicit finite S2xS2 model has f-vector(16,84,216,240,96) and mod2 Betti(1,0,2,0,1). Root's1465-check run took{root_cert['elapsed_seconds']}s; the saved independent author run took{author_cert['elapsed_seconds']}s. Product triangulation and simple connectivity are proved mathematically; the code checks finite combinatorics and homology, not the source-derived TOP loops.\n\nRoot and the independent higher-comparison agent passed both full proofs and original-source scope. The20:41 fresh Hartshorne/Ogus original-source retrieval pass did not change either remaining PartC access gate; its exact negative evidence is saved separately.\n''')

receipt = (now + '\nPromoted A.139 and A.140 after root and independent full audits.\n'
           'New parts: agents/singularities_duality/part_TOP_sphere_stabilization.tex\n'
           'agents/singularities_duality/part_four_obstruction_realization.tex\n'
           'Updated own results.csv/checks.tsv/references.bib/report.md.\n'
           'Root should include A139 after A138 and A140 after A139.\n')
(own / 'logs/A139_A140_promotion_receipt.txt').write_text(receipt)
print(receipt)
