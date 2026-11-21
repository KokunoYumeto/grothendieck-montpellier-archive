# Grothendieck and geometric dictionary report

Run: `GCT_NSRH_20261121_grothendieck_dictionary`; model: GPT-6 Astra Pro; effort: not exposed. Date: 2026-11-21, Europe/Berlin. This is a research/check report for the root paper, not a claim to have proved a nonstandard RH. New elementary observations below are deductions for this investigation, not claims of originality in the literature.

## 1. The ordinary geometric theorem, with conventions fixed

Use `Q` for the cardinality of a finite field and `v` for the formal Hecke/quantum parameter. They cannot be identified before a realization theorem has been proved. Let `G/F_Q` be split reductive, `B` a Borel subgroup, `W` its Weyl group, `C_w=BwB/B`, and `X_w=closure(C_w)` in `G/B`. Write

`IC_w^u = (j_w)_{!*}(Q_l[ell(w)])[-ell(w)]`.

The superscript `u` records the unshifted convention: its restriction to the open cell is the constant sheaf in degree zero. With this convention the Kazhdan–Lusztig geometric theorem identifies

`P_{x,w}(T) = sum_{j>=0} dim H^{2j}(IC_w^u)_x T^j`.

The relevant local statement is stronger than abstract weight purity: odd stalk cohomology vanishes, and Frobenius eigenvalues in degree `2j` equal `Q^j` (over extensions `Q^n`, their powers equal `Q^{nj}`). It therefore gives both parity and a Tate condition. These facts are explicitly stated in Haines, *A proof of the Kazhdan–Lusztig purity theorem via the decomposition theorem of BBD*, Theorem 2.0.1; the polynomial identification is Theorem 5.0.4. This note is an author-hosted proof, not a search-result paraphrase; full relevant sections were read locally.

For reference, if `(T_s+1)(T_s-v^2)=0`, one common normalization is `C'_w=v^{-ell(w)} sum_{x<=w} P_{x,w}(v^2) T_x`. Different normalized Hecke bases move powers of `v`; they do not alter the nonnegative dimensions in the displayed formula.

The geometric ingredients are distinct:

1. A Bott–Samelson/Demazure proper birational map `pi: X_tilde_w -> X_w`, with `X_tilde_w` smooth, provides a geometric object whose direct image contains `IC_w` as a summand after passage to the geometric category.
2. The fibers admit affine pavings (Haines, Proposition 3.0.2). This supplies even/Tate stalk information for the direct image.
3. Purity and the decomposition theorem transfer the required information to the intersection complex. One must control the Weil structures: a geometric direct-sum decomposition is not automatically Frobenius-equivariant. Haines §4, especially the paragraph after (4.0.1), explicitly warns of this point and then repairs it.
4. The geometric realization identifies the stalk polynomial with the algebraically specified `P_{x,w}`, rather than an unrelated positive polynomial.

No part of this should be abbreviated as “pure eigenvalues have positive coefficients.”

### Precise weight theorems and what they do not say

Deligne, *La conjecture de Weil II*, Definitions 1.2.2 and 6.2.2–6.2.4, Theorem 3.3.1 and Corollaries 3.3.4–3.3.6, distinguish upper weights on compactly supported cohomology from lower weights obtained through duality. For a lisse sheaf of weight `a` on a smooth proper scheme, degree `i` cohomology has weight `a+i`. For a general singular scheme or complex, purity is a condition involving both the complex and its Verdier dual; it is not an assertion of exact weights in every singular stalk.

BBD, *Faisceaux pervers*, Corollary 5.3.2 (printed p. 135) says intermediate extension preserves purity; Theorem 5.3.8 (p. 138) gives **geometric** semisimplicity of a pure perverse sheaf; Corollary 5.4.4 and Theorem 5.4.5 (p. 142) give purity of perverse cohomology and the **geometric** splitting of pure complexes. Proper direct image preserves purity by the weight formalism and duality. Relative hard Lefschetz is a further theorem, BBD 5.4.10. The complex-geometric decomposition theorem is BBD 6.2.5 (p. 163), for proper maps and semisimple complexes of geometric origin.

Arithmetic semisimplicity is not a consequence: immediately after BBD 5.3.8 and before Proposition 5.3.9, the source gives the unipotent Jordan-block sheaf `E_n`, pure of weight zero but not semisimple for `n>1` (pp. 138–139). This directly supports root F5(f).

For a precise finite-field package, let `f:X_0 -> Y_0` be a proper morphism of finite-type schemes over a finite field and let `K_0` be a bounded constructible mixed `Qbar_l` complex, `ell` invertible, pure of weight `w`. Then `Rf_*K_0` is pure of weight `w` (BBD Remark 5.4.9, printed p.143, explicitly recalls this), and its perverse cohomology in degree `i` is pure of weight `w+i` (5.4.4). After base change to the algebraic closure, 5.4.5 and geometric semisimplicity decompose it into shifts of intersection complexes with semisimple local-system coefficients. This is a geometric direct-sum statement; an equivariant splitting of the chosen Weil structures is additional information. If `f` is **projective**, `eta` is the first Chern class of a relatively ample invertible sheaf, and `F_0` is a **pure perverse sheaf**, BBD 5.4.10 (printed p.144) gives `eta^i: pH^{-i}(Rf_*F_0) -> pH^i(Rf_*F_0)(i)` isomorphisms for `i>=0`. Those are the hypotheses for the relative hard-Lefschetz symmetry used in a geometric unimodality argument; properness alone does not supply a chosen ample class.

## 2. Dictionary to the nonstandard target

| Ordinary geometric ingredient | Algebraic target in GCT | Missing datum or restriction |
|---|---|---|
| Split group scheme `G_Z`, its flag scheme and Schubert strata | `H`, an `H`-module `X`, `G=GL(X)`; nonstandard quantum matrix coordinate algebra `O(M_q^H(X))`; dual algebra `B_r^H(q)` | `H_Z`, `G_Z`, and the ordinary representation schemes exist, but the noncommutative quantum algebra is not the coordinate ring of a scheme in the SGA sense. A finite-field realization of its basis coefficients is not supplied. |
| Bruhat order and affine Schubert cells | Cells and subcells conjecturally defined by supports of multiplication/comultiplication coefficients | A combinatorial support relation is not a stratification by locally closed schemes and does not supply stalk functors. |
| Canonical `IC_w` with a specified Weil structure | Candidate bases `CB(S)`, `CB(A_r^H)`, `E(r)` from globalization/minimization algorithms | Basis existence/uniqueness and cell properties require their own conjectures. No identified intersection complex, Frobenius or weight normalization is provided. |
| Proper Bott–Samelson maps; proper convolution correspondences | Multiplication, comultiplication, restriction and tensor operations on nonstandard algebras/modules | No proper morphism/correspondence realizing these operations is constructed. One cannot apply a decomposition theorem to an algebra map alone. |
| Pointwise Tate parity from affine pavings | Desired nonnegative expansion coefficients or sign-normalized factors | Purity controls absolute values, not Tate eigenvalues, parity, or effectivity. These are separate gates. |
| Decomposition into shifted simple objects with nonnegative multiplicities | Positive canonical structure constants and cellular decompositions | Need an effective graded category and a basis-preserving identification of its split `K_0` with the particular algebra. Frobenius trace identities alone live in a virtual group. |
| Relative hard Lefschetz on the multiplicity objects | Symmetry/unimodality of `f(q)` in GCT VIII | Exact purity alone does not imply unimodality. A Lefschetz operator and its isomorphisms must be supplied. |
| Sheaf-function realization and specialization | Recovery of Kronecker/plethysm coefficients and PH1 rules | Need correct specialization, branching/cell compatibility, and an effective parametrization. A nonnegative dimension is not yet an efficient positive counting formula. |

