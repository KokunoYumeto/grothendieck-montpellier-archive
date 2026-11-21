# Further approaches to the actual multiplicity comparison

Run `GCT_KRON_20261120`; formulas worker `/root/positive_formulas`. The convention throughout these conclusions is the internal padding `X11^(n−m) perm_m` used in the supplied IP and BIP sources. The matrix identities also admit other substitutions for the padding form, but no external-padding shape bound is substituted into the cited theorems.

## 1. Recovering actual multiplicities from Young sets and wreath invariants

The Young-set formulas and wreath-group invariants determine the ambient multiplicity space `M_lambda`. They do not by themselves determine which copies survive an orbit-closure quotient. F-010 identifies exactly the missing datum: the component of `f^d`, viewed as a map `T_f,lambda : M_lambda → S_lambda V*`. The actual coordinate-ring multiplicity is its rank.

A factorization of the permanent evaluation map through the determinant evaluation map would suffice, but requires kernel inclusion and is stronger than the desired rank inequality. Neither positivity of the ambient representation nor simultaneous nonzero rank supplies it. The explicit two-column GL2 example in F-010 gives multiplicities one and two for different orbit closures in the same ambient representation, with the same irreducible present in both. This is a precise obstruction to the proposed inference; it is not a counterexample to a permanent-specific comparison.

**Current gate:** for the residual shapes, compare the ranks of the two specific evaluation tensors, or prove a sufficient kernel inclusion. No general rank inequality is established.

## 2. Universal projected forms

The parent construction M-007 gives the balanced two-trie determinant for every padded form in a bounded number of variables. Its use through the projection lemma compares actual multiplicities. O-010 proves that the resulting fixed-variable asymptotic threshold is optimal for this universal replacement method: at `n=m^c`, universal containment in a fixed number of variables forces at most `2c+1` variables.

**Failure point beyond that threshold:** the full space of padded forms has dimension greater than the determinant-image bound. This rules out replacing every projected permanent by every degree-m form in that many variables. It does not rule out using specific properties of permanent projections.

The parent's M-009 avoids that failure by preserving the evaluation of one highest-weight space instead of preserving the whole projected form. The precise weight-box truncation, Borel alignment, and capped-trie proof passed the independent review recorded in this worker's log. This is a strict shape-dependent improvement, not another assertion of universal containment.

## 3. Permanent-specific subset-lattice construction

The known Grenet construction, in the homogeneous form F-009, proves full orbit-closure containment once `n≥2^m−1`. Its cycle proof uses the specific permanent labels and hence goes beyond the ambient lambda object. It excludes every actual multiplicity obstruction, without a row or degree restriction.

At the minimum IP scale `n>3m^4`, this proves that the permanent size must be at least 19 for an actual obstruction to remain possible. At the minimum BIP scale `n≥m^25`, it must be at least 190. The cutoffs are exact for this numerical comparison, with symbolic determinant identities and exact integer certificates retained.

**Failure point:** the proved construction is exponential in m. For `m≥190` at the BIP minimum scale, the inequality `2^m−1≤m^25` fails permanently. This is a limit of that particular upper-bound argument, not a lower bound against improved representations of the permanent.

## 4. Scalar multiplicity and near-rectangle families

F-011 computes the entire ambient coefficient for `lambda=(d(n−k)+k,k^(d−1))`: it is one for even k and zero for odd k, with the degree-one exception stated separately. The calculation uses the Cauchy decomposition, a balanced torus-weight line, and the orientation character of its determinant twist.

In the BIP no-occurrence range, every actual obstruction must have permanent multiplicity at least two, and therefore ambient multiplicity at least two. Consequently the whole F-011 family is excluded there. In the IP range alone, the corresponding argument excludes the sufficient ordinary-Kronecker test; it is not promoted to an actual-closure comparison.

F-012 extends the same mechanism to mixed tails of the form `((k+1)^s,k^(d-s-1))`. The balanced-weight hook module is exactly the exterior power of the augmentation representation. Every intermediate case `1≤s≤d−2` has zero ambient multiplicity, independently of the padding scale. The two nonzero endpoints reduce to F-011. These are actual candidate exclusions supplied by exterior lambda operations with signs retained.

The k=2 scalar family has a stronger conclusion in the obstructions worker's O-011: `K=a=1`, and the internally padded permanent has `q=1` exactly up to its m²-variable length limit. I independently checked that full Hessian proof, including the exceptional all-ones calculation at `(m,n)=(3,4)` and its alternative explicit point. Thus this family is excluded for all `n>m`, even when it has many more rows than the general projection theorem covers.

## 5. The earlier remaining gate

