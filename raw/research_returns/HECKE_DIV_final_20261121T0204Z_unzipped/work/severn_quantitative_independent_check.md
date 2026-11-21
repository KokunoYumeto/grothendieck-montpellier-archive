# R29. Independent audit of the explicit Severn supplier bound

Run HECKE_DIV_20261121. Check date: 2026-11-21. Checker: `/root/reductions`, GPT-6 Astra Pro; effort setting not exposed. This is an independent reconstruction followed by a complete reading of SQ1–SQ9 in `work/severn_quantitative.md`, including the corrected globally generated 2Θ generators and the resulting factor 40G. It is not a proof-assistant verification.

## Conclusion and dependence on earlier audits

The quantitative extraction passes. With the notation of SQ1,

`G=39,191,040`, `g=4G+1`, `R=(2G+1)G!G^G`, `L=2gR`,

`S0=G^(2g)(g!)²`, `SB=(L/2)!S0^R`, `k=L/2+4`,

`B0=(40G)^k binom(k,4) SB·8!·G^8`,

and, for the target polarization product Δ,

`N=4G^8Δ`, `D=N^8B0`,

the construction gives effective integral four-cycles of degree at most D whose rational Weil projections span the Weil plane on the nonempty analytic period image supplied by the dominance theorem. In particular at least one has nonzero projection. All displayed expressions are finite integers.

This conclusion uses the separately audited inputs that the displayed finite group and Hurwitz family have the asserted representation and dominant split unitary period map, and that the Schoen supplier nonvanishing survives the repaired exceptional-divisor argument. I did not repeat the whole finite-group computation, boundary degeneration, or exceptional-divisor proof in this check. I read the relevant exact certificate output and the original Schoen and Milne source passages, and independently checked every new numerical and linear-algebra step below. These dependencies should remain distinct in the final ledger.

## R29.1. Polarization exponent and integral K-action

Let Λ be the unimodular symplectic lattice of the covering Jacobian and e the Rosati-symmetric primitive projector. The rational central projector onto the pair σ,σbar is

`ε=(6/G) Σ_g Tr_(K/Q)(χ(g^−1))g`.

Each trace is integral: it is rational and an algebraic integer. For an involutive reflection s, `e=ε(1−s)/2`, so `Ge` is integral in the group ring. The explicit K-model of σ makes the simple algebra `M6(K)` and the rank-one reflection projector primitive. The use of a symmetric projector is essential here.

Put `Λ_A=Λ∩eΛ_Q`. This is a primitive Z-sublattice. Its polarization-dual lattice is exactly `eΛ`: an integral functional on Λ_A extends to Λ, unimodularity represents it by pairing with some λ in Λ, and orthogonality of e represents its restriction by eλ. Nondegeneracy on eΛ_Q proves equality. Therefore

`GΛ_A^#=GeΛ⊂Λ_A`.

Every polarization elementary divisor d_i divides G. Consequently the polarization product `Δ_A=∏_(i=1)^8 d_i` divides `G^8` and `∫θ_A^8=8!Δ_A≤8!G^8`.

Source O-stability is also needed, not merely target O-stability. The exact certificate `work/severn_group.json` records that all six scalar units, in particular ω, belong to the generated group on its faithful spanning orbit. The corresponding scalar is central, hence commutes with e and preserves A. Its integral homological action satisfies `ω²+ω+1=0`, so Λ_A is stable under `O=Z[ω]`. I read this certificate and its membership-test code; I did not count that reading as a fresh run of the computation.

## R29.2. Supplier identity with bounded integer coefficients

The real linear characters of orders one and two contribute zero determinant columns. For a nonreal pair τ,τbar, restriction multiplicities against a real character agree, so their difference is zero. If τ is quaternionic, its invariant alternating form restricts nondegenerately to the isotypic space of a real one-dimensional character: all other isotypic spaces are orthogonal to it. Its dimension is therefore even, and the orthogonal multiplicity-space determinant coordinate vanishes modulo two. Orthogonal τ has a symplectic centralizer and supplies no character coordinate. Thus discarding these Brauer terms is legitimate.

A character with primitive eigenspace dimension h=0 also contributes zero: its dimension is a sum of nonnegative multiplicities weighted by the dimensions of the multiplicity spaces occurring in H¹(C). Every relevant restriction multiplicity must then be zero.

For a remaining character, m≥3. Rationality of H¹ makes all primitive cyclic characters have the same multiplicity h, so `φ(m)h≤2g(C')`. Since φ(m)≥2,

