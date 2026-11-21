# A44 author complete-proof audit

Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.  
Date: 2026-11-21.  
Source: A44_PRO_TWO_TOWER_OBSTRUCTION.tex.

Final source SHA256: d7ef05d824572383a63e35a89eb8d74f51d2f6a0e28bf2c7d326cabed15fb01a.

## Author result and scope

PASS: the entire mathematical proof was read at c5973acf166ba2e5a2c3a32e70781f086e9aa6a922090e0a40b6ca4d82193e2e. The subsequent display-only changes at d1e97e8250896fbbbf6801cc1caa94e6dee85b0092199ccaad17997f66a71e3e and the final additional Milne Proposition 12.9 citation were narrowly checked. No substantive mathematical correction followed the complete read.

This is an author check, not an independent proof review or proof-assistant verification. The theorem applies to every abelian surface over a finite field of characteristic two. It proves finite signed-2-eligible prime support in the pro-2 constant-field tower and a computable finite field containing all torsion with that support. The genus-two Raynaud-theta corollary simultaneously proves unbounded odd theta torsion in the tower, so all but finitely many of those odd orders contain an individually ineligible prime.

This closes the specific attempted mechanism of extracting an unbounded compatible supply from abundance in the characteristic-power tower. It does not decide whether its finite candidate set contains a witness for every curve. It does not extend to an odd auxiliary-prime tower, and no formerly open universal prescribed-point row is marked solved.

## Whole proof checks

1. **Frobenius polynomial and nonzero constants.** With P=T^4−aT^3+bT²−qaT+q², the proposed quadratic product has coefficients a=(1+epsilon*q)s and b=epsilon*(1+q²+q*s²). Substitution gives D_epsilon=0. Conversely D_epsilon=0 gives that product over Q, since 1+epsilon*q is nonzero. Its first quadratic would have root product of absolute value one while both roots have absolute value sqrt(q), a contradiction.

2. **First appearance and eigenvalue.** An odd prime first occurring at level 2^m yields nonzero geometric ell-torsion fixed by F^(2^m). On that kernel F is semisimple because its annihilating polynomial T^(2^m)−1 is separable. The minimal field-degree condition forces an eigenvalue of exact order 2^m. Its minimal-polynomial degree is ord_(2^m)(ell), at most four. No full-mod-ell semisimplicity assumption is hidden.

3. **Residue exclusion.** Eligibility excludes ell=1 mod8 since both generators are squares there. For ell=3 or5 mod8, the exact valuation v2(ell^4−1)=4 excludes m≥5. Thus every late eligible prime is7mod8. The residual degree is2or4.

4. **Quadratic norm case.** If the degree is2, v2(ell+1)≥m−1, so the norm of the primitive 2^m root is epsilon=±1. Reciprocal roots either overlap, forcing q=±1 modell, or give the full four-root factorization. Elimination without division yields ell|D_epsilon. The repeated-root/overlap possibility is retained in q²−1 and is not silently discarded.

5. **Quartic norm case.** Degree4 forces v2(ell+1)=m−2. The norm exponent (1+ell)(1+ell²) has valuation exactlym−1, so the norm is−1. The constant coefficient of the entire minimal polynomial isq², giving ell|q²+1. These and the first16-level primes give the finite displayed integer.

6. **All exponents.** Every ell-primary point in the pro-2 field has a Frobenius orbit of 2-power length dividing the order of GL4(Z/ell^r). Its2-part is independent of r because the reduction kernel is an ell-group. The exponent e in CT.4 therefore bounds every primary component's field degree, establishing actual equality of subgroups in CT.5. The whole-order signed-unit condition necessarily holds at each prime factor by reduction.

