# Candidate algebraic refinement for residual quadratic images

Status: candidate proof, awaiting the tensor agent's second review and the root's literature comparison. This is an algebraic comparison for the image-substitution method, not a norm-derived lower bound and not a novelty claim. Agent /root/geometry_dictionary, GPT-6 Astra Pro; effort not exposed; run GCT_GINEQ.

## QI-01 — Minimum matrix rank in the 2×2 minor and permanent spaces

Let E be the complex vector space of n×n matrices, n≥2. Let U_−⊂Sym²(E*) be spanned by the 2×2 minor polynomials

 x_ij x_kl − x_il x_kj,  i<k, j<l,

and let U_+ be spanned by the analogous 2×2 permanent polynomials with a plus sign. Regard each quadric Q as its symmetric coefficient matrix, equivalently its polarized bilinear form B_Q on E. Then

 min_{0≠Q∈U_−} rank B_Q = min_{0≠Q∈U_+} rank B_Q = 4.

### Proof

For either space, Q has the following two properties.

1. It vanishes identically on the coordinate subspace of matrices supported in any one row, and on the coordinate subspace supported in any one column. Consequently its polarized form is zero on each such subspace times itself.
2. For distinct i,k and distinct j,l, the polarized coefficients satisfy

 B_Q(E_ij,E_kl)=± B_Q(E_il,E_kj),

with minus for U_− and plus for U_+. Indeed, these two monomials belong to a unique corresponding 2×2 minor/permanent, so their coefficients have the stated relation in every linear combination.

Suppose 0<ρ=rank B_Q≤3. Let L:E→V=E/rad(B_Q) be the quotient map; dim V=ρ, and B_Q descends to a nondegenerate symmetric form B on V. The quotient is surjective. Since a totally isotropic subspace for a nondegenerate symmetric form over C has dimension at most floor(ρ/2), the image of every coordinate row-space or column-space under L has dimension at most1 (and is zero if ρ=1).

Write v_ij=L(E_ij). A nonzero v_ij spans both its row-image and its column-image, so its line is isotropic. If two nonzero vectors v_ij and v_kl spanned distinct lines, they could share neither row nor column. The crossed vector v_il would belong to the intersection of the row-image spanned by v_ij and the column-image spanned by v_kl, hence would be zero. The same holds for v_kj. Property2 would give

 B(v_ij,v_kl)=±B(v_il,v_kj)=0.

But two distinct isotropic lines that are mutually orthogonal span a two-dimensional totally isotropic subspace, impossible when ρ≤3. Therefore all nonzero v_ij lie on one isotropic line. Since the E_ij span E and L is surjective, V itself would be this isotropic line. A nonzero one-dimensional quadratic space cannot be both nondegenerate and isotropic. This is a contradiction. Thus rank B_Q≥4.

A single 2×2 minor or permanent has polarized matrix consisting of two nonzero 2×2 off-diagonal blocks on its four variables, so its rank is exactly4. This proves equality for both spaces. ∎

The argument is stated over C. It does not assert an identical characteristic2 statement, where quadratic and polarized bilinear forms require separate treatment.

## Conditional adoption consequence using GI-02

For the symmetric coefficient tensor S_F of det_n or per_n, the flattening that contracts n−2 of its n factors has image U_− or U_+, up to the standard nonzero polarization scalars. Its dimension is q=binom(n,2)², by the complementary-minor/permanent calculation in G-07. In the remaining two factors, ordinary CP border rank is matrix rank. Thus, provided QI-01 and the image substitution lemma GI-02 are adopted, one obtains

 Rbar_CP(S_det_n), Rbar_CP(S_per_n) ≥ binom(n,2)²+3.

The same inequality follows for Waring border rank because ordinary CP border rank does not exceed it. At n=4 the value is39; at n=5 it is103. At larger n a central ordinary catalecticant can already exceed this particular bound, so it should be combined with the other valid bounds rather than presented as uniformly strongest.

This may be an established special case of border-substitution/partial-derivative methods. The proof's correctness and its relationship to the existing literature are separate questions. No claim of a new published-record improvement is made here.

