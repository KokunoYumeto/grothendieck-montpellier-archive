# Rectangular coefficients and theta-lift positivity: source audit and checked auxiliary arguments

Run: GCT_NSRH_2026-11-21. Author/checker: /root/rectangular_and_theta, GPT-6 Astra Pro (developer-provided model identity), reasoning effort inherited and not exposed. User-facing date: 2026-11-21 Europe/Berlin. UTC work date began 2026-11-20. This report is input to the root's independently checked paper, not a claim of a new solution of a GCT conjecture.

## 1. Main conclusions and exact remaining gate

Alpöge's supplied note gives positivity statements for the analytic functionals and periods involved in his argument. It does not identify the associated spaces or forms with the nonstandard canonical bases, Kronecker multiplicity spaces, or plethysm multiplicity spaces. The phrase “wins multiplicity m” in step 8 is introduced on p. 1 as an analogue of Stepanov's order of vanishing; it is not an assertion that a Kronecker coefficient grows by one at each lift. Even granting every claim in the note as requested, that distinction prevents the numerical multiplicity gain from being substituted into a representation-theoretic multiplicity formula.

The strongest directly available positive construction is already classical: every Kronecker or plethysm coefficient is the rank/trace of an orthogonal averaging projector. This gives positive semidefinite matrices and nonnegative Gram determinants. It supplies no prescribed canonical basis and no efficient combinatorial indexing set. A new theta route must therefore identify its positive periods, lift images, and compatible basis with those exact projector images, and prove a graded, multiplication-compatible statement if canonical-basis structure constants are the target. A mere equality of dimensions would address fewer claims.

The concrete reduction for a chain of interlacing tests is Proposition T-PATH below: a compatible chain of exact functors between semisimple categories with 0/1 branching matrices counts paths. It is a fully proved conditional statement. The missing input is precisely that the relevant theta chain realizes the target restriction functor, with finite-dimensional algebraic objects, compatible composition, and the specified endpoints. Neither the note nor Fable's proposal gives this input. This does not refute the possibility that such a realization could be discovered.

## 2. Exact source statements: Ikenmeyer–Panova

Authoritative supplied file: `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/main.tex`. Its numbering agrees with arXiv:1512.03798v2, https://arxiv.org/pdf/1512.03798, opened and checked here. Beware that an unexpanded text reference “Cor. 1.6” within the supplied proof is stale: the actual degree bound is Corollary 1.9. Use labels and matched displayed statement numbers.

Notation: `n × d=(d^n)`, a rectangle with n rows and d columns. For λ⊢nd, write

- `g_n(λ)=g(λ,(d^n),(d^n))`;
- `a_λ(d[n])=mult_{S_λ V}(Sym^d(Sym^n V))`, dim V≥ℓ(λ);
- `q^m_λ(d[n])=mult_{S_λ V} C[overline(GL_{n²} · X_{11}^{n−m} per_m)]_d`.

The dual convention is fixed as in the supplied paper: coordinate functions on Sym^n(V*) form Sym•(Sym^n V). Under that convention no dual needs to be inserted in these displayed multiplicity definitions.

| Locator | Statement used |
|---|---|
| §1(a), equation (1.3), source label `eq:omegaa` | `0≤q^m_λ(d[n])≤a_λ(d[n])`, from restriction of polynomial functions to the closed orbit closure. |
| Theorem 1.4, label `thm:strategy` | `q^m_λ(d[n])>g_n(λ)` implies `dc(per_m)>n`. |
| Equation (1.5), label `eq:positivity` | Weaker occurrence criterion `q^m_λ(d[n])>0=g_n(λ)` implies the same lower bound. |
| Theorem 1.6, label `thm:together` | If `n>3m^4`, λ⊢nd, and `g_n(λ)=0`, then `q^m_λ(d[n])=0`. Equivalent contrapositive: permanent occurrence forces rectangular Kronecker positivity in this range. |
| Theorem 1.8, label `thm:kadishlandsberg` | `q^m_λ(d[n])>0` implies `ℓ(λ)≤m²` and `|bar λ|≤md`, where `bar λ` removes the first row. |
| Corollary 1.9, label `cor:degreelowerbound` | If `|bar λ|≤md` and `a_λ(d[n])>g_n(λ)`, then `d>n/m`. |
| Theorem 1.10, label `thm:secondmain` | Put `X={(1),(1,1),(1^4),(1^6),(2,1),(3,1)}`. If `bar λ∈X`, then `a_λ(d[n])=0`. If `bar λ∉X` and there exists m≥3 with `ℓ(λ)≤m²`, `|bar λ|≤md`, `d>3m³`, and `n>3m⁴`, then `g_n(λ)>0`. |
| Proposition 2.8, label `pro:main` | For λ=ρ(nd)=(nd−|ρ|,ρ), if `(n,d)∈St¹(ρ)` (in particular if n≥|ρ|), then `g_n(λ)≥a_λ(d[n])`. Definition of `St¹(ρ)` is §2(a), after Theorem 2.1. |
| Theorem 4.7, label `thm:mainpositivityresult` | If ν∉X, `L=max(ℓ(ν)+1,9)`, `a>3L^(3/2)`, `b≥3L²`, `|ν|≤ab/6`, then `g(ν(ab),a×b,a×b)>0`. |

