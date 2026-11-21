# D-OL-12–13 — independent whole-proof audit

**PASS. No mathematical repair requested.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. The complete frozen proof, complete author program, author output and exact source-interface note were read. The new universal arguments were checked in full, and a separate exact supplement was executed.

Frozen proof: `agents/imprimitive/orthogonal_lowlevels/orthogonal_odd_nonselfdual_section.tex`.

SHA-256: `0ed85dfb4a94ac000e411e22a2c9735157c2bd8fa606ff4d7c507c66cf8f2921`.

Author code and output: `check_orthogonal_odd_nonselfdual.py` and `orthogonal_odd_nonselfdual_checked.json`. They report a successful complete execution at 22:05:08.867398 UTC in 0.118284012 seconds. I read them in full; no fresh execution of that author program is claimed.

## 1. Prime powers and signed hyperbolic pairs

In the stated large odd natural dimension, the ordinary group `S=Ω(V)` is simple and centerless. The projective kernel of a nontrivial irreducible complex module is trivial: it is normal, and the alternative that all of the perfect group acts by scalars is impossible. Therefore a nonidentity prime-order power of an inner operator remains nonscalar. Taking powers cannot increase projective support.

If an `ε`-eigenspace contains a hyperbolic pair, its orthogonal complement is stable. I checked the actual conjugation formula for the abelian line radical: the weight action is `A=ε g|W`, rather than automatically `g|W`. The factor `ε` matters. If `ε=−1`, the original prime order is two and `A²=I`; otherwise the prime order is unchanged. `A` cannot be the identity, because that would make `g=εI` on all of `V`, contrary to the selected nonidentity element of `S`.

The proof correctly permits `rank(A−I)=1`. In particular, minus a natural reflection can have determinant and spinor norm one. No rank-two assertion from an even-dimensional or unsigned calculation is silently used.

The two opposite line radicals are conjugate and generate `S` in the previously proved range. Their invariant spaces have equal dimension and zero intersection in a nontrivial irreducible module, so the radical-invariant dimension is at most `a/2`. This is an actual restriction argument, not a claim that the whole representation remains irreducible on a Levi subgroup.

## 2. Uniform Gauss and orbit estimate

For `X=ker(A−I)`, its perpendicular space is `im(A−I)`, so the radical of the restricted polar form has dimension at most the moving rank `r`. Hence its polar rank is at least `N−2r`. When `r≤N/2`, the quadratic Gauss error is at most `q^(N/2)`; when `r>N/2`, the trivial point-count bound is already at most that quantity. The ceiling in the displayed error safely covers both parities of `N`.

The nonzero weight orbits are the actual norm levels, and the full Levi action makes their multiplicities constant. The denominator removes the zero vector where appropriate. Dividing the exact upper and lower counts by `q^(N−1)` gives the stated uniform ratio

`(q^(-1)+q^(-9))/(1−q^(-9)−q^(-19))`.

It decreases with `q`, and its value at five is strictly below one quarter. This monotonic argument is valid for every odd prime power `q≥5`; it is not an extrapolation from the finite supplement. The remaining weight orbits have full prime length, and component recovery works with arbitrary phases. Together with the radical-invariant bound, this gives support at least `3a/16`, which is strictly stronger than `δ* a`.

## 3. Exhaustion when no such pair exists

For prime order different from the characteristic, the `±1` eigenspaces are nondegenerate. A finite-field nondegenerate quadratic space of odd characteristic and dimension at least three contains a hyperbolic pair. Thus each of these eigenspaces has dimension at most two, giving restricted natural support at least `d−2`.

For prime order equal to the characteristic, the operator is unipotent. Its fixed subspace has polar rank at least `d−2r`. A polar rank of at least three would again give a fixed nondegenerate three-space and a hyperbolic pair. Hence `r≥(d−2)/2`, and the integer lower bound at odd `d=1135` is 567. The operator `g+I` is invertible in odd characteristic. These cases exhaust prime-order operators and establish the required minimum over precisely the scalar set `{1,−1}`.

Inflating an ordinary `Ω`-module along `Spin→Ω` preserves its irreducibility and nontriviality. It need not be faithful, and the cited character estimate imposes no such requirement. The natural orthogonal action and the restricted-support calculation are unchanged. The exact published exponent at `567=7·9²` gives the displayed `(19/20)^9` ratio. The triangle inequality `|χ(g)|≥a−2ν(g)` then gives the strict support bound `δ* a`.

## 4. Every compatible linear and semilinear normalizer

The odd-dimensional determinant identity makes the multiplier of a natural linear similitude a square. Thus `GO=F*O`. Also `O=⟨−I⟩×SO` and `SO/Ω` has order two, leaving exactly one possible nontrivial linear outer coset.

I checked the Clifford argument carefully. If that coset stabilizes the irreducible `ρ`, then all of `O` stabilizes it, since the remaining central `−I` acts trivially by conjugation. Every irreducible constituent of `Ind_S^O ρ` restricts to a positive multiple of `ρ`. Full `O` has real-valued irreducible characters; therefore this multiple, and hence `ρ`, would be real-valued and selfdual. This contradicts the hypothesis. The argument requires neither an arbitrary extension of `ρ` to `O` nor a character-field equality. Consequently every compatible linear normalizer is scalar times inner.

