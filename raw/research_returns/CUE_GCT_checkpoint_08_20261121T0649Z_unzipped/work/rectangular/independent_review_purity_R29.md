# Independent whole-proof review of R-29

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run CUE_GCT-20261121-purity. Actual review completed 2026-11-21 05:49:17 UTC.

**PASS** after a complete reading and independent rederivation of `r29_fragment.tex`, SHA256 `eef867fae9987faeb97cc87bc8ea0751eb65118ebd337a3247c697358d0e4bf3`. No repair requested.

## Prescribed product spectrum

The rational positive spectrum is first cleared to an integral partition, and its extremal flag weight removes the traceless part of the ordered Fourier tensor's moment. The condition k<=m-1 supplies at least k+1 full-spark factor lines, so the ordered tensor has finite projective stabilizer. Equality of every one-parameter minimum weight transfers stability to the multiplied enhanced product tensor.

The reverse Kempf–Ness direction is applied to that closed nonzero enhanced orbit, not to the unenhanced product alone. A unitary transformation maps the resulting partial flag to the fixed standard flag; this follows by an orthonormal basis adapted to its nested subspaces. Normalizing the auxiliary vector only changes a scalar and does not change its moment. Unitary equivariance and the induced pure-power metric therefore give `d M(P)-diag(theta)=c I`; the trace equation gives c=lambda_k exactly. This proves the claimed full moment spectrum without any additive-moment assumption for a polynomial product. The coordinate permutation and harmless special-unitary scalar adjustment preserve the argument.

The transformed factor lines remain distinct and contain a projective frame. A projective symmetry of the product permutes them; its permutation kernel fixes that frame pointwise and is trivial in PGL. Thus the product has finite projective stabilizer.

## Two-block construction

Both block dimensions lie in [2,m-1] precisely because 4<=r<=2m-2. The normalized spectra mu_i/w_b have sum m. The two products are orthogonal unit forms, so the chosen square-root coefficients give a unit sum and the required weighted block moment. Off-diagonal infinitesimal actions land in mixed bidegrees orthogonal to both pure blocks.

I checked the finite-stabilizer proof separately: the directional derivatives of each product are independent by restriction to each distinct factor hyperplane and the spanning of its factor lines. For m>=3 the two mixed bidegrees differ from one another, so no cancellation between the off-diagonal blocks is possible. Both off-diagonal blocks vanish. Each remaining block is scalar by the finite projective stabilizer of its product, and the common degree-m scalar equation makes the two scalars equal. This is a characteristic-zero projective Lie-algebra computation, exactly as stated.

## Common enhanced cones and absence of a period

The two-matching cycle pencil gives the sum of the two products as both a permanent and a determinant after the stated sign adjustment. The ordered padded tensor has the required moment and a finite stabilizer inherited from q. Minimum weights, rather than an unsupported moment formula for multiplication, establish stability of the padded polynomial tensor.

The enlarged affine parameter family is irreducible. It separately contains the stable two-block point, a finite-projective-stabilizer point, and the Eisenstein irreducible witness `x1^m+x2^(m-1)*x3`; all three required conditions are nonempty opens. Irreducibility persists on adjoining unused variables. After their intersection, a generic padding line avoids every fixed locus of the finite projective group while preserving stability. Unique factorization works also at padding exponent one. The center acts trivially with exponent `ns-|eta|=r*nu_r`, so R28's closed-orbit and numerical-semigroup argument supplies gcd one and occurrence at every integer stretch at least beta^2.

The coordinate-ring extraction and quotient dimensions from G22 depend on the existence of a stable point and the Cartan grading, not on r<=m. The final extension of that argument is therefore valid. The last scope statement is also exact: if r>m and n>m are integers, `r*m/(r-1)<=m+1<=n`, so no strict rectangular direction exists in that added range.

## Source and review scope

I used the previously checked G22/R28 and their cited Kempf–Ness, Hilbert–Mumford, openness, and invariant-separation inputs. This event does not claim a fresh complete proof audit of Losev or Mukai, nor an algorithm for the normalizing transformation or its coefficient heights. It is a full mathematical reading of the new written proof, not an external referee or formal proof-assistant certificate.
