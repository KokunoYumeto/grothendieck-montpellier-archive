# Part A.3–A.5 local status, 2026-11-19 06:28 UTC

This contribution is incomplete as an answer to all A.3–A.5. Every projective-space case and the arbitrary-X all-residue assertion are proved. Exact finite algorithms for general ambient monodromy and rank are now proved. Uniform structural classifications, and actual full groups for the product examples, remain separate gates.

| Item | Established | Remaining gate |
|---|---|---|
| A.3 positivity/rank | Explicit all-X threshold d0 and asymptotic deg(X)d^n/n!; exact finite matrix algorithm for every specified finite-field input in effective_rank_determinant.tex | Structural formula for every fixed X, uniform as d varies |
| A.3 generic relative ordinarity | Refuted for smooth X: explicit finite-group-scheme quotient construction has Pic0=alpha4 in characteristic2 and rank stable <=g−2<dimE=g−1 in all sufficiently large degrees | Exact generic rank of this X; final invariant-ring/Bertini finite-field search was not executed |
| A.3 projective-space rank | binom(d−1,n), all d,p, from ordinary hyperplane degeneration | None |
| A.3 Hodge-level parenthesis | Literal eventual statement on maximal-stable-rank U_d proved, including p-torsion; cor:eventual-hodge-parenthesis | Stronger individual-Y equivalence outside U_d is false; it is a different quantifier |
| A.4 projective space, odd p | All n>=2 and all d: full GL_binom(d−1,n)(Fp), geometric=arithmetic, with full determinant; zero vector space for d<=n | None |
| A.4 projective space, p2 | All n>=2 and all d: rank0 for d<=n; rank1 trivial for d=n+1; full GL if d≡n mod2; full nonzero-covector stabilizer if d≡n+1 mod2 and d>=n+3 | None |
| A.4 full-GL expectation | Refuted in infinitely many degrees for every Pn in characteristic2; general adjunction-square theorem gives an invariant covector in every sufficiently high such degree for arbitrary X, with explicit bounds | Exact geometric/arithmetic group for arbitrary X |
| A.4 determinant | Exact geometric and arithmetic determinant images for arbitrary X: valuation gcd of rational Hasse determinant, plus explicit constant Kummer character; root audited | None for the determinant image |
| A.4 ordinary abelian varieties | Proved exact entire fixed quotient for products: dimension2^n−1 at p2, dimensionn at oddp when p divides all factor degrees; generic rank h_d−1 all d. Explicit F2 and F3 surface certificates independently rerun | Exact full groups inside their pointwise stabilizers |
| A.5 projective space | Every nonempty smooth-parameter open attains every residue exactly from d=n+2, every p and n>=2; d<=n only1, d=n+1 ordinary open misses1 | None |
| A.5 arbitrary X | Proved for all requested smooth connected X, including geometrically disconnected X, all d>=explicit d_res and every nonempty open; general_X_residues.tex, root audit passed | None |
| Lead A | Universal full-GL assertion refuted; positivity and all residues proved for every X; exact Pn groups; generic relative ordinarity refuted for smooth X | Exact structural generic rank and full groups for arbitrary X remain |

## Current proof files

- results.tex: all-X positivity, projective-space rank, determinant Kummer character, plane residues and prerequisite audits.
- relative_ordinarity_counterexample.tex: smooth Pic0=alpha4 counterexample; root independently audited; finite Hopf/algebra checks executed; final invariant-ring/Bertini search explicitly not executed.
- odd_characteristic_plane.tex: all odd-p plane groups, with opened Kantor–Seress Theorem3.6 and elementary cocycle/block proof.
- projective_space_odd.tex: all odd-p Pn groups and sharp residue threshold; root independently audited all parts.
- projective_space_char2.tex: all characteristic-two Pn groups by independent AS quadric swaps, Johnson-coordinate transpositions, elementary finite-group generation, and explicit global Hasse covector; root independently audited all parts.
- general_X_residues.tex: arbitrary-X every-residue theorem with explicit all-degree threshold, independent node monodromy, henselian finite Lang part, error-factor isolation; root independently audited and promoted.
- effective_rank_determinant.tex: exact finite generic-rank algorithm and exact determinant image formulas, root independently audited and promoted.
- adjunction_covector.tex: characteristic-two general-X adjunction-square invariant covector, with explicit regularity and ambient restriction bounds; root independently audited.
- ordinary_abelian_covectors.tex: fixed quotient rank2^n−1, independently audited; product_surface_obstruction.tex: fixed quotient2 in every degree of an explicit F3 surface; product_exact_covectors.tex: entire invariant spaces for all product ordinary elliptic ambient varieties, independently audited after the explicit Cartier-weight correction.
- code/ordinary_abelian_surface.py and outputs/ordinary_abelian_surface.json: explicit smooth ordinary genus37 curve in degree2 on E×E/F2, rank35 relative module with3 independent fixed covectors, all singularity ideals checked.
- all_degree_char2_contact.tex and degree5/6/7 files: independent geometric plane-theta argument, still valid but superseded for group computation by the simpler all-Pn quadric proof.

