# S5: newer exceptional-zero theorems and positive Rankin bounds

Date: 2026-11-21. Author/checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

Status: completed source-hypothesis checks. The full MA-RB-011 proof is now written in s5_rankin_scope.tex, tagsMA-RB.150–168, and its complete author reading has passed. Independent whole-proof review is pending. No smaller arithmetic gate, shared-zero exclusion, or arithmetic counterexample is asserted. MA-RB-008 remains current.

## Prior routes and exact issue

Read the existing quadratic-Hecke, analytic-comparison, universal-Euler and endpoint-scope notes, and MA-RB.17–26/61–69. Heilbronn simplicity, Zaman near-one regions and Ramakrishnan–Wang Sym4 exceptional-zero exclusion were already checked and are not counted again.

Comparison failure need not give a zero of A: its order n can be zero. Nonvanishing of the odd-degree GL5 standard factor alone therefore does not contradict the branch. The actual Rankin cross factor A x (A eta) has order at least4k, and X x X at least3k, by MA-RB.65. A simple-zero-only theorem can exclude gamma only in its stated region.

## Fresh primary-source hypothesis checks

Harcos and Thorner (2025), A new zero-free region for Rankin–Selberg L-functions, arXiv:2303.16889v6, Theorem1.1, printedp.3, gives sigma>=1-c C(chi)^(-epsilon), with c depending ineffectively on the fixed pair and epsilon. It supplies neither c>=1/2 nor an interval-wide conclusion. The symmetric-power discussion before Theorem2.2 onp.5 also concerns a neighborhood of1. The full introduction, exact Theorem1.1 and its remarks, and that symmetric-power setup were read. The complete21-page proof was not audited or invoked. Primary version: https://arxiv.org/pdf/2303.16889 (v6 dated29January2025).

Harcos and Thorner (2026), Tatuzawa's theorem for Rankin–Selberg L-functions, arXiv:2508.10844v3, Theorem1.1/Corollary1.4 onp.3 and Theorem1.6 onpp.4–5, give effective conductor-dependent neighborhoods of1 with at most one simple exception. The self-Rankin exceptional-character condition pi tensor chi^2=pi is automatically met for quadratic chi; odd degree does not contradict it. Multiplicity4k or3k excludes gamma inside the region, but no verified comparison puts the whole remaining interval there. Varying epsilon does not remove the constant's dependence on epsilon. Exact statements, constants and exceptions were read; the full proof was not audited. Primary: https://arxiv.org/pdf/2508.10844 (v3 dated18January2026).

Brumley's appendix to Humphries, Standard zero-free regions for Rankin–Selberg L-functions via sieve theory (2018 online primary PDF), TheoremA.1 and RemarksA.1–A.4, PDFpp.12–13, retains a real exception when both factors are self-dual. Its GL5 Sym4 example requires a symmetric-fourth-power lift over the same field and addresses exceptional zeros near1. Calegari supplies the relevant GL2 construction after real-quadratic base change, not a GL2 representation overQ producing A. The exact statements and introduction were inspected, not the entire proof. Primary PDF: https://discovery.ucl.ac.uk/id/eprint/10060648/1/Humphries_Brumley2018_Article_StandardZero-freeRegionsForRan.pdf ; DOI https://doi.org/10.1007/s00209-018-2136-8 .

A search returned a later power-sum preprint arXiv:2608.12257, but primary PDF/HTML retrieval failed. No theorem or conclusion from that search-only hit is used.

## A further central-positivity scope test

Freshly read Lapid and Rallis (2003), On the nonnegativity of L(1/2,pi) for SO_(2n+1), Annals of Mathematics157(3),891–917, Theorems1–3 and the introduction/setup on printedpp.891–895. Theorem1 concerns symplectic cuspidal GL_n representations and concludes nonnegativity at the central point. The same introduction states that this self-duality type has even n, so it does not apply to the odd-degree GL5 standard factor A. Theorem3's root-number identities likewise do not assert real-interval nonvanishing. Primary publisher PDF: https://annals.math.princeton.edu/wp-content/uploads/annals-v157-n3-p05.pdf ; DOI https://doi.org/10.4007/annals.2003.157.891 .

