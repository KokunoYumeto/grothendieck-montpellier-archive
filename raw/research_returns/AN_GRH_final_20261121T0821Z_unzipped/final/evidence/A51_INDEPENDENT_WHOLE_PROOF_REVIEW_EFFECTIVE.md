# A51 complete independent proof review

Date: 2026-11-21. Reader: GPT-6 Astra Pro; effort not exposed; /root/effective_galois.
Source: work/row_audit/A51_NORM_COMPATIBILITY_AND_TOWERS.tex.
SHA256: ba76d8eba6a85ec3f81441dcf719d6565debcc38332507c3acedd1898d4a9fd2.
Outcome: PASS. All seven proof steps and the concluding scope paragraph were read. No mathematical correction was requested.

## Exact mathematical check

Steps 1–4 correctly convert the complete compatibility memo already reviewed in COMPATIBLE_COLLISION_INDEPENDENT_AUDIT.md. The actual rational p-primary norm splitting gives an exact direct sum and m'=lcm(m,ord b). Rational principal functions descend by the scalar cocycle; exact p-power order gives separability. The divisor-of-norm formula has the correct degree-one residue multiplicities. The unrestricted norm-one example is expressly not an etale pointed-cover example. Both constant split fibres provide the lower, rather than upper, bound on the particular point-difference order. The actual integral primitive projector is annihilated by each proper-quotient trace; pullback injectivity on p-primary torsion then gives genuine invisibility to the norm maps. No arbitrary realization of an invisible torsion element by two point lifts is asserted.

Step 5 is conditional on a Frobenius-stable rank-one Z_ell quotient. Through Abel–Jacobi and the Tate module, its arithmetic multiplier is a Weil eigenvalue, so it is not a root of unity. For odd ell, binomial expansion gives v_ell((a^t)^h-1)=s+v_ell(h), and therefore the exact minimal deck extension f_r=t ell^max(0,r-s). The convention on arithmetic Frobenius on points is compatible with the indicated multiplier. There is no assertion that every ell supplies such a quotient.

Step 6 applies the previously checked A45 descent on the full cyclotomic product algebra. The invariant ring is a product of unramified discrete valuation rings and the finite etale torsor has constant rank f_r. Its module is consequently free of that rank over the invariant ring, so the additive cardinality, exponent and p-torsion-dimension identities follow for arbitrary finite modules. The primitive dimension is (g-1)phi(ell^r), from the successive genus difference. Thus the displayed uniform rational generator bound is correct. The abstract O_r/p^e example satisfies the exact semilinear hypotheses for arbitrarily large e, but is carefully not asserted to be a Jacobian factor or geometric tower.

Step 7 uses a different, explicitly specified multiplication-by-Z action on the direct sum. Each element has finite support and open stabilizer. For r>m, Z^(ell^m)-1 is a unit at every residue factor because the roots have exact prime-to-p order ell^r; therefore the invariant group is exactly the finite sum through r=m. Its exponent can have arbitrary prescribed growth through the sequence e_r. This is a correct abstract limitation on the finite-invariant-group inference, not a geometric counterexample.

## Fresh primary source reading

- Stacks Theorem 59.24.1, Tag03P8, https://stacks.math.columbia.edu/tag/03P8 (web reference turn750903734view0): complete statement and displayed proof read. Taking Spec(k) gives the Hilbert90 scalar-cocycle vanishing used here.
- Stacks Lemma 42.18.1, Tag02RT, https://stacks.math.columbia.edu/tag/02RT (turn750903734view1): complete statement and displayed proof read; exact pushforward-of-principal-divisor equals divisor-of-norm formula.
- Stacks Proposition 35.3.9, Tag023N, https://stacks.math.columbia.edu/tag/023N (turn668176890view0): complete statement and displayed proof read. The publication explicitly omits proofs of assertions (2)–(3); no claim to have read omitted text is made. Its effective descent permits nonfree modules and requires no division by the group order.
- Milne, Jacobian Varieties, author version12June2021, Proposition9.1, p30, https://www.jmilne.org/math/xnotes/JVs.pdf (turn750903734view3, turn543627671view3): exact statement and displayed equivalence/nearby context reread. No fresh whole-chapter proof audit claimed.
- Milne, Abelian Varieties, author version2January2022, https://www.jmilne.org/math/xnotes/AVs.pdf: Remark15.3 and the adjacent Galois compatibility Remark15.5, pp28–29 (turn543627671view0), plus Theorem19.1 statement and complete displayed proof with Lemmas19.2–19.3, pp40–41 (turn668176890view1), read. Remark8.5, p14 (turn543627671view1), is used only for its numerical p-rank bound r<=g; no general group-scheme decomposition is used.

The recovered A1 A.31 proof was directly read in the earlier complete compatibility review. This review does not invoke its final appeal to A.1 to prove the hypothetical-collision consequences. No fresh numerical computation, new independent arithmetic implementation, formal verification, or universal witness-gate improvement is claimed.
