# Independent audit: proper parameter-surface gamma bound and weight-three lifting

**Verdict: PASS for PS.1–PS.4; PS.5 remains an explicitly unresolved boundary route. No main-gate movement.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed.

Read the entire root note `notes/ROOT_PARAMETER_SURFACE_LIFTING_RESEARCH.md`, current SHA256 **0dc020da082477088e517dee73aa0bd4c816cc65dac10cdb9b9de5f962ee94a6**, including the node limitation and full source ledger.

## Exact checks

The relative Serre construction permits arbitrary sufficiently high closed-fibre first jets. A rank at least three section has no zeros on the closed surface; properness over the local base then makes it nowhere zero on the entire product. It removes a line subbundle with locally free quotient, leaving line bundles and rank-two bundles as additive generators.

For a rank-two bundle, the two transverse closed-fibre equations have invertible relative Jacobian. Their zero scheme is étale near every closed-fibre point, and the proper-local argument removes the entire non-étale locus. It is finite étale by properness and quasi-finiteness. Such an immersion into the smooth relative surface is regular of codimension two even if the base ring is singular. The same checks hold for the finitely many simultaneous complete intersections of line-bundle sections. Finite algebras over the local base are semilocal, so rank-zero virtual classes restrict to zero. Perfect projection formula therefore gives I·G=0 exactly.

I independently expanded both identities used in PS.3. For D+ from M H^a and D− from H^a, the equality [M][O_D+]−[O_D−]=[M]−1 is exact. Multiplication of two independently chosen such expressions yields finite transverse intersections with trivial line twists, including a square of a line difference. For rank-two V, c(V)=detV−V+1 and

    c(V tensor H^n)=h c(V)+h(h−1)(detV−1)+(h−1)^2.

Its transverse Koszul class is c(V tensor H^n) because the determinant twist is trivial on the finite semilocal zero scheme. Hence c(V) belongs to G. Conversely every stated finite generator is a rank-two Koszul gamma-two class. Thus Fγ²=G, I² is contained in G and I³=0.

The gamma-series argument is needed beyond augmentation nilpotence and is correct: line factors have degree at most one, rank-two factors degree at most two with degree-two term in G, and inverses have the same truncation because every possible higher term contains I³ or I·G. This proves the integral Fγ³=0 statement.

For the polynomial assertion, splitting into line roots verifies

    ψ²c(V)=c(V)(detV+V+1)=4c(V),

since the correction belongs to I·G. The actions on the successive rank, I/G and G quotients are1,2,4. The product (ψ²−1)(ψ²−2)(ψ²−4) therefore annihilates all of K0 on the actual product, without requiring a splitting. Naturality in the fixed-product FF exact sequence and A(8)=168 then give the weight-three K1 lift and the stated K0 kernel injectivity over Q. The K1(S) contribution is already supplied by the actual projection from Z×S.

## Source and scope boundary

The complete statements and displayed proofs of Stacks062Y,02LS,02UP were freshly read in this reviewer's immediately preceding NK audit; the exact retrievals are turn877337893view0–2. The complete AE and FF proof fragments were freshly reread in the same continuation. Their previous TT/Weibel/KST/GH external audits are reused explicitly; not every foundational primary proof has been reopened here. The semilocal module and lambda identities are reconstructed above. No numerical run is needed or claimed.

PS.5 has not been proved. In particular, the proper-surface polynomial gives no supported dévissage at intersections of boundary components and does not eliminate the shifted negative-K node term. The current proof does not turn arbitrary component HK endpoint data into an actual exceptional family or alter the remaining UK.7 quotient.

Receipt saved: 2026-11-19T20:18:22.992172+00:00


## Complete TeX transfer audit and later typography confirmation

I freshly read the entire integrated proof in sections/C3_parameter_surface_lifting.tex at SHA256 8a82168ce70a95f7abc9d01a12b1489ac72ed0702b3578771fbcb0f986e3106a. Full mathematical transfer PASS: integral gamma-three vanishing, gamma-two identification, every exact identity, actual finite etale supports, Adams polynomial, whole fixed-surface K1 lift, weight-three K0 kernel injectivity, and the explicit unproved nodal boundary all agree with the previously audited proof. No main gate is changed.

Root subsequently made typography-only changes to the displayed eigenvalues and occurrences of 168. I checked those lines and confirmed the resulting file hash d156557522206f5d5d92ceb249b658443d4cc6959989673472db9ef83293b27a. This latter check is a typography/hash confirmation, not a newly claimed independent mathematical reproof or a new external source reading. The full-read receipt remains attached to the former 8a82168c hash.

Transfer receipt saved: 2026-11-19T20:33:11.735320+00:00
