# Root audit of B.082: universal polynomial-tensor criterion

Date: 19 November 2026, 18:20–18:22 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Targeted proof check and independent chain calculation, not a finite computational certificate.

We read the complete draft in two bounded chunks. We also opened the original Stacks Project section 10.107, tag 04VM, and checked Lemmas 10.107.10–11 and Remark 10.107.12, including the displayed finite matrix relations. Retrieval: https://stacks.math.columbia.edu/tag/04VM; root reference turn961101675view0. We claim no priority for the epimorphism criterion or the standard homological algebra.

## Scope and result

PASS for all unital inclusions of commutative rings R⊂S. The coefficient ring C and coefficient-value module E are defined from that inclusion before any tensor power of Ω is used. The resulting matrix test, K1 and K2 vanishing, and the two explicit δ0 coefficient tests are necessary and sufficient for the well-determined coaddition and comultiplication requested in original B.2(c). Thus this closes that original task row. No uniformly terminating algorithm for arbitrary infinite rings, elementary classification of all base rings, or automatic higher plethystic coherence is asserted or required by this result.

## Independent checks

1. The matrix certificate is exactly the condition c⊗1=1⊗c for each c∈C. Removing the zero-indexed row and column from the finite balancing certificate gives Y'M'Z'=m00−c. The block diagonal matrix diag(−M',m00), with a final coordinate 1 on both sides, gives c and retains both required products over R. This supplies the last omitted elementary step in the opened source.

2. Epicness gives C⊗(C/R)=0. Since E is a quotient of (C/R)[X] and also of F=C[X], right exactness gives F⊗E=E⊗F=E⊗E=0. No flatness is used.

3. The free resolution on the underlying set, iterated on kernels, is functorial. Its generators and boundaries have finite support even when the modules are infinite. Tensoring two such resolutions computes Tor by the usual bounded-below free double-resolution argument.

4. The two-column complex L has H0=ker(F→E)=Ω and no other homology. Its only negative term is free Q0 in degree −1; the surjection L0→Q0 splits. Removing that contractible summand leaves a nonnegative projective resolution. Therefore L⊗L computes Ω⊗^LΩ without a convergence or flatness assumption.

5. Multiplication by (−1)^(p1 b) on the summand with first column p1 and second vertical degree b identifies L⊗L with the three-column complex. We checked the first and second vertical and horizontal signs individually. Its differential is D=d+(−1)^q h, its horizontal square is zero, and the vertical maps commute with h.

6. For q=0,1, choosing dw=(−1)^(q+1)h0z and taking [(−1)^(q+1)h1w] modulo im b_(q+1) defines δq independently of both choices. Replacing z by z+dv changes w by the stated signed h0v; h1h0=0 removes that change. Replacing w by a cycle changes the target by im b.

7. A degree-zero total cycle is precisely a triple with dx1=−h0x0 and dx2=h1x1. This proves im θ2=ker δ0. Vanishing H_(−1) supplies a lift of every vertical cycle in column two, degree one, and hence proves δ0 is onto. Thus coker θ2=T1.

8. Removing a zero edge component identifies the next quotient of ker θ2 with ker b1/im a1. Removing that component leaves a pure column-two degree-two cycle. Its total boundaries are exactly im b2 and the lifts of δ1 from ker a1. Hence 0→K2→ker θ2→K1→0, with K2=coker δ1. We checked the boundary signs in total degree one directly.

9. The coaddition and comultiplication arrays are the actual coefficients of F(X+Y) and F(XY). Vanishing δ0 gives existence; vanishing K1,K2 gives uniqueness. Conversely uniqueness includes the zero polynomial and therefore forces injectivity of θ2. B.064 supplies the already checked necessary epicness and the fact that every coefficient lies in C.

10. If C is flat, the positive Tor groups containing F vanish, recovering the B.080 exact sequence. The author's fixed δ0 convention is the negative of the usual B.080 connecting map under one standard resolution identification; the vanishing tests and all exactness statements are unchanged. The final text must state the convention rather than claim an unqualified equality of signed maps.

Only Tor degrees one and two and free boundaries through vertical degree three enter the tests. The infinite universal quantifiers in the coefficient-value module and in the family of coefficient vectors are retained explicitly. This is an arithmetic and syzygy criterion, not an asserted finite algorithm.

## Final consistency calculations checked

We also read the added sign comparison and both explicit examples in full. For the nonflat forest, the Tor rows split by monic-basis index pairs; their exact sequences give K1=K2=0 and T1=(S/R)^16 without assuming the positive Tor groups of S vanish. The two identities for Q=X^4+X^2 give precisely zero low-low coefficient obstruction. For the flat cusp, E contains K/V as a split summand. The two long exact sequences identify Tor2(K/V,K/V) with the kernel of V⊗V→K⊗V; the displayed β⊗1−1⊗β is detected nontrivially after residue reduction. Its split image is the previously established Ω tensor kernel. These are algebraic consistency calculations, not additional finite program certificates.
