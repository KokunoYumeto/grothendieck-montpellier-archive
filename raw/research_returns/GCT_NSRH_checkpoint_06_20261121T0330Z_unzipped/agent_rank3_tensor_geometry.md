# Actual r=3 tensor action and the étale invisibility of collision order

Author/checker: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 Europe/Berlin. This extends `agent_rank3_specialization.md`. All additional assertions below are explicit deductions, not claims of historical novelty or a proof of a GCT canonical-basis conjecture.

## 1. Main gain and exact scope

The coherent model in the earlier report realizes the actual nonstandard algebra but initially used a new faithful module. Here the **particular 64-dimensional tensor lattice used by GCT IV when dim V=dim W=2 and r=3 is identified**, with its named generators, over the same finite localization. Thus action compatibility is proved in this example, not merely generic dimension agreement.

The resulting coherent module is supported on the two branches of the explicit center. It is not a vector bundle on that center. Its chosen regular decomposition and its ordinary constant-sheaf shadows do not establish that GCT VIII's designated bases are IC, parity, or Tate bases. In particular, even the full constant nearby/vanishing-cycle data do not recover the order-two branch collision: an explicit universal-homeomorphism comparison proves this.

## 2. Source inputs and conventions

Use the supplied revised GCT IV source

`sources/LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/Apr13KroneckerGCT4.tex`.

The source facts actually used are:

- §3.1, label `e Hecke algebra def`: `(T_i−v)(T_i+v^−1)=0`; the consistent lower generator is `c_i=C'_i=T_i+v^−1`, with `c_i²=delta c_i`, and the other generator is `C_i=c_i−delta`.
- §6.1, equation label `e T inverse_i act on V`, source lines 2313–2322, printed p. 33: the ordinary tensor-monomial right action. This specifies an integral lattice, not just a generic representation. The entire surrounding subsection was read. The initial report's section number 5.1 was corrected to 6.1 after the independent reviewer's contents check.
- §11.1, Definition 11.1 and equation (93), labels `d nonstandard Hecke algebra`, `e sP definition`: `P_i=c_i⊗c_i+(c_i−delta)⊗(c_i−delta)`.
- §11.6, Proposition 11.14 and equation (110), label `e bar N action`: the two generic two-dimensional modules `N(a_1),N(a_2)`, where `a_1=delta`, `a_2=delta²−2`, with right row matrices specified below.
- §12.3, labels `e ns Schur-Weyl r3` and `e ns comodules r=3`, source lines 4324–4376: the generic two-row tensor decomposition and the dimension check `64=20·1+16·2+4·2+4·1`. We reproduce the multiplicities by explicit regular changes of basis, so the assertion below is stronger than generic decomposition alone.

The §11.1 exponent reversal already documented in the source audit is not used. Every calculation uses the consistent §3.1 normalization. All module matrices act **on the right on row vectors**, exactly as in source equation (110). No left quantum-group/comodule convention is needed for the assertion about this right action.

Put

\[
\delta=v+v^{-1},\qquad D=\delta^2,
\]
\[
R_0=\mathbb Z[1/2,v,v^{-1},\delta^{-1},(D-1)^{-1},(D-2)^{-1}].
\]

All bases below are regular over this ring; `v=1` specializes it to `Z[1/6]`. The local ring `R=Q[v±1]_(v−1)` may be used throughout instead.

## 3. Explicit ordinary tensor-lattice splitting

Let `L=R_0²`, and give `L^{⊗3}` the source's tensor-monomial Hecke action. From the displayed source action of `T_i^{-1}` and `T_i=T_i^{-1}+v−v^{-1}`, the action of `c_i=T_i+v^{-1}` is

\[
\mathbf v_{\mathbf k}c_i=
\begin{cases}
v\mathbf v_{\mathbf k}+\mathbf v_{\mathbf k s_i},&k_i<k_{i+1},\\
\delta\mathbf v_{\mathbf k},&k_i=k_{i+1},\\
v^{-1}\mathbf v_{\mathbf k}+\mathbf v_{\mathbf k s_i},&k_i>k_{i+1}.
\end{cases}
\tag{T1}
\]

The one-dimensional weight spaces `111` and `222` are trivial Hecke modules. On the ordered weight basis `(112,121,211)`, formula (T1) gives