The actual positivity target is nuanced. GCT VIII, subsection “Positivity in the Kronecker case,” Conjecture `cposkroneckerleft`, allows rational nonnegative coefficients for expansions and structure constants of the form `±(q-q^{-1})^a f(q)`, where `f` is bar-invariant, positive and unimodal. In the general plethysm setting, subsections `ssaturationleft`/`snonstdposexp` explicitly discuss negative coefficients and replace simple coefficientwise positivity with saturation and “almost positivity” (`cnonstdposleft0`, `cnonstdposleft1`). A naive theorem asserting nonnegative structure constants without the specified signs, factors, and errors would not be the conjecture under study.

## 3. Root F1–F4 restated as an algebro-geometric conditional theorem

Let `F` be a constructible Weil sheaf on `A^d/F_q`, with extension-field trace functions `t_n`. Assume every complex embedding of every stalk eigenvalue has modulus at most `q^{n a/2}` and the ranks are bounded by `B`. Then `|t_n(x)| <= B q^{na/2}`. Let

`H_k = { (x_1,...,x_k) in (A^d)^k : sum_{i=1}^{k-1}<x_i,x_{i+1}>=0 }`.

Character orthogonality in F1 is the elementary counterpart of using an Artin–Schreier sheaf for the function `h sum <x_i,x_{i+1}>`; the weight function is the trace of the external tensor product `F^{boxtimes k}`. The exact comparison with cohomology is the Grothendieck trace formula. Suppose:

* `R Gamma_c(A^d_bar, F)` has only degree `d` cohomology, with spectral multiset `A`;
* for unbounded `k`, `R Gamma_c(H_k_bar, i^* F^{boxtimes k})` has only degree `kd-1` cohomology, with any explicitly separated background satisfying root F4's sublinear-in-`k` error budget;
* the finite-field trace formulas identify the same spectral multisets over **every** extension;
* all conjugate embeddings satisfy the pointwise estimates;
* an appropriate self-duality supplies invariance of the middle multiset under `alpha -> q^{a+d}/alpha`.

Then root F3 proves purity of the middle cohomology of weight `a+d`. The opposite sign is `(-1)^{kd-1}=-((-1)^d)^k`; multiplication of the path count by `q^n` is the Tate twist `(-1)`. The key conclusion is a bound in the category of Weil representations after compactly supported realization.

This dictionary is exact and does not assume properness of `H_k`: compact supports are used. It also makes the bottleneck visible. Being a hypersurface of dimension `kd-1` does not imply concentration in that degree; the singularity of the quadric, boundary terms, and other cohomology cannot be dropped. If only a complex is given, its trace is virtual and cancellation remains possible. A sheaf that realizes a canonical basis coefficient is also still missing.

Framework locators: SGA 4 XVII §3 (compactly supported direct image and base change), XVIII 3.2.5 (smooth duality); SGA 5 III 4.7 (Lefschetz–Verdier formula), III B 1.5 (Frobenius application), or Deligne SGA 4 1/2, *Rapport*, 3.2 (Grothendieck trace formula). The exact statement numbers of the latter SGA citations are carried as source-located background; this run did not re-prove their general theorems. Weil II 3.3.1, 3.3.4–3.3.6 provide the precise upper/lower-weight comparison. None is a nonstandard quantum realization theorem.

## 4. Elementary positive-cone and purity findings

### GD1. Effective categorification is sufficient, with the missing hypothesis exposed

Let `C` be an additive semisimple category equipped with a formal grading shift `<1>`, and choose simple representatives `L_a` modulo that shift. Suppose every relevant tensor/convolution product admits a finite decomposition

`L_a * L_b ~= direct_sum_{c,j} L_c<j>^{direct_sum m_{ab}^{c,j}}`, with `m_{ab}^{c,j}` nonnegative integers.

If an isomorphism of the split Grothendieck ring with the target algebra sends `[L_a]` to its **specified** canonical basis element `b_a` and the grading shift to multiplication by `v`, then every associated structure coefficient is

`h_{ab}^c(v)=sum_j m_{ab}^{c,j} v^j in N[v,v^{-1}]`.

Proof. The split Grothendieck relation of the displayed direct sum is the equality `[L_a][L_b]=sum_{c,j}m_{ab}^{c,j}v^j[L_c]`. Apply the ring isomorphism and compare coefficients in its specified basis. This proves the assertion. It does not follow from an arbitrary Euler-characteristic `K_0` realization, because in a triangulated Grothendieck group `[K[1]]=-[K]`. It also does not establish symmetry or unimodality without further structure. In the GCT rationally normalized setting one would additionally have to verify that the basis rescalings and factored signs match the conjecture.

Check: whole proof reread; the crucial premise is basis-preserving effective realization, not merely existence of some category. No fault found.

### GD2. Pure does not mean positive trace, and value positivity does not mean coefficient positivity

(a) On `Spec F_Q`, take the rank-one Weil sheaf whose Frobenius is `-1`. It is pure of weight zero, since every conjugate of `-1` has absolute value one. Its Frobenius trace is `-1` over `F_Q` and `(-1)^n` over `F_{Q^n}`. Thus exact purity does not force positive traces, even for an actual sheaf in one degree. The missing condition in the Schubert application is the stronger Tate statement identifying each eigenvalue with a positive power of `Q`, followed by the dimension interpretation.

(b) `p(v)=v^4-v^2+1=(v^2-1/2)^2+3/4` is positive for every real `v`, hence at every finite-field numerical specialization, but has a negative coefficient. Therefore even numerical positivity at every such value does not imply coefficientwise positivity of a canonical polynomial.

Proofs are the displayed computations and the definition of weight. Checked in full; no fault found. These refute the corresponding general implications, not Mulmuley's conjectures.

### GD3. Lambda and gamma identities do not replace an effective cone

In `R(G_m)=K_0(Rep(G_m))=Z[z,z^{-1}]`, let `z` be the class of the standard character. It is a line element, so `lambda_t(z)=1+zt` and `lambda_t(1)=1+t`. The lambda-ring sum identity gives

`lambda_t(z-1)=(1+zt)/(1+t)=1+(z-1)t+(1-z)t^2+...`,

and consequently `lambda^2(z-1)=1-z`, which is not the class of an actual representation: its coefficient at the simple character `z` is `-1`.

