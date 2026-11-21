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


## 18. Relative smooth repair and the precise Frobenius comparison defect

The complete F44 report agent_relative_auslander_repair.md retains the actual relative algebra as a corner of a smooth proper rank22 algebra over the base. The rank5 basic endomorphism algebra End_C(C plus L1) has an explicit finite relative diagonal resolution, so no unverified tacnode Auslander-order theorem is used. A perfect rank96 lift recovers the actual rank64 tensor lattice through Hom, and one oriented Ext contributes (R/Delta)^64, preserving the collision order while explicitly losing the other original orientation. Root has independently full-checked the report; gct fresh review is pending at this entry. The chosen noncommutative ring Frobenius lifts ordinary Frobenius on the commutative corner, but a unit extension-of-scalars structure over the larger algebra has a nonunit underlying base linearization. The exhaustive fixed-vertex lift condition uv=Delta^(p−1) proves the scoped tradeoff. This is distinct from cyclotomic TP Frobenius and from a Weil realization.

F41 gives a different precise distinction: finite weight windows of the actual stack cohomology restore finite spectral support and cannot retain the entire normalized extension trace, although an effective 64-dimensional subquotient supports the fixed-q action after a choice. F42 has now received a full fresh review here, including its stronger all-word pole-count obstruction and its valid fixed-q tensor-family construction. These results distinguish coefficient objects, actual fixed-parameter operators, and extension-wise parameter substitution.

## 19. Later full reviews, the exact Cayley model, and source-locator corrections

The F44 report and its full generated fragment have now passed both root and gct whole-proof review. The final parent-updated fragment hash at this entry is31135b18f70fe3ee598be5c4fa33397a3fc584797e5ce043ccb891415522ac70. Its closing scope explicitly preserves the independent F36 base-unit structure on the original corner module: the obstruction concerns inducing that property through unit pullback structures on this chosen larger smooth lift. It is not a contradiction to F36.

The full fresh review agent_F45_fresh_review.md passes the projective word-trace construction, including its added summand-preservation obstruction and the entire generated fragment763592f7e06e94366e8831a88174ae1a91d0ddd2ec2d7d8f983ff6dbbb9188f7. An actual rational permutation projector on a product of projective lines gives the scalar word-trace polynomial with integer twists, specified centering shifts, and invariant hard Lefschetz. Its degree-i cohomology has weight i; the complex is pure of weight zero and the total Weil space is mixed. The inserted commutant projector onto the N(D-2) sector has trace4(v^4+2+v^-4), which is not an SL2 character, so a simultaneous positive SL2-representation kernel model retaining that summand fails. Word-dependent motives remain valid.

The full fresh review agent_F46_fresh_review.md passes the Cayley report and the C15a commuting-action addition, current report hash06c90390243ec91ec86527ea2cd8cc1023e026f45b400ed94b43fea8cd41bf9e. The finite coefficient localization, cyclic Cayley operator, exact End/Hom comparison, and postcomposition commutant comparison work after every coefficient base change. The actual nilpotent centralizer survives collision. A finite flat divisor on the smooth proper relative projective line supplies the coherent coefficient geometry, and coherent Ext retains both crossed collision orientations with the separately recorded free688 term. At each specified arithmetic coefficient evaluation, all-conjugate pure Weil objects exist; continuous representations exist at good coefficient primes. The chosen linear operator is distinct from finite-field geometric Frobenius. Its extension-retuning failure and q=2 integrality obstruction are proved explicitly. The original Deligne Weil I Theorem1.6, printed p276, and its polynomial convention were reopened for this review.

The complete F47 report and generated fragment passed the fresh review agent_F47_fresh_review.md. The finite-based-ring obstruction uses the exact primary EGNO2009 statements. A real polynomial in the actual central element isolates the radical generator, which any positive self-adjoint realization kills. The regular center trace form has determinant Delta^2, attaining the proved minimum vanishing order four; the actual tensor module still has a regular positive form because it kills the radical at collision. These are precisely scoped faithful-action and based-ring obstructions, not a prohibition on all smooth categories or pure Weil data.

The exact source audit is agent_framework_locator_audit.md. EGA I Section9.5 is reserved for scheme-theoretic images, not affine module/sheaf equivalence. The latter is directly checked in Stacks Lemma26.7.5, tag01IB; perfect ring complexes are Definition15.76.1, tag0657. The root is separately checking the original EGA affine locators.

The original published SGA6 facsimile has now been visually inspected at Exposé I, Definition4.7 pp121–122 and Example4.8 p122, with Notation4.9 and the statement of Proposition4.10 p123. This removes the original-access qualification for those specific perfect-complex locators. Exposé V Sections2–3 remain a separate lambda/gamma background locator and are not the modern perfect-diagonal definition. Tabuada Section5.1 pp13–14 supplies that explicitly modern framework.

The earlier F33 introduction-only source description in Section13 has been superseded by the stronger exact primary Merkurjev Section5, Corollary5.3 p7 and Corollary5.5 p8. The full split-group motive formula was read there, and the generated F33 fragment records it as a known source application. The source does not supply the new nonstandard action.

Every review remains tied to its saved target hash and stated scope. A further final Part III snapshot will be needed after all new fragments and source corrections are integrated; the earlier scoped checks are not retroactive certification of later text.

