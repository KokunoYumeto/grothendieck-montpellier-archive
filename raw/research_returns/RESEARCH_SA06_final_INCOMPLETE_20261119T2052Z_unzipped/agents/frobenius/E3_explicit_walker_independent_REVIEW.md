# Independent audit of the specified generic Walker counterexample

## Outcome

The proof of E.3r in research/agents/cycles/explicit_walker_counterexample.tex passes this independent proof and primary-source audit. It specifies the generic fourfold and the exact Legendre point of order two, and gives a mathematically exact selection rule for the auxiliary integral cycle. It does not give polynomial equations for that auxiliary cycle. The construction is a function-field example over an algebraically closed field of characteristic zero, subsequently embedded in the complex numbers.

The only suggested clarification concerns the quantifier over embeddings. If the statement intends one selected cycle gamma to work for every embedding K into C, the proof should explicitly add the intrinsic mod-two étale-cohomology argument below. This is a valid strengthening of the written proof, not an obstruction to its conclusion for a fixed embedding.

## 1. Geometry of the family and integral parity transfer

There are exactly 72 independent coefficients: two rows, three columns, two monomials in the first projective-line coordinates, and six quadratic monomials in the appropriate projective-plane coordinates. The first-row zero scheme has degree 12 because the degree of (h+2l)^3 on P1 times P2 is 12. On an open set where the threefold is smooth and this scheme is finite étale, its product with the second projective plane is an effective Cartier divisor. One may choose this open to contain an Ottem–Suzuki rational matrix having their parity obstruction.

The relative Hilbert argument preserves integral coefficients. A curve over the complex realization of the generic coefficient tuple gives a point of a finite-type relative Hilbert scheme whose image in the coefficient space, considered as a Qbar-scheme, is the generic point. An irreducible Hilbert component containing that point therefore dominates the coefficient open. Its proper image is closed, so it has a point over the chosen Ottem–Suzuki matrix. The special subscheme has a one-cycle with integral multiplicities; no irreducibility of that special subscheme is required. Degrees against the two specified line bundles are constant in the flat Hilbert family, by the constancy of Euler characteristics. Embedded and zero-dimensional components do not contribute to these degrees. Thus the parity congruence transfers with coefficient one. There is no finite-cover trace or extension-degree multiplier.

The current wording, “one-cycle with integral multiplicities,” correctly avoids confusing an integral-coefficient cycle with an irreducible curve.

## 2. The defect class, its minimal multiple, and descent

Parallel transport of the Ottem–Suzuki integral homology class along the connected smooth coefficient open preserves its two intersections, one and zero. Their torsion-freeness result applies to the integral cohomology. Their H2(O)=0 assertion, Hodge decomposition, and hard Lefschetz make every rational fourth-cohomology class algebraic and every integral fourth-cohomology class a Hodge class. Thus the algebraic subgroup B has finite index in the torsion-free lattice H4.

Let m be the least positive integer with m beta in B. The transferred parity condition forces m to be even. If m beta were in 2B, torsion-freeness of H4 would imply that (m/2) beta belongs to B, contrary to minimality. Therefore m beta tensor 1/2 is nonzero in B tensor Q/Z, while its image in H4 tensor Q/Z is zero. Any algebraic representative gamma consequently has gamma tensor 1/2 nonzero in CH2(W) tensor Q/Z.

The descent of gamma to the algebraically closed coefficient field k is valid. For each integral component in a complex representative, take a component of the Hilbert scheme of the fixed k-variety containing that geometric point and then a k-point on it. Over an algebraically closed field, the relevant reduced irreducible components are geometrically irreducible. Connecting points by curves in such a component gives algebraic equivalence of the corresponding integral cycles, hence preserves integral cohomology classes. No norm is needed and no integer is introduced.

For a single gamma to work under every embedding, use the following intrinsic formulation. Its nonzero class in CH2(W/k) tensor Q/Z has already been established over k. Its mod-two étale cycle class is zero over k, because smooth proper base change identifies that group with the mod-two comparison group under the embedding used to construct gamma. Hence its cycle class is even under every complex embedding. Schoen injectivity and the Deligne calculation then apply unchanged under each embedding. This supplies the optional uniform-embedding clarification.

