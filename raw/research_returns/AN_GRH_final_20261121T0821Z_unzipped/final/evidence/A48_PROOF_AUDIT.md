# A48 author complete-proof audit

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: A48_TWISTS_AND_POINTING.tex.  
Final source SHA256: 0f942d786563c2fabee27b995042a70d8567bd77f430dd4f656c25699ea8324c.

## Verdict and scope

PASS. The author read the complete statement, four proof steps, and final scope discussion in the first draft, and reread the entire final source after the small corrections listed below. This is an author whole-proof check, not an independent review or formal verification. No new numerical certificate was required or executed.

The theorem supplies good unpointed twists of a fixed cyclic cover. It does not supply a good cover split at an arbitrarily prescribed point. In genus two at least n-phi(n) of the n constant twists have zero rational primitive p-primary group. Exactly one twist is split at the specified base point; a pointing extension of another twist restores any primitive rational p-torsion already present on that pointed model. The nonconstant-deck assertion concerns this same fixed-cover obstruction, not a count of nonconstant twists.

## Whole argument checked

1. Every nontrivial coherent character line bundle of a connected cyclic etale cover is a nontrivial degree-zero line bundle. Riemann--Roch gives h1=g-1. The functorial Artin--Schreier stable-part comparison is valid in all characteristics and all genera. Under the functorial duality between H1-etale with Fp coefficients and the etale p-adic Tate module modulo p, passing to geometric p-torsion inverts characters. Thus every faithful p-torsion character multiplicity is at most g-1, and f_n is at most (g-1)phi(n). The actual primitive factor is used; no geometric ordinarity is assumed.

2. Arithmetic Frobenius commutes with a constant deck group. Twisting by sigma^t scales the Frobenius eigenvalues on a faithful character space by chi(sigma)^t. Each eigenvalue excludes at most one t, and algebraic multiplicities give a valid union bound even with Jordan blocks. Eigenvalue one is equivalent to a fixed vector; a nonzero finite rational p-primary group contains order-p torsion. The n forms are distinct over C because the full geometric automorphism group of this Galois cover over C is its cyclic deck group.

3. On the prescribed fibre Frobenius is translation by a, so only t=-a is split. If the t-twist has a rational point after a degree-m constant extension, m(a+t)=0 modulo n and its full descent action equals that of the original pointed model over that extension. The actual primitive factors are identified, so the original rational p-primary subgroup injects. This is an exact statement for every such pointing extension.

4. For nonconstant deck action a, the mth action on the fibre is x -> a^m x+N_m(a)t. A fixed point gives N_m(a)t=(1-a^m)x. Conjugation by sigma^x cancels that term on the whole descent action, not only on the fibre, and identifies the two covers over the extension. Canonical primitive subvarieties and their original rational torsion are therefore preserved. No assumption of a constant group is hidden in this final step.

The conclusion expressly permits varying the geometric cover, conductor, or base curve. It does not infer an individual pointed witness from the unpointed average, number-field GRH, or Artin-prime density.

## Direct primary-source review

I reopened Katz, *Une formule de congruence pour la fonction zeta*, SGA7II, Expose XXII, author scan:
https://web.math.princeton.edu/~nmk/old/congzeta.pdf

Retrieval reference: turn529399932view0. I read the complete displayed proofs of Proposition 2.0 and Corollary 2.1 and of Propositions 2.2.4--2.2.5, printed pages 405--409. The first pair concerns a proper scheme over a separably closed field, and the second pair concerns a proper scheme over a finite field; every cohomological degree is allowed. No genus-two, ordinarity, or characteristic-two restriction occurs. The maps arise canonically from the Artin--Schreier sequence and base change, so the deck functoriality used here applies. The scalar-extension and Frobenius convention are distinguished in the source; A48's twist count itself takes place on geometric p-torsion with arithmetic Frobenius, so it does not exchange that action with the source's inverse action on cohomology.

The standard Jacobian identification of the dual etale Tate module with H1-etale is used in addition to Katz, not attributed to Katz's proposition. Its character inversion is explicitly written in the final source. Existing Jacobian/Kummer inputs were checked earlier in this run; no new independent reproof of them is claimed here.

## Final narrow corrections

The first draft had SHA256 4a7d80fb137274077cf9b3a873b045e3e6a1aa3f92b2d237980ed44c54af07fe. The final version fixes the literal TeX token `,qquad`, restores a stray carriage-return escape in `\rm faithful`, removes one indentation space, adds the precise Proposition 2.0/Corollary 2.1 locators, and spells out the Tate-module duality. These corrections change no theorem or proof argument. A byte scan found no remaining control characters other than tabs and newlines. The full final source was reread after these changes.

Root and effective_galois supplied separate whole-proof readings; those are recorded in their own audit fragments, not counted as author-independent checks here.
