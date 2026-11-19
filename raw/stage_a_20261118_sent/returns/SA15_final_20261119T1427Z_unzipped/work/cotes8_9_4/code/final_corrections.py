"""Explicit final source-driven updates; rerun serializers afterwards."""
from pathlib import Path
W=Path(__file__).resolve().parents[1]
changes={
'make_claims.py':[
('The finite-presentation formula matches Bergh–Rydh, AppendixB, PropositionB.4; the arbitrary-character limit is a separate scope issue.','Bergh–Rydh, AppendixB, PropositionB.4 proves the formula; its proof explicitly permits arbitrary locally constant character sheaves. The infinite-torus step of the manuscript remains a proof-presentation issue, not a counterexample to the formula.'),
('For smooth proper varieties over finite fields, the characteristic polynomials of crystalline and ℓ-adic Frobenius agree; applying this to restriction quotients requires the indicated exactness.','For smooth projective varieties over finite fields, the characteristic polynomials of crystalline and ℓ-adic Frobenius agree; applying this to restriction quotients requires the indicated exactness.'),
('The final point-count programme needs the generic stable vanishing rank to grow, not merely be positive, asd→∞. This is distinct from the exact positivity theoremC065.','The final programme needs generic stable vanishing rank r_d→∞ for a fixed smooth projective n-fold X⊂P^N of degreeD as d→∞. In fact r_d has leading term Dd^n/n!; subtracting the fixed image of H^(n−1)(O_X) does not change that leading term.'),
("'stated as a needed expectation','C','KoblitzI§5Theorems1–2 give asymptotic Hasse–Witt bounds, but key formulas were absent from the OCR; this run does not certify an exact growth exponent or every-X quantifier from them.'","'stated as a needed expectation','B','KoblitzI§5Theorem1 explicitly states the leading term Dd^n/n! for a constructed section. Lemma4 transfers its stable-rank bound to the generic open for Cohen–MacaulayX and d sufficiently large; Theorem2 combines them. This proves the weaker unboundedness needed here without using the unread displayed defect bound.'"),
("family='F09',confidence='medium')\nc(75","family='F09',confidence='high',date='Princeton thesis1974; published1975.')\nc(75"),
('For the indicated smooth projective surface S obtained as a free Z/p quotient','Over an algebraically closed field of characteristic p, for the indicated smooth projective surface S obtained as a free Z/p quotient'),
('assert [int(x[\'id\'][-3:]) for x in claims]==list(range(1,81))', '''c(81,7,[3],['130–147'],'Enveloping group and Lie algebra of the dual extension.',
 'For a p-divisible group G over a perfect characteristic-p field, the enveloping extension is interpreted as its universal vector extension: its vector kernel is the group associated to ω_(G*), denotedV(t_(G*)) in the manuscript’s vector-group convention. Its Lie sequence is0→ω_(G*)→LieE(G)→LieG→0; the dual gives0→ω_G→D(G)_k→LieG*→0. No finite-type representability of the whole p-divisible sheaf is asserted.',
 'construction stated without proof','B','IllusiePisa2015pp16–17 explains the universal-extension route and Messing’s crystalline construction; Berthelot–Messing1979§2 and§5 provide the later cohomological and duality framework.',['IllusiePisa2015','BerthelotMessing1979'],family='F02',date='Grothendieck1966letter discussed in the primary historical source; Messing1972 construction cited there.')
c(82,40,[12],['1280–1296'],'n≥2 qualification and the projective-line boundary remark.',
 'For X=P1 and a smooth degree-d zero-dimensional section Y, the vanishing H⁰ representation is Fp^d/Fp and monodromy factors through the permutation groupS_d. It therefore cannot be fullGL_(d−1)(Fp) in general: p=3,d=3 gives order at most6 versus48. This checks the need to exclude n=1; it does not refute the stated n≥2 question.',
 'boundary case explicitly separated in the manuscript','E','The permutation representation gives an elementary exact boundary test. No implication for higher-dimensional hypersurface monodromy is asserted.',[],comp='check_monodromy_boundary.py enumerates the six quotient matrices and all48 invertible2×2 matrices overF3.',family='F10')

assert [int(x['id'][-3:]) for x in claims]==list(range(1,83))''')
],
'make_items.py':[
('The modern ℓ/crystalline characteristic-polynomial comparison removes that particular standard-conjecture proviso in the smooth-proper setting;','The modern ℓ/crystalline characteristic-polynomial comparison removes that particular standard-conjecture proviso in the smooth-projective setting;'),
('The page’s historical statement that this is not known, even for plane curves, is not a present-day status claim.','The rank-growth input is established by Koblitz’s Theorem1 and Lemma4. The page’s historical statement that the congruences are not known, even for plane curves, is not a present-day status claim.'),
('The notes correctly separate the elementary conditional implication from the unproved monodromy and rank-growth inputs; the finite-field/open-set quantifiers are retained.','The notes correctly separate the elementary conditional implication from the monodromy and rank-growth inputs. Later literature settles rank growth; the fixed-X full-monodromy formulation is not verified. The finite-field/open-set quantifiers are retained.')
],
'make_problems.py':[
('Separate eventual positivity from a quantitative growth theorem for the chosen fixedX.','For a fixed smooth projective n-foldX of degreeD, the generic stable vanishing rank has leading term Dd^n/n!, hence tends to infinity.'),
('KatzXXITheorem1.4 proves positivity. KoblitzI§5Theorems1–2 give relevant asymptotic bounds, but key formulas could not be read in the retrieved OCR, so the exact growth rate and full quantifiers are not certified here.','KoblitzI§5Theorem1 explicitly states the leading term for a constructed section; Lemma4 transfers the stable-rank lower bound to a generic open for Cohen–MacaulayX in sufficiently high degree, and Theorem2 combines them. The unread displayed defect inequality is not needed for this conclusion.'),
('A focused readable-copy verification of Koblitz’s estimates could settle this branch without initiating new research.','The unboundedness branch is settled; the remaining research obstacle is the separate monodromy question.')
],
'make_references.py':[
('Opening statement of crystalline Dieudonné theory and duality discussion','§2, Theorem2; §5.1 formulas(5.1)–(5.3); §5.2,Theorem5 andCorollary2'),
('Background corroboration; not substituted for exact unresolved finite dualizing-bimodule formula. Numbered theorem locators are not asserted without a further targeted read.','Locally free crystalline realization and duality results were read; they do not resolve the manuscript’s finite truncation index or cancellation discrepancy.'),
('I§5Theorems1–2,pp138–141; I§6Theorem3,p142; II§§2–3','I§2,Lemma4,p132; I§5Theorems1–2,pp139–141; I§6Theorem3,p142; II§§2–3'),
('Asymptotic Hasse–Witt estimates, generic complete-intersection invertibility, and discussion of generalized hypotheses.','Theorem1 states leading stable-rank term Dd^n/n!; Lemma4 transfers the estimate to the generic Cohen–Macaulay section. Also proves generic complete-intersection invertibility.'),
('Several formula lines missing in OCR. No exact exponent or arbitrary-X full invertibility theorem is extracted from those missing lines.','Displayed defect bounds are missing in OCR, but the explicit prose leading-term statement and generic-transfer lemma suffice for unboundedness. No all-X full invertibility or monodromy theorem is inferred.')
],
'make_audit_tables.py':[
('computations={6,12,14,23,28,31,38,40,57,67,71,75,80}','computations={6,12,14,23,28,31,38,40,57,67,71,75,80,82}'),
('independent={5,7,19,21,22,23,25,28,31,38,53,57,64,67,71,75,78,80}','independent={5,7,19,21,22,23,25,28,31,38,53,57,64,67,71,75,78,80,82}'),
('The earlier theorem’s exact growth bound is unread','The earlier theorem’s displayed defect bound is unread'),
("tsv('readings.tsv'", "r(4,12,'1280–1296','n≥2 insertion and ambiguous parenthesisX=P^(r=1)','Retain the n=1 boundary exclusion.','ForP1, monodromy on the d-point quotient factorsS_d; p3,d3 gives at most6 elements, versus48 forGL2(F3). This does not refute n≥2.')\ntsv('readings.tsv'")
]
}
for name,cs in changes.items():
    p=W/'code'/name;s=p.read_text()
    for a,b in cs:
        if a not in s:
            if a=='The earlier theorem’s exact growth bound is unread':continue
            raise AssertionError((name,a))
        s=s.replace(a,b)
    p.write_text(s)
print('Applied source-driven growth, scope, universal-extension, and boundary refinements.')
