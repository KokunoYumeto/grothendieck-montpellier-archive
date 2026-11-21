---
title: 'GCT_PLETH: Plethysm, theta correspondence, and Grothendieck operations'
subtitle: 'Checked proofs, explicit positive formulas, and a continuing research ledger'
author: 'GPT-6 Astra Pro — GCT_PLETH_20261121_run01'
date: '21 November 2026 — working checkpoint'
---

# State of this research record

This is a continuing research record for the supplied prompt. The checked findings below are stated with their exact scope. The final part separates the remaining mathematical and input gates. A checkpoint is a dated snapshot of active work; it is not a declaration that the open questions have been settled.

The main constructive result is a terminating positive lattice-point procedure for every symmetric plethysm coefficient (G-009), every Schur plethysm coefficient (G-010), and every image multiplicity of the specified Hadamard--Howe map (G-011). It constructs the finite data from flag minors, balanced torus invariants, finite-group averages, and elimination. The proof gives an explicit invariant algebra or coherent module and a bijection from its standard monomials to a finite disjoint union of bounded polytope lattice sets. No previously computed plethysm coefficient is used as an oracle.

The construction contains large preprocessing steps: a Hilbert basis, a finite-group degree bound, and a Gröbner basis. Their size has no polynomial bound in the varying parameters in this work. Mulmuley's GCT VII, Problem 1.1, asks for a positive formula in the complexity class #P; the missing polynomial description and verification bounds are recorded explicitly. The construction proved here gives finite positive formulas in the literal lattice-count sense and leaves that complexity requirement open.

Several formulas avoid the general elimination step. G-012 gives four fixed polytopes for every symmetric outer-degree-three coefficient. T-037 now gives a complete positive formula for every outer-degree-four Schur label and every output partition, using at most 108 fixed polytopes with at most five variables. Its proof evaluates the entire four-point ideal model, including unequal opposite gaps, and its evaluator uses a fixed number of integer arithmetic operations. T-012–T-013 give finite explicit Littlewood–Richardson polytopes through stable width six, and T-018 evaluates an entire width-seven sector.

T-032 and G-015 construct an exact projective-frame ideal model in every outer degree, with an explicit balanced-chart inverse and proof of every transverse order. In outer degree five, T-038 and A-029 supply the actual equivariant quadratic resolution, cubic algebra, Rees presentation and linear powers. G-017 evaluates the quotient-bundle module at every point order by an explicit matrix factorization and an equivariant free multiplication map. G-020 evaluates every symmetric quotient power at every nonnegative extra twist, with 36 active positive terms and 115 exact support exceptions. G-021 evaluates every two-row quotient throughout c≥2k. Its 122 active polytopes use at most eleven variables; all positive-order Newton constants are proved strictly positive by a small exact coefficientwise domination certificate. Independent calculations reconstruct every margin polynomial, all 90,720,000 initial residue coefficients, and 882 genuine low-degree plethysms. The complete support has 155 exceptional parameter-label quadruples. The actual balanced multiplication and exterior complement pairing carry this result to every output with λ2+λ3≤2n or λ3+λ4≥2n. The remaining direct outer-five gate is the strict region between these inequalities. G-018–G-019 and T-039–T-043 retain smaller specialized formulas and independently checked comparisons.

For the actual canonical map, G-013 transports prime-adjacent square preimages through an explicit block specialization and multiplies them, with exact numerical semigroup certificates for ranks 2 through 100. G-014 supplies explicit preimages for every target highest-weight component whose tail has size at most the coordinate degree. R-017–R-020 prove second-row injectivity and settle the entire first-row boundary band of common polarization. R-021 supplies determinant preimages at every even-rank quadratic boundary. R-022–R-023 transfer these through an actual annihilator injection and exact rectangular prolongation. R-024 proves recursive componentwise surjectivity from the established degree-five base and the square-bound bases, including positive exact image ranks below the full-map range. R-025 gives two infinite explicit critical-boundary image families, and R-026 gives an explicit multiplicity-one image component at every b=r²−k, 2≤k≤r−1, for r=a−1≥3. Its endpoint proof evaluates the integral cofactor vector through a fully specified apolar pairing. The remaining critical annihilator has the smaller first- and second-row support stated in R-023, with these further components now removed by their actual nonzero images.

The archive audit now inventories 123 individual assertions: 80 proved, 25 refuted, and 18 exact gates. All thirteen supplied target leaves have been compared with the original Montpellier scans. A-021 proves the exact lattice-ring statement over every characteristic-zero discrete valuation ring. A-023 gives an explicit characteristic-zero local-ring counterexample even with base K0 equal to the integers. A-022 proves the hyperbolic characteristic-class formula over every scheme with 2 invertible using an actual injective splitting construction. The remaining historical and mathematical inputs are retained assertion by assertion.

## Conventions and checking

All representation multiplicities are in characteristic zero unless an integral or modular ring is explicitly specified. The notation \(a_{m,n}^{\lambda}\) means the multiplicity in \(\operatorname{Sym}^m(\operatorname{Sym}^n V)\). The canonical map uses normalized tensor averaging, and each integral comparison distinguishes symmetric and divided powers by its actual map.

An identifier labels a finding or explicit reformulation produced in this run; it does not claim historical priority for the underlying coefficient family. Known results are attributed with exact locators. Proof readings, independent re-proofs, finite computations, and background uses are separate events in `CHECK_EVENTS.tsv`. The model is GPT-6 Astra Pro; the runtime does not expose the reasoning-effort setting, so it is recorded as unexposed. No Lean proof was executed, and none of the prompt's named Lean source files was present in the supplied ZIP.

The package includes executable exact-arithmetic computations, complete finite tables, proof-review reports, a question register, and the timed ledger. The manuscript is assembled from the current proof reports; the source register records the original literature and Grothendieck locators. The entire checked mathematical argument is contained in the present TeX source, with its finite certificates also available as machine-readable files.


\part{Checked theta and positive formulas}


# Theta, balanced weights, and the finite projection

Run: `GCT_PLETH-20261121-theta`. Author/checker: GPT-6 Astra Pro, effort not exposed by the runtime. Mathematical statements below are unconditional statements over characteristic zero. They are exact realizations and explicit consequences of established duality, with no claim of historical novelty.

## Notation

Let `V=C^r`, let `m,n>=1`, and let `lambda` be a partition of `mn`. Set

\[
a_{m,n}^{\lambda}=\dim\operatorname{Hom}_{GL(V)}
(S_\lambda V,\operatorname{Sym}^m(\operatorname{Sym}^n V))
\]

in the stable range `r>=length(lambda)`. More generally, `p_{mu,nu}^lambda` is the coefficient of `s_lambda` in `s_mu[s_nu]`. Specht modules are written `[mu]`.

## T-001. The actual compact dual pair and its vacuum character

Equip `V=C^r` and `E=C^m` with positive definite Hermitian forms. Put `W=V tensor E`, considered as a real vector space, with symplectic form `omega=Im h_W`. The images of `U(V)` and `U(E)` in `Sp(W_R)` are mutual centralizers.

**Proof.** A real-linear map commuting with `U(V)` commutes with scalar multiplication by `i`, hence is complex-linear. The complex commutant of the natural `U(V)` action on `V tensor E` is `1_V tensor End_C(E)`: this follows either by the matrix units generated by the natural representation or by Schur's lemma on the irreducible natural `U(V)` module. A complex-linear map preserving `omega` preserves `h_W`, because its real part is recovered from `omega` and the complex structure. Thus the symplectic centralizer is exactly `1_V tensor U(E)`. Interchanging the two factors proves the reverse centralizer identity. This proof also covers `r=1` or `m=1`.

Choose the positive-energy oscillator convention in which the polynomial Fock module on a Hermitian space `W` is

\[
\mathcal F_{\mathrm{alg}}(W)=\operatorname{Sym}(W)\otimes\chi_0,
\qquad \chi_0^2=\det_W
\]

on the metaplectic preimage of `U(W)`. Explicitly this preimage is the double cover of `U(W)` with elements `(u,zeta)` satisfying `zeta^2=det(u)`, and the action on the homogeneous polynomial summand is `zeta Sym^d(u)`. Its infinitesimal action is `d Sym(A)+(tr_W A)/2`; on a diagonal rotation in the `j`th coordinate the eigenvalue is `k_j+1/2`, the usual number-operator realization of the oscillator. This specifies the convention and the character completely. The contragredient convention dualizes the polynomial space and inverts the displayed character.

For the homomorphism `U(V) x U(E) -> U(W)` the vacuum character has square

\[
(\det_V)^m(\det_E)^r.
\]

Consequently twisting the restricted oscillator by `chi_0^{-1}` gives exactly the polynomial Cauchy module. The twist is part of the dictionary; it is not discarded silently. On permutation matrices in `U(E)`, its square is `sgn^r`.

## T-002. Balanced-weight Howe realization

Let

\[
M_{\lambda,n}=(S_\lambda E)_{(n,\ldots,n)}.
\]

Here `S_m` acts by literal permutation matrices on `E`, not by an unspecified choice of representatives in `SU(m)`. There is an isomorphism of `GL(V) x S_m` modules

\[
(\operatorname{Sym}^n V)^{\otimes m}
\simeq \bigoplus_{\lambda\vdash mn} S_\lambda V\otimes M_{\lambda,n}.
\tag{T2.1}
\]

In particular,

\[
\boxed{a_{m,n}^{\lambda}=\dim M_{\lambda,n}^{S_m}}.
\tag{T2.2}
\]

**Proof of the precise realization.** Polynomial Howe/Cauchy duality is

\[
\operatorname{Sym}(V\otimes E)
\simeq\bigoplus_\lambda S_\lambda V\otimes S_\lambda E.
\]

Take the weight `(n,...,n)` for the diagonal torus acting on `E`. On the left, a polynomial has degree `n` in each of the `m` column spaces `V tensor e_i`; this weight space is `(Sym^n V)^{tensor m}`. A permutation matrix permutes those column spaces and gives exactly the ordinary tensor-factor action. The right side gives (T2.1). Taking `S_m` invariants gives (T2.2), because characteristic-zero symmetrization identifies invariant tensors with `Sym^m(Sym^n V)`.

The exact literature locator in the supplied source is Landsberg, *Geometric Complexity Theory: an introduction for geometers*, subsection “A duality theorem for weight zero spaces and plethysms,” theorem `gaythm`, lines 766–798; it attributes the statement to Gay (1976). The displayed corollary `gaycor` (ii) writes `S_d` where this construction requires the permutation group on `dim(E)=m` letters. The proof above fixes the group and the action rather than relying on that typographical line.

## T-003. General Schur plethysm, both oscillator and wreath-product versions

For `mu` a partition of `m`, the balanced-weight identity refines to

\[
\boxed{p_{\mu,(n)}^\lambda
=\dim\operatorname{Hom}_{S_m}([\mu],M_{\lambda,n}).}
\tag{T3.1}
\]

Indeed, Schur–Weyl duality on `(Sym^n V)^{tensor m}` gives
`sum_mu S_mu(Sym^n V) tensor [mu]`; comparing it with (T2.1) proves the formula.

For arbitrary `nu` of size `n`, write `W_nu=S_nu V`. Its invariant Hermitian form gives a homomorphism `rho_nu:U(V)->U(W_nu)`. The compact dual pair `U(W_nu),U(E)` on the polynomial Fock space `Sym(W_nu tensor E)` has Howe component

\[
\operatorname{Hom}_{U(E)}(S_\mu E,
\operatorname{Sym}(W_\nu\otimes E))=S_\mu(W_\nu).
\tag{T3.2}
\]

Here `dim E=m` suffices, and the vacuum twist is handled as in T-001. Restrict the first member along `rho_nu`; then the multiplicity of `S_lambda V` in (T3.2) is precisely `p_{mu,nu}^lambda`. This is an actual compact-oscillator realization. The restriction along the explicitly specified polynomial representation `rho_nu` is the remaining branching computation.

For a finite description, identify the `mn` tensor positions with an `m` by `n` grid and put `H=S_n wr S_m`. Let

\[
U_{\mu,\nu}=[\nu]^{\otimes m}\otimes\operatorname{Inf}_{S_m}^H[\mu],
\]

where block permutations permute the tensor factors in `[nu]^{tensor m}`. There is a natural isomorphism

\[
S_\mu(S_\nu V)\simeq
\operatorname{Hom}_{H}(U_{\mu,\nu},V^{\otimes mn}),
\qquad
p_{\mu,\nu}^\lambda=
\dim\operatorname{Hom}_H(U_{\mu,\nu},[\lambda]|_H).
\tag{T3.3}
\]

**Proof.** Apply `S_n`-Schur–Weyl duality separately to the `m` blocks. Taking `Hom_{S_n^m}([nu]^{tensor m},-)` gives `(S_nu V)^{tensor m}` and preserves the block-permutation action. Taking `Hom_{S_m}([mu],-)` gives `S_mu(S_nu V)`. This nested Hom space is precisely the Hom space for the semidirect product `H`. Full Schur–Weyl duality for `V^{tensor mn}` then gives the second equality. Every map used is functorial in `V`.

## T-004. The exact positive polytope count produced by interlacing

For `length(lambda)<=m`, pad `lambda` by zeros to length `m`; for greater length the balanced space and symmetric plethysm coefficient vanish. Define `GT(lambda;n^m)` by integer arrays `x_i^(k)`, `1<=i<=k<=m`, with

\[
x_i^{(m)}=\lambda_i,\qquad
x_i^{(k+1)}\ge x_i^{(k)}\ge x_{i+1}^{(k+1)},\qquad
\sum_{i=1}^k x_i^{(k)}=kn\quad(1\le k\le m).
\tag{T4.1}
\]

The inequalities define a bounded rational polytope. The usual `U(m)` to `U(m-1)` interlacing rule, iterated, gives

\[
\#(GT(\lambda;n^m)\cap\mathbb Z^{m(m+1)/2})
=\dim M_{\lambda,n}
=K_{\lambda,(n^m)}
=\boxed{\sum_{\mu\vdash m}(\dim[\mu])p_{\mu,(n)}^\lambda}.
\tag{T4.2}
\]

**Proof of the specified specialization.** Iterated branching associates a one-dimensional torus weight line to every interlacing pattern. Its `k`th torus weight is `sum_i x_i^(k)-sum_i x_i^(k-1)`. The row-sum equations in (T4.1) say exactly that every such weight equals `n`, so they select a basis of `M_{lambda,n}`. Decomposition of this `S_m` module into Specht modules, with multiplicities supplied by (T3.1), yields the final equality. The standard interlacing theorem itself is carried as background; this is its explicit balanced-weight specialization.

Thus the interlacing count controls the displayed positive weighted sum of outer Schur plethysms. The desired symmetric outer power is the summand indexed by `mu=(m)`, and T-002 identifies its projector exactly.

## T-005. Determinant twist, parity obstruction, and transport

On the determinant-normalized representation

\[
\widetilde M=S_\lambda E\otimes(\det E)^{-n},
\]

the balanced weight becomes torus weight zero. Its permutation action on that zero-weight space is

\[
\widetilde M_0\simeq M_{\lambda,n}\otimes\operatorname{sgn}^{n}.
\tag{T5.1}
\]

Consequently

\[
a_{m,n}^\lambda
=\dim\operatorname{Hom}_{S_m}(\operatorname{sgn}^{n},\widetilde M_0).
\tag{T5.2}
\]

The determinant of a permutation matrix is its sign, which proves (T5.1); tensoring by a one-dimensional character proves (T5.2). This supplies the exact morphism for normalization, including its finite character.

For `m>=2` and `lambda=(n^m)`, `S_lambda E=(det E)^n`. Its balanced weight space has dimension one and the permutation action is `sgn^n`. Hence

\[
\boxed{a_{m,n}^{(n^m)}=\begin{cases}1&n\text{ even},\\0&n\text{ odd}.\end{cases}}
\tag{T5.3}
\]

There is exactly one interlacing pattern in (T4.1), since each row is forced to consist of `n`s. For odd `n`, the polytope count is one and the desired coefficient is zero. This refutes the specific proposal of using those unprojected interlacing counts for the symmetric plethysm coefficient. It makes no claim about all possible positive formulas. The same pattern contributes to outer Schur type `(1^m)` in (T4.2).

More generally, for `t>=0`, functorial determinant twisting gives

\[
S_{\lambda+(t^m)}E\simeq S_\lambda E\otimes(\det E)^t.
\]

It follows that

\[
p_{\mu,(n+t)}^{\lambda+(t^m)}
=\begin{cases}
p_{\mu,(n)}^\lambda&t\text{ even},\\
p_{\mu',(n)}^\lambda&t\text{ odd},
\end{cases}
\tag{T5.4}
\]

where `mu'` is the conjugate partition. In particular,

\[
\boxed{a_{m,n+2t}^{\lambda+(2t)^m}=a_{m,n}^{\lambda}}.
\tag{T5.5}
\]

**Proof.** The balanced weight shifts from `(n^m)` to `((n+t)^m)`; its `S_m` representation tensors with `sgn^t`. The identity `[mu] tensor sgn=[mu']` and T-003 give (T5.4). Equation (T5.5) is its even case. This is an exact transport of every nonvanishing, and of every vanishing, on these rays.

The rectangular parity statement already occurs in the supplied Landsberg source, exercise `snssv` immediately after theorem `gaythm`, with attribution to Howe, Proposition 4.3(a). T5.1–T5.5 record the explicit character dictionary needed here; no novelty claim is made for determinant-shift identities.

## T-006. A complete positive formula for outer degree two

For `n>=1`,

\[
\boxed{\operatorname{Sym}^2(\operatorname{Sym}^n V)
=\bigoplus_{j=0}^{\lfloor n/2\rfloor}S_{(2n-2j,2j)}V.}
\tag{T6.1}
\]

The equality is understood in characteristic zero; summands of excessive length vanish. Its coefficient is the lattice count

\[
a_{2,n}^\lambda
=\#\{j\in\mathbb Z:0\le j\le n/2,
\lambda=(2n-2j,2j)\}.
\tag{T6.2}
\]

**Short proof in the balanced-weight form.** Partitions of `2n` occurring in T-002 have length at most two, so write `lambda=(2n-k,k)`, `0<=k<=n`. For `E=C^2`,

\[
S_{(2n-k,k)}E=\operatorname{Sym}^{2n-2k}E\otimes(\det E)^k.
\]

Its balanced weight line is spanned by `e_1^{n-k}e_2^{n-k}` tensored with the determinant factor. The transposition fixes the monomial and multiplies the determinant factor by `(-1)^k`. T-002 retains exactly even `k=2j`, each with multiplicity one. This provides a positive formula after evaluating the finite projector, rather than dropping it. The underlying decomposition is classical; this proof is included only to exhibit the exact Howe-to-polytope dictionary.

For the smallest sign obstruction, `Sym^2(Sym^3 V)=S_(6)V+S_(4,2)V`, whereas the GT count for `(3,3)` equals one.

## T-007. Inner degree two: established multiplicity-free positive formula

The classical symmetric-matrix identity is

\[
\operatorname{Sym}^m(\operatorname{Sym}^2 V)
=\bigoplus_{\alpha\vdash m}S_{2\alpha}V.
\tag{T7.1}
\]

An exact locator is Weyman, *Cohomology of Vector Bundles and Syzygies*, Proposition 2.3.8; Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, Chapter I, §8, Example 6. It is independently quoted with these locators in Fischer–Ikenmeyer, *The computational complexity of plethysm coefficients*, footnote 4 immediately before Theorem 3.5, https://pure.mpg.de/rest/items/item_3265369_1/component/file_3265370/content?download=true . The original books were not opened in this subtask, so the check event records the exact extent of verification.

Thus `a_(m,2)^lambda` is the number of integer points `alpha` satisfying `2alpha=lambda`, `alpha_1>=...>=alpha_r>=0`, `sum alpha_i=m`: zero or one. Combined with T-006 this proves the Foulkes coefficient inequality for the pair of outer degrees `2,m`: every constituent of `Sym^2(Sym^m V)` occurs once in `Sym^m(Sym^2 V)`. This is a coefficient statement; the actual Hadamard–Howe rank is handled by the grid projector supplied separately to the root agent.

## T-008. Explicit additive support semigroups

For fixed `m`, define

\[
\Gamma_m=\{(n,\lambda):|\lambda|=mn,\ell(\lambda)\le m,
a_{m,n}^\lambda>0\}.
\]

This set is closed under addition `(n,lambda)+(n',lambda')=(n+n',lambda+lambda')`.

**Proof in a domain, with all group actions specified.** Let `E=F=C^m`, let `U_F` be a maximal upper unipotent subgroup, and consider

\[
R=\operatorname{Sym}(E\otimes F)^{U_F}.
\]

It is a subring of a polynomial ring, hence a domain. Cauchy duality gives `R=sum_lambda S_lambda E tensor L_lambda`, where `L_lambda` is the one-dimensional highest-weight line of `S_lambda F`. Multiplication respects the right-torus weight, sending the `lambda` and `lambda'` summands to `lambda+lambda'`. It also respects the left diagonal-torus weights and the left permutation action. Nonzero vectors in `M_(lambda,n)^{S_m} tensor L_lambda` and `M_(lambda',n')^{S_m} tensor L_lambda'` have nonzero product, which has balanced weight `(n+n')^m`, right highest weight `lambda+lambda'`, and remains permutation invariant. T-002 gives the claimed additive support.

For fixed `n`, the analogous support set

\[
\Gamma^{n}=\{(m,\lambda):a_{m,n}^\lambda>0\}
\]

is also additive: use the domain `Sym(Sym^n V)` and the product of nonzero highest-weight vectors. The preceding proof specifies the less immediate fixed-outer-degree realization, which is useful for transporting nonvanishing in the direction of inner degree.

These semigroup properties construct further positive instances from positive seeds. T-005 gives their exact determinant translations. Neither calculation evaluates every finite `S_m` projector.

## T-009. A precise obstruction to homogeneous Ehrhart formulas

Kahle–Michałek, *Obstructions to combinatorial formulas for plethysm*, Electronic Journal of Combinatorics 25(1) (2018), P1.41, Theorem 5 and Remark 6, give

\[
a_{3,4s}^{(7s,5s)}=a_{4s,3}^{(7s,5s)}
=\phi(s)=\frac{s+r(s)}3,
\]

where `r(0),...,r(5)=(3,-1,1,0,2,-2)` periodically. This function is not the Ehrhart function of a rational polytope: `phi(1)=0` and `-phi(-1)=1` violate Ehrhart reciprocity. The theorem also excludes one-dimensional inhomogeneous polytopes. Its exact scope leaves higher-dimensional inhomogeneous constructions untreated. Source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf/ , printed page 4, Theorem 5 and Remark 6. No reproof of the known theorem is claimed. The attached computation checks the displayed values by independent partition counting for `1<=s<=40`.

## Exact projection and subsequent positive-count constructions

For symmetric plethysm the exact finite projection is

\[
\operatorname{rank}\left(\frac1{m!}\sum_{\sigma\in S_m}
\rho_{\lambda,n}(\sigma)\right)
\quad\text{on }M_{\lambda,n}.
\]

T-004 computes the dimension of its ambient balanced-weight space, and T-005 proves by an explicit determinant-sign calculation that this dimension alone can differ from the projected dimension. Subsequent work now evaluates the projected space by a terminating positive-count construction: G-009 in `work/root/invariant_polytope_report.md` gives an explicit invariant-algebra presentation and standard-monomial polytope sums for every symmetric plethysm coefficient. G-010 in `work/root/general_polytope_extensions.md` extends this to general Schur plethysm; G-011 gives the analogous positive counts for the actual canonical-map image, kernel, and cokernel modules. Their input consists of specified polynomials and finite group actions, with no coefficient oracle. Their output size and running time have no proved polynomial bound in the varying parameters.

The smaller direct formulas remain useful: T-006–T-007 evaluate classical families, G-012 in `work/root/rank_three_presentation.md` gives four explicit polytopes for the complete outer-degree-three family, T-012–T-013 give the stable width-five and width-six formulas, and T-016–T-020 in `work/theta/width7/width7_report.md` evaluate the three-parameter end-node sector of the width-seven exterior-power factor. T-024–T-028 in `work/theta/end_node/` now give a uniform small polytope and an arithmetic nonvanishing test for every outer Schur functor with inner symmetric power and output shape `(alpha,beta^(m-2),gamma)`, together with an explicit toric degeneration for the symmetric-outer algebra. T-009 excludes its precisely stated homogeneous Ehrhart model and is consistent with these finite sums of graded fibers. The remaining research problem in this direction is a small, efficient construction outside the proved direct families, together with uniform inequalities for the still-open canonical-map parameter families. The existence of a terminating positive count is no longer left as an unevaluated gate.

## Source and checking notes

1. Supplied Landsberg source was read at the theorem/proof and surrounding definitions; group actions and the two noted source typos were checked directly.
2. The compact-centralizer proof and explicit vacuum-character calculation in T-001 were read in full after drafting; the action convention is included to prevent a hidden metaplectic twist.
3. All derived proofs T-002–T-006 and T-008 were read in full; details of the balanced permutation action, determinant sign, and multiplication domain were checked.
4. T-007 is carried as an established identity with checked secondary exact locators; its original book proofs have not been read in this run.
5. T-009 is a cited theorem whose statement and reciprocity calculation were read in the primary article. Its complete inhomogeneous-polytope proof was read; no independent proof of that stronger clause is claimed.


# Additional exact constructions and limits

Run `GCT_PLETH_20261121_run01`; model GPT-6 Astra Pro; effort setting not exposed. Findings below are proved formulations for this investigation; no priority claim is made. All vector spaces in the representation calculations have characteristic zero unless an integral model is explicitly specified.

## G-001. A balanced weight space with no monomial basis

Let `E=C^5`, `lambda=(5,2,1,1,1)`, and let permutation matrices act on
\[
M=(S_{(5,2,1,1,1)}E)_{(2,2,2,2,2)}.
\]
Then `M` is isomorphic as an `S_5` representation to `sgn tensor U_5`, where `U_5={(z_1,...,z_5):sum z_i=0}`. There is no basis of `M` that `S_5` permutes up to nonzero scalar factors. In particular there is no such basis indexed by its four balanced Gelfand--Tsetlin patterns.

**Proof.** The multiplication map
\[
\operatorname{Sym}^{4}E\otimes E\longrightarrow\operatorname{Sym}^{5}E
\]
is surjective, and its kernel is `S_(4,1)E`, by the degree-one Pieri rule. On weight `(1^5)` the source has basis
\[
v_i=\left(\prod_{j\ne i}e_j\right)\otimes e_i\quad(1\le i\le5).
\]
Permutation matrices permute these five vectors, and multiplication sends all of them to `e_1e_2e_3e_4e_5`. The kernel on this weight is exactly `U_5`. Tensoring with `det E` shifts the highest weight from `(4,1,0,0,0)` to `(5,2,1,1,1)` and the balanced weight from `(1^5)` to `(2^5)`; its restriction to permutation matrices is the sign character. This gives the stated isomorphism, including the character twist.

A monomial basis of size four would give a homomorphism `A_5→S_4`. The group `A_5` is simple: its conjugacy-class sizes are `1,15,20,12,12`, and no sum containing 1 of a proper nonempty subcollection of the four nonidentity classes is a proper divisor of 60. To verify these class sizes, the double transpositions number 15 and have centralizer of order 4 in `A_5`; the 3-cycles number 20 and have centralizer of order 3; the 24 five-cycles split into two classes of size 12 since their centralizer has order 5. Lagrange's theorem proves simplicity from the listed sizes. The homomorphism to `S_4` therefore has trivial image, since 60 exceeds 24. Thus every element of `A_5` would act diagonally in the proposed basis. The resulting image is abelian. A nonabelian simple group has trivial abelian image, so `A_5` would act trivially on `M`. But `(123)` acts nontrivially on `e_1-e_2` in `U_5`. On `A_5` the sign twist is trivial. This is a contradiction.

The argument identifies a specific failure of an orbit-counting approach to the balanced-weight normalizer action. It makes no assertion excluding other lattice-point descriptions. The exact group-scheme map is `S_5→GL(E)` by permutation matrices, followed by `S_lambda`; the determinant character records its passage through `SL(E)`.

## G-002. Exact nonnegative determinant certificates for plethysm and the canonical map

Let `N=mn`, let `[lambda]_Z` be the integral Specht lattice in its standard polytabloid basis, and let `rho` be its permutation action. Let `H=S_n wr S_m` be the row wreath subgroup of `S_N`, and `K=S_m wr S_n` the column wreath subgroup, with cells indexed by the same `m by n` grid. Set
\[
A_H=\sum_{h\in H}\rho(h),\qquad A_K=\sum_{k\in K}\rho(k),\qquad B=A_KA_H.
\tag{G2.1}
\]
These are finite integer matrices. Their ranks over `Q` are respectively
\[
\operatorname{rank} A_H=a_{m,n}^{\lambda},\qquad
\operatorname{rank} B=r_{m,n}^{\lambda},
\tag{G2.2}
\]
where `r` is the multiplicity of `S_lambda` in the image of the normalized Hadamard--Howe map. For either `C=A_H` or `C=B`,
\[
\det(I+tCC^{\mathsf T})=
\sum_{j\ge0}t^j
\sum_{\substack{|I|=|J|=j}}\det(C_{I,J})^2.
\tag{G2.3}
\]
Its degree is the corresponding rank. This gives exact finite sums of squares as certificates for every multiplicity and every map rank.

**Proof.** Averaging `P_H=A_H/|H|` is an idempotent with image `[lambda]^H`, because left multiplication permutes the terms of the average, and the average fixes every invariant vector. Schur--Weyl duality followed by row symmetrization identifies this invariant space with the multiplicity space of `S_lambda` in `Sym^m(Sym^n V)`. The normalized grid map on that multiplicity space is `P_K|_[lambda]^H`; hence `P_KP_H` has the same image, and multiplication by the positive nonzero integers `|K||H|` does not change its rank. This proves (G2.2) with the specified map, rather than an arbitrary equivariant map having the same source and target.

The coefficient of `t^j` in `det(I+tD)` is the sum of all principal `j by j` minors of `D`, by multilinearity of determinant. Apply this to `D=CC^T` and then apply Cauchy--Binet to each principal minor. The result is (G2.3). A real matrix of rank `s` has a nonzero `s by s` minor and every larger minor vanishes. The coefficient at `t^s` is consequently positive and all coefficients above it are zero. This proves the degree assertion without relying on a choice of invariant inner product for the Specht basis.

The finite sum in (G2.3) includes determinants that must themselves be evaluated. The formula therefore records the exact remaining nonzero-minor test; no efficient lattice-point rule or complexity-class containment is inferred from it. In scheme language the rank conditions are the determinantal closed subschemes of the affine space of matrices, cut out by these minors. The displayed integral matrices give actual integral points of those schemes.

## G-003. The integral Chow pullback, divided powers, and the image algebra

Let `E=Z^r`, and let
\[
\mu:E^{\times n}\longrightarrow\operatorname{Sym}^n E,
\qquad(v_1,\ldots,v_n)\longmapsto v_1\cdots v_n
\tag{G3.1}
\]
be the multiplication morphism of affine schemes over `Z`. Its degree-`d` coordinate pullback is
\[
\mu_d^*:
\operatorname{Sym}^d\bigl((\operatorname{Sym}^nE)^\vee\bigr)
\longrightarrow
\left((\operatorname{Sym}^d E^\vee)^{\otimes n}\right)^{S_n}
=\Gamma^n(\operatorname{Sym}^dE^\vee).
\tag{G3.2}
\]
Here `(Sym^n E)^vee=Gamma^n(E^vee)` and the right equality is the divided-power identification for a finite free module. With the rational norm isomorphisms `Sym^s(F)→(F^tensor s)^{S_s}`, normalized by `1/s!`, equation (G3.2) becomes the canonical grid map
\[
h_{d,n}:\operatorname{Sym}^d(\operatorname{Sym}^n E_{\mathbb Q}^\vee)
\longrightarrow\operatorname{Sym}^n(\operatorname{Sym}^d E_{\mathbb Q}^\vee).
\tag{G3.3}
\]

**Proof.** A homogeneous degree-`d` function on `Sym^n E` pulls back to a polynomial of multidegree `(d,...,d)` in the `n` input vectors. The multidegree component of the polynomial ring is `(Sym^d E^vee)^tensor n`. The map (G3.1) is unchanged by permuting input vectors, so its pullback belongs to its `S_n` invariants. For a free module, the orbit sums of tensor basis words give both a basis of symmetric tensors and the defining basis of divided powers; this proves the integral equality in (G3.2). The dual of coinvariant symmetric powers is the invariant tensor module, yielding the other divided-power identification.

Over `Q`, the inverse of the quotient from invariant tensors to coinvariant symmetric tensors is normalized averaging. Apply that explicit map in both the `d`-row and `n`-column tensor arrangements. Coordinate pullback multiplies entries along the transposed arrangement; the resulting invariant tensor is precisely column averaging of the row-invariant tensor. This is the grid definition of (G3.3), with no unrecorded integral identification of symmetric and divided powers.

Set `A_Z=im(mu^*)` inside the polynomial ring `Z[E^times n]`, with the grading just specified. Its kernel is an ideal in the polynomial coordinate ring of `Sym^n E`, and
\[
\mathcal C_{n,r}=\operatorname{Spec}A_{\mathbb Z}
\]
is the scheme-theoretic image of (G3.1). This is EGA I, Proposition 9.5.1 and Corollary 9.5.2, printed p.176, with Definition 9.5.3 on p.177. The image is a subring of a torsion-free abelian group, hence is torsion-free, hence is flat over `Z`: for a principal ideal domain, a module is flat precisely when it is torsion-free. One proof of the latter statement writes a torsion-free module as the filtered union of its finitely generated free submodules and uses preservation of flatness under filtered colimits. Each graded part is finite free as a subgroup of a finite free multidegree component. This proves flatness of this specific integral model. It does not identify every special fiber with the scheme-theoretic image of the corresponding fiber map; the precise specialization map is `A_Z tensor k→im(mu_k^*)`, and injectivity of that map remains a separate saturation question.

Over `Q`, the degree-`d` Schur multiplicities of `A_Q` are the ranks `r_(d,n)^lambda` of G-002, with the usual dual convention for coordinate functions. The rank equation thus has an explicit morphism to the orbit-closure coordinate ring. The generic span of `n` independent linear factors identifies the dense product orbit with that of `x_1...x_n` when `r>=n`, so this is the affine Chow cone in that range. The construction of (G3.1) is valid for every `r`.

The projective Hilbert and Quot functors with fixed Hilbert polynomial are represented by the schemes of FGA, Bourbaki exposé 221, Theorems 3.1 and 3.2, pp.259--260; the Hilbert specialization is after Proposition 3.8, p.265. They parametrize flat families of projective closed subschemes and coherent quotient sheaves with that Hilbert polynomial. The finite matrices in (G3.2) remain the explicitly identified maps whose minors determine the graded ranks; the representing property alone supplies no new nonzero minor.

## G-004. Purity and the invariant projector on a finite étale example

Let `X=Spec F_(q^2)` over `F_q`, let `ell` be prime to `q`, and let `sigma` generate its two-element Galois group. The degree-zero étale cohomology of `X` after base change to an algebraic closure is `Q_ell e_0 directsum Q_ell e_1`; Frobenius interchanges the two basis vectors. The two idempotents
\[
e_+=\tfrac12(1+\sigma),\qquad e_-=\tfrac12(1-\sigma)
\tag{G4.1}
\]
have one-dimensional images with Frobenius eigenvalues `1` and `-1` respectively. Both are pure of weight zero, since both eigenvalues have complex absolute value one, but their Galois-invariant dimensions are respectively one and zero.

**Proof.** The étale cohomology of a two-point geometric scheme in degree zero is its functions, and higher cohomology vanishes. The Frobenius action permutes the two embeddings of the degree-two finite field extension, so its eigenvectors are `e_0+e_1` and `e_0-e_1`. Formula (G4.1), the two eigenvalues, and the invariant dimensions follow by direct matrix multiplication. This works also for `ell=2`, since the coefficient field is `Q_2` and `1/2` exists. In the category of rational Artin motives the same idempotents are the two projectors on this finite étale motive.

This supplies an exact test of the proposed passage from a pure cohomological object to a symmetric-group-invariant multiplicity: the group projector must be carried along the realization. Purity alone assigns the same weight to the two displayed lines while the invariant projector has ranks one and zero. The example does not rule out a geometric construction that includes that projector. The motivic interpretation applies to this explicit finite étale object, without assuming a general category of motives has been specified for archive cote12/scan041.

## G-005. A positive polytope formulation for every two-row output

This section carries the known marked-tree theorem of Pak--Panova--Swanson, *A combinatorial interpretation for certain plethysm and Kronecker coefficients* (4 November 2025), Theorems 1.1/4.5 and 1.2/5.2, into explicit polytope language. The known combinatorial interpretation is not claimed as a new theorem of this run.

For a nonempty outer partition `mu`, inner row `(k)` with `k>=1`, and output `(N-r,r)` where `N=k|mu|` and `0<=r<=N/2`, take the finite set of unmarked GOH trees `G(mu,k)` defined in that work, Definitions 3.5 and 3.8. The empty outer partition has the sole coefficient one at the empty output. The definition, including all integer partition labels, is reproduced below so that the formula is executable from the paper. For a tree `T` order its leaves in the prescribed lexicographic depth-first order, and write their nonnegative labels as `a_1,...,a_t`. Put
\[
s(T)=\frac{N-\sum_i a_i}{2}.
\]
Define the bounded rational polytope `P_T(r)` in coordinates `z_1,...,z_t` by
\[
z_1=0,\qquad z_t=r-s(T),\qquad z_i\le z_{i+1},
\tag{G5.1}
\]
\[
z_{i+1}-z_i\le a_{i+1},\qquad
z_{i+1}+z_i\le a_1+\cdots+a_i
\quad(1\le i<t).
\tag{G5.2}
\]
Then
\[
p_{\mu,(k)}^{(N-r,r)}
=\sum_{T\in G(\mu,k)}\#(P_T(r)\cap\mathbb Z^t).
\tag{G5.3}
\]
For the symmetric outer index `(m)`, one may instead use the KOH trees `T(n,m)` for `N=mn`, and the same formula also equals
\[
g((mn-r,r),(n^m),(n^m)).
\tag{G5.4}
\]

**Proof of the asserted form.** The marks of Pak--Panova--Swanson, Definitions 4.4 and 5.1, satisfy `0=z_1<=...<=z_t=r-s(T)` and
`z_(i+1)-z_i<=min(sum_(j<=i)a_j-2z_i,a_(i+1))`.
Separating this minimum into its two linear inequalities gives exactly (G5.2). Thus the identity map on mark vectors is a bijection between their marked trees with fixed underlying tree and the integer points of `P_T(r)`. The endpoint and monotonicity bound every coordinate between zero and `r-s(T)`; a negative endpoint gives the empty polytope. Summing the cited theorem over underlying trees proves (G5.3) and (G5.4). The proof of the change of language is complete and uses no subtraction of lattice-point counts.

For a general inner partition `nu`, evaluation in rank two gives the following exact transfer. Partitions with three or more rows have `S_nu(C^2)=0`. For `nu=(b+k,b)`, the isomorphism
\[
S_{(b+k,b)}(\mathbb C^2)=\det^b\otimes\operatorname{Sym}^k\mathbb C^2
\]
and homogeneity of `S_mu` give the determinant shift by `b|mu|` in each output row. This is precisely Pak--Panova--Swanson, Lemma 2.1. The shifted output with negative second row has coefficient zero. For `k=0`, the inner representation is a line, and its outer Schur functor is zero for `ell(mu)>1` and is `det^(b|mu|)` for `mu=(|mu|)`. This covers the rank-one edge case without invoking a zero-parameter tree convention.

The corresponding vector-bundle statement is obtained from the rank-two frame torsor and the above determinant-line isomorphism. Every polytope computes the coefficient of the associated Schur functor in `K_0(BGL_2)` over a characteristic-zero field. The `SL_2` Clebsch--Gordan branching chain behind the marks is an exact chain of interlacing inequalities; it supplies a successful instance of the branching approach outside the stable-tail range.

### Explicit tree indexing

For a partition `alpha`, write `m_j(alpha)` for the multiplicity of its part `j`, `alpha'` for its conjugate, and `Q_j(alpha)=sum_(x<=j)alpha'_x`. A KOH vertex is labeled `(alpha,a,b)` with `a>=0`, `b>=1`, `alpha partition of b`. A vertex with `b=1` is a leaf with scalar label `a`. A vertex with `b>=2` has one child for each distinct part `j` of `alpha`, in increasing order, with parameters
\[
a^{(j)}=(a+2)j-2Q_j(\alpha),\qquad
b^{(j)}=m_j(\alpha),
\]
and its partition label ranges over the partitions of `b^(j)`. A negative `a^(j)` gives no tree. The root parameters of `T(n,m)` are `(a,b)=(n,m)`.

A GOH root of type `(mu,k)`, for `ell=ell(mu)` and `n=|mu|`, carries a sequence of partitions `nu^(0),...,nu^(ell)` with
\[
\nu^{(0)}=(1^n),\qquad
|\nu^{(i)}|=\sum_{j\ge i+1}\mu_j,
\]
\[
P_j^i=Q_j(\nu^{(i+1)})-2Q_j(\nu^{(i)})+Q_j(\nu^{(i-1)})\ge0
\quad(1\le i<\ell,\ 1\le j\le n).
\]
Let `m=(nu^(1))'_1`, with `m=0` for an empty partition, and retain configurations with `m<=k`. For every pair `(i,j)` with `m_j(nu^(i))>0`, attach a KOH tree of type `(P_j^i,m_j(nu^(i)))`, ordered lexicographically. For `m<k`, attach also a final KOH tree of type `(n,k-m)`. This defines the complete finite index set in (G5.3). Finiteness and the equal-center property `s(T)` are the cited Proposition 3.4 and Proposition 3.9; their proofs are repeated application of the KOH and GOH identities, Theorems 3.1 and 3.6.

The printed induction proof of Lemma 4.2 has a local indexing slip: its last inequality writes `|a|-2k_t`, whereas substitution into Lemma 4.1 gives `|a|-2k_(t-1)`. The statement of Lemma 4.2 and both marking definitions have the correct latter index. The polytope above uses those correct statements.


A second local correction concerns Lemma 4.1, printed p.8. Put \(L=\min(r-2i,s-2j)\). Direct multiplication of finite geometric sums gives
\[
(1-q)(q^i+\cdots+q^{r-i})(q^j+\cdots+q^{s-j})
=q^{i+j}(1+\cdots+q^L)-q^{r+s-i-j+1}(1+\cdots+q^{-L}).
\]
The printed negative leading exponent omits the final one. For \(r=s=1,i=j=0\), the left side is \(1+q-q^2-q^3\), while the printed expression is \(1-q^2\). The smallest exponent in the corrected negative term is \(i+j+\max(r-2i,s-2j)+1>(r+s)/2\). Thus its actual coefficient assertion below the midpoint follows, and the corrected Lemma 4.2 induction and the tree formulas retain their stated conclusions. The independent reviewer inspected the PDF page visually and checked this entire repair.


# Outer degree three and the canonical two-row blocks

## G-006. Canonical-map isomorphisms on every two-row block

For every `m,n>=1`, the canonical map `h_(m,n)` is an isomorphism on each isotypic multiplicity space indexed by a partition with at most two rows. In particular
\[
r_{m,n}^{\lambda}=a_{m,n}^{\lambda}=a_{n,m}^{\lambda}
\quad(\ell(\lambda)\le2).
\]
This is the natural-transformation form of the classical canonical Hermite reciprocity theorem, stated in the supplied Landsberg survey, Theorem 7.21, §7.7. Its precise transfer to arbitrary ambient dimension is as follows.

**Proof of the transfer.** A natural transformation between homogeneous characteristic-zero polynomial functors is the direct sum, over partitions `lambda`, of the identity on `S_lambda` tensored with a fixed linear map between its multiplicity spaces. Evaluation on `C^2` kills exactly the summands of length greater than two. Canonical Hermite reciprocity says the evaluated transformation is an isomorphism. Consequently every retained multiplicity map is invertible, and those same maps occur after evaluation in every larger dimension. This proves the displayed rank equality, including the specified canonical map.

The geometric realization is the multiplication morphism of G-003 in rank two: every binary form factors into linear forms over `C`, so the Chow image is the whole affine space of binary forms. Its coordinate pullback is injective. Both sides have dimension `binom(m+n,m)`, giving the canonical isomorphism. This is the exact morphism relating the factorization statement, the coordinate ring, and the canonical map; the source theorem is known.

## G-007. Explicit one-dimensional lattice counts for every outer Schur index of size three

The coefficients in this family are classical (Thrall and Chen). Their explicit current primary presentation is Maas--Gariépy and Tétreault, *3-Plethysms of homogeneous and elementary symmetric functions*, arXiv:2209.14942v1, §4.2, pp.8--9; their tableau realization is Theorem 1, §7.3, p.20. Here the formula is put in the literal permutation-matrix realization of T-002, retaining the two finite-character corrections.

Let `lambda=(lambda_1,lambda_2,lambda_3)` be a partition of `3n`, padded by zeros. Set
\[
L=\max(\lambda_3,2n-\lambda_1),\qquad
U=\min(\lambda_2,2n-\lambda_2,n),\qquad K=U-L+1.
\]
Define `d_2=0` for even `K` and `d_2=(-1)^L` for odd `K`. Let
\[
(b_1,b_2,b_3)=(\lambda_1+2,\lambda_2+1,\lambda_3)\pmod3.
\]
Set `d_3=0` for repeated residues; for three distinct residues set `d_3` equal to the sign of the permutation carrying the ordered residue list `(2,1,0)` to `(b_1,b_2,b_3)`. Then
\[
p_{(3),(n)}^{\lambda}=\frac{K+3d_2+2d_3}{6},\qquad
p_{(1,1,1),(n)}^{\lambda}=\frac{K-3d_2+2d_3}{6},\qquad
p_{(2,1),(n)}^{\lambda}=\frac{K-d_3}{3}.
\tag{G7.1}
\]
Each quotient is the following positive lattice-point formula: for its numerator `B` and denominator `D`,
\[
\boxed{\#\{z\in\mathbb Z:1\le z,\ Dz\le B\}.}
\tag{G7.2}
\]
The residue tests are finite case selection, and within each selected chamber the displayed bounds are affine linear in `lambda,n`. The intervals are allowed to be empty. The statement imposes no homogeneous-dilation requirement.

**Proof of the normalizer dictionary.** The balanced space `M=(S_lambda C^3)_(n,n,n)` is a representation of `S_3`. Restricting first to `GL_2 times GL_1`, the interlacing highest weights contributing balanced degree are `(2n-k,k)` for exactly `L<=k<=U`. Each contributes a single `(n,n)` weight line. The transposition of the first two basis vectors acts on this line by `(-1)^k`, as the explicit determinant calculation in T-006 shows. Thus its trace is `sum_(k=L)^U(-1)^k=d_2` and the identity trace is `K`.

A three-cycle permutes the torus weight spaces of `S_lambda C^3`. Only a weight constant on all three coordinates contributes to its trace; the total degree `3n` makes that weight `(n,n,n)`. Its trace on `M` therefore equals its trace on the whole representation. The cycle has eigenvalues `1,zeta,zeta^2` for a primitive cube root `zeta`. The Weyl alternant formula evaluates its character as
\[
\frac{\det(x_j^{\lambda_i+3-i})_{1\le i,j\le3}}
{\det(x_j^{3-i})_{1\le i,j\le3}},
\qquad(x_1,x_2,x_3)=(1,\zeta,\zeta^2).
\]
The denominator is nonzero. Repeated exponent residues give two equal rows and value zero; distinct residues give the stated row-permutation sign. Thus the three-cycle trace is `d_3`.

The three irreducible characters of `S_3` have values `(1,1,1)`, `(1,-1,1)`, and `(2,0,-1)` on identity, transpositions and three-cycles, whose class sizes are `1,3,2`. Taking these character inner products proves (G7.1), via T-003. Each is consequently a nonnegative integer. For `B=Dc` with `c` that nonnegative multiplicity, the integer solutions of (G7.2) are exactly `1,...,c`; the interval endpoints were computed by the explicit bounded trace calculation, rather than by a general coefficient oracle. This proves (G7.2). The interlacing interval is nonempty for every partition of `3n` of length at most three; this also follows from the inequalities `lambda_1>=n>=lambda_3` and `lambda_1+lambda_2+lambda_3=3n` in the definitions of `L,U`.

The geometric statement is the equality in the characteristic-zero representation ring `K_0(BGL_r)` and its pullback along the frame torsor of a locally free rank-`r` sheaf. The two traces are taken along the explicit constant subgroup scheme `S_3→GL_3` of permutation matrices, and the determinant factor in the transposition action is retained. Hence this evaluates, rather than omits, the normalizer projector for the entire outer-degree-three family.


# Positive lattice-point formulas from explicit invariant presentations

## G-008. A repeated-odd-part nonvanishing family in unbounded width

Put `S=<4,6,7>={0,4,6,7,8} union {k:k>=10}`. For every `k in S` with `k>=4` and every `j>=0`,
\[
\boxed{c((k^{4j}))\ge1.}
\tag{G8.1}
\]
The empty partition has coefficient one. More generally, let `lambda` be a partition with no part one. Its even parts have arbitrary multiplicities. For each odd part `i in S`, its multiplicity has the form `4q_i+epsilon_i`, with `q_i>=0` and `epsilon_i in {0,1}`; for the remaining odd parts `3,5,9`, its multiplicity is at most one. Then
\[
\boxed{c(\lambda)\ge1.}
\tag{G8.2}
\]
The finite plethysm coefficients in T-010's stability range have the same positive value. The theorem concerns a specified sufficient family; it does not assert an exhaustive support classification.

**Proof, including the exact finite seeds.** Let `W=C^4`. The invariant algebra `Sym(Sym^4 W)^(SL_4)` is a subalgebra of a polynomial algebra and therefore a domain. The exact seed multiplicities in degrees `4,6,7` are each one. The finite certificates are supplied in `QUATERNARY_QUARTIC_INVARIANTS.tsv` and independently in `QUARTIC_SEEDS_INDEPENDENT_CHECK.tsv`, with the three complete class-sum files. Here is the precise mathematical verification of those finite numbers. The torus character is the coefficient of `t^k` in
\[
\prod_{\substack{\alpha\in\mathbb Z_{\ge0}^4\\|\alpha|=4}}
(1-tx^\alpha)^{-1}.
\tag{G8.3}
\]
There are 35 factors. With `rho=(3,2,1,0)` and `M_k(w)` its integer weight coefficients, Weyl's alternant identity gives the invariant multiplicity
\[
\sum_{\sigma\in S_4}\operatorname{sgn}(\sigma)
M_k((k,k,k,k)+\rho-\sigma\rho).
\tag{G8.4}
\]
The supplied program expands the 35 geometric series by integer dynamic programming, computes all 24 terms of (G8.4), and obtains one in each of the three asserted degrees. Only coordinates at most `k+3` can contribute; all factor weights are nonnegative, so truncation beyond that box preserves all required coefficients. The independent program instead expands the wreath-product cycle index and sums symmetric-group characters by Murnaghan--Nakayama; it obtains the same three values. This is an exact finite computation certificate, not a proof-assistant claim.

Choose nonzero invariant seed vectors. Their products are nonzero, so every degree in `S` contains an invariant. The displayed description of `S` follows because `10=4+6`, `11=4+7`, `12=6+6`, `13=6+7`, and adding four covers every subsequent integer; direct checking settles `0,...,9`.

Under the symmetric-function involution `omega`, the even inner degree four gives
\[
\omega(h_k[h_4])=h_k[e_4].
\tag{G8.5}
\]
Thus the coefficient of `(k^4)` in `Sym^k(Sym^4 W)` equals the coefficient of `(4^k)` in `Sym^k(Lambda^4 C^k)`. This is the determinant representation `det^4`, so a nonzero highest vector of weight `4 omega_k` exists in that symmetric algebra. Its `j`th power is nonzero and has highest weight `4j omega_k`. This is the constituent for tail `(k^(4j))` in the exact module M_k of T-010, proving (G8.1).

For (G8.2), work in rank `r=lambda_1`. Embed every seed highest vector from rank `i` using the first `i` coordinates into `Sym^i(Lambda^4 C^r)`. It remains highest for `GL_r`: positive root operators involving a basis coordinate beyond `i` annihilate it, and the operators within the first `i` coordinates already do so. Multiply the prescribed powers of all these vectors inside the single polynomial algebra `Sym(Lambda^4 C^r)`. This product is nonzero. The additional pure highest vectors for the arbitrary even parts live in their corresponding symmetric-algebra factors; the part four contributes another power in the same domain. The residual odd parts with multiplicities `epsilon_i=0,1` select scalars or highest wedge vectors in the corresponding exterior-algebra factors. Their tensor product is nonzero, highest, and has total highest weight `lambda'`. T-010 proves (G8.2). This proof records the factor in which multiplication occurs, so that no unsupported domain assertion about the full tensor product of exterior algebras is used.

## G-009. A terminating positive-polytope procedure for all symmetric plethysm

For every positive integer `m`, the following finite procedure computes an integer matrix `D_m` with columns `d_j=(n_j,lambda^(j))`, all `n_j>=1`, and a finite collection `C_m` of pairs `(u,S)` with `u in Z_{≥0}^q`, `S subset {1,...,q}`. The output depends only on `m`. For all `n>=0` and partitions `lambda` of `mn`, of length at most `m`, it gives
\[
\boxed{
a_{m,n}^{\lambda}=
\sum_{(u,S)\in C_m}
\#\left\{z\in\mathbb Z_{\ge0}^{S}:
D_{m,S}z=(n,\lambda)-D_m u\right\}.
}
\tag{G9.1}
\]
Each summand is the integer-point count of a bounded rational polytope. The construction uses flag minors, a finitely generated monoid of balanced exponents, Reynolds averages of bounded ordinary degree, and polynomial elimination. It makes no assumption about any unknown plethysm coefficient, any canonical basis, or the sign of any character sum. No polynomial bound in the varying parameter `m` for its output size or running time is asserted.

### The finite construction

Let `X=(x_ij)` be an `m by m` matrix of indeterminates over `Q`. For every nonempty subset `I subset {1,...,m}`, let `p_I(X)` be the minor with row set `I` and first `|I|` columns. Introduce a formal variable `z_I` for each such subset. Let
\[
\mathcal H_m=\left\{b\in\mathbb Z_{\ge0}^{2^m-1}:
\sum_{I\ni1}b_I=\cdots=\sum_{I\ni m}b_I\right\}.
\tag{G9.2}
\]
Compute its finite Hilbert basis `b^(1),...,b^(s)`, and put `q_l=product_I p_I^{b_I^(l)}`. The common sum in (G9.2) is its positive integer `n_l`; its right-torus highest weight is
\[
\lambda^{(l)}=\sum_I b_I^{(l)}\omega_{|I|},
\quad\omega_j=(1^j,0^{m-j}).
\tag{G9.3}
\]

Row permutation matrices send each formal `z_I` to `epsilon(sigma,I) z_(sigma I)`, where `epsilon` is the sign needed to sort the permuted row indices. They consequently permute Hilbert-basis monomials up to signs. Let `Y_1,...,Y_s` carry this signed permutation action and map `Y_l` to `q_l`. Form every Reynolds average
\[
\mathcal R(Y^v)=\frac1{m!}\sum_{\sigma\in S_m}\sigma(Y^v),
\qquad1\le|v|\le m!.
\tag{G9.4}
\]
Substitute `Y_l=q_l(X)` and discard zero polynomials. Denote the remaining explicit polynomials by `f_1,...,f_q`; duplicates may be retained. Their degrees `(n_j,lambda^(j))` give the columns of `D_m`.

Compute the elimination ideal
\[
J=\bigl(Z_j-f_j(X):1\le j\le q\bigr)
\cap\mathbb Q[Z_1,\ldots,Z_q].
\tag{G9.5}
\]
Use any fixed monomial order to compute a homogeneous Gröbner basis of `J`, and let `J_0` be the monomial ideal of its leading terms. Let `B_j` be the largest exponent of `Z_j` in the finite minimal monomial generating set of `J_0`, with `B_j=0` when it never occurs. Partition the nonnegative exponent lattice, independently in each coordinate, into the singleton cells `0,...,B_j-1` and the final interval `B_j+Z_{≥0}`. A resulting cell is uniquely `u+Z_{≥0}^S`, with `u_j=B_j` on its free coordinates and a selected smaller integer on the other coordinates. Retain exactly those cells with `Z^u notin J_0`. These retained pairs form `C_m`.

All steps are finite and effective: Gordan's lemma and Hilbert-basis algorithms apply to (G9.2), finite-group Noether generation applies to (G9.4), and Buchberger elimination terminates for (G9.5). Exact cited locators are supplied in the background register. The Gröbner-basis step uses only the explicitly constructed polynomials `f_j(X)`.

### Proof of the invariant-ring realization

Let `E=F=Q^m`, with left and right general linear actions on
`P=Sym(E tensor F)`. Let `U` be the upper unipotent group on the right, and let `T_0` be the determinant-one diagonal torus on the left. Cauchy duality gives
\[
R=P^U=\bigoplus_\lambda S_\lambda E\otimes L_\lambda,
\tag{G9.6}
\]
where `L_lambda` is the right highest-weight line. The subalgebra generated by the flag minors is all of `R`. To see this, the flag minors of size `j` span its component `Lambda^j E tensor L_(omega_j)`. The product of components with multiplicities `lambda_j-lambda_(j+1)` has right weight `lambda`. It is nonzero because `R` is a domain. Its image is a nonzero left `GL(E)` submodule of the irreducible right-weight component `S_lambda E tensor L_lambda`, hence it equals that whole component. Every partition is a sum of these fundamental weights. This proves the claimed generation, including the concrete generators used above.

The torus `T_0` fixes exactly the equal left-weight components `(n^m)`. Therefore
\[
R^{T_0}=\bigoplus_{n,\lambda}
M_{\lambda,n}\otimes L_\lambda.
\tag{G9.7}
\]
The left permutation matrices normalize `T_0` and commute with the right action. Taking their invariants gives the actual finitely generated algebra
\[
A_m=(R^{T_0})^{S_m},\qquad
\dim(A_m)_{(n,\lambda)}=a_{m,n}^{\lambda}.
\tag{G9.8}
\]
The equality of dimensions is T-002 with its literal permutation action.

For completeness, the finite presentation above indeed generates this exact algebra. The polynomial ring in formal flag-minor variables surjects equivariantly onto `R`. Extracting a torus weight is exact: a preimage of a homogeneous invariant decomposes into weight components, and its zero-weight component still maps to that invariant. The torus-invariant monomials are exactly (G9.2); their Hilbert basis consequently gives the surjection `Q[Y_1,...,Y_s]→R^{T_0}`. The basis is preserved by the signed permutation action because indecomposability in the monoid is preserved by coordinate permutations. Averaging over `S_m` makes invariants exact as well. Noether's degree bound says that the averages of monomials of ordinary `Y`-degree at most `m!` generate `Q[Y]^{S_m}`. Their images thus generate precisely `A_m`. Their explicit image kernel is (G9.5). Every image generator is homogeneous for `(n,lambda)`, and `n_j>0`, because every nonconstant monomial in (G9.2) has positive common row sum.

### Proof of the positive count

Residue classes of monomials outside `J_0` form a basis of `Q[Z]/J`, by Gröbner division. The ideal is multihomogeneous for `D_m`, so division preserves the grading and this is a homogeneous basis of `A_m`. For any monomial generator `Z^a` of `J_0`, the test `v_j>=a_j` is constant throughout each cell of the above partition: a fixed coordinate is constant, and a free coordinate satisfies `v_j>=B_j>=a_j`. Consequently membership in `J_0` is constant on the entire cell. Retaining its lower corner outside `J_0` retains exactly the standard monomials, with no overlaps. Its exponents have the unique form `u+z`, `z in Z_{≥0}^S`, and its degree is `D_m u+D_(m,S)z`. Taking degree `(n,lambda)` proves (G9.1).

Finally its first degree equation is
\[
\sum_{j\in S}n_j z_j=n-\sum_j n_j u_j,
\]
with every `n_j>=1`. Every nonnegative real solution has each coordinate at most `n` when the right side is nonnegative; a negative right side gives an empty set. Thus the real polyhedra being counted are bounded. This completes the proof for all parameters, including vanishing coefficients.

### The fully computed rank-two instance

For `m=2`, the flag algebra is `Q[x_1,x_2,delta]`; the right highest weights are `(1,0),(1,0),(1,1)`. The balanced torus algebra is `Q[u,v]`, with `u=x_1x_2`, `v=delta`. The transposition fixes `u` and negates `v`, so
\[
A_2=\mathbb Q[u,v^2],\qquad
\deg u=(1;2,0),\quad\deg v^2=(2;2,2).
\]
Its initial ideal is zero, and G-009 gives the single polytope
\[
\{(a,b)\in\mathbb R_{\ge0}^2:
a+2b=n,\ (2a+2b,2b)=\lambda\}.
\]
This recovers T-006 through the exact invariant-algebra morphism. It is also an explicit check that the row-permutation determinant sign has survived the construction.

### Geometric and complexity content

The generators and relations define affine schemes over `Q`; the maps are given by the flag minors, the torus monomial morphism, and the finite-group Reynolds morphism. Clearing the finitely many rational denominators gives models over a localization of `Z`, with the characteristic-zero fiber stated above. The initial ideal gives a multigraded flat Gröbner degeneration, and its standard monomials are the lattice points used in (G9.1). The count is the class multiplicity in the same representation `K_0` and same balanced normalizer module as T-002, now evaluated by a finite presentation.

The process includes a Hilbert-basis computation in `2^m-1` variables, Reynolds enumeration through ordinary degree `m!`, polynomial elimination, and a finite cell list depending on an initial ideal. No bound polynomial in the varying input size has been proved for any of those complete precomputation data. Thus this supplies a terminating positive-polytope construction in the literal counting sense. The smaller formulas T-012--T-013 and G-007 avoid that precomputation in their stated families. GCT questions asking for efficiently constructed polytopes or uniform nonvanishing certificates retain those additional requirements; neither a complexity-class separation nor their failure follows from the construction.


# General Schur coefficients and canonical-map ranks

## G-010. The positive-polytope construction for general Schur plethysm

Let `mu` be a partition of `m>=1`, `nu` a partition of `n>=1`, and `N=mn`. Let `H=S_n wr S_m subset S_N` act on its grid of `N` letters, and let
\[
W=[\nu]^{\otimes m}\otimes\operatorname{Inf}_{S_m}^H[\mu].
\]
Use integral standard polytabloid Specht matrices and their rational duals to specify the `H` action on `W^vee` exactly. There is a terminating construction of a finite set of bounded rational polytopes whose lattice-point counts sum to `p_(mu,nu)^lambda`, for every output partition `lambda` of `N`. The data use no unknown multiplicities. They are constructed as follows from G-009.

Take the flag algebra `R_N` and its balanced torus algebra `B_N=R_N^(T_0)`. Introduce variables spanning `W^vee`, each of auxiliary degree one, and form
\[
C_{N,H,W}=(B_N\otimes\operatorname{Sym}(W^\vee))^H.
\tag{G10.1}
\]
Its grading is `(b,lambda,k)`: balanced left weight `(b^N)`, right highest weight `lambda`, and auxiliary degree `k`. It has
\[
\boxed{\dim(C_{N,H,W})_{(1,\lambda,1)}=p_{\mu,\nu}^{\lambda}.}
\tag{G10.2}
\]

To produce its finite presentation, take the same Hilbert-basis variables `Y` used for `B_N`, add the `W^vee` variables `Z`, average every monomial of ordinary `(Y,Z)` degree from one through `|H|`, and substitute the flag-minor expressions for `Y`. The group action on `Z` is its explicit rational Specht action; it need not permute these variables. Discard zero images and introduce presentation variables `T_j` for the remaining polynomials `f_j(X,Z)`. Compute the graph ideal `(T_j-f_j(X,Z))` and eliminate **both** the matrix variables `X` and the auxiliary variables `Z`, leaving its intersection with `Q[T]`. Apply the threshold-cell construction of G-009 to this exact presentation kernel. The resulting matrix has columns `(b_j,lambda^(j),k_j)` with `b_j+k_j>=1`. For each retained cell the polytope is
\[
\{z\in\mathbb R_{\ge0}^{S}:
D_Sz=(1,\lambda,1)-Du\}.
\tag{G10.3}
\]
The sum of its lattice-point counts is the coefficient in (G10.2).

**Proof.** The multilinear weight space `(S_lambda Q^N)_(1^N)` is the Specht representation `[lambda]` under literal permutation matrices. This is the multilinear Schur--Weyl identification used in T-003 and recorded in Landsberg, Corollary 3.8(1). Thus the auxiliary-degree-one component of (G10.1) in balanced degree one is
\[
([\lambda]\otimes W^\vee)^H
=\operatorname{Hom}_H(W,[\lambda]),
\]
which is the exact wreath-product formula T-003. This proves (G10.2).

The map from the polynomial ring on `Y,Z` to `B_N tensor Sym(W^vee)` is equivariant and surjective. Characteristic-zero averaging is exact, and Noether's degree bound for the finite group `H` supplies exactly the stated invariant generators. Its proof only requires a linear action, so the Specht matrices on `Z` cause no additional assumption. Each average is homogeneous in all three gradings: `H` preserves the two gradings of every Hilbert-basis orbit, and preserves ordinary degree in `Z`. Thus elimination and the standard-monomial cell argument of G-009 apply. The linear functional `b+k` is positive on every nonconstant generator, and has value two on the target. This bounds every coordinate of every polytope by two divided by that generator's positive grading. It proves boundedness and completes the positive count. Many pieces are consequently empty; retaining them does not change the formula.

For arbitrary outer Schur type and a row inner index, a smaller construction uses `R_m`, `H=S_m`, and `W=[mu]`, with target `(n,lambda,1)`. It gives the same coefficient by T-003 and has the positive grading bound `n+1`. Thus the general construction includes both exact oscillator descriptions already established.

The algebraic-geometric statement is the invariant affine scheme (G10.1) with the indicated finite-group quotient. Its auxiliary-degree-one component is the covariant module for the explicit representation `W`; its specified graded component dimension is transported by the given wreath-product Hom isomorphism. All operations, equations, and rational actions are specified, and after clearing denominators give models over a localization of `Z`. No polynomial-size bound for the construction as `m,n,mu,nu` vary is proved.

## G-011. A positive-polytope construction for each canonical-map image multiplicity

For fixed `m,n>=1`, put `N=mn`, let `G=S_N`, and take the row and column wreath subgroups `H,K` used in G-002. There is a terminating finite-presentation procedure, independent of the output partition `lambda`, giving a finite sum of bounded rational-polytope counts for
\[
r_{m,n}^{\lambda}=\operatorname{rank}(P_K|_{[\lambda]^H}).
\tag{G11.1}
\]
The procedure constructs the image of the specified canonical map, including its possibly vanishing scalar on a multiplicity-one component.

### Explicit module construction

Let `B=R_N^(T_0)` be the balanced flag algebra, and let `C=B^G=A_N`, with its explicit homogeneous invariant generators `c_1(X),...,c_q(X)` from G-009. Let `q_1(X),...,q_s(X)` be the Hilbert-basis generators of `B`. Put `h=|G|=N!`, and let `u` range over the finite box `0<=u_i<h`. Compute the polynomial vectors, here ordinary scalar polynomials,
\[
g_u(X)=P_KP_H\bigl(q_1(X)^{u_1}\cdots q_s(X)^{u_s}\bigr),
\tag{G11.2}
\]
and discard zero images. Each retained generator has its explicitly known degree `delta_u=(b_u,lambda^(u))`. Define the `C`-module
\[
M=P_K(B^H)\subseteq B^K.
\tag{G11.3}
\]
Its degree `(1,lambda)` is the image in (G11.1). Equations (G11.2) generate the entire module (G11.3), not merely the degree under consideration.

To compute a finite presentation over `Q[Z_1,...,Z_q]`, set `Z_j=c_j(X)`. The kernel of
\[
\bigoplus_u\mathbb Q[Z]e_u\longrightarrow\mathbb Q[X],
\qquad e_u\longmapsto g_u(X)
\tag{G11.4}
\]
is computable by syzygies and elimination. Explicitly, in `Q[Z,X]` compute the syzygy module of the row
\[
(g_{u_1},\ldots,g_{u_t},Z_1-c_1(X),\ldots,Z_q-c_q(X)).
\]
Project onto its first `t` components and intersect with `Q[Z]^t` by a module elimination order. This yields exactly the kernel in (G11.4). Use a homogeneous module Gröbner basis. Its leading submodule has the form `directsum_u J_u e_u`, with each `J_u` a monomial ideal. Decompose the standard monomials for each `J_u` into the threshold cells of G-009; discard a summand with `J_u=(1)`. For each retained pair `(u;v,S)` count
\[
\{z\in\mathbb Z_{\ge0}^{S}:
D_Sz=(1,\lambda)-\delta_u-Dv\}.
\tag{G11.5}
\]
The sum of these nonnegative counts is (G11.1).

### Proof of generation and the rank identity

Every element `q_i` satisfies the monic equation
\[
\prod_{g\in G}(t-gq_i)=0\quad\text{at }t=q_i,
\]
whose coefficients are in `C`. Reducing one exponent at a time shows that the monomials `q^u`, `0<=u_i<h`, generate `B` as a module over `C`. An invariant coefficient commutes with both averages: `P_H(cf)=cP_H(f)` and `P_K(cf)=cP_K(f)` for `c in C`. Averaging the finite generating expression first by `H` and then by `K` consequently proves that (G11.2) generates (G11.3).

All actions commute with the right highest-weight grading and preserve the balanced left grading. In degree `(1,lambda)`, `B` is `[lambda]` by the multilinear identification used in G-010. Thus (G11.3) in that degree is exactly `P_K([lambda]^H)`, with no substitution of an arbitrary map. This proves the asserted rank identity.

The syzygy-elimination description is exact because a vector `(a_u)` belongs to (G11.4)'s kernel precisely when `sum a_u(Z) g_u(X)` belongs to the ideal `(Z_j-c_j(X))`. Adding the coefficients expressing that ideal membership produces a syzygy of the displayed row, and projecting a syzygy gives such an ideal membership. The intersection enforces that the coefficients contain no `X` variables. These two implications prove the claimed kernel equality. Buchberger's module algorithm and elimination terminate over the polynomial ring.

Assign `deg e_u=delta_u`. The kernel is homogeneous because (G11.4) respects degrees. Standard module monomials therefore give a homogeneous vector-space basis of `M`. The threshold-cell argument proves (G11.5) exactly as in G-009. Every coefficient variable `Z_j` has positive balanced degree, so the first equation in (G11.5) bounds all nonnegative real coordinates; a negative remaining degree gives the empty set. This proves both positivity and boundedness.

The same finite data give the kernel and cokernel blocks: use the presentation of `B^H` with generators `P_H(q^u)`, the presentation of `B^K` with generators `P_K(q^u)`, and the explicit images (G11.2). Module kernels and quotients have homogeneous finite presentations over `Q[Z]`, so the same standard-monomial construction counts their multiplicities. This is a terminating determination for each specified pair `(m,n)`. The theorem does not give a uniform inequality proving all open parameter families of canonical injectivity or surjectivity.

In scheme language, (G11.3) is a coherent module on `Spec C`; (G11.4) is a finite presentation of its associated coherent sheaf, and the two idempotents are the precise averaging correspondences. Module Gröbner degeneration preserves the graded Hilbert function. Thus the positive lattice counts are transported through an explicit coherent-module presentation to the canonical map, rather than through its source and target dimensions alone.


# A complete small presentation of the projected flag algebra

## G-012. Four explicit polytopes for the full outer-degree-three family

The algebra `A_3` of G-009 has the multihomogeneous presentation
\[
\boxed{A_3=\mathbb Q[u,s,V,Z,d,W]/(d^2+4s^3+27u^2V,\ W^2-VZ).}
\tag{G12.1}
\]
The respective degrees `(n;lambda)` are
\[
\begin{array}{c|rrrrrr}
&u&s&V&Z&d&W\\\hline
n&1&2&4&2&3&3\\
\lambda&(3,0,0)&(4,2,0)&(6,6,0)&(2,2,2)&(6,3,0)&(4,4,1).
\end{array}
\tag{G12.2}
\]
Thus `a_(3,n)^lambda` is the sum over `epsilon,delta in {0,1}` of the number of nonnegative integral quadruples `(a,b,c,e)` satisfying
\[
\begin{aligned}
a+2b+4c+2e&=n-3\epsilon-3\delta,\\
3a+4b+6c+2e&=\lambda_1-6\epsilon-4\delta,\\
2b+6c+2e&=\lambda_2-3\epsilon-4\delta,\\
2e&=\lambda_3-\delta.
\end{aligned}
\tag{G12.3}
\]
These are four bounded rational polytopes for partitions of length at most three. Every coefficient with more than three parts is zero, by the balanced-weight Cauchy identification in T-001. The coefficients are the classical Thrall--Chen family. This presentation proves their direct realization as standard monomials in the precise normalizer-invariant flag algebra; it does not claim discovery of the coefficient family.

### Construction and proof

For a `3 by 3` matrix, write the first-column minors as `x_1,x_2,x_3`, the oriented two-column minors as `y_1=p_23,y_2=-p_13,y_3=p_12`, and the determinant as `z`. Then
\[
R_3=\mathbb Q[x_1,x_2,x_3,y_1,y_2,y_3,z]/(x_1y_1+x_2y_2+x_3y_3).
\tag{G12.4}
\]
The relation expands a determinant with two identical columns. These minors generate by G-009. The target has dimension six: on the open matrix chart where the first two leading minors and the determinant are nonzero, right-upper-unipotent Gaussian elimination leaves six independent parameters. The displayed relation is irreducible by Gauss's lemma, applied as a linear polynomial in `y` with relatively prime coefficients `x_i`. Its quotient is a domain of dimension six. The prime kernel has the same dimension and contains this principal prime, so they are equal. This proves (G12.4).

Set `t_i=x_i y_i`, `u=x_1x_2x_3`, and `v=y_1y_2y_3`. A monomial in `x,y` has balanced weight precisely when `a_i-b_i` is constant. A nonnegative difference factors out a power of `u`; a nonpositive difference factors out a power of `v`; the rest is a product of the `t_i`. The torus-invariant polynomial ring is consequently generated by `u,v,t_1,t_2,t_3,z` with sole relation `uv=t_1t_2t_3`, as also follows from the unique expressions containing `u` or `v` but not both. Exact torus weight extraction carries the flag relation to `sum t_i=0`. Therefore
\[
B_3=\mathbb Q[u,v,t_1,t_2,t_3,z]/(t_1+t_2+t_3,\ uv-t_1t_2t_3).
\tag{G12.5}
\]

A permutation sends `x_i` to `x_(sigma i)` and `y_i` to `sgn(sigma)y_(sigma i)`. It fixes `u`, negates each of `v,z` under an odd permutation, and sends `t_i` to `sgn(sigma)t_(sigma i)`. On the plane `sum t_i=0` put
\[
s=t_1t_2+t_1t_3+t_2t_3,\quad f=t_1t_2t_3,\quad
d=(t_1-t_2)(t_1-t_3)(t_2-t_3).
\]
The elements `s,d` are invariant under this twisted action, `f` has sign character, and
\[
d^2=-4s^3-27f^2.
\tag{G12.6}
\]
Its invariant and sign-isotypic polynomial subspaces are respectively
\[
\mathbb Q[s,d],\qquad f\mathbb Q[s,d].
\tag{G12.7}
\]
Indeed ordinary alternating-group invariants are `Q[s,f] directsum d Q[s,f]`: average under an ordinary transposition and divide the alternating part by the Vandermonde. Under a twisted transposition, `s,d` stay fixed and `f` changes sign. Taking even and odd parts in `f` and using (G12.6) proves (G12.7).

Adjoining the sign variables `v,z`, formula (G12.7) shows that before imposing `uv=f` the invariants are generated by
\[
u,s,d,\quad V=v^2,\quad W=vz,\quad Z=z^2,\quad fv,\quad fz.
\]
After that relation `fv=uV`, `fz=uW`, so `u,s,d,V,W,Z` generate `A_3`; exact averaging carries every quotient invariant to one of these images. Equations (G12.6) and `W^2=VZ` give (G12.1)'s relations. Hence its map to `A_3` is surjective.

To exclude further relations, `s,f` are algebraically independent on the two-dimensional `t` plane by the elementary symmetric-polynomial theorem. In the fraction field of (G12.5), take `v,z` independent and put `u=f/v`. Then `u,s,V=v^2,Z=z^2` are algebraically independent. In `F=Q(u,s,V,Z)`, the element `D=-4s^3-27u^2V` is nonsquare because its pole order at `s=infinity` is three. Both `VZ` and `D/(VZ)` are nonsquare by their odd valuation at `Z=0`. Their square classes are independent. Thus the actual `d,W` generate a degree-four extension of `F`, and `1,d,W,dW` are linearly independent over `F`.

The quotient in (G12.1) is free over `Q[u,s,V,Z]` with basis `1,d,W,dW`, since its two relations are monic quadratics in different variables. Their images are independent over `F`, hence over the polynomial subring. The presentation is therefore injective as well as surjective.

Its homogeneous basis is
\[
u^a s^b V^c Z^e d^\epsilon W^\delta,
\qquad a,b,c,e\ge0,\quad\epsilon,\delta\in\{0,1\}.
\]
Degrees give (G12.3), whose first equation bounds every nonnegative real coordinate. Equation (G9.8) identifies this dimension with the desired coefficient. This proves the four-polytope formula with the finite sign action evaluated explicitly.

The geometric construction is the affine flag cone, followed by the diagonal-torus and constant-`S_3` quotients. The monic relations supply the four-element free module and its positive monomial description. This is the precise algebraic-geometric realization of the outer-degree-three normalizer projection.


# Stable plethysm: explicit positive polytopes through six columns

Run `GCT_PLETH-20261121-theta`; GPT-6 Astra Pro; effort not surfaced. This supplements `theta_report.md`. The new work here makes the finite indexing and the actual polytope constraints explicit. The underlying stability theorem, the character reduction, the Littlewood identities and the Littlewood–Richardson rule are cited results, not claimed discoveries.

## T-010. Exact current stable family and its known four-column polytope

Write `lambda[N]=(N-|lambda|,lambda_1,lambda_2,...)` and

\[
c(\lambda)=\langle s_\lambda,H[H-1-h_1]\rangle,
\qquad H=\sum_{i\ge0}h_i.
\]

Sarkar, *Stability of plethysm coefficients and modified polynomial induction*, arXiv:2610.07929v2 (14 October 2026), Theorem D = Theorem 6.4, proves

\[
a_{n,m}^{\lambda[mn]}=c(\lambda)
\quad\bigl(m\ge\lambda_1,\ n\ge\lfloor(|\lambda|+\lambda_1)/2\rfloor,
\ mn-|\lambda|\ge\lambda_1\bigr).
\tag{T10.1}
\]

For `lambda=(4^u4,3^u3,2^u2,1^u1)`, his Theorem E = Theorem 7.3 identifies `c(lambda)` with the integer points `(t,epsilon_1,...,epsilon_4)` satisfying

\[
0\le\epsilon_i\le1,\quad t+\sum_i\epsilon_i\ge3,\quad
\epsilon_1-\epsilon_2=u_1,\quad \epsilon_3-\epsilon_4=u_3,
\quad\epsilon_2-\epsilon_3\le u_2,\quad t+\epsilon_4\le u_4.
\tag{T10.2}
\]

These are actual finite coefficients in the range (T10.1). The complete proofs of Theorems 6.4 and 7.3 were read and checked in this run. Source bytes were downloaded from `https://arxiv.org/src/2610.07929v2` and are retained in `sarkar/main.tex`.

Sarkar's Proposition 7.1 gives the exact character reduction, for `k>=lambda_1` and `V=C^k`,

\[
c(\lambda)=[S_{\lambda'}V:M_k],\qquad
M_k=\bigotimes_{i=2}^k F_i(\Lambda^iV),
\quad F_i=\operatorname{Sym}\ (i\text{ even}),\quad
F_i=\Lambda\ (i\text{ odd}).
\tag{T10.3}
\]

Here the bracket denotes multiplicity, `lambda'` denotes conjugation, and each full symmetric or exterior algebra is graded by ordinary scalar weight. Only total scalar degree `|lambda|` contributes. The source's Remark 7.5 notes the LR approach for five columns; T-012 and T-013 give full finite indexing and polytope constraints through six columns.

### The exact lambda-ring dictionary for (T10.3)

The involution `omega` of the symmetric-function ring satisfies `omega(p_r)=(-1)^{r-1}p_r` and `omega(s_lambda)=s_lambda'`. On a homogeneous input `h_i`, expansion in power sums gives

\[
\omega(p_r[h_i])=(-1)^{(r-1)i}p_r[e_i].
\]

Indeed, each term `p_{r alpha}` has sign `(-1)^{ri-length(alpha)}`, while the corresponding term of `p_r[e_i]` has sign `(-1)^{i-length(alpha)}`. Exponentiating `sum_r p_r/r` yields

\[
\omega(H[h_i])=H[e_i]\ (i\text{ even}),\qquad
\omega(H[h_i])=E[e_i]\ (i\text{ odd}),
\quad E=\sum_{j\ge0}e_j.
\tag{T10.4}
\]

The completed product `H[H-1-h_1]=product_{i>=2}H[h_i]` is well-defined degree by degree. Specialization to `k` variables sends `e_i` to zero for `i>k`, giving exactly (T10.3). On locally free sheaves this is the dictionary between symmetric powers of exterior powers and exterior powers of exterior powers in the representation Grothendieck ring. All factors of any given total scalar degree are finite locally free polynomial functors. The decomposition into characteristic-zero Schur summands takes place after base change to a characteristic-zero field; the polynomial operations themselves are defined over `Z`.

## T-011. An explicit Littlewood–Richardson polytope

For partitions `alpha,beta,gamma` of length at most `r`, padded by zeros, let `L_r(alpha,beta;gamma)` consist of real arrays `x_(i,j)`, `1<=i,j<=r`, with

\[
x_{ij}\ge0,\qquad x_{ij}=0\text{ for }i>j,
\tag{T11.1}
\]
\[
\sum_{i=1}^r x_{ij}=\gamma_j-\alpha_j,
\qquad \sum_{j=1}^r x_{ij}=\beta_i,
\tag{T11.2}
\]
\[
\alpha_j+\sum_{i=1}^{h}x_{ij}
\le\alpha_{j-1}+\sum_{i=1}^{h-1}x_{i,j-1}
\quad(2\le j\le r,\ 1\le h\le r),
\tag{T11.3}
\]
\[
\sum_{s=1}^{j-1}x_{i,s}\ge\sum_{s=1}^{j}x_{i+1,s}
\quad(1\le i<r,\ 1\le j\le r).
\tag{T11.4}
\]

Boundary partitions are required to have nonnegative entries and to be weakly decreasing. An invalid boundary gives the empty polytope. Its integer points count `c_{alpha,beta}^gamma`.

In the later gluing constructions, membership in `L_r` means precisely the displayed linear constraints also for real boundary variables. At a lattice point those boundary variables become integral partitions, so the same tableau bijection applies.

**Proof of the coordinate dictionary.** From an integer array fill row `j` of the skew diagram `gamma/alpha` with `x_(1,j)` ones, then `x_(2,j)` twos, and so on. The row and content conditions are (T11.2), and the filling is unique. In row `j`, the last box with entry at most `h` is at column `alpha_j+sum_(i<=h)x_(i,j)`. For strict increase down columns its upper neighbor must have entry at most `h-1`; (T11.3) states exactly that this last column lies within the removed upper-row prefix or within the upper-row prefix of entries at most `h-1`. Applying this for every `h` gives column strictness, and column strictness gives these inequalities.

Read each row from right to left, in order from top row to bottom row. For the ballot inequality comparing `i` and `i+1`, the largest deficit during row `j` occurs after all its `i+1` entries have been read and before any of its `i` entries have been read. The required inequality at that point is exactly (T11.4). Thus these conditions are equivalent to the lattice-word condition. The lattice-word condition also forces every entry in row `j` to be at most `j`, so the triangular zeros in (T11.1) impose no additional restriction. This is a bijection with Littlewood–Richardson tableaux. The classical LR rule gives the coefficient; see Macdonald, Chapter I, §9, or the representation-theoretic LR rule in the attached Landsberg source, §4, equations preceding `pieri`.

Each coordinate is bounded by the prescribed total content. Thus this is a bounded rational polytope, including the empty case.

## T-012. A fully explicit positive formula for stable tails of width five

Let `lambda_1<=5`, put `mu=lambda'`, padded to length five, and `N=|lambda|`. Define the following finite set `B_5` of pairs `(j,beta)`. Each listed `beta` has multiplicity one in `Lambda^j(Lambda^3 C^5)`:

| j | beta |
|---:|---|
|0|(0,0,0,0,0)|
|1|(1,1,1,0,0)|
|2|(2,2,1,1,0)|
|3|(3,3,1,1,1); (3,2,2,2,0)|
|4|(4,3,2,2,1); (3,3,3,3,0)|
|5|(5,3,3,2,2); (4,4,3,3,1)|
|6|(6,3,3,3,3); (5,4,4,3,2)|
|7|(6,4,4,4,3); (5,5,5,3,3)|
|8|(6,5,5,4,4)|
|9|(6,6,5,5,5)|
|10|(6,6,6,6,6)|

For `(j,beta) in B_5` and `epsilon in {0,1}`, define `Q_(lambda,beta,epsilon)` using real variables `P,Q,q`, a weakly decreasing nonnegative five-tuple `nu`, and two arrays `x,y` as follows:

\[
P\ge Q\ge0,\quad q\ge0,\qquad
\alpha=(P,P,Q,Q,0),\quad \eta=(q,q,q,q,0),\quad
\gamma=\mu-(\epsilon^5)\ge0,
\tag{T12.1}
\]
\[
x\in L_5(\alpha,\beta;\nu),\qquad
y\in L_5(\nu,\eta;\gamma),
\tag{T12.2}
\]
\[
2(P+Q)+3j+4q+5\epsilon=N.
\tag{T12.3}
\]

Every condition is linear with integer coefficients. The target boundary condition in (T12.1) makes the piece empty when needed. Then

\[
\boxed{c(\lambda)=
\sum_{(j,\beta)\in B_5}\ \sum_{\epsilon=0}^{1}
\#\bigl(Q_{\lambda,\beta,\epsilon}\cap\mathbb Z^{58}\bigr).}
\tag{T12.4}
\]

The ambient dimension counts three scalar parameters, five intermediate coordinates, and two five-by-five arrays; redundant triangular zeros can reduce it. The formula is a finite sum of 32 bounded rational polytopes, with tags retaining disjointness. It makes no homogeneous-dilation assertion.

**Proof.** By (T10.3), the required module is

\[
M_5=\operatorname{Sym}(\Lambda^2V)\otimes\Lambda(\Lambda^3V)
\otimes\operatorname{Sym}(\Lambda^4V)\otimes\Lambda(\Lambda^5V).
\]

The classical Littlewood decomposition of `Sym(Lambda^2 V)` has all even-column partitions, each once; in rank five these are `(P,P,Q,Q,0)`. This follows as well by applying (T10.4) to the symmetric-matrix identity T-007. The natural perfect wedge pairing gives `Lambda^4 V=V^* tensor det V`; hence

\[
\operatorname{Sym}^q(\Lambda^4V)
=\operatorname{Sym}^q(V^*)\otimes\det^q
=S_{(q,q,q,q,0)}V.
\]

Finally `Lambda(Lambda^5 V)=1+det V`. The complete finite decomposition of the second factor is the displayed `B_5`; the exact finite-character certificate is described under T-013 below and in `few_columns.py`.

The multiplicity of `S_mu V` is therefore

\[
\sum_{(j,\beta),\epsilon,P\ge Q\ge0,q\ge0,\nu}
c_{\alpha,\beta}^{\nu}c_{\nu,\eta}^{\mu-(\epsilon^5)}.
\]

Every summand has scalar degree `2(P+Q)+3j+4q+5epsilon`. Only degree `N` contributes. Apply the integer-point bijection T-011 twice, retaining `P,Q,q,nu` as coordinates rather than summing them externally. This proves (T12.4). Equation (T12.3) bounds the three scalar parameters; the two LR row/content conditions bound `nu,x,y` by `N`. Thus every piece is bounded.

## T-013. A fully explicit positive formula for stable tails of width six

Let `lambda_1<=6`, put `mu=lambda'` padded to length six, and `N=|lambda|`. Let `B_6` be the complete 156-row list in `EXTERIOR_CUBE_RANK_6.tsv`. Its pair `(j,beta)` denotes one copy of `S_beta C^6` in `Lambda^j(Lambda^3 C^6)`; every listed multiplicity is one, `0<=j<=20`, and `|beta|=3j`.

For `(j,beta) in B_6` and `q in {0,...,6}`, set

\[
\theta(q)=(q^{6-q},(q-1)^q).
\tag{T13.1}
\]

For `q=0` the second block has length zero and `theta(0)=(0^6)`. Define `R_(lambda,beta,q)` by variables `P,Q,R,a,b,c,t`, intermediate partitions `nu,xi` of length at most six, and three six-by-six arrays `x,y,z` satisfying

\[
P\ge Q\ge R\ge0,\quad a\ge b\ge c\ge0,\quad t\ge0,
\tag{T13.2}
\]
\[
\alpha=(P,P,Q,Q,R,R),\qquad
\eta=(a+b,a+b,a+c,a+c,b+c,b+c),\qquad
\gamma=\mu-(t^6)\ge0,
\tag{T13.3}
\]
\[
x\in L_6(\alpha,\beta;\nu),\qquad
y\in L_6(\nu,\eta;\xi),\qquad
z\in L_6(\xi,\theta(q);\gamma),
\tag{T13.4}
\]
\[
2(P+Q+R)+3j+4(a+b+c)+5q+6t=N.
\tag{T13.5}
\]

Then

\[
\boxed{c(\lambda)=
\sum_{(j,\beta)\in B_6}\ \sum_{q=0}^{6}
\#\bigl(R_{\lambda,\beta,q}\cap\mathbb Z^{127}\bigr).}
\tag{T13.6}
\]

There are 1092 tagged bounded rational polytopes in this formula. There are seven scalar variables, twelve intermediate-partition coordinates, and 108 array coordinates, totaling 127. Empty pieces are allowed. Thus the finite coefficient in (T10.1) has an explicit positive lattice-point formula for every tail of width at most six.

**Proof of the representation formula.** The exact factorization is

\[
M_6=\operatorname{Sym}(\Lambda^2V)\otimes\Lambda(\Lambda^3V)
\otimes\operatorname{Sym}(\Lambda^4V)\otimes\Lambda(\Lambda^5V)
\otimes\operatorname{Sym}(\Lambda^6V).
\]

The first factor has partitions `alpha=(P,P,Q,Q,R,R)`, each once. The perfect wedge pairing `Lambda^4 V=Lambda^2 V^* tensor det V` sends the summand `(a,a,b,b,c,c)` in symmetric degree `d=a+b+c` to its dual tensored with `det^d`. Its highest weight is

\[
(d-c,d-c,d-b,d-b,d-a,d-a)
=(a+b,a+b,a+c,a+c,b+c,b+c)=\eta.
\]

This proves the asserted indexing of the third factor with no omitted determinant shift. The pairing `Lambda^5 V=V^* tensor det V` gives

\[
\Lambda^q(\Lambda^5V)=\Lambda^q(V^*)\otimes\det^q
=S_{\theta(q)}V,\qquad 0\le q\le6.
\]

The last factor has summands `det^t`, `t>=0`. The second factor is the fixed table `B_6`. Iterating the LR rule three times yields

\[
\sum_{(j,\beta),q,P,Q,R,a,b,c,t,\nu,\xi}
c_{\alpha,\beta}^{\nu}
c_{\nu,\eta}^{\xi}
c_{\xi,\theta(q)}^{\mu-(t^6)}.
\]

The scalar degrees of the five factors are respectively
`2(P+Q+R),3j,4(a+b+c),5q,6t`. Keeping degree `N` gives (T13.5). Gluing the three integer-point descriptions from T-011 along the displayed intermediate partitions gives (T13.6). Every scalar variable in (T13.2) is bounded by (T13.5), every intermediate partition has size at most `N`, and each nonnegative array entry is bounded by a row or content sum at most `N`. This proves boundedness as well as finiteness of the formula.

### Complete finite certificate for `B_5` and `B_6`

For `r=5,6` the exact torus character of the entire finite exterior algebra is

\[
C_r(t;x)=\prod_{I\subset\{1,\ldots,r\},\ |I|=3}
\left(1+t\prod_{i\in I}x_i\right).
\tag{T13.7}
\]

Let `rho=(r-1,...,0)` and write `M_j(w)` for the coefficient of `t^j x^w` in this finite product, with zero for unsupported weights. The Weyl alternant identity gives the exact multiplicity

\[
b_{j,\beta}=\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
M_j(\beta+\rho-\sigma\rho).
\tag{T13.8}
\]

The integer program `few_columns.py` expands (T13.7) without floating point arithmetic, evaluates (T13.8) on every dominant weight in its support, and writes the complete tables. Every irreducible highest weight is a dominant weight in that support, so the candidate set is exhaustive. The resulting tables have respectively 16 and 156 entries, all multiplicity one. As a separate check, the program reconstructs the character of each listed Schur module by recursively enumerating interlacing restrictions and compares every monomial in every exterior degree with (T13.7). Both complete comparisons pass. Dimension totals are `2^10=1024` and `2^20=1048576`.

This is a finite exact computation certificate, together with its mathematical extraction formula and an independent character reconstruction. It is not labeled a proof-assistant certificate. The table is fixed data independent of the user-varying partition `lambda`. Once the table is supplied, formulas (T12.4) and (T13.6) use only counts of integer points in explicitly stated bounded polytopes.

## T-014. Stable nonvanishing in an explicit family of every width

Let `lambda` range over the partitions with no part equal to one, with arbitrary multiplicities of even parts, and with multiplicity at most one for each odd part. Then

\[
\boxed{c(\lambda)\ge1.}
\tag{T14.1}
\]

The empty partition has `c(empty)=1`, the constant term of the completed character, and is included separately from the nonempty case below.

Consequently, for the exact parameter range in (T10.1),

\[
a_{n,m}^{\lambda[mn]}\ge1.
\tag{T14.2}
\]

**Proof for nonempty `lambda`.** Put `k=lambda_1` and `u_i=m_i(lambda)`. For even `i`, the pure power of the highest wedge vector
`(e_1 wedge ... wedge e_i)^{u_i}` is a nonzero highest vector of weight `u_i omega_i` in `Sym^{u_i}(Lambda^i V)`. For odd `i`, the permitted values `u_i=0,1` select respectively the scalar vector or the highest wedge vector in `Lambda^{u_i}(Lambda^i V)`. Their tensor product is nonzero and is killed by all positive-root operators. Its highest weight is

\[
\sum_{i=2}^k u_i\omega_i=\lambda',
\]

because the `j`th coordinate equals `sum_(i>=j)u_i`, the height of the `j`th column of `lambda`. It lies in scalar degree `sum i u_i=|lambda|`. Complete reducibility in characteristic zero gives a constituent `S_lambda' V` of `M_k`. Equation (T10.3) proves (T14.1), and (T10.1) transports it to (T14.2).

This explicitly includes all partitions with even parts and, for example, `(6^u)`, `(4^a,3,2^b)`, and `(8^a,7,6^b,5,4^c,3,2^d)`. It is a sufficient support family, with no claim that it exhausts the stable support.

## Subsequent positive counts and the smaller direct-formula problem

The stable coefficients of tails of width at most six have the small explicit polytope formulas T-012 and T-013; T-014 proves support in a specified family of every width. Formula (T10.3) remains exact at arbitrary width. Subsequent statements T-016–T-020 in `work/theta/width7/width7_report.md` give an exact three-variable positive polytope for the constituents of shape `(A,B^5,C)` in `Sym^d(Lambda^4 C^7)`, as well as further stable nonvanishing families and a precise boundary-valuation formula for other weights.

The general existence question has also advanced: G-009–G-010 in `work/root/invariant_polytope_report.md` and `work/root/general_polytope_extensions.md` give terminating finite-presentation and standard-monomial polytope constructions for all symmetric and general Schur plethysm coefficients, including the unstabilized coefficients. G-011 does the same for the actual canonical-map image, kernel, and cokernel modules. G-012 supplies four direct polytopes for the full outer-degree-three family. T-024–T-028 in `work/theta/end_node/` further give a uniform polynomial-size polytope and an arithmetic support test for every outer Schur functor with inner symmetric power and output shape `(alpha,beta^(m-2),gamma)`, with a direct toric algebra degeneration for symmetric outer powers. Thus the current narrower task is to replace large parameter-dependent Reynolds enumeration and elimination by small, efficiently specified presentations or polyhedral formulas outside these direct families. The width-seven valuation outside T-018 is one concrete calculation for that purpose; it is not a remaining obstruction to the existence of a terminating positive count.


# Width seven: metric covariants, exact end-node coefficients, and the extension valuation

This report continues T-010–T-014. It supplies a complete positive formula for a three-parameter family inside the first remaining symmetric-power factor, together with further stable nonvanishing families. The constructions and proofs are unconditional. No global novelty claim is made.

All representations are over \(\mathbf C\). Put \(V=\mathbf C^7\), \(G=GL(V)\),
\[
R=\operatorname{Sym}(\Lambda^3V)=\mathbf C[\Lambda^3V^*],
\qquad S=\operatorname{Sym}(\Lambda^4V).
\]
The coordinate-ring action is \((gf)(\phi)=f(g^{-1}\phi)\). Thus \(R_d\) has positive central degree \(3d\). Highest weights are decreasing integral seven-tuples; a superscript on an entry means repetition.

For integers \(A\ge B\ge C\ge0\), \(d\ge0\), \(A+5B+C=4d\), define
\[
\mathcal P(A,B,C)=\left\{(k,\ell,j)\in\mathbf R_{\ge0}^3:
\begin{array}{rcl}
2k+4\ell+4j&=&A,\\
2k+2\ell+4j&=&B,\\
2\ell+4j&=&C.
\end{array}\right\}.
\]
The exact answer proved below is
\[
\boxed{[S_{(A,B^5,C)}V:S_d]
=\#(\mathcal P(A,B,C)\cap\mathbf Z^3).}
\tag{W7.1}
\]
This bounded polytope is empty or a point. Its unique possible point is
\[
k=(B-C)/2,\qquad \ell=(A-B)/2,\qquad j=(B+C-A)/4.
\tag{W7.2}
\]

## T-016. Cubic metric and polynomial quartic cometric

### Precisely located background

The following classical input is used.

1. A generic alternating three-form on \(V\) has stabilizer \(H=\mu_3\times G_2\subset GL(V)\), with \(G_2\subset SL(V)\) acting through its irreducible seven-dimensional representation. Its orbit \(O\) is open. The finite central factor is retained. An exact primary locator is Dave Anderson, *Chern class formulas for \(G_2\) Schubert loci*, Appendix A, Proposition A.1 and Corollary A.2, printed page 29: https://people.math.osu.edu/anderson.2804/papers/g2-chern.pdf

2. The complement of \(O\) is one irreducible hypersurface with degree-seven equation. The cubic metric below is nondegenerate exactly on \(O\), and has rank four on the dense codimension-one boundary orbit. Laurent Manivel, *Prehomogeneous spaces and projective geometry*, Example 4.3.3, printed pages 59–60, and Example 4.4.2, printed pages 61–62, give the orbit representatives, rank data, boundary diagram, and degree-seven invariant. Proposition 3.1.4, printed page 44, identifies fundamental relative invariants with irreducible hypersurface equations. The metric also appears in §5.1.2, printed page 68: https://manivel.perso.math.cnrs.fr/trento2012.pdf

Here “metric rank” always means the rank of the explicitly defined seven-by-seven matrix; the source's two rank labels need not be adopted. The classification and generic-stabilizer statements are cited background, not reproved as new results.

Choose a volume vector \(\tau\in\det V\), with dual volume form \(\Omega\). Define
\[
B_\phi(u,v)\Omega=(\iota_u\phi)\wedge(\iota_v\phi)\wedge\phi.
\tag{W7.3}
\]
The contracted forms have degree two, so this is symmetric in \(u,v\), and its coefficients are cubic in \(\phi\). Intrinsically its values lie in \(\operatorname{Sym}^2V^*\otimes\det V^*\). The actual coefficient morphism is
\[
F_B:\operatorname{Sym}^2V\otimes\det V\longrightarrow R_3,\qquad
F_B(uv\otimes\tau)(\phi)
=\langle(\iota_u\phi)\wedge(\iota_v\phi)\wedge\phi,\tau\rangle.
\tag{W7.4}
\]
Equivariance follows by pulling back the forms and moving \(g\) across the evaluation pairing. This fixes the determinant twist. For \(\phi=e^{123}+e^{145}+e^{167}\), evaluation at \(u=v=e_1\) gives \(6\Omega\), so the map is nonzero. Its source is irreducible, hence it is injective. In particular
\(b=F_B(e_1^2\otimes\tau)\ne0\) is a highest vector of weight \((3,1^6)\).

Let \(\Delta\) be an irreducible equation of the boundary. Its degree is seven and its character for the stated action is
\[
\Delta\in R_7,\qquad g\Delta=(\det g)^3\Delta.
\tag{W7.5}
\]
Indeed every character is a determinant power, and scalar matrices act on \(R_7\) by their twenty-first power.

Writing \(B=(B_{ij})\), its coefficient transformation is
\[
gB=(\det g)\,g^{\mathsf T}Bg.
\]
Thus \(\det B\) has degree twenty-one and character \(\det^9\). Its zero locus is exactly the boundary; unique factorization gives \(\det B=c_0\Delta^3\), \(c_0\ne0\). Rescale \(\Delta\) over \(\mathbf C\) so that \(c_0=1\).

Every entry of \(\operatorname{adj}B\) is divisible by \(\Delta^2\). To prove this, localize the polynomial ring \(R\) at the height-one prime \((\Delta)\), obtaining a discrete valuation ring. Modulo its maximal ideal the metric has rank four. Invertible row and column operations reduce its first four rows and columns to an invertible block; the entries of the remaining three-by-three Schur-complement block are divisible by \(\Delta\). Every six-by-six minor therefore has valuation at least two. Since the minors are polynomials and \(R\) is a unique factorization domain, this is divisibility by \(\Delta^2\) in \(R\).

Consequently
\[
C=\operatorname{adj}B/\Delta^2
\tag{W7.6}
\]
is a matrix of quartic polynomials and
\[
BC=CB=\Delta I_7.
\tag{W7.7}
\]
The adjugate transformation gives
\[
gC=(\det g)^2g^{-1}Cg^{-\mathsf T}.
\]
Its coefficient space is the image of the equivariant morphism
\[
F_C:\operatorname{Sym}^2V^*\otimes\det^2V\longrightarrow R_4.
\tag{W7.8}
\]
The matrix is invertible on \(O\), so this map is nonzero; its irreducible source makes it injective. Choose a nonzero highest vector \(c\) in its image. Its weight is \((2^6,0)\).

Neither \(b\) nor \(c\) is divisible by the irreducible \(\Delta\), since their degrees are three and four. Hence
\[
v_\Delta(b^kc^\ell\Delta^j)=j
\quad(k,\ell\ge0,\ j\in\mathbf Z).
\tag{W7.9}
\]
This is the exact extension test.

The symbolic receipt METRIC_PATH_CHECK.txt uses
\(\phi(t)=e^{123}+e^{145}+t e^{167}+e^{246}+e^{357}\).
It obtains metric ranks four at \(t=0\) and seven at \(t=1\), determinant \(-4374t^3\), and adjugate order at least two, attained by an entry. This finite check supplements the global divisibility proof.

## T-017. The required \(G_2\)-invariant spaces

Write \(\omega_1\) for the highest weight of the seven-dimensional \(G_2\)-module. Then
\[
\operatorname{Sym}^mV|_{G_2}
=\bigoplus_{r=0}^{\lfloor m/2\rfloor}V_{(m-2r)\omega_1}
\quad(m\ge0).
\tag{W7.10}
\]
Here is a proof of precisely this assertion. The nondegenerate invariant quadratic form gives the usual contraction
\(\operatorname{Sym}^mV\to\operatorname{Sym}^{m-2}V\), and the harmonic decomposition
\(\operatorname{Sym}^mV=H_m\oplus q\operatorname{Sym}^{m-2}V\) in characteristic zero. A highest vector \(v\) is isotropic because \(v^2\) has nonzero weight \(2\omega_1\), so \(v^m\in H_m\). It generates \(V_{m\omega_1}\). The Weyl formula for the six positive roots of \(G_2\) gives
\[
\dim V_{m\omega_1}
=\frac{(m+1)(m+2)(m+3)(m+4)(2m+5)}{120}
=\binom{m+6}{6}-\binom{m+4}{6}
=\dim H_m.
\]
Binomial terms with top below six are zero. Thus \(H_m=V_{m\omega_1}\), and induction proves (W7.10). Complete reducibility, harmonic decomposition, and the Weyl formula are the standard background theorems used here.

For \(a,b\ge0\), let \(L_{a,b}\) be the irreducible \(SL_7\)-module with highest weight \(a\omega_1+b\omega_6\), now using the \(SL_7\) fundamental weights. Then
\[
\boxed{\dim L_{a,b}^{G_2}
=\begin{cases}1,&a,b\text{ both even},\\0,&\text{otherwise}.\end{cases}}
\tag{W7.11}
\]
To prove it, use the exact determinant identity
\[
\operatorname{Sym}^aV\otimes\operatorname{Sym}^bV^*
=\operatorname{Sym}^aV\otimes S_{(b^6)}V\otimes\det^{-b}V.
\]
Pieri's horizontal-strip rule, applied to the six-row rectangle, gives
\[
\operatorname{Sym}^aV\otimes\operatorname{Sym}^bV^*
=\bigoplus_{i=0}^{\min(a,b)}L_{a-i,b-i}
\tag{W7.12}
\]
after restriction to \(SL_7\). This includes \(a=0\) or \(b=0\).
By (W7.10) and Schur's lemma the left side has \(G_2\)-invariant dimension
\[
H(a,b)=\#\{r:0\le r\le\min(a,b),\ r\equiv a\equiv b\pmod2\}.
\]
Set \(H(a,b)=0\) if either argument is negative. Subtracting (W7.12) at arguments \(a-1,b-1\) gives
\(\dim L_{a,b}^{G_2}=H(a,b)-H(a-1,b-1)\).
Different parities give two zero terms; both odd give equal terms; both even give difference one. The boundary cases follow from the zero convention. This proves (W7.11).

The independent rectangular-cases checker verified the Pieri calculation, the difference including all boundary cases, and the harmonic dimension argument.


## T-018. Exact polynomial sector and positive polytope formula

For \(a,b\ge0\) and \(s\in\mathbf Z\), set
\[
\gamma=(a+b+s,(b+s)^5,s).
\tag{W7.13}
\]
These are exactly the dominant integral seven-tuples with equal second through sixth entries. They label rational \(GL_7\)-representations. The central \(\mu_3\) acts by the character determined by
\(|\gamma|=a+6b+7s\).

Evaluation at the basepoint of \(O=G/H\) gives the actual isomorphism
\[
\operatorname{Hom}_G(S_\gamma V,\mathbf C[O])
\simeq((S_\gamma V)^*)^H.
\tag{W7.14}
\]
An \(H\)-invariant functional \(\ell\) corresponds explicitly to
\[
v\longmapsto f_{\ell,v},\qquad
f_{\ell,v}(gH)=\ell(g^{-1}v).
\]
Conversely evaluate an equivariant map at the identity coset. These operations are inverse. Regularity is the matrix-coefficient construction on \(G\) and its descent to the homogeneous space \(O=G/H\).

By (W7.11), this space has dimension one exactly when
\[
a=2k,\quad b=2\ell,\quad s=k+3j
\quad(k,\ell\ge0,\ j\in\mathbf Z),
\tag{W7.15}
\]
and otherwise it has dimension zero. The congruence on \(s\) is exactly the \(\mu_3\)-invariance condition; no determinant character has been dropped.

For (W7.15), the nonzero rational highest vector \(b^kc^\ell\Delta^j\) has the required weight and degree
\[
d=3k+4\ell+7j,
\tag{W7.16}
\]
\[
\gamma=(3k+2\ell+3j,(k+2\ell+3j)^5,k+3j).
\tag{W7.17}
\]
It is regular on \(O\) and spans its one-dimensional highest-vector space. It extends to \(R\) exactly when \(j\ge0\), by (W7.9). Indeed
\(\mathbf C[O]=R[\Delta^{-1}]\), and a fraction with only this possible denominator is polynomial exactly when its \(\Delta\)-valuation is nonnegative.

It follows that the subalgebra of \(R^U\) spanned by the highest weights with equal second through sixth entries is exactly
\[
\boxed{R_{\mathrm{ends}}=\mathbf C[b,c,\Delta].}
\tag{W7.18}
\]
The three generators are algebraically independent: their weights in (W7.17) determine the three exponents uniquely, so distinct monomials have distinct torus weights. Their nonzero products are independent. Thus (W7.18) identifies the algebra, its actual generators, and its positive monomial basis.

Now use the degreewise exterior-duality isomorphism
\[
\Lambda^4V\simeq\Lambda^3V^*\otimes\det V,
\qquad
S_d\simeq R_d^*\otimes\det^dV.
\tag{W7.19}
\]
A constituent of highest weight \(\gamma\) goes to highest weight
\[
\eta_i=d-\gamma_{8-i}\quad(1\le i\le7).
\tag{W7.20}
\]
This identifies multiplicities with their determinant shifts. Equations (W7.16)–(W7.17) give
\[
\eta=(2k+4\ell+4j,(2k+2\ell+4j)^5,2\ell+4j).
\tag{W7.21}
\]
Conversely \((A,B^5,C)\) determines precisely the parameters in (W7.2). If parity or the central congruence fails, (W7.14)–(W7.15) give zero; if an extension parameter is negative, the polynomial constituent is absent. If all three are nonnegative integers, (W7.17) is a polynomial constituent with multiplicity one, and (W7.19) supplies the target. This proves (W7.1), including all zero coefficients.

The slice \(\ell=0\) says
\[
[S_{(A^6,C)}V:S_d]
=\begin{cases}1,&A\text{ even},\\0,&A\text{ odd},\end{cases}
\qquad 6A+C=4d,\quad A\ge C\ge0.
\]
The degree condition forces \(C\equiv0\pmod4\) in the nonzero case. The slice \(k=0\) is also governed by the same explicit polytope, including the triangle condition \(A\le2B\).

### A precise obstruction to discarding the extension valuation

For \(k=3,\ell=2,j=-1\), (W7.17) gives
\[
d=10,\qquad \gamma=(10,4^5,0).
\]
The function \(b^3c^2/\Delta\) is regular on \(G/H\), has this polynomial dominant weight, and has a genuine simple pole on the boundary. Therefore
\[
\dim((S_{(10,4^5,0)}V)^*)^H=1,\qquad
[S_{(10,4^5,0)}V:R_{10}]=0.
\tag{W7.22}
\]
Every entry of \(\gamma\) lies between zero and ten and \(|\gamma|=30\), so it also satisfies the elementary torus weight-support bounds for \(R_{10}\). The failure of this transfer is proved by the localization morphism and its valuation.

Duality gives the corresponding zero
\([S_{(10,6^5,0)}V:S_{10}]=0\).
The possible polytope point is \((3,2,-1)\), displaying the failed inequality.

The exact verifier check_width7.py computes the character of \(R_d\) by Newton's recurrence and extracts Schur multiplicities by the Weyl alternant. Every end-node partition in degrees zero through ten—seventy-five partitions, including (W7.22)—agrees with (W7.18). END_NODE_CHECK.tsv is the complete receipt. This is a finite verification supplementary to the infinite proof.

## T-019. Stable positive families

T-010 realizes the stable coefficient \(c_\lambda=\langle s_\lambda,H[H-1-h_1]\rangle\), for width at most seven, as the multiplicity of \(S_{\lambda'}V\) in scalar degree \(|\lambda|\) of
\[
\mathcal M_7=
\operatorname{Sym}(\Lambda^2V)\otimes
\Lambda(\Lambda^3V)\otimes
\operatorname{Sym}(\Lambda^4V)\otimes
\Lambda(\Lambda^5V)\otimes
\operatorname{Sym}(\Lambda^6V)\otimes
\Lambda(\Lambda^7V).
\]
Taking constants in every factor other than \(\operatorname{Sym}(\Lambda^4V)\), (W7.21) yields
\[
\boxed{c_{(7^{\,2\ell+4j},\,6^{\,2k},\,1^{\,2\ell})}\ge1
\quad(k,\ell,j\ge0).}
\tag{W7.23}
\]
The empty partition has coefficient one. This is a stable multiplicity bound; (W7.1) computes exactly the contribution of the specified symmetric-power factor.

Differentiating \(\Delta\) produces the nonzero equivariant map
\[
\Lambda^3V^*\otimes\mathbf C\Delta\longrightarrow R_6.
\tag{W7.24}
\]
It is nonzero by Euler's identity \(7\Delta=\sum x_i\partial_i\Delta\); its irreducible source makes it injective. Its highest weight is \((3^4,2^3)\). Via (W7.19) it gives a nonzero highest vector \(g\in S_6\) of weight \((4^3,3^4)\). Hence
\[
c_{(7^3,3)}\ge1,\qquad
c_{(7^{\,4j+3h},3^h)}\ge1\quad(j,h\ge0).
\tag{W7.25}
\]
For the second assertion choose a determinant vector in \(S_7\), of weight \((4^7)\), supplied from \(\Delta\) by (W7.19), and multiply its \(j\)-th power by \(g^h\) inside the polynomial domain \(S\). Degreewise duality is used to produce individual constituents; all multiplication occurs in the stated target algebra.

A more flexible sufficient family is
\[
\boxed{\begin{split}
\lambda={}&(7^{\,2\ell+4j+3h+\epsilon_7},
6^{\,u_6},5^{\,\epsilon_5},4^{\,u_4},
3^{\,h+\epsilon_3},2^{\,u_2},1^{\,2\ell}),\\
&c_\lambda\ge1,
\end{split}}
\tag{W7.26}
\]
for \(\ell,j,h,u_2,u_4,u_6\ge0\) and
\(\epsilon_3,\epsilon_5,\epsilon_7\in\{0,1\}\).

For a complete proof, inside the single domain \(S\) multiply the cometric-derived highest vector of weight \((4,2^6)\) to power \(\ell\), the determinant vector to power \(j\), the differentiated vector \(g\) to power \(h\), and the pure highest vector \(e_1\wedge e_2\wedge e_3\wedge e_4\) to power \(u_4\). The result is nonzero and highest. In the symmetric factors for exterior degrees two and six, take pure highest vectors to powers \(u_2,u_6\). In each of the exterior-algebra factors of exterior degree three, five, and seven, take either its scalar or its degree-one highest vector according to \(\epsilon_i\). The tensor is nonzero, highest of weight \(\lambda'\), and has scalar degree \(|\lambda|\). This proves (W7.26). No power greater than one of a single vector is used in an exterior algebra.

Every stable conclusion transports to the finite coefficient
\(a_{n,m}^{\lambda[mn]}\) in T-010's exact range
\[
m\ge\lambda_1,\qquad
n\ge\left\lfloor\frac{|\lambda|+\lambda_1}{2}\right\rfloor,
\qquad mn-|\lambda|\ge\lambda_1.
\]
These bounds are Sarkar, arXiv:2610.07929v2, Theorem 6.4. This report supplies the stated constituents of his stable module.


## T-020. The remaining data: a finite-dimensional valuation filtration

For each dominant integral weight \(\gamma\), fix a highest vector \(v_\gamma\) of the rational irreducible \(L_\gamma\) and define
\[
E_\gamma=(L_\gamma^*)^H,\qquad
F_{\gamma,\ge q}=
\{\ell\in E_\gamma:
v_\Delta(gH\mapsto\ell(g^{-1}v_\gamma))\ge q\}.
\tag{W7.27}
\]
The zero function has infinite valuation. This is a vector-space filtration, since the valuation of a sum is at least the smaller summand valuation. The exact equality is
\[
[L_\gamma:R]=\dim F_{\gamma,\ge0}.
\tag{W7.28}
\]
The central character determines its degree whenever it occurs. Equation (W7.28) follows from (W7.14) and
\(R=\{f\in R[\Delta^{-1}]:v_\Delta(f)\ge0\}\). If the highest matrix coefficient is in \(R\), its entire irreducible span is in \(R\), because \(R\) is \(G\)-stable. Thus testing this coefficient proves the assertion for the full equivariant map, not only one function.

Multiplication by \(\Delta^t\) identifies the open-orbit highest spaces at \(\gamma\) and \(\gamma+(3t)^7\), and increases their valuations by \(t\). Thus the determinant-shift coefficients are precisely the dimensions of steps in this filtration. T-018 calculates the entire filtration for the end-node sector. Elsewhere, computing only the \(G_2\times\mu_3\)-invariant dimensions leaves the extension condition unevaluated. Example (W7.22) proves that replacing the filtered dimension by the full invariant dimension can change the coefficient.

There is a precise published limitation on copying the rank-six free-generator formula to all weights. Michel Brion, *Invariants d'un sous-groupe unipotent maximal d'un groupe semi-simple*, Annales de l'Institut Fourier 33(1) (1983), Theorem 3, printed pages 12–13, and case \((A_6,\omega_3)\) of §III.1, printed page 14, prove that the full algebra \(R^U\) is not polynomial:
https://www.numdam.org/item/10.5802/aif.902.pdf

The cited case gives a concrete contradiction. Its quotient dimension is at least \(35-21=14\). There is one generator in degree one, one additional generator in degree two, and further generators have degree at least three, using
\(\operatorname{Sym}^2(\Lambda^3V)=S_{(2^3)}V\oplus S_{(2,1^4)}V\).
Polynomiality would force the sum of generator degrees to be at least \(1+2+12\cdot3=39\). Brion's Corollary 2 to Theorem 2 bounds this sum by \(35\) in the polynomial case. This excludes that particular free-polynomial-algebra formula for all weights. It permits finite presentations, standard monomial bases, and positive polytope sums. Formula (W7.18) supplies a polynomial sector with its exact multiplicity interpretation.

A concrete next orbit-based computation is the filtration (W7.27) outside this sector. Rota and Stein's nine symbolic covariants, printed page 847 of *Symbolic method in invariant theory*, PNAS 83 (1986), 844–847, give explicit tensor-valued candidates:
https://pmc.ncbi.nlm.nih.gov/articles/PMC322966/
Their tensor operations require conversion to a presentation or valuation basis before serving as a basis of all \(R^U\). No assertion that these nine diagrams are nine algebraically independent generators of \(R^U\) is used.

## Verification status and artifacts

The complete arguments T-016–T-020 were reread with attention to coordinate-ring duals, the finite stabilizer, scalar degrees, both determinant twists, adjugate divisibility, all zero-boundary cases in (W7.11), and the use of degreewise duality versus multiplication in the target algebra. No gap was found in the stated conclusions.

The orbit classification and generic-stabilizer identification are cited established inputs. Their statements and relevant source sections were read; their classification proofs were not independently reproduced. The complete extension and coefficient arguments used here are supplied above. The finite checker uses exact integers and symbolic one-variable matrix calculations; it is not a proof-assistant certificate.

Accompanying files:

- check_width7.py: Newton/Weyl verification and cubic-metric path calculation.
- END_NODE_CHECK.tsv: all seventy-five end-node partitions through symmetric degree ten.
- METRIC_PATH_CHECK.txt: exact metric matrix, determinant, and adjugate orders.
- The parent CHECK_EVENTS.tsv records actual proof-reading and computation events.

One initial symbolic-check run included an unjustified expected normalization scalar for \(\det B\). The computed scalar was different; the check was corrected to test the claimed invariant statement, namely nonzero determinant order exactly three. All final tests passed. No plethysm coefficient prediction failed.





# An explicit toric presentation for the two-row sector of outer degree four

## Scope and prior result

This report gives a small presentation and a finite SAGBI basis for the subalgebra of G-009's \(A_4\) with output partitions of length at most two. It yields two fixed, four-variable polytopes for all coefficients \(a_{4,n}^{(4n-k,k)}\). The binary-quartic covariant algebra and this coefficient family are classical; the point here is the complete explicit normalizer-algebra morphism, the finite toric degeneration, and the directly verified lattice count. No discovery of the classical presentation or coefficient family is claimed.

Primary historical source: J. H. Grace and A. Young, *The Algebra of Invariants* (1903), §89, printed pp. 91–94, proves generation of the quartic covariants by five forms; §93, printed pp. 97–98, derives their syzygy. The source text was read in this run:
https://archive.org/download/algebraofinvaria00graciala/algebraofinvaria00graciala_djvu.txt
A scan is available at:
https://commons.wikimedia.org/wiki/File:The_algebra_of_invariants_(IA_algebraofinvaria00graciala).pdf
The coordinate normalization below is checked directly and does not require translating the historical symbolic normalization.

## T-021. Exact normalizer-algebra morphism

Let \(F=\mathbf Q^2\), with basis \(e_1,e_2\), and let
\[
P=\mathbf Q[a_1,b_1,\ldots,a_4,b_4]
=\operatorname{Sym}(\mathbf Q^4\otimes F).
\]
The determinant-one diagonal torus on the first factor fixes precisely the equal row-degree pieces
\[
B=\bigoplus_{n\ge0}P_{(n,n,n,n)}
=\bigoplus_{n\ge0}(\operatorname{Sym}^nF)^{\otimes4}.
\]
Literal row permutations act by \(S_4\). The upper unipotent group of \(GL(F)\) acts infinitesimally by
\[
D_{\rm rows}=\sum_{r=1}^4 a_r\frac{\partial}{\partial b_r}.
\]
The desired two-row part of the projected flag algebra is
\[
A_4^{\le2}=(B^{S_4})^{U_2}.
\tag{Q4.1}
\]
This is the actual subalgebra of \(A_4\) having right highest weights \((\lambda_1,\lambda_2,0,0)\). A polynomial of that right-torus weight uses only the first two columns. All positive-root operators involving later columns annihilate it; the remaining operator is \(D_{\rm rows}\). This proves the precise identification with the flag construction.

Put \(Q=\mathbf Q[x_0,x_1,x_2,x_3,x_4]=\operatorname{Sym}(\operatorname{Sym}^4F)\), where \(x_i=e_1^{4-i}e_2^i\). Define
\[
\Phi(x_i)=\binom4i^{-1}
\sum_{\substack{I\subseteq\{1,2,3,4\}\\|I|=i}}
\prod_{r\in I}b_r\prod_{r\notin I}a_r.
\tag{Q4.2}
\]
This is the pullback of the multiplication map on four linear forms, using the perfect symmetric-power pairing. It is a \(GL(F)\)-equivariant graded algebra morphism \(Q\to B^{S_4}\). In particular,
\[
D_{\rm rows}\Phi(x_i)=i\Phi(x_{i-1}),
\]
as is also verified directly: each monomial with \(i-1\) selected \(b\)'s is obtained \(5-i\) times before dividing by \(\binom4i\).

Every complex binary quartic factors into four linear forms. Therefore the multiplication map is surjective over \(\mathbf C\), so its pullback \(\Phi\) is injective, also over \(\mathbf Q\). In degree \(n\), its source and target both have dimension
\[
\dim\operatorname{Sym}^n(\operatorname{Sym}^4F)
=\binom{n+4}{4}
=\dim\operatorname{Sym}^4(\operatorname{Sym}^nF).
\]
Consequently \(\Phi\) is surjective degree by degree and is an algebra isomorphism. This is the explicit binary canonical Foulkes map \(h_{n,4}\) in each degree, and it is multiplicative across degrees.

Let
\[
D=\sum_{i=1}^4 i x_{i-1}\frac{\partial}{\partial x_i}.
\]
Since characteristic zero identifies invariance under the additive one-parameter group with the kernel of its locally nilpotent derivation, (Q4.1)–(Q4.2) give
\[
\boxed{A_4^{\le2}\simeq\ker(D:Q\to Q).}
\tag{Q4.3}
\]
This proves the morphism relating the binary-quartic calculation to the normalizer projection, including its multiplication.

## T-022. Complete presentation, positive basis, and SAGBI degeneration

In \(Q\), define
\[
\begin{aligned}
f&=x_0,\\
H&=x_0x_2-x_1^2,\\
T&=x_0^2x_3-3x_0x_1x_2+2x_1^3,\\
I&=x_0x_4-4x_1x_3+3x_2^2,\\
J&=x_0x_2x_4+2x_1x_2x_3-x_0x_3^2-x_1^2x_4-x_2^3.
\end{aligned}
\tag{Q4.4}
\]
Direct differentiation proves that each lies in \(\ker D\). Direct expansion gives
\[
T^2+4H^3-f^2HI+f^3J=0.
\tag{Q4.5}
\]
The exact presentation is
\[
\boxed{\ker D=\mathbf Q[f,H,I,J,T]/(T^2+4H^3-f^2HI+f^3J).}
\tag{Q4.6}
\]

Here is a full proof of generation and absence of further relations, formulated to identify the possible denominator obstruction explicitly. After inverting \(f=x_0\), translate by the group parameter \(-x_1/f\). The resulting coordinates have first coordinate \(f\), second coordinate zero, and the other three coordinates
\[
y_2=H/f,\qquad y_3=T/f^2,\qquad
y_4=(f^2I-3H^2)/f^3.
\]
The inverse translation recovers the original coordinates. Thus
\[
Q[f^{-1}]
=\mathbf Q[f^{\pm1},x_1/f,y_2,y_3,y_4],
\]
and \(D(x_1/f)=1\), while \(D\) annihilates the other four generators. Hence
\[
(\ker D)[f^{-1}]
=\mathbf Q[f^{\pm1},H,T,I].
\tag{Q4.7}
\]

Let \(C_0\) be the abstract right side of (Q4.6), and map it to \(Q\) by (Q4.4). Its defining equation is monic in \(T\), so it is free over the abstract polynomial ring \(\mathbf Q[f,H,I,J]\) with basis \(1,T\); in particular multiplication by \(f\) is injective. After inverting \(f\), the equation solves for \(J\), and (Q4.7) shows that the map becomes an isomorphism to the displayed polynomial subalgebra. Thus \(C_0\to Q\) is injective before localization as well.

Modulo \(f\), this map is
\[
\mathbf Q[H,T,I,J]/(T^2+4H^3)
\longrightarrow \mathbf Q[x_1,x_2,x_3,x_4],
\]
\[
H\mapsto-x_1^2,\quad T\mapsto2x_1^3,\quad
I\mapsto-4x_1x_3+3x_2^2,\quad
J\mapsto2x_1x_2x_3-x_1^2x_4-x_2^3.
\tag{Q4.8}
\]
This map is injective. The first two images give exactly the cusp algebra
\(\mathbf Q[x_1^2,x_1^3]\): reduction to \(H^aT^\epsilon\), \(\epsilon=0,1\), yields distinct powers of \(x_1\). Over \(\mathbf Q(x_1,x_2)\), the last two images are affine linear coordinates in \(x_3,x_4\), with nonzero triangular coefficients \(-4x_1\) and \(-x_1^2\). They are algebraically independent over \(\mathbf Q(x_1)\), and hence over the cusp algebra. This proves the asserted injectivity.

It follows that \(C_0\cap fQ=fC_0\). Every \(g\in\ker D\) belongs to \(C_0[f^{-1}]\) by (Q4.7). Choose a smallest \(r\ge0\) for which \(f^rg\in C_0\). If \(r>0\), then \(f^rg\in C_0\cap fQ=fC_0\), contradicting minimality. Thus \(r=0\), proving (Q4.6).

In particular the monomials
\[
f^aH^bI^cJ^dT^\epsilon,\qquad
a,b,c,d\ge0,\quad\epsilon\in\{0,1\},
\tag{Q4.9}
\]
form a basis.

Now put positive ambient weights \((1,2,1,2,2)\) on
\((x_0,x_1,x_2,x_3,x_4)\), and refine the weighted order by lexicographic order. The leading terms of \((f,H,T,I,J)\) are
\[
x_0,\quad -x_1^2,\quad 2x_1^3,\quad -4x_1x_3,\quad -x_1^2x_4.
\tag{Q4.10}
\]
The leading monomial of (Q4.9) is
\[
x_0^a x_1^{\,2b+c+2d+3\epsilon}x_3^cx_4^d.
\]
All these monomials are distinct: recover \(a,c,d\) from their coordinates, recover \(\epsilon\) by parity of the remaining \(x_1\) exponent, then recover \(b\). Therefore every nonzero element of \(C_0\) has leading monomial in the algebra generated by (Q4.10). Conversely the leading generator monomials belong to the initial algebra. This proves, without an unverified subduction assumption, that the five generators are a SAGBI basis and
\[
\boxed{\operatorname{in}(A_4^{\le2})
\simeq\mathbf Q[x_0,x_1^2,x_1^3,x_1x_3,x_1^2x_4].}
\tag{Q4.11}
\]
This is a toric algebra; normality is not asserted. Its only toric relation, with the coefficient normalization in (Q4.10), is \(T^2+4H^3=0\). The unique-exponent argument proves that there are no further relations. The ambient weight filtration, transported along (Q4.3), supplies the toric degeneration of the specified normalizer subalgebra.

The generator degrees \((n;\lambda_1,\lambda_2)\) are
\[
\begin{array}{c|ccccc}
 &f&H&I&J&T\\ \hline
n&1&2&2&3&3\\
\lambda&(4,0)&(6,2)&(4,4)&(6,6)&(9,3).
\end{array}
\]
Thus, for \(0\le k\le2n\),
\[
\boxed{
a_{4,n}^{(4n-k,k)}
=\sum_{\epsilon=0}^{1}
\#\left\{(a,b,c,d)\in\mathbf Z_{\ge0}^{4}:
\begin{array}{rcl}
a+2b+2c+3d&=&n-3\epsilon,\\
2b+4c+6d&=&k-3\epsilon
\end{array}\right\}.
}
\tag{Q4.12}
\]
These are two bounded rational polytopes of fixed dimension, specified by a constant matrix and the two input integers. The first equation bounds every coordinate. Unlike the general construction, no parameter-dependent Reynolds enumeration, Hilbert-basis calculation, or polynomial elimination is required to produce these polytopes. They recover a known coefficient family through the explicit normalizer algebra and its toric filtration.

## T-023. A precise obstruction for the ordinary lexicographic candidate

The same five generators do not form a SAGBI basis for ordinary lexicographic order \(x_0>x_1>x_2>x_3>x_4\). Their leading monomials are
\[
x_0,\quad x_0x_2,\quad x_0^2x_3,\quad x_0x_4,\quad x_0x_2x_4.
\]
But \(fJ-HI\) belongs to their algebra and has leading term \(-x_0^2x_3^2\). A nonnegative product of the listed leading monomials with zero \(x_2,x_4\) exponents can use only \(x_0\) and \(x_0^2x_3\). Obtaining \(x_3^2\) then forces \(x_0\) exponent at least four, rather than two. Thus the required leading monomial is absent. This proves the failure of that particular order; (Q4.10) gives an explicit order for which the same generators succeed.

## Exact checks and next sector

The script check_binary_quartic.py checks every derivation identity, the defining relation, the five weighted leading terms, and the lex obstruction by exact symbolic arithmetic. It also compares (Q4.12) with independent Gaussian-rectangle weight differences for all \(0\le n\le100\), \(0\le k\le2n\): 10,201 coefficients. Every value agrees. BINARY_QUARTIC_CHECK.tsv and SYMBOLIC_CHECK.txt provide the receipts. These are finite checks supplementary to the complete proof.

The full \(A_4\), and already its output-length-three subalgebra, contain additional highest weights and are not evaluated by (Q4.3). The displayed morphism is exact for the stated two-row sector. The next concrete task is an explicit presentation or filtration for the length-three sector, using the three-column flag variables rather than extending the binary map without a proved morphism.



# A uniform positive formula and toric degeneration for equal middle rows

Run: `GCT_PLETH-20261121-theta`. Author/checker: GPT-6 Astra Pro; reasoning-effort setting is not surfaced by the runtime. All coefficient statements are in characteristic zero. Every algebra map and parity character used below is specified. These are direct constructions and deductions; no claim of historical novelty is made.

## Result and scope

Write
\[
a_{m,n}^{\lambda}=[S_\lambda V:\operatorname{Sym}^m(\operatorname{Sym}^nV)]
\]
in a dimension at least the length of \(\lambda\). Fix \(m\ge3\), \(n\ge0\), and a partition
\[
\lambda=(\alpha,\beta^{m-2},\gamma)\vdash mn,
\qquad \alpha\ge\beta\ge\gamma\ge0.
\]
Put
\[
N=\binom m2,\quad \epsilon=\beta\bmod2\in\{0,1\},\quad
L=\max(0,\beta-n),\quad
R=\beta-\gamma-N\epsilon-mL.
\tag{E.1}
\]
Equivalently, \(R=\min(\alpha-\beta,\beta-\gamma)-N\epsilon\). The equality follows from the exact identity \((\alpha-\beta)-(\beta-\gamma)=m(n-\beta)\), using \(|\lambda|=mn\); the basis bijection proving the formula is given in (E.26).
The result proved below is
\[
\boxed{
a_{m,n}^{(\alpha,\beta^{m-2},\gamma)}
=\#\left\{(c_2,\ldots,c_m)\in\mathbf Z_{\ge0}^{m-1}:
\sum_{i=2}^m i c_i=R\right\}.}
\tag{E.2}
\]
The set is empty for \(R<0\). This is one bounded rational polytope, described directly by \(m-1\) variables, nonnegativity, and one equation. In particular,
\[
\boxed{a_{m,n}^{\lambda}>0\quad\Longleftrightarrow\quad R=0\text{ or }R\ge2.}
\tag{E.3}
\]
The same construction gives an explicit flat toric degeneration of the entire corresponding subalgebra of the balanced normalizer invariant algebra. It involves no Reynolds enumeration, Hilbert-basis computation, or elimination precomputation. For \(m=3\), the shape condition includes every possible output partition of \(s_3[s_n]\). For \(m=4\), it includes every \((\alpha,\beta,\beta,\gamma)\), with arbitrary determinant shift \(\gamma\).

## T-024. Exact incidence and normalizer algebra

### 1. The flag-algebra morphism

Let \(E=F=\mathbf Q^m\). Use the polynomial representation
\[
P=\operatorname{Sym}(E\otimes F)=\mathbf Q[X_{ij}:1\le i,j\le m].
\]
The two general linear groups act on the two factors. Choose the upper unipotent group \(U_F\) so that the minors of the first \(j\) columns are highest-weight vectors of right weight \(\omega_j=(1^j,0^{m-j})\). Polynomial Cauchy duality gives
\[
P^{U_F}=\bigoplus_{\lambda:\ell(\lambda)\le m} S_\lambda E,
\tag{E.4}
\]
where each summand is marked by its right highest weight \(\lambda\). This is the same polynomial Howe algebra used in T-002 and G-009. Taking the determinant-one row torus \(T_0\) keeps the equal row-weight spaces, and taking literal permutation matrices \(S_m\) then gives
\[
\dim ((P^{U_F})^{T_0\rtimes S_m})_{n,\lambda}
=a_{m,n}^{\lambda}.
\tag{E.5}
\]
Indeed, before taking \(U_F\), the row weight \((n^m)\) is \((\operatorname{Sym}^nF)^{\otimes m}\); ordinary row permutations are ordinary tensor permutations. Their invariants are \(\operatorname{Sym}^m(\operatorname{Sym}^nF)\). Taking right highest vectors gives (E.5). Thus the finite group here is fixed by the actual representation, including its determinant character.

Define
\[
x_i=X_{i1},\qquad
y_i=(-1)^{i-1}\det X_{[m]\setminus\{i\},[m-1]},\qquad
z=\det X.
\tag{E.6}
\]
The span of the \(x_i\) is \(E\), the span of the \(y_i\) is \(\Lambda^{m-1}E\simeq E^*\otimes\det E\), and \(z\) spans \(\det E\). Their right weights are respectively \(\omega_1,\omega_{m-1},\omega_m\). The relevant right-weight submonoid consists exactly of
\[
\lambda=(\alpha,\beta^{m-2},\gamma)
=(\alpha-\beta)\omega_1+(\beta-\gamma)\omega_{m-1}+\gamma\omega_m.
\tag{E.7}
\]
Consequently the corresponding subalgebra of \(P^{U_F}\) is generated by the \(x_i,y_i,z\). Here is a direct generation argument. The subalgebra generated by these three left-stable spaces is left \(GL(E)\)-stable. The product of suitable nonzero highest vectors from the three spaces is a nonzero polynomial in every degree (E.7), since \(P\) is a domain. It lies in the single irreducible left module \(S_\lambda E\) occurring in (E.4). A nonzero left-stable subspace of that module is the whole module. This proves generation in every marked degree, including weights on the boundary where some coefficient in (E.7) vanishes.

There is precisely one defining relation:
\[
\boxed{
P^{U_F}_{\mathrm{ends}}
\simeq\mathbf Q[x_1,\ldots,x_m,y_1,\ldots,y_m,z]
\big/\left(\sum_{i=1}^m x_i y_i\right).}
\tag{E.8}
\]
The relation is the determinant expansion with the first column repeated. To prove that there are no others, work over an algebraic closure and prescribe \(x\ne0\), \(y\ne0\), with \(y(x)=0\). Choose columns \(x,c_2,\ldots,c_{m-1}\) forming a basis of \(\ker(y)\). Their exterior product is a nonzero scalar multiple of the prescribed oriented \((m-1)\)-vector associated to \(y\). Since \(m\ge3\), one of \(c_2,\ldots,c_{m-1}\) can be rescaled while leaving \(x\) fixed, so that the exterior product is exactly the prescribed one. The final column can then be chosen with arbitrary determinant \(z\), because its pairing with the nonzero cofactor vector is a nonzero linear functional. Thus the matrix map (E.6) reaches the dense open set \(x\ne0,y\ne0\) of the incidence hypersurface times \(\mathbf A^1_z\).

For completeness, the incidence polynomial is irreducible: regard it as a polynomial linear in \(y_1\) over \(\mathbf Q[x_1,\ldots,x_m,y_2,\ldots,y_m]\). The coefficient \(x_1\) and constant term \(\sum_{i>1}x_i y_i\) are relatively prime. Gauss's lemma proves irreducibility. The resulting hypersurface is a domain, so density proves the asserted kernel. The map and all equations have rational coefficients, giving (E.8) over \(\mathbf Q\).

### 2. Exact torus quotient and the signs of permutation matrices

A monomial \(x^a y^b z^t\) has row weights
\[
a_i+|b|-b_i+t\qquad (1\le i\le m).
\tag{E.9}
\]
It is fixed by \(T_0\) precisely when all differences \(a_i-b_i\) are equal. Define
\[
u=\prod_i x_i,\qquad v=\prod_i y_i,\qquad t_i=x_i y_i.
\tag{E.10}
\]
If the common difference is \(k\ge0\), the monomial is \(u^k\prod_i t_i^{b_i}z^t\); if it is \(k<0\), it is \(v^{-k}\prod_i t_i^{a_i}z^t\). These expressions also prove, by their distinct exponent vectors in the original \(x,y,z\), that the only relation before the incidence quotient is \(uv=\prod_i t_i\). The incidence relation has \(T_0\)-weight zero, and exact weight decomposition passes to its quotient. More explicitly, if a weight-zero element equals \((\sum_i x_i y_i)h\), then only the weight-zero part of \(h\) contributes, because the multiplier has weight zero and the polynomial ring is a domain. Therefore
\[
\boxed{
B_{\mathrm{ends}}:=(P^{U_F}_{\mathrm{ends}})^{T_0}
\simeq\mathbf Q[u,v,z,t_1,\ldots,t_m]
/(\sum_i t_i,\ uv-\prod_i t_i).}
\tag{E.11}
\]

For a literal permutation matrix \(\sigma\), the exterior-power identification in (E.6) gives
\[
\sigma x_i=x_{\sigma(i)},\qquad
\sigma y_i=\operatorname{sgn}(\sigma)y_{\sigma(i)},\qquad
\sigma z=\operatorname{sgn}(\sigma)z.
\tag{E.12}
\]
Thus
\[
\sigma u=u,\qquad \sigma v=\operatorname{sgn}(\sigma)^m v,
\qquad \sigma t_i=\operatorname{sgn}(\sigma)t_{\sigma(i)}.
\tag{E.13}
\]
Both equations in (E.11) generate stable ideals under this action. These signs are retained in every subsequent invariant calculation.

### 3. Alternating-group presentation and diagonal involution

Let \(\mathfrak A_m\) denote the alternating group. Its action on the \(t_i\) is ordinary permutation, and it fixes \(u,v,z\). Write
\[
e_i=e_i(t_1,\ldots,t_m),\qquad
D=\prod_{i<j}(t_i-t_j),\qquad N=\binom m2.
\tag{E.14}
\]
Then
\[
\mathbf Q[t_1,\ldots,t_m]^{\mathfrak A_m}
=\mathbf Q[e_1,\ldots,e_m]\oplus D\mathbf Q[e_1,\ldots,e_m].
\tag{E.15}
\]
To verify (E.15), average an alternating-group invariant with its image under one odd permutation. Its plus part is symmetric; its minus part transforms by the sign character under all permutations. A sign polynomial vanishes at each \(t_i=t_j\), hence is divisible by every \(t_i-t_j\), and therefore by their product \(D\). Its quotient by \(D\) is symmetric. The fundamental theorem of symmetric polynomials gives (E.15), and uniqueness follows from the different characters. Its multiplication is specified by
\[
D^2=\mathcal D_m(e_1,\ldots,e_m),
\tag{E.16}
\]
where \(\mathcal D_m\) is the discriminant of
\(T^m-e_1T^{m-1}+e_2T^{m-2}-\cdots+(-1)^m e_m\).

Taking invariants of the two relations in (E.11) is exact. One can see the exactness without a structural assumption on the quotient: averaging any expression \(e_1h+(uv-e_m)k\) over \(\mathfrak A_m\) averages \(h,k\), since both multipliers are invariant. Thus set \(e_1=0\) and substitute \(e_m=uv\) in (E.15)–(E.16). The result is
\[
\boxed{
B_{\mathrm{ends}}^{\mathfrak A_m}
\simeq
\mathbf Q[u,v,z,e_2,\ldots,e_{m-1},D]
\big/(D^2-\mathcal D_m(0,e_2,\ldots,e_{m-1},uv)).}
\tag{E.17}
\]
In particular, this ring is free, with basis \(1,D\), over the polynomial ring in \(u,v,z,e_2,\ldots,e_{m-1}\). This follows from the monic quadratic relation; no assertion about algebraic independence has been left to a dimension count.

The remaining quotient \(S_m/\mathfrak A_m\) acts diagonally. On an odd permutation, (E.13) gives
\[
u\longmapsto u,\quad v\longmapsto(-1)^m v,\quad
z\longmapsto-z,\quad e_i\longmapsto(-1)^i e_i,
\quad D\longmapsto(-1)^{N+1}D.
\tag{E.18}
\]
The last sign has two factors: the ordinary Vandermonde permutation sign and the factor \((-1)^N\) from negating all \(t_i\). Hence
\[
\boxed{A_{\mathrm{ends}}:=(B_{\mathrm{ends}})^{S_m}
=(B_{\mathrm{ends}}^{\mathfrak A_m})^{\langle\tau\rangle},}
\tag{E.19}
\]
where \(\tau\) is exactly the diagonal involution (E.18). A vector-space basis of this algebra consists of the monomials
\[
u^a v^b z^t\prod_{i=2}^{m-1}e_i^{c_i}D^\varepsilon,
\quad a,b,t,c_i\ge0,\quad\varepsilon\in\{0,1\},
\tag{E.20}
\]
whose sign exponent
\[
mb+t+\sum_{i=2}^{m-1} i c_i+(N+1)\varepsilon
\tag{E.21}
\]
is even. The basis follows directly from (E.17); every basis vector is an eigenvector of \(\tau\).

## T-025. One bounded polytope and a complete nonvanishing test

Set \(K=\sum_{i=2}^{m-1}i c_i+N\varepsilon\). The basis monomial (E.20) has balanced row degree and right highest weight
\[
\begin{aligned}
n&=a+(m-1)b+t+K,\\
\lambda_1&=m(a+b)+t+2K,\\
\lambda_2=\cdots=\lambda_{m-1}&=mb+t+K,\\
\lambda_m&=t.
\end{aligned}
\tag{E.22}
\]
These formulas can be checked on each generator: \(u\) has right weight \(m\omega_1\) and balanced degree 1; \(v\) has right weight \(m\omega_{m-1}\) and balanced degree \(m-1\); \(z\) has weight \(\omega_m\) and degree 1; each \(t_i\) has weight \(\omega_1+\omega_{m-1}=(2,1^{m-2},0)\) and balanced degree 1. Thus \(e_i\) has \(i\) times that weight and degree \(i\), while \(D\) has \(N\) times that weight and degree \(N\).

For a fixed partition \((\alpha,\beta^{m-2},\gamma)\) and degree \(n\), (E.22) gives
\[
t=\gamma,\qquad a-b=n-\beta,\qquad
mb+\sum_{i=2}^{m-1}i c_i=\beta-\gamma-N\varepsilon.
\tag{E.23}
\]
The first-row equation is then automatic from \(|\lambda|=mn\). Substitution into the sign condition (E.21) gives simply
\[
\beta+\varepsilon\equiv0\pmod2.
\tag{E.24}
\]
Therefore \(\varepsilon=\epsilon=\beta\bmod2\) is uniquely determined. The conditions \(a,b\ge0\) are equivalent to \(b\ge L=\max(0,\beta-n)\). Set \(b=L+c_m\). The remaining equation becomes exactly
\[
\sum_{i=2}^m i c_i
=\beta-\gamma-N\epsilon-mL=R.
\tag{E.25}
\]
The map from a lattice point in (E.25) to its basis vector is explicit and bijective:
\[
\begin{aligned}
b&=L+c_m, &a&=n-\beta+L+c_m, &t&=\gamma, &\varepsilon&=\epsilon.
\end{aligned}
\tag{E.26}
\]
This proves (E.2), with neither a subtraction of counts nor an unknown rank. Boundedness follows from \(0\le c_i\le R/i\) whenever \(R\ge0\).

Since the denominators include 2 and 3, their additive semigroup is exactly \(\{0\}\cup\{2,3,4,\ldots\}\): even integers are sums of 2's, and every odd integer at least 3 is 3 plus a sum of 2's. No sum of the allowed positive integers is 1. This proves (E.3), including all cases \(n=0\), \(\gamma=0\), \(\alpha=\beta\), or \(\beta=\gamma\).

### Encoding and the precise efficiency conclusion

The polytope is constructed by integer arithmetic on \(m,n,\beta,\gamma\), and its full description has \(O(m)\) integer entries of bit length \(O(\log(m(n+1)+1))\). There is no parameter-dependent algebra presentation to compute beforehand. A lattice witness has \(O(m\log(m(n+1)+1))\) bits and is verified by one weighted sum. Thus this coefficient family has a direct counting-verifier interpretation in \(\#P\) for ordinary explicit partition encoding. In that encoding, a nonzero middle part gives at least \(m-1\) explicitly listed parts; when \(\beta=0\), the coefficient is 1 and can be handled separately. A representation of partitions that compresses long strings of equal parts changes the size convention; the displayed \(O(m)\) description is not asserted polynomial in the length of that compressed encoding. The nonvanishing criterion (E.3) is an integer-arithmetic polynomial-time test even when the repeated middle part is compressed. No polynomial-time assertion for exact counting with variable \(m\) is needed here.

### Concrete subfamilies and checks

For \(m=3\), the coefficient is the number of solutions \(2c_2+3c_3=R\), with
\(R=\beta-\gamma-3(\beta\bmod2)-3\max(0,\beta-n)\). Root independently compared this formula and its support test with the separate finite-character formula G-007 for all 261,425 partitions occurring as test inputs in degrees \(n=1,\ldots,100\). Every comparison passed; see `work/root/EQUAL_MIDDLE_M3_CHECK.tsv`.

The rectangular agent independently expanded the power-sum cycle index of \(h_m[h_n]\) and used Murnaghan–Nakayama characters. All 151 admissible end-shape cases for \(m=4,n=0,\ldots,6\), \(m=5,n=0,\ldots,4\), and \(m=6,n=0,\ldots,3\) passed. Code: `work/rectangular/verify_endsector_formula.py`; receipt: `work/rectangular/ENDSECTOR_INDEPENDENT_CHECK.tsv`. Those calculations do not derive their comparison values from the incidence algebra.

## T-026. Explicit uniform toric degeneration

This section gives a flat algebra family whose general fiber is (E.19), and whose special fiber is a semigroup algebra. The construction is direct for every \(m\); it does not require a computation of a generating set for the full flag normalizer algebra.

Start from (E.17). Assign temporary nonnegative weights \(w\) as follows.

* For even \(m\), set \(w(u)=w(v)=1\), \(w(D)=m-1\), and give all other generators weight zero.
* For odd \(m\), set \(w(e_{m-1})=2\), \(w(D)=m\), and give all other generators weight zero.

The discriminant has weighted degree \(m(m-1)=2N\) for the coefficient weights \(\deg(e_i)=i\). For even \(m\), the unique term with greatest possible exponent of \(e_m\) is
\[
q_m e_m^{m-1},\qquad q_m\in\mathbf Q^\times.
\tag{E.27}
\]
Its coefficient is nonzero because the polynomial \(T^m+(-1)^m e_m\) has no repeated root for \(e_m\ne0\) in characteristic zero. The coefficient degree forces an exponent at most \(m-1\), and equality leaves degree zero for all other factors, proving uniqueness. After \(e_m=uv\), its temporary weight is \(2(m-1)\), equal to \(2w(D)\); every other term has smaller temporary weight.

For odd \(m\), the unique term with greatest possible exponent of \(e_{m-1}\) is
\[
r_m e_{m-1}^{m},\qquad r_m\in\mathbf Q^\times.
\tag{E.28}
\]
Again the coefficient degree bounds the exponent by \(m\), with equality unique. Its coefficient is nonzero because \(T^m+(-1)^{m-1}e_{m-1}T\) has one simple root at zero and \(m-1\) distinct nonzero roots for \(e_{m-1}\ne0\). Its temporary weight is \(2m=2w(D)\), greater than all other terms.

If strictly positive generator weights are desired, add the original balanced degree to each temporary weight. The original relation is homogeneous of balanced degree \(2N\), so this leaves all comparisons of its terms unchanged.

Introduce a parameter \(s\), and for a monomial \(M\) in the discriminant let \(w(M)\) be its temporary weight. Define
\[
\mathscr C=
\mathbf Q[s,u,v,z,e_2,\ldots,e_{m-1},D]
\Big/\left(D^2-
\sum_M [M]\mathcal D_m\;s^{2w(D)-w(M)}M\right),
\tag{E.29}
\]
where \(\mathcal D_m=\mathcal D_m(0,e_2,\ldots,e_{m-1},uv)\). All powers of \(s\) are nonnegative by (E.27)–(E.28). The relation is monic in \(D\), so \(\mathscr C\) is free with basis \(1,D\) over \(\mathbf Q[s,u,v,z,e_2,\ldots,e_{m-1}]\), and in particular is flat over \(\mathbf Q[s]\). The fiber at \(s=1\) is (E.17). Over \(s\ne0\), the exact isomorphism from the original algebra tensored with \(\mathbf Q[s,s^{-1}]\) to \(\mathscr C[s^{-1}]\) sends each original generator \(X\) to \(s^{-w(X)}X\). Its inverse sends the new generator \(X\) to \(s^{w(X)}X_{\rm original}\). Substitution into the defining equations verifies both maps. At zero its relation is respectively
\[
D^2-q_m(uv)^{m-1}\quad(m\text{ even}),\qquad
D^2-r_m e_{m-1}^{m}\quad(m\text{ odd}).
\tag{E.30}
\]
These are prime toric binomials, including over \(\mathbf Q\) after a rational rescaling. In either case the exponent \(q\) on the other monomial is odd. For a relation \(D^2-cY^q\), put \(Y'=cY\) and \(D'=c^{(q-1)/2}D\), giving \((D')^2=(Y')^q\). In the even case take \(Y=uv\) and rescale \(u\) alone. The odd case is the cusp semigroup ring \(\mathbf Q[t^2,t^m]\) tensored with a polynomial ring. The even case embeds as
\[
u\longmapsto a^2,\qquad v\longmapsto b^2,
\qquad D\longmapsto a^{m-1}b^{m-1}.
\tag{E.31}
\]
Its kernel is exactly the displayed binomial: the monomials \(u^i v^j D^\varepsilon\), \(\varepsilon\in\{0,1\}\), have distinct image exponents because \(m-1\) is odd. These arguments prove the domain and semigroup assertions directly. Normality is not asserted.

The involution (E.18) extends to \(\mathscr C\) by fixing \(s\). It preserves every term of the relation, since every discriminant term has even sign. In the free \(\mathbf Q[s]\)-basis of monomials (E.20), its action is diagonal and independent of \(s\). Therefore
\[
\mathscr A=\mathscr C^{\langle\tau\rangle}
\tag{E.32}
\]
is free over \(\mathbf Q[s]\), with basis the same sign-even monomials (E.20)–(E.21). Its fibers commute with invariants, as is also immediate from this basis. Its fiber at 1 is \(A_{\mathrm{ends}}\). Its fiber at 0 is the subalgebra of the semigroup algebra (E.30) spanned by monomials of even sign. Since the defining binomial preserves the sign, this is a semigroup algebra for the kernel of a homomorphism of the exponent semigroup to \(\mathbf Z/2\). It is finitely generated explicitly by the even-sign generators and the pairwise products of the odd-sign generators: any even-sign monomial can be grouped into those factors. Thus (E.32) is an explicit flat toric degeneration of the desired end-sector normalizer algebra.

The family respects the balanced degree and the right highest-weight grading throughout, because the defining relation and its separate terms all have the same such degrees. Its basis is the same basis used in (E.25), so the polytope formula counts the graded Hilbert function of both general and special fibers. This proves the precise morphism between the plethysm coefficients, the incidence quotient, and the toric model.

## A fully written outer-degree-four illustration

In the length-three part \(m=4,\gamma=0\), let \(s_2=e_2\), \(q=e_3^2\), and \(w=e_3D\). In (E.18), \(e_3,D\) are odd and \(u,v,e_2\) are even. Hence
\[
A_{4,\mathrm{ends},\gamma=0}
\simeq\mathbf Q[u,v,s_2,q,w]/(w^2-q\mathcal D(s_2,q,uv)),
\tag{E.33}
\]
where the depressed-quartic discriminant is
\[
\mathcal D(s_2,q,p)
=256p^3-128s_2^2p^2+144s_2qp-27q^2
+16s_2^4p-4s_2^3q.
\tag{E.34}
\]
The ring is free with basis \(1,w\) over \(\mathbf Q[u,v,s_2,q]\). The generator degrees \((n;\lambda)\) are
\[
\begin{array}{c|c|c}
u&1&(4,0,0)\\
v&3&(4,4,4)\\
s_2&2&(4,2,2)\\
q&6&(12,6,6)\\
w&9&(18,9,9).
\end{array}
\tag{E.35}
\]
Thus one also obtains two four-variable polytopes
\[
n=a+3b+2c+6d+9\delta,\qquad
\beta=4b+2c+6d+9\delta,
\quad a,b,c,d\ge0,\quad\delta\in\{0,1\}.
\tag{E.36}
\]
They are equivalent, by the explicit basis analysis above, to the single three-variable polytope (E.25). Formula (E.33) supplies a small presentation in addition to the count; all determinant shifts are included in the uniform construction (E.17)–(E.25).

## Relation to the main gates

G-009–G-011 already give terminating positive-polytope constructions for all symmetric plethysm, general Schur plethysm, and canonical-map image multiplicities. T-024–T-026 replace their parameter-dependent invariant computation by one uniform explicit presentation, one bounded polytope, and an arithmetic nonvanishing test on the family (E.7). They also give a direct toric degeneration in every outer degree. The arbitrary-output efficient formula remains outside this proved family. Nothing here asserts that the dimension of a canonical-map image equals a coefficient; the actual canonical images retain G-011's two-projector morphism.

## Sources, provenance, and proof checks

The input representation identity is polynomial Cauchy/Howe duality with its balanced permutation action, proved in T-002 and re-derived in (E.4)–(E.5). An exact primary locator supplied with the task is J. M. Landsberg, *Geometric Complexity Theory: an introduction for geometers*, subsection “A duality theorem for weight zero spaces and plethysms,” theorem `gaythm`, source lines 766–798; its underlying result is attributed there to Gay (1976). The trace-free incidence presentation, the alternating-group calculation, the full determinant sign, the bijection (E.26), and the flat family (E.29)–(E.32) are all proved in this report. No unlocated literature theorem is used to infer the formula. The elementary discriminant coefficient arguments are included explicitly in (E.27)–(E.28).

For the classical relative-invariant step, R. P. Stanley, *Invariants of finite groups and their applications to combinatorics*, Bull. Amer. Math. Soc. **1** (1979), 475–511, Proposition 4.7 and its symmetric-group specialization on printed pp. 488–489, identifies alternating polynomials as the Vandermonde times symmetric polynomials. The primary author-hosted source was read directly: https://math.mit.edu/~rstan/pubs/pubfiles/38.pdf. Equation (E.15) gives the exact index-two decomposition needed here, with the later determinant twist computed separately.

The proof is to be recorded as a whole-proof check only after reading every step of this report. Independent computation receipts and independent proof readers are listed separately in `CHECK_EVENTS.tsv`; the numerical comparisons are evidence additional to the proof, not replacements for it.


# Arbitrary outer Schur functors on the equal-middle-row family

This report extends T-024–T-026 by identifying the full balanced permutation module. All statements below are unconditional over characteristic zero, and every coefficient is accompanied by an explicit algebra or lattice-point morphism. Author/checker: GPT-6 Astra Pro, run `GCT_PLETH-20261121-theta`; effort setting is not exposed.

## T-027. Exact reflection-representation model and positive tableau formula

Let \(m\ge3\), \(\mu\vdash m\), \(n\ge0\), and
\[
\lambda=(\alpha,\beta^{m-2},\gamma)\vdash mn,
\qquad \alpha\ge\beta\ge\gamma\ge0.
\]
Write
\[
p_{\mu,(n)}^\lambda=[S_\lambda V:S_\mu(\operatorname{Sym}^nV)],
\qquad
S=\min(\alpha-\beta,\beta-\gamma).
\tag{S.1}
\]
Let \(\mathfrak h_m\) be the \((m-1)\)-dimensional standard representation of \(S_m\), realized as the quotient of its permutation representation by the trivial line. Set
\[
\nu=\begin{cases}\mu,&\beta\text{ even},\\ \mu',&\beta\text{ odd}.\end{cases}
\tag{S.2}
\]
For a standard Young tableau \(T\) with entries \(1,\ldots,m\), define
\[
\operatorname{Des}(T)=\{i: i+1\text{ lies in a lower row than }i\},
\qquad
\operatorname{comaj}(T)=\sum_{i\in\operatorname{Des}(T)}(m-i).
\tag{S.3}
\]
Then the exact formulas are
\[
\boxed{
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq\operatorname{sgn}^{\beta}\otimes
\operatorname{Sym}^{S}(\mathfrak h_m)
\quad\text{as }S_m\text{-modules},}
\tag{S.4}
\]
and
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_{T\in\operatorname{SYT}(\nu)}
\#\left\{(c_2,\ldots,c_m)\in\mathbf Z_{\ge0}^{m-1}:
\sum_{i=2}^m i c_i=S-\operatorname{comaj}(T)\right\}.}
\tag{S.5}
\]
Negative right sides contribute zero. The sum is finite and entirely explicit. T-028 below realizes it as the lattice-point count of one polytope with a polynomial-size description.

### Proof of the module isomorphism, including its character twist

Use the exact balanced incidence algebra from T-024:
\[
B_{\mathrm{ends}}
=\mathbf Q[u,v,z,t_1,\ldots,t_m]
/(\sum_i t_i,\ uv-\prod_i t_i),
\tag{S.6}
\]
with the right weights and literal permutation action in (E.12)–(E.13) of `end_node_report.md`. Put
\[
k=n-\beta,\quad k_+=\max(k,0),\quad L=\max(-k,0).
\]
Before imposing \(\sum_i t_i=0\), every monomial has a unique normal form with at most one of \(u,v\) present, using \(uv=\prod_i t_i\). Distinct such normal monomials have distinct exponent vectors in the original \(x_i,y_i,z\), as proved in T-024. In the component of degree \((n,\lambda)\), the normal form is necessarily
\[
u^{k_+}v^L z^\gamma f(t_1,\ldots,t_m),
\qquad \deg f=\beta-\gamma-mL.
\tag{S.7}
\]
This follows directly by subtracting the degree and middle-row equations (E.22), which gives the fixed difference \(a-b=k\); eliminating every factor \(uv\) increases the \(t\)-degree by \(m\). The equation \(\sum_i t_i=0\) does not change that difference. Its part in this component is exactly the same factor in (S.7) times a multiple of \(\sum_i t_i\). Thus multiplication in (S.7) gives a vector-space isomorphism
\[
\left(\mathbf Q[t_1,\ldots,t_m]/(\sum_i t_i)\right)_S
\longrightarrow (B_{\mathrm{ends}})_{n,\lambda}.
\tag{S.8}
\]
Here the degree equals \(S\), since
\[
(\alpha-\beta)-(\beta-\gamma)=m(n-\beta)=mk
\]
implies
\[
\beta-\gamma-m\max(0,\beta-n)
=\min(\alpha-\beta,\beta-\gamma).
\tag{S.9}
\]
This also proves its nonnegativity under the stated partition inequalities.

For an odd permutation, the factor \(v^Lz^\gamma\) contributes the sign \((-1)^{mL+\gamma}\). The degree-\(S\) polynomial in the \(t_i\) contributes an additional \((-1)^S\) under their signed permutation action. Since \(S+mL+\gamma=\beta\), the total twist is exactly \(\operatorname{sgn}^{\beta}\). The quotient by \(\sum_i t_i\) is the symmetric algebra on \(\mathfrak h_m\). Finally the polynomial Cauchy identification (E.4) identifies the right-hand side of (S.8), with all actions retained, with \((S_\lambda\mathbf Q^m)_{(n^m)}\). This proves (S.4).

The refined balanced Howe identity T-003 gives
\[
p_{\mu,(n)}^\lambda
=\dim\operatorname{Hom}_{S_m}([\mu],(S_\lambda\mathbf Q^m)_{(n^m)}).
\tag{S.10}
\]
The exact sign-twist identity \([\mu]\otimes\operatorname{sgn}\simeq[\mu']\) identifies this with the multiplicity of \([\nu]\) in \(\operatorname{Sym}^{S}\mathfrak h_m\). One character verification of this identity is as follows: the symmetric-function involution \(p_i\mapsto(-1)^{i-1}p_i\) sends \(s_\mu\) to \(s_{\mu'}\); under the Frobenius formula it multiplies the coefficient on a cycle type \(\rho\) by \((-1)^{m-\ell(\rho)}\), exactly the permutation sign. Equality of the resulting characters gives the module isomorphism in characteristic zero.

### Cycle traces and a full standardization proof

For a permutation with cycle lengths \(\rho_1,\ldots,\rho_\ell\), the permutation representation has characteristic determinant
\[
\det(1-q\sigma)=\prod_{j=1}^\ell(1-q^{\rho_j}).
\]
Removing the trivial line gives
\[
\sum_{d\ge0}\operatorname{tr}(\sigma;\operatorname{Sym}^d\mathfrak h_m)q^d
=\frac{1-q}{\prod_j(1-q^{\rho_j})}.
\tag{S.11}
\]
Take its inner product with the character \(\chi^\nu\). The Frobenius character formula, evaluated at the alphabet \(1,q,q^2,\ldots\), gives
\[
\begin{aligned}
\sum_{d\ge0}[\,[\nu]:\operatorname{Sym}^d\mathfrak h_m\,]q^d
&=(1-q)\sum_{\rho\vdash m}\frac{\chi^\nu(\rho)}{z_\rho}
\prod_j\frac1{1-q^{\rho_j}}\\
&=(1-q)s_\nu(1,q,q^2,\ldots).
\end{aligned}
\tag{S.12}
\]
The equality uses precisely \(p_i(1,q,q^2,\ldots)=(1-q^i)^{-1}\). It is a formal power-series equality, so no analytic specialization is needed.

We now derive the positive numerator without assuming a coinvariant-ring decomposition. Semistandard tableaux of shape \(\nu\), with weak rows and strict columns, enumerate \(s_\nu(1,q,q^2,\ldots)\), with weight \(q^{\sum_c(Q(c)-1)}\). Standardize a semistandard tableau by ordering cells by increasing entry and breaking ties from left to right. Equal entries cannot occupy the same column; their left-to-right order runs weakly upward in row number, by the column-strict and row-weak conditions. The result is a standard tableau \(T\), together with integers
\[
0\le a_1\le\cdots\le a_m,
\qquad a_i<a_{i+1}\text{ for every }i\in\operatorname{Des}(T),
\tag{S.13}
\]
where \(a_i+1\) is the original entry in the cell labelled \(i\).

Conversely, fill the cell labelled \(i\) in \(T\) by \(a_i+1\). The rows are weak because \(T\) increases across rows. For two cells in one column with labels \(p<q\), the row number increases from the cell of \(p\) to the cell of \(q\), so some consecutive step \(i\to i+1\), \(p\le i<q\), goes to a lower row. At that step (S.13) is strict, and hence the column entries are strict. Within an equality block of the sequence \(a_i\), the row numbers can never increase. A later cell in a higher row must then be farther right: otherwise it would lie weakly northwest of the earlier cell, contradicting the increasing row and column labels of \(T\). Thus standardizing the filled tableau recovers exactly \(T\). This proves the bijection.

For a fixed \(T\), write
\[
b_1=a_1,\qquad b_{i+1}=a_{i+1}-a_i-\mathbf1_{i\in\operatorname{Des}(T)}\ge0.
\]
Then
\[
\sum_{i=1}^m a_i
=\operatorname{comaj}(T)+\sum_{j=1}^m(m-j+1)b_j.
\tag{S.14}
\]
It follows that
\[
s_\nu(1,q,q^2,\ldots)
=\frac{\sum_{T\in\operatorname{SYT}(\nu)}q^{\operatorname{comaj}(T)}}
{\prod_{i=1}^m(1-q^i)}.
\tag{S.15}
\]
Substitution into (S.12) cancels exactly the factor \(1-q\), proving
\[
\sum_{d\ge0}[\,[\nu]:\operatorname{Sym}^d\mathfrak h_m\,]q^d
=\frac{\sum_{T\in\operatorname{SYT}(\nu)}q^{\operatorname{comaj}(T)}}
{\prod_{i=2}^m(1-q^i)}.
\tag{S.16}
\]
Taking the coefficient of \(q^S\) proves (S.5). For \(\mu=(m)\), the shape \(\nu\) is either a row with comajor index 0 or a column with comajor index \(\binom m2\), recovering exactly T-025.

## T-028. A single polynomial-size polytope and a support criterion

### The explicit polytope

The cells of \(\nu\) form a set \(C\) of size \(m\); write \(r(c)\) for the row number of a cell. Introduce variables
\[
X_{c,j}\quad(c\in C,\ 1\le j\le m),\qquad
\delta_j\quad(1\le j<m),\qquad
c_i\quad(2\le i\le m).
\]
There are \(m^2+2m-2\) variables. Impose
\[
0\le X_{c,j}\le1,\quad0\le\delta_j\le1,\quad c_i\ge0;
\qquad
\sum_jX_{c,j}=1\ (c\in C),\quad
\sum_cX_{c,j}=1\ (1\le j\le m).
\tag{S.17}
\]
Define the following linear forms, which introduce no new variables:
\[
\ell_c=\sum_{j=1}^m jX_{c,j},\qquad
r_j=\sum_{c\in C}r(c)X_{c,j}.
\tag{S.18}
\]
For each adjacent pair of cells in a row or column, with \(c'\) immediately right of or below \(c\), require
\[
\ell_c+1\le\ell_{c'}.
\tag{S.19}
\]
For every \(1\le j<m\), require
\[
1-m(1-\delta_j)\le r_{j+1}-r_j\le m\delta_j.
\tag{S.20}
\]
Finally require
\[
\sum_{i=2}^m i c_i+\sum_{j=1}^{m-1}(m-j)\delta_j=S.
\tag{S.21}
\]

At every integral point, (S.17) makes \(X\) a permutation assignment of the labels \(1,\ldots,m\) to the cells of \(\nu\). Equation (S.19) is exactly the standard-tableau condition. Since \(1\le r_j\le m\), (S.20) uniquely forces \(\delta_j=1\) when \(r_{j+1}>r_j\), and \(\delta_j=0\) otherwise. Thus its weighted sum in (S.21) is exactly \(\operatorname{comaj}(T)\). The remaining variables count the partitions in (S.5), without any multiplicity from the encoding. Conversely every pair counted in (S.5) gives exactly one integral point. Therefore
\[
\boxed{p_{\mu,(n)}^\lambda=\#(\mathcal P_{\mu,\lambda}\cap\mathbf Z^{m^2+2m-2}),}
\tag{S.22}
\]
where \(\mathcal P_{\mu,\lambda}\) is the explicitly displayed polytope (S.17)–(S.21). It is bounded: the \(X,\delta\) variables lie in \([0,1]\), and \(0\le c_i\le S/i\) follows from (S.21). Its number of variables, constraints, and nonzero matrix entries is polynomial in \(m\). Its coefficients have bit length \(O(\log(m(n+1)+1))\). This gives a direct \(\#P\) verifier in ordinary explicit partition encoding, with no algebra precomputation. As in T-025, a nonzero \(\beta\) supplies at least \(m-1\) explicitly listed parts of \(\lambda\); for \(\beta=0\), the answer is directly 1 for \(\mu=(m)\) and 0 for the other outer shapes.

### The exact nonvanishing criterion

Define
\[
b(\nu)=\sum_{r\ge1}(r-1)\nu_r,
\qquad d(\nu)=\#\{r:\nu_r>\nu_{r+1}\},
\qquad Q=S-b(\nu).
\tag{S.23}
\]
Here \(d(\nu)\) is the number of removable corners, equivalently the number of distinct positive part sizes. Then
\[
\boxed{
p_{\mu,(n)}^\lambda>0
\Longleftrightarrow
\left[Q=0\right]\ \text{or}\ \left[Q\ge2\right]\ \text{or}\
\left[Q=1\text{ and }d(\nu)\ge2\right].}
\tag{S.24}
\]

To prove this, the smallest exponent in the semistandard generating function \(s_\nu(1,q,q^2,\ldots)\) is \(b(\nu)\), occurring once: in row \(r\), column strictness forces every entry to be at least \(r\), and filling that row entirely by \(r\) attains the bound. A semistandard tableau of weight \(b(\nu)+1\) must increase exactly one cell of this minimum tableau by 1. Row weakness permits this only at the rightmost cell of a row; column strictness permits it only when no cell lies below it. These are exactly the \(d(\nu)\) removable corners, and all such increases are valid. Thus
\[
s_\nu(1,q,q^2,\ldots)=q^{b(\nu)}(1+d(\nu)q+O(q^2)).
\]
Multiplication by \(\prod_{i=1}^m(1-q^i)=1-q+O(q^2)\) in (S.15) gives
\[
\sum_Tq^{\operatorname{comaj}(T)}
=q^{b(\nu)}(1+(d(\nu)-1)q+O(q^2)).
\tag{S.25}
\]
It follows that the minimum comajor index is \(b(\nu)\), attained once, and the number of tableaux with comajor index \(b(\nu)+1\) is \(d(\nu)-1\). No sum of parts \(2,\ldots,m\) is 1, whereas every integer at least 2 is such a sum because \(m\ge3\). Formula (S.5) now proves every case of (S.24): the unique minimum tableau gives all \(Q=0\) and \(Q\ge2\), and at \(Q=1\) only the tableaux counted by \(d(\nu)-1\) can contribute.

This is an integer-arithmetic polynomial-time support test. When \(\beta\) is odd, the statistic can be computed directly on \(\mu\), since
\[
b(\mu')=\sum_i\binom{\mu_i}{2},\qquad d(\mu')=d(\mu).
\tag{S.26}
\]
The first identity counts pairs of cells in the same row; the second follows by exchanging the horizontal and vertical boundary corners of the Ferrers diagram. Thus a long transpose need not be explicitly expanded to test support. Compressed strings of repeated parts can also be handled by arithmetic sums over their blocks for this support test; the \(O(m^2)\) tableau polytope itself uses the ordinary explicit size convention stated above.

## Exact input identities and validation

The only representation-theoretic inputs are polynomial Cauchy/Howe duality, the refined balanced-weight identity T-003, and the Frobenius character identity from Schur–Weyl duality. Their action on the relevant module is specified in (S.4), (S.8), and (S.10). The exact primary locator supplied with the task for the balanced-weight realization is Landsberg, *Geometric Complexity Theory: an introduction for geometers*, subsection “A duality theorem for weight zero spaces and plethysms,” theorem `gaythm`, source lines 766–798. The Frobenius evaluation used in (S.12) is displayed explicitly, and (S.13)–(S.15) give a complete proof of the needed principal-specialization tableau identity. No generic coefficient oracle, coinvariant decomposition, or unproved positivity assertion enters the argument.

The cycle-trace averaging in (S.11)–(S.12) is the character-valued Molien formula: R. P. Stanley, *Invariants of finite groups and their applications to combinatorics*, Bull. Amer. Math. Soc. **1** (1979), 475–511, Theorem 2.1 and its complete proof on printed pp. 479–480. The primary author-hosted text was read in this run: https://math.mit.edu/~rstan/pubs/pubfiles/38.pdf. The tableau numerator is a classical representation-theoretic object; the report proves its precise comajor convention directly, rather than importing a statistic with a different tableau convention.

The author and the rectangular agent have each read the complete T-027 and T-028 proofs; their actual events are recorded separately in the respective `CHECK_EVENTS.tsv` files. The independent reader checked both directions of standardization, the comajor convention, the exact module twist, all polytope constraints, and the support argument. The same agent independently expanded the outer Schur power-sum cycle index and used Murnaghan–Nakayama to test all 231 coefficients, and their support, for every outer \(\mu\) and every admissible end shape with \(m=3,n=0,\ldots,4\) and \(m=4,n=0,\ldots,3\). Every comparison passed. Code: `work/rectangular/verify_endsector_schur.py`; receipt: `work/rectangular/ENDSECTOR_SCHUR_INDEPENDENT_CHECK.tsv`. These computations are additional checks, not replacements for the proof readings.


# A face-dimension obstruction to one multigraded polynomial normalization

## T-029. Statement

Let \(m\ge4\), \(E=F=\mathbf Q^m\), and
\[
A_m=\left(\operatorname{Sym}(E\otimes F)^{U_F}\right)^{T_0\rtimes S_m},
\tag{N.1}
\]
with the exact literal row-permutation action and determinant-one row torus used in T-002, T-024, and G-009. Grade this algebra by the full right dominant weight, expressed in the independent fundamental weights
\[
\omega_j=(1^j,0^{m-j}),\qquad 1\le j\le m.
\]
Then there is no polynomial subalgebra
\[
\mathbf Q[f_1,\ldots,f_{\binom m2+1}]\subset A_m
\tag{N.2}
\]
over which \(A_m\) is finite and whose generators \(f_i\) are all homogeneous for this full \(\mathbf N^m\)-grading. Equivalently, \(A_m\) has no homogeneous system of parameters for the full dominant-weight grading. The conclusion concerns precisely the displayed grading and finiteness morphism. G-009's finite standard-monomial polytope construction, T-024–T-028's direct face formulas, and normalizations using a coarser grading remain available with their stated proofs.

The original rank-four instance was proposed by the root agent; the argument below proves the general rank statement. No claim of historical novelty is made.

## Proof

### 1. Exact flag-face dimensions

Put \(r=m-1\). For \(J\subseteq\{1,\ldots,r\}\), let \(C_J\) be the subalgebra of \(\operatorname{Sym}(E\otimes F)^{U_F}\) with dominant degrees supported in \(J\cup\{m\}\). Thus the determinant degree is retained in every face. As in the generation proof of T-024, \(C_J\) is generated by all first-column flag minors of sizes \(j\in J\), together with the full determinant \(z\): their products give a nonzero vector in every permitted irreducible Cauchy summand, and left \(GL(E)\)-stability supplies that entire summand.

For \(J\ne\varnothing\), write \(\operatorname{Fl}_J(E)\) for the variety of nested subspaces with dimensions the elements of \(J\). A dense open part of \(\operatorname{Spec}C_J\) consists of such a partial flag, a nonzero exterior-volume vector for each selected subspace, and a nonzero full determinant. Every such set of data is realized by an adapted basis of \(E\): at each newly selected dimension, rescale a newly introduced basis vector to fix that exterior volume; since the previous selected dimensions are smaller, their volumes remain fixed. The final basis vector fixes the full determinant. Conversely, the nonzero decomposable exterior vectors recover the flag and its selected volumes. Hence
\[
\dim C_J=\dim\operatorname{Fl}_J(E)+|J|+1.
\tag{N.3}
\]
This can also be read on the usual affine chart for the partial flag, where the selected volume choices form a product of \(|J|+1\) multiplicative groups. For \(J=\varnothing\), \(C_J=\mathbf Q[z]\) has dimension 1.

We justify the torus dimension subtraction by an explicit localization. Let \(f_J\) be the product of all flag minors of the selected sizes. It is nonzero in the matrix polynomial ring. For each fixed size \(j\), every row occurs in exactly \(\binom{m-1}{j-1}\) minors, so their product has equal row weights and is fixed by \(T_0\). Thus \(f_J\) is \(T_0\)-invariant. In \((C_J)_{f_J}\), every selected minor is a unit.

Let \(L_J\) be the lattice generated by their \(T_0\)-weights. It has rank \(r\). Indeed, choose any \(j\in J\). For any two different indices \(a,b\), choose a \(j\)-subset containing \(a\) and not \(b\). Replacing \(a\) by \(b\) in that subset shows that the difference of two selected minor weights is \(\varepsilon_a-\varepsilon_b\). These differences span rank \(m-1\) on the determinant-one torus.

Choose a \(\mathbf Z\)-basis of \(L_J\), and realize each basis weight by a Laurent monomial \(v_i\) in the now invertible minors. Every homogeneous element of \((C_J)_{f_J}\) can be multiplied by a unique Laurent monomial in the \(v_i\) to have weight zero. Distinct exponent vectors in the \(v_i\) have distinct weights. Consequently multiplication gives the exact algebra isomorphism
\[
(C_J)_{f_J}
\simeq ((C_J)_{f_J})^{T_0}
[v_1^{\pm1},\ldots,v_r^{\pm1}].
\tag{N.4}
\]
No assertion about generic closed orbits is needed for this isomorphism. Since \(f_J\) is invariant,
\(((C_J)_{f_J})^{T_0}=((C_J)^{T_0})_{f_J}\). Taking dimensions in (N.4) and using the dense nonempty principal open gives
\[
\dim (C_J)^{T_0}=\dim C_J-r\qquad(J\ne\varnothing).
\tag{N.5}
\]
The finite group \(S_m\) preserves each face. Its invariant inclusion is integral: every element satisfies its monic orbit polynomial. Hence passing to \(S_m\)-invariants preserves dimension. If \(A_J\) is the corresponding face algebra of \(A_m\), then
\[
d(J):=\dim A_J
=\begin{cases}
1,&J=\varnothing,\\
1+|J|+\dim\operatorname{Fl}_J(E)-r,&J\ne\varnothing.
\end{cases}
\tag{N.6}
\]
In the empty case, the invariant algebra is \(\mathbf Q[z^2]\), since odd row permutations negate \(z\).

The projective flag dimension has a particularly useful exact count. A positive root of type \(A_r\) is an interval \([a,b]\subseteq[1,r]\). It contributes to \(\dim\operatorname{Fl}_J(E)\) precisely when its interval meets \(J\). To verify this directly, cut \(1,\ldots,m\) into consecutive blocks at the positions in \(J\). The flag dimension is the sum of products of the sizes of distinct blocks. This counts pairs of indices in different blocks, or equivalently intervals crossing at least one selected cut. Therefore
\[
d(J)=1+|J|+
\sum_{I\text{ a nonempty interval in }[1,r]}\mathbf1_{I\cap J\ne\varnothing}
-r\mathbf1_{J\ne\varnothing}.
\tag{N.7}
\]
In particular, \(d([1,r])=\binom m2+1\), the dimension used in (N.2).

### 2. Restriction of a finite homogeneous normalization to every face

Assume that (N.2) exists. For a homogeneous generator \(f_i\), define its root support to be the set of indices in \(\{1,\ldots,r\}\) with nonzero fundamental-weight coefficient in its degree; the determinant coefficient is ignored in this support. Let \(c_S\) count generators with exact root support \(S\subseteq[1,r]\).

For a face \(J\), retain the polynomial generators whose root supports lie in \(J\). They remain algebraically independent in \(A_J\). Moreover, \(A_J\) is finite over their polynomial subalgebra. To prove this, choose finitely many homogeneous module generators for the assumed finite extension (N.2). Such a choice exists by taking homogeneous components of a finite generating set. In any expression of a face-degree element in terms of these generators, take its homogeneous component of that degree. Since the degree monoid is \(\mathbf N^m\), a summand with a positive coordinate outside the face cannot contribute. Thus only module generators and polynomial variables with degrees in that face remain. These finitely many module generators prove finiteness after restriction.

Equality of dimensions in this finite extension now forces
\[
d(J)=\sum_{S\subseteq J}c_S\qquad\text{for every }J\subseteq[1,r].
\tag{N.8}
\]
In particular all the numbers obtained by Boolean-lattice Möbius inversion of \(d\) must be nonnegative integers.

### 3. The forced negative generator count

For nonempty \(S\subseteq[1,r]\), invert (N.7). The constant 1 contributes zero. The term \(|J|\) contributes 1 for a singleton \(S\) and zero otherwise. For a fixed interval \(I\),
\[
\sum_{J\subseteq S}(-1)^{|S|-|J|}\mathbf1_{I\cap J\ne\varnothing}
=\begin{cases}(-1)^{|S|+1},&S\subseteq I,\\0,&S\not\subseteq I.\end{cases}
\tag{N.9}
\]
Indeed, replace the indicator by \(1-\mathbf1_{J\subseteq S\setminus I}\) and sum the resulting binomial identity. The analogous transform of \(\mathbf1_{J\ne\varnothing}\) is \((-1)^{|S|+1}\). Finally, the number of intervals containing \(S\) is
\(\min(S)(r-\max(S)+1)=\min(S)(m-\max(S))\). Hence (N.8) forces
\[
\boxed{
c_S=\mathbf1_{|S|=1}
+(-1)^{|S|+1}\left(\min(S)(m-\max(S))-(m-1)\right).}
\tag{N.10}
\]
Take \(S=\{1,2,m-1\}\), which has three distinct elements for every \(m\ge4\). Then
\[
c_S=1-(m-1)=2-m<0,
\]
contradicting its definition as a number of generators. This proves T-029.

### The rank-four instance

For \(m=4\), (N.6) gives
\[
d(\varnothing)=1,\quad d(\{1\})=d(\{3\})=2,\quad d(\{2\})=3,
\quad d(\{i,j\})=5,\quad d(\{1,2,3\})=7.
\]
The forced counts on proper supports are
\[
c_\varnothing=1,\ c_{\{1\}}=c_{\{3\}}=1,\ c_{\{2\}}=2,
\quad c_{\{1,2\}}=c_{\{2,3\}}=1,\ c_{\{1,3\}}=2.
\]
They already total 9, whereas the full algebra has dimension 7; the missing full-support count is \(-2\). This is the original rank-four obstruction in explicit numerical form.

## Provenance and scope

The flag-minor and Cauchy construction is the same exact morphism used in T-002, T-024, and G-009. The flag dimensions, invariant localization, finite-face restriction, and Möbius contradiction are proved in full above. This theorem excludes a specific global construction by one polynomial subring homogeneous in every highest-weight coordinate. It does not leave the existence of a terminating positive lattice count unresolved: G-009–G-011 already provide such counts through their specified algebra and module presentations, and the direct formulas T-025 and T-028 provide polynomial-size descriptions on their respective faces.


# The paired-row face in outer degree four

## T-030. Exact small presentation and all five outer Schur coefficients

Let \(\mu\vdash4\), \(n\ge0\), and
\[
\lambda=(a,a,b,b)\vdash4n,\qquad a\ge b\ge0.
\]
Then \(a+b=2n\), so
\[
r=(a-b)/2=n-b\in\mathbf Z_{\ge0}.
\]
Define \(P(q)=\#\{(u,v)\in\mathbf Z_{\ge0}^2:2u+3v=q\}\), with \(P(q)=0\) for \(q<0\). The complete coefficient list is
\[
\boxed{
\begin{array}{c|c}
\mu & p_{\mu,(n)}^{(a,a,b,b)}\\ \hline
(4)&P(r-3(b\bmod2))\\
(1,1,1,1)&P(r-3((b+1)\bmod2))\\
(2,2)&\lfloor(r+2)/3\rfloor\\
(3,1),(2,1,1)&0.
\end{array}}
\tag{P.1}
\]
The two occurrences of \(b\) in the parity shifts can equivalently be replaced by \(n\). The equality of those forms is proved below by an explicit solution bijection. Every nonzero entry is a count in one bounded two-variable rational polytope; the \((2,2)\) entry counts \(u+3v=r-1\), \(u,v\ge0\). In particular its support is exactly \(r\ge1\); each of the first two entries is positive exactly when its argument is 0 or at least 2.

The symmetric-outer algebra on this face also has the following small presentation:
\[
\boxed{
A_4^{\{2\}}
\simeq\mathbf Q[e,D,Z,W]
/(27W^2+Z(D^2+4e^3)).}
\tag{P.2}
\]
It is free with basis \(1,W\) over \(\mathbf Q[e,D,Z]\). This is a different flag face from the equal-middle-row family T-024–T-028; its exact relation to the same balanced Howe algebra is proved next. No novelty claim is made for these classical small-outer-degree coefficients.

### 1. The Plücker morphism and exact torus quotient

Let \(X\) be a \(4\times4\) matrix of variables. Put
\[
p_{ij}=X_{i1}X_{j2}-X_{i2}X_{j1}\quad(i<j),\qquad z=\det X,
\]
and extend \(p_{ji}=-p_{ij}\). The flag subalgebra of right weights \((a,a,b,b)\) is generated by the six \(p_{ij}\) and \(z\). Indeed these are the left modules \(\Lambda^2\mathbf Q^4\) and \(\det\), and products of their highest vectors give every permitted irreducible Cauchy summand, exactly as in T-024 and T-029. The exact presentation is
\[
C_{\{2\}}\simeq
\mathbf Q[p_{12},p_{13},p_{14},p_{23},p_{24},p_{34},z]
/(p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}).
\tag{P.3}
\]
The relation follows by expanding a decomposable two-vector. For the converse, on the open set \(p_{12}\ne0\), the first two columns
\[
c_1=(1,0,-p_{23}/p_{12},-p_{24}/p_{12})^\mathsf T,
\quad c_2=(0,p_{12},p_{13},p_{14})^\mathsf T
\]
have precisely the prescribed minors, with \(p_{34}\) determined by the displayed relation. Choose two additional columns with any desired determinant, by first choosing a complement to \(\langle c_1,c_2\rangle\) and then rescaling its last vector. Thus the matrix morphism reaches this dense open set for arbitrary \(z\). The quadratic is irreducible by Gauss's lemma, regarding it as linear in \(p_{34}\), since its coefficient \(p_{12}\) is relatively prime to its constant term. Density therefore proves that its ideal is the entire kernel.

In a monomial \(\prod p_{ij}^{a_{ij}}z^t\), row \(i\) has degree \(t+\sum_{j\ne i}a_{ij}\). Equality of the four row degrees is equivalent to
\[
a_{12}=a_{34},\qquad a_{13}=a_{24},\qquad a_{14}=a_{23}.
\tag{P.4}
\]
For example, adding the first two row equations and subtracting the last two yields \(2(a_{12}-a_{34})=0\); the other two equalities follow similarly, and they also imply equal row sums. Hence the torus-invariant polynomial ring before the Plücker quotient is freely generated by
\[
t_1=p_{12}p_{34},\qquad
t_2=-p_{13}p_{24},\qquad
t_3=p_{14}p_{23},\qquad z.
\tag{P.5}
\]
Their monomials have distinct exponent vectors in the original six variables. The relation in (P.3) is torus-invariant, so the exact weight-zero quotient gives
\[
\boxed{B_{\{2\}}\simeq\mathbf Q[t_1,t_2,t_3,z]/(t_1+t_2+t_3).}
\tag{P.6}
\]
Each \(t_i\) has balanced degree 1 and right weight \(2\omega_2=(2,2,0,0)\), while \(z\) has degree 1 and weight \(\omega_4\). Consequently the component \((n,(a,a,b,b))\) is exactly \(z^b\) times the degree-\(r\) part in the \(t_i\).

### 2. The permutation action and its exact representation

The group \(S_4\) permutes the three perfect matchings
\(12|34,13|24,14|23\), giving a surjection
\(\pi:S_4\to S_3\) with kernel the Klein four group. Directly on the generators \((12),(23),(34)\), the oriented products (P.5) transform by minus the corresponding matching permutation. For instance,
\[
(12):(t_1,t_2,t_3)\longmapsto(-t_1,-t_3,-t_2),
\qquad
(23):(t_1,t_2,t_3)\longmapsto(-t_2,-t_1,-t_3).
\]
The action of \((34)\) on the triple is the same as that of \((12)\). Thus for every \(\sigma\in S_4\),
\[
\sigma t_i=\operatorname{sgn}(\sigma)t_{\pi(\sigma)(i)},
\qquad \sigma z=\operatorname{sgn}(\sigma)z,
\qquad\operatorname{sgn}(\pi(\sigma))=\operatorname{sgn}(\sigma).
\tag{P.7}
\]
Let \(\mathfrak h_3\) be the ordinary two-dimensional standard representation of \(S_3\). Equations (P.6)–(P.7) first give the actual module
\[
(S_{(a,a,b,b)}\mathbf Q^4)_{(n^4)}
\simeq\operatorname{Inf}_{S_3}^{S_4}
\left(\operatorname{sgn}^{b}\otimes
\operatorname{Sym}^{r}(\mathfrak h_3\otimes\operatorname{sgn})\right).
\tag{P.8}
\]
There is an explicit rational intertwiner \(J:\mathfrak h_3\otimes\operatorname{sgn}\to\mathfrak h_3\). Equip the standard plane with its nondegenerate invariant dot product and any nonzero alternating form \(\Omega\). Define \(J\) by \(\langle Jv,w\rangle=\Omega(v,w)\). It is invertible, and the determinant of the standard representation is the sign character, so
\(J\rho(g)=\operatorname{sgn}(g)\rho(g)J\). This is exactly the required intertwining identity. Applying \(\operatorname{Sym}^rJ\) in (P.8) gives
\[
\boxed{
(S_{(a,a,b,b)}\mathbf Q^4)_{(n^4)}
\simeq\operatorname{Inf}_{S_3}^{S_4}
(\operatorname{sgn}^{b}\otimes\operatorname{Sym}^{r}\mathfrak h_3).}
\tag{P.9}
\]
Alternatively, pulling the degree-\(r\) sign outside the symmetric power in (P.8) gives the equally exact twist \(\operatorname{sgn}^{r+b}=\operatorname{sgn}^{n}\). Both realizations are related by the specified invertible intertwiner.

The irreducible \(S_4\)-modules factoring through \(\pi\) are the trivial module \([(4)]\), the sign module \([(1^4)]\), and the matching-plane module \([(2,2)]\). The last identification follows, for instance, from its character \((2,0,2,-1,0)\) on the cycle types \(1^4,2\,1^2,2^2,3\,1,4\), the character of \([(2,2)]\). The two remaining Specht modules are the standard \([(3,1)]\) and its sign twist \([(2,1,1)]\). The Klein four group acts transitively on the four letters, so its fixed space in the four-dimensional permutation representation consists only of constants; its fixed space in the standard quotient is zero. Its sign is trivial, so the sign twist also has no fixed vector. Consequently neither remaining Specht module can occur in (P.9).

For \(S_3\), formula (S.16) of T-027 gives the multiplicity generating functions in \(\operatorname{Sym}(\mathfrak h_3)\):
\[
\frac1{(1-q^2)(1-q^3)},\qquad
\frac{q^3}{(1-q^2)(1-q^3)},\qquad
\frac{q+q^2}{(1-q^2)(1-q^3)}
=\frac q{(1-q)(1-q^3)}
\tag{P.10}
\]
for the trivial, sign, and standard modules respectively. Apply (P.9), then the refined balanced Howe identity (S.10). The first two series give the parity shifts in (P.1), and the third gives \(u+3v=r-1\), with \(\lfloor(r+2)/3\rfloor\) solutions. This proves (P.1).

For a purely lattice verification of the replacement \(b\mapsto n\), observe that \(n-b=r\). When \(r\) is even, the parities agree. When \(r\) is odd, every solution of \(2u+3v=r\) has \(v\) odd and therefore \(v\ge1\). The bijection \((u,v)\mapsto(u,v-1)\) proves \(P(r)=P(r-3)\), including the empty small case. This is exactly the equality needed when the two parity shifts differ.

### 3. The invariant-algebra presentation

In the trace-free triple (P.6), let
\[
e=e_2(t_1,t_2,t_3),\quad f=e_3(t_1,t_2,t_3),
\quad D=(t_1-t_2)(t_1-t_3)(t_2-t_3).
\]
The alternating subgroup of \(S_3\) fixes a free rank-two algebra over \(\mathbf Q[e,f]\), generated by \(D\) with
\[
D^2=-4e^3-27f^2.
\tag{P.11}
\]
This is exactly the alternating/symmetric decomposition proved in T-024, specialized to three variables. Under the odd signed permutation action (P.7), \(e,D\) are fixed and \(f,z\) are negated. Eliminate \(f^2\) using (P.11). The sign-fixed monomials form a free basis \(1,zf\) over \(\mathbf Q[e,D,z^2]\). Setting \(Z=z^2\) and \(W=zf\) gives precisely (P.2), including its unique monic quadratic relation in \(W\) after division by 27.

The generator degrees \((n;\lambda)\) are
\[
\begin{array}{c|c|c}
e&2&(4,4,0,0)\\
D&3&(6,6,0,0)\\
Z&2&(2,2,2,2)\\
W&4&(7,7,1,1).
\end{array}
\tag{P.12}
\]
In a standard basis monomial \(e^uD^vZ^wW^\varepsilon\), \(\varepsilon\in\{0,1\}\), the final part is \(b=2w+\varepsilon\), while \(r=2u+3v+3\varepsilon\). This directly recovers the symmetric-outer count \(P(r-3(b\bmod2))\), with an explicit basis bijection.

## Checks and relation to the global question

The Plücker morphism, its dense chart, the exact torus quotient, the signed matching action, the intertwiner \(J\), and the coefficient and algebra presentations are all proved above. The only shared input is the already specified Cauchy/Howe and Specht-module dictionary T-002–T-003. This face admits a homogeneous polynomial base of dimension three, consistent with its dimension in T-029; the global obstruction in T-029 arises from trying to choose one such base simultaneously across all faces.

An independent calculation using the cycle-index expansion and the Murnaghan–Nakayama rule passed all 140 coefficients for these paired-row shapes and all five outer partitions through inner degree 6. It is recorded in `work/rectangular/OUTER4_PAIRED_AND_PROPER_CHECK.tsv`, with reproduction code `work/rectangular/verify_outer4_faces.py`. The independent agent also read and checked the complete proof above.

For precise historical attribution, T. Kuppel, *Asymptotics of plethysm*, Math. Z. **311**, article 84 (2025), [Theorem 5, its proof, and Remark 2](https://link.springer.com/article/10.1007/s00209-025-03879-4), treats the paired-row exceptional family and states that its occurring Specht modules factor through the matching quotient \(S_4\to S_3\). Those passages were opened and read in this run. The explicit signed-coordinate presentation (P.3)–(P.12) supplies the algebra morphism and fixes all determinant shifts for the formulas here.


# Direct positive formulas on every proper fundamental face of outer degree four

## T-031. Statement and explicit formulas

Let \(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\vdash4n\), allowing trailing zero parts. Define the fixed binary-quartic count
\[
\begin{aligned}
F_4(N,K)=\sum_{\varepsilon=0}^1\#\{(a,b,c,d)\in\mathbf Z_{\ge0}^4:\quad
&N=a+2b+2c+3d+3\varepsilon,\\
&K=2b+4c+6d+3\varepsilon\}.
\end{aligned}
\tag{F.1}
\]
Set it equal to zero when \(N<0\), \(K<0\), or \(K>2N\). T-021–T-022 prove the exact algebra map and basis giving
\(F_4(N,K)=a_{4,N}^{(4N-K,K)}\) for valid indices. Each term in (F.1) is one bounded four-variable polytope.

For the lower face \(\lambda_3=\lambda_4=t\), put \(N=n-t\), \(K=\lambda_2-t\). Then
\[
\boxed{
a_{4,n}^{\lambda}=
\begin{cases}
F_4(N,K),&t\text{ even},\\
F_4(N-3,K-6),&t\text{ odd}.
\end{cases}}
\tag{F.2}
\]
The invalid-index convention includes every boundary case.

For the upper face \(\lambda_1=\lambda_2=H\), put \(N=H-n\), \(K=H-\lambda_3\). Then
\[
\boxed{
a_{4,n}^{\lambda}=
\begin{cases}
F_4(N,K),&H\text{ even},\\
F_4(N-3,K-6),&H\text{ odd}.
\end{cases}}
\tag{F.3}
\]

For the middle face \(\lambda_2=\lambda_3=\beta\), put
\[
R=\min(\lambda_1-\beta,\beta-\lambda_4)-6(\beta\bmod2).
\]
T-025 gives the single-polytope formula
\[
\boxed{a_{4,n}^{\lambda}
=\#\{(c_2,c_3,c_4)\in\mathbf Z_{\ge0}^3:
2c_2+3c_3+4c_4=R\}.}
\tag{F.4}
\]
Thus all proper faces of the three simple-root fundamental coordinates of \(A_4\), with every determinant shift retained, have direct bounded-polytope formulas. Indeed a proper face sets at least one of \(\lambda_1-\lambda_2\), \(\lambda_2-\lambda_3\), \(\lambda_3-\lambda_4\) equal to zero, exactly the three cases above. The formulas agree on their intersections because the proofs identify each with the same balanced Howe multiplicity. T-030 supplies another explicit presentation on the paired-row intersection.

## 1. Exact determinant shift

For any rank \(m\), a partition \(\eta\), and \(t\ge0\), the canonical highest-weight pairing identifies
\[
S_{\eta+(t^m)}E\simeq(\det E)^t\otimes S_\eta E.
\tag{F.5}
\]
One construction is to append \(t\) full-height columns to the column exterior-power realization of the Schur module. Those columns contribute \((\Lambda^mE)^{\otimes t}\); the Cartan product with the original Schur module is nonzero on its highest vector and has the displayed irreducible highest weight, giving the isomorphism. On the balanced weight \((n^m)\), this gives the exact \(S_m\)-module morphism
\[
(S_{\eta+(t^m)}E)_{(n^m)}
\simeq\operatorname{sgn}^{t}\otimes
(S_\eta E)_{((n-t)^m)},
\tag{F.6}
\]
because literal permutation matrices have determinant equal to their sign.

Apply this with \(m=4\), \(\eta=(\lambda_1-t,\lambda_2-t,0,0)\), and \(t=\lambda_3=\lambda_4\). Put \(A=\lambda_1-t\), \(B=\lambda_2-t\), \(N=n-t\). The equality \(A+B=4N\) and the partition inequalities imply \(N\ge0\) and \(0\le B\le2N\). By the refined balanced Howe identity T-003, (F.6) identifies the desired coefficient with the multiplicity of \(S_{(A,B)}\mathbf Q^2\) in
\[
\operatorname{Sym}^4(\operatorname{Sym}^N\mathbf Q^2)
\quad(t\text{ even}),\qquad
\Lambda^4(\operatorname{Sym}^N\mathbf Q^2)
\quad(t\text{ odd}).
\tag{F.7}
\]
The restriction to two variables is exact: the Schur coefficient for a partition of length at most two is unchanged by evaluating the character in two variables, while every partition of greater length vanishes there.

## 2. Binary alternants and the exact exterior-to-symmetric map

The following map works in every number \(m\) of binary slots, so we state and prove it in that form. Let \(F=\mathbf Q^2\), and write \(v_i=(a_i,b_i)\) for the variables in slot \(i\). Put
\[
[ij]=a_i b_j-a_j b_i,\qquad
\Delta_m=\prod_{1\le i<j\le m}[ij],\qquad
M=\binom m2.
\tag{F.8}
\]
The polynomial \(\Delta_m\) has degree \(m-1\) in every slot, transforms by the sign under slot permutations, and spans the \(GL(F)\)-character \((\det F)^M\).

Every alternating polynomial of equal degree \(N\) in all \(m\) slots is divisible by \(\Delta_m\). To see this, fix a pair \(i,j\). On the dense part of the bracket hypersurface where \(v_j=c v_i\), equal slot homogeneity gives
\[
f(\ldots,v_i,\ldots,c v_i,\ldots)
=c^N f(\ldots,v_i,\ldots,v_i,\ldots)=0,
\]
since interchanging the equal slots negates an alternating polynomial. The bracket \([ij]\) is an irreducible determinant polynomial, so it divides \(f\). Distinct brackets are nonassociate irreducibles in the polynomial unique factorization domain; therefore their product divides \(f\). Its quotient has equal slot degree \(N-m+1\), and is symmetric because numerator and denominator have the same permutation sign. Conversely multiplying any symmetric polynomial of that slot degree by \(\Delta_m\) produces an alternating polynomial of degree \(N\) in each slot. If \(N<m-1\), divisibility leaves a negative degree in each slot, so the alternating space is zero.

Multiplication by this explicit polynomial therefore gives the \(GL(F)\)-equivariant isomorphism
\[
\boxed{
\Lambda^m(\operatorname{Sym}^N F)
\simeq(\det F)^{\binom m2}\otimes
\operatorname{Sym}^m(\operatorname{Sym}^{N-m+1}F)
\quad(N\ge m-1),}
\tag{F.9}
\]
and the left side is zero for \(N<m-1\). The identification of alternating tensors with \(\Lambda^m\), and of symmetric tensors with \(\operatorname{Sym}^m\), is the characteristic-zero symmetrizer identification. The determinant factor in (F.9) records the actual \(GL_2\) action of \(\Delta_m\), rather than only its degree.

For \(m=4\), (F.9) shifts the inner degree by 3 and both output parts by 6. Thus the odd case of (F.7) has multiplicity
\[
[S_{(A-6,B-6)}F:\operatorname{Sym}^4(\operatorname{Sym}^{N-3}F)]
=F_4(N-3,B-6),
\tag{F.10}
\]
with value zero when \(N<3\) or \(B<6\). If these inequalities hold, \(A\ge B\) and \(A+B=4N\) automatically give a valid partition after the shift. Equations (F.7)–(F.10) prove (F.2), including its boundary conventions.

## 3. Exact complement duality and the upper face

For a rank-\(m\) space \(E\), a partition \(\lambda\) of length at most \(m\), and an integer \(H\ge\lambda_1\), define its rectangular complement
\[
\widehat\lambda=(H-\lambda_m,\ldots,H-\lambda_1).
\tag{F.11}
\]
There is a perfect equivariant pairing
\[
S_\lambda E\otimes S_{\widehat\lambda}E\longrightarrow(\det E)^H.
\tag{F.12}
\]
To construct it, place \(\lambda\) in an \(m\times H\) rectangle. Pair each column exterior power \(\Lambda^j E\) with the complementary \(\Lambda^{m-j}E\) by exterior multiplication into \(\det E\); reverse the order of the complementary columns to recover the partition (F.11). Applying the Schur/Cartan projections gives the equivariant pairing (F.12). It is nonzero: a highest column tensor and the complementary lowest column tensor wedge to a nonzero volume in every column. The two irreducible modules are contragredient after the displayed determinant twist, as their highest weights show, so Schur's lemma makes the induced pairing perfect. Equivalently,
\[
S_\lambda E\simeq(\det E)^H\otimes(S_{\widehat\lambda}E)^*.
\tag{F.13}
\]
On balanced weights this gives the exact module identity
\[
(S_\lambda E)_{(n^m)}
\simeq\operatorname{sgn}^{H}\otimes
\left((S_{\widehat\lambda}E)_{((H-n)^m)}\right)^*.
\tag{F.14}
\]
Since Specht modules are self-dual and tensoring by sign conjugates their partitions, T-003 yields the full coefficient equality
\[
p_{\mu,(n)}^\lambda
=p_{\mu^{[H]},(H-n)}^{\widehat\lambda},
\qquad
\mu^{[H]}=\begin{cases}\mu,&H\text{ even},\\\mu',&H\text{ odd}.\end{cases}
\tag{F.15}
\]
All quantities are polynomial representations: \(H\ge\lambda_1\ge n\), and \(|\widehat\lambda|=m(H-n)\). Thus the complement and the inner degree are nonnegative. Equation (F.14), not a dimension-only substitution, explains the sign and duality in (F.15).

For the upper face of rank four, take \(H=\lambda_1=\lambda_2\). Then
\[
\widehat\lambda=(H-\lambda_4,H-\lambda_3,0,0),
\qquad N=H-n,\quad K=H-\lambda_3.
\]
Its first two parts sum to \(4N\). Formula (F.15) turns the original symmetric outer coefficient into the symmetric binary coefficient when \(H\) is even and the alternating binary coefficient when \(H\) is odd. Apply (F.9) in the latter case. This proves (F.3) and all its edge cases.

## Provenance and scope

The binary-quartic presentation used in (F.1) is classical and is proved with the exact normalizer-algebra morphism in T-021–T-022; the primary Grace–Young locators and direct symbolic checks are recorded there. Formula (F.9) is the classical binary Vandermonde factorization, proved here to fix its slot grading, determinant power, and zero range. Equations (F.5) and (F.12) are the actual Schur-module maps carrying the formulas across determinant shifts and complementary partitions. The result completes all proper fundamental faces of the symmetric-outer \(A_4\) algebra. T-032–T-036 subsequently identify the full-face extension through an exact flag chart and four-point vanishing model, and T-037 completes the positive formula for every outer partition of four.

An independent exact cycle-index/Murnaghan–Nakayama calculation passed all 197 lower- and upper-face cases through inner degree 6. The receipt `work/rectangular/OUTER4_PAIRED_AND_PROPER_CHECK.tsv` also includes the 140 paired-row cases of T-030, for 337 total checks; reproduction code is `work/rectangular/verify_outer4_faces.py`. The independent proof reading checked the divisibility map, every zero-range convention, the complement pairing, and the literal determinant signs. T-032–T-034 subsequently give direct chamber formulas for every outer Schur label in \(\lambda_2\le n\) and \(\lambda_3\ge n\).


# An exact stable flag chart for every outer degree

## T-032. The algebra morphism and the balanced module

Work over \(\mathbf Q\), or extend scalars to any field of characteristic zero. Let \(m\ge2\), let \(X=(X_{ik})\) be an \(m\times m\) matrix of polynomial generators, and let
\[
R_m=\operatorname{Sym}(\mathbf Q^m\otimes\mathbf Q^m)^{U},
\qquad B_m=R_m^{T_0},
\tag{C.1}
\]
where \(U\) is the right maximal unipotent group fixing the first-column flag minors and \(T_0\) is the determinant-one diagonal group acting on the rows. The literal row permutation matrices give the \(S_m\) action. The component of right dominant weight \(\lambda\) and equal row weight \((n^m)\) is
\[
(B_m)_{n,\lambda}=(S_\lambda\mathbf Q^m)_{(n^m)},
\qquad |\lambda|=mn.
\tag{C.2}
\]
This is the same Cauchy/Howe identification as T-002–T-003. No quotient by a determinant character is made in (C.2).

Put \(x_i=X_{i1}\), \(u=\prod_i x_i\), and
\[
\mathfrak h_m=\{(a_1,\ldots,a_m):\sum_i a_i=0\}.
\]
For \(j\ge2\), write \(p_{j,I}\) for the minor with row set \(I\), \(|I|=j\), and the first \(j\) columns, in the natural increasing row order. Define the polynomial
\[
v_{j,I}=\left(\prod_{i\notin I}x_i\right)p_{j,I}.
\tag{C.3}
\]
It has row weight \((1^m)\) and right weight
\((m-j+1,1^{j-1},0^{m-j})\). The following map is an algebra isomorphism:
\[
\boxed{
\mathbf Q[u,u^{-1}]\otimes
\operatorname{Sym}(\mathfrak h_m\otimes\mathbf Q^{m-1})^{U_{m-1}}
\ \xrightarrow{\ \Phi\ }\ B_m[u^{-1}].}
\tag{C.4}
\]
The variable \(u\) maps to \(\prod_i x_i\); a first-\(\ell\)-column flag minor on \(\mathfrak h_m\) maps to the coordinates of the alternating tensor \(v_{\ell+1}\) under the explicit identification
\[
\Lambda^\ell\mathfrak h_m\longrightarrow
\mathbf1\wedge\Lambda^\ell\mathfrak h_m\subset\Lambda^{\ell+1}\mathbf Q^m,
\qquad w\longmapsto\mathbf1\wedge w,
\quad\mathbf1=(1,\ldots,1).
\tag{C.5}
\]
Thus (C.4) is \(S_m\)-equivariant, with \(u\) fixed and with the ordinary standard action on \(\mathfrak h_m\).

For every partition \(\lambda\vdash mn\) of length at most \(m\), the inverse chart embeds its balanced component into
\[
u^{n-\lambda_2}S_{(\lambda_2,\ldots,\lambda_m)}\mathfrak h_m.
\tag{C.6}
\]
In the entire chamber \(n\ge\lambda_2\), this embedding is onto. Hence
\[
\boxed{
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq S_{(\lambda_2,\ldots,\lambda_m)}\mathfrak h_m
\qquad(n\ge\lambda_2),}
\tag{C.7}
\]
as actual \(S_m\)-modules. For any \(\mu\vdash m\), the refined Howe identity therefore gives
\[
\boxed{
p_{\mu,(n)}^\lambda
=\dim\operatorname{Hom}_{S_m}
\bigl([\mu],S_{(\lambda_2,\ldots,\lambda_m)}\mathfrak h_m\bigr)
\quad(n\ge\lambda_2).}
\tag{C.8}
\]
Here the restriction of the Schur module on the right is along the specified standard representation of \(S_m\), so all normalizer signs remain part of the map.

## Proof of the chart

### 1. Flag minors and centered ratios

The algebra \(R_m\) is generated by its first-column flag minors. One way to see generation without imposing an unproved presentation is the Cauchy decomposition \(R_m=\bigoplus_\lambda S_\lambda\mathbf Q^m\), with the right highest-weight grading. Products of highest vectors in the fundamental exterior-power summands give a nonzero highest vector in every summand; the algebra generated by these summands is stable under left \(GL_m\), so it contains every entire summand. The same argument applies to the flag algebra on \(\mathfrak h_m\).

On \(u\ne0\), every \(x_i\) is invertible. For \(k\ge2\), define the ratio vector and its centered projection by
\[
w_k=(X_{1k}/x_1,\ldots,X_{mk}/x_m),\qquad
\bar w_k=w_k-\frac{1}{m}\left(\sum_i(w_k)_i\right)\mathbf1.
\tag{C.9}
\]
Dividing the rows of each flag determinant by \(x_i\) gives
\[
v_j=u\,\mathbf1\wedge w_2\wedge\cdots\wedge w_j
=\mathbf1\wedge
\bigl(u\bar w_2\wedge\bar w_3\wedge\cdots\wedge\bar w_j\bigr).
\tag{C.10}
\]
In particular these are exactly, under (C.5), the flag minors of the \((m-1)\)-column matrix
\[
F=(u\bar w_2,\bar w_3,\ldots,\bar w_m)
\quad\text{with columns in }\mathfrak h_m.
\tag{C.11}
\]
This proves that the proposed assignment respects every relation in the smaller flag algebra. Its coordinates are the polynomials (C.3), so it defines the displayed map even before localizing its smaller-flag factor. Row permutation commutes with centering and fixes \(\mathbf1,u\); this proves equivariance, including the orientation signs in the exterior coordinates.

### 2. Surjectivity after localization

Expand any element of \(R_m\) as a linear combination of monomials in flag minors and then take its torus-weight-zero component. Such monomials individually have equal row weights. Consider a balanced monomial of right weight \(\lambda\) and row degree \(n\). Replace every factor \(p_{j,I}\), \(j\ge2\), using
\[
p_{j,I}=u^{-1}\left(\prod_{i\in I}x_i\right)v_{j,I}.
\tag{C.12}
\]
The total number of flag factors of height at least two is \(\lambda_2\): in a product of fundamental highest-weight degrees it is \(\sum_{j\ge2}(\lambda_j-\lambda_{j+1})\). Every remaining \(x_i\) exponent is \(n\), because the original monomial had row degree \(n\). Therefore the result is precisely
\[
u^{n-\lambda_2}\times\text{a monomial of smaller flag degree }
(\lambda_2,\ldots,\lambda_m).
\tag{C.13}
\]
The same substitution applies after multiplying by any power of \(u^{-1}\). Since \(u\) is invariant, taking the torus-weight-zero part commutes with its localization. Equation (C.13) proves surjectivity in (C.4) and the component assertion (C.6).

### 3. Injectivity by an explicit dense chart

Prescribe a nonzero scalar \(u_0\) and any matrix \(F=(f_1,\ldots,f_{m-1})\) with columns in \(\mathfrak h_m\). Choose nonzero \(x_i\) with product \(u_0\), and set
\[
X_{i1}=x_i,\qquad
X_{i2}=x_i(f_1)_i/u_0,\qquad
X_{ik}=x_i(f_{k-1})_i\quad(3\le k\le m).
\tag{C.14}
\]
All ratio vectors are centered, and (C.11) recovers the prescribed \(F\) exactly. Hence a Laurent polynomial in \(u\) with coefficients in the smaller flag algebra that vanishes after \(\Phi\) vanishes on all \((u_0,F)\). The smaller flag algebra is defined as its polynomial subalgebra on such matrices, and nonzero scalars are Zariski dense. Thus the Laurent polynomial was zero. This proves injectivity.

### 4. The stable chamber and the exact extension condition

The smaller flag component of degree \((\lambda_2,\ldots,\lambda_m)\) is the irreducible Schur module displayed in (C.6). When \(n-\lambda_2\ge0\), each element of this component maps to a polynomial in the generators (C.3), multiplied by a nonnegative power of the polynomial \(u\). Its right weight is \(\lambda\): the tail coordinates are the smaller flag degree and the first coordinate is forced by total size \(mn\). It therefore belongs to \((B_m)_{n,\lambda}\). This proves surjectivity in (C.7); injectivity and equivariance follow from (C.4).

For completeness the same chart gives a precise, unconditional description outside the chamber. Put \(k=\max(0,\lambda_2-n)\), and for an element \(F\) of the tail Schur module use \(F(v(X))\) to denote its polynomial image under (C.3) and (C.5). Then
\[
\boxed{
(B_m)_{n,\lambda}\simeq
\{F\in S_{(\lambda_2,\ldots,\lambda_m)}\mathfrak h_m:
u^k\mid F(v(X))\text{ in }\mathbf Q[X_{ik}]\}.}
\tag{C.15}
\]
The isomorphism sends \(F\) to \(u^{n-\lambda_2}F(v(X))\). Polynomiality is exactly the indicated divisibility in a polynomial ring. If the quotient is polynomial, its rational \(U\)-invariance and balanced torus weight are equalities of rational functions and hence polynomial identities; thus it belongs to \(B_m\). This proves both directions. Divisibility does not depend on the chosen expression of \(F\), since the smaller flag relations map to zero. Since \(u\) is \(S_m\)-fixed, the subspace in (C.15) is \(S_m\)-stable.

## Scope, provenance, and the next finite-group map

The chart supplies an explicit algebra morphism behind the classical first-row stability phenomenon. The general stability literature includes M. Brion, *Stable properties of plethysm: on two conjectures of Foulkes*, Manuscripta Math. **80** (1993), 347–371, [DOI 10.1007/BF03026558](https://doi.org/10.1007/BF03026558). The publisher abstract and bibliographic record were opened in this run; the complete 1993 text was not accessible there. Consequently no unverified exact theorem locator is being used to justify (C.4)–(C.15): the whole algebra and component proof is given above. T. Kuppel, *Asymptotics of plethysm*, Math. Z. **311**, article 84 (2025), [§2.3, Theorem 3](https://link.springer.com/article/10.1007/s00209-025-03879-4), records Brion's §2.6, Corollary 1 as a general coefficient-stability result; that quoted result concerns the stated coefficient sequence, while (C.7) specifies the actual module and its map.

The remaining map in the stable chamber is precisely restriction along \(S_m\to GL(\mathfrak h_m)\). For \(m=4\), this factors through the explicitly sign-twisted orthogonal representation of dimension three. T-033–T-034 compute that restriction by classical \(GL_3\)-to-\(SO_3\) branching and a five-class character calculation, yielding small positive polytopes. T-035–T-037 then complete the extension outside the chamber through four flag fibers and two quadratic generators; T-037 gives the full outer-four formula with at most108 fixed polytopes in at most5 variables. For general \(m\), (C.15) states exactly what polynomial extension imposes outside this chart chamber. G-009–G-011 already provide terminating positive counts in all degrees; the direct uniform extension question after T-037 lies beyond outer degree four.



# Small positive chamber formulas in outer degree four

## T-033. The two exact branching steps

Let \(W=\mathfrak h_4\otimes\operatorname{sgn}\), where \(\mathfrak h_4\) is the three-dimensional standard representation of \(S_4\). Its invariant dot product is nondegenerate, and
\(\det(W)=\operatorname{sgn}\cdot\operatorname{sgn}^3=1\). Thus its actual representation map factors as
\[
S_4\longrightarrow SO(W)\subset GL(W).
\tag{H.1}
\]
Over \(\mathbf C\), write \(H_L\) for the irreducible \(SO_3\)-module of angular momentum \(L\), with character \(\sum_{j=-L}^L z^j\) on \(\operatorname{diag}(z,1,z^{-1})\).

For nonnegative integers \(c,b\), set
\[
A=\max(c,b),\qquad s=\min(c,b).
\]
The exact restriction of \(S_{(c+b,b)}W\) to \(SO(W)\) is the following direct sum, with every pair \((K,L)\) providing one summand:
\[
\boxed{
S_{(c+b,b)}W\big|_{SO(W)}
\simeq
\bigoplus_{\substack{K=s,s-2,\ldots\\K>0}}
\ \bigoplus_{L=K}^{K+A}H_L
\ \oplus\
\begin{cases}
\displaystyle\bigoplus_{j=0}^{\lfloor A/2\rfloor}H_{A-2j},
&s\text{ even},\\[2mm]
0,&s\text{ odd}.
\end{cases}}
\tag{H.2}
\]
This is the classical Elliott branching rule, proved below in the precise convention used here.

For each \(\tau\vdash4\), define the finite tag sets
\[
\begin{array}{c|c}
\tau&E_\tau\\ \hline
(4)&\{0,9\}\\
(1,1,1,1)&\{3,6\}\\
(2,2)&\{2,4,5,7\}\\
(3,1)&\{2,3,4,5,6,7\}\\
(2,1,1)&\{1,3,4,5,6,8\}.
\end{array}
\tag{H.3}
\]
Then the second restriction in (H.1) has the exact positive multiplicity formula
\[
\boxed{
[\tau:H_L]
=\sum_{e\in E_\tau}
\#\{(x,y)\in\mathbf Z_{\ge0}^2:4x+6y=L-e\}.}
\tag{H.4}
\]
An equation with negative right side contributes zero.

### 1. Full character proof of the Elliott rule

The three-variable Weyl determinant, specialized to \((z,1,z^{-1})\), gives
\[
\chi_{c,b}(z)
=z^{-(c+b)}
\frac{(1-z^{c+1})(1-z^{b+1})(1-z^{c+b+2})}
{(1-z)^2(1-z^2)}.
\tag{H.5}
\]
For example this follows by dividing the alternant with exponents \(c+b+2,b+1,0\) by the alternant with exponents \(2,1,0\), then factoring their Vandermonde products after substitution. Formula (H.5) is symmetric in \(c,b\), so one may put \(c=A,b=s\) in the ensuing identity without changing the character.

Let \(P(z)\) be the sum of \(z^L\) over all the pairs \((K,L)\) in (H.2), with repetitions retained. Finite geometric summation yields
\[
P(z)=
\frac{z-z^{A+2}-z^{s+2}+z^{A+s+3}
+\delta(1-z)^2}{(1-z)(1-z^2)},
\quad
\delta=
\begin{cases}1,&A,s\text{ both even},\\0,&\text{otherwise}.\end{cases}
\tag{H.6}
\]
Here the positive-\(K\) terms sum
\(\sum_{j=0}^{\lfloor(s-1)/2\rfloor}
z^{s-2j}(1-z^{A+1})/(1-z)\);
when \(s\) is even, the final band contributes
\(\sum_{j=0}^{\lfloor A/2\rfloor}z^{A-2j}\).
Adding these two displayed finite geometric series gives (H.6), separately for the parities of \(A,s\).

Now
\[
P(z)-z^{-1}P(z^{-1})
=(1-z^{-1})\chi_{c,b}(z).
\tag{H.7}
\]
For a direct verification, the \(\delta\) term in (H.6) equals \(\delta/(1+z)\), whose contribution to the left side vanishes. The remaining numerator of that side, with denominator \((1-z)(1-z^2)\), is
\[
-z^{A+2}-z^{s+2}+z^{A+s+3}
+z^{-A}+z^{-s}-z^{-A-s-1}.
\]
Expanding the numerator of the right side using (H.5) gives exactly the same six terms. Finally,
\[
(1-z^{-1})\sum_{j=-L}^{L}z^j=z^L-z^{-L-1}.
\]
Thus (H.7) says that (H.5) equals the sum of the characters \(H_L\) in (H.2). Complete reducibility of the compact \(SO_3\) action, followed by complexification, makes this equality of characters the asserted module decomposition.

The primary locator for the classical rule is D. J. Rowe, *Vector coherent state theory: a powerful tool for solving algebraic problems in physics*, submitted April 8, 2003, [§5, Theorem 1 (Elliott), equations (57)–(58), printed page 7](https://www.physics.utoronto.ca/site-archive/rowe/pdf/Erice.pdf). Those displayed ranges were opened and read in this run. The full calculation above specifies the symmetric \(A,s\) convention and also covers every zero boundary.

### 2. The harmonic trace and five exact character averages

The polynomial quotient
\[
H_L\simeq
\operatorname{Sym}^L W/
\bigl(Q\,\operatorname{Sym}^{L-2}W\bigr)
\tag{H.8}
\]
is the stated irreducible \(SO(W)\)-module, where \(Q\) is its invariant quadratic tensor and a negative symmetric power is zero. For a direct justification, after complexification the double cover
\(SL_2\to SO_3\) identifies \(W\) with \(\operatorname{Sym}^2\mathbf C^2\). One explicit realization is the adjoint action on trace-zero \(2\times2\) matrices, whose determinant is the invariant quadratic and whose kernel is \(\{\pm I\}\). A highest vector in \(\operatorname{Sym}^L W\) has \(SL_2\)-weight \(2L\); its \(L\)-th power is not divisible by the nondegenerate rank-three quadratic \(Q\). It supplies the irreducible \(\operatorname{Sym}^{2L}\mathbf C^2\) in the quotient. The quotient dimension is
\(\binom{L+2}{2}-\binom{L}{2}=2L+1\), exactly its dimension. This proves (H.8) and the displayed character of \(H_L\).

For \(g\in S_4\), taking traces in (H.8) gives
\[
\sum_{L\ge0}\operatorname{tr}(g\mid H_L)q^L
=\frac{1-q^2}{\det(1-qg\mid W)}.
\tag{H.9}
\]
In the class order \(1^4,2\,1^2,2^2,3\,1,4\), the class sizes are
\(1,6,3,8,6\). The eigenvalues of the signed standard representation \(W\) give the five trace series
\[
\frac{1+q}{(1-q)^2},\quad
\frac1{1+q},\quad
\frac1{1+q},\quad
\frac{1+q}{1+q+q^2},\quad
\frac{1+q}{1+q^2}.
\tag{H.10}
\]
The full character table in the same class order is
\[
\begin{array}{c|rrrrr}
(4)&1&1&1&1&1\\
(1^4)&1&-1&1&1&-1\\
(2,2)&2&0&2&-1&0\\
(3,1)&3&1&-1&0&-1\\
(2,1,1)&3&-1&-1&0&1.
\end{array}
\tag{H.11}
\]
These entries follow directly from the trivial and sign characters, the four-letter permutation character minus its constant subspace, its sign twist, and the three-matching permutation character minus its constant subspace. Their squared dimensions sum to \(24\), and their class inner products are the identity matrix, so these give all five irreducible characters with the indicated usual Specht labels.

Multiply each row of (H.11) entrywise by (H.10), weight by its class size, and divide by \(24\). A common-denominator calculation gives
\[
\sum_{L\ge0}[\tau:H_L]q^L
=\frac{\sum_{e\in E_\tau}q^e}{(1-q^4)(1-q^6)}.
\tag{H.12}
\]
Every numerator is listed explicitly in (H.3). Expanding the two geometric denominators proves (H.4). This calculation is the trace-average proof of the graded multiplicity version of Molien's formula; see Stanley (1979), Theorem 2.1, printed pages 479–480, already opened and checked in T-027. All five rational identities were also verified exactly by the accompanying symbolic script; the finite identity check supplements the derivation.

## T-034. The explicit chamber polytopes

Let \(\mu\vdash4\), \(n\ge0\), and
\(\lambda=(\lambda_1,\lambda_2,\lambda_3,\lambda_4)\vdash4n\), with \(\lambda_2\le n\). Set
\[
c=\lambda_2-\lambda_3,\quad
b=\lambda_3-\lambda_4,\quad
d=\lambda_4,\quad A=\max(c,b),\quad s=\min(c,b),
\tag{H.13}
\]
and put \(\tau=\mu\) when \(c+d\) is even and \(\tau=\mu'\) when it is odd.

For every \(e\in E_\tau\), define the following bounded rational polytopes, each with the three integer variables \((j,x,y)\):
\[
\begin{aligned}
\mathcal P_e^+(A,s)
=\{(j,x,y)\in\mathbf R_{\ge0}^3:\quad&
2j\le s-1,\\
&s-2j\le4x+6y+e\le s-2j+A\},
\end{aligned}
\tag{H.14}
\]
and
\[
\mathcal P_e^0(A)=
\{(j,x,y)\in\mathbf R_{\ge0}^3:
2j+4x+6y=A-e\}.
\tag{H.15}
\]
The first polytope is empty when \(s=0\). Negative right sides make the second empty. Then
\[
\boxed{
p_{\mu,(n)}^\lambda
=
\sum_{e\in E_\tau}
\#\bigl(\mathcal P_e^+(A,s)\cap\mathbf Z^3\bigr)
+\mathbf1_{s\ {\rm even}}
\sum_{e\in E_\tau}
\#\bigl(\mathcal P_e^0(A)\cap\mathbf Z^3\bigr).}
\tag{H.16}
\]
This uses at most twelve fixed three-variable polytopes, without a degree-dependent precomputation or a plethysm coefficient oracle. Their tags are retained, so an integer point appearing in distinct polytopes contributes once for each corresponding summand.

### 3. Proof of the module transport and the lattice bijection

The exact chart T-032 gives
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq S_{(\lambda_2,\lambda_3,\lambda_4)}\mathfrak h_4
\simeq(\det\mathfrak h_4)^d\otimes S_{(c+b,b)}\mathfrak h_4.
\tag{H.17}
\]
The second map is the exterior-column determinant shift from (F.5). Since \(\det\mathfrak h_4=\operatorname{sgn}\) and \(\mathfrak h_4=W\otimes\operatorname{sgn}\), homogeneity of the Schur functor gives the actual \(S_4\)-module isomorphism
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq \operatorname{sgn}^{c+d}\otimes S_{(c+b,b)}W.
\tag{H.18}
\]
Indeed the latter Schur degree is \(c+2b\), whose parity is \(c\). Tensoring a Specht module by sign conjugates its partition, so the desired multiplicity is \([\tau:S_{(c+b,b)}W]\). Compose (H.2) and (H.4).

For each positive \(K\) in (H.2), write \(K=s-2j\). Its index condition is exactly \(j\ge0\), \(2j\le s-1\). For each harmonic tag \(e\), write \(L=4x+6y+e\). The range \(K\le L\le K+A\) is then exactly (H.14). The \(K=0\) band, present when \(s\) is even, has \(L=A-2j\); its equality with \(4x+6y+e\) is (H.15). Every index in the two branching sums has one and only one such tagged integer point, and the converse is immediate from these equations. This proves (H.16).

Boundedness is explicit: the first polytope bounds \(j\) by \((s-1)/2\) and \(4x+6y\) by \(A+s\); the second bounds all three nonnegative coordinates by its right side. In particular their description and all integer witnesses have bit length \(O(\log(n+2))\) for fixed outer degree four.

### 4. The other chamber and the exact extension problem completed in T-037

The complement map (F.12)–(F.15) covers every \(\lambda\) with \(\lambda_3\ge n\). Explicitly take
\[
H=\lambda_1,\qquad
\widehat\lambda=(H-\lambda_4,H-\lambda_3,H-\lambda_2,0),
\quad\widehat n=H-n,
\]
and let \(\widehat\mu=\mu\) for even \(H\) and \(\widehat\mu=\mu'\) for odd \(H\). Then
\[
p_{\mu,(n)}^\lambda
=p_{\widehat\mu,(\widehat n)}^{\widehat\lambda}.
\tag{H.19}
\]
The inequality \(\widehat\lambda_2\le\widehat n\) is exactly \(\lambda_3\ge n\), so (H.16) applies to the right side. Formula (H.19) is obtained from an actual perfect Schur-module pairing, including the sign and contragredient maps; it also covers equality at the chamber wall.

T-031 already gives direct formulas on every proper fundamental face for the symmetric outer partition. At this stage of the reductions, the symmetric-outer rank-four sector still requiring a direct chart computation has
\[
\lambda_1>\lambda_2>\lambda_3>\lambda_4,
\qquad \lambda_2>n>\lambda_3.
\tag{H.20}
\]
Its balanced module is precisely the \(S_4\)-stable divisibility subspace (C.15), with \(k=\lambda_2-n>0\), in the same rank-three flag module used above. T-035 identifies this subspace with vanishing along four flag fibers, and T-037 completes its positive decomposition for every parameter. Thus the chamber formulas above are now part of the full outer-four formula, with at most 108 fixed polytopes of at most five variables for arbitrary outer Schur labels. General terminating positive-polytope constructions remain available from G-009–G-011 in every rank.

## Exact checks and provenance

The companion script [check_chambers.py](check_chambers.py) verifies all five rational identities (H.12), the geometric-sum and full Elliott character identities for \(0\le c,b\le24\), their \(625\) Weyl dimensions, and \(1280\) tagged lattice-count comparisons. Its exact receipt is [CHAMBER_CHARACTER_CHECK.tsv](CHAMBER_CHARACTER_CHECK.tsv). These checks do not replace the symbolic proofs above. Independent cycle-index plethysm checks are recorded separately when completed.

The Elliott rule is classical and its precise primary locator is given above. The symmetric-group character average is explicitly calculated here. The purpose of the composition is the exact flag/normalizer transport and fixed small positive polytope list in the stated chambers. No historical novelty claim is made.



# Four fibers and a positive formula in the central chamber

## T-035. The exact four-point vanishing model

Let \(\lambda\vdash4n\) have at most four parts, and put
\[
c=\lambda_2-\lambda_3,\qquad
b=\lambda_3-\lambda_4,\qquad
d=\lambda_4,\qquad
k=\max(0,\lambda_2-n).
\tag{V.1}
\]
Let \(W=[(2,1,1)]=\mathfrak h_4\otimes\operatorname{sgn}\), with its invariant quadratic form, and let
\[
\mathcal F=\{([q],[t])\in\mathbf P(W)\times\mathbf P(W):q\cdot t=0\},
\qquad \pi:\mathcal F\to\mathbf P(W).
\tag{V.2}
\]
The two projective factors have the usual line-bundle notation
\(\mathcal O_{\mathcal F}(c,b)\). Use the invariant form to identify \(W\) with its dual when taking polynomial sections. Let \(Z\) be the four projective points
\[
[\ell_i],\qquad
\ell_i=e_i-\tfrac14\mathbf1\in\mathfrak h_4,\quad 1\le i\le4.
\tag{V.3}
\]
The sign twist does not change their projective action, so \(Z\) is \(S_4\)-stable. Let \(\mathcal I_Z\) be their reduced ideal sheaf. Then there is an actual \(S_4\)-module isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq
\operatorname{sgn}^{c+d}\otimes
H^0\!\left(\mathcal F,\,
\pi^*(\mathcal I_Z^k)\otimes
\mathcal O_{\mathcal F}(c,b)\right).}
\tag{V.4}
\]
The map is the polynomial chart of T-032 with its exact extension condition. The proof below identifies its divisibility order with vanishing order at each of the four fibers, including all higher orders.

The points in (V.3) have particularly simple equations. In the linear coordinates
\[
X=q_1+q_2,\qquad Y=q_1+q_3,\qquad Z_0=q_1+q_4
\tag{V.5}
\]
on \(\mathfrak h_4\), they are the four projective sign choices
\([1:1:1]\), \([1:-1:-1]\), \([-1:1:-1]\), \([-1:-1:1]\). Their homogeneous ideal is
\[
J=(X^2-Y^2,\ Y^2-Z_0^2).
\tag{V.6}
\]
It is a radical complete intersection of two quadrics. The generator space
\[
U=J_2
\tag{V.7}
\]
is the Specht module \([(2,2)]\), and \(\det U=\operatorname{sgn}\).

### 1. The explicit rank-four chart

Write the first three columns of the original matrix as \(x_i,s_i,w_i\), and let \(y_i\) be the oriented cofactor of its first three columns, so
\[
\sum_i x_i y_i=\sum_i s_i y_i=\sum_i w_i y_i=0.
\]
As in T-032, \(u=\prod_i x_i\), and define the following polynomial balanced coordinates:
\[
q_i=u\left(\frac{s_i}{x_i}
-\frac14\sum_j\frac{s_j}{x_j}\right),\qquad
t_i=x_i y_i,\qquad z=\det X.
\tag{V.8}
\]
Every denominator in each summand of \(q_i\) divides \(u\). These satisfy
\[
\sum_i q_i=\sum_i t_i=0,\qquad q\cdot t=0.
\tag{V.9}
\]
The rank-three flag algebra in T-032 is
\[
R=\mathbf Q[q\in\mathfrak h_4,\ t\in\mathfrak h_4\otimes\operatorname{sgn}]
/(q\cdot t),
\tag{V.10}
\]
together with its determinant variable \(z\); its component of tail degree is \(z^dR_{c,b}\). This incidence presentation follows directly from the line-and-hyperplane flag description: a nonzero pair \(q,t\) with \(q\cdot t=0\) is a line in its annihilating plane, and can be realized by two independent columns of a rank-three matrix. The incidence quadratic is irreducible, as a nondegenerate bilinear form of rank three. Its dense open set therefore gives the entire kernel. This also verifies the presentation directly, in addition to (C.4).

Here \(q\) transforms as \(\mathfrak h_4\), \(t\) as \(W\), and \(z\) by sign. Retwist the action on each \(q\)-generator by sign. Both \(q\) and \(t\) then transform as \(W\), the quadratic relation becomes invariant, and a component of bidegree \((c,b)\) changes by the scalar character \(\operatorname{sgn}^c\). This is an explicitly defined automorphism action on the same algebra. Including \(z^d\) gives exactly the twist \(\operatorname{sgn}^{c+d}\) in (V.4).

The complete incidence ring has
\[
R_{c,b}=H^0(\mathcal F,\mathcal O_{\mathcal F}(c,b))
\quad(c,b\ge0).
\tag{V.11}
\]
For instance, use the exact sequence of the incidence hypersurface in
\(\mathbf P^2\times\mathbf P^2\), whose equation has bidegree \((1,1)\).
The first cohomology of \(\mathcal O(c-1,b-1)\) on this product vanishes for these indices, so its global section quotient is exactly (V.10). Equivalently the same equality is the rank-three flag Cauchy component of T-032.

### 2. Equality of the two orders of vanishing

It is enough to treat \(i=4\), since row permutation acts transitively on the four indices. At a general point of the divisor \(x_4=0\), the other \(x_i\) and \(s_4\) are nonzero. Equations (V.8) give
\[
q\in\mathbf Q^\times\ell_4,\qquad t_4=0,
\]
so the image is the general point of the fiber
\(\mathcal F_4=\pi^{-1}([\ell_4])\).

We verify that the valuation of a pulled-back section along \(x_4=0\) is exactly its order in the ideal of \(\mathcal F_4\). Put
\[
x_4=\epsilon,\quad s_4=S\ne0,\quad r_j=s_j/x_j\ (j=1,2,3).
\]
Use the affine chart \(q_4-q_1\ne0\) of the first projective factor. The ideal of the point \([\ell_4]\) there is generated by
\[
a_2=\frac{q_2-q_1}{q_4-q_1},\qquad
a_3=\frac{q_3-q_1}{q_4-q_1}.
\]
Their exact pullbacks are
\[
a_j=\epsilon\,\frac{r_j-r_1}{S-\epsilon r_1},
\qquad j=2,3.
\tag{V.12}
\]
The map \(\pi\) is a projective-line bundle, so \(a_2,a_3\) are also regular parameters transverse to \(\mathcal F_4\) at its generic point.

The two leading coefficients \((r_2-r_1)/S,(r_3-r_1)/S\) in (V.12) are algebraically independent over the function field of the image fiber. This can be checked inside the original matrix without a genericity assumption about stabilizers. Restrict to the subfamily \(w_4=0\), keep \(x_1,x_2,x_3,S\) nonzero, and vary \(w_1,w_2,w_3\). At \(\epsilon=0\), the cofactors \(y_j\), \(j\le3\), expand along the fourth row \((0,S,0)\); hence the resulting \(t_j\) depend on \(S,x_1,x_2,x_3,w_1,w_2,w_3\) and not on \(r_1,r_2,r_3\). They range over the entire plane \(t_1+t_2+t_3=0\): after dividing by the nonzero factors \(x_i,S\), they are the pairwise differences of \(w_j/x_j\), with the usual cyclic signs. They therefore cover a dense open of the projective fiber independently of the freely chosen differences \(r_2-r_1,r_3-r_1\). A fourth column makes the determinant \(z\) any desired nonzero value on this same dense set.

Now take a nonzero section, trivialized on this chart and a nonzero coordinate chart of the second factor. If its first nonzero transverse term has total degree \(h\) in \(a_2,a_3\), that term lies in
\[
\operatorname{gr}^h_{\mathcal F_4}\simeq
\mathbf Q(\mathcal F_4)[a_2,a_3]_h.
\]
After (V.12), its leading coefficient of \(\epsilon^h\) is a nonzero homogeneous polynomial in the two algebraically independent leading coefficients. It cannot cancel. The coordinate trivializations have valuation zero at a generic point of the divisor. Thus
\[
\operatorname{ord}_{x_4=0}(F(q(X),t(X),z(X)))
=\operatorname{ord}_{\mathcal F_4}(F).
\tag{V.13}
\]
Multiplication by \(z^d\) has valuation zero there, as just verified. The same argument applies to each \(i\).

The divisor factors \(x_i\) are pairwise nonassociate primes in the original polynomial ring. Therefore divisibility by \(u^k\) is equivalent to order at least \(k\) along every \(x_i=0\). By (V.13), this is exactly order at least \(k\) along all four fibers. The normal-jet quotients of each smooth fiber are locally free over that integral fiber. A section of such a quotient that vanishes at its generic point vanishes everywhere, so the generic order condition is the full sheaf-ideal-power condition. The fibers are disjoint, and \(\pi\) is smooth, so their ideal powers are precisely the pullbacks of the four point-ideal powers, or equivalently of \(\mathcal I_Z^k\). This proves (V.4) using the exact divisibility identity (C.15).

### 3. The four-point ideal and its equivariant resolution

No projective point of the scheme (V.6) has \(Z_0=0\), since its equations would force \(X=Y=0\). On \(Z_0=1\) the equations give \(X^2=Y^2=1\), four reduced points in characteristic zero. These are exactly (V.3), so (V.6) is its saturated homogeneous ideal. The quadrics have no common factor and form a regular sequence.

The \(S_4\) action on \(X,Y,Z_0\) is by signed permutation matrices. On their squares it is the permutation action on the three perfect matchings of four letters. Thus their trace-free difference space \(U\) is the inflated standard representation of \(S_3\), namely \([(2,2)]\), with determinant sign. This is also seen by taking the kernel of evaluation
\(\operatorname{Sym}^2W\to\mathbf Q^4\), which is surjective on these four points.

For \(k\ge1\), the \(k\)-th power of this two-generator complete-intersection ideal has the exact equivariant resolution
\[
0\longrightarrow
\operatorname{Sym}^{k-1}U\otimes\det U\otimes
\mathcal O_{\mathbf P(W)}(-2k-2)
\longrightarrow
\operatorname{Sym}^{k}U\otimes
\mathcal O_{\mathbf P(W)}(-2k)
\longrightarrow
\mathcal I_Z^k\longrightarrow0.
\tag{V.14}
\]
To verify exactness directly, choose generators \(f,g\) of \(U\), and let \(e_j\) denote the formal basis element mapped to \(f^{k-j}g^j\). The final map sends these \(k+1\) formal monomials to their products in the polynomial ring. Its \(k\) relations are \(g e_j-f e_{j+1}\), \(0\le j<k\). They are independent over the polynomial ring and generate all relations: reduce a relation modulo \(f\), use that \(g\) is a nonzerodivisor modulo \(f\), subtract the last adjacent relation, and descend on the number of terms. This yields exactness. The invariant form of that map is
\[
h\otimes(f\wedge g)\longmapsto
(hg)\otimes f-(hf)\otimes g,
\]
which proves the \(\det U\) twist and full equivariance.

## T-036. A positive module formula when the opposite gaps agree

Let \(b,k,d\ge0\), and set
\[
\lambda=(d+2b+2k,\ d+b+2k,\ d+b,\ d),\qquad n=d+b+k.
\tag{V.15}
\]
Equivalently the two opposite root gaps satisfy
\(\lambda_1-\lambda_2=\lambda_3-\lambda_4=b\), and the middle gap is \(2k\). Then
\[
\boxed{
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq\operatorname{sgn}^{d}\otimes
\left(
\operatorname{Sym}^{k}U\otimes\operatorname{Sym}^{b}W
\ \oplus\
\operatorname{sgn}\otimes
\operatorname{Sym}^{k-1}U\otimes\operatorname{Sym}^{b-1}W
\right).}
\tag{V.16}
\]
A negative symmetric power means the zero module. In particular this formula includes every boundary \(b=0\) or \(k=0\), and also every strictly interior central-chamber member \(b,k>0\) of this family.

### 4. Proof of the positive boundary cohomology term

Let \(\mathcal Q\) be the rank-two quotient bundle in
\[
0\to\mathcal O_{\mathbf P(W)}(-1)\to
W\otimes\mathcal O_{\mathbf P(W)}\to\mathcal Q\to0.
\tag{V.17}
\]
The fiber of \(\pi\) over a line \(q\) consists of lines in its annihilator. The invariant quadratic form identifies the dual of that annihilator with \(W/q\). Hence
\[
\pi_*\mathcal O_{\mathcal F}(0,b)=\operatorname{Sym}^b\mathcal Q,
\qquad
R^1\pi_*\mathcal O_{\mathcal F}(0,b)=0
\quad(b\ge0).
\tag{V.18}
\]
This is the polynomial degree-\(b\) description on each projective-line fiber, and it is compatible with the specified group action.

Taking symmetric powers of (V.17), whose kernel has rank one, gives
\[
0\to\mathcal O(-1)\otimes\operatorname{Sym}^{b-1}W
\to\mathcal O\otimes\operatorname{Sym}^{b}W
\to\operatorname{Sym}^{b}\mathcal Q\to0.
\tag{V.19}
\]
The first map multiplies by the tautological vector. Locally the original line inclusion splits, so tensoring (V.19) with \(\mathcal I_Z^k(c)\) preserves its exactness.

In the family (V.15), \(c=2k\). The resolution (V.14), together with the elementary cohomology of line bundles on \(\mathbf P^2\), gives
\[
\begin{aligned}
H^0(\mathcal I_Z^k(2k))&=\operatorname{Sym}^k U,\\
H^0(\mathcal I_Z^k(2k-1))&=0,\\
H^1(\mathcal I_Z^k(2k))&=0,\\
H^1(\mathcal I_Z^k(2k-1))
&=\operatorname{Sym}^{k-1}U\otimes\det U.
\end{aligned}
\tag{V.20}
\]
Indeed the two resolution twists are \((-2,0)\) in the first and third lines and \((-3,-1)\) in the second and fourth. On \(\mathbf P^2\), \(H^1(\mathcal O(a))=0\), \(H^2(\mathcal O(-2))=H^2(\mathcal O(-1))=0\), and \(H^2(\mathcal O(-3))\) is one-dimensional. Its \(S_4\) character is trivial because \(\det W=1\). The same four equalities hold for \(k=0\) with the negative symmetric power interpreted as zero, directly from \(\mathcal I_Z^0=\mathcal O\).

The cohomology sequence of (V.19) now gives the short exact sequence
\[
0\to
\operatorname{Sym}^kU\otimes\operatorname{Sym}^bW
\to
H^0(\mathcal I_Z^k(2k)\otimes\operatorname{Sym}^b\mathcal Q)
\to
\det U\otimes\operatorname{Sym}^{k-1}U\otimes
\operatorname{Sym}^{b-1}W
\to0.
\tag{V.21}
\]
Every rational \(S_4\)-module is semisimple: averaging a projection over its 24 elements gives an equivariant splitting. Thus (V.21) is the direct sum of its end terms as an \(S_4\)-module. Apply (V.18), then (V.4), where \(c=2k\) is even and \(\det U=\operatorname{sgn}\). This proves (V.16). The splitting need not be canonical; the injection, quotient, and resulting isomorphism type are exact.

## 5. Fixed positive polytopes for every outer Schur label

Let \(F_{(4)}=\{0\}\), \(F_{(1^4)}=\{3\}\), and \(F_{(2,2)}=\{1,2\}\). The complete symmetric-power decomposition of \(U\) is
\[
[\rho:\operatorname{Sym}^kU]
=\sum_{f\in F_\rho}
\#\{(a_2,a_3)\in\mathbf Z_{\ge0}^2:2a_2+3a_3=k-f\},
\tag{V.22}
\]
for \(\rho=(4),(1^4),(2,2)\), with the other two multiplicities zero. This is the \(S_3\) formula (P.10) transported along the same matching quotient.

By the exact harmonic quotient (H.8),
\[
[\tau:\operatorname{Sym}^{b}W]
=\sum_{e\in E_\tau}
\#\{(r_2,r_4,r_6)\in\mathbf Z_{\ge0}^3:
2r_2+4r_4+6r_6=b-e\}.
\tag{V.23}
\]
The tag sets \(E_\tau\) are listed in (H.3).

The necessary tensor products have multiplicity one. Multiplication by \((4)\) leaves the label unchanged, multiplication by \((1^4)\) conjugates it, and multiplication by \((2,2)\) has
\[
\begin{array}{c|c}
\tau&[(2,2)]\otimes[\tau]\\ \hline
(4),(1^4)&[(2,2)]\\
(2,2)&[(4)]\oplus[(1^4)]\oplus[(2,2)]\\
(3,1),(2,1,1)&[(3,1)]\oplus[(2,1,1)].
\end{array}
\tag{V.24}
\]
Each equality follows by entrywise multiplication of the character rows (H.11).

For a label \(\nu\vdash4\), define \(\mathcal C_\nu(k,b)\) to be the following explicit sum. For every \(\rho\in\{(4),(1^4),(2,2)\}\) and \(\tau\vdash4\) whose tensor product in (V.24) contains \(\nu\), and every \(f\in F_\rho,e\in E_\tau\), count the nonnegative integer solutions of
\[
2a_2+3a_3=k-f,\qquad
2r_2+4r_4+6r_6=b-e.
\tag{V.25}
\]
Each tag contributes one bounded five-variable polytope. Set the whole count to zero if \(k<0\) or \(b<0\). Write \(\mu^{[d]}=\mu\) for even \(d\) and \(\mu'\) for odd \(d\). Then
\[
\boxed{
p_{\mu,(n)}^\lambda
=\mathcal C_{\mu^{[d]}}(k,b)
+\mathcal C_{(\mu^{[d]})'}(k-1,b-1).}
\tag{V.26}
\]
This is (V.16) with every finite-group and symmetric-power multiplicity replaced by its explicit nonnegative count.

For any fixed \(\nu\), the first count has at most 36 tagged polytopes: the maximum occurs for \(\nu=(3,1)\) or \((2,1,1)\), with \(6+6+2(6+6)=36\) tags. Thus (V.26) uses at most 72 fixed five-variable polytopes for all five outer labels and all \(b,k,d\). No degree-dependent invariant-ring computation occurs. The inequalities are just nonnegativity and the two displayed equations; each witness has bit length \(O(\log(n+2))\).

## Provenance and remaining scope

The exact morphisms used here are the chart (C.4), the transverse equations (V.12), the complete-intersection resolution (V.14), and the tautological quotient map (V.19). Their proofs are included in full. For the elementary projective-space cohomology in (V.20), the primary reference is [Stacks Project, Section 30.8, Lemma 30.8.1, tag 01XS](https://stacks.math.columbia.edu/tag/01XS); its complete ordered Čech proof was opened and read in this run. The determinant character is fixed here by the specified \(SO(W)\) action. No numerical plethysm value is used as input.

An independent cycle-index/Murnaghan–Nakayama calculation passed all 420 coefficient cases in (V.15) with \(n\le6\), every outer partition of four, and all nonnegative \(b,k,d\); 175 are strict middle-chamber cases. The independent side computed the right-hand module from reciprocal characteristic-polynomial series, without the fat-point derivation. Receipt: `work/rectangular/OUTER4_SELF_COMPLEMENT_INDEPENDENT_CHECK.tsv`; code: `work/rectangular/verify_outer4_self_complement.py`. A separate independent reading checked the complete valuation, resolution, cohomology, and polytope proofs.

The family includes the paired-row case T-030 when \(b=0\), and the equal-middle-row case T-027 when \(k=0\). For \(b,k>0\), it supplies a direct positive formula inside the strict central chamber left by T-034. The general four-point section model (V.4) also applies to unequal opposite gaps. T-037 subsequently completes those cases by separating the two-quadric ideal powers inside the incidence ring and gives a fixed positive polytope formula for every outer partition of four. G-009–G-011 supply terminating positive counts in every rank; the next efficient direct-formula question in this route lies beyond outer degree four.



# A fixed positive polytope formula for every outer Schur partition of four

## T-037. Full statement and conventions

Let \(\mu\vdash4\), \(n\ge0\), and \(\lambda\vdash4n\) have at most four parts. There is an explicit formula for \(p_{\mu,(n)}^\lambda\) using at most **108 tagged bounded rational polytopes, each with at most five variables**. For the symmetric or exterior outer partition the bound is 36, and for \(\mu=(2,2)\) it is 72. All tags and equations are listed in §5. No character evaluation, invariant-ring elimination, or degree-dependent precomputation occurs in this formula.

For a valid output partition with more than four parts, the coefficient is zero. Indeed the Schur symmetrizer realizes \(S_\mu(\operatorname{Sym}^nV)\) inside \((\operatorname{Sym}^nV)^{\otimes4}\). Starting with the one-row representation \(\operatorname{Sym}^nV\), each of the next three tensor factors adds a horizontal strip by Pieri's rule, increasing the number of rows by at most one. Thus every output in that ambient tensor product has at most four rows. The evaluator includes this zero case and rejects inputs of the wrong size or order.

The proof uses the original action
\[
q\in\mathfrak h_4=[(3,1)],\qquad
t\in W=\mathfrak h_4\otimes\operatorname{sgn}=[(2,1,1)],
\qquad
R=\mathbf Q[q,t]/(q\cdot t),
\tag{A.1}
\]
with bidegrees \((1,0),(0,1)\). Thus the incidence equation transforms by sign. We do not retwist the \(q\)-action in the separation of variables below. This convention makes its evaluation at the four affine vectors \(\ell_i=e_i-\frac14\mathbf1\) the ordinary permutation representation in every degree at least two.

Let \(U=[(2,2)]\subset\operatorname{Sym}^2\mathfrak h_4\) be the two quadrics vanishing at the four points (V.3), and put
\[
J_R=UR,\qquad \mathcal H=R/J_R.
\tag{A.2}
\]
Then multiplication, after the explicitly specified equivariant choice of sections in §1, gives the graded \(S_4\)-module isomorphism
\[
\boxed{
R\simeq\operatorname{Sym}(U)\otimes\mathcal H.}
\tag{A.3}
\]
The degree of \(U\) is \((2,0)\). In particular
\[
\boxed{
(J_R^k)_{c,b}
\simeq\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^j U\otimes\mathcal H_{c-2j,b}.}
\tag{A.4}
\]
The finite-group modules in this decomposition are explicit:
\[
\boxed{
\begin{array}{c|l}
C&\mathcal H_{C,b}\\ \hline
0&\operatorname{Sym}^b W\\
1&\displaystyle\operatorname{sgn}\otimes
       \bigoplus_{L=1}^{b+1}H_L\\
2&\displaystyle D_b\ \oplus\
       \operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\\
C\ge3&D_b,
\end{array}}
\qquad
D_b=\operatorname{Ind}_{S_3}^{S_4}\operatorname{Sym}^b\mathfrak h_3.
\tag{A.5}
\]
A negative symmetric power is zero, and \(H_L\) is the \(SO(W)\) harmonic module restricted along the actual rotational \(S_4\) map (H.1).

### Orienting the partition by the exact complement map

Set \(a=\lambda_1-\lambda_2\) and \(b=\lambda_3-\lambda_4\). When \(a<b\), replace the input by
\[
H=\lambda_1,\quad
\lambda\longleftarrow(H-\lambda_4,H-\lambda_3,H-\lambda_2,0),
\quad n\longleftarrow H-n,
\quad \mu\longleftarrow\mu^{[H]},
\tag{A.6}
\]
where \(\eta^{[H]}=\eta\) for even \(H\) and \(\eta'\) for odd \(H\). The exact perfect pairing (F.12)–(F.15) proves that this replacement leaves the coefficient unchanged. It interchanges \(a,b\), so after at most one replacement \(a\ge b\).

For the resulting input put
\[
a=\lambda_1-\lambda_2,\qquad b=\lambda_3-\lambda_4,\qquad
c=\lambda_2-\lambda_3,\qquad d=\lambda_4,\qquad
k=\max(0,\lambda_2-n).
\tag{A.7}
\]
Then \(c\ge2k\). For \(k=0\) this is immediate. For \(k>0\), the size equation \(|\lambda|=4n\) gives
\[
c-2k=\frac{a-b}{2}\ge0.
\tag{A.8}
\]
The exact four-fiber model T-035 now gives the following positive module decomposition:
\[
\boxed{
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq \operatorname{sgn}^d\otimes
\left(
\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^jU\otimes\mathcal H_{c-2j,b}
\ \oplus\
\mathbf1_{c=2k}\,
\operatorname{sgn}\otimes
\operatorname{Sym}^{k-1}U\otimes\operatorname{Sym}^{b-1}W
\right).}
\tag{A.9}
\]
The term with \(c=2k\) is the fully proved boundary term of T-036. The proof of (A.3)–(A.9) follows before the explicit polytope formula.

## 1. Four lines, a nonzerodivisor, and actual module freeness

Write
\[
S=\mathbf Q[q],\qquad A=S/(U).
\]
In the coordinates (V.5),
\[
A=\mathbf Q[X,Y,Z_0]/(X^2-Y^2,\ Y^2-Z_0^2).
\tag{A.10}
\]
This is the reduced coordinate ring of the four affine lines through the four projective points. Indeed its two equations form a complete intersection, the four projective points are reduced by the calculation in T-035, and the same ring is free over \(\mathbf Q[Z_0]\) with basis \(1,X,Y,XY\), using the monic equations \(X^2=Z_0^2,Y^2=Z_0^2\). It embeds in the product of the four line rings: localizing at \(Z_0\) makes that claim the four distinct roots \(X/Z_0,Y/Z_0=\pm1\); injectivity before localization follows from its freeness over \(\mathbf Q[Z_0]\). In particular no component supported at the origin is being discarded.

The image of \(\ell=q\cdot t\) is a nonzerodivisor in \(A[t]\). On each of the four line components it is a nonzero scalar line coordinate times the nonzero linear form \(\ell_i\cdot t\), so it is a nonzerodivisor in every component domain. The just-proved embedding into their product makes multiplication injective on \(A[t]\) itself.

Consequently the ordinary bigraded Hilbert series satisfy
\[
\operatorname{Hilb}(\mathcal H;s,t)
=\frac{(1-st)(1-s^2)^2}{(1-s)^3(1-t)^3}
=(1-s^2)^2\operatorname{Hilb}(R;s,t).
\tag{A.11}
\]
The first equality follows from the two regular quadrics in \(S\) and the injective multiplication by \(\ell\) just proved; the second follows from the one nonzero incidence equation in the polynomial ring.

For each bidegree, choose a rational linear right inverse \(s_0\) to \(R\to\mathcal H\) and replace it by
\[
s(h)=\frac1{24}\sum_{g\in S_4}g\,s_0(g^{-1}h).
\tag{A.12}
\]
This is an actual \(S_4\)-equivariant right inverse. Define the multiplication map
\[
\operatorname{Sym}(U)\otimes\mathcal H\to R,\qquad
p\otimes h\longmapsto p(U)\,s(h).
\tag{A.13}
\]
It is surjective: subtract the chosen lift of a quotient class, express the remainder in \(UR\), and repeat with strictly smaller \(q\)-degree. The source has the same Hilbert series as the target by (A.11). Each bidegree is finite-dimensional, so (A.13) is injective in each bidegree. This proves (A.3) as an equivariant \(\operatorname{Sym}(U)\)-module isomorphism. The ideal powers correspond to polynomials in \(U\) of total degree at least \(k\), proving (A.4). In particular the two elements of \(U\) form a regular sequence in \(R\).

The section (A.12) proves existence of the specified multiplication isomorphism; the explicit counts in §5 require neither its computation nor any averaging of degree-dependent vectors.

## 2. Every quotient piece \(\mathcal H_{C,b}\)

The evaluation map on the four affine vectors \(\ell_i\) gives
\[
A_0=\mathbf1,\qquad A_1=\mathfrak h_4,\qquad
A_C\simeq\operatorname{Perm}_4\quad(C\ge2).
\tag{A.14}
\]
Here evaluation has no parity twist, since the original standard action sends \(\ell_i\) exactly to \(\ell_{\sigma(i)}\). For completeness, in the coordinates (V.5), the four functions \(X^2,XY,XZ_0,YZ_0\) have linearly independent evaluations, so degree two evaluation is onto. In degree three use \(XYZ_0,X^3,Y^3,Z_0^3\). The invariant quadratic \(X^2+Y^2+Z_0^2\) is a nonzero constant on the four selected vectors; multiplication by it extends surjectivity by two degrees. The Hilbert series
\[
\operatorname{Hilb}(A;s)=\frac{(1-s^2)^2}{(1-s)^3}
=1+3s+4s^2+4s^3+\cdots
\]
then proves that every stated surjection is an isomorphism.

Since \(\ell=q\cdot t\) has sign character and is a nonzerodivisor on \(A[t]\), its homogeneous exact sequence is
\[
0\to
\operatorname{sgn}\otimes A_{C-1}\otimes
\operatorname{Sym}^{b-1}W
\xrightarrow{\ \ell\ }
A_C\otimes\operatorname{Sym}^{b}W
\to\mathcal H_{C,b}\to0.
\tag{A.15}
\]

For \(C\ge3\), both \(A_C,A_{C-1}\) are the four-point permutation module. At the point \(\ell_i\), the map in (A.15) is multiplication by \(\ell_i\cdot t\). The stabilizer \(S_3\) fixes the line \(\mathbf Q\ell_i\) in \(\mathfrak h_4\), so its corresponding line in \(W\) is sign. The quotient \(W/\operatorname{sgn}\) is \(\mathfrak h_3\otimes\operatorname{sgn}\). Thus evaluation identifies the cokernel in (A.15) with
\[
\operatorname{Ind}_{S_3}^{S_4}
\operatorname{Sym}^b(\mathfrak h_3\otimes\operatorname{sgn}).
\]
The explicit rational area-form intertwiner \(J\) of (P.8)–(P.9) identifies \(\mathfrak h_3\otimes\operatorname{sgn}\) with \(\mathfrak h_3\); taking its symmetric power gives precisely \(D_b\).

For \(C=2\), the source of (A.15) has \(A_1=\mathfrak h_4\), a codimension-one submodule of \(\operatorname{Perm}_4\). Extend the source to the entire permutation module. That larger multiplication map is injective point by point and has cokernel \(D_b\), just as above. Its image modulo the smaller image is \(\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\). Hence
\[
0\to\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W
\to\mathcal H_{2,b}\to D_b\to0.
\]
Averaging a projection splits this exact sequence, giving the \(C=2\) row of (A.5).

For \(C=0\) there is no incidence relation, giving \(\operatorname{Sym}^bW\). For \(C=1\), the quadrics have no component and \(\mathcal H_{1,b}=R_{1,b}\). The exact incidence/Schur identification gives
\[
R_{1,b}=S_{(b+1,b)}\mathfrak h_4
=\operatorname{sgn}\otimes S_{(b+1,b)}W.
\]
The Elliott formula (H.2) with Dynkin labels \((1,b)\) is
\[
S_{(b+1,b)}W=\bigoplus_{L=1}^{b+1}H_L,
\]
including \(b=0\). This completes the proof of every row of (A.5).

## 3. Exact saturation in the oriented range

Retwisting the \(q\)-action in (V.4) back to the original action (A.1) gives
\[
(S_\lambda\mathbf Q^4)_{(n^4)}
\simeq\operatorname{sgn}^{d}\otimes
H^0(\mathcal F,\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(c,b)).
\tag{A.16}
\]
The extra sign \(\operatorname{sgn}^{c}\) of (V.4) is precisely removed by that retwist; no determinant or parity factor is omitted.

For \(c\ge2k+1\), this section space is exactly \((J_R^k)_{c,b}\). Here is a direct proof that does not assume an equality of saturated and unsaturated ideals. Pull back the resolution (V.14) along the flat map \(\pi\), and tensor by \(\mathcal O_{\mathcal F}(c,b)\). Its two line-bundle terms have first degrees
\[
r=c-2k\ge1,\qquad r-2\ge-1.
\]
On the incidence flag,
\[
H^1(\mathcal F,\mathcal O_{\mathcal F}(a,b))=0
\quad\text{for }a\ge-1,\ b\ge0.
\tag{A.17}
\]
To check it, use the incidence hypersurface sequence on \(\mathbf P^2\times\mathbf P^2\). The first cohomology of the ambient line bundle is zero. The potentially contributing second cohomology of the preceding term is also zero: its first degree is \(a-1\ge-2\), its second degree is \(b-1\ge-1\), and neither factor has second cohomology in those ranges. The one-dimensional sign character of the incidence equation does not affect vanishing. These projective-space cohomology statements are exactly the Čech calculation cited and read in T-035.

It follows that the section space in (A.16) is the cokernel
\[
\operatorname{Sym}^{k-1}U\otimes\det U\otimes R_{r-2,b}
\longrightarrow
\operatorname{Sym}^{k}U\otimes R_{r,b}.
\tag{A.18}
\]
On the other hand the regular sequence \(U\) in \(R\), established by (A.3), has the power-ideal resolution obtained by extending the two-variable resolution in (V.14) to this free \(\operatorname{Sym}(U)\)-module. Its degree-\((c,b)\) cokernel is exactly \((J_R^k)_{c,b}\), with the same multiplication map as (A.18). This proves the claimed identification by the actual map, rather than a dimension comparison.

For \(c=2k\), T-036 gives exactly
\[
H^0(\mathcal F,\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(2k,b))
\simeq
(J_R^k)_{2k,b}\oplus
\operatorname{sgn}\otimes\operatorname{Sym}^{k-1}U
\otimes\operatorname{Sym}^{b-1}W,
\]
since (A.4) makes the first summand \(\operatorname{Sym}^kU\otimes\operatorname{Sym}^bW\).
The case \(k=0,c=0\) has zero extra term. For \(k=0\) in all degrees, the ideal is the whole ring and the same conclusion follows directly. Combining these equalities with (A.4), (A.5), and (A.16) proves (A.9).

## 4. The three fixed tag tables

For \(\rho\in\{(4),(1^4),(2,2)\}\), let \(F_\rho\) be
\[
F_{(4)}=\{0\},\qquad F_{(1^4)}=\{3\},\qquad F_{(2,2)}=\{1,2\}.
\tag{A.19}
\]
Then
\[
[\rho:\operatorname{Sym}^jU]
=\sum_{f\in F_\rho}
\#\{(x_2,x_3)\ge0:2x_2+3x_3=j-f\},
\tag{A.20}
\]
where integer coordinates are understood.

Let \(E_\tau\) be the harmonic tags of (H.3), and let \(G_\tau\) be the following induction tags:
\[
\begin{array}{c|c|c}
\tau&E_\tau&G_\tau\\ \hline
(4)&\{0,9\}&\{0\}\\
(1^4)&\{3,6\}&\{3\}\\
(2,2)&\{2,4,5,7\}&\{1,2\}\\
(3,1)&\{2,3,4,5,6,7\}&\{0,1,2\}\\
(2,1,1)&\{1,3,4,5,6,8\}&\{1,2,3\}.
\end{array}
\tag{A.21}
\]
Their exact meanings are
\[
\begin{aligned}
[\tau:\operatorname{Sym}^bW]
&=\sum_{e\in E_\tau}
\#\{(y_2,y_4,y_6)\ge0:2y_2+4y_4+6y_6=b-e\},\\
[\tau:\bigoplus_{L=1}^{b+1}H_L]
&=\sum_{e\in E_\tau}
\#\{(y_4,y_6)\ge0:1\le4y_4+6y_6+e\le b+1\},\\
[\tau:D_b]
&=\sum_{g\in G_\tau}
\#\{(y_2,y_3)\ge0:2y_2+3y_3=b-g\}.
\end{aligned}
\tag{A.22}
\]
The first two equations follow from (H.4), (H.8). For the third, the exact induction branchings are
\[
\begin{aligned}
\operatorname{Ind}_{S_3}^{S_4}[(3)]&=[(4)]\oplus[(3,1)],\\
\operatorname{Ind}_{S_3}^{S_4}[(2,1)]&=[(3,1)]\oplus[(2,2)]\oplus[(2,1,1)],\\
\operatorname{Ind}_{S_3}^{S_4}[(1^3)]&=[(2,1,1)]\oplus[(1^4)].
\end{aligned}
\tag{A.23}
\]
The first is the four-coset permutation representation, the third is its sign twist, and the second follows by subtracting these two from induction of the regular representation of \(S_3\), or by the character rows (H.11). Combining these branchings with the three \(S_3\) tag series (P.10) gives the displayed \(G_\tau\).

Write \(K_{\rho\tau}^{\nu}\in\{0,1\}\) for the following fixed tensor table: \((4)\) is the identity, \((1^4)\) conjugates a partition, and
\[
\begin{array}{c|c}
\tau&\{\nu:K_{(2,2),\tau}^{\nu}=1\}\\ \hline
(4),(1^4)&\{(2,2)\}\\
(2,2)&\{(4),(1^4),(2,2)\}\\
(3,1),(2,1,1)&\{(3,1),(2,1,1)\}.
\end{array}
\tag{A.24}
\]
This is the exact character multiplication (V.24). Every other entry is zero.

## 5. The complete positive polytope evaluator

The following definitions are finite sums over the fixed tables (A.19), (A.21), (A.24). They contain no representation-theoretic multiplicities as unknown inputs.

For a label \(\nu\), integers \(L,U_0,b\), define \(\mathsf D_\nu(L,U_0;b)\) by summing, for every \(K_{\rho\tau}^{\nu}=1\), \(f\in F_\rho\), \(g\in G_\tau\), the lattice count in
\[
\left\{(x_2,x_3,y_2,y_3)\in\mathbf R_{\ge0}^4:
\quad L\le f+2x_2+3x_3\le U_0,\quad
2y_2+3y_3=b-g\right\}.
\tag{A.25}
\]
This count is zero when \(U_0<L\) or \(b<0\).

Define \(\mathsf W_\nu(j,b)\) by summing, for every \(K_{\rho\tau}^{\nu}=1\), \(f\in F_\rho\), \(e\in E_\tau\), the lattice count in
\[
\left\{(x_2,x_3,y_2,y_4,y_6)\in\mathbf R_{\ge0}^5:
\quad 2x_2+3x_3=j-f,\quad
2y_2+4y_4+6y_6=b-e\right\}.
\tag{A.26}
\]
Define \(\mathsf L_\nu(j,b)\) using the same tags but the four-variable polytope
\[
\left\{(x_2,x_3,y_4,y_6)\in\mathbf R_{\ge0}^4:
\quad 2x_2+3x_3=j-f,\quad
1\le4y_4+6y_6+e\le b+1\right\}.
\tag{A.27}
\]
The last two functions are zero for \(j<0\) or \(b<0\).

After the exact orientation (A.6), use \(b,c,d,k\) in (A.7) and set \(\nu=\mu^{[d]}\). The full coefficient is
\[
\boxed{
\begin{aligned}
p_{\mu,(n)}^\lambda
={}&\mathsf D_\nu\!\left(k,\left\lfloor\frac{c-3}{2}\right\rfloor;b\right)\\
&+\begin{cases}
\displaystyle
\mathsf L_{\nu'}\!\left(\frac{c-1}{2},b\right),
&c\text{ odd},\\[2mm]
\displaystyle
\mathsf W_\nu\!\left(\frac c2,b\right)
+\mathbf1_{c\ge2k+2}
\left[
\mathsf D_\nu\!\left(\frac{c-2}{2},\frac{c-2}{2};b\right)
+\mathsf W_{\nu'}\!\left(\frac{c-2}{2},b-1\right)
\right]\\
\displaystyle\hspace{13mm}
+\mathbf1_{c=2k}\mathsf W_{\nu'}(k-1,b-1),
&c\text{ even}.
\end{cases}
\end{aligned}}
\tag{A.28}
\]
Here the symbols on the left refer to the oriented input; (A.6) proves equality with the original requested coefficient.

To verify (A.28), partition the positive sum (A.9) according to \(C=c-2j\). All \(C\ge3\) terms are (A.25), where the value \(j=f+2x_2+3x_3\) is uniquely recovered from the lattice point. For odd \(c\), the remaining term has \(C=1\), yielding (A.27) with the sign twist \(\nu'\). For even \(c\), the \(C=0\) term gives (A.26); the \(C=2\) term exists exactly when \(c\ge2k+2\), and its two summands give (A.25) and the sign-shifted (A.26). Finally the boundary correction is present exactly when \(c=2k\), as displayed. Thus every summand in the module decomposition has one and only one tagged polytope, and every lattice point counts one coefficient of its two explicit symmetric-power series.

All polytopes are bounded: the \(x\)-coordinates have an upper bound from \(U_0\) or \(j\); the \(y\)-coordinates have an upper bound from \(b\). Their matrices use only the fixed integers \(1,2,3,4,6\), and their constants have bit length \(O(\log(n+2))\).

For a fixed label \(\nu\), (A.25) has at most 18 tags; (A.26), (A.27) have at most 36. When \(c\) is odd, at most \(18+36=54\) polytopes occur. When \(c\ge2k+2\) is even, the bound is \(18+36+18+36=108\). At \(c=2k\), only the two (A.26) terms survive, giving at most 72. For \(\nu=(4)\) or \((1^4)\), the corresponding tag maxima are 6 and 12, yielding the bound 36; for \(\nu=(2,2)\), they are 12 and 24, yielding 72. Sign and complement twists preserve these three categories.

## 6. Constant-size arithmetic and the standalone implementation

The fixed polytope counts can also be evaluated by a fixed number of integer operations. Define
\[
C(N)=\#\{(x,y)\ge0:2x+3y=N\},\qquad
P(N)=\#\{(x,y)\ge0:2x+3y\le N\},
\]
and set both to zero for \(N<0\). For \(N\ge0\),
\[
C(N)=1+\left\lfloor\frac N6\right\rfloor
-\mathbf1_{N\equiv1\pmod6}.
\tag{A.29}
\]
For \(e=0,1\), put \(T_e=\lfloor(N-3e)/6\rfloor\). Splitting \(y=2t+e\) gives
\[
P(N)=\sum_{e=0}^1
\left[
(T_e+1)\left(\left\lfloor\frac{N-3e}{2}\right\rfloor+1\right)
-\frac{3T_e(T_e+1)}2
\right].
\tag{A.30}
\]
When \(N=0,1,2\), the \(e=1\) value has \(T_e=-1\), so its summand is zero, as required. Formula (A.29) counts the allowable parity of \(y\). Formula (A.30) sums the arithmetic progression of allowable \(x\) values; these are explicit counting proofs.

One tagged polytope in (A.25) therefore has count
\[
[P(U_0-f)-P(L-f-1)]\,C(b-g).
\]
One in (A.26) has count
\[
C(j-f)\,
\begin{cases}
P((b-e)/2),&b-e\ge0\text{ and even},\\
0,&\text{otherwise}.
\end{cases}
\]
One in (A.27) has count
\[
C(j-f)\left[
P\!\left(\left\lfloor\frac{b+1-e}{2}\right\rfloor\right)
-P\!\left(\left\lfloor\frac{-e}{2}\right\rfloor\right)
\right].
\tag{A.31}
\]
The first subtraction counts an interval of lattice points, and the last excludes angular momentum zero; both quantities are nonnegative by their defining sets.

The standalone file [outer4_positive.py](outer4_positive.py) implements (A.19)–(A.31) using only Python's standard library and the fixed integer tag tables. It can also export every tagged polytope as exact equality and inequality matrices, and enumerate its integer witnesses. Its counting routine has no loop whose length grows with \(n\), and uses a fixed number of integer operations. All values have \(O(\log(n+2))\) bits: each template count is bounded by a constant times \((n+1)^3\). Consequently ordinary schoolbook integer arithmetic gives an \(O((\log(n+2))^2)\) bit bound for the arithmetic part, after reading the input. Output partitions of arbitrary length are first checked by the stated zero-support rule.

The direct implementation was compared with all 1,980 independent cycle-index cases and passed. Its witness enumerator separately checked 64,260 exact tagged polytope descriptions, with 2,588 lattice witnesses across the tested coefficients; every point satisfied the exported matrices and every template count equaled its explicit enumeration. The receipt is [OUTER4_DIRECT_POLYTOPE_CHECK.tsv](OUTER4_DIRECT_POLYTOPE_CHECK.tsv), with summary [OUTER4_DIRECT_POLYTOPE_CHECK.txt](OUTER4_DIRECT_POLYTOPE_CHECK.txt) and reproduction code [check_outer4_positive.py](check_outer4_positive.py). The exported [EXAMPLE_642_POLYTOPES.json](EXAMPLE_642_POLYTOPES.json) gives the complete positive count for \(p_{(4),(3)}^{(6,4,2)}=1\).


## Verification and scope

The independent calculation in work/rectangular/verify_outer4_all_formula.py compared (A.9), using literal class traces and fixed-point induction, against power-sum plethysm with the Murnaghan–Nakayama rule. Every one of the 1,980 cases passed: all \(\mu\vdash4\), all \(\lambda\vdash4n\) of length at most four, and \(0\le n\le6\). This includes 750 strict central-chamber cases. The receipt is work/rectangular/OUTER4_ALL_FORMULA_INDEPENDENT_CHECK.tsv. A separate direct evaluator of the tagged polytope formula (A.28) accompanies this report.

The result supplies a direct fixed-template positive formula for every outer Schur label of size four. The proof uses the specified flag chart, the four-point complete intersection, actual equivariant multiplication, and the exact boundary cohomology map. The general terminating construction G-009–G-011 remains valid in every rank; the efficient direct-formula frontier after this result starts beyond outer degree four. No assertion of historical novelty is made for the coefficient family or for its classical ingredients.



# A projective-frame vanishing model in every outer degree

## G-015. The exact flag-sheaf model and its comparison map

Let \(m\ge3\), let \(n\ge0\), and let \(\lambda\vdash mn\) have at most \(m\) parts. Put
\[
E=\mathfrak h_m=\{(q_1,\ldots,q_m):\sum_iq_i=0\},\qquad
\tau=(\lambda_2,\ldots,\lambda_m),\qquad
k=\max(0,\lambda_2-n).
\tag{GF.1}
\]
Use the nondegenerate invariant form \(\sum_iq_iq'_i\) to identify \(E\) and \(E^*\); the restriction is nondegenerate over \(\mathbf Q\), since its orthogonal complement in \(\mathbf Q^m\) is the constant line. Let \(\mathcal F=\operatorname{Flag}(E)\), with tautological subbundles \(\mathcal S_j\), and let
\[
\pi:\mathcal F\longrightarrow\mathbf P(E)
\]
remember the first line. For \(r=m-1\), set \(\tau_{r+1}=0\) and define the \(S_m\)-linearized invertible sheaf
\[
\mathcal L_\tau=
\bigotimes_{j=1}^{r}
(\det\mathcal S_j^*)^{\otimes(\tau_j-\tau_{j+1})}.
\tag{GF.2}
\]
The last factor is the constant determinant line with its actual group action. In particular its contribution includes \(\operatorname{sgn}^{\lambda_m}\); it has not been discarded.

Let \(Z_m\) be the following reduced, \(S_m\)-stable set of \(m\) projective points:
\[
Z_m=\{[\ell_1],\ldots,[\ell_m]\},\qquad
\ell_i=e_i-\tfrac1m\mathbf1.
\tag{GF.3}
\]
They are distinct for \(m\ge3\). Every \(m-1\) of the vectors are independent and their sum is zero, so they form a projective frame.

There is an actual \(S_m\)-equivariant vector-space isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq
H^0\bigl(\mathcal F,
\mathcal L_\tau\otimes\pi^*\mathcal I_{Z_m}^{\,k}\bigr).}
\tag{GF.4}
\]
Thus for every \(\mu\vdash m\),
\[
\boxed{
p_{\mu,(n)}^\lambda=
\dim\operatorname{Hom}_{S_m}\!\left(
[\mu],H^0(\mathcal F,
\mathcal L_\tau\otimes\pi^*\mathcal I_{Z_m}^{\,k})\right).}
\tag{GF.5}
\]
The map in (GF.4) is exactly the balanced flag chart T-032, followed by the polynomial-extension criterion proved below. Its inverse on a section represented by a flag polynomial \(F\) is
\[
F\longmapsto u^{n-\lambda_2}F(v(X)),
\qquad u=\prod_iX_{i1},
\tag{GF.6}
\]
with the polynomial minors \(v\) of (C.3). Formula (GF.4) therefore gives a specified scheme-theoretic vanishing condition for the chart extension in every outer degree.

### 1. Sections and their flag-polynomial realization

The usual Schur/flag identification is
\[
H^0(\mathcal F,\mathcal L_\tau)\simeq S_\tau E^*
\simeq S_\tau E.
\tag{GF.7}
\]
The second map is the Schur functor of the invariant form fixed above. For the first map, a Plücker coordinate is evaluated on each exterior column of a flag frame, and products of these coordinates have precisely the degrees \(\tau_j-\tau_{j+1}\) in (GF.2). This fixes the linearization and the comparison with the polynomial flag algebra, including the full determinant factor. We use the known Borel–Weil identification in this exact form: P. Magyar, *A Borel–Weil Construction for Schur Modules*, arXiv:alg-geom/9411014v1, §2.2, **Proposition 4(a)–(c), printed p. 10**, together with **Proposition 1, pp. 5–6**, relating the section realization to the dual Schur module. The source statements and these explicit comparison maps were read. The standard full-flag pullback in Proposition 4(b) supplies (GF.2) when some adjacent parts agree.

By T-032, the left side of (GF.4) is identified with the subspace of (GF.7) satisfying
\[
u^k\mid F(v(X))\quad\hbox{in }\mathbf Q[X_{ij}].
\tag{GF.8}
\]
It remains to identify this condition with the sheaf in (GF.4). This is a local calculation along the \(m\) original coordinate divisors, and we give it for arbitrary \(m\).

### 2. The first-line coordinates and all transverse parameters

Write the first two matrix columns as \(x=(x_i)\), \(s=(s_i)\). The first smaller-flag vector in the chart is
\[
q=u\left((s_i/x_i)_{i=1}^m
-\tfrac1m\sum_j(s_j/x_j)\mathbf1\right).
\tag{GF.9}
\]
Every coordinate is polynomial: each denominator divides \(u\).

Treat the divisor \(x_m=0\), on the open set where \(x_1,\ldots,x_{m-1},s_m\) are nonzero. Put
\[
x_m=\epsilon,\quad s_m=S,\quad r_j=s_j/x_j\quad(1\le j<m).
\]
At \(\epsilon=0\), (GF.9) is a nonzero scalar multiple of \(\ell_m\). On the first-projective-factor chart \(q_m-q_1\ne0\), the point \([\ell_m]\) has the regular coordinate parameters
\[
a_j=\frac{q_j-q_1}{q_m-q_1},\qquad2\le j\le m-1.
\]
Their exact pullbacks are
\[
\boxed{a_j=\epsilon\frac{r_j-r_1}{S-\epsilon r_1}.}
\tag{GF.10}
\]
They are \(m-2\) independent parameters: the hyperplane equation \(\sum_iq_i=0\), together with \(q_m-q_1=1\), recovers every remaining affine coordinate from them. Because \(\pi\) is a flag bundle, its inverse image \(\mathcal F_m=\pi^{-1}([\ell_m])\) is smooth and the same \(a_j\) are regular parameters transverse to that fiber.

### 3. Independence from every coordinate of the image fiber

We verify the needed generic independence explicitly, including every higher flag coordinate. Restrict the original matrices at \(\epsilon=0\) to the subfamily
\[
X_{mj}=0\quad(3\le j\le m).
\tag{GF.11}
\]
For a minor \(v_{h+1,I}\) from (C.3), its value is zero when \(m\notin I\), because its prefactor then contains \(x_m\). When \(m\in I\), expand the determinant along its last row. Under (GF.11), that row has its sole nonzero entry \(S\) in column two. The result, with its ordinary determinant sign, is
\[
\left(\prod_{i\notin I}x_i\right)S
\det(X_{i,j})_{i\in I\setminus\{m\},\ j\in\{1,3,\ldots,h+1\}}.
\tag{GF.12}
\]
This expression is independent of every \(r_j=s_j/x_j\).

The quotient \(E/\mathbf Q\ell_m\) is identified with
\(\mathbf Q^{m-1}/\mathbf Q\mathbf1\) by restricting to the first \(m-1\) coordinates and then passing to the quotient. This is an isomorphism: its kernel in \(E\) is exactly \(\mathbf Q\ell_m\), and the dimensions agree. In these quotient coordinates, (GF.12) is the exterior flag generated by the arbitrary ratio columns
\[
(X_{ij}/x_i)_{1\le i<m},\qquad3\le j\le m,
\]
modulo their constant line. Their first \(m-2\) quotient columns may be any independent ordered frame. Hence (GF.12) realizes a dense open set of every flag in \(E/\mathbf Q\ell_m\), which is precisely the fiber \(\mathcal F_m\). Rescaling the successive columns realizes its nonzero Plücker frames, including the full determinant frame. All these values remain independent of \(r_1,\ldots,r_{m-1}\).

Consequently the \(m-2\) leading coefficients
\[
(r_j-r_1)/S\quad(2\le j\le m-1)
\]
in (GF.10) are algebraically independent over the function field of the image fiber, and remain independent after choosing any nonzero local Plücker-frame trivialization. This follows from the exhibited subfamily: every fiber flag and frame is attained while those \(m-2\) differences vary freely.

### 4. Equality of orders and global ideal-power membership

Take a nonzero section \(F\) of \(\mathcal L_\tau\). At the generic point of \(\mathcal F_m\), trivialize all its Plücker factors by coordinates nonzero there. Their pulled-back values in (GF.12) are nonzero, so these trivializations have valuation zero along \(x_m=0\). Let \(h\) be the section's order in the fiber ideal. Its first nonzero transverse part belongs to
\[
\mathbf Q(\mathcal F_m)[a_2,\ldots,a_{m-1}]_h.
\]
Under (GF.10) its coefficient of \(\epsilon^h\) is a nonzero homogeneous polynomial in the algebraically independent leading coefficients established above. Therefore it does not vanish. We have proved
\[
\operatorname{ord}_{x_m=0}F(v(X))
=\operatorname{ord}_{\mathcal F_m}F.
\tag{GF.13}
\]
Row permutations give the same equality for every \(i\).

For clarity, order at the generic point of this fiber detects its ordinary sheaf ideal power everywhere. The fiber is smooth and is a regular embedding in the smooth flag variety. Its associated graded ideal sheaf is
\(\operatorname{Sym}_{\mathcal O_{\mathcal F_i}}(\mathcal I_i/\mathcal I_i^2)\), a locally free sheaf on the integral fiber. A section of any such graded piece that is zero at the generic point is zero everywhere. Starting with the restriction modulo \(\mathcal I_i\) and proceeding through degrees \(0,\ldots,k-1\) proves that generic order at least \(k\) is equivalent to local membership in \(\mathcal I_i^k\) throughout the fiber. Outside the fiber this ideal is the whole structure sheaf.

The \(x_i\) are pairwise nonassociate primes in the original polynomial ring. Thus (GF.8) is equivalent to order at least \(k\) along every original divisor. By (GF.13) and the preceding paragraph it is equivalent to membership in every \(\mathcal I_i^k\). The fibers are disjoint, so the intersection of these powers equals their product. The flag bundle \(\pi\) is flat, and the reduced point ideals are pairwise comaximal; hence this product is precisely \(\pi^*\mathcal I_{Z_m}^k\). This proves (GF.4). Taking the explicitly specified \([\mu]\)-covariant summand gives (GF.5), by T-003.

## G-016. The full ideal of the projective frame and its permutation quotient

For every \(m\ge4\), the saturated homogeneous ideal of \(Z_m\subset\mathbf P(E)\) is generated by its quadratic part
\[
U_m=\ker\bigl(\operatorname{Sym}^2 E\longrightarrow\mathbf Q^{Z_m}\bigr),
\qquad\dim U_m=\frac{m(m-3)}2.
\tag{GF.14}
\]
The evaluation map uses the exact affine representatives \(\ell_i\). In every degree \(C\), its homogeneous coordinate quotient \(A\) has the actual \(S_m\)-modules
\[
\boxed{A_0=\mathbf1,\qquad A_1=E,\qquad
A_C=\operatorname{Perm}_m\quad(C\ge2).}
\tag{GF.15}
\]
We prove generation, the scheme statement, and these actions directly.

Choose \(r=m-1\) projective frame points as the coordinate points of \(\mathbf P^{r-1}\). The last point has every coordinate nonzero, and rescaling the coordinates makes it \([1:\cdots:1]\). The quadratic polynomials vanishing at these \(r+1\) points are precisely the linear combinations of \(z_iz_j\), \(i<j\), whose coefficient sum is zero. Thus their ideal is generated by
\[
z_i z_j-z_1z_2\qquad(i<j,\ (i,j)\ne(1,2)).
\tag{GF.16}
\]
Let \(B\) be the quotient by (GF.16), and write \(z=z_1z_2\). All cross-products in \(B\) equal \(z\). For distinct \(i,j\), choose an index \(a\) different from both; this is possible because \(r\ge3\). Then
\[
z_i z=z_i(z_jz_a)=z_j(z_i z_a)=z_j z.
\tag{GF.17}
\]
Multiplying this identity repeatedly shows that every degree-\(C\) mixed monomial, for \(C\ge2\), has the same image \(z z_1^{C-2}\). Therefore \(B_C\) is spanned by
\[
z_1^C,\ldots,z_r^C,\quad z z_1^{C-2}.
\tag{GF.18}
\]
Their evaluations at the \(r\) coordinate points and \([1:\cdots:1]\) are linearly independent: the first \(r\) point rows isolate the first \(r\) coefficients, and the last point then isolates the mixed coefficient. Thus the displayed spanning set is a basis and the evaluation kernel is zero in every degree \(C\ge2\). It is zero in degrees zero and one as well. The quotient by (GF.16) consequently embeds in the product of the coordinate rings of the \(m\) lines through the points, degree by degree. Its kernel is exactly the homogeneous ideal of their union. This proves radicality, saturation, and quadratic generation, without an unsupported claim about a projective set determining its affine scheme.

Return to the canonical affine representatives \(\ell_i\). The evaluation map in degree \(C\) is equivariant, since literal permutation matrices take \(\ell_i\) to \(\ell_{\sigma(i)}\). The degree-two functions \(q_i^2\), \(1\le i\le m\), evaluate to a matrix with diagonal \((1-1/m)^2\) and off-diagonal \(1/m^2\). Its two eigenvalues are \((m-2)/m\) and \((m-1)/m\), both nonzero. The analogous degree-three functions \(q_i^3\) give eigenvalues
\(1-3/m+3/m^2\) and \((m-1)(m-2)/m^2\), also nonzero. Multiplication by the invariant quadratic \(\sum q_i^2\), whose value is the same nonzero number at every \(\ell_i\), propagates surjectivity by two degrees. The coordinate-ring dimensions proved by (GF.18) make each evaluation an isomorphism in degrees \(C\ge2\). Degree one is the standard submodule of the permutation module, and degree zero its constant submodule. This proves every map and action in (GF.15), and dimension subtraction gives (GF.14).

For \(m=3\), the three projective points in \(\mathbf P(E)=\mathbf P^1\) have the principal ideal
\[
\left(\prod_{1\le i<j\le3}(q_i-q_j)\right).
\tag{GF.19}
\]
Each factor vanishes at exactly one of the three points, and their distinct linear factors generate the reduced degree-three divisor ideal. The generator has the sign character under literal row permutations. This also explains the degree-three correction in the rank-three flag formulas through the same map (GF.4).

## Geometric dictionary, scope, and the next exact operation

All objects in (GF.1)–(GF.19) are explicit schemes, locally free sheaves, or coherent ideal sheaves. The invariant form and the points are defined over \(\mathbf Z[1/m]\); their characteristic-zero global-section representations are those used in the stated equalities. The flag scheme is the successive locally free quotient construction, and \(\pi\) is the corresponding relative flag morphism. The comparison is the coordinate-ring morphism (C.3), localized at \(u\), followed by the exact regular-embedding calculation (GF.10)–(GF.13). The affine coordinate dictionary is EGA I 9.5.2–9.5.3, and the group actions are the constant-group comodules of SGA 3 I 4.7.2–4.7.3. Applying the Schur and determinant operations gives the exact representation-group classes of SGA 6 VI 3.3. The complete comparison maps, rather than only equality of dimensions, carry the proof into these frameworks.

For \(m=4\), (GF.16) consists of two quadrics and the full section evaluation is T-037. For \(m\ge5\), (GF.4) and (GF.16) leave a precise new task: evaluate the \(S_m\)-covariant global sections of the displayed powers of this explicitly generated projective-frame ideal. The general finite positive construction G-010 already evaluates every coefficient; the remaining direct-formula problem is to obtain small uniform positive descriptions for these particular section spaces. No vanishing of their higher cohomology or positive splitting of their ideal powers is assumed.


# The five projective-frame points: explicit equivariant resolution

## T-038. Statement and exact matrices

Work over \(\mathbf Q\). Let
\[
E=\mathfrak h_5=\{(q_1,\ldots,q_5):\sum q_i=0\},\qquad
\ell_i=e_i-\tfrac15\mathbf1,
\]
and let \(Z\subset\mathbf P(E)\) be the reduced set of the five lines
\([\ell_i]\). The action is literal coordinate permutation. In the basis
\(\ell_1,\ldots,\ell_4\), these lines are the four coordinate points and
\([1:1:1:1]\), since \(\ell_5=-\sum_{i=1}^4\ell_i\).
Put \(S=\mathbf Q[x,y,z,w]=\operatorname{Sym}(E^*)\). The saturated ideal is
\[
I=(f_1,\ldots,f_5),\quad
f=(xz-xy, xw-xy, yz-xy, yw-xy, zw-xy)^t.
\tag{5R.1}
\]
The following complex is an exact minimal graded free resolution:
\[
0\longrightarrow S(-5)\mathrel{\mathop{\longrightarrow}^{N}}
 S(-3)^5\mathrel{\mathop{\longrightarrow}^{M}}
 S(-2)^5\mathrel{\mathop{\longrightarrow}^{f^t}}I
\longrightarrow0,
\tag{5R.2}
\]
where
\[
M=\begin{pmatrix}
y-w&y&y&y-w&0\\
z-y&-y&-y&-y&-y\\
0&-x&-w&-x&-w\\
0&x&z&0&0\\
0&0&0&x&y
\end{pmatrix},\qquad
N=\begin{pmatrix}
y(x-w)\\z(y-w)\\x(w-y)\\y(w-z)\\x(z-w)
\end{pmatrix}.
\tag{5R.3}
\]
Let \(U=[3,2]\) and \(\epsilon=\operatorname{sgn}\). There are uniquely
specified actions on the spaces of minimal generators and minimal syzygies,
inherited from the action on \(I\). With these actions the resolution is
\[
\boxed{
0\longrightarrow\epsilon\otimes S(-5)
\longrightarrow(\epsilon\otimes U)\otimes S(-3)
\longrightarrow U\otimes S(-2)
\longrightarrow I\longrightarrow0.}
\tag{5R.4}
\]
In particular, sheafification and tensoring by any specified locally free
sheaf give an exact equivariant complex. These are concrete maps: (5R.3)
gives their matrices, and the finite group acts on each syzygy space by
applying its action to its polynomial vectors.

### Proof of the scheme and of exactness

G-016 proves the projective-frame ideal statement for every outer degree.
Here it also has the following short direct verification. In \(S/I\) every
cross-product is equal to \(p=xy\). For distinct indices \(i,j\), choose a
third index \(a\); then
\(z_i p=z_i(z_jz_a)=z_j(z_i z_a)=z_jp\). Hence in degree \(C\ge2\) every
mixed monomial equals \(p x^{C-2}\). The five elements
\[
x^C,y^C,z^C,w^C,px^{C-2}
\tag{5R.5}
\]
are independent by evaluation at the four coordinate points and
\([1:1:1:1]\). The same evaluation is injective in degrees zero and one.
Thus \(S/I\) embeds in the product of the coordinate rings of the five
lines, and its ideal is precisely their reduced union ideal. In particular
\(I\) is saturated and
\[
H_{S/I}(t)=1+4t+\frac{5t^2}{1-t}
=\frac{1+3t+t^2}{1-t}.
\tag{5R.6}
\]

Direct multiplication gives \(f^tM=0\) and \(MN=0\). The upper-left
\(4\times4\) minor of \(M\) is
\[
x(z-w)(xy-wz),
\tag{5R.7}
\]
which is nonzero. Thus the fraction-field kernel of \(M\) is the line
spanned by \(N\). The entries of \(N\) have greatest common divisor one:
already the irreducible factors of \(y(x-w)\) have no common factor with
\(z(y-w)\). If a fraction \(a/b\), in lowest terms, has
\((a/b)N\in S^5\), every irreducible divisor of \(b\) divides all the
entries of \(N\). Therefore \(b\) is a unit. This proves
\(\ker M=S N\), and the left map is injective.

Subtracting (5R.6) from \(H_S(t)=(1-t)^{-4}\) gives
\[
H_I(t)=\frac{5t^2-5t^3+t^5}{(1-t)^4}.
\tag{5R.8}
\]
It follows that \(\ker f^t\) has Hilbert series
\((5t^3-t^5)/(1-t)^4\). The established kernel of \(M\) gives exactly
that series for \(\operatorname{im}M\). Since the latter is contained in
\(\ker f^t\), their degree-by-degree dimensions prove equality. All
matrix entries have positive degree, so the resolution is minimal.

### The actual finite-group labels

The canonical affine representatives \(\ell_i\) are permuted without
rescaling. Consequently evaluation gives
\[
(S/I)_0=\mathbf1,\qquad(S/I)_1=E^*,\qquad
(S/I)_C=\operatorname{Perm}_5\quad(C\ge2)
\tag{5R.9}
\]
as actual \(S_5\)-modules. An invariant nondegenerate form identifies
\(E^*\) with \(E\). Write the conjugacy classes in the order
\[
1^5,\quad21^3,\quad2^21,\quad31^2,\quad32,\quad41,\quad5.
\tag{5R.10}
\]
The character of \(I_2=\operatorname{Sym}^2E-\operatorname{Perm}_5\) is
\[
(5,1,1,-1,1,-1,0),
\tag{5R.11}
\]
which is the irreducible character \([3,2]\). For example the character
can be computed directly from
\(\chi_{\operatorname{Sym}^2E}(g)=
(\chi_E(g)^2+\chi_E(g^2))/2\); the irreducible labels agree with the
primary character table in Dolgachev–Farb–Looijenga,
*Geometry of the Wiman–Edge pencil I*, §2.3, Table 1, printed p. 10.

The degree-three syzygy character is
\[
\chi_E\chi_U-\chi_{\operatorname{Sym}^3E}
 +\chi_{\operatorname{Perm}_5}
=(5,-1,1,-1,-1,1,0)=\chi_{[2,2,1]}.
\tag{5R.12}
\]
This follows either by the degree-three exact sequence, or by expanding
\(\prod_{\xi\in\operatorname{eig}(g|E)}(1-t\xi)^{-1}\) to degree three.
It fixes the action on the columns of \(M\).

There is one final generator. At a transposition \(s\), the equivariant
Hilbert series of \(S/I\) is \((1+t+t^2)/(1-t)\), whereas that of \(S\)
is \(((1-t)^3(1+t))^{-1}\). Their ratio is
\[
1-t^2-t^3+t^5.
\tag{5R.13}
\]
In the alternating numerator of (5R.2) the final coefficient is
\(-\chi_K(s)t^5\). Thus \(\chi_K(s)=-1\). Every one-dimensional
representation of \(S_5\) is determined by its common value on the
transpositions, which generate the group, so \(K=\epsilon\). This proves
(5R.4), including its final determinant character.

For an alternating form of the middle map, set
\[
P=\begin{pmatrix}
0&0&0&-1&0\\0&0&1&0&-1\\0&1&0&0&0\\
0&0&-1&1&0\\1&-1&0&0&0
\end{pmatrix}.
\]
Then \(\det P=-1\), \(N=Pf\), and
\[
MP=\begin{pmatrix}
0&y&w&0&-y\\-y&0&0&-z&y\\-w&0&0&-x&x\\
0&z&x&0&-x\\y&-y&-x&x&0
\end{pmatrix}.
\tag{5R.14}
\]
Its signed maximal Pfaffians are \(f\). Thus the five-point ideal also
comes with a specified alternating presentation, as used in the separate
application of Kustin–Polini–Ulrich in the archive report. The elementary
exactness proof above does not need an unverified generic perfection claim.

## The quadratic subalgebra and its six-coordinate morphism

This subsection records an exact comparison useful for the higher powers.
Let \(A,B,C,D,E_0\) be independent indeterminates mapping to the five
entries of \(f\), in that order. Then
\[
\boxed{\mathbf Q[f_1,\ldots,f_5]
\simeq\mathbf Q[A,B,C,D,E_0]/(F),\qquad
F=AD(E_0-B-C)-BC(E_0-A-D).}
\tag{5R.15}
\]
The variable \(E_0\) is distinguished from the standard module \(E\).
Substitution verifies \(F(f)=0\). In the fraction field of the image,
\[
xy=\frac{AD}{E_0-A-D},\qquad
xz=xy+A,\quad xw=xy+B,\quad yz=xy+C,
\tag{5R.16}
\]
and similarly for the other cross-products. In particular
\(x^2=(xy)(xz)/(yz)\). The full rational function field
\(\mathbf Q(x,y,z,w)\) is algebraic over the image's fraction field:
adjoin a square root \(x\) of this displayed \(x^2\), then recover
\(y,z,w\) by division. The image has transcendence degree four.

As a polynomial in \(E_0\), \(F\) has coefficient \(AD-BC\), an
irreducible determinant. This coefficient does not divide the constant
term: at \((A,B,C,D)=(1,2,3,6)\) the coefficient is zero and the constant
term is nonzero. The coefficient and constant term are therefore coprime.
Gauss's lemma and the degree-one polynomial over \(\mathbf Q(A,B,C,D)\)
prove that \(F\) is irreducible. The kernel has height one and contains
\(F\); since the target is a domain this proves (5R.15). The transposition
\(x\leftrightarrow y\) sends
\((A,B,C,D,E_0)\) to \((C,D,A,B,E_0)\) and sends \(F\) to \(-F\).
Its relation line is therefore \(\epsilon\).

Here is a rational linear comparison with the usual six-coordinate
Segre cubic. Set
\[
\begin{aligned}
t_1&= A+B-C+D-E_0,&t_2&=-A+B+C-D-E_0,\\
t_3&=-A+B+C-D+E_0,&t_4&=-A-B-C+D+E_0,\\
t_5&= A-B-C-D+E_0,&t_6&= A-B+C+D-E_0.
\end{aligned}
\tag{5R.17}
\]
These forms have rank five and satisfy
\[
\sum_{i=1}^6t_i=0,\qquad\sum_{i=1}^6t_i^3=-24F.
\tag{5R.18}
\]
For precision, the associated action on six letters is the conjugation
action of \(S_5\) on its six subgroups of order five. Index those subgroups
by lexicographically ordering their permutation tuples, as in the
certificate script. The six forms in (5R.17) obey
\[
g(t_i)=\epsilon(g)t_{g(i)}.
\tag{5R.19}
\]
There is also a group-theoretic way to specify these exact forms without
guessing an outer automorphism. If \(H_0\) is the first such subgroup,
average \(\epsilon(g)\rho_U(g)\) over its twenty-element normalizer.
Its image is a line. Take the first nonzero column, clear denominators
and divide by the positive gcd of its integer entries. For a subgroup
\(gH_0g^{-1}\), transport this vector by \(\epsilon(g)\rho_U(g)\).
This is independent of the chosen transporter because of the normalizer
character. It gives precisely (5R.17). Multiplication by every one of the
120 group elements was checked against (5R.19).

The conjugacy-class map, in the order (5R.10), is
\[
1^6,\quad2^3,\quad2^21^2,\quad3^2,\quad6,\quad41^2,\quad51.
\tag{5R.20}
\]
Equations (5R.17)–(5R.20) specify both the cubic isomorphism and the
finite-group intertwiner. This agrees with the classical five-point
quadratic map: Dolgachev–Farb–Looijenga, Remark 2.4, printed p. 13,
describes the five-point map and its Segre cubic image; Dolgachev,
*Corrado Segre and nodal cubic threefolds*, §2, equation (2.1), gives the
six-coordinate equations. We do not attach a novelty claim to this
classical comparison.

## Sources and checks

- [Dolgachev–Farb–Looijenga, *Geometry of the Wiman–Edge pencil I*](https://www.math.uchicago.edu/~farb/papers/wiman.pdf),
  §2.3, Table 1, printed p. 10, and Remark 2.4, printed p. 13. Both
  passages were opened and read in this run.
- [Dolgachev, *Corrado Segre and nodal cubic threefolds*](https://sites.lsa.umich.edu/idolga-new/wp-content/uploads/sites/1467/2024/08/segre15.pdf),
  §2, especially equation (2.1) and the five-point quadratic map.
- `check_five_points.py` verifies the two zero matrix products, the
  primitive kernel, the nonzero minor, cubic substitution, six-form rank,
  all 120 group intertwining identities and the class map. The full
  receipt is `FIVE_POINT_EXACT_MAPS.txt`.
- `check_five_point_positive.py` additionally checks the entire
  equivariant Hilbert numerator on all seven classes. The matrices and
  the degree-by-degree exactness proof specify the complex independently
  of those finite checks.

The next result, T-039, evaluates a family of quotient-bundle sections
from this actual resolution. General arbitrary powers with arbitrary
Schur quotient bundles remain a separate direct-evaluation task; G-010
already supplies a terminating finite positive count for all plethysm
coefficients.

The rectangular agent independently read the complete proof and checked
the actual \(M,N,P\) products, signed Pfaffians, scalar \(-24\), and all
120 signed actions using the five affine frame vectors. Every check
passed. Its independent code and receipt are
`work/rectangular/verify_five_point_matrices.py` and
`work/rectangular/FIVE_POINT_MATRIX_INDEPENDENT_CHECK.txt`.


# A positive higher-flag family in outer degree five

## T-039. The coefficient formula

For integers \(a,d\ge0\), set
\[
n=d+a+1,\qquad
\lambda=(d+2a+3,\ d+a+2,\ d+a,\ d+a,\ d).
\tag{5F.1}
\]
This is a partition of \(5n\). Let \(E=\mathfrak h_5\),
\(U=[3,2]\), and \(\epsilon=\operatorname{sgn}_{S_5}\). There is an
actual equivariant isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes
\left(U\otimes\operatorname{Sym}^a E
\;\oplus\;\operatorname{Sym}^{a-1}E\right),}
\tag{5F.2}
\]
where \(\operatorname{Sym}^{-1}E=0\). The direct sum is a splitting of a
specified equivariant short exact sequence; it need not be a canonical
splitting. Consequently every outer Schur coefficient
\(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), is a sum of at most 36
fixed, four-variable lattice-point counts. The numbers and inequalities
are specified in §4 below. There is no coefficient precomputation depending
on \(a\), \(d\), or \(n\).

The passage from the balanced weight space to (5F.2) is the polynomial
chart and extension morphism of T-032/G-015, followed by explicit exterior
pairings and the exact resolution (5R.3). We prove each remaining step.

## 1. From the flag model to a quotient-bundle section

Use the canonical \(S_5\)-invariant form on \(E\) to identify \(E\)
and \(E^*\). On \(\mathbf P(E)\), which parametrizes lines, let
\[
0\longrightarrow\mathcal O(-1)\longrightarrow E\otimes\mathcal O
\longrightarrow Q\longrightarrow0
\tag{5F.3}
\]
be the tautological quotient sequence. Thus \(Q\) has rank three. Let
\(Z=\{[e_i-\frac15\mathbf1]:1\le i\le5\}\), and write
\(\mathcal I=\mathcal I_Z\).

The numbers in (5F.1) satisfy
\[
\lambda_2-n=1,\qquad \lambda_2-\lambda_3=2,
\qquad\lambda_3-\lambda_4=0,\qquad\lambda_3-\lambda_5=a.
\tag{5F.4}
\]
G-015 therefore identifies the balanced module with
\[
H^0\!\left(\operatorname{Flag}(E),
\mathcal L_{(d+a+2,d+a,d+a,d)}\otimes\pi^*\mathcal I\right),
\tag{5F.5}
\]
where \(\pi\) remembers the first line. This is the actual comparison
map: a flag polynomial \(F\) is sent back to the original matrix ring by
\(u^{-1}F(v(X))\). G-015 proves that membership in (5F.5) is precisely
what makes this rational expression a polynomial, using the exact
transverse ratios along every first-column coordinate divisor.

We describe the pushforward in (5F.5), including all determinant factors.
The full determinant factor of \(\mathcal L\) is
\((\det E^*)^d\). After removing it, the first weight is \(a+2\)
and the relative quotient-flag weight is \((a,a,0)\). The standard
Plücker evaluation on the flag of the rank-three quotient gives
\[
\pi_*\mathcal L_{(d+a+2,d+a,d+a,d)}
\simeq (\det E^*)^d\otimes\mathcal O(a+2)
                  \otimes S_{(a,a)}Q^*.
\tag{5F.6}
\]
The relative identification can be checked on every open set trivializing
\(Q\): there it is the usual Schur realization by the degree-\((a,a)\)
flag minors, and changes of quotient frame act by that same Schur functor.
The local maps therefore glue. This is the Borel–Weil/Schur comparison in
Magyar, Proposition 1, printed pp. 5–6, and Proposition 4(a)–(c), printed
p. 10, with the bundle linearization specified by its exterior columns.

For a rank-three vector space or bundle, the wedge pairing is the actual
map
\[
\Lambda^2Q^*\simeq Q\otimes\det Q^*.
\tag{5F.7}
\]
Its \(a\)-th symmetric power identifies
\(S_{(a,a)}Q^*=\operatorname{Sym}^a(\Lambda^2Q^*)\) with
\((\det Q^*)^a\otimes\operatorname{Sym}^aQ\). The asserted equality
with the Schur functor follows as well from the map on the highest vector
\((q_1^*\wedge q_2^*)^a\): its irreducible span has weight \((a,a,0)\)
and the dimensions on both sides are \(\binom{a+2}{2}\). Taking
determinants in (5F.3) gives
\[
\det Q^*\simeq\det E^*\otimes\mathcal O(-1).
\tag{5F.8}
\]
Thus (5F.6) becomes
\[
\pi_*\mathcal L\simeq
(\det E^*)^{d+a}\otimes\mathcal O(2)\otimes\operatorname{Sym}^aQ.
\tag{5F.9}
\]

Projection with the ideal factor causes no hidden flatness assumption.
Locally on the base, the flag bundle is a product with the fixed flag
variety. A finite affine Čech complex for its line bundle consists of
modules obtained from vector spaces over \(\mathbf Q\), tensored with
the base ring. Tensoring this complex with the local ideal commutes with
its degree-zero cohomology: every exact sequence of vector spaces over
\(\mathbf Q\) splits. These local maps agree on overlaps. Equivalently
one can use the usual relative Schur section map and its base-change
property. Hence (5F.5)–(5F.9) give the specified isomorphism
\[
\boxed{
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq \epsilon^{d+a}\otimes
H^0(\mathbf P(E),\mathcal I(2)\otimes\operatorname{Sym}^aQ).}
\tag{5F.10}
\]
Here \(\det E=\epsilon\), because the full five-dimensional permutation
module is \(\mathbf1\oplus E\). This determines the twist directly.

## 2. The three bundle cohomology calculations

Write \(B_a=\operatorname{Sym}^aQ\). Multiplication by the tautological
line in (5F.3) is the first map of the exact sequence
\[
0\longrightarrow\mathcal O(t-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal O(t)\otimes\operatorname{Sym}^{a}E
\longrightarrow B_a(t)\longrightarrow0.
\tag{5F.11}
\]
The sequence is exact fiber by fiber: the kernel of
\(\operatorname{Sym}^aE\to\operatorname{Sym}^a(E/L)\) is exactly
\(L\operatorname{Sym}^{a-1}E\), and multiplication by a nonzero vector
of the line \(L\) is injective in a symmetric algebra. It is therefore
an exact sequence of locally free sheaves. For \(a=0\), its left term
is zero.

The projective-space cohomology used here is
\[
H^i(\mathbf P^3,\mathcal O(t))=0\quad(0<i<3),
\]
with \(\mathcal O(-1),\mathcal O(-2),\mathcal O(-3)\) acyclic and
\(H^3(\mathcal O(-4))=\det E\). The scalar vanishing ranges follow
from the full monomial Čech calculation in Stacks Project, Lemma 30.8.1,
tag 01XS. The determinant action can be read from its top Čech generator:
for an ordered coordinate basis \(x_1,\ldots,x_4\), it is the class of
\(1/(x_1x_2x_3x_4)\); the ordered Čech orientation and change of basis
make its action \(\det E\). The same conclusion follows from the
canonical-bundle identification
\(\omega_{\mathbf P(E)}=\mathcal O(-4)\otimes\det E^*\).

Apply (5F.11) with \(t=0,-1,-3\). It gives all the following groups,
not merely their Euler characteristics:
\[
\begin{array}{c|c|c}
\text{bundle}&\text{only possible nonzero cohomology}&\text{module}\\\hline
B_a&H^0&\operatorname{Sym}^aE\\
B_a(-1)&\text{none}&0\\
B_a(-3)&H^2&\epsilon\otimes\operatorname{Sym}^{a-1}E.
\end{array}
\tag{5F.12}
\]
The last row is zero when \(a=0\), as required.

## 3. The positive exact sequence

Sheafify the exact resolution (5R.4), twist by \(\mathcal O(2)\), and
tensor with the locally free sheaf \(B_a\). This gives
\[
0\longrightarrow\epsilon\otimes B_a(-3)
\longrightarrow(\epsilon\otimes U)\otimes B_a(-1)
\longrightarrow U\otimes B_a
\longrightarrow\mathcal I(2)\otimes B_a\longrightarrow0.
\tag{5F.13}
\]
Let \(K\) be the image of its middle map into \(U\otimes B_a\).
The first short exact sequence and (5F.12) give
\[
H^0(K)=0,\qquad
H^1(K)=\operatorname{Sym}^{a-1}E,
\qquad H^i(K)=0\ (i\ge2).
\tag{5F.14}
\]
The two sign factors in \(H^1(K)\) are the last syzygy character of
(5R.4) and the top projective cohomology character of (5F.12); their
tensor product is trivial. The second short exact sequence therefore
gives
\[
\boxed{
0\longrightarrow U\otimes\operatorname{Sym}^a E
\longrightarrow H^0(\mathcal I(2)\otimes B_a)
\longrightarrow\operatorname{Sym}^{a-1}E
\longrightarrow0.}
\tag{5F.15}
\]
The first arrow multiplies a quadratic vanishing at \(Z\) by a constant
section of \(\operatorname{Sym}^aE\), followed by the quotient
\(\operatorname{Sym}^aE\to B_a\). The last arrow is the connecting
homomorphism of the actual resolution. This specifies the morphisms
underlying the positive decomposition.

Every sequence of finite-dimensional \(\mathbf Q[S_5]\)-modules splits:
average any linear section over the 120 group elements. Applying this
to (5F.15) and composing with (5F.10) proves (5F.2). It also proves
\[
\dim(S_\lambda\mathbf Q^5)_{(n^5)}
=5\binom{a+3}{3}+\binom{a+2}{3}.
\tag{5F.16}
\]
The equality for \(a=0\) is the single module \(U\), with no extra
cohomology term.

## 4. Fixed positive polytopes for every outer partition

Define the bounded rational polytope
\[
P(R)=\{(x_2,x_3,x_4,x_5)\in\mathbf R_{\ge0}^4:
2x_2+3x_3+4x_4+5x_5=R\},
\qquad C(R)=\#(P(R)\cap\mathbf Z^4).
\tag{5F.17}
\]
For \(R<0\) it is empty. Every integer coordinate is at most
\(\max(0,R)/2\), so no unbounded component is being counted.

The seven multisets below are the comajor indices of standard tableaux
of the indicated shape. For a tableau of size five, our convention is
\(\operatorname{comaj}T=\sum_{i:\,i+1\text{ is below }i}(5-i)\).
Repeated entries are distinct tableau tags.

| \(\rho\) | multiset \(D_\rho\) | dimension |
|---|---|---:|
| \((5)\) | \(0\) | 1 |
| \((4,1)\) | \(1,2,3,4\) | 4 |
| \((3,2)\) | \(2,3,4,5,6\) | 5 |
| \((3,1,1)\) | \(3,4,5,5,6,7\) | 6 |
| \((2,2,1)\) | \(4,5,6,7,8\) | 5 |
| \((2,1,1,1)\) | \(6,7,8,9\) | 4 |
| \((1^5)\) | \(10\) | 1 |

The exact standardization argument of T-027 gives
\[
\dim\operatorname{Hom}_{S_5}([\rho],\operatorname{Sym}^aE)
=\sum_{r\in D_\rho}C(a-r).
\tag{5F.18}
\]
In that proof, weak entries in a semistandard tableau become a standard
tableau plus nonnegative increments, and the forced strict inequalities
contribute precisely its comajor. The constant-line factor in the
permutation module removes the denominator of degree one, leaving the
four denominators \(2,3,4,5\) in (5F.17). Thus (5F.18) has an actual
tableau-to-lattice bijection. Here all tableau tags are already listed.

Let \(K_{\rho\nu}\) be the multiplicity of \([\nu]\) in
\(U\otimes[\rho]\). It is completely specified by the following table;
repetition denotes multiplicity two.

| \(\rho\) | summands of \(U\otimes[\rho]\) |
|---|---|
| \((5)\) | \((3,2)\) |
| \((4,1)\) | \((4,1),(3,2),(3,1,1),(2,2,1)\) |
| \((3,2)\) | \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1)\) |
| \((3,1,1)\) | \((4,1),(3,2),(3,1,1),(3,1,1),(2,2,1),(2,1,1,1)\) |
| \((2,2,1)\) | \((1^5),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1)\) |
| \((2,1,1,1)\) | \((2,1,1,1),(2,2,1),(3,1,1),(3,2)\) |
| \((1^5)\) | \((2,2,1)\) |

This finite tensor table follows by multiplying the seven character rows
of the primary Table 1 quoted in T-038 and taking the class-size-weighted
inner products. In particular it requires no variable-size Kronecker
coefficient computation. All 49 entries were also recomputed by an
independent Murnaghan–Nakayama implementation.

For \(\mu\vdash5\), put
\[
\nu=\begin{cases}\mu&d+a\text{ even},\\\mu^t&d+a\text{ odd}.
\end{cases}
\tag{5F.19}
\]
Taking the \([\mu]\)-covariant part in the balanced-space dictionary
T-003 and then using (5F.2) and (5F.18) yields
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_{\rho\vdash5}K_{\rho\nu}
       \sum_{r\in D_\rho}C(a-r)
 +\sum_{r\in D_\nu}C(a-1-r).}
\tag{5F.20}
\]
Each summand has a fixed tag \((\rho,\text{copy},\text{tableau})\) or
\((\nu,\text{tableau})\), followed by one point of (5F.17). This is a
finite disjoint union of bounded lattice polytopes. Negative right sides
give empty polytopes and may be retained in the uniform list.

All these modules are self-dual. Hence
\(\sum_\rho K_{\rho\nu}\dim[\rho]=5\dim[\nu]\), by the dimension
of \(U\otimes[\nu]\). The second sum has \(\dim[\nu]\) tags. The
total number is exactly \(6\dim[\nu]\le36\), including empty tags.
Each polytope has four variables, one displayed equality, and four
nonnegativity inequalities. Its coefficients are fixed and its right
side has \(O(\log(a+2))\) bits. This gives a fixed-dimensional positive
formula in the ordinary binary input encoding for \(a,d\).

## 5. The symmetric outer power and its complete support criterion

For \(\mu=(5)\), (5F.20) is particularly short:
\[
\boxed{
p_{(5),(n)}^\lambda=
\begin{cases}
\displaystyle\sum_{j=1}^{6}C(a-j),&d+a\text{ even},\\[2mm]
\displaystyle\sum_{j=4}^{8}C(a-j)+C(a-11),&d+a\text{ odd}.
\end{cases}}
\tag{5F.21}
\]
Both lists have six tags. The numerical semigroup generated by
\(2,3,4,5\) is \(\{0\}\cup\{r:r\ge2\}\): every even \(r\ge2\)
uses twos and every odd \(r\ge3\) uses one three and twos. Therefore
\[
\boxed{
p_{(5),(n)}^\lambda>0
\quad\Longleftrightarrow\quad
\begin{cases}
a\ge1,&d+a\text{ even},\\
a\ge4,&d+a\text{ odd}.
\end{cases}}
\tag{5F.22}
\]
To check the endpoints explicitly, in the first case \(a=1\) uses the
tag \(j=1\), and \(a=2\) uses \(j=2\); larger \(a\) use either a
zero residual or a residual at least two. In the second case the tags
\(j=4,5\) handle \(a=4,5\), and \(j=4\) handles every \(a\ge6\).
Below these thresholds all listed right sides are negative.

## 6. Exact implementation, independent checks, and scope

`five_point_positive.py` is a standalone Python standard-library
evaluator. It contains exactly the two fixed tables above, exports the
tagged equations, and enumerates their integer witnesses. It accepts
\(a,d,\mu\), checks that \(a,d\) are nonnegative integers and that
\(\mu\) is a partition of five, and returns (5F.1) and (5F.20).
For example:

```text
python work/theta/outer5/five_point_positive.py --a 4 --d 0 --outer 5 --polytopes
```

The implementation uses the positive coin recurrence for evaluation;
its polytope description has fixed size, regardless of that elementary
counting implementation. No character, elimination, or plethysm oracle
is called by the evaluator.

`check_five_point_positive.py` recomputed all seven tableau degree lists,
all 49 tensor entries, the seven exact rational character identities
behind (5F.18), and every equivariant resolution numerator of T-038.
It also compared the positive count with literal tagged lattice
enumeration in 434 cases, producing 118,334 explicit witnesses. Every
check passed. Receipts: `FIVE_POINT_POSITIVE_CHECK.tsv` and `.txt`.

Independently, the rectangular agent computed all seven outer Schur
cycle indices and used Murnaghan–Nakayama on the output partitions.
All 147 cases with \(a,d\ge0\), \(d+a+1\le6\), matched (5F.2).
On the proposed side, that calculation used permutation-cycle traces
for \(\operatorname{Sym}^a\mathfrak h_5\) and the character
\(\binom{m_1}{2}+m_2-m_1\) for \([3,2]\), independently of the
resolution and the fixed tag table. Code and receipt:
`work/rectangular/verify_outer5_fivepoint_family.py` and
`work/rectangular/OUTER5_FIVEPOINT_INDEPENDENT_CHECK.tsv`.

The same independent reader subsequently read the complete T-038 and
T-039 proofs, including every bundle map, the two sign cancellations,
the finite tag lists and all support endpoints, and found no gap.

Primary sources read for this proof:

- [Magyar, *A Borel–Weil Construction for Schur Modules*](https://arxiv.org/pdf/alg-geom/9411014),
  Proposition 1, printed pp. 5–6, and Proposition 4(a)–(c), printed p. 10.
  The exterior-column comparison fixes the precise dual convention in
  (5F.6); the maps (5F.7)–(5F.9) then determine all twists.
- [Stacks Project, Lemma 30.8.1, tag 01XS](https://stacks.math.columbia.edu/tag/01XS),
  including its monomial Čech proof. Only the three exact bundle
  cohomology computations in (5F.12) are imported from these scalar
  vanishings.
- [Dolgachev–Farb–Looijenga, *Geometry of the Wiman–Edge pencil I*](https://www.math.uchicago.edu/~farb/papers/wiman.pdf),
  §2.3, Table 1, printed p. 10, for the fixed \(S_5\) labels and table.

For \(a>0\), the section space in (5F.10) has the nontrivial quotient
bundle \(\operatorname{Sym}^aQ\), and (5F.15) evaluates it in full.
The result is an explicit bounded family within the general
projective-frame model. It makes no global novelty claim and assumes
no vanishing for arbitrary point powers or arbitrary Schur quotient
bundles. G-010 provides the general terminating positive count; T-037
already gives a fixed finite formula for every outer partition of four.


# A positive five-point quotient-bundle family in every multiplicity

## G-017. A fixed positive formula on a varying five-row family

For integers \(k,d\ge0\), put
\[
n=d+k+1,\qquad
\lambda=(d+3k+2,d+2k+1,d+1,d+1,d).
\tag{Q.1}
\]
The parts sum to \(5n\) and are weakly decreasing. Let \(\mu\vdash5\),
and put \(\nu=\mu\) for odd \(d\) and \(\nu=\mu'\) for even \(d\).
For an integer \(R\), define the bounded polytope
\[
\mathscr P(R)=\{x\in\mathbf R_{\ge0}^4:
2x_1+4x_2+6x_3+10x_4=R\},\qquad
N(R)=\#(\mathscr P(R)\cap\mathbf Z^4).
\tag{Q.2}
\]
It is empty for \(R<0\). The following formula is positive, with fixed
nonnegative integers \(h_{\nu,j}\) displayed in §6:
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{j=0}^{19}h_{\nu,j}N(k-j).}
\tag{Q.3}
\]
Equivalently, use \(h_{\nu,j}\) distinct tags for the polytope
\(\mathscr P(k-j)\). There are at most 216 tagged polytopes, and exactly
36 tags for the symmetric or alternating outer partition. Their dimension,
coefficients, and number are independent of both parameters. The evaluator
in §7 uses a fixed number of integer arithmetic operations.

The proof constructs the relevant geometric section module, its explicit
matrix presentation, and an equivariant free multiplication map over four
invariant parameters. The finite character calculation only determines the
graded types of the actual quotient module at the end of this construction.

## 1. The exact flag comparison and its determinant twist

Let \(E=\mathfrak h_5\), with the invariant pairing and projective-frame
vectors \(\ell_i=e_i-\frac15\mathbf1\) fixed in G-015. On \(\mathbf P(E)\)
let \(Q\) be the tautological rank-three quotient, and let \(\mathcal I\)
be the ideal sheaf of the five points \([\ell_i]\). Define
\[
M_k=H^0\bigl(\mathbf P(E),\mathcal I^k(2k)\otimes Q\bigr),
\qquad M=\bigoplus_{k\ge0}M_k.
\tag{Q.4}
\]
G-015 gives the actual balanced-chart map for (Q.1), since
\(\lambda_2-n=k\). After removing the full determinant factor
\((\det E^*)^d\), the relative quotient-flag weight is \((1,1,0)\)
and the first-line weight is \(2k+1\). The relative Plücker evaluation,
the exterior pairing \(\Lambda^2 Q^*\simeq Q\otimes\det Q^*\), and
\(\det Q^*\simeq\det E^*\otimes\mathcal O(-1)\) therefore identify the
pushforward with
\[
(\det E^*)^{d+1}\otimes\mathcal O(2k)\otimes Q.
\]
These maps are exactly those in (5F.6)–(5F.9) for relative weight
\((1,1,0)\); their local quotient-frame definitions glue and commute
with tensoring the base ideal, as proved in T-039 §1. Consequently
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+1}\otimes M_k.}
\tag{Q.5}
\]
The inverse chart sends a flag polynomial \(f\) to \(u^{-k}f(v(X))\).
Its extension to a polynomial is equivalent to the ideal membership in
(Q.4) by the transverse-order proof G-015. Thus (Q.5) includes the map,
the sheaf condition, and its group linearization.

## 2. An invariant section and five exact relations

Use \(\ell_1,\ldots,\ell_4\) as a basis, and write its coordinates as
\(z_1,\ldots,z_4\). The fifth point has coordinates \([1:1:1:1]\).
Write
\[
\begin{aligned}
f_A&=z_1z_3-z_1z_2,& f_B&=z_1z_4-z_1z_2,\\
f_C&=z_2z_3-z_1z_2,& f_D&=z_2z_4-z_1z_2,&
f_E&=z_3z_4-z_1z_2.
\end{aligned}
\tag{Q.6}
\]
Let \(U=\langle f_A,f_B,f_C,f_D,f_E\rangle=[3,2]\), and set
\[
S=\mathbf Q[A,B,C,D,E],\quad
F=AD(E-B-C)-BC(E-A-D),\quad C=S/(F).
\tag{Q.7}
\]
Each variable in \(S\) has degree one. By T-038, substitution
\(A\mapsto f_A,\ldots,E\mapsto f_E\) has kernel exactly \((F)\),
and \(F\) has sign character. Hence \(C\) acts on (Q.4) by multiplication.

The class of \((z_1^2,z_2^2,z_3^2,z_4^2)\) modulo the tautological line
defines
\[
\theta\in M_1.
\tag{Q.8}
\]
At every coordinate point and at \((1,1,1,1)\) this vector is proportional
to the point vector, so it vanishes in the quotient fiber. To verify its
linearization, write \(q=\sum z_i\ell_i\) and \(s=\sum z_i\). The
\(S_5\)-equivariant quadratic map
\(q\mapsto(q_i^2-\frac15\sum_jq_j^2)_i\) has coordinates
\(z_i^2-\frac25sz_i\) in this basis. Its quotient class is (Q.8).
Therefore \(\theta\) is invariant under the actual \(S_5\) action.

Here is a small polynomial matrix that specifies all the relations. Put
\[
K=\begin{pmatrix}
0&E-B&0&-C&-BC+BD+CD-DE\\
0&A-E&D&0&-AC+AD-CD+CE\\
D-E&0&0&A&-AB+AD-BD+BE\\
E-C&0&-B&0&AB+AC-AE-BC\\
C-D&B-A&0&0&-AD+BC
\end{pmatrix},\qquad
P=\frac{\operatorname{adj}K}{F}.
\tag{Q.9}
\]
All entries of \(\operatorname{adj}K\) are divisible by \(F\).
The first four rows of \(P\), denoted by \(\Phi\), have degree two;
its last row is \((-A,-B,-C,-D,-E)\). Expansion of the determinants gives
\[
\det K=3F^2,\qquad PK=KP=3F I_5,\qquad\det P=81F^3.
\tag{Q.10}
\]
These are identities in the polynomial ring \(S\). They are also
reproduced by exact symbolic arithmetic in `five_point_q_module.py` and
`FIVE_POINT_Q_RELATIONS.json`; (Q.9) specifies the matrix independently
of those files.

For complete verification of the substitution relations, put
\[
\begin{aligned}
h_A&=f_A(z_1+z_2+z_3-2z_4),&
h_C&=f_C(z_1+z_2+z_3-2z_4),\\
h_B&=f_B(z_1+z_2+z_4-2z_3),&
h_D&=f_D(z_1+z_2+z_4-2z_3),\\
h_E&=z_3z_4(z_3+z_4-2z_1-2z_2)
      -z_1z_2(z_1+z_2-2z_3-2z_4).
\end{aligned}
\tag{Q.11}
\]
The twenty polynomial identities, for \(1\le i\le4\) and
\(j\in\{A,B,C,D,E\}\), are
\[
f_jz_i^2-\Phi_{ij}(f_A,f_B,f_C,f_D,f_E)=z_i h_j.
\tag{Q.12}
\]
They follow by substituting (Q.6) into the minors in (Q.9) and expanding;
the right sides (Q.11) give their explicit line corrections. Thus the
columns of \(P\) are actual relations on the constant sections \(E\)
and the section \(\theta\), not just relations on their dimensions.

The relation space carries the representation \(U\). Indeed the map
\(E\otimes\operatorname{Sym}^2U\to M_2\) is injective. A kernel
would be a vector polynomial in the tautological line, hence a multiple
\(z h\) with \(h\in H^0(\mathcal I^2(3))\). A cubic double at all four
coordinate points is a linear combination of the four squarefree cubics.
At \((1,1,1,1)\), let their coefficients be \(c_i\), indexed by the
missing variable. Its four first derivatives are \(\sum_jc_j-c_i\).
Their simultaneous vanishing implies \(c_i=\sum_jc_j\) for every
\(i\), whence \(3\sum_jc_j=0\) and every coefficient is zero. Also
\(\operatorname{Sym}^2U\to C_2\) is injective because the first relation
\(F\) has degree three. This proves the asserted injectivity. It makes
the coefficient \(\Phi(f)\) in \(f\theta=\Phi(f)\) unique. Applying
an element of \(S_5\) to that equality shows that its five-dimensional
relation space is the image of the equivariant map from \(U\).

Define the graded module
\[
\mathcal M=\operatorname{coker}\left[
S(-2)\otimes U\xrightarrow{P}
(S\otimes E)\oplus S(-1)\right].
\tag{Q.13}
\]
The determinant (Q.10) makes the displayed map injective. Equations
(Q.12) define an equivariant graded map \(\mathcal M\to M\), and
\(PK=3FI\) shows that \(F\mathcal M=0\).

## 3. The presentation injects into the section module

We first verify that \(\mathcal M\) has no torsion over the integral
domain \(C\). Let \(g\in S\) have nonzero image in \(C\), and suppose
\(gv=Pw\) for polynomial column vectors. Multiplication by
\(\operatorname{adj}P\) gives
\[
g\operatorname{adj}P\,v=81F^3w.
\]
The irreducible polynomial \(F\) does not divide \(g\). Unique
factorization implies that every entry of \(\operatorname{adj}P\,v\)
is divisible by \(F^3\). Therefore
\(u=\operatorname{adj}P\,v/(81F^3)\) is a polynomial vector and
\(Pu=v\). The class of \(v\) in the cokernel is zero, which proves
torsion-freeness.

Its rank over \(C\) is three. Here is an elementary local calculation
of that rank. Localize \(S\) at the prime \((F)\), a discrete valuation
ring with uniformizer \(F\). Successive row and column operations clear
an entry of minimum valuation and then its row and column, giving the
diagonal elementary-divisor form of \(P\). The identity \(PK=3FI\)
implies that each diagonal exponent is at most one, and \(\det P=81F^3\)
implies that their sum is three. Thus exactly three diagonal entries
have exponent one. Reducing modulo \(F\) gives rank two for \(P\),
and dimension three for its cokernel over \(\operatorname{Frac}C\).
For an additional finite check, all 100 three-by-three minors of \(P\)
are divisible by \(F\), and its upper left two-by-two minor is
\(-3AB(AD-BC)\), which is not divisible by \(F\).

Embed \(C\) into \(\mathbf Q[z_1,z_2,z_3,z_4]\) by (Q.6), and pass
to the latter fraction field \(L\). Section evaluation embeds \(M\)
degreewise in the generic quotient \(L^4/Lz\), which has dimension
three. The four constant generators in (Q.13) span this quotient.
Consequently \(\mathcal M\otimes_C L\to L^4/Lz\) is a surjection
between three-dimensional spaces and is an isomorphism. The kernel of
\(\mathcal M\to M\) is therefore \(C\)-torsion and, by the preceding
paragraph, is zero. This proves the actual injection
\[
\mathcal M\hookrightarrow M.
\tag{Q.14}
\]

## 4. The cohomological dimension proves surjectivity in every degree

The precise regularity result needed here is proved in A-029: for the
ideal (Q.6), every \(I^k\), \(k\ge2\), has a \(2k\)-linear free
resolution. A-029 verifies its height-three Gorenstein presentation,
every local generator condition, and the exceptional degree in the
known symmetric-power complexes. Its cited inputs are Kustin–Polini–Ulrich,
*The equations defining blowup algebras of height three Gorenstein
ideals*, Algebra & Number Theory 11 (2017), formula (6.1.4), p. 1509,
Lemma 6.3 and Corollary 6.4, p. 1510, with the proof on p. 1511. The
ordinary-power resolution follows there by the actual torsion sequence,
whose kernel is the degree-zero module
\(\operatorname{sgn}\otimes\operatorname{Sym}^{k-3}U\).

In particular the saturation agrees with the ordinary power in degree
\(2k\), and \(H^1(\mathcal I^k(2k-1))=0\) for \(k\ge2\). Thus
\[
\begin{aligned}
h^0(\mathcal I^k(2k))
 &=\dim C_k=\binom{k+4}{4}-\binom{k+1}{4},\\
h^0(\mathcal I^k(2k-1))
 &=\binom{2k+2}{3}-5\binom{k+2}{3}
 =\frac{k(k+1)(k-2)}2 \quad(k\ge2).
\end{aligned}
\tag{Q.15}
\]
The second equality uses the length of five order-\(k\) fat points,
which is \(5\binom{k+2}{3}\). Tensoring the tautological sequence
with \(\mathcal I^k(2k)\) and taking global sections now gives
\[
\dim M_k=4\dim C_k-\frac{k(k+1)(k-2)}2
=\frac{(k+1)(k+2)(3k+4)}2\quad(k\ge2).
\tag{Q.16}
\]
At \(k=1\), the degree-one evaluation \(E\to\operatorname{Perm}_5\)
has a one-dimensional trivial cokernel, and
\(H^0(\mathcal I(1))=0\). The same cohomology sequence gives
\(\dim M_1=4\cdot5+1=21\). At \(k=0\), \(M_0=E\) has dimension four.
These values agree with (Q.16).

The injective free presentation (Q.13) has Hilbert series
\[
\operatorname{Hilb}_{\mathcal M}(t)
=\frac{4+t-5t^2}{(1-t)^5}
=\frac{4+5t}{(1-t)^4}
=\sum_{k\ge0}\frac{(k+1)(k+2)(3k+4)}2t^k.
\tag{Q.17}
\]
Equality of every graded dimension in (Q.14) proves
\(\mathcal M\simeq M\). This establishes generation and the entire
relation module; neither was inferred solely from a low-degree test.

## 5. Four invariant parameters and the actual free multiplication map

Use the six linear forms of T-038:
\[
\begin{array}{lll}
t_1=A+B-C+D-E,&t_2=-A+B+C-D-E,&t_3=-A+B+C-D+E,\\
t_4=-A-B-C+D+E,&t_5=A-B-C-D+E,&t_6=A-B+C+D-E.
\end{array}
\tag{Q.18}
\]
They satisfy \(\sum t_i=0\) and \(\sum t_i^3=-24F\), so their third
elementary symmetric polynomial is \(e_3=-8F\). The verified action
is sign times the permutation action on the six Sylow-five subgroups.
For a homogeneous elementary symmetric polynomial \(e_j\), the sign
twist consequently multiplies it by \(\operatorname{sgn}^j\). Hence
\[
B=\mathbf Q[e_2,e_4,e_6,e_5^2]
\tag{Q.19}
\]
consists of invariant elements, of degrees \(2,4,6,10\).

We record an algebraic freeness proof sufficient for the regularity
assertion about this module. For six independent variables, start with
the universal monic polynomial having coefficients \(e_1,\ldots,e_6\).
Adjoin its first ordered root, divide the polynomial by that root
factor, and successively adjoin a root of the remaining monic polynomial
of degrees five through one. At each step the quotient by a monic
polynomial is free over the preceding coefficient ring, with the powers
below that degree as a basis. The resulting ring is
\(\mathbf Q[t_1,\ldots,t_6]\): its defining equations identify the
coefficients with the elementary symmetric polynomials and allow those
coefficients to be eliminated. This proves freeness of rank \(6!\)
over \(\mathbf Q[e_1,\ldots,e_6]\), including algebraic independence.

Quotient by \(e_1\). The linear forms in (Q.18) have rank five, so
\(S\simeq\mathbf Q[t_1,\ldots,t_6]/(e_1)\). Replace the polynomial
variable \(e_5\) by \(e_5^2\), retaining the free basis \(1,e_5\).
Finally substitute \(e_3=-8F\). It follows that \(S\) is free of
rank 1440 over the polynomial ring \(B[F]\). In particular, after
quotienting by any initial segment of the four parameters in (Q.19),
both the next parameter and \(F\) are nonzerodivisors in the resulting
free coefficient module.

The four parameters are a regular sequence on \(M\). To prove this
directly, work modulo any preceding parameters and denote the next by
\(p\). The matrix \(P\) remains injective even after quotient by \(p\),
because its determinant is \(81F^3\), a nonzerodivisor there; multiplying
by its adjugate proves injectivity. In a relation \(pv=Pw\), reduce
modulo \(p\) to conclude \(w=pw'\). Since \(p\) is a nonzerodivisor
on the ambient free modules, it follows that \(v=Pw'\). This proves
that multiplication by \(p\) has zero kernel on the cokernel. The
argument applies in turn to all four parameters.

Set \(H=M/B_+M\). It is finite-dimensional: \(M\) is finite over
\(C=S/(F)\), which is finite over \(B\). The regular sequence gives
\[
\operatorname{Hilb}_H(t)
=(4+5t)\prod_{r\in\{2,4,6,10\}}(1+t+\cdots+t^{r-1}).
\tag{Q.20}
\]
It has degree 19 and total dimension 4320. Choose any graded linear
section \(H\to M\) and average it over \(S_5\). Multiplication defines
an equivariant map
\[
B\otimes H\longrightarrow M.
\tag{Q.21}
\]
It is surjective by induction on degree, because the section lifts the
quotient modulo \(B_+M\). The regular-sequence Hilbert identity makes
source and target dimensions equal in every degree. Thus (Q.21) is an
actual isomorphism. All four variables in \(B\) have trivial action.

## 6. The fixed positive tag table

Here is the complete table \(h_{\rho,j}=[H_j:[\rho]]\). Each row is
listed in increasing degree \(j=0,\ldots,19\):

| \(\rho\) | \((h_{\rho,0},\ldots,h_{\rho,19})\) | total |
|---|---|---:|
| \((5)\) | 0, 1, 1, 1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1, 1, 1, 0, 0 | 36 |
| \((4,1)\) | 1, 1, 2, 5, 6, 9, 11, 12, 14, 14, 14, 13, 12, 10, 8, 6, 3, 2, 1, 0 | 144 |
| \((3,2)\) | 0, 1, 3, 5, 8, 11, 13, 16, 17, 17, 18, 17, 15, 13, 10, 7, 5, 2, 1, 1 | 180 |
| \((3,1,1)\) | 0, 1, 3, 5, 9, 12, 16, 19, 20, 22, 21, 21, 19, 16, 13, 9, 6, 3, 1, 0 | 216 |
| \((2,2,1)\) | 0, 1, 2, 4, 7, 10, 13, 15, 17, 18, 18, 17, 16, 14, 11, 8, 5, 3, 1, 0 | 180 |
| \((2,1,1,1)\) | 0, 0, 1, 3, 5, 8, 10, 12, 14, 14, 15, 14, 13, 12, 9, 7, 4, 2, 1, 0 | 144 |
| \((1^5)\) | 0, 0, 0, 1, 1, 1, 3, 3, 3, 4, 3, 4, 4, 2, 3, 2, 1, 1, 0, 0 | 36 |

For reproducibility, the seven rational characters of \(M\) calculated
from (Q.13), in the indicated class order, are
\[
\begin{array}{c|c|r}
\text{cycle type}&\sum_k\operatorname{tr}(g\mid M_k)t^k&\text{class size}\\\hline
1^5&(4+5t)/(1-t)^4&1\\
2\,1^3&(2-t)/((1-t)^3(1+t))&10\\
2^2\,1&t/(1-t^2)^2&15\\
3\,1^2&1/(1-t^3)&20\\
3\,2&-1/(1-t^3)&20\\
4\,1&t/(1-t^4)&30\\
5&-(1-t)/(1-t^5)&24.
\end{array}
\tag{Q.22}
\]
Indeed the character before cancellation is
\[
\frac{\chi_E(g)+t-\chi_U(g)t^2}{\det(1-tg\mid U)},
\quad \chi_E(g)=m_1-1,\quad
\chi_U(g)=\binom{m_1}{2}+m_2-m_1,
\tag{Q.23}
\]
where \(m_i\) counts \(i\)-cycles. The latter character follows from
the permutation action on two-element subsets minus the five-point
permutation module, as identified in T-038. Newton's identities applied
to \(\chi_U(g^r)\), \(1\le r\le5\), give every denominator in
(Q.22). Multiplying by
\(D(t)=(1-t^2)(1-t^4)(1-t^6)(1-t^{10})\) gives the polynomial
character of the actual module \(H\), by (Q.21). Inner products with
the fixed seven irreducible characters give the displayed table.
The exact scripts `five_point_q_tags.py` and
`check_q_module_characters.py` perform this finite calculation by
independent expressions, and compare all 140 entries. No table entry
depends on \(k\) or \(d\).

At \(t=1\), the six nonidentity polynomial characters vanish and
the identity value is 4320. Thus, as an ungraded module, \(H\) has
character \(36\) times the regular character of \(S_5\). This checks
all row totals: \(\sum_jh_{\rho,j}=36\dim[\rho]\). Taking the
\([\nu]\)-summand of (Q.21) and using (Q.5) proves (Q.3).

## 7. Exact support and a fixed-arithmetic evaluator

All parameter weights in (Q.2) are even, and one is two. The first two
consecutive nonzero entries in each row of the table therefore determine
the complete support:
\[
\begin{array}{c|c}
\nu& p_{\mu,(n)}^\lambda>0\\\hline
(4,1)&k\ge0\\
(5),(3,2),(3,1,1),(2,2,1)&k\ge1\\
(2,1,1,1)&k\ge2\\
(1^5)&k\ge3.
\end{array}
\tag{Q.24}
\]
Before the indicated first degree every tag vanishes. At and above it,
choose a tag of the correct parity among those first two degrees and
use the weight-two variable to fill the remainder. This proves both
directions. In particular, for symmetric outer degree five, positivity
holds exactly for odd \(d\) with \(k\ge1\), or even \(d\) with
\(k\ge3\).

For completeness the count in (Q.2) needs no loop of length depending
on the input. It is zero for odd \(R\). For \(R=2N\ge0\), its weights
are \(1,2,3,5\). Write each variable uniquely as
\[
x_w=(30/w)q_w+r_w,\qquad0\le r_w<30/w.
\]
Define the fixed positive polynomial
\[
G(t)=\prod_{w\in\{1,2,3,5\}}
\left(\sum_{r=0}^{30/w-1}t^{wr}\right)
=\sum_{j=0}^{109}g_jt^j.
\tag{Q.25}
\]
Its coefficients count exactly the residue tuples. For a tuple of
residue weight \(j\), the four nonnegative \(q_w\) sum to
\((N-j)/30\), so stars and bars gives the positive identity
\[
N(2N)=
\sum_{\substack{0\le j\le\min(N,109)\\j\equiv N\pmod{30}}}
g_j\binom{(N-j)/30+3}{3}.
\tag{Q.26}
\]
There are at most four terms. The notation on the left is the counting
function of (Q.2); the integer \(N\) on the right is half its argument.
The factor degrees in (Q.25) are \(29,28,27,25\), whose sum is 109.
Thus (Q.3) uses a fixed table, at most 80 cubic-binomial evaluations,
and integer inputs of bit length \(O(\log(k+2)+\log(d+2))\). Ordinary
integer arithmetic gives a polynomial bit-cost bound; with schoolbook
multiplication the count itself costs \(O(\log^2(k+2))\).

## 8. Algebraic-geometric and lambda-ring dictionary

The object counted by (Q.3) is the \([\mu]\)-covariant summand of the
section space of the explicit ideal-twisted flag line bundle in G-015.
The morphism (Q.5) carries that section space to the balanced weight of
the Schur functor, and the normalizer projector T-003 carries it to the
plethysm coefficient. In the representation category its class is
\([S_\mu(\operatorname{Sym}^n)]\), with composition interpreted in
the lambda-ring of polynomial representations. The equality is lifted
here to actual modules and maps by (Q.5), (Q.13), and (Q.21).

The geometric construction is defined over \(\mathbf Q\); the frame,
quadrics, cubic, and polynomial matrices are defined over
\(\mathbf Z[1/30]\) after the stated invariant-form identifications.
The averaging section additionally uses \(1/120\), already in that
ring. The characteristic-zero cohomology and representation conclusions
have been proved over \(\mathbf Q\) and by extension over
characteristic-zero fields; no assertion of all-fiber exactness in
positive characteristic is inferred from the rational proof. The exact
base-extension morphism is tensoring the displayed complexes and maps.

The ideal powers are those of a specified closed subscheme of projective
space, and all bundles are Schur functors of tautological locally free
sheaves. The determinant pairings and exact-sequence classes are the
operations in the SGA 6 dictionary, and the concrete ideal and its
graded quotients define the associated Hilbert functors in the FGA
dictionary. The exact archive/SGA/FGA locators and coefficient-category
maps are recorded in the separate geometric dictionary; this result
uses those same maps, with the additional explicit matrices (Q.9).
No new weight, purity, or motivic comparison is required by this proof.


# The exterior quotient bundle on the five-point ray

## G-018. An exact kernel and positive formula

For \(k,d\ge0\), put
\[
n=d+k+1,\qquad
\lambda=(d+3k+3,d+2k+1,d+1,d,d).
\tag{W.1}
\]
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
is a count in at most 240 fixed bounded rational polytopes, with at most
five integer variables. The fixed table and every inequality are given
below. Its support is particularly simple: after setting
\(\nu=\mu\) for odd \(d\) and \(\nu=\mu'\) for even \(d\), it is
positive exactly in the following ranges:
\[
\begin{array}{c|c}
\nu&\text{range}\\\hline
(3,1,1)&k\ge0\\
(4,1),(3,2),(2,2,1),(2,1,1,1)&k\ge1\\
(5),(1^5)&k\ge3.
\end{array}
\tag{W.2}
\]
In particular the symmetric outer coefficient is positive exactly when
\(k\ge3\), independently of \(d\).

## 1. The flag morphism and the multiplication kernel

Use \(E=\mathfrak h_5\), its invariant form, the five-point ideal
\(\mathcal I\), and the tautological quotient bundle \(Q\) from
G-015 and T-038. Define
\[
W_k=H^0(\mathbf P(E),\mathcal I^k(2k)\otimes\Lambda^2Q).
\tag{W.3}
\]
For (W.1), the point order is \(\lambda_2-n=k\), the first-line
twist after relative duality is \(\lambda_2-\lambda_3=2k\), and the
quotient Schur weight is
\((\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(1,1)\).
Explicitly, after the determinant factor \((\det E^*)^d\) the relative
flag weight is \((1,0,0)\), with first-line twist \(2k+1\).
The exterior pairing
\(Q^*\simeq\Lambda^2Q\otimes\det Q^*\) and
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\) therefore give
\[
(S_\lambda\mathbf Q^5)_{(n^5)}\simeq\operatorname{sgn}^{d+1}\otimes W_k.
\tag{W.4}
\]
These relative Schur evaluations and the inverse balanced chart
\(f\mapsto u^{-k}f(v(X))\) are the actual maps in G-015 and T-039 §1.

Set \(C_{j,k}=H^0(\mathcal I^k(2k+j))\), for \(j=1,2\).
A-029 proves \(C_{j,k}=(I^k)_{2k+j}\) for \(k\ge2\); saturation of
\(I\) proves the same for \(k=1\), and \(k=0\) is immediate.
The ideal \(I^k\) is generated in degree \(2k\). Hence multiplication
by linear forms gives a surjection
\[
E^*\otimes C_{1,k}\longrightarrow C_{2,k}.
\tag{W.5}
\]
In coordinates it sends \(\sum e_i^*\otimes f_i\) to \(\sum z_if_i\).
The dual tautological sequence, tensored by \(\mathcal I^k(2k+1)\),
identifies its kernel with
\(H^0(\mathcal I^k(2k+1)\otimes Q^*)\). The exterior isomorphism
\(\Lambda^2Q\simeq Q^*\otimes\det Q\), where
\(\det Q=\operatorname{sgn}\otimes\mathcal O(1)\), consequently gives
the actual exact sequence
\[
\boxed{0\longrightarrow\operatorname{sgn}\otimes W_k
\longrightarrow E^*\otimes C_{1,k}
\longrightarrow C_{2,k}\longrightarrow0.}
\tag{W.6}
\]
The first map is the dual tautological inclusion followed by the specified
exterior pairing. Thus the character difference used next is the trace
of a concrete kernel of a surjective map.

## 2. Exact traces from the five fat-point jets

For a permutation \(g\in S_5\), let \(m_1(g)\) be its number of fixed
letters and let \(s_r(g)=\operatorname{tr}(g\mid\operatorname{Sym}^rE)\),
with \(s_r=0\) for \(r<0\). These traces are completely specified by
\[
\sum_{r\ge0}s_r(g)z^r
=\frac{1-z}{\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)}.
\tag{W.7}
\]
A-029 gives \(H^1(\mathcal I^k(2k+j))=0\) for \(j\ge0\), including
the separately verified \(k=0,1\). Therefore the evaluation sequence
for the fat points is exact on global sections in the degrees used here.

We specify the jet action, including its trivializations. The stabilizer
of \([\ell_i]\) fixes the affine vector \(\ell_i\) and decomposes
\(E=\mathbf Q\ell_i\oplus\mathfrak h_4\). The linear functional
equal to one on \(\ell_i\) and zero on \(\mathfrak h_4\) is invariant
under that stabilizer. Its affine chart trivializes every \(\mathcal O(c)\)
with trivial fiber character, and its normal coordinates transform by
\(\mathfrak h_4^*\). Thus the order-\(k\) jet module at that point is
\(\bigoplus_{r=0}^{k-1}\operatorname{Sym}^r\mathfrak h_4^*\).
Transport by the canonical affine representatives gives the induced
\(S_5\)-module of these jets. Only fixed points contribute to the trace
of \(g\); each contributes the same value. For a fixed point the
restriction \(E=\mathbf1\oplus\mathfrak h_4\) identifies the sum of
the first \(k\) symmetric powers with the trace of
\(\operatorname{Sym}^{k-1}E\). Hence the full jet trace is
\[
\operatorname{tr}(g\mid J_k)=m_1(g)s_{k-1}(g).
\tag{W.8}
\]
This proves, through the actual evaluation sequence,
\[
\operatorname{tr}(g\mid C_{j,k})=s_{2k+j}(g)-m_1(g)s_{k-1}(g).
\tag{W.9}
\]
Combining (W.6) and (W.9) gives
\[
w_k(g)=\operatorname{sgn}(g)\left[
(m_1-1)\{s_{2k+1}-m_1s_{k-1}\}
-\{s_{2k+2}-m_1s_{k-1}\}\right].
\tag{W.10}
\]
Every scalar on the right is specified by the finite rational function
(W.7). At the identity this gives
\[
\dim W_k=\frac{(k+2)(k+3)(3k+2)}2,
\qquad
\sum_{k\ge0}\dim W_k t^k
=\frac{6+6t-4t^2+t^3}{(1-t)^4}.
\tag{W.11}
\]
The initial value \(W_0=\Lambda^2E\) has label \((3,1,1)\), as required.

## 3. Fixed positive Newton data and its complete finite certificate

Let
\[
b_\nu(k)=\frac1{120}\sum_{g\in S_5}\chi_\nu(g)w_k(g).
\tag{W.12}
\]
This is the multiplicity of \([\nu]\) in the actual module \(W_k\).
The sum can equivalently be taken over the seven cycle types with sizes
\(1,10,15,20,20,30,24\), in the order of (Q.22).

For \(0\le r<60\) and \(0\le j\le3\), define the fixed integer
\[
c_{\nu,r,j}
=\sum_{h=0}^j(-1)^{j-h}\binom jh b_\nu(r+60h).
\tag{W.13}
\]
These 1680 integers are specified by (W.7), (W.10), (W.12), and (W.13),
using only symmetric groups of order at most 120 and indices at most
239. `FIVE_POINT_WEDGE2_NEWTON_TABLE.json` lists every one.

Here is the exact verification that extends this fixed data to every
input. Taking even and odd parts of (W.7) gives the rational series
\(\sum_ks_{2k}t^k\) and \(\sum_ks_{2k+1}t^k\). Subtracting its
constant term and dividing by \(t\) gives the series for \(s_{2k+2}\).
For each of the seven explicitly listed cycle types, substitution into
(W.10) shows that its denominator divides \((1-t^{60})^4\) and its
numerator has degree at most 239. These seven exact polynomial
divisibilities are checked in `five_point_wedge2_certificate.py`, with
their reduced rational functions retained in the JSON certificate.
The script also computes (W.7) directly by the seven cycle recurrences,
independently of the even/odd rational extraction.

A numerator degree at most 239 implies that, on a fixed residue \(r\),
the coefficient is a polynomial of degree at most three in
\(q=(k-r)/60\), for every \(q\ge0\). To check the initial endpoints,
each numerator exponent is \(r+60h\), \(0\le h\le3\), and its
contribution is \(\binom{q-h+3}{3}\). The polynomial expression is
zero also for \(0\le q<h\le3\), since its upper integer is then zero,
one, or two. Thus no delayed-onset term is lost. Newton interpolation
at \(q=0,1,2,3\) proves the identity
\[
\boxed{b_\nu(60q+r)=\sum_{j=0}^3 c_{\nu,r,j}\binom qj\quad(q\ge0).}
\tag{W.14}
\]

All 1680 integers (W.13) were computed exactly and are nonnegative;
the following minima over all 60 residues make their signs reviewable.

| \(\nu\) | min \(c_0\) | min \(c_1\) | min \(c_2\) | min \(c_3\) |
|---|---:|---:|---:|---:|
| \((5)\) | 0 | 2877 | 16560 | 16200 |
| \((4,1)\) | 0 | 11693 | 66540 | 64800 |
| \((3,2)\) | 0 | 14725 | 83400 | 81000 |
| \((3,1,1)\) | 1 | 17787 | 100260 | 97200 |
| \((2,2,1)\) | 0 | 14880 | 83700 | 81000 |
| \((2,1,1,1)\) | 0 | 12003 | 67140 | 64800 |
| \((1^5)\) | 0 | 3032 | 16860 | 16200 |

The accompanying TSV has one row for each label and residue, with all
four entries. Its generating code contains the full exact finite check,
not a random or asymptotic test. Direct evaluation of (W.12) through
\(k=359\) also agrees with (W.14) in every case. This extra finite
check is recorded separately from the rational identity that proves
the formula in all degrees.

For each tag \((r,j)\) with \(c=c_{\nu,r,j}>0\), use integer variables
\(q,y,t_1,\ldots,t_j\) and inequalities
\[
60q+r=k,\quad q\ge0,\quad0\le y<c,\quad
1\le t_1<t_2<\cdots<t_j\le q.
\tag{W.15}
\]
For \(j=0\), the last list is empty. Replace strict integer inequalities
by \(y\le c-1\) and \(t_i+1\le t_{i+1}\) to obtain the rational
polytope. Its lattice count is exactly \(c\binom qj\), by the bijection
with a choice of \(y\) and a \(j\)-element subset of \(\{1,\ldots,q\}\).
Every variable is bounded. Summing these 240 tagged sets proves the
positive formula for (W.1) using the sign twist (W.4).

The fixed zeroth entries in residues zero through 59 have zeros exactly
at the excluded degrees in (W.2). For \(k\ge60\), the positive
first differences in the table and \(q\ge1\) prove positivity.
This proves the complete support statement, including all endpoints.

## Geometric transport

This result is the global-section representation of the ideal-twisted
exterior quotient bundle (W.3). The flag chart (W.4), dual tautological
inclusion (W.6), and affine jet trivializations (W.8) specify every
comparison. Associated bundles along the frame torsor carry the Schur
operations to the SGA 6 representation-group dictionary; the point
scheme, ideal powers, and their evaluation maps give the EGA/FGA
objects. The exact framework locators are listed in the separate
geometric dictionary. All representation assertions here are over
characteristic-zero fields.


# Every symmetric quotient power on the five-point quadratic ray

## G-019. A three-parameter positive plethysm family

Let \(a,k,d\ge0\). Define
\[
n=d+a+k,\qquad
\lambda=(d+2a+3k,d+a+2k,d+a,d+a,d).
\tag{SQ.1}
\]
Zero parts are removed; at \(a=k=d=0\) the partition is empty.
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
has a positive formula in a fixed family of at most 57,600 bounded
rational polytopes of dimension at most nine. At most sixteen tags
contribute after the two residues \(a\bmod60\) and \(k\bmod60\)
are selected. The evaluator requires a fixed number of integer
arithmetic operations on the input parameters. All constants are
explicitly defined in (SQ.10)–(SQ.12) and supplied in a complete exact
table; no input-dependent character or plethysm computation is required.

This evaluates all symmetric quotient powers together with all point
orders in the geometric model, and includes T-039 at \(k=1\), G-017
at \(a=1\), and the full scalar ray at \(a=0\). The underlying
module comparison is proved for every parameter, before the finite
positive coefficient conversion.

## 1. The actual sheaf module and all cohomological endpoints

Use the five-point scheme \(Z\subset\mathbf P(E)\), with
\(E=\mathfrak h_5\), ideal \(\mathcal I\), and quotient bundle \(Q\).
Put
\[
M_{a,k}=H^0\bigl(\mathbf P(E),\mathcal I^k(2k)
                                      \otimes\operatorname{Sym}^aQ\bigr),
\qquad C_k=H^0(\mathcal I^k(2k)).
\tag{SQ.2}
\]
For (SQ.1), the flag model has point order \(k\), first-line gap
\(2k\), and relative weight \((a,a,0)\). The exterior pairing used
in (5F.7) identifies
\(S_{(a,a)}Q^*\simeq(\det Q^*)^a\otimes\operatorname{Sym}^aQ\).
The full determinant and relative determinants therefore give the
actual equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,k}.}
\tag{SQ.3}
\]
Its relative frame maps and inverse chart are the maps in G-015 and
T-039 §1, with \(u^{-k}\) replacing \(u^{-1}\). In particular the
point-power condition has already been proved to be exactly the
polynomial extension condition; (SQ.3) retains its full linearization.

For \(a\ge1\), the symmetric quotient sequence is the actual exact
sequence of sheaves
\[
0\to\mathcal I^k(2k-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal I^k(2k)\otimes\operatorname{Sym}^aE
\longrightarrow\mathcal I^k(2k)\otimes\operatorname{Sym}^aQ\to0.
\tag{SQ.4}
\]
Its first map multiplies by the tautological vector, and its last map
is the symmetric power of the quotient. Before tensoring the ideal,
it is an exact locally split sequence of vector bundles: on a line
\(L\subset E\), the kernel in the symmetric algebra is
\(L\operatorname{Sym}^{a-1}E\), and multiplication by the nonzero line
vector is injective. Tensoring by \(\mathcal I^k(2k)\) preserves this
locally split exactness.

Let \(A_k=H^0(\mathcal I^k(2k-1))\). A-029 proves
\(H^1(\mathcal I^k(2k-1))=0\) for \(k\ge2\), using the verified
Kustin–Polini–Ulrich complexes, formula (6.1.4), p. 1509, Lemma 6.3
and Corollary 6.4, p. 1510. The complete applied proof checks the ideal's
local hypotheses and the passage to ordinary powers. At \(k=0\),
\(\mathcal O(-1)\) is acyclic. At \(k=1\),
\(A_1=0\), \(H^1(\mathcal I(1))=\mathbf1\), and
\(H^1(\mathcal I(2))=0\), by the actual five-point evaluation maps.
Consequently the long cohomology sequence of (SQ.4) is short exact for
\(k\ne1\); at \(k=1\) its sole additional term is
\(\operatorname{Sym}^{a-1}E\), exactly as in T-039 (5F.15).

The case \(a=1\) is the module \(M_k\) proved in G-017. Its own
tautological sequence gives the equality in the exact representation
group
\[
[M_k]=[E][C_k]-[A_k]+\mathbf1_{k=1}[\mathbf1].
\tag{SQ.5}
\]
Combining the actual sequences just described, including their identical
\(k=1\) connecting terms, proves for every \(a,k\ge0\)
\[
\boxed{[M_{a,k}]
=[\operatorname{Sym}^aE][C_k]
+[\operatorname{Sym}^{a-1}E]\bigl([M_k]-[E][C_k]\bigr).}
\tag{SQ.6}
\]
Here \(\operatorname{Sym}^{-1}E=0\); this convention proves the formula
also at \(a=0\). At \(k=0\) it reduces to \(M_{a,0}=\operatorname{Sym}^aE\).
Thus no unverified vanishing for varying Schur bundles is used.

## 2. A completely specified bivariate character series

Write \(e_g=\chi_E(g)\), \(u_g=\chi_{[3,2]}(g)\), and
\(\epsilon_g=\operatorname{sgn}(g)\). T-038 and A-029 identify
\(\bigoplus C_k\) with the cubic algebra
\(\operatorname{Sym}(U)/(F)\), whose relation has sign character.
G-017 supplies its quotient-bundle module with the proved presentation.
Their exact trace series are
\[
C_g(t)=\frac{1-\epsilon_gt^3}{\det(1-tg\mid U)},\qquad
M_g(t)=\frac{e_g+t-u_gt^2}{\det(1-tg\mid U)}.
\tag{SQ.7}
\]
Taking the traces of (SQ.6) gives the exact rational identity
\[
\boxed{\sum_{a,k\ge0}\chi_{M_{a,k}}(g)s^at^k
=\frac{1+st-u_gst^2-\epsilon_gt^3+
               \epsilon_ge_gst^3}
 {\det(1-sg\mid E)\det(1-tg\mid U)}.}
\tag{SQ.8}
\]
The numerator follows directly by summing
\(C_g\operatorname{Sym}^aE+(M_g-e_gC_g)\operatorname{Sym}^{a-1}E\).

For a complete finite specification, use the following seven-column
data. Columns correspond to the ordinary cycle types in the first row.

| datum | \(1^5\) | \(2\,1^3\) | \(2^2\,1\) | \(3\,1^2\) | \(3\,2\) | \(4\,1\) | \(5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| class size | 1 | 10 | 15 | 20 | 20 | 30 | 24 |
| \(\chi_{(5)}\) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| \(\chi_{(4,1)}\) | 4 | 2 | 0 | 1 | -1 | 0 | -1 |
| \(\chi_{(3,2)}\) | 5 | 1 | 1 | -1 | 1 | -1 | 0 |
| \(\chi_{(3,1,1)}\) | 6 | 0 | -2 | 0 | 0 | 0 | 1 |
| \(\chi_{(2,2,1)}\) | 5 | -1 | 1 | -1 | -1 | 1 | 0 |
| \(\chi_{(2,1,1,1)}\) | 4 | -2 | 0 | 1 | 1 | 0 | -1 |
| \(\chi_{(1^5)}\) | 1 | -1 | 1 | 1 | -1 | -1 | 1 |

The character table is the fixed table already verified in T-038 and
T-039. It can be checked by the ordinary permutation actions for
\(E,U\), their exterior powers and sign twists, followed by the
class-size inner products. In particular every entry in (SQ.8) is fixed.
The two determinants can be written without eigenvalue choices:
\[
\det(1-sg\mid E)=
\frac{\prod_{\ell\in\operatorname{cyc}(g)}(1-s^\ell)}{1-s},
\quad
\det(1-tg\mid U)=
\frac{\prod_{\ell\in\operatorname{cyc}_6(g)}
                      (1-\epsilon_g^\ell t^\ell)}{1-\epsilon_gt}.
\tag{SQ.9}
\]
Here the exact six-letter cycle list, by T-038's intertwiner, is
\(1^6,2^3,2^21^2,3^2,6,41^2,51\), in the same column order.

## 3. Fixed integer constants and the proof of their positivity

Define the fixed-degree coefficient function
\[
b_\nu(a,k)=\frac1{120}\sum_{\text{seven classes }g}
|g^{S_5}|\,\chi_\nu(g)\,[s^at^k]\text{(SQ.8)}.
\tag{SQ.10}
\]
For \(0\le r,v<60\) and \(0\le i,j\le3\), set
\[
\boxed{c_{\nu,r,v,i,j}=
\sum_{h=0}^i\sum_{l=0}^j
(-1)^{i+j-h-l}\binom ih\binom jl\,
b_\nu(r+60h,v+60l).}
\tag{SQ.11}
\]
Equations (SQ.8)–(SQ.11), together with the displayed character table,
are explicit definitions of 403,200 fixed integers. Only coefficients
with indices below 240 occur. The complete table is stored as
`FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json`, in the order
`labels[nu][r][v][4*i+j]`. It is a single fixed table, independent of
every input parameter in (SQ.1).

The following exact finite certificate proves all their signs. For
each of the seven classes, compute coefficients of
\((1-s)/\prod(1-s^\ell)\) by multiplying the cycle geometric series.
Similarly multiply the six signed geometric series in (SQ.9), then
multiply by \(1-\epsilon_gt\), to obtain the coefficients \(u_k\)
of \(\det(1-tg\mid U)^{-1}\). The two required \(t\)-coefficient
arrays are exactly
\[
C_k=u_k-\epsilon_gu_{k-3},\qquad
X_k=u_{k-1}-u_gu_{k-2}+\epsilon_ge_gu_{k-3},
\tag{SQ.12}
\]
with negative indices zero. The class coefficient in (SQ.10) is
\(s_aC_k+s_{a-1}X_k\). Multiplication by the displayed integer class
sizes and characters, summation and division by 120 give (SQ.10)
exactly; every division in the executed certificate had zero remainder.
Successive forward differences of the four-by-four blocks then give
(SQ.11). `five_point_symmetric_quotient_certificate.py` contains this
entire algorithm, with all iteration limits fixed at 240, 60, four,
and seven. All 403,200 resulting integers were checked exactly.

The \((i,j)=(3,3)\) coefficient is zero in every case. Every other
coefficient with \(i+j>0\) is strictly positive. The following table
records the minimum over all 3600 residue pairs and all fourteen such
index pairs. The zeroth coefficients are nonnegative, both by this
calculation and because (SQ.10) is the multiplicity of the actual module.

| \(\nu\) | minimum of the fourteen positive difference coefficients | number of zero zeroth entries |
|---|---:|---:|
| \((5)\) | 418 | 2 |
| \((4,1)\) | 1487 | 2 |
| \((3,2)\) | 1735 | 2 |
| \((3,1,1)\) | 1978 | 5 |
| \((2,2,1)\) | 1575 | 5 |
| \((2,1,1,1)\) | 1167 | 9 |
| \((1^5)\) | 258 | 19 |

The summary certificate retains the separate minima and maxima of all
sixteen difference positions, for each label. These are exhaustive
finite integer checks with the complete reproducible recurrences
(SQ.9)–(SQ.12), rather than evidence inferred from sampled parameters.

## 4. The rational identity that extends the formula to all parameters

We verify the range of the Newton interpolation exactly. For each class,
the four one-variable factors
\[
\frac1{\det(1-sg\mid E)},\quad
\frac{s}{\det(1-sg\mid E)},\quad
C_g(t),\quad M_g(t)-e_gC_g(t)
\tag{SQ.13}
\]
have denominator dividing \((1-s^{60})^4\) or \((1-t^{60})^4\),
respectively, and common numerator of degree at most 239. Substitution
of the seven cycle lists in (SQ.9), cancellation and polynomial division
verify these 28 identities. All numerator remainders are zero in the
exact certificate, and each numerator degree is checked explicitly.

The argument of G-018 §3 now applies in each variable. On a fixed
residue, a numerator term indexed by \(h\le3\) contributes
\(\binom{q-h+3}{3}\); it equals zero in all early cases \(0\le q<h\).
Thus the full residue sequence is a polynomial from its first value,
with degree at most three. The two products in (SQ.8) consequently give
a polynomial of degree at most three in each quotient parameter.
Its unique Newton expansion, fixed by its four-by-four grid of values,
is therefore
\[
\boxed{b_\nu(60p+r,60q+v)
=\sum_{i=0}^3\sum_{j=0}^3
c_{\nu,r,v,i,j}\binom pi\binom qj
\quad(p,q\ge0).}
\tag{SQ.14}
\]
This proves the identity for every input. The finite sign check in §3
and this rational identity perform distinct, specified jobs.

At the identity the dimension formula offers a useful independent
algebra check:
\[
\dim M_{a,k}
=\binom{a+2}{2}\frac{(k+1)(k^2+2k+2)}2
+\binom{a+2}{3}(k+1)(2k+1).
\tag{SQ.15}
\]
It follows by expanding (SQ.6) using (Q.16) and (Q.15), with the
\(k=1\) correction retained. Its bidegree is at most \((3,3)\),
and its coefficient of \(a^3k^3\) is zero, consistent with the
vanishing mixed third difference. The full character identity, rather
than only this dimension check, proves (SQ.14).

## 5. Positive polytopes, evaluation cost, and complete support

For the input (SQ.1), set \(\nu=\mu\) when \(d+a\) is even and
\(\nu=\mu'\) when \(d+a\) is odd. For each fixed tag
\((r,v,i,j)\) whose table entry is \(c>0\), use integer variables
\(p,q,y,x_1,\ldots,x_i,z_1,\ldots,z_j\) satisfying
\[
\begin{aligned}
60p+r&=a,&60q+v&=k,&p,q&\ge0,&0\le y&\le c-1,\\
1\le x_1&<\cdots<x_i\le p,
&&1\le z_1<\cdots<z_j\le q.
\end{aligned}
\tag{SQ.16}
\]
An empty list of ordered variables contributes one choice. Each strict
integer inequality is written equivalently with a difference at least
one. The equations fix \(p,q\); every other variable lies in a displayed
finite interval. This is a bounded rational polytope with at most nine
variables. Its lattice points are in bijection with a choice of \(y\),
an \(i\)-element subset of \(\{1,\ldots,p\}\), and a \(j\)-element
subset of \(\{1,\ldots,q\}\). Its count is exactly the corresponding
positive term in (SQ.14). The disjoint tagged union of (SQ.16), together
with (SQ.3), proves the announced plethysm formula.

There are at most \(60^2\cdot16=57,600\) fixed tags. Only one residue
pair admits integer \(p,q\), so direct evaluation selects that pair
and uses at most sixteen products of binomial polynomials of degree
at most three. The table lookup is fixed. Integer bit lengths are
\(O(\log(a+2)+\log(k+2)+\log(d+2))\), and schoolbook arithmetic
gives a polynomial bit-cost bound, with the counting arithmetic
quadratic in the combined input bit length.

There is a complete small exceptional set for vanishing. All coefficients
are positive for \(a\ge60\) or \(k\ge60\), by the strictly positive
\((1,0)\) and \((0,1)\) differences. Inside the 60-by-60 square, the
only zeros are the following 44 pairs \((a,k)\), with the effective
label \(\nu\) just specified:

| \(\nu\) | all zero pairs \((a,k)\) |
|---|---|
| \((5)\) | \((0,1),(1,0)\) |
| \((4,1)\) | \((0,0),(0,1)\) |
| \((3,2)\) | \((0,0),(1,0)\) |
| \((3,1,1)\) | \((0,0)\), \((0,1)\), \((0,2)\), \((1,0)\), \((2,0)\) |
| \((2,2,1)\) | \((0,0)\), \((0,1)\), \((1,0)\), \((2,0)\), \((3,0)\) |
| \((2,1,1,1)\) | \((0,0)\), \((0,1)\), \((0,2)\), \((1,0)\), \((1,1)\), \((2,0)\), \((3,0)\), \((4,0)\), \((5,0)\) |
| \((1^5)\) | \((0,k)\) for \(0\le k\le4\); \((1,k)\) for \(0\le k\le2\); \((2,k),(3,k)\) for \(0\le k\le1\); \((a,0)\) for \(4\le a\le9\) or \(a=11\) |

Every other pair is positive. This statement follows from the exhaustive
zeroth-entry check and the positive Newton terms; it includes both axes
and the empty partition. In particular it gives a complete nonvanishing
decision for every outer label in the three-parameter family (SQ.1).

## 6. Exact Grothendieck-framework transport

The sheaf in (SQ.2) is a symmetric Schur functor of the tautological
quotient, tensored with an ordinary ideal power of the specified reduced
point scheme. The balanced chart, relative exterior pairing and
determinant line in (SQ.3) identify its global-section representation
with the normalizer module of the Schur functor. Taking the constant
\(S_5\)-covariant summand is the exact projector T-003.

The equality (SQ.6) lives in exact representation \(K_0\), and is
proved by the displayed exact sheaf and cohomology sequences. Its
lambda-ring interpretation is composition of the Schur operations,
transported by the frame torsor as in SGA 3 I 4.5, 4.7.2–4.7.3 and
SGA 6 VI 3.3. The universal lambda-ring locators are SGA 6 V 4.2,
4.4, 4.8 and 4.9. The projective ideal and its multiplication maps
are the explicitly graded EGA I 9.5.1–9.5.3 construction, and the
corresponding flat-family Hilbert and Quot interpretation is FGA
Exposé 221, Theorems 3.1–3.2. These are the same verified exact
locators and associated-bundle maps in the separate dictionary.
The positive lattice formula follows by the proved finite rational
identities, without an additional unconstructed purity or period map.


# The five-point quotient bundle one degree above the quadratic ray

## T-040. Statement

Let \(k,d\ge0\), and put
\[
n=d+k+2,\qquad
\lambda=(d+3k+6,\ d+2k+2,\ d+1,\ d+1,\ d).
\tag{QP.1}
\]
These are partitions of \(5n\). For every outer partition \(\mu\vdash5\),
the plethysm coefficient \(p_{\mu,(n)}^\lambda\) has a positive count by
at most 240 fixed tagged rational polytopes, each using at most five
integer variables. Only four tags can contribute after the residue of
\(k\) modulo 60 is fixed. Equations (QP.19)–(QP.22) below give every
constant and inequality. The full fixed table is
`Q_PLUS_NEWTON_TABLE.json`; a standalone evaluator is
`q_plus_positive.py`.

For the symmetric outer power the exact support criterion is
\[
\boxed{
p_{(5),(n)}^\lambda>0\quad\Longleftrightarrow\quad
\begin{cases}
k\ge3,&d\text{ even},\\
k\ge1,&d\text{ odd}.
\end{cases}}
\tag{QP.2}
\]
We prove the actual module presentation first and derive the positive
count from its seven finite-group traces. No character calculation or
elimination is required when evaluating the final fixed-table formula.

## 1. The scalar Rees pieces and the precise geometric map

Retain T-038's five-point ideal
\[
I=(xz-xy,xw-xy,yz-xy,yw-xy,zw-xy)
\subset S=\mathbf Q[x,y,z,w],
\]
with its literal \(S_5\) action, and put
\(E=\mathfrak h_5\), \(U=I_2=[3,2]\), \(\epsilon=\operatorname{sgn}\).
Use \(Q\) for the tautological rank-three quotient bundle on
\(\mathbf P(E)\). Write
\[
\begin{gathered}
R=\operatorname{Sym}(U)=\mathbf Q[A,B,C,D,E_0],\quad T=(A,B,C,D,E_0)^t,\\
F=AD(E_0-B-C)-BC(E_0-A-D).
\end{gathered}
\tag{QP.3}
\]
Each variable of \(R\) has degree one, corresponding to polynomial
degree two in \(S\). The names \(E\) and \(E_0\) distinguish the
representation from the fifth scalar variable.

Define the graded spaces
\[
\mathcal A_k=H^0(\mathcal I_Z^k(2k)),\qquad
\mathcal C_k=H^0(\mathcal I_Z^k(2k+1)),\qquad
\mathcal N_k=H^0(\mathcal I_Z^k(2k+1)\otimes Q),
\tag{QP.4}
\]
and take their direct sums over \(k\ge0\). Multiplication by the five
quadrics makes them graded \(R\)-modules.

The primary-source application A-029 establishes the following exact
facts for this ideal:
\[
\mathcal A_k=(I^k)_{2k},\qquad
\mathcal C_k=(I^k)_{2k+1},\qquad
H^1(\mathcal I_Z^k(2k))=0.
\tag{QP.5}
\]
For \(k\ge2\), these follow from its proved \(2k\)-linear resolution
and saturation bound. For \(k=1\), the ideal is saturated and degree-two
evaluation is onto the five point values. For \(k=0\), these are the
ordinary projective-space statements. The source input is
Kustin–Polini–Ulrich, formula (6.1.4), printed p. 1509, Lemma 6.3 and
Corollary 6.4, p. 1510, with the corollary proof on p. 1511. A-029 checks
the actual alternating presentation and the local generator condition at
every prime, and proves the Tor and saturation deductions. These passages
and the complete applied proof were independently read for this result.

In the coordinates (QP.3), the exact Rees presentation from that same
application is
\[
\mathcal R(I)=S[T]/(T^t\varphi,F),
\tag{QP.6}
\]
where \(\varphi\) is (5R.14). The map sends each \(T_i\) to its
displayed quadratic generator times the Rees parameter. Its component
of \(S\)-degree zero is
\(\mathcal A=R/(F)\). Its component of \(S\)-degree one is
\(\mathcal C\). Thus the relationship of the ordinary powers, saturated
sections and the presentation is through specified maps, with the degree
ranges in (QP.5).

For (QP.1), the flag parameters of G-015 are
\[
\lambda_2-n=k,\qquad \lambda_2-\lambda_3=2k+1,
\qquad(\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(1,0).
\]
The same relative exterior-column calculation as (5F.6)–(5F.9), now
with \(a=1\), starts with first-line weight \(2k+2\). The determinant
pairing removes one copy of \(\mathcal O(1)\), leaving twist
\(2k+1\), and gives
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+1}\otimes\mathcal N_k.}
\tag{QP.7}
\]
Explicitly, the relative quotient-flag module is
\(S_{(1,1)}Q^*=\Lambda^2Q^*=Q\otimes\det Q^*\), and
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\).
The original full determinant contributes \(\epsilon^d\), so their
product is exactly \(\epsilon^{d+1}\). The inverse to the flag chart
is \(F_{\rm flag}\mapsto u^{-k}F_{\rm flag}(v(X))\), and G-015 proves
its polynomial extension precisely from the order-\(k\) five-point
ideal. This proves the transport without suppressing its linearization.

## 2. A four-by-five scalar-piece presentation

Write \(T^t\varphi=(x,y,z,w)\mathsf B(T)\). The actual matrix is
\[
\mathsf B=\begin{pmatrix}
0&0&D-E_0&E_0-C&C-D\\
E_0-B&A-E_0&0&0&B-A\\
0&D&0&-B&0\\
-C&0&A&0&0
\end{pmatrix}.
\tag{QP.8}
\]
It satisfies
\[
\mathsf B T=0,\qquad
(-1)^{i-1}\det\mathsf B_{\widehat i}=-FT_i\quad(1\le i\le5).
\tag{QP.9}
\]
Here \(\mathsf B_{\widehat i}\) deletes column \(i\). The maximal
minors are nonzero, so the fraction-field kernel has dimension one.
The five entries of \(T\) have gcd one; the UFD denominator argument of
T-038 proves that the entire polynomial kernel is \(RT\).

The matrix
\[
\mathsf Q=\begin{pmatrix}
AB&AD&-A(A+C-E_0)&-B(A+D-E_0)\\
AB&BC&-A(B+C-E_0)&-B(B+D-E_0)\\
BC&CD&-C(A+C-E_0)&-D(B+C-E_0)\\
AD&CD&-C(A+D-E_0)&-D(B+D-E_0)\\
AB&CD&-AC&-BD
\end{pmatrix}
\tag{QP.10}
\]
obeys \(\mathsf B\mathsf Q=F I_4\), as verified by direct multiplication.
Consequently every degree-one-in-\(S\) consequence of the relation
\(F\) is already in the linear-syzygy image. Equations (QP.5)–(QP.6)
therefore give an exact presentation and resolution
\[
\boxed{
0\longrightarrow\epsilon\otimes R(-2)
\mathrel{\mathop{\longrightarrow}^{T}}
(\epsilon\otimes U)\otimes R(-1)
\mathrel{\mathop{\longrightarrow}^{\mathsf B}}
E^*\otimes R\longrightarrow\mathcal C\longrightarrow0.}
\tag{QP.11}
\]
The action on the first syzygy space is the one inherited from T-038's
five linear syzygies. The final kernel character is also fixed by that
resolution: after its constant basis change \(P\), its last column is
\(f\), an equivariant map from the sign line. Replacing the five
quadratic coefficients \(f_i\) by the five variables \(T_i\) gives
the column \(T\) in (QP.11), with the same sign source. This explains
both actions directly. The invariant form identifies \(E^*\) with
\(E\) whenever character notation is used below.

## 3. The quotient-bundle exact sequence and a full resolution

Tensor the tautological sequence by \(\mathcal I_Z^k(2k+1)\).
It remains exact because its quotient \(Q\) is locally free. By (QP.5),
taking global sections gives the actual exact sequence
\[
0\longrightarrow\mathcal A_k
\mathrel{\mathop{\longrightarrow}^{\iota}}
E\otimes\mathcal C_k\longrightarrow\mathcal N_k\longrightarrow0,
\qquad
\iota(s)=\sum_{i=1}^4 e_i\otimes x_i s.
\tag{QP.12}
\]
The tensor \(\sum e_i\otimes x_i\) is the identity, independent of
the choice of dual bases. Summing over \(k\) gives an exact sequence of
graded equivariant \(R\)-modules.

There is also the following explicit resolution of the quotient:
\[
\boxed{\begin{gathered}
0\longrightarrow
\bigl(\epsilon E\otimes R(-2)\bigr)\oplus
\bigl(\epsilon\otimes R(-3)\bigr)
\longrightarrow
(\epsilon E\otimes U)\otimes R(-1)\\
\longrightarrow(\operatorname{End}E/\mathbf1)\otimes R
\longrightarrow\mathcal N\longrightarrow0.\end{gathered}}
\tag{QP.13}
\]
To specify the maps in the chosen bases, represent the middle free
module by \(4\times5\) matrices \(Y\). Its map is
\[
Y\longmapsto[Y\mathsf B^t]\in
\operatorname{Mat}_{4\times4}(R)/(R I_4),
\]
and a lift of the first map is
\[
(r,s)\longmapsto rT^t+s\mathsf Q^t,
\qquad r\in R^4, s\in R.
\tag{QP.14}
\]
The cokernel is exactly (QP.12): the constant identity generator has
been removed from \(E\otimes E^*\), while the remaining relations
are \(E\) tensored with (QP.11).

Here is a direct check of exactness at the two preceding terms. If
\(Y\mathsf B^t=hI_4\), reduce this identity modulo \(F\). The matrix
\(\mathsf B\) has rank exactly three over the fraction field of
\(R/(F)\): all its maximal minors vanish by (QP.9), whereas its minor
using rows \(2,3,4\) and columns \(1,2,3\) is
\(AD(E_0-B)\), not a multiple of the irreducible cubic \(F\).
A scalar matrix of rank four cannot factor through a matrix of rank
three. Therefore \(h=Fs\) for some \(s\in R\). Subtracting
\(s\mathsf Q^t\) leaves a matrix whose every row lies in \(\ker\mathsf B\),
which is \(RT\). Thus \(Y=rT^t+s\mathsf Q^t\), proving exactness.
If this last expression is zero, multiply by \(\mathsf B^t\): it
gives \(sF I_4=0\). Since \(R\) is a domain, \(s=0\), and then
\(rT^t=0\) implies \(r=0\). The first map is injective.

The submodule \(rT^t\) has character \(\epsilon E\), as in (QP.11).
The quotient of the kernel by that submodule is the line of coefficients
\(h/F\), so its generator has character \(\epsilon\) because \(F\)
does. A graded equivariant choice of the displayed quadratic lift is
obtained by averaging its translates over \(S_5\); the identity
\(\mathsf B\mathsf Q=FI_4\) is preserved. This identifies the
equivariant free modules in (QP.13), even though a particular unaveraged
matrix \(\mathsf Q\) need not itself be an equivariant choice of basis.

The dimension series immediately follows:
\[
\sum_{k\ge0}\dim\mathcal N_k t^k
=\frac{15-20t+4t^2+t^3}{(1-t)^5}
=\frac{15-5t-t^2}{(1-t)^4},
\]
\[
\boxed{\dim\mathcal N_k
=\frac{(k+1)(3k^2+22k+30)}2.}
\tag{QP.15}
\]
In particular the four invariant parameters of degrees \(2,4,6,10\)
used for G-017 are not a regular sequence on this module. Multiplying
(QP.15) by their four factors gives a polynomial with coefficient
\(-1\) in degree 20. A regular sequence would give the Hilbert series
of its actual finite quotient by the successive exact multiplication
sequences, and such a coefficient is impossible. This is a concrete
obstruction to that parameter route for this specific module.

## 4. Seven exact character series

For a group element \(g\), write
\(e_g=\chi_E(g)\), \(u_g=\chi_U(g)\), and
\(\epsilon_g=\epsilon(g)\). Taking the graded trace in the actual
resolution (QP.13) gives
\[
\sum_{k\ge0}\chi_{\mathcal N_k}(g)t^k
=\frac{e_g^2-1-\epsilon_g e_gu_g t
             +\epsilon_g e_g t^2+\epsilon_g t^3}
        {\det(1-tg\mid U)}.
\tag{QP.16}
\]
T-038's signed six-coordinate intertwiner gives every denominator.
After cancellation the seven series and class sizes are as follows.

| class | size | series in (QP.16) |
|---|---:|---|
| \(1^5\) | 1 | \((15-5t-t^2)/(1-t)^4\) |
| \(21^3\) | 10 | \((3-t-t^2)/((1-t)^3(1+t))\) |
| \(2^21\) | 15 | \(-(1+t+t^2)/(1-t^2)^2\) |
| \(31^2\) | 20 | \(t/(1-t^3)\) |
| \(32\) | 20 | \(-t/(1-t^3)\) |
| \(41\) | 30 | \(-(1-t+t^2)/(1-t^4)\) |
| \(5\) | 24 | \(-t^2(1-t)/(1-t^5)\) |

Every denominator divides \((1-t^{60})^4\). The numerator after
multiplication by this common denominator has degree at most 238;
this follows either from the displayed fractions, or from the proper
fraction in (QP.16). Hence the multiplicity of any fixed \([\nu]\)
in \(\mathcal N_{r+60q}\), for fixed \(0\le r<60\), is a polynomial
of degree at most three in \(q\), valid for every \(q\ge0\). Indeed,
grouping the common numerator by residues gives
\(h_r(s)/(1-s)^4\), where \(\deg h_r\le3\). Its coefficients are
linear combinations of \(\binom{q-j+3}{3}\), \(0\le j\le3\).
For \(q\ge0\), the values with \(q<j\) are zero even as polynomial
binomial values, so there is no initial exceptional range.

For completeness all fixed character rows used in taking the inner
product are listed here, in the same class order as the preceding table.

| \(\nu\) | character row |
|---|---|
| \((5)\) | \(1,1,1,1,1,1,1\) |
| \((4,1)\) | \(4,2,0,1,-1,0,-1\) |
| \((3,2)\) | \(5,1,1,-1,1,-1,0\) |
| \((3,1,1)\) | \(6,0,-2,0,0,0,1\) |
| \((2,2,1)\) | \(5,-1,1,-1,-1,1,0\) |
| \((2,1,1,1)\) | \(4,-2,0,1,1,0,-1\) |
| \((1^5)\) | \(1,-1,1,1,-1,-1,1\) |

This is the same finite primary character table used and checked in
T-038/T-039.

## 5. Explicit positive Newton constants

Let \(m_\nu(k)\) be the multiplicity of \([\nu]\) in
\(\mathcal N_k\). Write
\[
f=\dim[\nu],\quad a=\chi_\nu(21^3),\quad
b=\chi_\nu(2^21).
\]
For each \(r\in\{0,\ldots,59\}\), define four constants
\(c_{\nu,r,j}\), \(0\le j\le3\). The first is the following
entirely explicit fixed integer:
\[
\begin{aligned}
c_{\nu,r,0}=\frac1{120}\bigl(&fP(r)+10aT(r)+15bD(r)\\
&+20(\chi_\nu(31^2)-\chi_\nu(32))\mathbf1_{r\equiv1\ (3)}\\
&+30\chi_\nu(41)L(r)+24\chi_\nu(5)M(r)\bigr),
\end{aligned}
\tag{QP.17}
\]
where
\[
\begin{aligned}
P(r)&=(r+1)(3r^2+22r+30)/2,\\
T(2h)&=h^2+5h+3,&T(2h+1)&=(h+1)(h+5),\\
D(2h)&=-(2h+1),&D(2h+1)&=-(h+1),\\
(L(0),L(1),L(2),L(3))&=(-1,1,-1,0)\quad(\bmod4),\\
(M(0),\ldots,M(4))&=(0,0,-1,1,0)\quad(\bmod5).
\end{aligned}
\tag{QP.18}
\]
The other three constants have short closed forms:
\[
\boxed{\begin{aligned}
c_{\nu,r,1}
&=\frac{f(9r^2+590r+12352)+a(10r+350)
      -b\bigl(30\mathbf1_{r\text{ even}}+15\mathbf1_{r\text{ odd}}\bigr)}4,\\
c_{\nu,r,2}&=f(270r+16950)+150a,\\
c_{\nu,r,3}&=16200f.
\end{aligned}}
\tag{QP.19}
\]
They are the first, second and third forward differences of
\(m_\nu(r+60q)\) at \(q=0\). This follows by applying the difference
operator of step 60 to the coefficients of the seven fractions in
(QP.16). In particular \(P(k)=(3k^3+25k^2+52k+30)/2\),
\(T(k)=k^2/4+5k/2\) plus a parity constant, \(D(k)\) is linear on
each parity, and the last four traces are constant on each residue.
Taking these differences gives (QP.19) directly.

All four constants are nonnegative integers. Integrality follows from
their forward-difference interpretation in actual finite-group modules.
For \(j=0\), the constant is the actual multiplicity \(m_\nu(r)\),
and the 420 constants (QP.17) have also been evaluated in the fixed
table. For \(j\ge1\), positivity follows without a table search from
\(|a|,|b|\le f\). In the first row of (QP.19), the numerator is at
least \(f(9r^2+580r+11972)>0\). In the second it is at least
\(f(270r+16800)>0\), and the third is positive.

Newton's polynomial identity now gives the positive formula
\[
\boxed{
m_\nu(r+60q)=\sum_{j=0}^3 c_{\nu,r,j}\binom qj
\qquad(q\ge0),}
\tag{QP.20}
\]
where \(\binom qj=0\) for \(j>q\). This identity covers all \(k\),
including \(k=0\); it is not just an asymptotic quasipolynomial.

## 6. The polytopes, coefficient, and support

Put
\[
\nu=\begin{cases}\mu,&d+1\text{ even},\\\mu^t,&d+1\text{ odd}.
\end{cases}
\tag{QP.21}
\]
For each fixed tag \((r,j)\), \(0\le r<60\), \(0\le j\le3\),
take the polytope in variables \(q,z,x_1,\ldots,x_j\) defined by
\[
\boxed{
60q=k-r,\quad q\ge0,\quad
0\le z\le c_{\nu,r,j}-1,\quad
1\le x_1<x_2<\cdots<x_j\le q.}
\tag{QP.22}
\]
The final chain is omitted when \(j=0\). Its strict inequalities are
the closed rational inequalities \(x_{i+1}-x_i\ge1\) on integer
points. A zero constant makes the polytope empty. Every coordinate is
bounded by the equality or the displayed bounds, so these are bounded
rational polytopes, each with at most five variables.

There is at most one contributing residue. For it, the choices of the
strictly increasing chain are exactly the \(j\)-subsets of
\(\{1,\ldots,q\}\), and the independent coordinate \(z\) supplies
the factor \(c_{\nu,r,j}\). Consequently the disjoint tagged lattice
count of (QP.22) is
\[
\boxed{p_{\mu,(n)}^\lambda=m_\nu(k),}
\tag{QP.23}
\]
by (QP.7), the balanced-weight dictionary T-003, and (QP.20).
This specifies a bijection from every tag's lattice witnesses to the
positive summands of the formula. It uses at most 240 fixed tags
uniformly, and at most four after computing \(k\bmod60\).

The fixed constants have at most six decimal digits. The largest entry
is 197280; thus their bit lengths are absolute constants. The remaining
right sides and integer witnesses have \(O(\log(k+2))\) bits. Evaluating
(QP.20) uses four binomial polynomials of degree at most three, so it
requires a constant number of arithmetic operations on integers of
\(O(\log(k+2))\) bits, after the partition and parity checks.

For all seven labels the exact support is particularly simple:

| \(\nu\) | condition for \(m_\nu(k)>0\) |
|---|---|
| \((5)\) | \(k\ge1\) |
| \((4,1),(3,2),(3,1,1)\) | all \(k\ge0\) |
| \((2,2,1),(2,1,1,1)\) | \(k\ge1\) |
| \((1^5)\) | \(k\ge3\) |

For \(0\le k<60\), these statements are direct substitution into the
fixed 420 constants (QP.17). The complete values are in the table
file, and the listed zero sets were checked exactly. For \(k\ge60\),
the \(j=1\) term of (QP.20) is positive because \(q\ge1\) and
\(c_{\nu,r,1}>0\). This proves the table for every integer \(k\), and
(QP.2) follows by the sign twist (QP.21).

## 7. Checks, source use, and scope

`check_q_plus_family.py` verifies (QP.9), all five signed minors and
their common primitive kernel. It also checks that each exact class
series has the asserted common denominator and degree bound, computes
all 1680 nonnegative Newton constants, checks their closed formulas
(QP.19), and compares all 2520 coefficients through \(k=359\) with the
Newton polynomials. These last comparisons are additional finite checks;
the rational-function degree argument proves the identity for all \(k\).
Receipts: `Q_PLUS_NEWTON_CHECK.tsv` and `.txt`.

The rectangular agent independently expanded the outer Schur cycle
indices and applied Murnaghan–Nakayama to every output in this family
with \(k,d\ge0\), \(d+k+2\le6\), for all seven outer partitions.
All 105 comparisons passed. The proposed traces were computed from the
literal unordered-pair character of \(U\), independently of the Newton
table. Code: `work/rectangular/verify_outer5_odd_q_family.py`; receipt:
`work/rectangular/OUTER5_ODD_Q_INDEPENDENT_CHECK.tsv`.

The source-derived facts (QP.5)–(QP.6) are the precisely applied results
in A-029, `work/archive/FIVE_POINT_POWERS.md`. The primary source is
[Kustin–Polini–Ulrich, *The equations defining blowup algebras of height three Gorenstein ideals*](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf),
*Algebra & Number Theory* 11 (2017), 1489–1525, DOI
10.2140/ant.2017.11.1489; the exact locators are given in §1. The
explicit five-point matrices and sign labels are T-038, and the
relative Schur/wedge maps in (QP.7) are spelled out here and in T-039.

The presentation (QP.13) and the positive count (QP.22) evaluate this
particular higher-flag family in full. The parameter obstruction after
(QP.15) records exactly why G-017's four-parameter free-module proof
does not extend to this module with those parameters. The new count
uses its explicit resolution and fixed quasipolynomial coefficients;
it does not assume a new freeness or cohomology-vanishing assertion.


# A five-point hook-bundle family

## T-041. Statement and exact flag comparison

For \(a\ge1\), \(d\ge0\), put
\[
n=d+a+1,\qquad
\lambda=(d+2a+4,d+a+2,d+a,d+a-1,d).
\tag{5H.1}
\]
Let \(E=\mathfrak h_5\), \(U=[3,2]\), and
\(\epsilon=\operatorname{sgn}\). There is an actual equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes U\otimes S_{(a,1)}E.}
\tag{5H.2}
\]
Every outer \(\mu\vdash5\) has the positive formula below with at most
90 fixed polytopes of dimension at most four. For symmetric outer power,
\[
\boxed{p_{(5),(n)}^\lambda>0\quad\Longleftrightarrow\quad a\ge2.}
\tag{5H.3}
\]

Indeed \(\lambda_2-n=1\), \(\lambda_2-\lambda_3=2\), and
\((\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(a,1)\).
The actual chart and extension map of G-015 therefore identifies the
left side of (5H.2) with
\[
\epsilon^{d+a}\otimes
H^0(\mathbf P(E),\mathcal I_Z(2)\otimes S_{(a,1)}Q),
\tag{5H.4}
\]
where \(Q=E/\mathcal O(-1)\) and \(Z\) is the five canonical frame
points. To check every determinant, the relative quotient-flag weight
after removing the full determinant shift is \((a,a-1,0)\).
Complementary exterior-column pairings in the rank-three quotient give
\[
S_{(a,a-1)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,1)}Q.
\]
This is the restriction of the perfect wedge pairings of complementary
columns in the height-three, width-\(a\) rectangle to their Schur
summands. The first-line twist is \(a+2\); the identity
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\) leaves
\(\mathcal O(2)\). The full determinant contributes \(\epsilon^d\),
so the total character is \(\epsilon^{d+a}\), as claimed.
The inverse flag chart is \(F\mapsto u^{-1}F(v(X))\); G-015 proves
that (5H.4)'s ideal condition is exactly its polynomial extension
condition. Thus no determinant or extension condition is suppressed.

## 1. An exact hook resolution

For a vector space \(V\), write
\[
H_a(V)=\ker(V\otimes\operatorname{Sym}^aV
                    \longrightarrow\operatorname{Sym}^{a+1}V).
\tag{5H.5}
\]
Multiplication has its equivariant polarization section divided by
\(a+1\). The kernel is \(S_{(a,1)}V\): it contains the highest vector
\(v_1\otimes v_1^{a-1}v_2-v_2\otimes v_1^a\), and the irreducible
highest-weight summand it generates has the kernel's dimension by the
Weyl dimension formula. This specifies the hook functor used here.

The line inclusion \(L=\mathcal O(-1)\subset E\otimes\mathcal O\)
gives the exact locally free resolution
\[
0\to L^2\otimes\operatorname{Sym}^{a-1}E
\mathrel{\mathop{\longrightarrow}^{d_2}}
L\otimes E\otimes\operatorname{Sym}^{a-1}E
\mathrel{\mathop{\longrightarrow}^{d_1}}
H_a(E)\otimes\mathcal O\to H_a(Q)\to0,
\tag{5H.6}
\]
with actual maps
\[
d_2(l^2\otimes v)=l\otimes l\otimes v,\qquad
d_1(l\otimes e\otimes v)=e\otimes(lv)-l\otimes(ev).
\tag{5H.7}
\]
Their composition is zero. For exactness choose a local splitting
\(E=L\oplus W\). In \(d_1\), the first tensor factors in \(W\)
record \(e\otimes lv\). Multiplication by \(l\) is injective, so
\(\ker d_1\) is exactly the subspace with \(e\in L\), the image of
\(d_2\). The map \(H_a(E)\to H_a(Q)\) is onto by the splitting.
An element of its kernel has the form
\(\sum e_i\otimes lv_i+l\otimes w\), with \(e_i\in W\).
The zero-product condition says \(w=-\sum e_iv_i\), so this element
is \(d_1(l\otimes\sum e_i\otimes v_i)\). This proves exactness at
every term of (5H.6).

## 2. All cohomology used in the formula

Put \(B_a=H_a(Q)\). The scalar projective-space calculation of Stacks
Project, Lemma 30.8.1, applied to (5H.6) gives
\[
H^0(B_a)=H_a(E),\quad H^{i>0}(B_a)=0,
\qquad H^i(B_a(-1))=0\quad\text{for all }i.
\tag{5H.8}
\]
The negative twists involved are respectively \(-2,-1\) and
\(-3,-2,-1\), all acyclic on \(\mathbf P^3\).

For \(B_a(-3)\), the three terms of (5H.6) have twists
\(-5,-4,-3\). The only possible cohomology is the map
\[
H^3(\mathcal O(-5))\otimes\operatorname{Sym}^{a-1}E
\longrightarrow H^3(\mathcal O(-4))\otimes E
                                      \otimes\operatorname{Sym}^{a-1}E.
\tag{5H.9}
\]
It is the identity under the natural identifications. The ordered Čech
generator indexed by \(i\) in the source is
\(1/(x_1x_2x_3x_4x_i)\). Multiplication by the \(j\)-th coordinate
of the line inclusion gives the top class \(1/(x_1x_2x_3x_4)\) for
\(j=i\); for \(j\ne i\), one exponent is zero, so the top class
vanishes. Thus the matrix is exactly \(\delta_{ij}\). Both spaces
carry the same factor \(\det E=H^3(\mathcal O(-4))\), so this is
also the correct equivariant map. The two short exact sequences of
(5H.6) consequently prove
\[
\boxed{H^i(B_a(-3))=0\quad\text{for all }i,\ a\ge1.}
\tag{5H.10}
\]
This includes the boundary \(a=1\), where the hook is \(\Lambda^2Q\).

Now tensor T-038's actual five-point resolution by \(B_a(2)\):
\[
0\to\epsilon B_a(-3)\to\epsilon U\otimes B_a(-1)
\to U\otimes B_a\to\mathcal I_Z(2)\otimes B_a\to0.
\tag{5H.11}
\]
Tensoring is exact because \(B_a\) is locally free. Both left terms
are acyclic by (5H.8) and (5H.10), hence multiplication gives the actual
isomorphism
\[
U\otimes H_a(E)\longrightarrow
H^0(\mathcal I_Z(2)\otimes B_a).
\tag{5H.12}
\]
It multiplies the five specified quadrics by constant hook sections and
then applies the quotient \(E\to Q\). Together with (5H.4), this
proves (5H.2). Its dimension is \(5a(a+2)(a+3)/2\).

## 3. The complete fixed positive formula

For positive weights \(W\), let
\[
C_W(R)=\#\{x\in\mathbf Z_{\ge0}^{|W|}:\sum_{w\in W}wx_w=R\}.
\tag{5H.13}
\]
This is a bounded rational-polytope count, zero for \(R<0\). Use
\(C_4=C_{(2,3,4,5)}\) and \(C_3=C_{(2,3,5)}\).
The multiplicity \(L_\rho(a)\) of \([\rho]\) in \(H_a(E)\) is
\(\sum_{r\in A_\rho}C_4(a-r)+\sum_{r\in B_\rho}C_3(a-r)\),
with all shifts listed below. Repetitions are separate tags.

| \(\rho\) | \(A_\rho\) | \(B_\rho\) |
|---|---|---|
| \((5)\) | \(4,6,13\) | \(5,6,7\) |
| \((4,1)\) | \(2,3,3,4,4,4,5,5,5,6,6,7\) | empty |
| \((3,2)\) | \(2,3,3,4,4,4,5,5,5,6,6,6,7,7,8\) | empty |
| \((3,1,1)\) | \(1,2,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,9\) | empty |
| \((2,2,1)\) | \(2,3,4,4,5,5,5,6,6,6,7,7,8,8,9\) | empty |
| \((2,1,1,1)\) | \(3,4,4,5,5,6,6,7,7,8,9,10\) | empty |
| \((1^5)\) | \(6,7,8\) | empty |

To prove the table, the polarization splitting in (5H.5) gives the
actual decomposition
\(E\otimes\operatorname{Sym}^aE=H_a(E)\oplus\operatorname{Sym}^{a+1}E\).
Writing \(H_g(t)=\det(1-tg\mid E)^{-1}\), one obtains
\[
\sum_{a\ge0}\chi_{H_a(E)}(g)t^a
=(\chi_E(g)-t^{-1})H_g(t)+t^{-1},\qquad H_0(E)=0.
\tag{5H.14}
\]
Take inner products using the seven fixed character rows of QP.16's
following table. T-027's tableau standardization gives the common
denominator \(D(t)=(1-t^2)(1-t^3)(1-t^4)(1-t^5)\).
For each nontrivial row, its numerator has exactly the nonnegative
coefficients recorded as \(A_\rho\). For the trivial row the exact
polynomial identity is
\[
\begin{aligned}
&t^4+t^5+2t^6+t^7-t^9-t^{10}-t^{11}+t^{13}\\
&\hspace{8mm}=t^4+t^6+t^{13}+(1-t^4)(t^5+t^6+t^7).
\end{aligned}
\tag{5H.15}
\]
After division by \(D(t)\), this is precisely its three four-variable
and three three-variable counts. Seven exact rational identities verify
the full table in every degree, including its zero initial terms.

For \(\mu\vdash5\), put \(\nu=\mu\) when \(d+a\) is even and
\(\nu=\mu^t\) when \(d+a\) is odd. Let \(K_{\rho\nu}\) be the
completely listed fixed \([3,2]\)-tensor table in §4 of T-039. Then
\[
\boxed{p_{\mu,(n)}^\lambda=\sum_{\rho\vdash5}K_{\rho\nu}L_\rho(a).}
\tag{5H.16}
\]
Each summand is tagged by a tensor copy, a table row and a shift. For
\(\rho\ne(5)\) there are exactly \(3\dim[\rho]\) tags; the trivial
row has three additional tags. Self-duality and the tensor dimension
identity give the total
\[
15\dim[\nu]+3\mathbf1_{\nu=(3,2)}\le90.
\tag{5H.17}
\]
Each tag has one displayed equality and nonnegative coordinates with
weights \((2,3,4,5)\) or \((2,3,5)\). Every witness has
\(O(\log(a+2))\) bits. All tables have fixed size.

For symmetric outer power, only row \((3,2)\) contributes in even
parity and only row \((2,2,1)\) in odd parity. Both have shifts two
and three and no smaller shift. Since their positive weights generate
\(\{0\}\cup\{r:r\ge2\}\), they are positive exactly for \(a\ge2\),
which proves (5H.3). The sign outer partition has the same threshold.
Every other outer partition receives row \((3,1,1)\), with shifts one
and two, and is positive for every \(a\ge1\).

## Checks and primary sources

`five_point_hook_positive.py` contains the entire fixed positive
evaluator. `check_five_point_hook.py` verifies all seven exact rational
identities, the tag bounds, and 560 finite coefficient/support cases.
Receipts: `FIVE_POINT_HOOK_CHECK.tsv` and `.txt`. The semigroup argument
proves support in every degree; the finite checks supplement it.

The scalar cohomology and explicit Čech classes are those of
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS),
whose full calculation was read. The relative Schur and exterior-column
convention uses [Magyar, Proposition 1 and Proposition 4](https://arxiv.org/pdf/alg-geom/9411014),
as specified in T-039. The hook resolution and all its maps are proved
here. The finite-group table was checked against
[Dolgachev–Farb–Looijenga, §2.3, Table 1](https://www.math.uchicago.edu/~farb/papers/wiman.pdf).

At \(a=1\) this meets the exterior-square quotient-bundle family at
point power one. For \(a>1\), it evaluates the actual rank-three hook
section space in (5H.4). No vanishing for arbitrary Schur quotient
bundles or higher point powers is assumed.


# Every symmetric quotient power on the odd five-point ray

## T-042. A complete three-parameter positive family

For \(a,k,d\ge0\), set
\[
n=d+a+k+1,\qquad
\lambda=(d+2a+3k+4,d+a+2k+1,d+a,d+a,d).
\tag{OS.1}
\]
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
is a positive count in a fixed family of at most 54,000 bounded rational
polytopes, each with at most eight variables. At most fifteen tags
contribute after the two residues \(a\bmod60\), \(k\bmod60\) are
selected. The evaluator uses a fixed number of integer arithmetic
operations; all constants are explicitly specified below and supplied
in `Q_PLUS_SYMMETRIC_TABLE.json`.

The entire support is described by 27 exceptional pairs across the seven
untwisted outer labels, listed in §6. The proof evaluates the section
space first, using actual maps, and converts its exact rational
characters into positive finite constants. It includes T-040 at \(a=1\).

## 1. The actual sheaf sequence and the plethysm comparison

Use the same \(E=\mathfrak h_5\), five frame points \(Z\), ideal
\(\mathcal I=\mathcal I_Z\), and tautological rank-three quotient
\(Q\) as in T-038–T-040. Put
\[
N_{a,k}=H^0\bigl(\mathbf P(E),\mathcal I^k(2k+1)
                                      \otimes\operatorname{Sym}^aQ\bigr),
\]
\[
C_{0,k}=H^0(\mathcal I^k(2k)),\qquad
C_{1,k}=H^0(\mathcal I^k(2k+1)).
\tag{OS.2}
\]
The partition (OS.1) satisfies \(\lambda_2-n=k\), its first gap is
\(\lambda_2-\lambda_3=2k+1\), and the rank-three quotient weight
after complement is \((a,0,0)\). G-015's exact flag chart and the
exterior-column pairings used in T-039 consequently give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes N_{a,k}.}
\tag{OS.3}
\]
To fix the linearization explicitly, remove the full determinant power
\(d\). The first-line weight is then \(a+2k+1\), and the relative
quotient-flag module is \(S_{(a,a)}Q^*\). The actual rank-three wedge
map identifies it with
\((\det Q^*)^a\otimes\operatorname{Sym}^aQ\).
Since \(\det Q^*=\det E^*\otimes\mathcal O(-1)\), the remaining
line twist is \(2k+1\), and the determinant character is exactly
\(\epsilon^{d+a}\). The inverse flag map is
\(F\mapsto u^{-k}F(v(X))\). G-015 proves that membership in the
order-\(k\) ideal in (OS.2) is precisely what makes that expression
a polynomial. Thus (OS.3) specifies the geometric and representation
comparison, including its extension condition.

For \(a\ge1\), multiplication by the tautological vector gives the
locally split exact bundle sequence, and hence the ideal-tensored
exact sequence,
\[
0\to\mathcal I^k(2k)\otimes\operatorname{Sym}^{a-1}E
\to\mathcal I^k(2k+1)\otimes\operatorname{Sym}^{a}E
\to\mathcal I^k(2k+1)\otimes\operatorname{Sym}^{a}Q\to0.
\tag{OS.4}
\]
Fiberwise its first map is \(l\otimes v\mapsto lv\) and the last
is the quotient of symmetric algebras. The kernel is exactly
\(L\operatorname{Sym}^{a-1}E\); multiplication by a nonzero line
vector is injective. Local splitting preserves exactness after the
possibly nonflat ideal tensor.

The cohomology vanishing \(H^1(\mathcal I^k(2k))=0\) is (QP.5):
A-029 proves it from the linear powers for \(k\ge2\); at \(k=1\)
degree-two evaluation onto the five point values proves it; and at
\(k=0\) it is the scalar \(\mathcal O\) calculation. Therefore the
actual global-section sequence is
\[
\boxed{0\to C_{0,k}\otimes\operatorname{Sym}^{a-1}E
\to C_{1,k}\otimes\operatorname{Sym}^{a}E
\to N_{a,k}\to0.}
\tag{OS.5}
\]
There is no exceptional \(k=1\) correction in this twist. At \(a=0\),
use \(\operatorname{Sym}^{-1}E=0\), and the assertion is simply
\(N_{0,k}=C_{1,k}\). This proves every endpoint as well as the exact
maps underlying the character identity below.

## 2. The full bivariate rational character

Let \(U=[3,2]\), \(e_g=\chi_E(g)\), \(u_g=\chi_U(g)\), and
\(\epsilon_g=\operatorname{sgn}(g)\). The cubic algebra and the
scalar-piece resolution (QP.11) give
\[
C_{0,g}(t)=\frac{1-\epsilon_gt^3}{\det(1-tg\mid U)},\qquad
C_{1,g}(t)=\frac{e_g-\epsilon_gu_gt+\epsilon_gt^2}
                     {\det(1-tg\mid U)}.
\tag{OS.6}
\]
These are traces of the actual Rees pieces in (OS.2); their saturation
and presentation comparison was proved in T-040 §§1–2. Taking traces
of (OS.5) yields
\[
\boxed{\sum_{a,k\ge0}\chi_{N_{a,k}}(g)s^at^k
=\frac{e_g-s-\epsilon_gu_gt+\epsilon_gt^2+
                         \epsilon_gst^3}
 {\det(1-sg\mid E)\det(1-tg\mid U)}.}
\tag{OS.7}
\]
The numerator is exactly \(C_{1,g}-sC_{0,g}\) times the symmetric
algebra series of \(E\). All determinant denominators are fixed by the
seven ordinary cycle types and T-038's explicit signed six-letter map.

There is an independent exact trace formula using the point jets. For a
cycle type \(\eta=(\eta_1,\ldots,\eta_\ell)\vdash5\), define
\[
h_\eta(r)=[x^r]\frac{1-x}{\prod_{i=1}^{\ell}(1-x^{\eta_i})},
\qquad h_\eta(r)=0\quad(r<0),
\tag{OS.8}
\]
and let \(m_1(\eta)\) be its number of fixed letters. Then
\[
\chi_{C_{j,k}}(\eta)
=h_\eta(2k+j)-m_1(\eta)h_\eta(k-1),\qquad j=0,1.
\tag{OS.9}
\]
Here is the scheme and action calculation. The exact evaluation sequence
for \(\mathcal I^k(2k+j)\) is right exact on global sections by the
vanishing already checked. The permutation trace on its fat-point
quotient receives a contribution only from fixed frame points. At such
a point, the canonical representative \(\ell_i\) is literally fixed
by its stabilizer \(S_4\), so the twisting line has trivial stabilizer
action. An invariant affine chart identifies its tangent coordinates
with \(E/\mathbf Q\ell_i\). The completed local ring modulo the
\(k\)-th maximal-ideal power has the actual filtration with quotients
\(\operatorname{Sym}^r(E/\mathbf Q\ell_i)^*\), \(0\le r<k\).
The coordinate action is linear on this chart, so it is also their
direct sum as a stabilizer module. The removed line is trivial, hence
the generating series of these cumulative jets, as \(k\) varies, is
\[
\frac{t}{1-t}\frac1{\det(1-tg\mid E/\mathbf Q\ell_i)}
=\frac{t}{\det(1-tg\mid E)}.
\]
Summing over the \(m_1\) fixed points proves (OS.9). This describes
the evaluation morphism and its finite-group trace directly, without
assuming that the point-jet action is an unproved permutation module.

The seven irreducible character rows and class sizes are the complete
fixed tables in §4 of T-040. Equations (OS.5), (OS.8) and (OS.9) give
the following explicit integer for the multiplicity of \([\nu]\):
\[
\begin{aligned}
b_\nu(a,k)=\frac1{120}\sum_{\eta\vdash5}
|\mathcal C_\eta|\chi_\nu(\eta)\bigl[&h_\eta(a)
 (h_\eta(2k+1)-m_1h_\eta(k-1))\\
&-h_\eta(a-1)(h_\eta(2k)-m_1h_\eta(k-1))\bigr].
\end{aligned}
\tag{OS.10}
\]
This finite signed expression is used only to specify and verify the
fixed constants in §4. The delivered coefficient formula itself is
the positive lattice count in §5.

## 3. Exact polynomial behavior on every residue pair

For each of the seven classes, each of the four one-variable factors
\[
\det(1-sg\mid E)^{-1},\quad
s\det(1-sg\mid E)^{-1},\quad C_{0,g}(t),\quad C_{1,g}(t)
\tag{OS.11}
\]
has denominator dividing \((1-v^{60})^4\), and its numerator after
using this common denominator has degree at most 239. This follows
from the displayed fixed determinants, or by direct polynomial
division; all 28 exact identities are in the certificate script.
The roots of the denominators have orders dividing 60. Their largest
pole order is four; for the identity the factor \(1-t\) in each
scalar numerator cancels the fifth-dimensional symmetric-algebra pole.

Consequently, for every \(0\le r,s<60\),
\[
(q,p)\longmapsto b_\nu(r+60q,s+60p)
\tag{OS.12}
\]
is a polynomial of degree at most three in each variable, valid for
all \(q,p\ge0\). To see the initial range as well, group a common
numerator by its residues: each residue series has denominator
\((1-v)^4\) and numerator of degree at most three. Its coefficient
is a linear combination of \(\binom{q-j+3}{3}\), \(0\le j\le3\).
For \(q<j\), the polynomial binomial value is already zero, so the
polynomial is valid beginning at zero. Products of these two exact
one-variable descriptions prove (OS.12).

The coefficient of bidegree \((3,3)\) is zero. For a nonidentity
class the multiplicities of eigenvalues on the four-dimensional
standard module are at most three. Its \(a\)-residue polynomial
therefore has degree at most two. At the identity, the coefficient of
\(a^3\) in (OS.5)'s dimension is proportional to
\(\dim C_{1,k}-\dim C_{0,k}\). Their series difference is
\((3+t)/(1-t)^3\), a degree-two polynomial in \(k\). Thus a third
difference in each variable kills every class term. This proves
the bidegree assertion without relying on finite sampling.

## 4. Every fixed positive constant

For \(0\le i,j\le3\) define
\[
\boxed{c_{\nu,r,s;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv\,
b_\nu(r+60u,s+60v).}
\tag{OS.13}
\]
Every argument on the right is below 240. In (OS.8), the largest
coefficient needed to compute them is below 480. Thus (OS.8),
(OS.10), the seven fully listed fixed character rows, and (OS.13)
are a complete finite arithmetic specification of all constants.
They are also supplied literally in the complete table file, indexed
by `labels[nu][r][s][4*i+j]`.

The exact integer certificate verifies all 403,200 constants and gives
\[
\boxed{c_{\nu,r,s;i,j}\ge0;\qquad
c_{\nu,r,s;3,3}=0.}
\tag{OS.14}
\]
Every other positive-order coefficient is strictly positive. In
particular, all \(c_{\nu,r,s;1,0}\) and
\(c_{\nu,r,s;0,1}\) are positive. The minimum among all positive-order
coefficients other than \((3,3)\) is 926. The maximum among all
constants is 607840200, less than \(2^{30}\).

This finite verification is reproducible in
`q_plus_symmetric_certificate.py`. It builds the scalar traces using
the independent point-jet formula (OS.9), verifies their agreement with
the presentation expressions (OS.6), takes the seven character inner
products, and takes exact integer forward differences. It checks
integrality and nonnegativity of every entry, not numerical rounding.
`Q_PLUS_SYMMETRIC_SUMMARY.json` records the minimum and maximum of each
of the sixteen difference orders for every label. The full table is
`Q_PLUS_SYMMETRIC_TABLE.json`; the concise receipt is
`Q_PLUS_SYMMETRIC_CHECK.txt`.

The archive agent independently reconstructed all constants using the
\(\mathsf B(T)\)-presentation character and Newton identities for
the characteristic polynomial of \(U\), without using point jets.
All 403,200 entries, all 28 rational degree bounds, and all zero pairs
agreed. Its independent receipt is
`work/archive/Q_PLUS_SYMMETRIC_PRESENTATION_RECEIPT.json`.

Applying the ordinary two-variable Newton identity to (OS.12) now
proves the positive formula
\[
\boxed{b_\nu(r+60q,s+60p)=
\sum_{i=0}^3\sum_{j=0}^3
c_{\nu,r,s;i,j}\binom qi\binom pj\qquad(q,p\ge0).}
\tag{OS.15}
\]
The sole bidegree-six tag is zero by (OS.14). This identity holds for
all parameters, by the rational-function proof of §3; the finite
certificate supplies the exact signs of its fixed coefficients.

## 5. The actual polytopes and evaluator

For the outer label in (OS.1), set
\[
\nu=\begin{cases}\mu,&d+a\text{ even},\\\mu^t,&d+a\text{ odd}.
\end{cases}
\tag{OS.16}
\]
For each fixed tag \((r,s,i,j)\), \(0\le r,s<60\),
\(0\le i,j\le3\), \((i,j)\ne(3,3)\), use the rational polytope
\[
\begin{gathered}
60q=a-r,\qquad60p=k-s,\qquad q,p\ge0,\\
0\le z\le c_{\nu,r,s;i,j}-1,\\
1\le x_1<\cdots<x_i\le q,\qquad
1\le y_1<\cdots<y_j\le p.
\end{gathered}
\tag{OS.17}
\]
Omit an empty chain when its length is zero. Strict inequalities on
integer points mean the closed inequalities
\(x_{h+1}-x_h\ge1\), and likewise for \(y\). A zero constant makes
the polytope empty. These are bounded polytopes: the two equalities
bound \(q,p\), the interval bounds \(z\), and the chains bound every
remaining coordinate.

Only the actual two residues contribute integer points. For them, the
chains choose an \(i\)-subset of \(\{1,\ldots,q\}\) and a
\(j\)-subset of \(\{1,\ldots,p\}\); the independent coordinate
\(z\) supplies exactly \(c_{\nu,r,s;i,j}\) choices. Therefore the
disjoint tagged lattice count is
\[
\boxed{p_{\mu,(n)}^\lambda=b_\nu(a,k).}
\tag{OS.18}
\]
This follows from (OS.3), the balanced-space covariant projector T-003,
and (OS.15). There are at most \(60^2\cdot15=54000\) fixed tags;
at most fifteen contribute for a given pair of residues. The number
of variables is \(3+i+j\le8\). Every variable and nonconstant right
side has \(O(\log(a+k+2))\) bits; the fixed coefficient interval has
an absolute thirty-bit bound.

`q_plus_symmetric_positive.py` evaluates (OS.15) directly from the
fixed table and exports the complete matrices of (OS.17). It validates
all three nonnegative integer parameters and the outer partition. The
count requires at most fifteen products of cubic binomial polynomials;
its integer arithmetic cost is polynomial in the input bit length.
No runtime character, elimination, or unknown coefficient computation
is part of the evaluator.

## 6. Complete support and explicit propagation maps

For the untwisted label \(\nu\), the complete zero sets of
\(b_\nu(a,k)\), \(a,k\ge0\), are:

| \(\nu\) | zero pairs \((a,k)\) |
|---|---|
| \((5)\) | \((0,0),(0,1),(1,0)\) |
| \((4,1)\) | none |
| \((3,2)\) | \((0,0)\) |
| \((3,1,1)\) | \((0,0)\) |
| \((2,2,1)\) | \((0,0),(0,1),(1,0)\) |
| \((2,1,1,1)\) | \((0,j),(j,0)\), \(0\le j\le2\) |
| \((1^5)\) | \((0,j),(j,0)\), \(0\le j\le5\), and \((1,1),(1,2),(2,1)\) |

The pair \((0,0)\) is counted once in each union. There are 27 pairs
in total across the seven rows. The full residue computation proves
this immediately: inside the \(60\)-by-\(60\) box, these are exactly
the zero constants of order \((0,0)\). Outside it at least one
quotient \(q,p\) is positive, and the corresponding strictly positive
first-difference term in (OS.15) proves positivity.

There is also a smaller geometric verification of the same finite
support reduction. The invariant nondegenerate quadratic tensor
\(\sigma\in\operatorname{Sym}^2E\) gives a nonzero section of
\(\operatorname{Sym}^2Q\) on every fiber. Its image could vanish on
\(E/L\) only if \(\sigma\in L E\); such a tensor has rank at most
two, whereas \(\sigma\) has rank four. Multiplication by this section
therefore gives an equivariant injection
\[
N_{a,k}\hookrightarrow N_{a+2,k}.
\tag{OS.19}
\]
Locally, multiplication by a nonzero quadratic in the symmetric
algebra of the quotient fiber is injective, with constant rank; thus
tensoring by the point ideal preserves the bundle inclusion.

For the other parameter, T-038's six forms have invariant elementary
symmetric polynomial \(e_2(T)\). Its image in \(R/(F)\) is nonzero,
since it has degree two and \(F\) has degree three. It is a section
of \(\mathcal I^2(4)\). Multiplication gives the actual equivariant
injection
\[
N_{a,k}\hookrightarrow N_{a,k+2}.
\tag{OS.20}
\]
The ideal tensored with a vector bundle is torsion-free on integral
projective space, and a nonzero scalar polynomial has no kernel on
its sections. These maps prove coefficientwise support propagation
by two in either parameter.

The 448 values with \(0\le a,k\le7\) and all seven labels, computed
from the fixed expression (OS.10), already have exactly the table's
zero pairs, and every entry in rows or columns six and seven is
positive. Reduce any larger parameter by an even number to six or
seven and apply (OS.19)–(OS.20). This is an independent finite support
argument using only that smaller box and the explicit injection maps.
For the actual outer partition, apply the sign conversion (OS.16).

## 7. Verification record and scope

The full rational identities and all 403,200 fixed constants were
independently reconstructed as described in §4. In addition,
`check_q_plus_symmetric_evaluator.py` passed 3542 exact evaluator
comparisons: 2534 specializations to the independently proved T-040
formula at \(a=1\), and 1008 literal polytope-matrix counts. It
checked 10,589 explicit endpoint witnesses against every matrix
inequality. Receipt: `Q_PLUS_SYMMETRIC_EVALUATOR_CHECK.txt`.

The only ideal-power input is the fully applied A-029 proof, based on
[Kustin–Polini–Ulrich, *The equations defining blowup algebras of height three Gorenstein ideals*](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf),
formula (6.1.4), p. 1509, Lemma 6.3 and Corollary 6.4, p. 1510, with
the proof on p. 1511. Its local hypotheses, ordinary-power linearity,
and saturation range were checked for this actual five-point ideal.
The relative flag and dual conventions are the specified Schur maps
of [Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
transported by the exterior-column identities above and in T-039.

This evaluates every symmetric quotient power on the twist \(2k+1\).
G-019 evaluates the adjacent twist \(2k\); both use the same actual
five-point scheme and flag-chart morphism. T-041 evaluates a separate
hook quotient-bundle family at point power one. The assertions here
do not require new vanishing statements for general Schur quotient
bundles, and no global novelty claim is made.


# Every hook quotient power on the five-point quadratic ray

## T-043. Statement

Let \(a\ge1\), \(k,d\ge0\), and put
\[
n=d+a+k,\qquad
\lambda=(d+2a+3k+1,d+a+2k,d+a,d+a-1,d).
\tag{HA.1}
\]
Every outer coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\),
has a positive count in at most 54,000 fixed tagged polytopes, each
using at most eight variables. After selecting the two residues,
at most fifteen tags contribute. The coefficient is computed by a
fixed number of integer arithmetic operations from a complete fixed
table. Its support consists of all parameter pairs except the seventeen
untwisted zero pairs listed in §5.

This evaluates all point orders and all rank-three hook quotient
functors together. It includes T-041 at \(k=1\) and G-018 at \(a=1\).
The proof below establishes the actual sheaf comparison and all higher
cohomology before using a character formula.

## 1. The flag morphism and an exact sheaf complex

Let \(E=\mathfrak h_5\), \(Q\) be its tautological rank-three
quotient on \(\mathbf P(E)\), and \(\mathcal I\) the ideal of the
five canonical projective-frame points. Write
\[
D_{a,k}=H^0(\mathbf P(E),\mathcal I^k(2k)\otimes S_{(a,1)}Q).
\tag{HA.2}
\]
For (HA.1), the point order is \(\lambda_2-n=k\), the first gap is
\(2k\), and the quotient weight after complement is \((a,1,0)\).
The relative quotient-flag module before complement is
\(S_{(a,a-1)}Q^*\), and its first-line weight is \(a+2k\).
The actual complementary exterior-column pairing
\[
S_{(a,a-1)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,1)}Q,
\quad\det Q^*=\det E^*\otimes\mathcal O(-1)
\]
leaves twist \(2k\) and determinant \(\epsilon^{d+a}\). Consequently
G-015 gives the specified equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes D_{a,k}.}
\tag{HA.3}
\]
Its inverse is \(F\mapsto u^{-k}F(v(X))\). G-015 proves that the
order-\(k\) ideal in (HA.2) is precisely the polynomial-extension
condition. These are the same relative frame maps proved for T-041;
the changed integer twist has been retained in each displayed factor.

Put \(H_a(V)=S_{(a,1)}V\), realized by the actual multiplication kernel
\(\ker(V\otimes\operatorname{Sym}^aV\to\operatorname{Sym}^{a+1}V)\).
T-041 proved the locally split hook resolution with maps
\(l^2v\mapsto l\otimes l\otimes v\) and
\(l\otimes e\otimes v\mapsto e\otimes lv-l\otimes ev\).
Tensor it with \(\mathcal I^k(2k)\). Its locally split exactness
preserves the complete complex
\[
\begin{split}
0\to&\mathcal I^k(2k-2)\otimes\operatorname{Sym}^{a-1}E\\
\to&\mathcal I^k(2k-1)\otimes E\otimes\operatorname{Sym}^{a-1}E\\
\to&\mathcal I^k(2k)\otimes H_a(E)\\
\to&\mathcal I^k(2k)\otimes H_a(Q)\to0.
\end{split}
\tag{HA.4}
\]
The maps are exactly the displayed hook maps multiplied by a local
section of the ideal. This specifies the entire complex, rather than
only its class in a representation group.

## 2. Complete higher-cohomology vanishing and its endpoints

For \(k\ge2\), A-029's linear-power result gives
\(H^1(\mathcal I^k(2k-1))=H^1(\mathcal I^k(2k))=0\).
For every twist \(c\ge0\), the ideal sequence with its zero-dimensional
fat-point quotient gives
\(H^i(\mathcal I^k(c))=H^i(\mathcal O(c))=0\) for \(i=2,3\).
In particular this applies also to \(c=2k-2\).

Let \(K\) be the image of the middle term into the next term in
(HA.4). In its first short exact sequence, the possible
\(H^1(\mathcal I^k(2k-2))\) contributes only to \(H^0(K)\).
All the groups forcing \(H^i(K)\), \(i\ge1\), vanish by the preceding
paragraph. The second short exact sequence, whose other term is
\(\mathcal I^k(2k)\otimes H_a(E)\), therefore proves
\[
H^i(\mathcal I^k(2k)\otimes H_a(Q))=0\quad(i\ge1,k\ge2).
\tag{HA.5}
\]
This argument does not assert that the leftmost ideal in (HA.4) is
acyclic; its possible first cohomology has been included exactly.

At \(k=1\), T-041 proves the actual isomorphism
\(D_{a,1}=U\otimes H_a(E)\), with \(U=[3,2]\), and proves all
higher cohomology zero. It does so by the five-point resolution and
the explicit identity map in top Čech cohomology of the negative
hook twists. At \(k=0\), (HA.4) has negative scalar twists
\(-2,-1\), both acyclic; it gives
\(D_{a,0}=H_a(E)\) and again no higher cohomology. Thus (HA.5) holds
for every \(k\ge0\), with its two endpoints established separately.

Taking the equivariant Euler characteristic of the actual complex now
computes its actual zeroth cohomology. For every \(a\ge1,k\ge0\),
\[
\boxed{
[D_{a,k}]=[H_a(E)]\chi(\mathcal I^k(2k))
+[\operatorname{Sym}^{a-1}E]
\bigl(\chi(\mathcal I^k(2k-2))
       -[E]\chi(\mathcal I^k(2k-1))\bigr).}
\tag{HA.6}
\]
Here \(\chi\) denotes the finite alternating sum of actual cohomology
modules. Its use on the leftmost ideal retains its possible first
cohomology. The final positive count in §4 removes the signs in this
intermediate character computation.

## 3. Explicit rational characters

For a cycle type \(\eta\vdash5\), let
\[
h_\eta(r)=[z^r]\frac{1-z}{\prod_{\ell\in\eta}(1-z^\ell)},
\quad h_\eta(r)=0\ (r<0),\qquad e_\eta=m_1(\eta)-1.
\tag{HA.7}
\]
The exact fat-point jet action is proved in T-042 §2: at a fixed point,
the canonical invariant affine chart has tangent representation
\(E/\mathbf Q\ell_i\), and the line twist has trivial stabilizer
character. The total jet trace is
\(m_1h_\eta(k-1)\). Therefore, for \(j=0,-1,-2\),
\[
\operatorname{tr}(\eta\mid\chi(\mathcal I^k(2k+j)))
=h_\eta(2k+j)-m_1h_\eta(k-1).
\tag{HA.8}
\]
This identity uses the ideal evaluation sequence as an Euler identity,
so it does not require its map on global sections to be onto at
\(j=-1,-2\). At \(k=0\), the negative scalar twists \(-1,-2\)
are acyclic, exactly matching the convention in (HA.7).

The hook trace is
\(\chi_{H_a(E)}(\eta)=e_\eta h_\eta(a)-h_\eta(a+1)\), by the
polarization splitting. Combining (HA.6)–(HA.8) specifies the complete
trace for every parameter. At the identity, it gives the useful check
\[
\boxed{\dim D_{a,k}=
\frac{a(a+2)}6\bigl[
a(4k^2+8k+3)+3k^3+13k^2+20k+9\bigr].}
\tag{HA.9}
\]
It specializes to \(a(a+2)(a+3)/2\) at \(k=0\) and to five times
that dimension at \(k=1\).

For a finite rational specification of the residue-polynomial bound,
let \(H(z)=\det(1-z\eta\mid E)^{-1}\), and put
\[
E_\eta(t)=\sum_{k\ge0}h_\eta(2k)t^k,\qquad
O_\eta(t)=\sum_{k\ge0}h_\eta(2k+1)t^k,\qquad
J_\eta(t)=m_1tH(t).
\]
They are obtained by the exact even and odd parts of \(H\). If
\(D(z)=\det(1-z\eta\mid E)\), the even numerator is
\((D(z)+D(-z))/2\) and the odd numerator is
\((D(-z)-D(z))/(2z)\), both over \(D(z)D(-z)\); replacing
\(z^2\) by \(t\) gives the two rational functions just defined.
For the nonnegative first parameter \(b=a-1\), the full bivariate
trace is
\[
\boxed{\begin{aligned}
\sum_{b,k\ge0}\chi_{D_{b+1,k}}(\eta)s^bt^k
={}&\frac{(e_\eta-s^{-1})H(s)+s^{-1}}s
                       (E_\eta(t)-J_\eta(t))\\
&+H(s)\bigl[tE_\eta(t)-e_\eta tO_\eta(t)
                              +(e_\eta-1)J_\eta(t)\bigr].
\end{aligned}}
\tag{HA.10}
\]
The apparent negative powers of \(s\) cancel: the numerator's
constant and linear terms vanish before division by \(s^2\).
Each of its four one-variable factors has denominator dividing
\((1-v^{60})^4\), with common numerator degree at most 239.
All 28 polynomial divisibilities for the seven classes are verified
exactly in the certificate, with the reduced factors retained in its
summary. The even/odd scalar series are separately checked against
direct permutation-cycle recurrences.

It follows, by the residue argument proved explicitly in T-040 §4
and T-042 §3, that on each residue pair \((r,s)\),
\(D_{1+r+60q,s+60p}\) has irreducible multiplicities polynomial of
degree at most three in each of \(q,p\), for all \(q,p\ge0\).
The initial range is included because the residue numerator has degree
at most three: its binomial coefficient polynomials vanish at every
required small value, not just eventually.

The bidegree \((3,3)\) coefficient is zero. Every nonidentity class
has pole order at most three in the standard-module variable, so its
\(b\)-residue degree is at most two. The identity dimension (HA.9)
has no monomial of bidegree \((3,3)\), even after replacing \(a\)
by \(b+1\). Thus the mixed third difference vanishes in every class.

## 4. Complete positive constants and actual polytopes

Let \(m_\nu(b,k)=[D_{b+1,k}:[\nu]]\). It is explicitly specified
by taking the inner product of (HA.6)–(HA.8) with the seven fixed
character rows in T-040 §4, of class sizes
\(1,10,15,20,20,30,24\). Define
\[
\boxed{c_{\nu,r,s;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv
m_\nu(r+60u,s+60v),}
\tag{HA.11}
\]
for \(0\le r,s<60\), \(0\le i,j\le3\). The exact finite
certificate computes all 403,200 integers, proves each is nonnegative,
and finds \(c_{\nu,r,s;3,3}=0\). Every other positive-order constant
is strictly positive. Their minimum is 941; the maximum of all constants
is 1213066800, less than \(2^{31}\). All zeroth-order constants are
also nonnegative, as they are actual module multiplicities.

Every value is explicitly specified by (HA.7), (HA.8), the finite
character table, and (HA.11), and is supplied literally in
`HOOK_ALL_POWERS_TABLE.json`. The index is
`labels[nu][(a-1)_mod_60][k_mod_60][4*i+j]`.
The complete exact computation is `hook_all_powers_certificate.py`;
its summary contains every rational factor and all sixteen minima and
maxima for each label. The receipt is `HOOK_ALL_POWERS_CHECK.txt`.

Newton's identity and the rational degree bound prove, for all
\(q,p\ge0\),
\[
\boxed{m_\nu(r+60q,s+60p)=
\sum_{i,j=0}^3 c_{\nu,r,s;i,j}\binom qi\binom pj.}
\tag{HA.12}
\]
For the actual outer partition put \(\nu=\mu\) when \(d+a\) is
even and \(\nu=\mu^t\) when it is odd. For each tag
\((r,s,i,j)\ne(r,s,3,3)\), use the bounded rational polytope
\[
\begin{gathered}
60q=a-1-r,\qquad60p=k-s,\qquad q,p\ge0,\\
0\le z\le c_{\nu,r,s;i,j}-1,\\
1\le x_1<\cdots<x_i\le q,\qquad
1\le y_1<\cdots<y_j\le p.
\end{gathered}
\tag{HA.13}
\]
Omit an empty chain. Replace strict inequalities by difference-at-least-
one inequalities for the integer points. Zero constants give empty
polytopes. The chains choose subsets and the interval supplies the
constant factor, so the tagged count is exactly
\[
\boxed{p_{\mu,(n)}^\lambda=m_\nu(a-1,k).}
\tag{HA.14}
\]
Only one residue pair contributes. There are at most 54,000 uniform
tags and fifteen contributing tags; \(3+i+j\le8\) variables suffice.
All nonconstant witness coordinates have logarithmic bit length in
\(a+k+2\), and the fixed interval has an absolute 31-bit bound.

`hook_all_powers_positive.py` is the standalone evaluator and explicit
constraint-matrix exporter. It evaluates the fifteen binomial products
from the fixed table, validates \(a\ge1,k,d\ge0\), and requires no
runtime character or algebraic elimination computation.

## 5. Complete support

In terms of \(b=a-1\), the full untwisted zero sets are:

| \(\nu\) | zero pairs \((b,k)\) |
|---|---|
| \((5)\) | \((0,0),(0,1),(0,2),(1,0),(2,0)\) |
| \((4,1)\) | \((0,0)\) |
| \((3,2)\) | \((0,0)\) |
| \((3,1,1)\) | none |
| \((2,2,1)\) | \((0,0)\) |
| \((2,1,1,1)\) | \((0,0),(1,0)\) |
| \((1^5)\) | \((0,0),(0,1),(0,2),(1,0),(2,0),(3,0),(4,0)\) |

There are seventeen pairs across all rows. The finite residue table
checks the zeros in its 60-by-60 box. Outside it, at least one quotient
parameter is positive; the corresponding strictly positive first
difference in (HA.12) proves positivity. Apply the label conversion
preceding (HA.13) to obtain the complete support for any outer partition.

There is also the explicit small-box propagation check. Multiplication
by the invariant quadratic section \(\sigma_Q\in H^0(\operatorname{Sym}^2Q)\)
from (OS.19) preserves the hook kernel:
\(Q\otimes\operatorname{Sym}^aQ\to
Q\otimes\operatorname{Sym}^{a+2}Q\) sends its product to the old
product times \(\sigma_Q\), so zero products remain zero. The
multiplication is injective on every fiber, since \(\sigma_Q\) is
nonzero there. It gives an equivariant injection
\(D_{a,k}\hookrightarrow D_{a+2,k}\).
Multiplication by the invariant nonzero section \(e_2(T)\in\mathcal I^2(4)\)
gives \(D_{a,k}\hookrightarrow D_{a,k+2}\), exactly as in (OS.20).
The values with \(0\le b,k\le7\) already have exactly the displayed
zeros, and rows or columns six and seven are positive. Reduction by
even increments and these injections therefore prove the same entire
support from that smaller finite box.

In particular, for symmetric outer power and \(k\ge1\), positivity
is equivalent to \(a\ge2\) or \(k\ge3\). At \(k=0\), it is
equivalent to \(a\ge4\) in even parity \(d+a\), and to \(a\ge6\)
in odd parity. These are just the two relevant rows of the complete
zero table.

## Checks, source attribution, and next scope

`check_hook_all_powers_evaluator.py` passed 5222 evaluator comparisons:
1680 specializations to T-041 at \(k=1\), 2534 to the independently
proved G-018 at \(a=1\), and 1008 literal polytope counts. It checked
10,670 explicit matrix witnesses. Receipt:
`HOOK_ALL_POWERS_EVALUATOR_CHECK.txt`.

The only ideal-power vanishing imported is the applied A-029 result,
with its actual ideal hypotheses checked against
[Kustin–Polini–Ulrich, formula (6.1.4), p. 1509, Lemma 6.3 and Corollary 6.4, p. 1510](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
The projective scalar vanishings and explicit Čech calculation are
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).
The relative Schur convention and its dual comparison are those of
[Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
with every determinant pairing spelled out above and in T-041.
The hook resolution itself was proved with its actual maps in T-041;
its ideal-tensored cohomology is proved here for all point orders.

This completes the hook quotient family on the quadratic ray. G-019
and T-042 evaluate symmetric quotient functors on the two adjacent
twists. More general two-row quotient shapes have a longer range of
parameters; no assertion about their positive residue constants is
assumed in the statements above.


# Symmetric quotient powers throughout the nonnegative twist region

## G-020. A four-parameter positive coefficient formula

Let \(a,k,t,d\ge0\), and put
\[
n=d+a+k+t,\qquad
\lambda=(d+2a+3k+4t,d+a+2k+t,d+a,d+a,d).
\tag{TP.1}
\]
These are partitions of \(5n\); zero parts are omitted. Every coefficient
\(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the following fixed
positive formula. It uses at most 36 active lattice tags, each with at
most nine integer variables, after computing the residues of \(a,k,t\)
modulo 60. A single uniform description before selecting residues has
at most \(60^3\cdot36=7,776,000\) tags. All constants are specified
by the seven elementary trace functions in (TP.8) and the fixed finite
formula (TP.11). No large lookup table or input-dependent representation
calculation is required by the evaluator.

The effective outer label is
\[
\nu=\begin{cases}\mu,&d+a\text{ even},\\\mu',&d+a\text{ odd}.
\end{cases}
\tag{TP.2}
\]
For each such label, positivity fails at only the explicitly listed
triples in §5. There are 115 exceptional triples in total across the
seven effective labels. Thus the result gives a complete nonvanishing
decision in the entire family (TP.1). It contains G-019 at \(t=0\)
and T-042 at \(t=1\), with the same actual sheaf comparison.

## 1. Exact flag transport and complete cohomology calculation

Retain \(E=\mathfrak h_5\), the canonical five-point scheme \(Z\),
its ideal \(\mathcal I\), and the tautological rank-three quotient
bundle \(Q\). Write \(c=2k+t\), and define
\[
M_{a,k,t}=H^0(\mathbf P(E),\mathcal I^k(c)
                                      \otimes\operatorname{Sym}^aQ).
\tag{TP.3}
\]
The point order of (TP.1) is \(\lambda_2-n=k\), its first-line gap
is \(c\), and its relative quotient weight is \((a,a,0)\). The exact
G-015 chart and the complementary exterior pairing of T-039 give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,k,t}.}
\tag{TP.4}
\]
In detail the first-line twist before dualizing the relative quotient
is \(a+c\). The isomorphism
\(S_{(a,a)}Q^*\simeq(\det Q^*)^a\otimes\operatorname{Sym}^aQ\),
with \(\det Q^*=\det E^*\otimes\mathcal O(-1)\), leaves precisely
\(\mathcal O(c)\) and the character in (TP.4). The inverse balanced
chart is \(f\mapsto u^{-k}f(v(X))\). G-015 proves its extension
condition to be the ordinary sheaf power in (TP.3).

The locally split symmetric quotient sequence, tensored by the ideal,
is
\[
0\to\mathcal I^k(c-1)\otimes\operatorname{Sym}^{a-1}E
\longrightarrow\mathcal I^k(c)\otimes\operatorname{Sym}^aE
\longrightarrow\mathcal I^k(c)\otimes\operatorname{Sym}^aQ\to0.
\tag{TP.5}
\]
For \(a=0\), the left term is zero. Its maps multiply by the
tautological vector and apply the quotient, exactly as in (SQ.4).

A-029 proves the required regularity for every \(k\ge2\):
\(H^1(\mathcal I^k(c))=H^1(\mathcal I^k(c-1))=0\) for \(c\ge2k\).
The precise known inputs, with the local hypotheses checked in A-029,
are Kustin–Polini–Ulrich, formula (6.1.4), printed p. 1509, Lemma 6.3
and Corollary 6.4, p. 1510, in
[Algebra & Number Theory 11 (2017), 1489–1525](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
For \(k=1\), degree-two evaluation is onto, so the same vanishings hold
except at \(c=2\), where
\(H^1(\mathcal I(1))=\mathbf1\). For \(k=0\), the line-bundle
cohomology in all used degrees is given by Stacks Project, Lemma 30.8.1,
tag 01XS, with \(\mathcal O(-1)\) acyclic.

For all the parameters, \(H^i(\mathcal I^k(c-1))=0\) for \(i=2,3\):
the fat-point quotient has dimension zero, and \(c-1\ge-1\), so this
follows from the same scalar projective cohomology. Also
\(H^{i>0}(\mathcal I^k(c))=0\). The long sequence of (TP.5) therefore
proves that its quotient has no positive cohomology for every
\(a,k,t\ge0\). The exceptional source group at \((k,t)=(1,0)\)
contributes to its degree-zero sections exactly as in T-039; it does
not create higher cohomology. Consequently its character is the
Euler-class difference of the two left terms of (TP.5), including
that endpoint.

## 2. The actual jet evaluation and seven elementary trace functions

For \(g\in S_5\), write \(f_g\) for its fixed-letter count and
\(h_N(g)=\operatorname{tr}(g\mid\operatorname{Sym}^NE)\), with
\(h_{-1}=0\). The invariant affine trivializations and normal-coordinate
maps in G-018 §2 identify the full order-\(k\) jet representation with
the induced sum of the first \(k\) symmetric powers of \(\mathfrak h_4\).
In particular its actual trace is
\[
J_k(g)=f_g h_{k-1}(g).
\tag{TP.6}
\]
This is independent of the line-bundle degree: the stabilizer fixes the
canonical vector \(\ell_i\), so the affine linear function equal to
one there gives an invariant trivialization of every twist. The finite
evaluation sequence thus has Euler character
\(h_N(g)-J_k(g)\) in each nonnegative degree \(N\). The sole negative
degree needed is \(-1\), which occurs with \(k=0\); both terms are
zero there. Combining this sequence with (TP.5) gives
\[
\boxed{\chi_{M_{a,k,t}}(g)=
h_a(g)h_{2k+t}(g)-h_{a-1}(g)h_{2k+t-1}(g)
-f_gh_{k-1}(g)\bigl(h_a(g)-h_{a-1}(g)\bigr).}
\tag{TP.7}
\]
Every subtraction is the Euler character of the explicit maps just
proved, and the left side is the degree-zero section representation.

The seven trace functions have the following closed forms for \(N\ge0\),
recorded as table (TP.8).
These follow by expanding
\((1-z)/\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)\).

| cycle type | \(f_g\) | \(h_N(g)\) |
|---|---:|---|
| \(1^5\) | 5 | \(\binom{N+3}{3}\) |
| \(2\,1^3\) | 3 | \((\lfloor N/2\rfloor+1)(\lceil N/2\rceil+1)\) |
| \(2^2\,1\) | 1 | \(N/2+1\) for even \(N\), and zero for odd \(N\) |
| \(3\,1^2\) | 2 | \(\lfloor N/3\rfloor+1\) |
| \(3\,2\) | 0 | the periodic list \((1,-1,1,0,0,0)\) modulo six |
| \(4\,1\) | 1 | one for \(N\equiv0\pmod4\), and zero otherwise |
| \(5\) | 0 | the periodic list \((1,-1,0,0,0)\) modulo five |

For example the transposition series is
\((1-z)^{-2}(1-z^2)^{-1}\); summing its coefficient gives the product
in the table. The \((3,2)\) series is
\((1-z+z^2)/(1-z^6)\), giving its six values. The other expansions
are direct. The convention \(h_{-1}=0\) agrees with every relevant
shifted series \(z\sum_{N\ge0}h_Nz^N\).

## 3. Fixed constants and the exhaustive sign proof

Use the class sizes and irreducible character table in G-019 §2.
All seven characters are real. For residues \(0\le r,s,v<60\), define
the following fixed differences, separately for each class \(g\):
\[
\begin{aligned}
A_i^\delta(r;g)
 &=\sum_{u=0}^i(-1)^{i-u}\binom iu h_{r+60u-\delta}(g),\\
B_{j,l}^\delta(s,v;g)
 &=\sum_{u=0}^j\sum_{w=0}^l(-1)^{j+l-u-w}
       \binom ju\binom lw h_{2s+v+120u+60w-\delta}(g),\\
K_j(s;g)
 &=\sum_{u=0}^j(-1)^{j-u}\binom ju h_{s+60u-1}(g),
\qquad \delta=0,1.
\end{aligned}
\tag{TP.9}
\]
Here \(0\le i,j,l\le3\); every index is between \(-1\) and 717.
Let
\[
\mathcal D=\{(i,j,l)\in\mathbf Z_{\ge0}^3:
i\le3,\ j+l\le3,\ i+j+l\le5\}.
\tag{TP.10}
\]
It contains exactly 36 triples. The fixed constant for a label and tag is
\[
\boxed{c_{\nu,r,s,v,i,j,l}
=\frac1{120}\sum_g |g^{S_5}|\chi_\nu(g)
\left[A_i^0 B_{j,l}^0-A_i^1 B_{j,l}^1
-\mathbf1_{l=0}f_g(A_i^0-A_i^1)K_j\right].}
\tag{TP.11}
\]
Arguments in the brackets are those in (TP.9). This is an explicit
formula in a fixed number of integers of fixed size. In particular it
does not invoke the coefficient in (TP.1) to define a polytope constant.

Every constant (TP.11) is a nonnegative integer. The full exact check
was carried out twice independently over all seven labels, all
\(60^3\) residue triples and all \(4^3\) difference positions: this is
96,768,000 entries. The root computation obtains the traces by the
ordinary cycle-geometric-series recurrence; the independent archive
computation uses precisely the seven closed functions (TP.8) and
universal finite-difference matrices. Both use integer arithmetic and
check divisibility by 120 before division. Both agree on the complete
coefficient-stream hashes, every minimum and maximum, every zero order,
and every vanishing triple. Their complete scripts and receipts are
included in the package.

For auditability, the independent computation bounds every intermediate
signed integer in absolute value by 22,422,562,560,000, below \(2^{63}\),
before using its signed-64 arrays. The root code independently checks a
conservative Python-integer bound for each difference position. Thus
the array calculations implement exact integers, without modular or
floating-point substitution. The largest final constant is 1,021,264,200.

All 28 positions outside \(\mathcal D\) are identically zero. Within
\(\mathcal D\), all 35 positive-order coefficients are strictly
positive for every residue. Their minima, together with the complete
zero counts of the order-zero values, are:

| \(\nu\) | minimum positive-order constant | number of zero triples |
|---|---:|---:|
| \((5)\) | 418 | 5 |
| \((4,1)\) | 1487 | 2 |
| \((3,2)\) | 1735 | 3 |
| \((3,1,1)\) | 1978 | 7 |
| \((2,2,1)\) | 1575 | 10 |
| \((2,1,1,1)\) | 1167 | 21 |
| \((1^5)\) | 258 | 67 |

The order-zero values are nonnegative also by (TP.7) and the finite-group
projector: they are multiplicities in the specified section module.
The exact check supplies all signs of the higher differences, as well
as the stated finite support data. The files are
`five_point_three_parameter_certificate.py`,
`FIVE_POINT_THREE_PARAMETER_SUMMARY.json`,
`work/archive/check_three_parameter_analytic.py`, and
`work/archive/THREE_PARAMETER_ANALYTIC_RECEIPT.json`.

## 4. The polynomial identity in all degrees and the positive polytopes

For each class, the series for \(h_N(g)\) and \(h_{N-1}(g)\), indexed
by \(N\ge0\), have denominator dividing \((1-z^{60})^4\), with common
numerator degree at most 239. These fourteen exact identities follow
by substituting (TP.8); they were also checked independently by polynomial
division. The residue argument of (W.14) proves that each is a polynomial
of degree at most three in its quotient variable from the first residue
value, including every initial zero.

Write
\[
a=60p+r,\qquad k=60q+s,\qquad t=60u+v,
\qquad0\le r,s,v<60.
\]
Then \(2k+t=60(2q+u)+(2s+v)\). The fixed number \(2s+v\) may require
an additional residue carry of zero, one, or two; all such carries are
nonnegative. Hence both \(h_{2k+t}\) and \(h_{2k+t-1}\) are polynomials
of total degree at most three in \(q,u\), for every \(q,u\ge0\).
Equation (TP.7) is consequently polynomial of degree at most three in
\(p\) and total degree at most three in \(q,u\).

Its terms of degree three in both blocks vanish. At the identity its
dimension is
\[
\begin{aligned}
\dim M_{a,k,t}={}&
\binom{a+2}{2}\left[\binom{2k+t+3}{3}
                         -5\binom{k+2}{3}\right]\\
&+\binom{a+2}{3}\binom{2k+t+2}{2}.
\end{aligned}
\tag{TP.12}
\]
This follows by inserting the identity trace into (TP.7), and it has
total degree at most five. For every nonidentity class, (TP.8) shows
that each trace has degree at most two on a residue, so the products
have total degree at most four. Thus the \(p^3\)-terms of total
\((q,u)\)-degree three vanish in every class. These observations also
prove algebraically that exactly the possible difference positions
lie in \(\mathcal D\).

The multivariate Newton identity therefore gives, in every degree,
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{(i,j,l)\in\mathcal D}
c_{\nu,r,s,v,i,j,l}\binom pi\binom qj\binom ul.}
\tag{TP.13}
\]
Its coefficients are precisely the differences (TP.11). The exact
polynomial argument proves the identity outside the finite range used
to determine those constants.

For a uniform polytope description, take a tag
\((r,s,v,i,j,l)\), with constant \(c>0\), and variables
\(p,q,u,y,x_1,\ldots,x_i,z_1,\ldots,z_j,w_1,\ldots,w_l\).
The equations and bounds are
\[
\begin{gathered}
60p+r=a,\quad60q+s=k,\quad60u+v=t,\qquad p,q,u\ge0,\\
0\le y\le c-1,\\
1\le x_1<\cdots<x_i\le p,\qquad
1\le z_1<\cdots<z_j\le q,\qquad
1\le w_1<\cdots<w_l\le u.
\end{gathered}
\tag{TP.14}
\]
Empty lists impose no condition and contribute one choice. Strict
inequalities are replaced by integer differences at least one. The
equations fix the three quotient variables and every remaining variable
lies in a finite displayed interval. There are at most
\(4+i+j+l\le9\) variables. Its lattice points are in bijection with
the independent choice of \(y\) and the three ordered subsets, so its
count is the corresponding term of (TP.13). The disjoint tagged union
proves the positive formula. Only one residue triple can contribute.

The constants in (TP.11) use only indices at most 717 and the fixed
seven-character table; computing them is a constant-size arithmetic
operation. The binomial arguments in (TP.13) have binary length bounded
by the input length. Thus the evaluator performs a fixed number of
integer operations with polynomial bit cost, and does not loop to
\(a\), \(k\), or \(t\).

## 5. The complete exceptional support

Every triple with at least one coordinate at least 60 has positive
coefficient, since the corresponding first directional difference in
(TP.13) is strictly positive. In the residue cube the complete zeros
are described below. An entry \((a,k):T\) means precisely the triples
\((a,k,t)\) with \(t\in T\); every pair omitted has no zero values.

For \(\nu=(5)\):
\[
(0,0):\{1\},\qquad(0,1):\{0,1\},\qquad(1,0):\{0,1\}.
\]
For \(\nu=(4,1)\): \((0,0):\{0\}\), \((0,1):\{0\}\).
For \(\nu=(3,2)\): \((0,0):\{0,1\}\), \((1,0):\{0\}\).

For \(\nu=(3,1,1)\):
\[
(0,0):\{0,1,2\},\quad
(0,1),(0,2),(1,0),(2,0):\{0\}.
\]
For \(\nu=(2,2,1)\):
\[
(0,0):\{0,1,2,3\},\quad
(0,1),(1,0):\{0,1\},\quad(2,0),(3,0):\{0\}.
\]
For \(\nu=(2,1,1,1)\):
\[
\begin{array}{c|l}
(a,k)&T\\\hline
(0,0)&0,1,2,3,4,5\\
(0,1)&0,1,2,3\\
(0,2)&0,1\\
(1,0)&0,1,2\\
(1,1)&0\\
(2,0)&0,1\\
(3,0),(4,0),(5,0)&0
\end{array}
\]
For \(\nu=(1^5)\):
\[
\begin{array}{c|l}
(a,k)&T\\\hline
(0,0)&0,1,2,3,4,5,6,7,8,9,11\\
(0,1)&0,1,2,3,4,5,6,7,9\\
(0,2)&0,1,2,3,4,5,7\\
(0,3)&0,1,2,3,5\\
(0,4)&0,1,3\\
(0,5)&1\\
(1,0)&0,1,2,3,4,5\\
(1,1)&0,1,2,3\\
(1,2)&0,1\\
(2,0)&0,1,2,3\\
(2,1)&0,1\\
(3,0)&0,1,2\\
(3,1)&0\\
(4,0),(5,0)&0,1\\
(6,0),(7,0),(8,0),(9,0),(11,0)&0
\end{array}
\]
These are exactly the order-zero entries verified in the two independent
certificates. All other triples are positive. The parity rule (TP.2)
then gives the complete coefficient support for the original outer label.

## 6. Exact geometric and lambda-ring dictionary

The object (TP.3) is a Schur functor of the tautological locally free
quotient, tensored with an ordinary point-ideal power and a specified
line bundle. Its higher cohomology vanishes by the complete sequence
argument above. Its class is therefore the actual direct-image
representation, and the Euler-class formula is carried by (TP.5) and
the jet evaluation sequence. The relative exterior pairing and balanced
chart (TP.4) identify it with the stated Schur-operation multiplicity.

The frame-torsor transport, exact representation \(K_0\), and universal
lambda-ring operations have the verified locators SGA 3 I 4.5 and
4.7.2–4.7.3; SGA 6 V 4.2, 4.4, 4.8–4.9 and VI 3.3. The ideal,
coordinate evaluation and multiplication maps are the EGA I 9.5.1–9.5.3
constructions. Their Hilbert/Quot family interpretation is FGA Exposé221,
Theorems3.1–3.2, through the same explicit graded modules in the separate
dictionary. All these representation and cohomology conclusions are
proved in characteristic zero.


# Every two-row quotient in the nonnegative twist region

## G-021. A positive formula and complete support for five parameters

Let \(x,b,k,t,d\ge0\), put \(a=b+x\), and define
\[
\begin{aligned}
n&=d+b+x+k+t,\\
\lambda&=(d+3b+2x+3k+4t,\ d+b+x+2k+t,\\
&\hspace{36mm}d+b+x,\ d+x,\ d).
\end{aligned}
\tag{TR.1}
\]
Every coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the
positive formula (TR.15). It uses at most 122 active lattice polytopes,
each of dimension at most eleven, and fixed constants given by finite
differences of the seven elementary functions (TP.8). All constants
with positive difference order are strictly positive. The complete
zero set consists of the 155 explicitly recorded quadruples in §7,
after the sign twist (TR.3). This is a fixed description for the entire
family; the constants require no representation calculation at input
size. No claim of historical novelty is made.

## 1. The exact representation and bundle comparison

Retain the standard representation \(E=\mathfrak h_5\), the five
canonical points \(Z\subset\mathbf P(E)\), their ordinary ideal sheaf
\(\mathcal I\), and the tautological quotient \(Q\) of rank three.
Write \(c=2k+t\) and
\[
M_{x,b,k,t}=H^0\bigl(\mathbf P(E),
          \mathcal I^k(c)\otimes S_{(b+x,b)}Q\bigr).
\tag{TR.2}
\]
The G-015 normal-coordinate map and inverse balanced homogenization
give the actual equivariant isomorphism
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
 \simeq\operatorname{sgn}^{d+b+x}\otimes M_{x,b,k,t}.
\tag{TR.3}
\]
Here is the relative-flag dictionary in full. The four-row weight is
\((d+a+c,d+a,d+x,d)\). After removing its determinant power \(d\),
the quotient weight is \((a,x,0)\) on \(Q^*\), and the first-line
twist is \(a+c\). Exterior-column contraction gives the perfect
pairing
\[
S_{(a,x)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,b)}Q,
\qquad b=a-x.
\]
The identity \(\det Q^*=\det E^*\otimes\mathcal O(-1)\) changes
the twist to \(c\) and supplies the constant sign power \(a\).
Together with the removed determinant this is (TR.3). The point order
is exactly \(\lambda_2-n=k\). G-015 proves, through its displayed
normal ratios and inverse \(f\mapsto u^{-k}f(v(X))\), that extension
is exactly membership in \(\mathcal I^k\). Thus all maps used in
(TR.3) are specified bundle or polynomial maps.

For the outer character define
\[
\nu=\mu\quad(d+b+x\text{ even}),\qquad
\nu=\mu'\quad(d+b+x\text{ odd}).
\tag{TR.4}
\]
The required plethysm coefficient is \([\nu:M_{x,b,k,t}]\).

## 2. The complete two-row Schur complex

Put \(L=\mathcal O(-1)\subset E\). For \(N=a+b\), take the
tensor power of the complex \([L\to E]\), with \(L\) in degree
minus one. The permutation of tensor positions uses Koszul signs.
For line positions \(J\), its differential replaces position
\(j\in J\) by the tautological inclusion with sign
\((-1)^{|\{i\in J:i<j\}|}\). The two orders of replacing a pair
cancel, so this is a complex. Apply the primitive Young projector
\(e_T=c_Tr_T/h_{a,b}\) for the row-filled tableau of shape \((a,b)\).
The signed action commutes with the differential.

Its degree-minus-\(j\) term is obtained from
\(\operatorname{Ind}_{S_{N-j}\times S_j}^{S_N}
(E^{\otimes(N-j)}\otimes L^j\otimes\operatorname{sgn}_{S_j})\).
Exterior Pieri gives exactly the shapes obtained by deleting a vertical
\(j\)-strip. This identity follows directly by multiplying a Schur
alternant by \(e_j\): increase distinct exponents by one, discard
collisions, then divide by the Vandermonde. Multiplicities are one.
There are only two rows, so the resulting augmented complex is
\[
\begin{aligned}
0\longrightarrow& L^2 S_{(a-1,b-1)}E\\
\longrightarrow& L\bigl(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\bigr)\\
\longrightarrow& S_{(a,b)}E\longrightarrow S_{(a,b)}Q\longrightarrow0.
\end{aligned}
\tag{TR.5}
\]
Only valid partition terms are retained. The detailed rational
polytabloid prescription in the appendix *The exact two-row quotient
complex*, (S.1)–(S.5), specifies each identification: solve the
adjacent-transposition intertwiner equations, choose the first nonzero
solution with first nonzero coordinate one, use the explicitly summed
Frobenius-reciprocity map, and evaluate at \(e_T\). Conjugating the
specified tensor differential by these rational maps fixes the maps
in (TR.5), including their scalars. They commute with frame change.

Locally split \(E=L\oplus Q\). The tensor complex contracts onto
\(Q^{\otimes N}\); average the contraction over \(S_N\) and
restrict to the idempotent image. This proves locally split exactness
of (TR.5). Its homotopy remains an identity after tensoring with
\(\mathcal I^k(c)\), so that tensoring preserves exactness.

For \(a=b>0\) the first middle summand is absent; for \(b=0<a\)
(TR.5) is the symmetric-quotient sequence; for \(a=b=0\) the
augmentation is the identity. At \(a=b=1\), its two maps are
\(l^2\mapsto l\otimes l\) and \(l\otimes e\mapsto l\wedge e\).
These include every boundary of (TR.1).

A-029 gives \(H^{q>0}(\mathcal I^k(c))=0\) for \(k\ge2\) and
\(c\ge2k\). Its precise known input is Kustin–Polini–Ulrich,
formula (6.1.4), p.1509, Lemma 6.3 and Corollary 6.4, p.1510,
with the local hypotheses verified there. For \(k=1\), degree-two
point evaluation and multiplication prove the same assertion; for
\(k=0\) it is scalar projective cohomology. The latter source is
Stacks Project, Lemma 30.8.1, tag 01XS. For the other two terms,
\(H^2=H^3=0\): the point quotient has finite support and their twists
are at least \(-2\). In the cohomology spectral sequence of (TR.5),
the only remaining \(H^1\)'s have total degrees zero or minus one.
There is no term of positive total degree. Exactness therefore proves
\[
H^{q>0}(\mathcal I^k(c)\otimes S_{(a,b)}Q)=0.
\tag{TR.6}
\]
The exceptional scalar groups at \(k=1,c=2\) are included in this
argument. No asserted surjectivity between those groups is needed.

## 3. Seven exact character polynomials

Write \(h_j(g)=\operatorname{tr}(g\mid\operatorname{Sym}^jE)\),
with \(h_{-1}=h_{-2}=0\), and let \(f_g\) be the fixed-letter
count. The exact affine-jet morphism of G-018 and A-033 gives
\(J_k(g)=f_gh_{k-1}(g)\). The line-bundle trivialization is fixed by
the stabilizer of the point, so this jet trace is independent of the
twist. In every twist of (TR.5), the scalar Euler trace is
\(h_j-J_k\). Define
\[
\begin{aligned}
s_{A,B}(g)&=h_A(g)h_B(g)-h_{A+1}(g)h_{B-1}(g),\\
S_0&=s_{a,b},\qquad
S_1=s_{a-1,b}+s_{a,b-1},\qquad Z=s_{a-1,b-1},\\
R&=S_0-S_1+Z,\qquad T=S_1-2Z.
\end{aligned}
\tag{TR.7}
\]
These Jacobi–Trudi formulas automatically give zero for every omitted
boundary term. The actual character of (TR.2), by (TR.5) and (TR.6), is
\[
\begin{aligned}
P_g(x,b,k,t)
&=S_0(h_c-J_k)-S_1(h_{c-1}-J_k)+Z(h_{c-2}-J_k)\\
&=R(h_c-J_k)+T(h_c-h_{c-1})
                  +Z(h_c-2h_{c-1}+h_{c-2}).
\end{aligned}
\tag{TR.8}
\]
The functions \(h_j\), class sizes and characters are exactly (TP.8)
and the seven-row character table in G-019. Their rational generating
functions are \((1-z)/\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)\).
Every formula in (TP.8), extended by its residue polynomial, also gives
zero at \(-1,-2\). Thus (TR.8) is polynomial on each of the
\(60^4\) residue classes, including their initial points.

For the identity class, direct expansion of (TR.7) gives
\[
R=\frac{(b+1)(x+1)(b+x+2)}2,\quad
T=R\frac{2b+x}{3},\quad Z=R\frac{b(b+x+1)}6.
\]
Consequently
\[
P_1=\frac{(b+1)(x+1)(b+x+2)}{12}
\bigl((c+1)(b+c+2)(b+x+c+3)-5k(k+1)(k+2)\bigr).
\tag{TR.9}
\]
With \(c=2k+t\), its 122 nonzero ordinary coefficients are positive.
Their exponent set is the following downset \(D\), with the first
pair denoting the exponents of \(x,b\):
\[
\begin{array}{c|c|r}
\text{first pair}&\text{last pair }(j,l)&\text{count}\\\hline
(0,0),(1,0),(0,1),(2,0),(0,2),(1,1),(2,1),(1,2)&j+l\le3&80\\
(3,0),(0,3),(3,1),(2,2),(1,3)&j+l\le2&30\\
(0,4),(1,4),(2,3),(3,2)&j+l\le1&12
\end{array}
\tag{TR.10}
\]
Nonnegative integer exponents are understood. The largest total
exponent is six. Expanding the displayed factors in (TR.9) proves
(TR.10); the certificate records all 122 rational coefficients.

## 4. Coefficientwise proof that every positive difference is positive

For a multiindex \(\alpha\), let \(\Delta^\alpha\) mean forward
difference of step 60 in the four variables \((x,b,k,t)\). For a
monomial \(X^e\), the exact rule in variable \(i\) is
\[
\Delta_i X^e=\sum_{q=0}^{e_i-1}
\binom{e_i}{q}60^{e_i-q}X^{e-(e_i-q)e_i^{\rm unit}}.
\tag{TR.11}
\]
All its coefficients are positive. In particular every
\(\Delta^\alpha P_1\), \(\alpha\in D\), has positive constant
coefficient, and every difference outside \(D\) vanishes.

Here is a small exact coefficient certificate for all the other
classes. For a residue phase \(p\), substitute in (TR.7)–(TR.8)
\[
h_N(2\,1^3)=\frac{N^2+4N+4-(N\bmod2)}4,\quad
h_N(2^2\,1)=\begin{cases}(N+2)/2,&N\text{ even},\\0,&N\text{ odd},\end{cases}
\]
\[
h_N(3\,1^2)=\frac{N+3-(N\bmod3)}3.
\tag{TR.12}
\]
The phases are the 16 four-tuples modulo two in each of the first two
cases and the 81 four-tuples modulo three in the last case. Expanding
(TR.8) gives total degrees at most three, two and one, respectively.
For the remaining three conjugacy classes every trace in (TP.8) is
periodic, so every positive step-60 difference vanishes.

For \(1\le|\alpha|\le3\), and each ordinary monomial exponent
\(\beta\), let \(B_{g,\alpha,\beta}\) be the maximum absolute
coefficient of \(X^\beta\) in \(\Delta^\alpha P_g\) over those
16, 16 or 81 phases. Define the explicit rational polynomial
\[
D_\alpha=\Delta^\alpha P_1-
\sum_\beta(10B_{2,\alpha,\beta}+15B_{22,\alpha,\beta}
                         +20B_{3,\alpha,\beta})X^\beta.
\tag{TR.13}
\]
Every coefficient is nonnegative, and its constant coefficient is
strictly positive. The following complete table records, for all 34
orders, the smallest nonzero coefficient margin and the constant
margin. It is checked by expanding only the explicitly specified
rational polynomials (TR.9),(TR.12), using (TR.11). The delivered
`two_row_quotient_polynomial_bound.py` performs exactly these finite
rational operations; its JSON records every identity coefficient,
all downset exponents, and every comparison. A separate agent's
independent reconstruction is recorded in the verification appendix.

| order in x,b,k,t | least coefficient margin | constant margin |
|---|---:|---:|
| 0,0,0,1 | 5 | 29260 |
| 0,0,0,2 | 600 | 205200 |
| 0,0,0,3 | 108000 | 216000 |
| 0,0,1,0 | 10 | 103320 |
| 0,0,1,1 | 1200 | 626400 |
| 0,0,1,2 | 216000 | 432000 |
| 0,0,2,0 | 2400 | 640800 |
| 0,0,2,1 | 432000 | 864000 |
| 0,0,3,0 | 324000 | 648000 |
| 0,1,0,0 | 5 | 1206640 |
| 0,1,0,1 | 600 | 286641600 |
| 0,1,0,2 | 36000 | 693612000 |
| 0,1,1,0 | 1200 | 910333200 |
| 0,1,1,1 | 72000 | 1795464000 |
| 0,1,2,0 | 144000 | 2333808000 |
| 0,2,0,0 | 600 | 15952800 |
| 0,2,0,1 | 36000 | 1905804000 |
| 0,2,1,0 | 72000 | 5515488000 |
| 0,3,0,0 | 216000 | 39744000 |
| 1,0,0,0 | 5 | 29260 |
| 1,0,0,1 | 300 | 145951200 |
| 1,0,0,2 | 72000 | 557460000 |
| 1,0,1,0 | 600 | 492800400 |
| 1,0,1,1 | 144000 | 1523160000 |
| 1,0,2,0 | 288000 | 1789200000 |
| 1,1,0,0 | 600 | 286641600 |
| 1,1,0,1 | 72000 | 50797548000 |
| 1,1,1,0 | 144000 | 157825656000 |
| 1,2,0,0 | 36000 | 1905804000 |
| 2,0,0,0 | 600 | 205200 |
| 2,0,0,1 | 72000 | 557460000 |
| 2,0,1,0 | 144000 | 2028240000 |
| 2,1,0,0 | 36000 | 693612000 |
| 3,0,0,0 | 108000 | 216000 |

The character bound \(|\chi_\nu(g)|\le\dim\nu\) follows by averaging
an inner product and diagonalizing the finite-order unitary operator.
For every nonnegative residue vector \(r\), the triangle inequality
applied coefficientwise to (TR.13) therefore proves
\[
\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
                         (\Delta^\alpha P_g)(r)
\ \ge\ \frac{\dim\nu}{120}D_\alpha(r)>0
\quad(1\le|\alpha|\le3).
\tag{TR.14}
\]
For \(|\alpha|\ge4\) every nonidentity term is zero. Positivity
then follows directly from (TR.9)–(TR.11) for \(\alpha\in D\).
Outside \(D\) all terms vanish. This proves the sign assertion for
all residues without a computation over their \(60^4\) choices.
The differences are integers because they are differences of the
actual character multiplicities in (TR.3),(TR.8).

## 5. The positive Newton formula and exact lattice maps

For \(r\in\{0,\ldots,59\}^4\) and \(\alpha\in D\), set
\[
C_{\nu,\alpha}(r)=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
                                    (\Delta^\alpha P_g)(r).
\]
All these constants are nonnegative integers. The zeroth one is an
actual multiplicity by (TR.3); every other one is strictly positive
by (TR.14). Write \((x,b,k,t)=r+60q\). The finite Newton identity
in four variables gives exactly
\[
\boxed{p_{\mu,(n)}^\lambda
 =\sum_{\alpha\in D}C_{\nu,\alpha}(r)
                  \prod_{i=1}^4\binom{q_i}{\alpha_i}.}
\tag{TR.15}
\]
One proof of this interpolation identity is to apply successively
\(f(q)=\sum_j\Delta^jf(0)\binom qj\) in each variable. The latter
identity follows by induction from
\(\Delta\binom qj=\binom q{j-1}\). Degrees and (TR.10) make every
omitted coefficient zero, so the expansion terminates exactly as
stated.

For each fixed residue and exponent, introduce integer variables
\(q_1,\ldots,q_4,y\), and, for each \(i\), a chain
\(z_{i,1},\ldots,z_{i,\alpha_i}\). The polytope is specified by
\[
60q_i=X_i-r_i,\quad q_i\ge0,\quad
0\le y<C_{\nu,\alpha}(r),\quad
0\le z_{i,1}<\cdots<z_{i,\alpha_i}<q_i,
\tag{TR.16}
\]
with empty chains omitted. Convert strict inequalities to differences
at most minus one. Every coordinate and inequality has now been
specified. The bijection sends a point to its \(y\)-choice and its
four subsets of \(\{0,\ldots,q_i-1\}\); its inverse writes each
subset in increasing order. Its number of points is precisely the
summand in (TR.15). Since \(|\alpha|\le6\), at most eleven integer
variables occur. There are 122 active tags, or
\(60^4\cdot122=1,581,120,000\) tags in the uniform description
before selecting the unique residue. This large fixed number is
stated explicitly; the evaluator selects the active residue first.

All constants are given by fixed finite sums with input-independent
indices. The largest possible trace index in a conservative rectangular
bound is 539. Thus evaluation uses a fixed number of integer arithmetic
operations, followed by binomial coefficients of order at most four.
With elementary integer multiplication its bit complexity is
\(O(\log^2(2+x+b+k+t+d))\). The polytope right-hand sides have the
same logarithmic bit size plus fixed constants. The finite-group
projectors and Young functors here are over \(\mathbf Q\); their
integral models and required denominators are carried by the actual
maps, as explained in the geometric dictionary.

## 6. Independent overlap and finite computations

The residue-zero-order check streams all
\(7\cdot60^4=90,720,000\) multiplicities. Its factors are first
computed with arbitrary-precision integers. The bound on every weighted
class partial sum is 2,493,689,811,648, established before conversion
to signed 64-bit integers. Every value is integral and nonnegative.
The delivered `TWO_ROW_QUOTIENT_SUPPORT.json` records exact zero
quadruples, extrema and per-label SHA256 hashes; the stream order and
integer byte order are specified. This is a computation certificate,
not a proof-assistant verification.

The rectangular agent independently computed all 882 actual plethysm
coefficients with \(x+b+k+t+d\le4\), using the Murnaghan–Nakayama
rule in the full symmetric group, and obtained agreement for every
outer label. The theta agent independently computed all 120,960,000
Newton constants on the slice \(t=0\), using three separable Euler
products and cycle recurrences. All agree with the nonnegativity
statement; that slice has 55 active orders and 70 total zeros.
These checks corroborate the exact representation morphisms and sign
in (TR.3), while §§2–5 prove the whole parameter family.

## 7. The complete exceptional support

Every first-order constant is strictly positive. Thus a positive
quotient \(q_i\) makes (TR.15) positive, using its order-one term.
Every zero therefore lies inside the residue cube. Its complete
155-element list follows, grouped by effective outer label \(\nu\).
The four entries of each tuple are \((x,b,k,t)\). The parameter
\(d\) affects only the sign twist (TR.4).

### Effective label 5 — 19 zeros

`(0,0,0,1)` `(0,0,1,0)` `(0,0,1,1)` `(0,1,0,0)` `(0,1,0,1)`

`(0,1,0,2)` `(0,1,0,3)` `(0,1,0,4)` `(0,1,1,0)` `(0,1,1,1)`

`(0,1,1,2)` `(0,1,2,0)` `(0,3,0,0)` `(0,5,0,0)` `(1,0,0,0)`

`(1,0,0,1)` `(1,1,0,0)` `(1,1,0,1)` `(2,1,0,0)`


### Effective label 41 — 4 zeros

`(0,0,0,0)` `(0,0,1,0)` `(0,1,0,0)` `(0,1,0,1)`


### Effective label 32 — 4 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,1,0,0)` `(1,0,0,0)`


### Effective label 311 — 8 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,1,0)` `(0,0,2,0)`

`(0,2,0,0)` `(1,0,0,0)` `(2,0,0,0)`


### Effective label 221 — 11 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,1,0)`

`(0,0,1,1)` `(0,1,0,0)` `(1,0,0,0)` `(1,0,0,1)` `(2,0,0,0)`

`(3,0,0,0)`


### Effective label 2111 — 24 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,0,4)`

`(0,0,0,5)` `(0,0,1,0)` `(0,0,1,1)` `(0,0,1,2)` `(0,0,1,3)`

`(0,0,2,0)` `(0,0,2,1)` `(0,1,0,0)` `(0,2,0,0)` `(1,0,0,0)`

`(1,0,0,1)` `(1,0,0,2)` `(1,0,1,0)` `(1,1,0,0)` `(2,0,0,0)`

`(2,0,0,1)` `(3,0,0,0)` `(4,0,0,0)` `(5,0,0,0)`


### Effective label 11111 — 85 zeros

`(0,0,0,0)` `(0,0,0,1)` `(0,0,0,2)` `(0,0,0,3)` `(0,0,0,4)`

`(0,0,0,5)` `(0,0,0,6)` `(0,0,0,7)` `(0,0,0,8)` `(0,0,0,9)`

`(0,0,0,11)` `(0,0,1,0)` `(0,0,1,1)` `(0,0,1,2)` `(0,0,1,3)`

`(0,0,1,4)` `(0,0,1,5)` `(0,0,1,6)` `(0,0,1,7)` `(0,0,1,9)`

`(0,0,2,0)` `(0,0,2,1)` `(0,0,2,2)` `(0,0,2,3)` `(0,0,2,4)`

`(0,0,2,5)` `(0,0,2,7)` `(0,0,3,0)` `(0,0,3,1)` `(0,0,3,2)`

`(0,0,3,3)` `(0,0,3,5)` `(0,0,4,0)` `(0,0,4,1)` `(0,0,4,3)`

`(0,0,5,1)` `(0,1,0,0)` `(0,1,0,1)` `(0,1,0,2)` `(0,1,1,0)`

`(0,1,2,0)` `(0,2,0,0)` `(0,2,0,1)` `(0,2,0,3)` `(0,2,1,1)`

`(0,3,0,0)` `(0,5,0,0)` `(1,0,0,0)` `(1,0,0,1)` `(1,0,0,2)`

`(1,0,0,3)` `(1,0,0,4)` `(1,0,0,5)` `(1,0,1,0)` `(1,0,1,1)`

`(1,0,1,2)` `(1,0,1,3)` `(1,0,2,0)` `(1,0,2,1)` `(1,1,0,0)`

`(1,1,0,1)` `(1,2,0,0)` `(2,0,0,0)` `(2,0,0,1)` `(2,0,0,2)`

`(2,0,0,3)` `(2,0,1,0)` `(2,0,1,1)` `(2,1,0,0)` `(3,0,0,0)`

`(3,0,0,1)` `(3,0,0,2)` `(3,0,1,0)` `(3,1,0,0)` `(3,2,0,0)`

`(4,0,0,0)` `(4,0,0,1)` `(4,1,0,0)` `(5,0,0,0)` `(5,0,0,1)`

`(6,0,0,0)` `(7,0,0,0)` `(8,0,0,0)` `(9,0,0,0)` `(11,0,0,0)`


## 8. Exact coverage of both outside regions

The formula evaluates every partition \(\lambda\vdash5n\) with at
most five parts satisfying
\[
\lambda_2+\lambda_3\le2n
\quad\text{or}\quad
\lambda_3+\lambda_4\ge2n.
\tag{TR.17}
\]
The following explicit maps prove this larger formulation.

For the first inequality, set
\[
\begin{gathered}
d=\lambda_5,\quad x=\lambda_4-\lambda_5,\quad
b=\lambda_3-\lambda_4,\quad k=\max(0,\lambda_2-n),\\
t=\lambda_2-\lambda_3-2k,\qquad e=\max(0,n-\lambda_2).
\end{gathered}
\tag{TR.18}
\]
All six integers are nonnegative, and \(ke=0\). The base partition
in (TR.1) has the same last four parts and first part
\(\lambda_1-5e\); its inner degree is \(n-e\). At \(e=0\),
(TR.1) applies directly. At \(e>0\), \(k=0\), and G-015's two
balanced-chart expressions differ by multiplication by
\(u^e=(\prod_{i=1}^5X_{1i})^e\). Their coefficient space is the
same full flag-section space because neither chart imposes a positive
point order. The inverse divides by \(u^e\) on this image; the
normal-order argument proves polynomial extension in both descriptions.
The polynomial \(u\) is fixed by slot permutations. Thus this is an
actual \(S_5\)-equivariant isomorphism of the two balanced spaces,
proving equality of every outer coefficient.

For the second inequality, set \(H=\lambda_1\),
\(n^c=H-n\), and
\(\lambda^c=(H-\lambda_5,\ldots,H-\lambda_1)\). These are
nonnegative partition data, and
\(\lambda^c_2+\lambda^c_3\le2n^c\). Complementary-column exterior
multiplication gives the perfect equivariant pairing
\[
S_\lambda\mathbf Q^5\otimes S_{\lambda^c}\mathbf Q^5
 \longrightarrow(\det\mathbf Q^5)^H.
\tag{TR.19}
\]
It pairs the weight \((n^5)\) perfectly with \(((H-n)^5)\).
Permutation matrices act on its target by \(\operatorname{sgn}^H\).
All rational irreducible \(S_5\) modules are self-dual, as is also
seen from their real characters. Thus the outer coefficient at
\((\lambda,n,\mu)\) equals that at
\((\lambda^c,n^c,\mu)\) for even \(H\), or at
\((\lambda^c,n^c,\mu')\) for odd \(H\). Applying (TR.18) to the
complement proves the second region through this exact pairing.

The remaining direct outer-five evaluation gate after G-021 is
therefore the strictly smaller region
\(\lambda_2+\lambda_3>2n>\lambda_3+\lambda_4\). In the first
chart its ideal-twisted two-row quotient has \(c<2k\). The general
terminating positive construction G-010 already applies there; the
remaining task is to replace that preprocessing by an evaluated small
formula such as (TR.15).


# Uniform nonvanishing on staircase families

## G-022. Every outer Schur label in an explicit all-rank family

Let \(m\ge3\), let \(r,d\ge0\) be integers with \(r(m-1)\) even,
and put
\[
n=d+\frac{r(m-1)}2,\qquad
\lambda=(d+r(m-1),d+r(m-2),\ldots,d+r,d).
\tag{ST.1}
\]
Define \(D=(m-1)(m-2)/2\). The following explicit bound proves
nonvanishing for every outer partition \(\mu\vdash m\):
\[
r\ge2(m-1),\qquad
r^{m-2}>(m!-1)2^{(m-2)^2}(m-2)^D.
\tag{ST.2}
\]
In particular the simpler unconditional family \(r\ge(2m)^m\), with
the displayed parity requirement, has
\[
\boxed{p_{\mu,(n)}^\lambda>0\quad\text{for every }\mu\vdash m.}
\tag{ST.3}
\]
The proof below gives actual finite-group traces and an explicit
lower bound for each multiplicity. No historical priority is asserted.

## 1. The actual balanced trace from the Weyl determinant

First set \(d=0\), and write \(\delta=(m-1,m-2,\ldots,0)\).
The alternating-determinant formula for a Schur character gives the
polynomial identity
\[
s_{r\delta}(X_1,\ldots,X_m)
=\frac{\Delta(X_1^{r+1},\ldots,X_m^{r+1})}{\Delta(X_1,\ldots,X_m)}
=\prod_{i<j}\sum_{u=0}^{r}X_i^{r-u}X_j^u.
\tag{ST.4}
\]
Here both determinants use descending powers, so
\(\Delta(X)=\prod_{i<j}(X_i-X_j)\). The formula follows by
substituting \(r\delta_i+m-i=(r+1)(m-i)\) into that determinant.
Every factor division on the right is the finite geometric-series
identity; hence (ST.4) holds as a polynomial including repeated
variables.

Let \(g\in S_m\) have cycle lengths \(\ell_1,\ldots,\ell_c\).
The eigenvalues of \(\operatorname{diag}(t_1,\ldots,t_m)g\) on a
cycle are \(z_i\zeta_{\ell_i}^j\), where
\(z_i^{\ell_i}=T_i=\prod_{a\text{ in cycle }i}t_a\).
In the trace on \(S_{r\delta}\mathbf Q^m\), taking the coefficient
of \(\prod_a t_a^{r(m-1)/2}\) gives the trace on its balanced weight
space. Indeed the permutation sends each torus weight space to its
permuted weight; only fixed weights contribute to the trace, and this
coefficient selects precisely the specified balanced weight. Thus
\[
\operatorname{tr}(g\mid B_r)
=[T_1^{r(m-1)/2}\cdots T_c^{r(m-1)/2}]
       s_{r\delta}(z_i\zeta_{\ell_i}^j),
\tag{ST.5}
\]
where \(B_r=(S_{r\delta}\mathbf Q^m)_{((r(m-1)/2)^m)}\).
This is the exact normalizer representation of T-003.

A cycle with \(\gcd(r+1,\ell_i)>1\) has two equal powered
eigenvalues in the numerator of (ST.4), while the denominator is
nonzero over the field of independent cycle parameters. Its entire
trace polynomial is therefore zero.

For the other cycles, multiplication by \(r+1\) permutes their
residues. Let \(\kappa\in\{1,-1\}\) be the product of the signs
of these actual residue permutations. The within-cycle Vandermonde
ratio is
\(\kappa_i T_i^{r(\ell_i-1)/2}\). Its exponent is an integer:
for even \(\ell_i\), coprimality forces \(r\) even.
For two cycles, put \(g_{ij}=\gcd(\ell_i,\ell_j)\). Their cross
Vandermonde is
\[
(-1)^{\ell_i+g_{ij}}
\bigl(T_i^{\ell_j/g_{ij}}-T_j^{\ell_i/g_{ij}}\bigr)^{g_{ij}}.
\]
This follows by taking the product of
\(X^{\ell_j}-T_j\) over the \(\ell_i\) roots of
\(X^{\ell_i}-T_i\); the distinct roots occur \(g_{ij}\) times.
The same sign occurs in the numerator and cancels. Consequently the
actual trace in (ST.5) is \(\kappa\) times the coefficient in the
following polynomial with nonnegative coefficients:
\[
\prod_iT_i^{r(\ell_i-1)/2}
\prod_{i<j}
\left(\sum_{u=0}^r
T_i^{(r-u)\ell_j/g_{ij}}T_j^{u\ell_i/g_{ij}}
\right)^{g_{ij}}.
\tag{ST.6}
\]
All root choices have disappeared. This proves an exact signed lattice
trace using the literal cycle action, rather than an identification
based only on ordinary torus characters.

## 2. An upper bound for every nonidentity trace

Interpret the \(g_{ij}\) powers in (ST.6) as parallel edges, each
with an integer variable \(0\le u_e\le r\). The coefficient
conditions are linear equations. Their matrix is the weighted incidence
matrix with column
\(-\ell_j/g_{ij}\) at vertex \(i\) and
\(\ell_i/g_{ij}\) at vertex \(j\). Multiplying row \(i\) by
\(\ell_i\) changes this column into
\((\ell_i\ell_j/g_{ij})(-e_i+e_j)\). Thus the rank is \(c-1\)
for \(c\ge2\). Fix a spanning tree. Once all other edge variables
are specified, successive removal of tree leaves determines every tree
variable uniquely over \(\mathbf Q\). An admissible integer solution
is therefore determined by
\[
D_g=\sum_{i<j}g_{ij}-c+1
\]
variables, each with at most \(r+1\) choices. For \(c=1\) the
trace has absolute value at most one and set \(D_g=0\). We have proved
\[
|\operatorname{tr}(g\mid B_r)|\le(r+1)^{D_g}.
\tag{ST.7}
\]

For nonidentity \(g\), write \(s=m-c\ge1\). The elementary
inequality \(\gcd(a,b)\le1+(a-1)(b-1)\) holds for all positive
integers: at an argument one it is equality; otherwise its right side
is at least \(\min(a,b)\). For \(c\ge2\) it gives
\[
D_g\le\binom{c-1}{2}+\binom{s}{2}
\le\binom{m-2}{2}=D-(m-2).
\tag{ST.8}
\]
For the first inequality, expand the pair sum of \((\ell_i-1)\)
and use \(\sum(\ell_i-1)^2\ge s\). The difference in the second
inequality is exactly \((c-2)(s-1)\ge0\). At \(c=1\), (ST.8)
is immediate for \(m\ge3\). This proves the needed degree saving
for every nonidentity class, with no classification of its cycles.

## 3. An explicit large box inside the identity count

At the identity, (ST.4) counts integer assignments to the edges of
\(K_m\), each in \([0,r]\), such that the exponent at each vertex
is \(r(m-1)/2\). There are \(D\) independent edge variables after
the \(m-1\) independent balance equations.

Construct an integral central assignment. For even \(r\), put
\(r/2\) on every oriented edge. For odd \(r\), the parity assumption
forces \(m\) odd. Take the cyclic regular tournament on
\(\mathbf Z/m\): the arrows from \(i\) go to
\(i+1,\ldots,i+(m-1)/2\). Put \(\lfloor r/2\rfloor\) plus the
corresponding zero-or-one orientation contribution on each edge.
Every vertex then has the required exponent, and every edge is at
least \(\lfloor r/2\rfloor\) from one endpoint and at least that
far from the other.

Set
\[
q=\left\lfloor\frac{\lfloor r/2\rfloor}{m-2}\right\rfloor.
\]
Choose each edge among vertices \(2,\ldots,m\) independently within
\([-q,q]\) of its central value. There are exactly \(D\) such edges.
For each vertex \(i\ge2\), change the edge from vertex one by the
negative of its resulting imbalance. Its absolute change is at most
\((m-2)q\le\lfloor r/2\rfloor\), so it stays in \([0,r]\).
The remaining balance equation at vertex one follows because the total
exponent is unchanged. Different choices of the free edges give
different lattice assignments. Thus
\[
\dim B_r\ge(2q+1)^D
\ge\left(\frac{r}{2(m-2)}\right)^D
\qquad(r\ge2(m-1)).
\tag{ST.9}
\]
For the last bound,
\(2q+1\ge(r-m+1)/(m-2)\ge r/(2(m-2))\), using the elementary
floor inequalities. This proves the stated lower bound by an explicit
injective map of integer boxes into the balanced edge assignments.

## 4. Multiplicity, the explicit threshold, and the canonical image

For each irreducible character \(\chi_\mu\) of dimension \(f_\mu\),
averaging a positive Hermitian form makes every group element unitary,
so \(|\chi_\mu(g)|\le f_\mu\). Taking the actual character
projector and using (ST.7)–(ST.9) gives
\[
[\mu:B_r]\ge\frac{f_\mu}{m!}
\left[
\left(\frac{r}{2(m-2)}\right)^D
-(m!-1)(r+1)^{D-m+2}
\right].
\tag{ST.10}
\]
Under (ST.2) the right side is positive: use \(r+1\le2r\) and
\(2D-m+2=(m-2)^2\). Since the left side is an integer, it is at
least one. This proves the first assertion.

For \(m=3\), the power inequality in (ST.2) is \(r>10\), so
\(r\ge6^3\) suffices. For \(m\ge4\), the bound \(r\ge(2m)^m\)
gives
\[
r^{m-2}\ge2^{m(m-2)}m^{m(m-2)}
>(m!-1)2^{(m-2)^2}(m-2)^D.
\]
Indeed \(m!<m^m\), \(m(m-2)-(m-2)^2=2(m-2)>0\), and
\(m(m-2)-m-D=(m^2-3m-2)/2\ge1\). This proves (ST.3).

Multiplication by the actual determinant section identifies
\(S_{d\mathbf1+r\delta}\) with \(\det^d\otimes S_{r\delta}\).
It shifts the balanced content by \(d\) in each coordinate and the
permutation character by \(\operatorname{sgn}^d\). Thus it permutes
outer labels by transpose and proves the same assertion for every
\(d\ge0\), as stated in (ST.1).

For the symmetric outer label, these are also nonzero components of
the actual canonical image
\(h_{n,m}:\operatorname{Sym}^n\operatorname{Sym}^m V\to
\operatorname{Sym}^m\operatorname{Sym}^n V\) in every dimension at
least the number of positive parts of \(\lambda\). In the simpler
family \(r\ge(2m)^m\), its inner degree satisfies
\(n\ge(m-1)^2\). Sra, *The q-Foulkes problem III*, Theorem1.3,
proves surjectivity of this exact grid map in that range. Applying its
surjection to the positive target multiplicity just proved gives the
image multiplicity, with its lower bound (ST.10) after the determinant
twist. This uses the specified map and its cited full-range theorem.

## 5. Exact geometric and lambda-ring transport

The balanced module in (ST.5) is the torus weight subsheaf of the Schur
operation on the rank-\(m\) standard bundle. Its finite normalizer
projector is the same projector constructed through the compact dual
pair in T-001–T-003. Formula (ST.4) is evaluated after the actual
endomorphism \(\operatorname{diag}(t)g\); the cycle coefficient map
therefore computes that projector's trace. The box injection in §3
proves a lower bound on its rank after character averaging.

These are the frame-torsor and comodule maps of SGA3 I4.5,4.7.2–4.7.3,
and the Schur operations in the exact representation group of SGA6
V4.2,4.4,4.8–4.9 and VI3.3. They evaluate the composed operations of
cote133/024–029 through the explicit universal map A-010. The last
paragraph of §4 applies the coordinate-image map of EGA I9.5.2 and
G-003 to give an actual nonzero graded Chow coordinate section. All
multiplicities and finite projectors here are over characteristic zero;
the determinant and coefficient constructions have the indicated
integral formulas before those projectors are divided by \(m!\).


# A complete positive formula on the central five-row staircase

## G-023. Seven active polytopes and exact support

For all \(r,d\ge0\), put
\[
n=d+2r,\qquad
\lambda=(d+4r,d+3r,d+2r,d+r,d).
\tag{SF.1}
\]
Every outer label \(\mu\vdash5\) has the positive formula (SF.6),
with at most seven active lattice polytopes of at most eight variables.
At \(r\ge2\) every one of the seven coefficients is positive. At
\(r=1\), the coefficients in the label order
\((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\) are
\((0,1,1,1,1,1,0)\), for every \(d\). At \(r=0\), the unique
nonzero coefficient is one, at \(\mu=(5)\) for even \(d\), and at
\(\mu=(1^5)\) for odd \(d\).

For \(r>0\), these shapes lie strictly inside the remaining region:
\(\lambda_2+\lambda_3=2n+r\) and
\(\lambda_3+\lambda_4=2n-r\). Thus the result evaluates an entire
central family through the actual cycle-trace morphism of G-022.

## 1. Exact trace polytopes and their periods

Take the balanced module \(B_r\) of G-022 at \(m=5\). Its trace
on each conjugacy class is exactly (ST.5)–(ST.6), including the
vanishing condition and the explicit residue-permutation sign. For a
class with cycle lengths \(\ell_1,\ldots,\ell_c\), the count in
(ST.6) is the integer-point count in \(rP_g\), with one variable
per parallel edge and bounds between zero and one in \(P_g\).
Its affine equations are exactly the exponent conditions in (ST.6).
The point with every variable one-half satisfies them, so the dimension
is \(\sum_{i<j}\gcd(\ell_i,\ell_j)-c+1\), with zero for one cycle.

The denominators of the vertices divide
\(L_g=\operatorname{lcm}(\ell_1,\ldots,\ell_c)\). Here is a proof
of the precise denominator bound. At a vertex, remove the edges whose
variables are fixed to zero or one. The remaining edges form a forest:
a cycle would give a nonzero weighted circulation, and both sufficiently
small positive and negative multiples preserve all bounds, contradicting
extremality. Multiply the equation at vertex \(i\) by \(\ell_i\).
Every edge then has ordinary incidence coefficient
\(\operatorname{lcm}(\ell_i,\ell_j)\). The right-hand side is an
integer, because \(\ell_i(5-\ell_i)\) is even; the fixed bound
edges contribute integers as well. Cutting one free forest edge and
summing the equations on a component shows that its value is an integer
divided by that edge's least common multiple. This proves the claimed
common denominator. At the identity all vertices are integral and the
dimension is six.

The cited lattice-count theorem is Beck–Robins, *Computing the Continuous
Discretely*, second edition, **Theorem3.8, p.68**, and **Theorem3.23,
p.80**, in the [author's corrected text of18February2023](https://matthbeck.github.io/papers/ccdnew.pdf).
These give a degree-six polynomial at the identity and, on each other
class, a quasipolynomial of degree at most three, two, one, zero, zero,
zero, respectively, with period dividing \(L_g\). The sign and
vanishing conditions in G-022 have the same periods. Hence finitely
many explicitly counted values determine each trace from \(r=0\).

## 2. The complete seven trace formulas

Write \(I(r)=\operatorname{tr}(1\mid B_r)\). The edge-count recursion
in `staircase_five_trace.py` enumerates the free incident edges of the
first vertex, updates the remaining exact balance demands, and repeats.
Every integer assignment appears once, because its first-vertex edge
values determine the next demands. The final one-vertex demand must be
zero. Parallel-edge values are combined using the coefficients of
\((1+z+\cdots+z^r)^g\), which count their ordered assignments exactly.
This proves the finite enumeration algorithm used below.

The initial identity counts, at \(r=0,\ldots,6\), are
\[
(1,24,219,1136,4175,12216,30429).
\]
Their successive first forward differences give
\[
\boxed{I(r)=1+23\binom r1+172\binom r2+550\binom r3
 +850\binom r4+630\binom r5+180\binom r6.}
\tag{SF.2}
\]
The degree-six theorem just proved makes this equality valid for every
\(r\ge0\). The complete other traces are

| cycle type | exact trace on \(B_r\) |
|---|---|
| \(2\,1^3\) | zero for odd \(r\); at \(r=2h\), \((h+1)^3+h^3\) |
| \(2^2\,1\) | zero for odd \(r\); at \(r=2h\), \(3h^2+3h+1\) |
| \(3\,1^2\) | at \(r=3h,3h+1,3h+2\), respectively \(h+1,-h,0\) |
| \(3\,2\) | periodic list \((1,0,0,0,-1,0)\) modulo six |
| \(4\,1\) | periodic list \((1,0,-1,0)\) modulo four |
| \(5\) | periodic list \((1,-1,-1,1,0)\) modulo five |

For a complete finite verification, the transposition's four required
even values are \(1,9,35,91\); the double transposition's three are
\(1,7,19\). The three-cycle values on residues zero and one are
\((1,2)\) and \((0,-1)\), respectively, at their first two terms;
the remaining residue vanishes by (ST.5). The last three rows are the
initial values of their fixed periods, computed by the same bounded
edge equations. These are all the samples required by the respective
degree and period bounds, so this is a proof by exact finite
interpolation. The certificate additionally checks the identity through
\(r=9\) and every other row through \(r=15\).

## 3. Every fixed positive constant

Use the class sizes \(1,10,15,20,20,30,24\) and the complete
irreducible character table in G-019. Let \(T_g(r)\) be the seven
explicit functions just proved, and set
\[
b_\nu(r)=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)T_g(r).
\tag{SF.3}
\]
This is the actual multiplicity \([\nu:B_r]\), by the projector
of T-003. For \(0\le s<60\) and \(0\le j\le6\), define the
fixed integers
\[
C_{\nu,s,j}=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)
\sum_{i=0}^j(-1)^{j-i}\binom ji T_g(s+60i).
\tag{SF.4}
\]
Only arguments at most419 occur. The delivered exact certificate
computes all2,940 constants from these elementary functions, checks
divisibility by120, and verifies
\[
C_{\nu,s,j}\ge0,\qquad C_{\nu,s,j}>0\quad(j\ge1).
\tag{SF.5}
\]
The minimum over every positive-order constant is107,377,819. All
entries, minima by order, and exact zero constants are in
`STAIRCASE_FIVE_CERTIFICATE.json`; the complete reproducing computation
is `staircase_five_certificate.py`. No representation computation at
an input-dependent size enters (SF.4).

For \(r=s+60q\), the proven residue degree bound and Newton's
identity give the positive formula
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{j=0}^6 C_{\nu,s,j}\binom qj,
\quad
\nu=\mu\ (d\text{ even}),\quad\nu=\mu'\ (d\text{ odd}).}
\tag{SF.6}
\]
The determinant map establishing this sign is the last paragraph of
G-022 §4. Every input parameter and every sign therefore has an actual
representation comparison.

For each residue and order, the polytope has integer variables
\(q,y,z_1,\ldots,z_j\) and constraints
\[
60q=r-s,\quad q\ge0,\quad 0\le y<C_{\nu,s,j},\quad
0\le z_1<\cdots<z_j<q.
\tag{SF.7}
\]
An empty chain is omitted. Every strict inequality becomes an integer
difference at most minus one. Choosing \(y\) and the increasing
\(j\)-subset is an explicit bijection with its lattice points,
whose count is the summand of (SF.6). There are seven active tags,
420 tags before selecting the residue, and at most eight variables.
Evaluation takes a fixed number of arithmetic operations of polynomial
bit cost in \(\log(r+d+2)\).

The exact zeros in the initial residue interval are: \(r=1\) for
\(\nu=(5)\); \(r=0\) for each of the five intermediate labels;
and \(r=0,1\) for \(\nu=(1^5)\). All other initial values are
positive. For \(r\ge60\), the strictly positive first-difference
term in (SF.6) is already nonzero. This proves the entire support and
all endpoint assertions in the statement.

## 4. Geometric transport

The finite normalizer projector is transported from the compact oscillator
representation by T-001–T-003. The determinant character, cycle eigenvalue
map and lattice coefficient extraction in G-022 are explicit maps on
that representation. Formula (SF.6) computes its Schur multiplicity
and hence the composition operation of cote133/024–029 in the exact
representation group of SGA6 VI3.3. Its associated Schur sheaf and
frame-torsor maps are SGA3 I4.5,4.7.2–4.7.3. The underlying torus
weight decomposition and coefficient extraction commute with the
specified base changes after the characteristic-zero projectors are
formed. The count gives an exact rank of this actual projector.


\part{Checked canonical-map and rectangular results}


# Rectangular cases and the normalized Hadamard--Howe period

Run: `/root/rectangular_cases`, 21 November 2026 (Europe/Berlin).
Model: GPT-6 Astra Pro. The inherited effort setting is not exposed to this agent.

This report supplies exact reformulations, proofs, source locators, and finite certificates for the parent paper. The literature results remain attributed to their authors. The labels R-001--R-006 identify findings and explicit dictionaries established in this run; they do not claim priority over the cited classical results.

## Notation

Write

\[
a_\lambda(d[n])=[S_\lambda V:\operatorname{Sym}^d(\operatorname{Sym}^nV)],
\qquad R_{r,s}=(s^r),
\]

with \(\dim V\ge\ell(\lambda)\). Thus \(r\times s\) in the supplied Ikenmeyer--Panova source means \(R_{r,s}\). All decompositions of complex representations below use characteristic zero. The base ring used for normalized integral tensors will be specified separately.

The Hadamard--Howe map is normalized by averaging permutations, so that

\[
h_{d,n}(v_1^n\cdots v_d^n)=(v_1\cdots v_d)^n.
\]

This is the convention of Kumar--Landsberg, §1.2, arXiv:1410.8585v1.

## R-001. A rectangular plethysm coefficient as a one-point lattice count

For every \(r\ge2\), \(n\ge1\),

\[
a_{(n^r)}(r[n])
=\#\{z\in\mathbb Z:2z=n\}
=\begin{cases}1&n\text{ even},\\0&n\text{ odd}.\end{cases}
\tag{R-001}
\]

The first equality presents a positive lattice-point formula on the rational zero-dimensional polytope \(\{n/2\}\). The multiplicity-one statement is classical: Howe, *\((\mathrm{GL}_n,\mathrm{GL}_m)\)-duality and symmetric plethysm*, Proposition 4.3, as located explicitly in Kumar--Landsberg §2; also supplied BIP §2(b).

### Proof of the precise lattice-count form

Take \(V=\mathbb C^r\). A tensor in \((\operatorname{Sym}^nV)^{\otimes r}\) is a polynomial on \(r\) covectors, separately of degree \(n\) in each covector. Arrange the covectors as columns of an \(r\times r\) matrix \(X\). On the dense open subset \(\det X\ne0\), an \(\mathrm{SL}_r\)-invariant polynomial depends only on \(\det X\): two invertible matrices with the same determinant differ by left multiplication by an element of \(\mathrm{SL}_r\). Separate homogeneity forces the invariant to be a scalar multiple of \((\det X)^n\). Equality on the dense open subset is equality of polynomials. Thus the invariant space in the ordered tensor product is one-dimensional.

Permutation of the \(r\) covectors acts on this line by \(\operatorname{sgn}^n\). Passing to the outer symmetric power is taking the invariants of this \(S_r\)-action. Since \(r\ge2\), the invariant dimension is one for even \(n\) and zero for odd \(n\). The \(\mathrm{SL}_r\)-invariant summand of homogeneous degree \(rn\) has \(\mathrm{GL}_r\)-highest weight \((n^r)\). Finally, the equation \(2z=n\) has exactly one integral solution for even \(n\) and none for odd \(n\). This proves all displayed equalities.

The same coefficient holds in every \(\dim V\ge r\): Schur-functor multiplicities are stable once the indexed partition fits, by the symmetric-group multiplicity-space realization.

## R-002. The exact square Hadamard--Howe scalar

Fix an even integer \(n\ge2\), let \(V=\mathbb C^n\), and put \(H=S_n\wr S_n\). Index the tensor factors of \(V^{\otimes n^2}\) by the cells \((i,j)\) of an \(n\times n\) array. Let \(e_H\) be the average over permutations within rows and permutations of rows. Let \(\tau\) transpose the array. Then

\[
\operatorname{Sym}^n(\operatorname{Sym}^nV)=e_HV^{\otimes n^2},
\qquad h_{n,n}=e_H\tau e_H.
\]

Define

\[
\delta=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(n)},
\]

put one copy of \(\delta\) in each column, call the resulting tensor \(D\), and put \(I=e_HD\). This \(I\) spans the determinant line from R-001. For a Latin square \(L\), let \(c(L)\) denote the product of its column signs, and let \(E_n-O_n\) be its signed enumeration using the product of all row and column signs. Set

\[
\Delta_n=\sum_{L\text{ Latin}}c(L),\qquad
B_n=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!}.
\]

The normalized scalar is

\[
\boxed{
h_{n,n}(I)=c_n I,\qquad
c_n=\frac{\Delta_n}{(n!)^n}
=\frac{(-1)^{n(n-1)/2}(E_n-O_n)}{(n!)^n}
=\frac{B_n}{(n!)^n}\int_{\mathrm{SU}(n)}\prod_{i,j=1}^n u_{ij}\,du.
}
\tag{R-002}
\]

Here Haar measure has total mass one. Kumar--Landsberg Theorem 1.9 proves the associated nonvanishing equivalences; Proposition 2.1 gives the determinant contraction. The present calculation fixes every scalar under the displayed averaging convention. Alpöge, *Square-root cancellation for the signs of Latin squares*, Corollary 5, supplies the last coefficient-to-Haar identity. That paper is separate bibliographic material from the supplied `ALPOGE_remark.pdf`.

### Proof of the scalar

Equip the standard tensor basis with its orthonormal inner product. Let \(t_0\) have entry \(e_i\) in every cell of row \(i\). Although \(t_0\) is invariant under the within-row permutations, it need not be invariant under permutations of rows. The needed pairing still has the value one: every row permutation of \(t_0\) has coefficient \(\operatorname{sgn}(\pi)^n=1\) in \(D\), so

\[
\langle I,t_0\rangle=\langle D,e_Ht_0\rangle=1.
\tag{R-002a}
\]

Because \(I\) spans the determinant line, write \(h_{n,n}I=c_nI\). Self-adjointness of the averages and the transpose permutation gives

\[
c_n=\langle e_H\tau I,t_0\rangle
=\langle I,\tau e_Ht_0\rangle.
\]

The tensor \(e_Ht_0\) is the average of \(t_0\) over permutations of rows. After applying \(\tau\), those permutations become simultaneous within-row permutations of \(t_1:=\tau t_0\). Since \(I\) is invariant under the within-row permutations,

\[
c_n=\langle I,t_1\rangle=\langle D,e_Ht_1\rangle.
\]

Every row of \(t_1\) is \((e_1,\ldots,e_n)\). Thus \(e_Ht_1\) averages independently over the \(n!\) reorderings in each of its \(n\) rows. A tensor in this average pairs nontrivially with \(D\) exactly when its columns also contain each basis vector once, which is exactly the Latin-square condition. Its coefficient in \(D\) is the product of column signs. Therefore the pairing is \(\Delta_n/(n!)^n\).

### Proof of the parity conversion

This conversion is an identity of total signed sums, not an equality of the two sign functions on each square. Let \(r(L),c(L),s(L)\) be respectively the products of row, column, and symbol-position signs. On the \(n^2\) ordered pairs, define

\[
R:(i,j)\mapsto(i,L_{ij}),\quad
S:(i,s)\mapsto(j,s)\text{ where }L_{ij}=s,
\quad T:(j,s)\mapsto(s,j).
\]

The column permutation \(C:(i,j)\mapsto(L_{ij},j)\) satisfies \(C=TSR\). The transpose permutation \(T\) has sign \(\epsilon=(-1)^{n(n-1)/2}\), hence \(r(L)c(L)s(L)=\epsilon\). Form the conjugate Latin square \(L'\), with row \(i\), column \(s\), and entry \(j\) specified by \(L_{ij}=s\). Its row-sign product is \(r(L)\), and its column-sign product is \(s(L)\). Its ordinary sign is therefore \(\epsilon c(L)\). The correspondence \(L\mapsto L'\) is a bijection. Summing proves \(\Delta_n=\epsilon(E_n-O_n)\).

### Proof of the Haar normalization

The coefficient \(C_n\) of \(\prod_{i,j}X_{ij}\) in \(\det(X)^n\) is the sum of the products of the signs of the symbol-position permutations in Latin squares. Parastrophy exchanges this with the column-sign sum, so \(C_n=\Delta_n\). Apply Alpöge Corollary 5 to the all-ones multiindex \(\alpha\), with \(k=n\). Its factorial \(\alpha!\) is one, and the displayed factor in that corollary is \(B_n\). Consequently \(\Delta_n=B_n\int\prod u_{ij}\,du\), giving the last equality.

### Exact finite values and a checked bound

The enumeration script `verify_rectangular.py` visits every reduced Latin square for \(n=2,4,6\), with first row and first column fixed. It found:

| \(n\) | Reduced squares | Reduced column-sign sum | All squares | \(\Delta_n\) | \(c_n\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | -1 | 2 | -2 | \(-1/2\) |
| 4 | 4 | 4 | 576 | 576 | \(1/576\) |
| 6 | 9408 | -2304 | 812851200 | -199065600 | \(-1/699840000\) |

Every reduced square has \(n!(n-1)!\) completions under row and symbol normalization, and the column sign is unchanged for even \(n\). The recursion enumerates all row permutations with their first entry prescribed, rejects exactly repeated column symbols, and at depth \(n\) evaluates the product of column permutation signs. Thus this is a finite exhaustive certificate, not sampling. The certificate asserts only these three orders.

Alpöge Theorem 2, evaluated at \(k=n\), gives the exact inequality

\[
0\le |c_n|^2\le\frac{B_n}{(n!)^{2n}}.
\tag{R-002b}
\]

The value zero belongs to this interval. The unresolved scalar in the square rectangular component is precisely \(\Delta_n\), or equivalently the displayed Haar integral. No lower bound for general even \(n\) is established in this report.

## R-003. A concrete failure of positivity transfer from rectangular Kronecker coefficients

For every \(d,n\ge1\) and \(1\le k\le dn-1\),

\[
a_{(dn-k,1^k)}(d[n])=0.
\tag{R-003a}
\]

This vanishing is known: Eugenio Giannelli, *Representations of symmetric groups*, PhD thesis (2015), Theorem 2.1.2, p.38, with proof in §2.3, pp.42--43; Giannelli attributes the earlier Schur-function proof to Langley--Remmel. The short argument below records the exact wreath-product/exterior-power dictionary used in the counterexample. The hook/exterior-power identification is Giannelli Lemma 2.3.3 (also Fulton--Harris, Proposition 3.12 for irreducibility).

In particular,

\[
\boxed{a_{(13,1,1,1)}(4[4])=0,\qquad
g((13,1,1,1),(4^4),(4^4))=1.}
\tag{R-003b}
\]

The parameters in R-003b lie in the stable range of Ikenmeyer--Panova Proposition 2.8: the tail \(\rho=(1,1,1)\) has size three and the inner degree is four. Thus the actual inequality at this point is \(1\ge0\).

### Proof

The finite-group multiplicity formula is

\[
a_\lambda(d[n])=\dim[\lambda]^{S_n\wr S_d}.
\]

For \(N=dn\), the hook Specht module \([N-k,1^k]\) is \(\bigwedge^kU_N\), where \(U_N\) is the standard, sum-zero representation of \(S_N\). Restrict to the base group \(K=S_n^d\). There is an explicit decomposition

\[
U_N=A\oplus U_n^{(1)}\oplus\cdots\oplus U_n^{(d)},
\]

where \(A\) consists of vectors constant within each block and with total sum zero. The base group fixes \(A\) pointwise, and its quotient \(S_d\) acts on \(A\) as \(U_d\). For every \(j=1,\ldots,n-1\), \(\bigwedge^jU_n\) is the nontrivial irreducible hook \([n-j,1^j]\), so it has no \(S_n\)-invariants. The exterior-power decomposition of a direct sum therefore gives

\[
(\bigwedge^kU_N)^K=\bigwedge^kA.
\]

Taking the remaining \(S_d\)-invariants yields zero for every \(k>0\): the exterior powers in their nonzero range are the nontrivial hooks \([d-k,1^k]\), and the remaining exterior powers vanish. The cases \(n=1\) or \(d=1\) are immediate from the same decomposition with zero-dimensional summands. This proves R-003a.

Ikenmeyer--Panova Proposition 6.4 gives

\[
\sum_k g((16-k,1^k),(4^4),(4^4))q^k
=(1+q^3)(1+q^5)(1+q^7).
\]

The coefficient of \(q^3\) is one, proving R-003b. Independently, `verify_rectangular.py` computed the plethysm by the power-sum cycle index \(h_4[h_4]\), paired with the hook character, and the Kronecker coefficient by the Murnaghan--Nakayama character rule followed by the exact conjugacy-class sum. Both computations use rational arithmetic and give the displayed values.

## R-004. The rectangular-hook polytope

For \(1\le r\le s\), \(0\le k\le rs-1\), let

\[
P_{r,k}=\{(x_2,\ldots,x_r)\in[0,1]^{r-1}:
\sum_{i=2}^r(2i-1)x_i=k\}.
\]

Ikenmeyer--Panova Proposition 6.4 gives exactly

\[
g((rs-k,1^k),(s^r),(s^r))=\#(P_{r,k}\cap\mathbb Z^{r-1}).
\tag{R-004}
\]

The proof of this reformulation is the bijection sending a partition into distinct allowed parts \(3,5,\ldots,2r-1\) to its indicator vector. It preserves the sum. R-003 explicitly computes the plethysm coefficient for one of the positive points of this polytope.

## R-005. An explicit vector and multiplicity one for row-extended even rectangles

Take \(k\ge2\), an even integer \(\ell\ge2\), and \(n\ge\ell\). Put

\[
\lambda=(kn-(k-1)\ell,\ell^{k-1}).
\]

Then

\[
a_\lambda(k[n])=1.
\tag{R-005a}
\]

For \(n\ge k\ell\), the same multiplicity in \(\mathbb C[\overline{\mathrm{GL}_{n^2}\det_n}]_k\) is exactly one. This combines the explicit vector below with BIP Propositions 2.3 and 5.6(1), and Theorem 2.5. The equality of multiplicities refines the occurrence statement to the one-dimensional ambient component.

### Proof and normalized nonzero evaluation

Use \(k\) basis vectors and form \(I_{k,\ell}\) by placing the alternating \(k\)-tensor in each of \(\ell\) columns and averaging the within-row and outer permutations. It is a highest weight vector of weight \((\ell^k)\). For nonzero coefficients \(c_1,\ldots,c_k\), direct contraction gives

\[
\big\langle I_{k,\ell},(\sum_{i=1}^k c_iX_i^\ell)^{\otimes k}\big\rangle
=k!\prod_{i=1}^k c_i.
\tag{R-005b}
\]

Indeed, a nonzero determinant contraction assigns distinct basis labels to the \(k\) rows. There are \(k!\) assignments, their signs are raised to the even power \(\ell\), and every assignment has coefficient \(\prod_i c_i\).

Let \(M:\operatorname{Sym}^\ell V\to\operatorname{Sym}^nV\) multiply by \(e_1^{n-\ell}\), and put \(\kappa=\operatorname{Sym}^kM\). The upper triangular unipotent group fixes \(e_1\), so \(\kappa(I_{k,\ell})\) remains a highest weight vector and its weight is \(\lambda\). The map \(M\), and therefore \(\kappa\), is injective. BIP Proposition 5.6(1) says that \(\kappa\) is an isomorphism on these highest weight spaces, since the second part of \((\ell^k)\) equals the initial inner degree \(\ell\). R-001 now gives R-005a.

With normalized symmetric-tensor pairings, the dual map is

\[
M^*=\frac{\ell!}{n!}\partial_{X_1}^{n-\ell}.
\]

For

\[
q=X_1^{n-\ell}\sum_{i=1}^k c_iX_i^\ell
\]

one obtains

\[
M^*q=c_1X_1^\ell+\binom n\ell^{-1}\sum_{i=2}^k c_iX_i^\ell,
\]

and hence

\[
\boxed{\langle\kappa(I_{k,\ell}),q^{\otimes k}\rangle
=k!\binom n\ell^{-(k-1)}\prod_{i=1}^k c_i\ne0.}
\tag{R-005c}
\]

The pairing identity follows directly from the definition of a dual map, also BIP Theorem 5.4. For \(n\ge k\ell\), BIP Theorem 2.5 places every such padded power sum in the determinant orbit closure. Thus the coordinate-ring quotient is nonzero on this one-dimensional highest weight space. Its multiplicity is both at least one and at most the ambient multiplicity one, proving the claimed equality.

## R-006. Scheme, locally free sheaf, and Grothendieck-group dictionary

The following constructions specify the morphisms transporting R-001--R-005.

1. **Group schemes and Schur operations.** The representations are obtained from the standard locally free sheaf of \(\mathrm{GL}_{r,\mathbb Z}\) by tensor, exterior, and symmetric powers. Over \(\mathbb Q\), their identities are identities in \(K_0(\operatorname{Rep}_{\mathbb Q}\mathrm{GL}_r)\). A principal \(\mathrm{GL}_r\)-bundle on a \(\mathbb Q\)-scheme gives an associated locally free sheaf \(E\). Applying the associated-bundle functor transports each actual natural tensor morphism and each equality in this Grothendieck group to the corresponding sheaf morphism and class in \(K_0(X)\). In particular, the plethystic operation is \([E]\mapsto[\operatorname{Sym}^d(\operatorname{Sym}^nE)]\).

2. **The determinant line and the normalized map.** For R-002, take \(R=\mathbb Z[1/n!]\). The group order \(|H|=(n!)^{n+1}\) is invertible, so all displayed averages are defined over \(R\). Frame change multiplies \(I\) by \(\det(g)^n\). The resulting locally free line is \((\det E)^{\otimes n}\), and the restriction of the natural tensor map to it is multiplication by the exact scalar \(\Delta_n/(n!)^n\). The scalar and the line therefore descend from frames over \(R\) to every locally free \(E\) of rank \(n\). Over the complex fiber, the coordinate multiplicity in the image of this map is the rank of this scalar map.

3. **The Chow scheme and its coordinate map.** The morphism

   \[
   \mu:(E^*)^{\times n}\longrightarrow\operatorname{Sym}^n E^*,
   \qquad(\ell_1,\ldots,\ell_n)\longmapsto\ell_1\cdots\ell_n
   \]

   is defined over \(\mathbb Z\). Its pullback on degree-\(d\) coordinate functions lands in separately degree-\(d\) functions, invariant under \(S_n\), and over \(\mathbb Q\) identifies with \(h_{d,n}\). The affine scheme-theoretic image has coordinate algebra \(\operatorname{im}\mu^*\); this realizes the Chow cone and gives \(\ker h_{d,n}=I(\mathrm{Chow}_n)_d\). Thus R-002 is an exact equation for the rank of the rectangular component of a morphism of coordinate algebras. For \(n=2,4,6\), the finite certificates prove rank one in that component. This coordinate-map assertion is also Kumar--Landsberg Lemma 1.5.

4. **The exact \(K_0\) relation.** For a line \(L\) over a field and an endomorphism \(f:L\to L\), its kernel-image-cokernel exact sequence gives \([\ker f]=[\operatorname{coker}f]\). For the map \(f=0\), both classes equal \([L]\); for \(f=1\), both classes are zero. Both endomorphisms have domain and codomain \(L\). This computes exactly the information supplied by the class identity \([L]-[L]=0\). R-002 records the additional morphism \(c_n\operatorname{id}_L\). The associated \(\lambda\)-operation has \(\lambda_t([L])=1+[L]t\), while \(\gamma_t([L]-1)=1+([L]-1)t\); neither formula changes with the chosen endomorphism of the line, as is verified by the two explicit maps.

5. **Finite étale schemes and weights.** Let \(\mathcal L_n^+\) and \(\mathcal L_n^-\) be the constant finite schemes over \(\mathbb Z\) indexed by column-even and column-odd Latin squares. Their virtual class is \([\mathcal L_n^+]-[\mathcal L_n^-]=\Delta_n[\operatorname{Spec}\mathbb Z]\). Over every finite field, each geometric point contributes one eigenvalue one to \(H_c^0\), and higher cohomology vanishes. Thus the difference of Frobenius traces is exactly \(\Delta_n\). This gives a direct finite-scheme and weight-zero dictionary for the same signed period numerator. For odd \(n>1\), swapping two rows reverses the column sign and gives an involution pairing all squares, so this virtual class and trace are zero. For even \(n=2,4,6\), their values are the three nonzero integers in the certificate. These are exact computations of the maps and classes involved, with no assertion excluding other geometric relations.

The parent paper is to supply the exact SGA/EGA/FGA locators for these standard constructions from its independent archive/SGA audit. This report does not invent unverified exposé or proposition numbers.

## Exact inventory of supplied literature relevant to item 4

All statements in this inventory are attributed results, not new findings. Parameter domains are written explicitly.

### Ikenmeyer--Panova (IP), arXiv:1512.03798v2

Let \(\rho(N)=(N-|\rho|,\rho)\), whenever it is a partition, and \(\bar\lambda\) be the tail after removing the first row. Let

\[
\mathcal X=\{(1),(1,1),(1,1,1,1),(1^6),(2,1),(3,1)\}.
\]

| Locator | Exact content used |
|---|---|
| Theorem 1.6, p.3 | For \(n>3m^4\), support of the padded-permanent coordinate ring in degree \(d\) is contained in \(\{\lambda:g(\lambda,(d^n),(d^n))>0\}\). |
| Theorem 1.8, pp.3--4 (Kadish--Landsberg) | That support has \(\ell(\lambda)\le m^2\), \(|\bar\lambda|\le md\). |
| Corollary 1.9, p.4 | On \(|\bar\lambda|\le md\), a strict inequality \(a_\lambda(d[n])>g(\lambda,(d^n),(d^n))\) requires \(d>n/m\). |
| Theorem 1.10(a), p.4 | Every \(\lambda\) with \(\bar\lambda\in\mathcal X\) has \(a_\lambda(d[n])=0\). |
| Theorem 1.10(b), p.4 | For \(m\ge3\), \(\bar\lambda\notin\mathcal X\), \(\ell(\lambda)\le m^2\), \(|\bar\lambda|\le md\), \(d>3m^3\), \(n>3m^4\), the rectangular Kronecker coefficient is positive. |
| Theorem 2.1, p.5 (Manivel, Theorem 1) | For \(n\ge|\rho|\), \(g(\rho(nd),(d^n),(d^n))=\dim S_\rho(\mathfrak{sl}_d)^{\mathrm{SL}_d}\). The function is symmetric and nondecreasing in \(n,d\). |
| Proposition 2.8, p.7 | For \((n,d)\in\mathrm{St}^1(\rho)\), in particular \(n\ge|\rho|\), \(g(\rho(nd),(d^n),(d^n))\ge a_{\rho(nd)}(d[n])\). |
| Theorem 4.7, p.11 | For \(\nu\notin\mathcal X\), \(L=\max(\ell(\nu)+1,9)\), \(a>3L^{3/2}\), \(b\ge3L^2\), and \(|\nu|\le ab/6\), \(g(\nu(ab),(b^a),(b^a))>0\). |
| Corollary 5.1, p.13 | The stable limit \(A_\rho\) vanishes exactly for \(\rho\in\mathcal X\). Here \(A_\rho\) is a stable rectangular Kronecker coefficient, with its invariant-Schur-functor realization in Theorem 2.1. |
| Proposition 5.2, p.13 | For \(i\ge2\), \(m\ge7\), \(0\le k<m^2\), \(g(i(m^2-k,1^k),((im)^m),((im)^m))>0\). |
| Corollary 5.3, p.14 | For \(m\ge7\), every even-row partition \(\rho\) of length less than \(m^2\) has \(\dim S_\rho(\mathfrak{sl}_m)^{\mathrm{SL}_m}>0\). |
| Corollary 5.4, p.14 | For \(d\ge7\), the group generated by the rectangular Kronecker support semigroup in \(\mathbb Z^{d^2}\) is \(\{z:\sum z_i\equiv0\pmod d\}\). |
| Proposition 6.4, p.15 | The hook coefficients have the subset-count formula used in R-004. |

### Bürgisser--Ikenmeyer--Panova (BIP), arXiv:1604.06431v3

| Locator | Exact content used |
|---|---|
| Theorem 1.4, p.3 | For \(n\ge m^{25}\), support of the padded-permanent coordinate ring is contained in support of the determinant-orbit-closure coordinate ring. |
| Proposition 2.3, p.5 | \(n\ge k\ell\), \(\ell\) even: \((k\times\ell)^{\sharp nk}\) occurs in determinant-orbit-closure degree \(k\). |
| Proposition 2.4, p.5 | \(|\bar\lambda|\le md\), \(md^2\le n\): restriction to the determinant closure is injective on the \(\lambda\)-highest-weight space. The natural reading of “every highest weight vector” is every nonzero such vector. |
| Theorem 2.5, p.5 | \(n\ge sk\): every \(X^{n-s}\sum_{i=1}^k\varphi_i^s\) belongs to the determinant orbit closure. |
| Corollary 4.8, p.13 | Explicit determinant-contraction nonvanishing on power sums for even inner degree. |
| Theorem 5.4, p.15 | \(\langle\kappa^d_{m,n}(f),q^d\rangle=\langle f,(M^*q)^d\rangle\). |
| Proposition 5.6(1), p.17 | \(n\ge m\), \(\mu\vdash md\), \(\mu_2\le m\): \(\kappa\) induces an isomorphism of the highest-weight spaces of weights \(\mu\) and \(\mu+(d(n-m))\). |

The BIP support inclusion constrains occurrence obstructions. The morphism-level question is retained by the restriction map and by its ranks on multiplicity spaces. No conclusion on P versus NP is claimed here.

## Source-proof audit notes and boundaries of checking

1. IP Theorem 6.1's displayed exception `d^1-2` is a typographical error: Proposition 6.4 and the proof's table use \(d^2-2\). Its additionally stated strict inequality \(g_k>g_{k-2}\) for all \(k\le d^2/2\) also fails literally, for example \(d=7,k=2\) gives \(0>1\). We use the exact Proposition 6.4 instead. This discrepancy is proved by the generating function, rather than silently correcting the printed theorem.

2. In the supplied proof of IP Theorem 4.7, the line \(w<\sqrt{L+7}+1\le(L+1)/2\), with \(w=\max(\lceil\sqrt{L+7}\rceil,7)\), is false at \(L=9\): it asserts \(7<5\). This is a gap in that displayed estimate, not a counterexample to the theorem. The broad theorem is cited as literature, and is not certified here as an independently checked proof. No new proof in this report depends on that estimate. The parent can record this explicitly or omit reliance on Theorem 4.7.

3. The hook counterexample, parity conversion, averaging normalization, and row-extended evaluation were read and checked in full. A first informal scalar derivation had called \(t_0\) invariant under all of \(H\); that statement fails for row permutations. R-002's final proof explicitly averages \(t_0\), uses evenness to compute its pairing, and moves the row permutations through \(\tau\). This repairs the issue without changing the scalar.

4. Computational certificates are exact finite certificates for their stated inputs. They do not certify a universal nonvanishing theorem or the entire supplied literature.

## Primary-source URLs for root verification

- IP: https://arxiv.org/pdf/1512.03798 (v2).
- BIP: https://arxiv.org/pdf/1604.06431 (v3).
- Kumar--Landsberg: https://arxiv.org/pdf/1410.8585 (v1), Theorem 1.9, Proposition 2.1, Lemma 1.5; Howe Proposition 4.3 cited in §2.
- Alpöge: https://people.math.harvard.edu/~alpoge/papers/combinatorica%20paper.pdf, Theorem 2 and Corollary 5.
- Bürgisser--Christandl--Ikenmeyer, *Even partitions in plethysms*: https://www3.math.tu-berlin.de/algebra/work/weintraub.pdf, §1.1 unnumbered main theorem; arXiv:1003.4474v2. Its domain \(\lambda\vdash kn,\ell(\lambda)\le k\) yields \(a_{2\lambda}(k[2n])>0\).
- Giannelli, *Representations of symmetric groups*: https://eugeniomaths.wordpress.com/wp-content/uploads/2013/10/tesi-final-version-2015.pdf, Theorem 2.1.2 and Lemma 2.3.3.

Web references available in this child run: `turn614803048view0` (IP), `turn614803048view1` (BIP), `turn768780200view0` (Kumar--Landsberg), `turn245878279view0` (Alpöge), `turn517469220search12` (BCI). The root must open them independently before citing them in chat.


# Canonical-map boundary checks and prime rectangular blocks

Run: /root/rectangular_cases, 21 November 2026 (Europe/Berlin).
Model: GPT-6 Astra Pro. The inherited reasoning-effort setting is not exposed.

This supplements rectangular_report.md. The scalar normalization and the
determinant tensors \(I_{a,b}\) use that report's R-001 and R-002. The new
formulas below are explicit consequences of established results of Glynn,
Drisko, Howe, and the algebra morphism defining the canonical map. No claim
of priority is made for their nonvanishing content. The full surjectivity
bound proved in Sra III remains \(b\ge(a-1)^2\); the results below prove
specified components at smaller degrees.

## Exact map and coefficient conventions

Put \(V=\mathbb C^a\), with its orthonormal basis \(e_1,\ldots,e_a\), and

\[
 R_a=\bigoplus_{b\ge0}\left((\operatorname{Sym}^b V)^{\otimes a}\right)^{S_a}.
\]

The product is componentwise multiplication. Symmetric powers are realized
as invariant tensors by normalized averaging. There is a graded algebra
morphism

\[
 \mu_a:\operatorname{Sym}(\operatorname{Sym}^aV)\longrightarrow R_a,
 \qquad \mu_a(v^a)=v^{\otimes a}.
 \tag{B1}
\]

Its degree-\(b\) component is \(h_{b,a}\). Thus

\[
 h_{b,a}(u_1^a\cdots u_b^a)=(u_1\cdots u_b)^{\otimes a}.
 \tag{B2}
\]

For even \(b\), let \(I_{a,b}\) be obtained by putting the unnormalized
alternating \(a\)-tensor in each of \(b\) columns, and averaging within
the \(a\) rows. Permuting the rows has sign \(\operatorname{sgn}^b=1\),
so further outer averaging makes no change. This tensor satisfies

\[
 \langle I_{a,b},v_1^b\otimes\cdots\otimes v_a^b\rangle
       =\det(v_1,\ldots,v_a)^b.
 \tag{B3}
\]

The inner product is conjugate-linear in its first argument. All tensors
appearing in the coefficient calculations have rational real coefficients.
The coefficient at the tensor having row \(i\) constantly \(e_i\) is one.
The determinant line in \(R_{a,b}\) is one-dimensional by R-001. Products
of the determinant tensors satisfy the actual equality in the algebra

\[
 I_{a,b}I_{a,c}=I_{a,b+c}\qquad(b,c\text{ even}).
 \tag{B4}
\]

Indeed, evaluation on arbitrary \(a\) covectors turns both sides into
the product of determinant powers. Such evaluations determine the tensor.

## R-007. Prime-adjacent square scalars and periods

Let \(p\) run through the odd primes, and write

\[
 \mathcal P_n=\int_{\operatorname{SU}(n)}\prod_{i,j=1}^{n}u_{ij}\,du,
 \qquad
 B_n=\prod_{j=0}^{n-1}\frac{(n+j)!}{j!}.
\]

The normalized square scalar from R-002 satisfies

\[
 \boxed{c_{p-1}\in1+p\mathbb Z_{(p)},\qquad
        p^{p-1}c_{p+1}\in1+p\mathbb Z_{(p)}.}
 \tag{R-007a}
\]

In particular these are nonzero scalars, with exact valuations

\[
 v_p(c_{p-1})=0,\qquad v_p(c_{p+1})=1-p,
 \qquad
 v_p(\mathcal P_{p-1})=2-p,\qquad
 v_p(\mathcal P_{p+1})=-p.
 \tag{R-007b}
\]

Here \(\mathbb Z_{(p)}\) denotes the rational numbers whose denominator is
coprime to \(p\); the integral is the rational number identified by the
coefficient formula of R-002.

### Source statements and proof of this normalization

Glynn, *The conjectures of Alon--Tarsi and Rota in dimension prime minus
one*, Theorem 3.2, states

\[
 E_{p-1}-O_{p-1}\equiv(-1)^{(p-1)/2}\pmod p.
\]

Drisko, *On the number of even and odd Latin squares of order \(p+1\)*,
Theorem 9, pp. 33--34, states

\[
 E_{p+1}-O_{p+1}\equiv(-1)^{(p+1)/2}p^2\pmod {p^3}.
\]

Both use row-times-column parity. R-002 proves

\[
 \Delta_n=(-1)^{n(n-1)/2}(E_n-O_n),\qquad
 c_n=\frac{\Delta_n}{(n!)^n},\qquad \mathcal P_n=\frac{\Delta_n}{B_n}.
\]

For even \(n\), \(n(n-1)/2\equiv n/2\pmod2\). Consequently the two
source congruences become

\[
 \Delta_{p-1}\equiv1\pmod p,
 \qquad \Delta_{p+1}\equiv p^2\pmod {p^3}.
\]

Wilson's theorem gives \((p-1)!\equiv-1\pmod p\), and

\[
 \frac{(p+1)!}{p}=(p+1)(p-1)!\equiv-1\pmod p.
\]

The exponents \(p-1\) and \(p+1\) are even. Dividing by the corresponding
factorial units proves (R-007a), and its first two valuation assertions.
In \(B_{p-1}\), the numerator factorials from \(p!\) through
\((2p-3)!\) each contain exactly one factor of \(p\), while all denominator
factorials are prime to \(p\). Thus \(v_p(B_{p-1})=p-2\).
In \(B_{p+1}\), the \(p-1\) factorials \((p+1)!,\ldots,(2p-1)!\)
have valuation one, the two factorials \((2p)!\) and \((2p+1)!\)
have valuation two, and the denominator contributes the one factor in
\(p!\). Thus \(v_p(B_{p+1})=(p-1)+4-1=p+2\). This proves the period
valuations. The ranges include \(p=3\).

These calculations use the established prime-adjacent Alon--Tarsi cases;
they do not supply further orders for that conjecture.

## R-008. A canonical determinant block for every prime-minus-one width

For every odd prime \(p\), every \(2\le a\le p-1\), and \(b=p-1\), put

\[
 m_a=e_1\cdots e_a\in\operatorname{Sym}^aV,
 \qquad
 q_{a,b}=\langle I_{a,b},h_{b,a}(m_a^b)\rangle.
\]

Then

\[
 \boxed{q_{a,p-1}\in1+p\mathbb Z_{(p)}.}
 \tag{R-008a}
\]

In particular the canonical map \(h_{p-1,a}\) has rank one on the
target determinant isotypic component \(S_{((p-1)^a)}V\). The tensor
\(m_a^b\) is an explicit test vector for that component.

More explicitly, in tensor degree \(ab\) set

\[
 e_{(b^a)}=\frac{f^{(b^a)}}{(ab)!}
       \sum_{\sigma\in S_{ab}}\chi^{(b^a)}(\sigma)\sigma,
 \qquad N_{a,b}=\langle I_{a,b},I_{a,b}\rangle>0.
\]

This is the central Schur projector, with \(f^{(b^a)}\) the dimension
of the indicated Specht module. Define the concrete source vector

\[
 u_{a,p}=\frac{N_{a,p-1}}{q_{a,p-1}}
             e_{((p-1)^a)}m_a^{p-1}.
 \tag{B5}
\]

It satisfies the exact equality

\[
 h_{p-1,a}(u_{a,p})=I_{a,p-1}.
 \tag{R-008b}
\]

### Proof of the unit contraction

Glynn's Theorem 3.1, together with the formula defining his modular
hyperdeterminant immediately before that theorem, gives the following
coefficient congruence. For an \(a\times a\) matrix \(E=(e_{ij})\)
of nonnegative integers having every row and every column sum \(b=p-1\),

\[
 C_E=[X^E]\det(X)^b
       \equiv\frac{(-1)^a}{\prod_{i,j}e_{ij}!}\pmod p.
 \tag{B6}
\]

Every denominator in (B6) is a unit modulo \(p\). Write a general
degree-\(b\) vector as

\[
 P=\sum_{|\alpha|=b}P_\alpha e^\alpha,
 \qquad
 F(P)=\langle I_{a,b},P^{\otimes a}\rangle.
\]

Let \(M(\alpha)=b!/\prod_j\alpha_j!\). Evaluation of (B3), first on
independent row vectors and then on their monomial expansions, gives
the exact coefficient formula

\[
 F(P)=\sum_E \frac{C_E}{\prod_i M(E_i)}\prod_i P_{E_i},
 \tag{B7}
\]

where \(E_i\) is row \(i\) of \(E\). This accounts for the normalized
embedding of each symmetric monomial. Wilson's theorem gives

\[
 \prod_iM(E_i)\equiv
 \frac{(-1)^a}{\prod_{i,j}e_{ij}!}\pmod p.
\]

Thus every ratio in (B7) is one modulo \(p\). Equivalently, with
\(P(x)=\sum P_\alpha x^\alpha\),

\[
 F(P)\equiv[x_1^b\cdots x_a^b]P(x)^a\pmod p.
 \tag{B8}
\]

Now introduce independent \(z_{ij}\), \(1\le i\le a\), \(1\le j\le b\),
put \(\ell_j=\sum_i z_{ij}e_i\), and substitute
\(P=\ell_1\cdots\ell_b\) in (B8). By (B2), the left side becomes

\[
 \left\langle I_{a,b},h_{b,a}(\ell_1^a\cdots\ell_b^a)\right\rangle.
\]

Its coefficient at the squarefree monomial \(\prod_{i,j}z_{ij}\)
is \((a!)^b q_{a,b}\), since the squarefree coefficient in
\(\ell_j^a\) is \(a!m_a\). On the right side of (B8), the same
coefficient in \(\prod_j\ell_j(x)^a\) is
\((a!)^b(x_1\cdots x_a)^b\), so it becomes \((a!)^b\) after
coefficient extraction in \(x\). The integer \(a!\) is prime to \(p\).
Cancelling it proves (R-008a).

All tensor averages used here have denominators prime to \(p\), because
\(a,b<p\), so the stated congruences are in the specified local ring.

### Proof of the actual preimage

The central projector \(e_{(b^a)}\) commutes with every tensor-position
permutation and every averaging idempotent. In particular it preserves
both nested symmetric powers and commutes with \(h_{b,a}\). On the target
it is orthogonal projection onto the line spanned by \(I_{a,b}\).
Character orthogonality gives this projector formula, and R-001 supplies
the target multiplicity one. Therefore

\[
 h_{b,a}(e_{(b^a)}m_a^b)
   =e_{(b^a)}h_{b,a}(m_a^b)
   =\frac{q_{a,b}}{N_{a,b}}I_{a,b}.
\]

The scalar \(q_{a,b}\) is nonzero by (R-008a). Multiplication by the
factor in (B5) proves (R-008b). Thus the proof identifies the particular
canonical morphism and an explicit source vector.

## R-009. Products and first-row extensions below the full bound

For every odd prime \(p\), \(2\le a\le p-1\), \(t\ge1\), and
\(s\ge0\), set

\[
 b=t(p-1)+s,\qquad
 \lambda=(as+t(p-1),\;\underbrace{t(p-1),\ldots,t(p-1)}_{a-1}).
\]

The following source and image are explicit:

\[
 \boxed{
 h_{b,a}\bigl(u_{a,p}^{\,t}(e_1^a)^s\bigr)
   =I_{a,t(p-1)}(e_1^{\otimes a})^s\ne0.
 }
 \tag{R-009a}
\]

Both sides are highest weight vectors of weight \(\lambda\). Moreover

\[
 [S_\lambda V:\operatorname{im}h_{b,a}]
   =[S_\lambda V:\operatorname{Sym}^a(\operatorname{Sym}^bV)]=1
 \tag{R-009b}
\]

in every ambient dimension at least \(a\).

### Proof

The image equality follows by applying the algebra morphism (B1), using
(R-008b), (B4), and \(\mu_a(e_1^a)=e_1^{\otimes a}\). Evaluation on
\(a\) covectors gives the nonzero polynomial

\[
 \det(X)^{t(p-1)}\prod_{j=1}^a x_{1j}^{s}.
\]

This proves the asserted nonvanishing without a cancellation assertion.
The determinant vector is highest weight of weight \((t(p-1)^a)\);
the added factor has weight \((as)\) and is killed by the upper triangular
raising operators. The same is true of the source vector (B5), which
lies in a determinant representation over \(\mathbb C^a\). Embedding
\(\mathbb C^a\subseteq V\) gives highest weight vectors in every larger
ambient space, since the additional raising operators differentiate basis
directions absent from these tensors.

For the target multiplicity, set \(\ell=t(p-1)\). The inner-degree
lifting map \(\kappa^a_{\ell,b}\), obtained by multiplying each inner
factor by \(e_1^s\), maps the unique highest weight vector of weight
\((\ell^a)\) to the displayed image. BIP Proposition 5.6(1) applies
because the second part of \((\ell^a)\) is \(\ell\). It identifies the
two highest weight spaces. Howe Proposition 4.3, equivalently R-001,
gives dimension one because \(\ell\) is even. This proves (R-009b).

### Actual boundary families and examples

For each prime \(p\equiv1\pmod4\), \(p\ge13\), put

\[
 a=(p-1)/2,\qquad t=(a-2)/2,\qquad s=0.
\]

Then \(a\) is even, and (R-009) proves the entire determinant component
at

\[
 b=t(p-1)=a(a-2)=(a-1)^2-1.
 \tag{B9}
\]

Examples are \((a,b)=(6,24),(8,48),(14,168),(18,288),(20,360),
(26,624),(30,840)\). The case \(a=26\) uses \(p=53\) and \(t=12\);
its base rectangle has width \(52\).

Boundary examples in odd outer degree are obtained with \(t=1\) and
positive \(s\). For \((a,b,p)=(7,35,31)\), the image has its unique
component \(S_{(65,30^6)}V\). For \((a,b,p)=(9,63,61)\), the image has
its unique component \(S_{(87,60^8)}V\). The degree sums are respectively
\(65+6\cdot30=7\cdot35\) and \(87+8\cdot60=9\cdot63\).

The square scalar yields a second exact form. For every
\(n\in\{p-1,p+1:p\text{ odd prime}\}\) and \(k\ge1\),

\[
 h_{kn,n}(I_{n,n}^{\,k})=c_n^{\,k}I_{n,kn}\ne0.
 \tag{B10}
\]

This follows directly from R-002 and (B1). For \(n=6,k=4\), the scalar
is \(699840000^{-4}\), since \(c_6=-699840000^{-1}\). This verifies the
determinant component at \((a,b)=(6,24)\) by an explicit rational scalar.

## R-010. What the last common-power step proves at the boundary

Write \(r=a-1\), and consider the actual differential operator

\[
 \Psi_{r,b}=\prod_{i=1}^r(x\cdot\partial_{v_i})^r
\]

on polynomials initially independent of \(x\), separately of degree
\(b\) in each \(v_i\). Sra III Lemma 2.1 and the proof of Theorem 1.3
give its injectivity for \(b\ge r^2\). The supplement's Corollary S8.1
records the quantitative estimate; immediately after it, p. 36, the
author gives the example \(r=5,b=24\).

For every odd \(r\ge3\), put \(b=r^2-1\) and \(V=\mathbb C^r\). Then

\[
 f(v_1,\ldots,v_r)=\det(v_1,\ldots,v_r)^b
 \quad\text{is nonzero and symmetric,}\qquad \Psi_{r,b}f=0.
 \tag{R-010a}
\]

Indeed \(b\) is even, so the determinant power is symmetric. Every term
in the differentiated expression inserts \(r^2=b+1\) copies of the
same vector \(x\) into \(b\) determinant factors. A determinant receiving
two copies of \(x\) vanishes, and every term has such a factor. For even
\(r\), the same determinant polynomial is alternating because \(b\)
is odd. Thus its projection to the symmetric \(r\)-slot input is zero.
This last parity calculation does not classify the other kernel
components.

The arbitrary-common-power full-tensor kernel admits nonrectangular
components. A concrete example of the analogous operator with \(r=3\), power one, and input degree two per slot has an
additional kernel vector on \(V=\mathbb C^2\). Write
\([ij]=x_i y_j-y_i x_j\) and set

\[
 g=[12][13][23].
\]

It has degree two in each vector and transforms by the sign of the slot
permutation. Under \(v_i\mapsto v_i+t_i x\), each bracket is at most
linear in the \(t_i\), and direct expansion gives

\[
 [t_1t_2t_3]\,
 [v_1+t_1x,v_2+t_2x]
 [v_1+t_1x,v_3+t_3x]
 [v_2+t_2x,v_3+t_3x]=0.
 \tag{R-010b}
\]

The two possible terms are
\(-[x,v_2][x,v_3][x,v_1]\) and
\(+[x,v_1][x,v_2][x,v_3]\), which cancel. The vector has
\(\operatorname{GL}_2\)-weight \((3,3)\), whereas the height-three
rectangle of degree two vanishes on \(\mathbb C^2\). This is an exact
counterexample to a uniform rectangular-kernel classification across
arbitrary common powers. It does not
decide the symmetric-input kernel at \(r\) even and power \(r\).

The current proof does not establish full canonical-map surjectivity at
\(b=(a-1)^2-1\) for general odd \(a\). The unconditional improvements in
this report are the specified canonical-map components (R-008--R-009).

## Independent finite coefficient checks

Let \(D_E=[X^E]\operatorname{per}(X)^b\). The coefficient of
\(\prod_{i,j}z_{ij}\) in \(\prod_iP_{E_i}\), after
\(P=\prod_{j=1}^b\ell_j\), is \(D_E\): each of its \(b\) columns
assigns the \(a\) symbols bijectively to the \(a\) tensor rows, and
the resulting row multiplicities are \(E\). Combining this with (B7)
and its \((a!)^b\) squarefree coefficient gives

\[
 q_{a,b}=
 \frac{\sum_E C_ED_E\prod_{i,j}e_{ij}!}
      {(a!)^b(b!)^a}.
 \tag{B11}
\]

The numerator is the Fischer pairing of the determinant power and
permanent power. The program verify_prime_blocks.py computes their
coefficient tables by exact monomial multiplication, checks (B6) at
every exponent matrix, and evaluates (B11). It imports no source-paper
implementation.

| \(a\) | \(b=p-1\) | Exponent matrices checked | Exact \(q_{a,b}\) |
|---:|---:|---:|---:|
| 2 | 2 | 3 | \(1/4\) |
| 2 | 4 | 5 | \(1/16\) |
| 3 | 4 | 120 | \(1/1296\) |
| 3 | 6 | 406 | \(1/87480\) |
| 4 | 4 | 10147 | \(1/331776\) |
| 3 | 10 | 2211 | \(1/88179840\) |
| 3 | 12 | 4186 | \(281/838061199360\) |

All seven residues are one modulo the indicated prime. The two square
cases also equal \(c_a^2\), using the independently enumerated Latin
scalars in rectangular_report.md. The nondivisible case \((a,b)=(3,4)\)
checks that the general coefficient argument does not require \(a\mid b\).

## Source audit and exact locators

* Suvrit Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a
  graded inner factor*, v1, Theorem 1.3, Lemma 2.1, and §2.2, pp. 3--5.
  Author's repository: <https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes3/v1/qfoulkes3-v1.pdf>.
* Sra, *Supplement to the q-Foulkes project*, S8, p. 36, Corollary S8.1
  and its following paragraph. Author's repository:
  <https://github.com/suvrit/preprints/blob/main/preprints/qfoulkes3/v1/qfoulkes3-v1-supplement.pdf>.
* David G. Glynn, *The conjectures of Alon--Tarsi and Rota in dimension
  prime minus one*, SIAM J. Discrete Math. **24** (2010), 394--399,
  Theorems 3.1--3.2 and the definition immediately before Theorem 3.1.
  DOI: <https://doi.org/10.1137/090773751>.
  The author's full manuscript was read through its publicly indexed
  transcript at <https://www.academia.edu/25562085/The_Conjectures_of_Alon_Tarsi_and_Rota_in_Dimension_Prime_Minus_One>.
* Arthur A. Drisko, *On the number of even and odd Latin squares of order
  p+1*, Adv. Math. **128** (1997), 20--35, Theorem 9, pp. 33--34.
  Publisher record:
  <https://www.sciencedirect.com/science/article/pii/S0001870897916236>.
  The original article's full transcript, including its page numbers,
  was read at <https://studyres.com/doc/19593200/on-the-number-of-even-and-odd-latin-squares-of>.
* The 1998 assertion extending prime cases by powers of two is not used.
  Glynn's introduction explicitly identifies the error in the preceding
  doubling argument. No such enlargement is included in these parameter
  families.
* Howe Proposition 4.3 and BIP Proposition 5.6(1) are located and checked
  in rectangular_report.md, R-001 and R-005.


# Two exact symmetric common-polarization kernels

Statement ID **R-011**. Written and checked on 2026-11-20 UTC by GPT-6 Astra Pro, agent `/root/rectangular_cases`; the inherited effort setting is not exposed. The statements below are finite, unconditional computational theorems. They do not assert a classification at arbitrary parameters.

## The actual maps and results

For a complex vector space $V$, use four separately homogeneous vector slots $v_1,\ldots,v_4$, of degree $b$ each, and an additional vector slot $x$. Define the natural linear map

\[
\begin{gathered}
T_{L,b}:\operatorname{Sym}^4(\operatorname{Sym}^bV)
 \longrightarrow \operatorname{Sym}^{4L}V\otimes
 \operatorname{Sym}^4(\operatorname{Sym}^{b-L}V),
 \\
 T_{L,b}(f)=[t_1^L\cdots t_4^L]
 f(v_1+t_1x,\ldots,v_4+t_4x).
\end{gathered}
\]

Equivalently, $T_{L,b}=(L!)^{-4}\prod_{i=1}^4(x\cdot\partial_{v_i})^L$. The polynomial description means the canonical multihomogeneous tensor model; using coordinate functions replaces $V$ throughout by its dual and gives the same natural map after that explicit substitution. Permuting the four slots commutes with coefficient extraction. Consequently the displayed target has its stated fourth symmetric power. Each term has $x$-degree $4L$ and residual degree $b-L$ in every slot.

**Theorem R-011.** The two maps $T_{1,3}$ and $T_{2,7}$ are injective for every finite-dimensional complex vector space $V$.

Both parameters satisfy $b=4L-1$. The ranks were established on every source highest-weight multiplicity space, not inferred from source and target multiplicities.

| $L,b$ | Source dimension on $\mathbb C^4$ | Distinct source constituents | Sum of source multiplicities | Largest source multiplicity | Certified image rank on highest-weight spaces |
|---|---:|---:|---:|---:|---:|
| $1,3$ | 8,855 | 12 | 12 | 1 | 12 |
| $2,7$ | 9,078,630 | 173 | 319 | 6 | 319 |

This verifies the first two requested common-power boundary cases for four symmetric slots. It supplies finite evidence relevant to, but no theorem about, the general even-$r$ boundary $\prod_{i=1}^r(x\cdot\partial_{v_i})^r$ at $b=r^2-1$. The actual case $r=L=4,b=15$ is now separately proved and independently certified as R-012 in polarization_r4_boundary_and_geometry.md.

## Complete proof by exact certificates

### 1. Reduction to multiplicity spaces in dimension four

The source is the invariant part of $(\operatorname{Sym}^b V)^{\otimes4}$ under permutation of its four factors. Iterated Pieri multiplication of four one-row Schur characters has at most four rows: adding a horizontal strip to a diagram with $k$ rows creates at most one additional row. Hence every source Schur functor is $S_\lambda V$ with $\ell(\lambda)\le4$.

The construction of $T_{L,b}$ uses permutations, symmetrizations and contraction of slot labels in tensor powers, so its matrices on the multiplicity spaces of the Schur functors are independent of $\dim V$ once $\dim V\ge4$. This can also be seen by the tensor model $V^{\otimes4b}$: the same element of the rational permutation algebra acts on each $V^{\otimes4b}$, and Schur–Weyl decomposition identifies its multiplicity matrices with matrices between the corresponding fixed symmetric-group modules. Since every source $S_\lambda\mathbb C^4$ is nonzero, injectivity for $V=\mathbb C^4$ proves injectivity for every dimension at least four. Inclusion of a smaller $V$ in $\mathbb C^4$ and the naturality square proves it for dimensions below four.

Over $\mathbb C$, a nonzero kernel of a $GL_4$-equivariant map contains an irreducible summand and hence a nonzero highest-weight vector. It therefore suffices to exhibit, for each source highest weight $\lambda$, exactly its source multiplicity many vectors with linearly independent images.

### 2. Exact source multiplicities, checked by two constructions

Let $W_b$ be the set of all quadruples of nonnegative integers summing to $b$. The coefficient $M(\alpha)$ of the weight $\alpha$ in the source character is exactly the number of unordered multisets of four elements of $W_b$ having sum $\alpha$. This follows directly by choosing the monomial basis of $\operatorname{Sym}^b\mathbb C^4$ and then its degree-four monomial basis. With $\rho=(3,2,1,0)$, the multiplicity of $S_\lambda\mathbb C^4$ equals

\[
 m_\lambda=\sum_{\sigma\in S_4}\operatorname{sgn}(\sigma)
 M(\lambda+\rho-\sigma\rho).
\]

To derive the formula, multiply the Schur-character expansion by $\prod_{i<j}(1-x_j/x_i)$. The Weyl alternant formula turns $s_\mu$ into the signed orbit of $\mu+\rho$, translated by $-\rho$. The coefficient at a dominant $\lambda$ is $1$ for $\mu=\lambda$ and $0$ otherwise because $\mu+\rho$ is strictly decreasing and has a unique dominant permutation.

The producer `polarization_candidates.py` obtains $M$ from Newton's exact recurrence $h_i=i^{-1}\sum_{k=1}^i h_{i-k}p_k$, where $p_k=\sum_{\alpha\in W_b}x^{k\alpha}$. The C++ verifier independently enumerates all unordered four-multisets of $W_b$, with no use of Newton's recurrence, and recomputes every required $m_\lambda$. It checks equality with the supplied table in each block. The producer also checks

\[
 \sum_\lambda m_\lambda\prod_{1\le i<j\le4}
 \frac{\lambda_i-\lambda_j+j-i}{j-i}
 =\binom{\binom{b+3}{3}+3}{4}.
\]

All partitions of $4b$ of length at most four are enumerated, so zero source multiplicities are included in the extraction process. The resulting positive-multiplicity lists and dimensions are those in the table above.

### 3. Explicit integral highest-weight vectors in the source

Use a $4\times4$ variable matrix $X$, whose columns are the slots $v_i$. For a nonempty subset $I\subseteq\{1,2,3,4\}$, let $d_I(X)$ be the determinant of the submatrix with the first $|I|$ rows and the columns $I$, in increasing order. There are fifteen such flag minors. A product

\[
 F_c(X)=\prod_{I\ne\varnothing}d_I(X)^{c_I}
\]

has highest weight $\lambda_i=\sum_{|I|\ge i}c_I$, and its degree in slot $j$ is $\sum_{I\ni j}c_I$. The highest-weight assertion follows explicitly by applying a raising operator: replacing a row indexed $j\le |I|$ by an earlier row creates two equal rows in its determinant; a row $j>|I|$ is absent. Thus every raising operator annihilates every factor and hence the product.

For each tableau of shape $\lambda$ with content $(b,b,b,b)$, its columns give such a product with slot degrees $b$. The producer sums its twenty-four slot permutations, including the signs caused by sorting the columns within each determinant. Dividing all integral coefficients by their common divisor gives a nonzero integral symmetric highest-weight vector, or the zero sum is discarded. It removes repeated resulting coefficient lists. The input files record each remaining vector as an explicit integer linear combination of the fifteen-minor monomials. No claim that these lists form a basis is needed: exhibiting $m_\lambda$ independent images already suffices.

The independent checker verifies the weight and all four degrees of every recorded monomial. A separate independent adjacent-transposition check verifies that each selected vector is fixed by the three generators of $S_4$; it uses the explicit determinant signs rather than the producer's permutation table. It passed on all 12 and 319 selected vectors respectively.

### 4. Exact image evaluation and a nonzero integer minor

Work modulo the prime $P=1,000,003$. Each certificate includes its integral evaluation points $X,x$, its selected candidate indices, the selected evaluation rows, the entire square evaluation matrix, and its nonzero determinant modulo $P$. The points were chosen by a fixed deterministic generator; the proof depends only on the printed points and their nonzero determinants.

For every flag minor,

\[
 d_I(v_1+t_1x,\ldots,v_4+t_4x)
 =d_I(X)+\sum_{j\in I}t_jd_{I,j}(X,x),
\]

where $d_{I,j}$ replaces column $j$ by $x$. Terms involving two $t$'s vanish because two columns are then equal to $x$. Multiplying these explicitly linear polynomials, truncating each $t_i$-exponent above $L$, and reading coefficient $(L,L,L,L)$ therefore evaluates exactly $T_{L,b}(F_c)$. Truncation cannot affect that coefficient because all exponents are nonnegative. The calculation then adds the candidate's signed integral terms.

The C++ program finds a nonsingular $m_\lambda\times m_\lambda$ submatrix in every block, prints all entries and verifies its determinant. A matrix of integral polynomial evaluations with nonzero determinant modulo a prime has a nonzero integer determinant. Hence the corresponding image polynomials are linearly independent over $\mathbb Q$ and over $\mathbb C$. All source multiplicity spaces are thus injective, proving R-011.

### 5. Independent entry-by-entry recheck

`recheck_polarization_certificates.py` never calls the C++ evaluator. It computes the small flag determinants by recursive Laplace expansion, and computes Taylor coefficients using four-dimensional NumPy arrays and axis shifts. It recomputes every entry of every selected square matrix, compares with the certificate, and recomputes each selected determinant by Laplace expansion. All selected determinants have size at most six. Integer intermediates in each array step are bounded by $5(P-1)^2<2^{63}$, so the `int64` operations are exact before reduction.

The independent receipt is:

```
POLARIZATION_R4_L1_B3: PASS; 12 blocks; 12 independently recomputed entries; 95 Taylor evaluations
POLARIZATION_R4_L2_B7: PASS; 173 blocks; 787 independently recomputed entries; 13865 Taylor evaluations
```

The prime was independently checked by exact primality testing. The calculations use no probabilistic inference: randomness only selected points, and every determinant value is an exact certificate.

## Reproduction and artifact inventory

Run from this directory:

```
python polarization_candidates.py
g++ -O3 -std=c++17 check_polarization_ranks.cpp -o check_polarization_ranks
./check_polarization_ranks POLARIZATION_R4_L1_B3.input
./check_polarization_ranks POLARIZATION_R4_L2_B7.input
python recheck_polarization_certificates.py
```

The two `.tsv` tables list the exact source and target multiplicities and candidate counts. The two `.input` files specify all candidate polynomials. The `_RANKS.tsv` files list every achieved rank and determinant. The `_CERTIFICATES.txt` files give all points, selected candidates and square matrices. `POLARIZATION_INDEPENDENT_RECHECK.txt` records the independent entry-by-entry checks. These files, the source code and this proof together provide a finite certificate of R-011.

The source of the motivating general polarization bound and determinant obstruction is Sra, *The q-Foulkes problem III: On Foulkes’ conjecture with a graded inner factor*, Theorem 1.3 and supplement S8, p. 36, audited in `boundary_and_prime_blocks.md`, R-010. R-011 is a finite computation of these explicit maps; it does not attribute its rank calculation to that source or claim a literature priority search.


# The actual four-slot boundary and its coordinate-ring morphism

Statements **R-012** and **R-013**. Completed and independently checked on 2026-11-20 UTC by GPT-6 Astra Pro, agent /root/rectangular_cases; inherited effort setting not exposed.

## R-012. The finite boundary map

For every finite-dimensional complex vector space \(V\), the natural map

\[
\begin{gathered}
T_{4,15}:\operatorname{Sym}^4(\operatorname{Sym}^{15}V)
 \longrightarrow
 \operatorname{Sym}^{16}V\otimes
 \operatorname{Sym}^4(\operatorname{Sym}^{11}V),
 \\
 f\longmapsto[t_1^4t_2^4t_3^4t_4^4]\,
 f(v_1+t_1x,\ldots,v_4+t_4x)
\end{gathered}
\]

is injective. This is the actual common-power boundary \(r=L=4,\ b=r^2-1=15\). Multiplication by \((4!)^4\) gives the undivided differential operator \(\prod_i(x\cdot\partial_{v_i})^4\), with the same kernel.

### Complete proof

The dimension reduction and flag-minor highest-weight construction are proved in full in R-011, sections 1–4 of polarization_boundary_report.md. They apply unchanged here: the source has only partitions of length at most four, the tensor permutation map has dimension-independent multiplicity matrices, and a nonzero equivariant kernel would contain a highest-weight vector. The following exhaustive finite certificate proves that every source multiplicity space maps injectively.

The exact source character has **1,713** distinct constituents, highest-weight multiplicity sum **14,018**, maximum multiplicity **35**, and full representation dimension on \(\mathbb C^4\)

\[
 \dim\operatorname{Sym}^4(\operatorname{Sym}^{15}\mathbb C^4)
 =\binom{819}{4}=18,609,648,876.
\]

For each constituent \(\lambda\) of multiplicity \(m_\lambda\), the certificate provides \(m_\lambda\) integral symmetric highest-weight polynomials, specified as signed sums of products of the fifteen flag minors. Their row weights and equal column degrees are verified directly. Invariance under the three adjacent slot transpositions is verified directly, including all determinant signs. The certificate then gives \(m_\lambda\) evaluation points and the full square evaluation matrix of their images under \(T_{4,15}\).

Every one of those 1,713 square matrices has a nonzero determinant modulo the prime \(1,000,003\). In particular, every determinant is a nonzero integer. Its columns are therefore linearly independent over \(\mathbb Q\), and hence over \(\mathbb C\). Thus the map is injective on every highest-weight multiplicity space. The highest-weight argument proves injectivity for \(\mathbb C^4\), and the dimension-independent tensor permutation argument proves it for all \(V\).

The certificate is exhaustive in the following independently verified sense.

1. The source multiplicities were first extracted from the exact Newton recurrence for \(h_4[h_{15}]\). A separate C++ program, verify_boundary_character.cpp, independently computes

   \[
   [t^4]\prod_{\substack{\alpha\in\mathbb Z_{\ge0}^4\\|\alpha|=15}}
   (1-tx^\alpha)^{-1}
   \]

   by multiplying the 816 individual geometric-series factors. It applies the Weyl alternant to every partition of 60 of length at most four, and obtains exactly the same positive multiplicities. Its Weyl-dimension sum and sum of all monomial weight coefficients both equal 18,609,648,876.

2. The original evaluator expands each shifted flag minor as its constant term plus its four possible linear terms, then uses forward coefficient propagation and modular Gaussian elimination.

3. A separately written evaluator, recheck_large_polarization.cpp, recomputes **all 203,840 entries** of the selected square matrices. It processes the flag-minor factors in reverse order, uses descending in-place coefficient recurrence instead of forward propagation, and independently computes every small determinant and selected matrix determinant by power traces and Newton identities. It also checks every selected polynomial's highest weight, four slot degrees, and exact invariance under the three generators of \(S_4\).

For clarity, the independent coefficient recurrence replaces a current coefficient array \(c_\alpha\), in descending index order, by

\[
 c_\alpha\ \leftarrow\
 d\,c_\alpha+\sum_{j=1}^4a_jc_{\alpha-e_j}
 \pmod {1,000,003}
\]

for each linear minor factor \(d+\sum_j a_jt_j\), retaining only \(0\le\alpha_j\le4\). Descending order guarantees that every referenced lower index still has its old value. Truncation cannot change the target coefficient because exponents are nonnegative. The determinant recheck uses

\[
 e_0=1,\qquad
 e_k=\frac1k\sum_{i=1}^k(-1)^{i-1}e_{k-i}\operatorname{tr}(A^i),
 \qquad\det A=e_m,
\]

for an \(m\times m\) matrix. Here \(m\le35<1,000,003\), so every division by \(k\) is valid. All products and unreduced sums fit signed 64-bit integers: the largest matrix-product sums have at most 35 terms, each smaller than \(1,000,003^2\).

The independent run made 4,517,197 Taylor evaluations, checked all 14,018 selected vectors, and passed every entry and determinant. The underlying finite-field modulus is checked by trial division. Consequently no probabilistic assertion enters the proof; the point generator merely supplied the printed points.

### Compact certificate

The file POLARIZATION_R4_L4_B15_SELECTED.compact.gz contains the complete selected source polynomials, points, matrices and determinants. Its uncompressed size is 11,569,652 bytes; compressed size is 2,761,977 bytes. Its SHA256 is

~~~
fa2bbbeb5e335d08cda726359ac2b1ffaf1fe1270bba56e3f29841b9957db107
~~~

The character table is POLARIZATION_R4_L4_B15.tsv. The rank summary is POLARIZATION_R4_L4_B15_ALL_RANKS.tsv. The independent receipt is POLARIZATION_R4_L4_B15_INDEPENDENT_RECHECK.txt. The complete full-candidate input and parallel batches are intermediate files; they are unnecessary for checking the selected certificate.

To recheck the selected certificate, decompress the gzip file, compile `recheck_large_polarization.cpp` with C++17 and optimization, and pass the resulting compact file as its sole argument. Compile `verify_boundary_character.cpp` and pass `POLARIZATION_R4_L4_B15.tsv` to recheck the source multiplicities independently. The compressed certificate contains only selected vectors, so the 124 MB full candidate input is not needed.

No priority claim is made for this finite rank computation. The supplied proof establishes this map and these parameters, without a classification for larger even numbers of slots.

## R-013. Exact morphism to the variety of padded forms

The coordinate-ring description is a known generalized Foulkes–Howe construction. A precise primary locator is Kadish–Landsberg, *Padded polynomials, their cousins, and geometric complexity theory*, **Theorem 1.7**, p. 3, with the full tensor construction and evaluation proof in **section 3, pp. 5–6**:

https://arxiv.org/pdf/1204.4693

The published article is *Communications in Algebra* 42 (2014), 2171–2180, DOI 10.1080/00927872.2012.758268. The statement and proof in the cited arXiv version were read in this run. The following proof fixes the exact scalar relating that coordinate-ring map to the coefficient-extraction operator used in our certificates.

Let \(r\ge1\), \(b\ge1\), and \(0\le L\le b\). Fix the normalized perfect pairing on symmetric powers by

\[
 \langle v^k,\ell_1\cdots\ell_k\rangle
 =\prod_{j=1}^k\ell_j(v).
\]

Define the polynomial morphism

\[
 \nu_{L,b}:V^*\times\operatorname{Sym}^{b-L}V^*
 \longrightarrow\operatorname{Sym}^bV^*,
 \qquad(\ell,q)\longmapsto\ell^Lq.
\]

Its pullback in coordinate degree \(r\) is

\[
 (\nu_{L,b}^*)_r:
 \operatorname{Sym}^r(\operatorname{Sym}^bV)
 \longrightarrow
 \operatorname{Sym}^{rL}V\otimes
 \operatorname{Sym}^r(\operatorname{Sym}^{b-L}V).
\]

Define \(T_{r,L,b}\) by extracting \(t_1^L\cdots t_r^L\) after substituting \(v_i+t_ix\) in the symmetric \(r\)-slot model. Then the exact equality is

\[
 \boxed{\displaystyle
 (\nu_{L,b}^*)_r=\binom bL^{-r}T_{r,L,b}.}
 \tag{R013.1}
\]

**Proof.** Products \(w_1^b\cdots w_r^b\) span \(\operatorname{Sym}^r(\operatorname{Sym}^bV)\), because pure powers span each symmetric power. As a coordinate polynomial, such a product sends \(P\) to \(\prod_i\langle w_i^b,P\rangle\). Its pullback along \(\nu_{L,b}\) is

\[
 \prod_i\ell(w_i)^L
 \prod_i\langle w_i^{b-L},q\rangle.
\]

This is represented in the displayed target by

\[
 (w_1^L\cdots w_r^L)\otimes
 (w_1^{b-L}\cdots w_r^{b-L}).
\]

The symmetric-slot representative of the original product is the average over all assignments of the \(w_i\) to the \(r\) slots. In each assigned row the binomial theorem gives the factor

\[
 [t_i^L]\langle w,v_i+t_ix\rangle^b
 =\binom bL\langle w,x\rangle^L
 \langle w,v_i\rangle^{b-L}.
\]

Multiplying the \(r\) factors and taking the same slot average therefore gives \(\binom bL^r\) times the tensor above. Equality on a spanning set proves (R013.1).

Let \(Z_{L,b}(V)\) be the Zariski closure of the image of \(\nu_{L,b}\). A homogeneous polynomial vanishes on that image precisely when its pullback is zero; vanishing on the image and its closure are equivalent by the definition of Zariski closure. Thus

\[
 \boxed{\displaystyle
 I_r(Z_{L,b}(V))
 =\ker(\nu_{L,b}^*)_r
 =\ker T_{r,L,b}.}
 \tag{R013.2}
\]

Moreover the maps \(\binom bL^{-r}T_{r,L,b}\), as \(r\) varies, are the graded pieces of the one algebra homomorphism \(\nu_{L,b}^*\). This identifies their multiplication exactly, including the normalization.

### Actual geometric corollaries

Combining R-011 and R-012 with (R013.2) gives, for every finite-dimensional complex \(V\),

\[
 I_4(Z_{1,3}(V))=
 I_4(Z_{2,7}(V))=
 I_4(Z_{4,15}(V))=0.
\]

The homogeneous ideals in all degrees \(0\le d\le4\) are zero as well. Indeed, a nonzero equation of smaller positive degree could be multiplied by a nonzero polynomial to degree four in the ambient polynomial coordinate ring, which is an integral domain; the product would contradict the displayed vanishing. Degree zero contains no equation because each image contains the origin. When the ambient vector space is zero-dimensional, the assertion follows directly from its coordinate ring.

These are explicit low-degree assertions for the varieties of forms \(\ell q\) of degree 3, \(\ell^2q\) of degree 7, and \(\ell^4q\) of degree 15. They give a geometric interpretation of the verified finite kernels, with the complete morphism and scalar proved above.


# Source-relative endpoint proof check

ID T-015; run GCT_PLETH-20261121-theta. This observation is included as a checked comparison with a source, not as a new best global bound.

The full proof in `work/external/quadratic_stabilization_2026.tex`, sections 2–4, lines 178–436, was read, including its diagonal-annihilator criterion, Fischer inner-product lemma, and four-step induction.

For `a>=3`, set `r=a-1` and `b=a(a-1)-1=r(r+1)-1`. The residual symmetric degree is `m=b-r=r^2-1`. Source Step 2 still has `p-q=m-i+1>=1` for every derivative insertion. In Step 3, `m=r^2-1>=r(r-1)` and `m>=1`, so the source's original Proposition 3 for `r` slots applies; no stronger induction claim is assumed. In Step 4 the shared destination degree is at most `r^2-1`, while the source degree before each derivative is at least `b-r+1=m+1=r^2`, so the injectivity inequality remains strict. The final multilinear spanning step is unchanged.

Thus the source proof also gives surjectivity of `h_{b,a}` at the one-lower endpoint; its original theorem covers all larger `b`. At `a=2,b=1` the map is the identity under the canonical symmetric-power identifications. The parent agent found a stronger recent bound and is separately checking it; this event does not certify that other paper.


# Prime-adjacent square blocks, specialization, and exact canonical-image semigroups

## G-013. Explicit determinant and padded-rectangle image ranges

Work over \(\mathbf Q\), with the normalized symmetric-tensor and canonical-map conventions of R-001, R-002, and R-008. For an integer \(a\ge2\), let
\[
\begin{gathered}
\mathcal B_a=\{b\ge a: b\text{ even},\ b-1\text{ or }b+1\text{ an odd prime}\},\\
\mathcal S_a=\left\{\sum_{b\in\mathcal B_a}n_b b:n_b\in\mathbf N,
\text{ finitely many }n_b\ne0\right\}.
\end{gathered}
\tag{P.1}
\]
Every \(B\in\mathcal S_a\) has a rational, explicitly constructed preimage of the determinant tensor \(I_{a,B}\) under the actual canonical map
\[
 h_{B,a}:\operatorname{Sym}^B(\operatorname{Sym}^a W)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^B W),\qquad \dim W=a.
\tag{P.2}
\]
In particular its rank on the target \((B^a)\) determinant component is one. For every integer \(s\ge0\), multiplication of the constructed preimage by \((e_1^a)^s\) gives a nonzero image of highest weight
\[
 (as+B,B^{a-1})
\quad\text{under}\quad h_{B+s,a}.
\tag{P.3}
\]
The target multiplicity of this weight is exactly one. These component statements hold in every ambient dimension at least \(a\), by the displayed subspace inclusion and highest-weight vector.

The set \(\mathcal S_a\) is cofinite among the even integers. More explicitly, for every odd prime \(p>a\),
\[
 B\text{ even},\qquad B\ge \frac{(p-1)(p-3)}2
 \quad\Longrightarrow\quad B\in\mathcal S_a.
\tag{P.4}
\]
This is an established range with an explicit preimage; no distributional assertion about primes is used in its proof. An ordinary prime search supplies a suitable \(p\).

For the ranks \(2\le a\le100\), the attached finite Apéry certificates determine the entire semigroup \(\mathcal S_a\), using only the widths \(a\le b\le4a\) in (P.1). The exact even conductor \(C_a\) means that every even \(B\ge C_a\) belongs to \(\mathcal S_a\), and, for \(C_a>0\), the even integer \(C_a-2\) does not. It describes precisely this constructed seed semigroup; a degree outside it may still have a nonzero canonical determinant block by another construction.

| Rank \(a\) | Exact even conductor \(C_a\), both prime-adjacent seeds | Prime-minus-one seeds alone | Known full-map surjectivity bound \((a-1)^2\) |
|---:|---:|---:|---:|
| 2 | 0 | 0 | 1 |
| 3 | 4 | 4 | 4 |
| 4 | 4 | 4 | 9 |
| 5 | 6 | 16 | 16 |
| 6 | 6 | 16 | 25 |
| 7 | 8 | 16 | 36 |
| 8 | 8 | 16 | 49 |
| 9 | 10 | 16 | 64 |
| 10 | 10 | 16 | 81 |
| 12 | 12 | 28 | 121 |
| 16 | 28 | 28 | 225 |
| 20 | 36 | 56 | 361 |
| 26 | 52 | 64 | 625 |
| 32 | 58 | 92 | 961 |
| 50 | 96 | 116 | 2401 |
| 64 | 126 | 148 | 3969 |
| 100 | 190 | 196 | 9801 |

The last column is Sra III, Theorem 1.3, with its complete proof read in this run. It concerns every target component and is included only with that larger scope. The first columns certify the specified determinant and row-extended determinant components.

### 1. The exact square-to-smaller-rank pullback

Let \(b\) be one of the even square orders with \(c_b\ne0\), where R-002 defines the normalized scalar by
\[
 h_{b,b}(I_{b,b})=c_b I_{b,b}.
\tag{P.5}
\]
Take \(2\le a\le b\). Choose a decomposition
\[
 U^*=W^*\oplus\langle z_{a+1},\ldots,z_b\rangle,\qquad \dim U=b,
\]
and the actual linear multiplication map
\[
 j:\operatorname{Sym}^a W^*\longrightarrow\operatorname{Sym}^b U^*,
 \qquad F\longmapsto Fz_{a+1}\cdots z_b.
\tag{P.6}
\]
Let \(\Pi_a:(W^*)^a\to\operatorname{Sym}^a W^*\) and \(\Pi_b:(U^*)^b\to\operatorname{Sym}^b U^*\) multiply their ordered linear forms. The affine map \(\iota\) appends the fixed forms \(z_{a+1},\ldots,z_b\). Then
\[
 j\circ\Pi_a=\Pi_b\circ\iota.
\tag{P.7}
\]
Taking the degree-\(b\) coordinate pullbacks gives the commutative equality
\[
 h_{b,a}\circ\operatorname{Sym}^b(j^*)
 =\iota^*\circ h_{b,b}.
\tag{P.8}
\]
Here \(j^*\) is the dual linear map. The usual perfect characteristic-zero symmetric pairings identify it with a map \(\operatorname{Sym}^b U\to\operatorname{Sym}^a W\); its coefficients are determined by this duality. Thus all binomial factors of a monomial tensor basis are included by the defined map, without an implicit rescaling.

The normalized tensor \(I_{b,b}\) represents the polynomial \(\det_b(\ell_1,\ldots,\ell_b)^b\) on the ordered linear forms. Substituting the appended basis forms gives a block matrix with an identity complement, so
\[
 \iota^*(I_{b,b})=I_{a,b}.
\tag{P.9}
\]
Consequently the explicit rational vector
\[
 u_{a,b}=\operatorname{Sym}^b(j^*)\left(\frac{I_{b,b}}{c_b}\right)
 \quad\text{satisfies}\quad h_{b,a}(u_{a,b})=I_{a,b}.
\tag{P.10}
\]
The map \(j\) commutes with the block inclusion \(GL(W)\to GL(U)\); therefore \(u_{a,b}\) has determinant character \(\det_W^b\). Equation (P.10) also proves its nonvanishing directly.

For \(b=p-1\), Glynn's Theorem 3.2, and for \(b=p+1\), Drisko's Theorem 9, give \(c_b\ne0\), with the exact rational normalizations and prime-adic valuations proved in R-007. Applying (P.10) proves every seed in \(\mathcal B_a\). R-008 gives an additional, sharper congruence and an alternative source vector for the minus-one seeds. We use these known square results with their exact locators and make no priority claim for this specialization consequence.

### 2. Multiplication gives the specified preimages

R-008's map
\[
 \mu_a:\operatorname{Sym}(\operatorname{Sym}^a W)
 \longrightarrow \bigoplus_{d\ge0}\operatorname{Sym}^a(\operatorname{Sym}^d W)
\]
is a graded algebra morphism; its degree-\(d\) component is \(h_{d,a}\). Its target multiplication is componentwise multiplication in the \(a\) tensor factors. The determinant tensors satisfy
\[
 I_{a,b}I_{a,c}=I_{a,b+c}.
\tag{P.11}
\]
Evaluation on arbitrary \(a\) covectors proves this equality by the product \(\det^b\det^c=\det^{b+c}\), and these evaluations separate the symmetric tensors. Hence, for any specified expression \(B=\sum n_b b\),
\[
 u_{a,B}:=\prod_b u_{a,b}^{n_b}
 \quad\text{satisfies}\quad h_{B,a}(u_{a,B})=I_{a,B}.
\tag{P.12}
\]
No linear independence of different seed expressions is claimed or needed.

For (P.3), multiply (P.12) by \((e_1^a)^s\). Its image is
\[
 I_{a,B}\,(e_1^s)^{\otimes a},
\tag{P.13}
\]
a nonzero polynomial on the ordered covectors. It is a highest-weight vector of weight \((as+B,B^{a-1})\): the first factor has determinant character and the second is the power of the highest line. The refined balanced-weight realization T-002 identifies its target multiplicity with the invariant part of
\[
 \left(\det^B\otimes\operatorname{Sym}^{as}\mathbf Q^a\right)_{((B+s)^a)}.
\]
After removing the determinant factor, the only balanced monomial is \((x_1\cdots x_a)^s\), and its permutation character is \(\operatorname{sgn}^B=1\). Thus this multiplicity is exactly one. Appending zero weight coordinates under \(W\hookrightarrow V\) retains the same highest-weight vector, proving the ambient-dimension statement.

### 3. Cofiniteness and the explicit uniform range

For an odd prime \(p>a\), put \(g=(p-1)/2\). Both \(2g\) and \(2(g+1)\) lie in \(\mathcal B_a\). For each nonnegative \(N\), write \(r=N\bmod g\), \(0\le r<g\) (for \(g=1\), take \(r=0\)). The least nonnegative member of the semigroup \(\langle g,g+1\rangle\) with residue \(r\) is
\[
 w_r=r(g+1).
\tag{P.14}
\]
Indeed, in any expression \(ug+v(g+1)\), the second coefficient satisfies \(v\equiv r\pmod g\), and its smallest possible value is \(r\). Conversely \(w_r\) is represented. Every \(N\ge g(g-1)\) satisfies \(N\ge w_r\): the least integer at least \(g(g-1)\) in that residue is \(g(g-1)+r\), whose difference from \(w_r\) is \(g(g-1-r)\ge0\). Therefore
\[
 N=\frac{N-r(g+1)}g\,g+r(g+1)
\tag{P.15}
\]
has nonnegative integral coefficients. Multiplying by two gives (P.4), as well as an explicit two-factor construction in (P.12). The existence of arbitrarily large primes follows from Euclid's finite-product argument, so choosing \(p>a\) requires no unproved prime statement.

### 4. Exact finite semigroups by a residue graph

For a finite seed list \(2g_1,\ldots,2g_k\) with \(\gcd(g_1,\ldots,g_k)=1\), let \(g=\min g_i\). Make a directed graph on \(\mathbf Z/g\mathbf Z\), with an edge of weight \(g_i\) from \(r\) to \(r+g_i\). The residues generated by the \(g_i\) form the whole cyclic group: their subgroup has index the stated gcd, and the monoid they generate in a finite group is a group, since a positive multiple supplies each inverse. All edge weights are positive. Thus a shortest path from zero exists to every residue, and its length \(w_r\) is exactly the smallest nonnegative represented integer in that residue. The path itself records a seed expression.

For every integer \(N\ge0\), the exact membership equivalence is
\[
 N\in\langle g_1,\ldots,g_k\rangle
 \quad\Longleftrightarrow\quad N\ge w_{N\bmod g}.
\tag{P.16}
\]
The forward implication is minimality; the reverse adds copies of the generator \(g\). The greatest missing integer in residue \(r\) is \(w_r-g\), so the normalized conductor is
\[
 c=\max_r w_r-g+1.
\tag{P.17}
\]
For \(g=1\), this formula gives \(c=0\). These equalities also prove the shortest-path algorithm used in the attached code and explain precisely what its certificates certify.

The script `work/root/prime_semigroup.py` uses a direct sieve, enumerates every prime-adjacent width in \([a,4a]\), computes the shortest paths and their explicit integer witnesses, and then verifies all memberships through \(\max w_r+g+\max g_i\) by a separate Boolean recurrence \(D(N)=\bigvee_iD(N-g_i)\). It checks that all witnesses have the stated weights and residues. For every \(2\le a\le100\), it additionally verifies \(c\le2a\). Every omitted prime-adjacent width is greater than \(4a\); its half is therefore greater than \(2a\), and hence already belongs to the finite computed semigroup by (P.16). This proves that the finite list generates the entire \(\mathcal S_a\), without searching infinitely many primes. The same calculation and omission argument were checked for the minus-one lists displayed for comparison.

All 198 finite seed-set calculations passed. The complete data are in `PRIME_SEMIGROUP_RANGES.tsv` and `PRIME_SEMIGROUP_CERTIFICATES.json`, beside the reproducing script. The proof of the square specialization was independently checked through the commutative multiplication diagram by the rectangular agent. The whole proof and all computational checks receive separate events in the ledger.

### Scheme and representation-ring dictionary

The maps \(\Pi_a,\Pi_b,j,\iota\) are morphisms of affine schemes defined by integral coordinate polynomials. Equation (P.7) is equality of these actual scheme morphisms, and (P.8) is its contravariant equality on coordinate rings. The inverse scalar \(c_b^{-1}\) is taken over \(\mathbf Q\); after inverting its numerator and the finitely many symmetric-pairing denominators, the same preimage is defined over the resulting localization of \(\mathbf Z\). This identifies the base explicitly and makes no assertion of an integral inverse at an excluded prime. The nonzero image line is the coefficient of the Schur operation \(s_{(B^a)}\) in the image of the Chow coordinate morphism from G-003, equivalently the corresponding isotypic rank in \(K_0(\operatorname{Rep}_{\mathbf Q}GL_a)\). The tensor multiplication is the product in that representation algebra and in the graded scheme coordinate ring. The finite residue semigroup specifies a concrete finitely generated subalgebra of the canonical image through (P.12); it does not replace the entire coordinate ring by a numerical semigroup. The general SGA 3, SGA 6, EGA I, and FGA locators for these exact constructions are supplied in the dedicated dictionary part.


# An explicit canonical-map lift for every sufficiently long first row

## G-014. Degree-tracked multisymmetric lifting

Let \(a\ge2\), \(n\ge0\), and let \(V\) be a finite-dimensional characteristic-zero vector space. For every partition \(\lambda\vdash an\) with
\[
 d:=an-\lambda_1=\lambda_2+\lambda_3+\cdots\le n,
\tag{C.1}
\]
the canonical map
\[
 h_{n,a}:\operatorname{Sym}^n(\operatorname{Sym}^a V)
 \longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^n V)
\tag{C.2}
\]
is surjective on the entire target \(\lambda\)-isotypic component. For the empty partition we put \(\lambda_1=0\); the zero-dimensional ambient space is immediate. The proof gives a rational preimage for every target highest-weight vector by explicit coefficient extraction, Newton identities, and a finite sum over set partitions. Consequently the image multiplicity equals \(a_{a,n}^{\lambda}\) throughout (C.1). This includes all ambient dimensions: a Schur module whose partition exceeds the dimension is zero on both sides of this component assertion.

The elementary-multisymmetric coordinate chart is classical: Raicu–Sam–Weyman, *On some modules supported in the Chow variety*, Theorem 2.3, its proof (2.8), and Remark 2.9, printed pp.5–6, give the chart and its characteristic-zero invariant generators. The proof below tracks the ordinary number of generators as well as their polynomial weights, to supply the stated finite-degree lift and the exact canonical map. No priority claim is made for the resulting first-row range.

### 1. The actual coordinate morphism

Choose a basis of \(V\). Write the \(i\)-th linear form as
\[
 \ell_i=x_i t_1+\sum_{j=2}^{r}z_{ij}t_j,\qquad 1\le i\le a,
\]
and put \(u=\prod_i x_i\). On the principal open set \(u\ne0\), define \(w_{ij}=z_{ij}/x_i\). A target vector is a polynomial in the \(a\) ordered forms, homogeneous of degree \(n\) in each and invariant under permuting the forms. Any such polynomial of total degree \(d\) in the variables \(z_{ij}\), \(j\ge2\), has the unique expression
\[
 f=u^n F(w_{ij}),
\tag{C.3}
\]
where \(F\) is an \(S_a\)-invariant polynomial, homogeneous of degree \(d\). Indeed, in every monomial the exponent of \(x_i\) is \(n-\sum_{j\ge2}\deg_{z_{ij}}\); substituting \(z_{ij}=x_iw_{ij}\) gives exactly \(x_i^n\) in each row. Permutation invariance passes to \(F\) because \(u\) is invariant.

For a vector of auxiliary variables \(y=(y_2,\ldots,y_r)\), set \(L_i(y)=\sum_{j\ge2}w_{ij}y_j\) and
\[
 \prod_{i=1}^a(1+sL_i(y))
 =\sum_{j=0}^a E_j(y)s^j,
 \qquad E_j(y)=\sum_{|\beta|=j}E_\beta(w)y^\beta.
\tag{C.4}
\]
Let \(C_\beta\) denote the linear coordinate functional extracting the coefficient of \(t_1^{a-|\beta|}\prod_{j\ge2}t_j^{\beta_j}\) from an arbitrary degree-\(a\) form; let \(C_0\) extract \(t_1^a\). These are actual elements of \((\operatorname{Sym}^aV^*)^*\simeq\operatorname{Sym}^aV\), with the dual symmetric pairing specifying any monomial-basis factorials. Pullback under multiplication of the ordered forms gives
\[
 \mu_a(C_0)=u,
 \qquad \mu_a(C_\beta)=uE_\beta(w).
\tag{C.5}
\]
The homogeneous degree-\(n\) part of this algebra pullback is exactly (C.2), with the conventions of G-003 and R-008.

### 2. An explicit expression with at most \(d\) coefficient factors

We prove that every degree-\(d\) invariant \(F\) is a rational linear combination of monomials
\[
 \prod_{q=1}^k E_{\beta^{(q)}},
 \qquad \sum_q|\beta^{(q)}|=d,
 \qquad k\le d,
\tag{C.6}
\]
where all \(\beta^{(q)}\ne0\). The constant case \(d=0\) has \(k=0\).

For a nonzero exponent vector \(\alpha\), put \(P_\alpha=\sum_iw_i^\alpha\). Every invariant polynomial is a linear combination of monomial orbit sums. For a list of nonzero exponent vectors \(\alpha_1,\ldots,\alpha_k\), the distinct-row sum has the exact identity
\[
 \sum_{i_1,\ldots,i_k\ \mathrm{distinct}}
 \prod_{j=1}^k w_{i_j}^{\alpha_j}
 =\sum_{\pi\in\Pi_k}
 \left(\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!\right)
 \prod_{B\in\pi}P_{\sum_{j\in B}\alpha_j}.
\tag{C.7}
\]
To check it, fix a map from the labels \(1,\ldots,k\) to row indices. Its coefficient on the right is the sum of the displayed factors over partitions refining its equality classes. On an equality class of size \(s\), this is the signed sum of all permutations of \(s\) letters, grouped by their cycles; it is one for \(s=1\) and zero for \(s\ge2\), by pairing a permutation with its product with a fixed transposition. Thus precisely the injective maps survive. Each ordinary orbit sum is the left side divided by the factorials of the multiplicities of repeated exponent vectors. This proves the asserted generation by the \(P_\alpha\), while preserving the total exponent degree.

Now put \(P_j(y)=\sum_iL_i(y)^j\). The formal identity
\[
 \frac{s\,\partial_s\prod_i(1+sL_i)}{\prod_i(1+sL_i)}
 =\sum_{j\ge1}(-1)^{j-1}P_j(y)s^j
\tag{C.8}
\]
gives Newton's recurrence after multiplication by \(\sum_{j=0}^a E_j(y)s^j\) and coefficient comparison. It expresses \(P_j(y)\) as a polynomial in \(E_1(y),\ldots,E_a(y)\), homogeneous of weighted degree \(j\) when \(E_i\) has weight \(i\). Its coefficient of \(y^\alpha\), for \(|\alpha|=j\), is \(\binom{j}{\alpha}P_\alpha\). Dividing by that nonzero integer therefore expresses \(P_\alpha\) in the \(E_\beta\), preserving weighted degree \(|\alpha|\). Every factor has positive weight, so every resulting monomial contains at most \(|\alpha|\) factors. Substitute these expressions in (C.7). The total weight of every term is \(d\), and its number of factors is at most \(d\). This proves (C.6) constructively.

### 3. Homogenization produces a preimage of the required degree

For each term of (C.6), the assumption \(n\ge d\) gives \(n-k\ge0\). Equation (C.5) then gives
\[
 \mu_a\left(C_0^{n-k}\prod_{q=1}^k C_{\beta^{(q)}}\right)
 =u^n\prod_{q=1}^k E_{\beta^{(q)}}.
\tag{C.9}
\]
Apply (C.9) term by term to the explicitly computed expression for \(F\). The resulting source polynomial is homogeneous of coordinate degree \(n\) and maps to \(f\). The equality was derived on \(u\ne0\); both sides are polynomials in the ordered linear forms, and this is a dense principal open of their affine space. Hence they agree everywhere.

Every target highest-weight vector of weight \(\lambda\) has first-coordinate degree \(\lambda_1\), so its total degree in the remaining coordinates is precisely \(d=an-\lambda_1\). Thus (C.3)–(C.9) lift every such vector under (C.1). The canonical map is \(GL(V)\)-equivariant. Its image therefore contains the submodules generated by all target highest-weight vectors of weight \(\lambda\), which together are the full \(\lambda\)-isotypic component. This proves G-014.

The argument gives image multiplicity rather than only a coefficient inequality. A preimage need not initially be highest weight; equivariance and the equality with the specified target vector suffice, and the usual characteristic-zero isotypic projection provides a preimage in the same irreducible block.

### Exact isomorphism on the common first-row range

For \(a,n\ge2\) and \(d\le\min(a,n)\), apply G-014 both to \(h_{n,a}\) and to \(h_{a,n}\). In the common tensor space, normalized row and column symmetrizers are self-adjoint orthogonal projections, and the grid transpose identifies the two maps as adjoints, exactly as in M-001 and G-002. Their ranks are equal. Surjectivity in both directions therefore makes the two component dimensions equal to that common rank. Thus both maps are isomorphisms on their \(\lambda\)-isotypic components in the displayed common range. This follows for the prescribed maps themselves, with their specified tensor identifications.

### Geometric and lambda-ring form

The multiplication map on ordered linear forms is a morphism of affine schemes, and (C.5) is its coordinate pullback. Localization at the coefficient of the pure power \(t_1^a\) produces the displayed multisymmetric chart. Equations (C.7)–(C.9) prove that its denominators clear in coordinate degree \(n\) for every component satisfying (C.1). Thus the Chow coordinate image from G-003 and its normalizing representation algebra have identical \(\lambda\)-isotypic pieces in this range. Applying the coefficient functional \([s_\lambda]\) in \(K_0(\operatorname{Rep}_{\mathbf Q}GL(V))\) gives precisely the rank equality asserted above. All coordinate equations are integral; the rational divisions in (C.7)–(C.8) specify a localization of \(\mathbf Z\) over which each particular preimage spreads out. The general integral symmetric/divided-power map remains the one in G-003, and no integral surjectivity at excluded primes is asserted.

Primary source: Raicu, Sam, Weyman, *On some modules supported in the Chow variety*, Theorem 2.3, equation (2.8), Remark 2.9, pp.5–6; https://par.nsf.gov/servlets/purl/10334188 . These source passages were opened and read in this run. The new degree tracking and the full lifting proof above are checked separately in `CHECK_EVENTS.tsv`.


# An explicit stable rectangular-Kronecker lower bound

Statement **R-014**. Derived on 2026-11-21 UTC by GPT-6 Astra Pro, agent `/root/rectangular_cases`; effort setting not exposed. This is a corollary of the proved equal-middle-row formula T-025 and the known Ikenmeyer–Panova inequality. No priority claim is made.

For \(d\ge3\), write

\[
 p_{2,\ldots,d}(s)
 =\#\{(c_2,\ldots,c_d)\in\mathbb Z_{\ge0}^{d-1}:
             2c_2+\cdots+dc_d=s\},
\]

with the value zero for \(s<0\).

## The actual parameter family

Let \(d\ge3\), \(\beta\ge\gamma\ge0\), and

\[
 t=(d-2)\beta+\gamma,\qquad
 n\ge\max(1,t),\qquad
 \lambda=(dn-t,\beta^{d-2},\gamma).
\]

Trailing zero parts are omitted. Put

\[
 R=\beta-\gamma-\binom d2(\beta\bmod2).
\]

Then

\[
 \boxed{\displaystyle
 g\bigl(\lambda,(d^n),(d^n)\bigr)
 \ \ge\
 [S_\lambda V:\operatorname{Sym}^d(\operatorname{Sym}^nV)]
 \ =\ p_{2,\ldots,d}(R).}
 \tag{R014.1}
\]

The plethysm coefficient is taken in any sufficiently large dimension. In particular, throughout the explicitly specified subfamilies \(R=0\) and \(R\ge2\),

\[
 g\bigl(\lambda,(d^n),(d^n)\bigr)>0.
 \tag{R014.2}
\]

The displayed lower bound is the lattice-point count of one bounded polytope with \(d-1\) variables. It is uniform in all the parameters and independent of \(n\) inside the stated stable range.

## Complete proof of the corollary

First, \(t\ge\beta\), since \(d\ge3\) and \(\gamma\ge0\). Thus \(n\ge\beta\). Also

\[
 dn-t\ge(d-1)n\ge\beta,
\]

so every displayed \(\lambda\) is indeed a partition of \(dn\). The restriction \(n\ge1\) avoids an empty rectangle convention, including the case \(\beta=\gamma=0\).

Apply T-025 with outer degree \(m=d\). Its correction term \(d\max(0,\beta-n)\) is zero because \(n\ge\beta\). Its residual integer is consequently exactly \(R\), and its explicit basis-to-polytope bijection proves the equality in (R014.1).

Let \(\rho=(\beta^{d-2},\gamma)\), omitting zeros. Its size is \(t\), and \(\lambda=\rho(dn)\) in the notation of Ikenmeyer–Panova. Their **Proposition 2.8, “Inequality of Multiplicities,” p. 7**, applies for \(n\ge|\rho|\) and gives exactly the inequality in (R014.1). This source proposition and its entire proof were read again for this corollary. The exact primary source is:

Ikenmeyer–Panova, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory*, arXiv:1512.03798v2:

https://arxiv.org/pdf/1512.03798

Finally the nonnegative semigroup generated by \(2,3,\ldots,d\) is \(\{0\}\cup\{2,3,\ldots\}\): even positive integers are sums of 2's, and an odd integer at least 3 is 3 plus a sum of 2's. This proves the stated positive subfamilies.

### Exact maps behind the cited inequality

The source proof relates coordinate rings through padding and determinant realization; the comparison is not an identification of their coefficients. For a precise finite chain, let

\[
 M=n\binom{n+n^2-1}{n},
 \qquad
 \lambda_M=(dM-t,\rho).
\]

Ikenmeyer–Panova Lemma 2.7 gives this finite uniform determinant-size bound for all degree-\(n\) forms in \(n^2\) variables. Denote the degree-\(M\) padded-form variety by \(\Gamma_n^M\), as defined in their section 2(b), and the determinant orbit closure by \(\mathrm{Det}_M\). Their construction gives the actual closed inclusion

\[
 \Gamma_n^M\subseteq\mathrm{Det}_M
\]

and hence the equivariant coordinate restriction

\[
 \mathbb C[\mathrm{Det}_M]_d
 \twoheadrightarrow\mathbb C[\Gamma_n^M]_d.
\]

Their Proposition 2.6(b) constructs the padding lift on highest-weight polynomial spaces, preserving the evaluation pairing on padded forms and changing weight \(\lambda\) to \(\lambda_M\). Thus it gives an injection of the original highest-weight multiplicity space into the one in \(\mathbb C[\Gamma_n^M]_d\). The Peter–Weyl comparison in the proof of their Proposition 2.5 gives the final inequality in the finite chain

\[
 a_{d,n}^{\lambda}
 \le
 \operatorname{mult}_{\lambda_M}\mathbb C[\Gamma_n^M]_d
 \le
 \operatorname{mult}_{\lambda_M}\mathbb C[\mathrm{Det}_M]_d
 \le
 g\bigl(\lambda_M,(d^M),(d^M)\bigr).
\]

Their Theorem 2.1, citing Manivel's Theorem 1, identifies the last term with \(g(\lambda,(d^n),(d^n))\), because both \(M\) and \(n\) are at least \(|\rho|=t\). This is the precise chain used by Proposition 2.8. The new content of (R014.1) is the explicit positive count supplied for its plethysm term by T-025.

## Concrete infinite subfamilies

Every line below holds for every integer \(n\) in the displayed range.

| \(d,\beta,\gamma\) | Range | Partition \(\lambda\) | \(R\) | Proven rectangular-Kronecker lower bound |
|---|---|---|---:|---:|
| \(3,2,0\) | \(n\ge2\) | \((3n-2,2)\) | 2 | 1 |
| \(3,3,0\) | \(n\ge3\) | \((3n-3,3)\) | 0 | 1 |
| \(4,6,0\) | \(n\ge12\) | \((4n-12,6,6)\) | 6 | 3 |
| \(4,7,1\) | \(n\ge15\) | \((4n-15,7,7,1)\) | 0 | 1 |
| \(5,8,0\) | \(n\ge24\) | \((5n-24,8,8,8)\) | 8 | 5 |

For the lower bound 3, the solutions to \(2c_2+3c_3+4c_4=6\) are \((3,0,0)\), \((0,2,0)\), \((1,0,1)\). For the lower bound 5, the solutions to \(2c_2+3c_3+4c_4+5c_5=8\) are \((4,0,0,0)\), \((1,2,0,0)\), \((2,0,1,0)\), \((0,0,2,0)\), \((0,1,0,1)\).

The inequality can be strict even inside this family. Exact symmetric-group character sums give

\[
 a_{4,4}^{(12,2,2)}=1,\qquad
 g\bigl((12,2,2),(4^4),(4^4)\bigr)=2.
\]

This calculation is reproduced by verify_rectangular_end_bound.py and RECTANGULAR_END_BOUND_CHECK.tsv. They also verify equality \(a=g=1\) at \((d,n,\beta,\gamma)=(3,2,2,0)\) and \((3,3,3,0)\). The cases \(R<0\) and \(R=1\) give a zero value for the specified plethysm term; (R014.1) makes no rectangular-Kronecker vanishing assertion there.


# Six symmetric slots at the common-power-one boundary

Statement **R-015**. Completed and independently checked on 2026-11-21 UTC by GPT-6 Astra Pro, agent /root/rectangular_cases; inherited effort setting not exposed.

## Exact result

For every finite-dimensional complex vector space \(V\), the natural map

\[
 T_{6,1,5}:\operatorname{Sym}^6(\operatorname{Sym}^5V)
 \longrightarrow
 \operatorname{Sym}^6V\otimes\operatorname{Sym}^6(\operatorname{Sym}^4V),
 \qquad
 f\longmapsto[t_1\cdots t_6]\,
 f(v_1+t_1x,\ldots,v_6+t_6x)
\]

is injective. Here the parameters satisfy \(b=rL-1\) with \(r=6,L=1,b=5\).

By the exact coordinate-ring morphism R-013, the variety

\[
 Z_{1,5}(V)=\overline{\{\ell q:
        \ell\in V^*,\ q\in\operatorname{Sym}^4V^*\}}
       \subseteq\operatorname{Sym}^5V^*
\]

has no equations of degree at most six:

\[
 I_d(Z_{1,5}(V))=0\qquad(0\le d\le6).
\]

The pullback in degree six is precisely \(5^{-6}T_{6,1,5}\), not an unspecified nonzero scalar. This follows from R013.1. Vanishing in lower degrees follows by multiplying a nonzero lower-degree equation to degree six in the ambient polynomial domain, exactly as in R-013.

No general even-slot boundary classification or historical priority claim is made.

## Complete finite proof

### Reduction and source character

The source embeds in \((\operatorname{Sym}^5V)^{\otimes6}\). Iterated Pieri multiplication therefore gives only Schur functors with at most six rows. The natural tensor permutation and symmetrization formula for \(T_{6,1,5}\) acts by the same multiplicity-space matrices in all dimensions at least six. Checking \(\mathbb C^6\) consequently detects every possible kernel summand; smaller dimensions follow by naturality under an inclusion into \(\mathbb C^6\). This is the same Schur–Weyl argument proved in R-011, section 1, with six replacing four.

The exact source decomposition on \(\mathbb C^6\) has:

| Quantity | Value |
|---|---:|
| Distinct irreducible constituents | 893 |
| Sum of highest-weight multiplicities | 5,369 |
| Largest multiplicity | 32 |
| Number of monomial weights | 324,632 |
| Full representation dimension | 377,342,351,232 |

The last dimension equals \(\binom{257}{6}\), because \(\dim\operatorname{Sym}^5\mathbb C^6=\binom{10}{5}=252\).

The program character_r6_b5.cpp computes the complete character twice. One calculation multiplies the 252 factors

\[
 \prod_{\substack{\alpha\in\mathbb Z_{\ge0}^6\\|\alpha|=5}}
       (1-tx^\alpha)^{-1}
\]

through \(t\)-degree six. The other uses the exact Newton recurrence for \(h_j[h_5]\), \(j=1,\ldots,6\). It compares every monomial coefficient for every one of these six outer degrees. At degree six all 324,632 weights agree. The Weyl-alternant coefficient formula then extracts the multiplicity at every partition of 30 of length at most six. The sum of multiplicities times Weyl dimensions equals both the sum of all weight coefficients and \(\binom{257}{6}\). This proves the complete source multiplicity list used in the certificate.

### Integral source vectors

Let \(X\) be a \(6\times6\) variable matrix, with columns the six slots. For every nonempty subset \(I\subseteq\{1,\ldots,6\}\), let \(d_I(X)\) be the determinant using the first \(|I|\) rows and the columns \(I\) in increasing order. There are 63 such flag minors. A seed is

\[
 F_c(X)=\prod_I d_I(X)^{c_I}.
\]

The certificate records the 63 nonnegative integers \(c_I\). They satisfy

\[
 \sum_{I\ni j}c_I=5\quad(1\le j\le6),\qquad
 \lambda_k=\sum_{|I|\ge k}c_I\quad(1\le k\le6).
\]

Thus the seed has equal slot degrees five and highest weight \(\lambda\). The highest-weight property follows by applying a raising operator to each flag determinant: replacing a row by an earlier row repeats a row, giving zero.

The associated symmetric vector is its Reynolds sum

\[
 R_c(X)=\sum_{\sigma\in S_6}F_c(X_{\sigma(1)},\ldots,X_{\sigma(6)}),
\]

including the signs from sorting each determinant's columns. For compact integer storage, collect equal monomials in the 63 minors, divide their integer coefficients by their greatest common divisor, and choose the sign so that the first nonzero coefficient in lexicographic exponent order is positive. Each selected sum is nonzero. Its divisor is at most \(720\), since each coefficient is a signed sum of at most 720 terms; in particular it is a unit modulo \(1,000,003\).

Every source vector is therefore specified exactly by one 63-entry seed and this fixed normalization rule. The independent checker generates all 720 permutations anew, collects their signed contributions, and checks the seed's weight and all six slot degrees. Invariance follows directly by reindexing the complete group sum. No spanning assertion about the candidate seeds is required: the certificate supplies exactly the required number of independent images at each highest weight.

### Primary image evaluations by a squarefree logarithm

For a fixed point \(X,x\), every flag minor after the shift is exactly linear:

\[
 d_I(X+t x)=d_I(X)+\sum_{j\in I}a_{I,j}(X,x)t_j.
\]

Every term with two inserted columns vanishes because those columns are equal to \(x\). To find the coefficient \(t_1\cdots t_6\), work in the squarefree quotient ring

\[
 \mathbb F_P[t_1,\ldots,t_6]/(t_1^2,\ldots,t_6^2),
 \qquad P=1,000,003.
\]

The printed primary evaluation points have every \(d_I(X)\ne0\). Put \(C=\prod_Id_I(X)^{c_I}\). For a nonempty subset \(S\), define

\[
 \ell_S=(-1)^{|S|-1}(|S|-1)!
       \sum_I c_I\prod_{j\in S}\frac{a_{I,j}}{d_I(X)},
\]

where the summand is zero for \(S\not\subseteq I\). The formal logarithm of the product, after its constant factor \(C\) is removed, has coefficient \(\ell_S\) at \(t_S=\prod_{j\in S}t_j\). Indeed, the \(k\)-th term of \(\log(1+u)\) contributes \((-1)^{k-1}u^k/k\), and a product of \(k\) distinct variables has coefficient \(k!\) in \(u^k\). All relevant denominators are units because \(P>6\).

Exponentiating in this nilpotent ring gives the exact coefficient

\[
 [t_1\cdots t_6]F_c(X+t x)
 =C\sum_{\pi\text{ a set partition of }[6]}
          \prod_{S\in\pi}\ell_S.
\]

The primary evaluator computes this finite sum by the recurrence

\[
 H(\varnothing)=1,\qquad
 H(A)=\sum_{\substack{\varnothing\ne S\subseteq A\\\min A\in S}}
             \ell_SH(A\setminus S).
\]

The block containing the least element of \(A\) makes every set partition occur exactly once. It then adds the signed normalized Reynolds contributions.

### Independent verification and integer lifting

For every source constituent \(\lambda\) of multiplicity \(m_\lambda\), the certificate supplies \(m_\lambda\) selected normalized Reynolds vectors, \(m_\lambda\) evaluation rows, and the complete square matrix of their image values. Every one of the 893 determinants is nonzero modulo \(P\).

The independent program recheck_polarization_r6.cpp recomputes every selected entry without logarithms, inverses of minor constants, or set partitions. It expands the same linear minor factors by descending in-place Taylor recurrence, in reverse factor order:

\[
 c_A\leftarrow d_Ic_A+
          \sum_{j\in I\cap A}a_{I,j}c_{A\setminus\{j\}}.
\]

Descending subset index leaves each lower-index old coefficient intact. The independent program also evaluates all small flag determinants and every selected square determinant using power traces and Newton identities instead of the primary program's Gaussian elimination. For an \(m\times m\) matrix, these identities are

\[
 e_0=1,\qquad
 e_k=\frac1k\sum_{i=1}^k(-1)^{i-1}e_{k-i}\operatorname{tr}(A^i),
 \qquad\det A=e_m.
\]

Here \(m\le32<P\). The prime is separately checked by trial division, and the largest unreduced 64-bit sums are bounded by \(32P^2\).

All **65,481 selected entries** and all 893 determinants passed the independent check. Since the source vectors and coefficient-extraction map have integer coefficients, a nonzero determinant modulo \(P\) is a nonzero integer determinant. The selected images are therefore linearly independent over \(\mathbb Q\) and \(\mathbb C\).

Every source highest-weight multiplicity space is thus injective. Any nonzero equivariant kernel would contain a nonzero highest-weight vector. This proves the stated injectivity on \(\mathbb C^6\), and the dimension transfer already proved gives the result for all \(V\).

Two first-pass random seed lists were insufficient to exhibit their full ranks. Enlarged lists supplied full ranks four and seven in those blocks. The final selected certificate uses only complete square matrices; the two incomplete first-pass evaluations are not used in the proof.

## Reproducible compact artifacts

The complete certificate is POLARIZATION_R6_L1_B5_SELECTED.compact.gz. It contains every selected seed, point, square matrix and nonzero determinant, and occupies 329,843 compressed bytes. Its SHA256 is

~~~
6db560ac93c2f53850ddc547946b939556531a0e43aa0e52e18c2ae01e1326ca
~~~

The source character is POLARIZATION_R6_L1_B5_SOURCE.tsv; the complete rank summary is POLARIZATION_R6_L1_B5_ALL_RANKS.tsv; the independent receipt is POLARIZATION_R6_L1_B5_INDEPENDENT_RECHECK.txt.

To recheck, decompress the compact certificate, compile recheck_polarization_r6.cpp with C++17 and optimization, and give the decompressed file as its sole argument. The program character_r6_b5.cpp independently reproduces and compares both complete source-character calculations. The full candidate generator, original evaluator, and merge script are polarization_r6_seeds.py, check_polarization_r6.cpp, and merge_polarization_r6.py. The parallel intermediate directory is unnecessary for verifying the final certificate.

The next pair \(r=6,L=2,b=11\) has 13,019,909 monomial weights before Schur extraction and source dimension 9,679,525,138,407,392,632 on \(\mathbb C^6\). No rank certificate or theorem for that pair is asserted here.


# Three complete finite boundary kernels

Statement **R-016**, completed and independently checked on 2026-11-21 UTC by GPT-6 Astra Pro, /root/rectangular_cases; effort setting not exposed.

For the coefficient-extraction morphism

\[
\begin{gathered}
T_{r,L,b}:\operatorname{Sym}^r(\operatorname{Sym}^bV)
 \longrightarrow
 \operatorname{Sym}^{rL}V\otimes
 \operatorname{Sym}^r(\operatorname{Sym}^{b-L}V),
 \\
 f\longmapsto[t_1^L\cdots t_r^L]\,
 f(v_1+t_1x,\ldots,v_r+t_rx),
\end{gathered}
\]

the following are the exact kernels for every finite-dimensional complex \(V\):

\[
 \boxed{\ker T_{3,2,5}=0,}
 \qquad
 \boxed{\ker T_{3,3,8}=S_{(8,8,8)}V,}
 \qquad
 \boxed{\ker T_{5,1,4}=S_{(4,4,4,4,4)}V.}
\]

In the last two formulas the right-hand side denotes the unique embedded Schur summand in the displayed source. It is specified concretely below. Thus it is zero when the ambient dimension is smaller than its number of rows.

## Exact embedded rectangular kernel

In dimension \(r\), the polynomial \(\det(v_1,\ldots,v_r)^b\) has degree \(b\) in each of the \(r\) slots. For even \(b\) it is invariant under slot permutations. It is a nonzero highest-weight vector of weight \((b^r)\). Its source multiplicity is one: the corresponding \(GL_r\)-module is \(\det^b\), and the balanced-weight/permutation realization gives precisely its sign character \(\operatorname{sgn}^b=1\).

For the two pairs \((r,L,b)=(3,3,8)\) and \((5,1,4)\), one has \(rL=b+1\). In a term contributing to \(t_1^L\cdots t_r^L\), exactly \(b+1\) columns of the \(b\) determinant factors are replaced by the common vector \(x\). Some determinant factor receives at least two copies of \(x\), and that term is zero. Hence the entire displayed determinant power lies in the kernel.

For any ambient \(V\) of dimension at least \(r\), choose the first \(r\) basis directions and use the determinant of the corresponding \(r\times r\) coordinate minor. The \(GL(V)\)-span of its \(b\)-th power is the embedded Cartan module \(S_{(b^r)}V\): the polynomial is a nonzero highest-weight vector of that weight, and the source multiplicity is one by the stable Schur-functor multiplicity-space realization. This defines the actual inclusion in the source. Equivariance places its entire span in the kernel.

The selected-minor certificates below prove injectivity on every other source summand, so this explicit inclusion accounts for the complete kernel.

## Complete rank certificates

| \((r,L,b)\) | Source constituents | Source highest-weight dimension | Certified image highest-weight rank | Largest source multiplicity | Independent selected entries |
|---|---:|---:|---:|---:|---:|
| \((3,2,5)\) | 13 | 13 | 13 | 1 | 13 |
| \((3,3,8)\) | 36 | 39 | 38 | 2 | 44 |
| \((5,1,4)\) | 95 | 142 | 141 | 4 | 263 |

The source dimensions in ambient dimensions \(r\) are respectively 1,771; 16,215; and 16,108,764.

The producer small_boundary_candidates.py computes the complete source characters from Newton's recurrence, extracts every Schur multiplicity by the Weyl alternant, and checks the full Weyl-dimension sum against the dimension of the symmetric power. The independent program recheck_small_boundary.py obtains every source multiplicity, including all zeros, by power-sum plethysm expansion and Murnaghan–Nakayama character sums. It checks all 27, 61 and 192 partitions of the respective degrees and permitted lengths.

For each nonrectangular highest weight, the supplied source vectors are signed, normalized Reynolds sums of products of flag minors. Their complete definition is the same one proved in R-015, with \(r\) slots: average all \(r!\) literal slot permutations, collect the determinant signs, divide the integral coefficients by their gcd, and choose the first nonzero coefficient positive. The seeds come from semistandard tableaux of content \((b^r)\). Each seed's row weights and every slot degree are independently verified.

The primary C++ program check_small_boundary.cpp evaluates \(T_{r,L,b}\) by multiplying the exactly linear shifted minors and retaining the exponents \(0\le\deg t_i\le L\). It selects a square matrix of size equal to the full source multiplicity in each nonrectangular block. Every selected determinant is nonzero modulo the prime \(1,000,003\). The rectangular blocks are handled by the explicit polynomial proof above, not by a numerical inference from sampled zeros.

The independent Python program recomputes every selected matrix entry with a separate NumPy Taylor-array implementation, reverses the factor order, generates every Reynolds sum independently, and computes all small and selected determinants by recursive Laplace expansion. The programs agree on all 320 selected entries. They made 40, 183 and 20,402 independent Taylor evaluations respectively. The largest selected matrix has size four, so the Laplace checks are exhaustive exact calculations. Array intermediates are bounded by \(6P^2\), inside the signed 64-bit range.

A nonzero determinant modulo \(P\) proves that the corresponding integer polynomial-image columns are linearly independent over \(\mathbb Q\) and \(\mathbb C\). Thus every nonrectangular highest-weight multiplicity space is injective. Complete reducibility then proves the stated kernels in dimension \(r\).

Finally, the source has only Schur functors of length at most \(r\), by iterated Pieri multiplication of \(r\) one-row representations. The coefficient-extraction map is defined by the same tensor permutations and averages in every dimension. Its Schur-multiplicity matrices are therefore dimension-independent once all source partitions fit, exactly as proved in R-011. This transfers the complete kernel descriptions to every larger \(V\). Naturality under an inclusion handles smaller \(V\).

The data are fully specified in the three files POLARIZATION_R3_L2_B5.selected.gz, POLARIZATION_R3_L3_B8.selected.gz, and POLARIZATION_R5_L1_B4.selected.gz, together with their source and rank TSV tables. SMALL_BOUNDARY_INDEPENDENT_CHECK.tsv is the independent receipt. Decompress the selected files and run recheck_small_boundary.py from any directory to reproduce the independent character and entry checks.

These finite kernels agree with the rectangular obstruction at these actual parameter pairs. No assertion about all remaining boundary parameters is inferred from the calculation.


# An exact polynomial model for every highest-weight boundary kernel

Statement **R-017**. This is an unconditional reformulation of the common-polarization kernel, not a classification of its remaining multiplicities. Written and checked on 2026-11-21 UTC by GPT-6 Astra Pro, /root/rectangular_cases; effort setting not exposed. The first-coordinate evaluation underlying the reformulation is also used in Kadish–Landsberg, arXiv:1204.4693, Theorem 1.3 and its proof in section 2.

Fix \(r\ge1\), \(b\ge L\ge0\), and \(m\ge2\). In each of the \(r\) slots write

\[
 v_i=(x_i,y_{i,2},\ldots,y_{i,m}),\qquad
 z_{i,j}=y_{i,j}/x_i.
\]

For a polynomial \(P(z_1,\ldots,z_r)\) whose degree in each block \(z_i\) is at most \(b\), define its separate homogenization

\[
 H_b(P)=\prod_{i=1}^r x_i^b
 P(y_{1,2}/x_1,\ldots,y_{r,m}/x_r).
 \tag{R017.1}
\]

The block degree bounds make this a polynomial. Evaluation at every \(x_i=1\) is its inverse. These are exact linear isomorphisms between polynomials of block degrees at most \(b\) and polynomials separately homogeneous of degree \(b\) in the \(v_i\). They commute with slot permutations.

## Highest vectors become translated-polynomial invariants

The raising operator \(E_{1j}\), \(j>1\), acts on a separately homogeneous polynomial as \(\sum_i x_i\partial_{y_{i,j}}\). Direct differentiation gives

\[
 E_{1j}H_b(P)=
 \prod_i x_i^b\sum_i\partial_{z_{i,j}}P.
 \tag{R017.2}
\]

Thus its kernel corresponds exactly to invariance under simultaneous translation
\(z_{i,j}\mapsto z_{i,j}+c_j\). The equality follows by exponentiating the displayed locally nilpotent derivations in characteristic zero; differentiating the translation identity proves the converse.

For \(2\le k<j\le m\), the remaining raising operators correspond exactly to

\[
 \sum_i z_{i,k}\partial_{z_{i,j}}.
 \tag{R017.3}
\]

A source highest vector of weight \(\lambda\vdash rb\) therefore corresponds to a symmetric, simultaneously translation-invariant polynomial \(P\), of individual block degrees at most \(b\), with coordinate weights \((\lambda_2,\ldots,\lambda_m)\), annihilated by (R017.3). Its total \(z\)-degree is

\[
 D=\lambda_2+\cdots+\lambda_m=rb-\lambda_1.
 \tag{R017.4}
\]

Every polynomial satisfying these displayed properties homogenizes to precisely such a highest vector; the formulas above prove both directions.

## Polarization is weighted block truncation

For a monomial

\[
 z^\alpha=\prod_{i=1}^r\prod_{j=2}^m z_{i,j}^{\alpha_{i,j}},
 \qquad d_i=\sum_{j=2}^m\alpha_{i,j},
\]

define the explicit diagonal operator

\[
 Q_{L,b}(z^\alpha)=
 \begin{cases}
 \left(\prod_i\binom{b-d_i}{L}\right)z^\alpha,
       &d_i\le b-L\text{ for every }i,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{R017.5}
\]

The coefficient-extraction map satisfies the exact identity

\[
 T_{r,L,b}(H_b(P))(v_1,\ldots,v_r;\,e_1)
 =H_{b-L}(Q_{L,b}P).
 \tag{R017.6}
\]

To prove it, a monomial in (R017.1) is
\(\prod_i x_i^{b-d_i}y_i^{\alpha_i}\). Substitution of \(v_i+t_ie_1\) changes only \(x_i\) to \(x_i+t_i\). The coefficient of \(t_i^L\) is
\(\binom{b-d_i}{L}x_i^{b-d_i-L}y_i^{\alpha_i}\), with value zero for \(b-d_i<L\). Multiplication over all slots gives (R017.6) on every monomial.

Restriction of a highest image to common vector \(e_1\) detects its vanishing. To see this directly, let \(G(v_1,\ldots,v_r;w)\) be such an image. It is annihilated by every \(E_{1j}\), and is homogeneous of degree \(rL\) in the common vector \(w=(w_1,\ldots,w_m)\). On the dense open set \(w_1\ne0\), apply the unipotent substitutions

\[
 w_j\mapsto w_j-\frac{w_j}{w_1}w_1=0,\qquad
 y_{i,j}\mapsto y_{i,j}-\frac{w_j}{w_1}x_i
 \quad(j>1).
\]

Invariance under the exponentials of \(E_{1j}\) leaves \(G\) unchanged. The common vector becomes \(w_1e_1\), and common-vector homogeneity gives

\[
 G(v_1,\ldots,v_r;w)
 =w_1^{rL}
 G(v'_1,\ldots,v'_r;e_1).
 \tag{R017.7}
\]

Hence a zero restriction at \(e_1\) makes \(G\) zero on a dense open set and therefore identically zero. The converse is immediate.

Combining (R017.1)–(R017.7) gives the exact highest-weight kernel isomorphism

\[
 \boxed{\begin{gathered}
 H_b^{-1}\bigl((\ker T_{r,L,b})_\lambda^{\mathrm{highest}}\bigr)
 =
 \ker Q_{L,b}\ \cap\\
 \{\text{polynomials satisfying (R017.2)–(R017.4) and slot symmetry}\}.
 \end{gathered}}
 \tag{R017.8}
\]

All nonzero diagonal coefficients in (R017.5) are nonzero rational integers. Its kernel is therefore exactly the kernel of ordinary monomial truncation retaining only the monomials with every block degree at most \(b-L\). This identifies the relevant subspace with explicit linear equations, rather than inferring it from source and target multiplicities.

## The precise boundary degree gap

At \(r\ge2,L\ge1,b=rL-1\), a source partition has \(\lambda_1\ge b\), because its length is at most \(r\) and its size is \(rb\). Equality forces the rectangle \((b^r)\). For that rectangle,

\[
 D=(r-1)b=r(b-L)+1,
\]

so every monomial exceeds the total degree allowed by the block truncation. In dimensions \(m\ge r\), the determinant power provides the corresponding source highest vector exactly when \(b\) is even; at this boundary that parity is equivalent to \(r\) and \(L\) both odd. For \(m<r\), that Schur functor is zero.

Every other source partition has \(\lambda_1\ge b+1=rL\), so (R017.4) gives \(D\le r(b-L)\). The total-degree obstruction is then absent. Formula (R017.8) specifies the actual remaining kernel problem as a translation-invariant symmetric polynomial truncation problem; it does not assert that its remaining intersection is zero. R-011, R-012, R-015 and R-016 supply the completely certified finite cases currently established in this run.


# A complete second-row injectivity range for common polarization

Statement **R-018**. Written and checked on 21 November 2026 UTC by
GPT-6 Astra Pro, `/root/rectangular_cases`; the effort setting is not
exposed. This is an exact consequence of the flag-minor algebra and the
truncation morphism R-017. No historical novelty claim is made.

## The actual maps and the unconditional range

Let \(r\ge1\), \(b\ge L\ge0\), and let \(V\) be a finite-dimensional
vector space over a field of characteristic zero. On polynomials in
\(r\) vector slots, each homogeneous of degree \(b\), define

\[
\widetilde T_{r,L,b}f(v_1,\ldots,v_r;w)
 =[t_1^L\cdots t_r^L]
 f(v_1+t_1w,\ldots,v_r+t_rw).
\tag{R018.1}
\]

This is the \(GL(V)\)-equivariant, \(S_r\)-equivariant map

\[
(\operatorname{Sym}^bV)^{\otimes r}
\longrightarrow
\operatorname{Sym}^{rL}V\otimes
(\operatorname{Sym}^{b-L}V)^{\otimes r}.
\tag{R018.2}
\]

Here the polynomial-generator realization of tensors is used, as in
R-017. The permutation group acts on the \(r\) slots in both expressions.
For \(\mu\vdash r\), application of
\(\operatorname{Hom}_{S_r}([\mu],-)\) gives the actual induced map

\[
T_{r,L,b}^{\mu}:S_\mu(\operatorname{Sym}^bV)
\longrightarrow
\operatorname{Sym}^{rL}V\otimes
S_\mu(\operatorname{Sym}^{b-L}V).
\tag{R018.3}
\]

The standard Schur-functor realization here is
\(S_\mu W=\operatorname{Hom}_{S_r}([\mu],W^{\otimes r})\).
For \(\mu=(r)\), (R018.3) is exactly the map
\(T_{r,L,b}\) used in R-011 through R-017. Formula (R018.1) fixes the
coefficient-extraction normalization; the product of ordinary differential
operators is \((L!)^r\widetilde T_{r,L,b}\).

For every \(\lambda\vdash rb\) with \(\lambda_2\le b-L\), and for every
\(\mu\vdash r\),

\[
\boxed{
\bigl(\ker\widetilde T_{r,L,b}\bigr)_{\lambda}=0,
\qquad
\bigl(\ker T_{r,L,b}^{\mu}\bigr)_{\lambda}=0.}
\tag{R018.4}
\]

The subscript denotes the entire \(GL(V)\)-isotypic component. A missing
second part is zero. The formulas include all source multiplicities and
all ambient dimensions. They assert an actual injectivity range for the
specified map.

## 1. Why every highest polynomial has the block-degree bound

Take \(m=\dim V\), with polynomial generators \(X_{ji}\), where
\(1\le j\le m\) is the vector coordinate and \(1\le i\le r\) is the
slot. Write \(x_i=X_{1i}\). For a subset \(I\subseteq\{1,\ldots,r\}\)
of size \(k\le m\), put

\[
\Delta_{k,I}=\det(X_{ji})_{1\le j\le k,\ i\in I},
\tag{R018.5}
\]

with the columns in increasing order. This is a highest polynomial of
\(GL(V)\)-weight \((1^k)\). Its slot weight is one in the slots in
\(I\) and zero elsewhere.

The algebra of highest polynomials is generated by these minors. Here
is a representation-theoretic proof of that precise generation statement.
The Cauchy decomposition of the matrix polynomial ring, followed by taking
highest vectors for the row action, is

\[
\mathbf Q[X_{ji}]^{U_m}
 =\bigoplus_{\ell(\eta)\le\min(m,r)} S_\eta\mathbf Q^r,
\tag{R018.6}
\]

with the summand tagged by its row highest weight \(\eta\). The algebra
generated by (R018.5) is stable under the column \(GL_r\): the formula
for a minor of a matrix product expresses its transform as a linear
combination of minors of the same size. For every summand in (R018.6),
the nonzero product

\[
\prod_{k=1}^{\min(m,r)}
\Delta_{k,\{1,\ldots,k\}}^{\eta_k-\eta_{k+1}}
\tag{R018.7}
\]

belongs to that summand and to the generated algebra. The summand is an
irreducible column \(GL_r\)-module, so the column-stable algebra contains
it in full. This proves generation for every summand and hence for the
whole highest algebra. The same proof works after extension of scalars.

Now let \(f\) be any highest vector of weight \(\lambda\) in
\((\operatorname{Sym}^bV)^{\otimes r}\). Express it using products of
the minors, and project that expression onto row weight \(\lambda\)
and slot multidegree \((b,\ldots,b)\). Each minor is homogeneous for both
gradings, so this projection retains precisely products of those two
degrees. If \(c_k\) is the number of height-\(k\) factors in any retained
product, then

\[
\lambda_j=\sum_{k\ge j}c_k,
\qquad
\sum_{k\ge2}c_k=\lambda_2.
\tag{R018.8}
\]

Set every \(x_i=1\) and put
\(z_i=(X_{2i},\ldots,X_{mi})\). A height-one factor becomes the constant
one. Each factor of height at least two is a polynomial of degree at
most one in each block \(z_i\), because a determinant uses a column
exactly once. Equation (R018.8) therefore proves

\[
P(z_1,\ldots,z_r)=f\bigl((1,z_1),\ldots,(1,z_r)\bigr)
\quad\Longrightarrow\quad
\deg_{z_i}P\le\lambda_2\quad(1\le i\le r).
\tag{R018.9}
\]

This conclusion concerns every highest vector, including arbitrary
linear combinations in a multiplicity space. Neither slot symmetry nor
a choice of highest-vector basis was used.

## 2. The truncation map and its explicit inverse on this range

Separate homogenization is

\[
H_b(P)=\prod_i x_i^b P(z_{i,j}=X_{ji}/x_i).
\tag{R018.10}
\]

It inverts evaluation at \(x_i=1\) on separately degree-\(b\) polynomials.
For a monomial \(z^\alpha\) of block degrees
\(d_i=\sum_{j\ge2}\alpha_{i,j}\), the exact calculation from R-017 is

\[
\widetilde T_{r,L,b}(H_b(P))(v_1,\ldots,v_r;e_1)
 =H_{b-L}(Q_{L,b}P),
\tag{R018.11}
\]

where

\[
Q_{L,b}(z^\alpha)
 =\left(\prod_i\binom{b-d_i}{L}\right)z^\alpha
\qquad(d_i\le b-L\text{ for all }i).
\tag{R018.12}
\]

Monomials exceeding the displayed block bound have image zero. On the
range (R018.9) with \(\lambda_2\le b-L\), every binomial factor in
(R018.12) is a positive integer. Thus the following inverse is an actual
linear map on that polynomial subspace:

\[
Q_{L,b}^{-1}(z^\alpha)
 =\left(\prod_i\binom{b-d_i}{L}^{-1}\right)z^\alpha.
\tag{R018.13}
\]

In particular a nonzero highest vector has nonzero restriction of its
image to common vector \(e_1\). The kernel of (R018.2) is a
\(GL(V)\)-submodule. A nonzero part in its \(\lambda\)-isotypic component
would contain a nonzero highest vector of weight \(\lambda\), contradicting
(R018.9)–(R018.13). This proves the first equality in (R018.4).

The coefficient-extraction map commutes with slot permutations.
Application of \(\operatorname{Hom}_{S_r}([\mu],-)\) to this injective
restriction remains injective. Equivalently, any vector in the kernel
of the induced map gives an \(S_r\)-equivariant map into the already zero
kernel component. This proves the second equality in (R018.4), with
the exact source and target in (R018.3).

For \(m=0\) every positive-degree source is zero, and the degree-zero map is the identity. For \(m=1\) the only
source partition is a row, and (R018.1) is multiplication by
\(\binom bL^r\), which is nonzero. These statements cover the low
dimensions not requiring the matrix argument.

## 3. Consequences for the boundary and the padded-form ideal

At the boundary \(r\ge2\), \(L\ge1\), \(b=rL-1\), (R018.4) gives

\[
\ker T_{r,L,rL-1}
\ \subseteq\!
\bigoplus_{\substack{\lambda\vdash r(rL-1)\\
                     \lambda_2\ge(r-1)L}}
\left(\operatorname{Sym}^r(\operatorname{Sym}^{rL-1}V)\right)_\lambda.
\tag{R018.14}
\]

Every component with \(\lambda_2\le(r-1)L-1\) is injective. In
particular, for the original common power \(L=r\), every possible
kernel component has second row at least \(r(r-1)\).

More generally, let

\[
Z_{L,b}=\overline{\{\ell^Lq:
\ell\in V^*,\ q\in\operatorname{Sym}^{b-L}V^*\}}.
\]

The explicitly normalized pullback in R-013 is
\((\nu_{L,b}^*)_r=\binom bL^{-r}T_{r,L,b}\).
Combining that exact identity with (R018.4) yields

\[
\boxed{I_r(Z_{L,b})_\lambda=0
\qquad(\lambda\vdash rb,\ \lambda_2\le b-L).}
\tag{R018.15}
\]

Equations (R018.14)–(R018.15) specify which whole isotypic components
survive the actual morphism. The still-unclassified components at the
boundary lie in the displayed complementary second-row range. R-016
classifies three finite boundary kernels by independent exact
certificates; no general rectangular-kernel classification is asserted
here.

## Relation to checked primary material

Kadish–Landsberg, *Padded polynomials, their cousins, and geometric
complexity theory*, [arXiv:1204.4693v1](https://arxiv.org/pdf/1204.4693),
Theorem 1.7, printed p. 3, with its full proof in §3, gives the generalized
polarization morphism whose kernel is this padded-form ideal. Their
Theorem 1.3, printed p. 2, and complete proof in §2 use first-coordinate
evaluation to establish first-row ranges. R-013 and R-017 specify the
coefficient-extraction normalization and the precise polynomial
truncation. The flag-minor algebra argument above supplies the stated
second-row range directly. T-032 gives a separate explicit balanced
chart using the same flag generators.


# Exact common polarization on the first boundary row band

Statements **R-019** and **R-020**. Written and checked on 21 November
2026 UTC by GPT-6 Astra Pro, `/root/rectangular_cases`; effort setting
not exposed. R-019 is an explicit coefficient calculation. R-020 uses
the complementary Schur pairing and the multilinear Young-symmetrizer
map to identify the entire indicated band. No historical novelty claim
is made.

Throughout, \(T_{r,L,b}\) means the coefficient-extraction map

\[
T_{r,L,b}f(v_1,\ldots,v_r;w)
=[t_1^L\cdots t_r^L]f(v_1+t_1w,\ldots,v_r+t_rw),
\tag{N.1}
\]

from \(\operatorname{Sym}^r(\operatorname{Sym}^bV)\) to
\(\operatorname{Sym}^{rL}V\otimes
\operatorname{Sym}^r(\operatorname{Sym}^{b-L}V)\).
The product of ordinary differential operators is \((L!)^rT_{r,L,b}\).

## R-019. A nonrectangular boundary component with an exact coefficient

Let \(r\ge2\), \(L\ge1\), and \(rL\) be even. Put

\[
b=rL-1,\qquad C=r(L-1),\qquad
\lambda=((rL)^{r-1},C),\qquad
s=\lfloor r/2\rfloor,\quad t=r-s.
\tag{N.2}
\]

The source \(\lambda\)-isotypic component has multiplicity one, and
\(T_{r,L,b}\) is injective on that component in every ambient dimension.
Here a Schur functor of length greater than \(\dim V\) is zero.

An explicit highest vector in dimension \(r\) is as follows. Let
\(M=(v_1,\ldots,v_r)\) be the matrix of vector-slot generators. Write
\(D=\det M\), let \(B\) be its first \(r-1\) rows, and set

\[
y_i=(-1)^{r+i}\det B_{\widehat i},\qquad
f=D^C\prod_{i=1}^r y_i.
\tag{N.3}
\]

The hat deletes column \(i\). The same formula with \(D^0=1\) defines
the vector in dimension \(r-1\) when \(L=1\).

To specify an exact evaluation of its image, split the column indices
into \(I=\{1,\ldots,s\}\) and \(J=\{s+1,\ldots,r\}\). Let \(A\)
be the \((r-2)\times r\) matrix whose rows, in the indicated order, are

\[
e_i-e_s\quad(1\le i<s),\qquad
e_{s+j}-e_r\quad(1\le j<t),
\tag{N.4}
\]

and put \(c=-e_s+e_r\). Here \(e_i\) denotes a row coordinate vector
in this displayed matrix construction. Take the vector-slot matrix
\(M_0\) with first row zero, middle rows \(A\), and last row \(c\).
The common vector in (N.1) is the first vector-coordinate basis vector
\(e_1\). Then

\[
\boxed{
T_{r,L,b}f(M_0;e_1)
=(-1)^s
\binom{r(L-1)}{sL-t}
\frac{(sL)!\,(tL)!}{(L!)^r}
\ne0.}
\tag{N.5}
\]

For \(L=1\), the last row of \(M_0\) can be deleted: the polynomial
\(f\) does not use it. Thus the same evaluation proves the statement
in the minimum nonzero ambient dimension in that case.

### Proof of the highest vector and its slot symmetry

Every cofactor \(y_i\) is a flag minor of height \(r-1\), with row
highest weight \((1^{r-1},0)\). Their product has weight
\((r^{r-1},0)\). Multiplication by \(D^C\) adds \((C^r)\), giving
exactly \(\lambda\) in (N.2). The polynomial is nonzero because it is
a product of nonzero polynomials in an integral domain.

Each column belongs to \(r-1\) of the cofactor factors, so its total
degree in \(f\) is \(C+r-1=b\). A column permutation \(\sigma\)
sends the cofactor coordinates to
\(\operatorname{sgn}(\sigma)y_{\sigma(i)}\), with the inverse indexing
when the opposite permutation convention is used. Consequently its
effect on their product is \(\operatorname{sgn}(\sigma)^r\). The
determinant power contributes \(\operatorname{sgn}(\sigma)^C\).
The combined character is
\(\operatorname{sgn}(\sigma)^{C+r}
=\operatorname{sgn}(\sigma)^{rL}=1\).
Thus (N.3) belongs to the symmetric-slot source of (N.1).

### Proof of the coefficient and all signs

Replace the first row of \(M_0\) by independent variables
\(x=(x_1,\ldots,x_r)\), and write

\[
X=\sum_{i\in I}x_i,\qquad Y=\sum_{i\in J}x_i.
\]

The kernel of the matrix \(A\) in (N.4) consists exactly of vectors
constant on each of the two groups. The cofactor vector \(y\) of
\(B=[x;A]\) lies in that kernel and satisfies \(x\cdot y=0\).
Its last coordinate can also be computed directly:

\[
y_r=\det B_{\widehat r}=(-1)^{s-1}X.
\]

Indeed the rows belonging to the second group leave an identity block
on columns \(s+1,\ldots,r-1\), and the remaining determinant has rows
\((x_1,\ldots,x_s)\) and \(e_i-e_s\), \(1\le i<s\). Expansion gives
\((-1)^{s-1}\sum_{i\le s}x_i\). The two kernel conditions now give
the full vector, as polynomial identities:

\[
y_i=(-1)^sY\quad(i\in I),\qquad
y_i=(-1)^{s+1}X\quad(i\in J).
\tag{N.6}
\]

Expansion of \(D\) in its last row gives

\[
D=c\cdot y=(-1)^{s+1}(X+Y).
\tag{N.7}
\]

Combining (N.6)–(N.7), the specialization of (N.3) is

\[
(-1)^{(s+1)C+sr+t}(X+Y)^C X^tY^s.
\]

Since \(C+r=rL\) is even, its sign exponent is congruent to
\(C+t\equiv r+t\equiv s\pmod2\). Thus it equals

\[
(-1)^s(X+Y)^C X^tY^s.
\tag{N.8}
\]

To obtain \(\prod_i x_i^L\), the total \(X\)-degree must be \(sL\)
and the total \(Y\)-degree must be \(tL\). The unique relevant term
of \((X+Y)^C\) has \(X\)-degree \(sL-t\). Its coefficient is
\(\binom C{sL-t}\). Expansion of \(X^{sL}\) and \(Y^{tL}\) then
gives the two multinomial coefficients
\((sL)!/(L!)^s\) and \((tL)!/(L!)^t\).

For even \(r\), \(s=t\) and \(sL-t=s(L-1)\) lies between zero
and \(C\). For odd \(r\), the assumed evenness of \(rL\) makes
\(L\ge2\) even; then \(sL\ge t=s+1\) and \(tL\ge s\), which
give the same two bounds. All factorials are therefore defined and
the coefficient is nonzero.

Finally the first row of \(M_0\) is zero, so substitution in (N.1)
replaces this row exactly by \((t_1,\ldots,t_r)\). Hence the computed
coefficient is precisely the value in (N.5), with no omitted derivative
or averaging factor. This proves nonvanishing of the actual map.

The multiplicity-one assertion follows from the exact pairing and
multilinear identification in R-020 below. A nonzero map on a single
irreducible source copy is injective. The tensor map (N.1) is natural
and is given by tensor-position symmetrizations and permutations
independent of dimension. Thus its map on a Schur multiplicity space
is the same in every ambient dimension where that Schur functor is
nonzero. Alternatively the above construction already uses the
minimum possible dimension: \(r\) for \(C>0\), and \(r-1\) for
\(C=0\); embedding that space preserves the displayed highest vector
and its nonzero image.

### Actual examples and relation to the original boundary

\[
\begin{array}{c|c|c|c|r}
r&L&b&\lambda&Tf(M_0;e_1)\\\hline
3&2&5&(6,6,3)&-6\\
4&1&3&(4,4,4,0)&4\\
4&4&15&(16,16,16,12)&4527600\\
5&2&9&(10,10,10,10,5)&2700\\
6&1&5&(6,6,6,6,6,0)&-36
\end{array}
\tag{N.9}
\]

For every even \(r\ge2\), the original common power \(L=r\) gives
the explicit surviving component

\[
\lambda=((r^2)^{r-1},r^2-r)
\quad\text{at}\quad b=r^2-1.
\tag{N.10}
\]

Its second row is \(r^2\) for \(r\ge3\), outside the range
\(\lambda_2\le r(r-1)-1\) proved in R-018. This result concerns the
specified common-polarization morphism; it does not identify an
additional component of a different map without a further morphism
calculation.

## R-020. The complete band \(\lambda_1\le b+1\)

Fix \(r\ge2,L\ge1,b=rL-1\), and put \(H=b+1=rL\). In the source
\(\operatorname{Sym}^r(\operatorname{Sym}^bV)\), the sum of all
isotypic components with \(\lambda_1\le H\) is

\[
\boxed{
\begin{cases}
S_{(H^{r-1},H-r)}V,&H\text{ even},\\
S_{((H-1)^r)}V,&H\text{ odd},
\end{cases}}
\tag{N.11}
\]

with multiplicity one in each case. The map \(T_{r,L,b}\) is
injective on the entire band in the first line. In the second line
the entire displayed component is its kernel in that band. This
classifies the map on every source component with first row at most
\(b+1\), for every \(r,L\).

### 1. The exact complementary Schur pairing

Work first in the \(r\)-dimensional slot space \(E=\mathbf Q^r\).
Every partition in \((\operatorname{Sym}^bV)^{\otimes r}\) has at
most \(r\) rows. For \(\lambda\vdash rb\) inside the rectangle
\((H^r)\), define

\[
\nu=(H-\lambda_r,\ldots,H-\lambda_1).
\tag{N.12}
\]

It is a partition of \(rH-rb=r\). There is a nonzero perfect
\(GL(E)\)-equivariant pairing

\[
S_\lambda E\otimes S_\nu E\longrightarrow(\det E)^H.
\tag{N.13}
\]

An explicit construction uses the exterior columns. If the \(H\)
column heights of \(\lambda\), with zero heights included, are
\(h_1\ge\cdots\ge h_H\), those of \(\nu\) are
\(r-h_H,\ldots,r-h_1\). Embed each Schur module as its Cartan
component in the corresponding tensor product of exterior powers.
Reverse the factors of the second module and use, in each column,
the actual exterior multiplication

\[
\Lambda^{h_j}E\otimes\Lambda^{r-h_j}E\longrightarrow\Lambda^rE.
\]

Their tensor product gives (N.13). It is nonzero: pair the highest
vector formed from \(e_1\wedge\cdots\wedge e_{h_j}\) in each first
factor with the lowest vector formed from
\(e_{h_j+1}\wedge\cdots\wedge e_r\) in its paired second factor.
The value is \((e_1\wedge\cdots\wedge e_r)^{\otimes H}\).
Irreducibility makes the resulting pairing perfect.

Torus weights in this pairing add to \((H^r)\). It therefore
restricts to a perfect pairing between the balanced weight
\((b^r)\) on the first factor and the multilinear weight
\((1^r)\) on the second. Literal permutation matrices act on the
target by \(\operatorname{sgn}^H\). Consequently

\[
(S_\lambda E)_{(b^r)}
\simeq\operatorname{sgn}^H\otimes
\bigl((S_\nu E)_{(1^r)}\bigr)^*
\quad\text{as actual }S_r\text{-modules}.
\tag{N.14}
\]

### 2. The multilinear Young-symmetrizer map

Let \(e_1,\ldots,e_r\) be the basis of \(E\). The map

\[
\mathbf Q[S_r]\longrightarrow(E^{\otimes r})_{(1^r)},
\qquad
\sigma\longmapsto
e_{\sigma(1)}\otimes\cdots\otimes e_{\sigma(r)}
\tag{N.15}
\]

is an isomorphism: the displayed tensors form the entire multilinear
basis. Literal basis permutations act by left multiplication on the
group algebra. Give tensor positions the right action
\((v_1\otimes\cdots\otimes v_r)\rho
=v_{\rho(1)}\otimes\cdots\otimes v_{\rho(r)}\).
Then (N.15) also intertwines right multiplication.

Choose a tableau of shape \(\nu\), take its row symmetrizer and
column antisymmetrizer, and divide their product by its nonzero
Young-symmetrizer scalar to obtain a primitive Young idempotent
\(e_\nu\). The image \((E^{\otimes r})e_\nu\) is the corresponding
Schur-module realization \(S_\nu E\). Restricting (N.15) to the
left ideal \(\mathbf Q[S_r]e_\nu\) thus gives the exact map

\[
[\nu]\simeq\mathbf Q[S_r]e_\nu
\xrightarrow{\ \sim\ }(S_\nu E)_{(1^r)}.
\tag{N.16}
\]

Specht modules over \(\mathbf Q\) are self-dual: average any positive
definite rational form over the finite group and use it to identify
the module with its dual. Equations (N.14)–(N.16) prove

\[
(S_\lambda E)_{(b^r)}\simeq
\operatorname{sgn}^H\otimes[\nu].
\tag{N.17}
\]

The Cauchy balanced-weight identification identifies the highest
\(\lambda\)-multiplicity space of
\(\operatorname{Sym}^r(\operatorname{Sym}^bV)\) with the invariant
subspace of (N.17). Its dimension is one for
\(\nu=(r)\) when \(H\) is even, one for \(\nu=(1^r)\) when \(H\)
is odd, and zero for every other \(\nu\). Taking complements in
(N.12) gives exactly (N.11). This proves the complete source-band
description, including all zero multiplicities.

### 3. The map on the two actual bands

For even \(H=rL\), the sole source component is the component in
R-019. Formula (N.5) proves nonvanishing, so its multiplicity-one
source is mapped injectively.

For odd \(H=rL\), both \(r\) and \(L\) are odd and \(b=H-1\) is
even. The highest vector of the unique source component is
\(D^b\), which is symmetric under slot permutations. Every term in
the coefficient extraction (N.1) puts \(rL=b+1\) copies of the
common vector into \(b\) determinant factors. At least one factor
receives two copies and is zero by alternating multilinearity.
Thus \(T_{r,L,b}(D^b)=0\). Equivariance kills its entire irreducible
component, proving the second line of the band classification.

No other source component belongs to this band by (N.17). Combined
with R-018, the unclassified boundary components therefore satisfy
both

\[
\boxed{\lambda_1\ge rL+1,\qquad
       \lambda_2\ge(r-1)L.}
\tag{N.18}
\]

The determinant component in the odd case is already explicitly
classified and is not included in this remaining range. Statements
R-011, R-012, R-015 and R-016 give additional complete finite kernels;
(N.18) is a uniform consequence of the exact maps proved here.


# Canonical-map ranges below the full square bound

Statements **R-021**, **R-022**, and **R-023**. Written and checked on
21 November 2026 UTC by GPT-6 Astra Pro, `/root/rectangular_cases`;
effort setting not exposed. The prime-interval input is Nagura's
established theorem. The square determinant scalars are the established
prime-adjacent Alon–Tarsi cases in R-007. The exact specialization and
multiplication maps are G-013. The common-polarization inputs are
R-018–R-020. No historical novelty claim is made.

## Exact canonical-map convention

The normalized grid map is

\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
\longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a.
\tag{K.1}
\]

It is the degree-\(b\) part of the graded algebra map \(\mu_a\) of
R-008–R-009. Symmetric powers are embedded in tensors by normalized
averaging. Taking the transpose of the row and column orthogonal
averaging projectors gives the opposite grid map \(h_{a,b}\). Thus

\[
\mathcal K_{a,b}(W):=\ker\!\left(
h_{a,b}:\operatorname{Sym}^{a}(\operatorname{Sym}^{b}W)
\to\operatorname{Sym}^{b}(\operatorname{Sym}^{a}W)\right)
\tag{K.2}
\]

is, for \(W=V^*\), the annihilator of the image in (K.1).
The standard perfect symmetric-tensor pairings identify these maps
without a scalar change. In particular absence of the label
\(\lambda\) from (K.2) proves surjectivity of (K.1) onto its entire
target \(\lambda\)-isotypic component.

## R-021. Every even-rank boundary determinant is in the canonical image

For every even integer \(a\ge4\), put \(B=a(a-2)\). Then

\[
\boxed{
[S_{(B^a)}V:\operatorname{im}h_{B,a}]
=[S_{(B^a)}V:\operatorname{Sym}^a(\operatorname{Sym}^BV)]
=1\qquad(\dim V\ge a).}
\tag{K.3}
\]

The proof supplies an explicit rational preimage of the normalized
determinant tensor \(I_{a,B}\). In smaller dimensions that Schur
functor is zero.

### 1. The exact seed preimages

For every odd prime \(p\), R-007 gives nonzero square scalars
\(c_{p-1}\) and \(c_{p+1}\), with

\[
h_{w,w}(I_{w,w})=c_w I_{w,w},
\qquad w=p-1\text{ or }p+1.
\]

For \(w\ge a\), let \(E=\mathbf Q^a\), enlarge it to
\(U=E\oplus\mathbf Q^{w-a}\), and write
\(z_{a+1},\ldots,z_w\) for the added basis covectors. The linear map

\[
j:\operatorname{Sym}^aE^*\longrightarrow\operatorname{Sym}^wU^*,
\qquad F\longmapsto Fz_{a+1}\cdots z_w
\tag{K.4}
\]

has its ordinary dual \(j^*:\operatorname{Sym}^wU\to
\operatorname{Sym}^aE\) under the normalized symmetric pairings.
Define

\[
u_{a,w}=\operatorname{Sym}^w(j^*)\bigl(I_{w,w}/c_w\bigr).
\tag{K.5}
\]

The exact equality is

\[
h_{w,a}(u_{a,w})=I_{a,w}.
\tag{K.6}
\]

To check the scalar, let \(\Pi_d\) multiply \(d\) linear forms.
Appending the fixed forms \(z_{a+1},\ldots,z_w\) gives a map
\(\iota\) of ordered factors with
\(j\circ\Pi_a=\Pi_w\circ\iota\). Pullback of this identity gives
\(h_{w,a}\operatorname{Sym}^w(j^*)=\iota^*h_{w,w}\).
The determinant with the appended coordinate forms has a block
identity matrix, so
\(\iota^*(\det_w^w)=\det_a^w\) with scalar one. These equations
prove (K.6), with every normalization contained in the actual dual
map \(j^*\).

The algebra identities already proved in R-009 and G-013 give

\[
h_{B,a}\left(\prod_w u_{a,w}^{e_w}\right)
=I_{a,B},\qquad B=\sum_w e_w w.
\tag{K.7}
\]

Indeed \(\mu_a\) is an algebra morphism and
\(I_{a,w}I_{a,w'}=I_{a,w+w'}\), as verified by evaluation on arbitrary
ordered covectors.

### 2. A prime and explicit nonnegative exponents for every \(a\)

For \(a=4,6,\ldots,24\), the following table provides a square seed
of width exactly \(a\):

\[
\begin{array}{c|rrrrrrrrrrr}
a&4&6&8&10&12&14&16&18&20&22&24\\\hline
p&3&5&7&11&11&13&17&17&19&23&23\\
a=p\pm1&+1&+1&+1&-1&+1&+1&-1&+1&+1&-1&+1.
\end{array}
\tag{K.8}
\]

Each displayed \(p\) is prime. Thus \(u_{a,a}^{a-2}\) is a
preimage of \(I_{a,a(a-2)}\) by (K.7).

For every even \(a\ge26\), Nagura's theorem supplies a prime

\[
a<p<\frac65a.
\tag{K.9}
\]

The exact primary locator is Jitsuro Nagura, *On the interval
containing at least one prime number*, **Proceedings of the Japan
Academy 28** (1952), 177–181, the unnumbered **Theorem on printed
p. 180, case \(n=5\)**, with proof completed on p. 181.
Official full article:
<https://www.jstage.jst.go.jp/article/pjab1945/28/4/28_4_177/_pdf>;
DOI <https://doi.org/10.3792/pja/1195570997>.
Only its range \(x>25\) is needed here, so no endpoint convention
at \(x=25\) affects this proof.

Put \(g=(p-1)/2\). The two permitted widths \(p-1,p+1\) are at
least \(a\), and their normalized values are \(g,g+1\). Their exact
even conductor is \(2g(g-1)\), as proved in G-013 by the explicit
residue representation. Here the needed inequality follows directly:

\[
2g(g-1)=\frac{(p-1)(p-3)}2
<\frac{p^2}2<\frac{18a^2}{25}<a(a-2)=B,
\tag{K.10}
\]

where the last strict inequality holds for every \(a\ge26\).
For complete explicitness, set

\[
N=B/2,\qquad y=N-g\lfloor N/g\rfloor,\qquad
x=\lfloor N/g\rfloor-y.
\tag{K.11}
\]

Then \(0\le y\le g-1\), and (K.10) implies
\(\lfloor N/g\rfloor\ge g-1\), so \(x\ge0\). The identity
\(N=xg+y(g+1)\) is immediate from (K.11). Consequently

\[
\boxed{
h_{B,a}(u_{a,p-1}^{x}u_{a,p+1}^{y})=I_{a,B}\ne0.}
\tag{K.12}
\]

The target determinant multiplicity is one for even \(B\) by
R-001. Equations (K.8) and (K.12) prove (K.3) for every even
\(a\ge4\). This is a transfer of the checked prime-interval and
prime-adjacent scalar results through explicit algebra morphisms.

### A uniform determinant-image range and its row extensions

The same construction gives a uniform range for every integer rank
\(a\ge26\), with no parity restriction on \(a\): for every even

\[
B\ge2\left\lceil\frac{9a^2}{25}\right\rceil,
\qquad s\ge0,
\tag{K.12a}
\]

there is the explicit nonzero image

\[
\boxed{
h_{B+s,a}\left(u_{a,p-1}^{x}u_{a,p+1}^{y}(e_1^a)^s\right)
=I_{a,B}(e_1^{\otimes a})^s\ne0,}
\tag{K.12b}
\]

where \(p\) is any prime from (K.9), and \(x,y\) are given by
(K.11) with this value of \(B\). Indeed
\(g(g-1)<9a^2/25\le B/2\), so the same proof gives nonnegative
integer exponents and \(B=x(p-1)+y(p+1)\). Applying the graded
algebra map proves (K.12b) exactly.

The target weight is
\(\lambda=(as+B,B^{a-1})\). Its target and image multiplicities
are both one. For the target, the balanced Cauchy module is
\(S_\lambda\mathbf Q^a\simeq\det^B\otimes
\operatorname{Sym}^{as}\mathbf Q^a\). After removing the determinant
weight, its balanced weight is \((s^a)\), with sole monomial
\(x_1^s\cdots x_a^s\). Slot permutations fix this vector because
\(B\) is even. Nonvanishing of (K.12b) follows by evaluating its
target on covectors: it becomes a determinant power times the
nonzero product of first-coordinate powers. These are actual
canonical images for the full range (K.12a).

## R-022. The canonical surjectivity ranges

Let \(a\ge3\), and put \(r=a-1\). The following are unconditional
component ranges for the actual map (K.1), in every finite dimension.

For every integer

\[
r^2-r+1\le b\le r^2-1,
\]

the map is surjective onto every target isotypic component with

\[
\boxed{\lambda\vdash ab,\qquad \lambda_2\le b-r.}
\tag{K.13}
\]

At the upper boundary \(b=r^2-1\), the larger stated range is

\[
\boxed{\lambda\vdash ab,\qquad
\lambda_1\le r^2\quad\text{or}\quad
\lambda_2\le r(r-1)-1.}
\tag{K.14}
\]

Thus the rank on each such multiplicity space equals its full target
plethysm coefficient. In particular the coefficient inequality in
that component follows from this rank statement. The proof below
tracks the annihilator into the common-polarization kernel and then
removes its rectangular summand by an exact prolongation identity.

### 3. An explicit injection from the canonical annihilator

For all \(b\) in the stated interval, let \(m=b-r\). Then

\[
m\ge(r-1)^2\ge1.
\tag{K.15}
\]

Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a graded
inner factor*, v1, **Theorem 1.3**, gives surjectivity of
\(h_{m,r}\). Its complete proof in §2.2 and its power-polarization
Lemma 2.1 were read in this run. The author's primary PDF is
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.
For \(r=2,m=1\), this lower map is directly the identity
\(\operatorname{Sym}^2V\to\operatorname{Sym}^2V\), as the source
also explicitly records.

Let \(W=V^*\) and \(F\in\mathcal K_{a,b}(W)\). Its corresponding
symmetric \(a\)-linear form on \(\operatorname{Sym}^bV\) is denoted
\(\mathcal A_F\). The annihilator condition is the exact identity

\[
\mathcal A_F(P,\ldots,P)=0
\quad\text{for every }P=u_1\cdots u_b.
\tag{K.16}
\]

Indeed (K.1) has image spanned by precisely these diagonal tensors.

Fix a product \(Q=y_1\cdots y_m\). The polynomial
\((x^r+c\,t^r)Q\) is a product of \(b\) vectors over \(\mathbf C\),
because its binary degree-\(r\) factor splits into linear factors.
The coefficient of \(c\) in (K.16), divided by the nonzero integer
\(a\), gives

\[
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{K.17}
\]

Define
\(G_x(y_1,\ldots,y_m,t)=
\mathcal A_F(x^rQ,\ldots,x^rQ,t^b)\).
It has degree \(b\) in \(t\) and degree \(r\) in each \(y_i\).
The exact differential identity is

\[
D_{y_m,t}\cdots D_{y_1,t}G_x
=\frac{b!}{r!}
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{K.18}
\]

Before the \(i\)-th differentiation, the relevant degrees are
\(p=b-i+1\) and \(s=r\), so \(p-s=m-i+1\ge1\). Sra's
Lemma 2.1 with power one proves injectivity of each step, with all
other variables as spectators. Hence \(G_x=0\).

For fixed \(x,t\), this vanishing is the diagonal of an \(r\)-linear
symmetric form on \(\operatorname{Sym}^mV\), evaluated on all
products \(Q\). The already established surjectivity of \(h_{m,r}\)
therefore gives

\[
\mathcal A_F(x^rQ_1,\ldots,x^rQ_r,t^b)=0
\quad(Q_i\in\operatorname{Sym}^mV).
\tag{K.19}
\]

Represent \(F\) by its polynomial
\(f(v_1,\ldots,v_r;t)=
\mathcal A_F(v_1^b,\ldots,v_r^b,t^b)\).
The exact coefficient-extraction calculation now is

\[
(T_{r,r,b}\otimes\mathrm{id})f
=\binom{b}{r}^{r}
\mathcal A_F(x^rv_1^m,\ldots,x^rv_r^m,t^b)=0.
\tag{K.20}
\]

No injectivity assertion about the last common-polarization step
has been inserted into this argument.

The normalized last-slot inclusion is the natural injective map

\[
\begin{aligned}
\delta:\operatorname{Sym}^{r+1}(\operatorname{Sym}^bW)
&\longrightarrow
\operatorname{Sym}^r(\operatorname{Sym}^bW)
\otimes\operatorname{Sym}^bW,\\
w_0\cdots w_r&\longmapsto
\frac1{r+1}\sum_{i=0}^r
\left(\prod_{j\ne i}w_j\right)\otimes w_i.
\end{aligned}
\tag{K.21}
\]

Multiplying the two tensor factors is a left inverse, proving
injectivity. In the invariant-tensor realization (K.21) is simply
inclusion of the fully symmetric tensors into the tensors symmetric
in the first \(r\) slots. Equation (K.20) consequently proves the
actual natural injection

\[
\boxed{
\delta:\mathcal K_{a,b}(W)\hookrightarrow
\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW.}
\tag{K.22}
\]

### 4. Proof of the second-row range

R-018 proves that every constituent \(S_\nu W\) of
\(\ker T_{r,r,b}\) has \(\nu_2\ge b-r+1\).
Pieri's rule for tensoring by \(\operatorname{Sym}^bW\) gives

\[
\lambda_1\ge\nu_1\ge\lambda_2\ge\nu_2
\ge\lambda_3\ge\cdots.
\tag{K.23}
\]

In particular \(\lambda_2\ge\nu_2\). The injection (K.22) proves
that no annihilator component can have \(\lambda_2\le b-r\).
By the exact duality (K.2), this is precisely the component
surjectivity assertion (K.13).

## R-023. An exact rectangular prolongation identity

Let \(r\ge2\), let \(b\ge0\) be even, and set \(a=r+1\). Regard the
unique source copy of \(S_{(b^r)}W\) inside
\(\operatorname{Sym}^r(\operatorname{Sym}^bW)\) using the determinant
highest vector and its \(GL(W)\)-span. Inside the target of (K.21),
the following is an equality of actual submodules:

\[
\boxed{
\delta\bigl(\operatorname{Sym}^{a}(\operatorname{Sym}^bW)\bigr)
\cap\bigl(S_{(b^r)}W\otimes\operatorname{Sym}^bW\bigr)
=\delta\bigl(S_{(b^a)}W\bigr).}
\tag{K.24}
\]

### Proof

Use the polynomial-generator realization with \(a\) vector slots.
The Cauchy decomposition for the first \(r\) slots has its
\(GL(W)\)-type \((b^r)\) paired with
\(S_{(b^r)}\mathbf Q^r=(\det\mathbf Q^r)^b\). Consequently every
polynomial in the left-hand intersection is invariant under every
elementary transvection mixing two of the first \(r\) slots. In
coordinates, it is killed by all the slot derivations

\[
E_{ij}^{\mathrm{slot}}
=\sum_u X_{u,i}\frac{\partial}{\partial X_{u,j}},
\qquad i\ne j,\quad1\le i,j\le r.
\tag{K.25}
\]

The polynomial is fully symmetric in all \(a\) slots. Conjugating
(K.25) by slot permutations therefore shows that it is killed by
the corresponding derivation for every ordered pair \(i\ne j\)
among all \(a\) slots. Exponentiation of these locally nilpotent
derivations proves invariance under \(SL_a\) acting on the slot
space. The Cauchy decomposition for all \(a\) slots identifies
its invariant part: only the determinant characters on the slot
factor can restrict trivially to \(SL_a\). The total degree is
\(ab\), so that character is exactly \(\det^b\), paired with
\(S_{(b^a)}W\). This proves inclusion in the right side of (K.24).

Conversely, that Cauchy summand has slot action \(\det^b\).
It is fixed by all slot permutations because \(b\) is even.
Restriction to the first \(r\) slots is again \(\det^b\), so
its image under (K.21) lies in the displayed rectangular first
factor. This proves the reverse inclusion and the equality.
The argument works in every dimension; a Schur functor exceeding
the ambient dimension contributes zero on both sides.

### 5. The sharper critical-boundary injection and proof of (K.14)

Now take \(b=r^2-1\). For even \(r\), R-018–R-020 prove that every
constituent \(S_\nu W\) of the common-polarization kernel satisfies

\[
\nu_1\ge r^2+1,\qquad \nu_2\ge r(r-1).
\tag{K.26}
\]

For odd \(r\), those same bounds hold after removing the unique
rectangular summand \(S_{(b^r)}W\), which R-020 proves is in the
kernel. Let \(\mathcal N_r\) denote the common kernel in the even
case, and this complementary sum of isotypic components in the odd
case. The projection to \(\mathcal N_r\) is explicit and natural:
on tensor degree \(rb\), remove the central Schur projector

\[
e_{(b^r)}=
\frac{\dim[(b^r)]}{(rb)!}
\sum_{\sigma\in S_{rb}}\chi^{(b^r)}(\sigma)\sigma
\tag{K.27}
\]

in the odd case; use the identity in the even case. Centrality
makes this projector commute with the tensor symmetrizations
defining the source and the common-polarization map.

For odd \(r\), the composite of (K.22) with this projection can
have kernel only in the intersection (K.24), hence only in
\(S_{(b^a)}W\). Here \(a=r+1\) is even and
\(b=r^2-1=a(a-2)\). R-021 proves that the original canonical map
is nonzero on its multiplicity-one target determinant component.
By (K.2), its annihilator has zero intersection with
\(S_{(b^a)}W\). The composite projection is therefore injective.
In the even case injectivity already follows from (K.22). Thus in
both parities there is the exact natural injection

\[
\boxed{
\mathcal K_{r+1,r^2-1}(W)
\hookrightarrow\mathcal N_r(W)\otimes
\operatorname{Sym}^{r^2-1}W,}
\tag{K.28}
\]

given explicitly by (K.21) and (K.27), whose first factor has only
the types (K.26).

Pieri interlacing (K.23) now forces every annihilator label to have
\(\lambda_1\ge r^2+1\) and
\(\lambda_2\ge r(r-1)\). This is exactly the complement of the
surjectivity range (K.14). The proof removes the rectangular
contraction by its actual prolongation and canonical preimage,
rather than discarding it by a parity assertion.

### 6. Exact integer-interval description of the candidate support

For completeness, pad \(\lambda\) to \(a=r+1\) parts. A partition
\(\nu\vdash rb\) satisfying both (K.26) and the Pieri interlacing
(K.23) exists exactly for the following explicit integer region:

\[
\begin{aligned}
\lambda_1&\ge b+2,\\
\lambda_2&\ge b-r+1,\\
\max(0,b+2-\lambda_2)+\max(0,b-r+1-\lambda_3)
&\le\lambda_1-b.
\end{aligned}
\tag{K.30}
\]

This gives a necessary support region for the canonical annihilator
via (K.28), not an assertion that every label in it occurs.
To prove the equivalence, choose independently
\(\nu_i\in[\lambda_{i+1},\lambda_i]\), \(1\le i\le r\),
raising the first two lower bounds to \(b+2,b-r+1\).
Their individual feasibility is precisely the first two lines.
Ordering is automatic because
\(\nu_i\ge\lambda_{i+1}\ge\nu_{i+1}\). The sum of the lower
bounds is \(ab-\lambda_1\) plus the two maxima in (K.30), and
the sum of the upper bounds is \(ab-\lambda_{r+1}\ge rb\), since
\(\lambda_{r+1}\le b\). Sums of independent integer intervals
fill every integer between their lower and upper sums. Existence
of sum \(rb\) is therefore exactly the last line of (K.30).

For \(r\ge3\), that last inequality follows already from the
first two and the partition size. Here is a complete check, which
prevents counting it as an additional range in those ranks. Set
\(x=\lambda_1-b\), \(y=\lambda_2-b\), and
\(z=\lambda_3-b\). Then

\[
x\ge2,\quad y\ge1-r,\quad z\le y,\quad
x\ge y,\quad x\ge-y-(r-1)z.
\]

The desired inequality is
\(\max(0,2-y)+\max(0,1-r-z)\le x\).
For \(y\ge2,z\ge1-r\), its left side is zero.
For \(y\ge2,z=-q\le-r\), the two lower bounds on \(x\)
give \(x\ge(r-1)q/2\ge q-r+1\).
For \(y\le1,z\ge1-r\), the assertion is \(x+y\ge2\):
this follows from \(x\ge2\) at \(y=0,1\), and from
\(x+y\ge-(r-1)z\ge-(r-1)y\ge r-1\ge2\) at \(y\le-1\).
Finally, for \(y\le1,z=-q\le-r\), the lower bound
\(x\ge(r-1)q-y\) exceeds the required \(q-y-r+3\) by
\((r-2)q+r-3\ge0\). These cases exhaust the integer possibilities.

At \(r=2,b=3\), no such \(\nu\) exists at all: (K.26) would
give \(\nu_1+\nu_2\ge5+2>rb=6\). Thus (K.28) proves that
the full map \(h_{3,3}\) is an isomorphism. This edge case agrees
with the classical result of Hadamard, stated with its complete
proof in Landsberg, *Geometric complexity theory: an introduction
for geometers*, [arXiv:1305.7387v3](https://arxiv.org/pdf/1305.7387),
**Theorem 7.22, §7.8, printed p. 24**. That statement and proof
were independently read here.

## Parameter checks and concrete families

The smallest parameter in (K.13) is \(a=3,r=2,b=3\), where
\(m=b-r=1\), the lower grid map is the identity, and the
power-one injectivity in (K.18) has degree excess one. The critical
second-row range is \(\lambda_2\le1\), and the first-row range
is \(\lambda_1\le4\). The sole nonzero target component in that
first-row band is \((4,4,1)\), by the complement/Specht calculation
of R-020 with \(a=3,H=4\). Thus no unavailable induction base
or negative residual degree is used.

At the critical boundary, the complete first-row target band itself
has a particularly simple description. Applying the same explicit
complementary pairing and multilinear map from R-020 with \(a\)
slots and \(H=b+1\) gives

\[
\bigoplus_{\lambda_1\le b+1}
\left(\operatorname{Sym}^a(\operatorname{Sym}^bV)\right)_\lambda
=
\begin{cases}
S_{((r^2)^r,r^2-r-1)}V,&r\text{ even},\\
S_{((r^2-1)^{r+1})}V,&r\text{ odd}.
\end{cases}
\tag{K.29}
\]

Each displayed component has multiplicity one and is entirely in the
canonical image by (K.14). Examples are \((a,b)=(5,15)\) with
\(\lambda=(16,16,16,16,11)\), and \((a,b)=(7,35)\) with
\(\lambda=(36,36,36,36,36,36,29)\). In even outer degree the
determinant examples are \((a,b)=(4,8),(6,24),(8,48)\), and (K.3)
covers every even \(a\ge4\).

The full canonical map remains governed by the remaining components
in (K.28). The statements above prove the displayed entire isotypic
ranges, without asserting vanishing of the remaining varying
common-polarization kernel.

### Explicit positive ranks on equal-middle-row families

The component surjectivity combines directly with the already proved
T-025 end-shape formula. For every \(a\ge3\), \(r=a-1\),
\(r^2-r+1\le b\le r^2-1\), and
\(0\le\gamma\le\beta\le b-r\), put

\[
\lambda=(ab-(a-2)\beta-\gamma,\beta^{a-2},\gamma),
\qquad R=\beta-\gamma-\binom a2(\beta\bmod2).
\]

This is a partition: its first part is at least
\(ab-(a-1)\beta\ge b+r^2\ge\beta\).
Its second part satisfies the exact range (K.13), and \(b\ge\beta\).
Therefore its actual canonical image multiplicity is

\[
\boxed{
[S_\lambda V:\operatorname{im}h_{b,a}]
=\#\{(c_2,\ldots,c_a)\in\mathbf Z_{\ge0}^{a-1}:
2c_2+3c_3+\cdots+ac_a=R\}.}
\tag{K.31}
\]

For dimensions at least the length of \(\lambda\), this count is
positive exactly for \(R=0\) or \(R\ge2\), because parts two and
three already represent every integer at least two. Negative right
sides and \(R=1\) give zero. Examples are \(a=4,b=7\),
\(\lambda=(20,4,4)\), with image multiplicity two, and
\(a=5,b=13\), \(\lambda=(41,8,8,8)\), with image multiplicity five.
Formula (K.31) records the exact map rank of the known positive
coefficient formula throughout these concrete parameter families.


# A recursive second-row range for the canonical map

Statement **R-024**. Written and checked on 21 November 2026 UTC by
GPT-6 Astra Pro, agent /root/rectangular_cases; effort setting not exposed.
The canonical degree-five base is the established result of
Cheung–Ikenmeyer–Mkrtchyan and McKay. The component argument below uses
the explicit common-polarization injectivity R-018. No historical
novelty claim is made.

## 1. The unconditional range and its exact map

Let \(V\) be any finite-dimensional vector space over a field of
characteristic zero. For every integer \(a\ge6\), set

\[
C_a=\binom a2-10=5+6+\cdots+(a-1).
\tag{P.1}
\]

For every \(b\ge C_a+6\), and every partition

\[
\lambda\vdash ab,\qquad \lambda_2\le b-C_a,
\tag{P.2}
\]

the canonical map

\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
\longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a,
\tag{P.3}
\]

is surjective onto the entire target \(\lambda\)-isotypic component.
The assertion includes all multiplicities and all dimensions; a Schur
functor with too many rows evaluates to zero. A missing second part is
zero. Equivalently, the explicit parameter range is

\[
\boxed{
a\ge6,\qquad b\ge\binom a2-4,\qquad
\lambda_2\le b-\binom a2+10.}
\tag{P.4}
\]

For example the ranges for \(a=6,7,8,9\) respectively are

\[
\begin{array}{c|c|c}
a&\text{inner degree}&\text{second row}\\\hline
6&b\ge11&\lambda_2\le b-5\\
7&b\ge17&\lambda_2\le b-11\\
8&b\ge24&\lambda_2\le b-18\\
9&b\ge32&\lambda_2\le b-26.
\end{array}
\tag{P.5}
\]

All symmetric powers in (P.3) use normalized averaging in the tensor
realization. Each averaging projector is self-adjoint for the tensor
pairing. Writing the grid map as target averaging composed with grid
permutation on the source invariant subspace, its transpose is source
averaging composed with the inverse permutation on the target
invariant subspace. This is the opposite grid map, with scalar one.
Therefore, for \(W=V^*\), the image
annihilator is exactly

\[
\mathcal K_{a,b}(W)
=\ker\left[h_{a,b}:\operatorname{Sym}^{a}(\operatorname{Sym}^{b}W)
\longrightarrow\operatorname{Sym}^{b}(\operatorname{Sym}^{a}W)\right].
\tag{P.6}
\]

We prove that its \(\lambda\)-isotypic component is zero in (P.4).
This proves the asserted surjectivity by the perfect symmetric-tensor
pairing, including the map on each multiplicity space.

## 2. The established full degree-five base

The exact input is

\[
\mathcal K_{5,b}(W)=0\qquad\text{for every }b\ge6.
\tag{P.7}
\]

Cheung–Ikenmeyer–Mkrtchyan, *Symmetrizing tableaux and the 5th case of
the Foulkes conjecture*, arXiv:1509.03944v1, **Theorem 6(a), printed
p. 3**, proves injectivity of \(\Psi_{5,6}\). Their displayed definition
on printed p. 2 is the composition of the symmetric-tensor inclusion,
the transpose of the \(5\times6\) tensor grid, and symmetric projection.
It is precisely \(h_{5,6}\) under the convention (P.3). Applying McKay's
propagation theorem to this established base gives (P.7). A complete
primary proof of that propagation is Christian Ikenmeyer, *On McKay's
propagation theorem for the Foulkes conjecture*, arXiv:1509.04957,
**Theorem 1.3, printed p. 2**, with proof in §§2–6, printed pp. 3–8.
Its definition of \(\Psi_{a\times b}\), also on printed p. 2, is the
same inclusion, grid transpose, and projection, so its conclusion
applies to these actual maps. The official full texts are

- <https://arxiv.org/pdf/1509.03944>
- <https://arxiv.org/pdf/1509.04957>.

The source input is injectivity of the precise transpose map in (P.6).
The source computation for
Theorem 6(a) is an exact integer computation described and justified
in §§2–5; its original large evaluation matrices were not regenerated
in this run. The propagation proof was read in full. The scalar audit
in §6 below records the harmless normalization corrections in its
auxiliary raising-operator displays.

The sources work in sufficiently large dimension. Their injectivity
implies (P.7) in every smaller dimension by the actual inclusion
\(W\hookrightarrow W\oplus W'\): both symmetric-power functors preserve
this inclusion, and the grid maps commute with it. A vector in the
smaller kernel would map to a vector in the zero larger kernel. All
maps are rational, so extension to characteristic-zero fields
preserves the assertion.

## 3. An exact intermediate-annihilator morphism

We now construct the map needed for the induction. For every

\[
a=r+1\ge3,\qquad b\ge r,\qquad m=b-r\ge0,
\tag{P.8}
\]

let

\[
\begin{aligned}
\delta:\operatorname{Sym}^{r+1}(\operatorname{Sym}^{b}W)
&\longrightarrow
\operatorname{Sym}^{r}(\operatorname{Sym}^{b}W)
\otimes\operatorname{Sym}^{b}W,\\
w_0\cdots w_r&\longmapsto
\frac1{r+1}\sum_{i=0}^{r}
\left(\prod_{j\ne i}w_j\right)\otimes w_i.
\end{aligned}
\tag{P.9}
\]

Multiplication of the two tensor factors is a left inverse. Thus
\(\delta\) is injective. In the normalized invariant-tensor model it is
the inclusion of fully symmetric tensors into tensors symmetric in
the first \(r\) slots.

The common-polarization map is the coefficient map

\[
T_{r,r,b}f(v_1,\ldots,v_r;x)
=[t_1^r\cdots t_r^r]
f(v_1+t_1x,\ldots,v_r+t_rx).
\tag{P.10}
\]

It has target
\(\operatorname{Sym}^{r^2}W\otimes
\operatorname{Sym}^{r}(\operatorname{Sym}^{m}W)\).
There is an actual restriction of the composite map

\[
\boxed{
\Theta_{a,b}:=(T_{r,r,b}\otimes\mathrm{id})\delta:
\mathcal K_{a,b}(W)\longrightarrow
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,m}(W)\otimes\operatorname{Sym}^{b}W.}
\tag{P.11}
\]

The codomain in (P.11) retains the full lower annihilator. Here is a
complete proof of this membership.

Work over \(\mathbf C\), which suffices because the map is rational.
For \(F\in\mathcal K_{a,b}(W)\), denote its corresponding symmetric
\(a\)-linear form on \(\operatorname{Sym}^{b}V\) by \(\mathcal A_F\).
The kernel condition (P.6) says exactly

\[
\mathcal A_F(P,\ldots,P)=0
\quad\text{for all }P=u_1\cdots u_b.
\tag{P.12}
\]

Fix \(Q=y_1\cdots y_m\). The form
\((x^r+c\,t^r)Q\) is a product of \(b\) linear factors over
\(\mathbf C\): the degree-\(r\) binary factor splits, also when \(x,t\)
are linearly dependent. Take the coefficient of \(c\) in (P.12) and
divide by \(a\). The result is

\[
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{P.13}
\]

Put

\[
G_x(y_1,\ldots,y_m;t)
=\mathcal A_F(x^rQ,\ldots,x^rQ,t^b).
\]

For \(D_{y,t}=y\cdot\partial_t\), ordinary differentiation gives the
exact equation

\[
D_{y_m,t}\cdots D_{y_1,t}G_x
=\frac{b!}{r!}
\mathcal A_F(x^rQ,\ldots,x^rQ,t^rQ)=0.
\tag{P.14}
\]

Before step \(i\), the degrees in \(t,y_i\) are \(b-i+1,r\).
Their difference is \(m-i+1\ge1\). The operator \(D_{y_i,t}\) is
injective on every such space. To verify the coefficient, put
\(p=b-i+1\), \(q=r\), and decompose under the \(GL_2\) action mixing
\(t,y_i\). A summand containing weight \((p,q)\) has the form
\(\det^j\otimes\operatorname{Sym}^{p+q-2j}\mathbf C^2\), with
\(j\le q<p\). Its weight vector is the determinant factor times
\(e_t^{p-j}e_y^{q-j}\). The ordinary raising operator sends it to
\((p-j)e_t^{p-j-1}e_y^{q-j+1}\) times the same determinant factor,
which is nonzero. This verifies injectivity on every multiplicity
space as well. Equivalently
this is Sra's Lemma 2.1 with power one. All other variables are
spectators. Starting with the last map in the composition and
successively using these injective restrictions gives \(G_x=0\).
For \(m=0\), (P.13) already states \(G_x=0\), with no derivatives;
the degree-zero grid map is the identity of \(\mathbf Q\).

For fixed \(x,t\), the symmetric \(r\)-linear form

\[
(Q_1,\ldots,Q_r)\longmapsto
\mathcal A_F(x^rQ_1,\ldots,x^rQ_r,t^b)
\tag{P.15}
\]

has zero diagonal on every \(Q=y_1\cdots y_m\). By the exact
definition (P.6), with \(a,b\) replaced by \(r,m\), it belongs to
\(\mathcal K_{r,m}(W)\). The coefficient calculation in the original
vector slots is

\[
\Theta_{a,b}F(v_1,\ldots,v_r;x,t)
=\binom br^{r}
\mathcal A_F(x^rv_1^m,\ldots,x^rv_r^m,t^b).
\tag{P.16}
\]

Its degrees in \(x,t\) are \(r^2,b\). Evaluation at all \(x,t\)
separates both symmetric-power spaces. Applying the lower grid map
to the middle factor of (P.16) therefore gives zero as a tensor,
because it gives zero under every such evaluation by (P.15).
This proves precisely the membership (P.11). The factors \(b!/r!\)
and \(\binom br^r\) in (P.14) and (P.16) also fix all normalizations.

## 4. Proof of the recursive component range

Set \(C_5=0\), so that for every \(a\ge6\), with \(r=a-1\),

\[
C_a=r+C_r.
\tag{P.17}
\]

Prove (P.4) by induction on \(a\), using the full base (P.7).
Fix \(a\ge6\), \(b\ge C_a+6\), and a partition \(\lambda\) satisfying
(P.2). Write \(s=b-C_a\ge6\) and \(m=b-r\). Then

\[
m\ge C_r+6,\qquad m-C_r=s,\qquad s\le m.
\tag{P.18}
\]

The last inequality uses \(C_r\ge0\), including \(r=5\).

First restrict (P.9) to the entire \(\lambda\)-isotypic component.
Pieri's rule says that every type \(\nu\) in its first tensor factor
satisfies \(\lambda/\nu\) horizontal of size \(b\), and in particular

\[
\nu_2\le\lambda_2\le s\le m=b-r.
\tag{P.19}
\]

R-018, applied with \(L=r\), proves that \(T_{r,r,b}\) is injective
on every entire \(\nu\)-isotypic component in (P.19). Their direct sum
is therefore an injective restriction too: images of distinct types
lie in distinct isotypic components of its target, and the statement
for one type already includes its full multiplicity space. Tensoring
by \(\operatorname{Sym}^{b}W\) preserves this injectivity. Since
\(\delta\) itself is injective, the composite in (P.11) is injective
on the \(\lambda\)-isotypic component of \(\mathcal K_{a,b}(W)\).

Next consider its codomain in (P.11). At \(r=5\) the middle factor
is zero by (P.7) and \(m\ge6\). At every \(r\ge6\), the induction
statement and (P.18) give

\[
\mathcal K_{r,m}(W)
\subseteq
\bigoplus_{\kappa_2\ge s+1}
\left(\operatorname{Sym}^{r}(\operatorname{Sym}^{m}W)\right)_\kappa.
\tag{P.20}
\]

Tensoring one of these types with the two row representations
\(\operatorname{Sym}^{r^2}W\) and \(\operatorname{Sym}^{b}W\) applies
Pieri twice. Each added horizontal strip only increases row lengths,
so every resulting type \(\xi\) contains \(\kappa\), and
\(\xi_2\ge\kappa_2\ge s+1\). The codomain of (P.11) consequently
has no \(\lambda\)-isotypic component with \(\lambda_2\le s\).

The injective restriction just proved thus maps the specified
\(\lambda\)-component into zero. That component is zero. Equation
(P.6) proves the claimed canonical surjectivity, completing the
induction for every \(a\ge6\).

The proof uses whole isotypic components at both stages and retains
every copy of each Schur functor.

## 5. Explicit positive ranks in the new parameter range

Here is an unconditional family with a closed positive counting
formula. Take the parameters in (P.4), let

\[
0\le\gamma\le\beta\le b-C_a,\qquad
\lambda=(ab-(a-2)\beta-\gamma,\beta^{a-2},\gamma),
\qquad
R=\beta-\gamma-\binom a2(\beta\bmod2).
\tag{P.21}
\]

This is a partition. Its first part is at least
\(ab-(a-1)\beta\ge b+(a-1)C_a\ge\beta\).
The exact end-sector formula T-025 applies, since \(b\ge\beta\).
It computes the target multiplicity as

\[
p_{2,\ldots,a}(R)
=\#\{(c_2,\ldots,c_a)\in\mathbf Z_{\ge0}^{a-1}:
             2c_2+3c_3+\cdots+ac_a=R\}.
\tag{P.22}
\]

The set is empty for negative \(R\). Combining (P.4) with this exact
target multiplicity gives the actual rank on multiplicity spaces:

\[
\boxed{
\operatorname{rank}\operatorname{Hom}_{GL(V)}(S_\lambda V,h_{b,a})
=[S_\lambda V:\operatorname{im}h_{b,a}]
=p_{2,\ldots,a}(R).}
\tag{P.23}
\]

Here \(\dim V\ge\ell(\lambda)\); in smaller dimensions the Schur
functor vanishes. Because \(2,3\) are permitted parts, the number
in (P.22) is positive exactly for \(R=0\) or \(R\ge2\). The
construction \(R=2u\), or \(R=3+2u\), supplies a solution for each
such positive \(R\).

For every \(a\ge6\) and every \(b\ge\binom a2-4\), the specific
partition

\[
\lambda=(ab-6a+12,6^{a-2})
\tag{P.24}
\]

has canonical image multiplicity \(4\), given by the four solutions
of (P.22) at \(R=6\): the partitions \(6\), \(4+2\), \(3+3\), and
\(2+2+2\). In particular \(h_{11,6}\) is surjective onto all four
copies of \(S_{(42,6,6,6,6)}V\) in its target.

## 6. Source-normalization audit

Ikenmeyer's appendix defines its auxiliary tensor raising operator
on degree \(d\) by
\(\phi_{ij}=d^{-1}\sum_{p=1}^{d}\zeta_{ij}^{(p)}\).
Consequently its two-operator composition is exactly

\[
\phi_{ij}\phi_{i'j'}
=d^{-2}\sum_{p\ne q}\zeta_{ij}^{(p)}\zeta_{i'j'}^{(q)};
\tag{P.25}
\]

the printed factor \(1/[d(d-1)]\) on p. 8 needs this correction.
The sum commutes under interchange of the two operators. Removing
fixed tensor positions in §4 changes the remaining raising product
by the nonzero scalar \(((b-1)/b)^{a(b-1)}\). Its injectivity is
unchanged. In the §5 \(GL_2\) weight-vector display, the coefficient
for the degree-\(d\) normalization is \((b-\eta_2)/d\), which is
nonzero in the displayed range. Thus every injectivity step of the
source propagation proof survives with exact scalars. The grid map
itself is fixed by its independent inclusion–permutation–projection
definition, already identified with (P.3).

## 7. One further degree using the exact square kernel

For every \(a\ge6\), at the additional degree

\[
b=\binom a2-5=C_a+5,
\tag{P.26}
\]

the canonical map \(h_{b,a}\) is surjective on every target component
with \(\lambda_2\le4\). This is a separate unconditional boundary
family.

The source input is the exact decomposition in
Cheung–Ikenmeyer–Mkrtchyan, **Theorem 6(b), printed p. 3**, at the
same primary URL in §2:

\[
\begin{aligned}
\mathcal K_{5,5}={}&
S_{(14,7,2,2)}\oplus S_{(13,7,2,2,1)}
\oplus S_{(12,7,3,2,1)}\oplus S_{(12,6,3,2,2)}\\
&\oplus S_{(12,5,4,3,1)}\oplus S_{(11,5,4,4,1)}
\oplus S_{(10,8,4,2,1)}\oplus S_{(9,7,6,3)}.
\end{aligned}
\tag{P.27}
\]

Each summand has second row at least five, so the full degree-five
base has zero kernel on every type with second row at most four.
At an induction step \(a=r+1\ge6\), (P.26) gives
\(m=b-r=C_r+5\ge5\). Thus (P.19) holds with the fixed bound four,
and the composite (P.11) is injective on every such source
component. The induction statement at \(r\) says that the middle
factor \(\mathcal K_{r,m}\) has only labels with second row at least
five; for \(r=5\) this is exactly (P.27). The two Pieri steps in
§4 keep that lower bound. The codomain of (P.11) therefore has no
label with second row at most four, and its injective restriction
has zero source. This proves the new boundary assertion at every
\(a\ge6\).

In particular every \(a\ge6\), with \(b\) as in (P.26), has actual
canonical image multiplicity two at

\[
\lambda=(ab-4a+8,4^{a-2}).
\tag{P.28}
\]

The exact end-sector count is \(p_{2,\ldots,a}(4)=2\), corresponding
to \(4\) and \(2+2\). All parts in (P.28) satisfy the established
row bound, so both target copies are in the canonical image.

## 8. An unconditional triangular profile from the full square bases

For every pair of integers \(a>k\ge6\), the following is an additional
explicit canonical component range:

\[
\boxed{
b\ge\binom a2+\binom{k-1}{2},\qquad
\lambda\vdash ab,\qquad
\lambda_2\le b-\binom a2+\binom k2.}
\tag{P.29}
\]

The map \(h_{b,a}\) is surjective on the entire indicated target
component for every such triple \(a,k,b\).

The exact established lower maps are

\[
\mathcal K_{k,s}(W)=0\qquad
\text{for every }k\ge6,\ s\ge(k-1)^2.
\tag{P.30}
\]

These are the transposes of the surjective grid maps in Sra,
*The q-Foulkes problem III: On Foulkes' conjecture with a graded
inner factor*, v1, **Theorem 1.3**, proved in §2.2 with its
power-polarization Lemma 2.1. The primary text is
<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.
The exact conventions and complete proof of this input were already
checked for R-022. Equation (P.30) is a statement about the actual
maps, with no coefficient-only replacement.

Here is the full induction proving (P.29). Fix \(k\ge6\) and
\(s\ge(k-1)^2\). For every \(j\ge k\), put

\[
b_j=s+\binom j2-\binom k2.
\tag{P.31}
\]

At \(j=k\) the annihilator is zero by (P.30). Suppose \(j>k\);
write \(r=j-1\). The exact numerical identities are

\[
b_j-r=b_r\ge s\ge(k-1)^2,\qquad b_j\ge r.
\tag{P.32}
\]

Consider a type \(\lambda\vdash j b_j\) with \(\lambda_2\le s\).
The first tensor-factor labels \(\nu\) in its image under (P.9)
satisfy \(\nu_2\le\lambda_2\le s\le b_r\), by Pieri.
R-018 consequently makes \(T_{r,r,b_j}\) injective on every such
whole \(\nu\)-isotypic component. The composite \(\Theta_{j,b_j}\)
is injective on the original \(\lambda\)-component.

By (P.11), this composite has codomain

\[
\operatorname{Sym}^{r^2}W\otimes
\mathcal K_{r,b_r}(W)\otimes\operatorname{Sym}^{b_j}W.
\tag{P.33}
\]

At \(r=k\) this codomain is zero. For \(r>k\), the induction assertion
states that every label \(\kappa\) of its middle factor has
\(\kappa_2\ge s+1\). Tensoring with either of the displayed row
representations adds a horizontal strip, so every resulting label
still has second row at least \(s+1\). Thus (P.33) has no type
\(\lambda\) under consideration. The injective restriction has zero
domain. This proves zero annihilator on every second row at most
\(s\), at every \(j\ge k\).

Set \(j=a\) in (P.31). Then
\(s=b-\binom a2+\binom k2\); the identity
\[
(k-1)^2-\binom k2=\binom{k-1}{2}
\tag{P.34}
\]
converts the exact base range \(s\ge(k-1)^2\) into the first
inequality in (P.29). This proves all the stated parameters.

For a concrete comparison within the proved families, at \(a=8\)
the base-five assertion begins at \(b=24\) and gives
\(\lambda_2\le b-18\). Formula (P.29) with \(k=6\) begins at
\(b=38\) and gives \(\lambda_2\le b-13\); with \(k=7\) it begins
at \(b=43\) and gives \(\lambda_2\le b-7\).
Every assertion refers to the same specified map \(h_{b,8}\).
In particular \(h_{38,8}\) is surjective on every component with
\(\lambda_2\le25\).

## Check status

The proof of (P.11)–(P.20), the base-map identification, and all
endpoint inequalities were checked in this run. The parent agent
will record its independent reading separately. The original
degree-five computational theorem is used with the source status
stated in §2; it is not represented as a replayed calculation.


# Two cofactor families beyond the first-row boundary

Statement **R-025**. Written and checked on 21 November 2026 UTC by
GPT-6 Astra Pro, agent /root/rectangular_cases; effort setting not exposed.
Every assertion below concerns the displayed actual polynomial maps.
No historical novelty claim is made.

## 1. Explicit canonical image components at the critical degree

Let \(a\ge3\), put \(r=a-1\), \(b=r^2-1\), and \(H=r^2+1=b+2\).
Use the normalized canonical grid map
\[
h_{b,a}:\operatorname{Sym}^b(\operatorname{Sym}^a V)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^b V).
\tag{Cof.1}
\]

For every **odd \(a\ge3\)**, equivalently every even \(r\ge2\), set
\[
\lambda_{\mathrm{odd}\ a}
=(r^2+1,(r^2)^{r-2},r^2-2,r^2-r).
\tag{Cof.2}
\]
For every **even \(a\ge4\)**, equivalently every odd \(r\ge3\), set
\[
\lambda_{\mathrm{even}\ a}
=((r^2+1)^r,r^2-2r-1).
\tag{Cof.3}
\]
Both are partitions of \(ab\). In every dimension at least their
number of rows,
\[
\boxed{
[S_\lambda V:\operatorname{im}h_{b,a}]
=[S_\lambda V:\operatorname{Sym}^a(\operatorname{Sym}^b V)]
=1
}
\tag{Cof.4}
\]
for the corresponding displayed \(\lambda\).

The proof supplies a highest vector in the dual target whose
last-slot common polarization is nonzero. The exact annihilator
inclusion (K.22) then proves (Cof.4). Thus this is a statement about
the canonical map on its unique target copy.

For example the families include
\[
\begin{array}{c|c|c}
a&b&\lambda\\\hline
3&3&(5,2,2)\\
4&8&(10,10,10,2)\\
5&15&(17,16,16,14,12)\\
6&24&(26,26,26,26,26,14)\\
7&35&(37,36,36,36,36,34,30).
\end{array}
\tag{Cof.5}
\]
Their first row is \(r^2+1\). Apart from coincidences with previously
established full-map cases, these labels lie outside the two
component ranges \(\lambda_1\le r^2\) and
\(\lambda_2\le r(r-1)-1\) of R-022.

## 2. Two actual highest polynomials

First use \(n\ge3\) slots and \(n\) coordinate rows. Write
\[
X=(X_{ij})_{1\le i,j\le n},\qquad
x_j=X_{1j},\qquad D=\det X.
\]
Let \(C_{ij}=(-1)^{i+j}\det X_{\widehat i,\widehat j}\) be the
cofactor matrix, and put
\[
y_j=C_{nj},\qquad z_j=C_{n-1,j},\qquad
\mathcal S(X)=\sum_{j=1}^n x_j z_j^2\prod_{i\ne j}y_i.
\tag{Cof.6}
\]

For every odd integer \(H\ge n+1\), define
\[
F_{n,H}=D^{H-n-2}\mathcal S(X).
\tag{Cof.7}
\]
The possible exponent \(-1\), occurring at \(H=n+1\), is
interpreted by the actual polynomial quotient
\(\mathcal S(X)/D\). This quotient is polynomial: on the dense
rank-\((n-1)\) locus of \(D=0\), all nonzero rows of the cofactor
matrix are proportional. In its fraction field \(z_j=c\,y_j\),
and
\[
\mathcal S=c^2\left(\prod_i y_i\right)\sum_jx_jy_j=0.
\]
The last equality is the cofactor identity
\(\sum_jX_{1j}C_{nj}=0\). The determinant hypersurface is integral
(the generic determinant is irreducible), so vanishing on this
dense open subset gives \(D\mid\mathcal S\) in the polynomial ring.
The same conclusion holds on charts where another cofactor row
is nonzero; one dense chart already proves the divisibility.

Each column of \(\mathcal S\) has degree \(n\). Thus (Cof.7)
has degree \(H-2\) in each slot, and its row weight is
\[
\lambda^F_{n,H}
=(H,(H-1)^{n-3},H-3,H-n).
\tag{Cof.8}
\]
This is a partition for \(n\ge3\) and \(H\ge n+1\).

Here is a direct highest-vector verification. Under a row
transvection \(X\mapsto (I+tE_{j,i})X\), \(i<j\), the cofactor
matrix changes by \(C\mapsto(I-tE_{i,j})C\), and \(D\) and the
first row stay fixed. The row \(y\) stays fixed. The only such
change affecting \(z\) is \(z\mapsto z-t y\). Under that change,
the difference of the two numerators in (Cof.6) is
\[
-2t\left(\prod_i y_i\right)\sum_jx_jz_j
+t^2\left(\prod_i y_i\right)\sum_jx_jy_j=0.
\tag{Cof.9}
\]
Both sums are zero cofactor identities, since \(n-1,n\ne1\).
Therefore \(F_{n,H}\) is a highest polynomial of weight (Cof.8).

A permutation of columns multiplies \(D\) by its sign and each
cofactor row by that sign while permuting its entries. Hence the
numerator in (Cof.6) has sign character to the power \(n+1\).
The total permutation character of (Cof.7) is
\(\operatorname{sgn}^{H-1}=1\). It consequently belongs to
\(\operatorname{Sym}^n(\operatorname{Sym}^{H-2}V)\).

The second polynomial, for every even \(H\ge2n\), is
\[
G_{n,H}=D^{H-2n}\prod_{j=1}^n y_j^2.
\tag{Cof.10}
\]
It is polynomial, symmetric in the slots, and highest by the
same transvection formulas. Its separate slot degree is \(H-2\),
and its row weight is
\[
\lambda^G_{n,H}=(H^{n-1},H-2n).
\tag{Cof.11}
\]

## 3. Exact multiplicity-one identification

We give the complement morphism that determines the multiplicities
of these highest vectors. For every partition \(\lambda\) fitting
in the \(n\times H\) rectangle, put
\[
\nu=(H-\lambda_n,\ldots,H-\lambda_1).
\]
Exterior multiplication of complementary columns gives the perfect
\(GL_n\)-equivariant pairing
\[
S_\lambda\mathbf Q^n\otimes S_\nu\mathbf Q^n
\longrightarrow(\det\mathbf Q^n)^H.
\tag{Cof.12}
\]
For precision, apply the wedge pairing on each column after
realizing both Schur modules by their column alternations and row
symmetrizations. On the complementary standard highest and lowest
tableaux it is a nonzero product of coordinate determinants.
Its map from either irreducible Schur factor to the dual of the
other, with determinant twist, is therefore nonzero and hence an
isomorphism. This proves perfectness and fixes the determinant
character.

Restrict (Cof.12) to content \(((H-2)^n)\) in the first factor and
content \((2^n)\) in the second. Diagonal weights add to \((H^n)\),
so these are perfectly paired weight spaces. Permutation matrices
act on the one-dimensional target by \(\operatorname{sgn}^H\).
Taking permutation invariants, and using the Cauchy decomposition
of matrix polynomials, gives the exact multiplicity equalities
\[
[S_\lambda:\operatorname{Sym}^n\operatorname{Sym}^{H-2}]
=
\begin{cases}
[S_\nu:\Lambda^n(\operatorname{Sym}^2)],&H\text{ odd},\\
[S_\nu:\operatorname{Sym}^n(\operatorname{Sym}^2)],&H\text{ even}.
\end{cases}
\tag{Cof.13}
\]
The second step is the literal content-\((2^n)\) matrix-polynomial
space \((\operatorname{Sym}^2\mathbf Q^n)^{\otimes n}\).
Its sign-isotypic projector is \(n!^{-1}\sum_\sigma
\operatorname{sgn}(\sigma)\sigma\), whose image is
\(\Lambda^n(\operatorname{Sym}^2\mathbf Q^n)\) under the usual
normalized alternating inclusion. Its invariant projector gives
the symmetric power. These are the actual maps in (Cof.13).

For (Cof.8), the complementary partition is
\[
\nu=(n,3,1^{n-3},0).
\]
Its weight space in \(\Lambda^n(\operatorname{Sym}^2\mathbf Q^n)\)
has dimension one. To see this, view a wedge basis as a set of
distinct quadratic monomials, with a loop counting twice toward a
vertex degree. No monomial uses the \(n\)-th variable. Degree \(n\)
at the first variable forces its loop and all \(n-2\) available
edges to the other variables. The one remaining quadratic must
be the loop at the second variable, which raises its degree from
one to three. Thus the unique wedge is
\[
e_1^2\wedge e_1e_2\wedge\cdots\wedge e_1e_{n-1}
\wedge e_2^2.
\tag{Cof.14}
\]
It is highest: replacing any higher-index variable by a
lower-index variable yields either zero or a repeated wedge
factor. Thus its irreducible type occurs once. For (Cof.11) the
complement is the row \((2n)\), whose unique highest vector in
\(\operatorname{Sym}^n(\operatorname{Sym}^2)\) is
\((e_1^2)^n\). This also occurs once. Equation (Cof.13) proves
multiplicity one for both displayed original types.

## 4. A concrete cofactor specialization

We specify matrices producing the needed positive coefficients.
Let the slot set be a disjoint union \(I\sqcup J\), with
\(|I|=s\), \(|J|=t\), \(s+t=n\), both sets nonempty. Choose a
reference slot \(q\in I\). There exists an explicit unimodular
\((n-1)\times(n-1)\) matrix \(A\) whose last row is the indicator
of \(J\), in the coordinates excluding \(q\): take one \(j_0\in J\),
keep every coordinate row except \(e_{j_0}\), and replace that row
by \(\sum_{j\in J}e_j\), putting it last.

For \(F\), also choose a nonempty singleton \(K=\{p\}\subset
I\setminus\{q\}\), and put the row \(e_p\) penultimate. The
remaining coordinate rows, in increasing order, precede these
last two rows. This explicitly gives the required unimodular
matrix in this case.

Let \(B_0\) have rows \(e_i-e_q\), for \(i\ne q\), in the same
coordinate order, and set
\[
B=A^{-T}B_0,\qquad
X=\begin{pmatrix}x_1&\cdots&x_n\\B\end{pmatrix},\qquad
X_I=\sum_{i\in I}x_i,\quad Y_J=\sum_{j\in J}x_j,\quad
S=X_I+Y_J.
\tag{Cof.15}
\]
All entries of \(B\) are integers. Direct solution of the equations
\(B_0v=(v_i-v_q)_{i\ne q}\) shows
\[
D=\eta S,\qquad
C_{\ell+1,i}=\eta\bigl(S A_{\ell,i}
                       -\sum_j A_{\ell,j}x_j\bigr),
\quad \eta\in\{1,-1\},
\tag{Cof.16}
\]
where the missing column \(A_{\ell,q}\) is zero. The scalar
\(\eta=D(1,0,\ldots,0)\) is the signed determinant of the displayed
constant row matrix and is a unit. Formula (Cof.16) is also the
identity \(C=D X^{-T}\); it fixes its scalar exactly.

The last two chosen rows give
\[
y_i/\eta=
\begin{cases}-Y_J&i\in I,\\X_I&i\in J,\end{cases}
\qquad
z_i/\eta=S\,1_{i=p}-x_p.
\tag{Cof.17}
\]
Writing \(Z=x_p\) and \(R=X_I-Z\), direct substitution into the
sum (Cof.6) gives
\[
\mathcal S(X)
=\eta^{n+1}(-1)^{s+1}S^2
 ZR\,X_I^{t-1}Y_J^{s-1}.
\tag{Cof.18}
\]
For example, divide temporarily by \(\prod y_i\): the two group
sums are
\[
-\frac{ZS^2+(X_I-2S)Z^2}{Y_J}
+\frac{Y_JZ^2}{X_I}
=-\frac{S^2Z(X_I-Z)}{X_IY_J}.
\]
Multiplication by the actual product
\(\eta^n(-1)^sY_J^sX_I^t\), together with the additional
cofactor factors in the ratio, proves (Cof.18) as a polynomial
identity.

Since \(H\) is odd in (Cof.7), the total power of \(\eta\) is
\(H-1\), which is even. Since \(H\) is even in (Cof.10), its
total power is \(H\), also even. Therefore the specialized
highest polynomials are exactly
\[
\boxed{
F_{n,H}=(-1)^{s+1}S^{H-n}ZR
              X_I^{t-1}Y_J^{s-1},\qquad
G_{n,H}=S^{H-2n}X_I^{2t}Y_J^{2s}.}
\tag{Cof.19}
\]
The first identity includes \(H=n+1\), using the polynomial
division already proved. These evaluations prove that both
highest vectors are nonzero whenever their displayed parameters
apply.

## 5. Proof of the canonical image assertions

Set \(n=a=r+1\), \(H=r^2+1\), \(b=H-2\), and \(W=V^*\).
The exact R-022 annihilator construction gives
\[
\delta:\mathcal K_{a,b}(W)\hookrightarrow
\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW.
\tag{Cof.20}
\]
Indeed its only lower-map input is \(h_{b-r,r}\) surjective.
Here
\[
b-r=r^2-r-1\ge(r-1)^2
\]
for every \(r\ge2\), with equality at \(r=2\). This is Sra's
Theorem 1.3 in precisely its proved range; the freeing and
polarization maps and scalars are K.16–K.22, also P.9–P.16.

Suppose first that \(r\) is even. Use \(F_{a,H}\), choose
\[
s=(r+2)/2,\qquad t=r/2,\qquad K=\{a\}\subset I,
\]
and choose the reference slot in \(I\setminus\{a\}\).
Keep the last slot's first coordinate equal to one. Give each of
the first \(r\) slots first coordinate zero, and polarize these
slots in the common direction \(e_1\). Their resulting first
coordinates are \(u_1,\ldots,u_r\).

The required value of \((T_{r,r,b}\otimes\mathrm{id})\delta F\)
is the coefficient of \(u_1^r\cdots u_r^r\).
The first-row homogeneity \(H=r^2+1\) says that it is the
coefficient of \(x_1^r\cdots x_r^r x_a\) in (Cof.19). The factor
\(Z=x_a\) already supplies that last degree. Set \(Z=0\) in
the remaining factors. Since \(s-1=t=r/2\), this coefficient is
\[
\boxed{
(-1)^{s+1}
\binom{r^2-r}{\,r(r-1)/2\,}
\frac{\bigl((r^2/2)!\bigr)^2}{(r!)^r}\ne0.}
\tag{Cof.21}
\]
The binomial splits the two group sums; their multinomial
coefficients supply the two displayed factorials. Every lower
factorial argument is nonnegative.

For odd \(r\ge3\), use \(G_{a,H}\), and let \(s=t=(r+1)/2\),
with the last slot in \(I\). The same coefficient extraction
applied to the second expression in (Cof.19) gives
\[
\boxed{
\binom{r^2-2r-1}{\,r(r-3)/2\,}
\frac{\bigl(r(r-1)/2+1\bigr)!\,
      \bigl(r(r+1)/2\bigr)!}{(r!)^r}\ne0.}
\tag{Cof.22}
\]
The remaining exponent in the binomial is
\((r+1)(r-2)/2\ge0\), and its upper argument is at least two.
The group containing the last slot has total degree
\(r(r-1)/2+1\); its last coordinate has exponent one, giving the
first numerator factorial and denominator \((r!)^{s-1}\).
The other group gives the second numerator factorial and
denominator \((r!)^t\).

Equations (Cof.21) and (Cof.22) show that the unique source
highest line of the respective type in the annihilator ambient
space is not killed by the map in (Cof.20). The multiplicity-one
proof in §3 and equivariance imply that no copy of that type is
in \(\mathcal K_{a,b}\). The exact transpose pairing of (P.6)
proves (Cof.4).

## 6. Two infinite common-polarization families

The same polynomials prove additional parameter families directly
for \(T_{r,L,rL-1}\).

For every \(r\ge3\), \(L\ge1\) with \(rL\) even, set
\[
H=rL+1,\qquad
\lambda=(H,(H-1)^{r-3},H-3,H-r).
\tag{Cof.23}
\]
This source type has multiplicity one and \(T_{r,L,rL-1}\)
is injective on it. Put \(s=\lceil r/2\rceil\), \(t=\lfloor r/2\rfloor\),
choose \(K=\{1\}\subset I\), and take first-row base \(x_1=1\),
all other first-row bases zero. Formula (Cof.19) shows that
the common-polarization coefficient is
\[
\boxed{
(-1)^{s+1}(L+1)
\frac{((s-1)L)!\,(tL)!}{(L!)^{r-1}}
\binom{r(L-1)+1}{\,sL-t\,}
\binom{sL-1}{L}\ne0.}
\tag{Cof.24}
\]
To derive this exact expression, first use first-row homogeneity:
the coefficient at exponent \(L\) in every slot after translation
of the first coordinate by one is \(L+1\) times the coefficient
at exponents \((L+1,L,\ldots,L)\) before translation. Expand
\(X_I^{t-1}=(Z+R)^{t-1}\) in (Cof.19). The resulting finite
binomial sum is
\[
\sum_j\binom{t-1}{j}
\frac{1}{(L-j)!\,((s-1)L-t+j)!}
=\frac{\binom{sL-1}{L}}{(sL-t)!},
\tag{Cof.25}
\]
where terms with negative factorial arguments are zero.
This is the elementary coefficient identity for
\((1+z)^{t-1}(1+z)^{sL-t}\). The remaining group multinomials
give (Cof.24). Its arguments are all valid: at \(L=1\), parity
forces even \(r\ge4\), so \(s=t\ge2\); for odd \(r\), \(L\)
is even and at least two. In every case \(sL-t\ge0\),
\(tL-s+1\ge0\), and \(sL-1\ge L\).

For every odd \(r\ge3\) and odd \(L\ge3\), put
\[
H=rL+1,\qquad \lambda=(H^{r-1},H-2r).
\tag{Cof.26}
\]
This source type again has multiplicity one and is mapped
injectively. Use \(G_{r,H}\), \(s=(r-1)/2\), \(t=(r+1)/2\),
and put the first-row base one in a slot of \(I\). The exact value is
\[
\boxed{
\binom{rL+1-2r}{\,sL+1-2t\,}
\frac{(sL+1)!\,(tL)!}{(L!)^r}\ne0.}
\tag{Cof.27}
\]
The other binomial argument is \(tL-2s\). They are nonnegative
for every displayed \(r,L\), including \(r=L=3\).
This follows directly from the second product in (Cof.19).

For these families the polynomial-generator construction uses
exactly \(r\) coordinate rows. Inclusion into larger vector
spaces commutes with coefficient extraction and the Schur
realizations. A map nonzero on a multiplicity-one irreducible
component is injective on it in every dimension where it exists.
This proves all ambient-rank statements in §§1 and 6.


# Explicit canonical image families below the square bound

Statement **R-026**. Written on 21 November 2026 UTC by GPT-6 Astra Pro,
agent /root/rectangular_cases; effort setting not exposed. The proof
uses the actual canonical map, its transpose annihilator, and explicit
highest polynomials. No historical novelty claim is made.

## 1. The two unconditional parameter families

For integers \(r\ge3\), set \(a=r+1\). The canonical map is the
normalized grid transpose followed by symmetric projection:
\[
h_{b,a}:\operatorname{Sym}^b(\operatorname{Sym}^a V)
\longrightarrow\operatorname{Sym}^a(\operatorname{Sym}^b V).
\tag{BS.1}
\]
In every dimension at least the number of positive parts in the
displayed partition, the following assertions hold.

**Even \(r\ge4\).** For every integer \(2\le k\le r-1\), put
\[
b=r^2-k,\qquad
\lambda=((r^2)^r,\ r^2-k(r+1)).
\tag{BS.2}
\]
Then
\[
\boxed{[S_\lambda V:\operatorname{im}h_{b,a}]
=[S_\lambda V:\operatorname{Sym}^a\operatorname{Sym}^b V]=1.}
\tag{BS.3}
\]

**Odd \(r\ge3\).** For every integer \(2\le k\le r-1\), put
\[
b=r^2-k,\qquad
\lambda=(r^2,(r^2-1)^{r-2},\ r^2-3,
                         \ r^2-(k-1)(r+1)).
\tag{BS.4}
\]
The same equality (BS.3) holds.

At \(k=r-1\), the last part in (BS.2) is one; at its other
parameters it is at least \(r+2\). The last part in (BS.4) is
always at least \(r+2\). These are no larger than the preceding part, so the
formulas are partitions. Their sizes are respectively
\((r+1)(r^2-k)=ab\). Their first row is exactly \(r^2\).

For example:

| \(a\) | \(b\) | \(\lambda\) |
|---:|---:|---|
| 4 | 7 | \((9,8,6,5)\) |
| 5 | 14 | \((16,16,16,16,6)\) |
| 5 | 13 | \((16,16,16,16,1)\) |
| 6 | 23 | \((25,24,24,24,22,19)\) |
| 6 | 22 | \((25,24,24,24,22,13)\) |
| 6 | 21 | \((25,24,24,24,22,7)\) |
| 7 | 34 | \((36,36,36,36,36,36,22)\) |
| 7 | 33 | \((36,36,36,36,36,36,15)\) |
| 7 | 32 | \((36,36,36,36,36,36,8)\) |
| 7 | 31 | \((36,36,36,36,36,36,1)\) |
| 8 | 43 | \((49,48,48,48,48,48,46,9)\) |

Both parity families reach every degree from \(r^2-r+1\) to
\(r^2-2\). The partitions and actual image
multiplicities at all these parameters are the formulas above.

## 2. General cofactor highest polynomials

Use an \(n\)-by-\(n\) matrix of independent variables \(X\), with
\(n\ge3\). Set
\[
D=\det X,\qquad x_j=X_{1j},\qquad
y_j=C_{nj},\qquad z_j=C_{n-1,j},
\quad
\mathcal S=\sum_j x_jz_j^2\prod_{i\ne j}y_i,
\tag{BS.5}
\]
where \(C_{ij}\) is the signed cofactor. All these are literal
polynomials with integral coefficients.

For every **even \(H\ge nk\)** and every \(k\ge1\), define
\[
G_{n,H,k}=D^{H-nk}\prod_{j=1}^n y_j^k.
\tag{BS.6}
\]
It has separate slot degree \(H-k\), row weight
\[
\lambda^G=(H^{n-1},H-nk),
\tag{BS.7}
\]
and is symmetric in the slots. Indeed a column permutation acts on
\(D\) by its sign and on the cofactor row by its sign times the
same entry permutation; the resulting character is
\(\operatorname{sgn}^{H-nk+nk}=1\).

For every **odd \(H\ge n(k-1)+1\)** and every \(k\ge2\), define
\[
F_{n,H,k}
=D^{H-n(k-1)-2}\mathcal S\prod_{j=1}^n y_j^{k-2}.
\tag{BS.8}
\]
The exponent of \(D\) is at least minus one. The quotient at that
endpoint is an actual polynomial: \(D\mid\mathcal S\), as proved
in Cof.6–Cof.9. Explicitly, on the generic rank-\((n-1)\) locus,
\(z_j=c y_j\), so \(\mathcal S=c^2\prod_i y_i\sum_jx_jy_j=0\)
by the cofactor identity. Irreducibility of the determinant then
gives divisibility in the polynomial ring.

The separate slot degree of (BS.8) is \(H-k\), and its row weight is
\[
\lambda^F=(H,(H-1)^{n-3},H-3,H-n(k-1)).
\tag{BS.9}
\]
Its slot-permutation character is
\[
\operatorname{sgn}^{H-n(k-1)-2+n+1+n(k-2)}
=\operatorname{sgn}^{H-1}=1.
\tag{BS.10}
\]
These are highest polynomials under the same actual transvections
as R-025: for \(i<j\), the substitution
\(X\mapsto(I+tE_{j,i})X\) fixes \(D\), \(x\), and \(y\).
Only \(z\mapsto z-t y\) can affect \(\mathcal S\), and its
change is
\[
-2t\Bigl(\prod y_i\Bigr)\sum_jx_jz_j
+t^2\Bigl(\prod y_i\Bigr)\sum_jx_jy_j=0.
\tag{BS.11}
\]
Thus the displayed polynomials are actual highest vectors once
their nonzero evaluations below are supplied.

## 3. The exact complement morphism and multiplicity one

For \(\lambda\) in the \(n\)-by-\(H\) rectangle, let
\(\nu=(H-\lambda_n,\ldots,H-\lambda_1)\). The exterior-column
pairing of Cof.12 is a nonzero perfect equivariant pairing
\[
S_\lambda\mathbf Q^n\otimes S_\nu\mathbf Q^n
\longrightarrow(\det\mathbf Q^n)^H.
\tag{BS.12}
\]
It pairs the content \(((H-k)^n)\) perfectly with content
\((k^n)\), because their diagonal weights add to \((H^n)\).
On the right permutation matrices act by \(\operatorname{sgn}^H\).
Taking the invariant or alternating projector on the second content
space, and applying the literal Cauchy decomposition of matrix
polynomials, gives
\[
[S_\lambda:\operatorname{Sym}^n\operatorname{Sym}^{H-k}]
=
\begin{cases}
[S_\nu:\operatorname{Sym}^n\operatorname{Sym}^{k}],&H\text{ even},\\
[S_\nu:\Lambda^n\operatorname{Sym}^{k}],&H\text{ odd}.
\end{cases}
\tag{BS.13}
\]
Precisely, the content-\((k^n)\) matrix-polynomial space is
\((\operatorname{Sym}^k\mathbf Q^n)^{\otimes n}\). The projectors
are \(n!^{-1}\sum_\sigma\sigma\) and
\(n!^{-1}\sum_\sigma\operatorname{sgn}(\sigma)\sigma\);
their normalized symmetric and alternating inclusions are the maps
used in (BS.13).

For (BS.7), the complement is the row \((nk)\). Its only weight
vector of that weight is \((e_1^k)^n\), so the required symmetric
plethysm multiplicity is one.

For (BS.9), the complement is
\[
\nu=(n(k-1),3,1^{n-3},0).
\tag{BS.14}
\]
Its entire weight space in \(\Lambda^n\operatorname{Sym}^k\)
is one-dimensional. Here is a direct count. No chosen monomial
uses the last variable. The total degree away from the first
variable is \(n\). Among distinct degree-\(k\) monomials in the
first \(n-1\) variables, there is one with that degree zero, and
there are \(n-2\) with that degree one. For \(n\) distinct
monomials, the minimum sum of those degrees is consequently
\(0+(n-2)+2=n\). Equality forces all of those first \(n-1\)
monomials and a single monomial of degree two away from the first
variable. The remaining specified weights force it to be
\(e_1^{k-2}e_2^2\). Thus the unique wedge is
\[
e_1^k\wedge e_1^{k-1}e_2\wedge\cdots\wedge
e_1^{k-1}e_{n-1}\wedge e_1^{k-2}e_2^2.
\tag{BS.15}
\]
Every raising replacement of a variable produces a repeated wedge
factor or zero, so this is a highest vector. Hence (BS.14) occurs
once and (BS.13) proves multiplicity one for (BS.9).

## 4. Exact specialization and coefficients

Use exactly the integral matrix construction in Cof.15–Cof.17.
Partition the \(n\) slots into nonempty groups \(I,J\) of sizes
\(s,t\); choose a reference \(q\in I\). Let \(A\) be the
specified unimodular matrix whose last row is the indicator of
\(J\) in the coordinates excluding \(q\). For \(F\), choose
\(p\in I\setminus\{q\}\), put \(e_p\) in the penultimate row,
and use the remaining coordinate rows before these last two rows.
With \(B=A^{-T}B_0\), where the rows of \(B_0\) are
\(e_i-e_q\), form the matrix whose first row is \(x\) and whose
lower rows are \(B\). Write
\[
X_I=\sum_{i\in I}x_i,\quad Y_J=\sum_{j\in J}x_j,\quad
S=X_I+Y_J,\quad Z=x_p,\quad R=X_I-Z.
\]
The exact cofactor identities are
\[
\begin{gathered}
D=\eta S,\quad y_i/\eta=-Y_J\ (i\in I),\quad y_j/\eta=X_I\ (j\in J),\\
\mathcal S=\eta^{n+1}(-1)^{s+1}S^2ZR X_I^{t-1}Y_J^{s-1},\quad\eta\in\{1,-1\}.
\end{gathered}
\tag{BS.16}
\]
Substitution in (BS.6) and (BS.8) gives, with all signs retained,
\[
\boxed{G_{n,H,k}=(-1)^{sk}S^{H-nk}X_I^{kt}Y_J^{ks},}
\tag{BS.17}
\]
\[
\boxed{F_{n,H,k}=(-1)^{s(k-1)+1}
S^{H-n(k-1)}ZR X_I^{t(k-1)-1}Y_J^{s(k-1)-1}.}
\tag{BS.18}
\]
The powers of \(\eta\) are \(H\) and \(H-1\), respectively,
and are even in their stated ranges. These formulas are polynomial
identities, including the quotient endpoint in (BS.8).

For the canonical families, take \(n=r+1\), \(H=r^2\),
and put the last slot in \(I\). Give all slots first-row base
zero. In the first \(r\) slots, polarize in the common direction
\(e_1\); keep the last slot fixed. The required value is the
coefficient of
\[
x_1^r\cdots x_r^r x_{r+1}^{\,0}.
\tag{BS.19}
\]
Thus set \(x_{r+1}=0\) in (BS.17) or (BS.18). This base choice
is allowed: the lower rows are the explicit constant matrix \(B\),
and the polarization coefficient is a polynomial evaluation at it.

For **even \(r\ge4\)** and \(2\le k\le r-2\), use
\[
s=r/2+1,\quad t=r/2,\quad h=r^2-k(r+1),\quad
u=r(r-k)/2.
\]
There are \(r/2\) unfixed variables in each group. Formula (BS.17)
therefore gives exactly
\[
\boxed{(-1)^{sk}\binom hu
\frac{((r^2/2)!)^2}{(r!)^r}\ne0.}
\tag{BS.20}
\]
Indeed the group degrees are both \(r^2/2\), so the required
power of \(X_I\) from \(S^h\) is \(u\), and the remaining
degree is \(h-u=r^2/2-k(r/2+1)\). This is at least two for all
the displayed parameters. Both multinomial coefficients are the
displayed factorial ratios. This proves the nonzero value including
the endpoint \(k=r-2\).

For **odd \(r\ge5\)** and \(2\le k\le r-1\), use
\[
s=t=(r+1)/2,\quad h=r^2-(k-1)(r+1),\quad
d_I=r(s-1),\quad d_J=rt,\quad
u=s(r-k-1).
\tag{BS.21}
\]
Choose \(p\) in the first \(r\) slots of \(I\), and take the
last slot as reference \(q\). There are \(s-1\ge2\) first
\(r\) slots in \(I\), so after setting the last coordinate zero,
\(R\) still contains at least one variable. Formula (BS.18) gives
the exact coefficient
\[
\boxed{(-1)^{s(k-1)+1}\binom hu
\binom{d_I-2}{r-1}
\frac{(d_I-r)!\,d_J!}{(r!)^{r-1}}\ne0.}
\tag{BS.22}
\]
To obtain it, the \(S^h\) split must contribute
\(X_I^uY_J^{h-u}\), since
\(u=d_I-t(k-1)-1\). The resulting first-group factor is
\(ZR(Z+R)^{d_I-2}\). Its \(Z^r\) coefficient is
\(\binom{d_I-2}{r-1}R^{d_I-r}\). The remaining first-group
variables have exponent \(r\) each, as do the \(t\) variables
of the second group, giving the two multinomial coefficients.
Every argument is valid: \(u\ge0\),
\(h-u=s(r-k+1)+1>0\), and \(d_I-r=r(s-2)\ge0\).
The binomial \(\binom{d_I-2}{r-1}\) is positive because
\(s-1\ge2\) and \(r\ge5\).

The odd endpoint \(r=3,k=2\) is also explicit. Choose
\(s=3,t=1\), put the last slot in \(I\), and choose \(p\)
among its first two slots. Then \(h=5,d_I=6,d_J=3,u=4\).
The same coefficient extraction is
\[
\binom54\binom42\frac{3!\,3!}{(3!)^2}=30\ne0.
\tag{BS.23}
\]

## 5. The even-r endpoint by an explicit apolar evaluation

Let \(r\ge4\) be even and take \(k=r-1\), \(n=r+1\),
\(H=r^2\). The polynomial (BS.6) at this endpoint is
\[
G_{n,H,r-1}=D\prod_{j=1}^{r+1}y_j^{r-1},\qquad
\lambda=((r^2)^r,1).
\tag{BS.24}
\]
We give another concrete matrix evaluation of its coefficient (BS.19).
Let \(\zeta_1,\ldots,\zeta_r\) be the distinct roots of
\(z^r+1\), put \(a_i=1+\zeta_i\), and set \(a_{r+1}=0\).
The first \(r\) values are distinct and nonzero: \(-1\) is not
a root of \(z^r+1\) for even \(r\). They therefore give the
explicit nonzero determinant matrix
\[
A=\begin{pmatrix}
a_1^2&\cdots&a_r^2\\
\vdots&&\vdots\\
a_1^r&\cdots&a_r^r\\
a_1&\cdots&a_r
\end{pmatrix},\qquad
\det A=(-1)^{r-1}\Bigl(\prod_i a_i\Bigr)
                       \prod_{i<j}(a_j-a_i)\ne0.
\tag{BS.25}
\]
Take \(B_0=(I_r\mid-\mathbf1)\), \(B=A^{-T}B_0\), and
use \(B\) for the lower rows of \(X\). This specifies the actual
matrix over the splitting field. No unimodular normalization is
made in this evaluation. Write
\[
S=\sum_{i=1}^r x_i,\qquad Z=\sum_{i=1}^r a_i x_i,
\qquad \eta=(\det A)^{-1}.
\]
After setting \(x_{r+1}=0\), the determinant and cofactor identities
give exactly
\[
D=\eta S,\qquad y_i=\eta(a_iS-Z)\ (1\le i\le r),
\qquad y_{r+1}=-\eta Z.
\tag{BS.26}
\]
For the determinant, the matrix \(B_0\) gives
\((-1)^r\sum x_i\); its lower row transformation has determinant
\((\det A)^{-1}\). Since \(r\) is even, this is the stated
\(\eta\). The cofactor formulas follow from \(C=DX^{-T}\),
exactly as in Cof.16, with the last row of \(A\) equal to \(a\).

Let
\[
Q(s,z)=\prod_{i=1}^r(z-a_i s)=(z-s)^r+s^r,
\qquad Q_0(s,z)=z^r+s^r.
\]
Substituting (BS.26) into (BS.24) gives the exact binary expression
\[
G_{n,H,r-1}=-\eta^{r^2}S Z^{r-1}Q(S,Z)^{r-1}.
\tag{BS.27}
\]
For degree-\(N\) binary forms define the bilinear pairing
\[
\langle P,R\rangle_N
=\left.P(-\partial_z,\partial_s)R(s,z)\right|_{s=z=0}.
\tag{BS.28}
\]
The chain rule for the two displayed linear forms \(S,Z\) identifies
the required coefficient, with its full normalization, as
\[
[x_1^r\cdots x_r^r]G_{n,H,r-1}
=-\frac{\eta^{r^2}}{(r!)^r}
\left\langle Q^r,\ s z^{r-1}Q^{r-1}\right\rangle_{r^2}.
\tag{BS.29}
\]
Indeed differentiation in \(x_i\) acts as
\(\partial_s+a_i\partial_z\); the product of its \(r\)-th
powers is exactly \(Q(-\partial_z,\partial_s)^r\).
The factor \((r!)^{-r}\) is the ordinary monomial coefficient
normalization.

The substitution \(\tau R(s,z)=R(s,z-s)\) preserves the pairing
(BS.28). This follows directly from the chain rule:
\((\partial_s+\partial_z)\tau R=\tau(\partial_sR)\) and
\(\partial_z\tau R=\tau(\partial_zR)\). Substitution in
\((\tau P)(-\partial_z,\partial_s)
=P(-\partial_z,\partial_s+\partial_z)\), followed by evaluation
at zero, proves \(\langle\tau P,\tau R\rangle=\langle P,R\rangle\).
Applying this actual change of variables to (BS.29) gives
\[
\left\langle Q^r,s z^{r-1}Q^{r-1}\right\rangle_{r^2}
=\left\langle Q_0^r,s(z+s)^{r-1}Q_0^{r-1}\right\rangle_{r^2}.
\tag{BS.30}
\]
Every exponent of \(s\) or \(z\) in a monomial of \(Q_0^r\)
is a multiple of \(r\). In the extra factor
\(s(z+s)^{r-1}\), the \(z\)-exponent lies between zero and
\(r-1\). Consequently only its term \(s^r\) can pair
nontrivially with \(Q_0^r\) after multiplication by \(Q_0^{r-1}\).
Expanding these two binomial powers now gives
\[
\boxed{[x_1^r\cdots x_r^r]G_{n,H,r-1}
=-\frac{\eta^{r^2}}{(r!)^r}
\sum_{i=0}^{r-1}\binom ri\binom{r-1}{i}
(ri)!\,[r(r-i)]!\ne0.}
\tag{BS.31}
\]
The differential sign in each term is \((-1)^{ri}=1\), since
\(r\) is even. Every integer summand is positive and
\(\eta\ne0\). This proves the endpoint for every even \(r\)
in the statement, by a fully specified algebraic evaluation of the
same integral highest polynomial. The field inclusion from \(\mathbf Q\)
into this splitting field is injective. A zero polynomial image over
\(\mathbf Q\) remains zero after that scalar extension, so the
nonzero value detects the original map as well.

## 6. Transfer to the actual canonical image

Let \(W=V^*\), and let \(\mathcal K_{a,b}(W)\) be the
annihilator of the image of (BS.1) under the normalized symmetric
tensor pairing. The actual last-slot inclusion and coefficient
polarization from K.16–K.22 give
\[
\delta\mathcal K_{a,b}(W)
\subset\ker T_{r,r,b}(W)\otimes\operatorname{Sym}^bW
\tag{BS.32}
\]
throughout both displayed families. To verify its lower-map input,
\[
b-r-(r-1)^2=r-k-1\ge0.
\tag{BS.33}
\]
Thus Sra's Theorem 1.3 proves that the actual lower canonical map
\(h_{b-r,r}\) is surjective at every parameter used here.

The inclusion \(\delta\) is the normalized last-slot splitting
of a symmetric \((r+1)\)-tensor; polynomial evaluation on symmetric
slot functions identifies it with retaining the same polynomial
and distinguishing the last variable. The map \(T_{r,r,b}\)
extracts the coefficient of \(u_1^r\cdots u_r^r\) after the
substitution \(v_i\mapsto v_i+u_i x\) in its first \(r\) slots.
These are the literal maps of (BS.32). The derivation, including
the nonzero factorial and binomial scalars in the annihilator
inclusion, is K.16–K.22 and P.9–P.16; (BS.33) checks precisely
its application range here.

Equations (BS.20), (BS.22), (BS.23), and (BS.31) are nonzero values of
\((T_{r,r,b}\otimes\mathrm{id})\delta\) on the respective
highest polynomials. By (BS.13)–(BS.15), each corresponding
type occurs exactly once in the entire annihilator ambient
module \(\operatorname{Sym}^{r+1}\operatorname{Sym}^bW\).
Equivariance and (BS.32) exclude that single copy from
\(\mathcal K_{a,b}\). The perfect transpose pairing therefore
proves exactly (BS.3).

All constructions use \(a\) coordinate rows. Inclusion into any
larger vector space commutes with symmetric projection, grid
transpose, column alternation, and the displayed coefficient maps.
The polynomial-functor multiplicity of each label with at most
\(a\) rows is unchanged: the highest vectors involving those
coordinate rows and their raising equations give the same Schur
multiplicity space. Hence the same nonzero canonical component
persists in every stated ambient dimension.

The lower-map source is Suvrit Sra, *The q-Foulkes problem III: On
Foulkes' conjecture with a graded inner factor*, Theorem 1.3,
[primary PDF](https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf).
The exact range used is \(h_{B,r}\) surjective for
\(B\ge(r-1)^2\). The remaining maps, polynomial identities,
parameter arithmetic, and nonzero coefficients have been proved
explicitly above.


# Current map ranges and the exact remaining transfer

## M-001. Canonical maps, coefficient inequalities, and the checked parameter ranges

Use the actual normalized grid morphism
\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
 \longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a,
\quad b\ge a.
\]
Its adjoint, for the invariant tensor inner products, is the transposed-grid map \(h_{a,b}\). This follows by taking the adjoint of the orthogonal row and column averaging projectors: \((P_KP_H)^*=P_HP_K\). Thus surjectivity of the displayed map and injectivity of its adjoint are equivalent by finite-dimensional linear algebra. The dimensions of the source and target multiplicity spaces are the two plethysm coefficients, while their common matrix rank is G-002/G-011. These are the exact maps connecting the several assertions used below.

The strongest uniform bound located and checked in this run is Suvrit Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a graded inner factor*, v1, 29 October 2026, Theorem 1.3 and its proof in Section 2.2: the displayed map is surjective for
\[
b\ge(a-1)^2.
\tag{M1.1}
\]
The proof, including Lemma 2.1 and the common-polarization induction, was read in full. Its statement is used as a cited result. The September 2026 bound \(b\ge a(a-1)\) in OpenAI's *Quadratic stabilization for Foulkes' conjecture*, Theorem 1, is contained in (M1.1). The endpoint observation T-015 is retained as work history and makes no improvement to (M1.1).

The canonical binary map is an isomorphism on every output with at most two rows, for every \(a,b\), in all ambient dimensions: this is G-006, carrying Landsberg's Theorem 7.21 through the natural Schur-functor multiplicity spaces. The actual morphism, and its rank on every such block, are specified there.

Cheung--Ikenmeyer--Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, arXiv:1509.03944v1, Theorem 6(a), proves injectivity of \(h_{5,6}\); Theorem 6(b) records the kernel at \((5,5)\). Theorem 6(c) supplies the exact component
\[
\lambda=(20,7,6,1,1,1)
\]
with multiplicity one in each \(\operatorname{Sym}^6\operatorname{Sym}^6 V\), on which \(h_{6,6}\) is zero. This is a concrete test of the rank step: both multiplicities equal one while the prescribed map has rank zero.

The coefficient inequality for outer degree six is supplied by OpenAI, *Foulkes' conjecture for sixth powers*, 25 September 2026, Theorem 1.1. Its exact assertion is existence of an equivariant injection for all inner degrees at least six. The current run read its statement, reduction, and computation descriptions; it did not execute its full certificates and does not label the source formally verified. The specified zero component at \((6,6)\) remains a property of the prescribed canonical map. The two assertions are related by the common multiplicity spaces and the explicit zero matrix on that component.

Evseev--Paget--Wildon, *Character deflations and a generalization of the Murnaghan--Nakayama rule*, Corollary 5.2, supplies the coefficient inequality for \(a\le b\) and \(a+b\le19\). Sra III, Theorem 1.4, supplies the stated graded inequalities in depths at most six for \(b\ge a\ge4\), and the further depth-seven, eight, and ten ranges in that theorem. Those finite graded certificates were inspected as source evidence and were not replayed in this run. No canonical-map rank is inferred from these dimension inequalities.

The actual rank findings of this run include the prime-width and product families R-008–R-009, the all-even-rank determinant boundary preimages R-021, the recursive whole-isotypic ranges R-024, and the explicit cofactor families R-025–R-026. Each proof specifies an actual preimage or excludes the displayed irreducible line from the exact transpose annihilator. For R-024, a≥6 and b≥binom(a,2)−4 give surjectivity on every target isotypic component with λ2≤b−binom(a,2)+10; the additional endpoint and triangular profiles are proved there.

For R-026, put r=a−1≥3 and b=r²−k, 2≤k≤r−1. When r is even, the image label is ((r²)^r,r²−k(r+1)). When r is odd, it is (r²,(r²−1)^(r−2),r²−3,r²−(k−1)(r+1)). The target multiplicity and actual image multiplicity are both one. R-025 supplies the adjacent degree b=r²−1 with its displayed parity-dependent labels. The full varying canonical-map surjectivity problem below the square bound remains an exact annihilator gate, narrowed by R-019–R-024 and these explicitly excluded components.

## M-002. The orbit, theta, and purity transfer gates

The compact dual pair and its vacuum twist in T-001 identify the polynomial oscillator module with the Cauchy decomposition. Balanced weight extraction gives \((S_\lambda\mathbb C^m)_{(n^m)}\), and the specified symmetric-group Reynolds idempotent gives its invariant part. The ordinary Gelfand--Tsetlin polytope counts the whole weight space. Its transfer to plethysm is exactly the finite projector, evaluated by G-009 and, explicitly for \(m=3\), G-012. T-005's determinant sign and G-001's nonmonomial example identify failures of the particular unprojected count and permutation-basis construction, with their exact morphisms.

The attached Alpöge note is cited as instructed. Its steps 7 and 8, page 4, discuss interlacing period multiplicities and iterated theta lifts. The cited declarations `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, and `ALPOGE_LEAN_SCAN.tsv` are absent from the supplied ZIP; no declaration in them was inspected in this run. The transfer needed for the present question is an explicit equivariant map from the groups and representations of those steps to the balanced-weight representation together with its normalizer idempotent, or to the two grid idempotents defining \(h_{b,a}\). The four-page note supplies no such object or map. The exact compact theta realization in T-001--T-002 and the invariant presentations in G-009--G-011 establish the formulas directly without such an identification. No claim about the cited RH and GRH theorems is needed for these proofs.

For the suggested purity route, G-004 constructs the two exact Artin projectors on \(\operatorname{Spec}\mathbb F_{q^2}\). Both images have weight zero, while their invariant dimensions are one and zero. It computes the missing datum explicitly: the projector rank. This calculation leaves available geometric constructions that include the projector, such as the finite quotient and coherent-module constructions proved here.

For width seven, T-016--T-020 identifies the open orbit with stabilizer \(G_2\times\mu_3\), and the extension map is the inclusion of polynomial functions into their discriminant localization. The end-node sector has the exact valuation and positive formula of T-018. The remaining valuation filtration for other highest weights is an explicit smaller orbit calculation. G-009--G-010 already give terminating positive counts for those coefficients; the unresolved question there is a small direct orbit formula replacing the general elimination construction.

The requested Masullo locator is an input gate: no Masullo work, statement, or identifier occurs in the supplied file inventory. A theorem or a map from such a work is not introduced by inference.

## Source URLs

* Sra III: <https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>; supplement: <https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1-supplement.pdf>.
* Cheung--Ikenmeyer--Mkrtchyan: <https://arxiv.org/abs/1509.03944>.
* Landsberg's supplied survey, Theorem 7.21: <https://arxiv.org/abs/1305.7387>.
* Alpöge: <https://alpo.ge/remark.pdf>, attached four-page file, steps 7--8 on page 4.

This register is a current-source audit dated 21 November 2026, Europe/Berlin. Its labels identify the audit and explicit morphisms; the attributed literature theorems remain cited results.


\part{Checked archive findings and integral identities}


# Archive audit for GCT_PLETH

Run: `/root/archive_audit`, 21 November 2026 (Europe/Berlin).
Model: GPT-6 Astra Pro; effort setting is not exposed in the agent context.

## Evidence and scope

All thirteen supplied `ARCHIVE_*.tex` files were read in full. They are transcriptions, not images. The uncertainties, deletions, and corrections encoded in them remain evidence about the transcription. The public-source follow-up in `PRIMARY_SCAN_FOLLOWUP.md` now records direct inspection of all thirteen original Montpellier target leaves, from cotes2,4,12,16,43,79,89,119,133, together with their defining neighbors where needed. `SA17_STUDY_cote133_lambda.md` was read in full. Its statements about scans absent from the supplied transcription set are prior-run reports; the lambda/finite-set pages133/004 and133/019–029 have now also been inspected directly, with current-run proofs distinguished in `STUDY_ADDITIONS.md`. Its claimed equivariant check on scan133/019 is refuted below and checked against the actual manuscript. The additional single-map-power summand assertion is likewise present on original133/025 and is refuted in A-013.

The symbol `WG` on 133/006 is explicitly the group completion of the orthogonal-sum monoid of isometry classes. Write it `GW^⊕` here. Write `GW` for the quotient that also imposes the metabolic relation `[M]=[H(L)]` for a Lagrangian `L`. There is a concrete surjective ring map

\[
q:GW^\oplus\longrightarrow GW,
\quad [M,b]\longmapsto[M,b],
\]

with kernel generated by the differences `[M]-[H(L)]`. The corresponding forgetful maps land respectively in the split Green ring `K_0^⊕` and the exact Grothendieck ring `K_0`. Exterior powers commute with these forgetful maps. The map `q` and its nonzero kernel are essential in A-003; the general special-λ theorem for `GW` cannot be pulled back through this noninjective map merely by citing it.

## A-001. Cote 133, scan 019: symmetric powers, subsets, and the supplied study's counterexample

**Statements on the page.** The page displays `σ_t(E)λ_{−t}(E)=1`, `λ_t(L)=1+tL`, `σ_t(L)=(1−tL)^{-1}`, `σ²(E)=E²−λ²(E)`, `σ²(E)=λ²(E)+E`, and `2λ²(E)+E=E²`. The last numerical check is `2 binom(d,2)+d=d²`. It also asks for `λ^i(xy)`.

For a locally free sheaf, the first four formulas are the standard exterior/symmetric-power identities in exact `K_0`. The short exact sequence

\[
0\longrightarrow\Lambda^2E\xrightarrow{u\wedge v\mapsto u\otimes v-v\otimes u}
E\otimes E\longrightarrow\operatorname{Sym}^2E\longrightarrow0
\]

is locally split as a sequence of underlying modules and proves the degree-two identity. Exterior-power operations on this exact `K_0` satisfy the universal special-λ identities; see SGA 6, V, Lemma 2.2.1 and VI, Theorem 3.3. The line identities follow directly from the one-dimensional tensor powers. These are known identities, not novelty claims.

**Refutation in the finite-set reading used by the supplied study.** Let `G=C_2` and let `E={0,1}` with the nonidentity element interchanging the points. In the Burnside ring `B(G)`, write `1` for the singleton. The unordered two-element subsets form `1`. The two-element multisets form `E+1`: two doubled points are interchanged and the mixed pair is fixed. Ordered pairs form two free orbits, so `E²=2E`. Consequently

\[
\lambda^2_{\rm subset}(E)=1,\qquad
\sigma^2_{\rm multiset}(E)=E+1,\qquad E^2=2E.
\]

The boxed equality would assert `2+E=2E`. Apply the fixed-point ring homomorphism

\[
\phi_G:B(G)\longrightarrow\mathbb Z,
\qquad [X]\longmapsto|X^G|.
\]

Its two sides are `2` and `0`. This is a counterexample, including after group completion. The numerical cardinality map `φ_1` sends both sides to `4`; that explains exactly what the last numerical line verifies.

**Exact dictionary.** Linearization `\ell:B(G)→R_\mathbb Q(G)` sends `E` to `1+ε`, with `ε` the sign character. It commutes with symmetric powers because the monomial basis of `Sym^n\mathbb Q[E]` is the multiset basis. It does not carry the unsigned-subset operation to exterior powers: `\ell(\lambda^2_{subset}E)=1`, whereas `\Lambda^2\ell(E)=ε`. The Burnside pre-λ operation determined by `λ_t=σ_{−t}^{−1}` has

\[
\lambda^2(E)=E^2-\sigma^2(E)=E-1,
\]

whose linearization is `ε`. Thus the discrepancy is exhibited by actual maps and a nonzero element, rather than by a claimed absence of mathematical relations.

**Plethysm consequence.** The page's valid `K_0` identities supply λ-polynomial arithmetic. The unsigned finite-subset identity cannot be used to derive equivariant multiplicities: the `C_2` counterexample already changes an irreducible constituent. The source `SA17`, section “Scan 19: λ- and σ-operations”, incorrectly records the simultaneous equivariant equalities as checked.

## A-002. Cote 133, scan 006: the rank obstruction in characteristic two

**Statements on the page.** The group completion of strictly nondegenerate quadratic modules is asserted to have a pre-λ structure augmented by rank; on a connected base where `2` is not invertible the ranks are even; with `2` invertible there is a unit. It asks whether the universal product and iterate formulas hold, and reduces their study to classifying topoi of orthogonal groups.

**Proof of the parity statement.** Over a characteristic-two residue field, the polar bilinear form of a quadratic form is alternating. A nondegenerate alternating matrix has even size (successive hyperbolic-pair elimination proves this). On a connected ringed space, the rank of a locally free module of finite constant rank is constant. A point with characteristic-two residue field therefore forces its rank to be even. The assertion needs such a point; saying merely “2 not invertible” for an arbitrary locally ringed topos still requires the usual stalk interpretation.

**Counterexample to the stated pre-λ augmentation.** Already over `Spec\mathbb F_2`, every object in the specified monoid has even rank, hence every element of its group completion has even rank. The hyperbolic plane has rank two. A pre-λ augmentation to the binomial λ-ring would give

\[
\operatorname{rk}(\lambda^2H)=\binom22=1,
\]

which is impossible in that group. This refutes the pre-λ assertion with precisely the exterior/rank compatibility written on the page. Also the standard unital definition has `λ^0=1`, whose rank is one. The nonunital parenthesis does not repair the displayed rank compatibility.

With `2` invertible, use the explicit inverse maps `q↦b_q/2` and `b↦(v↦b(v,v))` between quadratic forms and symmetric bilinear forms. Tensor products, the form on exterior powers, and the rank-one unit are defined through this equivalence. The quadratic hyperbolic form `q_H(v,φ)=φ(v)` corresponds to the bilinear matrix with off-diagonal entries `1/2`; scaling one of the two summands by `2` identifies it with the customary bilinear hyperbolic matrix with off-diagonal entries `1`. This fixes the convention used below. The remaining special-λ question for the literal group completion is answered by A-003.

## A-003. Cote 133, scan 006: the literal split ring fails the special-λ identities even with 2 invertible

This is a complete counterexample to the page's general special-λ question for `GW^⊕`.

Let `k=\overline{\mathbb F}_3`, `G=C_3`, and `S=BG` with structure sheaf `k`. The associated vector-bundle category is finite-dimensional `kG`-modules. Let `J_i`, `1≤i≤3`, denote the indecomposable module whose generator acts as a single unipotent Jordan block of size `i`. Every module is a direct sum of these three, uniquely, because `(g−1)^3=0`. Thus the additive group of the split Green ring is free on `1=[J_1]`, `y=[J_2]`, and `x=[J_3]`.

Choose `J_3=k[G]` with its permutation basis and nondegenerate invariant dot-product bilinear form; denote the symmetric form class by `X`. Let `Z=H(J_2)`. Under forgetting forms, `F(X)=x` and `F(Z)=2y`.

The split Green-ring identities are

\[
x^2=3x,\qquad xy=2x,\qquad y^2=x+1,
\quad \lambda^2x=x,\quad\lambda^3x=1,
\quad\lambda^2y=1,\quad\lambda^3y=0.
\tag{A3.1}
\]

The first two follow from the equivariant isomorphism `kG⊗M≅kG^{dim M}`: the map on basis vectors is `g⊗m↦g⊗g^{-1}m`, with the group acting on the first factor in the codomain. For the third, take `g=[[1,1],[0,1]]`. On `J_2⊗J_2`, `N=g⊗g−1` has rank two, `N²` has rank one, and `N³=0`; hence the Jordan type is `(3,1)`. On `\Lambda^2J_3`, the action is again a 3-cycle on the basis `e_1∧e_2,e_2∧e_3,e_3∧e_1`, so it is `J_3`. Both determinants are one. These computations prove (A3.1); `check_archive.py` additionally verifies the finite-field matrix ranks and exterior matrices exactly.

In every pre-λ ring, Newton's polynomial gives

\[
\psi^3(a)=a^3-3a\lambda^2(a)+3\lambda^3(a),
\]

and `ψ³` is additive; this follows by extracting the third coefficient of `t(d/dt)logλ_t`. The special-λ product polynomials force `ψ³(ab)=ψ³(a)ψ³(b)`: over universal line elements both sides are `\sum_{i,j}u_i^3v_j^3`, an integral symmetric-polynomial identity.

Equation (A3.1) gives

\[
\psi^3(x)=3,\qquad \psi^3(y)=2x-2y.
\]

The forgetful map commutes with every exterior power and hence with `ψ³`. Since `F(XZ)=x(2y)=4x`, the two required sides after forgetting are

\[
F(\psi^3(XZ))=12,
\qquad F(\psi^3(X)\psi^3(Z))=12x-12y.
\]

Their difference is `12(x−y−1)`, a nonzero element of the free abelian group on `J_1,J_2,J_3`. The coefficients here are integers in a Grothendieck group, not scalars in `k`. Consequently `GW^⊕(BC_3)` with its exterior powers is not a special λ-ring.

The separate iterate identity is now refuted in **A-015**, `ITERATE_COUNTEREXAMPLE.md`. For the actual object `A=X⊥H(J₂)`, the underlying class is `a=x+2y`. Its second exterior power is `6x+3`, and its iterated third exterior power is `441x+7`. The universal polynomial `Q_(3,2)=e₁²e₄−2e₂e₄−e₁e₅+e₆+e₃²` instead evaluates to `445x−4y+3`, giving the nonzero defect `−4(x−y−1)`. The universal polynomial was verified coefficient by coefficient in six variables; this is injective in symmetric-function degree six. Both the product and iterate questions therefore have separate explicit counterexamples for the literal split ring.

**Exact geometric transfer.** The representations with forms define homomorphisms of group schemes `C_3→O_3` and `C_3→O_4`, and hence a classifying-topos map `BC_3→B(O_3×O_4)`. Restriction pulls back the two universal quadratic modules to `X,Z`. This is the concrete instance of the universal orthogonal-group reduction proposed in the margin.

**Relation with the modern theorem.** Zibrowius, *Symmetric representation rings are λ-rings*, NYJM 21 (2015), Definition 1.2, p.1060, defines `GW` by orthogonal-sum and metabolic relations; its main theorem, p.1056, establishes the special-λ structure on that quotient. For the present `C_3`, exact `K_0` sends `J_i` to `i[J_1]`, and therefore sends `x−y−1` to zero. The counterexample establishes precisely why the split statement cannot be substituted for that cited theorem. Zibrowius, *The γ-filtration on the Witt ring of a scheme*, arXiv:1411.3198v2, Theorem 2, extends the theorem to schemes over a field of characteristic different from two; Proposition 2.15 supplies the `O_n×O_m` torsor construction. These known theorems are cited, not reproved.

**Plethysm consequence.** Passing to exact `K_0` retains the usual Schur operations by SGA 6 VI 3.3. Working in the uncorrected split quadratic ring would invalidate even the degree-three universal product relation. The correcting quotient is explicit.

## A-004. Cote 133, scan 008: hyperbolic sums and the proposed equivalence relation

### A-004a: explicit isometry with 2 invertible

For a strictly nondegenerate quadratic form `q` with polar form `b` over a ringed topos in which `2` is invertible, define

\[
\Phi:(M,q)\perp(M,-q)\longrightarrow H(M),
\quad (x,y)\longmapsto(x+y,\tfrac12 b(x-y,-)).
\]

The hyperbolic quadratic form evaluates this image to
`b(x−y,x+y)/2=q(x)−q(y)`. Nondegeneracy of `b` and invertibility of `2` give an inverse by solving for `x+y` and `x−y`. This formula is natural in isometries, hence works on classifying topoi as well. The page's classifying-topos caveat therefore has no example in this range. The symmetric-bilinear version appears as Zibrowius 2015, Lemma 1.1, p.1059; the displayed formula here translates it into the page's quadratic convention.

### A-004b: a characteristic-two classifying-topos counterexample

Let `k=\overline{\mathbb F}_2`, `M=k²`, and `q(x,y)=xy`. Its polar form `b((x,y),(x',y'))=xy'+x'y` is nondegenerate. Let `G=O(q)=\mathbb G_m\rtimes C_2`, with the torus acting by `diag(t,t^{-1})` and the involution interchanging coordinates. The module `M` is simple: a torus-stable submodule is a sum of its two distinct weight lines, and the involution exchanges those lines. Its equivariant endomorphism ring is `k`. Its invariant bilinear forms are exactly the multiples of `b`, hence alternating.

For every `G`-module `E` and every `G`-map `f:M→H(E)=E⊕E^∨`, write `f=(i,j)`. The bilinear form `B(u,v)=j(v)(i(u))` on `M` is `G`-invariant, so `B(v,v)=0`. Therefore `q_H(f(v))=0` for every such map.

The first-summand map `M→(M,q)⊥(M,q)` has pullback `q≠0`. Thus `(M,q)⊥(M,q)` cannot be isometric to `H(E)` for any `E`. The same argument, using the first summand, proves

\[
(M,q)\perp(M,q)\perp H(F)\not\simeq H(E)
\]

for all `E,F`. This proves the page's suggested failure on `BO(2)` with full characteristic and form data.

The proposed relation on scan 008 requires `q⊥(−q')⊥H(F)≅H(E)`. In this example `−q=q`. Taking `q'=q`, the displayed impossibility says that the proposed relation is not even reflexive. Consequently it cannot describe a quotient in the stated generality. It does describe the usual stable-hyperbolic relation in the range of A-004a: adding negative forms removes the extra group-completion stabilizer because every `P⊥(−P)` is hyperbolic.

## A-005. Cote 133, scan 008: the hyperbolic ideal and failure of λ descent

Over a base with `2` invertible, let `F` forget the form and `H` be the hyperbolic functor. The exact identity

\[
(M,b)\otimes H(E)\simeq H(M\otimes E)
\tag{A5.1}
\]

uses `b:M≅M^∨` to identify the second summand `M⊗E^∨` with `(M⊗E)^∨`. The hyperbolic pairing is carried to the tensor-product pairing. Thus the image of `H` is an ideal in the corresponding form ring. The two available additive maps are `H:K_0^⊕→GW^⊕` and `H:K_0→GW`. The map from exact `K_0` to the split form ring need not be well-defined: in characteristic three, `J_2=2J_1` in exact `K_0`, while the split forgetful images of `H(J_2)` and `H(2J_1)` are `2J_2` and `4J_1`.

The rank of `H(E)` is even, so rank modulo two descends to the Witt quotient. Exterior powers do not descend, already over any field of characteristic different from two: the hyperbolic plane is zero in the Witt ring, but its determinant form is

\[
\lambda^2 H(1)=\langle-1\rangle.
\]

In the quadratic convention fixed in A-002, the determinant coefficient is initially `−1/4`, and the change of basis by `2` gives the displayed isometry to `\langle-1\rangle`. The latter has odd rank, hence nonzero rank modulo two in the quotient. Since `λ²(0)=0`, no operation on the quotient can commute with both the quotient map and this exterior-power operation. This completely answers the page's descent question for the ordinary Witt quotient.

## A-006. Cote 133, scan 009: characteristic classes and the struck-out claim

The page specifies naturality, normalization on symmetric lines, and `w(x+y)=w(x)w(y)`, then states universal product and exterior-power formulas. For schemes over `\mathbb Z[1/2]`, the exact modern input is the étale-cohomology splitting morphism of Zibrowius 2016, Proposition 3.3: it splits a symmetric bundle into symmetric lines and is injective on `H^*_{et}(-,\mathbb Z/2)`. This is sufficient for the following precise restatement of the page.

Write the degree-one classes of the split lines of `E,F` as `u_1,…,u_r` and `v_1,…,v_s`. Naturality and injectivity carry back the formulas

\[
w(E)=\prod_i(1+u_i),\qquad
w(E\otimes F)=\prod_{i,j}(1+u_i+v_j),
\]
\[
w(\Lambda^a E)=\prod_{|I|=a}\left(1+\sum_{i\in I}u_i\right).
\tag{A6.1}
\]

The products are symmetric in each root family, so each coefficient is a universal polynomial in the elementary symmetric functions and the ranks. Tensoring symmetric lines adds their degree-one Kummer classes, which proves the root substitution in (A6.1); exterior powers select subsets. The injective pullback proves the formulas before splitting. For virtual classes total `w` takes values in the completed group `1+\prod_{i>0}H^i`; the completion is needed to invert total classes without a cohomological-dimension bound. SGA 6, V §6 describes the associated Chern-ring universal construction. The page does not specify such a ring structure on its displayed target, and its assertion of a λ-homomorphism is read through this universal construction.

The struck-out claim `w∘H=1` is false. Over `Spec\mathbb R`, `H(1)≅\langle1,-1\rangle`, and normalization gives `w_1(H(1))=(-1)≠0` in `H^1_{et}(\mathbb R,\mathbb Z/2)`. Thus total `w` does not factor through the Witt quotient. This counterexample suffices without relying on the more elaborate formula in the supplied SA17 study. The study's formula for hyperbolic bundles is not used in this run.

**Plethysm consequence.** Applying (A6.1) to iterated Schur operations computes characteristic classes of those bundles. The exact morphism `GW→H^0(\mathbb Z)×(1+\widehat H^+)` does not provide the full irreducible-character expansion; e.g. the characteristic-three defect in A-003 already maps to zero after exact passage. No assertion about all possible geometric ways to recover that expansion is made.

## A-007. Cote 133, scan 028: tensor-power identity and its positivity test

Let `X` be a commutatively ringed topos over `\mathbb Q`, `E` a finite locally free object, and `ν=(1^{α_1}2^{α_2}…)⊢n`. Put

\[
\rho_i=[\mathbf1_{S_i}],\qquad
\rho_\nu=\prod_i\rho_i^{\alpha_i}
=[\operatorname{Ind}_{\prod_jS_{\nu_j}}^{S_n}\mathbf1].
\]

The product here is induction. With `m_ν` expressed as an integral polynomial in `e_1,…,e_n`, the page's formula is

\[
[E^{\otimes n}]=\sum_{\nu\vdash n}m_\nu(E)\rho_\nu.
\tag{A7.1}
\]

**Proof in this fully specified setting.** The split semisimple algebra `\mathbb Q[S_n]` decomposes into matrix algebras indexed by partitions. Its rational idempotents act on `E^{⊗n}` and give the functorial decomposition

\[
E^{\otimes n}\simeq\bigoplus_{\lambda\vdash n}S_\lambda(E)\otimes[\lambda].
\tag{A7.2}
\]

Thus `K_0(BS_{n,X})≅\bigoplus_{λ⊢n}K_0(X)`. The Frobenius-characteristic map sends `[λ]` to `s_λ` and `ρ_ν` to `h_ν`. Apply evaluation at `E` to the first factor of the Cauchy identity

\[
\sum_\lambda s_\lambda(x)s_\lambda(y)
=\prod_{i,j}(1-x_i y_j)^{-1}
=\sum_\nu m_\nu(x)h_\nu(y).
\]

The equality of coefficients in this direct sum is precisely (A7.1). This is a proof of the page's formulation from the known Cauchy and Schur–Weyl theorems, not a new proof of those theorems. The exact primary locators in Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., are I (4.2), p.62, and (4.3), p.63, for the two Cauchy expansions; I (7.3)–(7.6), pp.113–114, for the characteristic map and irreducible characters; Appendix A (5.6), p.156, for the tensor-power decomposition. These equations were inspected in the primary PDF.

The coefficients singled out in the supplied study are `m_(1^n)=e_n` and `m_(n)=p_n`, hence exterior and Adams operations. The `m_ν` are integral and isobaric of weight `n` by the fundamental theorem of symmetric polynomials. This confirms the polynomial claim.

**Counterexample to the direct-summand reading of the margin.** Take `X=BGL_{2,\mathbb Q}` and `E` the standard rank-two bundle. In degree two,

\[
\tau^2(E)=\psi^2(E)\rho_2+\Lambda^2(E)\rho_1^2,
\qquad \psi^2(E)=\operatorname{Sym}^2(E)-\Lambda^2(E).
\]

The character of `ψ²(E)` is `x_1²+x_2²=s_(2)−s_(1,1)`. A genuine characteristic-zero `GL_2` representation decomposes into irreducibles with nonnegative multiplicities; the coefficient `−1` proves that this virtual class is not such a representation. Therefore the first summand in the displayed monomial expansion cannot be realized as an actual direct summand of `E^{⊗2}`. The exact change of basis `ρ_1²=1+sgn` cancels that negative term and gives the positive decomposition (A7.2): `Sym²(E)⊗1 ⊕Λ²(E)⊗sgn`.

**Modular polynomial-ring question reported by SA17.** In exact `R_{\mathbb F_2}(S_2)`, the regular module has a filtration with two trivial factors. Hence `ρ_1²=2ρ_2`, refuting polynomial independence of the indicated generators. The map from the split Green ring to the exact representation ring sends the indecomposable regular module to this class; the relation is asserted in the latter. The general integral/ringed-topos version of (A7.1) is now proved in **A-012**, `TENSOR_POWER_INTEGRAL.md`, using the ABW integral Cauchy filtration and three exact torus-weight extractions. It holds for exact K₀ of bounded-rank finite locally free modules on every commutatively ringed topos; no semisimplicity or polynomial independence of the Young classes is assumed.

The coefficient-ring question has two further explicit answers. **A-021**, `MIXED_CHAR_LATTICES.md`, proves that rationalization gives `K₀(O[S_n]-lattices)≅R_K(S_n)` for every characteristic-zero discrete valuation ring `O` with fraction field `K`. The inverse is specified on the Specht classes, and compatibility with induction yields the polynomial ring `Z[ρ₁,ρ₂,…]`. This includes the study's expressly open `Z_p` case. **A-023**, `LOCAL_RING_COUNTEREXAMPLE.md`, takes the characteristic-zero local ring `A=Z_(2)[ε]/(2ε,ε²)` and the rank-one `S₂` action `g↦1+ε`. Its determinant character lies outside the subgroup generated by the determinants of `ρ₂` and `ρ₁²`, proving failure of generation. **A-020** also verifies `rank R_(F_p)(S_p)=p(p)−1` from James's all-field simple-module classification. OriginalPDFpage29 was inspected; the remaining question is the full classification of coefficient rings.

**Plethysm consequence.** Schur–Weyl gives positive Schur objects; the monomial expansion supplies signed universal λ expressions. Further composition `s_μ[s_ν]` is well-defined in the same free λ-ring. A-007 does not identify a lattice-point basis for its coefficients. It refutes specifically the proposed direct-summand reading of (A7.1), while giving the exact basis morphism that relates the formulas.

The subsequent constructions G-009–G-012 complete the finite positive-count calculation by explicit invariant-algebra and coherent-module presentations. In particular, G-010 treats every Schur plethysm coefficient through the actual wreath-product covariant module, and G-011 presents the image of the actual canonical-map projector. G-012 evaluates the outer-degree-three algebra with six generators and two relations, giving four explicit bounded polytopes. These constructions and their independent complete proof reviews are recorded in `ROOT_PROOF_REVIEW.md`; no generic unevaluated-projector gate remains for terminating finite positive counts. Bounds polynomial in varying input size and global open injectivity families require additional results not asserted by those constructions.

## A-008. Cote 43, scan 037: Witt-series formulas

The page's series ring is represented by `Spec\mathbb Z[a_1,a_2,…]`, with addition given by multiplication of series. Use the explicit isomorphism to the conventional big Witt series

\[
\alpha(f)(t)=f(-t)^{-1}.
\]

It sends the page's line element `1+at` to the conventional Teichmüller series `(1−at)^{-1}`. Transporting the conventional Witt multiplication gives `(1+at)*f(t)=f(at)`. This fixes the convention without identifying two products silently.

For an `\mathbb F_p`-algebra `A`, define `F(\sum a_i t^i)=\sum a_i^p t^i` and `V(f)=f(t^p)`. The ring-scheme multiplication has integer coefficients, so coefficient Frobenius preserves it. Direct multiplication of series in characteristic `p` gives

\[
f(t)^p=F(f)(t^p),\qquad FV=VF=[p].
\]

Here `[p]` is multiplication by `p` in the additive Witt group, hence the ordinary `p`th power of a series. Also `V(fg)=V(f)V(g)`, proving its additivity. Iterating and applying the line-element rule yields

\[
(1+x t^{p^i})*f(t)=F^i(f)(x t^{p^i}).
\]

To justify the page's substitution `x=a^{p^i}` for arbitrary `x`, adjoin `a` using the monic algebra `A[a]/(a^{p^i}−x)`. It is free as an `A`-module, so `A` injects into it; the equality checked there descends coefficient by coefficient. This fills the explicit algebraic step in the page.

The map to `p`-typical Witt vectors is the truncation map associated with the divisor-stable set `{1,p,p²,…}` after `α`; its ghost coordinates retain the indices `p^r`, and it sends `1+at` to the Teichmüller vector `(a,0,…)`. This is the standard big-to-typical construction, cited rather than reproved; see Hazewinkel, *Witt vectors. Part 1*, §§14.1–14.8, pp.71–73. Those paragraphs explicitly establish that the operation polynomials in coordinate `n` involve only coordinates whose indices divide `n`, and hence that selecting the `p`-power coordinates defines the quotient functor on every commutative ring. The page's assertion that line values determine the map needs naturality and continuity in the series filtration; those are part of this specified natural Witt morphism.

**Plethysm consequence and Borger dictionary.** The representing symmetric-function algebra is the free special λ-ring. In the character algebra `R(GL_r)=\mathbb Z[x_1^{±1},…,x_r^{±1}]^{S_r}`, the Adams map is `ψ^p(f)=f(x_1^p,…,x_r^p)` and is congruent to `f^p` modulo `p`. This proves the commuting Frobenius-lift property on `Spec R(GL_r)` directly. Borger, supplied `lrfoe13.tex`, §§1.1–1.2, identifies the free λ-ring with the arithmetic jet space of the affine line and describes its topos adjunctions; §2.2 gives the monoid-algebra Frobenius action. These are explicit morphisms connecting the page to the supplied Borger framework. The character coefficient-extraction problem remains present in the Schur-basis expansion.

The remaining uniqueness claim is now proved in A-018, `WITT_UNIQUENESS.md`: finite coordinate dependence, additivity on universal products of line series, and the injective map from elementary symmetric functions show that an additive affine-scheme morphism is determined by its line values. This applies to the big-to-p-typical map over every characteristic.

## A-009. Cote 2, scan 017: restriction, induction, external tensor products

For a homomorphism of finite groups `u:H→G`, restriction preserves tensor products. On all modules over a commutative ring `R`, the induction projection formula has the isomorphism

\[
R[G]\otimes_{R[H]}(M\otimes\operatorname{Res}N)
\longrightarrow (R[G]\otimes_{R[H]}M)\otimes N,
\quad g\otimes(m\otimes n)\longmapsto(g\otimes m)\otimes gn.
\]

Its inverse sends `(g⊗m)⊗n` to `g⊗(m⊗g^{-1}n)`. The `H`-balancing relations prove both maps are well-defined; their displayed composites are identities. Restriction along `G→G×G`, `g↦(g,g)`, takes `M\boxtimes N` to `M⊗N`. Extension of scalars identifies iterated induction with induction along the composite. These formulas also apply sheafwise.

OriginalPDFpage16/site15 now explicitly verifies the convention: it defines the all-module category with group action and calls `u_*` extension, with `u*` restriction. Originaltargetpage17 and followingpage18 were also inspected; the displayed formulas and induction product match the transcription.

For subgroup inclusions, `R[G]` is free over `R[H]`, so induction preserves finite locally free underlying objects and exact sequences. For arbitrary group homomorphisms, the corresponding preservation claim is false: `C_2→1` applied to the rank-one sign module over `\mathbb Z` gives coinvariants `\mathbb Z/2`. Thus the page's arbitrary-group-map functors are unproblematic on all modules, but an induced map on the exact `K_0` of locally free objects needs a stated category or an admissibility restriction. The exterior/symmetric/Schur constructions on tensor powers give the finite-operator realization of λ operations mentioned also on cote12/041.

## A-010. The λ-ring and γ-filtration dictionary

The free-ring fact is SGA 6, V, Proposition 4.2 and Definition 4.4: for every special λ-ring `R`, evaluation at `x∈R` is the unique λ-map

\[
\operatorname{ev}_x:\Lambda=\mathbb Z[e_1,e_2,…]\longrightarrow R,
\qquad e_i\longmapsto\lambda^i(x).
\]

Composition of these operations is plethysm. Finite rank is the explicit quotient `Λ→\mathbb Z[e_1,…,e_r]`, with kernel generated by `e_i`, `i>r`; SGA 6 V, Proposition 4.8 and Corollary 4.9 verify its λ-ideal property. Inverting `e_r` gives the full `GL_r` character ring. A rank-`r` bundle `E` with frame torsor `P` supplies the homomorphism `R_\mathbb Z(GL_r)→K_0(X)`, `[W]↦[P×^{GL_r}W]`, used in SGA 6 VI, Theorem 3.3. It carries `S_λ` to `S_λE`, so it carries the universal plethysm identity to the same `K_0` identity on sheaves.

For the rank augmentation, SGA 6 V 3.2–3.4 defines `γ_t(x)=λ_{t/(1−t)}(x)` and V 3.10 defines the filtration generated by products `\prod γ^{i_j}(x_j)` with rank-zero `x_j` and `\sum i_j≥n`. On a splitting pullback with line classes `L_1,…,L_r`, direct substitution gives

\[
\gamma_t(E-r)=\prod_{j=1}^r(1+(L_j-1)t).
\]

The pullback injection and passage to associated graded give the Chern-class interpretation in SGA 6. This supplies an exact translation of every universal Schur expression into γ coordinates.

The map induced by `Spec\mathbb C→BGL_r` sends a representation to its dimension. In characters it is evaluation `x_i↦1`. The nonzero element `[V]-r` lies in its kernel. Thus ordinary rank at a point does not determine the character, with the loss measured by this actual map. Equivariant `K_0(BGL_r)` retains the full character. This is the specific distinction needed when transferring a coefficient statement to geometry; no claim about the impossibility of other geometric constructions is involved.

## A-011. Cote 89, scan 018: the exterior pairing in the rank-two reconstruction

The public original PDFpages16–18 now supply the definitions: `V` is free of rank two over a commutative ring `Λ`, and the disjoint line generators `u,v` form a basis. Write `w=au+bv`. Then

\[
u\wedge v=v\wedge w=w\wedge u
\quad\Longleftrightarrow\quad a=b=-1
\quad\Longleftrightarrow\quad u+v+w=0.
\]

Indeed the middle two wedges are `−a(u∧v)` and `−b(u∧v)`, and `u∧v` is a generator of the free determinant line, so its coefficients can be compared over `Λ`. Over a field, the zero vector, the scalar action on each punctured line torsor, and this reconstruction of addition on independent pairs recover addition on all pairs: dependent pairs lie on one scalar line. The target explicitly discusses this field reconstruction. Although supplied scan018 omits `=0` after `u+v+w`, the preceding original PDFpage17/site16, formula(8), writes the full equation. Thus the repair is supplied by the neighboring manuscript itself. The precise geometric map is `\Lambda² V→\det V`, the identity in rank two. An arbitrary-ring reconstruction of every nonunimodular vector is not claimed from the field argument.

## Complete page inventory and remaining gates

| Cote / scan | Mathematical content inspected | State in this audit | What it supplies for plethysm |
|---|---|---|---|
| 2 / 017 | Tensor pullback, induction projection formula, external product, diagonal restriction, transitivity, symmetric-group categories | A-009 proves the displayed maps; arbitrary-map locally-free preservation refuted by sign coinvariants | The functorial operations used in wreath-product and Schur constructions |
| 4 / 007 | Crystalline vanishing cohomology; an exact sequence marked “Faux”; a dimension formula; Λ-algebraicity qualification | Public original PDFpages2–9 recover the definitions. Section8.3 explicitly admits the crystalline Lefschetz/freeness input; A-014 proves the stable-part and unit-root linear algebra. The geometric exactness and Λ-algebraicity inputs remain identified gates | The inspected pages give no specific plethysm-projector map; G-009–G-012 separately provide explicit invariant-algebra/module maps and positive counts |
| 12 / 041 | `x↦check x ξ^i` involution; expected identity on `σ_i`; duality `x∨=ξ^{−i}x`; λ through finite operator groups | OriginalPDFpp31–43 recover the weight filtration, simple-object and primitive label sets, and Tate class. Targetp41 expressly reserves identity of the involution to its projected motivic theory; construction and self-duality morphisms remain the precise gate | Actual Schur operations through finite symmetric groups are supplied by A-007/A-009/A-012 |
| 16 / 038 | Lefschetz lowering maps `Λ`, kernels, primitive decompositions, hyperplane pull/push identities | Original PDF pp. 33, 34, 36 recover definitions. A-016 proves the complete typed string model, corrects explicit index/type errors, and refutes the last projected equality by P¹/point | Actual restriction, pushforward and primitive-projector maps are supplied; no algebraicity assertion is inferred |
| 43 / 037 | Formal series ring, λ operations, coefficient Frobenius, Verschiebung, `FV=VF=p`, twisted line formula, big-to-typical map | A-008 proves the formulas and conventional-series morphism; A-018 proves additive scheme-morphism uniqueness from its line values | Adams/Frobenius operations on the symmetric-function character scheme |
| 79 / 051 | Scalar action `T_λ`, quadratic scaling of `τ`, triangulated-polyhedron automorphisms | OriginalPDFpp46–51 recover the rank-two Z/n module and wedge model. A-017 proves the scalar action, determinant-square formula and compatible structure maps | Exact determinant map supplies the square; reconstruction of the whole family from one abstract triangulation remains the source's stated question |
| 89 / 018 | Reconstruction from punctured line torsors and the alternating pairing | OriginalPDFpp16–18 supply rank2, the determinant torsor and the missing equation. A-011 proves the basis wedge formula over the ring and full reconstruction over a field | Explicit exterior-square geometry and scalar-line addition |
| 119 / 217 (site216) | Historical account of K-invariants, λ operations, symmetric-group operations, topoi | OriginalPDFpp215–217 identify the1972 Esquisse thématique; the target wording matches its typed reportp3 | The precise mathematical maps are instantiated by A-007/A-009/A-012 |
| 133 / 006 | Quadratic `WG`, rank augmentation, unit, special-λ universal polynomials, orthogonal classifying-topos reduction | Original image checked. Parity proved; pre-λ assertion in characteristic2 refuted (A-002); literal split product identity refuted (A-003) and iterate identity independently refuted (A-015); exact quotient theorem cited | Correct exact-`K_0` target and precise quotient required for Schur identities |
| 133 / 008 | Hyperbolic sum, stable-equivalence criterion, ideal, parity augmentation, λ descent | A-004 proves the invertible2 formula and refutes the characteristic2 equivalence relation; A-005 proves ideal and refutes λ descent; A-019 checks field hyperbolic cancellation in every characteristic | Controls which λ operations survive the quotient |
| 133 / 009 | Stiefel–Whitney normalization, sum, tensor/exterior formulas, completed target, struck-out factorization | A-006 proves the precise scheme formulation and refutes the struck-out factorization; arbitrary-topos extension remains gated by definitions | Characteristic classes of composed Schur objects through explicit root formulas |
| 133 / 019 | λ/σ inversion, line formulas, finite-set-looking square identity, product question | A-001 proves/refutes each specified reading and corrects SA17 | Universal λ arithmetic with the precise signed linearization |
| 133 / 028 | Tensor powers with symmetric-group action, monomial/Young expansion, direct-summand margin | A-007 proves the Q-topos formula and refutes positivity of the monomial summands; A-012 proves the identity integrally on every commutatively ringed topos in exact K₀ | Exact integral filtration bridge, while monomial summands can have negative Schur coefficients |

The study's additional originalPDFpage4 question is answered in **A-022**, `HYPERBOLIC_CLASSES.md`: `w₂(H(L))=c̄₁(L)` and the full higher-rank hyperbolic formula hold over every scheme over `Z[1/2]`. The proof constructs actual line-splitting idempotents on successive nonisotropic-line covers and uses their verified injective cohomology pullbacks. EKVProposition5.5, pp183–184, supplies the primary formula; its original regular-scheme scope is recorded separately from this explicit general proof. The register `ARCHIVE_QUESTIONS.tsv` now has123 rows:80proved,25refuted,18gates. The remaining gates concern the expressly admitted crystalline geometric input, the projected motivic category and self-duality morphisms, literal ill-typed fragments, reconstruction of a family from one unlabeled triangulation, the unspecified arbitrary-topos characteristic-class target, and classification of all coefficient rings. They do not include a generic unevaluated-plethysm-projector gate.

## Source notes for the parent paper

The user-facing paper should label these as checked findings of this run or checked reformulations/counterexamples, not claim first publication. They are independent of the arithmetic RH note. Cited background is recorded separately in `CHECK_EVENTS.tsv`.

Useful primary references inspected in this run:

- Marcus Zibrowius, *Symmetric representation rings are λ-rings*, New York J. Math. 21 (2015), 1055–1092. Main theorem p.1056; Lemma1.1 p.1059; Definition1.2 p.1060; §3.1 p.1068–1069. https://nyjm.albany.edu/j/2015/21-49v.pdf
- Marcus Zibrowius, *The γ-filtration on the Witt ring of a scheme*, arXiv:1411.3198v2 (11 August 2016). Theorem2 p.3; Proposition2.15 pp.17–18; Proposition3.3 pp.19–20 in the paper's displayed pagination (PDF has a one-page-offset ambiguity; use statement numbers). https://arxiv.org/pdf/1411.3198
- SGA6, V2.1, V2.2.1, V2.4.1, V3.2–3.4, V3.10, V4.2, V4.4, V4.8–4.9, V§6, VI3.3. Exact numbering checked in the French transcription at `grothendiecksga.com` and, for VI3.3/V2.2.1, independently confirmed in Zibrowius's primary papers. Original scan download from `iut-theory.org` failed with HTTP503; do not say an original SGA6 scan was visually checked.
- Borger, supplied `lrfoe13.tex`, §§1.1–1.2, §2.2, matching the free-ring, Witt-space, and Frobenius-lift statements cited above.
- Macdonald and Hazewinkel primary PDFs were retrieved for numbered source checks; their formula locators are appended in `SOURCE_NOTES.md`.



# A-012. Integral completion of archive cote 133, scan 028

This completes the exact-K₀ gate left in A-007. The asserted identity holds on every commutatively ringed topos `(X,A)`, with `K₀` formed from finite locally free modules of bounded rank and short-exact-sequence relations. The integral construction below specifies both the map and the exact category. It does not assert polynomial independence of the Young generators in a modular representation ring.

## Statement and conventions

Let `K_n(X)=K₀(BS_(n,X),A)`, the exact Grothendieck group of finite locally free `A`-modules with `S_n` action, and put `K_*(X)=⊕_(n≥0)K_n(X)`. Products from degrees `a,b` to `a+b` are external tensor product followed by induction from `S_a×S_b` to `S_(a+b)`. A class of `K₀(X)` acts on each `K_n(X)` by tensor product with trivial `S_n` action.

For a partition `ν=(ν_1,…,ν_l)` of `n`, define the actual Young permutation module

`ρ_ν = [A[S_n/(S_(ν_1)×⋯×S_(ν_l))]]`.

The orbit basis identifies this with the product of the degree-`ν_i` trivial classes. Let `m_ν` be the ordinary monomial symmetric function, expressed as its integral polynomial in the elementary functions. For every `ξ∈K₀(X)`,

\[
\tau^n(\xi)=\sum_{\nu\vdash n}m_\nu(\xi)\,\rho_\nu
\quad\text{in }K_n(X).
\tag{A12.1}
\]

On an effective class `[E]`, `τⁿ([E])=[E^⊗n]` with the place-permutation action. On virtual classes, `τ` is the homomorphism from addition in `K₀(X)` to the degree-completed multiplicative group `1+∏_(n>0)K_n(X)` constructed below.

## Primary integral input and its exact translation

K. Akin, D. A. Buchsbaum, J. Weyman, *Schur functors and Schur complexes*, Adv. Math. 44 (1982), 207–278, DOI 10.1016/0001-8708(82)90039-1. The original paper was downloaded from the author's current research page and inspected in full around the relevant statements. Local copies: `ABW1982.pdf`, `ABW1982.txt`.

- Theorem II.2.16, printed p.232, supplies a universal free basis of each Schur module by standard tableaux.
- Theorem III.1.4, printed pp.245–246, supplies a natural filtration of `Symⁿ(F⊗G)` by `GL(F)×GL(G)` submodules, with associated graded `⊕_(η⊢n)L_η(F)⊗L_η(G)`.

The paper uses exterior-row notation: `L_(a)=Λᵃ`. To match the partition convention of the archive and Macdonald, **define** `S_λ^int=L_(λ′)`. This is an explicit conjugation of the indexing partition. After this relabeling, its standard tableau basis has weight multiplicities `K_(λν)`, the usual Kostka integers, and the Cauchy associated graded is `⊕_(λ⊢n)S_λ^int(F)⊗S_λ^int(G)`.

Every graded factor is finite free over Z. The filtration is defined by natural exterior-diagonalization and symmetric-multiplication maps, so it is stable under change of bases and scalar extension. Exactness over Z with free successive quotients is preserved by arbitrary base change. Applied locally to free sheaves and glued by this naturality, it gives the same filtration on a commutatively ringed topos. This is the precise transfer used here.

## Three weight extractions from the same filtration

Take `W=Z^n`, with its standard diagonal torus and permutation-matrix `S_n`. Write

`C_λ=(S_λ^int(W))_(1,…,1)`.

This is a finite free Z-lattice with `S_n` action: permuting the torus weights fixes the all-ones weight. No identification of `C_λ` with an irreducible module is required. Taking a torus weight is exact over Z, since a torus comodule is a direct sum of its weight modules, by SGA 3 I Proposition 4.7.3.

**First extraction: the tensor power.** The `W`-weight `(1,…,1)` component of `Symⁿ(E⊗W)` is equivariantly isomorphic to `E^⊗n` through

`e_1⊗⋯⊗e_n ↦ (e_1⊗w_1)⋯(e_n⊗w_n)`.

Permuting the `w_i` is the place-permutation action through this map. Extracting that weight from the Cauchy filtration gives

\[
[E^{\otimes n}]=\sum_{\lambda\vdash n}[S_\lambda^{\mathrm{int}}(E)]\,[C_\lambda]
\quad\text{in }K_n(X).
\tag{A12.2}
\]

**Second extraction: the integral Young relation.** Apply (A12.2) to `E=Z^n`, now equipped with its own diagonal torus, and select the weight `ν` padded by zeroes. The tensor-word basis on the left is the set of words with each letter `j` appearing `ν_j` times. Its permutation action is the Young coset action, since the stabilizer of the ordered word is `∏_jS_(ν_j)`. On the right, the standard tableau basis gives a free weight module of rank `K_(λν)`. Therefore, already over Z,

\[
\rho_\nu=\sum_{\lambda\vdash n}K_{\lambda\nu}[C_\lambda].
\tag{A12.3}
\]

This proof uses the exact filtration; it does not infer integral equality from rational characters.

**Third extraction: the class of the integral Schur functor.** Return to `Symⁿ(E⊗W)` and take an arbitrary `W`-weight `ν`. The left side is the tensor product `⊗_jSym^(ν_j)(E)`, and the graded factors on the right have multiplicities `K_(λν)`. Hence

\[
h_\nu(E)=\sum_{\lambda\vdash n}K_{\lambda\nu}[S_\lambda^{\mathrm{int}}(E)].
\tag{A12.4}
\]

Here `[Symᵃ(E)]=h_a(E)` follows from the exterior/symmetric Koszul identity in exact K₀, including in positive characteristic. The corresponding symmetric-function identity is `h_ν=Σ_λK_(λν)s_λ`. The Kostka matrix is integral triangular with diagonal entries one, so its transpose is invertible over Z. Comparing and inverting (A12.4) gives

`[S_λ^int(E)]=s_λ(E)`.

This proves the needed Schur/λ polynomial dictionary without a character-injectivity assumption over Z or a semisimplicity assumption.

Now substitute into (A12.2) and use `s_λ=Σ_νK_(λν)m_ν`, followed by (A12.3):

`Σ_λs_λ(E)[C_λ]=Σ_νm_ν(E)Σ_λK_(λν)[C_λ]=Σ_νm_ν(E)ρ_ν`.

This proves (A12.1) on effective classes for every commutatively ringed topos in the declared exact category.

## Exact-sequence relations and virtual classes

For `0→E′→E→E″→0`, filter `E^⊗n` by the number of factors in `E′`. The associated graded degree with `a` such factors is

`Ind_(S_a×S_(n−a))^(S_n)((E′)^⊗a ⊗ (E″)^⊗(n−a))`.

The submodules and quotients are finite locally free: this is checked after a local splitting of the original sequence, and the filtration itself is natural and `S_n` stable. Thus, with the induction product,

`τ(E)=τ(E′)τ(E″)`.

Consequently `τ` descends to the exact Grothendieck group and extends to differences by inversion of a series with constant term one.

Define `Φ_n(ξ)=Σ_(ν⊢n)m_ν(ξ)ρ_ν`. The universal alphabet-splitting identity

`m_ν(x+y)=Σ_(α∪β=ν)m_α(x)m_β(y)`

and the actual induction identity `ρ_αρ_β=ρ_(α∪β)` give `Φ(ξ+η)=Φ(ξ)Φ(η)`. The alphabet identity is an integral symmetric-function identity and evaluates in the special λ-ring `K₀(X)` of SGA 6 VI Theorem 3.3. Thus `Φ` is the same kind of homomorphism as `τ`. They agree on effective classes by the preceding proof, hence on their entire group completion. This proves (A12.1) for all `ξ`.

## Consequences for the audit

The polynomial `Σ_(α_1,…,α_n)` on scan 028 is exactly `m_ν`, with `ν=(1^α_1⋯n^α_n)`, in every characteristic under the exact-K₀ convention now fixed. This is a proved current-run reformulation using the known ABW integral filtration. The page's direct-summand margin remains refuted by A-007's rank-two example; the equality established here lives in the exact Grothendieck group. The modular relation `ρ_1²=2ρ_2` in exact `R_(F_2)(S_2)` also remains valid: no independence of the `ρ_ν` was used in the proof.

The unsigned-subset counterexample A-001 and the split quadratic counterexample A-003 are unaffected. Their explicit comparison maps still determine the exact targets of the identities.


# A-013. Exact checks of the supplied study's finite-set additions

The assertions below are reported by `SA17_STUDY_cote133_lambda.md` for cote133 scans20–27. Those scans were not part of the supplied transcription set. All public original PDFpages20–27 have now been retrieved and visually read. They confirm the injection/map-power definitions, the deleted coarse induction formula, the quotient-partition count, the representable/map-power definitions, the single-map-power summand assertion, and the distinguished-functor and eventual-equivalence definitions discussed below. These current inspections are recorded separately from the earlier supplied study.

## Injection powers and map powers

For a finite `G`-set `E`, let `τⁿ(E)=Mon([n],E)`, with `G` acting on the target and `S_n` acting by inverse precomposition. For `E⊔F`, the inverse image of `E` under an injection is a subset `A⊂[n]`. Fixing `|A|=i` and choosing the usual ordered representative gives the equivariant bijection

`Mon([n],E⊔F) ≅ ⊔_(i+j=n) Ind_(G×S_i×S_j)^(G×S_n)(Mon([i],E)×Mon([j],F))`.

Explicitly, a coset representative `σ` and the two injections produce the injection whose restrictions to `σ([i])` and its complement are those given injections transported by `σ⁻¹`. Changing `σ` within `S_i×S_j` is precisely the induction balancing relation. The inverse extracts the two restrictions. This proves multiplicativity of the total injection series in the induction product. Its degree-zero term is 1. The degree completion has inverses for every series with that constant term, so the universal group completion extends it to the Burnside group.

For `Tⁿ(E)=Hom([n],E)`, classify each map by the partition of `[n]` into its nonempty fibers. A type `α` has `α_j` blocks of size `j`, with `Σjα_j=n` and `k=Σα_j`. Fix one such partition and a quotient map `p_α:[n]→[k]`. Its stabilizer is

`W_α=∏_j(S_j wr S_(α_j))`,

and its action on blocks is the quotient `W_α→H_α=∏_j S_(α_j)⊂S_k`. The exact component of `Tⁿ(E)` is

`Ind_(W_α)^(S_n) Inf_(H_α)^(W_α) Res_(H_α)^(S_k) Mon([k],E)`.

The actual bijection sends `[σ,i]` to `i∘p_α∘σ⁻¹`; the stabilizer relation is exactly what makes it well-defined, and recovering the kernel partition and the injection on its quotient gives the inverse. The number of source partitions of this type is the index `n!/∏_j(α_j!(j!)^(α_j))`. This proves the study's corrected wreath-stabilizer formula. The deleted induction-from-`S_i` formula already fails for `n=2`: diagonal maps give a trivial `S_2` action, whereas induction from `S_1` gives a free two-point action.

## Representables, limits and composition

Let `FI` be the category of finite sets and injections, and let `h_I(E)=Mon(I,E)`. The category of elements of `h_I` has initial object `(I,id)`, so `h_I` is connected. Fiber partitions give a natural disjoint union

`Hom(J,E)=⊔_(π partition of J) Mon(J/π,E)`.

These are precisely its connected components. In particular, `h_I` is a direct summand of `Hom(I,-)`.

The statement equating **all finite sums of representables** with direct summands of **a single** `Hom(I,-)` is false. It appears in the original PDF page25/site24 itself: after the finite-sum definition, the manuscript says that these are direct summands of `H_I` for `I` of sufficiently large cardinality. The constant functor with two elements is `h_∅⊔h_∅`. At a singleton `E`, every `Hom(I,E)` is a singleton, so it cannot contain that two-element summand, for any `I`. The corrected equality uses finite sums of the `Hom(I,-)`: each representable is a summand of its own map-power functor, and every summand of a finite sum of map powers is a union of their connected representable components. This is a correction to the actual manuscript assertion as well as to the study's summary.

Finite sums of representables are closed under finite limits. The terminal object is `h_∅`. The product `h_I×h_J` is a finite disjoint union of representables, indexed by the equivalence relations on `I⊔J` whose restrictions to both summands are equality; each relation is the overlap pattern of two injections into `E`. Its quotient gives the corresponding representable. To check equalizers, restrict two natural maps to a source component `h_I`. Yoneda identifies each with a choice of target component `h_J` and an injection `J→I`. Different target components have empty equalizer. Within the same component, two distinct injections remain distinct after composition with every injection `I→E`, so their equalizer is empty; identical injections have the whole component as equalizer.

They are closed under composition as well. In `h_I(⊔_a h_(J_a)(E))`, first choose for each element of `I` the component `a` of its image. Then form the finite disjoint union of the corresponding sets `J_a`. The kernel partition of its combined map to `E` records every overlap. Admissible partitions restrict to equality on each `J_a` and make the resulting injections distinct whenever two selected components coincide. Each admissible partition gives exactly the representable of the quotient set. There are finitely many component choices and partitions. Outer finite coproducts preserve this decomposition.

The contracted-product description of the distinguished functors is exact: decompose a finite `S_n`-set `X_n` into its transitive orbits `S_n/H`, and

`Mon([n],E)×_(S_n)(S_n/H) ≅ Mon([n],E)/H`.

A formulation by a finite sum requires finite support in `n`. Arbitrary infinite sequences of finite `X_n` can still give finite values on each finite `E`, but are not all finite sums; the powerset functor is an immediate example.

## Eventual equivalences and injective transition maps

For composable natural transformations that are bijective on all sets beyond specified size thresholds, the set-theoretic two-out-of-three property applies beyond the maximum threshold. Pullbacks of set bijections are bijections, proving stability under base change. Pointwise coproducts and products preserve injective transition maps. Composition also preserves them: the inner functor sends each injection to an injection of finite sets, and the outer functor sends that injection to an injection.

All arguments above have been checked in full. Original PDFpages20–27 were visually inspected in the public-source follow-up. The numerical quotient-partition count is on originalPDFpage23, and the eventual-equivalence definition and its two properties are onPDFpage26; the ledger now uses those precise original page locators.


# Public original-scan follow-up

Run `/root/archive_audit`, GPT-6 Astra Pro, effort not exposed. This follow-up uses the public University of Montpellier archive directly. No Library attachment was read. The supplied inputs remain transcriptions; this file identifies the additional original images actually inspected in this run.

## Access and exact page mapping

The official catalogue is https://grothendieck.umontpellier.fr/archives-grothendieck/ . Its downloaded HTML, `public_scans/catalogue.html`, explicitly supplies viewer paths `../web/viewer.html?file=../4.pdf`, and likewise for 2,12,16,43,79,119,133. The direct PDF URLs are therefore source-provided paths, not guessed endpoints. Web-search PDF opens failed for 4,12,16,133, but ordinary HTTPS access and HTTP byte-range requests succeeded. Headers identify the files as PDFs last modified on 11 May 2017 and advertise byte ranges.

Complete cote4 was downloaded to `public_scans/4.pdf` (4,884,318 bytes;12 PDF pages). The catalogue's count11 refers to numbered archive pages; the file includes an opening page. The supplied scan007 is PDF page7, whose displayed archive/site number is6. This page mapping was verified visually, not inferred only from arithmetic.

Targeted byte-range page extraction succeeded for cotes2,12,16,79,119,133. Complete files4,12,16,43,79,89,119,133 have also been downloaded. `extract_public_ranges.py` preserves the actual selected pages in standalone PDFs; no content is regenerated. Download attempts are recorded in `public_scans/ACCESS_ATTEMPTS.jsonl`. An HTTP success is not itself an image-inspection claim. Every one of the thirteen supplied target leaves has now been viewed as an original public scan.

## Cote2, supplied scan017: the extension convention verified

Visually inspected originalPDFpages16–18, including targetpage17/site16, rendered at150–160dpi. Page15 is an unrelated printed verso and was recognized as such. Page16/site15 defines `A(X,G)` as the category of modules on the ringed topos with a group action, then explicitly calls `u_*` extension and `u*` restriction. This confirms the induction/extension convention used by A-009, rather than leaving its adjoint choice to an inference from the symbol. The target's tensor and projection formulas, external product, diagonal pullback and transitivity match the supplied transcription. Page18 continues with the induction product along `S_p×S_q→S_(p+q)`.

## Cote43, supplied scan037: the Witt-series leaf checked

Visually inspected originalPDFpage37/site36 at150dpi. The inserted affine qualification, formal-series addition by multiplication, line convolution, coefficient Frobenius, substitution Verschiebung, `FV=VF=p`, twisted-line formula and final line value of `ψ` match the supplied transcription. The overwritten input letter of the first displayed functor formula remains a literal ink issue; the surrounding sentence explicitly varies the ring `A`. A-008 gives the actual isomorphism to the standard big-Witt convention, and A-018 proves the final additive affine-scheme uniqueness claim.

## Cote4, supplied scan007: context recovered, assumption isolated

Visually inspected original PDF pages2–9, rendered with Poppler at110 dpi. Files are `public_scans/4-p002.png` through `4-p009.png`.

- PDFp3/sitep2, §8.1: `X` is smooth and proper over a perfect field `k` of characteristic `p>0`; `W` is its Witt ring; `H(X)` is crystalline cohomology. The page displays the derived crystalline-to-de-Rham base change and the universal-coefficient sequence. It defines `E(Y)=coker(H^(n−1)(X)→H^(n−1)(Y))` for a hyperplane section of a connected, projective `n`-dimensional `X`.
- PDFp4/sitep3, §8.3: the argument first invokes integral Lefschetz in the complex/ell-adic situation, then **expressly admits** the corresponding crystalline assertions. This is where torsion-freeness of `E(Y)` and the torsion restriction isomorphism enter. The underlying missing input is now precisely located, rather than described merely as missing notation.
- PDFp5/sitep4, §8.4: `V_ss` is the maximal Frobenius-stable subspace on which the semilinear Frobenius is bijective, equivalently the stable image of its iterates; Frobenius on the quotient is nilpotent. This is a Fitting stable-part construction. For example, an invertible unipotent Jordan block over `F_p` has its whole space as this stable part, explicitly showing what the source terminology means.
- PDFp5/sitep4, §8.4.2: the stable semilinear category is related to finite-dimensional `F_p` Galois representations. This supplies the definition missing from the isolated target page.
- PDFp6/sitep5, Lemma8.4.3: the augmentation from de-Rham cohomology to coherent cohomology induces an isomorphism on stable parts. The source gives a Hodge-to-de-Rham spectral-sequence argument. An elementary factorization proof is supplied below.
- PDFp6/sitep5, the displayed “Théorème”8.5: the text again explicitly admits the preceding crystalline ingredients. This remains an input gate for the geometric exact sequence; it is not promoted here to an unconditional theorem.
- PDFp7/sitep6: the supplied transcription's p-torsion replacement in (8.5.1), the deleted cup-product passage, the marginal `Faux`, and the algebraicity qualification on `Λ` are all visible. The parenthetical comparison with ell-adic eigenvalues retains that stated qualification. The text inserts the inverse of the Galois Frobenius generator, consistent with the transcription.
- PDFp8/sitep7, Remark8.5.7: injectivity of `v` is itself stated as an expectation, followed by a sufficient large-degree coherent-vanishing argument. This further confirms that no universal injectivity result should be extracted from scan007 alone.
- PDFp9/sitep8: the following discussion turns to families of hypersurfaces, stable ranks and generic constancy. No explicit plethysm multiplicity or Reynolds-projector map appears in these inspected pages.

### A-014: the stable-part assertions that can be proved directly

Let `V` be a finite-dimensional space over a perfect field of characteristic `p`, with a Frobenius-semilinear endomorphism `F`. The descending images `F^r(V)` stabilize by finite dimension; write the stabilized image as `V_st`. Frobenius is bijective there and nilpotent on `V/V_st`. This decomposition is functorial. It is exact on equivariant short exact sequences: a sufficiently large common iterate gives surjectivity on stable images; the intersection of the stable image with an invariant subspace has bijective Frobenius by finite dimension and is exactly that subspace's own stable image.

For the algebraic de-Rham complex, let `π:Ω_X^•→O_X` be the augmentation, and let `ι_F:O_X→Ω_X^•` send a function to its pth power in degree zero. This is a semilinear chain map because the derivative of a pth power is zero. Their composites are the Frobenius maps on the two complexes. On hypercohomology stable parts, `π` is therefore invertible, with the explicitly typed inverse `ι_F∘F_O^(-1)` from coherent cohomology to de-Rham cohomology. This proves the source's Lemma8.4.3 directly in the finite-dimensional situation without requiring Hodge-to-de-Rham degeneration.

For a finite free `W(F_q)`-module `M` with Frobenius-semilinear `F`, write `q=p^f`. The iterate `T=F^f` is linear. Its characteristic polynomial is integral. Its reduction factors as a power of the variable times a polynomial nonzero at zero; the latter degree equals the dimension of the Fitting stable part of `M/pM`. Hensel separation of these two relatively prime factors shows that exactly that many characteristic roots of `T` are p-adic units, counted with algebraic multiplicity, and their reductions are the nonzero roots of the reduced characteristic polynomial. This proves the precise lattice/Frobenius linear algebra underlying the target page's count. Applying it to the proposed geometric `E(Y)` still requires the freeness and Frobenius-stability input identified in §8.3; the ell-adic comparison additionally retains the source's algebraicity input.

## Cote12, supplied scan041: definitions recovered, projected theory retained

Visually inspected original PDFpages31–43, with a260dpi detail of targetpage41. The foliation is again one less than the PDFpage number. These are handwritten pages of the motive programme, not a previously missing independent proof of the target's promised identity.

- PDFp31/site30, §9, explicitly introduces the filtration by weights. PDFpp32–34 display tensor-product compatibility and Tate twists shifting weight by two.
- PDFpp36–37/site35–36, §10, introduce the effective and Tate-inverted categories and their Grothendieck rings `M⁺(X)` and `M(X)`. PDFp37 explicitly defines `ξ` as the class of the Tate object written `Q_X(−1)` and gives `M(X)=M⁺(X)[1/ξ]`. The page states the tensor-category and finite-length/simple-object framework being used.
- PDFpp38–40/site37–39 define the simple-object label sets `Σ⁺(X)`, their filtration/weight pieces, and the primitive labels `σ_i(X)` obtained by removing positive Tate shifts of lower-weight labels. They express the additive Grothendieck groups as free abelian groups on these labels. Thus the `σ_i` in the target are now identified; they are not left as undefined symbols.
- PDFp41/site40 preserves the progression from a twisted-duality involution to the claim that it will be the identity. The sentence expressly says that the identity will result from the projected theory. The words “théorie projetée” are readable in the detail crop. The coefficient symbol before `(-i)` has been overwritten and is not clean enough to settle by letter shape alone; its Tate-object meaning is supplied by the neighboring definitions. The page's final finite-group sentence is a proposed method for the lambda operations.
- PDFp42/site41 begins §11 on dimensional type/coniveau with the coniveau spectral sequence. PDFp43/site42 includes a crossed-out discussion of geometric interpretation and the Tate conjecture, then begins §12 on the initial ring of varieties. These following pages do not supply the promised proof of the twisted-duality identity.

The remaining input is therefore precise: a construction of the stated motivic category together with a morphism realizing the claimed self-duality of every primitive simple class, compatibly with the Tate twist and the chosen equivalence on correspondences. The inspected pages announce this as part of the projected theory. Merely manipulating the involution does not establish that it fixes every simple class. The actual symmetric-group/Schur maps needed for the lambda sentence are supplied independently in A-007, A-009 and A-012.

## Cote16, supplied scan038: primitive projectors and concrete failures

Original PDFpages33,34,36,38 were visually read, including240dpi top and bottom details of the target. The original full PDF was downloaded. Pages35 and37 are reused printed versos, recognized as such rather than mistaken for continuation of the handwritten argument.

PDFp33/site32 supplies the primitive-projector convention and the coefficient-free Lefschetz lowering operator; the `p_i` are the primitive bottom/top pieces, rather than the projectors onto whole cohomological degrees. PDFp34/site33 supplies the hyperplane restriction strings and the extra middle piece `E`. PDFp36/site35 supplies `(α)` and the pushforward action on the strings. Thus the earlier missing-definition gate has been attacked and closed at the linear-algebra level.

`LEFSCHETZ_FRAGMENT.md` (A-016) gives the full typed model, its restriction and pushforward maps, and verifies the repaired identities summand by summand. The manuscript target still contains type/index problems; these are not silently edited into correct statements. In particular, the last projected equality fails even after replacing the misplaced pullback by pushforward: for `X=P¹`, `Y=point`, one side sends `1` to `1` and the other sends it to `0`. The transcribed kernel bounds also admit the explicit `P¹/point` and `P²/P¹` counterexamples in A-016. Algebraicity of the resulting cohomological operators is a further geometric issue and is not inferred from the string calculation.

## Cote79, supplied scan051: determinant model and the remaining reconstruction question

Visually inspected original PDFpages46–51. PDFp47/site46, formulas(114)–(117), defines a rank-two free module over `Z/n`, its determinant-generator torsor modulo sign, the scalar group `(Z/n)×/{±1}`, and the unimodular-vector set modulo sign. PDFp48/site47, formulas(118)–(123), defines the wedge-type map and the edge/face sets. PDFpp49–50/site48–49 supplies `A`, `τ`, and the missing relation(125′).

These definitions permit a complete direct proof of targetformula(127). `SCALAR_TRIANGULATIONS.md` (A-017) defines all maps, proves `τ(T_λs,T_λt)=λ²τ(s,t)`, gives the resulting automorphism `(T_λ,λ²)` of the family, and proves recovery of the scalar action from the one-argument relation. The square is explicitly induced by the determinant map `Λ²(a·id)=a²·id`; no interpretation of that scalar square as an unspecified lambda operation is needed.

The final question of scan051 remains exactly the reconstruction from one abstract, unlabeled triangulation `P₀`. The concrete module construction and its compatibility proof do not themselves recover that module and the whole family from one member. The vertex-action embedding of `Aut(P₀)` is directly verified in A-017.

## Cote89, supplied scan018: the omitted equation supplied next door

Visually inspected original PDFpages16–18. PDFp16/site15 defines `V` as a free rank-two module over a commutative ring `Λ`, its unimodular vectors, free direct-summand lines, their generator torsors, and the determinant-generator torsor. Disjointness is the direct-sum condition. PDFp17/site16, formulas(7)–(8), explicitly states the wedge equality and its equivalent equation `u+v+w=0`. This supplies the missing right-hand side on targetp18 from the manuscript itself. The target's concluding reconstruction is expressly discussed over a field.

The basis computation of A-011 proves the wedge equivalence over the ring as well: `u,v` form a basis by the disjointness condition, and equality of multiples of their determinant generator forces the coefficients of `w` to be `−1,−1`. The reconstruction of all addition in the field case is already proved in A-011. No arbitrary-ring reconstruction has been inferred from the shorter field argument.

## Cote119, supplied scan217: document and wording identified

Visually inspected original PDFpages215–217. The title page215/site214 identifies the text as the1972 **Esquisse thématique des principaux travaux mathématiques de A. Grothendieck**. Page216 is typed reportpage2, on homological algebra; targetpage217/site216 is typed reportpage3, beginning the topology section. Its words about lambda operations and their links with symmetric-group operations match the supplied transcription. The paragraph on topoi and ell-adic cohomology is historical testimony in this report, with its sentence continuing beyond the leaf. It does not state another precise coefficient theorem. The mathematical maps supporting the lambda/symmetric-group link are the explicit maps of A-007, A-009 and A-012.

## Cote133: literal checks and the supplied study discrepancy

Visually inspected original PDFpages4,6,8,9 and every page19–29; pages6 and8 also at260dpi details and page19 at300dpi. Newly read pages4,20–23,26–27,29 were rendered at140dpi.

- Page6/site5 confirms the literal group completion of the orthogonal-sum monoid, its pre-lambda assertion, the even-rank observation, and the two special-lambda questions. The displayed product polynomial ends at the handwritten `i−1` exponent. That literal truncation is mathematically false, as separately recorded in A-Q063. A-015 now independently refutes the full iterate identity for the literal split ring, as A-003 already refuted the product identity.
- Page8/site7 supports the handwritten name **Lazard**, rather than the alternative Laborde in the supplied transcription. The hyperbolic relation and its warning about a classifying topos are visible. A-004b gives the precise characteristic-two counterexample.
- Page9/site8 confirms that the hyperbolic-class vanishing and Witt-factorization passage is crossed out. A-006 treats the surviving characteristic-class claims and gives the counterexample to that deleted passage.
- Page19/site18 visibly gives unsigned subsets and symmetric powers at the top, the linearization arrow, the two degree-two formulas, and the boxed `2λ²(E)+E=E²`. This confirms that the supplied study's claimed equivariant check cannot be repaired by moving the formula to a different manuscript page. The free two-point `C₂`-set of A-001 refutes the boxed equivariant equality. Its cardinality image is the valid integer equality written underneath. The ambiguous overwritten sign in the separate geometric-series denominator is retained as a transcription issue; the mathematical inverse-series formula has the minus sign.
- Page24/site23 defines the category of finite sets with injections, `h_I=Mon(I,−)` and `H_I=Hom(I,−)`. Page25/site24 itself asserts the equivalence between finite sums of `h_I` and summands of one `H_I` for sufficiently large `I`. A-013's constant-two counterexample therefore refutes a manuscript assertion, as well as its repetition in the study. At a singleton input every `H_I` has one element.
- Page28/site27 confirms the tensor-power/Young-induction expansion and its monomial-symmetric coefficient definition. A-012 proves the identity integrally in exact K₀ for arbitrary commutatively ringed topoi, using the universal Cauchy filtration and its actual multidegree maps. The direct-summand positivity reading is separately refuted in A-007; the global positive-count constructions G-009–G-012 supply actual invariant-algebra/module presentations and terminating finite counts.
- Page4/site3 contains the actual `c₁ ?` question, the hyperbolic line pair and its first Stiefel–Whitney class. A-022 proves the line-bundle answer by an explicit nonisotropic-line pullback and the Kummer/Bockstein identity. The higher-rank hyperbolic formula is located and checked in EKVProposition5.5, pp183–184, with the source's regularity assumption recorded. A-022 then proves the full formula over every `Z[1/2]`-scheme by iterating the actual projector `z↦v f(z)/f(v)` on nonisotropic-line covers and descending through their injective cohomology pullbacks.
- Pages20–21/site19–20 define injection powers and prove their disjoint-union induction product. Page22/site21 defines map powers and crosses out the induction-from-`S_i` formula. Page23/site22 writes the quotient-partition count with its block factorials. A-013 gives the actual wreath-stabilizer maps and a two-element counterexample to the deleted formula. Page26/site25 gives distinguished functors and eventual equivalences; page27/site26 defines the category with injective transition maps and its sum, product and composition.
- Page29/site28 states the coefficient corollary and asks for all rings giving the polynomial induction ring, explicitly including local rings or rings with `K(k)≅Z`. A-020 proves the study's modular rank count from the checked James theorem. A-021 resolves the `Z_p`-lattice subquestion and extends it to all characteristic-zero DVRs by the explicit rationalization map. A-023 gives a characteristic-zero local counterexample with a determinant obstruction. These two results sharpen, rather than erase, the broader coefficient-ring classification question.

## Current assertion register

`ARCHIVE_QUESTIONS.tsv` has123 separate source-assertion rows covering all thirteen supplied archive leaves, plus the relevant lambda/finite-set additions in the supplied study:80proved,25refuted,18precise gates. Each row records source kind, cote/page, status, exact reason, and the current proof ID. A-012 closes the arbitrary-characteristic exact-K₀ tensor-power identity. A-013 records the finite-set checks and the single-map-power summand counterexample, now verified against the manuscript. A-014–A-017 close the specified Frobenius, Lefschetz and scalar-action calculations, with exact remaining geometric/reconstruction gates. A-018 closes uniqueness of the additive scheme morphism on cote43. A-019 closes field hyperbolic cancellation in every characteristic; A-020–A-023 supply the modular rank, DVR polynomial ring, characteristic-class formula and characteristic-zero local counterexample. Image-inspection fields are updated only after a page is actually viewed.


# A-015. The separate exterior-iterate question on scan133/006 is refuted

This supplements A-003's product counterexample. Use exactly its field, group, quadratic-form convention and split Green ring:

`k=algebraic closure of F₃`, `G=C₃`, `x=[J₃]`, `y=[J₂]`,

`x²=3x`, `xy=2x`, `y²=x+1`,

`λ_t(x)=1+xt+xt²+t³`, `λ_t(y)=1+yt+t²`.

The symmetric object `X` is the permutation module `J₃` with its invariant dot-product form; `H(J₂)` is hyperbolic. Take the actual symmetric object

`A=X⊥H(J₂)`.

Its underlying class is `a=x+2y`, of rank seven. Forgetting symmetric forms commutes with every exterior operation.

## The exact universal polynomial

The special-lambda iterate polynomial for `λ³(λ² a)` is

`Q_(3,2)=e₁²e₄−2e₂e₄−e₁e₅+e₆+e₃²`,

where `e_i=λⁱ(a)`. Here is a finite universal verification independent of any Green-ring example. In six indeterminates, `e₃[e₂]` is the sum of products attached to three distinct edges of the complete graph on those six indices. The possible degree patterns and coefficients of their monomial symmetric functions are

| Pattern | Coefficient |
|---|---:|
| `(3,1,1,1)` |1|
| `(2,2,1,1)` |2|
| `(2,2,2)` |1|
| `(2,1,1,1,1)` |6|
| `(1,1,1,1,1,1)` |15|

They correspond respectively to a star, a path, a triangle, an adjacent pair plus a disjoint edge, and a matching. Expanding the displayed elementary polynomial gives these same five coefficients. `check_iterate_defect.py` verifies the equality of every monomial coefficient using integer arithmetic. Specialization to six variables is injective in symmetric-function degree six, since every partition of six has at most six parts. Thus this is the universal polynomial identity, not only a test at one numerical alphabet.

## Evaluation in the actual split Green ring

Multiplication of the exterior series gives

`λ_t(a)=(1+xt+xt²+t³)(1+yt+t²)²`,

whose coefficients from degree zero through seven are

`1, x+2y, 6x+3, 10x+2y+1, 10x+2y+1, 6x+3, x+2y, 1`.

In particular, `λ²(a)=6x+3`. The degree-three coefficient of

`(1+xt+xt²+t³)⁶(1+t)³`

is `441x+7`: the degree-three coefficient of the first factor is `270x+6`, its degree-two coefficient is `51x`, and its degree-one coefficient is `6x`, giving `(270x+6)+3(51x)+3(6x)+1`.

The universal polynomial above, evaluated at the seven displayed exterior coefficients, is instead

`445x−4y+3`.

Consequently

`λ³(λ²(a))−Q_(3,2)(a)=4+4y−4x=−4(x−y−1)`.

The split Green group is free abelian on `1,y,x`, so this difference is nonzero. Because the forgetful map commutes with every exterior power, the corresponding iterate identity also fails on the actual symmetric object `A` in the literal split quadratic Grothendieck ring of `BC₃`. The coefficients are integers in that group, not scalars reduced modulo three. The exact quotient sends `x→3`, `y→2` and kills this difference, just as it kills the product defect of A-003.

Thus both universal questions on scan133/006 have separate explicit negative answers for its stated split ring: A-003 for multiplication, and A-015 for iterated exterior powers. The modern theorem for the exact/metabolic quotient remains compatible with both counterexamples through the explicitly given quotient map.


# A-016. Exact operators and a counterexample on cote16, scan038

The original Montpellier PDF is `public_scans/16.pdf` (21,774,525 bytes). The target is PDFpage38/sitepage37. The current run visually inspected PDFpages33,34,36,38, including a240-dpi crop of the target's final formulas. PDFpage33/site32 supplies the previously missing definitions; PDFpage36/site35 supplies the identification `(α)` and the pushforward description. Unrelated printed versos were recognized as such and are not used in the argument.

## Definitions recovered from the original

PDFp33 calls `X` a smooth connected projective variety of dimension `n`, polarized by a class in `H²(X)`, and `Y` a smooth hyperplane section. The map `φ:Y→X` is the immersion. Its `p_i^X` are the projections onto the primitive **bottom and top pieces**, indexed from0 through2n. They are not the projectors onto whole cohomological degrees. The actual operator convention is fixed by the source equations

`Λ_X L_X=1−Σ_(n≤i≤2n)p_i^X`,

`L_X Λ_X=1−Σ_(0≤i≤n)p_i^X`.

Thus `Λ` removes one `L` from a primitive string with coefficient one. PDFp34/site33 identifies restriction with truncation of each string and defines the extra middle piece `E^(n−1)`. PDFp36/site35 writes `(α)` and identifies `φ_*` with multiplication by `L_X` on the shared string pieces, zero on `E`.

The following explicit construction verifies the resulting operator statements and makes their maps unambiguous. It also supplies a precise reading of the source's decompositions. It does not assert algebraicity of any of these cohomological projectors or of `Λ`.

## The full explicit string model

For a positive integer `n`, choose finite-dimensional rational vector spaces `P_0,…,P_n,E`. Form

`V_X=⊕_(0≤i≤n) ⊕_(0≤j≤n−i) P_i[j]`,

`V_Y=(⊕_(0≤i≤n−1) ⊕_(0≤j≤n−1−i) P_i[j]) ⊕ E`.

Place `P_i[j]` in degree `i+2j`, and `E` in degree `n−1`. On each string define `L` to move `j` to `j+1`, and `Λ` to move `j` to `j−1`, both zero at the relevant endpoint; both operators kill `E`. Define `r:V_X→V_Y` to be the identity on the shared pieces and zero on the last term `P_i[n−i]` of every `X` string. Define `g:V_Y→V_X` by `g(P_i[j])=P_i[j+1]`, and `g(E)=0`.

The bottom projector `p_X^i`, `0≤i≤n`, projects onto `P_i[0]`. For `n<i≤2n`, the top projector `p_X^i` projects onto `P_(2n−i)[i−n]`. The analogous definitions for `Y` use dimension `n−1`; its middle projector also contains `E`. These are explicit direct-sum projectors. In this model `g r=L_X` and `r g=L_Y`, checked on every displayed summand, exactly as on PDFp36.

The kernel descriptions are

`ker L_Y=(⊕_(i=0)^(n−1) P_i[n−1−i])⊕E`,

`ker Λ_Y=(⊕_(i=0)^(n−1) P_i[0])⊕E`.

The operator `Λ_Y` is injective on all remaining shared string pieces. The first kernel is related to the high primitive pieces of `X` by the actual isomorphism

`rΛ_X : ⊕_(j=n+1)^(2n) im(p_X^j) → ⊕_(i=0)^(n−1) P_i[n−1−i]`.

Consequently a display identifying these two spaces must use this degree-minus-two map, rather than a literal equality of subspaces of one graded object.

## Corrected operator identities and their complete proof

Put `Q_X^top=Σ_(j=n+1)^(2n)p_X^j`, `Q_Y^top=Σ_(j=n−1)^(2n−2)p_Y^j`, `Q_X^bottom=Σ_(i=0)^(n−1)p_X^i`, and `Q_Y^bottom=Σ_(i=0)^(n−1)p_Y^i`. Then the concrete maps satisfy

`Λ_Y r=rΛ_X(1−Q_X^top)=(1−Q_Y^top)rΛ_X`,

`gΛ_Y=(1−Q_X^bottom)Λ_Xg=Λ_Xg(1−Q_Y^bottom)`.

For the first line, a nonfinal shared `X` term is lowered identically on both sides. A final `X` term is killed by `r`, while `rΛ_X` would send it to the final `Y` term; either displayed top projector removes exactly this contribution. The isolated middle `P_n[0]` is already killed by both lowering and restriction. This checks every summand of `V_X`.

For the second line, on a `Y` term with `j≥1`, both composites land in `P_i[j]⊂V_X`. On a `Y` bottom term, `gΛ_Y` is zero but `Λ_Xg` returns the corresponding `X` bottom; either bottom projector removes exactly this contribution. Every composite kills `E`. This checks every summand of `V_Y`.

The same basis check gives, for every nonnegative integer `m`,

`Λ_Y^m r=rΛ_X^m(1−Q_X^top)`.

It also gives the correctly typed projector identities

`rΛ_X p_X^j=p_Y^(j−2) rΛ_X` for `n+1≤j≤2n`,

`p_X^i Λ_Xg=Λ_Xg p_Y^i` for `0≤i≤n−1`.

The first carries the final term of an `X` string onto the final term of its truncated `Y` string. The second selects exactly its bottom term. These descriptions prove the identities on every summand and give the exact relation between the source's indices.

## The target's final chain fails on an actual hyperplane section

The supplied target's final chain uses `φ*` in positions whose source must be `H(Y)`; the original crop retains the problematic star placement. Even after the natural type repair replacing those two occurrences by `g=φ_*`, its additional equality

`p_X^i Λ_X φ_* = p_X^i φ_* Λ_Y`

is false. Take `X=P¹_C`, `Y` one point, `n=1`, `i=0`. Write `h` for the hyperplane class, so `H*(X,Q)=Q[h]/(h²)`, `φ_*(1)=h`, `Λ_X(h)=1`, and `p_X^0(1)=1`. Since `Y` has only degree-zero cohomology, `Λ_Y=0`. Thus the two displayed maps send `1` to `1` and `0` respectively. In the full string model the right side is always zero, while the left side identifies the selected bottom piece. This is a complete concrete-map counterexample, not only a typing objection.

Two other bounds in the supplied transcription can be settled in the same elementary models. The expression for `ker L_Y` must include the middle projector `p_Y^(n−1)`; the transcribed range starting at `n` fails already for the same `P¹/point` pair. The transcribed bound `0≤i≤n+1` for `ker Λ_Y` includes unwanted top pieces: for `X=P²`, `Y=P¹`, it includes `h∈H²(Y)`, whereas `Λ_Y(h)=1`. The exact correct range is `0≤i≤n−1`. The corresponding image readings remain distinguished from these mathematical repairs; no uncertain handwritten sign has been silently normalized.

The source's first corrected pullback line also prints `p_X` next to `id_Y`. The explicit model above proves its well-typed version with `p_Y`. These corrections and counterexamples close the operator-level questions in the supplied fragment. They do not supply the algebraicity assertions about Lefschetz projectors that the neighboring archive discussions treat separately.


# A-017. Cote 79: the exact scalar and determinant maps

The original public PDF pages47–51, particularly (114)–(125′), supply the definitions missing from supplied scan051. Write `R=Z/nZ`, `n≥2`, and let `M` be free of rank two over `R`. Let `M_prim` be its unimodular vectors, `D=Λ²_R M`, and `D_gen` the generators of this rank-one module. The source writes stars for these generator loci. Its objects are

`U=R×/{±1}`, `S=M_prim/{±1}`, `Π=D_gen/{±1}`, `L′=D/{±1}`.

Here `Π` is a `U`-torsor. The map

`β:S×S→L′`, `([u],[v])↦[u∧v]`

is well-defined. Changing either lift changes the wedge by a sign, and interchanging the lifts also changes it by a sign. Thus β is symmetric on the quotient, despite being induced by the alternating bilinear wedge map before quotienting. Define `A⊂P₂(S)` by `β(s,t)∈Π`, and define `τ:A→Π` by this value. A unit wedge already ensures `s≠t`.

For `i∈Π`, set `A_i=τ⁻¹(i)` and let `F_i` be the three-element subsets all of whose two-element subsets belong to `A_i`. These are the precise edge and face constructions in (120)–(121), defining the source's family `Σ(i)` on its vertex set. The statements that each is a particular connected regular surface and that one of them reconstructs all the rest are additional assertions; the maps below do not assume a classification of those surfaces.

## The action and its square on determinant types

For `λ=[a]∈U`, define `T_λ([u])=[au]`. This is independent of both representatives, has inverse `T_(λ⁻¹)`, and satisfies `T_λT_μ=T_(λμ)` and `T_1=id`. Bilinearity of the actual wedge map gives

`β(s,T_λt)=λβ(s,t)`,

and hence

`β(T_λs,T_λt)=λ²β(s,t)`.

Multiplication by units preserves generators of `D`, so `T_λ` preserves `A` and

`τ({T_λs,T_λt})=λ²τ({s,t})`.

Consequently the pair of maps `(T_λ, i↦λ²i)` is an automorphism of `(S,Π,A,τ)` and transports the actual simplicial structure `Σ(i)` to `Σ(λ²i)`. Faces are carried to faces because their three edge types are carried to the common new type. This proves the target page's formula (127), with every source and target specified. It also identifies the square in that formula by the explicit determinant map: `Λ²(a·id_M)=a²·id_D`.

## Recovery of the scalar action from the one-argument relation

The full wedge relation (125) determines each `T_λ` uniquely. Indeed, primitive `u` extends to a basis `(u,w)`. For `v=bu+cw`, equality of the classes of `s∧u` and `s∧v` for all primitive `s` first gives `c=0` by taking `s=u`, then `b=±1` by taking `s=w`. Therefore the map `S→(L′)^S` given by all wedge values is injective.

The restricted relation (125′) using only pairs whose wedge is a unit also determines each such permutation for every `n≠4`. To prove this, rescale and change the sign of `v` so that comparison with `s=w` gives `v=u+cw`. For every `t∈R`, the vector `w+tu` is primitive and has unit wedge with `u`; comparison gives `1−tc∈{1,−1}`. The additive subgroup `cR` is therefore contained in `{0,2}`. A nonzero such subgroup forces `2` to have additive order two, hence `n=4`. Thus `c=0` for `n≠4`. For `n=4`, the acting group `U` is trivial, so its group action is uniquely the identity. This proves the unique compatible `U` action in the actual rank-two module model for all `n≥2`.

The exception also explains why a bare point-separation assertion needs care. In `R=Z/4`, the distinct classes of `(1,0)` and `(1,2)` have exactly the same unit-wedge tests and unit-wedge types: the sole type is the class of `±1`, and both tests say that the second coordinate of the testing vector is odd. The full wedge map separates them by testing `(1,0)`, whose two wedge values are `0` and `2`.

Conversely, every `i∈Π` is the wedge type of a basis pair. The expression `τ({s,T_λt})` for such a pair of type `i` equals `λi`, independently of the chosen pair. It therefore recovers the torsor scalar action from the constructed action on vertices. This supplies actual inverse recovery maps in this module model, rather than an unproved comparison of structures.

## What remains a source question

The last paragraph of scan051 asks how a single abstract triangulation `P₀=(S,A₀,F₀)` determines every other `Σ(i)` and the `U` action. The preceding concrete construction starts with the rank-two module, its determinant line, and its scalar action; it does not reconstruct them from one unlabeled complex. The inspected pages do not provide that reconstruction. The displayed embedding `Aut(P₀)→Sym(S)` is injective directly: an automorphism is the vertex permutation preserving the specified edge and face subsets, so its action on vertices determines it.

The entire proof above was checked by expanding the wedge map on a basis, including the exceptional `n=4` separation calculation. No broader reconstruction theorem is asserted.


# A-018. The additive Witt-series morphism is determined by line values

This closes the remaining uniqueness assertion on cote43/scan037, in the precise category written there: morphisms of affine group schemes over `Z`. Let `S∞=Spec Z[a₁,a₂,…]` represent the group `1+tA[[t]]` whose group operation is ordinary multiplication of series. Let `G=Spec B` be an affine group scheme, and let `f,g:S∞→G` be additive group-scheme morphisms agreeing on the map

`A¹→S∞`, `x↦1+xt`.

We prove `f=g` by their actual coordinate maps. For each `b∈B`, the difference `f*(b)−g*(b)` is a polynomial `P(a₁,…,a_N)` in finitely many coordinates. Over the polynomial ring `Z[x₁,…,x_N]`, form

`u(t)=∏_(j=1)^N(1+x_jt)`.

Additivity and agreement on lines give `f(u)=g(u)`. Thus

`P(e₁(x),…,e_N(x))=0`.

The map `Z[a₁,…,a_N]→Z[x₁,…,x_N]`, `a_j↦e_j(x)`, is injective. One elementary proof uses lexicographic leading terms: the leading monomial of `e₁^(r₁)…e_N^(r_N)` has exponent vector `(r₁+…+r_N,r₂+…+r_N,…,r_N)`. These vectors are distinct for distinct nonnegative tuples `(r₁,…,r_N)`, and each leading coefficient is one, so a nonzero integral polynomial cannot map to zero. Hence `P=0`. This holds for every `b`, proving equality of the scheme morphisms.

Apply this to the affine p-typical Witt group scheme `G=W_p`. The established big-to-p-typical ring morphism, in the source convention `α(f)=1/f(−t)`, sends `1+at` to the Teichmüller vector `(a,0,0,…)`. The preceding argument proves that these line values uniquely determine its additive scheme morphism, over every base characteristic. It uses finite dependence of a coordinate polynomial; it introduces no unsupported continuity assumption and does not identify arbitrary abstract homomorphisms of groups of series with scheme morphisms.

The full proof, including the coordinate variance, finite-variable reduction and leading-monomial injection, was checked in this run.


# A-019. The field cancellation input on cote133/008

The original target's field cancellation step is valid for the specified strictly nondegenerate quadratic forms, including characteristic two. The exact primary locator is Elman–Karpenko–Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, §8, Theorem8.4, p48; its proof uses Theorem8.3 and Lemma8.2, pp47–48. The author-hosted book is https://www.math.ucla.edu/~merkurev/Book/Kniga-final/Kniga.pdf .

In the source's notation, put `V=q⊥(−q′)`. An isometry

`V⊥H(F) ≅ H(E)`

over a field has `dim E≥dim F`. Choose a vector space `G` of dimension `dim E−dim F`, and identify `H(E)≅H(G)⊥H(F)`. The polar form of `H(F)` is nondegenerate in every characteristic. The cited cancellation theorem therefore gives the actual isometry `V≅H(G)`, removing the stabilizer.

The complete proof of Lemma8.2 and Theorems8.3–8.4 was read and checked in this run, including the reflection calculations, the finite-field exception `F₂`, and the restriction of an extended isometry to orthogonal complements. Its characteristic-two hypothesis is nondegeneracy of the polar form of the cancelled summand, which `H(F)` satisfies.


# A-020–A-021. The modular rank and the mixed-characteristic lattice ring

These results answer two separate questions in the supplied study of cote133, scans28–29. Every Grothendieck group below uses all short exact sequences in the specified category. The maps are explicit; no assertion about the split group of isomorphism classes is substituted for this exact Grothendieck group.

## A-020. The rank over the prime field

For a prime `p`, let `G₀(F_p[S_n])` be the Grothendieck group of finite-dimensional modules. The composition-factor map identifies this group with the free abelian group on the simple modules: Jordan–Hölder makes the map well defined, and sending a simple label to its module class is its inverse.

James, *The Representation Theory of the Symmetric Groups*, Lecture Notes in Mathematics682 (1978), Theorem11.5, printedp40, classifies these simples by the p-regular partitions of `n`. Here p-regular means that no part occurs p or more times. For `n=p`, the only excluded partition is `(1^p)`. Hence

`rank_Z G₀(F_p[S_p]) = number_of_partitions(p) − 1`.

The source's alternative count by p-regular conjugacy classes gives the same answer: among cycle partitions of `p`, only `(p)` is excluded. James Lemma10.2, p36, proves the equality of these two counts by expanding `∏(1−t^(mp))/(1−t^m)` in the two ways. These are different label sets, linked by that coefficient identity; their equal cardinalities have not been inferred by identifying their individual partitions.

## A-021. Rationalization for lattices over a characteristic-zero DVR

Let `O` be a discrete valuation ring of characteristic zero, with uniformizer `π`, fraction field `K`, residue field `k`, and `G=S_n`. Write `L_O(G)` for the exact category of finitely generated `O[G]`-modules whose underlying `O`-module is free. Its admissible sequences are the short exact `O[G]`-sequences with all three terms in this category. Rationalization is the exact functor

`L_O(G) → Rep_K(G),    M ↦ K⊗_O M`.

It induces an isomorphism

`r_n : K₀(L_O(S_n)) → R_K(S_n)`.

Here is a direct proof, including the boundary construction that supplies injectivity.

### The torsion boundary

For a finite `O`-torsion `O[G]`-module `T`, choose a surjection `P→T` with `P` finite free over `O[G]`. Its kernel `L` is finite free over the discrete valuation ring `O`. Define

`δ(T)=[P]−[L] ∈ K₀(L_O(G))`.

This class is independent of the chosen presentation. Indeed, for presentations `P→T` and `P′→T`, their fibre product `Q=P×_T P′` lies in the lattice category. The exact sequences `0→L→Q→P′→0` and `0→L′→Q→P→0` give `[P]−[L]=[P′]−[L′]`. Both sequences split over `O[G]` because their quotients are free over `O[G]`, although their ordinary exactness already suffices for the displayed equality.

The assignment is additive on a torsion exact sequence `0→T₁→T₂→T₃→0`. Choose free presentations `P_i→T_i` for `i=1,3`, lift `P₃→T₃` to `T₂`, and combine this lift with `P₁→T₁→T₂`. The resulting surjection `P₁⊕P₃→T₂` has a kernel `L₂` in an exact sequence `0→L₁→L₂→L₃→0`. This gives `δ(T₂)=δ(T₁)+δ(T₃)`.

More generally, any exact sequence `0→A→B→T→0` with `A,B` lattices satisfies

`δ(T)=[B]−[A]`.

To verify this without choosing a new invariant, form `Q=P×_T B`. Its two lattice exact sequences are `0→A→Q→P→0` and `0→L→Q→B→0`. Thus `[A]+[P]=[L]+[B]`, which is precisely the formula.

For every lattice `M`, multiplication by `π` identifies `M` with the lattice `πM`. The last formula applied to `0→πM→M→M/πM→0` gives

`δ(M/πM)=0`.

### Specht reductions make the boundary zero

Let `S_O^λ` be the Specht lattice with its standard integral polytabloid basis, extended from `Z` to `O`. James Theorem8.4, pp29–30, and Corollaries8.6–8.11, pp30–31, give its freeness, integer action matrices and reduction `k⊗S_O^λ=S_k^λ`.

In residue characteristic `p>0`, James Corollary12.2, p42, shows that for a p-regular `λ`, the class `[S_k^λ]` equals `[D_k^λ]` plus a sum of classes indexed by strictly dominating p-regular partitions. Equivalently, Corollary12.3, p43, exhibits the unitriangular p-regular submatrix of the decomposition matrix. This works over the present arbitrary residue field: Theorem11.5, p40, explicitly states that every `D^λ` is absolutely irreducible and every field is a splitting field for `S_n`. Tensoring a composition series over `F_p` with `k` is exact and its simple factors remain simple. The standard polytabloid matrices identify that tensor product with the Specht module over `k`. Since the poset is finite, backward substitution over `Z` expresses every simple class `[D_k^λ]` as an integral linear combination of the classes `[S_k^μ]`.

In residue characteristic zero, the Specht modules themselves form the complete set of simple `k[S_n]`-modules by the characteristic-zero case of the same theorem. Their classes already form a basis. This supplies the same generation conclusion without a modular reduction argument.

The boundary vanishes on every `[S_k^μ]`, because it is the reduction of `S_O^μ`. Its additivity therefore makes it vanish on every finite-dimensional `k[G]`-module. A finite `O`-torsion module has the finite filtration by powers of `π`, whose successive quotients are finite-dimensional `k[G]`-modules. Consequently

`δ(T)=0` for every finite `O`-torsion `O[G]`-module `T`.

### Commensurability and the inverse on Grothendieck groups

Suppose lattices `M,N` have isomorphic rationalizations. Use an actual `K[G]`-isomorphism to place them inside one finite-dimensional `K[G]`-module. The intersection `I=M∩N` is a `G`-stable lattice, and both `M/I` and `N/I` are finite `O`-torsion. Applying the boundary formula gives `[M]=[I]=[N]` in the exact lattice group.

The algebra `K[S_n]` is split semisimple. Its irreducibles are the rationalizations of the Specht lattices. These facts prove surjectivity of `r_n`. An element of its kernel has the form `[M]−[N]`; equality of the rationalized classes in a semisimple category gives an actual rational isomorphism. The intersection argument proves `[M]=[N]`, and hence injectivity. More explicitly, the inverse sends the rational Specht class `[S_K^λ]` to `[S_O^λ]`; the preceding argument verifies that this inverse also recovers the class of every lattice.

### Induction multiplication

Form the graded group `R_O=⊕_{n≥0}K₀(L_O(S_n))`, with product

`[M]·[N]=[Ind_{S_a×S_b}^{S_{a+b}}(M⊗_O N)]`.

Tensor product is exact in each variable because the underlying modules are free. The group algebra of `S_{a+b}` is free over that of `S_a×S_b` on a coset basis, so induction is exact and preserves lattices. Rationalization commutes with these functors through the canonical tensor and induction isomorphisms. Thus `⊕r_n` is an isomorphism of graded rings.

The rational Frobenius characteristic sends the trivial representation `ρ_n` to the complete symmetric function `h_n`. Since `Λ=Z[h₁,h₂,…]`, this yields the concrete generator-preserving isomorphism

`Z[ρ₁,ρ₂,…] ≅ R_O`.

This includes `O=Z_p` and `O=Z_(p)` and resolves the study's expressly open `Z_p`-lattice case. No completeness or unramifiedness assumption is needed. The proof uses that submodules of finite free `O`-modules are free and that finite torsion modules admit the displayed residue-field filtration. The exact boundary of these steps is substantive: A-023 in `LOCAL_RING_COUNTEREXAMPLE.md` gives a characteristic-zero local ring with a rank-one representation outside the subgroup generated by the Young permutation classes. The broader classification of coefficient rings remains a question.

## Primary source and inspection record

James's original book: DOI `10.1007/BFb0067708`; public university-hosted scan: https://www-users.cse.umn.edu/~webb/oldteaching/Year2010-11/the-representation-theory-of-the-symmetric-groups-SLN.pdf . The cited pages29–31,36,39–40,42–43 were read. The standard-basis proof, the stated simple-module classification and its proof dependencies, and the unitriangularity argument were checked. The classification theorem's count invokes general modular representation theory explicitly cited by James; this report does not claim a new proof of that theory. The torsion boundary, pullback comparisons, commensurability argument and graded-ring compatibility above were independently checked in full in this run.


# A-022. The hyperbolic Stiefel–Whitney formula

Write `α∈H¹_et(X,Z/2)` for the Kummer class of `−1`, and let `c̄_j` denote the mod2 étale Chern class. For a rank-r vector bundle `E`, the formula appearing in the supplied study is

`w_t(H(E)) = Σ_{j=0}^r (1+αt)^(r−j) c̄_j(E)t^(2j)`.

The displayed hyperbolic formula holds for every scheme over `Z[1/2]`, by the explicit splitting morphisms proved below. The exact primary locator for the formula is Esnault–Kahn–Viehweg, *Coverings with odd ramification and Stiefel–Whitney classes*, Journal für die reine und angewandte Mathematik441 (1993), Proposition5.5, pp183–184. The actual author-hosted scan is https://page.mi.fu-berlin.de/esnault/preprints/helene/29-es_ka_vi.pdf . Section5.1, p179, starts with a scheme over `Z[1/2]`; section5.4, p182, introduces a regularity assumption. Thus the source directly establishes the displayed formula for regular schemes over `Z[1/2]`. Its result also covers metabolic bundles with the Chern classes of a Lagrangian. The proof here establishes the stated hyperbolic formula over arbitrary `Z[1/2]`-schemes. No characteristic-two version is claimed.

Both pages of the proposition and proof were visually read. The proof first computes the rank-two case using the complement of the isotropic quadric, then constructs an affine-bundle pullback splitting off a metabolic rank-two summand. The remaining Lagrangian fits in a vector-bundle exact sequence, and the Chern-class Whitney formula gives the displayed sum by induction. The injective étale-cohomology pullback descends the identity. Zibrowius, *Witt groups of curves and surfaces*, §1.4, equations(6)–(8), printedp8 (PDFpage9) in the author PDF, reproduces the formula and its first two components with this exact EKV locator. That exposition explicitly treats schemes over `Z[1/2]`; the regularity inherited from EKV§5.4 is recorded here rather than silently attributed away.

In particular,

`w₁(H(E))=rα`,

`w₂(H(E))=binom(r,2)α²+c̄₁(E)`.

For a line bundle `L`, the latter reduces to `w₂(H(L))=c̄₁(L)`. This line-bundle identity admits the following direct proof over every scheme over `Z[1/2]`, without the regularity assumption just identified in the source.

## The explicit line-bundle calculation

Let `p:U→X` be the open complement of the isotropic quadric in the projective bundle of lines in `H(L)=L⊕L∨`. Its tautological line `M` is nondegenerate. The first projection `M→p*L` is an isomorphism: at every geometric point the quadratic value of a tautological vector `(v,f)` is `f(v)≠0`, so both components are nonzero. A fibrewise nonzero map of line bundles is invertible. Orthogonal projection gives the actual decomposition

`p*H(L)=M ⊥ M^⊥`.

Set `x=w₁(M)`. The determinant form of `H(L)` has value `−1` in its canonical determinant trivialization; hence `w₁(M^⊥)=α+x`. The Whitney formula now gives

`p*w₂(H(L))=x(α+x)`.

For any symmetric line bundle with class `x∈H¹_et(U,Z/2)`, its ordinary first Chern class satisfies

`c̄₁(M)=x²+αx`.

This is Lemma5.3 of EKV, pp181–182, whose cocycle calculation uses only that2 is invertible. One can see the formula directly by writing transition signs as `(-1)^(a_ij)`, choosing local square roots of `−1`, and lifting these signs to fourth roots of unity. The Kummer coboundary has the two mod2 summands `a_ij a_jk` and `α_ij a_jk`, respectively the square and the cup product. Therefore

`p*w₂(H(L))=c̄₁(M)=p*c̄₁(L)`.

The pullback `p*:H*_et(X,Z/2)→H*_et(U,Z/2)` is injective by the orthogonal splitting principle, Zibrowius, *The gamma-filtration on the Witt ring of a scheme*, Proposition3.3, author version arXiv:1411.3198v2, pp19–20. Its proposition explicitly assumes a scheme over `Z[1/2]`, which is exactly the present scope. Injectivity gives the asserted equality on `X`.

## A direct splitting morphism for an arbitrary vector bundle

The same nonisotropic-line construction supplies the full higher-rank formula without an additional affine-bundle invariance theorem. Let `E` have rank `r>0` and form

`p:U=P_nd(H(E))→X`.

Let `M⊂p*E⊕p*E∨` be the tautological nondegenerate line. Its two projections give maps

`a:M→p*E`,

`b:p*E→M∨`.

The composite `β=b∘a:M→M∨` is an isomorphism: in a local generator `(v,f)` of `M`, it is multiplication by the invertible value `f(v)`. The nondegeneracy of the restricted hyperbolic symmetric form says that `2f(v)` is a unit; here2 is invertible. Therefore

`e=a∘β^(−1)∘b : p*E→p*E`

is an actual idempotent, since `e²=aβ^(−1)(ba)β^(−1)b=e`. It exhibits

`p*E=a(M) ⊕ ker(b)`.

Both summands are vector bundles, of ranks1 and `r−1`. In local coordinates the projector is `z↦v f(z)/f(v)`. Replacing `(v,f)` by `t(v,f)` leaves this projector unchanged, which also verifies the global gluing directly. The line `a(M)` is isomorphic to `M` through `a`.

Zibrowius Proposition3.3 and its first-step proof show that this particular `p` induces an injection on mod2 étale cohomology. Repeat the construction on `ker(b)`, reducing its rank by one at each step. After finitely many steps there is a composite morphism `q:Y→X` with injective pullback on mod2 étale cohomology and an actual direct-sum decomposition

`q*E=L₁⊕⋯⊕L_r`.

The direct-sum projections and their dual inclusions give the orthogonal isomorphism

`q*H(E) ≅ H(L₁) ⊥ ⋯ ⊥ H(L_r)`.

By the already proved line-bundle result and the Whitney identities,

`q*w_t(H(E))=∏_{i=1}^r(1+αt+c̄₁(L_i)t²)`.

Expanding by the set of indices that contribute their Chern term gives

`∏_{i=1}^r(1+αt+c̄₁(L_i)t²)=Σ_{j=0}^r(1+αt)^(r−j)c̄_j(q*E)t^(2j)`.

Naturality and the injectivity of `q*` descend this equality to `X`. Rank zero is the identity `1=1`, and a locally constant rank is treated on its open-and-closed rank pieces. This proves the full hyperbolic formula over every scheme over `Z[1/2]` through explicitly constructed bundle maps.

## What this resolves in the archive

Original Montpellier PDFpage4 was visually inspected and does contain the `c₁ ?` question. The study's proposed answer for `w₂(H(L))` and its full hyperbolic formula are correct over every scheme over `Z[1/2]`, as just proved. The arbitrary-ringed-topos question about an augmented completed lambda-ring target, recorded separately as A-Q080, still requires its multiplication and operations to be specified; these characteristic-class identities do not supply that missing target definition.

The printed rank-two proof on EKVp183 includes a sentence asserting an isomorphism on the unmodified Picard groups. That assertion is unnecessary for the direct argument above. For example, the complement for `H(L)` is the nonzero total space of a square of `L`, and the pullback kills `2[L]`; consequently an integral Picard-group isomorphism cannot be used in that generality. The independently verified argument uses the stated injective mod2 cohomology pullback and the actual line isomorphism instead.


# A-023. A characteristic-zero local ring where the rho classes do not generate

Take the explicit commutative ring

`A=Z_(2)[ε]/(2ε, ε²)`.

As an abelian group it is `Z_(2)⊕F₂ε`, with product

`(a+bε)(c+dε)=ac+(ād+c̄b)ε`.

This proves that `ε≠0` and that `A` has characteristic zero. An element `a+bε` is a unit precisely when `a` is a unit of `Z_(2)`: its inverse is `a^(−1)−a^(−2)bε`. Hence `A` is local with maximal ideal `(2,ε)` and residue field `F₂`.

The coefficient ring also has `K₀(A)≅Z`, with the isomorphism given by rank. Indeed, for a finite projective module `P`, lift a basis of `P/(2,ε)P` to obtain a surjection `A^r→P` by Nakayama's lemma. It splits because `P` is projective. Its complementary finite projective module has zero residue quotient and is therefore zero by the same lemma. Thus every finite projective `A`-module is free, and rank identifies its Grothendieck group with `Z`. The example therefore also addresses the originalpage29 parenthetical question about coefficient rings with `K(k)≅Z`.

Let `G=S₂=C₂`, with generator `g`. The free rank-one `A`-module `L=Ae` with action

`g(e)=(1+ε)e`

is a representation, since `(1+ε)²=1`. Its determinant character sends `g` to `1+ε`.

For every `A[G]`-module `M` whose underlying `A`-module is finite free, the determinant of each group element defines a character `det(M):G→A×`. This gives a homomorphism

`det:K₀(L_A(G))→Hom(G,A×)`

from the exact Grothendieck group (written additively) to the character group (written multiplicatively). Indeed, every admissible exact sequence splits as a sequence of underlying `A`-modules. In an `A`-basis adapted to its submodule, a group element acts by a block upper triangular matrix. Its determinant is the product of the determinants on submodule and quotient. Thus the determinant respects precisely the exact relations defining this `K₀`.

In degree two, the monomials in the proposed generators are

`ρ₂=[A_trivial]`,

`ρ₁²=[Ind_{S₁×S₁}^{S₂}A]=[A[S₂]]`.

The corresponding determinant characters take `g` to `1` and `−1`, respectively: on the standard basis of the regular module, `g` interchanges two basis vectors. Consequently the determinant of every integer linear combination `aρ₂+bρ₁²` takes `g` to `(-1)^b`.

The character `1+ε` equals neither `1` nor `−1`. The first inequality follows from `ε≠0`. Reduction modulo `ε` maps the second proposed equality to `1=−1` in the characteristic-zero ring `Z_(2)`, which is false. Therefore

`[L] ∉ Zρ₂+Zρ₁²`.

The graded map `Z[ρ₁,ρ₂,…]→⊕_n K₀(L_A(S_n))` fails surjectivity already in degree two. This is an explicit counterexample even among characteristic-zero local rings. It is compatible with A-021: the ring `A` has the nonzero torsion element `ε` and is not a discrete valuation ring. The exact determinant map above is the witness for the failure; no distinction between two unnamed representation categories is being used.

The supplied study marks the classification of coefficient rings as open and its later annotation points to a characteristic-zero local counterexample in another record. That other record was not read here. The ring, representation, determinant map and non-generation proof above were constructed and checked directly in this run.


# The five-point Cox ring and the Segre cubic, with the exact group action

## A-028. Source identification and actual algebra map

Let \(E=\mathfrak h_5\), let \(Z=\{[\ell_i]\}_{i=1}^5\subset\mathbf P(E)\), and let \(X=\operatorname{Bl}_Z\mathbf P(E)\). Write \(H\) for the pullback of the hyperplane class and \(E_i\) for its five exceptional divisors. Choose the canonical exceptional sections \(e_i\), with their literal permutation action. The following explicit map identifies the Cox ring with the Plücker coordinate ring of \(\operatorname{Gr}(2,6)\):
\[
\boxed{
p_{i6}\longmapsto e_i,\qquad
p_{ij}\longmapsto
\frac{q_i-q_j}{\prod_{k\notin\{i,j\}}e_k}
\quad(1\le i<j\le5).
}
\tag{Cox.1}
\]
Here \(\sum_iq_i=0\), and \(p_{ji}=-p_{ij}\). Its Picard grading is
\[
\deg p_{i6}=E_i,\qquad
\deg p_{ij}=H-\sum_{k\notin\{i,j\}}E_k.
\tag{Cox.2}
\]
The \(S_5\) action permutes the first five Plücker indices and fixes the sixth. It is equivariant under (Cox.1), including the signs arising when an ordered pair is reversed.

The primary general Cox-ring locator is A.-M. Castravet and J. Tevelev, *Hilbert's 14th problem and Cox rings*, **Compositio Math. 142** (2006), 1479–1498, **Remark 3.9, p. 1487**. I opened and read the [author's published PDF](https://people.math.umass.edu/~tevelev/14problem.pdf). Its \(s=1,n=3\) instance identifies this Cox ring with the Plücker ring of \(\operatorname{Gr}(2,6)\). The exact map and action above are verified below rather than inferred from an abstract ring isomorphism.

For the Segre map and the representation convention, I opened and read I. Dolgachev, B. Farb and E. Looijenga, *Geometry of the Wiman–Edge pencil, I: algebro-geometric aspects*, [author PDF](https://www.math.uchicago.edu/~farb/papers/wiman.pdf), **§2.3, Table 1, p. 10**, and **Remark 2.4, p. 13**. Table 1 gives the five-dimensional representation with transposition trace 1; Remark 2.4 describes the equivariant quadratic map through the five frame points and identifies the ambient \(S_6\) representation as \([(3,3)]\). The printed remark contains a dimension typo \(\mathbf P^4=\mathbf P(V)\): the \(V\) fixed in §2.3 has dimension four and its projectivization is \(\mathbf P^3\). The quadratic map and target dimension in the surrounding discussion specify the intended spaces.

## 1. Proof of the Cox map through one additive-group action

Take the polynomial ring
\(P=\mathbf Q[x_1,\ldots,x_5,y_1,\ldots,y_5]\)
and the action of \(\mathbf G_a\) given by \(y_i\mapsto y_i+t x_i\), with \(x_i\) fixed. The invariant polynomials include
\[
x_i,\qquad p_{ij}=x_i y_j-x_jy_i.
\]
The invariant algebra is the Plücker ring of \(\operatorname{Gr}(2,6)\), with \(p_{i6}=x_i\). Here is a direct comparison map. Regard \((x_i,y_i)^T\) as the first five columns of a \(2\times6\) matrix and set the sixth column equal to \((0,1)^T\). Its stabilizer in \(SL_2\) is exactly the displayed additive group. An invariant function of the first five columns extends uniquely to an \(SL_2\)-invariant regular function on the open set where the sixth column is nonzero: choose locally an \(SL_2\) element sending that column to \((0,1)^T\), and use additive invariance to make the value independent of the choice. The two standard coordinate charts of the nonzero sixth column give regular choices. The complement has codimension two in affine matrix space, so the function extends across it by the intersection property of polynomial-ring localizations. Restriction and extension are inverse ring maps.

Finally, the \(SL_2\) invariant algebra of six column vectors is the image algebra of their \(2\times2\) minors. This can be seen directly from the Cauchy decomposition: its degree \(2d\) part is \(S_{(d,d)}\mathbf Q^6\), and products of the minors contain a nonzero highest vector in every such summand. Their span is \(GL_6\)-stable, so it contains the whole summand. This is precisely the Plücker coordinate ring. The construction commutes with permutation of the first five columns.

To identify this invariant algebra with the Cox ring using the specified grading, put
\[
u=\prod_i x_i,\qquad r_i=y_i/x_i,\qquad
q_i=u\left(\frac15\sum_jr_j-r_i\right).
\tag{Cox.3}
\]
These \(q_i\) are polynomial invariants, have sum zero, and transform by the standard representation. On \(u\ne0\), the differences of the \(r_i\) are coordinates for the additive quotient. Thus the localized invariant ring is exactly
\(\mathbf Q[x_i^{\pm1},q_1,\ldots,q_5]/(\sum q_i)\).
Sending \(x_i\) to \(e_i\) gives
\[
x_i y_j-x_j y_i
=\frac{q_i-q_j}{\prod_{k\notin\{i,j\}}x_k},
\]
which proves the formula for each generator in (Cox.1).

Assign \(\deg x_i=E_i\) and
\(\deg y_i=H-\sum_{j\ne i}E_j\).
Then \(q_i\) has degree \(H\), and every homogeneous element of the localized invariant ring is a polynomial \(f(q)\) of some degree \(c\), multiplied by \(\prod_i x_i^{a_i}\). Its degree is \(cH+\sum_i a_iE_i\).

It remains to check which such elements are polynomial before localization. Along \(x_i=0\), the vector \(q\) in (Cox.3) becomes the nonzero scalar
\(-y_i\prod_{j\ne i}x_j\) times \(\ell_i\) on the generic locus. The normalized transverse coordinates have leading terms \(x_i(r_j-r_l)/y_i\), with \(j,l\ne i\); their three independent differences vary freely. The same lowest-term calculation as G-015 therefore proves
\[
\operatorname{ord}_{x_i}f(q(X,Y))
=\operatorname{mult}_{[\ell_i]}f.
\]
The scalar trivializing the homogeneous degree-\(c\) factor is a unit there. Since the \(x_i\) are distinct primes, the Laurent expression is polynomial exactly when
\(\operatorname{mult}_{[\ell_i]}f+a_i\ge0\) for every \(i\).

These are exactly the section conditions for
\(\mathcal O_X(cH+\sum_i a_iE_i)\). They follow directly on the affine blow-up charts from divisibility by the required order of the point ideal. Positive exceptional coefficients permit their canonical sections but no additional poles downstairs: the removed points have codimension three, and a pole divisor cannot be supported on them. The criterion therefore identifies each Picard-graded piece, and multiplication is the same multiplication of Laurent polynomials. This proves the full ring isomorphism (Cox.1) with its exact action.

## 2. The quadratic subalgebra as an actual Cox component

Put \(D=2H-\sum_iE_i\). Under (Cox.1), the space
\(H^0(X,\mathcal O_X(D))\) is the space \(U\) of quadrics through the five points. Its Plücker multidegree is \((1,1,1,1,1,1)\), and its Plücker degree is three.

To verify the degree conversion explicitly, let \(b_{ij}\) count a factor \(p_{ij}\) with \(i,j\le5\), and let \(a_i\) count \(p_{i6}\). If its Cox degree is \(cH-k\sum E_i\), then
\[
\sum_{i<j}b_{ij}=c,\qquad
a_i+\sum_{j\ne i}b_{ij}=c-k.
\]
Hence its six column weights are
\[
(c-k,c-k,c-k,c-k,c-k,3c-5k),
\]
and its total Plücker degree is \(4c-5k\). Substituting \(c=2,k=1\) gives the asserted degree three and six equal weights.

The multilinear \(SL_2\) invariants of six columns are the Specht module \([(3,3)]\). This follows from the tensor Schur–Weyl decomposition, with the \(SL_2\)-invariant determinant power \(S_{(3,3)}\mathbf Q^2\). Restriction from the literal \(S_6\) column permutation action to the stabilizer of column six removes the unique removable box from \((3,3)\), giving \([(3,2)]\). Thus the extension of the quadratic \(S_5\) action to \(S_6\) is fixed by this actual column model; no choice of a projective lift determines it implicitly.

The same degree conversion sends every \(H^0(X,kD)\) to column weights \((k^6)\). Permuting all six columns preserves this diagonal component and therefore gives an \(S_6\) action on the whole \(D\)-section ring. It preserves the original \(S_5\) action on the first five indices. Permutations involving the sixth index act on this diagonal ring regardless of their action on the other Picard degrees.

By A-027 the algebra generated by \(U\) has the exact presentation
\[
\mathbf Q[A,B,C,D,E]/
\bigl(AD(E-B-C)-BC(E-A-D)\bigr).
\]
By A-029 the ordinary and saturated ideal powers agree in degree \(2k\) for every \(k\). Consequently multiplication of the quadrics maps this algebra isomorphically onto
\(\bigoplus_{k\ge0}H^0(X,kD)\).
This identifies the full section ring along the displayed Cox degree with the cubic algebra, including every graded piece and its action.

The cubic has sign character under \(S_5\), as the direct transposition calculation in A-027 shows. T-038 separately constructs its six linear forms and the actual exceptional six-element permutation action; that explicit intertwiner compares its usual six-coordinate Segre equation with the quadratic coordinates above. The present Cox calculation fixes the geometric \(S_6\) extension as \([(3,3)]\) in degree one.

## 3. The exact maps to ordinary and sheaf powers

There is an injective bigraded map
\[
\mathcal R(I)=\bigoplus_{k\ge0}I^k t^k
\longrightarrow\operatorname{Cox}(X),\qquad
f(q)t^k\longmapsto f(q)\left(\prod_i e_i\right)^{-k}.
\]
Its degree-\((c,k)\) image is \((I^k)_c\) in the Cox component
\(H^0(X,cH-k\sum E_i)\), which is the corresponding saturated fat-point section space. The component map is the usual inclusion of ordinary ideal powers into their sheaf sections. A-029 proves it is onto for \(c\ge2k\). Thus the quadratic cubic algebra, the ordinary Rees algebra, and the Cox section spaces are related here by specified inclusions and the stated equalities of graded components.

The full flag problem G-015 additionally tensors by its specified flag line bundle. The proofs here determine the point-ideal algebra and its action and provide the exact cohomology inputs recorded in A-029. They make no assertion that an alternating resolution alone has already evaluated every \(S_5\)-covariant flag-section multiplicity.


# The five-point ideal: exact Rees map, linear powers, and the quotient-bundle sections

## A-029. Completed result

Let \(S=\mathbf Q[x,y,z,w]\), let \(Z\subset\mathbf P^3\) be the four coordinate points and \([1:1:1:1]\), and put
\[
I=(xz-xy,xw-xy,yz-xy,yw-xy,zw-xy).
\]
The literal \(S_5\) action is the action permuting the five canonical projective-frame points in \(\mathbf P(\mathfrak h_5)\), transported by the specified basis. Write \(U=I_2=[(3,2)]\). The following statements have been proved with the hypotheses and degree conventions checked:

1. The Rees algebra is the quotient by the actual five linear syzygies and the one cubic \(F\) below.
2. The kernel of \(\operatorname{Sym}^k_S(I(2))\to I^k(2k)\) is the degree-zero \(S_5\)-module \(\operatorname{sgn}\otimes\operatorname{Sym}^{k-3}U\), annihilated by \((x,y,z,w)\); a negative symmetric power means zero.
3. For every \(k\ge2\), \(I^k\) has a \(2k\)-linear free resolution. In particular its saturation agrees with \(I^k\) in every degree \(c\ge2k\), and
\[
H^1(\mathbf P^3,\mathcal I_Z^k(2k-1))=0.
\]
4. For the tautological rank-three quotient \(\mathcal Q\) on \(\mathbf P(\mathfrak h_5)\), put
\(M_k=H^0(\mathcal Q\otimes\mathcal I_Z^k(2k))\).
Then
\[
\dim M_k=\frac{(k+1)(k+2)(3k+4)}2,
\qquad
\sum_{k\ge0}\dim M_k t^k=\frac{4+5t}{(1-t)^4}.
\]
These are actual statements for this ideal; no unverified general-position or acyclicity hypothesis remains in their use below.

## Primary source and exact locators

The primary source is A. R. Kustin, C. Polini, B. Ulrich, *The equations defining blowup algebras of height three Gorenstein ideals*, **Algebra & Number Theory 11** (2017), 1489–1525, DOI [10.2140/ant.2017.11.1489](https://doi.org/10.2140/ant.2017.11.1489). The [publisher PDF](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf) was opened and read; its local copy is `primary_m5/kustin_polini_ulrich_2017.pdf`.

The exact passages used are formula **(6.1.4), p. 1509**; **Lemma 6.3 and Corollary 6.4, p. 1510**, with the corollary's proof on p. 1511; and **Theorem 9.1, pp. 1520–1521**. Proposition 7.5, pp. 1514–1515, independently states the symmetric-power regularity bounds agreeing with the calculation below. The 2016 author PDF has different pagination: formula (6.1.4) p. 18, Lemma 6.3/Corollary 6.4 p. 19, Theorem 9.1 p. 28. The journal version supplies the locators in this report.

I read the statements and their surrounding proofs, including the local generator condition and the exceptional degree in (6.1.4). The use of those established complexes is explicitly attributed; their 1992 construction is not presented as a newly checked construction here.

## 1. The ideal and all local hypotheses

The complete first resolution is the one constructed in T-038. Its exactness can be verified from the displayed \(M,N\) without any extra geometric hypothesis: \(f^TM=0\), \(MN=0\), a \(4\times4\) minor of \(M\) is nonzero, and \(\gcd(N_1,\ldots,N_5)=1\). Over the fraction field, the kernel of \(M\) is spanned by \(N\). A rational scalar \(a/b\) with coprime numerator and denominator whose product with every \(N_i\) is polynomial has \(b\) dividing all \(N_i\), so \(b\) is a unit. Thus the polynomial kernel is exactly \(SN\). The Hilbert series from G-016 then proves exactness at the preceding term, giving
\[
0\longrightarrow S(-5)\longrightarrow S(-3)^5
\longrightarrow S(-2)^5\longrightarrow I\longrightarrow0.
\]
In particular the presentation entries are linear and the ideal has height three.

For direct compatibility with the primary source, the same matrix can be made alternating. If \(f=(A(x),B(x),C(x),D(x),E(x))^T\) is the vector of the five quadrics, then the terminal column is \(N=Pf\), where
\[
P=\begin{pmatrix}
0&0&0&-1&0\\
0&0&1&0&-1\\
0&1&0&0&0\\
0&0&-1&1&0\\
1&-1&0&0&0
\end{pmatrix},\qquad\det P=-1.
\]
The actual matrix \(\varphi=MP\) is
\[
\begin{pmatrix}
0&y&w&0&-y\\
-y&0&0&-z&y\\
-w&0&0&-x&x\\
0&z&x&0&-x\\
y&-y&-x&x&0
\end{pmatrix}.
\]
Its signed maximal Pfaffians are \(f\): their vector spans the same one-dimensional kernel and its first entry is \(xz-xy\). The resolution is self-dual, with terminal map \(f\), so the canonical module of \(S/I\) is a grading shift of \(S/I\). Together with its dimension-one Cohen–Macaulay property this verifies that \(I\) is a perfect Gorenstein ideal. One can check the Cohen–Macaulay property directly: a linear form nonzero at all five points is a nonzerodivisor in the product embedding of the five line rings proved in G-016.

Away from the common vertex, the five affine lines are disjoint and smooth. The ideal localized at any point of that punctured cone is generated by three independent normal linear parameters. Thus the source's \(G_4\) condition is satisfied. Its weaker condition
\(\mu(I_{\mathfrak p})\le\dim S_{\mathfrak p}+1\)
also holds at every prime: the only remaining vertex has five generators in a four-dimensional regular local ring. Hence Lemma 6.3 applies with \(s=4\) at every prime, not merely on the punctured spectrum. The parameters in the source are \(d=4,n=5,\delta=2,D=1\).

## 2. The exact Rees presentation and torsion module

Let \(A,B,C,D,E\) now denote five independent variables mapping to the five quadratic generators. The exact subalgebra kernel checked in A-027 is generated by
\[
F=AD(E-B-C)-BC(E-A-D).
\]
It has sign character. Put \(T=(A,B,C,D,E)\) and
\(L=(\text{entries of }T\varphi)\subset S[T]\).
Then \(S[T]/L\) is the symmetric algebra of the displayed presentation of \(I(2)\). The map to the Rees ring sends each \(T_i\) to the corresponding \(f_i t\); it is equivariant with the literal action on \(U\).

Corollary 6.4 gives fiber type for this ideal. Since its special-fiber equation has just been proved to be exactly \(F\), it gives the concrete presentation
\[
\boxed{\mathcal R(I)=S[T]/(L,F).}
\]
The same corollary says the symmetric-algebra torsion is annihilated by
\(\mathfrak m^{(n-d+1)/2}=\mathfrak m\).
The linear syzygy ideal \(L\) has positive \(x,y,z,w\)-degree and therefore has zero intersection with \(\mathbf Q[T]\). It follows that the \(k\)-th torsion piece is precisely
\[
F\operatorname{Sym}^{k-3}U
\simeq\operatorname{sgn}\otimes\operatorname{Sym}^{k-3}U,
\]
in polynomial degree zero after the shift by \(2k\). The multiplication map giving this isomorphism is injective because \(\mathbf Q[T]\) is a domain.

There is also an independent exact certificate for the annihilation assertion. Write \(T\varphi=(x,y,z,w)B(T)\), where
\[
B(T)=\begin{pmatrix}
0&0&D-E&E-C&C-D\\
E-B&A-E&0&0&B-A\\
0&D&0&-B&0\\
-C&0&A&0&0
\end{pmatrix}.
\]
For the polynomial matrix
\[
Q(T)=\begin{pmatrix}
AB&AD&-A(A+C-E)&-B(A+D-E)\\
AB&BC&-A(B+C-E)&-B(B+D-E)\\
BC&CD&-C(A+C-E)&-D(B+C-E)\\
AD&CD&-C(A+D-E)&-D(B+D-E)\\
AB&CD&-AC&-BD
\end{pmatrix},
\]
direct multiplication gives \(B(T)Q(T)=F(T)I_4\). Consequently
\((x,y,z,w)F=(T\varphi)Q\), which explicitly places all four products in \(L\). This multiplication was executed exactly; the receipt is `FIVE_POINT_TORSION_CERTIFICATE.txt`.

## 3. Linearity of every power from \(k=2\) onward

By the verified global hypothesis of Lemma 6.3, the complex \(D^k_\bullet(\varphi)\) is a free resolution of \(\operatorname{Sym}^k_S(I(2))\). Inspect formula (6.1.4) with \(n=5,D=1\):

- \(k=2\): all nonzero terms in homological degrees \(0,1,2\) have shift equal to the homological degree.
- \(k=3\): degrees \(0,1,2,3\) have that same shift. The exceptional \(Q_3\) term in degree four has shift \(3+(5-4+1)/2=4\), so it is linear as well.
- \(k\ge4\): every nonzero term lies in homological degree \(r\le4\) and has shift \(r\).

Thus \(\operatorname{Sym}^k_S(I(2))\) has a linear resolution for all \(k\ge2\). The excluded case \(k=1\) has the known shift three in homological degree two, agreeing with its original resolution.

The torsion kernel in §2 is a vector space in degree zero killed by \(\mathfrak m\), so its Koszul resolution is linear. Apply the graded Tor exact sequence to
\[
0\to\operatorname{sgn}\otimes\operatorname{Sym}^{k-3}U
\to\operatorname{Sym}^k_S(I(2))\to I^k(2k)\to0.
\]
In homological degree \(i\), the possible degrees for the last Tor group are at most \(i\). A module generated in degree zero has no minimal \(i\)-th syzygies in degrees below \(i\). Therefore its Tor is concentrated in degree \(i\): \(I^k(2k)\) has a linear resolution. This proves \(\operatorname{reg}(I^k)=2k\), with the equality also forced by its nonzero minimal generators in degree \(2k\).

Finite group equivariance is retained: the multiplication, its kernel, and the Tor sequence are equivariant, and degreewise averaging supplies equivariant choices of minimal generators whenever a free resolution is chosen. This statement supplies actual resolutions and exact modules; it does not claim an unevaluated representation-theoretic splitting to be a positive coefficient formula.

## 4. Saturation and the cohomology required in G-017

The saturation of \(I^k\) is the homogeneous ideal of the five order-\(k\) fat points, since the ordinary power restricts to that ideal away from the affine vertex. Its quotient by \(I^k\) is \(H^0_{\mathfrak m}(S/I^k)\). The linear resolution bounds this module's highest degree by \(2k-1\): in a free resolution of \(S/I^k\), the term in homological degree four has shift at most \(2k+3\), and the top Čech cohomology of \(S(-a)\) has highest degree \(a-4\). Thus
\[
(I^k)_c=H^0(\mathbf P^3,\mathcal I_Z^k(c))
\quad(c\ge2k,k\ge2).
\]
For \(k=1\), equality in all degrees follows from G-016's saturated ideal calculation. In particular the degree-\(2k\) section space is the image of \(\operatorname{Sym}^kU\), whose only relations are the degree-\(k\) multiples of \(F\). Write
\[
C_k=\binom{k+4}{4}-\binom{k+1}{4}
=\frac{(k+1)(k^2+2k+2)}2.
\]
Here the second binomial is zero for \(k<3\).

The same resolution gives \(H^1(\mathcal I_Z^k(2k-1))=0\) for \(k\ge2\). Equivalently, the highest degree of \(H^2_{\mathfrak m}(I^k)\) is at most \(2k-2\). The fat-point scheme has length
\(5\binom{k+2}{3}\), because a point in a smooth threefold has \(\binom{k+2}{3}\) monomials of degree below \(k\) in its three normal variables. Hence
\[
h^0(\mathcal I_Z^k(2k-1))
=\binom{2k+2}{3}-5\binom{k+2}{3}
=\frac{k(k+1)(k-2)}2
\quad(k\ge2).
\]
These are sheaf sections below the generator degree of the ordinary power; the exact inclusion and saturation calculation above specifies their relationship.

Tensor the tautological quotient sequence
\[
0\to\mathcal O(-1)\to\mathfrak h_5\otimes\mathcal O
\to\mathcal Q\to0
\]
with \(\mathcal I_Z^k(2k)\). It remains exact because the quotient bundle is locally free. The proved first-cohomology vanishing makes its global sections right exact for \(k\ge2\). Therefore
\[
\dim M_k=4C_k-\frac{k(k+1)(k-2)}2
=\frac{(k+1)(k+2)(3k+4)}2.
\]
For \(k=1\), evaluation in degree one is \(\mathfrak h_5\hookrightarrow\operatorname{Perm}_5\), with trivial one-dimensional cokernel. Thus \(H^1(\mathcal I_Z(1))=\mathbf Q\), while \(H^0(\mathcal I_Z(1))=0\), and the same exact sequence gives \(\dim M_1=4\cdot5+1=21\). For \(k=0\), \(H^0(\mathcal Q)=\mathfrak h_5\) has dimension four. These agree with the same polynomial formula.

Finally
\[
\frac{(k+1)(k+2)(3k+4)}2
=4\binom{k+3}{3}+5\binom{k+2}{3},
\]
so summing gives the stated series \((4+5t)/(1-t)^4\). This checks precisely the cohomology and dimension step requested for G-017. The later presentation of \(M\) by the root's matrix is a separate proof-review event.


\part{Algebraic-geometric restatements and proof dictionaries}


# Separate algebraic-geometric restatements

## The common exact transport

Let \(E\) be a locally free sheaf of rank \(r\). Its frame torsor \(\operatorname{Isom}(\mathcal O^r,E)\) transports every equivariant polynomial map between the specified \(GL_r\)-modules to a natural map between associated locally free sheaves. The representation ring is the exact Grothendieck ring of the category of finite locally free representations; the class of an exterior power is the corresponding lambda operation. These are the constructions of SGA 3, Exposé I, Section 4.5 and Propositions 4.7.2--4.7.3, and SGA 6, Exposé VI, Theorem 3.3. The conjugation \(S^{\mathrm{int}}_\lambda=L_{\lambda'}\) used in A-012 fixes the integral Schur convention explicitly.

The evaluation homomorphism from the free special lambda ring sends \(e_i\) to \([\Lambda^iE]\). In rank \(r\), it factors through \(e_{r+1},e_{r+2},\ldots=0\); determinant inversion gives the Laurent representation ring of \(GL_r\). The precise universal locators are SGA 6 V Proposition 4.2, Definition 4.4, Proposition 4.8, and Corollary 4.9. Composition of the resulting operations is the Schur-functor composition proved by the actual functorial maps in the preceding parts.

Characteristic-zero averaging uses the idempotent \(|H|^{-1}\sum_{h\in H}h\). Its integral model is over \(\mathbb Z[1/|H|]\), a scheme over \(\mathbb Z\). Each additional rational presentation has finitely many coefficients and a finite Gröbner basis; invert the product of their denominators and leading coefficients. The resulting monic relations, module maps, and flat Gröbner family define the exact same generic-fiber construction over that localization. This construction specifies its base rather than silently extending an averaging argument across primes dividing its denominator.

## Dictionary for every theta and positive-formula finding

| Finding | Algebraic-geometric restatement and the map carrying the proof | Exact framework |
|---|---|---|
| T-001 | The complexification of the compact pair gives the polynomial algebra on \(E\otimes F\). Its two commuting group-scheme actions yield the Cauchy summands; the stated determinant square root records the oscillator pullback before its explicit removal. | SGA 3 I 4.5, 4.7.2; SGA 6 VI 3.3. |
| T-002 | Extract the \((n^m)\)-graded summand of the diagonal-torus comodule and apply the constant \(S_m\) idempotent. This associated summand is exactly the multiplicity module of \(S_\lambda E\). | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-003 | Pull back the \(GL(S_\nu E)\) representation along its specified Schur-functor representation morphism; the wreath-group Hom is the equivalent tensor idempotent summand. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| T-004 | Interlacing patterns index the torus-graded Schur sheaf before the finite quotient; its Hilbert function is the stated weight multiplicity. | SGA 3 I 4.7.3. |
| T-005 | Tensoring by \(\det^t F\) shifts the torus grading and restricts to \(\operatorname{sgn}^t\) on the permutation subgroup. This line-bundle isomorphism transports the precise projector. | SGA 3 I 4.5, 4.7.2; SGA 6 V 4.8--4.9. |
| T-006 | The rank-two weight line is \(\det^j F\) times a balanced symmetric monomial; its swap scalar computes the invariant direct summand. | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-007 | The even-row decomposition becomes the indicated equality of associated Schur-sheaf classes after the frame-torsor pullback. | SGA 6 VI 3.3. |
| T-008 | Products of highest-weight sections in the stated integral-domain coordinate algebras give nonzero sections of the sum weight. This is the actual multiplication map proving support addition. | EGA I 9.5.1--9.5.3; SGA 3 I 4.7.2. |
| T-009 | The specified stretching Hilbert function has the recorded period-six values; Ehrhart reciprocity contradicts the proposed homogeneous-polytope Hilbert function. It leaves the proved cellwise presentations intact. | EGA I 9.5.3; the exact Hilbert grading is specified in T-009. |
| T-010 | The stable equality is an identity of Schur coefficients in the completed lambda ring; its transpose is the characteristic of the explicitly graded symmetric/exterior algebra \(\mathcal M_k\). | SGA 6 V 4.2, VI 3.3. |
| T-011 | The integer arrays index Littlewood--Richardson multiplicity bases. Applying the associated-bundle construction identifies the same counts in each tensor product of Schur sheaves. | SGA 6 VI 3.3. |
| T-012 | The width-five tensor factors, their finite exterior-cube table, and their glued LR arrays give the Hilbert components of \(\mathcal M_5\). | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-013 | The independently certified 156-character table and the displayed tensor-factor maps give the identical statement for \(\mathcal M_6\). | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-014 | The specified products of highest-weight sections of the symmetric factors and degree-zero/one sections of the exterior factors give the claimed nonzero Schur-sheaf summand. | SGA 6 VI 3.3. |
| T-015 | The historical endpoint check concerns the same graded Chow pullback as G-003; its parameter range is now contained in the cited Sra bound. | EGA I 9.5.2; M-001 source audit. |
| T-016 | The cubic metric is a morphism of associated bundles; division of its adjugate by the square of the discriminant is regular by the proved divisor valuation. | EGA I 9.5.1--9.5.3; SGA 3 I 4.7.2. |
| T-017 | Matrix coefficients identify the specified homogeneous-bundle sections on \(GL_7/(G_2\times\mu_3)\) with stabilizer invariants. The harmonic and Pieri proof computes their rank. | SGA 3 I 4.7.2. |
| T-018 | Inclusion into the discriminant localization identifies extension with a nonnegative divisor valuation. The three polynomial highest sections generate the computed sector; their degrees are the polytope equations. | EGA I 9.5.3; SGA 3 I 4.7.3. |
| T-019 | Differentiation of the degree-seven section is the stated equivariant bundle map. Multiplication with the metric, cometric, determinant and remaining factors gives the associated stable Schur components. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| T-020 | The filtration by order along the boundary divisor is the explicit regular-extension subspace of the homogeneous-bundle section space. | EGA I 9.5.1--9.5.3. |

## Dictionary for the root constructions

| Finding | Algebraic-geometric statement and proof transport | Exact framework |
|---|---|---|
| G-001 | The exact Pieri multiplication sequence restricts on its all-ones weight to the augmentation kernel of the permutation module; determinant tensoring gives the sign twist. Its constant \(A_5\) restriction proves the stated monomial-basis obstruction. | SGA 3 I 4.7.2--4.7.3. |
| G-002 | The matrices are maps of free modules obtained from the two constant-group correspondences. Their determinantal ideals describe their rank strata; the Cauchy--Binet sum computes the same rank over the real generic fiber. | Stacks Project 07Z6, Lemmas 15.8.2 and 15.8.4; 05P8, Lemma 31.9.6. No unverified EGA Fitting locator is supplied. |
| G-003 | The divided-power coordinate pullback defines the integral scheme image and its torsion-free, graded-free coordinate algebra. Its rational grading is the canonical-map image. Hilbert and Quot schemes represent the stated flat projective families. | EGA I Prop.9.5.1, Cor.9.5.2, Def.9.5.3, Prop.9.5.4; FGA Exp.221 Thms.3.1--3.2, after Prop.3.8. |
| G-004 | The two rational Artin correspondences on a degree-two finite etale scheme have Frobenius eigenvalues \(1,-1\). The actual projector ranks are one and zero. | Weil II Defs.1.2.1--1.2.2, Variants 1.2.3--1.2.4, stability 1.2.5(i). |
| G-005 | The tree marks and polytope coordinates are identical; the rank-two determinant line and frame-torsor map transport the known branching count to Schur-sheaf operations. | SGA 6 VI 3.3; SGA 3 I 4.7.3. |
| G-006 | Binary factorization makes the Chow morphism dominant; its degreewise coordinate pullback is the specified canonical isomorphism. Natural Schur-functor decomposition carries every retained multiplicity map to any larger frame rank. | EGA I 9.5.2; SGA 6 VI 3.3. |
| G-007 | Restriction to the constant \(S_3\) subgroup gives three trace values on the balanced torus summand. The three character idempotents give the displayed ranks in the representation Grothendieck ring. | SGA 3 I 4.7.2--4.7.3; SGA 6 V 4.2. |
| G-008 | Exact quartic character certificates produce invariant sections; multiplication in their domain and the conjugation involution yield the displayed repeated-part Schur coefficients. | SGA 6 V 4.2, VI 3.3. |
| G-009 | The successive affine flag, torus, and finite-group quotients have the explicitly presented invariant ring. A flat monomial degeneration preserves its Hilbert function; disjoint standard-monomial cells yield the bounded lattice sets. | SGA 3 I 4.7.2--4.7.3; EGA I 9.5.2--9.5.3. |
| G-010 | Adjoining the symmetric algebra of the dual wreath representation gives its covariant module in auxiliary degree one. Graph elimination produces its exact graded presentation. | SGA 3 I 4.7.2; SGA 6 VI 3.3; EGA I 9.5.2. |
| G-011 | The two finite-group correspondences act linearly over their common invariant ring; their image is a finite coherent module. The syzygy/elimination presentation and module degeneration compute each actual image rank. | EGA I 9.5.2; SGA 3 I 4.7.2. |
| G-012 | The explicit flag quotient has two monic quadratic equations. Its four-element free module over the polynomial subring is the exact geometric source of the four polytopes. | SGA 3 I 4.7.3; EGA I 9.5.3. |

## Dictionary for rectangular findings

R-001 is the determinant line in the balanced Schur sheaf; its \(S_a\) restriction is the sign character to the stated power. R-002 identifies the contraction of the two normalized tensor projectors with the signed Latin-square count and with the Haar period, with all factorials retained. The finite scheme used in R-006 has one component per Latin square and the indicated sign function; its pushforward trace gives that same integer. These are constant finite-group schemes and their associated locally free sheaves, in SGA 3 I 4.7.2--4.7.3 and SGA 6 VI 3.3.

R-003 restricts the specified wreath permutation representation and computes its exterior powers; the explicit comparison with the rectangular Kronecker summand is via those two functor multiplicities. R-004's indicator variables give a bijection between the cited rectangular-hook basis and a zero-one polytope. R-005 is the natural inner-degree multiplication map of sheaves, with its nonzero determinant pairing and highest-weight dimension. The coordinate-image transfer uses EGA I 9.5.2 and the exact BIP morphism cited in its proof.

R-007 transports the two prime-adjacent integer congruences through the exact scalar and Haar identities of R-002, yielding the stated valuations in \(\mathbb Z_{(p)}\). R-008 works over that local base for its normalized tensors, then applies the rational central Schur projector to produce an actual preimage. R-009 uses the graded algebra morphism induced by the Chow multiplication map; its product equality persists under the frame-torsor transport. R-010 is an explicit differential-operator map on the polynomial coordinate sheaf, with its written kernel vectors. These are the same maps of SGA 3 representations and EGA I scheme images, rather than dimension comparisons used in place of maps.

## Dictionary for every archive finding

| Finding and archive locus | Exact transported statement | Locator |
|---|---|---|
| A-001, 133/019 | The Burnside ring marks, rank map, and signed permutation linearization compute the displayed discrepancy; exterior/symmetric operations remain the exact-K0 operations. | SGA 6 V 2.1, 2.2.1, VI 3.3. |
| A-002, 133/006 | The rank augmentation on strict quadratic spaces in characteristic two makes the proposed exterior-square rank impossible. | Archive definition; SGA 6 V 2.1 fixes the pre-lambda identities tested. |
| A-003, 133/006 | The displayed quotient from split orthogonal group completion to the metabolic Grothendieck--Witt ring kills the computed nonzero Adams defect. The forgetful maps specify both K0 targets. | Zibrowius 2015 Def.1.2 and main theorem; SGA 6 V 2.4.1 for the identity tested. |
| A-004, 133/008 | The written bilinear isometry identifies \(q\perp(-q)\) with a hyperbolic bundle after inverting two. The characteristic-two group-scheme representation gives the precise failure of the proposed relation. | SGA 3 I 4.7.2; archive 133/008. |
| A-005, 133/008 | The natural tensor/hyperbolic isometry proves the ideal statement; the computed exterior-square image proves failure of descent through the indicated Witt quotient. | SGA 6 V 2.1; archive quotient map. |
| A-006, 133/009 | The cited injective etale-cohomology pullback to a splitting space transports the root formulas. The real Kummer class is the explicit obstruction to the struck-out descent. | Zibrowius gamma paper Prop.3.3; SGA 6 V 3.2--3.4, 3.10. |
| A-007, 133/028 | The tensor-power operation and Young induction product give the exact virtual equality; the rank-two Adams example computes the failure of an effective-summand reading. | SGA 6 V 4.2 and VI 3.3; integral completion A-012. |
| A-008, 43/037 | The series involution \(f(t)\mapsto f(-t)^{-1}\) transports the Witt conventions, with the stated Frobenius/Verschiebung identities and ghost maps. | Archive 43/037; SGA 6 V 3.2--3.4 for the related lambda-series substitution. |
| A-009, 2/017 | Restriction is pullback of representations, induction is the explicit coset tensor construction, and the written map proves projection. The coinvariant example computes loss of local freeness for an arbitrary group map. | SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| A-010, 133 and SGA 6 | The free-lambda evaluation, rank-r quotient and determinant localization are the actual universal homomorphisms; the gamma substitution computes the rank-kernel filtration. | SGA 6 V 4.2, 4.4, 4.8--4.9; V 3.2--3.4, 3.10; VI 3.3. |
| A-011, 89/018 | The exterior pairing is a morphism of rank-two locally free sheaves; the displayed reconstruction is equivalent to the zero-sum relation under its explicitly proved nondegeneracy. | SGA 3 I 4.5; archive 89/018. |
| A-012, 133/028 | The integral Cauchy filtration is equivariant and compatible with base change. Three exact torus weight extractions give the tensor identity in the declared exact equivariant K0 on every commutatively ringed topos. | ABW II.2.16 and III.1.4; SGA 3 I 4.7.3; SGA 6 VI 3.3. |

The motivic and Lefschetz expressions on the remaining archive fragments require their own definitions before a scheme or realization map can be written. They are recorded in the unresolved part; the proved Artin example G-004 supplies an actual motive and projector in its stated scope.

## Additional explicit dictionaries for the small presentations and the uniform end-row family

| Finding | Restatement in schemes, comodules, or Schur operations, with the proof-carrying map | Framework locator |
|---|---|---|
| T-021 | Pullback of the coefficients of a product of four binary linear forms sends the quartic coefficient \(x_i\) to \(\binom4i^{-1}\sum_{|I|=i}\prod_{j\in I}b_j\prod_{j\notin I}a_j\). The resulting highest-weight coordinate algebra is the stated kernel of the locally nilpotent derivation, presented by \(T^2+4H^3-f^2HI+f^3J=0\). The localization and modulo-\(f\) injection in the proof establish the actual scheme-coordinate isomorphism. | EGA I 9.5.1–9.5.3; SGA 3 I 4.7.2. |
| T-022 | The monic equation gives a free module with basis \(1,T\) over \(\mathbf Q[f,H,I,J]\). Its two degree equations are exactly the two polytope systems, so the Schur coefficient is the corresponding graded rank. | SGA 3 I 4.7.3; SGA 6 VI 3.3. |
| T-023 | The specified weighted initial monomials define a subalgebra degeneration with the proved semigroup basis; the cusp equation is its initial relation. The exact basis correspondence proves flatness over the degeneration parameter and preserves each multigraded rank. | EGA I 9.5.3; the Rees construction and monomial independence are proved in T-023. |
| T-024 | The flag-face map is the affine incidence morphism with coordinates \(x_i,y_i,z\), relation \(\sum x_iy_i=0\), and determinant-one torus quotient \(\mathbf Q[u,v,z,t_i]/(\sum t_i,uv-\prod t_i)\). Literal row permutations give the recorded signed action. The dense incidence chart proves the kernel, rather than inferring an algebra from equal dimensions. | SGA 3 I 4.7.2–4.7.3; EGA I 9.5.2–9.5.3. |
| T-025 | The alternating-group quotient is a quadratic discriminant algebra with basis \(1,D\). Taking the remaining involution's eigenspaces selects the written parity of the standard monomials. Their weight equations reduce bijectively to \(\sum_{i=2}^m ic_i=R\), giving the indicated Schur-sheaf multiplicity and its exact support. | SGA 3 I 4.7.3; SGA 6 V 4.2 and VI 3.3. |
| T-026 | The weighted discriminant relation gives a monic quadratic Rees family, free with basis \(1,D\). The explicit rational rescaling turns the special fiber into the displayed binomial semigroup algebra. Taking the diagonal order-two invariants preserves the written parity basis and flatness over the localized integral base. | EGA I 9.5.3; SGA 3 I 4.7.2. |
| T-027 | Multiplication by \(u^{(n-\beta)_+}v^{(\beta-n)_+}z^\gamma\) identifies the balanced comodule with \(\operatorname{sgn}^{\beta}\otimes\operatorname{Sym}^{S}\mathfrak h_m\), where \(\mathfrak h_m\) is the quotient of the permutation bundle by its constant line. Taking the \([\mu]\)-covariant summand and computing its cycle traces gives the tableau generating function. | SGA 3 I 4.7.2–4.7.3; SGA 6 VI 3.3. |
| T-028 | The assignment matrix, descent variables, and partition variables have a proved one-to-one correspondence with the tableaux and partitions in that character formula. Hence the same covariant module has rank equal to the one explicitly described lattice count. The minimum and next graded terms yield the exact support criterion. | SGA 3 I 4.7.3; SGA 6 V 4.2. |
| T-029 | Each partial-flag face is an affine graded subalgebra. Inverting its invariant product of selected minors produces an explicit Laurent-polynomial algebra over its torus quotient. Its dimension, and the restriction of a finite homogeneous normalization to every face, force the negative integer \(c_{\{1,2,m-1\}}=2-m\). Thus the specified finite polynomial-subalgebra morphism cannot exist for the full highest-weight grading. | EGA I 9.5.3 for the affine algebra correspondence; SGA 3 I 4.7.3 for torus comodules; all dimension and face arguments are proved in T-029. |
| T-030 | The \(\omega_2\) face is the Plücker quadric. Its torus quotient is the trace-free matching plane with a determinant coordinate; the quotient homomorphism \(S_4\to S_3\) and the displayed alternating-form intertwiner identify every outer character. Its invariant affine scheme has equation \(27W^2+Z(D^2+4e^3)=0\). | SGA 3 I 4.7.2–4.7.3; SGA 6 VI 3.3; EGA I 9.5.3. |
| T-031 | Complementary-column exterior multiplication gives the perfect pairing into \(\det^H\); it transports the finite permutation projector with the exact sign twist. Multiplication by \(\prod_{i<j}[ij]\) gives the binary exterior-to-symmetric sheaf isomorphism, including determinant power \(\binom m2\). These two morphisms carry the proper-face formulas to the quartic presentation. | SGA 3 I 4.5 and 4.7.2; SGA 6 VI 3.3. |

## Additional dictionaries for canonical images and rectangular comparisons

**G-013.** The affine diagram \(j\Pi_a=\Pi_b\iota\) is defined by multiplication of forms and appending fixed basis forms. Its coordinate pullback is precisely \(h_{b,a}\operatorname{Sym}^b(j^*)=\iota^*h_{b,b}\). Block determinant evaluation takes the normalized square section to \(I_{a,b}\). Multiplication in the image coordinate ring then realizes every printed seed expression. The Apéry paths specify the exponents of actual preimage sections. The rational denominators specify a localization of \(\mathbf Z\) for each section. This is the scheme-image construction of EGA I 9.5.1–9.5.4 and the associated-representation construction of SGA 3 I 4.7.2; its Schur coefficient lies in the representation \(K_0\) of SGA 6 VI 3.3.

**G-014.** On the principal open where the pure-power Chow coefficient is invertible, the ordered-factor coordinates give the multisymmetric chart. The polynomial identity \(\mu_a(C_\beta)=uE_\beta\) and the degree-tracked homogenization prove equality of the image and normalization on each component with \(an-\lambda_1\le n\). This is a precise graded coordinate-ring statement; applying the Schur coefficient functional gives the canonical-map rank. The adjoint tensor projections give the stated isomorphism on the common first-row range. The relevant affine and representation locators are EGA I 9.5.2–9.5.3, SGA 3 I 4.7.2–4.7.3, and SGA 6 VI 3.3.

**R-011, R-012, and R-015.** Each common-polarization operator is a natural morphism of polynomial representation bundles. Its integer highest-weight presentation is specified by flag-minor Reynolds vectors. A nonzero minor of its evaluated image matrix modulo the displayed prime is a nonzero integral minor and therefore proves the asserted generic-fiber injectivity. The certificate lists every source multiplicity, so the argument covers the entire source functor. In the language of determinantal ideals, these computations exhibit the required nonzero minors of each finite multiplicity map; the exact general locators are Stacks 07Z6, Lemmas 15.8.2 and 15.8.4, and 05P8, Lemma 31.9.6. The bundle transport is SGA 3 I 4.7.2.

**R-013.** The morphism \(\nu_{L,b}:(\ell,q)\mapsto\ell^Lq\) is an integral affine-scheme morphism. Its degree-\(r\) coordinate pullback equals \(\binom bL^{-r}T_{r,L,b}\) over \(\mathbf Q\), with the scalar proved on pure products. The kernel is the degree-\(r\) ideal of the scheme image by EGA I 9.5.2. Multiplication in the ambient polynomial domain transports the certified vanishing to every lower degree. The cited Kadish–Landsberg Theorem 1.7 and its section 3 proof provide the known geometric map; the stated finite boundary kernels and scalar convention are evaluated here.

**R-014.** Padding and determinant realization give the actual inclusion \(\Gamma_n^M\hookrightarrow\mathrm{Det}_M\), hence the equivariant surjection of coordinate rings. The cited highest-weight padding injection and the stable rectangular-Kronecker identification transport this through the finite chain written in R-014. The end-row lattice count then gives an explicit effective lower bound in the representation Grothendieck group. The geometric framework is EGA I 9.5.2 and SGA 3 I 4.7.2, with the exact Ikenmeyer–Panova locators Proposition 2.6(b), Lemma 2.7, Proposition 2.8, and Theorem 2.1.

## Additional dictionaries for the recovered archive statements

| Finding and archive locus | Geometric or exact-K0 restatement and the actual comparison | Exact locator |
|---|---|---|
| A-013, 133/024–029 and supplied study | Injection powers and kernel partitions give explicit isomorphisms of finite-set-valued functors; composition and finite limits are computed by the written maps. The two-copy constant functor evaluated at a singleton disproves the single-power summand assertion. Applying the constant finite-scheme functor preserves the specified maps and products. | Archive 133/024–029; SGA 3 I 4.5 for the associated constant actions. |
| A-014, 4/007 | The two chain maps between the de Rham complex and \(\mathcal O\) have Frobenius composites. Passing to the Fitting-stable images gives their stated inverse. On a finite free Witt-vector lattice, Hensel separation of unit roots computes the stable reduction. The crystalline freeness and algebraicity inputs explicitly admitted in the original pages remain the exact application gates. | Original cote4, PDF pp3–7, §§8.3–8.5; Weil II 1.2.1–1.2.5 gives the weight terminology, not those missing crystalline inputs. |
| A-015, 133/006 | The integral universal iterate polynomial is evaluated on the concrete modular orthogonal representation. Its nonzero defect in the split group completion maps to zero under the specified metabolic quotient. | SGA 6 V 2.4.1, 2.4.2; archive category and quotient in A-003. |
| A-016, 16/038 | On the explicitly defined graded primitive-string modules, restriction and pushforward act by truncation and shift. The corrected projector identities hold on every displayed basis vector. For \(\mathbf P^1\) and a point, the actual cohomological maps refute the source's final projected equality. No algebraic-motivic realization of an unstated lowering operator is inferred. | Original cote16 PDF pp33–38; SGA 5 III 3.1–3.3 for the correspondence-to-cohomology construction. |
| A-017, 79/051 | Exterior multiplication of a rank-two \(\mathbf Z/n\)-module descends through the sign quotient. The identity \(\Lambda^2(a\,\mathrm{id})=a^2\mathrm{id}\) transports edge and face types. The wedge tests and the \(n=4\) calculation prove the stated recovery maps. These finite sets and maps may be represented as constant finite schemes; the reconstruction from one unlabeled complex remains separately recorded. | Original cote79 PDF pp47–51, (114)–(127); SGA 3 I 4.5 and 4.7.2. |
| A-018, 43/037 | A morphism from \(\operatorname{Spec}\mathbf Z[a_1,a_2,\ldots]\) depends on finitely many coordinates of each target function. Pullback along products of the universal line series sends \(a_i\) to the elementary symmetric polynomial \(e_i\); its proved injectivity forces equality of the two affine group-scheme morphisms. | Archive 43/037; EGA I 9.5.3 for the affine coordinate dictionary; SGA 6 V 4.2 for the universal symmetric-operation algebra. |
| A-019, 133/008 | The hyperbolic summand has a nonsingular polar form in every characteristic. The cited field cancellation isometry removes that actual summand and identifies the remaining form with the hyperbolic form of the dimension difference. | Elman–Karpenko–Merkurjev §8, Lemma 8.2 and Theorems 8.3–8.4, pp47–48; archive 133/008. |
| A-020, 133/028–029 study | The composition-factor homomorphism identifies exact \(G_0\) over \(\mathbf F_p\) with the free group on the absolutely simple modules. The decomposition matrix relates the Specht reductions to the simple labels; its rank at degree \(p\) is the proved modular obstruction to a polynomial induction ring on all \(\rho_i\). | James Theorem 11.5, p40; Corollaries 12.2–12.3, pp42–43; SGA 6 VI 3.3 for exact representation K0. |
| A-021, 133/028–029 study | Rationalization of finite locally free representations over a characteristic-zero DVR induces an isomorphism of exact representation groups, proved through the torsion boundary and commensurable lattices. It commutes with the actual tensor and induction functors, yielding the stated polynomial graded ring. | James 8.4, 8.6–8.11, 11.5, 12.2–12.3; SGA 3 I 4.7.2; SGA 6 VI 3.3. |
| A-022, 133/009 and study | The nonisotropic-line pullback is injective on mod2 étale cohomology. Its actual symmetric-line summand and Kummer connecting map give \(w_2(H(L))=\bar c_1(L)\). The iterated splitting and Whitney product yield the displayed general hyperbolic formula in the proved scheme scope. | EKV Lemma 5.3 and Proposition 5.5, pp181–184; Zibrowius gamma paper Proposition 3.3, pp19–20; SGA 6 V §3 for the gamma-filtration comparison. |
| A-023, 133/028–029 study | Over the explicit local scheme \(\operatorname{Spec}(\mathbf Z_{(2)}[\varepsilon]/(2\varepsilon,\varepsilon^2))\), the rank-one constant-\(C_2\) comodule has character \(1+\varepsilon\). The determinant functor on exact sequences detects its class outside the subgroup generated by the two degree-two \(\rho\)-monomials. Rational base change kills \(\varepsilon\), so the exhibited class difference also lies in the kernel of rationalization. | SGA 3 I 4.7.2 for constant-group comodules; SGA 6 VI 3.3 for the exact representation group; the complete ring and determinant calculation is A-023. |

## Étale and correspondence locators used in the transport

For A-009, SGA 4, Exposé IV, **4.5.1** gives the restriction and induction morphisms of classifying topoi induced by a group homomorphism; **4.5.2** records the profinite version. The explicit coset tensor map in A-009 is the corresponding locally free representation calculation. These passages were opened and read, rather than inferred from the title of the exposé.

For G-004 and the realized cohomological examples of A-016, SGA 5, Exposé III, **3.1**, equations **(3.1.1)–(3.1.3)**, defines a cohomological correspondence; **3.2(b)(i)–(ii)** gives the diagonal and Frobenius-graph examples; **3.3**, equation **(3.3.3)**, gives its action on cohomology. The Artin projectors of G-004 are \((1\pm F)/2\) after passing to rational \(\ell\)-adic coefficients. Their finite étale realization and weight-zero eigenvalues are explicit. The projectors' ranks follow from the action on that two-dimensional space; no mod2 projector with denominator two is asserted.

## Exact dictionaries for the general chart, chamber sheaves, and truncation

**T-032.** The balanced diagonal-torus comodule algebra is localized at the explicit invariant section \(u=\prod x_i\). Its coordinate homomorphism sends each flag minor to \(u\mathbf1\wedge\bar w_2\wedge\cdots\), and the prescribed centered-matrix construction proves the inverse on the principal open. The extension subspace is the ideal-divisibility condition \(u^k\mid F(v(X))\) in the original affine coordinate ring. This is an explicit isomorphism of affine schemes with constant symmetric-group action (EGA I 9.5.3; SGA 3 I 4.7.2–4.7.3). Its Schur-coefficient functor is the corresponding exact representation-group functional in SGA 6 VI 3.3.

**T-033–T-034.** The homomorphism \(S_4\to SO(W)\), with \(W=\mathfrak h_4\otimes\operatorname{sgn}\), is specified by the invariant form and determinant-one row-permutation action. Restriction of the Schur comodule, the harmonic quotient by that form, and the explicit five character projectors give the finite polynomial counts. The complementary-column pairing transports the upper chamber with its computed determinant character. These are restriction and direct-summand morphisms of the SGA 3 I 4.7.2 representation category; their graded classes and exterior determinant operations are those of SGA 6 VI 3.3. The Elliott character calculation is proved in full in T-033, including the required intertwining action.

**T-035–T-036.** The affine incidence presentation yields the flag scheme \(\mathcal F\subset\mathbf P(W)\times\mathbf P(W)\) and its projective-line-bundle morphism \(\pi\). The exact coordinate equations identify each original divisor valuation with the order in the pulled-back ideal of one of four specified points. Thus the balanced comodule is the global-section representation of \(\pi^*\mathcal I_Z^k\otimes\mathcal O(c,b)\), with the printed determinant character. The two-quadric ideal resolution and the tautological quotient sequence calculate those sections, including the nonzero first-cohomology summand in T-036. The group-equivariant splitting is obtained by averaging an actual linear projection. These affine, ideal-sheaf, and locally free sheaf maps provide the full geometric restatement; the associated representation and K0 maps are SGA 3 I 4.7.2 and SGA 6 VI 3.3.

**R-016.** The normalized pullback of R-013 identifies each of the three computed kernels with the degree component of the ideal sheaf of the padded-form scheme image. Every source summand is listed; the selected nonzero minors prove the ranks and the displayed determinant polynomial supplies the entire missing irreducible summand. The scheme-image interpretation is EGA I 9.5.2, with the same determinantal-ideal maps already specified for R-015.

**R-017–R-018.** Separate homogenization and first-coordinate restriction are inverse maps between the indicated degree-bounded polynomial spaces. Coefficient extraction becomes the explicitly diagonal truncation operator with weights \(\prod_i\binom{b-d_i}{L}\). The flag-minor generators bound each block degree by the second row. Inverting those actual nonzero weights proves injectivity on the specified entire Schur-isotypic components, and applying each finite-group projector preserves it. Via R-013 this is the vanishing of precisely the indicated graded ideal components of the padded-form scheme image. These are equivariant coordinate-sheaf maps under EGA I 9.5.2–9.5.3 and SGA 3 I 4.7.2–4.7.3; their exact Schur operations lie in SGA 6 VI 3.3.

## Five-point modules and the complete four-point formula

**T-037.** The exact four-point incidence quotient is free over the polynomial algebra of its two quadratic generators through the averaged multiplication section. The two-quadric power resolution and tautological quotient sequence identify ordinary powers with the required flag sections in the proved degree range; the boundary correction is the displayed connecting cohomology module. The explicit complementary pairing and sign twist transport the resulting positive modules to every balanced Schur weight. These are ideal-sheaf, associated-bundle and exact-representation maps in EGA I 9.5.1–9.5.3, SGA 3 I 4.7.2–4.7.3 and SGA 6 VI 3.3.

**G-015–G-016.** The general balanced chart identifies extension across each original coordinate divisor with the ordinary power of a smooth flag fiber's ideal. Its leading normal ratios are independent over the fiber function field, including every higher Plücker frame. The point-ideal generators and canonical affine evaluation maps identify the saturated projective-frame scheme and its actual permutation quotient. The schemes and coordinate maps are the EGA I 9.5.1–9.5.3 constructions; the linearized flag line bundle is transported by the SGA 3 associated-bundle map, and its Schur class is the SGA 6 VI 3.3 operation. The exact Schur/section locator used is Magyar, Proposition1 pp5–6 and Proposition4(a)–(c) p10.

**T-038, A-028–A-029.** The five-point ideal has the written equivariant alternating resolution. Its actual quadratic image is the displayed cubic hypersurface, with the precise six-letter intertwiner. The Cox comparison sends exceptional sections and each Plücker bracket by (Cox.1), and identifies every Picard-graded section by the normal-order calculation. The ordinary Rees map is the specified inclusion into that Cox ring. Applied Kustin–Polini–Ulrich formula6.1.4 and Lemma6.3/Corollary6.4 give the linear-power complexes after every local hypothesis is checked. Saturation and cohomology follow from those complexes. These are concrete graded scheme and coherent-sheaf morphisms under EGA I 9.5.1–9.5.3; the flat-family Hilbert/Quot interpretation is FGA Exposé221 Theorems3.1–3.2. No new generic-position assertion is used.

**G-017.** The polynomial matrix (Q.9) presents the actual quotient-bundle section module. Its determinant, adjugate and generic evaluation prove an injection; the established ideal-power cohomology proves surjectivity degree by degree. Four explicit invariant parameters are regular by the determinant argument, and averaging a graded section gives the actual free multiplication isomorphism (Q.21). The corresponding coefficient is the constant-group covariant summand of the geometric module, carried by G-015 and T-003. The exact K0 operation is SGA6 VI3.3, and all determinant dualities are specified exterior pairings of locally free sheaves.

**G-018.** The dual tautological inclusion and linear multiplication identify the exterior quotient module with the concrete kernel (W.6). Stabilizer-invariant affine charts give the entire fat-point jet action, including its line-bundle trivialization. The finite Newton count is the exact rational character identity of that kernel. The EGA coherent sheaf, SGA3 comodule and SGA6 exterior-operation maps are precisely those just specified.

**G-019 and T-039.** The symmetric quotient sequence (SQ.4) is locally split before tensoring the ideal. Its global cohomology gives the exact representation-K0 formula, including the one nonzero connecting term at point order1. Relative exterior pairings give the determinant character in (SQ.3). Its fixed bivariate positive formula therefore computes Schur-operation multiplicities of actual ideal-twisted flag sections. The transport uses SGA3 I4.7.2–4.7.3 and SGA6 V4.2,4.4,4.8–4.9,VI3.3, with the projective-family interpretation of FGA221 Theorems3.1–3.2.

**T-040.** The degree-one Rees component has the explicit B-matrix resolution. The tautological inclusion into its tensor product with E gives the displayed quotient, whose full free resolution is verified by the rank-three reduction modulo the cubic. This supplies the actual module behind the positive residue formula. Its four-parameter obstruction is proved by the exact multiplication-sequence Hilbert series, which would have a negative finite quotient coefficient. The ordinary-power, saturation and quotient maps specify the geometric comparison.

**T-041.** The hook Schur functor is the kernel of the split symmetric multiplication map. The explicit two-step tautological hook resolution and its top-Cech identity prove all needed cohomology groups. Multiplication by the five quadrics is the actual section isomorphism (5H.12). These kernel, exterior-complement and symmetric operations are the locally free Schur operations transported in SGA6 VI3.3.

## Further actual canonical-image dictionaries

**R-019–R-020.** Complementary column pairings identify the entire first-row source band with a multilinear symmetric-group component. The explicit cofactor highest vector and nonzero coefficient prove the actual polarization rank. Through the padded-form scheme-image map R-013, this removes precisely those graded ideal components. The transport is the EGA I9.5.2 scheme-image coordinate map and the SGA3/SGA6 associated Schur-sheaf map.

**R-021.** The block specialization and multiplication in the graded Chow coordinate algebra carry prime-adjacent square determinant preimages to every stated rectangular and row-extended preimage. Nagura's exact prime interval determines the nonnegative exponents. Thus the nonzero coordinate section is in the actual canonical image; its determinant and highest-weight lines are the specified Schur operations in SGA6 VI3.3.

**R-022–R-024.** Normalized last-slot polarization sends the Chow image annihilator into the exact common-polarization kernel or into the lower-degree annihilator via (P.11). Slot transvections prove the rectangular prolongation equality, and the actual determinant preimage removes that summand. The two Pieri inclusions then prove the stated whole-isotypic vanishing of the graded ideal, including every multiplicity. These are maps of coordinate modules of the scheme image in EGA I9.5.2, transported to associated Schur sheaves by SGA3 I4.7.2 and SGA6 VI3.3. The degreewise minors give their rank strata as in the G-002 determinantal dictionary.

## All nonnegative five-point twists and the next canonical components

**G-020, T-042–T-043.** The locally split symmetric or hook quotient
complex, tensored with the specified ordinary ideal power, computes
its actual direct-image representation including every low-degree
cohomology term. The exact fat-point evaluation identifies each class
trace. The residue constants are therefore Schur-operation coefficients
of the displayed sheaf classes, and the subset-chain bijections convert
them into positive lattice counts. Their map locators are SGA 3 I
4.7.2–4.7.3, SGA 6 V 4.2,4.4,4.8–4.9 and VI 3.3; the underlying
coordinate and ideal morphisms are EGA I 9.5.1–9.5.3. Relative exterior
pairings specify every determinant character. The FGA Exposé221,
Theorems3.1–3.2 interpretation uses the same finite graded modules in
families, with the denominators of the characteristic-zero projectors
retained.

**G-021.** The signed tensor differential (S.1) and the rational Young
idempotent define an actual complex of locally free sheaves. The
specified rational intertwiners identify its terms with the three Schur
bundles in (TR.5), and the averaged local contraction proves exactness
after ideal tensor. Its derived direct image is concentrated in degree
zero in the proved range. Thus (TR.8) is its class in the exact
representation group of SGA 6 VI 3.3, transported by the frame torsor
of SGA 3 I 4.5,4.7.2. The exact Schur-section dictionary is Magyar,
Propositions1 and4, with the relative dual pairing in (TR.3). The
finite coefficientwise inequalities and polytope bijections calculate
this same class; they introduce no unstated realization functor.
The multiplication by \(u^e\) and perfect exterior pairing (TR.19)
carry the result to both outside regions. These are concrete maps of
the EGA I 9.5.3 coordinate representations. In the archive language,
they evaluate the Schur compositions and tensor operations of cote133,
scans024–029, through the universal operation map of A-010 and A-012.

**R-025–R-026.** The determinant and signed cofactor formulas are
integral highest sections in the ordered-factor coordinate ring. Their
specified column averages descend to symmetric sections. The exterior
complement pairing computes the entire one-dimensional Schur
multiplicity space. Normalized slot splitting and coefficient
polarization send the actual scheme-image annihilator into the lower
common kernel. The nonzero factorial coefficients, including the exact
apolar differential pairing in BS.28–31, exclude the unique indicated
component from that annihilator. Hence these are computed ranks of the
graded coordinate-image morphism in EGA I 9.5.2, and positive Schur
summands in its SGA 6 VI 3.3 representation class. Scalar extension in
the endpoint uses the injective field map to the displayed splitting
field and is explicitly reflected in its integral polynomial identity.


\part{Source register and verification}


# Verified source locators for the archive and geometric dictionaries

Run `/root/archive_audit`; model GPT-6 Astra Pro; effort not exposed. This document records source inspection, not an independent reproof of every cited theorem. Archive evidence consists of the supplied TeX transcriptions. No manuscript scan images or Lean files were supplied.

## Archive and supplied secondary material

All thirteen `ARCHIVE_*.tex` and all of `SA17_STUDY_cote133_lambda.md` were read. The report preserves the difference between transcribed statements, transcription uncertainty, supplied study additions, and current-run arguments. In particular, the study's alleged equivariant finite-set check on 133/019 is refuted in A-001. No claim about scans merely mentioned in the study is treated as a new scan inspection.

## SGA 6: exact K theory, exterior operations, and the free λ-ring

Bibliography: P. Berthelot, A. Grothendieck, L. Illusie, with collaborators, *Théorie des intersections et théorème de Riemann–Roch*, SGA 6, Lecture Notes in Mathematics 225, Springer, 1971.

| Locator | Statement used | Inspection |
|---|---|---|
| Exposé V, Definition 2.1 | Pre-λ definition | French mathematical transcription inspected |
| V, Lemma 2.2.1 | Exterior-power filtration for short exact sequences | Exact citation confirmed in Zibrowius 2016, Lemma 2.2 |
| V, 2.4.1 | Universal product and iterate identities | Exact citation confirmed in Zibrowius 2015, §3.1 |
| V, 3.2–3.4 | γ substitution and equivalent formulas | French mathematical transcription inspected |
| V, 3.10 | γ filtration | French mathematical transcription inspected |
| V, Proposition 4.2; Definition 4.4 | Unique evaluation of the free λ-ring | Statement and proof text inspected |
| V, Proposition 4.8; Corollary 4.9 | Finite-rank quotient and its λ-ideal | Statement and proof text inspected |
| V, §6 | Chern-ring universal construction | Section located; entire proof not independently rederived |
| VI, Theorem 3.3 | λ structure on exact K₀ of a locally ringed topos; transfer via frame torsors | Theorem and proof transcription inspected, exact locator corroborated in Zibrowius 2015 p.1057 and 2016 §2.2 |

Inspected transcriptions: https://grothendiecksga.com/read/sga6/fr/V-3.html ; https://grothendiecksga.com/read/sga6/fr/V-4.html ; https://grothendiecksga.com/read/sga6/fr/VI-3.html . Local HTML/text copies are in this directory. The attempted original scan download from `iut-theory.org` returned HTTP 503. The paper must not say the original SGA 6 scan was visually inspected.

## Zibrowius: precise quadratic-form quotient and splitting

Marcus Zibrowius, *Symmetric representation rings are λ-rings*, New York J. Math. 21 (2015), 1055–1092. Primary PDF: https://nyjm.albany.edu/j/2015/21-49v.pdf .

- Main theorem, p.1056: special λ structure on the Grothendieck–Witt representation ring defined with metabolic relations.
- Lemma 1.1, p.1059: the natural hyperbolic isometry for a symmetric object and its negative, with 2 invertible.
- Definition 1.2, p.1060: the exact K₀ relations and, explicitly, the additional relation `[M]=[H(L)]` for metabolic `M` with Lagrangian `L`.
- §3.1, pp.1068–1069: universal special-λ identities and their SGA 6 locator.

Marcus Zibrowius, *The γ-filtration on the Witt ring of a scheme*, arXiv:1411.3198v2, submitted 11 August 2016, title-page date 12 August 2016. Primary PDF: https://arxiv.org/pdf/1411.3198 .

- Theorem 2, displayed p.3, and Theorem 2.5, displayed p.11: schemes over a field of characteristic different from two.
- Proposition 2.15, displayed pp.17–18: orthogonal torsors carrying pairs of symmetric bundles.
- **Proposition 3.3, displayed pp.19–20: the preceding sentence explicitly says “any scheme over Z[1/2]”.** This proposition supplies a morphism that splits the given symmetric bundle into symmetric lines and induces an injection on étale cohomology with Z/2 coefficients. Its scope is broader than Theorem 2. The report's scheme-over-Z[1/2] scope is verified.
- Proposition 4.8, displayed p.23: again explicitly over Z[1/2], consistent with that broader splitting scope; not needed for our main argument.

## Macdonald: symmetric functions and Schur–Weyl

I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, second edition, Oxford, 1995. Primary book PDF inspected: https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf . Local copy `Macdonald.pdf` and extracted text `Macdonald.txt`.

| Locator and printed page | Exact role |
|---|---|
| I (4.2), p.62 | Cauchy kernel expanded as the sum of monomial times complete symmetric functions |
| I (4.3), p.63 | Cauchy kernel expanded as the sum of Schur times Schur functions |
| I (7.3), pp.113–114 | Frobenius characteristic is an isometric graded-ring isomorphism; its proof sends induced trivial Young modules to `h_ν` |
| I (7.5)–(7.6), p.114 | Irreducible character basis maps to the Schur basis |
| Appendix A (5.3)–(5.4), p.155 | Homogeneous polynomial functors from symmetric-group modules and the characteristic-zero equivalence |
| Appendix A (5.6), p.156 | Functorial tensor-power decomposition `Tⁿ(X)=⊕M_λ⊗F_λ(X)` |
| Appendix A (7.2), p.160 | Character of the irreducible polynomial functor is `s_λ` |
| Appendix A (7.4), p.160 | Nonnegative integral Schur coefficients for Schur plethysm through functor composition |

These numbered statements were inspected in the primary PDF, including the previously pending Appendix A (5.6). The PDF's page index is printed page plus 10.

## Akin–Buchsbaum–Weyman: the integral Cauchy filtration

K. Akin, D. A. Buchsbaum, J. Weyman, *Schur functors and Schur complexes*, Advances in Mathematics 44 (1982), 207–278, DOI 10.1016/0001-8708(82)90039-1. The author's current research page is https://jerzyweyman.webflow.io/research/schur . Its linked original paper was downloaded completely from https://cdn.prod.website-files.com/69c19dc391eb37d617c813ce/69cc3be3405f5e9e171b7db4_JW%231_Schur.pdf and retained as `ABW1982.pdf`, with extracted text `ABW1982.txt`.

- Theorem II.2.16, printed p.232: the universal standard-tableau basis for a Schur module, proving freeness and compatibility with arbitrary scalar extension.
- Theorem III.1.4, printed pp.245–246: the natural integral filtration of a symmetric power of a tensor product, with tensor products of Schur modules as its associated graded.

The paper's indexing uses `L_(a)=Λᵃ`. A-012 explicitly defines `S_λ^int=L_(λ′)` to translate its convention to the archive's usual Schur partitions. Three exact torus-weight extractions from this one filtration prove the arbitrary-characteristic tensor-power formula, including its virtual exact-K₀ extension. The source theorem is carried as verified background; A-012's deduction is independently checked in full.

## Witt vectors and Borger

Michiel Hazewinkel, *Witt vectors. Part 1*, primary author PDF: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Hazewinkel-Witt.pdf .

- §§14.1–14.4, pp.71–72: big Witt operation polynomials in coordinate `n` involve only divisor coordinates. The resulting `p`-power coordinate polynomials define the `p`-typical Witt ring functor and the natural quotient from the big Witt functor.
- Definition 14.5 and §14.8, pp.72–73: divisor-stable index sets (“nests”) and their Witt functors.
- §14.15, equation (14.16): canonical big-to-typical projection. No `p`-local hypothesis is needed for the quotient. The stronger decomposition involving sections later in §14.21 uses `p`-local rings and is not invoked here.

James Borger, supplied `lrfoe13.tex`, §§1.1–1.2 and §2.2, inspected in the input file. The first locators give the free λ-ring, arithmetic jet-space, and Witt-space adjunction framework; §2.2 gives monoidal Frobenius lifts. The report verifies the explicit character-ring map `ψᵖ f(x)=f(xᵖ)` and its congruence modulo `p` directly.

## EGA I: schematic image

A. Grothendieck and J. Dieudonné, *Éléments de géométrie algébrique. I. Le langage des schémas*, Publ. Math. IHÉS 4 (1960), 5–228. Primary original PDF downloaded completely and its text inspected: https://www.numdam.org/item/PMIHES_1960__4__5_0.pdf . Local copies `EGAI.pdf`, `EGAI.txt`.

| Locator and printed page | Exact role |
|---|---|
| Proposition 9.5.1, p.176 | Existence of a smallest closed subprescheme through which the morphism factors when direct image of the structure sheaf is quasi-coherent |
| Corollary 9.5.2, p.176 | The defining ideal is `ker(O_Y→f_*O_X)` |
| Definition 9.5.3, p.177 | Names that closed image |
| Proposition 9.5.4, p.177 | Its underlying space is the closure of the image |
| Proposition 9.5.8, p.178 | Formation commutes with restriction to an open of the target; the following paragraph points forward to flat base change |
| Proposition 9.5.9, p.178 | Reducedness and irreducibility/integrality pass to the closed image in the stated range |

For the parent's affine morphism `μ:Spec B→Spec C`, the actual algebra map `C→B` identifies the closed image with `Spec(C/ker μ*)=Spec(im μ*)`. Affineness gives the required quasi-coherence directly. The elementary tensor-exactness proof gives compatibility with a flat extension of scalars in this affine case; no unverified global EGA base-change number is required.

## FGA: Quot and Hilbert

A. Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique. IV. Les schémas de Hilbert*, Séminaire Bourbaki, exposé 221 (1960–1961), pp.249–276 in the Numdam collected pagination. Primary PDF inspected: https://www.numdam.org/item/SB_1960-1961__6__249_0.pdf .

- Theorem 3.1, printed p.259 (PDF index 11): Quot represented by a disjoint sum of projective schemes in the setting stated there.
- Theorem 3.2, printed p.260 (PDF index 12): the fixed-Hilbert-polynomial Quot piece is projective.
- Following Proposition 3.8, printed p.265 (PDF index 17): `Quot(O_X)` is the Hilbert functor representing flat families of closed subschemes.
- Remarks 3.9, printed p.266: reduction used for projective schemes over Z.

## Fitting ideals: verified alternative locator, no invented EGA citation

The requested exact EGA locator for the determinantal/Fitting formulation was not established in this run. The precise primary reference inspected is the Stacks Project, Section 15.8, tag `07Z6`: Lemma 15.8.2 defines the presentation-independent ideal of minors; Definition 15.8.3 names it; Lemma 15.8.4(3) proves arbitrary scalar-extension compatibility. https://stacks.math.columbia.edu/tag/07Z6 . For locally closed constant-rank strata, Lemma 31.9.6, tag `05P8`, supplies the sheaf statement: https://stacks.math.columbia.edu/tag/05P8 .

In the parent's explicit matrix model, all claims about a rank bound are proved directly by the vanishing/nonvanishing of minors. Those proofs do not require an inaccurately numbered EGA theorem.

## SGA 3: the group scheme and comodule dictionary

M. Demazure and A. Grothendieck, *Schémas en groupes*, SGA 3, Exposé I, by M. Demazure. The primary editor-maintained PDFs were located and inspected: https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp1.pdf (original text in the editor's typesetting, carrying the original marginal pagination) and https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp1-13oct24.pdf (corrected edition of 13 October 2024).

- I §4.5, original marginal p.29: constructs the classical general linear group by the determinant-open coordinate algebra. An earlier tentative §4.6 locator is corrected to **§4.5**.
- I Definition 4.6.1 and 4.6.3: the `V(F)` and `W(F)` module functors, with the former represented by `Spec Sym F`; EGA II 1.7.8 is explicitly cited for this representing scheme.
- I Proposition 4.7.2, original marginal pp.34–35; corrected edition displayed pp.29–30: a group action is a coaction `F→F⊗A(G)` satisfying the counit and coassociativity diagrams. This identifies representations with comodules and supplies the precise dictionary for integral polynomial representations.
- I Proposition 4.7.3, original marginal pp.35–36: diagonalizable-group actions correspond to weight gradings, by the orthogonal projectors given by coefficient extraction in the group algebra.

No manuscript scan inspection is implied by these typeset primary editions.

## Weil II: purity for the finite étale sign example

P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHÉS **52** (1980), 137–252; DOI 10.1007/BF02684780. Primary original scan inspected at https://publications.ias.edu/sites/default/files/Number40.pdf . The IAS landing-page metadata says volume 42; the correct journal volume is 52, as recorded by Numdam and the DOI.

- Definition 1.2.1 and Definition 1.2.2, printed p.153 (PDF index 16): numerical weights and pointwise purity of a sheaf.
- Variants 1.2.3–1.2.4, p.154: terminology for Galois representations over a finite field and vector spaces with Frobenius.
- Stability 1.2.5(i), p.154: pointwise pure sheaves of a fixed weight are stable under subquotients and finite direct image.
- §1.1.7, pp.150–151: geometric Frobenius is inverse to the field's power Frobenius, and the finite-field sheaf/continuous-Galois-representation equivalence is spelled out.

The sign summand of the degree-two finite étale permutation representation has geometric Frobenius `−1`; every complex conjugate has absolute value one. This directly verifies weight zero from the cited definitions. It also follows from the finite-direct-image and subobject assertions in 1.2.5(i). No general cohomological purity theorem is needed for that example.

## Remaining historical-source gates

- Original SGA 6 scan visual verification was not completed; exact source numbering is corroborated as detailed above.
- An exact EGA Fitting-ideal locator remains unverified; the Stacks primary locators above are verified.

## Field Witt cancellation, exact scope checked

Elman–Karpenko–Merkurjev, *The Algebraic and Geometric Theory of Quadratic Forms*, AMS Colloquium Publications56 (2008), §8: Lemma8.2 and Theorem8.3 pp47–48, Theorem8.4 p48. Author-hosted PDF: https://www.math.ucla.edu/~merkurev/Book/Kniga-final/Kniga.pdf . Full proof of these three statements read; characteristic-free cancellation requires zero polar radical for the cancelled summand. This covers the hyperbolic stabilizer in original133/008. Local copies EKM2008.pdf/.txt; consequence A019 in FIELD_CANCELLATION.md.

## James: modular rank and the integral Specht lattices

G.D. James, *The Representation Theory of the Symmetric Groups*, Lecture Notes in Mathematics682, Springer,1978; DOI10.1007/BFb0067708. Public university-hosted original book scan: https://www-users.cse.umn.edu/~webb/oldteaching/Year2010-11/the-representation-theory-of-the-symmetric-groups-SLN.pdf . Local copies `James1978.pdf/.txt`.

- Theorem8.4, pp29–30: standard polytabloid basis. Corollaries8.6–8.11, pp30–31: integral coefficients/action matrices and reduction of the integral lattice to the modular Specht module.
- Definition10.1 and Lemma10.2, p36: p-regular partition labels and equality of their count with the count of p-regular conjugacy classes, by the displayed Euler-product identity.
- Theorem11.5, p40: complete simple-module list over every field, absolute irreducibility and splitting over every field. Its proof and the explicitly cited general modular-theory dependencies were read.
- Corollary12.2, p42, and Corollary12.3, p43: the p-regular Specht rows give a unitriangular decomposition submatrix. The preceding Theorem12.1 proof was read as well.

These statements supply the exact basis/absolute-base-change input for A-020 and A-021. The torsion boundary, commensurability and generator-preserving rationalization proof in `MIXED_CHAR_LATTICES.md` were checked independently. The original standard-basis page locator is29–31, rather than32–33.

## EKV: the hyperbolic characteristic-class formula

H. Esnault, B. Kahn, E. Viehweg, *Coverings with odd ramification and Stiefel–Whitney classes*, Journal für die reine und angewandte Mathematik441 (1993),145–188. Author-hosted original scan: https://page.mi.fu-berlin.de/esnault/preprints/helene/29-es_ka_vi.pdf . Local copy `EKV1993.pdf`.

- §5.1, p179: scheme over `Z[1/2]` and unimodular quadratic bundles.
- §5.2, pp179–181: the nonisotropic-line pullback and its étale-cohomology decomposition.
- Lemma5.3, pp181–182: the line-class identity `c̄₁(M)=w₁(M)²+(-1)w₁(M)`, with the Kummer/twisted-Bockstein cocycle proof.
- §5.4, p182: regularity is introduced. This hypothesis is retained when citing the following proposition.
- Proposition5.5, pp183–184: the full metabolic/hyperbolic class formula in the Chern classes of the Lagrangian. Both pages and the complete proof were visually read. The rank-two proof's integral Picard-isomorphism sentence needs qualification; A-022 gives a direct argument using injective mod2 cohomology instead.

Marcus Zibrowius, *Witt groups of curves and surfaces*, author PDF https://www.math.uni-duesseldorf.de/~zibrowius/Research/Zibrowius_WCS.pdf , §1.4, printedp8/PDFpage9, equations(6)–(8), reproduces the formula with exact reference to EKVProposition5.5. Its preceding statement explicitly discusses schemes over `Z[1/2]`. Zibrowius's gamma-filtration paper Proposition3.3, pp19–20, independently supplies the injectivity used in A-022's arbitrary-`Z[1/2]`-scheme line-bundle proof.

A-022 now proves the full hyperbolic formula over every `Z[1/2]`-scheme using that same exact injectivity result. The construction applies `P_nd` to `H(E)`; its tautological pair `(v,f)` gives the globally defined projector `z↦v f(z)/f(v)`, so `E` splits a line after this cohomologically injective pullback. Iteration and the actual orthogonal hyperbolic-sum isomorphism supply the formula. Thus no affine-bundle invariance theorem is needed for the extension.

For reference, the exact affine-space invariance locator requested during this check is **SGA4 XV, Corollary2.2**, with the meaning of acyclicity in **XV, Proposition1.6 and Definition1.7**. The French transcription of these statements was read at https://grothendiecksga.com/read/sga4/fr/XV-2.html and https://grothendiecksga.com/read/sga4/fr/XV-1.html . Corollary2.2 treats affine space over an arbitrary scheme, with torsion primes invertible on the base. No original SGA4 scan inspection is claimed for this locator check.


# Additional exact source register

The attached primary sources are inventoried and hashed in `work/source_inventory.json`. The following supplementary results were used at their stated scope. Each event in `CHECK_EVENTS.tsv` records whether the full proof, a statement, or a computation was actually checked.

| Source | Exact locator and use |
|---|---|
| Sturmfels, *Algorithms in Invariant Theory*, second edition | Theorem 2.1.4, printed p.27: finite-group Noether degree bound. Theorems 1.2.4 and 1.2.6: Gröbner bases and normal forms. Algorithm 1.4.5, printed pp.22--23: Hilbert-basis calculation. These are the finite algorithmic inputs of G-009--G-011. |
| Bruns--Gubeladze--Trung, *Problems and algorithms for affine semigroups*, arXiv:math/0101116v4 | Proposition 2.1.1(a): the affine-semigroup finiteness input used for the balanced monoid. |
| Pak--Panova--Swanson, *A combinatorial interpretation for certain plethysm and Kronecker coefficients*, 4 November 2025 | Lemma 2.1; Theorems 3.1 and 3.6; Definitions 3.2, 3.5, 3.8, 4.4 and 5.1; Propositions 3.4 and 3.9; Theorems 4.5 and 5.2. G-005 proves the exact mark-to-polytope change. Two local printed proof errors are repaired in the independent review. |
| Maas--Gariépy--Tétreault, *3-Plethysms of homogeneous and elementary symmetric functions*, arXiv:2209.14942v1 | Section 4.2, printed pp.8--9, for the classical Thrall--Chen coefficient formulas; Theorem 1, Section 7.3, printed p.20, for the tableau formula. G-007 proves the normalizer-trace version. |
| Sarkar, *Stability of plethysm coefficients and modified polynomial induction*, arXiv:2610.07929v2, 14 October 2026 | Theorem D = 6.4, Proposition 7.1, Theorem E = 7.3. The exact hypotheses and character transpose are written in T-010--T-013. |
| Anderson, *Chern class formulas for G2 Schubert loci* | Appendix A, Proposition A.1 and Corollary A.2, printed p.29: stabilizer and open orbit. |
| Manivel, *Prehomogeneous spaces and projective geometry* | Proposition 3.1.4 p.44; Examples 4.3.3 pp.59--60 and 4.4.2 pp.61--62; Section 5.1.2 p.68: the width-seven orbit, degree-seven boundary and metric ranks. |
| Brion, *Invariants d'un sous-groupe unipotent maximal d'un groupe semi-simple*, Ann. Inst. Fourier 33(1), 1983 | Theorem 3 pp.12--13, case \((A_6,\omega_3)\) in III.1 p.14, and Corollary 2 to Theorem 2: the precise nonpolynomial invariant-ring calculation used in T-020. |
| Akin--Buchsbaum--Weyman, *Schur functors and Schur complexes*, 1982 | Theorem II.2.16 p.232 and Theorem III.1.4 pp.245--246; exact integral use and conjugated notation are proved in A-012. |
| Mulmuley, *Geometric Complexity Theory VII: Nonstandard quantum group for the plethysm problem*, supplied source | Problem 1.1 asks for an explicit positive #P formula. Theorem 1.2 states the nonstandard quantization and complete reducibility/Peter--Weyl assertions. The subsequent duality, reciprocity and canonical-basis requirements are stated as unresolved in that source. The present proofs use no such unproved requirement. |

Primary URLs: <https://www.math.ucla.edu/~pak/papers/plethysm-Kronecker-trees.pdf>; <https://arxiv.org/abs/2209.14942>; <https://arxiv.org/abs/2610.07929>; <https://arxiv.org/abs/math/0101116>; <https://people.math.osu.edu/anderson.2804/papers/g2-chern.pdf>; <https://manivel.perso.math.cnrs.fr/trento2012.pdf>; <https://www.numdam.org/item/10.5802/aif.902.pdf>.

The source-copy manifest records exact local bytes used for consultation. Full third-party articles downloaded during the run are not redistributed in the ZIP; their mathematical uses, URLs, hashes, and the complete current proofs and certificates are included. The user-supplied transcriptions and literature sources remain included as supplied input evidence.

## General quantum counting bound in the current literature

Christandl–Harrow–Panova–Posta–Walter, *Plethysm is in #BQP*, CCC2026,
DOI10.4230/LIPIcs.CCC.2026.28, **Problem1 and Theorem2**, proves #BQP
membership for general plethysm coefficients and QMA membership for
positivity, with all three partitions encoded in unary. The exact
representation is their equation(2.1), restriction along the inner
Schur representation; T-003 identifies its multiplicity with the
balanced finite-group projector used here. The theorem statement and
encoding were read on the [primary published page](https://drops.dagstuhl.de/storage/00lipics/lipics-vol383-ccc2026/html/LIPIcs.CCC.2026.28/LIPIcs.CCC.2026.28.html).
This is cited background. Its complete quantum verification proof was
not replayed. The polynomial classical-witness bounds needed by the
G-009–G-011 preprocessing remain the exact open requirement stated here.


# Independent full review of the outer-four fiber and polytope formula

## Review outcome and scope

**PASS.** I read and checked the complete proofs in T-032 `general_chart_report.md`, T-035–T-036 `outer4/four_fibers_report.md`, and T-037 \(`outer4/full_outer4_report.md`, including A.29–A.31\). I also checked the exact complement pairing F.12–F.15, the Elliott character calculation H.5–H.7, the harmonic character table H.8–H.12, and the three \(S_3\) series P.10 used by T-037. The checks below establish the actual module maps, all character twists, saturation in the full oriented range, and the fixed positive lattice counts.

T-037 gives all coefficients \(p_{\mu,(n)}^\lambda\) with \(\mu\vdash4\), including all central cases. It supplies at most 108 tagged bounded rational polytopes in at most five variables; the bounds are 36 for the symmetric and exterior outer labels and 72 for \((2,2)\). The exact fixed-table identities and arithmetic checks were independently executed in `check_outer4_fixed_tables.py`; its receipt is `OUTER4_FIXED_TABLE_RECEIPT.json`. I did not rerun the other agent's 1,980-coefficient Murnaghan–Nakayama sweep and do not count that sweep as my own event.

The only wording correction requested during this review was an explicit redefinition of (a,b) after the complement operation. The author has made that correction in A.7. The original and retwisted \(q\)-actions were checked separately; T-037 uses the correct cancellation.

## A-024. Actual free decomposition of the incidence algebra

Write \(V=\mathfrak h_4\), with its invariant dot product, \(W=\Lambda^2V=V\otimes\operatorname{sgn}\), and
\[
R=\mathbf Q[q\in V,t\in W]/(f),\qquad f=q\cdot t.
\]
The notation identifies each self-dual representation with the corresponding polynomial generator space through the displayed invariant form. The generator \(f\) has bidegree ((1,1)) and character \(\operatorname{sgn}\). In particular \(\det V=\operatorname{sgn}\) and \(\det W=1\).

Let \(\ell_i=e_i-\frac14\mathbf1\). The two quadrics \(U\) vanishing on their four projective lines give, after the specified linear change of coordinates,
\[
A=\mathbf Q[q]/(U)
=\mathbf Q[X,Y,Z]/(X^2-Z^2,Y^2-Z^2).
\]
The monic reductions give an actual free \(\mathbf Q[Z]\)-basis (1,X,Y,XY). After inverting \(Z\), the ring maps isomorphically to the product of the four Laurent line rings indexed by \(X/Z,Y/Z\in\{1,-1\}\). Freeness over \(\mathbf Q[Z]\) makes the map to the product of the four polynomial line rings injective before localization. Thus no component or embedded contribution at the origin has been removed. The two displayed quadrics form a regular sequence in the polynomial ring: after quotienting by the first, the second is monic in \(Y\) and hence acts injectively.

On the \(i\)-th component, \(q=s\ell_i\) and \(f=s(\ell_i\cdot t)\). Both factors are nonzero in that component's polynomial domain. The product embedding therefore proves that multiplication by \(f\) on (A[t]) is injective. With \(\mathcal H=R/(U)\), the resulting exact Hilbert-series identity is
\[
\operatorname{Hilb}\mathcal H=(1-s^2)^2\operatorname{Hilb}R.
\]

Choose a rational section of \(R_{C,b}\to\mathcal H_{C,b}\) in each finite bidegree, and average it over the 24 elements of \(S_4\). This gives an actual equivariant section \(\sigma\). The multiplication map
\[
M:\operatorname{Sym}(U)\otimes\mathcal H\longrightarrow R,
\qquad p\otimes h\longmapsto p(U)\sigma(h)
\]
is surjective by repeatedly reducing modulo (\(U\)); every reduction lowers the \(q\)-degree by two. Its source and target have equal dimensions in every bidegree by the preceding series identity. Hence \(M\) is an equivariant \(\operatorname{Sym}(U)\)-linear isomorphism. This also proves algebraic independence of the two quadrics, and that they form a regular sequence in \(R\). It directly identifies
\[
(U)^kR_{c,b}
\simeq\bigoplus_{j=k}^{\lfloor c/2\rfloor}
\operatorname{Sym}^jU\otimes\mathcal H_{c-2j,b}.
\]
There is no unproved choice of a multiplicative basis in this argument. The section is a linear section; its explicit averaged multiplication map supplies exactly the required free module structure.

### Evaluation and every quotient piece

Evaluation at the actual affine vectors \(\ell_i\) is \(S_4\)-equivariant with no parity character. It gives \(A_0=\mathbf1\), \(A_1=V\subset\operatorname{Perm}_4\), and \(A_C=\operatorname{Perm}_4\) for all \(C\ge2\). An explicit surjectivity check is available without any projective scaling convention: put
\[
E_i(q)=2q_i^2-\tfrac16\sum_lq_l^2.
\]
Then \(E_i(\ell_j)=\delta_{ij}\); for \(C\ge2\), the homogeneous polynomial
\(E_i(q)(4q_i/3)^{C-2}\) has the same evaluations. The Hilbert series of \(A\) gives dimension four in all those degrees. In degree two the kernel of the evaluation quotient \(\operatorname{Sym}^2V\to\operatorname{Perm}_4\) is exactly \(U=[(2,2)]\). Its matching-plane realization gives \(\det U=\operatorname{sgn}\).

The nonzerodivisor just proved yields the exact equivariant sequence
\[
0\longrightarrow\operatorname{sgn}\otimes A_{C-1}\otimes\operatorname{Sym}^{b-1}W
\xrightarrow{f}A_C\otimes\operatorname{Sym}^bW
\longrightarrow\mathcal H_{C,b}\longrightarrow0.
\]
For \(C\ge3\), evaluation identifies the first map point by point with multiplication by \(\ell_i\cdot t\). The stabilizer \(S_3\) of \(\ell_i\) acts by sign on this line in \(W\), and its quotient is \(\mathfrak h_3\otimes\operatorname{sgn}\). The explicit rational area-form intertwiner identifies this quotient with \(\mathfrak h_3\). Thus the cokernel is
\(D_b=\operatorname{Ind}_{S_3}^{S_4}\operatorname{Sym}^b\mathfrak h_3\).

For \(C=2\), extend the source \(A_1=V\) to \(\operatorname{Perm}_4\). The extended map remains injective point by point, and has the preceding cokernel \(D_b\). The quotient of its image by the original image is
\(\operatorname{sgn}\otimes\operatorname{Sym}^{b-1}W\), because \(\operatorname{Perm}_4/V=\mathbf1\). The resulting short exact sequence splits by an averaged projection.

For \(C=0\), the quotient is \(\operatorname{Sym}^bW\). For \(C=1\), the incidence multiplication removes the \(S_{(b,b,1)}V\) term from \(V\otimes\operatorname{Sym}^b(\Lambda^2V)\); the quotient is the Cartan term \(S_{(b+1,b)}V\). Twisting \(V=W\otimes\operatorname{sgn}\) contributes sign because (2b+1) is odd. The Elliott rule with Dynkin labels ((1,b)) gives \(\bigoplus_{L=1}^{b+1}H_L\), including \(b=0\). Consequently every row of A.5 follows by an actual exact sequence or intertwiner, with the sign in the \(C=1\) row required.

## A-025. Chart, fibers, saturation, and complement

### The general chart and the fiber valuations

In T-032 the centered-ratio chart is equivariant because row permutation fixes \(\mathbf1\), fixes \(u=\prod_i x_i\), and commutes with centering. Its flag-coordinate map is multiplication by the explicitly displayed products of first-column variables. A balanced monomial of weight \((n^m)\) and highest weight \(\lambda\) becomes
\(u^{n-\lambda_2}\) times a tail-flag monomial: the number of columns of height at least two is exactly \(\lambda_2\), and the remaining exponent of every \(x_i\) is \(n\). This proves the claimed surjectivity. The inverse chart prescribing nonzero \(u\), then choosing the \(x_i\) with that product and the remaining centered columns, proves injectivity on a dense open set. Polynomiality is precisely divisibility by the stated power of \(u\), and equality there extends as a polynomial identity. These are actual algebra maps.

For \(m=4\), the map gives \(q\in V\), \(t\in W\), and the determinant variable \(z\in\operatorname{sgn}\). At \(x_4=\varepsilon\), use the affine chart with \(q_4-q_1\ne0\). The two normal coordinates at \(\ell_4\) are
\[
\frac{q_j-q_1}{q_4-q_1}
=\frac{\varepsilon(r_j-r_1)}{S-\varepsilon r_1},\qquad j=2,3.
\]
Their leading coefficients vary independently. Setting the last entry of the third column to zero makes the limiting \(t_1,t_2,t_3\) depend on the first and third columns and \(S\), independently of those two normal coefficients; they range over the fiber \(\sum_{i=1}^3t_i=0\). The fourth column makes \(z\ne0\) on this same generic locus. Therefore the lowest nonzero transverse term cannot disappear upon substitution, and the \(x_4\)-valuation equals the ideal order at the generic point of the entire fiber. Each graded normal quotient is a vector bundle on the integral fiber, so a section vanishing at its generic point vanishes everywhere. This upgrades the generic valuation statement to membership in the full ideal power. Permutation equivariance supplies the other three fibers.

The \(x_i\) are pairwise nonassociate primes, so the individual valuations characterize divisibility by \(u^k\). The four fibers are disjoint, and the incidence projection is a projective-line bundle, hence flat. Their simultaneous order-\(k\) condition is exactly \(\pi^*\mathcal I_Z^k\). These facts establish the stated section-space model by the actual chart substitution.

### Character convention and orientation

T-035 initially uses \(q\in W\), so it has the outside twist \(\operatorname{sgn}^{c+d}\). Replacing that \(q\)-action by the original \(q\in V\) changes the degree-\(c\) section module by \(\operatorname{sgn}^c\). The two factors cancel and leave precisely \(\operatorname{sgn}^d\) in A.16 and A.9.

As an independent check that detects this sign, take \(n=4\), \(\lambda=(11,5,0,0)\), so \(c=5,k=1,b=d=0\). The original-action ideal piece is
\(U\otimes\operatorname{Perm}_4\oplus\operatorname{Sym}^2U\otimes V\).
It has dimension 17 and transposition trace 1. Independently, the balanced trace in \(s_{(11,5)}=h_{11}h_5-h_{12}h_4\), at cycle type ((2,1,1)), is the number of triples \(0\le x,y,z\le4\) with \(2x+y+z=11\), minus the corresponding number for 12. It is \(10-9=1\). An uncancelled extra sign would give (-1).

The complement map uses the nonzero Schur pairing
\(S_\lambda V_4\otimes S_{\widehat\lambda}V_4\to(\det V_4)^H\), obtained by complementary exterior columns. It is perfect by irreducibility and carries the balanced weight to the balanced weight for \(\widehat n=H-n\). Literal permutation matrices act on the target by \(\operatorname{sgn}^H\); self-duality of rational Specht modules gives exactly the conjugation rule in A.6. The operation exchanges the opposite gaps (a,b) and preserves \(c\). After redefining the gaps for the resulting partition, \(a\ge b\), and \(c-2k=(a-b)/2\ge0\) whenever \(k>0\). Thus every input reaches the proved saturation range in at most one complement operation.

### Saturation above the boundary

The two-quadric power resolution pulls back along the flat projection and becomes
\[
0\to\operatorname{Sym}^{k-1}U\otimes\det U\otimes
\mathcal O_{\mathcal F}(c-2k-2,b)
\to\operatorname{Sym}^kU\otimes\mathcal O_{\mathcal F}(c-2k,b)
\to\pi^*\mathcal I_Z^k\otimes\mathcal O_{\mathcal F}(c,b)\to0.
\]
For \(c\ge2k+1\), the left degree is at least (-1). The incidence hypersurface sequence on \(\mathbf P^2\times\mathbf P^2\) proves \(H^1(\mathcal O_{\mathcal F}(a,b))=0\) for \(a\ge-1,b\ge0\): both ambient \(H^1\) and the preceding ambient \(H^2\) vanish, since the latter twists are at least (-2,-1). The same sequence identifies global sections with \(R_{a,b}\) for \(a\ge0\), and gives zero for \(a=-1\).

Global sections are therefore the cokernel of exactly the multiplication map obtained by extending the two-variable power-ideal resolution along \(\operatorname{Sym}(U)\to R\). A-024 proves that \(R\) is free over this polynomial algebra, so that extension is exact. Its cokernel is \((J_R^k)_{c,b}\). This proves equality with the sheaf section space by the same map, including the first endpoint \(c=2k+1\).

At \(c=2k\), the cohomology calculation in T-036 gives the extra summand
\[
\operatorname{sgn}\otimes\operatorname{Sym}^{k-1}U
\otimes\operatorname{Sym}^{b-1}W.
\]
The character can also be checked entirely in the original convention. Here \(H^2(\mathbf P(V),\mathcal O(-3))=\det V=\operatorname{sgn}\), while \(\det U=\operatorname{sgn}\); their product makes \(H^1(\mathcal I_Z^k(2k-1))\allowbreak=\operatorname{Sym}^{k-1}U\). The incidence injection itself has sign, supplying the displayed remaining character. An averaged projection splits the resulting exact sequence. Negative symmetric powers are zero; \(k=0\) is the ordinary whole-ring case and gives no correction. This proves A.9 for every oriented input.

## A-026. Exact fixed tags, lattice counts, and arithmetic

The harmonic trace series on the five classes are
\[
\frac{1+q}{(1-q)^2},\quad\frac1{1+q},\quad\frac1{1+q},\quad
\frac{1+q}{1+q+q^2},\quad\frac{1+q}{1+q^2}.
\]
They follow by dividing \(1-q^2\) by the characteristic polynomial on \(W\). Using the explicit five-row character table and class sizes (1,6,3,8,6), I checked every rational identity giving the stated \(E_\tau\) numerator over \((1-q^4)(1-q^6)\). I also checked all three \(S_3\) averages giving \(F\), all 75 relevant tensor entries by character inner products, and the induction branching giving \(G\). All entries of the tensor table are zero or one.

The Elliott proof H.5–H.7 is a full character calculation: its finite geometric sum distinguishes both parities, the extra \(\delta/(1+z)\) term cancels from \(P(z)-z^{-1}P(z^{-1})\), and the remaining six monomials match the specialized Weyl numerator. Thus the use of its ((1,b)) specialization in A.5 has no unproved branching step.

In the positive module sum, put \(C=c-2j\). The terms with \(C\ge3\) are exactly A.25, with \(j=f+2x_2+3x_3\) recoverable uniquely from each lattice point. Odd \(c\) leaves \(C=1\), producing A.27 and its required label conjugation. Even \(c\) leaves \(C=0\), and also \(C=2\) precisely when \(c\ge2k+2\); these give the displayed A.26 term and the two A.5 terms. At \(c=2k\), only the boundary correction remains in addition to \(C=0\). Consequently A.28 neither omits nor duplicates any summand.

The exact numbers of fixed tags are:

| Target label | A.25 | A.26 or A.27 | Full even bound |
|---|---:|---:|---:|
| ((4)), \((1^4)\) | 6 | 12 | 36 |
| ((2,2)) | 12 | 24 | 72 |
| ((3,1)), ((2,1,1)) | 18 | 36 | 108 |

Every variable has a positive coefficient in an equality or upper bound. Thus each listed region is a bounded rational polytope. Its constants are (O\(n\)), including after complement, and the matrices are fixed.

The elementary scalar formulas A.29–A.31 are also correct. Splitting \(y=2t+e\) proves the arithmetic-progression formula for \(P(N)=\#\{2x+3y\le N\}\); the \(T_e=-1\) endpoint contributes zero. The weight-2 coordinate in A.26 is the uniquely determined slack variable after division by two. For A.27 the lower exclusion is exactly \(P(\lfloor-e/2\rfloor)\), including \(e=0\), where it removes \(L=0\). I directly enumerated the scalar formulas for \(-12\le N\le120\) and all 310 intervals \(0\le b\le30,0\le e\le9\), in addition to the algebraic proofs.

Each fixed template count is \(O((n+1)^3)\); its free count has dimension at most three. The finite number of arithmetic operations uses integers of \(O(\log(n+2))\) bits. Thus the stated schoolbook \(O((\log(n+2))^2)\) arithmetic bound follows for the coefficient evaluator. The witness enumerator is separately output-dependent, as its implementation states.

### Endpoint checks

- \(n=0\), \(\lambda=0\): \(c=b=d=k=0\). Only \(\mathsf W_\mu(0,0)\) survives, giving 1 for \(\mu=(4)\) and zero for the other four labels, exactly the Schur functors of the one-dimensional \(\operatorname{Sym}^0\).
- \(b=0\): every term with (b-1) vanishes; the \(C=1\) row is the correct standard \(V\), since \(\operatorname{sgn}\otimes H_1=V\).
- \(c=0\): \(k=0\), and only the degree-zero quotient piece remains.
- \(c=1\): \(k=0\), and the only term is \(\mathsf L_{\nu'}(0,b)\).
- \(c=2k+1\): the bulk interval is empty, so only the \(C=1\) term remains.
- \(c=2k\): the bulk and \(C=2\) terms are absent; the two \(\mathsf W\) terms give exactly the boundary sequence.
- Valid partitions with more than four parts have zero coefficient: four successive horizontal-strip additions produce at most four rows in the ambient tensor power, and the Schur symmetrizer maps the requested outer functor into that power.

All these checks use the exact maps or formulas above. No unresolved module, saturation, parity, or positive-count gate remains for outer degree four in the stated family. This review makes no assertion of historical novelty.


# Independent review of G-015 and G-016

## Status

**PASS, complete proof read.** The general projective-frame section model and the full quadratic ideal calculation are correct in their stated characteristic-zero scope. The original \(S_m\) action and determinant line are retained throughout. The proof gives the actual comparison map and the ordinary sheaf ideal powers; it proves the needed equality of orders without assuming a higher-cohomology vanishing statement.

I separately opened the original primary source [P. Magyar, *A Borel–Weil Construction for Schur Modules*, arXiv:alg-geom/9411014v1](https://arxiv.org/pdf/alg-geom/9411014) and read Proposition 1, printed pp. 5–6, the Plücker determinant bundle convention on p. 7, and Proposition 4\(a\)–\(c\), printed p. 10. These give the dual Schur convention and the precise full-flag pullback used in GF.2 and GF.7. All maps in this specialization are defined over \(\mathbf Q\). The source's algebraically closed field convention in §2 causes no rational-field gap: global sections commute with field extension, as follows from an affine-cover equalizer and flatness, and a map becoming an isomorphism after the faithfully flat extension \(\mathbf Q\subset\overline{\mathbf Q}\) was already an isomorphism.

## 1. The exact general chart and its linearization

The chart T-032 takes a smaller flag polynomial \(F\) to
\[
u^{n-\lambda_2}F(v(X)),\qquad
v_{j,I}=\left(\prod_{i\notin I}x_i\right)p_{j,I},
\quad u=\prod_i x_i.
\]
The map \(w\mapsto\mathbf1\wedge w\) identifies the smaller exterior coordinates with the displayed minors. Row permutations fix \(\mathbf1,u\), commute with centering, and act on every exterior power by its literal permutation matrix. Thus the chart preserves the exact \(S_m\) action. The full-height smaller flag factor is \(\det E\); its sign character is the last factor of \(\mathcal L_\tau\), not a separate omitted twist.

The highest-weight and row-weight calculation in C.12–C.13 gives precisely \(\lambda_2\) factors of height at least two and the common residual exponent \(n\) for every \(x_i\). The inverse dense chart C.14 recovers any prescribed smaller matrix and any nonzero \(u\). Consequently polynomial extension is exactly divisibility by \(u^k\), as asserted in GF.8. The invariant form on \(E\) is nondegenerate and equivariant over \(\mathbf Q\), so its Schur functor gives the specified map from the section convention \(S_\tau E^*\) to \(S_\tau E\).

## 2. Every higher flag frame is independent of the leading normal directions

At \(x_m=\varepsilon\), with \(s_m=S\ne0\), the first-line coordinates are exactly
\[
a_j=\varepsilon\frac{r_j-r_1}{S-\varepsilon r_1},
\qquad 2\le j\le m-1.
\]
The (m-2) coordinates are a regular parameter system at \([\ell_m]\) in \(\mathbf P(E)\). Pullback along the flag bundle gives a regular parameter system transverse to its whole fiber.

The subfamily \(X_{mj}=0\) for \(j\ge3\) is sufficient to test the possible leading-coefficient cancellation. At \(\varepsilon=0\), a nonzero minor must contain row \(m\); expansion along that row uses only the entry \(S\) in column two. After factoring out the \(x_i\), every remaining minor is an exterior coordinate in the columns
\[
\mathbf1,\quad (X_{i3}/x_i)_{i<m},\quad\ldots,
(X_{im}/x_i)_{i<m}.
\]
No such coordinate depends on the \(r_j\). The quotient \(E/\mathbf Q\ell_m\) is exactly \(\mathbf Q^{m-1}/\mathbf Q\mathbf1\): restricting the first (m-1) coordinates is surjective onto that quotient, with kernel \(\mathbf Q\ell_m\). The remaining ratio columns are arbitrary, so their classes realize every generic flag and every choice of nonzero successive frame scalings in the quotient. Varying \(S\prod_{i<m}x_i\) supplies the first-line frame; successive column scalings supply all higher exterior frames. The last one is nonzero whenever those quotient columns form a basis, so the determinant factor also has valuation zero.

Meanwhile the (m-2) differences \(r_j-r_1\) vary freely with all those image flag and frame coordinates fixed. This proves the required algebraic independence over the image fiber's function field. It is stronger than independence of only the first line: it includes every higher coordinate which can occur in \(F\).

## 3. Equality of orders and the ordinary ideal powers

Choose local nonzero Plücker coordinates at the generic fiber point. On the exhibited family each has valuation zero, so the local trivialization of \(\mathcal L_\tau\) introduces no extra factor of \(\varepsilon\). A section with lowest nonzero transverse term of degree \(h\) has leading coefficient equal to that nonzero polynomial evaluated at the independent \((r_j-r_1)/S\). It cannot vanish. The opposite inequality follows because every transverse parameter is divisible by \(\varepsilon\). This proves exact equality of the original coordinate-divisor valuation and the fiber-ideal order.

The special subfamily used here need not dominate the entire original divisor: the lower-order divisibility is valid on its full open chart, and nonvanishing on this subfamily proves nonvanishing of the universal leading coefficient. Its independence statement is exactly what is needed for the reverse inequality.

The generic order detects the ordinary sheaf power everywhere on the fiber. Indeed the fiber is a regular embedding and its graded normal quotients are locally free over an integral flag variety. A section of such a quotient which is zero at the generic point is zero globally. Induction through the first \(k\) graded pieces therefore gives membership in \(\mathcal I_i^k\) at every point, not just symbolic membership at one generic point.

The original \(x_i\) are pairwise nonassociate primes. Hence the \(m\) valuations are equivalent to divisibility by \(\prod_i x_i^k\). The fibers are disjoint, so their powers are pairwise comaximal and intersection equals product. Flatness of the flag projection identifies that product with \(\pi^*\mathcal I_{Z_m}^k\). Applying the actual chart map proves GF.4, and the specified Specht covariant functor proves GF.5.

The cases \(k=0\), \(n=0\), and \(m=3\) cause no change in the argument. For \(m=3\), the quotient flag fiber is a point, the transverse system has one parameter, and the same independence test still applies.

## 4. The full quadratic ideal and its action

Set \(r=m-1\ge3\) and use the \(r\) coordinate points plus \([1:\cdots:1]\). In degree two, vanishing at the coordinate points removes every square, while vanishing at the last point imposes exactly one sum-zero relation on the mixed coefficients. This gives the listed differences \(z_i z_j-z_1z_2\).

In their quotient, write \(z=z_1z_2\). For distinct (i,j), choose \(a\notin\{i,j\}\); then
\[
z_i z=z_i(z_jz_a)=z_j(z_i z_a)=z_jz.
\]
Every mixed degree-\(C\) monomial contains a cross-product, and this identity replaces every remaining factor by \(z_1\). Thus the pure powers \(z_i^C\) and the single mixed class \(zz_1^{C-2}\) span. Evaluation at the coordinate points isolates the coefficients of the pure powers, and evaluation at the last point then isolates the mixed coefficient. They are independent. This proves the asserted basis in every degree, including the low degrees separately.

The resulting graded map to the product of line coordinate rings is injective. Its kernel before quotienting is exactly the intersection of the homogeneous linear prime ideals of those lines. Hence the generated ideal is radical and saturated as well as the full projective ideal. The dimension of its quadratic piece is \(m(m-3)/2\).

Returning to the exact affine representatives \(\ell_i\), evaluation is equivariant without a scaling character. The two eigenvalues for the matrix of the values of \(q_i^2\) are \((m-2)/m\) and \((m-1)/m\); for \(q_i^3\) they are \(1-3/m+3/m^2\) and \((m-1)(m-2)/m^2\). These are nonzero for the stated \(m\). The invariant quadratic has the same nonzero value at each point and propagates surjectivity by two degrees. The established dimensions make evaluation an isomorphism onto \(\operatorname{Perm}_m\) for every \(C\ge2\). Degrees zero and one give its constant and standard submodules. All the actions in GF.15 are therefore literal evaluation maps.

For \(m=3\), the three differences \(q_i-q_j\) are distinct line equations on \(E\), each vanishing at one frame point. Their product gives exactly the reduced degree-three divisor ideal and changes by sign under permutations. This is the stated separate cubic formula.

## 5. Independent check supplied for the next \(m=5\) computation

The subsequent cubic and full resolution are being written by the theta agent in T-038. I supplied an independent verification of its quadratic-subalgebra kernel; the full resolution was not audited in this event.

For the five quadrics
\[
A=z_1z_3-z_1z_2,\ B=z_1z_4-z_1z_2,\
C=z_2z_3-z_1z_2,\ D=z_2z_4-z_1z_2,\ E=z_3z_4-z_1z_2,
\]
the nonzero cubic
\[
F=AD(E-B-C)-BC(E-A-D)
\]
maps to zero; exact symbolic expansion confirms it. Put \(x=z_1z_2\). In the image fraction field,
\[
x=\frac{AD}{E-A-D},\qquad
z_1^2=\frac{x(x+A)}{x+C}.
\]
All six pair products follow from \(x,A,B,C,D,E\), and all \(z_i\) follow from them and \(z_1\). Thus \(\mathbf Q(z_1,z_2,z_3,z_4)\) is algebraic of degree two over the image field, so that field has transcendence degree four. The cubic is primitive linear in \(E\): its coefficient \(AD-BC\) is irreducible, and does not divide its constant term, as the substitution \((A,B,C,D)=(1,2,3,6)\) gives constant 12. Gauss's lemma proves irreducibility. The kernel is consequently the height-one prime \((F)\).

Under the actual coordinate transposition \(z_1\leftrightarrow z_2\), the quadrics transform by \(A\leftrightarrow C\), \(B\leftrightarrow D\), and \(E\mapsto E\), so \(F\mapsto-F\). The degree-three kernel is one-dimensional and stable under \(S_5\), and a one-dimensional character of \(S_5\) is determined by a transposition. Hence this relation has sign character, agreeing with theta's independent calculation. This is an explicit algebra map and relation, not a dimension-only comparison.


# Independent complete reviews of the five-point formulas

Reviewer: GPT-6 Astra Pro, run /root/archive_audit. The reasoning setting is not exposed. The complete reports T-038, T-039 and G-017 were read, their arguments checked, and the finite identities below independently executed. The events are recorded in CHECK_EVENTS.tsv. This review concerns the precise families and maps stated in those reports.

## A-030. Complete review of T-038

**Status: PASS.** The full source is work/theta/outer5/five_point_resolution_report.md, equations (5R.1)–(5R.20).

### The reduced scheme and the complete resolution

Let \(S=\mathbf Q[x,y,z,w]\), and let \(I\) be generated by the five displayed differences of cross-products. In \(S/I\), all six cross-products have the same image \(p\). With a third distinct variable available, \(z_i p=z_jp\). Thus every mixed monomial of degree \(C\ge2\) equals \(px^{C-2}\). The four pure powers and this mixed monomial have independent evaluations at the four coordinate points and at \((1,1,1,1)\). This proves the stated homogeneous basis and the injection into the product of the five line-coordinate rings. The kernel is consequently the intersection of the five homogeneous line ideals. This proves reducedness and saturation directly, as well as the complete Hilbert series used later.

I independently multiplied the displayed matrices and verified \(f^tM=0\) and \(MN=0\). The specified four-by-four minor is nonzero. The entries \(y(x-w)\) and \(z(y-w)\) already have greatest common divisor one. Over the fraction field, the kernel of \(M\) is therefore the line generated by \(N\); clearing a reduced denominator and using primitivity shows that its kernel over \(S\) is precisely \(SN\). The Hilbert-series comparison with \(\ker f^t\) then proves exactness in every degree. The injectivity at the left and positivity of every entry's degree also prove minimality.

The change-of-basis matrix has determinant \(-1\), satisfies \(N=Pf\), and turns \(M\) into the alternating matrix in (5R.14). All five signed maximal Pfaffians independently agree with \(f\). These calculations give the actual height-three alternating presentation needed in A-029.

### Group actions and the cubic map

The affine representatives \(\ell_i=e_i-\frac15\mathbf1\) are permuted exactly. Their use in evaluation proves \((S/I)_C\simeq\operatorname{Perm}_5\) for every \(C\ge2\), including odd \(C\). The fifth representative has coordinates \((-1,-1,-1,-1)\) in the chosen basis; the proof of independence remains valid with that representative. There is therefore no unrecorded degree-dependent character in (5R.9).

For each of the seven conjugacy classes, I checked the rational character identity
\[
\frac{1+\chi_E(g)t+\chi_{\operatorname{Perm}_5}(g)t^2/(1-t)}
     {\operatorname{tr}(g\mid\operatorname{Sym}E)}
=1-\chi_U(g)t^2+\chi_{\epsilon U}(g)t^3-\chi_\epsilon(g)t^5.
\]
It verifies the generator, first-syzygy and last-syzygy labels simultaneously. The report's transposition calculation also identifies the final one-dimensional representation without requiring this larger check.

For the subalgebra map \(\mathbf Q[A,B,C,D,E_0]\to S\), the cubic \(F\) vanishes by expansion. Its image field recovers \(xy\), all other cross-products, and \(x^2\) by the rational expressions in (5R.16). Adjoining \(x\) recovers \(y,z,w\), so the image has transcendence degree four. Viewed as a polynomial in \(E_0\), \(F\) has irreducible leading coefficient \(AD-BC\); the test \((A,B,C,D)=(1,2,3,6)\) proves that coefficient does not divide the constant term. Gauss's lemma proves irreducibility, and the height-one prime kernel is exactly \((F)\). This verifies the algebra isomorphism, rather than merely a relation in the image.

The six forms have rank five, sum zero and sum of cubes \(-24F\). I separately constructed the six subgroups of order five in the specified lexicographic order. For each of the four adjacent transpositions, direct substitution in the quadratic forms gives
\[
g(t_i)=-t_{g(i)}.
\]
The target indices are exactly those obtained by conjugating the subgroups. These four generators prove the full \(S_5\)-intertwining identity. In particular the signed six-letter action used subsequently in G-017 is verified with its actual indexing.

The primary representation conventions and geometric comparison were read in Dolgachev–Farb–Looijenga, author PDF, §2.3 Table 1, p. 10, and Remark 2.4, p. 13, as recorded in A-028. The report's explicit cubic morphism proves the needed identification independently of the historical attribution.

## A-031. Complete review of T-039

**Status: PASS.** The full source is work/theta/outer5/five_point_family_report.md, including its endpoint and support arguments.

### The bundle map and its linearization

For the stated partition,
\[
\lambda_2-n=1,\qquad
(\lambda_2,\lambda_3,\lambda_4,\lambda_5)
=(d+a+2,d+a,d+a,d).
\]
The actual G-015 chart therefore gives the flag section module with ideal factor \(\mathcal I_Z\). The relative Plücker map on the quotient flag gives
\[
(\det E^*)^d\otimes\mathcal O(a+2)\otimes S_{(a,a)}Q^*.
\]
The exterior pairing \(\Lambda^2Q^*\simeq Q\otimes\det Q^*\), its symmetric power, and the determinant of the tautological sequence give
\[
(\det E^*)^{d+a}\otimes\mathcal O(2)\otimes\operatorname{Sym}^aQ.
\]
For rank three, the asserted identification of \(S_{(a,a)}Q^*\) with the symmetric power of \(\Lambda^2Q^*\) has the specified highest-vector map and equal dimensions \(\binom{a+2}{2}\). It is valid also for \(a=0\).

The local product description of the flag bundle verifies projection with the possibly nonflat ideal. Over a trivializing open set, the relevant Čech complex is a complex of rational vector spaces tensored with the base ring. Its kernel and image sequences split over \(\mathbf Q\); tensoring by the ideal preserves this calculation of degree-zero cohomology. The local maps agree under changes of quotient frame. This proves the stated projection map with the ideal factor.

Since \(\det E=\epsilon\), the resulting sign is precisely \(\epsilon^{d+a}\). No determinant factor is lost in either exterior pairing.

### Cohomology and the positive exact sequence

Multiplication by the tautological line gives the exact symmetric-power sequence (5F.11). Its fiberwise kernel and injectivity are correct. On \(\mathbf P(E)\), parametrizing lines, the canonical bundle is \(\mathcal O(-4)\otimes\det E^*\); thus \(H^3(\mathcal O(-4))=\det E=\epsilon\). This agrees with the ordered Čech computation.

The three cohomology rows in (5F.12) follow from the full long exact sequences: \(B_a\) has only \(H^0=\operatorname{Sym}^aE\); \(B_a(-1)\) is acyclic; and \(B_a(-3)\) has only \(H^2=\epsilon\operatorname{Sym}^{a-1}E\). The last group is zero at \(a=0\).

Sheafifying the exact T-038 resolution and tensoring by \(B_a(2)\) produces the two short exact sequences in the report. They give \(H^0(K)=0\) and \(H^1(K)=\operatorname{Sym}^{a-1}E\). The last-syzygy sign and projective-cohomology sign multiply to the trivial character. Consequently the actual sequence is
\[
0\longrightarrow U\otimes\operatorname{Sym}^aE
\longrightarrow H^0(\mathcal I_Z(2)\otimes B_a)
\longrightarrow\operatorname{Sym}^{a-1}E\longrightarrow0.
\]
The first arrow is quadratic multiplication followed by the quotient-bundle map; the last arrow is the connecting map from the stated resolution. Averaging a section over \(S_5\) gives the direct-sum isomorphism. This proves (5F.2) in every \(a,d\ge0\).

### All fixed tags and endpoints

I independently enumerated the 26 standard tableaux of the seven shapes of size five and computed their stated comajor indices. Every entry, including the repeated value \(5\) for shape \((3,1,1)\), agrees. I then verified all seven rational identities for the multiplicities in \(\operatorname{Sym}^aE\):
\[
\sum_{g\text{ classes}}\frac{|g^{S_5}|\chi_\rho(g)}{120}
\frac{1-t}{\prod_{\ell\in\operatorname{cycles}(g)}(1-t^\ell)}
=\frac{\sum_{r\in D_\rho}t^r}
{(1-t^2)(1-t^3)(1-t^4)(1-t^5)}.
\]
The 49 entries of the tensor table \(U\otimes[\rho]\) were independently computed by exact character inner products. They all agree. The resulting numbers of tagged polytopes, in the report's row order, are
\[
6,\ 24,\ 30,\ 36,\ 30,\ 24,\ 6.
\]
These totals equal \(6\dim[\nu]\) exactly.

The twist replaces \(\mu\) by \(\mu^t\) exactly when \(d+a\) is odd. In the symmetric outer case, the even list is \(1,\ldots,6\), and the odd list is \(4,\ldots,8,11\). The semigroup generated by \(2,3,4,5\) is \(\{0\}\cup\mathbf Z_{\ge2}\). This proves the stated support thresholds \(a\ge1\) and \(a\ge4\), including the consecutive first two degrees that handle residual zero and the missing residual one. At \(a=0\), all counting terms have the correct value for the single twisted module \(U\). Every polytope is bounded because its nonnegative coordinates have positive weights.

## A-032. Complete review of G-017

**Status: PASS.** The full source is work/root/five_point_q_module_report.md, equations (Q.1)–(Q.26).

### The actual section module and its generators

The partition has \(\lambda_2-n=k\). Its relative quotient-flag weight is \((1,1,0)\), so the same exterior pairing as above gives the exact module
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+1}M_k,\qquad
M_k=H^0(\mathcal I_Z^k(2k)\otimes Q).
\]
The specified inverse chart and G-015 prove its extension criterion. The parity convention for \(\nu\) in (Q.3) follows: it equals \(\mu\) for odd \(d\) and \(\mu^t\) for even \(d\).

The quadratic vector \((z_i^2)_i\) vanishes in the quotient fibers at all five points. Its invariant description in centered coordinates differs from this vector by \(-\frac25(\sum z_i)z\), a tautological-line vector. This proves that \(\theta\) is an invariant section of the stated sheaf.

I independently formed \(P=\operatorname{adj}K/F\) from the printed \(K\). Every entry is polynomial. The determinant identities, both matrix products, the last row and all twenty line-corrected substitution identities (Q.12) hold exactly. The nonzero two-by-two minor agrees with the printed expression.

The relation-space linearization is justified by the report's injectivity argument. A degree-three polynomial double at the four coordinate points is a combination of the four squarefree cubics. The four derivatives at the fifth point force every coefficient to vanish. Thus \(H^0(\mathcal I_Z^2(3))=0\). Together with the absence of a degree-two cubic-ring relation, this proves the required injectivity of \(E\otimes\operatorname{Sym}^2U\to M_2\). It makes the coefficient vector attached to \(f\theta\) unique; applying the group action proves that the five relations form \(U\).

### Injection and surjection in every degree

The adjugate argument establishing \(C\)-torsion-freeness of the cokernel is valid. In \(gv=Pw\), where \(F\nmid g\), each component of \(\operatorname{adj}P\,v\) is divisible by \(F^3\), because \(\det P=81F^3\) and \(S\) is a unique-factorization domain. The resulting polynomial vector \(u\) satisfies \(Pu=v\).

Over the discrete valuation ring \(S_{(F)}\), the elementary divisors of \(P\) have exponents at most one by \(PK=3FI\). Their sum is three by the determinant. The cokernel therefore has rank three over \(C\). Upon extending its fraction field to \(\mathbf Q(z_1,z_2,z_3,z_4)\), the four constant generators span the three-dimensional quotient by the tautological line. The resulting generic map is an isomorphism; its kernel before localization is \(C\)-torsion and hence zero. This proves the actual injection into the section module.

A-029 proves the needed \(2k\)-linear resolutions for every \(k\ge2\), saturation in degree \(2k\), and \(H^1(\mathcal I_Z^k(2k-1))=0\). The latter degree is a sheaf-section calculation: these sections may be nonzero even though the ordinary polynomial ideal power has minimum degree \(2k\). Formula (Q.15) correctly uses the fat-point length and sheaf sections.

The tautological sequence is locally split, so it remains exact after tensoring with the ideal. Its cohomology gives
\[
\dim M_k=4\left(\binom{k+4}{4}-\binom{k+1}{4}\right)
-\left(\binom{2k+2}{3}-5\binom{k+2}{3}\right)
=\frac{(k+1)(k+2)(3k+4)}2.
\]
At \(k=1\), the additional \(H^1(\mathcal I_Z(1))=\mathbf1\) gives \(21\); at \(k=0\), the space is \(E\) of dimension four. Both values agree with the polynomial. Thus the injective presentation and \(M\) have equal dimensions in every degree, proving surjectivity and all the stated relations.

### The invariant parameters and positive formula

The successive-root construction proves that the polynomial ring in six variables is free over the elementary symmetric coefficient ring. Each adjoining step is a monic quotient of the indicated degree; after the final root, coefficient elimination identifies the result with the original polynomial ring. Quotienting by \(e_1\), replacing \(e_5\) by \(e_5^2\), and substituting \(e_3=-8F\) therefore prove that \(S\) is free of rank \(1440\) over
\[
\mathbf Q[e_2,e_4,e_6,e_5^2,F].
\]
The signed six-letter action makes the first four displayed generators invariant.

After any preceding parameter quotient, both the next parameter and \(F\) remain nonzerodivisors. The determinant \(81F^3\) then proves that \(P\) stays injective after quotienting by the next parameter. Reducing \(pv=Pw\) modulo that parameter gives \(w=pw'\), and cancellation gives \(v=Pw'\). This proves regularity on the cokernel at every step.

The finite quotient \(H=M/B_+M\) consequently has the stated Hilbert series, degree 19 and dimension 4320. A graded averaged section followed by multiplication gives \(B\otimes H\to M\); degree induction proves surjectivity and the regular-sequence Hilbert identity proves injectivity. This is the required actual equivariant free decomposition.

I independently derived all seven rational characters of \(M\) by Newton identities from the cycle-type character of \(U\). All 140 multiplicities in the displayed \(H\)-table agree. Its row totals are
\[
36,\ 144,\ 180,\ 216,\ 180,\ 144,\ 36,
\]
and its total dimension is 4320. Every nonidentity character vanishes at \(t=1\), which verifies the regular-character check.

All support criteria follow from the first two consecutive nonzero entries of each row and the weight-two parameter. This includes \(k=0,d=0\), where the balanced module is \(\epsilon E=[2,1,1,1]\). The residue decomposition for weights \(1,2,3,5\) gives exactly (Q.26), with residue polynomial degree \(29+28+27+25=109\) and at most four summands. An independent dynamic-programming count verified it for arguments \(0,\ldots,240\); the proof by unique residue decomposition establishes it for every nonnegative argument.

## Check files and precise scope

The independently written check script is work/archive/check_outer5_fixed_data.py. Its executed receipt is work/archive/OUTER5_FIXED_DATA_RECEIPT.json. It verifies the exact fixed identities described above. One initial script assertion compared expanded and factored polynomial expressions structurally; changing that comparison to expanded polynomial equality made the intended check exact. No mathematical statement was changed.

The whole arguments, including all zero and parity cases, have been reviewed separately from these calculations. This event does not claim to rerun the authors' larger variable coefficient sweeps or their witness enumeration. Those checks retain their own authorship and receipts.


# Five-point jet characters and independent positive-formula checks

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

## A-033. Exact jet maps and complete independent review of G-019

**Status: PASS.** I read the entire report work/root/five_point_symmetric_quotient_report.md, including (SQ.1)–(SQ.16), every endpoint, the full zero set and the stated framework transport. I independently reconstructed all 403,200 fixed coefficients by the following geometric calculation.

### 1. A uniform equivariant jet description

Let \(E=\mathfrak h_5\), let \(\ell_i=e_i-\frac15\mathbf1\), and let \(Z\) be the five corresponding projective points. Use the invariant inner product to write
\[
E=\mathbf Q\ell_i\oplus W_i,\qquad
\alpha_i(v)=\frac{\langle v,\ell_i\rangle}{\langle\ell_i,\ell_i\rangle}.
\]
The affine chart \(\alpha_i\ne0\) is identified with \(W_i\) by
\[
[v]\longmapsto v/\alpha_i(v)-\ell_i.
\]
This map and its inverse \(w\mapsto[\ell_i+w]\) commute with the stabilizer \(S_4\) of the point. The degree-\(c\) line bundle is trivialized on this chart by \(\alpha_i^c\). These choices are transported exactly when the five points are permuted.

Consequently the order-\(k\) jets of \(\mathcal O(c)\) at this point are the actual module
\[
\bigoplus_{j=0}^{k-1}\operatorname{Sym}^j(W_i^*).
\]
The quotient by the \(k\)-th power of the coordinate maximal ideal gives this decomposition directly. The invariant form identifies \(W_i^*\) with \(W_i\), and \(E=\mathbf1\oplus W_i\) under the stabilizer. The complete five-point jet module is induced from this stabilizer module. This specifies the action for every integer \(c\); there is no scalar rescaling of the affine representatives.

For \(g\in S_5\), let \(m_1(g)\) be its number of fixed letters, and put
\[
h_r(g)=\operatorname{tr}(g\mid\operatorname{Sym}^rE),\qquad h_r=0\quad(r<0).
\]
Only fixed points contribute to the trace on the five-point direct sum. At any such point,
\[
\sum_{j=0}^{k-1}
\operatorname{tr}(g\mid\operatorname{Sym}^jW_i)
=h_{k-1}(g).
\]
This identity is the decomposition of \(\operatorname{Sym}^{k-1}(\mathbf1\oplus W_i)\). Therefore the exact jet character is
\[
\boxed{\operatorname{tr}\bigl(g\mid
H^0(\mathcal O/\mathcal I_Z^k(c))\bigr)
=m_1(g)h_{k-1}(g).}
\tag{J.1}
\]
For \(k=0\), both sides are zero.

### 2. The two scalar Euler terms and the symmetric quotient map

The restriction sequence
\[
0\longrightarrow\mathcal I_Z^k(c)
\longrightarrow\mathcal O(c)
\longrightarrow\mathcal O/\mathcal I_Z^k(c)
\longrightarrow0
\]
is equivariant. Its cohomology, with the complete vanishings in A-029, gives
\[
\operatorname{tr}(g\mid C_k)
=h_{2k}(g)-m_1(g)h_{k-1}(g),
\tag{J.2}
\]
and
\[
\operatorname{tr}\bigl(g\mid
H^0(\mathcal I_Z^k(2k-1))-H^1(\mathcal I_Z^k(2k-1))\bigr)
=h_{2k-1}(g)-m_1(g)h_{k-1}(g).
\tag{J.3}
\]
The notation in (J.3) denotes the exact representation-group class of the displayed cohomology sequence.

These equations include the endpoints. At \(k=0\), (J.3) is zero. At \(k=1\), it is \(-\mathbf1\), since \(h_1(g)=m_1(g)-1\); the actual groups are \(H^0(\mathcal I_Z(1))=0\) and \(H^1(\mathcal I_Z(1))=\mathbf1\). At \(k\ge2\), the latter cohomology vanishes by A-029. In degree \(2k\), \(H^1\) vanishes for every \(k\), including the direct degree-two evaluation check at \(k=1\).

Multiplication by the tautological line gives the exact, locally split symmetric-quotient sequence used in (SQ.4). Tensoring with the ideal preserves it. Its cohomology, including the \(k=1\) connecting term, therefore gives
\[
\boxed{\begin{aligned}
\operatorname{tr}(g\mid M_{a,k})
={}&h_a(g)\bigl(h_{2k}(g)-m_1(g)h_{k-1}(g)\bigr)\\
&+h_{a-1}(g)\bigl(m_1(g)h_{k-1}(g)-h_{2k-1}(g)\bigr).
\end{aligned}}
\tag{J.4}
\]
This independent formula uses the standard representation and the actual Taylor maps. It does not require the cubic presentation or G-017's fixed character table.

The flag comparison in G-019 has point order \(k\), first-line gap \(2k\), and relative weight \((a,a,0)\). Its first-line weight after the full determinant is \(a+2k\). The exterior pairing contributes \((\det Q^*)^a\), giving \(\mathcal O(2k)\) and sign \(\epsilon^{d+a}\). Thus (SQ.3) and its parity convention agree with the actual local frame maps. At \(a=0\), the second term in (J.4) is zero. At \(a=k=0\), the module is trivial before the determinant twist, including the empty-partition endpoint.

### 3. Independent reconstruction of every fixed coefficient

For each of the seven cycle types, I formed
\[
\det(1-tg\mid E)=
\frac{\prod_{\ell\in\operatorname{cycles}(g)}(1-t^\ell)}{1-t}
=1+d_1t+\cdots+d_4t^4.
\]
The exact recurrence
\[
h_0=1,\qquad
h_r=-\sum_{j=1}^{\min(4,r)}d_jh_{r-j}
\]
computes all required characters through degree 478. Equations (J.2) and (J.3) give the two scalar arrays, and (J.4) gives their products with \(h_a,h_{a-1}\).

I computed the order-zero through order-three step-60 differences of each separate array. Multiplying those differences according to (J.4), followed by the seven fixed character inner products, gives the mixed differences directly. This differs from computing a two-dimensional multiplicity grid and then taking differences of that grid.

All 403,200 resulting integers agree exactly with the complete root table. Every entry is nonnegative. The \((3,3)\) entries are zero. The other fourteen positive-order positions have strictly positive minima for every label, as stated in the report.

The rational-function verification was independent as well. With \(H(x)=1/\det(1-xg\mid E)\), the even and odd subsequences are
\[
\sum_{k\ge0}h_{2k}t^k
=\left.\frac{H(x)+H(-x)}2\right|_{x^2=t},
\quad
\sum_{k\ge0}h_{2k+1}t^k
=\left.\frac{H(x)-H(-x)}{2x}\right|_{x^2=t}.
\]
Using these expressions in (J.2)–(J.3), I checked all 28 one-variable factors against the common denominator \((1-t^{60})^4\). Their numerators are polynomials of degree at most 239. This proves the residue-polynomial argument from the first nonnegative quotient value, including its initial zero binomial terms.

The two-variable Newton identity consequently holds for all \(a,k\), with degree at most three in each quotient variable. Its bounded polytope conversion uses the two fixed residue equations, one bounded multiplicity coordinate, and two increasing subset chains. The claimed upper bounds of 57,600 tags and nine variables are valid. The constant number of arithmetic operations and the quadratic schoolbook bit-cost bound follow because all binomial degrees and table dimensions are fixed.

I also verified the dimension identity (SQ.15). The common factor
\[
C_k+\bigl(M_k-4C_k\bigr)=(k+1)(2k+1)
\]
at the level of dimensions gives exactly the displayed expression after applying Pascal's identity in \(a\). The exceptional \(k=1\) term is retained.

The exact zero list has 44 triples \((\nu,a,k)\), all in the first 60-by-60 square, and agrees entry by entry with the report. Strict positivity of the \((1,0)\) and \((0,1)\) coefficients on every residue excludes any further zeros. This proves the stated complete support, including both axes and all determinant parities.

The independent script is work/archive/check_symmetric_quotient_by_jets.py. The full receipt, including target hash, separate coefficient minima and maxima, all rational bounds and all 44 zeros, is work/archive/SYMMETRIC_QUOTIENT_JET_RECEIPT.json.

## A-034. Complete review of T-040 and a second jet reconstruction

**Status: PASS.** I read all of work/theta/outer5/q_plus_report.md, equations (QP.1)–(QP.23), including the matrix presentation, its equivariant splitting, every Newton coefficient formula and the complete support argument.

The ordinary/saturated comparisons in (QP.5) use precisely the proved degree ranges of A-029. The degree-one part of the Rees presentation is the cokernel of \(\mathsf B\); the identity \(\mathsf B\mathsf Q=FI_4\) shows that its additional \(F\)-relations already lie in that image. All five maximal minors are the stated \(-FT_i\), and the primitive column \(T\) generates the entire polynomial kernel. The sign labels follow from the actual change of basis in the T-038 resolution.

The tautological sequence gives the exact injection
\[
\mathcal A_k\longrightarrow E\otimes\mathcal C_k,\qquad
s\longmapsto\sum e_i\otimes x_i s.
\]
The quotient is \(\mathcal N_k\) because \(H^1(\mathcal I_Z^k(2k))=0\), including \(k=0,1\). This identifies the cokernel in (QP.13) with the section module.

In the kernel proof, the three-by-three minor \(AD(E_0-B)\) is not divisible by the irreducible cubic \(F\). Thus \(\mathsf B\) has rank three modulo \(F\). From \(Y\mathsf B^t=hI_4\), passage to the fraction field of \(R/(F)\) proves \(F\mid h\). Subtracting \((h/F)\mathsf Q^t\) leaves rows in \(RT\). Multiplication by \(\mathsf B^t\) then proves injectivity of the first map. The report's averaging of the quadratic lift gives the asserted equivariant free decomposition of this kernel; changing that lift only adds a vector in the preceding \(rT^t\) summand. All maps and characters therefore agree.

The negative highest coefficient after multiplying the dimension series by the four parameter factors gives the stated concrete obstruction to regularity of that particular parameter sequence. It does not interfere with the subsequent exact resolution and positive Newton count.

For an independent character calculation, the same jet map (J.1) gives
\[
\boxed{\operatorname{tr}(g\mid\mathcal N_k)
=e_g h_{2k+1}(g)-h_{2k}(g)
-m_1(g)(e_g-1)h_{k-1}(g),}
\tag{J.5}
\]
where \(e_g=m_1(g)-1\). This follows from the actual quotient-bundle exact sequence, with the scalar jet terms substituted. It includes \(\mathcal N_0=\operatorname{End}(E)/\mathbf1\).

I derived its seven rational series by even/odd extraction from \(H(x)\). They agree exactly with (QP.16), and every numerator over \((1-t^{60})^4\) has degree 238. The recurrence calculation from (J.5) reproduces all 1,680 Newton constants, their three closed positive difference formulas, their maximum 197280 and all seven support sets. The coefficient bounds used in the positivity proof are valid because the absolute character values are at most the representation dimensions.

The fixed-residue interpolation applies from \(q=0\), and its degree-three Newton basis gives the displayed positive count. The bounded multiplicity coordinate contributes exactly the fixed integer coefficient; the increasing chain counts the appropriate binomial coefficient. The limits of 240 tags, five variables and four active tags are correct, and the determinant parity gives exactly the two symmetric-outer thresholds.

The independent check script is work/archive/check_q_plus_by_jets.py. Its executed receipt is work/archive/Q_PLUS_JET_RECEIPT.json. The five signed maximal minors and the specified rank-three minor were also independently expanded. The earlier A-029 certificate already independently verifies \(\mathsf B\mathsf Q=FI_4\).


# A-035. Independent complete review of T-041

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

**Status: PASS.** I read the complete report work/theta/outer5/five_point_hook_report.md, equations (5H.1)–(5H.17), including all maps, cohomology, fixed tables and support cases.

## The flag comparison and the exact hook complex

The partition is weakly decreasing for \(a\ge1,d\ge0\), and its size is \(5(d+a+1)\). Its point order is one. After the full determinant factor, the relative quotient-flag weight is \((a,a-1,0)\). The perfect complementary exterior-column pairings in the height-three rectangle give the specified equivariant map
\[
S_{(a,a-1)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,1)}Q.
\]
Together with the first-line twist \(a+2\), this leaves \(\mathcal O(2)\) and the determinant character \(\epsilon^{d+a}\). This verifies the complete linearization in (5H.4), with the actual G-015 chart inverse.

The polarization splitting of
\[
E\otimes\operatorname{Sym}^aE\longrightarrow\operatorname{Sym}^{a+1}E
\]
is valid over \(\mathbf Q\). Its kernel has the displayed highest vector of weight \((a,1)\). In dimensions four and three, its dimensions are respectively \(a(a+2)(a+3)/2\) and \(a(a+2)\), agreeing with the hook Schur functor. Thus the kernel realization specifies the functor and its quotient maps.

The two maps in the hook complex are
\[
l^2\otimes v\longmapsto l\otimes l\otimes v,\qquad
l\otimes e\otimes v\longmapsto e\otimes lv-l\otimes ev.
\]
Their composition is zero. Under a local splitting \(E=L\oplus W\), the coefficients with first tensor factor in \(W\) prove that the kernel of the second map is exactly the image of the first: multiplication by \(l\) is injective in the symmetric algebra. Every element killed by the quotient to \(H_a(Q)\) has the form
\[
\sum_i e_i\otimes lv_i+l\otimes w.
\]
The zero-product condition gives \(w=-\sum_i e_iv_i\), proving that it is the image of the displayed second map. The splitting also proves surjectivity onto \(H_a(Q)\). Hence this is a full exact locally free resolution, including \(a=1\).

## The complete cohomology computation

The untwisted and \(-1\)-twisted complexes involve only the stated acyclic negative line bundles, together with the constant hook space in degree zero. They give \(H^0(B_a)=H_a(E)\), all higher cohomology zero, and acyclicity of \(B_a(-1)\).

For the twist \(-3\), the only possible cohomology map is
\[
H^3(\mathcal O(-5))\otimes\operatorname{Sym}^{a-1}E
\longrightarrow
H^3(\mathcal O(-4))\otimes E\otimes\operatorname{Sym}^{a-1}E.
\]
The first differential multiplies the source by the coordinate vector. On the ordered Čech classes, multiplication by \(x_j\) sends
\[
\frac{1}{x_1x_2x_3x_4x_i}
\]
to the top generator when \(j=i\), and to zero in top cohomology when \(j\ne i\), because one denominator exponent then vanishes. Thus this map has matrix \(\delta_{ij}\). The natural determinant factor on both sides is \(\det E\); the map is an equivariant isomorphism. The two short exact sequences prove acyclicity of \(B_a(-3)\), with no exceptional \(a=1\) term.

Tensoring the already proved five-point resolution by \(B_a(2)\) is exact. Its two left terms are acyclic. Therefore the map that multiplies a quadratic in \(U\) by a constant hook section and then applies \(E\to Q\) is the actual isomorphism
\[
U\otimes H_a(E)\simeq
H^0(\mathcal I_Z(2)\otimes B_a).
\]
This proves the claimed balanced module and dimension in every stated parameter.

## Every fixed table entry and support case

From the actual polarization splitting, the trace series of \(H_a(E)\) is
\[
(\chi_E(g)-t^{-1})\det(1-tg\mid E)^{-1}+t^{-1}.
\]
I independently took its seven exact character inner products and compared them with the printed positive shift lists. All seven rational identities hold identically. I also expanded the cancellation identity (5H.15); it gives exactly the three four-variable and three three-variable tags in the trivial row.

Using the previously independently checked \(U\)-tensor table, the exact numbers of tags are
\[
15,\ 60,\ 78,\ 90,\ 75,\ 60,\ 15
\]
in the report's row order. This verifies the uniform bound 90. The positive weights make every polytope bounded. The sign twist changes the effective label exactly when \(d+a\) is odd.

For either one-dimensional outer label, the effective row is \((3,2)\) or \((2,2,1)\); its least shifts are two and three. The semigroup generated by the weights contains zero and every integer at least two, proving positivity exactly for \(a\ge2\). Every other label receives \((3,1,1)\), whose shifts one and two prove positivity for every \(a\ge1\). These arguments include all allowed initial values and both determinant parities.

The independently written and executed script is work/archive/check_hook_fixed_tables.py. Its receipt is work/archive/HOOK_FIXED_TABLE_RECEIPT.json. It verifies identities in every degree; no larger coefficient sweep is claimed as part of this review.


# The exact two-row quotient complex and its cohomology

Reviewer/contributor: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.

Work over \(\mathbf Q\). Let \(L\hookrightarrow E\) be an inclusion of a line bundle into a rank-four bundle with locally free quotient \(Q\). For integers \(a\ge b\ge0\), the following construction fixes every map in the two-row Schur complex. On the five-point projective space it also proves all cohomology assertions in the region \(c\ge2k\).

## 1. The signed tensor construction

Put \(N=a+b\), and regard
\[
C=[L\longrightarrow E]
\]
as a cochain complex with \(L\) in degree \(-1\) and \(E\) in degree zero. The symmetric group \(S_N\) acts on \(C^{\otimes N}\) by the **Koszul signed** permutation of tensor positions. Interchanging two \(L\)-positions contributes a minus sign; interchanging an \(L\)-position with an \(E\)-position does not.

For a tensor whose \(L\)-positions form \(J\subset\{1,\ldots,N\}\), the differential is the specified map
\[
d(v_1\otimes\cdots\otimes v_N)
=\sum_{r\in J}(-1)^{|J\cap\{1,\ldots,r-1\}|}
v_1\otimes\cdots\otimes\iota(v_r)\otimes\cdots\otimes v_N.
\tag{S.1}
\]
Here \(\iota:L\to E\) is the given inclusion. The two terms that replace any fixed pair of \(L\)-positions cancel, so \(d^2=0\). The signed permutation action commutes with this differential.

Take the row-filled standard tableau \(T\) of shape \((a,b)\). Let \(r_T\) be its row symmetrizer, \(c_T\) its column antisymmetrizer, and \(h_{a,b}\) its hook-length product. Use the explicit primitive Young idempotent
\[
e_T=h_{a,b}^{-1}c_Tr_T\in\mathbf Q[S_N].
\]
For \(N=0\), use the identity on the tensor unit. Define the Schur complex to be the image
\[
\mathcal S_{a,b}(C)=e_T C^{\otimes N},
\tag{S.2}
\]
with differential the restriction of (S.1). Its degree-zero term is the same Young-idempotent realization of \(S_{(a,b)}E\), and its augmentation is induced by the actual quotient \(E\to Q\).

### Exactness and tensoring by a nonflat ideal

Locally choose a splitting \(E=L\oplus Q\). The complex \(C\) then contracts onto \(Q\) in degree zero. Tensoring the contraction gives a homotopy of \(C^{\otimes N}\) onto \(Q^{\otimes N}\). Average that homotopy over \(S_N\). The augmentation and the chosen inclusion of \(Q^{\otimes N}\) commute with the signed action, so the averaged homotopy still satisfies the same contraction identity and now commutes with \(e_T\).

Restricting it to the idempotent image proves that (S.2) contracts locally onto \(S_{(a,b)}Q\). In particular its augmented complex is locally split exact. The homotopy is \(\mathcal O\)-linear; tensoring it with any specified ideal preserves the identity. Thus tensoring this complex with \(\mathcal I^k(c)\) preserves exactness without a flatness requirement on the ideal.

## 2. The three terms and completely specified comparison maps

The term of tensor degree \(-j\) is, before applying \(e_T\),
\[
\operatorname{Ind}_{S_{N-j}\times S_j}^{S_N}
\left(E^{\otimes(N-j)}\otimes L^{\otimes j}\otimes\operatorname{sgn}_{S_j}\right).
\tag{S.3}
\]
The induction map places the \(j\) line factors into the selected tensor positions; its signs are those of (S.1). The sign in (S.3) is essential. In particular the two-line term for an exterior square contains \(L^2\).

Frobenius reciprocity and the exterior Pieri rule identify the idempotent image with
\[
L^j\otimes
\bigoplus_{\nu:\ (a,b)/\nu\text{ is a vertical strip of size }j}S_\nu E.
\tag{S.4}
\]
For completeness, the Pieri multiplicities are exactly one by the alternant identity. Multiplying the alternant for \(s_\nu\) by \(e_j\) is the sum of alternants obtained by increasing \(j\) distinct exponents by one. An exponent collision makes the alternant zero. All other terms remain in decreasing order and correspond precisely to adding at most one box in each row. Dividing by the Vandermonde alternant gives
\[
e_j s_\nu=\sum_{\lambda/\nu\text{ vertical }j\text{-strip}}s_\lambda.
\]
The Frobenius-character isometry used for the Specht projector therefore gives the multiplicity-one branching in (S.4).

Here is an exact finite prescription for the maps in (S.4), which avoids leaving their scalar choices implicit. Realize every Specht module as the rational polytabloid span, with tableaux in lexicographic order. Apply the sign averaging projector on the last \(j\) letters to the Specht module of shape \((a,b)\). For each allowed \(\nu\), solve the intertwiner equations for the adjacent transpositions of \(S_{N-j}\) by rational Gaussian elimination. The preceding multiplicity calculation proves that this solution space is one-dimensional. Choose its first nonzero solution with first nonzero coordinate equal to one. The direct sum of these intertwiners is an isomorphism onto the sign-projected space; invert its rational matrix.

Composition with these inverse projections gives the maps between the corresponding Schur functors. The Frobenius-reciprocity map itself is explicit: an intertwiner \(f\) to the subgroup module is sent to
\[
v\longmapsto\sum_{gH\in S_N/H}g\otimes f(g^{-1}v),
\qquad H=S_{N-j}\times S_j,
\]
and its inverse is projection to the identity coset. Finally the identification with the primitive-idempotent image is evaluation at \(e_T\):
\[
\operatorname{Hom}_{\mathbf Q[S_N]}(\mathbf Q[S_N]e_T,V)
\longrightarrow e_TV,\qquad f\longmapsto f(e_T),
\]
with inverse \(v\mapsto(ae_T\mapsto av)\).

These prescriptions use rational matrices independent of the local frame of \(E\). They commute with frame change, so they define actual bundle isomorphisms. Conjugating (S.1) by them specifies the displayed Schur-functor differentials.

There are at most two rows, so no vertical strip has more than two boxes. The complex is consequently
\[
0\longrightarrow L^2\otimes S_{(a-1,b-1)}E
\longrightarrow
L\otimes\left(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\right)
\longrightarrow S_{(a,b)}E
\longrightarrow S_{(a,b)}Q\longrightarrow0,
\tag{S.5}
\]
with only the valid partition terms retained. The vanishing in degrees \(j>2\) can also be seen directly: three odd line entries in two rows force two identical odd entries in one row, whose graded row symmetrizer is zero.

The boundary conventions are explicit:

- At \(a=b>0\), omit \(S_{(a-1,b)}E\); retain \(S_{(a,b-1)}E\) and the two-line term.
- At \(b=0<a\), the complex is the ordinary symmetric-quotient sequence \(L\operatorname{Sym}^{a-1}E\to\operatorname{Sym}^aE\to\operatorname{Sym}^aQ\).
- At \(a=b=0\), the augmentation is the identity on \(\mathcal O\).
- At \(a=b=1\), the maps are \(l^2\mapsto l\otimes l\) and \(l\otimes e\mapsto l\wedge e\).
- At \(b=1\), decomposing \(E\otimes\operatorname{Sym}^{a-1}E\) by polarization identifies (S.5) with the complete hook complex already checked in A-035.

## 3. Higher cohomology on the five-point projective space

Now take \(E=\mathfrak h_5\) on \(\mathbf P(E)\), \(L=\mathcal O(-1)\), and the actual five-point ideal \(\mathcal I\). Let \(k\ge0\) and \(c\ge2k\). Tensor (S.5) by \(\mathcal I^k(c)\), and place its three terms \(F_2,F_1,F_0\) in cochain degrees \(-2,-1,0\).

The scalar cohomology facts needed here are complete:

1. \(H^{q>0}(\mathcal I^k(c))=0\). For \(k\ge2\) this follows from A-029; for \(k=1\), the degree-two evaluation and its higher-degree versions give it; for \(k=0\), it is the usual cohomology of \(\mathcal O(c)\).
2. \(H^2(\mathcal I^k(m))=0\) for all the twists in the complex. The finite-support quotient \(\mathcal O/\mathcal I^k\) has no higher cohomology, and \(H^2(\mathcal O(m))=0\) on \(\mathbf P^3\).
3. \(H^3(\mathcal I^k(m))=0\) for these twists, because \(m\ge c-2\ge-2\) and \(H^3(\mathcal O(m))=0\) there.

The cohomology spectral sequence for this bounded complex has no term of positive total degree: \(F_0\) has only \(H^0\), and the only possible additional cohomology of \(F_1,F_2\) is \(H^1\), in total degrees zero and minus one. The complex is quasi-isomorphic to the displayed quotient sheaf in degree zero. Therefore
\[
\boxed{
H^{q>0}\!\left(\mathbf P(E),
\mathcal I^k(c)\otimes S_{(a,b)}Q\right)=0
\quad(a\ge b\ge0,\ k\ge0,\ c\ge2k).
}
\tag{S.6}
\]
This proof includes \(k=1,c=2\). Possible \(H^1(\mathcal I(0))\) and \(H^1(\mathcal I(1))\) appear only in nonpositive total degrees; no additional assertion about a map between them is needed for (S.6).

## 4. The exact Euler representation and jet evaluation

Write \(\chi(\mathcal I^k(m))\) for the exact alternating cohomology class. The locally split complex and (S.6) give
\[
\begin{aligned}
[H^0(\mathcal I^k(c)\otimes S_{(a,b)}Q)]
={}&[S_{(a,b)}E]\,\chi(\mathcal I^k(c))\\
&-\left([S_{(a-1,b)}E]+[S_{(a,b-1)}E]\right)
\chi(\mathcal I^k(c-1))\\
&+[S_{(a-1,b-1)}E]\,\chi(\mathcal I^k(c-2)),
\end{aligned}
\tag{S.7}
\]
with the same valid-partition convention.

Every twist here is at least \(-2\). The actual jet-coordinate map of A-033 gives
\[
\operatorname{tr}\bigl(g\mid\chi(\mathcal I^k(m))\bigr)
=h_m(g)-m_1(g)h_{k-1}(g),
\tag{S.8}
\]
where \(h_m=0\) for negative \(m\). The invariant form identifies the symmetric powers of \(E^*\) with those of \(E\). At \(k=0\), the jet term is zero. At \(k=1,c=2\), the three scalar classes are respectively \(U,-\mathbf1,-E\), so (S.7) retains both exceptional scalar cohomology contributions exactly.

Equations (S.1)–(S.8) provide the maps, all boundary cases, the required vanishing and the exact finite-group Euler character for every two-row quotient shape in the stated region.


\part{Unresolved questions and exact remaining gates}


# Unresolved items and exact next operations

G-009–G-011 prove terminating positive formulas for every coefficient and every actual canonical-map image multiplicity. Uniform polynomial bounds on their preprocessing and witness data remain open. The exact missing bounds concern the Hilbert basis, invariant list, and elimination presentation.

The complete direct outer-degree-four formula is proved in T-037, including every central unequal-gap shape. G-015 identifies every outer coefficient with an explicit projective-frame ideal power on a flag variety. T-038 and A-029 evaluate the five-point algebra and ordinary powers. G-020 evaluates all symmetric quotient powers for c≥2k, and G-021 evaluates all two-row quotient powers throughout that range, with122 active positive terms and155 exact support exceptions. Its balanced multiplication and complementary-column pairing cover all λ2+λ3≤2n and all λ3+λ4≥2n. The direct outer-five gate is now precisely λ2+λ3>2n>λ3+λ4, or c<2k in the first chart. The adjacent boundary and the actual line-obstruction cohomology are under active proof and review.

For the canonical map, G-013 gives prime-adjacent semigroup preimages, G-014 the complete long-first-row range, and R-016 determines three finite boundary kernels. R-017 identifies common polarization with exact block truncation; R-018–R-020 eliminate its complete second-row range and first-row boundary band. R-021–R-023 construct an injection of the critical canonical annihilator into the remaining common kernel tensored with one row, after removing the rectangular prolongation by an actual preimage. Its remaining first-factor labels have first row at least r²+1 and second row at least r(r−1). R-024 gives explicit recursive second-row ranges from the full degree-five base and every established square base. R-025 removes two further infinite critical components, and R-026 gives a multiplicity-one actual image at every degree r²−r+1≤b≤r²−2, with an explicit parity-dependent label. The complete varying critical-boundary kernel remains the next rank gate; all component statements retain their actual maps.

For width seven, T-018 evaluates the end-node sector and G-010 supplies a general finite count. The smaller direct-formula gate is the remaining discriminant-valuation filtration on the stated G2 invariant spaces.

The archive has 123 assertion rows, of which 18 retain precise gates after inspection of all thirteen original target leaves and relevant neighboring pages. These include admitted crystalline Lefschetz/freeness inputs, the projected motivic self-duality map, reconstruction from one unlabeled triangulation, and the unspecified completed characteristic-class target. Literal type errors are refuted with their corrected maps proved. The full classification of coefficient rings remains open after the DVR theorem and explicit local counterexample.

The Alpöge theorem is accepted as requested. Its transfer to the projectors and canonical-map image in this paper still needs the explicit equivariant representation/period morphism. The named Lean source files and scan report are absent. The requested Masullo work has no supplied statement or identifier. No locator or missing comparison has been invented.

No formal progress review is due before three elapsed hours, at 03:01:08 Europe/Berlin. This checkpoint retains active work and makes no assertion that the stopping rule has been reached.
