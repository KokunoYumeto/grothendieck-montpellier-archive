# Compact unitary audit

This evidence directory records the independent compact U(3) work in the KTOWER run. The source commit used for the Lean predicates is `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`.

## Results

The original eigenvalue 157899 belongs to compact coefficient highest weight **(5,0,−5)**, whose Harish–Chandra parameter is **(6,0,−6)**. The literal coefficient highest weight (6,0,−6) has dimension three. This is a correction of the weight terminology in the request; K17 already made the coefficient shift explicit.

`unitary_results.tex` proves the full invariant-space dimension formula in every nonnegative coefficient degree and gives its cubic quasipolynomial of period twelve. Its proof is a Burnside count of exponent-pair orbits, followed by the harmonic contraction exact sequence. The latter and the class-number-one setup are inherited inputs identified in the text.

`character_trace.py` gives a second exact computation of the scaled eigenvalue. It constructs three integral rank-one reflection matrices, with projective orbit sizes 3, 18 and 36. It averages representation characters over the 1296-element monomial group. The three scaled contributions per coset are 16807, 4067 and 952, giving

`3*16807 + 18*4067 + 36*952 = 157899`.

No K17 program, harmonic basis, neighbor matrix or operator is imported. The representation-theoretic setup is shared. This is an exact Python integer computation, not a new Lean kernel certificate. The implementation also compares the invariant dimensions with two independent combinatorial counts through degree thirty; the all-degree theorem rests on its written proof.

The uniform projector power-sum formula in `unitary_results.tex`, followed by Newton identities, gives the entire characteristic polynomial of the scaled operator in every weight. `minuscule7_cosets.json` saves all 57 rational unitary representatives by their integral numerators. An Eisenstein pair `[a,b]` denotes `a+b*omega`; every matrix is divided by `3+omega`. The construction proves integrality of the characteristic polynomial but does not prove smoothness of its comparison evaluations.

`coverage_results.tex` records a fresh reading of the exact source admissibility predicates and of the scopes of the inherited compact-transfer and classical-conductor proofs. It also proves the multiplicity-preserving comparison: distinct complete source representations require distinct complete automorphic systems, so a characteristic polynomial with full multiplicities controls the whole valuation sum. Together with the report's closed OneChar source chain, exact GD statement and inherited arithmetic comparisons, it gives

`|K_(2e)(Z)| divides N_(e,7)^2` and `log |K_(2e)(Z)| < (2/5)*e^4`

for all even `e>=2`, under the report-wide carried-source convention. The proof includes the separate vanishing of the 2-primary part. The constant is an explicit alternative; it is not an evaluation of the existential constant selected inside the archived VK-EXP7 theorem. The new `quartic_refinement.tex` further proves `log |K_(2e)(Z)| < e^4/4` using stable-only coverage, exact stable-plus-classical dimension, and the existing 57-coset norm; the stronger intermediate coefficient is 239/960. The constructed symmetric-square family is retained. The independent source-audit sibling read the entire refinement and replayed every rational constant and dimension bound successfully; see `../lean_chain/quartic_refinement_check.py` and its JSON result.

`endoscopic_results.tex` constructs the generic endoscopic packet `1 + BC(f)` for each non-CM quadratic-twist pair in the classical space. Its key check is that the global component-group generator `−I_2` belongs to the connected determinant-one local centralizer at every finite place, and has value +1 in the compact real packet. At `e=4,6` those lines fill the compact space. In particular the `e=6` eigenvalue is also obtained as `7^6+40250`, and the eigenvalue at thirteen as `13^6+1284050`. This proof constructs the global parameter before using the numerical values; it does not identify an automorphic representation from finite-prime coincidences.

`endoscopic_converse.tex` proves the full even-weight exhaustion. Its ramified local converse uses Haines's special-parahoric spherical representation theorem and the complete principal-series list of Adler–Lansky. Rogawski's published rank-three classification then reduces the global possibilities to generic parameters. The finite and compact-real component signs exclude the outer-character and three-character cases. Every remaining endoscopic line is one of the preceding lifts. Thus the endoscopic dimension is exactly `floor((e-1)/3)`, and the stable dimension is the full dimension minus this number. Both the parent and the independent source-audit sibling read the whole argument and approved its source scope. The resulting monic integral endoscopic and stable factors are given explicitly in that section.

