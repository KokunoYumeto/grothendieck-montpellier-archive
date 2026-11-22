# Complete root audit of C.3au

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), /root. **PASS of the complete revised proof**, with the restricted Fermat-quintic scope. This is not a result for the general quintic or for all three-dimensional singularities.

## Target and finite detection

The root read the full six-step proof, including its revised first-jet trace paragraph, and the full finite-certificate program and output. For the specified smooth Fermat quintic surface V, adjunction gives K_V=O_V(1)=L. The split thickening and the previously audited C.3ad weight-two calculation leave exactly H²(V,L)⊗Ω¹_(C/Q): the relative differential part vanishes by Kodaira–Akizuki–Nakano, and H²(V,L^j) vanishes for j≥2. Restriction to the first thickening therefore detects the whole relative rational weight-two group. Finite K0 detection and the Chern character imply that zero exceptional restriction together with zero first conormal invariant forces a rational Chow class to be zero. This is an injectivity argument, not an assumption that all formal K0 classes algebraize.

## The specified product cover

The map from the two plane quintics sends (a,b,c;t,v,w) to (tc,wc,va,vb). Its equation is exactly v^5(a^5+b^5+c^5)−c^5(v^5−t^5−w^5). The 25 base points are reduced, with local ideal (c,v). Each blow-up chart removes one common factor, so a single blow-up resolves the map and gives L′=pi* M(−E). On the generic chart, v has five possible roots and determines a,b uniquely, giving degree five. Characteristic zero makes this generic extension separable. L′ is explicitly not assumed ample.

The pulled-back strict-local line bundle total space Z′ is regular and proper over R. Its special divisor is T with multiplicity one, and the pulled-back maximal ideal is its Cartier ideal. Thus the first infinitesimal neighbourhood used in the line-bundle argument really is reduction modulo m_R².

## Actual line bundles and actual families

For a∈H¹(T,L′), the exponential of a degree-one formal cocycle gives a compatible invertible sheaf. Proper formal existence over the complete noetherian base algebraizes it. Its special fibre is invertible; Nakayama and properness show the algebraization is a line bundle on the entire scheme. Excellence and Popescu write the completion as a filtered union of smooth finitely presented R-algebras. The line bundle and its trivialization/first jet descend as finite data to one of them. The henselian smooth lifting lemma then produces an actual R-point with that same reduction modulo m². Only the first jet is preserved; no false claim about all higher coefficients is used.

The product c1(A_a)c1(q_B*O(q−o)) is ordinary algebraically trivial on the actual fixed Z′, using the diagonal-minus-o divisor on the proper parameter curve B. Its restriction to T is zero. The first conormal coefficient is a cup epsilon(O(q−o)), with the symbol normalization already established in C.3ar.

The blow-up has Rpi*O(−E)=I_(25 points), so H¹(L′) surjects onto H¹(M), and H²(L′) identifies with H²(M). These identifications commute with cup product by the pulled-back Picard class. The chosen nonzero section of O_B(1) induces a surjection H¹(O_B)→H¹(O_B(1)), because its Serre-dual multiplication map on sections is injective. The degree-15 map (t/w)^3 supplies 15 distinct unramified points over any transcendental parameter value. A canonical form has degree 10, so evaluation there spans the entire dual of H0(K_B). The resulting coefficient forms span all H²(T,L′)⊗Ω¹_(C/Q). Arbitrary complex scalars are absorbed into a before the actual line bundle A_a is constructed; no complex scalar multiplication on a Chow group is assumed.

## The corrected trace calculation

The initial wording paired an uncontracted coefficient-field one-form with a relative surface top form. Root requested a precise replacement. The final paragraph first applies minus contraction by a Q-derivation theta, then projects to relative degree-one differentials. Its normal coefficient has the correct sign because iota_theta(dt wedge omega_coeff)=−dt theta(omega_coeff).

A section eta of K_V⊗L^−1 has local representatives omega_i with omega_j=g_ij omega_i, while the fibre coordinates satisfy t_j=g_ij t_i. Consequently omega_i/t_i is a global meromorphic relative two-form with a simple pole along V. Wedge of the contracted relative one-form with omega/t, followed by the adjunction residue, pairs its normal coefficient with eta. The horizontal term vanishes because three horizontal relative differentials vanish on a surface. This establishes the exact tensor-conormal functional before any pushforward is used.

Proper supported Hodge trace is adjoint to pullback of this meromorphic form. On normalized curve supports it is the finite trace–residue identity with the actual branch degrees and intersection multiplicities. Thus the source pairing is with f*eta, and Serre duality identifies the resulting cohomological map precisely as tr_(f,L). Contraction commutes with trace because the geometric map and the line bundles are defined over Qbar. Derivations separate coefficient-field forms. This proves the required first-jet pushforward identity, including the ramification locus, with the stated normalization.

The use of supports is legitimate: on a finite quasi-projective model, choose a rational section of A_a that is a unit at the relevant generic points of the fibre divisors and of their intersections with T. Semilocal triviality permits this finite set of conditions. The resulting product-cycle components are curves not contained in T, so they meet T at finitely many points. Normalization reduces their local traces to finite curve-branch traces. No attempt is made to restrict a residue fraction whose whole support lies inside the exceptional divisor.

Root actually opened and read El Zein (1978), the supported Hodge-duality construction on pp.31–32, the residue construction on pp.32–33, and §3.1 Proposition2, p.41, together with El Zein (1974), Proposition2.1.2, pp.15–16. The printed heading of the residue paragraph has inconsistent numbering, so the final manuscript cites its pages rather than inventing a stable §2.5 locator. Primary URLs:

- https://www.numdam.org/item/MSMF_1978__58__1_0.pdf
- https://webusers.imj-prg.fr/~fouad.elzein/fondamentale.pdf

The Cartier square is Tor-independent with multiplicity one, so exceptional refined pullback commutes with proper pushforward. Pushforward of the actual parameter family remains an actual family. Since f is generically etale, pullback of the nonzero section of K_V L^−1 is nonzero; its Serre-dual trace onto H²(V,L) is surjective.

## Elimination, conclusion and finite certificate

Every class in the kernel of exceptional restriction has the same conormal invariant as a finite sum of the actual ordinary pushforwards above. Their difference has both invariants zero and hence is rationally zero. Subtracting the actual projection pullback treats an arbitrary class. The ordinary quotient on V is degree, and the exceptional image has nonzero degree by its normal self-intersection. Therefore B²(Z)_Q≃Q and B²(X)_Q=0, exactly as claimed.

The finite program verifies the Fermat image equation, both blow-up charts, the generic inverse, reduced base-point polynomials, genus and evaluation degrees, the cohomological dimensions stated as elementary values, and coefficient one in the first logarithmic jet. The full output was read. Runtime: 0.14749093900172738 seconds, at 11:15:39.329281 UTC. These finite algebra checks do not replace the cohomological trace or actual-family algebraization proof. No independent rerun is claimed.

The result is a restricted positive top-cone theorem. It does not count as movement of the unrestricted rational top gate in a scheduled review.