\[
c_1=\begin{pmatrix}\delta&0&0\\0&v&1\\0&1&v^{-1}\end{pmatrix},\qquad
c_2=\begin{pmatrix}v&1&0\\1&v^{-1}&0\\0&0&\delta\end{pmatrix}.
\]

Take the following new row basis:

\[
B_3=\begin{pmatrix}
v^2&v&1\\
-1-v^{-2}&v&1\\
-v^{-1}&-v^{-2}&\delta
\end{pmatrix}.
\]

Direct multiplication gives

\[
\det B_3=(D-1)^2,
\]
\[
B_3c_1B_3^{-1}=
\begin{pmatrix}\delta&0&0\\0&\delta&0\\0&1&0\end{pmatrix},\qquad
B_3c_2B_3^{-1}=
\begin{pmatrix}\delta&0&0\\0&0&1\\0&0&\delta\end{pmatrix}.
\tag{T2}
\]

Thus this weight space is a direct sum of one trivial module and the rank-two standard lattice `U` with

\[
c_1|_U=\begin{pmatrix}\delta&0\\1&0\end{pmatrix},\qquad
c_2|_U=\begin{pmatrix}0&1\\0&\delta\end{pmatrix}.
\tag{T3}
\]

On `(122,212,221)` the two original three-by-three matrices are interchanged. Apply the same basis matrix and then interchange its last two rows. This again gives trivial plus the same standard lattice (T3). Since the determinant of each change of basis is a unit in `R_0`, the actual integral tensor lattice satisfies

\[
L^{\otimes3}\cong \epsilon^{\oplus4}\oplus U^{\oplus2}
\tag{T4}
\]

as a right ordinary Hecke module, where `epsilon` means `c_i=delta`. This is an explicit integral action isomorphism, not a use of generic semisimplicity followed by an assumed integral splitting.

For comparison, the ordinary algebra itself is split over this localization: evaluate on trivial, sign and the matrices (T3). On the six-element basis `1,c_1,c_2,c_1c_2,c_2c_1,c_1c_2c_1` the determinant of the map to `R_0×R_0×M_2(R_0)` is

\[
-\delta(D-1)^3,
\]

also a unit. This is a separate exact consistency check; (T4) does not depend on inferring freeness of a projective module over a nonlocal ring.

## 4. Explicit nonstandard splitting of standard tensor standard

In `epsilon⊗epsilon`, the generator `P_i` acts as `D`, so this is the nonstandard scalar module `epsilon_+`. In `epsilon⊗U` or `U⊗epsilon`, it acts as `delta c_i`, exactly the source module `N(delta)`.

On `U⊗U`, with ordered tensor basis `(11,12,21,22)`, equation (93) and (T3) give

\[
P_1=\begin{pmatrix}
D&0&0&0\\
\delta&0&0&0\\
\delta&0&0&0\\
2&-\delta&-\delta&D
\end{pmatrix},\qquad
P_2=\begin{pmatrix}
D&-\delta&-\delta&2\\
0&0&0&\delta\\
0&0&0&\delta\\
0&0&0&D
\end{pmatrix}.
\]

Define four new row basis vectors by

\[
B_4=\begin{pmatrix}
\delta&-1&-1&\delta\\
0&-1&1&0\\
2-D&-\delta&-\delta&D\\
-D&\delta&\delta&D-2
\end{pmatrix}.
\]

Then

\[
\det B_4=8(D-1)^2,
\tag{T5}
\]
\[
B_4P_1B_4^{-1}=
\begin{pmatrix}
D&0&0&0\\0&0&0&0\\0&0&D&0\\0&0&D-2&0
\end{pmatrix},
\]
\[
B_4P_2B_4^{-1}=
\begin{pmatrix}
D&0&0&0\\0&0&0&0\\0&0&0&D-2\\0&0&0&D
\end{pmatrix}.
\tag{T6}
\]

The first row spans `epsilon_+`, the second spans `epsilon_-` (both generators zero), and the last two rows give exactly `N(D−2)` in the source's convention. Because (T5) is a unit in `R_0`,

\[
U\otimes U\cong\epsilon_+\oplus\epsilon_-\oplus N(D-2)
\tag{T7}
\]

over `R_0` itself. In particular, this splitting never divides by the colliding-root difference `z_1−z_2`.

Combining (T4) for the two ordinary tensor factors with (T7) proves the following.

**Claim R3-D (actual tensor action).** Let `V=W=R_0²`, and let

