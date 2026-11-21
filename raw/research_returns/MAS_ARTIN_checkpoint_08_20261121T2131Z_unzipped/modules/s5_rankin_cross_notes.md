# MA-RB-006: all fifteen Rankin cross products

Date: 2026-11-21.
Author and author checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

The full proof is modules/s5_rankin_cross.tex, MA-RB.61–70. The complete author post-writing proof reading passed. Root and pf26_audit have independently read the complete proof and passed it; root has integrated the module. PF also freshly checked the Cogdell terminal continuation/pole proof and exact statements. Root's pass does not claim a separate fresh Cogdell source reading.

## Exact outcome

Use the five actual cuspidal factors (A, A eta, V, V eta, X) and their corresponding Artin representations (W, W eta, V, V eta, X). At exceptional4A primes, the discrepancy exponent is +2 for the two five-dimensional self products, −2 for their cross product, and zero for every remaining pair. This is an exact full local-polynomial identity: the mixed products vanish in every logarithmic Euler coefficient because V, V eta and X have trace0 at all odd powers of4A, while the five-dimensional discrepancy vanishes at even powers.

All fifteen partial Rankin functions are holomorphic at the actual real gamma in (1/2,1). Their signed-order identities are exact genuine meromorphic identities. Each resulting inequality is already implied by the nonnegative Artin orders at that point and q=v1+e−k≥0. The order matrix is entrywise at least k times

    0 4 1 2 2
    4 0 2 1 2
    1 2 1 1 2
    2 1 1 1 2
    2 2 2 2 3

The formal genuine-character assignment k(V eta+W) attains every entry simultaneously, with regular order9k and all quadratic Schur inequalities still satisfied. Hence no stronger arithmetic gate or strict multiplicity improvement follows from this exact family of holomorphy inequalities. Additional nonvanishing or another proved analytic restriction could still exclude those simultaneous zeros; none is claimed here.

The proof does not assume an automorphic tensor-product lift, does not assert arbitrary formal matrices are realizable, and does not identify pi_V with the separate symplectic four-dimensional Pi.

## Checks performed

Read the complete written proof after writing and checked every local trace and ratio sign, all fifteen tensor decompositions against the existing character table, the partial-factor order passage, the two known Rankin holomorphy cases, the exhaustive nonnegative-remainder table, and the formal witness.

Executed checks/s5/s5_rankin_cross.py successfully. Its JSON records all fifteen exact cyclotomic local ratios, integer character decompositions, and order expressions. The script reuses the already checked S5 table; it is not an arithmetic zero computation.

Freshly opened the author-hosted Cogdell primary lecture notes. Read the exact Theorems9.1(i)/9.2(i), printed p74 (PDFp78), and their full terminal continuation/pole argument, Lecture9 sections2–3, printed p71 (PDFp75), with the preceding convergence context. Earlier global integral/local Whittaker theorems are retained as declared classical inputs, without a new complete audit of all their proofs.

Root owns integration and final packaging.
