# F30 supplement: a regular mixing repair and the exact commutant jump

Author/checker: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 UTC. Verification type: direct algebraic proof in the actual tower-rank-four, six-dimensional module. This supplement does not change the independently reviewed F30 obstruction report. It adds a constructive comparison at this one module and an exact limitation on lifting its classical projectors.

## 1. Fixed objects and source input

Use exactly the notation and fixed lattice of `agent_nonstandard_tower_specialization.md`:

\[
R=\mathbb Q[v,v^{-1}]_{(v-1)},\quad K=\mathbb Q(v),\quad k=R/(v-1)=\mathbb Q,
\]
\[
M_R=\mathsf S_{(3,1),R}\otimes_R\mathsf S_{(2,2),R},
\qquad \operatorname{rank}_R M_R=6.
\]

Let `A_R` be the actual nonstandard algebra at **tower rank four**, acting on this ordinary Specht tensor lattice by its specified generators `P_1,P_2,P_3`. Its generic action factors through the actual two-row nonstandard Temperley–Lieb quotient. Blasiak, arXiv:1201.2209v2, **Theorem 5.1, printed p.14**, states that this quotient over `K=Q(v)` is split semisimple and that the module labeled by the distinct pair `{(3,1),(2,2)}` is simple. I directly reread this full theorem and the adjoining Proposition 5.2 in the local primary text `primary_sources/Blasiak_1201_2209.txt`; split semisimplicity is explicitly part of the statement, so its simple module has endomorphism field `K`.

The reviewed F30 proof establishes

\[
M_K|_{A_{3,K}}=N(\delta)\oplus N(D-2)\oplus\epsilon_+\oplus\epsilon_-,
\tag{M1}
\]
\[
M_1=[(3,1)]\oplus[(2,1,1)],
\qquad \delta=v+v^{-1},\quad D=\delta^2.
\tag{M2}
\]

At specialization the image of `A_R` is the diagonal `k[S_4]` action: `P_i=2(1+s_i)` in that diagonal action, and hence `s_i=P_i/2−1` belongs to the specialized image. All conclusions about the special commutant below concern this actual action; they do not require the abstract specialization of the algebra to embed faithfully in the ambient tensor algebra.

## 2. Four regular penultimate summands

Let `p_+` be the regular ordinary `H_3` trivial projector from F30, and put

\[
E_R=M_R(p_+\otimes1),\qquad J_R=M_R((1-p_+)\otimes1).
\tag{M3}
\]

These are complementary `A_{3,R}`-stable direct summands of ranks two and four. The first is the saturated plane already used in F30. Their generic types are

\[
E_K=N(\delta),\qquad
J_K=N(D-2)\oplus\epsilon_+\oplus\epsilon_-.
\]

Use the actual regular rank-three algebra decomposition from F19,

\[
A_{3,R}\simeq R\times R\times M_2(C).
\]

Its three central block idempotents belong to `A_(3,R)` over this ring; no difference between the two roots of the center is inverted. Call them `z_+`, `z_-`, `z_mat`. They commute with the ordinary projector in (M3), so define

\[
L_{+,R}=J_Rz_+,\qquad L_{-,R}=J_Rz_-,\qquad F_R=J_Rz_{\rm mat}.
\tag{M4}
\]

They are direct summands with generic ranks one, one and two. Since `R` is local, each is free of that rank. Thus

\[
M_R=L_{+,R}\oplus L_{-,R}\oplus E_R\oplus F_R.
\tag{M5}
\]

The generic fibers of `L_(+,R),L_(−,R),F_R` are respectively `epsilon_+`, `epsilon_-`, `N(D−2)`. This construction does not attempt to separate the two matrix-center branches by dividing by their colliding root difference. It first separates `E_R` from `J_R` by the regular **ordinary** parabolic projector, and only then uses the three regular block idempotents inside `J_R`.

At `v=1`, these four summands have diagonal `S_3` types

\[
L_+=\mathbf1,\qquad L_-=\mathrm{sgn},\qquad E=[(2,1)],\qquad F=[(2,1)].
\tag{M6}
\]

