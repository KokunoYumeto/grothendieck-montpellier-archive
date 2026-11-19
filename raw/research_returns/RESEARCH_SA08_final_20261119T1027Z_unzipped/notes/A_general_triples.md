# A.1: arbitrary triples and completion via derived coefficient tails

2026-11-19. GPT-6 Astra, root. Independently checked in message by shadows_coalgebras; detailed proof below.

## Notation and explicit coefficient complexes

Let B=Γ_Z(T), I_r=⊕_{n≥r} Z T^[n] for r≥0, I_0=B. A PD triple (S,J,t) gives the ring map f:B→S, T^[n]↦γ_n(t). The underlying de Rham algebra only depends on this map; the rest of J determines the indicated augmentation and PD ideal but does not alter its underlying cochain algebra.

Define E_r(S)=S⊗^L_B I_r in D(S), with homological degrees≥0 (equivalently cohomological degrees≤0). For all X set

𝔥^i(X;E)=Hom_{D(S)}(C_*(X;S),E[i]),

where C_* is the normalized simplicial chain complex, regarded cohomologically in nonpositive degrees, and [i] is the usual cohomological shift. A module E in degree0 gives ordinary H^i(X;E).

Every E_r has an explicit two-sided normalized bar model, in homological degree h:

Bar_h(S,B,I_r)=S⊗_Z (B^+)^{⊗h}⊗_Z I_r.

In the basis s[a1|...|ah;b], aj≥1 and b≥r, its differential is

s f(T^[a1])[a2|...|ah;b]
+ Σ_{j=1}^{h−1}(−1)^j binom(aj+aj+1,aj)s[a1|...|aj+aj+1|...|ah;b]
+ (−1)^h binom(ah+b,ah)s[a1|...|ah−1;ah+b].

This is a complex of free S-modules. It computes the stated derived tensor even when S has torsion over Z: before tensoring with S the bar resolution is B-free because B^+, I_r are Z-free. The ordinary bar contraction proves exactness. Cohomology 𝔥 is computed by the product-total Hom complex from C_*(X;S) to this bar complex; no finiteness assumption on X is imposed. Its coefficient pairing is the signed bar shuffle followed by multiplication I_r I_s⊂I_{r+s}.

## Theorem A-006: all triples, all simplicial sets

For i>0 there is a natural isomorphism

H_DR^i(X;S,J,t) ≅ im(𝔥^i(X;E_i(S)) → 𝔥^i(X;E_{i−1}(S))).

In degree0 the answer is H^0(X;S). The arrow comes from I_i↪I_{i−1}. Thus this is a formula in ordinary normalized chains and explicit constant coefficient complexes, not an instruction to recompute differential forms on X.

Multiplication is as follows. Lift two image classes of degrees i,j to 𝔥^i(X;E_i) and 𝔥^j(X;E_j); apply derived cup product and the coefficient multiplication E_i⊗^L_S E_j→E_{i+j}; then take its image in 𝔥^{i+j}(X;E_{i+j−1}). The result is independent of the chosen lifts. Multiplication by s∈S is ordinary coefficient multiplication. Degree0 acts by cup product. These rules specify the entire graded S-algebra.

### Full proof

Write A_B for the universal simplicial de Rham algebra and Z_B^i=ker(d:A_B^i→A_B^{i+1}). The objectwise PD Poincaré contraction (ordered variables after elimination of X_0) is B-linear, preserves total weight and splits every exact differential sequence. Consequently every A_{B,n}^q and Z_{B,n}^q is a projective B-module. The Moore normalization functor is a direct summand in each simplicial degree and is exact. Thus its normalized terms remain projective, and tensoring with S commutes with cycles and normalization:

N Z_S^i = (N Z_B^i)⊗_B S, and N A_S^q=(N A_B^q)⊗_B S.