Moreover `gamma_t(z-1)=lambda_{t/(1-t)}(z-1)=1+(z-1)t`; the rank-zero input already belongs to the augmentation ideal, but its gamma bookkeeping introduces no positivity order. The effective cone is the separate submonoid `N[z,z^{-1}]`. The lambda-ring identities hold in the group completion and therefore cannot by themselves force a virtual expression to lie in that cone.

Proof. Expand `(1+t)^{-1}=sum_{r>=0}(-t)^r`, and substitute `t/(1-t)` for the gamma identity. Since every rational `G_m` representation is a direct sum of characters, its character coefficients are nonnegative; `1-z` fails this necessary condition. Checked in full; no fault found.

Framework locators: SGA 3 I 4.7.3 (diagonalizable-group representations as graded modules); SGA 6, Exp. V, §§2–3 (lambda operations and gamma operations/filtration), especially Lemma 2.2.1 (p. 315). These SGA 6 references are carried as background/source-location only: the original scan could not be visually inspected or downloaded in this run. A modern transcription was consulted as a finding aid, not used as mathematical authority. The original primary paper of Altman–Kleiman, *Foundations of the theory of Fano schemes*, Compositio Math. 34 (1977), §2.10, explicitly corroborates the locator “SGA 6, V, Lemma 2.2.1, p. 315.” GD3 itself is proved by the displayed formal-power-series calculation; no assertion in that proof depends on the unverified transcription.

### GD4. No automatic absolute Frobenius on a noncommutative coordinate algebra

Let `A=e_12` and `B=e_21` in `M_2(F_p)`. Then `A^2=B^2=0`, hence `A^p+B^p=0`. But `C=A+B` satisfies `C^2=I`, so `C^p=I` if `p=2`, and `C^p=C` if `p` is odd. Both are nonzero. Thus the map `x -> x^p` is not additive in this algebra.

Proof. Direct multiplication of the two matrix units gives the displayed identities. Checked in full; no fault found. This rules out the inference “reduce a noncommutative quantum coordinate algebra modulo `p`, then use its automatic scheme Frobenius.” It does not rule out a separately constructed quantum Frobenius or categorical Frobenius. SGA 3 I §4.2 concerns affine group schemes with commutative coordinate algebras, and I 4.7.2 describes representations as comodules; noncommutative bialgebras preserve part of the algebraic language without becoming schemes.

### GD5. An integral orbit-closure model need not commute with reduction

Fix a prime `p`. Let `G_m,Z` act by scalar multiplication on `A^1_Z` and choose the integral point `f=p`. The orbit map has coordinate homomorphism `Z[t] -> Z[z,z^{-1}]`, `t -> pz`. This homomorphism is injective: the image of `sum_i a_i t^i` is `sum_i a_i p^i z^i`, and the Laurent monomials are linearly independent over `Z`. Hence its affine scheme-theoretic image is all of `A^1_Z`, which is flat over `Z`.

After reducing the chosen point modulo `p`, however, the point is zero and its orbit closure is the single point `0` in `A^1_Fp`. Thus the special fiber of the integral closure is strictly larger than the closure of the reduced orbit. This does not obstruct working over a suitable open subset of `Spec Z`; it refutes only an automatic equality at every prime. Proof and example checked in full. The language belongs to ordinary affine schemes and group actions (SGA 3 I §4), not to a putative quantum scheme.

## 5. Translation of actual GCT coefficient statements

Over a characteristic-zero field, finite-dimensional rational representations of a reductive group are semisimple. Their Grothendieck ring has the irreducible classes as a free abelian basis, and actual objects lie in the positive cone. Kronecker coefficients can be written as the multiplicities in

`Res_{GL(V) x GL(W)}^{GL(V tensor W)} S_lambda(V tensor W)`.

Plethysm coefficients are the multiplicities in `S_lambda(S_mu(V))`. Schur functors on locally free sheaves are the geometric counterparts; lambda operations are exterior powers, and Schur operations are the corresponding symmetric-function expressions. These statements explain ordinary numerical nonnegativity before any RH argument. They do not provide PH1, effective lattice polytopes, canonical basis coefficients, or lower-bound obstructions.

Integral caution: `GL_n,Z`, tensor products, symmetric/exterior powers, and integral Schur functors are available over `Z`, but characteristic-zero semisimple decompositions must not be asserted over `Z` or in characteristic `p`. A Young symmetrizer divided by `|lambda|!` is not an integral projector. One must distinguish an integral Schur construction or filtration from a direct-sum decomposition, and verify specialization separately. Braided quantum representation categories are not automatically symmetric tensor categories with the SGA 6 exterior-power lambda structure.

### Orbit closures, Hilbert and Quot

For a free `Z`-module `M` and an integral form `f`, the ordinary `GL(M)_Z` orbit map into a finite free representation scheme is defined over `Z`. Its affine scheme-theoretic image is defined by the kernel of the induced coordinate-ring map. After tensoring with `Q`, this gives the usual characteristic-zero orbit closure; the image ring is torsion-free as a subring of the coordinate ring of `GL(M)_Z`, hence flat over `Z`. Its special fibers need not equal the scheme-theoretic orbit closures obtained by first reducing `f` modulo a prime: kernel formation need not commute with nonflat base change. Thus ordinary arithmetic models do exist, but no canonical coefficient has yet been identified with their local intersection cohomology.

Projective closures in a projective ambient space can be placed in a Hilbert scheme, and coherent quotients with fixed Hilbert polynomial are represented by a projective Quot scheme under the usual noetherian/projectivity hypotheses. Exact original locator: Grothendieck, FGA/Bourbaki Exposé 221, §3, Theorems 3.1 and 3.2, printed pp. 259–260 (PDF pages 12–13 including the Numdam cover). These parameter spaces do not themselves prove a purity or decomposition identification for the nonstandard basis.

### Motives

For smooth projective schemes and algebraic correspondences one can use Grothendieck's pure-motive vocabulary and then an `l`-adic realization. A spectral purity theorem does not construct an algebraic projector or a positive intersection pairing. A general intersection complex of a singular orbit closure is not automatically a Chow motive supplied by SGA 4/5/6; invoking an intersection motive would require an additional construction. The quantum coordinate algebra has no motive in that framework merely by being called a quantum group.

### Exact ordinary purity statement for a projective model

Let `X/F_q` be reduced, equidimensional, projective of dimension `e`, and let `j:U -> X` be a dense smooth open subscheme. With `ell != char F_q`, define `IC_X^u = j_{!*}(Q_l[e])[-e]` with its natural Weil structure. The constant local system on `U` has weight zero, its perverse shift has weight `e`, and BBD 5.3.2 makes `j_{!*}(Q_l[e])` pure of weight `e`. Thus `IC_X^u` is pure of weight zero. Proper direct image and duality imply that `IH^i(X_bar,Q_l)=H^i(X_bar,IC_X^u)` is pure of weight `i`. If a model's fiber is nonreduced, this assertion is applied to its reduction. This is a legitimate ordinary geometric theorem; it identifies no canonical GCT coefficient with those groups.