In the real orthogonal model from F30, `E=Rw tensor W`, where `w=(1,1,1,−3)` and `W` is the standard representation on the three pairings. The complementary first-factor plane is the standard `S_3` representation `U_0=w^perp` inside the sum-zero `S_4` representation. Accordingly `J_1=U_0 tensor W=1⊕sgn⊕[(2,1)]`, and `F` is its unique standard summand. The block projections at specialization are the usual central `S_3` isotypic projections, so this is the same `F` as (M4), not an arbitrarily chosen second copy of the standard representation.

The real model is used only to prove the exact rational identity in the next section. All actions, decompositions and ensuing basis constructions are defined over `k=Q` and lift over the stated `R`.

## 3. The class sum exchanges the two standard planes

Let

\[
Z=\sum_{1\le i<j\le4}(ij)
\]

act diagonally on `M_1`. The complete F30 compression calculation gives

\[
\Pi_E Z\Pi_E=0,
\tag{M7}
\]

where `Pi_E` is the orthogonal projection onto `E`. Its exact coefficients were `1` for the three internal transpositions and `−1/3` for the three external ones, and both corresponding transposition sums vanish on `W`. The scalar of `Z` on the two constituents in (M2) is respectively `+2` and `−2`; hence

\[
Z^2=4\,\operatorname{id}_{M_1}.
\tag{M8}
\]

The operator `Z` commutes with the diagonal `S_3`. By (M6), an `S_3`-homomorphism from the standard module `E` has no component in `L_+` or `L_-`. Thus `Z(E)` lies in `E⊕F`. Equation (M7) removes its `E` component, so `Z(E)⊂F`. Equation (M8) makes this map injective, and both spaces have dimension two. Consequently

\[
Z(E)=F,\qquad Z(F)=E.
\tag{M9}
\]

The map

\[
J=Z/2:E\longrightarrow F
\tag{M10}
\]

is an `S_3`-isomorphism with inverse `Z/2:F->E`. In the real model it is an isometry because `Z` is self-adjoint and `Z^2=4`.

The two graph planes

\[
G_+=\{x+Jx:x\in E\},\qquad
G_-=\{x-Jx:x\in E\}
\tag{M11}
\]

are the `+2` and `−2` eigenspaces of `Z` inside `E⊕F`. Indeed

`Z(x±Jx)=2Jx±2x=±2(x±Jx)`.

Restriction of the classical Specht modules to `S_3` gives

\[
[(3,1)]|_{S_3}=\mathbf1\oplus[(2,1)],\qquad
[(2,1,1)]|_{S_3}=\mathrm{sgn}\oplus[(2,1)].
\]

Therefore the actual two classical constituents inside the fixed specialization are

\[
[(3,1)]=L_+\oplus G_+,\qquad
[(2,1,1)]=L_-\oplus G_-.
\tag{M12}
\]

This constructs the missing comparison explicitly at this module. It complements rather than contradicts F30: every individual vector in `E` mixes the classical constituents, whereas the paired combinations `x±Jx` separate them.

## 4. A regular change of basis mixing only corresponding path pairs

The construction can be realized by a regular change of the actual generic tower path basis, without changing the fixed lattice.

Let

\[
e=P_1/D\in A_{2,R}.
\]

It is an idempotent because `P_1^2=DP_1`, and `D` is a unit in `R`. Its complementary idempotent is `1−e`. On each of `E_R,F_R` the images of these two idempotents have rank one: this holds generically in `N(delta)` and `N(D−2)` and the images are projective direct summands. Choose bases

\[
x_{+,R}\in E_Re,\quad x_{-,R}\in E_R(1-e),\qquad
f_{+,R}\in F_Re,\quad f_{-,R}\in F_R(1-e).
\tag{M13}
\]

The four generic lines in (M13) are precisely the tower paths through the two standard penultimate summands, with their matching rank-two scalar labels. They have regular nonzero reductions by construction. Together with bases of `L_(+,R)` and `L_(−,R)`, they form an `R`-basis of `M_R` consisting of representatives of the six generic path lines.

At specialization `e=(1+s_1)/2`. The map `J` commutes with `s_1`, so it sends the `+` line of `E` to the `+` line of `F` and the `−` line to the `−` line, in each case nontrivially. Hence each reduced `f_sigma` is a nonzero rational scalar multiple of `Jx_sigma`. Rescale `f_(sigma,R)` by the corresponding constant unit in `Q*⊂R*` so that its reduction is exactly `Jx_sigma`.