Forms of exterior degree i vanish on simplices of dimension<i. Therefore N Z_B^i starts in homological degree i. In weight w≥i, the resolution 0→Z T^[w]→A_w^0→...→A_w^{i−1}→Z_w^i→0, whose first i terms are simplicially contractible, gives π_n(Z_w^i)=Z if n=i and zero otherwise. Multiplication by T^[a] on this homology is binom(w+a,a). Hence

N Z_B^i ≃ I_i[i]

canonically in D(B), with [i] placing the sole homology in homological degree i. Similarly

N A_B^q ≃ Z[q],

where B acts on Z by its augmentation. For the latter statement use A_B^q=⊕_{w≥q}A_w^q: only w=q contributes simplicial homotopy, and that term is Λ^qΨ, whose normalization is Z[q]. All these projective complexes are bounded below homologically and hence K-projective. Consequently their tensor products with S compute derived tensors. In particular

N Z_S^i ≃ E_i(S)[i].

The short exact sequence of simplicial S-modules

0→Z_S^{i−1}→A_S^{i−1}→Z_S^i→0

gives a distinguished triangle. Before coefficient change it identifies with the triangle obtained from

0→I_i→I_{i−1}→Z·T^[i−1]→0

after shift by i−1. This can be checked weightwise: for w≥i the connecting map identifies the same coefficient generator; at w=i−1 the projection is the identity; all other weights vanish. After tensoring with S its final arrow is E_i[i]→E_{i−1}[i].

We now justify passing from actual cochain classes to homotopy classes, a point where no acyclicity assumption on A_S^{i−1} is needed. The map A_S^{i−1}→Z_S^i is degreewise surjective, so is a Kan fibration of underlying simplicial sets. If a map X→Z_S^i is simplicially nullhomotopic, lift a homotopy starting at its zero lift through this fibration. The terminal map supplies an actual preimage in Hom(X,A_S^{i−1}). Thus all nullhomotopic cocycles are boundaries. Conversely any cochain boundary lies in the image of the map on homotopy classes. It follows that

H_DR^i(X;S)=coker([X,A_S^{i−1}]→[X,Z_S^i]).

For a simplicial S-module V, [X,V]=Hom_{D(S)}(C_*(X;S),NV): linearize the simplicial map by the free S-module functor and use Dold–Kan. Its normalized source is a bounded-below complex of free modules, so simplicial homotopy gives the derived Hom group. Applying Hom_D(C_*(X;S),−) to the preceding triangle identifies the cokernel with the image in the theorem. For i=0, closed 0-forms are exactly the constant S-valued sections, proving the asserted degree0 formula.

For multiplication, Moore normalization with its shuffle map converts the cycle multiplication into

NZ_B^i⊗^L_B NZ_B^j→NZ_B^{i+j}.

After the identified shifts this is a map I_i⊗^L_B I_j→I_{i+j}. The source is homologically connective, and the target is a module in degree0. Hence this morphism is determined by its map on degree0 homology. The universal weightwise multiplicative comparison A-003 shows that this map is exactly T^[w]⊗T^[v]↦binom(w+v,w)T^[w+v]. One may test it on the two fundamental classes of S^i×S^j, using the exterior product of their normalized cycles. Thus it is the ordinary ideal multiplication. Base change gives the stated E pairing. On actual forms, multiplying a boundary da by a closed form z gives d(az), with the usual sign if needed. This proves independence of lifts in the image formula, and proves that its product agrees with the original product.

## Theorem A-007: completed coefficient version, no regularity assumption

Suppose S is complete and separated for its multiplicative PD-tail filtration F^rS, with γ_n(t)∈F^nS, and each F^rS the closed ideal generated by γ_n(t), n≥r. Complete simplex forms in total weight, giving variables and exterior generators weight1. Define \widehat E_r by completing the bar model above in the total filtration: s[a1|...|ah;b] has weight a1+...+ah+b plus the coefficient filtration of s. Equivalently its degree-h term is the product over aj≥1,b≥r of copies of S. In the first bar differential, the potentially infinite sums converge because γ_a(t)∈F^aS. All remaining coefficients use finite binomial sums. The product is the continuous bar-shuffle product.