## Prerequisite audit

R1 was read in check_8_5_7.md, sections1–4. Its nilpotence step is valid: Frobenius on the hypersurface ideal factors through its p^e-th power, hence through H^(n−1)(O_X(−p^e d)); Serre duality and Serre vanishing kill this group for large e. In the explicit positivity proof the stronger vanishing H^(n−1)(O_X(−d))=0 already holds for d>=r_omega−1. We subtract the stable ambient rank, not the full coherent dimension.

R2/R10's Lang/Artin–Schreier comparison is supported by the opened Katz SGA7II XXII Proposition2.0 and the finite-dimensional Lang basis argument. The degeneration arguments use the full coherent bundle on its explicit invertibility open. A rank-dropping elliptic degeneration is used only to calculate a Hasse determinant valuation, without extending a stable local system through it.

Root's A.1 all-degree complete-intersection/W2-liftable ranges were independently checked against Cotner–Zavyalov Definition2.2.1 and Theorem2.2.3, printedp1854. The finite de Rham filtration, cone triangle, and integral derived Nakayama shifts all check.

## Main next gate

For arbitrary geometrically connected X the coherent top rank need not be ordinary, as the smooth alpha4 example proves. A hyperplane-union boundary can lie below the generic stable rank. The henselian finite-part construction and independent alternating node factors now overcome this difficulty for traces, completely proving A.5. They do not determine the full group. The new adjunction covectors show that even a single fixed-hyperplane correction to full GL may be insufficient: ordinary abelian ambient varieties force a much larger fixed quotient, whose full dimension is now proved for products. Determining the full invariant structure and the group on its kernel remains the main A.4 gate.

## Exact full-image algorithm update, 06:28 UTC

effective_monodromy.tex and perfect_field_monodromy.tex give complete finite matrix lists, not an unspecified Galois-group oracle. Primitive frame algebras, bounded polynomial enumeration, finite coefficient-ansatz absolute factorization, and explicit constants E/k0 yield exact geometric and arithmetic images; parent read both proofs and original Stacks field lemmas. The arbitrary-perfect-field arithmetic answer uses precisely E intersection k. A genuine smooth plane-quartic family was executed in lang_frame_quartic.py, with geometric/arithmetic group diag(1,GL2(F2)) certified by a six-dimensional Lang frame algebra and elementary AS irreducibility. These exact effective answers do not assert a uniform named-group classification for arbitrary X.

## Exact product groups, independently audited at 06:47 UTC

For the fixed E×E/F2 Segre cubic surface, product_full_groups.tex now proves both geometric and arithmetic groups GL8(F2) at degree1, and the full pointwise stabilizer of three independent covectors, 2^96:GL32(F2), at degree2. The proof uses a short line certificate meeting every geometric Hasse divisor, henselian finite-part inertia and purity, two arithmetic Frobenius certificates, the opened transvection classification, and an exact rank certificate forcing all translations. The parent independently reran the complete script and audited all steps. This closes two concrete full-image gates; d>=3 and arbitrary-product full groups are not thereby settled.

## Uniform product structure, independently audited 07:13 UTC

product_uniform_structure.tex proves geometric transvection generation in EVERY degree on the fixed E×E/F2, by propagation from degree3 through ordinary reducible pencils and a codimension-one rank argument. Parent and reduction/descent agent independently audited all jet, incidence and specialization steps. The same file proves the exact full fixed-covector space in every characteristic-two ordinary elliptic product: dimension2^e−1, wheree is the number of even factor degrees. Thus the fixed surface has no invariant covectors in odd degree and exactlythree in even degree. Its entire groups are now proved in degrees1,2,3; degree3 is GL80(F2) with independent finite verification. Uniform full-group classification in higher degrees is still open, now reduced to transvection-generated groups with this exact invariant quotient. Degree4 exploratory certificates are retained but have not been promoted or used to replace the uniform gate.

## Single geometric gate for uniform product full groups, 07:52 UTC

product_irreducible_hasse_reduction.tex is independently audited as a complete CONDITIONAL reduction. All Hasse divisors are geometrically reduced. If the degree-d Hasse divisor is geometrically irreducible, then every nonzero proper invariant subspace has trivial quotient, the common kernel is irreducible, a uniformly embedded natural GL80 block excludes the bilinear-form alternatives, and H1 vanishing gives every translation. Thus the exact groups follow from this one precise irreducibility hypothesis. That hypothesis is NOT proved for all higher degrees. A constant-symmetrizer probe, retained with code/output, showed that a useful one-factor degree3 symmetrization does not persist at pole degrees6,9,12,15; no generic symmetric-matrix theorem is being applied.

## Bounded degree-four irreducibility test, 07:58 UTC

The complete 5,000-pair search retained in product_hasse_irreducible_line.py and its JSON tested 655 ordinary infinities in 62.777478975 seconds. It found no irreducible full-degree restriction and is explicitly inconclusive. It did find a rational smooth point of the Hasse divisor (rank M = rank M squared = 143). The uniform geometric-irreducibility gate is unchanged.