`h≤g(C')≤g`.

All inertia groups in the original cover have order two. Their cyclic images are trivial or the unique order-two element. The nonzero local cyclic exponents are therefore m/2, and their number is even by the global relation. They pair with their negatives. The formula `h=2g(X)−2+s` then makes h even. Retained suppliers have h≥2 and satisfy the required simple-branch condition.

I checked the integer coefficient bound independently. Add `2e_j` columns to replace the torsion coordinates by integer rows. The resulting matrix has rank r≤G and entries bounded by M=G. Select r independent rows and columns to obtain B with `d=|det B|≤r!M^r`. In the finite quotient `Z^r/BZ^r`, the class of the target vector can be reached by at most d−1 signed generator steps: a shortest path has no repeated vertex. Subtracting these columns leaves v in BZ^r with `|v|∞≤dM`. Cramer's rule gives each coordinate of `B^−1v` at most `r!M^r` in absolute value. Including the d−1 selected steps bounds the total coefficient sum by `(r+1)r!M^r`, which is at most R. Projection to the chosen independent rows is injective on the rational column span, so the solution on those rows solves the original system. Dropping the auxiliary torsion columns cannot increase the supplier coefficient sum.

## R29.3. The Schoen degree bound S0

The original source was checked at printed pp.12–18: P0 is a linear projective subspace in an Abel–Jacobi fibre; its strict transforms are isomorphic to it; a chosen split component pushes to Q0 mapping with degree one to P0. The generic point-incidence divisor therefore restricts to O(1). The primitive nonvanishing after pushdown is an input from the supplier proof, including its stated repair.

Here is the independent degree calculation. Let `q:C'^h→W0` be the quotient by the kernel-of-sum deck subgroup extended by permutations. Its order is

`d0=m^(h−1)h!`.

Let H be the sum of degree-one point classes on the h curve factors. The pullback of the point-incidence divisor from `Sym^hX` is mH. For a component Z0 over Q0 with generic degree e0,

`m^(h/2) deg_H(Z0)=e0`, with `1≤e0≤d0`.

No factorial is missing: the point-incidence divisor is a hyperplane on P0, whose top degree is one. The factorial from the permutation quotient is already part of d0.

Use the integral orbit sum `R0=Σ_(a∈G0)a_*Z0`, retaining repetitions. Rational Poincaré duality for finite complex quotients gives

`[R0]=e0 q^*[Q0]`.

This identity does not require flatness of q. One can derive it from the cohomological isomorphism `H*(W0,Q)≅H*(C'^h,Q)^G0`, the degree identity `q_*q^*=d0`, and averaging. It gives `q^*q_* =Σa_*`, and ordinary proper pushforward gives `q_*[Z0]=e0[Q0]`. Thus all primitive components of R0 are nonzero.

All group actions preserve the numerical class H. Consequently

`mass_H(R0)=d0 e0/m^(h/2)≤d0²/m^(h/2)`.

The residual cyclic primitive projector multiplied by m has integer Ramanujan-sum coefficients, each bounded by φ(m). Applying it gives an integral signed cycle Y in the determinant subspace, nonzero on each primitive eigenline, with

`mass_H(Y)≤mφ(m)d0²/m^(h/2)≤m^(3h/2)(h!)²≤G^(2g)(g!)²=S0`.

The final inequality uses m≤G and h≤g; it deliberately leaves substantial slack. No degree of an exceptional divisor or resolution enters because the cycle has first been pushed down to Q0 and degree is measured by the incidence class.

## R29.4. Middle-degree transfer on curve powers

For a supplier identity `e_σ=Σn_i a_i`, take |n_i| copies of each supplier curve power and let B be their product. Its even dimension is `ℓ=Σ|n_i|h_i≤gR≤L`. The external product of the signed supplier cycles has dimension ℓ/2. The multinomial expansion of the product point polarization gives

`mass_(H_B)(Y_B)≤[(ℓ/2)!/∏((h_i/2)!)^|n_i|] ∏S0^|n_i|≤SB`.

Each supplier cycle has nonzero components in both selected conjugate determinant lines. Select the line with character `sign(n_i)a_i`; its dual determinant line has opposite character and pairs nontrivially with it. This is the exterior determinant pairing induced by the nondegenerate H¹ pairing, so both lines lie in the tensor product of the h_i first-cohomology factors. A vector in the dual line paired with the supplier cycle is nonzero. Taking the external product of these dual vectors and a target Weil eigenvector yields a U-invariant class Γ on B×A. Its action on Y_B is a nonzero multiple of that target eigenvector. Complex conjugation handles the other line. The correspondence has codimension `c=ℓ/2+4`.