`character_trace13.py` independently constructs the five reflection orbits at thirteen, of sizes `3,18,18,36,108`, and proves that their projective images partition all 183 lines of `P²(F13)`. The exact orbit proof and normalization are in KT-U3-SECOND13. The script imports only this audit's integer-ring character helpers. Its traces and the corresponding traces at seven agree with the complete compact characteristic polynomials in all available even degrees through thirty. `check_spectral_split.py` verifies all thirty endoscopic/stable polynomial factorizations at seven and thirteen. The independent source-audit sibling read all three scripts and replayed byte-identical copies successfully.

`symmetric_square_results.tex` constructs a further stable subspace from the non-CM twist pairs in the lower classical space of weight `e+1`. Its dimension is `floor((e-2)/6)` and its scaled split eigenvalue is `a_p(f)^2-p^e`. The new source inputs are the Gelbart–Jacquet adjoint lift, prime-cyclic Arthur–Clozel base change, and Ramakrishnan's adjoint-fiber theorem. This is the subspace constructed from level-three forms over Q; no exhaustion of every conceivable adjoint origin over E is asserted. The parent and independent source-audit sibling read the whole theorem and code and replayed all thirty polynomial checks successfully. `symmetric_square_check.py` freshly computes all the required lower-weight classical matrices and verifies the corresponding exact monic factor in all thirty stable polynomials. At `e=26,28,30`, each smaller residual modulus lies in this symmetric-square factor, and both tested comparison values of the complementary stable factor are coprime to every listed residual modulus. The independently reviewed KT-U3-SYM2-EISENSTEIN uses Fretwell–Roberts Theorem 3.6 and exact lower Bernoulli values to prove that every prime divisor of each smaller modulus supports an actual stable system with the entire Eisenstein residual triple. This strengthens the finite-prime gcd observation and keeps admissible deformation-source realization separate.

`check_dual_hecke.py` tests both minuscule directions at each of seven and thirteen in the three higher-degree harmonic models. It records the exact coefficient-basis convention and uses only unit pivots modulo each smaller residual modulus, without a primality assumption. A primitive common kernel survives in negative swap parity for each of `e=26,28,30`, even after all four operators are imposed. Thus adding the opposite generators does not eliminate these three obstructions. The symmetric-square factor explains why both directions can carry the same Eisenstein eigenvalues.

## Reproduction

From this directory, run:

```text
python character_trace.py
python generate_cosets.py
python derive_dimension_polynomials.py
python character_trace13.py
python check_spectral_split.py
python check_dual_hecke.py
python symmetric_square_check.py
```

The character, coset, factorization, and modular-elimination code uses exact Python integers and fractions. The symbolic quasipolynomial derivation uses SymPy. The symmetric-square computation also uses python-flint for characteristic polynomials and imports the parent's audited `gl2_uniform.py` to construct the lower classical matrices. Each script writes the correspondingly named JSON evidence file. The parent's independent character and factorization replays are retained in the `root_*_replay.log` files. Large JSON integer values can exceed Python's default integer-string limit; the supplied scripts explicitly disable that limit.

## Audit boundaries

`CHECK_EVENTS.tsv` distinguishes newly proved statements, fresh source-scope checks and carried inputs. Model effort was not exposed and is recorded accordingly. `PRIMARY_LOCATORS.tsv` gives exact primary locators and reading depth. `source_retrieved.json` records pinned source URLs, hashes and retrieval provenance.

The closed OneChar implication is a direct extraction from the pinned source proof terms, documented separately by the `lean_chain` audit. No complete Lean rebuild, independent reproof of the trace formula, or rerun of the large published Vandiver computation is claimed.

The full stable/endoscopic decomposition is proved for every even Harish–Chandra degree used here. The all-weight elimination of large prime factors of comparison integers remains separate from these exact spectral and size formulas. The constructed symmetric-square family contains stable cuspidal parameters and must retain its arithmetic source conditions; its classical origin alone is not a reason to remove it from the rank-three comparison.

## Host sign and actual points

