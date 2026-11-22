# Complete independent review: the constant proper parameter-surface bound

**PASS for PS.1–PS.4, with the boundary-node limitation in PS.5 retained. Auxiliary mechanism; no main-gate movement.**

Reviewer: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, `/root/frobenius_continuation`; effort setting not separately exposed.

I read the entire `notes/ROOT_PARAMETER_SURFACE_LIFTING_RESEARCH.md`, including every displayed algebraic identity, its stated hypotheses, boundary limitation and source ledger. Reviewed SHA256: **0dc020da082477088e517dee73aa0bd4c816cc65dac10cdb9b9de5f962ee94a6**.

## Independent proof reconstruction

Relative Serre vanishing on the coherent sheaf mV supplies the closed-fibre section lifting required in PS.2. A generated bundle of rank at least three on a smooth closed surface admits a nowhere-zero general section by the incidence estimate; properness over local R makes its actual zero scheme empty. This gives the stated reduction of a vector bundle class to lines and one rank-two bundle, with a locally free quotient at each step.

A sufficiently high rank-two twist admits a section with finite transverse closed-fibre zeros. The two relative derivatives are independent there; the zero scheme is consequently etale over R near its entire closed fibre. Its non-etale locus is closed in that proper scheme, so the same local-base argument removes it globally. Thus the zero scheme is finite etale. Its immersion in the smooth relative surface is regular of codimension two, so the Koszul class is perfect without assuming regularity of R. Simultaneously transverse pairs of sufficiently positive line sections give the analogous finite complete intersections.

A finite algebra over local R is semilocal. Every finite projective module is determined by its locally constant rank, using the same CRT/Nakayama argument as for rank-one modules componentwise. Because a rank-zero class on the connected product restricts to rank zero on every component of a finite support, it restricts to zero in K0 of that support. The perfect projection formula therefore gives I G=0 exactly, and every line twist of a generator of G is unchanged.

I checked the Cartier twists in PS.3 explicitly. If D+ is the zero divisor of M H^a and D− that of H^a, then

    [M][O_D+] − [O_D−]
      = [M](1−[M]^−1[H]^−a) − (1−[H]^−a)
      = [M]−1.

Thus the displayed identity is exact before restricting to any finite support. Pairing this formula for two lines produces four finite complete-intersection classes; all twists disappear there. The same proof handles a square by making independent section choices.

For rank two, c(V)=detV−[V]+1 is gamma²([V]−2). The Koszul class of a transverse section of W=V H^n becomes c(W) after multiplication by detW; this twist is trivial on its finite semilocal zero support. Writing h=[H^n] and d=detV−1, direct expansion gives

    c(W)=h c(V)+h(h−1)d+(h−1)².

Hence c(V) belongs to G. The equality [V]−2=d−c(V) then generates I by line differences and G; I²⊂G and I³=0 follow from I G=0. Each finite-intersection generator is itself a rank-two gamma² Koszul class, so G⊂Fγ². Finally, inverses of the series 1+xz+cz² have no coefficient of degree at least three: x³=xc=c²=0. Products of the line and rank-two gamma series therefore prove the full Fγ³=0 assertion, not merely I³=0, and also Fγ²=G.

For the Adams calculation, with formal roots a,b,

    psi² c(V)=c(V)(a+1)(b+1)
             =c(V)(detV+[V]+1)
             =4 c(V),

because the difference between the bracket and 4 has rank zero and annihilates G. The successive quotient eigenvalues 1,2,4 yield the exact annihilating polynomial A(X)=(X−1)(X−2)(X−4), without a semisimplicity hypothesis. FF applied to the fixed proper parameter S then proves every weight-three K1 class lifts, since A(8)=168, and proves injectivity on the weight-three K0 kernel as stated.

## Useful polynomial refinement

The proof gives a slightly more flexible form: for **every** actual eta in K1(E×S)_Q, A(psi²) eta lifts to K1(Z×S)_Q. Its FF boundary is A(psi²) of a class in K0(R×S), hence zero. The K1(S) term is absorbed by its actual pullback. Thus a family need not first be globally pure weight three; an already exact pure weight-three endpoint is merely multiplied by 168. This refinement changes no boundary-decomposition claim.

## Source scope and unresolved step

The exact first-jet/section and perfect-pushforward inputs are the previously complete AE/WP audits. I freshly reread the full Stacks062Y,02UP,02LS statements and printed proofs in the NK audit, and directly reconstructed the semilocal argument. The finite-projective/perfect comparison is TT Corollary3.9 and Proposition3.10; their complete displayed statements and printed proofs were freshly read at20:16UTC. TT's reduction lemmas referenced there are part of the prior audit, not newly fully reread here. The FF KST/GH/TT exact sequence is reused at its stated characteristic-p fixed-product scope.

The node term in supported localization is not removed by this bound. No general singular purity, normalization decomposition, tensor-exterior injectivity, or symbolic-parameter lift follows just from PS.1–PS.4. PS.5 correctly leaves that precise gate unresolved. No numerical experiment was used or needed for the general integral argument.

Saved: 2026-11-19T20:20:25.443452+00:00.

## Complete C.3bw TeX transfer check

At 2026-11-19T20:26:57.707538+00:00, I read the entire final transfer in `sections/C3_parameter_surface_lifting.tex`, SHA256 **8a82168ce70a95f7abc9d01a12b1489ac72ed0702b3578771fbcb0f986e3106a**, and independently rechecked all PS.1–PS.8 displays. The expanded uniform first-jet argument uses the finite flat first infinitesimal neighbourhood of the diagonal in S×S and relative Serre vanishing; the bad rank-two jet incidence has codimension three before the point varies, so its image is proper. Every substantive step is a faithful complete transfer. The whole-class A(psi²) variant is included correctly. **Mathematical PASS.** Only typographic spacing in by1/by2/by4/eigenvalue8/by168 was reported to root; no mathematical change requested. This receipt does not claim inspection of the root master PDF.

## Final exact typography-diff receipt

At 2026-11-19T20:31:17.149020+00:00, final TeX SHA **d156557522206f5d5d92ceb249b658443d4cc6959989673472db9ef83293b27a** was checked by reversing only the five reported prose spacing/math-delimiter replacements. This reconstructs byte-for-byte the completely read source SHA **8a82168ce70a95f7abc9d01a12b1489ac72ed0702b3578771fbcb0f986e3106a**. Both multiplier occurrences are correctly `by $168$`. No mathematical or proof prose content changed. Final-file mathematical PASS retained.
