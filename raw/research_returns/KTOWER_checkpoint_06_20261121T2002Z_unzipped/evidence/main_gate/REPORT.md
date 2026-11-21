# Main arithmetic gate: results and provenance

Updated 2026-11-21 UTC by `/root/geometry_tower` (GPT-6 Astra Pro; effort not exposed). All paths below are relative to this evidence directory unless indicated otherwise. The parent integrates the deliverable; no input or root document was edited here.

## Strongest new result

`stable_residual_propagation.tex` proves **KT-STABLE-PROPAGATION** and **KT-STABLE-LARGE-PRIME**. A single simultaneous residual eigensystem in the full level-one compact unitary space over Q(sqrt(-3)) propagates to cubic multiplicity as the coefficient weight increases. The proof uses the finite group PGL3(F_ell), the formal Weyl character at ell-regular elements, simple Brauer-character independence, the exact averaging corner, and an integral eigenflag. It does not require semisimplicity in characteristic ell.

For ell=8361790201 and every sufficiently large integer t>=0, at

`e = 18 + (ell-1)t`

there is an actual stable compact automorphic eigensystem, with a single cuspidal GL3/E constituent, whose normalized residual Galois semisimplification is

`1 + omega^18 + omega^(-18)`.

The congruence holds simultaneously at every good split Hecke prime, in both minuscule directions, hence globally over G_E. Nevertheless the corresponding rational K-primary group vanishes for **every** t>=0:

`K_(36+2(ell-1)t)(Z){ell} = 0`.

This rules out a uniform all-weight unit assertion for the **entire compact stable comparison space at this fixed auxiliary field**, even at a prime above 2^31. It does not prove that the constructed representations satisfy the stricter archive predicate Adm3U_s, that an admissible deformation point exists, or that a rational Selmer group is nonzero. The proof explicitly distinguishes those claims.

The sufficient weight bound is explicit, although enormous. With

`N = ell^3(ell^2-1)(ell^3-1)`,

`e-1 >= N^(N^2+3)` suffices. The finite-group lower bound, including the root-separation, cyclotomic norm and inverse-minor estimates, is fully written in SP.2a--SP.2b.

**KT-PROPAGATION-SMALL-SUMMANDS** strengthens the result: any family of characteristic-zero Hecke-invariant discarded subspaces of dimension o(e^3) leaves copies of the same simultaneous residual character in all sufficiently large weights in the progression. This applies to the endoscopic subspace and to the constructed symmetric-square subspace now established by KT-U3-SYM2-INJECT. It only excludes that constructed symmetric-square family; no exhaustion of all conceivable symmetric-square origins over E is claimed.

The large-prime seed is certified by `large_prime_seed_certificate.py` and `.json`. Its exact identity is

`B_(37,chi_-3)/37 = -1701990248643001964415638362402/3`.

Fretwell--Roberts Theorem 3.6 supplies the all-prime level-three newform congruence. The inert-prime residue at 2 is 6536635074, excluding CM. Current-run KT-U3-ENDO-INJECT supplies the initial compact line. The rational vanishing imports the carried complete K17-BERNOULLI-8361790201 certificate and K17-REFLECTOR, then uses the all-positive-degree comparison (K2). The large reflected Bernoulli enumeration was not rerun.

## Ordinary symmetric-square admissibility (completed source check)

`ordinary_symmetric_square_admissibility.tex` proves **KT-ORDINARY-SYM2-FAMILY**, **KT-ORDINARY-SYM2-VANISHING-PROGRESSIONS**, and **KT-ORDINARY-SYM2-ADM3**. For every prime ell dividing the listed small modulus at e0=26,28,30 and every t>=0, e=e0+(ell-1)t admits a non-CM ordinary level-three form whose adjoint over E=Q(sqrt(-3)) actually satisfies `Adm3U_s(iota,e,2,rho)`, has the global residual triple, and coexists with K_(2e)(Z){ell}=0. The latter imports KT-K52-K56-K60-VANISH and carried all-degree K2 periodicity.

The ordinary step uses FR3.6 at q=ell itself, hence has no Fontaine-Laffaille restriction. The explicit upper triangular adjoint flag has inertia exponents (e,0,-e). Their gaps prove every positive-power nonlink. Exact `WitA` is discharged by the closed source `potOfFlag`, `sphUnl`, `winOf`, and `suppSmo` proofs, including the universal quantifier over all attached cusp representations; `FlagAt` supplies `Th.Unl`. No converse from `Adm3U_s` membership to a point of a selected deformation ring is asserted.

