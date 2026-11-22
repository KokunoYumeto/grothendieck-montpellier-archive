# Primitive positive-index connection lead — unproved

Recorded 2026-11-19T23:01:30.409242+00:00. This is a research note, not a promoted assertion or a rank result.

## Exact proved inputs

At actual local index zero, G=U P, where U is a nontrivial extension of O by O with class gamma and F gamma=0. Hence F*G is trivial of rank two, and all two global sections of Sym²G lie in its Frobenius-square subbundle F*G. The exact residual sequence is 0→E→G→i_*R→0. On smooth D, the induced quotient F_D*(G|D)→R² is surjective, so the two global sections give a base-point-free pencil S in H0(R²).

The residual boundary still has the additional term ker[H0(D,A G)→H1(Sym²G)] from the proved kernel formula. This term cannot be discarded. Nor can actual determinant directions Delta be replaced by H0(LP).

## Connection calculation to formalize

Choose gamma_ij²=f_j−f_i. In a global trivialization of F*U, its Cartier connection has one nonzero off-diagonal form eta_gamma=df_i. This form should be nonzero because if all df_i vanish, normality/perfectness gives local square roots and makes gamma a coboundary. It is locally exact, hence Cartier-killed. Tensoring by F*P gives scalar connection eta_P I plus that nilpotent off-diagonal. The forms eta_P and eta_gamma are independent invariant forms on the mixed abelian surface.

The needed exact identification is that the subline P→G→R gives the earlier norm section sigma in H0(RP), with the fixed determinant and P² normalizations. A raw off-diagonal trace-pairing calculation supports this but has not yet been written with all local units.

If that identification is made, global image sections z0=sigma²,z1 obey

    nabla z0 = eta_P z0,
    nabla z1 = eta_P z1 + eta_gamma z0.

Thus their ratio lambda=z1/z0 satisfies d lambda=eta_gamma on D. A nonzero horizontal constant combination of z0,z1 forces, after rescaling,

    r² = (eta_gamma/eta_P) sigma²

for a global section r of R. On a smooth ample D the restricted invariant forms are both nonzero, have disjoint zero divisors, and each zero divisor has degree 2b. If the right side is regular, its pole cancellation would force div(sigma²)=div(eta_P|D). In particular R² would be isomorphic to omega_D, equivalently A² would be isomorphic to omega_D.

Consequently, conditional on the typed connection/norm identification, A²≠omega_D would imply dim(S intersect Sym²H0(R))≤1: every two-dimensional subspace of the binary quadratic products contains a nonzero horizontal square combination. This still would not prove the required restricted surface-cup rank, because the extra twisted-pencil term and Delta restriction remain.

## A related local Gauss identity

For invariant derivations delta_o²=delta_o and delta_n²=0, and local smooth divisor equation w, put q=(delta_o w)/(delta_n w) on D where defined. The tangent derivation delta_o+q delta_n gives delta(q)=q; hence d log q=eta_P|D. This is compatible with q=eta_gamma/eta_P. The identity is independent of changing the local equation along D, but a complete typed write-up is still needed before using it in a theorem.

The functions lambda and q then have equal differentials, so lambda+q is a function-field square. Constancy is much stronger and is not implied. One possible way to exclude a horizontal global image is to prove lambda+q nonconstant for a suitable sharp source by actual section jets. No joint-jet surjectivity or generic nonconstancy has been established here.

## Unresolved constraints

Do not infer generic A²≠omega_D, h0(AP)=1, injectivity of H0(AG)→H1(Sym²G), or a lower bound on the actual restricted cup map from this note. An extra AP section can map nontrivially into H1(End^0V); simplicity of V alone gives no contradiction. Any future proof must retain actual KP as the determinant-direction kernel and must either work with smooth D obtained by the proved incidence construction or justify its nonreduced scope separately.
