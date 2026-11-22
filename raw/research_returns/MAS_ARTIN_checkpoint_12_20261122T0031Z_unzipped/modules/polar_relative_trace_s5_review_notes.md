# Independent complete review of MA-MO-021

Date: 2026-11-21, UTC. Reviewer: GPT-6 Astra Pro, `/root/s5_audit`; effort inherited/not externally exposed.

## Result and version

**PASS.** I independently read the complete written `polar_relative_trace.tex`, MA-MO.440–449, and then verified the final additive-cutoff pullback and prime-witness support clarifications. Reviewed SHA256: `da52a2b078b6fa82b34888f1618092f9d55c52c0bd5ca7f1e1cf5b67f35e20a9`. No mathematical correction remains.

The relative operator E is a genuine trace-class endomorphism preserving the positive completion. The raw full matrix D remains a different operator. Its trace is evaluated on its actual W domain; it is not assigned a quotient trace. Both uses of the explicit zero-free half-plane remain recorded.

## Complete proof checks

### The finite-rank term

The actual source-section coordinates give `Id-P_-` as two bounded polar input columns `v_j=(-r_j,e_j)`. Its rank is two, and composition with bounded C_g has rank at most two. The trace is the sum of the two polar coordinate functionals applied to `C_g v_j`. The translation representation on the polar quotient has characters `exp(-t/2)` and `exp(t/2)`, so this trace is exactly `G(-1/2)+G(1/2)`. Invariance of the range of `Id-P_-` is neither true by necessity nor used.

Subtracting the actual S1 operator D_g from this finite-rank term gives E_g and agrees on the dense original smooth common space with `C_g(Id-P_+)`. This defines the operator before any quotient or trace comparison.

### Source restriction and quotient

I rechecked the actual source formula against the Meyer definitions already freshly read for MO018. On the even rational source, the original approximate positive operator satisfies `p_+ i_+=Id+L`; it is not a projection. The additive cutoff in the final text is explicitly the pullback `phi(log|t|)`, extended by one at zero. The sign of the restriction is therefore `E_g|W_+=-L_g`, not `+L_g`.

The positive smooth source is invariant under this original action and is dense in the closed W_+. Continuity proves invariance of W_+. Its restriction agrees with the MO017 endomorphism on that dense source, so boundedness gives equality on the completion and trace `-tau`.

On any smooth common vector, `C_g P_+` lands in the positive source image. Consequently `q E_g=q C_g` on the dense common source. Both sides are continuous, so the identity holds on all W. The equivariant quotient map then identifies the induced operator with the actual C_g on H/J. No bounded extension of bare P_+ is assumed in this step.

### Trace and determinant

With the orthogonal decomposition by W_+, E_g is upper triangular and its quotient block is the isometric Hilbert quotient operator. Trace class of both diagonal blocks follows by compression. Absolute convergence of the two orthonormal-basis trace sums gives the first equality in MO.442, and subtraction from the finite-rank trace gives the second with the exact signs.

The determinant proof uses direct-sum finite-dimensional projections adapted to the invariant decomposition. Their compressions converge in trace norm. Each finite matrix is upper triangular, so its determinant factors. Fredholm determinant continuity gives MO.443 for every complex z. The factorization concerns E_g; no corresponding factorization for D_g is asserted.

### Full retained divisor and prime evaluation

The same half-plane premise and functional reflection put every nontrivial zero uniformly inside the strip. Thus the actual all-weight quotient trace theorem applies with every multiplicity retained. The maximum/sum exponential norms define boundedly isomorphic quotients, so this change of metric preserves trace. This is the second explicit use of the zero-location premise.

I independently checked the gamma normalization in addition to reading MA-TR.2–4. Differentiation of `m(z)=Gamma_R(1/2+z)/Gamma_R(1/2-z)` gives the sum of the two gamma logarithmic derivatives. Pairing their integral representation with G on the central line, and using `g(0)=0`, gives minus the integral with kernel `exp(-x/2)/(1-exp(-2x))` and test `g(x)+g(-x)`. Hence tau equals `-A_0(h)` with `h(exp x)=g(x)`. The full explicit formula in the established convention then gives precisely the positive finite-prime sum in MO.444. Compact support makes it finite.

For arbitrary g, the nonsymmetric-cutoff term `g(0) integral psi` remains in tau. The proof keeps it. For the stated prime witness, support meeting the prime-power logarithms only at `log 2` with value one there gives `log 2/sqrt(2)` and automatically avoids the value-zero issue if its support is chosen away from zero.

## Scope

This independently verifies a real evaluation of the full common-space trace under MO018's premise. It is compatible with MO020's rank-two failure of positive-space invariance for the raw matrix, because the invariant relative operator is E_g instead. It neither proves the half-plane premise nor removes FT002's arithmetic condition without that premise.

Fresh source/interface scope: the original Meyer source maps and `p_+i_+` formula were read in the immediately preceding complete MO018 review; the MO017 nuclear source return was completely reviewed separately; the completed-quotient and explicit-formula normalizations were checked at MA-TR.1–4 and the exact all-interior scope of MA-WP. No fresh full audit of the entire Meyer paper is claimed here.