The exact source `GD` condition also holds in every weight of these progressions, by the already checked ClassNumberThree.gd theorem and the three factorial gcds in `ordinary_family_gd_certificate.json`. The explicit fixed prime **697446897311 > 2^31** is proved prime by the full-factor Lucas certificate `ordinary_large_prime_certificate.py/.json`; this is independent of the parent's target trial division. **KT-ORDINARY-SYM2-EXPLICIT-LARGE** therefore supplies actual admissible global trace obstructions in unbounded weights at that fixed prime. All new corollaries and both tiny certificates passed the independent peer review in `../lean_chain/ORDINARY_ADMISSIBILITY_REVIEW.md`.

**Primary citation correction:** the all-prime irreducibility input is Momose's open-image theorem as explicitly recalled in Ribet1985, printed p191, immediately before Theorem3.1. The earlier draft's purported Theorem0.1 locator was incorrect. Ribet3.1 is an almost-all-prime statement. The exact p191 statement was freshly visually checked by author and peer; the original Momose proof is imported, not claimed reread. Ghate-Vatsal2004 p2144 eq1.1 is the exact checked ordinary statement. PDFs and SHA256 records are in `literature/ordinary_sources.json`.

## Other new results

| Statement | Proof | Exact contribution |
|---|---|---|
| KT-SOULE-STAB | `soule_stabilizer_correction.tex` | Explicit order-five matrix over O_Q(sqrt5) refutes the general-field cutoff in Soulé Lemma 9. The safe restriction-of-scalars cutoff is rN+1. The Q specialization remains unchanged. The proposed downstream replacement is conditional on the other published estimates. |
| KT-TWOFIELD-661 | `two_field_eisenstein_obstruction.tex` | At e=268, both normalized generalized Bernoulli numbers for conductors 3 and 7 are divisible by 661, although B392=53 modulo 661 kills the rational negative class component. An exact sufficient remaining support condition is stated, not proved. |
| KT-TRACE-AVOID | `residual_trace_avoidance.tex` | A common separating group element exists exactly when the product of the virtual residual character differences is nonzero modulo ell in the representation Grothendieck group. Valid even when ell divides the residual group order. |
| KT-TRACE-COVER | `residual_trace_avoidance.tex` | Three distinct rank-three semisimple determinant-one self-dual systems on C3 x C2 x C2 can have trace-agreement sets covering the whole group, for arbitrarily large ell. This is an abstract residual example, not an automorphic admissibility claim. |
| KT-TWOFIELD-GLOBAL | `two_field_global_obstruction.tex` | The e=268 non-CM newforms over both auxiliary fields have globally identical residual target traces; changing sigma cannot separate those ambient systems. |
| KT-TWOFIELD-FAMILY | `two_field_infinite_family.tex` | For every t>=0, e=268+330t gives simultaneous non-CM residual Eisenstein systems over both auxiliary fields, while K_(536+660t)(Z){661}=0. Only t=0 lies in the inequality 661>2e+2. |

## Rechecks, not new arithmetic results

The entire root `gl2_uniform_section.tex` and `gl2_uniform.py` passed review. All fifteen e=2,4,...,30 outputs were replayed with the same implementation and reconciled with the supplied JSON. This is not an independently implemented second computation.

The entire root `soule_comparison.tex` faithfully transcribes the attached paper's constants and Q specialization. The general-field defect is in the published Lemma 9, not in that transcription.

`residual_global_gate.tex` is an independently checked explanatory specialization of **carried K17-S17-JOINT**, with its joint-operator criterion. It must not be counted as newly discovered arithmetic progress. Its precise Lean source chain and empty-TwoPt argument were fully read by me and `/root/lean_chain`; the provenance correction has been communicated to the parent.

## Published primary locators

