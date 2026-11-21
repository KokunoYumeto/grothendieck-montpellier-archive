# Independent whole-proof review: G-17

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T03:01:03Z.

Scope: complete reading and independent rederivation of `g17_fragment.tex`, with the previously reviewed G-05, G-10, G-11, G-13, G-14, G-15, and G-16 as dependencies. No numerical computation or repeated source retrieval was necessary. This is an independent agent proof review, not a formal certification or external peer review.

## Verdict: PASS

Under the stated strict dimension hypothesis, the criterion for a successful stretch is exactly the conjunction `nu_4>0` and `nu_1>(n-m)s`. Both directions are established, including the equality boundary. The proof yields an explicit progression and correctly avoids asserting success at every sufficiently large integer stretch.

## 1. The auxiliary flag ring and the selected label

The displayed product of initial dual wedges has weight `-eta`. With the chosen Borel convention it is an extremal, equivalently opposite-highest, vector. Its weight is the sum of the individual wedge weights, and the corresponding extreme weight line in the tensor product is one dimensional. It therefore belongs to the single Cartan component `S_eta V*`. Its projective orbit is the partial flag variety determined by the positive adjacent differences of `eta`; the stabilizer's equal-part blocks give exactly the pair count `r_eta` for its dimension.

For each `d`, the pure tensor of this extremal vector has the unique extreme weight `-d eta`. The group span is the irreducible Cartan component `S_(d eta)V*`. The dual of the affine cone's degree-`d` coordinate space is exactly this group span: its annihilator consists of the degree-`d` polynomials vanishing on every group translate and scalar multiple. Thus the coordinate space is precisely `S_(d eta)V`, without an assumed projective-normality theorem. When `eta=0`, the cone is a line and every graded piece is one dimensional, as stated.

The first factor of the enhancement is the `s`th Veronese of the original standard-graded coordinate ring. Such a Veronese is generated in its new degree one by splitting any degree-`sd` monomial into `d` blocks of degree `s`. The auxiliary cone coordinate ring is also generated in degree one. Products of paired coordinates consequently span exactly `C[Y]_(sd) tensor S_(d eta)V`; the image definition supplies the kernel. This proves the exact ring identity without normality assumptions.

The dual-sensitive extraction is correct: the invariant space in `S_lambda V* tensor S_(d eta)V` is `Hom_SL4(S_lambda V,S_(d eta)V)`. It is one dimensional exactly when `lambda=d eta+t(1,1,1,1)`. Because `eta_4=0`, any polynomial partition in this relation has `t>=0`. Its size forces `t=nu_4 d`, so the unique label is `d nu`, in original coordinate degree `sd`. No additional labels or degrees are being summed.

## 2. Stability in every strict direction

The four stated probabilities are positive precisely under the two inequalities in the theorem, and their sum is one by `|nu|=ns` and `a=n-m`. The normalized padded monomials are orthonormal for the tensor-induced metric. Their weighted mean is `a e_0+m sum(theta_i e_i)=nu/s`. The moment of the pure `s`th tensor is therefore `nu`, and that of the normalized auxiliary weight vector is `-eta`. Their total is `nu_4(1,1,1,1)`, whose traceless part vanishes.

Off-diagonal matrix elements vanish on the Fermat combination because its monomial weights differ by `m` times a root rather than by a root, and on the auxiliary factor because it is a single weight vector. All four Fermat coefficients remain nonzero. Therefore the projective stabilizer calculation from G-16 applies unchanged. Stabilizing the line of the `s`th pure tensor implies stabilizing the original line by cancellation in the symmetric algebra in characteristic zero. Stabilizing the final decomposable tensor likewise implies stabilizing that first line. The projective stabilizer is finite.

The chosen form belongs to both cones by the same binary-product cyclic pencil construction as G-16. Kempf–Ness gives nonempty open stable loci. Subtracting the orbit dimension 15 from the enhanced cone dimensions yields exactly `u=2n^2+r_eta-13` and the strictly larger padded quotient dimension. The case `eta=0` is included; its stability inequalities specialize to the already proved strict rectangular range.

## 3. Action degree, parameter degree, and effectiveness

The ambient dimension is the dimension of `Sym^s(Sym^n V)` times the Weyl dimension of `S_eta V`, exactly the displayed `b`. The action on the first factor has polynomial degree `ns`; the dual action on the Schur factor uses cubic adjugate entries and has degree at most `3e`. Thus Derksen's action coefficient degree is `L=ns+3e`. The representation kernel is contained in the already proved finite projective stabilizer of the exhibited tensor, so the finite-kernel hypothesis is satisfied.

The smaller parameter degree is separately justified. The independent matrix in `End(V*)` acts polynomially on `S_eta V*` with degree `e`. Its invertible locus gives the GL orbit of the extremal vector. For `e>0`, central scalar matrices supply every nonzero scalar multiple over the complex numbers, so this orbit is dense in the affine flag cone. The determinant-pencil variables and this matrix are independent; their combined map has homogeneous degree `ns+e`, with no adjugate or inverse constraint. For `e=0`, the auxiliary vector is constant, and scaling the first cone supplies the missing scalar because complex `s`th roots exist. Thus the stated dense parameter map and `p=ns+e` hold in both cases.

The filtered Hilbert comparison is exactly the previously reviewed G-13/G-16 argument with these new parameters. Its degree bound is `(p beta)^u`, its algebraically independent generator lower bound uses `u+1` generators, and the chosen integer `h` makes the exact binomial comparison strictly larger than the required degree factor. Degree zero agrees, so some positive enhancement degree, hence some positive stretch, has a strict gap. The extraction formula converts it to the single label `j nu`.

The common explicit Veronese scale follows from the same generator-grouping argument. The determinant quotient has projective dimension `u-1`, which is positive in the stated range, and parameter degree `pE`. Chardin's bound and linear Noether normalization give the two displayed individual Hilbert bounds. The ratio of the lower to upper bounds exceeds one at and above `u(Q-1)+1`. Hence all sufficiently large multiples of `E`, rather than all integers, are proved successful. The ordinary four-row highest-weight restriction transfers the exact multiplicities to the full ambient orbit closures.

## 4. Necessity and boundaries

If the fourth part vanishes, every stretch has at most three rows, and the already proved ternary determinant saturation gives the full ambient multiplicity on the determinant side. If `nu_1<=as`, every stretched first part is at most its padding weight `a(sj)`, and G-14 gives the opposite weak multiplicity inequality. These arguments include equality and establish actual nonexistence, rather than merely failure of the chosen stable-point construction.

For a rectangular direction, the strict first-row inequality becomes `n<4m/3`, recovering G-11/G-12. The G-16 direction satisfies it for every positive padding amount. G-15's finite exclusion `j(nu_1-as)<=3` is compatible with, and does not contradict, the eventual progression in the strict interior.

No revisions are requested.