## 20. Tensor comparisons and an intrinsic global-form obstruction

The final F46 corrected fragment4f78dd6e27145a6016e9f40718102d8e418cecd8ba24b51806ce26ea133ff2c4 has now received an entire-fragment match, including the corrected S0-membership sentence and the explicit sufficient, not necessary, total-reality condition. The current F45 source-only framework addition and the F47 corrected archive paragraph were also read with their exact scope recorded.

The root has completed the original EGA I source audit: Theorem1.3.7 p86, Corollary1.3.8 p87, and Theorem1.4.1 pp90--92. The corresponding original PDF hash and the fact that this is a parent-reported source inspection are recorded in agent_framework_locator_audit.md. The affine access qualification can be removed for those exact locators.

The complete F48 report passed the independent review agent_F48_fresh_review.md. An exact faithful tensor forgetful construction gives identity Frobenius on the actual fixed-parameter family; diagonal finite-order characters give nontrivial pure tensor Frobenius with precisely checked covariance for the named ordinary operators. Full recovery from the entire point-Weil centralizer is impossible already from the actual End dimensions in degrees one and two. A rational eigenvalue family obeying the all-extension parameter-retuning law at one fixed base is necessarily a monomial, and weight zero forces it to be one. The exact IV tensor-dual convention is preserved.

The new report agent_global_lattice_projector.md proves an intrinsic global-form obstruction. The actual ordinary W3-isotypic projector has coefficient1/(v²+1+v^-2) on the original tensor lattice. Its extension to the rank64 module is a sum of the F43 commutant's diagonal units and is induced by a literal F46 coherent direct-summand projector. No change of basis of the same original global lattice can make that complete specified matrix-unit system integral. The defining pairing of VIII's dual global form forces integral tensor entries, so it excludes this projector even after algebraic integral closure. Its actual bar compatibility and regularity at both explicit boundary lattices coexist with the global obstruction.

This is compatible with IV's explicit Example19.2 and its stated change of integral form. It does not obstruct a smaller named-generator action, a changed lattice, or VIII's canonical basis within its prescribed global form. The report and full finding_F49.tex have both passed root and gct whole-proof review; the current report hash is80e971b423940d694701d30ff48c12ec2ea50f1b96ac72ca3c9e1904d1994788, fragmentd96ea5437ab9959a42f807ec3d4aa2baa1c35bebf89c4ba4c4505bb697fa7f2c, and gct final review22d4e468b15a1a15b4ed5fe42e5f5af8cd3431f8206d410a4f060302c3a0367a.

## 21. Exact Gaussian sign geometry and final source-scope checks

The entire final F48 fragment has now been independently read, including the stronger unlabeled matrix-spectrum classification and the collision local-center proof. Its current hash is6ad18f075da322432b437f06778431c9ebe0f38f758f3813ee37db649ec2f1db. The additional proofs show that rational all-extension spectral retuning forces a monomial characteristic polynomial, that one pure weight conflicts with the actual generic full centralizer, and that a regular fixed-rank mixed family cannot retain the full collision centralizer. Exact matrix retuning forces constant conjugacy to a diagonal monomial family. These are precisely stated extra comparison assumptions, not exclusions of the already constructed faithful actions.

The Gaussian report and full generated F50 fragment passed complete independent review. A quadratic pencil, simple rank drops, Kummer monodromy and compact Leray prove actual middle-degree concentration at an unbounded set of even path lengths. Normalization by the Gaussian line produces a perverse object with compact cohomology exactly the chosen effective coefficient object, and exact negative effective path output in degree minus one. Its degree-zero Hom embedding retains F46's actual endomorphisms and module actions; its module-functor property also transports F43's graded kernels with their stated coherence scope.

The remaining bound is quantified rather than described vaguely. For this construction the original pointwise estimate is equivalent to the upper spectral radius of the chosen coefficient object. The reciprocal system adds exactly the lower radius. One fixed integer target must work under every embedding; zero spectral width separately at each embedding does not suffice. The mixed total word object has dual exponent gap4L, whereas each actual homogeneous coefficient piece gives its already known pure weight. Arbitrary inserted traces need not have effective multiplicities and are not covered merely by retaining the operators as morphisms.

Original SGA4half pp196--197 were visually read, including the concentration proof and perfect pairing. The erroneous final absolute-value shorthand was not used. Original1.18b--d pp178--179 and the exact Milne base-change, compact-support, Kunneth and projection contexts were also checked. A direct Newton-identities argument verifies algebraicity and conjugate spectra without a hidden weight theorem. The finite-etale quadratic object has signed-permutation Frobenius, making its rational characteristic polynomial explicit.

Final F50 report hash: cf6ca3f1ed8f48f8bc8a28b234855a488330cc849e40a9dcc974737ff5a5ebde. Fragment hash: b2107d7d72737a7dd0d6ed7494e4c72b9a70d39645e448b03d264aae751c483d. Full review hash:268bd4f47efc8d0a4142828d06c600d0c6711f978b7e8833a895c354cfa2245f.

The complete current PartIII/archive/final-gates snapshot through F49 was reviewed separately as agent_dictionary_snapshot4_review.md. Its scope hash isbd89051d8ff5b54c74a31e54e0ed0e8ab6dcd5a3cc363387ae539c8588476a9d. All dictionary and archive claims pass, with two minor synthesis wording suggestions and the explicit requirement to update the ending after F50 integration. That snapshot review is not retroactive certification of a later F50 insertion or revised concluding gates.

