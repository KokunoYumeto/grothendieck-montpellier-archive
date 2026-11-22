# Independent whole-proof review of the endoscopic converse

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict and precise range

I read `evidence/unitary_audit/endoscopic_converse.tex` in full, including KT-U3-LEVEL-CONVERSE, KT-U3-ENDO-EXACT, both complete proofs, and the source-scope paragraph. The argument passes targeted proof review using the explicitly named published rank-three classification and local/global correspondences as imported theorems.

The exact dimension formula is proved for **even e>=2**, equivalently **odd coefficient degree d=e-1**. It is not a formula for every d>=0. Evenness is essential: the outer Hecke characters have value (-1)^e at the ramified uniformizer, and the exclusion argument uses that value being+1. The opposite parity requires a separate packet calculation.

No new Lean build is claimed. I did not reconstruct Rogawski's trace formula or read the entire Rogawski monograph. I did check the specific Bellaïche–Chenevier passages identifying the proved rank-three scope, the real parameter formulas, Haines's full spherical parametrization argument, and the explicit ramified principal-series cases and their applicable hypotheses.

## Sources read and exact scope

### Rank-three spectral exhaustion and real regularity

In the carried `hecke_coverage/bellaiche_chenevier_book.txt`, AppendixA.9 starts at lines11409ff. The opening paragraph, lines11418–11420, explicitly takes a unitary group that may be quasi-split or not. Lines11450–11477 give the decomposition of a discrete parameter into distinct stable constituents for a partition of the rank. Lines11478–11481 state that this spectral structure and the relevant Arthur predictions were proved by Rogawski for rank at most3. Thus the proof does not import an unproved unrestricted general-rank classification.

RemarkA.9.1, printed p.229, lines11488–11493, states the obstruction to compact regularity from a nontrivial Arthur SL2 block. Section6.7, printed pp.140–141, lines7059–7098, defines regular coefficient weight by strict inequalities and gives the exact real-parameter relation

`a_i = k_i + (m+1)/2 - i`.

For rank3 and coefficients (e-1,0,1-e), this gives (e,0,-e). A block of size2 contributes a pair with difference1, and a block of size3 contributes three consecutive entries. The displayed multiset has neither when e>=2. This proves genericity before the argument invokes the generic KMSW multiplicity formula. It also avoids confusing local L-base-change with global A-base-change in the nongeneric setting, a distinction explicitly discussed in BC AppendixA.8, lines11390–11408.

The cited Rogawski reference is BC's [Rog3], *Automorphic representations of unitary groups in three variables*, Annals of Mathematics Studies123 (1990), identified in the bibliography at lines12514–12515. The original publisher/JSTOR contents confirm Chapter13 “Automorphic representations,” pp.198–231, and Chapter14 “Comparison of inner forms,” pp.232–245. The full chapter text was not accessible in this review; the mathematical scope check used the explicit BC rank-three statement just described, not an invented Rogawski theorem number.

### Haines's spherical representation theorem

Read `evidence/unitary_audit/primary/haines_satake_parameters_v4.txt`, Section3, lines152–197, including all of the argument preceding Proposition3.1. Its hypotheses are a special maximal parahoric and a minimal F-Levi attached to the corresponding apartment. It parametrizes the spherical irreducibles by weakly unramified characters modulo the relative Weyl group. The spherical function is constructed inside the relevant principal series, so the required irreducible is a principal-series constituent.

Haines's introduction, lines17–45, separates this proved representation-theoretic parametrization from his conjecture matching Satake parameters with local Langlands. The converse proof uses only the former. It obtains the actual local base change from the explicit Adler–Lansky principal-series formulas, so no conjectural compatibility is inserted.

### Ramified group, full stabilizer, and base change

Read the carried `hecke_coverage/adler_lansky_ramified.txt` at:

- Section4.1, pp.10–11, lines467–525: from this point the assumptions are characteristic zero and odd residual characteristic; both relevant vertices are special.
- Section4.2.1, pp.11–12, lines555–563: the full lattice-stabilizer quotient is O3 and its connected part is SO3.
- Section4.4, pp.14–15, lines720–759: the inducing coordinates and all three reducibility cases.
- Proposition6.1, p.21, lines1121–1139: the complete principal-series packet list.
- Proposition7.1, p.28, lines1477–1519: the four explicit base-change cases and its proof reference to the earlier principal-series proposition.

The paper's introduction places q>3, q!=7 and a depth-preservation hypothesis on its main finite-group compatibility theorem, lines113–129. Those restrictions are not used in the principal-series classification and explicit base-change argument applied here. Section4.1's odd-residue-characteristic assumption includes the local field Q3. The proof correctly refrains from importing the main finite-group theorem at q=3.