For root F15's elementary polarization counterexample, a fully checked source replaces the guessed SGA5 locator: Milne, *Lectures on Étale Cohomology*, version 2.21 (2013), Example 16.3, printed p.109, computes the cohomology of projective space using the Gysin sequence. The general projective-bundle formula is Theorem 23.2, printed pp.139–140. With the conventional Tate twist, `H^0(P^1_bar,Q_l)=Q_l`, `H^2(P^1_bar,Q_l)=Q_l(-1)`, and other groups vanish. Since the hyperplane class is defined over `F_q`, geometric Frobenius acts on degree two by `q`. This data is independent of choosing `O(r)` as polarization, while `dim H^0(P^1,O(rd))=rd+1`. The latter dimension follows directly from homogeneous monomials and was checked independently of the cohomology reference.

## 6. Authentic archival anchors inspected so far

The archive numbers below are the numbers printed at the foot of the Montpellier scans. Each downloaded PDF has an added cover at PDF page 1, so archive scan `s` is PDF page `s+1` (one-based). A new finding of this run does not literally occur in Grothendieck's manuscripts; these are anchors for its language, not claims of historical authorship or proof.

* **Cote 90, scan 17 (PDF page 18)**: visually read. Begins with a flat affine group over `S`, its coordinate algebra, then a group action on a prescheme and quasi-coherent `G`–`O_X` modules. This is an authentic anchor for the equivariant-module/representation-`K_0` dictionary. Scan 19 continues with quasi-coherent modules on an affine scheme; scans 21 and 23 continue equivariance diagrams. No theorem about the nonstandard quantum groups is claimed there.
* **Cote 97, scan 4 (PDF page 5)**: visually read. It discusses Chern classes of regular representations, decomposition into characters, and product formulas. This anchors the characteristic-class interpretation of representation operations, not positivity of plethysm or the virtual-cone lemma GD3. The file's catalogue title is “Classes de Chern des représentations.”
* **Cote 133, scan 18 (PDF page 19)**: visually read at full resolution. It has the exterior- and symmetric-operation generating functions, including the relation `sigma_t(E) lambda_{-t}(E)=1`, formulas for a line element, and a map to representation rings. This is an authentic anchor for the operations used in GD3, but it does not assert GD3 or any coefficient-positivity theorem.
* **Cote 133, scans 19–21 (PDF pages 20–22)**: visually read. Scan 19 starts with a ring of virtual finite `G`-sets and operations into groups formed using symmetric groups; scan 20 explicitly calls an ensuing operation “pléthisme.” Do not silently identify these finite-set/Burnside-ring constructions with a proved formula for representation-theoretic plethysm coefficients. The catalogue title of the whole cote is **“[Groupes de Witt et formes quadratiques, groupes formels] : notes manuscrites (s.d.), tirés à part (1974)”**; “plethysm” is a content lead, not its official catalogue title.
* **Cote 16, scans 35, 37, 39 (PDF pages 36, 38, 40)**: visually read. These handwritten leaves contain Lefschetz operators, primitive summands/projectors, a complementary middle summand, and formulas relating the operators for a hyperplane section. They provide a genuine standard-conjecture/primitive-cohomology anchor. This audit does **not** certify a full proof of all handwritten assertions. In particular, a cohomological Euler sign in root F3 must not be identified with a positive-definite intersection form merely by citing these leaves.
* **Cote 16, scans 34, 36, 38, 40 (PDF pages 35, 37, 39, 41)** are reused typescript backs: scan 34 begins Max Karoubi's *Cohomologie des catégories de Banach*; the other even-numbered pages show upside-down typescript on injectives/coherent cohomology. Thus the broad “scans 34–40” citation in the Fable lead requires refinement. Scan 34 is a legitimate historical occurrence of a split Grothendieck-group definition, but is not Grothendieck's handwritten argument about a vanishing-cycle pairing.
* **Cote 16, scans 47–49 (PDF pages 48–50)**: visually read. These are a typed letter to Coates. Scan 47 discusses algebraic correspondences realizing duality, algebraic inverses, and rational characteristic-polynomial coefficients. Scan 48 explicitly says that `C(X)` together with the index relation `I(X x X)` implies semisimplicity of the ring of correspondence classes, and connects this with the semisimple-category-of-motives expectation. Scan 49 explicitly proposes including the deduction of the Weil conjectures from conjectures `C` and `A`, in the letter’s own notation. These are **conditional standard-conjecture statements**, not an unconditional substitute for Deligne's theorem or for nonstandard quantum geometry. The semisimplicity sentence is on scan 48, not scan 50. Scan 50 is a separate handwritten algebra-of-endomorphisms lemma.
* **Cote 16, scan 43 (PDF page 44)**: visually read. Another letter page to Coates explicitly cautions about polarization and `l`-independence in positive characteristic. It is useful evidence that the manuscript itself tracks unproved inputs carefully.
* The catalogue also gives **cote 60** as “Fonctions L / Équation fonctionnelle des fonctions L (cas géométrique)” and **cote 16** as “Formalisme algébrique des correspondances et algèbres de Poincaré-Hodge (cf conjectures standard).” Cote 60 was downloaded and thumbnail-inspected, but no exact theorem from its handwritten content is claimed in this report.
* **Cote 1: follow-up selective extraction succeeded.** The earlier full-download/range attempt was stopped; a later strict PDF reader with direct page-tree traversal and cached HTTP ranges extracted only eight target leaves. Each leaf below was visually inspected. The archive stamp, handwritten folio, and one-based PDF page must be distinguished. The handwritten folios are two ahead of the archive stamp in this range.

| Archival scan | Handwritten folio | Original PDF page | Visually verified content |
|---|---:|---:|---|
| 77 | 79 | 78 | Exterior-power, Hilbert/Fredholm operator and trace-norm calculations; heavily revised manuscript. |
| 78 | 80 | 79 | Fredholm determinant and trace formulas, including boxed `det(1+u)=product_i(1+lambda_i)` and marginal `Tr(u)=sum_i lambda_i`; proof is heavily revised. |
| 79 | 81 | 80 | Further determinant/trace calculations, with many cancellations and amendments. |
| 80 | 82 | 81 | Convex functions, epigraphs, supporting affine functions and supremum expressions. |
| 109 | 111 | 110 | Entire functions, products, order/genus and a statement attributed to Hadamard. |
| 110 | 112 | 111 | Entire-function genus, zeros and canonical-product estimates. |
| 111 | 113 | 112 | Canonical products and complex-sector estimates. |
| 112 | 114 | 113 | Positive decreasing sequences, summability and convergence exponents. |

Thus the Fable lead to “sheets 79–80” has a legitimate Hilbert/Fredholm interpretation if it means **handwritten folios**, i.e. archive scans77–78. This audit verifies the visible formulas and locator, not the correctness of the whole handwritten proof or every hypothesis. No `Xi(sqrt(w))/Xi(0)` identity or RH-equivalent positive-operator construction was verified on either interpretation of the requested pages. The entire-function leaves supply only the stated framework anchor; they do not close that bridge.