7. **Unbounded odd theta torsion in the same tower.** The 2-adic point-count proof is complete in the source. Roots of positive valuation and unit roots with nontrivial residue make zero contributions to v2(#A). For a unit congruent to1 in the residue field, repeated squaring eventually reaches valuation>1 and then increases the valuation exactly by1 per step. Weil roots are never roots of unity. The reciprocal pairing bounds the number of contributing unit roots by2. Thus the rational2-primary index eventually grows as a fixed constant times2^(t*m), t≤2. Applying the one-field Lang count at each level produces an unbounded odd theta count. Those auxiliary covers vary with m; A42's stable-primary hypothesis is not incorrectly invoked.

8. **A13 exact order3 illustration.** The ordinary genus-two curve has four geometric theta characteristics. Its three rational Weierstrass points are the three effective ones; B=W0+W1−Winfinity is canonical-half and distinct from them, hence the unique ineffective Raynaud characteristic. The original curve and its twist agree overF2. With r²+r+1=0 and a0²+a0=r², R=(r,a0) lies on the model and Norm(Y+a0h)=h(X+r)^3. Its conjugate value atR is1, its pole is5, and its branch values vanish, so the exact divisor is3R+W0+W1−5Winfinity. Dividing byh² gives3(R−B). Ineffectivity proves the class nonzero, hence exactorder3. The two choices each ofr and a0 give four distinct classes overF16.

## Primary input scope actually read

Milne, Abelian Varieties, author version 2 January2022:
https://www.jmilne.org/math/xnotes/AVs.pdf.

- Complete Theorem8.2 proof (including its continuation), and Remark8.4, pp13–14, for the free odd torsion modules.
- Complete displayed Proposition12.9 proof and its two stated supporting lemmas, pp23–24. Lemma12.10's proof is referenced by Milne to Lang; that external proof was not independently reconstructed.
- Complete Theorem19.1 proof, including Lemmas19.2–19.3 and their displayed proofs, pp40–42, for point counts and Weil roots. Earlier positivity results used there remain known inputs.
- Web references from this review: turn820698910view2, turn962960430view0, turn311308004view0.

Poonen, Multiples of subvarieties in algebraic groups over finite fields:
https://math.mit.edu/~poonen/papers/multiples.pdf.
The complete displayed Lemmas6.1–6.2 and proofs were reread during A42. A44 independently proves its explicit fixed-support field bound and does not import an unspecified numerical bound from Poonen.

## Executed finite certificates

### Symbolic and finite scalar certificate

verify_A44_finite.py was authored and executed successfully. It checks:

- both integral factor/elimination identities;
- every odd residue modulo2^m for5≤m≤16 satisfying the necessary degree≤4 and non-1mod8 conditions, including the exact norm exponent cases;
- the A13 N16 by an exact polynomial resultant and independently by its quadratic trace recurrence;
- L factorization, eligible prime list{3,5}, and the crude e-values9,11;
- the A13 point equation, norm identity and conjugate value1 by a polynomial quotient-ring calculation overF2.

Script SHA256: b7b7893de0f79e6388bef93624927eb1252982e917ee015ba2f77c8bf0d61c43.  
Output verify_A44_finite.json SHA256: f62580bade6acd01f20fd3b88119be24dcea3c77dbdfaa4004175485a0344769.

The bounded residue computation is a consistency check only; the proof for allm is the elementary valuation argument in the source.

### Retained bounded RR probe, without expanding the search

Before finding the short norm identity, probe_A44_theta15.py enumerated the one A13 curve overF256, with223 projective points and220 nonbranch points. For each nonbranchR it reconstructed the complete17×16 matrix for functions inL(17Winfinity) vanishing to order15 atR and once atW0,W1. It found216 matrices of rank16 and four of rank15. Every point, rank, selected minor, minor determinant and matrix hash is retained. The four candidates are (188,224),(188,225),(189,92),(189,93) in the AES polynomial basis.

Script SHA256: 8162ad50d0d963ed39a54c90bd64aae044918045b6a2c66e840e41b1e1df31c0.  
Output probe_A44_theta15.json SHA256: 86d2779834f17bdd39d8b89c5bd2026b7751757cf693578f114133e7188dd695.

This is one RR arithmetic implementation. The symbolic script records its output but does not independently reproduce its matrices. The main theorem and exactorder3 illustration do not depend on the negative rank assertions. No claim that these four exhaust every eligible theta point in the infinite tower is made.