Theorem 1.6 is a no-go statement for zero-versus-nonzero obstructions. It is not a positive rule for evaluating all coefficients, not a canonical-basis theorem, and not a no-go theorem for all multiplicity inequalities. Theorem 1.10 is a substantial actual positivity theorem in the large rectangular region; it is already proved in the cited literature and is not a consequence newly obtained from Alpöge's method.

The source itself notes after Theorem 1.6 that symmetric rectangular coefficients, which give determinant-orbit multiplicities, require a different argument because the transposition symmetry used for ordinary Kronecker coefficients is unavailable. BIP implies their no-occurrence conclusion indirectly. Do not conflate the symmetric coefficient, the ordinary coefficient, and the determinant-orbit-closure coefficient.

## 3. Exact source statements: Bürgisser–Ikenmeyer–Panova

Authoritative supplied file: `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/main.tex`. It agrees with arXiv:1604.06431v3, https://arxiv.org/pdf/1604.06431 (17 September 2018). The older TU Berlin PDF from March 2017 numbers the main result Theorem 1.5; **the supplied version's main theorem is Theorem 1.4**. This version discrepancy has been checked rather than silently mixed.

Let `Ω_n=overline(GL_{n²}·det_n)` and `Z_{n,m}=overline(GL_{n²}·X_{11}^{n−m} per_m)`. Let `K_n(λ)=mult_{S_λ V} C[Ω_n]_d` for λ⊢nd.

- **Theorem 1.4**, source label `th:main`, source lines 380–386, PDF p. 3: for positive n,d,m with n≥m²⁵ and λ⊢nd, occurrence of λ in C[Z_{n,m}] implies occurrence in C[Ω_n]. This refutes their Conjecture 1.3 on occurrence obstructions.
- **§1(b)**, after Theorem 1.4, source lines 415–428, PDF p. 3: `K_n(λ)≤sk_n(λ)≤g_n(λ)`, with `sk_n` the symmetric rectangular coefficient giving the determinant-*orbit* multiplicity. The source states the first-to-last bound and explains the orbit equality and intermediate upper bound.
- **§1(c), Future directions**, source lines 486–502, PDF p. 4: if Z⊆Ω, restriction gives a surjection C[Ω]→C[Z]. Thus `q^m_λ(d[n])≤K_n(λ)`. A strict inequality `q^m_λ(d[n])>K_n(λ)` still proves noncontainment. The theorem rules out support separation, not this multiplicity comparison.
- **Proposition 3.3**, label `pro:orbit-HWV`, PDF p. 10: the λ-highest-weight space in V^⊗D is the Specht module [λ], by Schur–Weyl duality, and is spanned by the symmetric-group orbit of one highest-weight vector.
- **§4, equation (4.1)**, label `eq:PROJ`, PDF pp. 10–11: the symmetrizer `Σ_{d,n}=(d!(n!)^d)^−1 ∑_{σ∈H_{d,n}}σ`, where `H_{d,n}=(S_n)^d⋊S_d` preserves d blocks of size n, projects V^⊗dn onto Sym^d(Sym^n V). The paper writes the wreath symbol as S_d wr S_n; specifying the semidirect product avoids a convention conflict.
- **Proposition 4.5**, label `pro:HWVSS-gen`, PDF p. 12: projected tableaux span the highest-weight space, with specified easy vanishing/equivalence relations. It does not claim that this spanning set is a basis.
- **Theorem 4.7**, label `eq:comb_contraction`, PDF p. 12: evaluation of a projected tableau on a tensor is a normalized sum of products of column signs. These summands can have either sign. BIP proves positivity for special constructions by controlling those signs; generic Gram positivity does not remove the dependencies/cancellation in this spanning system.

