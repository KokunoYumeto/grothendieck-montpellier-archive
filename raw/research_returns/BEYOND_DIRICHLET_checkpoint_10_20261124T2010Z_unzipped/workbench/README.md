# Cubic Kummer arithmetic and real zeros of S5 Artin functions

This workbench contains two main research papers and their complete proof companions. The main analytic target is

\[
L(s)=\frac{\zeta_{\mathbb Q(\sqrt[3]{269})}(s)}{\zeta(s)}.
\]

**The Riemann hypothesis for this function remains open.** The arithmetic K-group calculation is proved, and four explicit S5 fields have rigorous real-nonvanishing certificates. The general S5 automorphy criterion still has an off-central real-zero condition. The papers distinguish these proved conclusions from the estimates that remain to be found.

This is an editable, unfiled version. No public work number, remote deposit, or publication is asserted. The permanent local statement tags are preserved in the registers; an owner-assigned WB number can later be added through a crosswalk. The current checking and build state is described below, with dated details in `RESUME.md` and `LEDGER.md`.

## Start with the two main papers

### Paper I: exact K-groups and arithmetic certificates

[The 3-primary K-groups of Q(ω, cube-root(269)) in every degree](papers/paper_I/main.pdf) gives a full proof and exact finite witnesses. For E=Q(ω, cube-root(269)), λ=ω−1, and every e≥1,

\[
K_{2e}(\mathcal O_E)\{3\}\simeq
\mathbb Z_3[\omega]/(\lambda^{\kappa(e)}),
\qquad
\kappa(e)=5+2v_3(e)+[e\equiv2\pmod3].
\]

The ordinary 3-class group is zero. The matching strict Selmer length is 4+[e≡2 mod3], and its weight-zero value is zero. Fresh logarithmic class, genus, ray, unit and action certificates support the proof; the ordinary class group Cl(E)=C7×C7 is also established by a second computational route.

The complete seven-primary appendix proves the faithful cyclotomic module Z7[[T]]/(7,T), so the matched strict length is exactly one at every weight. Its aggregate contribution is 2(T−1)log7. A separate one-prime module has a linear characteristic factor and moving-center valuations; it must not be confused with the constant strict length. The main paper prints these proofs and their exact finite data, without requiring another manuscript.

### Paper II: real zeros and Artin's conjecture