The arguments do not decide the rank comparison for ambient multiplicities greater than one outside the shape-sensitive projection bound. An occurrence theorem cannot compare those positive ranks. Semigroup multiplication can construct nonzero highest-weight vectors, but by itself does not control the dimension of their span or the kernels of their evaluations. A further step must therefore supply additional permanent-specific geometry or an explicit comparison of multiplicity spaces.

These are gates for the actual `q>K` question. The stronger sufficient criterion `q>g` has additional restrictions, such as the cited IP degree inequality `d>n/m`, which are not imposed without justification on every actual multiplicity obstruction.

## 6. All-copy stabilization and coefficient support

F-013 computes rectangular-shifted two-row ambient multiplicities by exact rectangle partition differences, with the staircase shift required by an odd determinant twist. Its explicit coefficient-four family shows that the normalizer calculation reaches beyond occurrence. The original concern was that a single nonzero determinant value would not settle its four-dimensional multiplicity space.

F-014 removes that concern in a broad regime. Products of flag minors span the whole row highest-weight space because their nonzero column-group-stable span is an irreducible Cauchy module. A fixed column has at most `lambda2` entries below the first row. Balanced column degree therefore makes every polynomial divisible by the same first-row power. Division and inverse multiplication commute with column permutations, proving stabilization at inner degree `lambda2` for every copy. The degree-split graph and invertible padding pullback then give `K=a` under the explicit bound `n≥B(lambda2,r)`, at arbitrary outer degree.

The parent and archive workers independently reviewed a new primary Foulkes–Howe preprint and used it to derive M-010, the full ambient equality when `d(d−1)≤n`; this formulas worker has not independently read that source proof and does not count it as its own proof check. That degree gate already disposes of maximal-row families in the BIP range. F-014 remains useful beyond it because the argument does not require `d=r` or even comparable sizes.

F-015 restricts the padded coefficient space to the exponent box seen by the whole highest-weight space. It is not necessary that this box be Borel stable. All relevant polynomials already lie in its coordinate subalgebra, while the ambient padding lift is Borel semi-equivariant and its actual pullback is diagonal invertible on that subalgebra. This gives full `K=a` under the smaller capped graph counts.

## 7. Terminal supports and the mixed graph

F-016 strengthens the box: in each column, at most `lambda_j` flag-minor factors can contribute any variable in rows j through r. Consequently every coefficient generator used by every highest-weight vector satisfies the terminal exponent-sum bounds. The tensor-product monomial basis and disjoint column-permutation orbit sums make the passage to the coefficient algebra explicit; there is no unproved assertion about cancellation.

After stabilization this yields another full-multiplicity criterion, including `n≥lambda2+binom(r−2+lambda3,lambda3)`. Applied directly before stabilization, the same support statement gives M-011's actual comparison at permanent degree m, including shapes with `lambda2>n`. The O-015 example has `m=256,n=2^200,d=3n,lambda2=2n` and at least four permanent-side copies; it is excluded by the new comparison even though all inner-degree stabilization criteria fail.

F-017 improves the graph itself. It splits the early variables between two trees, uses two distinct copies of the later-variable monomials, and places one later variable on the coefficient edge. Splitting the remaining later degree gives the explicit product-of-binomial size formula. The determinant-cycle proof is supplemented by three symbolic identities, nine exact integer identities including zero padding, and thirteen rational size checks; these are saved in `mixed_tail_graph_certificate.json`.

The resulting necessary conditions are now a staircase. At `n≥m^25`, every actual obstruction must satisfy `lambda_(54−2s)≥s+1` for `1≤s≤25`, hence `lambda4≥26,lambda6≥25,...,lambda52≥2`. At `n>3m^4` the corresponding requirements are `lambda2≥6,lambda4≥5,lambda6≥4,lambda8≥3,lambda10≥2`. These restrictions hold for every outer degree and do not assume `n≥lambda2`.

## 8. What the current construction still does not prove

The mixed determinant graph is a sufficient support representation. Failure of its size inequality is not a lower bound on determinantal complexity, nor does it imply that a permanent evaluation rank exceeds a determinant evaluation rank. The remaining exact comparison remains F-010's pair of evaluation tensors after imposing all proved size, degree, support, and positivity gates.

A possible next refinement is to optimize over two downward-closed monomial sets whose sum, together with zero or one unit vector, covers the whole required support. The same cycle construction then has size equal to the two set sizes minus one. This would unify the fixed split constructions and make their exact optimization problem explicit, without asserting an efficient optimization algorithm or an effective Burnside lift. It still needs specific small support covers to move the unresolved rank comparison further.


## 9. Full support covers and exact permanent copies

