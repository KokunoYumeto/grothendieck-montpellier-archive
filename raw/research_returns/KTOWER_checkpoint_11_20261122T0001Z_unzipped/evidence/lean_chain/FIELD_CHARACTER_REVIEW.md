# Finite-character reduction: independent review

The complete `main_gate/field_variation_nonvanishing.tex` and
`field_character_certificate.py` were read. **KT-FIELD-CHARACTER-REDUCTION**
and its simultaneous-unit corollary pass the mathematical review.
The Sun Lemma 8.1(a) input is the already reviewed primary statement
used in the earlier infinite-family proof. The newly cited Wiles,
Beckwith, Bruinier and Burungale–Sun source statements were not
independently reread for this check; their source-scope discussion
is outside this review's independent-source claim.

For odd indices, the Sun exception `(ell-1) | b` never applies.
The normalized generalized Bernoulli values are integral by starting
with each odd index between 1 and ell-2 and applying the Euler-factor
congruence. The initial index 1 is legitimate even when its Euler
factor is zero, since the next factor is a unit. For indices at least
three both factors are congruent to one. This proves normalized
periodicity even if the original index is divisible by ell.

The complete-period identity (FV.5) follows directly by multiplying
the generalized Bernoulli generating series by `(exp(Mt)-1)/t`.
Every omitted term has valuation at least one because
`j-v_ell(j+1) >= 1` for j>=1 and ell>3. Odd character parity makes
every even generalized Bernoulli number zero. Taking
`r=1+ell(k-1)` gives both `r=k mod ell-1` and `r=1 mod ell`.
The relation `omega(a)=a^ell mod ell^2` permits division by
`f*ell` without losing the needed final modulus. Removing multiples
of ell changes the divided sum by an ell-multiple. The resulting
identity is precisely the normalized Bernoulli value, with no missing
factor of k or r. The nontrivial ell-character factor gives conductor
`f*ell` and the proof also establishes integrality of the twisted B1.

The quadratic class-number formula gives the first unit condition
because ell>3. The GD condition `(ell-1) ∤ 2e` excludes zero twists
and forces the first ell-part character to have order greater than
two. Thus the three-factor criterion is exactly the stated joint
unit requirement. It is a reduction; it establishes neither a
simultaneously suitable field nor the required converse exclusion
of automorphic systems.

The complete standard-library certificate was independently executed
from a byte-identical copy in this directory. All 171 finite-character
comparisons passed. The progression n=3,9,15,21 at ell=7 and conductor
3 has residue one in all four cases, including n divisible by ell.
The fresh JSON is byte-identical to the author's report.

- Script SHA-256: `8cb9b07dae206156815bbbdc74cb4deb3a6347498c88d45c211994bd16f34ce5`.
- Fresh report SHA-256: `5318ad0db9e30e6101c1d1b83622fcef790bbebaac438bbc70c8701dc62d3cc9`.
- All-row digest: `86778cec5d757ddf83452c539b8d496ab0f523d1457f2c29fa0bf87eceaa55dd`.

This is a source-level mathematical proof check and exact finite
execution; no Lean kernel build is claimed.
