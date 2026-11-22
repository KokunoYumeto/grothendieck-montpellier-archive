# P-F66 — actual source eigenvalues versus geometric Frobenius

Status at checkpoint08 freeze: new working fragment, not integrated or promoted. Author entire-proof reconstruction PASS at 2026-11-21 05:01:39 UTC; independent review requested after saving. No frozen checked fragment was changed.

The exact source discriminant is nonsquare at every q=3^e because A(q)=2 mod3. P39 already proves that the prescribed actual central eigenvalues alpha±=F(P±sqrt(D))/(2q20) are positive and distinct. Their quadratic conjugates have unequal absolute values, a property retained by every common nonzero rational normalization and every nonzero integral power. They are therefore not Weil numbers for any finite-field size or any weight. This excludes their literal realization as geometric Frobenius eigenvalues in globally Deligne-mixed compactly supported cohomology, its stable subquotients, sums and Tate twists. It does not exclude larger traces or auxiliary correspondence eigenvalues.

Fresh primary reading: original local work/positivity_sources/WeilII.pdf via its extracted text, Definitions1.2.1–2 printedp153, Variants1.2.3–4p154, Theorem3.3.1p204 and its explicit point interpretation in the introductionp138. Exact official source https://www.numdam.org/item/PMIHES_1980__52__137_0.pdf. The web PDF retrieval exceeded its13.5MB cap (turn228863832view0); official metadata page was retrieved as turn416801010view0. No claim of a successful web full-PDF read is made. The actual source normalization, central-word identification and all-positive real eigenvalues are existing fully checked P39/P52 inputs, not re-attributed to Deligne.

A small exploratory exact calculation, executed before writing the proof, found A(2)=360837=9*40093 and the mod3 obstruction for residue0; the proof itself uses only the transparent constant-term congruence and no finite numerical test. No numerical purity inference is used.

Scope: the theorem explicitly assumes mixedness using all complex conjugates, not arbitrary fixed-iota purity with real weights; geometric coefficients are included only where this mixedness is established. The two eigenvalues are those on the descended quadratic source module, not asserted to be the entire spectrum of the full21-dimensional algebra. Finite q=t^k is handled at t=3^e.

## 2026-11-21T05:06:28Z — checked after checkpoint release

Author, plethysm and root entire-proof/source reviews now pass. Root proposed the more direct Corollary3.3.4 printedp206; I freshly read it and added the exact locator and the finite maximum-weight step. The all-conjugates and geometric mixedness scopes are unchanged. Existing P39Q4/P52Q4/Q8 rows are updated in place to record that the literal individual-Frobenius-eigenvalue dictionary is excluded, while auxiliary correspondence eigenvalues/larger traces and actual source compatibility remain open.