## 22. Algebraic spectral families and the actual collision order

The focused F50 synthesis delta is checked in agent_dictionary_snapshot5_review.md. It records the exact delta from the previously fully read dictionary, the new F50 paragraph, abstract and final task states. The current ending correctly separates the proved negative path spectrum from the equivalent upper and reciprocal pointwise bounds; one earlier residual path-sign clause was flagged for narrowing. No later finding is retrospectively certified by that snapshot.

The complete F51 base report, integral-weight supplement and final fragment passed the independent review agent_F51_fresh_review.md, hash54090576e6fcd1dc2d8485594fe16a9e02130a5842c9329afdef375ab03bbb79. Algebraic coefficient entries and arbitrary allowed sheets do not evade the trace-only obstruction for one fixed integral pure weight. The several-integral-weight extension proves an actual positive Laurent trace and excludes nontrivial eigenvalue phases. A separately imposed full spectral comparison identifies the whole characteristic polynomial and excludes the regular mixed-weight collision centralizer. Trace comparison alone is not claimed to determine the entire family spectrum.

The complete F52 report passed agent_F52_fresh_review.md. A restriction-of-scalars polynomial forces each base eigenvalue to have an integral power equal to an integral power of the parameter. On one finite Kummer-cover component, full spectral retuning therefore gives monomial eigenvalue functions. The actual whole relative center forces its two colliding scalar values to differ by a multiple of Delta, with valuation twice that of v-1. Distinct monomial characters that agree above v=1 have only first-order contact, including after further ramification. This excludes the stated whole regular relative-centralizer comparison without assuming purity or integral weights.

The explicit first-order model nevertheless has the same abstract special algebra and retains the actual rank64 action through an embedded suborder. Its generic embedding is an isomorphism but its collision map kills the actual radical. The added saturation argument shows that ordinary linear commutation equations on this unchanged free module cannot recover that nonsaturated embedded suborder. These precise qualifications prevent a false obstruction to all models, specified subalgebras or abstract special fibers. The complete report plus this addition is3e1052bb200865e1a913ef5b8690786956633d86e84338a8ebb4bb5079697552; the independent review is9937c3107a44d89c60e32e4d5a8040c421a3157b7177794bf7e9eb2fcbad78a7. A generated-fragment match remains separate at this entry.

## 23. Coherent convolution and the sharper trace frontier

The full F52 generated fragment and its dictionary-only cokernel clarification have now passed direct match at840a7b635c48c69b7d9dd16182eac64996b83fb073a9657e2e77c5f10b92909b. The updated review is8497465cd49eb8005ba752f7288b9e1a594beacbdb763dc74111bb22bfa9af59.

F53 supplies actual coherent geometric tensor operations on the Gaussian image. The complete report and fragmentd9645af47cee8e4dd9abf06a567b99de51c8a19b95bd6a8aa09051b3c4bab667 passed agent_F53_fresh_review.md, hashd11b8485ee5cf2ed4a71b24cea74df8a81a9f7d9866f88daa1353325a59db971. Normalized constant sheaves have a trace-normalized convolution with their own idempotent unit. The explicit Gaussian gauge gives the kernel AS(2xy), both units, and the essential correction to the naive odd-shift symmetry. The three dual notions are kept distinct. Composing with F48 preserves actual tensor maps through all degrees and the unchanged F50 path sign, but its identity-Frobenius K0 character is only dimension, so it does not identify source simples or the designated global basis. The pointwise and reciprocal bound remains exactly the coefficient-weight condition.

The new F54 Part1 report agent_algebraic_trace_classification.md proves a trace-only base-root classification with arbitrary spectral radii. Killing finite torsion, finite-power uniqueness places the trace relation in a Laurent group algebra. Euler derivations and positive actual weight multiplicities force support onto the parameter character's rational line. Thus every base eigenvalue has a common integral power equal to an integral power of the parameter. For one common radius, a same-element finite-zero identity and equality in the triangle inequality force one base eigenvalue; a semisimple full centralizer is then a single matrix algebra. This removes the earlier integral-weight restriction for that obstruction without claiming the family characteristic polynomial is known. The report has parent, theta and gct full reviews. All three also reported complete generated-fragment matches, including the final derivative-zero/effective-cone additions. Theta records this in REVIEW_F54_THETA.md, hashffb79073b5eb55ec2ebb324645ab4aa230c1e9132b5d56eaac06a44e2756d6ee; gct in REVIEW_GENUINE_TRACE_CLASSIFICATION_GCT.md, hash3103dca5e09c78ce02a28b1f9a133d528654a50ba26fd5d2d873e5af95de1ad1. Current reportd02e3d2584d2a3fff644e2b179390f78d8d5db2dada1d02a3ab88a5e02e59fbc, fragmente768c405f06e883d96cea21817da52588213d8de933643b144aba06bd40ba543.

