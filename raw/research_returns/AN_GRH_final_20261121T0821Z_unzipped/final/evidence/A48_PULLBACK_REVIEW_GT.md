# A48 pullback-iteration supplement: complete independent review

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: work/row_audit/A48_PULLBACK_ITERATION_SUPPLEMENT.tex.  
Source SHA256: b80961b464066b270cf4edda207647bbf9bf17e4a55423c2292b6d7ca4ca824b.

## Verdict

PASS. I read the entire supplement, including both paragraphs and all six displayed identities. This is an independent complete mathematical review, not a new arithmetic implementation. No numerical computation is claimed.

For a connected same-degree cyclic pullback along an etale map of degree prime to p, deck-equivariant pullback and norm commute with the integral canonical conductor projector. Their composite is multiplication by that prime-to-p degree. This proves injection on rational p-primary groups over every finite extension and on geometric p-torsion; it also proves exponent divisibility. Nonconstant deck descent causes no issue because the canonical projector is invariant under automorphisms of the cyclic group. The stated connectedness and same-conductor qualifications are essential and are retained. The numerical failure statement concerns the same conductor and its exponent, not all possible covers upstairs.

Raynaud's geometric existence input and Proposition 1(5) give the stated containment of the entire pulled-back Jacobian in the support of the locally-exact-differential theta divisor. They do not identify singular coherent arrows with a nilpotent product in dimension greater than one. The elementary matrix example is explicitly a logical comparison, not an asserted geometric example. Trace splitting preserves an existing stable Frobenius subspace because the degree is invertible in the ground field. The final genus computation applies only to intermediate etale deck quotients and is correct. No claim of universal witness nonexistence is made.

## Primary-source scope checked directly

Michel Raynaud, *Revetements des courbes en caracteristique p>0 et ordinarite*, Compositio Mathematica 123 (2000), 73--88, DOI 10.1023/A:1001840726893.

Primary PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf

Retained local source: work/row_audit/Raynaud2000.pdf and Raynaud2000.txt. Retrieval references: turn198455416view0, turn375094264view0, turn375094264view1.

I read the definitions on printed p.74, Proposition 1(4)--(5) and its displayed proof on p.75, the statement of Theorem 2 on p.76, Theorem 17 and its displayed deduction, and the complete concluding construction of Theorem 2 on pp.85--86. The construction first uses a prime-to-p cyclic cover to adjust the genus, then a Heisenberg representation with no theta divisor, and induction back to the original fundamental group. The genus-two characteristic-two choice is m=5, n=3. I did not independently reprove every earlier Heisenberg lemma or the cited Hirschowitz input, and this audit does not claim to have reviewed every proof in the paper.

The hypotheses and conclusions used in the supplement match these primary statements. Descent and pointing are explicitly kept separate from the geometric existence theorem.
