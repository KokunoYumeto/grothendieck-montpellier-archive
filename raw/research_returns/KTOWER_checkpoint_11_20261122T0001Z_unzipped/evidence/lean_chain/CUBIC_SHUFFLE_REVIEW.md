# Independent whole review: cubic shuffle and raw norm identification

**PASS** at final proof SHA `0268d7127561c8d93ea1da4dc99389b67683aedcf64d7696e86084ce91a32e3c`. The full original shuffle proof, full added corollary CS.11–14, and complete final code were read. All eleven exact symbolic/matrix identities passed in a copied run; the entire report agrees with the author's after removal of the actual check timestamp. The preceding nine-check replay remains separately preserved.

The signs and coefficient characters are consistent: `h=-u²/2`, `a=-w-uv/2`, `b=w-uv/2` satisfy their three defining equations; `Theta+2Phi=-d(ua)` and `Omega_+=3Phi-dR` transport the actual relative primitives by `(R-z_v)/3`. The relative ordinary obstruction is exactly minus three times this specified consecutive product. The binomial conjugation changes the noncentral (1,3) entry to `(u²-u)/2`; the (1,4) change is central and irrelevant to the quotient system.

For the new corollary, restriction to K=Q(sqrt(D),mu_p) is injective on H¹ because its degree is prime to p. With F_p coefficients and nonzero u the quotient is cyclic of order p. The cocycle `f=v-a x` modulo x² has x² differential `-u(g)a(h)+binom(u(g),2)v(h)`. This is the Sharifi cocycle, equal to `-Phi-da/2`, so its Bockstein class is `-[Phi] x²`. No equality of dimensions is being substituted for this cochain identity.

## Primary scope

Sharifi's author version was read in full for section 4, printed pages 17–22, including the matrix conventions, defining equations, group generators, Proposition 4.2 and its proof, and the proper norm-system definition. The complete statement and proof of Theorem 5.4 on printed pages 26–27 were read. Lam–Liu–Sharifi–Wake–Wang was read for Definition 3.3.2; the complete proofs of Lemma 3.3.3 and Theorem 3.3.4; Lemma 4.1.1 and Theorem 4.1.2; the binomial construction in section 4.2; and all of section 4.3. The explicit identification of the binomial-block proper systems with Sharifi's Galois proper systems was also retrieved in the Cambridge published version, DOI 10.1017/fms.2022.103.

That explicit primary identification does remove the former raw norm-properness gap for this F_p-valued system. Here n=2 and A=R=F_p meet the size condition 2p<p². Sharifi's m=n=1 and repeated length 2 satisfy 2<p-1, so there is no exceptional boundary term. His negative norm-ideal formula and the cochain sign give the raw ordinary coset `-3[N(Y)]`, with the stated coefficient untwisting and lower-product indeterminacy. No separate proof of the imported general properness identification is claimed.

## Exact limits

A nonzero norm-ideal coset would suffice for a nonzero ordinary relative obstruction. No such coset is evaluated. A raw coset does not determine the local correction in the relative obstruction space. General finite extension coefficient fields still require a scalar/cyclic reduction, and no arbitrary characteristic-zero source has been shown to yield the requisite cubic jet. The result is an exact expression and a usable conditional evaluation route, not arithmetic vanishing or exclusion.

The final report and primary/source hashes are in `cubic_shuffle_review_manifest.json`; the final eleven-check replay is in `cubic_shuffle_proper_replay/`.