F54 Parts2–3 were independently checked in full here, including both generated fragments and the exact SymPy certificate. Review agent_F54_parts23_fresh_review.md is a6aa61dabe01343d89355f8ccb877f07f021b4983dc6ef0d6966c80d80400783. A concrete multiple-radius model retains the entire actual relative order, rank64 named action, ordinary left action and both H/K identity-trace laws. This prevents an invalid upgrade from identity traces to full spectral retuning. A regular named central insertion instead detects the collision: its comparison is impossible under the stated full-centralizer, common-radius, or integral-weight hypotheses. Finally, preserving the two fixed inserted words P1 and P1 squared under retuning contradicts their actual parameter-dependent quadratic relation. That last theorem needs neither purity nor algebraicity. It excludes the specified fixed-operator composition law, while graded coefficient-object relations and separate word objects remain different alternatives.

All F54 parts preserve this distinction between a negative theorem about an explicit comparison and the remaining designated arithmetic/grading/simple-label question. The final main-text synthesis requires a later snapshot after these parts are integrated; earlier dictionary snapshots do not certify that later version.

## 24. Fractional trace models and compatibility at the collision

The complete F55 fractional report, final hash dfaaf497699824878f0db1399f0fb69da7bd1d5235910f87a36d52aeaafbf34e, passed an independent whole-proof review recorded in agent_F55_fractional_escape_review.md. The exact script was read and rerun successfully. A fixed finite cover and localization carry an actual right-action-compatible rank64 operator, regular at the negative collision place, retaining both ordinary identity and marked-X trace laws for every extension degree. Its base has distinct fractional spectral weights. The actual ordinary left action, fixed generator insertions and even unordered full spectral retuning fail explicitly. The eigenvalue-one multiplicity argument compares58 with at most40 and does not rely on tracking sector labels.

The report also proves that any genuine algebraic trace has a place above one with residue equal to its positive dimension. The scalar place extends to all coefficient data by finite normalization and lying over. This gives an obstruction under regularity at every collision place, for arbitrary mixed spectra. Stacks10.161.8/032L,10.36.17/00GQ,10.119.7/00PD were independently opened and their hypotheses checked; the standard trace-pairing derivation is correctly identified as known. The explicit model removes the other collision place and so does not satisfy the all-places premise. No new archive locator is required.

Root's complete same-branch report e178cd1cdb075878faf34862259e027ae8b86508e5e1d2e7043a0d6bec117d89 and entire generated Part3 fragment5f89efcab162ad785e8356dc9d41a9327d3be750a20c87eb2e1be3d62abcd108 also passed a fresh full review, recorded in agent_F55_continuous_branch_review.md. Positive Laurent conjugate branches cannot meet the positive branch without agreeing identically. Continuity, connectedness and two consecutive extension indices then force positive rational-power roots and the positive dimension at one. On the actual marked sector, regularity along that same branch instead forces zero, yielding the contradiction without any weight or full-centralizer hypothesis. Continuity is explicit additional comparison data, not a property supplied by a finite coefficient scheme. The fractional example's selected-sector trace and matrix entries have poles on the positive collision sheet even though its normalized marked and total scalar traces are regular there. These exact scopes are retained in both dictionaries.

The entire generated F55 Parts1–2 fragment9680e2bd817ab25d7b6dfe77aaa70f35e978c74955c765bf119a1a4891dffa22 has also received a complete direct text match. Standard normalization is cited through its exact checked primary statement; all new construction, field/place and trace proofs remain explicit.

## 25. A concrete coefficient category and its completion limits

The entire F56 report agent_coefficient_kernel_category.md was independently reconstructed and passed. Final report hash09ba4b88f65c22b9c367e311648bb79a4a2bad928d5119959efea00daf40e2bf includes the precise lambda/sigma scope requested in this review. The record is agent_F56_kernel_category_review.md. The supplied IV presentation context and actual right-row convention were reread, and the exact permutation/matrix certificate was read and rerun successfully.

The full additive positive word category has actual kernel maps for the two defining rank-three algebra relations and coherent ordered coefficient comparisons. Its split K0 is exactly the actual Laurent word-algebra image. This is a constructed category with specified relation maps, not a claim that an unspecified source higher presentation has been verified. The64-state Karoubi completion has split K0 rank104, while the faithful six-state completion has rank10 but replaces the actual double-contact order by its split normalization. The positive word category lacks the stated transpose-dual adjoints. These are exact properties of this category and its natural completions, not exclusions of every other categorification.

At fixed q, actual Weil coefficient lines retain the coefficient-object relations at every extension. Entrywise F53 transport supplies actual perverse operations with its corrected symmetry. Different grades retain their known different weights and the total need not be pure. The graded rank-three construction and the all-degree fixed-parameter F53 realization are kept distinct. The noncommutative split algebra is not called a lambda-ring: SGA6 lambda/sigma vocabulary applies to the symmetric coefficient category only. The report and generated dictionary delta have been checked here; theta is assigned the complete generated-fragment match. No later main-paper integration is certified by this entry.

## 26. Stronger all-places traces and two precise bar constructions

