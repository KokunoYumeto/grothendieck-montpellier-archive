# AN_GRH: checked paper, certificates and remaining gates

The standalone `AN_GRH.tex` and its matched PDF contain findings A01–A52, the analytic premise comparison, the finite cyclotomic certificates, explicit Galois bounds, historical-source audit, and a separate part for unchecked inputs and remaining gates. All new proofs have recorded whole-proof readings. The sixth scheduled review governs the stopping status; auxiliary lemmas and packaging do not reset the progress count.

The final verified contents include a185-page PDF,1400question rows and1391recorded check events. The build manifest records the exact source/PDF and visual-review bindings.

## Stopping status

The actual review at 2026-11-21 08:15:00 UTC recorded the second consecutive main-route review without substantive movement. All four workstreams are stopped under the requested rule. The exact review, all-row snapshot and remaining gates are under `final/reviews/` in the archive. The final mathematical state is reported below; the requested Hooley proof remains unestablished.

## Results of the four requested workstreams

| Requested work | Result reached | Remaining requirement |
|---|---|---|
| Exact cote149 A1 and proof through Masullo–Hooley | A01 states the arithmetic point-section assertion precisely. A05 gives a separate unconditional proof by the recovered cuspidal/configuration route. M implies the required Kummer Dedekind-GRH hypotheses for Hooley; the requested proof through that route remains unestablished. | A universal geometric supply theorem for allowed pointed covers, or another proved way to separate the compatible point classes. Arithmetic density of eligible orders alone does not supply it. |
| Every historically flagged analytic row | All supplied flags and all800 recovered full statements are represented;591 proof blocks were available. Exact L-function and source-scope classifications are retained. |390 full register statements and209 additional LM7 proof blocks remain unavailable. The1190 summary entries are not all fully audited proofs. |
| Finite GT cyclotomic certificates |53 identified moduli and4825 unit words are verified, together with the stated infinite families. The exact certificate proves the cyclotomic unit-coordinate claim at those targets. |The missing full GT register and actual quotient maps are needed for exhaustive original-target coverage. The applicable general Bach theorem has coefficient3; coefficient2 is checked on the stated targets and ranges. |
| Effective Galois images and trace separation |G01–G06 give explicit bounds under their precise analytic hypotheses, including the identified LM7 predicates and LM8 elliptic factors. General M-dependent statements remain conditional. |Further row applications require their actual fields, representations and ramification data. Frobenius traces determine semisimplifications, and do not recover arbitrary extension classes. |

Alpöge's Dirichlet-GRH statements are accepted as theorems exactly as instructed. They give the relevant abelian Dedekind-zeta consequences and Bach input. The supplied theorem scope does not discharge the nonabelian Kummer family needed by Hooley. A1 already holds by A05 independently of either GRH input. No logical-independence theorem about other possible deductions from Alpöge is claimed.

Masullo's all-field Hecke-GRH assertion is always treated as a draft claim. The intended final theorem heading13.3.1.2 in the supplied draft has no completed statement. Its trivial-Hecke specialization, if accepted, supplies the all-number-field Dedekind-GRH premises used here. This work does not verify that draft.

## Strongest checked reductions and limits of the main route

A46 supplies an all-characteristic, all-genus separation criterion: an allowed pointed geometrically cyclic etale cover of odd degree prime to p suffices when its actual primitive rational p-primary group vanishes. The deck group need not be constant. A45 and A47 permit bounded nonzero exponents, with explicit inequalities; for2<=g<=p these exclude a collision directly, and in larger genus they leave a precise totally ramified wild elliptic map. A52 extends the same argument to any sufficiently small integral annihilator with nonzero faithful evaluation and gives a fixed-field lattice construction of such operators. It does not establish a universal bound for the lattice index, and in the fully transitive case its uniform inequality is the earlier n>(2M−1)^2 condition.

For the characteristic-two genus-two point-section problem, A33 reduces the residual case to ordinary genus-two Jacobians with integral Rosati-invariant O5 action. This target is nonempty and proper. Canonical-primary detectors, exact examples of degrees7,13,15,19,39 and4159, and other primitive-cover tests supply particular witnesses. None proves a universal witness for every prescribed curve and point. Literal universal primitive-cover existence is kept distinct from the point-section assertion.

The unsuccessful approaches are retained with their exact failure points. A06 refutes the original universal primitive-root theta bridge. A07/A21 and A22 show generic odd-torsion avoidance and the failure of every fixed finite prime support. A23/A27 exhibit all-extension failures of older numerical tests, while existing geometric witnesses persist. A36–A43 distinguish dense good target points from the images of a prescribed reflection cover; all images of one cover can fail the detector. A44 identifies limits of constant-field towers. A48 proves why unpointed twists and connected same-conductor pullbacks do not repair a fixed pointed group. A49 supplies an exact finite-quotient Fourier test and unrestricted nonuniformity, but only one good signed packet without the missing joint conductor conditions. A50 gives an exact abstract integral-operator obstruction, expressly without a Jacobian realization.