The reproducible extraction script is `primary_sources/read_selected_archive1.py`. Its two small outputs were `archive_1_selected.pdf` (scans79,80,111,112) and `archive_1_selected_77_78_109_110.pdf`. They are research copies, not intended for redistribution in the deliverable ZIP. Official source: `https://grothendieck.umontpellier.fr/1.pdf`.

### What the archival anchors do and do not establish

The labels `F1`–`F4` and `GD1`–`GD5` name arguments assembled for the present investigation. None is presented as a newly discovered theorem of Grothendieck. The genuine translation is: finite-field trace sums to the SGA 4/5 trace formalism; exact weight statements to Weil II/BBD; effective classes versus virtual classes to split `K_0` and representation rings; exterior/symmetric operations to SGA 6 and cote 133; projectors and positivity of intersection forms to the standard-conjecture language of cote 16. The outstanding nonstandard realization is not supplied by any of these historical texts.

## 7. Source URLs and retrievable web references

Root must open each URL before citing its web reference in chat. The paper may use conventional bibliography locators.

* Haines: https://www.math.umd.edu/~tjh/KL_purity1.pdf — web ref `turn897457529view0` / `turn138642049search7`; downloaded locally as `primary_sources/KL_purity_Haines.pdf`.
* BBD original: https://www.numdam.org/item/AST_1982__100__1_0.pdf — source ref `turn785735283search5`; local `primary_sources/BBD.pdf` and extracted text. IAS copy https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf — ref `turn844527745view0`.
* Weil II: https://publications.ias.edu/sites/default/files/Number40.pdf — ref `turn485874357view1`, exact 3.3.x content at `turn977762259view3`; web-readable primary PDF, local download failed.
* FGA221 original: https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf — ref `turn977762259view0`, source locator check `turn609861491view3`; local `primary_sources/FGA221.pdf`.
* SGA3 I, Gille–Polo re-edition: https://wstein.org/sga/SGA3/Exp1-20jan2010.pdf — ref `turn228166332view0`; exact §4.7 at `turn609861491view2`. Editor-added notes are labeled in the source and should not be attributed verbatim to Grothendieck.
* SGA6 original scan index: https://wstein.org/sga/sga/6/ — ref `turn967559184view2`; individual original scan at https://wstein.org/sga/sga/6/6t_315.html, ref `turn660236797view0`. The clickable JPEG was resolved by web, ref `turn505028294view0`, but the tool exposed no readable image; direct JPEG/TIFF/PDF downloads returned 403. SGA6 is background only, not a fresh original-source check. Modern reconstruction URLs were finding aids and must not be cited as technical authority. Primary independent locator corroboration: Altman–Kleiman, https://numdam.org/item/CM_1977__34_1_3_0.pdf, §2.10, ref `turn991896280view1`, lines 435–441. Publisher metadata confirms Exp. V by P. Berthelot, pp. 297–364: https://link.springer.com/book/10.1007/BFb0066283, ref `turn807521340view0`.
* Montpellier catalogue: https://grothendieck.umontpellier.fr/archives-grothendieck/ — ref `turn485874357view3`, catalogue entries at `turn230764049view0`; actual PDFs are `https://grothendieck.umontpellier.fr/90.pdf`, `/97.pdf`, `/16.pdf`, `/1.pdf`, `/133.pdf`.
* Milne's author-hosted primary exposition: https://www.jmilne.org/math/CourseNotes/LEC.pdf, version 2.21, 2013 — ref `turn809570392view0`; Example16.3 at `turn477079294view0`, lines5502–5556; Theorem23.2 at `turn809570392view2`, lines7126–7161. This is used for the explicit projective-line calculation rather than inventing an SGA5 proposition number.

## 8. Checks actually performed

* Root draft F1–F5: read the entire `MAIN_PROOF_DRAFT.md` and checked each displayed argument. Type: targeted proof check, not independent re-proof. F1 norm-chain and transpose convention correct; F2 pole/Cauchy–Hadamard proof correct; F3 exponent and sign reduction correct; F4 error budget correct. F5 countermodels correct. Clarification requested for arithmetic progressions: bounds on a progression suffice only if the relevant regrouped coefficients do not cancel.
* GD1–GD5: constructed the displayed short proofs and reread them in full; targeted proof checks passed. GD4 independently checked against root's supplied matrices. GD5 is an explicit affine-coordinate calculation, not an assertion that generic spreading out is impossible.
* BBD 5.3.2, 5.3.8, 5.4.4–5.4.6, 6.2.5: used and rechecked the actual statements in extracted original source with surrounding discussion. This is not a re-proof of BBD.
* Haines Thms 2.0.1 and 5.0.4, Prop.3.0.2 and §4: used and rechecked in this run; whole local argument read, including the Weil-structure caveat.
* FGA221 Thms3.1,3.2: used and rechecked statements and hypotheses in original source; no re-proof of representability.
* SGA3 I 4.7.1–4.7.3: used and rechecked in re-edition, respecting editor notes.
* SGA6 V §§2–3: carried as source-located background only. The modern transcription was a finding aid and is not technical authority. Original-scan access attempts did not produce a readable source. Exact p.315 for Lemma2.2.1 was corroborated by an explicit citation in the original Altman–Kleiman paper, which was read; this is a locator check, not a proof check of SGA6.
* Cotes90/97/133/16: catalogue identity and the specific scan contents listed above visually inspected at readable resolution; no claim to have checked full manuscript proofs. The range cited in the Fable lead for cote 16 was corrected, and the distinction between finite-set operations and representation operations in cote 133 was retained.
* Current root LaTeX: read KL section, geometric interpretation of F03/F04, F06–F08, F11, and all of F15. Targeted proof/source-hypothesis check passed, with requests to spell out the pure-IC hypotheses and replace an unverified SGA5 projective-bundle locator by the checked Milne example. An extraneous comma in the exponent of F03's displayed error bound was reported as a typesetting error. No geometric realization was inferred from the ordinary orbit-model construction.
* Root F16: read the entire new proof and checked `E^2=delta^2 E`, the normalized polynomial of `P^1 x P^1`, and the sign-tensor-sign specialization. Passed. The paragraph correctly states degreewise purity and does not call the total cohomology a pure weight-zero representation. The motive expression denotes a Tate direct sum with grading normalization; it identifies no full GCT representation. Suggested wording “rank-one Hecke case” to distinguish Coxeter rank one from this algebra's rank two as an `R`-module.

## 9. Review of the completed Part III and implications

Initial completed-text review snapshot: `agent_grothendieck_review_snapshot.tex`, SHA-256 `ee0bd384f7621d72b92b1e987f7d658ed50b4a5b75d32b8072f6fbd51ed09aad`. Scope: entire Part III, every row of the finding-by-finding dictionary, archival audit, F14–F17 in full, the final sufficient-package conditions, attempted-route table, task states, and relevant bibliography. Also reread F09–F10 and F13 to check the corresponding dictionary rows, and rechecked BBD5.3.1 in the original text. This is a targeted whole-text/proof check within that scope, not a re-proof of all cited literature.

