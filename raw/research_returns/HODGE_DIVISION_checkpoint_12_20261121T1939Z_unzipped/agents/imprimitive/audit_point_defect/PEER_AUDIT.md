# Independent whole-proof audit of SF-E817

**Result: PASS.** Reviewer `/root/imprimitive`, GPT-6 Astra Pro, effort inherited and not exposed; HODGE_DIVISION, 2026-11-21, approximately16:48–16:55 UTC. The complete written proof and every line of the author certificate were read. The exact proof hash is retained in the independent computational output.

## Canonical geometry and exact self-Ext sequence

The given translation/tensor action transports the actual double-dual map functorially, so the locally free hull and its finite-length quotient carry coherent equivariant structures. Grouping the canonical local-support decomposition by support orbits gives actual equivariant quotient summands; no individual noncanonical stable factor is linearized.

The two vanishing ranges are correct on a smooth fourfold. The first follows from the locally free source and finite support. The second follows from the four-variable regular local Koszul resolution and finite-length dévissage; the local-to-global sequence introduces no additional terms. Taking finite-group invariants is exact.

I independently reconstructed every map in the displayed long exact sequences. For the triangle T[-1]→E→H→T, the maps Ext^j(H,E)→Ext^j(H,H) are isomorphisms for j=2,3. The maps Ext^j(T,T)→Ext^j(T[-1],E) are isomorphisms for j=1,2. In the contravariant long exact sequence, both boundary maps are zero: under the second identification, a class b:T→T[j] maps to the composite H→T→T[j]→E[j+1], whose first two arrows form an element of Ext^j(H,T)=0. This proves the actual short exact sequence

`0 → Ext²_G(H,H) → Ext²_G(E,E) → Ext²_G(T,T) → 0`.

The proof does not use a splitting or degeneration of a hyper-Ext spectral sequence. Its use of the invariant category rather than ordinary dimensions is valid.

## Full cap-rank reconstruction

The Fock representative is the four-term vector with coefficients a,b,c,d. The two pure exterior blocks each have matrix determinant bc−ad, and thus rank two when the point defect is nonzero. The mixed block is the direct sum of four four-dimensional scalar isomorphisms, with nonzero coefficients a,b,c,d, so its rank is sixteen. These blocks have different bidegrees and cannot cancel. The full rank is exactly twenty.

Here a=r, b=c=−rq and d=rq²+length(T)/Delta. Positivity of r, Delta and length(T), and nonvanishing of q, make all four coefficients nonzero, and ad−bc=r length(T)/Delta is strictly positive. The balanced case has both pure blocks of rank one, hence total rank eighteen. A pure nonzero point class has pure ranks one and one and mixed rank four, hence rank six. Divisor shears conjugate the cap map by invertible transformations and do not alter these ranks.

I rebuilt the complete 28-by-28 exterior map with tuple wedge products, selected its nonzero support rows and columns automatically, and computed its generic determinant without importing the author script or its chosen minor. It is `(ad−bc)^2 (abcd)^4`, up to the harmless ordering sign. The three numerical ranks are eighteen, twenty and six. A separately expanded truncated exponential calculation recovers the entire rank-eighteen balanced character after the length-sixteen modification. These exact calculations are retained in `independent_check.py/.json` and do not purport to compute categorical Ext groups.

## Invariants and the quantitative trace kernel

The evaluation map lands in invariant Ext because the specified translation/degree-zero-tensor action is trivial on Hochschild cohomology. Its composition with full trace is cap with the Chern character. Thus the hull contributes at least twenty invariant degree-two self-Ext directions and each actual support-orbit summand contributes at least six. The exact sequence gives e₂(E)≥20+6s.

I freshly reread the supplied DEG_L S-20 adjunction paragraph and S-21 identity-sector, coherent-action, Serre-pairing and trace/evaluation passages, including equations S21.4–S21.8 and the intervening proof. They apply here without a simplicity hypothesis. The finite action preserves the Calabi–Yau pairing, and averaging makes its restriction to invariant Ext nondegenerate. Consequently evaluation and trace have the same rank h. If k=e₂−h, then the composition inequality is `18 ≥ 2h−e₂ = e₂−2k`, hence k≥1+3s. This is an actual trace-kernel lower bound, not only an obstruction inferred after assuming injectivity.

The supplied categorical framework remains an accepted input with its stated publication status. This audit does not claim a fresh independent reading of every Perry or companion-paper dependency cited inside that supplied framework.

## Actual example and scope

The integral matrices S and US from E815 provide the required line-bundle classes. The full exponential sum is `18+24(x²+y²)+36x²y²`. Removing sixteen points subtracts `4x²y²`, leaving `18(1+4x²/3)(1+4y²/3)=18v_(8/3)`. The kernel of an actual fibrewise surjection is torsion-free, has the claimed locally free double dual, and is locally `m_p ⊕ O^17` at each chosen point, so it is singular. The primitive divisor classes give slope zero, and the kernel is semistable as a subsheaf of a polystable bundle with the same slope.

For the trivial action there are sixteen support orbits, giving the stated lower bound forty-nine. Under an arbitrary effective coherent finite action, the theorem retains the correct orbit count. The result is restricted to zero-dimensional defects of a locally free hull; no conclusion about positive-dimensional defects or singular reflexive hulls has been added.