The complete strengthened F55 Part2 report and final replacement fragment8096d9e0f1a241445b32629b5a4d9f775bee3e3689bd365ed86020fafc37b68e passed agent_F55_inserted_trace_review.md. The new argument encodes any polynomial in an inserted trace as one finite tensor/direct-sum inserted trace, and invertible Cayley--Hamilton propagates eventual zero back to index zero. Finite normalization and common all-place residue produce a characteristic polynomial with prescribed special reduction. Consequently the actual marked comparison is excluded under all-places regularity without commutation, purity, effectivity or weight hypotheses. Finite virtual comparisons are excluded precisely when their zeroth inserted Euler trace is nonzero. The separate continuous-branch theorem still uses its genuine positive-multiplicity assumption. Primary Stacks0AUW(3) was additionally checked for finite freeness.

The full F55 bar-compatible variant reportf99c7ff251a6437ef69a9ce4b35b104f1bac03fea117e6d2c030c895123ef725 and entire fragmente1786cdbc0bb272407cbe94c5e81ef2019650602b96005213077730d71090fe1 passed agent_F55_bar_escape_review.md. A chosen cover involution t to inverse t, fixing sqrt2, preserves the actual formal bar as well as both traces and the actual right action. It does not exchange the two collision places and does not make the positive-place operator regular. This proves that the formal bar alone does not supply the stronger collision comparison. It is distinct from arithmetic duality and the prescribed VIII globalization.

A separate authored F56 formal-bar supplement has full report6dbc03af0b390d8b671e31b8b26ce45fa66937d5cc1497e111bed06c1f457c6c and fragmentdf2c113c5ea3c152e12795b8687e17aff7af22216c29ebb4c9778b39d118424c. Entrywise graded duality is a coherent contravariant monoidal involution that realizes the actual F43 bar on the split algebra and64 state classes. Symmetric product pairings make the named relation maps dualize to inverses; arbitrary shifted contexts are replaced by their dual contexts. The state transpose is absent, so this does not contradict the proved exclusion of transpose-dual adjoints. It does not provide a positive Hermitian polarization, designated global lattice or canonical basis. Root has reported a complete initial proof review, with its exact precision changes applied; gct is assigned a fresh whole-proof and fragment review. Author match is recorded separately.

The F56 formal-bar supplement now also has an independent entire-report and entire-fragment PASS by gct, recorded in REVIEW_FORMAL_BAR_GCT.md at8feb39e6a45c7ee294a66580f4aeb1877ddd1fe2d4e5ad78a23f9261dd08acf9. I read the complete review and confirmed its exact final targets and scope. The final fragment also passed isolated syntax/log compilation with the current paper preamble, three pages and no over/underfull box warnings; this does not claim a new visual-layout audit.


## Checkpoint 06: synthesis and F57 scope audit

Main8e7e9dea... new dictionaries, full abstract and PartIV scope PASS; two concise nonblocking synthesis refinements and task-state navigation updates sent root. This is a delta/scope audit, not a fresh whole-paper proof audit. Saved `agent_dictionary_snapshot7_review.md`, SHA256 `7a989e49ed1881b7f54bf3721f09cde22fc7bf5a7d66c3bbedd824b9fede1a5f`.

F57 primary-source scope, effective-cone and parity arguments PASS. Exact Laurent expansion and bounded two-parity Tate witness checked; current fragmentd96f71bf... relevant passages and dictionary matched. Full length-eleven matrix/source-figure audit belongs to theta. Saved `agent_F57_dictionary_scope_review.md`, SHA256 `278080b07086a35200e204fc3ad7048a324f5c1feb45afcad83f2e1fae0b53aa`. No shared master file or main TeX edited.


## Post-checkpoint 06: pure point traces and bounded Hecke complexes

The complete F57 pure-complex supplement and fragment were independently reconstructed, including the final proper-setting and signed-factor deltas. Final proof review `agent_F57_pure_point_review.md`, SHA256 `976d4908e487e568fd0cac20f045dcde9ead8d26135ce595838d63687e502fc5`.

New F59 core report `agent_soergel_derived_gate.md` SHA256 `09da1ff79542cb849f30d98cc4248a1813aaf03235f693d3d90047ab460f800f` proves the bounded direct-sum obstruction in every ordinary type-A rank and tests actual dot and coupled Rouquier lifts. Full fragment `finding_F59.tex` SHA256 `0bc2b46346e1dc1cdb8680ff0462bbf41e199bd344c87945742c9428a80153ae`, separate exact bibliography, and author record `AUTHOR_MATCH_F59.md` SHA256 `c9d6c7f95bcc60a436020357da128e87e249f96fb45083c7233bb07ea71ff36a` saved. Theta independently whole-read the report PASS; final fragment match requested. Main and shared master logs unchanged.


## F59 strengthening: arbitrary bounded ordinary type-A lifts

The complete new report `agent_soergel_frobenius_closure.md` SHA256 `7b354be09d00bedd715adbd2461ce56add9bcdf663551170435db744d233a647` closes the coupled bounded case in the ordinary type-A Soergel category, with the original ambient class and the cohomologically degree-zero delta-squared coefficient. Central finite coinvariant fibers force free H0 and no other cohomology; the two-root graph splitting then forces impossible integral multiplicities. Every type-A Frobenius fiber hypothesis is proved explicitly. Theorem scope excludes unbounded/changed-category/changed-coefficient routes.

