# Conditional endpoint descent in higher degrees

Full proof is in `I_endpoint_descent_candidate.tex`. GPT-6 Astra (OpenAI), 20 November 2026. Status: candidate awaiting separate audit; the broad full presentation remains Undecided.

Assume continuous maps on the **entire** endomorphism groups in degrees below i, respecting all lower-degree products. For a height-gap-i pair p⊂q, localize the residual complex at q. Its last term is E_q. On the previous column define ψ(g)=e_q T Φ_(i−1)(g). This is continuous precisely because the entire preceding-degree map exists; componentwise continuity would be insufficient.

The preceding local differential has image killed by ψ: its expression is e_q T a_q T Φ_(i−2), and incidence removes the intermediate cutoff a_q, leaving T²=0. I6 says this image is dense in the kernel of the final differential. I7b makes the final differential an open quotient onto its image, which is dense in Hom(E_p,E_q). Hence ψ descends continuously and extends uniquely by completeness of the target corner.

With I9 accepted, this gives every individual degree-two interval map. It does not yet assemble them into the global degree-two map. Therefore it cannot be iterated to degree three without an additional whole-family continuity theorem. This limitation is part of the proposition, not omitted from its induction hypothesis.