\[
M=(V\otimes W)^{\otimes3}\cong V^{\otimes3}\otimes W^{\otimes3}
\]

be the GCT tensor-monomial lattice with the nonstandard generators acting by source equation (93). Then

\[
M\cong\epsilon_+^{\oplus20}\oplus\epsilon_-^{\oplus4}
\oplus N(\delta)^{\oplus16}\oplus N(D-2)^{\oplus4}
\tag{T8}
\]

as right modules for the **actual** nonstandard algebra. Every change of basis is regular over `R_0` and specializes in characteristic different from 2 and 3.

Indeed, `epsilon⊗epsilon` occurs 16 times, the two mixed types together 16 times, and `U⊗U` occurs 4 times. Equation (T7) therefore produces multiplicities `20,4,16,4`. The total rank is `20+4+32+8=64`. At `v=1`, both two-dimensional blocks become the ordinary standard representation, giving standard multiplicity 20, together with trivial multiplicity 20 and sign multiplicity 4. The source's dimension check and this specialization agree.

The assertion is about the specified right action. It is not a simultaneous canonical identification of the left nonstandard quantum-group action, all its based-module structures, or the source's proposed canonical tensor lattice. In fact GCT IV's discussion after its later canonical-basis conjecture explicitly warns that the proposed canonical integral form need not equal the tensor-monomial integral form (`source line 7970` in the attached version).

## 5. The actual tensor module on the coherent center model

Keep the earlier algebra isomorphism

\[
A\cong R_0\times R_0\times M_2(C),\qquad
C=R_0[z]/((z-z_1)(z-z_2)),
\]
\[
z_1=1-\delta^2/D^2,\qquad z_2=1-(D-2)^2/D^2.
\]

Let `L_i=C/(z−z_i)`, an `R_0`-free branch module of rank one. For each `a=a_i`, write `q=a/D`; this is a unit in `R_0`. In the source module `N(a)`, the row-basis change

\[
S_a=\begin{pmatrix}1&0\\-q^2&q\end{pmatrix}
\tag{T9}
\]

has determinant `q` and gives