[Real zeros and Artin's conjecture for some S5-extensions, after Calegari](papers/paper_II/main.pdf) begins with the precise comparison to Calegari's theorem. It permits a central zero of arbitrary order and proves a common-real-zero criterion using two explicit quadratic Hecke quotients. Every possible off-central comparison pole must be a zero of both quotients, with the stated multiplicity bound. The published Pilloni–Stroh input removes the former auxiliary local-five restriction.

The full argument from Cohen's idempotent theorem is written in prose and then proved. Exact algebra and separately written MPFR/Arb interval calculations certify the required real nonvanishing for quintic discriminants **8249, 30301, 48976, and 60061**. The estimates apply to the whole real critical interval; they are not inferences from sampled numerical values. The paper also proves the limitations of the off-central boundary argument and the precise scope of possible symmetric-square and Asai comparisons. The proposed third Dedekind-zero condition is redundant relative to the existing Artin-factor variant.

## The cubic estimate and what the further work establishes

The cubic theta kernel is strictly positive on its required real range. Mellin inversion and the functional equation prove positivity of the completed L-function on the real axis, including a nonzero central value. This does not locate its nonreal zeros.

The main analytic reduction is a balanced two-ideal inverse convolution with a strictly smaller joint rational-content support. With separate zero-free inputs β for the cubic Hecke function and ρ for ζ, the proved tail exponent and cutoff are

\[
a=2\beta-\rho/2,\qquad
\gamma=\frac{\beta-1/2}{2\beta-\rho/2}.
\]

The proof needs no additional mixed real-part condition. With the named external theorem giving β=ρ=B*=0.873345856106718576801…, the cutoff is γ=0.284992750196395…. With ρ=1/2 it is γ=0.249447399928862…. The remaining signed arithmetic expression still lacks its square-root bound. The external analytic zero-free theorems are explicitly identified inputs; their complete proofs are not claimed as newly verified here.

The all-mixed Euler calculation proves that a full holomorphic content tube meets genuine quarter-line poles. A complete grouped-residue subtraction has now been reconstructed separately: at cutoff γ=0.28, the bulk and single-residue contributions fit the square-root target, but the best inherited complete double-residue exponent is 0.5065405965418968. Cancellation in that complete weighted term remains unproved. Its block convergence, arbitrary-order cap collisions and exact cofactor powers are recorded in full; a proposed manuscript integration is kept separate until built.

Natural-row cubic moments admit the fixed character, but fixed-row extraction, full cube-deletion reconstruction and shifted amplification retain their complete length costs. A separate comparison with polar-subtracted Gauss means identifies a vanishing source polar term, a still-present TypeII cost, and a coupled cubic phase. These are precise applicability results, without a stronger cubic estimate.

The structural comparisons also distinguish an arithmetic representation from a bound for its Frobenius traces. The Borger category theorem requires **finite localizations Z[1/N]**. The earlier unrestricted wording is preserved as refuted and superseded; over Q it admits immediate counterexamples. The fixed cubic fiber, relative Frobenius lifts, Dickson normalization, finite-kernel averages, Kummer factorizations, growing-CM host obstructions, and theta-transport identities each have their own exact scope.

## Paper and companion index

Every PDF below is accompanied by its editable main TeX file, all local inputs, a BUILD file and a deposit sheet. `papers/PROJECTS.json` is the authoritative list of current manuscripts. The older `research/cubic_k_long_proof/` is preserved proof history and is not a second current edition of Paper I.

| Project | Main subject | PDF |
|---|---|---|
| Main Paper I | All positive even 3-primary K-groups; full seven-primary appendices | [Paper I](papers/paper_I/main.pdf) |
| Main Paper II | Common-zero automorphy criterion and four interval certificates | [Paper II](papers/paper_II/main.pdf) |
| Seven-primary extract | Full strict cyclotomic stability proof | [Extract](papers/paper_I/supplement_seven/main.pdf) |
| Cubic analytic tests | Theta positivity, signed squares, prime windows, composites and shells | [Analytic tests](research/cubic_analytic.pdf) |
| Structural comparisons | Borger descent, lifts, phases, kernels and Kummer factors | [Structural comparisons](research/structural_comparisons.pdf) |
| Auxiliary-prime consequences | Conditional primes, algorithms and exact AM promises | [Consequences](research/cubic_followup.pdf) |
| Seven-adic weight profiles | Stability, universal norms and local specialization corrections | [Selmer profiles](research/selmer_weight_profiles.pdf) |
| Other imaginary quadratic fields | Q(i) arithmetic and real positivity; the discriminant−23 comparison | [Test cases](research/imaginary_quadratic_tests.pdf) |
| Switched logarithmic convolution | Small direct factor, smooth logarithmic cutoff and exact remaining sum | [Switched convolution](research/cubic_switched_convolution.pdf) |
| Rational content | Scalar content tail and primitive coefficient formulas | [Rational content](research/cubic_rational_content.pdf) |
| Balanced fixed k | Complete balanced convolution and coefficient accounting | [Balanced identity](research/cubic_balanced_fixed_k.pdf) |
| Joint content | Two-input contour theorem and strict support reduction | [Joint content](research/cubic_joint_content.pdf) |
| CM hosts | Literal size, conductor, prime-norm and projection comparisons | [CM hosts](research/cubic_cm_hosts.pdf) |
| Equivariant transport | Coherent transported copies and the missing arithmetic intertwiner | [Theta transport](research/cubic_equivariant_theta_transport.pdf) |
| Quadratic-polynomial comparison | Exact coefficient and range mismatch for a proposed TypeII input | [Quadratic comparison](research/cubic_gmpp_obstruction.pdf) |
| All-mixed Euler factors | Normal convergence, content poles and meromorphic continuation | [Euler factors](research/cubic_all_mixed_euler_factors.pdf) |
| Natural-row moments | Fixed-character applicability, deletion reconstruction and amplifier costs | [Moment comparison](research/cubic_moment_limitations.pdf) |

## Proof, computation, and review records

- `STATEMENTS.tsv`: permanent statement tags, current status, proof and checks.
- `CHECK_EVENTS.tsv`: every check with its true type, model, date and scope; older events remain visible.
- `CROSSWALK.tsv`: printed statements, permanent local tags, earlier tags and evidence.
- `DICTIONARY.md`: the findings in the language of schemes, λ-rings, K-theory, motives, correspondences and weights.
- `QUESTIONS.tsv`: all34 research questions, their current gates, work completed and next mathematical steps.
- `SOURCES.tsv` and `LITERATURE.md`: primary citations, addresses, inspected payload hashes, exact reading scopes and dated searches.
- `programs/`, `certificates/`, paper-specific `programs/` and `evidence/`: original reproducible implementations and their outputs.
- `reviews/`: frozen statement-only reconstructions, clearly distinguished author-exposed checks, failures/corrections, build receipts and visual reviews.

Published inputs are cited, not copied. The third-party software and source-paper cache are outside this deliverable. An imported theorem, a finite certificate, an independent derivation and a targeted review are different kinds of evidence and are labelled separately.

## Building and reproducing

Use each paper's BUILD file for its exact commands and arithmetic expectations. Standard pdfLaTeX packages suffice; bibliographies are inline or local. The portable coordinator

```sh
python3 programs/build_papers.py --engine pdflatex --output build --jobs 4
```

makes fresh project copies and records each input hash, reference stabilization, warnings and overfull boxes. It deliberately does not claim visual inspection. PARI/GP2.19.1, Python3.12, Sympy1.14.0 and python-flint0.9.0 were used for the recorded arithmetic. Their exact roles and finite certificates are stated beside the programs.

## Current completion boundary

All17 current papers have freshly compiled matching source/PDF pairs after the coordinated opening revisions: **295 pages**, stable references, and no overfull boxes. These are working drafts before the final printed provenance and final page-by-page review. The content-residue and Gauss-comparison extensions are being integrated in separate stages. A fresh statement-only structural proof is underway; the older cubic analytic and natural-row applicability main statements have identified independent-check obligations that remain to be completed. No all-checks-complete claim is made for this state.

The actual19:39UTC progress review recorded no movement, the first consecutive such review. The next actual review is20:39UTC. The research stop rule has not yet been reached. Checkpoints continue every45minutes; no earlier checkpoint is modified. `RESUME.md` contains the exact continuation instructions and dated receipts.

## Attribution and rights

The mathematics, text and original code were produced by GPT-6 Astra in ChatGPT Pro mode. Separate workers of the same model performed the checks recorded here; inherited checks by other named models are attributed only within their documented scopes. No human has checked this work. Original text and programs are dedicated to the public domain under **CC0 1.0 Universal**. Cited publications retain their own terms.
