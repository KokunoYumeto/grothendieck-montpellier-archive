# Complete independent audit of C.3bl

**Finite-certificate addendum, 2026-11-19T15:23:58Z:** I read the complete `../real_weil/code/check_C3bl_primitive_boundary.py` and every recorded output field and all 44 check outcomes in `../real_weil/output/C3bl_primitive_boundary_certificate.json`.  Inspection PASS; no independent rerun.  The author run began at 15:22:58.888027 UTC and took 0.04399013499642024 seconds.  The free rank-six quotient matrix has the indicated integral right inverse and kills the primitive anticanonical vector.  Its full tensor products multiply each of the nine retained ample matrices to zero.  The local adjoint matrices and finite projective chains have the correct commutator and positive metric.  The (m=0\) samples choose the third input in the cup kernel, a permissible special case of the textual independent-vector witness.  The 44 checks concern finite lattice products, local chains and tensor coefficients only; no geometric search or infinite-range theorem is represented as a computation.

**Reviewer:** GPT-6 Astra Pro, `/root/cycles`, RESEARCH_SA06; independent agent re-proof, not independent-model verification.

**Completed:** 2026-11-19T15:23:30Z.

**Object:** `../real_weil/C3_full_higher_integral_kernel_draft.tex`, all three proof steps and the complete universal integral injectivity corollary, together with its included final `../frobenius/C3_primitive_exceptional_boundary.tex`.

**Outcome: PASS in exactly the stated scope.**  For each algebraically closed field of characteristic (p>0), each (r\geq2), and each (N\geq2r), the construction gives an actual ordinary restriction-kernel class of exact order (p).  Its data can be selected over \(\overline{\mathbb F}_p\).  The universal integral injectivity classification follows after combining the separately proved lower interval.  No rational nonzero class, universal claim over each fixed field in the lower interval, or higher surjectivity conclusion is inferred.

## 1. Geometry and the new (m=0) endpoint

I rederived the dimension (N=m+2s+2=m+2r\), with (s=r-1\).  The elementary cubic cup has rank two in every characteristic, so the sections (s_i,t_i\) can be chosen with independent nonzero images.  When (m=0\), the three tensors in (C.3bl.3) are independent because their first factors are independent and all remaining factors are nonzero.  Their first two cup images are independent.  This is a valid nonempty rank-open witness even though the witness itself need not cut out a smooth divisor.

The external line bundle on \(\prod W_i\times C\) is very ample.  The immersion form of Bertini supplies a second nonempty open of smooth sections in the same irreducible affine parameter space.  The two opens therefore meet.  This argument has no dimension restriction beyond (s\geq1\), and is valid in every positive characteristic.  Since the data and opens are defined over finite fields, selecting a qualifying closed point by finite-field enumeration terminates.  The proof does not claim a uniform computational bound or an unperformed exhaustive search.

For (m\geq1\), the earlier section-tuple proof of transverse base locus and smooth incidence likewise has no dependence on the safe exceptional-lattice bound (m\geq r-1\).  I checked that the very-ampleness and Künneth vanishings used in both cases retain their full stated ranges.

## 2. The actual local scheme and its endpoint line bundle

The total-line equation is well typed.  The original quartic is smooth along the zero section; (F\nmid\ell H\) follows from the nondegenerate deformation choice and the nonzero degree-one coefficient.  The graph open is integral, and the codimension-two complement supplies no additional Cartier component.  The Segre contraction, finite normalization and vertex strict henselization therefore give the regular projective model already proved in bk.  The proof requires no new projection to the curve.  The projection to the product of projective/cubic factors is an actual morphism, so every divisor polynomial used by PB is an actual class.

I checked the scheme-theoretic equality \(\mathfrak m_R\mathcal O_{\mathcal Z}=I_V\), the normal line, and the split target for (f=\tau\ell\).  They remain valid when (m=0\).  Smoothness and connectedness of the target exceptional divisor follow from the ample smooth section and the displayed cohomology; its punctured split-line model is regular.

The first Picard-extension image has rank three because the coefficient sections are independent and the curve deformation form is nondegenerate.  The ordinary Verschiebung kernel maps with span exactly that vector subspace.  Since the product cup is a nonzero linear map on its span, some actual kernel point has a nonzero cup.  This does not require every vector in the subspace to be a finite kernel point.

The target first-neighbourhood vector coordinate vanishes on the proper abelian lift.  Its remaining Picard coordinate factors through Verschiebung.  The selected kernel point consequently restricts trivially at first order.  The higher (H^1\) vanishings give uniqueness of the trivial formal extension on the target.

The proof constructs the source endpoint on the fixed product with a smooth proper curve.  Pulling the normalized Poincare bundle along Verschiebung kills the first obstruction; the higher family obstructions vanish by Künneth and the dimension-one parameter.  Projective formal existence followed by finite-data Popescu and henselian smooth lifting preserves the prescribed first jet on that same product.  The exact order-(p\) endpoint argument uses first-order (p\)-annihilation and higher uniqueness, then the already established completion comparison.  It is not a replacement of an actual family by a family on a varying henselized product.

## 3. The entire exceptional image

I previously independently re-proved all of PB.1–PB.18, and then read its actual final integral quotient replacement for Step 3.  The detailed receipt is `C3_primitive_exceptional_boundary_independent_REVIEW.md`.  Its hypotheses are all explicitly verified by (C.3bl.2), (C.3bl.5) and the actual projection.  The designated nonzero cup is exactly (C.3bl.6).

In particular, the extra torsion in the exceptional multiplication kernel is retained through the exact Smith decomposition.  The free integral tensor quotient kills its saturated ample image before reduction modulo (p\).  The remaining curve-line products have a unique relative Milnor class; their differential is independent of the chosen actual lift and is additive from the divisible curve Picard group to a group killed by (p\), hence zero.  The actual Chow projection formula and finite smooth-model Milnor–Bloch comparison then kill the whole exceptional image in the chosen component.  This is sufficient to show the displayed product is nonzero on (X\); no false integral hard Lefschetz assertion is used.

The product family proves ordinary algebraic triviality, its restriction is zero, and multiplication by (p\) kills it because it kills the actual Picard endpoint.  Nonvanishing therefore gives exact order (p\), without any divisibility or factorial ambiguity.

## 4. Universal corollary and source scope

For (N\leq r\), the puncture has no codimension-(r\) points, so the source group is zero.  For (r\geq2\), the intervals (r+1\leq N\leq2r-1\) and (N\geq2r\) are exhaustive.  The former uses C.3aw with its specified transcendental coefficient field; the latter is the present every-field construction.  The degree-one result is exactly C.3bh.  The asserted universality is therefore correct and does not silently strengthen the fixed-field lower interval.

Exact primary inputs were freshly checked in this same audit window: the individual Bertini lemma **Stacks 0FD6**, Jiang's integral projective-bundle and blow-up maps, Stacks **02TX**, and the formal/actual inputs **0C6R**, **0885**, **0AH2**, **07GC**, **0B8W**, **0H74**.  The earlier complete Rost, Kerz and Braunling reads and their precise hypotheses are recorded in our bj/bk and all-degree auxiliary receipts.  The final PB Euler calculation was additionally checked against **01XS**.  No new theorem or unverified general Picard representability statement is imported by bl.

No bl-specific computation has yet been inspected or rerun in this receipt.  The geometry and all-degree conclusion above have been checked by proof, while the separately inspected bk and lattice certificates retain their own exact limited scopes and runtimes.