For a general compatible normalizer, the proof takes a nonscalar power of prime projective order before examining its field component. A nontrivial field part has that same prime order. The previously checked arbitrary cyclic descent applies to the full mixed linear-field lift: its projective scalar power is norm-rescaled away, its quadratic form is rescaled, and a fixed basis exists without division by the extension degree. The resulting hyperbolic pair and line radical are defined over the fixed field. The uniform fixed-weight proportion from ON.9 is below one quarter, giving at least `3a/16` support. No assumption that the linear and field components separately stabilize `ρ` is inserted.

The full natural semilinear-normalizer coverage, including its centralizer/cardinality argument, is the already reviewed OL07/09 interface. The present proof uses it on all compatible operators rather than on a chosen subgroup of outer automorphisms.

## 5. Tensor and geometric consequences

Convolution preserves the lower support fraction of an active nonscalar tensor factor. A genuine tensor permutation has the stronger quarter bound. A genuine nonidentity scalar has full actual moving rank. These facts cover mixed odd fields and natural dimensions as stated.

The elementary `k=1` specialization of the published degree bound gives `a_i≥q_i^(d_i−4)(q_i−1)>28`. The actual multiplicity Euler identity rules out genus at least two. Genus one has moving sum six, at most six genuine branch points and period image dimension at most six. Thus an actual rank-nine source would have genus zero, at least twelve genuine inertias and moving sum `2e+6`. The strict support estimate forces

`e < 1536000000000/55936906663 < 28`,

contradicting the degree floor. This is a necessary constraint on the actual intermediate variation, with no sufficiency inference from parameter counts and no identification of inducing and original fields.

Selfduality is invariant under automorphic pullback. Therefore in the transitive case the factor modules are uniformly selfdual or nonselfdual. The earlier OL09 bound handles the former; the new theorem handles the latter, yielding the stated odd integer cutoff `d≤1133`. The proof does not extend to arbitrary faithful spin characters or assert existence within the remaining interval.

## 6. Primary-source reading

I freshly reopened and read the complete invoked KTV passages, printed pp. 39–45, including the full-group reality statement, the exact determinant/spinor quotient definitions and the distinction from the derived group's reality. Source: Kim–Trefethen–Vinroot, *Reality properties of finite simple orthogonal groups*, AGTA 16 (2023), 39–66, DOI `10.32037/agta-2023-007`; <https://www.advgrouptheory.com/journal/Volumes/16/KimTrefethenVinroot.pdf>. Theorem 1 on p. 44 is the published restatement actually read. No fresh reading of Wonenburger's original article is claimed.

For LST2011, the complete theorem proof was previously read in this run. Here I reread the exact theorem and bound on pp. 1917–1918, its final parameter choice on pp. 1922–1923 and Remark 4.3.7 on p. 1923 from the retained published text. The restricted scalar set for Spin, absence of a faithful-character condition and threshold 567 were checked at the actual application. Source: <https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>.

I also reread the published GLT2024 Theorem 3.7 and the invoked proof passages on pp. 165–167 from `orthogonal_levels/cache/GLT2024_published.txt`. The `k=1` bound is directly `q^(d−4)(q−1)` in this range. The earlier full Li–Xia, Taylor and cover-source checks retain their recorded scopes; the pertinent OL06/07/09 constructions were reread at their uses. No new classification theorem is inferred from the finite data.

## 7. Independent exact supplement and boundary

The separate `audit_orthogonal_odd_nonselfdual.py` imports no author code. The author code had been read beforehand. It reconstructs norm distributions by cyclic convolution of directly counted binary hyperbolic and unary square-value distributions, rather than the author's exhaustive vector loops. It checks **216** distributions, for nine odd primes, twelve numbers of hyperbolic planes, and both square classes of the final line coefficient. This is a count of exact distributions, not a claim to enumerate all vectors of the largest spaces.

A different thirteen-dimensional symbolic model uses twelve reflections with total spinor norm one. It verifies the orthogonal and abelian-radical identities and the exact signed conjugation, whose induced weight action has moving rank one. Every universal endpoint constant is also checked with rational arithmetic.

The first execution completed its assertions but failed while serializing the SymPy integer `One` into JSON. Only the output conversion `int(spin)` was changed. The complete program was rerun and passed at **2026-11-21 22:10:14.961093 UTC**, in **0.070781199 seconds**. The failure and repair are retained in `audit_orthogonal_odd_nonselfdual_attempts.json`; final output is `audit_orthogonal_odd_nonselfdual.json`, bound to the exact frozen proof hash.

The independent convolution reproduces the characteristic-three rank-one counterexample: in weight dimension 23 the fixed fraction is `29525/88574>1/3`. The symbolic signed action shows why such rank-one actions cannot be discarded by an incorrect determinant argument. This refutes the attempted uniform quarter fixed-fraction bound at `q=3`; it does **not** prove or suggest existence of a curve source there.

All universal representation, normalizer and geometric conclusions rest on the written proofs, not finite extrapolation. TeX compilation was not performed or claimed.
