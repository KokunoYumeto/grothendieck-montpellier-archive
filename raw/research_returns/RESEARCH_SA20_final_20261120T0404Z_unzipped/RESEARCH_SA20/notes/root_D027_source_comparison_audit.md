# Root original-book comparison and D.027 audit

Audit recorded 2026-11-19T18:04:19.727408+00:00. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

We opened Slodowy LNM815's original front matter (ppIII–V and contents), and original appendices (pp152–159), through the publisher's freely accessible PDFs. The former states the ADE subregular-slice/semiuniversal assertions and, on pIV, the complete B_r/A_(2r−1), C_r/D_(r+1), F4/E6, G2/D4 correspondence with the fixed-diagram-symmetry qualification. The latter explicitly says details of the arithmetic forms are deferred. These are actual original statements, not later quotations. Root web refs turn119671960view0/1.

We also opened Steinberg LNM366's original appendix pp156–159 (turn244668017view0, turn363179314view0), and explicitly viewed the full local images of printed pp157 and158 and Slodowy pIV. The hypotheses immediately before the printed deformation theorem say simple simply connected complex G and a subregular unipotent u; no explicit ADE restriction is present in the standalone formulation. The preceding ADE discussion can indicate intended scope, and the paper acknowledges this rather than attributing an unqualified error without context.

D.027's first-order deformation argument passes. For a C2=Sp4 subregular slice of type A3, the Tjurina quotient of x^4+y^2+z^2 is C[[x]]/(x^3), of dimension3. The quotient base T/W has tangent dimension2, so its first-order class map cannot be onto. This refutes even ordinary versality under the unrestricted literal hypotheses. Changes of variables and multiplication by units give exactly the displayed Jacobian ideal at first order. Slodowy's original pIV supplies the corrected fixed-symmetry semiuniversality assertion.

We requested an explicit u=I4+N, N=[[0,I2],[0,0]], to verify every counterexample hypothesis directly. For standard symplectic J=[[0,I2],[-I2,0]], N^T J+JN=N^T JN=0. The Lie-centralizer equations for X=[[A,B],[C,−A^T]], B,C symmetric, are C=0 and A+A^T=0, so its dimension is1+3=4=rank(Sp4)+2.

We independently reran code/check_steinberg_universality.py from the lie_theory agent. It produced the reduced rational Groebner basis (x^3,y,z), exactly three standard monomials, and the base-dimension comparison, in0.048790819seconds; output logs/root_steinberg_universality.txt. This checks the finite algebra calculation. The deformation and source-scope argument is separately proved.

The original later sections SlodowyIV8.3 and SteinbergIII3.10 remain unopened. They are not needed if every assertion in the requested source comparison is replaced by the actual opened original locators above and the prior opened primary papers. Root is checking that complete replacement before closing the original task row.


## Completed full audit and original-row closure

2026-11-19T18:08:38.949067+00:00: the revised proof now includes the exact symplectic unipotent and centralizer computation, as requested, and also verifies flatness of the displayed first-order deformations. We read the complete assertion-to-original-locator table in agents/lie_theory/source_audit_D.md and the updated paper/source metadata. Every Slodowy/Steinberg366-dependent assertion used in the requested comparison is supplied by the opened original introduction, appendices, previews, or separately identified primary articles. The unread later sections remain accurately identified and no longer form a needed dependency. Outcome: PASS; original D.1 literature-comparison row closed.

The complete revised matrix-plus-Groebner certificate was independently rerun in0.154355627seconds, output logs/root_steinberg_universality_complete.txt. The earlier0.048790819second run covered only the Tjurina calculation and is not relabelled as the full check.
