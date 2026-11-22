# Independent whole-proof audit: odd rank-three symplectic normal cores

**Verdict: PASS for D-C3-01, D-C3-02 and D-C3-03.**

Reviewer: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited and not exposed, HODGE_DIVISION. Date: 2026-11-21. The exact record-write time is in `audit_record.json`; no estimated completion time is used.

Audited canonical proof: `agents/g34_eightfolds/bireflection/csp6_odd/csp6_section.tex`, SHA-256 `3aec637863bd7c2e7773af72805b518b3f909ab64d1235b9aeeed2a09f5116eb`. The whole mathematical text, exporter, generic parser and verifier, small-spectrum verifier, and F9 verifier were read. The separately established Hurwitz-factorization input and already reviewed finite-group classification inputs are identified below, rather than claimed as new classifications.

## Whole mathematical review

### D-C3-01: complete table and Clifford restriction

The bound is established from the complete CSp6.1 table, not its unipotent subtable. The official inventory explicitly makes this distinction. The original source has 100 character types and 90 class types. The first row type consists of linear similitude characters; the first column type is the center. The central entry at identity specialization agrees with the declared degree for every row. Every other class-length polynomial is greater than one for q at least five. Each entry is a sum of polynomial coefficients times phases of absolute value one. Expanding at q=5+x and taking absolute values coefficient by coefficient is therefore a valid upper bound for every admissible parameter value and every real x at least zero. No phase cancellation or parameter sampling is required.

The cyclic quotient CSp/Sp extension argument is correct. The inertia index is one or two, since scalar similitudes act trivially on the irreducible Sp representation and CSp/(Sp times center) has order two. A cyclic intertwiner can be rescaled to satisfy its power relation. Clifford induction then gives a CSp irreducible of degree a or 2a, with multiplicity-one restriction. This does not assert that every restriction remains irreducible.

I checked the semisimple fusion proof on all three kinds of natural primary summands. On the plus/minus-one summands there are arbitrary symplectic similitudes; on reciprocal pairs one can scale one of the two dual factors; on a self-reciprocal factor, the finite-field norm on its scalar endomorphism field supplies every desired base-field multiplier. The trace pairing recovers the relevant sesquilinear form and its adjoint involution. The same multiplier may be selected on every orthogonal summand, including multiplicities. Thus the CSp centralizer multiplier map is surjective. CSp-conjugate semisimple elements of Sp are already Sp-conjugate, so the character ratio transfers with the factor D/a canceled. The same-degree extension for a diagonal-stable irreducible, followed by Schur's lemma, covers arbitrary compatible inner-diagonal operators up to scalars.

### D-C3-02: all normalizers and the q=9 case

The perfect-cover lift and scalar ambiguity are handled correctly. The stated ordinary quasisimple covers and outer groups are precisely those covered by the cited classification inputs. Neither a particular character field nor selfduality is used.

For prime q, a nontrivial unipotent part has a nonidentity order-p unipotent power. The Fourier bound is applied first in a CSp representation of degree at most 2a, and only then to an Sp constituent. The resulting support a(p-3)/(2p) is at least a/5 for p at least five. This correctly avoids an unjustified transfer of the full unipotent character ratio across a reducible restriction.

For composite q at least 25, the unipotent ratio is at most 1/4 and the semisimple ratio has already been established. Any compatible nonscalar outer operator has a nonidentity commutator with the irreducible core. A noncentral commutator has support at least 3a/8; a nonidentity scalar commutator has actual moving rank a. The rank inequality rank([T,h]-1) at most 2 nu(T) gives the claimed 3a/16 bound in both cases.

For q=9, I requested one scope clarification: the same-degree extension paragraph applies to nontrivial diagonal outer class **and trivial field part**. The author inserted those words in the audited hash. The remaining field case is proved separately, so this was a precision repair rather than a missing case.

I checked the q=9 descent in full. If the squared automorphism is nontrivial inner, the square of the intertwiner supplies the inner support bound. Otherwise a natural lift h sigma has h sigma(h)=cI, with c in F3*. Taking multipliers gives Norm(mu)=1. Rescaling by z of norm c inverse produces a semilinear involution, whose multiplier beta has norm one. Choosing d squared equal to beta gives the descended alternating form d b. The displayed two-coordinate decomposition with zeta squared equal to minus one proves that the fixed F3-space has dimension six, spans the natural space over F9, and has a nondegenerate F3-valued alternating form. Its symplectic basis gives a similitude change of basis. Relabeling the representation by that change does not require diagonal invariance.

The row subgroup U has order 81. Its 80 nonzero additive weights all have a common multiplicity by the GL2(9) action. The unipotent ratio gives m at least a/162. Frobenius fixes nine dual weights and pairs the other 72. After scalar normalization the intertwiner is an involution; every paired weight sum contributes equally to its two eigenspaces. This proves nu at least 2a/9. The finite F9 certificate is a check of the identities, not a replacement for this six-dimensional proof.

For q=3, the two complete ATLAS-origin tables cover both central kernels and every compatible cyclic outer operator. The argument rescaling an arbitrary intertwiner to the fixed extension power relation is valid even if another abstract extension has a different scalar square. The outer quotient has order two, so no further cyclic subgroup is missing.

### D-C3-03: tensor products and actual variation

The tensor and factor-permutation bounds are valid. A factor-preserving operator has normalized eigenspace multiplicities given by convolution. A nontrivial factor cycle can be tensor-conjugated to one diagonal twist; each basis-word orbit contributes at most one eigenvector of each eigenvalue, and every nonconstant word orbit has length at least two. Thus its projective support is at least one quarter of the full dimension, including arbitrary outer intertwiners on the cycle.