`host_sign_results.tex` proves the precise tangent-sign distinction, a complete ordinary-component bridge, and actual TypeI/TwoPt realization for the ordinary adjoint families. The parent and independent geometry/source sibling read the entire proof and its exact source interfaces and passed it; the sibling also read and freshly replayed the entire matrix certificate. The theorem is promoted under its explicitly retained component and automorphic inputs. The normalized global polarization, finite-ramification split residual lattice, coefficient order, and inert local case are explicit. `host_sign_matrix_check.py/json` verifies sixteen exact matrix identities; it does not certify the deformation-theoretic proof. The pinned additional source files and retrieval history are in `host_sign_source/manifest.json`.

## Integral projector and exact Selmer scope

`projector_results.tex` gives a source-located audit of the existing length proof. Its auxiliary Rees ideal squares the weight-one equations; reduced generic point detection occurs only after inverting the coefficient DVR. Two elementary examples distinguish a fixed generic point from vanishing integral odd cotangent. No counterexample to the source's stated length theorem is claimed.

The same section proves that the prescribed local component is the integral ordinary framed ring `O[[12 variables]]`, and constructs an actual involution on the normalized global ring through a Cayley change of marked slice. This gives an unsquared odd cotangent presentation and a maximal-minor criterion. It also identifies the odd normal Galois module along an adjoint point as the quadratic twist of the normalized symmetric fourth plus the scalar line. A separately conditional norm-transfer lemma specifies the finite-flat integral comparison required to turn branchwise normal Jacobians into a global length bound. Those additional hypotheses have not been established for the source.

`projector_selmer_equivalence.tex` proves the reverse map: the odd weight-minus-one cotangent is exactly the Matlis dual of the original rational strict Selmer module. The proof checks the actual modulus `N=2`, uses divisible coefficients for the extra decomposition group at two, and checks the finite-coefficient local condition at ell separately. Consequently the minor criterion is an equivalent formulation of the original Selmer vanishing problem. **No evaluated minor, stricter arithmetic gate, all-weight vanishing, or removal of an adjoint branch is claimed.** Both independent siblings have passed the complete projector and equivalence proofs and their exact source interfaces. The parent has integrated these sections and compiled the assembled document successfully.

`projector_matrix_check.py/json` verifies sixteen exact Cayley, Jacobian, eigensign, and elementary cotangent identities. The sibling independently replayed a byte-identical copy and reproduced the whole JSON. This certificate does not automate the deformation or Selmer proofs. The additional pinned files are recorded in `projector_source/manifest.json`.

`projector_flatness_audit.tex` verifies two hypotheses of the conditional norm-transfer tool: the actual homogeneous fixed-locus weight-zero algebra is finite over the coefficient DVR, and its weight-minus-one conormal is a finite module surjecting onto the Selmer cotangent. Its explicit counterexample shows that even a finite flat reduced ambient algebra may have a fixed-locus quotient with vertical torsion. The parent and independent geometry/source sibling read the entire proof and exact generation/finiteness source theorems successfully. No flatness or generic-support theorem for this actual quotient has been established.

## Evaluated Hecke separation and its limit

The new `hecke_normal_results.tex` derives an integral all-prime consequence of the three previously computed complementary-factor units. At every prime divisor of the smaller residual modulus for `e=26,28,30`, the stable Hecke order localized at the full Eisenstein residual character has equal opposite minuscule generators at every split prime. All of its generic cuspidal factors belong to the constructed symmetric-square subspace. `hecke_normal_audit.py/json` saves six small modular evaluations and explicit Bezout certificates, using the already reviewed polynomial arrays.

This section also proves that every actual odd Selmer first-order deformation has unchanged characteristic coefficients at every element of `G_E`. Restriction of those derivations to trace coordinates is the zero map. An integral trace-algebra comparison therefore still requires separate off-diagonal extension or generalized-matrix-algebra data to control the Selmer cotangent. At an actual split-residual adjoint lattice, the full trace-algebra discriminant has valuation at least twelve; characteristic-zero irreducibility does not give a unit integral matrix-recovery determinant. Exact primary-source checks of Hida–Tilouine and Zhang identify a failed residual-image hypothesis in their congruence-ideal comparison theorems. These are precise scope results and an evaluated Hecke separator, **not a stricter Selmer bound**. The independent source-audit sibling read the entire section, code, and relevant primary hypotheses and passed them; its fresh six-certificate replay reproduces the JSON byte for byte. See `../lean_chain/HECKE_NORMAL_REVIEW.md`.
