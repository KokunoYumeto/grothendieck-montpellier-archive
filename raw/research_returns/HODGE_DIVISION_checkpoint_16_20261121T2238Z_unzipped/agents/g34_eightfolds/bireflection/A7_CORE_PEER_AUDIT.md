# Independent whole-proof audit of D-A7-01–03

**Verdict: PASS in the stated transitive-core, nonsplit sixfold scope.**

Reviewer:/root/g34_eightfolds, GPT-6AstraPro, effort inherited/unexposed, HODGE_DIVISION. Actual record time from the clock tool:2026-11-21 19:29:43UTC. Complete mathematical reading and the independent exact run were finished before this timestamp.

Reviewed full proof: `research/a7_cores/a7_section.tex`, SHA-256 `647b2870393b00b531be6cfb2efde3b1b9079a9d188653b66b10a32def71c71a`. Both complete author programs and bibliography were read. The final framework-placement paragraph is read as using the previously established framework, not as a new verification here of its archival sources.

## D-A7-01: cover and normalizer coverage

Using every nonlinear row of the universal6.A7 cover includes every central quotient, with no unsupported faithfulness assumption on the full center. The center is cyclic of order six, so its subgroups are characteristic. An automorphism of a represented perfect central quotient lifts to the universal cover, and a lift trivial on A7 is itself trivial because the difference is a homomorphism from a perfect group to its center. Thus the actual normalizer automorphism is inner or belongs to the unique outer class.

The cyclic-extension scalar rescaling is valid. For a fixed outer lift t, a compatible intertwiner A has A²rho(t²) inverse scalar. Removing this scalar supplies the actual defining relation of the chosen6.A7.2, whether or not it splits. Inner correction recovers every normalizer element up to scalar, and scalar multiples have the same projective support. This also handles central quotients and another isoclinic extension; the proof does not claim isoclinism preserves the entire character table.

The two finite exceptions belong exactly to the two degree-six extensions of the unique center-trivial degree-six core character. Double transitivity of the natural A7 action proves that its deleted module is irreducible; uniqueness in the complete table identifies this row, so the exceptions have been removed for a mathematical reason, not by arbitrary row selection. Every other compatible normalizer has the quarter bound, and all nonstandard degrees4/6 have support at least2. The lower endpoint and extension nonoccurrence are independently reconstructed below.

## D-A7-02: actual standard tensor operators

The full automorphism group of A7 is S7, without the A6 exception. Together with Schur's lemma and factor permutation, this identifies every normalizer as an actual scalar times a rational standard tensor-wreath operator. The trace contraction around each factor cycle gives a product of standard traces in{-1,0,…,6}; every negative product has size at most6^(t-1). The same holds for every power. This proves the trace lower bound−e/6 at n7 without extrapolating a finite check.

For a nonreal root of unity, an appropriate power has real part at most−1/2. Its two conjugate eigenspaces then give trace at most e−3m, even if their powered eigenvalues coincide. Hence m≤7e/18. The scalar is a root of unity because both operators have finite order. Nontrivial multiplier lambda² implies its inverse is a nonreal eigenvalue of the rational tensor operator, so the actual moving rank is at least11e/18. The proof correctly extracts this actual scalar before using the nonreal bound; it does not assert preservation under arbitrary scalar convolution.

Every other genuine inertia costs at least e/6; a factor permutation is stronger, and a nonidentity scalar costs e. The tensor form's multiplier is nontrivial since a trivial multiplier would make the inducing character real, contrary to containment of the original imaginary quadratic field. The source factorization supplies genus zero and at least twelve genuine inertias, and a generating product-one tuple has at least two nontrivial multipliers. Thus the displayed26e/9 lower total and e≤27/4 are exact, contradicting e≥36. I reread the complete D-AST-01 statement and proof: its all-n≥3 trace statement includes n7; the normalizer extension is separately proved here using Aut(A7)=S7.

## D-A7-03: scope and endpoint geometry

Transitivity on quasisimple factors forces all factor characters to agree up to automorphism. The ordinary standard character is invariant under S7 and has intrinsic full central kernel, so one standard factor forces every factor standard. For multiple factors D-A7-02 applies. For a single factor the actual image contains A7 and lies in scalarS7 in its deleted representation. I reread D-BI-08's exact statement and relevant proof scope: it permits arbitrary inducing cyclotomic field initially and proves actual polarization splitness if rank is nine. Thus its use here is valid in precisely the stated nonsplit problem.

If no factor is standard, factorwise spectral convolution and the weighted word-orbit factor-cycle argument give support e/4 on every nonscalar normalizer. The actual intermediate-cover formula6=2e(h−1)+D excludes genus at least two for e≥4 and gives rank at most six in genus one. Therefore rank nine forces genus zero, at least twelve branches, and D=2e+6. The quarter inequality yields e≤6. Multiple factors have e≥16; the remaining single degrees4 and6 have support at least2, so twelve inertias cost24 while the total is at most18. This is a necessary-rank contradiction, not a sufficiency inference.

The theorem deliberately requires transitive factors. A nontransitive mixture of standard and nonstandard factors is not silently included. Neither determinant-free exclusion of the single standard case nor an equality of the inducing character field with the original field is asserted.

## Independent exact computation

`audit_a7_core.py` is independently written and imports no root checker, selected-row list, scan, or Ramanujan arithmetic helper. It performs all arithmetic as integer polynomials modulo cyclotomic polynomials, with exact power maps and Galois action. Extension rows are selected by pointwise equality of their restricted characters with a core irreducible, using exact common-field polynomial comparison. The fusion is checked for identity kernel, order preservation, complete normal-class unions and prime-power compatibility.

The actual complete run passed in1.901178seconds:

| Table | Selected rows | Nonscalar spectra |
|---|---:|---:|
|6.A7|39|1326|
|6.A7.2|18|558|

Total57rows,1884spectra. The only quarter exceptions are extension rows3/4, class26, degree6, support1, restricting to core row2. Their multiplicities are(5,1) and(1,5). The unique center-trivial degree-six core row is2. The minimum nonlinear degree is4; the only nonlinear degrees at most6 are4/6; every nonstandard row of those degrees has support at least2 and has no irreducible extension row. The numerical tensor and endpoint contradictions are recomputed exactly.

Input SHA-256 is `185c2a90af296395c33ad8c7c5e839fadba5fffaeda3aacac2d99c8d20c906ab`. Output is `audit_a7_core.json`. No independent construction of the original ATLAS tables or repeat full orthogonality computation is claimed; the author's GAP program checks full orthogonality, and this audit reconstructs all stated spectral inequalities independently.

## Fresh source audit

HHM2015, Chapter4 opening paragraph, numberedp31, was freshly reread in the retained full original author PDF. It explicitly includes the double covers and the triple/sixfold covers of A6/A7. No imprimitive-character classification theorem of that chapter is used.

All three official pages were freshly opened and read:

- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/6.A7.html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/6.A7.2.html
- https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/A7.2.html

They confirm ATLAS provenance, orders15120/30240/5040, class counts40/35/15, the stored normal fusion, and the actual identification of A7.2 as both S7 and Aut(A7). Their generated version1.3.10/May2025 metadata is distinguished from the retained actual package1.3.11. The newly checked claims are the derived full-support inequalities and their source-gate consequences, not new character-table classifications.

No defect was found in the complete proof. No TeX compilation is claimed.