The mathematical conclusions in that scope passed. F17's extension-degree refinement is valid because every root in the positive sum is replaced by its `e_k`th power and collisions still have positive multiplicity; the `(e_k k)`th root removes the extension factor. The separate dual system gives the lower bound using the rational Tate scalar `q^d`; the compact-support/ordinary-cohomology comparison remains explicitly required.

Corrections requested and subsequently observed in the root source:

* The integral projector assertion now applies to the actual integral Specht models, or to a coefficient ring carrying the representation with `|H|` invertible. An arbitrary complex representation need not descend to `Z[1/|H|]`.
* The diagonalizable-group sentence refers to **representations** and graded modules.
* The dictionary no longer asserts the universal negative “no manuscript contains” the new inclusion theorem; it explicitly declines historical attribution.
* The Hilbert/Quot paragraph distinguishes the intrinsic functors from the fixed-Hilbert-polynomial pieces that use a chosen polarization.
* The trace determinant is stated for a bounded complex of **finite-dimensional** Weil representations.
* BBD Remark5.4.9, printed p.143, now explicitly supports proper-pushforward purity in F15 and the bibliography.

The final sufficient-package and incomplete-status paragraphs do not claim that F03/F04 construct a nonstandard realization, an effective basis, a polytope rule, or an obstruction. They distinguish the actual rank-one inherited-cone obstruction from an impossibility theorem for all realizations. F15 keeps polarization and linearization separate from ordinary cohomological purity. F16 distinguishes both degreewise purity and the grading-step issue `(1,2,1)` versus `(1,0,2,0,1)`. These limitations are mathematically appropriate.


## 10. Additional constructive Satake route: ordinary multiplicity spaces

This is a fresh mathematical check of the root’s proposed route. It uses the published primary Richarz paper and the original BBD text. It constructs ordinary classical multiplicity spaces with weights; it does not identify the quantum or nonstandard canonical bases of GCT VIII.

### Precise primary locators

Timo Richarz, *A new approach to the geometric Satake equivalence*, Documenta Mathematica19 (2014),209–246, official PDF `https://ems.press/content/serial-article-files/26224?nt=1` (web refs `turn106538141view0`, `turn790512219view0`, `turn790512219view1`, `turn790512219view2`). Published numbering differs from arXiv1207.5314v2: Theorem3.1, printedp214, proves perverse convolution and the symmetric tensor structure over arbitrary fields. Its proof, pp226–227, gives the parity modification of commutativity and explicitly tracks the Galois action. Proposition4.1, p227, gives geometric semisimplicity. Theorem5.1, p230, identifies the dual group. The projective twisted convolution varieties and semismallness occur pp231–232, Corollary5.3; Lemma5.4’s proof, p232, identifies the twisted external product of IC complexes with the IC of the twisted Schubert product by smooth-local verification. Section6, especially Theorem6.1, p235, treats Galois descent. These statements and their relevant proofs were read; the general Satake theorem is invoked, not reproved.

Original BBD locators additionally rechecked: 5.1.2 p123 (fully faithful descent of perverse sheaves to geometric perverse sheaves with Frobenius; essential image stable under subquotients); 5.1.8 pp126–127 (weight convention and lisse-complex criterion); 5.1.14(i),(i*) p128 (the two weight bounds under operations); 5.3.1 p134 (perverse subquotients preserve each weight bound); 5.3.2 p135, **second proof** (intermediate extensions preserve purity for immersions not assumed affine); 5.3.8 p138 (geometric semisimplicity); Remark5.4.9 p143 (proper pushforward preserves purity). These primary statements were checked directly. The second proof qualifier matters because the first displayed statement of5.3.2 says affine immersion.

### Plethysm construction and purity

Let `G=GL_r/F_q` be split and `ell != char(F_q)`. Fix a partition `mu` of length at most `r`, and let `D_mu=dim Gr_mu=<2rho,mu>`. Use the unnormalized perverse Weil complex

`IC_mu = j_mu,!*(Qbar_l[D_mu])`

with its natural constant-sheaf Weil structure, so it has weight `D_mu`. For `d=|nu|`, the twisted external product of `d` copies is the IC of the twisted Schubert product, of dimension `d D_mu`, and hence is pure of that weight. The restricted convolution map is proper between finite-type projective varieties. Its direct image

`K = IC_mu star ... star IC_mu`

is pure of weight `d D_mu` by BBD Remark5.4.9 and perverse by Richarz Theorem3.1. The parity-modified symmetric constraint is defined over `F_q`, so the resulting `S_d` action commutes with Frobenius. Choose a primitive Young idempotent `e_nu in Q[S_d]` for the partition `nu` (a central isotypic projector would retain an unwanted Specht-dimension factor). Since the perverse category is abelian, `P_nu=e_nu K` exists as an actual direct summand, and BBD5.3.1 gives purity of the same weight. No positivity or self-adjointness of `e_nu` is needed for this purity statement.

Under geometric Satake, the underlying object corresponds to `S_nu(S_mu(Qbar_l^r))`. Therefore, for a partition `lambda`, the vector space

`M_lambda = Hom_geom(IC_lambda,P_nu)`

has dimension the ordinary plethysm coefficient. The next argument shows that its natural Frobenius action is pure of weight `d D_mu-D_lambda`; it does not assume an arbitrary decomposition is Frobenius-equivariant.

### Canonical isotypic decomposition and the Hom weight

More generally, let `P` be a Weil perverse sheaf pure of weight `w`, geometrically semisimple with simple constituents among the naturally defined `IC_lambda`. Set `M_lambda=Hom_geom(IC_lambda,P)`, with Frobenius acting by conjugation through the two Weil structures. The evaluation map

`direct_sum_lambda IC_lambda tensor M_lambda -> P`

is a canonical geometric isomorphism and is Frobenius-equivariant by construction. Since `G` is split, the individual strata, supports and chosen `IC_lambda` are defined over `F_q`; the isotypic summands are separately Frobenius-stable. Full faithfulness and the subquotient statement in BBD5.1.2 justify descent, or equivalently the construction can be stated directly in the Weil category. Each isotypic summand is pure of weight `w` by BBD5.3.1.

Restrict the `lambda` summand to the smooth open orbit of its own support. There it is `M_lambda[D_lambda]`, because the chosen `IC_lambda` restricts to the constant sheaf with Frobenius1. Open restriction preserves both weight bounds (`j^*=j^!`, where the latter means extraordinary pullback), and BBD5.1.8 says that this lisse complex is pure of weight `w` exactly when `M_lambda` is pointwise pure of weight `w-D_lambda`. This proves the claimed formula without arithmetic semisimplicity. In particular, no half Tate twist has been introduced.

For partitions with `|lambda|=d|mu|`, `D_lambda=(r-1)|lambda|-2n(lambda)`. Hence the resulting weight is the even integer `2(n(lambda)-d n(mu))`; its equality to that integer is elementary bookkeeping, not an identification with the grading variable of GCT VIII.

### Kronecker construction

