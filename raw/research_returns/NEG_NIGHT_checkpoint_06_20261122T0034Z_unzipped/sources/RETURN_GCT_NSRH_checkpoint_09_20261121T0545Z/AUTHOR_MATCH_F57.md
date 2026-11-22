# F57 author whole-fragment match

Author: /root/gct_statements, GPT-6 Astra Pro. Effort setting is not exposed. Date: 2026-11-21 UTC.

## Final artifacts

- Full source/proof report: agent_rank4_negative_trace.md, SHA256 d22b8faf7f5616686c736e26bd28b320766ad7b823574e0a4693cf0a2d465778.
- Complete integration fragment: finding_F57.tex, SHA256 d96f71bfefb7e38e1d6a3b638cb42856476ac0edb9caca21667c4440d63e267e.
- Exact standalone certificate: verify_rank4_negative_trace.py, SHA256 38675f81b97955ca9d1d7f7bfe80eb342aceb8194d2ded23749765355c370d9c.
- Successful output: verify_rank4_negative_trace_output.txt, SHA256 265731353041b3579a9456f0407ae9574df8ce182b47ba7fa8d14e0c46a411d8.

## Scope and verdict

I read the entire generated fragment directly and matched all mathematical claims to the full checked report and exact certificate. **PASS.** This is an author proof/text match and exact symbolic calculation, not an independent proof review or formal verification.

The complete fragment retains the five-dimensional source matrices, the source row-action convention, the full product diagonal, the rank-one reduction, the actual Theta-op word reversal, the source simple-module occurrence in the ordinary Specht tensor, and all strict-positivity and arithmetic hypotheses.

The actual ordinary factor dimensions are 3 and 2 (or larger, or interchanged), and the relevant simple is the additional full-algebra block omitted from the two-row quotient. The claim at v=3 is explicitly a claim about the displayed specialization; no generic irreducibility assertion is silently specialized.

The finite power-trace argument applies to either overall sign and remains valid after a fixed Tate twist. It excludes a genuine power trace or one common cohomological parity, while allowing inserted endomorphism traces and alternating complexes.

The one transparent corollary added in the fragment beyond the frozen report is the explicit bounded Tate complex. Its positive multiplicities are 668 in degree zero and 657,476,297,176,67,36,4,2 for each pair of opposite Tate exponents 1 through 8. Thus its even part has dimension 668+2(1715)=4098; its odd part consists of the two Tate lines at exponents 9 and -9. Its Euler trace is exactly the displayed Laurent polynomial at every extension degree. It supplies a scalar trace and no unproved family of word-operation maps.

The separate dictionary limits torus-effectivity and lambda/sigma language to coefficient representations. It does not declare a scheme-group realization of the noncommutative algebra or a lambda-ring structure on that algebra. The stated perfect-complex framework concerns the bounded coefficient complex, with the Frobenius action supplied separately.

The last delta from fragment c37c7ffa6a62016df69f3d24cbd9c7052d06c2587564985d9493d8a392d4af7a only makes the Tate coefficient hypothesis explicit: choose ell not dividing q. The revised paragraph was reread; no other content changed.

The exploratory searches remain confined to the report and are not treated as proofs of positivity in the main fragment.
