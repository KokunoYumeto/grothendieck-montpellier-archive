# Monoidal acyclic models: source audit and strictification gate

Inspected 22 November2026 (Europe/Berlin), root, GPT-6 Astra Pro; reasoning effort not exposed.

Primary work: F. Guillén Santos, V. Navarro, P. Pascual, A. Roig, *Monoidal Functors, Acyclic Models and Chain Operads*, Canadian Journal of Mathematics60(2) (2008),348–378, DOI10.4153/CJM-2008-017-7. Publisher introduction identifies the cohomology comparison as Theorem9.2. The directly inspected author arXiv version math/0506624v2,3 October2005, has §9.1.1 axioms, Theorem9.1.2 (pp25–27), Corollary9.2.1 (p28), and Example9.2.2. The numbering difference is explicit; do not conflate versions.

Primary URLs:
- https://arxiv.org/pdf/math/0506624
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/div-class-title-monoidal-functors-acyclic-models-and-chain-operads-div.pdf

The author version assumes: R is a PID; every simplicial/form term is free; each simplex's complex is homotopy equivalent to R; every form row is simplicially contractible. It obtains a zigzag for contravariant monoidal functors, hence an equivalence of associative differential graded algebras with singular cochains. The proof uses a cotriple built from finite products of simplices, vertical acyclicity for its acyclic-model condition, and horizontal contraction plus free-module splitting for presentability.

These hypotheses are not the archive's hypotheses verbatim: archive conditions are degreewise eventual in a weight, and arbitrary admissible theories need not have free terms. Most significantly, an associative DGA comparison is not a strict commutative divided-power comparison over Gamma_Z(T). The cosimplicial cochain totalization uses the Alexander–Whitney direction; the symmetric chain shuffle comparison does not by itself supply the missing strict symmetric cochain structure integrally.

Possible next route: adapt the comparison only in bounded degree and the eventual-weight category, then inspect whether it identifies full weighted Massey defining systems. This could rule out a nonlinear obstruction without deciding strict-PD connectedness. A subsequent strictification theorem would still be needed. No such adaptation or strictification is currently asserted as proved.

This is a targeted applicability audit of the exact theorem and proof architecture, not an independent proof of the external paper.