This verifies the modification that keeps suppliers in middle cohomology on powers of curves. No inverse hard-Lefschetz cycle is required, and no unbounded correspondence degree is silently imported from such an inverse.

## R29.5. Explicit invariant divisors and the factor 40G

For each quotient curve, Abel–Jacobi followed by pullback to J(C) induces a surjection on first cohomology with a U-equivariant rational section, using the averaging idempotent and norm–pullback identity. The inclusion of A likewise has the U-equivariant section supplied by e. Consequently Γ lifts to a U-invariant class on `J(C)^(ℓ+1)`.

This is the full centralizer U of the group algebra in the symplectic group. Using only the connected orthogonal group would incorrectly introduce extra orientation tensors; using invariants of G itself would be the wrong group. Over C, U is a product of full orthogonal groups, symplectic groups, and paired general linear groups. Its exterior invariants are generated in degree two. I directly checked the exact primary statements of Milne's Lemma3.5, Proposition3.6 and Remark3.7, including the full orthogonal case. Applied to the semisimple algebra `End_D(V)` and its adjoint involution, the lemma and double centralizers give `End_U(V)=D`, the image of Q[G].

Invariant alternating forms on copies of V are therefore given by self-adjoint matrices over D. Such matrices are spanned by the diagonal identity, diagonal `g+g^−1`, and off-diagonal `g,g^−1` pairs. They are generated, over Q, by the divisor classes

`pr_i^*(2Θ)` and `(pr_i+g pr_j)^*(2Θ)`, including i=j.

Indeed the theorem of the square subtracts the individual polarization terms to isolate exactly those matrix entries. The factor 2 is necessary for the stated uniform global generation: 2Θ is globally generated, and arbitrary pullback preserves global generation. Coefficients in the linear combination need not be bounded because the conclusion uses the spanning collection of integral cycle classes, rather than the signed combination itself.

For `π:C→C'` of degree a, the canonical-polarization norm identity gives `(π^*)^*Θ_C≡aΘ_C'`. Thus the curve map η has theta degree `a g(C')`. Riemann–Hurwitz gives `a(g(C')−1)≤g−1=4G`, whence `deg η^*Θ_C≤5G` because a≤G. On `T=B×A`, the restricted product Jacobian polarization is at most `5G H0` in the nef order, where `H0=H_B+θ_A`.

Each displayed divisor is at most eight times that product polarization. For distinct factors, the parallelogram identity bounds the 2Θ pullback by four times the two-factor polarization. For i=j it gives

`(1+g)^*(2Θ)+(1−g)^*(2Θ)=8Θ`,

so the uniform bound eight is correct in every case. Therefore `D_j|_T≤40G H0`.

Global generation allows successive proper intersections with all finitely many effective terms of Y_B×A. If a section has no zero, that contribution is zero. The intersection cycles have integral nonnegative multiplicities. Nef comparison can be multiplied against their effective ambient cycles: expand the difference of products as a sum containing one nef difference in each term. Therefore each monomial action, after pushforward to A, has total degree mass at most

`(40G)^c ∫_(Y_B in mass × A) H0^c θ_A^4`

`=(40G)^c binom(c,4) mass_(H_B)(Y_B) ∫_A θ_A^8≤B0`.

The sole surviving term in the binomial expansion has H_B exponent ℓ/2 and theta exponent four before the outside theta-four factor. This proves the binomial coefficient exactly; the huge dimension of the containing Jacobian does not appear. Because the complex combination of these monomial actions gives each target eigenvector, their rational Weil projections span the plane. At least one individual effective integral constituent has nonzero projection and degree at most B0.

## R29.6. Integral Hermitian comparison

For an O-stable lattice define

`h(x,y)=E(x,ωy)−barω E(x,y)`.

Direct use of `ω²+ω+1=0` and Rosati conjugation proves that h is conjugate-linear in x, linear in y, and Hermitian. Its coefficients are integral in O, and the coefficient of ω is E(x,y). The identity Hermitian matrix gives the standard unimodular alternating lattice on `(v_i,ωv_i)`. A Hermitian matrix H changes the alternating determinant by `Norm(detH)=(detH)²`. Thus the absolute Hermitian determinant is exactly the polarization elementary-divisor product Δ. There is no extra factor of 3.

