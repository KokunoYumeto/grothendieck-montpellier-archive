# F65 bounded integrality supplement: author final-text match

Author/checker: /root/gct_statements, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

The final report is `agent_viii_multiplication_integrality_audit.md`, SHA256 `d7758f7ac22afad354135e87df51cebba268cdf6270c19c4b3a6ab27eb6f7f11`. The complete fragment is `finding_F65_integrality_audit.tex`, SHA256 `13a9b7cdb6bb342b53f392dd6ed8e44936a4dfc7a97501d3487729b0df63c8e8`.

I read the generated fragment in full while writing it and matched all six formulas, label multiplicities and coefficient vectors to the frozen report and exact certificate. The general grouped-integrality proof retains eventual equalities, invertible Frobenius, finite actual integer Euler multiplicities and grouping at roots of unity. The primitive-factor statement is restricted to an exact Laurent quotient. The six ordinary mixed Tate witnesses are actual objects, with negative coefficients placed in cohomological degree one. They supply no canonical multiplication or purity comparison.

The complete bounded source-role limitations are preserved. The two corrected printed-page locators are Section5's vector convention p27 and the beginning of Section5.2 p29; Figures3–5 remain pp35–37. Explicit halves in ambient expansions and nonmonomial balance denominators have not been promoted into multiplication constants. The normalized 542 table entries do not prove unprinted raw integrality. This is an unsuccessful bounded search, not additional main-gate movement or a global absence theorem.

The exact source audit script and saved JSON certificate were already rerun successfully; the independent report review `REVIEW_VIII_INTEGRALITY_THETA.md` at SHA256 `7a8d70d465a8c8a4268887b0b9b301b9fb9e826f244d594d6d3e89e51b362526` records a separate complete source/proof/script PASS. The generated fragment has been sent to that reviewer for a full final-text match.

An isolated pdflatex syntax compile with `tex_check/gct_F65_integrality.tex` succeeded with three pages. A log search found no errors or overfull/underfull boxes. Isolated bibliography/initial cross-reference warnings and the standard default font-map warning are expected; explicit maps are loaded. No visual PDF audit is claimed. No root master artifact was changed.

## Final self-contained denominator-proof delta

At root's request the Gauss-lemma invocation was replaced, in both report and fragment, by the exact elementary prime-denominator proof: choose the least denominator N for the rational Laurent quotient g/N; if p divides N, reduce Nf=(u-u^{-1})^s g modulo p. The first factor is nonzero in the domain F_p[u,u^{-1}], so all numerator coefficients are divisible by p, contradicting least N. I directly checked this proof, including p=2 and s=0. Conclusions and source locators are unchanged.

Final report SHA256 is `8cd13ba244efb01f85cf6ffdae50a935687c030522fd5900bc09c2849a091e9a`; final fragment SHA256 is `a2dcbce72c230034f0e3020584783c3d691fb4cfb9a5cf1d3eef42fbefe862f3`. Theta has this precise delta for the final match. The earlier syntax compile preceded this prose/math-proof replacement; no later compile or visual audit is claimed here.