On `Gr_GL_m x Gr_GL_n`, take `A=IC_(1) external IC_(1)`, of weight `(m-1)+(n-1)=m+n-2`. Its Satake representation is the tensor product of the two standard representations. Applying the primitive Young idempotent for a partition `nu` of size `d` to `A^{star d}` gives `S_nu(V tensor W)`. The geometric multiplicity space for `IC_lambda external IC_mu` has dimension `g(lambda,mu,nu)` and is pure of weight

`d(m+n-2)-D_lambda-D_mu`.

The rank constraints are the usual length restrictions on `lambda` and `mu`. The product-category construction uses the same proper finite-type convolution and weight argument.

### GL2 example: purity survives, but a component basis is not permuted

Take `G=GL_2`, `mu=(1)`, `d=2`, and `lambda=(1,1)`. The determinant multiplicity space in `IC_(1) star IC_(1)` has dimension1 and weight2. More precisely it is `Qbar_l(-1)`: the two-step minuscule convolution variety is smooth of dimension2 and the fiber over the determinant lattice is `P^1`; proper base change identifies the relevant degree-zero perverse stalk contribution with `H^2(P^1,Qbar_l)`. A lattice-level description is immediate: intermediate lattices between `tO^2` and `O^2` are the lines in `O^2/tO^2`, hence `P^1`.

Under the **modified symmetric Satake** action, the transposition acts by `-1` on this determinant multiplicity line, since the corresponding classical summand is `wedge^2 V` inside `V tensor V`. A one-element basis is permuted only by the identity; therefore no basis of this line is permuted by that `S_2` action. This is compatible with the existence of a component basis for the convolution multiplicity before asking how the commutativity action operates: it negates this one-dimensional basis. It does not refute positivity of ordinary multiplicities or every possible nonstandard categorification.

The construction narrows the ordinary-purity gate substantially, using existing Satake and Weil-II/BBD machinery. It still supplies no basis-preserving identification with the nonstandard quantum algebra, no positive component rule for Young-projector images, no effective polytope description, and no complexity bound. The symmetric constraint is a sheaf-theoretic isomorphism and its projector may use negative rational coefficients. An algebraic correspondence realization, an effective cycle realization, and an algorithmic counting model are further assertions requiring separate proofs.

## 11. New F19/F20 final-text check and motivic refinement

A second root-source snapshot, `agent_grothendieck_review_snapshot2.tex`, has SHA256 `fa7a864670d6afcb6d791da0557d9ce8661de42c953baf8931f7fc4f0fcc0296`. The new scope checked in that snapshot is the **entire F20 statement and proof**, plus F19’s complete displayed algebra argument and geometric/étale discussion, taking the cited complete IV presentation as an external input. The latter source presentation was not freshly reproved by this reviewer. Both checks passed. The GL2 stalk degree in F20 is correct: the smooth two-dimensional convolution source gives `H^0` of its shifted stalk equal to `H^2(P^1)`, and intermediate extension excludes the other constituent’s degree-zero boundary contribution.

Precision requests sent to root: explicitly retain the natural constant Weil normalization of the twisted IC; specify BBD5.3.2’s second proof for a non-affine open immersion; add Richarz Theorem5.1 p230 for identification with the dual group; add BBD5.1.2/5.1.8/5.1.14 to the expanded source-locator list. These do not change the asserted mathematics. At this snapshot, the old PartIII table, attempted-routes table and archive1 row had not yet been updated for the newer findings; no check of their later versions is claimed here.

The ordinary étale statement used by F19 has now been directly source-checked in Stacks Proposition59.45.4 (tag03SI) and Theorem59.45.2 (tag04DZ). It concerns nilpotent thickening of the underlying scheme. It does not forbid an extra algebra action with nilpotent operators on an étale sheaf or on a vector space. The stated rank-six endomorphism model is a particular replacement and is not a nonexistence theorem for all representations of the rank-ten algebra.

The standalone note `agent_satake_purity.md` now contains SP1–SP4 in full, the new motivic corollary SP5, and the checked GL2 three-step fiber calculation supplied to the rectangular/projector agent. Its current SHA256 is `9e08ce3641d5a3da769f6e3d1f5ca880e6f0737471e9fd4a6db9dca178fb6893`.

SP5 uses Richarz–Scholbach’s published motivic Satake category, not a general inference from l-adic purity to motives. Their Theorem4.1, Proposition4.8, Proposition5.9, Definition6.2, Lemma6.3, Corollary6.4 and Lemma6.5 show that the rational Young-projector image decomposes into actual `IC_lambda(n)` motives. Purity fixes `n=(D_lambda-w)/2`. Its coefficient motive is therefore `1(n)` with the classical multiplicity, and l-adic Frobenius is exactly scalar `q^{-n}`. The ordinary Hom vector space in the motivic category must use the correctly twisted simple object; the untwisted Hom need not be the coefficient motive. This closes arithmetic Jordan ambiguity for this particular classical construction and leaves the quantum-basis and positive projector-label tasks open. Exact source URLs, numbered statements, page mapping, and the relevant 2023 foundational corrigendum check are in the standalone note.

## 12. Subsequent checked routes and current standalone reports

The following reports extend the original dictionary. They are intermediate research records for integration by the root; their individual check scopes and hashes are recorded in `agent_grothendieck_check_events.tsv`.

- **F23 signed projector gate:** `agent_satake_projector_gate_review.md` is a fresh full review of the rectangular agent's SPG1–SPG8. Signed orbit induction, primitive-versus-central projector factors, mixed Young/Pieri counts, explicit witness hypotheses, the GL2 three-step non-signed-permutation example, and the binary-quadratic family all pass. Primary statements were checked; they are not new general counting theorems.
- **F24 signed-even path criterion:** `agent_signed_even_full_review.md` and `agent_F20_F24_final_fragment_review.md` record full independent checks. Real alternating coefficients are sufficient at unbounded even powers. The top visible radius must survive any permitted extension powering. The complex-i countermodel in the final fragment now uses k>=6, k=2 mod4, avoiding duplicate-set notation. Hidden equal roots canceled in Euler degree remain unbounded by this criterion.
- **F26 rational-normalization obstruction:** `agent_rank3_projector_trace_gate_review.md` checks the full analytic proposal, including the general rational-function criterion. `agent_F26_F27_generated_review.md` separately checks the shorter final recurrence/maximal-pole proof. The actual trace was reconstructed independently from the ordinary tensor action: the four eight-dimensional traces are 4D+2, 2-2D, 2-2D,2, whose squares sum to 24D^2+16. The normalized trace 24+16/D^2 is therefore basis independent. The all-extension word-trace comparison with one fixed finite Weil complex fails; fixed-parameter actions and other dictionaries remain possible.
- **F27 derived and character-cone route:** `agent_rankone_derived_gate.md` gives complete elementary proofs of the inherited-KL-cone parity obstruction, the specified zero-differential lift's homotopy amplitude, the separate exact-fiber cohomological amplitude law, the four-character positive action model, and the localization trace limit. The four-point model retains both equal-sign character actions. Its Tate object has weights -2,0,0,2, and its effective cone differs from the integral KL cone. Algebraic scalar localization does not automatically become an all-extension finite trace. Root independently reviewed this note; the generated fragment received a direct full reread here, with an explicit abelian-category qualifier requested for the cohomological statement.
- **F31 primitive Grassmannian route:** `agent_grassmannian_primitive.md` gives the exact construction for equal rectangles and a two-row output. The Plücker map is H^{2r-2}(-1)->H^{2r}; its cokernel is Q_l(-r)^g for g=g((nd-r,r),(d^n),(d^n)). On V_j=H^{2j}(j), E_r=Id-L B_r^{-1}A_r is an explicit Frobenius-equivariant primitive projector. Its motivic inverse exists within the full rational matrix Hom spaces of the cellular Tate motive, not by assuming the standard conjectures. For Gr(2,4), the prescribed primitive-versus-Lefschetz integral decomposition has index2, while a different-kernel integral projector still exists. This report has an author check; fresh independent review is requested.

