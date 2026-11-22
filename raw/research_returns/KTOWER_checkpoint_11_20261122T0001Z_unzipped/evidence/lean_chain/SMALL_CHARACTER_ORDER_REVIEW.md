# Independent review of the small-order rational-component reduction

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed.
Date: 2026-11-21. No Lean kernel build was run.

PASS after reading the complete application proof and checking the exact primary theorem statements, including rendered scans of the ambiguous inequalities. The adjacent manifest records the final corrected proof hash.

## Exact imported statements

Moser–Payan, *Majoration du nombre de classes d'un corps cubique cyclique de conducteur premier*, J. Math. Soc. Japan 33 (1981), 701–706: the setup on page 701 assumes prime conductor p congruent to 1 modulo 3. Section 4, the unnumbered theorem and corollary on page 705, explicitly give `h(F)<2p/3` and p not dividing h(F). The theorem covers all such primes: the preceding paragraph supplies its small-prime range from the cited tables. Those tables and the analytic estimates were not independently recomputed in this review. The scanned theorem page was rendered and read, as well as the paper's text.

Moser, Grenoble seminar 1979–1980, exposé 3: Theorem B on printed page III.2 assumes p congruent to 1 modulo 8, the real quartic subfield F of Q(mu_p), and k=Q(sqrt(p)). The scan gives **`h(k) <= sqrt(p)/2` and `h(F)/h(k) <= p/4`**. These exact inequalities replace the draft's weaker/inferred strict inequalities; the arithmetic conclusion is unchanged. Theorem 1(2), printed page III.1, states divisibility of class numbers for a cyclic prime-degree extension with exactly one ramified prime. The application F/k has degree two, exactly the single finite prime above p ramified, and no archimedean ramification because both fields are totally real. Thus the quotient is an integer. Both positive integer factors of h(F) are less than p, so p cannot divide their product.

The quadratic case uses the already checked Le Theorem (a), printed page 141, for the real quadratic field of discriminant p. No new claim of reconstructing that analytic theorem is made.

## Application audit

The character omega^(-e) has the same order d as omega^e. For even e its fixed field is totally real of degree d. Thus d=2 and d=4 impose exactly the congruence hypotheses required by the cited quadratic and quartic results. The order-one case is Q; the order-three field is the unique prime-conductor cyclic cubic field. Each case has zero p-primary class group.

For H=Gal(Q(mu_p)/F), the extension–norm identity on ideal classes is `jN=sum_H sigma`, including at ramified primes. An H-invariant p-primary class has norm zero in Cl(F), and multiplication by |H| is invertible on the finite p-group. Hence the H-invariant p-primary class group is zero. The desired character component is contained in these invariants. The carried all-positive-k comparison K17-(K2), reread in the preceding mirror-scope event, then identifies the K-primary vanishing with zero character component for every even e. Only character exponents are periodic; no K-group periodicity is asserted.

The resulting restriction `ord(omega^e)>=5` for an unresolved rational component is correct. No degree-six assertion was inferred from an inaccessible title or bibliographic entry.

## Preserved source evidence

The primary PDFs and retrieval records are under `main_gate/literature/low_character_orders/`. Their SHA256 values are `0cf87da10b9acb8b32c0c81926734543b4362431dc1ef0337d9ff961d291dcf1` (Moser–Payan) and `249653cd352841ec86a668f85eaed6898c048352e8ddb3527f19cb8622325b8c` (Moser). The three inspected page renders are under `lean_chain/low_order_source_pages/`.
