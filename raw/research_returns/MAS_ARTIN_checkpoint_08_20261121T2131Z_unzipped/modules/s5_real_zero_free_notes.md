# The real Hecke gate: an explicit endpoint part

Date: 21 November 2026. Author/checker: GPT-6 Astra Pro, /root/s5_audit, MAS_ARTIN. Effort is inherited and not externally exposed.

## Result and exact scope

s5_real_zero_free.tex, MA-RB-001, proves under the stipulated Dirichlet theorem A that B has no real zero in (0,δ_L) ∪ (1−δ_L,1), where δ_L=min(1/2,(√5−1)^2/(1+(log Δ_L)/2)). No general Hecke GRH hypothesis M is used. The central compact interval remains unresolved.

The proof does not presume Artin holomorphy for the five-dimensional representations. At the particular off-center real point, C≠0 by A and L_W=B/C is holomorphic. Also L_(Wη)=ζ_F/ζ is holomorphic because ζ(σ)<0 on (0,1). Calegari supplies the already established four- and six-dimensional holomorphy. Thus any zero of B has multiplicity at least five in ζ_L.

The completed ζ_L has signature (0,60). The module retains the exact 60(ψ(σ)−log(2π)) term, fixes the Hadamard exponential constant using the functional equation at 0 and 1, and proves ψ(x)≤log x from the gamma integral. The resulting inequality 5/(t+d)≤1/t+1+(log Δ_L)/2 gives the stated constant by an explicit permitted choice of t. The upper endpoint interval reflects through the exact quadratic Hecke completion; F and H have signatures (2,2) and (4,4).

## Remaining approach tested

Heilbronn's normal-extension descent theorem applies to simple real zeros. Its exact Theorem 1, printed page 870, was freshly inspected in the primary four-page PDF. In this family it would force a simple real zero of ζ_L into ζ_E, where A excludes it off center. The hypothetical B zero already has multiplicity at least five and does not meet that simplicity premise. The formal order vector (0,0,0,0,1,0,0) respects all induced-character nonnegative order tests and has regular multiplicity five and quadratic-subfield order zero. It is only a compatibility test, not an arithmetic counterexample.

The needed completed Hadamard identity is derived in the new proof. The standard analytic continuation/functional equation and unconditional fixed-strip bounds are the existing NT-Z10/MT-M18 inputs, with Ramakrishnan–Valenza's exact locators retained. No new external zero-free theorem, unverified preprint, or recomputed finite representation certificate is used.

## Review state

The author read the complete written proof after creation, then corrected the optimization paragraph to derive Δ_L>1 from the exact displayed archimedean formula rather than importing an additional discriminant bound. The entire argument, including that correction, has passed the author check. The parent subsequently read the whole proof independently and reported a pass, including the signed orders, Hadamard constant, archimedean bound, optimizer, signatures, and reflection. Its separate events record that independent reading; the author events here remain labeled as author checks.