New primary inputs for the last route are Pak–Panova, QBC23 author manuscript (13 October 2016), Lemma1.3 p2; Brosnan, author `bb.pdf`, §2 pp3–4 and Theorems3.3/3.5 pp5–6; and BBD Theorem5.4.10 p144. The newer Pak–Panova–Swanson paper (4 November 2025), arXiv2511.02312, Lemma1.3(2) p2 and Theorems1.1/4.5,1.2/5.2, already gives positive marked-tree interpretations for the equal-rectangle/two-row and two-row-output plethysm families. Its numerical-size computation discussion must not be silently converted into succinct binary PH1. The paper's complete proofs were not independently certified here; the relevant exact statements were inspected, and a minor subscript typo in the proof of Lemma4.2 was flagged to the rectangular agent.

The original PartIII/archive review remains valid within its earlier saved scope. The root is extending the final dictionary to these new findings; a final whole-PartIII check must use the eventual final-source hash rather than retroactively treating old snapshots as current.


## 13. Rectangular hooks: exact group-scheme realization and mixed weights

The additional note `agent_rectangular_hook_geometry.md` applies IP Proposition 6.4 to the explicitly displayed split-group motive formula in Merkurjev, Introduction (1.1), p. 1. It realizes all equal-rectangle hook coefficients by ordinary cohomology of SL_m, where m is the minimum side. The formula is read in a primary research paper and its attribution to Biglari is preserved; Biglari's original proof was not retrieved. Subset Tate summands have degrees 2s−|I| and weights 2s, so a fixed cohomological degree can be mixed. H15(SL8)=Ql(−8)⊕Ql(−9) is the first displayed example here. No nonstandard action or canonical basis is supplied by this numeric coefficient realization.

A targeted read of the evolving Part III found two integration points: distinguish normalization of F27's coefficient Hecke algebra from the geometric support correspondence of a Soergel bimodule, and update the approach table to record F27's qualified repair of F16's action mismatch. Both were reported to the parent before final integration. The F27 abelian exact-fiber qualifier and the F22 Q_ell TeX typo have been corrected in the main text.


## 14. Actual stack completion and the exact duality limit

The complete F35 proposal is `agent_stack_trace_realization.md`. The fixed finite-type Artin stack, consisting of 24 points and 16 copies of A6 times Gm8 times BGL2 to the fourth power, realizes the actual F26 normalized word trace for every finite extension. Sun's published trace theorem and exact BGL2 compact-cohomology computation, together with the original Laszlo–Olsson II duality/Kunneth statements, were inspected. Explicit graded Tate cohomology proves unbounded negative compact degrees, absolute convergence, and the precise signed countable Euler expansion. Poincare duality exists; its ordinary dual has unbounded visible eigenvalue support, so F17/F32's independent dual upper bound is not supplied. No nonstandard generator/correspondence action is constructed by the scalar realization.

The full F30 mixing supplement was independently checked and passed: `agent_F30_mixing_review.md`. The regular graph-plane basis change is compatible with the absence of generic commuting projector lifts. Its target hash and exact review scope are in the check-event log.


## 15. Trace inversion versus an actual tensor inverse

The F38 proposal `agent_trace_inverse_tensor_gate.md` gives the explicit stack Z=A1×Gm2×BGL2 of mass 1/(Q+1), and its product with P1 has mass one in every extension but nonzero negative compact cohomology. It proves directly that ordinary RΓ(P1) cannot become tensor-invertible within the usual unbounded derived Weil realization. The necessary total-cohomology dimension-one condition for tensor units is proved by Kunneth over a field; it does not rely on semisimplicity of Weil representations. The normalization factor D(Q)=Q+2+Q^-1 has a stack inverse at the level of convergent Euler trace sequences but cannot be the trace of an invertible derived Weil object. Thus a formal coefficient localization is distinct from an object-level tensor localization that preserves the specified realization. No claim is made against fixed-parameter scalar division or different completed trace formalisms.


## 16. Finite-algebra smoothness test and the actual plethysm ray algebra

The complete F39 generated-fragment review is `agent_F39_fresh_review.md`. The actual dual-number collision block has the explicitly checked infinite bimodule resolution, so its positive Hochschild homology never terminates and its perfect dg category is not smooth. This excludes that direct input from the cited smooth proper noncommutative Weil framework; good split fibers are instead Morita equivalent to four points. Tabuada v7 exact source definitions and comparison equations were inspected, not its full general proof. The source action locator should include equations (7.3)–(7.4) in addition to (7.1)–(7.2).

The full fresh review `agent_plethysm_ray_algebra_review.md` passes the rectangular agent's explicit ordinary highest-weight algebra B=Q[f2,...,fk], with deg fi=i. The triangular slice calculation and the degree-minus-index grading prove the global ray statement directly, with characteristic zero essential. Its monomial basis lies in the actual multiplicity algebra. This constructive result coexists with the F34 compact-input dimension obstruction and does not identify a nonstandard canonical basis.

The requested F38 full LaTeX proof and separate dictionary paragraph are now in `finding_F38.tex`; its author fragment check and hash are recorded separately from any parent fresh review.


## 17. A direct smooth categorical repair of the collision fiber

The F40 note agent_auslander_collision_repair.md constructs the actual five-dimensional Auslander algebra Gamma=End_B(B plus k), with B the dual numbers. Its diagonal has the explicitly proved length-two projective resolution of dimensions 4 to 12 to 13 to 5. Lambda=k squared times M2(Gamma) is smooth proper, with the actual A1 as an idempotent corner and the actual 64-dimensional specialized tensor module as Hom between two projective objects. The 104-dimensional projective lift recovers its action exactly through the corner. Perf(A1) embeds fully faithfully but not right-admissibly, and the nonperfect module is recovered by restriction rather than by a perfect-module embedding. A full exceptional pair proves the motive has four unit summands; the cited Frobenius-enriched TP functor therefore has four even eigenvalues one and no odd part. This repairs the direct smoothness gate without identifying based operations or the relative collision order. Root and gct have been asked for independent full review.