The last four locators directly support the positive-projector reduction below and demonstrate that the missing issue cannot be dismissed as finding some positive quadratic form: a projector and spanning generators are already known exactly.

## 4. What Alpöge's attached note actually supplies here

The four-page PDF has a public introduction on pp. 1–2 and a compressed timeline on pp. 3–4. The prompt's numbering refers to timeline items, not theorem numbers. Relevant exact locators:

| Locator | Relevant content | Transfer not supplied |
|---|---|---|
| p. 1, paragraph on Stepanov and chaining theta lifts | Theta lifts mimic arithmetic multiplicity; the proposed chain length for a length-X von Mangoldt sum is approximately √X. | No representation-multiplicity identification. |
| p. 3, introductory paragraph before timeline | Multiplicity 2 on O(2,n), an automorphic determinant, and further theta lifts form the analogy with qN=M^k+R. | No Schur functor or canonical-basis map. |
| p. 3, step 4 | Positivity W(1_S)≥0 obtained via a determinant and interpreted as Stepanov multiplicity one. | W, the indexing S, and the determinant are not identified with GCT structure constants. |
| p. 4, step 7 | Determinants containing GGP periods and 0/1 interlacing information, or up to m noninterlacing weights. | A brief statement about periods is not a full branching theorem with specified endpoints, nor a rule for plethysm. |
| p. 4, step 8 | Iterated lifts between totally definite unitary groups `U(X_0)→⋯→U(X_m)`, representation modification `π↦π⊞μ_j[t]`, and multiplicity m. | No exact tensor functor to nonstandard quantum groups; no additive path decomposition; no independent family of m vectors in a target multiplicity space. |

`ALPOGE_Main.lean` imports `Statements` and `Supplements.Kernels.MainTheoremsAll`; its five exported theorem wrappers concern RH and Dirichlet L-functions. `ALPOGE_Statements.lean` defines the four Dirichlet/zeta line/nonvanishing propositions used by those wrappers. None of these supplied wrapper statements is a canonical-basis, interlacing, theta-functor, or nonstandard-RH theorem. This is a locator limitation, not a challenge to the stipulated RH/GRH theorem. No kernel build of the missing imported files was performed.

Fable's suggestion 8 explicitly marks the plethysm link as proposed and asks which coefficients occur. It cannot be upgraded to a theorem. Suggestions 3 and 4 similarly propose identifications with archive cotes 1, 16, and 44, but those archive scans and intake runs are not attached. Consequently none of the cited cote/scan claims has been independently verified in this subtask. Cote 133 is named as a lead for plethysm/λ-operations; it is not evidence of the missing theta/GCT functor.

## 5. Auxiliary proposition T-PROJ: exact positive-projector form

**Statement.** Let H be a finite group and U a finite-dimensional unitary complex H-representation. Set `P_H=|H|^−1∑_{h∈H}ρ(h)`. Then P_H is the orthogonal projector onto U^H; in particular

`P_H=P_H*=P_H²`, `〈v,P_Hv〉=‖P_Hv‖²≥0`, and `tr P_H=rank P_H=dim U^H`.

If m=dim U^H, then `det(I+tP_H)=(1+t)^m`; every principal minor of the matrix of P_H in an orthonormal basis is nonnegative. For partitions λ,μ,ν⊢D,

`g(λ,μ,ν)=tr P_{S_D}` on `[λ]⊗[μ]⊗[ν]`.

For λ⊢dn and dim V≥ℓ(λ),

`a_λ(d[n])=tr P_{H_{d,n}}` on `[λ]`, where `H_{d,n}=(S_n)^d⋊S_d⊂S_{dn}`.

These are reformulations of classical numerical nonnegativity, **not newly proved numerical-positivity theorems**. BIP §4, equation (4.1) and Proposition 3.3 contain the ingredients of the plethysm statement.