A51 computes norm compatibility for the actual point classes, semilinear descent and bounded rational generator numbers. None bounds their exponents. Its Fox-matrix supplement separates arbitrary completed coefficients from a fixed rational determinant; the needed actual geometric identification is missing. The transitive-deck calculation leaves one cyclic rational torsion group with uncontrolled return valuation. The reflection-field supplement controls finite-depth constant fields and proves dense good points inside the same constant extension, without prescribed-orbit incidence. Actual ordinary principally polarized Weil restrictions show that weights, polarization, cyclic polynomial shape and one rational generator alone allow exponentially large exponents; these varieties are not asserted to be the needed Jacobian covers. A52's trace/norm boundary explains why a trace-annihilated function belongs to the lower quotient and cannot use the larger upstairs cyclic degree in the separation inequality.

The final actual-point differential calculation records a nonzero regular trace-zero form at an order jump without bounding that order. Finitely many old good packets can be preserved during further supply, but the exact noncyclic line-quotient norm calculation still does not combine them into a whole good block or a successful small operator.

These additional criteria, examples and obstructions are not by themselves counted as strict movement of the full remaining universal gate. The dated reviews preserve the precise movement decisions.

## Archive layout and required files

The final ZIP has convenient reading copies of `AN_GRH.tex`, `AN_GRH.pdf`, `QUESTIONS.tsv`, `LEDGER.md`, `CHECK_EVENTS.tsv`, `IMPLICATIONS.md`, `TRANSCRIPTION_NOTES.tsv` and this README at its root. Their identical project copies are under `final/`, together with all certificates, modular proof sources and reproduction scripts. Original supplied files are under `source/`; selected recovered texts and certificates are retained at their documented paths under `final/recovered/`.

The retained `work/` tree and historical `final/evidence/build/` tree are stored losslessly in `work_and_build_evidence.tar.xz` inside the ZIP. After extracting the ZIP, restore them from its root with:

```sh
tar -xJf work_and_build_evidence.tar.xz
```

`FINAL_CONTENTS_MANIFEST.json` binds every retained file to its path, size and SHA256 hash and identifies the actual stopping review. `RESTORE_WORK_EVIDENCE.txt` gives the same layout instructions. No earlier checkpoint ZIP is nested. Complete externally downloaded research-paper caches are excluded; exact locators, source hashes and scoped reading records are retained. The supplied inputs and selected recovered materials remain available at the documented retained paths; unselected recovery caches and transfer helpers are omitted.

Run the reproduction examples below from `final/`, treating each code block as a fresh shell in that directory. Run regenerating commands in a working copy if the delivered evidence should remain unchanged. The standalone paper itself needs no modular source files.

## Reproduce the arithmetic

The GT and short A06 checks use Python 3 and only its standard library:

```sh
cd certificates/gt
python verify_gt_units.py
python check_unit_certificates.py
python check_lls_bound_scope.py
```

```sh
cd certificates/A06
python check_theta_obstruction.py
python verify_theta_small_independent.py
python check_a06_prime_orbit_independent.py
```

The B.23 polynomial and supplementary curve-geometry checks require `python-flint==0.9.0` (the version used in this run):

```sh
cd certificates/B23
python primitive_conductors.py
python primitive_verify.py
```

```sh
cd certificates/A06
python check_b23_geometry.py
```

Run regenerating scripts in a working copy if the delivered logs and data should remain unchanged. The supplied B.23 binary coefficient arrays and manifests are complete; the verifier checks both full Bezout identities at 191 and 229. The new A06 proof itself needs only the small arithmetic checks, not the large Bezout certificates.

The A09 direct producer and point-count checker use the standard library. Its independently written polynomial verifier also uses SymPy:

```sh
cd certificates/A09
python theta13_direct.py
python verify_theta13_norm.py
python check_base_counts.py
```

The A13 checks use the standard library, with independently computed recurrence and Sylvester-determinant group orders. The A15 unit-group checks also use the standard library:

```sh
cd certificates/A13
python lang_weil_4159_certificate.py
python verify_ordinary_4159_independent.py
```

```sh
cd certificates/A15
python check_A15_units.py
```

The A16 Taylor producer and finite search use the standard library. The independent norm verifier uses SymPy and imports no producer arithmetic:

```sh
cd certificates/A16
python construct_theta15.py
python verify_theta15_symbolic.py
python search_theta15_F8.py
```

