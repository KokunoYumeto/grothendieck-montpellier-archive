# Independent whole-proof audit of SF-E836

**PASS. No mathematical repair requested.** The complete frozen draft, the author's entire certificate, the new published socle input and its invoked proofs, and the E819 deformation interfaces have been read and checked. An independently written exact algebra supplement also passed.

Auditor: `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`. Actual audit/computation completion: **2026-11-21 21:48:14 UTC**. This records the draft actually reviewed, not an unperformed rereading of its later canonical TeX conversion.

Frozen draft: `agents/sixfolds/rm_ci_point_quantization_obstruction_draft.md`, SHA-256 `e63e9b1cc184b675d6a141673b9fb0d6a3c9fa512af7346378d42eaac03f035b`.

## 1. Exact hypothesis and local reduction

The local statement concerns a common Artinian complete-intersection quotient `A=R/I` and defect modules free over that same quotient. The chosen four actual generators are a regular sequence. The three designated generators commute modulo I for one of the two complementary constant bivectors. None of these hypotheses is replaced by a statement about arbitrary finite modules or arbitrary embedding-dimension-four ideals.

I reread the complete E819 map-lifting, finite-perfect-cone, commutator-trace and completed-local characteristic-map arguments at their points of use. In particular, the finite-length filtration and four-variable Koszul resolution give the needed Ext vanishing into the free hull. The lifted Hom-complex obstruction is indeed Ext1(M,R^r), which vanishes. Flatness over the dual numbers identifies the kernel of reduction with the epsilon multiple; the finite free resolution argument keeps formal operations continuous. The cone has finite cohomology and finite Tor amplitude over the dual numbers, so its supertrace is a finite-complex trace, not a trace on an infinite-dimensional power-series module.

The supertrace conclusion forces `ell*m=ell*n`. Since the quotient has positive length, the nontrivial case has `m=n>0`. The ordinary quotient-basis change and splitting of the remaining free summand are legitimate; no deformation of that chosen splitting is assumed. Koszul duality gives exactly six matrices in `Mat_m(A)` for the extension class.

## 2. Both matrix orders

The map C from T to Q is well-defined. A different lift of a torsion element changes the coefficient of its hull image by an element of K, and reduction to Q removes it. Since the hull image has zero reduction, multiplication by an ordinary coefficient on that image is simply multiplication by the same coefficient in the epsilon term. Thus C is A-linear.

Applying the lifted hull map to the relations gives `C B_ij=P_ij I`. It suffices to apply the relation to constant basis vectors of R^m; for a general coefficient vector any extra differentiation term has an ideal-generator factor and also vanishes modulo I.

I independently followed the opposite-order calculation. From `f_i*tilde(t)=epsilon*tilde(m_i)` one obtains `phi(m_i)=f_i c`. Decomposing m_i using the ordinary chosen lifts and the free-part splitting introduces only a torsion term and a commuting free term. In the commutator, the former is annihilated by I and the latter cancels. The remaining term is `B_ij C(t)`, while the star commutator is `P_ij t`. Hence `B_ij C=P_ij I`, with the same sign as the first equation. Because this calculation is already the epsilon coefficient, no derivative of the chosen lift of c is lost.

Associativity now implies the displayed scalar cross-minor equations for the two independent deformations. They do not require the deformations to form a joint two-parameter deformation. They also do not require any matrix or coefficient to be invertible. In particular all steps are valid over the nonreduced quotient with zero divisors.

## 3. Wedge contradiction and source

The commuting triple is used essentially: all plus-bracket entries with both indices at least2 are zero. Each potentially nonzero term in the mixed fourth wedge is therefore killed by one of the cross-minor equations. This is a termwise argument; it does not infer proportionality of forms over an Artinian ring.

For the Jacobian J, the bracket matrices are `J Pi_plus J^t` and `J Pi_minus J^t`. The mixed exterior-power identity is exactly the determinant transformation. With the stated ordered planes, its constant coefficient is nonzero. The Jacobian class in A is nonzero by the zero-dimensional complete-intersection socle theorem, giving the contradiction.

I freshly read the original published Eisenbud–Ulrich source:

David Eisenbud and Bernd Ulrich, *Duality and socle generators for residual intersections*, Journal für die reine und angewandte Mathematik **756** (2019),183–226, DOI10.1515/crelle-2017-0045. Published author-hosted full PDF: <https://www.math.purdue.edu/~bulrich/papers/published%20version%20of%20Duality%20for%20Residual%20Intersections.pdf>.

Local PDF SHA-256: `fa8959341544a1dd80f7789709039ba401dabc9972d935da753ac3fe9abdd949`.

Theorem7.1 on printed p.210 explicitly includes complete local power-series algebras in characteristic zero and identifies the nonzero Jacobian ideal with the socle for a zero-dimensional complete intersection. I read the complete invoked Appendix proofs: TheoremA.1 and its four steps on pp.222–223; TheoremA.3 on p.224; TheoremA.5 on pp.224–225; and the following proof of Theorem7.1. The positive finite length is nonzero in characteristic zero, exactly as needed in the trace argument of A.5. No polynomial-only hypothesis is silently substituted for the formal setting.

The theorem is used as a known published result. This audit does not claim an independent reconstruction of all upstream different theory cited in that paper.

## 4. Formal generator reduction and covariance

If the embedding dimension is at most3, I contains a function with a nonzero linear term. Its class is nonzero in `I/mI`, so it extends to a minimal four-generator set. These four parameters in the regular local ring form a regular sequence.

A linear change inside one of the two planes makes the x derivative nonzero. The implicit solution `x=phi(y,z,w)` then allows a unit change of the first generator and triangular changes of the other three. The ambient Poisson coordinates are not changed nonlinearly. Thus the other three generators become independent of x and their plus brackets vanish, including when phi has a mixed linear conormal component.

Under a generator change U, differentiation modulo I gives `df'=U df`. In the ordinary extension presentation the matrices transform by the same second exterior power. C does not change. The companion equations and the unit change of the Jacobian therefore remain valid. There are no surviving derivatives of U modulo I.

## 5. Global consequence and actual examples

The two balanced cap-kernel classes retain the two required bivector projections after the divisor shear. The reviewed E819 characteristic-map bridge takes weak invariant semiregularity to vanishing of the ordinary local multiplication obstruction for each of them. I rechecked the complete interface in the written E819 argument. Its Buchweitz–Flenner and supplied S21 equivariance inputs are retained as earlier checked inputs; I do not claim a new complete source audit of those papers or of the supplied theorem in this E836 event.

The local action need not preserve any chosen defect basis or ideal presentation. The argument only requires the specified coherent action on the actual global object. It consequently gives the stated obstruction for every such action, without claiming that an action exists.

For the examples, both displayed ideals are finite complete intersections. The mixed-linear quotient has length8 and embedding dimension3; the square quotient has length16 and embedding dimension4. Their finite formal quotients descend to algebraic finite subschemes through sufficiently high jets. This does not assert algebraicity of the formal logarithm. The rank32 balanced vector bundle is the previously checked E815/E820 input, not reconstructed anew in this audit.

The quotient from the bundle exists over each local Artinian subscheme. Ext into a point-supported module from a vector bundle vanishes in positive degree, and the Koszul resolution gives extension dimension `6m^2 ell`. An extension E has torsion exactly T because its image K is torsion-free; its double dual is H and its hull cokernel is Q. The full character is unchanged because T and Q coincide in K-theory. Coherence gives ordinary gluability. Simplicity, indecomposability and existence of an equivariant structure are correctly left unasserted.

## 6. Independent exact supplement

`independent_check.py` uses integer polynomial dictionaries and a free-associative word algebra; it imports none of the author's SymPy arithmetic. The author's code was read first, so the reconstruction is not described as blind.

The checker proves the mixed-wedge/Jacobian identity with all16 first derivatives independent, then performs the elimination substitution and verifies the three cross-minor reduction. It independently expands the companion-equation syzygy in a free associative algebra with central scalar coefficients. Finally it reconstructs the two actual quotient socles, obtaining `8*y*z*w` and `16*x*y*z*w`, with their annihilation and nonzero cross-minor values. The corresponding extension dimensions are48m² and96m².

Actual result: **PASS,0.001669476 seconds**, at21:48:14 UTC, saved in `independent_checked.json`. No failed attempt occurred. The finite algebra supplement does not certify the module deformation, global geometry, formal implicit function or published socle theorem; those are covered by the complete mathematical/source audit above.