**Proof.** Since ρ(h)*=ρ(h^−1), inversion of H gives P_H*=P_H. In the double sum defining P_H², every group element occurs exactly |H| times, hence P_H²=P_H. For any k∈H, ρ(k)P_H=P_H, so its image is invariant; P_H acts as the identity on every invariant vector, proving that image equals U^H. A self-adjoint idempotent has an orthogonal decomposition U=im P_H⊕ker P_H and is the identity on the first summand and zero on the second. The quadratic-form, trace, rank, and determinant assertions follow. A principal submatrix is the Gram matrix of vectors P_He_i because 〈P_He_i,P_He_j〉=〈e_i,P_He_j〉, so its determinant is a squared exterior-product norm, hence nonnegative.

Specht modules admit invariant positive Hermitian forms by averaging any positive form. They are self-dual in characteristic zero. The Kronecker invariant-space description in IP §1(a) or BIP §1(b) identifies its multiplicity with the invariant dimension of the displayed triple tensor. For plethysm, averaging within each of d blocks gives `(Sym^n V)^⊗d`; averaging permutations of the d blocks gives Sym^d(Sym^n V). Taking H-invariants in the Schur–Weyl direct sum `V^⊗dn=⊕_λ S_λ V⊗[λ]` therefore gives `Sym^d(Sym^n V)=⊕_λ S_λ V⊗[λ]^H`. Reading its λ-multiplicity proves the last identity. □

**Exact limit.** The theorem gives no description of the image in a prescribed combinatorial basis. For a redundant spanning family v_i of that image, the Gram matrix G=(〈v_i,v_j〉) is positive semidefinite and `rank G=m`. More precisely, `∑_{|I|=k}det G_I=∑_{|I|=k}‖∧_{i∈I}v_i‖²`; it is positive iff rank G≥k. Thus determinant positivity can restate the rank question exactly, while the need to decide which minors are nonzero remains. There is no claim here that such a rank problem is intrinsically inefficient; the point is that positivity of the form alone proves no efficiency bound and no basis selection theorem.

**Grothendieck dictionary.** For the constant group scheme H over `Z[1/|H|]`, the same average is an idempotent in the group algebra. On every finite locally free representation its image is a direct summand and represents an effective class in K_0. After base change to C the rank is the dimension above. Pullback along subgroup-scheme maps induces the restriction operation on representation K_0. Exterior powers and Schur functors are the λ-operations and their polynomial consequences. The actual-effectivity statement is weaker than coefficientwise positivity in an arbitrarily prescribed integral basis, as T-BASIS proves. Precise SGA locator verification is left to the root's Grothendieck audit; no unverified archive cote is used here.

## 6. Auxiliary proposition T-PATH: what an interlacing chain would prove

**Statement.** Let C_r,…,C_0 be split semisimple linear categories, all objects considered having finite length, with exact additive functors F_i:C_i→C_{i−1}. Let S_i(a) be chosen simple objects and suppose

`F_i S_i(a) ≅ ⊕_b S_{i−1}(b)^{⊕b_i(a,b)}`

with finite sums and b_i(a,b)∈{0,1}. Then the multiplicity of S_0(c) in `F_1⋯F_r S_r(a)` equals

`∑_{a_{r−1},…,a_1} b_r(a,a_{r−1})⋯b_1(a_1,c)`.

It is the number of allowed endpoint-fixed paths. If each allowed step is given by integral interlacing inequalities and all intermediate coordinates are bounded by the fixed endpoints, that count equals the number of integer points in the polytope cut out by those inequalities.

**Proof.** Apply F_{r−1} to the finite direct sum for F_rS_r(a). Additivity replaces each summand by its finite direct-sum decomposition and multiplies the multiplicities. Repeat to F_1. Semisimplicity and Schur's lemma identify the coefficient of S_0(c) with its multiplicity; collecting coefficients gives the displayed sum. Each summand is 1 precisely for an allowed chain and otherwise 0. The last statement is the bijection from a chain to its array of intermediate integral weights; the inequalities describe exactly those arrays, and the boundedness hypothesis makes the polyhedron a polytope. □

**Classical example and exact source.** Ordinary `GL_r→GL_{r−1}` restriction has b_i=1 exactly when `λ_j≥μ_j≥λ_{j+1}`. See A. I. Molev, *Gelfand–Tsetlin bases for classical Lie algebras*, Theorem 2.1 and equation (2.2), printed p. 7, followed by equations (2.4) and Theorem 2.3, printed pp. 8–9. Primary author-hosted PDF: https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2002/molev-18.pdf (PDF pages 9–11 because of front matter). The theorem and following pattern definition were read here. This supplies familiar positive interlacing counts, but the subgroup maps are standard block inclusions.

