# Further exact r=3 consequences: commutants, extensions, and a regular normalized basis

Author: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 Europe/Berlin. These are explicit deductions from the actual algebra and tensor-module calculations in `agent_rank3_specialization.md` and `agent_rank3_tensor_geometry.md`; they are not claims of historical novelty. No root deliverable has been edited.

## 1. Setup

Let `R=Q[v±1]_(v−1)`; all algebraic formulas before the length statement also work over the finite localization `R_0` specified in the earlier reports. Put

\[
\delta=v+v^{-1},\quad D=\delta^2,\quad
z_1=(D-1)/D,\quad z_2=4(D-1)/D^2,
\]
\[
\Delta=z_1-z_2,\qquad
C=R[z]/((z-z_1)(z-z_2)),\qquad L_i=C/(z-z_i).
\]

The previous full proofs establish

\[
A=\check H_3\cong R\times R\times M_2(C)
\]

with its actual named generators, and identify the actual right tensor lattice as

\[
M\cong\epsilon_+^{20}\oplus\epsilon_-^4
\oplus N_1^{16}\oplus N_2^4,
\]

where `N_i` is the standard row Morita module evaluated on `L_i`. Each `N_i` is free of rank two over `R`. The root difference is a nonzerodivisor, and

\[
\Delta=\frac{D-1}{D^2}(v-v^{-1})^2
=u(v-1)^2
\]

for a unit `u` in the local ring.

## 2. Actual centralizer and its base-change failure

**Claim R3-F.** The commutant of the actual tensor action over `R` is

\[
\operatorname{End}_A(M)
\cong M_{20}(R)\times M_4(R)\times M_{16}(R)\times M_4(R).
\tag{D1}
\]

It is free of rank `20²+4²+16²+4²=688`. Over the special fiber `k` at `v=1`,

\[
\operatorname{End}_{A_1}(M_1)
\cong M_{20}(k)\times M_4(k)\times M_{20}(k),
\tag{D2}
\]

of dimension `20²+4²+20²=816`. The base-change map from `(D1)⊗k` into `(D2)` is injective and has cokernel of dimension 128.

**Proof.** The three central algebra blocks separate the scalar plus, scalar minus and matrix-sector modules. For the matrix sector use Morita equivalence; its multiplicity module is `L_1^16⊕L_2^4`. An element of `Hom_C(L_1,L_2)` is determined by the image of one. This image is an `r∈R` with

\[
(z_2-z_1)r=0.
\]

Since `R` is a domain and `Delta≠0`, `r=0`. Similarly `Hom_C(L_2,L_1)=0`, while `End_C(L_i)=R`. The commutant is therefore exactly (D1).

At the special fiber, both `L_i` become the same residue module of `C_1=k[epsilon]/epsilon²`, with `epsilon` acting as zero. The two-dimensional row modules both become the same simple standard module for the `M_2(k)` quotient. Thus their multiplicity spaces merge into `k^(16+4)`, giving (D2). The base-change map on the last two blocks in (D1) is the block-diagonal embedding

\[
M_{16}(k)\times M_4(k)\hookrightarrow M_{20}(k).
\]

Its missing two off-diagonal blocks have dimensions `16·4` and `4·16`, totaling 128. The other two blocks are unchanged. This proves injectivity and the cokernel dimension. ∎

The generic number 688 and classical number 816 are already recorded in GCT IV §12.3, immediately after the two-row tensor example; see the source formulas described in the previous report. The new deduction here is an explicit regular commutant and a precise description of the base-change map and its missing blocks.

**Scope.** This commutant family is itself free of rank 688. It does not follow that its special fiber is the full classical commutant; (D2) proves the failure of that equality. Nor does this alone identify every integral form of the FRT coordinate algebra with the dual of (D1). Generic quantum Schur–Weyl duality and a chosen integral/specialized coordinate algebra are different inputs. The proof must not be summarized as “688 becomes 816 in the same flat algebra.”

## 3. A coherent extension group measures the collision order

**Claim R3-G.** Over the same ring,

\[
\operatorname{Ext}^1_C(L_1,L_2)
\cong\operatorname{Ext}^1_C(L_2,L_1)
\cong R/(\Delta),
\tag{D3}
\]

while `Ext¹_C(L_i,L_i)=0`. In particular each crossed extension group has `R`-length two at `v=1`. For the actual tensor module,

\[
\operatorname{Ext}^1_A(M,M)\cong(R/(\Delta))^{128},
\tag{D4}
\]

so its `R`-length is 256.

**Proof.** Put `f_i=z-z_i`. The relation of `C` is `f_1f_2=0`. There is an exact two-periodic free resolution

\[
\cdots\xrightarrow{f_1}C\xrightarrow{f_2}C
\xrightarrow{f_1}C\longrightarrow L_1\longrightarrow0.
\]

To verify exactness rather than merely invoke a hypersurface theorem, work in the domain `R[z]`: if `f_1h` is divisible by `f_1f_2`, cancellation gives divisibility of `h` by `f_2`; the other kernel is the same argument with indices exchanged. Apply `Hom_C(-,L_2)`. The cochain complex begins

