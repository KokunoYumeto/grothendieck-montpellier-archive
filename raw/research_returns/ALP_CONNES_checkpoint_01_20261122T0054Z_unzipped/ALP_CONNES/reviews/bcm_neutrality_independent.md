# Independent whole-proof review: BCM and neutrality module

Reviewer: /root/sites_twistor. Model: GPT-6 Astra Pro. Effort: inherited; not separately observable. Review scope: every statement and proof AC-B01–AC-B06 in modules/bcm_neutrality.tex as read in this run. Check type: targeted proof check by an independent reviewer, not a claim to have independently re-proved the foundational KMS classification, Artin formalism, or CM class-field theorem.

## Verdict

The six mathematical arguments pass. Two Yalkinoglu source locators require correction in the supplied source version; they do not change the mathematics. No main analytic gate is closed by these results.

## Exact locator corrections

The provided sources/LIT_Yalkinoglu_BC_arithmetic_models/new_version_bck.tex places equation `arithalg` in **§6, The endomotive E_K**, not §4. The label `kmsinfty` is **§1.2, Classification at beta=infinity**, not an equation in §2.1. Its ground-state evaluation is an unnumbered display. LLN Theorem2.1, source `mainthm`(iv), independently and directly supplies the stated ground-state result.

## AC-B01

The trace expansion is absolutely convergent for Re(s)>1, including conductor-zero convention. Restricting the basis without phase insertion gives exactly zeta_F times the deleted finite Euler factors. Their zeros lie on Re(s)=0; abelian factorization transfers A to zeta_F in the open critical strip. The physical heat trace remains divergent below or at beta1. For the restricted positive series, divergence at beta1 follows from the nonzero finite Euler factor multiplying the pole; for smaller positive beta it follows termwise. The argument does not conflate analytic continuation with a trace-class heat operator.

Read LLN `mainthm` in the supplied source: uniqueness for0<beta<=1, Gal(F^ab/F) indexing for beta>1, and ground-state=KMS_infinity evaluation are stated exactly. Read HP §8.2 and preceding Dirichlet discussion: its infinity-trivial hypothesis and unresolved nontrivial-infinity remark support the module's even-character qualification.

## AC-B02

The diagonal projection values prove failure of positivity on B(ell2): chi5(2)=-1 and L(beta,chi5)>0 for beta>1. Three distinct cubic phases cannot simultaneously be nonnegative real under a fixed nonzero scalar. The text correctly confines the counterexample to that full trace domain and does not claim every restriction to a smaller algebra fails. Insertion does not change H, so no zero eigenvalue conclusion follows for this Hamiltonian.

## AC-B03

The finite algebra injection from AC-K03 is contravariant to the verified Deligne–Ribet quotient; the unit factor embeds E_p in its ray field and all other factors receive K. The observable (alpha,0,...) and boundary idempotent have the componentwise relation a^3=p e, with finite support/value range and hence boundedness. Boundary evaluation gives the three values by Galois action.

Read Y `arithalg` and `kmsinfty`; their content agrees, after correcting section locators. Read CMR `Kground` and `FtauKab`: values regular at tau generate K^ab. The module appropriately presents the CMR radical value as an existence/rational-expression conclusion, not an explicit modular function, and does not infer an estimate of H04.4.

## AC-B04

The sign convention is consistent. The infinity component is (z/|z|)^(-k); triviality on global units forces the finite unit value epsilon^k. The ideal formula r_pi(alpha)^(-1)*(alpha/|alpha|)^k is invariant under replacing alpha by epsilon*alpha and gives the desired local component r_pi. Finite-image continuity on C^times forces a trivial infinity component.

The cubic residue formula at omega gives descent iff N(pi)=1 mod9. The reduction mu6 -> (O_K/(3))^times is bijective because -1 and omega have orders2 and3 and the target has6 elements. The unique correcting cubic character is nontrivial on the order3 principal-unit subgroup, so its lambda-conductor is lambda^2=(3), not lambda. The other conductor remains pi. The finite correction and angular correction are distinct; the latter is infinite order. All edge cases pi not dividing3 are handled.

## AC-B05

Both norm signs are correct. Phi3 roots at odd primes other than3 are primitive cube roots, Phi6 roots their negatives; simple roots lift uniquely. Prime2 has none. The lone root modulo3 has exact valuation1 under every lift, excluding modulo9. CRT gives exactly the stated criterion/count for arbitrary composite R.

The Fourier conjugation factor is correct: sum chi(d) conjugate chi(zeta e), then sum d,e, gives conjugate chi(zeta) times |sum chi(d)|^2. Root conditions are disjoint for the unit ratio. The adjacency matrix of the3-cycle minus its loops has eigenvalues2,-1,-1; it is nonnegative on nonnegative counting vectors but indefinite on complex vectors. Thus the counting identity does not give the proposed Weil-form positivity.

## AC-B06

The table of characters modulo12, their product on units and all-prime Artin factorization are correct; the zero-extension qualification is necessary and is present. The cyclotomic norm is Phi12 homogenized, with sign minus in the middle term.

E_p has Galois group S3 and unique quadratic subfield K, so E_p and Q(i) are disjoint and E'=E_p Q(i) has S3xC2. The identity Ind_{G_M}^{G_K}(Res chi)=chi directsum chi*eta gives the base-change L-function at all primes by Artin formalism. Restriction of the cubic character stays nontrivial on the index2 subgroup; chi*eta also stays nontrivial. Complex conjugation preserves eta and interchanges the cubic characters, so the two cyclic factors over M agree, giving the squares. Entire Hecke factors cannot cancel off-line zeros in the open critical strip. With A for zeta_M the asserted RH equivalence follows. No nonabelian factor is removed.

The non-CM-overfield conclusion uses the earlier explicitly proved obstruction AM-H03; the compositum contains E_p. The final local-purity/global-RH distinction and DELTA23 attribution gate are appropriately retained.