The finite search records the specified models and points tested; it is not a classification up to isomorphism or a universal existence proof.

For A20, the producer uses a four-dimensional integer companion matrix, the independent verifier uses a polynomial resultant, and a separately written check uses Newton power sums:

```sh
cd certificates/A20
python check_three_primary.py
python verify_three_primary.py
python A20_recurrence_check.py
```

Only the second command requires SymPy. A19 supplies the geometric finite-support reduction used with these exact computations.

The optional A23 recurrence cross-check uses the standard library:

```sh
cd certificates/A23
python verify_A23_recurrence.py
```

Its finite range is an arithmetic cross-check. The paper proves the all-extension inequality symbolically.

The optional A24 and A25 checks use the standard library:

```sh
python certificates/A24/check_A24_orbits.py
python certificates/A25/verify_lang_pairing_cutoffs.py
```

A24 proves the inert-prime-power obstruction uniformly without relying on its small-prime consistency checks; A25 proves the entire cutoff ranges after the exact anchor comparisons.

The A32 and A34 character computations use two separate standard-library divisor-arithmetic implementations. Run them in a working copy to preserve the recorded outputs:

```sh
python certificates/A32/verify_A27_character13_linear.py
python certificates/A34/probe_A27_c19.py
python certificates/A34/verify_A34_conductor19_cantor.py
```

The complete point-image tables and subgroup cycles are retained. These finite checks support the written divisor/character proofs; they are not formal verification.

## Build the paper

With an ordinary XeLaTeX or LuaLaTeX installation containing standard AMS, longtable, fontspec, Latin Modern, microtype, hyperref and enumitem packages:

```sh
lualatex AN_GRH.tex
lualatex AN_GRH.tex
```

`python reproduce/assemble_paper.py` rebuilds the standalone source from `proof_sources/`. The initial missing-format failure was resolved by using the installed XeTeX toolchain with process-local search paths and an isolated format. `reproduce/compile_standalone_tex.py` records that environment-specific build procedure. No packages or fonts were installed, and no system configuration was changed.

The compiled paper and visual checks are recorded under `evidence/build/`; the manifest binds the checks to exact TeX and PDF hashes. Structural validation also checks included-source completeness, citation keys, finding/check-event coverage and retained-source hashes. Compilation and visual inspection are separate from mathematical proof checking.

## Verification convention

CHECK_EVENTS.tsv records what actually happened. A whole-proof reading is not a formal certificate. A replay of an earlier independently written verifier is not a new independent implementation. Source-statement inspection is not a reproof of a cited theorem. Alpöge's theorem is accepted as instructed; the Lean archive was not rebuilt. Masullo's all-field Hecke-GRH claim is conditional, and its intended final theorem heading 13.3.1.2 has no statement in the supplied draft.

Original handwritten scans were not provided. TRANSCRIPTION_NOTES.tsv distinguishes mathematically forced notation/typing corrections from possible authorial lapses, conventions and items requiring visual confirmation.

## Further checked real multiplication results

**The ordinary real multiplication target is now checked to be nonempty and proper.** The A13 Jacobian has an integral Rosati O5 action overF2, proved using its full two-torsion group scheme. The ordinaryF4curve y²+y=x+u/x+u²/(x+1) has geometric endomorphism field whose Rosati fixed field isQ(sqrt2), so it never enters this target after extending constants.

**A36 rules out the forced-five repair on an actual reflection quotient.** A constant pointed quintic cover of A27 overF256 has an ordinary genus2 reflection target E with #J_E=2^10*3^4. Every fixed rational canonical class and both inhomogeneous correspondence constants have zero5part. The exact identity on Pic^d is (T²+T−1)L=dF, giving b0=(T+3)a and (2−T)b0=5a. This does not exclude a3primary detector or5primary classes of new points over larger fields.

**A37 closes the finite-support proposal on this precise target.** On ordinary Hilbert–Blumenthal genus2 moduli for O5, the geometric generic Raynaud theta has no nonzero odd-order point. For every finite odd support, including5, a Zariski-dense collection of finite-field curves avoids all nonzero geometric theta points with that support, with all powers and products allowed. The proof uses the full joint integral level torsor, an inverse-different pairing at5 and exact-field Frobenius specialization. Variable-prime witnesses on an individual curve and the prescribed-image canonical problem remain open.

The A34 degree19cover also has an exact constant-degree rule: its rational2primary Prym exponent is1 if7 does not divide m,2 if7 divides odd m, and2^(v2(m)+2) if14 divides m. Its sufficient separation inequality holds exactly when14 does not divide m. This refinement alone is not counted as a new main-gate reduction.