The full fragment `finding_F59_frobenius.tex` SHA256 `8c5944021f382e24c6d4c4a62f65708b441c1b759bf82829f9748b26cc999303` was author-read and compiled cleanly. Author record `AUTHOR_MATCH_F59_FROBENIUS.md` SHA256 `9c180b58565173d4a0dc97384f8708558c78001d9acdd95f5d58d3204bfb00e9`. Theta has independently reported whole final-report PASS and is final-matching the generated fragment. The separate theta coupled-support note was independently read in full PASS, review `agent_F59_coupled_support_review.md` SHA256 `78c9bb45de0dd1ac6d8fe65559bd8d16f43b2600a68bbcd5fa9f0f780a909731`. No main or master-log edit.


## Checkpoint 07: strongest bounded-Hecke closure and pure rank-three kernels

The full F59 invariant-correspondence fragment `finding_F59_support.tex` at99bf5dcea3da338e2b9e4dc2c4de233c23a55834cce2b3a58030e25487b94dbb has now been read and matched to its previously reviewed report. The saved review is `agent_F59_coupled_support_review.md`, SHA25693a66a6b168565848cf1442e49434cb764fc7621788865708bf1211c3a95f8c2. Its concluding scope correctly recognizes that the following strongest theorem closes the ordinary bounded case.

Theta's complete independent strongest-F59 proof and entire-fragment PASS was read in `REVIEW_SOERGEL_FROBENIUS_THETA.md`, SHA256c427babecb70355be7b9cc19beac67955ea4cfc45be95ee9f93e8b8ac36418d1. The target report/fragment remain7b354be.../8c594402..., with both exact central-generator and homogeneous-Frobenius hypotheses retained. Root independently reports complete proof and fragment PASS too. The new altered scalar-coefficient-complex alternative remains a separate active task; this theorem does not silently exclude it.

The entire final F61 reportf48551682261cf37efe0160e23fffd103245d013a079a1b1778d8694efd5816a and all484 lines of fragment765a660843a8954a309b63291976b29fe96e80a99c0471ad44f0f5c1c63cc9f1 have passed a fresh independent proof and text-match review. Record: `agent_F61_pure_kernel_review.md`, SHA256298206f9567689a4bc9cfc784369773f15efa2653ffbc1d279d1b1ae063b8b54. This includes both strong monoidal grading functors, exact half-step parity domain/state potentials, actual quadratic and degree-five maps, corrected bar with shift twice the potential difference, coherent double dual and Gaussian derived transport. The difference between pure complex weight and a common total Frobenius radius is explicit. Source BBD5.1.8/11 and the F53 Gaussian conventions were reread; no new compilation or visual audit is claimed. Root has the integration-ready final review.


## Altered scalar coefficients and nonproper convolution

The full altered-scalar report `agent_soergel_scalar_complex_gate.md` atf0805ab3ae6735815c3acd08b4b42272e6d53a1308cdabb0d2016734278ceafb and complete fragment `finding_F59_scalar_complex.tex` atd2582ec9bd1d71877eb2bb0546abc380a71e257aa686e125164556ec6eb68fa7 now have author, root and independent theta full-proof/match PASS. Author record `AUTHOR_MATCH_F59_SCALAR_COMPLEX.md` is1d6224d2311bf73d9e642df37798c15af6946ea041377184669b07768549d262; theta final review74b54fdc5257c981a4bad130d355ae6ff59153aee30c9acc22cfe716f6304f6d. Generic positive cohomology is uniform on the two graphs, while a global left-flat cohomology lift contradicts integral coefficient parity. The generic argument deliberately forgets internal grading. Nonflat cohomology remains a necessary residual condition. The four-page isolated syntax check was clean.

F62's entire report and fragment have passed a fresh independent review, with the final requested proof that the outer convolution triangle itself is nonsplit. Final reportb70ed1e87088267222e206f1e1fec8147f288f816846462f5d495b902f87398a / fragment6fd83439f9c710c3a34d8bd052a429367ed0bf0b0b38facc0605eb247c151ec8. Review `agent_F62_nonproper_kernel_review.md`, SHA99d91af7ed3db4f5ee9a64841033e8b5a40bf709ea479910751d6d17541c5d44. The graph convention fixes the actual O(1,-1) torsor, its Chern-class extension is nonzero, and ordinary base hypercohomology distinguishes it from the constant fiber complex. Product torsors realize the exact IV c0 and one exact VIII printed scalar coefficient, with all twists and signs specified, without identifying designated canonical labels. The primary projective-bundle and source-coefficient contexts were reread.

A separate, not-yet-integrated amendment `agent_soergel_scalar_amendment.md` at09b861197691f5bc6492ce400e89f8d0a57ad114c9d4e50c05c45a27d092b57d proves two further tests and has been sent for fresh review: the invariant-correspondence factor fails arbitrary scalar coefficients by a top-degree origin-fiber contradiction; the pure full/half F61 scalar coefficient cannot satisfy the ordinary-Hecke quadratic because its two outer cohomological multiplicities are odd. The general genuinely nonfactorable mixed nonflat case is still unresolved.


## Post-checkpoint 08: complete scalar-complex closure

The singular-factor/pure-coefficient amendment and the invisible-direct-summand amendment now have full author, root and independent gct proof/fragment reviews. Final targets are report56022996.../fragment0edcea01... and reportf3db729b.../fragment41fa377d..., respectively. The combined author record is AUTHOR_MATCH_F59_AMENDMENTS.md, now d7d95c6e32ad4551dde985dd5ce7c42d227f887bbf16d53aec2bba628b6e2b2c. These preserve their narrower original scopes.

