# Task 2: completed branch

## Status

NX-L01–NX-L07 are written in full in `findings.tex` and have received an entire final author rereading. The corresponding events specify their actual scope: targeted proof checks, not independent re-proofs or formal certificates. Root has also reported an entire reading of the first six. The separate reviewer `/root/cm_effectivity` read NX-L02 in full twice, reconstructed its delicate local arguments, and found no remaining gap; that review and its own event are in `../cm/lambda_L2_review.md` and `../cm/CHECK_EVENTS.tsv`.

The mathematical outcomes are:

- **NX-L01:** the literal flat finite-type conjecture is refuted. Doubling affine space along the complement of an arbitrary vertical closed subscheme gives a nonseparated Lambda-scheme whose extra bad factor is that subscheme's zeta function. The explicit affine elliptic curve over F5 has correction `(1+2t+5t^2)/(1-5t)`.
- **NX-L02:** for a proper flat Z_p-model with a single Frobenius lift, special finite-coefficient cohomology is the colimit of generic cohomology under that lift. Its rational cohomology is a G_Qp-stable direct summand of the generic cohomology.
- **NX-L03:** therefore proper flat global Lambda-schemes have actual semisimple Artin–Tate cohomology at every bad prime, including a noncanonical derived splitting. This is stronger than a virtual determinant identity, but it asserts no motivic or cycle projector.
- **NX-L04:** multiplicities and the full inertia-invariant generic cohomology need not survive. For mu_p the generic, inertia-invariant, and special H0 dimensions are p, 2, and 1; the finite correction is `1-t`.
- **NX-L05:** the vertical blowup of P2 along a smooth plane elliptic curve has no Frobenius lift: special H3 is H1(E)(-1), while generic H3 vanishes.
- **NX-L06:** under the stipulated Alpöge theorem A, every non-real divisor of the zeta function of a proper flat Lambda-scheme lies on a half-integer line. Global Dirichlet–Tate divisors are on j+1/2; actual local and correction divisors are on integral lines. NX-L01–05 and NX-L07 require neither A nor Masullo M.

- **NX-L07:** cyclotomic number-ring local factors do not imply a Lambda-structure; Z[zeta5] has no Frobenius lift at5. Its elementary argument is now a separately identified proposition.

## Essential qualifications

Borger's definition is on schemes/spaces without separatedness: introduction p2 and §1.1 p6. He explicitly adds separatedness before §6 Theorem6.1 and Corollary6.2. Thus the nonseparated counterexample answers the question as literally written. A separated nonproper amendment is a different question and is **not** settled by this work. The proper argument needs proper formal/algebraic comparison; no Lambda-equivariant compactification theorem is assumed.

DP_MULT DP11 is the binomial / identity-Adams special case, not a criterion saying all Lambda-rings are binomial. Ramified abelian integer rings have the stated cyclotomic local factors but need not admit Lambda-structures: Z[zeta5] cannot lift Frobenius at5 because every endomorphism is automorphic and the mod5 Frobenius is not. This qualification is proved as NX-L07 in `findings.tex`.

## Main local proof and repaired hazards

The formal Frobenius tower has local completed ring W((A/p)^perf). After completed scalar extension to O_C it is perfectoid; its tilt is the perfection of the constant special-fibre model. The proof explicitly checks p-torsion-freeness, flatness over the valuation ring, Frobenius modulo a pth root of p, plus-ring matching, principal formal opens as rational domains, compatible bounded valuations, and Galois equivariance. The characteristic-p proper comparison is first performed over the noetherian base Fp[[u]], then base-changed, so no noetherian Huber theorem is silently used over O_Cflat.

The final rational comparison uses an integral Fitting projector `e=lim T^(n!)` and a uniformly bounded torsion remainder from universal coefficients. The false shortcut `colim with Q_l = rationalized finite-coefficient colim` is not used: T=l on Z_l disproves that shortcut.

## Approaches tried and their exact limitations

1. **Proper base change alone:** insufficient to identify generic and singular special fibres. The mu_p example refutes even equality with generic inertia invariants.
2. **Vertical elliptic blowup:** a naive ambient Frobenius lift pulls `(p,F)` back on the chart p=Fv to `F(v,F^(p-1)+vg)=F(v,F^(p-1))`, which is not invertible along the regular crossing F=v=0. NX-L05 strengthens this obstruction to every potential endomorphism of the blowup, regardless of whether it descends to P2.
3. **Direct rational colimit:** invalid for l-divisible nonzero eigenvalues; repaired integrally as above.
4. **Fixed-point trace/Lefschetz route:** might establish trace identities, but on its own does not identify the lifted-endomorphism spectrum with the Galois representation or prove semisimplicity. The tower gives the needed actual stable summand.
5. **Extension to separated nonproper schemes:** the invariant formal domains need not cover the entire algebraic generic analytification without properness. An equivariant compactification with controlled boundary would be a new theorem, not an automatic application of Nagata compactification.

## Sources and audit limits

Exact source locators are in `bibliography.tex` and `SOURCES.tsv`. The source statements actually read and the inherited background are separated in `CHECK_EVENTS.tsv`. The SGA and archive locators are carried from the supplied checked predecessor. No new archive scan transcription is claimed. The main analytic inputs are Scholze's *Perfectoid spaces* (the primary author PDF) and Huber 1994 Remark4.6(iv)(d); their cited theorems are not re-proved here.

An entire journal issue was downloaded under the misleading working name `Ito_Mieda_2020.pdf/.txt`; only Imai–Mieda Lemma3.3, p408, was consulted as a corroboration. It is unused in the proof and should be omitted from the final source bundle if size matters. The primary Huber paper suffices.

No independent final deliverable was written outside this task directory; root handles integration and final saving.
