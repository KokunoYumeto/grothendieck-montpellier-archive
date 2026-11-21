# Independent review of PLE-F8

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Date: 2026-11-21 UTC.

## Result and actual review scope

**PASS.** Before the full draft was available, I independently reconstructed the proposed algebraic isomorphism from its formulas, including direct expansions of the derivation and relation. I then read the complete author draft `work/positivity_actual_plethysm.tex` and checked every proof step and consequence, including the positive basis, integral model, finite-field assertions, and scope qualifications. The first event is an independent re-proof from the proposed statement; the second is an independent-agent targeted whole-proof review of the actual draft. Neither is a formal proof-assistant certificate or a historical-priority determination.

## Independent algebraic verification

Write `h=ac-b²`, `j=a²d-3abc+2b³`, and `delta=a²d²-6abcd+4ac³+4b³d-3b²c²`. The derivation satisfies `E(a)=0`, `E(b)=a`, `E(c)=2b`, `E(d)=3c`. Hence

- `E(h)=2ab-2ab=0`.
- `E(j)=3a²c-3(a²c+2ab²)+6ab²=0`.
- Directly, the five terms of `E(delta)` give respectively `6a²cd`, `-6a²cd-12ab²d-18abc²`, `24abc²`, `12ab²d+12b³c`, and `-6abc²-12b³c`; their sum is zero.

Expanding `j²` gives

`a⁴d²+9a²b²c²+4b⁶-6a³bcd+4a²b³d-12ab⁴c`.

Adding `4h³=4a³c³-12a²b²c²+12ab⁴c-4b⁶` gives exactly `a² delta`. This proves the required relation independently of a general binary-cubic invariant theorem.

The degree/weight pairs of `a,h,j,delta` are `(1,3),(2,2),(3,3),(4,0)`. Thus `u=h²delta`, `v=aj delta²`, and `w=a²h delta³` have pairs `(8,4),(12,6),(16,8)`, respectively. Set `z=w-2u²`. Then

`v²+4uw=a⁴delta⁵` and `w²=u(v²+4uw)`.

It follows by expansion that `z²=uv²+4u⁴`. All these elements lie in the required highest-weight diagonal.

For algebraic independence, let a nonzero relation `F(u,v)=0` be given and divide `F` by the largest common power of its first formal variable. The domain property and `u!=0` preserve the relation. The resulting polynomial has nonzero specialization `F(0,Y)`. At `a=1,b=c=0`, the formulas become `u=0`, `v=d⁵`, so one obtains `F(0,d⁵)=0`, which is impossible in the polynomial ring in `d`. This proves independence without a dimension or Jacobian shortcut.

Over `K=C(U,V_0)`, the rational function `UV_0²+4U⁴` has valuation one at the prime `U`: the factor `V_0²+4U³` is a unit there. It is not a square. The monic quadratic in `Z` is therefore irreducible over `K`, and the relation just checked defines an embedding of its degree-two field extension into `Frac(S)`. Restricting gives injectivity of the claimed algebra map. Alternatively, the monic relation gives a unique remainder `A(U,V_0)+Z B(U,V_0)`, and a vanishing nonzero remainder would contradict either the independence of `u,v` or this nonsquare property.

The source ring is free with basis `1,Z` over `C[U,V_0]`; its Hilbert series is `(1+t⁴)/((1-t²)(1-t³))`. Its graded dimensions are therefore the previously established `phi(s)`. The highest-weight calculation below supplies the same dimension for each target piece, so the injection is surjective degree by degree. This is an algebra isomorphism, not just a comparison of characters or Hilbert functions.

## Highest-weight and source check

In `Sym^(4s)(Sym³ C²)`, the central character has weight `12s`. A `GL_2` constituent with highest weight `(p,q)` has highest `SL_2` torus weight `p-q`, and the raising derivation kills exactly its highest vector. Requiring torus weight `2s` therefore forces `p+q=12s` and `p-q=2s`, hence `(p,q)=(7s,5s)`. Complete reducibility over `C` identifies this highest-weight space with the usual multiplicity space after a highest-line choice. The product is the inherited product of these actual highest-weight spaces.

I rechecked **Kahle--Michałek, Theorem 5**, in `work/positivity_sources/KM.txt` against its previous primary retrieval. The theorem explicitly states the multiplicity formula for **both** `Sym³(Sym^(4s))` and `Sym^(4s)(Sym³)`. Thus this application does not silently extend Hermite reciprocity to more general shapes. Its partition `(7s,5s,0)` is the same two-row Schur functor; evaluating on `C²` preserves these two-row coefficients, while longer Schur functors vanish. The formula at `s=0` is checked directly. Exact primary URL: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p41/pdf>, printed p. **4**, Theorem **5**, and Remark **6** for the homogeneous Ehrhart obstruction. Earlier own retrieval ref: `turn574800003view1`. This event rechecks the relevant source text; it is not a new scan-image check.

## Basis, integral model, and finite fields

The integral hypersurface quotient is free over `Z[U,V_0]` with basis `1,Z`, hence free over `Z` on the indicated monomials and flat. The same polynomial-division argument works after arbitrary coefficient base change, so every fiber has the same graded Hilbert function. Multiplying basis monomials requires at most the one reduction `Z²=UV_0²+4U⁴`, whose coefficients are nonnegative integers. This basis is positive as an algebra basis; no claim that it is a crystal or canonical basis follows.

The finite-field assertion is precisely the earlier verified PLE-F7 hypersurface and grading, under its same conditions `q=1 mod12` and `ell` prime to `6q`. Thus its compactly supported ordinary cohomology and intersection complex have the stated pure Tate forms. The paragraph correctly distinguishes the explicit flat integral model of the characteristic-zero algebra from a possible kernel of the reduced Lie-algebra operator: in characteristic `p`, `E` kills `p`th powers and its kernel can enlarge. No equality with modular highest-weight multiplicities is asserted.

Normality follows from the already established binary-dihedral invariant-ring presentation in characteristic zero; the pure finite-field geometry does not identify the weight grading with cohomological degree. The conclusion therefore correctly refutes an implication from these properties alone to literal homogeneous PH1, while leaving richer canonical-basis compatibility conditions and the narrow quantitative PH2/PH3 questions open. In this example the exhibited positive denominator weights are already two and three.

## Editorial clarification

I suggested making explicit that `a,b,c,d` are independent polynomial generators in `Sym(Sym³V)`. The expressions `x³,x²y,xy²,y³` identify vectors in the basis of `Sym³V`; multiplication relations among these expressions in `Sym(V)` are not relations among the four generators in `Sym(Sym³V)`. The conventional original wording is mathematically correct, but the clarification prevents mistakenly setting `ac=b²`. No mathematical correction was required.