Then exactly the same image formula holds for completed de Rham cochains, with E_r replaced by \widehat E_r. Proof: the normalized universal cycle resolutions are graded projective resolutions of I_r. They are graded-chain-homotopy equivalent to the graded bar resolutions (the comparison theorem, proved by lifting successively against surjections onto cycles; all lifts may be chosen homogeneous). Tensor these comparison maps and homotopies with S and complete. They remain continuous and remain mutually inverse up to chain homotopy. The objectwise Poincaré splitting is filtration preserving, so its split exact cycle sequences remain exact after completion; normalization commutes with this completion. Thus completed normalized cycles represent \widehat E_r[r]. The homotopy lifting argument and product argument of A-006 apply unchanged.

This supplies an exact answer even if grS is not a free divided-power polynomial algebra. A statement replacing \widehat E_r by the ordinary ideal F^rS needs additional hypotheses and is not asserted in this generality.

## Theorem A-008: completion under grS≅Γ_k(T)

Assume k=S/F^1S and that the canonical graded PD map Γ_k(T)→gr_F S is an isomorphism. Then the augmentation of the completed bar complex induces a quasi-isomorphism

\widehat E_r ≃ F^rS[0].

Consequently, for i>0,

H_DRhat^i(X;S) ≅ im(H^i(X;F^iS)→H^i(X;F^{i−1}S)).

Degree0 is H^0(X;S). Products are obtained by lifting to H^i(X;F^iS), taking coefficient cup product into H^{i+j}(X;F^{i+j}S), and passing to its image. The coefficient action is ordinary S-action.

Proof of the bar comparison: associated graded of the completed bar resolution is the bar complex obtained by tensoring the universal graded B-free resolution of I_r with Γ_k(T)=k⊗_ZB. Its higher homology vanishes because I_r is Z-free; its degree0 homology is ⊕_{n≥r}kT^[n]=gr_F F^rS. The augmented complex is complete and separated; in homological degree h its basis weights are at least r+h. For any fixed filtration bound only finitely many homological degrees occur. A closed positive-degree element can therefore be killed successively in its lowest filtration using graded exactness; the successive primitives converge in the completion. The same correction proves injectivity and surjectivity in degree0 onto F^rS. This gives a quasi-isomorphism, not merely an associated-graded calculation. Naturality of augmentation identifies the tail maps and multiplications, so A-007 gives the formula.

For the split universal completion k{{T}}, each inclusion F^iS→F^{i−1}S splits over k; the formula becomes ∏_{w≥i}H^i(X;k), with the binomial Cauchy multiplication of A-005. For a nonsplit base the image in consecutive ideals must be retained; it need not coincide with a tensor product or with the image in H^i(X;S).

## Finite test A-009: t=0 does not permit replacing derived tails by ordinary tails

Let S=k=F2, J=0,t=0, X=Δ[2]/∂Δ[2]. The ordinary ideal generated by t and all its divided powers is0. Nevertheless total weight2 of H_DR^2(X;S,0,0) is F2. In coordinates x=X_1,y=X_2, the relative weight2 complex has one generator in each degree0,1,2:

xy ↦ x dy+y dx ↦ 0, with top generator dx∧dy.

All boundary-face restrictions vanish: the faces x=0 and y=0 are immediate, and the third face y=−x gives xy=−2x^[2]=0 and xdy+ydx=−2x dx=0. The first displayed differential is an isomorphism and the second is0. There are no higher forms. Thus H^2=F2. These are all forms in that weight: the other degree0 and degree1 basis coefficients are forced to vanish by x=0 and y=0, and the third-face relation leaves precisely the displayed combinations. A finite program checks the spaces and differentials. Completion does not change this weight2 calculation.

This is a complete counterexample to an ordinary-tail formula without the associated-graded hypothesis, and a check that the derived correction in A-006/A-007 is essential.
