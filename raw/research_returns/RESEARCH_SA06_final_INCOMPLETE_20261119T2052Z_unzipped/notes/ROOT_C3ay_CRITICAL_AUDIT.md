# Root full proof and certificate audit: C.3ay

**PASS.** AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). We read the complete typed proof, rederived its integral Chow-ring and incidence identities, opened and read its primary inputs, and inspected the entire retained certificate program and every output case. We also read the complete independent review by /root/cycles. This event does not claim an independent rerun of the finite program.

## Exact statement checked

For every prime p and every r at least 2, a normal excellent strictly henselian local ring of dimension 2r is explicitly constructed over the algebraic closure of the function field of the indicated constant elliptic curve over the algebraic closure of F_p. Its puncture and its principal-divisor puncture are regular. The restriction on actual ordinary algebraically trivial codimension-r cycles has an infinite-order kernel element. Its restriction vanishes in integral Chow, including when p divides r. This does not assert a nonzero rational ordinary class over the algebraic closure of a finite field itself.

## Full proof checks

1. The two cubic equations are smooth, including in characteristics 2 and 3. The chosen geometric generic point is not a point of any finite multiplication kernel E[n], including the nonreduced kernels at multiples of p. Its degree-zero line bundle therefore has infinite order. The displayed diagonal line bundle gives an actual proper-curve family with exactly the claimed fibres.
2. The finite-field enumeration specifies r distinct horizontal sections with pairwise disjoint reduced degree-three divisors. The separability conditions are precisely b²+b nonzero at p=2 and 4−27b⁴ nonzero at odd p. The sections y_i(V−b_iW) have exactly 3r reduced common zeros and independent local differentials. This argument establishes the universal geometric statement independently of the finite sample.
3. The incidence hypersurface is smooth off the base by its projective-bundle description and on the base by the independent differentials. Its tautological quotient-bundle section is regular of rank r−1, with zero scheme P^(r−1) times the base. The integral top Chern class is the sum of (-h)^j a^(r−1−j), with coefficient one in every term. The degree-zero line bundle restricts trivially to each zero-scheme component; the resulting annihilator identity follows by the integral projection formula.
4. The source Chow ring is CH(E)[h,h_y]/(h^r,h_y^r). Eliminating h=−(h_y+c), using c²=0, produces exactly the relation r h_y^(r−1)c in degree r. The degree-r quotient is Pic(E)/Z(M^r). The degree map shows that Pic^0(E) injects. The exhibited class becomes r lambda and retains infinite order, irrespective of p dividing r: multiplication in the integral Chow group is integer multiplication.
5. The complete section ring is normal and generated in degree one by the explicit cubic and Segre construction. Its cone has dimension 2r and a regular puncture; the incidence section gives the regular principal puncture. The previously fully audited C.3e strict-cone injection transfers the infinite-order class. Pulling back the actual diagonal family and applying the fixed integral Chern operator proves ordinary algebraic triviality on the actual puncture.
6. On the principal puncture the normal line L becomes trivial, hence h=−a. The Chern annihilator is exactly r a^(r−1), so it kills precisely the chosen class, integrally. No division by r, characteristic-zero deformation, formal-only family, or finite-field nontorsion inference is used.

## Primary inputs actually opened

- Stacks Project, Tag 0FA8, Lemma 42.44.1 and proof: the regular-section zero scheme represents the integral top Chern class.
- Stacks Project, Tag 02UB, Lemma 42.39.1 and equation 42.39.1.1: the twist formula, including coefficient one in top degree.
- Stacks Project, Tag 02TX, Lemma 42.36.2 and proof: integral projective-bundle formula.
- Milne, *Abelian Varieties* (2022 version), Proposition 8.1 and Theorem 8.2 with proof, pp.12–14: finiteness of multiplication by every positive integer.

Root web receipts for the actual source readings: turn855795214view0/1/2, turn565740770view0, turn655577121view0/1. These are source-audit metadata, not replacements for the bibliography's URLs and theorem locators.

## Finite certificate inspected

The full program is `agents/real_weil/code/check_positive_characteristic_critical_injectivity.py`; its JSON output is the same path with `_output.json`. We read every record, not only the aggregate booleans. It contains six projective smoothness checks (p=2,3,5,7,11,13), 24 explicitly enumerated horizontal-base cases (r=2,3,4,6), 29 integral Chern identities (r=2 through30), and 14 integral Smith quotient models (r=2 through15). The latter models explicitly retain an independent infinite-order lambda generator, a degree generator, and M=3 times the degree generator; the sole nonunit Smith factor is 3r and the lambda functional takes the value r on the witness. These finite formal models check the algebraic identities, not the geometric infinite-order assertion, which is separately proved.

The retained run completed at 2026-11-19T11:30:58.334892+00:00 in 0.4120008620011504 seconds. All displayed cases passed. The /root/cycles independent full-proof review completed at 2026-11-19T11:31:19.776876+00:00 and was read in full.

## Progress classification

Together with C.3aw this proves failure of universal ordinary restriction injectivity for every r+1<=N<=2r in every positive characteristic, with the exact field and coefficient scope above. It strictly reduces the positive-characteristic restriction gate in main item C.3. It does not decide the higher range N>=2r+1 or the unrestricted rational top B-group problem.