For the actual intermediate cover, the multiplicity Euler formula gives 6=2e(h-1)+D. With e at least 13, genus at least two is impossible. Genus one has at most six genuine branch points and actual variation rank at most six. Rank nine therefore requires a genus-zero family with at least twelve genuine branch points. The uniform support gives 12 ceil(3e/16) at most 2e+6, hence e at most 24. Multiple factors have e at least 169; a single factor at q at least five has e at least 62. The q=3 quarter bound forces e at most six, contradicting its minimum degree 13. The contradiction is necessary and uses actual Hurwitz factorization; no dimension inequality is treated as sufficient. The argument allows different field sizes, arbitrary compatible scalar/outer/permutation actions, either polarization determinant, and an inducing character field larger than the original quadratic field.

## Independent arithmetic reconstruction

`independent_check.py` imports no author parser, selected-row list, or arithmetic implementation. It uses a new exact rational-polynomial AST evaluator based on flint, and the reviewer's previously reviewed cyclotomic polynomial Fourier routine in `sporadic/verify_quarter_bound.py` (SHA-256 `1b5546a37c2ed0da7ab52b4c41cbaab547de06a5fff6e88fb4c22ca74c471393`). This is independent of the author's rational-trace/Ramanujan implementation.

The checker re-extracts every entry, degree, class length and class-type pair from the frozen original Julia source and compares them with the retained compact input. It executes no downloaded Julia code. It independently verifies all 8,811 shifted-coefficient quarter bounds, all 99 degree floors q cubed minus one, every noncentral class length, and every central-entry degree identity. It reconstructs all 228 selected rows and all 31,428 nonscalar spectra, checks fusion/order/power compatibility and the normal class union, and obtains the stated minima:

| Table | Selected rows | Spectra | Minimum degree | Minimum support ratio |
|---|---:|---:|---:|---:|
| 2.S6(3) | 140 | 19,460 | 13 | 2/7 |
| 2.S6(3).2 | 88 | 11,968 | 78 | 8/21 |

The complete execution passed in 2.862127 seconds. The first auditor run stopped on the auditor's `min([])` handling of a **zero** polynomial in the degree-floor test. The repair changed that test to coefficientwise universal quantification, so zero correctly passes. This was an auditor implementation error, not a failed mathematical inequality; it is recorded here rather than omitted.

`check_f9_independent.py` uses a separate tuple model F3[zeta]/(zeta squared plus one), importing none of the author's finite-field code. It passed all 5,760 invertible two-by-two matrices, 240 projective semilinear-involution cocycles, 5,760 symplectic descent bases, 19,440 vector decomposition identities and 6,561 dual trace-pairing identities. It also verifies the nine fixed dual weights, support 2/9, the common 3/16 constant and final degree ceiling 24. Actual runtime: 0.242371 seconds. These finite checks are explicitly subordinate to the universal proof.

## Sources and exact input boundary

1. Frank Lübeck, 1993 Heidelberg dissertation, *Charaktertafeln für die Gruppen CSp6(q) mit ungeradem q und Sp6(q) mit geradem q*. Freshly read the complete invoked passages: Introduction printed pp. 3–4, §2.2 printed pp. 18–21, §9 printed pp. 78–79. The introduction identifies complete ordinary tables; p.4 explains that the complete values are supplied electronically and that only part fits in the printed appendix; §2.2 explains the complete construction; §9 records the CHEVIE mathematical files, orthogonality checks, and the two-constituent restriction issue. URL: https://www.math.rwth-aachen.de/~Frank.Luebeck/preprints/CharTabCSp6.pdf . Full author PDF locally retrieved, 794,539 bytes, SHA-256 `5d336441c90390b3f2072ed7ceaaacdfb83776549954d9d830dbabe4967af070`. It is a dissertation, not silently promoted to a refereed journal article. Its complete character-table construction is a cited mathematical input, not independently rebuilt here.

2. Official GenericCharacterTables inventory, freshly read its complete C3 entries and contrasting C2 warning: https://oscar-system.github.io/GenericCharacterTables.jl/stable/tables_list/ . Freshly read the generic-cyclotomic semantics at https://oscar-system.github.io/GenericCharacterTables.jl/stable/cyclo/ . The source is the immutable CSp6.1.jl at commit `87231738271ed548f62e7f1c98ff2bbfc1ed30d3`, SHA-256 `f5e68e9429054370df7376f174a095bc548cf1ecf7ce44f5446f1eaebba250dc`.

3. Official CTblLib table records, freshly opened: https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6(3).html and https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbltoc/data/2.S6(3).2.html . Both specify ATLAS origin; their orders, class counts and fusion records agree. These web pages identify library version 1.3.10 and a May 2025 generation date, while the retained actual export is version 1.3.11; no claim that the web metadata has the newer version is made.

4. Li–Xia 2022, §2.2.2/Table 2.1, author p.14; Liebeck 2017, definitions pp.2–3 and Theorem 2.4(i), p.4; HHM 2015, Chapter 5/Table 1, p.35. These exact primary passages were already read and checked in this run's earlier HES and normal-core audits and are reused with their existing scope. The unipotent estimate has denominator **sqrt(q) minus one**, with minus one outside the radical. No new proof of the automorphism or Schur-multiplier classifications is claimed.

The full intermediate-cover/multiplicity factorization is the previously reviewed D-BI-01 input. The source tables and classification statements remain explicit known inputs. Subject to precisely those identified inputs, no gap was found in the new proof.
