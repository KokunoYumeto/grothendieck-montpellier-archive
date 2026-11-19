# Direct audit and reconstruction of R-vanishing on the actual Johnson image

19 November 2026. Work-only supplement; the production F.3.32 text has not been changed during this audit.

## Exact source statement and what its sketch supplies

The opened original MSS2026 v1, *The first Galois obstruction in the Johnson cokernel*, printed pp. 9–11, defines an Sp-equivariant map from `Ker ES7` to the standard representation H which kills the actual degree-seven Johnson image J7. Proposition 4.1 on printed p. 11 extends it to a five-term contraction on the full ninth tensor power. These are exactly the coefficients used in F.3.29–32. The proof is explicitly headed “Sketch of Proof”; it says the formula is obtained by evaluating on the H and primitive-third-exterior-power isotypical components. The six concrete Johnson vectors and their contraction matrix are not printed there.

The original MSS2015 v2, *Structure of symplectic invariant Lie subalgebras of symplectic derivation Lie algebras*, proof of Theorem 7.5(iv), printed pp. 29–30, already gives the stable multiplicity

`J7[H] = 6 H`.

Its stated dimension argument is: the H-multiplicities of h7 and the formal filling ideal j7 are 10 and 3; the ES7 image multiplicities on those spaces are 3 and 2. Hence `Ker ES7` has H-multiplicity 7 and its intersection with j7 has H-multiplicity 1. The actual Johnson image lies in `Ker ES7` and has zero intersection with j7, the latter being Proposition 3.5(ii), printed pp. 16–17. Thus its multiplicity is at most 6. Six explicit Johnson copies give equality. The present reconstruction only needs the upper bound from that older calculation, and supplies its own six concrete copies and all R evaluations.

The proof below first works in any sufficiently large genus G in that source's stable range, with G at least 5. No unverified minimal genus cutoff is assigned to the source's degree-seven multiplicity calculation. Since arbitrary genus embeds in a larger stable genus, this is enough to prove the desired result in every genus at least 3.

## Six literal actual Johnson vectors

Use symplectic basis letters numbered 0,...,9, with pairs (0,1), (2,3), (4,5), (6,7), (8,9), and form +1 on each ordered pair. For an ordered triple t=(u,v,w), define

`delta_t(z)=<z,u>[v,w]+<z,v>[w,u]+<z,w>[u,v]`.

This is the actual degree-one Johnson element corresponding to `u wedge v wedge w`. For each of the following seven-triple rows form the left-nested bracket `[[[[[[delta_t1,delta_t2],delta_t3],delta_t4],delta_t5],delta_t6],delta_t7]`:

| vector | ordered triples |
|---|---|
| Z1 | (3,7,5); (1,2,0); (9,8,6); (6,8,5); (2,4,7); (9,0,3); (4,6,7) |
| Z2 | (9,5,0); (6,4,7); (6,2,0); (6,5,8); (7,3,8); (1,4,3); (9,2,7) |
| Z3 | (1,3,4); (4,2,0); (5,7,0); (9,2,7); (5,6,8); (5,3,0); (1,4,6) |
| Z4 | (0,1,4); (3,5,0); (9,0,5); (2,3,9); (4,6,8); (8,1,0); (2,7,1) |
| Z5 | (3,7,0); (4,9,6); (3,5,2); (7,3,8); (6,7,2); (0,8,9); (1,2,6) |
| Z6 | (5,4,0); (0,8,1); (5,2,3); (7,4,3); (0,4,1); (6,5,2); (6,7,9) |

Each Zi lies in the actual J7 because J is a Lie subalgebra and every factor is an actual J1 element. Their degree-seven derivation tensors have torus weight x1, namely weight vector (1,0,0,0,0). The computation verifies this on every term and verifies specialness `Zi(omega)=0` by literal substitution. These assertions also follow from the actual Johnson map and the bracket definition.

## Exact detector and the finite certificate

For every perfect matching C of positions 1,...,8 define the H-valued map

`K_C(u1 tensor ... tensor u9) = product_((i,j) in C)<ui,uj> * u9`.

There are 105 matchings. List them recursively by pairing the smallest remaining position with each possible partner in increasing order, then recursing on the remaining positions. Every `K_C(Zi)` is a multiple of x1, by its torus weight. The standalone program `work/check_R_J7_six_generators.py` recomputes all six full word derivations and all 630 scalar coefficients. It uses only exact Python integers and a rational SymPy matrix calculation; it reads no stored matrix or witness file.