**Why that example is not the requested theorem.** Kronecker multiplicities are restriction along `(g,h)↦g⊗h` from GL(V⊗W), while plethysm is restriction along `g↦S_μ(g)` from GL(S_μV). These are not the consecutive block inclusions in T-PATH's classical example. A theta lift between dual pairs is likewise not merely restriction along such an inclusion. To use T-PATH, one must prove that a proposed chain has the exact functor and endpoint identification; single-stage branching tests do not provide that theorem.

For a concrete normalization check, `S_(d^r)(C^r)=det^d` has a unique ordinary interlacing pattern under the standard chain. The rectangular Specht module [(d^r)] is a different object. For r=d=2, `[(2,2)]⊗[(2,2)]=[(4)]⊕[(2,2)]⊕[(1,1,1,1)]`; the GL_2 determinant character is one-dimensional. Thus “use the same rectangular highest weight in a compact branching chain” already changes the object. For completeness, the S_4 equality follows from the character values of [(2,2)], which on cycle types (1^4),(2,1,1),(2,2),(3,1),(4) are (2,0,2,−1,0): their squares are (4,0,4,1,0), the sum of the trivial character (1,1,1,1,1), the sign character (1,−1,1,1,−1), and that same two-dimensional character. The two-dimensional character itself is obtained by subtracting the trivial summand from the permutation action on the three pairings of four letters. Equality of characters proves the decomposition. This example is explanatory; it does not rule out an elaborate correctly identified theta construction.

**Grothendieck dictionary.** Over Q, categories Rep(GL_i) are semisimple and restriction is pullback of representations along block subgroup schemes. In K_0, T-PATH says that composing positive homomorphisms multiplies their nonnegative matrices in the basis of simple classes. The proof is purely the functoriality and additivity of K_0, with a stronger object-level decomposition supplied by semisimplicity. Over Z or finite fields, such a decomposition into simple summands cannot be silently retained; a compatible filtration or restriction to characteristic zero must be stated. T-PATH does not establish such an integral filtration for theta lifts.

## 7. Counterexample T-BASIS: pure, positive geometry does not fix basis signs

**Statement.** Positive-definite Gram forms, positive Gram determinants, pure weight-zero realization, and effectivity of all chosen basis elements do not imply nonnegative multiplication constants in that basis.

**Construction/proof.** Let X be the disjoint union of two rational points over F_q. Then `K_0(X)=Z⊕Z`, with componentwise tensor product, and `H^0_et(X_bar,Q_l)=Q_l⊕Q_l`, with componentwise cup product. Frobenius is the identity on H^0, so this realization is pure of weight zero. Define two classes/vectors

`b_1=(1,1)`, `b_2=(1,2)`.

They form an integral basis because the determinant of their coordinate columns is 1. Both are effective: b_1 is the structure sheaf and b_2 is a vector bundle of ranks 1 and 2 on the respective components. After choosing a complex realization, the natural pairing is `〈x,y〉=x_1 y_1+x_2 y_2` on real coordinates. Its Gram matrix in this basis is

`[[2,3],[3,5]]`, with positive principal minors 2,5,1.

Nevertheless `b_2²=(1,4)=3b_2−2b_1`. The coefficient −2 refutes the asserted implication. This is already a finite étale smooth projective example, so adding smoothness, properness, or purity does not repair the inference. What repairs it in familiar geometric positivity arguments is identification of the chosen basis with effective simple objects and compatibility of the relevant operation, not positivity of an arbitrary form. □

**Scope.** The example is not a counterexample to any specific canonical-basis conjecture of GCT VIII. It refutes only the proposed general bridge from determinant positivity/purity to coefficients in an unspecified or independently prescribed basis.

**λ-ring form.** K_0(X) has componentwise exterior-power operations: for a bundle of ranks (r,s), `λ_t(r,s)=((1+t)^r,(1+t)^s)`. Hence the example lies within ordinary special λ-rings arising from schemes and uses actual locally free sheaves. Passing to λ-operations or to a graded construction does not logically restore the disproved implication. No nontrivial γ-filtration computation is being claimed.