The F65 joint normalization report and final fragment passed a complete independent source/proof/text review, including the essential proper-structure-map-to-a-point qualification. The arbitrary-beta supplement also passed: agent_F65_arithmetic_parameter_review.md, SHAb5544bcb31f924f636d9e80e17564d304a12256b6e5bc53bfcffcd96a7dbd630, anchors report5f79181a... and fragment1a205331.... Simultaneous pure point traces for the two actual multiplication constants occur precisely when beta cubed is1, in which case the signed coefficient vanishes identically and its pure object is zero. All small root-collision cases and finite-etale sufficient witnesses are checked.

The earlier residual scalar-complex case is now closed in the ordinary rank-one product by the complete elementary proof agent_soergel_rankone_scalar_closure.md, SHA3272f93b6fe00db9d2f09c4e9bebc0d2e0dc18c6cc57e021680a24efa5dacb8f, and full fragment finding_F59_rankone_scalar.tex, SHAa873f1e948475f0cb752c27b29b16a361c2c4f1c187f50c29b54ad530a506f91. Theta's two-variable module lemma includes torsion-bearing modules. A canonical near-top Kunneth map, verified through right-module splitting only, gives an origin-fiber descending induction that forces all cohomology to be actual free graph modules. The restored full internal grading then contradicts the odd coefficients of delta squared. Root and theta have full-proof/final-text PASS; the five-page syntax check is clean.

A separately verified known theorem of Lichtenbaum extends the necessary tensor-dimension equality criterion to every polynomial dimension. The complete application checks completion, torsion-freeness, all finite-length Tor hypotheses and the last-minimal-differential socle. The original article's author-uploaded text, Hochster's primary-author field-case corroboration and exact Stacks completion statements were independently opened and read. The new all-rank report agent_soergel_allrank_scalar_closure.md, SHA475bd56d0486831328193453faec89612ea1c97a8bb81786d12970053eb34f27, and full fragment finding_F59_allrank_scalar.tex, SHA956b51070bd4cfc30b208512912bf0501d2da8d38a43ec94c65bbd56bd763b77, prove the complete bounded scalar-complex exclusion directly in each actual type-A ambient ring. No spectator specialization or bimodule formality is assumed. Root and theta have complete proof/source/text PASS; the additional independent gct whole-proof review is pending. Bibliography finding_F59_allrank_bib.tex is49f61afe0214ec14d4b7e666f943e04a6c64674373277aa6bf68a254ef416e17. The four-page proof-plus-bibliography compile has no errors or overfull boxes, with two underfull warnings confined to the first bibliography item.

These theorems keep the ambient ordinary Soergel Euler class, bounded scalar coefficient complex and actual quadratic fixed. They do not exclude non-scalar polynomial coefficient complexes, changed categories or K0 embeddings, localizations or unbounded models, and they assert no arithmetic purity or source canonical-basis equivalence. The previous residual-open descriptions in this working report record earlier snapshots; the bounded scalar case is closed by the new precisely scoped proof. No main paper or shared master log was edited.

The additional independent all-rank review is now complete: REVIEW_SOERGEL_ALLRANK_SCALAR_GCT.md, SHA62d35f6936cd76a5c2bb52e058117a4986968205ef53f0552f8242f6baa57852, was read in full and anchors the exact frozen report, fragment and bibliography. Gct independently reconstructed every proof step and reopened all new primary local-theorem and ordinary-graph contexts. The all-rank scalar closure has no remaining peer-review gate.

## Actual tensor inversion and the next operation boundaries

F68 is fully proved in agent_tensor_inversion_gate.md, SHAdf472500e57cdd877f2ca7cf3dee320b0b3537a2792a05964060d04bd8f22551, with complete fragment finding_F68.tex, SHA5751824d8b300ab870f859a6fa15b6e265d68522807707d4f6c63c348b0e9e32. Any finite sum of at least two invertible objects is noninvertible in a nonzero additive monoidal category. Independently, an additive strong monoidal image of a dualizable zero-dimension source object cannot become invertible, even without a target symmetry: its transported duality maps and source symmetry would make the zero trace an isomorphism of the unit. The actual source maps and two-sided inverse premise are explicit.

The torus coefficient has an actual derived Weil splitting, supplied by the rational point1 and smooth-curve duality, into E[-1] and E(-1)[-2]. This is not merely a cohomology or Euler-class statement. The projective line is also a sum of two invertibles, and its nonzero categorical dimension is correctly distinguished from the torus's zero dimension. The relative F62 coefficient retains its nonzero Chern extension; its locally perfect tensor-dualizable structure and actual zero source trace suffice without a global splitting. Formal trace-ring or Grothendieck-ring inversion and arbitrary extraction remain outside the theorem. Root and gct have complete proof/fragment PASS; gct's final reviewde264b1251e266fa4ebb10cd8b0604d1e1a0afe947ee50c22397df050cf9ef1e was read in full. Author recordaa0623685a82d4cc85046360b7d5de215a169a3fd7b58779f4a177bdcd713496 documents the exact targets and four-page isolated syntax check, with no visual claim.