## 3. Exact Schoen theorem and the selected point of order two

We directly opened the local primary PDF and viewed the theorem on printed p.177. Schoen's Theorem (0.2) assumes precisely: k and K algebraically closed, W smooth proper over k, E a genus-one curve over K with j-invariant transcendental over k. Its injectivity statement is for CH(W) tensor CH(E)tors as a whole. It does not remove the prime two and does not single out a special torsion direction.

For the specified Legendre equation, the discriminant is 16 t^2(1-t)^2 and its j-invariant is the nonconstant rational function 256(1-t+t^2)^3/[t^2(1-t)^2]. Transcendence of t over k gives the required transcendence of j. The difference (0,0)-infinity is a nonzero point of exact order two. Any such point is the image of 1/2 in a direct summand Q/Z of the elliptic torsion group (Q/Z)^2: extend that nonzero vector in the two-torsion subgroup to a basis of the divisible torsion group. Consequently gamma tensor tau is nonzero, and Schoen's theorem makes its exterior product nonzero of exact order two.

## 4. Deligne cohomology and Walker torsion injectivity

The Deligne sequence has divisible kernel J2(W). The tensor product of a divisible group with a torsion group is zero. Right exactness of tensoring therefore identifies the tensor product of H_D^4 with the elliptic torsion group with the corresponding tensor product of the integral Hodge lattice. Multiplicativity of the Deligne cycle class sends the exterior product through this latter tensor product. Its value is m beta tensor tau, which is zero because m is even. Thus the product is Abel–Jacobi trivial. This is exactly the mechanism in Suzuki's Proposition 3.1, author pp.5–6, now checked for the specified field and elliptic point.

Ottem–Suzuki Lemma 2.4 gives CH0(W_C)=Z. Moving each point of a fibre W times {e'} to the fixed point w0 shows that CH0(W times E) is supported on {w0} times E. Suzuki Theorem 1.1, author p.2, applies to a smooth projective variety whose CH0 is supported on a subvariety of dimension at most three and to codimension p in {3,dim(X)-1}. Both conditions hold for this fourfold in codimension three. Its Walker map is injective on algebraically trivial torsion. The nonzero two-torsion exterior product therefore has nonzero Walker image and is not in the zero-cycle-generated relation N.

The already audited family-converse theorem E.3j applies to this same fourfold, so the indicated example does refute the literal integral biconditional. It does not close or alter the separate general Walker-generation equality.

## Primary-source opening ledger

1. Ottem, J. C., and Suzuki, F. (2020). A pencil of Enriques surfaces with non-algebraic integral Hodge classes. Primary author PDF: https://arxiv.org/pdf/1906.08994 . Opened in full through the web tool and read locally at research/agents/cycles/sources/OttemSuzuki2020.pdf. Checked Lemmas 2.3–2.7, author pp.4–6; Theorem 3.1, pp.6–8; parity equation (1), p.7; and the integral homology class, p.8. Retrieval refs: turn125996541view0 and turn663610137view0.

2. Suzuki, F. (2020). A remark on a 3-fold constructed by Colliot-Thélène and Voisin. Primary author PDF: https://arxiv.org/pdf/1805.01067 . Opened in full through the web tool and read locally at research/agents/cycles/sources/Suzuki2020Remark.pdf. Checked Theorem 1.1, author p.2, and Proposition 3.1 with proof, pp.5–6. Retrieval refs: turn125996541view1 and turn663610137view1.

3. Schoen, C. (2000). On certain exterior product maps of Chow groups. Mathematical Research Letters, 7, 177–194. Primary publisher URL: https://intlpress.com/site/pub/files/_fulltext/journals/mrl/2000/0007/0002/MRL-2000-0007-0002-a004.pdf . The web-tool request returned HTTP 403 and is not counted as a successful web opening. The independently acquired local primary PDF research/agents/cycles/sources/Schoen2000Exterior.pdf was read and its printed p.177 was rendered and visually checked. Exact locator: Theorem (0.2), p.177. Own image: research/agents/frobenius/output/Schoen2000_p177_theorem_crop.png.

This is an independent audit; no shared source fragment was edited.