\[
R\xrightarrow{-\Delta}R\xrightarrow{0}R
\xrightarrow{-\Delta}R\xrightarrow{0}\cdots.
\]

Therefore its degree-one cohomology is `R/(Delta)`. Exchanging the indices gives the same answer. Applying `Hom_C(-,L_1)` instead begins `R→^0R→^DeltaR`, whose degree-one cohomology is zero because `Delta` is a nonzerodivisor.

Morita equivalence transports these computations to the `M_2(C)` block. Its crossed multiplicities contribute `16·4+4·16=128` copies. The two scalar blocks contribute no self-extensions because their modules are free over `R`, and different central blocks have zero extensions. This proves (D4). Finally `Delta` is a unit times `(v-1)²`, so each quotient has length two. ∎

For the general collision model `C_m=R[x]/(x(x-t^m))`, the same resolution gives crossed `Ext¹=R/(t^m)` and length `m`. Thus this is a specific coherent functor that retains the collision order which the constant-coefficient étale comparison in the previous report cannot distinguish. There is no inconsistency: the coherent module and its extension group carry additional structure beyond a constant coefficient sheaf and its traces.

The dimension 128 in the commutant base-change failure is also compatible with the usual cohomology-and-base-change obstruction: `(R/(t²))^128` has a 128-dimensional `t`-torsion subspace. The direct block-matrix proof of R3-F is independent of any general derived base-change theorem.

## 4. A regular basis with an explicit normalized structural factor

There is a simple regular center basis in which the sole nontrivial coefficient has precisely the visible squared degeneration factor. Put

\[
y=D^2(z_1-z),\qquad
\lambda=D^2(z_1-z_2)=(D-1)(D-4).
\]

Since `D` is a unit, the affine change from `z` to `y` is invertible over `R_0`, so `1,y` is a regular basis of `C`. Its relation is

\[
y^2=\lambda y,
\qquad
\lambda=(v-v^{-1})^2(v^2+1+v^{-2}).
\tag{D5}
\]

**Proof.** At the two roots, `y` takes values zero and `lambda`. Since evaluation into `R²` is injective, `y(y−lambda)=0`. Alternatively substitute directly in `(z-z_1)(z-z_2)=0`. The factorization follows from `D−4=(v-v^{-1})²` and `D−1=v²+1+v^{-2}`. ∎

Consequently the two scalar block idempotents and the eight matrix elements

\[
E_{ij},\qquad yE_{ij}\qquad(1\le i,j\le2)
\]

form a regular basis of the actual rank-ten algebra. Its products are matrix-unit products with coefficients among `0,1,lambda`; for example

\[
(yE_{ij})(yE_{kl})=\delta_{jk}\lambda\,yE_{il}.
\]

This basis is transported through the explicit isomorphism from the actual presentation. It remains regular at `v=1`, where `lambda=0` and the `yE_ij` span the radical.

The factor after `(v-v^{-1})²` is the centered Tate polynomial of `P²` when `v²` is the Tate variable: `v^{-2}(1+v²+v⁴)`. Its three nonzero Tate-degree dimensions are `(1,1,1)`. This observation is **not** a claim about the consecutive-`v` unimodality convention in VIII, nor does it identify this elementary basis with any source-designated canonical basis, its cells, or its external expansions. The expanded scalar `lambda=v⁴−v²−v^{-2}+v^{-4}` has negative Laurent coefficients.

There is also an elementary alternating geometric interpretation of this one scalar. On writing `Q=v²`,

\[
\lambda=Q^{-2}(Q-1)^2(1+Q+Q^2).
\]

This is the normalized point-count polynomial of `G_m²×P²`: the product has `(Q−1)²(1+Q+Q²)` rational points over `F_Q`. Its compact-support cohomology is mixed Tate, and a Tate twist `(2)` multiplies its Frobenius trace by `Q^{-2}`. Thus the signed factor has a concrete ordinary trace interpretation for this basis coefficient. This is an alternating-trace interpretation, not an assertion that every summand has one cohomological degree or that these traces are a categorification of multiplication/associativity. No monoidal functor or positive multiplicity object is inferred merely from equality of one polynomial.

## 5. Verification and source scope

- R3-F was proved by direct Hom computations and block matrices, with actual multiplicities established by the regular tensor-lattice changes of basis in the earlier report.
- R3-G was checked by writing and verifying the full periodic resolution and its two Hom complexes. The local lengths use the earlier exact order-two formula, not a generic-versus-special dimension heuristic.
- Equation (D5) was checked by direct substitution and factorization. The matrix basis follows from the already proved isomorphism, without claiming preservation of a source canonical basis.
- The product point count is elementary; the standard compact-support trace and Tate-twist interpretation is background already used in the main sign route. It adds no new purity theorem.
- GCT IV §12.3 is cited only for the existing dimensions 688 and 816 and its generic duality context, not as a source for these explicit new extension/center calculations.
- A second independent review of this added report remains pending; no claim is made that the prior review of R3-A–E already covers it.