Even a valid central nonnegativity result for an auxiliary factor would permit a zero at gamma>1/2; no interval theorem is obtained by changing the evaluation point. A real norm twist to move gamma to the center changes a unitary self-dual representation into a generally nonunitary, non-self-dual one, so the theorem cannot simply be reapplied to that twist. This is a hypothesis check, not a full audit of the27-page proof and not a new arithmetic obstruction. The related Lapid2003 IMRN theorem was located in publisher/search metadata, but its primary PDF retrieval failed; no additional proof or application is claimed from it.

## Exact algebra, now proved in MA-RB-011

For the honest Artin X, the inertia average of the End(X) character is the average of |chi_X|^2. It bounds both its conductor codimensions by0.3 times regular codimensions and every ramified local logarithmic Euler coefficient below by0.3 times the corresponding regular coefficient. At complex conjugation2B its archimedean dimensions are20/16. The favorable gamma difference is psi(sigma/2)-psi((sigma+1)/2). The pole contribution is1 rather than0.3. Thus the naive degree-only comparison misses an adverse term; for k=1 the crude near-one constant is (sqrt3-1)^2/(0.15logDelta), versus8/logDelta for the regular representation.

The corrected exact table gives Theta=V eta+W values(9,-1,1,0,2,-1,-1). For nonnegative five-factor weights, let p=sum a_i^2, d=(5,5,4,4,6) dot a and m=a^T M a. Then m<=2p+(7/120)d^2 and 1/118<=x=p/d^2<=1/16. When m>p the score is strictly below4/120, because the squared comparison reduces to (x-1/120)(x-3/40)<0. This is an exact certificate, not numerical optimization.

The score uses the positive part max(sqrt(m)-sqrt(p),0)^2. If m<=p, the elementary pole-versus-zero inequality gives no positive repulsion, even though the unqualified square could be positive. The complete optimization and squared inequality are written in the TeX proof.

The current certificate controls only this guaranteed leading near-one score. It does not show that every exact Euler/gamma variational combination is weaker. For weights involving A, no finite Artin-conductor bound is assumed. The exact gamma/Euler expression is expressly that of the actual Artin End(X) completion. A scalar standard-L equality is not used to identify ramified tensor-product factors; the already checked partial Rankin identity is sufficient for the score. No arithmetic witness, compatible Galois representation, or interval-wide nonvanishing has been constructed. An exploratory message had incorrect Theta entries; direct inspection of the existing checked JSON corrected them before any saved derivation.

## Author whole-proof check

Read every line of the first377-line written proof in two untruncated portions, then reread every final delta: the positive delta hypothesis, regular degree wording, exact completion and all-place caveat, bibliography years and review status. Recomputed every inertia/coset trace, ramification-filtration inequality,20/16 signature, prime-five sum, corrected character cone bound, both squarings and their positive signs, exact Landau-model maximum and gamma difference. Freshly read Calegari's definition of modularity, Theorem1.1 and its four-/six-dimensional construction; the TeX does not infer stronger ramified tensor compatibility than those scalar statements furnish. Read the inherited NT-C06 conductor-discriminant source locator; no new original-Neukirch-page claim. No numerical optimization or rerun of the settled character certificate was performed.

## Independent review and promotion

Root and PF have independently read the complete397-line proof and passed it. PF additionally checked the exact Harcos–Thorner statement interfaces; these are statement readings, not whole-source-proof audits. At2026-11-22T00:01:07UTC only the review-status paragraph was promoted. Its final hash is385c36d20c412514f99bdcd325e9d5e8538abe38a85d6ec1c86b5d5975a681ef. The mathematics is unchanged from the reviewed efc93d7b version. This remains a limitation of a proposed route, not a smaller arithmetic gate.