## 8. Supplementary exact computation (optional explanatory example)

`agent_theta_kronecker.py` implements Murnaghan–Nakayama by enumerating all rim-hook removals, exactly over rationals. It verifies the complete character orthogonality matrices for S_4 and S_9, then computes

`g((5,2,2),(3,3,3),(3,3,3))=2`.

`agent_theta_kronecker_certificate.tsv` lists all 30 cycle types ρ⊢9, their centralizers z_ρ, the two character values, and the exact summands `χ_522(ρ)χ_333(ρ)^2/z_ρ`, summing to 2. This is recorded as an exact computation plus a consistency check, not an independent formal certificate, not an independent proof of the character algorithm, and not a new theorem of rectangular positivity. The report's main argument does not require this example.

## 9. Fable leads: what can and cannot be carried forward

1. Suggestion 8's interlacing path-count statement is rigorously available in the conditional T-PATH form. It does not identify theta lifts with that path-count functor. The statement “branching along a chain of compact dual pairs counts GT patterns” is too broad without a precise pair and functor.
2. Suggestions 3/4 invoke the missing archive cotes. They remain leads. In particular, an analytic determinant with nonnegative scalar value does not identify its entries or coefficients with GCT basis structure constants.
3. For the path-quadric toy, the Fourier operator is not automatically self-adjoint or positive even when t≥0. For t≡1 on F_3, the normalized Fourier matrix F satisfies F²=reflection and F⁴=I; its trace is i, so it cannot be a positive self-adjoint operator. This refutes the bare identification of that operator with a positive operator without an additional conjugation, symmetrization, or different construction. The path sum is an endpoint matrix coefficient, whereas a trace of a power closes the path into a cycle. The toy norm estimate alone does not prove the claimed operator identity with an archive determinant. The root owns the full sign-only analysis; this observation is passed on to avoid treating Fable's identification as proved.

## 10. Check events performed in this subtask

Use these only with their stated scope. Cited theorem proofs were not re-proved in full unless stated.

| ID | Type | Event/outcome |
|---|---|---|
| SRC-IP | used and rechecked in this run | Read full relevant source statements and their immediate proofs/context; matched numbers against arXiv v2. Parameters and exceptional tails confirmed. Full long positivity proof not re-proved. |
| SRC-BIP | used and rechecked in this run | Read Theorem 1.4, §§1(b,c), Prop 3.3, eq (4.1), Prop 4.5, Thm 4.7; matched to arXiv v3 and disambiguated old numbering. Main long theorem carried as cited result. |
| SRC-ALP-THETA | used and rechecked in this run | Read entire four-page extracted note and the supplied Lean wrappers. Located steps4,7,8; no theta/GCT transfer statement found in those supplied materials. No kernel verification claimed. |
| SRC-FABLE8 | used and rechecked in this run | Read suggestions3,4,8 in original/expanded files; kept proposed status and missing-cote boundary. |
| SRC-GT | carried as background without fault found | Read Molev Theorem2.1, equations2.2/2.4, following pattern interpretation; no independent proof of classical branching. |
| T-PROJ | targeted proof check | Checked finite averaging idempotence, self-adjointness, image, trace, minors and Schur–Weyl/wreath restriction step end-to-end. Valid in characteristic zero; integral statement restricts to |H| invertible. |
| T-PATH | targeted proof check | Read full direct-sum induction proof; verified finite support, semisimplicity, exact/additive functors and polytope boundedness hypotheses. Valid conditional theorem; theta realization remains open. |
| T-BASIS | targeted proof check | Read full scheme/K0/purity/Gram proof; checked determinant1 and expansion (1,4)=3(1,2)−2(1,1). Valid counterexample only to general bridge, not to GCT's specific basis. |
| COMP-RECT9 | computation or formal certificate | Exact rational MN computation, all S4/S9 character inner products checked. Output2; finite computation only, no formal proof assistant certificate. |
| FABLE-FOURIER | targeted proof check | For F3 normalized Fourier, trace=(1+2 exp(2πi/3))/√3=i; nonreal trace rules out self-adjointness/positivity. General toy→positive operator bridge refuted in this naive form. |

The full proof texts in §§5–7 were reread after writing; the root should record its own independent reading separately. No independent second agent proof check has yet occurred in this subtask.