## Entire fixed-product groups in every degree, 08:15 UTC

The former uniform product gate is now CLOSED. product_hasse_irreducibility.tex proves geometric Hasse irreducibility for every degree d>=4 by a pointed Cartier calculation at a mixed tacnodal union and an incidence argument merging all factors. Both the parent and reduction-descent agent independently audited the complete proof, including degree-one and degree-two jet exceptions. Corollary thm:product-char2-all-full-groups combines this with the retained degrees1,2,3 certificates: rank9d²−1, full GL in odd degree, full pointwise stabilizer of three covectors in even degree, geometric=arithmetic over every perfect field. The representation is irreducible exactly in odd degree. General ambient-X structural classification remains separate and is the next gate. The older entries above record the historical state at their timestamps.

## General ordinary-pair extension candidates, 08:41 UTC

ordinary_products_general_structure.tex and ordinary_products_isogeny_full_groups.tex are explicitly CANDIDATES pending independent audits. The first uses a universally checked 3×3 Cartier symmetrizer, tensor independent diagonals and a squarefree-monomial argument to start the mixed-tacnode proof in degree1 for every ordinary elliptic pair; proposed consequences are irreducible reduced Hasse divisors and transvection generation for everyd>=2, plus irreducibility of the common kernel. The second proposes a complete eventual group theorem via a nonempty degree1 GL8 moduli open, Chai1995 Theorem2 (opened original indexed text, printedp477), odd isogeny images with eighteen-point node covers, prime31 Goursat separation, and an effective isogeny search giving d1=max(m1,m2)+1. Nodal-image incidence, generic-frame connectedness, and the effective threshold are explicit audit gates; no unaudited claim is promoted.

## General ordinary-pair extension PROVED, 09:07 UTC

Both ordinary_products_general_structure.tex and ordinary_products_isogeny_full_groups.tex have now passed independent complete proof audits by the parent and reduction/descent agent. The parent independently reran both retained exact programs and reopened the precise original Chai and Stacks results. All displayed statuses have been promoted. For any ordinary elliptic pair in characteristic two, degree d>=2 has geometrically irreducible reduced Hasse divisor, geometric transvection generation, and irreducible common kernel of the exact fixed covectors. A terminating odd-isogeny search yields m1,m2 and the explicit eventual threshold d1=max(m1,m2)+1: for every d>=d1 the geometric and arithmetic groups are full GL_(9d^2-1)(F2) in odd degree and the full pointwise stabilizer 2^(3(9d^2-4)):GL_(9d^2-4)(F2) of three independent covectors in even degree. All perfect base fields are covered; computability is relative to an effective field presentation. The remaining arbitrary-X structural gate is not claimed solved.

## Supersingular degree-one full-image candidate, 09:21 UTC

For E/F2:y^2+y=x^3, the universally checked degree-one tensor Cartier pencil is the Hessian of a3×3 determinant after constant basis reversal. Its relative Hasse polynomial is det(S)^2*(s^[2]^tJs), so it has distinct double and simple cubic components. A complete candidate in supersingular_product_degree_one.tex gives exact geometric=arithmeticGL8 using one explicit F8 Frobenius polynomial and one local wild-transvection certificate. The latter is a first-derivative/simple-pole Artin-Schreier argument; this is the new independent audit gate. Exact polynomial and finite-field programs have passed, including a verifier using a different restriction-of-scalars characteristic-polynomial method. No full-group conclusion is promoted pending audit. OC owns the separate uniform supersingular parity/generic-rank theorem.

## Supersingular degree-one entire group PROVED, 2026-11-19T09:24:37Z

The parent and reduction/descent agent have independently passed the complete proof in supersingular_product_degree_one.tex and independently rerun both retained exact certificates. The relative Hasse determinant has the proved factorization det(S)^2 Q(s), yet the entire geometric and arithmetic groups are GL8(F2), over every perfect characteristic-two base field. The local wild-transvection criterion is independently proved by a simple-pole Artin–Schreier equation; it does not infer transvection generation from a rank-two Hasse component. This closes the degree-one supersingular full-image gate. Higher-degree supersingular images remain separate, with the exact generic parity-rank formula supplied by OC.

## Uniform supersingular structure candidates, 2026-11-19T09:48:10Z

The entire invariant-quotient proof in supersingular_exact_covectors.tex has passed the reduction/descent independent audit and awaits parent promotion. It gives dimension0 in odd degree and1 in even degree, overcoming the persistent nilpart through a bounded purely inseparable lift and homogeneous quadratic coefficient comparison. A separate complete candidate, supersingular_uniform_GL8_block.tex, places an actual natural GL8(F2) block in every degree via nodal isogeny images or a two-component boundary. This would exclude nondegenerate alternating forms both on the full representation and on its even-degree common kernel. The remaining full-image gate is irreducibility of that representation/kernel and, in even degree, the full translation subgroup; neither candidate asserts those conclusions.
