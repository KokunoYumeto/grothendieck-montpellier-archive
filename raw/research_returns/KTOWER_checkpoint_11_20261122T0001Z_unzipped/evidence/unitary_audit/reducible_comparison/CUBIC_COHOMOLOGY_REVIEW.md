# Independent cubic cohomology review

Reviewer: /root/unitary_audit, GPT-6 Astra Pro. Effort is not exposed. No Lean kernel build is claimed.

**PASS** for the whole sibling cubic_cohomology.tex at SHA-256 dd41ab455e172acecc59e76e7f5b3bd97e574db353378f46515b42276aa64127, including its exact finite-S scope and the finite example. I read the entire proof and the entire small example script. I also reread Milne ADT Chapter I Theorem 4.10(a)–(b), its complete exact sequence and duality definitions on printed pp.56–57, and Theorem 2.6 with its complete proof on pp.30–31. The previous local-duality and Euler statement checks remain in force.

For the twisted negative cubic character eta·psi^-1, the Cartier dual is eta·omega^(e+1), exactly the even mirror killed by the exponent-e auxiliary unit. The local H2 groups vanish at p, at each prime dividing D, and at infinity. Global Euler gives H1 dimension one, and the already proved strict vanishing makes localization to Qp an isomorphism. No positive-root unit or new class-group vanishing is silently assumed.

For the rational positive character psi, the dual is omega^(1-e). Restriction to Q(mu_p) identifies strict cohomology with equivariant homomorphisms from the class group modulo p and the classes of primes over D. The unique prime over p is principal, so it adds no further quotient. Conversely these homomorphisms descend, and every local restriction is injective through the extension of degree dividing p-1. This proves equality, not only an injection.

The last part of Poitou–Tate gives exactly the local summands at q dividing D for which q^(e-1)=1 modulo p. There is no local contribution at p because the odd dual exponent is nontrivial on inertia. The example p=7, e=2, D=-43 proves that the raw H2 group can be nonzero even when all three auxiliary units hold; it does not evaluate a Massey obstruction.

The finite script computes complete conductor-301 sums modulo 49, using the correct Teichmüller lift x^7 modulo 49, and independently checks them by exact rational generalized Bernoulli polynomials. Its asserted values 166 and -106082 reduce to 5 and 3 modulo 7. A fresh byte-identical copy is replayed in the adjacent cubic_cohomology_replay directory and compared with the sibling report.

For a prescribed ordinary/unramified deformation, raw Sha2 is not the entire obstruction: matching local H1 primitives remains necessary. The separate cubic_massey_condition.tex retains that extra term, and its full dual Selmer dimension involves the class group without quotienting by the prime classes over D. This distinction is part of the successful review.