For a split rank-eight Hermitian space, a maximal isotropic K-subspace meets the lattice in a primitive rank-four O-module. Since O is a PID it extends to an O-basis `(v,w)`, with matrix

`[[0,B],[B*,D]]`, `Δ=Norm(detB)`.

Let `X=(B*)^−1D/2`. Then `w'=w−vX` is isotropic, because its self-pairing is `D−B*X−X*B=0`. With `u=w'B^−1`, the basis `(v,u)` is hyperbolic. Writing b=detB, the only denominators are b, 2bar b, and their product 2Norm(b)=2Δ. Explicitly, the isometry and inverse are

`μ(v)=e`, `μ(w)=fB+eX`,

`μ^−1(e)=v`, `μ^−1(f)=wB^−1−vXB^−1`.

Both are integral after multiplication by 2Δ. No bound on the sizes of the entries of B or D is required. Comparing source and target therefore has denominator dividing `4Δ_AΔ`; `N=4G^8Δ` clears it since `Δ_A|G^8`.

Transporting this rational comparison over a marked simply connected period neighbourhood and multiplying by N gives the stated K-linear isogeny. Since the rational comparison is an isometry, `φ^*θ_target=N²θ_source`. For a four-dimensional effective cycle, the projection formula gives the exact degree factor N⁸. Isogeny pushforward preserves nonzero Weil projection and spanning of the plane. The dominant period map therefore supplies the required nonempty analytic target open with the common bound D.

## R29.7. Projector and Gram conversion

SQ8's projector and its degree polynomial were independently checked earlier in R25/P1; this audit does not count that prior computation twice. The degree-mass estimate follows from `a^*θ=7θ` and the dimension-four pullback factor `7^(4j)`.

I checked SQ9's general conversion independently. Middle Weil classes are primitive because multiplication by a mixed theta class would exceed one K-eigenspace dimension. The Hodge star is +1 on primitive (4,4)-classes, so their integral intersection pairing is positive definite. The signed representatives of mass B give norm at most B under the explicitly stated degree-to-norm inequality. Two independent projected integral classes consequently have an integral positive Gram determinant d with `1≤d≤B^4`. If q_t clears the fixed class t and `T=(q_t t,q_t t)`, Cramer's rule gives

`d q_t t=n1 y1+n2 y2`, with `|n1|+|n2|≤4B^3 sqrt(T)`.

The multiplier is at most `q_t B^4`; the signed degree mass is at most `4B^4 sqrt(T)`. Since T is a positive integer, `C=B^4(q_t+4T+4)` bounds both. The already checked bounded-Chow closedness lemma then extends this bound from the analytic open to the irreducible fixed moduli component. This last step uses actual bounded integral cycles and finite multipliers, not pointwise rational algebraicity alone.

## Source and check log

- Schoen, C. (1988). *Hodge classes on self-products of a variety with an automorphism*. Compositio Mathematica,65,3–32. Original PDF: https://www.numdam.org/item/CM_1988__65_1_3_0.pdf. In this turn I read Theorem2.0 and the projective-space, strict-transform, and quotient-duality passages at printed pp.11–18; exact web references `turn970694548view0`, `turn592396862view0`. The new orbit-sum and degree estimates above are independent derivations. The exceptional-divisor repair is separately audited, not newly reproved here.
- Milne, J.S. (1999). *Lefschetz classes on abelian varieties*. Duke Mathematical Journal,96,639–675. Author PDF: https://jmilne.org/math/articles/1999aP.pdf. Lemma3.5 is on preprint pp.15–16, Proposition3.6 on p.17, and Remark3.7 on p.18. Their statements and proofs were read directly; references `turn822257618view0`, `turn731151528view0`, `turn731151528view1`, `turn731151528view2`.
- `work/severn_quantitative.md`: whole SQ1–SQ9 proof read, and the new estimates independently reconstructed as recorded above.
- `work/severn_group.json` and the relevant scalar-membership code in `work/severn_group.py`: read; no new execution was counted. The full finite-group and dominance audits belong to their earlier separate check records.
- Check result: passed with the explicitly stated inputs and hypotheses. The factor 40G, source O-stability, full (possibly disconnected) centralizer, quotient cohomological transfer, and codimension/dimension conventions must be retained in the final formulation.