The previously checked Langlands statements in `primary/langlands_base_change_gl2.pdf`, Section2(B),(C),(E), p.13, and Lemma11.6(b), p.142, give the middle-constituent descent and the two quadratic-twist descents. The prior ENDOSCOPIC_REVIEW.md contains the exact KMSW radical, packet-pairing and generic/pure-inner multiplicity scope checks and the rendered GGP compact-root formula.

## Local converse: deduction checked

A full-stabilizer fixed vector is also fixed by its connected special maximal parahoric. Haines therefore places the representation in a principal series. Exactness of compact-open invariants in characteristic zero makes that principal series have a nonzero full-stabilizer fixed vector. Iwasawa decomposition reduces its fixed-space calculation to the inducing character on B intersect K. The fixed space has dimension1, and the inducing coordinates satisfy lambda1 unramified and lambda2=1.

The ramified quadratic restriction in reducibility case(4.4PS–2) is incompatible with this unramified lambda1. In case(4.4PS–1), the trivial constituent already consumes the one fixed dimension, so the Steinberg constituent has none. In case(4.4PS–3), exactly one of the two constituents has that fixed dimension. All other possibilities are the irreducible principal series.

The four explicit base-change formulas then give a direct sum of unramified Weil characters with zero monodromy. In the GL2 one-dimensional constituent appearing in case(ii), the corresponding GL2 parameter consists of two unramified characters, not a Steinberg block; this distinction is needed for the zero-monodromy assertion. In case(iii), the relevant constituent is trivial and again has zero monodromy.

The unordered unramified triple has the form {lambda1,1,lambda1 inverse}; it determines lambda1 up to inversion, including repeated roots. Thus it determines the principal series up to the Weyl action. The one-dimensional fixed-space calculation shows uniqueness of the full-stabilizer member and of its fixed line within the packet. There is no unproved assertion that an arbitrary compact fixed vector automatically implies unramified base change.

## Global exhaustion checked

All finite local base-change parameters are unramified with zero monodromy. Every simple constituent therefore has this same finite-level property. The determinant has trivial infinity type and is everywhere unramified; class number1 makes it trivial.

For a one-dimensional constituent of infinity type (z/bar(z))^s, class number1 gives existence and uniqueness exactly when3 divides s. The unit obstruction is the image of mu6 under u/bar(u), which is mu3. Its local value at an inert rational prime is1. A ramified uniformizer proportional to sqrt(-3) gives value(-1)^s. Thus the two possible outer characters are trivial at all nonsplit finite places in the stated even-e range.

For a middle constituent, its character is1 and the rank-two cuspidal constituent has determinant1. Rank-two duality and conjugate self-duality give conjugation invariance, so cyclic base change supplies exactly two cuspidal descents. Their infinity type gives weight2e+1 and their central character is epsilon, rather than1, by oddness. Away from3, restriction to the unramified extension preserves inertia and monodromy, so the descents are unramified. At3 their inertia factors through the quadratic quotient, with determinant epsilon; its two characters are1 and epsilon. The conductor is exactly1. These are precisely the non-CM level3 twist pairs already constructed.

For an outer character, the global component element acts as -I2 on the rank-two constituent. At nonsplit finite places the character is trivial and that rank-two constituent has determinant1. Its reciprocal roots put the element in the connected determinant-one centralizer, in every repeated-root case as well. At a split place the semisimple centralizer is a product of general linear groups on eigenspaces; its determinant-one subgroup is connected and contains the same element. All finite packet values are consequently+1. The two constituent weights are adjacent at infinity, so GGP gives value-1. This fails the trivial generic global epsilon character and excludes the packet.

For the three-character partition, the only candidate is theta_e plus1 plus theta_-e. All three are trivial at finite nonsplit places. An adjacent pair of sign generators lies in SO3 there, and in the connected determinant-one centralizer at split places. Its finite values are+1 and its compact real value is-1. The same multiplicity condition excludes it.

These are all nongeneric-excluded rank partitions3,2+1,1+1+1. Thus the remaining endoscopic parameters are exactly the constructed middle-character ones. Uniqueness of every local fixed line, the unique compact real coefficient member, and global multiplicity1 make each contribute exactly one line. Subtracting floor((e-1)/3) from the carried D(e-1) gives the three displayed cubic formulas; the odd-degree residue formulas in KT-U3-DIM agree in all six classes modulo12.

## Source limits and outcome

The conclusion is a proof using published classification and correspondence inputs. It is not a reconstruction of the full classification, a proof of all-rank Arthur theory, or a new formal kernel certificate. Within that precise convention and the even-e range, no remaining packet-normalization, conductor, repeated-root, multiplicity, or dimension gap was found.

Reviewed proof SHA256: `7f4731cd9654282236bcf14bcbfb72f992067780cec7d5bbfeefc526c6538641`.