Now replace the pair `(x_(sigma,R),f_(sigma,R))`, separately for `sigma=+,-`, by

\[
g_{\sigma,+}=x_{\sigma,R}+f_{\sigma,R},\qquad
g_{\sigma,-}=x_{\sigma,R}-f_{\sigma,R}.
\tag{M14}
\]

Each change-of-basis block is

\[
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\]

whose determinant is `−2`, a unit in `R`. Thus this is a regular invertible change of basis in the original lattice. The two `g_(sigma,+)` reduce to a basis of `G_+`, and the two `g_(sigma,−)` reduce to a basis of `G_-`. Adding the unchanged bases of `L_(+,R),L_(−,R)` gives a regular basis whose specialization is partitioned into bases of the two classical constituents in (M12).

This positive construction uses non-diagonal mixing of corresponding path lines from **different** penultimate generic summands. It is exactly the freedom left open by the F30 obstruction. It does not change the ordinary Specht tensor lattice and does not require a pole or a colliding-root denominator. It is a construction at the single tower-rank-four example, not a uniform general specialization algorithm, an VIII canonical basis, or a positive structure-constant theorem.

## 5. The classical projectors nevertheless do not lift as regular nonstandard endomorphisms

The endomorphism algebra of the full deformation module is

\[
\operatorname{End}_{A_R}(M_R)=R\,\operatorname{id}.
\tag{M15}
\]

**Proof.** Every such endomorphism extends to the generic fiber. By the primary source's split simplicity,

\[
\operatorname{End}_{A_K}(M_K)=K\,\operatorname{id}.
\]

The extension of an `R`-endomorphism is therefore a scalar matrix `lambda I` with `lambda in K`. In any `R`-basis of the free module `M_R`, its diagonal entries lie in `R`, so `lambda in R`. Conversely every scalar in `R` is an endomorphism. ∎

At specialization the actual algebra image is the diagonal symmetric-group action, and (M2) has two pairwise nonisomorphic absolutely simple constituents with multiplicity one. Therefore

\[
\operatorname{End}_{A_1}(M_1)=k\times k.
\tag{M16}
\]

The natural base-change map is exactly

\[
k=\operatorname{End}_{A_R}(M_R)\otimes_R k
\longrightarrow\operatorname{End}_{A_1}(M_1)=k\times k,
\qquad a\longmapsto(a,a).
\tag{M17}
\]

It is injective and has one-dimensional cokernel. The two special projectors `(1,0)` and `(0,1)` do not lift to `A_R`-linear endomorphisms: the only idempotents in the local domain `R` are zero and one. In particular the split classical decomposition cannot be a decomposition of the generic nonstandard module into `A_R`-stable direct summands.

The regular mixed basis constructed in section 4 does not claim such a decomposition. Its three-vector groups span direct summands of the **underlying free `R`-module**, whose specializations are classical constituents; those submodules are not `A_R`-stable generically. This is necessary because the generic module is simple. No contradiction exists between a regular specialization-compatible basis and the absence of regular `A_R`-linear projector lifts.

This is the exact additional demand that would fail in a proposed projector realization: requiring the classical central projectors to lift as endomorphisms commuting with the entire nonstandard action over the deformation. Constructions in which new endomorphisms arise only at specialization, or in which the comparison is not required to commute generically, remain available. A geometric purity theorem alone does not specify which of these comparisons is intended.

## 6. Verification record and limited novelty claim

The source theorem supplying split simplicity and the actual generic modules was matched directly to its complete primary statement. The graph-plane formulas, regular pairing of rank-two path labels, invertibility of the two-by-two mixing blocks, and the commutant/base-change calculation were proved here in full. They depend only on the already independently checked F30 compression and rank-three regular block decomposition. No external theorem about a geometric realization is invoked.

Suggested check event: `F30-MIXING-COMMUTANT-PROPOSAL`, exact algebraic construction and proof. A fresh independent checker and a match to any later generated paper supplement should be recorded separately. This report does not claim priority for these elementary deductions.
