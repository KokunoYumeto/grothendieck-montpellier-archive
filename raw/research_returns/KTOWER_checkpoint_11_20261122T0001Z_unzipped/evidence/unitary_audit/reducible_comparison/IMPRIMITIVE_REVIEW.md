# Independent ordinary imprimitive-source review

Reviewer: /root/unitary_audit, GPT-6 Astra Pro. Reasoning effort is not exposed. This is a whole mathematical proof review, not a Lean kernel execution.

**PASS** for the entire sibling proof at evidence/lean_chain/determinant_normalization/ordinary_imprimitive_exclusion.tex, SHA-256 e118a9623d55d06f3103be295e1a78c125b891fe9d25c69869909f91e6f78c16. I read the whole argument twice, including its exact source-scope paragraph.

The stable monomial lattice is valid: the compact line stabilizer has unit-valued scalar character, so the chosen orbit basis has unit monomial entries. Reduction therefore preserves the permutation quotient. The residual composition factors are all characters, which triangularizes every stable residual lattice after a finite residue extension. Its diagonal kernel is a normal p-group and its quotient is abelian. Since p>3, the transitive permutation quotient must be C3.

The ordinary inertia argument uses characteristic-zero characters, not merely distinct residual characters. On the finite-index inertia subgroup fixing the three lines, the cyclotomic image remains infinite, so the characters chi^e, 1, chi^-e stay distinct. Their invariance under inertia conjugation forces all three lines to remain fixed by full inertia. The resulting cubic self-twist is unramified at p, but residual multiset invariance forces its reduction to equal omega^e or omega^-e. Both are nontrivial on inertia because the local field is unramified over Qp and the stated exponent condition holds. This contradiction includes the residual order-three case.

The final exclusion of finite projective image follows directly from the same infinite distinct inertia characters on every finite-index subgroup.

The hypothesis is the actual full ordinary flag. The result does not reconstruct an ordinary representation from a residual Hecke value, and makes no new claim about all algebraic subgroups or about Selmer vanishing. It is a source-scope reduction only.