F67's entire report3c9dfc4388135ebe628d1c909568828fd0c74f886e13ef0cba95083f97be2354 and final fragment8c2c2a116799ab94967ee610dabe92235966b3c925ec5fe2233812f08dbc8d4b have passed a fresh independent full review. Record: agent_F67_six_factor_review.md, SHA6bcb3f5353d8e5765ec6b215f04818c011773892393991b5aebf9a7288e35123. The actual published three-plus-three restriction sends individually effective two-state inputs to a full four-dimensional tensor whose two-word trace has coefficient minus12 at v to either tenth power. The calculation needs no projector in that output and no claim about the total much larger ambient tensor. Original Blasiak source contexts, the generic occurrence, the failure of the chosen lattice's ambient specialization, both purity conventions and the explicit mixed Tate witness were independently checked. The exact script was read and rerun successfully.

The central polynomial-coefficient extension of F59 also has complete fresh report/fragment/source PASS: agent_F59_central_coefficients_review.md, SHAaf343fd4fb98dc458762159edeab6997983343369ec7ea670833a0cc32ba5074. The final reportd276c3b9a8b85081eaab8e7cc7937e4cc4d3abc7c9a449a9137e4ae5301bef03, fragment69963bc08fc1d5c6385bcdc06f40a701ba1b8e2fc5d5a325d1e4d268551fdf3c and bibliography0714bea556c15ee85bc01dfc683c44fa3a69a8e34316468a9e1528ab7f8761c6 retain the precise nonflat/nonflat residual case for the designated generator class. Single-Koszul commutation is equivalent to invariance; invariant-descended coefficients have actual coherent central maps. Flat cohomology on either side is excluded, with the delicate nonflat-C implication proved by an actual one-sided Kunneth map and projective direct summands. An explicit central nonflat quadratic has the required coefficient Euler class but a different generator class, so it does not solve or contradict the designated problem. No shared master file was edited.

## Checkpoint09: actual quotient normalization

F67's smaller one-plus-three supplement also passed complete independent report/fragment/source-scope and exact-script review: agent_F67_one_three_review.md, SHA58a19c3e4953b4c5b7e7dd06e27fd27ef3bb7740138bcef2ebd223401437960c. The full four-state output at total factor count4 has coefficient minus4 at exponents6 and-6, while its two effective inputs remain actual source modules. This is compatible with the positive two-plus-two model because the inputs and output constituents differ. Generic occurrence, the collision-lattice caveat and the mixed Tate136/8 witness are retained; no minimality or whole-ambient trace claim was added.

The actual F69 quotient normalization is fully proved and frozen in agent_variable_group_quotient.md at6f8a8954b95880d5385cf7fa54c639d1c8e840530f3893bd13bba9e34f26dada and finding_F69.tex atcfb5f340cddcae7c1a9c94a333dbfdedbec2e5c4c95d9e4c71e62a8fc0276518, with bibliographybccb82673246f4b54d4406438c16fc8cbc5c189c567e8cb0b5b63b1675156591. The degree-two divisor algebra retains its nilpotent collision. Its units modulo scalars form an explicit group with multiplicative off-diagonal fibers and additive diagonal fibers. Evaluation of O(1), projective frame ratios and local missing-point sections identify the entire path scheme as an actual torsor; its quotient stack is precisely the endpoint scheme.

This construction retains the nonsplit off-diagonal Chern extension and does not tensor-invert ordinary torus compact cohomology. On four-point paths, the second named group family cannot descend equivariantly along the first action because its Ga and Gm fibers lie in one orbit. A separately defined new endpoint action yields an actual [A1/Gm] residual fiber off the diagonal, including a BGm fixed-point stratum. Its exact extension-degree masses have positive-definite rational Hankel matrices of unbounded rank and cannot be eventual finite uninserted Weil Euler traces. These are exact limits on the stated constructions, not a no-go for every weak or higher coherent quotient.

The author reread every report, fragment and bibliography line. Root has full report/final-text PASS. Independent gct review6bd7177985f65d5d17804b78b98f57795960d95d41ba3d11cf3908e34ba6debd and the contributor-scoped theta reviewad55184879ad0c8c52b459ccb58b7eb2941095b7b5070360c696bc5bdcff009f were read in full, including all final additions. Five exact Stacks primary contexts were independently opened. The five-page isolated syntax check has no errors or overfull boxes and one underfull bibliography warning. AUTHOR_MATCH_F69.md records the exact scope; no visual layout claim is made.

An optional integral-model sentence is held separately in F69_integral_model_pending.md at eeca1321a063a0ba141a9576c21ac30feffe0014fc734225122910ecd55be56e, following root's instruction to preserve the already fully reviewed checkpoint hashes. It is not part of the frozen finding. No main file or shared master log was edited.

## Checkpoint 09 targeted synthesis review

The full abstract, all Part IV through final task states and new F68/F69 dictionary context were read at main SHA256 0139e4d7db1d971c6a3e2f81d5c50573b2b86397db17e5229a58eb21b0f2e21c. No required scope correction was found. REVIEW_CHECKPOINT09_SYNTHESIS_GROTH.md records the precise read scope and the distinctions between bounded scalar versus polynomial coefficients, actual tensor inversion versus variable-group quotient, and named-family no-descent versus all higher operations. No main source, frozen F69 artifact or master log was edited.