The six detector columns with zero-based indices `(1,2,4,7,8,10)` give the exact matrix

```
 18   12   -2   15   -7  -10
  0    3    0   -4    4    0
 15  -24    3    2   -5    6
-17   14  -10   11  -11   -4
 -3  -10    2  -15    3   16
  2  -16   -1    2   -3    0
```

Its determinant is exactly **−203784**. The five displayed R contractions of MSS2026 Proposition 4.1 give

`(R(Z1),...,R(Z6))=(0,0,0,0,0,0)`.

The fixed-witness certificate passed in **2.430248686 seconds**. The earlier deterministic search is preserved separately as `search_R_J7_generators.py/.output.txt/.json`; its output supplied the six fixed rows but is not a dependency of the final program.

## Why these six checks establish the complete vanishing

1. In characteristic zero, every Sp-equivariant map from the special derivation space h7 to H extends to the ambient ninth tensor power, by complete reducibility. The symplectic invariant tensor theorem spans those ambient maps by contracting four pairs and leaving any one of the nine positions as output: there are 9 times 105 such maps.

2. Every special derivation tensor is invariant under cyclic rotation of its nine positions. Rotate any chosen output position to position 9. The remaining pair contractions become one of the 105 displayed matchings, with its explicit alternating-form signs. Thus the 105 maps K_C span **all** maps from h7 to H. Their joint map is injective on the H-isotypical summand: otherwise an H copy in its kernel would admit a nonzero equivariant map to H, contrary to the spanning property.

3. Let e_H be the projector to the H-isotypical component. The vectors Zi themselves may have components in other irreducible representations. Every K_C kills those components. Hence the nonzero six-by-six determinant proves that the six vectors e_H Zi are independent in the weight-x1 subspace of the H-isotypical part of J7. The source upper bound gives that this weight space has dimension at most six. They therefore form a basis of that weight space. Their Sp-orbits span the entire H-isotypical part.

4. The tensor map R is Sp-equivariant by its literal contraction formula, so it vanishes automatically on every irreducible component not isomorphic to H. Since R(Zi)=R(e_H Zi)=0 for all six basis vectors, equivariance makes R vanish on the entire H-isotypical part as well. Therefore **R(J7)=0** in every stable genus.

5. The six witnesses use only five handles. Under inclusion in any larger genus, their tensor expressions and every contraction coefficient above are unchanged. Thus the same nonzero determinant and all six R zeros apply throughout the stable range; no interpolation in genus is involved.

6. For an arbitrary genus g at least 3, extend the actual boundary mapping class by the identity to a surface of stable genus G at least g. Its actual Johnson derivation extends by zero on the extra handles. For the inclusion i, the five contraction formula gives exactly `R_G(i^tensor9 T)=i R_g(T)`. Vanishing on the actual stable Johnson image and injectivity of i imply `R_g(J7)=0`. The same argument works for the strict Malcev/actual geometric image used in F.3.24, via its identified graded Johnson image; no filtration-kernel density is asserted.

## Audit verdict and retained dependency

The 2026 sketch states the precise theorem used in F.3.32 but does not print its finite six-vector computation. The fixed-witness certificate and the six steps above now reconstruct that computation and its full representation-theoretic implication. This gives a proof of the used R-vanishing statement **without importing the 2026 Proposition 4.1 vanishing assertion**. The explicit five-term formula is still taken from that opened source and checked directly. The remaining dimension input is the older MSS2015 stable multiplicity bound, with the exact dimension/intersection derivation and locators stated above. This audit does not claim to independently recompute every character or ES-rank calculation in the older paper.

Sources: opened originals `work/sources_audit_next/MoritaSakasaiSuzuki2015_v2.pdf` (https://arxiv.org/pdf/1404.3351), pp. 16–17 and 29–30; `work/sources_audit_next/FirstGaloisObstruction2026_arxiv2608_17673.pdf` (https://arxiv.org/pdf/2608.17673), pp. 9–11 and 27. The actual generation and strict-image maps were separately reopened by generation in Enomoto–Satoh Theorem 3.5/Proposition 3.6 p. 640 and Hain1997 pp. 610–611, 643.