F-018 now proves the proposed finite optimization. For a downward-closed support Gamma, choose two downward-closed subsets P,Q whose sum together with zero or one unit vector covers Gamma. A fixed decomposition of each supported monomial gives a single coefficient edge and a determinant of size |P|+|Q|−1. The minimum kappa is finite, at most |Gamma|, and at least the maximum supported total degree. There is no claim that this is the optimal determinant size among all architectures.

At permanent degree m, n≥kappa(Gamma_m,lambda) excludes the actual obstruction by ideal inclusion. At stabilized degree lambda2 it proves full K=a. With positive tree labels the same graph computes a permanent; a noncentral diagonal is exactly the padding form. After moving it to X11, the internal-padding convention is preserved. Consequently kappa≤m proves q=K=a for the entire multiplicity space. This is an exact permanent-side equality, although it does not add a new q≤K exclusion where the determinant criterion already applies.

The ongoing strict-profile example uses two simultaneous terminal bounds and therefore a support much smaller than every one-cut enlargement. Its all-copy comparison is proved by kappa≤|Gamma|; four genuine permanent-side copies are supplied by the binary seed and a common nonzero Hessian multiplier. The obstructions worker owns the detailed example and the dimension comparison, so its completed file and independent review, rather than this prospective description, govern the final claim.


## 10. Jet dominance and the new remaining boundary

M-013 improves the full-copy determinant comparison without exact containment of the truncated form space. An explicit acyclic pencil has cofactor derivatives equal to all monomials through a prescribed jet order. The unit Jacobian minor injects the jet coordinate algebra after arbitrary base change; the multiplicity consequence remains in characteristic zero. At n at least m^25 it proves lambda2 at least 27 for every surviving actual candidate. Together with F-017, the full staircase is `lambda_(2j)>=28-j` for 1<=j<=26.

O-019 shows why merely extending this whole-jet target cannot improve indefinitely: at r=m^2,n=m^c, dominance onto all jets of order b eventually requires b<=c+1. That dimension obstruction is methodological; it does not show that any particular highest-weight ideal component or actual permanent obstruction survives. O-018 instead uses the full nested support and proves the independent joint gate `lambda3>=139 OR lambda52>=3` at the BIP scale. Its strict profile example has at least four genuine permanent copies and defeats every one-cut universal enlargement while the full nested support still fits a determinant.

O-020 supplies a complementary full-copy comparison: n>=2r-4 and lambda3<=2 imply K=a with arbitrary lambda2 and outer degree. The detected coefficients form the second infinitesimal neighborhood transverse to a binary plane. This is a geometric injectivity result, not a claim that every truncated form itself has the same-size determinant.

## 11. Closing special formulas without conflating them with a general gate

F-020 gives the exact Kronecker multiplicity for two hooks and a two-row output, including the overlapping hook outputs k=0 and k=1. Its interval cancellation is positive and every value is 0, 1, or 2. The arXiv-v1 Rosas Corollary 14 expression has a literal overlap issue at k=1; the finding records that version-scoped correction without attributing it to an unexamined later version. A complete exact character check covers 1967 cases.

The archive worker's A-024 gives a positive polynomial highest-weight algebra for the known two-row rectangle-square rule. Its four invariant generators and unique monomial basis are stronger data than virtual K0 classes, but only for that special multiplicity-free family. They do not provide the missing comparison of the permanent and determinant evaluation kernels in F-010.


## 12. Full permanent multiplicities and strict support-cover separation

F-021 transfers the compressed-tree jet method to the internally padded permanent. A permanent cofactor of an acyclic matrix is a positive sum of directed path monomials. The selected cofactors are single monomials, and fixing X11=x1 removes no required direction. Hence every ambient copy survives on the permanent whenever m>=J_b(r), giving q=K=a without an outer-degree bound. The cyclic star also gives q=K=a at m>=r^2 for second row at most five.

For the full degree-four simplex, every exact F-018 cover must place at least one pair inside each four-subset. Double-counting yields kappa>=1+ceil(R(R-1)/12). At r=1024 this is at least87127, whereas the jet matrix has size65536. With m65536,n65537 and d2048, the tail (4^1023) has at least two ambient copies, distinguished by divisibility by the leading coefficient, and F-021 proves both actual multiplicities equal the full ambient one. Thus the jet conclusion is strictly outside every exact support cover in that defined architecture. It is not a lower bound for all possible matrix representations.

The independent geometric improvements now also include O-020 at n>=r-1 for lambda3<=2, and M-015 at n>=r^2 for lambda2<=5. M-014 gives the complete general staircase lambda_(2j)>=c+3-j at n>=m^c, c>=6. These remain sufficient exclusion methods; outside all their inequalities the unresolved object is still the pair of evaluation ranks in F-010.