\[
S_a(P_1/D)S_a^{-1}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
\[
S_a(P_2/D)S_a^{-1}
=\begin{pmatrix}1-z_i&1\\z_i(1-z_i)&z_i\end{pmatrix}.
\]

Thus it is exactly the standard row module for `M_2(C)` evaluated on branch `i`, with the same named generators. This supplies the remaining module-action compatibility between (T8) and the coherent algebra model.

To express it geometrically without reversing left/right conventions, take

\[
S=\operatorname{Spec}R_0\sqcup\operatorname{Spec}R_0\sqcup\operatorname{Spec}C,
\]

and the explicitly trivial bundle `E=O⊔O⊔O_C²`, so `A=End(E)`. Let `F` be the coherent sheaf with components

\[
F=(\mathcal O^{20},\mathcal O^4,
\widetilde{L_1}^{\oplus16}\oplus\widetilde{L_2}^{\oplus4}).
\]

Then

\[
M\cong\Gamma\bigl(S,\mathcal Hom_{\mathcal O_S}(E,F)\bigr)
\tag{T10}
\]

as **right** `A`-modules, where the right action is precomposition. On the matrix component this is `E^vee⊗(L_1^16⊕L_2^4)`, i.e. the row Morita module. Using `E⊗F` with an unspecified side would conceal an opposite-algebra convention; (T10) fixes it explicitly.

At `v=1`, both `L_i` become the residue module of the dual-number center. Consequently the radical acts as zero on (T10), in agreement with the actual specialized ambient action. Before specialization, the two branch modules together detect both generic matrix blocks, and their joint annihilator in `C` is zero because evaluation at the two roots embeds `C` into `R_0²`. Thus this is a faithful actual tensor module before specialization. The two scalar blocks are also present.

The matrix component of `F` is not locally free over `C`: its generic branch ranks are 16 and 4, while at the collision its `R_0`-fiber has rank 20 with the central nilpotent acting trivially. It is a specified sum of branch pushforwards. This coherent realization is concrete and action compatible, but by itself has no designated Frobenius, canonical positive graded basis, or efficient basis enumeration.

## 6. Useful independent lattice lemma

The following alternative argument was suggested and proved independently by `/root/rectangular_and_theta`. It is not required by the explicit matrices above, but explains why a local generic identification can sometimes be upgraded safely.

**DVR lattice lemma.** Let `R` be a DVR with fraction field `K`, and let `M,N` be finite free `R`-modules with an `R`-algebra action. If `M_K≅N_K` and the reductions `M_k,N_k` are isomorphic simple modules, then `M≅N` over `R`.

**Proof.** Start with a generic intertwining isomorphism. Multiply it by a suitable power of the uniformizer so that its matrix is integral and at least one entry is a unit. Its reduction is therefore a nonzero homomorphism between the two simple special fibers. It is an isomorphism. The determinant of the integral matrix is a unit, so the integral map is an isomorphism; its inverse also intertwines. This proof does not assert the lemma over an arbitrary nonlocal ring, with reducible special fibers, or in the absence of a generic isomorphism. ∎

## 7. Collision order is invisible to the ordinary étale topos

This section uses an explicit comparison, not an analogy between coherent and étale geometry. Let `R=k[[t]]`, with fraction field `K`, and let `m≥1`. Define

\[
C_m=\{(u,w)\in R^2:u\equiv w\pmod{t^m}\}
\cong R[x]/(x(x-t^m)),
\tag{E1}
\]

where `x` maps to `(0,t^m)`. Each `C_m` is free of rank two over `R`, has two split generic points, and has special fiber `k[x]/x²`.

**Claim R3-E.** For `m≥n≥1`, inclusion `C_m⊂C_n` induces a finite universal homeomorphism

\[
h_{n,m}:\operatorname{Spec}C_n\longrightarrow\operatorname{Spec}C_m
\tag{E2}
\]

over `Spec R`. Its generic restriction identifies the two labeled `K`-points, and its special restriction induces the identity on the reduced `k`-point. Nevertheless the coherent normalization quotient has length

\[
\operatorname{length}_R(R^2/C_m)=m.
\tag{E3}
\]

**Proof.** The inclusion is finite because `C_n` is generated by two elements as an `R`-module and `R⊂C_m`. It is integral. After inverting `t` it is the identity on `K²`. Each special fiber has a single point, with residue field `k`, and the map induces the identity there. Thus the map is surjective and injective on points with identical residue fields. This is a radicial integral surjective morphism, hence a universal homeomorphism. Equivalently, after any field-valued base change the geometric fibers have exactly one point; the closed geometric fiber may be nonreduced, which does not affect universal injectivity.

The difference map `(u,w)↦w−u mod t^m` is a surjective `R`-linear map `R²→R/(t^m)` with kernel `C_m`, proving (E3). The integral closure is `R²`: `R²` is normal and finite integral over `C_m`, and is the product of the normalization of its two generic branches. Its conductor back into `C_m` is `(t^m)R²`: multiplication of a pair by arbitrary pairs preserves the congruence if and only if each coordinate lies in `(t^m)`. Both the normalization-defect length and conductor retain `m`. ∎

By the primary theorem on topological invariance of the étale site, (E2) induces an equivalence of the small étale topoi, compatible with the map to the base trait. This includes the equivalence of ordinary constructible coefficient-sheaf categories and their cohomology; it does **not** identify the coherent structure sheaves as ringed objects. Thus the comparison cannot recover `m` merely by applying ordinary étale operations to corresponding coefficient sheaves. An additional prescribed coefficient object or geometric construction can encode `m` externally; this statement does not prohibit doing that.

Sources freshly opened for the theorem:

- Stacks, Theorem 59.45.2, tag **04DZ**, citing EGA IV 18.1.2: https://stacks.math.columbia.edu/tag/04DZ (`turn909767227view1`).
- Stacks, Proposition 59.45.4, tag **03SI**, étale-topos and cohomology invariance: https://stacks.math.columbia.edu/tag/03SI (`turn909767227view0`).
- Stacks, Lemma 59.91.9, tag **0A4E**, cohomology and finite base change: https://stacks.math.columbia.edu/tag/0A4E (`turn909767227view2`).

The universal-homeomorphism proof and coherent length calculation are our explicit deductions. They are not borrowed claims about the GCT center from these references.

## 8. Nearby and vanishing cycles in the finite collision family

Let `k=F_q`, let `ell≠char k`, and put `X_m=Spec C_m→Spec k[[t]]`. Use unshifted constant `Q_ell` coefficients. At the unique geometric special point, the strict-local geometric generic fiber consists of two geometric points: the branches are already split over `K`. Therefore the defining stalk formula for nearby cycles gives

\[
R\Psi_{X_m}\mathbb Q_\ell=\mathbb Q_\ell^2[0].
\tag{E4}
\]

The inertia action is trivial and the arithmetic residue-field Frobenius acts as the identity, since each branch is defined over `K` and the coefficient sheaf is constant. The special restriction is `Q_ell[0]`, and its specialization map to (E4) is the diagonal map: a constant section takes the same value on both generic branches. Consequently, with the convention

\[
i^*\mathbb Q_\ell\longrightarrow R\Psi\mathbb Q_\ell
\longrightarrow R\Phi\mathbb Q_\ell\longrightarrow i^*\mathbb Q_\ell[1],
\]

one obtains

\[
R\Phi_{X_m}\mathbb Q_\ell=\mathbb Q_\ell[0].
\tag{E5}
\]

There are no higher groups in (E4) or (E5); both displayed Frobenius modules have weight zero. These are unshifted nearby/vanishing cycles; applying a perverse shift would change the reported degree.

No normality or smooth total space was assumed: this is a finite flat family with two branches. Since the unique local finite algebra over a strict henselian base is itself strictly henselian, the stalk calculation is directly the cohomology of two geometric points. Alternatively, finite proper base change gives the same computation. The morphisms (E2) identify this entire constant-coefficient specialization triangle for all `m≥1`; the calculation itself also makes its independence of `m` manifest.

For the actual nonstandard center in the earlier report, complete locally at `v=1` and translate `z` by one root. Its root difference is

\[
z_1-z_2=\frac{D-1}{D^2}(v-v^{-1})^2=u\,(v-1)^2,
\]

where `u` is a unit in characteristic different from 2 and 3. Rescaling the translated coordinate by `u` identifies that completed center with (E1) for **m=2**. The ordinary constant nearby cycles distinguish its two generic branches from its one special point, but not its order-two collision from `m=1` or any other positive order. The coherent conductor and normalization-defect length do distinguish it.

This gives a narrower remaining gate: an ordinary pure nearby-cycle object can be supplied, with explicit spectra; retaining the actual order-two deformation data, the named action and designated positive graded bases requires additional structure. Ordinary purity of the constant nearby-cycle representation alone does not supply that structure.

In particular the constant-coefficient trace families in (E4) and (E5), over every finite extension and in every tensor power, are identical for all `m≥1`: their traces are respectively `2^r` and `1` in tensor power `r` (and `2` and `1` without tensoring). Hence no criterion whose input consists only of these traces, including the paper's F03 sign-trace criterion applied to these specified systems, can recover the conductor exponent `m`. The criterion can correctly prove their weight-zero purity while leaving `m` undetermined. This is an information limitation for this coefficient family; a sheaf endowed with a separately specified nilpotent algebra action or another `m`-dependent coefficient construction carries additional input and is outside this conclusion.

## 9. Verification record

- Read the whole relevant source §6.1 tensor-action subsection, §11.6 matrix/presentation context and §12.3 two-row tensor example directly, not only search hits.
- Derived (T1) from the stated source action of `T_i^{-1}` with the consistent Hecke relation.
- Performed exact symbolic matrix multiplication over rational functions for (T2), (T5), (T6), and the ordinary six-dimensional evaluation determinant. These checks used formal symbols, not numerical sampling.
- `/root/rectangular_and_theta` independently recomputed the entire 4×4 conjugation and the six-dimensional evaluation determinant; both passed exactly. That check preceded this completed report. The 3×3 tensor block and (T9) were checked by this author and remain available for their fresh full-report review.
- The decomposition multiplicities and coherent right-module convention were checked by direct expansion and precomposition, respectively.
- The universal-homeomorphism, conductor and normalization-length proof was checked in full. The nearby/vanishing-cycle computation uses the standard defining stalk formula and was checked in full for this split finite family.
- Primary Stacks statements were opened and read at the exact tags listed above. The initial search also found an author's research discussion of the standard stalk formula citing SGA 7 II, Exposé XIII; no new general nearby-cycle theorem from that discussion is needed for the explicit two-point computation.
- This report does not assert full general-r categorification, positivity of a source-designated canonical basis, a compatible geometric realization functor from coherent sheaves to pure sheaves, or NSRH.