* Fretwell--Roberts, *Newform Eisenstein congruences of local origin*, Ramanujan Journal 64 (2024), Theorem 3.6, printed pp.517--518 (PDF pp.12--13): <https://link.springer.com/article/10.1007/s11139-024-00838-1>. The full proof of Theorem 3.6 was read. Its sufficient direction has no ell>weight hypothesis. Theorem 3.5 has the stated ell>k+1 condition; its equation (5) supplies the residual semisimplification argument.
* Zhi-Hong Sun, *Congruences concerning Bernoulli numbers and Bernoulli polynomials*, Discrete Applied Mathematics 105 (2000), 193--223, Lemma 8.1(a), printed pp.219--220 (PDF pp.26--27): <https://maths.hytc.edu.cn/__local/6/FC/FC/1ABF8BB04EF342FE2E847D09D24_C25CB165_314DA.pdf>. Part (a), including its full proof, was read. The n=1 induction is valid even when the varying index is divisible by 661. Local PDF and text are in `literature/`.
* Sug Woo Shin, *Galois representations arising from some compact Shimura varieties*, Annals of Mathematics 173 (2011), Theorem 1.2 and following compatible-system paragraph, printed pp.1647--1648: <https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p09-p.pdf>. Exact statement and coefficient-field paragraph were read; underlying trace-formula proof is cited, not reconstructed. It gives the required semisimple system in odd rank three, not characteristic-zero irreducibility.
* Christophe Soulé, attached 2003 paper, source pp.777--780 and Lemma 9: <https://ems.press/content/book-chapter-files/27335>, DOI 10.4171/DMS/3/21. The attached text is `../Soule_2003.txt`; the relevant page images in this folder were visually inspected.
* Matthias Schütt, *CM newforms with rational coefficients*, arXiv:math/0511228v5, Theorems 1.1 and 1.4, pp.2--3. The CM classification statements used here are general; they do not restrict all newforms under discussion to rational coefficient fields. Their imported classification proofs were not reproved.

## Checks and remaining boundary

`CHECK_EVENTS.tsv` records actual author and peer checks, parent-reported checks, same-code replays, independent finite arithmetic, imported background and provenance searches separately. The entire stable propagation proof and its effective estimates passed the parent and independent lean-chain whole-proof reviews. The added small-summand corollary also passed peer review; its proof was refined to allow arbitrary scalar extensions by counting dimensions in common eigenspaces.

Independent peer reports are in `../lean_chain/STABLE_PROPAGATION_REVIEW.md` and `../lean_chain/TWOFIELD_FAMILY_REVIEW.md`. These reports distinguish source statement checks from reconstructing a cited theorem's full proof. The finite-group propagation proof was searched for in the supplied checkpoint and earlier-checkpoint evidence before being classified as current-run work; no matching carried proof was found. This is a provenance search, not a claim of historical novelty.

The main uniform arithmetic gate is not closed. The new stable counterfamily identifies exactly why full compact-space automorphy plus counts cannot by itself establish the needed units. The ordinary symmetric-square families now meet even the exact Adm3U_s restrictions. A further argument must use the smaller image of the selected deformation-point construction, a different auxiliary field, or the rational reflected class-group component. No such exclusion follows merely from the automorphic eigenvalue counts.

## Later host and integral-projector review

The earlier suggestion that the selected host image might remove the ordinary symmetric-square families has now been tested directly: the full `../unitary_audit/host_sign_results.tex` construction realizes the families as actual local/global host points. My independent complete-proof review is in `HOST_SIGN_INDEPENDENT_REVIEW.md`. Their polarization sign does not by itself exclude those points.

The new `../unitary_audit/projector_results.tex` instead constructs an actual involution of the normalized integral deformation ring and injects rational strict Selmer torsion into its odd weight−1 cotangent dual. The whole proof, including the appended conditional finite-flat transfer, passed my independent review in `PROJECTOR_INDEPENDENT_REVIEW.md`; the exact16-identity matrix replay is recorded in `projector_review/`. The odd normal module along an adjoint point is eta tensor (1 plus normalized Sym^4). A unit maximal minor of the actual odd Jacobian would prove the desired vanishing, but no such minor is evaluated. Passing from branch normal determinants to the base cotangent still needs an integral comparison; generic point detection and source finiteness alone do not establish it.

## Explicit field-variation partial result

`explicit_two_unit_family.tex` proves KT-EXPLICIT-TWO-UNIT-FAMILY: for ell>=7, ell=3 mod4, e=(ell−3)/2+(ell−1)t, both D_±=−4 sf(ell±2) give two Bernoulli units, with opposite splitting atell. The third unit remains separate. `bernoulli_prefix_formula.tex` proves the exact finite-sum formula behind `explicit_two_unit_certificate.py/.json`; all1135 eligible primes through20000 and both fields have allthree unit residues, with72 direct mod-ell² and12 rational-polynomial reconciliation checks. This bounded computation is not an all-prime theorem. `FIELD_VARIATION_FOLLOWUP.md` records exact Naito/CM/p-rational/simultaneous-coefficient scopes and the primary locators. Parent and peer reviews of the infinite theorem are recorded separately from the new formula/code check.
