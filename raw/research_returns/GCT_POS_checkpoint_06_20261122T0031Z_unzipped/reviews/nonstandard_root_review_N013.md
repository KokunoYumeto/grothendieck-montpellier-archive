# Whole-proof review of N-013

Date: 2026-11-21. Reviewer: `/root`, GPT-6 Astra Pro, effort not exposed,
run GCT_POS. Type: targeted proof check, whole proof read.

Read the complete `branches/nonstandard/bar_fixed_descent.tex`, equations
N-44 through N-52, including the final bounded-feasibility discussion.
Outcome: PASS within its explicitly modified domain.

The coefficient extension Q[D] -> Q[v,v^-1] is finite free of rank four;
the four distinct automorphisms verify independence as well as spanning.
The actual Q[D] word submodule is finite, torsion-free, and hence free
over the PID Q[D]. The injectivity after base extension uses the already
checked Q(D)-form property, rather than an unjustified submodule/base-change
identification. This does not contradict mixed-characteristic nonfreeness.

Both involutions fix every rational-D word combination and therefore every
specified GT vector and every lower-label span. The bar-fixed Laurent
order decomposes as B_S plus delta B_S. The parity projection preserves
the leading residue and the actual rational order. For odd parity,
division by delta lies in B_S, raises the v-adic leading exponent by one,
preserves the lower-label residue conditions, and lowers every surviving
ambient degree by one half. At a minimal old-support coordinate the
reverse partial-degree comparison fails, so the improvement is genuinely
strict even without choosing a total order. For even parity the projection
has coordinatewise no larger degree, preserving global minimality;
uniqueness therefore forces descent.

No existence or uniqueness is proved. The conclusion concerns a rational
normalization, a chosen genuine label order, K=Q(v), half-integral scaling
exponents, and the added equation bar(y)=y. It is not a construction of the
printed E(4), a repair of its unspecified order by implication, or a claim
that rational-D constants are Laurent/Tate polynomials. The final discussion
correctly retains the missing global degree cutoff and the possibility that
earlier-coordinate improvements permit later-coordinate growth.

This was a mathematical proof reading, not a computation or formal proof-
assistant verification. No numerical experiment is needed for this lemma.
