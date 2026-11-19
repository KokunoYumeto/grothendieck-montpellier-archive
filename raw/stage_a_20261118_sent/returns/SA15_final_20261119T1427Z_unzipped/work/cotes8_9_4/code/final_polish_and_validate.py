"""Final presentation cleanup and structural QA; no verdicts inferred from text.

Run after the authored serializers. The TSV rewrites below are explicit editorial
decisions. This script is idempotent and preserves source text and identifiers.
"""
import csv
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PACKAGE = 'MPL_8_079-081+9+4+100'

def read_tsv(name):
    with (BASE / name).open(newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)

def write_tsv(name, fields, rows):
    with (BASE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

links = [
('folder', 'cote 8:78, other Pro package lines 2755–2799; P78-I060', 'cote 8:79, lines 3–25; P894-I001', 'Direct continuation of the co-Lie character formula', 'Both endpoints were read. Scan 79 begins the additional calculation with coefficients in Λ. Root will merge P894-I001 into P78-I060.', [1,2]),
('folder', 'cote 8:80, lines 50–64', 'cote 100:37, lines 2192–2216', 'Earlier-run comparison of the degree-two obstruction and completion', 'Both endpoints were read. The deformation problems differ; no canonical comparison is proved. The cote 100 endpoint lies outside TOPIC.', [5]),
('folder', 'cote 9:19, lines 564–604', 'cote 4:6, lines 1065–1088', 'Earlier-run comparison of unit-F étale sheaves and stable de Rham augmentation', 'Both endpoints were read. Frobenius descent and dualization provide a connection, without identifying every object in the two constructions.', [57]),
('folder', 'cote 9:23, lines 689–713', 'cote 100:3, lines 1346–1392', 'Earlier-run comparison of the ordinary extension datum and reconstruction from (A_U,M,φ)', 'Both endpoints were read. This is a structural lead only. Cote 100 remains excluded from the SA15 claims census.', [73]),
('folder', 'cote 9:25, line 793', 'cote 9:27, lines 831–836', 'The intermediate sign doubt is resolved by the positive Hermitian square-root proof', 'The continuation was read directly; its proof ends with “cqfd”.', [79,85,86]),
('folder', 'cote 4:7, lines 1105–1108', 'cote 4:10–11, lines 1216–1221 and 1250–1271', 'The amended torsion sequence changes the failure of φ from surjectivity to injectivity', 'Both revisions were read in the Pro and Codex witnesses.', [120,136,137,138]),
('published work', 'cote 8:79–80, lines 3–64', 'BerghRydh2019, Appendix B, Proposition B.4', 'Exact derived co-Lie formula', 'The primary PDF proof and both manuscript pages were read. This modern source is not attributed to Grothendieck.', [1,3]),
('published work', 'cote 9:3, lines 128–176', 'Oda1969, Theorem 3.19 and Corollary 5.11', 'Dieudonné duality and the de Rham/Hodge realization', 'The precise published objects were checked. Uncertain stars and operators remain questions for inspection of the ink.', [11,12]),
('published work', 'cote 9:23, lines 697–713', 'Katz1981, Theorem 2.1', 'Explicit extension parameters for ordinary formal deformations', 'The theorem matches the local deformation quantifiers. It does not supply coordinates over every global base.', [71]),
('published work', 'cote 4:6, lines 1065–1088', 'SGA 7 II, XXII, Theorem 3.3, formula (3.3.4), p. 411', 'Stable de Rham augmentation', 'The exact formula was verified in Katz’s chapter of SGA 7; authorship is not assigned to Grothendieck.', [115]),
('published work', 'cote 4:9, lines 1173–1183', 'SGA 7 II, XXI, Theorem 1.4, pp. 374–376', 'Positive generic Hasse–Witt vanishing rank in sufficiently large degree', 'The theorem for all projective equidimensional Cohen–Macaulay X was read. The absent manuscript section 7 remains unidentified.', [129]),
('published work', 'cote 4:12, lines 1295–1312', 'SGA 7 II, XXII, Corollary 3.2, pp. 410–411', 'Trace congruence used in the point-count programme', 'The published trace formula supplies one ingredient. The proposed monodromy conclusion remains conditional.', [146]),
]
fields = ['kind','from','to','what','evidence','note_ids']
rows = []
for kind, origin, dest, what, evidence, ids in links:
    rows.append(dict(zip(fields, [kind, origin, dest, what, evidence, ';'.join(f'{PACKAGE}##{i}' for i in ids)])))
write_tsv('links.tsv', fields, rows)

# Readable mathematical descriptions; these do not edit the diplomatic witness.
reading_text = [
('ℓ with superscript G/C; f⁻¹ versus f*', 'Retain the distinct sheaf inverse image and derived ringed-topos pullback.', 'The two functors have different tensor factors; Codex corroborates the distinction, not the ink.'),
('Deleted flatness of O_S over Λ', 'Do not restore the deleted condition.', 'Locally free end cohomology modules suffice for the Postnikov base-change argument.'),
('p² versus n² after n=p was inserted', 'p² is consistent with the live representation-lifting question for a prime p.', 'Composite n and prime p give different lifting problems; the insertion changes the quantifier.'),
('“pour tout M” in the H² injection', 'Use a locally constant π-module M and the indicated vanishing of H¹ on the universal cover.', 'Cartan–Leray does not justify a version for an arbitrary sheaf.'),
('p-operation and F/V on the reduced module', 'Check the operator and Frobenius twist before identifying the tangent p-power.', 'Covariant and contravariant conventions exchange F and V; the duality diagram constrains the reading.'),
('Pro: G sans tore; Codex: G* sans tore', 'A starred dual is required if this is intended as the connected-dual criterion.', 'μ_p∞ is connected but has an étale dual; it distinguishes the statements.'),
('H^(2|1)(G,Ga)', 'Read the superscript on the scan; no degree is selected here.', 'The surrounding Dieudonné realization does not uniquely fix the ambiguous cohomological model.'),
('W_n with F^(n+1), V^(n+1) truncations', 'Determine whether W_n denotes length n or length n+1.', 'The exact small-ring pairing is perfect with target Z/p^(n+1), and degenerate with target Z/p^n under the specified exponents.'),
('Canceled F^iV^i↦0 and the coefficient λ00', 'Keep the assertion canceled; the normal-form coefficient includes p^i.', 'FV=p makes diagonal monomials contribute unless the target kills that power.'),
('The final φ(Fz)=φ(zF)= is left unfinished', 'Compare it with the live σ-twisted identity above.', 'With nontrivial Witt Frobenius the untwisted equality can fail; the coefficient calculation requires σ.'),
('Finite bimodule isomorphism live in Pro, canceled in Codex', 'The cancellation must be decided on the scan.', 'The witnesses disagree materially; standard duality cannot decide a strike-through.'),
('u·V=π(u∘F)', 'Compare the later precomposition by V_g, with the correct twist.', 'F=J3, V=0 makes the literal dual operators violate FV=0.'),
('λ_g/λ_d and F_g/F_d,V_g', 'Retain the side labels instead of combining the coefficient actions.', 'The two W-actions in the bimodule model differ by Frobenius; the page itself says “ATTENTION”.'),
('Order of composition in the canceled torsor lemma', 'Check f∘g versus g∘f and the missing final conclusion.', 'Type checking depends on the composition order; the entire sheet is canceled.'),
('“inégales caractéristiques” with inserted “in”', 'Retain the mixed-characteristic qualification.', 'The historical Tate theorem invoked is not an unqualified equal-characteristic result.'),
('Superscript G versus G/I on the representation group', 'The residual quotient acts on both inertia and W(k′).', 'Ordinary conjugation invariance would omit the semilinear coefficient action.'),
('M(o) versus M(0)', 'This likely denotes the first p-torsion level, but the indexing must be read.', 'The argument uses μp and the mod-p module; a shifted level would change the comparison.'),
('T_ℓ for any ℓ', 'Use ℓ≠p Tate inertia, or an appropriate finite p-adic comparison realization.', 'Good reduction need not make raw T_p inertia finite. The finite character cannot be that literal representation.'),
('Trace=n=dim A', 'For the full realization the rank is 2 dim A.', 'At the identity the trace must equal the rank; the same sheet gives elliptic trace 2.'),
('G⊂Aut(A_s′); “faux par Tate” margin', 'G may mean inertia after unramified closure; locate the margin’s intended target.', 'The full residual Galois action is semilinear. Both witnesses leave the margin without a definite leader.'),
('Discrete GL_g over k', 'Use the constant finite group GL_g(Fp).', 'Unit-F local systems have finite Fp fibers; the algebraic group GL_g,k has positive dimension.'),
('A[p](k) over a perfect field', 'Use geometric points with Galois descent or the associated étale sheaf.', 'The ordinary curve E/F5: y²=x³−x has no nonzero rational 5-torsion but has a one-dimensional tangent space.'),
('Canceled t_A*→t_A versus live t_A→t_A*', 'Keep the live direction and check the transpose convention.', 'The homomorphism attached to a line bundle is A→A*, while alternating duality can introduce a sign.'),
('L/ω and determinant of the tangent space without a dual', 'Use ω_A=det(t_A)^∨; the section belongs to ω_A^(p−1).', 'Taking the determinant of t_A^(p)→t_A fixes the line exponent and its dual.'),
('Q_ℓ versus Q_p and the leftward arrow', 'Check the coefficient and arrow; the normalized ordinary map is p-adic.', 'The preceding comparison uses ℓ≠p, but this construction uses T_p(A)_et.'),
('Δ(ψ)/δ(φ|ψ)', 'For the comparison of normalized maps, the denominator should use the same polarization ψ.', 'Otherwise the displayed multiplicative reduction does not follow.'),
('u* versus Rosati u′; conjugation exponent −1', 'Distinguish the Cartier dual map from the Rosati involution.', 'The proof of Δ(u*)=Δ(u) uses conjugacy in the positive symmetric case, not for all u.'),
('Canceled T_p(u)_et=T_p(u*)_et without det', 'A missing det is possible, but even the determinants are unequal for arbitrary u.', 'Codex also has no determinant sign. Preserve the cancellation and do not silently repair it.'),
('Q_p/Z_p; herm/hom; canceled Zp[T]∩Q[T]=Z[T]', 'The polynomial is on the Rosati-self-adjoint subspace and rational coefficients suffice.', 'The integer-ring intersection is false; values on integral coordinates give rational coefficients by interpolation.'),
('Δ versus δ on the square root; v versus w', 'The multiplicative determinant Δ(w²)=Δ(w)² proves the sign.', 'An undefined square-root function δ would not give the same polynomial argument.'),
('Kernel(p) decoration and parentheses', 'Read the p-primary component, distinct from a Frobenius twist.', 'The valuation argument compares the orders of the étale and multiplicative p-primary kernels.'),
('u*⁻¹ versus u*; inserted det', 'Retain the inverse dual and both determinant signs.', 'The product equals 1 for automorphisms; the individual determinants need not agree.'),
('The final comparison lacks det; biduality sign?', 'Keep a determinant-line comparison; do not infer a full module isomorphism.', 'For dimension g>1, a rank-one determinant line cannot be a rank-g Tate module.'),
('ss superscript/subscript; T_lib/H_lib; Tor/Tors', 'The superscript refers to V and the subscript to F; read each degree separately.', 'Duality exchanges the stable operators with a shifted torsion degree; ordinary semisimplification is a different functor.'),
('p≠2 historical attribution; shifted torsion degree', 'Check the historical qualifier but preserve H^(i+1)[p] in the universal-coefficient sequence.', 'Modern smooth-proper crystalline base change includes p=2; the exact sequence requires the next cohomological degree.'),
('Live reference to canceled (8.2.1)', 'Keep the reference as surviving after cancellation, without validating the formula.', 'The canceled Gysin route cannot supply a missing premise of the amended argument.'),
('Coker w replaced by H^n_cris[p]_st; old ker w ending canceled', 'Use the inserted torsion term and final 0.', 'The later dimension and bijectivity corrections are coordinated with this replacement.'),
('n−1/n+1 and faint Katz/Faux margin in the deleted w', 'Require a scan check; do not reconstruct a claim from the faint margin.', 'The Gysin degree shift matters, but the formula is canceled and the annotation is not recoverable.'),
('E^(n−1)(Y|X); geometric Frobenius versus inverse Galois Frobenius', 'Vanishing cohomology belongs to Y; retain the inverse convention.', 'The variable section is Y, of dimension n−1; arithmetic and geometric eigenvalues are inverse.'),
('Canceled negative ker w corrections', 'Use only dim H^n[p]_st−dim ker v in the live identity.', 'Restoring the deleted terms contradicts the amended exact sequence.'),
('Growth to ∞ replaced by >0; absent section 7', 'Distinguish positivity from growth and record the unavailable internal endpoint.', 'SGA 7 XXI, Theorem 1.4 proves positivity; it cannot identify the missing manuscript section 7.'),
('p-linear semisimplicity over imperfect k; constant kernel; degree superscript', 'Use relative F*E≃E and check H^n versus H^(n−1).', 'An inverse to absolute semilinear Frobenius over an imperfect base is not the unit-F structure. Kernel constancy needs control of ker v.'),
('Surjective replaced by injective, “donc bijective”; dual torsion n+1', 'Preserve the corrected criterion and its ker v=0 qualification.', 'φ is already surjective in the live exact sequence; the old “resp.” cases are canceled.'),
('General equivalence of φ-bijectivity with equality in the free-rank inequality', 'Check whether a missing hypothesis kills the preceding-degree stable torsion and ker v.', 'The independent derivation gives defect b+c but dim ker φ=c−dim ker v.'),
('H¹(X)=0; truncated Z/; H²[p] versus H²⊗k', 'Interpret H¹ as crystalline here and distinguish the p-torsion kernel from the tensor quotient.', 'The universal-coefficient argument produces H²[p], not all of H²/p; Codex corroborates the group ending Z/p.'),
('Canceled stable term from a product with projective space', 'Keep it canceled; positive-degree Tate classes have zero F-stable reduction.', 'The proposed factor does not supply slope-zero classes.'),
('Full π₁ image, arithmetic/geometric distinction, rank r≥2, and conditional point counts', 'Separate the monodromy groups and retain the finite-extension and every-open qualifiers.', 'Arithmetic cosets can restrict Frobenius classes even when the arithmetic image is large.'),
('n≥2 insertion and ambiguous parenthesis X=P^(r=1)', 'Retain the exclusion of the n=1 boundary.', 'For P1, monodromy on the d-point quotient factors through S_d. For p=3 and d=3 it has at most 6 elements, whereas GL₂(F3) has 48. This does not refute the n≥2 statement.'),
]
fields, rows = read_tsv('readings.tsv')
assert len(rows) == len(reading_text) == 48
for row, (reading, alternative, evidence) in zip(rows, reading_text):
    row.update(reading=reading, alternative=alternative,
               evidence=evidence + ' No scans or second-pass corrections were supplied.')
write_tsv('readings.tsv', fields, rows)

# Exact prose-only substitutions. IDs, source quotations, keys and URLs are not
# mechanically tokenized, and mathematical conventions are not normalized.
replacements = {
 'initiallyandrereadfinalaudit;leads,noverdictrows.': 'initially and reread during the final audit; leads only, with no verdict rows.',
 'Fullyread': 'Fully read ',
 'Initial readingbeforeutility; reread mathematicalendpointsspanswhilecheckingclaims.': 'Initial reading before the utility was created; the mathematical endpoint spans were reread while checking the claims.',
 'Fullmanualread; reread19Novemberduringfinalreadingsaudit.': 'Full manual reading; reread on 19 November during the final readings audit.',
 'Numberedreread corrected cote4itemlocators.': 'Numbered rereading corrected the cote 4 item locators.',
 'Numberedreread ofRosatisign,lattice,variance.': 'Numbered rereading of the Rosati sign, lattice and variance arguments.',
 'Numberedreread added marginaltrace-integralityclaim.': 'Numbered rereading added the marginal trace-integrality claim.',
 'Numberedreread added everycoefficientidentity.': 'Numbered rereading added every coefficient identity.',
 'cote100': 'cote 100', 'Cote100': 'Cote 100', 'cote8': 'cote 8', 'cote9': 'cote 9', 'cote4': 'cote 4',
 'other Pro package2755': 'other Pro package lines 2755',
 'AppendixB': 'Appendix B', 'PropositionB.': 'Proposition B.',
 'printedpp': 'printed pp. ', 'printed33': 'printed pp. 33', 'printed34': 'printed pp. 34',
 'Author PDF2May2019.': 'Author PDF dated 2 May 2019.',
 'Verified author version2May2019': 'Verified author version dated 2 May 2019',
 'introductionp3': 'introduction p. 3', 'firstcirculation': 'first circulation',
 'Singla2010introductionp3': 'Singla 2010, introduction p. 3',
 'Oda1969Theorem3.19': 'Oda 1969, Theorem 3.19',
 'IllusiePisa2015§3.2': 'Illusie, Pisa 2015, §3.2',
 'IllusiePisa2015pp16–17': 'Illusie, Pisa 2015, pp. 16–17',
 'Illusie1976§2.4': 'Illusie 1976, §2.4',
 'Berthelot–Messing1979§2': 'Berthelot–Messing 1979, §2',
 'Katz–Oda1968construction': 'Katz–Oda 1968 construction',
 'Katz–Messing1974': 'Katz–Messing 1974',
 'Katz1981gives': 'Katz 1981 gives',
 'MilneTheorem11.1': 'Milne, Theorem 11.1',
 'KatzTheorem2.1': 'Katz, Theorem 2.1',
 'CaraianiLemma4.1.7': 'Caraiani, Lemma 4.1.7',
 'Caraiani§4.1': 'Caraiani, §4.1',
 'Achter–PriesProposition4.8': 'Achter–Pries, Proposition 4.8',
 'Berthelot–Esnault–RüllingRemarks9.2': 'Berthelot–Esnault–Rülling, Remarks 9.2',
 'Berthelot–Esnault–Rülling§9.2': 'Berthelot–Esnault–Rülling, §9.2',
 'BMSLemma2.12': 'BMS, Lemma 2.12',
 'BMSTheorem1.1': 'BMS, Theorem 1.1',
 'Berthelot’s1973note': 'Berthelot’s 1973 note',
 'original1958scan': 'original 1958 scan',
 'KoblitzI§5Theorem1': 'Koblitz I, §5, Theorem 1',
 'KatzSGA7II,XXII,Theorem3.3,formula(3.3.4)': 'Katz, SGA 7 II, XXII, Theorem 3.3, formula (3.3.4)',
 'KatzSGA7II,XXI,Theorem1.4,': 'Katz, SGA 7 II, XXI, Theorem 1.4, ',
 'KatzSGA7XXIICorollary3.2': 'Katz, SGA 7 XXII, Corollary 3.2',
 'KatzSGA7XXICorollary2.2': 'Katz, SGA 7 XXI, Corollary 2.2',
 'KatzSGA7XXII(3.3.4)': 'Katz, SGA 7 XXII, formula (3.3.4)',
 'KatzSGA7XXII uses': 'Katz, SGA 7 XXII uses',
 'KatzXXIICorollary3.2': 'Katz, XXII, Corollary 3.2',
 'KatzXXICorollary2.2': 'Katz, XXI, Corollary 2.2',
 'KatzXXII(3.3.4)': 'Katz, XXII, formula (3.3.4)',
 'KatzXXII;': 'Katz, XXII;',
 'deJong': 'de Jong', 'deRham': 'de Rham',
 'forW_n': 'for W_n', 'forp5': 'for p=5', 'forp2': 'for p=2',
 'forℓ': 'for ℓ', 'atp': 'at p', 'rawp-adic': 'raw p-adic',
 'rawT_p': 'raw T_p', 'constant5-torsion': 'constant 5-torsion',
 'unramifieddegree4': 'unramified of degree 4', 'degree4': 'degree 4',
 'order3': 'order 3', 'rank-one': 'rank-one',
 'andF25': 'and F25', 'andy²': 'and y²',
 'overK=': 'over K=', 'overQp': 'over Qp',
 'trace2': 'trace 2', 'traces−1': 'traces −1',
 'and2': 'and 2', 'characteristicp': 'characteristic p',
 'characteristic0': 'characteristic 0', 'characteristic≠': 'characteristic ≠',
 'characteristic(0,p)': 'characteristic (0,p)',
 'for ordinaryA': 'for ordinary A', 'For ordinaryA': 'For ordinary A',
 'closedk': 'closed k', 'perfectk': 'perfect k', 'residuek': 'residue k',
 'localR': 'local R', 'mapsT_p': 'maps T_p',
 'letter6.7': 'letter 6.7', 'inC018': 'in C018',
 'inC034': 'in C034', 'inC036': 'in C036', 'inC041': 'in C041',
 'inC023': 'in C023', 'ofC056': 'of C056', 'UnderC056': 'Under C056',
 'onC051': 'on C051', 'byC060': 'by C060', 'InC056': 'In C056',
 'Theorem3.19': 'Theorem 3.19', 'Corollary5.11': 'Corollary 5.11',
 'Theorem2.1': 'Theorem 2.1', 'Theorem4.2': 'Theorem 4.2',
 'Theorem1': 'Theorem 1', 'Theorem2': 'Theorem 2', 'Lemma4': 'Lemma 4',
 'Lemma4.1.7': 'Lemma 4.1.7', '§2.3.1': '§2.3.1',
 'andTheorem': 'and Theorem', 'and§2.3': 'and §2.3',
 'pp374–376': 'pp. 374–376', 'proofs.md§': 'proofs.md §',
 'Illusie§': 'Illusie §', 'Dembélé–Freitas–Voight§': 'Dembélé–Freitas–Voight §',
 'and§14': 'and §14', 'and§5': 'and §5', 'in§2.3': 'in §2.3',
 'ReductionGL_d': 'Reduction GL_d', 'constantGL_g': 'constant GL_g',
 'algebraicGL_g': 'algebraic GL_g', 'fullGL_': 'full GL_',
 'imageGL_r': 'image GL_r', 'provesGL_f': 'proves GL_f',
 'thereforeGL_r': 'therefore GL_r', 'mapsSL_r': 'maps SL_r',
 'ontoFp': 'onto Fp', 'groupS_d': 'group S_d',
 'for eacht': 'for each t', 'andr≥': 'and r≥', 'andtracet': 'and trace t',
 'at most6': 'at most 6', 'versus48': 'versus 48',
 'rank0': 'rank 0', 'rank1': 'rank 1', 'rank2,p2': 'rank 2, p=2',
 'pairs(': 'pairs (', 'semilinearFrobenius': 'semilinear Frobenius',
 'invertingp': 'inverting p', 'inW(k)': 'in W(k)',
 'theμp': 'the μp', 'whenK': 'when K', 'containsμp': 'contains μp',
 'ifμp': 'if μp', 'forμ_p': 'for μ_p',
 'counterexampleμ_p': 'counterexample μ_p',
 'equivariantK₀': 'equivariant K₀', 'exactK₀': 'exact K₀',
 'equivariantTor0/Tor1': 'equivariant Tor0/Tor1',
 'freeZ/n': 'free Z/n', 'freeZ/p': 'free Z/p',
 'ordinaryE/': 'ordinary E/', 'OrdinaryE/': 'Ordinary E/',
 'overF5': 'over F5', 'overF': 'over F',
 'integer√': 'integer √', 'degreep': 'degree p', 'while−1': 'while −1',
 'degree1': 'degree 1', 'determinant−1': 'determinant −1',
 'example1/2': 'example 1/2', 'rank2g': 'rank 2g', 'is2g': 'is 2g',
 'notg': 'not g', 'factor2': 'factor 2',
 'base change,F,V': 'base change, F, V', 'ImF': 'Im F',
 'degreei': 'degree i', 'everyi': 'every i', 'gives0→': 'gives 0→',
 'divisorY': 'divisor Y', 'n-foldX': 'n-fold X', 'dimensionn': 'dimension n',
 'hypersurfaceY': 'hypersurface Y', 'sectionY': 'section Y', 'locusU_d': 'locus U_d',
 'Cohen–MacaulayX': 'Cohen–Macaulay X', 'projectiveX': 'projective X',
 'smoothX': 'smooth X', 'arbitraryX': 'arbitrary X', 'allX': 'all X',
 'all-X': 'all-X', 'degreeD': 'degree D',
 'depending onX': 'depending on X', 'allowableX': 'allowable X',
 'there isd0': 'there is d0', 'everyd≥': 'every d≥',
 'ifH^': 'if H^', 'Forn=': 'For n=', 'ifker': 'if ker', 'iffker': 'iff ker',
 'andker': 'and ker', 'controlker': 'control ker', 'withker': 'with ker',
 'Underker': 'Under ker', 'ker v0': 'ker v=0', 'byker': 'by ker',
 'Ifker': 'If ker', 'fromk': 'from k',
 'relativeφ': 'relative φ', 'forφ': 'for φ', 'letE=': 'let E=',
 'termH^': 'term H^', 'dimH^': 'dim H^', 'dimker': 'dim ker',
 'dimcoker': 'dim coker', 'one-dimensionalkerφ': 'one-dimensional ker φ',
 'Sincev': 'Since v', 'surfaces,ker': 'surfaces, ker',
 'withH¹': 'with H¹', 'andH¹': 'and H¹', 'givesH²': 'gives H²',
 'stableH²': 'stable H²', 'H¹_cris0': 'H¹_cris=0',
 'theoremread': 'theorem read', 'isomorphismF*': 'isomorphism F*',
 'crystallinep-torsion': 'crystalline p-torsion', 'degreen': 'degree n',
 'Letb=': 'Let b=', 'isc−': 'is c−', 'isb+c': 'is b+c',
 'is b+c whereasdim': 'is b+c whereas dim', 'whiledim': 'while dim',
 'such asb=': 'such as b=', 'andk0=': 'and k0=',
 'patternb1,c0,k0=0': 'pattern b=1, c=0, k0=0',
 'divisible byp': 'divisible by p', 'genusg': 'genus g',
 'andp-adic': 'and p-adic', 'modp': 'mod p',
 'van derPut': 'van der Put', 'van derMarel': 'van der Marel',
 'useT_ℓ': 'use T_ℓ', 'anyℓ': 'any ℓ',
 'withFa=': 'with Fa=', 'coefficientφ': 'coefficient φ',
 'obeysφ': 'obeys φ', 'preserveφ': 'preserve φ',
 'canceledφ': 'canceled φ', 'wheneverp^': 'whenever p^',
 'denotedV(': 'denoted V(', 'is0→': 'is 0→',
 'coefficient-of1': 'coefficient of 1',
 'continuousπ': 'continuous π', 'scan80': 'scan 80', 'scan79': 'scan 79',
 'scan27': 'scan 27', 'scan28': 'scan 28',
 'subclaimsC': 'subclaims C', 'ofker': 'of ker', 'toH^': 'to H^',
}

protected = {'id','items','sources','refs','key','web_ref','url','entry_id',
             'item_id','statement_id','source','his_words','his_statement',
             'reading','heading','note_ids'}

def polish(text):
    for a,b in sorted(replacements.items(), key=lambda pair: -len(pair[0])):
        if a != b:
            text = text.replace(a,b)
    # All unqualified three-digit I/C/P cross-references in this owned package
    # refer to its temporary namespace. Fully qualified root IDs stay intact.
    while 'P894-P894-' in text:
        text=text.replace('P894-P894-','P894-')
    return re.sub(r'(?<![A-Za-z0-9_-])([ICP])([0-9]{3})(?![A-Za-z0-9_-])',
                  lambda m: 'P894-'+m.group(1)+m.group(2), text)

def walk(obj, key=None):
    if key in protected:
        return obj
    if isinstance(obj, str):
        return polish(obj)
    if isinstance(obj, list):
        return [walk(v) for v in obj]
    if isinstance(obj, dict):
        return {k:walk(v,k) for k,v in obj.items()}
    return obj

for name in ['items.json','claims.json','problems.json','reference_evidence.json']:
    data = walk(json.loads((BASE/name).read_text()))
    if name == 'claims.json':
        by_id = {d['id']: d for d in data}
        by_id['P894-C024']['statement'] = ('For an elliptic curve over an algebraically closed field of characteristic ≠2,3, '
            'the origin-preserving automorphism group has order 2, 4 or 6. A finite potentially-good inertia image '
            'embeds in this group and may have any subgroup order, including 1 and 3.')
        by_id['P894-C031']['statement'] = ('The literal formula identifying a rank-g unit-F tangent module with '
            'k⊗FpA[p](k) or its dual fails with the quantifier “every perfect k”. For E/F5: y²=x³−x, '
            'E is ordinary but E[5](F5)=0. Use geometric points with Galois descent or a sheaf formulation.')
    (BASE/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

for name in ['supplementary_entries.tsv','check_events.tsv','source_read_log.tsv']:
    fields, rows = read_tsv(name)
    rows = [{k:(v if k in protected else polish(v)) for k,v in row.items()} for row in rows]
    if name == 'source_read_log.tsv':
        rows = [dict(zip(fields, r)) for r in dict.fromkeys(tuple(row[f] for f in fields) for row in rows)]
    write_tsv(name, fields, rows)

for name in ['directions.md','contribution.md','proofs.md','research_log.md']:
    file=BASE/name
    file.write_text(polish(file.read_text()))

# Structural QA. All scopes and verdicts were authored before these checks.
items = json.loads((BASE/'items.json').read_text())
claims = json.loads((BASE/'claims.json').read_text())
problems = json.loads((BASE/'problems.json').read_text())
refs = json.loads((BASE/'reference_evidence.json').read_text())
families = json.loads((BASE/'claim_search_families.json').read_text())
_, entries = read_tsv('supplementary_entries.tsv')
_, events = read_tsv('check_events.tsv')
_, reads = read_tsv('readings.tsv')
_, links = read_tsv('links.tsv')
item_ids = {i['id'] for i in items}
claim_ids = {c['id'] for c in claims}
reference_keys = {r['key'] for r in refs}
expected = {f'{PACKAGE}##{i}' for i in range(1,149)}
actual_sources = [s for i in items for s in i['sources']]
assert len(items)==41 and len(item_ids)==41
assert len(claims)==82 and len(claim_ids)==82
assert len(problems)==26 and len({p['id'] for p in problems})==26
assert set(actual_sources)==expected
assert all(n==1 for n in Counter(actual_sources).values())
assert {e['entry_id'] for e in entries if e['scope']=='in scope'}==expected
assert len(entries)==349
assert len([e for e in entries if e['scope']=='outside TOPIC'])==201
assert all(not e['item_id'] and e['verdict']=='out of scope' for e in entries if e['scope']=='outside TOPIC')
assert all(e['item_id'] in item_ids for e in entries if e['scope']=='in scope')
assert set(families)==claim_ids
assert all(set(c['items']) <= item_ids for c in claims)
assert all(set(c['refs']) <= reference_keys for c in claims)
assert all(set(p['refs']) <= reference_keys for p in problems)
assert claim_ids <= {e['statement_id'] for e in events}
assert item_ids <= {e['statement_id'] for e in events}
assert all(s.startswith(PACKAGE+'##') for link in links for s in link['note_ids'].split(';'))
assert 'P78-I060' in links[0]['from'] and 'P78-I062' not in json.dumps(links)
assert len(reads)==48 and len(links)==12
assert not any('codex' in s.lower() for s in actual_sources)
assert all(r['read_status'] for r in refs)
all_local_ids = item_ids | claim_ids | {p['id'] for p in problems}
used_local_ids = set()
for name in ['items.json','claims.json','problems.json','directions.md','contribution.md','proofs.md']:
    text=(BASE/name).read_text()
    assert 'P894-P894-' not in text, name
    assert not re.search(r'(?<![A-Za-z0-9_-])[ICP][0-9]{3}(?![A-Za-z0-9_-])',text),name
    used_local_ids.update(re.findall(r'P894-[ICP][0-9]{3}',text))
assert used_local_ids <= all_local_ids, used_local_ids-all_local_ids
sessions = []
for file in sorted((BASE/'outputs').glob('search_sessions_*.json')):
    d=json.loads(file.read_text())
    sessions.extend(d if isinstance(d,list) else d.get('sessions',[]))
report = {
    'result':'PASS', 'items':len(items), 'claims':len(claims),
    'problems':len(problems), 'in_scope_supplementary_entries':len(expected),
    'excluded_cote100_entries':201, 'readings':len(reads), 'links':len(links),
    'opened_references':len(refs), 'search_family_coverage':len(families),
    'check_events':len(events), 'source_read_events':len(read_tsv('source_read_log.tsv')[1]),
    'search_session_count':len(sessions),
    'resolved_internal_ids':len(used_local_ids),
    'checks':['Unique in-scope source assignment', 'Every claim has a search family',
              'All item and reference joins resolve', 'All linked source IDs are fully expanded',
              'Cote 100 segregated', 'Codex leads have no verdict rows',
              'Root continuation points to P78-I060', 'Every claim and item has a check event'],
    'editorial_corrections':['C024 says automorphism-group order, not every individual automorphism order',
                             'C031 rejects the universal perfect-field quantifier, not every instance'],
}
(BASE/'outputs/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
