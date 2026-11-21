# A42 — complete proof review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

Reviewed source: `work/gt_certificates/positive_rank_theta/A42_FIXED_LANG_DENSITY.tex`.

SHA256: `4674c99fa0944da6928d469aaca6e128571f259603b791e294ec3bacba628d87`.

**Result: PASS.** I read the entire statement, all five proof steps, the theta/canonical application, and the concluding scope paragraph. This is a targeted whole-proof check by a separate reader, not an independent re-proof or a formal verification. No source modification was needed.

## Mathematical checks

1. **The extension condition controls actual primary groups.** The polynomial `V_n(T)=1+T+...+T^(n-1)` has nonzero values on every eigenvalue of Frobenius modulo each selected prime. The condition on `n` handles the eigenvalue one as well as every nontrivial eigenvalue. An invertible polynomial in a matrix remains invertible without any semisimplicity hypothesis. A nonzero kernel on a finite prime-power torsion group would contain an element of prime order, so the argument passes to every exponent and proves equality of the actual fixed primary subgroups. For the characteristic prime, only geometric torsion points are used. The larger displayed modulus is a valid sufficient replacement.

2. **The same Lang quotient is used for every counted extension.** The factorization through the complementary subgroup of `J(k)` has constant kernel exactly `G_S`. Translating by the specified rational component does not change geometric connectedness. The proof of connectedness correctly quotients by the geometric monodromy subgroup, subtracts one geometric value of the lifted Abel map, invokes the Jacobian universal property, and obtains an impossible section of a nontrivial isogeny. The argument does not exclude the characteristic prime.

3. **The exact split-fibre calculation has the correct norm factor.** Telescoping gives `Phi^n z-z=pi_H(N_n x-nc)`. The selected component is `n(x_S-c)`, since the extension condition already makes `x_S` rational over the original field. The complementary component stays complementary after the norm. Multiplication by `n` is invertible on `G_S`. Consequently the fibre has exactly `d` rational points precisely for the specified component and none otherwise. This checks the potential compatibility problem between Lang maps over different finite fields: the proof never changes its Lang map.

4. **Counting and density follow with the stated constants.** The connected etale cover has genus `b=d(g-1)+1`, including when its degree is divisible by the characteristic. The Weil estimate therefore gives the exact error displayed in PE.5. The numerator tends to infinity along `n=1 mod M`. The sufficient search inequality gives at least two points, so it supplies a nonzero Abel class even when the requested component is zero. The coarse sufficient inequality `q^n>(2b+d)^2` is valid for `d>=1`.

5. **The theta and point-separation applications preserve their precise scope.** The argument uses the actual Raynaud line bundle on `C^(1)`, rather than an arbitrary theta translate. Prescribing a nonzero component of order `r` with even `ord_r(2)` gives a nonzero corresponding component of the canonical class because multiplication by two is invertible there. A29 then applies to each point over its field of rationality. The characteristic-primary Lang cover is only an auxiliary counting device, and is not used as an odd-degree neighbourhood. The conclusion neither controls the whole torsion order nor forces any member of a specified finite collection of transfer images to be good.

## Primary-source review and limits

- Poonen, *Multiples of subvarieties in algebraic groups over finite fields*, author PDF, p. 6: read Lemma 5.1 and its complete proof, and the complete displayed proof of Theorem 1.4. Also read Lemmas 6.1–6.2 and their complete proofs on p. 7. These support the source credit for the Lang quotient and primary-group control. URL: https://math.mit.edu/~poonen/papers/multiples.pdf . This review does not claim that the entire paper or every cited dependency was read.
- Milne, *Jacobian Varieties*, Proposition 6.1, printed pp. 19–20: read the statement and complete displayed universal-property proof. Proposition 9.1, printed pp. 30–32: read the statement and complete printed argument, including Lemmas 9.2–9.5 and the characteristic-primary conclusion. Some of those printed lemmas refer to proofs elsewhere; those external proofs were not all independently retrieved or rebuilt. The actual connectedness proof in A42 was checked directly. Theorem 11.1 is used as the classical curve Weil bound, not independently reproved here. URL: https://jmilne.org/math/xnotes/JVs.pdf .

No numerical experiment was required for this proof review. No claim is made that A42 closes the prescribed-point cover-selection gate or the primitive-orbit torsion gate.
