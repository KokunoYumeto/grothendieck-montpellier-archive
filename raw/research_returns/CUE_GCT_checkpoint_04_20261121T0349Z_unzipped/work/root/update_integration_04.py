from pathlib import Path
from datetime import datetime, timezone
import csv

R = Path(__file__).resolve().parent
OUT = R.parents[1] / 'deliverables'
now = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p = R / 'findings.tex'
s = p.read_text()
assert '\\label{G-14}' not in s
p.write_text(s + '\n' + (R / 'g14_fragment.tex').read_text())

with (R / 'questions.tsv').open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['G-Q14', 'Prompt Q1/Q2; coefficient-weight boundary and cyclic ternary pencil', 'Can the standard first-row padding boundary be strengthened in the four-row sector?', 'PROVED G-14: the determinant first-jet projection is dominant; no positive padded-form multiplicity gap can have lambda1<=d(n-m)+1. Every gap needs lambda1>=d(n-m)+2.'])
    w.writerow(['G-Q15', 'Prompt Q1/Q2; G14 higher-jet continuation', 'Can the padding exclusion be extended through the second or third jet?', 'OPEN: establish dominance of j2 or j3 for determinant pencils. The precise cofactor-algebra multiplication maps are being tested; weak Lefschetz alone does not establish the required power map.'])

rows = [
    ('G-14', 'targeted proof check', 'PASS complete root reading: all cyclic ternary cofactors span degree m-1 by the nonzero Gaussian-binomial coefficients and finite Fourier decomposition; m1 separate; block-surjective first-jet differential; coefficient weights bounded by first row; determinant-ideal isotypic containment; arbitrary padding linear form and full ambient highest-weight restriction. The higher-jet statement is explicitly conditional.'),
    ('I-26', 'targeted proof check', 'PASS complete root reading of final corrected proof: kernel dimension and injective evaluation over every stated field; Cauchy-Binet nonzero coefficient; exact Lagrange reproduction and common translation invariance; all-minor translation representation and its independence; square-zero and commuting matrices; Wk logarithmic necessary growth; every coefficient of the width4 example; unique matroid-basis cocharacter repair with its separate scalar grid requirement.'),
    ('I-B09-HMM', 'used and rechecked in this run', 'Root independently opened primary published Theory of Computing20(1)2024 article and read Theorem1.3 printed p6, Corollary1.5 p7, Theorems1.9-1.10 p10. Confirmed determinantal vanishing-ideal provenance and the retained low-degree-monomial hypothesis; not a full independent reproof of the cited paper.')
]
with (R / 'integration_04_check_events.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['statement_id', 'date', 'who', 'type', 'outcome'])
    for identifier, kind, result in rows:
        w.writerow([identifier, now, who, kind, result])

p = R / 'grothendieck.tex'
s = p.read_text()
marker = '\\subsection{What the manuscript record does and does not establish}'
new = r'''
\paragraph{G-14. Truncated coefficient jets and Schur-weight exclusion.}
The restriction modulo the square of the padding coordinate defines a linear
jet projection between affine parameter schemes. At a cyclic ternary pencil,
the differential is surjective: its two blocks are the cofactor-span map and
its multiplication by linear forms. The nonzero differential minor gives a
dominant morphism in characteristic zero (D-FGA). Every weight in the Schur
functor of shape $\lambda$ uses any fixed basis direction at most
$\lambda_1$ times, by its exterior-column construction in D-S6. After padding,
the low-weight part of an equation therefore factors through the first jet.
Its vanishing on the dominant determinant-jet image forces vanishing on all
padded forms. This is containment of the corresponding isotypic ideal
submodules, followed by exact passage to the characteristic-zero quotient;
it is not an assertion that the full padded varieties are contained.

\paragraph{I-26. Determinantal equations of an interpolation image.}
The maps $U$ and $V$ define bundle maps with $UV^T=0$. The determinant of
$U\operatorname{diag}(X)V^T$ is a nonzero section by a maximal-minor chart,
but its pullback to the centered interpolation parameter scheme vanishes
because that pulled-back bundle map factors through a rank-$k$ bundle.
The common center acts trivially. All exterior minors form a finite free
module on which rank-one additive translations act by commuting unipotent
matrices; the proof uses polynomial identities and remains valid in the
stated characteristics. This is the D-S3 additive group action and the
D-FGA determinantal rank locus. The surviving column-matroid bases give the
separate cocharacter nonvanishing certificate of D-S3. No purity assertion
turns the annihilated interpolation pullback into a nonzero section.

'''
assert marker in s
p.write_text(s.replace(marker, new + marker))

with (OUT / 'LEDGER.md').open('a') as f:
    f.write('\n\n## ' + now + ' — first-jet boundary and centered interpolation test\n\n')
    f.write('G14 is proved and whole-proof checked: determinant pencils dominate their first two padding-coordinate jets, so every positive four-row padded-form multiplicity gap needs lambda1>=d(n-m)+2. The higher-jet extension has a precise remaining dominance gate. I26 supplies nonzero centered-SV_k annihilators of degree k+1 and width binom(2k+2,k+1), including a width-four one-pair example; it forces at least logarithmically many pairs within that particular generator family. Its commuting construction is compared with the established commuting-ROABP literature, and its monomial cocharacter repair is explicit. This is an ordinary progress entry, not the scheduled three-hour review.\n')

with (OUT / 'IMPLICATIONS.md').open('a') as f:
    f.write('\n\n### First-jet refinement and dense interpolation limitation\n\n')
    f.write('G14 strengthens the necessary first-row condition for any four-row multiplicity obstruction against a degree-m form padded to degree n: lambda1 must be at least d(n-m)+2. The first-jet dominance is proved; second- and third-jet dominance remain explicit targets. I26 refutes centered interpolation with a constant number of pairs as a uniform-in-width rank-test construction: its necessary pair count grows at least logarithmically with width. This is a limitation of that map, not a lower bound against general hitting sets; the displayed counterexamples admit simple cocharacter detection.\n')
print(now)
